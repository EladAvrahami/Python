
#הערך שהמשתמש יכניס יהיה סטרינג ונמיר אותו לסוג אינט
wight= int( input('wight :'))
unit= input('(L)bs or (K)g :')
#השתמשתי באפר ככה שלא משנה אם היוזר יכניס אותו גדולה או קטנה התנאי יתקיים
if unit.upper() =="L":
    coverted=wight*0.45
    print(f" you are {coverted} kilos")
else:
    #/ - אחד יחזיר אינטגר //- יחזיר מסוג פלואוט
    coverted=wight/0.45
    print(f"YOU ARE {coverted} pounds")