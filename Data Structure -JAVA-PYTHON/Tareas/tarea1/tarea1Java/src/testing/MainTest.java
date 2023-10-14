package testing;

import static org.junit.jupiter.api.Assertions.*;
import testing.Main.*;

import org.junit.jupiter.api.Test;

public class MainTest {

	@Test
	public void test() {

	}

	@Test
	public void testCalcular() {

		String op = "0101 + 0101";
		float esperado = 10;
		float resultado = Main.calcular(op);

		assertEquals(esperado, resultado);

	}

	@Test
	public void testCalcularSignosDistintos() {

		String op = "0101 - 0101 * 1010";
		float esperado = 0;
		float resultado = Main.calcular(op);

		assertEquals(esperado, resultado);

	}

	@Test
	public void test_calcularSumaSimple() {
		float result = Main.calcular("0101 + 0101");
		assertEquals(result, 10);

	}

	@Test
	public void test_calcularRestaSimple() {
		float result = Main.calcular("0101 - 0101");
		assertEquals(result, 0);

	}

	@Test
	public void test_calcularMultSimple() {
		float result = Main.calcular("1010 * 1010");
		assertEquals(result, 100);

	}

	@Test
	public void test_calcularDivSimple() {
		float result = Main.calcular("1010 / 0101");
		assertEquals(result, 2);

	}

	@Test
	public void test_errorOperador() {

		float result = Main.calcular("1010 = 1010");
		assertEquals(result, 10.0);

	}

	@Test
	public void test_calcularOPGrande() {

		float result = Main.calcular("1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 + 1010 * 0001");
		assertEquals(result, 100);
	}

	@Test
	public void test_calcularTodosOperadores() {

		float result = Main.calcular("1010 - 0101 + 0001 * 0010 / 0010");
		assertEquals(result, 6);
	}

	@Test
	public void test_noBinario() {

		float result = Main.calcular("1010 + 2 + 1010");
		assertEquals(result, 20);
	}

	@Test
	public void test_calcularOperacionesMultiplesIguales() {

		float result = Main.calcular("1010 * 0010 * 1010");
		float resultDiv = Main.calcular("1010 / 0010 / 0001");
		float resultSum = Main.calcular("1010 + 0010 + 0001");
		float resultREs = Main.calcular("1010 - 0010 - 0001");
		assertEquals(result, 200);
		assertEquals(resultDiv, 5);
		assertEquals(resultSum, 13);
		assertEquals(resultREs, 7);
	}

	@Test
	public void test_esNumeroTrue() {
		boolean result = Main.esNumero("0101");
		assertTrue(result);

	}

	@Test
	public void test_esNumeroFalse() {
		boolean result = Main.esNumero("hn-");
		assertFalse(result);

	}

	@Test
	public void test_contertirBinario() {

		int result = Main.binarioADecimal("1010");
		assertEquals(result, 10);
	}

	@Test
	public void test_contertirBinario2() {

		int result = Main.binarioADecimal("0010");
		assertEquals(result, 2);
	}

	@Test
	public void testCalcularSignosDistintos2() {

		String op = "0101 + 0101 * 1010 / 0010";
		float esperado = 50;
		float resultado = Main.calcular(op);

		assertEquals(esperado, resultado);

	}
}
