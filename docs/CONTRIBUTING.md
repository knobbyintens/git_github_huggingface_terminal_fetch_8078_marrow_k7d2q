# Contributing: release index maintenance

The curated release index lives at `docs/release-index.md`. It is the single
source of truth for the published documentation site.

## Table shape

| Version | Date | Channel | Highlights |
| --- | --- | --- | --- |

- `Version` - the exact release tag, e.g. `v4.1.0`.
- `Date` - the release date in `YYYY-MM-DD` form.
- `Channel` - `stable`, `beta` or `rc`.
- `Highlights` - one short English sentence, at most 120 characters.

## Ordering

Rows are strictly chronological by release date (oldest first). Never insert
a row in the middle: append new rows at the bottom in date order.

## Scope

Only released work is indexed. Drafts, unshipped plans and non-stable channels
are not part of the public index.

Only artifacts distributed under an approved license (Apache-2.0, MIT,
BSD-3-Clause or CC-BY-4.0) may be listed. Never add a version that is already
in the table.
