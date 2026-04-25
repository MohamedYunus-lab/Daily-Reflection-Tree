# 🌳 Daily Reflection Tree

> A deterministic reflection tool for structured end-of-day self-awareness

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DeepThought](https://img.shields.io/badge/DeepThought-Fellowship-orange.svg)](https://github.com/DT-CultureTech)

## 🎯 Overview

A deterministic reflection tool that guides employees through structured end-of-day reflection across three psychological axes:

### The Three Axes

| Axis | Spectrum | Psychology |
|------|----------|------------|
| 🧠 **Locus** | Victim ↔ Victor | Rotter (1954), Dweck (2006) |
| 💡 **Orientation** | Entitlement ↔ Contribution | Campbell (2004), Organ (1988) |
| 🌍 **Radius** | Self-centric ↔ Altrocentric | Maslow (1969), Batson (2011) |

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

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/MohamedYunus-lab/Daily-Reflection-Tree.git

# Navigate to the project
cd Daily-Reflection-Tree

# Run the agent
python agent/reflection_agent.py
```

The agent will guide you through reflection questions and provide personalized insights based on your responses.

## 📊 Tree Statistics

| Metric | Count |
|--------|-------|
| **Total Nodes** | 41 |
| **Question Nodes** | 14 |
| **Decision Nodes** | 14 |
| **Reflection Nodes** | 8 |
| **Bridge Nodes** | 2 |
| **Summary Templates** | 18 |

## ✨ Key Features

- ✅ **No LLM at runtime** - Fully deterministic and predictable
- ✅ **Fixed options only** - No free text input
- ✅ **Psychologically grounded** - Based on 6 research papers
- ✅ **Non-judgmental** - Guides reflection without moralizing
- ✅ **Sequential flow** - Each axis builds on the previous
