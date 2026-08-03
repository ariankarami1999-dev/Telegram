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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 498K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 02:23:17</div>
<hr>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuOH_Yp4V5-jDDnDcA8btBUP2sY6-5V0sQ_TGmKFAUAb4iOuf73-9hjO5AZhqNDQvjwxQDBAGOVoVtF7Vt-3cal-zZi0qwNNie3jyoOf9JDfu5E6babyOISpcTimWNWvhnWAZt0gphhPAcbGNDQepwiM5BT-JavpTAreyDhfqmihzP2Q18TblSn6cTmSkU8bNrBp4tVQKbkEcnUBfpVDo6-FsWbJYLezJVLqQyHnEEChvlzThfsf_iJtO-1AuiMTTBs8SksGI0LbhYTU6DpI5B7KCAkHm0SodArywt11LTT47Wafb1-1vNq6BwUuZTBTUjEwg5eU8G_5i0JTabpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obcSzdhUA0nGrDOwQ9N6RDb0Aq1scTLFANmXh-W2ytRDZICMHzV5yhNQOkTGbaaVwtCxVidsICqA9tq1vZtBU2tDd-GyOueIg536VV2ORtUcLsWSPBkzaHOxEfxMtr8MErcxHo92Cgh7_T9QooSNt3IXEPLCoSDSYsgS2FE1ygVR3OC7_XV7zuNNcv6ciUQAWHUq45dwyY6ISM6QZmT5SK8ri0B_YwGPCFm6z86Q3RrDch4dDOgTrD_-Xd8sXGUdkyokU5sHVZyL0ZMamzxfP2dLkqAlYD-YhYpK7ZU_YRNOsCket_KA3ieK3BveHOegLgj2rxPYUbAW0rzbyVwf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KziZVXHRDlL7BFLJpO8-jSaMpo-xjjDQNu0wbnkh3SpNo5xXOKCms6R2uWNQmIlEW0HrLNwAvAFv6mtmkCDX2x7-_ZLjDkQjSFP1yu60zAkxJ8bZDAuiWPkIwgc9Nm4Jbm-j_owd2yGr6eLQaC10aPD7OXATL8nc5TGeMkxqwW4W6qTdbnkmNRXX8EEmOTruPMqjDysosMyimpHBguT_BgVxwIcjtGG1qi82Bi8ERSo_Lj-XDSx_WONCSPphXfRF8N_TWhCm_caEWvHzg-J5itZ95FeFwXZvSD_o3cNM8LQcJ-aMKfcZfxj6clNbp710DpBa59nqCePv48EuHtrJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
با تایید تار تار و اعلام رسمی ایجنت بازیکن قرارداد نهایی شد
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZlxLj-srXeOdjonwpmkp9dL65bqFME80BHcihJ0I68kGfcaX2L2Zfj4jVeBYyi2Pj0ZgUc8DlCOKKAd1WjggOUUdYWBIt1R0YclF2kj3lTb_IGKn8vXBWBmI5tK9FXbLAn54sqgprjzBCi1QHto4cuv7cJWy04HNhxMVMBm2nxRMI6s3gqx3irko0tuoZJyZ-zy4OsoLzQPC36tYJqEpSm6kjWQD1rkKs8poPS_Pib51mOEi88JMam3XwMKupqsDo9rAkcERc2vCKyDD9g_mTfmYssXA68SLYySWnhGkshIJp58VouAVzQi_VSjGL_msHAXw90uQdsIY74Oy0PvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDFUZcFo_lKcMwrjjHKnpPOBbBZ4hhMSJEnGKeX1HJ7EHzcxeXLz4xYcnUYE60VAX06CKXpIuJMlstKEbih-lZ-X_4QnfydmjRu_gP4QWBMHyzWlspmLharfZg5MD6ZRHM-V_9MeKd-AKTcPDRtSSidHfqt0gDLBEnLxHi0PpZs3kUHgRdlqQZYJy1alfI9XwUTu0f2RQKbWrW_wdDPAH3JGe1t-j39cf5HqSLFRtf429ZxMxEZh-qp_Z1FLm0sK4e34xZuA3f2O6_LRs5pM2LoMlSqTZ7HXa43jWSUMttybKY6xatCaE944nuPWBnwF_xIVmCiS8_84J3OsaGgVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIZAy9ZTRakw1YxTvOYD3GSfikl64AOyC9XrWeMinDws7OVhHEiCyKgxoOj3GezBlyouUc9_Pe3wnwj6kfJSFLYOxo4-ja6sluA-T-ogmvIv4agNEvxdgwpzmDMizoSDHgVIbqbCmcCzt12vhQqOJxhgb48N_le3mG_gAdgZ2WbIKESqEUSwqJBi96a0NKLZMy5JJbJKiFm6IlTblyDDju0dvFOoNmup7SUdaxzH7snlAm1j-4Iw-Wk8mp0Rc4DVjgNGBhJNVy3Oq9qNHUlCvfzjujYGWOaO_qlPelt18nC-qyX6NWM-SwYAqmIKi3dfna7UlX8OUjgmgW0GR-jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC4pYrDWA4Ifo-DAdwlVvQRgcQiorzAHrgh3DyA0LQktav4yrooy_LKRCsctSPdCU5NlJxyPmOaDjO-7wRV0aOflfeJgOPtzKsFDDAylgtj95rBxvx3O6RVr2X8c3Fo1KLQ0kDwfwG72miHYoB9gy9uSCIQ7m5blWkz5UTDP_Kl5HkBAwj0jqngea-p97GaarsuaKoueWbnAVjbQfEuAY6gvb5f-hCUK3_LwoYUQ09bZTgdFjKW-I4z9UQf2qQUu0E4Nn2pRNEtt9PtclKXcmEX1_u4qRAhhaUW2A56RzkEBJsGcDFlRcjUr5BPiZ8jFRxp1IiledudYoVFe_vqjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7gT1QiNqLKATi9zuC_NKYoEWaM3i9kkSo4OIRWZRf6dcRUZn4gQKULC38QGjqL3OkeqUYuWtH5di4Oz6spTFqYbeJyylV__ZQxWfI5tkraFnLu1Jp3ZaKSnok22ABacQ3PjsPhU9JdnMgdPFJJ2o4nSVWzYOq3dwQBDzUDw48g0yoz-lU7p4GAHS5PH3dn2mJHAG3c7hSLPPuXlT5GxWCUgqsfVC6cKgUZ7-roduPmrGVdrH4JaBbeTrloaUvTYtZYYnqjP0-pu7cvX-D95nRKM1Li1kjsZ2v1zVV31Akh6-daSLH7edKpfaP_0H_tb0HXRO_7H5Aos2zk5gabsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAfdqxt1D6Zv-5lQmh-q8sigVOHnQHg1yXi8TmF9SPn8tTRlM14sgRhREYzL-ugJ_TQ93z7bzqDORE7w-OahFYf-8XHeqR8G8LdiOQj1uU2MH8rGogJykb0PK-Kw7CaVcvNnwFIJ2fMGfpq9fjgyy1PnNHfb_PgF-buAOLPBgUuwOIxtJsexrhDQJREV-jrROq2Gyl53unF1Oi7wC-Qyf5uMDYiRTelEUVXSI81fKHs1KZzH_4fi7IqZigiEs6xrIoj6p3pMIYrVLAb1d3X0xAnwdiI-40c2FLVkIcmJxW4SfGvChriZScr85VxF_beqChRY40wL4bNVYfWf5zhmTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRn9Zwurded4par3QENiQODDuEBbdTPBt6N5MN-WyYGz5si9tgoOOLTfvHtavxvRX1cLUKqz4vRVoUbwjIncxcla2iXPSvaPdKSProFb6r0UDfl3nzVUuwfRNke_t6hsAJ_-iQlttzOi2Ddd3J4IoJFETOQY6xJkQizN9PhSe4SxK8MYSofXWdzckU-qREh59rjE_Z7yrZl5YjHz-ysAFQ78MnbLWFNn_ZT8MqfuhygRgBKGFMKxc22xkkKdUGNxrhyoj5tD5atc4iNszR7BO824sxF-v3Ixcd6v5esM-7T0ngMYz0WA_Fd5s5ZM8920RD6glJPn_tMrBszYk4plSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3MSHLdEA93RxTZRq0k0OwRw64pmHCfntfS_cB8GzQdllWsHAxsfIgqsydAvqMb4WtuEp-38JZGOLVAe9HzsgYSyczClys2HF6W8Gztewc25_OBuWg9zRL-Tt_BMXLyhjWmrMJxULbav35C50gChw_LaXs5xez9xBjD4M1HQoR_gD-aUFToRgtBPLbZ76Se6CgJgDgq_79mgqoBTnWT3UAeTFUTzgi4wYhFXhsyoHbOrpqyeoSGy5BeivgJWp0Y7bbQLzePUcAaL6qQe2QmOFswaQAlMcRW-AvBhryqkuV5ILHwvT9qym042MmfDVmc2xT7HXGKwF51fRx2DMFsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQT9816BZr-y___1Zcl1Nv8owJg4TgzTJdm_12YJ1zOSzxMT3aq0eAdFn9r6DgOBug7d42XJE8e6Q1HQYyEf0h-4wBEsbOUBqxd4AXl-KMmhpo-I9RJMQBHmw0bC5KQ1eGaFLtXSBpm6-WmpMgEHGT75ac0smzcIQsIRWmqa5aEDISqucZdxjjMU6F55mfFXF7039BHFSjipsDMvuYB9C2Aog28KGoPQZQy0QroFmLTUvREw0pnydtjxtUwM_QLMj2ppNCK0hRxRo57NJdgOHK3rb44exNsr_y2TLyrKXR-M8yZ0yOmPXdW1tClkLnFOyFyJXUExMCnfdvUmShKeGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx5XO6NMefhBIwQT-6zEs4rLexupecnmfet_0JqDODeyGwu_n-zZnEiWgTeYg5Z8FXCK1gKvE6mJbQatc0OtHi4CqJH_Tvk1nc49h_OPNL3xpwDpK8mAvN7PbGA2zXmNQcGcs6tVCP7y7Z_RHs9lOscypbcYhzizgtGSz_QT47DbRdtz548brvqfvrNOS72D9WRRwgGk3AS0HJilJE0iL0qMPI_WtbjIT_J-i3j8eLV5MnsbnRaQxd3vGIIRr-zBcYiAnEkYu2LQ1INeRGe_FYxrkz71r5Ljy2bBC-zKPBcjpWWM0PvGHCdwqDEhryH_OmBBWdkbecOVyUr54FBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pXyRH4BvmWjGQB_0vBf3MFFW9OJo4AVDnG0UgRZDjkicT2de07iSyh2Npec8j-DW9-xdv-WvwlFajkgKgprOAhqlIogOhQgUbKmAlqtFyC6SK4XRE_vpr7IlVHb8my5tl9Wkqdrad77Jz488EgLF_MU2d_PZRK8GkDga5z0SfY3Wo721oQ5MDu1PY7GfEgGCosSO99kO3nWBMXjD3QOzVqCISGPH-0DVVHX2f3tUQbutZWFZa4nfVQNwAzhtsXJAzdAe1Ex3ycZP1abvMIuFtWPqlteIJriiwwWBCw_bghrUISDfk_IYGIeoaYlKoIKb6kb44kW623LOvehA3iWC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcQLUGi-Sr88dgpO_s0h2dNKiVzoM-SFk0tcZ8wqnup8yBYjlrMb89N5DMtlA6-5UVLVS31Tzz3yqfQpsNPTZ7N_S4i1psIlfTYeaVJx7PRWcs1nYpETrn92NVBb0_6yrrLDwNswSOGnZykAJlESpr59yiuH4druKRpQXm2m2Y-LxMNdCJOQTeqM8nWdWiCUOx8ww_2h-724GPh5T-5Su3vqjWhkY163KAKG6opujPqDdoGOe2ID-hEBE_uK2srS1JEP8x8-bmxXlfuoXeD-3vx8k_ZNM2tQsvYCBesRwq5CPY35ocnDdP4TQloGVMzVOGFXg6hN5M-8ygw7VPzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCAz7t4jTYD4buu1vpnvFphl5OYcOzqjZPgvcDFQoO7AZAn_mYSuSRnXJW40c8v9usD05q8C3ufdbZBkZDsjAnnG0WV0IDE1UCb-NzaeVPwUKUdFWCSNNMNnQeus2z_zkzz1LkLzBzgVjNEfFTBi_D4n8luokoxcMempvTrwnnbcFSIlKD3zc-DLGFvH6egYEkbCCy-Eu8Z7gR6T5d4zzzmbKx85SOzYDBDvLq-jfSr7OK-ePMBg_W5AVdMDGzCRGHOpZthcpdmc3FTDgy91HudEX-ddWhvI0ql3MMIfx8hYrdlY-Hzfzd-SImwEc0PIZq4UYpzsbnCCiiZtzt9UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEA_HyimysYkoN1OPqa-ySsQ4dkk5VklLOUKLtpc1QzG7BmSHptD5U19EcQOu1s6SjdZvyyZQWS1HWYBaOtG1xSIebTkOZnEFVXVro8oB4mHuu8xtgLWBA-IHkWcYg26OOWvb9Ar3zIK9auFYwAaP2I2psR2BrwSRYiJ8kccWVL1OKzL0UvI9I2LW0d1A85ctSWkU1GiO9RYuPNzEsyc-awAS3hya-DES8mwUbxx_XFBlL0OKoKtr5LUOzgJ4gNMr7e0MaUAFX2Gwi27ygNoB7fJjg5EaZQJ2yvh_beT32qtV_3CmwtgZIUB4yv7CnOVQLPItLU1w9-EltcVauYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwJueIpBSmSfl8eoUsIt-zRLfMN4oB8zQuiWMP43Zl2nJYPtRQ6Uq6p810_sF7X3Nrt1GuYB4GwCPLpV9WQtJNQf3R2E5jOZKGWq5mOvJaQJnPghuTmG4M9ix3RzbE86ewLtPtAqo9CVYt_BFH-ctDXgNC-3GdkGQSokDKDQiM21IQoMKkl8yPdeTH852GmO5NRd3gaLdrOmY4BcH58JwnwH0RA4K-eIydwUx0dHRC8YgfApXnO6LZ9ylELxWlXu45xEWk0okOUx_cgrBuFYp4-SammqTjC8AAq6M_4jLX9-0VL_OjTJQcDuaW41f2kTiSzMFb1kYbEjq4iY76ullA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnyKCdiK8cxNLPDT-sk67osyULAR2zL9x8tMjkF0zGr8wuScyby8nG-0-SrZ2V2lUZwPn6mj3lRtJgrCiC1_nFZfi-K58kunEaDJG5ierYotCfOQuoXy06Vos-PtOJ488RAmMklU3S2qVJt_Gz99j2Tzg0637UgCRvWlV_2kAgKs_UM4ufDoWSSeTSCJI-R2eg-eVL8QuzIvK-eMNNiKZQlB2C0THI09aWd66a69WMVwOoCv6ZF7Uc1oq1-OSu2YpGKOJVbIIxDnfTe3qWDkCHhLmAg_nAEHokzuL0rl2znD_r-gcxZFQYGJvRcLMnBPraKQ1-_5K8U22npKoKbfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkR0Ki79ECeVNClilmNuAe_9pBUNs23aF-nB-tSyGtkVU2Rg-FdMEcAI0ALm2UJ8VpcmrSXa5bHJS6_tbqMtGPkkEM5V9tjxg1mGv1TvYuctK_cJvoT9rRWKjuc37yjVh2XbGKXF8zpKh-P7S_EUCJEXaizgEGTQWzU9by86fTfzwQHfSLMUa6-HWraS6TdUS-XgqGD0dqwG2LQHB7cEjsPNT-qTenT04xvEViwZ0x43jaze6HsYt1JD8U5QVBWZmvSaIlUO7K_EMvbz3PF-Ym7BCDZ7GGGC_GUgO-_w4OSe5dBL4iJogotK8qwBd-n-AwaR0oCq6raoqNZycRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKUDyRhh9SgEqYCtGNHOJV36p_EJPe6FkCfLEy22YKG8U5pG2pCaEP7CVdlbscG14tEEo9wnRI4pOhEROsCbKIeWta_ikNUV8ih3anrsSGk-y-F8TQ8ziEHvQ2FlDWhS9kICeKeyqrWNnCtjAmzcPdA14-gvoprBoLJka-p6HrFtgkl0mgN-u9396UIaOGiYV82HtFJkCG9zdajXt0Yi9OY9E_kVh0vcQwlKCU6BfEO_fYhqoDweI97hhxE4B_gz64l6-RDfDsjP1tfj7ouLE9P2_cOITr2P_vu7H_W-7EyOCmdSscwanGCYIJj0M_Q6MaFVcZcXQ2oawYbYkduTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgh7HcoS3TxTj_K7GcAyXTVu1hKhWdN-e_0f7h_nAiAJVWZKVdKWkzZHVhvd1UvSOmlSgysEMBTxHCNerHrvH-Ncnf6U9qjv2Te_pxxJExfIkXcT8AubF4lvOR7P7AHrzsm-9szgGQ5rDJdBBew-WnINpfb45qlFu-ltjA2bccJphc4kF1Vg5Rx2gDak8Dfer-0-dwybUlSQWFTEg69SaGP4fNu6JHmGu90BW7wN31gnwaXIV4NiqmVCExzDToJ26uD7v2wH1gH4jazwDJFsHh6ncbbyYHu2sUegvZYDyS-u5oUuoZkBk9L6YwVGr2PyaOThIPVcCFFjx1iQHjNeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyyzfG7_7fSr21I2BytNQvfMmputyodIEyAbRQ9m3USJNMTIDmPcI58p7tb7oKkukmVnvvEFG4lEx0S24Z5swS8x0_zFlyWkTYY5_cMytJmV84JLcTNmAdmnPjOgVqhch42H_iZFtMANHRGAA_PuJ_WQHneIAG7iUixRbxAd8Gj836oCoz7dYOFTTTbPPojma4LTwB5VjsBYJhpuaxlIUrQHT1_j4RApX7U8FJb9gVNgC06O9nfZBIDrwflNWB5ETL9jzbfJW_ZaxJeJr4gxZ36PCWrHSlUU_fJAtf5IQ4RDYdocA01K1_oGzzcYsSDC3VH-SlvGI9yKTG-zk9FXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVP3qBhEuFHJw1tmdWfo3-BAtC-v749G-ICVtdnMTqWN2Mhk3rU4unRu1NO2gS5Z-3woWk3Szq5_IqqcU5tcViG_cBVcmpEhWunaNOxNf6-74SUXjXKbeeFhNDUOwkdFT32IeKXgKCbvmKG5NfLB1y9LTB0OmTI6oo5cSb8S1PgwbFXfQAFXZefOALIpahW6S1hE1yruAz0x9tiXNqXf8TX1JRxRCS8v1rTTVkvguPWBBWBJn69X94oHhMncJECenqSLvEt6kmqZ2rh8-GPN50z5JNpviRJBEhdWcDQGo3P4JkwLwNR9Xgnet-A_5fPc6CaBlPavQ99cXjpGDdD2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJiRknv3zPgDRDlVRjS7-OywfGyaD1_hY1UJgaXhaskV61T7ra-vJj8p9gCPGG5DMn7XP8Vzlo41fYCshnKST-0WnKSr5YaAnL0RSmo5GKB1NlrZSW8hdUhE_CzEFGWEbOsq7lNtd4zip6bwhwtVJfspcCWQDO8kR4XOjVbxsBbFBn42zr_lH3-gUO6yrrVmm-K-4hTkW_wl4XsB1waWgmFOe9b7D9oM9qJSC2cQHpBuX-q-llIbTaPQdrnRpGq0EjcHb_YahE7rUrvkr0jgneRVXXQ1Q_7-03fKvSO4pomh-7DqySzY-7oBpNWWtdMqlJmkdq8MdzrPHSeenjNh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxSzOAv9Y-26PQvKJyXhlQyCnR8JtOi50tDd0qUSKUDYSlt7xQPpGEMurQYqXnl6zde7cC2t2xbg_ezqkYaC7hGGdcoRgDI50hPTyXsSI9YnifROUDF0uF2Yg6B4nv7RmV79fKK4B-c_b5mzbAqFrkt8Tpr-_7ArQuNzqPPvA6pODzXLCAM2gzq827xfGU-4r7ZQPXE_ObQyhGWS8GHa6ueT9dKismeZ5UXzGzzbHaw8geBoQwXAnRAfF8mWHwQnJyNjT0sp-Zi0tKjOe3r80YfYanjx7WgT9IiCYXMBdwVdUtwi0TQoamFVYacAZa4sZy8RXpizuORdmqgFwiJ6YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv9ciCdr35efEW4EAKKXywPxu5VXDi_q2E5VIT0htDgfMhdcTLqLmy0tV7dhyxiW-6UaceAwd-8gJtlEFDWjDfERkoPDbg5gWE-dKic2VCgMZgaucIJX493_8jge3-PHUyUUw8glteo8s5fHrxtuDgunX9RZo7n0sThBuRidEOe4ZCJpMmic4CSgFCz92vdFlBwOQdO7DSj1C-CdXvRZ3v-LFDfmEkSrRbUITRTmYwHWX66CUZOAVX1l2GHaNrIanMhXkycJ4D-icE8AjhcrhYFVYaHUzH5t64u2hvyW13A1AlBEkWyA3ICNtI9JTpHKG0CZ8GLgLy1H6uLrklCEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkQcb5rJdg7Dwewc33xnsqWxhUwzoCZ2DhPVJQDgheenRU3A-L9viHsyn2H0Eiw-3ld4XiAuEIVJYG15FtNnku4Dez0NQSwPoMF7mp_ccU3rajiX8rvje6iKDJ6ccphY6y5CCqRXwafSgh5il5VPO9kvWAKveIN4lpOBoETpBhhkVDddf7-yzMALmHPiY8-0jhQxZmBWYaz32UslYAwLOv1JpRMgNq1wyhGMwoymVsm20OcYVvxx-Aw_X4p91OG0kMa1DJ2UA4b1KbriPZlxPb4KGM8o6dD3OasgtFYOFpDnXHHasYlS0PX0DFPXxpW3AjsE4VvCBw0ERK_JEUVN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=pHFmgtcqZAX38-6r-pLPqDyRFyvDWx0igP_NJKlsojmWPdO8zN6D97EJ_FfTheZrga2xmX3XrJkHb646uDdo-LokHITuAs7k1J9rxiYLt2wCdjDStr5whQWehbKRLZdgZoSFlwdRsxeHu78U89LyVAbNmV7HGiVl3ggbp6-_fgAZ6Q9wVv-_IJgwj41dsAh0FFHoWkKUJurDjM0lYw7Le7GDZ7B9l8HX0jrzrpg4zasZxjKPyB4lUvB1Ww7QJncMsfYZaO-B9H8Y221bU6mYUN-ypGD6YNYFiEDSAKvfg3tV6qMbN9LhIeVpP_CsV7Apkztx8HzrOCHkZv1geYtuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=pHFmgtcqZAX38-6r-pLPqDyRFyvDWx0igP_NJKlsojmWPdO8zN6D97EJ_FfTheZrga2xmX3XrJkHb646uDdo-LokHITuAs7k1J9rxiYLt2wCdjDStr5whQWehbKRLZdgZoSFlwdRsxeHu78U89LyVAbNmV7HGiVl3ggbp6-_fgAZ6Q9wVv-_IJgwj41dsAh0FFHoWkKUJurDjM0lYw7Le7GDZ7B9l8HX0jrzrpg4zasZxjKPyB4lUvB1Ww7QJncMsfYZaO-B9H8Y221bU6mYUN-ypGD6YNYFiEDSAKvfg3tV6qMbN9LhIeVpP_CsV7Apkztx8HzrOCHkZv1geYtuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=hnlHmbkwsF5DjqpzC5cdwZDYpD13C8hLjgN8EkhwPRtdvR7E3cfGAPeEHqAB2AmdAN3_VE1mvmUg_yZB3J6vDZwK96L4wgzsaOcknmCj1wQMDPNaF2p4OQMhNzzhTFxen2DPxE2V-408UMY-xKxeTY4WQJbCKvuc-vP1mQQmKiFPYV2TkHXu6uUtHQeBv5tI2Mekf_nzeAThmUbpt7HAV9YbhNn-i3bBHGdqLCcbf-hIAad3RL6pr3H_EIdp-R81-w0BhzW0OfMllrTc4TcMdCMNeZiBPiL8NBNROM-cmYHBzj3un_5CX4wW6mx6AHTRbcVDLKhDVMoHa2EuI6pLdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=hnlHmbkwsF5DjqpzC5cdwZDYpD13C8hLjgN8EkhwPRtdvR7E3cfGAPeEHqAB2AmdAN3_VE1mvmUg_yZB3J6vDZwK96L4wgzsaOcknmCj1wQMDPNaF2p4OQMhNzzhTFxen2DPxE2V-408UMY-xKxeTY4WQJbCKvuc-vP1mQQmKiFPYV2TkHXu6uUtHQeBv5tI2Mekf_nzeAThmUbpt7HAV9YbhNn-i3bBHGdqLCcbf-hIAad3RL6pr3H_EIdp-R81-w0BhzW0OfMllrTc4TcMdCMNeZiBPiL8NBNROM-cmYHBzj3un_5CX4wW6mx6AHTRbcVDLKhDVMoHa2EuI6pLdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=Jm2agT7bzZO4WZCunoXGgvQGBUYLRzI1QQ2qMVzMmvUha3D2zbnqQnCgW-u9JDI905rw67TZraO2j6N3cvOzlTvI-e2QkRNUvimBKcHC5v0BtHY13v4HTZyMa-kQ-WMp6s2MApBF-klJ0KFRZn0uU4JSUmWj5MOLUy77HMV9PHNQBt_-jN5UuOdZVBvhy4HFbMll_J_RfeigccTQK0Fn6KV9btrrTnf0XAshzjgkCz0fH1me7qoLjUgavN6slMXh7brhkgKVPqAVcVlBS4xoyyNuNLGfAhjm2UK-lPSmfEpPAw2ORaIaMhr6E5EA-ZlxIItGqbLD4Jl0l4x4HflHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=Jm2agT7bzZO4WZCunoXGgvQGBUYLRzI1QQ2qMVzMmvUha3D2zbnqQnCgW-u9JDI905rw67TZraO2j6N3cvOzlTvI-e2QkRNUvimBKcHC5v0BtHY13v4HTZyMa-kQ-WMp6s2MApBF-klJ0KFRZn0uU4JSUmWj5MOLUy77HMV9PHNQBt_-jN5UuOdZVBvhy4HFbMll_J_RfeigccTQK0Fn6KV9btrrTnf0XAshzjgkCz0fH1me7qoLjUgavN6slMXh7brhkgKVPqAVcVlBS4xoyyNuNLGfAhjm2UK-lPSmfEpPAw2ORaIaMhr6E5EA-ZlxIItGqbLD4Jl0l4x4HflHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=I46W7Fz0JP259XDJ3nQT5cyOgKm4IqNYNPf9SmRTTp7laUsKdyxTyW4NlHczS_t-p8DJoufPwtAXS-aGC_l1TfWqTkEz1lp6URB7AbR3Yg6hnS5s33lB8e-PWmrANXb41LuynmYZiF0RSnVXNKeeSTklxNzbo4ORSXuIiVaMuxj8psV2oEutkgQSVbUM-tFneio2qNiOq6oBOC6Qmc9I-ZfNRUYu9YIwQyQIbneaPTpjEz81cqrX-Nc9hbAq9BMScNB05F2ZLUM9JowDRWqdNjiZUdjPEj24CyzOPAxLx4OJIN8nlYlVNWoH4n_xTiVuEIIXONxtyGDFRi0pulCO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=I46W7Fz0JP259XDJ3nQT5cyOgKm4IqNYNPf9SmRTTp7laUsKdyxTyW4NlHczS_t-p8DJoufPwtAXS-aGC_l1TfWqTkEz1lp6URB7AbR3Yg6hnS5s33lB8e-PWmrANXb41LuynmYZiF0RSnVXNKeeSTklxNzbo4ORSXuIiVaMuxj8psV2oEutkgQSVbUM-tFneio2qNiOq6oBOC6Qmc9I-ZfNRUYu9YIwQyQIbneaPTpjEz81cqrX-Nc9hbAq9BMScNB05F2ZLUM9JowDRWqdNjiZUdjPEj24CyzOPAxLx4OJIN8nlYlVNWoH4n_xTiVuEIIXONxtyGDFRi0pulCO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjJ9-wGIJbb-_spwvzoaqoS5BH1ZcpnUfrfP71jCpgemY21sbywFinPQdlWbQUAAxklVyFTznbnqksSjrjEaF1Ad0u9F4Mz5XQk2awWDXa9agGCbgOSiEgsKLFis_c0qnUg0eEXKdaxMKfxUUws74HXDumIoEVOs7lglNLcS0YxFI-I5sMMvNy8z7PKUdAo1EfDx4ctI2t0_sCV3KzAOqstcgW2MQi-rXs8YzyVydmtpY8TLJ8oXbxqukdFrJ0UOipjofS5D4Q2bx4ukDoF-ljO0X6b0k0kBfB8zt_uDOeKJViFtVE8Q7QpyKfBwtnKX2aFLuhoDaxpa5ChlViZVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_YbMT1mYVarKt8BFqgsKd0k1BCmFNRcVtAg0VvbH8kROiTGaLDcQfTs1BM-1sioZbFQbeXsY-dUi53nOB0NF8DFHQBz5HsXkgAAhRnF-d9Y_UjEhZhRgRMPmizLM3U6RjuSrLi5xmCCT8xvNc67NZ9_8_s8KH6crCthth5CDTdM-Atvs4YDT-vW3Fakqoeg1dRVrGExR4B4n35obygY4tEdRGvpQ4XpNfmPza5dfrnqnCl4-h1bQbRm61W4Cgo_JdER0zmB-mF34cFI1_R8BvOgBaMqQoDNStpTKF34z20KOhkg18xetGiByHXixkAmFwWRYdxZlmlUMQl56IemcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=dh_LI5XW1NajRoLnce4LzgxP-3leGaFPdLdDqFZE0b5dbjZw4KG0Q_kmwbQ7qJjoGzR_07Z5SuzQocbnILYyKNK2ijmH-38zywt12L5TGTKxDrj6hY2C3eby55MBoGpJBpYJMi3VGzRoUe2ZwybzzPS0o0D5FvnKrcFYuqeBMyM5-i_F87UgmekhfC3_qQ1iNpj9Tt6pYgXq-ewtZ05sF5IdxkgbIzsm0ZembI9a7IlZ27Ypiv88QPakhx94oKjrqCDAih3M3SypYm3tCi6zlHzGTIjnksNr8IvP1PkUZ0-5UVaPZVto8l7gsAKs4684ImTM4qSwn76677WaljvnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=dh_LI5XW1NajRoLnce4LzgxP-3leGaFPdLdDqFZE0b5dbjZw4KG0Q_kmwbQ7qJjoGzR_07Z5SuzQocbnILYyKNK2ijmH-38zywt12L5TGTKxDrj6hY2C3eby55MBoGpJBpYJMi3VGzRoUe2ZwybzzPS0o0D5FvnKrcFYuqeBMyM5-i_F87UgmekhfC3_qQ1iNpj9Tt6pYgXq-ewtZ05sF5IdxkgbIzsm0ZembI9a7IlZ27Ypiv88QPakhx94oKjrqCDAih3M3SypYm3tCi6zlHzGTIjnksNr8IvP1PkUZ0-5UVaPZVto8l7gsAKs4684ImTM4qSwn76677WaljvnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=Cdw_PwLH9D-Z1_J9D5-nlrJNOw3duWxZVZkLrkpROtpu7jzQzWk4t7oYE3zJ194-ygQdxbFkMrTRi1D5uBl69C2pU1VnQaXbSc2OMEfz46LYpCoORr7eoLqXM_qgcaPdlpuGT5KGs1rjJil5GMk4LJI35LHkToJt0_3lNLQ74zKmUVV0cUhO7zOl9YNbDwkYkysSQZQSbf9mfxXnoqUzhCb1Ta2BDi7Osk0NB1xcW7zYKyoxOVhq49rOwGzFEXcBRCIEZAIP8WzV790SukldwJ8jQ3xYUH-mIwUqOHYf2duUb7xTGM7HJI0aiAoNNrXwmOQVVLFZJN3cdATQ4ywieA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=Cdw_PwLH9D-Z1_J9D5-nlrJNOw3duWxZVZkLrkpROtpu7jzQzWk4t7oYE3zJ194-ygQdxbFkMrTRi1D5uBl69C2pU1VnQaXbSc2OMEfz46LYpCoORr7eoLqXM_qgcaPdlpuGT5KGs1rjJil5GMk4LJI35LHkToJt0_3lNLQ74zKmUVV0cUhO7zOl9YNbDwkYkysSQZQSbf9mfxXnoqUzhCb1Ta2BDi7Osk0NB1xcW7zYKyoxOVhq49rOwGzFEXcBRCIEZAIP8WzV790SukldwJ8jQ3xYUH-mIwUqOHYf2duUb7xTGM7HJI0aiAoNNrXwmOQVVLFZJN3cdATQ4ywieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjaVjTXNT1QDuOZVCDWkwYOvRflebGfDCz5x6JWCVsqE3tLSVuMT5jQSiHoTtn1VI0P8QGiIjHyOvJqfedvka_YnWc27jBbvE-YBo7aSG7D9DI4u6QG8ayFcwAn7Dm77spXx_nxSssnSty__K_9VJGqYtQj23NJRYczR6zC1qDkLXHBr2Zvt5yh9n3qOuYorhO6UUpnLb5HGtqfcEQrVmm_oIJwNNSUvTNQeXuISPEeerEHfvmGtIFncf32G3Zxlv4zJ_4QPPicbbfKFihMha4Bo5Cg8tovUDKHjRp_UB8cpI3o5T7-sF8tvGkXsPd9rajf61WxxTNOcam4i7i1Llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueo2YZREjtwvV0V-WAsH7Q3LAkJG8b_bPPSu-mNANP1Y8h4xZYEhFSrcPofbEUZ8Gx6OcUYb4JOvp45NN2W3OOavmLzzqTJE7BnWOgwXlDOT1qL8Ha266QsZX-GtFMbwSJXAr2Awr4G1jYtRPVygzJqpX6oTc_HqTwodfuz7UG1vino-DdVmf0Nf1X4wZinFwwsgYegs0CAKKJ6dp2hnYAljnj99hwxorisrB7x5mXreaLDKJ2kMpAOmGbMz_jBgp3KXbatqz5vCjjjxU6YMjMTd_2b8rAqVJpZJ-P4KTLzEXHr2FkRA2EZyycvRj2vgblsQ0bER8AeTrJXJIRm83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=LftJnTI8OjgsyHGsJ9FuaV0CHLZUbBLq9HVYMXr-F3nq5DxQVGHrWMYKbFo4QOsPm6C22jz8K4H4gWINzWNrzWEyopS32iq46bOqAy1XKO8va0qSwFUbYNYGWdQ0sSyPR8skZZXjTRuzC1oZ2pnXrpT_Di4JYbmS8SxwZp9pYLJU6eVBwRKNhbGJ8w37fJsrVMNOY53fqomDR3wH3pMbrmY2xYv5NbEJD2BqRTrWr7Bcv1Kou5ipXxmolURYPT5y7ttXR8Iqel_VkK68o8dBFI_8bmn_dh86L3-Dc4tivU070Bf0r0E5qNYReBVT9nHkpwi6gsHhx1I2kGIvT3sZ4YmU1zRXMb5NmXUd1tohmhx9fQgVr-sSwsM_L8djujsoAAfNx9sDd2hkpUnYbwqPOJWrA4GqT5DJ9kuv4bvXJRoFyi04MreRxHwo1nnEtekfK3Ut1bROfVOLnSBPvpwyF3vFW_I5FV6-aoeYyJ-s3M4J8kyMptvc3b_CqFIcZRWfK38WWqgTN_4ExArcBlgs4M4IHpWgriZtIGmmaCIuKITcdIjTEJ_WiEbzPSaHIsYDgdX1tzeMebepD3x-p_kEPrmRdGZGWB_qSGjEa5NcMsUQ5RDRkh1xzCt493cSsCT0g5DPbRvcPq9sRcWdU7EGNY5QuKqQLV6C90nOcw2iSWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=LftJnTI8OjgsyHGsJ9FuaV0CHLZUbBLq9HVYMXr-F3nq5DxQVGHrWMYKbFo4QOsPm6C22jz8K4H4gWINzWNrzWEyopS32iq46bOqAy1XKO8va0qSwFUbYNYGWdQ0sSyPR8skZZXjTRuzC1oZ2pnXrpT_Di4JYbmS8SxwZp9pYLJU6eVBwRKNhbGJ8w37fJsrVMNOY53fqomDR3wH3pMbrmY2xYv5NbEJD2BqRTrWr7Bcv1Kou5ipXxmolURYPT5y7ttXR8Iqel_VkK68o8dBFI_8bmn_dh86L3-Dc4tivU070Bf0r0E5qNYReBVT9nHkpwi6gsHhx1I2kGIvT3sZ4YmU1zRXMb5NmXUd1tohmhx9fQgVr-sSwsM_L8djujsoAAfNx9sDd2hkpUnYbwqPOJWrA4GqT5DJ9kuv4bvXJRoFyi04MreRxHwo1nnEtekfK3Ut1bROfVOLnSBPvpwyF3vFW_I5FV6-aoeYyJ-s3M4J8kyMptvc3b_CqFIcZRWfK38WWqgTN_4ExArcBlgs4M4IHpWgriZtIGmmaCIuKITcdIjTEJ_WiEbzPSaHIsYDgdX1tzeMebepD3x-p_kEPrmRdGZGWB_qSGjEa5NcMsUQ5RDRkh1xzCt493cSsCT0g5DPbRvcPq9sRcWdU7EGNY5QuKqQLV6C90nOcw2iSWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=Y38Lmj9XxC2z0M1MmchodaAp-PLBPIgOSEW23FiDAff5Lu5Gcol0FdDxJytrTeByjuTV_hdMTkdvmihqP4OhrS_4cTtl4swFwJPF4aikGRjlzDfpcKMJbBHP09ATvgHwii347NHAwGcytH7On1G6IctZ-f41R34gkEMVVyyKaYOtbuVo68taOj0tLtihauJQjTW7DcNJawSHiBD7gcvdcGWNUueiBlDNWZOL20lkIZUdCJxkfw2_BkE9KjaeRPcNe8x3lBLjyb5o6EUd10vxIMQE-p-GC7-ycPNWwBBYuWmdZzSwCJiUaElUvhjje2YoebG-isHnjZp6oMnUq8rILg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=Y38Lmj9XxC2z0M1MmchodaAp-PLBPIgOSEW23FiDAff5Lu5Gcol0FdDxJytrTeByjuTV_hdMTkdvmihqP4OhrS_4cTtl4swFwJPF4aikGRjlzDfpcKMJbBHP09ATvgHwii347NHAwGcytH7On1G6IctZ-f41R34gkEMVVyyKaYOtbuVo68taOj0tLtihauJQjTW7DcNJawSHiBD7gcvdcGWNUueiBlDNWZOL20lkIZUdCJxkfw2_BkE9KjaeRPcNe8x3lBLjyb5o6EUd10vxIMQE-p-GC7-ycPNWwBBYuWmdZzSwCJiUaElUvhjje2YoebG-isHnjZp6oMnUq8rILg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw8UVr_vZgRCyjKRNwwgfeB9nVjwmj1dKEyYvV_ZiWloqyH-MkkYySfFomfjZxnHNXvsHKkLl4-mVs1EQayF5uUkIECOsQfgUVi6h0txAYnPArntZtvJhQd_G5dPjh-wHRUmWRJRVtCYv8l0gsavgCF8OM9qQtH_iQyBay3wbd78LQfPZRQEd_eJ9XyAUhFPyS8W0mkdU77gM_Oe0KAHMlP5RESDr-2sLQhwvuDGGU7xiCBv0TDMKdaAHDGpjOpIXlbuCvKfD36kMJyZwqLaipCikuJqbFUD5JjWFxzYwtRO2eoswaxYeskLe73v16ENnAiJojZ7iypTLRPJE6BSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go3sqNqxvhB46ewpfH8BTRApA_f7-3EpQtymXf68rCjiqPwuJRnAABDDWecVee2HGJKO9MgVhZjD0s3oQ4bA3Sd0NPjA57uWF5YsCvUKAF8ZkEaMriSij2bG2FFs7UwtaZJBZ1u6-kp6O6aopMzSin2zupsn0Wsc8Sv2uzaPkNRQOge82eqkmVLz3tUiUppeuw4WeOTJFqd-Z4sIYIOf7CEqYY327A25l83Mz4fRiMY3t5NV0ZEEhN5i2_93wvS3vbo1QXKdOclmWbHZiCyAcaOhEkEPqoCzoDRVa_Y7AvRBa1c-DEZF_KfPGMUa0pewN4_TbNM5jhvl81ef0H7Bkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0XWUjhOpjdWO-adTDPheYV-q4cKObTY4T_a1GsEMC-qq0aHFlMxfAe3TWjgbACgcG6HZ4vDsgu0yrdudUxXRN7qGBCLjJureexaXfWzlt5qvjVeahJpFzIMRILQWyj2xiMng5HbyUpitWu_dm55NUnRpZoT4bVl1jpaj6qH95hiQEeZszekN1nlnL6oAs3fo0R9fbY4r0TA5zWpT0NpJfFZTagyFCt1p9Objd2vsWoGMqwMaYjgmnwuaE4ylpw7OrODe0JFaaDH5GZJNp-qCqSWGLmneV5j7EIbSjTNfwDAT69-lWIvQ4apy5xT2TVrc4pMm2Ucmq1h_FZNOCLK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFDUpgahVbKbm94E0Q6CwCBI8g-tGnWizlDCIonKvrCSBvaJA53VNXJUXp7Ui24iv6RTgmaNvvJbassgD1ZKgJcRyHg-WL3TlhZCBExOxBKy1WB18J9UhAZRGaXVECd7PbxWn5AlPKG_0OU96rGb-7DctkxKiFvrwOqgE0FssIDQcqQf0CIPxB7QUzUo2aX3CoG3U0DLYEptJmSSFKv7gA2NoRAHbxsO_kcoluQN0vHgpN4cOxW5dbibcfTIDA5RY7DA3ue8-gccS_ZDmswD98ranfEh2z8zh4KYgzRaISNKajcKDa4OnJvajw9ajf1CHl-W5192Qr1Y0oQJ-KukOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzCddhXmvdoEkierH_rA1s362rg2JYSsGTc1JpWSI13ngsbKzL_daKLYeYgvxhBzNQAtShEVegR4eJqQj5yga1X8mhYXzG39PohO56gskF77N0z1DnP9E-EsvIqoL21-PEr7j0ZNGPonKv5y1kef2PZCyVL8FaqzxU4kZAClUe-eYHQ19qbXWwK-wUAu50G2zwYSjZmdnWDqN4pF95Pj1_8Jn2feVYZXPor3aSRXP9NNCW-XAkFaeBRo0XyoI35icgev19PrpVlbmJeFb7awgr-Q4VO9pSkrx_-xTt-fPqE5XGvuSdSvoLTdyH7vTqYyw3PwPfZAr0X9vYmIOLRPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBPLoFuJJs08EWTx_hJ_XKdY7WK7yoJXVnwDeGZbwz8bIBqTcUdz5tYZUZ9VW3vPsRHVGiVz0HvNAw_Of5G-7V9jdeIKLVTprT7-Z0y-yHx5aojBVIs7MUqL9YDFjz-B7YlKVdiSnxOv0yxCR5S0XpWBS2cKyAVWoBWNYEnCcPCtZu1duRqRjcWfk76lQ3Y53D_dTTkuQScWINJZuVaanHoliD3tBeJ_UVsaWk8KO6rrJHfLM3lvP52YEIQbVhpAXDle0n23XIqWxD7DwZogrlWIOskEidA1ZW0U5mdxDn8Ix28WpX5pRP9Nx9mfS4K1dxa9MrAlxA_05OAe4vg5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBc9fK9f1rQV5XL7kaXhmFM3fiAJEIrz3Jw71VcTOX7lKc5IzaQxKwMHm8r4rQQyXPbMIeEZ9psQe0V4M-_c2G2E5WLwEwQXIXnF-DixVjkLYVdANSwfaqHs1xM1-0jIE5kZI1kkpyQrGD-Rxo6rOjHNK_RCQiYyNKP1ENFqPWc7r1yNVuBNHyA9ePpd2aGd3gQSeselnmXsp38YQfioAmgMHsYL2NWVVYmoz0qDccCMC8695VEc688SMosYi06IXIt0VnrJbqRQo9rHqpl39k99UufR7kIXhyondXU1m2x04NLO7fZ8kwHdtPLt_eKoW0sICru5c1SscHY70JcMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=QE8YiNVKXUkwWuMbDRJMqgI0MtMzOn8VYBCh5CuZdPYglaiXW_k9kovKbs6Esl-JGLgflbrSvELPWroSsIBqkjt0dBTKO0lcVwK80K-tDO88sVctk7PJa3OAXsJ4p5uNyUBalJJGlH-NpsOyNQeLn0kqQscGMgfu0x6pTIFFGcuZxwlErQUdhiVHvz66NZhjCayM3k7c6beu_y6osT2QdDd_uy68TLqZLPJ6_oIHR3kBT-wur8eqHcvXlKlQXC7HRUwE7X7uBdc0DTMfqBtID9Siec1Giln5TLyBFuLNGvSmKpOa6AHXYh5fUTW6ae92ftEuQo-jl86TCK6Tkocqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=QE8YiNVKXUkwWuMbDRJMqgI0MtMzOn8VYBCh5CuZdPYglaiXW_k9kovKbs6Esl-JGLgflbrSvELPWroSsIBqkjt0dBTKO0lcVwK80K-tDO88sVctk7PJa3OAXsJ4p5uNyUBalJJGlH-NpsOyNQeLn0kqQscGMgfu0x6pTIFFGcuZxwlErQUdhiVHvz66NZhjCayM3k7c6beu_y6osT2QdDd_uy68TLqZLPJ6_oIHR3kBT-wur8eqHcvXlKlQXC7HRUwE7X7uBdc0DTMfqBtID9Siec1Giln5TLyBFuLNGvSmKpOa6AHXYh5fUTW6ae92ftEuQo-jl86TCK6Tkocqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=Pru899TSupaBl90nLeX25W478JBFvG1NT0xMotgn4m6KrNXs5lj9C6aXPfVFyyLjgY0dTom7MRsCVks4nqVyo_-QsXz6MYxk8QkBym2EquJo9VsArGD6RVcPySdzPGR6W0WsXhO50pXuUp9oVVa5aVBD7X6_PFEdpkabGC_tS29uxnNuYaTFkVN53lkMfExKAtyHh8FDgVJsLaU8hPmerBFj0dOf_NNXjMgkxwDngKrZgVnHWr6kkR_lOkmW-4sEEdG6isyyhbrrpPmKo6R0-F7S9ZThzas80YwPaKJhqj_GBJv3JfAnJmEImA0E860OPHLP8UEP6hd6LCH-3fWZhzBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=Pru899TSupaBl90nLeX25W478JBFvG1NT0xMotgn4m6KrNXs5lj9C6aXPfVFyyLjgY0dTom7MRsCVks4nqVyo_-QsXz6MYxk8QkBym2EquJo9VsArGD6RVcPySdzPGR6W0WsXhO50pXuUp9oVVa5aVBD7X6_PFEdpkabGC_tS29uxnNuYaTFkVN53lkMfExKAtyHh8FDgVJsLaU8hPmerBFj0dOf_NNXjMgkxwDngKrZgVnHWr6kkR_lOkmW-4sEEdG6isyyhbrrpPmKo6R0-F7S9ZThzas80YwPaKJhqj_GBJv3JfAnJmEImA0E860OPHLP8UEP6hd6LCH-3fWZhzBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyug1ox7xhxjRdMpmjtIEeGQLLhxEkjOS43jZUUCLd53Z6PzK4NEVGvK0HEn4mPKvpqxtYDNx2eOV0WxkeWntJbDMgvCEIdhi7dz1AJDM1-0vaEtZ54HucJRaypLoWEtER1WAe2EmATGw4guT6t9vPjZGbo36B1I3UNhmqOvgbEJB0Cj7tG-oPllC6qH4DUkoEM37j4la-aQvlaH6KK5tgQB4TDLb_ltrRKY5gEcWgO0eKH0C1XQE8lTjaDpBaX2MOC5Evp0kiUyfZGlfDK7SbJQucP1pzwXIPrDHhPzp1cJ1X7zWE7VF3uRzGNx8Hw2Bua7beHTK56VSztR-2shbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mer5KFmH13epgA1nTuqCbkVVjo4JyekTLy42j5nPexFEqNkvNduistIGQImAv1GaEPmqPXKWe7899Ngt6hnuuo_L2CwOdzADqrSIZEVcromm2RmW_r7VsEZsl1S3vmZz9O5ihNrhe1urjF_9uSnqYFetKEXY5vGRmdsM6gSJweDNRelfqGuEN9c4ESlPBtVMnNsSeNyDw1ktacnF6AXQtgV-iSsuxPda85qJdW9DrnM27tLRcKwrNb3_l1qvgrCjvbiVgCu-Kr2dKGmqH20uw769xNMzoInXBgmj9UJQLvZMm8-iLIFX2fVmlIPw8oe65Z7kTqKOJ_Ghr9m0Op-dwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvpLCIV7YgE7i_HITw0T-RlTa9jn2Gd7r-g5lQKBPpxoFkxKgxfdRkARCJCCis4yefuxISCkHzVYETETRIMdEjvx1oud87zw0eeWXoFve9abvrVX-MoYV-Fj7lQ7w_ofei8rKwkmX5vQNq0hbPTSBdBdMGR_uxbm8ivvGZZHCDNlZrQYHCmpDsLmY_YOMYe0xrDwcSwrAId8pIqPBRKDFH6knQXEcVRTDglR_fMxejnHQU_t7TDBqqGScttSgkQsLNHmN8Veeiu94VF6A7XdWejJVP4UIBrASZJiIUeCcKn6YnTLMxEmaZ2HuCUY4ih6a6BuyB9AgiSrtJeA2kQFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEljjt5v8Udo9PSexsrfDefJUd3r7GKHxcFmMWvoGGCALr6le50ABZlfWIBLdb-_2V-lMloJZKgYae-BgOpFw0CCScZBHL0Q0R7VGCN3DDHFNklV7E1r0cUPIOa5g2N8YhAVTeQJPfLEnUZlGPwJWu4Z8g2MtJOfrldxceUG2JhBzCB_dnhku4rmF6_CtjDM3J_qYbJGQo-PvOB6I3VrzfXF1XCxV-GuuVGVl0uOC6T3rD-G7bWmQJe4rBgaAariOVGOpUJKnDf4v9y5optGf7WV_n5gucu-w6m-BNySRZb_CS5132_-J6PK2ggzPCqcAzs3_Ai-bGlb8IwMZAggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=XXGgzRAO23KNFTbmd2pJ-U6D5PATAoHbGZ8hbcSzZnSsBr0bEFkxEd0Gi9F6H-XpjdeTIy0DdAjf9PvvGhH4ui1dLn6JfDwVHFUuVagUxk8zzsQGLR8Z8az1PTwEKqNzEeN596Al4X7OedFMqNj0WwwSAjcypigNjlLRSt0_o5sqtnHdmtEk7rWAal5WODbRrf1toO7pfXD_QXq4a_GK_g8_JVjTT2nTuTWJqkjEv1Zfxn3og-rMdzWHHPVxH6NizOltzL2w43-PpHhjQnPvLhj1MmQ9pBgEniZnFDpf6aOuPqqgHS-W75GDteXAxvSqijOIACrrdf8EScM4mqa_UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=XXGgzRAO23KNFTbmd2pJ-U6D5PATAoHbGZ8hbcSzZnSsBr0bEFkxEd0Gi9F6H-XpjdeTIy0DdAjf9PvvGhH4ui1dLn6JfDwVHFUuVagUxk8zzsQGLR8Z8az1PTwEKqNzEeN596Al4X7OedFMqNj0WwwSAjcypigNjlLRSt0_o5sqtnHdmtEk7rWAal5WODbRrf1toO7pfXD_QXq4a_GK_g8_JVjTT2nTuTWJqkjEv1Zfxn3og-rMdzWHHPVxH6NizOltzL2w43-PpHhjQnPvLhj1MmQ9pBgEniZnFDpf6aOuPqqgHS-W75GDteXAxvSqijOIACrrdf8EScM4mqa_UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=OqGWA5Btp8ZqhR0eaBEM9Rsolu2zz2Cbi75uWLOnEfWz2Sehd-6iH3c9xuV1b8y88z4CfQJidHQZuDH47XU7PtnY9bIlKF0OZgp-qOjacxFIUVhdMPAiX1y45gq_nWaKhEJPq2Zt3R1UU2qZ0gvkbm_Vwd0b2iFFlNHdt29O5kpEsieD-ysaBVgf1kYVsd7BYB3i1Y9Xe0L_UsH1xqwE0P3yChRlYHkIK3eAzErKY5Tzx-j5Gokf7qmg2Y0v9X8pNK-l1-b9PRWP22bcimQMcv4Pm2cQV3PrhQITNT0vWL3nE4ospF3vkqIVn6BGrSX374oA_RsBrQoiMsWgQDbrDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=OqGWA5Btp8ZqhR0eaBEM9Rsolu2zz2Cbi75uWLOnEfWz2Sehd-6iH3c9xuV1b8y88z4CfQJidHQZuDH47XU7PtnY9bIlKF0OZgp-qOjacxFIUVhdMPAiX1y45gq_nWaKhEJPq2Zt3R1UU2qZ0gvkbm_Vwd0b2iFFlNHdt29O5kpEsieD-ysaBVgf1kYVsd7BYB3i1Y9Xe0L_UsH1xqwE0P3yChRlYHkIK3eAzErKY5Tzx-j5Gokf7qmg2Y0v9X8pNK-l1-b9PRWP22bcimQMcv4Pm2cQV3PrhQITNT0vWL3nE4ospF3vkqIVn6BGrSX374oA_RsBrQoiMsWgQDbrDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6IHUIJGcUe-8i5JVW95V6t7I8R3i-HRDU7aJgfOpMd49caISkvf3jSCjsWpaAoNeQ1qd8VNw5yxwQzUGkz8kNve9lD5ZjXqRx0ic3xuWXwY7fj0qq77Z1gjbGj9BRHRgKy6urV5XDrbOy8-ID6zyX_SRRax2_oxuxHC9PyURmxX16NnuETt-B5_EDcxY-bAuRVgHXqDOBwWcPdkzVmyPTCdVPZ7pvEJ8D9OCnVbp-ytgVNiW01dU6wFbTQoEZhQHh6TcLGhz9toVysVk-aRX10joV6SP54OA6heVguFlIkFGE70DYYp18XZRwn2bV09TzGHH9IUgEyXI6BkCsAjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EthTZoOqt9begtMHdtC-YQIRqV1E81_NlXbx7ZY37U7FVVJabzADZcU8NHyZQ1T2uBcZkHc2yEtZMVjproFpV9pDPTnpDjZrwoDwZXJhGbJzpyWKJkNW4WzTUcfeODlDc3zqpf73LBVrEuAoGpQV8oEoaVpEOR-JX85YJLmsEeGZjrUgpfkNBQf7lav2zfrTJspi2u2cWpzLJnlYUj32m0IEpPMMxGcEJtEMhBNSZI0M7W6hxQDm3doGzvuCR9PR2VM13pRXbDz3txs172UftcN7hyboTAZnJyA0Zw_gVOLLONRqdyGkqMSlZ7I9MDrWKzAll3SIcjpS1fAxD-_SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvypZvi96JSGCCeuw5NhonaLAZb75WqWXCbXroTuPd0Bb0o10C86T0r-EXT0F118rD5_qd0Y40ZCvnGnORwCxzmO0_Ml5Nw6vWr7doutyIfxizlIMSfjMCWbhrywSwd_Qji9EBcftfEnA9CkGVZ8MHge2S-BTVzl-F7JaocrZJGnhNHmHaCJ2C_pfb3Qixpg9PiWcvBes0zY6iWnpg1Yw66K61likYOdSBEnE286Z-zkNhwfG_W-Cgmu5POvyOdzlb8TwS0Rojdg5uKLhjyiIW-d5f_SaPV_3moPZv6jfppPOoOo3xEdU5SKLpfZ0IKBFo-BSEMfIh1vHBNNCXEK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6I17fA8uvZuke0D5lU2C973PEkhTj3YsRA528LuM5JzQeArtqC5Mm9Ud8nDUD9LVNtJCyWdEmJenrCqvyhipMvhf-aF1uTeybziog3XL-f9htsjsXfcBSwPOJS5iJZWXF4fnPgsxPyci7g9Fkal9BDsDSEa9CrH_NPtmw_l9xfBoE0m4oCgmf6xxNz4rGVfQTrWv7WAxEuAV3n5vkZmv5BEn0Q5O69AtvihU7QKkJj5nUXRmz2ybmi728ijg8UWuYeu3t0N1Z5ZSnVLPKIcIT4kkZ7eE6WO-Z23xxSlbQ8aA0MfiA-ZXMFRVr-7M_Xc_9WWi4sdniwfaiu2GxjiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=f3FbNyfIWPWYq4d_OrmzrKxcKU0q3KjSyNsSc3LXYnwwRp1IkShALeRfPFm-1ZD6y9ZjmRbjV9k1osPOi3o5BhQ327pS-9sz72-oFRjl5wDoaXc82DU3kBDyndmWsMQ8CKwC_MDAsoxIH8MOWsrkI4ObJG-WkeLBqfhQGMW1JsJ411MXyDirPKQO1-9h_WxLCoiWTjnE1-lkIDs147uO8xulMaE1r0TXBPww-76QDbxit3sgTIQaBhwYc7qbrt-9dnJyPe9ASzRS-9RzIz2-qtPHEy4Y8Mo4hyl3SwxMqE_xlGnxkUhu4t4Up7c8hJxRj9zktDVKZNvJfzkExIVROg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=f3FbNyfIWPWYq4d_OrmzrKxcKU0q3KjSyNsSc3LXYnwwRp1IkShALeRfPFm-1ZD6y9ZjmRbjV9k1osPOi3o5BhQ327pS-9sz72-oFRjl5wDoaXc82DU3kBDyndmWsMQ8CKwC_MDAsoxIH8MOWsrkI4ObJG-WkeLBqfhQGMW1JsJ411MXyDirPKQO1-9h_WxLCoiWTjnE1-lkIDs147uO8xulMaE1r0TXBPww-76QDbxit3sgTIQaBhwYc7qbrt-9dnJyPe9ASzRS-9RzIz2-qtPHEy4Y8Mo4hyl3SwxMqE_xlGnxkUhu4t4Up7c8hJxRj9zktDVKZNvJfzkExIVROg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kArzA5w29HJS6iM9bf2hygSeY-ewex1gLuQZkk105z7P09AKxTRZQ8rlf3yhdFLcfrHNOnxx3Y_pT443lhPN104J8Zv8dwii-6TLjlezXZcZmwG1zZ6t7G-3Iz5G_wfjy0OTieXLMPFvYF0HO6FD3iYNRQCbH_rXVlSu0hPYXkZ80LuUSMMxMyg4MQlrqbcGhP_4SbXY5t-Cq0N5VMlO09jyU3WAfcrUPRh1x3p3fPyTG-PeXovrRKfrsUjKFMnCCwDBHaTzrq-yPnGQ-Q9fmCglV_oVegoRJOR6qT16VLGOHIXzH9R-HeJA0CR48GHNA3W1jn3GYpytm10UDYBD0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=sqjz7oOjYWjB0y1PMvPpDAwIrWuNzQxjQzCqoiCRhgmQaZJqao7i6bnMlVBmGPhqIKYL-zIQja-s2jw5zSjBEZvizh48KySC0Ij2nv65I_7sR40BWqkh-9SkAeAZcuxAoBQoBDnb0-uaGmP5WB_ew_Dc2ViPzCwVzYOCvp7RNp-pRkrH0ivW1JcrqBV3e-zqD8iKsC4AJnsrLnCVO2MTAwIbtCkJFayMA-iD0oMPjEdqv2tENrITfyxZX-7bFjfkmQbx_RUwIWZp9fMJF2d4rKDPag7VS-oLiqJhFqtdwsj7AQhrNOM3g76jFuPVicdh1cHAoIclsWtxGj7YwfOnwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=sqjz7oOjYWjB0y1PMvPpDAwIrWuNzQxjQzCqoiCRhgmQaZJqao7i6bnMlVBmGPhqIKYL-zIQja-s2jw5zSjBEZvizh48KySC0Ij2nv65I_7sR40BWqkh-9SkAeAZcuxAoBQoBDnb0-uaGmP5WB_ew_Dc2ViPzCwVzYOCvp7RNp-pRkrH0ivW1JcrqBV3e-zqD8iKsC4AJnsrLnCVO2MTAwIbtCkJFayMA-iD0oMPjEdqv2tENrITfyxZX-7bFjfkmQbx_RUwIWZp9fMJF2d4rKDPag7VS-oLiqJhFqtdwsj7AQhrNOM3g76jFuPVicdh1cHAoIclsWtxGj7YwfOnwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkD1h64OEgw9thk8rql5eISEsY-TlPOSTjlBKp6XQ56u4TRX2m6ITms-UyNhweSJui96MivVUSsDbUQEiZgGgfIc1gFzd9XUNbhfvuzniHXKXZ-2M_Dl9G4E79oXvti3i5xEJyqkmlp1s2xBiNWYMhui-z6HCNDJugGzPibsHBdYx_xSqIJoc4GS0bZQsKQD1qD1PuK8XLuL5Rvm90o0IAq5ySH4_EYmp1KuYTK3L6CE3FdvHsTlDPrwVZq1wZQ-LO9uWPrEzXq7oe__WtWeEogF8AfbyNGOWHCeFgg6GD6UD78RuyQwsJzXqUBIKnmEm04fQEBQRWQTMbBSN5DdA2bc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkD1h64OEgw9thk8rql5eISEsY-TlPOSTjlBKp6XQ56u4TRX2m6ITms-UyNhweSJui96MivVUSsDbUQEiZgGgfIc1gFzd9XUNbhfvuzniHXKXZ-2M_Dl9G4E79oXvti3i5xEJyqkmlp1s2xBiNWYMhui-z6HCNDJugGzPibsHBdYx_xSqIJoc4GS0bZQsKQD1qD1PuK8XLuL5Rvm90o0IAq5ySH4_EYmp1KuYTK3L6CE3FdvHsTlDPrwVZq1wZQ-LO9uWPrEzXq7oe__WtWeEogF8AfbyNGOWHCeFgg6GD6UD78RuyQwsJzXqUBIKnmEm04fQEBQRWQTMbBSN5DdA2bc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhy9J4_SICeoDd_Cw0MB86KWutZKP5b_69RQ5uQA--Rwt1nWqYrWxon_rwfRKmqbqBpKi22_0V4DtWwWG_1A7lagxZ7WRjMmgHYCKDzm85V0zYVhIWszn2Vg2lPqxqagfdcQthyFSJ_4WEU_y-nj4G6bzszhQeqDrSYXEdUn509qenKn5j-3bLZQP1M4ecRF2mSVqpvt9VUiehzd7RpmZr6QYU6XzQ6A_waX8gdkkHwkXNyOUBU7bDAYwQJWKgyh-KmIa870eeFucGqA7c58HS74lk7e_XMeqBCn9WQseL7YU9xyMQalbjiMW3mqygvzWcVO5_Z87Bfhff9Zu65VNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhR-paYEyd0aoqtGxLS3MDoxYBgHudb-blYtr76RRZ6aPlon-zMUNVqYpr1WT0bgSFclfnNMxf5Hk5MXxfmUdXWEVmWKpf0oMyw5JPtHT6NUAF1SsoySedrzn2lcIn1cwwJf-p2kJ6SEh2JX21zhcxyb0O_oSwhrK1mtB5LkMVgS-3UvePU-hB0vLGDF9HAVwTgSAHO-OeQCqpqXvWg6MSFhSU4yUEm_CmDTU5VjNiUr7NRnDpzZrmzVUEXXCFs4nfalNgrdZr_57wqf3HhXScphizPcZLIcf2rjvQVplgdEQzlvPUcp4mTkgD1ldLbJttHt-DyBrZFEEakUE56UVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQgXytPxgv2YuO6y7MBB59j9sPpuR2V9-jak8KyfADjNJ-rs2oXx9xKVNsJ2vKPz9P0-m9KJqQPoYE49226kvjqD4B5ew8hxdurXylYEt2v1qwtDmK7f4Rdqfu9CQGFXjxXPpjjRSI3mM1QHQ8mq_Xo_g_DXu90WpYb3gZ9xmaGm3tn7L2tDcLa80YB6_AE4m_vYopt-AHUHma4RSD2WqaH3UBo-oeoj2IaT8ZOBWvseW4s6VQ6Msqw4IeyCx5HqeJerpc_eotpXf_1rGM6PoklDaDpXIa9zf75LY0DzPIOGbsp6y3p-FeQZO_bOMK5BC9sxgCgo1ttxMoXHPKVi8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfS9GrpnW15of8pu_YMAlAkIWI7d3eV-I2S9irC3sgBmVob6jMHLdTdMcwQOb8trq6kbb2xM8MXsJOaUxaI3SfrMHm1wjnHNZAP_7X3Fab9cfnojNLds8flBi7FTkG0H6EhEo3TmDN_4KgO9IfYIOYPDTOCGOopGo92JTrSiZPeZ8TIUPVvojY21qqFtLy9zk4vGhtzaCjqTd6PiH71Ho0GAkFp_8lN-q2iHiMp0lWPV_JRjIfl5UQIy7fasdL00HsSE9qVZmTCYQ79hB3ypGu9B9HoFBDDSJ2r8amiNLMiGOCM44uQRLtv4tuDyw3XD7G0fQm5T8YuBd9bu1TPH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU-mnJnkRtws1JIcM6XiXnvw0o2ND-26UT2ar1fNceYHbASRsZK-1IaqT2TCLysGHYrlNmBCfAXmDozkcJmEEl_4F8wGOnUgdiElTmkrhPm2i30c7di-ygVh_bJW0mD2bAB9ZkQf5jEuVml6iQFe5RpNXDUmUyUyfmDTf49bIlJ3tivDh1SDNa63SRO2nkwyzIUi-xcN4-COomxOEYUq1kbJyrtqNZCSp42Vy9Hh-2yiSx3Q2BQku6W0hqPLIbUSn0o4XQnji4XLqQeyzlBvzFaPTxxSaRS6Dh4KPk2030--8PAj5fN07bVFQEeSRL2LqOJVAbVaeXOjR5JAV_XQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhz_fXnuPUSA3DY0FWEMBZvbr23NcL5T_qFu6ueC0FJD073-k2PbrMAF4hLR91s_q6mmT1afPLTg_UdAS16YY2100dwWimrtrcs2DNwoEXtOODpsLDNSnqF3hGOCQr-98I3Ao5XIhZjL8t_-n5FPrMGPYKgKgd1lLGqjBtUC_hw9Xq0DOp5x_DHukeJKDGtQYoEZchQ-I8hcySJ48qPSxkbD4w7n6uR05IK43Kd0IyjGKyrh4Izf3MtCr8IRgMOhGVlrT5xyXu6__qdm-hyL0PmNp4N6JzSu7yUPIBWvFfGe-wkdP4x2WCXC6ENTGtSr3nIgRZGI0k0Qj-EkdrwADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=cFv4t0oWBePX2UynHQcoPmayfYuff0e2Cfjhgvv8a5u2RKB3tCeVooHON3MbfdUBwxl3FRRTPysV64iLmLbER65u_t_OGQSFby98-_cf4q3rCcEPgZ-eu4pWi_L-OWGhztuva4IZ7Q4l9D75Eq_dMEQioA6-TsNY4GeSifQ7BNkD_6-VO7_YX1gimZxDCxr07Ic8mI5PJ2KrZ4VVHpjQCiQ65fktzfH77vaZQsd8TsaIbhvKviIzojlGjZHh4kFVDf1sZlLLT33PbyceY04N3aBsrK_UdoDJzjP9zxdz-p-6zZ4ZDD-MKAfHbHyiLtpYybNikcogfzRQMByeQANvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=cFv4t0oWBePX2UynHQcoPmayfYuff0e2Cfjhgvv8a5u2RKB3tCeVooHON3MbfdUBwxl3FRRTPysV64iLmLbER65u_t_OGQSFby98-_cf4q3rCcEPgZ-eu4pWi_L-OWGhztuva4IZ7Q4l9D75Eq_dMEQioA6-TsNY4GeSifQ7BNkD_6-VO7_YX1gimZxDCxr07Ic8mI5PJ2KrZ4VVHpjQCiQ65fktzfH77vaZQsd8TsaIbhvKviIzojlGjZHh4kFVDf1sZlLLT33PbyceY04N3aBsrK_UdoDJzjP9zxdz-p-6zZ4ZDD-MKAfHbHyiLtpYybNikcogfzRQMByeQANvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=bkMj4ygWgJYrnsitB1L6z5iP_DHlBxXHHCrTyVyAuXgQkwXJx5w3y8DKaBVAStfhHoIJVJnqW8dLlfXQOSXa95_tsS_qcqQxQ3aAQUr9c6sstSps9RSVk52qXs5V90WhgsC2_ohHHB8XIOsvfHM5Q7uUJ0yvep8UGwzZ7J0e1KwW-if77mel4zgAljadMF96la7uewzwAV_hkrF9q1P4Jz4_yF4OHv8I2lsbHOg2ikGmH-oO5NysnWIIajThfxlfeBAD98CkTYaXs6YYY1aEF7gVNjhVEXi3OO3TuaDf5PwCBh3d6T41d6rdDzHZHeQiMIi2Zby4pGXU-VdlYKf5aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=bkMj4ygWgJYrnsitB1L6z5iP_DHlBxXHHCrTyVyAuXgQkwXJx5w3y8DKaBVAStfhHoIJVJnqW8dLlfXQOSXa95_tsS_qcqQxQ3aAQUr9c6sstSps9RSVk52qXs5V90WhgsC2_ohHHB8XIOsvfHM5Q7uUJ0yvep8UGwzZ7J0e1KwW-if77mel4zgAljadMF96la7uewzwAV_hkrF9q1P4Jz4_yF4OHv8I2lsbHOg2ikGmH-oO5NysnWIIajThfxlfeBAD98CkTYaXs6YYY1aEF7gVNjhVEXi3OO3TuaDf5PwCBh3d6T41d6rdDzHZHeQiMIi2Zby4pGXU-VdlYKf5aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=rwkCm2RsA9LXCB6urr1JBbM89vcNmghSI94MdzD5023q1flkSJiKsBv19RDOkfW3ivNXNF5sAtX04BmLEarjKSuTS4Q5pJX3hro9kFdCy13M5eINnYdf1DnE78d_y0XSSzN2tz68ddp-lEcZdikCX38OCxuMBAaqb_Je8ilOs5-1pSfHXlB2JeDZYXzebzXB-b4gco6_ZnyWgMWV_OQB1eVBCHnYp60omHYNefnWhhbCO5gnY_3DpP2X7bAl7s5z2D1jZnEkDxfuEAYBsv0EASHgdfjdyu-TLtwlh4zithLGMaaKuDdtxHJWcRvHE96vEjJ-5EU7_jwMwHrVEvK0rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=rwkCm2RsA9LXCB6urr1JBbM89vcNmghSI94MdzD5023q1flkSJiKsBv19RDOkfW3ivNXNF5sAtX04BmLEarjKSuTS4Q5pJX3hro9kFdCy13M5eINnYdf1DnE78d_y0XSSzN2tz68ddp-lEcZdikCX38OCxuMBAaqb_Je8ilOs5-1pSfHXlB2JeDZYXzebzXB-b4gco6_ZnyWgMWV_OQB1eVBCHnYp60omHYNefnWhhbCO5gnY_3DpP2X7bAl7s5z2D1jZnEkDxfuEAYBsv0EASHgdfjdyu-TLtwlh4zithLGMaaKuDdtxHJWcRvHE96vEjJ-5EU7_jwMwHrVEvK0rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=uSmezcmdSRft7Y6eepT-3pg2mSeKc1iwg6729JvLNLcbUM7XNk3bEsKKD9utHlBjHXOX94sEax11PwBnwsxrYteWgKQTB9Z2ELYoIHhxpSr4DUNe8NrMGsU2KpTWpuVLJBVWVR-GT1CZqgGJCGmsnuSeTsxDwTV-dF7DR-s3hwly82ffCwHcnBbvRBJWdqCsHy-nCewVX4YpvcTUC5buDgnzFJ-88X1BJ4IKg0FQm8id0g-60jrIxSlktlL87UgjfgCt6zos_U5racTDxhSvdYTf-nopfOwWcmxJwWH6SGW1zGBl1dI-XyAgi6z3lrfhDRszRC96bCQ6qcP6xONMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=uSmezcmdSRft7Y6eepT-3pg2mSeKc1iwg6729JvLNLcbUM7XNk3bEsKKD9utHlBjHXOX94sEax11PwBnwsxrYteWgKQTB9Z2ELYoIHhxpSr4DUNe8NrMGsU2KpTWpuVLJBVWVR-GT1CZqgGJCGmsnuSeTsxDwTV-dF7DR-s3hwly82ffCwHcnBbvRBJWdqCsHy-nCewVX4YpvcTUC5buDgnzFJ-88X1BJ4IKg0FQm8id0g-60jrIxSlktlL87UgjfgCt6zos_U5racTDxhSvdYTf-nopfOwWcmxJwWH6SGW1zGBl1dI-XyAgi6z3lrfhDRszRC96bCQ6qcP6xONMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=MlTHYuHK0E4fcKL7oZA0-65zuHeQEwI5N83fvHeXwBR1Slnpyv_0x3EQNZ1XngBcY5bgdEFKhLBDxlZkovVFcwpBesDK2jZ8pKv5C4S82GcZCndaGGQyK3DnRYEKOtYHTGeCsZC_u090oFlTE55TQAjraXoa8qWc2MBD5RtPifXVj0a5ny4WsaQHWetR-NYja87zexBUQY1DHzob1qNOQcCDZ9cGLVgkpEWIq1dw1hImAlPYY68Hn2BGrZuZOwpRIVmsUFKXVhoDT-IXDLl7TvybRkLN-bp26Q3ifYnNhaz02CP2PDT7UtlS_Rox5WgYRzNOxpDrNkd3WqQ2PkWYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=MlTHYuHK0E4fcKL7oZA0-65zuHeQEwI5N83fvHeXwBR1Slnpyv_0x3EQNZ1XngBcY5bgdEFKhLBDxlZkovVFcwpBesDK2jZ8pKv5C4S82GcZCndaGGQyK3DnRYEKOtYHTGeCsZC_u090oFlTE55TQAjraXoa8qWc2MBD5RtPifXVj0a5ny4WsaQHWetR-NYja87zexBUQY1DHzob1qNOQcCDZ9cGLVgkpEWIq1dw1hImAlPYY68Hn2BGrZuZOwpRIVmsUFKXVhoDT-IXDLl7TvybRkLN-bp26Q3ifYnNhaz02CP2PDT7UtlS_Rox5WgYRzNOxpDrNkd3WqQ2PkWYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=ccv2b2QW91begIF1iOzEDeTp1NLkiRtL_wAG_TtjW-mM7mEt-vLzfQ8bp0u1N-WpOlgoardcAXRnBKsinCUBPmvkkk5aGx6Mko9uWn3dIk376j591XfFZjhnUjlp2SEsQlS6DjNBshCsqfVSOwY9YMO4ew2sRZW_USpcVrbw7oEihOLsjmas47exmkfGdYJyfALI8fxtKIZg6xj7BeBAhqe0soLRJVO9gNf_vMPRBRII4562hxOZHu3i0g4js0Koa4nsV9JR8xAKO89GKKHLGIii3yCXKnLj0d6M4WkDuYWwalnlsdvsclrBhexScuJeR-0IY2BPw0RR852EVpROyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=ccv2b2QW91begIF1iOzEDeTp1NLkiRtL_wAG_TtjW-mM7mEt-vLzfQ8bp0u1N-WpOlgoardcAXRnBKsinCUBPmvkkk5aGx6Mko9uWn3dIk376j591XfFZjhnUjlp2SEsQlS6DjNBshCsqfVSOwY9YMO4ew2sRZW_USpcVrbw7oEihOLsjmas47exmkfGdYJyfALI8fxtKIZg6xj7BeBAhqe0soLRJVO9gNf_vMPRBRII4562hxOZHu3i0g4js0Koa4nsV9JR8xAKO89GKKHLGIii3yCXKnLj0d6M4WkDuYWwalnlsdvsclrBhexScuJeR-0IY2BPw0RR852EVpROyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=oVaDb0b_sJdn7gVkcSpa1jgfp7xLk_akqmU43vlCZ9qYvkCpwJ3FshfWSRkQotT9CHvdeYRe2CZK37C1Y12SvIXyaWCQ9hBhhsfbhfxkFbfGLwXS0C84xCo8Tj3VO1n7mnVZhLJJ7k2O3BUjruOOYo3UoiZuFqzXWR1qdUp3KAUvqUM_aiCx0H5zGrDiIfkJuuF6lXEKH1XaAgZbbuB3yfOMyIsxlngH7AwFmgFpOZd-hTOWq9WjNBX5uZhT_DpCxbifC6ogEjZQHwnvOVS8vDGRNGZJyPzZCwUVG2vpRgApwXCxbGT7doztVf2ynpgCfjjQyWA4-xl64z6-1bdYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=oVaDb0b_sJdn7gVkcSpa1jgfp7xLk_akqmU43vlCZ9qYvkCpwJ3FshfWSRkQotT9CHvdeYRe2CZK37C1Y12SvIXyaWCQ9hBhhsfbhfxkFbfGLwXS0C84xCo8Tj3VO1n7mnVZhLJJ7k2O3BUjruOOYo3UoiZuFqzXWR1qdUp3KAUvqUM_aiCx0H5zGrDiIfkJuuF6lXEKH1XaAgZbbuB3yfOMyIsxlngH7AwFmgFpOZd-hTOWq9WjNBX5uZhT_DpCxbifC6ogEjZQHwnvOVS8vDGRNGZJyPzZCwUVG2vpRgApwXCxbGT7doztVf2ynpgCfjjQyWA4-xl64z6-1bdYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rae8SIuyOR3f4eSiZ593_w4wrqvEXwNygjlpm8o2yMbSYZH0pWM02LxGa0-IXEoSH8Q-9gLQAo5fgs8r8o0lyNntgIrUs1f2S95jVvjQEC7V2iMIErV4jamg5MA5AqsH_7lkvhq9iB9osPKQFgQ01_nhNcIm6HFtb9WSCzDCQ-4ClvQ7kWt4lsBgNAbgBkp73_qNGa1X3vept9ilQ1Jr0Ja7Rvuhzg8xFAhdZFKGS7lXYcbgl3tUOZutY1t-pQS64QCjgl6jbW4gicvrQM8bK1AuXABzwL5NmGjiDRnSeDAwUDJkuzKVm_hvVjj3g0qSGuwqW1JZb32m8kRoEGMPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=f8m__pPiLNcccgtIUtGCJkfkTAWhCE-Q-ZSfhIeaJpbxrbVHdcnedg0sMOa-MjKyzipvK0lU05sQtYtqsLjen09Pv552_CIsZtSLhd_Ys2vnC3HGPzlk6d5hemB9VPhHiqaQuDqfF6n8_yp-BRW6P1BFBYfREghxsh2Gez9e3gwF4v3EcyThnFQINKYMsjYvDcimyVlre-kVyLLzwztdXTWmh15g9jEaM93ZMyTsjvKhV3YYHnj6E9NC-sORZsyh29oNTphTsBz6yb2r-gxsCX13yu81Io7idp4Ym2DpZiLUn-HDyxDQl1KzJ_R_HhDoaFQjtUTbujziV7tFJ5O-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=f8m__pPiLNcccgtIUtGCJkfkTAWhCE-Q-ZSfhIeaJpbxrbVHdcnedg0sMOa-MjKyzipvK0lU05sQtYtqsLjen09Pv552_CIsZtSLhd_Ys2vnC3HGPzlk6d5hemB9VPhHiqaQuDqfF6n8_yp-BRW6P1BFBYfREghxsh2Gez9e3gwF4v3EcyThnFQINKYMsjYvDcimyVlre-kVyLLzwztdXTWmh15g9jEaM93ZMyTsjvKhV3YYHnj6E9NC-sORZsyh29oNTphTsBz6yb2r-gxsCX13yu81Io7idp4Ym2DpZiLUn-HDyxDQl1KzJ_R_HhDoaFQjtUTbujziV7tFJ5O-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSQW5G4pC4qswHWx65MQ6cUQeGNMWezXAR9VT0YQ9Sa262utoAh9_j5SNKnRqTm2Sx4k7rz5Q7fS4czUx2bUK38OL7iLo86D9PQS4Ufsl8JhDNc5nFm3Q9yrkTpiNwyWeMXNKXdFkmYAsSMNXUjarI87620KPNxvBJbjsr5nr4M1s_P2ZNFvtapmGZ2iwFlYYTib5Yl_suWs_jPIOQt9aQvhbP8z_hwCqcuUn9KI334_jN1JyYic1gRH9ctz37Zuz8EQjNf4exeUKroN3afWU7GgMrXVrDkYPVVMWpGZylvbVWEIRxl9QJXXu-8_Xd3LvDrBlEL7VtXbILfHVCHkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
