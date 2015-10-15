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
    var htmlList = document.getElementById("output");
    var reftestList = aManifest.items.reftest;
    for (var i = 0; i < reftestList.length; i++) {
        var reftest = reftestList[i];
        var item = "<li>";
        item += "<a href=\"" + reftest.url + "\">" + reftest.url + "</a>";
        item += " (" + reftest.references[0][1] + " ";
        item += "<a href=\"" + reftest.references[0][0] + "\">reference</a>)";
        item += "</li>";
        htmlList.insertAdjacentHTML("beforeend", item);
    }
    // FIXME: consider testharness and manual tests too.
}

function displayReftestList(aHTMLList, aReftestList)
{
}

window.addEventListener("DOMContentLoaded", fetchManifest);
