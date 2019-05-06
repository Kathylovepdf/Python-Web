//jQuery只是一个“写得少，做得多”JavaScript的函数库，简单来说，就是用它组装好的功能来代替复杂的原生JavaScript代码
//定义两个全局变量
var a_int;
var b_int;

//获取input的值，并转化为数字
function getInputNum() {
    //这里是局部变量
    var a =document.getElementById('num1').value;
    var b =document.getElementById('num2').value;

    a_int =parseInt(a,10);
    b_int =parseInt(b,10);
}

//加法
function additon(x,y){
    return x+y;
}

//减法
function subtraction(x,y){
    return x-y;
}

//乘法
function multiplication(x,y){
    return x*y;
}

//除法
function division(x,y){
    if(y==0){
        alert("0不能做除数");
        return;
    }else{
        return x/y;
    }
}

//为按钮添加加法
$('#add').click(function(){
getInputNum();
var result1 =additon(a_int,b_int);
//用jQuery的写法
$('#result').html(String(result1));
});
//为按钮添加减法
$('#sub').click(function(){
    getInputNum();
    var result2 =subtraction(a_int,b_int);
    //用jQuery的写法
    $('#result').html(String(result2));
});
//为按钮添加乘法
$('#mul').click(function(){
    getInputNum();
    var result3 =multiplication(a_int,b_int);
    //用jQuery的写法
    $('#result').html(String(result3));
});
//为按钮添加除法
$('#div').click(function(){
    getInputNum();
    var result4 =division(a_int,b_int);
    //用jQuery的写法
    $("#result").html(String(result4));
});
