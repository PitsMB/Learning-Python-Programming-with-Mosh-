#While loop
get_help = input('>')

if get_help == 'help' or get_help == 'HELP':
    print ('start - to start the car')
    print ('stop - to stop the car')
    print ('quit - to exit')

end = True

while end:
    get_function = input('>')
    if get_function == 'start':
        print('Car started')
    elif get_function == 'stop':
        print('Car Stopped')
    elif get_function == 'quit':
        break
    else:
        print('I do not understand that')