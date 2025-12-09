# Test Cases for Demoblaze E-commerce Website

## 1. User Registration / Signup

| TC ID | Test Case Description | Precondition | Steps | Test Data | Expected Result | Actual Result | Priority | Results | Commnents |
|------|------------------------|--------------|--------|-----------|-----------------|---------------|----------|---------|------------|
| TC001 | Verify user can open signup dialog | Website is loaded | 1. Click "Sign Up" | N/A | Signup modal should open | Signup model has been opened | P1 | PASS |
| TC002 | Verify signup with valid data | Signup modal open | 1. Enter valid username + password 2. Click Sign Up | username: test123, pass: Test@123 | Success alert: "Sign up successful" | Sign up is successful | P1 | PASS |
| TC003 | Verify signup with existing user | Existing account | 1. Enter same username 2. Click Sign Up | username: test123 | Error alert: "This user already exist" | Showed alert: "This user already exist" | P4 | PASS |
| TC004 | Verify signup with empty fields | Signup modal open | Leave fields blank → Click Sign Up | blank | Browser should show validation or error | Showed alart: "Please fill out username & password" | P3 | PASS |

---

## 2. Login

| TC ID | Test Case Description | Precondition | Steps | Test Data | Expected Result | Actual Result | Priority | Results | Commnents |
|------|------------------------|--------------|--------|-----------|-----------------|---------------|----------|---------|------------|
| TC005 | Verify user login with valid credentials | User exists | 1. Open Login modal 2. Enter valid creds 3. Click Login | username: sohel123, pass: sohel@123 | Login success → Username appears on navbar | Login success → Username appears on navbar | P1 | PASS | 
| TC006 | Verify login with invalid password | User exists | Same as above | wrong pass | Alert: "Wrong password" or login failure | Showed alert: "Wrong password" | P3 | PASS |
| TC007 | Verify login with non-existing user | None | Same | random username | Alert: "User does not exist" | Showed alert: "User does not exist" | P4 | PASS |
| TC008 | Verify login with empty fields | None | Leave fields empty | blank | Should not login | Showed alart: "Please fill out Username and Password" | P3 | PASS |

---

## 3. Product Browsing & Categories

| TC ID | Test Case Description | Precondition | Steps | Test Data | Expected Result | Actual Result | Priority | Results | Commnents |
|------|------------------------|--------------|--------|-----------|-----------------|---------------|----------|---------|------------|
| TC009 | Verify all product categories appear | None | View homepage | All categories displayed | All categories displayed | P2 | PASS |
| TC010 | Verify filtering by category | None | Click Phones/Laptops/Monitors | Products related to that category shown | Products related to that category shown | P3 | PASS |
| TC011 | Verify product details page | None | Click any product | Product image, price, description displayed | Product image, price, description displayed | P2 | PASS |

---

## 4. Cart Functionality

| TC ID | Test Case Description | Precondition | Steps | Test Data | Expected Result | Actual Result | Priority | Results | Commnents |
|------|------------------------|--------------|--------|-----------|-----------------|---------------|----------|---------|------------|
| TC012 | Add item to cart | Logged in | Open product → Click "Add to cart" | Alert: “Product added” | Shown alert: “Product added” | P0 | PASS | 
| TC013 | Remove item from cart | Item exists in cart | Go to Cart → Delete an item | Item should be removed | Item is removed | P3 | PASS |
| TC014 | Verify cart total updates | Items in cart | Add 2 items | Total price = sum of products | Shown sum of products accurately | P0 | PASS |

---

## 5. Checkout / Place Order

| TC ID | Test Case Description | Precondition | Steps | Test Data | Expected Result | Actual Result | Priority | Results | Commnents |
|------|------------------------|--------------|--------|-----------|-----------------|---------------|----------|---------|------------|
| TC015 | Place order with valid data | Items in cart | 1. Go to Cart 2. Click "Place Order" 3. Fill form 4. Purchase | Order placed → Confirmation popup |
| TC016 | Try placing order with empty fields | Items in cart | Click Purchase without data | Alert or validation |
| TC017 | Verify purchase confirmation data | Order placed | Observe popup | Should show amount + Name + Credit Card |

---

## 6. Logout

| TC ID | Description | Precondition | Steps | Expected Result |
|------|-------------|--------------|--------|-----------------|
| TC018 | Verify user logout | Logged in | Click Logout | Login/Signup buttons reappear |

---

## 7. UI Test Cases

| TC ID | Description | Precondition | Steps | Expected Result |
|------|-------------|--------------|--------|-----------------|
| TC019 | Verify homepage UI loads properly | None | Load homepage | All UI components visible |
| TC020 | Verify responsiveness | Resize browser | Adjust window size | UI should not break |
