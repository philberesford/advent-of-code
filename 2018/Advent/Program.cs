using System;
using System.IO;

namespace Advent
{
    class Program
    {
        static void Main(string[] args)
        {
            var lines = File.ReadAllLines(@"..\..\Day1\input.txt");
            var d1 = new Day1(lines);
            d1.Calculate();
            Console.ReadLine();
        }
    }
}
