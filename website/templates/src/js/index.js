$('.dropdown-trigger').dropdown({coverTrigger: false,inDuration:400});

var dropdownParent = document.getElementById('dropdown');
dropdownParent.addEventListener('click',e => {
    var clickedOption = e.target;
    console.log(clickedOption);
    var dropDownButton = document.getElementById('searchbar').querySelector('a');
    var dropDownIcon = document.getElementById('searchbar').querySelector('a').querySelector('i').cloneNode(true);

    dropDownButton.textContent = clickedOption.textContent;
    dropDownButton.appendChild(dropDownIcon)
})
