# 0.2.14 — Infernux 0.4.3-v5

- Rebuild the complete Linux Player payload against Infernux 0.4.3-v5.
- Build from frozen engine commit `f683bfa678eb680748c20be91badb9fe668ec553`.
- Keep the package engine requirement `>=0.4.3`; precompiled Players require the exact matching engine release.

# 0.2.10 — Infernux 0.4.3

- Rebuild against the final asset-error handling changes.

# 0.2.9 — Infernux 0.4.3

- Rebuild the complete Player payload against the final 0.4.3 engine source, including asset import-failure publication.
- Keep the engine requirement >=0.4.3.

# 0.2.8 — Infernux 0.4.3

- Rebuild the complete Linux Player payload with Infernux 0.4.3.
- Include current asset catalogs, startup preparation, UI batching and animation fixes.
- Keep the package engine requirement >=0.4.3; native payloads require the exact engine release.

- Derive the runtime version from the package/engine identity instead of hard-coding a previous release.

# 0.2.6 — Infernux 0.4.2 revision 2

- Publish the exporter and precompiled Player payload built with Infernux 0.4.2-v2.
- Preserve the exact engine-release check for precompiled runtimes.
- Keep the package engine requirement >=0.4.2.
- Publish new immutable artifacts; earlier package releases remain unchanged.
