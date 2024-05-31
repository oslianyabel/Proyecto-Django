function enviar() {
    form = new FormData(taskForm);
    if (btn_cambiante.textContent == "Actualizar")
        send_update();
    else
        send_create();
}

function send_update() {
    fetch("select/" + select, {
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
    }).
        then(response => response.json()).
        then(data => {
            if (data["errors"])
                alert("Campos incorrectos");
            else {
                console.log(data["message"]);
                window.location.href = "/tasks/list";
            }
        }).
        catch(error => {
            alert("Error al editar tarea");
            console.log(error);
        });
}

function send_create() {
    fetch("list", {
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
    }).
        then(response => response.json()).
        then(data => {
            if (data["errors"])
                alert("Campos incorrectos");
            else{
                console.log(data["message"]);
                window.location.href = "/tasks/list";
            }
        }).
        catch(error => {
            alert("Error al crear la tarea");
            console.log(error);
        });
}

function completar(id) {
    fetch("select/" + id, {
        method: 'GET',
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
    }).
        then(response => response.json()).
        then(data => {
            console.log(data["message"]);
            window.location.href = "/tasks/list";
        }).
        catch(error => {
            alert("Error al cambiar estado");
            console.log(error);
        });
}

function eliminar(id) {
    fetch("select/" + id, {
        method: 'DELETE',
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
    }).
        then(response => response.json()).
        then(data => {
            console.log(data["message"]);
            window.location.href = "/tasks/list";
        }).
        catch(error => {
            alert("Error al eliminiar tarea");
            console.log(error);
        });
}