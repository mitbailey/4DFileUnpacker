import h5py as h5

def h5dump(path, group='/'):
    """
    Print an HDF5 format file's internal structure including groups and object attributes.
    
    Group: you can give a specific group, defaults to the root group.
    """
    with h5.File(path,'r') as f:
         _descend_obj(f[group])

def _descend_obj(obj, sep='\t'):
    """
    Iterate through groups in a HDF5 file and prints the groups and datasets names and datasets attributes
    """
    if type(obj) in [h5._hl.group.Group,h5._hl.files.File]:
        for key in obj.keys():
            print (sep,'-',key,':',obj[key],obj[key].attrs.keys())
            _descend_obj(obj[key],sep=sep+'\t')
    elif type(obj)==h5._hl.dataset.Dataset:
        for key in obj.attrs.keys():
            print (sep+'\t','-',key,':',obj.attrs[key])

def unpack(path):
    if not path.endswith('.4d'):
        print('Error: file must be a .4d file')
        exit(1)

    surfaces = {}
    metadata = {}

    hfdata = h5.File(path, 'r')

    surfaces['FringeAmplitude'] = hfdata['Measurement']['FringeAmplitude']['Data']
    surfaces['Intensity'] = hfdata['Measurement']['Intensity']['Data']
    surfaces['Modulation'] = hfdata['Measurement']['Modulation']['Data']
    surfaces['SurfaceInWaves'] = hfdata['Measurement']['SurfaceInWaves']['Data']
    surfaces['SurfaceInNanometers'] = hfdata['Measurement']['SurfaceInWaves']['Data'] * hfdata['Measurement'].attrs['WavelengthInNanometers']
    surfaces['UnprocessedUnwrappedPhase'] = hfdata['Measurement']['UnprocessedUnwrappedPhase']['Data']

    metadata['WavelengthInNanometers'] = hfdata['Measurement'].attrs['WavelengthInNanometers']
    metadata['ExposureTimeInMilliseconds'] = hfdata['Measurement']['GlobalSettings']['ACA2440'].attrs['ExposureTimeInMilliseconds']
    metadata['Timestamp'] = hfdata['Measurement']['Metadata'].attrs['Timestamp']
    metadata['MeasurementNumber'] = hfdata['Measurement']['Metadata'].attrs['MeasurementNumber']
    metadata['NumberOfAveragedMeasurements'] = hfdata['Measurement']['GlobalSettings']['BurstSettings'].attrs['NumberOfAveragedMeasurements']

    return surfaces, metadata