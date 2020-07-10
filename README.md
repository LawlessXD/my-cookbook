# My Cookbook - Milestone Three Project

You can view the deployed web application [here](https://mycookbook-dl.herokuapp.com/)!

***


The purpose of this project is to create an online cookbook that allows users to create, manage and share recipes. The web application uses HTML, CSS, Javascript & Bootstrap for the Front-End connecting to a MongoDB database using Python Flask application.

![Am I Responsive Image](https://github.com/LawlessXD/my-cookbook/blob/master/wireframes/responsiveview.jpg "Am I Responsive")

***

## UX

The primary objective of this website is to create and share recipes online with other people. The site allows any visitor to view recipes but only registered users can add, edit or delete recipes.

### Strategy

#### User Stories

- As a general (unregistered) user, I want to be able to view recipes from other people.
- As a general (unregistered) user, I want to be able to search for a recipe based on ingredients or recipe name.
- As a general (unregistered) user, I want to be able to register to add my own recipes.
- As a registered user, I want to be able to login.
- As a registered user, I want to be able to reset my password.
- As a registered user, I want to be able to logout.
- As a registered user, I want to be able to view my recipes only.
- As a registered user, I want to be able to edit a recipe.
- As a registered user, I want to be able to delete a recipe.
- As a registered user, I want to be able to like or unlike a recipe.
- As a user (registered/unregistered) , I want to see how long a recipe takes to prepare & cook.
- As an admin user, I want to be able to manage enable or disable any user.
- As an admin user, I want to be able to see how many recipes exist.
- As an admin user, I want to be able to see how many users exist.
- As an admin user, I want to be able to view recipes by user.
- As an admin user, I want to be able to edit or remove any recipe.

### Scope

The scope of the project is derived from the user stories outlined in the strategy plane above. At this stage of the UX process, we decide what features will be provided now 
and what will be provided at some point in the future. The main requirement of the project is to allow users to create, view, update and delete a recipe. 

### Structure

The structure chosen is a simple layout with a navigation bar, main content and footer sections.

### Skeleton

At this stage, wireframes were created using MS Visio for each of the different scenarios below;
- All Recipes 
- Login 
- Register  
- Add a recipe
- Edit a recipe

### Surface

The primary colour for the navigation bar is derived from the colour used by https://materializecss.com/ (HEX value #ee6e73). The remaining colours selected throughout the site were generated 
using the Adobe colour wheel https://color.adobe.com/create to compliment the primary colour.  

The background image for the body compliments the light colours used on the navigation and footer sections. It also allows recipes and forms throughout the site to stand out as opposed to using a plain
white background for the content section.

## Features 

The features implemented in the application are listed below:
- Recipes page: This is used as the landing page for the application and displays the recipes in card format using the Bootstrap grid system.
- Navigation: This allows the user to navigate through the application with different options displayed for users that are logged in.
- Login: This allows a registered user to log in to the application.
- Register: This allows new users to create an account.
- Logout: This allows a user to logout from the application.
- Add recipe: This allows a registered user to add a recipe.
- Edit recipe: This allows a user to edit their own recipe. If the current user is not the author, an error message is displayed below the navigation bar.
- Delete recipe: This allows a user to edit their own recipe. If the current user is not the author, an error message is displayed below the navigation bar.
- Flash messages: Flash messages are used to display messages to the user when carrying out different functions.

The features that will be implemented at a later date are listed below:
- Search: The functionality to search for a recipe based on ingredients or recipe name.
- Filter: Filter recipes by type, user etc.
- Reset Password: The functionality to send a user a one time token to reset their password with expiry time.
- My Recipes: Allow a user to view their recipes only.
- Like/Unlike a recipe: Allow a user to like and unlike a recipe.
- Admin Section: Manage users, recipes and view dashboard with recipe and user details.
- Pagination: Add pagination to the site as the number of recipes increase.

## Database Schema

The web application connects to a MongoDB database with the information stored in two collections **Recipes** and **Users**. The schema was created using [Mongo.tools ](https://mongo.tools/).

The username field in the users collection is inserted into the recipes collection when a recipe is created.

![Mongo DB Schema](https://github.com/LawlessXD/my-cookbook/blob/master/wireframes/schema.jpg "Mongo DB Schema")

___

## Technologies Used

### Languages
- **HTML** - Used as markup for the website
- **CSS** - Used to add style to the page and position elements
- **jQuery** - Used in conjunction with Bootstrap V4 Framework
- **Javascript** - Used for form validation, toggling the navigation bar and adding/removing ingredients/steps on the add/edit recipe forms.
- **Python** - Used for different functions of the web application.


### Libraries
- **Flask** - Uses the Flask framework for rendering html templates and managing sessions.
- **Flask-PyMongo** - Used to connect Flask application to MongoDB.
- **Bootstrap** - Used throughout the site for responsive design
- **Font Awesome** - Used to enhance the UX 
- **Google Fonts** - imported into CSS

### Tools
- **MongoDB Atlas** - Used to host the database for the application
- **VSCode** - Used as IDE for project
- **Git** - Used for version control throughout the project
- **MS Visio** - Used to create wireframes
- **Autoprefixer** - Used to add vendor prefixes to animations in style.css

___

## Testing