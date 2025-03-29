export default {
    async fetchStates() {
        try {
            const response = await fetch("https://servicodados.ibge.gov.br/api/v1/localidades/estados");
            return await response.json();
        } catch (error) {
            console.error("Erro ao buscar estados:", error);
            return [];
        }
    },
    async fetchResults(searchTerm, selectedState) {
        try {
            const response = await fetch("http://127.0.0.1:8000/operadoras/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    termo: searchTerm,
                    uf: selectedState || null,
                    limite: 20
                })
            });

            if (!response.ok) {
                throw new Error(`Erro na API: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error("Erro ao buscar resultados:", error);
            return [];
        }
    }
};
