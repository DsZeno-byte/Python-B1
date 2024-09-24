while True:
    userInput=input("Enter A number (or use 'exit' to quit):")

    if userInput.lower()== 'exit':
        break
    
    try :
        Number=float(userInput)

        if Number>0 :
             print("This is a Positive Number.")
        elif Number<0:
             print("This is a Negative Number.")
        else:
         print("The Number is Zero.")
    
    except ValueError:
         print("Invalid input or use  'exit' to quit.")


