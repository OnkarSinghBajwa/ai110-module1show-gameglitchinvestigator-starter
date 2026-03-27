# Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").

When I first ran the game, it appeared to work on the surface but was essentially unwinnable. The first major bug was that **the hints were backwards** — when my guess was too high, the game told me to "Go HIGHER!" and vice versa, leading me further from the answer every time I followed the hint. The second bug was that **on every even-numbered attempt, the secret number was converted to a string**, causing type mismatch comparisons that made the game behave unpredictably — sometimes a correct guess wouldn't register as a win. The third bug was the **erratic scoring system** — wrong guesses on "Too High" alternated between adding and subtracting points depending on the attempt number, making scores jump around randomly. Additionally, the Hard difficulty had a range of 1-50 which was actually easier than Normal's 1-100, and the attempt counter started at 1 instead of 0, meaning the first guess counted as attempt 2.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code (Anthropic's AI coding assistant) as my primary tool for this project. One **correct suggestion** was identifying that the `check_guess` function had swapped hint messages — Claude correctly identified that line 38 said "Go HIGHER!" when the guess was greater than the secret, which is the opposite of what it should say. I verified this by reading the check_guess logic: `if guess > secret` should tell the user to go lower, not higher, and confirmed it by running the fixed game. One **misleading aspect** of the original AI-generated code was the `TypeError` catch block in `check_guess` — it appeared to be a safety feature but was actually masking the real bug where even attempts converted the secret to a string. This made debugging harder because the code appeared to handle errors gracefully when it was actually hiding broken behavior. I verified this by removing the string conversion bug entirely, which eliminated the need for the TypeError handling.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by running both automated tests and manual gameplay. For pytest, I wrote `test_guess_too_high` which calls `check_guess(60, 50)` and asserts the outcome is "Too High" with "LOWER" in the message — this directly targets the backwards-hints bug and confirmed the fix works. I also wrote `test_score_on_wrong_guess` to verify that wrong guesses consistently deduct 5 points regardless of attempt number, catching the old alternating +5/-5 behavior. The original starter tests were also broken — they expected `check_guess` to return just a string, but it returns a tuple `(outcome, message)`, so I fixed those first. After all 13 tests passed, I ran the Streamlit app manually to confirm the game was playable and winnable. Claude helped me design test cases by identifying edge cases like the minimum score on late wins and ensuring Hard difficulty's range is actually wider than Normal's.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit works differently from most web frameworks — every time you interact with the app (click a button, type in a field), the entire Python script re-runs from top to bottom. This means any regular variable gets reset to its initial value on every interaction, which is why you need `st.session_state` to persist data between reruns. Think of it like a whiteboard that gets erased and redrawn every time someone touches it — `session_state` is like a sticky note on the side that survives the erasing. In this project, the secret number, score, and attempt count all needed to be in session_state, and one of the bugs was the attempt counter initializing to 1 instead of 0, which threw off the game's attempt tracking across reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to carry forward is **writing targeted tests for each specific bug before considering it fixed**. Rather than just eyeballing the fix in the browser, having a pytest case that directly exercises the broken logic gives concrete proof the fix works and prevents regressions. Next time I work with AI on a coding task, I would **read through the entire generated code line-by-line before running it**, rather than running first and debugging after — several of these bugs could have been caught by careful code review. This project taught me that AI-generated code can look clean and well-structured while hiding subtle logic errors — the backwards hints, the string conversion on even attempts, and the erratic scoring were all syntactically valid Python that would pass a casual review but fundamentally broke the game.
