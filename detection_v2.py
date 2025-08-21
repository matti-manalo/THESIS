import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
import numpy as np
import hailo
from hailo_apps.hailo_app_python.core.common.buffer_utils import get_caps_from_pad, get_numpy_from_buffer
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp


class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        self.label_counts = {}           # per label
        self.total_count = 0             # total detections
        self.microplastics_count = 0     # grouped microplastics
        self.non_microplastics_count = 0 # grouped non-microplastics


def app_callback(pad, info, user_data):
    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK

    # Get the detections from the buffer
    roi = hailo.get_roi_from_buffer(buffer)
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

    # Define allowed labels
    valid_labels = {
        "black fragment",
        "blue fragment",
        "film",
        "green fragment",
        "grey fragment",
        "orange fragment",
        "pebble",
        "red fragment",
        "shell",
        "teal fragment",
        "white fragment",
        "white pellet",
        "yellow fragment",
    }

    # Define groups
    microplastics_labels = {
        "black fragment", "blue fragment", "green fragment", "grey fragment",
        "orange fragment", "red fragment", "teal fragment",
        "white fragment", "yellow fragment", "white pellet", "film"
    }
    non_microplastics_labels = {"shell", "pebble"}  # ✅ moved pebble here

    # Reset counts for this frame
    user_data.label_counts = {label: 0 for label in valid_labels}
    user_data.total_count = 0
    user_data.microplastics_count = 0
    user_data.non_microplastics_count = 0

    # Count detections
    for detection in detections:
        label = detection.get_label()
        if label in valid_labels:
            user_data.label_counts[label] += 1
            user_data.total_count += 1

            if label in microplastics_labels:
                user_data.microplastics_count += 1
            elif label in non_microplastics_labels:
                user_data.non_microplastics_count += 1

    return Gst.PadProbeReturn.OK


def update_text_overlay(pipeline, user_data):
    overlay = pipeline.get_by_name("text_overlay")
    if overlay is not None:
        if user_data.total_count > 0:
            lines = [f"Total: {user_data.total_count}", ""]

            # Microplastics section
            if user_data.microplastics_count > 0:
                lines.append(f"Microplastics: {user_data.microplastics_count}")
                for label, count in user_data.label_counts.items():
                    if count > 0 and label not in {"shell", "pebble"}:  # exclude non-micro labels
                        lines.append(f"{label}: {count}")
                lines.append("")

            # Non-microplastics section
            if user_data.non_microplastics_count > 0:
                lines.append(f"Non-microplastics: {user_data.non_microplastics_count}")
                for label, count in user_data.label_counts.items():
                    if count > 0 and label in {"shell", "pebble"}:
                        lines.append(f"{label}: {count}")

            text = "\n".join(lines)
        else:
            text = "No detections"

        overlay.set_property("text", text)
    return True


if __name__ == "__main__":
    user_data = user_app_callback_class()
    app = GStreamerDetectionApp(app_callback, user_data)
    GLib.timeout_add(100, update_text_overlay, app.pipeline, user_data)
    app.run()
