
// ---login-popup form----
function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }
  



// -----fill out and valid email--

document.getElementById('myForm').addEventListener('submit', function(event) {
    var inputs = this.querySelectorAll('input[required], textarea[required]');
    var valid = true;
    inputs.forEach(function(input) {
      if (!input.value.trim()) {
        valid = false;
        input.style.borderColor = 'red'; // Highlight empty fields
      } else {
        input.style.borderColor = '#ccc'; // Reset border color
      }
    });

    if (!valid) {
      event.preventDefault(); // Prevent form submission if any field is empty
      alert('Please fill out all required fields.');
    }
  });

  