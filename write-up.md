# Design Rationale: Daily Reflection Tree

## Overview

This reflection tree guides employees through a structured conversation across three psychological axes: Locus (agency), Orientation (contribution), and Radius (concern). The design prioritizes psychological validity, conversational flow, and actionable self-awareness over scoring or judgment.

## Question Design Philosophy

### 1. Honest Options, Not Leading Ones

The hardest part of this design was creating options that genuinely capture the spectrum without telegraphing "right" answers. For example, in A2_OPEN (Axis 2 opening):

- "I helped someone with something outside my job description"
- "I did my work well and expected recognition for it"
- "I went out of my way to make someone else's day easier"
- "I felt frustrated that my efforts weren't acknowledged"
- "I taught someone something without being asked"

Options 1, 3, and 5 indicate contribution orientation. Options 2 and 4 indicate entitlement orientation. But crucially, option 2 ("I did my work well and expected recognition") is not inherently wrong—it's honest. A tired employee at 7pm should be able to select it without feeling judged. The tree's job is to surface the pattern, not shame it.

### 2. Conversational Progression, Not Quiz Questions

Each axis flows as a conversation, not three independent assessments. The opening question establishes emotional tone ("How would you describe today?"), which determines whether the follow-up explores success (agency-high path) or difficulty (agency-low path). This creates natural branching that feels responsive, not algorithmic.

The bridge nodes explicitly connect axes:
- "Now let's shift from how you handled things—to what you gave and what you expected."
- "Finally, let's zoom out. From 'what I did' to 'who it affected.'"

These transitions make the progression feel intentional—each axis builds on the previous one.

### 3. Reflection Without Moralizing

The reflection nodes are the most delicate part. They must:
- Acknowledge the employee's experience
- Reframe without lecturing
- Point toward growth without demanding it

Compare these two reflections:

**A1_R_INTERNAL (Internal Locus):**
> "You see your hand in what happened today. That's agency—not control over everything, but ownership of your response. Even when circumstances constrained you, you stayed in the driver's seat."

**A1_R_EXTERNAL (External Locus):**
> "A difficult day pulls attention outward—to what others did or didn't do, to circumstances beyond your control. That's natural. But somewhere in there, you made choices. What were they? Even deciding to wait is a choice."

The first celebrates agency. The second doesn't criticize its absence—it validates the difficulty, then gently points to where agency might be hiding. This is the tone throughout: a wise colleague, not a therapist or manager.

## Branching Strategy

### Decision Nodes as Invisible Routers

The tree uses decision nodes (type: "decision") as internal routing logic. These are invisible to the employee—they auto-advance based on prior answers. For example:

```json
{
  "id": "A1_D1",
  "type": "decision",
  "options": [
    "answer=Productive|Rewarding:A1_Q_AGENCY_HIGH",
    "answer=Challenging|Frustrating|Overwhelming:A1_Q_AGENCY_LOW"
  ]
}
```

This keeps the tree data clean and readable. The routing rules are explicit—no hidden logic in code.

### Trade-off: Depth vs. Breadth

With 43 nodes, I had to choose: go deep on one axis, or cover all three with moderate depth? I chose breadth. Each axis gets 3-4 questions and 2-3 reflections, which is enough to surface patterns without exhausting the employee.

The alternative—10 questions on Axis 1 alone—would produce richer data but lose the employee's attention. Reflection tools must respect cognitive load. This tree takes ~5-7 minutes to complete, which feels sustainable for daily use.

### Handling Ambiguity

Some answers don't cleanly map to one pole. For example, in A1_Q_AGENCY_HIGH:
- "The team came through when it mattered"

