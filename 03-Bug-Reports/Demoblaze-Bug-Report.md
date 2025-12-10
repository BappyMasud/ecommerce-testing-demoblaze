# Bug Report – Demoblaze E-commerce Website

## Bug ID: BUG001
### Title:
Signup form accepts weak passwords

### Severity:
Medium  
### Priority:
Medium

### Description:
There is no password strength validation.

### Steps to Reproduce:
1. Open Sign Up  
2. Enter username: testweak  
3. Enter password: 1  
4. Click Sign Up

### Expected:
Password should require minimum length or complexity.

### Actual:
Signup is successful with a single-digit password.

### Evidence
- Screenshot of signup form with “1”
- Confirmation popup
---

## Bug ID: BUG002
### Title:
Cart does not update total price after deleting an item

### Severity:
High  
### Priority:
High

### Steps:
1. Add two products to cart  
2. Go to Cart  
3. Delete one product  
4. Check total price

### Expected:
Total price should decrease accordingly.

### Actual:
Total price stays the same.

### Evidence
- Cart before delete
- Cart after delete
- Total unchanged
---

## Bug ID: BUG003
### Title:
Place Order accepts empty credit card format

### Severity:
Medium  
### Priority:
Medium

### Description:
There is no password strength validation.

### Steps to Reproduce:
1. Add item to cart  
2. Go to Cart → Place Order  
3. Enter invalid card number like "abc"  
4. Click Purchase
   
### Expected:
The order does not accepted without valid credit card format.

### Actual:
Order is still accepted.

### Evidence
- Invalid card input
- Order confirmation displayed
---

## Bug ID: BUG004
### Title:
Category filter not updating product count properly

### Severity:
Medium  
### Priority:
Low

### Steps to Reproduce:
1. Click Phones  
2. Then click Next page  
3. Observe product list  
   
### Expected:
Products should be displayed according to the category listing.

### Actual:
Sometimes leftover items from the previous category appear.
