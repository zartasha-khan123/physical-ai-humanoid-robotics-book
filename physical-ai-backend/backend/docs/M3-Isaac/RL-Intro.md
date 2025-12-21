
---

## **📄 03-RL-Intro.md**
```md
---
title: "Chapter 3 — Reinforcement Learning for Humanoids"
---

# RL Introduction

Reinforcement Learning (RL) allows robots to learn locomotion, balancing, and manipulation.

## Isaac Gym vs Isaac Sim

| Feature | Isaac Gym | Isaac Sim |
|--------|-----------|-----------|
| Fast parallel RL | Yes | No |
| High fidelity | Medium | High |
| Humanoid learning | Excellent | Excellent |

## PPO (Proximal Policy Optimization)

Most humanoid locomotion policies use PPO.

Common observations:
- Joint positions
- Joint velocities
- Ground contact
- IMU data

Common rewards:
- Forward velocity
- Balance
- Smooth joint torque

## Training Loop Example

```python
obs = env.reset()

for step in range(max_steps):
    action = policy(obs)
    next_obs, reward, done = env.step(action)
    policy.update(obs, action, reward)
    obs = next_obs



---

## **📄 04-Labs.md**
```md
---
title: "Labs — Isaac Sim & RL"
---

# Lab 1 — Build a Humanoid Scene
- Add ground plane  
- Import humanoid  
- Add camera + Lidar  
- Add physics components  

# Lab 2 — ROS2 Camera Stream
- Enable ROS bridge  
- Subscribe to depth + RGB topics  
- Visualize in RViz  

# Lab 3 — Humanoid Joint Control Node
Write a node that moves the robot’s leg using ROS2 trajectory commands.

# Lab 4 — RL Policy Deployment
- Train a walking RL policy  
- Load model in Isaac  
- Run simulation  

---
title: "Assignments — Module 3"
---

# Assignment 1 — Build a Full Humanoid Simulation
- Humanoid  
- Sensors  
- Joint control  
- Terrain  

# Assignment 2 — ROS2 Integration
Publish:
- IMU  
- Camera  
- Lidar  

# Assignment 3 — RL Training
Train a simple humanoid standing + balancing policy.
