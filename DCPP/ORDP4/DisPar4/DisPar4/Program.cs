using System;
using System.Threading;
namespace SemaphoreDemo
{
    
     class Program
     {
        public static Semaphore semaphore = new Semaphore(2, 3);

        static void Main(string[] args)
        {
             for (int i = 1; i <= 10; i++)
             {
                 Thread threads = new Thread(PayLoad)
                 {
                     Name = "Thread " + i
                 };
                 threads.Start();
             }
             Console.ReadKey();
        }

        static void PayLoad()
        {

             Console.WriteLine(Thread.CurrentThread.Name + " Ready and waiting");
             try
             { 
                  semaphore.WaitOne();
                  Console.WriteLine("Success: " + Thread.CurrentThread.Name + " working");
                  Thread.Sleep(1000);
                  Console.WriteLine(Thread.CurrentThread.Name + "Done.");
             }
             finally
             {
                 semaphore.Release();
             }
        }
     }
}
