#AWS #Service #ML
### Translate

Amazon Translate is a neural machine translation service supporting dozens of languages. It provides real-time and batch translation APIs, custom terminology and formality settings, and integrates with S3, Lambda, and other services for multilingual content pipelines.

### How It Works
- Text is sent via a synchronous API for real-time translation or to batch jobs that read documents from S3.
- Neural machine translation models translate the full context of a sentence, not word-by-word.
- Custom terminology files ensure brand names and product terms are translated consistently.
- Custom translation models can be trained on parallel data (aligned source/target documents).
- Formality and profanity settings adapt output to the target audience.

### Key Features
- Real-time and asynchronous batch translation APIs.
- Custom terminology for domain-specific and branded phrasing.
- Custom models trained on parallel data for specialized domains.
- Automatic source language detection when not specified.
- Formality (formal/informal) and profanity masking controls.
- Translation of documents while preserving layout for select file types.

### Common Use Cases
- Localizing websites, product pages, and mobile apps into many languages.
- Translating customer support content and chat in real time.
- Multilingual content pipelines: translate text, then speak with Polly.
- Translating subtitles and documentation for global audiences.
- Standardizing global marketing and compliance communications.

### Pricing & Limits
- Billed per character of text translated.
- Custom terminology and custom models add a separate per-character training or usage charge.
- Batch jobs have document and text-size limits per request.
- Real-time API requests have a maximum text length per call; longer text uses batch processing.

### Related Services

- [[Comprehend]]: NLP analysis alongside translation.
- [[Polly]]: Speaks translated text.
- [[S3]]: Batch translation input/output.
- [[Lambda]]: Automates translation pipelines and post-processing.
- [[SQS]]: Queues batch translation job notifications.
- [[SNS]]: Alerts on completed translation jobs.
- [[CloudWatch]]: Monitors translation usage and job metrics.
- [[Step Functions]]: Orchestrates multilingual content workflows.
- [[Kinesis]]: Streams text for near-real-time translation.

### Related Concepts

- Neural MT: Deep-learning translation.
- Custom Terminology: Domain-specific phrasing.
- Batch vs Real-Time: API modes.
- Language Detection: Automatic identification of source language.
- Custom Models: Trained on parallel data for domain accuracy.
- Formality Control: Adapts politeness level of translated output.
