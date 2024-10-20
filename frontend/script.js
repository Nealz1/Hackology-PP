const ctx1 = document.getElementById('chart1').getContext('2d');
        const chart1 = new Chart(ctx1, {
            type: 'pie',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    data: [30, 50, 70, 40, 60, 90],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)', 'rgba(255, 206, 86, 0.6)']
                }]
            }
        });

        const ctx2 = document.getElementById('chart2').getContext('2d');
        const chart2 = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    label: 'Sprzedaż w tysiącach (PLN)',
                    data: [100, 150, 200, 170, 190, 220],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

        const ctx3 = document.getElementById('chart3').getContext('2d');
        const chart3 = new Chart(ctx3, {
            type: 'bar',
            data: {
                labels: ['Mazowieckie', 'Wielkopolskie', 'Małopolskie', 'Pomorskie', 'Śląskie'],
                datasets: [{
                    label: 'Sprzedaż w regionach (szt.)',
                    data: [300, 200, 180, 220, 260],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { y: { beginAtZero: true } }
            }
        });

        // Wykresy dla chleba
        const ctx4 = document.getElementById('chart4').getContext('2d');
        const chart4 = new Chart(ctx4, {
            type: 'pie',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    data: [50, 70, 60, 40, 90, 80],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)', 'rgba(255, 206, 86, 0.6)']
                }]
            }
        });

        const ctx5 = document.getElementById('chart5').getContext('2d');
        const chart5 = new Chart(ctx5, {
            type: 'line',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    label: 'Sprzedaż w tysiącach (PLN)',
                    data: [90, 120, 150, 140, 130, 160],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

        const ctx6 = document.getElementById('chart6').getContext('2d');
        const chart6 = new Chart(ctx6, {
            type: 'bar',
            data: {
                labels: ['Mazowieckie', 'Wielkopolskie', 'Małopolskie', 'Pomorskie', 'Śląskie'],
                datasets: [{
                    label: 'Sprzedaż w regionach (szt.)',
                    data: [250, 180, 200, 210, 230],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { y: { beginAtZero: true } }
            }
        });

        // Wykresy dla laptopa
        const ctx7 = document.getElementById('chart7').getContext('2d');
        const chart7 = new Chart(ctx7, {
            type: 'pie',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    data: [10, 20, 30, 15, 25, 35],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)', 'rgba(255, 206, 86, 0.6)']
                }]
            }
        });

        const ctx8 = document.getElementById('chart8').getContext('2d');
        const chart8 = new Chart(ctx8, {
            type: 'line',
            data: {
                labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'],
                datasets: [{
                    label: 'Sprzedaż w tysiącach (PLN)',
                    data: [500, 600, 700, 650, 720, 780],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderWidth: 2,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

        const ctx9 = document.getElementById('chart9').getContext('2d');
        const chart9 = new Chart(ctx9, {
            type: 'bar',
            data: {
                labels: ['Mazowieckie', 'Wielkopolskie', 'Małopolskie', 'Pomorskie', 'Śląskie'],
                datasets: [{
                    label: 'Sprzedaż w regionach (szt.)',
                    data: [150, 130, 170, 180, 200],
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { y: { beginAtZero: true } }
            }
        });