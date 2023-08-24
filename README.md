## Demo church website with animation and Twitter integration

Welcome to the repository for my Django-based website project that utilizes Bootstrap for the frontend, features animations to enhance user experience, connects to Twitter to update blog posts, and includes an admin page for easy management.

##Project Demo


https://github.com/safegergis/aamc-website/assets/33107228/b25e4987-6a6b-4296-85df-c2e3e84ac41e


<img width="1489" alt="Screenshot 2023-08-23 at 3 28 57 PM" src="https://github.com/safegergis/aamc-website/assets/33107228/e7eeca32-864b-4524-8c08-43562f39d8c4">
<img width="1489" alt="Screenshot 2023-08-23 at 3 29 30 PM" src="https://github.com/safegergis/aamc-website/assets/33107228/8a61aa8f-007a-423b-9fbb-6ef64d032283">
<img width="854" alt="Screenshot 2023-08-23 at 6 03 16 PM" src="https://github.com/safegergis/aamc-website/assets/33107228/71a10ad6-6fa6-4be1-af18-5e1d1d290893">

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Twitter Integration](#twitter-integration)
- [Admin Page](#admin-page)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a dynamic web application built using the Django framework, HTML, CSS (Bootstrap), and JavaScript. My primary goal with this project is to create a visually appealing website with interactive animations, facilitate real-time blog post updates through Twitter integration, and offer an admin panel for convenient content management.

## Features

- **Bootstrap Frontend:** The website is designed with a responsive and modern frontend using the Bootstrap framework, ensuring compatibility across various devices and screen sizes.

- **Animations:** I've integrated animations throughout the website to enhance user engagement and provide a visually pleasing experience. From subtle hover effects to more elaborate transitions, animations are used to create a dynamic interface.

- **Twitter Integration:** The website connects to the Twitter API to fetch and display the latest blog posts or updates from a specified Twitter account. This ensures that the website's content remains up-to-date and relevant.

- **Admin Page:** I've implemented an admin page that is accessible only to authorized users. This admin panel allows content managers or administrators to conveniently add, edit, or remove blog posts, update animations, and manage various aspects of the website.

## Dependencies

The project relies on the following dependencies:

- **Django:** The web framework used for building the website.
- **Bootstrap:** A popular CSS framework for creating responsive and visually appealing designs.
- **Tweepy:** A Python library for accessing the Twitter API and integrating Twitter functionality.
- **Whitenoise:** A static file serving library for Django that helps optimize serving static files in production environments.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository:** Begin by cloning my repository to your local machine using the following command:
   ```
   git clone https://github.com/safegergis/aamc-website.git
   ```

2. **Navigate to the Directory:** Move into the project directory:
   ```
   cd aamc-website
   ```

3. **Create a Virtual Environment:** It's recommended to create a virtual environment to manage project dependencies. Use the following commands to create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies:** Install the required Python packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

5. **Database Setup:** Set up the database by applying migrations:
   ```
   python manage.py migrate
   ```

6. **Run the Development Server:** Start the development server to preview the website locally:
   ```
   python manage.py runserver
   ```

The website should now be accessible at `http://127.0.0.1:8000/`.

## Usage

Once the project is set up and the development server is running, you can explore the website, interact with the animations, and check the Twitter-integrated blog posts. The admin page is accessible at `http://127.0.0.1:8000/admin/` where you can log in with your admin credentials to manage content.

## Twitter Integration

The Twitter integration is achieved through the Twitter API. To enable this feature, you'll need to:

1. Create a Twitter Developer Account and set up a Twitter App to obtain API keys and tokens.
2. Add your API keys and tokens to the project's settings to enable communication with the Twitter API.

## Admin Page

The admin page provides an interface for authorized users to manage the website's content. To access the admin panel:

1. Create a superuser account using the following command:
   ```
   python manage.py createsuperuser
   ```
2. Visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
3. From the admin panel, you can manage blog posts, animations, and other aspects of the website.



## License

This project is licensed under the [MIT License](LICENSE), allowing you to use, modify, and distribute the code for both commercial and non-commercial purposes.

---

I hope you find this project enjoyable and informative. Feel free to reach out with any questions or suggestions!
