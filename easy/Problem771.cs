﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//771. Jewels and Stones
//You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

//The letters in J are guaranteed distinct, and all characters in J and S are letters.Letters are case sensitive, so "a" is considered a different type of stone from "A".

//Example 1:
//Input: J = "aA", S = "aAAbbbb"
//Output: 3

//Example 2:
//Input: J = "z", S = "ZZ"
//Output: 0

//Note:
//    S and J will consist of letters and have length at most 50.
//    The characters in J are distinct.
namespace Algorithm_Leetcode_CSharp
{
    class Problem771
    {
        public int NumJewelsInStones(string J, string S)
        {
            int count = 0;
            for(int i=0; i<S.Length; i++)
            {
                if(J.Contains(S[i])){
                    count++;
                }
            }
            return count;

        }
    }
}
