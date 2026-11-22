# Polybrutus D60 — exact 65-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d59@v0.1.0, actual peeled scientific Git commit \`bc935bffa479a1843a4359b66e06a00ace4772a1\`, DOI 10.5281/zenodo.24431368, original full source ZIP SHA256 \`30ec6a1b9baae1fec7a2c085750c6b9364e5e8de8244fe4b42c845e713fb05fa\`, original D59 certificate SHA256 \`921a07b27808e980fa1bc253528276e4192ab04fb4ae8b9e4db8d47d873fb5f7\`.

## Conservative perpendicular norm-one extension

Embed all 64 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_65. Every one of C(64,2)=2016 old labelled squared distances remains unchanged; all 64 new squared distances equal 2R². Total C(65,2)=2080 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **53** independent mutually orthogonal norm-one axes (rank 53). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+53=60**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/65, B=-(HDH)/2=HGH is PSD of rank **60**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 60 (61 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2049, 9:3, 10:10, 12:6, 13:2, 16:2; total 2080. Exact sum of squared pair distances R=1: **16687/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 64 old points with weight 1/2. The chosen ideal Laplacian is L60=[[L59+I64/2,-1_64/2],[-1_64ᵀ/2,64/2]]. Its characteristic recurrence is chi65(z)=z(z-65/2)chi64(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi65(z)=z(z-65/2)^54(z-32)^4*f6(z-29).
Exact rational nullities yield Laplacian eigenvalue **65/2 multiplicity 54**, and **32 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D59 DOI 10.5281/zenodo.24431368; historical D7 DOI 10.5281/zenodo.24407952.
