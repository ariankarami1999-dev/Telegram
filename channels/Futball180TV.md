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
<img src="https://cdn5.telesco.pe/file/NmvmpTe7GEian4gTDnLLqm0XAduXjdy5fpN88Kb93KqZbB0x2dM0WJzw05c-KTePRvBOmnpjccjzyq8D-LvzuSl4SWz2Nt6TMiZ40IXy59bEbn71FNH__mWAd6qQrrXTC-cW8N5B7qHzKVJUFLo4W7sZzPF4xTkcJkD1ndbUX-NM6PiNk1TrYiuoKqi9Bjc8GREGfWOLuDU3BROKVTfEjwTU1-pvtHE_5cAoTzbc8hO_zsUhSOD2vlpU-FHE8BMHa4qyr_UmcZcRekkYb2w1_6vemd1yafFcm4Y4ZQoDTlQ5yicKkZMFcAxDd1dFErFuu3kVO1atbpSa8-IqFkN4Qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 411K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-106682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
قائم‌پناه، معاون پزشکیان: اگر بنزین را ۸۰ هزار تومان کنیم، می‌توانیم به هر نفر ۷ میلیون یارانه بدهیم!
❌
پ‌ن: ۳۰۰ تومن یارانه دادید، از ۳۰۰ جای ما دراومد، برای ۷ میلیون چه بلایی سر ما میاد ...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/106682" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/Futball180TV/106681" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqCc7aX29mdBWpCFswGSJNy6SuZegjbpCG23n897y9lgvwXvndmccDANszfBZMPbjRgLdx-d9M_iSY-b6coWrMEF3llVULvSkrJb8raHiIjbNrM_W-mqnnc6xSc5t2HfTGGh-vxeupUcIWt-IVb_rJGLYZ-42y5AVQQCD33rMBHFX51uRfAGhtgKd_EB-pPJKU7hh285NeDOvH5vZt7-O8IUBN942F6nubsgtYzO9PCseYv3irkMZqAx4OSUDBY2Yo32186w6O7ZvxuWaXUZmCiIxuLZAP29l35088sW9qyO5ldKKSkVcSsjkd461cw0JfO7Ix6NHm87h-ab5T0PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/Futball180TV/106680" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKaZlNDLcx9k17CYJvPi7i38_YEbIYgnrsoPIWKC62aSOnWNbAkdJOaIi69mH2AdJlZxgoMaPspH_3W1ordrFTtJNTbNX9lihOO6OrLDC3ZcjzRX1KUgSCxyk1F1ObUbCjbHtQnIfyPurrfbF0ISuHVtL0mI1ZiExi-4F8vFIJ2TKemQEFs2w_PmUsfs7m3JKya4zP53k-sk1fq8AMceXA0suV-jWZrZEHt_4QxqvVf-_DKr7WdnO7Oaxm0v-Wq33zFsOUpAYW91rrC8pSF3DmgHflGj7G0tQkHfKex_VTLDvw2OixdPnfj7EdPLOrCHdMx9aDroNC03uY9lZE1R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اعلام زمان‌برگزاری سوپرکاپ اسپانیا
نیمه‌نهایی: ۱۳ و ۱۴ بهمن(۲ و ۳ فوریه)
فینال: شنبه ۱۷ بهمن(۶ فوریه) در استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/106679" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVlBGFpNGAZ5pEs5WSruH6lCcEFrD5Oxkw1GyWHfcHcUGalqKgcP0RV_vHx3vtQN0uzpGXMCw5XSaHsZOgZEvdGe4R_B8ShL3i6RLjdNoJmRSf4HuVVAJjXPefS9KeBGx72Ikuf5uZY7lqAwUCCrMIFlUXxEWIWwzPRhn4RxtmheviKuy_VY2pLH_Uirs66cwdXdhxrUW3cfWwhRRk-zLKLcqnRvai6V29ytjtF1RoDdyhD4lW0C7qgh6M-bXnpdVhugMUPQGMq485JtkFRWW0VOJISAe9jEoFTANH6q0roYNsoGQ0cK8f_TPAein3XvANKcMbXnT6D5vmHFPkhAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه افتخارات ۵ نامزد اصلی توپ‌طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/106678" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
واکنش دیشب رونالدو به تشویق لیونل‌مسی در ورزشگاه العین امارات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/106677" target="_blank">📅 17:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روایت مجتبی‌پوربخش از اعطای مجوز فوق‌العاده عجیب کشف معدن توسط فدراسیون کشتی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/106676" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل توتی در یک‌دیدار دوستانه در ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/106675" target="_blank">📅 16:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE4e40ZMlzF-ae5C587XXWH_YT6Avmwfq1_1QiEuj6HvC_Tvd3IbzNj0JTG_UbWhc2VU1C_o9eO6pUtVfZ-bE016nAlQEp-xACxS5eSJtVJwY90vNw58GMbRfDAfZgeQ7SxHGVLeh2jFyllSQOTKCn-4MBCKsXRtr914-OAx76LZWaF6R1aZVME-ao0kpUWRdNvj-0hW0rgR9Iuf4buEVqUZg8PxzzreRSpu4m1MyznNtUKz_fTFpbTnN4IaMQBOXjhbSugZvV4_RO1QUgrLzSXgvAG5jBqHLVFq2qpdIkgFfvV_JIj2pC5RhaRbojGgl4EHniBSTZzGNNa_WuoOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106674" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
صحبت‌های عجیب و بامزه پارتنر مهران مدیری در سریال مرد سه‌هزارچهره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106673" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از استاد آریا بام رفیع دبیر زیست کنکور تو چند ساعت میلیونی ویو خورده و خیلی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106672" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هانسی فلیک: چه به عنوان مربی، چه به عنوان هوادار بارسا، در فینال چمپیونزلیک ۲۰۲۹ که در نیوکمپ برگزار خواهد شد، حضور خواهم داشت.⁣
❗️
خبرنگار: لطفا به عنوان مربی ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106671" target="_blank">📅 15:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های هانی‌رامبد درباره ضررهای مصرف سیگار روی بدنسازی و عضله‌سازی؛ حتما تماشا کنید بسیار مفید و کاربردیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106670" target="_blank">📅 14:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
🇪🇸
رودری: قهرمانی برای بارسا دست‌یافتنیه اما بارسلونا مدعی اصلی قهرمانی چمپیونزلیگ نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106669" target="_blank">📅 14:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106668">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
شوخی‌سمی رودیگر با تدارکات رئال‌مادرید در بازی دیشب مقابل الچه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106668" target="_blank">📅 14:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106667">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrVGw4mWFHqLvRJ6CGXiwil_MIQkTACs3545HiNCAaX_gp1FpJS1oW9blDHfTC0w90QZ-MHZxgHhqh01atlf1ysin3qIQoz6AspP1Rvw8geWSLtvtfAd_g3YMO1hk9YL5eeAnY0fBokSknn0XhocA8QcdpBid0rqCSYm2PR3o-xjXSM1fNG8RxvNT1RhlVEouDUSsLsrF9-Afm6aGqBHJI0PGzpj6Oxx765dYTRZpCCAYy_FgYC_JMX6oGllinYRNkC41GWO-wbkNT9d9UActGMYvMs5BOCcWjqoPnJk_a4UgP0x50yLigAwAJMKcL_fgJMn07NLasZa5Jf8TIOEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
لیدز یونایتد تنها تیمی بود که در میان تیم‌های میزبان هفته‌گذشته پریمیرلیگ، به پیروزی رسید. تیم‌هایی مانند لیورپول، تاتنهام، چلسی، منچستریونایتد و استون ویلا، و دیگر تیم‌ها، نتوانستند در خانه خود به پیروزی برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106667" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106666">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=Dxtj2faxxpKQBiec_LlxqvTnidrRCPFXJAIkzsH00zePRPzo_jdYAcWJuLECDWBPzAQ7SwsE1MaBKQ9acUVghHs9XwKQ81mwuNCBJ1mo1T8XOm-KaFhWlSet_4OpqKv_NSeIqYxebb9jJgx5FMwOOqNDCjpOUtlotWoYZPBnFVTC-my94_Sp07tLeSfbe3QMpSDp96nReIO7F7E4qDnZ0LR78JdctbjI-DqeKdwkemz-b2_N-6Riae5PTaPCqKzYVqvahCA62Pbm1PIxPmhHQ2nQV_lMAuSCYV1n3RBfqFawzSwExItxGT92k-a0XsnUmbquicvR7Xsnvf8Af0XO400I5NLMVSRGknaRULWProfT1PNZtefNQmikgc2hR8BX5iYRS-6-kZkTUQ4Bh4BeNEAu4AeNBbPESGFv0fZELjVDRonVqWW9w4MFzPDWsxlQjSwF_OYH6G_-jadi-p80QVub29GXYfLyFL7EnqwukE-lVm5DhPo2n1M6FY9eAvYuf0Qger9gOyoZ2KscxNMrGC8bDeoiksVyslAyBoCqyq9W_pWyd3Y5cYtthtpr-Vq2VZvExO-SbpeJ7r1yWicdL7sl5C9fUlu8Q4Zy62SqrPK28QjQcR7Z-ThwpbzssZTp4HXWc1I13vgqKijHR9lTm4Ze_TEOwIEn4NZd0Ev24dU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇵🇹
عملکرد ضعیف اسطوره رونالدو جلو العین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106666" target="_blank">📅 13:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106665">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=ZGQjUbREnlEKepIO2wGrbPPJLV8MS1e3XFP8noFN3o9WV1_Hu0s5rSCxDWZGcqBgmCWhCFxRbo04vAgXh92sWlAa022kv7Y9mkZmCA6WtvirshyGiFdSfdL1ZrpE60N0r7QQ0Oo5sgOnUUm7EKh-5Npp60yzb_mg6T8Z4EFd_Ue-hFxxVaYBKZLAMx_TTjs7_Q1fcVu2A6f_uYAyeQuHnuhqtrYsSuFJ8aXkiAAbkEq9xy0KW1CODLse8AA1u-BOmIXDoVB97c6B12oPV_llhLzcpad8GzEqZHZ6MYWlryMEGo3ub4U1ygMI37IHGOLCjBsA9V_W2bIhfr78lq5L0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=ZGQjUbREnlEKepIO2wGrbPPJLV8MS1e3XFP8noFN3o9WV1_Hu0s5rSCxDWZGcqBgmCWhCFxRbo04vAgXh92sWlAa022kv7Y9mkZmCA6WtvirshyGiFdSfdL1ZrpE60N0r7QQ0Oo5sgOnUUm7EKh-5Npp60yzb_mg6T8Z4EFd_Ue-hFxxVaYBKZLAMx_TTjs7_Q1fcVu2A6f_uYAyeQuHnuhqtrYsSuFJ8aXkiAAbkEq9xy0KW1CODLse8AA1u-BOmIXDoVB97c6B12oPV_llhLzcpad8GzEqZHZ6MYWlryMEGo3ub4U1ygMI37IHGOLCjBsA9V_W2bIhfr78lq5L0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از علیرضا منصوریان میپرسه چون الطلبه مشکلات مالی داره این باشگاه رو ترک میکنی؟ اونم در جواب میگه: اگه تو این روز سخت تیم رو تنها بزارم کم لطفیه و امید هوادارا به منه و نا امیدشون نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106665" target="_blank">📅 13:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106664">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=FU-_WbLJU8VhfrHs_1sUwTRoemcoP8kehm3pyrjsPJINATx1ukcbPAujHd9quFug3jJN8TKvqE-W7lC6tZeU7LK6Tdub5fOmHbHGp65G7qk52qLBIrO9uRNT4X8uxaZ0YB2atotXd-reLv3X6VKgO1u66OX4sFNVBiUILGoGvNEW-f5i4aZKLjXomrz3A2Dsido_WYear0F8PX1XmmZEqikEHZemOBM_ysQA50g_d8fGIKDEYJG7rOQQTdyHbErHOb9-0BYZzTc3dc3aLJ9DuMrGy-XV7my-SGPmW5zKwRwYRO6kg1bmRtZA8EscOuhMA4H65_wykVTfaTR6LRQrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇪
🇸🇦
هیجان‌بالای گزارشگر خانوم استادیوم هزا‌بن‌زاید العین امارات در بازی دیشب مقابل النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106664" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=WZCHgDQh2acCHspOHYCgCyrvyHeu89nOILtZH_Tarr_x9gEUc0GLMWfhSoH4SkHdniVGNsx-MJywP6pFdzwX38U-a27HXrrqTsFR36dnDHIgWMYBPv9e6Rviqfj7xjL9rReCtOpd0ImFH-p4__YUBwCySSkcppfuppo0sGMQpnKBipTBsPH1hVxwn-LXqCNAvnWfbGOgTuGP0ppShSs3UfbEQ7hMFGhygNbDhSLXlDgHTYas1bNd4DVbrLuienmf3nbo5BOB3eEqk2_XnNwuSnryHhT7A4ZQWyj2OFIIk2EV1LIRlRjNChZ5ML_E9GFHqa1zyH5ogPztBiIwwWDNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
✅
قبل از ترک باشگاه چه‌کاری مهمه که انجام بدیم؟ برای دوستان بدنساز‌تون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106663" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HC4tR2rKlUBaeu7u1TBft-l_bPjD1AkuQZBgj7wL2lCw8CQ3eCuxAzBmv3U9vYw6z79eQt9C97G2gfluv9evJ2M5ude4nbJ4mgLqcfPsaJfZ-fG23SqPBMJ1wFMH_Zma0ib88DvFnImuHdRHI0x0uLgF7GiCtZesMl74e0rTKi1xSciOHRvsoWnC53EQRmPSBjSkn3GpKZoeecWGvKxCMvrAGz7QfOYlxb7VJiG6a9Xi9Ub1mEeRY9n9L4HLZ6-LQhSFl9PwQ9J9MQPpNEsOHa4T1SUIVDXyktHs55zEjM0cgFnL_LKJHJ-5MazJpCoXCp-mKr6fpaqo--czPaC-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz0k2q6k9mx7kf59CrM9PSNPNgn6crgTdxDU3BPPbjcqycDX3OgQiWDlaeOd9UA1gb7aVSEYCE0EmeumO4FEhChjVT_iDnS4X7kZNSMCzlhCPTQdlw4H0FSBYp3BTE1MmzKEjjNDv35L5_EOd9lgBqShofLDscndIy-6TQhfCagaIDfy4iV_8DZ187mhqgBEp03_u1ZXdMNahN__yhCEivpeZvdj0Kl3_IHFHgQOkYwp-koKghWaXky2Upph1EwvZoHBx6io6VJFoR3RkJocr1mSdprssh_5inZeC3_AqdqxljPILdMmCjVoc66IDQ7tg1n64A4r9zDIH3QZLUKHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
عکس‌های جدید شکیرا در ششمین دهه زندگیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106661" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🇸🇦
🇶🇦
درگیری شدید دیشب بازی الهلال و الغرافه از این زاویه؛ بن‌ناصر بخاطر کشیدن موهای سامرویل کارت قرمز گرفت و جلو استقلال غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106660" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106659" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmnbf4s2u0dHgeeRUoD5g4rgcQHwi_Jcgzpr7U-NM7VK-g3angtBKTvW5uCeNcNyrRfquk_GOOkm1cEJGgoQfnFc4Ic62YkkjCnzwFsn6xcbW0S2ty7JFu5jIo5MUtttsfpJ5y2FLMt5lzw0zte3gQdwqL6sj9ZdSX4ZuU0xFBOJjtNdl5oM035rDZplgH_8M7qmEYK1NQHOuQ_7LIaWPa4hYKxw5GFBJS9GB3JvbhBrurQ2KfAHAsySj8uycj5LWHkfIwEf7vporVJznIAtWqdft912pno-2m9ReV99e9XJ0pnuWoiRYq3AikBmak4i94JkYbVVmcMEvya9sVdo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106658" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp3RSa0INf1IKRlWK0xPQ4KByasm3vo_w0QKte2s8CT8a-36sSEzLNpIwzVda0Q9scTcaiNPvRnSyw1mOwGptPgFj1z1bJBYDzRrAh7QgqlQ5XWMdRK7w36qpkPF5fdVYRJyVyQxlOC9-RZ1dKGAzvtjP-1Pj1qEPZl0KLICedVOXi1UVhj0fTRwJf0KKkTATHJK4ElK7QqiVR1VLB0BTb2_8e_itn_XUNh_-eH3DXM_1la-GClolpJhck07MUt1YRy8UF5oSxs04MFBreO_xsL-iYtdcko--latbee1Kz9gXSY7TbDaPRg8Vp0pLi6XoKPd2IKKVarvt7qSTI82-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری اسماعیل قلی‌زاده بازیکن استقلال: من هازارد فوتبال آسیا هستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106657" target="_blank">📅 11:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796caa8457.mp4?token=sPyer2Ewtz1v6gV4okaS_eaxBl5yBDHnwW2GCgJjUaUpewklViqF9E-2nysNjlscbzNgo5GSF2avij1aHe3bfq0xBJ7-gdSIklodynFrhBOvUbQ3MAuvX8a8x0jXAiO5PxMSEEy841C-ssnZyjBHl9Y0dzz3tKJNQUogo2A3cEvRu9LXATYXhb992bj9mKOMht5Zetc6QgQGvnVJigEQszNBMrpIk9YevGSOUc2KaYTzYS3CHsPD-hXRAPajnozQtSq3G3YWPDt3QYaIcnB0QcwjOv8FEhT2xNlL4bUGb3RHQ_veBUcZmtHAM_qSJqhvzRfM8_LCeM6YpK5qF9vtmrYGQZoLKOfVv8FxTArSzSQiyPBmJnjafT2p92kNJVvTxPUjKX8BVuguUcBv03u91U17Mrao_r9Ac1CWRjrmilScSCKsOf_1wmp1nk6WN8q7xL1nu0Lda88e1S5bzA3sfR_Qyb8V7Tpfrfp1teKjkl5S0hDI904fcR_IjAGZ4fvatmZZhn31VCQsT0TnA5ZdGAOYNYhMGn7QD9E0u59PV2KhJhDiZHFVrgm1bePty1bcD351KDybKKI26sq0e5djIQ06B-9EDVemGx9OXqyohKdg7wjssQiYhARKyPn5RuDkbpwUJ4m7wEgQCrtkrbQMbRGPBwq0tFNugF0NAJj2PSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از زیباترین پاس‌گل‌های اسطوره CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106656" target="_blank">📅 11:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=bwRUaBxiCoVS9nPodx44PmULUBeKfZRjc3voDS8yGpoAo0IkHPSpcLL24cPcpmHXc5mswQtJq7pZ4XWfDI33eOy3lj2UysKNWL5XiWXstl-m1Az83PHrC9QkKVE_TJYR0SV2moAPEPYENxpbzJfHFJoudcVPHjtcZ1hXbykD8WyYoLHwZi3XRTiVtxz1SXWdz1jCPKuUf-ZLyL02kQ2FUohPPJ1JLJCoao_76VLkSvojB3US2wQ9928V8jqkNjoz612WApqsGnY5Mk7zYP0xlAe9q1AQgqQOwnUTA9DDuG90Fz2mvh6z_ZFxBQloEb0FmgLxOH0wff2GgaxL6VSkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یهو هم دیدی سر توپ‌طلا غافلگیر شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106655" target="_blank">📅 10:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=oKAoiEqp2jsoUcQ-m6u7Ik48A6BEhfFl6cGTzyqT68XHis91i1Z35Jwfq_i73Yxr6E-GiMcLklIuZ441iFZpvl5qTno8iDYOtURIFXlpg2nGaVSW7vGcyX2YFQanTA10nH5NVpKOBsQ5LY5HsAglCJ4zj4zZa6lPM1dY40A9nspanbh9H44Lsk9Zqs4lxgJnaU-OZLaWrz65WKfCyItfafP9H6I3UDBgLvZFIa4uUTymjuBe-IqnxcLk3O4i7GdXCJrqtEA4aGQXZm9dPdoFaG5WBZ6zzAOYhkL2qx5LLYZRoqQUM2qbfj7NuHpfPegt7lU4oELcBtqgBO49ONpdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل سوم ایران به امارات توسط مزرعه(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106654" target="_blank">📅 10:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LOr-5fY7ihEPIWtPbQvgCHmm1lTWGY-HKQbHIK8LJzYfazAEFd_1z-0_wH7NN_7EgbCoVQ8LfujgPXSMTo_i-NzmKkiQzkn9VxEhWZGIqBLUAIgzh2ILvFQbPlQ1hP7srNntgBMoqTeDytoiAC78AgJFAE7Bp-UZeYJAhc9PmGVQdobZAa0nqiNvE2_IZ8BrvCYEU59tKj3TeJxffy3CmoT67ixa59Iy3R-zp3Ko7QaoHVTKDNf61T2wTSlhAwUOMwlvnV3nxudEqEwt9NHWocvjyFh74ostjP9YP5cri03aFVCof0PYQnPL1nk4JwXvi1GfuIKzw29k0wdIUtbZ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
انتقاد طرفدار همیشگی هادی چوپان از رفتار وی: درس خیابان با ساندو فرق دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106653" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_bcI_FmXx-ZQxhJftO-v54ds0Ka6DmSyhWMEQCT2HgSVt2ZqMcmRwlkJ5VK7A1Pb7dsi42jk0eBDCazeVPjC1v1EGiRfrslTrVhKfNGra2OCNhU0Kgtqun4_8pYtLeoJh0fyLy7y6p-gte8PsMNjGGf2zMy-UTskjQqF5_7eYbQ9xLOoE86OU0Bhaf-U2lOAtQsquUQOkOjW0e-73dmw-lAKq8WP9TdVSVcq8F8ZfeP1KXGKMBEkW68ZgD1_i6pP2Jgw0OkmvFYIV6tXB0s3WPp-7Izb-p-crwAZXGcVZtpz-maCEMcEdesBZb9kNMg6iRlbO7f-j9jiDZFbnWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
تفکیک گل های لامین در فصل های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106652" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=cQSkCTRmMg3qsODhz4LjxdJMoe4thSfBz66TCSz-Ds0Arr1Svy7_Sb8Ka7--4-WFTAyOG4NNCTs6y0TQ6hQfwBkuj_KXvSAN5Psy3uW6-kf4RID35qXEf8U2HdPTaHTRRy1V0MGWm6qNx9sUmCx56CQELhfLkjusBjJ0Q77cb3Nim26fXmQzLhzXd74pNDsHPJ4B8NCGiZNWK2QM006Uh2x9q1v6_wuexinpvw8faMniyPq6_huoMuMMT94RgQcmEDWUk9ewJol2jWpNjGATG7G6dKaxAjJYT0YMj9xaZerBxGTRtFvyFGx7nqM0DwPVO08ZnvkmIsYvoEKJoH7HjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc7f1ed9d.mp4?token=cQSkCTRmMg3qsODhz4LjxdJMoe4thSfBz66TCSz-Ds0Arr1Svy7_Sb8Ka7--4-WFTAyOG4NNCTs6y0TQ6hQfwBkuj_KXvSAN5Psy3uW6-kf4RID35qXEf8U2HdPTaHTRRy1V0MGWm6qNx9sUmCx56CQELhfLkjusBjJ0Q77cb3Nim26fXmQzLhzXd74pNDsHPJ4B8NCGiZNWK2QM006Uh2x9q1v6_wuexinpvw8faMniyPq6_huoMuMMT94RgQcmEDWUk9ewJol2jWpNjGATG7G6dKaxAjJYT0YMj9xaZerBxGTRtFvyFGx7nqM0DwPVO08ZnvkmIsYvoEKJoH7HjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل اول تیم‌ملی امید امارات به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106651" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=dzZzlYuXBFn8Imkvo6O1KamMVcg-G3qjqTcBHM5E3hmMS0jcOXvTXtdlHRchhO4c0O2KqrRHbHjoEBrPsoILW70aFmT8Sl0lkQA-UQHHhdiyNXDCXbkR0bJNqkYha1dF1iZ9d7F0Af7n-zrg7-I72NS6VkKQwE6iiP01Bj2GTruUUSQq0g8tDu8BcfxIowglnoaQI7anc3Vo37xHHgCrAoTHrlExf0Nww3ShNQ4Slxd9-zwi1Jsyqcjn31g6Tv36apNKoNxlpK-s9SPoOULhZ3seKjVLl6-kyyDNg9k-UgFyh_5aFsqeZ-eDDYRQo2wkd6c4WNiJk8kPnTgEpNieTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل دوم ایران به امارات توسط شهرآبادی (51)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106650" target="_blank">📅 09:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5m4Z13mcH6zjjpnCuG6B5j2INz-KyHayZx2SXhDxHPUDaFiIReI3iOytskHiDY2Vqqi0gkf3-ozgkhOSKchWJx6UXKGs3RtzQhRBjvKE9Qv_SGdkV5sYD7jbW3W_eVeQcQtjv7bwOLgXTn0vPQNiMIM4e7-hf6Jl1kEwJR6NqUlCJKYzhjR7uaC1-AqOMuiEulG8PWMeqcTI2Yn33WMSQMbLO_svPsCua2XjMFd1-EAA6EQMdAi3Ub25n3xoZQ-gsDF2L1L6mAEFS-xp40xrHTFUP7OKl8IY3qFMstHZawG-wZJP0vj44RMYjTS-hry-39udzJ9iZ7lqMO9JM1dGnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران به امارات توسط شهرآبادی(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106649" target="_blank">📅 09:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4029ff1503.mp4?token=KyRIgt-63ZJBLf0Q62-fs7hOzeRK18JXcN0iVIo4nIOUViBiQN_QBiQSDozfpYpX_5FcUuLpMtKJUQWLXOxmrRCCHQFix0ak_Epfiag1nygswCpdniQsyrOhXGerY-yU4g5WlH_q4KtmpqQ88m3gIcweSAGu5kJls--DCXDrJcIG6JWpcldA2tm3eMiiXhT0hTCYOPBmm5XDVUXpnkQf6UGVS2a6vKfEdbx7w2rVxjTxEhsnHN_aTsQIO9GIYswu3vApll2rsF70C8aS-_zfwgf77C59NO0OY2r6BJRqSE3eOsJg2G4TWM5Zg-PVfRg4L6gVlxtnHuveqL5VuDO64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
رئال مادرید با شکستِ الچه به تونل وحشتِ نیم فصل اول رسید.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106648" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ec17c4bb.mp4?token=N-VvoVw1QMPPax5M_egdI4xLSKXamEF-93PmBBAhXQq6VeUL8tURBWJxrPG1Ps26gnXd_LpF30BnTIKkbBTsMlCpal9SH-XF_U4t_Y1aukzL-FH39OIvTCF4x3N9ohgipefAH-VGGGgPsMSNU-E1qAbgBHRu2FsTaw3UBPCPcoeg9FVvngGzrOEOg6a-oB3BA5JSpsgji_U8u2h7l_rh2tGtIjKzfnnbs8K-ORw8JLZnk-lMJxcZ1aSLTtIpA0DHIUN0fuBw4sq_wmCBy9qhmxy8b6MKHizZstIPscRuCRt7dxOW2E2euHlIT7QtLteBf2QeugTz0Pa1ICORmhrvfYSgpJYr-X10V7XydOv8GZXVu0klT3t3tCrnWFAk84_Kztm9VrkFgqTK70FE_UD6cY69bqY2Cfmq2oC116W_LejmCo-2pGUoPhw1_WZdIWxQ7Xspybt89s6XzGqU3r3-MFk4A_B_olVHrs1J5WtjG9D5zghY1_Ms63Mbc9AvMF9ANNXJjtAOA3G8Kd3OwddJr02akFlBDyE1gHU07Adfj1Dazjv_iMPmMR2tXW9hJmBovy_SLTtAfEluzw4UQH6kkgaVe33yyzJ-1VnWEhaOcJybAoRjZe1L5rmaHf-OTfvhldE4o6acqunQ0v8EvEcZtHT7busoBHWMpxZDs3mtM9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی وحشتناک پویا پورعلی در گفتگو با عادل فردوسی‌پور که باعث منفجر شدن برنامه شد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106647" target="_blank">📅 08:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5PlLLgR4kkpZXKMLp7fHYAXt1_nD_dICykRYUPz8J2cEyMFTDaAj3wecI_tIVn5XRVDhMVMs4P5W4iDG-OjwyY-cyjPp6gmHKRBnVKxOu8BnTPL1o14JVmHidt5_32Kc2rFre3XQqfxoV3d0XqRzhXWdpFXOzOPKnXPkoLstASKm9tk2jMaouMAfaeFW6MJhu9nMcHUUWA-TFyvKFlCXIpWwCzqJq5xLMEReGAtQEG1jYtI1ngefSw4C7ivKq1GuLM-UAyX0eNxwH_GXZSMzGgRXXN5PMcmSZMCWsEU7ljUFIQQEnlOjvPmQIwBPsGZHpZwBj8v3y3OPoBPyYW8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
اتوبوسی که رحمتی امشب پارک کرد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106646" target="_blank">📅 08:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106645" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMNp9qeQeRh7m0CxvLIAGAT6mH68CZqPIvpxy_dFIaepbcHGrsjWNWORDy5545uKWEsK6upXGKPhgrYSDqi-vj-s4rEBfPc3ITe8-xicf4ZDAPTejKolkPqypmuQ93-mivZ54zPxIXz1McfinUB43eWcyCWocrkCEv21XrYOKqJBBFtalS0-syxwOHRPlFbe3IeYhgV6av3w3eDSu7qVZUKOqLaskNHyyRlXi-H7q1UsGVuY3aY-9TpWzBOpmMJmLbbrjjoSl8EhsFYM4b1OsdIo_aeUuCO1hRSQYUgBT2sIBV70W2m1sVcKD1ZKoqnPsnkNcmSbRuDb5PeijzyaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106644" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106643" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFw7Pqm1DpdpnLTy_ABzokMMx-cqOY_dChPcYhIeQTwnhko5DPplRpUgKCv4cIxoG7tg3-eGM10WF_aAnnW4-FdMsSTDk0DO81HSVtjxNJpS3di-9zwEkDeDuX1huIP2JYcR_mrPDWWhCH2aK2h7802GmNJBnK0e2emEFn1hh5PpBk7JkpshqJpNgLXc0YCWdfAh2pRMDsqAyhBDzbwk2U1JRCq1zuM0-HJMV-UO4y_uAxuw-EnXqMojGhy7HkwMWph-2RdWa5JwaZ3meyWG6vL0RL1LwuU5ewtrEFW1HUQ932upTDpUJnG1wHd_U709Z3vK90YtqMZGwvKjf5uSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🌟
یان دیومانده در حال حاضر بالاترین درصد دریبل‌های موفق را در هر ۹۰ دقیقه بازی در لیگ اسپانیا، در این فصل، دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106642" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpkGxzMWN7yUz_qG5oCGk1LomegfERlpNBLpsI35Uinld_jIOGTpbboI7qMvkTAVZEwI55tokC0PFNTD3aiiTLA5eekhT9EzFatqTjd-GJMFkoxopE47ZDdOpdoimgx9iFo3dGi8vumZ564zJtoZe0c1It6eVjv2C3WKVY0zUp9yslPUMYddAU9IIbgdrZ1aXVo7otKXNOtnlbCM5eKjLhcGeSy1c-nImJg7VbUb7koNrdAmF1grkMQQNKHO0u8Mb6Fos94R6FXJf7j7b7v11cLGFWF4PQKI9IqiK68iPEKHnilLHf0Z-exkO3XlGw2mBx5AxH6VRxt2K5D-Cdbhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
🇪🇸
ژوزه‌مورینیو: کسب سه امتیاز اهمیت زیادی داشت و صحبتی بیشتر از این وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106641" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9Leew-JKIVBmWn89Yr6v1fJ0G8BwBA1x7LnTAM4OU9q0jr857oKeXYH3SNmiA_lxoDh-uQiseoQvJTzV2cvTSFvDUnxd-N43xpXxkSDjQo2nYl8JjBiCvkOWZ2d7bVpCDmdaV-X_QFWrQncOTq6aNEeR8d0AU_rnkw8sv6nHcteCZggMxjl0VnrL_ZrvLoO_Bc75us67SctSl3RTh-bPK_h_Ptqy7u5LyDPf9oAp4YUM7ndY4TTjNHEFxFEfh75QvEQvfOFEXq50BedjGzD7WQnFhLRoOUNkBSbDcG75U2OQbnUxNPMfdDxTji--gxTIv6yYBsjiX-dhwfb2Q9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اسپی یکی دوتا بازی گل نزنه، شعار حیا کن رها کن تو سانتیاگو شنیده میشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106640" target="_blank">📅 01:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=MhdQsn1OHZ4104wFWTFAWiTrXAakWToDYLUF9jQCCRDe0efQt3GGyzovadELQO_6K0J4DPG2ghWZPYXysGcqT8vG1Fd2ymZ1Brq1STFzAuyVNCFqtWE45LhSgQOAK9kSJelCNTrRMKHCtvHNGbR_10s1xnaMZPwnTcdHBiP4t7M43ecRmwFwpNLUEuotiMY0GI8yNwpwsIgPGfA954BQocV0dmORdW1vdf9Dw77eq7QRELCkBVCt6lH30HlK1F0tB9nFSn9voxzbltO3X8utxIsqy-baBmDCOgTQUNeuVKk0eNz7irU5U64WNb0d1hyXnWvwWtBCqnTw1D2Gp7SjwSRZDIM7frtN74U7yjCsrc_evLGFmh_lPNyBdRpMkspXNpIpGSNbync0GhDdEx6DWTQMb8Gplf0u1AhfWS0VBqT4aRcZ2zcLt-CrtTqFG0F8Hx1npOW8ghokGyiocFlQP3Fpy180Np4UyDkGdHM0MlRPO1ciuehy0oPv1ZJDs72EW2SlLLGbmTe_byE1szqkL21-3Thd7dS1RLBrbQiEtJDA51o9aGnGk6ikgOAmOwysJDRxdQIUJWB2Z5hF_tzuLGzkIDd1SHHrbWs_35VyqdiIS7muiZvyJTzcvBmAGwgaLp95xOgGHd_yr-oiIpWjRPC_XM-8uqtq-Uns5Bk6AN4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=MhdQsn1OHZ4104wFWTFAWiTrXAakWToDYLUF9jQCCRDe0efQt3GGyzovadELQO_6K0J4DPG2ghWZPYXysGcqT8vG1Fd2ymZ1Brq1STFzAuyVNCFqtWE45LhSgQOAK9kSJelCNTrRMKHCtvHNGbR_10s1xnaMZPwnTcdHBiP4t7M43ecRmwFwpNLUEuotiMY0GI8yNwpwsIgPGfA954BQocV0dmORdW1vdf9Dw77eq7QRELCkBVCt6lH30HlK1F0tB9nFSn9voxzbltO3X8utxIsqy-baBmDCOgTQUNeuVKk0eNz7irU5U64WNb0d1hyXnWvwWtBCqnTw1D2Gp7SjwSRZDIM7frtN74U7yjCsrc_evLGFmh_lPNyBdRpMkspXNpIpGSNbync0GhDdEx6DWTQMb8Gplf0u1AhfWS0VBqT4aRcZ2zcLt-CrtTqFG0F8Hx1npOW8ghokGyiocFlQP3Fpy180Np4UyDkGdHM0MlRPO1ciuehy0oPv1ZJDs72EW2SlLLGbmTe_byE1szqkL21-3Thd7dS1RLBrbQiEtJDA51o9aGnGk6ikgOAmOwysJDRxdQIUJWB2Z5hF_tzuLGzkIDd1SHHrbWs_35VyqdiIS7muiZvyJTzcvBmAGwgaLp95xOgGHd_yr-oiIpWjRPC_XM-8uqtq-Uns5Bk6AN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
کارلووووووووس اسپیییییییییییییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106639" target="_blank">📅 00:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وینیسیوس بیاد برا اسپی چند دست میل کنه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106638" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عجب بازیکنیههههههه
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106637" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کوووووون رئال‌ نجات دادددد
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106636" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسپیییییییییییی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106635" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگگلغاگاگا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106634" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=MzGI5dsOcyZTB3Srqq_olmOGBZFVAKu5ydZ1MFhdo0z5aOsuTMFYqupolyzdOYLOUdjeeE1kg7WW-6PA0vpgPqJbcWIZ0jiA_YDiT34HrgsGLazCZtTgM9tKJVw_-1IV3-PA4ao9Bcw-GTL6dY_TA_eIfDBMxdHf9tOwNdCxviwt2oVRgaefsTjiv53qQw4i4kDBDlA0dTDOZrfitOlRUQutQ3kiB3RWzdTB0b-GTOdLTGNQijl2QJFb7lxqPVPkTtmkLZeTCP8FG8nrkbJcORepSipWgSmxA6Nw7Vj7jQ3kI7DRzFzJhsUcdt1ffU4bZVzXF2h-rFfGSx5gSJ6-5DR5XoPIwXQz9U0i4ihjHejUj5wYLCMeYMyzvsCnBSYWg0uLYQ0mMzPwc1JBftDlK7gty64Vuh0J_r6PHaDlpR-UsYmL4--nltnaer9ja_6cyRo_k4YtTaU6irNBQGDRfVuYnUqT8FxQ3QPQCOo5xiGeUdZLQgmar68kruiAxKNX2835HsmvI7Uzto2LqPtbQAF1DOOVegt6BqGVYxwMZcCzA-VW_x9BFaNINr-r7IAbBgrk-DVtkU0XqI0Rbf87EcTNtNCDOFYZGc1Hgku-mR4nyHQDCJSEKrxXnfbjRJncfVgNL23UyysHz3duGHwhXWBPt5y11p4wqjt9gtgqVRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=MzGI5dsOcyZTB3Srqq_olmOGBZFVAKu5ydZ1MFhdo0z5aOsuTMFYqupolyzdOYLOUdjeeE1kg7WW-6PA0vpgPqJbcWIZ0jiA_YDiT34HrgsGLazCZtTgM9tKJVw_-1IV3-PA4ao9Bcw-GTL6dY_TA_eIfDBMxdHf9tOwNdCxviwt2oVRgaefsTjiv53qQw4i4kDBDlA0dTDOZrfitOlRUQutQ3kiB3RWzdTB0b-GTOdLTGNQijl2QJFb7lxqPVPkTtmkLZeTCP8FG8nrkbJcORepSipWgSmxA6Nw7Vj7jQ3kI7DRzFzJhsUcdt1ffU4bZVzXF2h-rFfGSx5gSJ6-5DR5XoPIwXQz9U0i4ihjHejUj5wYLCMeYMyzvsCnBSYWg0uLYQ0mMzPwc1JBftDlK7gty64Vuh0J_r6PHaDlpR-UsYmL4--nltnaer9ja_6cyRo_k4YtTaU6irNBQGDRfVuYnUqT8FxQ3QPQCOo5xiGeUdZLQgmar68kruiAxKNX2835HsmvI7Uzto2LqPtbQAF1DOOVegt6BqGVYxwMZcCzA-VW_x9BFaNINr-r7IAbBgrk-DVtkU0XqI0Rbf87EcTNtNCDOFYZGc1Hgku-mR4nyHQDCJSEKrxXnfbjRJncfVgNL23UyysHz3duGHwhXWBPt5y11p4wqjt9gtgqVRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی الچه قعرجدولی به رئال‌مادرید
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106633" target="_blank">📅 00:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اندریک بدبخت بالاخره اومد زمین</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106632" target="_blank">📅 00:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسپی رو آوردن زمین گل بزنه
😂
😳</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106631" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دفاع رئال جلو حمله بارسلونا رسما خاله میشه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106630" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مورینیو ریدههههههههههه
😳
😳
😳
😐</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106629" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الچه قعر جدولی مساویو زددددددد
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106628" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گللگگلگلگلگلگلگلگلگاگلگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106627" target="_blank">📅 00:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=tE2qk7kS0jWzmgEDEdNvzU6g3iqGUrqjYlCN8-SiV21v9O8TPA1ExhXvH-neOcPDAGXbi2a_Bqu5mLl00DAjPBdYBNAHTruz4jh3eA4y1dvu9k3OAHOXD5EUrKHcx29P7KqivJXYTo6NtBZopPbYQ54c2ut2d6UYlsJx-itQIpgmFbsX30UaDx5q7sBxQogyesJDBf-i7v0_Z1ujWdDB7txO-nXFwm-RMUo7UNTOLL7FcqnThkhVYJNsarN55kK5w96jXy7nzC-JX89BJ6gvDTetZyQf_6RxAzy_xI8D004-O3KY5K4RefCY27dWtX_4iyIg8J1bjeaGzYt6KK7BwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=tE2qk7kS0jWzmgEDEdNvzU6g3iqGUrqjYlCN8-SiV21v9O8TPA1ExhXvH-neOcPDAGXbi2a_Bqu5mLl00DAjPBdYBNAHTruz4jh3eA4y1dvu9k3OAHOXD5EUrKHcx29P7KqivJXYTo6NtBZopPbYQ54c2ut2d6UYlsJx-itQIpgmFbsX30UaDx5q7sBxQogyesJDBf-i7v0_Z1ujWdDB7txO-nXFwm-RMUo7UNTOLL7FcqnThkhVYJNsarN55kK5w96jXy7nzC-JX89BJ6gvDTetZyQf_6RxAzy_xI8D004-O3KY5K4RefCY27dWtX_4iyIg8J1bjeaGzYt6KK7BwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گل‌اول الچه به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106626" target="_blank">📅 00:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الچه زدددددددد یکی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106625" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106624" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=BvJkGt8SUlZHmbzvVeMz_rUhaDC50A2iUFJrHLldsYvby1ioHQo3WacujEX5vIZz2FbRwhHoCj1hFlZM-jjY6pnpKZmFUPDIJsFDfVyyPYQ12k48OAwdpCrtV3NmRDk_0r7pLIy-7wn2qx0ELH9S2TNrvuPEzxYPfNcHQtMzVITUwzrk-3NaN4PRoW9ou4lrIDY9fmUs8sgMzak5FaGCltjVH3SJab2t0o2dfSYm6c3NZtvv0ENs8W67bElOybApPr1wWgQbO84VppE9EaAqUnf5YBoN4OSJr1nj9Ov7QOFR34dY-Vwd1xaCIPybjWh9I28a_D0LjcbOsdfwDgw8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=BvJkGt8SUlZHmbzvVeMz_rUhaDC50A2iUFJrHLldsYvby1ioHQo3WacujEX5vIZz2FbRwhHoCj1hFlZM-jjY6pnpKZmFUPDIJsFDfVyyPYQ12k48OAwdpCrtV3NmRDk_0r7pLIy-7wn2qx0ELH9S2TNrvuPEzxYPfNcHQtMzVITUwzrk-3NaN4PRoW9ou4lrIDY9fmUs8sgMzak5FaGCltjVH3SJab2t0o2dfSYm6c3NZtvv0ENs8W67bElOybApPr1wWgQbO84VppE9EaAqUnf5YBoN4OSJr1nj9Ov7QOFR34dY-Vwd1xaCIPybjWh9I28a_D0LjcbOsdfwDgw8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوپر موشک تاماهاوک سوبوسلای جلو تاتنهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106623" target="_blank">📅 00:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سوبوسلای چه سوپرگلی زدددددددددد
🔥</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106622" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106621">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106621" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106620">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxoEKUPE5x95g8IVNFE138udb2i3Or5dLNfmd0VkzTOGZQPDdkHsM37oX8khJnXf-dmyJJkAoIJbdw6P5qc580UOYc43KtfhM0TL9zlcJcozv1bTOeLXbF7I2vb2Hk9VaU7JRnCdPfNv-Iugp-ErP_ySKe1eLgiYhY1KZG9FvXE1gcK7YhVWniQUFPEWRt6m4kHHfT5xBf7f2Wr7AT5eDQAKsuJ3MEtOzmr-BGMn8tbrpj5U0y6cJ7-KpXM1DxrL-Z03LUx7HsgdLL-SQYuEgF20BRPZfCQTm6fx1sYLfX_H67dhZ8kUtr5oZwkpGOk2F-LgpAdT47NDS-gUMTxEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست تیم‌ملی آرژانتین برای فیفادی با حضور لیونل‌مسی؛ بازی مقابل بنین مراسم ویژه فدراسیون فوتبال این کشور برای خداحافظی اسطوره تاریخ فوتبال برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106620" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106619">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6KdVm4rEa13hAdZ9mL6kEz5qZnZx3aQ2QwuZhB8Ox4LvivH8H27TUXLkiZkYH4uPYv_ZLZrjHxG9P2MnYIVKJx8h797JMeQVdCP74L620ye2jsgJryTzQ8jdWNagF5hlLMeu1qMNl6xKC5PJNR98_bE89PmI95wN9Kl_4BKEtR4OkSHg8Qg44PiIQ77gR_C5OxgO4oTc1Wx59NLIdXGy9is0hdtw5E1ZOLa3EEntMbnGoHMi9gLADIpZtQks5_t8-rj9U--Z3Fs9J5RtCCz6GFsYfBl36nd194V-UwM6IAjD7bAsTfKbap54cryumPtcuSe91ADepOM4ajUbrhA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
جدول لیگ‌نخبگان آسیا در منطقه غرب پس از پایان هفته‌اول و حضور استقلال در رده دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106619" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=Xr0d4iBcUXVtqYy7sYYtf3tAxVoWloVluPcDOQL3u58WlfJx1h6unVQpL8WouVqUFXGtpEFBPBATsWUl6cyLROM8N7Zq5KvaknO75L4CpRsONgBNhRKzm-Qxbhe7QKgRrct0lr4gQ47ayLJeCEh7T5qvKwh0r5Lv-n90nvgaDAQc1tV-WlYaXgY3UK8US79nn6IwZpTOsx9kdsDerdwqIEDpO0H6hup6Qmmt3kc4cQ8l6ez6UaGTySCAQ0ORARoleq2zbQJX2BxiKWCl6TZHhwo00Dy095JlUci4Jg40T4Jltjzl3ix7sWS0fcYkQdTywfhgNvHvqBMXjiVVRExkMWPH89r11DPFPT4TQV573ej0Z9s8UhYdOnbzQubeQr3xm_658DJZtkeRTeasfnASzOWL-DG-mq0TEWcVGZLLlrV7DDiuwKMDh33xx_Quecr02SYFSVwxyFt_a9kBs-Wgawfa50vglEJi_p_FLQpxb0NLkafVnfPJDA2Pk8Mf8F-3R8gYpk5q6efQhwailJDQtcsA7mRHtlABr6MhJtExN0yVZctN9-96PWz7oB0A2kkpcOKda4h3CTo-s5Hab0SWawxYsnrehLTSJMq9IhFbsDzX3jKhdiq3VP2fLqsysBgjljD-sZsldv2Ewgrrv3beea0BF1O-VUxF13xSu2Hyy_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=Xr0d4iBcUXVtqYy7sYYtf3tAxVoWloVluPcDOQL3u58WlfJx1h6unVQpL8WouVqUFXGtpEFBPBATsWUl6cyLROM8N7Zq5KvaknO75L4CpRsONgBNhRKzm-Qxbhe7QKgRrct0lr4gQ47ayLJeCEh7T5qvKwh0r5Lv-n90nvgaDAQc1tV-WlYaXgY3UK8US79nn6IwZpTOsx9kdsDerdwqIEDpO0H6hup6Qmmt3kc4cQ8l6ez6UaGTySCAQ0ORARoleq2zbQJX2BxiKWCl6TZHhwo00Dy095JlUci4Jg40T4Jltjzl3ix7sWS0fcYkQdTywfhgNvHvqBMXjiVVRExkMWPH89r11DPFPT4TQV573ej0Z9s8UhYdOnbzQubeQr3xm_658DJZtkeRTeasfnASzOWL-DG-mq0TEWcVGZLLlrV7DDiuwKMDh33xx_Quecr02SYFSVwxyFt_a9kBs-Wgawfa50vglEJi_p_FLQpxb0NLkafVnfPJDA2Pk8Mf8F-3R8gYpk5q6efQhwailJDQtcsA7mRHtlABr6MhJtExN0yVZctN9-96PWz7oB0A2kkpcOKda4h3CTo-s5Hab0SWawxYsnrehLTSJMq9IhFbsDzX3jKhdiq3VP2fLqsysBgjljD-sZsldv2Ewgrrv3beea0BF1O-VUxF13xSu2Hyy_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106618" target="_blank">📅 23:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دیومانده بالاخره پاس گل داد
😂
🔥</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106617" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امباپه زدددددددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106616" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگگلگلگلگلگللگلگلگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106615" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96af48f644.mp4?token=IwXMb1wPhok4u7rlnAUC6GPsyDugkerGEYWkzNjtvNmsKexi2W-aF79dRz2_8qzYjdx51e4AyXXM1GcM7iH4ye7aK-J61kKK7KYMawkFY_MAiAfuDPGE7cwR-x5IvRAqHAW-XblP0_TP_xNKmlZl1IbsfSSHq_1KH32vkbEttL1NRsjYEkR0Ffp5yFIQZYobpsOot8rG8Wso4Py9y0s2JsRBYIQCPNXK3CmAHOICC_esWCju1xSt_qd0Sya3FcYGfwjkREBl1mdV3yxcIvGF4xPi3lpd4-U_9JOKECnzGJMBo36dd_3q5JUE_g_tH5oRfkZaUW63bJ73WM4OtlXcYxxv0nYEghqpfVnVknwdL-g900HMaB48mwhsY4NbmMsqxGGJjUDXIDqCGisjcxgycc4APj3ncvoFQ-85pUfT0l8xwwBAlNV0fr0r7uUS3oOLVrFSE3DKbYgJoa1RVE4pBpuPorY5rT6K3pd2jNTgDjWj-G0yulWQ9RJL0LjVV16BjwUcPkWY1NzW_AtaTcXCwmyrGgsNsnsepiVj9YFbshTHGkU8eJ7q8bW4E1eV_6FS84Qq7GSk2DrLS3B2OpqVbpChcU22wIyOfupJNt2QIWILhDdw5Qwo-x5EuJO1pRISER-G7IvvA_L9I082QHOnTERrZc5HBfJIvAJhj6V7yG4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96af48f644.mp4?token=IwXMb1wPhok4u7rlnAUC6GPsyDugkerGEYWkzNjtvNmsKexi2W-aF79dRz2_8qzYjdx51e4AyXXM1GcM7iH4ye7aK-J61kKK7KYMawkFY_MAiAfuDPGE7cwR-x5IvRAqHAW-XblP0_TP_xNKmlZl1IbsfSSHq_1KH32vkbEttL1NRsjYEkR0Ffp5yFIQZYobpsOot8rG8Wso4Py9y0s2JsRBYIQCPNXK3CmAHOICC_esWCju1xSt_qd0Sya3FcYGfwjkREBl1mdV3yxcIvGF4xPi3lpd4-U_9JOKECnzGJMBo36dd_3q5JUE_g_tH5oRfkZaUW63bJ73WM4OtlXcYxxv0nYEghqpfVnVknwdL-g900HMaB48mwhsY4NbmMsqxGGJjUDXIDqCGisjcxgycc4APj3ncvoFQ-85pUfT0l8xwwBAlNV0fr0r7uUS3oOLVrFSE3DKbYgJoa1RVE4pBpuPorY5rT6K3pd2jNTgDjWj-G0yulWQ9RJL0LjVV16BjwUcPkWY1NzW_AtaTcXCwmyrGgsNsnsepiVj9YFbshTHGkU8eJ7q8bW4E1eV_6FS84Qq7GSk2DrLS3B2OpqVbpChcU22wIyOfupJNt2QIWILhDdw5Qwo-x5EuJO1pRISER-G7IvvA_L9I082QHOnTERrZc5HBfJIvAJhj6V7yG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید به الچه با گل‌بخودی گلر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106614" target="_blank">📅 23:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imxl_ln1zncNyqOxtQ8zyTfyfOanv7FwKUSUgcMQhWRdDECDkcOQdgdxuxr9KxMAJblC0n37zEPDifh2ueeQHrT3GhhQozDze3STpUqgqtteddTrk0gPtrcIw4HfFgztawj017l9HeEbQY4vE-W2x9QP9Y1EFRgws2KVUwC6vifjwCZqnczHqpgmhuhzCaE4QrpMdOYb3dd1c4Y_cyKe4FYjcxI9kcP_gHVRJwsQvIjVQam_hF-6u6OChPZu1Zf06sh7wxjpq9iO90VVEg9oNo8zQxYejWNPJnoA7nnEO84b77SqmPQnB2CWgTlrLwReE5VD24Ze2US7rqvast4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووف
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106613" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عجب سوپرگلی زدددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106612" target="_blank">📅 23:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آردا گولررررررر زددددددد برای رئال
🔥
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106611" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگغگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106610" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=OERHvGdvVl5tUM-YQExRjF8tgKjTnEZ9zJtzOBHNit3KlxgWkAdfNZzNOm1b9rWEUOvqesXnnqx4Fwj1HuBvzgORvnlYzbcdsnfqvWF_1TW7Qd87sWxeVaivyXYtfgd9VdbZ0dxUItJBI17ewCt7MyYGTY31wZZGNjLf4MeB-OPsHKT2jyybJwP4b6MkPZlCG_GAGUWN8DcCImbJJNKx9WcuokzJ1eX2EhqEzXEGT0YFRfzUWtB_J7lIWfIZlAKJ-QVfwYpSjJd6wcSLlGVZ2LJHwDmjAcGHWMYUBMnCzszNH3v1shCSs_JvDEflGim9_01wrD4rfN-5-BbNf07snX49pcIe-D5tq69bJpGS7cF9sruIlBiXfl0vo9qEKKR-ljwkfwr-ezrUfIVwPWJEjrbNAeeCIpfpEqmfyicKcQP71MqF5OQTxnWD2dEvTCmccsIOiNO72zXDZNG182ftBcDGoYRxBfNDch2M4jRiWQj7zUGEWCYhrnKDNQCHiovEReqOSe-NBxramx8CATLV0wqjl2guPUi7UuLNpR2U21RlBQXdd2qlneZqhWuz5I-UuosbGyJxvuVBzVs3KBr0XO3RPWwfu2log1iBmqAVu5Q172KWIyYX3UHAmFtlyJlgXKfHuqHsfIoFjKlc4Ep4vgpXmzSUwoKabMOZOvEeiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=OERHvGdvVl5tUM-YQExRjF8tgKjTnEZ9zJtzOBHNit3KlxgWkAdfNZzNOm1b9rWEUOvqesXnnqx4Fwj1HuBvzgORvnlYzbcdsnfqvWF_1TW7Qd87sWxeVaivyXYtfgd9VdbZ0dxUItJBI17ewCt7MyYGTY31wZZGNjLf4MeB-OPsHKT2jyybJwP4b6MkPZlCG_GAGUWN8DcCImbJJNKx9WcuokzJ1eX2EhqEzXEGT0YFRfzUWtB_J7lIWfIZlAKJ-QVfwYpSjJd6wcSLlGVZ2LJHwDmjAcGHWMYUBMnCzszNH3v1shCSs_JvDEflGim9_01wrD4rfN-5-BbNf07snX49pcIe-D5tq69bJpGS7cF9sruIlBiXfl0vo9qEKKR-ljwkfwr-ezrUfIVwPWJEjrbNAeeCIpfpEqmfyicKcQP71MqF5OQTxnWD2dEvTCmccsIOiNO72zXDZNG182ftBcDGoYRxBfNDch2M4jRiWQj7zUGEWCYhrnKDNQCHiovEReqOSe-NBxramx8CATLV0wqjl2guPUi7UuLNpR2U21RlBQXdd2qlneZqhWuz5I-UuosbGyJxvuVBzVs3KBr0XO3RPWwfu2log1iBmqAVu5Q172KWIyYX3UHAmFtlyJlgXKfHuqHsfIoFjKlc4Ep4vgpXmzSUwoKabMOZOvEeiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صحبت‌های عادل فردوسی‌پور درباره اسامی عجیبی که بازیکنان استقلال در پشت پیراهنشان در بازی دیشب نوشته بودند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106609" target="_blank">📅 23:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=ufSAPYcXkFxKlsg8P11QaBcwgUe7SWcES1LQu5YD4y4ES_C8JWGDTT04uoSR2uVhoeMbVaQ9LvotxhK5VyiCQRvhowM0UsBn_onegojdTcDfLvPKCmXXGH9ygFFi5v4iILuhG6d4MccDEYevpH_M-6T2sDivkpj1ibErZDsbAL1fYt9pCyEGKKALHpwIYTPnbKa_kVD4kH4_ePg6fN9pbH1Qu_w6kY5uxuZREgnYNjfJpDdpkbdVtRNa4JNmEToVlfUOu4yAynLVYMos4px-PFt7Dq4m8qWPDkriAUL-hJicJ7O-EAGoeJEBwDtucTFVqoNJcnNMbJd_N_XryE9ehYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=ufSAPYcXkFxKlsg8P11QaBcwgUe7SWcES1LQu5YD4y4ES_C8JWGDTT04uoSR2uVhoeMbVaQ9LvotxhK5VyiCQRvhowM0UsBn_onegojdTcDfLvPKCmXXGH9ygFFi5v4iILuhG6d4MccDEYevpH_M-6T2sDivkpj1ibErZDsbAL1fYt9pCyEGKKALHpwIYTPnbKa_kVD4kH4_ePg6fN9pbH1Qu_w6kY5uxuZREgnYNjfJpDdpkbdVtRNa4JNmEToVlfUOu4yAynLVYMos4px-PFt7Dq4m8qWPDkriAUL-hJicJ7O-EAGoeJEBwDtucTFVqoNJcnNMbJd_N_XryE9ehYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌دوم الهلال عربستان توسط ساویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106608" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106607" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106606" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75776b642.mp4?token=fz5I7xGmgAzfjpbtygsSfLpTaMKf1We3DnWj561hmO7o4ZPGiKK5Wh57i_w4xLmvVFCbKK1Ofn1Sl6V28gYPO360D9t9MuyDjtift8XrrLcabLyyhdFU04mbKh1fRpxx4KM_hJeezW-w8CVdAV00NmML6OOsQjETU0jN3HnkqIGIw6Epq15atfrDPKJiy7Vz95ZEeAF2GoUb1wGE3gWGPauGXmGBUW9PBYYCipMo9-LD7Bff2evVlZ-qJJdILKXD57HjOULSVtnPI85-etck92CVrPjB3_Si65-hOP6IzGhplTUdGgMwdEhLv-O4dOkZl2KUdQ9VgMZcGNxfmYhXig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75776b642.mp4?token=fz5I7xGmgAzfjpbtygsSfLpTaMKf1We3DnWj561hmO7o4ZPGiKK5Wh57i_w4xLmvVFCbKK1Ofn1Sl6V28gYPO360D9t9MuyDjtift8XrrLcabLyyhdFU04mbKh1fRpxx4KM_hJeezW-w8CVdAV00NmML6OOsQjETU0jN3HnkqIGIw6Epq15atfrDPKJiy7Vz95ZEeAF2GoUb1wGE3gWGPauGXmGBUW9PBYYCipMo9-LD7Bff2evVlZ-qJJdILKXD57HjOULSVtnPI85-etck92CVrPjB3_Si65-hOP6IzGhplTUdGgMwdEhLv-O4dOkZl2KUdQ9VgMZcGNxfmYhXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌اول الهلال به الغرافه توسط روبن نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106605" target="_blank">📅 22:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🟥
🇶🇦
اسماعیل‌بن‌ناصر هافبک الغرافه بدلیل دریافت کارت قرمز دیدار با استقلال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106604" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxf0MXvt3h4CYfokRO0mFRmQFRRuFYPo8zhMfsiDBGvcHfOGfMNBflaW2NVUYgiS0lSfmHX_jXf6Ifye3w8cayj_wqtGQoOEluA_n5qk8zd5XOPEQvZNPOMugW9MxlXd8ds1ilfzCDJqCB0UYvrUeH7xkweqr6scEV9Zvx2g2I4m1Dpp8a0pTqmFZLIo4ggWMeH8bB_kfcSmyhx6LWLG9tBRrHtAsNoQWYcsz5_VuLRoUhA6WYX7zuaMGH2SC5FFLHD_4UNPJ4IT8oAez_BSRTOSoWciHFvueL9PUQhLRoIez3HditUdqWebWKkB6G3Q5G9hA3-OZm9nawlQe745tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
ترکیب رئال‌مادرید مقابل الچه؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106603" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
🇸🇦
عصبانیت
رونالدو از مدافعان النصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106602" target="_blank">📅 21:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=ZEyKIXRCtfILTbG5HC1gjilyhpj_Tb9yW3dQLQnFiOgUXRq8PvnnKTd_Yt9PIPIEVRwRlvYN9l6uNPfnfIgUtLwarIj9wNPirAyGBXz6h94QIwzM0Qs_715HpGWUz-Z-0D7cZ1E2uRdpRucAznn5d-ixIsWDCitVPAOh2vimKtE3HGKhuB2di9Ar97CupZGE5P_xMfyWXmFgDlNHppY_N6T73ZuLRqfxb5arjjmH7YhyhuyZYvvvMDp_XfRTtIYcx2UYqAC7bfAJwDOEuefD3FLRP4QXBWJP1dK6TS66preWwalP73yVutv6p45jmxOxfEN_AhfEKy6Vx9cj3Ce2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=ZEyKIXRCtfILTbG5HC1gjilyhpj_Tb9yW3dQLQnFiOgUXRq8PvnnKTd_Yt9PIPIEVRwRlvYN9l6uNPfnfIgUtLwarIj9wNPirAyGBXz6h94QIwzM0Qs_715HpGWUz-Z-0D7cZ1E2uRdpRucAznn5d-ixIsWDCitVPAOh2vimKtE3HGKhuB2di9Ar97CupZGE5P_xMfyWXmFgDlNHppY_N6T73ZuLRqfxb5arjjmH7YhyhuyZYvvvMDp_XfRTtIYcx2UYqAC7bfAJwDOEuefD3FLRP4QXBWJP1dK6TS66preWwalP73yVutv6p45jmxOxfEN_AhfEKy6Vx9cj3Ce2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇪
گل‌چهارم العین به النصر عربستان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106601" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoDTsiWqijRupa9A26WQVltljP4rFW-H6xDpxiYXIdzlDcDKkOwOwaWyd4QBrqsj_ONWkfUcqhLabpNaBMM3oRxYWf5_6U8PiI1amy8m1GybXJuJoOgxk0AKBmPvtb1ZETdVWtTVp3OghhRSk6g0GuGz6EPpksUmm1htytkSLSU6WBxLRtfVp_T1YEO-MjQUiD8maUqgoGBlaTUT7S6vfF9QY7n4x3c5fE6RAV2hpyJpT2j1hvcoAA7zsKPuCEulFOzcm4nR1XuB5NbVfj70MLoEvKVHMV5gKwkvRF9YrbNdRYYfhMVNTdVEjT6279zE722tYdA75Ly5XalulBCUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106600" target="_blank">📅 21:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=OuUPfXUwcmqhyqHWFSZj-fiGfKQ8vjtuKzkXBGFG_md-uaUu4MSPgAvWYEuznNNiYqs-cmMPpw3UzzoAvCYfu3w6T7EFODJ8J0LzEF-ixPfC5CdR84NGmrrViD2AXyKPIt9_zBWCbjaZRd5FufnYAjN_FIQLHBex-aIGziXnPiwj1Qh-c_bCoMYc4Jp9VP_P68ZCskl6DrWY7YEF9qUeZgR-jvurUvJRtNk-NstsS5jdxndAUuz0C_9inCgMFnLloZ1gkc_gTl20VUviZhRSkWiiCix9M_jIDVJMbKDObKvnUsdsF5nGcK1ofOfmf5i21LmSlOXU-CjX6Viv26JhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=OuUPfXUwcmqhyqHWFSZj-fiGfKQ8vjtuKzkXBGFG_md-uaUu4MSPgAvWYEuznNNiYqs-cmMPpw3UzzoAvCYfu3w6T7EFODJ8J0LzEF-ixPfC5CdR84NGmrrViD2AXyKPIt9_zBWCbjaZRd5FufnYAjN_FIQLHBex-aIGziXnPiwj1Qh-c_bCoMYc4Jp9VP_P68ZCskl6DrWY7YEF9qUeZgR-jvurUvJRtNk-NstsS5jdxndAUuz0C_9inCgMFnLloZ1gkc_gTl20VUviZhRSkWiiCix9M_jIDVJMbKDObKvnUsdsF5nGcK1ofOfmf5i21LmSlOXU-CjX6Viv26JhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106599" target="_blank">📅 21:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگگلگلگلگل سوم العین به النصر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106598" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=MAkKeCduv_4mGxEZh6vVIsKbcTe3u45ZazB3pdqBTLVtzo8lJdKbh7LjxcnSIgeZUjGVS-NPXD-9wFNaTEPXdFeYJ3lFtqbPy5gDi1NasNU4DcKJKZVqIhRvU_BraWZDrtTMLanSpdobBkJToUEGCIhVex2nSdxStbJB70DV-aQm1KzayxqU0BZKI8lbovHM8bNlCJcZaj3eB2TnuA1vuyawXkqmD2CyFauhME8LOuT6vQI7mmGsdnrdnOqMy6YzvgJeyUcWRZ-DN-vSpBpjVjNo7JTkZ_VcygSCV4DuEXB-d7LmfPE3YP88xBFtFMGPk8KmjVmeoZrOncgi7vUmYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=MAkKeCduv_4mGxEZh6vVIsKbcTe3u45ZazB3pdqBTLVtzo8lJdKbh7LjxcnSIgeZUjGVS-NPXD-9wFNaTEPXdFeYJ3lFtqbPy5gDi1NasNU4DcKJKZVqIhRvU_BraWZDrtTMLanSpdobBkJToUEGCIhVex2nSdxStbJB70DV-aQm1KzayxqU0BZKI8lbovHM8bNlCJcZaj3eB2TnuA1vuyawXkqmD2CyFauhME8LOuT6vQI7mmGsdnrdnOqMy6YzvgJeyUcWRZ-DN-vSpBpjVjNo7JTkZ_VcygSCV4DuEXB-d7LmfPE3YP88xBFtFMGPk8KmjVmeoZrOncgi7vUmYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم العین به النصر توسط حسین‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106597" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">العین دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106596" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگلگلگللگگلگلگلگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106595" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=hIwUJy1iTqQdz0fGfnDN1b_NvTARoCt3CGza-_a6tWUF1xRUVbi9bjQ-ECxheq0fR2CKzct47dAfHje-2OwgRJBiCMoeVfHrJWDAbyOECyK8kOGV_lWRemDmNJJrtkISJNgiVN6WK2DFGMwAyW4dlPlUIVRtnjJqFSjxXt2vF_f7-PzloDvO_qSOmbdbWk_eNfxRvR5WtxBzq-DrdaNJf1T-nzrgf5-yhnrkbvNuWB2R2bpUxTzmuYcp_KvVQBH6qlrzK2JpKLF2OMvL5nEiuTwBqPDOCyRsUrnYaw3UV1XBIZw_fMMzDrbie8HppdbQO4gRwefge3O6d8lgFkQlIJYH5mWIwmT2kJl0HHCySx4EYvkNElmiDILm_L0g9mF2ehDJ9hurVkptXAFPQ5hf5I2GTeHrYZDN6lHrPtX2rsUvyE4Jdx0IaTuBDEFq8iEkpa0AVPmtYexQNzN8XcjouO_uch3hytdd7H-v76C2X6ye32Kc0Zj05oXfknJBYg_PJ8iHrfoduwFzXKYLdR6PDxe34DYPeUOD_GvK2NreOffSslJAEz1F7syRzVCXl6jrU4LjrGVWYMMZAWA1-KkQCaHY7HLCBKZtv8KX8TnYr5t4dYlWJQc5Id3Pk1xk-xQ0hs6q0jXahBEg9IAh4Q0Bpj7glA2_4BfkbfQtYtKoYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=hIwUJy1iTqQdz0fGfnDN1b_NvTARoCt3CGza-_a6tWUF1xRUVbi9bjQ-ECxheq0fR2CKzct47dAfHje-2OwgRJBiCMoeVfHrJWDAbyOECyK8kOGV_lWRemDmNJJrtkISJNgiVN6WK2DFGMwAyW4dlPlUIVRtnjJqFSjxXt2vF_f7-PzloDvO_qSOmbdbWk_eNfxRvR5WtxBzq-DrdaNJf1T-nzrgf5-yhnrkbvNuWB2R2bpUxTzmuYcp_KvVQBH6qlrzK2JpKLF2OMvL5nEiuTwBqPDOCyRsUrnYaw3UV1XBIZw_fMMzDrbie8HppdbQO4gRwefge3O6d8lgFkQlIJYH5mWIwmT2kJl0HHCySx4EYvkNElmiDILm_L0g9mF2ehDJ9hurVkptXAFPQ5hf5I2GTeHrYZDN6lHrPtX2rsUvyE4Jdx0IaTuBDEFq8iEkpa0AVPmtYexQNzN8XcjouO_uch3hytdd7H-v76C2X6ye32Kc0Zj05oXfknJBYg_PJ8iHrfoduwFzXKYLdR6PDxe34DYPeUOD_GvK2NreOffSslJAEz1F7syRzVCXl6jrU4LjrGVWYMMZAWA1-KkQCaHY7HLCBKZtv8KX8TnYr5t4dYlWJQc5Id3Pk1xk-xQ0hs6q0jXahBEg9IAh4Q0Bpj7glA2_4BfkbfQtYtKoYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لحظه‌مردود شدن گل السد از جایگاه تماشاگران در بازی دیشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106594" target="_blank">📅 20:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=O27jTG3qWWVbK8-AuAH4dKt9SoLG_UjASvwoSfSC40krlJzUFn0M6X6XS4i2q71qTsHCT75MFSRmvfGQcqpiquHlo7IZDDVVAPD1168TcX3-vGy8gw_UgbtMla2gmwgklhD78Bx6jhcgKrlmHRBZpmg4hB8YcBp8EPheklUzftNnRnyPtXzZSpTmOkuCGEYAc6O8X7tUcTDCkhribkoMIpVHCOU7faQIPcaZT9sdJoGJOEHj9sz-L4_34JI-sypG-VLLDdtA7p2Uk_YhiuDKocuWBcuW2TQy6tRKIG0gJacBdGp58OMV_K2F1yshEIHwJXXwoz_OnCAExZZ19RL18mn0W9-u7fpdcBsSuS5VFEmgiDoT78S_UYaU6KfxcC0c2L6VRvQSlXICkRn7G3UkojqzH1PKnOxiQ4-JE5Nr33jtlC8fn4gXjDzxStxk3qcQ79_erbkfilJhRsos1bTYClq3ppvYUmwsZVaQ_ixZNuZxYhPYOatCgvhMVx5zJjyuPti5F6i_SIeCxEy5ek2ExyDQclFZKkVMHPP_PP_aSsyinWpDTvD30GWsFU5w0hch_wrz_HgnENDIuvl9DoQrouIOEFeZ_pOj-OBCsgQd5yz3TXFabfZF8NMrT1OW-tjgVKwG247fvYemGBH4OFhPc_w2VwfLX3EYzpkjxFNE8Uo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=O27jTG3qWWVbK8-AuAH4dKt9SoLG_UjASvwoSfSC40krlJzUFn0M6X6XS4i2q71qTsHCT75MFSRmvfGQcqpiquHlo7IZDDVVAPD1168TcX3-vGy8gw_UgbtMla2gmwgklhD78Bx6jhcgKrlmHRBZpmg4hB8YcBp8EPheklUzftNnRnyPtXzZSpTmOkuCGEYAc6O8X7tUcTDCkhribkoMIpVHCOU7faQIPcaZT9sdJoGJOEHj9sz-L4_34JI-sypG-VLLDdtA7p2Uk_YhiuDKocuWBcuW2TQy6tRKIG0gJacBdGp58OMV_K2F1yshEIHwJXXwoz_OnCAExZZ19RL18mn0W9-u7fpdcBsSuS5VFEmgiDoT78S_UYaU6KfxcC0c2L6VRvQSlXICkRn7G3UkojqzH1PKnOxiQ4-JE5Nr33jtlC8fn4gXjDzxStxk3qcQ79_erbkfilJhRsos1bTYClq3ppvYUmwsZVaQ_ixZNuZxYhPYOatCgvhMVx5zJjyuPti5F6i_SIeCxEy5ek2ExyDQclFZKkVMHPP_PP_aSsyinWpDTvD30GWsFU5w0hch_wrz_HgnENDIuvl9DoQrouIOEFeZ_pOj-OBCsgQd5yz3TXFabfZF8NMrT1OW-tjgVKwG247fvYemGBH4OFhPc_w2VwfLX3EYzpkjxFNE8Uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌اول العین به النصر توسط حسین رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106593" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">العین دومی رو زد ولی مردود شد
‼️</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106592" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106591" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">العین خیلی قویه بیشرف
النصر رو کرده تو قوطی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106590" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">العین یه گل به النصر زدددددد
💥</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106589" target="_blank">📅 19:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106588" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILxgf86LdhBeL7BDMyqrDDOJOfYzxGttt5hAYupkSyZZdJYay5jxdwKJhw6levxtBZVp0dWi8OsGt2i8rA0AUR_MMU583ETld63qJpV4T4ynLsqcOp23PtSH6ZmZn-Z830x_6_s9Wo48FqW_ZCApOaB8xGME4tghIM464VzEyFHfcH83mB4R-hcGFKqkdt743c-qOQskG2ZUSXX8j0oxTNf_sI4uN7FlwevG9q3Ab9SxMZ-QkE_Ber9vd-yefpTIPXEF4xXn9F9PSkXgKH5OcVAxCyPO7xAb5C38xc5I8NcgOhVrxvQh66OKXhjdoATTWWHqZWOJ0LTTeM7P26Rr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106587" target="_blank">📅 19:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=XGohviLji9gEAytJ8tkTf1XPOh1W5wfPYE0qtMkC9MxbHa3_rjAJFIBzs4l0xesyeH73TmGN_owKpBrJoS1YcLisIegPXTiiH0dCwkP5orXny5VGzHh_9LwofcwdXaEF4dTpHt8AwVWR7EY9araQUQkp3qNlp5OSeD49Uea99rucgizUsHoY18D9KbkFx0g8V3bjW_OPoO1_c4qUUPGfA_jcth9uruGAeFHynyStI8gcx3QWHjZUQL3sGlijD2noDpyBQ9K55ng_EORSBg4nyfuUVLJiyFwAyu_6x3CTHV9XTXHnZAP-dHAmL2X3_my5FT5w6sA3bmZl-D1PE63BKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=XGohviLji9gEAytJ8tkTf1XPOh1W5wfPYE0qtMkC9MxbHa3_rjAJFIBzs4l0xesyeH73TmGN_owKpBrJoS1YcLisIegPXTiiH0dCwkP5orXny5VGzHh_9LwofcwdXaEF4dTpHt8AwVWR7EY9araQUQkp3qNlp5OSeD49Uea99rucgizUsHoY18D9KbkFx0g8V3bjW_OPoO1_c4qUUPGfA_jcth9uruGAeFHynyStI8gcx3QWHjZUQL3sGlijD2noDpyBQ9K55ng_EORSBg4nyfuUVLJiyFwAyu_6x3CTHV9XTXHnZAP-dHAmL2X3_my5FT5w6sA3bmZl-D1PE63BKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
پست‌سمی الچه در آستانه بازی با رئال‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106586" target="_blank">📅 19:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106585" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjL8WznQIy_KfblgLfmbIDtXxxntVn8Qnr2vMVpbChO1HF1IoqyZEFBqWWXfrUXR7ismwK7gRaWWJx5FxByG4-sg_mOG6N277IO_i71ExunqUaeOjBC1fISs608QmheTO4IP-Dm3Q04JKBknu_Jf2TWvwO-XTgYbQcEnSqsmFpov6kMut28aTKf-8MECmWHnPqWRFasHQFd8ZFKyWCEyWmNWiz4tlh_o5TnTE_S7JuShv1lJe7q4ESsdwk2JZCsRPEj-7VQ9d2kJIVVUqWP9zDor3WHrLgWNa_e9YBOYsI8xcl260hXD8jwcdXy3cDd90RQeH8IXQeMfbqcFSz9CLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
لامینه یامال دومین بازیکنی در قرن بیست و یکم است که در 5 هفته اول لالیگا، 3 بار هت‌تریک اثرگذاری در لالیگا کرده است. تنها کسی که پیش از او این رکورد را ثبت کرده بود، لیونل مسی در فصل 2012/13 بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106584" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=s4d5CqPOpfmrmNuB_FE4BiI6HITlXKH09CC4BG2Mm2yjCanINToejSQ-o8BpaVdwJ8inwkuELpS-bq5WuJe9JsymFlGn2-ANcuBQsXAd1HaAQFUiG4QRzc354UR3SJM4KJ3uqq7DQoo5kt8gfJxBnDb3u2DUrLrQMzDprEnvfi3kAGL108skPRPBFEDtE2OGu0JgoYHJayPgNVXEZG5Ex74xvE6WoE1n0ejQ6oGYIb_LjgylL6fGa72YM8mgOVhT_lBq8dSv4SKTS9J6YkWMmBmxLdxzRnaETR6dia00NCrAicP1kFZzp7hvgxcxWD92OtTEbvmHV6VH84OVyEQg4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=s4d5CqPOpfmrmNuB_FE4BiI6HITlXKH09CC4BG2Mm2yjCanINToejSQ-o8BpaVdwJ8inwkuELpS-bq5WuJe9JsymFlGn2-ANcuBQsXAd1HaAQFUiG4QRzc354UR3SJM4KJ3uqq7DQoo5kt8gfJxBnDb3u2DUrLrQMzDprEnvfi3kAGL108skPRPBFEDtE2OGu0JgoYHJayPgNVXEZG5Ex74xvE6WoE1n0ejQ6oGYIb_LjgylL6fGa72YM8mgOVhT_lBq8dSv4SKTS9J6YkWMmBmxLdxzRnaETR6dia00NCrAicP1kFZzp7hvgxcxWD92OtTEbvmHV6VH84OVyEQg4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
امیر نوری بازیگر سینما: والا منم جای نتانیاهو بودم به ایران حمله میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106583" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7gMFkNE4kb0a4ns8hUaSrsl2QJJz6pWsgQWFNkJTAM0zbpyAhCTKIk0OcHQtUJOMT0X6uqPGPRLqxfZX3C79ZeoF_zgvmS3KatMWwKfHbbsKgDDtAxVRvscF_7lhU1M4JI47IjxadZnB3ym39Z5cS1rlnh-8XEtqPU9fpLTNFzg9ZJG_eeOcS7-gJLdW64OZG02AZQbVb3ZO3WsVYjW9UZsdujVxQJcBY2cBDaa0mRvxJFcUSECTx44hYPeSmKo1Bb51wXoQkkbgNdYlOHPB1FN66-b5H8JWSv-Gs5aNubTS4ncP5vbCtT_ve8aQ80GEFXpsDfYG5eOvOMA3HFSXKCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7gMFkNE4kb0a4ns8hUaSrsl2QJJz6pWsgQWFNkJTAM0zbpyAhCTKIk0OcHQtUJOMT0X6uqPGPRLqxfZX3C79ZeoF_zgvmS3KatMWwKfHbbsKgDDtAxVRvscF_7lhU1M4JI47IjxadZnB3ym39Z5cS1rlnh-8XEtqPU9fpLTNFzg9ZJG_eeOcS7-gJLdW64OZG02AZQbVb3ZO3WsVYjW9UZsdujVxQJcBY2cBDaa0mRvxJFcUSECTx44hYPeSmKo1Bb51wXoQkkbgNdYlOHPB1FN66-b5H8JWSv-Gs5aNubTS4ncP5vbCtT_ve8aQ80GEFXpsDfYG5eOvOMA3HFSXKCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی مجتبی پوربخش درباره جاویدنام سحرخدایاری ملقب به دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106582" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
