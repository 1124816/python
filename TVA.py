class power:

    def __init__(self):
        self.power = 0
        self.costAll = 0
        self.cost = 0
        self.time = 0
        self.dams = [0] * 40
        self.nuclear = [0] * 5
        self.lCoal = [0] * 3
        self.sCoal = [0] * 15
        self.cc = [0] * 10
        self.ct = [0] * 40
        for i in range(len(self.dams)):
            self.dams[i] = dam()
        for i in range(len(self.nuclear)):
            self.nuclear[i] = nuclear()
        for i in range(len(self.lCoal)):
            self.lCoal[i] = lCoal()
        for i in range(len(self.sCoal)):
            self.sCoal[i] = sCoal()
        for i in range(len(self.cc)):
            self.cc[i] = cc()
        for i in range(len(self.ct)):
            self.ct[i] = ct()
    def changePower(self, by):
        self.power += by

    def changeCost(self, by):
        self.cost += by

    def changeTime(self, by):
        self.time += by

    def update(self):
        for i in range(len(self.dams)):
            self.dams[i].update()
        for i in range(len(self.nuclear)):
            self.nuclear[i].update()
        for i in range(len(self.lCoal)):
            self.lCoal[i].update()
        for i in range(len(self.sCoal)):
            self.sCoal[i].update()
        for i in range(len(self.cc)):
            self.cc[i].update()
        for i in range(len(self.ct)):
            self.ct[i].update()
        if(self.time % 12 == 0):
            self.costAll +=self.cost




class dam:
    powerC = 50
    cost = 5
    online = 1
    start = 0

    def __init__(self):
        self.online = dam.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-dam.powerC*self.percent)
        all.changeTime(-dam.powerC*self.percent*dam.cost)
        self.online = dam.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(dam.powerC*self.percent)
                all.changeTime(dam.powerC*self.percent*dam.cost)
                self.online = 0
                self.change = False


class nuclear:
    powerC = 1000
    cost = 10
    online = 864
    start = 0

    def __init__(self):
        self.online = nuclear.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-nuclear.powerC*self.percent)
        all.changeTime(-nuclear.powerC*self.percent*nuclear.cost)
        self.online = nuclear.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(nuclear.powerC*self.percent)
                all.changeTime(nuclear.powerC*self.percent*nuclear.cost)
                self.online = 0
                self.change = False



class lCoal:
    powerC = 1000
    cost = 15
    online = 96
    start = 500000

    def __init__(self):
        self.online = lCoal.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-lCoal.powerC*self.percent)
        all.changeTime(-lCoal.powerC*self.percent*lCoal.cost)
        self.online = lCoal.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(lCoal.powerC*self.percent)
                all.changeTime(lCoal.powerC*self.percent*lCoal.cost)
                self.online = 0
                self.change = False



class sCoal:
    powerC = 200
    cost = 25
    online = 48
    start = 75000

    def __init__(self):
        self.online = sCoal.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-sCoal.powerC*self.percent)
        all.changeTime(-sCoal.powerC*self.percent*sCoal.cost)
        self.online = sCoal.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(sCoal.powerC*self.percent)
                all.changeTime(sCoal.powerC*self.percent*sCoal.cost)
                self.online = 0
                self.change = False

class cc:
    powerC = 250
    cost = 20
    online = 12
    start = 1000

    def __init__(self):
        self.online = cc.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-cc.powerC*self.percent)
        all.changeTime(-cc.powerC*self.percent*cc.cost)
        self.online = cc.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(cc.powerC*self.percent)
                all.changeTime(cc.powerC*self.percent*cc.cost)
                self.online = 0
                self.change = False

class ct:
    powerC = 75
    cost = 40
    online = 5
    start = 200

    def __init__(self):
        self.online = ct.online
        self.change = False
        self.percent = 1.00

    def turnOn(self, percent = -1):
        if(percent != -1):
            self.percent = percent
            all.costAll += self.start
        self.change = True

    def turnOff(self):
        global power
        global cost
        all.changePower(-ct.powerC*self.percent)
        all.changeTime(-ct.powerC*self.percent*ct.cost)
        self.online = ct.online
        self.change = False

    def setPercent(self, percent = -1):
        if(percent != -1):
            self.percent = percent

    def update(self):
        if(self.change == True and self.online >= 1):
            self.online = self.online - 1
            if(self.online == 0):
                all.changePower(ct.powerC*self.percent)
                all.changeTime(ct.powerC*self.percent*ct.cost)
                self.online = 0
                self.change = False



all = power()
print all.power

power = int(raw_input("Things that are cool"))
for a in all.dams:
    a.turnOn()
for a in all.nuclear:
    a.turnOn()

a = 0

while(a<900):
    all.update()
    a+=1

all.update()
print all.power
