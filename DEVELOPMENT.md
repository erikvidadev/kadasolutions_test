**1. Crate Virtual Environment**
 ```bash
   python3.11 -m venv .ve
   ```

**2. Activate Virtual Environment**
 ```bash
   . .ve/bin/activate
   ```

**3. Install Requirements**
 ```bash
   pip install -r requirements.txt
   ```


## Run Tests

**1. Run App Locally**
 ```bash
   pytest tests
   ```


## Run FastAPI APP

**1. Run App Locally**

 ```bash
   uvicorn src.main:app --reload
   ```

**2. Access The API**

 ```bash
   http://127.0.0.1:8000/docs
   ```

**3. Input description to create tasks**

 ```bash
   {
  "title": "title of the task",
  "description": "description of the task",
  "due_date": "due date of the task",
  "status": "current status of the task (pending, in_progress, completed)"
}
   ```

**4. Example input to create a task**

 ```bash
 {
  "title": "Nice Title",
  "description": "Nice Description",
  "due_date": "2030-03-17T19:57:04.783Z",
  "status": "in_progress"
}
   ```