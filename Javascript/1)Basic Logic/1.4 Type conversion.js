// Number
let num = 25;
console.log("Number:", num);
console.log("Number to String:", String(num));
console.log("Number to Boolean:", Boolean(num));

// String
let str = "100";
console.log("\nString:", str);
console.log("String to Number:", Number(str));
console.log("String to Integer:", parseInt(str));
console.log("String to Float:", parseFloat("100.50"));
console.log("String to Boolean:", Boolean(str));

// Boolean
let flag = true;
console.log("\nBoolean:", flag);
console.log("Boolean to Number:", Number(flag));
console.log("Boolean to String:", String(flag));

// Float
let decimal = 12.75;
console.log("\nFloat:", decimal);
console.log("Float to Integer:", parseInt(decimal));
console.log("Float to String:", String(decimal));

// Array
let arr = [10, 20, 30];
console.log("\nArray:", arr);
console.log("Array to String:", String(arr));
console.log("Array using join():", arr.join("-"));

// Object
let student = {
    name: "Sona",
    age: 20
};
console.log("\nObject:", student);
console.log("Object to String:", JSON.stringify(student));

// Character (ASCII / Unicode)
let ch = "A";
console.log("\nCharacter:", ch);
console.log("ASCII/Unicode:", ch.charCodeAt(0));

let code = 66;
console.log("Character from Code:", String.fromCharCode(code));

// Date to String
let today = new Date();
console.log("\nDate:", today);
console.log("Date to String:", today.toString());

// Number to Binary, Octal and Hexadecimal
let n = 25;
console.log("\nNumber:", n);
console.log("Binary:", n.toString(2));
console.log("Octal:", n.toString(8));
console.log("Hexadecimal:", n.toString(16));