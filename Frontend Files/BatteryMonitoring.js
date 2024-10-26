import React, { useEffect, useState } from 'react';
import { BatteryManager } from 'react-native-battery-manager';
import { startTracking } from './api';

export default function BatteryMonitoring({ userId }) {
    const [batteryLevel, setBatteryLevel] = useState(null);
    const startLocation = "latitude,longitude"; // Replace with actual location data
    const endLocation = "latitude,longitude";   // Replace with actual destination

    useEffect(() => {
        const monitorBattery = async () => {
            const level = await BatteryManager.getBatteryLevel();
            setBatteryLevel(level);

            if (level < 0.2) {
                await startTracking(userId, startLocation, endLocation, level * 100);
            }
        };
        monitorBattery();

        // Set monitoring interval
        const intervalId = setInterval(monitorBattery, 60000); // Check every minute

        return () => clearInterval(intervalId);
    }, [userId]);

    return null;
}