date = new Date()
day = date.getDate()
month = date.getMonth() + 1

activities = []
//LOAD ELEMENTS

const dayToday = document.getElementById("day_today")
const dayCustom = document.getElementById("day_other")
const customDayDate = document.getElementById("customDayDate")
const stressI = document.getElementById("stressIndex")
const moodI = document.getElementById("moodIndex")
const activityObj = document.getElementById("activity")
const activityEnter = document.getElementById("activityEnter")
const activityReset = document.getElementById("activityReset")
const activityOutput = document.getElementById("activityText")
const diary = document.getElementById("diary")
const output = document.getElementById("output")


customDayDate.setAttribute("disabled", "")
customDayDate.setAttribute("max", `2021-${month}-${day}`)

//functions

function dayOptionChanged() {
    if (dayToday.checked === true) {
        customDayDate.setAttribute("disabled", "")
    } else {
        customDayDate.removeAttribute("disabled")
    }
}

function checkIfNumberIsRight() {
    if (moodI.value < 0) moodI.value = 0
    if (moodI.value > 10) moodI.value = 10
    if (stressI.value < 0) stressI.value = 0
    if (stressI.value > 10) stressI.value = 10
}

function activityEntered() {
    entered = activityObj.value.trim()
    console.log(entered)
    if (entered === "") return
    entered = entered.toLowerCase()
    if (activities.find(e => e === entered)) return
    if (activities.length >= 20) return
    if (entered.length > 256) return
    activities.push(entered)
    activityOutput.innerText = "Activities: " + activities.join(", ")
    activityObj.value = ""
}

function activityReseted() {
    activities = []
    activityOutput.innerText = "Activities: None"
    activityObj.value = ""
}

function ENTER() {
    targetDay = 1
    targetMonth = 1
    object = {
        "mood": moodI.value,
        "stress": stressI.value,
        "activities": activities,
        "diary": diary.value
    }
    if (dayToday.checked === true) {
        targetDay = day.toString()
        targetMonth = month.toString()
    } else {
        if (customDayDate.value) {
            targetDate = customDayDate.value 
            targetDate = targetDate.split("-")
            targetMonth = targetDate[1]
            targetDay = targetDate[2]
        } else {
            output.innerText = "Error: You didn't enter a date!"
            return
        }
    }
    console.log(targetDay, targetMonth)
    if (!localStorage) return output.innerText = "Error: Data not found - this happens because you went to this page for first time without going to main page! - if it's not because of that please report the issue"
    data = JSON.parse(localStorage.tmt)
    if (data.data[targetMonth][targetDay]) {
        data.data[targetMonth][targetDay] = object
        localStorage.tmt = JSON.stringify(data)
        output.innerText = "Success: Data saved!"
    }
}