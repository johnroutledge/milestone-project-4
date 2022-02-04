
## Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|  Uppermost promotional offers banner          | Page load      |  Change every three seconds to different message          | PASS          |
|  Uppermost promotional offers banner          | Scroll         |  Disappear/reappear on scroll                             | PASS          |
|  Main navbar                                  | Scroll         |  Hide banner, then stick, then disappear                  | PASS          |
|  Jiira navbar logo                            | Click          |  Navigate to homepage from all pages                      | PASS          |
|  Navbar search box                            | Click          |  Return relevant items according to search term           | PASS          |
|  Navbar user profile icon                     | Click          |  Display relevant menu items                              | PASS          |
|  Navbar shopping basket icon                  | Click          |  Navigate to shopping basket page                         | PASS          |
|  Navbar links                                 | Click          |  Navigate to the correct pages                            | PASS          |
|  Navbar links                                 | View on mobile |  Should be visible as hamburger icon                      | PASS          |
|  Navbar links                                 | Hover          |  Pink underline fade up                                   | PASS          |
|  Hero image/video                             | Page load      |  Should be image on mobile, video on larger screens       | PASS          |
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
|  Product details page ratings count           | Page load      |  Show correct score and number of ratings                 | PASS          |
|  Product details page edit/delete links       | Page load      |  Only be visible for admin login                          | PASS          |
|  Product details page edit/delete links       | Click          |  Navigate to edit page or delete item                     | PASS          |
|  Product details page select size dropdown    | Page load      |  Only be visible for product with sizes                   | PASS          |
|  Product details page keep shopping button    | Click          |  Navigate to product page with all products               | PASS          |
|  Product details page add to basket button    | Click          |  Add product to basket, update and display basket toast   | PASS          |
|  Product details page reviews                 | Page load      |  Should display any reviews for the product               | PASS          |
|  Product details page review form             | Page load      |  Should allow entry of title, description and rating      | PASS          |
|  Product details page submit review button    | Click          |  Should correctly validate and save review                | PASS          |
|  News page images                             | Hover          |  Border shadow change to pink                             | FAIL********  |
|  News (blog) page images                      | Click          |  Should navigate to correct story                         | PASS          |
|  News (blog) page news story links            | Click          |  Should navigate to correct story                         | PASS          |
|  News (blog) detail page edit/delete links    | Page load      |  Only be visible for admin login                          | PASS          |
|  News (blog) detail comments                  | Page load      |  Should display any comments on the post                  | PASS          |
|  News (blog) detail comments form             | Page load      |  Should allow entry of name and comment                   | PASS          |
|  News (blog) detail comments form add button  | Click          |  Should correctly validate and save comment               | PASS          |



