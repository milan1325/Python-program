#     0 1 2 3 4
# 0     * * *
# 1   *       *
# 2   * * * * *
# 3   *       *
# 4   *       *

# for i in range(0, 5):
#     for j in range(0, 5):
#         if ((j == 0 or j == 4) and i != 0) or ((i == 0 or i == 2) and (j > 0 and j < 4)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")




print(" star pattern 2 :")
#     0 1 2 3 4
# 0   * * * *
# 1   *       *
# 2   *       *
# 3   * * * *
# 4   *       *
# 5   *       *
# 6   * * * *

# for i in range(7):
#     for j in range(5):
#         if (j==0) or (j==4 and (i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")


print("star pattern 3 :")
#     0 1 2 3 4
# 0   * * * * *
# 1   *
# 2   *
# 3   *
# 4   *
# 5   *
# 6   * * * * *

# for i in range(7):
#     for j in range(5):
#         if (j==0) or (i==0 or i==6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")





print("star pattern 4 :")
#     0 1 2 3 4
# 0   * * * *
# 1   *       *
# 2   *       *
# 3   *       *
# 4   *       *
# 5   *       *
# 6   * * * *

for i in range(7):
    for j in range(5):
        if (j==0) or (j==4 and i!=0 and i!=6) or ((i==0 or i==6) and (j>0 and j<4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")






