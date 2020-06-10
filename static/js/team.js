function searchstdn(){
    x = document.getElementById('search').value
    if(x===""){
        document.getElementById('searchlist').style.display = 'none'
    }
    else{
        $.ajax({
            url: `http://localhost:8000/api/stadion/?search=${x}`,
            method: 'GET',
            success: function(result){
                console.log(result)
                for(let i=0; i<5; i++){
                    y = document.createElement('li')
                    z = document.createElement('a')
                    id = result[i].id
                    // link = `{% url 'stadion:detail' ${id} %}`
                    link = `http://localhost:8000/stadion/detail/id=${id}`
                    z.setAttribute('href', link)
                    z.innerHTML = result[i].name
                    y.appendChild(z)
                    document.querySelector('#searchlist ul').appendChild(y)
                }
            },
            error: function(result){
                console.log(error)
                console.log(result)
            }
        })
    }
}