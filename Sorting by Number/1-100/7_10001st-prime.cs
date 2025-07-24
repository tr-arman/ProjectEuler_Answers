using System;

class Program
{
    static void Main()
    {
        int count = 0;
        int number = 1;

        while (count < 10001)
        {
            number++;
            if (IsPrime(number))
            {
                count++;
            }
        }

        Console.WriteLine(number);
    }

    static bool IsPrime(int num)
    {
        if (num < 2) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        int boundary = (int)Math.Sqrt(num);

        for (int i = 3; i <= boundary; i += 2)
        {
            if (num % i == 0)
                return false;
        }

        return true;
    }
}

//104743
//https://projecteuler.net/problem=7