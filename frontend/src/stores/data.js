import { writable } from 'svelte/store';

export const data = writable(null);

export async function fetchData() {
    const response = await fetch('http://127.0.0.1:5000/api/data');
    const result = await response.json();
    data.set(result);
}
