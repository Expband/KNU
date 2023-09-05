let loginFromField;
let passwordFromField;

function compareAuthorizationData(){
    loginFromField = document.getElementById('login').value;
    passwordFromField = document.getElementById('password').value;
    var data = {
        'login' : loginFromField, 
        'password' : passwordFromField
    }
    const URL = 'http://127.0.0.1:5000/postLogin'
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