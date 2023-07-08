from unittest import TestCase

from classical.Caesar import Caesar
from classical.Vigenere import Vigenere
from classical.Affine import Affine


class TestCaesar(TestCase):
    def test(self):
        caesar = Caesar()

        assert caesar.encrypt("hello world") == "khoor zruog"
        assert caesar.decrypt("khoor zruog") == "hello world"

        assert caesar.encrypt("hello 2 world!") == "khoor 2 zruog!"
        assert caesar.decrypt("khoor 2 zruog!") == "hello 2 world!"

        assert caesar.encrypt("Hello WORLD 123") == "Khoor ZRUOG 123"
        assert caesar.decrypt("Khoor ZRUOG 123") == "Hello WORLD 123"


class TestVigenere(TestCase):
    def test(self):
        v = Vigenere()
        key = "myKey"

        # edge case: empty string
        assert v.encrypt("", key) == ""
        assert v.decrypt("", key) == ""

        # edge case: string only contains spaces
        assert v.encrypt("   ", key) == "   "
        assert v.decrypt("   ", key) == "   "

        # edge case: string only contains non-alphabetic characters
        assert v.encrypt("1234567890!@#$%^&*()", key) == "1234567890!@#$%^&*()"
        assert v.decrypt("1234567890!@#$%^&*()", key) == "1234567890!@#$%^&*()"

        # edge case: string with all alphabets, uppercase and lowercase
        assert v.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                         key) == "MZMHCRERMHWJWRMBOBWRGTGBWLylgbqdqlgvivqlanavqfsfavkx"
        assert v.decrypt("MZMHCRERMHWJWRMBOBWRGTGBWLylgbqdqlgvivqlanavqfsfavkx",
                         key) == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        # edge case: very long string
        assert v.decrypt(v.encrypt("A" * 10000, key), key) == "A" * 10000

        # edge case: key is a single character
        try:
            single_char_key = "A"
            assert v.encrypt("Hello, World!", single_char_key) == "Jvjah, Ewtcb!"
        except ValueError as e:
            print("")

        # edge case: key is longer than the text
        long_key = "ThisIsALongKeyThatIsLongerThanTheText"
        assert v.encrypt("Hello", long_key) != "Hello"
        assert v.decrypt(v.encrypt("Hello", long_key), long_key) == "Hello"

        assert v.encrypt("hello world", key) == "tcvpm imbpb"
        assert v.decrypt("tcvpm imbpb", key) == "hello world"

        assert v.encrypt("hello 2 world!", key) == "tcvpm 2 imbpb!"
        assert v.decrypt("tcvpm 2 imbpb!", key) == "hello 2 world!"

        assert v.encrypt("Hello WORLD 123", key) == "Tcvpm IMBPB 123"
        assert v.decrypt("Tcvpm IMBPB 123", key) == "Hello WORLD 123"


class TestAffine(TestCase):
    def test(self):
        a = Affine()
        key = (5, 8)

        # edge case: empty string
        assert a.encrypt("", key) == ""
        assert a.decrypt("", key) == ""

        # edge case: string only contains spaces
        assert a.encrypt("   ", key) == "   "
        assert a.decrypt("   ", key) == "   "

        # edge case: string only contains non-alphabetic characters
        assert a.encrypt("1234567890!@#$%^&*()", key) == "1234567890!@#$%^&*()"
        assert a.decrypt("1234567890!@#$%^&*()", key) == "1234567890!@#$%^&*()"

        assert a.encrypt("Hello World!", key) == "Rclla Oaplx!"
        assert a.decrypt("Rclla Oaplx!", key) == "Hello World!"

        # edge case: string with all alphabets, uppercase and lowercase
        assert a.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                         key) == "INSXCHMRWBGLQVAFKPUZEJOTYDinsxchmrwbglqvafkpuzejotyd"
        assert a.decrypt("INSXCHMRWBGLQVAFKPUZEJOTYDinsxchmrwbglqvafkpuzejotyd",
                         key) == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        # edge case: very long string
        assert a.decrypt(a.encrypt("A" * 10000, key), key) == "A" * 10000

