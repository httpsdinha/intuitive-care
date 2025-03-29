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
            <article v-for="result in results" :key="result.ans" class="result">
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
export default {
    props: {
        searchTerm: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            selectedState: "",
            states: [],
            results: [] 
        };
    },
    watch: {
        searchTerm: "filterResults" // Refiltra os resultados ao alterar o termo de busca
    },
    created() {
        this.fetchStates();
        this.filterResults(); 
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
        async filterResults() {
            try {
                const response = await fetch("http://127.0.0.1:8000/operadoras/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        termo: this.searchTerm,
                        uf: this.selectedState,
                        limite: 20
                    })
                });
                this.results = await response.json();
            } catch (error) {
                console.error("Erro ao buscar resultados:", error);
            }
        }
    }
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
        display: block; /* Change layout to block */
    }

    .result {
        width: 100%; /* Make each article occupy full width */
        box-sizing: border-box;
        border: 1px solid #985260;
        border-radius: 5px;
        padding: 1rem;
        background-color: #f9f9f9;
        margin-bottom: 1rem; /* Add spacing between articles */
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