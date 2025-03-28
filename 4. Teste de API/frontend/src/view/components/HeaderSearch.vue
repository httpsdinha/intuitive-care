<template>
    <div class="header-container">
        <img src="./assets/logo.png" class="logo" />
        <div class="search-container">
            <img src="./assets/search.png" class="search-icon" />
            <input type="text" placeholder="Buscar operadora..." class="search"/>
        </div>
    </div>
</template>

<style>
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px; 
    }

    .logo {
        width: 70px;
        height: 70px;
        margin-left: 0; 
        padding: 10px;
        margin-right: 1.5em;
    }

    .search {
        border-radius: 3px;
        background: #FFF;
        width: 500px;
        height: 25px;  
        border: none;
        padding-left: 35px; 
    }

    .search-container {
        display: flex;
        position: relative;
        align-items: center;
        
    }

    .search-icon {
        position: absolute;
        left: 10px;
        top: 50%;
        transform: translateY(-50%);
        width: 15px;
        height: 15px;
        cursor: pointer;
    }
</style>