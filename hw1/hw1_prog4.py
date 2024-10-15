hawk = True
count = 0
while hawk:
    tuah = input("enter something: ")
    if tuah.isdigit():
        count = count + int(tuah)
    elif tuah == 'q':
        hawk = False
        print(count)
    else:
        print("invalid")
        
        