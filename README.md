# Hero's Personal Training

Hero's Personal Training is a comprehensive web application designed to help users manage their fitness journey through personalized training and nutrition plans. Users can create and manage bookings for personal training sessions, track their progress, and receive customized workout and nutrition advice. The application also allows trainers to manage their clients and schedules efficiently.

[Live Site - Hero's Personal Training](LINK)

![Mock Up](docs/readme_images/)

## Table of Contents
- [Hero's Personal Training](#heros-personal-training)
  - [Table of Contents](#table-of-contents)
  - [User Experience Design](#user-experience-design)
    - [Project Goals](#project-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
  - [Database Design](#database-design)
  - [Security](#security)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Running Locally](#running-locally)
  - [Credits](#credits)

## User Experience Design

### Project Goals

- Provide a user-friendly interface for booking and managing personal training sessions.
- Enable trainers to manage their schedules and client information efficiently.
- Offer personalized training and nutrition plans to users.
- Ensure the application is accessible on various devices, including desktops, tablets, and smartphones.

### Target Audience

- Individuals looking for personalized fitness and nutrition plans.
- Personal trainers who need an efficient way to manage their clients and schedules.
- Fitness enthusiasts who want to track their progress and achieve their fitness goals.

### User Stories

#### Epic 1: Base Setup

- As a developer, I need to set up the project so that it is ready for implementing core features.
- As a developer, I need to create the base.html page and structure so that other pages can reuse the layout.
- As a developer, I need to create static resources so that images, CSS, and JavaScript work on the website.
- As a developer, I need to create the footer with social media links and contact information.
- As a developer, I need to create the navbar so that users can navigate the website from any device.

#### Epic 2: Standalone Pages

- As a developer, I need to implement a 404 error page to alert users when they access a non-existent page.
- As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.
- As a developer, I need to implement a 403 error page to redirect unauthorized users.
- As a site owner, I would like a home page so that customers can view information about my services.

#### Epic 3: Authentication

- As a developer, I need to implement allauth so that users can sign up and have access to the website's features.
- As a site owner, I want users to verify their email when registering an account.
- As a site owner, I would like the allauth pages customized to fit the site's styling.

#### Epic 4: Booking Management 

- As a user, I would like to create a new booking when I want to schedule a training session.
- As a user, I would like to view my bookings to check the details.
- As a user, I would like to edit a booking to make changes when needed.
- As a user, I would like to delete a booking when I no longer need it.
- As a trainer, I want to be able to view all bookings to manage my schedule.

#### Epic 5: Deployment

- As a developer, I need to set up Whitenoise to serve static files in deployment.
- As a developer, I need to deploy the project to Heroku to make it live for users.

#### Epic 6: Documentation

- Complete README documentation
- Complete testing documentation write-up


The Kanban board was created using GitHub projects and can be viewed [here](https://github.com/users/defridge/projects/2/views/1). The epics are organized into labels: To Do, In Progress, and Done. All user stories have a set of acceptance criteria that confirm when the stories have been completed.

## Features

### Implemented Features

1. **User Authentication:** 
   - User registration and login.
   - Password reset functionality.
   - Secure authentication using Django Allauth.

2. **Booking Management:**
   - Book personal training sessions.
   - View, edit, and cancel bookings.
   - Trainers can view all bookings.

3. **Responsive Design:**
   - Accessible on desktops, tablets, and smartphones.

### Features Left to Implement

1. **Social Media Integration:**
   - Allow users to share their progress on social media platforms.

2. **In-App Messaging:**
   - Enable communication between trainers and clients within the app.

3. **Advanced Analytics:**
   - Provide detailed analytics and insights on user progress and performance.

4. **Training and Nutrition Plans:**
   - Personalized training plans based on user goals.
   - Customized nutrition advice.

5. **Progress Tracking:**
   - Log workouts and track progress.
   - View progress over time with visual charts.

## Technologies Used

- **Frontend:**
  - HTML5, CSS3
  - Bootstrap 5

- **Backend:**
  - Python, Django

- **Database:**
  - PostgreSQL

- **Version Control:**
  - Git, GitHub

- **Deployment:**
  - Heroku
