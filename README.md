# THESIS AISL-1-2425-2
AQUA-μ: A Portable Microplastic Detection System using Object Detection Algorithm 

### A short few things to say
GitHub can be overwhelming at first, especially if you have never used this platform before ***like actually***, but it is possibly the best way for us to collaborate in terms of coding, software, etc. With that, I recommend taking the time reading, learning, and trying the following guides to get started with GitHub:

1. https://dev.to/parnab03/the-ultimate-git-github-guide-from-beginner-to-advanced-2aoh
2. https://skills.github.com/
3. https://docs.github.com/en/get-started/start-your-journey

### Goals of this GitHub Repo
1. ***Give us confidence that we absolutely know what we are doing***
2. Let everyone be on the same page in terms of hardware and software components
3. Collaborate on the software (object detection algorithm or YOLOv8)
4. Track all changes made ***(very important)***
5. Documentation
6. Learn, learn, learn

### THESIS GitHub Repo Checklist
- [ ] Hardware set-up
  - Setting up the Raspberry Pi 5
  - Setting up the AI Kit
  - A few reminders for myself:
    - List down everything I did
    - What I did to complete the set-up
    - I installed the cooler
    - Creating profiles
    - Basic camera commands and AI kit setup from Hailo
- [ ] Project workflow
  - Gathering of samples
  - Creating custom dataset
  - Training the object detection algorithm (YOLOv8) using Google Colab
  - Deploying on the Raspberry Pi 5 with AI Kit add-on
  - Evaluating the performance of the system
- [ ] Add pictures and codes


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
