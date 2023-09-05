class GetIncedent{
    constructor() {

    }
    redirectToList() {
        window.location.assign("http://127.0.0.1:5000/incedentlist");
    }
    redirectToAdd() {
        window.location.assign("http://127.0.0.1:5000/addincedentdash");
    }
    redirectToHome() {
        window.location.assign("http://127.0.0.1:5000/");
    }
    takeIncedentData(){
        const url = 'http://127.0.0.1:5000/getlist';
        fetch(url , {
            method :'GET',
            headers :{
                'Content-Type':'application/json',
                'Access-Control-Allow-Origin':'*'
            }
        }).then(res =>{
            return res.json()

        })
    }
    getBase64Data(){
        let file = document.querySelector(
            'input[type=file]')['files'][0];
        let reader = new FileReader();
        console.log("next");
        reader.onload = function () {
            let base64String = reader.result.replace("data:", "")
                .replace(/^.+,/, "");
            let imageBase64Stringsep = base64String;
            return  base64String;
        }
        reader.readAsDataURL(file);
    }
}