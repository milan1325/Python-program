# ..................................................CHARACTERS..................................................................................
A = ['  ' + '* '*3 + '  '] + ['*       * ']*2 + ['* '*5] + ['*       * ']*3
B = ['* '*4 + '  '] + ['*       * ']*2 + ['* '*4 + '  '] + ['*       * ']*2 + ['* '*4 + '  ']
C = ['  ' + '* '*4] + ['*         ']*5 + ['  ' + '* '*4]
D = ['* '*4 + '  ' ] + ['*       * ']*5 + ['* '*4 + '  ' ]
E = ['* '*5] + ['*         ']*2 + ['* '*5] + ['*         ']*2 + ['* '*5]
F = ['* '*5] + ['*         ']*2 + ['* '*4 + '  '] + ['*         ']*3
G = ['  ' + '* '*3 + '  '] + ['*       * '] + ['*         '] + ['*   * * * '] + ['*       * ']*2 + ['  ' + '* '*3 + '  ']
H = ['*       * ']*3 + ['* '*5] + ['*       * ']*3
I = ['* '*5] + ['    *     ']*5 + ['* '*5]
J = ['* '*5] + ['      *   ']*4 + ['*     *   '] + ['  * *     ']
K = ['*       * '] + ['*     *   '] + ['*   *     '] + ['* *       '] + ['*   *     '] + ['*     *   '] + ['*       * ']
L = ['*         ']*6 + ['* '*5]
M = ['*       * '] + ['* *   * * '] + ['*   *   * '] + ['*       * ']*4
N = ['*       * ']*2 + ['* *     * '] + ['*   *   * '] + ['*     * * '] + ['*       * ']*2
O = ['  ' + '* '*3 + '  '] + ['*       * ']*5 + ['  ' + '* '*3 + '  ']
P = ['* '*4 + '  ' ] + ['*       * ']*2 + ['* '*4 + '  '] + ['*         ']*3
Q = ['  ' + '* '*3 + '  '] + ['*       * ']*3 + ['*   *   * '] + ['*     * * '] + ['  ' + '* '*4]
R = ['* '*4 + '  ' ] + ['*       * ']*2 + ['* '*4 + '  ' ] + ['*   *     '] + ['*     *   '] + ['*       * ']
S = ['  ' + '* '*3 + '  '] + ['*       * '] + ['*         '] + ['  ' + '* '*3 + '  '] + ['        * '] + ['*       * '] + ['  ' + '* '*3 + '  ']
T = ['* '*5] + ['    *     ']*6
U = ['*       * ']*6 + ['  ' + '* '*3 + '  ']
V = ['*       * ']*5 + ['  *   *   '] + ['    *     ']
W = ['*       * ']*4 + ['*   *   * '] + ['* *   * * '] + ['*       * ']
X = ['*       * ']*2 + ['  *   *   '] + ['    *     '] + ['  *   *   '] + ['*       * ']*2
Y = ['*       * ']*3 + ['  *   *   '] + ['    *     ']*3
Z = ['* '*5] + ['        * '] + ['      *   '] + ['    *     '] + ['  *       '] + ['*         '] + ['* '*5]


# ..................................................NUMBERS..................................................................................
ZERO = ['  ' + '* '*3 + '  '] + ['* *     * '] + ['*       * '] + ['*   *   * '] + ['*       * '] + ['*     * * '] + ['  ' + '* '*3 + '  ']
ONE = ['    *     '] + ['  * *     '] + ['    *     ']*4 + ['* '*5]
TWO = ['  ' + '* '*3 + '  '] + ['*       * '] + ['        * '] + ['  ' + '* '*3 + '  '] + ['*         ']*2 + ['* '*5]
THREE =  ['  ' + '* '*3 + '  '] + ['*       * '] + ['        * '] + ['  ' + '* '*3 + '  '] + ['        * '] + ['*       * '] + ['  ' + '* '*3 + '  ']
FOUR = ['      *   '] + ['    * *   '] + ['  *   *   '] + ['*     *   '] + ['* '*5] + ['      *   ']*2
FIVE = ['* '*5] + ['*         ']*2 + ['* '*4 + '  '] + ['        * '] + ['*       * '] + ['  ' + '* '*3 + '  ']
SIX = ['  ' + '* '*3 + '  '] + ['*       * '] + ['*         '] + ['* '*4 + '  '] + ['*       * ']*2 + ['  ' + '* '*3 + '  ']
SEVEN = ['* '*5] + ['        * '] + ['      *   '] + ['    *     '] + ['  *       '] + ['*         ']*2
EIGHT = ['  ' + '* '*3 + '  '] + ['*       * ']*2 + ['  ' + '* '*3 + '  '] + ['*       * ']*2 + ['  ' + '* '*3 + '  ']
NINE = ['  ' + '* '*3 + '  '] + ['*       * ']*2 + ['  ' + '* '*4] + ['        * '] + ['*       * '] + ['  ' + '* '*3 + '  ']




def character(char,line):
    return CHARACTER[char][line]

def digit(number,line):
    return NUMBERS[number][line]





if __name__ == "__main__":
    
    CHARACTER = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

    dict = {
            'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 
            's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25
            }


    NUMBERS = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]



    def Number_and_character_printing_many_time():


        number_character = input("Enter a Number/Digit/Both : ").lower()


        for i in range(7):
            for n in number_character:
                if n.isdigit():
                    print(digit(int(n),i),end="  ")
                else:
                    print(character(dict[n],i),end="  ")
            print()



Number_and_character_printing_many_time()

while True:
        y_or_n_input = input("\nDo U Want To Print Again?\nIf \'Yes\'Press \'y\' Otherwise Press \'n\' : ")

        if y_or_n_input == 'Y' or y_or_n_input == 'y':
            Number_and_character_printing_many_time()
        elif y_or_n_input == 'N' or y_or_n_input == 'n':
            print("\n..........Thanks For Choosing Number and character Project Created By Milan_Hingu..........\n")
            exit()
        else:
            print("Wrong input, Enter Again...")


    

    

