###Bedirhan Yalcin###

import random

class game():
    def __init__(self):
        self.start()

    def veriler(self):
        self.score = 0
        self.pcscore = 0
    def start(self):
        self.score = 0
        self.pcscore = 0
        while True:
            pc = random.randint(1,3)
            user = int(input("Rock 1 - Paper 2 - Scissors 3 : "))
            if user !=1 and user != 2 and user !=3:
                print("you can write only 1 , 2 or 3")
            else:
                if pc == 1:
                    
                    print("computer --> Rock ")
                elif pc ==2:
                    print("computer --> Paper")

                elif pc == 3:
                    print("computer --> Scissors")
                if user == 1 and pc == 1 or user ==2 and pc ==2 or pc ==3 and user ==3:
                    self.draw()
                elif user ==1 and pc == 3 or user ==2 and pc ==1 or user ==3 and pc == 2:
                    self.userwon()
                else:
                    self.pcwon()

    def draw(self):
        print("Draw")
        print("User score : ", self.score, " computer Score : ", self.pcscore)

    def userwon(self):
        self.score +=1
        print("User Won")
        print("User score : ",self.score ," computer Score : ",self.pcscore)

    def pcwon(self):
        self.pcscore += 1
        print("Pc Won")
        print("User score : ", self.score, " computer Score : ", self.pcscore)

game = game()
