#AWS #Service #ML
### Rekognition

Fully managed computer vision service for analyzing images and videos. Uses machine learning to detect objects, faces, text, and scenes, and supports facial recognition, content moderation, and custom labels. Ideal for media analysis, security, and user engagement applications.

### How It Works
- Images are analyzed via a synchronous API; videos are processed asynchronously with jobs that read from S3.
- Pre-trained models detect labels (objects, scenes, concepts), faces, text, and celebrities.
- Face APIs extract facial features, compare faces, and search a face collection for matches.
- Content moderation scores images and video frames for adult or violent content.
- Custom Labels trains a private model on labeled image data for domain-specific detection.

### Key Features
- Object, scene, and activity detection across thousands of labels.
- Face detection, analysis (age range, emotions, glasses), comparison, and search in collections.
- Celebrity recognition and text-in-image (OCR) detection.
- Content moderation with confidence scores for inappropriate content.
- Video analysis for activities, people, and objects across frames.
- Custom Labels for bespoke detectors trained on your own images.

### Common Use Cases
- Media asset management: tagging photos and video libraries by content.
- Moderating user-generated content on social platforms before publishing.
- Security and surveillance: finding people of interest from camera feeds.
- Analyzing video for sports events, retail footfall, or industrial safety.
- Building image search and recommendation features in applications.

### Pricing & Limits
- Billed per image analyzed (label detection, face detection, moderation) and per minute of video.
- Face storage in collections and searches are metered separately.
- Custom Labels billing includes training time and inference usage.
- Free tier provides limited monthly image and face analysis allowances.

### Related Services

- [[S3]]: Stores images and videos for Rekognition analysis.
- [[Lambda]]: Triggers Rekognition for automated image/video processing.
- [[CloudWatch]]: Monitors Rekognition API usage and metrics.
- [[API Gateway]]: Exposes Rekognition capabilities via APIs.
- [[SNS]]: Sends notifications based on Rekognition results.
- [[Kinesis]]: Feeds live video streams into Rekognition video analysis.
- [[Textract]]: Handles structured document text; Rekognition handles image/video text in the wild.
- [[Step Functions]]: Orchestrates multi-stage media processing pipelines.

### Related Concepts

- Computer Vision: ML-based analysis of visual content for insights.
- Facial Recognition: Identifies or verifies faces with high accuracy.
- Content Moderation: Detects inappropriate content in images/videos.
- Custom Labels: Trains models for domain-specific object detection.
- Face Collections: Stored face vectors used to search and match faces.
- Object & Scene Detection: Labels everyday objects and environments in media.
