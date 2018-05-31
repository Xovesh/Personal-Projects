class Pokemon:

    # Pokemon constructor

    def __init__(self, number, name, height, weigth, gender, category, abilities, ptype, weakness, stats,
                 firstevolution):
        self.__number = Pokemon.convertnumber(number)
        self.__img_path = "pokemonpictures/" + self.__number + ".png"
        self.__name = name
        self.__height = height
        self.__weight = weigth
        self.__gender = gender
        self.__abilities = abilities
        self.__category = category
        # array
        self.__weakness = weakness
        # array
        self.__ptype = ptype
        # array
        '''
        [0] -> hp
        [1] -> attack
        [2] -> defense
        [3] -> special_attack
        [4] -> special_defense
        [5] -> speed
        '''
        self.__stats = stats
        self.__firstevolution = firstevolution

    # returns a dictionary with the stats
    def statsdictionary(self):
        stats = {"hp": self.gethp(), "attack": self.getattack(), "defense": self.getdefense(),
                 "special_attack": self.getspecial_attack(), "special_defense": self.getspecial_defense(),
                 "speed": self.getspeed()}
        return stats

    # returns the stats in a string
    def tostringstats(self):
        return "\n".join(
            ["Hp: " + str(self.gethp()), "Attack: " + str(self.getattack()), "Defense: " + str(self.getdefense()),
             "Special_attack: " + str(self.getspecial_attack()),
             "Special_defense: " + str(self.getspecial_defense()),
             "Speed: " + str(self.getspeed())])

    # returns the weakness array in a string
    def tostringweakness(self):
        quantity = len(self.__weakness)
        info = ""
        for i in range(quantity):
            info = info + self.__weakness[i] + "/"
        return info[:-1]

    # returns the ptype array in a string
    def tostringptype(self):
        quantity = len(self.__ptype)
        info = ""
        for i in range(quantity):
            info = info + self.__ptype[i] + "/"
        return info[:-1]

    # returns the number integer value in a string
    @staticmethod
    def convertnumber(number):
        if number < 10:
            return "00" + str(number)
        elif number < 100:
            return "0" + str(number)
        else:
            return str(number)

    # Prints the basic info of the pokemon
    def basicinfo(self):
        print("\nNumber: " + self.__number)
        print("\nName: " + self.__name)
        print("\nGender: " + self.__gender)
        print("\nHeight: " + str(self.__height))
        print("\nWeight: " + str(self.__weight))
        print("\nCategory: " + self.__category)
        print("\nAbilities: " + self.__abilities)
        print("\nStats:")
        print(self.tostringstats())
        print("\nType:")
        print(self.tostringptype())
        print("\nWeakness:")
        print(self.tostringweakness())
        print("-------------------------------------")

    # Getters for all the values
    def getnumber(self):
        return self.__number

    def getimg_path(self):
        return self.__img_path

    def getname(self):
        return self.__name

    def getgender(self):
        return self.__gender

    def getheight(self):
        return self.__height

    def getweight(self):
        return self.__weight

    def getcategory(self):
        return self.__category

    def getabilities(self):
        return self.__abilities

    def getweakness(self):
        return self.__weakness

    def getptype(self):
        return self.__ptype

    def getfirstevolution(self):
        return self.__firstevolution

    # stats getters
    def gethp(self):
        return self.__stats[0]

    def getattack(self):
        return self.__stats[1]

    def getdefense(self):
        return self.__stats[2]

    def getspecial_attack(self):
        return self.__stats[3]

    def getspecial_defense(self):
        return self.__stats[4]

    def getspeed(self):
        return self.__stats[5]
