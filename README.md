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

### Chrome DevTools

**Chrome Devtools** was used to simulate how the website displayed on different devices with emphasis on Large Laptop (17.3") & Mobile screen sizes. It was also used as the main debugging tool when content was displayed incorrectly.

### Manual Testing
The website was tested on a Samsung A50 Android Device and the resulting layout is similar to the iPhone 8 within Chrome Devtools.

Each of the user journeys were tested manually

- As a registered user, I want to be able to login.
The login form uses HTML5 required attribute to ensure that both username and password fields are completed. This was tested by attempting to login leaving the fields blank.
The login form was also tested using an invalid username to ensure the user received the appropriate error message via flash.
Similarly, the login form was tested with a valid username but an invalid password to ensure the user received the appropriate error message via flash.

- As a general/unregistered user, I want to be able to register.
The register form uses javascript on the client side to validate user input. This was tested manually by leaving fields blank and entering invalid data.
Once valid data has been submitted, the register function in the Flask web application will check if the username is unique.
If the username is not unique an error message is displayed via Flash messaging. 

- As a registered user, I want to be able to logout.
This function was tested manually after being logged in.

- As a registered user, I want to be able to add a recipe.
Adding a recipe is only available to registered users. This was tested when logged out and logged in successfully.
Adding a recipe redirects the user to the add recipe form where they can add the recipe details.
The add recipe form uses HTML5 to validate user input which was tested by entering invalid data.
The save recipe adds the recipe to the database and displays a success message to the user via flash messaging.

- As a registered user, I want to be able to edit a recipe.
Editing a recipe successfully populated the edit recipe form with recipe details to be edited.
Clicking on update recipe calls the update function and successfully updated the values for the document in the MongoDB database.
The edit recipe function only allows the author of the recipe to edit the recipe, this was tested by trying to edit a recipe from another user.
The user receives an error message via flash messaging if the user doesn't match the author.

- As a registered user, I want to be able to delete a recipe.
Clicking on delete recipe opens a modal to ask the user to confirm the delete operation. 
The delete recipe function only allows the author of the recipe to delete the recipe, this was tested by trying to delete a recipe from another user.
The user receives an error message via flash messaging if the user doesn't match the author. 

- As a user (registered/unregistered) , I want to see how long a recipe takes to prepare & cook.
The recipe details are available to any user by clicking the view recipe button on the recipe card.

Throughout the development of the web application JavaScript functions were tested using console.log statements in particular the validateForm() function to check that the value
of the errors variable incremented as each of the if conditions were tested. Print() statements were used in the Flask application to ensure that the values of the form fields were being sent
from the client to the server.

Setting Debug=True in the Flask application allows any routing issues to be corrected.

### Mentor Sessions
The sessions with my mentor Precious Ijege identified minors bugs such as form validation which was then corrected using both HTML5 attributes and JavaScript. These sessions also identifed 
a but with the recipe card images which was corrected using Bootstrap embed-responsive class.

### Additional Testing
W3C CSS Validator and W3C HTML Validator were used to identify any issues with the HTML and CSS code. 

Autoprefixer was used to ensure that vendor prefixes had been added to the CSS.

## Deployment

The project was developed locally using Visual Studio Code. Git was downloaded from https://git-scm.com/ and installed locally for version control. In parallel, a repository also called My-Cookbook was created on GitHub.

The project workspace was initialised using git init command from the cmd terminal within VS Code.

To connect the local git repository to GitHub repository, the following command was executed from the cmd terminal.

git remote add origin https://github.com/LawlessXD/my-cookbook.git

Each time a new feature was added the files would be added to the staging area using git add \* from the cmd line.

The features were then committed with a suitable message using git commit -m "Added login, logout, and register functionality".

The changes were pushed to the remote repository using git push -u origin master initially and using git push for each subsequent push.

### How to deploy this application locally

Before you can run this application on your own machine, you must meet the following requirements;
- Use a suitable IDE e.g. VS Code, GitPod etc.
- Have Git installed. 
- Have Python installed.
- Have PIP installed.
- An account on [MongoDB Atlas](mongodb.com) to create a Cluster, Database and Collections using the DB Schema above.  

#### Steps

1. Create a local project folder
2. Navigate to main page for the repository https://github.com/LawlessXD/my-cookbook
3. Click "Code"
4. Copy the URL.
5. Open folder to the project folder where you would like to Clone the repository.
6. Open terminal within your local IDE
6. Execute git clone https://github.com/LawlessXD/my-cookbook.git from the command line.
7. The project will now be cloned.
8. Alternatively, you can Download a ZIP of the repository, extract the folder and open with your preferred IDE.
9. Open a CMD terminal, and create a virtual environment using the below command
```
python -m venv venv
```
10. Activate the virtual environment using the below command
```
venv\Scripts\activate   
```
11. Upgrade PIP if required
```
pip install --upgrade pip.
```
12. Install the modules in the requirements file
```
pip -r requirements.txt
```
13. Open sampleenv.py and update the environment variables included
14. rename sampleenv.py to env.py
15. Run the application using the below command
```
python app.py
```
16. The application can be opened in your browser `http://127.0.0.1:5000`

### Heroku

The application is hosted on [Heroku](heroku.com) and was deployed as follows; 

1. Created an account at [Heroku](heroku.com) 
2. Clicked "New" and "Create new app"
3. **App name** - Entered "mycookbook-dl" as the app name (This must be unique on Heroku).
4. **Region** - Selected "Europe".
5. Clicked "Create App".
6. **Deployment Method** - Leave as default "Use Heroku CLI".
7. Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).
8. Enter heroku login at the command line and enter your credentials when prompted.
9. Create a local `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
10. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.
11. Add to Heroku remote using terminal command `heroku git:remote -a mycookbook-dl`
12. Pushed local git repository to Heroku using terminal command `git push heroku master`
13. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
14. Enter the following variables;

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
MONGO_DBNAME | `<your db name>`
SECRET_KEY | `<your_secret_key>`

15. Enter the following using terminal command to start dynos
`heroku ps:scale web:1`

16. The application is now deployed and can be viewed on [Heroku](https://mycookbook-dl.herokuapp.com/).

## Acknowledgement & Credits

I would like to thank my mentor Precious Ijege for his guidance and support throughout the project review sessions and Anna Greaves for a very informative guide to setting up environment variables.

I would like to credit https://github.com/MiroslavSvec/DCD_lead for the login and register functionality.

How to add fields dynamically was achieved following the guide at https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/

### Media

The recipes used on the site are taken from [BBC Good Food Recipes](https://www.bbcgoodfood.com/recipes),