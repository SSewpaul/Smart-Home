﻿using DeviceController;

class Program
{
    public static async Task Main(string[] args)
    {
        await Discovery.FindDevices();
    }
}