// Define a function to be executed when Enviar button is clicked
function Enviar() {
    // Get the values of the input fields by their id
    var nome = document.getElementById("nomeid");
    var tel = document.getElementById("foneid");
    var email = document.getElementById("emailid");

    // Check if the value of tel field is not empty
    if (tel.value != "") {
        // Display an alert with the user inputs
        alert('Obrigado sr(a) ' + nome.value + ' os seus dados, Tel: ' + tel.value + ' e Email: '
            + email.value + ' foram encaminhados com sucesso');
    }
}

// Define a function to be executed when Trocar button is clicked
function Trocar() {
    // Get the values of the input fields by their id
    var nome = document.getElementById("nomeid");
    var email = document.getElementById("emailid");
    
    // Set the value of email field to the value of nome field
    email.value = nome.value;
}
