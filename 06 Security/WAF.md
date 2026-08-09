#AWS #Service #Security
### WAF

AWS WAF is a managed web application firewall that filters and monitors HTTP(S) traffic. It protects CloudFront, ALB, and API Gateway from common attacks like SQL injection and cross-site scripting using rules, rule groups, and rate-based rules.

### How It Works

- Associates web ACLs with CloudFront, ALB, API Gateway, or AppSync.
- Each web ACL contains rules and rule groups that inspect requests.
- Rules match on IP, headers, body, URI, and geo data.
- Rate-based rules track IP addresses and block those exceeding thresholds.
- Actions on a match are allow, block, count, or challenge.

### Key Features

- Managed rule sets from AWS, including OWASP Top 10 protection.
- Custom rules for application-specific patterns.
- Rate-based rules and bot control.
- Real-time metrics and logging to CloudWatch, S3, and Kinesis.
- Integration with AWS Firewall Manager and Security Hub.

### Common Use Cases

- Blocking SQL injection and XSS at the edge.
- Rate-limiting login endpoints against brute force.
- Protecting APIs behind API Gateway with token-based auth rules.
- Geo-blocking traffic from unwanted regions.
- Bot mitigation for scraping and credential stuffing.

### Pricing & Limits

- Billed per web ACL and per rule, plus per request inspected.
- Managed rule groups incur additional charges per request.
- Costs vary by traffic volume and rule complexity.

### Related Services

- [[CloudFront]]: Common integration point for WAF.
- [[Shield]]: DDoS protection layered with WAF.
- [[API Gateway]]: Protected via web ACLs.
- [[ELB]]: Application Load Balancers that can be associated with web ACLs.
- [[CloudWatch]]: Monitors WAF metrics and alerts.
- [[Security Hub]]: Aggregates WAF-related security posture findings.
- [[ACM]]: Provides the TLS certificates for protected endpoints.

### Related Concepts

- Web ACL: Set of rules applied to traffic.
- Rate-Based Rule: Blocks IPs exceeding a threshold.
- OWASP: Common managed rule sets.
- Bot Control: Managed protections against automated traffic.
- Managed Rule Groups: AWS-curated rules covering known attack vectors.
