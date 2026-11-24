---
name: just-enough-prompt
description: Improves a prompt by adding only the prompt-engineering practices it is actually missing, then shows a short table of what was added, what was skipped, and why. Use when the user asks to improve, rewrite, fix, review or optimize a prompt, system prompt or agent instruction; pastes a prompt and asks how to make it better; turns a rough one-line request into a proper prompt; or says a prompt "doesn't work" or gives bad results, even if they never say "prompt engineering". Not for compressing prompts to save tokens or for reviewing how a skill is packaged.
license: MIT
metadata:
  author: Stanislav Fedyna
  version: "1.0.0"
---

# Just Enough Prompt

## Goal

Take a weak or incomplete prompt → diagnose it → return an improved prompt that applies **only** the practices that actually raise the quality of *this* request.

**Core principle:** do not apply every technique. Find what is specifically missing and add only that. A short prompt that needed one fix should come back short.

## Catalog of practices

Before improving, go through this catalog and mark which practices fit. The "skip when" line matters as much as the "use when".

### BP-1: Role (persona)
**Use when** the task needs expertise, a particular style or a point of view.
**How:** `You are a [role] with [expertise].`
**Skip when** it's a simple factual request where a role adds nothing.

### BP-2: Clear instruction (directive verb)
**Use when** the prompt has no clear action verb. Almost always worth checking.
**How:** start with a verb: Write / Summarize / Explain / Classify / Generate / List / Compare / Translate / Refactor / Review.
**Skip when** the directive is already clear.

### BP-3: Context / background
**Use when** the answer depends heavily on context the model can't guess.
**How:** a `Context:` block or a sentence covering who, what, and why.
**Skip when** context wouldn't change the answer.

### BP-4: Output format
**Use when** the shape of the answer matters: structure, length, format.
**How:** `Respond in markdown`, `Return a JSON object with keys …`, `Use bullet points`, `Maximum 3 paragraphs`, `Format as a table`.
**Skip when** it's a short chat answer whose format is obvious.

### BP-5: Audience
**Use when** depth, vocabulary and detail should fit a specific reader.
**How:** `for a senior developer`, `for a non-technical stakeholder`, `for a first-time founder`.
**Skip when** the audience is obvious or doesn't matter.

### BP-6: Few-shot examples
**Use when** the task is classification, format conversion, pattern-following generation, or "show, don't tell".
**How:** 1–3 `Input: … Output: …` pairs before the task. Make them varied and representative.
**Skip when** it's an open creative task where examples would narrow the range.

### BP-7: Reasoning trigger
**Use when** the task needs reasoning: analysis, multi-step logic, math, cause and effect.
**How:** for models without built-in reasoning, `Think step by step` or numbered reasoning steps. For reasoning models, state the goal and the success criteria instead (see Gotchas).
**Skip when** it's a factual lookup, where reasoning text is just noise.

### BP-8: Constraints and boundaries
**Use when** scope needs limits, unwanted patterns need ruling out, or rules must be explicit.
**How:** `Limit to 200 words`, `Only use information from the provided text`, `Avoid jargon`. Prefer saying what to do over only what not to do.
**Skip when** there are no real limits and adding some would only narrow usefulness.

### BP-9: Tone and style
**Use when** tone matters: documents, marketing, documentation, feedback.
**How:** `Professional and transparent, not defensive`, `Conversational`, `Concise and direct`.
**Skip when** it's a neutral technical request where tone is obvious.

### BP-10: Delimiters and structure
**Use when** the prompt mixes several blocks (instructions + data + examples) and they could blur together.
**How:** `###`, `"""`, `---` or XML-style tags like `<document>…</document>`. Tags work especially well with Claude.
**Skip when** it's a simple single-block prompt.

### BP-11: Success criteria
**Use when** "a good answer" is unclear or open to several readings.
**How:** `A good response should…`, `The output is successful if…`, `Focus on X, not Y`.
**Skip when** the task is already specific.

### BP-12: Specificity over vagueness
**Always check** for vague words: "good", "detailed", "appropriate", "nice", "interesting".
**How:** replace them with concrete parameters. "Detailed" → "with an explanation of each step". "Good code" → "readable, DRY, with meaningful variable names".
**Skip when** the prompt is already concrete.

## Workflow

1. **Read** the input prompt carefully. Note what it will be used for if that's visible (chat, system prompt, agent task, API call, a specific model).
2. **Identify the task type:** coding / writing / analysis / classification / Q&A / creative / agent instruction / other.
3. **Scan BP-1…BP-12** and mark only the ones that would genuinely improve this prompt.
4. **Apply** them and write the improved prompt.
5. **Explain** the changes in a short table: what was added, what was skipped, and why.

