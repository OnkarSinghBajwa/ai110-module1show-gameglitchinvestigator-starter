# Game Glitch Investigator: The Impossible Guesser

## The Situation

An AI built a simple "Number Guessing Game" using Streamlit — but it was riddled with bugs. The hints lied, the scoring was erratic, and the game was nearly unwinnable. This project documents the process of investigating, diagnosing, and repairing the AI-generated code.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run tests: `python -m pytest tests/ -v`

## Game Description

A number guessing game where you pick a difficulty (Easy, Normal, Hard), and the game generates a secret number within a range. You get a limited number of attempts to guess the number, with hints telling you whether to go higher or lower. Your score depends on how quickly you find the answer.

## Bugs Found and Fixed

1. **Backwards hints**: `check_guess` told users to "Go HIGHER" when their guess was too high, and "Go LOWER" when too low. Fixed by swapping the hint messages.
2. **String conversion on even attempts**: On every even-numbered attempt, the secret was cast to a string, causing type mismatch comparisons. Fixed by always comparing integers directly.
3. **Erratic scoring**: "Too High" outcomes alternated between +5 and -5 points based on attempt parity. Fixed to always deduct 5 points for wrong guesses.
4. **Hard mode was easier than Normal**: Hard had range 1-50 vs Normal's 1-100. Fixed Hard to use 1-200.
5. **Attempt counter off-by-one**: Started at 1 instead of 0, making the first guess count as attempt 2. Fixed to start at 0.
6. **Hardcoded range in UI**: Info text always said "1 and 100" regardless of difficulty. Fixed to use actual range values.

## Fixes Applied

- Refactored all game logic (`check_guess`, `parse_guess`, `update_score`, `get_range_for_difficulty`) from `app.py` into `logic_utils.py`
- Fixed hint direction in `check_guess`
- Removed string conversion bug on even attempts
- Simplified and fixed scoring logic in `update_score`
- Fixed Hard difficulty range to 1-200
- Fixed attempt counter initialization
- Fixed UI to display correct range for selected difficulty
- Added 13 pytest tests covering all logic functions

## Document Your Experience

- [x] Describe the game's purpose: A number guessing game with difficulty levels, scoring, and hints
- [x] Detail which bugs you found: 6 bugs identified (see above)
- [x] Explain what fixes you applied: Logic refactored to logic_utils.py with all bugs corrected

## Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
