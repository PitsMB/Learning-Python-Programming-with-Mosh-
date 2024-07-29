#While loop
end = True
car_started = False
car_stopped = False
while end:
    get_function = input('>')
    
    if get_function == 'start':
        if car_started == True:
            print('Car already started')
            continue
        car_started = True
        car_stopped = False
        print('Car started')
    elif get_function == 'stop':
        if car_stopped == True:
            print('Car already stopped')
            continue
        car_stopped = True
        car_started = False
        print('Car Stopped')
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