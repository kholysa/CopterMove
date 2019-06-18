import time
class Localisation:

    @staticmethod
    def GetPosition():
        # Will read the text file and provide the most up to date localisation information
        location = open('C:\\Users\\blab\\Desktop\\test.txt')
        lastLine = location.readlines()[-1]
        lastLine = lastLine.replace('[','')
        x = float(lastLine.split(']')[0])
        y = float(lastLine.split(']')[1])
        location.close()
        return x, y
