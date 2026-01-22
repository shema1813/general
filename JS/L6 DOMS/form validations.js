


let colors = ["Red", "Green", "Blue", "Yellow"];


let students = [
    { name: "Ali", age: 20 },
    { name: "Sara", age: 22 },
    { name: "John", age: 21 }
];

let output = "";

output += "<b>Access by Index:</b><br>";
output += "Color at index 0: " + colors[0] + "<br>";
output += "Color at index 1: " + colors[1] + "<br><br>";

output += "<b>Access using Object Keys:</b><br>";
output += "Student Name: " + students[0].name + "<br>";
output += "Student Age: " + students[0].age + "<br><br>";


output += "<b>Whole Array using join():</b><br>";
output += colors.join(" , ") + "<br><br>";


let removedItem = colors.pop();

output += "<b>Using pop():</b><br>";
output += "Removed Item: " + removedItem + "<br>";
output += "Array After pop(): " + colors.join(" , ") + "<br>";


document.getElementById("arrayOutput").innerHTML = output;
