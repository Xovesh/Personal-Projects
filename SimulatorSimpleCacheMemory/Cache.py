class Cache:
    def __init__(self, wordsize, blocksize, setsize, replacepolicy):
        self.wordsize = wordsize
        self.blocksize = blocksize
        self.setsize = setsize
        self.replacepolicy = replacepolicy
        self.setq = int(8/setsize)
        self.cm = self.createcm()

        # hit/access
        self.totalaccess = 0
        self.hit = 0
        # cycles
        self.tcm = 2
        self.tmm = 21
        self.tbuff = 1
        self.tbt = self.tmm + self.blocksize/self.wordsize-1 * self.tbuff
        self.totaltime = 0

    def createcm(self):
        cm = []
        for i in range(self.setq):
            cm.append([])
            for j in range(self.setsize):
                cm[i].append(Line())
        return cm

    def interprateaddres(self, address):
        word = int(address / self.wordsize)
        block = int(word / (self.blocksize / self.wordsize))
        sets = int(block % self.setq)
        tag = int(block/self.setq)
        print("\nAddress: {} - Word: {} - Block: {} (Words {} - {})".format(address, word, block, block*8, block*8+7))
        print("Set: {} - Tag: {}\n".format(sets, tag))
        return tag, sets, block

    def checkcm(self, address, operation):
        tag, sets, block = self.interprateaddres(address)
        self.totalaccess += 1
        find = False
        for i in self.cm[sets]:
            if i.tag == tag and i.busy != 0:
                print("Cache Hit")
                self.hit += 1
                find = True
        if not find:
            print("Cache Miss")

        if operation == 1:
            repl = self.write(find, tag, sets, block)
        else:
            repl = self.load(find, tag, sets, block)
        self.accesstime(find, repl)

    def accesstime(self, find, repl):
        time = 0
        if find:
            time += self.tcm
            print("Access time: Cache Access {} Cycles".format(self.tcm))
        elif not find and repl:
            time += self.tcm + self.tbt + self.tbt
            print("Access time: Cache Access {} Cycles,  -- block transf. (MM>CM or CM>MM), {} cycles --repl. {} cycles".format(self.tcm, self.tbt, self.tbt))
        elif not find:
            time += self.tcm + self.tbt
            print("Access time: Cache Access {} Cycles,  -- block transf. (MM>CM or CM>MM), {} cycles".format(self.tcm, self.tbt))
        print("T_Access: {} Cycles".format(time))
        self.totaltime += time

    def write(self, hit, tag, sets, block):
        repl = False
        if not hit:
            repl = self.load(hit, tag, sets, block)

        if self.replacepolicy == 1:
            pos = 0
            obj = None
            for i in self.cm[sets]:
                if i.tag == tag:
                    pos = i.counter
                    i.dirty = 1
                    i.counter = 0
                    obj = i
                    break
            for i in self.cm[sets]:
                if i.busy == 1 and i.counter < pos and i != obj:
                    i.counter += 1
        else:
            for i in self.cm[sets]:
                if i.tag == tag and i.busy == 1:
                    i.dirty = 1
                    break
        return repl

    def load(self, hit, tag, sets, block):
        repl = False
        if not hit:
            load = False
            for i in self.cm[sets]:
                if i.busy == 0:
                    i.tag = tag
                    i.data = "B" + str(block)
                    i.busy = 1
                    i.dirty = 0
                    i.counter = 0
                    load = True
                    break
                else:
                    if i.busy == 1:
                        i.counter += 1

            if not load:
                oldest = 0
                replace = self.cm[sets][0]
                for i in self.cm[sets]:
                    if i.counter > oldest:
                        oldest = i.counter
                        replace = i
                replace.tag = tag
                replace.data = "B" + str(block)
                if replace.dirty == 1:
                    repl = True
                replace.dirty = 0
                replace.counter = 0
        else:
            if self.replacepolicy == 1:
                pos = 0
                obj = None
                for i in self.cm[sets]:
                    if i.tag == tag:
                        pos = i.counter
                        i.counter = 0
                        obj = i
                        break

                for i in self.cm[sets]:
                    if i.busy == 1 and i.counter < pos and i != obj:
                        i.counter += 1
        return repl

    def visualizecm(self):
        header = "Busy Dirty Tag Repl. || data"
        print(header)
        print("-" * len(header))
        for i in self.cm:
            for j in i:
                print(" ", j.busy, 2*" ", j.dirty, 2*" ", j.tag, 2*" ", j.counter, "  ||", j.data)
            print("-" * len(header))
        print("Note: in repl. the biggest number is the oldest/least used")

    def finalhitrate(self):
        print("Ref: {} -- Hits: {} -- Hit rate, h = {}".format(self.totalaccess, self.hit, self.hit/self.totalaccess))
        print("Total access time = {} cycles".format(self.totaltime))

class Line:
    def __init__(self):
        self.busy = 0
        self.dirty = 0
        self.tag = 0
        self.counter = 0
        self.data = "----"
