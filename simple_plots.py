import yt

# Load the dataset.
ds = yt.load("data/GasSloshing/sloshing_nomag2_hdf5_plt_cnt_0150")

# Create gas density slices in all three axes.
yt.SlicePlot(ds, "x", ("gas", "density"), width=(800.0, "kpc")).save()
yt.SlicePlot(ds, "y", ("gas", "density"), width=(800.0, "kpc")).save()
yt.SlicePlot(ds, "z", ("gas", "density"), width=(800.0, "kpc")).save()

# Display non-weighted line integral of gas density
yt.ProjectionPlot(ds, "x", ("gas", "density")).save()
yt.ProjectionPlot(ds, "y", ("gas", "density")).save()
yt.ProjectionPlot(ds, "z", ("gas", "density")).save()

# Weighted line integral of gas density
yt.ProjectionPlot(ds, "x", ("gas", "density"), weight_field=("gas", "density")).save()
yt.ProjectionPlot(ds, "y", ("gas", "density"), weight_field=("gas", "density")).save()
yt.ProjectionPlot(ds, "z", ("gas", "density"), weight_field=("gas", "density")).save()
