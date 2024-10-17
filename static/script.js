let type= new Typed('#changing-text',{
    strings:['programmer','nature lover','foodaholic','cinephile'],
    typeSpeed:30,
    backSpeed:30,
    loop:true,
});

const slides= document.querySelectorAll(".slide")
var counter=0;


document.addEventListener('DOMContentLoaded', function () {

    function updateClock() {
        var now = new Date();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        var seconds = now.getSeconds();

        var isDayTime = hours >= 6 && hours < 18;

        var sunOrMoon = isDayTime ? '☀️' : '🌙';

   
        var ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; 

        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;

        var timeElement = document.getElementById('time');
        timeElement.textContent = sunOrMoon + ' ' + hours + ':' + minutes + ':' + seconds + ' ' + ampm;
    }

    function updateDate() {
        var now = new Date();
        var dateElement = document.getElementById('date');
        var options = { weekday: 'long', year: 'numeric', month: 'numeric', day: 'numeric' };
        dateElement.textContent = 'Today is ' + now.toLocaleDateString('en-US', options);
    }

    setInterval(updateClock, 1000);

    updateClock();
    updateDate();
    setInterval(updateDate, 30000); 


});



document.addEventListener("DOMContentLoaded", function () {
    var scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition !== null) {
        window.scrollTo(0, scrollPosition);
        sessionStorage.removeItem('scrollPosition');
    }
});

function saveScrollPosition() {
    sessionStorage.setItem('scrollPosition', window.scrollY);
}
