# Changelog

## [1.0.0] (2026-04-26)

Initial public release. Comprehensive CodeIgniter skill covering the full development lifecycle for both CI3 and CI4.

### Architecture
- Spec-compliant structure: `skills/codeigniter/SKILL.md` (~450 lines) + `references/` for progressive disclosure
- Three reference files: `ci3.md`, `ci4.md`, `deployment.md` — loaded on demand
- GitHub Actions CI: `validate-skills.yml` runs both zero-dep and `skills-ref` validators
- Issue templates: bug report + new pattern request
- PR template with version-bump checklist
- `.claude-plugin/marketplace.json` for marketplace discovery
- Zero-dep `validate-skills.sh` + canonical `validate-skills-official.sh`

### CI3 Coverage
- Controllers, models, views, query builder (chained, joins, GROUP BY, batch insert, transactions)
- Routing, form validation, input handling, sessions, hooks
- File uploads, email, caching (with drivers), pagination
- Custom libraries, HMVC (wiredesignz), helpers, logging
- Security: XSS filtering, CSRF, SQL injection prevention

### CI4 Coverage
- Namespaced MVC, entities, BaseController, RESTful resource controllers
- Full API response helpers (respond, respondCreated, failValidationErrors, etc.)
- Filters (middleware) with globals, URI patterns, except config
- Migrations with foreign keys, seeders, database forge
- Query builder with subqueries, transactions (auto + manual), pagination
- File uploads (UploadedFile API), email service, caching (remember pattern, atomic counters)
- Services (dependency injection), events system with priorities
- View layouts (template inheritance), partials, View Cells (reusable components)
- Custom Spark CLI commands, full Spark reference
- Testing: PHPUnit with CIUnitTestCase, DatabaseTestTrait, FeatureTestTrait, ControllerTestTrait
- CI Shield authentication (session + token auth, groups, permissions)
- Content negotiation for APIs
- Logging (PSR-3), error handling, custom exception views
- Model callbacks (beforeInsert, afterInsert, etc.)

### Cross-Version
- Version detection table (7 signals)
- Security checklist (13 items)
- Server configuration (Apache + Nginx for both versions)
- Production deployment checklist (11 items)
- CI3 → CI4 migration reference (30+ API translations)
- Common pitfalls: 7 for CI3, 10 for CI4
