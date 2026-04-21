# Quick Start Guide

## What You Have

This repository contains a complete implementation of the Daily Reflection Tree assignment for DeepThought:

### Part A (Required) ✅
- **Tree Data**: `tree/reflection-tree.json` - Complete decision tree with 41 nodes
- **Visual Diagram**: `tree/tree-diagram.md` - Mermaid diagram showing all paths
- **Design Write-up**: `write-up.md` - 2-page rationale with psychology sources

### Part B (Optional) ✅
- **Working Agent**: `agent/reflection_agent.py` - Python implementation
- **Sample Transcripts**: Two personas showing different paths through the tree
  - `transcripts/persona-victor-transcript.md` (internal/contribution/altrocentric)
  - `transcripts/persona-victim-transcript.md` (external/entitlement/self-centric)

## Running the Agent

### Step 1: Verify Python
```bash
python --version
# Should show Python 3.8 or higher
```

### Step 2: Run the Reflection Session
```bash
python agent/reflection_agent.py
```

### Step 3: Answer the Questions
The agent will:
1. Greet you and start the session
2. Ask questions with numbered options
3. Branch based on your answers (deterministically)
4. Show reflections at key points
5. Generate a personalized summary

### Example Interaction
```
How would you describe today in one word?

  1. Productive
  2. Challenging
  3. Frustrating
  4. Rewarding
  5. Overwhelming

Your choice (enter number): 1
```

## Understanding the Tree

### The Three Axes

1. **Axis 1: Locus** (Victim vs Victor)
   - Do you see your agency in outcomes?
   - Based on Rotter's Locus of Control + Dweck's Growth Mindset

2. **Axis 2: Orientation** (Contribution vs Entitlement)
   - Are you giving or keeping score?
   - Based on Campbell's Entitlement + Organ's Organizational Citizenship

3. **Axis 3: Radius** (Self-Centrism vs Altrocentrism)
   - How wide is your circle of concern?
   - Based on Maslow's Self-Transcendence + Batson's Perspective-Taking

### How Branching Works

The tree uses **decision nodes** to route based on your answers:

```
Question: "How would you describe today?"
Answer: "Productive" → Routes to "agency-high" path
Answer: "Frustrating" → Routes to "agency-low" path
```

Every path is **deterministic** - same answers always lead to the same reflection.

## Key Design Features

### 1. No LLM at Runtime
The tree is fully deterministic. No API calls, no AI generation. All intelligence is encoded in the structure.

### 2. Fixed Options Only
Every question has 3-5 predefined options. No free text input. This forces honest self-assessment.

### 3. Non-Judgmental Reflections
The tree guides awareness without moralizing. Even the "victim/entitled/self-centric" path ends with compassion and a concrete next step.

### 4. 18 Personalized Summaries
Based on your path through the three axes, you get one of 18 hand-written summary reflections.

## Validating the Tree

### Check Tree Structure
```bash
python test_tree.py
```

Should output:
```
✓ Tree loaded successfully
✓ Total nodes: 41
✓ Node types: [breakdown by type]
✓ Tree structure is valid!
```

### Read the Tree Data
Open `tree/reflection-tree.json` in any text editor. The structure is:

```json
{
  "metadata": { ... },
  "nodes": [
    {
      "id": "START",
      "type": "start",
      "text": "Good evening...",
      "options": [],
      "target": "A1_OPEN",
      "signal": null
    },
    ...
  ],
  "summary_templates": { ... }
}
```

### Trace a Path
Pick any path from the diagram in `tree/tree-diagram.md` and follow it through the JSON. You'll see exactly how answers lead to branches.

## Submission Checklist

- [x] Tree data file (JSON format)
- [x] Visual diagram (Mermaid in Markdown)
- [x] Design write-up (psychology sources, rationale)
- [x] Working agent (Python, runs the tree)
- [x] Two sample transcripts (different personas)
- [x] README with instructions
- [x] All files organized in proper structure

## What Makes This Tree Good

1. **Psychologically Grounded**: Every question maps to research (Rotter, Dweck, Maslow, Campbell, Organ, Batson)

2. **Honest Options**: No "right" answers. Options capture the real spectrum of human experience.

3. **Conversational Flow**: Not a quiz. Each axis builds on the previous one.

4. **Compassionate Reflections**: Meets people where they are, points toward growth without demanding it.

5. **Readable as Data**: You can trace every path by reading the JSON. No hidden logic.

## Next Steps

1. **Test the agent** with different answer combinations
2. **Read the transcripts** to see how different paths feel
3. **Review the write-up** to understand the design choices
4. **Examine the tree diagram** to visualize the structure

## Questions?

The tree is self-documenting:
- `tree/reflection-tree.json` - The complete data structure
- `tree/tree-diagram.md` - Visual representation
- `write-up.md` - Design philosophy and psychology
- `agent/reflection_agent.py` - Implementation with comments

Everything is deterministic, readable, and traceable. That's the point.
