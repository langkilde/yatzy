def fast_counter(dices):
    count = {1: dices.count(1),
             2: dices.count(2),
             3: dices.count(3),
             4: dices.count(4),
             5: dices.count(5),
             6: dices.count(6)}
    return count


def upper_section_validator(dices, die_value=None, die_count=None):
    # Any set of dices are valid for the upper section
    return True


def n_kind_validator(dices: list, die_value=None, die_count=None):
    # check if there are die_count number of die_value
    # or die_count of any if die_value is None
    # returns Boolean, [list of options]

    valid = False
    options = []

    if not die_value:
        count = fast_counter(dices)
        for n in range(1, 7):
            if count[n] >= die_count:
                options.append(n)

    if die_value:
        number_of_die = dices.count(die_value)
        if number_of_die >= die_count:
            options.append(die_value)

    if len(options) > 0:
        valid = True

    return valid


def two_pairs_validator(dices, die_value=None, die_count=None):
    pairs = 0
    dies = []
    die_count = fast_counter(dices)
    for die in die_count:
        if die_count[die] >= 2:
            pairs += 1
            dies.append(die)
    if pairs > 1:
        return True
    return False


def small_straight_validator(dices, die_value=None, die_count=None):
    return {1, 2, 3, 4, 5}.issubset(dices)


def large_straight_validator(dices, die_value=None, die_count=None):
    return {2, 3, 4, 5, 6}.issubset(dices)


def full_house_validator(dices, die_value=None, die_count=None):
    die_count = fast_counter(dices)
    for die1 in die_count:
        if die_count[die1] == 3:
            for die2 in die_count:
                if die_count[die2] == 2:
                    return True
    return False


def chance_validator(dices, die_value=None, die_count=None):
    return True
