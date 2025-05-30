# THESIS AISL-1-2425-2
AQUA-μ: A Portable Microplastic Detection System using Object Detection Algorithm 

### Some few short things to say
GitHub can be overwhelming at first, especially if you have never used this platform before ***like actually***, but it is possibly the best way for us to collaborate in terms of coding, software, etc. With that, I recommend taking the time reading, learning, and trying the following guides to get started with GitHub:

1. [The Ultimate Git & GitHub Guide: From Beginner to Advanced](https://dev.to/parnab03/the-ultimate-git-github-guide-from-beginner-to-advanced-2aoh)
2. [Start your journey/Learn the basics of GitHub](https://docs.github.com/en/get-started/start-your-journey)
3. [GitHub Skills](https://skills.github.com/)

Also, it is important to get the basics of Python. It makes sense why **<ins>Raspberry Pi</ins>** is called like that since Python is its foundation.

Here is a quick guide, just the super basics, in 10 minutes.

[![Learn Python in Less than 10 Minutes for Beginners (Fast & Easy)](https://img.youtube.com/vi/fWjsdhR3z3c/0.jpg)](https://www.youtube.com/watch?v=fWjsdhR3z3c)

This one is a more detailed guide but guaranteed to actually learn the essentials in Python. (There are 15 parts)

[Introduction to Python 3 (basics) - Learning to Program with Python 3](https://pythonprogramming.net/introduction-learn-python-3-tutorials/)

Lastly, of course, we have to grasp **<ins>Computer Vision</ins>.** It is expected of us to be a master of this topic, so we can answer questions and explain concepts with ease. It is a hard topic to learn, especially when starting from the ground up. But yeah, **<ins>we absolutely got this.</ins>**

There are prerequisites for Computer Vision, such as Deep Learning, Artificial Neural Networks, and many more. I absolutely think we have to study all of these concepts really well.

In the end, this will be our forte, something that is supposed to combine all the learnings we had studying this course. Ironically, we chose a topic that was never taught to us, but it was taught to Computer Engineering students as an elective.

### Goals of this GitHub Repo
1. Let everyone be on the same page in terms of hardware and software components
2. Collaborate on the software (object detection algorithm or YOLOv8)
3. Track all changes made ***(very important)***
4. Anyone can recreate/implement this project by following this
5. Documentation
6. Learn, learn, learn
7. ***Give us confidence that we absolutely know what we are doing***

### THESIS GitHub Repo Checklist
- [x] Hardware set-up
  - Setting up the Raspberry Pi 5
  - Setting up the AI Kit
  - Setting up the Arducam IMX519
- [ ] Project Workflow
  - Gathering of samples
  - Creating custom dataset
  - Training the object detection algorithm (YOLOv8) using Google Colab
  - Deploying on the Raspberry Pi 5 with AI Kit add-on
  - Evaluating the performance of the system
- [ ] Add pictures and codes

## Hardware set-up
The following equipment/materials was used:
* Raspberry Pi 5 8GB RAM
* 27W USB-C power supply
* 128 GB microSD
* Raspberry Pi AI Kit
* Raspberry Pi Active Cooler
* Arducam IMX519
* Small screwdriver
* Screws
* PC

### Raspberry Pi 5
Setting up the RPi requires having the peripherals and microSD ready beforehand. Peripherals include the mouse, keyboard, and monitor via micro USB to HDMI/DP port. The microSD is for the storage of the RPi.

We also need to install the operating system for RPi, which can be done by installing [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC. Then, connect the microSD and open the Raspberry Pi Imager. We can now choose Raspberry Pi 5 as the device and Raspberry Pi OS (64-bit) as the operating system.

~~However, I realized I am going to waste lots of time if I am going to write the all the steps again, so~~ the official guide made by Raspberry Pi is listed here:

[Getting started with your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)

An important detail from the guide that can be listed here is the use of **Raspberry Pi Connect**. It allows us to remotely control the RPi without using any peripherals. Straight controls from the PC!

### Raspberry Pi AI Kit

The full guide for installing the AI Kit can be found here:

[AI Kit Documentation](https://www.raspberrypi.com/documentation/accessories/ai-kit.html)

Before installing the AI Kit, it was recommended to install the official active cooler on the RPi to maximize the performance of the system, so this is the guide for installing the active cooler: 

[Active Cooler](https://datasheets.raspberrypi.com/cooling/raspberry-pi-active-cooler-product-brief.pdf)

I remember watching a Youtube video to ensure I correctly installed the Active Cooler since it says in the documentation that it should not be removed after sticking the thermal pads to the board. 

Afterwards, I referred to the official AI Kit documentation to install the AI Kit, which involved using spacers, screws, connecting the ribbon cable, and carefully ensuring the GPIO pins are inserted well.

Setting up the software portion of the AI Kit involves entering (copy pasting) code into the terminal, which if done correctly, it will allow us to successfully use the AI Kit. Again, it is useless to write everything from the official documentation since it is already written there. The following guide helps us get started with the software for the AI Kit:

[Getting Started on AI Kit and AI HAT+ software](https://www.raspberrypi.com/documentation/computers/ai.html)

### Arducam IMX519

Moving on to the camera module, the installation guide is written here:

[Arducam Hardware Quick Start Guide](https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/Quick-Start-Guide/#22pin-top-contact-csi-connector)

In essence, it teaches the correct orientation for connecting the ribbon cable towards the camera and the RPi. Next, this is the software guide for Arducam IMX519:

[Software Guide for IMX519 Autofocus Camera](https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/16MP-IMX519/#step-1-download-the-bash-scripts)

You may have noticed that it always start at installing certain dependencies or packages when reading the guides for the software portion. Softwares rely on these dependencies or packages to function properly. Developers write these to save time and effort rather than coding everything from scratch. All we have to do is run them.

After connecting everything, we can move on to testing whether the components work. I gathered the codes from the guides that will allow us to test certain components.

```
rpicam-hello -t 10s
```

Test whether the camera works. It is something similar to printing "Hello World!"

```
rpicam-hello -t 0 --post-process-file /usr/share/rpi-camera-assets/hailo_yolov8_inference.json
```

Run the sample YOLOv8 object detection model

### Finished Hardware set-up

At this point, we must have correctly installed and set up the RPi 5, RPi AI Kit, and RPi Active Cooler. We also installed the necessary dependencies and tested whether the components function correctly. Don't forget to verify the versions from the logs.

Typically, the hardware set-up is a one-time thing, and 99.99% of the time the process is smooth. As stated earlier, there are goals for this GitHub Repo, such as documentation, recreateable steps, and most importantly, <ins>***everyone must know the process from the beginning until the end.***</ins> 

## Project Workflow
* Gathering of samples
* Creating custom dataset
* Training the object detection algorithm (YOLOv8) using Google Colab
* Deploying on the Raspberry Pi 5 with AI Kit add-on
* Evaluating the performance of the system

### Gathering of samples

We gathered microplastics from the shore of Manila Bay and Dolomite Beach. Others were artificially created by cutting plastic wrappers into tiny pieces. 

**Not much to say about it, but I will come back on this section soon.**

### Creating custom dataset

After gathering the samples, we took hundreds of pictures of the samples using the Raspberry Pi 5 and Arducam IMX519. Then, we used Roboflow to create the custom dataset. I will thoroughly explain each step moving forward.

Taking pictures of the samples

Code Block Example:

```
git status
```

Picture -> Import -> Annotate -> Export

### Training the object detection algorithm (YOLOv8) using Google Colab

Show steps on how to train

List important parameters and explain what they do

Exporting .onnx

### Deploying on the Raspberry Pi 5 with AI Kit add-on

WSL

Converting .onnx to .hef

Running the .hef on RPi 5

File transfer between RPi and PC

### Evaluating the performance of the system

METRICS

Precision, Recall, mAP, F1 score
