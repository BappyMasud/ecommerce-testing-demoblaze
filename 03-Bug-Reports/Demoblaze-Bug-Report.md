# Bug Report – Demoblaze E-commerce Website

## Bug ID: BUG001
### Title:
Login form allows submission with empty fields

### Severity:
High  
### Priority:
High  

### Environment:
- Browser: Chrome 120  
- OS: Windows 10  
- URL: https://demoblaze.com  

### Precondition:
Website is loaded

### Steps to Reproduce:
1. Open the Login modal  
2. Leave both username & password empty  
3. Click "Log in"

### Expected Result:
System should show validation message or block submission.

### Actual Result:
The system attempts to log in (no error message).

### Evidence:
- Screenshot: (add later)  
- Video: (optional)

### Status:
Open
---

## Bug ID: BUG002
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
---

## Bug ID: BUG003
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