This could indicate external attribution (luck, others' effort) or internal attribution (I built relationships that paid off). The tree routes it to the external path, then asks a follow-up (A1_Q_EXTERNAL_ATTR) that surfaces whether the employee sees their influence in those relationships.

This is the power of sequential questions: ambiguity in one answer gets resolved by the next.

## Psychological Grounding

### Axis 1: Locus of Control (Rotter, 1954) + Growth Mindset (Dweck, 2006)

**Core insight:** People with an internal locus believe their actions shape outcomes. Those with an external locus attribute outcomes to luck, others, or circumstances.

**How the tree surfaces this:**
- A1_Q_AGENCY_HIGH/LOW: "What made it happen?" vs. "What was your first instinct?"
- A1_Q_CHOICE: "What guided your decision?" (Own judgment vs. others' expectations)
- A1_Q_EXTERNAL_ATTR: "Where do you see your influence?" (Preparation vs. external factors)

**Key source:** Rotter, J. B. (1966). "Generalized expectancies for internal versus external control of reinforcement." *Psychological Monographs*, 80(1), 1-28.

Dweck's growth mindset extends this: people with a growth mindset see abilities as developable through effort, while those with a fixed mindset see talent as innate. The tree doesn't explicitly ask about ability, but the framing of "what you could control" vs. "what happened to you" captures the same distinction.

### Axis 2: Entitlement (Campbell et al., 2004) + Organizational Citizenship (Organ, 1988)

**Core insight:** Entitled employees focus on what the organization owes them. Contributing employees focus on discretionary effort—helping colleagues, improving processes, volunteering for unglamorous work.

**How the tree surfaces this:**
- A2_OPEN: "Which statement feels most true?" (Helped vs. Expected recognition)
- A2_Q_CONTRIBUTION: "What motivated you?" (Intrinsic vs. transactional)
- A2_Q_ENTITLEMENT: "What did you deserve?" (Recognition, support, resources)
- A2_Q_DISCRETIONARY: "Did you do anything not required?" (Volunteered vs. stuck to lane)
- A2_Q_COMPARISON: "How do you feel compared to others?" (Balanced vs. resentful)

**Key source:** Campbell, W. K., Bonacci, A. M., Shelton, J., Exline, J. J., & Bushman, B. J. (2004). "Psychological entitlement: Interpersonal consequences and validation of a self-report measure." *Journal of Personality Assessment*, 83(1), 29-45.

Organ's OCB (Organizational Citizenship Behavior) is the positive counterpart: discretionary effort that benefits the organization but isn't formally rewarded. The tree asks directly about this: "Did you do anything today that wasn't required?"

### Axis 3: Self-Transcendence (Maslow, 1969) + Perspective-Taking (Batson, 2011)

**Core insight:** Maslow's later work argued that the healthiest humans move beyond self-actualization to self-transcendence—orienting toward something larger than themselves. Batson's research on empathy distinguishes sympathy (feeling for someone) from perspective-taking (imagining their experience).

**How the tree surfaces this:**
- A3_OPEN: "Who comes to mind?" (Just me → Team → Customer → Mission)
- A3_Q_SELF: "What were you worried about?" (Performance vs. impact on others)
- A3_Q_TEAM: "Did you take action based on that awareness?" (Checked in vs. just noticed)
- A3_Q_TRANSCENDENT: "How does the mission change your experience?" (Makes frustrations smaller vs. doesn't change much)

**Key source:** Maslow, A. H. (1969). "Various meanings of transcendence." *Journal of Transpersonal Psychology*, 1(1), 56-66.

The progression from self → team → mission mirrors Maslow's hierarchy. The tree doesn't judge someone for being self-focused—it asks whether widening the lens changes anything. For some employees, it will. For others, not yet. The tree plants the seed.

## Summary Templates: 18 Personalized Endings

The tree generates one of 18 summary reflections based on the employee's path:
- Axis 1: Internal vs. External (2 options)
- Axis 2: Contribution vs. Entitlement vs. Transactional (3 options)
- Axis 3: Altrocentric vs. Team-aware vs. Self-centric (3 options)

2 × 3 × 3 = 18 combinations.

Each template is hand-written to reflect the specific combination. For example:

**internal_contribution_altrocentric:**
> "You showed up with agency, gave without keeping score, and held others in your awareness. That's a day of growth. Not perfect—growth never is—but directionally sound."

**external_entitlement_self:**
> "Today felt like it happened to you. You did what was required, no more. Your focus stayed on your own experience. That's the smallest possible frame. Here's the path out: agency first, then contribution, then widening your concern. One step at a time."

The second doesn't shame—it names the pattern and points to a path. This is the tree's core philosophy: awareness without judgment, direction without demand.

## What I'd Improve With More Time

### 1. More Granular Branching on Axis 3

Axis 3 (Radius) has the widest spectrum—from pure self-focus to mission-oriented transcendence. With more nodes, I'd add:
- A question about whether the employee knows the names of people affected by their work
- A question about whether they've ever met an end user
- A reflection on the difference between "team" (people you know) and "mission" (people you'll never meet)

### 2. Temporal Dimension

The tree asks about "today," but patterns emerge over time. With more sophistication, I'd:
- Track answers across sessions (stored locally, not sent anywhere)
- Surface trends: "You've leaned external on agency for three days. What's happening?"
- Celebrate shifts: "Last week you were transactional. Today you volunteered. What changed?"

This would require persistent state, which adds complexity but also value.

### 3. Contextual Branching

Some questions assume a team environment. A solo founder or remote worker might answer differently. With more time, I'd:
- Add an initial context question: "Do you work alone or with a team?"
- Branch Axis 2 and 3 questions accordingly
- For solo workers, reframe "team" questions as "community" or "customers"

### 4. Accessibility Features

The current tree is text-only. For broader use, I'd add:
- Audio narration (for employees with visual impairments or reading fatigue)
- Adjustable pacing (some people need more time to reflect)
- Option to skip a day without guilt (the tree should invite, not demand)

## Conclusion

This tree is a knowledge engineering artifact. It encodes psychological research (Rotter, Dweck, Maslow, Batson, Campbell, Organ) into a navigable structure that guides employees toward self-awareness. It's deterministic—no LLM, no randomness—but it feels conversational because the questions are honest and the reflections are human.

The hard part wasn't the code. The hard part was writing questions that make a tired employee at 7pm stop and think: *"Huh. I did have more control today than I realized."*

That's the goal. That's what this tree does.

---

**Word count:** ~1,850 words
