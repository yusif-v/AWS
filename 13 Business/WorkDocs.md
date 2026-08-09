#AWS #Service #Business
### WorkDocs

Amazon WorkDocs is a secure content collaboration service for creating, sharing, and storing documents. It supports versioning, commenting, and access control, integrates with WorkSpaces, and offers audit logging for compliance.

### How It Works
- Documents are stored in managed S3-backed repositories with per-user workspaces.
- Sync clients (desktop and mobile) replicate folders to local drives for offline use.
- Admins define folder structures, sharing, and granular permissions.
- Version history and activity feeds track changes and collaboration.
- Audit logging records administrative and user actions for compliance.

### Key Features
- Document versioning with the ability to compare and restore older versions.
- Real-time commenting and feedback for review workflows.
- Fine-grained access control and admin-managed sharing policies.
- Desktop sync client and mobile apps for offline access.
- Integration with Active Directory for user authentication.

### Common Use Cases
- Internal document libraries and project collaboration.
- Contract and policy review with version history.
- Secure file storage for virtual desktop users.
- Compliance-minded repositories needing audit trails.

### Pricing & Limits
- Billed per active user with included storage; additional storage is billed per GB.
- Charged for documents under management and retained version history.
- Note: AWS announced it would discontinue WorkDocs in 2025; study it as a legacy service.

### Related Services

- [[WorkSpaces]]: Desktop integration.
- [[Chime]]: Collaboration alongside documents.
- [[S3]]: Underlying object storage.
- [[CloudTrail]]: Provides audit logging for user and admin activity.
- [[IAM]]: Controls permissions for the service.

### Related Concepts

- Document Collaboration: Shared workspaces.
- Version Control: Track document revisions.
- Access Controls: Fine-grained permissions.
- Active Directory: Source of user identity and policies.
- Offline Sync: Local access to documents when disconnected.
