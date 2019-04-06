def greed_is_good(dice):
    score = 0
    ones = dice.count(1)
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    sixs = dice.count(6)
    if ones > 2: score += 1000
    if ones > 3: score += 100 * (ones % 3)
    if ones < 3: score += 100 * ones
    if twos > 2: score += 200
    if threes > 2: score += 300
    if fours > 2: score += 400
    if fives > 2: score += 500
    if fives > 3: score += 50 * (fives % 3)
    if fives < 3: score += 50 * fives
    if sixs > 2: score += 600
    return score
