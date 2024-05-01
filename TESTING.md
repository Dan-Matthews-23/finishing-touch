## Responsiveness Testing

### Testing

| Page         | Testing for                                            | Result |
| --- | --- | --- |
| index.html  | Is the page responsive across all Bootstrap breakpoints | Pass |
| login.html  | Is the page responsive across all Bootstrap breakpoints | Fail - allauth container too small |
| logout.html  | Is the page responsive across all Bootstrap breakpoints | Fail - allauth container too small |
| register.html  | Is the page responsive across all Bootstrap breakpoints | Fail - allauth container too small |
| sandwiches.html  | Is the page responsive across all Bootstrap breakpoints | Fail - no gaps between selections. Order info veers to left |
| basket.html.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint|
| checkout.html  | Is the page responsive across all Bootstrap breakpoints | Fail - container veers to left on smaller breakpoint|
| order_confirmed.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint|
| profile.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint |
| previous-orders.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint |

### Re-testing failed elements

| Page         | Testing for                                            | Result |
| --- | --- | --- |

| login.html  | Is the page responsive across all Bootstrap breakpoints | Pass - allauth container now responsive |
| logout.html  | Is the page responsive across all Bootstrap breakpoints |  [Pass](/media/images/testing/sandwiches-b.png) - all elements now responsive|
| register.html  | Is the page responsive across all Bootstrap breakpoints | [Pass](/media/images/testing/sandwiches-b.png) - all elements now responsive|
| sandwiches.html  | Is the page responsive across all Bootstrap breakpoints | [Pass](/media/images/testing/sandwiches-b.png) - all elements now responsive |
| basket.html.html  | Is the page responsive across all Bootstrap breakpoints |  [Pass](/media/images/testing/basket-b.png) - all elements now responsive|
| checkout.html  | Is the page responsive across all Bootstrap breakpoints | [Pass](/media/images/testing/checkout-b.png) - all elements now responsive |
| order_confirmed.html  | Is the page responsive across all Bootstrap breakpoints |[Pass](/media/images/testing/order-confirmed-b.png) - all elements now responsive |
| profile.html  | Is the page responsive across all Bootstrap breakpoints | [Pass](/media/images/testing/profile-b.png) - all elements now responsive |
| previous-orders.html  | Is the page responsive across all Bootstrap breakpoints | [Pass](/media/images/testing/previous-orders-b.png) - all elements now responsive |

## Testing User Stories

![Testing User Stories](/media/images/testing/testing-user-stories.png)

## Known Bugs

### process_checkout

I spent hours with Tutor Support and the support team at Stripe to try and identify why my checkout page was redirecting to order_confirmed.html without processing payments, or why the intent was not recognised when I tried to fix it. In the end I was unable to resolve the issue itself so I had to implement a work-around. On checkout.html, I had to create the following input field:

HTML: ![Toggle HTML](/media/images/testing/known-bugs-toggle-hidden-html.png)

JavaScript ![Toggle JS](/media/images/testing/known-bugs-toggle-hidden-js.png)

Python ![Toggle Python](/media/images/testing/known-bugs-toggle-hidden-python.png)

The work-around means that once Process Checkout button is clicked, the event listener in the JavaScript changes the hidden input value to True. Once this is True, the Python function will execute the order, or it will render the form and stripe elements if not clicked. Of course this could be a security concern. If a hacker was able to manipulate this hidden form field, the order would execute without taking Stripe payment.

This work-around is not what I wanted or intended. I cannot save this in the 'Solved Bugs section as it's not solved, only mitigated. 

### basket_form

There is a bug in where the user updates their information on their profile, the full_name does not appear on the basket_form, nor the checkout_form. This means a user will need to add their full_name on each order. I've also engaged with Tutor Support with this problem but have been unable to resolve it so far. 




