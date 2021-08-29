import re



# 1. Найдите все натуральные числа (возможно, окружённые буквами);

# find_numbers = re.findall(r"\d", r"44лрп2j.5паывnk 9куц4")


# print(find_numbers)


# 2. Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);

# find_upper_register = re.findall(r"[А-Я]", r"аааБББввв")


# print(find_upper_register)


# 3. Найдите слова, в которых есть русская буква, а когда-нибудь за ней цифра;
# find = re.findall(r"[а-я][0-9]", "аыв43афы23авфы45")

# print(find)

#4. Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова);

# find = re.findall(r"\b[A-ZА-Я]\w*", "ASSA JL ОВЛЫ ")

# print(find)

#5 Найдите слова, которые начинаются на гласную (\b — граница слова);;

# find= re.findall(r"\b[AEIOUY]\w*", "ASDE IFDS ERTY Afds fdsfsd")

# print(find)

#6 Найдите все натуральные числа, не находящиеся внутри или на границе слова;
# find = re.findall(r"\d\b", "dfs4gfd dsf3y 9fkds4")

# print(find)


#7 Найдите строчки, в которых есть символ * (. — это точно не конец строки!); 
# find = re.findall(r"\w*[*(.]\w*", "fds(kl ds.re po*з fds 432f")

# print(find)

#8 Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки;


# find = re.findall(r"[(]\w+[)]", r"(fdsfsd) fdsaf (fds00)fds") #r"[(]\w+[)]\w+" наверное, можно и так

# print(find)



#9. Найдите пустые строчки;

find = re.findall(r"\s", r"fds asd daasd dasdas")

print(find)


