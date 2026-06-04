from pathlib import Path
import subprocess
import json
import time

ROOT = Path.cwd()

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode(errors="ignore")

def git_files():
    return run("git ls-files").splitlines()

def read_file(path, max_chars=4000):
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")[:max_chars]
    except:
        return ""

def build_snapshot():
    files = git_files()
    return {
        "repo_root": str(ROOT),
        "file_count": len(files),
        "timestamp": time.time(),
        "files": [
            {
                "path": f,
                "content_preview": read_file(f)
            }
            for f in files
        ]
    }

def build_context_pack(snapshot):
    files = sorted(snapshot["files"], key=lambda x: len(x["path"]))
    return {
        "summary": {
            "file_count": snapshot["file_count"],
            "timestamp": snapshot["timestamp"]
        },
        "top_files": files[:20]
    }

def write(path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def main():
    print("RW START")

    snapshot = build_snapshot()
    context = build_context_pack(snapshot)

    snap_path = ROOT / "docs" / "repo-snapshot.json"
    ctx_path = ROOT / "docs" / "context-pack.json"
    latest = ROOT / "docs" / "runtime-state.json"

    write(snap_path, snapshot)
    write(ctx_path, context)

    write(latest, {
        "snapshot": str(snap_path),
        "context": str(ctx_path),
        "status": "ok",
        "timestamp": snapshot["timestamp"]
    })

    print("RW COMPLETE")
    print("snapshot -> docs/repo-snapshot.json")
    print("context  -> docs/context-pack.json")
    print("latest   -> docs/runtime-state.json")

if __name__ == "__main__":
    main()
