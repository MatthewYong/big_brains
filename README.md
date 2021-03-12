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

Below you can find an example of a wireframe of the landing page.

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


## Deployment



## Credits
### Content
- All toy description are taken from [Learningresources.co.uk](https://www.learningresources.co.uk)
- All blog stories are taken from [Edutopia.org](https://www.edutopia.org)
- To maintain consistency through all my Code Institute projects, a similar structure for the Readme file has been used from my previous projects
- All remaining text is written by myself

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