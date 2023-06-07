// RESTAURENT SPECIAL PRODUCT SLIDING EFFECT
const procontainer=[...document.querySelectorAll('.pro-container')];
const prebtn=[...document.querySelectorAll('.pre-btn')];
const nxtbtn=[...document.querySelectorAll('.nxt-btn')];
procontainer.forEach((item,i)=>{
  let containerdimension =item.getBoundingClientRect();
  let containerwidth=containerdimension.width;
  nxtbtn[i].addEventListener('click',()=>{
    item.scrollLeft += containerwidth;
  })
  prebtn[i].addEventListener('click',()=>{
    item.scrollLeft -=containerwidth;
  })
})
// RESTAURENT SPECIAL PRODUCT SLIDING EFFECT

//REVIEW SLIDING EFFECT
document.addEventListener('DOMContentLoaded',function(){
  const slider1 = document.querySelector('.testimonial-slider');
  const sliderWrapper1 = slider1.querySelector('.slider-wrapper');
  const slides1 = slider1.querySelectorAll('.slide');
  const prevBtn = slider1.querySelector('.prev-btn');
  const nextBtn = slider1.querySelector('.next-btn');
  let slideIndex1 = 0;
  
  function showSlide(index) {
    slides1.forEach(slide1 => slide1.style.display = 'none');
    slides1[index].style.display = 'block';
  }
  
  function slideNext() {
    slideIndex1++;
    if (slideIndex1 >= slides1.length) {
      slideIndex1 = 0;
    }
    showSlide(slideIndex1);
  }
  
  function slidePrev() {
    slideIndex1--;
    if (slideIndex1 < 0) {
      slideIndex1 = slides1.length - 1;
    }
    showSlide(slideIndex1);
  }
  
  prevBtn.addEventListener('click', slidePrev);
  nextBtn.addEventListener('click', slideNext);
  
  showSlide(slideIndex1);//REVIEW SLIDING EFFECT
  
  
});
//REVIEW SLIDING EFFECT
//CART PAGE FUNCTIONS

//CART PAGE FUNCTIONS