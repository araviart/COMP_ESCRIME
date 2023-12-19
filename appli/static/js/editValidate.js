function edit(id) {
    var p = document.getElementById(id);
    var text = p.innerText;
    p.innerHTML = `<input type="text" id="${id}-input" value="${text}" style="width: 300px;"> <button onclick="validateField('${id}')">Valider</button>`;
}

function validateField(id) {
    var input = document.getElementById(id + '-input');
    var text = input.value;
    var p = document.getElementById(id);
    p.innerHTML = text;
    updateDatabase(id, text)
}