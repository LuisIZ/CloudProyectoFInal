var solicitar_lista_EC=  (event) => {
        fetch('https://4glinllb9b.execute-api.us-east-1.amazonaws.com/prod/ec/listar')
        .then(r => r.json())
        .then(json => {
            var participaciones = json.participaciones

            var table = document.getElementById("table_body");

            var c = 0;
            for (let index = 0; index < participaciones.length; index++) {

                c++;

                var row = table.insertRow(-1);


                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                var cell3 = row.insertCell(2);
                var cell4 = row.insertCell(3);
                var cell5 = row.insertCell(4);
                var cell6 = row.insertCell(5);
    

                cell1.innerHTML = c;
                cell2.innerHTML = participaciones[index].codigo_curso;
                cell3.innerHTML = participaciones[index].codigo_alumno;
                cell4.innerHTML = participaciones[index].puntaje_total;  
                cell5.innerHTML = participaciones[index].ultimo_puntaje;
                cell6.innerHTML = participaciones[index].fecha_ultimo_puntaje;           
                
            }


        })
        .catch(err => {
            console.log(err);
        })  
};

if(document.forms[0]){
    const element = document.querySelector('form');
    element.addEventListener('submit', event => {
    event.preventDefault();


        var codigo_curso = document.getElementById("codigo_curso").value;
        var codigo_alumno = document.getElementById("codigo_alumno").value;
        var puntaje_total = document.getElementById("puntaje_total").value;
        var ultimo_puntaje = document.getElementById("ultimo_puntaje").value;
        var fecha_ultimo_puntaje = document.getElementById("fecha_ultimo_puntaje").value;

        var data = {
            codigo_curso : codigo_curso,
            codigo_alumno : codigo_alumno,
            puntaje_total : puntaje_total,
            ultimo_puntaje : ultimo_puntaje,
            fecha_ultimo_puntaje : fecha_ultimo_puntaje
        }  

        fetch('https://4glinllb9b.execute-api.us-east-1.amazonaws.com/prod/ec/crear',{
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


var solicitar_lista_T=  (event) => {
    fetch('https://us4r0cpd46.execute-api.us-east-1.amazonaws.com/prod/t/listar')
    .then(r => r.json())
    .then(json => {
        var tarea = json.tarea

        var table = document.getElementById("table_body");

        var c = 0;
        for (let index = 0; index < tarea.length; index++) {

            c++;

            var row = table.insertRow(-1);


            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            var cell4 = row.insertCell(3);
            var cell5 = row.insertCell(4);
            var cell6 = row.insertCell(5);


            cell1.innerHTML = c;
            cell2.innerHTML = tarea[index].codigo_curso;
            cell3.innerHTML = tarea[index].nombre_tarea;
            cell4.innerHTML = tarea[index].descripcion;  
            cell5.innerHTML = tarea[index].fecha_inicio;
            cell6.innerHTML = tarea[index].fecha_limite;           
            
        }


    })
    .catch(err => {
        console.log(err);
    })  
};

if(document.forms[0]){
const element = document.querySelector('form');
element.addEventListener('submit', event => {
event.preventDefault();


    var codigo_curso = document.getElementById("codigo_curso").value;
    var nombre_tarea = document.getElementById("nombre_tarea").value;
    var descripcion = document.getElementById("descripcion").value;
    var fecha_inicio = document.getElementById("fecha_inicio").value;
    var fecha_limite = document.getElementById("fecha_limite").value;

    var data = {
        codigo_curso : codigo_curso,
        nombre_tarea : nombre_tarea,
        descripcion : descripcion,
        fecha_inicio : fecha_inicio,
        fecha_limite : fecha_limite
    }  

    fetch('https://us4r0cpd46.execute-api.us-east-1.amazonaws.com/prod/t/crear',{
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
