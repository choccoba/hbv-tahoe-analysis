import scanpy as sc
import pandas as pd

# Load the analysis result
adata = sc.read_h5ad("analysis_results/hbv_tahoe_analysis_20260112_121919.h5ad")

print("=" * 60)
print("HBV Tahoe Analysis Result Summary")
print("=" * 60)
print(f"Total cells: {adata.n_obs:,}")
print(f"Total genes: {adata.n_vars:,}")
print()

print("obs (cell metadata) columns:")
print(adata.obs.columns.tolist())
print()

print("var (gene metadata) columns:")
print(adata.var.columns.tolist())
print()

print("obsm (embedding) keys:")
print(list(adata.obsm.keys()))
print()

print("uns (misc info) keys:")
print(list(adata.uns.keys()))
print()

# Show sample distribution
if "sample" in adata.obs.columns:
    print("=" * 60)
    print("Sample Distribution:")
    print(adata.obs["sample"].value_counts())
    print()

# Show HBV status if available
if "HBV_status" in adata.obs.columns:
    print("=" * 60)
    print("HBV Status Distribution:")
    print(adata.obs["HBV_status"].value_counts())
    print()

# Show cell types if available
if "cell_type" in adata.obs.columns:
    print("=" * 60)
    print("Cell Type Distribution:")
    print(adata.obs["cell_type"].value_counts())
    print()
elif "leiden" in adata.obs.columns:
    print("=" * 60)
    print("Leiden Cluster Distribution:")
    print(adata.obs["leiden"].value_counts())
    print()

# Show Tahoe embedding info
if "X_tahoe" in adata.obsm:
    print("=" * 60)
    print(f"Tahoe Embedding Shape: {adata.obsm['X_tahoe'].shape}")
    print()

# Show first few cells
print("=" * 60)
print("First 5 cells metadata:")
print(adata.obs.head())
