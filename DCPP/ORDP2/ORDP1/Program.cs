using System;
using System.Threading;


namespace ORDP1
{
    public class ThreadingMethods
    {
        public int Value = 0;
        public AutoResetEvent event1 = new AutoResetEvent(false);
        public AutoResetEvent event2 = new AutoResetEvent(false);
        public AutoResetEvent event3 = new AutoResetEvent(false);
        public void ThreadFirst()
        {
            WaitHandle.WaitAll(new WaitHandle[] { event2, event3 });
            Value = 1;
            event1.Set();
        }
        public void ThreadSecond()
        {
            Value = 2;
            event2.Set();
        }
        public void ThreadThird()
        {
            Value = 3;
            event3.Set();
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
            WaitHandle[] waitHandles = new WaitHandle[] { threadingMethods.event2 , threadingMethods.event3}; 
            thread.Start();
            thread2.Start();
            thread3.Start();
            WaitHandle.WaitAny(new WaitHandle[] {threadingMethods.event1});
            Console.WriteLine(threadingMethods.Value);
            Console.Read();
        }
    }
}
