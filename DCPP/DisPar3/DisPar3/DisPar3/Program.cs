int Value = 10;
Console.WriteLine(Value);
Console.WriteLine("Default value of value");
EventWaitHandle eventWait = new EventWaitHandle(false , EventResetMode.AutoReset);
Thread thread1 = new Thread(() =>
{
    Value = 100;
    Console.WriteLine(Value);
    Console.WriteLine("First thread finished");
    eventWait.Set();
});
Thread thread2 = new Thread(() =>
{
    eventWait.WaitOne();
    Value = 1000;
    Console.WriteLine(Value);
    Console.WriteLine("Second thread finished");
});
thread1.Start();
thread2.Start();
Console.Read();


