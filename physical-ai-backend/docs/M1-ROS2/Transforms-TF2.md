
---

# 📘 **M1-ROS2 / 04-Transforms-TF2.md**

```md
---
title: "ROS 2 TF2 — Coordinate Transforms"
---

## 1. Why TF2?

Robots operate in 3D space.  
Every sensor, joint, and link needs a consistent reference frame.

TF2 solves:
- Robot orientation  
- Position of links  
- Sensor alignment  
- Mapping & localization  

---

## 2. Common Frames

| Frame | Meaning |
|-------|---------|
| base_link | robot body |
| odom | drift-free pose |
| map | world reference |
| camera_link | camera pose |

---

## 3. TF Tree Example


---

## 4. Broadcasting TF

```python
t = TransformStamped()
t.header.frame_id = "base_link"
t.child_frame_id = "camera_link"
