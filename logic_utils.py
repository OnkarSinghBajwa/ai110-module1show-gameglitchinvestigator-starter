def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Hard mode now has a wider range (1-200) making it actually harder than Normal (1-100).
    # Previously Hard was 1-50, which was easier than Normal.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome: "Win", "Too High", or "Too Low"
    """
    # FIX: Removed the buggy TypeError catch that compared int to string.
    # FIX: Swapped hints - "Too High" now correctly says "Go LOWER" and vice versa.
    if guess == secret:
        return "Win", "Correct!"

    if guess > secret:
        # FIXME was here: Previously said "Go HIGHER!" when guess was too high
        return "Too High", "Go LOWER!"
    else:
        # FIXME was here: Previously said "Go LOWER!" when guess was too low
        return "Too Low", "Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Simplified scoring - no more erratic +5/-5 toggling on wrong guesses.
    # Win gives bonus points for fewer attempts; wrong guesses always deduct 5.
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # Wrong guesses always lose 5 points
    return current_score - 5
