
---

# 📘 **M1-ROS2 / 02-Nodes-Topics-Services.md**

```md
---
title: "ROS 2 Nodes, Topics, and Services"
---

## 1. ROS 2 Nodes

A **Node** is a process that performs computation.

Examples:
- A node reading LiDAR  
- A node controlling motors  
- A node running a neural network  

Nodes discover each other automatically through DDS.

---

## 2. Topics (Publish / Subscribe)

Topics allow continuous data flow.

Examples:
- `/scan` → LiDAR distances  
- `/cmd_vel` → velocity commands  
- `/image_raw` → camera images  

### Publisher Example:

```python
self.publisher = self.create_publisher(String, "status", 10)

self.subscription = self.create_subscription(
    String,
    "status",
    self.listener_callback,
    10
)
response = client.call(request)
return Trigger.Response(success=True, message="Reset done")
