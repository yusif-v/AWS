#AWS #Service #ML
### Textract

Amazon Textract extracts text, tables, and forms from scanned documents using machine learning. It goes beyond OCR by preserving structure and relationships, enabling document processing for invoices, IDs, and forms, and integrates with Step Functions and Lambda.

### How It Works
- Documents (PDF, TIFF, PNG, JPG) are submitted synchronously (small) or asynchronously via S3 (large or batch).
- ML models detect text, tables, forms, and key-value pairs while preserving reading order and layout.
- Queries (Ask a Document) let you request specific fields such as invoice totals or dates.
- Output is returned as structured JSON with bounding boxes and confidence scores.
- Results feed downstream services such as Comprehend, Kendra, or databases.

### Key Features
- OCR for printed text plus handwriting support.
- Table extraction that preserves row and column structure.
- Form and key-value pair extraction for documents like tax forms and W-2s.
- Queries API for extracting specific information with natural-language questions.
- Identity document (ID) analysis for driver's licenses and passports.
- Document analysis of expense reports, insurance claims, and contracts.

### Common Use Cases
- Automating invoice and receipt processing in accounts payable.
- Onboarding customers by scanning identity documents.
- Converting scanned contracts into searchable, structured data for Kendra.
- Insurance claims and mortgage application document processing.
- Building serverless pipelines: S3 upload triggers Lambda to run Textract, then Comprehend.

### Pricing & Limits
- Billed per page or per document analyzed, with different rates per feature (text, tables/forms, queries).
- Asynchronous batch processing can handle large page volumes; synchronous calls have size limits.
- Documents stored in S3 incur standard storage and (when triggered) S3 event notification charges.
- Free tier provides a limited number of pages per month.

### Related Services

- [[Rekognition]]: Image analysis (distinct from documents).
- [[Lambda]]: Automates document workflows.
- [[Comprehend]]: Extracts meaning from extracted text.
- [[S3]]: Stores source documents and Textract output.
- [[SQS]]: Queues asynchronous Textract completion notifications.
- [[SNS]]: Alerts on completed document analysis jobs.
- [[Step Functions]]: Coordinates multi-step document processing workflows.
- [[Kendra]]: Indexes extracted text for enterprise search.

### Related Concepts

- OCR: Optical character recognition.
- Document Structure: Tables and forms preserved.
- Automated Processing: Pipeline from scan to data.
- Key-Value Pairs: Form fields extracted with their labels.
- Queries API: Natural-language requests for specific document fields.
- Confidence Scores: ML certainty used to decide human review vs auto-processing.
