#AWS #Service #Business
### WorkSpaces

Amazon WorkSpaces is a fully managed virtual desktop infrastructure (VDI) service. It provisions Windows or Linux desktops in the cloud, lets users access them from any device, and provides persistent, pay-as-you-go desktops without managing the underlying infrastructure.

### How It Works
- Desktops run on EC2-backed instances with preconfigured bundles (CPU, memory, storage).
- Users connect through lightweight client apps on laptops, tablets, or thin clients.
- Streaming protocols (PCoIP/WSP) transmit the desktop over the network.
- Integrates with Microsoft Active Directory for authentication, group policy, and user profiles.
- Supports persistent desktops (state saved) and non-persistent pools.

### Key Features
- Fully managed Windows or Linux desktops with no VDI infrastructure to run.
- Accessible from any device via native clients or web browser.
- Pay-as-you-go (hourly) and monthly billing with savings for full-time users.
- Bring Your Own License (BYOL) options for Windows and other software.
- Fast provisioning of many desktops from images or shared templates.

### Common Use Cases
- Remote and hybrid work for employees on personal devices (BYOD).
- Secure contractor or vendor access without shipping hardware.
- Testing and development environments that need disposable desktops.
- Delivering Windows applications to macOS, Linux, and Chromebook users.

### Pricing & Limits
- Billed per user per month or per hour based on bundle size.
- Additional charges for storage, bandwidth, and dedicated infrastructure.
- Requires an Active Directory for user management unless using Simple AD.

### Related Services

- [[WorkDocs]]: Secure storage for desktop users.
- [[Chime]]: Voice/video for remote workers.
- [[IAM]]: User identity for desktops.
- [[EC2]]: Underlying compute for WorkSpaces instances.

### Related Concepts

- VDI: Virtual desktop infrastructure.
- BYOD: Access from personal devices.
- Persistent Desktops: User-specific state retained.
- Streaming Protocol: PCoIP/WSP transmission of the desktop session.
- Image Template: Golden image used to provision desktop fleets.
