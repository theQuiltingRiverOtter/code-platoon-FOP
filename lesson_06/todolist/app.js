document.querySelector("#create").addEventListener("click", addTask)
const ol = document.querySelector("ol");
let allSpans = document.querySelectorAll("span");
allSpans.forEach(span => span.addEventListener('click', removeTask));

let tasks = JSON.parse(localStorage.getItem('tasks'));
if (tasks == null) {
    tasks = [];
}
displayTasks();

function addTask() {
    let newTask = document.querySelector("#newToDo").value;
    if (newTask !== "") {
        let rId = crypto.randomUUID();
        console.log(rId);
        tasks.push({ id: rId, task: newTask, completed: false });
        displayTasks();
        document.querySelector("#newToDo").value = ''
    }
}

function removeTask(e) {
    console.log(e.target);
    let node = e.target.parentNode;
    let taskId = node.id;
    tasks = tasks.filter(item => item.id != taskId);
    displayTasks();
}
function toggleCompleted(e) {
    let taskId = e.target.id;
    tasks = tasks.map(item => {
        if (taskId == item.id) {
            return { ...item, completed: !item.completed }
        } else {
            return { ...item }
        }

    })
    displayTasks();
}

function displayTasks() {
    ol.innerHTML = '';
    if (tasks.length == 0) {
        ol.style.display = 'none'

    }
    for (let item of tasks) {
        const li = document.createElement("li");
        li.classList.add('list-group-item');
        li.classList.add("d-flex");
        li.classList.add('justify-content-between');
        li.classList.add("align-items-center")
        //create checkbox
        const textItem = document.createElement("span");
        textItem.classList.add("d-flex");
        textItem.classList.add('justify-content-between');
        textItem.classList.add("align-items-center")
        textItem.setAttribute("id", item.id);
        textItem.innerText = item.task;
        textItem.addEventListener('click', toggleCompleted)
        if (item.completed) {
            textItem.style.textDecoration = 'line-through';
        }
        li.appendChild(textItem);

        //create trashcan
        const span = document.createElement("span");
        span.setAttribute("id", item.id);
        span.addEventListener("click", removeTask);
        span.classList.add('bg-purple');
        span.innerHTML = '<i class="bi bi-x-circle"></i>'
        li.appendChild(span);

        //append li
        ol.appendChild(li);
    }

    localStorage.setItem('tasks', JSON.stringify(tasks))
}
