using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//7. Reverse Integer
//Given a 32-bit signed integer, reverse digits of an integer.

//Example 1:
//Input: 123
//Output: 321

//Example 2:
//Input: -123
//Output: -321

//Example 3:
//Input: 120
//Output: 21

//Note:
//Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

namespace Algorithm_Leetcode_CSharp__Easy
{
    class Problem007
    {
        public int Reverse_1(int x)
        {
            // avoid overflow, so use long variable
            long num = 0;
            while (x != 0)
            {
                int r = x % 10;
                num = num * 10 + r;
                x /= 10;
            }
            if (num > int.MaxValue || num < int.MinValue) return 0;

            return Convert.ToInt32(num);
        }

        public int Reverse_2(int x)
        {
            int num = 0;
            while (x != 0)
            {
                int r = x % 10;
                //avoid overflow
                if (num > int.MaxValue/10 || num < int.MinValue/10 ) return 0;
                num = num * 10 + r;
                x /= 10;
            }
        
            return (num);
        }
    }
}
