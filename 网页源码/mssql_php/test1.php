<html>
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
    echo $e->getMessage();
}

// $query = "select * from types";
// $statement = $conn->query($query);
// $result = $statement->fetchAll();
// echo $result[0][0];
// echo "sss" . $statement->columnCount() . "\n";
// foreach ($result as $rows) {
//     echo "";
//     foreach ($rows as $col_values) {
//         echo $col_values;
//     }
// }

?>

</html>