function generateTestPageFor(aTestFunction, aJSON)
{
    for (mathvariant in aJSON) {
        for (baseChar in aJSON[mathvariant]) {
            var transformedChar = aJSON[mathvariant][baseChar];
            baseChar = parseInt(baseChar).toString(16).toUpperCase();
            transformedChar = transformedChar.toString(16).toUpperCase();
            var testString = aTestFunction.call(null, mathvariant, baseChar, transformedChar);
            document.body.insertAdjacentHTML("beforeend", testString);
        }
    }
    document.documentElement.removeAttribute("class");
}

function generateTestPage(aTestFunction)
{
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                var json = JSON.parse(httpRequest.responseText);
                generateTestPageFor(aTestFunction, json);
            }
        }
    };
    httpRequest.open("GET", "./mathvariant-transforms.json");
    httpRequest.send();
}
