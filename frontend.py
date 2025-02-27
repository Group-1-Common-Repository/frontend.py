import flet as ft
import requests

API_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "TrustLocal - Business Directory"
    
    # UI Elements
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True)
    register_btn = ft.ElevatedButton("Register", on_click=lambda e: register_user(username.value, password.value))
    login_btn = ft.ElevatedButton("Login", on_click=lambda e: login_user(username.value, password.value))
    
    business_name = ft.TextField(label="Business Name")
    category = ft.TextField(label="Category")
    location = ft.TextField(label="Location")
    owner = ft.TextField(label="Owner")
    add_business_btn = ft.ElevatedButton("Add Business", on_click=lambda e: add_business(business_name.value, category.value, location.value, owner.value))
    
    business_list = ft.ListView(expand=True)
    refresh_businesses_btn = ft.ElevatedButton("Refresh Businesses", on_click=lambda e: fetch_businesses(business_list))

    # Add elements to the page
    page.add(ft.Text("User Authentication"), username, password, register_btn, login_btn)
    page.add(ft.Text("Add Business"), business_name, category, location, owner, add_business_btn)
    page.add(ft.Text("Business Listings"), refresh_businesses_btn, business_list)

def register_user(username, password):
    response = requests.post(f"{API_URL}/register", json={"username": username, "password": password})
    print(response.json())

def login_user(username, password):
    response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
    print(response.json())

def add_business(name, category, location, owner):
    response = requests.post(f"{API_URL}/businesses", json={"name": name, "category": category, "location": location, "owner": owner})
    print(response.json())

def fetch_businesses(business_list):
    response = requests.get(f"{API_URL}/businesses")
    business_list.controls.clear()
    for business in response.json():
        business_list.controls.append(ft.Text(f"{business['name']} - {business['category']} ({business['location']})"))
    business_list.update()

ft.app(target=main)
