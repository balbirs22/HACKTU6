# src/config.py

# Pre-trained BERT model to use from Hugging Face
MODEL_NAME = "bert-base-cased"

# Training hyperparameters
TRAINING_ARGS = {
    "output_dir": "./results",                # Directory for checkpoints and logs
    "evaluation_strategy": "epoch",             # Evaluate at the end of each epoch
    "learning_rate": 2e-5,                      # Learning rate
    "per_device_train_batch_size": 16,          # Training batch size per device
    "per_device_eval_batch_size": 16,           # Evaluation batch size per device
    "num_train_epochs": 3,                      # Number of epochs
    "weight_decay": 0.01,                       # Weight decay for regularization
}

# Directory to store the fine-tuned model and tokenizer
FINE_TUNED_MODEL_DIR = "./fine_tuned_resume_parser"
