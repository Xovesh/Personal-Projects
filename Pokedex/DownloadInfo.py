import os
import sqlite3
from pokedex.Pokemon import Pokemon
from bs4 import BeautifulSoup
from urllib import request


class DownloadInfo:
    # Main variables
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/35.0.1916.47 Safari/537.36 '
    URLDB = "https://pokemondb.net/pokedex/national"
    URLIMAGES = "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/"
    DIRECTORY1 = "pokemonpictures/"
    DIRECTORY2 = "pokemoninfo/"
    FILE1 = "pokedex.db"
    MAX_POKEMON = None

    # Downloadinfo constructor
    def __init__(self, max_pokemon):
        DownloadInfo.MAX_POKEMON = max_pokemon
        DownloadInfo.boot()

    @staticmethod
    # To download and check all images
    def boot():
        DownloadInfo.check_directory()
        DownloadInfo.check_images()
        DownloadInfo.checklinkspath()
        DownloadInfo.checkpokemoninfo()

    @staticmethod
    # Checks if the folders exists
    def check_directory():

        # checking pokemonpictures folder
        if not os.path.exists(DownloadInfo.DIRECTORY1):
            print("Creating new directory " + DownloadInfo.DIRECTORY1)
            os.makedirs(DownloadInfo.DIRECTORY1)

        # checking pokemoninfo folder
        if not os.path.exists(DownloadInfo.DIRECTORY2):
            print("Creating new directory " + DownloadInfo.DIRECTORY2)
            os.makedirs(DownloadInfo.DIRECTORY2)

    @staticmethod
    # checks if all images are in the folder
    def check_images():
        # Pokemon pictures
        for l in range(DownloadInfo.MAX_POKEMON):
            path = DownloadInfo.DIRECTORY1 + Pokemon.convertnumber(l + 1) + ".png"
            url = DownloadInfo.URLIMAGES + Pokemon.convertnumber(l + 1) + ".png"
            if not os.path.isfile(path):
                try:
                    DownloadInfo.downloadimages(url, Pokemon.convertnumber(l + 1))
                    print(Pokemon.convertnumber(l + 1) + ".png downloaded " + Pokemon.convertnumber(
                        l + 1) + "/" + str(DownloadInfo.MAX_POKEMON))
                except:
                    print("We cant download the image at this moment, please try again later || number: %i" % (l+1))

        # specials image
        if not os.path.isfile(DownloadInfo.DIRECTORY1 + "pokedex.png"):
            DownloadInfo.downloadimages(
                "https://www.puclpodcast.com/wp-content/uploads/2017/01/900px-479Rotom-Pok%C3%A9dex-300x300.png",
                "pokedex")

        if not os.path.isfile(DownloadInfo.DIRECTORY1 + "error.png"):
            DownloadInfo.downloadimages("https://www.spreadshirt.es/image-server/v1/mp/designs/142931972,width=178,"
                                        "height=178/signo-de-interrogacion-icono-de-la-idea-regalo.png", "error")

    @staticmethod
    # download an image
    def downloadimages(url, file_name):
        full_path = DownloadInfo.DIRECTORY1 + file_name + ".png"
        request.urlretrieve(url, full_path)

    @staticmethod
    # download links path and check
    def checklinkspath():
        try:
            conn = sqlite3.connect(DownloadInfo.DIRECTORY2 + DownloadInfo.FILE1)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Pokedexlink (number INTEGER NOT NULL PRIMARY KEY, link text)''')
            c.execute("SELECT number FROM Pokedexlink")
            quantity = len(c.fetchall())
            if quantity < DownloadInfo.MAX_POKEMON:
                c.execute("DELETE FROM Pokedexlink")
                conn.commit()
                DownloadInfo.downloadlinkspath()
        except:
            print("Error with the database")

    @staticmethod
    # download links path
    def downloadlinkspath():
        try:
            # connection
            headers = {'User-Agent': DownloadInfo.USER_AGENT}
            data = request.Request(DownloadInfo.URLDB, None, headers)  # The assembled request
            response = request.urlopen(data)
            html = response.read()  # The data u need

            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("div", attrs={'class': 'infocard-tall-list'})

            e = 1
            linkin = True
            for link in table.find_all("a"):
                a = link.get("href")
                if "/pokedex/" in a:
                    if linkin:
                        conn = sqlite3.connect(DownloadInfo.DIRECTORY2 + DownloadInfo.FILE1)
                        c = conn.cursor()
                        print(a)
                        pokemoninfo = [e, a]
                        pokemoninfo = tuple(pokemoninfo)
                        c.execute('''INSERT INTO Pokedexlink(number,link) VALUES (?,?)''', pokemoninfo)
                        e += 1
                        conn.commit()
                        conn.close()
                        linkin = False
                    else:
                        linkin = True
        except:
            print("Error downloading linkspaths")

    @staticmethod
    # checks if the pokemon info exists
    def checkpokemoninfo():
        try:
            conn = sqlite3.connect(DownloadInfo.DIRECTORY2 + DownloadInfo.FILE1)
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Pokedex(number INTEGER NOT NULL PRIMARY KEY, name text, height REAL, 
                      weigth REAL, gender INTEGER, category text, abilities text, ptype text, weakness text, hp INTEGER, 
                              attack INTEGER, defense INTEGER, special_attack INTEGER, special_defense INTEGER, 
                              speed INTEGER, firstevolution text)''')

            for p in range(1, DownloadInfo.MAX_POKEMON + 1):
                c.execute("SELECT * FROM Pokedex where number=(?)", (p,))
                registros = c.fetchone()
                if registros is None:
                    DownloadInfo.downloadpokemoninfo(p)

            conn.close()
        except:
            print("Error with the database")

    @staticmethod
    # downloads the pokemon data where s is the number of the pokemon
    def downloadpokemoninfo(s):
        conn = sqlite3.connect(DownloadInfo.DIRECTORY2 + DownloadInfo.FILE1)

        c = conn.cursor()

        url1 = "https://www.pokemon.com/uk"
        url2 = "https://pokemondb.net"
        headers = {'User-Agent': DownloadInfo.USER_AGENT}

        pokemonurldifferent = {"/pokedex/nidoran-f": "/pokedex/nidoran-female",
                               "/pokedex/nidoran-m": "/pokedex/nidoran-male"}
        try:

            c.execute("SELECT link FROM Pokedexlink WHERE number=(?)", (s,))
            registros = c.fetchone()

            line = registros[0]

            # connection
            sub_path = line
            if sub_path in pokemonurldifferent.keys():
                sub_path = pokemonurldifferent[sub_path]
            full_path = url1 + sub_path
            data = request.Request(full_path, None, headers)
            response = request.urlopen(data)
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("div", attrs={'class': 'info match-height-tablet'})
            # info/number/name
            pokemoninfo = [s, sub_path.split("/")[2].title()]

            # height,weight,gender

            values = table.find("div", attrs={'class': 'column-7'})
            span = values.find_all("span", attrs={'class': 'attribute-value'})
            pokemoninfo.append(float(span[0].get_text().replace(" m", "")))
            pokemoninfo.append(float(span[1].get_text().replace(" kg", "")))
            j = span[2].find_all("i")
            if len(j) == 0:
                pokemoninfo.append("None")
            elif len(j) == 1:
                mf = j[0].get("class")
                if "male" in mf[1]:
                    pokemoninfo.append("Male")
                else:
                    pokemoninfo.append("Female")
            else:
                pokemoninfo.append("Both")

            # category,abilities
            values = table.find("div", attrs={'class': 'column-7 push-7'})
            span = values.find_all("span", attrs={'class': 'attribute-value'})
            pokemoninfo.append(span[0].get_text().replace(" ", "_"))
            string = ""
            for k in range(1, len(span)):
                string = string + span[k].get_text().replace(" ", "_") + "/"
            pokemoninfo.append(string[:-1])

            # ptype
            values = table.find("div", attrs={'class': 'dtm-type'})
            li = values.find_all("li")
            string = ""
            for k in range(len(li)):
                lia = li[k].find("a")
                string = string + lia.text.replace(" ", "_") + "/"
            pokemoninfo.append(string[:-1])

            # weakness
            values = table.find("div", attrs={'class': 'dtm-weaknesses'})
            li = values.find_all("li")
            string = ""
            for k in range(len(li)):
                lia = li[k].find("span")
                lia = lia.text.replace("\n", "")
                lia = lia.replace("\t", "")
                string = string + lia.replace(" ", "") + "/"
            pokemoninfo.append(string[:-1])
            # stats
            # connection
            sub_path2 = line
            full_path2 = url2 + sub_path2
            data2 = request.Request(full_path2, None, headers)
            response2 = request.urlopen(data2)
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, "html.parser")
            # statsdata
            table2 = soup2.find("div", attrs={'class': 'col desk-span-8 lap-span-12'})
            values2 = table2.find("tbody")
            stats = values2.find_all("td", attrs={'class': 'num'})
            for k in range(0, len(stats), 3):
                pokemoninfo.append(int(stats[k].get_text()))

            pokemoninfo.append("False")
            s += 1

            pokemoninfo = tuple(pokemoninfo)
            c.execute('''INSERT INTO Pokedex(number,name, height, weigth, gender, category, abilities, ptype, 
                                      weakness,hp, attack, defense, special_attack, special_defense, speed, 
                                      firstevolution) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', pokemoninfo)

            conn.commit()

            print("Downloading data from " + full_path)
            print(pokemoninfo)
        except:
            print("Error, we cant connect with the database Pokemon ID: %i" % s)
        conn.close()
