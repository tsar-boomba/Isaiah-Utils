import os, time, sys

oldNet = 0
oldGross = 0
taxRate = 0
week1Hrs = 0
week1Mins = 0
week1Ot = 0
week2Hrs = 0
week2Mins = 0
week2Ot = 0
totalHours = 0
payRate = 0

def main():
    print("\n")
    try:
        global oldGross
        oldGross = float(input("Input the gross pay of your last paystub (input 0 to skip tax calculation): "))
        oldGross = oldGrossValidation()
    except:
        oldGross = oldGrossValidation()
    if (oldGross == 0):
        inputHours()
    try:
        global oldNet
        oldNet = float(input("Input the net pay of your last paystub: "))
        oldNet = oldNetValidation()
    except:
        oldNet = oldNetValidation()
    global taxRate
    taxRate = 1 - ((oldGross - oldNet)/oldGross)
    inputHours()

def inputHours():
    try:
        global week1Hrs
        week1Hrs = int(input("Input your HOURS worked for the first week of this payperiod: "))
        week1Hrs = week1HrsValidation()
    except:
        week1Hrs = week1HrsValidation()
    try:
        global week1Mins
        week1Mins = int(input("Input your MINUTES worked for the first week of this payperiod: "))
        week1Mins = week1MinsValidation()
    except:
        week1Mins = week1MinsValidation()
    totalWeek1 = week1Hrs + (week1Mins/60)
    if (totalWeek1 > 40):
        global week1Ot
        week1Ot = week1Ot + (totalWeek1 - 40)
    try:
        global week2Hrs
        week2Hrs = int(input("Input your HOURS worked for the second week of this payperiod: "))
        week2Hrs = week2HrsValidation()
    except:
        week2Hrs = week2HrsValidation()
    try:
        global week2Mins
        week2Mins = int(input("Input your MINUTES worked for the second week of this payperiod: "))
        week2Mins = week2MinsValidation()
    except:
        week2Mins = week2MinsValidation()
    totalWeek2 = week2Hrs + (week2Mins/60)
    if (totalWeek2 > 40):
        global week2Ot
        week2Ot = week2Ot + (totalWeek2 - 40)
    global totalHours
    totalHours = (totalWeek1 - week1Ot) + (totalWeek2 - week2Ot)
    calcPay()

def calcPay():
    global oldGross, taxRate, totalHours, week1Ot, week2Ot
    totalOt = week1Ot + week2Ot
    try:
        global payRate
        payRate = int(input("Input your $/hr payrate (deciamals are ok): "))
        payRate = payRateValidation()
    except:
        payRate = payRateValidation()
    if (oldGross == 0):
        print(f"Your projected pay is: {((payRate * totalHours) + ((payRate * 1.5) * totalOt)) * 0.925}")
    else:
        print(f"Your projected pay is: {((payRate * totalHours) + ((payRate * 1.5) * totalOt)) * taxRate}")
    input("Press enter to end program")


def oldGrossValidation():
    global oldGross
    try:
        if 1 <= oldGross <= 3000:
            return oldGross
        else:
            print("Please input a number from 1 to 3,000")
            time.sleep(1)
            try:
                oldGross = float(input("Input the gross pay of your last paystub: "))
                return oldGrossValidation()
            except ValueError:
                return oldGrossValidation()
    except:
        print("Please input a number from 1 to 3,000")
        time.sleep(1)
        try:
            oldGross = float(input("Input the gross pay of your last paystub: "))
            return oldGrossValidation()
        except ValueError:
            return oldGrossValidation()

def oldNetValidation():
    global oldNet
    try:
        if 1 <= oldNet <= 3000:
            return oldNet
        else:
            print("Please input a number from 1 to 3,000")
            time.sleep(1)
            try:
                oldNet = float(input("Input the gross pay of your last paystub: "))
                return oldNetValidation()
            except ValueError:
                return oldNetValidation()
    except:
        print("Please input a number from 1 to 3,000")
        time.sleep(1)
        try:
            oldNet = int(input("Input the gross pay of your last paystub: "))
            return oldNetValidation()
        except ValueError:
            return oldNetValidation()

def week1HrsValidation():
    global week1Hrs
    try:
        if 1 <= week1Hrs <= 80:
            return week1Hrs
        else:
            print("Please input a number from 1 to 80")
            time.sleep(1)
            try:
                week1Hrs = int(input("Input your HOURS worked for the first week of this payperiod:"))
                return week1HrsValidation()
            except ValueError:
                return week1HrsValidation()
    except:
        print("Please input a number from 1 to 80")
        time.sleep(1)
        try:
            week1Hrs = int(input("Input your HOURS worked for the first week of this payperiod:"))
            return week1HrsValidation()
        except ValueError:
            return week1HrsValidation()

def week1MinsValidation():
    global week1Mins
    try:
        if 1 <= week1Mins <= 59:
            return week1Mins
        else:
            print("Please input a number from 1 to 59")
            time.sleep(1)
            try:
                week1Mins = int(input("Input your MINUTES worked for the first week of this payperiod: "))
                return week1MinsValidation()
            except ValueError:
                return week1MinsValidation()
    except:
        print("Please input a number from 1 to 59")
        time.sleep(1)
        try:
            week1Mins = int(input("Input your MINUTES worked for the first week of this payperiod: "))
            return week1MinsValidation()
        except ValueError:
            return week1MinsValidation()

def week2HrsValidation():
    global week2Hrs
    try:
        if 1 <= week2Hrs <= 80:
            return week2Hrs
        else:
            print("Please input a number from 1 to 80")
            time.sleep(1)
            try:
                week2Hrs = int(input("Input your HOURS worked for the second week of this payperiod: "))
                return week2HrsValidation()
            except ValueError:
                return week2HrsValidation()
    except:
        print("Please input a number from 1 to 80")
        time.sleep(1)
        try:
            week2Hrs = int(input("Input your HOURS worked for the second week of this payperiod: "))
            return week2HrsValidation()
        except ValueError:
            return week2HrsValidation()

def week2MinsValidation():
    global week2Mins
    try:
        if 1 <= week2Mins <= 59:
            return week2Mins
        else:
            print("Please input a number from 1 to 59")
            time.sleep(1)
            try:
                week2Mins = int(input("Input your MINUTES worked for the second week of this payperiod: "))
                return week2MinsValidation()
            except ValueError:
                return week2MinsValidation()
    except:
        print("Please input a number from 1 to 59")
        time.sleep(1)
        try:
            week2Mins = int(input("Input your MINUTES worked for the second week of this payperiod: "))
            return week2MinsValidation()
        except ValueError:
            return week2MinsValidation()

def payRateValidation():
    global payRate
    try:
        if 7.25 <= payRate <= 15:
            return payRate
        else:
            print("Please input a number from 7.25 to 15")
            time.sleep(1)
            try:
                payRate = int(input("Input your $/hr payrate (deciamals are ok): "))
                return payRateValidation()
            except ValueError:
                return payRateValidation()
    except:
        print("Please input a number from 7.25 to 15")
        time.sleep(1)
        try:
            payRate = int(input("Input your $/hr payrate (deciamals are ok): "))
            return payRateValidation()
        except ValueError:
            return payRateValidation()

if __name__ == "__main__":
    main()
