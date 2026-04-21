# Daily Reflection Tree - DeepThought Assignment

## Overview
A deterministic reflection tool that guides employees through structured end-of-day reflection across three psychological axes:
- **Axis 1: Locus** (Victim vs Victor)
- **Axis 2: Orientation** (Contribution vs Entitlement)
- **Axis 3: Radius** (Self-Centrism vs Altrocentrism)

## Structure
```
/tree/
  reflection-tree.json          - The complete decision tree data
  tree-diagram.md               - Visual Mermaid diagram
/agent/
  reflection_agent.py           - Python implementation
  requirements.txt              - Dependencies
/transcripts/
  persona-victim-transcript.md  - Sample run (victim/entitled/self-centric)
  persona-victor-transcript.md  - Sample run (victor/contributing/altrocentric)
write-up.md                     - Design rationale and psychology sources
```

## How to Run the Agent (Part B)

### Prerequisites
- Python 3.8+

### Installation
```bash
pip install -r agent/requirements.txt
```

### Run the Reflection Session
```bash
python agent/reflection_agent.py
```

The agent will:
1. Load the tree from `tree/reflection-tree.json`
2. Walk you through the reflection questions
3. Branch based on your answers (deterministically)
4. Provide personalized reflections
5. Generate a summary of your session

## Design Principles
- **No LLM at runtime** - Fully deterministic
- **Fixed options only** - No free text input
- **Psychologically grounded** - Based on research (Rotter, Dweck, Maslow, etc.)
- **Non-judgmental** - Guides reflection without moralizing
- **Sequential flow** - Each axis builds on the previous

## Tree Statistics
- **Total nodes**: 41
- **Question nodes**: 14 (with fixed options)
- **Decision nodes**: 14 (internal routing)
- **Reflection nodes**: 8 (insights/reframes)
- **Bridge nodes**: 2 (axis transitions)
- **Start/End nodes**: 2
- **Summary node**: 1
