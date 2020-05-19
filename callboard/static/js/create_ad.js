let button = document.querySelector('button.btn.btn-primary');
    let form = document.querySelector('form');
    button.addEventListener('click', function(e){
        e.preventDefault();
        alert('asd');
        form.submit()
    })