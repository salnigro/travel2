
class Npc(object):
    def __init__(self,quest):
        self.quest = quest

    def speech(self):
        if(self.quest.cpm == 0):
            t = input("I need your help adventurer (y/n)")
            if(t == "y"):
                print("Thanks you adventure i need you to do " + self.quest.task)
                self.quest.cpm = 1
        if(self.quest.cpm == 1):
            s = input("did you do it (y/n)")
            if (s == "y"):
                print("Thanks")
                self.quest.cpm = 2
            else:
                print("please hurry")

        if(self.quest.cpm == 2):
            print("thanks again")
           
