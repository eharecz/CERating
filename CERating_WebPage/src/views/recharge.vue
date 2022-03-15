<template>
  <div class="recharge">
    <NavigationBar />
    <div class="box">
      <div class="head">
        <p>订单确认</p>
      </div>
      <div style="height: 10px; background: #eee; margin: 20px 0 20px 0"></div>
      <div class="user-box">
        <div style="flex: 1; height: 80px">
          <p class="dec">用户信息</p>
        </div>
        <div
          style="display: flex; justify-content: space-between; height: 40px"
        >
          <div></div>
          <div>
            <p>当前剩余评级次数：{{ num }}</p>
          </div>
        </div>
      </div>
      <div class="money-box">
        <div style="display: flex; justify-content: space-between">
          <div
            style="display: flex; justify-content: space-between; width: 100%"
          >
            <div style="display: flex">
              <div class="">购买模拟评级数量</div>
              <div style="display: flex">
                <div @click="reduce" class="reduce">➖</div>
                <div>
                  <input placeholder="" v-model="purchaseNum" />
                </div>
                <div @click="plus" class="plus">➕</div>
              </div>
            </div>
            <div>应付金额：{{ sum }}</div>
          </div>
        </div>
        <div style="margin-top: 20px; display: flex">
          <!--          <el-radio v-model="radio" @change="radioBtn" v-for="v in 6" :label="v" :key="v">选项{{ v }}</el-radio>-->
          <p style="white-space: nowrap; margin-right: 30px">充值余额</p>
          <el-input
            id="rechargePrices"
            v-model="radio"
            @change="radioBtn"
            maxlength="10"
            type="number"
            placeholder="请输入"
          ></el-input>
        </div>
      </div>
      <div style="display: flex">
        <button
          class="el-button el-button--primary el-button--mini"
          type="button"
          data-v-fae5bece=""
          style="
            margin-top: 30px;
            --el-button-bg-color: #409eff;
            --el-button-border-color: #409eff;
            --el-button-hover-bg-color: rgb(102, 177, 255);
            --el-button-hover-border-color: rgb(102, 177, 255);
            --el-button-active-bg-color: rgb(58, 142, 230);
            --el-button-active-border-color: rgb(58, 142, 230);
          "
          @click="$router.go(-1)"
        >
          <!--v-if--><span>返回</span>
        </button>
        <button
          class="el-button el-button--primary el-button--mini"
          type="button"
          data-v-fae5bece=""
          style="
            margin-top: 30px;
            --el-button-bg-color: #409eff;
            --el-button-border-color: #409eff;
            --el-button-hover-bg-color: rgb(102, 177, 255);
            --el-button-hover-border-color: rgb(102, 177, 255);
            --el-button-active-bg-color: rgb(58, 142, 230);
            --el-button-active-border-color: rgb(58, 142, 230);
          "
          @click="submitOrder"
        >
          <!--v-if--><span class="">提交订单</span>
        </button>
      </div>
      <MessageBox
        class="mb"
        :fTitle="this.mb['mbTitle']"
        :fMessage="this.mb['mbMessage']"
        :fGoURL="this.mb['mbGoURL']"
        :fGoName="this.mb['mbGoName']"
        @changeMB="closeMB"
      ></MessageBox>
    </div>
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import MessageBox from "../components/MessageBox.vue";
import Global from "../components/Global.vue";

export default {
  components: { NavigationBar, MessageBox },
  name: "recharge",
  data() {
    return {
      num: 0,
      purchaseNum: 1,
      purchasePrise: 2.0,
      sum: 3,
      radio: 1,
      mb: {
        mbTitle: "温馨提示",
        mbMessage: "温馨提示内容",
        mbGoURL: "/",
        mbGoName: "主页",
      },
    };
  },
  methods: {
    // 关闭提示窗口
    closeMB(msg) {
      if (msg == false) {
        document
          .getElementsByClassName("mb")[0]
          .setAttribute("style", "display:none");
      }
    },
    plus() {
      this.purchaseNum++;
      this.sumData();
    },
    radioBtn() {
      this.sumData();
    },
    sumData() {
      this.sum = this.radio * 1 + this.purchasePrise * this.purchaseNum;
    },
    reduce() {
      if (this.purchaseNum > 0) {
        this.purchaseNum--;
      } else {
        alert("不能小于0");
      }
      this.sumData();
    },
    // 提交订单
    submitOrder() {
      let data = new FormData();
      data.append("simulateCount", this.purchaseNum);
      data.append("money", this.radio);
      data.append("email", localStorage.getItem("email")); 
      this.$axios
        .post(Global.address + "/api/enterprise_recharge/recharge2/",
          data,
          { emulateJSON: true, credentials: true })
        .then((response) => {
          if (response["code"] == "0") {
            // 正常
            this.mb["mbMessage"] = "充值成功！";
            this.mb["mbGoName"] = "确定";
            this.mb["mbGoURL"] = "-1";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (response["code"] == "1") {
            // 邮箱不存在
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "该邮箱不存在，请确认无误以后再进行操作！";
            this.mb["mbGoName"] = "确定";
            this.mb["mbGoURL"] = "-1";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (response["code"] == "2") {
            // 充值金额/次数有误
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "充值金额/次数有误！";
            this.mb["mbGoName"] = "修改";
            this.mb["mbGoURL"] = "-1";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          } else if (response["code"] == "4") {
            // 没有登录
            // this.mb["mbMessage"] = response["msg"]
            this.mb["mbMessage"] = "您还未登录，请先登录以后再进行操作！";
            this.mb["mbGoName"] = "去登陆";
            this.mb["mbGoURL"] = "/login";
            document
              .getElementsByClassName("mb")[0]
              .setAttribute("style", "display:block");
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          alert("数据获取失败,请刷新重试");
        });
    },
  },
  watch: {
    radio() {
      this.sumData();
    },
  },
};
</script>

<style scoped>
.mb {
  position: absolute;
  top: 30%;
  left: 50%;
  display: none;
}

.box {
  width: 750px;
  border: 1px solid #eee;
  height: 100%;
  margin: 0 auto;
  padding: 20px;
}

.head {
  line-height: 50px;
  font-size: 18px;
  font-weight: 500;
  border-bottom: 5px solid #00a1ef;
}

.user-box {
  border: 1px solid #00a1ef;
  height: 100px;
  border-radius: 5px;
  padding: 20px;
}

.money-box {
  cursor: pointer;
  padding: 30px;
  background: #fdffc7;
  margin-top: 30px;
}

.plus {
  margin-right: 20px;
}

.reduce {
  margin-left: 20px;
}

input {
  width: 30px;
  text-align: center;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
