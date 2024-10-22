
import keyboards


first_name = keyboards.input_string('Enter name: ')
last_name =  keyboards.input_string('enter the last name: ')
age = keyboards.input_integer('enter the age: ')
salary = keyboards.input_real('enter the salary: ')
is_salary_hidden = keyboards.input_boolean('Hide salary? (y/n)')


print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('last name', last_name)
print('age', age)
if is_salary_hidden == "n":
    print('Salary:', salary)
