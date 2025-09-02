import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="google/medgemma-4b-it",
    local_dir="models/medgemma-4b-it",
    local_dir_use_symlinks=False,
    resume_download=True,
)
