# import timeOperation as t

class Vehicle:

    def __init__(self, speed, routeNum):

        self.speed = speed
        self.rNum = routeNum

        try:
            routeFile = open("routeFile.txt", "r")
        except:
            print("There is no file with that name")

        try:
            for lines in routeFile:
                tempString = ""
                i = 0
                while lines[i] != ",":
                    tempString += lines[i]
                    i += 1
                if int(tempString) == self.rNum and len(tempString) == 2:
                    route = lines[2:]
                    routeTime = route.replace(",", "")
                    self.rTime = int(routeTime)
                    break
                elif int(tempString) == self.rNum and len(tempString) == 1:
                    route = lines[1:]
                    routeTime = route.replace(",", "")
                    self.rTime = int(routeTime)
                    break
                else:
                    continue

        except:
            print("That route does not exist")

    def getSpeed(self):
        return self.speed

    def setSpeed(self, s):
        self.speed = s

    def getRouteNum(self):
        return self.rNum

    def getRouteTime(self):
        return self.rTime
