function toggle() {
    var x = document.getElementById("topnav");
    if (x.style.opacity == 0) {
        x.style.display = "block";
        x.style.opacity = 0.9;
    } else {
        x.style.opacity = 0;
        x.style.display = "none";
    }
}