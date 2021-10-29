// Do NOT touch any variables or anything here
VERSION = "demo.14-dev"

// pre-loaded objects

OBJ_NAVBAR = `<header>
<nav id="navbar">
    <h1 id="navtitle">Taha's Mood Tracker <span class="smaller-font">(dev-build - version: ${VERSION})</span></h1>
    <ul>
      <li><a name="navbarlocate" href="main.html">Main Page</a></li>
      <li><a name="navbarlocate" href="addData.html">Enter Data</a></li>
      <li><a name="navbarlocate" href="">Placeholder</a></li>
      <li><a name="navbarlocate" href="">Placeholder</a></li>
    </ul>
  </nav>
</header>`

//Loading vars
AppName = "TMT"
if (VERSION.search("dev")) AppName = "TMT (dev-build) / version: " + VERSION 

//Funcs

///////////////////////////////////

document.title = `${AppName} - ${document.title}`
document.getElementById("navbar-div").innerHTML = OBJ_NAVBAR

navbar = document.getElementById("navbar")
if (navbar) {
    navbar.style["background-color"] = "powderblue"
    //navbar.style["color"] = "red"
}