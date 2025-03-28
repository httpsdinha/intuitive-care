<template>
<div>
  <header>
    <HeaderSearch/>
  </header>
  <main>
    <SearchPage/>
  </main>
</div>
</template>

<script>
import HeaderSearch from './components/HeaderSearch.vue'
import SearchPage from './components/SearchPage.vue'

export default {
  name: 'App',
  components: {
    HeaderSearch,
    SearchPage,
  }
}
</script>

<style>
  body{
    margin: 0;
    margin-right: 5em;
  }
  header {
    background: linear-gradient(91deg, #653740 25.84%, #985260 100%);

;
    padding: 10px;
    box-shadow: black 0px 0.2px 20px;
  }

  main {
    padding: 1em;
    padding-left: 10em;
    padding-right: 10em;
  }
</style>
