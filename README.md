# MotionVault · Infographic & 3D Motion Graphics Library

> ⚠️ **Upload in progress:** This repository currently contains documentation and initial configuration only. The full 23-file source bundle is available in the ChatGPT conversation as `MotionVault-Remotion-2D-3D.zip`. The React/Remotion source files have **not** been fully uploaded to GitHub yet; `npm run build` will not work until they are added. No deployment or MP4 rendering has been verified.

A reusable **Vietnamese** Remotion video library with a searchable React web app, editing fields, a live embedded player and editable 2D + genuine 3D animations for short-form videos.

## Included in v0.2.0

- **11 native 2D Remotion templates**: Bar Chart, Donut, Counter, Comparison, Process, Kinetic Title, Progress, KPI Grid, Price, Checklist, Timeline.
- **5 native WebGL 3D Remotion templates**: Tower Chart 3D, Orbit KPI, Cement Package Turntable 360°, Isometric Construction and Globe Network.
- Search, category filters, favorites (saved in your browser), editable titles/data/colors, live Player and an external source registry.
- Each video is 1080 × 1920, 30 fps (vertical TikTok format).
- All original project code is authored for this project. **No third-party template code was copied into this repo.**

## Requirements

- Node.js 20+ and npm
- Google Chrome / Chromium or Microsoft Edge with WebGL enabled for 3D previews
- Internet access for initial npm install (not possible in the authoring environment)

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:5173 . Click a card, then use the right-hand editing panel. Click play in the preview to inspect an animation. For technical composition editing run `npm run studio` (Remotion Studio).

## Render an MP4

Select a composition and customize its text/data in the gallery. Click **Tải cấu hình xuất MP4**. It downloads `render-props.json`. Move that file to the project root. Click **Sao chép lệnh render**, paste into a terminal in the project root. Or use:

```bash
mkdir -p out
npx remotion render src/remotion/index.ts TowerChart3D out/TowerChart3D.mp4 --props=render-props.json --gl=angle
```

On Windows PowerShell, create output directory with `New-Item -ItemType Directory -Force out` if it does not already exist. Alternatively render any template with its default props:

```bash
npx remotion render src/remotion/index.ts BarChart out/BarChart.mp4
```

**Important:** The gallery is a live preview and JSON export tool, **not** a browser-based MP4 renderer. MP4 encoding is handled by the Remotion CLI and requires a working local install. `--gl=angle` requests an appropriate Chromium renderer for WebGL; rendering may require graphics drivers and Chrome dependencies, depending on OS.

## All composition IDs

```text
BarChart, DonutChart, NumberCounter, Comparison, Process,
KineticTitle, Progress, StatGrid, PriceTag, Checklist, Timeline,
TowerChart3D, OrbitKPI3D, ProductTurntable3D, Construction3D, GlobeNetwork3D
```

## Folder structure

```text
src/
  main.tsx                 # Search, filters, favorites, editing, preview UI
  styles/app.css           # Responsive interface and card artwork
  catalog/types.ts        # Editable props + template metadata types
  catalog/templates.ts    # 16 built-in templates + unimported source registry
  remotion/compositions.tsx   # Native 2D scenes
  remotion/three.tsx          # Native THREE.js scenes
  remotion/Root.tsx           # Remotion composition registration
  remotion/index.ts          # Remotion Studio entry point
```

## Where to add templates

1. Implement `React.FC<TemplateProps>` in `src/remotion/compositions.tsx` or `src/remotion/three.tsx`.
2. Import and register it in `src/catalog/templates.ts` using `make()`.
3. Gallery and Studio will both discover it from the registry automatically.
4. Check license and compatibility before importing external sources, and preserve original copyright notices where applicable.

## External source catalog (reference only, no copied code)

- https://github.com/lifeprompt-team/remotion-scenes
- https://github.com/reactvideoeditor/remotion-templates
- https://github.com/RenderComp/free-remotion-templates
- https://github.com/Thedurancode/locomotion-templates

Licensing statements in metadata are provisional until the individual LICENSE files and any third-party asset licenses are checked when importing code.

## Limitations / status

- Initial implementation has been statically reviewed but **not dependency-installed, typechecked or MP4-render-tested** in the current sandbox because npm registry is unreachable (`EAI_AGAIN`). Run `npm install && npm run build` on a network-connected machine and resolve any package-version issues before production use.
- 3D visuals are **procedural models**, not scans or branded product models. Product artwork is explicitly illustrative.
- UI has no server, authentication or real cloud rendering.
- No GitHub repository has been created or pushed by this build. To publish, create a new repository on your connected GitHub account, then run `git init`, `git add .`, `git commit -m "Initial MotionVault"`, set `origin` and `git push -u origin main`.

### License

Original project code (excluding separately linked resources): MIT. See LICENSE. Remotion and dependencies retain their own terms — verify the Remotion commercial licensing applicable to your business at https://www.remotion.dev/license .

## Offline UI demo

Open `preview-offline.html` directly in a browser. This dependency-free demonstration shows the catalog layout, search, filters and a CSS-simulated scene. **It is NOT a WebGL/Remotion Player and cannot generate real video.** The working Remotion frontend is `src/main.tsx` and requires `npm install`.

## Publish the gallery using GitHub Pages

This repository includes `.github/workflows/pages.yml`, which builds and deploys the Vite gallery when pushed to the `main` branch. First create a repo in GitHub and enable **Settings → Pages → Build and deployment → GitHub Actions**. The workflow handles a repository subpath with `VITE_BASE_PATH`. Your browser and hardware must support WebGL for the 3D player to work. The Pages site only provides previews; encoding MP4 still runs locally through the CLI.

## Shortcut on Windows

After extracting the zip, double-click `START-WINDOWS.cmd` to run npm installation (if needed) and start the UI, then open http://localhost:5173 . See `PUBLISH-GITHUB.md` for beginner-friendly GitHub instructions.