<html>
<?php
$conn = oci_connect("root", "root");
//检查连接是否成功
if ($conn) {
    echo "connect success";
} else {
    echo "connect error";
}
$query = "select * from USERS";
$statement = oci_parse($conn, $query);
oci_execute($statement);
oci_fetch_all($statement, $result);
foreach ($result as $rows) {
    echo "";
    foreach ($rows as $col_values) {
        echo $col_values;
    }
}
?>

</html>