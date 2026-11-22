#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d60.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==60
assert c['vertices']==m['norm_one_vertices']==65
assert c['pairs']==m['exact_labelled_squared_pairs']==2080
assert c['affine_rank']==c['centered_gram_rank']==60
assert c['eigenvalue_65_over_2_multiplicity']==m['model_eigenvalue_65_over_2_multiplicity']==54
assert c['eigenvalue_32_multiplicity']==m['model_eigenvalue_32_multiplicity']==4
assert c['parent_tag_commit']=='bc935bffa479a1843a4359b66e06a00ace4772a1'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24431368'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24431368','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty' in m['keywords']
assert 'fifty-fourfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24431368' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not any(x in str(m['keywords']) for x in ('fifty-nine','fifty-threefold','sixty-one','fifty-fivefold'))
note=(R/'publication/POLYBRUTUS_60D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24431368','10.5281/zenodo.24407952'))
print('D60_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D59_PARENT_AND_SEPARATE_D59_D7_REFERENCES_PASS')
