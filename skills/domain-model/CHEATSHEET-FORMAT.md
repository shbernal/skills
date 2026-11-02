# GLOSSARY-CHEATSHEET.md format

Personal companion to `GLOSSARY.md`: the terms the user has struggled with, explained in plain language. Create it on the first explanation, and keep it out of git:

```sh
echo GLOSSARY-CHEATSHEET.md >> "$(git rev-parse --git-common-dir)/info/exclude"
```

The exclude is shared by all worktrees, but the file itself is not: a linked worktree starts without it. Don't copy it there, link it, so every worktree reads and writes the one copy in the main worktree:

```sh
ln -s "$(git rev-parse --path-format=absolute --git-common-dir)/../GLOSSARY-CHEATSHEET.md" GLOSSARY-CHEATSHEET.md
```

Do this when the file is missing and `git rev-parse --git-dir` differs from `git rev-parse --git-common-dir`.

```md
# {Project name} cheatsheet

**Order** (glossary):
What a customer sends when they want to buy something. One Order can hold several products,
and it exists before any money moves: paying is a later step. Example: ...

**Idempotency** (general):
Doing the same thing twice has the same effect as doing it once. Here it matters because ...
```

## Rules

- **One entry per term**, marked `(glossary)` when it expands a glossary term and `(general)` when it is an industry concept the glossary doesn't cover.
- **Plain words, longer than the glossary.** Explain with an example from this project. Say why the term matters here.
- **Only what the user struggled with.** Not a copy of the glossary, not a textbook.
- **Rewrite, don't append**, when the user stumbles on the same term again: the old explanation didn't land.
- **Glossary stays the source of truth.** Never define a project term only here; add it to `GLOSSARY.md` first.
