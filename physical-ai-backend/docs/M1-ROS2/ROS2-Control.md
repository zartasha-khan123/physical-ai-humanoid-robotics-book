
---

# 📘 **M1-ROS2 / 05-ROS2-Control.md**

```md
---
title: "ROS 2 Control — Hardware & Command Interfaces"
---

## 1. What is ros2_control?

It is the framework used for:

- Motor control  
- Humanoid joint control  
- PID loops  
- Hardware interfaces  
- Realtime motion  

---

## 2. Components

| Component | Purpose |
|----------|----------|
| Controller Manager | Loads controllers |
| Hardware Interface | Talks to motors |
| Controllers | Send commands |

---

## 3. Control Flow


---

## 4. Example Config (YAML)

```yaml
controller_manager:
  ros__parameters:
    update_rate: 100
    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster
