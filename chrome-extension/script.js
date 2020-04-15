var url = "https://newtab.click";

function redirect() {
    document.location.href = url;
}
redirect();

document.addEventListener('DOMContentLoaded', function() {
   /*if the 1st redirect fails, try again or failover to link*/
   redirect();
   setTimeout(function(){ document.getElementById("notloaded").style.opacity = '0.8'; }, 300);
}, false);