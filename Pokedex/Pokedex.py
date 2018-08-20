from pokedex.Pokemon import Pokemon
import sqlite3
from pokedex.DownloadInfo import DownloadInfo


class Pokedex:
    MAX_POKEMON = 806

    # pokedex constructor
    def __init__(self):
        self.listpokedex = []
        self.boot()

    # Add a pokemon to the pokedex
    def addpokemon(self, pokemon):
        self.listpokedex.append(pokemon)

    # print the pokedex
    def printpokedex(self):
        for i in range(self.pokequantity()):
            self.listpokedex[i].basicinfo()
            print("")

    # get the pokemon with the number i
    def getpokemon(self, index):
        for i in range(len(self.listpokedex)):
            if index == int(self.listpokedex[i].getnumber()):
                return self.listpokedex[i]

    # quantity of pokemons in the pokedex
    def pokequantity(self):
        return len(self.listpokedex)

    # to boot the pokedex data
    def boot(self):
        DownloadInfo(Pokedex.MAX_POKEMON)
        self.readpokemondb()

    # reads the pokemon database and include all of them in the pokedex
    def readpokemondb(self):
        try:
            conn = sqlite3.connect("pokemoninfo/pokedex.db")

            c = conn.cursor()

            c.execute("SELECT * FROM Pokedex")
            registros = c.fetchall()
            for arrayinfo in registros:
                try:
                    newpokemon = Pokemon(arrayinfo[0], arrayinfo[1], arrayinfo[2], arrayinfo[3],
                                         arrayinfo[4], arrayinfo[5], arrayinfo[6], arrayinfo[7].split("/"),
                                         arrayinfo[8].split("/"), [arrayinfo[9], arrayinfo[10],
                                                                   arrayinfo[11], arrayinfo[12], arrayinfo[13],
                                                                   arrayinfo[14]], arrayinfo[15])
                    self.addpokemon(newpokemon)
                except:
                    pass

            c.close()
        except:
            print("We cant connect with the database")
        finally:
            print("Data and pictures from: https://www.pokemon.com/uk/pokedex")
            print("Data from: https://pokemondb.net/pokedex/all\n")
            print("Pokemons in the pokedex: " + str(self.pokequantity()))
            print("Impossible to add: " + str(Pokedex.MAX_POKEMON - self.pokequantity()))
            if Pokedex.MAX_POKEMON - self.pokequantity() != 0:
                print("Please close the program and open again, we are going to download the remaining ones")
