let pos=0;

function slideShow(class1,class2,class3,px,btn,figur){
    let itemCount=figur;
    let containerWidth=document.querySelector('.'+class1).clientWidth;
    let items=document.querySelectorAll('.'+class2)

    for(let i=0;i<items.length;i++){
        items[i].style.width=containerWidth/itemCount +'px'
    }

    let sliderContainer=document.querySelector('.'+class3)
    sliderContainer.style.width=containerWidth/itemCount*items.length +'px';

    if(btn == 'prev'){
        if(pos>0){
            pos=-px
            sliderContainer.style.left=pos+'px';
        }else{
            sliderContainer.style.left=pos+'px';
            pos+=containerWidth/itemCount
        }
    }else{
        if(pos>-px){
            pos-=containerWidth/itemCount
            sliderContainer.style.left=pos+'px';
        }else{
            pos=0
            sliderContainer.style.left=pos+'px';
        }
    }
}

function Accordion(){
    event.preventDefault()
    for(let i=0;i<document.forms['userForm'].elements.length -1;i++){
        if(document.forms['userForm'].elements[0].value==""){
            document.forms['userForm'].elements[0].style.borderBottomColor="red"
            document.querySelector('.group-btn').nextElementSibling.className='form-output form-output-open'
        }
        if(document.forms['userForm'].elements[1].value==""){
            document.forms['userForm'].elements[1].style.borderBottomColor="red"
            document.querySelector('.group-btn').nextElementSibling.className='form-output form-output-open'
        }
        if(document.forms['userForm'].elements[2].value==""){
            document.forms['userForm'].elements[2].style.borderBottomColor="red"
            document.querySelector('.group-btn').nextElementSibling.className='form-output form-output-open'
        }
        else{
            document.forms['userForm'].elements[i].style.borderBottomColor="#585d65"
            document.querySelector('.group-btn').nextElementSibling.className='form-output close'
            document.querySelector('.form-output').nextElementSibling.className='contact-output open'
        }
    }
}

let slayt=document.getElementsByClassName("slayt")

let slaytSayisi=slayt.length

let slaytNo= 0;

slaytGoster(slaytNo)

function onceki(){

    slaytNo--

    slaytGoster(slaytNo)

}

function sonraki(){

    slaytNo++

    slaytGoster(slaytNo)
}

function slaytGoster(slaytNumarasi){

    slaytNo=slaytNumarasi;

    if(slaytNumarasi >=slaytSayisi){

        slaytNo= 0;
    }

    if(slaytNumarasi <0){

        slaytNo=slaytSayisi -1;
    }

    for(i= 0;i <slaytSayisi;i++){

        slayt[i].style.display= "none"
    }

    slayt[slaytNo].style.display= "block"
}

function Popup(){
    event.preventDefault()
    hdModal=document.querySelector('.hd-modal')
    hdModal.className=('hd-modal book-open')
}

function Close(){
    hdModal=document.querySelector('.hd-modal')
    hdModal.className='hd-modal modal-close'
}

function videoModal(){
    event.preventDefault()
    document.querySelector('.hd-modal').nextElementSibling.className='book-open book'
}

function videoClose(){
    let bookModal=document.querySelector('.book')
    bookModal.className='modal-close'
}


