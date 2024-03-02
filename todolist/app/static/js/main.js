const btnLogout = document.querySelector('.btn-logout');
let cont = 0;
let select = -1;

btnLogout.addEventListener('click', function () {
    window.location.href = 'login.html';
});

const btnToggleDarkMode = document.querySelector('.btn-toggle-dark-mode');
const body = document.body;

btnToggleDarkMode.addEventListener('click', function () {
    body.classList.toggle('dark-mode');
    if (body.classList.contains('dark-mode')) {
        btnToggleDarkMode.classList.remove("btn-dark");
        btnToggleDarkMode.classList.add("btn-light");
        btnToggleDarkMode.innerHTML = '<i class="fas fa-sun"></i>';
    } else {
        btnToggleDarkMode.classList.remove("btn-light");
        btnToggleDarkMode.classList.add("btn-dark");
        btnToggleDarkMode.innerHTML = '<i class="fas fa-moon"></i>';
    }
});

const taskForm = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const filterSelect = document.getElementById('filterSelect');
const sortByDueDateBtn = document.getElementById('sortByDueDateBtn');
const sortByPriorityBtn = document.getElementById('sortByPriorityBtn');

taskForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const title = document.getElementById('titleInput').value;
    const description = document.getElementById('descriptionInput').value;
    const dueDate = document.getElementById('dueDateInput').value;
    const priority = document.getElementById('priorityInput').value;
    let btn_cambiante = document.querySelector("#btn-cambiante");
    let titulo_menu = document.querySelector("#titulo-menu");

    if (btn_cambiante.textContent == "Actualizar") {
        let taskItems = taskList.querySelectorAll('.list-group-item');
        for (let i = 0; i < taskItems.length; i++) {
            if (taskItems[i].getAttribute("data-id") == select) {
                taskItems[i].setAttribute("data-due-date", dueDate);
                taskItems[i].setAttribute("data-priority", priority);
                taskItems[i].innerHTML = `
                  <h5 class="mb-1 title-list inline">${title}</h5>
                  <div class="circulo"></div>
                  <p class="mb-1">${description}</p>
                  <small class="text-muted">Prioridad: <b>${priority}</b> </small>
                  <br>
                  <small class="text-muted">Vence: <b>${dueDate}</b> </small>
                  <button type="button" class="btn btn-sm btn-danger float-end delete-btn"><i class="fas fa-trash-alt"></i></button>
                  <button type="button" class="margen btn btn-sm btn-warning float-end edit-btn"><i class="fas fa-edit"></i></button>
                  <button type="button" class="btn btn-sm btn-success float-end complete-btn"><i class="fas fa-check-circle"></i>
                  </button>
                `;
                break;
            }
        }

        btn_cambiante.textContent = "Agregar";
        btn_cambiante.classList.remove("btn-warning");
        btn_cambiante.classList.add("btn-primary");
        titulo_menu.textContent = "Agregar Tarea";

    } else {
        const taskItem = `
        <div class="list-group-item" data-due-date="${dueDate}" data-priority="${priority}" data-id="${cont}">
          <h5 class="mb-1 title-list inline">${title}</h5>
          <div class="circulo"></div>
          <p class="mb-1">${description}</p>
          <small class="text-muted">Prioridad: <b>${priority}</b> </small>
          <br>
          <small class="text-muted">Vence: <b>${dueDate}</b> </small>
          <button type="button" class="btn btn-sm btn-danger float-end delete-btn"><i class="fas fa-trash-alt"></i></button>
          <button type="button" class="margen btn btn-sm btn-warning float-end edit-btn"><i class="fas fa-edit"></i></button>
          <button type="button" class="btn btn-sm btn-success float-end complete-btn"><i class="fas fa-check-circle"></i>
          </button>
        </div>
      `;

        taskList.innerHTML += taskItem;
        cont++;
    }
    taskForm.reset();
});

taskList.addEventListener('click', function (event) {
    if (event.target.parentElement.classList.contains('delete-btn')) {
        event.target.parentElement.parentElement.remove();
    } else if (event.target.classList.contains('delete-btn')) {
        event.target.parentElement.remove();
    } else if (event.target.parentElement.classList.contains('complete-btn')) {
        event.target.parentElement.parentElement.classList.toggle('completed');
    } else if (event.target.classList.contains('complete-btn')) {
        event.target.parentElement.classList.toggle('completed');
    } else if (event.target.parentElement.classList.contains('edit-btn') || event.target.classList.contains('edit-btn')) {
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
});

// Filtrar tareas
filterSelect.addEventListener('change', function () {
    const filterValue = filterSelect.value;
    const taskItems = taskList.querySelectorAll('.list-group-item');

    taskItems.forEach(task => {
        const isCompleted = task.classList.contains('completed');
        switch (filterValue) {
            case 'completadas':
                task.style.display = isCompleted ? 'block' : 'none';
                break;
            case 'pendientes':
                task.style.display = isCompleted ? 'none' : 'block';
                break;
            default:
                task.style.display = 'block';
        }
    });
});

// Ordenar tareas por fecha de vencimiento
sortByDueDateBtn.addEventListener('click', sortByDueDate);

function sortByDueDate() {
    const taskItems = [...taskList.querySelectorAll('.list-group-item')];
    taskItems.sort((a, b) => {
        const dateA = new Date(a.getAttribute('data-due-date'));
        const dateB = new Date(b.getAttribute('data-due-date'));
        return dateA - dateB;
    });

    taskList.innerHTML = '';
    taskItems.forEach(item => taskList.appendChild(item));
}

// Ordenar tareas por prioridad
sortByPriorityBtn.addEventListener('click', sortByPriority);

function sortByPriority() {
    const taskItems = [...taskList.querySelectorAll('.list-group-item')];
    taskItems.sort((a, b) => {
        const priorityOrder = {
            alta: 1,
            media: 2,
            baja: 3
        };
        const priorityA = priorityOrder[a.getAttribute('data-priority')];
        const priorityB = priorityOrder[b.getAttribute('data-priority')];
        return priorityA - priorityB;
    });

    taskList.innerHTML = '';
    taskItems.forEach(item => taskList.appendChild(item));
}