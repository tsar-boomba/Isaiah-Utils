import os, time, sys

legalInputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberOfGuards = "null"
timeToSwitch = "null"
hours = "null"
meridian = "null"
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
        numberOfGuards = numberOfGuardsValidation()
    except ValueError:
        numberOfGuards = numberOfGuardsValidation()
    try:
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
        global meridian
        meridian = input("Will it start in the AMs or PMs? (AM or PM) ")
        meridian = meridianValidation()
    except:
        meridian = meridianValidation()
    try:
        global minutes
        minutes = int(input("What minute will the rotation start at? (0 - 59) "))
        minutes = minutesValidation()
    except ValueError:
        minutes = minutesValidation()
    global rotations
    rotations = (21-hours)*(60/timeToSwitch)
    global startTime
    startTime = timeFormatter()
    global tempNOG
    tempNOG = str(numberOfGuards)
    global tempTTS
    tempTTS = str(timeToSwitch)
    global tempTime
    tempTime = str(startTime)
    global guardNumber
    guardNumber = 1
    global finalValidation
    finalValidation = input("\nIs this info corect?\nThere are " + tempNOG + " guards working.\nSwap every " + tempTTS + " minutes.\nStart working at " + tempTime + meridian + ".\n(Y for yes, N for no) ")
    finalValidationValidation()
    input("\nPress enter to end the program. ")

def timeFormatter():
    global hours
    hours = str(hours)
    global minutes
    global startTime
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
        if 1 <= numberOfGuards <= 10:
            return numberOfGuards
        else:
            print("Please input a number from 1 to 10")
            time.sleep(1)
            try:
                numberOfGuards = int(input("How many guards are working? (max 10) "))
                return numberOfGuardsValidation()
            except ValueError:
                return numberOfGuardsValidation()
    except:
        print("Please input a number from 1 to 10")
        time.sleep(1)
        try:
            numberOfGuards = int(input("How many guards are working? (max 10) "))
            return numberOfGuardsValidation()
        except ValueError:
            return numberOfGuardsValidation()

def timeToSwitchValidation():
    global timeToSwitch
    try:
        if 1 <= timeToSwitch <= 60:
            return timeToSwitch
        else:
            print("Please input a number between 1 and 60")
            time.sleep(1)
            try:
                timeToSwitch = int(input("How long between swaps? (max 60) "))
                return timeToSwitchValidation()
            except ValueError:
                return timeToSwitchValidation()
    except TypeError:
        try:
            timeToSwitch = int(input("How long between swaps? (max 60) "))
            return timeToSwitchValidation()
        except ValueError:
            return timeToSwitchValidation()

def hoursValidation():
    global hours
    try:
        if 1 <= hours <= 12:
            return hours
        else:
            print("Please input a number between 1 and 12")
            time.sleep(1)
            try:
                hours = int(input("What hour will the rotation start at? (1-12) "))
                return hoursValidation()
            except ValueError:
                return hoursValidation()
    except TypeError:
        try:
            hours = int(input("What hour will the rotation start at? (1-12) "))
            return hoursValidation()
        except ValueError:
            return hoursValidation()

def meridianValidation():
    global meridian
    try:
        if meridian == "AM" or meridian == "PM":
            return meridian
        else:
            print("Please input \"AM\" or \"PM\".")
            time.sleep(1)
            try:
                meridian = input("Will it start in the AMs or PMs? (AM or PM) ")
                return meridianValidation()
            except:
                return meridianValidation()
    except:
        try:
            meridian = input("Will it start in the AMs or PMs? (AM or PM) ")
            return meridianValidation()
        except:
            return meridianValidation()

def minutesValidation():
    global minutes
    try:
        if 0 <= minutes <= 59:
            return minutes
        else:
            print("Please input a number between 1 and 12")
            time.sleep(1)
            try:
                minutes = int(input("What minute will the rotation start at? (0-59) "))
                return minutesValidation()
            except:
                return minutesValidation()
    except TypeError:
        try:
            minutes = int(input("What minute will the rotation start at? (0-59) "))
            return minutesValidation()
        except:
            return minutesValidation()

def finalValidationValidation():
    global finalValidation
    global tempNOG
    global tempTTS
    global tempTime
    if finalValidation == "y" or finalValidation == "Y":
        print("Great! Generating your schedule...")
        time.sleep(3)
        scheduleGenerator()
    elif finalValidation == "n" or finalValidation == "N":
        print("Okay... restarting the program i guess...")
        time.sleep(2)
        return main()
    else:
        print("Input Y for yes and N for no")
        time.sleep(1)
        finalValidation = input("Is this info corect?\nThere are " + tempNOG + " guards working.\n Swap every " + tempTTS + " minutes.\n Start working at " + tempTime + meridian + ".\n (Y for yes, N for no) ")
        return finalValidationValidation()

def scheduleGenerator():
    global numberOfGuards
    global timeToSwitch
    global rotations
    global hours
    global meridian
    global minutes
    minutes = int(minutes)
    global startTime
    global guardNumber
    if rotations > 0:
        shiftTime = timeFormatter()
        guardNumber = str(guardNumber)
        print("Guard " + guardNumber + "  " + shiftTime + meridian)
        guardNumber = int(guardNumber)
        guardNumber = guardNumber + 1
        if guardNumber > numberOfGuards:
            guardNumber = 1
        rotations = rotations - 1
        hours = int(hours)
        minutes = int(minutes)
        minutes = minutes + timeToSwitch
        if minutes >= 60:
            hours = hours + 1
            minutes = minutes - 60
        if hours > 12:
            hours = 1
        if hours == 12:
            if meridian == "AM":
                meridian = "PM"
        return scheduleGenerator()
    else:
        print("\nDone! :D")


if __name__ == "__main__":
    main()