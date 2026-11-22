# Polybrutus D60 — proof-first validation and controlled publication

1. Direct scientific parent D59 frozen v0.1.0 peeled Git commit bc935bffa479a1843a4359b66e06a00ace4772a1, DOI 10.5281/zenodo.24431368, entire original source ZIP SHA256 30ec6a1b9baae1fec7a2c085750c6b9364e5e8de8244fe4b42c845e713fb05fa, certificate SHA256 921a07b27808e980fa1bc253528276e4192ab04fb4ae8b9e4db8d47d873fb5f7. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 65 norm-one points and 2080 labelled exact squared distances; 2016 unchanged old D59 pairs and 64 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 60.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 65/2 mult 54 and 32 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D60 sixty/fifty-fourfold keywords, structured isDerivedFrom direct D59 DOI, separate D59/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d60.py
    python tests/independent_d60.py
    python src/check_zenodo_metadata.py
