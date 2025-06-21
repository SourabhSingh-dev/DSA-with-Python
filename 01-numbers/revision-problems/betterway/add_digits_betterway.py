def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num-1)%9
if __name__ == "__main__":
    sample_input = 38
    print("Output : ",addDigits(sample_input))