from SimulatorSimpleCacheMemory import Cache

words = int(input("Word size (bytes): 4 - 8: > "))
lines = int(input("Block/Line size (bytes): 32 - 64: > "))
sets = int(input("Set size (lines): 1-2-4-8: > "))
repl = int(input("Replacement pol.: 0(FIFO) - 1(LRU): > "))

a = Cache.Cache(words, lines, sets, repl)
x = int(input("Mem. address (byte) (-1 to finish): > "))
while x != -1:
    y = int(input("Load (0) / Store (1): > "))
    a.checkcm(x, y)
    a.visualizecm()
    x = int(input("Mem. address (byte) (-1 to finish): > "))
a.finalhitrate()
