
    var one = document.getElementById("1")
    var two = document.getElementById("2")
    var three = document.getElementById("3")
    var four = document.getElementById("4")
    var five = document.getElementById("5")
    var el = document.querySelectorAll(".bi");
    one.addEventListener("click", (event) => {
     
        el.forEach(element => {
            element.classList.add("bi-star")
        })
        one.classList.remove("bi-star")


    } );
    two.addEventListener("click", (event) => {
        el.forEach(element => {
            element.classList.add("bi-star")
        })
        one.classList.remove("bi-star")
        two.classList.remove("bi-star")
     } );
     three.addEventListener("click", (event) => {
        el.forEach(element => {
            element.classList.add("bi-star")
        })
        one.classList.remove("bi-star")
        two.classList.remove("bi-star")
        three.classList.remove("bi-star")
        
     } );
     four.addEventListener("click", (event) => {
        el.forEach(element => {
            element.classList.add("bi-star")
        })
        one.classList.remove("bi-star")
        two.classList.remove("bi-star")
        three.classList.remove("bi-star")
        four.classList.remove("bi-star")
     } );
     five.addEventListener("click", (event) => {
        el.forEach(element => {
            element.classList.add("bi-star")
        })
        one.classList.remove("bi-star")
        two.classList.remove("bi-star")
        three.classList.remove("bi-star")
        four.classList.remove("bi-star") 
        five.classList.remove("bi-star") 
     } );
    
