function AddHouse() {
   alert("House added!");

}

function AddLocation() {
  alert("Location Added")
}

function UpdateHouse() {
  r = confirm("Are you sure you want to update {{ house }}?");
  
  if (r == true) {
    alert(" Updated ");
    } else {
        alert("Not updated");
      }
  
}
