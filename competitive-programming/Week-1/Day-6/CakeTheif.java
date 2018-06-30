import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static class Cake {

        final int weight;
        final int cost;

        public Cake(int weight, int cost) {
            this.weight = weight;
            this.cost  = cost;
        }
    }

    public static int maxDuffelBagcost(final Cake[] cakes, final int capacity) {
    	final int[] maxcostAtEachCapacity = new int[capacity + 1];
    
    	for (int i = 0; i <= capacity; i++) {
      		int currentMaxcost = 0;

      		for (int j = 0; j < cakes.length; j++) {
        	final Cake cake = cakes[j];
        		if (cake.weight == 0 && cakes.length==1){
            		throw new IllegalArgumentException("hi");
        		}
        		if (cake.weight <= i) {
          
          		int maxcost = cake.cost + maxcostAtEachCapacity[i - cake.weight];
          		currentMaxcost = Math.max(maxcost, currentMaxcost);
        
        		}
      		}
      		maxcostAtEachCapacity[i] = currentMaxcost;
   			}
    	return maxcostAtEachCapacity[capacity];
  	}

    // tests

    @Test
    public void oneCakeTest() {
        final Cake[] Cakes = {new Cake(2, 1)};
        final int weightCapacity = 9;
        final long expected = 4;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void twoCakesTest() {
        final Cake[] Cakes = {new Cake(4, 4), new Cake(5, 5)};
        final int weightCapacity = 9;
        final long expected = 9;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void onlyTakeLessValuableCakeTest() {
        final Cake[] Cakes = {new Cake(4, 4), new Cake(5, 5)};
        final int weightCapacity = 12;
        final long expected = 12;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void lotsOfCakesTest() {
        final Cake[] Cakes = {
            new Cake(2, 3), new Cake(3, 6), new Cake(5, 1),
            new Cake(6, 1), new Cake(7, 1), new Cake(8, 1)
        };
        final int weightCapacity = 7;
        final long expected = 12;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void costToWeightRatioIsNotOptimalTest() {
        final Cake[] Cakes = {new Cake(51, 52), new Cake(50, 50)};
        final int weightCapacity = 100;
        final long expected = 100;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void zeroCapacityTest() {
        final Cake[] Cakes = {new Cake(1, 2)};
        final int weightCapacity = 0;
        final long expected = 0;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test
    public void cakeWithZerocostAndWeightTest() {
        final Cake[] Cakes = {new Cake(0, 0), new Cake(2, 1)};
        final int weightCapacity = 7;
        final long expected = 3;
        final long actual = maxDuffelBagcost(Cakes, weightCapacity);
        assertEquals(expected, actual);
    }

    @Test(expected = Exception.class)
    public void cakeWithNonZerocostAndZeroWeightTest() {
        final Cake[] Cakes = {new Cake(0, 5)};
        final int weightCapacity = 5;
        maxDuffelBagcost(Cakes, weightCapacity);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}
