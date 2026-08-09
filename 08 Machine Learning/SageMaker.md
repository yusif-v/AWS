#AWS #Service #ML
### SageMaker

Fully managed machine learning (ML) service for building, training, and deploying ML models. Supports data preparation, model training, hyperparameter tuning, and deployment for inference. Offers built-in algorithms, Jupyter notebooks, and integration with frameworks like TensorFlow and PyTorch. Ideal for data scientists and developers.

### How It Works
- Data is stored in S3 and prepared using built-in processing jobs, notebooks, Glue, or EMR.
- Training runs as managed jobs on EC2-backed compute, with automatic scaling and checkpointing.
- Built-in algorithms and framework containers (TensorFlow, PyTorch, XGBoost) avoid managing clusters.
- Hyperparameter tuning (Bayesian optimization) runs multiple trials automatically.
- Trained models are deployed to endpoints (real-time) or as batch transform (offline) jobs.
- SageMaker Pipelines and Model Registry formalize the ML lifecycle for CI/CD.

### Key Features
- SageMaker Studio, an integrated IDE for the full ML workflow.
- Autopilot (AutoML): automatically prepares data, trains, and tunes candidate models.
- Built-in algorithms plus Bring-Your-Own-Container (BYOC) for custom code.
- Feature Store, Model Registry, and Pipelines for production ML operations.
- Managed endpoints with auto scaling, plus serverless inference options.
- Clarify for bias detection and Model Monitor for drift detection.

### Common Use Cases
- Training and serving custom models for prediction, classification, and recommendation.
- Building NLP and computer vision models alongside managed AI services.
- MLOps: versioning, testing, and promoting models to production.
- Batch scoring of large datasets at low cost with transform jobs.
- Enabling citizen data scientists with Autopilot for automated modeling.

### Pricing & Limits
- Billed per instance-hour for notebooks, training jobs, endpoints, and processing.
- Storage (S3) and data transfer incur separate AWS charges.
- Pay only for compute time; models at rest in S3 cost standard storage.
- On-demand endpoints run continuously and incur cost even when idle; consider serverless inference for intermittent traffic.
- Free tier provides limited monthly notebook and training allowances.

### Related Services

- [[S3]]: Stores datasets, models, and training artifacts for SageMaker.
- [[Lambda]]: Triggers SageMaker endpoints for serverless inference.
- [[CloudWatch]]: Monitors SageMaker training jobs and endpoint performance.
- [[Glue]]: Prepares and transforms data for SageMaker.
- [[API Gateway]]: Exposes SageMaker models as APIs.
- [[EMR]]: Runs large-scale distributed data processing before training.
- [[Step Functions]]: Orchestrates multi-step ML pipelines and deployments.
- [[Bedrock]]: Alternative path using managed foundation models instead of custom training.
- [[IAM]]: Controls access to training resources and model endpoints.

### Related Concepts

- Machine Learning Lifecycle: Encompasses data prep, training, tuning, and deployment.
- Model Inference: Real-time or batch predictions using trained models.
- AutoML: SageMaker Autopilot automates model creation and tuning.
- Jupyter Notebooks: Interactive environment for data exploration and model development.
- Hyperparameter Tuning: Automatically searches the best model settings.
- Model Registry: Versioned catalog of approved models for deployment.
- Drift Monitoring: Detects when production data diverges from training data.
