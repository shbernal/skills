# AI project guidelines

`skills`: public collection of agent skills, one directory per skill under `skills/<name>/SKILL.md`, installable with `npx skills add shbernal/skills`.

- Conventions
  - A skill is self-contained: no references to other skills, private paths, or this machine.
  - Frontmatter `name` matches the directory name. `description` says when to use the skill.
  - Verify every command a skill shows by running it.
  - New skills get a row in the README table.

- Key documentation
  - [docs/preferences.md]: my setup, which skills target

- Iron Laws
  - Tokens are expensive, state of the art models need minimal guidance, don't repeat yourself, don't babysit, don't be over-specific.
  - AI-native project. All code is AI-generated.
  - Minimal attention when model implements without errors, we document in more detail when model struggles.
  - Do not expect the user to have read each line, don't lose him on the internals, give visibility on a higher-architectural level.
  - No journaling: code comments / documentation describe current state, they don't carry a log of their own edit history.
