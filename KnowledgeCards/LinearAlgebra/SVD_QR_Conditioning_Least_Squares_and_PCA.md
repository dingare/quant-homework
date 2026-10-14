# SVD, QR, Conditioning, Least Squares, and PCA

## Purpose and review status

Added October 13, 2026, from [Q8 and the follow-up discussion](../../DailyTests/2026-10-11.md#q8--conditioning-and-least-squares). A learning reference, not evidence of independent mastery. English terminology with Chinese explanations. Revisit formulas and independently run the examples.

## 1. Eigenvalues versus singular values

An **eigenvector** is a nonzero direction satisfying $Av=\lambda v$ for a square matrix A. The **eigenvalue** is the scaling factor; for a general real matrix, eigenvalues may be negative or complex and eigenvectors need not form an orthogonal basis.

**Singular values** are nonnegative stretching factors and apply to rectangular matrices too. Right singular vectors describe input directions; left singular vectors describe corresponding output directions:

$$
Av_i=\sigma_i u_i.
$$

For an arbitrary matrix, the eigenvalues of $A^\top A$ are squared singular values (including zeros). Eigenvalues and singular values of A are generally different. For a symmetric PSD matrix, they coincide; for a symmetric indefinite matrix, singular values are absolute eigenvalues.

Applications: covariance eigenvectors give PCA directions; eigenvalues govern growth/decay in repeated linear dynamics (discrete-time asymptotic stability requires spectral radius strictly below one). Singular values expose rank, weak directions, and inverse sensitivity.

## 2. Vector and matrix 2-norm; condition number

$$
\|x\|_2=\sqrt{\sum_i x_i^2},\qquad
\|A\|_2=\max_{x\ne0}\frac{\|Ax\|_2}{\|x\|_2}=\sigma_{\max}(A).
$$

For square invertible A:

$$
\kappa_2(A)=\|A\|_2\|A^{-1}\|_2
=\frac{\sigma_{\max}}{\sigma_{\min}}.
$$

For a tall full-column-rank matrix, the same ratio describes conditioning on the identifiable input space; use the pseudoinverse instead of an inverse. Rank deficiency gives infinite condition number under the usual full-column identification convention.

Conditioning is a property of the problem; numerical stability is a property of the algorithm. A correct stable algorithm cannot remove inherent sensitivity. For fixed square invertible A and perturbation only to b in $Ax=b$:

$$
\frac{\|\delta x\|_2}{\|x\|_2}
\le \kappa_2(A)\frac{\|\delta b\|_2}{\|b\|_2}.
$$

This is a worst-case bound, not a statement that every perturbation is amplified equally. General least-squares perturbation bounds also depend on the residual and perturbation type.

**Q8 example:** singular values 10, 1, 0.01 imply $\kappa_2(A)=1000$. Under full column rank:

$$
\kappa_2(A^\top A)=\kappa_2(A)^2=10^6.
$$

Tall-matrix qualification: if a wide matrix has a nontrivial input nullspace, $A^\top A$ is singular; do not apply the finite full-column-rank identity blindly.

## 3. SVD formula and dimensions

Let $A\in\mathbb R^{m\times n}$ and $r=\min(m,n)$. Reduced SVD is:

$$
A=U\Sigma V^\top,
$$

where U is m by r, Sigma is r by r, and V is n by r. Columns of U and V are orthonormal; Sigma has nonnegative diagonal entries in decreasing order. A full SVD instead uses square orthogonal U and V, with rectangular Sigma.

Geometric interpretation: $V^\top$ gives coordinates in input singular directions, Sigma scales those coordinates, U maps to output directions. In a full SVD the two orthogonal transformations preserve lengths; reduced factors may also project away null directions.

### Conceptual computation through eigenvalues

1. Solve $A^\top A v_i=\lambda_i v_i$ with orthonormal eigenvectors, sorted by eigenvalue.
2. Set $\sigma_i=\sqrt{\lambda_i}$.
3. For positive singular values, set $u_i=Av_i/\sigma_i$.
4. Complete orthonormal bases where needed; do not divide by zero.

This explains where singular vectors come from. **Do not explicitly form $A^\top A$ as the default numerical route to SVD**: it squares conditioning and can damage small singular values. Direct SVD algorithms typically reduce the matrix to bidiagonal form and compute its singular decomposition using orthogonal transformations.

## 4. Least squares with SVD

Solve $\min_x\|Ax-b\|_2^2$. For tall full-column-rank A:

$$
\hat x=V\Sigma^{-1}U^\top b.
$$

Project b onto output directions, divide by positive singular values, then combine input directions. Small singular values amplify the corresponding projected disturbances.

If rank deficient, the **Moore–Penrose pseudoinverse** uses zero for zero singular values and reciprocals for nonzero ones:

$$
\hat x=A^+b=V\Sigma^+U^\top b.
$$

This selects the minimum-Euclidean-norm least-squares solution. Numerical pseudoinverse routines use a tolerance to determine effective rank; discarding a small but nonzero singular value changes the mathematical solution and acts as regularization.

## 5. QR and least squares

For tall full-column-rank A, reduced **QR decomposition** is:

$$
A=QR,\qquad Q^\top Q=I_n,
$$

with Q m by n and R n by n upper triangular. Then:

$$
\|Ax-b\|_2^2
=\|Rx-Q^\top b\|_2^2+\|(I-QQ^\top)b\|_2^2.
$$

The second term does not depend on x. Solve:

$$
R\hat x=Q^\top b
$$

by **back substitution**, rather than explicitly computing an inverse. Householder QR is a standard stable approach; column-pivoted QR can help reveal rank. SVD is often more informative for rank deficiency and spectral regularization, at greater cost. Poor conditioning does not make QR intrinsically unstable; SVD also cannot eliminate the original problem's sensitivity.

Normal equations are:

$$
A^\top A\hat x=A^\top b.
$$

They can be computationally convenient but square the condition number. QR and SVD work directly with A and avoid this extra loss of numerical accuracy. Neither technique creates information missing from the data.

## 6. PCA directly from SVD

Let X have n samples in rows and p features in columns; assume n exceeds one. Center each feature using training-set means:

$$
X_c=X-\mathbf1\bar x^\top.
$$

Standardization is optional and changes the objective: covariance PCA emphasizes absolute variance, while standardized-feature PCA adjusts for feature scales.

Compute $X_c=U\Sigma V^\top$. The sample covariance matrix is:

$$
C=\frac{X_c^\top X_c}{n-1}
=V\frac{\Sigma^2}{n-1}V^\top.
$$

For reduced SVD with fewer columns than features, missing covariance directions have zero eigenvalues. Thus:

- Columns $v_j$ of V are **principal component directions**, one weight per original feature.
- Variance of component j is $\lambda_j=\sigma_j^2/(n-1)$.
- Explained variance ratio is $\sigma_j^2/\sum_\ell\sigma_\ell^2$ when total variance is nonzero.
- First k **scores** are $Z=X_cV_k=U_k\Sigma_k$.
- Rank-k reconstruction is $\hat X=ZV_k^\top+\mathbf1\bar x^\top$.
- For new data use the training mean and the same directions, not a newly fitted test-set mean or PCA.

NumPy returns **Vt**, which is $V^\top$: right singular vectors are its rows. The top ten vectors are `Vt[:10, :]`; projection directions are `Vt[:10, :].T`. Need at least ten available directions; ten nonzero-variance components require centered rank at least ten. Component signs are arbitrary, and tied singular values allow rotations within the tied subspace.

PCA ranks directions by feature variance, not by predictive importance for a target. Low-variance directions can still contain useful predictive information.

## 7. Runnable Python examples

Requires NumPy. Standard library functions should be preferred to manually forming inverses.

```python
import numpy as np

A = np.array([[10.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 0.01],
              [1.0, 1.0, 1.0]])
b = np.array([1.0, 2.0, 3.0, 4.0])

# SVD: reduced factors, singular values sorted descending
U, s, Vt = np.linalg.svd(A, full_matrices=False)
assert np.allclose(A, (U * s) @ Vt)
x_svd = Vt.T @ ((U.T @ b) / s)  # full-column-rank example only

# QR: solve triangular system without forming an inverse
Q, R = np.linalg.qr(A, mode="reduced")
x_qr = np.linalg.solve(R, Q.T @ b)
x_library = np.linalg.lstsq(A, b, rcond=None)[0]
assert np.allclose(x_svd, x_library)
assert np.allclose(x_qr, x_library)

# Exact Q8 singular values / conditioning
D = np.diag([10.0, 1.0, 0.01])
assert np.isclose(np.linalg.cond(D), 1000.0)
assert np.isclose(np.linalg.cond(D.T @ D), 1_000_000.0)

# PCA: rows are samples; columns are features
X = np.array([[1.0, 2.0, 0.0], [2.0, 1.0, 1.0],
              [3.0, 4.0, 2.0], [4.0, 3.0, 0.0],
              [5.0, 6.0, 3.0]])
mean = X.mean(axis=0)
Xc = X - mean
U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
k = 2
components = Vt[:k]           # shape (k, features)
scores = Xc @ components.T   # shape (samples, k)
explained_variance = s**2 / (len(X) - 1)
explained_ratio = s**2 / np.sum(s**2)
X_approx = scores @ components + mean
assert np.allclose(scores, U[:, :k] * s[:k])
assert np.allclose(np.cov(scores, rowvar=False),
                   np.diag(explained_variance[:k]))
assert np.isclose(explained_ratio.sum(), 1.0)
```

## 8. Regularization and interview retrieval

For ridge with lambda positive, the SVD-direction multipliers are $\sigma_i/(\sigma_i^2+\lambda)$ instead of $1/\sigma_i$. Truncated SVD discards weak directions; ridge shrinks them smoothly. Both trade bias against sensitivity.

Interview answer: "QR is a standard stable choice for full-rank least squares. SVD directly exposes singular directions and effective rank, and supports pseudoinverses, PCA, and spectral regularization. Forming normal equations squares conditioning; neither QR nor SVD removes inherent ill-conditioning."

- [ ] Explain eigenvalues versus singular values without mixing them up.
- [ ] Re-derive $A^\top A=V\Sigma^2V^\top$ and the full-column-rank condition-number identity.
- [ ] Derive QR and SVD least-squares formulas and explain small-singular-value sensitivity.
- [ ] Compute PCA scores, explained variance, and new-data projections; identify V versus Vt shapes.
- [ ] Run the code and explain each output independently.

Related: [L001 — Ridge / PCA shrinkage](../../Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md), [L002 — PCA covariance geometry](../../Questions/LinearAlgebra/L002_PCA_Covariance_Geometry_and_Why_Butterfly_Trades_Curvature.md).
