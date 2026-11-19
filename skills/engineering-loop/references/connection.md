# Required PMS MCP connection

Read before any activated stage or specialist, including analysis-only work. Team configuration or explicit user input identifies the service, workspace/project and workflow. A board URL identifies a project, not an MCP endpoint. Keep private bindings, member mappings and credentials outside this skill.

## Pass with actual reads

1. **Capability and identity:** required PMS tools are present and an authenticated identity read succeeds. The connection actor is not automatically the user or responsible task member.
2. **Intended target:** read the workspace/project identified by explicit input or maintained project configuration and check its returned identity. A previous project's access is not a default. Ask only a missing target decision when ambiguous; supplied task references must belong to the intended project.
3. **Workflow:** read actual project statuses; inspect required field definitions when relevant to the next operation. Use returned slugs/options, never guessed labels. Success from another project or unrelated service does not pass.

Keep a compact result with actor, target, required capabilities, status mapping, successful-read evidence and limits. Configuration, tool registration, dependency metadata or a self-written "connected" receipt are insufficient. Reads prove read access, not write permission or atomic claiming. Metadata does not install, authenticate or call the service.

Missing tools, failed identity, denied/wrong project, unreadable workflow or unavailable required capability block downstream stages, specialists and source/PMS writes. Permit only minimal local reads and probes needed to identify the target or diagnose/repair connection within existing authority. Report the failed prerequisite and remedy; do not substitute offline work, expose secrets, change global configuration without authority or bypass MCP with direct APIs. A stop request takes effect immediately.

Reuse evidence within the same session, credential identity, target and valid connection. Account/target changes, access changes or authentication/transport errors invalidate affected evidence: restore it before further routed work. A stage change alone needs no repeated identical probe. Preserve completed artifacts, live handles and pending synchronization; do not replay verified work to repair a connection.

## Adapter and next route

Discover the current tool schema. For Kaneo, use `whoami`, `get_project` and `list_project_columns`; read `list_project_custom_fields` for relevant required fields. Another PMS must establish equivalent capabilities, not inherit assumed names.

After success, identify the current task's stage through the [entrypoint](../SKILL.md), read that stage and apply the common [route challenge](grill.md) before execution. Read [pms.md](pms.md) when working with a task reference, performing task operations or following an applicable tracking policy; it contains creation, claiming, concurrency and write-back rules. Connection checks remain read-only and do not authorize those operations.
