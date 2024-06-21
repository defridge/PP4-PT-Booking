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
  - [Site Design](#site-design)
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

### Milestones & User Stories

#### Milestone 1: Base Setup

- USER STORY: As a developer, I need to set up the project so that it is ready for implementing core features.
- USER STORY: As a developer, I need to create the base.html page and structure so that other pages can reuse the layout.
- USER STORY: As a developer, I need to create static resources so that images, CSS, and JavaScript work on the website.
- USER STORY: As a developer, I need to create the footer with social media links and contact information.
- USER STORY: As a developer, I need to create the navbar so that users can navigate the website from any device.

#### Milestone 2: Standalone Pages

- USER STORY: As a developer, I need to implement a 404 error page to alert users when they access a non-existent page.
- USER STORY: As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.
- USER STORY: As a developer, I need to implement a 403 error page to redirect unauthorized users.
- USER STORY: As a site owner, I would like a home page so that customers can view information about my services.

#### Milestone 3: Authentication

- USER STORY: As a developer, I need to implement allauth so that users can sign up and have access to the website's features.
- USER STORY: As a site owner, I would like the allauth pages customized to fit the site's styling.

#### EMilestone 4: Booking Management 

- USER STORY: As a user, I would like to create a new booking when I want to schedule a training session.
- USER STORY: As a user, I would like to view my bookings to check the details.
- USER STORY: As a user, I would like to edit a booking to make changes when needed.
- USER STORY: As a user, I would like to delete a booking when I no longer need it.
- USER STORY: As a trainer, I want to be able to view all bookings to manage my schedule.

#### Milestone 5: Deployment

- USER STORY: As a developer, I need to set up Whitenoise to serve static files in deployment.
- USER STORY: As a developer, I need to deploy the project to Heroku to make it live for users.

#### Milestone 6: Documentation

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
  - The sign up form has 5 sections:
    1. Email - A user must enter a email address.
    2. Email (again) - A user must confirm the email address by inputting it again here.
    3. Username - A user must enter a username and it will be this username they use to sign into the account in the future.
    4. Password - A user must enter a password for their account here.
    5. Confirm password - a user must confirm their password here and it must match the password above.
  - If sign up has been successful the user will be redirected to the site home page.

  ![Mock Up](docs/readme_images/)

5. **Create Booking:**
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

6. **Managing Bookings:**
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

7. **Trainer Booking Management:**
  - ``USER STORY - As a trainer, I want to be able to view all bookings to manage my schedule.``
  - At present the site allows for one trainer and that trainer is registered as the sites superuser and can manage their clients bookings via the admin page.
  - Once the trainer has logged is they can navigated to the bookings section on the admin panel.
  - From here the trainer can see any and all bookings their clients have made.
  - They can see all the info the client input on the create booking form.
  - From here they can filter the bookings by date, time or session type.
  - They can also delete the bookings from this page if they wish.

  ![Mock Up](docs/readme_images/)

8. **Error Pages**
  - ``As a developer, I need to implement a 404 error page to alert users when they access a non-existent page.``
  - ``As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.``
  - ``As a developer, I need to implement a 403 error page to redirect unauthorized users.``
  - If a user navigates to a broken link/missing page then a custom 404 error page will be displayed that easily helps the user get back to the home page without using the browser back buttons.
  - A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.
  - A 403 error page has been created and styled to match the other error pages in look and functionality, however at present there is no reason why this error page would be raised with this project.

9. **Base Setup and Other User Stories**
  - ``As a developer, I need to set up the project so that it is ready for implementing core features.``
  - ``As a developer, I need to create the base.html page and structure so that other pages can reuse the layout.``
  - ``As a developer, I need to create static resources so that images, CSS, and JavaScript work on the website.``
  - ``As a site owner, I would like the allauth pages customized to fit the site's styling.``
  - All the above user stories have been implemented in order to complete all the features of the app as outlined above.
  
### Features Left to Implement

1. **Social Media Integration:**
    - Allow users to share their progress on social media platforms.

2. **In-App Messaging:**
    - Enable communication between trainers and clients within the app.

3. **Multiple Trainers:**
    - Have multiple trainers on the app

4. **Progress Tracking:**
    - Log workouts and track progress.
    - View progress over time with visual charts.

## Technologies Used

- **Frontend:**
  - HTML5, CSS3, JavaScript
  - Bootstrap 5

- **Backend:**
  - Python, Django

- **IDE:**
  - GitPod (Visual Studio Code Online)

- **Database:**
  - PostgreSQL

- **Version Control:**
  - Git, GitHub

- **Deployment:**
  - Heroku

- **Site Syling:**
  - Google Fonts, Favicon.io

- **Image Processing**
  - convertio.co, TinyPNG

### Python Modules Used in the Project

#### Standard Python Modules:
- `os`: Used for accessing environment variables and handling file paths.
- `timezone`: Used for managing date and time operations.
- `forms`: Used for creating forms.
- `models`: Used for creating database models.

#### Django Modules:
- `django`: The primary framework for building the application.
- `django.contrib.admin`: Provides the Django admin interface.
- `django.contrib.auth`: Provides authentication framework.
- `django.contrib.contenttypes`: Supports generic relations between models.
- `django.contrib.sessions`: Manages user sessions.
- `django.contrib.messages`: Provides a messaging framework.
- `django.contrib.staticfiles`: Manages static files.
- `django.contrib.sites`: Enables multi-site support.
- `django.template.backends.django.DjangoTemplates`: Used for template rendering.
- `django.template.context_processors`: Provides context processors for templates.
- `django.middleware`: Provides various middleware classes for processing requests.
- `django.db`: Provides database management functionalities.

#### Third-Party Modules:
- `dj_database_url`: Used for parsing database URLs.
- `allauth`: Provides authentication, registration, account management, and more.
- `allauth.account`: Extends `allauth` for account management.
- `allauth.socialaccount`: Extends `allauth` for social account management.
- `whitenoise.middleware.WhiteNoiseMiddleware`: Serves static files in production.

#### Environment Management:
- `env`: For accessing environment variables.

#### Other Modules:
- `django.contrib.messages.constants as messages`: Provides constants for message tags.
- `django.forms`: Provides form handling.

### External Python Modules

- `asgiref==3.8.1`: ASGI (Asynchronous Server Gateway Interface) reference implementation and utilities.
- `dj-database-url==0.5.0`: Utility to parse database URLs.
- `Django==4.2.13`: The web framework used to build the project.
- `django-allauth==0.57.2`: Integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.
- `gunicorn==20.1.0`: Python WSGI HTTP Server for UNIX.
- `oauthlib==3.2.2`: A generic and thorough implementation of the OAuth request-signing logic.
- `psycopg2==2.9.9`: PostgreSQL database adapter for Python.
- `PyJWT==2.8.0`: JSON Web Token implementation in Python.
- `python3-openid==3.2.0`: Python OpenID support.
- `requests-oauthlib==2.0.0`: OAuthlib support for Python Requests.
- `sqlparse==0.5.0`: A non-validating SQL parser.
- `whitenoise==5.3.0`: Radically simplified static file serving for WSGI applications.

## Database Design

### Database Design Summary for the Booking Model

The `Booking` model represents the core of the database design for the application. It is used to manage and store information about personal training and consultation sessions booked by users. Below is a summary of the database design based on the provided `Booking` model.

#### Models

1. **User Model**
   - **User**: Provided by Django's built-in authentication system (`django.contrib.auth.models.User`).
     - This model manages user-related data including username, password, email, etc.

2. **Booking Model**
   - **Booking**: Custom model for storing booking information.
     - Fields:
       - **user**: Foreign key to the `User` model, representing the user who made the booking.
       - **date**: DateField to store the date of the booking. Defaults to the current date.
       - **time**: CharField to store the time of the booking. Uses predefined choices for different time slots.
       - **session_type**: CharField to store the type of session. Uses predefined choices for "Consultation" and "Personal Training".
       - **duration**: IntegerField to store the duration of the session in minutes. Defaults to 60 minutes.
       - **contact_number**: CharField to store the user's contact number.
       - **contact_email**: EmailField to store the user's contact email.
       - **additional_info**: TextField to store any additional information provided by the user. Has a default value and cannot be blank or null.
     - **Meta**:
       - `unique_together = ('date', 'time')`: Ensures that each combination of date and time is unique, preventing double bookings for the same time slot.
     - **Methods**:
       - `__str__(self)`: Returns a string representation of the booking, including the username, session type, date, and time.

#### Choices for Fields

1. **SESSION_TYPE_CHOICES**
   - Defines the types of sessions available for booking:
     - `('consultation', 'Consultation')`
     - `('personal_training', 'Personal Training')`

2. **TIME_CHOICES**
   - Defines the time slots available for booking:
     - `('08:00', '8:00 AM - 9:00 AM')`
     - `('09:00', '9:00 AM - 10:00 AM')`
     - `('10:00', '10:00 AM - 11:00 AM')`
     - `('11:00', '11:00 AM - 12:00 PM')`
     - `('14:00', '2:00 PM - 3:00 PM')`
     - `('15:00', '3:00 PM - 4:00 PM')`
     - `('16:00', '4:00 PM - 5:00 PM')`
     - `('17:00', '5:00 PM - 6:00 PM')`

#### Database Relationships

- **One-to-Many Relationship**:
  - The `Booking` model has a foreign key relationship with the `User` model. This means that each user can have multiple bookings, but each booking is associated with a single user.

#### Constraints

- **Unique Constraint**:
  - The combination of `date` and `time` must be unique across all bookings to prevent double-booking the same time slot.

This design ensures that the application can effectively manage user bookings, including preventing conflicts and storing all necessary information related to each booking.

## Site Design

### Colour-Scheme

For this website the primary colors are Black (#212529), Red (#DC3545), and White (#ffffff). The black in mainly used in the nav and footer elements, with some buttons such as call-to-action button being black also. The red is used to give a nice contrast to the black nav and footer elements and is used on most of the buttons throughout the site. White is manily used for all the page backgrounds. These 3 colours match the colour scheme of the pictures used on the site home page and I really like how these all work together to give a clean and professional look.

### Typography

The Montserrat font was used throughout the website. This font is from google fonts and was imported into the style sheet.

### Imagery

All images on the site are owned by the site designer.
