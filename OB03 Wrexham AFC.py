team = []

class WrexhamPlayer():
    def __init__(self, playernumber: str, forename: str, surname: str, position: str):
        self.__playernumber = playernumber #string
        self.__forename = forename #string
        self.__surname = surname #string
        self.__position = position #string
        self.__communityinvolvement = 0 #real
        self.__injured = False #boolean

    def get_player_info(self):
        print("Player name:",self.__forename,self.__surname)
        print("Player position:",self.__position)

    def change_community_involvement(self, change: float):
        self.__communityinvolvement += change

    def change_injured(self):
        if self.__injured == False:
            self.__injured = True

        if self.__injured == True:
            self.__injured = False

    def __repr__(self):
        return self.__playernumber, self.__forename, self.__surname, self.__position, self.__communityinvolvement, self.__injured

file = open('wrexham.txt','r')
content = file.readlines()
file.close()

for i in range(28):
    team.append(WrexhamPlayer(content[i*4].strip(),content[i*4+1].strip(),content[i*4+2].strip(),content[i*4+3].strip()))

print(team[2].get_player_info())
