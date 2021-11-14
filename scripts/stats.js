date = new Date()
day = date.getDate()
month = date.getMonth() + 1

lastmonthdata_mood = []
lastmonthdata_stress = []
activitySummary = [] // {"name": name, "amount": amount}

function loadTodaysStats() {
    if (!localStorage.tmt) return alert("No data found. Please head to main page first. If this still persists this might be a bug.")
    tmt = JSON.parse(localStorage.tmt)
    if (!tmt.data) return alert("No data found. Please head to main page first. If this still persists this might be a bug.")
    today = tmt.data[month][day]
    if (today.mood) document.getElementById("todaymood").innerText = today.mood
    if (today.stress) document.getElementById("todaystress").innerText = today.stress
    if (today.activities) document.getElementById("todayactivities").innerText = today.activities.toString()
    if (today.diary) document.getElementById("todaydiary").innerText = today.diary
}

function loadLastMonthData() {
    if (!localStorage.tmt) return
    tmt = JSON.parse(localStorage.tmt)
    if (!tmt.data || tmt.status != "DONE") return


    Object.keys(tmt.data[month - 1]).forEach((d, i) => {
        ri = (i + 1).toString()
        if (ri > day) {
            activity = tmt.data[month - 1][d].activities ? tmt.data[month - 1][d].activities : []
            mood = tmt.data[month - 1][d].mood
            stress = tmt.data[month - 1][d].stress
            //if (!mood) mood = null
            lastmonthdata_mood.push({
                label: ri, y: mood ? Number(mood) : null
            })
            lastmonthdata_stress.push({
                label: ri, y: stress ? Number(stress) : null
            })

            activity.forEach(a => {
                act = activitySummary.find(obj => obj.name === a)
                if (act) {
                    act.amount = act.amount + 1
                } else {
                    activitySummary.push({
                        name: a,
                        amount: 1
                    })
                }
            })
        }
    })
    Object.keys(tmt.data[month]).forEach((d, i) => {
        ri = (i + 1).toString()
        if (ri <= day) {
            activity = tmt.data[month][d].activities ? tmt.data[month][d].activities : []
            mood = tmt.data[month][d].mood
            stress = tmt.data[month][d].stress
            //if (!mood) mood = null
            lastmonthdata_mood.push({
                label: ri, y: mood ? Number(mood) : null
            })
            lastmonthdata_stress.push({
                label: ri, y: stress ? Number(stress) : null
            })

            activity.forEach(a => {
                activity = tmt.data[month - 1][d].activities ? tmt.data[month - 1][d].activities : []
                act = activitySummary.find(obj => obj.name === a)
                if (act) {
                    act.amount = act.amount + 1
                } else {
                    activitySummary.push({
                        name: a,
                        amount: 1
                    })
                }
            })
        }
    })
    console.log(lastmonthdata_mood, lastmonthdata_stress, activitySummary)
}

function fetchAQuote() {
    fetch("https://gist.githubusercontent.com/b1nary/ea8fff806095bcedacce/raw/6e6de20d7514b93dd69b149289264997b49459dd/enterpreneur-quotes.json").then(res => res.json()).then(quotes => {
        quote = quotes[Math.floor(Math.random() * quotes.length)]
        document.getElementById("randomQuote").innerText = quote.text + " - " + quote.from
    }).catch(err => err) //ignore error
}

function exportActivityData() {
    activityDiv = document.getElementById("lastmonthactivity")
    activitySummary.forEach(ac => {
        el = document.createElement("p")
        el.innerText = ac.name + ": " + ac.amount + " times"
        activityDiv.appendChild(el)
    })
}

loadTodaysStats()
loadLastMonthData()
fetchAQuote()

window.onload = function () {
    try {CanvasJS} catch(err) {return alert("Cannot find CanvasJS! Please check your internet connection, need internet connection to make a graph.")}
	var chart = new CanvasJS.Chart("lastmonthgraph", {
        animationEnabled: true,
        zoomEnabled: false,
        theme: "dark2",
        title: {
            text: "Mood and Stress Index Graph for Last 30 Days"
        },
        axisX: {
            title: "Day",
            interval: 1
        },
        axisY: {
            minimum: 0,
            maximum: 10,
            title: "Index",
            titleFontColor: "#6D78AD",
            lineColor: "#6D78AD",
            gridThickness: 0.1,
            lineThickness: 1
        },
        legend: {
            horizontalAlign: "top",
            verticalAlign: "top"
        },
        data: [{
            showInLegend: true,
            connectNullData: true,
            type: "line",
            color: "#1bbf47",
            name: "Mood Index",
            dataPoints: lastmonthdata_mood
        },
        {
            showInLegend: true,
            connectNullData:true,
            type: "line",
            color: "#1573ed",
            name: "Stress Index",
            dataPoints: lastmonthdata_stress
        }]
    });
    chart.render();
    exportActivityData()

}