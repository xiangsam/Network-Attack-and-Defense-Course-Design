<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <style>
        .websitetitle {
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            margin: 20px 10% 20px;
            padding: 20px;
            border-style: outset;
        }

        .board,
        .movieselect {
            /* background-color:transparent; */
            background-color: rgba(245, 245, 245, 0.6);
            color: black;
            margin: 20px 10% 20px;
            padding: 20px;
        }

        table {
            border: black 1px solid;
            border-collapse: collapse;
        }

        th {
            border: black 1px solid;
            font-style: italic;
            font-family: sans-serif;
        }

        td {
            border: black 1px solid;
            text-align: center;
            text-align-last: center;
        }

        button {
            background-color: whitesmoke;
            -webkit-transition-duration: 0.4s;
            /* Safari */
            transition-duration: 0.4s;
        }

        button:hover {
            background-color: red;
            /* Green */
            color: white;
        }
    </style>
</head>

<body>
    <canvas id="cas" style="position:absolute; z-index:-2"></canvas>
    <script src="./background.js" type="text/javascript"></script>
    <div class="websitetitle">
        <h2>Movie World</h2>
        <p>欢迎您,
            <?php
            session_start();
            echo $_SESSION['name'];
            ?></p>
        <p><a href="./mypremovie.php">电影收藏夹</a> <a href="./profile.php">账号管理</a> <a href="./movies.php">返回首页</a></p>
    </div>
    <div class="board">
        <?php
        if (isset($_POST["formsubmit"]) && $_POST["formsubmit"] == "搜索") {
            $moviename = $_POST["moviename"];
            $director = $_POST["director"];
            $writer = $_POST["writer"];
            $actor = $_POST["actor"];
            $type = $_POST["type"];
            $area = $_POST["area"];
            if ($moviename == "" && $director == "" && $writer == "" && $actor == "" && $type == "" && $area == "") {
                echo "<script>alert('搜索内容不能为空'); history.go(-1);</script>";
            } else {
                include_once('./sqlconnect.php');
                $arr1 = array();
                $arr2 = array();
                $arr3 = array();
                $arr4 = array();
                $arr5 = array();
                $arr6 = array();
                if ($moviename != "") {
                    $sql1 = "select movie_id from movies where movie_name='$moviename'";
                    $result1 = $conn->query($sql1);
                    $rows = $result1->fetchAll(PDO::FETCH_ASSOC);
                    $num1 = count($rows);
                    if ($num1) {
                        foreach ($rows as $rs) {
                            $arr1[] = $rs;
                        }
                    }
                }
                if ($director != "") {
                    $sql2 = "select movie_id from directors natural join movie_director where director_name='$director'";
                    $result2 = $conn->query($sql2);
                    $rows = $result2->fetchAll(PDO::FETCH_ASSOC);
                    $num2 = count($rows);
                    if ($num2) {
                        foreach ($rows as $rs) {
                            $arr2[] = $rs;
                        }
                    }
                }
                if ($writer != "") {
                    $sql3 = "select movie_id from writers natural join movie_writer where writer_name='$writer'";
                    $result3 = $conn->query($sql3);
                    $rows = $result3->fetchAll(PDO::FETCH_ASSOC);
                    $num3 = count($rows);
                    if ($num3) {
                        foreach ($rows as $rs) {
                            $arr3[] = $rs;
                        }
                    }
                }
                if ($actor != "") {
                    $sql4 = "select movie_id from actors natural join movie_actor where actor_name='$actor'";
                    $result4 = $conn->query($sql4);
                    $rows = $result4->fetchAll(PDO::FETCH_ASSOC);
                    $num4 = count($rows);
                    if ($num4) {
                        foreach ($rows as $rs) {
                            $arr4[] = $rs;
                        }
                    }
                }
                if ($type != "") {
                    $sql5 = "select movie_id from types natural join movie_type where type_name='$type'";
                    $result5 = $conn->query($sql5);
                    $rows = $result5->fetchAll(PDO::FETCH_ASSOC);
                    $num5 = count($rows);
                    if ($num5) {
                        foreach ($rows as $rs) {
                            $arr5[] = $rs;
                        }
                    }
                }
                if ($area != "") {
                    $sql6 = "select movie_id from areas natural join movie_area where area_name='$area'";
                    $result6 = $conn->query($sql6);
                    $rows = $result6->fetchAll(PDO::FETCH_ASSOC);
                    $num6 = count($rows);
                    if ($num1) {
                        foreach ($rows as $rs) {
                            $arr6[] = $rs;
                        }
                    }
                }
            }
        } else {
            echo "<script>alert('提交未成功！'); history.go(-1);</script>";
        }
        ?>
        <?php

        $idarr = array(array(), array(), array(), array(), array(), array());
        for ($i = 0; $i < count($arr1); $i++) {
            $idarr[0][] = $arr1[$i]["movie_id"];
        }
        for ($i = 0; $i < count($arr2); $i++) {
            $idarr[1][] = $arr2[$i]["movie_id"];
        }
        for ($i = 0; $i < count($arr3); $i++) {
            $idarr[2][] = $arr3[$i]["movie_id"];
        }
        for ($i = 0; $i < count($arr4); $i++) {
            $idarr[3][] = $arr4[$i]["movie_id"];
        }
        for ($i = 0; $i < count($arr5); $i++) {
            $idarr[4][] = $arr5[$i]["movie_id"];
        }
        for ($i = 0; $i < count($arr6); $i++) {
            $idarr[5][] = $arr6[$i]["movie_id"];
        }
        $index = array();
        for ($i = 0; $i < 6; $i++) {
            if (count($idarr[$i]) != 0) {
                $index[] = $i;
            }
        }
        $ans = $idarr[$index[0]];
        for ($i = 1; $i < count($index); $i++) {
            $ans = array_intersect($ans, $idarr[$index[$i]]);
        }
        $ans = array_values($ans);
        if (count($ans) == 0) {
            echo "查找无结果，请尝试缩减限制条件并确认条件正确";
            echo "<p><a href='./movies.php'>" . "返回" . "</a></p>";
        } else {
            for ($i = 0; $i < count($ans); $i++) {
                $movieid = $ans[$i];
                $sql_base = "select movie_picture ,movie_name, movie_score, movie_year from movies where movie_id = '$movieid'";
                $sql_director = "select director_name from movie_director  natural join directors where movie_id='$movieid'";
                $sql_writer = "select writer_name from movie_writer  natural join writers where movie_id='$movieid'";
                $sql_actor = "select actor_name from movie_actor  natural join actors where movie_id='$movieid'";
                $sql_type = "select type_name from movie_type  natural join types where movie_id='$movieid'";
                $sql_area = "select area_name from movie_area  natural join areas where movie_id='$movieid'";
                $result_base = $conn->query($sql_base);
                $result_director = $conn->query($sql_director);
                $result_writer = $conn->query($sql_writer);
                $result_actor = $conn->query($sql_actor);
                $result_type = $conn->query($sql_type);
                $result_area = $conn->query($sql_area);
                echo "<table align=center border=1 width=80%>";
                $rec = $result_base->fetch();
                echo "<tr>";
                echo "<td rowspan='7' width=240><img src=" . $rec['movie_picture'] . "width=250 height=300></td>";
                echo "<td>" . $rec['movie_name'] . "  (" . $rec["movie_year"] . ")";
                echo "<form id='" . $movieid . "'action='./likemovie.php' method='post'><input type='hidden' name='movieid' value='" . $movieid . "'/><input type='hidden' name='username' value='" . $_SESSION['name'] . "'><button onclick='javascript:document.getElementById(" . $movieid . ").submit();'>" . "like!" . "</button><input type='hidden' name='formsubmit' value='like'></form>";
                echo "</td>";
                echo "</tr>";
                echo "<tr>";
                echo "<td>" . "score:" . $rec['movie_score'] . "</td>";
                echo "</tr>";
                $rows = $result_director->fetchAll(PDO::FETCH_ASSOC);
                if (count($rows) != 0) {
                    echo "<tr>";
                    echo "<td>" . "导演：";
                    foreach ($rows as $rec) {
                        echo $rec['director_name'] . " ";
                    }
                    echo "</td>";
                    echo "</tr>";
                }
                $rows = $result_writer->fetchAll(PDO::FETCH_ASSOC);
                if (count($rows) != 0) {
                    echo "<tr>";
                    echo "<td>" . "编剧：";
                    foreach ($rows as $rec) {
                        echo $rec['writer_name'] . " ";
                    }
                    echo "</td>";
                    echo "</tr>";
                }
                $rows = $result_actor->fetchAll(PDO::FETCH_ASSOC);
                if (count($rows) != 0) {
                    echo "<tr>";
                    echo "<td>" . "演员：";
                    foreach ($rows as $rec) {
                        echo $rec['actor_name'] . " ";
                    }
                    echo "</td>";
                    echo "</tr>";
                }
                $rows = $result_type->fetchAll(PDO::FETCH_ASSOC);
                if (count($rows) != 0) {
                    echo "<tr>";
                    echo "<td>" . "类型：";
                    foreach ($rows as $rec) {
                        echo $rec['type_name'] . " ";
                    }
                    echo "</td>";
                    echo "</tr>";
                }
                $rows = $result_area->fetchAll(PDO::FETCH_ASSOC);
                if (count($rows) != 0) {
                    echo "<tr>";
                    echo "<td>" . "地区：";
                    foreach ($rows as $rec) {
                        echo $rec['area_name'] . " ";
                    }
                    echo "</td>";
                    echo "</tr>";
                }
                echo "</table>";
                echo "<br><br>";
            }
        }
        ?>
    </div>
</body>

</html>