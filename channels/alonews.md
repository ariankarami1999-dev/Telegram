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
<img src="https://cdn4.telesco.pe/file/aZ4WC0Qd41_uZPlFkFonY_ELRs-Y_U9phNYSuq540lw7Lif9W1Z1d-PYp0CaJloPua3dHUJYtPXUWXwglAYquHqVcwuZ6PO9CVAyRil0URHo3cvic4r47myzvvgW7Hq6fNICz65mhZlAJMaaeAUTgUqH0w8uVoItedvOBoWQXj5mzLEpresAAoDgXrcY7MxOOLuwD1iinXBQItHyBvIG1TPhJ9ZEhqPt42E7QiOqA8JFAj2CuUURnRFiltO73PcDR6-JHN0YzjOalZakghnDI6AVFtT-vqvZriziRjVjgiHHnusQVplTNDhAepBnMoENthBEW21iVVuROIyzJ_7iIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 962K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-144568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز:
آمادگی نظامی آمریکا کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/144568" target="_blank">📅 17:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است در نشست G۲۰ کشورهای عضو را به کاهش روابط اقتصادی با ایران و همراهی بیشتر با تحریم‌های واشنگتن ترغیب کند.
🔴
یک مقام خزانه‌داری آمریکا گفته هدف واشنگتن، ایجاد «هماهنگی میان همه اعضای G۲۰» در کارزار اقتصادی علیه ایران است.
🔴
نشست دوشنبه و سه‌شنبه G۲۰ در آمریکا، علاوه بر ایران، تعرفه‌های ترامپ، جنگ تجاری و افزایش قیمت انرژی را نیز بررسی خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/144567" target="_blank">📅 17:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5932ec682b.mp4?token=Ovf4VilP8ZN7oczWyh97g_-N9T3AMj9IRR0wSDSapgh-GV8XL6z8nbE7unc9qTMkxRJKV7vuBzPNVSK4tKkydRiytAAgJvUEXHg8ClA05v5Jbjbu7fA0W5tL_6MXSTMhyloqb0jeGjNvHxVEZtbEiIzERDmolAPV0cTKEsiy5DBddt4JIRYXKKA_bpOpWy6vg_iHulxv5ICKj53xqLk6O_nGw8rjlPKAxUB4BMdAr7k4K_FgleEiEX4aSYnDGgV-hgqZDVtbnd_Ca5OrBDGFkuG1x_rSsIeD82g717YtS2AD-Y59BAkqnOaE_KG7nzh-9c3GVPCDGmEBNsoR9YvMFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5932ec682b.mp4?token=Ovf4VilP8ZN7oczWyh97g_-N9T3AMj9IRR0wSDSapgh-GV8XL6z8nbE7unc9qTMkxRJKV7vuBzPNVSK4tKkydRiytAAgJvUEXHg8ClA05v5Jbjbu7fA0W5tL_6MXSTMhyloqb0jeGjNvHxVEZtbEiIzERDmolAPV0cTKEsiy5DBddt4JIRYXKKA_bpOpWy6vg_iHulxv5ICKj53xqLk6O_nGw8rjlPKAxUB4BMdAr7k4K_FgleEiEX4aSYnDGgV-hgqZDVtbnd_Ca5OrBDGFkuG1x_rSsIeD82g717YtS2AD-Y59BAkqnOaE_KG7nzh-9c3GVPCDGmEBNsoR9YvMFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر آیات قرآن کریم توسط محسن نامجو که اخیرا به تهران آمده و بخاطر حمایت از حکومت، یک حکم الهی بخشیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144566" target="_blank">📅 17:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc5bd3dad.mp4?token=SMuhUFvMF3_0KmOQNJAVflDtkDTxi1fSJqYCV2ZQvlVTDcrU7spuPQzWZ79Mzf3U3UvUNil149FmHXgqg7my1UnZx8UOBHaKCFpIeHH9IMA_BFx4f3hE7xUHI7hS2vseJr-tGWd5yzgVIyWCXxeSSo63fMGck2bGy9O_CJQ29KtbUioYMBKBLhPD67vbnoC5cALVHUIR0Usf46PtYMCK2majtNDkzoSjKJRHOa8Wq0scBNdzf49RSswumPrtLNrrSTCVf2Ly_yw-XgmIcXlm300PRXqpQ4Lb4UodLKO2O5ea944vGDILNzGqKjEKnRrweie28r7eMA5B46AcqZ-uCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc5bd3dad.mp4?token=SMuhUFvMF3_0KmOQNJAVflDtkDTxi1fSJqYCV2ZQvlVTDcrU7spuPQzWZ79Mzf3U3UvUNil149FmHXgqg7my1UnZx8UOBHaKCFpIeHH9IMA_BFx4f3hE7xUHI7hS2vseJr-tGWd5yzgVIyWCXxeSSo63fMGck2bGy9O_CJQ29KtbUioYMBKBLhPD67vbnoC5cALVHUIR0Usf46PtYMCK2majtNDkzoSjKJRHOa8Wq0scBNdzf49RSswumPrtLNrrSTCVf2Ly_yw-XgmIcXlm300PRXqpQ4Lb4UodLKO2O5ea944vGDILNzGqKjEKnRrweie28r7eMA5B46AcqZ-uCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک FPV روسها تلاش کرد یک میل ۱۷ اوکراینی را سرنگون کند که دعای مادر خلبان اوکراینی به فریادش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/144565" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O82rAEWWulu40xhz_fCqbMGLk-2TB7EZjTxP8r5cADk0cs1OzkuHA74X5zifNsMLP-ep93VZ2jfOywzut3NpD7o4voZY3XmmTKXQ2OoeRi5AuU7Fo-Zs_L0FYGryINQdOLAYBTGEg7eKKiRhaXjbmQEQRIx5v_vYXCKGGHhKE_9iIAi9m4DN39Jzn9hCpQSXtjJpsyqQWNfg0U5dgVlCPxEOfhwvnNwJPrAjhX0v1FmbPjHN58ZIg94f0UcMg4T_abklanNaGPyBC2pruhgJnxRZdpc7aZyLHFvzDQ8gv2SF-ORWU2r6uRmnq1WJfLyO4Q0fK-ouoo9C2bdrHA0jqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLOoDBG81jfUJ4O3fSNlLoMBmbwcQWZ9ZaAVv4IORVDebmpDISj9EOKAsFuIVeB7NqYNTT_-CGAmomwaQFcPkM3KuQ7bRD9TjfeIjERKxsd6CTsbCsKoYqlSMJ0pEYhaxdxTz9yahZUolB2IB80u2lpuSaNYn6jf4KGGNbL9iBjSYG4xvbqZ_gZYsKOFrw7jd-YA5tm60mCfO3RIsHVcvoEZ2AqOB27MDwCxrPZv9D8vmVprI5Widn6dhzBJ5Dw4ZdaG6giLtDVPxkUbCa9XgIQi_A2Fychwz18h3Kys27RF_omjKceR1vm5hSPRJqw4t5JAxfpd-S2u6Ix0CIWW-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی که از نیکولاس مادورو در زندان منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/144563" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رویترز: آمادگی نظامی آمریکا کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/144562" target="_blank">📅 16:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=T7zfvYd8TZpXdosq8_mVFFy9wKqYnrxplzRj2Q7XbekO6zyPnbwDqPg5kofF6rHl4OG29_cXH0XTT1h9N8rJp_UcB0E-A7TsLTaeXTc8tqDrOcfHUb5jFYdLQliRZ55MIzwVGqd68xUOVhfP9mbK2-Ap7bcwxLTzd2eTqdIu6x2rLKKaBz15KtmWCmwRJH_BR34JDFG9iBjshK6HIM_I7iqd7BsfqRaswUPnkGvVEYMpTTXYUd3ACTNdTiymYeFdZNdp_uoZy9ZSRBSbVxJ55mpVpg6M2G_cwgotLuP59pznlr9ahieUW8eZOJDqPyNey7xHq0iLARwGrLOVQcWUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=T7zfvYd8TZpXdosq8_mVFFy9wKqYnrxplzRj2Q7XbekO6zyPnbwDqPg5kofF6rHl4OG29_cXH0XTT1h9N8rJp_UcB0E-A7TsLTaeXTc8tqDrOcfHUb5jFYdLQliRZ55MIzwVGqd68xUOVhfP9mbK2-Ap7bcwxLTzd2eTqdIu6x2rLKKaBz15KtmWCmwRJH_BR34JDFG9iBjshK6HIM_I7iqd7BsfqRaswUPnkGvVEYMpTTXYUd3ACTNdTiymYeFdZNdp_uoZy9ZSRBSbVxJ55mpVpg6M2G_cwgotLuP59pznlr9ahieUW8eZOJDqPyNey7xHq0iLARwGrLOVQcWUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیمت دلار در بازار آزاد به ۲۰۸هزار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144561" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9bNpfqjPefzajMX_vqMw74lkshPFlZeKI1UFoXFLa4aVaG43ADaPcVYGsBEMuy2tcA8CXj_N7JymEyGa_St0pIQTqgO1X8Q-c7BGtdwsNTgVBakL0J8kb1nmsgDWd0IA4Z5UUBPjWowRReD-AaL9nIim_RtbD6_dsaj39wDCV4jnVrcQZOxiLjVoSzkm3N0oICQ-C7xEjzcSlNkv0H6J3nkYYgZuhKvD6BOoslOypBnvjzHlo3SurTDSQsQdxlrdFx5zGqxsLs0DJ9o2zMgRxh4EgX6JxWsEOc1pXoq7YqVZhsEkW3l5fWiRmWZjhDxJU0LrGYE64W59srKuUogxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت چیپس دل مزه در سایت باسلام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/144560" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfre-a_5swanI3AOptWPo-7x4gsY2ES0TSoQ9fb15ZR6q7AC4QW-gAedYnjBogtwAGfP2UQfn6dpvvNRVCbzGcZbGw2uD8i6GEy-pUqw-eiJPRsmlM-OsqUhM-UPSdfB7skJDGOdbve5kr0mBEE5OGkWi6njv7rDxcGzGXRlUz1IEvTT6M2wJASg8v3LjWzA9CdcZ0oo6GUqBBmANxGloBESPurikO9XhP1FvWm0B8x4WXzB1Jdf3bctTO7114euzSU2EYxPImnRCZ8IUyLm3536dWY-pbEoozmnVsT6hmiToHiyRFigRGik5ocIWAA0FHnIzJhxXYHtrAH7IHvN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «نظرسنجی‌های جعلی که رسانه‌های فاسد ما از آن‌ها استفاده می‌کنند، از کنترل خارج شده‌اند و باید کاری در این‌باره انجام شود.
🔴
کمیسیون ارتباطات فدرال (FCC) باید وارد عمل شود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/144559" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CckZWi35SH37Ul19X_WE2wgB0j8hKHZYp3AW2pa0-CYUU4VVQF1DCf8oyRNc954vzQPz5NBWfXVwoGa-OEdC-TG_Otq3QxHkIlKps9pOvBHX9Q_GWlj4cRFHcTmb6Jtr2uiFk4hzbggzvwawestlecCUm9yfqQW0QXNj0Y9RCpElaTpvgBT_Ryu0o8-wb9ht9lHJZBjViv5ERp2frb6n05EeHb3wDjdIoUVzUIQdp9UrEPoK47nWUxQNQ3KhIhifKSgYujqAdq-DLFNxPl9Lr7TlnXMk3HUn-H6iH02VC0I2YaxytzDvGIxex6ZujCVKqM6bZ48Pii5L1Rer7Tvb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CckZWi35SH37Ul19X_WE2wgB0j8hKHZYp3AW2pa0-CYUU4VVQF1DCf8oyRNc954vzQPz5NBWfXVwoGa-OEdC-TG_Otq3QxHkIlKps9pOvBHX9Q_GWlj4cRFHcTmb6Jtr2uiFk4hzbggzvwawestlecCUm9yfqQW0QXNj0Y9RCpElaTpvgBT_Ryu0o8-wb9ht9lHJZBjViv5ERp2frb6n05EeHb3wDjdIoUVzUIQdp9UrEPoK47nWUxQNQ3KhIhifKSgYujqAdq-DLFNxPl9Lr7TlnXMk3HUn-H6iH02VC0I2YaxytzDvGIxex6ZujCVKqM6bZ48Pii5L1Rer7Tvb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تجمعات شبانه یه خانم با شلوار جذب رو بردن پشت تریبون و میگه فکر میکنیم شعب ابی طالبه و محاصره تحمل میکنیم
😌
🔴
اما خبری از تحریک امت معکوس نبود چون حرفای این زنه باهاشون همسو هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144557" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بمباران شدید جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/144556" target="_blank">📅 16:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhXQSfTvwtDMdV9kRrkNKAhxN3vfVMy5-O7kA83VPQU3ms28OJawBJ3qt4zTWu--zgYaroQlmkysetzvanHrRwmjgRVkGHj-suPI0DqewRWkGmTWB6Zzml7O10-pWKvyYge7tFrRr0WCl00dmGWTuxqsd69CKRBbVuaV2HV_cjRV90GaU7WwR4WtKKVjmEm90fOlNRJwC1saehUdHnzaY0l0wuNm51d6GZ_5jZA2lk3H7IYefLVMsQ5UePJMizFiZ294nEvzMrB2mHf3IyVnbEEPi8yLXOUkIR_FZ4OBbkXyiup5BQtaycL3oAARBEzvTWNoRzDC6IIz4bxsvm5hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار جباری:
آقای شهید از من ۳۰۰هزار دستی قرض کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/144555" target="_blank">📅 16:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بهرام یوسفی فعال اقتصادی نزدیک به دولت:
بنظر میرسد مذاکرات پشت پرده در همان گام های اول به یک بن بست دیگر رسیده است!
🔴
ترامپ به میانجی گران اعلام کرده است محاصره تا تسلیم کامل تهران ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/144554" target="_blank">📅 16:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDO9fcpTgNLCS9R3ce1898Coo6klxRyFvSyCgZqO5oAzyKNzfbhxGo8LjHZKhCjNA8h8y2x8Tk_ZFt3EeP-Hw_HoSaA4l9D_tdeSj6rxQpU-fR52PjwL1-1BOH6lhitvC4A7y4zZ0T4_RjGQH_PKRo_BGIYHDDzU-NMLubMf_lx5fBOw5v0tWaUnU7cIDrmJ5V4usUkCUCVlUxYbEnQhx0W6rlTwYqoTk4e4qrIFhtScfDcuKoJ1O_6urZ6m_zoJLf8XFG4tzmf7TQ6-cr9_RJlY1iUT0y-NEOyQBOH8fQP0Uoz2rQR1h5fjh1UhyR6bPOTgQ_NhiQKZNkL_F00kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پستی را بازنشر کرد: توافق تاریخی نفتی ترامپ با ونزوئلا، معادلات انرژی جهان را تغییر می‌دهد و هشداری جدی برای اوپک و کانادا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144553" target="_blank">📅 16:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
واشنگتن پست: هشدار محرمانه پنتاگون درباره ادامه جنگ با ایران؛ ادامه عملیات گسترده، خطر تضعیف توانمندی‌های نظامی آمریکا در دیگر نقاط جهان را به همراه دارد
🔴
فرماندهان با تصمیم تمدید مأموریت‌های خود در منطقه مخالفت کرده‌اند
🔴
صحبت فرماندهان درباره خطرات، موضوعی معمول است، اما این بار چشم‌انداز «وخیم‌تر» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144552" target="_blank">📅 16:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIM8gbjTvMNm6eLWnzyqZLvMPunYTel3wF2Yd3PpdQfNqPqc4ifmHQF4UiC0vdqg5It8h8PBOjNkJM8-F_p1drDBCuTIQjNyR6RDkOKotFzAuTHCYGHXPPRvJ9yr6r99wcVKOqkC4wFsWPVWLICnIlHcZ3vr-G8fTQRQP6ZFkCqIt_CHIw2I9CXt8wONl6sxS17_2OuzBfjSjoOp34V-6FglHrtbU6qIgw0ZhoBelV_Pl7tlTMqreLRuBVvFnTxddCXC2Se9YaiJmnQEhGVlkG8zPeBgNku_cL_atuIcDssNskxODcHIwCL1sA0qdGQN3t6bxjooalbkyef177JAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میزان محبوبیت مکرون به 21 درصد سقوط کرد
🔴
بر اساس نظرسنجی «سی‌اس‌ای»، 79 درصد از فرانسوی‌ها از عملکرد او در دوران ریاست‌جمهوری‌ ناراضی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144551" target="_blank">📅 16:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e105fffe5.mp4?token=kq6yPVkWZ_zIxDNVwZ2KopiMg8CQbvthgrVCWVyEnBLo6go1DJ3B2xsm_VzAHjozJy_T7RWfaIipi7FKekeH2HJReofixs5MZKA2AVXTRNEdkOE98zVcZhXCFVW7YWnNcw8E2o0gaDXARLg4DGTdmKJnz_1yS9FyvjsFlPPSf2O_O8wCwEwx7M1LcxTbicJzcqGUNdUtp90aJVL5NYwxubfnKBq7rDsvWIJoXpJyxwKoF39LbcMQLuBXT-PIgP4q9WYWbdwAGGue85Sm9aAl9_q9aoMrd0ni85RxMwLTlXhWAO0-iG2oGnvSV7Oke3IIxVw3v316PnswcyEhDIAenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e105fffe5.mp4?token=kq6yPVkWZ_zIxDNVwZ2KopiMg8CQbvthgrVCWVyEnBLo6go1DJ3B2xsm_VzAHjozJy_T7RWfaIipi7FKekeH2HJReofixs5MZKA2AVXTRNEdkOE98zVcZhXCFVW7YWnNcw8E2o0gaDXARLg4DGTdmKJnz_1yS9FyvjsFlPPSf2O_O8wCwEwx7M1LcxTbicJzcqGUNdUtp90aJVL5NYwxubfnKBq7rDsvWIJoXpJyxwKoF39LbcMQLuBXT-PIgP4q9WYWbdwAGGue85Sm9aAl9_q9aoMrd0ni85RxMwLTlXhWAO0-iG2oGnvSV7Oke3IIxVw3v316PnswcyEhDIAenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای سبک که توسط خلبانی ناشناس به سرقت رفته بود، در مسیر پرواز به سوی نیروگاه هسته‌ای «پاکس» مجارستان دچار سانحه شد و در مزارع اطراف سقوط کرد.
🔴
مقامات امنیتی مجارستان تحقیقات گسترده‌ای را برای شناسایی هویت سارق و انگیزه اصلی این اقدام خطرناک آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144550" target="_blank">📅 15:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7iwWsGLD1SNUClZW5ALs8J3w2SwY-uM6MlR4lPK7c_9-9cl_HKvk_0UXj1nnZIx4pVSfZn15SfBfxuFbMCuux5j1OLs2tMgj74A_qUmywrOmY6nk7UqQWzaj88irhIaPDoTFb0JTCzmuPu4zqLHLcpW-aKCYHSr6FcqpKPdBVyzYM8ziKChVrOrRArT5t4ksLZE5-_cAPV2gYcoPaVp9eM3PoYJyHGQkDzHygn-tAGjKYJa2AQy86woHRPT5VGLoXW_F8IH9lBqBvWWIAfV90EQT2mFeC0UFv-bV0KiaJZ6d3gBLNwc6YMkd6yRa4OpKVvSej3zNJXHsl_B3UeqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوگل‌مپ نام دریاچه انتاریوی کانادا را به «دریاچه آمریکا» تغییر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/144549" target="_blank">📅 15:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598d3d3b8d.mp4?token=JcoF4p6ExquzY-CfeTfVJnmrCb8O8XGllaowIgopnBygqAJV_-qEGLpCQEQmvkC6lZrXr4HE-wld6q5ij3Vv4O6I98UlK5Zsnd4gaBTRBrYcJed-sxVPjafj8hfJOfcGgIoSpxSsZ8qxCLzKrELimdThgVhI1RgB1zfM5sLjB_SaEXhLZ14L36hDyhpWYKeJxewyOoUZEsKkFYnUcH9Vt1pA9rRCbvt3Q1EaSg5OLoiDpWqSo92EClftWCOpfhdMVUplVrvc5XQt1gVVCbVcRhPftDSOEWHkdZPYB1Cz3KZrtkAggcpaVRbGv7QMnDdzX7lAbsvz5LpP-87Ry0WzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598d3d3b8d.mp4?token=JcoF4p6ExquzY-CfeTfVJnmrCb8O8XGllaowIgopnBygqAJV_-qEGLpCQEQmvkC6lZrXr4HE-wld6q5ij3Vv4O6I98UlK5Zsnd4gaBTRBrYcJed-sxVPjafj8hfJOfcGgIoSpxSsZ8qxCLzKrELimdThgVhI1RgB1zfM5sLjB_SaEXhLZ14L36hDyhpWYKeJxewyOoUZEsKkFYnUcH9Vt1pA9rRCbvt3Q1EaSg5OLoiDpWqSo92EClftWCOpfhdMVUplVrvc5XQt1gVVCbVcRhPftDSOEWHkdZPYB1Cz3KZrtkAggcpaVRbGv7QMnDdzX7lAbsvz5LpP-87Ry0WzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در جلسه هیات دولت خطاب به رئیس صداوسیما: آقای جبلی! اصلا صداوسیما را نگاه نمی‌کنم؛ وقتی می‌بینم اعصابم خراب می‌شود
🔴
من که زندگی‌ام را می‌خواهم برای نظام بگذارم این نگاه را پیدا کرده‌ام، ببینید مردم چه نگاهی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/144548" target="_blank">📅 15:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پلیس اسرائیل اعلام کرد دو نوجوان ۱۴ و ۱۶ ساله از حیفا به اتهام جاسوسی و انجام وظایف پولی برای مامور ادعایی اطلاعات ایران بازداشت شدند.
🔴
آن‌ها پس از پاسخ به آگهی استخدام تلگرامی با این فرد ارتباط برقرار و دوست خود را نیز اضافه کردند. وظایف آن‌ها شامل عکاسی از مکان‌های مرکز اسرائیل، جمع‌آوری اطلاعات امنیتی مراکز خرید تل‌آویو و هرتزلیه، اسپری‌کردن شعارهای ضد دولتی و جذب نوجوانان دیگر بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/144547" target="_blank">📅 15:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد با ما تجارت کند. من با این موضوع موافقم
🔴
من از تجارت به‌عنوان ابزاری برای صلح و حل اختلافات استفاده می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/144546" target="_blank">📅 15:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الجزیره: پزشکیان قرار است روز دوشنبه برای شرکت در اجلاس دو روزه سازمان همکاری شانگهای به بیشکک، پایتخت قرقیزستان سفر کند.
🔴
پیش‌بینی می‌شود مسعود پزشکیان، شی جین‌پینگ و ولادیمیر پوتین در این اجلاس که به مناسبت بیست‌وپنجمین سالگرد تأسیس سازمان همکاری شانگهای برگزار می‌شود، حضور داشته باشند.
🔴
حدود ۱۲ رئیس‌جمهور و مقام ارشد کشورهای عضو و شریک این سازمان نیز در این نشست شرکت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/144545" target="_blank">📅 15:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
طالبان امروز در بیانیه ای رسما خواستار پایان جنگ با آمریکا و عادی سازی روابطشون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144544" target="_blank">📅 15:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مدیرعامل شرکت ساخت:
هزینه بازسازی پل کرج ۲.۵ تا ۳۰۰۰ میلیارد تومان برآورد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144543" target="_blank">📅 14:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
استارلینک در امارات فعال شد؛ اینترنت ماهواره‌ای به کاربران خانگی رسید
🔴
سرویس اینترنت ماهواره‌ای استارلینک در امارات متحده عربی در دسترس کاربران قرار گرفت و این کشور به یکی از بازارهای مهم منطقه برای اینترنت مبتنی بر ماهواره‌های مدار پایین زمین تبدیل شد؛ اقدامی که می‌تواند جایگاه اینترنت ماهواره‌ای را در خاورمیانه بیش از پیش تقویت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144542" target="_blank">📅 14:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الجزیره: مارک پفایل، مقام سابق امنیت ملی ایالات متحده، اعلام کرد واشنگتن قصد دارد از تحریم‌های ثانویه بر خریداران چینی نفت ایران خودداری کند و این گزینه را برای شرایط ضروری نگه می‌دارد.
🔴
او اشاره کرد که اتخاذ تدابیر گسترده علیه پکن به دلیل پیوندهای اقتصادی عمیق میان ایالات متحده و چین دشوار است، بنابراین واشنگتن می‌کوشد پالایشگاه‌های چینی را تشویق کند تا نفت را از منابع دیگر تأمین کنند.
🔴
پفایل افزود که چین از نفت خام ارزان‌قیمت ایران بهره‌مند می‌شود و انگیزه‌ای برای کمک به واشنگتن در جریان جنگ ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144541" target="_blank">📅 14:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت امور خارجه ترکیه:پیش‌بینی می‌شود که وزرای امور خارجه و دفاع، و فرماندهان ارتش‌های عربستان سعودی، ترکیه و پاکستان در نشست فردا شرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144540" target="_blank">📅 14:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiapA5cR4GNtTBucTIlZxbG9tCGkBv08VJwPb9lFDnv-mR6Y1H0h0YAjYcTSyOMz24rg41R0excTA1Up9yykhmyFtGxB3teIgXNKcq7LnqNL0cxZ94jzSI2BR_zrupOxD_hUGB-QrlWC_js3F7cPFTMAjQOhdbisQUoKGz9VYaYnrVxizxkar4cgqt3x5Lq8p8D7RXD5BKEPi8vEiePs0KT3d8FxhhBRRlQqxtK7bGnZWuE7QlQrSHqtk6Vd2yJibwbQd3sTyWuvvWAxHytj7WSCq7J4wcoixns5zsnKIgHOrWRTkens5SrF7Wqjy_r1ZTE5M75_OufI8a6szm-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن از سنگاپور عبور
کرد
🔴
ناو هواپیمابر آبراهام لینکلن آمریکا، بامداد یکشنبه پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پس از مأموریت در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت.
🔴
خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144539" target="_blank">📅 14:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ادعای تاکر کارلسن، روزنامه نگار معروف آمریکایی: گزینه استفاده از سلاح هسته‌ای تاکتیکی علیه ایران در وزارت جنگ آمریکا مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144538" target="_blank">📅 14:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تلویزیون سوریه گزارش داده نیروهای اسرائیلی در حال پیشروی به اطراف شهر «جباثا الخشب» در حومه شمالی قنیطره هستند.
🔴
جزئیات بیشتری درباره ابعاد این تحرک، تعداد نیروها یا درگیری احتمالی منتشر نشده است.
🔴
این پیشروی، تنش در جنوب سوریه و مناطق نزدیک مرزهای جولان را وارد مرحله تازه‌ای می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144537" target="_blank">📅 14:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بلومبرگ: جناح‌های تندرو ونزوئلا و نیروهای مخالف دولت از دلسـی رودریگز، رئیس‌جمهور موقت، به دلیل توافق نفتی با ترامپ
🔴
این توافق بدون مشارکت مخالفان ونزوئلا مذاکره شده
🔴
رودریگز روی این حساب کرده بود که توافق با ترامپ راه او برای تحکیم بیشتر قدرتش باشد
🔴
این توافق احتمالاً انگیزه‌های امریکا برای حرکت سریع به سمت برگزاری انتخابات جدید را کاهش می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144536" target="_blank">📅 14:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIGfhcDi67XAdZHNEor7InMqMKt0WVlLXGhkCDUrFP1TXCTkeYXIk4YkSl_ZhJH4JIplPQ_X8ASgM6AzOrnzdGfO0XFVk7gqzEoUcRFrcsnTnKKh-E9NQhAz7jaFrPSF8fDBg4Zwh0mflxRl-ZxoM2o3F8UMSm3iRiDvgjqwznu5tkelWRH8zyB8YwlDX4x8enQSdB8RzAVWCvHD0_J3X4srRM9xMxwWW6gafKqtMUzUBN4be5JiNr1_FV0viTABfjr6MPtxAI-GeAJAZU3v9Phj-rochRaOvqfdID2u9BEHHce_QYl-h4k-aZElPB8uo7hQGoCGG-hrpc_wLbVrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزمون تافل هم برای ایرانیان متوقف شد؟
🔴
گزارش‌هایی درباره نبود امکان ثبت‌نام و انتخاب تاریخ آزمون تافل در تهران منتشر شده است
🔴
لغو یا توقف برگزاری تافل برای ایرانیان هنوز به‌صورت رسمی تأیید نشده است اما مجوزی که اخیرا وزارت خزانه‌داری آمریکا لغو کرده شامل این آزمون نیز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144535" target="_blank">📅 13:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴.۸ در مقیاس ریشتر، بخش‌های شرقی خلیج عدن را تکان داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144534" target="_blank">📅 13:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Day-a8Tvlt_hZLjKqMrrwfPmoAZCsCGYA8hXdv6AOw3Zg4HnSYRjGUvTY4vxxb9sTdvFJoWTIAQFwkBF0FOrc9MK5hmjtDK1mpXV_3MFHCFJwh_vr2yuG8xDIhgneM-nrc02MoQ6hfU4p0AH7ucQrLfI8-jh6IXn2iy-5xAKME9s_40tCjVUdYvMsk6ltcx0fHbMQAfPDnC9sD-BntJtP1uwZIbFzLlnO5QZ09g8inQbJZPzw4vePKgIQJj7U3wxU0GyIU87Xy6HRbviNdZcPjyV5V16UrS6IAPPhkGfrgZ1tS2Uai8XCEQP_mMtLUnZMEK_NrobluYwfQIrPO8npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیگار با تورم 160 درصدی رکورددار تورم مرداد ماه شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144533" target="_blank">📅 13:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شبکه کان: ایالات متحده درخواست محمد بن سلمان، ولیعهد عربستان سعودی، برای رهبری یک عملیات نظامی علیه حوثی‌های یمن را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/144532" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز : بانک مصر در حال بررسی پیشنهاد وزارت خزانه‌داری آمریکا برای قطع ارتباط شعب امارات از بانکداری واسطه‌ای دلاری به دلیل تراکنش‌های ادعایی مرتبط با ایران است. بانک مرکزی امارات بازرسی ویژه و فوری از این شعب آغاز کرده است. بانک مصر اعلام کرد عملیات در امارات عادی است و اقدام آمریکا هنوز پیشنهادی بوده و تنها به شعبه امارات محدود می‌شود، نه عملیات در مصر یا سایر نقاط.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144531" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فاجعه سیل در نپال و تبت؛ شمار قربانیان به ۷۵۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144530" target="_blank">📅 13:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تانکر ترکرز: در هفت روز اخیر، روزانه به طور میانگین ۳.۸ میلیون بشکه نفت خام از طریق تنگه هرمز صادر شده است.
🔴
در دوره ۲۵ روزه اجرای تفاهم‌نامه، این رقم ۹.۸ میلیون بشکه در روز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144529" target="_blank">📅 13:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بابک زنجانی در واکنش به پلمپ کافه تازه تاسیسش به علت بی حجابی: ملتی که معیشت ندارد دین هم ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144528" target="_blank">📅 13:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ابوترابی، نماینده مجلس: می‌توانیم اموال کشورهای عربی را مصادره کنیم و اگر اموال بلغارستان و قبرس وارد خلیج فارس شود، آن را مصادره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144527" target="_blank">📅 13:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فایننشال‌تایمز: شورای بازرگانی ایران در امارات، یک نهاد غیرانتفاعی که با هدف تقویت تجارت دوجانبه فعالیت می‌کند، همچنان فعال است
🔴
شرکت‌های هواپیمایی ایرانی همچنان به دبی پرواز دارند
🔴
روابط تجاری ایران و دبی آن‌قدر عمیق است که نمی‌توان آنها را به‌طور کامل از میان برد
🔴
شبکه‌های بازرگانی ایرانی در امارات به‌دنبال مسیرهای جایگزین از جمله عمان و ترکیه رفته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144526" target="_blank">📅 12:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک بازرگان ایرانی به فایننشال‌تایمز گفت: «ما همان‌طور که تحریم‌ها را دور زده‌ایم، محاصره را هم دور می‌زنیم. چیز زیادی تغییر نکرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144525" target="_blank">📅 12:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رئیس مرکز امور اتباع: جمعیت اتباع خارجی به زیر ۵ میلیون نفر رسید
‏
🔴
در طول یک سال گذشته نزدیک به ۱.۸ میلیون نفر از اتباع غیرمجاز از کشور خارج شده‌اند
‏
🔴
جمعیت دانش‌آموزان اتباع خارجی هم از ۶۰۰ هزار نفر به ۳۲۰ هزار نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144524" target="_blank">📅 12:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b1dfb59e.mp4?token=jyEeDoSNY7KvVoSB19N-Fj2R0G3rni4ipNw2bB6RMnLHKGpZ0ux1uYa10S831hv6Gh9pwaJ4McNUsDn1AuQdh8-wbfm19LSp3boT02RSnRYFtgH4TNC9RwP3zv1dYgkb38BhhpiSjDjs5Qo0xS6hbp3kSFFxse_B3fS3fS-4O_kxUUrKBrJLVcx7jutRKyUVwohP4sD0-778UvJSJsHGhlA5Pqu22MahXmYPdkAHlwzdtHkFSbdZNP9d16EttQ0AT1IofwXjq_4xKgR35cyAd9HqNmg-QShFV1dlmVrbgy92i-mRcuBFB20mCDhks7Y5suH55WiRlreDj6k-oJsf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b1dfb59e.mp4?token=jyEeDoSNY7KvVoSB19N-Fj2R0G3rni4ipNw2bB6RMnLHKGpZ0ux1uYa10S831hv6Gh9pwaJ4McNUsDn1AuQdh8-wbfm19LSp3boT02RSnRYFtgH4TNC9RwP3zv1dYgkb38BhhpiSjDjs5Qo0xS6hbp3kSFFxse_B3fS3fS-4O_kxUUrKBrJLVcx7jutRKyUVwohP4sD0-778UvJSJsHGhlA5Pqu22MahXmYPdkAHlwzdtHkFSbdZNP9d16EttQ0AT1IofwXjq_4xKgR35cyAd9HqNmg-QShFV1dlmVrbgy92i-mRcuBFB20mCDhks7Y5suH55WiRlreDj6k-oJsf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هلی‌کوپترهای اسرائیلی بر فراز درعا در جنوب سوریه پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144523" target="_blank">📅 12:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دلار هم اکنون 208,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144522" target="_blank">📅 12:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl4NV7YXmWXHgoerNcEACorNfIZ-QLvqOpYuMt7hoDgLvy-lyxCM3rJIRlyE1cEtm4cYcrEoniUeiAK1Ki9GN1QidHmbGRaumxNLLn-3aEYNBch4eTNDsL7mOFxxnCQny7hpluD-i3A0UejDxTVSOPVyPykR-UJ0zb9UFC6M5SP3uHPjhf4qS6eMK7187iU3vA1zQoUAyMC226Ux8iCN37AcyHsplremEAxBaLEPS35MFggQ8uLgXO3c4zIxCy5d8A_dyGRKpySiZOa0OhoGOE2oMWaHpzELKm1wo7t8w6NdN6xMlLMTb_eGAqI8miATfEOacAgQc07GW1IMQbNCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ نزدیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144521" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447286c66f.mp4?token=mMnTnPg01evb3n02LdyNy7PXvqI7wpP1If6KTS4DD0xfNr5wWmVL-rYz3pmTQSVgTb9OoojW7LkTMWe6MrLTlsC7LNSwqeJCG71Gn16m1SQNBPjwK4j1McZoOLVBoew_vQoFEEHZ_4SGhk2HPuby3kqnvLqTVyiFchUK2Mt9SBKGYqXn1sKlOxIv7Xbf-4OssTJN0x38I77p9GjHi8J4hl0HylKwCm9yO764X3HopqZM3d14Z5eDYvhqz1Ief2jen816qiMxoy9x1_MqFbA9kLInbcfu9RkYPpOKwkOiqR2YYLC3QJ-h8Fpxd7Li2rUf-tm4VVpULUVx-p5qFGPT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447286c66f.mp4?token=mMnTnPg01evb3n02LdyNy7PXvqI7wpP1If6KTS4DD0xfNr5wWmVL-rYz3pmTQSVgTb9OoojW7LkTMWe6MrLTlsC7LNSwqeJCG71Gn16m1SQNBPjwK4j1McZoOLVBoew_vQoFEEHZ_4SGhk2HPuby3kqnvLqTVyiFchUK2Mt9SBKGYqXn1sKlOxIv7Xbf-4OssTJN0x38I77p9GjHi8J4hl0HylKwCm9yO764X3HopqZM3d14Z5eDYvhqz1Ief2jen816qiMxoy9x1_MqFbA9kLInbcfu9RkYPpOKwkOiqR2YYLC3QJ-h8Fpxd7Li2rUf-tm4VVpULUVx-p5qFGPT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از طوفان در مالاتیا ترکیه
🔴
تصاویر منتشرشده نشان می‌دهد که شدت باد به حدی بوده که تابلوها و اشیاء سنگین با سرعت بالا در میان آسمان به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144520" target="_blank">📅 12:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prjkJowjSQV9L2ix77HaMNOuY6AY4Nb8S7ExpnNLpVaVF5gOuyo_oVTtvjc_AqDMppgsEWtE_qnFgvmgPu5IVeHEq7BQeVMXZvevG1DO7mQ3m3cckeZN0-xsdO7Psuoat3_Ftvv1lb2GnmyG2yNASkKnmbvDE79hCOuzAxjDPpB5D0lTyhmRgBo08gxWKpZEiR7ul4XYvLt8pGn6YVg5UAIHmbYv5HfHrTDKwvUDBN4IaqOuTMTeh0cqjUxIPu6f2X9hv2BOXLwEKkLeJhIp2h9uS-fA0SXkjRqWca5wpV7EE2q2oMM5oyV1xHupobS-SlcJo5sPkvWIUv8-X2abow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو اسکادران جنگنده F-16 به همراه تعدادی هواپیمای ترابری نظامی به خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144519" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مجری صدا و سیما: آمریکا و اسرائیل فقط دنبال این بودن بمب رو مردم غیرنظامی ما بریزن!
🔴
دوستان تایید میکنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/144518" target="_blank">📅 11:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
عراقچی: ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144517" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس‌جمهور چین وارد پایتخت قرقیزستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144516" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ثبت احوال: ۷ میلیون و ۵۰۰ هزار کارت ملی هوشمند به مردم بدهکار بوده‌ایم که این رقم به ۶ میلیون کاهش یافته
🔴
بسیار امید داریم که تا پایان پاییز امسال، این بدهکاری‌ها تمام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144515" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Jo1XMEwzd7rmd9-b2fjse2Ev1DY2FLts8yOKV-d5cTUEuDzishrBzWtwFgQ11rM_RUNpMyf8ECojfk_2Cq8hQ4wH-thYzda7L4uooQGSdG3ry2HZPscMSc7FohTLvhB_momx9APkpCZwjux98AwMnYF8WKPwhSWlQ7OZ3CNvtjN3Az15rFtldYDt1lDBVgmIJrWON_0IC4KImhXW6WJmH3S-q3k6LAq_CvASeqJTAOjrQedswb5VQZ5yZHWkWkZTYfIzQfcbO9sDFU21LFdAWVKBV273z_vfg2ysavHE27Ou6m6wsKXeAewNuQd4pc_9A6RHsVM3H98nqSXsrBVusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Jo1XMEwzd7rmd9-b2fjse2Ev1DY2FLts8yOKV-d5cTUEuDzishrBzWtwFgQ11rM_RUNpMyf8ECojfk_2Cq8hQ4wH-thYzda7L4uooQGSdG3ry2HZPscMSc7FohTLvhB_momx9APkpCZwjux98AwMnYF8WKPwhSWlQ7OZ3CNvtjN3Az15rFtldYDt1lDBVgmIJrWON_0IC4KImhXW6WJmH3S-q3k6LAq_CvASeqJTAOjrQedswb5VQZ5yZHWkWkZTYfIzQfcbO9sDFU21LFdAWVKBV273z_vfg2ysavHE27Ou6m6wsKXeAewNuQd4pc_9A6RHsVM3H98nqSXsrBVusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدویی از روش جالب روشن کردن مشعل گاز فلر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144514" target="_blank">📅 11:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de36d36926.mp4?token=KwdBzI3XEvFNmCRfRflt5LJZQeXhRFbW1S23MOqHMmd_JyzPuhabBDH8cR0zCJqDvfV5fL2NRUtnW2KOsPWM8cSiZsXtZ5Oku7UtFW1Lw4PelfEupppNd8G2t8FwubPoa2ExRw961iJ1U-JQkbbLEFOqiA8jFaZO8cqO94-hucSdoi1OQ9FI2vqa2M_i8dbWru-LB0vn0hkINL7LYrDTdM1Un0_uVWDYk-sS3394ldcA1aLCuRhOWAOKK6pV4peAawEd3ynihdIN0JlBkoKjn13k3D8In6RjCec_nPesrV9sxtTEjHG23KN-lUtDyx9RxrTDT2yuiDhuesSEh_0fMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de36d36926.mp4?token=KwdBzI3XEvFNmCRfRflt5LJZQeXhRFbW1S23MOqHMmd_JyzPuhabBDH8cR0zCJqDvfV5fL2NRUtnW2KOsPWM8cSiZsXtZ5Oku7UtFW1Lw4PelfEupppNd8G2t8FwubPoa2ExRw961iJ1U-JQkbbLEFOqiA8jFaZO8cqO94-hucSdoi1OQ9FI2vqa2M_i8dbWru-LB0vn0hkINL7LYrDTdM1Un0_uVWDYk-sS3394ldcA1aLCuRhOWAOKK6pV4peAawEd3ynihdIN0JlBkoKjn13k3D8In6RjCec_nPesrV9sxtTEjHG23KN-lUtDyx9RxrTDT2yuiDhuesSEh_0fMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوت ناگهانی، هنگام سخنرانی شبانه!
🔴
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144513" target="_blank">📅 11:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d179adfd44.mp4?token=pAuWrQ1GItJzm-tDL9dcD9a_7vXlQCBxq5Bz305KmeWTo9e3AmUbnafESII9oeCkJTRmpI9ZUlpnl7Ji5Mt5wLI92VIoNW63vxdgyqGTautfioHuHIcxFz888wqNqG4DWrG_iKCEuLZIFBa4M0oYizjq6YCBHhOGKO5A7Mz1Z-y83bSqzSilVIxZhpzdGxHGnIkl3tLknrKXuwlLWCKQrOdtjKKHOGHCjXa-CLwU-7gdO-zleE-39lplpJTTz0LqP53r5gYImzpJ41a9oEl2uFpbV6U10nJXRJDRk3i4M8Sf7zUEtMyqblIE7fUvNnm_Vb-taRVoR7usN5AmzPb6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d179adfd44.mp4?token=pAuWrQ1GItJzm-tDL9dcD9a_7vXlQCBxq5Bz305KmeWTo9e3AmUbnafESII9oeCkJTRmpI9ZUlpnl7Ji5Mt5wLI92VIoNW63vxdgyqGTautfioHuHIcxFz888wqNqG4DWrG_iKCEuLZIFBa4M0oYizjq6YCBHhOGKO5A7Mz1Z-y83bSqzSilVIxZhpzdGxHGnIkl3tLknrKXuwlLWCKQrOdtjKKHOGHCjXa-CLwU-7gdO-zleE-39lplpJTTz0LqP53r5gYImzpJ41a9oEl2uFpbV6U10nJXRJDRk3i4M8Sf7zUEtMyqblIE7fUvNnm_Vb-taRVoR7usN5AmzPb6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل
:
دونالد ترامپ رئیس‌جمهور صلح است.
🔴
او دیپلماسی را در اولویت قرار می‌دهد و شما به یک مکان در جهان نیاز دارید که همه حداقل بتوانند آنجا بیایند و صحبت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144512" target="_blank">📅 11:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf358072ce.mp4?token=SiKgUElhN9L-pTwVfIpofj2dByvHYk-5b1Ys6roPefXrjDSvub_whnK3DkJZyegPLSWtN2V96Yv1k3Agp0FA0iWxF2m3Fl6ph-YFzmKEumHCTT9VUhmzYe-qRdsezpBcIB1iAZ4xjMHeKdaLPtchn59k7rlx-PQE56LhQkP_0tPGlOICksl4qolm8yZrSgwUKMS91rvFFcWbtaxI6y0AUgCNO6cHIGn9WUYDQu-9ZG-16HwEij1GG8jc5CcwQulkAG-_g0g-ThKQDAqfwnxiA0XU0imzzIPERiBlsfwt_IhOxXFIjO_uPQ4mCQ3RZykKwgyeCvDzdcVg7b8MhZ9KBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf358072ce.mp4?token=SiKgUElhN9L-pTwVfIpofj2dByvHYk-5b1Ys6roPefXrjDSvub_whnK3DkJZyegPLSWtN2V96Yv1k3Agp0FA0iWxF2m3Fl6ph-YFzmKEumHCTT9VUhmzYe-qRdsezpBcIB1iAZ4xjMHeKdaLPtchn59k7rlx-PQE56LhQkP_0tPGlOICksl4qolm8yZrSgwUKMS91rvFFcWbtaxI6y0AUgCNO6cHIGn9WUYDQu-9ZG-16HwEij1GG8jc5CcwQulkAG-_g0g-ThKQDAqfwnxiA0XU0imzzIPERiBlsfwt_IhOxXFIjO_uPQ4mCQ3RZykKwgyeCvDzdcVg7b8MhZ9KBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل متحد
:
شما یا با ما هستید یا علیه ما. نمی‌خواهید در کنار ایران بایستید.
🔴
رئیس‌جمهور ترامپ جهانی را در نظر دارد که در آن فرزندان ما توسط یک رژیم اسلامی نسل‌کشنده که سلاح‌های هسته‌ای دارد، ترسانده نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144511" target="_blank">📅 11:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b826c1015.mp4?token=piF0Su8dHOrtPRpu3KvA3pyK7JBrlfQ0r0mnY69tkRa0GbLHgLXzHZbq8n0au4yxsg4OT-u-md-D7bzU_NNzJ5D9j1rHTQ1Mb1oSR4zpso-NTXgq04N1_ejhbnmQji8MeKrnRophODkfHS7vbK0W3zJW9xbu39vD7IAtSY3LXVOQhXsG_6SrM5DTEWkEjnyrIjy5UURFYg2m7TXwuH9MW7QBEhFjoLsQli0IAkHczlVRP-Ade_iQxi-hLIB9_A8zgMwT9VD4mujwphPIr0CFx9efeEol3r-cgKmBxTPr7UDNENrjYoNNQGnn8j-mNRxPNzvnZdIgjCyM_eNzNlUqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b826c1015.mp4?token=piF0Su8dHOrtPRpu3KvA3pyK7JBrlfQ0r0mnY69tkRa0GbLHgLXzHZbq8n0au4yxsg4OT-u-md-D7bzU_NNzJ5D9j1rHTQ1Mb1oSR4zpso-NTXgq04N1_ejhbnmQji8MeKrnRophODkfHS7vbK0W3zJW9xbu39vD7IAtSY3LXVOQhXsG_6SrM5DTEWkEjnyrIjy5UURFYg2m7TXwuH9MW7QBEhFjoLsQli0IAkHczlVRP-Ade_iQxi-hLIB9_A8zgMwT9VD4mujwphPIr0CFx9efeEol3r-cgKmBxTPr7UDNENrjYoNNQGnn8j-mNRxPNzvnZdIgjCyM_eNzNlUqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیفون 17 پرو، رکورد سقوط آزاد رو شکست؛
🔴
این گوشی با استفاده از قاب محافظ RhinoShield AirX، از ارتفاع 30 کیلومتری رها شد و بدون هیچ‌گونه آسیبی سالم موند و تو کتاب رکوردهای گینس ثبت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144510" target="_blank">📅 11:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3784a4f2c0.mp4?token=Eew-sdJHcvREpLBO0eUDGJJ5qhFg4q6nw0lN3vfDrEOQ7BP7NK4lDTs3dA6ohwehHUztrgRlBqgkC6s9m-cNtCXbFRQB0rCqXCyPZqPITSizogcBBHqlT9JZvgK6Bu4K95mnCUgjbqVwTxfsOX_5KtlsjR139S2yCLkoTqla2-OqJXPz1N0GSoEDF5jZ8mYuuSnb4_0bOCUhRExIsNCB4XHE2sVP2AK19-F2brQ4k6LADuV3N-BetVejbDE_VqyYAyJxVTZMjmtP-8v-1WFNMkKkP5VL9Bc7i2mwglF9KlpRNqc3WpME5KeRYWdQmU5R8WNH6TzbAvpQydxNBfd7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3784a4f2c0.mp4?token=Eew-sdJHcvREpLBO0eUDGJJ5qhFg4q6nw0lN3vfDrEOQ7BP7NK4lDTs3dA6ohwehHUztrgRlBqgkC6s9m-cNtCXbFRQB0rCqXCyPZqPITSizogcBBHqlT9JZvgK6Bu4K95mnCUgjbqVwTxfsOX_5KtlsjR139S2yCLkoTqla2-OqJXPz1N0GSoEDF5jZ8mYuuSnb4_0bOCUhRExIsNCB4XHE2sVP2AK19-F2brQ4k6LADuV3N-BetVejbDE_VqyYAyJxVTZMjmtP-8v-1WFNMkKkP5VL9Bc7i2mwglF9KlpRNqc3WpME5KeRYWdQmU5R8WNH6TzbAvpQydxNBfd7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیلی به ارتفاعات الدبشه در جنوب لبنان هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144509" target="_blank">📅 10:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
جنگ هوش مصنوعی به مرحله تازه رسید؛ OpenAI مقابل ایلان ماسک
🔴
شرکت OpenAI اعلام کرده قصد دارد ارائه مدل‌های هوش مصنوعی خود به Cursor را متوقف کند؛ شرکتی که اکنون تحت مالکیت SpaceX قرار دارد.
🔴
رویترز این تصمیم را تازه‌ترین مرحله از اختلاف فزاینده میان سم آلتمن و ایلان ماسک دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144508" target="_blank">📅 10:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع مطلع:
رئیس سازمان سیا در جریان سفر محرمانه خود به روسیه، پیشنهاد برگزاری یک نشست سه جانبه میان ترامپ، پوتین و زلنسکی را با هدف پایان دادن به جنگ اوکراین، مطرح کرده
🔴
مقام‌های اوکراینی می‌گویند «پوتین در حال برنامه‌ریزی برای تشدید عمده جنگ است»؛ این موضوع مانعی بر سر راه تلاش‌های دیپلماتیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144507" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از منابع غربی:روسیه، هواپیماهای بدون سرنشین اوکراینی را تصرف کرده است که ممکن است از آنها در عملیات تحریک‌آمیز علیه کشورهای عضو ناتو استفاده کند. این در حالی است که هشدارهایی درباره افزایش فعالیت‌های روسیه در اروپا وجود دارد که شامل نفوذ با استفاده از هواپیماهای بدون سرنشین، خرابکاری و حملات سایبری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144506" target="_blank">📅 10:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c0f6ac56.mp4?token=dH5-AYHHspCc9pThjP4ZOzjVvQqhOVliQnW64M42CA2VpqW7ZvJzrjzj5g-3xxyHbOJPGyf3vMkHEE_mdw2_aJenHNHzBW9M_cd5A0yU4aDW-_plJFjn-ZW6b1MwyGKFTn52zvuUpLl9ch2r1E4iKOtNVNzOYuQzsC9ze2LcNI3xFYzAvLM7yLsHg88cVNMInrX7o8qx-ABQk7340NHCudAxxZyVonf2mFtmB_YzGcOizC3CZPtwKY95URWx80WmRi1KqJSD47z24jDKY2OOU5tA5MsG8nDRYvVZcolAyu3OqmF1PwNs0RJJ4UioEr5jedAA2ebAo4qYBW-JZQ2Kbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c0f6ac56.mp4?token=dH5-AYHHspCc9pThjP4ZOzjVvQqhOVliQnW64M42CA2VpqW7ZvJzrjzj5g-3xxyHbOJPGyf3vMkHEE_mdw2_aJenHNHzBW9M_cd5A0yU4aDW-_plJFjn-ZW6b1MwyGKFTn52zvuUpLl9ch2r1E4iKOtNVNzOYuQzsC9ze2LcNI3xFYzAvLM7yLsHg88cVNMInrX7o8qx-ABQk7340NHCudAxxZyVonf2mFtmB_YzGcOizC3CZPtwKY95URWx80WmRi1KqJSD47z24jDKY2OOU5tA5MsG8nDRYvVZcolAyu3OqmF1PwNs0RJJ4UioEr5jedAA2ebAo4qYBW-JZQ2Kbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی به یک هدف در منطقه برانسک روسیه حمله کرد و به نظر می‌رسد انفجار که در نتیجه این حمله رخ داد، ناشی از انفجار مهمات بوده است.
🔴
گفته شده یک سامانه اس ۳۰۰ روسی آنجا منفجر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144505" target="_blank">📅 10:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دیلی بیست به نقل از منابع آگاه: ترامپ امید خود برای حل‌ درگیری با ایران را به جای وزیر جنگ، به وزیر خزانه‌داری سپرده
🔴
این تغییر رویکرد پس از آن رخ داد که ترامپ با عصبانیت هگست را درباره کاهش ذخایر مهمات ایالات متحده مورد بازخواست قرار داد
🔴
دولت آمریکا به این نتیجه رسیده که تهران با فشار نظامی، امتیاز نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144504" target="_blank">📅 10:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر دفاع کره شمالی به عنوان بخشی از تغییر در رهبری نظامی این کشور، برکنار شد
🔴
رسانه های دولتی کره شمالی گزارش دادند که وزیر دفاع این کشور به عنوان بخشی از تغییر در رهبری نظامی پیونگ یانگ برکنار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144503" target="_blank">📅 10:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بلومبرگ: تلوزیون دولتی روسیه نحوه نابود کردن بریتانیا با بمب اتم را بررسی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144502" target="_blank">📅 10:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febae98a7f.mp4?token=D_rTLnQVEjY78JgcikXEMNYARrrLD_ECW3_c2Azr2E89pX8LcEsIN45rg5ZkEt72qRMG9jlnY3OCm-QBOV9RZigD0CX28Q21meg5l_3b-TCnPSivUqNTUAAQWHF1GTiWjwKuTbwrYZNQT6uZE0SuAYXEx85kv1tfOGMyGE_oXUUlWi4CFDIZOrCoZHPOKBw0BMy7SGY_6Jv8PSi3pIDA4wMKevC5lfD40ATDOpCienjXWtNv0QWronVeDNSnXSHssXbxZDnnKCohfVuP5WvPJNHw1HN--T44rxFkAHWkzEA1CYR-vkiCH4IoLCPMMVsAWV6IenLjotbi1Yj2ycBHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febae98a7f.mp4?token=D_rTLnQVEjY78JgcikXEMNYARrrLD_ECW3_c2Azr2E89pX8LcEsIN45rg5ZkEt72qRMG9jlnY3OCm-QBOV9RZigD0CX28Q21meg5l_3b-TCnPSivUqNTUAAQWHF1GTiWjwKuTbwrYZNQT6uZE0SuAYXEx85kv1tfOGMyGE_oXUUlWi4CFDIZOrCoZHPOKBw0BMy7SGY_6Jv8PSi3pIDA4wMKevC5lfD40ATDOpCienjXWtNv0QWronVeDNSnXSHssXbxZDnnKCohfVuP5WvPJNHw1HN--T44rxFkAHWkzEA1CYR-vkiCH4IoLCPMMVsAWV6IenLjotbi1Yj2ycBHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ ویدیویی تولیدشده با هوش مصنوعی منتشر کرد که در آن تابلوی دریاچه انتاریو را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس به ریتم آهنگ «ای‌ام‌سی‌ای» (YMCA) می‌رقصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/144501" target="_blank">📅 09:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سدهای خراسان رضوی فقط هفت درصد آب دارد
🔴
آب موجود در سدهای تأمین‌کننده آب مشهد شامل: دوستی، طرق، کارده و ارداک نیز فقط ۳۸ میلیون متر مکعب و معادل سه درصد حجم ذخیره آنهاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144500" target="_blank">📅 09:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvzihKQfx0FtjsS_SXm0VHup29D6zDnUEWVohx-9leQV4e5KR7xASO-QSh7_u7TD2ZCxDKfskxqRJ6L9VOHGNT6yAGxEYJA7BiDO7FgzW7OQfzfh2TEVEGcAdsODtAW0EnspW6QNUOtBpUqU-YQ1vfZ8VmOB_4pHfzrVML4So_p7o0TAcNEExx1PNSgSD11Ydn0SFp8ceByRfEGrm55_18YPYR8ku2I5pIwhDOR-mADAiRxf3pR8yEZGFg4UfAlgLJRHEfx2xA1nNRwCDY_0sbau0VF1N_OEWsl0BAyuVsE6Dd-DdjQZ9BEW-Cr3x5anW4zKwUKFAf2OCA1LM4YYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سال پیش جلوی واردات لوازم خونگی رو گرفتن که قیمت‌ها بیاد پایین
🔴
اما الان قیمت کارتن لباس‌شویی شده ۲.۵ میلیون!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144499" target="_blank">📅 09:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLh5cVRwEroB3Ax3x6eV1ZKrQ3Yp1FkGO-oYnLDADUdljuLSCsk2pN7rsw_9wJTwOP-w-jfD8XEkQzVAUkYTgpBBB9f3zKGByWncWcwuXVlHLXRl8aI4xIkIe_NEmSQGIfZdHar3ABKlExyWKohisJ1UDa6-I10exAnys6PFYbAfntE49Mnq3DK7IfqASQJnJFM0my-iMNlw3KBSE0YkRyZ15UVSdOqAzVvI-xumz-gLFCttrHEK4LeEoAxeF7GF9-8iC46YN-ebE2cw3fiOsk9PnnX81ExzhXcKRtD6q5gchayGx1aZR1FVgHtwnYDtQRgJKtVIEYPQk85Hr96lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک آدامز، نویسنده و فعال رسانه‌ای جنجالی آمریکایی در واکنش به صحبت‌های ترامپ در مورد نفت ونزوئلا: ایالات متحده تقریبا همین کار را با عراق هم انجام داد و تا به امروز، تمام درآمدهای نفتی عراق به بانکی در شهر نیویورک منتقل می‌شود. این همیشه یک عملیاتِ غارت و چپاول بوده که امپراتوری علیه کشورهای جهان به راه انداخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144498" target="_blank">📅 09:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه اسرائیلی «کان» مدعی شد که عربستان تلاش کرد آمریکا را به اقدام نظامی علیه یمن متقاعد کند، اما واشنگتن درخواست ریاض را رد کرد.
🔴
طبق این گزارش‌ها، عربستان اصرار زیادی به همراهی آمریکا داشت اما واشنگتن «لحظه آخر» پشیمان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144497" target="_blank">📅 09:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394581bae.mp4?token=MGD6VCSLPPNFrCoGkrRpBaG2caXWzyxfk26K3Thvs6dK6-t01tWiqrlcdXBnS0a2yT8WBOC5jQa8IL6sLjPhfQMXNUarddgqmN8bl4mdmRC9dhVr0ZtFT5lQabt7s3R6xej6v0hU_tgj_Di2SR_lZfm6V-njTSTRPuM-hNiOIL_cwgQLjcNKvWWuzhQNL4XuHrBylciAnkGIKDCDfFtnlLUzAH2_510f-S2NF5Nsn1480GgHTkuYIFtuFcKIHtEVxvzFzdzXsgZigEdyc7pceOQneJNOLUSTlnpk5RCgmyM6s-CgOvmL_HUXY3kajCOp8AW-IOTn-3K_utI0YVquDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394581bae.mp4?token=MGD6VCSLPPNFrCoGkrRpBaG2caXWzyxfk26K3Thvs6dK6-t01tWiqrlcdXBnS0a2yT8WBOC5jQa8IL6sLjPhfQMXNUarddgqmN8bl4mdmRC9dhVr0ZtFT5lQabt7s3R6xej6v0hU_tgj_Di2SR_lZfm6V-njTSTRPuM-hNiOIL_cwgQLjcNKvWWuzhQNL4XuHrBylciAnkGIKDCDfFtnlLUzAH2_510f-S2NF5Nsn1480GgHTkuYIFtuFcKIHtEVxvzFzdzXsgZigEdyc7pceOQneJNOLUSTlnpk5RCgmyM6s-CgOvmL_HUXY3kajCOp8AW-IOTn-3K_utI0YVquDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود سامانه بارشی به غرب و شمال غرب کشور و صدور هشدار نارنجی سازمان هواشناسی برای برخی نقاط
🔴
هوا در نیمه دوم هفته خنک می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144496" target="_blank">📅 09:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حمله اوکراین به پالایشگاه ۴۰۰ هزار بشکه‌ای روسیه
🔴
پهپادهای اوکراین، پالایشگاه ۴۰۰ هزار بشکه‌ای روسیه در کیریشی را منفجر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/144495" target="_blank">📅 09:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: سازمان امنیت داخلی اسرائیل می‌گوید پس از اینکه تهدیدی جدی علیه جان پسر نتانیاهو شناسایی شد، فوراً از آمریکا به اسرائیل بازگردانده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/144494" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
👈
۳ ساعت تاخیر تا الان در پرواز کاسپین تهران استانبول
‏
🔴
پرواز شماره ۷۹۰۲ هواپیمایی کاسپین که قرار بود ساعت ۶/۱۵ صبح به مقصد استانبول پرواز کند، به ساعت ۸/۵۰  دقیقه صبح موکول شده است، اما هنوز ساعت پرواز تایید نشده.
‏
🔴
هیچ مقام‌مسئولی در باره علت تاخیر پرواز، توضیحی ارئه نمی داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/144493" target="_blank">📅 08:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وال استریت ژورنال: فعالیت‌های تجاری و بانکی ایران در دبی، با وجود هشدار‌های آمریکا و اعلام پایان روابط، همچنان به طور علنی ادامه دارد
🔴
وال استریت ژورنال نوشت: اسکات بسنت، وزیر خزانه‌داری آمریکا، هنگام اعلام «روز دی اقتصادی» (Economic D-Day) به‌صراحت گفت که آمریکا دیگر در برابر کشورهایی که از فعالیت‌های اقتصادی ایران حمایت می‌کنند، چشم‌پوشی نخواهد کرد. اما یک گشت‌وگذار در دبی نشان می‌دهد که این فعالیت‌ها همچنان در برابر چشم همگان در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144492" target="_blank">📅 08:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عراق: تلاش می‌کنیم پلی برای ارتباط میان ایران و آمریکا باشیم تا به توافقی دست یابیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/144491" target="_blank">📅 08:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یله نیوز گزارش داد: فنلاند به دور از توجه رسانه‌ها یک یادداشت تفاهم‌ محرمانه ۱۰ ساله با اسرائیل امضا کرده که شامل تحقیق، توسعه تجهیزات نظامی می‌شود و روابط نظامی دو کشور را گسترش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/144490" target="_blank">📅 08:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
👈
آکسیوس به نقل از یک منبع: مقامات اوکراینی گفتند که اطلاعاتی در اختیار دارند که نشان می‌دهد پوتین برای تشدید بزرگ جنگ برنامه‌ریزی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/144489" target="_blank">📅 08:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جروزالم پست: اسرائیل فردا توافق‌نامه‌ای را با یونان برای فروش یک سامانه پدافند هوایی جهت مقابله با تهدیدات احتمالی ترکیه و ایران امضا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/144488" target="_blank">📅 08:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVmFvZjK6rzbbICp9CiinM8OlFKeKirGRNG-2Ei9QchgiES6CXE-8BM9E1BJPe33RtDDMPuYDO_sa7hDdLimzvzmJVEkl2aluRbqPAazwEhFgwaeFBcAgV0N-BvowiLq2m6QYpnvJOfXd9LMTsJk_sVMYMi3_bzad7KdSOgYOXXYVW_oHdARFqVsAqqxQGj2UYauDSkDNHboOHBZg2YnMbG2j3SrdiWbke-AqhD8JfbuDWq0Fhl0iMqTQI6nTT7-6Uw7QSzKtki2-7zRfCD5RA9VKpjaY2usEmqrzmkDROS8ui5pjsJgOk1OezATk5_0M09cVm6BImRDoNc3KWHBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش کان نیوز:
ولیعهد عربستان سعودی، محمد بن سلمان، از ایالات متحده خواست رهبری عملیات نظامی علیه حوثی‌های یمن را بر عهده بگیرد. این درخواست در جریان دیدار با ژنرال براد کوپر، فرمانده مرکز فرماندهی نیروهای مرکزی (سنتکام) مطرح شد. واشنگتن رهبری مستقیم این عملیات را با این استدلال رد کرد که حوثی‌ها کشتی‌های آمریکایی در دریای سرخ را هدف قرار نمی‌دهند، اما موافقت کرد تا از عملیات‌های عربستان علیه این گروه حمایت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144487" target="_blank">📅 02:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSrm1hN4rTzGDk0IMF1MpkKv_Yc5gPBfjx_YinFOrRyQ1oUbcLYywksyyJRX39Rnsl75pvcTWpZpNoff1D3xoP5t1tFDpKl4WgV01ccVdRd2sJNo6bK6tNHioosmaeEVAd1mrcIHzulgPtetUJb1bnwZofe8fmEEjqua_4QW6vVouPIFGQbWqnoeXg_Df55Tqr51vjDtRQd0K0jM41Ewv_cXhhcgDMvc5BhNfQD0Gj3ZfyI1i7rqXAkSxd5dr58V-W98_Eo3GTBpPIYpjDmDx8tJUnHCs0lBqNtfJJXrOcBvb8PQKpTcQ87twn88JJztbZT1SrTbvTXTpmxzLvp3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادای احترام جامعه پرورش اندام به جاویدنام مسعود ذات پرور در مسابقات کشوری اصفهان
🔴
مجتبی ملکی، رئیس فدراسیون کچل خایه مال هم این اقدام رو محکوم کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/144486" target="_blank">📅 02:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f066db6043.mp4?token=YecAIl82dTXAf7LBR_SNEJJVwDDGV_NoQyDD2RZA5c69pJTALedweWRco7fvHwjghJP_7iRmS_C6Z6g0UoCs07O_98b_WRt-4e6OIeOz6Af-gjcDsY7K2nLaw4WQm2Hp5IveB7vqOv7JcVkJ0YX9b4SHe3yK3nRNfwz2o5cOLWcY-io7VShwvUsdZr0T6isQalUWNKoXoFcgv1ofCiHFIoNh99YmrfaltmHx9p7q5c_9NEvLSbHn-aMbGHmznzQsnxS2s9Ffhii5XiACJXcc4qPpdN9Mj2HvetmTqgAsFxUdKgHFIL6pb6CyK1fd9pF9a3suiHiNTJwhuuc1Bwm7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f066db6043.mp4?token=YecAIl82dTXAf7LBR_SNEJJVwDDGV_NoQyDD2RZA5c69pJTALedweWRco7fvHwjghJP_7iRmS_C6Z6g0UoCs07O_98b_WRt-4e6OIeOz6Af-gjcDsY7K2nLaw4WQm2Hp5IveB7vqOv7JcVkJ0YX9b4SHe3yK3nRNfwz2o5cOLWcY-io7VShwvUsdZr0T6isQalUWNKoXoFcgv1ofCiHFIoNh99YmrfaltmHx9p7q5c_9NEvLSbHn-aMbGHmznzQsnxS2s9Ffhii5XiACJXcc4qPpdN9Mj2HvetmTqgAsFxUdKgHFIL6pb6CyK1fd9pF9a3suiHiNTJwhuuc1Bwm7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادای احترام جامعه پرورش اندام به جاویدنام مسعود ذات پرور در مسابقات کشوری اصفهان
🔴
مجتبی ملکی، رئیس فدراسیون کچل خایه مال هم این اقدام رو محکوم کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/144485" target="_blank">📅 02:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3d8xihAQ_LClPHr1YClAap9OnErVkTWl9u8vo0eaM7HHDia4Gi-kjRpPgQGnVAOz7nhVXLI51Xbi4gkBcA5UvTDgK_zEDnHWRifi8OZhrasYG3f6w6sXIy2O4JB7wU_V2JuBDHMi_-njCaQBR2oKh_9OppAv9NCyVia_c1SpZ7PE_5cok4AnSPhBqZ9fTzJgb0yPy3ZRkyyu1RLAxP3V855F8lI0M3RQC2I-CrhW_eFT-ipDwyMHxDV02Rg_OPVvx6h7ytWid7Ba31RWovc2DsLODxLHAuk3k2Fx95iyC6c3ixBzg15QjC7cNXN0cWcIPZFvvoZjxCdQkdJLZYvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد لواسانی، رئیس سابق کانون صرافان ایران هست که حدود ۴۰۰ میلیون دلار پول کشور را برد و پس نداد، که دیروز بازداشت شد
🔴
وی همواره بر حفظ شعائر انقلاب تاکید داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144484" target="_blank">📅 02:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
طبق گزارشات تو چند روز اخیر، ماشین تعدادی از هموطنان به مشکلاتی مثل "خاموشیِ یهویی ، لرزش یا سوختن موتور ، ریپ زدن ، بد استارت خوردن ، دیر روشن شدن و..." خورده که بعضی‌ها بنزینِ بی‌کیفیت رو علت اصلی این مشکلات میدونن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144483" target="_blank">📅 01:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J49G0j6CDeY0Q0MhR99nrz6IppskmiltUe5MQ33VaBLalz_r4FpUQ_5zGToVxdr78MRvWPNlLibUgP9CRp9eQ7RxYSUZNeGWyb1YpGuxu-HRhb-IujfyRd7Nbqfvjt17onufXaHeQEZKJlwlF5XobP9mm2DSDeSEGElwzPyw3pRVXtBGSS3nx70oPtinPh_NmjOgDFwCVVu5Kv4r4ZL8eZXNa6BGF7btb4VZvJgpf4qUJE4Ri4kntQRAsIu75uviOTw0mdNUGwQrFSmtZfCDMzAHVTl8gUqj2c-FON84phdgYaTUfOVeedBL-y_0nQOPmET_O_xhfMnxZD8a7HyIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مالی، خبرنگار:
چند روز پیش تو یکی از بیمارستانای اهواز یه بیمار تو ICU به طرز مشکوکی فوت میکنه، خانواده بیمار از طریق پزشکی قانونی علت مرگ ناگهانی رو پیگیری میکنن که با بررسی های پزشکی قانونی معلوم میشه چند نفر از رزیدنت ها و کادر بیمارستان خودشون مریض رو کشتن، تا تخت بیمارستان رو برای ی نفر دیگه که پول بیشتری داده بود خالی کنن، الان اون کارکنان بازداشت شدن و وزیر بهداشت کمیته حقیقت یاب فرستاده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/144482" target="_blank">📅 01:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144480">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfNA8MekEBA3vMZNUaIDtLUURzZdUzRjvsvcIPsTfpHekbUfvgF1oyknzV2CR9NVst9rLgZ-G6AEvCng8E0ag7hyCOQItcZE52eEv1He0cSTZih55TKcpA-O55PNUuiR0PS3Z4gq8FWl1db88P4UzFIdvcQMowtpWoG3mVGzxKm2Nf1B0lqZWNMblsdHvMrOLDP9GLYHepuwDdUBGeZ-Xxja9AOFNFwC6mgdy-aFhmlyExeFJsNIgCsR1zzSD1LRe3U7wXStocCmL75BWe5oBWdcGkATSRYgRuE-IyBF6xSsZ0EnMcBgiihp6HewcP-a8MvvJvsa_hgFmNNKsMqX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5d94A8uivDZSBo8FY3LwIErNM0OcqsCxBwILoFL1xGT5KlCZ6NepQhQ3YPXKVNIuo4tL6Pfwmyo4jE3mrkw3Oy4vxpQp8aGuMZceLDVI6nvhhOu9BxGR0z12qU4kLdngmyPScmAaSFlYTa1ki3f3vm4GSmWBh5ey7TBhMf0gWJTFWauLwDnUaDgpYuL54uTGX0ZKU6qEvE-5_DtfpfPY7E1RG7s-r4ZJQkmGxuZtcZz0yV9C_vpDFMaoaD9fVXkpohscE65DVCxE9LDOpewzM4WFk5GURqdlanhyG-7X5zbwBMUizlMvExOFV2jBJCIHPwTLYcJdoqFsckRjKC4Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مجتبی ملکی، رئیس فدراسیون بدنسازی: مسعود ذات پرور یه اغتشاشگر بود و نباید ورزشکارها اونو تشویق یا عکسشو تو باشگاه بزارن!
🔴
جوابتون به این شخص کچل چاق چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/144480" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بانک مرکزی امارات متحده عربی، بازرسی فوری از شعب بانک مصر در این کشور را اعلام کرد، این اقدام پس از آن صورت می‌گیرد که ایالات متحده تحریم‌های مرتبط با ایران را علیه فعالیت‌های این بانک در امارات متحده عربی اعمال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/144479" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144478">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر علوم: خیلی از اساتیدِ اخراجی را که از کشور خارج شدند، نتوانستیم بازگردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/144478" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144477">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
موسسه گلدمن ساکس: روزانه 15میلیون نفت از تنگه هرمز خارج میشود و فقط نفت ایران صادر نمیشود
🔴
ایران با دست خود، خودش را محاصره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144477" target="_blank">📅 23:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddaa4078e.mp4?token=VA6CY99RDTfwNvA76COynA7Qzea-nL6whfRLSFA20C_YWsxl2JZ4xqyiIZ5APi1CHFUUCc8YZVv2_lDy4ekq3d3-LiTWpwkZIue9RsBwcJMyM5vQ6HHFyUwFGgW-A16yenz3D_Wu464zLwR1T4tb9g3MSg6Q-uTWKb_YG4qgLFZybN5xSp2zFuwopQDKTsGHcLuDafHMq2MsDBO4iw8Po9hTgK62Yu-u_dFGobu1UJBeQitgpWa-nIQk7GssHGUtJLJPLhyHOI80zv0CxNGpH_q8Keh-TGhDsSENGX8-rEElQfsETKzBL2y-KMomkyyvcQmaqROQN7CqXM0Nq9V8enqL6_tWj0VFAuLUnh_Ru-qqFsu1-TDq0XUTDA56mPGn-l7qVos0-MtHkrOEmxyofdGTIa0dYpWLrFJWcO2o02sN2Ui2SSr5fWnMtkF0ScgVpkpJ_5RT-1GCUtFWZdZzds7fyH62NJ_Yy3HUBhg8dBkzOjt8zDcqxblcHw9PUvJM8rZ09vuT4IazuH3Q84hGF3HOJOyRfpIWKdsA8ctER9e8206Hn3xdwKBbbeXGO2ALXETPSMnv68kEUHqi-JOV--e7I5LfFd7WRmmPnV4zPaOKvE5X9DAaqrX1Hk0vPxT6VR3BGuvcQGzsNkqS9iFspdULRm0Xcwr-PvEAn2NzhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدر عبدالاتی، وزیر امور خارجه مصر:
ما شاهد بحران‌هایی در تمام جهات هستیم و در شرایط بسیار دشواری قرار داریم، به ویژه در مصر.
🔴
به طور خلاصه، ما در یک منطقه بسیار ناپایدار زندگی می‌کنیم و این وضعیت غیرقابل پیش‌بینی است، به خصوص پس از جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/144476" target="_blank">📅 23:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144475">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006470b470.mp4?token=sdXTdAyp_o7VyLxrmSMhgCvA5nfJRAtKsKuCcQRf6XZsc_SMwlGQxWINgQ0hOSs88yD-SEKJ4XvQuiKlDKoKoA5dCS2r31MqN5mOHAZFPsT_sooDpzVoamXxE2SaNFW5pz5cKMIO3ty3-CqIzzRwdWO7gBQ7uG_kHNLUkIypdIDBbei3tDfkpXXyIL83s3gt0MBM92h_yXHYQ-18a1UjAxR6dzf1VXk2TK5kTGrdqWeqKR3WK-O1GaUbIiUvGtnipX50n3cSmb_hBSF93n2hUPC7LH6wOe-1E2GrdSyMoc-vT6l0pUZ6kKuN5CSkczeiNOHEv8AYG_XTZDq50_aD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی تجمعات شبانه در میدون ابن‌سینا خانی‌آباد، یه سامانه پدافندی رو گذاشتن وسط میدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144475" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
حوثی ها، مواضع عربستان در استان الضالع را با موشک و پهپاد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144474" target="_blank">📅 23:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP_PRVMN2TGNR-RUpAJP9EM2SKxC2HubGAsPVFQFB0mJIxjGwm67nDmQKBOPf5lttAKA5-1LvAYKPhQnps_DDRHfghq4-0EvSUbSsxnxWjJmEYKy5d_m2NAG0SC2ov6tVqb-7B3zmwBvzww-B9RSWjI4Mkv_VmxEBgx-WcmXlMXKCbytupB1I8JF9wt3DXOYae5b1P1Dh6MC9MqxXjsUPtGoR5md9hKk_Dvi7Ag51mRN4uRcvPGck3tnDo8w_AwzOmQVSXe1J34BkDTUxW7VPIm5OXg0egZzX4Jp2iqiwtxlXqGLypkFxN0SyR5hxbG-9FEGk6dwmjegYO_U4PBPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در یک کارگاه در بزرگراه آزادگان؛ یک کارگر جان باخت
🔴
در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/144473" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بلومبرگ: ترامپ باور دارد که قدرت غلبه خواهد کرد و با سرسختی او انتظار نمی‌رود جنگ پیش از انتخابات میان‌دوره‌ای در آبان پایان یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144472" target="_blank">📅 23:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khIZ2Yhe-0hQmOiUNRzzrDMv2NlrOYS7AmCCe5CdKOTpbipDobCDK9Lh-mm6YCiPqvuUvWrXusIVGB8EYrONNHSG5CY-XIGsayF0hKgk1cAwAHPUPbkD6Q4Dzda-YN3UBMTMkOkkK7etqeSIbFerQdNFLz1FWLfThId8b9YeB3YiXiMyNHDoJPwZ9p2B33Prqmg40pjoZwB9y7c63vUYqhDyQOkloFjwp4MUOOngXEUL2la16HaIizVfJ5wYPkHm1KSisaxzMbsBwieb9uitE1WKBn1Z8ERzBUk55dx5bBNf0bV8SKnP0kmfFRRCVhO4shVDt5SGTO5Bx9RfFU13iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتیوپی خود را با امارات متحده عربی و گروه  RSF همسو کرده است
🔴
غرب اتیوپی در حال تبدیل شدن به یک قطب لجستیکی برای امارات متحده عربی است، زیرا آدیس آبابا به طور فزاینده‌ای خود را با گروه RSF در یک قمار خطرناک بر سر پویایی‌های در حال تغییر قدرت منطقه‌ای همسو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/144471" target="_blank">📅 23:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اطلاعات نظامی اوکراین اعلام کرد که پوتین به برنامه‌ریزان نظامی روسیه دستور داده است طرح‌هایی برای حمله زمینی به سمت کی‌یف آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/144470" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=bciuA_E62YSXvp7v12fHBuEvXZH44DxSI6-s8VApuu5jQ5KiBKgMjImD9drRsf-_yyEncMfynWET8Xi3CHBns3XgPlqX8PeMVhnh7zw7y4Q0euktIcF-Z_A4KO6hYvOut2RAJaomfyitUOvoZDYXkmRYEOOcySGmSM7vv11W2IxtVbpjwckVexiCeHkRm7Nh3pySbTlB0PtpdZg6Z--4MwKSCRCaQ0ZA5gIbHo4vNpAix5eDTnbeWOr8eZA8TXqfaMmUJYT9cEkWuTSPAIVO6v1U1D-A2rxYW01MSleRccfkpUcj8P4i1ctioLbGBQQsbpfaAKYuTBTblmUxCiNx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a636fbbb.mp4?token=bciuA_E62YSXvp7v12fHBuEvXZH44DxSI6-s8VApuu5jQ5KiBKgMjImD9drRsf-_yyEncMfynWET8Xi3CHBns3XgPlqX8PeMVhnh7zw7y4Q0euktIcF-Z_A4KO6hYvOut2RAJaomfyitUOvoZDYXkmRYEOOcySGmSM7vv11W2IxtVbpjwckVexiCeHkRm7Nh3pySbTlB0PtpdZg6Z--4MwKSCRCaQ0ZA5gIbHo4vNpAix5eDTnbeWOr8eZA8TXqfaMmUJYT9cEkWuTSPAIVO6v1U1D-A2rxYW01MSleRccfkpUcj8P4i1ctioLbGBQQsbpfaAKYuTBTblmUxCiNx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده مجلس: ادعای عدم فروش نفت، یک دروغ بزرگ است/ در بدترین شرایط روزانه ۳۵۰ تا ۴۰۰ هزار بشکه نفت فروختیم!
🔴
محسن زنگنه، عضو کمیسیون اقتصادی مجلس گفت: تحقق درآمدهای نفتی نسبت به سال قبل ۲۸ واحد درصد افزایش داشته است/دلیل این حرف ها در وسط یک جنگ شناختی و ترکیبی چند لایه چيست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/144469" target="_blank">📅 22:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
غریب‌آبادی: هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند
🔴
تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.
🔴
نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای آمریکایی‌ها در مورد عبور کشتی‌ها از تنگه درست نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144468" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144467" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144466">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر امورخارجه: تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
🔴
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.
🔴
آمریکا تعهدات خود را متوقف کرده و برای بازگشت به مسیر، باید اقدامات لازم را انجام دهد؛ پس از آن مسیر مشخص خواهد بود.
🔴
ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/144466" target="_blank">📅 22:43 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
