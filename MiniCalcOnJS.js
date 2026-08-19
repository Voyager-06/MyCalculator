//работает на любых (почти) сайтах кроме гитхаба, т.к. на нём security politic не даёт сделать eval()
let a = prompt('Введите выражение: / Input: ');
let b = confirm(eval(a)+'. Дальше? / Further?');
while (b==true){
    a = prompt('Введите выражение: / Input: ');
    b = confirm(eval(a)+'. Дальше? / Further?');
    }
