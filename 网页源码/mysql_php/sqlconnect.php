<?php
    $type = 'mysql';
    $hostname = 'localhost';
    $dbname = 'movieworld';
    $username = 'root';
    $password = 'root';
    $dsn = "$type:host=$hostname;dbname=$dbname";
    try {
        $conn = new PDO($dsn, $username, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);
    } catch (PDOException $e) {
        echo "<script> alert('连接数据库失败');history.go(-1); </script>";
    }
?>