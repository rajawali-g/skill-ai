# AGENTS.md — instructions for agents editing this repo

This file tells AI coding agents (Claude Code, Cursor, Codex, etc.) how to work on *this repo itself* — i.e. when you're adding new CodeIgniter patterns, fixing examples, or expanding coverage. It's not for agents *consuming* the skill at runtime; those agents read the SKILL.md directly.

## Ground rules

1. **Every code example must compile and run.** Don't show patterns you haven't mentally traced through the framework. If it's CI3, it must use CI3 APIs. If it's CI4, it must use CI4 namespaced APIs. Never mix them.

2. **Always state the version.** Any pattern that's version-specific must say CI3 or CI4. If it works on both, say so explicitly.

3. **Don't copy the official docs.** The CodeIgniter User Guide is open source (MIT) but our skill adds value by being opinionated, concise, and showing patterns the docs don't. Link to docs for deep dives; don't mirror them.

4. **Security first.** Never show an insecure pattern as a working example. If you show a wrong way, mark it clearly and immediately follow with the correct version.

5. **Keep SKILL.md body under 500 lines.** The spec recommends this for progressive disclosure. Move deep content into `references/` files.

## Where things live

| Path | Purpose |
|---|---|
| `skills/codeigniter/SKILL.md` | Core skill — frontmatter + essential patterns (~450 lines) |
| `skills/codeigniter/references/ci3.md` | CI3 deep dive: uploads, email, caching, HMVC, libraries |
| `skills/codeigniter/references/ci4.md` | CI4 deep dive: REST, migrations, testing, Shield, services |
| `skills/codeigniter/references/deployment.md` | Server config, production checklist, migration table |
| `.claude-plugin/marketplace.json` | Plugin manifest for marketplace discovery |
| `README.md` | Public-facing intro, install, features, keywords |
| `CHANGELOG.md` | Keep-a-changelog format, one section per tagged release |
| `CONTRIBUTING.md` | How external contributors should submit changes |
| `AGENTS.md` | This file — instructions for agents editing the repo |
| `THIRD_PARTY_NOTICES.md` | License acknowledgements |
| `validate-skills.sh` | Zero-dep spec validator |
| `validate-skills-official.sh` | Canonical `skills-ref` validator |

## Frontmatter

```yaml
---
name: codeigniter            # must match directory name under skills/
description: "..."           # 1-1024 chars, must include trigger keywords
license: MIT
metadata:
  author: yasserstudio
  version: "1.0.0"          # semver — bump on meaningful changes
---
```

## Progressive disclosure

Per the [agentskills.io spec](https://agentskills.io/specification):

1. **Metadata** (~100 tokens) — `name` + `description` loaded at startup
2. **SKILL.md body** (<500 lines) — loaded when the skill activates
3. **References** (on demand) — `references/*.md` loaded only when the topic comes up

Keep the core SKILL.md tight. If a section grows, move it to a reference file.

## PR checklist

Before submitting changes:

- [ ] `./validate-skills.sh` passes locally
- [ ] SKILL.md body still under 500 lines
- [ ] Description still under 1024 chars
- [ ] Code examples are syntactically correct PHP
- [ ] CI3 examples use `$this->load->`, `$this->db->`, `CI_Controller`, etc.
- [ ] CI4 examples use namespaces, `model()`, `service()`, `view()`, etc.
- [ ] No raw `$_POST`/`$_GET` in any example
- [ ] CHANGELOG.md updated with what changed
- [ ] Version in SKILL.md frontmatter bumped if this is a release
- [ ] `.claude-plugin/marketplace.json` version updated if releasing
