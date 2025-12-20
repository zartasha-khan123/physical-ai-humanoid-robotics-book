
---

## **📄 02-Voice-to-Action.md**
```md
---
title: "Chapter 2 — Voice-to-Action Systems"
---

# Voice → Intent → Action

Pipeline:

1. Speech-to-Text (ASR)
2. Intent classifier (LLM)
3. VLA Planner generates structured actions
4. Humanoid executes

Example:

User says: **"Turn on the lights and sit down."**

LLM Output (structured):

```json
{
  "action_sequence": [
    {"type": "toggle_switch", "target": "light_switch"},
    {"type": "move_to", "target": "chair"},
    {"type": "sit"}
  ]
}
