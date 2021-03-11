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
To understand what the result of the website needs to be, we need to define the development process of each stage. This can be done by analysing and breaking down the problem into five planes:

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

[wireframe tree]: https://github.com/MatthewYong/big_brains/blob/master/static/wireframes/image-wireframe-tree.jpg?raw=true

#### Information architecture

This project has 4 collections in the database. The database structure in MongoDB has been set up as follows:

![alt text][diagram]

[diagram]: https://raw.githubusercontent.com/MatthewYong/




### Skeleton Plane
The skeleton plane defines a basic visual design of the website through, for example, a wireframe.  
The wireframes for this project are made with Balsamiq can be downloaded from the following link:

- [Wireframe - Desktop version](https://github.com/MatthewYong/
- [Wireframe - Tablet version](https://github.com/MatthewYong/
- [Wireframe - Mobile version](https://github.com/MatthewYong/

Below you can find an example of a wireframe of the landing page.

### Surface Plane
The surface plane defines the appearance of the website. This website needs to attract and encourage users to focus on the website's content.
The following design style has been used:

| Design Style | Design Choice|
| :------------- | :---------- |
Font: Open Sans | A font with an improved readability|
Text colour: #0F0F0 | A dark color|
Background colour: #FFFF| To enhance text and images |
Contrast ratio: 19.16 | A high ratio to express the visibility of the text (source: contrast-ratio.com)|

## Features
A summary of the features was described in the scope plane. This chapter will explain what the purpose is of each feature and what will be left to implement for the future.

### Existing Features
| Features (included) | Explanation|
| :------------- | :---------- |
|1. Navigation menu | 1. Allows user to quick access different pages of the website|
|2. Hero image with link to add recipe | 2. Allows users to quick access the add recipe page |
|3. Landing page with category recipes | 3. Allows users to quick access a specific recipe category|
|4. Add recipe page | 4. Allows users to add their recipe by filling out the recipe form|
|5. Edit button/recipe page | 5. Allows users to edit their own recipes|
|6. Login page | 6. Allows users to login to their profile|
|7. Registration page | 7. Allows users to create a new profile
|8. User's profile page | 8. Allows users to view all of their own recipes

### Features Left to Implement


## Technologies Used

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
    - The context.py & templatetags in the Cart app
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