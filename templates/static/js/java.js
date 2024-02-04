var id_novo_contador = 1;
var idTextareaAtivo = ''; // Variável para rastrear o textarea em foco

function criarNovoTextarea() {
    var novoTextarea = document.createElement('input');
    novoTextarea.placeholder = "Digite '\\ ' para opções...";
    novoTextarea.setAttribute('id', 'myInput' + id_novo_contador);
    novoTextarea.setAttribute('name', 'texto');
    novoTextarea.setAttribute('type', 'text');

    adicionarEventosTextarea(novoTextarea);

    document.querySelector('.tarefa').appendChild(novoTextarea);
    id_novo_contador++;
}

function adicionarEventosTextarea(textarea) {
    textarea.addEventListener('focus', function () {
        idTextareaAtivo = textarea.id; // Atualiza a variável com o ID do textarea atual
        aplicarEventoDropdown();
    });

    textarea.addEventListener('keyup', function (event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            criarNovoTextarea();
        } else if (event.target.value.includes('\\')) {
            document.getElementById('myDropdown').style.display = 'block';
        } else {
            document.getElementById('myDropdown').style.display = 'none';
        }
    });

    textarea.addEventListener('keydown', function (event) {
        if (event.key === 'Backspace' && textarea.value === '' && !event.target.classList.contains('deleted')) {
            event.target.classList.add('deleted'); // Mark the textarea as deleted
            setTimeout(() => {
                if (event.target.classList.contains('deleted')) {
                    event.target.remove();
                }
            }, 50); // Delay to ensure Backspace is still pressed
        }
    });
}

function exibirDropdown(textarea) {
    const dropdown = document.getElementById('myDropdown');

    dropdown.style.display = 'block';
}

function esconderDropdown(textarea) {
    const dropdown = document.getElementById('myDropdown');

    dropdown.style.display = 'none';
}

function aplicarEventoDropdown() {
    
    const dropdown = document.getElementById('myDropdown');
    dropdown.addEventListener('click', function (event) {
        var target = event.target;
        if (target.tagName === 'A') {
            var selection = target.textContent || target.innerText;
            var textareaAtivo = document.getElementById(idTextareaAtivo);
            aplicarEstiloHs(selection, textareaAtivo);
            esconderDropdown();
        }
    });
}

function aplicarEstiloHs(selection, textarea) {
    switch (selection) {
        case 'H1':
            textarea.style.cssText = "font-size: 2em; font-weight: bold; text-align: center; border: 0px;";
            break;
        case 'H2':
            textarea.style.cssText = "font-size: 1.5em; font-weight: bold; text-align: center; border: 0px;";
            break;
    }
}

function removerUltimoElemento(classe) {
    const elementos = document.querySelectorAll(classe);
    if (elementos.length > 0) {
        const ultimoElemento = elementos[elementos.length - 1];
        ultimoElemento.remove();
    }
}

document.addEventListener('DOMContentLoaded', function () {
    criarNovoTextarea(); // Cria o primeiro textarea
    
});
