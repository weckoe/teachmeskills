def decorator(func):
    def wrapper():
        user_input = input("Введите номер телефона: ")
        if "+" not in user_input:
            users_correct_input = "+" + user_input
            print(users_correct_input)
        else:
            print("Правильный номер телефона.")
        if "+375" not in user_input:
            users_correct_input = "+375" + user_input
            print(users_correct_input)
        else:
            print("Правильный номер телефона.")
        main_function()
    return wrapper

@decorator
def main_function(number_from_user):
    print("number_from_user")


main_function()



dictionary = {}

def decorator(url = ""):
    def wrapper_1(func):
        def wrapper_2():
            
            dictionary[url] = func.__name__
            print(dictionary)
            func("some_text")
        return wrapper_2
    return wrapper_1

@decorator("/home/")
def my_function(some_text):
    print(some_text)


my_function()
