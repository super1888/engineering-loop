# Record workspace

The list has a group filter, pagination and an independently scrollable record area. Users open details while working through the list.

- Returning from a detail opened from the list preserves the selected group, page and record-area scroll position. This applies to Save, Cancel, the close button, Escape and clicking the backdrop.
- Save applies the edited record name. Dismissal does not apply an unsaved name. Each action leaves one usable list view.
- A direct detail URL (`?record=17`) has no originating list context. Closing it opens the default list: all groups, page 1, scroll position 0.
- Keep the existing group filtering, page size, editing and labels except for any explicitly requested copy change. No new navigation framework, persistence mechanism or visual redesign is required.
