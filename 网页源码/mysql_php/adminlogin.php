<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
<style>
.websitetitle {
    background-color:rgba(139, 0, 139, 0.7);
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
        <p>管理员系统</p>
    </div>
    <div class="login">
        <center>
            <h3>登录</h3>
            <p>亲爱的管理员，请登陆</p>
            <form action="./adminlogincheck.php" method="post">
                <label>用户名:</label><input type="text" name="adminname">
                <br>
                <label>密&nbsp码:</label><input type="text" name="adminpassword">
                <br>
                <input type="submit" name="formsubmit" value="登录">
            </form>
        </center>
    </div>

</body>
</html>