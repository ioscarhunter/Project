class Pizza():
    def __init__(self):
        self.order = [0,0,0,0]
        self.extra = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.info = ['','','']


    def export(self):
        tmp = []
        tmp.extend(self.order)
        tmp.extend(self.extra)
        tmp.extend(self.info)
        stri = "O"
        for i in tmp:
            stri+="<>"+str(i).rstrip()
        