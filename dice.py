from random import randint


def dice_func(die):

    """Function finds a type of dice wanted and rolls it.
    If the dice is not in the tuple it returns "Wrong input!" statement"""

    viable_dice = ('d3', 'd4', 'd6', 'd8', 'd100', 'd12', 'd20', 'd10')
    dice = ""

    for d in viable_dice:
        if d in die:
            dice = d
            break

    if len(dice) == 0:
        return "Wrong input!"

    try:
        dice = int(dice.replace('d', ""))
    except (TypeError, ValueError):
        return "Wrong input!"
    return dice


def amount_func(amount):

    """Function for setting amount of dice to roll"""

    amount_of_rolls = ""
    amount = list(amount)

    for i in amount:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            amount_of_rolls += i
        else:
            break

    if len(amount_of_rolls) == 0:
        amount_of_rolls = 1
        
    # If user does not input any number before the dice in input, it will assume 1 as the amount of dice to roll
    
    elif amount_of_rolls == "0":
        amount_of_rolls = 0

    return int(amount_of_rolls)


def mod_func(roll):

    """Function for setting a modifier for the roll"""

    mod = ""

    if "+" in roll:
        roll = roll.split("+", 1)
    elif "-" in roll:
        roll = roll.split("-", 1)
        mod += "-"
    else:
        mod = 0

    if mod != 0:
        mod += roll[-1]

    try:
        mod = int(mod)
    except ValueError:
        return "Wrong input!"
    
    return mod


def dice_roller():

    """Function for dice rolling"""

    print('Use the xDy+z format to roll the dice. Example: "2D6+4"')
    roll = input("Enter the dice: ").lower()

    if roll.count('d') > 1:
        return "Wrong input!"

    validate = roll.replace("d", "").replace("+", "").replace('-', "")

    # "validate" variable is made just for checking if input is correct, by trying to convert itself into a integer.
    # This allows us to find if there are any unwanted characters, because we got rid of +, - and d which are essential for the roll.
    # Even if there are multiple of + or - signs, we can catch them either later in function or in other 3 functions.

    if not isinstance(roll, str):
        return "Wrong input!"

    try:
        validate = int(validate)
    except ValueError:
        return "Wrong input!"

    # Checking if the input is correct, so that user can only use xDy+z format
    # and is informed if they input something wrong.

    dice = dice_func(roll)
    amount_of_dice = amount_func(roll)
    modifier = mod_func(roll)

    if dice == "Wrong input!" or modifier == "Wrong input!":
        return "Wrong input!"

    # Checking if the other functions did not return "Wrong input!" statement

    else:
        result = 0
        for amount in range(amount_of_dice):
            result += randint(1, dice)
            
        # The last loop simulates the rolling of the dice, each one individually, just like in an RPG game.

    return result + modifier
