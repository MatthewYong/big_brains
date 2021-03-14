# Big Brains | Testing


## Table of Contents
- [Manual Testing](#manual-testing)
    * [Navigation Testing](#navigation-testing)
    * [Browser and Mobile Devices Testing](#browser-and-mobile-devices-testing)
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

