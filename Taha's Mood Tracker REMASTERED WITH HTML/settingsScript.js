//const resetdata = document.getElementById("RESET_DATA")
const dataInput = document.getElementById("dataInput")

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
        data: pastedData.data
    })

}

function checkUpdate() {
    return alert("This is unavailable in dev builds & early access releases, will be added after a full release is out.")
}