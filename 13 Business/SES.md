#AWS #Service #Business
### SES

Amazon Simple Email Service (SES) is a cost-effective platform for sending and receiving email at scale. It handles marketing and transactional email, supports deliverability monitoring, reputation management, and integrates with SNS, Lambda, and other services.

### How It Works
- Applications send email through the SES SMTP endpoint or the SendEmail API.
- Domains are verified with DNS records; sending identities (domain or email) gate usage.
- Inbound email is routed by receipt rules to S3, SNS, Lambda, or WorkMail.
- Configuration sets attach metadata and publish sending events (delivery, bounce, complaint).
- Reputation is managed via suppression lists, bounces, and complaint feedback loops.

### Key Features
- High-throughput transactional and marketing email at low cost.
- Deliverability dashboard and reputation metrics for inbox placement.
- Email authentication with SPF, DKIM, and DMARC signing.
- Event publishing to CloudWatch, Kinesis, and SNS for analytics.
- Sandbox mode for new accounts; production access after a support request.

### Common Use Cases
- Transactional mail such as password resets, order confirmations, and receipts.
- Marketing and notification campaigns with open and click tracking.
- Receiving and processing inbound email into applications via Lambda.
- High-volume programmatic mail from applications and CI pipelines.

### Pricing & Limits
- Charged per 1,000 emails sent, plus data transfer; inbound processing is billed separately.
- Daily sending quota and maximum send rate apply and can be increased.
- Sandbox accounts can only send to verified addresses until production access is granted.
- Attachments add to message size; per-message size limits apply.

### Related Services

- [[SNS]]: Alternative push notification channel.
- [[Lambda]]: Processes inbound email.
- [[Route 53]]: Domain and DKIM DNS records.
- [[S3]]: Stores inbound email and attachments.
- [[CloudWatch]]: Collects sending and delivery metrics.
- [[Kinesis]]: Streams sending events for analytics.

### Related Concepts

- Deliverability: Inbox placement and reputation.
- Transactional Email: Password resets, receipts.
- DKIM/SPF: Email authentication.
- DMARC: Domain policy for authenticated email.
- Suppression List: Blocks repeated bounces and complaints.
- Configuration Set: Tracks sending events per email stream.
