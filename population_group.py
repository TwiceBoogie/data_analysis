# A module containing the PopulationGroup class and related code

class PopulationGroup:

    def __init__(self, category, male_count, female_count, total_count):
        self.category = str(category)
        self.male_count = int(male_count)
        self.female_count = int(female_count)
        self.total_count = int(total_count)

    def calculate_category_percentage(self):
        return round((self.total_count/951982) * 100, 2)


def main():
    print("Unit testing output follows...\n")
    print("Testing the constructor:")
    category_age = "40-44"
    male_count = 28176
    female_count = 29271
    total_count = 57447
    test = PopulationGroup(category_age, male_count, female_count, total_count)

    print(test.category)
    print(test.male_count)
    print(test.female_count)
    print(test.total_count)

    print("\nTesting the calculate_category_percentage method")
    print(test.calculate_category_percentage())


if __name__ == "__main__":
    main()
