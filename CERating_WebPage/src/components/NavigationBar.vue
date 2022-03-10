<template>
  <div>
    <div class="top-bar">
      <div class="top-earth">
        <img src="../assets/topimg-earth.jpg" alt="leaf" />
        <div class="top-text">
          <span class="top-text-en">Carbon emissions rating query</span>
          <span class="top-text-cn">碳排放评级查询</span>
        </div>
      </div>
      <div class="top-leaf">
        <img src="../assets/topimg-leaf.jpg" alt="leaf" />
      </div>
    </div>
    <div class="nav-bar">
      <!-- LOGO -->
      <div class="logo">
        <a href="/consultoverview" @click="activeURL = 0"
          ><img src="../assets/logo.png" alt="logo"
        /></a>
      </div>
      <!-- 菜单栏 -->
      <div class="menu">
        <!-- <div class="menu-item" :key="0">
            <a href="/" @click="activeURL = 0">Logo</a>
            <div
                class="menu-underline"
                :class="{ activedPage: activeURL == 0 }"
            ></div>
          </div> -->
        <div class="menu-item" :key="1">
          <a href="/consultoverview" @click="activeURL = 1">首页</a>
          <div
            class="menu-underline"
            :class="{ activedPage: activeURL == 1 }"
          ></div>
        </div>
        <div class="menu-item" :key="2">
          <a href="/bulletin" @click="activeURL = 2">公告</a>
          <div
            class="menu-underline"
            :class="{ activedPage: activeURL == 2 }"
          ></div>
        </div>
        <div class="menu-item" :key="3">
          <a href="/announcement" @click="activeURL = 3">帮助</a>
          <div
            class="menu-underline"
            :class="{ activedPage: activeURL == 3 }"
          ></div>
        </div>
        <div class="menu-item" :key="4">
          <a href="/simurateoverview" @click="activeURL = 4">模拟评级</a>
          <div
            class="menu-underline"
            :class="{ activedPage: activeURL == 4 }"
          ></div>
        </div>
      </div>
      <!-- 个人 -->
      <div class="person">
        <div class="person-img">
          <a href="/Login" @click="activeURL = 0"
            ><img src="../assets/person.png" alt=""
          /></a>
        </div>
        <!-- TODO 点击头像下拉框 -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.top-bar {
  width: 100%;
  height: 65px;
  display: flex;
  justify-content: center;
  text-align: center;
  /* opacity: 0; */
  transition: all 0.5s ease;
  background-color: rgb(255, 255, 255);
}
.top-earth {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.top-earth .top-text {
  display: flex;
  flex-direction: column;
}
.top-text .top-text-en {
  color: rgb(2, 169, 185);
  font-size: 0.6rem;
  font-weight: bold;
}
.top-text .top-text-cn {
  font-size: 1.6rem;
  font-weight: bold;
}
.top-earth img {
  height: 80%;
}
.top-leaf{
  height: 65px;
  position: absolute;
  right: 0;
}
.top-leaf img {
  height: 100%;
}
.nav-bar {
  width: 100%;
  height: 35px;
  padding: 5px 0;
  display: flex;
  justify-content: space-between;
  text-align: center;
  /* opacity: 0; */
  transition: all 0.5s ease;
  background-color: rgb(0, 153, 255);
}
/*.nav-bar:hover {*/
/*  padding-top: 15px;*/
/*  opacity: 1;*/
/*}*/
.nav-bar .logo {
  padding-left: 10px;
  height: 35px;
}
.nav-bar .logo img {
  height: 100%;
}
.nav-bar .menu {
  width: 30%;
  height: 35px;
  left: 35%;
  position: absolute;
  display: flex;
  justify-content: space-between;
  line-height: 35px; /* 垂直居中 */
}
.nav-bar .menu-item {
  width: 64px;
}
.nav-bar .menu-item .menu-underline {
  width: 10px;
  height: 5px;
  background-color: #ffffffcc;
  border-radius: 5px;
  margin-left: calc(50% - 5px); /* 注意空格，否则无效！ */
  transform: scaleX(0);
  transition: transform 0.3s ease;
}
.nav-bar .menu-underline.activedPage {
  transform: scaleX(1);
}
.nav-bar .menu-item a {
  color: #ffffffcc;
  text-decoration: none;
}
.nav-bar .menu-item a:hover {
  color: #fff;
}
.person {
  padding-right: 10px;
  display: flex;
  justify-content: right;
}
.person a {
  color: #fff;
}
.person .person-img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  padding-left: 10px;
  /* border: 4px solid rgba(255, 255, 255, 0.3); */
  overflow: hidden;
}
.person .person-img img {
  width: 100%;
  height: 100%;
  color: #fff;
  border-radius: 50%;
  object-fit: cover;
}
.person .settings {
  padding: 0;
}
</style>
