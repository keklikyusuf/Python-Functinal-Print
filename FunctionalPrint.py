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
    printPurple.dateStamp('Printing with date stamp with Purple!')
    printPurple.timeStamp('Printing with time stamp with Purple!')
    printPurple.datetimeStamp('Printing with date and time stamp with Purple!')
    printBlue.dateStamp('Printing with date stamp with Blue!')
    printBlue.timeStamp('Printing with time stamp with Blue!')
    printBlue.datetimeStamp('Printing with date and time stamp with Blue!')
    printCyan.dateStamp('Printing with date stamp with Cyan!')
    printCyan.timeStamp('Printing with time stamp with Cyan!')
    printCyan.datetimeStamp('Printing with date and time stamp with Cyan!')
    printGreen.dateStamp('Printing with date stamp with Green!')
    printGreen.timeStamp('Printing with time stamp with Green!')
    printGreen.datetimeStamp('Printing with date and time stamp with Green!')
    printYellow.dateStamp('Printing with date stamp with Yellow!')
    printYellow.timeStamp('Printing with time stamp with Yellow!')
    printYellow.datetimeStamp('Printing with date and time stamp with Yellow!')
    printRed.dateStamp('Printing with date stamp with Red!')
    printRed.timeStamp('Printing with time stamp with Red!')
    printRed.datetimeStamp('Printing with date and time stamp with Red!')
    printNormal.dateStamp('Printing with date stamp with Normal/Gray!')
    printNormal.timeStamp('Printing with time stamp with Normal/Gray!')
    printNormal.datetimeStamp('Printing with date and time stamp with Normal/Gray!')





