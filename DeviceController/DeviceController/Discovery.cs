using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Zeroconf;

namespace DeviceController
{
    internal class Discovery
    {
        public static async Task FindDevices()
        {
            var availableDomains = await ZeroconfResolver.BrowseDomainsAsync();

            foreach (var availableDomain in availableDomains)
            {
                Console.WriteLine($"\n=== Discovering devices for: {availableDomain.Key} ===");

                IReadOnlyList<IZeroconfHost> hosts = await ZeroconfResolver.ResolveAsync(availableDomain.Key);

                foreach (var host in hosts) 
                {
                    Console.WriteLine($"Name:{host.DisplayName}");
                    Console.WriteLine($"IP Address:{host.IPAddress}\n");
                }                                                 
            }
        }
    }
}
