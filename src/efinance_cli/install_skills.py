#!/usr/bin/env python3
"""Install efinance-cli skills to ~/.claude/skills/

Usage:
    # Using uvx (recommended)
    uvx --from github:PegasusWang/efinance-cli install-skills

    # Using pipx
    pipx run --from github:PegasusWang/efinance-cli install-skills

    # Direct download and run
    curl -sSL https://raw.githubusercontent.com/PegasusWang/efinance-cli/master/src/efinance_cli/install_skills.py | python3
"""

import shutil
import tempfile
import subprocess
from pathlib import Path


def main():
    """Install skills to Claude Code skills directory."""
    target_dir = Path.home() / ".claude" / "skills"
    target_dir.mkdir(parents=True, exist_ok=True)

    print("Downloading skills from GitHub...")

    with tempfile.TemporaryDirectory() as tmpdir:
        # Clone the repo
        subprocess.run([
            "git", "clone", "--depth", "1",
            "https://github.com/PegasusWang/efinance-cli.git",
            tmpdir
        ], check=True, capture_output=True)

        skills_source = Path(tmpdir) / "skills"

        # Copy skills
        for skill_dir in skills_source.iterdir():
            if skill_dir.is_dir():
                dest = target_dir / skill_dir.name
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(skill_dir, dest)
                print(f"Installed: {skill_dir.name}")

    print(f"\n✅ Skills installed to {target_dir}")
    print("Available skills:")
    print("  - filter-fund-by-name")
    print("  - query-fund-purchase-limit")


if __name__ == "__main__":
    main()