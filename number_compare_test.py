from number_compare import larger_than_15


def test_larger_with_big_number():
    # Given
    # When
    result = larger_than_15(100)
    # Then
    assert result == True


def test_larger_with_big_number_short():
    assert larger_than_15(100)