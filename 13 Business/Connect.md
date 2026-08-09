#AWS #Service #Business
### Connect

Fully managed, cloud-based contact center service for omnichannel customer interactions via voice, chat, messaging, email, video, and screen sharing. Uses AI (Amazon Q in Connect) for self-service, agent assistance, and real-time analytics. Scales automatically, supports global telephony in 158 countries, and offers pay-as-you-go pricing. Ideal for customer service, support, and outbound campaigns.

### How It Works
- Contact flows (visual, drag-and-drop) define IVR menus, routing rules, and agent assignment.
- Connects to phone networks via country-specific telephony and routes calls to available agents.
- Amazon Q in Connect (formerly Wisdom) surfaces real-time articles, answers, and next-best actions to agents.
- Contact Lens provides call analytics, transcription, and sentiment scoring on recorded interactions.
- Integrates with AWS services to store records, run custom logic, and monitor live traffic.

### Key Features
- Omnichannel support across voice, chat, messaging, and email in one agent workspace.
- AI-driven self-service through natural-language IVR and chatbots built with Amazon Lex.
- Per-minute metered billing with no upfront costs or minimum commitments.
- Contact Lens speech analytics with transcription and sentiment detection.
- Integration with CRM systems and agent desktops.

### Common Use Cases
- Customer service and support centers replacing legacy on-premises ACD/PBX systems.
- Outbound campaigns such as appointment reminders and follow-ups.
- AI self-service bots that resolve simple requests before human handoff.
- Seasonal scale spikes that need elastic capacity.

### Pricing & Limits
- Billed per minute of voice usage, per chat message, and for outbound telephony.
- Additional charges apply for features such as Contact Lens analytics and Amazon Q in Connect.
- No upfront fees; supporting services (Lambda, S3, etc.) are billed separately.
- Telephone numbers are provisioned per region and country; some countries require additional registration.

### Related Services

- [[Lambda]]: Powers custom logic in contact flows.
- [[Lex]]: Builds conversational AI for IVR and chatbots.
- [[S3]]: Stores contact data and analytics.
- [[CloudWatch]]: Monitors performance and metrics.
- [[Kinesis]]: Streams real-time data for analysis.
- [[SNS]]: Sends notifications for events and alerts.
- [[Bedrock]]: Underlies generative-AI assistance in Amazon Q in Connect.
- [[IAM]]: Controls permissions for the Connect environment.

### Related Concepts

- Omnichannel Contact Center: Seamless customer experience across multiple channels.
- Conversational AI: Enables natural, AI-driven interactions.
- Scalability: Automatically handles varying interaction volumes.
- Pay-as-You-Go: Charges based on usage, no upfront costs.
- Contact Flow: The visual workflow that routes customer interactions.
- ACD: Automatic call distribution for routing calls to available agents.
