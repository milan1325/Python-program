# import datetime
# d = datetime.datetime.now()

# do you want to print date and time then we will use -->>  str([str(d)]),":"




n = int(input("Enter a number from 0 to 99999 : "))
word_to_nine = ["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE","THIRTEEN","FOURTEEN",
"FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN"]
# print(word_to_nine[n])
word_to_ten =["","","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINETY"]
word_to_hundred = ["","ONE HUNDRED","TWO HUNDRED","THREE HUNDRED","FOUR HUNDRED","FIVE HUNDRED","SIX HUNDRED","SEVEN HUNDRED",
"EIGHT HUNDRED","NINE HUNDRED"]
word_to_thousand = ["","ONE THOUSAND","TWO THOUSAND","THREE THOUSAND","FOUR THOUSAND","FIVE THOUSAND","SIX THOUSAND","SEVEN THOUSAND",
"EIGHT THOUSAND","NINE THOUSAND"]
word_to_tenthousand = ["","TEN THOUSAND","TWENTY THOUSAND","THIRTY THOUSAND","FOURTY THOUSAND","FIFTY THOUSAND","SIXTY THOUSAND",
"SEVENTY THOUSAND","EIGHTY THOUSAND","NINETY THOUSAND"]



if n==0:
    print("ZERO")
elif n<=19:
    print(word_to_nine[n])
elif n<=99:
    print(word_to_ten[n//10] + " " + word_to_nine[n%10])
elif n<=999:
    print(word_to_hundred[n//100] + " " + word_to_ten[(n//10)%10] + word_to_nine[(n%100)%10])
elif n<=9999:
    if (n//100)%10 == 0:
        print(word_to_thousand[n//1000] + " " + word_to_hundred[(n//100)%10] + word_to_ten[(n%100)//10] + word_to_nine[(n%1000)%10])
    else:
        print(word_to_thousand[n//1000] + " " + word_to_hundred[(n//100)%10] + " " + word_to_ten[(n%100)//10] + word_to_nine[(n%1000)%10])
elif n<=99999 :
    if n//1000<=19:
        print(word_to_nine[n//1000] + " THOUSAND" + " " + word_to_hundred[(n//100)%10] + " " + word_to_ten[(n//10)%10] + word_to_nine[n%10])
    elif n//1000<=99:
        print(word_to_ten[n//10000] + word_to_nine[(n//1000)%10] + " THOUSAND" + " " + word_to_hundred[(n//100)%10] + " " + word_to_ten[(n//10)%10] + word_to_nine[n%10])
else:
    print("input only number from 0 to 99999")

'''
20001
20012
20123
'''