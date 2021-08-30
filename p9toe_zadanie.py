class Converter:
	def __init__(self, any_arg):
		self.any_arg = any_arg

	def to_int(self):
		converted_any_arg = int(self.any_arg)
		print(converted_any_arg)


	def to_list(self):
		converted_any_arg = self.any_arg.split()
		print(converted_any_arg)

	def to_string(self):
		converted_any_arg = str(self.any_arg)
		print(converted_any_arg)
		print(type(converted_any_arg))

c1 = Converter("2")

c1.to_int()
c1.to_list()
c1.to_string()

class Employee:
	def __init__(self, name, surname, salary):
		self.name = name
		self.surname = surname
		self.salary = salary
       
	def year_salary(self):
		employee_salary = 12 * self.salary
		return employee_salary

    	

class Manager(Employee):
	def __init__(self, name, surname, salary, bonus):
		super().__init__(name, surname, salary)
		self.bonus = bonus

	def bonus_salary(self):
		salary_without_bonus = self.year_salary()
		print(f"Зарплата без бонуса {salary_without_bonus}")
		salary_with_bonus = ((salary_without_bonus * self.bonus)//100) + salary_without_bonus
		print(f"Зарплата с бонусом {salary_with_bonus}")

james = Manager("James", "Bond", 2000, 20)

james.bonus_salary()