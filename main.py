import json
from datetime import datetime 

        
def load_tasks():
      try:
         with open('tasks.json', 'r') as f:
            all_task = json.load(f)
      except (FileNotFoundError, json.JSONDecodeError):
            all_task = []
      return all_task

def save_tasks(all_task):
      with open('tasks.json', 'w') as f:
         json.dump(all_task, f, indent=2)

def status_valid_input():
   valid_status = ['todo', 'in-progress', 'done']

   while True:
      status = input('status (todo / in-progress / done)').lower()
      if status in valid_status:
         return status
      else:
         print('Invalid status, choose form: ', valid_status)

def get_valid_task_id(all_task):
    if not all_task:
      print('No task to update!')
      return None
    
    ids = [task['id'] for task in all_task]
    while True:
      try:
         task_id = int(input('Enter task id: '))
         if task_id in ids:
            return task_id
         else:  
            print('Task id not found, choose form: ', ids)
      except (ValueError):
         print("Invalid input please enter a valid value!")

def add_task():
      description = input("description: ")
      status = status_valid_input()

      all_task = load_tasks()

      if not all_task:
         unique_id = 1
      else:
         unique_id = int(all_task[-1]['id']) + 1

      new_task = {
      'id': unique_id,
      'description': description,
      'status': status,
      'createdAt': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
      'updatedAt': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      }

      all_task.append(new_task)

      save_tasks(all_task)


def view_tasks():
   all_task = load_tasks()

   if not all_task:
         print('There are no tasks!')
   else:
      for task in all_task:
         print(f"id : {task['id']} | task_description : {task['description']} | status :  {task['status']} | Creation_time : {task['createdAt']} | Update_time : {task['updatedAt']}")

def update_task():
   all_task = load_tasks()

   if not all_task:
         print('There are no tasks to update!')
   else:
      for task in all_task:
         print(f"Task id: {task['id']}\nDescription: {task['description']}")
      
      update_id = get_valid_task_id(all_task)
      if update_id is None:
         return

      found = False

      for task in all_task:
         if task['id'] == update_id:
            found = True
            task['description'] = input('Enter the new descrition for the task: ')
            task['status'] = status_valid_input()
            task['updatedAt'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            break

      if found == True:
         save_tasks(all_task)
      else:
         print('Task not found')

def delete_task():
      all_task = load_tasks()

      for task in all_task:
         print(f"Task id: {task['id']}, Description: {task['description']}, Status: {task['status']}") # viewing it
         
      delete_id = get_valid_task_id(all_task)
      if delete_id is None:
         return

      found = False

      for task in all_task:
         if delete_id == task['id']:
            found = True
            all_task.remove(task)
            break
      
      if found == True:
        save_tasks(all_task)
      else:
         print('Enter a valid i_d!')


      
def main():
   while True:

      print('''Welcome To Task_Tracker

      Menu:
      1. Add Task (add)
      2. View Tasks (view)
      3. Update Task (update)
      4. Delete Task (delete)
      5. Exit (exit)
      ''')

      user_input = input('Choose your option: ').lower()


      # ADDING  
      if user_input == 'add':
         add_task()
      # VIEWING
      elif user_input == 'view':
         view_tasks()
      # UPDATING
      elif user_input == 'update':
         update_task()
      # DELETING
      elif user_input == 'delete':
         delete_task()
      elif user_input == 'exit':
         print('Byy 🤡')
         break
      else:
         print('Choose the valid option')

if __name__ == "__main__":
   main()

