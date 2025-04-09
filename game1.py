import random
def Game_1():
    print("Find the smallest common multiple of given numbers.")
    a = (random.randint(1, 10))
    b = (random.randint(1, 10))
    c = (random.randint(1, 10))
    print("Question:", a, b, c)
    
    ma = max(a,b,c)
    while ma % a != 0 or ma % b != 0 or ma % c != 0:
        ma += 1
    return str(ma)
