<script>
    import { onMount } from 'svelte';
    import { data, fetchData } from '../stores/data';

    onMount(() => {
        fetchData();
    });
</script>

<main>
    <h1>Hello SvelteKit with Flask!</h1>
    <p>{$data ? $data.message : 'Loading...'}</p>
</main>
