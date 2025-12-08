
---

## **📄 03-Multimodal-HRI.md**
```md
---
title: "Chapter 3 — Human Robot Interaction (HRI)"
---

# Multimodal HRI

Robots must understand:
- Speech  
- Gestures  
- Gaze direction  
- Objects  
- Emotions  
- Spatial cues  

## Example Inputs

| Modality | Example |
|---------|---------|
| Vision | detecting objects, poses |
| Audio | speech commands |
| Touch | haptic feedback |
| IMU | balancing |

## Grounding Model Example

A grounding model maps **vision tokens** → **actions**.

```json
{
  "vision": ["cup", "table"],
  "language": "pick up the cup",
  "action": "grasp(cup)"
}
