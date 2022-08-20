def areacalculator():
    _input_ = input("Enter the shape you want to calculate area of: ")
    area = 0
    pie = 3.14
    if _input_=="Square":
        s = int(input("Enter the lenth of side of square"))
        a = s*s
        print("The area of the square with value you have given is", a,"cm**")
    
    elif _input_=="Circle":
        r = int(input("Enter the radius of the circle"))
        b = 3.14*(r*r)
        print("The area of the square with value you have given is", b,"cm**")
    
    elif _input_=="Triangle":
        b = int(input("Enter the base of the triangle"))
        h = int(input("Enter the height of the triangle"))
        c = 0.5*b*h
        print("The area of the square with value you have given is", c,"cm**")
        
areacalculator()
