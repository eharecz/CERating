<template>
  <div>
    <NavigationBar></NavigationBar>
    <div class="head-title">
      <h1>{{ title }}</h1>
      <p id = "slogan">{{ slogan }}</p>
    </div>
    <div class="main-wrapper">
      <MainTitle></MainTitle>
      <div class="content-wrapper">
        <a class="content-box" id="content-box-1" href="/consultdetail">
          <div class="content-title" >{{ content[0].title }}</div>
        </a>
        <a class="content-box" id="content-box-2" href="/consultdetail2">
          <div class="content-title" >{{ content[1].title }}</div>
        </a>
        <a class="content-box" id="content-box-3" href="/consultdetail3">
          <div class="content-title" id = "content-title-3">{{ content[2].title }}</div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import MainTitle from "../components/Consult/MainTitle";
import NavigationBar from '../components/NavigationBar.vue';
export default {
  name: 'ConsultOverview',
  components: {
    MainTitle,
    NavigationBar
  },
  data() {
    return {
      title: 'CERating',
      slogan: '专注于碳排放评级，让减排更简单',
      content: [{
        title: '碳达峰、碳中和的经济学解读'
      },{
        title: '新鲜出炉 | 中国企业碳中和社会责任研究报告'
      },{
        title: '启动！2022中国能源企业碳中和贡献力报告企业材料征集'
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
  /* position: absolute; */
  left: 0;
  /* top: 0; */
}
.head-title h1{
  position: relative;
  top: -40%;
  color: white;
  font-size: 2em;
}
.head-title p{
  position: relative;
  top: -35%;
  color: white;
  font-size: 2em;
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

#content-box-1 {
  background-image: url(../assets/title1_background.png);
  background-size:300px;
  background-repeat: no-repeat; 
  background-position: 18px 130px;
}
#content-box-2 {
  background-image: url(../assets/title2_background.png);
  background-size:310px 355px;
  background-repeat: no-repeat; 
  background-position: 0px 0px;
}
#content-box-3 {
  background-image: url(../assets/title3_background.png);
  background-size:313px 488px;
  background-repeat: no-repeat; 
  background-position: 0px 0px;
}


.content-box{
  width: 30%;
  margin: 3%;
  height: 350px;
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