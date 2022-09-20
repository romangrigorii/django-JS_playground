// document.addEventListener("DOMContentLoaded", function() {
//     document.querySelector('#red').onclick = function(){
//         document.querySelector('#hello').style.color = 'red';
//     }
//     document.querySelector('#blue').onclick = function() {
//         document.querySelector('#hello').style.color = 'blue';
//     }
//     document.querySelector('#green').onclick = function(){
//         document.querySelector('#hello').style.color = 'green';
//     }
// })

document.addEventListener("DOMContentLoaded", function() {
    
    //// reference 1
    // document.querySelector('#red').onclick = function(){
    //     document.querySelector('#hello').style.color = 'red';
    // }
    // document.querySelector('#blue').onclick = function(){
    //     document.querySelector('#hello').style.color = 'blue';
    // }
    // document.querySelector('#green').onclick = function(){
    //     document.querySelector('#hello').style.color = 'green';
    // }

    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {
            document.querySelector('#hello').style.color = button.dataset.color;
        }
    });

    document.querySelector('select').onchange = function() {
            document.querySelector('#hello').style.color = this.value;
        }
});
