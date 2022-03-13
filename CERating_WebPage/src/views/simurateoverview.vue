<template>
  <div>
    <NavigationBar />
    <div class="main-wrapper">
      <div class="detail-box">
        <div class="img-box">
          <img :src="detail_box.pic_src" alt="skyBG">
        </div>
        <div class="display-box">
          <p style="margin-top: 80px">模拟评级详情</p>
          <a class="btn" href="simurate">模拟评级入口</a>
        </div>
      </div>

      <div class="detail-box">
        <div class="img-box">
          <img :src="detail_box.pic_src" alt="skyBG">
        </div>
        <div class="display-box">
          <p style="margin-top: 80px">模拟评级导航</p>
          <a class="btn" href="simurateguide">模拟评级导航入口</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import pic1 from '../assets/rating_pic1.jpg'
import NavigationBar from "../components/NavigationBar.vue";
export default {
  components: { NavigationBar},
  name: 'main',
  data() {
    return {
      detail_box:{
        pic_src: pic1
      }
    }
  }
}
</script>

<style scoped>
::-webkit-scrollbar {
  /*隐藏滚轮*/
  display: none;
}
#todo{
  width: 100%;
  height: 100%;
  border-radius: 6px;
  background-color: #ecf0f1;
}
.main-wrapper {
  /*组件主体*/
  height: 100vh;
  width: 50%;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 25%;
  overflow: auto;
}
.detail-box {
  position: relative;
  border: 2px solid #0984e3;
  border-radius: 8px;
  height: 49%;
  padding: 1%;
  margin-bottom: 15px;
  overflow: auto;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  box-shadow: 0 10px 20px rgb(0 0 0 / 20%);
  word-break: break-all;
}
.img-box{
  overflow: hidden;
  width: 100%;
  height: 70%;
}
.img-box img{
  width: 100%;
  height: 100%;
  border-radius: 6px;
}
.display-box{
  display: flex;
  flex-direction: column;
  height: 30%
}
.display-box p{
  position: relative;
  left: 50px;
  top: -40px;
  color: #54a0ff;
  font-size: 1.5em;
}
.display-box h2{
  position: relative;
  left: 50px;
  top: -10px;
  z-index: 1;
  font-size: 1.5em;
  font-weight: 500;
}
.display-box .btn{
  position: absolute;
  right: 70px;
  bottom: 20px;
  font-weight: 300;
  text-decoration: none;
}
.navi-box{
  position: relative;
  width: 90%;
  top: -50px;
  margin: auto;
  display: flex;
  flex-direction: column;
}
.navi-box .head-bar{
  position: relative;
  background-color: #54a0ff;
  height: 10px;
  width: 100%;
}
.navi-box .content-bar{
  position: relative;
  background-color: #ecf0f1;
  height: 20px;
  width: 100%;
  margin-top: 10px;
}

.btn{
  border-radius: 8px;
  border: 1px solid #3498db;
  color: #3498db;
  background: none;
  padding: 10px 20px;
  font-size: 20px;
  font-family: "montserrat",sans-serif;
  cursor: pointer;
  margin: 10px;
  transition: 0.8s;
  position: relative;
  overflow: hidden;
}
.btn:hover{
  color: #fff;
}
.btn::before{
  content: "";
  position: absolute;
  left: 0;
  width: 100%;
  height: 0;
  background: #3498db;
  z-index: -1;
  transition: 0.8s;
  bottom: 0;
  border-radius: 50% 50% 0 0;
}
.btn:hover::before{
  height: 180%;
}

.material-box {
  position: relative;
  border: 2px solid #0984e3;
  border-radius: 8px;
  height: 49%;
  padding: 1%;
  overflow: auto;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  box-shadow: 0 10px 20px rgb(0 0 0 / 20%);
  word-break: break-all;
}
</style>