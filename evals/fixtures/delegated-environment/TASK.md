# Delegated execution environment controls

Motivation: prior real trials found a protected checkout’s interpreter inaccessible to a child, a sanitized PATH unable to resolve the CLI, and host browser modules absent from a contributor’s module path. See the retained independent-review and frontend runtime reports. Do not reinterpret those failures as code defects or evidence that new guidance improves model decisions.

Reusable controls, documented after the initial mechanism test run (not a pre-registered model study):

- Demonstrate that the parent can use a synthetic script inside a directory that will be denied to the child. Under the actual guard, establish permission failure instead of treating a missing file or broken interpreter as a successful denial.
- Invoke a permitted interpreter and a workspace script without changing the denied roots; verify legitimate work succeeds while the protected script remains unreadable.
- When Node is available, create a temporary synthetic module. An explicit module-resolution path makes it usable in one child, while the same child command without that setting fails to resolve it. Restore the setting rather than installing or copying a toolchain.

These are executable environment controls, not model trials. They do not require Playwright or a paid service. macOS-only guard checks and missing Node are reported as skips where applicable, not as verified capability. A clear read-only assignment with no runtime dependency remains a legitimate lightweight counterexample.

Future behavioral evaluation should give a fresh contributor a real authorized runtime task and relevant non-sensitive entrypoints, then observe execution or an accurately reported environment limit. Do not claim that these deterministic controls establish that transfer, task quality or speed.
