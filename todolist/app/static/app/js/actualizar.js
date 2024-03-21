function actualizar(event) {
    if (event.target.parentElement.classList.contains('edit-btn') || event.target.classList.contains('edit-btn')) {
        let btn_cambiante = document.querySelector("#btn-cambiante");
        let titulo_menu = document.querySelector("#titulo-menu");
        if (btn_cambiante.textContent == "Actualizar") {
            btn_cambiante.textContent = "Agregar";
            btn_cambiante.classList.remove("btn-warning");
            btn_cambiante.classList.add("btn-primary");
            titulo_menu.textContent = "Agregar Tarea";
        }
        else {
            btn_cambiante.textContent = "Actualizar";
            btn_cambiante.classList.remove("btn-primary");
            btn_cambiante.classList.add("btn-warning");
            titulo_menu.textContent = "Actualizar Tarea";
            if (event.target.parentElement.classList.contains('edit-btn'))
                select = event.target.parentElement.parentElement.getAttribute("data-id");
            if (event.target.classList.contains('edit-btn'))
                select = event.target.parentElement.getAttribute("data-id");

            console.log(select);
        }
    }
}

taskList.addEventListener('click', actualizar);
taskList_public.addEventListener('click', actualizar);