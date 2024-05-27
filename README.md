# StudyBud

StudyBud is an interactive web application designed to facilitate collaborative learning and interaction among users interested in various programming topics. The platform allows users to create and join study rooms, follow topics of interest, and engage in discussions with other members.

![StudyBud](https://github.com/harry9425/likeus/assets/101708836/2660eee7-b900-4212-b2a9-a44bac51a5df)

## Features

### User Authentication
- User login and registration functionalities.
- Secure authentication mechanism to protect user data.

### Study Rooms
![Study Rooms](https://github.com/harry9425/likeus/assets/101708836/786c8752-0f27-4809-b7ab-404b8b344f1f)
- Users can create new study rooms on specific topics.
- Each study room displays the host, topic, and list of members who have joined.
- Users can join existing rooms to participate in discussions.

### Topic Management
- A list of topics is available for users to browse and follow.
- Topics include Python, HTML, JavaScript, ReactJS, NextJS, AWS, Appwrite, and C#.

### User Interface
- A modern and intuitive interface created using ReactJS and styled with CSS.
- Responsive design ensuring compatibility across various devices and screen sizes.

### Backend Services
![Backend Services](https://github.com/harry9425/likeus/assets/101708836/29e19752-65f8-4851-a099-734b091d0df4)
- Developed using Django, a high-level Python web framework.
- RESTful APIs created using Django REST framework to handle frontend-backend communication.
- CRUD operations for managing study rooms, topics, and user interactions.

### Database
- AWS DynamoDB is used as the primary database, offering fast and scalable data storage.
- Efficient handling of user data, room details, and topic information.

### Real-time Updates
- Real-time data updates and notifications to enhance user engagement.
- Recent activities section displaying the latest interactions such as replies and room creation.

## Detailed Functionality

### Browse Topics
![Browse Topics](https://github.com/harry9425/likeus/assets/101708836/73167717-5d28-4de6-b3bb-63d4b5794bc0)
- Users can browse through a list of available topics on the left sidebar.
- Each topic shows the number of active rooms.

### Rooms
- The main section displays all available study rooms.
- Each room card shows the room title, host information, and the number of members joined.
- Users can click on a room to view detailed discussions and participate.

### Top Hosts
- A sidebar section highlighting top hosts based on activity and engagement.
- Users can follow top hosts to stay updated with their activities.

### Recent Activities
![Recent Activities](https://github.com/harry9425/likeus/assets/101708836/6c29eb11-77c6-4227-a22c-efb7416a463b)
- Displays the latest activities such as replies to posts and new room creations.
- Provides quick insights into active discussions and popular rooms.

## Implementation Details

### Frontend
![Frontend](https://github.com/harry9425/likeus/assets/101708836/86e90b88-7930-47ed-ab50-8514646e60c2)
- Built with ReactJS to create a dynamic and responsive user interface.
- CSS is used for styling to ensure a visually appealing design.
- State management and component-based architecture for efficient rendering and performance.

### Backend
- Django serves as the backbone, providing robust and secure backend services.
- Django REST framework is used to build RESTful APIs for seamless communication with the frontend.
- Authentication and permission classes ensure secure access to data and functionalities.

### Database
- AWS DynamoDB is chosen for its scalability and low-latency data access.
- Structured to store user information, room details, and topic metadata efficiently.

### Hosting and Deployment
- The application is hosted on AWS, ensuring high availability and reliability.
- AWS services such as EC2 and S3 might be used for hosting frontend and backend services.

## Future Enhancements
- **Real-time Chat**: Implementing WebSockets for real-time chat functionality within study rooms.
- **Advanced Search**: Enhancing the search functionality to allow filtering by topics, hosts, and activity.
- **Mobile Application**: Developing a mobile app version to reach a broader audience.
- **Gamification**: Introducing badges and rewards to encourage user participation and engagement.

## Conclusion
StudyBud is a comprehensive platform designed to bring together learners and enthusiasts of various programming languages and technologies. By leveraging the power of Django, ReactJS, and AWS DynamoDB, the application offers a seamless and engaging user experience. The project exemplifies modern web development practices, ensuring scalability, performance, and usability.

---

Feel free to modify or expand on this description based on additional details or specific features you have implemented in your project.
