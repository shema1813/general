//display Helpers
function getHistory(){
    return document.getElementById("history-value").innerText;
}

function printHistory(num){
    return document.getElementById("history-value").innerText = num;
}

function getOutput(){
    return document.getElementById("output-value").innerText;
}

function printOutput(num){
    if (num === ""){
        document.getElementById("output-value").innerText = "";
    } else{
        document.getElementById("output-value").innerText = formatNumber(num);
    }
}

//Number formating 
function formatNumber(num){
    if (num === "" || num === "-") return num;
    return Number(num).toLocaleString("en");
}

function reverseNumberFormat(num){
    if (num === "") return "";
    return Number(num.replace(/,/g, ""))
}

//operator buttons
var operators = document.getElementsByClassName("operator");

for (var i = 0; i < operators.length; i++) {
    operators[i].addEventListener("click", function () {
        
        var output = getOutput();
         var history = getHistory();

         if( this.id === "clear"){
            printHistory("");
            printOutput("");
            return
         }

         if(this.id === "backspace"){
            output = reverseNumberFormat(output).toString();
            output = output.slice(0,-1);
            printOutput(output);
            return
         }

         //prvent double operators
         if (output === "" && history !=="") {
            if (isNaN(history[history.length - 1])) {
                history = history.slice(0,-1);
            }
         }

         //Main calculation logic
         if (output !== "" || history !== ""); {
            output = output === "" ? "": reverseNumberFormat(output);
            history  = history + output;

            if(this.id === "="){
                try{
                    var result=eval(history);
                    printOutput(result);
                    printHistory("");
                } catch{
                    printOutput("Error");
                    printHistory("");
                }
            }else {
                    history = history + this.id;
                    printHistory(history);
                    printOutput("");
                }
         }
    });
}

//number buttons
var numbers = document.getElementsByClassName("number");

for(var i=0;i < numbers.length; i++){
    numbers[i].addEventListener("click", function(){
       

        var output = reverseNumberFormat(getOutput());

        if(!isNaN(output)){
            output = output + this.id;
            printOutput(output);
        }
    });
}

