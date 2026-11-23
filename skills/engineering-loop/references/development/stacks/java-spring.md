# Team Java / Spring service rules

**ID:** `dev.stack.java-spring` · **Status:** partial. Extracted on 2026-11-21 from the team's two maintained Java services, keeping what both follow or what a build check enforces. Confirmation as the cross-project standard is pending, and the open decisions at the end are not settled.

Use when the affected module is a Java/Spring service. An existing project's effective instructions and checks win where they differ. A new service starts from these rules. Baseline observed: JDK 21, Spring Boot 4.1, MyBatis-Plus 3.5, MySQL 8; confirm the module's own versions first.

Several rules deliberately differ from common Spring advice. Follow them; do not "correct" them toward the mainstream style.

## Structure and naming (B1, B2)

- Inject beans with `jakarta.annotation.Resource` on fields. No `@Autowired`, and no parameterized constructor or `@RequiredArgsConstructor` on a managed component.
- No `record` in production code. No nested Request/Response classes and no nested enums.
- Name by boundary: `*Request` in, `*Response` out, `*DTO` / `*CommandDTO` / `*QueryDTO` inside, `*Entity` persisted. An entity never crosses an HTTP or module boundary, and a mapper never returns a Response.
- Layer as Controller → application `*Manager` (orchestration) → `*Service` (MyBatis-Plus `IService`, thin persistence) → Mapper. One Mapper, Service and Impl per entity. Impl classes do not call each other, and nothing uses the static `Db` lookup.
- Call another module only through its narrow `api` package or a domain event. Never import its Mapper, Entity or Service, or write its tables. `common` does not depend on a business module.
- A closed vocabulary is an enum in an `enums` package, with `code` equal to the enum name and a Chinese description. Do not compare raw strings or keep the vocabulary in a `*Constants` class.
- Import types and use short names; write a fully qualified name only for a real clash.

## API (B1)

- Give every HTTP input an explicit Bean Validation bound: text length, collection size, identifier format, path variable, page size, cursor and the `Idempotency-Key` header, with `@Valid` cascading. A bare `String` or `List` field in a `*Request` is the sign of a miss.
- Page with an explicit `Page` / `IPage`, the pagination interceptor last and at most 100 rows. Never expose `IPage`, `Page` or `PageInfo` over HTTP. No PageHelper or ThreadLocal paging.
- Send long IDs, cursors and resource versions as JSON strings. Do not fix a frontend type error by changing the global Jackson policy. See [R1](../rules/data-fidelity.md).

## Persistence (B3)

- List columns; never `SELECT *`. Use Lambda wrappers, not a string-column `QueryWrapper`.

## Transactions and concurrency (B4)

- As a team convention, put `@Transactional` only on public methods. In Spring 6 and later, class-based proxies can also advise protected and package-private methods by default. Interface-based proxies require a public method declared in the proxied interface. In proxy mode, transaction advice applies only to calls through the proxy. [Spring transaction method visibility](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html#transaction-declarative-annotations-method-visibility)
- Keep model, OCR, object-storage, mail and broker calls out of a database transaction. Wrap the short write segments around the remote call in `TransactionTemplate`. A remote client call inside a `@Transactional` manager is the sign of a miss.
- A persistent `version` field carries `@Version`, one per hierarchy. Turn an affected-row count other than 1 into a conflict response; never overwrite silently. See [R5](../rules/concurrent-edits.md).
- Scope idempotency to actor, key, action and request fingerprint. The same key with a different payload is a conflict. Write the reservation in the business transaction. See [R4](../rules/async-idempotency.md).
- Treat a Redis or Redisson lock as a short-window guard. The final defence is a unique key, an optimistic lock or a compare-and-set state update, and the path fails closed when Redis is down. Never keep permissions, balances or task status in a local cache.

## Jobs (B6)

- Never combine `@Scheduled` with `@Async`: `fixedDelay` enqueues the next run before the previous one ends. A scheduled worker submits to a named bounded executor through a coalescing dispatcher.
- Claim a task with a compare-and-set on its prior state plus a lease. Keep state machines monotonic so a late event cannot overwrite a terminal state. Write the outbox row in the same transaction as the business fact and mark it published only after the broker confirms.

## Configuration, logging and build (B8, E3)

- Read configuration through validated `@ConfigurationProperties`; never `@Value`.
- Log through the SLF4J facade only. Keep secrets out of `toString`, and never log tokens, full prompts or full vendor payloads.
- Pin the JDK and Maven ranges, reactor convergence and patched-dependency floors with Maven Enforcer.

## Testing

- Run a targeted test as `-pl <module> -am -Dtest=X -Dsurefire.failIfNoSpecifiedTests=false`, because `-am` pulls in upstream modules without that class. Never use `-DskipTests`.
- A MySQL integration test connects directly to a freshly created random database. A reused Connector/J `Statement` keeps its original database and can run unqualified DDL against the wrong schema.

## Adapted from public sources (unconfirmed for the team)

A team rule above wins where they differ, and every open decision below stays open. This section holds Spring Boot 4 facts and migration safety only. It does not change the injection, naming or layering rules and adds no dependency.

Spring Boot 4, after confirming the module's version:

- Starters were renamed. When a build file is touched, use `spring-boot-starter-webmvc` (not `-web`), `-aspectj` (not `-aop`), `spring-boot-starter-security-oauth2-*`, `spring-boot-starter-flyway` with `flyway-mysql`, and the per-technology test starters `spring-boot-starter-<technology>-test`.
- Jackson 3 lives in `tools.jackson`. Use `JsonMapper` where `ObjectMapper` was used, and `@JacksonComponent` for `@JsonComponent`. Only the annotations keep `com.fasterxml.jackson.annotation`.
- `@MockBean` and `@SpyBean` are removed. Use `@MockitoBean` and `@MockitoSpyBean`.
- Boot no longer manages a Spring Retry version. An existing use needs an explicit version or the framework's own retry support.
- Build with the Maven command, not from IDE-compiled classes, which can hide compiler errors.

Errors:

- A catch-all handler logs the exception and returns a fixed message. It never returns the exception's message, class name or SQL text, in either response shape.
- Where the project uses problem details, the catch-all 500 and validation errors use that shape too.
- Map a unique-key violation to a conflict by its error code, not by matching message text that can change.

Migrations, where the project uses versioned Flyway files:

- Never edit an applied migration. Each change is one new `V<n>__<description>.sql`, in the same commit as the entity and mapper change.
- A new `NOT NULL` column carries a `DEFAULT` or a backfill, so existing rows keep working.
- Name every constraint and index explicitly in the project's prefix scheme. Keep column defaults equal to entity defaults.
- Check lock behavior and index shape against the [SQL rules](sql.md).

## Enforcement

In the reference service most of these rules are ArchUnit or contract tests run by the build. Port the check together with the rule into a new service; a rule without its check is documentation only. Three rules above are documentation only today: remote calls outside transactions, the lock rule, and the claim and outbox rule.

## Open team decisions

The team's services differ on these. Follow the current project's choice. For a new service, raise the choice with its owner in stage 02 and do not pick silently.

- Response shape: problem-detail errors with bare success bodies, or a success/code/message/data envelope.
- Schema changes: versioned immutable migration files, or one maintained SQL baseline.
- Configuration: literal development values, or `${VAR:default}` placeholders with a configuration centre.
- Identifier type: string ULID, or `Long` serialized as a string.
- A shared `CommonUtils` class: narrowly allowed, or banned.
- Test database: an in-memory database in MySQL mode, or real MySQL only; and how much mocking is acceptable.
- Status for an optimistic conflict: 409, or 412 with 428 for a missing precondition.
