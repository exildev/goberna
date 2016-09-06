$(document).ready(function() {
    $("#id_imagen").change(function() {
        validar($(this));
    });
});

function validar(imagen) {
    if (imagen.val() !== "") {
        if (imagen[0].files[0].size / 1024 > 1024) {
            alert("la image no puede pesar mas de 1 mega");
            imagen.val("");
        }
    }
}
