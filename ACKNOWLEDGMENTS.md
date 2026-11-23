# Acknowledgments

This independently written draft was informed by public ideas in:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), including [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) and [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) (MIT): dependency-aware questioning, delegated fact lookup and scoped learning. The built-in route challenge is independently written; no upstream skill is installed or bundled.
- [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills): executable constraints and evaluating skill behavior.
- [Superpowers](https://github.com/obra/superpowers): diagnostic discipline, verification before completion, a confirmation gate before building and reviewers that do not receive the author's reasoning.
- [OpenSpec](https://github.com/Fission-AI/OpenSpec): separating effective specifications from changes.
- [GSD Core](https://github.com/open-gsd/gsd-core): recoverable task state and end-to-end wiring.
- [Project-vibe-spec](https://github.com/coderlishang/Project-vibe-spec) and [ai-rd-skills](https://github.com/535803710/ai-rd-skills): project-aware documentation and practical requirement clarification.
- [CS146S public assignments](https://github.com/mihail911/modern-software-dev-assignments): applying workflow automation to a working application and recording before/after outcomes; describing entities, relationships and UI flows. Classroom tool and stack requirements are not adopted as project requirements.
- [Google Cloud's Vibe Coding for Beginners](https://www.coursera.org/learn/vibe-coding-for-beginners-from-zero-to-app): the public module outline's emphasis on incremental features and task context. This is not a claim to have reviewed the full course or validated its outcomes.

v0.1.35 rewrote method rules from the sources below into the stage guides. Each was read at its repository's default branch on 2026-11-23; the license is as read there. No text, table or example was copied.

| Source | License | Informed |
|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills): grilling, domain-modeling, codebase-design, prototype, to-tickets, tdd, diagnosing-bugs, code-review, retro | MIT | Question rounds, decision-record gate, deletion test, structural variants, task slices, test seams and doubles, diagnosis loop, two-pass review, checks over instructions |
| [obra/superpowers](https://github.com/obra/superpowers): writing-plans, test-driven-development, systematic-debugging, requesting-code-review, receiving-code-review, subagent-driven-development, verification-before-completion | MIT | Plan contents, failing for the right reason, boundary tracing, reviewer isolation, acting on feedback, claim-to-evidence mapping |
| [github/spec-kit](https://github.com/github/spec-kit): clarify, checklist, specify, analyze commands | MIT | Ambiguity scan, checking requirement text, measurable criteria, requirement–task trace |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills): interview-me, api-and-interface-design | MIT | Replies that are not confirmation, idempotency keys |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills): software-architecture, api-design-and-evolution, qa-methodology, release-engineering, migration-engineering, site-reliability-engineering, incident-learning | MIT | Quality scenarios, representation semantics, frozen acceptance expectations, undo paths, recovery classes, bounded production actions, closure evidence |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable): shape reference | Apache-2.0 | Content ranges and anti-goals before layout |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official): code-review command | Apache-2.0 | Validating each finding, do-not-report list |
| [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | MIT | Find, filter, drop; default exclusions; trust assumptions |
| [github/awesome-copilot](https://github.com/github/awesome-copilot): incident-postmortem | MIT | No invented facts, timeline gaps, detect versus mitigate |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin): ce-compound | MIT | Whether to record a lesson and in which form |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills): react-best-practices, composition-patterns | MIT per skill frontmatter | Request waterfalls, server boundaries, bundle loading, component variants |
| [ant-design/ant-design-cli](https://github.com/ant-design/ant-design-cli): antd skill | MIT | Optional offline lookup of props, tokens and deprecated usage |
| [piomin/claude-ai-spring-boot](https://github.com/piomin/claude-ai-spring-boot) | Apache-2.0 | Spring Boot 4 changes, migration and error-handling rules |
| [fastapi/fastapi](https://github.com/fastapi/fastapi): bundled agent skill | MIT | Annotated dependencies, return types, router-level configuration |
| [wispbit-ai/skills](https://github.com/wispbit-ai/skills), [supabase/agent-skills](https://github.com/supabase/agent-skills), [planetscale/database-skills](https://github.com/planetscale/database-skills) | MIT (the first per skill frontmatter) | PostgreSQL and MySQL index, lock and migration rules |
| [openai/skills](https://github.com/openai/skills): security-best-practices | Apache-2.0 | FastAPI and React security items |

Ideas only, with no adapted wording: [trailofbits/skills](https://github.com/trailofbits/skills) (CC-BY-SA-4.0; restating a finding's claim and classifying risk by what a change touches) and the vercel-labs web-design-guidelines skill (no license found; a few interface checks).

No third-party skill implementation is bundled. Links acknowledge influences, not compatibility certification, endorsement, or a claim that this project reproduces their behavior.
