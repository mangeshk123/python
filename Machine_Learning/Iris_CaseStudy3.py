from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris classification case study")
    print("-"*30)

    Dataset = load_iris()
    # Metadata of dataset
    print("Independant variables are")
    print(Dataset.feature_names)
    print("Length of Independant variables is", len(Dataset.feature_names))
    print("Dependent variables are")
    print(Dataset.target_names)
    print("Length of Dependant variables is", len(Dataset.target_names))
    
if __name__ == "__main__":
    main()