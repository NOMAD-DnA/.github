"""Basic Markdown hygiene and repository-local file links; no network calls."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO_PREFIX = "https://github.com/NOMAD-DnA/.github/blob/main/"
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^\"']*[\"'])?\)")


def check_file(path, root):
    errors = []
    relative = path.relative_to(root)
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return [f"{relative}: not UTF-8"]
    if not text.endswith("\n"):
        errors.append(f"{relative}: missing final newline")
    if "\r" in text:
        errors.append(f"{relative}: use LF line endings")
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        location = f"{relative}:{number}"
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            chars, tail = marker.groups()
            if fence is None:
                fence = (chars[0], len(chars))
            elif chars[0] == fence[0] and len(chars) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence:
            continue
        if re.match(r"^(<{7}|={7}|>{7})(?: |$)", line):
            errors.append(f"{location}: merge conflict marker")
        if "\t" in line:
            errors.append(f"{location}: use spaces instead of tabs")
        if re.match(r"^#{1,6}[^#\s]", line):
            errors.append(f"{location}: heading needs a space")
        # Ignore inline code examples, including literal link syntax.
        prose = re.sub(r"(`+).*?\1", "", line)
        for match in LINK.finditer(prose):
            url = match.group(1).strip("<>")
            if url.startswith(REPO_PREFIX):
                target = root / unquote(urlsplit(url[len(REPO_PREFIX):]).path)
            else:
                parts = urlsplit(url)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                target = (root if parts.path.startswith("/") else path.parent) / unquote(parts.path.lstrip("/"))
            resolved = target.resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"{location}: link escapes repository: {url}")
            elif not resolved.exists():
                errors.append(f"{location}: missing local target: {url}")
    if fence:
        errors.append(f"{relative}: unclosed fenced code block")
    return errors


def main():
    paths = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    errors = [error for path in paths for error in check_file(path, ROOT)]
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(paths)} Markdown files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
