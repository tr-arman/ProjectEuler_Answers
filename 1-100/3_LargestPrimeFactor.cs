using System;

class Program
{
    static void Main()
    {
        long number = 600851475143;
        long factor = 2;
        long lastFactor = 1;

        while (number > 1)
        {
            if (number % factor == 0)
            {
                number /= factor;
                lastFactor = factor;
                while (number % factor == 0)
                    number /= factor;
            }
            factor++;
        }

        Console.WriteLine(lastFactor);
    }
}

//6857