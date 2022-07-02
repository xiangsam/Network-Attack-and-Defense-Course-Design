<?php
$type = 'sqlsrv';
$host = 'localhost';
$port = '1433';
$dbname = 'moviesystem';
$username = 'root';
$password = 'root';
$dsn = "$type:Server=$host,$port;Database=$dbname";
try {
    $conn = new PDO($dsn, $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
} catch (PDOException $e) {
    echo "<script> alert('连接数据库失败');history.go(-1); </script>";
}
