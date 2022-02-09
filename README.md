<img src="static/images/logo_jiira.png" alt="Logo" width="15%" height="15%">


# Jiira
**Full Stack Frameworks with Django Milestone Project**

![Main Mockup](https://johnroutledge.github.io/milestone-project-4/readme/jiira_mockup.png "Main Mockup")
 
[Link to Live Website](https://jiira.herokuapp.com)

[GitHub Repo](https://github.com/johnroutledge/milestone-project-4)

**Rationale**

Jiira is a fully functional e-commerce website specialising in handmade jewellery from Thailand. Jiira's current online sales channels are through Facebook Marketplace and Lazada, a Thai version of Amazon/eBay. To extend Jiira's market outside of Thailand and to better showcase the product range, a tailor-made website is required.

This website is designed to promote Jiira's products and provide news on the company, while at the same time fulfulling the full stack framework milestone project four requirements of the Code Institue course.

It has e-commerce functionality for customers using Stripe for payments, has an admin area for the business owner to maintain the product range and blog posts which provide updates on Jiira's activity. Visitors to the website also have the ability to leave comments on the blog posts, giving them more interaction with the Jiira brand.


The typical user for the website would be someone who:
* Is interested in jewellery
* Is just browsing for jewellery ideas
* Is looking to buy jewellery
* Knows about Jiira
* Wants to find unique, handmade Thai Jewellery

People visiting this website are looking for:
* Fashionable Jewellery
* A range of earrings/necklaces/rings
* The latest in handmade jewellery
* Special discounts

Jiira is the ideal site for such people because:
* It includes all of the above in one place
* It has intuitive controls and layout
* It is both clear and concise in its layout
* The information it provides is kept to a minimum to avoid cognitive overload

***

## Index – Table of Contents

* [User Experience (UX)](#user-experience) 
* [Features](#features)
* [Technologies Employed](#technologies-employed)
* [Database](#database)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


***

## UX

**Strategy**

The business goal is to design and build a fully-functioning e-commerce site so that people can browse, choose and purchase Jiira's products. It also needs to encourage users to register so that they have access to their own profile and order history. This also gives the business owner the potential to market directly to registered users (subject to marketing opt-ins).

To satisfy user needs, the site must be visually appealing, unintimidating, simple to navigate and have intuitive design with stylish appearance. It should also be straightforward to search/select/add/edit/remove items to the basket as well as having a simple yet secure checkout.

From the business owner's point of view, the site must provide the ability to easily maintain the product offering. It should also enable the business owner to create brand loyalty through registration and sharing relevant news items about the company.

**Scope**

User Stories:

| # | As a/an       | I want to be able to...                          | So that I can...                            |
|---|---------------|--------------------------------------------------|---------------------------------------------|
| 1 | Shopper       | easily see what the page is about                | decide if it's relevant to my needs         |
| 2 | Shopper       | view the products                                | choose what I want to buy                   |
| 3 | Shopper       | view each product's details                      | learn more about its price/features/size    |
| 4 | Shopper       | see product reviews left by other shoppers       | so that I can make an informed purchase     |
| 5 | Shopper       | see the total of my shopping basket              | stay within my budget                       |
| 6 | Shopper       | sort products                                    | locate them quicker by price, name, type    |
| 7 | Shopper       | search for products                              | find what I'm looking for                   |
| 8 | Shopper       | see my search results                            | decide if it's what I want                  |
| 9 | Shopper       | choose qunatity and size of jewellery            | purchase exactly what I want                |
|10 | Shopper       | see what's in my shopping basket                 | make sure I have what I want and the cost   |
|11 | Shopper       | adjust my basket                                 | make easy udates before the checkout        |
|12 | Shopper       | easily enter my payment information              | pay quickly and confidently                 |
|13 | Shopper       | leave a review of a product                      | help other shoppers with their purchase     |
|14 | Shopper       | see an order confirmation                        | be sure I've made the correct purchase      |
|15 | Shopper       | receive an email copy of my order                | have physical proof of my purchase          |
|16 | Site User     | easily register for an account                   | make subsequent purchase quicker            |
|17 | Site User     | have email confirmation of registering           | be sure it was done correctly               |
|18 | Site User     | have my own Jiira profile                        | store my details and view purchase history  |
|19 | Site User     | easily login/logout                              | make subsequent purchases quicker           |
|20 | Site User     | contact Jiira directly                           | get an answer to my query                   |
|21 | Site User     | see the latest news about the company            | keep up to date with the brand              |
|22 | Site User     | comment on news items                            | share my views and show support             |
|23 | Store Owner   | add a product                                    | increase my offerings and make more money   |
|24 | Store Owner   | edit a product                                   | be sure details and prices are correct      |
|25 | Store Owner   | delete a product                                 | remove any out of trend/stock products      |
|26 | Store Owner   | add a news post                                  | inform users of Jiira's news and events     |
|27 | Store Owner   | edit a news post                                 | change the text/image                       |
|28 | Store Owner   | delete a news post                               | remove posts no longer relevant/suitable    |


**Structure**

To make sure the content/functionality is intuitive to navigate, I maintained consistency throughout the different pages by using the same layout/structure wherever possible and having standard header and footer elements. There is also a logical workflow throughout the site which signposts how users get specific information and where they can go to next.

On pages that take up more than the visible vertical area, I used content hinting so that users would be encouraged to scroll further down the page.

**Skeleton**

To make sure the app is intuitive to navigate and use, all UI elements are placed in such a way as to optimize the user journey through the website. For example, buttons and links are in similar locations on each page. Furthermore, by minimizing the amount of text content past the landing page, I also reduced distraction and maximized user engagement.

Wireframes

*Mobile*

* [Homepage](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_home.png)
* [Products](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_products.png)
* [Product Details](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_product_details.png)
* [Basket](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_basket.png)
* [Checkout](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_checkout.png)
* [News](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_news.png)
* [News Item](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_news_item.png)
* [Contact](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_contact.png)
* [Profile](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/mobile_profile.png)

*Tablet*

* [Homepage](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_home.png)
* [Products](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_products.png)
* [Product Details](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_product_details.png)
* [Basket](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_basket.png)
* [Checkout](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_checkout.png)
* [News](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_news.png)
* [News Item](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_news_item.png)
* [Contact](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_contact.png)
* [Profile](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/tablet_profile.png)

*Desktop*

* [Homepage](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_home.png)
* [Products](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_products.png)
* [Product Details](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_product_details.png)
* [Basket](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_basket.png)
* [Checkout](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_checkout.png)
* [News](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_news.png)
* [News Item](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_news_item.png)
* [Contact](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_contact.png)
* [Profile](https://johnroutledge.github.io/milestone-project-4/readme/images/wireframes/desktop_profile.png)


**Surface**

The 'Monserrat' Google font was chosen to give a clean and modern feel, while the white/grey/pink color scheme added to this style.

The color scheme was chosen as it feels clean and stylish, yet also soft in order to match the style of Jiira's product range. At the same time, it is both visually unintimidating and easy on the eye. The button color is consistent throughout the app to maintain consistency and increase the intuitiveness of the page.

The model hiding her face hero image was chosen for the landing page as it suggests the page is about jewellery, while at the same time evoking a slight feeling of intrigue and mystery often synonymous with Thailand. The large message within the hero image was used to give a clear, unambiguous description of what the website is about.

On larger screen sizes, a purpose-made video replaces the hero image. This video was made especially for Jiira jewellery and showcase some of the products. It is only viewable on larger screen sizes as they don't generally use mobile data and so usage it's not an issue. The video is not active on mobile or tablet as I didn't want to eat into people's data allowance which may cause them to have an unfavourable reaction to the website.

The Jiira logo used in the nav bar and favicon was to maintain consistency and reinforce the brand.  

***

## Features

**Implemented**

*Generic*
* Responsive design on the vast majority of devices
* Delivery banner which displays the purchase requirement for free delivery and also the first order discount.
* Navigation bar, including logo and link to the home page, a search box, an account icon and shopping basket icon which also displays the number of items currently in the basket.
* Links in the navigation bar collapse to a hamburger button on smaller devices such as smartphones and tablets.
* Toast messages giving users meaningful feedback to their actions on the website.
* Footer with with navigation links to all pages, Jiira's contact details, social media links and copyright information.
* 'Back to top' button where applicable.

*Homepage*
* Hero image with call to action button to encourage people to make a purchase.
* On larger screens, a video with models showing some of the jewellery Jiira has to offer.
* Product and about sections with fade-in images and text for the various jewellery Jiira has to offer and some background on the company.

*Product Pages*
* Clear pictures of the products.
* Ability to sort products by name and price.

*Product Details Page*
* The product detail page gives a larger image.
* Also gives users the ability to select a quantity to add to the basket.

*Basket Page*
* Shows all the products in the basket.
* The ability to ammend items in the basket.
* Also shows the total amount due, delivery costs and any applicable discount.

*Checkout Page*
* Users can enter delivery and payment information for their purchase.
* This information is pre-filled if the user already has logged in to their saved profile.
* Webhooks were employed to ensure smooth and secure transactions.

*News (Blog) Page*
Note: 'Blog' was renamed 'News' as it felt more stylish and in-line with the website's theme.
As it was changed towards the end of development, all 'blog' references were left in the code due to time constraints.

* Images along with truncated version of each news post and links to the full posts.
* Details of the author and date published.

*News (Blog) Detail*
* Each full news post along with any comments left by visitors to the site.
* A form where people can leave comments on a post (this includes a call to action to be the first to comment).
* The ability to edit or delete a news post (admin logins only).

*Contact Jiira Page*
* Gives a user the ability to contact Jiira directly via email.

*User Profile Page*
* User can edit their contact and delivery information held on the system.
* User can also see their order history.

**Future Features to Implement**
* A Thai version of the website.
* The ability to login using a social media account.
* A wishlist feature.
* Inventory tracking so stock availability can be shown on website.
* 'Track my order' functionality so that customers can see the status of their order.
* Confirmation when editing or deleting products for admin logins.
* Skip navigation links for visitors to the site with certain disablities to enhance their UX.
* The ability to accept or edit cookies.
* Marketing opt-in options on the registration page.


***

## Technologies Employed

*IDE*
* Gitpod

*Languages*
* Python
* HTML
* CSS
* JavaScript

*Frameworks, Templates & Libraries*
* Django
* JQuery
* Jinja
* Bootstrap
* Font Awesome
* Google Fonts

*Storage & Hosting*
* Heroku
* Github
* Amazon Web Services

*Databases*
* SQLite3 for development
* PostgresSQL for the deployed site

*Payment Service*
* Stripe

*Other Tools*
* Google Dev Tools (including Lighthouse)
* Pep8online.com (to check Python code for PEP 8 requirements)
* W3C Validator (to check validity of HTML and CSS)
* Code Beautify (to beautify JavaScript)
* dbdiagram.io (to produce the MongoDB ERD)


***

## Database

(NOT COMPLETE!!!)

The data was allocated across the following tables:

* Users - stores a user's personal information and undergoes CREATE, READ and UPDATE operations.
* Transactions - stores a user's transaction history has a many-to-one relation with the users table on the email address field. It undergoes CREATE, READ and DELETE operations.
* Categories - stores a user's current balances for each currency has a one-to-one relation with the users table on the email address field. It undergoes CREATE, READ and UPDATE operations.  
* Products - stores additional information about all of the cryptocurrencies and undergoes READ operations.
* Reviews - stores additional information about all of the cryptocurrencies and undergoes READ operations.
* News (Blog) - stores additional information about all of the cryptocurrencies and undergoes READ operations.


**Schema**

![ERD](https://johnroutledge.github.io/milestone-project-4/readme/images/jiira_erd.png "ERD")


***


## Testing

Due to the amount of information regarding testing, it has been detailed in the following separate [file](readme/testing/TESTING.md).


***

## Deployment

As with testing, due to the amount of information regarding deployment, it has been detailed in the following separate [file](readme/deployment/DEPLOYMENT.md).


***

## Credits

**Content**

- Product descriptions and blog posts were translated from Thai to English by my wife, Chonchanok Routledge.
- Cryptocurrency coin descriptions taken from wikipedia.com and investopedia.com

**Media**

- All images were taken by Jiratchaya Chaiyasak
- The Jiira logo was designed by Jiratchaya Chaiyasak
- All other icons used in the site are from FontAwesome.com and Bootstrap

**Code**

- Core setup, use of Django, linking to Stripe, Heroku, PostgresSQL and Amazon Web Services were all taken from the Code Institute's Full Stack Frameworks with Django Boutique Ado walkthrough project
- 
- Kevin Powell's YouTube channel video 'INSERT CREDIT'


**Acknowledgements**

- To Jira Chaiyasak for giving me the opportunity to develop this website for her.
- To my wife, my sister, and various work colleagues for testing the app on multiple devices.
- To my fellow Code Institute students who, via Slack, gave me guidance with various issues.
- To Brian Macharia, my Code Institute mentor, for giving me invaluable tips and insight throughout the whole process.