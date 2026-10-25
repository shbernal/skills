---
name: yutu
description: Use when managing a YouTube channel or reading YouTube data from the terminal with the yutu CLI, including uploads, metadata and privacy changes, thumbnails, playlists, comments, captions, search and video stats.
---

# YouTube with yutu

Version: v0.11.0

If the command is missing, install it:

```bash
mise use -g github:eat-pray-ai/yutu
```

## Setup

yutu reads and writes files only inside `YUTU_ROOT` (default: the current directory), and looks for `client_secret.json` and `youtube.token.json` there. Point it at a fixed location once:

```bash
mise set -g YUTU_ROOT=/ \
  YUTU_CREDENTIAL='{{env.HOME}}/.config/yutu/client_secret.json' \
  YUTU_CACHE_TOKEN='{{env.HOME}}/.config/yutu/youtube.token.json'
```

Without `client_secret.json`, the user creates it in [Google Cloud Console](https://console.cloud.google.com/): a project with YouTube Data API v3 enabled, an OAuth consent screen listing them as a test user, and an OAuth client of type Desktop app, downloaded as JSON. A consent screen left in Testing issues tokens that expire after 7 days. Publishing it to production avoids that, and an unverified app is fine for personal use.

The user signs in through a browser, so they run auth themselves. `auth` ignores the env vars unless they are passed as flags:

```bash
yutu auth --credential "$YUTU_CREDENTIAL" --cacheToken "$YUTU_CACHE_TOKEN"
yutu channel list --for mine
```

## Rules

- Write commands print their target and refuse to run without `--yes`. Run without it first, show the user what will change, and add `--yes` only after they confirm. Get explicit confirmation before any `delete`.
- Report resource IDs back to the user.
- File flags (`--file`, `--thumbnail`) reject absolute paths: pass them relative to `YUTU_ROOT`. With `YUTU_ROOT=/`, strip the leading slash: `--file "$(realpath video.mp4 | cut -c2-)"`.
- The YouTube Data API v3 quota is 10,000 units a day. `search list` costs 100 units and a `list` call costs 1. Prefer `list` with IDs or playlists over search.

## Reading

`--output json` returns an array. `--maxResults` defaults to 5, and `0` means no limit.

```bash
yutu channel list --for mine --parts id,snippet,contentDetails,statistics --output json
yutu channel list --forHandle @somechannel --output json
yutu video list --ids VIDEO_ID --parts id,snippet,status,statistics --output json
yutu search list --q 'rust tutorial' --types video --order viewCount --maxResults 10 --output json
yutu playlist list --mine --maxResults 0 --output json
yutu commentThread list --videoId VIDEO_ID --maxResults 50 --output json
yutu caption list --videoId VIDEO_ID --output json
yutu caption download --id CAPTION_ID --tfmt srt --file captions.srt
yutu videoCategory list --regionCode US --output json
```

`caption download` works only on the user's own videos.

### Unlisted and private videos

`search list` returns public videos only. The uploads playlist holds every upload whatever its privacy. Its ID is the channel ID with `UC` swapped for `UU`. `video list --ids` takes up to 50 IDs per call.

```bash
UPLOADS=$(yutu channel list --for mine --parts contentDetails --output json \
  | jq -r '.[0].contentDetails.relatedPlaylists.uploads')
yutu playlistItem list --playlistId "$UPLOADS" --maxResults 0 --output json \
  | jq -r '.[].snippet.resourceId.videoId' | xargs -n50 | tr ' ' ',' \
  | while read -r ids; do yutu video list --ids "$ids" --parts id,snippet,status --output json; done \
  | jq -c '.[] | select(.status.privacyStatus != "public") | {id, title: .snippet.title, privacy: .status.privacyStatus}'
```

## Writing

`video update` keeps every field you don't pass. `--tags` replaces the whole tag list.

```bash
yutu video insert --file "$(realpath video.mp4 | cut -c2-)" --title 'Draft' \
  --description 'Brief of what happens in the video' --categoryId 22 --privacy unlisted --output json
yutu video update --id VIDEO_ID --title 'New title' --tags 'a,b,c' --privacy public
yutu thumbnail set --videoId VIDEO_ID --file "$(realpath thumb.jpg | cut -c2-)"
yutu playlist insert --title 'Series' --privacy public --channelId CHANNEL_ID
yutu playlistItem insert --kind video --playlistId PLAYLIST_ID --channelId CHANNEL_ID --kVideoId VIDEO_ID
yutu commentThread insert --videoId VIDEO_ID --channelId CHANNEL_ID --textOriginal 'What should I cover next?'
yutu comment insert --parentId COMMENT_ID --textOriginal 'Thanks!'
yutu video delete --ids VIDEO_ID
```

Each runs only with `--yes` appended. To take an item out of a playlist, delete the playlist item's ID, not the video's ID:

```bash
yutu playlistItem list --playlistId PLAYLIST_ID --maxResults 0 --output json \
  | jq -r '.[] | select(.snippet.resourceId.videoId == "VIDEO_ID") | .id'
yutu playlistItem delete --ids ITEM_ID
```

### Publishing pipeline

1. Upload as unlisted, with a plain description of the content as a brief.
2. Read it back with `video list`, then draft the title, description and tags from the brief.
3. After the user approves, update with `--privacy public`, set the thumbnail and add the video to its playlist.

Metadata that helps a video get found:

- Title: keywords at the front, under 60 characters. Offer 2 or 3 options.
- Description: the first two lines show in search. Include keywords, timestamps for long videos, a call to action, and 3 to 5 hashtags at the end.
- Tags: mix broad and long-tail terms. The first few carry the most weight.
- Thumbnail: high contrast, 3 or 4 words of large text, one focal point, a style that matches the channel.

## Troubleshooting

`YUTU_LOG_LEVEL=DEBUG` logs requests. `failed to parse client secret` means the credential path is outside `YUTU_ROOT` or missing. yutu then tries to read the path as Base64.
