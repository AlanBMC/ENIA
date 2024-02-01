var id_novo_contador = 1; // Contador global para garantir IDs únicos
var idTextareaAtivo = ''; // Inicializa a variável globalmente

function criarNovoTextarea() {
    var novoTextarea = document.createElement('textarea');
    novoTextarea.placeholder = "Digite '\\ ' para opções...";
    novoTextarea.setAttribute('id', 'myInput' + id_novo_contador); // ID único
    novoTextarea.setAttribute('name', 'texto' + id_novo_contador);
    novoTextarea.setAttribute('type', 'text');
    novoTextarea.setAttribute('class', 'textarea');
    // Classe para estilização, se necessário

    document.querySelector('.tarefa').appendChild(novoTextarea);
    // Aplica eventos ao novo textarea
    adicionarEventosTextarea(novoTextarea);

    id_novo_contador++; // Incrementa o contador para o próximo ID único
}
function adicionarEventosTextarea(textarea) {
    textarea.addEventListener('focus', function () {
        idTextareaAtivo = textarea.id; // Atualiza a variável com o ID do textarea atual
    });
    console.log('id atual: ', idTextareaAtivo)
    textarea.addEventListener('keyup', function (event) {
        // Verifica se a tecla Enter foi pressionada sem a tecla Shift
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // Impede a quebra de linha padrão
            criarNovoTextarea(); // Chama a função para criar um novo textarea
        }
        // Exibe ou esconde o dropdown com base na presença de '\'
        else if (event.target.value.includes('\\')) {
            document.getElementById('myDropdown').style.display = 'block';
        } else {
            document.getElementById('myDropdown').style.display = 'none';
        }
    });
}



function aplicarEstiloHs(selection, idTextareaAtivo) {
    var textarea = document.getElementById(idTextareaAtivo)
    switch (selection) {
        case 'H1':
            textarea.style.cssText = "font-size: 2em; font-weight: bold; text-align: center; border: 0px;";
            break;
        case 'H2':
            textarea.style.cssText = "font-size: 1.5em; font-weight: bold; text-align: center; border: 0px;";
            break;
    }
}

// Função para adicionar eventos ao dropdown
function adicionarEventoDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    var textareaAtivo = document.getElementById('myInput')
    dropdown.addEventListener('click', function (event) {

        var target = event.target;
        if (target.tagName === 'A') {
            var selection = target.textContent || target.innerText;

            if (textareaAtivo.tagName === 'TEXTAREA') {
                if (idTextareaAtivo) { // Verifica se idTextareaAtivo não está vazio
                    dropdown.style.display = 'none';
                    aplicarEstiloHs(selection, idTextareaAtivo); // Usa a variável global
                }

            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    adicionarEventosTextarea(document.getElementById('myInput'));
    adicionarEventoDropdown('myDropdown');
});