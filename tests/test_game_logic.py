from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


# --- check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should say "Too High" and tell user to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should say "Too Low" and tell user to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- parse_guess tests ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."


def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False


def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert "not a number" in err


def test_parse_float_string():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3


# --- update_score tests ---

def test_score_on_win_first_attempt():
    # Win on attempt 1 should give 90 points (100 - 10*1)
    score = update_score(0, "Win", 1)
    assert score == 90


def test_score_on_wrong_guess():
    # Wrong guess always deducts 5
    score = update_score(50, "Too High", 1)
    assert score == 45
    score = update_score(50, "Too Low", 2)
    assert score == 45


def test_score_win_minimum():
    # Even on late attempts, win gives at least 10 points
    score = update_score(0, "Win", 20)
    assert score == 10


# --- get_range_for_difficulty tests ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
