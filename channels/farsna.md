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
<img src="https://cdn4.telesco.pe/file/KSisxuQEB-UYgrSishDZdc30S7ysmSCzbss_C6hvjfeykzK2pJxtp5cScts1_z82RtaXAyeceNCD89Bg29rdjCh6fhb86Q8qZCIoGkKVOJVhfCg4DdQug0va-uw2hYi3P07AY6sGY6R-9y3O-hylduHPI9K5pRj0RFu10hmB9jKoAKDd2t310QrE0CLvE8WLBDm66-7bfTeM7ASYlAcL-OqNE4nwwiQYs1hY6y6bzxQs3bAgmK-XuashUbH6Bl55Jitv84yhHvdOdgE_Zh7HPu7dPkMkzKmUwDAO_W3eFmifuknKopYhNa7-Mlcnz-q6zNvxwado6TTuItgJMV4vKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-448744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر باید این‌شکلی باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/448744" target="_blank">📅 18:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریایی خروشان، به رنگ انتقام
@Farsna</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/448743" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعده دختر دهه هشتادی به «آقای شهید ایران»
#حاشیه‌های_بدرقه_در_تهران
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farsna/448742" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ در آغوش ابدی خورشید
🔸
برخی تصاویر رهبر شهید در این نماهنگ برای اولین‌بار منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/448741" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ملت، یک داغ و آخرین وداع
@Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/448740" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448739">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته شدن پرچم‌های انتقام در تشییع امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/448739" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448738">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از سیل جمعیت مردم مشهد در بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/448738" target="_blank">📅 17:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XALCM6-K8nVpjLlICQ0pMByq6YOM-C8dZxpDvUvdJSmGaqDUgew47ljkkn1bn1wTnBjzYBK-AnuhbX011kxDcTtGr_9APaW6qarlpIAAd6HOFeLH3ZJE1SPmumWk45B6S1KCSxBpnGlr-BHej33fKDQzPl7C-qQqJXgmJJmC2dKpcUHfuA9XZL147yyADGxQSWohbRBGQdsOaE6jLGkzC8a9RAZchFCt9p28w0erDTZ3EhXvEsmp4elY6zHNl-nLkaCzij-1bNrLUvLkf55orQju8y-8a88nC0UZyFvHqjs7jsSPm4jBi9l2EVKRWUUeHU2TDkx9LZpOIKSRCp3zDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbnJ-8ICq9ami7vAndpDudAuk3sXaOaeD7qtB8lte38lgH8IqCVKmVLvuUVTOzZyg8n8hS-YvPo5QlW39uKhME0Q4d8RXElMBEQPnreJESQ-FYk2olIhDdppDQQexoZ9MPDdxmVAC5uJZhScdL2BoEWGRc_EaZGg3VLzpiVHWuPOuhM_5RN41EbsWOJq95RVspK4fdrjECYOdAwMRL6EiPX8jRm4to6t6Ji066OXYocaw6V5vFD4_82slPzvfyhNBifEPj9Y53ubtv2SbGEK_CqpK4R87_ojrrblNn0RfOlczS3y9y6uD-ipdGmODTiK24NxcpHrPIky4Px3MdTmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAPnRvinTI18_8DaWplvY2qnD5EBuBDPzYUpK4Pak9oHVOvoiSx-oGan14O_BK-OPFpeIELnQ9tIZl6okxjbhTqht28HyyLcoIKGTJ_SdAu01RZmEk2nXvcQLfDJEnqEwJ61YL2_sc9jnrOt2kXSD_IKNSfKc6bu-rsqyxHMZ4piyM3n9yt-QvNILy8YFQNRivh_TjXfYm-7oYT7SI84R1FOjklXTdscp6J2uQ-uHlp16GYDc2GFbElJACyLEKb6wOyp9C4EMD4mjiyhar7XKaPLFUL-tulcQ7s2611lmWD8NyB3_AlmQEHOM0p5PGe_EsdtGgLKAU5MVyvNm20vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pM-yng1BHxw93VLtbGP0lZU9reqdJp_49bjl5gE8QnA5ncVJPAS3ptt8cfPMFcJLXj8AR_y9w4CWbFjzjT4nYeXHCWhSLii2KU0Ur6aQ0-wEn7Cxn5GDygtkavz2lPWhdrBp3myHgff6FfG26KY3MG5b5E7_4x6uMrzB3QJFpmAkXn6_-BTe-CP6JwqPJUR2gIc_vLILRHGokAhu4aBiRvnk6O2x07KLER_-ydio9do4H3XUYGs4JBQlVSMjMPz6BeDrzkDMUhsdbtBmeYtfpQq557K5m2wFqAPt1X4cbUxaKN9AnVlS1BJ7Ord9XXW_8lJI7ZH5kysp6ugdkz_jiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbNs7NzSK2_1xO6b_Dd3f_tQi_aVRI5UB54ERBtKAVYZKaZ-CshaNaIKNi53dmaHF70g-UxxC--C8AeenPfa0bsFqZCyxzTyqv9tydPxNvAeTuX2XV14I8hRcEamEDvb6DORBACExcJg81nTReNFnYRkulEN3lqjW99UiOHdNVrCoFCMvNhinznfrScEN8J9XKabs7lGIU7g-ppXtdJFSXJ91WOrKsyyRqEgZDn57JXAshejpvlyC7-jKbCXNrGGT0_egz6x6domVxZ_baDrrkJ-XHgzuIV8vH-BfrjF6U1JwjBRD0aZXgxG0NzhR2_qNBJQ3yXvJLIgoZGzJkJPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VB6GMfthSCWnYnYegJft1Nt1Ckv7rOfZtoD8a0OKAiN_Du6lWL8RUXGKbgpnFXfqsm51-QNwyXJBciZboswgJrF-VK2XX_8eM7_ZITsA7YCksWl8FAFnUPK_lojrRqJT710lsIpVHQyoVOZ76yZVdfUIEl9PLOlCPsqjVKNkQQVUU5bBZC61k6VOQOLIapPAUmYdi1LVId0JW5OAidgsvy_R1HgYnIEtnAeOKG6DcYw5NVvH5s9ubQORdMI6BNu4poK7je6eXIvxyO998AqwRnL5z9b_KIC40HDD0pQuh569mtizTueC-VMqCst7tz2NjXi2VG4ZTnyUWk0tb34YfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej5nn33btIiaWw7pzfOjil1UwC8JYfjlPufyEd5JUlnMXymR6ZDAhJQLJpvP4JGiRS-s4gnMCySr9y6M83mCLr35vc7amVegBAax9taPVOSzxy06QUYDvPay3atA3Kx4YJdwB8IvHivBuBdfGPECzyErpFX9-JPg-sPhIX_3YdkZw32t099eBe0C0nwCi-o0fhQQE8wu4jL4ZR3RYGctzJln8rYtBRuhyiduVpBoDcp8CvWNVeW5QB_IjD7JpNJJ0oDtpt-C_rhjRkRXvc3QfU8MbkgQU0BM1CTMgsmqZ0DsuxION0K9EOMbc7WOzyuGAo2PDOAV-AqvkTER_j5SMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم ما ترامپ را خواهیم کشت در دست مردم عزادار مشهد
عکس:
حسین توحیدی فرد
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/448731" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظرفیت حرم مطهر رضوی تکمیل شد
🔹
ستاد برگزاری تشییع رهبر شهید در مشهد: ظرفیت تمامی صحن‌ها و رواق‌های حرم رضوی تکمیل شده است. از  از زائران و عزاداران درخواست می‌شود از مراجعه به محدوده‌های پرتراکم و ورودی‌های باب‌الرضا(ع) و باب‌الجواد(ع) خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/448730" target="_blank">📅 17:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی از میزبانی مردم عزیز مشهد از مراسم بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/448729" target="_blank">📅 17:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحن پیامبر اعظم(ص) پیش‌از رسیدن پیکر رهبر شهید مملو از جمعیت شد
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/448728" target="_blank">📅 17:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر پرچم سرخ؛ فریاد بلند خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/448727" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغل واکن در آغوشت بگیر این‌ میهمان، سلطان
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/448726" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با پرچم یالثارات برخاستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/448725" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم مشهد: حرف ما یک کلام؛ «انتقام، انتقام»
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/448724" target="_blank">📅 17:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر فاخر پرواز همای در رثای قائد شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/448723" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم متفاوت خون‌خواهی مردم: ترامپ را خواهیم کشت
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/448722" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c874506631.mp4?token=jIbgJACqAVFy8DucqNbtpZkqbIybW62MJnG953A5P0eNE8YNy_IoBWraDnQOt3_rfCWaNvIxjD0GPD1DBOrA12uawvFbZAGNpzH31PtyOOqOXNOJdZJo05kL5Xp37PQpXkaT0_4Sn4ZbJIjCLppm38nFrht9SAtM_R3SIEtOrlh5QxaRG7aeyxkCbsUcP_HwBYhrXRe7eQyKlFQFByH_NigIdoOqVJ-sjXWbVIJB1-GQBfOJtv_w6Yh2d7tkkumORC8VN20EnjaS4175-EU6wi3Cm2pRqnyDAvnvgmFFno427rWn6gpgCp73PdzQz6pILNnSr1icojTnUN3QIKMkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c874506631.mp4?token=jIbgJACqAVFy8DucqNbtpZkqbIybW62MJnG953A5P0eNE8YNy_IoBWraDnQOt3_rfCWaNvIxjD0GPD1DBOrA12uawvFbZAGNpzH31PtyOOqOXNOJdZJo05kL5Xp37PQpXkaT0_4Sn4ZbJIjCLppm38nFrht9SAtM_R3SIEtOrlh5QxaRG7aeyxkCbsUcP_HwBYhrXRe7eQyKlFQFByH_NigIdoOqVJ-sjXWbVIJB1-GQBfOJtv_w6Yh2d7tkkumORC8VN20EnjaS4175-EU6wi3Cm2pRqnyDAvnvgmFFno427rWn6gpgCp73PdzQz6pILNnSr1icojTnUN3QIKMkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی تصویری از شکوه و عظمت ملت در تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/448721" target="_blank">📅 16:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=LK9FHxGjRloTrNMSMfKgpXltOKw5wA-55tN5GloyBC6NtjU2bf8zfVIrLh80Z5MKPOHSQyPJMtLMsybjMkhxr54UnRgwZ14gxJC0BaPnqXaJWK8n_U_Fd8mM3hi_IYrpXC3t2PoZ4k4QJSumJ4EeW63i6RZddKYrPEATyBBnWFgRzDof9A8WajVolP0IvD4W0JA0ZMMsiyO0zn1oYxhK8U3-_zwaIU4GTBKFv20ue5l4XK18w8nwwEVyCCNNp1LquYuOpfUPzF20p8sYrJPlxoFddAAeHigUYBiWkKZoaJE3eTYnorZNEC_C_Fhzv0LVkvsCScttk73jh4X2LRwaJr6SmuMP1eTVlK3dUrkS8LK90XLcbod5Icw4I3K_JdrBxjRfepCNzAc1u2S_YdmzWpLE-tiaFIXWBh9Ra4FqElMUAgS7Jo9lMU2MzoD3rD6tXIUR5cWJI3uL_StHmSgCCcZ5HnMt8omrJgoCB0sBSh2pkXuCUMewQ2rGyWd7zMtxFwEaP8b0HxXjgt_zzg-d0Jqox0nV4tUB3wQAAvhQEpJxi-ndA-5LlaLsvk_JSxlTARzpAA25GYCPhtS4hsZS-e8FlM5t7MAsBfuBdD2t5yhfJecnQQ3_DCG_VEn6Us0Sa6G_IgwUnUFXs85OTL8Q8k652eee3jS7RFEKvri-jr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=LK9FHxGjRloTrNMSMfKgpXltOKw5wA-55tN5GloyBC6NtjU2bf8zfVIrLh80Z5MKPOHSQyPJMtLMsybjMkhxr54UnRgwZ14gxJC0BaPnqXaJWK8n_U_Fd8mM3hi_IYrpXC3t2PoZ4k4QJSumJ4EeW63i6RZddKYrPEATyBBnWFgRzDof9A8WajVolP0IvD4W0JA0ZMMsiyO0zn1oYxhK8U3-_zwaIU4GTBKFv20ue5l4XK18w8nwwEVyCCNNp1LquYuOpfUPzF20p8sYrJPlxoFddAAeHigUYBiWkKZoaJE3eTYnorZNEC_C_Fhzv0LVkvsCScttk73jh4X2LRwaJr6SmuMP1eTVlK3dUrkS8LK90XLcbod5Icw4I3K_JdrBxjRfepCNzAc1u2S_YdmzWpLE-tiaFIXWBh9Ra4FqElMUAgS7Jo9lMU2MzoD3rD6tXIUR5cWJI3uL_StHmSgCCcZ5HnMt8omrJgoCB0sBSh2pkXuCUMewQ2rGyWd7zMtxFwEaP8b0HxXjgt_zzg-d0Jqox0nV4tUB3wQAAvhQEpJxi-ndA-5LlaLsvk_JSxlTARzpAA25GYCPhtS4hsZS-e8FlM5t7MAsBfuBdD2t5yhfJecnQQ3_DCG_VEn6Us0Sa6G_IgwUnUFXs85OTL8Q8k652eee3jS7RFEKvri-jr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سیل عظیم جمعیت مردم عزادار و خون‌خواه در مشهد مقدس  عکس: محمدعلی حسینی @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/448720" target="_blank">📅 16:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=XU7IY3WuSey5DcwHMgQqnDjUd8xRvhgst9KEAFosTVakH6iTL_9ZibjewGU575jL1HvYwEL643s53gJ_3Yb512Cr-ctoqxao-6wybA898yuY16Qum4EMfo8S0XKXyd5qfNAUJk3kW6VfaZdgmRfn6Cn-c7SoXnDlw51aHb_FJqoaVJvM75yyt-pIoelw7oMb2gVtd6kkZIIWs1JKzvMX6rwciy8K6dYRG-9AoxfE7ACQ6iv613Di6i8gs2yd1qYB9nqe_cHv99y8dvyREKMWRWrwC7rl0cEXZI6ITrsxbjT7zJ_G1rWZYhXsIrYMg_S_r0Ttver9E7i7k1C55UAE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=XU7IY3WuSey5DcwHMgQqnDjUd8xRvhgst9KEAFosTVakH6iTL_9ZibjewGU575jL1HvYwEL643s53gJ_3Yb512Cr-ctoqxao-6wybA898yuY16Qum4EMfo8S0XKXyd5qfNAUJk3kW6VfaZdgmRfn6Cn-c7SoXnDlw51aHb_FJqoaVJvM75yyt-pIoelw7oMb2gVtd6kkZIIWs1JKzvMX6rwciy8K6dYRG-9AoxfE7ACQ6iv613Di6i8gs2yd1qYB9nqe_cHv99y8dvyREKMWRWrwC7rl0cEXZI6ITrsxbjT7zJ_G1rWZYhXsIrYMg_S_r0Ttver9E7i7k1C55UAE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش ملت عزادار ایران، وارد میدان ۱۵ خرداد مشهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/448719" target="_blank">📅 16:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025348386b.mp4?token=mRuwV_8T1tOhrBfzmGDMLBP9KLWuiSns6FfX1pesOf6vG4qbegpj3m0RR15l1zbEoOZJM_oOByI5-lTur2v1F2aSzjRWOoHL2Kl1f5WmwF9qbOiGmPzFEDMxRoTWVMV_8ZTxKaKLPJyObGZKqesvH6MB4Yh3ce2Ste9ubyu84DBQ-fNQDeNgezhcukIBSWEH6GtSNA3GQFRmC-I3GWXq4b1f9PunrouV-cspAVGLXqLa-nVx4FuzFI1S0YyRwFgk1emDzZexdI49edn4aMmIqf9jeS46DoQBX7kBIDq9m0ScXz3vV5EGJVer52EF6vgFRF6gu15v9kfC9iJYboPFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025348386b.mp4?token=mRuwV_8T1tOhrBfzmGDMLBP9KLWuiSns6FfX1pesOf6vG4qbegpj3m0RR15l1zbEoOZJM_oOByI5-lTur2v1F2aSzjRWOoHL2Kl1f5WmwF9qbOiGmPzFEDMxRoTWVMV_8ZTxKaKLPJyObGZKqesvH6MB4Yh3ce2Ste9ubyu84DBQ-fNQDeNgezhcukIBSWEH6GtSNA3GQFRmC-I3GWXq4b1f9PunrouV-cspAVGLXqLa-nVx4FuzFI1S0YyRwFgk1emDzZexdI49edn4aMmIqf9jeS46DoQBX7kBIDq9m0ScXz3vV5EGJVer52EF6vgFRF6gu15v9kfC9iJYboPFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌های انتظار و دلتنگی و حسرت
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/448718" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e61f7f3c.mp4?token=dYPTyOlk02uc5u4VksMEUfCgiUXVqVbxfQzzOPSGTAykFtsYcrNJZYbGEiJOQvcO7h5wucCMUQ4AF01jfuUlUZe9uxbIM_5256aFtXdtW3LiFXlVBf9_I2mPTk_ffie_KOrk2w08VjkowpS324eKiUOSmiD-ZtHkvcwkxzyFdO0GWJpjaK_HfYbYx8WgEO5fK6QjDooyYIlCx60nYOQ9o0TvxhE1NJhKvmBQXyftBzCRD6ELgoBKr-YF2Zz9Im-6p3kU07KiI3fkQWDkwtxCD3NBj1jePUmz0JSMl80VXlIKziaiDe5ygQFF0BZmCrauDsJDnHDrl62BzAPx4xWPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e61f7f3c.mp4?token=dYPTyOlk02uc5u4VksMEUfCgiUXVqVbxfQzzOPSGTAykFtsYcrNJZYbGEiJOQvcO7h5wucCMUQ4AF01jfuUlUZe9uxbIM_5256aFtXdtW3LiFXlVBf9_I2mPTk_ffie_KOrk2w08VjkowpS324eKiUOSmiD-ZtHkvcwkxzyFdO0GWJpjaK_HfYbYx8WgEO5fK6QjDooyYIlCx60nYOQ9o0TvxhE1NJhKvmBQXyftBzCRD6ELgoBKr-YF2Zz9Im-6p3kU07KiI3fkQWDkwtxCD3NBj1jePUmz0JSMl80VXlIKziaiDe5ygQFF0BZmCrauDsJDnHDrl62BzAPx4xWPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلدادگان رهبر شهید انقلاب در نزدیکی حرم مطهر رضوی، چشم‌انتظار رسیدن پیکر امام مجاهد شهیدند
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/448717" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
سفارت آمریکا در اردن: گزارش‌ها حاکی از آن است که چندین موشک‌، پهپاد یا راکت‌ در حریم هوایی اردن هستند.  @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/448716" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
رهبر ما از سفر کربلا آمده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/448715" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3a346e64.mp4?token=f122LVo99JpYbHh2WGbpnZ5Yr0Vt5qm6BW6oncDYyn-YIfEO-QZbO685Th6tCFxCnoaHuq8cDBY91skmjlvuHmYT-F5JmnF1L1LXQ2QElyEM3x0zRq-XYB0wT348sGragTgwKi5x84QfV45wwKNeCre_3CJSH3y98PmpkcQZdDmCTXSqzuiKNHpLJt1NZcPLQlWsg4_X7IMkczZvP_9NmlnWl1eyZmxg7W2B3WBpoMqAon0J8SYSzRfiqlIPi_yvQse_5gVo4b0K1y4FFcqK4yUhb_uY6M78bhPLcRfWFp2Shsy-y9MOsfmpEXYtcIHCCMa8LG6ghaxBvFrmDuiWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3a346e64.mp4?token=f122LVo99JpYbHh2WGbpnZ5Yr0Vt5qm6BW6oncDYyn-YIfEO-QZbO685Th6tCFxCnoaHuq8cDBY91skmjlvuHmYT-F5JmnF1L1LXQ2QElyEM3x0zRq-XYB0wT348sGragTgwKi5x84QfV45wwKNeCre_3CJSH3y98PmpkcQZdDmCTXSqzuiKNHpLJt1NZcPLQlWsg4_X7IMkczZvP_9NmlnWl1eyZmxg7W2B3WBpoMqAon0J8SYSzRfiqlIPi_yvQse_5gVo4b0K1y4FFcqK4yUhb_uY6M78bhPLcRfWFp2Shsy-y9MOsfmpEXYtcIHCCMa8LG6ghaxBvFrmDuiWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملات امروز سپاه در پاسخ به تجاوز و عهدشکنی آمریکا  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/448714" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmUe6UaISCvyEeqYF_h2leZKgwp7mshWxWPoNQbR2D-4L9Av6do2r-GlltniG7UJZJxZ8Yg3pyPhNLCgg-Bg5eKLILRdOMWEf_Sv0U6Wa8bc-yVNySnGQXDzR7JkAHwq69H8Fl086v_lN4eVoeI53HEgm79afhOEwjPR22fM7a0Ryv5rrfJgozQl1Nq3rbo3KzffdWFQNHvr4W-M0hwrunE-5-U-up57OdLR0IrH4X5rMsPo25GvbJVMtoN3vIQANKQGX1aLRYluiYGkPd6mx9bUOQaKSmBbd63vcDZWxDPj2vEXa1yVa5uQQHbmqggXQjtPX_aHzQwOE06kl74wKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعطای نمایندگی فروش
شرکت فنی و مهندسی شهدآوران، تولید کننده محصولات:
پودر عسل، کرک و ماسالا، پودر شربت، گلاب، عسل و فراورده های آن (عسل ارده، عسل بادام رمینی)
با افتخار 30 سال سابقه تولید
متقاضیان و علاقه مندان محترم جهت کسب اطلاعات بیشتر تماس حاصل فرمایند.
01132347085
01132347084
09116336557</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/448712" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/448711" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بغداد: بیش از ۱۰ میلیون نفر رهبر شهید را در عراق بدرقه کردند
🔹
کمیتهٔ عالی مسئول سازماندهی و برگزاری مراسم تشییع، امروز از مشارکت بیش از ۱۰ میلیون نفر در تشییع پیکر مطهر رهبر شهید ایران در عراق خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/448710" target="_blank">📅 16:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f14782d82.mp4?token=ZilxrFMonn8Jhty07q-jTiQkGCdjdcsZHs3rpj4iSfvRCUJD0fknqFUAREAFnR0j1aiMR8bGWHksTEDReh-97ezuLRh0rKtQyRNjVD54N0ondX1KVl_Z65ZQGHfmP8wvP_vra0YLSs3uZhishHktm7Qi5B6ikYKtSn1oy4QTKBt7lmnpcIdFvFFOqzHYEiVvLeQfOsZbW02VsLxmV-UcTLfVQzi-97udRLoDbGnVhQjdSL3C0DxyxGJgUwTEodOeveLRHTq2P9WiTcK8jQMHjJjdra2CAAJwEjqmK81lX6Lw07kYma009tupMMhNXy3JSIF4JMf1DsfDrA2csjdfBFM-A2vOOgRzRGXW8djWQ6daXQmjfclw3M2u8AbKS_DqNFpjtVhTqvvHz8S1XBQq3rl-06XLQ_X26lawmzyu90ee3yjazK-7IW4b4fzvqMfWbeDKdojRIHngnI_rQp8qvhQiuH7Km4J8IJcYCFuIhzeMG84QIQZbcePuEdZJAyY5xl9GKwcvmRWOPKEbWuL1YI1KVf3ug1xq1XGJJA1KzJxTo9sCW_mw1K_fggqH8q81KPyxuRt0b10xMkVvHhMtNFZ3Ggq4Ev295jcJhZFQ6e5dcBpSfN-KNLV92TQwU39q-zsVeiB8X8GAJKujnizQyRnhx8ZVwExy14UxDrCHn0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f14782d82.mp4?token=ZilxrFMonn8Jhty07q-jTiQkGCdjdcsZHs3rpj4iSfvRCUJD0fknqFUAREAFnR0j1aiMR8bGWHksTEDReh-97ezuLRh0rKtQyRNjVD54N0ondX1KVl_Z65ZQGHfmP8wvP_vra0YLSs3uZhishHktm7Qi5B6ikYKtSn1oy4QTKBt7lmnpcIdFvFFOqzHYEiVvLeQfOsZbW02VsLxmV-UcTLfVQzi-97udRLoDbGnVhQjdSL3C0DxyxGJgUwTEodOeveLRHTq2P9WiTcK8jQMHjJjdra2CAAJwEjqmK81lX6Lw07kYma009tupMMhNXy3JSIF4JMf1DsfDrA2csjdfBFM-A2vOOgRzRGXW8djWQ6daXQmjfclw3M2u8AbKS_DqNFpjtVhTqvvHz8S1XBQq3rl-06XLQ_X26lawmzyu90ee3yjazK-7IW4b4fzvqMfWbeDKdojRIHngnI_rQp8qvhQiuH7Km4J8IJcYCFuIhzeMG84QIQZbcePuEdZJAyY5xl9GKwcvmRWOPKEbWuL1YI1KVf3ug1xq1XGJJA1KzJxTo9sCW_mw1K_fggqH8q81KPyxuRt0b10xMkVvHhMtNFZ3Ggq4Ev295jcJhZFQ6e5dcBpSfN-KNLV92TQwU39q-zsVeiB8X8GAJKujnizQyRnhx8ZVwExy14UxDrCHn0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
🔹
سپاه پاسداران: ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی…</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/448708" target="_blank">📅 16:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae2a9a6e61.mp4?token=Ve39XS7a-m9lkwvuXpAfjrMivW2apuT2A1ATwxVVsMuTpHIJ3mIvnUkdMTDGPHH7GKfqLqvge9KO2Wge6wFsY21PpkjVyN0JlpIgr2ZnjfXM-mirendMlYJ_0vwfFWhPAJQiaFhvxYmHVh8HaK3w2i_1_uzoAxvmBCODRh0Vkd96QyNNdYhWtWtn00XghY69QAXV58ZMkJGb0ZGMlOgi-Ro-fEu8mq7ZulDSOWZhH33W0Xuw7J6ERvCS1SydVr3AtKkRH0sx4DQLP3CBfltoE-XntfFlkoonwtQBhNBu1Sjr7vH0E4XcAAGtStfX3r_-Ok_1xCjh2kV_GQdphm67ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae2a9a6e61.mp4?token=Ve39XS7a-m9lkwvuXpAfjrMivW2apuT2A1ATwxVVsMuTpHIJ3mIvnUkdMTDGPHH7GKfqLqvge9KO2Wge6wFsY21PpkjVyN0JlpIgr2ZnjfXM-mirendMlYJ_0vwfFWhPAJQiaFhvxYmHVh8HaK3w2i_1_uzoAxvmBCODRh0Vkd96QyNNdYhWtWtn00XghY69QAXV58ZMkJGb0ZGMlOgi-Ro-fEu8mq7ZulDSOWZhH33W0Xuw7J6ERvCS1SydVr3AtKkRH0sx4DQLP3CBfltoE-XntfFlkoonwtQBhNBu1Sjr7vH0E4XcAAGtStfX3r_-Ok_1xCjh2kV_GQdphm67ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید در آغوش مردم مشهد
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/448707" target="_blank">📅 16:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11318f247d.mp4?token=PuZmvt3KKINmzuygLYaFcrVFm9httVSD4-IhexI6tGjsH_M4vvbbed9PeM-421BYdHK-UQdT7go87G6uf_fyKJ__eq9M6jqls74DLixdDU3zWeThrMsuO1IkOrY-ki1KaDbZcAa9HW5uhvuGgBDgqNhHVPiULH8tHGOk86DDSpgHZm-HY6Rh8wuue4Wr3DRpCGi10dyIIDg0vuKVqcvzptYk_3OicH-wTYyj5G-37vXuG_cTI4s92zeKuuNEylv5Uez35fcdKjKy0RvF3MQCDUXLi4Vhq2f1JyuXONxx4Fv2uaLtxPKfdB5rC5YG7bLZgLMN6Pml-GXt5fjJOTZm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11318f247d.mp4?token=PuZmvt3KKINmzuygLYaFcrVFm9httVSD4-IhexI6tGjsH_M4vvbbed9PeM-421BYdHK-UQdT7go87G6uf_fyKJ__eq9M6jqls74DLixdDU3zWeThrMsuO1IkOrY-ki1KaDbZcAa9HW5uhvuGgBDgqNhHVPiULH8tHGOk86DDSpgHZm-HY6Rh8wuue4Wr3DRpCGi10dyIIDg0vuKVqcvzptYk_3OicH-wTYyj5G-37vXuG_cTI4s92zeKuuNEylv5Uez35fcdKjKy0RvF3MQCDUXLi4Vhq2f1JyuXONxx4Fv2uaLtxPKfdB5rC5YG7bLZgLMN6Pml-GXt5fjJOTZm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پرواز جنگنده‌های ارتش برای تامین امنیت آسمان مراسم تشییع
🔹
پیگیری‌ خبرنگار فارس در مشهد نشان می‌دهد پرواز جنگنده‌های ارتش در استقبال از پیکر مطهر رهبر شهید و برای تامین امنیت هوایی آسمان مراسم تشییع بر فراز خیابان‌های منتهی به حرم مطهر رضوی انجام شده‌ است.…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448706" target="_blank">📅 16:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xws1Lf93-iT1K7GmI0j5jDvCfY3KO99xRpUmyjHZjWpLNLUM97icuWyp4n8-X55AZl1YyLVw8Mh55N5fc9NN4H90XM-82mURmAIh9mgnyT8zVyzLb9INTZjG1Tl87wNqZzIMN3QHjxT1eVZlHnhds-m2bceUpds8id14v_oXuvxJYM1sSYCub-Qj3ucdp-5CwaPvvGvrqiCd0UpuqKw-d5fTp1n1LFSccsue458Jf5v2eMgjx6T6AzfmydtsuxHKnfkvbOiuFX8EHtaY4jhssl_rfNrzdx8O4jQvr6kxSQdRgIt4WkLgFxkuQYKvHtkWF92nCRy5NeJoLx5WBW20xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqrC9zYfqsXvpuRoAEz7R4ouzEv5BG3WWeEH0bxLBqPDP6s8aZ3PLXvJ6h8g0j6avwbz2FV_g2cjVt2dATIkLhUz87brpmlfOFgmcSSQHrRWYv6XLNvk0WEbrOE-PlBCOhOpAxt2LU-sS7gPN-UNVJXIu7f2RvED0X7_yz0jZ3jAlWqjpzEBUKUSokNgy537Y3tGqovhFVOAh_AYjWmCbHo3vJcRK1EDQW87ZOUTVcR4UyOj-2tR08PNwKtcxo8fgNsQxbDmfE3midNxkVYSwfvzOT1lVsgIYqvHXLh2qRF1bAqS1LHWGIAtVBd1DOYnNzYj5PH36kTM_6F9SMxcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXCbOQkj7pBdOViHEfoK0mKaiWNUqy1_AXVR0-4qocRvEhd4XyVO6-zCxfhlnOeFE4RHYfWvCbAbqjQNFvtbcj2LbyjcidyX3YFHzS0n55_0Wxa_nYsOfB4lIKpH7BpHASRZ0yqXiZS6L5NQgko55ruh-7_CmwdF31LUUZbiaUJ1IsP4_BbkXEdB7B9cgi-rq6gC_p4pF5tz_H9oaPQ4YVOxHrVoRYlwVAwcY9gX1ZpWU7a-iYsNN5egpu-YWUUAY5VjyVF2UmuaNl-lG7CIZVa4V2eB74Cz_a5bxySny2u7cIxjz2-XpPE-hjByDWjkEb-1_iF_e5VpdFHn_qc42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfwNN0GgCXngXqx2sC00YZK9TFdMk--ZeY_Sgc0JSuueI3EA-_h1V-1jeuQS1jgCrmWxsmhY_tdh9sVvN7E3--8Vjmrm0h5Z69w2M1TyPAsoOMtnpPYa-jXq7Sc_7_se8hKdYXfAKw5b9vHhr1DDy7N2vw1S9nPqrzG1-jzDd4iWz-oENPym8GjuWEFqqRC1j9aV3ZTVfgpoC8ZeEBTTYVePHcizM8bjBDVvN58eS-j0Ox2aDQLMu-3ilsVcC5EwyN5tjT1ZuO71fsCTIldZ8IevwKVinIbDZcTR5n1WLEFdyX6fCMIF1wLAppL7HQlYBOOyWKkGOSjXaoK50bNt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rILOs5cRQyy2ZK1C3VcQ9Y7i69Ji5FOjkRoDTZbLeB4baTnck4gji6xdEPDPUI7w34GkkEcgvVbWLKvhhv3kVon-kZJmpggZAJ2Vvc73GnNfrWP_W5MhbO77ZFR-x8zD785CBf44r3C8rjOwsb8Q0kxDu0FMwiH9mlR4oFR_o2wxF_JDzi5AzOJz5rpYWrYaHl8EAQOWTwM8TempoiBFHEBCqfvx9hh-E3jzmG4i1Fvkyiq70UFHqxJW_seEu9eR5tTjCO92txGicx5_Qzyt_Mdphm2LuI69vsEpXblMxCBnSJ-FoS8l3TO-U3w25PzsIOu6lbyFUfNNBkh5gqfvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YICI4BBatjLtoXmUb626ihGWmhTjjlThwIcR1hvcSUYkBgh5YEJogqSj_wKgOsmlDAXEbEd-wM8uQL7uKLB33efoSOViFjsQ0YzFx2I4tq7SpYKQBVFo5pLoyjztf0iwc6wzb9HEQ6JcOzbWHNg3WYm2NOQChPjqFPbYXOfxUA5t5UHWGGjkQIxIkDqcpWBNVtOF0bwAVgbmCzMqL3dFshZX0-dZUNuPCJxSSYKK8XXvQML2Ga8AKcm1y1WIv1YkYRPfeHK56lw9TgN699fvcw7HZuzJ96qqXKkeRIpy7Pyxi5scy9I60PVcRbhVxRT7bs4bmQEcnQyuUg-WeSMfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7Z4NOtJQduyMZXZp_L_MrUnsALbTO5DbTM4Idr7RuXF58cVn5nLTiq-yQ-8kV-pXTRDKTM79PJJT71LgwfdWE-g3EeI77TmvCn3edwYpDt_-hEFNNmiMJSmnLBp5Xw8bHlK-vxw60_W8cmkrxJNwf1JRRV4sL4Sjh4sdKUu7948_m2FhQJ5-W5iVsu7e7KLzkWZtYAax25XFCWDuhD5FTE64tibDr9q90_DuRYdBuQ3J66_hqZQ8qlI7lhkFrNMkabVpGF0uzyLTIs89f0wPbEpLj3THsHCSkaCkHO-LQDHL5NHY4xVwieflMHjIOEPT9bE107dWjrpOPZWZVQXqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیابان امام رضا(ع) مشهد جای سوزن انداختن نیست
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448699" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرلشکر عبداللهی: قاتلان قائدِ شهید را قصاص خواهیم کرد
🔹
با عرض تسلیت و تعزیت به مناسبت شهادت پیشوای مسلمانان و آزادگان جهان، حضرت آیت‌الله‌العظمی امام خامنه‌ای (قدس‌الله نفسه الزکیه)، به محضر حضرت بقیه‌الله الاعظم (روحی و ارواحنا فداه)، رهبر فرزانه انقلاب، حضرت آیت‌الله العظمی امام سید مجتبی حسینی خامنه‌ای (مدظله‌العالی) و امت اسلامی؛ در روزهای گذشته، جهان شاهد خلق حماسه‌ای کم‌نظیر و ماندگار در تاریخ بود.
🔹
آیین تشییع و بدرقه امامِ شهیدِ امت، به عنوان نماد و جلوه‌ای از شکوه، بصیرت، ایمان، جهاد و مقاومت در حافظه بشریت به ثبت خواهد رسید.
🔹
اینجانب‌ ضمن ادای احترام به مقام شامخ آن قائد شهیدِ عظیم‌الشأن، بر خود فرض می‌دانم مراتب سپاس و قدردانی عمیق خویش را از ملت بی‌نظیر، شرافتمند و بزرگ ایران و مردم سلحشور، مسئولان و نیروهای مسلحِ کشور برادر و دوست، عراق، رزمندگان اسلام و تمامی مسلمانان و آزادگان جهان که با حضور بی نظیر و معنادار خود در آیین‌های وداع و بدرقه سیدِ شهیدانِ انقلاب اسلامی و جبهه مقاومت، حماسه‌ای بزرگ آفریدند، ابراز نمایم.
🔹
حضور بی‌سابقه امت اسلامی، فراتر از یک مراسم وداع، فریاد رسای حق‌طلبی و خط بطلانی بر نقشه‌های مستکبران عالم بود که حق و باطل را به‌وضوح از یکدیگر متمایز ساخت. این خیزشِ انسانی، تجلی‌گاهِ پیوند عمیق میان اراده ملت‌های بیدار با مسیر متعالی شهادت است.
🔹
دنیا و سردمداران کفر و استکبار جهانی، به‌ویژه آمریکای جنایتکار و رژیم خبیث صهیونیستی، مبادا حزنِ جاری در چشمان ملت و خروشِ برخاسته از این اندوه را به حساب ضعف بگذارند.
🔹
این سوگ و خشمِ مقدس، در مسیر خون‌خواهیِ قاتلان قائدِ شهید و رهبرِ مسلمانان و آزادگان جهان و شهدای مظلومِ جنگ‌های تحمیلی دوم و سوم، استمرار خواهد یافت و آنان را به سزای اعمالشان خواهد رساند.
🔹
فرزندان برومند و دلاور ملت در نیروهای مسلح، با توکل و یاری خداوند متعال و همراهی ملت‌های مسلمان و آزادی‌خواه، با اقدامی انقلابی، خواب را از چشمان دشمن خواهند ربود و عاملان این جنایات تروریستی را دیر یا زود قصاص خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/448697" target="_blank">📅 16:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5479d3f368.mp4?token=lQ7UVfcxHfJQX_lRxPW4rEeQwkNbnKfV72Cbotuh882GOPPRAyfqLjhE3mD0AAbsJufLRTj199-1iG-zIVRZ5bpwWdOBOu7JrtnEdEvW-As31Cn2TTtpEnKxkrrdDrzcPYaHz0V9cKIMXAodjTS89S3dJ0Js0Q8234qyLXMSLGlvgKqDxkv6ohR_A91K59iFmRT1KnWPlCHgxO_bjTbjZ1rYBvl0DJdkRRZ_dr0X5oZNrnhbsI85OsPk1t-6AaWiD7L3gVyeDt0XewSq4yHFGAJGYOhledF7If0jGMne4M8zts50EcwSj7nkoCLseydsXCreYR7ff-ui_oJwnMcbzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5479d3f368.mp4?token=lQ7UVfcxHfJQX_lRxPW4rEeQwkNbnKfV72Cbotuh882GOPPRAyfqLjhE3mD0AAbsJufLRTj199-1iG-zIVRZ5bpwWdOBOu7JrtnEdEvW-As31Cn2TTtpEnKxkrrdDrzcPYaHz0V9cKIMXAodjTS89S3dJ0Js0Q8234qyLXMSLGlvgKqDxkv6ohR_A91K59iFmRT1KnWPlCHgxO_bjTbjZ1rYBvl0DJdkRRZ_dr0X5oZNrnhbsI85OsPk1t-6AaWiD7L3gVyeDt0XewSq4yHFGAJGYOhledF7If0jGMne4M8zts50EcwSj7nkoCLseydsXCreYR7ff-ui_oJwnMcbzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حضور جمعیت عزادار در خیابان‌های مشهد
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/448696" target="_blank">📅 16:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfae7ebd2a.mp4?token=OIwZwE1Sb7nELE-ivBIEr_272xkeO-ldZ-rUfIPxXr5jXGALIxYY4FchpfvjikOUHCLPTbR4S05TSNZq7y8t8uafwYrMnz_fUs-MsWDPZrdlMbpbjdgEfnBtY88OIsa01aYlQVRON9QIw6sDCz1F5HYjsMRNTSkkhj-wlfrsRMs9COiIOhUBQOSQGC0HbgcSN28PHCtcy7m61E7w5Tr-WWc6rvUXLva8OzdPyWzs4CvEv74bFWuoNOJBGFjDd44EO2Fx_v4KkZJmHc45gnrmAP66MC3sj7UtemO6NcLeIEZY86i8-PwquxMLD9HOZYeOftAuPkGTvvb3rOqVmFIKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfae7ebd2a.mp4?token=OIwZwE1Sb7nELE-ivBIEr_272xkeO-ldZ-rUfIPxXr5jXGALIxYY4FchpfvjikOUHCLPTbR4S05TSNZq7y8t8uafwYrMnz_fUs-MsWDPZrdlMbpbjdgEfnBtY88OIsa01aYlQVRON9QIw6sDCz1F5HYjsMRNTSkkhj-wlfrsRMs9COiIOhUBQOSQGC0HbgcSN28PHCtcy7m61E7w5Tr-WWc6rvUXLva8OzdPyWzs4CvEv74bFWuoNOJBGFjDd44EO2Fx_v4KkZJmHc45gnrmAP66MC3sj7UtemO6NcLeIEZY86i8-PwquxMLD9HOZYeOftAuPkGTvvb3rOqVmFIKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خروشان منتقمان رهبر شهید در چهارراه دانش مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/448695" target="_blank">📅 16:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3326c346ff.mp4?token=iWpIX6vkQ-D4OmViF8c8kRvnC4NiXeWQsEnlHOZ_imV89V6uXb_D5ztLDh23ccb90OpA0g8YnAh1FQt7i-Tf98tIPjavRI00KRKtR4cgzDUWVdIv75zQx8-LxGsckhB2tSv-dYaeHTTMVTuWeqOTAQxkgToQ3FxM4tmm6NTTSh9DSOPOsxjfsFRvGmqZSvmtqJYd2uFT--zsotzk1VtyrUgDAkZnuR4WpvMqGgR1_shmVxrSJ-HDs1o7y8153I-cFJemL-37QZXdDf3B9rjjBMVAY7-Bd734VSyMRsA4iFGc2LNl28mFp22O2yYnCL0Ru7BpjXZ-lbYnzSM3A-ZsZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3326c346ff.mp4?token=iWpIX6vkQ-D4OmViF8c8kRvnC4NiXeWQsEnlHOZ_imV89V6uXb_D5ztLDh23ccb90OpA0g8YnAh1FQt7i-Tf98tIPjavRI00KRKtR4cgzDUWVdIv75zQx8-LxGsckhB2tSv-dYaeHTTMVTuWeqOTAQxkgToQ3FxM4tmm6NTTSh9DSOPOsxjfsFRvGmqZSvmtqJYd2uFT--zsotzk1VtyrUgDAkZnuR4WpvMqGgR1_shmVxrSJ-HDs1o7y8153I-cFJemL-37QZXdDf3B9rjjBMVAY7-Bd734VSyMRsA4iFGc2LNl28mFp22O2yYnCL0Ru7BpjXZ-lbYnzSM3A-ZsZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه یک عهد، از بلندای آسمان
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/448694" target="_blank">📅 16:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448693">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeUT8LXmGo6JyrnKUwJivtOhCc5YkgAmMv0mkeoiV3HKP9t0bgdZjXGf2U2-iBCKRVEJz08HUcsalnlHbKHi4eBXzfnddWNjcV1kGWwaQH_XM_dzLlH-ehAdq7wOknNlQcSSWthLrfHHu66b3lLy4qwvjJfeOWy-PORJUWJPL2OkFEvjYZ1GGxN7jRc6nTzLQgLPQMKmcAhBJZlF7cy5ngNCwioZhv_wRrIqcoMsGJDCyeTj4WImkguKd1gUJjj8a7tNMTyfmpM63OZNyUxXZMDUy0R-OYznadF3snYEQqWazMMKGPkXxkpUhI8MOLmLmuiWgHI506XRCtjDiRmKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شاه پناهم بده...
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/448693" target="_blank">📅 16:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bb03071a.mp4?token=QmJJBOch42D7RRSUQtI_65MXNJ3v50Z3KZBAWJR2BiAMRnhRHyUXct0u0w-okDuJQe4uHWdfqeJajEiwtoeZ4GmhAer0Z_rihg1ZlorMaierafeil0P4NER-_5jbbNxr_FatH6aybwAZNNHLgm334w4D-z0Ca38w7ZDLHHx5_-GTXZA7wylIjFCBAGdmwPsunOITmn2LbB99sxxp6WwHpFF5pQGR33JIg1ivqpN6FHHZdtIxUWQlXIUq9lmbygDRLT2St4qVendB6AVZfwldsGCxTKhYZ6E6yXb-zblfzyRxJoeucL2CKgbJwPTu6MTE5Og7J3r9_Dll_ol_LQvmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bb03071a.mp4?token=QmJJBOch42D7RRSUQtI_65MXNJ3v50Z3KZBAWJR2BiAMRnhRHyUXct0u0w-okDuJQe4uHWdfqeJajEiwtoeZ4GmhAer0Z_rihg1ZlorMaierafeil0P4NER-_5jbbNxr_FatH6aybwAZNNHLgm334w4D-z0Ca38w7ZDLHHx5_-GTXZA7wylIjFCBAGdmwPsunOITmn2LbB99sxxp6WwHpFF5pQGR33JIg1ivqpN6FHHZdtIxUWQlXIUq9lmbygDRLT2St4qVendB6AVZfwldsGCxTKhYZ6E6yXb-zblfzyRxJoeucL2CKgbJwPTu6MTE5Og7J3r9_Dll_ol_LQvmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر پاکستانی: آقا را خیلی دوست دارم چون رهبر آزادگان عالم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/448692" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03205958f1.mp4?token=MflrulSSXJsWqLiBMUj2M-qVNLcYQ9KUnX4j_YhA5YHS7yWIWkuEEAlcdEXc1T_EMzbkzLqRnbMio4N-3oBpTN4LkDi4W_wnKnys7s3u64J2DAysxfWBpw6xPIALRvDmFcGrmTyNdp4CN_Flb7DBBoAtfDhx52V5ERjgzva_r4apSH1RQTRsjqFoCsxkdhpZXfvKG4HbqNPqXsBcAsoSmi1NxaRYkOYduXNZtVgQ1klPOV-_DhaWgM2jVE0aZzLmEelMzw0vfJbBjh2uiGm_Je5snZVl_1ac3OZmgWHyslbQtl0KAeFeO6AhIsueguTIBxUHe2hq4PC2mVYApzDiSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03205958f1.mp4?token=MflrulSSXJsWqLiBMUj2M-qVNLcYQ9KUnX4j_YhA5YHS7yWIWkuEEAlcdEXc1T_EMzbkzLqRnbMio4N-3oBpTN4LkDi4W_wnKnys7s3u64J2DAysxfWBpw6xPIALRvDmFcGrmTyNdp4CN_Flb7DBBoAtfDhx52V5ERjgzva_r4apSH1RQTRsjqFoCsxkdhpZXfvKG4HbqNPqXsBcAsoSmi1NxaRYkOYduXNZtVgQ1klPOV-_DhaWgM2jVE0aZzLmEelMzw0vfJbBjh2uiGm_Je5snZVl_1ac3OZmgWHyslbQtl0KAeFeO6AhIsueguTIBxUHe2hq4PC2mVYApzDiSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خروشان آخرین بدرقۀ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448691" target="_blank">📅 15:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl82yo_IwGVqcWu8rgHjlbsdG5pD0zAfanLn-0VkKvPOZjf8tFQHd4hqkGTtgAPQJJLHVqhk3-gSyV6xGw-oUJ_zYbtpavQ3rcfRyCKDQhSJMKJCkpvPxUxTzuDLX3eL6_lnvbc1sfBh_BYfeHaX1itHfQZ2b2kL3XEPZUaP033rpm5YIGVrRL-AkMNWXdsiLrswc7USDkeuIjYEZgasGxqVPEKXJe8NcpSoBhErx5ujxZN9zU2uNidfiSwYQaB3JJ7L_xzeNYhgPA0cqQDzazJg7jNDJBfYB5I1YLWRJswAKAPfbOLLiGFIOCbkORkx4ueDIVE1MKuKHBFuBeeBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام مهمی که امروز از مشهد مخابره شد
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448690" target="_blank">📅 15:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a27e5555.mp4?token=MI1jXUUGelEdBae3Fo7uNSrS4P774XWRivCNzwOMzG6YxccJ2utFd6uPcIkexJ4BYxQXZ54m0RFmytdK1SRvUPo-u8ixMl14JcjjYKhej4yUAV8ZdwHIeAP7RSIS0z1Y97RMm1WjMRpaURlT1elBiJTDd27gnAndmUyCzd148xdVmIeYZtcIGBFV5WusUn9WOaY1vh0r0h6eXPu5AaNDAfqSKSW5cj8TicTVYkZW6RGVtDp8oHrE61y5ughcavGqfbwXBdeVOpEZviNqUz-PG1V_RtWce1Q7XD5Tox2blZiIF9sP7oevkP-FZbweYKnQ7_Mi0Ly_--B9hadBctPlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a27e5555.mp4?token=MI1jXUUGelEdBae3Fo7uNSrS4P774XWRivCNzwOMzG6YxccJ2utFd6uPcIkexJ4BYxQXZ54m0RFmytdK1SRvUPo-u8ixMl14JcjjYKhej4yUAV8ZdwHIeAP7RSIS0z1Y97RMm1WjMRpaURlT1elBiJTDd27gnAndmUyCzd148xdVmIeYZtcIGBFV5WusUn9WOaY1vh0r0h6eXPu5AaNDAfqSKSW5cj8TicTVYkZW6RGVtDp8oHrE61y5ughcavGqfbwXBdeVOpEZviNqUz-PG1V_RtWce1Q7XD5Tox2blZiIF9sP7oevkP-FZbweYKnQ7_Mi0Ly_--B9hadBctPlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک و حماسه، زیر سایۀ خورشید
نوای روضه حضرت رقیه(س) در تشییع رهبر شهید در مشهد طنین‌انداز شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/448689" target="_blank">📅 15:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U67bB6klBHWCR38uwakG9ubWHMqep-GfAKsAQrbsguXvSn3h7M7KJEVrToeEkGzz0OLwM8OgPo3Kwto5N69owy9Tum3keuXaEAVu7NJlmDJikAwxrm706JmJwJhDO569HrrHzDHfVE8M3NOUcTWzYjWLRlFLwDVOxXn6s2mEybJ9no529CXZuVeHTzYUDZbz9hRah2Gjt5WycJcO4Pheo1_FT81vNbGsPkDYG-o8kbWJdidJvHRIYzCMmjso_B1hZHu3VczenRL4rZaK40PMxq0A7OVfujRZfHo7yWH6C13zUDidpE7BXTER3_2LmzExmrSQeYhVXbC7YK7o1FVunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قاب ماندگار از تشییع رهبر شهید در مشهد  @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/448688" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7626a8268.mp4?token=ThHhso-VM2210D2IhVfr-Vevfp2wufnF3WQ7wf9RMHmeYM6q_rlT6YQrTpqG0VODAcrcuox6gFhLVAyiGJZird62n2RlPRFjKAl3xu7Yu5ZxOfzckp6A7XBHIW2SQHHk-h6XKyihQuv3rDZqd3Yg1_Kw2g86ovzwqag10VM_EphARZcqlWNmB9-jTpq4Yb4sIgO3PyqpYNETFeZZVbpzvIV6jPffi1T4WpS6qt4ZF6DTZ3HAG2wV0XcLFN3w7LE1Et1Vt37-DKwSPXIMP7dgP1UZv2Wvlot27CIPBVjV-9J3wNIU9P69x6zvbnudn9WcKvHmXlMMRDZ15cwpun2ozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7626a8268.mp4?token=ThHhso-VM2210D2IhVfr-Vevfp2wufnF3WQ7wf9RMHmeYM6q_rlT6YQrTpqG0VODAcrcuox6gFhLVAyiGJZird62n2RlPRFjKAl3xu7Yu5ZxOfzckp6A7XBHIW2SQHHk-h6XKyihQuv3rDZqd3Yg1_Kw2g86ovzwqag10VM_EphARZcqlWNmB9-jTpq4Yb4sIgO3PyqpYNETFeZZVbpzvIV6jPffi1T4WpS6qt4ZF6DTZ3HAG2wV0XcLFN3w7LE1Et1Vt37-DKwSPXIMP7dgP1UZv2Wvlot27CIPBVjV-9J3wNIU9P69x6zvbnudn9WcKvHmXlMMRDZ15cwpun2ozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مشهدی‌ها: ارتشی، سپاهی، انتقام انتقام
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/448687" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=cIO2_tD6HWcXiP9lzMRzJN7Txe1WxqAbYrIUuOvARzvhsq6U20RVUxysV36rjsrijdxQtymR7BWGK_lFnPjLbwZ15Pq7u5p6N3K2Ptes9Yts9d5r18BOZNgr5I96DYXHD9Lug3UyNoAvpCmneAdThO3zDXf13Rf2Z55b0M0P1xfU02lVNUCcBKzLyM_mkUiEIu69jJhSaeOn0G0QPa9gOgFG_8zQVb_ZekyaPRyjKhKAVgcJ2IazDq_1qtj0eFTNOTfepRCPeCSOc7H0ypnRSY7uflOU8jtRixLmHzN3dzZ9LovMoCHKPztK5d1NehAOHhdNWPwtxZgHMjbS8YEyAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=cIO2_tD6HWcXiP9lzMRzJN7Txe1WxqAbYrIUuOvARzvhsq6U20RVUxysV36rjsrijdxQtymR7BWGK_lFnPjLbwZ15Pq7u5p6N3K2Ptes9Yts9d5r18BOZNgr5I96DYXHD9Lug3UyNoAvpCmneAdThO3zDXf13Rf2Z55b0M0P1xfU02lVNUCcBKzLyM_mkUiEIu69jJhSaeOn0G0QPa9gOgFG_8zQVb_ZekyaPRyjKhKAVgcJ2IazDq_1qtj0eFTNOTfepRCPeCSOc7H0ypnRSY7uflOU8jtRixLmHzN3dzZ9LovMoCHKPztK5d1NehAOHhdNWPwtxZgHMjbS8YEyAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب ماندگار از تشییع رهبر شهید در مشهد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448686" target="_blank">📅 15:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cb84d9de.mp4?token=LvqZGgI6tlKtsW5aWaftDHNIaM838CzmrROUJZP_rqGp6p_rHXLLHmyL9I1VsnS7n5xCv0LHyx5Ekb9WQKNYYWhLf9BlvPs9rhr4cKxUXjhRB1px-S57XCMnKYIwK-G2R-yW04aI27yJfNE1DptlixTFA9TXcjElpLM3R4f-p7ZR1SLb_pKzg0wQltvaB1P0C1yX05QlICU-7CjZxj2EFB98necgkl_YpPDOJ10eBNc107bGyrCYtqwv3g8JvDBNKtJV8jr8-fh7wnLfsuirjkoNxhNz0_P51z5J_AbBQDUKKwVVaAmidRFVhePeITCs9U32KE8hglcgOtrPSc7d9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cb84d9de.mp4?token=LvqZGgI6tlKtsW5aWaftDHNIaM838CzmrROUJZP_rqGp6p_rHXLLHmyL9I1VsnS7n5xCv0LHyx5Ekb9WQKNYYWhLf9BlvPs9rhr4cKxUXjhRB1px-S57XCMnKYIwK-G2R-yW04aI27yJfNE1DptlixTFA9TXcjElpLM3R4f-p7ZR1SLb_pKzg0wQltvaB1P0C1yX05QlICU-7CjZxj2EFB98necgkl_YpPDOJ10eBNc107bGyrCYtqwv3g8JvDBNKtJV8jr8-fh7wnLfsuirjkoNxhNz0_P51z5J_AbBQDUKKwVVaAmidRFVhePeITCs9U32KE8hglcgOtrPSc7d9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبی که شهادت رهبر انقلاب عراقی‌ها را تکان داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448685" target="_blank">📅 15:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b17be43a7.mp4?token=tlXUzqMOixo06XrSkiVnMHF2PSWJDYbYN_c_9vUTUggzxc2Y4DXujv97AoUP6pqWitZ-gW_U5elWr3FiJA5CqFLm6vr-1KHOxxtEX9HagSuF3E1h_A72hLd6dBw-BbkatBTb5D9tVxJG6gN9ANOC28womvpAQinvQnh1RcqDOBcAn0DymXYnzym51yRXhxxsMnZ0eWqN85VDM_I6mURr0VC7bE3keLGr4AxdXABtxDEuIpD2DQh8ppPglGld2wbiu9eNQTG98K-9J9BUpIN0cek4dmR2KBKxLVue9xMbMTorhuxokIzNkweYMnBxCTxXFAZHs94lG56kwnEGYZpL5wqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b17be43a7.mp4?token=tlXUzqMOixo06XrSkiVnMHF2PSWJDYbYN_c_9vUTUggzxc2Y4DXujv97AoUP6pqWitZ-gW_U5elWr3FiJA5CqFLm6vr-1KHOxxtEX9HagSuF3E1h_A72hLd6dBw-BbkatBTb5D9tVxJG6gN9ANOC28womvpAQinvQnh1RcqDOBcAn0DymXYnzym51yRXhxxsMnZ0eWqN85VDM_I6mURr0VC7bE3keLGr4AxdXABtxDEuIpD2DQh8ppPglGld2wbiu9eNQTG98K-9J9BUpIN0cek4dmR2KBKxLVue9xMbMTorhuxokIzNkweYMnBxCTxXFAZHs94lG56kwnEGYZpL5wqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد مینابی ۲۵ شهید داده، اما خود را برای خون‌خواهی رهبرش به مشهد رساند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448684" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محل خاک‌سپاری رهبر شهید در نزدیکی روضۀ منوره است
🔹
رئیس اداره اطلاع‌رسانی و رسانۀ حرم رضوی: پیکر مطهر رهبر شهید و خانوادۀ ایشان پس از آیین تشییع و اقامه نماز به یکی از رواق‌های نزدیک به روضه منوره منتقل خواهد شد و مراسم تدفین در آن مکان با حضور خانواده و بیت رهبر شهید انقلاب انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448683" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a81c3bb0a.mp4?token=d21_OzxmnBU5nUKhgPHJkDhUe9LCVR_b8sUJtKgiYHZRaVCs30efVm7JZlPtSt-8Il6gbSjVP16dieo9_jb6Ra84-QS8LnBlSXUlWn1DV42uuKPqOZMfR_RNxEQFCca6pVwFBH4NgmNtxLtBFsTDwc4OtFfn0-GFYgWfDWgBmcPyQ_XEw6XJAmi_-X8rEgT_3xINVeS0ePW82qMHFPRP5o-hXwTqLZZePI_CuvIzKxTWiQvrY30AZTLdS1nvnsLFhSJsd_HYVpC9TxLpDiQEc3cOhzMUW9KLW1XCbFUR--V7pjh9FcEFwvrha4vffeOwQhbM9uJIQjnql9dMMRPYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a81c3bb0a.mp4?token=d21_OzxmnBU5nUKhgPHJkDhUe9LCVR_b8sUJtKgiYHZRaVCs30efVm7JZlPtSt-8Il6gbSjVP16dieo9_jb6Ra84-QS8LnBlSXUlWn1DV42uuKPqOZMfR_RNxEQFCca6pVwFBH4NgmNtxLtBFsTDwc4OtFfn0-GFYgWfDWgBmcPyQ_XEw6XJAmi_-X8rEgT_3xINVeS0ePW82qMHFPRP5o-hXwTqLZZePI_CuvIzKxTWiQvrY30AZTLdS1nvnsLFhSJsd_HYVpC9TxLpDiQEc3cOhzMUW9KLW1XCbFUR--V7pjh9FcEFwvrha4vffeOwQhbM9uJIQjnql9dMMRPYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «یالثارات الحسین علیه‌السلام» ملت غیور ایران در لحظات ابتدایی تشییع پیکر مطهر «آقای شهید ایران» در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448682" target="_blank">📅 15:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd499f35e.mp4?token=JykKbxkhXPdHgAehuUPHn2T2mXurO2HwJc0xXJOB079Yhly1f2hD0cBHyslUdF9VhEVVhFM4--azrg1MUndDaqiDOC9KqzdJGUShivrAvwGhwzYgU20Dw9hb59PtCCOsdHglY2fYCSY6b3y6NwlIJio7Wewc41X6ShMw9ceiZFF8HSLyolrUcUJ_xlG2S6stXmoETSeVV6XQg_ykkQ7zpkziZgy29w6kdd8W0Au7bb08dAxwz0IH9fWUG35wKAizVzYd7GHFt0gJJtR-Drdvc5IM1pMe7oHeIr-EOsAuAl0tS9jsl-EOeerOJ1fctBdEWpvN4fSr2EnJCSiVSn0mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd499f35e.mp4?token=JykKbxkhXPdHgAehuUPHn2T2mXurO2HwJc0xXJOB079Yhly1f2hD0cBHyslUdF9VhEVVhFM4--azrg1MUndDaqiDOC9KqzdJGUShivrAvwGhwzYgU20Dw9hb59PtCCOsdHglY2fYCSY6b3y6NwlIJio7Wewc41X6ShMw9ceiZFF8HSLyolrUcUJ_xlG2S6stXmoETSeVV6XQg_ykkQ7zpkziZgy29w6kdd8W0Au7bb08dAxwz0IH9fWUG35wKAizVzYd7GHFt0gJJtR-Drdvc5IM1pMe7oHeIr-EOsAuAl0tS9jsl-EOeerOJ1fctBdEWpvN4fSr2EnJCSiVSn0mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی و میثم مطیعی در کنار پیکر مطهر رهبر شهید در پرواز تهران به نجف
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448679" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpstmxf_33KnIGM2zN5B3101zzjcMOSKdexMwMKbFFgY2PY74D8I9xiTVd7AWlRxFV0y2Tp9Q8As-I9-IxywbMGhwdxsvdwFzpyWs1QAGN2oJl3YzrytiRmsW84j6H0wbbBLCeO44-E47bmpQVzgn4IhIpvKl72pgbfq0XI-KTyWvNgbjogOQBxbGdufXyP8oK3xHCyg5OiHy-mCO4Vl4MUz2BM-2AgOfuFSu0y0GXHnyq7oOMnqVo6sJX2ERGGfSfmPD0MZPNYtLqZ0GPgitvnpu6eJoUO5-zsaedtrAh1dMnINFls-6k_G9r31tY0bA9jiPtxw9y2XAPG5oSnc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: ماجراجویی‌های ارتش تروریستی آمریکا پاسخ کوبنده ما را به دنبال خواهد داشت و روند بازگشایی تنگه هرمز را با اختلال مواجه می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448678" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNbaWJ2OlaB7PpCuADTNZqFskKBXz6SofW5kagqEiAU6-wjXrqQ0cGcAk4qboAdWyUtleqnhvpFeyQHShubdT3zYymajTq8Y9DNQ-JveV3g5Y2OzB_W9Y9HRjDXiaiGfIN35XhyVq9XgQY6fkvAiTszXuv_N2MgNB6v6UL_NNhCMKdW80S2BJH5r7DMpmvL08CRE748Gjx7x-8G2lu1g8sNiXnxkCn-pBf1qhiX1Zyj0Eq7oOj6Y8GL0F38CQH4KiTNFXX7BpfMN6g71bEJKIPWtYEdiZQngd5LROzy-cxa0_l3z_6fmdosovyxDazoWHVdgtsLkIp6UMtoc3zTpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی از نیروهای مرزبانی هرمزگان در حملۀ آمریکا
🔹
ستوان‌سوم حمید زارعی حاجی‌آبادی، از نیروهای مرزبانی استان هرمزگان، ساعت ۰۱:۳۰ بامداد روز هفدهم تیرماه، در جریان حملات هوایی رژیم صهیونیستی و آمریکا در محدوده بندرکوهستک، هنگام انجام مأموریت به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448677" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgILGxcQIOeH75eAe97sNdSx7OLEgwg5F0hovV61Z0DlyB0ffNA0lmkumY7HXFr04e1nSiQxaEf57a35_GM5L-FNj9WTBUihUcasTXGd-v-q3F8j8_EJeaoIORsiDGvjLfDNb5OvVGxc1OT3QS1Ow7AZQqL-VvzZ2K_I0cX3WLbvti6EUC6VUQGEu45LMVnM71thHwIAGBJGtx3sqPPbfGdIF24psDh-qWv2bImN3KTIC3UbjQGwS4RrFWHZb5OW36Gb7PYfEpRSJvYGAu-zu0U377RH-OnA_yxVSXGJKNEBERkv2iFT56BbQMCFRkOIZMPD-cfHds3-Iqlbz2tZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای چند انفجار در چغادک بوشهر
🔹
دقایقی پیش مردم شهر چغادک استان بوشهر صدای چند انفجار شنیدند. هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔸
ساعتی پیش هم مردم بخش‌هایی از بوشهر از شنیدن صدای انفجار خبر داده بودند. همچنین صبح امروز…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448676" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی یک جنگنده F-16 نیروی هوایی یونان پس از فرود اضطراری در فرودگاه زاکینتوس
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448675" target="_blank">📅 15:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظم ایرانی در تنگۀ هرمز همچنان برقرار است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448674" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی مردم عزادار با مشت‌های گره‌کرده در مسیر تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
الجزیره: آژیرهای خطر در چندین منطقه اردن فعال شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448672" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عراقی: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448671" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448670" target="_blank">📅 14:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در مشهد؛ خیابان‌های امام‌رضا (ع) سرخ‌پوش شد
🔹
خیابان‌های منتهی به حرم مطهر رضوی مملو از جمعیتی است که از ساعات پیش برای تشییع پیکرهای مطهر شهیدان حضور یافته‌اند.
🔹
مردم با سر دادن شعار «لبیک یا حسین» و برافراشتن پرچم‌های سرخ خون‌خواهی، خیابان…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448668" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a84aaabb.mp4?token=tL-C4Jjr-QjLiN0RXzL8gZPbMMicHkjTIyJBB_9FRcAJomOAkDv_ZdCsilxVRjUGiGRKiyY0Tmu3Z_kO6thnx_zZmCYcy_fzpUHDcvDJ_PA5gcSpX5p_cnW-dUc-oO5T1J6n9DZjsbPgL4u_tSnyPUiJ46tfO2oMZLf_3AKEijmaojuhfiSoRWhfu5c2w7g0YdgCD82A6h91qAQXuGF5kbOXzwtBYniZYLCjyjQLaq91ajL6WVq5lLQwYphzoea73Yz5vHXYJoIX7ZWfoJRniisset_Y5Fs0tOUqF2Zln8HKV4bJtJoxTtiuYy1xhayQwTa9BAJv0GOEJ0Ye877HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a84aaabb.mp4?token=tL-C4Jjr-QjLiN0RXzL8gZPbMMicHkjTIyJBB_9FRcAJomOAkDv_ZdCsilxVRjUGiGRKiyY0Tmu3Z_kO6thnx_zZmCYcy_fzpUHDcvDJ_PA5gcSpX5p_cnW-dUc-oO5T1J6n9DZjsbPgL4u_tSnyPUiJ46tfO2oMZLf_3AKEijmaojuhfiSoRWhfu5c2w7g0YdgCD82A6h91qAQXuGF5kbOXzwtBYniZYLCjyjQLaq91ajL6WVq5lLQwYphzoea73Yz5vHXYJoIX7ZWfoJRniisset_Y5Fs0tOUqF2Zln8HKV4bJtJoxTtiuYy1xhayQwTa9BAJv0GOEJ0Ye877HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در مشهد؛ خیابان‌های امام‌رضا (ع) سرخ‌پوش شد
🔹
خیابان‌های منتهی به حرم مطهر رضوی مملو از جمعیتی است که از ساعات پیش برای تشییع پیکرهای مطهر شهیدان حضور یافته‌اند.
🔹
مردم با سر دادن شعار «لبیک یا حسین» و برافراشتن پرچم‌های سرخ خون‌خواهی، خیابان را کاملاً قرمز کرده‌اند و مطالبه اصلی آنان، خون‌خواهی رهبر شهید است.
🔹
هنوز خودروی حامل پیکرهای مطهر به خیابان نرسیده و به نظر می‌رسد رسیدن به حرم مطهر رضوی زمان‌بر باشد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448667" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448666">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اقامۀ نماز بر پیکر آقای شهید ایران در صحن پیامبر حرم امام رضا (ع)
🔹
قابل توجه زائرین و شرکت‌کنندگان در مراسم تشییع و تدفین رهبر شهید، پس از تشییع پیکر رهبر شهید انقلاب اسلامی در مسیر خیابان امام رضا (ع)، نماز بر پیکر مطهر شهدا در صحن پیامبر اعظم (ص) و سایر اماکن حرم مطهر رضوی اقامه می‌شود.
🔹
با توجه به تکمیل ظرفیت حرم مطهر، اتصال به نماز از خیابان‌های شیرازی، نواب صفوی و طبرسی برقرار می‌شود.
🔹
از زائران عزیز تقاضا می‌شود از تشرف به حرم مطهر از ورودی های باب‌الرضا (ع) و باب‌الجواد (ع) خودداری فرمایند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448666" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448665">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
الجزیره: آژیرهای خطر در چندین منطقه اردن فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448665" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448664">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981b2eee7a.mp4?token=Vsu8pLR387bw2X4WNxUlt_bucLhXHYCZHEUoGKZLUq1Zf0qsVG5E2DUK-X1k8S3kqQaIPQNrJg7bE0Hp2Hie7764hnMwc4geteBUaIwuI-LNnbC_jEmZKM039PZk3B1_z1FVRATEQ5lzzmdfqepD9R6HsD2Hx58RhYGnqXNTTJ98LYMxs2ojkqd0Cn1gUUrhD_8w-RBPEyALDC-dXqkqMjrucVr4Hs4ZubFv8DR9Fm0C3i6nBzsFWf5lCVTqnuXDHJNpw-ubY1q-VYZzsrJclcDOGnK2adT7Bmp_8XMoLIO6e0rQwn_L1mph2-mVX6r0FiBL3BtuE5HMTMJgWTXtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981b2eee7a.mp4?token=Vsu8pLR387bw2X4WNxUlt_bucLhXHYCZHEUoGKZLUq1Zf0qsVG5E2DUK-X1k8S3kqQaIPQNrJg7bE0Hp2Hie7764hnMwc4geteBUaIwuI-LNnbC_jEmZKM039PZk3B1_z1FVRATEQ5lzzmdfqepD9R6HsD2Hx58RhYGnqXNTTJ98LYMxs2ojkqd0Cn1gUUrhD_8w-RBPEyALDC-dXqkqMjrucVr4Hs4ZubFv8DR9Fm0C3i6nBzsFWf5lCVTqnuXDHJNpw-ubY1q-VYZzsrJclcDOGnK2adT7Bmp_8XMoLIO6e0rQwn_L1mph2-mVX6r0FiBL3BtuE5HMTMJgWTXtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از خروش سرخ مشهد در انتظار تشییع پیکر امام شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448664" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448663">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تکذیب غیبت ناطق نوری در مراسم نماز بر پیکر رهبر شهید
🔹
در پی انتشار برخی شایعات درباره عدم حضور حجت‌الاسلام علی‌اکبر ناطق نوری در مراسم تاریخی
نماز بر پیکر مطهر رهبر شهید ایران
، پیگیری‌ها نشان می‌دهد وی در این مراسم حضور داشته است.
🔹
براساس اطلاعات به‌دست‌آمده، ناطق نوری صبح روز یکشنبه در مراسم نماز بر پیکر رهبر شهید و اعضای خانواده ایشان شرکت کرده، اما در صفوف نخست حضور نداشته است.
🔹
حجت‌الاسلام علی‌اکبر ناطق نوری از چهره‌های سیاسی کشور است که ریاست مجلس شورای اسلامی در دهه ۷۰، وزارت کشور در دهه ۶۰ و ریاست دفتر بازرسی دفتر رهبر انقلاب را در سوابق خود دارد.
🔸
نماز تاریخی بر پیکر رهبر شهید انقلاب اسلامی ۱۴ تیرماه با حضور میلیونی مردم در مصلای تهران و خیابان‌های اطراف آن برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448663" target="_blank">📅 14:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh4K3MyggoebN_Pnz91DJkJN2nAdfyhTUvClempzSHgSQOYmMFY73ea1Efd7oAsVAN8LRRcSDc5azWX-AgZFp8ILPHoKCbpshEYA2ntazkOtqVsxUsNAvcRqSOZKwzO12IeyfvHXTYoPz9t--R-N9w2vhdCwB5xMKEVbVf2DUY1me3190upJseU2Anx6u8B8QUIrgwyEPR8CJQ0M2YGSWXPiblWs4USdsXCRyCWzVQj8sgXnZwMtI_0ii_JIUAtOTn_9Hm11OmTjYQogCrExO_JLwaVHmFimf531k28ny08eINjN3KqIg-iX90EY3bVhvdNOf7fmnCQwiRs5JEf3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظاتی از تشرف سحرگاهی علمدار شهید انقلاب اسلامی به حرم حضرت عباس علیه‌السلام.   @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448662" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadca97172.mp4?token=nonKsQzTFRpsNomVzb-HLwvDegQmOAHbwnx8EpEVZHoPTg2wbq867qNA4fXK9BN_ZShAM7Tdo6GwEQYyBE4tNfQSLXTnDjxKCvvAPD6OS3Gzas-X41IJ2_lzIl9Lbl__yQ-oYYB9YW9DQOlz34zA2_DXQPr4-kDD2Bjjv86UTD3g1fpENnF7Rt6ZWJ_4ZAGuDHMo1jD2M5ie00phnltcq20xU133CjYdHopo0s-3hyH5u8rtI0ea83iIPJ89EvqHbvlh2DkrFjxTF8_k63cJf4_Tc8kB0RsnKaVhxg0nSbtoIfJsd0D0UWEVgfAFOEoVor6zYGG6LGsfSO_bb0zong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadca97172.mp4?token=nonKsQzTFRpsNomVzb-HLwvDegQmOAHbwnx8EpEVZHoPTg2wbq867qNA4fXK9BN_ZShAM7Tdo6GwEQYyBE4tNfQSLXTnDjxKCvvAPD6OS3Gzas-X41IJ2_lzIl9Lbl__yQ-oYYB9YW9DQOlz34zA2_DXQPr4-kDD2Bjjv86UTD3g1fpENnF7Rt6ZWJ_4ZAGuDHMo1jD2M5ie00phnltcq20xU133CjYdHopo0s-3hyH5u8rtI0ea83iIPJ89EvqHbvlh2DkrFjxTF8_k63cJf4_Tc8kB0RsnKaVhxg0nSbtoIfJsd0D0UWEVgfAFOEoVor6zYGG6LGsfSO_bb0zong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸ قهرمان ارتش به شهادت رسیدند
🔹
روابط عمومی ارتش: به دنبال تجاوز جنایتکارانه ارتش تروریستی آمریکا به مناطقی از جنوب ایران اسلامی در بامداد امروز، ۸ نفر از دلاورمردان  نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در بندرعباس و بوشهر، حین دفاع از میهن اسلامی،…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448661" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448660">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=GKcBjC_AKnsF_cWmID-KGb-1QHiIdNXH2FlXEtifKFh9sOSiw-uplGJQZBX1s5VSr21QXpAgzoczQDmhYcUWfKVgmP3MG_fnZ9Io1c46wAgojtsD046PUQ3y_iaUxaFHfMDVVAcv5l3X58tK7XZuDtWtKxERqaQVEM_41md9VsHCj0YxCyww-xQ0fl9FzRe8sqyLTh2EZs27i7jYpUpD0yc9Ec2b6iKatWXv0n16y4gsIKgUGBEnqa8jCpb7WmuT1rfmBePwK0yz_9Ftcm10q7LqF_k6jKLm-zgL_8pHueNoQqW8xezZuwYB5SgvI4f3vihHnOGBhEnGARFVwbXFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=GKcBjC_AKnsF_cWmID-KGb-1QHiIdNXH2FlXEtifKFh9sOSiw-uplGJQZBX1s5VSr21QXpAgzoczQDmhYcUWfKVgmP3MG_fnZ9Io1c46wAgojtsD046PUQ3y_iaUxaFHfMDVVAcv5l3X58tK7XZuDtWtKxERqaQVEM_41md9VsHCj0YxCyww-xQ0fl9FzRe8sqyLTh2EZs27i7jYpUpD0yc9Ec2b6iKatWXv0n16y4gsIKgUGBEnqa8jCpb7WmuT1rfmBePwK0yz_9Ftcm10q7LqF_k6jKLm-zgL_8pHueNoQqW8xezZuwYB5SgvI4f3vihHnOGBhEnGARFVwbXFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت الاسلام هاشم‌زروندی: از تمام کشور موکب‌ها برای خدمت به زائران در مشهد مستقر شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448660" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بخش‌هایی از بوشهر
🔹
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔹
صبح امروز هم دشمن آمریکایی نقاطی را در استان بوشهر هدف قرار داد.
🔹
همزمان اخباری در خصوص اصابت پرتابه‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448658" target="_blank">📅 13:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f21f58acd.mp4?token=WNoTTHOT1uWZXLYNP_vD1h6qI9BgxHdEAA2DB8mNCx9B4vB5jR2jgjXqOqTM8lxLXOURAvOGZXiwmLjKqNxBGz8_dRteQmIz2CUqxnUoJp1EbkjeInj2bZo_A4q3Ec7uai-S9lPT-siVveASprp6CPpH-lP8VIuYJZxxqkbLB108xlWsmLu4h89YGXUhzC8v0zHNr5cCUHOs3av9CfoJ2Ipb8mJrRFTZuA8dQA60hmFoyVlEOAnyFsdcuhrkJJY27HZd0-RU4h-4vYq9WkjczDoaAzlJc5VHyp9dW0_wxkldY23ikNsncA4EKtgB0_uxHFFfotXqA9UEdv7AvyCG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f21f58acd.mp4?token=WNoTTHOT1uWZXLYNP_vD1h6qI9BgxHdEAA2DB8mNCx9B4vB5jR2jgjXqOqTM8lxLXOURAvOGZXiwmLjKqNxBGz8_dRteQmIz2CUqxnUoJp1EbkjeInj2bZo_A4q3Ec7uai-S9lPT-siVveASprp6CPpH-lP8VIuYJZxxqkbLB108xlWsmLu4h89YGXUhzC8v0zHNr5cCUHOs3av9CfoJ2Ipb8mJrRFTZuA8dQA60hmFoyVlEOAnyFsdcuhrkJJY27HZd0-RU4h-4vYq9WkjczDoaAzlJc5VHyp9dW0_wxkldY23ikNsncA4EKtgB0_uxHFFfotXqA9UEdv7AvyCG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میزبانی موکب‌های کنار حرم رضوی از عاشقان رهبر شهید
🔹
آستان قدس رضوی با برپایی و تجهیز موکب‌ها در مسیرهای مراسم تشییع، خدمت‌رسانی به زائران و عزاداران را از نخستین ساعات آغاز کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448657" target="_blank">📅 13:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=JdhgP4-XRTnPTpm3g1YqVnEQvk2LVX1gCRrTXXF9uqyZtYPhazcZl_QUbhauVoUZ68yhTRzwiIDqYgKIAOiQ25oBWpkhxDH08NYMgEYcOxXpGTVU1rJ9sflXpWecJCf6WTtBfsFORekxopH_KeHD58u6el_RJn8Y7jdJbQdKh73GXqrfI_v7usvIxvMZTvqAMcYVsPj3mDLGRtYnl3WfMaM3d_eisCH5DEfW3jbb0r5tW66kOu4iIdUiP9YwP3dFOJiQxgUu03m67HgzLjn_Z3oZo5V_zmTKK7uFJ20cWmFB4YhpJQp5E1dEAuvq2FtVJoEWyK8GDoHsNwGIt3jdnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=JdhgP4-XRTnPTpm3g1YqVnEQvk2LVX1gCRrTXXF9uqyZtYPhazcZl_QUbhauVoUZ68yhTRzwiIDqYgKIAOiQ25oBWpkhxDH08NYMgEYcOxXpGTVU1rJ9sflXpWecJCf6WTtBfsFORekxopH_KeHD58u6el_RJn8Y7jdJbQdKh73GXqrfI_v7usvIxvMZTvqAMcYVsPj3mDLGRtYnl3WfMaM3d_eisCH5DEfW3jbb0r5tW66kOu4iIdUiP9YwP3dFOJiQxgUu03m67HgzLjn_Z3oZo5V_zmTKK7uFJ20cWmFB4YhpJQp5E1dEAuvq2FtVJoEWyK8GDoHsNwGIt3jdnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کثیری، کارشناس برنامه پرچمدار: اگر پیکر رهبر شهید در سایر کشورهای همسایه مثل ترکیه و پاکستان یا هند هم تشییع می‌شد، آن‌جا هم شاهد جمعیت عظیمی ‌بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448656" target="_blank">📅 13:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448649">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FK1boMXCLYT_BgXgBa08la_t0H8dQQDAMJceAaKfHYX5DachXqBd_4jDAPDf7mnFtuSxbBeNA0cIv5H_wXresttUlzzL7jjOrN-va3ey-2AqDuV4EUBI-o2LC2-zKM16R8u8sEd_MCnQY_CFGnOb-zGymkWDVQLe29otthwP_8IOpNQgBM-V1abo-zcEvBs4nYkj43SXfFtMcfzUQWwsR0ZB_xV7ffuskONEgHlUsEwHMIHNGQKUFEOW5KFZ-YLHuF3zznVZIRn-caFCExiWj3ZM6TBp6YsRikLONTOt3-1AG7fYGrchc4k0aY1NbtpYjNXJxyOnmcLCATOS7adW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cspeP_z9-JBDl0ZKrMihZRNHTxZ6yzJ_S0fwi7dU0wpIncSBvftaqYxyikA1d3MnWxz89FykgnvQ0qfua4u_JB8meLovEBJFMIcWNiN059xogAd9OXRxHuiE5PstSEcRdmh2wU6uDZmn_9aQZtq70LInzYBueRZ28cBlaUMH_gDfDmqzA2f7nDjwMq2QXJsJMyEeE4pdLyxiqezGgNw3TTKa2iCNPoN-zFpehhCsj6OwfNLd6rFNxrJ6vwST6TMkpOnmpIVOrOvymRXB77eivBy2hP3I-Vjb-PJGaYtRaVtyA3OmPAM_irTsjAqKuwuGm7gG5JBlxqBI6Bt0kSJ6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vxfkzap4Ad6Y6eA-nNpSaWwI0dwI9nNQ-a-PfFCQRXO89PYxuLyMdrytsco4Yk0yjqq3RITN_TJdd8jENrkqPrrz1tsGl5iVBQ4qvNDCLK7C_XMOck8oInnw-I4YsvQQsTKOy2GxVaXsls5cEtcRLpsZd4b8vJ4Qkn8heIEyg0josmHiEXiIceQ3z1V05DDFajrCP-pVt-yDvVK9MmqQBCjAICpqbUAKKd8euM8q1RXei_CJtah9aO3sT6DTxgB-5UIDK36yxhH9J43VomnMMUTxJE2pkTIJrBxfQjgniV9zXFT58CQJsQ93qotFoJ6KdQ04pXEUGZyfxt0yLAyyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT2AZ78KtbtJ_cgBXGanrPiYOybwKJ74f0tQ9TNdacxHnUOpxLtaLaJMOssj_mO8UbsjOmYUvwcUxBHFSRYsKKfakMQjAkRCG7oQmMH-RVg8piBPKQFV3fZqEc_jzgg_-5z6v_QAwAlEGXiNuOadkyfURxN4m2M6dEjJfmM5-9PTioo8UL9IcUm0P6E-WQWGdmZHi-rQO-1IDeTPpwGjDWXhprjhXVCdYF5VqI_QCLMPLF60R-s30_sb0cmNOaq4MP-ReRRfRND2bBZiwZjtoFidmnUuO3dRmiKwG-s5Ygm5Ba3LNUfSPm4wfxkg0_KBUSZ7oN6nAYya5_WHudyoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fafyE5sZKGv1rZyIgwBL9SzqwphvRcV95EVccKGHARr9cuJmyInmNMX1GKc4Tc8m1IRj6hyLav5dvOj0Sgwr39FZ-m73Udn5IduyTvgdCX28Hi9EtmkuFmd5nVIjh9Fsdpj5t3VKRIcIWKXTRbOgVeBq_c-AbiLtPGMsM12f5ohB_Ej7dKZlAVlVNTPOBz8nvolTPZHRXNkQSJcpvyGTQm-U2vcyd-PNLFUKXUkOAMVd2rhSl_m9TU7lhK_6lTXX8mzq5YnW5fK6UGqVbqehdjAO1xN2JEJ-nYVfkUke9vQMSmajjj_gs8nQjWIwhOAd6UGhAVvjNqPCmbePyAaB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBYBpV6OkEzbHfHe2Lq25eQftA-WJYqefVyr2O427VvbojkHEnTvWAyp2X6xvNYRNFNJMvrxJ-nXiU9MgqQsjBUGR5cz8RbO7vCpH91BZ83b_8o9_apyXse7sM4I-z0FR5lJ1EH2CnoaWNfVeSkG2atsBGig8EBjVBWLdpGGqos2als-gN82eANML0WQS7k-DUYiAY03WuhsvuY47eGAslgaY4_DSkvuWVCVV8j2iH6MomvE_Cg4wAXB-S4JVpNAhKEph1iePrNLkrm3_tZnJHfZdbZjtD9R6P7fW9v4dq7JWeOf4o2q6_OjWJ2Eg9w25E0f6XS5EKolrfIQ9poQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvds9v9DGBeh0jatQ0cDj1XXZNde8REpNThbmUDEhZI2xJDVs4-Do7Dj_qnvTp0nJj7T3VyUTvd8fVXbE9SFXzH8ps-Qsju1fqZXUr8JcixddzwrBv43IRR8lvz87rk3EKC_7nE0Asw61ZpV8CMvn9cXjSBy1dEhnFAOX_4VAoml2jYolA27nIsf8S9-ewO9MXdsIYT-kvfcV9dWAbY5rtD0mSb5ua2NYCYR1LfvTjLKClIZgwkVe8y6vCMv6A4wZNvE6TRlh7OfsQkZm-RQNGrY3ipPTmzewRtAIh3T3wohZ3Ad2jHxjvDoPUlkumvb5xfNXm8C75aSTnxnUo-SaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خط‌ونشان مردمی برای ترامپ
🔹
در روزی که همه در انتظار تشییع پیکر رهبر شهید ایران در شهر مقدس مقدس هستند، شرکت‌کنندگان در این حماسه با حمل پلاکارد حاوی محکوم کردن جنایات رئیس‌جمهور جانی آمریکا نفرت و انزجار خود را مقابل مردم دنیا نشان دادند.
عکس:
غلامرضاشمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/448649" target="_blank">📅 13:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448648">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بخش‌هایی از بوشهر
🔹
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔹
صبح امروز هم دشمن آمریکایی نقاطی را در استان بوشهر هدف قرار داد.
🔹
همزمان اخباری در خصوص اصابت پرتابه‌های دشمن به نیروگاه اتمی بوشهر مخابره شد که فرماندار بوشهر آن را تکذیب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/448648" target="_blank">📅 13:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448647">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بیمه دانا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkw2dfkj8OYaY7PUaMb0QWE9axDS0aF6PnypuiSlO5zp87je5BiYdNODq6JdduJ1EZS4ucA3Kdq8Zgfi6ss5VZESGKyZmd1Dae9VgUd4aMTSOEQ6_oz2A4BaJ-IHp4o66pokzGEqfRrFWd9h8aVRfKIrLuxzC0UI10RRiY9yXH3upuez2OjNIqCSNQKoBwW2Q73Lz_xDstunge9MDttpN5u8n4jq4uqpbAdN4x925UQE3AOwtCShDEwZIdtty1JMzAw8-rJSEXrsjxC5MFJTdx-xID6hIA5D1RsH8TLnZGCDhzAIcTJHDTNUcIQQJD7LDiQcaGu26oAHzuJRxW4_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
حضور همکاران در ایام تشییع رهبر و آقای شهید ایران ؛
ارائه خدمات خسارت سیار بیمه دانا در سراسر کشور
🔺
همزمان با برگزاری آیین بدرقه، وداع و تشییع رهبر شهید انقلاب، شرکت بیمه دانا با هدف تسهیل خدمات‌رسانی به هموطنان و زائران، خودروهای خسارت سیار خود را در شهرها و مسیرهای منتهی به محل برگزاری مراسم مستقر نموده است.
🔺
به گزارش روابط‌عمومی بیمه دانا، خودروهای خسارت سیار شعب منتخب این شرکت در استان‌ها و شهرهای واقع در مسیر تردد زائران، به‌ویژه در مبادی ورودی و خروجی شهرها، مستقر شدند تا خدمات ارزیابی، تشکیل پرونده و رسیدگی به خسارت خودروها را در کوتاه‌ترین زمان ممکن به بیمه‌گذاران ارائه کنند.
🔺
این اقدام با هدف تسریع در فرآیند رسیدگی به خسارت‌ها، کاهش دغدغه هموطنان و تسهیل تردد زائران انجام می‌شود و بیمه دانا با بهره‌گیری از ظرفیت شعب و تیم‌های خسارت سیار خود، آمادگی کامل دارد تا در تمام ایام برگزاری مراسم، خدمات مورد نیاز بیمه‌گذاران را به‌صورت میدانی و در سریع‌ترین زمان ممکن ارائه دهد.
🏴
بدرقه آقای شهید ایران
#یالثارات_الحسین
(ع)
#باید_برخاست
☂️
بیمه دانا
📞
02182468
🔰
@dana24_insurance</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448647" target="_blank">📅 13:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448646">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فعالیت موکب سازمان منطقه آزاد ارس در مشهد مقدس
سازمان منطقه آزاد ارس طی این روزها با برپایی موکب در مشهد مقدس خدمات مختلف پذیرایی، اسکان و تکریم به زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید انقلاب ارائه می کند.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448646" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448645">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448645" target="_blank">📅 12:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448644">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ec02ec64.mp4?token=D7Cq5sIi4ZQ1NZTaGdOokOqfjd7p51-7YvvFnKKfAjbdYWfkzbOpbBP9o5qqWqs2GyAQRd_xCY3OrHdbVyPGESLPNA_LUY2ymQ2FT7oyF7CasAbQ6NwhMECMzh5vEvrXGPt23cJFjPTkIA5f-EPr4S8EyruD2DVtmhNbvWqtve2wl7UetH1uoquPk_P0XwYBMLkS2oDDoyjiNxZincMgc5A_81ViBs5J8VtXDHkSigwE1V1HqgoPd8IJXdWFHTVnJt6yevTPqI_Z60XpPhvObUFBquqB2DA6qVnrXcyxOs_QXhSdj2A7_ewfs7FRaWNFnzOmJv8TAu3F-F6Rh7bNug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ec02ec64.mp4?token=D7Cq5sIi4ZQ1NZTaGdOokOqfjd7p51-7YvvFnKKfAjbdYWfkzbOpbBP9o5qqWqs2GyAQRd_xCY3OrHdbVyPGESLPNA_LUY2ymQ2FT7oyF7CasAbQ6NwhMECMzh5vEvrXGPt23cJFjPTkIA5f-EPr4S8EyruD2DVtmhNbvWqtve2wl7UetH1uoquPk_P0XwYBMLkS2oDDoyjiNxZincMgc5A_81ViBs5J8VtXDHkSigwE1V1HqgoPd8IJXdWFHTVnJt6yevTPqI_Z60XpPhvObUFBquqB2DA6qVnrXcyxOs_QXhSdj2A7_ewfs7FRaWNFnzOmJv8TAu3F-F6Rh7bNug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448644" target="_blank">📅 12:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448643">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6f87502.mp4?token=TA8So-aDrRQQjd3cp91bi_ew9ZIYRbps3F67aI87NH-wz292Nhk1QIuhTyIH1InXwGU6Bi2Q_l7R_zkkRZnhM8duB45nA9kIaKCgY5LPykIu3E_QZ-y8JDevqBGPmgUzRPJIa024BPokgP05nDICmaCA4FoRzJuufg0rl3hYFKDZcC8LxwdCNokfD5-BgXGrMCQmbdMi4FLrrXdjiA0ZZ3tZa-1O7E9BvN9x6QRxITSmrdWIUkjKCOuUJpfotPvwE-VZPHNRgelZYDRBn4UVqdP4fTbW21yVXpApRrXh6oy0wVnKtFiz541rshc77Qr14d79hXPyv8TLECSQjvXRuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6f87502.mp4?token=TA8So-aDrRQQjd3cp91bi_ew9ZIYRbps3F67aI87NH-wz292Nhk1QIuhTyIH1InXwGU6Bi2Q_l7R_zkkRZnhM8duB45nA9kIaKCgY5LPykIu3E_QZ-y8JDevqBGPmgUzRPJIa024BPokgP05nDICmaCA4FoRzJuufg0rl3hYFKDZcC8LxwdCNokfD5-BgXGrMCQmbdMi4FLrrXdjiA0ZZ3tZa-1O7E9BvN9x6QRxITSmrdWIUkjKCOuUJpfotPvwE-VZPHNRgelZYDRBn4UVqdP4fTbW21yVXpApRrXh6oy0wVnKtFiz541rshc77Qr14d79hXPyv8TLECSQjvXRuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر پاکستانی: آقا فقط برای ایران نبود بلکه جهانی بود.  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448643" target="_blank">📅 12:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
سپاه نینوای گلستان: دشمن آمریکایی در بامداد امروز با موشک کروز نقاطی از پل آق‌تکه‌خان واقع در شهرستان آق‌قلا را هدف قرار داد.
🔹
این حمله هیچ‌گونه تلفات جانی در پی نداشته است. مردم عزیز آرامش خود را حفظ کرده و به شایعات توجه نکنند. @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448641" target="_blank">📅 12:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1320feb57c.mp4?token=p4cJtTOPQ9tzE7tkg54v7NG-BR9LxaW04GRJaoEQOybv4sNelvqbi0qnqjoU-QHJ3xKRx_yxFqWuSuH6EmKiDCbtrn0IpWB0K9fRa4GCvX7LfyC62_j0EuL7hlDYJNymGyjfazxjkgYw89RbLGwPqv6cOXJ5STRw06x6p0yY5QzOvbKPYMs2cFQwR7YOUhp32Fi2UHJz5apHN7awRrhrnfIolG29LaJBbKNKEaVO6LiYY6h0WDptfg7hDxAqV-SwtFfXgtG_O45LuWgnj-2kLB_Ff7rGUsK5twgBMGWc92C-0-4B0YCKhS2iT013yyD6Xgj9ja0IZApohKvhl55hKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1320feb57c.mp4?token=p4cJtTOPQ9tzE7tkg54v7NG-BR9LxaW04GRJaoEQOybv4sNelvqbi0qnqjoU-QHJ3xKRx_yxFqWuSuH6EmKiDCbtrn0IpWB0K9fRa4GCvX7LfyC62_j0EuL7hlDYJNymGyjfazxjkgYw89RbLGwPqv6cOXJ5STRw06x6p0yY5QzOvbKPYMs2cFQwR7YOUhp32Fi2UHJz5apHN7awRrhrnfIolG29LaJBbKNKEaVO6LiYY6h0WDptfg7hDxAqV-SwtFfXgtG_O45LuWgnj-2kLB_Ff7rGUsK5twgBMGWc92C-0-4B0YCKhS2iT013yyD6Xgj9ja0IZApohKvhl55hKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شیخ زکزاکی در مشهد برای مراسم تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/448640" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdd229a75.mp4?token=E7JBMpH42mK6htubiEVnrvkYPOu-qULazWLdbzJa4C-AYeJtomsPFcWPaYpkAj7ipZztYeLurRLq4sHetHPhGE2X9J0b5XiAsBCZPDAGtchih5HSBCLwjQ_GJa8941JMrfSkPyVX99N6ZaL0fJ2B5IZS1dC-gzPh7_sSY0f6uNz6WCJKDZdkr9SZCjuAFqn4Bsmy8tf9z8eIuSPNanpBOhK45qwjjBrqaa3O2KiVM8EI2GL8WqkmFftBksF6GXVXTwrLlXBdHNuQplEg--QU7rgBrDaimfJSHY1E4hF7jiIv96C23-6l-bm2SFfaB7g3e56_pUWIi0oehz5MoIJhVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdd229a75.mp4?token=E7JBMpH42mK6htubiEVnrvkYPOu-qULazWLdbzJa4C-AYeJtomsPFcWPaYpkAj7ipZztYeLurRLq4sHetHPhGE2X9J0b5XiAsBCZPDAGtchih5HSBCLwjQ_GJa8941JMrfSkPyVX99N6ZaL0fJ2B5IZS1dC-gzPh7_sSY0f6uNz6WCJKDZdkr9SZCjuAFqn4Bsmy8tf9z8eIuSPNanpBOhK45qwjjBrqaa3O2KiVM8EI2GL8WqkmFftBksF6GXVXTwrLlXBdHNuQplEg--QU7rgBrDaimfJSHY1E4hF7jiIv96C23-6l-bm2SFfaB7g3e56_pUWIi0oehz5MoIJhVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در انتظار آقای شهید ایران
🔹
حضور گستردۀ مردم عزادار امام شهید ایران اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع   @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/448639" target="_blank">📅 12:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194e21f6b5.mp4?token=DUUamg8qLatwkHfPC-8lvkLvdGMzrImg9c6UGoFbAAuzJ-WdehOZY9OXo-Zx5BKrcX0yJN0s0y9oE8fssNuW2FnDys4gY3eQeqTecBDSyc7XP3qq6Ab6L09-z47dIT-PV3p6zeNYeLsRO2kJYlNKXaHgFCZb6zpEasM1Nh8hHJpqzFReHNS5Uhkc-IiwD1bGBOdlT6PsEJvQPS0VYWp4X6CPAy6cbIzPV8tfwFxgf0gF1i7kSl7nIftfMRxJSzMbg4_wI2QWctxsGYfLeV578n-Bj3pQlpbLzzGF2fQSqY_rm1N7vDArPAsfdVy9nHdmVbdFpNjDX2onKf56WHZ6Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194e21f6b5.mp4?token=DUUamg8qLatwkHfPC-8lvkLvdGMzrImg9c6UGoFbAAuzJ-WdehOZY9OXo-Zx5BKrcX0yJN0s0y9oE8fssNuW2FnDys4gY3eQeqTecBDSyc7XP3qq6Ab6L09-z47dIT-PV3p6zeNYeLsRO2kJYlNKXaHgFCZb6zpEasM1Nh8hHJpqzFReHNS5Uhkc-IiwD1bGBOdlT6PsEJvQPS0VYWp4X6CPAy6cbIzPV8tfwFxgf0gF1i7kSl7nIftfMRxJSzMbg4_wI2QWctxsGYfLeV578n-Bj3pQlpbLzzGF2fQSqY_rm1N7vDArPAsfdVy9nHdmVbdFpNjDX2onKf56WHZ6Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ ورود هواپیمای حامل پیکر رهبر شهید انقلاب به مشهد و پایان آخرین سفر ایشان  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448638" target="_blank">📅 12:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5f17605e.mp4?token=ul-rrtbmzP9OXVz3ONfvsknkTbDmIosAYtGGwH7u4twBIpsTKydGIXs8UX-g668VkRq5eyf-3G35B7A1LSXojrt9GsHfs9-wAdI0KzNVPeRikszmP_r6cK8A2c1GgamKSDVV-tkKgX_t1OcvNfsGKRy6syYgfUgHSCk58n4MhMCNuSE-ApJUIQGIAbkUPieglQ9p4mwwIT9OsmwI9M2FLt78xUbSjU1bLHh674OLxukelR5m3srhqtPFlPB83kz5i8BOa6lsh8V2RwefkZluxEXBAHeWCyr4UwWYQZGEo2QA9Nl89b_jDJmX2l-6JwpM4yqHmtnko5O0_bu0r4A2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5f17605e.mp4?token=ul-rrtbmzP9OXVz3ONfvsknkTbDmIosAYtGGwH7u4twBIpsTKydGIXs8UX-g668VkRq5eyf-3G35B7A1LSXojrt9GsHfs9-wAdI0KzNVPeRikszmP_r6cK8A2c1GgamKSDVV-tkKgX_t1OcvNfsGKRy6syYgfUgHSCk58n4MhMCNuSE-ApJUIQGIAbkUPieglQ9p4mwwIT9OsmwI9M2FLt78xUbSjU1bLHh674OLxukelR5m3srhqtPFlPB83kz5i8BOa6lsh8V2RwefkZluxEXBAHeWCyr4UwWYQZGEo2QA9Nl89b_jDJmX2l-6JwpM4yqHmtnko5O0_bu0r4A2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در انتظار آقای شهید ایران
🔹
حضور گستردۀ مردم عزادار امام شهید ایران اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448637" target="_blank">📅 12:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkdlZiD25aJ75iigfvEJ7gc5tXp0JMfEOlIw3sY4AjtD58XJFw5yJvMw8UDKxtD0eNpXsI3brdnC7xT4VfTJPC5wGD2yYy_ZATCserRdLfc_1b3NgyVknHdHBJVzCGJd9-D1V2tVWiAoGhGRioIUU2OOMnZIljC7OltAgP1aN4VmXbwlOJhoracyRp-mMpkqf_JVakjJJifBawWaHLM0nFsUCzepzUY8_lCwz9iQKrA6VSlgJwl36jTWrktGbihnBefE3OkJwI2IA0fEdXgvfHeUg-9ll48Zthgh0HZojHeYLbR6YgJOIMSX9HfqPLaos4tbUNpOXzw5n_JkSjvdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس ختم رهبر شهید انقلاب از طرف رهبر انقلاب فردا در قم برگزار می‌شود
🔹
مجلس ختم امام شهید امت، از طرف آیت‌الله سیدمجتبی خامنه‌ای، فردا بعداز نماز مغرب و عشا در شبستان امام خمینی حرم حضرت معصومه (س) با سخنرانی حجت‌الاسلام سید علی خمینی برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/448636" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
انفجار در بحرین
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیک‌ترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448635" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تردد نفتکش‌ها در تنگۀ هرمز به صفر رسید
🔹
درحالی که در مدت اخیر پس از تفاهم اسلام‌آباد میانگین روزانه ۳۲ نفتکش از تنگۀ هرمز عبور می‌کرد، با نقض مکرر آتش‌بس از سوی آمریکا، بلومبرگ امروز پنجشنبه از تعلیق تقریبی همه عبور و مرور دریایی در این منطقه خبر می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448634" target="_blank">📅 11:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSEAoR-4l8D6GTgs3cBJWrzofziQatfGYT8-wmfg493fKqmjxTu8WqosnhMxjW-ZEF8tUnxQ_3UVo-kkvno-cPTtVROzoe1fhHJoL2KH5RNPN3KBvjRDxS4jKMCBaxjTgVp-Xlv5DtXicGDftiS6N63gOI4Hj3YoFhOsw5qi9IKmrQ--BkHd8GQNUCRiz48QdJBbWfFoVLJN1WQvzl_Z30Lmxn9dePnETxTdNkWi1gxzdzwBlRdrKXCZTnzd0uoY-xIjUvaSxAKCnn1ZV3d5Ma747wWB6BVBaUC9TR9eOWIUB7bAZmV9lrkGu3Ph1EwS498ZHtVbHvZyDc6LWZrrug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان در پیام‌هایی جداگانه به سران پاکستان، تاجیکستان، ارمنستان، گرجستان و رهبر ملی ترکمنستان، از حضور آنان در مراسم تشییع پیکر رهبر شهید انقلاب و ابراز همدردی با ملت ایران قدردانی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448633" target="_blank">📅 11:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d7c1b18d.mp4?token=E0rYpT9_6CVKfuyXk2XMprafvo_ljWjsum5BafdFxX5XzXq4F8qpzBqD-t_KzNv9-fZGDSPQTHJpwyL9vPHC7Stm0V8FT6xVzRQLZqATlSJwjAEa1mmb10qP5phRNa7UNj7eXhuppK8LV95HQS2tSBLkDnai897eryaQ9AkBCB-WldfVKAmRFg2bRLV77VIhF7BkQyBWE_s7DuvoGcLLl8hOm24eh7Nsgd8Uqa0JG8nugI1LrZUQPK4JIhYKuKQeKgciZADihcJ1aUD6a0mCzSN7x9Zmf2z3TgsQ5IUVD1pypEWM0MZ2jhPxtNBC3HSZbYhJWExXqOh2Q2IEq2Owtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d7c1b18d.mp4?token=E0rYpT9_6CVKfuyXk2XMprafvo_ljWjsum5BafdFxX5XzXq4F8qpzBqD-t_KzNv9-fZGDSPQTHJpwyL9vPHC7Stm0V8FT6xVzRQLZqATlSJwjAEa1mmb10qP5phRNa7UNj7eXhuppK8LV95HQS2tSBLkDnai897eryaQ9AkBCB-WldfVKAmRFg2bRLV77VIhF7BkQyBWE_s7DuvoGcLLl8hOm24eh7Nsgd8Uqa0JG8nugI1LrZUQPK4JIhYKuKQeKgciZADihcJ1aUD6a0mCzSN7x9Zmf2z3TgsQ5IUVD1pypEWM0MZ2jhPxtNBC3HSZbYhJWExXqOh2Q2IEq2Owtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ورود هواپیمای حامل پیکر رهبر شهید به مشهد
🔹
هواپیمای حامل پیکر مطهر رهبر شهید انقلاب و خانوادهٔ ایشان وارد فرودگاه شهید هاشمی‌نژاد مشهد شد.
🔹
براساس اعلام ستاد تشییع رهبر شهید، با توجه به استقبال کم‌نظیر مردم عراق از پیکر مطهر امام شهید، ورود پیکرهای مطهر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/448632" target="_blank">📅 11:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سفیر انگلیس به وزارت خارجه احضار شد
🔹
در پی تکرار اتهام‌های بی‌اساس مقام‌های انگلیسی دربارهٔ «تلاش ایران برای انجام اقدامات ضدامنیتی در انگلیس» سفیر این کشور به وزارت امور خارجه احضار شد و اعتراض جمهوری اسلامی ایران نسبت به رویکرد ناشایست دولت انگلیس در قبال ملت ایران، به او ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448631" target="_blank">📅 10:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسِدخارجی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdzYDHf-TdL0kSJ4g7ZzTyx3G2VD4p9VN_fyTp_rH1ufzS98KvURKTqOgucJquXvYoI7yegxir8W7IrKdWBMCza-fPEJRUUheIdJ73nhRdtiPVv8SZQCaeqcSbxhy16Kqs2DiFY8RZLOOXNWNtwrxmu6KDRMM6xcdXLZ4371XNtFDB3Sn8JJ67PukHcwbGH6Efe6Q_eFcLWeTGVTY9WVck9J9AST0AWFS-41OYjeJjZa93fioUqa1gOa-yjMzU-vrhAnmS2H5VtQ8bp62JyhYyHprHonoMflgoCNUr76qYIU2SL3UwMcOyYIvDtFWci-Bbf58deUivbYlpMwp9wvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی؛
خیلی از ما این روزها و روزهای آینده، بخشی از یک واقعه بزرگ تاریخی خواهیم بود.
«
به همین خاطر، برای ساخت یک مستند بزرگ و مردمی، به همکاری شما نیاز دارم.
»
از هر قشر، با هر نگاه و از هر کجای دنیا که هستید، می‌خواهم داستان و روایت خودتان را برای من بفرستید تا در کنار هم این تاریخ را ثبت کنیم. اگر خادم هستید، اگر میزبان، میهمان، مسافر و زائر هستید... یا حتی جامانده هستید...
📸
چه ویدئویی برای من بفرستید؟ هرچیزی که فکر میکنید!
🔻
اگر خواستید جلوی دوربین بیایید، اگر خواستید حرف بزنید، داستانتان را بگویید و از حس‌وحالتان در این روزها صحبت کنید. حتی اگر دوست داشتید باهاشون مصاحبه بگیرید. نیازی هم نیست حتما به پیکر مطهر شهدا نزدیک باشید.
🔻
ویدئوهایی که قبل‌تر هم گرفتید که مرتبط با مراسم‌های رهبر شهیدمون هست هم به کار می‌ایند. حتما بفرستید.
🔻
گاهی پشت‌صحنه‌ها و حاشیه‌ها از اصل جذاب‌تر می‌شوند.
🔻
فقط ویديو بفرستید. افقی فیلم‌برداری کنید (اگر قبلتر ویدئویی رو عمودی گرفتید هم مشکلی نداره بفرستید)
✉️
راه‌های ارسال ویدئوها:
سایت برای آپلود:
https://upload.sedkhareji.ir
تلگرام:
T.ME/SEDKHAREJIPM
اگر باز موردی یا سوالی بود بهم در
@SEDKHAREJIPM
پیام بدید
خاکم؛ سدخارجی
✔️</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448629" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPabHZ7Q64u_jg0TvhfxJ5_RIh7FdHQZrL0d1xOxRMrbuYtz6xv9AsLeSFlqfJvT6tQFYCp3Ix-Qo9VMHQOZFX-s-S0p_861BKOAFx8l26CaPZlkMgr0y6xrNlF6mdESieT072ji2oJE8Lw19cEivtgNOXzw-cJgmNmlaqdj_7451yB1zgrxZPGhh8ShomwFEvV822kWLdaiS0GBfxUwof77BQtv35i6alGJdYOvIX5-XAbH89aeX6PwC_e3eeg1Z5YmJvZ04BVNWE1qxf0N4xJ39zFyxBhcNu1FJFMfsqMiqyTDt6ebmfxNst5-9pEz5E2oXm_9ooKtxTlk1SkKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448628" target="_blank">📅 10:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448627" target="_blank">📅 10:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید در حال ترک فرودگاه نجف به مقصد مشهد  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448626" target="_blank">📅 10:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3efea6cc.mp4?token=iCrVlF_gxuKfg9UZGAiUNZmRTPyDIrb6ugwesACGV2Tdz_e8sItate-Xaukb7ZjIhDxmZpuBt2tsaGxZyt40ThjA1L08l4IONhXALnVlsRu9csQokAzh3Ap9SjKJGspAwS6L-ZFXhTed-ZRer_tG1CmP9ZixOhXh7oPwZygyqkJD6CYf9YKK2sNftCQTEon-WsVhBRtZqoF2B98_2FeXojLO2G7ne5BepooxzCDdXF6krcTfVeb4Na7_OfoVsjTV80ftYIuVGRvLdqpoWUb7vof_Rxr_x3JeWPIHUEhs_Tj7Znvb3K-MK6iYMSg4hF2tVIZf859zUpj5yZJvVze8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3efea6cc.mp4?token=iCrVlF_gxuKfg9UZGAiUNZmRTPyDIrb6ugwesACGV2Tdz_e8sItate-Xaukb7ZjIhDxmZpuBt2tsaGxZyt40ThjA1L08l4IONhXALnVlsRu9csQokAzh3Ap9SjKJGspAwS6L-ZFXhTed-ZRer_tG1CmP9ZixOhXh7oPwZygyqkJD6CYf9YKK2sNftCQTEon-WsVhBRtZqoF2B98_2FeXojLO2G7ne5BepooxzCDdXF6krcTfVeb4Na7_OfoVsjTV80ftYIuVGRvLdqpoWUb7vof_Rxr_x3JeWPIHUEhs_Tj7Znvb3K-MK6iYMSg4hF2tVIZf859zUpj5yZJvVze8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در مسیر منتهی به حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448624" target="_blank">📅 10:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
🔹
سپاه پاسداران: ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/448623" target="_blank">📅 09:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c1c4ac0e.mp4?token=hpZsBeMDqENSg2l9CbuekqdFBXCochs0xGpHcWIxyKuOhpptm4KORI2BhmKB_yfrp2ofM-_cZX5jJxuJqGOtG8ma5Qp863u7OTPLx2ti-yX-XV-h0lOJ5TcXPz5XSOLv24QV_VcaXr-TIwdg6i4wmMfpIsI5FESSUganARb8krjep9u9NhuaV3vWPpTpgSIUAT9t9112Ndn735kq3y_DXbFAzcQ6tE17w1Adx5Q-ec1rAE9Q-gjHzzh9r1pliGZjDk9uHhF5feJ38O4yip6qrIydmoxMx8ZjV7HVQM8pgolIqFw_0lTl-pkyJM5iWbPas8l_Un4CwHEkgZiG5uwwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c1c4ac0e.mp4?token=hpZsBeMDqENSg2l9CbuekqdFBXCochs0xGpHcWIxyKuOhpptm4KORI2BhmKB_yfrp2ofM-_cZX5jJxuJqGOtG8ma5Qp863u7OTPLx2ti-yX-XV-h0lOJ5TcXPz5XSOLv24QV_VcaXr-TIwdg6i4wmMfpIsI5FESSUganARb8krjep9u9NhuaV3vWPpTpgSIUAT9t9112Ndn735kq3y_DXbFAzcQ6tE17w1Adx5Q-ec1rAE9Q-gjHzzh9r1pliGZjDk9uHhF5feJ38O4yip6qrIydmoxMx8ZjV7HVQM8pgolIqFw_0lTl-pkyJM5iWbPas8l_Un4CwHEkgZiG5uwwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید در حال ترک فرودگاه نجف به مقصد مشهد
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/448622" target="_blank">📅 09:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3nkoHD8f3EgiBejcMG-HCagj5Yg3dvRfdVcGPqz3ofs3Dp_2n-VdNzsVVND60DuMVM0xlYrjnmmXD475BRJagjjM9z2RoHjKn4lbTvKj8dxondxoKZua9vu0Wf2eQFdLdEkBV_hCLW48eA0jvGSoV361fyYRFubtIw81anqGbdy2sxE1HQLVGcUV0Kc0BJuGeEClc2cjldXf-XOtJskT-wn2mbSyT-ICSZZeGNTQLhCcMLvuDVZ9FvgU3zl4UKKT1ZHyc5Ld7t2aBUhoMQl97_FCKjK5PeFsKZ1txvTxsNs_Sz8aN6HK3NyuVwLovPiGfHZbUz6HOKOmoq1LKbHmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gm3nVPmFnY8jpC9eM8WKaEIM5xuBuP5Es4STgTt9xePtD9lXvyVyb5YPE1pGoe99CE8qMKwlW-JOiZ4b4Y6GUzKimqdzpsuqqDUJzIermPce-O5X9Cf7m31HRqgdiFGRSOufzeHMnk-2PIacNbZGQYTBVXX8-Uw9p3SNrz8QGyUPQFdPyiLM273Oc1cqQUsbq_z1ysT0obDWFLJxD9S-0KHyTWvfSNJOG-vkBpPyHlDHwyxc18zJJ09XA-2GjpjgfmRcPAjJ7qkGxZzXtSTX7GJSi1UBSDy_fjOUYxbHJ7bw_Rm_7fcY2_1NK3nZO61FJOpRdF5_6Pdi5lU5nVpieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4UJhtUzs6hc4eNWdbuM34Z89Kdj3N0bnAcXJjJaZ3JV5o_ng9zOx-Vkp9B0IG9r1f-lYsti4jdYxZzNab2oy-QgKDw9z-2UYYXAgLwtk1yXhSC35ZF16N8K0OpAHWHXrTkV1yHpUoLssnJeCX7yNq0Y-cuokeMOseUXIi5_dhZwvQG_C-eirbX4_DBQ6QM47tAwAvnQL2j0WwrJalJVH1tocMhI-TEPpQBZ9uVQfKQ1luUBWqmUSX4r2J5YEhiq-tDpI3VxIujINE-3_irubsB61aVpSGWsug03_TlZiXW7Qkg8HlRP54P2MMV6lSWm15t_OkKwa9Axl2He6OdITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWnzUu4T7sY8vCxyzISdr72LnVk9MUpUUEKta3UdoWvvDEG7t0-7nispOC4VeFJ7Pn-t-MUV-sA4FL2tAYKyc7PP91FXM4Nr-5UjCumiGY03nnGbUDYeBtbD8MHgTMsYQkI73asxX6uN6ITOnsYhfjx0nzr1VfNxEiKzAvGJRJV-Bxv2BI43EzpCW_SfLEoiS7GRSkknzFFMLLKXU82o-PfbfZvor4ixOMN1c8ez0gfRNc5n_f3BMUuaIWa-QOam24qETbln5KEAKnuY3jDKOXo2MXYYZF3nMcT92ErBz6aXG3BYZ1SmmX6Wmsm3JP658_gJpjzOnhd7LjZY6GhnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qomeM4gLFtGfjTUmURjLrbmVm6UporMdZmaEuRE8CzZ_XalFDGKhMyodqqxOVAQbuTH7-ORsjeHBDHilcR4KeKm2LS2eoB4NSuzOXWu3dQ_k6M3sIJdXMsg8ESF46d22N55URzebES-Ki8Xg6R1uecL3AhqodSM56_Zvdl1uJyM41n1O_OzvPIHR_s8txQD_AyAZb2fvT7cpCRbN4Z8Te5Lz1sLItV2EBka9bTG1dFZt4UiYePTqZmmQ3QHXMmqoEmBKvYDGvAYhW27-I0gFLZ0gpJ7RBsB39J-iRIZ4S4bsFtzWzTU4sJjcVPf5rEszUZ1j5bhvr7Vul8NNM86vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXJMMZaC8S8ZubiEl3qPHmQbo_LYC5OHePXKhnVQvd0Myfucphl_z7mpT6uS4myfeY9rZGFWFXd6Dx9VXGdAZ-XdLusF7aNVLBl6J5y_qD4xPOTHwCbJXoLSw8J4vZrZphdMj9GOqZ95OdhfPm21jBRvsUyh7lweBG0RtYDKQmjQKMj678KS01KOHfgZ2JI5IH8XAYHK1ol2EvfCgp8eWKaF7R4E-4pJ3x69GibQ26rWlwiOVu2HGFue-zNYSVQMTapmqokNgBTcWT5fphOhOPzvAbPGWH1gQINhphyb2cP4imlphKOPMYOP2fXcsfLZeBmQvHtgui1oGNPzCo4_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKhsnr8jRicTt6WizZfjcMdSV3UFLmqjRggrZdz4OuMIdmZaP2o28szup8_N1na89hCKizoAAMwOcLdMdWrjaLiIItvhzApSJ5guizQBdLimLTqN2nn17mH9opOi0fnwT9Ab2UJLjIwEcZRtsG-m2yQjyY7hymTMw5J3zbbYgkPUXzUXgJJ07Og3ND_-_NDUhLSvnZHL0atXXVwMcx_xFPaQ9PdyDe_-kl-c4QALVGUC3K8Wtld8RBwXtK3jLLWbWUIpfk-VK7kZ308XDEqxOuPeeWPOXPXrYywkwzbgoxeigoX3Pb2gQHHew1SC7--Z5TvARVeBEoK_flJLJT-FIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حب‌الخامنه‌ای یجمعنا
🔹
تشییع پیکر مطهر رهبر شهید انقلاب از قاب عکاس اعزامی فارس به کربلا  عکس: محمد آهنگر @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448615" target="_blank">📅 09:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5046daeb0.mp4?token=VvmD24CrT2UtvxV3OGJbmIXfmWmKjzALo1oKEaOFuShnregxhN1uoiXUUa_-vOCmB_VPhdsatbV9FmGhstAFjVsxozg9IFNiVfNDbwyE2LTsGWhPl2MRwVVRw8SonhkHYk77Hzsm7WxoYrpTED-bS5dfwd1sZUzzVIc1dlGVT9unz-ZA3cddWKFNqEEb5z_HlN1HSjrdkhWL4PAy9tduHgtKekXfq8RWwZcSLYrJYJn-8Ce7VxDK1X2A8k0GJIO0O5e8n09yZkQlo60ySFpGoG-k1FP7X-nk1L5HB3fZmQ_CGNMm91QTG6_8_mCWhti5mFR4DcrjGi5-ApPqPAdoVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5046daeb0.mp4?token=VvmD24CrT2UtvxV3OGJbmIXfmWmKjzALo1oKEaOFuShnregxhN1uoiXUUa_-vOCmB_VPhdsatbV9FmGhstAFjVsxozg9IFNiVfNDbwyE2LTsGWhPl2MRwVVRw8SonhkHYk77Hzsm7WxoYrpTED-bS5dfwd1sZUzzVIc1dlGVT9unz-ZA3cddWKFNqEEb5z_HlN1HSjrdkhWL4PAy9tduHgtKekXfq8RWwZcSLYrJYJn-8Ce7VxDK1X2A8k0GJIO0O5e8n09yZkQlo60ySFpGoG-k1FP7X-nk1L5HB3fZmQ_CGNMm91QTG6_8_mCWhti5mFR4DcrjGi5-ApPqPAdoVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی خاص از طواف پیکر رهبر شهید انقلاب  بر گرد ضریح حضرت اباالفضل العباس(ع)  @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448614" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
🔹
راه‌آهن: به‌دنبال حملۀ جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می‌شود در کمترین زمان ممکن این مسیر ترمیم شود.
🔹
برنامه‌ریزی لازم برای جابه‌جایی مسافران قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده‌ای به مشهد انجام شده است.
🔹
مسافران برای کسب اطلاعات بیشتر از آخرین وضعیت اعزام قطارها در این مسیر از سامانه صدای مسافر راه‌آهن با شماره تلفن 0215149 اطلاعات مورد نیاز خود را دریافت نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/448613" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fkqu2ub0E3qZYJg7PaRarqafO1ZdjLCTx0Y6FHkC-gEFPG5F7k-9F3O3-AQ0mZbryPOru2TGOPV7T16X6Ow-SlVoOLJr7gzPaGcCuWvdQe8AqQ66o6V2D2Q88gVWVVl0HhxeVB-5j0idHruNcgmdxTP0R4CB-w7undVX3-2SaFohfkx1XbO76fz6w8t75I-13s-Zcxx69NeKfn6msaimEvdxCKpnigscqRcjIpiADhrFcPVDd9A7zwZv5gorMl72uWGbOsNJJjzpScIbwJKakLDm6wzEKc8F0K1-YKy8aoNASxyasC6i9LAR4t5Pw544RkS9iSLV3kfa3u-LDBeACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1_5VxbY_hAlq1aQJlnmG4A8rk9bMEz80mlysU97XngF8NpULLyYDZ0GslLTtVX-rIwlwn69JJaz3iyI1b2miIvYsBT0ownpPBl0O9he6MoMT_gSrDKWyagD3VWhPIeia1tBQ57USFL_V0fGtkq6-P9KfafzpybF_FUrAnT2kLHo_fvBx-vvLSeh8PqWYs5VLR9vcsHrImw6elZsYYMQ6VZRpFnwyD8obgmBq3WFLcpE8IVKGtf80Fs1o1ehGTg3nAXupao2_KjiK_cQlXBBNubRoIDB8CunkmIQwzBuP2-JGc0pCKgqxZBfIjTzxUdPkYFnVpeuIoWqxW20t4R8jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSJCOxqOLsKCyx2AyE7_mVL70jWycOOrPUaMUb2PXk6n0_UlTNRXi6pBxomYNZeW1Q0-dU9Swpx7n5R3WUBLUghC318LDEeFAgzOlEhPDMUX6_l488bbbxR8HxWKjypY0CPIKRkG70eu2xPxxAxHZl4GqM7wESLd5PT7C3oxnEKSZiI0Pt8Dwz0ZwjasKwaRm1X6zznqZLLWFHzAcKtFZrGQvtbhKbtMBEzsNfT_XxfhJ9rV5QeNrniLlw2-A84l7NMAbC01HApaHW5wE_QOewFDIsNmmdKYIj9bOIShpbebiFZGUuFfN5AUZoQtsLfC6L6-G6b8LwC7MfGVHRD7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZd_CiR6rZHSJBvi_ZWEE9QdhddJ8I_kSONALDAq6acsv_rHz0dzy1IGbRGNbQ3Pq8L3zv2mItSipmJuiyh0rQlZ8EhtjUDAs24yMCUePu-Cob6EwQ0BBZQ8Vb3Bq9P4KpIzrK8-3uYmoiiRQxjZh--5Ip1A-4--oDGA1msKt-71oZOInGU3j9AFY1JluWcihSv4Suom0VvotvfJR99Z9aMzpOPU-Yqj3IH2BkAkVhpoFNL39LdPUvsjGQANPBn0ABO9Zpb41NP6EIVhoh7ksYicjgtWn1-efzayp2-vcvEAT29iA1gs6tj_NvkgET112QQs39fWV7n4kxhr5Ig_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmQFatm3rW5dmGB9InjGm8J2dC1Sn_TzM3lyPq7lwu3G0azk-YhZvbqbw9YRrmb7cmN87wMzyGkJH8ZsicdjfRmPqijAIfb3qrJzJprmZNTJ8AdCiuUF2CdgYQY-Myi73noQOGpCZkMlC9DJdB2maVP9wFsHxXCl1ipLmpOK1y9nemuTW8KucyqFfqXvWGxg85E_a_bcVaYCZeqjaM8WqBnBYIDN53NVBupM_zFIE1rN-qkycf856Sv0mIKEPBEjkFAvORSdbUIW4RJfbUKQQ0xNYzsAMUQe-ET8ZOMKFIvOBDwd7elRjXL93CyX_wMJ3597c3lFt8UA4F-_FPtYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndsHOCsMDeLB1HeN7y68yqoaREYoQVnjAEyYeMnw9M1LJzhshOYSif9iXv2WLW5zE-fnZmb19iereM1Lc_bJklD1k1qjT4Z9Wk6J3tkDJlsUKP2a8qhQ44KSqJ6JNaPC1_rZUNu_fDbyNkRfJYufOmZgBjDWmZtXSfVZwXhHO7dTdRiPx66xG13zlOaJmvabgaysn-e_2-PDonouuYcipMBqbpoEQAHLQAm43pB2fPnh1hcTc0AL1Zj0Q2t78e-QNu24NmCXgbek5Cv6wE1rQ2pRQ3JqHjCE5LqDcKqcfY5XzfJgZKWp7lZqdqBZh6ichI3NGisCN1E0ogglSmhdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJUh0Q48q5DeCoh6fJjN-Avvpv5WzoP5sxBtHuqSWzJscnCo14QtVyn9ciLWxxbnt3aEXd1mjSUMmZsoDHtyIi89jzwyDyLxFKTwuGDZpE09ktWjv8Qi9xvZP7zhxUROEKBkl4rov5OzBtkkxm2OxpI8UwJGspy3VsK59nVTFt_vvTrqPl1k4Bs2hdbHXUDnYrdW2BGr4VwejXiQX9T1r-9fZJQ_xpaBBMM1w2whb07OslqBhCzkkppKBn311HP2zv0mTRCkBZW73EFD_Fzho2LpCbGWN5Jt8_si3mnujUX_lvJlaZkf-UVQ-3PZnAhjnHBCbhbhd1dNhmwZ0LYwRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حب‌الخامنه‌ای یجمعنا
🔹
تشییع پیکر مطهر رهبر شهید انقلاب از قاب عکاس اعزامی فارس به کربلا
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/448605" target="_blank">📅 07:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6c8a542d.mp4?token=m4bz2gN0ky9A5QUmci646u5fR0WUGQwJDEJxNayKdLWfO1E4LsfASYrpSPLANkS_56n-KWwSUIbC4Nsm3CeeBtUKVjoJw1L_ecfwlDpJqQmPCnVvlZQSbrqauZxlxfyCAWz0FBoYQzSsfESETzjLAFXeVfZ0-E3JxPInG47OkaMKFfsgSAFB7EtIwgdhBFd29BK4Pp1D9o8TN0JXDYcAjGlhki4chYVRjb7HxP657vYokq2bmLVfkfoZ5LACK6ws7gE8jAKg99ful7dYZyEd4fVOzfrj_u6r6_Yn5L6XxyeqXXsqFteKdlUQ3Wet2CRB0xf1RZLoTLbGkoKi-SFHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6c8a542d.mp4?token=m4bz2gN0ky9A5QUmci646u5fR0WUGQwJDEJxNayKdLWfO1E4LsfASYrpSPLANkS_56n-KWwSUIbC4Nsm3CeeBtUKVjoJw1L_ecfwlDpJqQmPCnVvlZQSbrqauZxlxfyCAWz0FBoYQzSsfESETzjLAFXeVfZ0-E3JxPInG47OkaMKFfsgSAFB7EtIwgdhBFd29BK4Pp1D9o8TN0JXDYcAjGlhki4chYVRjb7HxP657vYokq2bmLVfkfoZ5LACK6ws7gE8jAKg99ful7dYZyEd4fVOzfrj_u6r6_Yn5L6XxyeqXXsqFteKdlUQ3Wet2CRB0xf1RZLoTLbGkoKi-SFHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکر مطهر رهبر شهید بر ضریح حضرت عباس(ع)  @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/448604" target="_blank">📅 07:39 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
