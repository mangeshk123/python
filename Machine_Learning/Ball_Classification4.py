from sklearn import tree

def main():
    print("Ball classification case study...")

    Independant = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,0],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Dependent = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    print("Independant vars are ", Independant)
    print("Dependent vars are ", Dependent)
    
if __name__ == "__main__":
    main()