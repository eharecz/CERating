<template>
  <div class="head-title">
    <h1>{{ title }}</h1>
    <p>{{ slogan }}</p>
  </div>
  <div class="main-wrapper">
    <MainTitle></MainTitle>
    <div class="content-wrapper">
      <div class="content-box">
        <div class="content-title">{{ content[0].title }}</div>
      </div>
      <div class="content-box">
        <div class="content-title">{{ content[1].title }}</div>
      </div>
      <div class="content-box">
        <div class="content-title">{{ content[2].title }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import MainTitle from "../components/Consult/MainTitle";
export default {
  name: 'ConsultOverview',
  components: {
    MainTitle
  },
  data() {
    return {
      title: '宣传语和宣传页',
      slogan: '此处可添加合适的宣传语',
      content: [{
        title: '政策解读'
      },{
        title: 'NEWS'
      },{
        title: 'NEWS'
      }]
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
.main-wrapper{
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
}
.content-box{
  width: 30%;
  margin: 3%;
  height: 800px;
  background-color: #7ed6df;
  display: flex;
  flex-direction: column;
}
.content-title{
  position: relative;
  color: white;
  font-size: 2em;
  font-weight: 700;
  text-align: center;
  top: 50px;
}
</style>