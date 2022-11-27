// Nuevo T
if(document.forms[0]){
    const element = document.querySelector('form');
    element.addEventListener('submit', event => {
    event.preventDefault();
    
        var codigo_curso = document.getElementById("codigo_curso").value;
        var nombre_tarea = document.getElementById("nombre_tarea").value;
        var descripcion = document.getElementById("descripcion").value;
        var fecha_inicio = String(document.getElementById("fecha_inicio").value);
        var fecha_limite = String(document.getElementById("fecha_limite").value);
    
        var data = {
            codigo_curso : codigo_curso,
            nombre_tarea : nombre_tarea,
            descripcion : descripcion,
            fecha_inicio : fecha_inicio,
            fecha_limite : fecha_limite
        }  
    
        fetch('https://w4n2zcmkfh.execute-api.us-east-1.amazonaws.com/prod/t/crear',{
            method : "POST",
            body: JSON.stringify(data)
        })
        .then(function(response) {
            if(response.ok) {
                location.href ="index.html";
                
            } else {
                throw "Error al grabar";
            }
        
        })
        .catch(err => {
            console.log(err);
        })
    });
    }