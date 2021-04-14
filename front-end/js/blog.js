var slideIndex4 = 1;
showSlides4(slideIndex4);

function plusSlides4(n) {
    event.preventDefault()
  showSlides4(slideIndex4 += n);
}

function currentSlide4(n) {
  showSlides4(slideIndex4 = n);
}

function showSlides4(n) {
  var i;
  var slides4 = document.getElementsByClassName("mySlides4");
  if (n > slides4.length ) {slideIndex4 = 1}    
  if (n < 1) {slideIndex4 = slides4.length}
  for (i = 0; i < slides4.length; i++) {
      slides4[i].style.display = "none";  
  }
  slides4[slideIndex4-1].style.display = "block";  

}

var slideIndex5 = 1;
showSlides5(slideIndex5);

function plusSlides5(n) {
    event.preventDefault()
  showSlides5(slideIndex5 += n);
}

function currentSlide5(n) {
  showSlides5(slideIndex5 = n);
}

function showSlides5(n) {
  var i;
  var slides5 = document.getElementsByClassName("mySlides5");
  if (n > slides5.length ) {slideIndex5 = 1}    
  if (n < 1) {slideIndex5 = slides5.length}
  for (i = 0; i < slides5.length; i++) {
      slides5[i].style.display = "none";  
  }
  slides5[slideIndex5-1].style.display = "block";  

}

let modalsref=document.querySelectorAll("#open_modal");
modalsref.forEach(function(ref){
    ref.onclick = function(){
        event.preventDefault()
        let modal = ref.getAttribute("data-modal");
        document.getElementById(modal).setAttribute("style","opacity: 1; display: block;");
    }
});

 //Baglanma icon teyin edilsin
 let closeref = document.querySelectorAll("#modal_close");
 closeref.forEach(function(ref){
     ref.onclick = function(){
         // Works_modal classli parent tap ve style teyin et 
         let modal  = (ref.closest(".works_modal").setAttribute("style","opacity: 0; visibility: hidden;"));
     }
 });


function myfun() {
  window.open('https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fmyour.bslthemes.com%2F2020%2F06%2F17%2Finspiring-design-trends-this-fall-2019%2F', 'facebook', 'width=600px height=900px');
}

function myfun2() {
  window.open('https://twitter.com/intent/tweet?text=%20https%3A%2F%2Fmyour.bslthemes.com%2F2020%2F06%2F17%2Finspiring-design-trends-this-fall-2019%2F', 'twitter', 'width=500px height=500px');
}

function myfun3() {
  window.open('http://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fmyour.bslthemes.com%2F2020%2F06%2F17%2Finspiring-design-trends-this-fall-2019%2F&amp;title=Inspiring%20design%20trends%20this%20fall%202019', 'linkedin', 'width=500px height=500px');
}

function myfun4() {
  window.open('http://www.reddit.com/submit?url=https%3A%2F%2Fmyour.bslthemes.com%2F2020%2F06%2F17%2Finspiring-design-trends-this-fall-2019%2F&amp;title=Inspiring%20design%20trends%20this%20fall%202019', 'reddit', 'width=500px height=500px');
}

function myfun5() {
  window.open('http://pinterest.com/pin/create/button/?url=https%3A%2F%2Fmyour.bslthemes.com%2F2020%2F06%2F17%2Finspiring-design-trends-this-fall-2019%2F', 'pinterest', 'width=500px height=500px');
}