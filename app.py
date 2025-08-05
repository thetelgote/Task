# import os
# import sys

# tasks = []

# def is_headless():
#     return os.environ.get("CI") == "true" or not sys.stdin.isatty()

# def show_menu():
#     print("\n--- To-Do List ---")
#     print("1. View Tasks")
#     print("2. Add Task")
#     print("3. Delete Task")
#     print("4. Exit")

# def view_tasks():
#     if not tasks:
#         print("No tasks yet.")
#     else:
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")

# def add_task():
#     task = input("Enter a new task: ")
#     tasks.append(task)
#     print("Task added.")

# def delete_task():
#     view_tasks()
#     try:
#         task_num = int(input("Enter task number to delete: "))
#         if 1 <= task_num <= len(tasks):
#             removed = tasks.pop(task_num - 1)
#             print(f"Deleted task: {removed}")
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Please enter a valid number.")

# if is_headless():
#     print("Running in non-interactive mode (CI/Kubernetes/Docker)")
#     tasks = ["Demo Task 1", "Demo Task 2"]
#     view_tasks()
#     sys.exit(0)

# while True:
#     show_menu()
#     try:
#         choice = input("Choose an option: ")
#     except EOFError:
#         print("No input stream available. Exiting.")
#         break

#     if choice == '1':
#         view_tasks()
#     elif choice == '2':
#         add_task()
#     elif choice == '3':
#         delete_task()
#     elif choice == '4':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option. Try again.")c




from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)
tasks = []

# Inline HTML using Jinja2
HTML = """
<!doctype html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body { font-family: Arial; background-color: #f4f4f4; padding: 20px; }
        h1 { color: #333; }
        ul { padding: 0; }
        li { background: #fff; margin: 5px 0; padding: 10px; list-style: none; border-radius: 4px; }
        form { margin-top: 20px; }
        input[type=text] { padding: 8px; width: 250px; }
        button { padding: 8px 12px; }
    </style>
</head>
<body>
    <h1>📝 To-Do List</h1>
    <ul>
        {% for task in tasks %}
        <li>{{ loop.index }}. {{ task }} 
            <a href="/delete/{{ loop.index0 }}">❌</a>
        </li>
        {% endfor %}
    </ul>
    <form method="POST">
        <input type="text" name="task" placeholder="Add new task" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect('/')
    return render_template_string(HTML, tasks=tasks)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# from flask import Flask, jsonify
# import bugsnag
# from bugsnag.flask import handle_exceptions

# # Configure Bugsnag
# bugsnag.configure(
#     api_key="a8e5e961c365880e96b5145b2978526f",
#     project_root="."
# )

# app = Flask(__name__)
# handle_exceptions(app)

# # Sample tasks list
# tasks = ["Sample Task 1", "Sample Task 2"]

# @app.route("/")
# def index():
#     return "Todo App is live!"

# @app.route("/tasks")
# def get_tasks():
#     return jsonify({"tasks": tasks})

# @app.route("/error")
# def trigger_error():
#     raise Exception("This is a test error for Bugsnag!")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
