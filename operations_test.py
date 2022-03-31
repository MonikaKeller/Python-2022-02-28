from operations import add

def test_add():
    #given
    number1 = 5
    number2 = 10
    #when
    result = add(number1,number2)
    #then
    assert result == 15