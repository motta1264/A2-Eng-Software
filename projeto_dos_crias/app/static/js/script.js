document.getElementById("taskForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;

  await fetch("/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description })
  });

  document.getElementById("title").value = "";
  document.getElementById("description").value = "";
  loadTasks();
});

async function loadTasks() {
  const res = await fetch("/tasks");
  const tasks = await res.json();
  const list = document.getElementById("taskList");
  list.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = `${task.title} - ${task.description}`;
    list.appendChild(li);
  });
}

loadTasks();
