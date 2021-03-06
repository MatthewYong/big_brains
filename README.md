# Big Brains | Educational Toys for Children
Big Brains is a website for parents who wants to improve the development of their child. The website sells educational toys that challenges children under twelve. It also sells paid online services such as music, math, or language lessons. 
The user can register a profile and keep track of its order history and payments. The superuser can manage the products and services through the Django admin portal.
The goal of the website is for user to improve their child’s development. The website should give the user an ‘shopping’ experience.


![alt text][logo]

[logo]: https://github.com/MatthewYong/big_brains/blob/master/static/images/readme/image-landing-device.png?raw=true

## Table of Contents
- [UX](#ux)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [Surface Plane](#surface-plane)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)


## UX
To understand what the result of the website needs to be, we need to define the development process of each stage. This can be done by analyzing and breaking down the problem into five planes:

### Strategy Plane
The strategy plane defines the developer’s objective and the user needs (goals).

#### User Stories
As a **User** I want to:
1.  Buy toys
2.	Be informed of latest toys
3.	Contact the website owner
4.	Pay safely
5.	Check my purchase history
6.	Register my profile
7.	Login to my profile

As a **Developer** I want to:
1.  Gain more knowledge on Django
2.	Create a full-stack framework
3.	Learn more on databases, such as MySQL

As an **Admin** I want to:

1.	Add products/services
2.	Manage products/services
3.	Remove users
4.	Check user’s purchase history


### Scope Plane
The scope plane defines the features that are and are not possible to include on the website.
This will be further explained in the next chapter. A summary of the included and not included features are:

| Features (included) | Future features (not included)|
| :------------- | :---------- |
|1. Navigation menu | 1. Edit review|
|2. Banner | 2. Admin page for owners to add toys directly on the website instead of the Django portal|
|3. Landing page| 3. Webhook handling with delay
|4. Toy view & detail pages | 4. Order confirmation by mail
|5. Blog view, add & edit pages | 5. More JavaScript to attract customers
|6. Cart & Checkout pages |
|7. Login & registration pages |
|8. Profile page |
|9. Add toy review |

### Structure Plane

The structure plane defines the information architecture and interaction design with the user. 

#### Interaction Design
The following definitions has been used for this website:
- First impression of the website needs to be as simple and clear as possible
- No more than three clicks are required for the user to reach the page
- The type of information architecture that will be used is the ‘Hierarchical Tree’, see below:

![alt text][wireframe tree]

[wireframe tree]: https://github.com/MatthewYong/big_brains/blob/master/static/images/readme/image-wireframe-tree.jpg?raw=true

#### Information architecture

The initial database used for this project is sqlite3. During production the database was changed at the deployment stage to PostgreSQL with Heroku as add-on.

Databases have been setup in models.py of the following apps:

- Toys
- Blogs
- Profiles
- Reviews
- Checkout

An example of the Toy's database can be found below:

| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 age | ForeignKey |  null=True, blank=True, on_delete=models.SET_NULL
 sku | CharField | max_length=200, null=True, blank=True
 name | CharField | max_length=200
 description | CharField | max_length=2000
 price | DecimalField | max_digits=6, decimal_places=2
 image_url | URLField | max_length=1024, null=True, blank=True
 image | ImageField | null=True, blank=True

More about the Django database models can be found [here](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options).

### Skeleton Plane
The skeleton plane defines a basic visual design of the website through, for example, a wireframe.  
The wireframes for this project are made with Balsamiq can be downloaded from the following link:

- [Wireframe - Desktop version](https://github.com/MatthewYong/big_brains/raw/master/static/wireframes/Wireframe%20-%20Desktop.pdf)
- [Wireframe - Tablet version](https://github.com/MatthewYong/big_brains/raw/master/static/wireframes/Wireframe%20-%20Tablet.pdf)
- [Wireframe - Mobile version](https://github.com/MatthewYong/big_brains/raw/master/static/wireframes/Wireframe%20-%20Mobile.pdf)

Below you can find an example of a wireframe of the landing page:

![alt text][wireframe landing]

[wireframe landing]: https://github.com/MatthewYong/big_brains/blob/master/static/images/readme/image-wireframe-landing.jpg?raw=true


### Surface Plane
The surface plane defines the appearance of the website. This website needs to attract and encourage users to focus on the website's content.
The following design style has been used:

| Design Style | Design Choice|
| :------------- | :---------- |
Font: Open Sans | A font with an improved readability|
Text colour: #0F0F0 | A dark color|
Background colour: #FFFF| To enhance text and images |
Contrast ratio: 21 | A high ratio to express the visibility of the text (source: contrast-ratio.com)|

#### Color Scheme

![alt text][color scheme]

[color scheme]: https://github.com/MatthewYong/big_brains/blob/master/static/images/readme/image-colorscheme.png?raw=true


## Features
A summary of the features was described in the scope plane. This chapter will explain what the purpose is of each feature and what will be left to implement for the future.

### Existing Features
| Features (included) | Explanation|
| :------------- | :---------- |
|1. Navigation menu | 1. Allows user to quick access different pages of the website|
|2. Banner image with link to toys page | 2. Allows users to quick access the toys page |
|3. Landing page | 3. Allows users to identify which toys are available and which blogs can be read|
|4. Toy pages | 4. Allows users to view all the toys|
|5. Blogs pages | 5. Allows users to, besides reading all the blogs, add, edit and delete their own blogs|
|6. Cart & Checkout pages | 6. Allows users to add toys to the cart and checkout from the cart by completing the payment|
|7. Login & Registration pages | 7. Allows users to create a new profile
|8. User's profile page | 8. Allows users to view all its purchase history
|9. Toy reviews | 9. Allows users to view and add a review for a specific toy

### Features Left to Implement
| Features (not included) | Explanation|
| :------------- | :---------- |
|1. Edit review | This feature allows users to edit their own reviews, instead of deleting and rewriting their reviews|
|2. Adding toys through website| This feature allows the owner to add new toys through the website instead of the main portal
|3. Webhook handling with delay | This feature prevents a payment being taken from the user before the order has gone through|
|4. Order confirmation by email | This feature allows users to receive a confirmation by email when the order is completed|
|5. More JavaScript to attract more customers | This feature enhances the site experience for users|


## Technologies Used
The following technologies have been used to achieve this project:

Resources
- [HTML](https://www.w3.org/TR/html52/) is used as the main writing language of this project
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) is used for styling the HTML text
- [JavaScript](https://www.javascript.com/) is used for Stripe payments, scroll-to-top button, owl carousel and hiding and showing contact form
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is used as templating language for Python and its depending framework Django
- [Jquery](https://jquery.com/) is used for simplifying JavaScript commands

Styling
- [FontAwesome](https://fontawesome.com/) is used to improve the visual design of the website
- [Contrast-ratio.com](https://contrast-ratio.com/) is used to test the visibility of the text with the background color
- [Google fonts](https://fonts.google.com/) is used for the style the font
- [AOS](https://michalsnik.github.io/aos/) is used to animate the headers on the landing page when scrolling
- [OwlCarousel2](https://owlcarousel2.github.io/OwlCarousel2/) is used for the toys and blogs on the landing page

Framework, Libraries & API
- [Django](https://www.djangoproject.com/ is used as main web framework for the website
- [Django Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) is used for simplifying forms through Python
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used for user login and user registration
- [Bootstrap](https://getbootstrap.com/) is used for its grid system and navigation bar
- [Stripe](https://stripe.com/) is used for the payment system in the checkout app
- [Gunicorn](https://gunicorn.org/) is used for the deployment to Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) is used as an adapter for PostgreSQL with Django 

Database & Platform
- [sqlite3](https://www.sqlite.org/download.html) is used for storing data from the store. Specifically, for this website: storing of user order information, blogs, toys and toy reviews
- [PostgreSQL](https://www.postgresql.org/) is used for the same purpose as sqlite3, but is used for production
- [Heroku](https://heroku.com/) is used for deploying the app through its cloud platform
- [AWS S3](https://aws.amazon.com/) is used to store static and media files in production

Images
- [Adobe Photoshop CC 2020](https://www.adobe.com/uk/products/photoshop) is used to crop the images and deleting white background
- [Tinyjpg.com](https://tinyjpg.com/) is used to reduce the size of the JPG images
- [Tinypng.com](https://tinypng.com/) is used to reduce the size of the PNG images

Wireframe
- [Balsamic](https://balsamiq.com/) is used to draw wireframes for the skeleton plane and making the visual design of the structure plane

Testing
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) is used to test the responsiveness of the website and to debug any problems
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) is used to determine any overflow on the website
- [Validator.w3.org](https://validator.w3.org/) is used to validate the HTML code
- [Jigsaw.w3.org/css-validator](https://jigsaw.w3.org/css-validator/validator.html.en) is used to validate the CSS code
- [JSHint](https://jshint.com/) is used to validate the JavaScript code
- [Pep8](http://pep8online.com/) is used to validate the Python code


## Testing
The test procedures and the key issues of the tests are written in the file[TEST.md](https://github.com/MatthewYong/big_brains/blob/master/TEST.md).


## Deployment
The following chapter explains how to:
    - Clone a Repository from Github
    - Work with a Local Copy
    - Deployment on Heroku and file storage on AWS

### Requirements
- Python (version 3.0)
- Heroku account
- Github account
- Stripe account
- Gmail account
- AWS account

### Cloning the Repository
To work with a local copy of this project the following steps needs to be taken:

1. Go to the main page of the GitHub repository and click on the dropdown menu **Code**
![alt text][copy-clone]

[copy-clone]: https://github.com/MatthewYong/big_brains/blob/master/static/images/readme/image-dropdown-clone.jpg?raw=true
2. Copy the URL and go to your local IDE

3. In the terminal of your IDE type in **git clone** and the paste the URL copied from step 2
4. Press Enter and the clone will be created


### Working with a Local Copy
To work with the local copy that is created the following steps needs to be taken:

#### Step 1: Installing the Requirements
1. To install all the required libraries of the project go to the workspace of your local copy
2. In the terminal window of your IDE type in: **pip3 install -r requirements.txt**

#### Step 2: Setting Up Environment Variables
Depending on the IDE, the user has to make sure that the Environment Variables are properly setup. The following Environment Variables have been set up in **GitPod** to ensure that the project keys and project files are respectively taken from and migrated to the correct source. 


| Name | Value|
| :------------- | :---------- |
|1. DEVELOPMENT | True|
|2. SECRET_KEY | *'Your Secret Key'*|
|2. STRIPE_PUBLIC_KEY | *'Your Stripe Public key'* |
|3. STRIPE_SECRET_KEY | *'Your Stripe Secret key'* |
|4. STRIPE_WH_SECRET | *'Your Stripe WH Secret key'* |

For more information about Stripe API keys, please read the [Stripe API keys documentation](https://stripe.com/docs/keys).


#### Step 3: Migrating the Database
1. In the terminal window of your IDE type in: **python3 manage.py makemigrations**
2. In the terminal window of your IDE type in: **python3 manage.py migrate**

#### Step 4: Create SuperUser
1. In the terminal window of your IDE type in: **python3 manage.py createsuperuser**
2. Enter the credentials of the Superuser to access the Django Admin panel

#### Step 5: Loading Fixtures
1. In the terminal window of your IDE type in: **./manage.py loaddata 'Fixture_Filename'.json**
2. Make sure to that load the fixtures in the following order:
    - Categories
    - Toys
    - Blogs
3. Please note that a SuperUser has to be created **first**, in order to load the *blogs.json* fixture

#### Step 6: Run the App
1. Open your terminal window in your IDE
2. Type in **python3 app.py** to run the app
3. To access the Djanog Admin panel, add **/admin** at the end of the URL link and login with your credentials


### Heroku Deployment
To host this project on Heroku the following steps needs to be taken:

#### Step 1: Setting Up Heroku
1. Create a Heroku account
2. Create a new app and select your region

#### Step 2: Preparing Local Workspace for Heroku
In the terminal window of your local IDE type in the following:
file. This file is needed so that Heroku knows which files needs to be installed
1. **python app.py > Procfile** to create a Procfile. This file is needed so that Heroku knows which file is needed as its entry point to get the app up and running
2. Inside the Procfile enter: *web: gunicorn big_brains.wsgi:application* and then save the file
3. **pip3 install psycopg2-binary** to use PostgreSQL as the database
4. **pip3 install gunicorn** to install Gunicorn, which will act as the webserver and replace our development server once the app is deployed to Heroku
5. **pip3 freeze --local > requirements.txt** to store the packages into a file that tells Heroku what to install

#### Step 3: Setting the Configuration Variables in Heroku
1. Go back to your Heroku account and go to **settings**
2. Click on **Reveal Config Vars** to reveal the keys and the values
3. Set the keys and values as follow:
    (**KEY: VALUE**)
    - AWS_ACCESS_KEY_ID: *'Your Key'*
    - AWS_SECRET_ACCESS_KEY: *'Your Key'*
    - DATABASE_URL: *'Your Key'*
    - EMAIL_HOST_PASS: *'Your Key'*
    - EMAIL_HOST_USER: *'Your Email'*
    - SECRET_KEY: *'Your Key'*
    - STRIPE_PUBLIC_KEY: *'Your Key'*
    - STRIPE_SECRET_KEY: *'Your Key'*
    - STRIPE_WH_SECRET: *'Your Key'*
    - USE_AWS: *True*

#### Step 4: Preparing migration to PostgreSQL Database
1. Go back to your Heroku account and go to **Resources**
2. Search for Heroku PostgreSQL and add to Heroku
3. Go back to the IDE and comment out the Default configuration:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
4. Then add:
```
 DATABASES = {     
        'default': dj_database_url.parse("Your Postgres database URL")     
    }
```
Important note: Do **NOT** save and commit this change, this is a temporary procedure to push the files to PostgreSQL database. Commiting this file will expose the PostgreSQL Database URL.

#### Step 5: Migrating to PostgreSQL Database
1. In the terminal window of your IDE type in: **python3 manage.py makemigrations**
2. In the terminal window of your IDE type in: **python3 manage.py migrate**

#### Step 6: Create SuperUser
1. In the terminal window of your IDE type in: **python3 manage.py createsuperuser**
2. Enter the credentials of the Superuser to access the Django Admin panel

#### Step 7: Loading Fixtures
1. In the terminal window of your IDE type in: **./manage.py loaddata 'Fixture_Filename'.json**
2. Make sure to that load the fixtures in the following order:
    - Categories
    - Toys
    - Blogs
3. Please note that a SuperUser has to be created **first**, in order to load the *blogs.json* fixture

#### Step 8: Pushing files to Heroku 
1. In the terminal window of your local IDE type in **heroku login** or **heroku login -i** and fill in your heroku credentials and password
2. Commit all your files and type in the same terminal window **git push heroku master**. Now all your files are committed to Heroku

#### Step 9: Open App in Heroku
1. Click on **Open app** in the right corner of your Heroku account, the application will open in a new window
2. The live link is available from the address bar

#### Storing Static and Media files with AWS
For setting up the AWS S3 bucket please refer to the 
[AWS S3 Bucket documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) and the [S3BotoStorage documentation](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). The media files have to be taken from the repository and manually placed into the AWS S3 bucket.

#### Gmail
To obtain the **EMAIL_HOST_PASS**, please refer to 
[Google SMTP documentation](https://support.google.com/a/answer/176600?hl=en#zippy=%2Cuse-the-gmail-smtp-server).


## Credits
### Content
- All the toy's descriptions are taken from [Learningresources.co.uk](https://www.learningresources.co.uk)
- All the blog stories are taken from [Edutopia.org](https://www.edutopia.org)
- All remaining text is written by myself
- To maintain consistency through all my Code Institute projects, a similar structure for the Readme file has been used from my previous projects


### Media
- All photos for this project are used from:
    - [Unsplash.com](https://unsplash.com)
    - [Learningresources.co.uk](https://www.learningresources.co.uk)
    - [Edutopia.org](https://www.edutopia.org)    

### Source of Codes
The following codes were inspired or taken from:
- [Code Institute](https://codeinstitute.net/): The project is mainly based on the Boutique Ado example project from the module Full-stack Framework with Django. The following codes are derived or used in this project:
    - The Stripe payments in the Checkout app
    - The context.py & templatetags-cart_tools.py in the Cart app
    - All settings to deploy to AWS & Heroku
- [W3schools](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp*/): Hiding the quantity arrow in the input field. Code used on line 69 in base.css
- [CSS Tricks](): Animating underlines. Code used on line 76 in base.css
- [AOS Animate on Scroll](https://michalsnik.github.io/aos/): Animating fade in headers on landing page. Code used on landing.html
- [Owl Carousel 2 ](https://owlcarousel2.github.io/OwlCarousel2/demos/demos.html): Code derived for Toys and Blogs carousel on landing page. Code used on landing.html and main.js


### Acknowledgement
The completion of this project could not have been possible without support and the extensive knowledge of other people. My appreciation goes to:
- Gerard (Gerry) McBride, my mentor, for giving me tips on testing in Django and guidance throughout the project
- Code Institute, for the valuable lessons through videos and exercises, mainly the last project lesson Boutique Ado from Chris-ckz8780
- Stack Overflow, for giving me code support 
- Slack community for giving me new ideas and code support

## Disclaimer
This website is for educational purposes only. All content and images are illustrative.