var expanded = false;

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
function show()
{
var elem=document.getElementById("print");
var element=document.getElementById('design');
elem.style.display= element.value=='print'? "block" : "none";
}
