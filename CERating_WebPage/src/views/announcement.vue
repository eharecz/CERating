<template>
  <div class="announcement">
    <div class="box">
      <!--      <div class="title-box">
              <p>一线大厂在线讲解</p>
            </div>
            <div>
              <div class="title">
                <p>1，百度在线网络技术（北京）有限公司介绍：</p>
              </div>
              <div class="dec">
                <p>百度在线网络技术（北京）有限公司，是中国大型互联网公司百度的全称 [1]
                  。百度（Nasdaq简称：BIDU）是全球最大的中文搜索引擎，2000年1月由李彦宏、徐勇两人创立于北京中关村，致力于向人们提供“简单，可依赖”的信息获取方式。“百度”二字源于中国宋朝词人辛弃疾的《青玉案·元夕》词句“众里寻他千百度”，象征着百度对中文信息检索技术的执著追求。</p>
              </div>
            </div>-->
      <div data-v-93c81e66="" class="overflow-hidden mt-20" style="">
        <div data-v-93c81e66="" class="overflow-hidden pb-5" style="background: rgba(255, 255, 255, .7)">
          <div class="logo-box">
            <img src="../assets/logo.png" alt=""/>
            <span>CERating</span>
          </div>

          <p data-v-93c81e66=""
             class="md-title text-center">帮助中心</p>
          <p data-v-93c81e66="" class="md-title1 text-center">解决您在使用过程中遇到的问题</p>
          <div data-v-93c81e66="" class="help help1" style="padding: 89px 80px 50px;">
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">Q：评级最终结果与设想（模拟）出现很大差别该如何做？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：可以向官方申请成绩结果审核，官网将会在2个工作日内给出审核结果报告，除非真实有误否则不会做出调整。</p></div>
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">Q：评级结果是否提供纸质印章版？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：可以提供带有网站专属印章的纸质版报告，企业可以联系我们的官方人员，并正确填入邮寄地址，我们将及时为您寄出报告，需要您注意运费到付。</p>
            </div>
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">
              Q：网页是否存在功能设限？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：网页的所有功能企业都可以免费（付费）的情况下多次浏览，若存在非法盗取的情况后台将会予以监视封锁账号。</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "announcement"
}
</script>

<style scoped>
.announcement {
  /*background: #eee;*/
  background: url("../assets/login_background.jpg") no-repeat;
  background-size: cover;
}

.box {
  width: 1200px;
  margin: 0 auto;
  text-align: left;
  min-height: 100vh;
}

.box .title-box {
  width: 70%;
  padding: 50px;
  border-radius: 15px;
  background: #fff;
  margin: 0 auto 50px;
  font-size: 28px;
  color: #eb0019;
  text-align: center;
  font-weight: 600;
}


.box .title {
  color: #cc3c50;
  font-size: 18px;
  font-weight: 600;
}

.md-title {
  font-size: 32px;
  font-weight: 400;
  color: #151515;
  text-align: center;
  padding-top: 40px;
}

.background-FFFFFF {
  background: #fff;
}

.md-title1 {
  font-size: 16px;
  font-weight: 400;
  color: #888;
  text-align: center;
}

.color-2B6BFF {
  color: #2b6bff;
}

.font-size-16 {
  font-size: 16px;
}

.list {
  line-height: 40px;
  margin-bottom: 20px;
}

.logo-box {
  position: fixed;
  left: 7%;
  top: 10%;
  color: #fff;
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.logo-box span {
  margin-left: 10px;
  font-size: 30px;
  font-family: Times;
}

.logo-box img {
  height: 50px;
  width: 50px;
}
</style>
