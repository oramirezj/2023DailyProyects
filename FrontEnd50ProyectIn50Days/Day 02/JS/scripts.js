/** Bring elements from the DOM ******/
const progress = document.getElementById('progress');
const prev = document.getElementById('prev');
const next = document.getElementById('next');
const circles = document.querySelectorAll('.circle');

/* Add event listeners to the buttons Next and Prev and add funtionality by using the DOM and chang values */
let currentActive =1;

next.addEventListener('click', () => {
    currentActive++;   //it give at variable currentActive on clic a +1 value
    if(currentActive>circles.length) {     //compare the value of currentActive if is mayor to total of circles stay on max value
        currentActive= circles.length;     //no mather how many clicks you make the max value will be the max of objets of circles 
    }

    update();  //calling a funtion to update values
})

prev.addEventListener('click', () => {
    currentActive--;   //it give at variable currentActive on clic a -1 value
    if(currentActive < 1) {     //compare the value of currentActive if is menor to 1
        currentActive = 1;     //if it is menor than 1 go back the value of 1 to the variable currentActive   
    }

    update();   //calling a funtion to update values
})

function update() {
    circles.forEach((circle, idx) => {
        if(idx < currentActive){                      //check if the circle index is menor than de value of currentActive variable
            circle.classList.add('active');            //if is menor, add the class active
        } else {
            circle.classList.remove('active');
        }
    })

    const actives = document.querySelectorAll('.active')     //bring from the DOM the value of total of actives classes

    progress.style.width = (actives.length - 1) / (circles.length - 1) * 100 + '%';    //add a value id element progress a style widht value 
    //on click you will have: (2-1)/(4-1)*100%= 1/3 * 100 = 33% on the next clic will have 66% and in the last 99%

    /**** enable and disable next and prev button depending on value of currentActive value ****/
    if(currentActive === 1){
        prev.disabled = true;
    } else if(currentActive === circles.length) {
        next.disabled = true;
    } else {
        prev.disabled = false;
        next.disabled = false;
    }
}