let text = document.getElementById('about');
text.innerHTML = 'ABOUT';

add = (i) => {
    let val = document.getElementById('val');
    val.innerHTML = parseInt(val.innerHTML) + i;
};

sub = (i) => {
    let val = document.getElementById('val');
    val.innerHTML = parseInt(val.innerHTML) - i;
};