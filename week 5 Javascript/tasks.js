document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length >0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }        
    }

    document.querySelector('form').onsubmit = () => {
        
        const task = document.querySelector('#task').value;
        console.log(task);
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#tasks').append(li); // adds the entry of the input field to the list in submit
        document.querySelector('#task').value = ''; // clears our the input field
        document.querySelector('#submit').disabled = true;
        return false; // stops the form from submitting.

    }
})