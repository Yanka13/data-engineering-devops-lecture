from dice_roller.dice import Dice 


def test_dice_roll():
    result = Dice().roll()
    assert result > 0 
    assert result < 7 


def test_dice_roll_int(): 
    result = Dice().roll()
    assert type(result) == int  
