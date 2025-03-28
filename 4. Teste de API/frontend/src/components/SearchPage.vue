<template>
    <div>
    <section class="filter">
        <h2>Resultados:</h2>
        <select v-model="selectedState" @change="filterResults">
            <option value="">UF</option>
            <option v-for="state in states" :key="state.id" :value="state.sigla">{{ state.nome }}</option>
        </select>
    </section>
    <main>
        <article class="notresult">
            <img src="../assets/no-results.png" class="no-results" />
            <h3>Nenhum resultado encontrado!</h3> 
        </article>
    </main>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selectedState: "",
            states: []
        };
    },
    created() {
        this.fetchStates();
    },
    methods: {
        async fetchStates() {
            try {
                const response = await fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados");
                this.states = await response.json();
            } catch (error) {
                console.error("Erro:", error);
            }
        },
    }
};
</script>

<style>
    h2{
        color: #A38989;
        font-family: "Inter", sans-serif;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        display: inline-block;
        margin-right: auto;
    }

    h3{
        font-family: "Inter", sans-serif;
        font-size: 13px;
        color:#A38989;
        font-weight: 500;

    }
    
    select{
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

    .no-results, .notresult{
        width: 200px;
        height: 200px;
        margin: 0 auto;
        margin-top:2em;
    }

</style>