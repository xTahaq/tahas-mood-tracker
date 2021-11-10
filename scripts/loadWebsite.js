// Do NOT touch any variables or anything here
VERSION = "v2.0.2"
Settings = null
// pre-loaded objects

OBJ_NAVBAR = `<header>
<nav id="navbar">
    <h1 id="navtitle" style="color: black;">Taha's Mood Tracker <span class="smaller-font">(version: ${VERSION})</span></h1>
    <ul>
      <li><a name="navbarlocate" href="main.html">Main Page</a></li>
      <li><a name="navbarlocate" href="addData.html">Enter Data</a></li>
      <li><a name="navbarlocate" href="statistics.html">Statistics</a></li>
      <li><a name="navbarlocate" href="settings.html">Settings & Config</a></li>
      <li><a name="navbarlocate" href="help.html">Help</a></li>
    </ul>
  </nav>
</header>`

SETTINGS_OBJECT = {
  bg_img: "",
  bg_clr: "",
  txt_clr: "",
  alert_errors: true
}

//Funcs
function handleError(evt) {
  if (evt.message) { // Chrome sometimes provides this
    alert("error: "+evt.message +" at linenumber: "+evt.lineno+" of file: "+evt.filename);
  } else {
    alert("error: "+evt.type+" from element: "+(evt.srcElement || evt.target));
  }
}

function loadSettings() {
  if (!localStorage.tmt) return
  tmt = JSON.parse(localStorage.tmt)
  if (!tmt.settings) {
    tmt.settings = SETTINGS_OBJECT
  }
  if (tmt.settings.bg_img) document.body.style.backgroundImage = `url(${tmt.settings.bg_img})`
  if (tmt.settings.bg_clr) document.body.style.backgroundColor = tmt.settings.bg_clr
  if (tmt.settings.txt_clr) document.body.style.color = tmt.settings.txt_clr
  Settings = tmt.settings
}

//Loading vars
AppName = "TMT / version: " + VERSION
if (VERSION.search("dev")) AppName = "Taha's Mood Tracker / " + VERSION 

///////////////////////////////////

document.title = `${AppName} - ${document.title}`
document.getElementById("navbar-div").innerHTML = OBJ_NAVBAR
navbar = document.getElementById("navbar")
if (navbar) {
    navbar.style["background-color"] = "powderblue"
    //navbar.style["color"] = "red"
}
loadSettings()
try {
  if (Settings && Settings.alert_errors === true) window.addEventListener("error", handleError, true);
} catch(err) {console.log(err)}