# CodeIgniter Skills for AI Coding Agents

**Stop your AI agent from mixing up CI3 and CI4 code.** This skill gives Claude Code, Cursor, Codex, and Copilot 1,600 lines of production-tested CodeIgniter patterns — so it writes framework-correct code instead of generic PHP.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Spec: agentskills.io](https://img.shields.io/badge/spec-agentskills.io-green.svg)](https://agentskills.io/specification)
[![CI4: 4.7.x](https://img.shields.io/badge/CI4-4.7.x-EF4223.svg)](https://codeigniter.com)
[![CI3: 3.1.x](https://img.shields.io/badge/CI3-3.1.x-DD4814.svg)](https://codeigniter.com)

---

## The Problem

AI agents don't know CodeIgniter well. Ask one to build a CI4 controller and you'll get:

- `$this->load->model()` in a CI4 project (that's CI3 syntax)
- Missing `$allowedFields` — silent mass assignment vulnerabilities
- Raw `$_POST` instead of `$this->request->getPost()`
- `echo view()` instead of `return view()` — broken response handling
- Generic PHP instead of query builder, Shield auth, or Spark CLI

Every fix costs you a back-and-forth. Multiply that across a real project and you're spending more time correcting the agent than coding yourself.

## The Fix

Install one skill. Your agent instantly knows both CI3 and CI4 — correct syntax, security patterns, version-specific APIs, and 30+ migration mappings between the two.

```bash
npx skills add yasserstudio/codeigniter-skills
```

## Before & After

| Without this skill | With this skill |
|---|---|
| Mixes CI3/CI4 syntax | Auto-detects version from project signals |
| Forgets `$allowedFields` | Includes mass assignment protection by default |
| Uses raw `$_POST`/`$_GET` | Uses `$this->request->getPost()` with CSRF |
| Writes generic PHP auth | Integrates CI Shield (session + token auth) |
| Doesn't know Spark CLI | Generates migrations, seeders, filters, commands |
| Ignores upload security | Uses `guessExtension()` + MIME validation |
| No tests | PHPUnit with `FeatureTestTrait` + `DatabaseTestTrait` |

## What's Inside

### CI3 — 12 Sections
Controllers, models, query builder (joins, transactions, batch insert), routing, form validation, input/security, file uploads, email, caching, pagination, custom libraries, HMVC, sessions, hooks, helpers, logging.

### CI4 — 20 Sections
Controllers, RESTful resource controllers (11 response helpers), models with callbacks, entities, routing (groups, custom placeholders), filters/middleware, migrations with foreign keys, seeders, query builder (subqueries, manual transactions, pagination), file uploads (UploadedFile API), email service, caching (remember pattern, atomic counters), services/DI, events, view layouts/partials, View Cells, custom Spark commands, testing (unit/feature/controller), Shield authentication, content negotiation, logging, error handling.

### Cross-Version — 5 Sections
Version detection (7 signals), security checklist (13 items), server config (Apache + Nginx), production deployment checklist (11 items), CI3 → CI4 migration table (30+ mappings).

## How It Works

```
1. Install the skill             →  npx skills add yasserstudio/codeigniter-skills
2. Open your CI project          →  The agent detects CI3 or CI4 automatically
3. Ask it to build something     →  It writes version-correct, secure code
```

The skill loads into your agent's context when it detects a CodeIgniter project (via `system/core/CodeIgniter.php`, `app/Config/App.php`, `spark` CLI, or `codeigniter4/framework` in `composer.json`).

## Who Is This For

- **CI3 maintainers** stuck on legacy projects who need their agent to understand `$this->load->`, HMVC, and CI3 query builder
- **CI4 developers** building APIs, admin panels, or SaaS apps with Shield auth, resource controllers, and Spark CLI
- **Teams migrating CI3 → CI4** who need the agent to know both APIs and the translation between them
- **Anyone tired of correcting** their AI agent's CodeIgniter code

## Quick Install

**One command:**

```bash
npx skills add yasserstudio/codeigniter-skills
```

**Or clone locally:**

```bash
git clone https://github.com/yasserstudio/codeigniter-skills.git
npx skills add ./codeigniter-skills
```

Works with Claude Code, Cursor, Codex, Copilot, and any agent that supports the [agentskills.io](https://agentskills.io) spec.

## FAQ

**Does this work with CI3, CI4, or both?**
Both. The skill covers CI3 (3.1.x) and CI4 (4.7.x) with version-specific patterns. It auto-detects which version your project uses.

**Will this slow down my agent?**
No. The skill is a single markdown file (~1,600 lines) that loads into context only when working on a CodeIgniter project.

**Does it cover Shield authentication?**
Yes — setup, session/token filters, route groups, user groups, and permissions.

**What about testing?**
Full CI4 PHPUnit coverage: `CIUnitTestCase`, `DatabaseTestTrait`, `FeatureTestTrait`, `ControllerTestTrait` with examples.

**Is this just a copy of the CodeIgniter docs?**
No. The official docs are 2,000+ pages of reference material. This skill is 1,600 lines of opinionated, agent-optimized patterns focused on what agents get wrong — security, version confusion, common pitfalls, and production deployment.

## File Structure

```
codeigniter-skills/
  skills/codeigniter/
    SKILL.md                   # Core skill (~450 lines, spec-compliant)
    references/
      ci3.md                   # CI3 deep dive: uploads, email, caching, HMVC, libraries
      ci4.md                   # CI4 deep dive: REST, migrations, testing, Shield, services
      deployment.md            # Server config, production checklist, full migration table
  .claude-plugin/
    marketplace.json           # Marketplace discovery manifest
  .github/
    workflows/validate-skills.yml
    pull_request_template.md
    ISSUE_TEMPLATE/
      bug.md
      new-pattern.md
  validate-skills.sh           # Zero-dependency spec validator
  validate-skills-official.sh  # Canonical skills-ref validator
  README.md
  CHANGELOG.md
  CONTRIBUTING.md
  AGENTS.md
  THIRD_PARTY_NOTICES.md
  LICENSE
```

## Disclaimer

This skill is an independent community project. It is not affiliated with, endorsed by, or officially connected to the British Columbia Institute of Technology (BCIT) or the CodeIgniter Foundation. "CodeIgniter" is a trademark of BCIT.

## License

MIT — [Yasser's Studio](https://github.com/yasserstudio)
