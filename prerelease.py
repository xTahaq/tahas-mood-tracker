#imports
import os
from datetime import date
import json
#from typing import OrderedDict
import time
import shutil
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
#import psutil
DRP = True
try:
    from pypresence import Presence
except ModuleNotFoundError:
    DRP = False
#default value
print("This is debugger log, you can see all of the printed texts here.\nLoading app...")
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


class SETTINGS:
    class drp:
        enabled = False
        activity = False

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

objects = []

#LOAD SETTINGS
with open("data.json", "r") as json_file:
    data = json.load(json_file)#, object_pairs_hook=OrderedDict)

    SETTINGS.drp.enabled = data["example_user"]["settings"]["discord_presence"]["enabled"]
    SETTINGS.drp.activity = data["example_user"]["settings"]["discord_presence"]["show_activity"]
        
        
#load discord rich presence
try:
    if SETTINGS.drp.enabled == True and DRP == True:
        client_id = '733025847493132371' 
        RPC = Presence(client_id,pipe=0) 
        RPC.connect()
except Exception:
    DRP = False

##################################################################################################


master = Tk()
master.title("Taha's Mood Tracker App")
master.minsize(1000,750)
master.option_add("*Font", "calibri")
mf = Frame(master)
mf.pack(side="top", expand=True, fill="both")


#functions
def clear():
    for widget in mf.winfo_children():
        widget.destroy()

def splitSerToArr(ser):
    return [ser.index, ser.as_matrix()]

def updateDiscordPresence(s, first=False):
    if DRP == True and SETTINGS.drp.enabled == True:
        if SETTINGS.drp.activity == True:
            RPC.update(details="Using Mood Tracker App by Taha", state=s, large_image="tmt", large_text="Taha's Mood Tracker App :)", start=startts)
        else:
            if first == True:
                RPC.update(details="Using Mood Tracker App by Taha", state="Activity is hidden", large_image="tmt", large_text="Taha's Mood Tracker App :)", start=startts)

def main():
    updateDiscordPresence("In Main Menu")
    clear()
    print("main menu")
    if date.today().year != workingYear:
        print("returned invalid year")
        Label(mf, text="Sorry, this program is outdated and needs to be updated to this year. Closing the program in 7 seconds...")
        time.sleep(7)
        exit()

    b1 = Button(mf, text="Log an activity", command=logActivity, height=2,width=30)
    b1.pack()
    b2 = Button(mf, text="Get statistics", command=statsMenu, height=2,width=30)
    b2.pack()
    b3 = Button(mf, text="Check diary", command=diaryMenu, height=2,width=30)
    b3.pack()
    b4 = Button(mf, text="Delete a data (NOT AVAILABLE)", command=deleteDataMenu, height=2,width=30)
    b4.pack()
    b5 = Button(mf, text="Backup data", command=backupData, height=2,width=30)
    b5.pack()
    b6 = Button(mf, text="Settings (NOT AVAILABLE)", command=settingsMenu, height=2,width=30)
    b6.pack()
    b7 = Button(mf, text="Exit", command=exit, height=2,width=30)
    b7.pack()
    space = Label(mf, text="")
    space.pack()
    frame = Frame(mf)
    frame.pack()
    cmdEntry = Entry(frame)
    cmdEntry.pack(side=LEFT)
    def enterCmd():
        cmd = cmdEntry.get()
        if cmd == "cmds":
            showCmds()
        elif cmd == "codingmode":
            codingMode()
        elif cmd == "idle":
            idleMode()
        else:
            cmdEntry.delete(0, END)
            cmdEntry.insert(0, "Invalid cmds, type 'cmds'")
    okbutton = Button(frame, text="OK", command=enterCmd, height=1, width=5)
    okbutton.pack(side=RIGHT)

def showCmds():
    clear()
    Label(mf, text="Available Commands:\ncolors - Shows all colors for this app (used in statistics tab) (NOT AVAILABLE ANYMORE / CONSOLE ONLY)\nidle - Changes your discord presence activity to 'Idle'").pack()
    Button(mf, text="Go Back", command=main).pack()

