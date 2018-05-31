from tkinter import *
from tkinter import ttk
from Pokedex import Pokedex


class Application:

    # Application constructor and boot
    def __init__(self, pokem):
        self.pokedexlist = pokem
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.resizable(0, 0)
        self.root.title("Pokedex")

        self.screen = ttk.Frame(self.root)
        try:
            self.image1 = PhotoImage(file="pokemonpictures/pokedex.png")
        except:
            self.image1 = PhotoImage(file="pokemonpictures/error.png")
        self.label = ttk.Label(self.screen, image=self.image1, anchor="center")
        self.label2 = ttk.Label(self.screen, text="Welcome to the National Pokedex, the pokedex where you are going to "
                                                  "find all the pokemons")
        self.label3 = ttk.Label(self.screen, text="and their stats, feel free to use it whenever you need it")
        self.label.pack(side=TOP, pady=10)
        self.label2.pack(side=TOP, padx=20)
        self.label3.pack(side=TOP)
        self.screen.grid(column=1, row=0, sticky=(N, S, E))

        self.listpokemon = ttk.Frame(self.root)
        self.scrollbar = Scrollbar(self.listpokemon)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.listpokemon, yscrollcommand=self.scrollbar.set)
        for i in range(1, Pokedex.MAX_POKEMON + 1):
            try:
                self.listbox.insert(END, self.pokedexlist.getpokemon(i).getnumber() + " " +
                                    self.pokedexlist.getpokemon(i).getname())
            except:
                pass

        self.listbox.bind("<<ListboxSelect>>", self.seepokemon)
        self.listbox.pack(side=LEFT, fill=BOTH)

        self.scrollbar.config(command=self.listbox.yview)

        self.listpokemon.grid(column=0, row=0, sticky=(N, S, W))

        self.root.rowconfigure(0, weight=1)

        mainloop()

    # when a pokemon is selected from the listbox it gets the data needed
    def seepokemon(self, event):

        w = event.widget
        list_item = w.curselection()

        if len(list_item) != 0:
            fp = w.get(list_item[0])
            fpp = fp.split(" ")
            code = int(fpp[0])

            pokemonvar = self.pokedexlist.getpokemon(code)

            infoframe = ttk.Frame(self.root)

            # name number image
            try:
                pokimage = PhotoImage(file=pokemonvar.getimg_path())
            except:
                pokimage = PhotoImage(file="pokemonpictures/error.png")
            image1 = ttk.Label(infoframe, image=pokimage, anchor="center")
            image1.image = pokimage
            textnumber = ttk.Label(infoframe, text="Number " + pokemonvar.getnumber())
            textname = ttk.Label(infoframe, text=pokemonvar.getname())
            textnumber.pack(side=TOP, padx=225, pady=5)
            textname.pack(side=TOP)
            image1.pack(side=TOP)

            # pokemon info
            textheight = ttk.Label(infoframe, text="Height: " + str(pokemonvar.getheight()) + " m")
            textweight = ttk.Label(infoframe, text="Weight: " + str(pokemonvar.getweight()) + " kg")
            textgender = ttk.Label(infoframe, text="Gender: " + str(pokemonvar.getgender()))
            textcategory = ttk.Label(infoframe, text="Category: " + str(pokemonvar.getcategory()))
            textabilities = ttk.Label(infoframe, text="Abilities: \n" + str(pokemonvar.getabilities()))
            textypes = ttk.Label(infoframe, text="Type: \n" + str(pokemonvar.tostringptype()))
            textweakness = ttk.Label(infoframe, text="Weakness: \n" + str(pokemonvar.tostringweakness()))
            texthp = ttk.Label(infoframe, text="Hp: " + str(pokemonvar.gethp()))
            textattack = ttk.Label(infoframe, text="Attack: " + str(pokemonvar.getattack()))
            textdefense = ttk.Label(infoframe, text="Defense: " + str(pokemonvar.getdefense()))
            textspecialattack = ttk.Label(infoframe,
                                          text="Special attack: " + str(pokemonvar.getspecial_attack()))
            textspecialdefense = ttk.Label(infoframe,
                                           text="Special Defense: " + str(pokemonvar.getspecial_defense()))
            textspeed = ttk.Label(infoframe, text="Speed: " + str(pokemonvar.getspeed()))

            # place info
            textheight.place(x=250, y=300)
            textweight.place(x=250, y=320)
            textgender.place(x=250, y=340)
            textcategory.place(x=380, y=300)
            textabilities.place(x=380, y=320)
            textypes.place(x=250, y=360)
            textweakness.place(x=250, y=400)
            # stats place info
            texthp.place(x=0, y=300)
            textattack.place(x=0, y=320)
            textdefense.place(x=0, y=340)
            textspecialattack.place(x=130, y=300)
            textspecialdefense.place(x=130, y=320)
            textspeed.place(x=130, y=340)

            infoframe.grid(column=1, row=0, sticky=(N, S, E))


# noinspection PyCallingNonCallable
poke = Pokedex()

j = Application(poke)
