window.idioma_actual 

document.getElementById("boton-traducir").onclick = function() {
    const idioma = document.getElementById("idiomas");
    for (var i = 0; i < idioma.childElementCount; i++) {
        if (idioma[i].selected) {
            console.log(idioma[i].value);

            fetch('https://w4n2zcmkfh.execute-api.us-east-1.amazonaws.com/prod/t/traducir',{
                method : "POST",
                body: JSON.stringify({
                    'idioma_destino': idioma[i].value
                })
            })
            .then(function(response) {
                if(response.ok) {
                    console.log(response);
                    // location.href ="index.html";
                } else {
                    throw "Error al grabar";
                }
            })
            .catch(err => {
                console.log(err);
            })
        }
    }
}