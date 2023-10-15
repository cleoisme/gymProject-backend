# Assignment 1 - 2023-10-14

## Tasks

- [x] 配置开发环境
- [x] VS Code: Django, Python Formatting Extensions Install
- [x] 根据现有需求考虑需要什么 endpoints: **Object X CRUD**

  - [x] 每个 endpoint 的 response 包括什么内容，以什么格式

  1. **Admin:**

     - List all admins: `GET /api/admins/`
       - Response: A JSON array of client objects.
     - Create a new admin: `POST /api/admins/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific admin: `GET /api/admins/<admin_id>/`
       - Response: The specific client object in JSON format.
     - Update an admin: `PUT /api/admins/<admin_id>/`
       - Response: The updated client object in JSON format.
     - Delete an admin: `DELETE /api/admins/<admin_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

  2. **Clients:**

     - List all clients: `GET /api/clients/`
       - Response: A JSON array of client objects.
     - Create a new client: `POST /api/clients/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific client: `GET /api/clients/<client_id>/`
       - Response: The specific client object in JSON format.
     - Update a client: `PUT /api/clients/<client_id>/`
       - Response: The updated client object in JSON format.
     - Delete a client: `DELETE /api/clients/<client_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

  3. **Appointments:**

     - List all appointments: `GET /api/appointments/`
       - Response: A JSON array of client objects.
     - Create a new appointment: `POST /api/appointments/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific appointment: `GET /api/appointments/<appointment_id>/`
       - Response: The specific client object in JSON format.
     - Update an appointment: `PUT /api/appointments/<appointment_id>/`
       - Response: The updated client object in JSON format.
     - Delete an appointment: `DELETE /api/appointments/<appointment_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

  4. **Notifications:**

     - List all notifications: `GET /api/notifications/`
       - Response: A JSON array of client objects.
     - Create a new notification: `POST /api/notifications/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific notification: `GET /api/notifications/<notification_id>/`
       - Response: The specific client object in JSON format.
     - Update a notification: `PUT /api/notifications/<notification_id>/`
       - Response: The updated client object in JSON format.
     - Delete a notification: `DELETE /api/notifications/<notification_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

  5. **Tasks:**

     - List all tasks: `GET /api/tasks/`
       - Response: A JSON array of client objects.
     - Create a new task: `POST /api/tasks/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific task: `GET /api/tasks/<task_id>/`
       - Response: The specific client object in JSON format.
     - Update a task: `PUT /api/tasks/<task_id>/`
       - Response: The updated client object in JSON format.
     - Delete a task: `DELETE /api/tasks/<task_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

  6. **Posts:**

     - List all posts: `GET /api/posts/`
       - Response: A JSON array of client objects.
     - Create a new post: `POST /api/posts/`
       - Response: The newly created client object in JSON format.
     - Retrieve a specific post: `GET /api/posts/<post_id>/`
       - Response: The specific client object in JSON format.
     - Update a post: `PUT /api/posts/<post_id>/`
       - Response: The updated client object in JSON format.
     - Delete a post: `DELETE /api/posts/<post_id>/`
       - Response: A success message or HTTP 204 (No Content) on success.

- [x] 根据现有需求设计 Data schema

  1. **Clients**

     ```json
     {
         "_id": ObjectId,
         "name": "Client Name",
         "email": "client@email.com",
         "phone": "123-456-7890",
         "address": "123 Main St",
         // Other client-specific fields
     }
     ```

  2. **Admins**

     ```json
     {
         "_id": ObjectId,
         "username": "admin_user",
         "password": "hashed_password",
         // Other admin-specific fields
     }
     ```

  3. **Appointments**

     ```json
     {
         "_id": ObjectId,
         "client_id": ObjectId, // Reference to the client
         "date": "YYYY-MM-DD",
         "time": "HH:MM",
         // Other appointment-specific fields
     }
     ```

  4. **Notifications**

     ```json
     {
        "_id": ObjectId,
        "message": "Notification message",
        "created_at": "Timestamp",
        // Other notification-specific fields
     }
     ```

  5. **Tasks**

     ```json
     {
         "_id": ObjectId,
         "title": "Task title",
         "description": "Task description",
         "assigned_to": ObjectId, // Reference to an admin or client
         "due_date": "YYYY-MM-DD",
         // Other task-specific fields
     }
     ```

  6. **Posts**
     ```json
     {
         "_id": ObjectId,
         "title": "Post title",
         "content": "Post content",
         "author": ObjectId, // Reference to an admin or client
         "created_at": "Timestamp",
         // Other post-specific fields
     }
     ```

- [ ]Github 上 CI/CD Pipeline Setup

## Ask

- 模拟实际工作中的标准流程
  - eg. feature proposal -> design review -> implement -> code review -> merge -> staged deployment and release
- Weekly meeting:
  - 1/2 Code review/Q&A session
  - 2/2 Presentation and overview of the next week
