class Balloon:
    def __init__(self,Colour,DefenceItem):
        #Colour STRING
        #DefenceItem STRING
        #Health INTEGER
        
        self.__Colour=Colour
        self.__DefenceItem=DefenceItem
        self.__Health=100
        
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self,ThisNum):
        self.__Health=self.__Health+ThisNum
        
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False


def main():
    Colour=input('Enter colour:')
    DefenceItem=input('Enter defence method:')
    Balloon1=Balloon(Colour,DefenceItem)
    Balloon1=Defend(Balloon1)   #return amended object
    
    
def Defend(BalloonObj):
    Strength=int(input('Enter opponent strength:'))
    BalloonObj.ChangeHealth(-Strength)
    print('Defence item is',BalloonObj.GetDefenceItem())
    result=BalloonObj.CheckHealth()
    if result==False:
        print('Defence Success')
    else:
        print('Defence Failed')
    return BalloonObj
    
main()