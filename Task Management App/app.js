const apiUrl = 'http://localhost:8080/api/tasks';

document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();
});

function fetchTasks() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('taskList');
            taskList.innerHTML = '';
            data.forEach(task => {
                const taskElement = document.createElement('li');
                taskElement.innerHTML = `
                    ${task.title} - ${task.description} 
                    <input type="checkbox" ${task.completed ? 'checked' : ''} onclick="toggleCompletion(${task.id})">
                    <button onclick="deleteTask(${task.id})">Delete</button>
                    <button onclick="editTask(${task.id}, '${task.title}', '${task.description}')">Edit</button>
                `;
                taskList.appendChild(taskElement);
            });
        });
}

function toggleCompletion(id) {
    fetch(`${apiUrl}/${id}/complete`, {
        method: 'PUT',
    }).then(() => fetchTasks());
}

function addTask() {
    const title = document.getElementById('taskTitle').value;
    const description = document.getElementById('taskDescription').value;

    const newTask = {
        title: title,
        description: description,
        completed: false
    };

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTask)
    })
    .then(response => response.json())
    .then(() => {
        fetchTasks();
        document.getElementById('taskTitle').value = '';
        document.getElementById('taskDescription').value = '';
    });
}

function editTask(id, currentTitle, currentDescription) {
    const title = prompt("Edit Task Title", currentTitle);
    const description = prompt("Edit Task Description", currentDescription);

    if (title && description) {
        const updatedTask = { title, description, completed: false };
        fetch(`${apiUrl}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedTask)
        }).then(() => fetchTasks());
    }
}

function deleteTask(id) {
    fetch(`${apiUrl}/${id}`, {
        method: 'DELETE'
    }).then(() => fetchTasks());
}
