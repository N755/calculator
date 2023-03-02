import logging
logging.basicConfig(level=logging.DEBUG, filename="logfile.log")

operation = input("Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення:")
num1 = int(input("Введи перше число: "))
num2 = int(input("Введи друге число: "))
operator1 = 'Додаю'
operator2 = 'Віднімаю'
operator3 = 'Множу'
operator4 = 'Ділю'

def calculator():
    if operation == '1':
        print (operator1), 
        result = num1 + num2
    elif operation == '2':
        print (operator2)
        result = num1 - num2
    elif operation == '3':
        print (operator3)
        result = num1 * num2
    elif operation == '4':
        print (operator4)
        result = num1 / num2
        return
        
    logging.info(f" {num1} i {num2} ")
    print(f" {num1} i {num2} ")
    print (f"Результат: {result}")
calculator()