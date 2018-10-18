
document.getElementById('button').addEventListener("click", main)

// calcDenom(a){
//   num = 2*a;
//   return num;
// }

function calcDisc(a, b, c){
  var  num = eval((-b*-b) -4*a*c);
  return num;
}
function main(){
  var aValue = document.getElementById('a-Input').value;
  var bValue = document.getElementById('b-Input').value;
  var cValue = document.getElementById('c-Input').value;
  //alert(aValue + bValue + cValue);
  var discriminant, denom;

  discriminant = calcDisc(aValue, bValue, cValue);
  alert("n"+discriminant);
  // denom = calcDenom(aValue);
  // alert("d"+denom);
}
