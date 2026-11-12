# Contributing

Issues and PRs are welcome, including fully AI-generated ones.

- Say which agent harness and model wrote the change, in the PR or issue body (the PR template has an `AI disclosure:` line). Commit messages carry no AI attribution; CI rejects it.
- One skill per directory: `skills/<name>/SKILL.md`, with `name` in the frontmatter matching the directory. CI checks the frontmatter: `uv run scripts/check-skills.py`.
- Run every command your skill shows before you submit it.
- Add the skill to the table in the README.
