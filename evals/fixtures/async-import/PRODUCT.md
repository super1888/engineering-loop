# Batch import — revision 1

Users submit 1–100 named rows. Each row has an opaque string rowId unique within the batch and a nonblank name. Submitting is asynchronous: HTTP acceptance does not mean records have been imported. Users must be able to see queued work and a terminal outcome.

When processing one row fails, retain the other successfully imported rows. The UI must show that the batch is only partially successful. Failures can be inspected; retry is not yet included in revision 1.

Repeated submission with the same client requestId and identical row payload identifies one batch, including after reopening the database. Reusing it for different data is a conflict. Successful rows must never create duplicate records.

The maximum batch size is 100. No file-upload parsing, authentication, new framework, real external integration or visual redesign is in scope.
