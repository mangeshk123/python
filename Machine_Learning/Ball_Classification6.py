from sklearn import tree

def main():
    print("Ball classification case study...")

    Independant = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,0],[96,0],[43,1],[110,0]]
    # Testing 
    Dependent = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    # Testing 1, 2
    model = tree.DecisionTreeClassifier()
    model = model.fit(Independant,Dependent)
    Result = model.predict([[35,1],[95,0]])
    print("Predicted model of result is ",Result)

    
if __name__ == "__main__":
    main()