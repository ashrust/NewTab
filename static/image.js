function showBackground(){
  console.log('showing background');
  elem = document.getElementById("bg");
  elem.style.opacity='1';
  elem.style.marginTop ='0px';
}
window.addEventListener("load", showBackground);