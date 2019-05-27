var tax = 0;
var rate = 0.19;

function calculateTax(income){
    tax = rate * income; 
}

calculateTax(1200)
console.log(tax) //228