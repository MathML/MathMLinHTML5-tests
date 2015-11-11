function fetchManifest()
{
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                var data = JSON.parse(httpRequest.responseText);
                displayTestList(data);
            }
        }
    };
    httpRequest.open("GET", "./MANIFEST.json");
    httpRequest.send();
}

function displayTestList(aManifest)
{
    var i, htmlList;

    var reftestList = aManifest.items.reftest;
    htmlList = document.getElementById("reftestList");
    for (i = 0; i < reftestList.length; i++) {
        var reftest = reftestList[i];
        var item = "<li>";
        item += "<a href=\"" + reftest.url + "\">" + reftest.url + "</a>";
        item += " (" + reftest.references[0][1] + " ";
        item += "<a href=\"" + reftest.references[0][0] + "\">reference</a>)";
        item += "</li>";
        htmlList.insertAdjacentHTML("beforeend", item);
    }

    var testharnessList = aManifest.items.testharness;
    htmlList = document.getElementById("testharnessList");
    for (i = 0; i < testharnessList.length; i++) {
        var test = testharnessList[i];
        var item = "<li>";
        item += "<a href=\"" + test.url + "\">" + test.url + "</a>";
        item += "</li>";
        htmlList.insertAdjacentHTML("beforeend", item);
    }

    // FIXME: consider manual tests too.
}

function displayReftestList(aHTMLList, aReftestList)
{
}

window.addEventListener("DOMContentLoaded", fetchManifest);
