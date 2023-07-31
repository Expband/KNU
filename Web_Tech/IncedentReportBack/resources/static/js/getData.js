photo = document.getElementById('Photo');
photo.onchange = function (){
    getBase64Data();   
}
function getBase64Data(){

    var file = document.querySelector(
        'input[type=file]')['files'][0];
    var reader = new FileReader();
    console.log("next");
    reader.onload = function () {
        base64String = reader.result.replace("data:", "")
            .replace(/^.+,/, "");
        imageBase64Stringsep = base64String;
        photo = base64String;
    }
    reader.readAsDataURL(file);
}


function postReuest(){
    fname = document.getElementById('fname').value;
    lname = document.getElementById('lname').value;
    description = document.getElementById('Description').value;
    lat = document.getElementById('lat').value;
    lan = document.getElementById('lan').value;

    const url = 'http://127.0.0.1:5000/postincedent';
    var data = {
        fname,
        lname,
        description,
        photo,
        lat,
        lan
    };
    console.log(data);
    fetch(url , {
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
