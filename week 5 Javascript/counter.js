function hello(){
    alert("Hello World");
}

if (!localStorage.getItem('counter')){ // checks local storage for a varaible, and if it doesn't exist, initialize it to 0
    localStorage.setItem('counter', 0);
} 

let counter = localStorage.getItem('counter'); // sets the js variable to the value found in the local storage

function count(){
    counter++;
    if (counter % 10 === 0){
        alert(`The counter is ${counter}`);
    }
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}

function swap(){
    const heading = document.querySelector('h1');
    if (heading.innerHTML === 'Hello!'){
        heading.innerHTML = 'Goodbye!'
    } else {
        heading.innerHTML = 'Hello!'
    }
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerHTML = counter; // when the page DOM is loaded the value is automatically set to the value of the counter
    document.querySelector('#but1').onclick = count;
    setInterval(count, 1000); // every 1000ms apply the count function
    document.querySelector('form').onsubmit = function(){
        const name = document.querySelector('#name').value;
        alert(`Hello ${name}`)
    }

});

let person = { // this is in the javascript object notation (.json)
    first: 'Harry',
    last: 'Potter'
}