|  Navbar 'Portfolio' 'Prices' 'Trade' links   | After login    |  See only these links if user logged in                   | PASS          |
|  Navbar 'Transactions' 'Settings' 'Logout'    | After login    |  See only these links if user logged in                   | PASS          |
|  Register page input wrong data format        | Submit         |  Catch all incorrect data formats                         | PASS          |
|  Register page existing email address in db  | Submit         |  Display email already registered flash message           | PASS          |
|  Register page passwords not matching         | Submit         |  Display passwords do not match flash message             | PASS          |
|  Register page successful register            | Submit         |  Display registration successful flash message                       | PASS          |
|  Register page successful register            | Submit         |  Navigate to user's portfolio page                        | PASS          |
|  Register page link to login page             | Click          |  Navigate to sign-in page                                 | PASS          |
|  Sign-in page input wrong data format         | Submit         |  Catch all incorrect data formats                         | PASS          |
|  Sign-in page input wrong login details       | Submit         |  Display incorrect email/password flash message           | PASS          |
|  Sign-in page successful login                | Submit         |  Display user welcome back flash message                  | PASS          |
|  Sign-in page successful login                | Submit         |  Navigate to user's portfolio page                        | PASS          |
|  Sign-in page link to register page           | Click          |  Navigate to register page                                | PASS          |
|  Portfolio page member information            | Page load      |  Display name, join date, balance, loss/gain %            | PASS          |
|  Portfolio page portfolio change %            | Page load      |  Render in green text if gain, red text if loss           | PASS          |
|  Portfolio page cryptocurrency data           | Page load      |  Display logo, name, USD balance, coin quantity & code    | PASS          |
|  Portfolio page trade buttons                 | Click          |  Navigate to trade page and auto select chosen crypto     | PASS          |
|  Prices page cryptocurrency data              | Page load      |  Display logo, name, code, coin price, loss/gain %        | PASS          |
|  Prices page cryptocurrency change %          | Page load      |  Render in green text if gain, red text if loss           | PASS          |
|  Prices page extra cryptocurrency information | Click          |  Reveal/Hide hidden text when clicking on cryptocurrency  | PASS          |
|  Trade page (via portfolio 'trade' button)    | Page Load      |  Display correct 'buy' currency                           | PASS          |
|  Trade page 'buy' currency select list         | Page Load      |  List all cryptocurrencies in database                    | PASS          |
|  Trade page 'purchase using' select list      | Page Load      |  List only cryptocurrencies user has positive balance of  | PASS          |
|  Trade page input wrong data format           | Click Submit   |  Catch all incorrect data formats                         | PASS          |
|  Trade page input zero amount                 | Click Submit   |  Display amount entered cannot be zero flash message      | PASS          |
|  Trade page input duplicate currencies        | Click Submit   |  Display traded currencies must be different flash message| PASS          |
|  Trade page not enough cryptocurrency         | Click Submit   |  Display not enough cryptocurrency flash message          | PASS          |
|  Trade page successful trade                  | Click Submit   |  Display trade successfully processed flash message       | PASS          |
|  Trade page successful trade                  | Click Submit   |  Navigate to portfolio page and display new balances      | PASS          |
|  Transactions page user transactions          | Page load      |  Show no transactions text if no transaction history      | PASS          |
|  Transactions page user transactions          | Page load      |  List all user's transactions since registered/reset      | PASS          |
|  Transactions page user transactions          | Page load      |  Show date/time, amount bought, crypto logo & code        | PASS          |
|  Transactions page user transactions          | Page load      |  Show bought with crypto logo & code, price per coin      | PASS          |
|  Settings page                                | Page load      |  Display user first name, last name and portfolio balance | PASS          |
|  Settings page 'edit' button                  | Click          |  Navigate to edit settings page                           | PASS          |
|  Edit Settings page input wrong data format   | Click Save     |  Catch all incorrect data formats                         | PASS          |
|  Edit Settings page reset balance switch      | Set to 'off'   |  Not reset user's portfolio when saving                   | PASS          |
|  Edit Settings page reset balance switch      | Set to 'on'    |  Reset user's portfolio when saving                       | PASS          |
|  Edit Settings page successful save           | Click Save     |  Display settings successfully updated flash message      | PASS          |
|  Edit Settings page successful save           | Click Save     |  Display account reset flash message if reset balance on  | PASS          |
|  Edit Settings page successful save           | Click Save     |  Navigate back to settings page and display new data      | PASS          |
|  Edit Settings page 'cancel' button           | Click          |  Navigate back to settings page and display existing data | PASS          |
|  Logout navbar link                           | Click          |  Display log out successful flash message                 | PASS          |
|  Logout navbar link                           | Click          |  Navigate to sign-in page                                 | PASS          |
|  Media Query mobile screen size               | Resize screen  |  Page should render correctly on mobile screen            | PASS          |
|  Media Query tablet screen size               | Resize screen  |  Page should render correctly on tablet screen            | PASS          |
|  Media Query desktop screen size              | Resize screen  |  Page should render correctly on 14 inch screen           | PASS          |
|  Media Query 5k screen size                   | Resize screen  |  Page should render correctly on 5k screen                | PASS          |