# Course Management Microservices

| Service | Responsibility | Endpoints | Database |
|----------|---------------|-----------|----------|
| Course Service | Course CRUD | /api/courses | course.db |
| Student Service | Student CRUD, Enrollment | /api/students | student.db |
| Auth Service | Login, Registration, JWT | /api/auth | auth.db |
| Notification Service | Email Notifications | /api/notifications | notification.db |

## Architecture

Gateway (Port 5000)

↓

Course Service (Port 5001)

↓

Student Service (Port 5002)

Each service owns its own database.

No service directly accesses another service's database.

Inter-service communication happens using HTTP requests.

## Synchronous vs Asynchronous

### Synchronous (HTTP)

Advantages

- Easy to implement
- Immediate response
- Simple debugging

Disadvantages

- Tight coupling
- Service downtime affects others
- Higher latency

### Asynchronous (RabbitMQ / Kafka)

Advantages

- Loose coupling
- Better scalability
- High reliability

Disadvantages

- Eventual consistency
- More infrastructure
- Harder debugging
