# Robot-Vision
Autonomous 6-DOF robotic arm simulation with YOLOv8 object detection and RViz2 visualization using ROS2 &amp; Gazebo

# ME6 Robotic Arm — Autonomous Inspection System

A ROS2-based simulation of the ME6 6-DOF robotic arm performing 
an autonomous inspection mission using YOLOv8 object detection.

## Overview
The robot moves through 3 target positions, captures images, 
runs real-time object detection, and makes decisions based on 
what it detects in the environment.

## Features
- 6-DOF robotic arm simulation in Gazebo Classic
- Inverse Kinematics (IK) for precise positioning
- YOLOv8 real-time object detection
- Smart decision-making based on detected objects
- Live visualization in RViz2

## Decision Logic
| Detected Object | Action |
|----------------|--------|
| Person, Cat, Dog | Move Away |
| Bottle, Cup | Approach |
| Other | Log & Continue |

## Tech Stack
- ROS2 Humble
- Gazebo Classic
- RViz2
- YOLOv8 (Ultralytics)
- OpenCV & CV Bridge

## Run
```bash
ros2 launch me6_description gazebo.launch.py
python3 dual_image_publisher.py
rviz2
```

## Inspection Positions
| Position | X | Y | Z |
|----------|-----|------|------|
| Left | 0.25 | 0.15 | 0.28 |
| Center | 0.05 | -0.05 | 0.22 |
| Right | 0.28 | -0.20 | 0.18 |
