$(document).ready(function() {
    $("#contacto").validate({
        rules:{
            nombre : {
                required: true,
                maxlength: 50
            },
            apellido : {
                required: true,
                maxlength: 50
            },
            telef : {
                maxlength: 9,
                number: true
            },
            mail : {
                maxlength: 50
            }
        },
        messages:{
            nombre : {
                required: "El nombre no puede estar en blanco",
                maxlength: "Maximo 50 caracteres"
            },
            apellido : {
                required: "El apellido no puede estar en blanco",
                maxlength: "Maximo 50 caracteres"
            },
            telef : {
                maxlength: "Maximo 9 digitos",
                number: "solo se permiten numeros"
            },
            mail : {
                required: "El email no puede estar en blanco",
                maxlength: "Maximo 50 caracteres"
            }
        }
    }
    );
  });

function msg(){
    alert("xd");
}
