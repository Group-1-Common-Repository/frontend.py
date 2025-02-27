# TrustLocal - Frontend Setup (`frontend.py`)

This **Flet-based desktop application** serves as the **user interface** for **TrustLocal**, allowing users to **register, log in, add businesses, and view business listings**. It interacts with the **FastAPI backend** through **HTTP requests**.

---

## Prerequisites
Before running the frontend, ensure you have the following installed:

- **Python 3.8+**
- **TrustLocal Backend (`backend.py`) running on `http://127.0.0.1:8000`**
- **Pip package manager**

---

## Install Required Dependencies
Open a terminal and install the required Python libraries:

```sh
pip install flet requests
```

- `flet` → Used for building the graphical desktop UI
- `requests` → Used for sending API requests to the backend

---

## Ensure the Backend is Running
The frontend depends on the FastAPI backend. Start the backend before launching the frontend:

```sh
uvicorn backend:app --reload
```

Once started, the API should be accessible at **`http://127.0.0.1:8000`**.

---

## Run the Flet Frontend Application
Start the **Flet desktop app** by running:

```sh
python frontend.py
```

This will open a **graphical user interface** where users can interact with the system.

---

## UI Features & Functions

### User Authentication
- **Register a new user**
  1. Enter **username** and **password** in the respective text fields.
  2. Click **"Register"** to create an account.
  3. The response will be displayed in the **console**.

- **Log in as an existing user**
  1. Enter **username** and **password**.
  2. Click **"Login"** to authenticate.
  3. The response will be displayed in the **console**.

---

### Business Listings
- **Add a Business**
  1. Enter **business name, category, location, and owner**.
  2. Click **"Add Business"** to store it in the database.
  3. A success message will be displayed in the **console**.

- **View all Businesses**
  1. Click **"Refresh Businesses"** to fetch all listings from the backend.
  2. Businesses will be displayed in a **list view** in the app.


