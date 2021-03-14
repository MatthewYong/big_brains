# Big Brains | Testing


## Table of Contents
- [Manual Testing](#manual-testing)
    * [Navigation Testing](#navigation-testing)
    * [Browser and Mobile Devices Testing](#browser-and-mobile-devices-testing)
- [Python Testing](#manual-testing)
- [Key Issues and Code Validation](#key-issues-and-code-validation)


## Manual Testing
Manual tests have been done throughout the development of the project.  
The following test scenarios confirms that the website is behaving accordingly, and that bugs have been taken care of:

### Navigation Testing
#### Access Toys page through Landing Page
1. On the landing page click on **SHOP NOW** button
2. Verified that this will open the target page

#### Access each a specified Toy or Blog page through Landing Page
1. On the landing page click on a specific toy in the carousel
2. Verified that this will open the Toy detail page
3. Go back to the landing page and click on a blog in the carousel
4. Verified that the Blog detail page will open

#### Access each Payment method on the Landing page
1. On the landing page select one of the payment method
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining elements

#### Access each Element on the Navigation menu
1. On any page click on one of the elements in the navigation menu
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining elements

#### Access each Element on the Footer
1. On any page click on one of the social media icons in the footer
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining icons

#### Access Contact form in the Footer
1. On any page click on **CONTACT** in the footer
2. Verified that this will open a form

#### Scroll To Top button
1. On any page scroll down the page until a button with an upward arrow pops up
2. Click and the button
3. Verified that the screen will scroll to the top


### Feature Testing
#### Add Toy to Cart
1. Go to any Toy on the either the Landing page or Toys page
2. Click on button **ADD TO CART**
3. Verified that a popup window with the text 'ADDED TO CART' will show
4. Click on the Cart icon
5. Verified that the toy has been added to the cart

#### Update Toy Quantity in Cart
1. Add a toy to the cart
2. Go to the cart page 
3. Change the quantity and click on the update icon 
4. Verified that the quantity has been updated

#### Complete an Order from the Toy's Cart
1. Add a toy to the cart
2. Go to the cart page and click on **CHECKOUT**
3. Fill in the form and use the Stripe test payment method **4242 4242 4242 4242**
4. Click on **BUY NOW**
5. Go to Profile page
6. Verified that the order has been fulfilled added to the Profile page

#### Add Review
1. Login to an account
2. Go to a detail page of any toy
3. Fill in the form and click on **ADD REVIEW**
4. Verified that the review has been added

#### Delete Review
1. Login to an account
2. Go to a detail page of any toy
3. Fill in the form and click on **ADD REVIEW**
4. Go to the review that has been added and click on **DELETE REVIEW** 
4. Verified that the review has been deleted

#### User Profile - All Orders
1. Login to account
2. Add a toy to the cart
3. Go to the cart page and click on **CHECKOUT**
4. Fill in the form and use the Stripe test payment method **4242 4242 4242 4242**
5. Click on **BUY NOW**
6. Go to Profile page
7. Verified that the order has been fulfilled added to the Profile page

#### Add Blog
1. On Add Blog page:
2. Fill in all required fields on the form
3. Click on button **ADD ARTICLE**
4. Verified that the Blog has been added to the website 

#### Edit Blog
1. Add a blog to the website and go to the all blogs page
2. Click on button **EDIT**
3. Make changes to the form
4. Click on button **EDIT YOUR ARTICLE**
5. Verified that the blog is updated

#### Delete Blog
1. Add a blog to the website and go to the all blogs page
2. Click on button **DELETE** of the blog that it is added
3. Verified that the blog is deleted in all blogs page

#### Send Email through Contact Form
1. On any page click on **CONTACT** in the footer
2. Fill in the form and click on **SEND**
3. Verified that an email will be received 


### Login, Logout, Registration Testing
#### Registration - Successful
1. Click on **SIGNUP** in navigation menu
2. Choose an email, username and password
3. Click on **SIGN UP** button in the form
4. Verified that profile has been created and redirected to landing page

#### Login - Successful
1. Click on **Login** button in navigation menu
2. Fill in your username and password
3. Verified that login was succesful and redirected to landing page

#### Login - Unsuccessful
1. Click on **Login** button in navigation menu
2. Fill in a wrong username and/or password
3. Verified that login failed and that a text message **'The username and/or password you specified are not correct.'** will appear above the login input 

#### Logout
1. Login into account
2. Click on logout button in navigation menu
3. Verified that this will open the login page 
4. Verified that a text message **'YOU HAVE SIGNED OUT.'** will appear as a popup window
5. Verified that Signup and Login will appearin the navigation menu

#### 404 Error Testing
1. Open any page on the website
2. Add extra text to the address bar to change the URL
3. Verified that link does not exist and 404 page will show


### Browser and Mobile Devices Testing
All the test scenarios have been carried out in the browsers and mobile devices as listed below. No problems were found regarding the responsiveness, overflow and the functionality.

#### Browser Testing
- Google Chrome - version 89.0.4389.90 (64-bit)
- Mozilla Firefox - version 86.0 (64-bit)
- Microsoft Edge - version 89.0.774.54 (64-bit)
- Internet Explorer - version 11.719.18362.0

#### Mobile Device Testing through Chrome DevTools
- Moto G4 
- Galaxy S5
- iPhone 5/SE/6/7/8/Plus/X
- iPad (Normal & Pro)


## Key Issues and Code Validation
### W3C Markup Validator
- No errors or warnings were found on index.html, toys.html, toy_detail.html, blog_add.html, blog_detail.html, blog_edit.html, blogs.html, cart.html, checkout.html, checkout_success.html, login.html, logout.html, signup.html, profile.html, 500.html and 404.html

### W3C CSS Validator
- No manual coded related errors or warnings were found on base.css, index.css, blogs.css, checkout.css, toys.css, cart.css, profile.css, allauth.css and error.css
- Errors and warnings that were found are related to Bootstrap and can be ignored

### JSHint Validator
#### main.js
- The following errors and warnings were found on main.js:
    - Two undefined variables: **$** and **AOS**
- These errors can be ignored as they are needed for JQuery and AOS

#### stripe.js
- The following errors and warnings were found on stripe.js:
    - Two undefined variables: **$** and **Stripe**
- These errors can be ignored as they are needed for JQuery and Stripe

### Pep8 Online Validator
- No errors were found on all the apps
- Three warnings were found with a message that indicates that the **'line is too long'**. The warning won't affect the application and can be ignored

### Browser and Mobile testing
- No issues were found on Google Chrome, Mozilla Firefox, Microsoft Edge and Internet Explorer
- No issues were found on any mobile devices