//работает на любых (почти) сайтах кроме гитхаба, т.к. на нём security politic не даёт сделать eval()
let a = prompt('Input your... 1+1 :) ');
let b = confirm(eval(a)+'. Further?');
while (b==true){
    a = prompt('Input your... 1+1 :) ');
    b = confirm(eval(a)+'. Further?');
    }
