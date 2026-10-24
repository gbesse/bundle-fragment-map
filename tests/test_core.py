import unittest,hashlib,itertools
from bundle_fragment_map import run
class Tests(unittest.TestCase):
 def test_missing_half_open_ranges(self):
  r=run({'total_bytes':6,'fragments':[{'id':'a','offset':1,'hex':'6162'},{'id':'b','offset':4,'hex':'63'}]});self.assertEqual(r['missing_ranges'],[[0,1],[3,4],[5,6]]);self.assertIsNone(r['payload_sha256'])
 def test_overlap_conflict_never_emits_arbitrary_payload(self):
  r=run({'total_bytes':2,'fragments':[{'id':'a','offset':0,'hex':'6162'},{'id':'b','offset':1,'hex':'63'}]});self.assertFalse(r['complete_unambiguous']);self.assertEqual(r['conflicts'],[{'offset':1,'fragment_ids':['a','b']}]);self.assertIsNone(r['payload_sha256'])
 def test_permutation_invariance_and_real_hash(self):
  fs=[{'id':'a','offset':0,'hex':'616263'},{'id':'b','offset':2,'hex':'6364'},{'id':'c','offset':3,'hex':'64'}]
  for order in itertools.permutations(fs):
   r=run({'total_bytes':4,'fragments':order});self.assertTrue(r['complete_unambiguous']);self.assertEqual(r['payload_sha256'],hashlib.sha256(b'abcd').hexdigest())
 def test_out_of_range_rejected(self):
  with self.assertRaises(ValueError):run({'total_bytes':1,'fragments':[{'id':'a','offset':1,'hex':'61'}]})
 def test_empty_payload(self):self.assertEqual(run({'total_bytes':0,'fragments':[]})['payload_sha256'],hashlib.sha256(b'').hexdigest())
