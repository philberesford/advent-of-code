using System;
using System.Collections.Generic;
using System.Linq;

namespace Advent
{
    // Reference question: https://adventofcode.com/2018/day/1

    class Day1
    {
        private readonly string[] _args;

        public Day1(string [ ] args )
        {
            _args = args;
        }

        public void Calculate()
        {
            CalculateTotal();
            CalculateFrequencyCollision();
        }

        private void CalculateFrequencyCollision()
        {
            var seen = new HashSet<int>();
            var current = 0;
            seen.Add(current);
            var duplicateFound = false;

            do
            {
                foreach (var arg in _args)
                {
                    if (!duplicateFound)
                    {
                        current += Convert.ToInt32(arg);
                        if (!seen.Add(current))
                        {
                            Console.WriteLine($"Duplicate frequency is {current}");
                            duplicateFound = true;
                        }
                    }
                    
                }
            } while (!duplicateFound);
        }

        private void CalculateTotal()
        {
            var total = _args.Sum(Convert.ToInt32);
            Console.WriteLine($"Resulting frequency is {total}");
        }

    }
}
