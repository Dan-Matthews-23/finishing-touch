## Responsiveness Testing

### Testing

| Page         | Testing for                                            | Result |
| --- | --- | --- |
| index.html  | Is the page responsive across all Bootstrap breakpoints | Pass |
| login.html  | Is the page responsive across all Bootstrap breakpoints | Fail - allauth container too small |
| logout.html  | Is the page responsive across all Bootstrap breakpoints | |
| register.html  | Is the page responsive across all Bootstrap breakpoints | |
| sandwiches.html  | Is the page responsive across all Bootstrap breakpoints | Fail - no gaps between selections. Order info veers to left |
| basket.html.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint|
| checkout.html  | Is the page responsive across all Bootstrap breakpoints | Fail - container veers to left on smaller breakpoint|
| order_confirmed.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint|
| profile.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint |
| previous-orders.html  | Is the page responsive across all Bootstrap breakpoints | Fail - unresponsive on smaller breakpoint |

### Responsiveness testing conclusions

It's clear from the results of these tests that the mobile-first approach was not followed as well as it could have been. 