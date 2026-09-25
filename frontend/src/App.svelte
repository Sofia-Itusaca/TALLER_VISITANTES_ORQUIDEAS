<script>
  import { onMount } from "svelte";

  let loading = true;
  let error = "";
  let dashboard = null;

  async function loadDashboard() {
    loading = true;
    error = "";

    try {
      const response = await fetch("/api/dashboard");

      if (!response.ok) {
        throw new Error("No se pudo obtener el pronóstico.");
      }

      dashboard = await response.json();
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  onMount(loadDashboard);

  function formatDate(dateString) {
    const date = new Date(`${dateString}T12:00:00`);
    return new Intl.DateTimeFormat("es-PE", {
      weekday: "short",
      day: "2-digit",
      month: "2-digit",
    }).format(date);
  }
</script>

<svelte:head>
  <title>Clima y visitantes — Las Orquídeas</title>
</svelte:head>

<main class="page">
  <header class="header">
    <div>
      <p class="eyebrow">Tingo María · Huánuco</p>
      <h1>Las Orquídeas</h1>
      <p class="subtitle">Predicción de visitantes según el clima</p>
    </div>

    <button onclick={loadDashboard}>Actualizar</button>
  </header>

  {#if loading}
    <section class="state">Consultando el clima...</section>
  {:else if error}
    <section class="state error">
      <strong>No se pudo cargar la información.</strong>
      <p>{error}</p>
      <button onclick={loadDashboard}>Intentar nuevamente</button>
    </section>
  {:else if dashboard}
    <section class="current">
      <div class="current-weather">
        <div>
          <p class="label">Clima actual</p>
          <h2>{dashboard.current.tempC}°C</h2>
          <p>{dashboard.current.description}</p>
          <small>Sensación térmica: {dashboard.current.feelsLikeC}°C · Humedad: {dashboard.current.humidity}%</small>
        </div>
        <img src={dashboard.current.icon} alt={dashboard.current.description} />
      </div>

      <div class="source">
        Fuente meteorológica: {dashboard.source}
      </div>
    </section>

    <section>
      <div class="section-title">
        <div>
          <p class="eyebrow">Pronóstico</p>
          <h2>Esta semana</h2>
        </div>
        <span>Visitantes estimados</span>
      </div>

      <div class="cards">
        {#each dashboard.days as day}
          <article class="card">
            <div class="date">{formatDate(day.date)}</div>
            <img src={day.icon} alt={day.description} />
            <h3>{day.description}</h3>

            <div class="temp">
              <strong>{day.maxTempC}°</strong>
              <span>máx.</span>
            </div>

            <div class="rain">
              🌧️ {day.rainChance}% · {day.rainMm} mm
            </div>

            <div class="prediction">
              <span>Visitantes esperados</span>
              <strong>{day.prediction.estimatedVisitors}</strong>
              <small>
                rango {day.prediction.rangeMin}–{day.prediction.rangeMax}
              </small>
            </div>
          </article>
        {/each}
      </div>
    </section>

    <section class="explanation">
      <h2>¿Cómo funciona la predicción?</h2>
      <p>
        El sistema relaciona la condición meteorológica pronosticada con un
        historial de visitantes. Los valores actuales son un modelo inicial
        de demostración y deben calibrarse con datos reales de Las Orquídeas.
      </p>
    </section>
  {/if}
</main>

<style>
  :global(*) {
    box-sizing: border-box;
  }

  :global(body) {
    margin: 0;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: #f5f7fb;
    color: #182230;
  }

  .page {
    max-width: 1250px;
    margin: 0 auto;
    padding: 38px 24px 60px;
  }

  .header {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    align-items: end;
    margin-bottom: 30px;
  }

  .eyebrow {
    text-transform: uppercase;
    letter-spacing: .12em;
    font-size: .72rem;
    font-weight: 800;
    color: #68758a;
    margin: 0 0 6px;
  }

  h1 {
    font-size: clamp(2rem, 4vw, 3.2rem);
    margin: 0;
  }

  .subtitle {
    color: #697587;
    margin: 8px 0 0;
  }

  button {
    border: 0;
    border-radius: 12px;
    padding: 12px 18px;
    font-weight: 800;
    cursor: pointer;
    background: #182230;
    color: white;
  }

  .current {
    background: white;
    border: 1px solid #e5e9ef;
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 34px;
    box-shadow: 0 12px 30px rgba(24, 34, 48, .06);
  }

  .current-weather {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .current-weather h2 {
    font-size: 4rem;
    margin: 5px 0;
  }

  .current-weather p {
    margin: 4px 0;
  }

  .current-weather small {
    color: #6d7888;
  }

  .current-weather img {
    width: 100px;
    height: 100px;
  }

  .source {
    border-top: 1px solid #edf0f4;
    margin-top: 18px;
    padding-top: 14px;
    color: #738094;
    font-size: .85rem;
  }

  .section-title {
    display: flex;
    align-items: end;
    justify-content: space-between;
    margin-bottom: 18px;
  }

  .section-title h2 {
    margin: 0;
  }

  .section-title > span {
    color: #697587;
    font-size: .9rem;
  }

  .cards {
    display: grid;
    grid-template-columns: repeat(7, minmax(140px, 1fr));
    gap: 12px;
  }

  .card {
    background: white;
    border: 1px solid #e5e9ef;
    border-radius: 18px;
    padding: 16px;
    min-height: 280px;
  }

  .date {
    text-transform: capitalize;
    color: #667286;
    font-weight: 800;
    font-size: .85rem;
  }

  .card img {
    width: 58px;
    height: 58px;
    margin: 10px 0 2px;
  }

  .card h3 {
    font-size: .9rem;
    min-height: 38px;
    margin: 0 0 12px;
  }

  .temp strong {
    font-size: 1.6rem;
  }

  .temp span,
  .rain {
    color: #748095;
    font-size: .8rem;
  }

  .rain {
    margin-top: 8px;
  }

  .prediction {
    border-top: 1px solid #edf0f4;
    margin-top: 14px;
    padding-top: 12px;
    display: grid;
    gap: 2px;
  }

  .prediction span,
  .prediction small {
    color: #68758a;
    font-size: .72rem;
  }

  .prediction strong {
    font-size: 1.8rem;
  }

  .explanation {
    margin-top: 34px;
    background: #eef6f0;
    border-radius: 20px;
    padding: 22px;
  }

  .explanation h2 {
    margin-top: 0;
  }

  .explanation p {
    color: #566575;
    line-height: 1.6;
  }

  .state {
    background: white;
    border-radius: 20px;
    padding: 40px;
    text-align: center;
  }

  .error {
    border: 1px solid #f0caca;
  }

  @media (max-width: 1000px) {
    .cards {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 600px) {
    .page {
      padding: 24px 14px 40px;
    }

    .header {
      align-items: start;
      flex-direction: column;
    }

    .current-weather h2 {
      font-size: 3rem;
    }

    .cards {
      grid-template-columns: 1fr;
    }
  }
</style>
