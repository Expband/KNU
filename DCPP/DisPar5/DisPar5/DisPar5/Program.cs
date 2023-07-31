class MutexExample
{
    private static Mutex mutex = new Mutex();
    public const int IteratioCount = 3;
    private const int ThreadCount = 3;
    static void Main(string[] args)
    {
        for (int i = 0; i < ThreadCount; i++)
        {
            Thread thread = new Thread(new ThreadStart(Threading));
            thread.Name = String.Format("Thread{0}", i + 1);
            thread.Start();
        }
    }
    private static void Threading()
    {
        for (int i = 0; i < IteratioCount; i++)
        {
            DoSomeWork();
        }
    }
    private static void DoSomeWork()
    {
        Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} is waiting for mutex object");
        mutex.WaitOne();
        Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} got an mutex");
        Thread.Sleep( 1000 );
        Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} leave");
        mutex.ReleaseMutex();
        Console.WriteLine($"Thread {Thread.CurrentThread.ManagedThreadId} release the mutex");
    }
}