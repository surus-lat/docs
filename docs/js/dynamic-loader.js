async function fetchModelsAndPricingsFromAPI() {
    const apiUrl = 'https://api.gradientesur.com/functions/v1/models';
    // IMPORTANT: Security reminder - this endpoint should be public or use a secure client-side auth method.
    // Do not embed sensitive API keys here.
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`API request failed: ${response.status} ${response.statusText}`);
        }
        const jsonData = await response.json();
        return jsonData.data; // Assuming your API wraps models in a "data" array
    } catch (error) {
        console.error('Failed to fetch data from API:', error);
        return null; 
    }
}

function renderModelsTable(models, containerElement) {
    if (!models || models.length === 0) {
        containerElement.innerHTML = '<p>No hay modelos disponibles en este momento o no se pudieron cargar.</p>';
        return;
    }

    let tableHtml = `
        <p>Consultá los modelos disponibles también usando el endpoint <code>/functions/v1/models</code>.</p>
        <table>
          <thead>
            <tr>
              <th>Modelo</th>
              <th>Descripción</th>
            </tr>
          </thead>
          <tbody>
    `;
    models.forEach(model => {
        tableHtml += `
          <tr>
            <td>${model.name || 'N/A'}</td>
            <td>${model.description || 'N/A'}</td>
          </tr>
        `;
    });
    tableHtml += `
          </tbody>
        </table>
    `;
    containerElement.innerHTML = tableHtml;
}

function renderPricingsTable(models, containerElement) {
    if (!models || models.length === 0) {
        containerElement.innerHTML = '<p>No hay información de precios disponible en este momento o no se pudo cargar.</p>';
        return;
    }

    const sections = [
        {
            title: "Texto",
            types: ["text"],
            columns: ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            rows: []
        },
        {
            title: "Visión",
            types: ["vision", "image"],
            columns: ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            rows: []
        },
        {
            title: "Audio",
            types: ["audio"],
            columns: ["Modelo", "Precio por segundo de entrada", "Precio por segundo de salida"],
            rows: []
        },
        {
            title: "Embeddings",
            types: ["embedding", "embeddings"],
            columns: ["Modelo", "Precio por token de entrada"],
            rows: []
        }
    ];
    
    const formatPrice = (price) => (price !== undefined && price !== null) ? `$${Number(price).toFixed(2)}` : "-";

    models.forEach(m => {
        const mtype = m.type ? m.type.toLowerCase() : "";
        const p = m.pricing || {};
        for (const section of sections) {
            if (section.types.includes(mtype)) {
                // Adjust the 'p.PROPERTY_NAME' accessors below to match your API's pricing fields
                if (section.title === "Texto" || section.title === "Visión") {
                    section.rows.push([
                        m.name || 'N/A',
                        formatPrice(p.input_price_per_million_tokens || p.input),
                        formatPrice(p.output_price_per_million_tokens || p.output)
                    ]);
                } else if (section.title === "Audio") {
                     section.rows.push([
                        m.name || 'N/A',
                        formatPrice(p.input_price_per_second || p.input),
                        formatPrice(p.output_price_per_second || p.output)
                    ]);
                } else if (section.title === "Embeddings") {
                    section.rows.push([
                        m.name || 'N/A',
                        formatPrice(p.input_price_per_token || p.input)
                    ]);
                }
                break;
            }
        }
    });

    let htmlContent = "";
    sections.forEach(section => {
        htmlContent += `<h2>${section.title}</h2>`;
        htmlContent += '<table><thead><tr>';
        section.columns.forEach(col => htmlContent += `<th>${col}</th>`);
        htmlContent += '</tr></thead><tbody>';
        if (section.rows.length > 0) {
            section.rows.forEach(rowData => {
                htmlContent += '<tr>';
                rowData.forEach(cellData => htmlContent += `<td>${cellData}</td>`);
                htmlContent += '</tr>';
            });
        } else {
            // Placeholder row for empty sections
            htmlContent += '<tr>' + section.columns.map(() => '<td>-</td>').join('') + '</tr>';
        }
        htmlContent += '</tbody></table><br/>';
    });
    htmlContent += '<hr/>';
    containerElement.innerHTML = htmlContent;
}

document.addEventListener('DOMContentLoaded', async () => {
    const modelosContainer = document.getElementById('modelos-table-container');
    const pricingsContainer = document.getElementById('pricings-table-container');

    if (modelosContainer || pricingsContainer) {
        if (modelosContainer) modelosContainer.innerHTML = '<p>Cargando modelos...</p>';
        if (pricingsContainer) pricingsContainer.innerHTML = '<p>Cargando precios...</p>';

        const modelsData = await fetchModelsAndPricingsFromAPI();

        if (modelsData) {
            if (modelosContainer) {
                renderModelsTable(modelsData, modelosContainer);
            }
            if (pricingsContainer) {
                renderPricingsTable(modelsData, pricingsContainer);
            }
        } else {
            const errorMessage = '<p>Error al cargar los datos. Por favor, intentá de nuevo más tarde.</p>';
            if (modelosContainer) modelosContainer.innerHTML = errorMessage;
            if (pricingsContainer) pricingsContainer.innerHTML = errorMessage;
        }
    }
});
