class EasyHTTP { 
  
    async put(url, data) { 
   
  
     const response = await fetch(url, { 
       method: 'PUT', 
       headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken
    },
       body: JSON.stringify(data) 
     }); 
       
     const resData = await response.json(); 
   
     return resData; 
   } 
  }

function flip(button){
    const room = getRoom()
    const port = location.port
    const host = location.hostname
    const apiLink = `/api/${room}/${button.dataset.pin}/`

    const flag = button.dataset.pinstatus.toLowerCase()=='true' ? false:true;
    
    console.log(button.dataset.pinstatus);

    const http  = new EasyHTTP()
    const a = http.put(apiLink, {
    "status": flag
    })

}



// async function getPinsValue(){
//     const room = getRoom()
//     const port = location.port
//     const host = location.hostname
//     const apiLink = `/api/${room}/`
//     response    = await fetch(apiLink)//.then(res => res.json()).then(json => console.log(json));
//     api         = response.json()
    
//     return api
// }