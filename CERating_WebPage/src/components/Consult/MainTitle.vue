<template>
  <div class="main-title">
    <div class="title">{{ title }}</div>
    <div class="bar"></div>
  </div>
</template>

<script>
export default {
  name: "MainTitle",
  data() {
    return {
      title: '图文资料'
    }
  }
}
</script>

<style scoped>
.main-title{
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.title{
  position: relative;
  left: 8%;
  top: 10px;
  font-size: 1.2em;
  font-weight: 700;
}
.title::before{
  position: absolute;
  content: '';
  left: -20px;
  width: 10px;
  height: 30px;
  border-radius: 2px;
  background-color: #01a3a4;
}
.bar{
  position: relative;
  left: 2%;
  width: 96%;
  height: 4px;
  background-color: gray;
  margin-top: 20px;
  border-radius: 24px;
}
</style>