document.addEventListener("DOMContentLoaded", function () {
    let asignadasSelect = document.getElementById("etiquetas-asignadas");
    let disponiblesSelect = document.getElementById("etiquetas-disponibles");

    asignadasSelect.addEventListener("change", function () {
        let select = getSelectedOptionValue(asignadasSelect);
        fetch("select/" + task_id + "/" + select, {
            method: 'DELETE',
            headers: {
                "X-CSRFToken": csrftoken,
            },
        }).
            then(response => response.json()).
            then(data => {
                console.log(data.message);
                moveSelectedOptions(asignadasSelect, disponiblesSelect);
            }).catch(error => {
                alert("Error al asignar etiqueta a tarea");
                console.log(error);
            });
    });

    disponiblesSelect.addEventListener("change", function () {
        let select = getSelectedOptionValue(disponiblesSelect);
        fetch("select/" + task_id + "/" + select, {
            method: 'GET',
            headers: {
                "X-CSRFToken": csrftoken,
            },
        }).
            then(response => response.json()).
            then(data => {
                console.log(data.message);
                moveSelectedOptions(disponiblesSelect, asignadasSelect);
            }).catch(error => {
                alert("Error al asignar etiqueta a tarea");
                console.log(error);
            });
    });
});

function moveSelectedOptions(sourceSelect, targetSelect) {
    let selectedOptions = sourceSelect.selectedOptions;
    for (let i = 0; i < selectedOptions.length; i++) {
        let option = selectedOptions[i];
        targetSelect.appendChild(option);
    }
}

function getSelectedOptionValue(selectElement) {
    var selectedOption = selectElement.selectedOptions[0];
    return selectedOption ? selectedOption.value : null;
}