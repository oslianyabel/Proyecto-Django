btnLogout.addEventListener('click', function () {
    window.location.href = "{% url 'login' %}";
});

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