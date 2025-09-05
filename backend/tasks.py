from invoke import task


@task
def dev(ctx):
    cmd = "uv run uvicorn --reload --host 0.0.0.0 --port 8000 main:app"
    ctx.run(cmd)


@task
def build(ctx):
    cmd = "pyinstaller -F --clean --noupx --collect-all funasr --collect-all transformers main.py"
    ctx.run(cmd)


@task
def run(ctx):
    cmd = "uv run main.py"
    ctx.run(cmd)


@task
def clean(ctx):
    import os
    import shutil

    for root, dirs, _ in os.walk(".", topdown=False):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"已删除: {pycache_path}")

    print("清理完毕")
