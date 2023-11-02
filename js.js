document.getElementById('criarRequisicoes').addEventListener('click', function() {
    let currentID = 1; 

    for (let i = 1; i <= 2; i++) {

        const order = {
            ID: currentID,                 
            Price: (Math.random() * 100).toFixed(2), 
            Tax: (Math.random() * 10).toFixed(2)    
        };

        fetch('http://localhost:8000/receber_dados', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(order)
        })
        .then(response => response.json())
        .then(data => {
            console.log(`Requisição ${i} enviada com sucesso:`, data);
        })
        .catch(error => {
            console.error(`Erro na requisição ${i}:`, error);
        });
        currentID++;
    }
});
