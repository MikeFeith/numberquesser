import pandas as pd
a= {'row1': [1,3,5,7,9,11,13,15], 'row2': [17,19,21,23,25,27,29,31],'row3': [33,35,37,39,41,43,45,47], 'row4': [49,51,53,55,57,59,61,63]}
b= {'row1': [2,3,6,7,10,11,14,15], 'row2': [18,19,22,23,26,27,30,31], 'row3': [34,35,38,39,42,43,46,47], 'row4': [50,51,54,55,58,59,62,63]}
c= {'row1': [4,5,6,7,12,13,14,15], 'row2': [20,21,22,23,28,29,30,31], 'row3': [36,37,38,39,44,45,46,47], 'row4': [52,53,54,55,60,61,62,63]}
d= {'row1': [8,9,10,11,12,13,14,15], 'row2': [24,25,26,27,28,29,30,31], 'row3': [40,41,42,43,44,45,46,47], 'row4': [56,57,58,59,60,61,62,63]}
e= {'row1': [16,17,18,19,20,21,22,23], 'row2': [24,25,26,27,28,29,30,31], 'row3': [48,49,50,51,52,53,54,55], 'row4': [56,57,58,59,60,61,62,63]}
f= {'row1': [32,33,34,35,36,37,38,39], 'row2': [40,41,42,43,44,45,46,47], 'row3': [48,49,50,51,52,53,54,55], 'row4': [56,57,58,59,60,61,62,63]}
global resultaat
resultaat= int(0)

def guesser(cardnr):
    global resultaat
    df= pd.DataFrame(eval(cardnr))
    print(df.to_string(index=False))
    cardres= input("zit je nummer in dit veld? Y/N")
    if cardres == "Y" or cardres == "y":
        resultaat= resultaat + df['row1'].iloc[0]
    else: return

cardarray = array = ['a','b','c','d','e','f']
for i in cardarray:
    guesser(i)
print("Jouw nummer is: " + str(resultaat))
