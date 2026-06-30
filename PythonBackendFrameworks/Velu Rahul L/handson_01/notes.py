"""
Task 1 : Request–Response Cycle

Browser
    │
    ▼
URL Router (urls.py)
    │
    ▼
Middleware (process_request)
    │
    ▼
View (views.py)
    │
    ▼
Model (Database Query)
    │
    ▼
View prepares HttpResponse
    │
    ▼
Middleware (process_response)
    │
    ▼
Browser


-----------------------------------------------------

Middleware

Middleware sits between the incoming request and the view,
and again between the response and the browser.

Examples

1. AuthenticationMiddleware
   Identifies the logged-in user.

2. SessionMiddleware
   Handles user sessions.


-----------------------------------------------------

WSGI vs ASGI

WSGI
-----
• Synchronous interface
• Handles one request at a time
• Default deployment interface in Django

ASGI
-----
• Asynchronous interface
• Supports WebSockets
• Supports long-lived connections
• Better for chat applications and real-time apps

Use ASGI when building:

• Chat applications
• Notifications
• Live dashboards
• WebSocket applications


-----------------------------------------------------

MVC vs Django MVT

MVC

Model
View
Controller


Django MVT

Model  -> Model

View -> Controller

Template -> View

Django's View performs the work of the Controller in MVC.
"""
