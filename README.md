# GeoShift
A Python-based geospatial troubleshooting tool that ensures reliable coordinate reference system (CRS) conversions when traditional GIS software (QGIS, ArcGIS) fails.

## 🔍 Problem Statement
When working with geospatial data in QGIS/ArcGIS/ArcMap, you might encounter:
- Silent CRS assignment failures
- Corrupted .prj files
- Coordinate mismatches after reprojection
- CRS null errors in geoprocessing

This Jupyter Notebook provides a **programmatic solution** to validate and reproject geospatial files (Shapefile/GeoJSON/GeoPackage) when traditional GIS GUI tools fail.

## ✨ Features
- ✅ Automatic CRS validation
- � Auto-fix for missing CRS (UTM 33N fallback)
- 📂 Supports multiple formats: SHP, GeoJSON, GPKG
- 🛡️ Comprehensive error handling
- 📊 Coordinate verification pre/post conversion

## 📦 Prerequisites
- Python 3.8+
- [GeoPandas](https://geopandas.org/en/stable/getting_started/install.html)
- [Jupyter Notebook](https://jupyter.org/install)
