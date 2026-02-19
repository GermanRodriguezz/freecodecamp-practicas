first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
# Recuerde que las cadenas son inmutables; por lo tanto, 
# esta operación no modifica la cadena original. 
# En cambio, crea una nueva cadena y la reasigna a la variable
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is '
# si quiero concatenar al final de employee_info la variable employee_age
# aparecera el error typeError porque python no permite concatenar
# textos y numeros directamente, para eso convierte el numero en cadena
employee_info += str(employee_age) + ' years old'
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
# python 3.6 introdujo las cadenas F', se pueden colocar variables
# y expresiones dentro de campos de reemplazo representados por llaves {}

position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]

year_code = employee_code[4:8] # toma de la pos 4 a la 8
initials = employee_code[9:11] # toma de la pos 9 a la 11
print(year_code) # imprime 2026
print(initials) # imprime JD

#También puedes usar números negativos para cortar desde el final de una cadena. Por ejemplo, 
# -1se refiere al último carácter, -2se refiere al penúltimo carácter, etc.
# Para obtener los tres últimos caracteres de una cadena, puede usar string[-3:].
last_three = employee_code[-3:]
print(last_three)
