
function mostrarGrafico(container, checksTotales, checksCompletados) {
    container.find('#myChart').html('');

    // CALCULATE
    var porcentajeCompletado = (checksCompletados / checksTotales) * 100;

    // CHART
    var progressHTML = `
        <div class="progress">
            <div class="progress-bar bg-success" role="progressbar" style="width: ${porcentajeCompletado}%" aria-valuenow="${porcentajeCompletado}" aria-valuemin="0" aria-valuemax="100">
                ${Math.floor(porcentajeCompletado)}%
            </div>
        </div>
    `;

    container.find('#myChart').html(progressHTML);
}