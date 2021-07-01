console.log("hello,world")

const copyBtns = [...document.getElementsByClassName('copy-btn')]

console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
    console.log('click')
    const details = document.getElementById("details").textContent;
    console.log(details)

    // copy text
    navigator.clipboard.writeText(details)
    btn.textContent= 'copied'

    //***//
    navigator.clipboard.readText().then(clipText=>{
        console.log(clipText)
    })

    if (previous) {
        previous.textContent = 'click'
    }
    previous =btn

}))

// Sidebar starts

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}

// Sidebar ends

// Topbar starts

function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
// Topbar ends