import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;
import java.util.Stack;

public class Solution {
    
    public static boolean checkIfSame(char pop, char c)
    {
        if(pop == '(' && c == ')')return true;
        else if(pop == '{' && c == '}') return true;
        else if(pop == '[' && c == ']') return true;
        else return false;
    }

    public static boolean isValid(String code) {
        Stack<Character> stack = new Stack<Character>();
        // determine if the input code is valid
        for(int i = 0; i < code.length(); i++)
        {
            if(code.charAt(i) == '(' || code.charAt(i) == '{' || code.charAt(i) == '[')
            {
                stack.push(code.charAt(i));
            }
            
            else if(code.charAt(i) == ')' || code.charAt(i) == '}' || code.charAt(i) == ']')
            {
                if(stack.empty()) return false;
                else if(checkIfSame(stack.pop(),code.charAt(i))==false) return false;
            }
        }
        if(stack.empty()) return true;
        else return false;

    }


    // tests

    @Test
    public void validShortCodeTest() {
        final boolean result = isValid("()");
        assertTrue(result);
    }

    @Test
    public void validLongerCodeTest() {
        final boolean result = isValid("([]{[]})[]{{}()}");
        assertTrue(result);
    }

    @Test
    public void mismatchedOpenerAndCloserTest() {
        final boolean result = isValid("([][]}");
        assertFalse(result);
    }

    @Test
    public void missingCloserTest() {
        final boolean result = isValid("[[]()");
        assertFalse(result);
    }

    @Test
    public void extraCloserTest() {
        final boolean result = isValid("[[]]())");
        assertFalse(result);
    }

    @Test
    public void emptyStringTest() {
        final boolean result = isValid("");
        assertTrue(result);
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
