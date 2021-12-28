from main import calcJacobian, modulo, solovoyStrassen
import sympy

iterations = 50
num = [14, 11, 20, 83, 103, 305, 654, 1259, 8493, 29034]

def test_prime():
	for i in range(len(num)):
		assert solovoyStrassen(num[i], iterations) == sympy.isprime(num[i])