def createDateData():
    returnData = {}
    for m, dAmount in dayAndMonthData.items():
        returnData[m] = {}
        for d in range(1, dAmount + 1):
            returnData[m][str(d)] = {}
    return returnData

def backupData():
    clear()
    Label(mf, text="Taking a backup...\nQuit if it takes longer than few seconds.").pack()
    print("Starting a backup...")
    shutil.copy2('data.json', 'data_backup.json')
    clear()
    print("Done")
    Label(mf, text="Took a backup, you can go back now!").pack()
    Button(mf, text="Go Back", command=main).pack()

def codingMode():
    clear()
    updateDiscordPresence("Coding the app...")
    input("You are in CODING MODE. Please press ENTER to leave.")
    return

def idleMode():
    clear()
    updateDiscordPresence("Idle")
    print("idle mode trigger")
    if SETTINGS.drp.activity == True and DRP == True:
        Label(mf, text="[SUCCESS] - You are currently in Idle Mode. Press 'Go Back' to close idle mode.").pack()
    else:
        Label(mf, text="[ERROR] - Your discord is either closed, or you don't have an internet or you closed discord presence/discord presence activity in the settings.\nNone of these above? Try restarting.").pack()
    Button(mf, text="Go Back", command=main).pack()
    
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
    """
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
        if len(obj["d7"]) == 0: obj["d7"] = None"""
    texts = []
    if (t == "mood"):
        moodData = {}
        monthData = data["example_user"]["data"][m]
        loopA = 0
        for i,v in monthData.items():
            loopA = loopA + 1
            if len(v.keys()) > 0:
                moodData[i] = monthData[i]["mood"]
            else:
                moodData[i] = None
        figure = plt.figure(figsize=(5,5), dpi=100)
        figure.add_subplot(111).plot(moodData.keys(), moodData.values(), linestyle='-', marker='o')
        plt.ylim(0, 7)
        chart = FigureCanvasTkAgg(figure, mf)
        chart.get_tk_widget().pack()
        '''
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

        print(stringText)'''
    """
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

        print(stringText)"""


def questions(choiceM, choiceD):
    returnObject = {}
    def endQ(note):
        clear()
        returnObject["note"] = note
        print(returnObject)
        with open("data.json", "r+") as json_file:
            data = json.load(json_file)#, object_pairs_hook=OrderedDict)
            data["example_user"]["data"][choiceM][choiceD] = returnObject
            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()
            print("logged status for today")

            l = Label(mf, text="Logged status for today!")
            l.pack()
            b = Button(mf, text="Go back", command=main)
            b.pack() 
    def q4(activityTXT):
        clear()
        activity = activityTXT.split(",")
        if activity[0] == "":
            activity = []
        n = 0
        for i in activity:
            activity[n] = i.strip()
            n = n + 1
        returnObject["activities"] = activity
        Label(mf, text="Type a note about this day (optional)\nIt will also show up on your diary.").pack()
        f = Frame(mf)
        f.pack()
        e = Entry(f)
        e.pack(side=LEFT)
        Button(f, text="OK", command=lambda: endQ(e.get())).pack(side=RIGHT)

    def q3(n):
        clear()
        returnObject["stress_level"] = n
        Label(mf, text="Type your activities, split your activities with commas (','). Leave it blank if you want.").pack()
        f = Frame(mf)
        f.pack()
        e = Entry(f)
        e.pack(side=LEFT)
        Button(f, text="OK", command=lambda: q4(e.get())).pack(side=RIGHT)
    def q2(n):
        clear()
        returnObject["mood"] = n
        Label(mf, text="Rate your stress level from 1 to 10").pack()
        f = Frame(mf)
        f.pack()
        Button(f, text="1", command=lambda: q3(1), width=3).pack(side=LEFT)
        Button(f, text="2", command=lambda: q3(2), width=3).pack(side=LEFT)
        Button(f, text="3", command=lambda: q3(3), width=3).pack(side=LEFT)
        Button(f, text="4", command=lambda: q3(4), width=3).pack(side=LEFT)
        Button(f, text="5", command=lambda: q3(5), width=3).pack(side=LEFT)
        Button(f, text="6", command=lambda: q3(6), width=3).pack(side=LEFT)
        Button(f, text="7", command=lambda: q3(7), width=3).pack(side=LEFT)
        Button(f, text="8", command=lambda: q3(8), width=3).pack(side=LEFT)
        Button(f, text="9", command=lambda: q3(9), width=3).pack(side=LEFT)
        Button(f, text="10", command=lambda: q3(10), width=3).pack(side=LEFT)
    #mood question
    Label(mf, text="How are you feeling right now?").pack()
    Button(mf, text="VERY AWESOME!", command=lambda: q2(7), width=14).pack()
    Button(mf, text="Amazing", command=lambda: q2(6), width=14).pack()
    Button(mf, text="Good", command=lambda: q2(5), width=14).pack()
    Button(mf, text="Meh", command=lambda: q2(4), width=14).pack()
    Button(mf, text="Bad", command=lambda: q2(3), width=14).pack()
    Button(mf, text="Very bad", command=lambda: q2(2), width=14).pack()
    Button(mf, text="Disgusting", command=lambda: q2(1), width=14).pack()