Don't over-engineer. A simple, decent prompt may need only one or two practices. The goal is effectiveness, not length.

## Gotchas

- **Never invent facts.** Dates, names, numbers, product details and requirements the user didn't give go in as `[placeholders]`, listed under the prompt as "Fill in before using". An improved prompt with made-up facts is worse than the original.
- **Keep the user's intent and language.** Don't change what is being asked. Write the improved prompt in the same language as the original unless the user asks for another one.
- **Reasoning models** (models with extended or built-in thinking): drop "think step by step". Give them the goal, the constraints and what a good answer looks like; they plan the steps themselves.
- **Explain the why instead of shouting.** "Keep it under 100 words because it's shown on a phone" works better than "KEEP IT SHORT!!!". Reserve ALL CAPS and "MUST" for the one rule that really can't bend.
- **Positive over negative.** Turn lists of "don't" into what to do instead (see `references/anti-patterns.md`).
- **One prompt, one job.** If the prompt bundles several unrelated tasks, say so and suggest splitting it into a chain; don't silently cram everything into one improved version.
- **Agent and system prompts:** the same catalog applies, but weigh BP-3 (context), BP-8 (constraints) and BP-11 (success criteria) highest; roles and tone matter less there.

## Response format

Always answer in this structure (headings in the user's language):

```
## 🔍 Diagnosis

[1–3 sentences: what's wrong or missing]

## ✅ Improved prompt

[the full improved prompt in a code block]

[If any: "Fill in before using:" + the list of placeholders]

## 📋 What changed

| Practice | Applied | Why |
|---|---|---|
| BP-X: Name | ✅ Added | why it helps here |
| BP-Y: Name | ❌ Skipped | why this case doesn't need it |
```

List only the practices you considered relevant either way; don't pad the table with all twelve.

## Examples

### Example 1: coding

**Before:**
```
write a sorting function
```

**After:**
```
You are a senior software engineer writing clean, production-ready code.

Write a [language] function that sorts an array of objects by a given key.

Requirements:
- Handle edge cases: empty array, missing key, mixed value types
- Return a new array (do not mutate the input)
- Add a doc comment

Example:
Input: [{name: "Zara", age: 25}, {name: "Alex", age: 30}], key: "name"
Output: [{name: "Alex", age: 30}, {name: "Zara", age: 25}]
```
Fill in before using: `[language]`.

**Added:** BP-1 (role), BP-3 (requirements as context), BP-8 (edge cases, no mutation), BP-6 (example), BP-4 (doc comment).

### Example 2: writing

**Before:**
```
write an email about the project delay
```

**After:**
```
Write a professional email to a client telling them the project is delayed by [length of delay].

Context: the delay is caused by [reason]. The original deadline was [original date]; the new one is [new date].

Tone: professional, transparent and solution-focused, not defensive.

Include:
1. A clear statement of the delay and the new timeline
2. A brief reason, without technical jargon
3. The concrete next steps we are taking
4. An apology that doesn't over-apologize

Length: at most 150 words.
```
Fill in before using: `[length of delay]`, `[reason]`, `[original date]`, `[new date]`.

**Added:** BP-3 (context as placeholders, not invented), BP-9 (tone), BP-8 (what to include, length), BP-4 (numbered structure).

### Example 3: analysis

**Before:**
```
why do startups fail?
```

**After:**
```
Analyze the most common reasons tech startups fail within their first 3 years.

1. Identify the top 5 root causes, based on research and case studies.
2. Give one real-world example for each.
3. Conclude with the single most preventable failure mode and why.

Format: a numbered list of causes with examples, then one concluding paragraph.

Audience: a first-time founder with no startup experience.
```

**Added:** BP-7 (numbered reasoning steps; for a reasoning model, keep the steps as the structure of the answer), BP-4 (list + paragraph), BP-5 (audience), BP-8 (3 years, top 5), BP-11 (the synthesis as the target).

## Further reference

- Read `references/techniques.md` when a prompt needs a technique beyond the catalog: few-shot, chain-of-thought, self-consistency, tree of thoughts, ReAct, meta prompting.
- Read `references/anti-patterns.md` when diagnosing a prompt that "doesn't work", to name the failure pattern precisely.

The catalog draws on the [Prompt Engineering Guide](https://www.promptingguide.ai) by DAIR.AI and on model vendors' published prompting guidance.
