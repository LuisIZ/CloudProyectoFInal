// Nuevo EC
if(document.forms[0]){
    const element = document.querySelector('form');
    element.addEventListener('submit', event => {
    event.preventDefault();


        var codigo_curso = document.getElementById("codigo_curso").value;
        var codigo_alumno = document.getElementById("codigo_alumno").value;
        var puntaje_total = document.getElementById("puntaje_total").value;
        var ultimo_puntaje = document.getElementById("ultimo_puntaje").value;
        var fecha_ultimo_puntaje = String(document.getElementById("fecha_ultimo_puntaje").value);

        var data = {
            codigo_curso : codigo_curso,
            codigo_alumno : codigo_alumno,
            puntaje_total : puntaje_total,
            ultimo_puntaje : ultimo_puntaje,
            fecha_ultimo_puntaje : fecha_ultimo_puntaje
        }  

        fetch('https://w4n2zcmkfh.execute-api.us-east-1.amazonaws.com/prod/ec/crear',{
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