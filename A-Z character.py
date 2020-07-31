import time

def word():
    def ver():
        def print_row(*col):
            for i in range(5):
                if i in col:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        def A():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)

        def B():
            print_row(0,1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3)

        def C():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0)
            print_row(0)
            print_row(0)
            print_row(0,4)
            print_row(1,2,3)

        def D():
            print_row(0,1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3)

        def E():
            print_row(0,1,2,3,4)
            print_row(0)
            print_row(0)
            print_row(0,1,2,3,4)
            print_row(0)
            print_row(0)
            print_row(0,1,2,3,4)

        def F():
            print_row(0,1,2,3)
            print_row(0)
            print_row(0)
            print_row(0,1,2,3)
            print_row(0)
            print_row(0)
            print_row(0)

        def G():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0)
            print_row(0,2,3,4)
            print_row(0,4)
            print_row(0,4)
            print_row(1,2,3)


        def H():
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)

        def I():
            print_row(0,1,2,3,4)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(0,1,2,3,4)

        def J():
            print_row(0,1,2,3,4)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(0,2)
            print_row(1)

        def K():
            print_row(0,4)
            print_row(0,3)
            print_row(0,2)
            print_row(0,1)
            print_row(0,2)
            print_row(0,3)
            print_row(0,4)

        def L():
            print_row(0)
            print_row(0)
            print_row(0)
            print_row(0)
            print_row(0)
            print_row(0)
            print_row(0,1,2,3,4)

        def M():
            print_row(0,4)
            print_row(0,1,3,4)
            print_row(0,2,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)

        def N():
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,4)
            print_row(0,2,4)
            print_row(0,3,4)
            print_row(0,4)
            print_row(0,4)

        def O():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(1,2,3)

        def P():
            print_row(0,1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3)
            print_row(0)
            print_row(0)
            print_row(0)

        def Q():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,2,4)
            print_row(1,3,4)
            print_row(1,2,3,4)

        def R():
            print_row(0,1,2,3)
            print_row(0,4)
            print_row(0,4)
            print_row(0,1,2,3)
            print_row(0,2)
            print_row(0,3)
            print_row(0,4)

        def S():
            print_row(1,2,3)
            print_row(0,4)
            print_row(0)
            print_row(0,1,2,3)
            print_row(4)
            print_row(0,4)
            print_row(1,2,3)

        def T():
            print_row(0,1,2,3,4)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)

        def U():
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(0,4)
            print_row(1,2,3)

        def V():
            for i in range(5):
                print_row(0,4)
            print_row(1,3)
            print_row(2)

        def W():
            for i in range(4):
                print_row(0,4)
            print_row(0,2,4)
            print_row(0,1,3,4)
            print_row(0,4)

        def X():
            print_row(0,4)
            print_row(0,4)
            print_row(1,3)
            print_row(2)
            print_row(1,3)
            print_row(0,4)
            print_row(0,4)

        def Y():
            print_row(0,4)
            print_row(0,4)
            print_row(1,3)
            print_row(2)
            print_row(2)
            print_row(2)
            print_row(2)

        def Z():
            print_row(0,1,2,3,4)
            print_row(4)
            print_row(3)
            print_row(2)
            print_row(1)
            print_row(0)
            print_row(0,1,2,3,4)

        import time
        word= input("Enter a word : ")
        u = word.upper()
        for ch in u:
            exec(ch+'()')
            print()

    def hor():
        def print_row(*col):
            for i in range(5):
                if i in col:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

        def A0():
            print_row(1,2,3)
        def A1():
            print_row(0,4)
        def A2():
            print_row(0,4)
        def A3():
            print_row(0,1,2,3,4)
        def A4():
            print_row(0,4)
        def A5():
            print_row(0,4)
        def A6():
            print_row(0,4)

        def B0():
            print_row(0,1,2,3)
        def B1():
            print_row(0,4)
        def B2():
            print_row(0,4)
        def B3():
            print_row(0,1,2,3)
        def B4():
            print_row(0,4)
        def B5():
            print_row(0,4)
        def B6():
            print_row(0,1,2,3)

        def C0():
            print_row(1,2,3)
        def C1():
            print_row(0,4)
        def C2():
            print_row(0)
        def C3():
            print_row(0)
        def C4():
            print_row(0)
        def C5():
            print_row(0,4)
        def C6():
            print_row(1,2,3)

        def D0():
            print_row(0,1,2,3)
        def D1():
            print_row(0,4)
        def D2():
            print_row(0,4)
        def D3():
            print_row(0,4)
        def D4():
            print_row(0,4)
        def D5():
            print_row(0,4)
        def D6():
            print_row(0,1,2,3)

        def E0():
            print_row(0, 1, 2, 3, 4)
        def E1():
            print_row(0)
        def E2():
            print_row(0)
        def E3():
            print_row(0,1,2,3,4)
        def E4():
            print_row(0)
        def E5():
            print_row(0)
        def E6():
            print_row(0,1,2,3,4)

        def F0():
            print_row(0,1,2,3)
        def F1():
            print_row(0)
        def F2():
            print_row(0)
        def F3():
            print_row(0,1,2,3)
        def F4():
            print_row(0)
        def F5():
            print_row(0)
        def F6():
            print_row(0)

        def G0():
            print_row(1,2,3)
        def G1():
            print_row(0,4)
        def G2():
            print_row(0)
        def G3():
            print_row(0,2,3,4)
        def G4():
            print_row(0,4)
        def G5():
            print_row(0,4)
        def G6():
            print_row(1,2,3)

        def H0():
            print_row(0,4)
        def H1():
            print_row(0,4)
        def H2():
            print_row(0,4)
        def H3():
            print_row(0,1,2,3,4)
        def H4():
            print_row(0,4)
        def H5():
            print_row(0,4)
        def H6():
            print_row(0,4)

        def I0():
            print_row(0,1,2,3,4)
        def I1():
            print_row(2)
        def I2():
            print_row(2)
        def I3():
            print_row(2)
        def I4():
            print_row(2)
        def I5():
            print_row(2)
        def I6():
            print_row(0,1,2,3,4)

        def J0():
            print_row(0,1,2,3,4)
        def J1():
            print_row(2)
        def J2():
            print_row(2)
        def J3():
            print_row(2)
        def J4():
            print_row(2)
        def J5():
            print_row(0,2)
        def J6():
            print_row(1)

        def K0():
            print_row(0,4)
        def K1():
            print_row(0,3)
        def K2():
            print_row(0,2)
        def K3():
            print_row(0,1)
        def K4():
            print_row(0,2)
        def K5():
            print_row(0,3)
        def K6():
            print_row(0,4)

        def L0():
            print_row(0)
        def L1():
            print_row(0)
        def L2():
            print_row(0)
        def L3():
            print_row(0)
        def L4():
            print_row(0)
        def L5():
            print_row(0)
        def L6():
            print_row(0,1,2,3,4)

        def M0():
            print_row(0,4)
        def M1():
            print_row(0,1,3,4)
        def M2():
            print_row(0,2,4)
        def M3():
            print_row(0,4)
        def M4():
            print_row(0,4)
        def M5():
            print_row(0,4)
        def M6():
            print_row(0,4)

        def N0():
            print_row(0, 4)
        def N1():
            print_row(0,4)
        def N2():
            print_row(0,1,4)
        def N3():
            print_row(0,2,4)
        def N4():
            print_row(0,3,4)
        def N5():
            print_row(0,4)
        def N6():
            print_row(0,4)

        def O0():
            print_row(1, 2, 3)
        def O1():
            print_row(0,4)
        def O2():
            print_row(0,4)
        def O3():
            print_row(0,4)
        def O4():
            print_row(0,4)
        def O5():
            print_row(0,4)
        def O6():
            print_row(1,2,3)

        def P0():
            print_row(0,1,2,3)
        def P1():
            print_row(0,4)
        def P2():
            print_row(0,4)
        def P3():
            print_row(0,1,2,3)
        def P4():
            print_row(0)
        def P5():
            print_row(0)
        def P6():
            print_row(0)

        def Q0():
            print_row(1, 2, 3)
        def Q1():
            print_row(0,4)
        def Q2():
            print_row(0,4)
        def Q3():
            print_row(0,4)
        def Q4():
            print_row(0,2,4)
        def Q5():
            print_row(1,3,4)
        def Q6():
            print_row(1,2,3,4)

        def R0():
            print_row(0,1,2,3)
        def R1():
            print_row(0,4)
        def R2():
            print_row(0,4)
        def R3():
            print_row(0,1,2,3)
        def R4():
            print_row(0,2)
        def R5():
            print_row(0,3)
        def R6():
            print_row(0,4)

        def S0():
            print_row(1,2,3)
        def S1():
            print_row(0,4)
        def S2():
            print_row(0)
        def S3():
            print_row(0,1,2,3)
        def S4():
            print_row(4)
        def S5():
            print_row(0,4)
        def S6():
            print_row(1,2,3)

        def T0():
            print_row(0,1,2,3,4)
        def T1():
            print_row(2)
        def T2():
            print_row(2)
        def T3():
            print_row(2)
        def T4():
            print_row(2)
        def T5():
            print_row(2)
        def T6():
            print_row(2)

        def U0():
            print_row(0,4)
        def U1():
            print_row(0,4)
        def U2():
            print_row(0,4)
        def U3():
            print_row(0,4)
        def U4():
            print_row(0,4)
        def U5():
            print_row(0,4)
        def U6():
            print_row(1,2,3)

        def V0():
            print_row(0,4)
        def V1():
            print_row(0,4)
        def V2():
            print_row(0,4)
        def V3():
            print_row(0,4)
        def V4():
            print_row(0,4)
        def V5():
            print_row(1,3)
        def V6():
            print_row(2)

        def W0():
            print_row(0,4)
        def W1():
            print_row(0,4)
        def W2():
            print_row(0,4)
        def W3():
            print_row(0,4)
        def W4():
            print_row(0,2,4)
        def W5():
            print_row(0,1,3,4)
        def W6():
            print_row(0,4)

        def X0():
            print_row(0,4)
        def X1():
            print_row(0,4)
        def X2():
            print_row(1,3)
        def X3():
            print_row(2)
        def X4():
            print_row(1,3)
        def X5():
            print_row(0,4)
        def X6():
            print_row(0,4)

        def Y0():
            print_row(0,4)
        def Y1():
            print_row(0,4)
        def Y2():
            print_row(1,3)
        def Y3():
            print_row(2)
        def Y4():
            print_row(2)
        def Y5():
            print_row(2)
        def Y6():
            print_row(2)

        def Z0():
            print_row(0,1,2,3,4)
        def Z1():
            print_row(4)
        def Z2():
            print_row(3)
        def Z3():
            print_row(2)
        def Z4():
            print_row(1)
        def Z5():
            print_row(0)
        def Z6():
            print_row(0,1,2,3,4)



        word = input("Enter a word :")
        u = word.upper()
        import time
        for k in range(7):
            for ch in u :
                exec (ch+str(k)+'()')
                print(end="   ")
            print()



    x = input("IF WORD PRINT TO VERTICAL THEN PRESS \'V\' and word print horizonatal THEN PRESS \'H\' :")
    u = x.upper()
    if u == 'H' or u == 'h':
        hor()
    elif u == 'V' or u == 'v':
        ver()
    else:
        print("INPUT NOT VALID......")
        print("ONLY YOU CAN PRESS \'H\' OR \'V\' ")
    again()




def again():
    wodag = input("DO YOU WANT TO PRINT WORD AGAIN ?\n"
                  "PLEASE TYPE \'Y\' FOR YES OR \'N\' FOR NO : ")
    if wodag == 'Y' or wodag == 'y':
        word()
    elif wodag == 'N' or wodag == 'n':
        print("THANK YOU")
        print("SEE YOU LATER")
    else:
        print("type a invaliad key")

word()
print(time.process_time())