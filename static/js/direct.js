btn = document.querySelectorAll('table button')
truebtn = []
falsebtn = []
for(let i=0; i<btn.length; i++){
    if(btn[i].innerText == 'Dolu'){
        falsebtn.push(btn[i])
        btn[i].style.backgroundColor = 'red'
        btn[i].disabled = true
        btn[i].style.color = 'black'
    }
    else{
        truebtn.push(btn[i])
        btn[i].style.backgroundColor = '#4CAF50'
    }
}

buttons = document.querySelectorAll('table button')
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
for(let i=0; i<buttons.length; i++){
    buttons[i].addEventListener('click', function(){
        if(i<7){
            saat=21
        }
        else if(i>=7 && i<14){
            saat=22
        }
        else if(i>=14 && i<21){
            saat=23
        }
        else{
            saat=24
        }
        document.getElementById('day').value = days[i%7]
        document.getElementById('hour').value = saat
    })
}