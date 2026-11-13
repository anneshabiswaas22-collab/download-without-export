# Understanding 3D file types

**The file extension does not tell you whether you have the editable scene you want.** Geometry type, UVs, materials, rig and object separation must be inspected independently.

| Type | Typical contents | Edit Mode in Blender? | Typical next work |
|---|---|---|---|
| `.spz` | Compressed Gaussian splat scene | **No polygon Edit Mode for the splats themselves** | Compatible importer/renderer, or lossy research reconstruction to mesh |
| `.ply` | Can be point cloud, Gaussian splats or polygon mesh | **Only when actual polygon faces exist** | Inspect header/elements and downstream geometry |
| `.glb` | Binary glTF; mesh/material/animation possible | Yes **if it contains meshes** | Verify geometry, images, materials, skeleton, independent objects |
| `.gltf` | JSON scene description with external/embedded buffers | Same as GLB when meshes present | Collect all referenced buffers/textures |
| `.fbx` | Scene/object/rig/animations possible | Yes for included polygon mesh(es) | Confirm external texture references, armature, compatibility |
| `.obj` | Polygon model, optional MTL/texture files | Yes for polygon faces | Materials, UVs and rig (OBJ has no general rig workflow) |
| `.blend` | Blender project with objects, add-ons, textures, caches | **Depends on included object types** | Inspect file dependencies and representation; do not trust unknown embedded code |

## Three independent acceptance dimensions

1. **Representation:** splat/point cloud versus actual vertices/edges/faces.
2. **Scene structure:** one merged triangle mesh versus objects that can be selected and moved independently.
3. **Animation readiness:** armature, skin weights, blendshapes, controllers, imported actions and facial controls.

A successful conversion from `.spz` to a Blender project may preserve an appearance for rendering but does not automatically produce a clean, subdividable room, a walking character, movable sofa or editable materials.

### A better requirement for an editable room

Ask for a **textured polygon mesh GLB/FBX/OBJ** where accessible, then check polygon counts, UV maps, material images, separate object hierarchy and topology. If you need doors that open or props that move, reconstruct/re-model the critical objects and manually refine or retopologize. Single-view generation guesses hidden surfaces.

### If only a splat is available

You can use a compatible Gaussian-splat viewer/Blender integration to render backgrounds, add separate rigged character assets, and composite. Automatic mesh reconstruction or tools such as [SuGaR](https://github.com/Anttwo/SuGaR) are **experimental/approximate**: expect geometry artifacts, disconnected surfaces and missing semantic labels. Never describe a splat as editable meshes merely because it lives in a `.blend`.

### Validation

`python scripts/inspect_asset.py filename` performs a **lightweight header and hash inspection**, not a full geometry/material/rig validation. A layered acceptance test should include provider-specific structural parsers and a Blender inspection with captured logs/versions.
