// Lista de moedas
const currencies = ["USD","EUR","BRL","JPY","AUD","CAD","CHF","CNY","GBP","ARS","CLP","MXN","INR","ZAR","KRW","NZD"];

// Preencher dropdowns automaticamente
function loadCurrencies() {
    let base = document.getElementById("base");
    let target = document.getElementById("target");

    currencies.forEach(c => {
        base.innerHTML += `<option value="${c}">${c}</option>`;
        target.innerHTML += `<option value="${c}">${c}</option>`;
    });

    base.value = "USD";
    target.value = "EUR";
}

loadCurrencies();

let chartHistory = null;
let chartCompare = null;

// Submeter busca SEM RELOAD
document.getElementById("currencyForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const base = document.getElementById("base").value;
    const target = document.getElementById("target").value;

    // Buscar taxa atual
    const response = await fetch(`/currency/fetch/?base=${base}&target=${target}`);
    const data = await response.json();

    const result = document.getElementById("result");
    result.classList.remove("d-none");
    result.innerHTML = `<strong>1 ${base}</strong> = <strong>${data.rate}</strong> ${target}`;

    // Atualizar gráficos
    loadCharts(base, target);
});

// GRÁFICO HISTÓRICO FILTRADO
async function loadCharts(base = "USD", target = "EUR") {

    // Busca correta: BASE + TARGET
    const res = await fetch(`/api/rates/?base=${base}&target=${target}`);
    const data = await res.json();

    const labels = data.map(i => i.created_at.split("T")[0]);
    const rates = data.map(i => i.rate);

    // ----- HISTÓRICO -----
    if (chartHistory) chartHistory.destroy();

    chartHistory = new Chart(document.getElementById("chart"), {
        type: "line",
        data: {
            labels,
            datasets: [{
                label: `Histórico ${base} → ${target}`,
                data: rates,
                borderWidth: 2,
            }]
        }
    });

    // ----- COMPARATIVO -----
    if (chartCompare) chartCompare.destroy();

    chartCompare = new Chart(document.getElementById("chartCompare"), {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: `Variação ${base} → ${target}`,
                data: rates,
                borderWidth: 2,
            }]
        }
    });
}
loadCharts();
