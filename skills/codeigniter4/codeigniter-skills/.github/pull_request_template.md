## Summary

<!-- One-liner: what this PR changes and why. -->

## Type of change

- [ ] New section or pattern added to skill
- [ ] Description change (triggering behavior)
- [ ] Content fix (typo / clarification / example / link)
- [ ] Infrastructure (validator / CI / marketplace.json / docs)

## Checklist

- [ ] `./validate-skills.sh` passes locally
- [ ] SKILL.md body still under 500 lines
- [ ] Description still under 1024 chars
- [ ] Code examples are syntactically correct PHP
- [ ] CI3 examples use CI3 APIs; CI4 examples use CI4 APIs
- [ ] No raw `$_POST`/`$_GET` in any example
- [ ] `CHANGELOG.md` updated
- [ ] If description changed, noted whether it broadens or narrows triggering

## Version bump (if releasing)

- [ ] MAJOR — removed/renamed skill, narrowed description, broke compatibility
- [ ] MINOR — new section, broadened description
- [ ] PATCH — typo, clarification, link fix
- [ ] N/A — not a release PR
