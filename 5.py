#מתייחס לזה כמערך
course='Python is greate'
print(course[0])
#מכיוןן שהתא הראשון בסטרינג הוא P ידפיס אותו וכן הלאה

#פקודה זו תחזיר את האות e מכיוון שעכשיו הוא סופר אחורה כביכול
print(course[-1])
#יציג t וכן הלאה
print(course[-2])

# טווח של מערך עמ להדפיס מילה מסויימת נוכל לעשות כך
print(course[0:3])
# ידפיס לי את הצירוף Pyt מכיוון שמתחיל מ0 ועובר הלאה עד תא 3 לא כולל

# ידפיס הכל
print(course[0:])

# ידפיס פרט לאות הראשונה P
print(course[1:])
# גם ידפיס הכל
print(course[:])


another=course[:]
print(another)

name='Jennifer'
#ידפיס לי מתא מס 1 עד תא מס -1 כלומר ידפיס ennife
print(name[1:-1])