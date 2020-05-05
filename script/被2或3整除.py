for i in range(100):
    if i%2 == 0:
        if i%3 == 0:print(f'{i:0>2d}能被2和3整除')
        else:print(f'{i:0>2d}只能能被2整除')
    elif i%3 == 0:print(f'{i:0>2d}只能能被3整除')
    