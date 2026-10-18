---
name: freehire-search
description: Use when searching for IT jobs on freehire.me with the `freehire` CLI, filtering by keyword, location, seniority, skills, salary or remote work, opening a posting, or listing a company's open roles.
---

# Searching jobs with freehire

`freehire` is a CLI over the [freehire.me](https://freehire.me) job catalogue. Search, facets, job and company work without an account. Every command takes `--json` for the raw API payload, so pipe it to `jq`.

If the command is missing, install it:

```bash
curl -fsSL https://freehire.me/install.sh | sh
```

## 1. Learn the filter values

Never guess a filter value. Read the live vocabulary first:

```bash
freehire facets
freehire facets --category backend
freehire --json facets | jq '.facets.seniority'
```

Each facet lists its values with a vacancy count. Filters narrow the counts to that slice. Skills are lowercase slugs (`go`, `react`, `kubernetes`).

## 2. Search

```bash
freehire search "golang" --region eu --remote --seniority senior --limit 10
freehire search "" --country IT --employment-type contract --exclude-skill python
freehire --json search "data engineer" --skills spark --limit 5 | jq '.[] | {title, company, public_slug}'
```

- Repeat a filter flag to OR its values.
- `--facet key=value` reaches any facet without its own flag. Add `_exclude` to the key to filter values out (`--facet company_type_exclude=outstaff`).
- `--region`, `--country` and `--city` form one OR group. `--region eu --country BR` means Europe or Brazil. To search one country, pass only `--country`.
- An empty query browses by filters alone.
- `--json` hits include the full description as markdown, so keep `--limit` small when you read them.

Watch stderr. The API ignores unknown filters without failing, and the CLI prints `warning: ignored unknown filter ...`, often with a `did you mean`. Fix the filter and rerun before you quote any count.

Skill tags come from the description text. Treat `--exclude-skill` as a rough filter, not proof of the stack.

## 3. Open results

```bash
freehire job <slug>
freehire company <company-slug>
```

`job` shows the full posting, the original URL where the person applies, and the company slug.

## Presenting results

Link each job as `https://freehire.me/jobs/<public_slug>`, one per line. Say which filters you used, so the person can adjust them.
