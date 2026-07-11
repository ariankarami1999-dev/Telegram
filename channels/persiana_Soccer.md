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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
<hr>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmNygX_HyyvuOcMk-vvEB5T4oL18hitAJvdDvZr9vs10Qv5nmNRTAIWGP_FNzu7ABpHlraU3Hdk-MqsC9ljHV5xA_B8dXQFx7kE0oiHL9oC0W6bvt_2OvVouSdZz78E6kaICB3L0I8PidsC6zQm5fr94-KKzqCnJv_87-PhIG40ssI8QhD4lQoSb4RI0n5tGjN-TFISxutQ7vTn7JtrWrnuZncr6bxlX4WGj1fPEmTL0G8nKjypo73xBiwMnEHXp3IcfY20SMKy6zOksg-b-TXRyDIpgHyJ0vlzIbbdO6zalOwmc98heYz0iKgXahDIYp4jDRJWzK7v7Utvwj8HUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpEGHOSdjo_mTJOR_awXv5vngu31nR-nS1x1bpul5Q5I4KV9NHOfgH9R1E4yBxS3DYSnKGjbiviK3yqGNbogDbdh3a9vjPheTABm6NQB5aOCJW3Ar4N8mU1l3uFo_8HG9qwRE8QTDifdkIvOlv-P19X3ErfeSNDgTD-IwIlDNMYK97RgM6z1u90edGfMQvqQdi1nb4-BXhlwyUFziUHMlW0PsOWPPh46M7O10oqdL7O8FBtR2iObyRaKhEYuxZvao799OMWpcsDE5F2KQk8b1MrfPMkOR_9kf5SP8cWDOldsqhwZWv7fdbjrnnFXCWdVxhNc3rFt54yRbvuTCNZ9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6wfVNXPsUu8TyKuWbeBXfF7PGamn07sIvjKXVBZ_dOvIpyW2d4aevsWxf7M8whoIXvTNqhnNoai9v_VcpRR215qXdXr7D4yEqGascc8PVY9m2mIksLrRqqaEebxD3_AydrrC8Ul5W5cOvRASvnm157nVHaNAl1rZNsDWp-9MTdJdF7yp70N_fDuoB8n3lc7NmxuHnDImGaFI_myqYlcKHrUQvsOvoM1D6WbvcKWAkoWAr7fBOCxP3Gh3e6T9983ecg7LM4oEmQkOMS0LceGXZkLrIzti9q5etKL9pKM-NvLiwXHPZ_sQ_ON4Z8aKWbV7XyORMCdIoy0JoDgle4gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiMPOzTfymkxhsqm6Z94bQmlsAffhLdLgJ6QwKShAbheF9xqD9Sp-JsafB69me6foS5Xb1P5iuywXGIhAm7FxtJ3bfwLwEvaJNMcby_E_5WAGi6ThMIhjNSBCANrXEudATeA8qut2fnjKgglva0syi3fdETwXRIzDVAx0iMGtK22h2tfQuTbYyBvDp4UhYopjZ67fd6ZOAuo7qaOLF1xt5ZwjDo88rtrqxCI8OxO-2EC1DlJxKjZYO3FkNJaJxdvEO2b1Ys-whec47_sEm7ktPnFrJwb-k2815wbhal6feYFPkAZxztLrfvENZSkii7fwL81o22eDuKz26jKhWiO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvARRLiA-7oBSC_8tRNGkzqh4dChfqL4hMwaHTpg4L9GhaPQjmCyG14WsAcW3BXFqdsxceBuXJIiLCF_ClDXFCKbkQFLgJl_5QbKaYCY5gTt0pJ4GPRYYARyONNv6jym223_QVwVm6VbSfpp44m2QEYPweozlThxCI0R2qY80F7M5A8sCYl3RACrptXOqFeYrtLKXilK7Xmvu_xLfp3G9tz7fQr-XuZ7T5kGU8B2ypqJ45R0AeYUauoSmesBfZwFjKboPDTqR1uBn5TxWnfL_nuESJw4e9WTosMiCTcuN8r01KrN6yKDYV_pppNXA2Qo92e6FiQpNHYkxxRCMzY5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rutWJ-aS4A2ppOXmT1dr1AKLIvV9Q63AxkLDNdhuLxr4aGm-Ww_rytRW4GFw9dGm6cBpiZfXgXomxqaP5OsN1MlDePzgBpx0kRbdffm3n8XuthYUbjAekkxNqEIh0v6s8R41BjEHLUQbjxrhOdpQ5QS1Dujp3CPEqak-FUHDoaHVnzSFNu0CHIrL4zUO7Ak3jZ9WfQiC1N9ZtGsibvdQIbLOTZa01Wex4xS8IjOtlnCJqujAax0CvfZ-Ep5EQXA6galqN6pDtDn_DNMRtD_QCzaJ0K29FmwJvsJVzdjZAzTfBXAu4RzgOE7nXzUn6DqeuY4H4SFM29eooc31IFgrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvW6LCyxYvvJAD_Wc0c-tMwN3XA7IIHoatTAap8o9N8a0d1CIhmt3G8SMWE2Kbl3jKy-s2nHMsUebSqSA29eeDDOvW_HxaHuFztg1vDiq7PlOnHNVOwSikmgb5ub92HkheXI5gk7qv0gOSQvaNeaciI0iugBisialqZAkqb5Z_ioiGkgK6kXcRH3i4j4Bdp75QwgMwcYBGbf5lklOsxF1RxkQ7mR_S9SbGrmi63UoCFdC-z-6O114gZBKw3F5k6VJBb7etd99kAvT7onzd0bNAbtGi9BHGtzYMO0WQ0yvK2WOSYJUy8Ek4ohe71yLRZc8qeJmLN-a2dsDnjkzmyvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWguu9UU-Ll0EyXY0O2akFAK1KJkVhjcKuKy_EwQd8yM95_jQzlt0jVXVfJqi2sVwB3GGTafhu0g1cw2dS2tYyM_VoYwKHFArgw44oauNhHE3jlhy8U4YqEU8T68bxK_xSfcD9RlvSMzt7Fg9DrxA283NXeRooI8VKGOukAXdCna-VuxZ3wC96--vDqyYIIwbiddRQ-d6K9Q3tykDqrVy5eacmbvodDyBFD6-8eFD6SBy4XK4duG2BTxstEvhMd10r0dKlUUE360m9SyCjEIFC0hCq3zcP-0gzdbzihG3YI0LKfG1o5UabzG-smgP3eLfxaF_mOxW3drRw4cfjV7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbf3L-WYiMBbsJARhkm7wmeUp9I1AKDTp9_0Rj5ERb__PvIPdEnjh08IKyXJPpDfXbQcOnSGO2xkyf8G0FmE1HIaHxRDkMrGGUtTFtAsrq5ErNhCyPBN574pddNuK7N9M_OA5DmIxg_ZcDYfh1qVeb7sruHfkd3rCnbJxXCF0sCYHk4Xwxyc4k0H73cX_p-EwqmpHtd9VgvN_7ePSuYXuh-eCqOZgWWZ4W4OVpu_8jTD0CgARkJ19iRXAgNA5XxngpbpFiTOFkDF6sdxmmXfb5d87zVYujzuuwvkjPpRTSKJy-aGOesk8kn37UgH1ujdWMV8_LxYw6r0xaisV4WiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSpuMgmbkm7GTXcCPF93jgZ_L66O9lQl3pMLPzD-KEl44ELFfHCZydQ_y3qkdKRnSlC2HAb7EoZYBP_D_pNeFuJ2g4HqAelj7J-g5EKN70Zm513Etg3urFi4DTr7ktUwvdcdEizb_cKRJQnbWsk7ST5OgYKDn64wzquy1iR8U6nZCAjHtzLKtQyJo-4REb3eqb-EACiKPmjt0OF8YYpZotrfNXj43RKJ4_TZ5QTZrdUjUTZkbIZmhTQs6u2gv2Hh8vI1E9u-j-oIibEG0j4lQ6pf3NnwaJLRFWuVfKLOHEUxxhTUxFqDQOF5rxzYxOU004fF_V6ojbEFwYYic6LnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzgyp31Wcyd0OnmCHIGmo78U9UYF8x6MHG_XfV3U3LpGmH7cFUbBTB7EvZ67t5r1YfbFJpIFkNNmKPxZoOjcOhzbjNqQ7zDhOIsWYBUwoIDbr3UzMcodwZZULHfsSk7KtYXeU-W5q3q2kpjITY5vYAfGc6aDHPD6GHUG6A06StCOABP4nMIfxcwoYn943mVVCXxo2HZtYBRobfkQoMTnYtEly-WMGILCRu8SCABSm87HiP8Hr782exuYamdOlP8Agemtxdmc7fr96Q3DObXiBNwwdHlpPpDHopIhhkvhalif7CXSzHY98gjnUv0FWDlk1P52Fr9Qnuet6s0wb2dolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzZXCDF0_QMzXJe4WiwuPDz5JE6UGuxcMe3ohlQbr_1U9IYwEvSrMhofKMnFYV21GdhhY8yUYbiWzTus2XsV9zsDusoACGy02_cvvJ-veFffN5zsSD8vQ3CyBwzz8QTlxKAs-zJrJNXV-30MZcMmLbjDT2bhuqCHqa7vGpJ7SXZH0GUuIEnl3b63qRikMAdq-jH00p2IMvnMtjDbkkHNiXJmSoa5Rd_ByKIAV_8fSXL-0BTYb_EuasE15tVFWvF5JIrrWbxzgkD-JkDoeJDmYoWdtN2LlCset-pDOr0dmyR7UBYL-_x-4PVVI-I7584cuPQEA2a10GYK9Pm6LoMv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyfccNvi76dvBXGNvaYTD_SPgQvYOPhRZfed3uj46IFrNeKflRO0ivccXwlY8Rv7K7hX-zCzklofuVjs5YG9rOB7o0zUlRNh6fpduXtGsvEknbkQJVRqe1MYKSm2R_rd7SID5547hwDJKUrFcOnelrfthpCNasNaZBotO8oiN7G2MR4yL_bOf1a8MLDG9W2yxuXX7OU-gYmVwEI_UcJQia0Ei22Ffr2UQf7r_es-ebV9Wu2XteXiIGSXe88wVuJz3qlWHhIB0BJvZBcS_ZdJyG_4sFPUQqU7PGz9_AeSraFywmDgaihCkIPtw-BUYGakeXsH1nEypW38WvfHzFejvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKeBVCt5h1jliEAd0ese7tmPt5ogxGuYq6I9YGOum-x0bC76eKeCQtYrlRUSzUfnbH78wM-F8s3zrwvI_NL747pBQp60pMg0UTLZKTxfQa3oMOPRPjAT6qa9GlK1-9wDUBRdUFUIQSgiqYppPVsMsKU-FnNoN6pGqNa4TJB0rg9OeKxinee-_o89rGivKZI1-gTsTLMYjFrZERe5qSoSqMoholZSuTQwPo8QmF9rHVD5ihJzwMtSZ-JhyuDw1zbws-6ygW3xBPD8njjKstcRaq73FVAVmBmhG-Ynfk-tOsr6tW0iYByTmI_5TwnibjNfj6nu2XtqoZsVRw9QWN-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1yT2uz2ZZs2ZAOUCSBabcnN4fj_MPtQHO7SoxZED-7BFRsd681xtaMpMobgopTeCN6x2IBg97K8TxpPz0grnJw_wFFwn2DJuHnVhDb_LPwH6nhQoq6QZJRf2nXkMlgjbenf_KJKWAv7FsopGicaGlwgjiiAvVk6GYg7IXy_YiNbc8FbG7sajSWD1NO3bkyiFvTJhbqOd4dE44mvfMfnL8SMVkPovPxtYohWz4gFuMdKhznHdvy-Jt9gNRZeC6pchAYW38LqYCJkk6tJCGQJ-JNlHd-q6vAq8HbLcXXEYpWB8lPPUFBh9IYV5bxTcc1JZFSjX9GASRR4iWr_p-66gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7G1V4OsRS2w5l2i2gMa5V95OhXYBHn2BUC4fPS4ghNVqyxGOGLuUcTlsgDxocFZXynS85JzWy3q1CwxgHdQ5jYEAM6Ih4nwiQkU7l7cWQwdsuin7d464x2MVzCidte23of9FPshv1TU-Sqg_Z2x6aPUqRnenpOfzH0YMm8mnpT9a1WO0OlqyUO80yRVQDz2fOpt_lFhETk8R89STd-Lsl1_W0_8IulJRtp5cgf0S7uPB3p1kr0WNtZywbMExaTG5-83oEeu6kIzUB2yjPJTQ6htxxMSirMUhiBBN7v8bwRCwwjkEzSSGpCMyynCql5q90X4QHY0f5k-MC-Mr8f35A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIX5c4QIgqOxQaKphC5SFr9J6eP9Enwkh_S7xK2vXNTOwrRXoQsWRHCDHGY-cTeaZ5K9G1OKh7j--4hJ5zuTmxB3vPalIb7sdVXbe9qEPUAYlYkJJ7xHckjRsM46M9i7Ybyame_pfrKrafc2_arQOkEoUch0obpwq2jppadPWris5Cl6b1yrPQV9n2tVT10RUREMNebsWfgtXiXmiPnYHz6wq66XAPZFnC90nh1wpf4NkHhj5QDJAn-Bs9hPl8QnKvskcs9J7XEf8jnVWIVjGLkCiZRvXWeM6Rijrajd2Nw5f4LVZzcdabYA2tWdpiMhp4fAzsfPES2pIbhAUYH6cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Rc4CtwFINz-euCeStzljOLei7JlRtRLJQy7ge6qtqlUHVV3eNJjkMFSKCJPKutWBzxy2AQq7brXFP6Rb04nsiT4ofFjZGNZVrxICHWAjqXyZIwbLbf5gyUt-kHRybDGMJTe8INOG3pic8ZzVGfHZgZqTa62RerBe_x1BJKwasbwrsTkShYrPF1x34J8jUhCWtg-jRgrcCxUGuGUMbh5p9_W6OryKsthmzZtNOAlWgke4ivnxGn6cidaKtzhofGVLBhosfeas4dDlBQaaTAPCP9DiMwUMcL4ekBDljxpHRmFqAghWSeknsDqoM64NGZBWpFXhNs83kBVrbSK-Cwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCyI3h7CdSXfOTanNHzaZY1vvirSOjzbMekUVFQuTzdIepP_62jUKjS8Uqo-C30fLyxMMDHjDRGP3B_EerMDXSR4DhbnUOhqgYSB0zuWgOwcTivsHGby7uJtpJfdQpi3Akye31vKQC1xCXSnq6BkDpwIKMFhFiykNQcH5MJx0On3ed_SQzEFBc2zTkjkwWDKKrF1bnRejw6pSXwlRdN_xh6nDHJJVwD1_U7gzvdHwCCknNnuefhG4Z1UhwlVxzaNAVRSTfUt7k0rUmLSrPGO9NjUtBlUwQED1_s0M_QZ0QK705ed7bRe4vvmEHg66EbTEzx7KHNumYZcCroxurVU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkfdgH8VDVZKikJAGS-tHqza0NX_LbEIQr7ShnkVqf8Jc4i3W9aKpEFkDKUQ-Xzs4DIvcF5C4LGOiiH5NpyZxSDVeL5oKLbnZ1czBeQMrIUiz2j49YF8mgktRMslaCBS8psWqWkSnU-GIJhvYtxs6fZvWxrzcOZzoEsOGIamMIltM83aEhtF1mm5crlci68Okj8usmlHYpSsN1CrHSJyHV3zx706qfIgxxnBEd-BnrlmXqaQW95TosMiKv9sz7Jq_JBISCyx7G-GsXiol7waX1GSFJ8KaHnq_e-2xaXqLIb8h9ViCtimUVduuk4tzZzXEqXCY0FwPbsD3dKmIXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZjMrLsuThrXWyjJG2q5EjKjNM7SGj_Cr3mSKoDx9aQXijeQXiKSd136m2EquDSusackHKGEs_fyOn1xE9JPGNS3_gj6pU5bE95zdrlIHx-enxuAP_XDMSq4OkftlmEcBbuLXd_cFL9UeTKaga5TOMaafgCVbUQjqXe9BrL8weDxDhV4p4OCc0xbYGRpwolbqyibofxAZalUnfpxiDVIVdZYqZZRBTsghz9Q5l50f2W_Ob0Vm9dHvl4lkdpavLHOnsxaU9am7-fdWc-u09N_1wXpxf7TktG1NJtCxd29Bnd8N1hybf_0-Znh3SVd5dDpHMIsdNh4VZOL1ZzSxHtnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8hf2ynEVrzPN6mptDN5WIJoLtlMB2aMB9ce7ukXEE4btTjpVqE5rs3kwVqml4dJgW31ZR-BWJ9S_YY4tI0BWLtn4cgHmAsf-AuL4xmY9Is-kKkVhlPUDSKQEs-Zu8StTHwmo6mw3fOrW2u323f3kFvjxoI36g7C88fdtlmtFRITvU-NbihJA85U_S250nDPjta06HK896xhurdeOhtgeUpW3bduXMEmFDO24KrYdxiyL8G-0fOS8AlnpStyjOEySX2Lc4yIm1o8XB_eH6ipfyFYsccfGPFmXXT3MV5WieyaHBTk7XaPa9gNbQwZsqVHYN1EZ85efdloNdCBk6CPBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWXykUQGfzj9sACsoCI0DIjk7Ayu9RB4M83ktoAWZ_wkU9H-DCOVGLSX0_PNaJXDfvfDKav3fSV6fPbS3efBnM_uKY088JHvojlA0YfNzXlQkTnyS7VcJJoPVh__PW-sqA6ss63z-XSXjMU3O8yyx_DKxiUAiKG2kkOq-dViRUeLjhuN-JqgIbhc_1nlQM9XqQk60mKFg_W-K4Mat0zzGPYxeYU-AuK3hVAu1to43H-IH9x0M8w1Ix1ylI7igvWiZ4cAqlo1awZXASdyIRC6EVOjGnbJmVCvP-6v5akr465L09MoKoB_cc7a4flIcSfHAEuWvipNxtU8qLRDjkHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTemXLV_bWU54sQCvmTXJk9ozAiBjZ9mkbeeolUfzsMLjklG3lYNWVUF0-PPDS_bLZ_P7MwRYyD8LbRfiGUalxiLQBuocWkWSjW8aZiruGT1GJXwT7-liHpJwYixy3ZuWQOENFpEcP3_UjDtO7X6HjKQA7KfQNLjNp1IkT2U2htIXnOvow8XL_6BnOYM4WDBnhh_cUYiQVMhuC1cKP7ElNCsXgtj498dJENqsDIwMncjQ-FZy-xdTssqkrDNDjnkWWJ1l3tPXY-jkyfglo0f8bUuoJu2XNTXEUh84LQ9KWgvPvk0EzTDbo19em1r2hRUyE7TdEJi95QHhSVCtGiYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnJRFdT_qNwUKl0xynHqkL9tqjvc4p8obcoR0yB8gS2awNa7A4lRpYOZPM-32epdogQ1haJ6WpH8tGDG-h1x4b4xZyj6iaGwdlyewdke6c1coMCutzSGTK82r3k3xIKX_17ut97wUTuV4yfiA-XIkfEw0Gplh1KledB11_e_4mSIXbRQVD9Q6QUsf2JxmShA08L-EWVGU5_rW4rDbnY3KBni9qnrJ3B4vclr4GYLnOFZipDsCkzyt1fwR3JVlU13KNURu0B6rpNVtrf_ndsRmKHMpt1rAkhWufg04Z481BXR7vNeMSQLgx2vxIUBIW0X-hrEb_hgEwTrWIxCXTJMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-0e-oH-693fWxAODFKgq5GwS0B27utI2s5i-fLjdJCEjtPNTeZbWF_OmxqhbIat_m1qj6_KU35M8QZ9ZzVDecFDFn8_zO341KEGjOjyQFGUluwlnUeoDEjSOVIMItzDQpNJkEGNGGF4QAzNPc6pj497jEzqe7lb4w413exR5_Cpop6wrQBrXLHlps6cumjGqggH2X8tLbz5NKSQMEPPBRYsdZUDpnZGEhUJxikYVgd4Fi6x1LGhodjp3cF8HJn_shPYO15I5R4MC4SGSnNsn4ZiRh3Ug1rdztldht71v2-VU2UBv9d_Oe8_kNtcdmlvE1FK2sIowzudbkpVb3vE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRheRWbXZaVNtwmufKtFgMRJ2iOR3r_y0x1-9HHt9FOqCXlHqCDREyqZFdLWkXB1g9gk6vvgHWsrFCPIRVvDYqe2bmqdo-eookibACccIsl8DAOXuA08XDiIJ5ZaCIBn4KUn50vv37fKZCznI8kg0b3yfBrliYjOQ7pAoqPhHLdZZyziqMfCE0xKaN4hMqUEQ--m6Ob6WE0BwEacxS64-vu1vCFxdwAUozo5ddi1IXJameIuv21eM5Rfan-k4RPYrJK9RShqj79SXDEsmsUXkro2LZXnK1br6wLctfg1upEvi2a5YL6QlPn-p1NVb00ZiZKVpDho3OhnVYS4R8W0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWjRwW99JfXDa-p_hzOx4786H0qlFfU52BC7QcUNJGf65A3d4cWRTvD5kr0XPFszV4BzQQm1QAK3XkupmdOa2tWqVQebFeqpJHjLvm3MWE2xAx4a3Unh_i1Yvmebozj3Ul1VL5CgwsQynkMDM2bv_7XlL67pQawI3yJjXdcMLmcGacnjPvxafJUzBFhlrozorIxyqvQP3ILM5ibgMiS_jEm7VVgvUoMDuT2nq4AxPTLPyVSZ1aPJ_Nleezn_QRK2THIopl5emogII59NLhDttmdJqIOY-P-HeRElO7GHzfr5wE_enQ3D559FMlEs56uv6qpZjNPquhDWs15mGMJo5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9rAqk8QImbrG4LMpZRrTYn9Tg6m9VxBTFzQfFSDCT2SN7fL1T2XtO0WeTnXQMU73zRittq3AqAyFWDaITzd9V6r806Tk60SZj3EeFMtLqnTCkZD7LeoWQRIE09Vgjg0cFoHv9vy6nNFpPurE49bv6bi_YiREO2vb4BUbHFZQcQOQ0wY8O_N4mhZax4cWkKMvRDMMeR6xKNRWwUKqJaHqivlNB1czfU2nfFQllrsxsARi7OR9yC5d1dQP0kfCv9K17riNyHWjAxGwnjYu4AHrBaeAw75Enil3N8bzy_HeWf03h5DNT6ORnuuiiBGxszVt8VviFW5iqUdQuL9daI-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEDFvtInPwnHZHnWzbVScXl56lzWagmsX6B4jPve7nR-JrMJiDxVvozFRM7ppi1qheFnLwAG_vx3NxSSB4AiGZ_hsYNA1PI5v3B5KqRQ9pu43AFFwRqRoItPGveSJrTM0jmEUGtXbVIZK-e2bW7rkcyzqcNmtJ2lcyCBkyPsEskniaUTaPKMKUO-BX2LaH4X9_1iwTxdNmqH7T-8oPs9c4Qg2VVc9A0hDQ2m92Ax2-XsqUypmr0qKsrNqeNebT0B5TIsQe0KQi1h3raKsww5dxUkamvKFqJjIgCdM9zzkOKUpoj2ylmRPPSfiBzDdb0lcXyPCjIs73fM1bKkftqhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YciVz5MzKiH9pw5cSdxQWKMa3425WVVwmryoLZKaOAIgOFWxzV9s8EOhoK8FkuTkVwa5L8R4XrA453Mw1LDOB4j2q8CcL5nT5_oMslYf8fbOd1NN8dZAWhR80tzXzo14LOuLxAySRSrf8iBTeveopeeqlSFQNEiKwN7IJBUc2WiaRbqUq_nSnyyujuzL2TdZ8f9LVC2xibpofy_Wne6dgtwysgPXzhMT02x1FiNnWIlGaKJ2t6f1ZsAJ0idTl9302SMJf6Y3oriDrS71P0Rs8cDbcbK3WMOEomag1_guZ0L9IFcjH4GLJg9vWS0z8GA_vll5OQjG-_3BYhJJjV3sLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb4TWwPetK62MpnG1RIf2QnzpHQ9qmODy4GyBNNBAJS6QAhsOraLVvonm8zWYgLhIGF3-YVmeXRElRRDBLj7vwOnSck_vhr5uSPq39oCpABVojT-Ezw78cMWTU4q4bH6POSFfJaR2pjFb5S5Z5En4SCp8-1Jcx1hO_gOWaqq_QFPQ3YmX0rKDvJn4Zi5Maaa5LNrLgGb8miPjkU4N4hMsP31of9zlVGIt5D5J3fuLNlcY3GzuJC4aOSj1_5-N2KfjjxjWnOY9ldkxL1-33xIdKj1Hbj_lyN6TjnvoQYfhb95kREzpZmYKxkEF1qg3P447ZR02hX-fgiuAA9ItuGeqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqy3hD8Xfs5UfZy247Vf1IQ-_wwjfUdq7rrqF0GloJwuO8F0oqRPrrko10zHoDVegJnMmL4F38fqZcsEVASK9ekW_1ov0X_xqZaHLkhwsh0qkL0Pobhq8ezgBZfUYREo_1nrFHR8QhdlkTECPILeoKraVI2tLxhkE5aNO74MGZzgGUYBDd1C8qC07MYCARC-zY7gPG4M3Mi_Gz5fDedab5_sfzz55za2TIehpBPQZ0GYs9KM_kgsAfVNSXSRwO2XWvgHidFaZrfeS-sKdg2n38NTE0h2UJxBkuDx-dn5Ea5y-J5Qgrs9jNpoXO9wlsItW1DXaLCoUm7n2RrNjEoRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyxfac6TAJ8JHzum3JvCnwQzYKGzFwt2lrXFgtM4sh_CXlalYVB8Mb3lUfbKUQbrpjGYca28KuPI8-Vt3cwC4H3jNwcvqhJD-qVb1igOhmAaMGEVoIjugww2YvP5FNSAI0rNn7-4X0ccP4EL75Eb_6-SusYV7TzBYIxgALKiE6BzYh9EtbFx7A5XHfsvCRbuSyo1Exx7qCasnVGpZ4ZZBHkxn8nrChsxGuvVeb3VM0hhzggjocFLovkKVOOggvHi9TVmaxAqXVk1BrPeqZskRdF0rV-XffJbKNHiZXzsNEwKp5oyP455I5j1_O3qtE0UKXCRiHS81GgqxdUcxFBapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGQMiFed0k_SZ2uzhs_28PPcsBNBylpKKYPyuxOa-c4eUp6JM3vaW5aUfA7QpkUPM2xd-tASwwu2pjZqpXVQ7X68Xc81rPMV9DIBE2t04oQ2280MII5cL2OtK0Shp_xY-GyiQP5XPxsPYAIGvG-CGvQNmW8eNhEoHp66iyIN5KE7JMzCtfuDjrmqtsJt964EcliS0MTlhSD1Eqk9LTL3BHcehT9JcmEd9lhCbQfj6cVh1SDrSMs-id0RBwd-yQi9awEZ2pheSNvTlx40Ne9X6NHDVgIOhFNKPXgDMoLtDbKpdhPfAhqtjbir8EdS2xCwa2_5yDy8XV307iT_qqP8Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEav5qF1144ZTn2caxcvHSrrb5Nsc6iB9kIxC8aftSlLH7UapEF7yQuVIqxbs1FCOlAx3GuJjz-Gvmim_6JlOyeTY3nNi4-MmXpWZQJDz5gyvtDcflGiTnbJ1OLC04EOQHUAd6j3bWh74YfpwoAmK6QR3-TNcI1LO_8pCQs5SvFUFesyU89CqS_JU9PObbyM7shix4FeBj7LmipIbXQSDNL81mtPeb1xDKCfM3B3taTIH98gKtLGrm6aRnIgZGA3pp9qpB0hTtUPARLKmRNX5mAlovgjROYpsptMp-qbUx3hQZA62X6bsh-Z0_gyupXkvrwB1YPDQwxyM_zISeVvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH4sJFZJK2azPldp3n7WPaaHsVUC0mC28IdD0VddXqDgfaThHT-7o2Gk07SZIscRcHW5ClE8edFs1ijMsNioY_0IepC7IzVEYWXkO2uclCqMy3O6f5W6uALidcd9Hdh2kX5W_LdDBNqvrDRttgFPqtr_ppXCkZ8ZGAxGpdF_uOgI_kxNIFDi1NvJ74wl9BY0HxaFJPZaevGOMX07gDxip8P7VkhJcZasC9Uj8C0lbWWG7qN7UFuSQxbGj9XboS0-xot4c3c_oYyohKA04IldT6RTInv9EqgXWs5bqGHdVpNmS_s2F8R4p-mCg5_CbM66B_Gq8Auhb9cVskS66DS17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB2hOiKb4xS98E_55WH6S6xRe1-TN-j5DcL_1asvoRt5BeLjIuACwkZEPSfoDlNsFEaJQSWwlqkyABIPGac2zG2WkzgDtobbJQiu2_hlTIyAl47ZUzgnUvPhM3TJucNJqQ_tUJOyBiTSSVr20Zz4RzjtFSf0f8Ds6c6MCQIG2f0ZoJBQGuQb3tWPVgyRIzm36BaX27Xwji9da-MYw1AwLfuKfSBQ1ieMeiBTTGXVaSKXFsd4CVIRFm8tKOt-UaT5G0_vt1YzwTcxGooJQDFW_3sD5eu6RRyLNzY5r2G96YnG-VjMJ4VoPGczzUZaUwFnzk0akmyz3dvkQ3guqi9VXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=mIxkur_vhmInc76pHqKLGPpAvXUgn_Un5i-OGLEAv76QInNERbySMV4cxFRnJDWYFUxQnegZukXbxDNUbCt_qloXA7ZE__-24dqvF7wYvRr_tshSQE7IeHULUgW38v2UL87XlxGZRSwacOuAiE6Y5GJzCoHsYV5xZFsHyKQydE6OFEGxsB6Ths7ZXZHetoS4YZQLmxHx0xpn_agwTTnBuz4ookE2xsiiuRttNqto4pH6iCpGx9jvbIgvRlZSyCUS3dMXt3z2ObRDC-YAzz3CCVFCFPwhT0haT3p8EZc_MAkx080QUBlfW-9FLtYJ6pnia1bdsELLBvDUhFKgCJXZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=mIxkur_vhmInc76pHqKLGPpAvXUgn_Un5i-OGLEAv76QInNERbySMV4cxFRnJDWYFUxQnegZukXbxDNUbCt_qloXA7ZE__-24dqvF7wYvRr_tshSQE7IeHULUgW38v2UL87XlxGZRSwacOuAiE6Y5GJzCoHsYV5xZFsHyKQydE6OFEGxsB6Ths7ZXZHetoS4YZQLmxHx0xpn_agwTTnBuz4ookE2xsiiuRttNqto4pH6iCpGx9jvbIgvRlZSyCUS3dMXt3z2ObRDC-YAzz3CCVFCFPwhT0haT3p8EZc_MAkx080QUBlfW-9FLtYJ6pnia1bdsELLBvDUhFKgCJXZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZfIodcdVXJBs_lzNEpT36OMnwbNLsaVvqToRK98fo5laur0TVzoqNisaAXkeUiOHR_5BkfjRZTc_XkxVWN7mZjZ6LNr9au5Rrs38DCRZYo_nrmixIC1VM1V9H0YtnkMil8oWFp1okq2YEXCDJgb4hVqBg1pVgDs9S6ajTPTbN7mnu-VxCTknw00jMvezw5voO0-u9Toi3zfnzp4fHIxXSiDpdDFKaMSCjO4VCpnVCCetarel9oeoibkFbAc3YXaXNR0ew69slfAS177tRdRxJ_uGRcCzLP-EDzcxanqpbYARPBes4kXa-PQXMjLd6gKaUsWLvKfTrwpqDPcbLBfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ryub1NjMC8FW5pHC5C0vfjTbYs1Lpg88Ge_BrhhpuqKVEzqQUQlORFf0gyaDV41GbE5hj90RV85cDNMQSzk3G947qLuZNkcNoymVSys5mdAXXkqZmlobiDF79Qbu3ACX0wyZV89G3-HXcYjoLCuk4eZu1KX4nijZweYk-jJ1OnI3yd4fpYyC1IJBrtxvq9wDRsa-D8wChtUPXMzZpoULoxLC2Yb2UNfNyJo0YjqtGJnI-18hrW0wtxnJY5L0CvDwaiE13co8SZij8cUIiHDHU7DonvgKvHtnVfpNyyrUOpbHvmmSM456vuLuf8A4QsMShtEP2ZUT3xN6EzE0Tg3L-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0h-thuILcIthRJS4GALQlH4I92U7fLUyfiajSdbNJFdhHItCyWoXWvRUi69uJRUVVRVROij2uNxp9-dPGQ_Cv6B1Gcidz2dCbGFtSWFGVchhHjtMEaPzGHzTMGtYVLrybwUaaPP3lTv4YkDMKWNadJftUny0-ebVtsvG4v-RvfgLagocapvLf22U5DXb6NXDaloSSlijXLAdaO8hRazsGC1amz5rambvKrNQfvE4DD5sXzv4TO4hSH1YjFlB8U0Ayf4d-LQGJ6XYjLN0O8ELs3v0LOiFbJPqhU-wOoNwa56sVRUtK_t1D9RgPs_0fePuxLP7o2cgcJ5d0LH4CfcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ozsw46xnjD-dDCxd-okV_nOYCTEmv8q6kP_6dJsgAEvL1nNPh6MI0qlsB4JTeDjorSNqCtRvrF_OHyzaY5VBQDPP-z3kMFZJchHC35bsE5KP229yTiUx4CPNx3c8OJi43FL2MiqfY3MLar9_kJN_6F2s52UZaFf5VbmeVe1G9CRuJQBzn8doVPRW769fBgoiDKlZb5WMcfrrpV7Iwoiag7y2idbLoqlsNiUXO6Ikk3hKd-oHeXPPzijHSmNlpTkrUOcAkGudBR1rGGyPAPxGLHld-L1TNtuFf_bb-UKPgOWW4amzGYfSZKtqKegRnvAUHWbBNz2CMSZEFJgFldqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cojEeryUDbH0xhaoXsRa-kg5z9ZDrQWKU_eilmQ4xYy3Ed3dUferRggiSNrxiEv5m6ApUdnpUCcIUyD-ZYJtmcK-9UwjwvnKJ0EjlSyb_BstQfqAsYbKZKV3GW-fMg_RVxyYsvvtzFcLnnmUwkDzza63NEF_IZORfpb-VMBBjktVL8-z8Fuw76--K3ptGCN4tV5KUF23msVj578ryGFdCtWquRIrpGohhH5EA-KYZ8A7RBnwlfdMo1WPTs4bDPa2RE6sNkToJ-C7vqc9aTR44krX2icOQACBKLc3zTmjxnbUO1pRcNDHL68s1z64lRvj0YWpaN5u4LukY2IvdNTXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8-y53DrLrK8DMBvdf4JRrQJ0lvtB70jisq_JOQL-Mo3KogCewgJZIB1OMt6uRt4tgO-PTZXiFQYcBEJ6ktYQP1HMgcCpfI32KLpnlji51eaZtqtgNmWUiIsldgVhO9vs3f4X2bliIXrkMFmuklMi3e7u5oebUP8hNNupbMoyCObM6vulckNmlTJH4dE9NMLBxJS6FxAbBeOIiFWFLgHoijlJo95swwQIBjoWxVrfDndWX6ALvGRTndE6p6QzsM0z8uNxPLWMIsOr-Wm7_AT01XT6hESmmVs51qW1JrFAZl_QNiAbZg1mx4qNuYYxv057uxa8YTneEoNFQatX4o5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goww--M1F9K2QcjMkDhs-3sNkXXp820hT7w-Le5MJT10V1xWoHAszO7YIT2SjWAnB2mTTwJbFINNV-ZMzjeq0N1OKk7ye0o6zvEHUW7K0uLay4AZEoEy0urs9JNTpHAmK1lWTmL3kKXJDhJdol7BNKt53MttVvHABTpHYWW9MHWKhQ3dCL-Fb0f-1LoJGtftImV-F2E2jl3HiONMuM1TxqEZfqlm9hiouQzqnrnEydhk0Jna7mGjXRHKx63KGL3vNUqS9dqge5dg4Lra1s9J4RA_KNwkMCcx6tIuxYOwqAOD1mDJVtJxPS_T9CMlmTSa-qeMNkIWEXRoqQiwOc01pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHCEAulDJRe1Gm9pF9bt8_52iyHVnZZ63V06ZQ7uUUGSLlQ4cu-I56qGvV8Er77uGQ_XSPOxIohPObS0QNQ5ORHtD6eIrhx_3JDBIvuHC8ZmeQslKx0bN-enthczoedOyKXiL9kGuIbTpnSM6PFEudcPIma4uNBbVkNxQQKS9unxiypttTemGNonxwlZpsWGL4YrdSpgvNiud0EUMx8El9gNeBb5hKszZZmkJTM0CFsXzuDjB6h9y5YdBaq2em5COmqoIJUGvD8gn94dn8CduoBtg5FqWTMD8G6z6vcJKNXf4DqlLJe4cHPqbeevKFTuKQJml4Q_6KLZuDeJKWuzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFPyVNNa1XZL9CKrq5yeWhBCCAjQLIGDXHHTu--KWYCgiSr_ClefWe6HD_ziDQAsQfiXRlAGmBKtutSg4v6LTEWoyYVlB5bU-wKPJsMrpXX_ZO1IIlaxm1209Vy3UPCr8xmm0Bzmz9qBzJflY88bvyAP9Q4J78xaI36NQMaHxuananewaltXo_oqHnczXioDW7n8Co1xBIePC34XutihohZWRipvrIES6sn3UBKjL64MqjCmEOrBjFPYOu0_6iofGu9abq_-XM9ei30cm7RyejNgsgvxkRizXoFzpmdj9HnrDr5b-HfSUOEi1vmubpN4S1gRzLWyzWaypICR79DWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgT9uC37-RhywJJXTz8Qsyp_wbzqObGSCAgjb5FGYbOOn3IB3VWKBk6Ii6PQOv4mwLxj6VUbHSR80fngAdynkQ4kTnQwtSpACQ9znnkZpWthe_HVED9aIoxp7r6RhUpF9a1JEPD7Pc-_m4onLxh2CF7Q9zv2Ur6f18oen1GWsXJBOsDLlEdAx76uvfKBwf-V6CMLurm8ZkgVkdRLUGIRlzDPYnB9LmaymvxK7Mz7LCShbkZ64x-JaItfOOa0L8n4wEUpfo5gh9Nl_yE95QKlHOSWdXiycSuaVhKO18xkavlBonfkF0EQLrPa3imCNDA_eIJPyeMz4YN9AK6UFB3BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6WJMogU3hUzQp_9zwVyvBnvbRCURDZ5Qs3R5yNpHa6ci0rG3e1lXlJc5iVffh2TGhU24RIAwneV-ugQQBWuXpSMY9GeC7TERdNuulSA03SqKgZYlcyF0gxSG7dafp3sdYFlBeepnMPTj005I990UHZM4H6lzVTcWWew2ZIHmoet-aEDPlySOZazonIUZ8V0aYA8K4T4ZJko8-3xRLtO6UffWJZlH9BDODZ3iZiVtq8iSAC9bakMbJjfsUGG2N8weTYN2-rgHoVkWSc_djhWEQZruvzLaR0fY9IlJb7IhJR8ViE6i6PZQ5cIthcvR5NPf6s4kBakYviWLnZkg-7TVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXkmr7Dr7QmcEDglqftVMoOm6j6_AwJpapwDAfNOj9BpPmaH1qtEi0aSQtyOIZyGsqHJjWKEyic9wtUtAWazS3_iBbIsZCgmpJDpdkY8MvIO_UFnRFhatGmH5M5s8f_rr60mPBcChIXrKrCjgb10QUmvenp1JD00Yvcl4ijiiDPx0I8qrSSsnWegZYeok0iHuaaEZEo6O2V1EwbGxGFSmALFgzxiTMx8BKgw_U_mH2fxnubUwGw1Wnh16e_9sUAUtFS9JvaDfPCIjauvoGwCCWFxIKakCtDDWBt8jdt9rFKc9ZRI3qRNtaREIxO7FoNQRR24kp9lqAhF7t1LD44X9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4XiTTjOejT0N_-f0Ta0cu6k8xNmI0LymzB_lPf-UdS6HucUhNx7Eqp0t-pK6K5SObA-wraU9OrN901SulDuoyDBEFw8MGbaq5P7DCWJn4R1BAzQ6Ac9fZcNROsfFuiUbX0VH23qJuR8iHB3uz4ieQ6GeLMsuj1QFh7Fo_tzsDhWP6sYRf6bjXy0OL4uC2IFUibrD2bDc6kQEj_F6gdw8ZtTihCv0p0XHtF9NaqvxZ-5EsmPf5aG0BzaUen0tBwMuQoP1umTGQW0teTVW4PmkaMe7SmgZ9JxRh7vSjAu7HE6bwFyuWTwQkZgnVwQkDul9lUIn6pDFepc1NbFIdaW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=KLWr3gf1TuMlemMmZQAb7qO6fYW-kcjDndi3TQpz-n5axqhVbZ64Y4WnSYi-yk6yZlLTpLrHiW17Zh5fJI63Z3v7CsQ-gw_FsOiI0iIGZ1vVkn7vOIKIlAAOn3PqHjSwgNtnQlbogvjD9NtZ2J8s3W0QdLz2av_6xlNoyKnn5VwxD9R1hEBspW3CpWq7H6RiPlRjiBM_gUn698C3nk7vnrVCVO8qLsfczFg0V1YL-LEFgh3r0UXJQ8gr5nCKpu3D8s49ChhgBRTEImOMb-U5HqasIiJBTWgoA1Rrm4aIw4je2DEmpKI8HMu0ZBvq-KbGd5y79ahdgQN_H5d9TlHwkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=KLWr3gf1TuMlemMmZQAb7qO6fYW-kcjDndi3TQpz-n5axqhVbZ64Y4WnSYi-yk6yZlLTpLrHiW17Zh5fJI63Z3v7CsQ-gw_FsOiI0iIGZ1vVkn7vOIKIlAAOn3PqHjSwgNtnQlbogvjD9NtZ2J8s3W0QdLz2av_6xlNoyKnn5VwxD9R1hEBspW3CpWq7H6RiPlRjiBM_gUn698C3nk7vnrVCVO8qLsfczFg0V1YL-LEFgh3r0UXJQ8gr5nCKpu3D8s49ChhgBRTEImOMb-U5HqasIiJBTWgoA1Rrm4aIw4je2DEmpKI8HMu0ZBvq-KbGd5y79ahdgQN_H5d9TlHwkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=NpyhruY7TFuTAjUyb5dZniJI2yztMVBKn6-RXbKQyTR8C-4xRycptWgUUlhCUXJIpQUqOdIgbl8Zrsh97FBFEH7xp228N3VrwYCbruGRw_F8-RVU-QJ25CKd8oIE8ZtRPAS-UE5mj2qMv5lD2M4IqxJNDTpLOa8HBvjPPgSlwY3dcL6MI8Grbi2Q6XXNB6qSWnfdhSG7UJi_ndgCfMNGeF-pf8km2fQjto_rz4-HqVdkckiwbsAyMi99k--UY8p4UpnJ3RS6tXIlSo_d0fEGmKd7OfleXeETMvi4Fnln0bF4jxOGSlAlh9cYKcMT8bXTl7d1aju_z_XlwRmZjUTI1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=NpyhruY7TFuTAjUyb5dZniJI2yztMVBKn6-RXbKQyTR8C-4xRycptWgUUlhCUXJIpQUqOdIgbl8Zrsh97FBFEH7xp228N3VrwYCbruGRw_F8-RVU-QJ25CKd8oIE8ZtRPAS-UE5mj2qMv5lD2M4IqxJNDTpLOa8HBvjPPgSlwY3dcL6MI8Grbi2Q6XXNB6qSWnfdhSG7UJi_ndgCfMNGeF-pf8km2fQjto_rz4-HqVdkckiwbsAyMi99k--UY8p4UpnJ3RS6tXIlSo_d0fEGmKd7OfleXeETMvi4Fnln0bF4jxOGSlAlh9cYKcMT8bXTl7d1aju_z_XlwRmZjUTI1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upeez1fm0DnCAT5uGPmLHxYD2JScia14Zqa3DglEVQkh4NOmHlaRmmMiM9XOMuVXSE6lq5MBud3LVytd4nlwqY7W86U_zRNGCh7dr2HAhZsqJ5Q3ekjtviSMYK8TUl9Pq4YC-guw3Wonz1N9vmxFfHmxvlD4vrQ03LBuN0zJXCHWjsmRwqzKR0pUqD_cQG7kiEW-OhmizAVvn7VMrKt1PUI72aptkebmozGFwzFvcOP5mJgsbGurUG_UWlek2WpJ5vYhX9fl7O9T9tCXoAWGqP0vKQnH3EQ0mult8mYfTldcxmSfBu_WkLJXp3WAtNdkZFwe0EOm6dztENZ8lrsoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n70BabZCvRD08q-RTjuT2yCPC7N83b3JIzQ1bKa7iJEbbVGZ42j-BykXScO-v5kE3KZ6oDCjXoA1rND8LnuYxuvldccXhKWXU8WQsvuuSA8dymT48s-gyRHNSjSd4RGRYCyUnySKUVSl-8pWHlHa-BOtiUtWSiMo8Y3ZxVNaRxpc5GTKaXTNtsWeU0_Hw7SyP0z1YP82vWo7tfl84MsJfSPdOQrFg0x9j-VuFWThOaDhE_uio0-2qqhaSGyk8_RGhz6Ou5rQxWC64Pjj_k1Ur0tRPINyz6GSP0AcHUTX-AKY5W-dPXspij4m_ZnKxKvoJLzTS-0Wwfj4KG36zwszVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL-ShWe839zuWInbWuiOPmh4sIQrqrV_WVX0WYPuaOl2nStKwFbO4drNGZYDJft_CTDFuKCzabNvCL7kT-oFHjQnU2oLQpHsP6cUivLFsG1BHdfT_y0vRGL7jBE0cWc2HjSv6aTV-Jf8sPKtXXQasdRvmZv1iNOaVqyAOPlfPGs8IXF3Hne-MIDyxz9WXfQDIMx4uqJzADcIR25Blj-2by0J_pq7RqGCcD17fscHngZFfHedp1T4SXnrz6-NQW-HOva-8F7an-8VwYBDTNnirhyGYulJZE-Xw9O1ITDjT_IOmmCr3nyTOUULLIHVu-_m1cKECDy9ZzMOGLzFiTNOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAmJWmDpsUTCegJK6SBDCfH70YAJWun8PDmbgEJO8DL8B6adJApT3SgHEHff_1sUgo1ZymffMywzUTiSt05mmjjXKl9qedryoACpjRl2QZaD1vq0lr_AZgqBLIyiXKZSR_7EMLY_kxRwlTKMJqpPE2UwO66sAOla59_fUyV-dChZGHbfurM90KMxRSHRtRZwyLbcYl1j7rbr6DvPd2R2GEYLmXRg4XyJitBKwhFMdxoaW06kzUnpit7PAfuvD8UXFeNGitYdnKSMgArDjyiWd7whTWTQPnu36-mtSNypPz_VXyWZTzHun9EY1WmDv93hpmuhMtxmqSJPkIss-0-l1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRyXq1gzOpPbtfF11Uh_mDArX87eiU8chx0bt8bkbIep-LqMmNVy3K5OcCtwBoGODFX3xu4EASKWCBZiblwuSz8dph9UCRkkH8uc83pnDR2V4bSNpI8o6sf8jdVwgBWuIiVoSBgAruAtWZ-gqrUAZMfzCGYqhTOtvpvloh-oMJEBwTOQJQipLSFn5i7ryhFflf34NitP7dYyYawPnAW8qPfD68dmTk3fCb83YakxRgaRsY-V3RebwQcL1i5kU5LN2L8JGuzeyuUjlB0kFAhTrJjG_WS9jZsUipq0_BulCggEIlrbIcOZWkV229a_HGNvypqqAHhE6owiW_d43rS0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2puLH8zH7BqCOvW5h9GQ22rlsLpCvjkjsDRMNuF_6SkLOx2VC_nQYBtPN0o3Aj3pPRofmOgKJGdrPxVZiJrHfh6KQkIoG70UVkTm_NCztF4XBQ2nEt9EX9BMB4KWQayIumiEBHHxRmpBeZI2pLR-sa4jxqcOMY2MnG4Y55TRf66anqsm0BnHm5iQGbIFBZmmU2CYbeENxw3ntE4hg0DO7pLAPqUSUeDTvLGPKrnV9SKoHxrNRBFNKzvI-suYHRkExLf_Sv0J-w5qoEMgAGzVOhzBWeb3JibbysRFu0Ga6ZSWn_-qshjgDEZfJipRRsG7405XFVfw7oN5G8Kd7-HBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzXo5jZcPTKSzWO5DEnG2gByJb-0zr26sJUvKVAxZd-W2f3vgID9dQCA-YwpXz8XQ5uq4-9vGDsLGsKVYVsmTBiA5FtAuKsrfVtj9HxFd3o1w2W4Li4uDrqNMIEFOIg5NNixVC5hzWMwIodYt-wrB7AQJ5GqOXL5iBtJnfeqbWKG0Z_VwVQMGPh2q-l9SJIZDgOEEHWUbchE8014THwEq5-zqYOlVsDL1JVhMTQ2mrumsT6VoUcgD0-cWQosxQnViEX9zskgfRLa9b4wYKRfQFKSYkjHYafxJFyf9_7o7pcxnojhrpl6T7GeC0J_0E3qVgf2T0FgoyLLHvpYWCmi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzZ_aTbevaJA66gbZ4ai2s1PBPbBEZhNKnT-Php8avv_BExtUYPA0L-IARF7qqqGn8f8esfTz_vfdUjBcyygL9YFJXsKCT364Wx15pd2n-J1PnbdKoC8reL3hAMaavllnpPnl3aWJL1o0tJKlXrom-D_RmNdoPVcBxYlS9W2668rhz9HLo_8i-sRjyhroxdmqD7BCMxiy6UjpncVDt_YfGPkDxK3XF2TrPAX9C4LRQPA85Z_UBd9vEjNbCyejE45IRx506Ysj3DeeOh4cU4PV28ljU8ZDj1ZZv02OlU_2JC1-g1Epx6Q3pIF2wh0e8fRcuwKIX5nrfDCgE0sZh-rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hljs0lKsjQiHpcGJahYolWYhZ2q3nhokOZ-Z-VtSGXjTPRxUrC451mX4cA_s_Xy-wHrQstQg8_P-ShINvkd0niWGE7NkX-tYPw6h-dv4i07av0etjKoc5BaShIPtTCIrmXHkgAGUIgmIah7twV-L1dDV5P0qvOHbe5g108anA-WFwoZsWv8jt2A8DRLbnImkGgn3bq4eDuFP0kogIJzoWi38xdeV2Sh9IhgL9K0YvzEjeyqEEBcRyBP7afA9bc_xlO5M4fSWrFX6r4owiLA1ZeaG4ZYNEvO8zn3vZyUt0UIYqgLfuyeSuwzMus7ex6y1n_Y9mU6gFxXNVFWMq8XXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heJxUtx6qvBnsOgbHKzpSVLOSmYzzMHuz_3l0u8PDWEzK0e-fXXcNkuDT0QiAAij8aG_7dkkQ5BdfdTXyFCm4OOKC2OugdmlC0exXBnyYI0YHDO0JmKMr1TUBDwADVbh4DKTPnjGinMmSlLw_Ti17SoMdvLKweoEUsrYkC1OMmOZTiR8o0TGTxPBiS5NazA4v0DHjpdfATVEyQ5WscDcIGA2uIdiIHWCrZJbGvoPsulroHO7N98JkaEi2kNxp4peo2OYWomwp1WfFmOH_ep1kzqIXAbEx7ckwvnTXNmNc-pHP-z4CkkSAxI-aWTwLSUufwMY9AU2Pc5JYV70jYALuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=eYGYvLJKGztg-3NF8nbWXMmELrHOUkGRlWYOXmmKsj5MT-i0qzyN6YTkjgaX9vIIoak6flrIjvFrkPrkcRHd8T3Z8J332E3qNIrj7wTanStQTaLyViB_-bjfuELXlIgKDDqgIPcRWCzTYgNDvGTLYrbV83FvQDTeZGc5d5-GU2HF7SQiVyJEj8egXmxky16A4hvqqTvFgBVQm1rPjY1usXqdNABkRdREPJ0OYf6uHNunarUhrHzTHrli3hlw_1fkwuV3evNzwa2vqdmdEnGqunyhK4j41YvcyB4wINoPwwz-iY2QCDMFlSZzlnLFn5awod6NxSLreME3MBs23i7Y2h92EsTdedAYfIL_D1Q_npQpM2hioXmVbId0dI-ZQS04iFmFPo35ZQGhrtrwxQ_-BIGAatvzujH79btGhKmS32Kl15oLy8moehXO-gkDPnSOb2N-5yqBou2-hqKCf7ZF1GoBtOkh74fnOZT0_Jmd062PX4Igf8Nhu8n_FQL-moVAj8kMWWXP43ZFAl2d1xgecmD-egj2ORDoV2MOw1G6WQWciJ8FSrta-M3gwdYycHQcFYwz4rq1SFme4Sm7EWasgXQWE9XCIJPm3-G2pIgzQTUM8FB0N4ABt4_jLfTRrRMi95E5xR9RCjUpJEQLSz4aYTCysOC_ybEg696Vr-Hlo00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=eYGYvLJKGztg-3NF8nbWXMmELrHOUkGRlWYOXmmKsj5MT-i0qzyN6YTkjgaX9vIIoak6flrIjvFrkPrkcRHd8T3Z8J332E3qNIrj7wTanStQTaLyViB_-bjfuELXlIgKDDqgIPcRWCzTYgNDvGTLYrbV83FvQDTeZGc5d5-GU2HF7SQiVyJEj8egXmxky16A4hvqqTvFgBVQm1rPjY1usXqdNABkRdREPJ0OYf6uHNunarUhrHzTHrli3hlw_1fkwuV3evNzwa2vqdmdEnGqunyhK4j41YvcyB4wINoPwwz-iY2QCDMFlSZzlnLFn5awod6NxSLreME3MBs23i7Y2h92EsTdedAYfIL_D1Q_npQpM2hioXmVbId0dI-ZQS04iFmFPo35ZQGhrtrwxQ_-BIGAatvzujH79btGhKmS32Kl15oLy8moehXO-gkDPnSOb2N-5yqBou2-hqKCf7ZF1GoBtOkh74fnOZT0_Jmd062PX4Igf8Nhu8n_FQL-moVAj8kMWWXP43ZFAl2d1xgecmD-egj2ORDoV2MOw1G6WQWciJ8FSrta-M3gwdYycHQcFYwz4rq1SFme4Sm7EWasgXQWE9XCIJPm3-G2pIgzQTUM8FB0N4ABt4_jLfTRrRMi95E5xR9RCjUpJEQLSz4aYTCysOC_ybEg696Vr-Hlo00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdEeiLys3gyiSi3LWCcrnuw_AiroOg3-feHOk96yu8e39xVSz3DKErU94dk71iT4LpMgXHKe3KL9hCrnyAFrr4fN7pOgu63HuVWCavzTSlJuydvz4-OfVRNm0J-I6tli-dx84sa1QSqElZ49ARRyOiuCuQGadIBoK35Nz75syfjyjB_kCApVkzcuu7kw8AEBAKmEL6o6Gm6M2sGBONq2wInVg5Y0qiMre4NQ9x7hjjP_itpa-HvAnfaxMD7aoHpnNEO_BnzMVwIHGyoRqbdamUWQ5uR_QKHg95LlepZ3Je1Nqb8m-ndJTactQO1FNsk3Xr6HegAdsbNqlGT76idlvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkEdAaWPeMAn5l4hukQPP9lnLxIQqyvun_YK_I0PvAX_rku-F9ewcU8RwHVMJSYFJjUBKfow9L3DLiQotZptyIO2YjzTTuabjqbQUfbY_QEFRGeclkyF2K8x3o1-XcBJILwNkbawxSGM9wkZwwEckA8HoypbnyFJrHaOC5tPTCS343QLdkQlqxkTAaFzskoDVLc954psOgtsLhBsjYrCmos7cgXqhe4ttixtJcyQEqQRJukRpnWx0QRVKyychujDQbUkah3lW0PHwq74YkNIv5we54Ag9epQBOnr054eLIcWYXjlflDNtGRa6DqREKe5dadEVKVH0GzOvY9MIpN4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n48pLTL7wGhc82kSRu5Kw-S7AVBBzW8hsAPCeGDiNEMVVlW9ctwehilnp29n7jfuselIl1fSHMdelP7f7xeuG2w9GF8uuELlhJrqoZ7F5iFE4nyubQoke1nYe6QEFAC6aLJ29PweulBW3RVZoF-XRSAR2TTuK1C3TNik2o4s12J3lHo2a-skTvGqZmmxo-BA_rG8Qi51qf7zEh12HLjkMRz7Jvgyl-G0GkAduZWkZ2I5uqa5KFLzMm5bCVflR7OtHG5J3B-4S8urJd6cQhK90oPPxbu2arGttweqxyVLTAH4wgs70oxdAhmHcH395qylJe4qha7rKwKXmlEzN6vs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=Ww5nnDCIi6FOBRVoAX2j70DnMOw8fa51pmp50gNyck3Fjqz4V9byOpNtu--ieu7TDLuBEUzhwwzenvPsa8LXAWnMa4YwKXVFCBAJZfG8xbv_YJovA68ElztHbPc5HZyMJzS9t39e40Lo-r_TV2anMq1xtgEOquoj5Q3qnAs8THpnbAeJ_8qW6cO__oTFG5HoAeX7DY_HCEUn0a_aWIOUU6C7elq_OyMkQZ2LYGIIqyh_BW4BWiajQrZiSxDNW9pQHuik5P85O3n59YbqpK_ZZTIoy0IMJvNi6GWnG3aD0KyRSS-7Q6jOvJ6YH-Wvfj9qqy8cgbv5Dkhu_uh1XWQjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=Ww5nnDCIi6FOBRVoAX2j70DnMOw8fa51pmp50gNyck3Fjqz4V9byOpNtu--ieu7TDLuBEUzhwwzenvPsa8LXAWnMa4YwKXVFCBAJZfG8xbv_YJovA68ElztHbPc5HZyMJzS9t39e40Lo-r_TV2anMq1xtgEOquoj5Q3qnAs8THpnbAeJ_8qW6cO__oTFG5HoAeX7DY_HCEUn0a_aWIOUU6C7elq_OyMkQZ2LYGIIqyh_BW4BWiajQrZiSxDNW9pQHuik5P85O3n59YbqpK_ZZTIoy0IMJvNi6GWnG3aD0KyRSS-7Q6jOvJ6YH-Wvfj9qqy8cgbv5Dkhu_uh1XWQjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8OYf413Swbns0SJH0v9yEgekzY9bLGr7QnAPljPCiyP_L_m9KNQPpLaC7zd4DyBfEGUpP6prQOkrZU1F7Wh6pnOprDLjmCv-9w2AfK4uaLsgd-PQ7YgKbfdGgJ3Q2uVYhv7lBv8t8q0TVuKyW9WcyqZPG-NkwlTD7gjIbI7dPGjIOvDNBr1e3S6-resU47Crjb0fS6k6vwjTzkU82kpj4iGbhba46W_Zkp5kG0nuhF04WAYS0Lubcq3NMewB-CkdZ2jjKEHSHZ5NNseG8pyb4IbPKNQsxqMP0kpgMM7VuOLyG5pNmxbzSytelb4VHqJl3MKbkUBbjnmVRL57zO8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsPKom_DWO9o0mlrHFw-6_zJU0tCDZre6t_-Ec9OKi9zsMqwDo8svMYiwU3UEsMW5bgWaRK637M_KpuA9cLbljx1dtJmFY4-7YNwJ4PFLeuVFJfPiEQqoQuuvzbSiUbnl_aO1tiNtl5LZYEDmxcmDARV6-n8qfYIuo4w9AP5Sc4WSsTkM9gkm2t4rUvenCmxX9qV3fvDdyxcHyUYeVo7i7HnWMZljeds8VZp-XA6PpTtPpjbsvPvg2-knztFArR2YvvqjFclgYGDeMMQxKyMZ2FzeA5J3viahGWrk5G59qsQpGmWx6FxrdWM34WqqzlJEe8h7s8YJ3a4ngswxN0C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bse6gdFito8Vv1WriqITNI8xXe9BuMlqdu95u5o7oumy6K8rQqIz1npeszEIklBUOPaLFMp3Pa5q46VG3TX__OY_9KdPu8v5dw_7IF_k1TE2z0UOK3Ztjnr1fonxRE7OEJ9mLAq6ILK7_hTxyWCRaXxw-dfTHWS5Dua8qIGp-OL-3irKVONrGhJWdzEKSPWG0omOrKrLHfGpC1RTNwsZJ2lxGmEE69mFqjKBldUxchgS8wdn-pHHl3Zr4io7kPOU30wQrKnppwEE4mBDmEXYDGiELT-bbF3EZeFfd20wkHPv6yXCqfEmf7iZCqnFpkZ1sstBoBoSaTTrMCjPMGHrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNv7U54_aJg2IZA05uAKk-OAt9no1tBqre1HxiNru4X9PqtryCRfExpGp9HCWcnoNZ3U2t__MZvrJDCUtgM79DfYble2RZWXlvfpdOKVFEs04c6-6ixemEIkCVNr1TUIzjti27li3rNMu7UgPAM7ygW-_MsPXhEfTXf9AlzTIM0GOiKm03RzsKiiZm9ykbYlXEzsHWzEWLo7a7EgN8EsnVqjgI8Wlhn4efLDMEeROOMViG4jIz4Gq7CKdXmrO_AbM8dPDoF0ZhUs705PDoqson-aUDlgam2IsfNYg901UGOb2J0xATqU0nWwOqK20bKIXMfUDEb3v0yIjbBL-iTQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBU-5byZIH-SBqtGbrJG_1pHSgeOOfvppzuvPyTuADGyiK7rvRxIzAW08W5htCpt77cP9VvS3pe7KDALT8OED_e3jlhP9hO5h5NA6lQf71DvMPVvFA7NovdSItXAKuFaw6P7uWaQcfGiK6rXiZal_x25hIxn8Fu_gQ9LlkxWOh_QkQnkTkFD3TJ_tVGCfB03QmDo6SSDAD2CylPa4hjvDl9YLm4I3e4CwHRBdxTO5jJbtcxe09ef4DXzro-jdexsfgKK0jUSlQJi8r0BVRcsNPnCm4YQpqFV6mubcUW81qthLcQs6Dz2m5yyOCaKVOJOk1fAGGHXMc2JI1r_tklaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPaBvN3gFD-yeSriunO3P-H4P5YXPsD5qGGbNuo3IM6AEh5w_nyThRRalgFpvOVP8m7MPKIGu9VKbQqM3UAT8twNTil51O8dUUF5DFAOENJ-xdB2HNsnDNqkTH00Tk5zdxTxrFvI0psDVbLz5tziByawyIw3u7jHZRcl5qoMazLKJyfWX5-BzvbRd52_whh23eimRB7nxowAXEx5mKRUihh5rO2vXidZ2PNxGAcCFuhkhkgTYb7fw6To1SoX349SxLDmpuPvPvbNx9KP3wu6X0777Vs5-kqAdb9Lt_qMH7k19EKjWCC1GKQ5QYiQZ9u1vXf-37aNa7d8qdbxwHot_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPnjng2oBJNHac2f8m-nHbYU9zWfkyFV3aVlOj2iWthuI79EPcxR4xMDjqZrROkvLOj5Ec_3GVHDo5ZcTj6TCK5cAFZcd7qtf6josLmPTN33hfTomCMT0aZFLTyOyGY4SZN-_DTz6HuNsiCD4iAIx2BQU6UG0--RCSDjZdyiRt6U8kCAxf6pZkFhrKY3jt1Hxm00iWsPIRwZshmAOzpGC7oHXvB3dxT5Mjb2ADjksR2nakOXLakkvGt2XpPNzVUEDbbmqeQF_R7ATl2sm8X1KXn5i2xP0gbH5mzWDN_1ZbO-HuBGxgW5a2k26KJbCxRmXzVD4Q1Keb2csVno3moyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-dsmYHDq0JZeHKDhi69Aayscv04jSUpwjRAGqANU1sbxdYosV9XVNWCfx_1SHo25ChWFuiiKi8Su9y6gHnxKAd8OISgVytmCZ8BPTHySkcIp4LkdMhXp00EKTRqD8uxf0ZglUG_FCVZvLwKCIavFFTqWcCnqDdVHKmOIugEYv_ly4PuDhBQ3oPX3WK7tW7vPudTNCTmhSrkr0BgQuypzoXH9qa6Ngtz4BDdDfPJDZMsTGikqH7KBBZO2QtvBOsAETe1bXCE-WcuD7Gq5iCISA8uysEPcfNL5yZ7x3ldSfpkuvazyEI19AlLP1z49VjPxatvXW5dABFM_vfXqWI-Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEhSOS7LbJ4KMpYgnk8a_3YIzNWbezVpfRui3ynJlBv6-ahIZWic747Ha_B6yPLkdXhSGqGEKI3QKzCN3Q-3pTylIV1V8rPmp6MQCtp1oHQiA3AYlyzUpFnN_wTtSPxBLSg2oWvdbUjZqdCTbYL-U683b5yKpmz-0o9ccy6iS7DnqZw2VsyEm5VXRlCbwXHuXrctHbq6K4Rr--fZ1z188nrUatqLURd-1tK5tDizKFPVJtFflCeO1oVUzWXiTcF1LHzdIaEVjIH2Q5CqYko8-0T1qIi6yaw49KMuSNuidpHcZnnFG7yNmjt3zQEoWO-w6Lmx2O3lDABOPzp5QKLPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke_QsHUsFkLcZgwug-Pk0gWwS-b_mClXoUz8CDgfYd3w6exUcnu_3CGNMiCIBKIoTxM66UFoVUnT0CEqQwKXcEEOz-zpzxm_dM1ysj5f97y0j1RpHml14uUcYJr_qh1FkiSLxm2XvZKZBDR43DBnulvHG6bKlhWz1m0lcWrUAK4-x0Ejderp6MHY-LMl267uY1BzbtwgTwrA7aBGI2pkZpXEdERZNlGaiV7UPnIQkHLDLNNPx47VNUl0-Pxcf0OPtSls-gjt_k8q77eshb67p1IOtHwDJ2DpK1O6ZTJ-uh-bWbZmqu2WQ03oM1OLu8mJkrc-Jh2bXQRSZpiP4zNz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Wu_kT0t4LbC-dwNaGLP7j3TBoDfUpHSTTc-CWBxK-yZD_VfiieOMuqxM9iy9vGFVrF7SbrmxmGNVgkvFeb39ysKGvKNJVTVSYOwIhQmHwNJwOX7M4wgXEHl1HGz2vz1ukQ3XftCq6ZYIrhTSNjsrpW6CAVzhN4u9XnZ2hZBdejEWw9jgZ6und41PTCiX_BkoVLqB5FTtVREpGsyPJivtX_5CoXD8s1ft_FGWvuaNag_ms7ktUwsxAyQfx3vu24tJXUUdKuKyfMuaIyslogTV6GBKBzgDixkAIakpYPSH2COwMXujCDGt-zTAbHAs0rDBZcxQ26FZUgNHSs8iJu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzKYsxkOVG6EQd8pydSMtuh0wqCH3SnfPgXqZApYLbPT3b7YyL96xtxSkf2l9R0yV3YmPy0VCJcR35cmfO1-uX6Yq1nwbr5BiDuDPsNnDsm-sZxoJkiEEHazELZjnlIYmow6jRBpWs9YSAkiv8kpAXfBMta1o1D31wateDKjBdeLJ_MXBYpqbUFAp9dGiz4YBo-2i80mR6ZZ00PcgPZ0pveWkOFxmIJ-Kklqh7pp9lJD65BaEg2sOY1_mOeL072AjhitN3u1cqFk72XXt7PqFs9qyd_RhgxLxlg80Z1Yn0kIg5spsywBgr8P_uWmUzD2nCMOadEVr2NUdjOTgLrOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2t6vQgHkQp_sHYs7T0eMOhGt07kKyko6c7oMYDOWHsSj7XA_qvaNnAcX2BWxMjVzgTcnWiYKaQ6tFbW6q9z9poIsEw89MWsDrGOlYRXOZAD5NYQDGHAypEYDDEI6b1ch-EidvJFOe4gCi_fDUuE5LhIvKYsMLZX7swg3HEWcjB3mn9fmVhFBXdK3pbmwwhI5G5bhNJbr9We-B_6dpVnrRUopqCxBMYV_C8pZDTA_gLWFvrwpkap4efb79y3LXFvN8E5ILo6Qn00PQQQWUUc642GUau_EbHwdcPNTI_JfKPJeqMQWSzGBiRsn1gMgDuU7RzXBOz-wWm3YxItAz4-YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUWr0AYg7jjJrYwnd3SLhghR-bSyZpBImZYAi0xwe9tOsLi7jktfppzaSPCDhFg9zLJ07-RRu54A21jwea9azL8xlKEyQW2rlspm7BUPdVnQK7bEU00k58Ob3_Durp1zL2pheI2YwWn036rYkGCGSTTm7JqLxhGoxftWq0Aq6qG1xijBFLY1mId6mJZi6CAX5ngASEUsAhuWi4RpCxZ7mmGb9GhCYQZFkNBs2KranbILysWjebMfe5NiqXmQ93809nxZrFKpeYL-fvIY2RD5XQDAXjSyyCOXY8rVXtnFqyO0_qcqchXEJIZIMrKHJ1RZTtuiL6r153_fYAHp--L1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8pGyOC--IosTXumMq_j8TKBGf9hCTO46M0xSZPDErIkQB-vwA30o9_V40TRrc62KfE0h2-4EkkqQGDgL6gxNJpI5JYz_lU5-PEKyDYiiYqvoBEfyPkQZqN7ovddixEQ7pbHn-MZ-9SEeBf5rFQIbTZf-WuS8YoNjGlBGHqdwNHViREoJKCVGXWY3LWVllmJvIWPi_UXjgw7KERqnFIO9QTkKzlPIrwBAj5gLpgSbfTSV1Ob_JIaSHkHaFNMdw_UveCPNc0snQT_g4A9iNtu9avpzw6wV1BVHxv8S74TabRRqs3s7vQlBFurZnJoukyeRE89jec875EXwNhaH2X69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsWm2DkpH7x5E8iBQdwktuy4uu3araHwvrvx5FfV_ExGpgRbHWddzzVhuXiks3ZQ2fD1NwNnp7rGsCVsgMzy488k2h3X5b9SxVEBmILKQeSK3D6G9Y0SlfZkbgVVuk5g_RYRY4WWt0j8FxyUXGR40rJAVs8kjNeBvAlbikhtKX49xYGolknlCIpRdJYYrRtB3Ty9nehDINrcDC_jOhmyzRKT7Cdl8OwymhH0IB-7XxL9vBdKyvGgyDJD-I83KRL8lHAYWT3SI3sd9AVJFchQ1202jrfs7SCkNBs6CUX59p-D6bigc_IIXtO4wceaWBz40P0-hYvFv9pXKkOApKtEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOeumZtzTXUtfMaLfF3HMXERhQwQNtuA6Z4BqD5_6fUFXUvblSdslaRkgXutBnyS0HZHlaEPHtWgF36bcYTM_9WgTgBtemtkqXkpRGzgmAWem6Swpl5qtyQuF7pihsv5GG1eBIPm92ehXwbIc7l7x_mplqScpjNDhp1NNGJrkiZI8ssxQPaCqrkVl46MJ2UW5R4vufYEBkczmVKnzNYiop0U7adkG0LkWjrveSChIA0ILZqloCArgL6PKGAPRvcSlS4CL5PmERNblI_JK2KcdvH2pCsy4EWnJntKOe_nwxBlaw5mq2acr6cgratboIdPAdszSGXHGqTDQdFLmyKWBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7EVWqWV5pM4oTyFwyKptM2-vFAwflp-NK2nTYGfLzNQWaseHSjqeeL7WacZe_1G7QQTRFeLnoY9VvRpTnxGcd6jzw5PrrHyPsRAiGU8ZS_Txzf-TPTM7rzGXoQLIpH1wmJQ93DKEQdIO2HnTbbuD-WY3y97Eih98MtErF340nTVbDciw5de2mCiodxBX7WB1vDNnxEOZ7Qt5HSew5V7cLAxO2lpmiVxj_Kp49zhyVmjQ6hIzKYeBaPj2ibfyi7poAz9Vu2MDaAYavyyxYVpgrccpnE0LbcQh6o1jqqPhWAFZDyANtnXM-5F7EyNvC9yFQBSfBGOL42JbqoEEGdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=LAnlubrPgOZedGSAl5ZZ7Hvy63JSzHFqJlZwfQxLte0--ishx27rPdGYv-bo9oHpXIhANx_OoPotmfEj4mIuTJa6mMinkquCVAz7nMoFbzycg300-b6HGBaqqw_gmKXFigMtr_QrSF4ajoMDwngZp0ZWvhdHwLCSPZMIEVoGSPfvFe0HKTEERj1egDAxKO7Th0v6Lr_CtmPZ8iOFHDP5qEWmGCllKbhT8G10QaGxplVgBM4oGLka55eRVbmStzjCI051mUOMcbn-4-YwNhKvWMuyrj_vnFakLtFr-JSIHHRxX6CmdWrNamkZf9JUwqCYZrFiNu8NR7ko9wl00_A-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=LAnlubrPgOZedGSAl5ZZ7Hvy63JSzHFqJlZwfQxLte0--ishx27rPdGYv-bo9oHpXIhANx_OoPotmfEj4mIuTJa6mMinkquCVAz7nMoFbzycg300-b6HGBaqqw_gmKXFigMtr_QrSF4ajoMDwngZp0ZWvhdHwLCSPZMIEVoGSPfvFe0HKTEERj1egDAxKO7Th0v6Lr_CtmPZ8iOFHDP5qEWmGCllKbhT8G10QaGxplVgBM4oGLka55eRVbmStzjCI051mUOMcbn-4-YwNhKvWMuyrj_vnFakLtFr-JSIHHRxX6CmdWrNamkZf9JUwqCYZrFiNu8NR7ko9wl00_A-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=Gt-nJDxq9ZiogXMVsQp5XRX0JzZ8IY6kXsHx6FQNgK2EndPohZh1n6mV4h_XLz1ZoAjX3fohE5IL7UOB4YewZD8l9pFq8srVYtm8xMIhmXvnXt8p0AFgbdzGDciHgLTRpxQAMsuyfvmw65RVAHBDWiDjaBOW3wrn8s1gQRGpcP-kt5HF0UMQCRM2OMZkZr4x6BnRdrQ2StX76lrrRb88EmqdW1kDM_VOSyY1frhpipxItkLv5NZqQO7oaqlwVaNHO53mhCpbwjRBgnbVvOOQCD2XW0S8onvL42o7JfWAyk-N451k5cVIdeauuCF8xvb2VwHCG6YsWSfjt6p-57DLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=Gt-nJDxq9ZiogXMVsQp5XRX0JzZ8IY6kXsHx6FQNgK2EndPohZh1n6mV4h_XLz1ZoAjX3fohE5IL7UOB4YewZD8l9pFq8srVYtm8xMIhmXvnXt8p0AFgbdzGDciHgLTRpxQAMsuyfvmw65RVAHBDWiDjaBOW3wrn8s1gQRGpcP-kt5HF0UMQCRM2OMZkZr4x6BnRdrQ2StX76lrrRb88EmqdW1kDM_VOSyY1frhpipxItkLv5NZqQO7oaqlwVaNHO53mhCpbwjRBgnbVvOOQCD2XW0S8onvL42o7JfWAyk-N451k5cVIdeauuCF8xvb2VwHCG6YsWSfjt6p-57DLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=tOaqDLwq8OC-QhvRtyqLaAOrA42pn3ZqPmVGzDtH8GYslnDNv5hTtOQP-itPeVatfrnWN7uwFPALw5C13bfUaXe7OwwI1y26DI3BDctBWuENeOTtqitPLhUCZAqXA3JSB82KwQUn8AUDPPvrjJ_wn5ZnpG4E5kI_1sHJZ3U0mYt9ycFJLnHc0N8J9mR5BNijC6O_MP9sCwGBE6kyBXd-GHV49BvzIa4rrcYU8wsj-yvu-HHq9NIDk44-4KXMiZTEAWw3kpI7xAL_y9QEDIqWJHas_C7TM4e00Q003yA_iSvJK7EsMQ4HPeWU8aNFmcn3XiOiDg9DymbzM6zYiln37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=tOaqDLwq8OC-QhvRtyqLaAOrA42pn3ZqPmVGzDtH8GYslnDNv5hTtOQP-itPeVatfrnWN7uwFPALw5C13bfUaXe7OwwI1y26DI3BDctBWuENeOTtqitPLhUCZAqXA3JSB82KwQUn8AUDPPvrjJ_wn5ZnpG4E5kI_1sHJZ3U0mYt9ycFJLnHc0N8J9mR5BNijC6O_MP9sCwGBE6kyBXd-GHV49BvzIa4rrcYU8wsj-yvu-HHq9NIDk44-4KXMiZTEAWw3kpI7xAL_y9QEDIqWJHas_C7TM4e00Q003yA_iSvJK7EsMQ4HPeWU8aNFmcn3XiOiDg9DymbzM6zYiln37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN7jNfn0oGoIu-szRi2B1q-zrMyUVo22KRSXA-WeNWWx5yzNVrbntGYi_qHc-Q4841NtZLoSq9iX3rJEDl1Dc_LXxaLxrGFwtQrFzNoYfJsiKOhITJwyysyDck3Gxj8RfTQj5VzYLo6hw0QWyAir7whEAlByjONkL5T-r-RSpbcNdzVwRre8duceuy2xo-qJHM0NmGcwRrjCH4zXqDqY7goF8xMO4m2yqOuNSVU5OxYTRZkTKHP-Y59a--fEsPy6qEm0kZ3g1OWADPFF6v94d1bRnt_Q-b5jjUSpocDcmfNPc9P54HDxHe9BjEpZZDs2uB0jIGGvkEhLVcVToL3v3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
