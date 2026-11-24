# Prompting techniques reference

Techniques beyond the core catalog, with when to use each and a template.

## Contents
1. Few-shot prompting
2. Chain-of-thought (CoT)
3. Self-consistency
4. Tree of thoughts (ToT)
5. ReAct
6. Meta prompting

---

## 1. Few-shot prompting

Give 1–5 input→output examples before the real request.

**When:** classification, format conversion, generation that follows a pattern.

**Template:**
```
Here are some examples:

Input: [example input 1]
Output: [example output 1]

Input: [example input 2]
Output: [example output 2]

Now complete this:
Input: [actual input]
Output:
```

**Important:** examples must be representative and varied. Three near-identical examples teach the model to copy their surface, not the pattern.

---

## 2. Chain-of-thought (CoT)

Have the model reason before its final answer.

**When:** math, logical inference, cause-and-effect analysis, multi-step tasks.

**Ways to trigger it:**
- Zero-shot CoT: `Think step by step.`
- Few-shot CoT: examples that show the reasoning, not just the answer.

**Zero-shot template:**
```
[task]

Let's think step by step.
```

**Few-shot template:**
```
Q: [question 1]
A: Let's think step by step. [reasoning] … Therefore, the answer is [X].

Q: [question 2]
A:
```

**Reasoning models:** models with built-in or extended thinking already reason before answering. For them, skip the trigger phrase; describe the goal, the constraints and what a good answer looks like.

---

## 3. Self-consistency

Generate several independent reasoning paths and pick the answer they agree on most.

**When:** hard problems where a single chain of reasoning can go wrong.

**In a prompt:**
```
Solve this problem using three different approaches.
Then identify which answer appears most consistently across them.

Problem: [problem]
```

---

## 4. Tree of thoughts (ToT)

Explore several branches of reasoning and evaluate each.

**When:** problems with several possible strategies: planning, creative writing, complex problem solving.

**Template:**
```
Consider this problem: [problem]

Generate 3 different high-level approaches.
For each approach:
1. Describe the strategy
2. Name its strengths and weaknesses
3. Rate its likelihood of success (1–10)

Then choose the best approach and carry it out step by step.
```

---

## 5. ReAct (reason + act)

Alternate Thought → Action → Observation, for tasks with tools or multi-step search.

**When:** agent tasks, research with search, tasks that require deciding and acting.

**Format:**
```
Thought: [what I think about the situation]
Action: [what I do]
Observation: [what I see]
Thought: [next step]
…
Final Answer: [answer]
```

Most agent frameworks implement this loop themselves. In an agent's system prompt, describe the tools and when to use each rather than spelling out the loop.

---

## 6. Meta prompting

Ask the model to design the approach first, then carry it out.

**When:** long, complex tasks where the approach matters.

**Template:**
```
Before answering, outline your approach:
1. What are the key parts of this task?
2. What information do you need?
3. What format will be most useful?

Then give your full answer following that outline.

Task: [task]
```
