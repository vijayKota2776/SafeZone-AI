import axios from 'axios';

const api = axios.create({
    baseURL: 'http://your-backend-url', // Replace with your actual backend URL
});

export const startTracking = async (userId, startLocation, endLocation, batteryLevel) => {
    try {
        const response = await api.post('/start_tracking', {
            user_id: userId,
            start_location: startLocation,
            end_location: endLocation,
            battery_level: batteryLevel
        });
        console.log(response.data);
    } catch (error) {
        console.error("Error starting tracking:", error);
    }
};