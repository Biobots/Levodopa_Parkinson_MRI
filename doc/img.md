## General Feature Extraction

不限于T1

### Novel nested patch-based feature extraction model for automated Parkinson’s Disease symptom classification using MRI images
1. 2022, Computer Methods and Programs in Biomedicine, 7.0
2. PD诊断，鉴别诊断
3. FLAIR
4. PHOG (分层方向梯度直方图) 提取梯度特征
5. **NCA, Chi2, mRMR, ReliefF**筛选特征
6. KNN, SVM分类
7. PHOG特征提取--特征筛选--分类预测--选择最优结果

### Multivariate radiomics models based on 18F-FDG hybrid PET/MRI for distinguishing between Parkinson’s disease and multiple system atrophy
1. 2020, European Journal of Nuclear Medicine and Molecular Imaging, 10.1
2. PD鉴别诊断
3. T1, T2, T2 FLAIR, SWI, PET
4. ROI: putamen, caudate nucleus
5. **PyRadiomics**
6. mRMR, LASSO (10-fold cv)

### Substantia Nigra Radiomics Feature Extraction of Parkinson’s Disease Based on Magnitude Images of Susceptibility-Weighted Imaging
1. 2021, Frontiers in Neuroscience, 
2. PD诊断
3. SWI (In SWI, the magnitude image can be acquired directly and has been an easy applicable diagnostic tool for nigral degeneration in PD)
4. 2D slices of the SN ROI
   1. Histogram features (n=42)
   2. Form factor features (n=15)
   3. GLCM features (n=154)
   4. Run length matrix features (n=180)
   5. Gray level size zone matrix (GLSZM) features (n=11)
5. 特征筛选: mRMR + LASSO -- 16 features
6. LASSO logistic, RF, svmLinear, svmRadial, KNN
   1. 100-fold leave group-out cross-validation (LGOCV)

### Feature selection and machine learning methods for optimal identification and prediction of subtypes in Parkinson’s disease
1. 2021, Computer Methods and Programs in Biomedicine, 7.0
2. PD亚型预测
3. SPECT
4. ...


## Structure Specific Feature Extraction

### 3D Textural, Morphological and Statistical Analysis of Voxel of Interests in 3T MRI Scans for the Detection of Parkinson’s Disease Using Artificial Neural Networks
1. 2020, Healthcare, 3.2
2. PD早期诊断 三分类
3. MPRAGE T1
4. Eight subcortical structures, namely, caudate nucleus, putamen, globus pallidus internus and externus (GPi & GPe), thalamus, STN, substantia nigra (SN), and red nucleus (RN)
5. **PyRadiomics**: Textural, morphological, statistical features of the eight subcortical structures
6. MLP, xgboost, RF, SVM分类
7. 5-fold cv
8. 107x16项特征--107项特征--相关系数排除42项特征，剩余65项--Recursive feature elimination筛选20项最佳特征

### Classification of PPMI MRI scans with voxel-based morphometry and machine learning to assist in the diagnosis of Parkinson’s disease
1. 2020, Computer Methods and Programs in Biomedicine, 7.0
2. PD诊断
3. Male/Female分别预测
4. 方法描述比较详细
5. T1 (PPMI)
6. VBM -- ROI -- Features
   1. First-order: average, central moments, entropy
   2. Second-order: GLCM based
7. PCA + Wrappers Feature Subset Selection
   1. Wrappers Feature Subset Selection: 根据相关性添加新特征，同时去除insignificant特征 (How to evaluate significance using complex models)
      1. Logistic, RF, NB, Bayes Network, KNN, MLP, SVM
8. 10-fold cv
   1. Logistic, RF, NB, Bayes Network, KNN, MLP, SVM
9. Regions with the most selected features
   1. 部分ROI特征没有用到
   2. 不同ROI对PD检测的贡献不同

### Unsupervised learning based feature extraction for differential diagnosis of neurodegenerative diseases: A case study on early-stage diagnosis of Parkinson disease
1. 2015, Journal of Neuroscience Methods,
2. PD鉴别诊断 PD, HC, SWEDD
3. T1
4. 分组
   1. Age-Unrelated Groups (AUG): 3 binary classification groups * 2 types of brain tissues (WM, GM)
   2. Age-Related Subgroups (ARS):  3 binary classification groups * 2 types of brain tissues * 6 age divisions - 2 types of brain tissues * 2 subgroups each for PD vs. SWEDD and SWEDD vs. HC above the age of 80 years
5. VIC (voxel intensity changes): 不同组间体素均值之差 (a vs. b)
6. WAT (Welch-Aspin test) 用于评估体素对各组的区分能力
7. KSOM (Kohonen self-organizing map): vector quantization and feature extraction from VIC image