def factorials(n):
    fact = 1
    i = 1
    while fact <= n:
        print(fact,end = " ")
        i += 1
        fact *= i
if __name__ == "__main__":
    factorials(25)