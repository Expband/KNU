using System;
namespace sqt5
{
    public class Calculator
    {
        public Calculator()
        {
        }
        public void Validation()
        {
            Console.Write("a = ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.Write("b = ");
            double b = Convert.ToDouble(Console.ReadLine());
            if ((a - (2 * b)) !=0)
            {
                double[] values = new double[2];
                values[0] = a;
                values[1] = b;
                Calculate(values);
            }
            else Console.WriteLine("this values a wrong");
        }
        protected double Calculate(double[] values)
        {
            double Result = (((2 * values[0]) - values[1]) * ((2 * values[1]) + values[0])) / (values[0] - (2 * values[1]));
            DisplayDaya(Result);
            return Result;
            
        }
        public void DisplayDaya(double Result)
        {
            Console.WriteLine(Result);
        }
    }
}
