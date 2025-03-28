<template>
  <header>
    <HeaderSearch/>
  </header>
  <main>
    <HelloWorld/>
  </main>
    
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import HeaderSearch from './components/HeaderSearch.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    HeaderSearch
  }
}
</script>

<style>
  body{
    margin: 0;
  }
  header {
    background: linear-gradient(91deg, #653740 25.84%, #985260 100%);

;
    padding: 10px;
    box-shadow: black 0px 0.2px 20px;
  }

</style>
