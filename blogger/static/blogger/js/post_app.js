
let tags = document.querySelectorAll('.badge');

let colors = ['badge-primary',
'badge-secondary',
'badge-success',
'badge-danger',
'badge-warning',
'badge-info',
'badge-light',
'badge-dark'];

let i = 0;
for (let p of tags){
    p.classList.add(colors[i]);
    i+=1;
    if (i == 7){
        i = 0;
    }
}

let list = document.querySelectorAll('.list-group-item');

let list_colors = ['list-group-item-primary',
'list-group-item-secondary',
'list-group-item-success',
'list-group-item-danger',
'list-group-item-warning',
'list-group-item-info',
'list-group-item-light',
'list-group-item-dark'];

let j = 0;
for (let l of list){
    l.classList.add(list_colors[j]);
    j+=1;
    if (j == 7){
        j = 0;
    }
}

// function ocultar(){
//     document.querySelector('.busqueda').classList.toggle('ocultar');
// }

// document.querySelector('.fa-search').onclick = ()=>{
//     ocultar();
// }

let search = document.querySelector('.fa-search');
search.addEventListener('click', ()=>{
    document.querySelector('.busqueda').classList.toggle('ocultar');
})