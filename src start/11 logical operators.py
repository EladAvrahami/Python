# אם יש ללקוח הכנסות גבוהוות וגם עוש טוב תאפשר הלוואה

has_high_incom = False
has_good_credit = True
has_criminal_record=False

if has_high_incom and has_good_credit:
    print("ניתן לאפשר הלוואה כי יש את שני הפרטים נכונים  ")


if has_high_incom or has_good_credit:
        print("ניתן לאפשר הלוואה כי יש אחד מהתנאים ")


if  has_good_credit and not has_criminal_record:
        print("ניתן לאפשר הלוואה כי אין עבר פלילי ויש קרדיט ")
else:
    print("יש עבר פלילי או קרדיט נמוך")


name="elad"

if len(name)<3:
    print('it is too short')
elif len(name)>50:
    print('name too long')
else:
    print("name looks good")