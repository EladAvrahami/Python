secret_num=9
counter=0
gussLimit=3
#while counter<gussLimit:
 #   guess=int( input('guess:'))
  #  counter+=1
   # if guess==secret_num:
    #    print("you won !")
     #   print("this method has problem becouse it keep leting me guss after i won ...")

while counter<gussLimit:
    guess=int( input('guess:'))
    counter+=1
    if guess==secret_num:
        print("you won !")
        break
else:
    print("U fail gussing")

