import random
def Game_2():
    print("fill in the missing")
    lenn = (random.randint(5, 10))
    n = (random.randint(0, lenn - 1))
    a = (random.randint(1, 5))
    b = (random.randint(1, 5))
         
    s = [str(a)]
    for i in range(1, lenn - 1):
         s.append (str(int(s[i-1]) + int(s[i-1]) * b))
    ans = s[n]
    s[n] = ".."
    print(s)
    return ans
