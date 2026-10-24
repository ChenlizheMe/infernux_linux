# 0.2.16 — Infernux 0.4.3-v5 embedded host shutdown

- Rebuild from frozen engine commit `3b54b810a8dec25246bd764104a979e92f08b7de`.
- Preserve the embedded host's native SIGINT handler and complete normal Player cleanup.
- Retain native scene unloading before asset catalog release, the engine requirement `>=0.4.3`, and the exact matching precompiled Player release.

# 0.2.15 — Infernux 0.4.3-v5 Player shutdown fix

- Rebuild from frozen engine commit `de7cc8c8b0ecbfbb7afd8553f256a1fa236f0aaa`.
- Unload native scenes before releasing asset catalogs so component shutdown retains font and other asset references.
- Keep the package engine requirement `>=0.4.3` and exact matching precompiled Player release.

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
