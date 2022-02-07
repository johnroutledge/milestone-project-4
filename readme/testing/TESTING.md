
## Testing

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
|  Basket page remove link                      | Click          |  Should remove product from basket                        | PASS          |
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