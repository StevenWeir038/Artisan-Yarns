# Manual Testing

## Navigation
### Autentication
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Sign Up link | redirects unauth to Sign Up page | click on link | redirects to Sign Up page | Pass |
| Sign In link |  redirects  unauth to Sign In page| click on link | redirects to Sign In page | Pass |
| Sign Out link | redirects auth user to Sign Out page | click on link | redirects to Sign Out page | Pass |
| Sign Up page button | on success, redirects user to confirm email page and displays info toast for user to check their email | click sign in button | on success, redirects user to confirm email page and displays info toast for user to check their email | Pass |
| Confirm page button | clicking on sent email link takes user back to the site's confirm email page, confirm button verifies their email, redirects to the sign in page and displays success toast | click confirm button | clicking on sent email link takes user back to the site's confirm email page, confirm button verifies their email, redirects to the sign in page and displays success toast | Pass |
| Sign In page button | redirects auth user to homepage and displays success toast with auth users name page OR remains on sign in page and display error message stating incorrect username/password | click sign in button | redirects auth user to homepage and displays success toast with auth users name page OR remains on sign in page and display error message stating incorrect username/password | Pass |
| Sign Out page button | redirects auth user to homepage and displays success toast with signed out message  | click sign out button | redirects auth user to homepage and displays success toast with signed out message | Pass |

### Header Site Links
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Home image | redirect to homepage from anywhere in site | click on homepage link  | navigates to home | Pass |
| Contact button | redirect to contact page from anywhere in site | click on contact page button | navigates to contact page | Pass |
| Help button | opens help modal | click on help button  | opens help modal | Pass |
| Wishlist button (visible to auth users only) | redirect to wishlist page from anywhere in site | click on wishlist button | navigates to wishlist page | Pass |
| Basket button | redirect to basket page from anywhere in site | click on basket button | navigates to basket page | Pass |
| Account button (unauth users) | dropdown menu opens with 2 options - Sign Up / Sign In | click on account button | dropdown menu opens with 2 options - Sign Up / Sign In | Pass |
| Account button (auth standard users) | dropdown menu opens with 2 options - My Acccount / Sign Out | click on account button | dropdown menu opens with 2 options - My Acccount / Sign Out | Pass |
| Account button (auth superusers) | dropdown menu opens with 3 options - Product Management / My Acccount / Sign Out | click on account button | dropdown menu opens with 3 options - Product Management / My Acccount / Sign Out | Pass |

### Header Product Menu
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Products menu item | shows dropdown menu with 3 options for all products, price, category | click on products menu item  | shows dropdown menu with 3 options for all products, price, category | Pass |
| Products menu list items | redirects to filtered all_product page containing items for all products | click on products menu list item  | redirects to filtered all_product page containing items for all products | Pass |
| Products menu list items | redirects to filtered all_product page containing items with list item name in its `category` field | click on products menu list item  | redirects to filtered all_product page containing items with list item name in its `category` field | Pass |
| Yarns menu item | shows dropdown menu with 5 options for all yarns, and each name from the `brand` field in the `Product` model | click on products menu item  | shows dropdown menu with 5 options for all yarns, and each name from the `brand` field in the `Product` model | Pass |
| Yarns menu list items | redirects to filtered all_product page containing items from all categories excluding `other` | click on yarns menu list item  | redirects to filtered all_product page containing items with list item name in its `category` field | Pass |
| Yarns menu list items | redirects to filtered all_product page containing items with list item name in its `category` field | click on yarns menu list item  | redirects to filtered all_product page containing items with list item name in its `category` field | Pass |
| Clearance menu item | redirects to filtered all_product page containing items with `clearance` in their `category` field | click on clearance menu item  | redirects to filtered all_product page containing items with `clearance` in their `category` field | Pass 
| Accessories menu item | redirects to filtered all_product page containing items with `accessories` in their `category` field | click on accessories menu item  | redirects to filtered all_product page containing items with `accessories` in their `category` field | Pass 

