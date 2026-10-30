<div align="center">

# skills

Agent skills by shbernal.

[![License][license-badge]][license]

---

[Skills](#skills) • [Install](#install) • [Credits](#credits)

---

</div>

A skill is a `SKILL.md` file that tells a coding agent how to do one task.
Each skill here stands alone, so install only the ones you want.

The skills are opinionated: they assume my setup (Arch Linux, [mise](https://mise.jdx.dev) for CLIs).
See [docs/preferences.md](docs/preferences.md).

## Skills

| Skill | What it does |
| --- | --- |
| [domain-model](skills/domain-model/SKILL.md) | Build a project's glossary of domain terms and its architecture decision records (ADRs) while you design |
| [freehire-search](skills/freehire-search/SKILL.md) | Search IT jobs on [freehire.me](https://freehire.me) with the `freehire` CLI, no account needed |
| [grill-me](skills/grill-me/SKILL.md) | Interview you relentlessly about a plan or idea, in rounds of numbered questions with recommended answers |
| [hacker-news](skills/hacker-news/SKILL.md) | Search and read [Hacker News](https://news.ycombinator.com) with the [hn](https://github.com/voska/hn-cli) CLI, and know which API answers what |
| [himalaya](skills/himalaya/SKILL.md) | Read, search, sort and send email with the [Himalaya](https://github.com/pimalaya/himalaya) CLI |
| [slopit](skills/slopit/SKILL.md) | Run a free blog on [SlopIt](https://slopit.io) through its REST API |
| [yutu](skills/yutu/SKILL.md) | Manage a YouTube channel and read YouTube data with the [yutu](https://github.com/eat-pray-ai/yutu) CLI |

## Install

Install one skill with the [skills](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add shbernal/skills --skill freehire-search
```

Install all of them:

```bash
npx skills add shbernal/skills
```

## Credits

Some skills build on others' work:

| Skill | Inspired by |
| --- | --- |
| [domain-model](skills/domain-model/SKILL.md) | Matt Pocock's [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling), © Matt Pocock, MIT |
| [grill-me](skills/grill-me/SKILL.md) | Matt Pocock's [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) and [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me), © Matt Pocock, MIT |
| [slopit](skills/slopit/SKILL.md) | Run a free blog on [SlopIt](https://slopit.io) through its REST API |
| [yutu](skills/yutu/SKILL.md) | eat-pray-ai's [youtube](https://github.com/eat-pray-ai/yutu/tree/main/skills/youtube) skill, © eat-pray-ai & OpenWaygate, Apache-2.0 |

[license]: LICENSE
[license-badge]: https://img.shields.io/github/license/shbernal/skills?style=for-the-badge&color=7aa2f7
