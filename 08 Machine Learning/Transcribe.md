#AWS #Service #ML
### Transcribe

Fully managed automatic speech recognition (ASR) service that converts audio to text. Supports multiple languages, speaker identification, and custom vocabularies for domain-specific terms. Ideal for transcription of meetings, call center recordings, or media content, with real-time and batch processing options.

### How It Works
- Batch jobs read audio files from S3 and return transcripts with word-level timestamps.
- Real-time streaming transcribes audio as it arrives via HTTP/2 or WebSocket (Kinesis Video Streams).
- Custom vocabularies boost accuracy for names, acronyms, and industry jargon.
- Speaker diarization labels each utterance with the detected speaker.
- Automatic language identification detects and switches languages mid-recording.

### Key Features
- High-accuracy ASR across many languages with automatic punctuation and formatting.
- Custom vocabulary and custom language models for domain accuracy.
- Speaker diarization for separating callers and meeting participants.
- Medical-specific transcription with clinical terminology.
- Subtitles and caption generation in formats like SRT and VTT.
- Real-time streaming as well as batch processing.

### Common Use Cases
- Meeting and interview transcription for searchable notes.
- Call center analytics: transcribe recordings, then analyze with Comprehend.
- Generating captions and subtitles for video content.
- Indexing audio/video archives into Kendra for search.
- Voice search and media asset management.

### Pricing & Limits
- Billed per second of audio transcribed; real-time streaming is typically charged at a higher rate than batch.
- Medical transcription is billed as a separate offering per second.
- Audio files have duration limits per job; longer recordings are split into segments.
- Text stored in S3 incurs standard storage costs.

### Related Services

- [[S3]]: Stores audio inputs and transcription outputs.
- [[Lambda]]: Triggers processing or post-processing of transcriptions.
- [[Polly]]: Converts transcribed text back to speech.
- [[CloudWatch]]: Monitors transcription job performance and metrics.
- [[Comprehend]]: Analyzes transcribed text for sentiment or entities.
- [[Kinesis]]: Streams live audio into real-time transcription.
- [[Kendra]]: Indexes transcripts for enterprise search.
- [[SNS]]: Notifies completion of batch transcription jobs.
- [[Step Functions]]: Orchestrates audio-to-insight pipelines.

### Related Concepts

- Automatic Speech Recognition (ASR): Converts spoken language to text.
- Custom Vocabularies: Enhances accuracy for industry-specific terms or jargon.
- Speaker Diarization: Identifies and separates speakers in audio.
- Real-Time Transcription: Streams text output for live audio feeds.
- Word Timestamps: Time-aligned text for captions and search.
- Batch vs Streaming: Job-based offline processing versus continuous live input.
