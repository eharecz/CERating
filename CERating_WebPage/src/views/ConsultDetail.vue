<template>
  <div class="head-title">
    <h1>{{ title }}</h1>
    <p>{{ slogan }}</p>
  </div>
  <div class="main-wrapper">
    <MainTitle></MainTitle>
    <div class="content-wrapper">
      <div class="content-box">图文</div>
      <div class="vertical-bar"></div>
      <div class="navi-box"></div>
    </div>
  </div>
</template>

<script>
import MainTitle from "../components/Consult/MainTitle";
export default {
  name: "ConsultDetail",
  components: {
    MainTitle
  },
  data() {
    return {
      title: '政策解读',
      slogan: '此处可添加内容'
    }
  }
}
</script>

<style scoped>
.head-title{
  background: url("../assets/consult_pic1.jpg")fixed center no-repeat;
  width: 100%;
  height: 60vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  position: absolute;
  left: 0;
  top: 0;
}
.head-title h1{
  position: relative;
  top: -20%;
  color: white;
}
.head-title p{
  position: relative;
  top: -20%;
  color: white;
}
.main-wrapper {
  overflow-x: hidden;
  position: absolute;
  width: 90%;
  left: 5%;
  top: 35%;
  background-color: #fff;
  border-radius: 12px;
}
.content-wrapper{
  display: flex;
  margin: 50px;
  align-content: center;
  justify-content: center;
}
.content-box{
  border: 2px solid #74b9ff;
  background-color: #bbbbbb;
  border-radius: 6px;
  width: 60%;
  height: 800px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.vertical-bar{
  height: 600px;
  width: 2px;
  background-color: #bbbbbb;
  margin: 20px;
  margin-left: 30px;
}
.navi-box{
  width: 30%;
  height: 700px;
  border: 2px solid #74b9ff;
  border-radius: 6px;
}
</style>