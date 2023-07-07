

window.onload = insertDateTime;


function insertDateTime() {
  now = new Date();
  DateTime = now.toLocaleString();
  document.getElementById('output').innerHTML = DateTime


}






