def cal(x, a, b):
    height = 0
    minutes = 0

    while True:
        minutes += 1
        if minutes % 2 == 1:
            height += a  # climb
            if height >= x:
                return minutes
        else:
            height -= b  # slip
print("Test 1:", cal(30, 10, 5))  # Expected: 7
print("Test 2:", cal(25, 7, 4))   # Expected: 9