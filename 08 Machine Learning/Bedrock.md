#AWS #Service #ML
### Bedrock

Amazon Bedrock is a fully managed service for building generative AI applications using foundation models from Anthropic, AI21, Cohere, Meta, and Amazon. It provides model access via API, supports fine-tuning and agents, and integrates with the rest of AWS for secure, scalable GenAI. Developers experiment with many models through a single API and deploy with enterprise-grade security, governance, and observability.

### How It Works
- Foundation models (FMs) are hosted and managed by AWS and accessed through a unified API, so you do not provision or operate any GPU infrastructure.
- Requests are routed to the chosen model; input and output tokens are billed per use on a pay-as-you-go basis.
- Prompts and responses are encrypted in transit and at rest, with optional integration with KMS for customer-managed keys.
- Agents break complex tasks into multi-step plans and invoke Lambda functions, APIs, and knowledge bases.
- Knowledge Bases connects Bedrock to vector stores (e.g., OpenSearch, Amazon Aurora) for retrieval-augmented generation (RAG).

### Key Features
- Access to leading FMs from Anthropic, AI21, Cohere, Meta, Amazon, and Mistral AI through one consistent API.
- Fine-tuning and continued pre-training of select models on your own data without managing infrastructure.
- Guardrails for content filtering, PII redaction, and topic-based safety controls on model output.
- Agents that plan, call tools, and orchestrate multi-step workflows against your systems.
- Provisioned throughput for predictable, dedicated capacity on production workloads.
- Integration with IAM, CloudWatch, CloudTrail, and VPC for security and observability.

### Common Use Cases
- Building chatbots and virtual assistants grounded in enterprise documents via RAG.
- Content generation: summaries, drafts, code, and marketing copy.
- Multilingual translation and content localization pipelines.
- Document analysis working alongside Textract and Comprehend to extract and summarize insights.
- Automating customer support and routing to humans through Connect when confidence is low.

### Pricing & Limits
- Billed per token for text generation and per image for vision models; fine-tuning adds training and storage charges.
- Provisioned throughput is billed hourly for dedicated capacity with predictable pricing.
- Guardrails, agents, and knowledge base usage are metered separately.
- On-demand inference has concurrency limits that can be raised via a support request.

### Related Services

- [[SageMaker]]: For building and training custom models.
- [[Lambda]]: Runs application logic calling Bedrock.
- [[KMS]]: Encrypts prompts and responses.
- [[OpenSearch]]: Vector store option for Bedrock knowledge bases (RAG).
- [[API Gateway]]: Exposes Bedrock-backed generative AI behind a REST API.
- [[EventBridge]]: Triggers workflows on model invocation and evaluation events.
- [[GuardDuty]]: Monitors for compromised credentials used against Bedrock.

### Related Concepts

- Foundation Model: Pre-trained LLM served via API.
- GenAI: Generative applications.
- Guardrails: Content filtering for model output.
- Retrieval-Augmented Generation (RAG): Grounds model answers in private documents to reduce hallucination.
- Fine-tuning: Adapting a pre-trained model on domain data for higher accuracy.
- Agents: Multi-step task decomposition with tool invocation.
