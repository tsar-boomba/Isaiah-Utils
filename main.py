import os, time, sys

legalInputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
global numberOfGuards
numberOfGuards = 0
global timeToSwitch
timeToSwitch = 0
global hours
hours = 0
global minutes
minutes = 0


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

def inputValidation(validatedInput):
    global numberOfGuards
    global timeToSwitch
    global hours
    global minutes
    if validatedInput == numberOfGuards:
        tempInput = numberOfGuards
        if numberOfGuards < 1 or numberOfGuards > 10:
            print("Please inupt a number between 1 and 10")
            time.sleep(0.5)
            try:
                numberOfGuards = int(input("How many guards are working? (max 10) "))
                return numberOfGuards
            except ValueError:
                inputValidation(tempInput)
        else:
            return validatedInput
    elif validatedInput == timeToSwitch:
        tempInput = timeToSwitch
        if timeToSwitch < 1 or timeToSwitch > 60:
            print("Please inupt a number between 1 and 60")
            time.sleep(0.5)
            try:
                timeToSwitch = int(input("How long between swaps? (max 60 mins) "))
                return timeToSwitch
            except ValueError:
                inputValidation(tempInput)
        else:
            return validatedInput
    elif validatedInput == hours:
        tempInput = hours
        if hours < 1 or hours > 12:
            print("Please inupt a number between 1 and 12")
            time.sleep(0.5)
            try:
                hours = int(input("What hours will the rotation start? (1-12) "))
                return hours
            except ValueError:
                inputValidation(tempInput)
            
        else:
            return validatedInput
    elif validatedInput == minutes:
        tempInput = minutes
        if minutes < 0 or minutes > 59:
            print("Please inupt a number between 0 and 59")
            time.sleep(0.5)
            try:
                minutes = int(input("What minutes will the rotation start? (0 - 59) "))
                return minutes
            except ValueError:
                inputValidation(tempInput)
        else:
            return validatedInput

print("\n")
numberOfGuards = int(input("How many guards are working? (max 10) "))
numberOfGuards = inputValidation(numberOfGuards)
timeToSwitch = int(input("How long between swaps? (max 60 mins) "))
timeToSwitch = inputValidation(timeToSwitch)
hours = int(input("What hours will the rotation start? (1-12) "))
hours = inputValidation(hours)
minutes = int(input("What minutes will the rotation start? (0 - 59) "))
minutes = inputValidation(minutes)
timeFormatter()

