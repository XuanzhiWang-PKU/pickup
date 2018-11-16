def pickUpBalls(motionProxy):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.0183661, [3, -1, 0], [3, 0.8, 0]], [-0.621311, [3, -0.8, 0], [3, 0.64, 0]], [-0.589098, [3, -0.64, 0], [3, 0.733333, 0]], [-0.664264, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.615176, [3, -0.0533333, -0.000876629], [3, 0.466667, 0.0076705]], [-0.607505, [3, -0.466667, 0], [3, 0.72, 0]], [-0.653526, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.653526, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.0383921, [3, -1.12, -0.046256], [3, 0.52, 0.021476]], [-0.016916, [3, -0.52, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.00916195, [3, -1, 0], [3, 0.8, 0]], [0.0137641, [3, -0.8, -6.50186e-09], [3, 0.64, 5.20149e-09]], [0.0137641, [3, -0.64, -5.20149e-09], [3, 0.733333, 5.96004e-09]], [0.0214341, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.0214341, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.0137641, [3, -0.466667, 0], [3, 0.72, 0]], [0.0137641, [3, -0.72, 0], [3, 0.0266667, 0]], [0.0137641, [3, -0.0266667, 0], [3, 1.12, 0]], [0.0214341, [3, -1.12, 0], [3, 0.52, 0]], [0.00916195, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-1.18944, [3, -1, 0], [3, 0.8, 0]], [-0.745566, [3, -0.8, -0.136457], [3, 0.64, 0.109166]], [-0.452572, [3, -0.64, -0.00133875], [3, 0.733333, 0.00153398]], [-0.451038, [3, -0.733333, -0.00153398], [3, 0.0533333, 0.000111562]], [-0.4403, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.563021, [3, -0.466667, 0.0446411], [3, 0.72, -0.0688749]], [-0.780848, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.780848, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.357464, [3, -1.12, -0.00991231], [3, 0.52, 0.00460214]], [-0.352862, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.023052, [3, -1, 0], [3, 0.8, 0]], [-0.0260359, [3, -0.8, 0], [3, 0.64, 0]], [0.16418, [3, -0.64, 0], [3, 0.733333, 0]], [0.153442, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.153442, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.158044, [3, -0.466667, 0], [3, 0.72, 0]], [0.158044, [3, -0.72, 0], [3, 0.0266667, 0]], [0.158044, [3, -0.0266667, 0], [3, 1.12, 0]], [0.0061779, [3, -1.12, 0.0099119], [3, 0.52, -0.00460196]], [0.00157595, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.987855, [3, -1, 0], [3, 0.8, 0]], [-0.300622, [3, -0.8, 0], [3, 0.64, 0]], [-0.309826, [3, -0.64, 0], [3, 0.733333, 0]], [-0.053648, [3, -0.733333, -0.0834167], [3, 0.0533333, 0.00606667]], [-0.0413761, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.338973, [3, -0.466667, 0.00298194], [3, 0.72, -0.00460071]], [-0.343573, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.343573, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.108872, [3, -1.12, 0], [3, 0.52, 0]], [-0.417486, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-1.37144, [3, -1, 0], [3, 0.8, 0]], [0.159494, [3, -0.8, 0], [3, 0.64, 0]], [0.159494, [3, -0.64, 0], [3, 0.733333, 0]], [0.191708, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.184038, [3, -0.0533333, 0.000786665], [3, 0.466667, -0.00688332]], [0.168698, [3, -0.466667, 0], [3, 0.72, 0]], [0.179436, [3, -0.72, 0], [3, 0.0266667, 0]], [0.179436, [3, -0.0266667, 0], [3, 1.12, 0]], [-1.18276, [3, -1.12, 0.0364746], [3, 0.52, -0.0169346]], [-1.19969, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.246, [3, -1, 0], [3, 0.8, 0]], [0, [3, -0.8, 0], [3, 0.64, 0]], [0.0164, [3, -0.64, -0.0164], [3, 0.733333, 0.0187916]], [0.2272, [3, -0.733333, -0.0385007], [3, 0.0533333, 0.00280005]], [0.23, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.0196, [3, -0.466667, 0.00233333], [3, 0.72, -0.0036]], [0.016, [3, -0.72, 0], [3, 0.0266667, 0]], [0.0336, [3, -0.0266667, -0.00209923], [3, 1.12, 0.0881675]], [0.2868, [3, -1.12, -0.0264289], [3, 0.52, 0.0122705]], [0.299071, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.569072, [3, -1, 0], [3, 0.8, 0]], [-0.943368, [3, -0.8, 0.164479], [3, 0.64, -0.131583]], [-1.45726, [3, -0.64, 0], [3, 0.733333, 0]], [-1.45726, [3, -0.733333, 0], [3, 0.0533333, 0]], [-1.45726, [3, -0.0533333, 0], [3, 0.466667, 0]], [-1.15353, [3, -0.466667, -0.120048], [3, 0.72, 0.185218]], [-0.54146, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.54146, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.455556, [3, -1.12, -0.0165195], [3, 0.52, 0.00766977]], [-0.447886, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.039926, [3, -1, 0], [3, 0.8, 0]], [-0.167164, [3, -0.8, 0.0553945], [3, 0.64, -0.0443156]], [-0.259204, [3, -0.64, 0.00401626], [3, 0.733333, -0.00460196]], [-0.263806, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.263806, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.197844, [3, -0.466667, -0.0277499], [3, 0.72, 0.0428141]], [-0.052114, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.052114, [3, -0.0266667, 0], [3, 1.12, 0]], [0.0061779, [3, -1.12, 0], [3, 0.52, 0]], [0.00310993, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.612024, [3, -1, 0], [3, 0.8, 0]], [-0.993989, [3, -0.8, 0.0948807], [3, 0.64, -0.0759046]], [-1.12438, [3, -0.64, 0.0120488], [3, 0.733333, -0.013806]], [-1.13819, [3, -0.733333, 0], [3, 0.0533333, 0]], [-1.13819, [3, -0.0533333, 0], [3, 0.466667, 0]], [-1.13665, [3, -0.466667, -0.00153345], [3, 0.72, 0.00236589]], [-1.12591, [3, -0.72, 0], [3, 0.0266667, 0]], [-1.12591, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.00609398, [3, -1.12, 0], [3, 0.52, 0]], [-0.00762796, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[2.10461, [3, -1, 0], [3, 0.8, 0]], [2.03711, [3, -0.8, 0], [3, 0.64, 0]], [2.11255, [3, -0.64, 0], [3, 0.733333, 0]], [2.10921, [3, -0.733333, 0], [3, 0.0533333, 0]], [2.10921, [3, -0.0533333, 0], [3, 0.466667, 0]], [2.11255, [3, -0.466667, 0], [3, 0.72, 0]], [2.00029, [3, -0.72, 0], [3, 0.0266667, 0]], [2.00029, [3, -0.0266667, 0], [3, 1.12, 0]], [0.699462, [3, -1.12, 0], [3, 0.52, 0]], [0.70253, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[1.42504, [3, -1, 0], [3, 0.8, 0]], [0.544529, [3, -0.8, 0], [3, 0.64, 0]], [0.54913, [3, -0.64, -0.00460121], [3, 0.733333, 0.00527222]], [0.605888, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.605888, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.470897, [3, -0.466667, 0.00298306], [3, 0.72, -0.00460244]], [0.466294, [3, -0.72, 0], [3, 0.0266667, 0]], [0.466294, [3, -0.0266667, 0], [3, 1.12, 0]], [1.55697, [3, -1.12, 0], [3, 0.52, 0]], [1.46334, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.288349, [3, -1, 0], [3, 0.8, 0]], [-0.15651, [3, -0.8, 0], [3, 0.64, 0]], [-0.00771189, [3, -0.64, 0], [3, 0.733333, 0]], [-0.2869, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.250084, [3, -0.0533333, -0.00886312], [3, 0.466667, 0.0775523]], [-0.0276539, [3, -0.466667, 0], [3, 0.72, 0]], [-0.0506639, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.0506639, [3, -0.0266667, 0], [3, 1.12, 0]], [0.283748, [3, -1.12, 0], [3, 0.52, 0]], [0.176053, [3, -0.52, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.00771189, [3, -1, 0], [3, 0.8, 0]], [-1.62301, [3, -0.8, 0], [3, 0.64, 0]], [-1.54018, [3, -0.64, 0], [3, 0.733333, 0]], [-1.65369, [3, -0.733333, 0], [3, 0.0533333, 0]], [-1.63835, [3, -0.0533333, 0], [3, 0.466667, 0]], [-1.79176, [3, -0.466667, 0], [3, 0.72, 0]], [-1.76107, [3, -0.72, 0], [3, 0.0266667, 0]], [-1.76107, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.22554, [3, -1.12, -0.422851], [3, 0.52, 0.196324]], [0.0964535, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-1.18421, [3, -1, 0], [3, 0.8, 0]], [-0.719404, [3, -0.8, -0.125561], [3, 0.64, 0.100449]], [-0.506178, [3, -0.64, 0], [3, 0.733333, 0]], [-0.515382, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.515382, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.615092, [3, -0.466667, 0.0412226], [3, 0.72, -0.0636006]], [-0.829852, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.829852, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.355846, [3, -1.12, 0], [3, 0.52, 0]], [-0.360449, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.046062, [3, -1, 0], [3, 0.8, 0]], [0.0445281, [3, -0.8, 0.00153397], [3, 0.64, -0.00122717]], [-0.118076, [3, -0.64, 0.0026775], [3, 0.733333, -0.00306797]], [-0.121144, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.121144, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.161028, [3, -0.466667, 0.00663584], [3, 0.72, -0.0102382]], [-0.171766, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.171766, [3, -0.0266667, 0], [3, 1.12, 0]], [0.0123138, [3, -1.12, 0], [3, 0.52, 0]], [0.00771189, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.0349066, [3, -1, 0], [3, 0.8, 0]], [0.297638, [3, -0.8, -0.083311], [3, 0.64, 0.0666488]], [0.484786, [3, -0.64, 0], [3, 0.733333, 0]], [0.19486, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.19486, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.200996, [3, -0.466667, -0.00361954], [3, 0.72, 0.00558443]], [0.222472, [3, -0.72, 0], [3, 0.0266667, 0]], [0.222472, [3, -0.0266667, 0], [3, 1.12, 0]], [0.04913, [3, -1.12, 0.0107405], [3, 0.52, -0.00498668]], [0.0441433, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[1.36522, [3, -1, 0], [3, 0.8, 0]], [0.469363, [3, -0.8, 0.0230109], [3, 0.64, -0.0184087]], [0.450954, [3, -0.64, 0.0184087], [3, 0.733333, -0.0210933]], [-0.0583339, [3, -0.733333, 0], [3, 0.0533333, 0]], [-0.0583339, [3, -0.0533333, 0], [3, 0.466667, 0]], [-0.0874801, [3, -0.466667, 0.00522824], [3, 0.72, -0.00806643]], [-0.0982179, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.0982179, [3, -0.0266667, 0], [3, 1.12, 0]], [1.24863, [3, -1.12, 0], [3, 0.52, 0]], [1.18682, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[0.16, [3, -1, 0], [3, 0.8, 0]], [0.9668, [3, -0.8, 0], [3, 0.64, 0]], [0.954, [3, -0.64, 0.0128], [3, 0.733333, -0.0146666]], [0.5712, [3, -0.733333, 0.241503], [3, 0.0533333, -0.0175638]], [0.1768, [3, -0.0533333, 0.00192], [3, 0.466667, -0.0168]], [0.16, [3, -0.466667, 0.00613483], [3, 0.72, -0.00946517]], [0.13, [3, -0.72, 0], [3, 0.0266667, 0]], [0.17, [3, -0.0266667, -0.000542636], [3, 1.12, 0.0227907]], [0.2, [3, -1.12, -0.0113821], [3, 0.52, 0.00528455]], [0.21, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.589097, [3, -1, 0], [3, 0.8, 0]], [-1.24105, [3, -0.8, 0.0479379], [3, 0.64, -0.0383503]], [-1.2794, [3, -0.64, 0], [3, 0.733333, 0]], [-1.27786, [3, -0.733333, 0], [3, 0.0533333, 0]], [-1.27786, [3, -0.0533333, 0], [3, 0.466667, 0]], [-1.11373, [3, -0.466667, -0.0727932], [3, 0.72, 0.11231]], [-0.722556, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.722556, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.454106, [3, -1.12, -1.86421e-06], [3, 0.52, 8.65527e-07]], [-0.454105, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.240796, [3, -1, 0], [3, 0.8, 0]], [-0.0429101, [3, -0.8, -0.0906196], [3, 0.64, 0.0724957]], [0.24855, [3, -0.64, 0], [3, 0.733333, 0]], [0.24855, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.24855, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.14884, [3, -0.466667, 0.037402], [3, 0.72, -0.057706]], [-0.0367741, [3, -0.72, 0], [3, 0.0266667, 0]], [-0.0367741, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.00916195, [3, -1.12, -0.00768249], [3, 0.52, 0.00356687]], [-0.00302602, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.612024, [3, -1, 0], [3, 0.8, 0]], [-0.993989, [3, -0.8, 0.0948807], [3, 0.64, -0.0759046]], [-1.12438, [3, -0.64, 0.0120488], [3, 0.733333, -0.013806]], [-1.13819, [3, -0.733333, 0], [3, 0.0533333, 0]], [-1.13819, [3, -0.0533333, 0], [3, 0.466667, 0]], [-1.13665, [3, -0.466667, -0.00153345], [3, 0.72, 0.00236589]], [-1.12591, [3, -0.72, 0], [3, 0.0266667, 0]], [-1.12591, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.00609398, [3, -1.12, 0], [3, 0.52, 0]], [-0.00762796, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[2.11255, [3, -1, 0], [3, 0.8, 0]], [2.10623, [3, -0.8, 0.00259118], [3, 0.64, -0.00207295]], [2.09855, [3, -0.64, 0], [3, 0.733333, 0]], [2.11236, [3, -0.733333, 0], [3, 0.0533333, 0]], [2.11236, [3, -0.0533333, 0], [3, 0.466667, 0]], [2.10316, [3, -0.466667, 0], [3, 0.72, 0]], [2.10316, [3, -0.72, 0], [3, 0.0266667, 0]], [2.10316, [3, -0.0266667, 0], [3, 1.12, 0]], [0.688808, [3, -1.12, 0], [3, 0.52, 0]], [0.690342, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[1.42206, [3, -1, 0], [3, 0.8, 0]], [0.710284, [3, -0.8, 0], [3, 0.64, 0]], [0.721022, [3, -0.64, 0], [3, 0.733333, 0]], [0.590632, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.590632, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.526205, [3, -0.466667, 0], [3, 0.72, 0]], [0.544613, [3, -0.72, 0], [3, 0.0266667, 0]], [0.544613, [3, -0.0266667, 0], [3, 1.12, 0]], [1.03089, [3, -1.12, -0.248748], [3, 0.52, 0.11549]], [1.63733, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.276162, [3, -1, 0], [3, 0.8, 0]], [-0.128898, [3, -0.8, -0.0596555], [3, 0.64, 0.0477244]], [0.0459781, [3, -0.64, -0.0629089], [3, 0.733333, 0.0720831]], [0.276078, [3, -0.733333, 0], [3, 0.0533333, 0]], [0.276078, [3, -0.0533333, 0], [3, 0.466667, 0]], [0.185572, [3, -0.466667, 0], [3, 0.72, 0]], [0.210117, [3, -0.72, 0], [3, 0.0266667, 0]], [0.210117, [3, -0.0266667, 0], [3, 1.12, 0]], [-0.250084, [3, -1.12, 0.010661], [3, 0.52, -0.00494975]], [-0.255034, [3, -0.52, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([3, 5.4, 7.32, 9.52, 9.68, 11.08, 13.24, 13.32, 16.68, 18.24])
    keys.append([[-0.0138481, [3, -1, 0], [3, 0.8, 0]], [1.33454, [3, -0.8, -0.011505], [3, 0.64, 0.00920402]], [1.34374, [3, -0.64, -0.00920402], [3, 0.733333, 0.0105463]], [1.72571, [3, -0.733333, 0], [3, 0.0533333, 0]], [1.72571, [3, -0.0533333, 0], [3, 0.466667, 0]], [1.73491, [3, -0.466667, -0.00542962], [3, 0.72, 0.00837713]], [1.76713, [3, -0.72, 0], [3, 0.0266667, 0]], [1.76713, [3, -0.0266667, 0], [3, 1.12, 0]], [0.133416, [3, -1.12, 0.0747885], [3, 0.52, -0.0347232]], [0.0986927, [3, -0.52, 0], [3, 0, 0]]])

    try:
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def throwBall(motionProxy):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.016916, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.6704, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.666632, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.667332, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.00916195, [3, -0.453333, 0], [3, 0.386667, 0]], [0.0106959, [3, -0.386667, 0], [3, 0.386667, 0]], [0, [3, -0.386667, 0], [3, 0.253333, 0]], [0.0137641, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.352862, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.351328, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.352862, [3, -0.386667, 0.00153415], [3, 0.253333, -0.00100513]], [-0.358998, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.00157595, [3, -0.453333, 0], [3, 0.386667, 0]], [0.00464392, [3, -0.386667, 0], [3, 0.386667, 0]], [0, [3, -0.386667, 0.00216249], [3, 0.253333, -0.00141681]], [-0.00609398, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-1.0078, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.96331, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.96331, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.946436, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-1.33922, [3, -0.453333, 0], [3, 0.386667, 0]], [-1.34229, [3, -0.386667, 0], [3, 0.386667, 0]], [-1.34229, [3, -0.386667, 0], [3, 0.253333, 0]], [-1.31468, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.2624, [3, -0.453333, 0], [3, 0.386667, 0]], [0.2488, [3, -0.386667, 0], [3, 0.386667, 0]], [0.2488, [3, -0.386667, 0], [3, 0.253333, 0]], [0.2676, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.447886, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.447886, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.447886, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.44942, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.00310993, [3, -0.453333, 0], [3, 0.386667, 0]], [4.19617e-05, [3, -0.386667, 4.19617e-05], [3, 0.386667, -4.19617e-05]], [0, [3, -0.386667, 0], [3, 0.253333, 0]], [0.0061779, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.00762796, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.00455999, [3, -0.386667, -0.00127133], [3, 0.386667, 0.00127133]], [0, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.00455999, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.70253, [3, -0.453333, 0], [3, 0.386667, 0]], [0.704064, [3, -0.386667, 0], [3, 0.386667, 0]], [0.70253, [3, -0.386667, 0.00123575], [3, 0.253333, -0.000809627]], [0.697928, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[1.38363, [3, -0.453333, 0], [3, 0.386667, 0]], [1.44192, [3, -0.386667, 0], [3, 0.386667, 0]], [1.44192, [3, -0.386667, 0], [3, 0.253333, 0]], [1.43578, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.294486, [3, -0.453333, 0], [3, 0.386667, 0]], [0.196309, [3, -0.386667, 0], [3, 0.386667, 0]], [0.196309, [3, -0.386667, 0], [3, 0.253333, 0]], [0.185572, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.0537319, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.023052, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.023052, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.0291879, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.360449, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.363515, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.360423, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.360448, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.00771189, [3, -0.453333, 0], [3, 0.386667, 0]], [0.00464392, [3, -0.386667, 0.00128532], [3, 0.386667, -0.00128532]], [0, [3, -0.386667, 0], [3, 0.253333, 0]], [0.00771189, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[1.00328, [3, -0.453333, 0], [3, 0.386667, 0]], [0.0349066, [3, -0.386667, 0], [3, 0.386667, 0]], [0.0349066, [3, -0.386667, 0], [3, 0.253333, 0]], [0.0353239, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[1.33914, [3, -0.453333, 0], [3, 0.386667, 0]], [1.51248, [3, -0.386667, 0], [3, 0.386667, 0]], [1.51248, [3, -0.386667, 0], [3, 0.253333, 0]], [1.49101, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.36, 2.52, 3.68, 4.44, 5.24, 6.08])
    keys.append([[0.2592, [3, -0.453333, 0], [3, 0.386667, 0]], [0.2356, [3, -0.386667, 0], [3, 0.386667, 0]], [0.9904, [3, -0.386667, 0], [3, 0.253333, 0]], [0.9816, [3, -0.253333, 0.00880003], [3, 0.266667, -0.00926319]], [0.52, [3, -0.266667, 0], [3, 0.28, 0]], [0.12, [3, -0.28, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.454105, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.449504, [3, -0.386667, 0], [3, 0.386667, 0]], [-0.454105, [3, -0.386667, 0.00216246], [3, 0.253333, -0.00141678]], [-0.460242, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.00302602, [3, -0.453333, 0], [3, 0.386667, 0]], [0.00617791, [3, -0.386667, 0], [3, 0.386667, 0]], [0, [3, -0.386667, 0.00154464], [3, 0.253333, -0.001012]], [-0.00149202, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.00762796, [3, -0.453333, 0], [3, 0.386667, 0]], [-0.00455999, [3, -0.386667, -0.00127133], [3, 0.386667, 0.00127133]], [0, [3, -0.386667, 0], [3, 0.253333, 0]], [-0.00455999, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.690342, [3, -0.453333, 0], [3, 0.386667, 0]], [0.690342, [3, -0.386667, 0], [3, 0.386667, 0]], [0.690342, [3, -0.386667, 0], [3, 0.253333, 0]], [0.687274, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[1.39598, [3, -0.453333, 0], [3, 0.386667, 0]], [0.0107799, [3, -0.386667, 0], [3, 0.386667, 0]], [0.0107799, [3, -0.386667, 0], [3, 0.253333, 0]], [0.098218, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[-0.27923, [3, -0.453333, 0], [3, 0.386667, 0]], [0.305223, [3, -0.386667, 0], [3, 0.386667, 0]], [0.305223, [3, -0.386667, 0], [3, 0.253333, 0]], [0.306758, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.36, 2.52, 3.68, 4.44])
    keys.append([[0.075124, [3, -0.453333, 0], [3, 0.386667, 0]], [0.0873961, [3, -0.386667, 0], [3, 0.386667, 0]], [0.0873961, [3, -0.386667, 0], [3, 0.253333, 0]], [-1.5049, [3, -0.253333, 0], [3, 0, 0]]])
    try:
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

