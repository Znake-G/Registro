
const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
    window.location.href = 'index1.html'
});

function registerr(){
    var email = document.getElementById("correo").value;
    var pass = document.getElementById("Pass").value;
    var name = document.getElementById("Name").value;
    if (email == "" || pass == "" || name == ""){
        alert("Faltan datos");
    }
    BuscarUserSinPass(name, email, pass);
}
function BuscajrUserSinPass(Name, email, pass){
    alert("Buscando usuario ");

    confir = False;
    alert("Buscando usuario ");
    /* Validar que el usuario este en la base de datos confir = True si se encuentra el usuario */
}

function Validar(){
    var email = document.getElementById("email").value;
    var pass = document.getElementById("Password").value;
    var gerente = document.getElementById("Gerente").checked;
    var supervisor = document.getElementById("Supervisor").checked;
    if (email == "" || pass == "" || (gerente == false && supervisor == false)){
        alert("Faltan datos");
    }
    if (gerente == true){
            //comprobarBD("Gerente",email,pass);
            alert("Validando Gerente");
            /*condicional : si se encuentra el usuario en la base de datos 
            * se REDIRIJE A LA PAGINA DEL Gerente*/
    }else{
            //comprobarBD("Supervisor",email,pass);
            alert("Validando Supervisor")
            /*condicional : si se encuentra el usuario en la base de datos 
            * se REDIRIJE A LA PAGINA DEL Supervisor*/
    }
}

function comprobarBD(Cargo, email, pass){
    confir = False;
    /* Validar que el usuario este en la base de datos confir = True si se encuentra el usuario */
}
