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
    console.log(button)
}

async function getPinsValue(){
    const room = getRoom()
    const port = location.port
    const host = location.hostname
    const apiLink = `/api/${room}/`
    console.log(apiLink)
    response    = fetch(apiLink).then(res => console.log(res);
    // api         = response.json()
    // console.log(api)
    
    return room
}