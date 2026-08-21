const TAMANHO = 5;
const LIMITE_RANKING = 5;

const tabuleiroElemento = document.getElementById("tabuleiro");
const movimentosElemento = document.getElementById("movimentos");
const tempoElemento = document.getElementById("tempo");
const rankingElemento = document.getElementById("ranking-list");

const resultadoElemento = document.getElementById("resultado");
const resultadoTitulo = document.getElementById("resultado-titulo");
const resultadoInfo = document.getElementById("resultado-info");

const btnCima = document.getElementById("btn-cima");
const btnBaixo = document.getElementById("btn-baixo");
const btnEsquerda = document.getElementById("btn-esquerda");
const btnDireita = document.getElementById("btn-direita");
const btnReiniciar = document.getElementById("btn-reiniciar");

let tabuleiro = [];

let jogadorLinha = 0;
let jogadorColuna = 0;

let damaLinha = 0;
let damaColuna = 0;

let movimentos = 0;

let venceu = false;
let perdeu = false;

let tempoInicio = 0;
let tempoFinal = 0;

let intervaloTempo = null;


/* =========================
   RANKING
   ========================= */

function carregarRanking() {
    const dados = localStorage.getItem("aUltimaCasaRecordes");

    if (!dados) {
        return [];
    }

    try {
        const ranking = JSON.parse(dados);

        if (!Array.isArray(ranking)) {
            return [];
        }

        return ranking;

    } catch (erro) {
        return [];
    }
}


function salvarRanking(ranking) {
    localStorage.setItem(
        "aUltimaCasaRecordes",
        JSON.stringify(ranking)
    );
}


function registrarRecorde() {
    const ranking = carregarRanking();

    ranking.push({
        casas: movimentos,
        tempo: tempoFinal
    });

    ranking.sort((a, b) => {

        if (a.casas !== b.casas) {
            return b.casas - a.casas;
        }

        return a.tempo - b.tempo;
    });

    const melhores = ranking.slice(0, LIMITE_RANKING);

    salvarRanking(melhores);

    atualizarRanking();
}


function atualizarRanking() {
    const ranking = carregarRanking();

    rankingElemento.innerHTML = "";

    for (let i = 0; i < LIMITE_RANKING; i++) {

        const linha = document.createElement("div");

        if (ranking[i]) {

            linha.textContent =
                `${i + 1}º  ${ranking[i].casas} casas | ${ranking[i].tempo.toFixed(2)}s`;

        } else {

            linha.textContent =
                `${i + 1}º  --`;
        }

        rankingElemento.appendChild(linha);
    }
}


/* =========================
   TABULEIRO
   ========================= */

function criarMapa() {

    const mapa = [];

    for (let linha = 0; linha < TAMANHO; linha++) {

        mapa.push([]);

        for (let coluna = 0; coluna < TAMANHO; coluna++) {

            mapa[linha][coluna] = true;
        }
    }

    return mapa;
}


/* =========================
   POSIÇÕES
   ========================= */

function sortearPosicoes() {

    jogadorLinha =
        Math.floor(Math.random() * TAMANHO);

    jogadorColuna =
        Math.floor(Math.random() * TAMANHO);

    do {

        damaLinha =
            Math.floor(Math.random() * TAMANHO);

        damaColuna =
            Math.floor(Math.random() * TAMANHO);

    } while (
        damaLinha === jogadorLinha &&
        damaColuna === jogadorColuna
    );
}


/* =========================
   REINICIAR JOGO
   ========================= */

function reiniciarJogo() {

    tabuleiro = criarMapa();

    sortearPosicoes();

    movimentos = 0;

    venceu = false;
    perdeu = false;

    tempoInicio = performance.now();
    tempoFinal = 0;

    resultadoElemento.classList.add("escondido");
    resultadoElemento.classList.remove("vitoria");
    resultadoElemento.classList.remove("derrota");

    iniciarCronometro();

    desenhar();

    atualizarHud();
}


/* =========================
   CRONÔMETRO
   ========================= */

function iniciarCronometro() {

    if (intervaloTempo) {
        clearInterval(intervaloTempo);
    }

    intervaloTempo = setInterval(() => {

        if (venceu || perdeu) {
            return;
        }

        atualizarTempo();

    }, 50);
}


function atualizarTempo() {

    const agora = performance.now();

    const segundos =
        (agora - tempoInicio) / 1000;

    tempoElemento.textContent =
        `${segundos.toFixed(2)}s`;
}


function pararCronometro() {

    if (intervaloTempo) {

        clearInterval(intervaloTempo);

        intervaloTempo = null;
    }
}


/* =========================
   MOVIMENTAÇÃO
   ========================= */

function tentarMover(dLinha, dColuna) {

    if (venceu || perdeu) {
        return;
    }

    const novaLinha =
        jogadorLinha + dLinha;

    const novaColuna =
        jogadorColuna + dColuna;

    if (
        novaLinha < 0 ||
        novaLinha >= TAMANHO ||
        novaColuna < 0 ||
        novaColuna >= TAMANHO
    ) {
        return;
    }

    if (!tabuleiro[novaLinha][novaColuna]) {
        return;
    }

    const linhaAnterior = jogadorLinha;
    const colunaAnterior = jogadorColuna;

    jogadorLinha = novaLinha;
    jogadorColuna = novaColuna;

    tabuleiro[linhaAnterior][colunaAnterior] = false;

    movimentos++;

    verificarEstado();

    desenhar();

    atualizarHud();
}


