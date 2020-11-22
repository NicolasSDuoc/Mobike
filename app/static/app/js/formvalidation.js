  $(document).ready(function() {

    $.validator.addMethod("RUT", function(value, element) {
        return this.optional(element) || /^\d{1,2}\.?\d{3}\.?\d{3}-?(k|\d)$/i.test(value);
    }, "Favor ingrese un rut valido");


    $("#registro").validate({
        rules:{
            username : {
                required: true,
                RUT: "required RUT"
            },
            first_name : {
                required: true,
                maxlength: 50
            },
            last_name : {
                required: true,
                maxlength: 50
            },
            email : {
                required: true,
                maxlength: 50,
                email: true
            },
            phone : {
                maxlength: 9,
                number: true
            }
        },
        messages:{
            username : {
                required: "El rut no puede estar en blanco",
                RUT: "favor ingrese un rut valido"
            },
            first_name : {
                required: "El nombre no puede estar en blanco",
                maxlength: "Maximo 50 caracteres"
            },
            last_name : {
                required: "El apellido no puede estar en blanco",
                maxlength: "Maximo 50 caracteres"
            },
            phone : {
                maxlength: "Maximo 9 digitos",
                number: "solo se permiten numeros"
            },
            email : {
                required: "El email no puede estar en blanco",
                maxlength: "Maximo 50 caracteres",
                email: "Email invalido"
            }
        },
        submitHandler: function(form) {
            form.submit();
          }
    }
    );
  });