#task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  
        self.__allocated_budget = allocated_budget  
        self.__remaining_budget = allocated_budget 

#task 2
    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, name):
        if isinstance(name, str) and name.strip() != "":
            self.__category_name = name
        else:
            print("Invalid category name. Please provide a valid string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, budget):
        if isinstance(budget, (int, float)) and budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  
        else:
            print("Invalid budget amount. Please provide a positive number.")

#task 3
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"\nExpense of ${amount} added to {self.__category_name}. Remaining budget: ${self.__remaining_budget}\n")
            else:
                print(f"Insufficient funds. Cannot deduct ${amount}. Remaining budget: ${self.__remaining_budget}")
        else:
            print("Invalid expense amount. Please provide a positive number.")

#task 4
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}\n")


food_category = BudgetCategory("Food", 500)

food_category.add_expense(100)

food_category.display_category_summary()

food_category.set_allocated_budget(600)

food_category.display_category_summary()