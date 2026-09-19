# Stack Routing

Use this reference only after resolving the UX outcome. Framework rules do not replace semantic UI requirements.

## React

Prefer semantic HTML, local state, derived state, and measured optimization. Do not add memoization everywhere. Keep reusable primitives small and composable. Test focus behavior after portals, dialogs, menus, and conditional rendering.

## Next.js

Keep client component boundaries narrow. Prefer server rendering where interaction does not require client state. Stream meaningful regions, not arbitrary fragments. Use framework image and font primitives where they improve performance. Preserve accessible navigation and focus after route transitions.

## Vue

Use computed state for derivation, focused components, semantic templates, and restrained watchers. Keep transitions compatible with reduced motion and ensure conditional UI retains sensible focus.

## Svelte / SvelteKit

Use reactive primitives for real dependencies, not as a substitute for data modeling. Keep rendered DOM semantic and accessible. Avoid effect chains for derived state.

## Astro

Ship static HTML by default. Hydrate only interactive islands. Ensure primary content and navigation remain useful without JavaScript where practical.

## HTML + Tailwind

Start from semantic HTML. Centralize recurring values through design tokens or Tailwind theme configuration. Avoid unreadable one-off utility duplication. Verify focus, dark mode, responsive overflow, and long text after styling.

## shadcn/ui

Reuse accessible primitives and preserve underlying Radix semantics. Customize through tokens and variants rather than forking every component. Recheck focus rings, disabled states, invalid fields, dialog focus management, menu keyboard behavior, and contrast after visual customization.

## Angular

Use current framework primitives appropriate to the project. Keep templates semantic, state ownership explicit, and change detection predictable. Do not hide accessibility semantics inside generic clickable containers.

## Nuxt / Nuxt UI

Use server rendering and data composables intentionally. Keep client-only regions narrow. Reuse system components and tokens before custom variants. Verify route transitions, focus, overflow, and loading states.

## React Native

Use platform semantic props, safe areas, performant list primitives, and platform-specific feedback. Test font scaling, screen-reader order, touch targets, keyboard avoidance, and reduced motion. Do not transplant desktop interaction patterns.

## Flutter

Use ThemeData and semantic tokens consistently. Prefer adaptive or platform-appropriate controls when user expectations differ. Avoid hard-coded text heights. Test semantics, text scaling, keyboard navigation where relevant, and list performance.

## SwiftUI

Prefer native controls, semantic styles, Dynamic Type, accessibility labels/values only where needed, safe areas, and Apple navigation conventions. Avoid fixed font sizes and frames that clip enlarged text.

## Jetpack Compose

Use Material semantics and theming, state hoisting at the right owner, lazy layouts for large collections, and meaningful content descriptions. Test font scaling, TalkBack order, focus, and gesture alternatives.

## Three.js

Treat 3D as enhancement unless the product task fundamentally requires it. Keep critical navigation and form actions outside the canvas. Cap pixel ratio, manage asset loading, reduce motion, handle WebGL failure, and provide accessible equivalents for important information.

## Laravel / Blade / Livewire

Preserve server-rendered semantics and progressive enhancement. Return validation errors adjacent to fields, retain inputs, and avoid replacing standard form behavior with inaccessible custom controls.

## JavaFX

Use native controls and CSS tokens. Keep keyboard focus, selection, density, and virtualized tables explicit. Avoid custom canvas controls for standard inputs unless there is a compelling requirement.

## WPF

Centralize styles/resources, preserve automation properties, use virtualization for large collections, and make keyboard/focus order intentional. Test high DPI and Windows text scaling.

## WinUI 3

Follow Fluent patterns and system backdrops only where they improve hierarchy. Use access keys, keyboard navigation, automation properties, and responsive window layouts.

## Avalonia

Use theme resources and flexible layout. Test keyboard/focus behavior and platform differences rather than assuming identical WPF behavior across targets.

## Uno Platform

Keep shared semantic components and tokens, then adapt platform-specific navigation/input behavior. Verify focus, scaling, and safe-area behavior on actual target platforms.

## UWP

Treat as legacy maintenance. Preserve accessibility and established platform behavior. For new strategic development, recommend a migration path rather than extending legacy architecture without reason.

## Version-sensitive guidance

The bundled stack notes are principles, not a current-version database. When implementation depends on a library version, API, browser behavior, or framework feature that can change, inspect project manifests and current official documentation before prescribing exact APIs.
