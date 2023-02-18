
from random import randint
import time

Weights = [128,64,32,16,8,4,2,1]

PositiveAttributes = ["Sharp Teeth","Claws","Strong Legs","Thumbs","Good Vision",
                      "Good Hearing", "Tough Skin", "Aquatic Ability"]

class Agent:
    def __init__(self,SetAtts,AttStr):
        self.Atts = self.GetAtts(SetAtts,AttStr)
        self.Strength = self.GetStrength()

    def GetStrength(self):
        Total = 0
        for i in range(len(self.Atts)):
            if self.Atts[i] == "1":
                Total = Total + Weights[i]
        return Total
    
    def GetAtts(self,SetAtts,AttStr):
        self.NoOfAtts = 0
        if not SetAtts:
            AttStr = ""
            
            for i in range(8):
                Num = randint(0,1)
                AttStr = AttStr + str(Num)
                
        for i in range(len(AttStr)):
            if AttStr[i] == "1":
                self.NoOfAtts += 1
        return AttStr

    def PrintAtts(self):
        MyAtts = []
        for i in range(8):
            if self.Atts[i] == "1":
                MyAtts.insert(-1,PositiveAttributes[i])

        return MyAtts

class EvolutionSim:
    def __init__(self):
        self.Agents = self.MakeAgents()
        self.StrongestOriginalAgent = self.GetStrongestAgent()
        self.GenerationStrength = self.GetGenStrength()
        self.OriginalGenStrength = self.GenerationStrength

    def GetGenStrength(self):
        Total = 0
        
        for i in range(len(self.Agents)):
            Total += self.Agents[i].Strength
        return Total/15

    def GetSuccessRate(self):
        print("At the start, the population had an average strength of",self.OriginalGenStrength)
        print("Currently, the population has an average strength of",self.GetGenStrength())
        print()
        print("At the start, the strongest animal had a strength of",self.StrongestOriginalAgent.Strength,", including",self.StrongestOriginalAgent.PrintAtts())
        print()
        print("currently, the strongest animal has a strength of",self.GetStrongestAgent().Strength,", including",self.GetStrongestAgent().PrintAtts())

    def GetStrongestAgent(self):
        Current = self.Agents[0]
        for i in range(len(self.Agents)):
            if self.Agents[i].Strength > Current.Strength:
                Current = self.Agents[i]
        return Current

    def MakeAgents(self):
        Agents = []
        for i in range(15):#creates 6 random agents
            NewAgent = Agent(False,"")
            Agents.insert(-1,NewAgent)
        return Agents

    def KillWeak(self):
        Pointer1 = ""
        Pointer2 = ""

        for i in range(15): #this finds the two strongest
            try:
                if self.Agents[i].Strength > self.Agents[Pointer1].Strength:
                    Pointer2 = Pointer1
                    Pointer1 = i

            except:
                Pointer1 = i
                Pointer2 = i

        A1,A2 = self.Breed(Pointer1,Pointer2)#this breeds them

        Pointer1 = ""
        Pointer2 = ""

        for i in range(15): #this finds the two weakest to replace
            try:
                if self.Agents[i].Strength < self.Agents[Pointer1].Strength:
                    Pointer2 = Pointer1
                    Pointer1 = i
                    
            except:
                Pointer1 = i
                Pointer2 = i
                
        self.Agents[Pointer1] = A1
        self.Agents[Pointer2] = A2#this replaces the two weakest with the new children
            
    def Breed(self,Pointer1,Pointer2):
        #swap bits
        BitSelect = randint(1,7)
        Agent1 = self.Agents[Pointer1]
        Agent2 = self.Agents[Pointer2]
        BitChunks = []
        
        BitChunks.insert(-1,Agent1.Atts[0:BitSelect])#splits apart the bits
        BitChunks.insert(-1,Agent1.Atts[BitSelect:9])
        BitChunks.insert(-1,Agent2.Atts[0:BitSelect])
        BitChunks.insert(-1,Agent2.Atts[BitSelect:9])

        NewBitStr1 = BitChunks[0]+BitChunks[3]
        NewBitStr2 = BitChunks[2]+BitChunks[1]#repairs new bit strings

        BredAgent1 = Agent(True,NewBitStr1)
        BredAgent2 = Agent(True,NewBitStr2)

        return(BredAgent1,BredAgent2)

        
def Main():
    Evolution = EvolutionSim()
    print("How many Generations would you like to simulate?")
    x = int(input(">"))
    for i in range(x):
        Evolution.KillWeak()
        #print("Generation",i,"complete")
        #time.sleep(0.5)
    print("All generations complete")
    pause = input("enter to reveal results")
    Evolution.GetSuccessRate()

Main()
