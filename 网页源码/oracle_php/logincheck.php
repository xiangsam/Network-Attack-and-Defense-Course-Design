<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <?php
    include_once('./sqlcheck.php');
    if (isset($_POST["formsubmit"]) && $_POST["formsubmit"] == "登录") {
        $user = $_POST["username"];
        $pwd = $_POST["password"];
        if ($user == "" || $pwd == "") {
            echo "<script> alert('用户名与密码不能为空');history.go(-1);</script>";
        } else {
            if (!safe($user) || !safe($pwd)) {
                die('SQL INJECTION DETECT!!!!');
            }
            include_once('./sqlconnect.php');
            $user = urldecode($user);
            $pwd = urldecode($pwd);
            $sql = "select * from users where user_name='$user' and user_password=$pwd";
            $result = $conn->query($sql);
            if ($result != FALSE) {
                $rows = $result->fetchAll();
                if (count($rows) > 0) {
                    session_start();
                    $_SESSION['name'] = $user;
                    header("Location:movies.php");
                } else {
                    echo "<script>alert('用户名或密码不正确！');  history.go(-1); </script>";
                }
            }
        }
    } else {
        echo "<script>alert('提交未成功！'); history.go(-1);</script>";
    }
    ?>
</head>

</html>