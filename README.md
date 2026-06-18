# MySite 2026

Welcome to the **mysite2026** Django project repository.

---

## API Endpoints Documentation

Here is the list of available URLs, including their HTTP methods, expected parameters, and HTTP status codes.

| URL Path | HTTP Method | Request Payload / Format | Response Format | Status Code (Success) | Status Code (Error) | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `/` | `GET` | None | HTML | `200 OK` | - | Displays the default Django congratulations welcome page. |
| `/info` | `GET` | None | HTML | `200 OK` | - | Displays the client's IP address and detailed request HTTP headers. |
| `/hello` | `GET` | None | HTML | `200 OK` | - | Renders the greeting form input page. |
| `/hello` | `POST` | Form-data: `name=value` <br>or JSON: `{"name": "value"}` | HTML | `200 OK` | - | Greets the user with "Hello, [Name]". |
| `/quiz/question` | `GET` | None | JSON | `200 OK` | `400 Bad Request` (If not GET) | Returns a predefined quiz question in JSON format. |
| `/quiz/question/create` | `POST` | JSON: `{"id": int, "text": string, "choices": [...]}` | JSON | `200 OK` | `400 Bad Request` (If not POST or invalid JSON) | Receives a new quiz question payload and echoes it back. |

---

## Endpoint Response Examples

### 1. `/info` (GET)
- **Response Status**: `200 OK`
- **Output**:
  ```html
  Your IP Address is: 10.255.65.80
  Content-Length: ...
  Content-Type: ...
  Host: 10.255.65.80
  ...
  ```

### 2. `/hello` (POST)
- **Request Parameters**: `name=Antigravity`
- **Response Status**: `200 OK`
- **Output**: Beautiful HTML page with text `Hello, Antigravity`

### 3. `/quiz/question` (GET)
- **Response Status**: `200 OK`
- **Output**:
  ```json
  {"id": 1, "text": "ประเทศไทยมีกี่จังหวัด", "choices": [50, 68, 72, 77]}
  ```

### 4. `/quiz/question/create` (POST)
- **Request Payload**:
  ```json
  {"id": 9, "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล", "choices": ["C", "C++", "C#", "Python", "R", "Julia"]}
  ```
- **Response Status**: `200 OK`
- **Output**:
  ```json
  {"id": 9, "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล", "choices": ["C", "C++", "C#", "Python", "R", "Julia"]}
  ```

---

## Local Dev Server

Start the Django development server on your machine:

- Run on Port 80 (default HTTP):
  ```powershell
  .venv\Scripts\python.exe manage.py runserver 0.0.0.0:80
  ```
- Run on Port 8000:
  ```powershell
  .venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000
  ```