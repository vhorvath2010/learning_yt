import yt

# Load the dataset.
ds = yt.load("data/GasSloshing/sloshing_nomag2_hdf5_plt_cnt_0150")

print("list of gas fields: ", dir(ds.fields.gas))

#for normal in "xyz":
    # Create gas density slices in all three axes.
    #yt.SlicePlot(ds, normal, ("gas", "density"), width=(800.0, "kpc")).save()

    # Display non-weighted line integral of gas density
    #yt.ProjectionPlot(ds, normal, ("gas", "density")).save()

    # Weighted line integral of gas density
    #yt.ProjectionPlot(ds, normal, ("gas", "density"), weight_field=("gas", "density")).save()

# Create a phase plot of the temperature/density pairs by cell mass
# phase_plot = yt.PhasePlot(ds, ("gas", "density"), ("gas", "temperature"), ("gas", "cell_mass"), weight_field=None)
# phase_plot.set_unit(("gas", "cell_mass"), "Msun")
# phase_plot.save()

# Create a line plot of gas temperature vs velocity_magnitude
# line_plot = yt.LinePlot(ds, [("gas", "temperature"), ("gas", "velocity_magnitude")], (-0.1, -0.1, -0.1), (0.1, 0.1, 0.1), 1000)
# line_plot.save()

# Create a probability distrubtion function of the earlier tempreature density phase plots
pdf_plot = yt.PhasePlot(ds, ("gas", "density"), ("gas", "temperature"), ("gas", "cell_mass"), weight_field=None, fractional=True)
pdf_plot.set_unit(("gas", "cell_mass"), "Msun")
pdf_plot.save()