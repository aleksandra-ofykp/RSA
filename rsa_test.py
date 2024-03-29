import unittest
import random

from rsa import rsa,encode_rsa,decode_rsa,evklid,are_relatively_prime,adv_evk

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class RSATest(unittest.TestCase):
    def test_relatively_1(self):
        self.assertEqual(are_relatively_prime(27, 98), True)

    def test_relatively_2(self):
        self.assertEqual(are_relatively_prime(25, 88), True)

    def test_evklid_1(self):
        self.assertEqual(evklid(3, 7), (1))
    
    def test_evklid_2(self):
        self.assertEqual(evklid(3, 9), (3))

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
    
    def test_encode_rsa_encrypt_massage_1(self):
        self.assertEqual(encode_rsa([899, 11], 60), (308))

    def test_decode_rsa_encrypt_massage_1(self):
        self.assertEqual(decode_rsa([899, 611], 308), (60))

    def test_decode_encode(self):
        pubk, prk = rsa(13)
        r = random.randint(1,500)
        for i in range(1,r):
            self.assertEqual(decode_rsa(prk, encode_rsa(pubk, i)), i)
    


if __name__ == "__main__":
    unittest.main()
