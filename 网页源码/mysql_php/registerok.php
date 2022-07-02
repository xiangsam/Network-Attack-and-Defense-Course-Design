<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
<style>
.websitetitle {
    background-color:black;
    color:white;
    margin:20px;
    padding:20px;
}
.register {
    background-color:whitesmoke;
    color:black;
    margin:20px;
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
    <div class="websitetitle">
        <h2>注册</h2>
        <p>还差几步，就可以完成注册啦！我们期待您的加入</p>
    </div>
    <div class="register">
        <center>
            <h3>注册</h3>
            <p>注册成功</p>
            <br>
            <p>正在跳转..请耐心等待5秒...</p>
        </center>
        <?php header("refresh:3;url=login.php");  ?>
    </div>
    
</body>
</html>
