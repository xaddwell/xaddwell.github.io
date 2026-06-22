#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "_data" / "profile.json"
README_PATH = ROOT.parent / "xaddwell" / "README.md"


def load_profile() -> dict:
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def format_link(link: dict) -> str:
    text = link["text"]
    url = link.get("url", "")
    return f"[{text}]({url})" if url else f"[{text}]()"


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_research(profile: dict) -> str:
    sections = ["## AI Risk Measurement and Mitigation"]
    icons = {
        "Risk Measurement": "### Risk Measurement",
        "Risk Mitigation": "### Risk Mitigation",
    }
    for area in profile["research_areas"]:
        sections.append(icons.get(area["title"], f"### {area['title']}"))
        sections.append("")
        for item in area["items"]:
            links = ", ".join(format_link(link) for link in item["links"])
            sections.append(f"- {item['label']}: {links}")
        sections.append("")
    return "\n".join(sections).rstrip()


def render_readme(profile: dict) -> str:
    replacements = {
        "__WECHAT_IMAGE__": profile["site"]["readme_wechat_image"],
        "__REPORT_PDF__": profile["site"]["readme_report_pdf"],
    }
    bio = [
        paragraph.replace("__WECHAT_IMAGE__", replacements["__WECHAT_IMAGE__"])
        for paragraph in profile["profile"]["bio"]
    ]
    news = [
        item.replace("__REPORT_PDF__", replacements["__REPORT_PDF__"])
        for item in profile["news"]
    ]
    parts = [f"# {profile['profile']['name']}", ""]
    parts.extend(bio)
    parts.extend(
        [
            "",
            render_research(profile),
            "",
            "# News",
            render_list(news),
            "",
            "# Publications",
            profile["publications_note"],
            render_list([item.strip() for item in profile["publications"]]),
            "",
            "# Honors and Awards",
            render_list(profile["honors"]),
            "",
            "# Educations",
            render_list(profile["education"]),
            "",
            "# Service",
            render_list(profile["service"]),
            "",
            "# Internships",
            render_list(profile["internships"]),
            "",
        ]
    )
    return "\n".join(parts)


def main() -> None:
    profile = load_profile()
    README_PATH.write_text(render_readme(profile), encoding="utf-8")


if __name__ == "__main__":
    main()
