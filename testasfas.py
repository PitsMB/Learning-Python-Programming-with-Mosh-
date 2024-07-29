#While loop
end = True
car_started = False
while end:
    get_function = input('>')
    
    if get_function == 'start' and not car_started:
        print("Car started")
        car_started = True
    elif get_function == 'start':
        print("Car already started.")
    elif get_function == 'stop' and car_started:
        print("Car stopped")
        car_started = False
    elif get_function == 'stop':
        print("Car already stopped")
    elif get_function == 'quit':
        break
    elif get_function == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    else:
        print('I do not understand that')