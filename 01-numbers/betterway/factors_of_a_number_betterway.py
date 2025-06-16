import math
def countFactors (n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            count += 1
            if i != n//i:
                count += 1
    return count
if __name__ == "__main__":
    sample_input = 25
    print("Output : ",countFactors(sample_input))