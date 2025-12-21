---
title: "Module 3 — Isaac Sim, Robotics Simulation & RL"
---

# Module 3 Overview

This module focuses on **high-fidelity robotics simulation using NVIDIA Isaac Sim**, including humanoid control, ROS2 integration, domain randomization, synthetic data generation, and reinforcement learning pipelines.

After this module, you will be able to:

- Understand Isaac Sim’s physics engine, articulations, and action graphs.
- Build complete humanoid robot simulations.
- Integrate ROS2 with Isaac for perception + control loops.
- Train RL-based locomotion, navigation, and manipulation.
- Create synthetic datasets for robotics and AI training.

This is the most *critical* module because your **Quarter 2 Capstone** depends heavily on simulation + RL.

---
title: "Chapter 1 — Isaac Sim Basics"
---

# Introduction to Isaac Sim

Isaac Sim is NVIDIA’s high-fidelity physics simulator designed for **robotics, humanoids, and embodied AI**.

## Key Features

- PhysX 5 engine for realistic collisions and articulation.
- USD scene graph for building worlds.
- Native ROS2 bridges.
- Domain randomization for robust training.
- GPU-accelerated synthetic sensor pipelines.

## Installing Isaac Sim

You can install Isaac Sim via:
- Omniverse Launcher  
- Docker Container  
- Conda / CLI  

Example (Linux):

```bash
./isaac-sim.sh
