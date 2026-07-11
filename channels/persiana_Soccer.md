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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 424K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 14:08:51</div>
<hr>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJe5WjnWK2BClSb6LCaZFtXzgr0x6fRaaB-2LZkU_xhwqExkkZbU6E5oEtqph4U0kbb7NkOXV5-HtDAP8Op7TKPDz7jqWMbmhnvcAxYC1vggvC7sdNBvDmCQCw3GCXNSfMDvul4HW96jkFFeaSCnNJ3xpYbcCcAGhjFj4jyAv3ktvpJW48z8oAtbWihVdzdOHkKf40AOI-26NkzqfZx0Dj6-8gdSTGQHJJTukQgfV-xyupCKybAm6Dm9a8njfzcj3IM6kZ6mpI2xpBKzH6eJVu50SP7Ct8yQigU70kSHV9YZu11VVAUEyob7nobWeVYFCciBzNmfgRYQvRunirM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf__u0qFYpuD_1-6Ohm_m9fujtjTc02TtbHq3RglO1sqyULvDgv0XIwzgZWviBKcsaQ5oa5ze6bKxJ_8J4JaMzCWHNanXblPTvkv60y2anLUkjXizwGLl_dcawKGWcZUcuAgSPAfdcMWRBra3UvgPDxKETWfa4J5wY5vQHjQAq7rkYrgvHAR9mkAnraaghKXoD_0IwG33OdEPHR-H_IX_xXGlMhQw-qkxje0JyfdelhgxTNjWY7X0zBZgqg4BbxMcXSxn5wdYKJrbREv2Be5c1QiS9HOPN9YCy47tPuyBlLUQv9r9XBj9zxuzpDU1Gf_U9e_X-GdzeK-znRxNDvp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1qFi5NPtQNL8jN0ao0sqmK7yugCS0ZaBZZAGTgAZKbW6hppXJtvLfEkEEERPdku2GYdO3-k1mVx1PXHR63VzUco1hAwVksuIW_PyNbt5sGVXUUOg_NnlLMhkrxK6QOBC4KdZImznHvpCovOahdNBxwbcd-P8-9ISItDPsOZitcsVQzweDMeByu6GZRlQ1GyFl3Xav2uhpmSfuOoE519ZfVg87ALKUWQyyFQE7hni98UhKLTJmYrMS_n97bJZe4Ltce0uEXx_J6me5ZErNdw09NH0u_46AOWVkqCGUcXDXNzNYzj6gqpKY5iBoPJBseXmxjATAiOiR9y3EUbfEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0nmQuMvx2kQmfzdz8wSQM96i1eQzPYR7Ah29IYHupKq5vr4Ymf-07n5BT0qUyfJDhCc5u8beUttlFkDlK14fR1fwNtpbAL3936pCx1QkI7iY7Y5tmIRLhH-2V-CD_XLoqnGa8MpgkfRtZAQWT-a3URUDOD0L7WqEMDNMUs0QztjtpHNj5hxERN3U8jGYjmaOqmLvdcCDiHyE_KX58rL6QaCsruwXwobO6PMoWHOt9qgQwTDil_7nKBgHIc_lQoWjbkDkjRpgpdNHNhk5p2U_DtRzbO-5hNIzzgkWe43vywVlvF6vKvzVPbklQaONHxE1AG-a7FfCXUI3N-g17Gxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmNygX_HyyvuOcMk-vvEB5T4oL18hitAJvdDvZr9vs10Qv5nmNRTAIWGP_FNzu7ABpHlraU3Hdk-MqsC9ljHV5xA_B8dXQFx7kE0oiHL9oC0W6bvt_2OvVouSdZz78E6kaICB3L0I8PidsC6zQm5fr94-KKzqCnJv_87-PhIG40ssI8QhD4lQoSb4RI0n5tGjN-TFISxutQ7vTn7JtrWrnuZncr6bxlX4WGj1fPEmTL0G8nKjypo73xBiwMnEHXp3IcfY20SMKy6zOksg-b-TXRyDIpgHyJ0vlzIbbdO6zalOwmc98heYz0iKgXahDIYp4jDRJWzK7v7Utvwj8HUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLSkupeRUMs6AzCGUEpCniTZM6vXvnQ8KFbfWps7_cft6USFWIinsOjX-5fmSpEcOKi5meSZ-fozlRiSq3OnGpeIjLdxqrXNg9N0kjNZAtk5aBE7PvwxK20M03ZIsJ7Np1Ni99xzRod73-v5U2RllbHPx2aVlXfi0dCna6Ukw9IKz3l_dCoX96HAVPcMeZlo8mkMHkO3wsT16oaqMQCRN9ilw0OB2uryA7I61ngfFk1iuXLuaUJFXLxBZhJ3jV9LOeTI6BDXQohAJdvERSJZTlxT6KneHrSdNxjx6vYSdX-qMFQ1cjD4voZ3Gft4k-ty1MLI-qr7RzC4yJTckUw5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzj97lJr9HTGwHELc57kMbO83OAmc8aJAM4IVvJzPm0AL11k6lyt7wFL7mV7whh0fUyRiLRAlqMaAtHx-D27cRHX3FXa6iZp1zYql5I3BEcMWrkvj4uHGVrisDyueMikHtfMVGHTzm-Ndj8wyanXlXJSehlR1HZbQ8kustgnYcyLFlrLrPvhi_Foe9ey_aCl4-8ZXGHKF5nMdTb4qt9uNUUw41VFUYj30U1YKaKUNAz2OAkBXZJdhhdSiEGJ_4JmzqABBTkpFR8o_mGtjyN3-G5Tn74-0VYfhe9hjK7c4vvD4AxZZHUCwOvHOn5Zjq86dO4dUO-X8fh_Cuoz7a5MWcNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=VgxzQVL95Z8TXEaHABw2ntcTHUnPUh88TGnLXR2aBLty7Tyzj7UCgCYUYtixfkUALjw-OVbgiAxDa9K-3zNJvXp07Xr64j4pTm-vMihn9LRtAxVKdPDPMqz04gG5f1k7DGlVP3S6wUFC5aFfmqesXVshsqz4bSGx2YFLm70mhwn8xMfqegEAgFp4VNeEgyz6dW7o1E_yHl9yKmSogpwJNBiGDudUQGlPVO9tUKemS6ETakEiuZsYjFTvANt8TLFx81Hy9Z_gwz5wJSJ-FNk_5PQiMetMOqe4VtlFcrtpvzni0dsB25oEMYjUM4idYU1n2J-KWxv--Vi6cztXg3tFzj97lJr9HTGwHELc57kMbO83OAmc8aJAM4IVvJzPm0AL11k6lyt7wFL7mV7whh0fUyRiLRAlqMaAtHx-D27cRHX3FXa6iZp1zYql5I3BEcMWrkvj4uHGVrisDyueMikHtfMVGHTzm-Ndj8wyanXlXJSehlR1HZbQ8kustgnYcyLFlrLrPvhi_Foe9ey_aCl4-8ZXGHKF5nMdTb4qt9uNUUw41VFUYj30U1YKaKUNAz2OAkBXZJdhhdSiEGJ_4JmzqABBTkpFR8o_mGtjyN3-G5Tn74-0VYfhe9hjK7c4vvD4AxZZHUCwOvHOn5Zjq86dO4dUO-X8fh_Cuoz7a5MWcNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpEGHOSdjo_mTJOR_awXv5vngu31nR-nS1x1bpul5Q5I4KV9NHOfgH9R1E4yBxS3DYSnKGjbiviK3yqGNbogDbdh3a9vjPheTABm6NQB5aOCJW3Ar4N8mU1l3uFo_8HG9qwRE8QTDifdkIvOlv-P19X3ErfeSNDgTD-IwIlDNMYK97RgM6z1u90edGfMQvqQdi1nb4-BXhlwyUFziUHMlW0PsOWPPh46M7O10oqdL7O8FBtR2iObyRaKhEYuxZvao799OMWpcsDE5F2KQk8b1MrfPMkOR_9kf5SP8cWDOldsqhwZWv7fdbjrnnFXCWdVxhNc3rFt54yRbvuTCNZ9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6wfVNXPsUu8TyKuWbeBXfF7PGamn07sIvjKXVBZ_dOvIpyW2d4aevsWxf7M8whoIXvTNqhnNoai9v_VcpRR215qXdXr7D4yEqGascc8PVY9m2mIksLrRqqaEebxD3_AydrrC8Ul5W5cOvRASvnm157nVHaNAl1rZNsDWp-9MTdJdF7yp70N_fDuoB8n3lc7NmxuHnDImGaFI_myqYlcKHrUQvsOvoM1D6WbvcKWAkoWAr7fBOCxP3Gh3e6T9983ecg7LM4oEmQkOMS0LceGXZkLrIzti9q5etKL9pKM-NvLiwXHPZ_sQ_ON4Z8aKWbV7XyORMCdIoy0JoDgle4gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=RVNvO4gzAytMLNafsEb273cJcjVLfHJaS3QpZj-ljaeZJTo_pOhvfpcRPKchwPBwOFXZy0YsZiBVtaVjGANJCPnK9axP54lSlH3cS_hJfWssuZcqs9hDiTtDKgHuRx7Z5CPVXUB3YsbKVvjzHlojTGNDavQcJECP-sWFYmz60akvpZKnPpWnBE-FPrmKttOhL2P8D8qSTnXuw_QzgDuL0AF3J4BfJLRGBgyKt-hoYPtb4R36ebyzob5ukgJil4RjVcL5BpPTwFHR5UBxr-kHttMxHPKkF8MhaxKEZhi5FJC46GXB2Rr8g-TLXksftXAlGws53KRWAXvcH6LoTFdyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=RVNvO4gzAytMLNafsEb273cJcjVLfHJaS3QpZj-ljaeZJTo_pOhvfpcRPKchwPBwOFXZy0YsZiBVtaVjGANJCPnK9axP54lSlH3cS_hJfWssuZcqs9hDiTtDKgHuRx7Z5CPVXUB3YsbKVvjzHlojTGNDavQcJECP-sWFYmz60akvpZKnPpWnBE-FPrmKttOhL2P8D8qSTnXuw_QzgDuL0AF3J4BfJLRGBgyKt-hoYPtb4R36ebyzob5ukgJil4RjVcL5BpPTwFHR5UBxr-kHttMxHPKkF8MhaxKEZhi5FJC46GXB2Rr8g-TLXksftXAlGws53KRWAXvcH6LoTFdyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiMPOzTfymkxhsqm6Z94bQmlsAffhLdLgJ6QwKShAbheF9xqD9Sp-JsafB69me6foS5Xb1P5iuywXGIhAm7FxtJ3bfwLwEvaJNMcby_E_5WAGi6ThMIhjNSBCANrXEudATeA8qut2fnjKgglva0syi3fdETwXRIzDVAx0iMGtK22h2tfQuTbYyBvDp4UhYopjZ67fd6ZOAuo7qaOLF1xt5ZwjDo88rtrqxCI8OxO-2EC1DlJxKjZYO3FkNJaJxdvEO2b1Ys-whec47_sEm7ktPnFrJwb-k2815wbhal6feYFPkAZxztLrfvENZSkii7fwL81o22eDuKz26jKhWiO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08az2MUJsIz5uBlB9Wj2As7wYWC9OcP-06L7S9e3mO_QEPs-cIcrcWWfC4kGWLX8URbzvbGOBjczy8PeD_GTBl2AxG0BFHuop0_7gyR3qibVP7q0BB6u9nGh3jYFZ9v18_ZqwAnYnjXdhoFCDyQjddWIdUB6gx_Z50duobQo6eyyGD0jpb9eZ2hmm7hPHsgef5sLu6ZOuw3FdUqj7JAcD5gJNwz45nhPUxvFW1gBick5nNgT8h_SilJz8Bm7THml-drobqJKosj6EpHjIyvplHC8UC_T1v0STtgF0L7N9yAIuEsS_TU6XE9j0FD6NEAs6MFhWOB7uaLO_nO-qposw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvARRLiA-7oBSC_8tRNGkzqh4dChfqL4hMwaHTpg4L9GhaPQjmCyG14WsAcW3BXFqdsxceBuXJIiLCF_ClDXFCKbkQFLgJl_5QbKaYCY5gTt0pJ4GPRYYARyONNv6jym223_QVwVm6VbSfpp44m2QEYPweozlThxCI0R2qY80F7M5A8sCYl3RACrptXOqFeYrtLKXilK7Xmvu_xLfp3G9tz7fQr-XuZ7T5kGU8B2ypqJ45R0AeYUauoSmesBfZwFjKboPDTqR1uBn5TxWnfL_nuESJw4e9WTosMiCTcuN8r01KrN6yKDYV_pppNXA2Qo92e6FiQpNHYkxxRCMzY5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rutWJ-aS4A2ppOXmT1dr1AKLIvV9Q63AxkLDNdhuLxr4aGm-Ww_rytRW4GFw9dGm6cBpiZfXgXomxqaP5OsN1MlDePzgBpx0kRbdffm3n8XuthYUbjAekkxNqEIh0v6s8R41BjEHLUQbjxrhOdpQ5QS1Dujp3CPEqak-FUHDoaHVnzSFNu0CHIrL4zUO7Ak3jZ9WfQiC1N9ZtGsibvdQIbLOTZa01Wex4xS8IjOtlnCJqujAax0CvfZ-Ep5EQXA6galqN6pDtDn_DNMRtD_QCzaJ0K29FmwJvsJVzdjZAzTfBXAu4RzgOE7nXzUn6DqeuY4H4SFM29eooc31IFgrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm4CnRcR49AB06gTq4ZNpYLZYFzefnIKGuO6iQfRZ_LICE3Jul4wj0gYtyE4RfCHtOh2LJUCBTi1seSEoX3VDS9k7kEcE3SuoXNzp2CZp56lMkd_8t4wozFyyaz2do7LEQmxlQAfIutYxkI53xQFtRV74ocozZ-Sv3wtzLQufjixHxbtLa0_ZrzDFfYaXlruU4XSG18mI-420LnB0K2YxFhwULiT30vK5_g7VWu1g6zbR2CGBKXkTWKNKi6muJGRS9jFIdeqFZ6g7dSTvtvYgyG0ZAoLvOhQNNbmLedHz3GM4vePD0bWDMMsC__XhdlW6tRt3cPYcWMYkYyO9UVaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvW6LCyxYvvJAD_Wc0c-tMwN3XA7IIHoatTAap8o9N8a0d1CIhmt3G8SMWE2Kbl3jKy-s2nHMsUebSqSA29eeDDOvW_HxaHuFztg1vDiq7PlOnHNVOwSikmgb5ub92HkheXI5gk7qv0gOSQvaNeaciI0iugBisialqZAkqb5Z_ioiGkgK6kXcRH3i4j4Bdp75QwgMwcYBGbf5lklOsxF1RxkQ7mR_S9SbGrmi63UoCFdC-z-6O114gZBKw3F5k6VJBb7etd99kAvT7onzd0bNAbtGi9BHGtzYMO0WQ0yvK2WOSYJUy8Ek4ohe71yLRZc8qeJmLN-a2dsDnjkzmyvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=DZYeXTXf_nlZBaTpaJr5c_aym8E9IqkAp_ressX9Dmu5Ve17obVZEv7UMYv4QsidRajvFdTJMw6aPc8fav8aiDSP1wceUAHGeYXEI7Arde0DA8BPKufwFve-KldZZgMGrVdgtJ-buDGIjOlhk3ExPaM7kzeeijwPEdMw_fPi7Aa4EsT8VMMlp0oOURXoHXQaOS4yDwJkA0jX2baoeHAOHzeT9pOOc1HPdXR4CccT3733IM5i2wZ1W6l2oDvBvZFMw-qBG-X6_dTgLQI6v-mi77pVijnNWjAUbDigbBwbFgJHOltHypR23X0g6U8p73vhV4dcPwy5OJ2wgU-CSwQfqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=vgO7oNQ3t97imrb-0Yv1D_wDxqR4QSFDCNhSCnlJ6JLGiO5g4GpqKho2Olqv3PjJz20MKLPS1LUr5mM5ZrhujhEnUCTP5WXKF1UOi6N9RkrfqpFta02l1Risomo_9EsP76AKBrfHGSq4q_IYEFVlC_gmbTpA5AkByWqHtEzMcIo-WlLHux-KqLB3dVyHdAIu3XRtAp64utuGQWWm3Nlb0NYxKlNMErjQPYNISnacThwTGFuvF5m1oCmQudVsGrirTcUhzoZYNyrWJ4MA5jgNV7P5t-uqBQPXLpCOpL_5yHWxFIzVNb_aD_f2zsOyh1JwQJEz8PLzwHE1rZGanOisTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWguu9UU-Ll0EyXY0O2akFAK1KJkVhjcKuKy_EwQd8yM95_jQzlt0jVXVfJqi2sVwB3GGTafhu0g1cw2dS2tYyM_VoYwKHFArgw44oauNhHE3jlhy8U4YqEU8T68bxK_xSfcD9RlvSMzt7Fg9DrxA283NXeRooI8VKGOukAXdCna-VuxZ3wC96--vDqyYIIwbiddRQ-d6K9Q3tykDqrVy5eacmbvodDyBFD6-8eFD6SBy4XK4duG2BTxstEvhMd10r0dKlUUE360m9SyCjEIFC0hCq3zcP-0gzdbzihG3YI0LKfG1o5UabzG-smgP3eLfxaF_mOxW3drRw4cfjV7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=VhzmHr4Nls9wkGaCsr5M7XTwtbDL_FdFA3mzcGPNNc1t0g_dI2ivriILkh8EzgRjZJIQFvRjf3gnll_6WpHDLfw_MAQAFgGLf1XG41t5cMwdSv3Ah8NikFHo9hRTfU_w4veO1OGJY6e-y5cq12CaKCls9YwrhGtC1KF5p6yYQZc-CFli1a2GEQOX0MgDKF-smJt5Pgld6lCH8gl_Tw-N6X1pgcupWNYwZUTwin9TMoRk7hwZlg5swkOkyBD0chxY9buPdaft--VG5cXOmFpT8U3QsDIlV9rIVlGWJ8ppv-ZhfApxGaPIL787RS8BxnJEpRARZbVO0ZJn9LrLky-kWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBuULCBCWqM9Cdpfv4HgQVlQCNN88PSeV9RJ5eFmZQdWR3ldNLRnLDMJfdOrR9WCe8hfYqP4tEoEPUiX8_7q7OTRye-w0VjAf9qzpME7LjEKHOf4Fbq_Av-ujkpMfEEripIkUGk-LedWGh43-bFcMUGaFM8lRMncBcI494-SK40kOAQ1CYX1kjiSlCL7Rd82bStx8DRlI2uGXmVZI-qofEHtkyEPtdT_qEogoixTbAzQpHR-iCNElqD1pROZZEQeXAzdifUNJvdNujbHx8JU38gjJxMwbksBdnumpJx-T4xp7NBXobMVxTBtJ70ajiseyicnOi4MW5cBwxvuJqpPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AApilATnLRxxB4UdomS7RZa4pgMOi0bqceBg8vVkVHtabsx-wfp1lz573PTCfdJUPoODkUANLlAFCf0ApU9FhmY7Bo298jbwchdwHyvYEjVoVAPNqRCy_fxXNl7nDOJSFzzDuEF8mMmbjKUGfrVIwLkhtDCI-zIrpYIjhmRQzwOjzvdpCu5He6CC0dO4IJLUStyoVMWCrndgxirGiCoO2AP-EEfxV2UswecY8EDqOGNhtgDFibcafDNz84tqXtiIgotthes3Agtdkagn9d8eC89eHNiT9VyAA3SmgNyX-Ec9tdkMi8O6p8uGZVDl--pUO7i8euvLUrjdrbt2tOrpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL4S0_FejAlcnBX4lG3FLwlZyYyCDvVNemBju8I1hFUwALYrc148zOpmlzSHAMQ1cIHt6HvO25YSDQClXvG3_LxWZNuunY3E5Qmh79aPEuimzVGSuQMfPJlblWOS6kF9QPwt0xb6ZfrAiVqYXeyMDfIAYctiL8KUZgyqMBK_1UyKtDb6fat2INqCQjBEyrM2uYi2ksY5gk5iiYelRtbVNtFd1PiUivvZlcCqDq5w5gMG_KjBEoE4QK5bumJXnGMbtuBRbM79XREu_oQDoZ0O039RhDYR48xEL-rBU6uGICJCOmOrtNFhROHmX6tKMnvW0Zf3kzZbss5XDlUGuEMvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtg3Kil6sQhDDbMsepauqQaQCzNtO2cczSsC6iyS-wYvpyFe3Fm63wEgH5j8mg-icjVcey0N_EKinUxdHlnHyKNITfF06Cd4MZB0RxzfK86e87TWfTfokbINu6MFQhD-uOgMJsGj-mTFRE7cCWJO348jsTkrEzSyTzc52hPYZdsifLOKx27nRIkVBJv1RkDSGVP0mDHQDiO6__hMHbmJpovhGaXhfZW2katHUmf4_o_4gOSQ-B47eA2cpgOsyJlob6LR2qlrCLgimD6T6yOfogvoT3PLgZtUFYen9_N5EqkutejX6S0XR6QpF_H4twF72xV2l24Md3ZzJNa9FBFVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKx7cqEOQtczTeqn43dSlrgWUuNyGXBzjFKEZFdzHUyA2UMzHz9T-1Q8oVj5PUtDu8lLvBmF--2t7SHXRroDei1lUZiofajMH-_CCZ8qcvlY-NLeoaEKz1_jKhMNq0SPAUB9wigPgTKdy2DghXJjkgWzKj9BSzCxfq59TqHmGlWtbrKl3z-oH_guP_vAYRJwaL5WrNK5yVeo-mwwqONrr5u7hBGpSIGlillCJxx5R0ApTglJMhuw2R2Se1qDNr59WL0shoxVZP7PVN7HhCFR8B9aM_s4PndkdDJzwV8N69eHAcS68cZDb4vM4SdOjaPX8yrWLt4dBfwpcq65T-h7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTk4D_0Z81XMHpmGa7FgFiNAn1CA1mhNwuQUcPOB1trHJV3F4jHoRsWAMBf8oU-Hu9i5rWJy18WOsDYi60CWdjnHNzEvyXUMWDWSn9fQsb44eV6FDmbIlO3e5v5yRqxZjxHyPmCM_WvDyd4H3h-ljZ6_KbfXCmqDf-9Ix1V3DOof4MSJWiE30MjV8IUTIahiP7932w3qU_HRIlqGFFs5_oBrDLdfKzbhdWklqMDJbNGWoce3L20e1zq3LkK12aXong4aTBGtfKP5wG_UL05bJDW9CvTW0_U28I7xjzSGWi_YL-AGrZrmjZgzyzjZNRPD4B2kD_tk2QP_O4_D8ijesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjYxpk1ml4XlgjHy-7eU4vneTBL9XHWpsq633avsIoPC-VR7SEH4v_L1WIkCXJL5zXaQTrheHAbgASUid4_DIz6bf6uKK0MSW5XPaJm5hqbx7ePMoS4TicH0oWddWAoOUen32zrkYuowlP-c_YTaCO6S0wv7Eknjhv6P2SAFLg3--BiYrlyitJKPpEPgsauy3JNnoQXhrsHP4Ai8S0xs5AH7veI5BcsKxFP2YScmDEtGJsivbfFxMaSjs9yrPR3yHxunvZUVTqZz0CcMYsXRPtTtYvBNFyTnh21qkRT65y8qjN5CGFbaxHsvJxUS4eBLBpKWmokXGs-Y7Aiw-KvUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrZco7pn-x421rrbnH0wQP1wcolIgr-aq4i7vSy4PUfI12FW5r3PyDNibLjf2OdsqvSDimGl_LyUgAOOCeozxjvW22AOR1c58QvTMLeA5wO5_Ly5Hl9pSN93-ZWvm3GryAMWaVq8fzavhUafsQXafo1F4VeU7GCl0cix_oIMMNOK8h7uerMRq9bZlg3RefRG5pVQdylSo4hiygVrUMiCs2WddMvmbbhEthojW3riufw02nNJ3QrSWKcULfWGsD9-A2qh0IXMC4Rzc_rLfm3WfcU6e7FjWahMeihSuQbozBRAjJ6YjVkD51AJy3EWv5d32f2emd0hf-fuI2w6MehLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb5n_ZOmAJk6EOhvPK5n_3FFZTl11CIvP7g1lnEAk-vS2nPBA6T2yxN4J-7grUnBw0aDN7tz1RhlQ_0mf-XKK1QNF9jzsVlW6gOnX3g9x5_KslYJuQ8YLOQG99w3rroGak46zqNnRz5vgZuW7Vioq6FnxEuD3UFNawt7Q5xDGC5JiySmyKfRoWkJhUyzN6ZEYzghfgy35hNulv8rb1DBDMrjvAp06p9KiIt7Z3b5dAEx3iq1nTbON7s1qsPhKELN-KuT9b1buFyae7m2Urk5AoFeIQ9eFDiDxiPmdB5dKPF1PsKAisQwn7bxcXpQ49NPqeUOvzND124Qi0s_JToC4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSAogASS0mEqgEPTBlNqXdlp2ghyMw3aVoMQ1M94-i3j0LlcHwz70vmnNpGq54fSmTJUa9yLDaraVfO2R_TXDFWiDLWv6b812XC_2gqDvS5Cp3nTXeytbfPH0BsGiQFtwaC6bf98xifcSJSdPIm1lR23DPA80OwpFyHUXH4UU3-xG77gdfb5xyoxjShKwr8euyioXqo3blUkQtpqxzJ7DFSfUMsNVvjXcMk-EPZUsMxP71d1wYPBfvBfK4s9AL19iM2B5paqnBB782g3F9hssyXhLS0b89yUaRDzEAlnOaS-vj1XoMCp2Ch_hiRBp2b5Nb9aanGlQiOE5DHpr4pcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1V3l8pawEiA-mt9vt-49rxIBeSOu_t_ifxMHtwuZ5FwhOqkHTwysyuAaPotiu6PG2re-c5X1IWrznCm8oVKxBSGRUV4Gr1R2ivjWK6lfmDx6ohOsh05sRYcNIznY1JIB0z6QGMMqD2bCKgkmXf0juDHzsBCOMwlnt9ghQszLbDOnsjyb5jKJ2hwy2dldhjH9snqAN3AlkJj0l-ODiOYz_mSQEmAMA-DM3bapI-CjzCEMp8b2BrpS3UyhQSgbfjVOnMOPGlZskTMGr_Siv9yNdOzqqrCJBpr-ADspmchKtwIMjfJNUA9WV_9JmAH8t2DlS2liBGa912UwTA__urynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzAthHpWJY3GXLWy1o78-BznlTzq19BI8FRx1roDrrmCcCN6bG8-fY5RnR8Q7KEhMOdjD8uF6ea6d7v9UuBt_qj8WAijGZZ0nsQ4nxJAt8kPM57SRUQDfiKmotq1FehbRovJqNtR7704cMzSI4Fo0Wx0ASQvkvl9vaTzkV12XCiwi2MzxmHRRwTXYw5GbGP6LxIcQeS-GF8TIvX6CJGXENP1XPKOOAawSeqRhQdcxZ1shKKdy_kxMWZl1Hn4YtzbAJ1caNIIB1pe6xCu8xcZWggFc2_PmbUAQcNIuew-IDsbzBr_77C1hpf2GjskUr3SygTQ7MN0bZjQq7Pu_AT-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck1LfHmMYanW17WWOb71gpQfy1Cv5ObD_9tiMWAjA6ersQVpBv8saZeo34wi4QkYMXgE_hpSYEfRQrzy2Dqwti6TL6KCU6VndmbaGeLu8PPLm9Y1gpFh91dmE8bLm2E9fwJpKG7UtanMh9h_B4mI3hK-BsK1j3E1Dwo2NdWg6SokMfT-OkmZKseEV7fDYi1t7at78bN4RoS-VZX5nV4OREp7Q-Z7cXBMJ3fHJVJJumtGYMmWrGH4SJR1SvWx1w4p7S2y8vKAcLREP4Gf6L292Sj7xK_hoRX83PSv1x8fgjyQkNPPlFHF_RxtFxY3gr6OrVYKI-YBT6ScZjn3bE0QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxtO26BcCoVzUsKCMNng22nOIi-0hIYrhD3YzbrSrPFTqPbVJkojiC6hLxgxZThkRVOUIoQG9HxJ6-gPO8A1BxHaiXb5hfVjY1fNVqCb5fGRTLSXw_oj4LieBdAwxLliCij3Vl13CST98TR5va4kcac2qEVAtAgjXXeUd4RQv71liaTX7TgTeMWJJIdVq3uoR6OgS7BUUrW65y0SUPxgTJweCD4wyXkMXOQpQmhul2EyVFhSvufeQS6bcjRrNdSKqMbsfGuFhAa20K6w-SetEQKkuSz2qYX8LCsc3EfiwpoIS4Lxuvlr8e0udtiwbcgGC1CN6DVGc390I_pjYUwKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwZP_6OJ5h5GRtlMV_uCaW7c_nWzJZC6dk50r6mPNwj4tOnmsPrf8vsVo9fcrV8TQ3O4yNqq8KSEtOe3PR5J33tdN8U5dLwTsJlY1hEehGPT8M5b9fLn2NtmaOGJDKvxQySfrj7H4Y5hBM0p6ejmWD1BFy4whq02JMagGyPPiaESxOR3nXFvl1S8wQ8shHMhBbo2oRJlys4GjYMLWUAEuJgdKN3thqUi9wsOaTbqKo-08GSrrR7Kbv4Iqv1If8eaWkTei6-7EXIG-dBZunN-fmKqa_-HfnkBVpJ2MlDPILzUy7mDwyUgdFjqm1S84DgO9DOnsfecibZDAjmcRwdAmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDotMYbJ5vcfRaaxGWxozpi99SMW59UZN4W_TqpMarBdUImWHsFhNFRt4Aavn0ggwBo080FLmSW4WiN7FYU84p0vOTNvuMw__rqNUggDoEog8kHWVCfZ36-OCbQnWK5-OSyTY47WyP_v7z5FbWfHRoA63qm3AU1ftVC_e_cJr5jmbJE0vX4Cs6udN2sSrcQw9R_ywYFYNJf_aTW4H3Obq6LsRSxp8aO3dP1awvtZI-_s9q1pz7qXoEDGTh8A_UIgnWl9EtRj6mj295xTdr2R_ioGSQFTRvuhz3sqYWDf0j_RK05wopgxbNuzA3lbUMEOR1Hhj7VfyKRQ1XOEUBHdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwhY8qo2FT20YLbpvG_fIkc2a_9pRuqGXDBqCsIW8TVHyL0IwpgxBDBJrBQ2ewzINSH079kbfbfII2Se_W_gvYyTYLkG9BKj7ChlrIeuYEsE1ESoQVSwV9XpoAPBtuzey7HNdW_Di9krDaXVzwkKfKb7LeOvIsdT82DUuudG-T7xttpe_qp-35OYVaUVTmonau2fEuDnjKQXyRhYzxUhZUcGTuQyki-S_J9JHb8rV_12cE3o_qwwQ-oXrJjGn0ogIgkpbdwTVLq5-Qh138H3cBv04CjxH0ajvdku_QW0BS710tv9O4RlIh5RLbaQwj0lZCBxaXTSYclvii9XMD010w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCHDTKthkIQol19ZURZcG37jtWG5ZKpZQAK86N9MdIo3R9QfnXCUbLs54aTm2v9Y6BSeZbVHcpDuE2tf5t0VcZAVauENC785mVN14fml5lM6hwvUjfMleyAyvvbh4H0zcm0n8ARVJjrho9_NAjAwoD-qOQPpM1ckhDOxSQGIEYsUkrAeGeZoKEV3-h_w1a7S5LyjEzU_yldXm9_vWD0-URg4aIBmt7nZfZgOaZJqZwHifZkOW-oicfWxEzfNl2NNSM4hY6o01NZcJJu7c7VP4sB5Y79TLfArlWhZLsMhMuu8EKBU5JJWgQkF5i_UBP0DjIxw9vaziTUwDAuY8ceq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgUdAMwhLjoNBMFQbRV6l4nuMLMTggCJybvrLW1trBGBjUFaGVq5wBmHGulQ69e4xE73hv2o8CwcUYslOEx6dOR86LA9lQV662etO8aYSLGXNFnAlPoZ77RPrRZ5Q-xoTwtULwAAeyldJK3YyyXtEee5SfE2DJb_4_RUN6PKDeTG8ZCjldnJJnIh3FU1EbK7-h3wBAycXJNM-BztcUhOG-vlc1xyjP0FUURYOCiatTtGpPfndi5jLQbKgB5Z8OwFrBdnMApGTzGgiTKWRoVeRa5pHPWc5tCUjTwIKoDZY-E65y5iaTHHUjZ66giO_kgPS8sMOZTYmVeu5-DPEIOWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5wjlaRZV9l2cgh1KyDWaJZX7vwaQM1feVgO3BwTXFRCYQ7Z_42QzHbbwsMRTejsC06uH6U8qwEvaGWD6GrXVB2ORp8pgziRrqT04CT8NTFJwagCmTKfN6J2X-_3d6hU2fGb_WG4UnG0r6GzoKmyosf6uKHSi7C5CG-kUK6r8VvIwEXzrY6RWVAkd5tigPLa4Ahl2dl4VpPcf6yLbuxK4GPol9fpUAy1SeZMdgv1i7RQmB8vlxVx0L86XJyGOy8R3qaBTZhnlbROQse63NX1oQ3aLGb3qh_KY3Z6lOE50Q-CM1CaWcLejxYE1qv5CWVUGv9x-EbqxpPgvv8_95EFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_8Q9Nj5uql6oYlvTp6kNmqg_zU7fH2WV4x6Ek1ltTQqUF_FcF0KPgnesTnJeBs61lX4LOh33UQLFl1NV3sJvOpVl7gE5uNcAArpMTnqdy0VabmISAK-y3GQxyPpuMYjT-D03XqxV2ek0UEE3e4DsIczrL9SyxzLvbbzHKS7zbGvL9ctRX_aV7npbxE7oEmC6s7xBPIdHB4kiAWGxC-FMqBGIvoWTLScBE5j43rsxa-XJADzRWyLNBxRRips91E3qUE2im4JsswnKjzkol_KXsKz6i3vaIL_6-pyUD1STNDGvzJkWheqfPFGyWthfvIR0nrIc-yieJ6EB3f-aynLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4o7KbDK_qn1jM0OBO7g04P--mhA3Iud4o8sp0cs9_qM0VNI5Sxe5Oohtqe2M1ihxEZLjydJQLUYpABeFme3uqHcyeVikYIQ5yRmTZYO3ZI7Ino0CzUaSE5wuYkbDN6HIB8cU3T_IUTAnTLcO0lQcGuS6XH0jwCF7Jb_3fhM6DyFV_Ze8ZgwRArQLFssqrq74fRh_jjIBKfB3TC9hhYP2KLO1jj6Uv0ijwjH1CCT7vmK4gL_wefxEjS0aTCYWqiuPTgX70Icg0EIXCASDTdSryafjtU0v3NdA1AiZSUpMTNhilHPyYY7A5v8XJFj6c359yCUWlrWpBNm2Mh9lLs20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCtCjOebgR_8Z1iR-Abhm4sLKDjNUHulNz6t2T0hAfj41EIEIxHQaSgU2EQ5Ge50h9ud1jdIhZPOw2t4rZPlSwZHIjoS9-8ESC9LknIbnxVCcjIK3OGgyg222SBalcFJyjuR8GRFX11un69_dTm9ZQ4HsS1K92ioq3BgAvSi9OIj4HElIJH1TpdJf5zCaUqM-hYCzQkelj1x9CZvLpjTqJnC7x1BgxHRr452ASwwjC7LFa9VBqovErF5tMY9e9etRzSpTJgzy9jlpVS1cZjId3a62HWcfO9onIqlN7eTjDcTKHTqedXaSnQlXM1dCJeQ3UizVqEdXDYUpOkxv1pAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwQqGXUggNe2_6VsgvTt5NGrxvvokocIEUhhuUGnGPjIvs3bIidpgyIIqqq-EsmHUariO1iTMkP-lTF6z_b_HWMFaL71vShQe81tOCr6ae2K5bQbuHwpBtrYGvHyIFAH7fRzy2eJ9ppirM7pCdpidDKhFd1VVWnpdvXPgTnEu_bUsliLmz5xkjk8lJrFoB_f99iiqswhkyXkQ7HCk7wxcdm7y08r0n05aU7URHEyyLcACSZVn6Q3HI8DB3TJKPNlEV0290AUICaHdNzLL7FuxKsLLZfFWZlzNNezLWEDrRFyZ21GT3dKs-pR2iQyXAQYLgk1LNFQmaRD7oiQtA8TvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6sYIzwlxQ5tSTcis4GhgI4xEqxdmzx06G1zG_pIuBo0PAiGx90IhNtSw2vR8mK7bS-OMGYkzE5dvJ7XQVfILTC5SC2Cq5h6o1CzaW5Mix62Ln1ZXqDImA8ZXS7CURGhpWC7rYXZjUCXR862XASfHKuPi7fIH9ubhlMsnYWCgUg_PvUaExhePyd8qfkApVvrlemFvMpcWK2fKH5njbdk_qDajef6P7lLvWqHFnrJPUnhCb3ioEI2j9hQgf-KqJJqT-VjGsaDsCt8o9mZYM6zzEGGqP3VDYJfVNroOPsVZLx3dLM6N9dAJfliNiO8fnfrqOJjdff4WiJZQ6dC34OCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=NVXxf-ZmVaS1U5BRCrSl9Lx2IV4uIS6xv1qKDcfk2dC3KVw9cFXnOwqxKvmo83DBCYp7psUPXRe1Yywi1W5GO7ipEwO0G_WCYV60URuk4BC14owPH4ytomeTAioA9erhyRbgFTaBWAtq_ln9N4j3_LaHXufNJ6Atr-h_C68D8ITjkDPc60uiLhfGhWa8ve72c8eSX9AdlMyesHqGHFc7EXkbmgQw5ILRR7bKQicd5LyW-HE29fjX80VXqEPawohtD108XJqog7B_zpiBD0c_C6PzfqwwTF5_m6qkyoJIQ_i7EuHe0o__pA6cajHyxTA63tbLojy0zYqiGxIYHgGLug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=NVXxf-ZmVaS1U5BRCrSl9Lx2IV4uIS6xv1qKDcfk2dC3KVw9cFXnOwqxKvmo83DBCYp7psUPXRe1Yywi1W5GO7ipEwO0G_WCYV60URuk4BC14owPH4ytomeTAioA9erhyRbgFTaBWAtq_ln9N4j3_LaHXufNJ6Atr-h_C68D8ITjkDPc60uiLhfGhWa8ve72c8eSX9AdlMyesHqGHFc7EXkbmgQw5ILRR7bKQicd5LyW-HE29fjX80VXqEPawohtD108XJqog7B_zpiBD0c_C6PzfqwwTF5_m6qkyoJIQ_i7EuHe0o__pA6cajHyxTA63tbLojy0zYqiGxIYHgGLug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZfIodcdVXJBs_lzNEpT36OMnwbNLsaVvqToRK98fo5laur0TVzoqNisaAXkeUiOHR_5BkfjRZTc_XkxVWN7mZjZ6LNr9au5Rrs38DCRZYo_nrmixIC1VM1V9H0YtnkMil8oWFp1okq2YEXCDJgb4hVqBg1pVgDs9S6ajTPTbN7mnu-VxCTknw00jMvezw5voO0-u9Toi3zfnzp4fHIxXSiDpdDFKaMSCjO4VCpnVCCetarel9oeoibkFbAc3YXaXNR0ew69slfAS177tRdRxJ_uGRcCzLP-EDzcxanqpbYARPBes4kXa-PQXMjLd6gKaUsWLvKfTrwpqDPcbLBfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdBJQPY2_LF8VMzLOFkRenkwHvVWjC4sp1eOhTQ-jsluwWEWp9v3dhN2MUqc7dy5UPwQOcoprCiee3mN1PdgKa8GGOrEjDvdLQ_djOlsaEtVsnmK-eX8iDW8QY8kCpPEtR81bFrq0bUaHqsxbCINQusTWdUaNx1drTpi8bRYNXdWcoqctgicaM3VK0er25SOSk8QjOgSOSTT8vu7Mq0iFAZYkZ_bskgIyBgQdGgRuLWvSqdCAKndnMOn2UZS-fs2CDfF5B7cGBfM5jvZvfuaercJWkmsiFo6SwYH2FcmyO1097vDtc13jEnAlBlk8YV4iWVLjQP0MBZQafl3_ZCUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngNpNF0qx-PfoSejscQSwX5k2YFK90Kll__uf0rjU8slGyZUFT6yzZWY2X_jaQNpHfV_A0OFbCfzBeYr757VkrBpDZqufSj8dJ-E7D7tCtD2b3aoFR7R2QbgiDZAGYu0y8hM5w_DuSjbrKG-5WFfd_nSh6HRJEFNfZMwbVeYqlif4DB_fTLh5FIscUmkDyS12Xk0OSTwP-uhi6lh65FreDeKHHs2-Qwx0gjWrFU6CZuwtz6FwLGURv7qC-9xzSDvbcturkDHDOEzualvBkYu4zQExmr3K89uhY15rAvMO52j3y-cF34Uj8s9oyA8Wrc0ebwx3PqHC402d-K8Peys6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN-0n3FX4ilrV5Iss0dyJTNNL5BR-LYW_swIBbBnRyJCvloBX3ucl_W31Nml4nY4_36LA_W0qH6R1fiOVEH8EjV-7YkmIGx09WFw5Cq04Or5CgdpWLKtegsuIy9asUw5iIKBezjRERcVTju8mLO69AXv3I0M3G5WHpaDLbQ7l0JhlXDe0tLFBA9_xzBiRpsHXK7Mmc6X3oL7G_zhXIWomIIrXKLrIVjT_9aLf6t8B5PKmAHNldHF4l4DtEapnGQfIx5k52qLbmwwH92z0CD0oot6vKjTyYxtL6m3DlYiMfe9otupEHCraoMLBMUOV8JNvACLMRVnctrOm1NrzVS3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxu_jiI2BqhoFWnUn4JZSiYuV3rQKP9ZQoZThPYOJht57KfT3b1cYU2HvxjzgPvC5zIKuXxeioKOwYD2wlKRwvgJySc9pTI9Nfl1lWcTgRW8HepcRNaCKRfVqQ5GJqquHGMacuwx_DMferOoDde8F2BYvaKw2ftkmnYh72n4IK7ukngWIE2dLygiD5btb7QBQmCsP_fySvoqbvHA0iMa_AHLMkLdiCjsvv8TY1iMgpsG1g-Icrih_uQF2ldNrOjnwq2irAN--7nzKYHcE0iqHXZIHcxX8ddf60I1NgM4Fi76pi9bOcgEM3QL0zEDzB0EdR32jOkIUPVPI5O32Ev57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prFDZMk-mr_QIZncHc7oKSUbq4Toq0D3XAQoz21Hhga_EISNMMI2eHhYIqjI3vbw9kioCp-oaTYND7vZpvs3szhI_PpgHKAhSzLhNLJMVDQO7x1M7BxUAaLUmRI-GnISlUJx1B8l1wEJCpM9XxI_vcpceBLPzu-VCdFDVtqfLj1jDLD027T9NZEYSimQkO_0R9wXNSkTT9VoVe6OMgVG21BaOofEg3VrtqmdEHDjCovBiO5qFIs5UbJdXxyl22MAbCc9FWjl4X8gMFekDr9dMzMaJSHACRJ3-QPlsDeejQLgSMbo0jnnUR7C4OxANL2plLvNxqa5jw9KCaAxNM-EMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_wuwT5UeoiyAqoi-3akQsh9-64XutVkAn6lUCINNvaiQDkG1K4YjX1Ncsfir4nJsZv_CbxnMQCOYvnRqJxmkok20Nx1LT50QTBSjh4x48Qu1-Isv7b7fn8JQZ2_SxW5iGkY0vI43bd76ru769pUESblimGLYNwLTT6x_E9POq2s484Q3i9gRs2kKTBGCh28w5jmmSRvb2GlxqOmwHxuk1G7CoUI6CMDT9CBxBL17IRRxDhn8F7DFI25j9zHPWAqkCTdpZVKZNAWxGl68zN8iT-S86SYMnl4BT1ZchOUjiiiIqM-3IppZPnLBEemr2XzMekVq0CXu3vOwwkgqAGQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXctfAL-o5r6Ljhm2-EYGGr1F8OYOSB-t-vfZe_UGLMnNqX9KZPSoS6-UkyVOkMHnFd2f0dbkirAvDXXudoV3wYI-W4E1dgQsIwrAfFLhpehicflO-vxywa6k_jlNSW-WRUOG-1TRGjsNMKWOadV4LTFbjp9cGsnQQQqeBsdScfAQ3D1vT2WA-XpeTHYVQc2-Q1d8sKZvM087SwXDkuU-R8FFhQmiROTVecitIErp0qTeDa_jcpedSD0MzpQoZ8KpIQG5pZ-qZqLnOOd9i0g30cTA47y2u-JEJD0MqKKHsl98YWjyw026AuCErL7SSdax8ZNc2BNA0Qk82G1G0yEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbahGHEowLcZk9s2QWE80WHx3xe5OQL83rG9tIok8uU6dzZitv4Q1JCoicm_hFuLbWdqHUUHr8RQnxBTzETR-eaU6IrM00lv6moixc_MQG2Cj5hCbmkPUHU_G3HbtuGK3yY87vhqfIST0D8sjjoD708lqp76fmVIM_Tl7a7yAY-23KXCDNIBap4duW7HhfMlItwqu1ZcneUAQ6uS0JhJ8RSq6191A41Qa4_c7v-j91BkZoZ9Rb6XQ5D5cjmMV9b3bnKNNT4e2JngUY8rsVlNEQxW6URYXRCLIGR4d9SA7Zm1GFodLQApkvCKyREBoPdopPD-fMKc1X8yj4NikU-vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfsc8t6_RjlzE66363wsm2l1I8Z8mlN1vDadUxoNxUttXjlKEDagG435gPK_blEEfcEAbSmGD3Hw7x12ioap5jf8M2lH7fXMIUIQYJ8y3ZA9GvseblO4XrfSXVpIaiESH2DcK8Y2NGup5AUy4hAhSgDUB222yQN_l-2GBWHXQAMTqDFNnTxQj9TvQnncKVHGu0jP35J8Ia2sEOebyqbrup-U9bO3twbagElAo063fVeMD5gzAeaDvHRNomtlP8yy4tlIe2wgx6OTOsYiNcufPnj6g1z4dqisidbsyr27izJRn6xkN2pKxeB7E9asx79Hfl1mE2g7dwIOM5UfGxRIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThocRQpP4NoYkqCRF5RW5W_qYTZL-fszZcrCErzatzYE7HN1uCEsl5XSFu8EQZainZbpRj_9RaEK44RG0VromqAfNs82U-qp5E77Tb9QUoIRj1F4jRY_6DJ8RX6IHot7imYVF5cwtLffrEz5sx1qXFLChMakFTQSDlgIibJ_9_T1Y4_3ppCRKOZHMTRZqMvLuINWxDHe43wLrW6qDQpbpI-TbFxI5e6C7qdAZtMo94ICeUbx3D_ZQNrWi5syglrJdGF83uxQ99pK2qDILVsl6AduFQbWOeAqEHcleJ5y2LPpoLt--9eF9vMa63kP9nmD9JH_W6QECH2zUeSXov03_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6_EfLff5MSm9mJ7XPtYKmFf-dvOeI6za1-wgWz9fJU7P2gQ6xcOjFIekCbDjaKfitaafIyDb726HqqBfRE7rWP5NJnxdW3KItXKnO-iSTiAggFB15Rp-L_qIMiJ3oJaQE-bl6yL94jcTy1z6hQ1A0VN29AQ1nBHoAIGwliKA3s2kYk9IcGf1hBp62UUq764SQawkmS9f2JauP_J51puCeUJuqhAsUu08Ypw8TxL99YG1OmaBr0caW1ABvVaHj0eNClVNRKeSjbAJIrgvgppq8nPW3PjF0vMMGRmXxF-SN8LNmtZ_huNgIWy3fYiZsz4R9oPpUpM--Ew2mIGzl_Ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s94aZf2pN808S5LgBQTnKXZ1lA7WxJ-rRQOdKw9hnBeK9eIkyDIdUkjYQCQn6uFz8gG3S_ctM6NYN7AX6ls0gaQs6VjyDJY7Q6wJDlwB5qiq_QLOl-1j7jJUKmk6ENDeMf6a4zQkWfg4_MaPN2CKbZJj5Geinex1tnKKp-cMXWn94n977CPO2pq3Y8LLJjg5FPkJAOoRC-6ItSO7GyOmAPcj5Il-ZT8emG0sRp2-xkos6Jn44AtXvPjiwQRywFh5VexQn7IUsbVZfuTdHUB1YPQ1yTA1A4ZDKftvTBY4CEdwXkM1_4uzuWQGYvSkNSA9a0oiks1qc3AGLvSaudAXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=MrEz5rrK8zIxZCjfvMkHfXbAxK64mUn2sagjEvuwC0bk9U1QmBkRQ146-YdZAzntj_4zRdXcYhoqzUDJfyrL37xZPWqQyaVq861-7ze3cBfyeN9gfvXhzKovv7yfqnDxKPMrNzAdmf2eu0mJU0EDPnZchsdEUXmHQkIy9qn6wq7xL1zLsajTu-CdbcRIX7nXG_O42oHh2pPYmJYqNslCzogvHKxk0C_RVy9TNcDDlYNWCVX2YK87ktjjyrKYNo2RXPsTa73kzJWuNu9DepR9Nxnr4ZQ8RNk5NbN7rVWYpMxG5-Kiqxqt4FQrNYgzeJOexovJmgOhgO1g3TlwVwaQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=MrEz5rrK8zIxZCjfvMkHfXbAxK64mUn2sagjEvuwC0bk9U1QmBkRQ146-YdZAzntj_4zRdXcYhoqzUDJfyrL37xZPWqQyaVq861-7ze3cBfyeN9gfvXhzKovv7yfqnDxKPMrNzAdmf2eu0mJU0EDPnZchsdEUXmHQkIy9qn6wq7xL1zLsajTu-CdbcRIX7nXG_O42oHh2pPYmJYqNslCzogvHKxk0C_RVy9TNcDDlYNWCVX2YK87ktjjyrKYNo2RXPsTa73kzJWuNu9DepR9Nxnr4ZQ8RNk5NbN7rVWYpMxG5-Kiqxqt4FQrNYgzeJOexovJmgOhgO1g3TlwVwaQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=Ov4pdBIOmgOyjpHBvSfpL4y9L2wEk5hE1F2gcpT-BNCYSKrj5NF56gc68OAZsfvZ5ja_QBMk4VUSoT5xWOhwEj3CyWwsESe1C43CySt8_HsItgc69838vkjywTzxwuZOokfsUL7TkJS2g5eqVkGqOw5bFPqZGscG5QI3Zii4NIU_mmQh5k_4JeHoNV98GZFVxfn8OcQ92RmlPAEg3aRjqGg8uVs5Xo4FQEd3KDtVU72JtiluPk-h2Q1UmaMGWo60PVqx96cg6JxbQEUU9pnT6bs8AJUlXoSXIwq_JOjfWW-fEpMa6_oEny8SkbEevH1Y5OBptlC_XKQ-tIXnRCKnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=Ov4pdBIOmgOyjpHBvSfpL4y9L2wEk5hE1F2gcpT-BNCYSKrj5NF56gc68OAZsfvZ5ja_QBMk4VUSoT5xWOhwEj3CyWwsESe1C43CySt8_HsItgc69838vkjywTzxwuZOokfsUL7TkJS2g5eqVkGqOw5bFPqZGscG5QI3Zii4NIU_mmQh5k_4JeHoNV98GZFVxfn8OcQ92RmlPAEg3aRjqGg8uVs5Xo4FQEd3KDtVU72JtiluPk-h2Q1UmaMGWo60PVqx96cg6JxbQEUU9pnT6bs8AJUlXoSXIwq_JOjfWW-fEpMa6_oEny8SkbEevH1Y5OBptlC_XKQ-tIXnRCKnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG15p3VhxDS3xnBFCpJI5_7rbSivigncRTy5tY2O60t99Q1t6HFjeco_dYknT2AhKcyfgMWmnwj6nrbA8cTCLJ4fJoPshRfVVUkKt3PRgayinxq6b7ocRMll6Kzdvw3J2K82JSRUQkQ8R01G_1qMzdL2XSFYI65ISkJNnqp1wsmdZEGIdPTCAOnDYH4Cdplq9OevambWAjFnHh_j9m5tPzeCN5Aonc2yjRGGpGjXlTSwPNxpL9ErBnF-CDHJY8jgHe4EMvjxlPH9geWXkJdVX-50lM1HhabQFEf5buXEmthn-V5ozSdLDer-cplJS475KHrg_pAYkxs_U43m84DuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-ZsGVTrZZX--eeXCLk9sVvx-KWJn5fMdE1nSBGqnd4GgCi1RzpRsLLDdx2FzBr4GQfUj_RoZTUPNr12Ar5RZDmmSc2Cv0hiBgskSRdRbiqfAVcruI92067rWeUBi53yUkv86CQNMsRcQ8NqqhMgKIphQAvnmNNnnS0FVOwSDRLjvuw6Jzi4sacqOD3qo1JHFE9y2fTmTpUCMlesFv4cOupfybTJdmDjHMK0uzxLHthijGMy0iG0PgjG3ZHcazBjYyqWqmiEJ04tFekqFqMC10mBFPa4v-N3OC_OOOiQ9nry_of1hQTp_YyZA6LMHXvLQRTXm7USnPRS_pKKn7kV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxjQNXaLoUDZVbn5jqArvpthR2c2fpMbDStwRxmW8e4pm_KFsebk23kGEctxWw_hYllfk2Gs4aHu0U91K-06Aq63xRArYRoNceMcKYQLetngSODBOYFdLkP7ILMkn0gF3FkmlHoL6z6Wco_InvRrN4HV18oyzcqeM_e9293hNYj2QnchJNAptrmDZ_a7VeD-W-FhUbjz8jaNJB0YVWVeKaj9TWso3ApgExSvhgx4tihEq45F7mAzY-t9MuKiY8d46W2p3926WmYfzjA6auvbIkLey5Hy3Wg2cz9cD-UeATknvaMBQO4qa4LeJcLh2DAZ85kERkcVL1JdDwAiqQMqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5TFWkv96T2v9jKAKoOviAx0tkZtlHsCWVpxKYVko1osvb-6czi29_tti6KU5WGQp16rny3ypsFHb7Zge1ib1nUqJiz8jAKlH3N3VwW7ztCiUse5n6THt2ykTpu7weAOi4YLk5fCrsJOR4Yi1b97f0dfV-WpxcM8_7DROUNnsIoNubdlTSKeZl8sSTI3h01MEfbBDRsusu5ePFtimsQx7wtTVo-tz0D5rXAtSGwaBT3_rRUFOesPlhwSPcIbSnaahLwfCV3zKi6h7OedFXuYj_PhpO6_vcx0T8WyPI0eyaDUW-00J5IGtjLCyppCChMn1FLcfxBIiouD-aMfpo_H5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqmYXMNjUEbosfN-bxP_1pUg9ZSznZUNtUt79wY0zv-HXlJzVo3bQ3wDJ4yeppzQvLZh2vNsPfsGopVLxFv1PyDcoyrU0wAfGYd-zli0DK9MAoZqCc3v8EUlZYbS1E4sXrQLfs6XVOdtHpM3uSR-J-zqVkmABigIMicwvdNfZqb8qcpxJAaakUDYnblcqPM5VoDBHO1r9wF5SPNKMMvy2ER4xp70WNYgBBlLv-a9q2-jbSAkHm0M3ttEeZubOMXpgFtR4Gizs9wCnFQc273IYv_KGq11zxvQeOup-VUEEyD43tfaBRiOoNA0rshtyrkyfCkjjxTzAEEBjJM5Bvh7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUmMd006zLiB7ae-7vvAzJcGDCC5RRRKu2n4tB_WxtKNzhxr_bl2pu_NWoTZoe3TsE_6elfKkE5m15gXqQ55wolzKaJMqlwLPaqQ37YK9yJx6P8P4gO4fIXIUayUuKAjbKum8sXnDLyGroOWo_r8TwqE-K-jjS-3rO9BTr0ADOOCGa3VbcnyD6Xpd7POXNtaHn85OPlYf7y7EF3jVJUNxZMhLd1bxmt9yUYTiio8O6yrVfiNE11_wFkkxgsCXE5pircX-B-YCNPds5GEaeAkmnXtuIiw32CBVqk1l6ye61HsGaWdHTf9_jndBtnNjKqZPPAsOA8bZW3V0KAUMyb_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmgU4iKaeHkb_HWPggBEGvNYU9hfM0THCPiuv5pnw94RBM8mmUY_52jYfaOtRzeuujU5JbgGRb7b0tnzAZo_W12i4UtH537RLnmZHt0gDMa1i3kEGS4n4EPbXPnDYwgh47z0WW7ZVucxIKid3f-gG9KdJ1i2DQjsvNS4gFnj86UcMt93IpH6kI55KFP-N7O72d55S3kXbscBctlUgcc6ipPZYjOxKOFnrwvt4z4km7XGIFTIde4TlJ6FEadoAZYiRu0SaUmFjytFSKR98bTF_ocxzC9YKoh4MMU1k-I987iKPIhGfKVjpY6Jnonr1xebdjmWp2XzKh_sRqOmz_rtbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbWCm8vEpEWpniQ55eHVAJ_GZMwXUTasgqlmyd4bX1RUfYCX78PzRkg8Z4F2ceFQca2GP_mNsjohJNa8FwEPSnvly_EyxUBLpYSHLQN-vW19yltYXyajLgHA0jkBkK5W383IH90jKb84JgxUn-7v9f2781L-O5gCvldDdr5WUEy2FC2ju1qQDG4v6rhcqP43UyASOR4WNSbliRzuszqekZI5Jx3RtpL_TqDzCRNKR9arbrOqle4a7n5sQjSEQyowTEGAt-2yAaUDH_96jw1FhlISuIalAV6GLwaWPPIDabA2U1o34jAzBAZa0qQzGwSjdg5egtQqaXKbIS10jGZVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNtO3pJtbN1JOVolEm1kgxxKSjvqZvyfZQXsMcBwXg7DsoF0WoLARoFQyhrGDJKMrWd1jERKxnyPn0EVc3ROEEpAFzjMLjsAXcUe5yz9ETOGOgi1fn6MDesaSkno59bhAk26AJq4SESx6IWO3cRd6p7_uia16woHV78capuRvHS14z0evLwdovSo81ZdANeJM9qKvuDZxjbH_BGXlapZzJF99vyElo53gSDR-jJJ6vjw-pSSdS6FrA9AMr3ecUQq0g_Oc6EKylxbv3rZYQfnMHfHH1YjbqH1N6CQBXGzFGTvd2w-jha-sjF0tdWnx4LUkO4m1IuHjEt5MHztUusTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDBCqzmwCg9OeMPku_Gsr7uWzqS6TgBSt0Zfq1Q5D0bS5dJ1Ld4RBu83vvrp1t3sVBQr7g6PmD-BM_QufvBjtJGiLhThSRek7EKy-M7VjUn1olLmFszUend43RWESSac2OcPb4yhGSVCZSqSloP_e-9oDN8Cqj9nBSwQfZkJhhLXa3Xblrz39qM3LQ3VWCpx5eC7AuNDMakQAvsX9oabn5BefwJ9OkgebZ1aS8fo9xB2BdaWCo7jS2jzfgZkP3SekZEiCF_RM-q_qopEcZNaNXbFJH21rfGbsLK3bQnCoz-NahjgUDrqZpCKk1CE2lUwRp7AMnIyz-s97naRS59KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=QbJQGbo9CC2E5dT21fzXiwhBgB4ZZVudqb6tT_DFJ5dZqWiBd5yVLkoOIJ6Kcxhhn9aBySSwDNQnrD4CZLNK15rjvbbhWHzcrTE1-0L_COoOaCs6AdR8s1CxPY8vtzJOX7t9VqHY7DOSmIqYd-5LjMJvuNUGu3Wj5rj3tU5osaNHVW0tHLdrnOdiXjLMhxqfaYE3QFGDpO_S2rMDNgg-AUbepr94VYr6QyZaB5Rp0HW31uvC0KIaCIE0s9IUCAEWgfkqb1ohlPBQjb6mKhvrxqWQYjuVjHmgou8YKpgM494kxGLTXPJ6EUgJHymnA1mQtdi815fYFF_mLmcBxJZUT0UAdrdMFg_N_4IWROY3ek1OtNk4uL0PPzj4O6zS0gYw4u57qmRZCe6TNwBPBJuVNMzgxyyemynPaygIYQK4byVf29HV-4oog4dp6JiAOJCzQ01VNy-Ivad-ViZIiCHZXzAd9961KBSqj71inFF1YXM2KdwC9tV_bNMFxawM4HQ1CdmSuZs5uc_VuAl52opp0TQ3VszYFBF7YCe7NWgP2BgBWD0d3LlrI24PYAfRhnuwhG83HiRdi2c4bab3fupxXYFMFG58NODYtR1cudtOAYA4w1N1BgyXfSXlcuaI4TM6XNM8xsejM4NU6Q03BJCcDxVfQw4aE1y_J7H5YB5whwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=QbJQGbo9CC2E5dT21fzXiwhBgB4ZZVudqb6tT_DFJ5dZqWiBd5yVLkoOIJ6Kcxhhn9aBySSwDNQnrD4CZLNK15rjvbbhWHzcrTE1-0L_COoOaCs6AdR8s1CxPY8vtzJOX7t9VqHY7DOSmIqYd-5LjMJvuNUGu3Wj5rj3tU5osaNHVW0tHLdrnOdiXjLMhxqfaYE3QFGDpO_S2rMDNgg-AUbepr94VYr6QyZaB5Rp0HW31uvC0KIaCIE0s9IUCAEWgfkqb1ohlPBQjb6mKhvrxqWQYjuVjHmgou8YKpgM494kxGLTXPJ6EUgJHymnA1mQtdi815fYFF_mLmcBxJZUT0UAdrdMFg_N_4IWROY3ek1OtNk4uL0PPzj4O6zS0gYw4u57qmRZCe6TNwBPBJuVNMzgxyyemynPaygIYQK4byVf29HV-4oog4dp6JiAOJCzQ01VNy-Ivad-ViZIiCHZXzAd9961KBSqj71inFF1YXM2KdwC9tV_bNMFxawM4HQ1CdmSuZs5uc_VuAl52opp0TQ3VszYFBF7YCe7NWgP2BgBWD0d3LlrI24PYAfRhnuwhG83HiRdi2c4bab3fupxXYFMFG58NODYtR1cudtOAYA4w1N1BgyXfSXlcuaI4TM6XNM8xsejM4NU6Q03BJCcDxVfQw4aE1y_J7H5YB5whwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2cpudXNoygJ9ua0oJQ6WNoxMV5XcU8yhnu2Ztw9n-puo1CT0L7RKnIaq10cws2s1RAwsHqovuRPECTgENDK4IKZNzxFi2_g7VXV5pND2eiyE-tPupUvF58PCvbuk1Ef5H9W4OOS-7gmZtMeDmo1ArYE-qGrtWBKHDY5wLxV8nnIdpOHac7ChEv2fHt60aX7OrH4yA4y4W5xM4hHshx-AyWlmNNMabtBnucjO3nCffQaC4HbCzUfFML2S0ACE9nIBkV31TpbKON3hTsbXodHivyAVZtWo8qJHbFjxnywbI0z5cOm7U_vtjwK2JjBDtuQyOTmQD_CuFQXW_UoHxC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooWWwLoHFYEGg5IZemoHBFIvAINIj72FFEM3XSkR7XPGZOKt6jm1RqpqrIXOZ7elf2ktxEcf4blfIxtWvqh7QscZ2L5NeGCpxY7Tm-fETptdiH5rUhuWtKmQVXMDI6prA1RrqVDLlih2NwF7kWN7Qb18s58aBnQ0Pp0e8W7hTw0O7L1P9vi0-xRbN1kdRNM8-8e1mISUHPBwqkqK9mpoq861EEeDqfe-8j7Kta-D7YcjUrQOIOnX20hymY-Gq2D5YGNY3U3qEisy84pur4f2Digr4UxCo9O_SxVyXJzkLHDXjL1umlT576FTAg7dP4FvyJ8aizwsNFWKIc8SwmA5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtDp3BIzoE1ZgTbYvmgO6e59P02MJDa16TUM3ELbO6xGok19YnxSSzazjHM-wgOs2rlN0mQdjp5oLOP-m2zlz7MvLqrxLt25e-c67ZfzQKR80mGGQq_CT3s_U9TTzJHgYAX4D6RoujInyIdnsfwlbAyzIrSSjUFP9_NpucCGqQfPYp8SSeUPKsfaT6Yd9Dqdh7RqpHXQtA60Vsn51E1bGqH8wRlmXtTrHBe2qN1pzMDWNKwAGcwoVuolQFIf1PAE9gEWSFqJohWneNgJqVW75-zKmo3AWw0fghLHulTkvexx1P0QkxXe7Pg_UCHEwZMALWNL0Z4hWp84CnXJSTmWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=hFVfWtEtFxeGhZZtXcDFG73PL6SXCaTg1-K7LfduLUmIPnzbvn_R4jX_vCSiatAUQCOn7BJlu1GaIaKlD04zZiZcEtvtVQhUB61ZOgeTCxInv1yD2JTesGmvT_1SSW1mYrfDv4X7nVoJZPZCPiDewhyvrGIRwMMLTWKAYHN-IKC0BQIj69bvT8vVbPSNEO0_8-1CsP33Xi4S1U2XtlHiJ9oOnj-ii5_KJ1qrh9ZSDZRaZrrf51g89PGM1zS_dsS0yivRZSWz0CVU36XGFrcbAwfnxZ27XEHeIj8f_Fhg1lQY-0imeodJcF-EMbAaQwVZHb1jvd1aCnLJmF3tIrBr4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=hFVfWtEtFxeGhZZtXcDFG73PL6SXCaTg1-K7LfduLUmIPnzbvn_R4jX_vCSiatAUQCOn7BJlu1GaIaKlD04zZiZcEtvtVQhUB61ZOgeTCxInv1yD2JTesGmvT_1SSW1mYrfDv4X7nVoJZPZCPiDewhyvrGIRwMMLTWKAYHN-IKC0BQIj69bvT8vVbPSNEO0_8-1CsP33Xi4S1U2XtlHiJ9oOnj-ii5_KJ1qrh9ZSDZRaZrrf51g89PGM1zS_dsS0yivRZSWz0CVU36XGFrcbAwfnxZ27XEHeIj8f_Fhg1lQY-0imeodJcF-EMbAaQwVZHb1jvd1aCnLJmF3tIrBr4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMAc5ft1CvjcEv9l6Ko11zONDJd7lnYtDBs3M5iTkZR-b-_PjEH0w7RfabYjs08e9-N16nzdYarjSRlWQvRFKMNaYXQ4rFntrA8-dOilaEoFcu4BqnyNfcPJipcItx5HqBwqBGBCs04Q75inevPk9djWs1p4GCEN8t7LdGdX3BckogNbyI9f9GVUiOohDiSIkNwHyh1AB6MnRPBKyuIL6W5LDOPXldlwPZlDP7ONmwHbLfyxs0rNKqOzaWx7CyMhWQFPiLC_LXSXdUEI3p6olhRTOUUYVce1BJRkyqYXF2jilHrbfDCBn-DiD-E6okNV53xPgRsDsuGyKUUYk75Xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_uZ08xbnpCh9YESIhvED4eWT49IK-ji1E15uV4jKE7fUuMYZItlKAHwDJyVFboUjxZD4xg_3q6HPjPvfEWTU6--gJLb66xtOLFX704y-abbswEXR8BzKczWuGyo-0_SbV9cvqqCxwv-DiQHwqy_xPrSwNiaSucv7XCfDybD_QApYKtIqYMmxr1zS9FEorh8xPaa02K0_C46MXTi31bS7ulaOpqrSmIsNMlpLz3w856rd4th16aQFJ3vSPu8RoizpjV9I8qY0Qqx8EkNRsMj-7MNM_ZQddjJ45rFylxatWhbtM3bEdhKRFCVfrRDyOPjGZpfPvnlprGhPb-xq8v-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiaPKJNDG52-OCmAh1o-DWEhAXt4q-TZKFxCoWOazv5IlkgJEXK320LZlQGK2jiQnJz_YstwFXjeV9Vlz5y2TkySXU1UjOMaWAo32eMxthZQF1fHLGd8nltWsJPfZUZVTnZacfDcsf2fU6nNEO70bJA09Hs3ZJyLv8pRUB1nWTfxSM6sUlMZQ14a3Q6hSyL9jeA5mDtc6anw69IP5NnzSbc5bs0osDWIVtEoMB9q6oxWiwXBqHd28doLH3g1olVCvFTxg5KNHjduNjiPdywnCAUN_oVe4xB6jkc5ZaKyc-q7q3OW8CDb2snsHpmOT2ToXBoXFtd3n8Pcf6_iTre53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0nmymoxL8yM-7XEgv_agR887_0k3XzNcv9rj265h4j1gkj13CGv3Z8SskpfdhvzYUIyeD5Pqdx-GGeVY23-UNQnHRkkxUV5T_h1b8CduDl1HKprnHorHTtYFQdBqEqC2VpJdb8Efp_5txFFQbgSin58GyJbgEJwsAA1tT6Nft2WHUqWspLixDwNqm1zPY1HC6axOcz5a0xRpNbKdXWHrUooIwkBjQV1-cn9jYwCbEUKbIELz4_gjM-WYmmmeHYv80BoGG6tidJOempcUC8P4rifElCkcyUv7HUIeoat7SPyfLan5E7ZaF8KWQSGe6uI4MaB6hgU4pkzOVIvbB_vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWiV9HMj3-oZMUgr_B48w_p5YqhwXuoWmApFhpi_qezPWEcIuLYE5sGpHx1mIUzIKJwzhcLBxnIwnZV3AnUi3JumlJsHENH9DpHCs1b3S3Jl1dGEzC-3ZDkukADbRgZ8P8hU0zs98kTHJrsGoF7dVD09gCRlMV4TRIe61wAz3I3dbjWJ29GmNzPFdTvZ2mcjXs-MAFpRZDj5MBA_Qq6VQ3X02WMIi2_Wq7vOM7s54719RorHHYPFd2oC3fClYje78IDGa8RjErk470PkU3piv0AMMZDGnaBRAJwtgAd9PA6TtByPaCYalMhVn7l8ZFD3OhvLOMrzDB1GpnyYPryaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9HwV1nBs9ROMY0IRT7usPDneAPitWsX8WlOgG5p_wlv3RfLyfqM1NBlvev5pcHUiMkM-b23hnn_zxZMufhCdLpeI8F0uEZxxmri99KWaXO-oc-ZBi4gLyph30I0iezxTR4ByvHQxSe02xouqZU2WQCfvRzS5nHFhRuN-hCIkL499XUXOgpmO5UoqRYO0lw_YIcKb4aSU5TN6c1Dpu0avjK-RjBOp9wqfo7bypAhKmD0qdZW4m7yZkD3syG3ThKNgqVCnOlRJxnAviLqidWjok77NzptwIdvQqandDD3fi6JfULQ9ZRT_1XXKEbYvDx5Knhbl_qg1n711-1cFr9GIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUdHphCu7btI7O_ZPc4oLS26xJjIQNoT3pMGMeNY02LtAOYse471sOK2Hc5C53D_YxZ9EG-bEcqOl437txEz2aSWDFT3VRp7La_tkIF_dkHUrDaj8oKwBBHkWli0MxqVZywFqQpzplSKPQwtH6O5jHE6Rd8U-AYhWtT6qr7chh_njtgcBFyQ6d3ix0r_6WjzArzogadNAqfu6qDL2MRcHD0IoKuj5Iz13_v8juwIp6YVc_lTCBtpqgkxhBffBtg-xtjqZxzmXmYQQ1IBCb3v6zLo2DtTEY7v7wmRUX6C0yOeTseAFTJf-Bof0KD6IwTiZJ4iyRARI2YBXLiUNorUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRWJW0ezzyppta0mRm_q8m7jTPN91lgM-nyOyKfudKcyABaHKY7JxrRZB6Px7wrHlRWysmEG1-QLuzgEIG0-izqm4KhWpIRzqHvc3KQx69g5jrM98IMCF-hjMXeIoazmCzc-biv5E4FkTzwcs9JlrdQ2v7PYI2GbuaBmIPQRhB-kWuhDjJn6yw3AhxQzw27MoYzpJMc8M5N12fL9OaTexwfwJ4eT_JeoGLOoWO7ZRg1JXyVUodY2LsbKStlfTZmaAQnMwxiEglTWdxerqYKKPO3hkljHJhPqKH7CRMFK0xrPYFHRD8iyMOqshyZCpV2s_59cQmnc80ymUK3bNqumiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAckeE-wc3-aAhdqiUxXrKtrpxGoHuoBfC5f_G2S9uBXHn4hhfFZfZiuFuyQI52d5YhjgJCOTLrZ0EVlct150qWnggvjd4cK8JUIj9nb_T1W3jyPW3mZ96f9GCLDbhu5Qrxv-g5kYALmHC6DYeMtkAoi_zPdQcbsPXDoWeR0wMgCy0MHU-hNKGNtt7cM0t0P3sW8_o1-wZIsig67aHHfkOQNL55iNFBg8V8SKgilkctN2O-Z1O3JgYNNndq1MeWPQv2jJA4jtvrfarjNH6QvJQDHFDpF6gaND40Pyc7FhMzE35W_XnHSvtZa7oc-zon5CuHHicczQkd13x4KOD6M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaW83okFrRHyPZ9vafUdWq2ZU4XS4T0595x5_PMYJShG0lVuzIogYWWzrhbj8b8qQijIkKsYpdW7Zn1JtAKt4hGiIX-FXPIF0z9GluQTjmFWiVOygyDoQXCVN0hwesjGzmh1z7sSV0YX8QVgFTy6y96EN-ErfzvWi0F9H0wRYgZgcHqJu_d097yPhPqk7B7grbU746bP8t_fO3HtAYRvNMYEuWvHU-0spVr7fg2Zy5guUS5v9UCWn-HXSuvoMc3UX1WlnO9vpNa77hzdxHl0MFHpHwdvXwpLYFtUfJ_msS5ekaUUmd47rpWmlwth3701WyRo6APdfW_ya8PaC8xY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qchba9N3SzQuTjBdjybIYyVH3-V4SwFru4UoLo2tew3vbX-5i-lFit4taDheoGKIldIFHyNCz3JWQd7JPgH_Y5Ekn_EC_kejEM7NJUr-vq9o5FSsfRlCSoG_fXQPeE18IP1ZcpY0As4aSN_wlCDgLvmyDr566i5O2vi3UMpZL2-6jKbVPVH9fKVGjQpd-jlAid1GW4DxJYhZvb9vsWMNtmfpumc0-Et20D8svtRY-Rj6LYbfjktYKuJC5gmTJQ-WFkI0-44QFK2qZRbx2yEZ9psnPd84UOmnzuFKdTxpJAMjBraQEsVDsFHLGxBenKCH6XLC3_BpcJQ6KqF9hrJl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDfWrQkF3w8RtYgHBgx1bXqh8UdnfoL6TstTF0kHyGgx4IgwnHEzUQy2mcIEJRAUj4xXfWk3-UM9W8M5QvHicCrO9xkZIf4I1nHonl1Nsq2KwAUIEz-oWzmVcztp7xOS96J9-u0zEX-ld0v3pATyWLUBxihZfj6BUz6bMI8b0rC867Kzl6ETY3a1B3NViG5Rg352ATBchiBfPIL0cHvLPERGraPg2DPjn1oOqeanKPY48mXJhVENqWlsMzJ_R03Fwh-MUSSGdTrEwW_OQwMfwZM9Ke4oDRMY86VnpktW19XKv3hHbv0epmlO7SSFkOEWQKXnZbdYHJ-G7MuMpcTxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVDYPwkfT7wvv7dtX6NdbqyKwC1WuSaSo9a77QAKXoCrtJJmoML6uxndgQbV_d9oAFAvbLrKeH2v-KtQNJBfJsnc0h_UYDYOdbaUd-jk09q1pbw7K4WPF3EBa713va7GrykzMGPJo2bdBISu8IS3SQH5V1K4QsPAs4vkPQDEV0rdYFy1FKQWJk6CXHxiEhbL6flvLFJ21IqnXK7O7tsnObmEZW2IsfYCklshYgycm4v8lw8CWWcpUMBwbM3GQFfnZXADKg7VAi68w6cZwtPcNzdu5j04CGIWYKLYr8rP-19YsTjUQtIPS94AiWAItQ70Zvg2yDL8d31qpNpNLbi9Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqkr4KZF9UoCISJsv2HGdT83EXw2eygEx3XHmS3tYZvpX5L9YPf9683s5afWRO7JlxDp4lZwyUN1SX7d7CeuEBsdxRXdo8XGUAbv2hYduu_N4jS-vFcL3zoAdQQhl_KeqhAt8Xyz0436Bj5Cq1WkXzxnwjTMZlynMa2t8hUX-3C4jEfm4y2O2ar7WxlZXsSKTxXAlftTuhCXMpdGbEruMMXl-PXAG9NgXaFFJdGuxL_jnvEjjA53tln8Jd8RY-og27ZleXBUixUiCzKVVwhAaWBJwc1zcvvuY_pgXE0tnoC5_Y2oy5S20nhMmX8IomJgrpMA6hucIwbtkRCo7SJJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftQkI4EX9ECa7zXE7s5o2OTAJMZJrUYLEYc-A0jBUzQ05bkusW4H882XDcBEN-14tP7cNRaqDPy7k9GtquhKPsA79T_4xqKQ9Un8kdjvH3hoSjXY-JdAN3M-G6PzXX06dX5F-ETu7oXGvEfVhPQ2YUyk41pHrU6Epg0DGPzu7qIsEohdBajR2t9-7D5pbwny5SW7bULdQSzmszgdIJFwNIgOZhMZ0vAXCK7aF98SQpty1XlNHXQW5fpdVX1RuAui4BbNqUlMcADxco1Tht6K7yH3mSxkNguyiYuxDc91C5BdX1280AoktpvrXEM458ji0b-Twy6HA2YP32bTa5-UPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMvLjWz9W7y-c6XY9VWvZ7WmpoyfLGo7MS4LVE6-7Vo3MlF_KEWGBcsxJHT-TO70125uRur50L28W4u2oJ1VWKRngKicuYoJ_RJrCr-TdUSDvpgZfR1D1k2YF300FjUYVj13HCQGHxc4mVIg5adqeBSmMBMNtAec0MNBRVcykY1wR-dv-FHFcTCSoqpeIj5R5McqhVnXAvhEZruevXS4j6__wM8afWuV6vonIe2qunXMMz2ksICwyL3Fv4nK1GKltF_QqVDrSXAbrjJVF5sO8KuhZGcom5YMPdY-T0xMMe5_wDZL455D9M9cCz5VMa8_fFnlyi0raxgRFABumYcWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyaDfBK0TfW7SsuySJVJ3i0_HdtUBqBBTKQ9xtKMkqycB3fHABVNJQk6dWUVTfe1Dhu9Ti1rEeOI068eZzzg-ch4XVlZhrABH9Fh2gmIjihFtaTCerDpPM5PpTVpb-cTSY2DeoI1_IbSgSWsjNTWRcV2Cg-61kzTelW0V9uBv7Fmj1K7Tmd8E6okuAnEInufF4kxl4MaXXkm5e94NudHqSbP-2_IA0WWyjKPyXpmkQLelsv8NETGw44WHKzdzTiNdGCBGkEievnQdA83UC74OPBqP4B6O3-lAjfusnNghuM9m5S9k0faCL0WHlYWpRf8bShCbrHptvIZOZE56uIAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVbrWJKpHdM_AfZgqyEw1gQ7Za6SqsFzFThvauW6xgVxbVjUloRuA5MHK7e8gA6RPMnp6coLPYa_IywoGZ96l6GPVN3ENNWqkImLu5UxvSrAv5RH-DG5m2yPpaiDPZrmaeYnSpEGBlvl-GV5lTcqvUp0h7Uu1rII9T1wi0VmzZq1quGEJBWatl0LvlzOXnPNZFPhPxfwziAJhx-bS2BMBQzJjFqfyoAISVqzQJSIJB4NcroPu4eOg1WwpLdrD-HB206tFnA65Cw8Bm5Ari4gXjOKkMzv729VRQ83hNTv9s7RQAgWzZziME11Hwf4qawJFwlodQS_eU-jwHDdA8VD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
