$('.dropdown-trigger').dropdown({coverTrigger: false,inDuration:400});

var dropdownParent = document.getElementById('dropdown');
dropdownParent.addEventListener('click',e => {
    var clickedOption = e.target;
    console.log(clickedOption);
    var dropDownButton = document.getElementById('searchbar').querySelector('a');
    var dropDownButtonText = document.getElementById('searchbar').querySelector('a').querySelector('span');
    var dropDownIcon = document.getElementById('searchbar').querySelector('a').querySelector('i').cloneNode(true);

    dropDownButtonText.textContent = clickedOption.textContent;
    dropDownButton.appendChild(dropDownIcon)
})
function sendData(url) {
    var query = document.getElementById('searchbar').querySelector('input').value;
    var option = document.getElementById('searchbar').querySelector('a').querySelector('span').textContent;
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            query: query,
            option: option
        })
    })
    .then(response => {
        // 
        response.json()
        .then(result=> {
            renderHTML(result);
        })
    })
}
var searchButton = document.getElementById('searchbar').querySelector('button');

searchButton.addEventListener('click',e => {
    sendData('/result')
})
function renderHTML(response) {
    console.log(response)
    var elFlair = document.getElementById('flair-result').querySelector('span');
    var elPercent = document.getElementById('percent-result').querySelector('span');
    elFlair.textContent = 'Flair: ' + response.flair;
    elPercent.textContent = 'Percent: ' + response.percent;

}