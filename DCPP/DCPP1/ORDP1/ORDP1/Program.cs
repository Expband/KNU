using System;
using System.Threading;

namespace ORDP1
{
    public class ThreadingMethods
    {
        public int Value = 0;
        public void ThreadFirst()
        {
           Value = 1;
        }
        public void ThreadSecond()
        {
            Value = 2;
        }
        public void ThreadThird()
        {
            Value = 3;
        }
    }
    internal class Program
    {
        

        static void Main(string[] args)
        {
            ThreadingMethods threadingMethods = new ThreadingMethods();
            Thread thread = new Thread(new ThreadStart(threadingMethods.ThreadFirst));
            Thread thread2 = new Thread(new ThreadStart(threadingMethods.ThreadSecond));
            Thread thread3 = new Thread(new ThreadStart(threadingMethods.ThreadThird));
            thread.Start();
            thread2.Start();
            thread3.Start();
            Console.WriteLine(threadingMethods.Value);
            Console.Read();
        }
    }
}
