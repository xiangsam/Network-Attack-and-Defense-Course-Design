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

        .movielist {
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
        <p><a href="./mypremovie.php">电影收藏夹</a> <a href="./profile.php">账号管理</a></p>
    </div>
    <div class="movielist">
        <h3 align=center>IMDB Top250 movies</h3>
        <?php
        include_once('./sqlconnect.php');
        $sql = "select * from movies order by movie_rank";
        $result = $conn->query($sql);
        if ($result === false) {
            echo "exec error";
        } else {
            echo "<table align=center border=1 width=80% frame=void>";
            echo "</tr>";

            echo "<th>" . "图片" . "</th>";
            echo "<th>" . "名称" . "</th>";
            echo "<th>" . "排名" . "</th>";
            echo "<th>" . "评分" . "</th>";
            echo "<th>" . "上映时间" . "</th>";

            echo "</tr>";
            $rec = $result->fetchAll(PDO::FETCH_NUM);
            for ($idx = 0; $idx < count($rec); $idx++) {
                echo "<tr>";

                $picture = $rec[$idx][4];
                echo "<td width=45><img src=" . $picture . "width=45 height=67></td>";
                $moviename = $rec[$idx][1];
                $movieid =  $rec[$idx][0];
                echo "<td><form id='" . $movieid . "'action='./search.php' method='post'><input type='hidden' name='director'><input type='hidden' name='writer'><input type='hidden' name='actor'><input type='hidden' name='type'><input type='hidden' name='area'><input type='hidden' name='moviename' value='" . $moviename . "'/><a href='javascript:document.getElementById(" . $movieid . ").submit();'>" . $moviename . "</a><input type='hidden' name='formsubmit' value='搜索'></form></td>";
                $rank = $rec[$idx][2];
                echo "<td>" . $rank . "</td>";
                $score = $rec[$idx][3];
                echo "<td>" . $score . "</td>";
                $year = $rec[$idx][5];
                echo "<td>" . $year . "</td>";
                echo "<td><form id='" . $rank . "'action='./likemovie.php' method='post'><input type='hidden' name='movieid' value='" . $movieid . "'/><input type='hidden' name='username' value='" . $_SESSION['name'] . "'><button onclick='javascript:document.getElementById(" . $rank . ").submit();'>" . "like!" . "</button><input type='hidden' name='formsubmit' value='like'></form></td>";
                echo "</tr>";
            }
            echo "</table>";
        }
        ?>
    </div>
</body>

</html>