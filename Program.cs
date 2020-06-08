using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithm_Leetcode_CSharp__Easy
{
    class Program
    {
        static void Main(string[] args)
        {
            //Problem001 Instance001 = new Problem001();
            //int[] nums = new int[] { 2, 7, 11, 15 };
            //int target = 9;
            //int[] result = new int[] { };
            //result = Instance001.TwoSum(nums, target);
            //Console.WriteLine(result[0].ToString() + ',' + result[1].ToString());

            Problem1470 Instance = new Problem1470();
            int[] nums = new int[] { 2, 5, 1, 3, 4, 7 };
            int[] result = Instance.Shuffle(nums, 3);
            foreach (int item in result)
            {
                Console.Write(item);
            }
            Console.ReadLine();
        }
    }
}
