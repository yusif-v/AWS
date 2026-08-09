#AWS #Service #ML
### Kendra

Fully managed, ML-powered enterprise search service for accurate, natural language queries across data sources like S3, databases, and file systems. Indexes unstructured data, provides contextual answers, and supports custom connectors for enhanced search experiences. Unlike keyword search, Kendra understands synonyms and meaning to rank results by relevance.

### How It Works
- An index is created and connected to data sources such as S3, RDS, SharePoint, and ServiceNow via built-in or custom connectors.
- A synchronizer crawls the sources and builds an ML-powered searchable index, preserving document metadata and structure.
- Queries use natural language and are matched semantically, not just by keyword.
- Results are returned with excerpts and relevance scores, optionally grouped into answer passages and FAQs.
- Custom synonyms and relevant documents can be used to tune relevance over time.

### Key Features
- Natural-language question answering with highlighted answer passages.
- Semantic search that understands context, synonyms, and abbreviations.
- Built-in data source connectors plus a developer toolkit for custom connectors.
- Document FAQ extraction and auto-generated FAQs from source content.
- Custom synonyms and relevant documents for relevance tuning.
- Access controls and user context to personalize results per identity.

### Common Use Cases
- Employee self-service portals retrieving answers from HR and IT documents.
- Customer support search over manuals, knowledge bases, and FAQs.
- Legal and compliance search across contracts and filings.
- Search over transcribed audio (Transcribe) and scanned documents (Textract).
- Internal developer documentation and code search.

### Pricing & Limits
- Billed per hour for each provisioned index instance and per query performed.
- Indexed document storage is metered, and each index has a document capacity limit.
- Custom connectors may require Lambda and S3 resources billed separately.
- Enterprise Edition adds features such as relevance tuning at a higher per-hour rate.

### Related Services

- [[S3]]: Stores data indexed by Kendra.
- [[RDS]]: Provides relational data sources for Kendra indexing.
- [[Lambda]]: Customizes Kendra search workflows and responses.
- [[QuickSight]]: Visualizes Kendra search insights.
- [[IAM]]: Manages access to Kendra indexes and queries.
- [[Textract]]: Extracts text from scanned PDFs so Kendra can index them.
- [[Transcribe]]: Produces searchable text from audio and video for indexing.
- [[CloudWatch]]: Monitors index synchronization and query metrics.

### Related Concepts

- Enterprise Search: Unifies search across disparate data silos.
- Natural Language Processing (NLP): Enables query understanding for relevant results.
- Machine Learning (ML): Powers semantic search and ranking.
- Data Indexing: Crawls and structures data for efficient retrieval.
- Semantic Search: Matches on meaning rather than literal keywords.
- Document FAQs: Auto-generated Q&A pairs surfaced as direct answers.
