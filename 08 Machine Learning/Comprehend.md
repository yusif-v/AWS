#AWS #Service #ML
### Comprehend

Fully managed NLP service using ML to analyze text for entities, key phrases, sentiment, language, syntax, and topics. Supports custom models, medical text analysis, and real-time/batch processing for insights from documents. It is a serverless API, so no models need to be built or managed to extract meaning from unstructured text.

### How It Works
- Text is submitted via synchronous API calls or asynchronous batch jobs reading from S3.
- Pre-trained models detect language, entities (people, places, organizations), key phrases, and sentiment automatically.
- Syntax analysis produces part-of-speech and dependency parsing for linguistic features.
- Custom models can be trained on labeled data for domain-specific classification or entity recognition.
- Results are returned as structured JSON for downstream processing by Lambda, Glue, or databases.

### Key Features
- Entity recognition and linking, including names, dates, quantities, and locations.
- Sentiment detection (positive, negative, neutral, mixed) and targeted sentiment per entity.
- Language detection across a broad set of languages.
- Custom classifiers and custom entity recognizers built with SageMaker-backed training.
- PII detection and redaction for privacy compliance.
- Comprehend Medical for extracting entities from clinical and medical text.

### Common Use Cases
- Analyzing customer feedback and support tickets for sentiment trends.
- Extracting structured data (entities, key phrases) from documents processed by Textract.
- Monitoring social media and call-center transcripts (via Transcribe) for brand insight.
- Redacting PII from text before storage or analysis.
- Classifying documents for routing, archival, or compliance.

### Pricing & Limits
- Real-time APIs billed per unit of text (typically per 100 characters).
- Batch and custom model jobs billed by volume of text processed plus training usage.
- Comprehend Medical priced as a separate offering per unit of text.
- Per-request document size limits apply; very large corpora should use batch processing.

### Related Services

- [[S3]]: Stores text data for Comprehend analysis.
- [[Lambda]]: Processes Comprehend outputs in workflows.
- [[SageMaker]]: Builds custom ML models for Comprehend.
- [[Transcribe]]: Converts speech to text for Comprehend input.
- [[CloudWatch]]: Monitors Comprehend metrics and jobs.
- [[Textract]]: Extracts text from scanned documents for Comprehend analysis.
- [[Glue]]: Prepares and catalogs text data at scale.
- [[Athena]]: Queries extracted insights stored in S3.

### Related Concepts

- Natural Language Processing (NLP): Extracts meaning from unstructured text.
- Sentiment Analysis: Detects positive/negative emotions in text.
- Entity Recognition: Identifies names, places, organizations in text.
- Custom Classifiers: Trains models for domain-specific text analysis.
- PII Detection: Identifies and redacts personal data for compliance.
- Topic Modeling: Groups documents by recurring themes.
