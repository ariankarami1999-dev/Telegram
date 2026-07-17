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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 22:01:32</div>
<hr>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raOYel0Gj_FV8S2WmMTDETKE5krbF0VO8ThVsoJ5rPcGHFjdkjdJEchu74ogZE3iy5BPHn1XLcO51zg9z2fK6vshMXttULa1Oj6iLJFpg3cpOBjoVQbwH2bDfxvtECMp_x-rA7IEtF-XlR7ieQYTbj1p7Xuk5arodyhssKeoK6TXyHqb0jgjf-QvIwUVIzVaNCfbFb3VPuw4mIk3wob7LyCDOnBsSR43DLKv_slTJhMnyWdVQU9mmxWPwR9AplECPBlgv6XSdQLRH88VCNBjfSwXXAMWostj-ngNl_Dw4XJTMy3AXonTaPW8Rq-VKb5W9fcbev4mnfhsQt_O1-zuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kowQ9Ujb1aFv7NE-VJ4O1UtrUiwvYn-Tp_gOYcCC9intS2vg_vcyPoS53kZnVHrgNNKK4cJIkg7148f1OWr4pfFVo4m6GPkI1FfYlj45ZfpG0unn8oBJg_y-bE8mBuRlujbTra7JSETafA5HxTWNRPsrnf6U7LwUcJf4JkNk7icVKrJEa5D1u4N5rGp73lSDZgJSV_gYf2AqNvx4R_xG65mdF_1XDLQK_nOsgAHyJMy4Q_dCYZgEn-xbKTQm6O90ORTEKij8RWDtsYMZ3FI_t9NY1TS601mHlmiTuf66eudIffJuu85qpOz78PyOu7ONcdbF9TaZfILpCATsKzoynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXQjf6WRE1ISMxo9dagc4Krqqt_EAQ0eVtvezu1o13439Euwy7ZQcvmsUIvRcvyraR2l3bKsDluOVBul8x7rB2nV9dU5EkcqAmXQuqavlJ57qy8n6JZilycA9uNefLIpNQyLOyod1QzTgcNLA0p5hphupyG5dXDWYu9uisRQIo45s2Ad_a0T5Sshu-0ZIAQBAQO-DBD4xgOyUL6LFKcj0XUAgseDpNjSpcBnh7ILyxJSv2KVlGn8QkHzQL9CUol9n3MQFc7eYJAlTPCEe3U-Yc5LwyYzUtmnxtQ9lLq6FpCvbDiRHxdHiAV_Vx2PCTmNdYixg1nXP6geKPK5v_nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi7BttRD_VR5EK9QC8cUXdoDUzZbQ0xZBg4QqOiwpK3IABA-J3_7HhZloHFKXbAESOsKMS4CqnKhGsi_xUBigEaaf6fdE-MTGO-3q4xOzTDVm-NjoWJsVrGPrsDmoePIBg_9oInEiUG2QKu0-FUYGLoFpGLhgYrahJ3MNUqB6LBDxcmcrivse2lNotPKcAD8ATTCTDJyvxqhOqIRC0JrXI9StuySMbaakcCTFq9wi9G2k0blT1kuLQECiURV6PoQRbPRgUNRlox7aO3ggmyJ5PFfLIgCLKKMT7JTLwOxqTEpJJxQEAl7mfxQVRrLDD-ARQQyogmmBotlUkPWWDRgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcKRR0ukohSmu2TwdLkfo7lZRvoRYl46BVhrtxUkFtEwZAZaLO7j3cnn8HmfgLtNPq1lmLpWyOBz4k9yMfdw5OBwrNQibH-EKcEpVtpSvMb9yUSLuY-N5nBpCs1J_BaKxEBKGTe2l_QHuqk9JirdAsMmqBSsKqXjqo0aesRJDh1WuCRo5OolSsEiMlR7UcclQdwlIC-2Zj8nzMGSGUuFzWeIZj1Y2t2tDwCObfQKAlwmi_enpxfIQ2qHwMJSb0VtUcTLxrsYadD2DpOg0PR0YMz_XDXG2ZfatWHA8CsK4PqOlYuW7tgzGyrjT6fBTAMT_XabExl5riKocOWSbFKg3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2nxrlVHIFxVOibw0bcckepEoDzXIrdUVRkRcukWeAHF6I5N8AfeJdfoffFEzfOnwNevucUVv5bo6ZNH8jQ5Pzlq0KavZnpAeyP7qEhUIygfZZPyOao3_8UXFnzYXKr90Rks1emUunjWToC8pTHroe_C-_O3klGTun4J97LOiLfIx-KGy5h_cbE76tKI8x4Z3_Sf4jOoaG2i4hSwsU7U0XB2lH-t-AfwspayzfwnJsvhCpscuBYoPudNsKcWogs2QdHGLXuUjsh6CH1XRJSyRKu-bNdX-Gx1laEjKovJO_M4DDp9KihdDzMdpCLG3qK5pTdotBRYnbL0OAy2UDHRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSEvhXWR_reVlvuXq34y4-0ZGZQPuSiLwOh5G5PsbaArkWlSjxCIhXgrVXyGIp7fgE9fLqmfCYRMIZsq9rbFO2B-PTFfa73PmQgastYVSrEIjyfTPRSe_1htFUkh2WdO4x9-QuefVDXFJjkXLH1jyNa0mgUVu-kKbcn6H036gbwBEcVEHeoYyAb4hNqLxbXF4V-SMTEimYpv9o1sooNJ5SIoIkhSNn_18obKJRpdWZi5vo051vtuZCRPDQXMxB3_vgxNrqWSQKCHxU37uHPquya7XmNGayQMDb_7p9vSjHgRbj04_g8hVnzvwgk25jqARgyhdnhtltYFlEx4UzOhWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khUIkCtQDwJtTPXDTO430S4btMi--AT8V0egBuU3LYRm5tv8U1jreuvWjNEqxl3fknLzSskmA9VQCnzhF7NWlQL_GSZZC9gASBSDFezsP6YaCXycC_6lwVo0fx87TsGmLk8y0-UZTx-H5To-CENzi_nHgqYirQD6-e2YImqMEOFQlEcIKSwV-O0vPwtxmR98ODTEBHu54EdHU64ReqTX4L3zYrtIwdEHPYbVvg5k4ZILMfw11pe4SPiLHg5uOUdhV1pYL7FAAiJR06nzWbP32pJpXE-FzFqoPuxTj2LMWvw7mYGqViDEKwQkxZ1KF5MKc590ojcJjcKDRMRbeYrOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPDkojMbdYkRpMrRAG_cbIiO5Nf5aM8J-a5ZdSqFosXYLocPrvP3wknkpBI7mT3FL99qeb84-zOlM4QM8K2NchcR6Bovb4-OZcK-lH7tDfHlqNm_tn2QfSxknVbzWcoPksRw7YjX52opnBVImGAePt4wkJT_tgdimueUISAyBWIJElLMX-YKRif_Pz5lEciP1yhs3QD5OeKeEgT1UU4iHM64eHNcAk84jK8umg4JKmcYcBTPU1Bvm6ZM9ESCC2OvfuYM-1yOjakj6zkRqOrpye4M1SeKLr3uBenW-FY_z91qgNOEklDLxLs1n_E_U3K1Gz_eQshrwsIV2qrk2SlZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=LGSuMy5thnsU5j7_0nlbjp4MyIYXysU8YWjPiIhfsk3nZnYY9Am5toth6pA4cGyqb5Tvt08doU3FutjiJFPHapqIRFfxVG9KLARmBs9hsVIMJ4UZb6Pyo1sap5HU-lzYBFStq8D65chURBXbwHnNJi2uvwX-la4lUvsUCQ773BgwKu-gakCaATKSgoKQJwiR7-atR_VBYSTdfwjYS3lvG-eF7_FTmzDS3GwPXUyrLXL2djXErYatZnyfrAHAUBCEcWYDm6F-t0FrrcmX8bBjRCHQtaK1flTTQnWUJzVSVozROGp4MtqaQmPayPVCu6JQ03KlimOlekBLgwDuSSz2PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=LGSuMy5thnsU5j7_0nlbjp4MyIYXysU8YWjPiIhfsk3nZnYY9Am5toth6pA4cGyqb5Tvt08doU3FutjiJFPHapqIRFfxVG9KLARmBs9hsVIMJ4UZb6Pyo1sap5HU-lzYBFStq8D65chURBXbwHnNJi2uvwX-la4lUvsUCQ773BgwKu-gakCaATKSgoKQJwiR7-atR_VBYSTdfwjYS3lvG-eF7_FTmzDS3GwPXUyrLXL2djXErYatZnyfrAHAUBCEcWYDm6F-t0FrrcmX8bBjRCHQtaK1flTTQnWUJzVSVozROGp4MtqaQmPayPVCu6JQ03KlimOlekBLgwDuSSz2PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcu2pbBaxQh1YH03RSnAu5fX2x26mt4NkIO9YQebWACEGfNzEFCHY8HYzwKcZZpFopAExOtKMGTgqExcsC_mJnPBRVdfCFuNtzJGRXowI50O7J9Bkkeo9F17YzI_5CY_OR-02jD3ZKZ_fyXeo-93nMEuKKVvyDyFJaU7nUyE-PZWti__xld7FqyDGMVES3dHpa1KDrDWU5V-mKvSDbjv0OglfLRXLPe8DgPUSlEOHvYs3CZZz5J7zzonrd_n12osj5PJng_QxhY1eGQLInYnyohZHQccIO1jsmuFmGQGA9n-q9-2vaA7f-wwtI0BPH17Ra3NjK-Zkk3A66QFLeHZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=vf3KuCpjCse7EzodCSC27iuzYWGtDndd6gsGy6lZ2-NWgPapUgG24WsRzF89-nvlpeSjzCcXNq_96ZaL8I4V3Q_b60tz8dHIgJ4qTAvQjl1ObmM-2E9QjtshPE7GneTzHzsVFBL4D_in_RynyBjrE53r0oy1T8iABvSdHBGp94TA0ACDICTNWp7S1HxB_AnzBmSc7EM3cuFfIJY_NxSap9a_8IwyKDcGgqLuvsAXhsUDk-5XCtjE1lWFQfOszIJ9VxJyXLlInRxKNNOKeNl32oPdfcoZMp-rD72-d-jhyLe_XYGUJHiIzBIR-a2-ZZSvY4NlRBTuTTZpW0PgF-qTfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=vf3KuCpjCse7EzodCSC27iuzYWGtDndd6gsGy6lZ2-NWgPapUgG24WsRzF89-nvlpeSjzCcXNq_96ZaL8I4V3Q_b60tz8dHIgJ4qTAvQjl1ObmM-2E9QjtshPE7GneTzHzsVFBL4D_in_RynyBjrE53r0oy1T8iABvSdHBGp94TA0ACDICTNWp7S1HxB_AnzBmSc7EM3cuFfIJY_NxSap9a_8IwyKDcGgqLuvsAXhsUDk-5XCtjE1lWFQfOszIJ9VxJyXLlInRxKNNOKeNl32oPdfcoZMp-rD72-d-jhyLe_XYGUJHiIzBIR-a2-ZZSvY4NlRBTuTTZpW0PgF-qTfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=s3VFsfJT6-BQWBKSCnpH1FT65_LK1X8EMiFjlXj0NQlDJelpdfjb5sJeKDgVWqwLbIxq9IuzBAFGA9d2YRUi-ae1-plTjy-DHFsT9tOCJYb5-m4vZi2Sry8P_bLpKsNVyGPyo77lDPWJkGVRYJU171Zy-sARUS3mM8EvPpd9nmcwZffLvrAoEWfHERXFTGXeWU9P5xbiNef3aFhxRwvHrcZEKbihv0P-cVVueOdABJirBmWQtFJyuc7JoQPo4YOJHRLK0h_dXex90z2PHS_O7aahRYonwoWTD9FjGcNt1qrSAeyIGqsIuraibm474TcIYlRo6LuXh9KuTjZX9TCx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=s3VFsfJT6-BQWBKSCnpH1FT65_LK1X8EMiFjlXj0NQlDJelpdfjb5sJeKDgVWqwLbIxq9IuzBAFGA9d2YRUi-ae1-plTjy-DHFsT9tOCJYb5-m4vZi2Sry8P_bLpKsNVyGPyo77lDPWJkGVRYJU171Zy-sARUS3mM8EvPpd9nmcwZffLvrAoEWfHERXFTGXeWU9P5xbiNef3aFhxRwvHrcZEKbihv0P-cVVueOdABJirBmWQtFJyuc7JoQPo4YOJHRLK0h_dXex90z2PHS_O7aahRYonwoWTD9FjGcNt1qrSAeyIGqsIuraibm474TcIYlRo6LuXh9KuTjZX9TCx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=eHbMJ9sizPKUmuGxDGtKK3OLA8qiqNpl0_hCBnuijFC9XK8xOAUW-914RxahU9bBXfPE5ZK4hjbgjBdu7LxOiGYrZWZWv7_LhJsMtL5mEv32OiJPKyLGkAJYDMM_tQDgvMW4q9UJ0LNy5pZ7xNzHwmDrnLs0d7krnaJRCyasdOhbTuWnc6hDOd8JTOhoH4OijV9Nx7KWopnzwIoyiz2wIaKPI-hG1jlaZPgkolLWvQu4LFsmv-Kh2Jj07aSje3n0IeqyIEMMWR58ONFnysN0BmcWm7vrl8_zcuVJDfshkQ5XvH707i9N7GU12fiqZpD2VzU6fJpFVKAX2p8sAExg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=eHbMJ9sizPKUmuGxDGtKK3OLA8qiqNpl0_hCBnuijFC9XK8xOAUW-914RxahU9bBXfPE5ZK4hjbgjBdu7LxOiGYrZWZWv7_LhJsMtL5mEv32OiJPKyLGkAJYDMM_tQDgvMW4q9UJ0LNy5pZ7xNzHwmDrnLs0d7krnaJRCyasdOhbTuWnc6hDOd8JTOhoH4OijV9Nx7KWopnzwIoyiz2wIaKPI-hG1jlaZPgkolLWvQu4LFsmv-Kh2Jj07aSje3n0IeqyIEMMWR58ONFnysN0BmcWm7vrl8_zcuVJDfshkQ5XvH707i9N7GU12fiqZpD2VzU6fJpFVKAX2p8sAExg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=BFFGNL9eUOSUMq_qQHPpTzsGtRxC8_WTKDc9BtBZ6clrO8p2BVoTuJ7wqKM65Rz4dBWTNTGLvyKaIJbd3JPWlktTcWwEIF75hVXoES49-Sb2Cxns4kPKwwch5l7cZU0NR5PMQ9xnM6a2iozICeF-WnnHgXYcPWplINxDPKSrviD6sCn-PKcm-QgU00MlA7CWOKxp52iZ-F1Zf3y8bRR6kj8uxnK8d-C2eUwRdTwfFKRaagv-AAWjaowT7JiOacmEZ2WXkHujh8Ie9JMGbJEDKm-L9npEYcoR-dgBau-lRiUqaUiBvM1podemeJDc3i_nxjQgd4_S8ySRvBbHBm1z-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=BFFGNL9eUOSUMq_qQHPpTzsGtRxC8_WTKDc9BtBZ6clrO8p2BVoTuJ7wqKM65Rz4dBWTNTGLvyKaIJbd3JPWlktTcWwEIF75hVXoES49-Sb2Cxns4kPKwwch5l7cZU0NR5PMQ9xnM6a2iozICeF-WnnHgXYcPWplINxDPKSrviD6sCn-PKcm-QgU00MlA7CWOKxp52iZ-F1Zf3y8bRR6kj8uxnK8d-C2eUwRdTwfFKRaagv-AAWjaowT7JiOacmEZ2WXkHujh8Ie9JMGbJEDKm-L9npEYcoR-dgBau-lRiUqaUiBvM1podemeJDc3i_nxjQgd4_S8ySRvBbHBm1z-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=OMijOd9LmYXwRKmQ_PDt9hc-JRtJrfr4J89DXNFmv2Cyc68RvBs-KhKXOQZcfdR3sPlvH--G1p-c6qUl-otWxttd_3YeJbsUbMOOdpzH1t6gzmP4TLr68QImRnPffzzvckL7DYvIvlkWbdG9-WoFe_WlNnCzYfmZc-2KZQ6F3znfAQE54n5XuogUC4wWy9hU5ryZMjRQ-PmgRZAi4U23Omb4i-U9LC3vOOCysB8DMMy8_3sFoyhdlq9G86Qd8DDDFw_W65_GiHCt-SvFvKQEY55Pgwq1ZF7FwbEOw2sv66N8kXXXSB4sN78ZMJ5QPlDHbim_bsx1QmwVNtUgSzOnexOXaKdUwoYADmSQ26QzFg0R-P_B_Mzh1GbpRdy5myMAssWkcF9RP18fQtqP6PuG7qBirB37FtS-cdp4A5Ui2GZpzSbIZlVPFilryko3pIurHJHoZEr2DX9N9fhif4HPUNVVkPxaIcAwDUmU2pYr05v0HvBQtXnSC_0VjGhyHAcSVXty8R7EQZMIz3lMVEURjYsDV_RPpukuLRBS-lJLRfplprWrEl4qqUkI_6ZvnDPqvsE7lRGBzEcxdnZXBoyQAYdhzr3XC7SR0hOAXAeu2qMK-s39fs_3gARS_V1MbiepjDrgcnxsBktiZ2XoSMoLsVhPTKigdiY3VUyTIUctD8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=OMijOd9LmYXwRKmQ_PDt9hc-JRtJrfr4J89DXNFmv2Cyc68RvBs-KhKXOQZcfdR3sPlvH--G1p-c6qUl-otWxttd_3YeJbsUbMOOdpzH1t6gzmP4TLr68QImRnPffzzvckL7DYvIvlkWbdG9-WoFe_WlNnCzYfmZc-2KZQ6F3znfAQE54n5XuogUC4wWy9hU5ryZMjRQ-PmgRZAi4U23Omb4i-U9LC3vOOCysB8DMMy8_3sFoyhdlq9G86Qd8DDDFw_W65_GiHCt-SvFvKQEY55Pgwq1ZF7FwbEOw2sv66N8kXXXSB4sN78ZMJ5QPlDHbim_bsx1QmwVNtUgSzOnexOXaKdUwoYADmSQ26QzFg0R-P_B_Mzh1GbpRdy5myMAssWkcF9RP18fQtqP6PuG7qBirB37FtS-cdp4A5Ui2GZpzSbIZlVPFilryko3pIurHJHoZEr2DX9N9fhif4HPUNVVkPxaIcAwDUmU2pYr05v0HvBQtXnSC_0VjGhyHAcSVXty8R7EQZMIz3lMVEURjYsDV_RPpukuLRBS-lJLRfplprWrEl4qqUkI_6ZvnDPqvsE7lRGBzEcxdnZXBoyQAYdhzr3XC7SR0hOAXAeu2qMK-s39fs_3gARS_V1MbiepjDrgcnxsBktiZ2XoSMoLsVhPTKigdiY3VUyTIUctD8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=ExROm_0usRt0ZpvPEv3W7jX1R-iQucT_nRVZJBY3axsNuTBo_hdbc_d3BYmrwOh2-1GdlacyDPfHbyisJrnSuFaaK3l3YkIHWAfpSHoFqNb0_p-r_oKCCTmEc5AhF7aHu6NQ570EXdPMJToVoJs9UnweAkAX7Vg3QnTp0JbAWkNUAdh5Yxbrfy7DMCuH3aWhWXPmGwa23lSdhlNxi0YPg0uoTg76UkGWcClcqd5XR4-EMnwh9h-JlxJhgZ6NsOKc4fGsVh7G6REHZLAmXlj4z3X0PajKOtcKIB4gwo4jW3Om-cu1cLRGtYu4D375lhrEyHEgS8JlXtXk1h6-mTnuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=ExROm_0usRt0ZpvPEv3W7jX1R-iQucT_nRVZJBY3axsNuTBo_hdbc_d3BYmrwOh2-1GdlacyDPfHbyisJrnSuFaaK3l3YkIHWAfpSHoFqNb0_p-r_oKCCTmEc5AhF7aHu6NQ570EXdPMJToVoJs9UnweAkAX7Vg3QnTp0JbAWkNUAdh5Yxbrfy7DMCuH3aWhWXPmGwa23lSdhlNxi0YPg0uoTg76UkGWcClcqd5XR4-EMnwh9h-JlxJhgZ6NsOKc4fGsVh7G6REHZLAmXlj4z3X0PajKOtcKIB4gwo4jW3Om-cu1cLRGtYu4D375lhrEyHEgS8JlXtXk1h6-mTnuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvZOUNkIJDpfIQbvBKkZA5oGMQST6WKEiluxWcTY6dQw-RULx5TUv_M3jsblrWI8cATdLYLbOCh0OiMZbGtyXg6FLGh0DPu-QXdNy8W8k51hKVT1NsFf-yQhjkNeheOdjZsmGo3TA5movxdt4D3mRTjGSnFdmhvJPo6IL-47zwL5uupWjNfVTlkp1IvHYmyJMYbVOnbjceknwYm4cwu32nYeJL9Ssxyurtm3Iu7Tot7N41xNSNb0Db4po4tq90YPGYA6QJUQB0pE1WZkc0-2JMRtPrTXUKgFp1FTgvzd_EYXgqh6evaDXo_NsCdI1Mx9RUc6L8ouQ0jJrykTIizLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gODJp0z8pOFNk529sRRVoimhAC8qX7oo9W3ym0Zso3vbDC4ZHOVuVCPGOsR6_4NmHcxkSt1psDmSRVxWtCHMfujoDuZ3sEr6PYyVRAFkTfOPQj3s8GhQ74HWHAIgJy_t-OuTS7gJYJluIb-xLyIddj7g_QrhPYIdIYvODGqSZI95_RwoC9xCO4TTtRXa6BUDJBMBuc1yChd2ej50RXdZw_DiHZF82IT5yZE8pjntE5TGps__QkFWzBaq2sRY8J4M90UxHg_-P2irmvc6Ic6agspU71H6sD9B7rKMQQFd7rwlvg3XI8B6Cdy-pcpX5YRiXUEdXWWUGfH2ayFlxgvaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i71l2RHEt5-VSh82lgh0uNOCOwRnmMuR0QRpyTjV6EBV3PrZtgdlrhPT6oofTsiFY7nMbOsSjdEJIgdboWO0uZEM50-FZYqM6PKI2CcDu5HUjCbxCvJPC-ai-WGq_wbDFEz70Zohwht3cDr_uu-tX3Bd4kmgmu5UKk-rmL_Fy-EHZM8TgeSNDg22GlRi_Svrf0qDPAwUr1JM9rqC-vuoJlPNZIQWQ3JbyIx5yiYTMyhFxRqKMbn5eXDI7zOf5fsLFOLFoQ3l58RVNt0ZNOmGDEHstw86lS_HeYAOWB_ujufKwsYEd0DN7lR1cyid2YyNlqr-v98O9nEOoDkj15G6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgkjw4MbLKc3nGrBKuogWBkV-RFir9V_566AjITJsDhP2YIS4dgA_54HT9g-84qvctL7UJY7xaBA88lw0bHA3-nD8JoiwSBtAxuyQ7RQwf5mPISdVl1UvRIRkHVOtrESYEEyZ7KXDsaqbUx6Le2hmtFF-7_0kUlpfaiEOA0cWfHEBXHRKFOKZy46glWrONn_1RTCzabkOFjcuEYWBbff7quoCl-LOFpPPb99GNRNt-Zn3YHFU3YT9MUCxzshzDXC08S-LpNzGkguyrKcc4n5e7aXBqAsSgaCCaOCAPk_SjKGq2tXs5pa0eIrG5urNbyKinG2AuKsxagYtZwuvH8E0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=qX0ofatU3LTG0ip8lHnSKA8sC6ZxBDErVuLLhxhmXHzemHpG3WFdT566voLQXCPpgOzXvdiFceoZF_hh0B_PZ6E0szj06dFKzAYairhb7QDMh4trE7rqmSu7oqFji87rvDD9r_0WinrcNFVdyzDjVxn0v7js1WtyQ-fmJDO5KE9Sr9_IwnyZOwN2wACWDRy8X0-Cxet-BgLYoviNgy0IIR4x08G4Ouewe28kVyp0yEWPKFhjHu02Wf2NWnOVCn5qjeVayXew4dDWCKcU6voGV-HBh7LPX5AjSS9zH-eNjDwU3y4O3hP0uqWAeLQGgwfdqDlbJ0chl9xzaq50BN9Nmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=qX0ofatU3LTG0ip8lHnSKA8sC6ZxBDErVuLLhxhmXHzemHpG3WFdT566voLQXCPpgOzXvdiFceoZF_hh0B_PZ6E0szj06dFKzAYairhb7QDMh4trE7rqmSu7oqFji87rvDD9r_0WinrcNFVdyzDjVxn0v7js1WtyQ-fmJDO5KE9Sr9_IwnyZOwN2wACWDRy8X0-Cxet-BgLYoviNgy0IIR4x08G4Ouewe28kVyp0yEWPKFhjHu02Wf2NWnOVCn5qjeVayXew4dDWCKcU6voGV-HBh7LPX5AjSS9zH-eNjDwU3y4O3hP0uqWAeLQGgwfdqDlbJ0chl9xzaq50BN9Nmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=WL17bmxG3u24VWs95aiTauABvyRFvK7hMNfK6jbnvzxjmTnMVJu3aI7caW-7DjiKGbmYw3KeC-B6vaYZ5OIovNQb-dQfr5dRJTcD1RYdbVBiHHEF-MXnNbSPUFLCb-rskoQ7xvGR93U8YDHhX9E9GO3GOkIiTSRsy-ZJ8uvgnRW1xjHHdIM8rD66V-V06bI3KnSe2pMQkHAcqB3U7bHy_fxL_meM6WpguShlDL_qDWayQptqidDlANHexAzQfsWi3HeF-_KIIjjmLl6qVADLA3zf5zCldDzm-Nwe11pNzOxa57sP2Z4oWH_iLSqVM9EdONF_7dO3BqBTTHS7zZzqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=WL17bmxG3u24VWs95aiTauABvyRFvK7hMNfK6jbnvzxjmTnMVJu3aI7caW-7DjiKGbmYw3KeC-B6vaYZ5OIovNQb-dQfr5dRJTcD1RYdbVBiHHEF-MXnNbSPUFLCb-rskoQ7xvGR93U8YDHhX9E9GO3GOkIiTSRsy-ZJ8uvgnRW1xjHHdIM8rD66V-V06bI3KnSe2pMQkHAcqB3U7bHy_fxL_meM6WpguShlDL_qDWayQptqidDlANHexAzQfsWi3HeF-_KIIjjmLl6qVADLA3zf5zCldDzm-Nwe11pNzOxa57sP2Z4oWH_iLSqVM9EdONF_7dO3BqBTTHS7zZzqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=YTt7Utj_MWlhJFZpnrS9rEuHDun0YrpQ5KyoR1yHaNQuoPJJXrPqePcM2AHFMr_OZxvykLLRlvMJqVZ6W36Yxucy9CQ61s6_IdWvUj56wYfdqvXUVAfuOeba3XcAXro3Zm_zOkgFN2PZBLdKRlfZAQqRUMB1y11dgMlky4YoKvezuSxTDaUggSSNMPbbfLYU7torcoSNTVexc6x391IXF0WvOUCndaywpVfZKnr8pvX_j73BBppGWs_kv-Y6OPsZkyCqd7ZM-wIcL8FWbmvWADauj0vekVte06hMHX4mwdYgR8z2Grtj1WeuoXCFzmofU-e0S4mX-tpiQ-CX6MLzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=YTt7Utj_MWlhJFZpnrS9rEuHDun0YrpQ5KyoR1yHaNQuoPJJXrPqePcM2AHFMr_OZxvykLLRlvMJqVZ6W36Yxucy9CQ61s6_IdWvUj56wYfdqvXUVAfuOeba3XcAXro3Zm_zOkgFN2PZBLdKRlfZAQqRUMB1y11dgMlky4YoKvezuSxTDaUggSSNMPbbfLYU7torcoSNTVexc6x391IXF0WvOUCndaywpVfZKnr8pvX_j73BBppGWs_kv-Y6OPsZkyCqd7ZM-wIcL8FWbmvWADauj0vekVte06hMHX4mwdYgR8z2Grtj1WeuoXCFzmofU-e0S4mX-tpiQ-CX6MLzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfSQf6x0B4QHpTayjpCRuh5HCdpc_ouZowqHcVfmZk-VMk4Z7iZL_tH1dZtL7jIZmaXup9n_fNAVLT9IlxYOH8JzCe8JiN5xJ0L7zrc5fJtLRUGNBVaG33i-ZiYGHVc4WRM7Xt8UA2l-Y9SwkvUgzlFmR2FFrgWfIUXT8341zkd6J_-niSJgSCGSs3l4pnr1IUIJlSz7T9OP6P-a65PykjtvjwkBmM0gzEZMoqZvVuXrcass4ki7T2iil2Qria3ZsXnTGmgctf-dIxlvSq75suODna9SDlwcMACieFzwGAdniBCFv4uS8f00YS2WTfRK-zYLRHHa1uQMaMARdwd32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6nCxGMKt63gh5LlaKuFgWBIukmd_ROrfbdaMSfEJcMNoPnnc1lKIFuEfu5ikwVPK7QodXPmeYpMV6l6cO8_cvzoax4C2gvo7a1-mUZ0c9gFrxBHUoO2jplAU3xDSZNB8nAy4KYPBRgrkJw2eM0nxf3UduWeujR48r2zZaWsSjrLVainSq4XBnyVDlXb2wIM8OwZG0cKf2O3fzR5A7IVcurIbhdbTjT7x1MhvZhBPHnxItSKq0XcKDbNnHPfNz4nTPMannakHO4pQyvFIsK4BGOng56gXgh6aV5bdm-6YAKzSLMG_WQOHjHtO4qBKqDP2zzK_uA0ifF5rMvdbGUb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=Qfn_ZgzpRTKQEoYebAdW3C1Qx2YZrM2umJHnCdlxFdkQn02WhA2Ja2WLSd2EaEKcZzqOKBiVWWzBiMzs8dHJ7liZ8U52QDs-zMXithC6uvMmlKQmwfOtKI5vAVp1cFG-Uy7HGg2zdRKuLkL7I5qKTxjXn703azkt8a4EyOZbvGtaxEsigP0uVj0I7L5WLhT3jEfaz9cVwrk3cJGoh94ftoQxqXOlYLFcLuOqoTDQZfqESmXKYDwvMZ2SSu49LXC2CdXg0G_saBAd1S9Us2FWSQkkiRB9mGbudZkVlC9ZcXaktMdtTLGeWfCenKzh1RGlqBFcMWtpRZxCGSXKvL9O7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=Qfn_ZgzpRTKQEoYebAdW3C1Qx2YZrM2umJHnCdlxFdkQn02WhA2Ja2WLSd2EaEKcZzqOKBiVWWzBiMzs8dHJ7liZ8U52QDs-zMXithC6uvMmlKQmwfOtKI5vAVp1cFG-Uy7HGg2zdRKuLkL7I5qKTxjXn703azkt8a4EyOZbvGtaxEsigP0uVj0I7L5WLhT3jEfaz9cVwrk3cJGoh94ftoQxqXOlYLFcLuOqoTDQZfqESmXKYDwvMZ2SSu49LXC2CdXg0G_saBAd1S9Us2FWSQkkiRB9mGbudZkVlC9ZcXaktMdtTLGeWfCenKzh1RGlqBFcMWtpRZxCGSXKvL9O7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=VAy4FlEzzuwTYIbw1mVagV2qbdSG7-DI9vW0lzl-VrbPm_-4CGDEyzZfZBiM5mHSgplNX8F40kpmChKWJhXRwKyw2qEwUiEjhcMbQR8N8sMtNa4K21IKptwo9bysSgl7L57kA19dlH7RS0yiGIAh5HLEid-H4eqGjOujJSiCyMx801KJhajfg8jRN3INb0_rjMXVwPodFZf4RPyaTlBlh0dy9XW1bR_pWj2Ov9UEjgD-LpxuApm8GQUIaHMmq5sArn_DwcgBFD0EmnUiSWDJSLZylCX301Z28Bij3AhmQGODMITn_w9ZT9_0eHjdWzKF0kj2kEN0lwySHLxuRFHk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=VAy4FlEzzuwTYIbw1mVagV2qbdSG7-DI9vW0lzl-VrbPm_-4CGDEyzZfZBiM5mHSgplNX8F40kpmChKWJhXRwKyw2qEwUiEjhcMbQR8N8sMtNa4K21IKptwo9bysSgl7L57kA19dlH7RS0yiGIAh5HLEid-H4eqGjOujJSiCyMx801KJhajfg8jRN3INb0_rjMXVwPodFZf4RPyaTlBlh0dy9XW1bR_pWj2Ov9UEjgD-LpxuApm8GQUIaHMmq5sArn_DwcgBFD0EmnUiSWDJSLZylCX301Z28Bij3AhmQGODMITn_w9ZT9_0eHjdWzKF0kj2kEN0lwySHLxuRFHk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9rvQvA6X-53TZ-aGdeykx58Dg1gAf5WQiDOLeo8Q8rJa1kXrvw3kU4tcfP5mlTOaa9gP40rubTF8MyE2ZMEG-BWLJwASXWW2SAbROPbCAPT9-llcxjpqIZgXrZAwZNm6LiKYyPYd2OIiY0DNaL0uz4bBGiHbHxjrtaj2hSyMWoqU83i7zsiA_1IU4h7_qFLJ7MOFmbH19-alHXbTmp9pxntRW7aoXrr4vM07sIbPXoNIQ_0YIMm5oKIovNjOPx41kJglfcmqP8_VuWXTVZzt55eOu6LApbGFS6slJ0OEOoPfZlk7Kwv_C9a3nfvFM7JIgNGYM3vI-yQVS8dmsEZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=aLY3pyp4SVG6k0B7-JsdxKQjRo2yAqBtueC7GhfqTdjo5oPRytqVkzw-bbrNFro7zWJhlrcxUbpYX-I9ehwTG3dpCA-KJDxVxBgUSwmmNwlcJwXEgwzXFl3yHr_lL-AwaGvaNeJMSQ6E-RWPyc7YKosHyTtrIcrlucmSYrp5-ADynnBGP9efnHUdPTShFRHzC2TiTDwpwQYe_SZ5TL7xipE1llFPhQsK6_Z3Sxbxfgq4XHyZji_kunu0HWLt1pzkAm7GKq6edLyp7bWty-2SMsESNH9xrEpLXcl9vB6jgVVBRhJovtbe9QD_rDEzdiq63lSpy7FJ27NWlMHVceDg2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=aLY3pyp4SVG6k0B7-JsdxKQjRo2yAqBtueC7GhfqTdjo5oPRytqVkzw-bbrNFro7zWJhlrcxUbpYX-I9ehwTG3dpCA-KJDxVxBgUSwmmNwlcJwXEgwzXFl3yHr_lL-AwaGvaNeJMSQ6E-RWPyc7YKosHyTtrIcrlucmSYrp5-ADynnBGP9efnHUdPTShFRHzC2TiTDwpwQYe_SZ5TL7xipE1llFPhQsK6_Z3Sxbxfgq4XHyZji_kunu0HWLt1pzkAm7GKq6edLyp7bWty-2SMsESNH9xrEpLXcl9vB6jgVVBRhJovtbe9QD_rDEzdiq63lSpy7FJ27NWlMHVceDg2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me8hZ2HcOU1VNgK3k2uM4S4-Pe1VD5JpgAS44vQXeoMiEvpsAx_drwjLg4hvNCmM3_j8camKjIwb4t8hmjDVxbTmIF36vdzCdurUJ-9vnsJd1sSREoYrngarZOyPtIyMUO9ak2IpyFYCtzgOstiTY_Rzr1iaGWm1YsxyuBnOjLgkVxdqEL57OWUKA8S8U-YjL5ENCu4_EdY1v3r0hBhN9pTGAP2NYY7iQTv__pjzYbwXkZ_LeuiQahEGXy1kB2HMNOweVyIMPy1kCuCrCaEgyub7re1kabH2Lw08gRcFxVsrk8EdvjE3D8HLaRTs6SzKxxN0J466e_aIekDg9h5pHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=tdI4u6J7QfGYeikJXdtT66ERDndmKAQUnxJHAlZKECii4Yc88GI6SB0aA1kwh9EXdQgPIqDJaPYktORUxBhTPnqGIRFqHm2TYCQ-0XVePbhPqqjNbbf5PdLPDq0x9I0lf1mdvykLFHgZRbHG-lfGYl7BWDFb5qrCP2cYEyppY3tKXgmZnz-lGWxU-3PVIz3CS4maXe8nDWtg4xcf1ILMgV83dMJBZ6CG8E8azvzskci7wktUsg3_E7Ic_P5QfNvXFfX84epJH080Pr9T-dSMejBZBBR4dO7T8jJhAsN59umT33Un6cXlPydaZZEU21IjU1eO2RHPXep8RC6X3OilOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=tdI4u6J7QfGYeikJXdtT66ERDndmKAQUnxJHAlZKECii4Yc88GI6SB0aA1kwh9EXdQgPIqDJaPYktORUxBhTPnqGIRFqHm2TYCQ-0XVePbhPqqjNbbf5PdLPDq0x9I0lf1mdvykLFHgZRbHG-lfGYl7BWDFb5qrCP2cYEyppY3tKXgmZnz-lGWxU-3PVIz3CS4maXe8nDWtg4xcf1ILMgV83dMJBZ6CG8E8azvzskci7wktUsg3_E7Ic_P5QfNvXFfX84epJH080Pr9T-dSMejBZBBR4dO7T8jJhAsN59umT33Un6cXlPydaZZEU21IjU1eO2RHPXep8RC6X3OilOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=OyaLO9MwRWk4axprPVDRzWlSZw9BBrBZW633_SFfRcex7_zr8jUy5lPOn9jL1kFVvpq7e0BhDV1vnLRDfbkEq36ez387PnLsofKkmiDoGNaWX37ftXnhreFR_GiSRuBP2suoetlEzKqz8cNX31qnJJrBE2jUq7-PRT_Ug2OjU9gBoJ0QbG9DN9J5NarTrlbT6eHkhAO_UmCvu7S_WTlDS0_6CNgulEAxRw-NNoJ1oo64sLIjDD3a09E5Qta7cdUYWX0dBhLEtEGwD7aZ6ghXucV8AyoIjF-kb6VXJnNeh184vbv4Smtojj43CFQ4bHQC1rpEyQ5l5o1LqnAlqRj4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=OyaLO9MwRWk4axprPVDRzWlSZw9BBrBZW633_SFfRcex7_zr8jUy5lPOn9jL1kFVvpq7e0BhDV1vnLRDfbkEq36ez387PnLsofKkmiDoGNaWX37ftXnhreFR_GiSRuBP2suoetlEzKqz8cNX31qnJJrBE2jUq7-PRT_Ug2OjU9gBoJ0QbG9DN9J5NarTrlbT6eHkhAO_UmCvu7S_WTlDS0_6CNgulEAxRw-NNoJ1oo64sLIjDD3a09E5Qta7cdUYWX0dBhLEtEGwD7aZ6ghXucV8AyoIjF-kb6VXJnNeh184vbv4Smtojj43CFQ4bHQC1rpEyQ5l5o1LqnAlqRj4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcoy4U1Tb-Y9CGQac91ScU3OR2w4gzvc7gAimrnc-8jUa4afM4XsODqpzDb_ZfYXKrZT1xUqj3EIl9C2A4NT6pRnyKVMjxLk-s5Bkcvl7mho7GrvEpPgvlYdTxYW0cZcSvVjk7SoJ1awETDSypTRvo6yA0aTKeM5Ex22BvlB7c6E5Y2fdjEe0FVcGrDatdq3VhwBU0jPf_RArEX7nG9iT5LfIo7lGIuKrB83Yp4chvfLc3JQDpX3eFwTEEBn86xVGkkewA03S_RKFcJ0JhBc4VvCELjDbb4vyPgZprtW9u_Tx-oWJTBxFRsUhlUUr4d1-AWmGi_fZtWEnvLsg12Mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6vVpxCXDMbUdhutSrFyWTzWe0ErUKc7QuYpnfdI3ZzScEYVm4QPrWeHjq9SjMwS77156kXdcIUaiIec1SWIw4YRjCbhppNMglmncAiGXf6bzJpvX4OuKWVeKWRuhVa7AoVeBh350r6yhxsRdaA0JTts_c_EFjMS7KNJbWQmg_C6JHWGM21JfjBpIv_4usYo3dBlKpdOBb-vt1ih-ksPL3kmThweVa_wdMdL_hl0NM-vfsbGgXpt-LhU4KUFxWBSbUkYBfxpRJ3jY6Q-dlgB9W-f_vUjiQwrf4bHI1CLJKeyiJM6DOlqMfRCqIJNqEHV2WdyY1RJZ5Wh20d6zm1BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=aYye7ZMocTB7TZkjk85eiSIxwecsVbHZNXgzThLZrFxS2S2f9OGppATro5ybnScRGyPpuPaKmglmgJytoHrGZrPAVRr3fkbP7NVQjkLikpn0bQyaCT02qRKuIh6NuclPNP-Z-JGu7vuLUUXWThjuwqxN3EwQ4iL_CWi9MRkf1cQ8luybo5BI9bwq0DJ_GitnliIGp6k-atW2XgulBs3mfxjBeZA25H11L_WHkGvpQb5Oo6WkJ19lWrpgIsE0c8sI_QsfTR8j2wlD4DJKH8iHHHaWStX81nqtp2vygoFmFXis6rxZNTOzStnInz69EPz_gZZ5VBHOEaQG-WaiXzp5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=aYye7ZMocTB7TZkjk85eiSIxwecsVbHZNXgzThLZrFxS2S2f9OGppATro5ybnScRGyPpuPaKmglmgJytoHrGZrPAVRr3fkbP7NVQjkLikpn0bQyaCT02qRKuIh6NuclPNP-Z-JGu7vuLUUXWThjuwqxN3EwQ4iL_CWi9MRkf1cQ8luybo5BI9bwq0DJ_GitnliIGp6k-atW2XgulBs3mfxjBeZA25H11L_WHkGvpQb5Oo6WkJ19lWrpgIsE0c8sI_QsfTR8j2wlD4DJKH8iHHHaWStX81nqtp2vygoFmFXis6rxZNTOzStnInz69EPz_gZZ5VBHOEaQG-WaiXzp5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=sDP_pJ0HHLFhKGhhE--kpdUl9li1JfkT5oyjVm5nCLd0sGQ6q3D18dYldGrljN_HpakM700lQaEIQ6kprCIT36SPBl7IZBqwET5x4QHJoxj6u_lC062TUHLkyzQRuF3QFVjfavXenAHyLgx5cteND_FSfVuvSLlkT7v4-Tra1ODA-bJ4wLv5a6E9zR0lv_ISHdXIJYsZg1TqoElhaBvHOYhTebGH6xf-RJC34CP01oJYmlIVeXc2zlm9GRzanGjBbouOPXS9647_OHgPEG09V-4jqW_yTE6Rt_Zi6KY9cbnrzcvMx9DtBmNJUkOjzSjKh-14J6OHOnFo2Cp-gYLaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=sDP_pJ0HHLFhKGhhE--kpdUl9li1JfkT5oyjVm5nCLd0sGQ6q3D18dYldGrljN_HpakM700lQaEIQ6kprCIT36SPBl7IZBqwET5x4QHJoxj6u_lC062TUHLkyzQRuF3QFVjfavXenAHyLgx5cteND_FSfVuvSLlkT7v4-Tra1ODA-bJ4wLv5a6E9zR0lv_ISHdXIJYsZg1TqoElhaBvHOYhTebGH6xf-RJC34CP01oJYmlIVeXc2zlm9GRzanGjBbouOPXS9647_OHgPEG09V-4jqW_yTE6Rt_Zi6KY9cbnrzcvMx9DtBmNJUkOjzSjKh-14J6OHOnFo2Cp-gYLaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF5NBSqWevubxzwW9hgKJpOUcLigvSBkdNfTPNG957rx6qSV3-eBBSID_CR6drt4wFvpiS9VNs0HtswV79XsowRFQ719Ik_OSAi1WrWwAfPt-wuy4GvaHnY-nNSP_XiMM4g6XXlEBmrNS6SjRBZK4180Hg5pwzjmD1PVPm2tUjFfRmuyWFvhoHE2Js7pzR92tES1U4MqJUGuCFte0iUtCnaZyo_NW8abhkehXPlh-jc8lvOm2ftsJ4qjnP_A6NQ-GvxaQJqIp_XLJqtfkjy2RJR4kwmOWZFzC89Xz4ZevHJYuxR2QXtg-Q3cYQpuPcCDi1jV81BwxDIzFoDaj_F-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZfSBI1eGMuOwI9U5BDIo_7LjWYHIIIc3PYAZ8-4-w379S5-nLJl39qWwgluzYz99qAGNRnC3Jqff-zuou52uM_N-BsE0g-IbO50tPWoCoI-6MVjydCSbLM3byXDCCIwGWMT9RwEoKadCZpwBV6cHCvm56jc0po8rBhmX_DkXXMGNXFDhG5bb21fHP7VZPS0OlqA43l-zgN9BpJoft-to6RoLOLvagb6E6d8chETZ73QvwlFB_9mkeV0L07wR1hRoaQttyfWmV9OVE8P9N_eUTb0pY7eePvoPPDVwri_wdE06rEy_d3bIYQZmCF0Skt-6c3Cz324HHoaz6V4rpQ0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=S1eCFUPNQzQp0Pn00wsGl6u-QkValdGtW9kJVZ8f81ShmbyVND2FKC3XSlUJ9ay4R-02GhRkGCok6Xx272IUyRPPHAP5TS5bO8t0ivL8kAXYo6Noxew75wvdx7IxqG_dHz2XugX09XtguKA7rKIj9WpKMxqwU3a7SfpS45ZO1K89a5QwRFNhSLWgd53dNVqsAWuJ0OEf5GM9ZnkpgqFgtuRil8zb1UeKDTE3Q1Gb8qiuYgQUpUGD0k-IRA6qINkmZadwGNaP9EZsvPSRVZq_CB1R7gZA6HJeG2xxfD0y1jSvgAj1JIN60TieXxbA1sqvJ47pvIena_hk10EWMiuXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=S1eCFUPNQzQp0Pn00wsGl6u-QkValdGtW9kJVZ8f81ShmbyVND2FKC3XSlUJ9ay4R-02GhRkGCok6Xx272IUyRPPHAP5TS5bO8t0ivL8kAXYo6Noxew75wvdx7IxqG_dHz2XugX09XtguKA7rKIj9WpKMxqwU3a7SfpS45ZO1K89a5QwRFNhSLWgd53dNVqsAWuJ0OEf5GM9ZnkpgqFgtuRil8zb1UeKDTE3Q1Gb8qiuYgQUpUGD0k-IRA6qINkmZadwGNaP9EZsvPSRVZq_CB1R7gZA6HJeG2xxfD0y1jSvgAj1JIN60TieXxbA1sqvJ47pvIena_hk10EWMiuXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBUBXd00xn4F1r03KZS-ig_0DIxiNMZNM6C0gcx42oGTxbBkA32uVB5W6Te_XegZH1tKpUBm7ZQ__zcy-KFBeqvYzcPJJRUmD_BRKzeYRR82Fuonqs45BLNMEp6900nardn44rJDEjr1Om2pJfRXL6Fa3sJ7XqEwPUYyHHh0jjH0r7eG3nzsupUu_3XGti_6jp7K-9HD26oC-oMZaLVzIa512bjOItKuUFki1tpJ64GsUIhoZ1ArGTIf2iww8N0nJqZBQEQlV-oadjgRpUYNpDCsZVOUFmLlL-Bb1hv-51L3jmMloKQBVoST4Jr3xuaP55LJJa8fKVlyodJWBEnXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=qxE49R4F2gix5mwMI0nRlngukTALyXoB9Q9El_cW4AHDNcKIMCq9Y7vJevfxblos0nBJ4vFOckK0hULxuice94weGPs7VnFkpFwTBwQibTDUyFwkJ8b6QgDHmunb_G6ZIStBbPsQxJf2syyC8uazFwzk0ILwG14MmIKLP1hxZDTVVA8iwAPW41Vz6UhWQyE8eAEdG8N4aR8ue_cIzIT8muutTQjdrFOZXwzYe1x-jJtjmV5MaP8DAaOTThcsz_aO0sK-EMtN1ro9-8I_65Cp1J55Z3gKUCmoJifZ3astnnlOk08D8-hhoHgELClJrbGnvlX1i7-OOokDm4d4VPngyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=qxE49R4F2gix5mwMI0nRlngukTALyXoB9Q9El_cW4AHDNcKIMCq9Y7vJevfxblos0nBJ4vFOckK0hULxuice94weGPs7VnFkpFwTBwQibTDUyFwkJ8b6QgDHmunb_G6ZIStBbPsQxJf2syyC8uazFwzk0ILwG14MmIKLP1hxZDTVVA8iwAPW41Vz6UhWQyE8eAEdG8N4aR8ue_cIzIT8muutTQjdrFOZXwzYe1x-jJtjmV5MaP8DAaOTThcsz_aO0sK-EMtN1ro9-8I_65Cp1J55Z3gKUCmoJifZ3astnnlOk08D8-hhoHgELClJrbGnvlX1i7-OOokDm4d4VPngyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uqj_AxsDsLp3tpRqpG-MahpGTST-MWbk-SYFzQ9zM_0z6KbXOK66RtwRzDb6GPOt2bO_GBKxSKScLZkjxmRpfy9r2ndoKwc2nr4xEGMg6t2350ZaVmP21ST78ykoLm4u9NVBkiKutB4tdBuNfKdgHsPlW5Gi5lDUOH9va_8r3mEOMRt_HaTM15e0ul8wT5lzwkLOE-ZBGP1eWBkkngVf5UKfN6zubyd63MtpRGXgJiXQjWZypwh4qfXDhZgj2jGEMCK57R__9e9JC1vk6_VqZTK68aiiOcM-eHW4_Co8Wz1TaWu2ht4SWLewm9qWLID33vZcM7EWtOCCACI5NmxBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uqj_AxsDsLp3tpRqpG-MahpGTST-MWbk-SYFzQ9zM_0z6KbXOK66RtwRzDb6GPOt2bO_GBKxSKScLZkjxmRpfy9r2ndoKwc2nr4xEGMg6t2350ZaVmP21ST78ykoLm4u9NVBkiKutB4tdBuNfKdgHsPlW5Gi5lDUOH9va_8r3mEOMRt_HaTM15e0ul8wT5lzwkLOE-ZBGP1eWBkkngVf5UKfN6zubyd63MtpRGXgJiXQjWZypwh4qfXDhZgj2jGEMCK57R__9e9JC1vk6_VqZTK68aiiOcM-eHW4_Co8Wz1TaWu2ht4SWLewm9qWLID33vZcM7EWtOCCACI5NmxBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-kkVx4HEFb5vCR2nOPCQsI9gMcvvduWtMVD3Huiy8lyt6Fl29eC0VB_MoTudaw0tyXuIIv4DAx_J3jAON5eaLUPCmpud2QinaHh7mbhj61vI_Nv8UlB8brw-3KDz4YwlgOmQpnWzKfBDUOEhuNHPaeqyd_9PImnLuF7ifdKdd97Uqd0EkOaFnF4xdoQHpyitlGH_UcE6X3QmzMIq9411MflQKULe0Q4Y0RAOrqqWXuqRpu6COYqtw3E9IwYeq3Oinms1OcdxShi7IpTKDktmFFbZkLHHAJmnwLsRLc9tmEPpkVORyAXWUSjUjLCqkhgHXAgTC8HDo57J2bCSt0J5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxYtyaLfynDvhSYk-Ie_f3vl_ObMpqbHIakzeCsf-MN_0Jsxl6wXCJSOfcOKcUaHiub3RDShwojImNMbiU8B6SccGZXnMrdT3mZ9838g84sjjzQRMTqfabctrYdm7v9gCEfgzp09S74H37De8odJGDNWJrdQkTG7d_m24CORD8c2j67IxP4ShfZFJs2jB5pL-IAkpvxubm7RwMOkr85k_vkRnEsM1VNZv9bMtyUAOdlwpIqa1e6NvHnxIFZ3fIh9Rke4-2fT9z9Lu-McL6wyasV-GGyDJCccDF_euaCZrqG2v1BL0tRzS9HFYCV8C9mVB-dPEuCBkBYS7tR2cx6PJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
