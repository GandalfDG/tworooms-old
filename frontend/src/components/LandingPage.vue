<template>
<div>
    <h1>Landing Page</h1>
    <button @click="newGame" type="button" class="btn btn-primary">New Game</button>
    <button @click="joinGame" type="button" class="btn btn-outline-primary">Join Game</button>
</div>
</template>

<script>
export default {
  methods: {
    newGame () {
      this.$router.push('/new/')
    },
    joinGame () {
      this.$router.push('/join')
    }
  }
}
</script>
