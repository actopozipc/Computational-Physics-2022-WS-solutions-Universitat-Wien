def smallestMultiple():
    c = 2520;
    while True:
        div = True;
        for i in range(1,20):
            if c % i != 0:
                c = c+1;
                div = False;
        if div:
            return c;
if __name__ == "__main__":
   
    print(smallestMultiple());
    # n = 2520
    # t = lambda c: all(map(lambda x: n % x ==0, range(2,c)))
    # while not (t(20)):
    #     n = n+1;
    # print(n)
    