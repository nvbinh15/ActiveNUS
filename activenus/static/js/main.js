function toggle() {
    var x = document.getElementById("topnav");
    // if (x.style.display === "block") {
    //   x.style.display = "none";
    // } else {
    //   x.style.display = "block";
    // }
    if (x.style.opacity == 0) {
        x.style.opacity = 0.9;
    } else {
        x.style.opacity = 0;
    }
}