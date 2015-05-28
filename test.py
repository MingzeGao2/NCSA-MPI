def read_and_plot(file_name):
        import matplotlib.pyplot as plt
        import matplotlib as ml
        import matplotlib.cm as cm
        dataset_check = gdal.Open(file_name, GA_ReadOnly)
        band_check = dataset_check.GetRasterBand(1)    
        cols_check = dataset_check.RasterXSize
        rows_check = dataset_check.RasterYSize
        data_check = band_check.ReadAsArray(0,0, cols_check, rows_check)
        fig = plt.figure()
        plt.imshow(data_check)
        plt.colorbar(orientation='vertical')
        plt.show()
