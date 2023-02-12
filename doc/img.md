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
3. T1 (PPMI)
4. VBM -- ROI -- Features
   1. First-order: average, central moments, entropy
   2. Second-order: GLCM based
5. PCA + Wrappers Feature Subset Selection
   1. Wrappers Feature Subset Selection: 根据相关性添加新特征，同时去除insignificant特征 (How to evaluate significance using complex models)