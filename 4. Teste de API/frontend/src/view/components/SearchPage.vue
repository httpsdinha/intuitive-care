<template>
  <div>
    <section class="filter">
      <h2>Primeiros 20 Resultados:</h2>
      <select v-model="selectedState">
        <option value="">UF</option>
        <option v-for="state in states" :key="state.id" :value="state.sigla">{{ state.nome }}</option>
      </select>
    </section>
    <main>
      <NotFound v-if="results.length === 0" />
      <article v-else v-for="result in results" :key="result.ans" class="result">
        <h3>{{ result.Nome_Fantasia }}</h3>
        <p>Modalidade: {{ result.Modalidade }}</p>
        <p>Logradouro: {{ result.Logradouro }}</p>
        <p>Telefone: {{ result.telefone }}</p>
        <p>{{ result.Cidade }} - {{ result.UF }}</p>
      </article>
    </main>
  </div>
</template>

<script>
import NotFound from "./NotFound.vue";
import useSearch from "../../viewmodel/useSearch";

export default {
  props: {
    searchTerm: {
      type: String,
      required: true
    }
  },
  components: {
    NotFound
  },
  mixins: [useSearch]
};
</script>

<style>
    h2 {
        color: #A38989;
        font-family: "Inter", sans-serif;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        display: inline-block;
        margin-right: auto;
    }

    h3 {
        font-family: "Inter", sans-serif;
        font-size: 13px;
        color: #653740;
        font-weight: 500;
    }

    select {
        border-radius: 3px;
        border: 1px solid #985260;
        background: transparent;
        width: 8rem;
        height: 2rem;
        display: inline-block;
        vertical-align: middle;
        margin-left: auto;
    }

    .filter {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .loc{
        color: #985260;
    }
    
    main {
        display: block;
    }

    .result {
        width: 100%; 
        box-sizing: border-box;
        border: 1px solid #985260;
        border-radius: 5px;
        padding: 1rem;
        background-color: #f9f9f9;
        margin-bottom: 1rem; 
    }

    .result h3 {
        margin: 0 0 0.5rem 0;
    }

    .result p {
        margin: 0.2rem 0;
        font-size: 12px;
        color: #555;
    }

</style>