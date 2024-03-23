# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    i = 0
    j = 0
    for words in range(5):
        if words == 0 or words == 2:
            print(f'{name}' * 7 + ' ' +
                  f'{"U"}' + "      " + f'{"U"}')
        else:
            print(f'{name}' * 2 + ' \t    ' +
                  f'{"U"}' + "      " + f'{"U"}')


    # print(f'{name}' * 6 +' \t ' +f'{secondname}' +'\t\t\t' +f'{secondname}')  # Press ⌘F8 to toggle the breakpoint.
    # print(f'{name}' * 2 +' \t\t ' +f'{secondname}' +'\t\t\t' +f'{secondname}')
    # print(f'{name}' * 6 +' \t ' +f'{secondname}' +'\t\t\t' +f'{secondname}')
    # print(f'{name}' * 2 +' \t\t ' +f'{secondname}' +'\t\t  ' +f'{secondname}')
    # print(f'{name}' * 2 +' \t\t\t ' +f'{secondname}' + f'{secondname}' + f'{secondname}')secondname


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('F')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
