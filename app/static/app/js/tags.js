let etiquetas = document.getElementById('etiquetas');
const btn_submit = document.getElementById('btn-submit');
const form_etiqueta = document.getElementById('form-etiqueta');
const nombre_etiqueta = document.getElementById('nombreEtiqueta');
let select = -1;
let form;

function editar(id) {
    if (btn_submit.textContent == "Crear") {
        btn_submit.textContent = "Actualizar";
        btn_submit.classList.remove("btn-primary");
        btn_submit.classList.add("btn-warning");
        select = id;
        let lista_etiquetas = document.querySelectorAll('.etiqueta');
        for (let i = 0; i < lista_etiquetas.length; i++) {
            if (lista_etiquetas[i].getAttribute('data-id') == id) {
                nombre_etiqueta.value = lista_etiquetas[i].getAttribute('data-nombre');
                break;
            }
        }
    }
    else {
        btn_submit.textContent = "Crear";
        btn_submit.classList.remove("btn-warning");
        btn_submit.classList.add("btn-primary");
    }
}

function enviar() {
    form = new FormData(form_etiqueta);
    if (btn_submit.textContent == "Crear") {
        fetch("list", {
            method: 'POST',
            headers: {
                "X-CSRFToken": csrftoken,
            },
            body: form,
        }).
            then(response => response.json()).
            then(data => {
                if (data["errors"]) {
                    alert("Error al crear etiqueta");
                    console.log(data["errors"]);
                }
                else{
                    console.log(data["message"]);
                    window.location.href = "/tasks/tags/list";
                }
            }).catch(error => {
                alert("Error al crear etiqueta");
                console.log(error);
            });
    }
    else {
        fetch("select/" + select, {
            method: 'POST',
            headers: {
                "X-CSRFToken": csrftoken,
            },
            body: form,
        }).
            then(response => response.json()).
            then(data => {
                if (data["errors"]) {
                    alert("Error al crear etiqueta");
                    console.log(data["errors"]);
                }
                else{
                    console.log(data["message"]);
                    window.location.href = "/tasks/tags/list";
                }
            }).catch(error => {
                alert("Error al crear etiqueta");
                console.log(error);
            });
    }
}

function crearEtiqueta(data) {
    let tag = document.createElement('div');
    tag.classList.add("etiqueta");
    tag.classList.add("mb-2");
    tag.setAttribute("data-id", data.id);
    tag.setAttribute("data-nombre", data.nombre);
    tag.innerHTML = `
        ${data.nombre}
        <button onclick="eliminar(${data.id})" class="btn btn-danger btn-sm ml-2 eliminar">Eliminar</button>
        <button onclick="editar(${data.id})" class="btn btn-secondary btn-sm editar">Editar</button>`;
    etiquetas.appendChild(tag);
}

function actualizarEtiqueta(data) {
    let lista_etiquetas = document.querySelectorAll('.etiqueta');
    for (let i = 0; i < lista_etiquetas.length; i++) {
        if (lista_etiquetas[i].getAttribute('data-id') == data.id) {
            lista_etiquetas[i].setAttribute('data-nombre', data.nombre);
            lista_etiquetas[i].innerHTML = `
            ${data.nombre}
            <button onclick="eliminar(${data.id})" class="btn btn-danger btn-sm ml-2 eliminar">Eliminar</button>
            <button onclick="editar(${data.id})" class="btn btn-secondary btn-sm editar">Editar</button>`;
            break;
        }
    }
    btn_submit.textContent = "Crear";
    btn_submit.classList.remove("btn-warning");
    btn_submit.classList.add("btn-primary");
    nombre_etiqueta.value = "";
}

function eliminar(id) {
    fetch("select/" + id, {
        method: 'DELETE',
        headers: {
            "X-CSRFToken": csrftoken,
        },
    }).
        then(response => response.json()).
        then(data => {
            eliminarTarea(id);
            console.log(data.message);
        }).catch(error => {
            alert("Error al eliminar la etiqueta");
            console.log(error);
        });
}

function eliminarTarea(id) {
    let lista_etiquetas = document.querySelectorAll('.etiqueta');
    for (let i = 0; i < lista_etiquetas.length; i++) {
        if (lista_etiquetas[i].getAttribute('data-id') == id) {
            lista_etiquetas[i].remove();
            break;
        }
    }
}