from dataset_tool import DatasetHandler

dh = DatasetHandler("iris.data", has_header=False)
dh.print_headers()
dh.print_data(0, 5)
dh.count_classes()
train, test, valid = dh.split_dataset(0.7, 0.2, 0.1)
print(f"Rozmiary zbiorów: train={len(train)}, test={len(test)}, valid={len(valid)}")
dh.save_to_csv(train, "train.csv")
