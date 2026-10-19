# MotionVault external sources research — 2026-10-19

This is a **research registry only**: 19 indexed external sources in `src/catalog/external-sources.json`. They are NOT installed template components. The complete local ZIP retains 11 authored 2D and 5 authored procedural 3D scenes. Do not equate upstream template counts with ready-to-render MotionVault scenes.

## Priority 1
- [Remotion Scenes](https://github.com/lifeprompt-team/remotion-scenes) — infographic scenes and typography
- [React Video Editor](https://github.com/reactvideoeditor/remotion-templates) — charts/data and other React video templates
- [RenderComp](https://github.com/RenderComp/free-remotion-templates) — stats, counters, marketing
- [Onda](https://github.com/degueba/onda) — components and transitions
- [Remocn](https://github.com/Remocn/remocn) — animated text and motion UI
- [Remotion Bits](https://github.com/av/remotion-bits) — effect building blocks
- [Remotion Three starter](https://github.com/remotion-dev/template-three) — R3F / ThreeCanvas
- [Poly Haven](https://polyhaven.com/) — CC0 models, textures, HDRIs, inspect each downloaded asset
- [Drei](https://github.com/pmndrs/drei) — Three.js helpers

## Additional research
SwiftClip, Locomotion, RemotionUI, Khronos glTF Sample Assets, Adobe Mixamo, D3, Recharts, official Remotion resources, Remotion 3D best practices and third-party template registries.

## Import rules
1. Before reuse, verify each upstream LICENSE, asset license, attribution requirement and version.
2. Create an import branch and record upstream URL/tag/commit SHA.
3. Import one scene per iteration, map props to `TemplateProps`, test preview and render.
4. For 3D, synchronize movement to `useCurrentFrame` rather than wall-clock animation.
5. Keep original notices. Don't bulk copy model libraries or redistribute Mixamo assets.
6. Do not push or merge new code without reviewing changes.

## Caution
The GitHub repository currently contains the research catalog and starter files, but **not the entire local 16-scene project**. For a complete runnable project, sync the downloadable ZIP, inspect diffs, install npm dependencies, and test a render. No third-party template code was bundled by this research pass.
