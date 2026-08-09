#AWS #Service #Storage
### S3 Access Control

Amazon S3 provides multiple, layered mechanisms for controlling access to buckets and objects: IAM policies, bucket policies, bucket ACLs, object ACLs, and S3 Object Ownership. Together they enable granular, least-privilege access for users, roles, and cross-account sharing, while S3 Block Public Access acts as a safety net against accidental public exposure.

### How It Works

- IAM policies grant permissions to IAM users, groups, and roles for specific S3 actions (e.g., `s3:GetObject`).
- Bucket policies are JSON resource-based policies attached to a bucket that grant access to principals inside or outside the account.
- ACLs are the legacy, simpler permission model applied per bucket or object; they are disabled by default when Object Ownership is set to Bucket owner enforced.
- Object Ownership determines who owns objects uploaded by other accounts (Bucket owner enforced, Bucket owner preferred, or Object writer).
- Access decisions combine identity-based and resource-based policies; an explicit Deny always overrides an Allow.
- S3 Block Public Access settings override all other permissions to prevent public access at the account or bucket level.

### Key Features

- Bucket policies support conditions on IP ranges, VPC endpoints, MFA, required encryption, and principal ARNs.
- IAM integration provides a centralized, cross-service permission model.
- Pre-signed URLs grant temporary, time-limited access to specific objects without changing policies.
- S3 Access Points provide named network endpoints with their own policies and optional VPC restrictions.
- MFA Delete and MFA-protected API calls add extra protection for destructive operations.
- S3 Block Public Access blocks public ACLs and public bucket policies by default.

### Common Use Cases

- Granting an IAM role read-only access to a data lake bucket.
- Allowing another AWS account to write objects via a bucket policy.
- Serving a static website publicly while keeping the rest of the bucket private.
- Giving external users temporary access to specific objects via pre-signed URLs.
- Enforcing server-side encryption on all uploads using bucket policy conditions.

### Pricing & Limits

- No additional charge for the access control features themselves; costs come from data requests and storage.
- Bucket policies have a size limit (around 20 KB), so very large policies may need multiple buckets or IAM-based controls.
- ACLs are discouraged in favor of bucket policies and IAM; new best practice is Bucket owner enforced ownership.

### Related Services

- [[S3]]: The bucket and object storage service these controls protect.
- [[IAM]]: Issues identity-based policies for users, groups, and roles.
- [[IAM Policies]]: JSON policy documents that define allowed actions.
- [[VPC Endpoints]]: Gateway endpoints enable private, policy-restricted access to S3.

### Related Concepts

- Resource-Based Policies: Policies attached to the bucket rather than to an identity.
- Least Privilege: Granting only the minimal actions and resources needed.
- Public Access: Unauthenticated access to objects; blocked by default.
- Pre-Signed URLs: Temporary URLs that grant limited-time object access.
- S3 Object Ownership: Determines who owns objects uploaded by another account.
