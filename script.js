document.getElementById('registroUsuario').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const edad = parseInt(document.getElementById('edad').value);
    const planBase = document.getElementById('planBase').value;
    const paqueteAdicional = document.getElementById('paqueteAdicional').value;
    const duracion = document.getElementById('duracion').value;

    if (edad < 18 && paqueteAdicional !== 'Infantil') {
        alert('Los usuarios menores de 18 años solo pueden contratar el Pack Infantil.');
        return;
    }

    if (planBase === 'Básico' && paqueteAdicional !== '') {
        alert('El Plan Básico solo permite un paquete adicional.');
        return;
    }

    if (paqueteAdicional === 'Deporte' && duracion !== 'Anual') {
        alert('El Pack Deporte solo puede ser contratado con una duración de 1 año.');
        return;
    }


    this.submit();
});

