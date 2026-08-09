#AWS #Concept #Concept
### AWS Account & Root User

Every AWS account has a root user with full, unrestricted access. AWS recommends enabling MFA on the root user, never using it for daily tasks, and instead creating IAM users/roles for day-to-day administration. Root user credentials can be used to close the account or change support plans.

### How It Works
- The root user is created from the account's email address and password at signup and cannot be deleted.
- Root has unrestricted access to every service and cannot be constrained by IAM policies.
- A small set of account-level actions require root credentials, including closing the account and changing support plans.
- Using root credentials generates an event in [[CloudTrail]], enabling monitoring of unexpected usage.

### Key Features
- Full access to all AWS services, billing, and account settings.
- Account-level capabilities: account closure, support plan changes, and IAM password policy management.
- Cannot be replaced; the account is permanently bound to the root identity.
- Eligible for MFA and password policies to reduce compromise risk.

### Common Use Cases
- Creating the account and setting up the first [[IAM]] users.
- Performing rare account-level operations that only root can execute.
- Managing billing, payment methods, and support plans.
- Recovering access when other credentials are lost.

### Security Best Practices
- Enable MFA on the root user immediately after signup.
- Create [[IAM]] users or [[IAM Roles]] with least privilege and use them for daily work.
- Never share root credentials or embed them in code or automation.
- Monitor root activity with [[CloudTrail]] and alert on unexpected usage.

### Pricing & Limits
- The root user and account creation are free; costs accrue per service usage.
- Billing is per account; [[AWS Organizations]] enables consolidated billing and centralized management across accounts.
- One root user per account, and each email address can own a limited number of accounts.

### Related Services

- [[IAM]]: The identities used instead of the root user.
- [[AWS Organizations]]: Manages multiple accounts centrally.
- [[CloudTrail]]: Records root user activity.
- [[IAM Roles]]: Temporary credentials for administration.

### Related Concepts

- MFA: Multi-factor authentication for root protection.
- Least Privilege: Limit root usage to emergencies.
- [[Shared Responsibility Model]]: Root compromise is the most severe access-control risk an account faces.
