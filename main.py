import os, time, sys

legalInputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberOfGuards = "null"
timeToSwitch = "null"
hours = "null"
minutes = "null"
finalValidation = "null"
tempNOG = "null"
tempTTS = "null"
tempTime = "null"

def main():
    print("\n")
    try:
        global numberOfGuards
        numberOfGuards = int(input("How many guards are working? (max 10) "))
        print(numberOfGuards)
        numberOfGuards = numberOfGuardsValidation()
    except ValueError:
        numberOfGuards = numberOfGuardsValidation()
    try:
        print(numberOfGuards)
        global timeToSwitch
        timeToSwitch = int(input("How long between swaps? (max 60 mins) "))
        timeToSwitch = timeToSwitchValidation()
    except ValueError:
        timeToSwitch = timeToSwitchValidation()
    try:
        global hours
        hours = int(input("What hour will the rotation start at? (1-12) "))
        hours = hoursValidation()
    except ValueError:
        hours = hoursValidation()
    try:
        global minutes
        minutes = int(input("What minute will the rotation start at? (0 - 59) "))
        minutes = minutesValidation()
    except ValueError:
        minutes = minutesValidation()
    startTime = timeFormatter()
    global tempNOG
    tempNOG = str(numberOfGuards)
    global tempTTS
    tempTTS = str(timeToSwitch)
    global tempTime
    tempTime = str(startTime)
    global finalValidation
    finalValidation = input("\nIs this info corect?\nThere are " + tempNOG + " guards working.\nSwap every " + tempTTS + " minutes.\nStart working at " + tempTime + ".\n(Y for yes, N for no) ")
    finalValidationValidation()

def timeFormatter():
    global hours
    hours = str(hours)
    global minutes
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
        startTime = hours + ":" + minutes
        return startTime
    else:
        minutes = str(minutes)
        startTime = hours + ":" + minutes
        return startTime

def numberOfGuardsValidation():
    global numberOfGuards
    try:
        print(numberOfGuards)
        if numberOfGuards >= 1 or numberOfGuards <= 10:
            return numberOfGuards
        else:
            print("Please input a number from 1 to 10")
            time.sleep(1)
            try:
                numberOfGuards = int(input("How many guards are working? (max 10) "))
                numberOfGuards = numberOfGuardsValidation()
            except ValueError:
                numberOfGuardsValidation()
    except TypeError:
        print("Please input a number from 1 to 10")
        time.sleep(1)
        try:
            numberOfGuards = int(input("How many guards are working? (max 10) "))
            numberOfGuards = numberOfGuardsValidation()
        except ValueError:
            numberOfGuardsValidation()

def timeToSwitchValidation():
    global timeToSwitch
    try:
        if timeToSwitch >= 1 or timeToSwitch <= 60:
            return timeToSwitch
        else:
            print("Please input a number between 1 and 60")
            time.sleep(1)
            try:
                timeToSwitch = int(input("How long between swaps? (max 60) "))
                timeToSwitch = timeToSwitchValidation
            except ValueError:
                timeToSwitchValidation()
    except TypeError:
        try:
            timeToSwitch = int(input("How long between swaps? (max 60) "))
            timeToSwitch = timeToSwitchValidation
        except ValueError:
            timeToSwitchValidation()

def hoursValidation():
    global hours
    try:
        if hours >= 1 or hours <= 12:
            return hours
        else:
            print("Please input a number between 1 and 12")
            time.sleep(1)
            try:
                hours = int(input("What hour will the rotation start at? (1-12) "))
                hours = hoursValidation()
            except ValueError:
                hoursValidation()
    except TypeError:
        try:
            hours = int(input("What hour will the rotation start at? (1-12) "))
            hours = hoursValidation()
        except ValueError:
            hoursValidation()

def minutesValidation():
    global minutes
    try:
        if minutes >= 0 or minutes <= 59:
            return minutes
        else:
            print("Please input a number between 1 and 12")
            time.sleep(1)
            try:
                minutes = int(input("What minute will the rotation start at? (0-59) "))
                minutes = minutesValidation()
            except:
                minutesValidation()
    except TypeError:
        try:
            minutes = int(input("What minute will the rotation start at? (0-59) "))
            minutes = minutesValidation()
        except:
            minutesValidation()

def finalValidationValidation():
    global finalValidation
    global tempNOG
    global tempTTS
    global tempTime
    if finalValidation == "y" or finalValidation == "Y":
        print("Great! Generating your schedule...")
        time.sleep(3)
    elif finalValidation == "n" or finalValidation == "N":
        print("Okay... restarting the program i guess...")
        time.sleep(2)
        sys.exit()
    else:
        print("Input Y for yes and N for no")
        time.sleep(1)
        finalValidation = input("Is this info corect?\nThere are " + tempNOG + " guards working.\n Swap every " + tempTTS + " minutes.\n Start working at " + tempTime + ".\n (Y for yes, N for no) ")

if __name__ == "__main__":
    main()