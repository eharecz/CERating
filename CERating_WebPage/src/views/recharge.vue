<template>
  <div class="recharge">
    <div class="box">
      <div class="head">
        <p>订单确认</p>
      </div>
      <div style="height: 10px;background:#eee;margin: 20px 0 20px 0"></div>
      <div class="user-box">
        <div style="flex: 1;height: 80px">
          <p class="dec">用户信息</p>
        </div>
        <div style="display:flex;justify-content: space-between;height: 40px;">
          <div></div>
          <div>
            <p>当前剩余评级次数：{{ num }}</p>
          </div>
        </div>
      </div>
      <div class="money-box">
        <div style="  display: flex;
  justify-content: space-between;">
          <div style="display: flex;justify-content: space-between;width: 100%;">
            <div style="display:flex;">
              <div class="">购买模拟评级数量</div>
              <div style="display:flex;">
                <div @click="reduce" class="reduce">➖</div>
                <div>
                  <input placeholder="" v-model="purchaseNum"/>
                </div>
                <div @click="plus" class="plus">➕</div>
              </div>
            </div>
            <div>
              应付金额：{{ sum }}
            </div>
          </div>
        </div>
        <div style="margin-top: 20px;display:flex;">
<!--          <el-radio v-model="radio" @change="radioBtn" v-for="v in 6" :label="v" :key="v">选项{{ v }}</el-radio>-->
          <p style="white-space:nowrap;margin-right: 30px;">充值余额</p><el-input v-model="radio" @change="radioBtn" maxlength="10" type="number" placeholder="请输入"></el-input>

        </div>
      </div>
      <div style="display:flex;">
        <button class="el-button el-button--primary el-button--mini" type="button" data-v-fae5bece=""
                style="margin-top: 30px;--el-button-bg-color:#409eff; --el-button-border-color:#409eff; --el-button-hover-bg-color:rgb(102, 177, 255); --el-button-hover-border-color:rgb(102, 177, 255); --el-button-active-bg-color:rgb(58, 142, 230); --el-button-active-border-color:rgb(58, 142, 230);">
          <!--v-if--><span class="">返回</span></button>
        <button class="el-button el-button--primary el-button--mini" type="button" data-v-fae5bece=""
                style="margin-top: 30px;--el-button-bg-color:#409eff; --el-button-border-color:#409eff; --el-button-hover-bg-color:rgb(102, 177, 255); --el-button-hover-border-color:rgb(102, 177, 255); --el-button-active-bg-color:rgb(58, 142, 230); --el-button-active-border-color:rgb(58, 142, 230);">
          <!--v-if--><span class="">提交订单</span></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "recharge",
  data() {
    return {
      num: 0,
      purchaseNum: 1,
      purchasePrise: 2.0,
      sum: 0,
      radio: 1
    }
  },
  methods: {
    plus() {
      this.purchaseNum++;
      this.sumData();
    },
    radioBtn() {
      this.sumData();
    },
    sumData() {
      this.sum = this.radio * 1 + this.purchasePrise * this.purchaseNum
    },
    reduce() {
      if (this.purchaseNum > 0) {
        this.purchaseNum--
      } else {
        alert('不能小于0')
      }
      this.sumData();
    }
  },
  watch:{
    radio() {
      this.sumData();
    }
  }
}
</script>

<style scoped>
.recharge {
  height: calc(100vh - 120px);
  padding: 40px;
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
