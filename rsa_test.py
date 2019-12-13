import unittest

from rsa import rsa,encode_rsa,decode_rsa

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class RSATest(unittest.TestCase):
    def test_encrypt_open_and_close_key_1(self):
        self.assertEqual(rsa(11, 13), ([143, 7], [143, 103]))

    def test_encrypt_open_and_close_key_2(self):
        self.assertEqual(rsa(3, 7), ([21, 5], [21, 5]))

    def test_numbers_is_prime(self):
        with self.assertRaisesWithMessage(ValueError):
            rsa(6, 17)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
    
    def test_encode_rsa_encrypt_massage_1(self):
        self.assertEqual(encode_rsa([899, 11], 60), (308))

    def test_decode_rsa_encrypt_massage_1(self):
        self.assertEqual(decode_rsa([899, 611], 308), (60))


    


if __name__ == "__main__":
    unittest.main()
