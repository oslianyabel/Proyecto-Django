// Ordenar por fecha de vencimiento
sortByDueDateBtn.addEventListener('click', sortByDueDate);
sortByDueDateBtn_public.addEventListener('click', sortByDueDate_public);

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

function sortByDueDate_public() {
    const taskItems = [...taskList_public.querySelectorAll('.list-group-item')];
    taskItems.sort((a, b) => {
        const dateA = new Date(a.getAttribute('data-due-date'));
        const dateB = new Date(b.getAttribute('data-due-date'));
        return dateA - dateB;
    });

    taskList_public.innerHTML = '';
    taskItems.forEach(item => taskList_public.appendChild(item));
}

// Ordenar por prioridad
sortByPriorityBtn.addEventListener('click', sortByPriority);
sortByPriorityBtn_public.addEventListener('click', sortByPriority_public);

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

function sortByPriority_public() {
    const taskItems = [...taskList_public.querySelectorAll('.list-group-item')];
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

    taskList_public.innerHTML = '';
    taskItems.forEach(item => taskList_public.appendChild(item));
}