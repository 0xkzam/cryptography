from unittest import TestCase
from util.math import *
import time
import math


class Test(TestCase):

    def test_gcd(self):

        with self.assertRaises(ValueError):
            self.assertEqual(gcd(0, 0), 0)

        self.assertEqual(gcd(1, 1), math.gcd(1, 1))
        self.assertEqual(gcd(1, 0), math.gcd(1, 0))
        self.assertEqual(gcd(34, -12), math.gcd(34, -12))
        self.assertEqual(gcd(-34, -12), math.gcd(-34, -12))

        self.assertEqual(gcd(100, 11), math.gcd(100, 11))
        self.assertEqual(gcd(499017086208, 676126714752), math.gcd(499017086208, 676126714752))
        self.assertEqual(gcd(5988737349, 578354589), math.gcd(5988737349, 578354589))

    def test_gcd_recursive(self):

        with self.assertRaises(ValueError):
            self.assertEqual(gcd_recursive(0, 0), 0)

        self.assertEqual(gcd_recursive(1, 1), math.gcd(1, 1))
        self.assertEqual(gcd_recursive(1, 0), math.gcd(1, 0))
        self.assertEqual(gcd_recursive(34, -12), math.gcd(34, -12))
        self.assertEqual(gcd_recursive(-34, -12), math.gcd(-34, -12))

        self.assertEqual(gcd_recursive(100, 11), math.gcd(100, 11))
        self.assertEqual(gcd_recursive(499017086208, 676126714752), math.gcd(499017086208, 676126714752))
        self.assertEqual(gcd_recursive(5988737349, 578354589), math.gcd(5988737349, 578354589))

    def test_extended_gcd(self):

        p, q = 0, 0
        with self.assertRaises(ValueError):
            gcd_, s, t = extended_gcd(p, q)

        p, q = 1, 1
        gcd_, s, t = extended_gcd(p, q)
        self.assertEqual(gcd_, 1)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 1, 0
        gcd_, s, t = extended_gcd(p, q)
        self.assertEqual(gcd_, 1)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 161, 28
        gcd_, s, t = extended_gcd(p, q)
        self.assertEqual(gcd_, 7)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 28, 161
        gcd_, s, t = extended_gcd(p, q)
        self.assertEqual(gcd_, 7)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = -45122, 885
        gcd_, s, t = extended_gcd(p, q)
        self.assertEqual(p * s + q * t, gcd_)

    def test_extended_gcd_recursive(self):

        p, q = 0, 0
        with self.assertRaises(ValueError):
            gcd_, s, t = extended_gcd_recursive(p, q)

        p, q = 1, 1
        gcd_, s, t = extended_gcd_recursive(p, q)
        self.assertEqual(gcd_, 1)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 1, 0
        gcd_, s, t = extended_gcd_recursive(p, q)
        self.assertEqual(gcd_, 1)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 161, 28
        gcd_, s, t = extended_gcd_recursive(p, q)
        self.assertEqual(gcd_, 7)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = 28, 161
        gcd_, s, t = extended_gcd_recursive(p, q)
        self.assertEqual(gcd_, 7)
        self.assertEqual(p * s + q * t, gcd_)

        p, q = -45122, 885
        gcd_, s, t = extended_gcd_recursive(p, q)
        self.assertEqual(p * s + q * t, gcd_)

    def test_mod_inverse(self):
        # 0 <= a < m and m > 1
        with self.assertRaises(ValueError):
            a_inv = mod_inverse(4, 3)
        with self.assertRaises(ValueError):
            a_inv = mod_inverse(2, -3)
        with self.assertRaises(ValueError):
            a_inv = mod_inverse(-2, 3)
        with self.assertRaises(ValueError):
            a_inv = mod_inverse(1, 1)

        a_inv = mod_inverse(0, 1)
        self.assertEqual(0, a_inv)

        a_inv = mod_inverse(11, 26)
        self.assertEqual(19, a_inv)

        with self.assertRaises(ValueError):
            mod_inverse(464632, 26)

    def test_q1_isprime(self):

        for p in Test.primes_first_1000:
            self.assertEqual(q1_isprime(p), True)

        for p in Test.non_primes:
            self.assertEqual(q1_isprime(p), False)

        # # Large prime
        # start = time.time()
        # print("large prime: " + str(q1_isprime_1(Test.large_primes[0])))
        # end = time.time()
        # print("large prime- time taken: " + str(end - start))

    def test_q2_isprime(self):
        for p in Test.primes_first_1000:
            self.assertEqual(q2_isprime(p), True)

        for p in Test.non_primes:
            self.assertEqual(q2_isprime(p), False)

        # Large prime
        start = time.time()
        print("large prime: " + str(q2_isprime(Test.large_primes[0])))
        end = time.time()
        print("large prime- time taken: " + str(end - start))

    def test_miller_rabin_test(self):
        for p in Test.primes_first_1000:
            self.assertEqual(miller_rabin_test(p), True)

        for p in Test.non_primes:
            self.assertEqual(miller_rabin_test(p), False)

        # Large primes
        for p in Test.large_primes:
            start = time.time()
            result = miller_rabin_test(p)
            self.assertEqual(result, True)
            end = time.time()
            print("large prime: " + str(p))
            print("time taken: " + str(end - start))

        start = time.time()
        x = Test.large_composites[0]
        result = miller_rabin_test(x)
        self.assertEqual(result, False)
        end = time.time()
        print("composite: " + str(x))
        print("time taken: " + str(end - start))

    def test_factors(self):
        num, expected = 1, []
        self.assertEqual(expected, factors(num))

        num, expected = 2, [2]
        self.assertEqual(expected, factors(num))

        num, expected = 3, [3]
        self.assertEqual(expected, factors(num))

        num, expected = 996, [2, 2, 3, 83]
        self.assertEqual(expected, factors(num))

        num, expected = 763823487, [3, 7, 139, 261673]
        self.assertEqual(expected, factors(num))

    # Testing data
    large_primes = [174440041, 3731292319, 3657500101, 88362852307, 414507281407, 2428095424619, 4952019383323,
                    12055296811267, 17461204521323, 28871271685163, 53982894593057,
                    35742549198872617291353508656626642567,
                    5210644015679228794060694325390955853335898483908056458352183851018372555735221,
                    6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
                    ]
    large_composites = [
        6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057157]

    primes_first_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                         197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
                         311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                         431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
                         557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
                         661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                         809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
                         937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    non_primes = [-1, 0, 1, 4, 9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 69, 75, 77, 81, 85, 87, 91,
                  93, 95, 99, 105, 111, 115, 117, 119, 121, 123, 125, 129, 133, 135, 141, 143, 145, 147, 153, 155, 159,
                  161, 165,
                  169, 171, 175, 177, 183, 185, 187, 189, 195, 201, 203, 205, 207, 209, 213, 215, 217, 219, 221, 225,
                  231, 235, 237, 243, 245, 247, 249, 253, 255, 259, 261, 265, 267, 273, 275, 279, 285, 287, 289, 291,
                  295, 297, 299, 301, 303, 305, 309, 315, 319, 321, 323, 325, 327, 329, 333, 335, 339, 341, 343, 345,
                  351, 355, 357, 361, 363, 365, 369, 371, 375, 377, 381, 385, 387, 391, 393, 395, 399, 403, 405, 407,
                  411, 413, 415, 417, 423, 425, 427, 429, 435, 437, 441, 445, 447, 451, 453, 455, 459, 465, 469, 471,
                  473, 475, 477, 481, 483, 485, 489, 493, 495, 497, 501, 505, 507, 511, 513, 515, 517, 519, 525, 527,
                  529, 531, 533, 535, 537, 539, 543, 545, 549, 551, 553, 555, 559, 561, 565, 567, 573, 575, 579, 581,
                  583, 585, 589, 591, 595, 597, 603, 605, 609, 611, 615, 621, 623, 625, 627, 629, 633, 635, 637, 639,
                  645, 649, 651, 655, 657, 663, 665, 667, 669, 671, 675, 679, 681, 685, 687, 689, 693, 695, 697, 699,
                  703, 705, 707, 711, 713, 715, 717, 721, 723, 725, 729, 731, 735, 737, 741, 745, 747, 749, 753, 755,
                  759, 763, 765, 767, 771, 775, 777, 779, 781, 783, 785, 789, 791, 793, 795, 799, 801, 803, 805, 807,
                  813, 815, 817, 819, 825, 831, 833, 835, 837, 841, 843, 845, 847, 849, 851, 855, 861, 865, 867, 869,
                  871, 873, 875, 879, 885, 889, 891, 893, 895, 897, 899, 901, 903, 905, 909, 913, 915, 917, 921, 923,
                  925, 927, 931, 933, 935, 939, 943, 945, 949, 951, 955, 957, 959, 961, 963, 965, 969, 973, 975, 979,
                  981, 985, 987, 989, 993, 995, 999]
