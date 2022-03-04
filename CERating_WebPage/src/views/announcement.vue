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
          <p data-v-93c81e66="" class="md-title1 text-center">全方位解决你的商标问题</p>
          <div data-v-93c81e66="" class="help help1" style="padding: 89px 80px 50px;">
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">Q：商标更正有哪几种情况？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：商标更正有两种，一种是注册人或代理人的笔误，另一种是商标局在受理商标注册申请文件时，在录入或扫描过程中将个别内容弄错的。</p></div>
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">Q：商标更正和商标变更有什么区别？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：商标更正：是指在商标过程中，由于申请文件文字错误，不涉及商标、申请名称、地址等内容的更改。商标变更：商标核准注册后，商标注册人的名义、地址或其他注册事项发生变更的，应当向商标局申请办理相应变更手续。</p>
            </div>
            <div data-v-93c81e66=""><p data-v-93c81e66="" class="font-size-16 color-2B6BFF mt-5">
              Q：变更成功后，会下发新的商标注册证吗？</p>
              <p data-v-93c81e66="" class="font-size-16 list color-0D253E">
                A：商标局会下发《商标更正核准证明》，此文件须同原商标证书一并使用，不再下发新的证书。</p>
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
