/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculatormutationtests;

import calculatormutation.CalculatorMutation;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author henriqueconte
 */
public class CalculatorMutationTests extends CalculatorMutation {
    
    public CalculatorMutationTests() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }
    
    @Test
    public void testSum() {
        int a = 4;
        int b = 5;
        int expectedResult = 9;

        assertEquals(expectedResult, CalculatorMutation.sum(a, b), 0.0001);
    }
}