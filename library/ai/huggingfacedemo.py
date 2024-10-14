# ****************************************************************分割线****************************************************************
# todo hf_hub_download（下载模型）

from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="SakuraLLM/GalTransl-7B-v1.5",
    filename="GalTransl-7B-v1.5-Q6_K.gguf",
    local_dir="models",
    endpoint="https://hf-mirror.com"  # 国内镜像地址
)

# ************************************************************半分割线******************************
# todo snapshot_download（下载快照）

# from huggingface_hub import snapshot_download
#
# snapshot_download(
#     repo_id="SakuraLLM/GalTransl-7B-v1.5",
#     allow_patterns="GalTransl-7B-v1.5-Q6_K.gguf",
#     local_dir="models",
#     resume_download=True,
#     max_workers=8,
#     endpoint="https://hf-mirror.com",
# )
