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

function check() {
    if (!localStorage.tmt) {
        return true
    } else {
        data = JSON.parse(localStorage.tmt)
        if (data.status != "DONE") return true
    }
    return false
}
if (check() === true) {
    data = {
        status: "INCOMPLETE",
        createdAtVersion: VERSION,
        data: {}
    }

    Object.keys(dayAndMonthData).forEach((m) => {
        data.data[m] = {}
        dayA = dayAndMonthData[m]
        for (i = 1; i < dayA + 1; i++) {
            data.data[m][i.toString()] = {}
        }
    })

    data.status = "DONE"
    localStorage.tmt = JSON.stringify(data)
    console.log("Setup is done, object: " + data)
}