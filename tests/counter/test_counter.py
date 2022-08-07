from src.counter import count_ocurrences


def test_counter():
    case_Industry = count_ocurrences("src/jobs.csv", "Industry")
    assert case_Industry == 1346
