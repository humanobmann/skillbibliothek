# React and Next.js Checks

## Client boundaries

Use `"use client"` only when required by state, effects, event handlers, browser APIs, client-only libraries, or interactive component contracts. Keep the boundary as low in the tree as practical.

## Data and rendering

- Prefer server-side data access where the framework supports it and the interaction does not require client ownership.
- Avoid mirroring server data into client state without a reason.
- Avoid unnecessary waterfalls and repeated requests.
- Preserve streaming and Suspense opportunities where appropriate.
- Keep expensive client libraries out of the initial bundle when possible.

## Component design

- Keep UI primitives focused and reusable.
- Prefer composition over giant prop-driven components.
- Avoid wrappers that merely rename shadcn APIs without providing real domain value.
- Keep domain components separate from generic UI primitives.

## Next.js specifics

- Respect App Router versus Pages Router conventions.
- Use framework-native metadata and navigation APIs.
- Do not add client navigation hacks where `Link` or router APIs suffice.
- Avoid browser-only code during server rendering.
- Verify hydration when output depends on locale, time, random values, theme, viewport, or browser storage.

## Performance review

Check for:

- Excessive client JavaScript.
- Unnecessary rerenders from unstable props or context scope.
- Large icon or chart imports.
- Expensive tables rendered entirely on the client without need.
- Images without appropriate sizing or framework optimization.
- Layout shift from late-loading content.
- Repeated component-local fetches that should be shared.
