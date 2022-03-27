class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f" hi, I'm {self.name}")

#שים לב לאתחל את האובייקט ברגע שהוספת קונסטרקטור
jon=Person("jon smith ")
jon.talk()

bob=Person("bob habanai")
bob.talk()