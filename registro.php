<?php
session_start();
require 'conexion.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre_usuario = $_POST['nombre_usuario'];
    $correo = $_POST['correo'];
    $contrasena = password_hash($_POST['contrasena'], PASSWORD_BCRYPT);

    // Verificar si el correo ya existe
    $stmt = $pdo->prepare("SELECT * FROM usuarios WHERE correo = ?");
    $stmt->execute([$correo]);
    if ($stmt->rowCount() > 0) {
        echo "El correo ya está registrado.";
    } else {
        $stmt = $pdo->prepare("INSERT INTO usuarios (nombre_usuario, correo, contrasena) VALUES (?, ?, ?)");
        if ($stmt->execute([$nombre_usuario, $correo, $contrasena])) {
            header("Location: inicio_sesion.php");
            exit();
        } else {
            echo "Error al registrar usuario.";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro de Usuario</title>
</head>
<body>
    <h2>Registro de Usuario</h2>
    <form action="registro.php" method="POST">
        <label for="nombre_usuario">Nombre de Usuario:</label>
        <input type="text" id="nombre_usuario" name="nombre_usuario" required><br><br>
        
        <label for="correo">Correo Electrónico:</label>
        <input type="email" id="correo" name="correo" required><br><br>
        
        <label for="contrasena">Contraseña:</label>
        <input type="password" id="contrasena" name="contrasena" required><br><br>
        
        <button type="submit">Registrarse</button>
    </form>
</body>
</html>