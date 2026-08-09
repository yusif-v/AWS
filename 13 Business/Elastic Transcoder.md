#AWS #Service #Business
### Elastic Transcoder

Fully managed media transcoding service for converting video and audio files into multiple formats for playback on various devices (e.g., smartphones, TVs). Uses pipelines to process jobs, supports presets for common formats, and scales automatically. Charges based on output duration.

### How It Works
- Jobs read source media from S3, transcode it, and write the outputs back to S3.
- Pipelines define the input bucket, output bucket, and the IAM role used for processing.
- Presets bundle codec, resolution, and bitrate settings for target devices and streaming formats.
- Supports HLS and MPEG-DASH output for adaptive bitrate streaming.
- Can trigger downstream work through notifications and event-driven processing.

### Key Features
- Serverless, pay-per-minute transcoding with no infrastructure to manage.
- Library of built-in presets for common devices and formats, plus custom presets.
- Handles HD, SD, and 4K output as well as adaptive-bitrate (HLS/DASH) packages.
- Automatic scaling to handle spikes in video volume.
- Notifications via SNS on job completion or failure.

### Common Use Cases
- Converting video uploads into multiple formats and bitrates for web playback.
- Preparing adaptive streaming packages for distribution through CDNs.
- Repurposing media for mobile, tablet, TV, and broadcast targets.
- Transcoding audio-only content such as podcasts.

### Pricing & Limits
- Billed per minute of transcoded output, with rates varying by output resolution.
- No monthly minimums or upfront fees; S3 storage and data transfer are billed separately.
- Maximum input and output file size limits apply per job.

### Related Services

- [[S3]]: Stores input and output media files for transcoding.
- [[Lambda]]: Triggers transcoding jobs or processes output files.
- [[CloudWatch]]: Monitors transcoder performance and job status.
- [[SNS]]: Sends notifications for job completion or errors.
- [[IAM]]: Controls access to transcoder pipelines and resources.
- [[CloudFront]]: Delivers transcoded media to viewers at scale.

### Related Concepts

- Media Transcoding: Converts media files to different formats or resolutions.
- Pipelines: Define workflows for input, output, and transcoding settings.
- Presets: Preconfigured settings for common device formats.
- Scalability: Automatically handles large volumes of transcoding jobs.
- Adaptive Bitrate Streaming: Switches quality based on viewer bandwidth.
- HLS/DASH: Standard streaming protocols for media delivery.