### Footer Back To Top Button
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| btt button | auto scrolls to top of current page | click btt button | auto scrolls to top of current page | Pass |

### Footer Site Links
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Home image | redirect to homepage from anywhere in site | click on homepage link  | navigates to home | Pass |
| Contact link | redirect to contact page from anywhere in site | click on contact page link | navigates to contact page | Pass |
| Help link | opens help modal | click on help link  | opens help modal | Pass |
| Wishlist link (visible to auth users only) | redirect to wishlist page from anywhere in site | click on wishlist link | navigates to wishlist page | Pass |
| Basket link | redirect to basket page from anywhere in site | click on basket link | navigates to basket page | Pass |
| Account link (unauth users) | dropdown menu opens with 2 options - Sign Up / Sign In | click on account link | dropdown menu opens with 2 options - Sign Up / Sign In | Pass |
| Account link (auth standard users) | dropdown menu opens with 2 options - My Acccount / Sign Out | click on account link | dropdown menu opens with 2 options - My Acccount / Sign Out | Pass |
| Account link (auth superusers) | dropdown menu opens with 3 options - Product Management / My Acccount / Sign Out | click on account link | dropdown menu opens with 3 options - Product Management / My Acccount / Sign Out | Pass |

### Footer External Site Links
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Facebook Icon | redirect to external facebook page from anywhere in site | click on facebook icon link  | navigates to external facebook page | Pass |
| Instagram Icon | redirect to external instagram page from anywhere in site | click on instagram icon link  | navigates to external instagram page | Pass |
| GitHub Icon | redirect to developers personal github page (new tab/external) from anywhere in site | click on github icon link  | navigates to developers personal github page (new tab/external) | Pass |

## Header Searchbar
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| searchbar form input | redirects to filtered all_product page containing items with the search parameter in their title or description | type something into search form | redirects to filtered all_product page containing items with the search parameter in their title or description | Pass |
| searchbar for input | redirects to product page and displays error toast if no input made when search form submitted | type nothing into search form and submit | redirects to product page and displays error toast if no input made when search form submitted | Pass |

## Footer Newsletter
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| email form input | valid email triggers success toast, redirects to newsletter, sends email to recipient | enter valid email to form input or with an `@` | valid email triggers success toast, redirect to newsletter page, sends email to recipient | Pass |
| email form input | invalid email triggers warning to fill out field | enter with no input or without `@` | triggers warning to fill out field. Focus reset to input field for another try | Pass |
| subscribe button | performs valid/invalid action depending on input field | click subscribe button | performs valid/invalid action depending on input field | Pass |

### Homepage
| FEATURE | EXPECTED | TEST METHOD | RESULT | PASS/FAIL |
| -- |--| --| -- | :--: |
| Enter store image | navigates to all_product page | click on enter store image | navigates to all_product page | Pass |
| Clearance image | navigates to all_product page filtered for clearance items only | click on clearance image | navigates to all_product page filtered for clearance items only | Pass |
| Schweepjes image | navigates to all_product page filtered for schweepjes items only | click onschweepjes image | navigates to all_product page filtered for schweepjes items only | Pass |
| Lighter Weights image | navigates to all_product page filtered for items with a value of `Light` in the `Product` model `weight` field | click on lighter weights image | navigates to all_product page filtered for items with a value of `Light` in the `Product` model `weight` field | Pass |
| Accessories image | navigates to all_product page filtered for accessories items only | click on accessories image | navigates to all_product page filtered for accessories items only | Pass |


### Products Pages
#### Products
#### Product Details
#### Reviews

#### Add Product
#### Edit Product
#### Delete Product

### Basket

### Checkout
### Wishlist



## Browsers
## Lighthouse
## Validation Checks
### HTML
### Jigsaw
### JSHint
### PEP8


[Back to contents](#contents)
[Back to Readme](README.md)