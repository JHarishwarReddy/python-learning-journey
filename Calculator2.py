while True:
        print("\n---Claculator---")    
        n1= float(input("first num: "))
        n2= float(input("second num: "))
        op= input("choose your operation (+, -, *, /)")

        if op== "+":
            result = round(n1+n2,2)
        elif op== "-":
            result = round(n1-n2,2)
        elif op== "*":
            result = round(n1*n2,2)
        elif op=="/":
            if n2==0:
                print("Error: Undefined(X/0, not possible)")
                continue
            else:
                result = round(n1/n2,2)
        else:
            print("Please choose one of these +,-,*,/")
            continue

        print(f"Ans {int(result) if result == int(result) else result}")

        again = input("Calculate again? (yes/no):  ")
        if again.lower()!= "yes":
             print("thanks and come again!")
             break 