def logActivity():
    updateDiscordPresence("Logging a daily activity")
    clear()
    print("log menu")
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    def apply(choiceM, choiceD):
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
                print("data setup done")

            if len(data["example_user"]["data"][choiceM][choiceD]) > 0:
                l = Label(mf, text="There's already a data about today!")
                l.pack()
                b = Button(mf, text="Go back", command=main)
                b.pack()
                return

            questions(choiceM, choiceD)

    def activityToday():
        apply(curMonth, curDay)
    def activityAny():
        input("ERR: Not done")
    label = Label(mf, text="Choose an action")
    label.pack()
    b1 = Button(mf, text="Log an activity for today", command=activityToday)
    b1.pack()
    b2 = Button(mf, text="Log an activity for any day", command=activityAny)
    b2.pack()
    b3 = Button(mf, text="Return to menu", command=main)
    b3.pack()
        
def statsMenu():
    updateDiscordPresence("Looking at statistics")
    clear()
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

        print("stats menu")
        Label(mf, text="Mood statistics\nYour mood stats for this month. Higher is better.").pack()
        printLastWeekStatistics(curDay, curMonth, data, "mood")

        printLastWeekStatistics(curDay, curMonth, data, "stress")

        printLastWeekStatistics(curDay, curMonth, data, "notes")

        printLastWeekStatistics(curDay, curMonth, data, "activity")

        Button(mf, text="Go Back", command=main).pack()

def diaryMenu():
    print("diary menu")
    clear()
    updateDiscordPresence("Checking out their diary")
    curDay = date.today().day
    curMonth = date.today().month
    atLeastOne = False
    def loadit(month):
        clear()
        month = str(month)
        gridN = 2
        f = Frame(mf)
        f.pack(side="top", fill="both")
        Button(f, text="Go back", height=1, width=10, command=main).pack(side=RIGHT)
        Label(f, text="DIARY OF MONTH " + month).pack(side=LEFT)
        txt = ""
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            for k,v in data["example_user"]["data"][month].items():
                gridN = gridN + 1
                if len(v) != 0:
                    if k == str(curDay) and int(month) == curMonth:
                        txt = txt + "Day " + k + " (TODAY): " + v["note"] + "\n"
                        break
                    else:
                        txt = txt + "Day " + k + ": " + v["note"] + "\n"
        txtlab = Text(mf, height=500, width=1000)
        txtlab.pack()
        txtlab.insert(INSERT, txt)


    f1 = Frame(mf)
    f2 = Frame(mf)
    f3 = Frame(mf)
    f4 = Frame(mf)
    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()
    Button(f1, text="JANUARY - 1", command=lambda: loadit(1), height=2, width=15).pack(side=LEFT)
    Button(f1, text="FEBRUARY - 2", command=lambda: loadit(2), height=2, width=15).pack(side=LEFT)
    Button(f1, text="MARCH - 3", command=lambda: loadit(3), height=2, width=15).pack(side=RIGHT)
    Button(f2, text="APRIL - 4", command=lambda: loadit(4), height=2, width=15).pack(side=LEFT)
    Button(f2, text="MAY - 5", command=lambda: loadit(5), height=2, width=15).pack(side=LEFT)
    Button(f2, text="JUNE - 6", command=lambda: loadit(6), height=2, width=15).pack(side=RIGHT)
    Button(f3, text="JULY - 7", command=lambda: loadit(7), height=2, width=15).pack(side=LEFT)
    Button(f3, text="AUGUST - 8", command=lambda: loadit(8), height=2, width=15).pack(side=LEFT)
    Button(f3, text="SEPTEMBER - 9", command=lambda: loadit(9), height=2, width=15).pack(side=RIGHT)
    Button(f4, text="OCTOBER - 10", command=lambda: loadit(10), height=2, width=15).pack(side=LEFT)
    Button(f4, text="NOVEMBER - 11", command=lambda: loadit(11), height=2, width=15).pack(side=LEFT)
    Button(f4, text="DECEMBER - 12", command=lambda: loadit(12), height=2, width=15).pack(side=RIGHT)
    

