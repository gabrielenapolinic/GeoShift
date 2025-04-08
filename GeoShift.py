# %%
import geopandas as gpd
import os

# %% [markdown]
# ## 1. Verify Input Shapefile
# Check file existence and CRS

# %%
input_path = "/path/to/your_data.geojson"

# Check if file exists
if not os.path.exists(input_path):
    raise FileNotFoundError(f"Input shapefile not found at: {input_path}")

gdf = gpd.read_file(input_path)

# Force set CRS if missing (UTM zone 33N)
if gdf.crs is None:
    print("Warning: Input CRS not defined! Forcing CRS to EPSG:32633")
    gdf = gdf.set_crs(epsg=32633)

print("Original CRS:", gdf.crs)

# %% [markdown]
# ## 2. Perform Reprojection

# %%
try:
    gdf_wgs84 = gdf.to_crs(epsg=4326)
    print("New CRS:", gdf_wgs84.crs)
except Exception as e:
    print(f"Reprojection failed: {str(e)}")
    raise

# %% [markdown]
# ## 3. Save Reprojected Shapefile

# %%
output_path = "/path/to/output_4326.shp"

try:
    gdf_wgs84.to_file(output_path)
    print(f"File saved successfully to: {output_path}")
except Exception as e:
    print(f"Error saving file: {str(e)}")
    raise

# %% [markdown]
# ## 4. Verify Output

# %%
# Final verification
output_gdf = gpd.read_file(output_path)
print("Output CRS verified:", output_gdf.crs)
print("First 3 coordinates example:")
print(output_gdf.head(3).geometry.to_wkt())
print("Reprojection completed successfully!")
