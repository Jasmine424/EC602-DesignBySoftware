# Copyright siminz@bu.edu
# Copyright liuzulin@bu.edu
# Copyright jafallac@bu.edu

import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['siminz@bu.edu','liuzulin@bu.edu','jafallac@bu.edu']


PROGRAM_TO_TEST = "collision"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        timeout =2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)

def change(out):
    out = out.replace(".0000","")
    return (out)


class CollisionTestCase(unittest.TestCase):   # no valid value on command line
    # "empty class - write this"
    def test_empty(self):
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],"")
        self.assertEqual(rc,2)
        out = change(out)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

   
    def test_one_3(self):  # after 0 second
        strin = "one 20 10 -2 1"
        correct_out = "0\none 20 10 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["0"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_one_4(self): # one ball after two period of time
        strin = "one 20 10 -2 1"
        correct_out = "1\none 18 11 -2 1\n3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1", "3"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")
     

    def test_two_2(self): # two balls collide and change velocity
        strin = "one 0 0 1 0\ntwo 11 0 -1 0"
        correct_out = "1\none 0 0 -1 0\ntwo 11 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")


    def test_three_4(self): # s is not a number
        strin = "one 0 0 1 0 \n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["s"],strin)
        self.assertEqual(rc,2)
        out = change(out)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_three_5(self): # too many fields on one line
        strin = "one 0 0 1 0 two 11 0 -1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,1)
        out = change(out)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_three_6(self):
        strin = "one 0 -8 0 2\ntwo 0 8 0 -2\nthree -8 0 2 0"
        correct_out = "3\none 5.0710678 -7.0710678 2 0\ntwo 5.0710678 7.0710678 2 0\nthree -12.142136 4.4408921e-16 -2 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_1(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_2(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1", "5"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_four_3(self):
        strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"
        correct_out = "5\none -1.9289322 -7.0710678 -1 0\ntwo 0 9 0 1\nthree -7.0710678 -1.9289322 0 -1\nfour 9 0 1 0\n10\none -6.9289322 -7.0710678 -1 0\ntwo 0 14 0 1\nthree -7.0710678 -6.9289322 0 -1\nfour 14 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-1", "5", "-1", "-1", "10"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_complicated(self):
        strin="2MU133 -34.94 -69.13 0.468 -0.900\n0WI913 -43.08 92.12 -0.811 -0.958\n6UP738  2.97 -66.25 -0.077 0.074\n1IA244 72.94 -86.02 -0.665 -0.283\n8RT773 -32.25 -2.63 -0.797 0.628\n0HV350 -73.97 24.21 0.960 -0.870\n0DU118 -82.09 44.95 0.661 -0.343\n4FA522 -18.20 72.32 0.734 -0.990\n1WR684 31.71 68.89 -0.509 -0.706\n7SW673 41.29 42.68 0.549 -0.012"
        correct_out = "10\n2MU133 -30.26 -78.13 0.468 -0.9\n0WI913 -51.19 82.54 -0.811 -0.958\n6UP738 2.2 -65.51 -0.077 0.074\n1IA244 66.29 -88.85 -0.665 -0.283\n8RT773 -40.22 3.65 -0.797 0.628\n0HV350 -64.37 15.51 0.96 -0.87\n0DU118 -75.48 41.52 0.661 -0.343\n4FA522 -10.86 62.42 0.734 -0.99\n1WR684 26.62 61.83 -0.509 -0.706\n7SW673 46.78 42.56 0.549 -0.012\n50\n2MU133 -11.54 -114.13 0.468 -0.9\n0WI913 -83.63 44.22 -0.811 -0.958\n6UP738 -0.88 -62.55 -0.077 0.074\n1IA244 39.69 -100.17 -0.665 -0.283\n8RT773 -16.981282 29.905421 0.92840971 0.66354266\n0HV350 -81.088718 -20.425421 -0.76540971 -0.90554266\n0DU118 -49.04 27.8 0.661 -0.343\n4FA522 8.2965691 14.806549 0.1031531 -1.4854472\n1WR684 16.463431 41.603451 0.1218469 -0.21055284\n7SW673 68.74 42.08 0.549 -0.012\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["10", "50"],strin)
        self.assertEqual(rc,0)          
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_timecrease(self):
        strin = "one 20 10 1 1"
        correct_out = "3\none 23 13 1 1\n4\none 24 14 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["4", "3"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    

    def test_largetime(self):
        strin = "one 0 0 1 0"
        correct_out = "20000\none 20000 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["20000"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"") 

    def test_sameline(self):
        strin = "one 0 0 1 0\none 0 0 1 0"
        correct_out = "1\none 1 0 1 0\none 1 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"") 

    def test_11balls(self):
        strin = "one 0 0 1 0\ntwo 15 0 1 0\nthree 30 0 1 0\nfour 45 0 1 0\nfive 60 0 1 0\nsix 75 0 1 0\nseven 90 0 1 0\neight 105 0 1 0\nnine 120 0 1 0\nten 135 0 1 0\neleven 150 0 1 0\n"
        correct_out = "1\none 1 0 1 0\ntwo 16 0 1 0\nthree 31 0 1 0\nfour 46 0 1 0\nfive 61 0 1 0\nsix 76 0 1 0\nseven 91 0 1 0\neight 106 0 1 0\nnine 121 0 1 0\nten 136 0 1 0\neleven 151 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1"],strin)
        self.assertEqual(rc,0)
        out = change(out)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"") 


#  def main():
#     # "show how to use runprogram"
#      strin="2MU133 -34.94 -69.13 0.468 -0.900\n0WI913 -43.08 92.12 -0.811 -0.958\n6UP738  2.97 -66.25 -0.077 0.074\n1IA244 72.94 -86.02 -0.665 -0.283\n8RT773 -32.25 -2.63 -0.797 0.628\n0HV350 -73.97 24.21 0.960 -0.870\n0DU118 -82.09 44.95 0.661 -0.343\n4FA522 -18.20 72.32 0.734 -0.990\n1WR684 31.71 68.89 -0.509 -0.706\n7SW673 41.29 42.68 0.549 -0.012"
#      command=["10", "50"]
# #     strin = "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0";
# #     command = ["-1","5"];
#     print(runprogram('./collisionc_19', command, strin))

#     # print(runprogram('./collisionc_44', command, strin))
#     # print(runprogram('./collisionc_20', command, strin))
#     # print(runprogram('./collisionc_9', command, strin))
#     # print(runprogram('./collisionc_0', command, strin))
#     # print(runprogram('./collisionc_27', command, strin))
# #     print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
# #     unittest.main()

# # if __name__ == '__main__':
# #     main()

# # def main():
# #     "show how to use runprogram"

# #     print(runprogram('./collisionc_27', ["-1", "5", "test"], "one 0 -6 0 1\ntwo 0 6 0 -1\nthree -6 0 1 0\nfour 6 0 -1 0"))
# #     unittest.main()

#  if __name__ == '__main__':
#     main()