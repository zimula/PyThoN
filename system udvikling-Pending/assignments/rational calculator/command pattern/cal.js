
    const calculateButton = document.querySelector("#btn");
    const fraction1 = document.querySelector("#fraction1");
    const fraction2 = document.querySelector("#fraction2");
    const operation = document.querySelector("#operation");
    const resultElement = document.querySelector("#result");
    let result;


    calculateButton.addEventListener("click", () => {
        const x = parseFloat(fraction1.value);
        const y = parseFloat(fraction2.value);
        switch (operation.value) {
            case "Add":
                result = x + y;
                break;
            case "Subtract":
                result = x - y;
                break;
            case "Multiply":
                result = x * y;
                break;
            case "Divide":
                result = x / y;
                break;
        }
        if(result || result == 0){
            resultElement.innerHTML = result;
        }
        else{
            resultElement.innerHTML = "value issue";
        }
    });


