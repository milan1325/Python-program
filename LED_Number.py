def led_nnumber():
    ZERO = ['# '*3] + ['#   # ']*5 + ['# '*3]
    ONE = ['  #   '] + ['# #   '] + ['  #   ']*4 + ['# '*3]
    TWO = ['# '*3] + ['    # ']*2 + ['# '*3] + ['#     ']*2 + ['# '*3]
    THREE =  ['# '*3] + ['    # ']*2 + ['# '*3] + ['    # ']*2 + ['# '*3]
    FOUR = ['#   # ']*3 + ['# '*3] + ['    # ']*3
    FIVE = ['# '*3] + ['#     ']*2 + ['# '*3] + ['    # ']*2 + ['# '*3]
    SIX = ['# '*3] + ['#     ']*2 + ['# '*3] + ['#   # ']*2 + ['# '*3]
    SEVEN = ['# '*3] + ['    # ']*3 + ['  #   '] + ['#     '] + ['#     ']
    EIGHT = ['# '*3] + ['#   # ']*2 + ['# '*3] + ['#   # ']*2 + ['# '*3]
    NINE = ['# '*3] + ['#   # ']*2 + ['# '*3] + ['    # ']*2 + ['# '*3]

    NUMBERS = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]

    def hases(number,line):
        return NUMBERS[number][line]

    number = input("Enter a Number : ")
    print()

    while not number.isdigit():
        number = input("Not a Number, Enter Again : ")

    for i in range(7):
        for n in number:
            print(hases(int(n),i),end="  ")
        print()

if __name__ == "__main__":
    led_nnumber()

    while True:
        y_or_n_input = input("\nDo U Want To Print Again?\nIf \'Yes\'Press \'y\' Otherwise Press \'n\' : ")

        if y_or_n_input == 'Y' or y_or_n_input == 'y':
            led_nnumber()
        elif y_or_n_input == 'N' or y_or_n_input == 'n':
            print("\n..........Thanks For Choosing \'LED_NUMBER\' Created By Milan_Hingu..........\n")
            exit()
        else:
            print("Wrong input, Enter Again...")