import { writable } from 'svelte/store';

export const data = writable(null);
export const mlData = writable(null);

export async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const result = await response.json();
        data.set(result);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

export async function fetchMl() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/ml', {
            method: 'POST'
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const result = await response.json();
        mlData.set(result);
    } catch (error) {
        console.error('Error fetching ML data:', error);
    }
}
