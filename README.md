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

1. **Site Navigation/Nav Menu:** 
   - ``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device.``
   - The navigation menu contains links for Home, Create Booking, Manage Bookings, Sign Up, and Sign in (If the user hasnt signed in).
   - If the user has sign in the links shown will be Home, Create Booking, Manage Bookings, and Sign Out.
   - The links are displayed on all pages and the navigation menu collapses into the hamburger menu on smaller devices.

  ![Mock Up](docs/readme_images/)

2. **Home Page:**
   - ``USER STORY - As a site owner, I would like a home page so that customers can view information about my services.``
   - When the app is loaded from the url the user is brought to the app home page.
   - The home page is made up of 5 sections:
      1. Hero Section - The hero section is a the top of the home page and includes a welcome message, and a "Book Session" button.
      2. About Me Section - Next we have a section that provides info and background about the trainer/trainers.
      3. Service Details Section - Provides the user with all the info on the services provided by the trainer/trainers.
      4. Testimonials Section - Client testimonials are displayed here.
      5. Call to Action Section - Displays company tag line and priveds another button element that will allow users to make a booking.

  ![Mock Up](docs/readme_images/)

3. **Footer:**
   - ``USER STORY - As a developer, I need to create the footer with social media links and contact information.``
   - The footer section shows at the bottom of all pages.
   - contains all social page icons which link to the social media sites and open in a new tab.
   - Contains all relevant contact info and address.

  ![Mock Up](docs/readme_images/)

4. **Sign Up:**
  - ``USER STORY - As a developer, I need to implement allauth so that users can sign up and have access to the website's features.``
  - The sign up page can be clicked on in the nav menu (if the user hasnt already signed in) or can accessed via the link in the sign up page.
  - The sign up form has 4 sections:
      1. Username - A user must enter a username and it will be this username they use to sign into the account in the future.
      2. Email - A user can enter an email address here but this is optional.
      3. Password - A user must enter a password for their account here.
      4. Confirm password - a user must confirm their password here and it must match the password above.
  - If sign up has been successful the user will be redirected to the site home page.

  ![Mock Up](docs/readme_images/)

4. **Create Booking:**
  - ``USER STORY - As a user, I would like to create a new booking when I want to schedule a training session.``
  - The create booking page only shows when a user has registered with the site as a user and has looged in.
  - If a user has not signed in they will be redicted to the sign in page.

  ![Mock Up](docs/readme_images/)

  - If a user has successfully sign in they will be sent to the create booking page.
  - The create booking form has 6 sections the user must fill in:
      1. Date - The user is asked to choose a date for their session.
      2. Time - The user will be asked to choose a a time for there session that are predetermined by the trainer (if the time is already booked the user will be asked to choose another time).
      3. Session Type - The user will have a choice between 2 session types: Consultation or Personal Training.
      4. Contact number - The user must enter a contact number.
      5. Email address - The user must enter a email address.
      6. Additional info - The user is asked to provide any additional info they feel is relevant or that theyd like the trainer to know before the first session.
  - If the suer leaves any section incomplete, except for the additional info section the form will not submit.

  ![Mock Up](docs/readme_images/)

5. **Managing Bookings:**
  - ``USER STORY - As a user, I would like to view my bookings to check the details.``
  - ``USER STORY - As a user, I would like to edit a booking to make changes when needed.``
  - ``USER STORY - As a user, I would like to delete a booking when I no longer need it.``
  - On the manage booking page the user is able to see all the sessions they have booked with the trainer.
  - The are shown the session type, and the date and time it is due to take place.
  - From here the user will have 2 options to edit an existing booking and delete a booking.

  ![Mock Up](docs/readme_images/)

  - If a user clicks edit they are taken to their origanl booking form with all the info they have already entered when making the booking.
  - From here the user can change any of the sections and save their changes or cancel them.

  ![Mock Up](docs/readme_images/)

  - If a user clicks on delete they will be asked to confirm if they wish to delete their booking or can cancel the delete request.

  ![Mock Up](docs/readme_images/)

6. **Trainer Booking Management:**
  - ``USER STORY - As a trainer, I want to be able to view all bookings to manage my schedule.``
  - At present the site allows for one trainer and that trainer is registered as the sites superuser and can manage their clients bookings via the admin page.
  - Once the trainer has logged is they can navigated to the bookings section on the admin panel.
  - From here the trainer can see any and all bookings their clients have made.
  - They can see all the info the client input on the create booking form.
  - From here they can filter the bookings by date, time or session type.
  - They can also delete the bookings from this page if they wish.

  ![Mock Up](docs/readme_images/)
  
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