def deleteDataMenu():
    clear()
    updateDiscordPresence("Deleting a data...")
    curDay = str(date.today().day)
    curMonth = str(date.today().month)
    opt = input("Which data you want to delete? Please choose:\n1 - Delete today's data\n2 - Delete any day's data\n3 - Cancel\n\n> ")
    choiceM = None
    choiceD = None
    if opt != "1" and opt != "2" and opt != "3":
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
    elif opt == "1":
        choiceM = curMonth
        choiceD = curDay
    else:
        return

    with open("data.json", "r+") as json_file:
            data = json.load(json_file)#, object_pairs_hook=OrderedDict)

            data["example_user"]["data"][choiceM][choiceD] = {}
            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()
            input("Deleted the data, please press ENTER to return to menu.")

def settingsMenu():
    clear()
    updateDiscordPresence("In settings menu")
    print("---------------------------------------\nSETTINGS\n---------------------------------------\n\n")
    print("Commands:\n\ndiscordpresence [on/off] - Turns discord rich presence on/off for this app.\ndiscordpresenceactivity [on/off] - Makes it so it shows/doesn't show what are you doing in the app.")
    cmd = input("\n>")
    if cmd == "discordpresence on" or cmd == "discordpresence off":
        b = None
        if cmd == "discordpresence on":
            b = True
        else:
            b = False

        with open("data.json", "r+") as json_file:
            data = json.load(json_file)#, object_pairs_hook=OrderedDict)
            
            data["example_user"]["settings"]["discord_presence"]["enabled"] = b

            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()
            print("Discord presence is now", b)
            input("You need to restart app to save changes, press ENTER to go back to menu.")

    elif cmd == "discordpresenceactivity on" or cmd == "discordpresenceactivity off":
        b = None
        if cmd == "discordpresenceactivity on":
            b = True
        else:
            b = False
        
        with open("data.json", "r+") as json_file:
            data = json.load(json_file)#, object_pairs_hook=OrderedDict)
            
            data["example_user"]["settings"]["discord_presence"]["show_activity"] = b

            json_file.seek(0)
            json.dump(data, json_file, indent=4, sort_keys=False)
            json_file.truncate()
            print("Show activity in discord presence is now", b)
            input("You need to restart app to save changes, press ENTER to go back to menu.")


def passwordMenu():

    updateDiscordPresence("Entering password...", True)

    label = Label(mf, text="Please enter the password")
    label.pack()
    entry = Entry(mf)
    entry.pack()
    labelSpace = Label(mf,text="")
    labelSpace.pack()

    def buttonFunc():
        print("Recieved", entry.get())
        if entry.get() == PASSWORD[0] or entry.get() == PASSWORD[1]:
            main()
        else:
            entry.delete(0, END)
            entry.insert(0, "WRONG PASSWORD")

    button = Button(mf, text="ENTER", command=buttonFunc)
    button.pack()

passwordMenu()
master.mainloop()