import React from 'react';
import { SafeAreaView } from 'react-native';
import BatteryMonitoring from './BatteryMonitoring';

export default function App() {
    return (
        <SafeAreaView>
            <BatteryMonitoring userId={1} />
        </SafeAreaView>
    );
}