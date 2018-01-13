"""this is the main part of the assignment"""

# Copyright ? ?@bu.edu
# Copyright ?? ??@bu.edu
# Copyright ??? ???@bu.edu
import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['?@bu.edu', '??@bu.edu', '???@bu.edu']

PROGRAM_TO_TEST = "collision"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
    def test_empty(self):
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],"")
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_one_1(self): # move rightup
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_one_2(self):  # no velocity still
        strin = "one 20 10 0 0"
        correct_out = "3\none 20 10 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_one_3(self):  # after 0 second
        strin = "one 20 10 -2 1"
        correct_out = "0\none 20 10 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["0"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_one_4(self): # one ball after two period of time
        strin = "one 20 10 -2 1"
        correct_out = "1\none 18 11 -2 1\n3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1", "3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
     
    def test_two_1(self): #  two balls have the same direction and same v.
        strin = "one 0 0 1 1\ntwo 10 10 1 1"
        correct_out = "1\none 1 1 1 1\ntwo 11 11 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    # def test_two_1(self):
    #     strin = "one 0 0 1 1\ntwo 10 0 -1 1"
    #     correct_out = "1\none -1 1 -1 1\ntwo 11 1 1 1\n"
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
    #     self.assertEqual(rc,0)
    #     self.assertEqual(out,correct_out)
    #     self.assertEqual(errs,"")

    def test_two_2(self): # two balls collide and change velocity
        strin = "one 0 0 1 0\ntwo 11 0 -1 0"
        correct_out = "1\none 0 0 -1 0\ntwo 11 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_two_3(self): # two balls collide and change velocity after 2 period of time
        strin = "one 0 0 1 0\ntwo 11 0 -1 0"
        correct_out = "1\none 0 0 -1 0\ntwo 11 0 1 0\n3\none -2 0 -1 0\ntwo 13 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_three_1(self):  # three balls only two collide
        strin = "one 0 0 1 0\ntwo 11 0 -1 0\nthree -10 -10 -5 -5"
        correct_out = "1\none 0 0 -1 0\ntwo 11 0 1 0\nthree -15 -15 -5 -5\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_three_2(self): #negative time should be ignored
        strin = "one 0 0 1 0\ntwo 11 0 -1 0\nthree -10 -10 -5 -5"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1"],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_three_3(self): # exp(1) is not a valid value
        strin = "one 0 0 1 0\ntwo 11 0 -1 0\nthree -10 -10 -5 -5"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["exp(1)"],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")
        
    # def test_three_1(self):
    #     strin = "one 0 0 1 0 1\n"
    #     (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
    #     self.assertEqual(rc,1)

    def test_three_4(self): # s is not a number
        strin = "one 0 0 1 0 \n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["s"],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_three_5(self): # too many fields on one line
        strin = "one 0 0 1 0 two 11 0 -1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_three_6(self):
        strin = "one 0 -8 0 2\ntwo 0 8 0 -2\nthree -8 0 2 0"
        correct_out = "3\none 5.0710678 -7.0710678 2 0\ntwo 5.0710678 7.0710678 2 0\nthree -12.142136 4.4408921e-16 -2 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_1(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_2(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1", "5"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_3(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n10\none -6.9289322 -7.0710678 -1 0\ntwo 0 14 0 1\nthree -7.0710678 -6.9289322 0 -1\nfour 14 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1", "5", "-1", "-1", "10"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_4(self):
        strin = "one one one one one"
        #correct_out = "5\none 0 -6 0 0\ntwo 0 6 0 0\nthree -6 0 0 0\nfour 6 0 0 0\n10\none 0 -6 0 0\ntwo 0 6 0 0\nthree -6 0 0 0\nfour 6 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1", "5", "-1", "-1", "10"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_complicated(self):
        strin="2MU133 -34.94 -69.13 0.468 -0.900\n0WI913 -43.08 92.12 -0.811 -0.958\n6UP738  2.97 -66.25 -0.077 0.074\n1IA244 72.94 -86.02 -0.665 -0.283\n8RT773 -32.25 -2.63 -0.797 0.628\n0HV350 -73.97 24.21 0.960 -0.870\n0DU118 -82.09 44.95 0.661 -0.343\n4FA522 -18.20 72.32 0.734 -0.990\n1WR684 31.71 68.89 -0.509 -0.706\n7SW673 41.29 42.68 0.549 -0.012"
        correct_out = "10\n2MU133 -30.26 -78.13 0.468 -0.9\n0WI913 -51.19 82.54 -0.811 -0.958\n6UP738 2.2 -65.51 -0.077 0.074\n1IA244 66.29 -88.85 -0.665 -0.283\n8RT773 -40.22 3.65 -0.797 0.628\n0HV350 -64.37 15.51 0.96 -0.87\n0DU118 -75.48 41.52 0.661 -0.343\n4FA522 -10.86 62.42 0.734 -0.99\n1WR684 26.62 61.83 -0.509 -0.706\n7SW673 46.78 42.56 0.549 -0.012\n50\n2MU133 -11.54 -114.13 0.468 -0.9\n0WI913 -83.63 44.22 -0.811 -0.958\n6UP738 -0.88 -62.55 -0.077 0.074\n1IA244 39.69 -100.17 -0.665 -0.283\n8RT773 -16.981282 29.905421 0.92840971 0.66354266\n0HV350 -81.088718 -20.425421 -0.76540971 -0.90554266\n0DU118 -49.04 27.8 0.661 -0.343\n4FA522 8.2965691 14.806549 0.1031531 -1.4854472\n1WR684 16.463431 41.603451 0.1218469 -0.21055284\n7SW673 68.74 42.08 0.549 -0.012\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["10", "50"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
        
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.endswith('.py'),"wrong program name")

# def main():
#     "show how to use runprogram"

#     print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
#     unittest.main()

# if __name__ == '__main__':
#     main()