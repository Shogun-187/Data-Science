def Corr_Matrix(df):

  """ A function that plots a correlation matrix."""

  # Build a canvas:
  f = plt.figure(figsize=(13, 8))

  # Plot data:
  plt.matshow(df.corr(), fignum=f.number)

  # Format plot:
  plt.xticks(range(df.shape[1]), df.columns, fontsize=12, rotation=45)
  plt.yticks(range(df.shape[1]), df.columns, fontsize=12)
  cb = plt.colorbar()
  cb.ax.tick_params(labelsize=14)
  plt.title('Correlation Matrix', fontsize=21, pad=90)
  plt.show()
