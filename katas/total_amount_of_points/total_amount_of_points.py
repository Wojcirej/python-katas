def total_amount_of_points(games):
    sum = 0
    for game in games:
        x, y = game.split(":")
        x = int(x)
        y = int(y)
        if x > y:
            sum += 3
        elif x == y:
            sum += 1
    return sum
