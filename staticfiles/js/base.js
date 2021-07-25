document.addEventListener("DOMContentLoaded", function(){
    const nav_bar = document.querySelector(".nav_box_mobile")
    const close_btn = document.querySelector("#close-btn")
    close_btn.onclick = () => {
        nav_bar.style.display = "none"
    } 
    const show_btn = document.querySelector("#bar-icon")
    show_btn.onclick = () => {
        nav_bar.style.display = "block"
    } 
});