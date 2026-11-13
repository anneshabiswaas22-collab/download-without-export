# Blender, textures and animation workflows

## A. Actual polygon mesh received (GLB/FBX/OBJ)

1. Record original file hash and rights; keep source files separate from edits.
2. In Blender, **File → Import** the appropriate format. Ensure associated `.mtl`, image textures or glTF external buffers are present as needed.
3. Inspect the Outliner: MESH objects, armatures, cameras, collection hierarchy, and whether the scene is a single fused object.
4. Inspect Geometry/UV Editing/Materials and texture images; verify missing links and normals.
5. Confirm mesh really supports **Edit Mode** and UV/material editing, and identify regions requiring retopology.
6. For characters, inspect rig, weights, root transforms, pose controls, actions, face/lipsync controls. Retarget supplied animations (e.g. Mixamo) only after checking compatibility.
7. Save an editable `.blend`; keep attribution and original assets in a manifest.

Do not treat a single GLB as guaranteed animation-ready or object-separated.

## B. Only an SPZ Gaussian splat received

1. Preserve SPZ exactly and hash it; do **not** rename the extension to GLB/FBX.
2. Confirm Blender version and availability of a **compatible Gaussian-splat import/render workflow**. Previous project messages were inconsistent about native Blender 5.3 import for the target scene: treat it as **unverified for this asset** until you test it.
3. If the splat renders in Blender or externally, use it as a background and place separate editable character/prop meshes in matching coordinates.
4. Do not expect to enter polygon Edit Mode and reposition individual furniture inside a splat.
5. If a true mesh is mandatory, first check for a legitimately accessible **HQ textured GLB**; otherwise rebuild or reconstruct geometry using an independently authorized pipeline.

## C. Script → video (future milestone, not yet built)

Inputs: a rigged character (`.blend`/`.fbx`/`.glb` with legal assets), environment (mesh or compatible splat), script, duration/timing, voice/dialogue and optional subtitle/audio files.

Proposed sequence:
1. Preflight supported file versions, rig actions, textures and coordinate units.
2. Import set and characters; choose compositing strategy for splat vs meshes.
3. Define shot list: durations, camera moves, actor blocking, gestures and dialogue.
4. Apply existing body actions and retarget (test foot contact and deformation); facial expressions/lip sync only if supported.
5. Add lighting/camera, render a **10-second, 16:9 technical preview** (e.g. 720p/1080p) to verify scene before a long movie.
6. Run approved rendering infrastructure; mux video/audio/subtitles to MP4 as required; preserve final `.blend`, logs and licenses.

## D. Colab/Kaggle GPU notes

- Notebook GPUs are **not** guaranteed; quotas, session duration, VRAM and device support change.
- Do not assume installed Blender has a working GPU render engine, that SPZ supports a specific renderer, or that a video can render end-to-end on a free tier.
- Keep assets in legitimate user-controlled storage; do not hardcode tokens or mount secrets into notebooks.
- Start with a tiny import/1-frame render/small MP4 smoke test, record `blender --version`, GPU/driver details, peak VRAM, duration and output size.
- For long output, split into individually renderable shots or frames with checkpoints and concatenate only after validation.
- Offline local Blender CPU fallback should be documented for reproducibility, though slow rendering is expected.

## First production tests to implement

- Import each verified format and capture object count, mesh vertex/faces, materials, images, armatures, dependency paths.
- Render one still frame with a checker camera and record success/failure.
- Produce a minimal MP4 from a user-owned rig and open-license sample scene before attempting larger narrative animations.
