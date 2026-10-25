# Contributing

Thanks for your interest in improving this skill.

## How to Contribute

1. Fork this repository
2. Create a branch for your change
3. Edit `SKILL.md` — this is the skill content that agents consume
4. Update `CHANGELOG.md` with your changes
5. Open a pull request with a clear description

## Guidelines

- **Accuracy first**: Every code example must work on the stated CI version. Test it.
- **Version-specific**: Always clarify whether something applies to CI3, CI4, or both.
- **Security-conscious**: Never show insecure patterns without marking them as wrong. Always show the secure alternative.
- **Concise**: Agents load the full SKILL.md into context. Keep examples tight — show the pattern, not a full application.
- **No opinions**: Show framework-recommended patterns. Save architectural opinions for your own projects.

## What's Welcome

- Bug fixes in code examples
- Coverage for CI features not yet documented
- Updates for new CI4 releases
- Improved security guidance
- Better CI3 → CI4 migration mappings

## What to Avoid

- Adding non-CodeIgniter content (Laravel, Symfony, etc.)
- Opinionated architecture patterns (pick X over Y)
- Duplicating the official CodeIgniter documentation verbatim
- Adding third-party package guides (except CI Shield, which is official)

## Testing Your Changes

Install the skill locally and verify it triggers correctly:

```bash
npx skills add ./codeigniter
```

Then start a coding agent session in a CodeIgniter project and check that the skill loads and produces correct code.
