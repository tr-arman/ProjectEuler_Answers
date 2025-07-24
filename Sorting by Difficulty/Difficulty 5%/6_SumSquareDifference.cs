using System;

class Program
{
    static void Main()
    {
        int limit = 100;
        long sumOfSquares = 0;
        long sum = 0;

        for (int i = 1; i <= limit; i++)
        {
            sumOfSquares += i * i;
            sum += i;
        }

        long squareOfSum = sum * sum;
        long difference = squareOfSum - sumOfSquares;

        Console.WriteLine(difference);
    }
}

//25164150