import csv
import random
from collections import Counter
from typing import List, Tuple


class DatasetHandler:

    def __init__(self, file_path: str, has_header: bool = False):
        self.file_path = file_path
        self.has_header = has_header
        self.data: List[List[str]] = []
        self.headers: List[str] = []
        self.load_dataset()

    def load_dataset(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            if self.has_header:
                self.headers = next(reader)
            self.data = [row for row in reader if row and len(row) == 5]

    def print_headers(self):
        if self.headers:
            print("\nEtykiety kolumn:")
            print(", ".join(self.headers))
        else:
            print("Brak etykiet w zbiorze danych.")

    def print_data(self, start: int = None, stop: int = None):
        print("\nDane:")
        rows = self.data[start:stop] if start is not None and stop is not None else self.data
        for row in rows:
            print(row)

    def split_dataset(self, train_ratio: float, test_ratio: float, valid_ratio: float) -> Tuple[List, List, List]:
        if abs(train_ratio + test_ratio + valid_ratio - 1.0) > 1e-6:
            raise ValueError("Suma udziałów musi wynosić 1.0")
        random.shuffle(self.data)
        total = len(self.data)
        train_end = int(total * train_ratio)
        test_end = train_end + int(total * test_ratio)
        return self.data[:train_end], self.data[train_end:test_end], self.data[test_end:]

    def count_classes(self):
        labels = [row[-1] for row in self.data]
        counter = Counter(labels)
        print("\nLiczba przykładów dla każdej klasy:")
        for label, count in counter.items():
            print(f"{label}: {count}")

    def filter_by_class(self, class_name: str):
        filtered = [row for row in self.data if row[-1] == class_name]
        print(f"\nDane dla klasy {class_name}:")
        for row in filtered:
            print(row)

    def save_to_csv(self, data: List[List[str]], filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"\nDane zapisane do pliku {filename}")
