#1. Составить список с числами от 0 до 1000, которые деляться без остатка на 3 и на 9. Список составить 2-мя
b = []
for i in range(1000):
	if i % 3 == 0 and i % 9 == 0:
		b.append(i)	
print(b)

c = []
a = 0
while a < 1000:
	c.append(a)
	a += 3
print(c)

#2.Составить словарь, где ключи - цифры от 65 до 122 (включительно), а значения - соответствующий символ из
#таблицы unicode :) (подсказка - chr()). Словарь составить 2-мя способами: при помощи цикла и при помощи 
#словарного включения;
a = {}
for k in range(65,122):
	a[k] = chr(k)
print(a)		

a = {}
k = 65
while k < 122:
	a[k] = chr(k)
	k += 1
print(a)



#1. Необходимо попросить пользователя ввести имя и фамилию, разделенную пробелом. На данный момент
#принимаем, что пользователь ответственный и сделает всё правильно :)
#2.Полученные данные нужно напечатать в формате (имя с Большой буквы (даже если пользователь ввёл с маленькой),
#логин - только маленькие буквы):
#"""Привет, {имя}. Твой логин в нашей системе {имя}_{фамилия}"""
#3.Полученное значение сохранить в словарь под ключом равным логину
#   в виде словаря (с ключами "name" and "surname"). Для Ивана Иванова результат будет 
#{
#    "иван_иванов": {
#        "name": "Иван", 
#        "surname": "Иванов"
#    }
#}

user_input = input("Введите имя и фамилию: ")
name_surname = user_input.split()
login_1 = user_input.lower()
login_2 = "_".join(login_1.split())

users = {

}

for user in name_surname:
	users['name'] = name_surname[0]
	users['surname'] = name_surname[1]

logins = {
	
}

logins[login_2] = users

print(logins)