/* =========================
   VERIFICAR ESTADO
   ========================= */

function verificarEstado() {

    if (
        jogadorLinha === damaLinha &&
        jogadorColuna === damaColuna
    ) {

        venceu = true;

        finalizarPartida();

        return;
    }

    if (!temSaida()) {

        perdeu = true;

        finalizarPartida();
    }
}


function temSaida() {

    const direcoes = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ];

    for (const [dLinha, dColuna] of direcoes) {

        const linha =
            jogadorLinha + dLinha;

        const coluna =
            jogadorColuna + dColuna;

        if (
            linha >= 0 &&
            linha < TAMANHO &&
            coluna >= 0 &&
            coluna < TAMANHO &&
            tabuleiro[linha][coluna]
        ) {
            return true;
        }
    }

    return false;
}


/* =========================
   FINAL DA PARTIDA
   ========================= */

function finalizarPartida() {

    pararCronometro();

    const agora = performance.now();

    tempoFinal =
        (agora - tempoInicio) / 1000;

    tempoElemento.textContent =
        `${tempoFinal.toFixed(2)}s`;

    if (venceu) {

        resultadoTitulo.textContent =
            "VOCÊ VENCEU!";

        resultadoInfo.textContent =
            `${movimentos} CASAS  |  ${tempoFinal.toFixed(2)}s`;

        resultadoElemento.classList.remove("escondido");

        resultadoElemento.classList.add("vitoria");

        registrarRecorde();

    } else if (perdeu) {

        resultadoTitulo.textContent =
            "VOCÊ PERDEU!";

        resultadoInfo.textContent =
            `${movimentos} CASAS  |  ${tempoFinal.toFixed(2)}s`;

        resultadoElemento.classList.remove("escondido");

        resultadoElemento.classList.add("derrota");
    }
}


/* =========================
   DESENHAR TABULEIRO
   ========================= */

function desenhar() {

    tabuleiroElemento.innerHTML = "";

    for (let linha = 0; linha < TAMANHO; linha++) {

        for (let coluna = 0; coluna < TAMANHO; coluna++) {

            /*
             * Cada casa é criada exatamente
             * da mesma maneira.
             */

            const casa = document.createElement("div");

            casa.classList.add("casa");

            const disponivel =
                tabuleiro[linha][coluna];

            if (disponivel) {

                casa.classList.add("disponivel");

                if ((linha + coluna) % 2 !== 0) {
                    casa.classList.add("escura");
                }

            } else {

                casa.classList.add("usada");
            }


            /*
             * CASA DA DAMA
             *
             * O destaque é apenas uma classe.
             * Não alteramos largura, altura,
             * posição ou grid da casa.
             */

            const eDama =
                linha === damaLinha &&
                coluna === damaColuna;

            if (eDama) {

                casa.classList.add("objetivo");
            }


            /*
             * REI
             */

            const eJogador =
                linha === jogadorLinha &&
                coluna === jogadorColuna;

            if (eJogador) {

                const imagemRei =
                    document.createElement("img");

                imagemRei.src =
                    "../assets/rei.png";

                imagemRei.classList.add("peca");

                casa.appendChild(imagemRei);
            }


            /*
             * DAMA
             */

            if (eDama) {

                const imagemDama =
                    document.createElement("img");

                imagemDama.src =
                    "../assets/dama.png";

                imagemDama.classList.add("peca");

                casa.appendChild(imagemDama);
            }


            tabuleiroElemento.appendChild(casa);
        }
    }
}


/* =========================
   HUD
   ========================= */

function atualizarHud() {

    movimentosElemento.textContent =
        movimentos;

    atualizarTempo();
}


/* =========================
   TECLADO
   ========================= */

document.addEventListener("keydown", (evento) => {

    if (
        evento.key === "ArrowUp" ||
        evento.key === "ArrowDown" ||
        evento.key === "ArrowLeft" ||
        evento.key === "ArrowRight"
    ) {

        evento.preventDefault();
    }


    if (evento.key === "ArrowUp") {

        tentarMover(-1, 0);

    } else if (evento.key === "ArrowDown") {

        tentarMover(1, 0);

    } else if (evento.key === "ArrowLeft") {

        tentarMover(0, -1);

    } else if (evento.key === "ArrowRight") {

        tentarMover(0, 1);

    } else if (
        evento.key.toLowerCase() === "r" &&
        (venceu || perdeu)
    ) {

        reiniciarJogo();
    }
});

/* =========================
   CONTROLES MOBILE
========================= */

btnCima.addEventListener("click", () => {
    tentarMover(-1, 0);
});

btnBaixo.addEventListener("click", () => {
    tentarMover(1, 0);
});

btnEsquerda.addEventListener("click", () => {
    tentarMover(0, -1);
});

btnDireita.addEventListener("click", () => {
    tentarMover(0, 1);
});

btnReiniciar.addEventListener("click", () => {
    reiniciarJogo();
});

/* =========================
   INICIAR
   ========================= */

atualizarRanking();

reiniciarJogo();