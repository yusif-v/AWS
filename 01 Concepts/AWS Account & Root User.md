#AWS #Concept #Concept
### AWS Account & Root User

Every AWS account has a root user with full, unrestricted access. AWS recommends enabling MFA on the root user, never using it for daily tasks, and instead creating IAM users/roles for day-to-day administration. Root user credentials can be used to close the account or change support plans.

### Related Services

- [[IAM]]: The identities used instead of the root user.
- [[AWS Organizations]]: Manages multiple accounts centrally.
- [[CloudTrail]]: Records root user activity.

### Related Concepts

- [[IAM Roles]]: Temporary credentials for administration.
- MFA: Multi-factor authentication for root protection.
- Least Privilege: Limit root usage to emergencies.
