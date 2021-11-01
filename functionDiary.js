function noData() {
    const div = document.createElement("div")
    div.setAttribute("class", "div-normal")
    document.body.appendChild(div) 
    const h2 = document.createElement("h2")
    h2.innerText ="You don't have any recorded diaries yet, head to the 'Enter Data' page in navigation bar and create one!"
    div.appendChild(h2)
}

function loadDiary() {
    if (!localStorage.tmt) return noData()
    data = JSON.parse(localStorage.tmt)
    if (data.status != "DONE") return noData()
    data = data.data
    i = 0
    Object.keys(data).reverse().forEach(month => {
        Object.keys(data[month]).reverse().forEach(day => {
            if (data[month][day].diary) {
                i++
                const div = document.createElement("div")
                div.setAttribute("class", "div-normal")
                document.body.appendChild(div)
                const button = document.createElement("button")
                button.setAttribute("onclick", `getDiary(${month}, ${day})`)
                button.innerText = `Month ${month} - Day ${day}`
                const text = document.createElement("p")
                text.innerText = data[month][day].diary
                text.setAttribute("style", "display: none;")
                text.setAttribute("id", `${month}/${day}`)

                div.appendChild(button)
                div.appendChild(text)
            }
        })
    })
    console.log("Found " + i + " datas.")
    if (i < 1) return noData()
}

function getDiary(month, day) {
    console.log(month, day)
    const el = document.getElementById(`${month}/${day}`)
    if (el) {
        if (el.style.display === "none") {
            el.style.display = "block"
        } else {
            el.style.display = "none"
        }
    }
}

loadDiary()