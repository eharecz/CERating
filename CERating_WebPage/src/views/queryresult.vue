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
                    <th>序号</th>
                    <th>指标</th>
                    <th>数据</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(data, index, i) in this.moreInfo" :key="index">
                    <td>{{ i + 1 }}</td>
                    <td>{{ index }}</td>
                    <td>{{ data }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="result-button" @click="getMoreInfo()">
          点击获得详细数据 >
        </div>
        <MessageBox
          class="mb"
          :fTitle="this.mb['mbTitle']"
          :fMessage="this.mb['mbMessage']"
          :fGoURL="this.mb['mbGoURL']"
          :fGoName="this.mb['mbGoName']"
          @changeMB="closeMB"
          @mbfun="purchase"
        ></MessageBox>
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

export default {
  name: "Home",
  components: { NavigationBar, MessageBox, Footer },
  mounted: function () {
    this.comRating.bName = this.$route.query["enterprise"];
    this.comRating.bYear = this.$route.query["year"];
    let data = new FormData();
    data.append("name", this.comRating.bName);
    this.$axios
      .post(
        this.$Global.address + "/api/enterprise_simurate/getEnterpriseRating/",
        data
      )
      .then((response) => {
        this.comRating.bGrade = response["rate"];
      })
      .catch((error) => {
        console.log(error);
        alert("数据获取失败,请刷新重试");
      });
  },
  data() {
    return {
      comRating: {
        bName: "花旗",
        bYear: "2022",
        bGrade: "",
      },
      moreInfo: {},
      activeURL: 4,
      mb: {
        mbTitle: "温馨提示",
        mbMessage: "温馨提示内容",
        mbGoURL: "/",
        mbGoName: "主页",
      },
    };
  },
  methods: {
    // 购买相应企业数据
    purchase() {
      let data = new FormData();
      data.append("name", this.comRating.bName); // 购买公司的名字
      data.append("email", localStorage.getItem("email"));
      console.log(localStorage.getItem("email"));
      this.$axios
        .post(
          this.$Global.address + "/api/enterprise_simurate/purchaseRatingData/",
          data,
          { emulateJSON: true, credentials: true }
        )
        .then((res) => {
          if (res["code"] == 0) {
            this.mb["mbMessage"] = "购买成功，感谢您的支持！";
            this.mb["mbGoName"] = "确定";
            this.mb["mbGoURL"] = "-1";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (res["code"] == 1) {
            // 没有登录
            this.mb["mbMessage"] = "您还未登录，请先登录以后再进行操作！";
            this.mb["mbGoName"] = "去登陆";
            this.mb["mbGoURL"] = "/login";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (res["code"] == 2) {
            // 余额不足
            this.mb["mbMessage"] = "余额不足，请先进行充值！";
            this.mb["mbGoName"] = "充值";
            this.mb["mbGoURL"] = "/recharge";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          }
        });
    },
    // 关闭提示窗口
    closeMB(msg) {
      if (msg == false) {
        document
          .getElementsByClassName("mb")[0]
          .setAttribute("style", "display:none");
      }
    },
    getMoreInfo() {
      let data = new FormData();
      data.append("name", this.comRating.bName);
      data.append("email", localStorage.getItem("email"));
      console.log(localStorage.getItem("email"));
      console.log(this.$Global.address)
      this.$axios
        .post(
          this.$Global.address + "/api/enterprise_simurate/getEnterpriseRatingData/",
          data,
          { emulateJSON: true, credentials: true }
        )
        .then((response) => {
          if (response["code"] == "0") {
            // 正常
            this.moreInfo = response["data"];
            console.log(response["data"]);
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
          } else if (response["code"] == "1") {
            // 未登录
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "您还未登录，请先登录以后再进行操作！";
            this.mb["mbGoName"] = "去登陆";
            this.mb["mbGoURL"] = "/login";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (response["code"] == "2") {
            // 企业不存在
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "该企业不存在，请确认企业名称等是否正确！";
            this.mb["mbGoName"] = "去登陆";
            this.mb["mbGoURL"] = "-1";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (response["code"] == "3") {
            // 当前用户并没有购买这个企业的信息
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "抱歉，您未购买相应的数据，请先购买！";
            this.mb["mbGoName"] = "购买";
            this.mb["mbGoURL"] = "-2"; // -2 表示进行相应post操作
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          }
          // console.log(response);
        })
        .catch((error) => {
          console.log(error);
          alert("数据获取失败,请刷新重试");
        });
    },
  },
};
</script>

<style scoped>
.mb {
  position: absolute;
  top: 30%;
  display: none;
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
  min-height: 450px;
}

.generalInfo-box {
  margin-top: 20px;
  width: 100%;
  min-height: 450px;
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
  min-height: 450px;
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
  min-width: 40px;
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
