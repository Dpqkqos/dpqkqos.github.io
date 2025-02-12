document.addEventListener("DOMContentLoaded", function() {
    // Элемент таблицы для обновления состояния
    const stateTable = document.getElementById('states-tbody');

    // Функция для обновления таблицы
    function updateStateTable(state, date) {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${date}</td><td>${state}</td>`;
        stateTable.appendChild(row);
    }

    // Запрос на сервер для получения состояния
    fetch("/user-state/{chat_id}/")
        .then(response => response.json())
        .then(data => {
            if (data.user_state) {
                // Обновляем таблицу с текущим состоянием
                updateStateTable(data.user_state.state, data.user_state.date);
            } else {
                // Если состояния нет, выводим "Не заполнено"
                updateStateTable("Не заполнено", "Сегодня");
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});