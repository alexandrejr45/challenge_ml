
let bloco_de_notas = document.querySelector('#bloco_de_notas')
let botao_adicionar = document.querySelector('#add_nota')
let contador_nota = 0


function adicionar_nota() {
    let texto_nota = document.querySelector('#nota_texto').value
    contador_nota++;
    let template_nota = `
    <div class=nota_22 id=nota_${contador_nota}>
        ${texto_nota}
    </div>
    <br/>
    <button id=editar_nota_${contador_nota} onclick=${editar_nota(contador_nota)}>Editar nota</button>
    `

    bloco_de_notas.innerHTML += template_nota

}

function editar_nota(contador_nota) {
    if (contador_nota > 0) {
        let texto_nota = document.querySelector('#nota_texto')
        let nota_em_edicao = document.querySelector(`#nota_${contador_nota}`)
    }

}
