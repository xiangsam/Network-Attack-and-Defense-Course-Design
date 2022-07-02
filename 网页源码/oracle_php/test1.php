<html>
<?php
$type = 'oci';
$dbname = 'localhost:1521/xe';
$username = 'root';
$password = 'root';
$dsn = "$type:dbname=$dbname";
try {
    $conn = new PDO($dsn, $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
} catch (PDOException $e) {
    echo "<script> alert('连接数据库失败');history.go(-1); </script>";
}

$query = "select * from types";
$statement = $conn->query($query);
$result = $statement->fetchAll();
echo $result[0][0];
echo "sss" . $statement->columnCount() . "\n";
foreach ($result as $rows) {
    echo "";
    foreach ($rows as $col_values) {
        echo $col_values;
    }
}

?>

</html>