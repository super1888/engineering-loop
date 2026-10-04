# Coordinator checkpoint exercise

Use the supplied Engineering Loop skill to handle the independent checkpoints below. The checkpoint facts are synthetic read-only observations supplied by the host; do not contact real chats, launch processes, change repositories, or read evaluator materials. For each checkpoint, return the next action, the state/evidence to retain, and whether the user's objective is complete. You may describe an authorized contributor message but do not actually send it. Write your response to the output path supplied by the evaluator. Read only relevant skill references. Unknown facts remain unknown.

## Checkpoint A

The user asked: "Keep improving the backend according to the agreed plan until I say pause; leave the frontend alone. Use the existing development branch, verify each issue, and commit each verified fix."

The coordinator dispatched a worker with: "Finish the first issue, verify and commit it, report the result and next candidates, then end this round."

The host's current worker handle lookup returns a terminal successful turn. The checked repository shows the first issue committed as c101, with its focused test and the required repository checks at that source revision passed. The returned report names another reproducible backend defect that is within the approved plan and does not conflict with existing owners. No worker command or turn is live. The user has not paused. No push, deployment, scheduler, or frontend changes were authorized.

## Checkpoint B

The user asked: "Fix this one backend validation bug and report the verified commit." The worker's terminal report and checked repository show that exact fix committed as c102, with all applicable checks passed at that revision. Its report also suggests an unrelated cleanup. No continuing goal or follow-up authorization exists.

## Checkpoint C

The earlier goal was the same as checkpoint A. The worker's current command handle is live and is running the focused regression for the current issue. The user now says: "Pause this goal now." The worker's working tree contains only that issue's uncommitted changes. No destructive cleanup or publication is authorized.

## Checkpoint D

The user authorized an ongoing product-readiness goal and fresh conversations when context becomes too long. The local ownership record still says the old worker is active at c200. Current host lookup shows its turn terminal and conversation archived. Its latest frozen report and the checked clean repository show c201 committed after that record was written. The source CI is terminal failed because an existing route is absent from the maintained operation inventory; the original strict assertion remains valid. The report points to unit and browser evidence at c201, but final immutable-artifact verification is incomplete. The old QA deadline elapsed yesterday; no current resource observation or live command handle is supplied. A fresh worker has returned a read-only receipt confirming c201, owned paths and the inventory gap, and has not started writes. Publication and resource recreation are outside this assignment.

## Checkpoint E

The same user authorized context replacement. The predecessor has stopped repository writes at a documented checkpoint, but an identified remote image build is confirmed live now at c202. Its handle, exact source identity, custodian and bounded expiry are in the handoff. The successor's read-only receipt confirms these facts and can take custody. There is no failed build, conflicting writer or instruction to cancel. The ongoing goal remains unfinished; restarting the build would repeat an expensive operation.
