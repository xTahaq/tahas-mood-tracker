// Do NOT touch any variables or anything here
VERSION = "demo.16-dev"

// pre-loaded objects

OBJ_NAVBAR = `<header>
<nav id="navbar">
    <h1 id="navtitle">Taha's Mood Tracker <span class="smaller-font">(dev-build - version: ${VERSION})</span></h1>
    <ul>
      <li><a name="navbarlocate" href="main.html">Main Page</a></li>
      <li><a name="navbarlocate" href="addData.html">Enter Data</a></li>
      <li><a name="navbarlocate" href="statistics.html">Statistics (PLACEHOLDER)</a></li>
      <li><a name="navbarlocate" href="settings.html">Settings & Config</a></li>
      <li><a name="navbarlocate" href="help.html">Help</a></li>
    </ul>
  </nav>
</header>`

//Funcs
function handleError(evt) {
  if (evt.message) { // Chrome sometimes provides this
    alert("error: "+evt.message +" at linenumber: "+evt.lineno+" of file: "+evt.filename);
  } else {
    alert("error: "+evt.type+" from element: "+(evt.srcElement || evt.target));
  }
}

//Loading vars
window.addEventListener("error", handleError, true);
AppName = "TMT / version: " + VERSION
if (VERSION.search("dev")) AppName = "TMT (dev-build) / version: " + VERSION 

///////////////////////////////////

document.title = `${AppName} - ${document.title}`
document.getElementById("navbar-div").innerHTML = OBJ_NAVBAR

navbar = document.getElementById("navbar")
if (navbar) {
    navbar.style["background-color"] = "powderblue"
    //navbar.style["color"] = "red"
}