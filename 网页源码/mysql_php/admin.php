<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <style>
        .websitetitle {
            background-color: rgba(139, 0, 139, 0.7);
            color: white;
            margin: 20px 10% 20px;
            padding: 20px;
            border-style: outset;
        }

        .queryboard {
            /* background-color:transparent; */
            background-color: rgba(245, 245, 245, 0.6);
            /* opacity: 0.7; */
            color: black;
            margin: 20px 10% 20px;
            padding: 20px;
        }
    </style>
</head>

<body>
    <canvas id="cas" style="position:absolute; z-index:-2"></canvas>
    <script src="./background.js" type="text/javascript"></script>
    <div class="websitetitle">
        <h2>管理员系统</h2>
        <p>欢迎您,
            <?php
            session_start();
            echo $_SESSION['name'];
            ?></p>
        <p><a href="./login.php">返回</a></p>
    </div>
    <center>
        <div class="queryboard">
            <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
                <textarea row="10" cols="100" name="item" placeholder="SQL语句"></textarea>
                <br>
                <input type="submit" name="formsubmit" value="执行">
            </form>
            <p>执行结果</p>
            <p>
                <?php
                if (isset($_POST["formsubmit"])) {
                    $item = $_POST["item"];
                    include_once('./sqlconnect.php');
                    $result = $conn->query($item);
                    if ($result === false) {
                        echo "exec error";
                    } else {
                        if (strcasecmp(substr($item, 0, 6), "select") == 0) {
                            echo "<table border=1>";
                            $field_count = $result->columnCount();
                            for ($i = 0; $i < $field_count; ++$i) {
                                $field_info = $result->getColumnMeta($i);
                                echo "<td>" . $field_info['name'] . "</td>>";
                            }
                            echo "</tr>";
                            $rec = $result->fetchAll(PDO::FETCH_NUM);
                            for ($idx = 0; $idx < count($rec); $idx++) {
                                echo "<tr>";
                                for ($i = 0; $i < $field_count; ++$i) {
                                    $field_info = $rec[$idx][$i];
                                    echo "<td>" . $field_info . "</td>";
                                }
                                echo "</tr>";
                            }
                            echo "</table>";
                        } else {

                            print("\nSuccessful!");
                        }
                    }
                }
                ?>
            </p>
        </div>
    </center>

</body>

</html>