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
.register {
    background-color:rgba(245, 245, 245, 0.6);
    /* background-color:whitesmoke; */
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
        <h2>注册</h2>
        <p>还差几步，就可以完成注册啦！我们期待您的加入</p>
    </div>
    <div class="register">
        <center>
            <h3>注册</h3>
            <p>新世界的入口~</p>
            <form action="./registercheck.php" method="post">
                <label>&nbsp用户名:</label><input type="text" name="username">
                <br>
                <label>&nbsp邮&nbsp箱:</label><input type="text" name="email">
                <br>
                <label>&nbsp密&nbsp码:</label><input type="text" name="password">
                <br>
                <label>确认密码:</label><input type="text" name="password2">
                <br><br>
                <input type="submit" name="formsubmit" value="注册">
            </form>
            <br><br>
            <p>
                已经有账号了？<a href="./login.php">登录</a>
            </p>
            <br><br><br>
            <p align="right">
                管理员请点击<a href="adminlogin.php">这里</a>
            </p>
        </center>
    </div>
    
</body>
</html>
