function crearTarea(data) {
    titulo.value = "";
    descripcion.value = "";
    let tarea = document.createElement('div');
    tarea.setAttribute("data-id", data.id);
    tarea.setAttribute("data-titulo", data.titulo);
    tarea.setAttribute("data-descripcion", data.descripcion);
    tarea.setAttribute("data-due-date", data.vence);
    tarea.setAttribute("data-priority", data.prioridad);
    tarea.setAttribute("data-completed", data.estado);
    tarea.classList.add("list-group-item");
    let clases = "";
    if (data.estado)
        clases = "fas fa-check-circle completed";
    else
        clases = "far fa-circle no-completed";

    tarea.innerHTML = `
    <h5 class="mb-1 title-list inline">${data.titulo}</h5>
    <i class="${clases}"></i>
    <p class="mb-1">${data.descripcion}</p>
    <small class="text-muted">Prioridad: <b>${data.prioridad}</b> </small>
    <br>
    <small class="text-muted">Vence: <b>${data.vence}</b> </small>
    <button onclick="completar(${data.id})" class="btn btn-sm btn-success float-end complete-btn"><i class="fas fa-check-circle"></i></button>
    <button type="button" class="margen btn btn-sm btn-warning float-end edit-btn"><i class="fas fa-edit"></i></button>
    <button onclick="eliminar(${data.id})" class="btn btn-sm btn-danger float-end delete-btn"><i class="fas fa-trash-alt"></i></button>
    `;
    let grupo;
    if (data.is_public)
        grupo = taskList_public
    else
        grupo = taskList

    grupo.appendChild(tarea);
}

function actualizarTarea(data) {
    titulo.value = "";
    descripcion.value = "";
    let tarea;
    let taskItems = document.querySelectorAll('.list-group-item');
    for (let i = 0; i < taskItems.length; i++) {
        if (taskItems[i].getAttribute("data-id") == data.id) {
            tarea = taskItems[i];
            break;
        }
    }
    tarea.setAttribute("data-titulo", data.titulo);
    tarea.setAttribute("data-descripcion", data.descripcion);
    tarea.setAttribute("data-priority", data.prioridad);
    tarea.setAttribute("data-due-date", data.vence);
    let clases = "";
    if (data.estado)
        clases = "fas fa-check-circle completed";
    else
        clases = "far fa-circle no-completed";

    tarea.innerHTML = `
            <h5 class="mb-1 title-list inline">${data.titulo}</h5>
            <i class="${clases}"></i>
            <p class="mb-1">${data.descripcion}</p>
            <small class="text-muted">Prioridad: <b>${data.prioridad}</b> </small>
            <br>
            <small class="text-muted">Vence: <b>${data.vence}</b> </small>
            <button onclick="completar(${data.id})" class="btn btn-sm btn-success float-end complete-btn"><i class="fas fa-check-circle"></i></button>
            <button type="button" class="margen btn btn-sm btn-warning float-end edit-btn"><i class="fas fa-edit"></i></button>
            <button onclick="eliminar(${data.id})" class="btn btn-sm btn-danger float-end delete-btn"><i class="fas fa-trash-alt"></i></button>
            `;
}

function eliminarTarea(id) {
    let taskItems = document.querySelectorAll('.list-group-item');
    for (let i = 0; i < taskItems.length; i++) {
        if (taskItems[i].getAttribute("data-id") == id) {
            taskItems[i].remove();
            break;
        }
    }
}