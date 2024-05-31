filterSelect.addEventListener('change', function () {
    const filterValue = filterSelect.value;
    const taskItems = taskList.querySelectorAll('.list-group-item');

    taskItems.forEach(task => {
        const isCompleted = task.getAttribute("data-completed");
        switch (filterValue) {
            case 'completadas':
                task.style.display = (isCompleted == "True") ? 'block' : 'none';
                break;
            case 'pendientes':
                task.style.display = (isCompleted == "True") ? 'none' : 'block';
                break;
            default:
                task.style.display = 'block';
        }
    });
});

filterSelect_public.addEventListener('change', function () {
    const filterValue = filterSelect_public.value;
    const taskItems = taskList_public.querySelectorAll('.list-group-item');

    taskItems.forEach(task => {
        const isCompleted = task.getAttribute("data-completed");
        switch (filterValue) {
            case 'completadas':
                task.style.display = (isCompleted == "True") ? 'block' : 'none';
                break;
            case 'pendientes':
                task.style.display = (isCompleted == "True") ? 'none' : 'block';
                break;
            default:
                task.style.display = 'block';
        }
    });
});