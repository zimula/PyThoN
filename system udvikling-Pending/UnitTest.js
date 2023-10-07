const input = document.getElementById("input-area");
const btn  = document.querySelector(".add");
const btn1 = document.querySelector("#result");
const btn2 = document.querySelector(".diff");



class Rational{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    mySum(){
        let res = this.x + this.y
        return res;
    }
    myDiff(){
        return this.x - this.y;
    }
    myMultiply(){
        return this.x * this.y;
    }
    myDivide(){
        return this.x/this.y;
    }
    
}



let temp1 = 0;
let temp2 = 0;
btn.addEventListener("click", ()=>{

    temp1 = parseInt(input.value);
    console.log(temp1);
});
btn1.addEventListener("click", ()=>{
    temp2 = parseInt(input.valueJ);
    prob = new Rational(temp1, temp2);
    let result = prob.mySum();
    console.log(temp2);
    console.log(result);

});


