---
title: "Module 1 — Introduction to ROS 2 Architecture"
---

## 1. What is ROS 2?

ROS 2 (Robot Operating System 2) is an open-source framework used to build robotics applications.  
It provides communication tools, hardware abstraction, simulation integration, and libraries for building robot intelligence.

ROS 2 is used in:

- Humanoid robotics  
- Industrial robotics  
- Autonomous vehicles  
- Service robots  
- Drone systems  

---

## 2. Why ROS 2 for Physical AI & Humanoid Robotics?

Humanoid robotics requires:
- Real-time control  
- Reliable communication  
- Sensor fusion  
- AI integration  
- Distributed systems  

ROS 2 is designed exactly for this.

### Key Improvements over ROS 1
| ROS 1 | ROS 2 |
|------|-------|
| Single computer | Multi-robot, distributed |
| Custom message transport | DDS (industry-standard middleware) |
| Not real-time safe | Real-time capable |
| Python/C++ only | Supports more languages |
| Weak security | Built-in security |

---

## 3. ROS 2 Architecture Overview

ROS 2 is built on:

- **DDS (Data Distribution Service)** → communication layer  
- **Nodes** → programs that do work  
- **Topics** → publish/subscribe messaging  
- **Services** → request-response  
- **Actions** → long-duration tasks  
- **Parameters** → dynamic settings  
- **Packages** → reusable components  

Below is a conceptual diagram:

+----------------------+
| ROS 2 Master |
| (DDS Discovery) |
+----------------------+
/ |
/ |
+-----+ ++ +------+
|Node | |Node| |
+-----+ +----+-------+
Publish Subscribe
\ /
+----Topic-----+ 

---

## 4. Example ROS 2 Node (Python)

```python
import rclpy
from rclpy.node import Node

class MinimalNode(Node):
    def __init__(self):
        super().__init__("minimal_node")
        self.get_logger().info("ROS 2 node running!")

def main(args=None):
    rclpy.init(args=args)
    node = MinimalNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
