import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;
import static org.junit.Assert.*;

public class Solution {

    public static int[] sortScores(int[] unorderedScores, int highestPossibleScore) {
        
    	int len = unorderedScores.length;
    	int count[] = new int[highestPossibleScore];
    	Arrays.fill(count,0);

    	for (int i :unorderedScores) {
    		count[i] += 1;
    	}

    	for(int i = 1; i < highestPossibleScore; i++)
    	{
    		count[i] += count[i-1];
    	}

    	int output[] = new int[len];
    	
    	for(int i = 0; i < len; i++)
    	{
    		output[count[unorderedScores[i]-1]] = unorderedScores[i];
    		count[unorderedScores[i]]--;
    	}

    	for(int i=0; i<output.length/2; i++)
		{ 
			int temp = output[i]; 
			output[i] = output[output.length -i -1]; 
			output[output.length -i -1] = temp; 
		}
    	return output;
    }

   // tests

    @Test
    public void noScoresTest() {
        final int[] scores = {};
        final int[] expected = {};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void oneScoreTest() {
        final int[] scores = {55};
        final int[] expected = {55};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void twoScoresTest() {
        final int[] scores = {30, 60};
        final int[] expected = {60, 30};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void manyScoresTest() {
        final int[] scores = {37, 89, 41, 65, 91, 53};
        final int[] expected = {91, 89, 65, 53, 41, 37};
        final int[] actual = sortScores(scores, 100);
        assertArrayEquals(expected, actual);
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
