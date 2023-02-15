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
5. **PyRadiomics**: 没有说明具体特征
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
2. PD分型 clustering
3. SPECT
4. HMLS (hybrid machine learning system): predictor algorithms linked with faeture selector algorithms (FSAs)
   1. Most machine learning algorithms cannot accurately work with a high dimensional dataset
5. 2 stages:
   1. Clustering (subtype identification): After dimensionality reduction (PCA), cluster the data via the K-Means algorithm
   2. Classification (subtype prediction): FSAs to rank features, and each sequential combination selected by FSAs is assessed using multiple classifiers
6. Feature extraction algorithm (FEA): PCA
7. Clustering algorithm: KMA
8. Feature selection algorithms (FSAs): ILFS, ReliefA, LLBCFS, UMCFS, UDFSA, CSFA, FSASL, UFSOL, LASSO
9. Classification algorithms:


## Structure Specific Feature Extraction

### 3D Textural, Morphological and Statistical Analysis of Voxel of Interests in 3T MRI Scans for the Detection of Parkinson’s Disease Using Artificial Neural Networks
1. 2020, Healthcare, 3.2
2. PD早期诊断 三分类
3. MPRAGE T1 PPMI
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
4. 分组 (class)
   1. Age-Unrelated Groups (AUG): 3 binary classification groups * 2 types of brain tissues (WM, GM)
   2. Age-Related Subgroups (ARS):  3 binary classification groups * 2 types of brain tissues * 6 age divisions - 2 types of brain tissues * 2 subgroups each for PD vs. SWEDD and SWEDD vs. HC above the age of 80 years
   3. a vs. b -> classification group
5. VIC (voxel intensity changes): 不同组间体素均值之差 (a vs. b)
6. WAT (Welch-Aspin test) 用于评估体素对各组的区分能力
7. KSOM (Kohonen self-organizing map): vector quantization and feature extraction from VIC image ???
   1. 特征投影?
8. LSSVM (least squares support vector machine)
9. KSOM-WAT-LSSVM

### Machine Learning Models for Diagnosis of Parkinson’s Disease Using Multiple Structural Magnetic Resonance Imaging Features
1. 2022, Frontiers in Aging Neuroscience, 5.7
2. PD诊断
3. T1 (private + PPMI)
4. 根据前处理提取不同特征
   1. Cerebellar
   2. Subcortical
   3. Cortical
5. Pearson's correlation test, LASSO to select the most discriminating features
6. 5-fold cv, logistic regression
7. Heatmap analysis分析保留特征

### Exploring diagnosis and imaging biomarkers of Parkinson’s disease via iterative canonical correlation analysis based feature selection
1. 2018, Computerized Medical Imaging and Graphics, 7.4
2. PD诊断
3. T1
4. Segmentation -- GM, WM ROI -- GMV, WMV for each ROI
5. ICCA feature selection 两组变量间相关性
6. RLDA (robust linear discriminant analysis) 分类
7. Feature Extraction:
   1. Unsupervised: PCA, t-test
   2. Supervised: LASSO

### Extraction of large-scale structural covariance networks from grey matter volume for Parkinson’s disease classification
1. 2017, European Radiology, 
2. PD诊断
3. T1
4. ICA
   1. Extract SCNs: characterize the common inter-subject GMV covariations without setting a priori regions of interests
   2. 70 components (subj * ICs) * (ICs * voxels)
5. 70 ROIs (structural covariance networks)
6. Spatial regression analysis
   1. (#subjs * 70): 每个患者对应70个network integrity index (beta weight)
7. Logistic regression:
   1. Network integrity * 70
   2. LOOCV to determine the subset of 70 SCNs