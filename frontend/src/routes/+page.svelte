<script>
  import { onMount } from 'svelte';
  import { data, mlData, fetchData, fetchMl } from '../stores/data';

  onMount(() => {
      fetchData();
      fetchMl();
  });
</script>

<main>
  <h1>Hello SvelteKit with Flask!</h1>
  <p>{$data ? $data.message : 'Loading...'}</p>
  <h2>ML Data</h2>
  <p>{$mlData ? $mlData.message : 'Loading ML data...'}</p>
</main>