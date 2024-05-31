function actualizar(id) {
    if (btn_cambiante.textContent == "Crear") {
        btn_cambiante.textContent = "Actualizar";
        btn_cambiante.classList.remove("btn-primary");
        btn_cambiante.classList.add("btn-warning");
        select = id;
        let lista_tareas = document.querySelectorAll('.list-group-item');
        for (let i = 0; i < lista_tareas.length; i++) {
            if (lista_tareas[i].getAttribute('data-id') == id) {
                titulo.value = lista_tareas[i].getAttribute('data-titulo');
                descripcion.value = lista_tareas[i].getAttribute('data-descripcion');
                break;
            }
        }
    }
    else {
        btn_cambiante.textContent = "Crear";
        btn_cambiante.classList.remove("btn-warning");
        btn_cambiante.classList.add("btn-primary");
        titulo.value = "";
        descripcion.value = "";
    }
}