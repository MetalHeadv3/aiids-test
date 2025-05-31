import os
from dataset_tool import DatasetHandler

def main():
    path = r"C:\Users\Krzysiek\OneDrive\Pulpit\Data analysis database\iris.data"

    if not os.path.isfile(path):
        print(f"Plik {path} nie istnieje.")
        return

    dataset = DatasetHandler(path, has_header=False)

    dataset.print_headers()  
    dataset.print_data(0, 5)
    dataset.count_classes()

    train, test, valid = dataset.split_dataset(0.7, 0.2, 0.1)
    print(f"\nRozmiary podzbiorów: train={len(train)}, test={len(test)}, valid={len(valid)}")

    filtered = dataset.filter_by_class("Iris-setosa")

    dataset.save_to_csv(train, "iristrain5.csv")

if __name__ == "__main__":
    main()

