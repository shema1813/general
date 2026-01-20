function validate(e){
    e.preventDefault();

    const email = document.getElementById('email').value
    const pass = document.getElementById('password').value
    const Age = document.getElementById('Age').value
    const msgbox = document.getElementById('message')

    let message = '';
    if (email === '') {
        message = 'please enter an email.';
        msgbox.style.color = 'red';
    } else  if (pass === '') {
        message = 'please enter a password.';
        msgbox.style.color = 'red';
    } else  if (Age === '') {
        message = 'please enter your Age.';
        msgbox.style.color = 'red';
    } else  {
        message = 'Login successful!';
        msgbox.style.color = 'green';
    }
    msgbox.innerHTML = message;
}

//run validate when login in clicked
document.getElementById("LoginForm").onsubmit = validate;

//real-time validate (like the screenshots)
document.getElementById("email").onsubmit = () => validate({ preventDefault: () => {}});
document.getElementById("password").onsubmit = () => validate({ preventDefault: () => {}});
document.getElementById("Age").onsubmit = () => validate({ preventDefault: () => {}});