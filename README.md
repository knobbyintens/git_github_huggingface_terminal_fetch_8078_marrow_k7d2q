# Marrow SDK

Marrow is our internal event-processing SDK. It ships on a rolling schedule
and powers the batch and streaming pipelines used by the data desk.

## Repository layout

- `docs/release-index.md` - curated index of shipped stable releases; the
  documentation site is generated from this table.
- `docs/CONTRIBUTING.md` - release and index maintenance rules.
- `release-desk/manifests-2026.json` - raw release manifests emitted by the
  release desk after every cut.
- `src/marrow/` - SDK sources.
- `tests/` - unit tests.

The default branch always carries the full release index. Work on the index
tooling happens on a feature branch and is published from there.
