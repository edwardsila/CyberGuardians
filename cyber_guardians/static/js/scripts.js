const codeLines = [
    "import security_module",
    "def encrypt(data):",
    "    return encrypted_data",
    "if __name__ == '__main__':",
    "    print(encrypt('Sensitive Data'))"
];

let index = 0;
const codeElement = document.getElementById('code');

function displayCode() {
    if (index < codeLines.length) {
        codeElement.innerHTML += codeLines[index] + "<br>";
        index++;
        setTimeout(displayCode, 1000); // Adjust timing as needed
    }
}

displayCode();