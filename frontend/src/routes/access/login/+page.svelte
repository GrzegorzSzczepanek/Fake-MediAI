<script lang="ts">
    let email = '';
    let password = '';
    let message = '';

    const login = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });
            const result = await response.json();
            message = result.message || result.error;
        } catch (error) {
            message = 'An error occurred during login';
        }
    };
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
    <h1 class="text-2xl font-bold mb-4">Login</h1>
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" on:submit|preventDefault={login}>
        <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">
                Email:
                <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="email" bind:value={email} />
            </label>
        </div>
        <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2">
                Password:
                <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" type="password" bind:value={password} />
            </label>
        </div>
        <div class="flex items-center justify-between">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Login</button>
        </div>
    </form>
    {#if message}
        <p class="text-red-500 text-xs italic">{message}</p>
    {/if}
</main>
