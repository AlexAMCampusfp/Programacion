<?php
session_start();
require 'conexion.php';

if (!isset($_SESSION['usuario_id'])) {
    header("Location: inicio_sesion.php");
    exit();
}

$id = $_GET['id'];
$stmt = $pdo->prepare("DELETE FROM tareas WHERE id = ? AND usuario_id = ?");
$stmt->execute([$id, $_SESSION['usuario_id']]);

header("Location: tareas.php");
exit();
?>