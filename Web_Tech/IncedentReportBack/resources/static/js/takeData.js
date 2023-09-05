function takeIncedentData(){
    const url = 'http://127.0.0.1:5000/getlist';
    fetch(url , {
        method :'GET',
        headers :{
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        }
    }).then(res =>{
        return res.json()
    }).then(data =>{
            addIncedentToDiv(data.data)
        })

}

function addIncedentToDiv(data){
    console.log(data);
    let mainElement = document.getElementById('table-place');
    let table = document.createElement('table');
    let tablehead = document.createElement('thead');
    let headtr = document.createElement('tr');
    let headFirstName = document.createElement('td');
    headFirstName.innerHTML = 'First name';
    headFirstName.style.marginLeft = '2em';
    let headLastName = document.createElement('td');
    headLastName.style.marginLeft = '2em';
    headLastName.innerHTML = 'Last name';
    let description = document.createElement('td');
    description.innerHTML = 'Description';
    description.style.marginLeft = '2em';
    let photo = document.createElement('td');
    photo.innerHTML = 'Photo';
    photo.style.marginLeft = '2em';
    let lanLat = document.createElement('td');
    lanLat.innerHTML = 'Lat / Lan';
    lanLat.style.marginLeft = '2em';
    headtr.appendChild(headFirstName);
    headtr.appendChild(headLastName);
    headtr.appendChild(description);
    headtr.appendChild(photo);
    headtr.appendChild(lanLat);
    tablehead.appendChild(headtr);
    table.appendChild(headtr);
    let tableBody = document.createElement('tbody');
    console.log(data[0].photo)
    for(let i = 0;i < data.length ;i++ ){
        console.log(data[i]);
        let elTr = document.createElement('tr');
        let elFirstNameTd = document.createElement('td')
        elFirstNameTd.innerHTML = data[i].fname;
        let elLastNameTd = document.createElement('td');
        elLastNameTd.innerHTML = data[i].lname;
        let elDescriptionTd = document.createElement('td');
        elDescriptionTd.innerHTML = data[i].description;
        let photoTd = document.createElement('td');
        let img = new Image();
        img.src = 'data:image/png;base64,' + data[i].photo;
        img.style.width = '100px';
        photoTd.appendChild(img);
        let lanLatTD = document.createElement('td');
        lanLatTD.innerHTML = data[i].lat + ' ' + data[i].lan;
        elTr.appendChild(elFirstNameTd);
        elTr.appendChild(elLastNameTd);
        elTr.appendChild(elDescriptionTd);
        elTr.appendChild(photoTd);
        elTr.appendChild(lanLatTD);
        tableBody.appendChild(elTr);
    };
    table.appendChild(tableBody);
    mainElement.appendChild(table)
}

