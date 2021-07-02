#imports
import os
from datetime import date
import json
#from typing import OrderedDict
import time
import shutil
#import psutil
from pypresence import Presence
#default value
print("Loading app...")
PASSWORD = ["TahaMadeThisApp", "lazypass"]
workingYear = 2021
dayAndMonthData = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}
startts = time.time()

DEFCOLOR = '\033[0m'
def rgb(r=0, g=0, b=0, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

class colors:
    class mood:
        c1 = rgb(0, 255, 0)
        c2 = rgb(19, 219, 15)
        c3 = rgb(132, 207, 27)
        c4 = rgb(222, 222, 24)
        c5 = rgb(235, 171, 21)
        c6 = rgb(242, 103, 17)
        c7 = rgb(255, 0, 0)
        
    class stress:
        c1 = rgb(10, 198, 255)
        c2 = rgb(10, 145, 255)
        c3 = rgb(19, 94, 235)
        c4 = rgb(56, 64, 214)
        c5 = rgb(143, 56, 214)
        c6 = rgb(196, 56, 214)
        c7 = rgb(209, 50, 167)
        c8 = rgb(235, 28, 131)
        c9 = rgb(237, 57, 90)
        c10 = rgb(224, 52, 52)

#load discord rich presence
client_id = '733025847493132371' 
RPC = Presence(client_id,pipe=0) 
RPC.connect()


##################################################################################################


#functions
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def updateDiscordPresence(s):
    pass
    RPC.update(details="Using Mood Tracker App by Taha", state=s, large_image="tmt", large_text="Taha's Mood Tracker App :)", start=startts)  # Set the presence

def main():
    updateDiscordPresence("In Main Menu")
    clear()
    print("--------------------------------------------------------\n\n\nWelcome to the Mood Tracker\n\nMade by Taha\n\n\n--------------------------------------------------------\n")
    if date.today().year != workingYear:
        print(date.today().year)
        input("Sorry! This program is outdated and needs to be updated. Press ENTER to leave.")
        exit()
    print("Activities:\n1 - Log an activity\n2 - Get statistics\n3 - Check diary\n4 - Delete a data\n5 - Backup data\n6 - Exit")
    OPT_menu = input("Please type an activity: ")
    if OPT_menu == "1":
        logActivity()
    elif OPT_menu == "2":
        statsMenu()
    elif OPT_menu == "3":
        diaryMenu()
    elif OPT_menu == "4":
        deleteDataMenu()
    elif OPT_menu == "5":
        backupData()
    elif OPT_menu == "6":
        exit()
    elif OPT_menu == "cmds":
        showCmds()
    elif OPT_menu == "colors":
        showColors()
    elif OPT_menu == "codingmode":
        codingMode()
    elif OPT_menu == "idle":
        idleMode()

def showCmds():
    clear()
    print("Commands:\ncolors - Shows all colors for this app (used in statistics tab)\ncodingmode - Changes your discord presence activity to 'Coding'\nidle - Changes your discord presence activity to 'Idle'")
    input("Press ENTER to go back to menu.")

def createDateData():
    returnData = {}
    for m, dAmount in dayAndMonthData.items():
        returnData[m] = {}
        for d in range(1, dAmount + 1):
            returnData[m][str(d)] = {}
    return returnData

def backupData():
    clear()
    print("Starting a backup...")
    shutil.copy2('data.json', 'data_backup.json')
    input("Backup complete, press ENTER to go back.")
    return

def codingMode():
    clear()
    updateDiscordPresence("Coding the app...")
    input("You are in CODING MODE. Please press ENTER to leave.")
    return

def idleMode():
    clear()
    updateDiscordPresence("Idle")
    input("You are in IDLE MODE. Please press ENTER to leave.")
    return
    
def showColors():
    clear()
    print("\nMood colors:\n\n" + colors.mood.c1 + "#" + colors.mood.c2 + "#" + colors.mood.c3 + "#" + colors.mood.c4 + "#" + colors.mood.c5 + "#" + colors.mood.c6 + "#" + colors.mood.c7 + "#" + DEFCOLOR)
    print("\n\nStress colors:\n\n" + colors.stress.c1 + "#" + colors.stress.c2 + "#" + colors.stress.c3 + "#" + colors.stress.c4 + "#" + colors.stress.c5 + "#" + colors.stress.c6 + "#" + colors.stress.c7 + "#" + colors.stress.c8 + "#" + colors.stress.c9 + "#" + colors.stress.c10 + "#" + DEFCOLOR)
    input("\n\n\nPress ENTER to go back to menu.")
    return

def printLastWeekStatistics(d, m, data, t):
    obj = {
        "d1": None,
        "d2": None,
        "d3": None,
        "d4": None,
        "d5": None,
        "d6": None,
        "d7": None
    }
    obj["d1"] = data["example_user"]["data"][m][d]
    if len(obj["d1"]) == 0: obj["d1"] = None
    if int(d) > 1:
        obj["d2"] = data["example_user"]["data"][m][str(int(d) - 1)]
        if len(obj["d2"]) == 0: obj["d2"] = None
    if int(d) > 2:
        obj["d3"] = data["example_user"]["data"][m][str(int(d) - 2)]
        if len(obj["d3"]) == 0: obj["d3"] = None
    if int(d) > 3:
        obj["d4"] = data["example_user"]["data"][m][str(int(d) - 3)]
        if len(obj["d4"]) == 0: obj["d4"] = None
    if int(d) > 4:
        obj["d5"] = data["example_user"]["data"][m][str(int(d) - 4)]
        if len(obj["d5"]) == 0: obj["d5"] = None
    if int(d) > 5:
        obj["d6"] = data["example_user"]["data"][m][str(int(d) - 5)]
        if len(obj["d6"]) == 0: obj["d6"] = None
    if int(d) > 6:
        obj["d7"] = data["example_user"]["data"][m][str(int(d) - 6)]
        if len(obj["d7"]) == 0: obj["d7"] = None
    texts = []
    if (t == "mood"):
        for k,v in obj.items():
            if not v:
                texts.append("No data")
            elif v and v["mood"] == 7:
                texts.append(colors.mood.c7 + "###                      (Disgusting)" + DEFCOLOR)
            elif v and v["mood"] == 6:
                texts.append(colors.mood.c6 + "######                   (Very Bad)" + DEFCOLOR)
            elif v and v["mood"] == 5:
                texts.append(colors.mood.c5 + "#########                (Bad)" + DEFCOLOR)
            elif v and v["mood"] == 4:
                texts.append(colors.mood.c4 + "############             (Meh)" + DEFCOLOR)
            elif v and v["mood"] == 3:
                texts.append(colors.mood.c3 + "###############          (Good)" + DEFCOLOR)
            elif v and v["mood"] == 2:
                texts.append(colors.mood.c2 + "##################       (Amazing)" + DEFCOLOR)
            elif v and v["mood"] == 1:
                texts.append(colors.mood.c1 + "#####################    (VERY AWESOME)" + DEFCOLOR)
            else: 
                texts.append("Unknown data (ERR: NOT VALID NUMBER)")
        n = 0
        stringText = ""
        for i in texts:
            n = n + 1
            stringText = stringText + str(n) + " => " + i + "\n"

        print(stringText)

    elif (t == "stress"):
        
        for k,v in obj.items():
            if not v:
                texts.append("No data")
            elif v and v["stress_level"] == 10:
                texts.append(colors.stress.c10 + "####################" + DEFCOLOR + "      (10)")
            elif v and v["stress_level"] == 9:
                texts.append(colors.stress.c9 + "##################" + DEFCOLOR + "         (9)")
            elif v and v["stress_level"] == 8:
                texts.append(colors.stress.c8 + "################" + DEFCOLOR + "           (8)")
            elif v and v["stress_level"] == 7:
                texts.append(colors.stress.c7 + "##############" + DEFCOLOR + "             (7)")
            elif v and v["stress_level"] == 6:
                texts.append(colors.stress.c6 + "############" + DEFCOLOR + "               (6)")
            elif v and v["stress_level"] == 5:
                texts.append(colors.stress.c5 + "##########" + DEFCOLOR + "                 (5)")
            elif v and v["stress_level"] == 4:
                texts.append(colors.stress.c4 + "########" + DEFCOLOR + "                   (4)")
            elif v and v["stress_level"] == 3:
                texts.append(colors.stress.c3 + "######" + DEFCOLOR + "                     (3)")
            elif v and v["stress_level"] == 2:
                texts.append(colors.stress.c2 + "####" + DEFCOLOR + "                       (2)")
            elif v and v["stress_level"] == 1:
                texts.append(colors.stress.c1 + "##" + DEFCOLOR + "                         (1)")
            else: 
                texts.append("Unknown data (ERR: NOT VALID NUMBER)")
        n = 0
        stringText = ""
        for i in texts:
            n = n + 1
            stringText = stringText + str(n) + " => " + i + "\n"

        print(stringText)

    elif (t == "notes"):

        for k,v in obj.items():
            if not v:
                texts.append("No data")
            else: 
                texts.append(v["note"])
        n = 0
        stringText = ""
        for i in texts:
            n = n + 1
            stringText = stringText + str(n) + " => " + i + "\n"

        print(stringText)
        
    elif (t == "activity"):

        for k,v in obj.items():
            if not v:
                texts.append("No data")
            else:
                txt = ""
                for x in v["activities"]:
                    txt = txt + x + " - "
                texts.append(txt)

        n = 0
        stringText = ""
        for i in texts:
            n = n + 1
            stringText = stringText + str(n) + " => " + i + "\n"

        print(stringText)


def questions():
    returnObject = {}
    #mood question
    QUESTION_mood = input("How are you feeling right now?\n1 - VERY AWESOME!\n2 - Amazing\n3 - Good\n4 - Meh\n5 - Bad\n6 - Very bad\n7 - Disgusting\n\n> ")
    QUESTIONSUCCESS_mood = False

    for i in range(1, 8):
        if str(i) == QUESTION_mood:
            QUESTIONSUCCESS_mood = True
            returnObject["mood"] = i
    if QUESTIONSUCCESS_mood == False:
        input("Your answer was invalid. Returning to the menu. Press ENTER to continue.")
        return

    QUESTION_stresslevel = input("Rate your stress level 1 to 10: ")
    QUESTIONSUCCESS_stresslevel = False

    for i in range(1, 11):
        if str(i) == QUESTION_stresslevel:
            QUESTIONSUCCESS_stresslevel = True
            returnObject["stress_level"] = i
    if QUESTIONSUCCESS_stresslevel == False:
        input("Your answer was invalid. Returning to the menu. Press ENTER to continue.")
        return

    returnObject["activities"] = []
    print("Please type your activities one by one, when you are done type 'DONE'")
    while True:
        QUESTION_activity = input("\n>")
        if QUESTION_activity == "DONE": 
            break
        else:
            returnObject["activities"].append(QUESTION_activity)

    QUESTION_notes = input("Type notes about this day! (optional)\n>>> ")
    returnObject["note"] = QUESTION_notes

    return returnObject


def logActivity():
    updateDiscordPresence("Logging a daily activity")
    clear()
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    opt = input("Choose an action:\n1 - Log an activity for today\n2 - Log an activity for any day\n> ")
    choiceM = None
    choiceD = None
    if opt != "1" and opt != "2":
        input("Invalid answer, press ENTER to go back to menu.")
        return
    elif opt == "2":
        choiceM = input("Please type the month: ")
        choiceD = input("Please type the day: ")
        try:
            choiceM = int(choiceM)
            choiceD = int(choiceD)
        except Exception:
            input("Invalid date number, press ENTER to go back to menu.")
            return

        if choiceM > int(curMonth):
            input("You cannot log activity for future data, press ENTER to go back to menu.")
            return
        elif choiceM <= int(curMonth) and choiceD > int(curDay):
            input("You cannot log activity for future data, press ENTER to go back to menu.")
            return

        choiceM = str(choiceM)
        choiceD = str(choiceD)
    else:
        choiceM = curMonth
        choiceD = curDay

    clear()
    with open("data.json", "r+") as json_file:
        data = json.load(json_file)#, object_pairs_hook=OrderedDict)
        
        if data["example_user"]["setup_status"] == 0:
            datedata = createDateData()
            for i,v in datedata.items():
                data["example_user"]["data"][i] = v
            data["example_user"]["setup_status"] = 1
            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()

        #if data["example_user"]["data"][choiceM][choiceD] == None:
        #    input("nope")
        #    return
        if len(data["example_user"]["data"][choiceM][choiceD]) > 0:
            input("There's already data about today! Press ENTER to go back to menu.")
            return
        obj = questions()

        data["example_user"]["data"][choiceM][choiceD] = obj
        json_file.seek(0)
        json.dump(data, json_file, indent=4, sort_keys=False)
        json_file.truncate()

        print("Logged status for today!")
        
def statsMenu():
    updateDiscordPresence("Looking at statistics")
    clear()
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

        print("------------------------------------\n\nMOOD AND STATUS STATISTICS\n\n------------------------------------")
        print("\nYour mood in last 7 days:\n")
        printLastWeekStatistics(curDay, curMonth, data, "mood")

        print("\n\n")

        printLastWeekStatistics(curDay, curMonth, data, "stress")

        print("\n\n")

        printLastWeekStatistics(curDay, curMonth, data, "notes")

        print("\n\n")

        printLastWeekStatistics(curDay, curMonth, data, "activity")

        print("\n\n")

        input("Press ENTER to go to the menu.")
        return

def diaryMenu():
    clear()
    updateDiscordPresence("Checking out their diary")
    curDay = date.today().day
    curMonth = date.today().month
    print("-----------------\nDIARY\n-----------------\n\n\n")
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
        for i in range(1, 13):
            if i > curMonth: break
            print("Month " + str(i) + ":")
            for k,v in data["example_user"]["data"][str(i)].items():
                if len(v) == 0:
                    if k == str(curDay) and i == curMonth:
                        print("    Day "+ k + " (TODAY): N/A")
                        break
                    else:
                        print("    Day "+ k + ": N/A")
                else:
                    if k == str(curDay) and i == curMonth:
                        print("    Day " + k + " (TODAY): " + v["note"])
                        break
                    else:
                        print("    Day " + k + ": " + v["note"])

    input("Press ENTER to return to menu.")
    return

def deleteDataMenu():
    clear()
    updateDiscordPresence("Deleting a data...")
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    ddmOpt = input("Which data you want to delete? Please choose:\ntoday / any / cancel\n\n> ")
    if ddmOpt == "today":
        with open("data.json", "r+") as json_file:
            data = json.load(json_file)#, object_pairs_hook=OrderedDict)

            data["example_user"]["data"][curMonth][curDay] = {}
            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()
            input("Deleted the data, please press ENTER to return to menu.")

    else:
        return

def passwordMenu():
    updateDiscordPresence("Entering password...")
    askpass = input("Please enter the PASSWORD to access this app: ")
    if askpass == PASSWORD[0] or askpass == PASSWORD[1]:
        while True:
            main()
    else:
        print("WRONG PASSWORD, exiting app in 3 seconds.")
        time.sleep(3)
        exit()

passwordMenu()