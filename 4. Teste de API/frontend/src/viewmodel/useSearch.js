import SearchModel from "../model/SearchModel";

export default {
    data() {
        return {
            searchTerm: "",
            selectedState: "",
            states: [],
            results: []
        };
    },
    async created() {
        this.states = await SearchModel.fetchStates();
        this.updateResults();
    },
    watch: {
        searchTerm: "updateResults",
        selectedState: "updateResults"
    },
    methods: {
        async updateResults() {
            this.results = await SearchModel.fetchResults(this.searchTerm, this.selectedState);
        }
    }
};
