const container = document.getElementById('container');
const signInBtn = document.getElementById('sign-in');
const signUpBtn = document.getElementById('sign-up');

signUpBtn.addEventListener('click', () => {
    container.classList.add("active");
});

signInBtn.addEventListener('click', () => {
    container.classList.remove("active");
    window.location.href = 'index.html';
});
