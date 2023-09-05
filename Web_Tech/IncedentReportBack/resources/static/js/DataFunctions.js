let redirectToAdd = document.getElementById("redirect-to-add")
redirectToAdd.onclick = function (){
    getIncedent.redirectToAdd()
}
let takeIncedentData = document.getElementById("take-incedent-data")
takeIncedentData.onclick = function (){
    let data = getIncedent.takeIncedentData()
    console.log(data)
}
photo = document.getElementById('Photo');
photo.onchange = function (){
    getIncedent.getBase64Data();
}