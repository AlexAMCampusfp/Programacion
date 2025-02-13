<?php
session_start();
require 'conexion.php';

// Mostrar errores para depuración
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if (!isset($_SESSION['usuario_id'])) {
    header("Location: inicio_sesion.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $titulo = $_POST['titulo'];
    $tarea = $_POST['tarea'];
    $usuario_id = $_SESSION['usuario_id'];

    // Verificar que la variable $pdo esté definida y sea una instancia de PDO
    if (isset($pdo) && $pdo instanceof PDO) {
        try {
            $stmt = $pdo->prepare("INSERT INTO tareas (usuario_id, titulo, tarea, completada) VALUES (?, ?, ?, 0)");
            if ($stmt->execute([$usuario_id, $titulo, $tarea])) {
                echo "Tarea agregada exitosamente.";
            } else {
                echo "Error al agregar la tarea.";
            }
        } catch (PDOException $e) {
            echo "Error en la consulta: " . $e->getMessage();
        }
    } else {
        echo "Error en la conexión a la base de datos.";
    }
}

try {
    $stmt = $pdo->prepare("SELECT * FROM tareas WHERE usuario_id = ?");
    $stmt->execute([$_SESSION['usuario_id']]);
    $tareas = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    echo "Error en la consulta: " . $e->getMessage();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestión de Tareas</title>
</head>
<body>
    <h2>Gestión de Tareas</h2>
    <form action="tareas.php" method="POST">
        <label for="titulo">Título de la Tarea:</label>
        <input type="text" id="titulo" name="titulo" required><br><br>
        
        <label for="tarea">Descripción de la Tarea:</label>
        <input type="text" id="tarea" name="tarea" required><br><br>
        
        <button type="submit">Agregar Tarea</button>
    </form>
    <h3>Tareas Pendientes</h3>
    <ul>
        <?php foreach ($tareas as $tarea): ?>
            <li>
                <strong><?php echo htmlspecialchars($tarea['titulo']); ?>:</strong> <?php echo htmlspecialchars($tarea['tarea']); ?>
                <?php if (!$tarea['completada']): ?>
                    <a href="completar_tarea.php?id=<?php echo $tarea['id']; ?>">Marcar como completada</a>
                <?php endif; ?>
                <a href="eliminar_tarea.php?id=<?php echo $tarea['id']; ?>">Eliminar</a>
            </li>
        <?php endforeach; ?>
    </ul>
    <a href="cerrar_sesion.php">Cerrar Sesión</a>
</body>
</html>