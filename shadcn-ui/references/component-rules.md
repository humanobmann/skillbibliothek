# Component Rules

## Composition

- Keep `SelectItem` inside `SelectGroup`, menu items inside menu groups, and command items inside command groups.
- Use `asChild` for Radix-based custom triggers and the Base UI equivalent supported by the installed component API. Confirm the project's `base` field before choosing syntax.
- Include an accessible title in `Dialog`, `Sheet`, and `Drawer`. A visually hidden title is acceptable when the visual design supplies equivalent context.
- Use the complete Card structure when the content has a title, description, body, or actions. Do not collapse every concern into `CardContent`.
- Put `TabsTrigger` inside `TabsList`.
- Always include `AvatarFallback`.
- For loading buttons, compose a spinner and disabled state. Do not invent unsupported `isLoading` props.

## Prefer standard components

Use the available shadcn component instead of custom markup when suitable:

- Callout: `Alert`
- Empty state: `Empty`
- Toast: `sonner`
- Separator: `Separator`
- Loading placeholder: `Skeleton`
- Status label: `Badge`
- Destructive confirmation: `AlertDialog`
- Modal task: `Dialog`
- Side panel: `Sheet`
- Mobile bottom surface: `Drawer`
- Command palette: `Command` within `Dialog`

## Forms

- Structure fields with `FieldGroup` and `Field`.
- Use `InputGroupInput` or `InputGroupTextarea` inside `InputGroup`.
- Put buttons or other adornments inside `InputGroupAddon`.
- Use `FieldSet` and `FieldLegend` for semantic related groups.
- Use `data-invalid` on the field container and `aria-invalid` on the control.
- Use `data-disabled` on the field wrapper when the field is disabled.
- Keep labels associated through `htmlFor` and control `id`, or use the supported accessible composition API.
- Ensure error descriptions are programmatically connected when validation messages appear.

## Styling

- Prefer semantic tokens to fixed palette classes for application surfaces and state styling.
- Avoid raw dark-mode overrides when semantic tokens already cover the state.
- Use `flex` or `grid` with `gap-*` rather than `space-x-*` or `space-y-*`.
- Use `size-*` for equal width and height.
- Use `truncate` instead of manually composing overflow, ellipsis, and nowrap classes.
- Use `cn()` for conditional classes.
- Avoid arbitrary z-index values on overlays unless a verified layering bug requires a local fix.
- Keep reusable theme changes in the project's actual global CSS or token location reported by shadcn info.

## Icons

- Use the configured icon library from project info.
- Inside shadcn buttons and similar components, use the component's expected icon semantics such as `data-icon` when supported.
- Do not force icon sizing classes when the parent component already controls icon dimensions.
- Pass icon components directly rather than stringly typed icon-name lookups when the API expects components.

## Accessibility

Check:

- Logical heading hierarchy.
- Accessible names for icon-only controls.
- Keyboard reachability and expected arrow-key behavior for composite widgets.
- Visible focus treatment.
- Dialog focus trapping and focus return.
- Sufficient contrast in default, hover, focus, disabled, and destructive states.
- Error messages linked to fields.
- No color-only communication of status.
- Correct semantics for buttons versus links.
- Touch targets that remain usable on mobile.

## Responsive behavior

- Define mobile stacking and reflow explicitly.
- Avoid tables that become horizontally unusable without a deliberate responsive strategy.
- Use `Sheet` or another appropriate pattern for dense navigation on narrow screens when justified.
- Verify dialogs, popovers, menus, and command palettes fit small viewports.
- Avoid fixed heights that clip dynamic content or localization.
