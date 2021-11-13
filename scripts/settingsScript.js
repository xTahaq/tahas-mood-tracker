let showingUpdates = false
//
const dataInput = document.getElementById("dataInput")
const pnTxt = document.getElementById("patchNotesText")

function refresh() {
    window.location.reload()
}
function clearData() {
    if (confirm("Are you sure? Pressing OK will CLEAR and RESET YOUR ENTIRE DATA!")) {
        localStorage.tmt = JSON.stringify({
            status: "DELETED"
        })
    }
}
function copyData() {
    if (localStorage.tmt) {
        navigator.clipboard.writeText(localStorage.tmt)
    }
}

function pasteData() {
    pastedData = {}
    try {
        pastedData = JSON.parse(dataInput.value)
    } catch(err) {
        return alert("Invalid data type. This isn't JSON!")
    }
    if (!pastedData.status) return alert("Missing status object. This isn't a valid data for TMT!")
    if (!pastedData.data) return alert("Missing data object. This isn't a valid data for TMT!")
    
    if (pastedData.createdAtYear != 2021) return alert("This data belongs to another year. Mood Tracker does not support older years, stated in help page. If you still want to view it somewhat, go to a 'JSON Formatter' website and paste this data there.")
    
    localStorage.tmt = JSON.stringify({
        status: "DONE",
        createdAtVersion: VERSION,
        createdAtYear: 2021,
        settings: pastedData.settings,
        data: pastedData.data
    })

}

function createSettings() {
    console.warn("Creating the settings data...")
    parsedData = JSON.parse(localStorage.tmt)
    parsedData.settings = SETTINGS_OBJECT
    localStorage.tmt = JSON.stringify(parsedData)
    console.log("Done.")
    refresh()
  }

function checkUpdate() {
    outp = document.getElementById("versionOutput")
    outp.innerText = `Update status: Checking...`
    fetch("https://gist.githubusercontent.com/xTahaq/90f1ff22989e6d579605a21e26fc0e2d/raw/e2d72c84d8dd4f69878bada7920a3ec72332a1dc/tmt-appinfo.json").then(res => res.json()).then(versionJson => {
            outp = document.getElementById("versionOutput")
            if (versionJson.version != VERSION) {
                outp.innerText = `Update status: New version available! (${VERSION} => ${versionJson.version}) Please update it at https://github.com/xTahaq/tahas-mood-tracker`
            } else {
                outp.innerText = `Update status: ${VERSION} is not outdated, you are up-to-date!`
            }
        }).catch(err => alert(err))
}

function viewLastUpdates() {
    if (showingUpdates === true) {
        pnTxt.innerText = ""
        showingUpdates = false
    } else {
        fetch("https://raw.githubusercontent.com/xTahaq/tahas-mood-tracker/master/appinfo.json").then(res => res.json()).then(versionJson => {
            textToShow = "Click the button again to hide this.\nTo see all versions, go to https://github.com/xTahaq/tahas-mood-tracker/releases\n\n"
            Object.keys(versionJson.lastestPatchNotes).forEach(release => {
                textToShow = `${textToShow} Update ${release} Patch Notes:\n`
                versionJson.lastestPatchNotes[release].forEach(line => {
                    textToShow = textToShow + line + "\n"
                })
            })
            pnTxt.innerText = textToShow
            showingUpdates = true
        }).catch(err => alert(err))
    }
}

function changeSetting(setting, arg) {
    if (!localStorage.tmt) return alert("No data found, please head to the main page first.")
    tmt = JSON.parse(localStorage.tmt)
    if (!tmt.settings) {
        createSettings()
        tmt = JSON.parse(localStorage.tmt)
    }
    if (setting === "bg_img") {
        if (arg === "input") {
            inp = document.getElementById("input_bg_img")
            if (inp) {
                tmt.settings.bg_img = inp.value
            }
        } else {
            tmt.settings.bg_img = ""
        }
    } else if (setting === "bg_clr") {
        if (arg === "input") {
            inp = document.getElementById("input_bg_clr")
            if (inp) {
                tmt.settings.bg_clr = inp.value
            }
        } else {
            tmt.settings.bg_clr = ""
        }
    } else if (setting === "txt_clr") {
        if (arg === "input") {
            inp = document.getElementById("input_txt_clr")
            if (inp) {
                tmt.settings.txt_clr = inp.value
            }
        } else {
            tmt.settings.txt_clr = ""
        }
    } else if (setting === "alert_errors") {
        if (arg === "true") {
            tmt.settings.alert_errors = true
        } else {
            tmt.settings.alert_errors = false
        }
    }
    localStorage.tmt = JSON.stringify(tmt)
    refresh()
}

if (localStorage.tmt) {
    tmt = JSON.parse(localStorage.tmt)
    if (tmt.settings) {
        document.getElementById("input_bg_img").value = tmt.settings.bg_img
        document.getElementById("input_bg_clr").value = tmt.settings.bg_clr || "#FFFFFF"
        document.getElementById("input_txt_clr").value = tmt.settings.txt_clr || "#000000"
        document.getElementById("alerterrinf").innerText = `(current: ${tmt.settings.alert_errors})`
    }
}