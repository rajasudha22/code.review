class TaskService:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description):
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def update_task(self, task_id, title, description, completed):
        task = self.tasks.get(task_id)
        if task:
            task.update({"title": title, "description": description, "completed": completed})
            return task
        return None

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None) is not None

    def get_all_tasks(self):
        return list(self.tasks.values())