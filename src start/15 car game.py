
command=""
started =False
#אופציה ראשונה חוזרת על עצמה ההעבקה של האינפוט לאותיות קטנות
#while command.lower() !="quit":
 #  command= input(">")
  # if command.lower() == "start":
   #    print("car started ...")
   #elif command.lower() == "stop":
    #   print("car stopped")


#שיטה קצרה יותר

#ניתן לוותר על הביטוי הזה ולכתןב :
# while while command !="quit":
while True:
   command= input(">").lower()
   if command == "start":
       if started:
           print("Car already started")
       else:
           started= True
           print("car started ...")

   elif command == "stop":
       if not started:
           print("car already stopped")
       else:
           started=False
           print("car stopped")

   elif command =='help':
       print("""
start- to stsrt the car
stop - to stop the car.
quit - to quit
       """)
   elif command =="quit":
       break
   else:print("sorry i dont understand that ")