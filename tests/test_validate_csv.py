import pytest
from app.services.csv_validation import validate_csv

def test_validate_csv_valid(tmp_path):
    csv_content = "student_id,name,score,date\n1,Alice,85,2023-01-01\n2,Bob,90,2023-01-02"
    file = tmp_path / "valid.csv"
    file.write_text(csv_content)

    result = validate_csv(str(file))
    assert result['rows'] == 2
    assert 'score' in result['columns']

def test_validate_csv_bad_date(tmp_path):
    csv_content = "student_id,name,score,date\n1,Alice,85,notadate\n2,Bob,90,2023-06-02"
    file = tmp_path / "bad_date.csv"
    file.write_text(csv_content)

    with pytest.raises(ValueError, match='date'):
        validate_csv(str(file))

def test_validate_csv_bad_range(tmp_path):
    csv_content = "student_id,name,score,date\n1,Alice,150,2023-06-01\n2,Bob,-10,2023-06-02"
    file = tmp_path / "bad_range.csv"
    file.write_text(csv_content)

    with pytest.raises(ValueError, match='Scores must be between'):
        validate_csv(str(file))
