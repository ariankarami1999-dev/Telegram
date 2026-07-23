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
<img src="https://cdn4.telesco.pe/file/Hy-43fF5_pucDh4i9ICWmaPkamxKDXaXLw93TRIUgNvvnJGOa12lfVMVRB9YnbNgvvtgVkKJJnc0ps-5s5590XN2PH1ZKKwAPG0MjUgncrs4MQpI28n8kkienMK66CGqKCJgiLPZXRXwBPSJDCwoVA_eOc4kO7Uw4foU8Pc7e-GVWEpSSOTv_SOhM_31KoxC7jpNuL90JENOCYlaaGZVTbcGZGrMurl44m1coZj-sFPJb5D62WaWBc54fp7GxUWhjsUvOwt71Rkv1VW8g1nbSv9pMdX5pgj-TY8HYMXCV4uHBc854Dxv1_-zAqyX75m317e1FSEgF4hE_tjk-cXhqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-136930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
صدا و سیما : دو موشک به شهر کنارک در استان سیستان و بلوچستان اصابت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136930" target="_blank">📅 13:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مظفری،نماینده ولی‌فقیه : قرارگاه مشترک عفاف و حجاب تو استان قزوین تشکیل می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/136929" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhHy2FKclov-tmdnp64M0I2nUX03B738x5jOd9FxfT83Oj3cacBnr85TWQze1woCZ6zs7AOZujSUvD0wgF3umnCFOTROf5HCmvZ52EUEbvHWnxE2c3Kipg3CaTR0YA5la38piv_HqdFHNI1ZVjxNYuhq-yCGLeriPBC0khzF8JFUGRmcI4cGCMt89SCUjQTgFecFsKORTRNYDJQfNTjQyGLR9ZNIxEzJSqoh52oM1oaRS4j5q2hqfvxYIUfmsc9K1iW3LctYHUv63s_KK5JDGVPfz9ndOMtELL5n_-DuQwFDJCwDotbX8QxlXYDDJFnq4XSZiNTCr3__CBGq5xaYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت پس از حمله حوثی های یمن به دو تانکر نفتی عربستان سعودی، از 98 دلار به ازای هر بشکه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136928" target="_blank">📅 13:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b94d872.mp4?token=dgJdCr9r6lJlGbOQZEaCGcT11lTuxyVWoAe2zuP0Lqv4QHouDee1tjOAbXv6K3mr7IghLg8gXfR-GSmu9SRGmR3K7VhvN4Ux9jHppI3IK5MYFfd4tlePR7KnjgsR7evbgHpU0e9YwHV7VANl0nT22shM1jHzH7wRjuEq-BiX-gbxiy_FeyKEcTNSiNeeOnKZfaV4WuzGYeKEs-SRvJ1xucuzV5qA0ikJKZB71l5kNiro51DXsVIxGBIEtv8qa7-XlIG5qa07wNPe9IgUS3nSoN3KVV9Tai-nB03V1f6AG2GFc-avpR6d6_Rr4UQiBtj1zqPCCTvcrhe9hlBHpd8k3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b94d872.mp4?token=dgJdCr9r6lJlGbOQZEaCGcT11lTuxyVWoAe2zuP0Lqv4QHouDee1tjOAbXv6K3mr7IghLg8gXfR-GSmu9SRGmR3K7VhvN4Ux9jHppI3IK5MYFfd4tlePR7KnjgsR7evbgHpU0e9YwHV7VANl0nT22shM1jHzH7wRjuEq-BiX-gbxiy_FeyKEcTNSiNeeOnKZfaV4WuzGYeKEs-SRvJ1xucuzV5qA0ikJKZB71l5kNiro51DXsVIxGBIEtv8qa7-XlIG5qa07wNPe9IgUS3nSoN3KVV9Tai-nB03V1f6AG2GFc-avpR6d6_Rr4UQiBtj1zqPCCTvcrhe9hlBHpd8k3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال پزشکیان از نخست‌وزیر عراق در کاخ سعدآباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136927" target="_blank">📅 13:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=P3LLR3c91LZ4tFjcqaINEfD-qhJMyubk3QhyxWOHWM6IKgOoI7ZKHYxZS-5uXjCPvK7tzgvHgErFWVCdElWFoavSn2TJhaNHPxcvi1OD9RdzTBxk8NDZRnfYHuSc4_OJnwaarm7Df7hVp05kobSxweszxcNNB0nB7ZAjB52S9xeT5Dc7E6bEhTBvP2F7f8bEKIwvIY49dyEFhR_5majASGcuYbPwtPHe2xxi4VPfhUaK6JYXUDK3g_2RtpIVtTjcSswFecKfebQEsE8P8OAs8G66ClvndVFWdlhZkTGwSPSRmJZarArRwsGPLH5aEb0VH4yKMI2ozyEikqkNlA8JeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=P3LLR3c91LZ4tFjcqaINEfD-qhJMyubk3QhyxWOHWM6IKgOoI7ZKHYxZS-5uXjCPvK7tzgvHgErFWVCdElWFoavSn2TJhaNHPxcvi1OD9RdzTBxk8NDZRnfYHuSc4_OJnwaarm7Df7hVp05kobSxweszxcNNB0nB7ZAjB52S9xeT5Dc7E6bEhTBvP2F7f8bEKIwvIY49dyEFhR_5majASGcuYbPwtPHe2xxi4VPfhUaK6JYXUDK3g_2RtpIVtTjcSswFecKfebQEsE8P8OAs8G66ClvndVFWdlhZkTGwSPSRmJZarArRwsGPLH5aEb0VH4yKMI2ozyEikqkNlA8JeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبوسی
ِ
پزشکیان با نخست‌وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/136926" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: در گفت‌وگوی تلفنی با بن سلمان، توافق کردیم که به همکاری برای حفظ تجارت دریایی از طریق دریای سرخ و تنگه هرمز ادامه دهیم
🔴
حملات یمن به تانکرهای نفتی سعودی در دریای سرخ را محکوم کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/136925" target="_blank">📅 13:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb7b3edf8.mp4?token=RY5h2fWVZ-qFkDlNp2cTdxqx0CB4ijt_ixq5kwgIhU5hYvTSBzNMOPguTYpirmALWbLdQGDo1EE_TdPWMi-EmvbNEo8l174l9bUpT1GVee_HHMEfsukocx4Huw8Y3gwiXZIDNzUjIAjwo5pidIcMgC6Atw_9-wsvOtZWpPgUEVelxY2tfuvyiyi7LVVCAztzvAvgHWVycqKu9Dtvs9EVKDxHFsh1wUzH96a3qYhduyKVm0elv9pUFQwkAG-BtepuSaJ6Asa2ocjTUiYkWhlk61hnSm0BQVfpX1K1j_ArjgZDtG291CCcy5SPhNAuNxGc94OMrpnFkeeC3S2eP6ekSEDZSfztfmWs3e_SDO5elYyN2ajiYVv0MMetXjJG6C8ZZptqkQI0NY43P7DQwmEpfBun9khIBkt7uuKJTrOCiBOmh_E1v-DTzPPXcTmRvQ9pcSF_dkFhhUMQP-xLxYXOnp2Iivvx3TLnwOvpnEMxD1wyKXWJ73_puJ1N25hGWPcP11AJEdb4xRMO2gd4IxWgCch169N0VSc7MmrO0c1NSSlbfLzyLJ685l4usj91yZ-QME3_Zi9Ev1MN7lG1t7OjTNMT0VWLj647tPdXPsrQSm9Twc2cV13rAYCOt0lVLqq2GwOWEAaoaJ6GVDCeCtRFY0xg46ipOQJ38A5OSUVZq9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb7b3edf8.mp4?token=RY5h2fWVZ-qFkDlNp2cTdxqx0CB4ijt_ixq5kwgIhU5hYvTSBzNMOPguTYpirmALWbLdQGDo1EE_TdPWMi-EmvbNEo8l174l9bUpT1GVee_HHMEfsukocx4Huw8Y3gwiXZIDNzUjIAjwo5pidIcMgC6Atw_9-wsvOtZWpPgUEVelxY2tfuvyiyi7LVVCAztzvAvgHWVycqKu9Dtvs9EVKDxHFsh1wUzH96a3qYhduyKVm0elv9pUFQwkAG-BtepuSaJ6Asa2ocjTUiYkWhlk61hnSm0BQVfpX1K1j_ArjgZDtG291CCcy5SPhNAuNxGc94OMrpnFkeeC3S2eP6ekSEDZSfztfmWs3e_SDO5elYyN2ajiYVv0MMetXjJG6C8ZZptqkQI0NY43P7DQwmEpfBun9khIBkt7uuKJTrOCiBOmh_E1v-DTzPPXcTmRvQ9pcSF_dkFhhUMQP-xLxYXOnp2Iivvx3TLnwOvpnEMxD1wyKXWJ73_puJ1N25hGWPcP11AJEdb4xRMO2gd4IxWgCch169N0VSc7MmrO0c1NSSlbfLzyLJ685l4usj91yZ-QME3_Zi9Ev1MN7lG1t7OjTNMT0VWLj647tPdXPsrQSm9Twc2cV13rAYCOt0lVLqq2GwOWEAaoaJ6GVDCeCtRFY0xg46ipOQJ38A5OSUVZq9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا:من قبلا پیش بینیمو در مورد سال ۱۴۰۵ گفتم.
بهار پر رعدوبرق داریم(حملات نظامی).
تابستان بسیار گرم داریم(کمبود انرژی در اثر حمله به زیرساخت ها).
پاییز بسیار برگ ریزان از داخل(تـرور رهبران افراد بلندپایه حکومت و فروپاشی).
زمستانی که بذر سال های ۱۴۰۶ و ۱۴۰۷ رو روش میکارن(ورود افراد جدید و مد نظر خود آمریکا به سیستم حکومت).
این جنگ از ۱۴۰۰ تا ۱۴۰۴ مقدماتش فراهم‌ شد؛ از ۱۴۰۴ تا ۱۴۰۷ وارد پیک میشیم و از ۱۴۰۷ تا ۱۴۱۰ پیامدهاش نشون داده میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136924" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ارتش اردن : در ۲۴ ساعت گذشته، چهار موشک و شش پهپاد ایرانی را رهگیری کردیم
🔴
هیچ تلفات انسانی یا خسارت مادی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/136923" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9xK55s9Wnu-42R5j8WerSWWyHwUelUbH0YFNr-7XQUZDLLOqKAEY0G3K-98b4hB-nL40g9SNALye03iyj-cpSrKJY3MglA7ZX3jM0Rt7RLME8z_VBVJbkdbo_WZfp8VnNP2UQh5Sx6l-HotDvosmAR_tDVmy8E8s199Y0ZexW3TUv80VTI2BDI9tvtsvzEdcfARasJVTx2yaqWyFFBUGlYoPIqJ7sP-zhBW99FTxCp2Ne3lwSGbfrdC1vMpY6QDE8UiKh2FUW11wS51mV-jaUvLao6M_B3YkSAFdWOxI7QzGKOyyqH6hqKAuSmM1h6bbNUyW0yPtoQCFwbgVpXNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضاییه: احضاریه پرونده قصاص ترامپ برای کاخ سفید ارسال شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/136922" target="_blank">📅 13:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f08eb177.mp4?token=eG3roGpI5PmipIGl867FTkE_l54kAiAu-zRsFvyyclPWXcbOr-jfrGDMbW1Se53QY91j6lH-oH50UmGMGW-vWS-v6VMrVE2RGiHKJOTECzynL-i1xYDT4r3_l34uBUqCU_v9JIFmaTlUeAK4_zi_uTyvNjT1wJgaSv_pi5zPGZVNTcbS747ISmHPaJSC564WDvpkrAtj8PfSWe7AkQwQVYA7EyqHi2HKE-vs-dApWkabA40NRRy07zec0jQ7eh5I0s3F8meNrLRYR69ks7WbIAz7C2nY9zQJlf20lwcV32usW7VRhpq0BVASPKIRIfimt5PFFaaBDY7HNQOV4RXdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f08eb177.mp4?token=eG3roGpI5PmipIGl867FTkE_l54kAiAu-zRsFvyyclPWXcbOr-jfrGDMbW1Se53QY91j6lH-oH50UmGMGW-vWS-v6VMrVE2RGiHKJOTECzynL-i1xYDT4r3_l34uBUqCU_v9JIFmaTlUeAK4_zi_uTyvNjT1wJgaSv_pi5zPGZVNTcbS747ISmHPaJSC564WDvpkrAtj8PfSWe7AkQwQVYA7EyqHi2HKE-vs-dApWkabA40NRRy07zec0jQ7eh5I0s3F8meNrLRYR69ks7WbIAz7C2nY9zQJlf20lwcV32usW7VRhpq0BVASPKIRIfimt5PFFaaBDY7HNQOV4RXdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری نشان می‌دهد که یک موشک بالستیک ایرانی صبح دیروز به پایگاه هوایی فیصل در اردن اصابت کرد.
🔴
پس از این اصابت، انفجارهای ثانویه نیز مشاهده می‌شود. همچنین، مسیرهای چندین موشک رهگیر قابل مشاهده است، که نشان می‌دهد همگی آن‌ها ناکام بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136921" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f640ff2a.mp4?token=R63xWG5BUG9rCu0el8j-ZEnL4tQ6mQNhyj_WiH-FTAzI-Gvc0T8tdXYel6bBPd04vF_-C61KrnQnLlc0XK7CM0SEQjXrEGP7ptk5_Rl1Ovx6NOcmNLQ0PPz7WadQRRyfqdcrDNnc7KR3EbOXstDM3PocINmuclI5almwZjwmkNVIBqY3q6-kEf_by5V1JqY5E-LxthuE2APUHxcBa7igleqZVoG0ApAIFWMZxT7qpBaoYQFLo841lM2eJPEW862Uw62hXZy2k1ARdvtGXQexyWUeeXSYh0xjYgotv4K16oMzaR1w0yHCiIfa3d9B7hdGgv6zslPgDo4uktOk3fab6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f640ff2a.mp4?token=R63xWG5BUG9rCu0el8j-ZEnL4tQ6mQNhyj_WiH-FTAzI-Gvc0T8tdXYel6bBPd04vF_-C61KrnQnLlc0XK7CM0SEQjXrEGP7ptk5_Rl1Ovx6NOcmNLQ0PPz7WadQRRyfqdcrDNnc7KR3EbOXstDM3PocINmuclI5almwZjwmkNVIBqY3q6-kEf_by5V1JqY5E-LxthuE2APUHxcBa7igleqZVoG0ApAIFWMZxT7qpBaoYQFLo841lM2eJPEW862Uw62hXZy2k1ARdvtGXQexyWUeeXSYh0xjYgotv4K16oMzaR1w0yHCiIfa3d9B7hdGgv6zslPgDo4uktOk3fab6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گوینده جمله تنگه مامان ثابتی: اگه جرات دارید رفراندوم برگزار کنید، هیچکس دیگه با ایران دوست نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/136920" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه عمان و پاکستان پیرامون تحولات اخیر در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/136919" target="_blank">📅 12:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9b370e41.mp4?token=breyaiWFqaEGd0TC6j_Xf0EfE-TvP1rFef0Qccuc5gzcxrZEbCry3Rtp4OmFxNmOpmRpDpGqa-mUWxHXopX36HrBlD6r5MI_rI_hT1pmPtCycyQEBtnmmss22EDNE7LcaCYiHfA3tXX-zuJVBF7ZNOWi_zAXYFmMreaqlvESBt4ORG4zE9QTlllgyypU278r5OTcCms4GPUmq3pr45iqGuh1wVCOf9X2sxd39X6tyCavXAAr31wa8b8rU7aww9Dec4nQrVj5mBQM-DkEjCt4RZ6UIwsaH-8yFUZDUeauSvFQMhmp3rXoBoM7pb8xfDRx0cHyYk0e04Iw4ekfJvBKWZpxwPSWbFftc83VC1pAz-zXd6CeEbTu9uFN5nf5QoJetiAQ5ZwugUGE9zcjC4S3xVvOUKfjavw_3GwZ24pUNJRJCB87XvJ5Gc_zs5VVkR5EmaH0PwhlSITLU3HURrNMd57YQ3OGFWVrOM7bIGQt8BsOLjAd0tCKJSFo2VhE9DU4efQku8Ve_exQOfcVT57nxldxipRA--eJtJ735vb3Nu-W2wJC4xJCRhepdWVJzb2zXna0CAv3eugqIG4nS7d_vrqkEnVFqZUw_EpiXtthdyp6H9P5zh2JoZfCs7isdm_9d4V2d8urnyI3rALrqwpP5B4BET6axhXEk_ccKDAzRmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9b370e41.mp4?token=breyaiWFqaEGd0TC6j_Xf0EfE-TvP1rFef0Qccuc5gzcxrZEbCry3Rtp4OmFxNmOpmRpDpGqa-mUWxHXopX36HrBlD6r5MI_rI_hT1pmPtCycyQEBtnmmss22EDNE7LcaCYiHfA3tXX-zuJVBF7ZNOWi_zAXYFmMreaqlvESBt4ORG4zE9QTlllgyypU278r5OTcCms4GPUmq3pr45iqGuh1wVCOf9X2sxd39X6tyCavXAAr31wa8b8rU7aww9Dec4nQrVj5mBQM-DkEjCt4RZ6UIwsaH-8yFUZDUeauSvFQMhmp3rXoBoM7pb8xfDRx0cHyYk0e04Iw4ekfJvBKWZpxwPSWbFftc83VC1pAz-zXd6CeEbTu9uFN5nf5QoJetiAQ5ZwugUGE9zcjC4S3xVvOUKfjavw_3GwZ24pUNJRJCB87XvJ5Gc_zs5VVkR5EmaH0PwhlSITLU3HURrNMd57YQ3OGFWVrOM7bIGQt8BsOLjAd0tCKJSFo2VhE9DU4efQku8Ve_exQOfcVT57nxldxipRA--eJtJ735vb3Nu-W2wJC4xJCRhepdWVJzb2zXna0CAv3eugqIG4nS7d_vrqkEnVFqZUw_EpiXtthdyp6H9P5zh2JoZfCs7isdm_9d4V2d8urnyI3rALrqwpP5B4BET6axhXEk_ccKDAzRmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخوندی که گفته بود شاشیدم وسط اتحادی که قالیباف درست کرده، خلع لباس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/136918" target="_blank">📅 12:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136917">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
برخی منابع غیررسمی عربی مدعی شده اند که نیروهای آمریکایی و شخصیت‌های مهم دیپلماتیک، ساعتی پیش بدون ارائه هیچ توضیحی، بغداد را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/136917" target="_blank">📅 12:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صدای آژیر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/136916" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09a5113ef.mp4?token=cxKyrgqZEBtURJdSQtY-xkhOaTwZTKYbN6oFLCvpYClPf3JiaRwbRpOlRDjHCGVLUKXBo6H3EOD_gr45mt795P1-R570uBIFkUKsVF1suSDV924tTh-7RRkjqAGdhagHJ3g_ydIb-Gr7zYMVF-kqxgAUTdhrU2306bu7LFB7JeMOcfRjIgYvTFhnOeMkY1ykX7M-pQza2w0xGtDIxSRkLDmCbpaCBRP06dRXVSMDXkw5GoZ5IYcXmY28aNSvhusbjwUn96ppbjmeeWV9-PhioTm_lDMrpEJLtczvxd8Bxc4lXhigpAeHqKJn8l5UA2XjojP6bHHdGDRS8Shh9a7ozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09a5113ef.mp4?token=cxKyrgqZEBtURJdSQtY-xkhOaTwZTKYbN6oFLCvpYClPf3JiaRwbRpOlRDjHCGVLUKXBo6H3EOD_gr45mt795P1-R570uBIFkUKsVF1suSDV924tTh-7RRkjqAGdhagHJ3g_ydIb-Gr7zYMVF-kqxgAUTdhrU2306bu7LFB7JeMOcfRjIgYvTFhnOeMkY1ykX7M-pQza2w0xGtDIxSRkLDmCbpaCBRP06dRXVSMDXkw5GoZ5IYcXmY28aNSvhusbjwUn96ppbjmeeWV9-PhioTm_lDMrpEJLtczvxd8Bxc4lXhigpAeHqKJn8l5UA2XjojP6bHHdGDRS8Shh9a7ozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا ایالات متحده به دنبال تغییر حکومت در ایران است؟
🔴
روبیو: ما به دنبال خلع سلاح هسته‌ای ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/136915" target="_blank">📅 12:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وضعیت کانالای ایتا وقتی آژیر کویت و بحرین فعال میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136914" target="_blank">📅 12:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
صدای آژیر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136913" target="_blank">📅 12:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شهر رامات گان در اسرائیل، که در حومه تل‌آویو واقع شده و دارای جمعیتی حدود ۱۷۲ هزار نفر است، دستور بازگشایی تمام پناهگاه‌های ضد بمب را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/136912" target="_blank">📅 12:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03ba6f662.mp4?token=skQsf7qp1I8Jn2YDVG_0SHJVLScD-MoS3vgPYbaslK74YENfmiC2TLyQ87zKDZvjGZR4Mrf90LI7tMaI5tXGkttQ_YwLByExniC7RH4UVrqvIyuIp9YiDTgRqGgmbobfnYy-f4t3NM2o-fyve64Ufd4dvCTzwmbX2s0y07oYLTeUYUnCfgTTvzKZ_YN_jktX0qTysdsHDV3DAwMPTA3Zx4bKWbtOw4Pfw32YPVrF3mLvrYSKr4TgapTo3W65L1VhgwXYknKFA5fQ_NXDMfnZHou4BiD1c4f31HAM3IyQJLr0D86WuN1-TAqc6VZWIwfu0-xxcg1DVBmwvBp3_H9rvSVBZSyscKpnWfcjjGQR2aXGLcjGGdVTyrXEM-03UV0oMiNhnmV8lqSBHY0Dd_iXYYuXenP5bPzVVzNXO5rW6MQ7KMmmoS_CMgAxV16fASo50jGONNC3_sPeX0ZZyN4Vw2PoTxLbZAZ0VZIjIO8PnqjCbCtBHTPMV_HGHACl-h6dScMbyuPVjf6AomlNayxC032jfT6DVfNPUSYap-mUmN_KMLLOVjHYI94ULhji-kP-3j217eA9T95mOO-T60Fbs0YgvFaLIh7evrAbBd7QICJH7a6Qh9HJCBIzKi29x0DtIBtd86tO8RwpfH-DfPORLxJVjHnh8gFrnEdd9HJkydc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03ba6f662.mp4?token=skQsf7qp1I8Jn2YDVG_0SHJVLScD-MoS3vgPYbaslK74YENfmiC2TLyQ87zKDZvjGZR4Mrf90LI7tMaI5tXGkttQ_YwLByExniC7RH4UVrqvIyuIp9YiDTgRqGgmbobfnYy-f4t3NM2o-fyve64Ufd4dvCTzwmbX2s0y07oYLTeUYUnCfgTTvzKZ_YN_jktX0qTysdsHDV3DAwMPTA3Zx4bKWbtOw4Pfw32YPVrF3mLvrYSKr4TgapTo3W65L1VhgwXYknKFA5fQ_NXDMfnZHou4BiD1c4f31HAM3IyQJLr0D86WuN1-TAqc6VZWIwfu0-xxcg1DVBmwvBp3_H9rvSVBZSyscKpnWfcjjGQR2aXGLcjGGdVTyrXEM-03UV0oMiNhnmV8lqSBHY0Dd_iXYYuXenP5bPzVVzNXO5rW6MQ7KMmmoS_CMgAxV16fASo50jGONNC3_sPeX0ZZyN4Vw2PoTxLbZAZ0VZIjIO8PnqjCbCtBHTPMV_HGHACl-h6dScMbyuPVjf6AomlNayxC032jfT6DVfNPUSYap-mUmN_KMLLOVjHYI94ULhji-kP-3j217eA9T95mOO-T60Fbs0YgvFaLIh7evrAbBd7QICJH7a6Qh9HJCBIzKi29x0DtIBtd86tO8RwpfH-DfPORLxJVjHnh8gFrnEdd9HJkydc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا با وزیر امور خارجه روسیه در مورد این موضوع صحبت کردید که روسیه اطلاعاتی را با ایران به اشتراک می‌گذارد که هدف آن سربازان آمریکایی است؟
🔴
روبیو: چه کسی گفته که اینطور است؟
🔴
خبرنگار: آیا اینطور نیست؟
🔴
روبیو: چه کسی گفته که اینطور است؟
🔴
خبرنگار: گزارش‌هایی در این زمینه منتشر شده است...
🔴
روبیو: گزارش‌هایی در رسانه‌ها؟ اوه، پس حتماً درست است. این در رسانه‌ها است. این یک منبع اطلاعاتی است. من نمی‌خواهم... اجازه بدهید بگویم، بیایید فرض کنیم که این درست باشد. من قطعاً در مطبوعات در مورد آن صحبت نمی‌کنم.
🔴
هیچ کاری که کسی برای کمک به ایران انجام می‌دهد، به هیچ وجه توانایی آن‌ها را برای هدف قرار دادن آمریکایی‌ها افزایش نمی‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136911" target="_blank">📅 12:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران:
آنها هر روز با ما تماس می‌گیرند و از ما تقاضای توافق می‌کنند اما به نظرم برای آن اماده نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/136910" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت خارجه آمریکا برای سومین بار پیام هشدار صادر کرد: تنش در خاورمیانه بالا است، خطر تشدید ناگهانی وجود دارد.شهروندان آمریکایی احتیاط بیشتری داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136909" target="_blank">📅 12:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دقایقی پیش نخست وزیر عراق به تهران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136908" target="_blank">📅 12:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قیمت نفت برنت ساعت به ساعت افزایش می یابد و به 98.5 دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136907" target="_blank">📅 12:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: ترامپ مسئول مذاکرات با ایران است
🔴
تمام تیم‌های مذاکره‌کننده بر اساس دستورات ترامپ عمل می‌کنند.
🔴
مذاکره‌کنندگان آمریکایی با ایران دستورات ترامپ را اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136906" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
دقایقی پیش صدای چند انفجار در کنارک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/136905" target="_blank">📅 11:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر خارجه آمریکا:به نظر می‌رسد ایران برای انعقاد توافق آماده نیست
🔴
واضح است که ایران برای انعقاد توافق آماده نیست، یا حداقل برای انعقاد توافقی که آماده پایبندی به آن باشد، آماده نیست.
🔴
امیدوارم حوثی‌ها حملات خود را متوقف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136904" target="_blank">📅 11:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
انفجار در اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136903" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
روبیو: اگر وضعیت همین گونه ادامه یابد ایران بهای سنگینی خواهد پرداخت، هر شب سنگین‌تر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136902" target="_blank">📅 11:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیروی قدس سپاه اعلام کرد که به چندین هدف نظامی آمریکایی در اردن حمله کرده است، از جمله یک رادار THAAD، یک سیستم پاتریوت، یک رادار C-RAM، انبارهای ذخیره سوخت و مراکز تعمیر و نگهداری هلیکوپتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136901" target="_blank">📅 11:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: بهایی که ایران خواهد پرداخت هر شب افزایش خواهد یافت تا زمانی که به خود بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136900" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اکسیوس: به گفته منابع آگاه، میانجی‌های قطری همچنان با مقام‌های آمریکا، ایران و عمان در حال رایزنی هستند تا به توافقی جدید برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136899" target="_blank">📅 11:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / ایران پیشنهاد آتش‌بس میانجی‌ هارو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136898" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر نیرو:  نیروگاه زمین‌گرمایی مشگین‌شهر اردبیل به ظرفیت پنج مگاوات و با حجم سرمایه‌گذاری ۱۰ میلیون یورو به شبکه برق کشور متصل و وارد چرخه تولید انرژی الکتریکی شد.
🔴
این طرح به عنوان یک پایلوت بر روی مخزنی از انرژی زمین‌گرمایی با ظرفیت تولید حدود ۲۵۰ مگاوات درحال تکمیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136897" target="_blank">📅 11:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTvnISWmcf70spY100EtoGyvOjdk7FfS2OuF2lLktA8ep8kMtfF3bSyM3hZXPdLgGJRwFiJgdKSQMbC3-Cux3Yxcc6jKzBOdUNJp6HSnyi03sM0vFInE6GCI4id_z5XcS4PLertw-ShDk7UYnLx6mrK6icZrOIciosurwSqwOqx8RFoOS7l7Si8Tg2mIBkONqZtqq-t_uWVpTiVBvNXynzEDkQO8vfMlr_i9qYUrm2hSJVLXlNf6DADnckmX8ZyAxwV-ggM-RFilqx1XR1RrcXEMhpQ8Dr2ce_GLFigOY0PxiL2ujSvd09NZGBTp-Vo2kUlWmQGXW-R3G0q2vFNMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۷.۶۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136896" target="_blank">📅 11:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
صدای انفجار از قطر و اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136895" target="_blank">📅 11:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd04aa4c7.mp4?token=rEWZvy-ZgDNCeBuWpOxQx6hDO948fm9SDUiwpCxlzOVUFsSstUMwZG0XOW-0j_fevVtIQIKILeY9e4xQfCILeT_vyljd4TBT8iobulH5Ro669Jtl91KXW1dYqQylagXSXWzmkEBwIBYpr5ijADfAmZ2j2PgPM2JoanL_RnzwN_AgVsrVYmSxTmzvEdqjyIVnPGWfyHh4fn7IIxP_GjSBmEzC7UMuAhFJX3rJdtdkJtsKqqtZ8SN_oUohDQQcUV4dElP9p0Li9og61AvODDc5VVKw0ArpKkH6j0oplV4NV8bf8NV3FXpFyfa0YY5ihXScSSNz9sCtmxRbd0ZfISGmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری های نیروهای حوثی و نیروهای یمنی تحت حمایت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136894" target="_blank">📅 11:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اتحادیه اروپا با صدور یک معافیت یک‌ساله و قابل تمدید، انتقال گاز طبیعی مایع (LNG) روسیه به کشورهای ثالث را مجاز اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136893" target="_blank">📅 11:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ1FdY-TNAEb1UnGDDXmFKDeMJwbF7C-gclGDiC50GkdJVEZKqnWeYNPGp_yYQSvLy4kpJKCzFz__adc-SrV3TAxyp5aTTUDELp2sF08tuL_bLI8orppgQzxM2RubXHmM3UIR7g1vFmZ4-4PMhfvtnz4cnCo2l6hMci5zInf9f8iEfsHc31TWEdIVGpT2jS0dquViG2fyV5_fOhZGGX-Rw_aDxXC5281iyffa1cFP--doZcJMlnByzS3WTqufsf88Zt7iz3D9vPWQ4AsfWHR_Tr5PEZnPpqZbY0kNutC-sDdTM-vnGQ40BaOWcGqkgl6yqrwl6z0k5qoXTDLri1qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر عراق عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136892" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7bWGTAp73_v0T_vAswypfaDVYo1upVjK28lnroE0oWhw-_RLKvJcU4uNLKLpW5HBdHj9dbwSX2BD7749nrwtf2GeKZ0UibkzA7HDcVXRbr3FcUMQ4tjjTqVuaY05_gzk101JIJz0o_4eVF9FQCDKPNP8IOAFtJHV53i5rYIv7C_u6y4XDTrfS_2xk3JFbFRstjabM2CgqQkEkzpcRcGmyXOwG5fInI1spwzfCoUGzf5dKr2oIkOSx8t5jecZekyG4vJuMaklOr5rojspq3BWXgbWIzxIG_uqEsv_yTjP4n8AdOwL24psvsF3mYpad040B52j_SRdKD0zOFqfB9bIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
دو شلیک موشک از آسمان خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136891" target="_blank">📅 11:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
تهدید هر کشتی که پرچم پاکستان را حمل کند، تهدیدی برای امنیت ملی ماست و حق پاسخگویی (واکنش) را برای خود محفوظ می‌داریم.
🔴
ما بر ضرورت کاهش تنش و پایبندی به مفاد تفاهم‌نامهٔ اسلام‌آباد تأکید می‌کنیم.
🔴
پاکستان از تلاش‌ها برای کشاندن عربستان سعودی به درگیری در خاورمیانه ابراز نگرانی می‌کند.
🔴
ما بر حمایت خود از امنیت، حاکمیت و تمامیت ارضی عربستان سعودی تأکید می‌ورزیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136890" target="_blank">📅 10:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شمار قربانیان زلزله‌های ویرانگر در ونزوئلا به ۵۳۹۸ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136889" target="_blank">📅 10:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌گید تنگه رو باز کنیم، مفت بدیم بره.
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
🔴
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136888" target="_blank">📅 10:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLGi39UoKBlHGLmc9Q5rXC96Sx7BAi1QEFqj9FhI4WsCnfdYYENUs2hg8hh4FlILK31hK4UKIP9dGtgJgJcsyV-3vwKhJ5Br-xrO8yWPUE7tLd55BJKRvZx5iNWYTIL5YDY1_5O9nmSIvQ6V4KA2w3tqCImQNgW2QjornMwlvXSW1lJC1fy_LOjBuo47hig59dey1Voob_WYKDwdwWmzh6vU5TIk344lS-V4StLnoUme-p6xRXNKfgFCcVKqvWPem_DvFv5u-GuOxwbXDgq_PyvX4KjV4_Pki-yQk6dcndVAOLQvOK_4fibrB8zcLqz_gF4-mLbVvIE8lbkCACQtbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش از حمله موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136887" target="_blank">📅 10:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApAIbvCFCXkNp8ZSwCT62Z8AwYHShRuAl-_8PWdEh-xAkgS1zdBkl7s0Ur_bAqkN-u0TvYgmM4e8Z_hf0hiFz0YDZGacOjF0WDrgAbUJbeIB0KgXFQpFpjgCI-UbpG9FhyhsSEFg3rTbyj45ejWSF1u4GXa-_rjAdxo4VfCKSm5HcnDfQ2avMpT1YYsCJ68R8Miv1X0esxqiEbwWJJgP4v59Fx6_j7UFKK3ErqdmXOaBYghzUlUFQcgXPTVXAEVei56J_aMvoXYjYHQoJuenuMDRkGP_7o8Ny5_vbBh3g-MgZdvGGQqwv5Ud1-AHE4oOzwyu0RVba5fwIxRU3e0wXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متأسفانه امروز صبح خواهران دوقلو
رومینا رحیمی و  ترانه رحیمی از معترضان دی ماه اعدام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136886" target="_blank">📅 10:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رسانه رسمی عربستان تأیید کرد که یک نفتکش این کشور در دریای سرخ هدف حمله قرار گرفته و دچار آتش سوزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136885" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=chamZj4AlwwTZzejuEUfjMSVBhFwlkVMePND8c51K_wdTjdADXQBeD4ahBhsqaztAa2Ghuy_d1C2P7xkR9F79_2vvkkJMXD2sMSJL7JgoBCm3g7x5NT-zwHJ1mEWJM3Fr34rjtzTwmrwXbpeB-CPXS0RAmhIZPcbTC-iIC04XUhhA2Dgg4BpONhHBP-e2Rna-x2Eb7E26CMT1qZ4ISOY_nroH1T0CWbMXUOCP4ZkqpM4QdPctGZKDEO1gRwh3UImpeuVyxvy8rdCo9JPnLHUynoNhmRbUn4Zd7P380YdqxvXr05wp7EpyH-TCvrF3h7jxmgXOUECGldt6clmy-1SIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af710f15dc.mp4?token=chamZj4AlwwTZzejuEUfjMSVBhFwlkVMePND8c51K_wdTjdADXQBeD4ahBhsqaztAa2Ghuy_d1C2P7xkR9F79_2vvkkJMXD2sMSJL7JgoBCm3g7x5NT-zwHJ1mEWJM3Fr34rjtzTwmrwXbpeB-CPXS0RAmhIZPcbTC-iIC04XUhhA2Dgg4BpONhHBP-e2Rna-x2Eb7E26CMT1qZ4ISOY_nroH1T0CWbMXUOCP4ZkqpM4QdPctGZKDEO1gRwh3UImpeuVyxvy8rdCo9JPnLHUynoNhmRbUn4Zd7P380YdqxvXr05wp7EpyH-TCvrF3h7jxmgXOUECGldt6clmy-1SIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز هوای شمال غرب و جنوب شرق کشور با رگبار رعد و برق همراه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136884" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
براساس حکم قاضی آمریکایی محاکمه نیکلاس مادورو، رئیس‌جمهور ونزوئلا، و همسرش سیلیا فلورس از اول ژوئن ۲۰۲۷ آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136883" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=FwBtXcxpwqFWbjEwQbxe_fxLg-TCMpIj-ea6_R8oYzhHOYjNytBZWbmtCA4RotaRuUC8kfOlITtK1L49awUfGvCLrcu0lJMTiNpEComwJDvDwo1p2CNhPZhP6zfiiA1hllp_ERLHWizOt_ftJYpD8a9vg8qnd9ogJbYL9ht_UQh80d7a4XmWpDDu8TEUA1xFoPiIt22Vp2gRdSJZy_yEDNA22cThK6MsDM6tNugBFsRscyFNiZwyipNU8tabYZ8umMfT5fkbUrmZUFy8R2ZBm-qkjv_ZUFrmUx-X7TyNegj0HB0JdzzeFGjKm49PljN9wVGvYeNmt5FGY2kBG0QEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8a27cdc2.mp4?token=FwBtXcxpwqFWbjEwQbxe_fxLg-TCMpIj-ea6_R8oYzhHOYjNytBZWbmtCA4RotaRuUC8kfOlITtK1L49awUfGvCLrcu0lJMTiNpEComwJDvDwo1p2CNhPZhP6zfiiA1hllp_ERLHWizOt_ftJYpD8a9vg8qnd9ogJbYL9ht_UQh80d7a4XmWpDDu8TEUA1xFoPiIt22Vp2gRdSJZy_yEDNA22cThK6MsDM6tNugBFsRscyFNiZwyipNU8tabYZ8umMfT5fkbUrmZUFy8R2ZBm-qkjv_ZUFrmUx-X7TyNegj0HB0JdzzeFGjKm49PljN9wVGvYeNmt5FGY2kBG0QEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک‌ مرد که پشت سر ترامپ بود، در یک گردهمایی در جورجیا خود را به جای رئیس جمهور آمریکا جا زد و توجه همه را به خود جلب کرد
🔴
او به طور کامل حرکات، سر و صورت رئیس جمهور فعلی کاخ سفید را تقلید کرد و عبارات او را تکرار کرد.
🔴
این ویدئو به سرعت در رسانه‌های اجتماعی و رسانه‌ها پخش شد. برخی این تقلید مسخره‌آمیز را سرگرم‌کننده دانستند، برخی دیگر آن را تمسخر دانستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136882" target="_blank">📅 10:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=jTs39uwX0w9bNeBEXW-li5kS_vz_WXFDXAXbE8khx3UlBM9e2YUah9fXYa-JSbXn1fzKtlidjJioY7DsHMZgh2ds1BvV_pfZfpli8FM7yVmQWu0p626xJlgtoT08IFsOd7msOSdV-y_Rv7VQUa3KY4WBOoVs90CriibjTtLPq4yfWXeYqp5jwb5J_BapYWXnXimb8TBSlQFJ2Tzur-UNOgL9Mli7p3xiJ2Sk9oLPu2kSr0xlIWWfRv3GfnZBoEGrUxVRBx5t83jCSwIuM7N0e6P46Qis6LcDfCzF2ByUH9vNAYWaptSFpvj0sUuhTFAjzFwycUZKmBz3HLL26rEHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e26a43d45.mp4?token=jTs39uwX0w9bNeBEXW-li5kS_vz_WXFDXAXbE8khx3UlBM9e2YUah9fXYa-JSbXn1fzKtlidjJioY7DsHMZgh2ds1BvV_pfZfpli8FM7yVmQWu0p626xJlgtoT08IFsOd7msOSdV-y_Rv7VQUa3KY4WBOoVs90CriibjTtLPq4yfWXeYqp5jwb5J_BapYWXnXimb8TBSlQFJ2Tzur-UNOgL9Mli7p3xiJ2Sk9oLPu2kSr0xlIWWfRv3GfnZBoEGrUxVRBx5t83jCSwIuM7N0e6P46Qis6LcDfCzF2ByUH9vNAYWaptSFpvj0sUuhTFAjzFwycUZKmBz3HLL26rEHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی همچنان در پایگاه علی‌السالم در کویت ادامه دارد، پس از حمله ایران. می‌توان دود ناشی از این آتش‌سوزی را از فاصله دور مشاهده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136881" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRqTu7c-gI-CL3VVOsGCpEpCskKM7aL53ieBTJ3JTvQSL3Dr8PJZEaUNZt0yWLEweJGkRuxRbjBneQ2hnPrqDdJVsM4aWkOahltpi1ExujGc_7Fl1VqmVesrG7aZ-FGiCLqGx9PyTPp0N2kn8mwFLJni8mO8hvJTOFj78z2phZ4DWCdP6S0_2Di78RsZzb-jkjvJ3jGmOepI3xdfqy44gg7l9CFUiSDobnPRR5I1wEy5iopZW7NZWj3Z492GW5jSRa9Cv2V4t-gQjObNW74IswQZqmgpaEa-9s-bHcpGwZTowkO4yCPlX-ea0MM1TfCXg6m6oBGzxjcTveSP8-dvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری رسول خادم برای عادل فردوسی‌پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136880" target="_blank">📅 09:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه آی۲۴نیوز: نتانیاهو همچنان منتظر تأیید کاخ سفید برای دیدار با ترامپ است؛ سفر او به واشنگتن در صورت تشدید تنش با ایران ممکن است لغو شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136879" target="_blank">📅 09:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=d643dVFz72NTPOgmTkAYP2osZXm9TIRcHF2RsHoZ-FuMQFSE5iuE3OioKnf9Tc4nvPdPHugu1J5wXIyFIcvALFCdQx2dkYyEoIq_QXezWyO5Vz9b5jjKjIM535XbW506pLbtACcVcZSvxovsS05UN2DMVWcFxjEW6MsO5lkGPHY7HXvXm_b5jnz_qn8KTmwHK1ghmBl0xSGVjyF2WSRh5yxl4Ek-rt271XtbdeZBjYqIRq32P9_QEOO679Rkj0rwhi5mhPyr-s1H92NeWUZmO3qg6kqLTWSyWP9LLZdK_KaPrJwF2PE7V57o3_y5EMvYyyqsywh_i7nsLl1E8zMbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f280731e5e.mp4?token=d643dVFz72NTPOgmTkAYP2osZXm9TIRcHF2RsHoZ-FuMQFSE5iuE3OioKnf9Tc4nvPdPHugu1J5wXIyFIcvALFCdQx2dkYyEoIq_QXezWyO5Vz9b5jjKjIM535XbW506pLbtACcVcZSvxovsS05UN2DMVWcFxjEW6MsO5lkGPHY7HXvXm_b5jnz_qn8KTmwHK1ghmBl0xSGVjyF2WSRh5yxl4Ek-rt271XtbdeZBjYqIRq32P9_QEOO679Rkj0rwhi5mhPyr-s1H92NeWUZmO3qg6kqLTWSyWP9LLZdK_KaPrJwF2PE7V57o3_y5EMvYyyqsywh_i7nsLl1E8zMbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اخراج خبرنگاران از اتاق دیدار روبیو و لاوروف وقتی سوالات حساسی می‌پرسند
🔴
خبرنگاری از مارکو روبیو می‌پرسد که آیا از وزیر امور خارجه لاوروف در مورد کمک روسیه به ایران برای هدف قرار دادن نیروهای آمریکایی سوال خواهد کرد یا خیر.
🔴
خبرنگار دیگری از لاوروف می‌پرسد که روسیه چه زمانی حمله به اوکراین را متوقف خواهد کرد. سپس یکی از کارکنان، خبرنگاران را از اتاق خارج می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136878" target="_blank">📅 09:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=pMebASnqNdCVr6DBXrG6n9syeMzcv5n6htH4uobWTqvcxkIGpkOeTQg5C5HkJcojm6WAaYrA5S279Lb33iM7KBJOarwUiDH4wsfhOUNjJV3JaJN4kXuYw-HwJS9TWOdqOPelgP1nyDeFlr0CmeuPBb1H3J90mjQxFjjGd9QoW4PcUTYFJ7guuDnT1zPPLad4-N0TJHzSO97_5Y4Qe0aJuiZRU3EXLB3HJ0RV0g72kC6MiIe_klmHEs3lHSIJXXsbimBNcuzgOUW9slJW-QQL4pmmi6V-S7pZpRVgjh8mC9SMr93ZkT7TZV-NggqNOnexQ8vBqZpXsGwocETgFbLq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d28883e8.mp4?token=pMebASnqNdCVr6DBXrG6n9syeMzcv5n6htH4uobWTqvcxkIGpkOeTQg5C5HkJcojm6WAaYrA5S279Lb33iM7KBJOarwUiDH4wsfhOUNjJV3JaJN4kXuYw-HwJS9TWOdqOPelgP1nyDeFlr0CmeuPBb1H3J90mjQxFjjGd9QoW4PcUTYFJ7guuDnT1zPPLad4-N0TJHzSO97_5Y4Qe0aJuiZRU3EXLB3HJ0RV0g72kC6MiIe_klmHEs3lHSIJXXsbimBNcuzgOUW9slJW-QQL4pmmi6V-S7pZpRVgjh8mC9SMr93ZkT7TZV-NggqNOnexQ8vBqZpXsGwocETgFbLq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلمچه دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136877" target="_blank">📅 09:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عربستان سعودی در پیامی به یمن اعلام کرده است که انهدام یک کشتی را بدون پاسخ نخواهد گذاشت. این هشدار در شرایطی مطرح می‌شود که تنش‌ها در دریای سرخ و آب‌های منطقه همچنان رو به افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136876" target="_blank">📅 09:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=tOJgtUf8vNsQEEkfHdllaPEEOR1iP68Jbl4N6Q2rvjbwwcoIHlmb-k2OXiRYUT8bQ-uag5NVVwo2QPZ1Ai96VK_LZMSFmAKmaRHLpQk7JyUwsveQT3zT16Zp4vS1GXTnJrx3bTOmGOt3escySpQFnmO1sSaNJ3s8pRrrbvsdN9bkcInYzRRSPJWizUTi-EzXMBSgttpBj1gE4ykmIeER8RC08QmNzxSfU7oekru8mYJtFG9UKReP12bJRLnB5DcVnhsGJsUxQOY8Sx3LBpAiLp-2mLIT_eMmdDxlL17sSHdRr1TtQRDv4dpAmM4mX9vF4tX3wd-ud_NdL6oX9Wniaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=tOJgtUf8vNsQEEkfHdllaPEEOR1iP68Jbl4N6Q2rvjbwwcoIHlmb-k2OXiRYUT8bQ-uag5NVVwo2QPZ1Ai96VK_LZMSFmAKmaRHLpQk7JyUwsveQT3zT16Zp4vS1GXTnJrx3bTOmGOt3escySpQFnmO1sSaNJ3s8pRrrbvsdN9bkcInYzRRSPJWizUTi-EzXMBSgttpBj1gE4ykmIeER8RC08QmNzxSfU7oekru8mYJtFG9UKReP12bJRLnB5DcVnhsGJsUxQOY8Sx3LBpAiLp-2mLIT_eMmdDxlL17sSHdRr1TtQRDv4dpAmM4mX9vF4tX3wd-ud_NdL6oX9Wniaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری نماینده بجنورد به ثابتی: تنگه هرمز مال ننت بوده؟ مال عمه‌ات بوده؟ ارث باباته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136875" target="_blank">📅 09:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
به گزارش وال استریت ژورنال:
اعزام گسترده تجهیزات و نیرو: آمریکا در حال ارسال نیروهای ویژه، کادر درمانی، تسلیحات و هواپیماهای سوخت‌رسان به خاورمیانه است تا گزینه‌های نظامی بیشتری علیه ایران در اختیار ترامپ بگذارد.
🔴
آماده‌باش نیروهای ویژه: پروازهای باری از پایگاه‌های عملیات ویژه انجام شده و این نیروها آماده اجرای مأموریت‌های مختلف از جمله رزمی، جست‌وجو و نجات هستند.
🔴
آماده‌سازی بمب‌افکن‌ها و جنگنده‌ها: بمب‌افکن‌های دوربرد B-1 مستقر در بریتانیا برای عملیات‌های بزرگ آماده می‌شوند و جنگنده‌های F-16 و F-35 نیز به منطقه اعزام شده‌اند.
🔴
میزبانان احتمالی: کشورهای اردن و اسرائیل به عنوان پایگاه‌های احتمالی استقرار این جنگنده‌ها و تجهیزات جدید در نظر گرفته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136874" target="_blank">📅 09:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون استاندار خوزستان: در حمله آمریکا به گذرگاه مرزی شلمچه در استان خوزستان، ۲ نفر کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136873" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=KOgxqxoNjtHN0cEiWt8CqqqTPNa30J0UHtfkW4w3HBtT68j26qcsRhmHiMckCFyeJAN5gEtWyljQc4PkuwQUWUWz3IoBMsL7b1XNQ3oAmAC4-KhfbD8UGu8w2arZog2PlJtVTR4i1p72aNDTcq7OtPQeF3D85dtQEPfJGaMfqv97f67Vh3vUlX5OVDj1KpfTHJ95B7z0yConXEnF6s_q9Mf9lzD8Ztzn3iVUDtoOvZNitQxI3Go52rr9WjXFBJAHADHYQPB6lhIrx8v8wQVNC-pn8rUjX0Qmu1lEAyL0rBAw3KaDLQMXCmSUF0T_HtM-7oEIzB0Va4-C3TLVAQEJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bda1db65.mp4?token=KOgxqxoNjtHN0cEiWt8CqqqTPNa30J0UHtfkW4w3HBtT68j26qcsRhmHiMckCFyeJAN5gEtWyljQc4PkuwQUWUWz3IoBMsL7b1XNQ3oAmAC4-KhfbD8UGu8w2arZog2PlJtVTR4i1p72aNDTcq7OtPQeF3D85dtQEPfJGaMfqv97f67Vh3vUlX5OVDj1KpfTHJ95B7z0yConXEnF6s_q9Mf9lzD8Ztzn3iVUDtoOvZNitQxI3Go52rr9WjXFBJAHADHYQPB6lhIrx8v8wQVNC-pn8rUjX0Qmu1lEAyL0rBAw3KaDLQMXCmSUF0T_HtM-7oEIzB0Va4-C3TLVAQEJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: چابهار و کنارک شب آرامی را پشت گذاشتند و زندگی همچنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136872" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlJH59TgYqYYh6t8cDLQlns6rLdvba51YKZyyNtmMxRz5_atGoI2jM5D4aJcYgstfiXr0iiPpD0drdd0DPpPWAmZz-e0LgAJOyW30ukL87qs2sRuenJRCnxxqV7tlmgUPTZShG5k-DNVVMaOyNy35QoMQqCrS1MYzYGeJW-HWFLdZaeCU65e6X6iqyhs4YK12VkDX-EPX4R9fbnl6FTtJ3gBemaL6c1Oic-dwVgbWMHmVVCe7VYLHN2ph_1xAECBt-dv_HptQfOmMzO_UXTdGf8hpKjf-YAVKGW3_t4F30z1jIQzsheZMw7lrujbVpafk3Mop34KN4IUUWntF-BJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخابره کد اضطراری توسط «آواکس» آمریکایی در آسمان عربستان
🔴
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🔴
مخابره کد اضطراری ۷۷۰۰ به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136871" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40882f729.mp4?token=RHM4mhrmn6BHkQJWgwyeDJXg_zidmuqbebWMOIl0-V5ruuezY75sKpIbE1q3cAIPYHnAdcoG3fecIHltgLE3Sed0eJUXiDbsBHHtUwRadEKKhoMrV5PBltdWJtsgP1LKhxp2smWlznvugB8zxVZFOE5SKAIKkdPurbqIIBXbwFEZbqZl9PPhqWKz8GozYJkY84KiiWElDX4cgwMOqE46tBLRorZzLOFFXFBKtr4i3ohrE_t45iLDLYYqPNLPt7VralM_Bsq1kdedsDh0wuiAxKwSTiebPPD15nL2c12_mFbR2QJxHHNuqd19Zr21UADxf3TjWpHIf7Vx5YLQukw2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40882f729.mp4?token=RHM4mhrmn6BHkQJWgwyeDJXg_zidmuqbebWMOIl0-V5ruuezY75sKpIbE1q3cAIPYHnAdcoG3fecIHltgLE3Sed0eJUXiDbsBHHtUwRadEKKhoMrV5PBltdWJtsgP1LKhxp2smWlznvugB8zxVZFOE5SKAIKkdPurbqIIBXbwFEZbqZl9PPhqWKz8GozYJkY84KiiWElDX4cgwMOqE46tBLRorZzLOFFXFBKtr4i3ohrE_t45iLDLYYqPNLPt7VralM_Bsq1kdedsDh0wuiAxKwSTiebPPD15nL2c12_mFbR2QJxHHNuqd19Zr21UADxf3TjWpHIf7Vx5YLQukw2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، و سرگئی لاوروف، وزیر خارجه روسیه، در حاشیه نشست وزیران خارجه اتحادیه کشورهای جنوب شرق آسیا (آسه‌آن) در شهر پاسای در مانیل فیلیپین با یکدیگر دیدار کردند.
🔴
روبیو پیش از این دیدار، با اعلام آنکه واشنگتن به دنبال ایفای نقشی سازنده برای پایان دادن به جنگ است،‌ اعلام کرده بود قرار است درباره جنگ اوکراین با همتای روس خود گفتگو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136870" target="_blank">📅 09:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سپاه: یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ۹ آمریکا در پایگاه هوایی علی السالم را با حمله پهپادی منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136869" target="_blank">📅 09:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLko3UsTn65qHeJ0QeR63qFvROfmc_FVbybEibGvKGPcELgtfV1ZskSjIxa3jHslBUr4IIx6yXZmp8j0yIJoj2mqmRcxGxg-fvWOE2eRgwaxDtkQAsVdldcZEZuLbKipIJE4Mp3-fGtWCF8FsnJeKmSvKCZKXvJAchgfXLCmh1vA_j-WG1bFrWWu7HMEc6pTzuP1iKdZi5UIiegMc5AuZOMruA--YQ7SemznmipHtngFZNMMu-LjE0XjD0IbO-RzaSrCrw4GavC_NgwWBPLi2gQafwLp-aZ1mkWGzZ3W0cqKWCvH1Q-kzFUn6qrMfBEEYjHHIxcs0l7MZH2YCYu9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مسئول آمریکایی:در این ماه، ۱۲ سرباز به شدت مجروح شدند. این جراحات ناشی از حملات موشکی و پهپادی ایران در اردن و کشورهای دیگر بود. به طوری که این سربازان به دلیل شدت جراحات، با هواپیما به یک بیمارستان نظامی آمریکایی در آلمان منتقل شدند تا تحت درمان قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136868" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خبرگزاری فرانسه: بعد از اعلام محاصرۀ عربستان سعودی توسط یمن، ۹ کشتی مسیر عبوری خود از تنگۀ باب‌المندب را تغییر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136867" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شهر هایی که دیشب مورد حملات ارتش ایالات متحده آمریکا قرار گرفته‌اند
🔴
بندرعباس
🔴
بندر جاسک
🔴
سیریک
🔴
بوشهر
🔴
اهواز
🔴
شلمچه
🔴
رامشیر
🔴
بندر ماهشهر
🔴
اندیمشک
🔴
کرمانشاه
🔴
اسلام آباد غرب
🔴
ابهر
🔴
شدت گرفتن حملات به غرب کشور در دومین شب پیاپی
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136866" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwsyDesPDz6uTvq3AB-Z09xV8dtUTCBijM35dfWJcfzPd-_Wk8NxeKs3fv_sctA9z35MpUMS23ERhWaKHA0A6Mk1XEr5D3kgfm3sh-2z_ohdf89q93Cxxlo6qCzSesZkhme85tEFtbu1GWOnArEI1yGBrFdolWOqqVqKOQzdzGDk8K-YvN7hcxYLfjkECs_hUxcga716erIT2H7zOyrZzI4X92dlAcFEnGuAZ0HLaWvhDn33intfKAYRVvlCKqdo78ofUKN0Fl5p7jbQqvFqz8Fnbvot2-yMbpxmlfWWjGgxGu_H6KMvIFNPLloHm1rsY9ZMT-01CxPlDiPeotnzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۹۶ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136865" target="_blank">📅 08:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سپاه به مردم کویت: آمریکا تمامیت ارضی شما را هتک کرده، نه ما
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136864" target="_blank">📅 08:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjHj_Vsm-B2wkv-ZGYz7FPi-aNkOnPwvyx4GSJAv_aQjQu_-LFyQUVukRLmOMnUXPga6-s3BgSbZHXfU-GyJ-f-75vAsi0tbxZ2RYSIy5yn6n9oXU7TZvnmQlPWbvC1JDr2u5IuuIlNv-jMP3QmX57y9h6z8pI7G-Oufsar7QuKBQvfq6SPYCS1dq747e-vrcO-HLSWqYMgufsM3hzGn39e0S55eh2nahHP3QuoadIf4-KYoOYH-SsCuuOhSzEaRcpUhurmjCPgHHcBRKix2v4go9tPd9uec7ttrnWqR13WgwbIv2wMvfoBgAqvSQyFdomwfmPBeNPqiWaZr5rjn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس، با استناد به مقامات آمریکایی، گزارش داد که یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/136863" target="_blank">📅 08:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
منصور حقیقت پور، فرمانده پیشین سپاه:
اگر آمریکا خارک را بگیرد روزی ۱۰۰۰ موشک رویشان می‌ریزیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/136862" target="_blank">📅 08:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfBqYg_Zmv6KB8XG515XP3Yb5MvVH7Iyy768h91cU2MsL2nN8a5zSnoo8HQqzQQjppJEg1RFeA9Nxlwtf7RodskSrbtEkPnH3DlMkzmD0ZsznsYjlTjmVzXRxDaHAApk6Aus1ZnAPbs1N1l50yr3RiwsEAol0_TfL6A5FoDx-C-BQmIdcJAChiSiLw1a2O07n5RpvNumTbSe6d_PFhNXOpXtrJlquXi3wLUZpMvEKRYlQe4AInxXvpbtCGW4G7nSyJGeMallMgifwl8C-pa6XZgYCHk_OpHm_s1P_jhVfsQPBgmQXXkgpbPDpyHYl7WZgbs-2JoZEg3a6gjbMHeLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از کتاب «قدرت مذاکره» دکتر عراقچی، کتاب «دیپلماسی ایرانی» نوشته دکتر ظریف رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/136861" target="_blank">📅 07:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سپاه:
حملات دشمن رو با قدرت بیشتر پاسخ میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/136860" target="_blank">📅 06:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959a8c1fa6.mp4?token=rj5DM17DSLm11EDTUfm0wJv5bQSSRwCLrUYlXMNDBP5gNWMjZgv4wv3dlJ3972lwcdZ6SJHt5LsS-TL4IX5nPjzAwK9eKJUXX3Hr5KyrNGN1WyU3qdqsWiXctrXVBy65HI8PCNnB_YXOuS95XOHd71drGzJj6b33D26ysIbycZtHofIoQbE5OgXls2SO7_72GaOKC2lKafLkbFPAxh3QW8Cf11cuIQM2TWPh0FzgDq6lGTIGjahXBGKf3tn7jH6djoBwblC85NknEF13Vh6WGzEpbFigEWX9-0_SvREi6Y506Fk3s1uyPfzV04oS_gF9hHecvBrUtGPNSWs8jNe-Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959a8c1fa6.mp4?token=rj5DM17DSLm11EDTUfm0wJv5bQSSRwCLrUYlXMNDBP5gNWMjZgv4wv3dlJ3972lwcdZ6SJHt5LsS-TL4IX5nPjzAwK9eKJUXX3Hr5KyrNGN1WyU3qdqsWiXctrXVBy65HI8PCNnB_YXOuS95XOHd71drGzJj6b33D26ysIbycZtHofIoQbE5OgXls2SO7_72GaOKC2lKafLkbFPAxh3QW8Cf11cuIQM2TWPh0FzgDq6lGTIGjahXBGKf3tn7jH6djoBwblC85NknEF13Vh6WGzEpbFigEWX9-0_SvREi6Y506Fk3s1uyPfzV04oS_gF9hHecvBrUtGPNSWs8jNe-Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سود ۶۷ برابری دولت ایران از واردات BMW
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/136859" target="_blank">📅 06:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHrORIESa6rG53foPM3v5FOSrx642mKGPXKRdR6JUHOYRejAlam9EDCa5X5UWlJDpFS5DgNLdeAx_jwr4El9z4dOEbDkuggvEli8MOkXnzTuDrb4sjNFlCOTWtZuOkUv6m5hTGcBr4BO49PBBkVvQt_7_jvYxG68Ag0lIfn7tMVQNToe_adaYmwm4jUwFHTJ2kekSgVlGBXWqUHKnXgPxnJ4PyrUz7aD43bfWhHq_tqrmdrEotrWkA6MvFBh98SWHbrrUFqWYIYy_KLbrj6oB4HAb1fdFS7TRyQy_aPIoDNcvkEkfeIdOxoXd5TYES9OYu3EoQNuR5a_OXNcgCE6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136858" target="_blank">📅 02:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136857" target="_blank">📅 02:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مارکو روبیو: توافقنامه با ایران به دلیل نقض تعهدات، دیگر معتبر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/136856" target="_blank">📅 02:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حملات امشب خیلی ضعیف و کم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/136855" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/136854" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9377b3601.mp4?token=W9vNFz4EESAldLkOAR5l24XC30PrQuJizxsiZQ4RCDdVjfm_TrRpBlSfTaj58tjJ6ricv_6i858pM7YL6I0lck66RtLHtDw24N0cCkTQRKfN745gh1hGrbT65iBhPDi1uo8gQq3XJKHMH1AberaLvyQrcI2P7HPAbrDkQcWn8B1Xtf04Y7ndgSpfYL3IsIaADluIH7iOCKE1U6qSEJ5Z7t1I3MFf2cwDUdbFfTPABVY86cVettUZWAiHg4QPCQ1waJjOCyUkHmcr8g68hlZhCS4UdLcBDHvK5XfOMFINhmyF67g1xn_uBKYJqnYZBiV1EzK5z2xPaePLZ5NvuP-83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده لایحه سیاست دفاعی به ارزش ۱.۱۵ تریلیون دلار را با ۲۱۶ رای موافق در برابر ۲۱۲ رای مخالف تصویب کرد که شامل ۶۰ میلیارد دلار هزینه نظامی اضافی است و انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ علیه ایران را پوشش دهد.
🔴
این اقدام که تنها شش دموکرات به آن رای موافق دادند و هفت جمهوری‌خواه به آن رای مخالف دادند، اکنون به سنا ارجاع می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/136853" target="_blank">📅 01:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فووووووووووووووووری/مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران رو تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/136852" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k15w0dFNymx4oSsw6NAdeqxiPMYxpFte4YarXPj8Pi4jtd-tjloEfiM6ZAltgzH3syl6WETUZ2iN81FG8cunKUpQ7NxTvIRO_utsXSe9EH1ZXuAOBLyshJffrhuw2CmAkuCm5tkBX2-4AsaBa2pgiwx_rYMWVIOZ-yCKLt2QNVOx8WMRjaltgBRVlR7sVq31IenmBid_dCXf2IpAKsaNElmLbPtyO2aKG5jY8lN8A0YX7ruCR99Yf72Lg_TIuqeqgqbS2RjJvyKMrSf0FXfl7Cohh3SN7aVyDvdJ-QaxinWkuS7OF6hMQBEcYJqqg6B-CH2o-nzcr9e_EPXpFgfA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: امروز ساعت ۵:۳۰ بعد از ظهر به وقت شرقی، نیروهای ایالات متحده طبق دستور فرمانده کل قوا، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این مأموریت ادامه خواهد یافت تا توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای را بیشتر تضعیف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/136851" target="_blank">📅 01:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
العربیه: ارتش پاکستان هشدار داده است که در صورت هرگونه اقدام حوثی‌ها علیه کشتی‌های پاکستانی، پاسخ لازم را با استفاده از همه گزینه‌ها، از جمله نیروی نظامی، خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136850" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=cVEj8zblmoma7_wLpMvk5ZvOV3jRtOwILIUIxgofaUCdFyd2J7PLcx7BNnysNM0G8tE3bRTUrw_HnBFiBTmNFV7h1Epgh-5TYuiVeENI_Qovd8MI_yNg_yTeqQbSnO8fQvyn79tw8HVWVh5lT0OqZk8AenwRVkf73E1xuN9zwjRETmrFtbi6ms-dr55uwSPlPtEJlQvJQxPEice7ukG_SyMx9PmhQEq3QQ0IKVWRKS8lKIQUtp8GyjtVg7HxLwJHbVL6w-pVJajyGXe7iuVDrJYS7D0c3SxabmATljazRIsMeWDaAB-6ynyU9bpmvCoj_ivrgSdBJrfJ8DFVXAns5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کانالای ایتا وقتی آژیر کویت و بحرین فعال میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136849" target="_blank">📅 01:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/136848" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
الان به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/136847" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فرماندار بوشهر: یک نقطه در مرکز استان مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/136846" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یمن: ۲ نفت‌کش عربستان که سعی در شکستن محاصره داشتند را با موشک و پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136845" target="_blank">📅 01:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سیریک رو بازم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136844" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/ماهشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/alonews/136843" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پاکستان به حوثی‌ها هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/136842" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
️12 فروند جت جنگنده یوروفایتر تایفون ارتش سلطنتی بریتانیا جهت حفاظت از حریم هوایی متحد خود، اردن وارد این کشور شدند .
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/136841" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy-5CUp0v7aafV1JvFLMa7CHNx5wQggMGLI9BEPNuDrgtIpSQlQjx3KdlicOMJSmTr_vRVCR-L-YENgIva10Aa-DO6twj9fAtlwHiQDOmRHWlLSTlZ-oBreHHv3p2bozQwQRAYEuW0HqchaY9sm07EdZpyUEwv6zXq7mKTQ3pP8HEILTjKBQNFqDnU1mv56LeFUwkhJDDemP4Mm--fozOQ53FjxdXKvvyYNudG5uF9jut4q51wnWEyo0nlLldZGrH_2RM0c5_HgrRlUul4uGUgVgxo44iQtpT0QgU72LJ0Nn4UQXQF_AweAFp4rF-U5oP4EJZUSnDUZxd92BWzYWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان بین‌المللی امنیت کشتی‌ها (UKMTO) گزارش داد که یک نفت‌کش در فاصله ۷۰ مایل دریایی جنوب غربی الشقیق، عربستان سعودی، توسط یک پرتابه هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/136840" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
اینترنت ضعیف شده؟
👍
👎</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/136838" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/136837" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay7MjMWXqUb6AQi9hl55lTWN8r55124Zm8IurPyDr9FYALkYZyCtSM1kiYl_5dNlZlzVxMSm5QaJX7kUrU-1QoCpzWLYfA9b57Pr6KTmpthlb9oy6X5u0eM6N497Y6IhS3KQZJnj-hgSvUETqhLoIfnq331UYphtg1lGJm4Zf6-1HOGnhubS8jECqVvxG00DHL8Q76m282OGZouD_ClqLBb7EmEBbt42t1FRBArtm63cwWPogv0RkD2BmkuipDTeeNRJ1PJ586bF1riMaydcAEWhw2b-tr7WfjwZBImJbF3J3qDbQEY3GfWpAteBjMjmhXwli3WmL-M21nrxghCLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان ایران همانند خودش در انزوای کامل
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/136836" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی در نزدیکی عربستان سعودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/136835" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پایگاه موشکی چمران رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/136834" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یه سوله انبار آسفالت تو اطراف رامشیر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/136833" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پایگاه دریایی سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/136832" target="_blank">📅 00:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
لشکر ۷ زرهی ولیعصر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/136831" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال استریت ژورنال:
‏به صورت اضطراری نیروهای ویژه، جنگنده‌ها و بمب‌افکن‌های ارتش ایالات متحده در حال اعزام گسترده به خاورمیانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/136830" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
