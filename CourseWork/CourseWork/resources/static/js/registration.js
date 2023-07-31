let login;
let password;
let firstName;
let lastName;
let phoneNumber;
let isOwner;

function postRegistrationData(){
    login = document.getElementById('loginFieldForm').value;
    password = document.getElementById('passwordFieldForm').value;
    firstName = document.getElementById('firstNameFieldForm').value;
    lastName = document.getElementById('lastNameFieldForm').value;
    phoneNumber = document.getElementById('phoneNumberFieldForm').value;
    isOwner = document.getElementById('isOwner').value;
    console.log(login , password , firstName , lastName , phoneNumber , isOwner);
    const URL = 'http://127.0.0.1:5000/registrationUser'
    var data = {
        'login' : login,
        'password' : password,
        'firstName' : firstName,
        'lastName' : lastName, 
        'phoneNumber' : phoneNumber,
        'isOwner' : isOwner
    }
    fetch(URL , {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        },
        body: JSON.stringify(data)
    })
    .then(function(response){
        console.log(response.status);
        if(response.status === 200){
            console.log(response.json());
        }
        else {
            throw new Error('Response is not ok');
        }
    })
}
