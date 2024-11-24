from src.calculator.divide import divide

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."