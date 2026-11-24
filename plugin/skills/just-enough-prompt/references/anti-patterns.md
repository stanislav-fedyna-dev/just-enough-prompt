# Prompting anti-patterns

Common reasons a prompt "doesn't work", each with symptoms and a fix.

## 1. Vague instructions

**Bad:** "Write a good text about marketing."
**Better:** "Write a 300-word LinkedIn article on content marketing for B2B SaaS companies. Tone: professional but approachable. Include 3 actionable tips."

**Symptoms:** words like "good", "detailed", "appropriate", "suitable", "interesting" with nothing concrete behind them.

---

## 2. Missing context

**Bad:** "Explain this error."
**Better:** "Explain this Python error: `TypeError: 'NoneType' object is not subscriptable`. I'm indexing into the dict returned by `get_user_data()`."

**Symptoms:** pronouns with nothing they refer to ("this", "it"); no code, data or scenario.

---

## 3. Overloaded prompt

**Bad:** "Analyze the market, find competitors, write a strategy, do a SWOT and recommend pricing."
**Better:** split it into a chain of separate prompts, each feeding the next.

**Symptoms:** "and", "also", "plus" joining more than 2–3 distinct tasks.

---

## 4. Negative-only instructions

**Bad:** "Don't write too much. Don't use jargon. Don't be formal."
**Better:** "Write 3–4 sentences. Use plain language. Keep the tone conversational."

**Symptoms:** the prompt is only "don't do X", with no positive direction.

---

## 5. No output format

**Bad:** "Compare React and Vue."
**Better:** "Compare React and Vue in a markdown table with columns Category | React | Vue. Categories: learning curve, performance, ecosystem, typical use case."

**Symptoms:** answers come back in unpredictable shapes that are hard to read or parse.

---

## 6. Ambiguous subject

**Bad:** "Fix the bugs and deploy."
**Better:** "Review the code in `auth.service.ts`, fix any TypeScript type errors, then describe the changes you made."

**Symptoms:** it's unclear what exactly, where, and what "fix" means.

---

## 7. Assuming the model knows your domain

**Bad:** "Write a test for the component."
**Better:** "Write a React Testing Library unit test for the `<UserCard>` component (TypeScript). Props: `{ name: string, email: string, isAdmin: boolean }`. Test that it renders the name and email, and shows an 'Admin' badge when `isAdmin` is true."

**Symptoms:** the model gives a generic answer that doesn't fit your project or stack.

---

## 8. No reasoning cue on a complex task

**Bad:** "Which architecture is better for my project?"
**Better:** "I'm building a real-time collaborative document editor for about 10,000 concurrent users. Work through the key architectural challenges, the patterns that address each, and recommend one approach with your reasons."

**Symptoms:** a shallow, generic answer with no real analysis.

---

## 9. Invented specifics

**Bad:** an "improved" prompt that adds dates, numbers or names the user never gave ("the deadline moved from June 15 to June 29").
**Better:** put unknowns in `[placeholders]` and list them for the user to fill in.

**Symptoms:** the improved prompt looks complete but contains facts that are not true for the user.
