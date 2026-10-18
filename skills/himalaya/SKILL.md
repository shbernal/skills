---
name: himalaya
description: Use when reading, searching, sorting or sending email from the terminal with the Himalaya CLI, including replies, forwards, attachments, flags and moving messages between mailboxes.
---

# Himalaya email CLI

Written for Himalaya 2.2. On another version, check `himalaya <command> --help` first; 2.x dropped `template` and the 1.x config keys.

If the command is missing, install it:

```bash
mise use -g github:pimalaya/himalaya
```

## Rules

- Confirm with the user before sending, replying, forwarding, moving, deleting or changing flags. Show the recipients, subject, body and attachments first.
- Never resend after an error that reports the message as sent. Himalaya sends before it saves the copy, so a failed save does not mean a failed send.

## Reading

`--json` is global and goes before the subcommand. Reading leaves the seen flag alone unless you pass `--seen`.

```bash
himalaya mailbox list
himalaya --json envelope list -m inbox -s 20 | jq '.envelopes[] | {id, from, subject, date}'
himalaya message read 42
himalaya attachment list 42
himalaya attachment download --dir "$PWD/downloads" 42 2
```

`-m` takes an alias, a role (`sent`, `trash`) or the raw name from `mailbox list`. IMAP often reports no roles, so on Gmail use `'[Gmail]/Sent Mail'` unless the config sets an alias.

IDs belong to a mailbox and change when a message moves. List again before reusing an old ID, and confirm a move by the `message-id` field.

## Searching

`envelope list` takes no query. Use `envelope search`; its `--help` documents the grammar.

- There is no free-text condition: `search 'acme'` is a parse error. Name the fields: `'subject acme or body acme or from acme'`.
- There is no `before`. Use `not after 2026-09-01`.

```bash
himalaya --json envelope search 'after 2026-09-01 and (subject "acme corp" or body "acme corp") order by date desc'
```

## Changing the mailbox

```bash
himalaya message move --from inbox --to Archive 42
himalaya flag add --flag seen 42
himalaya message delete 42
```

`message delete` moves to Trash. Run on a message already in Trash, it deletes permanently.

## Sending

`message compose`, `reply` and `forward` print a draft without sending it. Under `--json` the draft is a decoded `{from, to, cc, bcc, subject, body}` you can show for review. Once approved, rerun the same command with `--send`.

```bash
himalaya --json message compose --to a@example.com --subject 'Follow-up' --body-file body.txt --attach cv.pdf
himalaya --json message reply 42 --body 'Thanks, Tuesday works.'
himalaya message reply 42 --body 'Thanks, Tuesday works.' --send
```

Gmail and Microsoft Graph file sent mail themselves. Don't pass `--save` there, or the copy is stored twice.

## Troubleshooting

```bash
himalaya account check
himalaya --log-level debug --log-file /tmp/himalaya.log envelope list
```

Debug logs hold message metadata, so keep them private.
