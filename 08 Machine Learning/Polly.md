#AWS #Service #ML
### Polly

Text-to-speech service that converts text into lifelike speech using advanced deep learning. Supports multiple languages, voices, and speech styles (e.g., conversational, newscaster). Generates audio in formats like MP3 for applications like voice assistants, audiobooks, or accessibility tools.

### How It Works
- Text (or SSML) is submitted via a synchronous or asynchronous (S3 bucket) API call.
- Neural text-to-speech engines generate natural prosody, intonation, and pauses from the input.
- Voices are selected by language and style (neural, standard, or child voices, and styles such as conversational or newscaster).
- Output audio can be streamed directly or saved to S3 in MP3, OGG, or PCM formats.
- Lexicons customize pronunciation of words such as product names and acronyms.

### Key Features
- Broad selection of neural voices across many languages and locales.
- SSML support for control of pauses, emphasis, rate, pitch, and pronunciation.
- Custom pronunciation lexicons (plain text or SSML-based).
- Speech Marks that time-align audio with word/sentence boundaries for captions.
- Streaming output for real-time voice responses.
- Scalable, low-latency synthesis suitable for voice assistants.

### Common Use Cases
- Voice responses for Lex chatbots and voice-enabled applications.
- Audiobook and e-learning narration generated from written content.
- Accessibility: reading web pages, dashboards, or documents aloud.
- Call-center IVR prompts and notifications.
- Localized content pipelines: Translate text, then speak it with Polly.

### Pricing & Limits
- Billed per character of text converted to speech.
- Neural voices are priced higher per character than standard voices.
- Synthesized speech stored in S3 incurs standard S3 storage costs.
- Asynchronous synthesis to S3 supports larger volumes than real-time requests.

### Related Services

- [[Lex]]: Integrates with Polly for conversational bot voice responses.
- [[S3]]: Stores Polly-generated audio files.
- [[Lambda]]: Triggers Polly for serverless speech generation.
- [[CloudWatch]]: Monitors Polly usage and performance metrics.
- [[API Gateway]]: Exposes Polly functionality via APIs.
- [[Translate]]: Translates text into another language before synthesis.
- [[SNS]]: Notifies completion of asynchronous synthesis jobs.
- [[Step Functions]]: Orchestrates document-to-audio pipelines.

### Related Concepts

- Text-to-Speech (TTS): Converts text into natural-sounding audio.
- Neural TTS: Advanced ML models for realistic voice output.
- SSML (Speech Synthesis Markup Language): Customizes speech with pauses, emphasis, or pronunciation.
- Voice Customization: Adjusts pitch, speed, or style for specific use cases.
- Speech Marks: Timestamps mapping audio to words for captions and lip-sync.
- Pronunciation Lexicons: Custom word-to-phoneme mappings for accurate speech.
