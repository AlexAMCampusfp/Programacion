<?php
$conn = new mysqli('localhost', 'localhost', 'contraseña', 'base_de_datos');

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $edad = $_POST['edad'];
    $plan_base = $_POST['planBase'];
    $paquete_adicional = $_POST['paqueteAdicional'];
    $duracion = $_POST['duracion'];


    $stmt = $conn->prepare("INSERT INTO usuarios (nombre, correo, edad, plan_base, paquete_adicional, duracion) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssisss", $nombre, $correo, $edad, $plan_base, $paquete_adicional, $duracion);
    
    if ($stmt->execute()) {
        echo "Usuario registrado exitosamente.";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
}
$conn->close();
?>
