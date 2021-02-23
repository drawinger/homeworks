
# ДОМАШКА ПО ГОДУ РОЖДЕНИЯ
# спросить год рождения

birth_date = int(input('Введите Ваш год рождения: '))

# уточнить желаемый год

desired_age = int(input('К какому году посчитать Ваш возраст?  '))

# расчитать желаемый год

if desired_age - birth_date > 0:
    print("Вам будет: ", desired_age - birth_date, ' года')
elif desired_age - birth_date == 0:
    print("Простите, Ваш возраст не изменился ¯\_(ツ)_/¯")
else:
    print("Путешествуете во времени?", desired_age - birth_date, ' года')

'''
# ДОМАШКА ПО ЗАРПЛАТАМ
# спросить зарплату у 3х человек

salary_person1 = int(input('Простите, какая у Вас зарплата?  '))
salary_person2 = int(input('Простите, а у Вас ?  '))
salary_person3 = int(input('А ваша зарплата?  '))

# считаем среднюю

average_salary = (salary_person1 + salary_person2 + salary_person3) / 3

# расчитать желаемый год

print("Дорогие члены семьи, Маркс просит всех быть равными и получать каждому по:", average_salary)

'''
