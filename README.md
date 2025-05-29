# THESIS AISL-1-2425-2
AQUA-μ: A Portable Microplastic Detection System using Object Detection Algorithm 

### Some few short things to say
GitHub can be overwhelming at first, especially if you have never used this platform before ***like actually***, but it is possibly the best way for us to collaborate in terms of coding, software, etc. With that, I recommend taking the time reading, learning, and trying the following guides to get started with GitHub:

1. [The Ultimate Git & GitHub Guide: From Beginner to Advanced](https://dev.to/parnab03/the-ultimate-git-github-guide-from-beginner-to-advanced-2aoh)
2. [Start your journey/Learn the basics of GitHub](https://docs.github.com/en/get-started/start-your-journey)
3. [GitHub Skills](https://skills.github.com/)

### Goals of this GitHub Repo
1. Let everyone be on the same page in terms of hardware and software components
2. Collaborate on the software (object detection algorithm or YOLOv8)
3. Track all changes made ***(very important)***
4. Documentation
5. Learn, learn, learn
6. ***Give us confidence that we absolutely know what we are doing***

### THESIS GitHub Repo Checklist
- [ ] Hardware set-up
  - Setting up the Raspberry Pi 5
  - Setting up the AI Kit
  - Setting up the Arducam IMX519
- [ ] THESIS WORKFLOW
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

### Raspberry Pi 5
Setting up the RPi requires having the peripherals and microSD ready beforehand. Peripherals include the mouse, keyboard, and monitor via micro USB to HDMI/DP port. The microSD is for the storage of the RPi.

We also need to install the operating system for RPi, which can be done by installing [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC. Then, connect the microSD and open the Raspberry Pi Imager. We can now choose Raspberry Pi 5 as the device and Raspberry Pi OS (64-bit) as the operating system.

~~However, I realized I am going to waste lots of time if I am going to write the all the steps again, so~~ the official guide made by Raspberry Pi is listed here:

https://www.raspberrypi.com/documentation/computers/getting-started.html

An important detail from the guide that can be listed here is the use of **Raspberry Pi Connect**. It allows us to remotely control the RPi without using any peripherals. Straight controls from the PC!

### Raspberry Pi AI Kit

Before installing the AI Kit, it was recommended to install the official active cooler on the RPi to maximize the performance of the system

### Arducam IMX519



## THESIS WORKFLOW
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
