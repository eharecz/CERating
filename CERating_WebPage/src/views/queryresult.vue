<template>
  <div class="qr-box">
    <el-container>
      <!-- 背景图片 -->
      <!-- <div class="home-background"></div> -->
      <!-- 头部导航 -->
      <NavigationBar />
      <!-- 主体部分 -->
      <el-main>
        <div class="result-title">
          {{ this.comRating["bName"] }}公司{{
            this.comRating["bYear"]
          }}年碳排放评级
        </div>
        <div class="result-box">
          <div class="generalInfo-box">
            <div class="gb-title">碳评级为</div>
            <div class="gb-grade">
              {{ this.comRating["bGrade"] }}
            </div>
          </div>
          <div class="moreInfo-box">
            <div class="mb-title">详细碳排放数据</div>
            <div class="mb-index">
              <table class="pure-table">
                <thead>
                  <tr>
                    <th></th>
                    <th>Make</th>
                    <th>Model</th>
                    <th>Year</th>
                  </tr>
                </thead>

                <tbody>
                  <tr>
                    <td>1</td>
                    <td>Honda</td>
                    <td>Accord</td>
                    <td>2009</td>
                  </tr>

                  <tr>
                    <td>2</td>
                    <td>Toyota</td>
                    <td>Camry</td>
                    <td>2012</td>
                  </tr>

                  <tr>
                    <td>3</td>
                    <td>Hyundai</td>
                    <td>Elantra</td>
                    <td>2010</td>
                  </tr>

                  <tr>
                    <td>4</td>
                    <td>Hyundai</td>
                    <td>Elantra</td>
                    <td>2010</td>
                  </tr>
                  <tr>
                    <td>4</td>
                    <td>Hyundai</td>
                    <td>Elantra</td>
                    <td>2010</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="result-button" @click="getMoreInfo()">
          点击获得详细数据 >
        </div>
        <MessageBox class="mb"></MessageBox>
      </el-main>
      <!-- 底部信息 -->
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import Footer from "../components/Home/Footer.vue";
import MessageBox from "../components/MessageBox.vue";
import { postRequest } from "@/utils/api";

export default {
  name: "Home",
  components: { NavigationBar, MessageBox, Footer },
  mounted: function () {
    postRequest("http://127.0.0.1:8000/getEnterpriseRating/").then(
      (response) => {
        console.log(response);
        if (response.code === 0) {
          this.comRating["bName"] = response.data["bName"];
          this.comRating["bYear"] = response.data["bYear"];
          this.comRating["bGrade"] = response.data["bGrade"];
        }
      }
    );
  },
  data() {
    return {
      comRating: {
        bName: "花旗",
        bYear: "2022",
        bGrade: "S",
      },
      moreInfo: {},
      activeURL: 4,
    };
  },
  methods: {
    getMoreInfo() {
      document
        .getElementsByClassName("generalInfo-box")[0]
        .setAttribute("style", "width:20%");
      document
        .getElementsByClassName("gb-title")[0]
        .setAttribute("style", "margin: 50px 25px;");
      document
        .getElementsByClassName("gb-grade")[0]
        .setAttribute("style", "margin: 40px 0 0 60px;");
      document
        .getElementsByClassName("moreInfo-box")[0]
        .setAttribute("style", "display:flex");
      postRequest("http://127.0.0.1:8000/getEnterpriseRatingData/").then(
        (response) => {
          if (response.code === 0) {
            // 获得详细数据
          } else if (response.code === 1) {
            // 提示登录
          } else if (response.code === 2) {
            // 提示购买
          }
        }
      );
    },
  },
};
</script>

<style scoped>
.mb {
  position: absolute;
  top: 30%;
}
.qr-box {
  display: flex;
  justify-content: center;
}
.el-main {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.el-main .el-button {
  color: #ffccee;
  left: 50%;
  right: 30%;
  top: 40%;
  bottom: 60%;
}
.result-title {
  font-size: 1.8rem;
  text-shadow: 0 0 20px #02a8ba42;
  color: rgb(39, 156, 150);
  font-weight: bold;
}
.result-box {
  overflow: hidden;
  width: 60%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background: url("../assets/earth.png") no-repeat;
}
.gb-right {
  position: absolute;
  width: 60%;
  height: 350px;
}

.generalInfo-box {
  margin-top: 20px;
  width: 100%;
  height: 350px;
  box-shadow: rgb(0 0 0 / 20%) 0 0 25px;
  background-image: linear-gradient(
    -180deg,
    #02a8babe,
    #99dee5,
    rgba(0, 153, 255, 0.637)
  );
  border-radius: 20px;
  transition: all 0.25s;
}
.gb-title {
  margin: 50px 40px;
  font-size: 2rem;
  color: #fff;
  font-weight: bold;
  text-shadow: 0 0 20px #02a8babe;
}
.gb-grade {
  margin: 40px 0 0 70px;
  font-size: 5rem;
  color: #fff;
  font-weight: bold;
  text-shadow: 0 0 20px #02a8babe;
}
.moreInfo-box {
  margin-top: 20px;
  display: none;
  width: 75%;
  height: 350px;
  box-shadow: rgb(0 0 0 / 20%) 0 0 25px;
  background-image: linear-gradient(
    -180deg,
    rgb(252, 176, 46),
    rgb(250, 90, 11)
  );
  border-radius: 20px;
  transition: all 0.25s;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.mb-title {
  font-size: 1.5rem;
  color: #fff;
  font-weight: bold;
  text-shadow: 0 0 20px rgb(250, 90, 11);
}
.result-button {
  margin-top: 15px;
  margin-left: 43%;
  color: rgb(21, 149, 143);
  background-color: rgba(197, 197, 197, 0.685);
  width: 250px;
  height: 1.6rem;
  text-align: center;
  line-height: 1.6rem;
  box-shadow: rgb(0 0 0 / 20%) 0 0 25px;
  border-radius: 15px;
  cursor: pointer;
}
.el-footer {
  width: 100%;
  display: flex;
  justify-content: center;
  position: absolute;
  bottom: 0;
  padding-bottom: 12px;
  height: inherit;
}
.mb-index {
  margin-top: 30px;
  width: 80%;
  max-height: 300px;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}

td,
th {
  padding: 0;
}

.pure-table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
  empty-cells: show;
}

.pure-table caption {
  color: #99dde57c;
  font: italic 85%/1 arial, sans-serif;
  padding: 1em 0;
  text-align: center;
}

.pure-table td,
.pure-table th {
  border-width: 0 0 0 1px;
  font-size: 1.1rem;
  margin: 0;
  overflow: visible;
  padding: 0.5em 1em;
  color: #fff;
}

.pure-table thead {
  border-top: solid 1px;
  border-bottom: solid 1px;
  color: #fff;
  text-align: left;
  vertical-align: bottom;
}

.pure-table td {
  background-color: transparent;
}
</style>
