
---

# 📘 **M1-ROS2 / 03-ROS2-Packages.md**

```md
---
title: "ROS 2 Packages & Workspace Structure"
---

## 1. What is a Package?

A package is the basic unit of software in ROS 2.

A package can include:
- Nodes  
- Launch files  
- URDF robot models  
- Config files  
- AI models  

---

## 2. Workspace Structure


---

## 3. Creating a Package


---

## 4. Launch Files

Launch files start multiple nodes together.

Example:
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package="demo", executable="talker"),
        Node(package="demo", executable="listener")
    ])
