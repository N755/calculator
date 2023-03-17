import logging
logging.basicConfig(level=logging.DEBUG, filename="calculatorlogfile.log")
addition_count = 0
subtraction_count = 0
multiplication_count = 0
division_count = 0

while True:
    print("For EXIT enter 0")
    operation = input("Enter the operation using the number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: ")
    if operation == '0':
        break   
    if operation not in ['0','1','2','3','4']:
        print('Wrong operator!')
        continue
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if operation == '1':
        addition_count += 1
        logging.info(f'Addition operation with {num1} and {num2}')
        print('Addition operation')
        result = num1 + num2 
    elif operation == '2':
        subtraction_count += 1
        logging.info(f'Subtraction operation with {num1} and {num2}')
        print ('Subtraction operation')
        result = num1 - num2
    elif operation == '3':
        multiplication_count += 1
        logging.info(f'Multiplication operation with {num1} and {num2}')
        print ('Multiplication operation')
        result = num1 * num2 
    elif operation == '4':
        division_count += 1
        logging.info(f'Division operation with {num1} and {num2}')
        if num2 == 0:
            logging.warning(f"Second number is {num2}. You cannot divide by {num2}.")
            print("You cannot divide by 0.")
            print(None)
            continue 
        else:
            print ('Division operation')
            result = num1 / num2
    
        
        
    logging.info(f"Result: {num1} i {num2} equal {result}")
    logging.info(f"Addition count: {addition_count}")
    logging.info(f"Subtraction count: {subtraction_count}")
    logging.info(f"Multiplication count: {multiplication_count}")
    logging.info(f"Division count: {division_count}")
    print(f"{num1} i {num2}")
    print (f"Result: {result}")


    
   