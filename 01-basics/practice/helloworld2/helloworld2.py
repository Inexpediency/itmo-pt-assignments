def greetings(input, print):
    """Функция приветствия"""
    
    s = input('What is your name?')
    
    if s.isalpha() and s[0].isupper():

        if len(s) >= 2 and s[1:].islower():
            print("Hello, {}!".format(s))
        
        elif len(s) == 1:
            print("Hello, {}!".format(s))

        else:
            print("Hello, World!")

    else:
        print("Hello, World!")
