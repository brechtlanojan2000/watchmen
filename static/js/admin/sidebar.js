const sidenav = document.getElementById("sidenav-admin");
const sidenavInstance = mdb.Sidenav.getInstance(sidenav);

let innerWidth = null;

const setMode = (e) => {
  // Check necessary for Android devices
    if (window.innerWidth === innerWidth) {
        return;
    }

    innerWidth = window.innerWidth;

    if (window.innerWidth < 1200) {
        sidenavInstance.changeMode("over");
        sidenavInstance.hide();
    } else {
        sidenavInstance.changeMode("side");
        sidenavInstance.show();
    }
};

setMode();

window.addEventListener("resize", setMode);