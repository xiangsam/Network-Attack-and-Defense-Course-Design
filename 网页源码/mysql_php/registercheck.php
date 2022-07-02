<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <?php
    include_once('./sqlcheck.php');
    if (isset($_POST["formsubmit"]) && $_POST["formsubmit"] == "注册") {
        $user = $_POST["username"];
        $pwd = $_POST["password"];
        $pwd2 = $_POST["password2"];
        $email = $_POST["email"];
        if ($user == "" || $pwd == "" || $email == "") {
            echo "<script> alert('用户名、密码与邮箱都不能为空');history.go(-1);</script>";
        } else if ($pwd != $pwd2) {
            echo "<script> alert('两次密码不一致！');history.go(-1);</script>";
        } else {
            if (!safe($user) || !safe($pwd)) {
                die('SQL INJECTION DETECT!!!!');
            }
            include_once('./sqlconnect.php');
            $sql1 = "select * from users where user_name='$user'";
            $result = $conn->query($sql);
            if ($result) {
                echo "<script> alert('用户名以及被使用过啦,请换一个吧');history.go(-1); </script>";
            } else {
                $sql2 = "insert into `users`(`user_name`,`user_email`,`user_password`) values('$user','$email',$pwd)";
                $result = $conn->exec($sql2);
                if ($result == 0) {
                    echo "注册失败";
                } else {
                    header("Location:registerok.php");
                }
            }
        }
    } else {
        echo "<script>alert('提交未成功！'); history.go(-1);</script>";
    }
    ?>
</head>

</html>