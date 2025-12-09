# Test Plan — Demoblaze E-commerce Website

## 1. Document Info  
- **Test Plan ID**: TP-Demoblaze-v1  
- **Date**: YYYY-MM-DD  
- **Prepared by**: Bappy Masud  
- **Version**: 1.0  

## 2. Introduction & Objectives  
Brief description of Demoblaze and what this test plan aims to achieve.  
**Objectives**:  
- Validate core functionalities of the website (user flows, cart, checkout, login/signup).  
- Identify functional bugs.  
- Ensure the website behaves correctly under normal load (later phases).  
- Provide deliverables (test cases, reports) to demonstrate full testing coverage in portfolio.

## 3. Scope  
**In-Scope (Features / Functions to test)**:  
- User registration / login / logout  
- Browsing product catalog (categories, product details)  
- Searching / filtering (if exists)  
- Adding items to cart  
- Removing items from cart / Updating quantities  
- Checkout / Order placement (if applicable)  
- UI/UX across major browsers (Frontend)  
- Backend flows: data persistence, order processing  

**Out-of-Scope** (for now):  
- Payment gateway integrations (if external / third-party)  
- Advanced security tests (penetration, vulnerability scanning) — optional future work  
- Mobile-app (since Demoblaze is web only)  

## 4. Test Strategy / Approach  
**Testing Types**:  
- Manual Testing (functional, UI, exploratory)  
- Automation Testing (regression for repeatable flows)  
- API Testing (if Demoblaze provides public or semi-public APIs)  
- Performance Testing (load, stress)  

**Approach**:  
- Start with manual testing to cover all major flows and write test cases.  
- Use automation for repeatable, high-value user flows (login, add-to-cart, checkout, logout).  
- Use API testing for backend where possible (if endpoints accessible).  
- Use performance testing to simulate users/transactions under load (later phases).  

## 5. Test Environment & Tools  
- Browsers: Chrome (latest), Firefox (latest), optionally Edge.  
- OS: Windows 11  
- For automation: Selenium, Python, browser-driver (e.g. ChromeDriver).  
- For API testing: Postman.  
- For performance testing: JMeter.  
- For documentation: Markdown files / Excel / CSV for test cases.  
- Test data: sample user accounts, sample products (use existing products on Demoblaze), edge cases (empty fields, invalid input).  

## 6. Test Schedule & Estimation (high-level)  
| Phase | Start Date | End Date | Deliverables |
|---|---|---|---|  
| Test Plan & Strategy | **today** | +1 day | Test Plan document |  
| Test Case Design & Review | +1 day | +2 days | Test Cases (manual) |  
| Manual Test Execution | +3 days | +5 days | Test execution results, Bug reports |  
| Automation Script Development | +6 days | +10 days | Automation framework, scripts |  
| API Testing | +6 days | +8 days | Postman collection + reports |  
| Performance Testing | +9 days | +11 days | Load / stress test scripts + report |  
| Test Summary & Closure | +12 days | +12 days | Final test report, metrics, README |  

## 7. Test Deliverables  
- Test Plan document (this file)  
- Test Cases (manual)  
- Bug Reports (with screenshots)  
- Automation framework & scripts  
- API test collection & scripts  
- Performance test scripts & reports  
- Final Test Summary Report  

## 8. Entry & Exit Criteria  
**Entry Criteria**:  
- Demoblaze site accessible and stable  
- Test environment ready (browsers, tools installed)  
- Test data prepared (user accounts etc.)  

**Exit Criteria**:  
- All planned test cases executed (manual + automation)  
- Critical & major bugs fixed / logged  
- Performance tests complete  
- Test summary report ready  

## 9. Risks & Assumptions  
**Assumptions**:  
- Demoblaze site will remain stable (no major changes during testing)  
- No downtime during critical test phases  
- Tools (Selenium, JMeter, etc.) will work reliably  

**Risks**:  
- Site changes may break tests — may require rework  
- Network / connectivity issues during performance testing  
- Limited time availability  

## 10. References  
- Demoblaze website: https://demoblaze.com  
- This Test Plan document  
- Future Test Cases, APIs, etc.  

