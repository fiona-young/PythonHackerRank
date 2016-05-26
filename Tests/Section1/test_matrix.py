from unittest import TestCase
from Section1.Matrix import Matrix

class TestMatrix(TestCase):
    def test_get_from_edges(self):
        test_subject = Matrix.get_from_edges(3, {0: [1,2], 1: [1,2], 2: [1,2]})
        self.assertListEqual(test_subject.matrix, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])

    def test_get_zeros(self):
        test_subject = Matrix.get_zeros(4)
        self.assertListEqual(test_subject.matrix, [[0]*4]*4)

    def test_pad_zeros(self):
        test_subject = Matrix.get_from_edges(3, {0: [1,2], 1: [1,2], 2: [1,2]})
        self.assertListEqual(test_subject.matrix, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])
        test_subject.pad_zeros()
        self.assertListEqual(test_subject.matrix,  [[0]*3]*3)

    def test_copy(self):
        test_subject = Matrix.get_from_edges(3, {0: [1,2], 1: [1,2], 2: [1,2]})
        self.assertListEqual(test_subject.matrix, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])
        test_subject2 = test_subject.copy()
        test_subject.pad_zeros()
        self.assertListEqual(test_subject2.matrix, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])
        self.assertListEqual(test_subject.matrix,  [[0]*3]*3)

    def test_mat_square_mult(self):
        test_subject1 = Matrix.get_from_edges(3, {0: [1,2], 1: [1,2], 2: [1,2]})
        test_subject2 = Matrix.get_from_edges(3, {0: [0,2], 1: [0,1], 2: [1,2]})
        result = test_subject1.mat_square_mult(test_subject2)
        self.assertListEqual(result.matrix,[[1, 2, 1], [1, 2, 1], [1, 2, 1]])

    def test_pow_1(self):
        test_subject = Matrix.get_from_edges(3, {0: [1, 2], 1: [1, 2], 2: [1, 2]})
        self.assertListEqual(test_subject.pow(1).matrix, test_subject.matrix)

    def test_pow_2(self):
        test_subject = Matrix.get_from_edges(3, {0: [1, 2], 1: [1, 2], 2: [1, 2]})
        self.assertListEqual(test_subject.pow(2).matrix, [[0, 4, 4], [0, 4, 4], [0, 4, 4]])

    def test_pow_4(self):
        test_subject = Matrix.get_from_edges(3, {0: [1, 2], 1: [1, 2], 2: [1, 2]})
        self.assertListEqual(test_subject.pow(4).matrix, [[0, 8, 8], [0, 8, 8], [0, 8, 8]])

    def test_pow_40(self):
        test_subject = Matrix.get_from_edges(3, {0: [1, 2], 1: [1, 2], 2: [1, 2]})
        self.assertListEqual(test_subject.pow(40).matrix,
                             [[0, 549755813888, 549755813888], [0, 549755813888, 549755813888],
                              [0, 549755813888, 549755813888]])

    def test_pow_40_mod_54975581(self):
        test_subject = Matrix.get_from_edges(3, {0: [1, 2], 1: [1, 2], 2: [1, 2]})
        self.assertListEqual(test_subject.pow(40, 54975581).matrix, [[0, 3888, 3888], [0, 3888, 3888], [0, 3888, 3888]])
