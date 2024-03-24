function sacudirElemento() {
    const elemento = document.getElementById('saludo');
    elemento.classList.add('sacudir'); // Agrega la clase para la animación
    
    // Quita la clase después de un período de tiempo
    setTimeout(function() {
        elemento.classList.remove('sacudir');
    }, 5000); // Duración de la animación
}

// Llama a la función para que se ejecute inicialmente
sacudirElemento();

// Llama a la función cada cierto tiempo
setInterval(sacudirElemento, 10000);