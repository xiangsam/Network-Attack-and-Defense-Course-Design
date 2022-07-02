<?php
$type = 'oci';
$dbname = 'localhost:1521/xe';
$username = 'root';
$password = 'root';
$dsn = "$type:dbname=$dbname;charset=AL32UTF8";
try {
    $conn = new PDO($dsn, $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
} catch (PDOException $e) {
    echo "<script> alert('连接数据库失败');history.go(-1); </script>";
}
