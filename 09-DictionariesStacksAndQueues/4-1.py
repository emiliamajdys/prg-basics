import queue

# Creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    print()

    if menu == '1':
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)
        print(f'File "{file_name}" added to the print queue.')
        print()
    
    elif menu == '2':
        # Check if the print queue is not empty
        if not files_to_print.empty():
            file_to_print = files_to_print.get()
            print(f'File "{file_to_print}" is currently being printed. Please wait!')
        else:
            print('The print queue is empty. No files to print.')
        print()

    elif menu == '0':
        print('Exiting the program. Goodbye!')
        break

    else:
        print('Invalid option. Please select 1, 2, or 0.')
        print()
