// var m=5;
// var n=2;
// var a =m+n;
// var b =m-n;
// var c =m*n;
// alert(a);
// alert(b);
// alert(c);
// var d;
// if (n==0){
//     alert("0不能作为除数");
// }else{
//     d =m%n;
//     alert(d);
// }

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

// var result1=additon(5,10);
// alert(result1);
// var result2=subtraction(1,2);
// alert(result2);
// var result3=multiplication(4,5);
// alert(result3);
// var result4=division(2,0);
// alert(result4);

//获取按钮
// var addBtn =document.getElementById('add');
// var subBtn =document.getElementById('sub');
// var mulBtn =document.getElementById('mul');
// var divBtn =document.getElementById('div');
// var resNum =document.getElementById('result');

//定义两个全局变量
var a_int;
var b_int;

//为按钮添加加法
// addBtn.onclick = function() {
//     //调用加法，弹出结果
//     getInputNum();
//     var result1 =additon(a_int,b_int);
//     // alert(result1);
//     // resNum.innerHTML=String(result1);
//     var resultHtml='<p>' + result1 + '</p>';
//     resNum.innerHTML=resultHtml;
// };
$('#add').click(function(){
    getInputNum();
    var result1 =additon(a_int,b_int);
    //用jQuery的写法
    $('#result').html(String(result1));
});
//为按钮添加减法
// subBtn.onclick =function() {
//     //调用减法，弹出结果
//     getInputNum();
//     var result2 =subtraction(a_int,b_int);
//     // alert(result2);
//     resNum.innerHTML=String(result2);
// };
$('#sub').click(function(){
    getInputNum();
    var result2 =subtraction(a_int,b_int);
    //用jQuery的写法
    $('#result').html(String(result2));
});
//为按钮添加乘法
// mulBtn.onclick =function() {
//     //调用乘法，弹出结果
//     getInputNum();
//     var result3 =multiplication(a_int,b_int);
//     // alert(result3);
//     resNum.innerHTML=String(result3);
// };
$('#mul').click(function(){
    getInputNum();
    var result3 =multiplication(a_int,b_int);
    //用jQuery的写法
    $('#result').html(String(result3));
});

//为按钮写除法
// divBtn.onclick =function() {
//     //调用除法，弹出结果
//     getInputNum();
//     var result4 =division(a_int,b_int);
//     // alert(result4);
//     resNum.innerHTML=String(result4);
// };
$('#div').click(function(){
    getInputNum();
    var result4 =division(a_int,b_int);
    //用jQuery的写法
    $("#result").html(String(result4));
});

//获取input的值，并转化为数字
function getInputNum() {
    //这里是局部变量
    // var a =document.getElementById('num1').value;
    // var b =document.getElementById('num2').value;

    //应用jQuery的写法
    var a =$('#num1').val();
    var b =$('#num2').val();

    a_int =parseInt(a,10);
    b_int =parseInt(b,10);
}
