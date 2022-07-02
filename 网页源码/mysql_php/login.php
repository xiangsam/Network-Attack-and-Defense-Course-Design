<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
<style>
.websitetitle {
    background-color:rgba(0, 0, 0, 0.7);
    color:white;
    margin:20px 10% 20px;
    padding:20px;
    border-style: outset;
}
.login {
    /* background-color:transparent; */
    background-color:rgba(245, 245, 245, 0.6);
    color:black;
    margin:20px 10% 20px;
    padding:20px;
}
label {
    display: inline-block;
    width: 70px;
    text-align: justify;
    text-align-last: justify;
    margin-right: 10px;
}

</style>
</head>
<body>
<canvas id="cas" style="position:absolute; z-index:-2"></canvas>
<script src="./background.js" type="text/javascript"></script>
    <div class="websitetitle">
        <h2>Movies World</h2>
        <p>你可以在这里畅所欲言，收藏你喜欢的电影</p>
    </div>
    <div class="login">
        <center>
            <h3>登录</h3>
            <p>请登录之后再查看哦~</p>
            <form action="./logincheck.php" method="post">
                <label>用户名:</label><input type="text" name="username">
                <br>
                <label>密&nbsp码:</label><input type="text" name="password">
                <br><br>
                <input type="submit" name="formsubmit" value="登录">
            </form>
            <br><br>
            <p>
                没有账号？快点加入我们吧!<a href="./register.php">注册</a>
            </p>
            <br><br><br>
            <p align="right">
                管理员请点击<a href="adminlogin.php">这里</a>
            </p>
        </center>
    </div>
</body>
</html>