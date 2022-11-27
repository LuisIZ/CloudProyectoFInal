window.idioma_actual = 'es';

// Listar Evaluacion Continua
var solicitar_lista_EC=  (event) => {
        fetch('https://w4n2zcmkfh.execute-api.us-east-1.amazonaws.com/prod/ec/listar')
        .then(r => r.json())
        .then(json => {
            var participaciones = json.participaciones

            var table = document.getElementById("table_body_ec");

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

// Listar Tareas
var solicitar_lista_T = (event) => {
    fetch('https://w4n2zcmkfh.execute-api.us-east-1.amazonaws.com/prod/t/listar')
    .then(r => r.json())
    .then(json => {
        var idioma = document.getElementById("idiomas");
        var idioma_destino = ""
        for (var i = 0; i < idioma.childElementCount; i++) {
            if (idioma[i].selected) {
                idioma_destino = idioma[i].value;
                }
            }
        
        var tarea = json.tarea
        var table = document.getElementById("table_body_t");

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
            cell4.innerHTML = tarea[index].descripcion
            cell5.innerHTML = tarea[index].fecha_inicio;
            cell6.innerHTML = tarea[index].fecha_limite;
        }
    })
    .catch(err => {
        console.log(err);
    })  
};