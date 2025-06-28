from app.routes.upload import is_allowed_file

def test_is_allowed_file_accepts_csv():
    assert is_allowed_file('scores.csv') is True

def test_is_allowed_file_accepts_uppercase_extension():
    assert is_allowed_file('scores.CSV') is True

def test_is_allowed_file_accepts_multiple_dots():
    assert is_allowed_file('report.final.csv') is True

def test_is_allowed_file_strips_whitespace():
    assert is_allowed_file('grades.csv ') is True

def test_is_allowed_file_rejects_txt():
    assert is_allowed_file('scores.txt') is False

def test_is_allowed_file_rejects_exe():
    assert is_allowed_file('virus.exe') is False
