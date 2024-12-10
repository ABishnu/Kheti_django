const signUp = document.querySelector('.signup-link');
const formContent = document.querySelector('.form-content');
const prev = document.querySelector('.prev');
const passwordToggles = document.querySelectorAll('.ri-eye-off-line');


signUp.addEventListener('click',function(){
    formContent.classList.add('active')
})


prev.addEventListener('click',function(){
    formContent.classList.remove('active')
})


passwordToggles.forEach(function(toggle){
    toggle.addEventListener('click',function(){
        const passwordField = this.previousElementSibling;
        if(passwordField.type === 'password'){
            passwordField.type = 'text';
            this.classList.remove('ri-eye-off-line')
            this.classList.add('ri-eye-line');
        }else{
            passwordField.type = 'password';
            this.classList.remove('ri-eye-line')
            this.classList.add('ri-eye-off-line');
        }
    })
})