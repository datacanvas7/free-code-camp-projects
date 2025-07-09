from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Test categorical plot
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')
print("Categorical plot saved as catplot.png")

# Test heat map
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')
print("Heat map saved as heatmap.png")