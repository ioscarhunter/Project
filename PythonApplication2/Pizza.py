class Pizza():
    def __init__(self):
        self.order = [0,0,0,1]
        self.extra = [0,0,0,0,0,0,0,0,0,0,0,0]



    def export(self,prize):
        tmp = []
        tmp.extend(self.order)
        tmp.append(prize)
        tmp.extend(self.extra)
        stri = "O"
        for i in tmp:
            stri+="<>"+str(i).rstrip()
        return stri
        