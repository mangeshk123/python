import threading
# 2+4+6+8
def sumeven(No):
    sum  = 0
    for i in range(2,No,2):
        sum = sum + i
    print(f"Sum even is {sum}")

# 1+3+5+7+9
def sumodd(No):
    sum  = 0
    for i in range(2,No,2):
        sum = sum + i
    print(f"Sum odd is {sum}")

def main():
    sumeven(10000000)
    sumodd(10000000)

if __name__ == "__main__":
    main()