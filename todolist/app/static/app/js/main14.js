const btnLogout = document.querySelector('.btn-logout');
let cont = 0;
let select = -1;

btnLogout.addEventListener('click', function () {
    window.location.href = "{% url 'login' %}";
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

/* function eliminar(tarea) {
    id = tarea.getAttribute("data-id");
    //tarea.remove();
    var confirmacion = confirm("¿Estás seguro de que deseas eliminar?");
    if (confirmacion) {
        $.ajax({
            url: id,  // URL de tu API para eliminar la tarea por ID
            type: 'DELETE',  // Método HTTP DELETE
            headers: { "X-CSRFToken": "{{ csrf_token }}" },
            success: function (response) {
                // Manejar la respuesta exitosa
                alert("yes");
                console.log('Tarea eliminada exitosamente:', response);
            },
            error: function (xhr, status, error) {
                // Manejar errores
                alert("No");
                console.error('Error al eliminar la tarea:', error);
            }
        });
    }
} */