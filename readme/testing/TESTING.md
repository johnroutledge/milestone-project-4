
# Testing

## Index – Table of Contents

* [Manual Testing](#manual-testing) 
* [User Stories Testing](#user-stories-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [HTML Testing](#html-testing)
* [CSS Testing](#css-testing)
* [JavaScript Testing](#javascript-testing)
* [Python Testing](#python-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [Notable Bug Fixes](#notable-bug-fixes)


## Manual Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  Uppermost promotional offers banner          | Page load      |  Change every three seconds to different message          | PASS          |
|  Uppermost promotional offers banner          | Scroll         |  Disappear/reappear on scroll                             | PASS          |
|  Main navbar                                  | Scroll         |  Hide banner, then stick, then disappear                  | PASS          |
|  Jiira navbar logo                            | Click          |  Navigate to homepage from all pages                      | PASS          |
|  Navbar search box                            | Click          |  Return relevant items according to search term           | PASS          |
|  Navbar user profile icon                     | Click          |  Display register and log in items if not logged in       | PASS          |
|  Navbar user profile icon                     | Click          |  Display my profile and log out options if logged in      | PASS          |
|  Navbar user profile icon                     | Click          |  Also display product & blog items if admin logged in     | PASS          |
|  Navbar shopping basket icon                  | Click          |  Navigate to shopping basket page                         | PASS          |
|  Navbar links                                 | Click          |  Navigate to the correct pages                            | PASS          |
|  Navbar links                                 | View on mobile |  Should be visible as hamburger icon                      | PASS          |
|  Navbar links                                 | Hover          |  Pink underline fade up                                   | PASS          |
|  Hero image/video                             | Page load      |  Should be image on mobile, video on larger screens       | PASS          |
|  First Order Discount CTA button              | Hover          |  Background change to pink and font to black              | PASS          |
|  First Order Discount CTA button              | Click          |  Navigate to products page and display all products       | PASS          |
|  Jewellery sections on homepage               | First scroll   |  Images and text should fade in                           | PASS          |
|  Jewellery section images on homepage         | Hover          |  Border shadow change to pink                             | PASS          |
|  Jewellery section images on homepage         | Click          |  Navigate to correct pages                                | PASS          |
|  Jewellery section titles on homepage         | Hover          |  Underline slide across                                   | PASS          |
|  Jewellery section titles on homepage         | Click          |  Navigate to corresponding pages                          | PASS          |
|  About section on homepage                    | First scroll   |  Text should fade in                                      | PASS          |
|  Site navigation links in footer              | Click          |  Navigate to the correct pages                            | PASS          |
|  Social Media links in footer                 | Click          |  Navigate to the correct social media homepages           | PASS          |
|  Register page                                | Page Load      |  Should correctly display input fields to register        | PASS          |
|  Register page back to log in button          | Hover          |  Background and font colors should invert                 | PASS          |
|  Register page back to log in button          | Click          |  Should navigate back to log in page                      | PASS          |
|  Register page sign up button                 | Hover          |  Background color change to pink and font to black        | PASS          |
|  Register page sign up button                 | Click          |  Should correctly validate all input fields               | PASS          |
|  Register page sign up button                 | Click          |  Once validated, should register and log the user in      | PASS          |
|  Register page sign up button                 | Click          |  Once validated, should display success toast             | PASS          |
|  Sign In page                                 | Page Load      |  Should correctly display input fields to sign in         | PASS          |
|  Sign In page home button                     | Hover          |  Background and font colors should invert                 | PASS          |
|  Sign In page home button                     | Click          |  Should navigate back to homepage                         | PASS          |
|  Sign In page page sign in button             | Hover          |  Background color change to pink and font to black        | PASS          |
|  Sign In page page sign in button             | Click          |  Should correctly validate all input fields               | PASS          |
|  Sign In page page sign in button             | Click          |  Once validated, should log the user in                   | PASS          |
|  Sign In page page sign in button             | Click          |  Once validated, should display success toast             | PASS          |
|  Products page category buttons               | Page load      |  Should display correct category                          | PASS          |
|  Products page category buttons               | Click          |  Should reload page and display items in that category    | PASS          |
|  Products page products home link             | Click          |  Should reload page and display all jewellery             | PASS          |
|  Products page product count                  | Page load      |  Should display correct number of products                | PASS          |
|  Products page sort dropdown                  | Click          |  Should sort results according to selected option         | PASS          |
|  Products page product images                 | Hover          |  Border shadow change to pink                             | PASS          |
|  Products page product images                 | Click          |  Navigate to product details page for chosen product      | PASS          |
|  Products page edit/delete links              | Page load      |  Only be visible for admin login                          | PASS          |
|  Products page edit/delete links              | Click          |  Navigate to edit page or delete item                     | PASS          |
|  Products page edit/delete links              | Click          |  Success toast should be displayed                        | PASS          |
|  Product details page ratings count           | Page load      |  Show correct score and number of ratings                 | PASS          |
|  Product details page edit/delete links       | Page load      |  Only be visible for admin login                          | PASS          |
|  Product details page edit/delete links       | Click          |  Navigate to edit page or delete item                     | PASS          |
|  Product details page select size dropdown    | Page load      |  Only be visible for product with sizes                   | PASS          |
|  Product details page keep shopping button    | Hover          |  Background and font colors should invert                 | PASS          |
|  Product details page keep shopping button    | Click          |  Navigate to product page with all products               | PASS          |
|  Product details page add to basket button    | Hover          |  Background change to pink and font to black              | PASS          |
|  Product details page add to basket button    | Click          |  Add product to basket, update and display basket toast   | PASS          |
|  Product details page add to basket button    | Click          |  Success toast should be displayed                        | PASS          |
|  Product details page reviews                 | Page load      |  Should display any reviews for the product               | PASS          |
|  Product details page review form             | Page load      |  Should allow entry of title, description and rating      | PASS          |
|  Product details page submit review button    | Hover          |  Background change to pink and font to black              | PASS          |
|  Product details page submit review button    | Click          |  Should correctly validate and save review                | PASS          |
|  Basket page                                  | Page load      |  Should show correct count of basket items                | PASS          |
|  Basket page                                  | Page load      |  Should show all products in basket                       | PASS          |
|  Basket page                                  | Page load      |  Should show correct quantities and subtotals             | PASS          |
|  Basket page update link                      | Click          |  Should update product quantity, subtotal and total       | PASS          |
|  Basket page update link                      | Click          |  Should display success toast                             | PASS          |
|  Basket page remove link                      | Click          |  Should remove product from basket                        | PASS          |
|  Basket page remove link                      | Click          |  Should display success toast                             | PASS          |
|  Basket page basket total                     | Page load      |  Should show correct basket total price                   | PASS          |
|  Basket page first order discount CTA         | Page load      |  Should show first order discount CTA if not logged in    | PASS          |
|  Basket page first order discount             | Page load      |  Should show correct discount if customer's first order   | PASS          |
|  Basket page total                            | Page load      |  Should show correct total price after any discount       | PASS          |
|  Basket page delivery charge CTA              | Page load      |  Should show CTA if delivery threshold not reached        | PASS          |
|  Basket page delivery charge                  | Page load      |  Should show correct delivery amount                      | PASS          |
|  Basket page grand total                      | Page load      |  Should show correct grand total                          | PASS          |
|  Basket page continue shopping button         | Hover          |  Background and font colors should invert                 | PASS          |
|  Basket page continue shopping button         | Click          |  Navigate to product page with all products               | PASS          |
|  Basket page secure checkout button           | Hover          |  Background change to pink and font change to black       | PASS          |
|  Basket page secure checkout button           | Click          |  Navigate to checkout page                                | PASS          |
|  Checkout page                                | Page load      |  Should display input field for delivery information      | PASS          |
|  Checkout page                                | Page load      |  Should correctly display all products in basket          | PASS          |
|  Checkout page                                | Page load      |  Should correctly display all discounts, totals, charges  | PASS          |
|  Checkout page adjust basket button           | Hover          |  Background and font colors should invert                 | PASS          |
|  Checkout page adjust basket button           | Click          |  Should navigate back to basket page                      | PASS          |
|  Checkout page complete order button          | Hover          |  Background color change to pink and font to black        | PASS          |
|  Checkout page complete order button          | Click          |  Should correctly validate all input fields               | PASS          |
|  Checkout page complete order button          | Click          |  Process payment and load thank you page                  | PASS          |
|  Checkout page complete order button          | Click          |  Success toast should be displayed with order details     | PASS          |
|  Checkout page card charge message            | Page load      |  Should display warning message with correct grand total  | PASS          |
|  Thank you page                               | Page load      |  Should display order summary                             | PASS          |
|  Thank you page back to jewellery button      | Hover          |  Background color change to pink and font to black        | PASS          |
|  Thank you page back to jewellery button      | Click          |  Navigate to products page with all products              | PASS          |
|  News page images                             | Hover          |  Border shadow change to pink                             | PASS          |
|  News (blog) page images                      | Click          |  Should navigate to correct story                         | PASS          |
|  News (blog) page news story links            | Click          |  Should navigate to correct story                         | PASS          |
|  News (blog) detail page edit/delete links    | Page load      |  Only be visible for admin login                          | PASS          |
|  News (blog) detail comments                  | Page load      |  Should display any comments on the post                  | PASS          |
|  News (blog) detail comments form             | Page load      |  Should allow entry of name and comment                   | PASS          |
|  News (blog) detail comments form add button  | Hover          |  Background color change to pink and font to black        | PASS          |
|  News (blog) detail comments form add button  | Click          |  Should correctly validate and save comment               | PASS          |
|  News (blog) detail comments form back button | Hover          |  Background and font colors should invert                 | PASS          |
|  News (blog) detail comments form back button | Click          |  Navigate back to main News (blog) page                   | PASS          |
|  Contact page contact form send button        | Page load      |  Should display empty fields for a new message            | PASS          |
|  Contact page contact form send button        | Hover          |  Background color change to pink and font to black        | PASS          |
|  Contact page contact form send button        | Click          |  Should correctly validate all input fields               | PASS          |
|  Contact page contact form send button        | Click          |  Should send an email to the Jiira email address          | PASS          |
|  My Profile page                              | Page Load      |  Should correctly display delivery information            | PASS          |
|  My Profile page                              | Page Load      |  Should correctly display order history                   | PASS          |
|  My Profile page update information button    | Hover          |  Background color change to pink and font to black        | PASS          |
|  My Profile page update information button    | Click          |  Should correctly validate all input fields               | PASS          |
|  My Profile page update information button    | Click          |  Should save updated default delivery information         | PASS          |
|  Product Management page                      | Page Load      |  Should display empty fields for a new product            | PASS          |
|  Product Management page category drop down   | Click          |  Should display all available categories                  | PASS          |
|  Product Management page has sizes drop down  | Click          |  Should display correct options                           | PASS          |
|  Product Management page select image button  | Hover          |  Background color change to pink and font to black        | PASS          |
|  Product Management page select image button  | Click          |  Should display file explorer modal                       | PASS          |
|  Product Management page add product button   | Hover          |  Background color change to pink and font to black        | PASS          |
|  Product Management page add product button   | Click          |  Should correctly validate all input fields               | PASS          |
|  Product Management page add product button   | Click          |  Should save new product if data successfully validated   | PASS          |
|  Product Management page add product button   | Click          |  Success toast should be displayed                        | PASS          |
|  Product Management page cancel button        | Hover          |  Background and font colors should invert                 | PASS          |
|  Product Management page cancel button        | Click          |  Should return to products page and display all products  | PASS          |
|  News Management page                         | Page Load      |  Should display empty fields for a news item              | PASS          |
|  News Management page choose file button      | Hover          |  Background color change to darker gray                   | PASS          |
|  News Management page choose file button      | Click          |  Should display file explorer modal                       | PASS          |
|  News Management page save news post button   | Hover          |  Background color change to pink and font to black        | PASS          |
|  News Management page save news post button   | Click          |  Should correctly validate all input fields               | PASS          |
|  News Management page save news post button   | Click          |  Should save news post if data successfully validated     | PASS          |
|  News Management page save news post button   | Click          |  Success toast should be displayed                        | PASS          |
|  News Management page cancel button           | Hover          |  Background and font colors should invert                 | PASS          |
|  News Management page cancel button           | Click          |  Should return to news page                               | PASS          |
|  Logout confirmation page                     | Page load      |  Should display confirmation question                     | PASS          |
|  Logout confirmation page cancel button       | Hover          |  Background and font colors should invert                 | PASS          |
|  Logout confirmation page cancel button       | Click          |  Remain logged in and navigate to homepage                | PASS          |
|  Logout confirmation page sign out button     | Hover          |  Background color change to pink and font to black        | PASS          |
|  Logout confirmation page sign out button     | Click          |  Log user out and navigate to homepage                    | PASS          |
|  Logout confirmation page sign out button     | Click          |  Display success toast stating user signed out            | PASS          |
|  Media Query mobile screen size               | Resize screen  |  Page should render correctly on mobile screen            | PASS          |
|  Media Query tablet screen size               | Resize screen  |  Page should render correctly on tablet screen            | PASS          |
|  Media Query desktop screen size              | Resize screen  |  Page should render correctly on 14 inch screen           | PASS          |
|  Media Query 5k screen size                   | Resize screen  |  Page should render correctly on 5k screen                | PASS          |



## User Stories Testing

| # | As a/an       | I want to be able to...                          | So that I can...                            | Test Outcome  |
|---|---------------|--------------------------------------------------|---------------------------------------------|---------------|
| 1 | Shopper       | easily see what the page is about                | decide if it's relevant to my needs         | PASS          |
| 2 | Shopper       | view the products                                | choose what I want to buy                   | PASS          |
| 3 | Shopper       | view each product's details                      | learn more about its price/features/size    | PASS          |
| 4 | Shopper       | see product reviews left by other shoppers       | so that I can make an informed purchase     | PASS          |
| 5 | Shopper       | see the total of my shopping basket              | stay within my budget                       | PASS          |
| 6 | Shopper       | sort products                                    | locate them quicker by price, name, type    | PASS          |
| 7 | Shopper       | search for products                              | find what I'm looking for                   | PASS          |
| 8 | Shopper       | see my search results                            | decide if it's what I want                  | PASS          |
| 9 | Shopper       | choose qunatity and size of jewellery            | purchase exactly what I want                | PASS          |
|10 | Shopper       | see what's in my shopping basket                 | make sure I have what I want and the cost   | PASS          |
|11 | Shopper       | adjust my basket                                 | make easy udates before the checkout        | PASS          |
|12 | Shopper       | easily enter my payment information              | pay quickly and confidently                 | PASS          |
|13 | Shopper       | leave a review of a product                      | help other shoppers with their purchase     | PASS          |
|14 | Shopper       | see an order confirmation                        | be sure I've made the correct purchase      | PASS          |
|15 | Shopper       | receive an email copy of my order                | have physical proof of my purchase          | PASS          |
|16 | Site User     | easily register for an account                   | make subsequent purchase quicker            | PASS          |
|17 | Site User     | have email confirmation of registering           | be sure it was done correctly               | PASS          |
|18 | Site User     | have my own Jiira profile                        | store my details and view purchase history  | PASS          |
|19 | Site User     | easily login/logout                              | make subsequent purchases quicker           | PASS          |
|20 | Site User     | contact Jiira directly                           | get an answer to my query                   | PASS          |
|21 | Site User     | see the latest news about the company            | keep up to date with the brand              | PASS          |
|22 | Site User     | comment on news items                            | share my views and show support             | PASS          |
|23 | Store Owner   | add a product                                    | increase my offerings and make more money   | PASS          |
|24 | Store Owner   | edit a product                                   | be sure details and prices are correct      | PASS          |
|25 | Store Owner   | delete a product                                 | remove any out of trend/stock products      | PASS          |
|26 | Store Owner   | add a news post                                  | inform users of Jiira's news and events     | PASS          |
|27 | Store Owner   | edit a news post                                 | change the text/image                       | PASS          |
|28 | Store Owner   | delete a news post                               | remove posts no longer relevant/suitable    | PASS          |


## Responsiveness Testing
The website was tested on various screen sizes using Chrome DevTools, from iPhone5 up to 5k screen.

It was also tested using [Am I Responsive](http://ami.responsivedesign.is/) and the results were as per the following image:

![Main Mockup](/readme/images/jiira_mockup.png "Main Mockup")

## Testing Browser Compatibility

The website was successfully opened and rendered correctly in Chrome (both desktop and mobile versions), Edge and Safari.


## HTML Testing
HTML was validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option.

The main errors which had to be fixed were all within the basket app and related to duplicate IDs on the quantity-form.html, one of which is shown
in the following image:

![HTML Test Errors](/readme/images/code/html_test_errors.png "HTML Test Errors")

These occured because
basket.html references the quantity-form twice, and hides one depending on the device size (mobile or desktop). To fix the errors, the IDs in question were changed to classes and the javascript was also changed to look for the class rather than ID.

Having remedied the above errors, all HTML checks resulted in warnings as per the image below. These were non-critical issues and therefore not fixed following advice from my tutor.

![HTML Test Warnings](/readme/images/code/html_test_warnings.png "HTML Test Warnings")


## CSS Testing
CSS was validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option.

Results of all tests came back with the same 'no errors found' message, as per the image below:

![CSS Test Results](/readme/images/code/css_test_results.png "CSS Test Results")


## JavaScript Testing

JavaScript was tested with [JSHint](https://jshint.com/) JavaScript linter. Warnings were thrown up (as per the images below), but no errors or anything which required a code change.  Some examples of the JavaScript test results are as follows:

#### base.js<br>
![Base.js Test Results](/readme/images/code/base_js.png "Base.js Test Results")

#### observers.js<br>
![Observers.js Test Results](/readme/images/code/observers_js.png "Observers.js Test Results")

#### basket.html javascript<br>
![Basket.html JavaScript Test Results](/readme/images/code/basket_html_js.png "Basket.html JavaScript Test Results")

#### banner text javascript<br>
![Changing Banner Text JavaScript Test Results](/readme/images/code/changing_banner_text_js.png "Changning Banner Text JavaScript Test Results")


## Python Testing
Python code from all .py files was checked using [Pep8online](https://www.pep8online.com).

The first check on each file brought back numerous errors which were all rectified (see note below), so subsequent tests all passed. A small selection of results are shown in the screenshot below:

![Python Test Results](/readme/images/code/python_test_results.png "Python Test Results")

Note: There was one 'line too long' error (see bottom-right screenshot in above image) in settings.py which wasn't fixed after consulting with my mentor. I also checked on Slack and several other students' MS4 projects (which had passed grading), all of which left the same error alone.


## Lighthouse Testing
The results shown in the images below are for the home, products, basket, checkout, news item and contact pages on both mobile and desktop. These were chosen as they produced the lowest figures and best illustrate the gains made by implementing Lighthouse's recommended changes.

All improvements were made to the accessibilty scores as these were the lowest on all tests. To improve the scores, an 'alt' value was given to the Jiira logo and 'aria-label' values were given to the search icon in the navbar (both mobile and desktop) and quantity controls in the basket page.


![Homepage Results](/readme/images/lighthouse/lighthouse_home_page.png "Homepage Results")


![Products Page Results](/readme/images/lighthouse/lighthouse_products_page.png "Products Page Results")


![Basket Page Results](/readme/images/lighthouse/lighthouse_basket_page.png "Basket Page Results")


![Checkout Page Results](/readme/images/lighthouse/lighthouse_checkout_page.png "Checkout Page Results")


![News Item Page Results](/readme/images/lighthouse/lighthouse_news_item_page.png "News Item Page Results")


![Contact Page Results](/readme/images/lighthouse/lighthouse_contact_page.png "Contact Page Results")


## Notable Bug Fixes

1. User Profile Drop-Down Menu

In an early version of the website, when clicking on the user profile icon in the navbar, the resulting drop-down menu appeared partially off screen (see screenshots below). This occured on both mobile and desktop versions. To fix the issue, the class 'dropdown-menu-right' was added to the offending div in both 'base.html' and 'mobile-top-header-html'. 

![User Profile Menu Bug](/readme/images/code/user-profile-menu-bug.png "User Profile Menu Bug")


2. Review Form Bug

Towards the end of the development of the website, I decided to add the 'reviews' app in order to give users the ability to add product reviews. Once the initial code was in place, the review form wasn't appearing on the product details page. Having read and re-read my code for over an hour, I finally realised that it was a simple naming mistake in the view which was causing the problem. While a was passing a 'form' in, I had called it 'review_form' instead of 'form'. Once I changed the name to just 'form', the reivew form then rendered correctly on the page product details page. Below are screenshots of the code before and after the changes.

![Review Form Bug](/readme/images/code/review-form-bug.png "Review Form Bug")
