
---

## **📄 02-Isaac-ROS-Integration.md**
```md
---
title: "Chapter 2 — ROS2 Integration with Isaac"
---

# Isaac Sim + ROS2

Isaac Sim has a built-in ROS2 bridge that publishes sensor data and receives control commands.

## Publishing Camera Data

```json
{
  "ros": {
    "image_topic": "/camera/color/image_raw",
    "depth_topic": "/camera/depth"
  }
}
ros2 launch isaac_ros_examples pub_sub_demo.launch.py
ros2 topic pub /joint_trajectory trajectory_msgs/JointTrajectory "
joint_names: ['hip_left', 'knee_left']
"
