function checkYear() {
    if (new Date().getFullYear() != 2021) {
      alert("CRITICAL WARNING: YEAR IS NOT 2021. MONTH-DAY NUMBERS WILL BE INCORRECT AND YOU MIGHT BREAK THE APP. PLEASE UPDATE THE APP IF YEAR IS 2022, DOWNLOAD HERE => https://github.com/xTahaq/tahas-mood-tracker  / (please clear your data at settings after updating)")
    }
}

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

checkYear()

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
        createdAtYear: 2021,
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