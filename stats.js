date = new Date()
day = date.getDate()
month = date.getMonth() + 1

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

loadTodaysStats()