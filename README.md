<div align="center">

# skills

Agent skills by shbernal.

[![License][license-badge]][license]

---

[Skills](#skills) • [Install](#install)

---

</div>

A skill is a `SKILL.md` file that tells a coding agent how to do one task.
Each skill here stands alone, so install only the ones you want.

## Skills

| Skill | What it does |
| --- | --- |
| [freehire-search](skills/freehire-search/SKILL.md) | Search IT jobs on [freehire.me](https://freehire.me) with the `freehire` CLI, no account needed |

## Install

Install one skill with the [skills](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add shbernal/skills --skill freehire-search
```

Install all of them:

```bash
npx skills add shbernal/skills
```

[license]: LICENSE
[license-badge]: https://img.shields.io/github/license/shbernal/skills?style=for-the-badge&color=7aa2f7
