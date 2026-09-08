<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/Bc2ppDu7HewdycFybn6C2p5tCxweoGMEVfo272MzeBpQ44qzQFhujPQ1B1v45x1mcTjfE-NGoMlVtoXybXPZmmGrhAjOYgXrjUBBWMUXSuD47oRVIoh3OlJNTchGjfDu0jYRQscJgpThC2CU4ObzozF3omDk9HLvSbz4XZCXj5jkpFYzGDIvltL4DUuSQNAkvdR9NZ10rFMknttZC_ysAO10REmx-BHwnbNpWi8U1Hy7hemOhlaxJB6GCuFb76C1_5Vs8Ysg9aAtvHrp8TfKpB5psn11jSzGhll5lkmOUrSzqSHpWsy4cxf57G32eU1fHnVZP-wxZWrMwoY3Tr9OEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فلافل قسطی ام اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/funhiphop/83140" target="_blank">📅 12:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=rmXbL7XDXN1EoNG8ftHmumuLYPoeu0YZA0sgKibtJynyP4x0jwiHopKdCTuMcfNyaXgdPPiLiDAO3vXqu8b3jZmYOU_EOzruroxAfqOOMJZQ3BC5fARptolqSuGZgIbXdkCiTkP9azEOkoq-sy3W-gw5cMR7WfjCCG6Iv7RIjiRPRuUcBGX1HX1cwfQyMh24lf2arTOmwBNVDxoE1fotd35LMq1ORacvX0vf71ot23SpzQBP6OXFhDvtnu7VjjSOMIn0hH_wYFNLGOfQvO_8T9p2dCeXMFEvwDh4Iot_VSH70YhBHRFhHot5bfVsVoi6pdyjVwwQuaKYc_eagGlgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=rmXbL7XDXN1EoNG8ftHmumuLYPoeu0YZA0sgKibtJynyP4x0jwiHopKdCTuMcfNyaXgdPPiLiDAO3vXqu8b3jZmYOU_EOzruroxAfqOOMJZQ3BC5fARptolqSuGZgIbXdkCiTkP9azEOkoq-sy3W-gw5cMR7WfjCCG6Iv7RIjiRPRuUcBGX1HX1cwfQyMh24lf2arTOmwBNVDxoE1fotd35LMq1ORacvX0vf71ot23SpzQBP6OXFhDvtnu7VjjSOMIn0hH_wYFNLGOfQvO_8T9p2dCeXMFEvwDh4Iot_VSH70YhBHRFhHot5bfVsVoi6pdyjVwwQuaKYc_eagGlgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/83139" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور: فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند. در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم. تحریم فناوری و فیلترینگ در فضای مجازی نتیجه‌بخش نیست.باید با فرهنگ غنی اسلامی و ایرانی در اینترنت فعالیت کنیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/83138" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83137">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/83137" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVpaYcEnLhZ7TkKPcx72ShFoOIsZxqXYJL5aj9vdWyzIUphFMqIjUlQ0voLPlAOchB8uVybf5UKTGP2lWggJmtoZpuJJtsgTDMH4Z33GOSGqxJR-_EsaI1oXjRikPgbioc8qnbkXPKqRlTd3ax23Ry8peUA_lVge5cpwhjOyCHnJoZ74QC9Tay9MO8g9Hqt7MeSTElg7130jSu3VLg8OMtnvIxtKf64h0O51qWMJqfW3np8eI6JUtJ6MuIO6pHjA8rSESMQQtIJMiF1l5olm8lT5PZVM2hW5bth95QxsUu5DX1wEbsBPnkI1HBF_vfTTHcsAy8U6qBucnmalYXWVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r17
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/83136" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40085684e0.mp4?token=plGjL_2do0YLqSWvqemRsYurycBpkb1Dofvtjlee884pwBNzr9N_XCmb45lEwp8c65hUk-PvNue-sVK_DBuILL_RX3QVZ019GOotyQWfMkqS6x1i1cHBuczT9bnIkfPQ3CEMA6zpY61GV51M31u9yPfttn3XHVVC5cozg8S3khDAL19DYF-MK7_ZSjNNhJs6iRPuawXrc1w_aVZk6Q_8K8SfUvJH7i5z10cmmRczIR456NoagIPFA634DhxJ1N7snX5hu2NFg4F8f7_OehE7plqZbZcAV6yqqjGxNQ9BRj0x_jkVGnmdL1ZmVYG8rfaamu9pKLpe2WNpPBMMhO5s6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40085684e0.mp4?token=plGjL_2do0YLqSWvqemRsYurycBpkb1Dofvtjlee884pwBNzr9N_XCmb45lEwp8c65hUk-PvNue-sVK_DBuILL_RX3QVZ019GOotyQWfMkqS6x1i1cHBuczT9bnIkfPQ3CEMA6zpY61GV51M31u9yPfttn3XHVVC5cozg8S3khDAL19DYF-MK7_ZSjNNhJs6iRPuawXrc1w_aVZk6Q_8K8SfUvJH7i5z10cmmRczIR456NoagIPFA634DhxJ1N7snX5hu2NFg4F8f7_OehE7plqZbZcAV6yqqjGxNQ9BRj0x_jkVGnmdL1ZmVYG8rfaamu9pKLpe2WNpPBMMhO5s6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بخدا این چیزا تو اکسپلور من میاد ناخوداگاه یاد رضا پیشرو میوفتم وگرنه دلیل دیگه ای نداره که اینجا پستشون میکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/83135" target="_blank">📅 09:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X86GWIi_cUndR3IZ101mPLpj_y60yvmEOm4v5HhLyx3JvkA6EURKel5AgYho6QNFNV5Y0-TOXfbgm9ChfyP4dQG988kqO3p191vnQ4HAkeCPywB0XASp344yBNFAU17vlfqW7pH0NGOptvZyxOK9VBDApMNmBgfO8W1nw6uxfvdci_kuy11DKrUp5syzOB7FvG2C6ntpM-CMj_sPHfB3ccRKK4sd7TEB-UFQcDIq0fi7_c5S0P4fVhK0Wyl21GkVYV7ozi2EhkuV5w20SddEuU995SR5ofo1D8TUa1Jp9YW23ghcEpsI22PVLJxVMqhjncYIBO6D8nPS7v7tKt_1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/83134" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83131">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بنظرم که خلوت کنید آقای خمسه اس</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83131" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83130">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=jIY79HDI4O3et4mcSiGP_GheULuIvndl8uEa4EIKre35LmzmErtHn79dOMTUDd3b_5yOemcZlZIkhQZ2_pMhjnOamiGUMjBBepjtIITOpQEpl_m_HmNqUvu3hpoz6o-SIuH8Skbpgli5ZLQaSegjjKHP3fHV9VWTFYSk5yeTtgbK7xbBZ3e6uBI8L4r9GCyu28QykAMaIC2d4yBY6U8A3PVukmNbFTsRUvKwYYbUEWozpvjX227C5Ype_y58QpS1HdmMsG0AN_4JbqB7Zq26NFv85jrnav7mP1s_qQ-Xm98hFF75crBxCwz1r8651aWGaz3s_QybmuiNQmiU1TWW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=jIY79HDI4O3et4mcSiGP_GheULuIvndl8uEa4EIKre35LmzmErtHn79dOMTUDd3b_5yOemcZlZIkhQZ2_pMhjnOamiGUMjBBepjtIITOpQEpl_m_HmNqUvu3hpoz6o-SIuH8Skbpgli5ZLQaSegjjKHP3fHV9VWTFYSk5yeTtgbK7xbBZ3e6uBI8L4r9GCyu28QykAMaIC2d4yBY6U8A3PVukmNbFTsRUvKwYYbUEWozpvjX227C5Ype_y58QpS1HdmMsG0AN_4JbqB7Zq26NFv85jrnav7mP1s_qQ-Xm98hFF75crBxCwz1r8651aWGaz3s_QybmuiNQmiU1TWW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83130" target="_blank">📅 04:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83129">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83129" target="_blank">📅 04:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83128">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=kRuregGYE9LrBEaXHXyhalivbYyyNm8hvVF1Ke0j05CuYcITUwWOciVHivQyoyrVjOi4pOTy7KNXwW2Pw0v-tRJYlZEW_bywUpYRW9_XUIYtjheiAtBbyIUY5k2QilyU457JdTvQC-csbxKyfYz_HpJTjzKWoSaDX_Cy5E4GQWhWG4OsXux_HOVG0cd0Y6SAiUgPRwfRBejj2FaYYk9CVrMhlJaSLkK2dUzpfUICVoHsE7V736XgpTyowR64Gac8tV2N2Z-KfaDF98rf4Ok1bZjGvc-VG5GTzhNG_hSiMNGxbRQ9ZINdw5_l9W1UdltJDpU6pHtw3snHVDuHAyDyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=kRuregGYE9LrBEaXHXyhalivbYyyNm8hvVF1Ke0j05CuYcITUwWOciVHivQyoyrVjOi4pOTy7KNXwW2Pw0v-tRJYlZEW_bywUpYRW9_XUIYtjheiAtBbyIUY5k2QilyU457JdTvQC-csbxKyfYz_HpJTjzKWoSaDX_Cy5E4GQWhWG4OsXux_HOVG0cd0Y6SAiUgPRwfRBejj2FaYYk9CVrMhlJaSLkK2dUzpfUICVoHsE7V736XgpTyowR64Gac8tV2N2Z-KfaDF98rf4Ok1bZjGvc-VG5GTzhNG_hSiMNGxbRQ9ZINdw5_l9W1UdltJDpU6pHtw3snHVDuHAyDyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که این ویدیو رو درست کردی دهنتو گاییدم
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83128" target="_blank">📅 01:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83127">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83127" target="_blank">📅 01:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83125" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d524cae959.mp4?token=d38Weq4iPwiHzXsd_nIlQj3kMOiLXS79SJVyTbw9kefxw4hd4rkYbQ_6cB7obLFfgxkS2c_3SdwHiwmuyUT-SDlhG82Oob-DG1rcN_IU6ogBCfr4j7MzbiZoNs10RO7GprO9aN4dltKJD5SbkIh9VE5aMtUgtu1dms_BB2QBIODBa3HdXMVU7gO9lVvwFSCXuG96CZtxhBuXZi1VxNvplrEbHQqCDWVYCILxKhpWo95cpdmwmmKfc7x_JoMyGfILZdh3isF-x-uUfzw-HDa2R75Dgk12naK3RmQqb-0mhmidXZ9TlXgmcg83DlclX-hKAJP47_GEbSkkFW4woWsbTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d524cae959.mp4?token=d38Weq4iPwiHzXsd_nIlQj3kMOiLXS79SJVyTbw9kefxw4hd4rkYbQ_6cB7obLFfgxkS2c_3SdwHiwmuyUT-SDlhG82Oob-DG1rcN_IU6ogBCfr4j7MzbiZoNs10RO7GprO9aN4dltKJD5SbkIh9VE5aMtUgtu1dms_BB2QBIODBa3HdXMVU7gO9lVvwFSCXuG96CZtxhBuXZi1VxNvplrEbHQqCDWVYCILxKhpWo95cpdmwmmKfc7x_JoMyGfILZdh3isF-x-uUfzw-HDa2R75Dgk12naK3RmQqb-0mhmidXZ9TlXgmcg83DlclX-hKAJP47_GEbSkkFW4woWsbTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینهمه هزینه کن زن بگیر، تهشم یارو بیاد برا اکسش دابسمش درست کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83124" target="_blank">📅 01:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83123" target="_blank">📅 00:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نرخ سوم بنزین رسما شد ۱۰ هزار تومن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83122" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.  SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83121" target="_blank">📅 00:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_vLQk6ctYL1EirCXTYu42_5dkW1WcM31HsHSv8vN16vBSAK7YVT9jKwz0sLEI_7yI3KxygybzAdJHtEut341Y3T-Cgcm6pRjkojhnDRsvbYfA5NFflbIwb7vGM4kMyIpXdpPM2GL0qp3DkVU89vRbwSI7DhGjXDKUAHKCBsxq7DnWEnepdhM8HHW2WNsxjLovs-PF1iI0r35dSz_Q_OgefBhygxk1FW3__IdqP66zSeTpSN2DDxwF5ue_5DkcG5i4m4vu5n13Kg_4P9Tdru-fEXxj4lIUgUZOv-H8yEIhlhHHXfvxZkT8hBmyCb6C8URbRNuBm_zxxrRjz-lnOq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83120" target="_blank">📅 23:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=H3kjeu_VcvMfOE8Rxn10eJxW1um_I3y-zs3nHcQ4I4k-tIvnR8osjVLhP8OY8hzkPHxPLTrLA4NunT4WJBv96TQJl5633k-ldx9KBK8yOqx56u3wHXC3qTJW83Z2IqzUH3Sm2tFUJ6gu3auQR5ECT6KEeavgd0VvC4cz1G163ZgJU5f7oJlMMqq5Tv8Cuzy3uqcJiiNjtPVB6KsPhMcAGv3YZHGE1KVHEONJJSRMdwAOoyW3ct5X7lsMBe61ur66AAa-dItu5pW87yW_OKhgIcyNcqsGqd61wvutAuui-z6D-u8NugwtxPRiQM0k9r4lpltO2OanL-YJuR3CHM60Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=H3kjeu_VcvMfOE8Rxn10eJxW1um_I3y-zs3nHcQ4I4k-tIvnR8osjVLhP8OY8hzkPHxPLTrLA4NunT4WJBv96TQJl5633k-ldx9KBK8yOqx56u3wHXC3qTJW83Z2IqzUH3Sm2tFUJ6gu3auQR5ECT6KEeavgd0VvC4cz1G163ZgJU5f7oJlMMqq5Tv8Cuzy3uqcJiiNjtPVB6KsPhMcAGv3YZHGE1KVHEONJJSRMdwAOoyW3ct5X7lsMBe61ur66AAa-dItu5pW87yW_OKhgIcyNcqsGqd61wvutAuui-z6D-u8NugwtxPRiQM0k9r4lpltO2OanL-YJuR3CHM60Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر کصلیسه رو یادتونه؟
بزرگ شده ریش در اورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83119" target="_blank">📅 23:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buogPUGuepx_YlHA9JOqc1aw_CrpmHsGlVIVTiaH_PifQA9Cf0jJ9yy_MNzW7fkqVQ_94BU6uOTvmk4P9ngvkKWKKkuxm3BGeMYaOC8zXwJXrc17-L1VIKb_rJMwov-EjvfTyaowlMbpB8wReAM-X01jPIK1JnybJLYN-Ev-SDe4i-NnJECL7pAwIfdusoW-NGTNZDHHRwEkrWlmgS6jHQcprSPWuroeyjuT3wLuzTtNT9rOjWVxhq35Jnu2XJ8AGV1MZvQOtr8QH6EhchjeKsuwx_q602-zxJJJRLfUhrSvgGK5xbq6f9MtuZklH27hTCoIXT5kYfOWAMdTIT62Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ناراحت کننده امیر پارسا نشاط
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83118" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur587IBhARWu1kORWGSpiuTjNzNFpIdgLW5eLPXGo1nxGAHf59h-EXqaLGFyX68-6nRX-d_mMApSts-kI30dEh-uDk6x7iVBb556EjZrDdyxSaB7aNdG6do006YhjOiJdqBWIKuHsFdvOZSht-dbPasfLiB-PiqSO-I88HKLzzaU4ghdhoebNO3AkDt39fTeRvuyF48qgAJa1ctlbMJDhxY0P20wFdHQG56TnJgpJdm9a09NEn-fNYuiYIrO2KtbIDd-tAHCBZV5Zwk1XTsrS-nbSpQ-iYj8_pC0RzDMf39HyUZ_5lyJQHnvjSGYLLLI7sWJmqwbZ60dnPsdCF6fEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایبرلیک هکر معروف بازی GTA VI اعلام کرد نسخه کنسول و PC  از بازی را استخراج کرد و بزودی منتشر خواهد کرد.
اف‌بی‌آی همچنان دنبال این فرد است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83117" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مارتنیلی تو لیگ عربستانم کیریه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83116" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbtin🇺🇸</strong></div>
<div class="tg-text">کیری کیری کیری
واتساپ برگرد تلگرام گاییدمون</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83115" target="_blank">📅 22:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تلگرام جدیدا خیلی پر باگ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83114" target="_blank">📅 22:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwqWR5UpDCBm_3LbVIpyi04IfzTlibmQ7VraBv1MVYTLJOlgjiFV_RGWtdUu21Qj7rEPM4WsY0VRcrmYpuFqLV7atE6TEdMa8fbo_syEr8M5xPBm54epj0g4C6pb-xYz-NlgRA3qVVVLKD6kwI6Y8oK3lUmtaqGvL8Pk6AEcmqh8-Y9Iq9_uCgbTcglMWsCP6w3Kt_cwmsMBNkqZbj48Yz3ml80HWIMlTg9l5bFSdNIy-9VuTr1_PT_YmF8yWRm3yAOWjfe0alw4rBMritQE_C5pXefMxL7DWctdJSzOrwAqfCk-MvPNVHng0YsoQZsJaAj5Q5kngPEJAIn_dNs1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا از ایران نجاتم بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83113" target="_blank">📅 22:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=l64YLuvTI88GhQtai8iWqj1eiDagcXxAbW5y9YaPIqHodcxzdY-AThmJnVQXHoCcpW7V8aLPJfWnaRcqA9Rp90dfT3HuM0BwTl2IZe4Pn4nNSFtQ3vpZiYea1MtWRSNtMTwWiZ9LDWSj4QriVVRylPdmgiZOyrux_NJhukuadeorSeRPWIMjx2-HfPzHg3eNHkQVY2LtqutHAideFi-IT3JmXv57_d7mJ6DqawSb8r2YshYuUF_HuZ8tunfRJSI1Kn7oeh2EfhM0UrjeGnkv096Iirzsc8KfrzR8DfDPwDauv5x3CQcWpTjIyeTSvzp8UPgJMttKfeGoAGTT_oqi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=l64YLuvTI88GhQtai8iWqj1eiDagcXxAbW5y9YaPIqHodcxzdY-AThmJnVQXHoCcpW7V8aLPJfWnaRcqA9Rp90dfT3HuM0BwTl2IZe4Pn4nNSFtQ3vpZiYea1MtWRSNtMTwWiZ9LDWSj4QriVVRylPdmgiZOyrux_NJhukuadeorSeRPWIMjx2-HfPzHg3eNHkQVY2LtqutHAideFi-IT3JmXv57_d7mJ6DqawSb8r2YshYuUF_HuZ8tunfRJSI1Kn7oeh2EfhM0UrjeGnkv096Iirzsc8KfrzR8DfDPwDauv5x3CQcWpTjIyeTSvzp8UPgJMttKfeGoAGTT_oqi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.  کصکش پا پرانتزی
😂
😂
😂
@Funhiphop | Menot – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83112" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoEAVO6Sn1puPVtZInuC0SsryvG1dJauLuGhiVUmdyA97PMekvJpKd7OSd9hQpdZ6LlgkpE-NaQPGw0j9OD4Jzsk27oviVoAxR1C5ZXfDEpH5gMw3e6pW3qKL_gChliuVxkMLS5q5wxpbWk8hG3mg6eABc4-D_xWVvF4r-xsPJsyQOTNtsnMggVx8xynipeY6j_SICsRkFN9OdYBK2NLTbN6ehnKibbUQMDNrGk0XTErBxLAXj5G-AzQgPtcLQ2R2P2zoCP8VL44IVcs6VnqD8bdf862fun6-Ta47P4sHR8k2GhtqGA-HkuqdHoNOIPsVpkTQI6Nfys12Zo80m-q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو با این قد و هیکل باید خیابون ببندی، نشستی با بلاگرا و رپرا تاک شو ضبط میکنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83111" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چرا از کلش آف کلنز حرفی نمیزنی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83110" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا کاری ندارم ولی آدمی که نفس میکشه قطعا عقب موندس</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83107" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QClnlCTqD2QOkhAHhDhTdcLt4t7v5Y0YRvFiEuqhlf5L3zi3xydl7gw4lCSEGsw0VwGlkB6lCE6jvm1ovMW3joH6Naz_T40r6Kf_xyzCyc1v5TN1BppokVGNbka5gbPZDoVF09M83wYMdmgwyyW2dFNFEI6GYjcs9vWFWVz23M0oIOCTi9aoT9fY0bOfn__FPuFV6rNmg_hZ5GoF3xwMumfWYVHfQgGc20Xgd8M0u2xfB68ak5Oq0x2YIkyhi3YutkvIxY2MSd-JVQEOrM4tegSD3yL1cCWx2jp5ntTedyTvpv__dJ1Dwa-8Gss-s-LfJcFyyiDvKS6YS67-Qf46cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب مونده واقعی این پیجایین که از هوش مصنوعی کپشن میگیرن میزارن زیر ریلزاشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83106" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQrZj-lFWD6cdfI4tUE58sz0KcQEqJINP8enOUd2SDxd4qqwOHT7OVg_XNzAGG0jGlYl2nYGSeUpWSxRtO2u9_NNYV_Hi4lKp5I7ff_9j0t-raWjm6ADfFJKCP1iigukBQ9GYw-L4bY_vYNwM4VRhhxr1a7dqtYbDMAgtmZk3GsfZT7kBVQLklRIrHL968wpXcJOqHOSK2INQyQtMI3lYW-T5SX7ySFk7c_RGXOyPqi5zjOafryRygZQJ_WQYo__4OdGakO0qOwSiii_kQFghdKOUnFmdovJGOo9AyW0Chlg84xolCynCnQwtSfnAP43qXTNNt1wuexDxtaUv_z54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت: پسری که اکانت توییتر داره و خیلی جدی توش فعالیت میکنه عقب موندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83105" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=RKU1GQ61pbBYH_5kZPYUbzwSGPeS34XlwrqAx1xSe9Q3nCWSWf0LvFOMxhu_zLFcg9VXkg3EqL1nKopaGVlYmpX_Nuqw2O5tjR5r8eEOSWmQGKllNuOAvsQaIvvnpeoRwNU7tGG9aBkG8o_DZJD3dDILB56OlZmuKLIrf6i3N85sLJgSFMKS--l-wbvrGiheAq3CD6cgi4L9sjHl-elQ8kL18PFVSoZ5oMP8HdaveA8aOkpEOEMYPw9S7KBJzy34TZN3CZ8Yl7x1LaPUytL0ZFsGr57jmoCLSO4Mi-ouwA4v1KPYb6fRohCfQhIkdgD6e-oILOk72DK9cXkV8qwUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=RKU1GQ61pbBYH_5kZPYUbzwSGPeS34XlwrqAx1xSe9Q3nCWSWf0LvFOMxhu_zLFcg9VXkg3EqL1nKopaGVlYmpX_Nuqw2O5tjR5r8eEOSWmQGKllNuOAvsQaIvvnpeoRwNU7tGG9aBkG8o_DZJD3dDILB56OlZmuKLIrf6i3N85sLJgSFMKS--l-wbvrGiheAq3CD6cgi4L9sjHl-elQ8kL18PFVSoZ5oMP8HdaveA8aOkpEOEMYPw9S7KBJzy34TZN3CZ8Yl7x1LaPUytL0ZFsGr57jmoCLSO4Mi-ouwA4v1KPYb6fRohCfQhIkdgD6e-oILOk72DK9cXkV8qwUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مگه ما اینهمه شهید ندادیم عراقیا نریزن تو ایران و به ناموسمون تجاوز نکنن؟
هرجور حساب میکنم تو ضرریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83104" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlG86BAFwdGptEfPc-Jx8ZCkVpyW__Kp4mo_DpsIuKbVvIqnSAhVOw2gPMchDRCONCs62Qw6CMLZFoHgvAY_jRUX_ofFlEQsltvnVlquzwgsGkwxj28kAGKGGETpQG_2q_dVj0YyXjg2vS-IaOux53g0SyPcNM-Y9x8BzsVTWBmOC8r_Cp8j4HI6RwLOQnc2K5fxCiJQLCirZR_zb7rNJop_NCaS3zq7K7elImKXuKk_qNzs-amEk2yEKY4JbwWq0ysMsdhmqQofldF7RVkpMoSw-lDoAIXZ8r0Rc6EPgLwi2ZlSgpOVqCJdVOEf-zOsESYZd6b-kPLjyYMPltXNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
😢
سرور فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
g16
🅰
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83103" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امیر پارسا بگیرمت کردمت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83102" target="_blank">📅 17:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شین:
پرتاب موشک بالستیک در هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83101" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjjmXWkHit-6Hgnei7X2DGht5HFnCRwefmhlKGGfliq6uzkqkCAdicKr6kE9r4jPqktgZInwr9QdURUEJmfD5lq6gDdJTHFVm7sZgNNq2A8vpHwlVSxMeh31f36IPlkiwgszhLYLs1e6UjsrB9mx8IiQ2ek0TqnAXkqy6TVJthXuclYhyg92fmj3XEIke0wa2pZdJntisoFJnwy_Q6r7oSn_roe1ylND68R57fzkRj1li7iMPWufI0kowbQGBcDW_NMWZzcn3mHrBGObnarCv5S4bKb5Mb9WU8ddFzWRWG2otchU_I7gLBk80QB6uHdVuw23mbD1rSV12b76ySYgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان بد رو فرمه پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83100" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKzJ5nIoBT_1xRw82qwfRO131NUTv6szCxLyACMLdCXaP1MKiceEIkK6fCZsIYUnjmBPUvw6LXpMIrdGzX2Ceu_fomm2ieWUrqYbA9Jmdqo-iFYVQfElIMCXdS7hGSYMR4cF9V8x5nBfkq_wWYqa6mWwffUuTcb8-L4Wzg92Yri3HSqINoLkbFtaWYcKhcn1aRL8KxWN9AtYcCigFuX4YASF7dfUoWhdLb_GQEplrOK5lWTEOfv7i2mhhpU3-izoeHd79v2DMY1Qz21VUmq67IpAf-P8atdbPfP7r2ZwTz4_Xxmc3hxR_7qIRMf2xf2aj8h9d1sQIxYnZFrBjilmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان میرزایی، هنرمند و معترض جوان که در دی ماه بازداشت شده بود، دیروز مخفیانه در زندان دستگرد اصفهان اعدام شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83099" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ناشکری نکنید، درسته دلار نسبت به دو ماه پیش سی چهل تومن بالا رفته ولی نسبت به هفته بعد مفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83098" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویس جدید علی دایی و کیره خر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83097" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ویس علی دایی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83096" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=uhgHhR7W2-dsokbWN2g9rI1SCEugO5epT9zDkPR-EbYtrAAxfv2SFi3zK_3iUzaxANT2f5VIF8q3pQHuPkBpOy_ZOqOCns74psYTI1owtaUrq016LvRcPFA8p94W6FHMzxeSrDA_Ko8jd-qXKDE5jmc7pScU6FEQo2-5PLqmb4s0LQVeKWrXZ-vtiZf5qp1Utd7rI-iGia32jzPXmuhLBVn5JvPpNesZvOtuLM92SRXhhDA7s2WLpLOKfZo23_Uyeszhl17RN7_bQoD1SN_5RP7-Be1iThxpTbm6tmscH7RRiBhkaWiNKyv1QU7d31H073TLokytAUKkGEMi9afm7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=uhgHhR7W2-dsokbWN2g9rI1SCEugO5epT9zDkPR-EbYtrAAxfv2SFi3zK_3iUzaxANT2f5VIF8q3pQHuPkBpOy_ZOqOCns74psYTI1owtaUrq016LvRcPFA8p94W6FHMzxeSrDA_Ko8jd-qXKDE5jmc7pScU6FEQo2-5PLqmb4s0LQVeKWrXZ-vtiZf5qp1Utd7rI-iGia32jzPXmuhLBVn5JvPpNesZvOtuLM92SRXhhDA7s2WLpLOKfZo23_Uyeszhl17RN7_bQoD1SN_5RP7-Be1iThxpTbm6tmscH7RRiBhkaWiNKyv1QU7d31H073TLokytAUKkGEMi9afm7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83095" target="_blank">📅 13:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رپر عزیزی که دندوناتو طلا میکنی و میای تو خایه های دوربین باهاش فلکس میکنی و به دشمن فرضیت فحش میدی
بخدا نه تو ترویس اسکاتی نه اینجا آمریکاس، بزار درتو</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83094" target="_blank">📅 11:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiCaErGpjFq93E23PoQ4qlGk9Amro_Uugv2X4lGolu3F9hOOT3ar-aZ_nMdgYhPkS8GGbA1MZTgSGZlTIQlMnls3vCZA5Mrd-xhQKw2RWSNc7R-jJqsmd4ci6YzkhcAAW9HCC6PL5bzZvGGDfLxgIvQ8qgpIxlJ_TtPk-Z-Y788P2NsOFbTiuaFNh9MdYytE1EdyobBWV6iHfUtVcTAWHpOsxmSfZd-0uXZmUwAph9mr2ejjd5G-5AdSGKiazkIbShyt9tBmnq3QXTfnuISXRIHCF38kwAl2nia_c0Vngn3X4YzKuLNGierdgRCJDiIyrpgeqbFtjNUoj1tRyM4WOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد عوارض تنگه ما چیشد استاد ما رو پولش حساب کرده بودیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83093" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی  شاه کهکشان راه شیری فتوا صادر کرد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83092" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYJWfQdHJvC8Z9kEDE-hG0Ed9Kjbl5YO66_Bnd9I2gCzYSlXxJJbbuaVvcz-yONWn7S7d2H2wg8QnkR-ATo-DVuuDuh_vrPdlihSzGSVg2YcGOVBuxIQQI-kLhOZEz8IfTt1gdovLdBSOclRI1X_356WHB66jE59sQdCg7Yw_zPaoaiREpia3KjxVXxLbUnZ_DdteWUV094hRJeVXZOmRpl9efvikZPU9YDxOEfABwEefkzTMUuEx8L0kacF6V2F4K149GFL9jWLMgfv92QL1oK_Bl3-ve0RCU4EuQ22QHAgQjHkzu3YKdKt8IX2rMBTFuEwLRHHjHKTkq3wvjnkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوتک به نام TiKToK منتشر شد
YouTube
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83091" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83090" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiK52ZfHbC9r6-4wegufmfrQ8BnPJcdgTGa7a3v_xkZpVtmq_awzGBi8GBhoh6xUVfg5urCa6W-StBBzH7L_vAzf17lkiquK_zQ6LmddRuYr87YmRO5frHC44G-uYKaZz2YQSwSZgoWhkdUXYf5ktrsCnZZi5a1fG1g3k5moPLY7lCOEBrud_Hk7smnPj_avplCh2PN5j4qRVZeuXtwG2fmhm1HDGrZJjOvpeLkc-2dsgO0r3M5DfWU-Qa4-J7RE_RF7p-AGgouAkrg0fyNNgYeS56LTvmBX3Eq-z8TLwpwm4XGqk5pLgzocjP1yLMPAbR3-BAcjHFb4q9_9GxAA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r16
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83089" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi9E5pFWrrdZ_N_CUqKLjcLqOzE9qFvaxTxvIR2AfFsGp54yrCrOtFrbfeurfpNXjnbX0bGfqIc5BIUNFNziW_JLdXBdcb6aJSjHAqUcaFJcukFvhuv3TebdXHPM6pFl7cDWgOZVhiEargCX4Y-e2nvKFXDBbEyioN1bRvnPQV4K60YnBcyochHHFhJ9JfH1ApmGQK65H5lYKzKyq-0kA0E2utd3j352HzUuko9YhosQEymYFyFjMnhV7kAVkYfBiFVXh1nTPZXgudLAdtcWcBGVIkjo8NeQH_pg8m8cqy2840sj8ZViurrWvnbs2xvYYkuvjpNuy738Cjs8oVMMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی
شاه کهکشان راه شیری فتوا صادر کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83088" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJnvq6E2xca9XLQb2FxUP9PuKcd16iJqfNn-h8BhD6P5_R0QrJjxM5FlXW7L_hz2nmBfn1HEt1qFWRIG1JJAsF1Yx423c2oKLdh_eRJHE8KFSmZO-MsD-9Sdj6Nkte7nBzTlr7W0O-_5zxz1alj-OQBXUn1WaztMCrwjz5gJGrjsfAy-qA6RV9dqfG0pIBTFgY2DDSkUgqvTRv2aGNlvOfi2x0IHMn2br74RRIF2SmCduZ4gBCouY9gj2Hhnj90LRau9mcjMrtcv17aYWTEcuSIOs44sGBhnQhziiJ1LKLo4S5Gn8thEmVRuUVwWrQ85dhn7mTNh-X-2WDyuNFZ8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون به زیبایی و درخشندگی این تصویر
❤️
😍
😘
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83087" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مثل همیشه درست وقتی بهترین املت زندگیمو زدم فهمیدم نون نداریم</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83086" target="_blank">📅 03:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید  یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83085" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56316020cf.mp4?token=Tiu9d2hbG9GXwVc3i6bRWvWCtkSjqXccxu3h6B1vh-qy7kU3vtN8Z7vi8KnepE85ojkjDq1cRW9ggu-WRWx-7Op8KfSAvZg4bVHyL_ZzgJ1FnyR3DHGhLhRbKcB3-jWP5z-xZnG7BA1xwDqENZ41iai3IZ83cvqV8AvLBy8Qdve9G-T7FHGNYbJ2nktpsNn3gCF2tg3Kw2sJQkwBUtHMFPZTGWWVOHJUfM6td3DdQgNYPFSpKKdJU8AI9QxOyZeH1alg9u6b9vAHHOThzJw5fNsx_8b-TRnHJLNJK-TpUZhP--KISsLTUFha3SlCfk7aFP0RLnwxbmDkP5Ii3goGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56316020cf.mp4?token=Tiu9d2hbG9GXwVc3i6bRWvWCtkSjqXccxu3h6B1vh-qy7kU3vtN8Z7vi8KnepE85ojkjDq1cRW9ggu-WRWx-7Op8KfSAvZg4bVHyL_ZzgJ1FnyR3DHGhLhRbKcB3-jWP5z-xZnG7BA1xwDqENZ41iai3IZ83cvqV8AvLBy8Qdve9G-T7FHGNYbJ2nktpsNn3gCF2tg3Kw2sJQkwBUtHMFPZTGWWVOHJUfM6td3DdQgNYPFSpKKdJU8AI9QxOyZeH1alg9u6b9vAHHOThzJw5fNsx_8b-TRnHJLNJK-TpUZhP--KISsLTUFha3SlCfk7aFP0RLnwxbmDkP5Ii3goGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید
یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83084" target="_blank">📅 00:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4lLOL3h1hWfM__F-H_SyTRGM7rD5V6I8jGOverlED_MLeVSi6ba6TGHVIidOlCT2veG-wOJzoGAXFFlHMzy2wjkNYLLsDSYxCXGObSNXyEnojGOkVdPbvbjKItlKQLyh05hxVAP7W5morvLrO3fyr_AP_9c-jlz-a-uVlR4IvQfoJbervrBoQ0EsmE9jgueYLUMsEa_5ivlUZJJ7MpNnva5Ao2DXyegJTpPOp7LiC67FC6H-usVbvCg_1kscdxjbOOWWsYZ-C5B0uB_yTCxTqPoNqlki0wv6k8mG3D1MViPDRsHBy9GObA0gnWFd4qnr3yiZJApJ9X4o64Qk39hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83083" target="_blank">📅 23:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_Dn-TIoAMpiT4Pu0xcWwMign9NHXT1zm0_qs65bCwlHAEHwsjCSBoWiL1BlwCA-kuETsBLPdEdzrbG3pSKMoJbdFUygWCe25hIeBUYqiQxUqxIK2fpXnhTA4kBgJtFLo_gTDOrrT1RFNGyuKJ_Eb5mORVj3zIMPoIMKYufuZqw6Oc-kY0imd26pcofzrK-J36Bt_sVC4Uu4An5GewFlDxAboMnCEUCBHzsY4XqlXwXkuTBLnblDwitbuy_VnpnNZ2RnVsRRnSFPo3ugY17eAMpmCRHsHgeQgqu-f27-xfu7nZyyp-d4fOXWqRx38c_LBuj8YzqXupZOCOCRJXGXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkJ-deCVEEkUE-KsqSd6fDdQUWteosiWl4hdE4mU-tlkehnQZp8lY3_-32AhZA1-UrlsS2nYYOrj9UqrsMqlg29iv4_4RdF7hIev5RlA0qmg_WiRcUoAj0UL_3_FIhPksTBXi31AjQznj-j_XknJJ3UaYLEHL5ykKAuJTHSizcF6Dz9AQvqsEZEZHuX2ywyOUjcX2HJzEyaCWRPdAXI1EFgszxje-Pk9btHXH6wR_DBbmmyEDCufGWb3XvH1e5ho-7zhTMKjtZTNjZnudaSU4F0Lt9CMtTnDXA4rglJkEwGCbUSRYKEHfBjwE0DktOMtFzPjx8l3vfd62VNVg5QE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKncmF9GTLVx2a5Ub2KdKp1uIelxGAag_ShxTtaFOJsWzlSsKvFNY6SdrXvhNjWM7Z-9yodaMz8Bc9rIVGEroYf41mkLNZjsjLCQ8ZzuzVjQVAr_fgoRJbbkshDeiEdhVGahAXL2AnlRZL-f9pVRJXT2pkiNdMKbsEkWrKacdmcxXx3-mffI-Q32bKny3FXmPNvpKNzPoku43ny15VTWM8XDSXfBoZFrU2JRA630-pFJuPazCO4CL3PeYpJr1FOFc49HNiBCkr9bgpbXs6RcCuiKJ0Z51SnXNQTBHSgC-K4exJqNCp3vQZSK30P-lNtUsZo7451MDL5J5cLAJCyGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOFELd7xX5lW_EwZ14XHx6n_dbU95mm3yRVPTDuGv4MxbSYXh0z8VSXJAbCJ1iix_iLKKLfK6CTieKds9nJpKAr2UQkbUMWRuTwvQdzjE-8xvVUe7aM607TfqKlNoFFG81OS4fUjEV2_laWBJxo2RxdfHVStMwiIHaYeJagXd_c5I__DtzlPGhXuG9lW4jn4lu1gTwVME3VJ9N6B5fdmKEDrK1oQKpoVRhSpOfzby9oqzr2q-ibXFlluxh0TFQ6eWZbDfr0pjLCkKZrBKsg30S81hqTJ42gYIyPxdYHKFXZiJNV_Hb8pf-r7qjUbVcblimMhif8h1oOHOGPVaW_8TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صد رحمت به سلامت‌روان دوست‌دختر تلخون.  ترجمه:
ماه مال ما است
🇺🇸
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83079" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia5UZKOx8yiyKWRe8oGAMRQZNSrSBQWjyVcIVAQKg-GEK0TsVIhodYu2xDdzKrZ8kopZYjwIiZfTivbKmNaBQCRT5uEPM55Zog5fVBOBu-9kKoRzd8ICyWGlZz0CahRzNRcjcYrUYi5DLE9ibbadaFEYT13YyB7YEgr0MKY6QF9HcZbrek2NU1rtipbZ1ILUVl_gH4A1J3ozFh_P6KqX3DAg_j8tJc58MxpPqt3Mqu69RXf4OYKYh4eLJ7WwNvaC76h_J05ZscNEjXPtfPPPO2Mk6Wfaaj7kPtt1_6XzS7IuljiF6N_4TlcuJxRax_cO9Tci1G0QEieKFDnQoV2H_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛ این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83078" target="_blank">📅 22:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMCfX1ryzebe5E1s7TjI7OoupncLFOzTcKwlKYky_OexLY9f3cLj1Djv2HvjppecsRmYUAHtzshTeeeOFWVsJLjykluR5q4JTXGNnsRxiexMpeMJiMSP0WartNbF2TAsze6ABhLBncx8-T7pd4dDn9bIfWC2IxfQGaseVQykWk7i6KSoRc8V8o_yxPlwOkomHwnOpCe17yrwzS1XChNflhVoY2ns6L--mqi-JC7mkuZADagP15BA6A9DJjqiwuWZ4kHoTvK-7L-qrylToMrKZdMT_hfdf5J--lJSEtoirQxWHogxEGoDVQWMzSk0-BWPPvmc03NWm_dKt8KOTR1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛
این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83077" target="_blank">📅 22:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از امشب نرخ سوم بنزین ۱۰ هزار تومان میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83076" target="_blank">📅 20:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2dxdd6Q_jKUeO6M5bDpMUYGIHjrLDLSxT2ekFo1cL5hjLdz1s7anoh3vBG1VOD4P2XjYW6QGvlWDkTrtya40R9Mamy-04Mgp-5ykPAz5NvZ1dCrHLDNshybFoWXiVGo3d14V8p-Y-XrNnb3QajumEMjMmTn5PLvkAVpuiSdcSYa0c2OqhYJd90VByI8D-26VUKvLdzm2xFboCbIDnkj53bJh943ajqmyrPXMfKLCxHg5BdixWwvAkwG7KWTb_rMJq4KJX5mMUFkJ6xvzsy9yRzJeoQHUim6aeFzwVro5xHGAiD8afUJLGwbdoHeh4xED2w4fnEbXSqM31U2E0B5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمین صبا میره براتون نونم میگیره</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83075" target="_blank">📅 19:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXAMpcHbhNO3ede7uX6yoixJJQt2zLQ0Ky-_XPLILFw_vke6fHnRDDMwviWWUIsiRrQBsqDLss9CsqrwiySyCTflEVYAH0yrKKkiq8YL9wkR8Xmd0TejaLI6aCVsQNET5laA8324is3Vf4ubzasitBym79OVS2ul0PSZoxcT6l71TWGf8T4C4WXlMVlOuIYXMlLbo833neqWSaLcG83eIruQC2iXBOb8dXPrMkvcSSoXOvHrwVtopS3Dz3HQA3V2K5fPPP4ut92ye67fLGNiTtYr_tN9FpYlWjEPIwexJV47ChJOEOs1BejhRSQ26EAOOMvHeEKlsIJaLscRQ-a1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش به خدا یک هفته از درگیریت با بسنت گذشته،تمومش کن، به خودت بیا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83074" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کصکش پا پرانتزی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83073" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">منچستر کصمادرت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83072" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLOhKtrEqSK3EqXPVIN-qdrnLERA7ViMtHydLeeQSStOUy0yM5umbpBLNCBEgfdV3I-yYe5Cpeo-oeZmnwtk5rieOeedT31FDEr90fDU6qSQv12FaVljxhtQ6c4GzFASbcgcal4pR7FcV9C53XNO07-IudJ4ufHeLPS-naPitKKOVFfAoi7kWtPeS9UQz6mTobw5ToMQ_RnT8p2p8oK7eAch0VLG6RsdjPyj3XWm_0W5doixV_qVqyNzc9rY1L8fZSy1Jn2gl3kBqrCTxzBwoib17hu7rtkxcBhMwB-8m1S7JfRYC3frzoBGzRZWE0BCf0vz-xEkphmJzEr741Xj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خداروشکر گفت روحشون شاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83071" target="_blank">📅 18:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرمین لوپز شاهکار بشریته</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83069" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ2QdRne2D6L4JW8yPnT9oHcq5RWYWbt4FwueVkTsBVE0ClW4H6NmQ2O5YmhkAu09cqNl9Jaa89V-lTHVxbuSyhYpbQmTxfd3zmtaGTb30PCBD3glKbjOiUHJA1iJRxE3F87FrzDrUd3YH-5JUfMTzvbvbwEKdELs7iOlj6gFOmr-tFLlFQhZFmWfpX7RPGkvvbbjf4osLD2zuSEypaoKogkKQA74duTsoVkaPejH3URk-Dsyt22tfp8Yh1g82-01fIAuK6bslBJJ24ybGL9cXD7f8T8YflfKiGcuphj5jlwSL-DgqQTOrzf5QFnuCX0sCgyK95VyJpBSWBeOqBE9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشم آلوارز نفوذی درجه یک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83068" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtakQEWcgkodCDwfP6dvlGXa-axYtPRfnjGVVGFZbbjSQ_jKI6dEMsewmwvh78tFdqVkKmga5YP5-U5lOW8oVSovbn1Eq-zcH4C35okPMN28l8T4Qoh_JfDvqZcpVh_hrxP5wjVTZtQ4HDtrm8ZEM-A8VveMXZZzZzduwIotSbCFtnwZ9mmg5Prwtp50e0fi-KBpk-T1NLv5jSZuBDlCVKRmBeCUn7TOSbpsL8yO3FP9QzI8O1bUaZxxlfJB8Bi9mb7ooXphiTmG0LF3wGR2C0cq1J2Gh84VOqKyMaKCIQ6jSyVElrqNzgBtJwHU6yhB_10G-oqNhGRkbhozB1FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس شش گانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83066" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnNgX5xUpj35RdF95l87mZec70QYyjLGXWsjPQLD7yEQzvSH74rspSKgJiu1zqWxGVZWpuc9akgnqEa6GzVUB2TNjFR-X0lVAg1HwEv6S1HHmgrFpIOsoQzfdoSqAzgmq9BHU-mXzwj2WO964WQ-zZvRPL0YNJhqSkrCJFQXvnzYxJfsR26kUkudBDXIpMgmHz8SgXL-NAOJ913zQyD7gy5bVu4TTl9KUwph0PZhDgDnazLIi3hO64_6XMyQSuhByO4YsjlyKWAFS2wqlD2D_iUPMO_FfScG5SCRH9Pr1TrC0iqxHPw19TTNgi0drNekodKB7CaH0hZy_-b4ukXYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به هیچ عنوان برا تازه کارا ساخته نشده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83065" target="_blank">📅 17:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saMwxmrBUkfZb7bxwdy3leAm_RteNo__mX8M3BoHss2gMgSZLkyVJ1x99l_nwgkUVgDfvthAU59jpJ319P21hWwX2G-1V7lsNCkb7LXlMDisRSp2Te5BbqW30k9-VJyj2dXs_k2S8Hcqrz7Z7s35fuPJ0uDxjCKtYi2K46LYZYAAg4bi8qQjuttICx6CU9aGfVEAJkFeateRTlRP7MIk2RIBNfEC9AL3qtv_n8hLcG-f-sZkVFCBBOdeCHWpRKpBAG5iuJSs6QCRia9rfCHVQWiojpL_UFy1hA7mZ9KTInvRy5g39-dLEzEFEo9tNwSJJvyMwACuBDqyVAO4OlRsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=C9G_QMwzGz8lfDtLIKTErOgCDWDHXCC6s_zTwIYva8r86PV5fTDRY9x7-e8Nsmy8C5oSmClyeTgoAwjBHAhcJTB9EKb_iWFQJjuilo9fjBEX5k7njAJQ3l3R3WpD0lcEQ4gEyaG8delzPfz7ToP66Od0aDBgdgwkFu3Jbui7IZSfDhOzwhfh-XVUVv4tspbEBtUw858odsi8m5z3zwDd2u65LSRi87Iwgs6L4RrEzdFvEHJ6QmGAlSBSkpWBUpsoRHnqNhiGNb33PvneaOBH6MhNrG3TekfVt2TY2s7_fCJmxt00iqVkFraaUp4ZDo1-Xk-LpqB-fD981d52ZFoh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=C9G_QMwzGz8lfDtLIKTErOgCDWDHXCC6s_zTwIYva8r86PV5fTDRY9x7-e8Nsmy8C5oSmClyeTgoAwjBHAhcJTB9EKb_iWFQJjuilo9fjBEX5k7njAJQ3l3R3WpD0lcEQ4gEyaG8delzPfz7ToP66Od0aDBgdgwkFu3Jbui7IZSfDhOzwhfh-XVUVv4tspbEBtUw858odsi8m5z3zwDd2u65LSRi87Iwgs6L4RrEzdFvEHJ6QmGAlSBSkpWBUpsoRHnqNhiGNb33PvneaOBH6MhNrG3TekfVt2TY2s7_fCJmxt00iqVkFraaUp4ZDo1-Xk-LpqB-fD981d52ZFoh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عشق ابدی براتون رپ خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83063" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ساندی‌تایمز: دو تا آپارتمان پنت‌هاوس لوکس تو پلاک 3a Palace Green لندن (منطقه کنزینگتون) که برای مجتبی خامنه‌ای هستن به فروش گذاشته شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83062" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=iqgxlQfMWfJ1JLeUrzUIDTUUKdcu5YsLjYPeaLRKL9QOaZZH9wLZF8tJtC4Jcg7oKawcos1CbQ1dGEIGA9wbV-Htf0IoAWhMW1uw7dVPDu2qwMNj_I67QQg6dEGoJ5kD4eNbbjYVlBvMARrkXtas9_mLOUpVdJEco0fUlr2e8T3SwWx2jiEEhVdfKx-PYhXDaEMQ8Ur_jtH12ZckNHNIg2DgjiYIuf_LiiWFA1d1Us5lrJ-D2My2DVJ_832zVBYhW9Xd6YjQdmUyRzQyuH7_CpD8Jz3u2fZitMSIB9hrAgJrzXhDZ4tk-ddJNrCtNnY9q0NeIC-oBkfct8x4484ZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=iqgxlQfMWfJ1JLeUrzUIDTUUKdcu5YsLjYPeaLRKL9QOaZZH9wLZF8tJtC4Jcg7oKawcos1CbQ1dGEIGA9wbV-Htf0IoAWhMW1uw7dVPDu2qwMNj_I67QQg6dEGoJ5kD4eNbbjYVlBvMARrkXtas9_mLOUpVdJEco0fUlr2e8T3SwWx2jiEEhVdfKx-PYhXDaEMQ8Ur_jtH12ZckNHNIg2DgjiYIuf_LiiWFA1d1Us5lrJ-D2My2DVJ_832zVBYhW9Xd6YjQdmUyRzQyuH7_CpD8Jz3u2fZitMSIB9hrAgJrzXhDZ4tk-ddJNrCtNnY9q0NeIC-oBkfct8x4484ZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK-b-bOf5zK8AYwXwcnyZhKc3blLZRgWx3M2XMlPtV1GuhbIKvtTz6T3bDJAIPGfIMAPxLRurcHkGdf6LKH-sQVQCJc4Ma9Yq1tXqP3asr_v707zsDsC9vR-q-vIMOwU9cwS4AzssDs0r0O3xjAa_lyqNv9GR_wDdSKK1HtZJdJn2_DyC-fG3NxfawT8zSYeuKrlg39pFaI0otDSzKTjG1EkYmp4FDn-nSAnhIo759weUKLTbnMwpxKrwFI4Ya7rlAnEBP5T7UrhKYASBz2J-oE0_1_l2x5B__SxvFXLV7L8XFmGa81mTD6ODAhLaSrwbVwjIpOBismApwZbTiO3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNeIkZiN9zJqNnpnGOXN1kQD8Bzkd7DudXGi0JgaDE4AUXS89lhcKwto4wDdZV7B4AV1x0TlsOgsAZgxnR7fKnrHPtIkWtmhH_EpU0QbWiM9vykK3V1EsrNKxNlwo8L76JUjs8AtD1ndxC3ZCxO5POpu0xx4M4b4z4zFyDZOlp75GCe1nc3FOrJ8zp25r068KhqADxyrohMDYnkXbPNZzdr9ZYLP6ACCvsuKBcxCYAvyQlzDoJ5J-XRa3JwMfkCLpauudlkGrJH9T1l14sj_FhNi_fy6mO-xu-WLz0xuS3bciid_TGu4WhISC-w5ZWCPwTvN9xhy4I0nQFrFTwJ6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=tSTYQGzeUv3-3AIEMurqOZJ8Yyq6nlxSJEL1cmRAUrQkwdI7o-LkuNSFOJ49eowiWII6FWwARiPwfhYVUz2PefDiF3fDj--CCOW4PFhP20YykYD0o9aNwbSiUQCmI3wLHMTkn9B51i-edom-PzMSpg3uPiLlSXo1Lc6bwixJ1G40B_FX41p3sAKBj8dZ_bPFaJ0mGo2PBABhct2PZkHH6vU9OmFwY67kNedhQ-Nm_KABmz8NnhHl6fDDPgMdL8ftFor-LVDzx2OfSqS1JtCA-c3udpnBKe-LEqMbx6k2wpZO8cPSoY2-6QnrRw-x4h5Y7NwFQCCZ68HD8baFXScalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=tSTYQGzeUv3-3AIEMurqOZJ8Yyq6nlxSJEL1cmRAUrQkwdI7o-LkuNSFOJ49eowiWII6FWwARiPwfhYVUz2PefDiF3fDj--CCOW4PFhP20YykYD0o9aNwbSiUQCmI3wLHMTkn9B51i-edom-PzMSpg3uPiLlSXo1Lc6bwixJ1G40B_FX41p3sAKBj8dZ_bPFaJ0mGo2PBABhct2PZkHH6vU9OmFwY67kNedhQ-Nm_KABmz8NnhHl6fDDPgMdL8ftFor-LVDzx2OfSqS1JtCA-c3udpnBKe-LEqMbx6k2wpZO8cPSoY2-6QnrRw-x4h5Y7NwFQCCZ68HD8baFXScalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی یه ربات هوش مصنوعی ساخته بعد تو یه حالت مثلا ما خریم یکیو گذاشته با کنترل کنترلش میکنه، یعنی در اصل اصلا ربات نیست و اسباب بازیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/83054" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.
کصکش پا پرانتزی
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdREAUICLIFVVp7c-DTyhD70rZUhcMx5hy2Ly0RbAU2n4-khNcifSCZUEE4g8rebYxXZNfBZwEBezWqZSUk2f_QjrzPYNeBUc8AwXcS0hEhRVhlvXa_aW6a4AYo3CuER8usHiOm1SXSWXx37tND0X2saADUselGvy1y6j89UukukUq01kxrkNhq39L-Q18dT2SKhZp4BR5EhpwSzePHNA-1ySQ0SZ5PkBRs5hSBvjAo8e04ba7i-zWs3LAXseXQdpjfw-ZXOHbTUr8FCdE5-MiQ8lyFLAoKfnTm4dwJIdPxSvDwJdq3W75nw8kjwaWbyz3tAVbWGmOroQw2qvhK8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnSXV0KDSN3UJrPUXlaaL5Yh6sH2llD9BGfCX2wNbN3MIiTebQcDkLBngalcb_DGkEiIDBTICupcKNZZUdf3wCEwK7vSwMUO5Hmueb6aZzoDsCAvJgHV5jDRbNb3G8p6oHfNVl1ZvyBfqtPFZf8as1OORW_RG3PN9SWPEMse_tWJO5VvnzsuoeDrB0EI5lBpCnI36BAneJW6KL8MyBWfKsrseR0jCkFi3MY8RSNEL4EEM-xb_MgVWTkmEPoEJci-zKMySyCRxTVs9czWjCl2VbKe46mi_VH93V6b3tIN-eME-y8WTGcjeqqbGHxl6Rucc6YKXmdmxO9SjAf1RcnCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همین الان برق ما رفت
وزیر نیرو : خاموشی‌ های برنامه‌ ریزی شده دیگه تموم شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83046" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83044" target="_blank">📅 20:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG7nlK_b8xsLovseru9nm895jvTdUfSKvycorElxBPmkUrcF2GXsMs_E5HFETWJ-TQOPt2RiZMm_bVoitZibshNsFOkaRbPO4fzLsfcx4VJI7K-80CXoxKjiA2XbYYsM5e1pjYk0W1UfhbFOdXlaum25itGAwit-KK6TBiTXcCN25MYE8UmFQDikEWcJaMxZ8-CquvdV0ZVZuyw3mQt_eZrgNJmR4r5CesfuhtlmW57QpntZi0H1v7ItTp_NFBE0lbvo-2UFYEJPQ-rWq5u9qwzDDRnDepLqVqv_mBn8ir-OwfOurxv9Apd0SzPJzJD5yrb-gaV2os6Bmgw7ZVe9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83043" target="_blank">📅 20:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلار از تعداد ممبرا بیشتر شد که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83042" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lerH_RytbwhO0GKvmf8ScjtU6hqexhpLnkQHO4ZFZWJMMF1t_qW4AElILHFHqaWOeQDI_0XLGhbzQ24d0D1_fRLqvugDe59m5GC1A9akXU0zFGwoe0Ct36nAfFYeMplDdm1Kn-w7h77ywbDdLw5sH2Ee2Pv2vi0kDZnE3SKGhehF9p3rZS9Mu9DkOdkpfugUDkSuzzrdJFF4c9cDKY5avpTjetuzEawQhcSX4uTnrNQu0Bcr-se6mst4iEahCHQL6LG3lgsmz5DxERvgxOxQ_15TXSmMzffqfmpzpadxzfMdRGsh3THmLbI9cY-fKpsnlDnycuNQfgMZCgESQtAOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4nnRYZXcq1Wu0kb7UWuY62wiTvjvhGXS5wA7h5Ogab2pZuhsr1nQJA6s4qXgqMdsXVUNEUxmuSEqywCOSdelmdB9LtsVUvaHyeMT7gQzvrgcJUHK-ejWPg4OKw_bi-tryxlywJc7edwCyKTz4M6uTM794d0SVLXToS3OerkTUMKIxiez96lyN7qNexWD4mYk-R30cTQG07HD4B1P2A0GpSCGU3_NNtXmSrShj48DNqyg227m3Ams-LYbCe5Gy0CuZkul6U0wDQ_SbIgrVe_xDkbijw0f2BYwvYh9254g_9WCc7Ud4BCtUeoUsI0YJqeVZOI6w_36XkJSPuy4LgpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpZO4X0RRenbJ0AJpRTUV_-k5U8WXbWh5FibCZ8Fx_hiDxbLu7X9OZ5vQnocJg8pR_32rXHbwFNRlQj8CIx0HLFbzkXud7Yg504JEUF7T4REGJvPXqZ1KZS5Lhi4Ll-iqoJPBDG7pkCvypiILqzhw0-AdSNDqU9SmynVvVN0Icjs17_6AP1jJvkdrS8Kk6Wl0gZg58m1ELfrFYjzlR_BWnoso0R_4xXW7qcnQp5ZyZOtkvWHxqtZCPfCDi0ikMD431Glxp4nkMFddmNZsstNGDNKBO2Zu5t6Gic0YLbCIPy7W8--98U0RtZH4RTiKvbAzEL5YsTJolNJk0FShom4-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبریک به فوت فیتیشا
ترند جدید توییتر اینه که دخترا عکس لاک پاهاشونو میزارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83039" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=llsRzhntlJGCp2TVxJBFl3mUmRpNtYY2UUWwciKNejXPpqMFrMLAspVyFVtvWCyGdnkUojD9wsAdl2cSXzqPBSwBHSX9mKfSzt6EMBT3wrNj4yNliCdQQXhTZtVKmNGvURbwcuPEaewA2vYIncpKNgGEY-pI9mgguUEQCnh0szI52ktkdjDjAGeqh0B8BHA6c8gKdCo3zFGKtgKaH0_aHTLPAuibCYKbr-JnOZCKLdNKBikk9QENR62BREnyTCYp20aNIvfHZt36Qkcgv1EjEesxhJL0w9kfDNE3u7f6_CpXKN_8F26v5njpZ26yhFBlcs5e7x2a_AeJctP9uy_kJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=llsRzhntlJGCp2TVxJBFl3mUmRpNtYY2UUWwciKNejXPpqMFrMLAspVyFVtvWCyGdnkUojD9wsAdl2cSXzqPBSwBHSX9mKfSzt6EMBT3wrNj4yNliCdQQXhTZtVKmNGvURbwcuPEaewA2vYIncpKNgGEY-pI9mgguUEQCnh0szI52ktkdjDjAGeqh0B8BHA6c8gKdCo3zFGKtgKaH0_aHTLPAuibCYKbr-JnOZCKLdNKBikk9QENR62BREnyTCYp20aNIvfHZt36Qkcgv1EjEesxhJL0w9kfDNE3u7f6_CpXKN_8F26v5njpZ26yhFBlcs5e7x2a_AeJctP9uy_kJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیناموس این بمب اتمو کی میزنی راحت شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83036" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تاتنهام کصشر ترین تیم فوتبال تاریخه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83035" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حاجی یه سر داروخونه برید قیمتارو ببینید دیگه خایه نمیکنید سرما بخورید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83034" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4cTHzC1i6hA1knrclgiN3tvrnpgmyAUb1xLNFWYDkAAYaLvdc0qXAc4ZgSGxZzpKhYI4tOZOFL3MCRSfQV2dJQosk0oYwAhMpwB6js9oR8od0DZCkyLguDP5rVKLJjIIEj1q4vW3BMnCIrXWE5FOREQuEKWlogepFJ3vDAk4k_Hp3OonCgG6xCprCCHu8pXWyFP426MVsAexunHMZJoCaofufiGtop85afGnj-zSnanZPIdaKs204I9y_gL74toBbNc6N8lT81WIf0YG48raJSMefE1EwrJ-vGA4L5sC1rSn5DBZ79fajsSLOJ1YoY-6XaJ7gUzkbHeiNs73AtL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو بک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83033" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دالی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83031" target="_blank">📅 18:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گیمرا قراره به آرزوتون برسید، شایعاتی پخش شده که میگن تو GTA VI سیستم قطع عضو اجرا شده، مثلا با شاتگان به سر یکی شلیک کنی کلش میپاچه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83030" target="_blank">📅 18:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=D2XxGIjSxrXTWGeQZ-VpXmYhCHB9gcU9rB1VakFmF6mwHACPqWdmMJNGsIFof4cCE44k0H8iKzKGaVXizPX15tEetc3GCxj37v1PtuyQSjTs95TPX8gWYDOxdehf-_rQeTCuf8Vs3bzQwiGgqSFtvgiqRA7Qbq_bE_2kvNBRfTlLOd3S3J_Wl4gDlgNv89XSZm9AROwr6nF1pIRjIpMqjDqui4cJ2fLMp0AgAM8EQGOSL85QgvbYTDdNxs3xMp6Z2_ezzOne_SefZSj1307cQBd3Yv659OzkENMESZ7gOuKwdku9zOoUyC3MlJcAavAUcCVtxyAEqfHxQJaAChX9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=D2XxGIjSxrXTWGeQZ-VpXmYhCHB9gcU9rB1VakFmF6mwHACPqWdmMJNGsIFof4cCE44k0H8iKzKGaVXizPX15tEetc3GCxj37v1PtuyQSjTs95TPX8gWYDOxdehf-_rQeTCuf8Vs3bzQwiGgqSFtvgiqRA7Qbq_bE_2kvNBRfTlLOd3S3J_Wl4gDlgNv89XSZm9AROwr6nF1pIRjIpMqjDqui4cJ2fLMp0AgAM8EQGOSL85QgvbYTDdNxs3xMp6Z2_ezzOne_SefZSj1307cQBd3Yv659OzkENMESZ7gOuKwdku9zOoUyC3MlJcAavAUcCVtxyAEqfHxQJaAChX9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای به هند سفر کرده و مورد استقبال مردم هند قرار گرفته که یکیشونم رفت و دستشو بوسید‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83029" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMdhmg3bHCytLk23EUTrYQWqdQ1nnX35bmn_4L4DJ0aUlUbLuVAL7AfidJ6ukE-24SMW9Qtrtb8PdMfG8p5IzIQd8QXzu5b6SEO3HkSZDELa7lF6i7OeKZ7XkeGWTYplyeIFyPha1dJyiX8r-zldA0DvaizWHCC6OoM5ry1zs66Phsak-rogVTjvk2dYxRaxsyajArzJXOhzzaxQyK50gddt_S9QCdsyMEpwIpRCoApZvO-qxiyrI78rUljpJdV23RIZ4S_HYNF2HPcdscvMMeSvf4rG-vGR94ANc35QVQchc0RA9GubJQcbSq_Gu17KLZIKye4n7a0Wm5FNX2P0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr83GDcdLhToAtop1AoamPEQ5VPdSfaRGk7X67iplNvUqPCEGFIZYg0X6fItQDg4hTouCRIdHGsH7YnEO8SGLQecpQChdoSomb40-ADqd_Xe41X7zPjZHS55j2Puyp6M95tBxa-xrHZOKc77p4DDYJ8lgAwiCZ71E2V-V1HxYxvvQShEVKy087EM_YNoP7cQeaZiGZcRbxqsMRDmYx4bBayiLEM_p14tc7bBl8XxyBdninUbb3SULuD6jrFXunbAI1unity5YNDB5qb4rLyFOvcOSzAFjOxqKNe9qGgujDESm39hfEwb_Xt1EVM5IMxt3YxcMq6UXA0DSlMdCo20RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBZJ4Fa5STS9paYtUNRZ-d1jPicIfXZ_7At3XzQ2b-IfpYzZ_OhNJzO039gc1O97Oz31LXygE9b8ovoshLa3zdNa-bQ3lEHjXtufqrKKYpw16Ww-GpBZIt81WnSxYjeSZji6WKkkwZJXEJmbcyni5rEOALukeC8Y3P3984ERrRa2xIF4Q7rLjyTbab-3rmyWG7eMwIRG3vbO3-XrKTxlsBpINlzARpaW_CKxGkj3n16epqZCQx0nh2rVNqhWiDhZ2whDECB6VJC02Bcr3m8uYgkiGxW8czHpc30EUv4FlKj-p28ygPjDZr18lmNmJPF3DC8hfUAgwo-JfmVKcrKPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR6ced42JYX7mP5FupK-JSqnNQPrPJYw5GdQI-0g8rI753A6xFDQ_7_vBhP8CEj5aWwh40k7FLlTLjk3BSGsC3k5TY34oBJ6tCAYCz9TxRLdBNhl3bzZhLiDNtc-ntLr9iovWNbRa7BrMaL4lwE3e2wIq_-TOnYWTKrZJr2-LFLrnvrUbSpYgTLLRhXn_764JslQy-DfRgUkmlOb3EUhKgvAxmZB2nKLXdV5Fo4rVcJdf9PdsWk_v3Ev2je81TRrJRiW6FwLKjNCrwnK8-Q1MRsGKD6Tf8ZfHGJHckwTP1J7iN9I_odFVStcz3RWaHNw2U0Dncon9lUNFuYG3wUS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
