"""
This is created for functional printing!
You can select which type of print functionality you need for effective printing with desired colors!
version 0.0.1
@keklikyusuf
"""

import datetime
import sys


class BColors:

    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    normal = '\033[0m'


class PrintStamps:

    def __init__(self, color):
        self.spacer = '------------------------------------------------------------------------------------'
        self.color = color

    def dateStamp(self, message):
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%d/%m/%Y")}: {message} \n{self.spacer}'
        print(text)
        return text

    def timeStamp(self, message):
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%X")}: {message} \n{self.spacer}'
        print(text)
        return text

    def datetimeStamp(self, message):
        sys.stdout.write(self.color)
        now = datetime.datetime.now()
        text = f'{now.strftime("%d/%m/%Y - %X")}: {message} \n{self.spacer}'
        print(text)
        return text

if __name__ == '__main__':
    printPurple = PrintStamps(BColors.purple)
    printBlue = PrintStamps(BColors.blue)
    printCyan = PrintStamps(BColors.cyan)
    printGreen = PrintStamps(BColors.green)
    printYellow = PrintStamps(BColors.yellow)
    printRed = PrintStamps(BColors.red)
    printNormal = PrintStamps(BColors.normal)
    ###########################################
    printPurple.dateStamp('Printing with date stamp!')
    printPurple.timeStamp('Printing with time stamp!')
    printPurple.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printBlue.dateStamp('Printing with date stamp and error!')
    printBlue.timeStamp('Printing with time stamp!')
    printBlue.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printCyan.dateStamp('Printing with date stamp and error!')
    printCyan.timeStamp('Printing with time stamp!')
    printCyan.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printGreen.dateStamp('Printing with date stamp and error!')
    printGreen.timeStamp('Printing with time stamp!')
    printGreen.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printYellow.dateStamp('Printing with date stamp and error!')
    printYellow.timeStamp('Printing with time stamp!')
    printYellow.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printRed.dateStamp('Printing with date stamp and error!')
    printRed.timeStamp('Printing with time stamp!')
    printRed.datetimeStamp('Printing with date and time stamp!')
    ###########################################
    printNormal.dateStamp('Printing with date stamp and error!')
    printNormal.timeStamp('Printing with time stamp!')
    printNormal.datetimeStamp('Printing with date and time stamp!')





