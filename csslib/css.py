
def ch(li, num):
    try:
        return li[num]
    except:
        return ""
class CSS3():
    def __init__(self, text):
        #f = open("test1.css", "r").read()
        self.f = text
    def parse(self):
        self.csstree = {}
        self.vars = {}
        self.comments = []
        word = ""
        cssname = ""
        cssproperty = ""
        varn = ""
        nomen = False
        define = False
        comment = False
        dun = False
        i = 0
        for c in self.f:
            next = ch(self.f, i + 1)
            if c != "\n" and c != "":# and c != " ":
                if c == "{":
                    nomen = True
                    self.csstree[word] = {}
                    cssname = word
                    word = ""
                elif c == "}":
                    cssname = ""
                elif c == "/" and next == "*":
                    comment = True
                    dun = True
                elif c == "*" and next == "/":
                    comment = False
                    self.comments.append(word)
                    dun = True
                    word = ""
                elif c == ":":# and nomen == True:
                    if define == False and nomen == True:
                        #print cssname
                        if cssname != "":
                            self.csstree[cssname][word.replace(" ", "")] = ""
                            cssproperty = word.replace(" ", "")
                            word = ""
                    elif define == True and nomen == False:
                        try:
                            varn = "$" + word
                            word = ""
                            nomen = False
                        except:
                            word = word + c
                    else:
                        word = word + c
                elif c == ";":
                    if define == False:
                        #print word
                        if word[0] == " ":
                            w = list(word)
                            w[0] = ""
                            word = "".join(w)
                        if word[0] == "$":
                            out = self.vars[word]
                            #print "true"
                        else:
                            out = word
                            
                        self.csstree[cssname][cssproperty] = out
                        word = ""
                    else:
                        if word[0] == " ":
                            w = list(word)
                            w[0] = ""
                            word = "".join(w)
                        self.vars[varn] = word
                        varn = ""
                        word = ""
                        define = False
                elif c == "$" and cssname == "":
                    define = True
                    nomen = False
                else:
                    if dun == True:
                        dun = False
                    else:
                        word = word + c
                #print c
            i = i + 1
        #print self.csstree
        #print self.vars
        #print self.comments
    def getItem(self, itemname):
        return self.csstree[itemname]
    def get(self, name):
        if name == '__tree__':
            return self.csstree
        elif name == '__vars__':
            return self.vars
        elif name == '__comments__':
            return self.comments
        else:
            print """
Use '__tree__' to get the css tree
Use '__vars__' to get the vars
Use '__comments__' to get the comments
            """
            return ""
    def getIds(self):
        all_ids = {}
        for a in self.csstree:
            if a[0] == "#":
                all_ids[a] = self.csstree[a]
        return all_ids
    def getClasses(self):
        all_ids = {}
        for a in self.csstree:
            if a[0] == ".":
                all_ids[a] = self.csstree[a]
        return all_ids
    def getAllStartWith(self, sw):
        all_ids = {}
        for a in self.csstree:
            if a[0] == sw:
                all_ids[a] = self.csstree[a]
        return all_ids
