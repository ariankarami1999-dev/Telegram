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
<img src="https://cdn4.telesco.pe/file/piD4lcIqYLobH8lH4Y7HkE_clKNZ6ybcG2Y1CwbQjhNN05YyuJN6If-r9CxZsi5V5_VmQqCgi-CV3pmOA0bCibVZ0H2hctQMHBAEHafqb0q2srCP0HzYinBh4SWyxmkt0WGbawyRKo1R1TjawOwKvxFyOhoQ8M-cGkWpFG2E9fsMm8JouzJoc4mmnbhxK9wEiWVQk4-fW7FpffzPGPc0oQsLH0JHbQL3vS2OGJR9llZdWAd_oos1Bp4eAUFtfL2PRKGGMOlUp2IlW4UrdhngFe_J54wGbEp4q-svt_InxqBGqah_VDUFx1ila9l9nqC-vWMMHpjyyxSNzfzYu2012Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onaQrXsBM61k2-e_7xrmnyDgdAktKPmTVNWbi3cpoA7EWzmUaxY0tIwGmGiL5c6TrmhBsWsDVCAN03Z5fhAKVWmfNUHFZ4bifyJp3GEt5UtoQ1RSaD6uNcDxsPEnLvogY4KWG31b1aHEV054YEkCf6jKOVeNyvPDjAsZEmujkNITforAYnKXZ5wW2QmDN9YvI7cwONdNnNw6ekt-xg0i3CWkGOVLJYtjuthzUZB9gpiKfttTVSsRF1aiZ7UKniZjd4NiJgpKTysis04AOSlMqZDyxfqjUmLNaaYBW5o-3XwZxpe5xAtqzwOWj_Vdmp-NkYux3fdchOY1DIr0mbuXC6DY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=KAxgK-b464Lye4t7dtvQmaQK6YvMNyt7-81b40qnEIS8neoAKeFex7qjfFVaX6aZMcpCWKvdgoQcKURhLhE9yrJzdzhoGXmIjU7pqCjhmvL229ad9fxG0duCJNlHiTh1gU_5jRJVqP6UkbhSc2VbcDx2Bq3Af26QW5WiHVJYbx7O9200JlTLZN6bqWiXzZ-HhvOwaNGiRPpJZQBvf8hBQNk28lPDDonHmKEdd9t89Xo8hpnHo44myFobfRHVGKLs2dgeaHqDDDTJBl2SFDjiPsQPa__FsXMZiWov4hNtRrxFrksahdCKDg0AqcHD1Ofqm9yrTRLnGdyEBJFCkN1onaQrXsBM61k2-e_7xrmnyDgdAktKPmTVNWbi3cpoA7EWzmUaxY0tIwGmGiL5c6TrmhBsWsDVCAN03Z5fhAKVWmfNUHFZ4bifyJp3GEt5UtoQ1RSaD6uNcDxsPEnLvogY4KWG31b1aHEV054YEkCf6jKOVeNyvPDjAsZEmujkNITforAYnKXZ5wW2QmDN9YvI7cwONdNnNw6ekt-xg0i3CWkGOVLJYtjuthzUZB9gpiKfttTVSsRF1aiZ7UKniZjd4NiJgpKTysis04AOSlMqZDyxfqjUmLNaaYBW5o-3XwZxpe5xAtqzwOWj_Vdmp-NkYux3fdchOY1DIr0mbuXC6DY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6nEaNuJtvfehjKva7g36NdicnWcqgYfr9wKjy2izqSASstwZZ7Vuc9Rj2VM3Cxfv0DUjbk3MqwVTYHz-Rc0xrOFU107APf12l-c7rWxkepfJgoyIU20SXBioS9WhEsXQRpUH_jE3JfE3vUeIeIQCPtO7z_FIgZ8h27pwaR50Gf2h_aPQceh9_iezARm1M8SH_U-qbn3cdDkGlEocOZF_zk-MRMx6ltvq5vtuPGAFpQckbZ7jM1FJnubTakcJ1vTfXG-HyrzjO4xYp7fKUI4eKlZa1Us0UToFyK00KGkH9clOiqxXYIMTxlOJJzJ6QeepVdzY_uFoqkuX9JH_OIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTdVwuEAaOWpPB6tNiSE8wN92ibKS6jviTFxR9QHM4NyjWa2kTGgs6FMs_x_YDxsT6GxcmmXNzwbTw3J9gN6c-6yuYUG33Ej04I2Y53ul4UUuylVriDte5dlGY0VQTY7TSgIO4B_izOWefCu4nm2qfMiZ1GAe_rA8xRnvmmFD80goEQT3JsY7B7fRRDyW-ffKrKBesh_pjm7vY0vWob-0bAO0uVh4Vvo5bPrKVZ7M8pf7FC6dVkOIwNZZ5HkqwsAdj5X_Ufghys0Q-S5wDUdp5YYTxmOqUDgEDVRumkQpnOqyO4SxuxIcz3JeKxenpKXd2077Z8rZ_Y_J5Tbgmj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cw3_f8ECK9Hkxd8H2AOdSo68XHBCQuwu9CcYI-NLblk32x_SCnBQNupwe9hm7Xr4Z1QMIqHH78bElUrVtTM5FXUGqO61SmfzU5EaNJQq_iCqXpXQU2TW-OQKVY-7fPzdQ4NABWJMtk9YERlkbJCZbh93JUqNyWQY9SQko10kdjk6Vyx5Rjc5KH-UK64_mT-u2VJ5Ukimd3Bpbt-aKGtuJFt7U2dUpI_L5kUrUoaiTFYhc9j78SXrRbEqzlrME84MC94HDFvsM8NYo4SbBOoy9AC1VUX6Yi5oaA4M5PvmVWdIWM6wFi4g5DEpO-etGS1yJF8nbAC4mZ-uDao8eHa3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cw3_f8ECK9Hkxd8H2AOdSo68XHBCQuwu9CcYI-NLblk32x_SCnBQNupwe9hm7Xr4Z1QMIqHH78bElUrVtTM5FXUGqO61SmfzU5EaNJQq_iCqXpXQU2TW-OQKVY-7fPzdQ4NABWJMtk9YERlkbJCZbh93JUqNyWQY9SQko10kdjk6Vyx5Rjc5KH-UK64_mT-u2VJ5Ukimd3Bpbt-aKGtuJFt7U2dUpI_L5kUrUoaiTFYhc9j78SXrRbEqzlrME84MC94HDFvsM8NYo4SbBOoy9AC1VUX6Yi5oaA4M5PvmVWdIWM6wFi4g5DEpO-etGS1yJF8nbAC4mZ-uDao8eHa3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=N5rjY_NLBrvE2TTtUu0zWks_9uVV7LxHcypVFB3l-2U77VanMeBlDHx6hHopsArC40PG4sltBwLIfnqHrACPMlpNXmCloHPwB_8y_hGbabTItfQ822gyJi22BiHcuuo1fDLhIl_exOXgYxnSeOmxxR4QBhMCE48pv3PqkxsuWlmOQA9VWULHjLGAc1HvvdHwwStzZ7oqdeqMbZ_0V8xptW9WLPK52ZacY6jjQpHO2LgfLdIUi3epAIaSJKczmpmE_FDHOtbWcBjEdntOEyCDEiIsBDchLqb3ir8raOBExM1DsC_H-reHZgv5YPlSEkTboxL9zhwjP1xHMnUWye2t7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=N5rjY_NLBrvE2TTtUu0zWks_9uVV7LxHcypVFB3l-2U77VanMeBlDHx6hHopsArC40PG4sltBwLIfnqHrACPMlpNXmCloHPwB_8y_hGbabTItfQ822gyJi22BiHcuuo1fDLhIl_exOXgYxnSeOmxxR4QBhMCE48pv3PqkxsuWlmOQA9VWULHjLGAc1HvvdHwwStzZ7oqdeqMbZ_0V8xptW9WLPK52ZacY6jjQpHO2LgfLdIUi3epAIaSJKczmpmE_FDHOtbWcBjEdntOEyCDEiIsBDchLqb3ir8raOBExM1DsC_H-reHZgv5YPlSEkTboxL9zhwjP1xHMnUWye2t7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج استعفا در ایران طی ۷۲ ساعت اخیر!
طی چند روز اخیر، یکی از شدیدترین موج استعفای تاریخ ایران اتفاق افتاده و پرستاران، معلمان و کارمندان به علت حقوق بسیار پایین، از کارشون استعفا دادن!
به قدری این موج استفعا شدید بوده که خیلی از بیمارستان‌ها خالی از کادر درمان شده!
خیلی از کلاس‌های درس هم دیگه معلمی برای آموزش وجود نداره و صدها نفر استعفا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=Thj2K3k-xIKqzMERax5PVgASkZx9rhoNz3PBMGSF8dDQWHGVsGNZXG-iz_Ab3L8baIrqbckQjAhWvAxS1l_hDu8wG6tpKLzkNhSHesBqQrwjqlnLN97W4HvtR4xGL9BTvgZmLPr5ktvbSU6uAvtZ7EAyKzaTR-2RKta4zYqO2GFKLURLxTAIHTOSV460bwfDry_vtTLAXAAtJPN5kgnezstMMe3CCZYYCTi0kj2K8Ffqx9ZeKIJn5A1WCjeNlR3P7tn8hFWbRa5_tVEBnMl_qmg8B8hIeiC_at4-Z42YRX0lx3XSXSfAxyNhav8m0HBM0r3jvhrROqTEZn6_KmJdxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=rObhVuHu4Xk9Pbc03iDNmsdF79bGtiMUduTyjhh519SJfs8VgrQWB48eeKcXlbrEBlKl5nCHW22p7oBQyLl6lL-adBZb9FoVY-OyMpEFJ1mHvznecSMkhME0fGrATDo-pENXD420PpFlw--2H9ID_99Cr81Hjc8gDA43r7td2gHdZDQlFLMg8z67cZQXuaK_GFe8oSPRXaZaRQuZrPFNo7IyHSTF6hIb0Xo_GNUSKsiuaozuCDh2ocjL5VRTlut7a73Rp-ui2ZNe53Hqkfu0AcIMQ_33SImJ5KcsKbjTfHjXHfIA94PgrXBKi3VWtnfphxqHxh0nEWAY8F5HWyvAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=rObhVuHu4Xk9Pbc03iDNmsdF79bGtiMUduTyjhh519SJfs8VgrQWB48eeKcXlbrEBlKl5nCHW22p7oBQyLl6lL-adBZb9FoVY-OyMpEFJ1mHvznecSMkhME0fGrATDo-pENXD420PpFlw--2H9ID_99Cr81Hjc8gDA43r7td2gHdZDQlFLMg8z67cZQXuaK_GFe8oSPRXaZaRQuZrPFNo7IyHSTF6hIb0Xo_GNUSKsiuaozuCDh2ocjL5VRTlut7a73Rp-ui2ZNe53Hqkfu0AcIMQ_33SImJ5KcsKbjTfHjXHfIA94PgrXBKi3VWtnfphxqHxh0nEWAY8F5HWyvAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNwXjljDlGYb-55_lCqGxWAlCL97OJPL3VJoZWzpi5f10NNRUo9s_kashw_pf1KOZ2U1JSMfKkFWZRqOWWK_srHmvXi34lZfE_xDu-o_8N0s7MS18JjAvSllCPWXv41E9WNNt8z2GZQVDubDzXEaq46-pDTyBE5_AxG0ReKHy17x98E-u_N0hHOBLw_dPx-trYQXJttiF2LR7wPlQ6mUk1v2EENQVkTnPUhwgyHHnG0Dx7pdpaS3JWdqO9LpENRjuJYyRIvoVaX6HVT3fvNfNXcyGLFcMWWJl8RfzqasBJcEeTp1yS4Icio-j3PRKcoLBmUk9GabPvO7oMFk7HucfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBS9MoZo4Y8PIa73auyXTUv4YgHnQeR2p7xky1bXzEo2MSvQVtv57CInVRc0zy4IAysILFtyCPeZw632OkpYPt-rba7fpeD9zh6yJWy3Ooxsf3jAOJ5YKD5FzXZdQG6a1Jq39vrZDZe90Yj3EtvaY2GOSaibWPNTqYdxcNbQYSGmmvBRqfkS6Ya2kfhxN_U5vG7huVYMs80iwmEOfKKdBtOhzL_BJa1hgeH8GWTNeqA2-jywr-khJToNBCDGP_ubOVKKpTxqauYihAn4fmmElKs_DEfz2fU3xhoTMo7cb4B4bKgKtDmoJeviz1xogqMpGqNpuPIdtkypo5BhDu_jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72478" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfnz4HNhCjmpCOQ3YDYodkdKKaSPx6cmFT4vIpXLBQIPbHANjAoKv4z99SaQ6wZo9ljVlN7eiyoYnnURAyQ9-HEiaPWSAKGKg9ssluGR8WjCMA5-1QN6rr9yqfpUXozB4iam7k8dB_FMni15bQSx6tcpD0iaFc5r1FVFZgqj3I1DDASCmM8ohuujdDLOi3GNXdNvk-8EXhorhE49vmDdkp8kUapbtvNmbJ4qGIy67vZrk9jSa9ZslCrTy3p6Ch5EJUGpdDyhZXVAk0b_nxPQEHGL-ijJSuW8xWSJvkRx3FordrXAOTKiwlQqoAUtKj4ZGsxc83AYwTc1ZtdzfJSeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72459" target="_blank">📅 13:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=iJ5NwnyWfCOqCNpI-Scbw5jUGuaoGWBcAGU9uQKW8RUsBukXogr7Ej4kz32oI7RUSdWZ9ofBzuW-qSsCfFth-9MMh0bxVp0KDTY_Dsb1PQNtTLiXSe3grZ5doPbPOepOpwIJmgUViPBW95wmMJQyyqqMtm7tZoKvtII7t089t7brKTDnLUm32TwyEC5JB-o0IeMMjw0Ono0ZkgV_tUmVqSRTEq8VTMaJmXriCJe5T4N1MyS19f6rToBQD6kYitSSYtU4AfKrAFCvGhFNaDBtI1kmyAho8oj2LDPXMZ5zCRD9Wdq0ZB-DD8yj6YhRrbQev0aoECcrQ8ZyBgJ3aGRYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=iJ5NwnyWfCOqCNpI-Scbw5jUGuaoGWBcAGU9uQKW8RUsBukXogr7Ej4kz32oI7RUSdWZ9ofBzuW-qSsCfFth-9MMh0bxVp0KDTY_Dsb1PQNtTLiXSe3grZ5doPbPOepOpwIJmgUViPBW95wmMJQyyqqMtm7tZoKvtII7t089t7brKTDnLUm32TwyEC5JB-o0IeMMjw0Ono0ZkgV_tUmVqSRTEq8VTMaJmXriCJe5T4N1MyS19f6rToBQD6kYitSSYtU4AfKrAFCvGhFNaDBtI1kmyAho8oj2LDPXMZ5zCRD9Wdq0ZB-DD8yj6YhRrbQev0aoECcrQ8ZyBgJ3aGRYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت : خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
خبرنگار : به به خوش خبر باشید دست شما درد نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72458" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72457">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1910edd949.mp4?token=cfbtNozK6rAcQekhYTbzQefxzuHKDYBJv98Yf5DOIeYufwDQtxkgfwQUy7DljBsGpGezQtwPcobOsxqM7CH2oakHcsLqi8MX2bpgzZqE1Jhc018FFGiROViAxNhLnSBgXvsQtzt-QnAOocd-gE89zPM2-xff3_yJkGotAU9gObvcFEhb7hcCC_Wu8M3yx1yPA6itbM1urOap5pUCTDnQVzos7NuhCOrO-BAtSoB-u8UGtwbkvXZJUPzxDj7nNU147lu9iwO5O1mOYKOy9iWiCv1Ft0X2mJY1HYXEkO3nQ-5mgKnXvHOxM_Dtx0DhBIGMA6oWgjDx1hvtyzJ-SQLujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1910edd949.mp4?token=cfbtNozK6rAcQekhYTbzQefxzuHKDYBJv98Yf5DOIeYufwDQtxkgfwQUy7DljBsGpGezQtwPcobOsxqM7CH2oakHcsLqi8MX2bpgzZqE1Jhc018FFGiROViAxNhLnSBgXvsQtzt-QnAOocd-gE89zPM2-xff3_yJkGotAU9gObvcFEhb7hcCC_Wu8M3yx1yPA6itbM1urOap5pUCTDnQVzos7NuhCOrO-BAtSoB-u8UGtwbkvXZJUPzxDj7nNU147lu9iwO5O1mOYKOy9iWiCv1Ft0X2mJY1HYXEkO3nQ-5mgKnXvHOxM_Dtx0DhBIGMA6oWgjDx1hvtyzJ-SQLujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار افراد از پنجره‌های ساختمان در حال سوختن آکادمی علوم کی‌یف، پس از اصابت پهپاد جت‌سوز روسی به آن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72457" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmp0KF6zo9TlRsVdsq7vu57Zy3oMgaquohJBX-QeqVYGvLfXyp37mTnd6lO1AoJOoF_S5FiQ_CKxhFqLKyiy73ZztkSQL9KcWBOSHUqJVfp99z4sZpA09H-raxlgOT3YYCXK6edgT8HgZmqiDoNtJH7omlyRlgaviFAPSI6hU75GXkSAZ0104BSvXrWe4HkYRAyGTQ9v87_Zix47NfQa_Hh5-w8VHj2wI1JqrBRCM4gWxdmed68nuGG_FD1bJJVMwFqQuRWfT_lFvCCew5bpY9Tv5AxopVo5TwYBu4X7C59B3RplwAzAwV_9EVRFJX_FXwz1yuDfuUinbxwqjH-4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoY0CXx_-e6CUtBlvm6HJRmQJdJoHORZx9ADWw_K2aA6XQkFt1pgEXe_29m7WNvaAWTLD9Mz_ihTXRQu0gQp1jTi6D1OTnpa0CnTdL2U9Kk3q7Z5RAVGSIfNxBDDsa9WGvAhgqn48i0qWHJoJAn0gbIzWv72m0rwZ2DCLLoLoAF6RTIKTM4Cj4g35UrouVnVAsGeTuCzO9JqR0LCj1GotHcJCX1VPNDJ_PoGn0nGluT0JWUxC0dLNBx-6ZdYS-FUcQ_e_tW2NAA-18sTQMWjxM-YI8NrkfOK-h8z220_MlmEdedEdwUHuZYDyy80pIzRP4fI8KoKQHsRC17PQsNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvkX-Don22xBCwUJIh0RPD9Nv3p1mSwaMigFYdHhuPEQHOFeyU6qpwg0KgEU6qxgICQboHkVQbtLWiTEyvzONv3oQa1583IMyERe8n5_bVlWMwdzrwz293WYg8rf7cIzmqnjW2CUIy1gw0-YRhOkMo_jsmQz37nyu5z9uzVqtN4ffiekvI-AeShFIL_pylU0mj-PJ3BY6G3mHlIDE1j8uDXGFJyWK-gbSpv7ZwVeFTKPX4aMbt0Zv3o9hb4u9MXoQ2WIczjUqK3vhBDKuuIAefCxdtkBhq8SoSifzxs34rgm02BjoCd4O8xp1MLc1OL2dynlHRRzb-43V0TUG7Q2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو به‌تازگی در برابر دیدگان میلیون‌ها نفر فاش کرد که باراک حسین اوباما به تأمین مالی رژیم تروریستی ایران و مرگ هزاران نفر کمک کرده است.
«در مورد هر دلاری که ایران در اختیار دارد، کاری که آن‌ها طی ۳۰ سال گذشته انجام داده‌اند این بوده که هر زمان پولی به دست آورده‌اند — چه در جریان لغو تحریم‌ها توسط اوباما، چه از طریق فروش نفت و گاز و غیره — آن پول را صرف ساخت بیمارستان برای مردم خود نکرده‌اند.»
«آن‌ها این پول را صرف دو کار می‌کنند: ساخت سلاح برای خودشان و صدور انقلاب!»
«آن‌ها این پول را صرف تأمین مالی حزب‌الله می‌کنند. صرف تأمین مالی حماس می‌کنند. صرف تأمین مالی شبه‌نظامیان شیعه در عراق می‌کنند. بله، این‌گونه آن را خرج می‌کنند. آن‌ها این پول را برای حمایت از تروریسم و توطئه‌های ترور در سراسر جهان به کار می‌گیرند!»
«[ما] مانع دسترسی آن‌ها به پولی می‌شویم که قرار است برای کشتن آمریکایی‌ها استفاده کنند.»
اوباما پول نقد و لغو تحریم‌ها را برای ایران فرستاد و آیت‌الله‌ها آن را به موشک و تروریسم تبدیل کردند.
رئیس‌جمهور ترامپ دقیقاً برعکس عمل کرد و جریان پول را قطع نمود و...
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
مشکل اصلی در مورد ایران، «انقلاب» است؛ نه آن مقامات دولتی کت‌وشلوارپوشی که در برنامه (Meet the Press) شبکه ان‌بی‌سی ظاهر می‌شوند و در رسانه‌های آمریکا بی‌هیچ دردسری تریبون رایگان در اختیار می‌گیرند!
«بحث ما درباره آن‌ها نیست؛ کسانی که در ایران حرف آخر را می‌زنند، روحانیون شیعه تندرویی هستند که دیدگاهی آخرالزمانی نسبت به آینده دارند.»
«آن‌ها معتقدند که رسالت مذهبی‌شان این است که آغازگر وقایع پایان جهان و آخرالزمان باشند.
این واقعیت است؛ این هدفِ اعلام‌شدۀ انقلاب آن‌هاست. چنین افرادی هرگز نباید به سلاح هسته‌ای دست پیدا کنند، چرا که از آن برای باج‌گیری از جهان و کشتار مردم استفاده خواهند کرد. این ریسکی غیرقابل‌قبول است.»
ترامپ دارد کار درستی برای جهان انجام می‌دهد. او اکنون به دنبال کسب پیروزی کامل بر ایران است، زیرا این تنها راه چاره است!
بانک‌های مرتبط با ایران در حال تعطیلی هستند، ترامپ عقب‌نشینی نمی‌کند و ایران قادر به صادرات نفت نیست.
اوضاع کاملاً علیه آن‌هاست. هرگز نباید سلاح هسته‌ای داشته باشند!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RstxSG-41j--rSzJAvjhKSfhCEwFPFyvMcZHnCKyzeZxNjdROiOXIftchTItSRuOa9_fMFJ3zJ8IvzUN8-1wY2g15xNah1vgZ6qLokchaIS0e5boNSOrIuvrNHnOTEl2Ty7cB-zBHuq1FNO9x7pUL1GE_OX1hqslVKJ7hq9zEjRlpzjDJNdxyXw0kPySh6O2tOplmiacZIZHZDKFOgUawwPTozHCbe-8wDL1PDe9Sd9iv7D0r2zEH-K5uUTtNJb-zFMrmxOcpccMHPfEovtdPpy21GJtIq4GoZEgc0lJa3tVkwCZRSVa9oDUcRWsIBKh1nYEHNEn0ryX9QlyEG1V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmbD8W06FwRDFmOxsqomkfBSx4udSWJQbpmGHiwIt_XrawxrntJDy7XzjWG2G9s0d_nrqKeQuD6NrxC4TYSQJviyGt5nVkRZua-UEiN5rFcZtISlyT-FdBv31TsNuq0f9zQoIHWRdlbXSda8fsNMYkHp94wK8Q8uQ3yQ_ynkeSrysLrdPDGY1C0lAj6RKa5Lzxk7oWcPv2hF4iD1bUfHNKe--p7rc3G8slplR3Ya58U_0ScAWagdQ2bhcjqndd4OlAjEznD1krMWgtgs61Pwv-S3LqJIAbVUo7O99jtiLULb_M5C5MGCjzwHvVkbxDHHQVdgctLQsZ5mYiMCq8DmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=FUd63xP07BfwZzRkfKNRov_DN1eJC8BWa0ZA1C8y6bWGYr9VHkavF3W8hh6EMZjVMw-20A0hj58REEMexkCCcUtd68pEXbLhHuFUAVis2P4KEGziIyDp3tQSRnBcw6bfnGDUuclrSUEujLR0wujC71BwRQ1gs1QTnWdWCnXG0UYmSf_I5RgXjEycS1EjJpUURocCWDN3frNtI1M394ffR2Cvja6bK-Hwg5YlzKqNjiiczhVU5Pge0lYGhgPCbBqX1SuCR_O_wUpNfzLN3HXQ5qJ7_nGR1zMo-bKE0LusE5bhC1yz6-kBoADWe393UhrJbdzly--XnMuiEcwpfN3YVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=FUd63xP07BfwZzRkfKNRov_DN1eJC8BWa0ZA1C8y6bWGYr9VHkavF3W8hh6EMZjVMw-20A0hj58REEMexkCCcUtd68pEXbLhHuFUAVis2P4KEGziIyDp3tQSRnBcw6bfnGDUuclrSUEujLR0wujC71BwRQ1gs1QTnWdWCnXG0UYmSf_I5RgXjEycS1EjJpUURocCWDN3frNtI1M394ffR2Cvja6bK-Hwg5YlzKqNjiiczhVU5Pge0lYGhgPCbBqX1SuCR_O_wUpNfzLN3HXQ5qJ7_nGR1zMo-bKE0LusE5bhC1yz6-kBoADWe393UhrJbdzly--XnMuiEcwpfN3YVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Lq3zWxP_C8mxFgkn_R7cfmIPZMjdAKQ8ZutPUKirWrVpXaeVgFc_nvuCSDG0Mw3xMNNLp_Mowm5TPoZuRjUVPui5aUfSEFj0F9bq_sybExX0hUbsXzKna5NlOmHjzPAXG1wjmMh9BZ6nh4wPqPGtU_uOQtod2QpH6KpcscOqkdHcAS9fiX6QF9K1P0A29c0BOJAwbf-zKUeCjAs-D08PR5vyx8R2hsPVqyDZBuISom0Aj3uFuudfwIkdcZrtoXIDAc39EDQDxbcvtade6jDA2iG-myhMafWh7PHl5HR1Uuk5SSFSckrh6pxe39N3saoFLkFpMgnH7HqrnoPseYzY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Lq3zWxP_C8mxFgkn_R7cfmIPZMjdAKQ8ZutPUKirWrVpXaeVgFc_nvuCSDG0Mw3xMNNLp_Mowm5TPoZuRjUVPui5aUfSEFj0F9bq_sybExX0hUbsXzKna5NlOmHjzPAXG1wjmMh9BZ6nh4wPqPGtU_uOQtod2QpH6KpcscOqkdHcAS9fiX6QF9K1P0A29c0BOJAwbf-zKUeCjAs-D08PR5vyx8R2hsPVqyDZBuISom0Aj3uFuudfwIkdcZrtoXIDAc39EDQDxbcvtade6jDA2iG-myhMafWh7PHl5HR1Uuk5SSFSckrh6pxe39N3saoFLkFpMgnH7HqrnoPseYzY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=S1kamNoTt8QAUzbxKjprl_1lgJsPe1qkkKS4LUl_WEapLcpnicxApIOvzbAc-7hmaPVPhrC0CvbqaqNnl-90urbcHYCk-A6kM6XPE-AmhalXSQvPSfSyer6LlZE2AlPDipXlNx67Sj4oG8OyWJxJKH-3XU4Tj_5-y8J5Z01bmgs9UudfXKYXb1mIDlo8b87Sq31NgzqcW5p8JaJyO9ziSv9_Od-KLbFbaWtmklVYeAMDOTZvPpBVIR6CaX7NZ0le0N_j8jSBBQPcO0OgrWqSV13nL7AZNXUyUT7oC1n2KL8TNA0i76gMLSUEMNFD87HsC3wgP-nYHlVXs2Nzldd5FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=S1kamNoTt8QAUzbxKjprl_1lgJsPe1qkkKS4LUl_WEapLcpnicxApIOvzbAc-7hmaPVPhrC0CvbqaqNnl-90urbcHYCk-A6kM6XPE-AmhalXSQvPSfSyer6LlZE2AlPDipXlNx67Sj4oG8OyWJxJKH-3XU4Tj_5-y8J5Z01bmgs9UudfXKYXb1mIDlo8b87Sq31NgzqcW5p8JaJyO9ziSv9_Od-KLbFbaWtmklVYeAMDOTZvPpBVIR6CaX7NZ0le0N_j8jSBBQPcO0OgrWqSV13nL7AZNXUyUT7oC1n2KL8TNA0i76gMLSUEMNFD87HsC3wgP-nYHlVXs2Nzldd5FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=jRp7eEAAL6LJ2UrVmu7RkuWq5P7NJWz0qy4SMfva0rXPIRQ11fEcmcQgfzGaveyiZ_91LDRQ_HBqZGsjORNdvT_rgKNafMvMYnlZPhLhv1peWOsdgNHB8gifg-tLtBO08cPMlCFsuYxduhDbz0j4hmD8XotfCP89puQ5Y0PiYKFVeRXehicrhv_laBoYqrowsjcXXkb_Bptsb1YMeL8zeVrHMTUNvA6E7Du390Vx3xR0DqkKQe3224PXd-8G2XsA01wfoulabBhmMIvMdpbPYoONPHNSkaPKAcQ3SK65msvUV9xmiUCJctuLngEqxpoCcD60gPnF1WbFoSWTqikBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=jRp7eEAAL6LJ2UrVmu7RkuWq5P7NJWz0qy4SMfva0rXPIRQ11fEcmcQgfzGaveyiZ_91LDRQ_HBqZGsjORNdvT_rgKNafMvMYnlZPhLhv1peWOsdgNHB8gifg-tLtBO08cPMlCFsuYxduhDbz0j4hmD8XotfCP89puQ5Y0PiYKFVeRXehicrhv_laBoYqrowsjcXXkb_Bptsb1YMeL8zeVrHMTUNvA6E7Du390Vx3xR0DqkKQe3224PXd-8G2XsA01wfoulabBhmMIvMdpbPYoONPHNSkaPKAcQ3SK65msvUV9xmiUCJctuLngEqxpoCcD60gPnF1WbFoSWTqikBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=vUaJQLEbnxG2aepi1_p87HD_3Y4yzeXgBy3i11Rg9iaTN7GUX6fla38SnfYsMW4sFOvxWAGhIdQBQpSna6Wzm2ufqs0fduHYiK4LxrDXeaBsKphZzUAU1OKdI2_ioS79n82eL4OzukpJt_ZHT7JqJiDZZ2wm43JmY0k2GzonyA5k7d_TK7nUx0Zwsqd4QWITAvvrh3GGpflxM50y_b-QhmkV5sC0h6HHTkLJoFAqqL1dOjeJ8oLrUIRo4K0x4lqfY6z_pjFoq9ldRKrnkIbgGQHepkjQ4MdPO-Y_V-MG2yf_LO45MVnAiN6J7_EYDQHyEvPOmamQgyQe-GKXBXJ22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=vUaJQLEbnxG2aepi1_p87HD_3Y4yzeXgBy3i11Rg9iaTN7GUX6fla38SnfYsMW4sFOvxWAGhIdQBQpSna6Wzm2ufqs0fduHYiK4LxrDXeaBsKphZzUAU1OKdI2_ioS79n82eL4OzukpJt_ZHT7JqJiDZZ2wm43JmY0k2GzonyA5k7d_TK7nUx0Zwsqd4QWITAvvrh3GGpflxM50y_b-QhmkV5sC0h6HHTkLJoFAqqL1dOjeJ8oLrUIRo4K0x4lqfY6z_pjFoq9ldRKrnkIbgGQHepkjQ4MdPO-Y_V-MG2yf_LO45MVnAiN6J7_EYDQHyEvPOmamQgyQe-GKXBXJ22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=TdmIjjTYyzrgcxpl6ZlnML4tMclgx4bbN54Xmtqw1iEMHNh7nQg8pnEv-c6KPQlG2GlaWUjo208PWZQzpKwL_QODm-PW_6GryOd2JFJVlw67dLlEBYA9kOLLCemyOKhIIqiWaXUw_H9eaYci-eNRgatIaLyFabrGyEZpXpwaTlRkwK7oD4ggy_kBrF7M2rHWIDqt2UnwDeHbJ6LG8VXUQnhICAlmVwGxHhcPHkqq-pkQvyfr2Wr84Y0iRHjAy-_9-0TCP0IYQ4Q9_2VQOTvYuJVe9yRZ9bEH-7cqEXMjBEOwZ3L0D4eTY3bdJmTtlyVHLfGNvTEoHG9YybR6ZqYmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=TdmIjjTYyzrgcxpl6ZlnML4tMclgx4bbN54Xmtqw1iEMHNh7nQg8pnEv-c6KPQlG2GlaWUjo208PWZQzpKwL_QODm-PW_6GryOd2JFJVlw67dLlEBYA9kOLLCemyOKhIIqiWaXUw_H9eaYci-eNRgatIaLyFabrGyEZpXpwaTlRkwK7oD4ggy_kBrF7M2rHWIDqt2UnwDeHbJ6LG8VXUQnhICAlmVwGxHhcPHkqq-pkQvyfr2Wr84Y0iRHjAy-_9-0TCP0IYQ4Q9_2VQOTvYuJVe9yRZ9bEH-7cqEXMjBEOwZ3L0D4eTY3bdJmTtlyVHLfGNvTEoHG9YybR6ZqYmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGu06fUVjHdtbYRuE0NMTIEJOdH8ZGpm_7HXPdrytN87zS7rExGKRQQBSFn_O9XKZ8_GqhI4X5UZuqHxjOWWNROObKxwSm62pT1WUycZcEPalzxhLsL7mLvYLGJCXJK5WsW9kJB1YpnpA-dyaiNiDkrc-zQkipAc4ALr9nK_UbHf-QBYceeb21DZv4-db_NCuVl9k6TJdSVBZ1D8hgCgXQU0UvQ4cXH6SwoP4uCCBsOKh3rJRLl1VygxJkbqA9iPDKNzLq7VU3ssVE1qtq0v0wTXlYOyFpU38JbsIU2bu2kZzjeg0TR8samObQZDFQeD9B_RGX0irugL7BlgwKLKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1m4bOKk1KAOrvxVMCNtttlkwyK4Xxr3HmosTNRF11TpDT4-AbyccULI4PNGbwyMHtZc7KXfkw61nFJhQfME4seQLmsCEEbLEtUIVeCSgfcTFpUkkHDzfvGa1E8f3QqELcFKTjDLDXBIMgLZ5DzeJfLwgfqzzKEvGSjWnh_cdI6K3VIsrM_OAsJ75rn6f2odshBd1b7ybwvfduLSaO-M1yB8XyyMmYPGeXwwwXTcVBq6lyCpEmOhHljnLd4xc1nw5wagDAYT82YhfmQWV0M-dlfawbqq-_iyqcYGwMCJpCZliO-ZVe723q3CXkHUD-d2X9KBsSVVaY2r61m4LNAg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RveXV1AHCA8hQmtpMZPlYPfbRhnov7xFQaI1ZmgMqXpg12FuurBKZHR_lIOgFIrNgdSe3y7IkXDqyOVlrxe51PNQrFJqh9yvu2h6QllTe-GGrhsrVcAfkqL0XBLgbqFnki4vmJT34MGqaOEMJkY1GDP0HRBda1fe_npAIdegBEr-hiqF_-JeWtnFYIS8aMpyjHBigqxQ-bY8QLi_MjjZzq2gOOjVr5D5abi31ceUJNMM717mrmyVv0xKVzas5QWoKKykFT6pTugRNhwkvSEUvn3iD_qiSHJqbXLlw1RQaM-OxIjKt2I2K5H78e6t76uDU1CE1dTyhpC89vQl6COwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=SQ56qX3pKrEt4apuUmPeIvBIzX4jF1huSnR_eW3X-HEZNkajAWN903jnjFtHrqqx6BBEfkV11YdgFsRrDHKX_hwg_HR4j32eECxkVsEXEaLhhwac85uGWWlj7MzLgvqTgr9VikiiApq5Dtg4_hKarOGx8WqZgj20t52SGm0YbwcyDThbeuHaadQIAaBQOjlv_oh-6uvShYf0E-aiuYoca8b_N7Nzo4pyL2YGPmzIqCNMOxKJeEtt6c_mK8oiNzLOY8Nd2ZTnKnJRVEG3rx5wUsydinTb-fJ4Y6MWyGdCkI2EreeuLR2ZJuQ0kuNYQq6vN1rdsZw55ubjdVeRZJ98BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=SQ56qX3pKrEt4apuUmPeIvBIzX4jF1huSnR_eW3X-HEZNkajAWN903jnjFtHrqqx6BBEfkV11YdgFsRrDHKX_hwg_HR4j32eECxkVsEXEaLhhwac85uGWWlj7MzLgvqTgr9VikiiApq5Dtg4_hKarOGx8WqZgj20t52SGm0YbwcyDThbeuHaadQIAaBQOjlv_oh-6uvShYf0E-aiuYoca8b_N7Nzo4pyL2YGPmzIqCNMOxKJeEtt6c_mK8oiNzLOY8Nd2ZTnKnJRVEG3rx5wUsydinTb-fJ4Y6MWyGdCkI2EreeuLR2ZJuQ0kuNYQq6vN1rdsZw55ubjdVeRZJ98BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQrSlYyY8as3WEH2Y-XPe3B5g6HWvTqlE4_-BC1FB3ArUGj5lSGYTmyhV6kT_ZhfJAgsxc341GhyILxibONMRuxHgJM0TWW9Z7L21QTtTIKzGUjUPIPOmmlb0NeWyTJpRsIgkWRK6pO2U4uJ1gm9zvWkLvKajLPx-to_obtHEtq6hIujOXIieDPPQqcjiSJlZkWsA2QdEFPofq9hDFAQYyYwIu9h1j55V9tUj5M5NXBOlmosf9wAJ4utN99uqGsl5km3oLNhobYagvx-3FfLxH790Ay1F6P2ABk70Hnl29c1ipo1wJbmmw4pSMKYaP5xqSSH_Qe7HW_3f2lDpUczCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVx8IbcHmXjna5dmSuwWOpYaDCmaojkzULxcseyHZRYZpGFEeXUSux_fFd3hl2wOMe4B8HhkUN9zRbYUrEh3aDFjkE2NpLWbVmC3eH8jqclzB1Ag3GMfR8--4VqLnfCSFYcF9ZI1yFK85z0L0Ze5ZitVlB30JwYHGmv1690o7zJMdmyoTKmKLZp8MIYGMf-q0RzQQbVCRL6ng3cSVb8KqK02yn2guVZSnewH9AvYdPaU0RCCTaQ9ZP4fWk6fsfFGD0ryy0_2zsV1Gs_IVHW3Kf5lQgiMwVeNEQ7mAXmhQ3339JuylclkIZOc1k7h8xwBEZskylsm_DKPegB6i3_EVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaXoU27fLQq8L4DqunSzSxzRc945_r9qscA4lV_e9dCvOGx2b0k0LP2gGDbTvsYPTxaH6_vL_tU9j1dmL7BkFbTw0Cic7koR3EZ3VwYllGbVkLqgooYfkPeHVoDrUJy4vLSwHhxvrkrRKD5Piymij8eNitBJcwTXsFNt5ZkOj5tOKvS4rlcTkttv0vld3Zj8s13ouDWbb0ZSSq33-7uVaIXtTORRs8CJKovSbRS4FwQAik0K4TpctsFDIK5rQAjQJ8qNaT5ewoSPvgnCC-4U3A6LuR74Y7LBp3qzn2FUVPTjBkA9aBSm42Z6_x0ibbLcmEter0Sls5xNbZd75jlDpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=GiomfbLRFEncjveA1-WqIhno9q9SUMyI97jHH2fzHdvVHeJEKAAL_Mpifg2cxcAO4qSA7SSG3t6HtVo16Y1tp4zDiQ3JEEtaipYcnxJBlAIiKlkBFZkQ3dABwb3_pI7dn_ZylXpFSdiss83pqpkZD17DUSPmKJa8iLISYxMLGYwNQsDj_Uocf4brrOEHPtvMb78HImTjAR8PL_gSeaGBwW_EAS51OdekZ0w4u0Jd3wceYof3BJ0w3QXYJOj5-kwuqB5JT2879PTShEinuKQAh1RvGpIdTCWicM_K7OWLtEtv4zBis5btN1OJl9ddg7F-TFQhcFWc2Xu75nKNbilJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=GiomfbLRFEncjveA1-WqIhno9q9SUMyI97jHH2fzHdvVHeJEKAAL_Mpifg2cxcAO4qSA7SSG3t6HtVo16Y1tp4zDiQ3JEEtaipYcnxJBlAIiKlkBFZkQ3dABwb3_pI7dn_ZylXpFSdiss83pqpkZD17DUSPmKJa8iLISYxMLGYwNQsDj_Uocf4brrOEHPtvMb78HImTjAR8PL_gSeaGBwW_EAS51OdekZ0w4u0Jd3wceYof3BJ0w3QXYJOj5-kwuqB5JT2879PTShEinuKQAh1RvGpIdTCWicM_K7OWLtEtv4zBis5btN1OJl9ddg7F-TFQhcFWc2Xu75nKNbilJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=Yaj2dgAwlpP0BNngUGmyKGcIraRPG_fV9LE6-DXrxNo4UVvfpwkD9kVlFejPXGBzZkrNm5qCt5E8ed7tlvvnc3_2GlL32QmHhJ5Dr1jVZsjfVKFlEcE9Xrqx6CxDt3ALT8oR5ivL31q5cAdUWZL7ysn4iDUchlFd3FjdQ3vJCCgwwVJNGq1v4EBmNc8YvbwfYZw1LWnA_wi293PEqTpPfSt2s9MdouL43dTWm_SlM31b7DBNnS-vTYT2mhjRzo_w5C8eweuBgKyf6J3wm6SWLRj-QhRNA2mO-ncFe1wTevtBvHsOtq5TStsx7DC-46X8dO3Cv3G-aFF3ZFDiTDPROA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=Yaj2dgAwlpP0BNngUGmyKGcIraRPG_fV9LE6-DXrxNo4UVvfpwkD9kVlFejPXGBzZkrNm5qCt5E8ed7tlvvnc3_2GlL32QmHhJ5Dr1jVZsjfVKFlEcE9Xrqx6CxDt3ALT8oR5ivL31q5cAdUWZL7ysn4iDUchlFd3FjdQ3vJCCgwwVJNGq1v4EBmNc8YvbwfYZw1LWnA_wi293PEqTpPfSt2s9MdouL43dTWm_SlM31b7DBNnS-vTYT2mhjRzo_w5C8eweuBgKyf6J3wm6SWLRj-QhRNA2mO-ncFe1wTevtBvHsOtq5TStsx7DC-46X8dO3Cv3G-aFF3ZFDiTDPROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=PZZ3ogu23DzTbVy1WCbTiCrBWx03JthIXFa4Tk5pym30ObnVflc8qP9q1nmuzrM5ofbo25r2NVh8l2TTn4K4XrrcYxKBRU1SursRxXfdyVSj2Xu2vg2hMIQQIs7kP3jzaq9r2h8OLfefyu9_jcnYd0bC0cqgvz9Aq6T_6nrpGS2jeo0h4f-0e2v9sfCFPEGTVkgbUEnaXiVpAio3ci11suDfb-ngvqP4lNw1PbaIAkr1OBjf6Htx5RTI88_nf7ix3UhbNiHd-TZYbYAKeLIQWllSLLkePKIOYj36IKpEJETHTns_vA4OLJI0ECUeLXo_o74QHormxFA2izMHKuB9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=PZZ3ogu23DzTbVy1WCbTiCrBWx03JthIXFa4Tk5pym30ObnVflc8qP9q1nmuzrM5ofbo25r2NVh8l2TTn4K4XrrcYxKBRU1SursRxXfdyVSj2Xu2vg2hMIQQIs7kP3jzaq9r2h8OLfefyu9_jcnYd0bC0cqgvz9Aq6T_6nrpGS2jeo0h4f-0e2v9sfCFPEGTVkgbUEnaXiVpAio3ci11suDfb-ngvqP4lNw1PbaIAkr1OBjf6Htx5RTI88_nf7ix3UhbNiHd-TZYbYAKeLIQWllSLLkePKIOYj36IKpEJETHTns_vA4OLJI0ECUeLXo_o74QHormxFA2izMHKuB9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=F8fo14fNS7aArdVG1Og36OagPE-1XsQWgLdXCbf7stkOKmATjuPeGjkWf4WIa4yLwUsGxL59zCVvBmILT1pvKIJ3MB7GxIACFO_h52w6tW_p07yQoUxKkVcn86cLfQ1di7FbvmV3lVmK-K5676VXQTi4zqJ56mSOkP4PfSEaRzqEoxhZdPShqbk5MnmL8h0jVbfMdb-g2pELBEoJPVtFJOlqJwakReG80AATNdS8ZF86zW1vhQJXFg-njDlkjnYE1g1jgURqb9UI2rQSkgKAZLJHO1s3OMo65k0jWBmG0OtzyhnmVAr9Bnt3fCyCdEPCJxBnqDp4dBR4UxEAXZ9oog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=F8fo14fNS7aArdVG1Og36OagPE-1XsQWgLdXCbf7stkOKmATjuPeGjkWf4WIa4yLwUsGxL59zCVvBmILT1pvKIJ3MB7GxIACFO_h52w6tW_p07yQoUxKkVcn86cLfQ1di7FbvmV3lVmK-K5676VXQTi4zqJ56mSOkP4PfSEaRzqEoxhZdPShqbk5MnmL8h0jVbfMdb-g2pELBEoJPVtFJOlqJwakReG80AATNdS8ZF86zW1vhQJXFg-njDlkjnYE1g1jgURqb9UI2rQSkgKAZLJHO1s3OMo65k0jWBmG0OtzyhnmVAr9Bnt3fCyCdEPCJxBnqDp4dBR4UxEAXZ9oog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=CTuGkoeSAvLWcaxU8SQSUF4sb5RuQZgtgje2rnfGNKeGtS232Md8cdUd2JeY6yczyXfgmakDSXOCHi6909oT_5ewqGq3svufLTepMQ7SsZfvylAvvtvdZY0BAr8YEU8AaG7a-zQFetVJhoEvp-K5DKuO9sha_Pduw97lHcFf6Amj49WJo3vdgeCh0Du6xwYJDM6sHrpFa3cIKCTlIHgz0BiLrov4yZB2c21MtgvJPlmC7CfeOZv0unEEz7zTlo2KOv4rpwr9dZb3O5b3yq4OBd5JvP3-ftG5hu23HxIY3vqJhvJt9C5_jc2AktuutOluRIp0-dfsggU6-QxGr4bPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=CTuGkoeSAvLWcaxU8SQSUF4sb5RuQZgtgje2rnfGNKeGtS232Md8cdUd2JeY6yczyXfgmakDSXOCHi6909oT_5ewqGq3svufLTepMQ7SsZfvylAvvtvdZY0BAr8YEU8AaG7a-zQFetVJhoEvp-K5DKuO9sha_Pduw97lHcFf6Amj49WJo3vdgeCh0Du6xwYJDM6sHrpFa3cIKCTlIHgz0BiLrov4yZB2c21MtgvJPlmC7CfeOZv0unEEz7zTlo2KOv4rpwr9dZb3O5b3yq4OBd5JvP3-ftG5hu23HxIY3vqJhvJt9C5_jc2AktuutOluRIp0-dfsggU6-QxGr4bPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=vPdhOy-N4MDoVXxcYHq9JbvXa1ZkjkWVRq4iq-QXgN6JljnTF5wOyZAdpRcWxbYsHs78E9yx24q35MOThBT8uwdwxi4PiT5oDIySk1443PNpych9p93hLIagM5W-FOQ6NqsFo7KwrLvPyofFHSy68uXbB4zM2G3OZGXrRRhTS2gwrWTkE-FEmcIkAJN8gI_UdznwVJ9enuBsKHC6Fjma4SU3D4kWCKVzNjgZo5YYrFEzjEB6aHLiqm_vJBfzSsMArWvqvMxVXkAxLW7hbbF3LmTUhu2VPlJTZJFKsvyK_4P3gm03rnU6T50h4M7ZfaBhg6G3iqf30AoT48Q7YfdT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=vPdhOy-N4MDoVXxcYHq9JbvXa1ZkjkWVRq4iq-QXgN6JljnTF5wOyZAdpRcWxbYsHs78E9yx24q35MOThBT8uwdwxi4PiT5oDIySk1443PNpych9p93hLIagM5W-FOQ6NqsFo7KwrLvPyofFHSy68uXbB4zM2G3OZGXrRRhTS2gwrWTkE-FEmcIkAJN8gI_UdznwVJ9enuBsKHC6Fjma4SU3D4kWCKVzNjgZo5YYrFEzjEB6aHLiqm_vJBfzSsMArWvqvMxVXkAxLW7hbbF3LmTUhu2VPlJTZJFKsvyK_4P3gm03rnU6T50h4M7ZfaBhg6G3iqf30AoT48Q7YfdT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=oO_pIWnWsOMf-4n8QrES0ffWyTp0d3F1FW4BaAKyUuR3y9MiSxboZOBWrObShPpFNt44FUP75FEAH1C_rTIMiDUtaFiiDWXDjOk1aAm3__kl3HQgQGxdSUpkFAfzGKsMWDkvTObg8Bbt8QMWdIIQcGsFpupi7LhFCblrJqXRa1tNLQIm5cG5msd2tMu-7-ilBDi3a5mioFeVy5ILBauvhjFMf_b4mdOieeckZsNaL-ymhEzgzGNZpCQg62nHTO89ztnaBEOpb3x3zP7hbuzhXLP8LAV2uR5jvi1BVNTjD85xyhvY2eSLvSELSmwbdBnW_l_tiT8SgH2BB4cIDX3GtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=oO_pIWnWsOMf-4n8QrES0ffWyTp0d3F1FW4BaAKyUuR3y9MiSxboZOBWrObShPpFNt44FUP75FEAH1C_rTIMiDUtaFiiDWXDjOk1aAm3__kl3HQgQGxdSUpkFAfzGKsMWDkvTObg8Bbt8QMWdIIQcGsFpupi7LhFCblrJqXRa1tNLQIm5cG5msd2tMu-7-ilBDi3a5mioFeVy5ILBauvhjFMf_b4mdOieeckZsNaL-ymhEzgzGNZpCQg62nHTO89ztnaBEOpb3x3zP7hbuzhXLP8LAV2uR5jvi1BVNTjD85xyhvY2eSLvSELSmwbdBnW_l_tiT8SgH2BB4cIDX3GtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=jB68Xg56Nl6daaqcV-6c1Mo1evmH1aikA3tPjuBPOjt7SYzyUqRITU00igb7c-xSppwHrpubbliXl8EgbGdP5D1NaADm8ZZWnM9RzFlLsxBqhEH1kv-4xDl1nyEyTliyIXuEzExDQ64oV7S6ewi-nWKq9T3zgP5OiDo8_MyXBCayYzh2l_DSUFwyO704bl17hnC_wQZM1ODPWvV7y4RnfTwfOk4Esp68EbzqACAEN6dq4x2V1rs4D8Nt-24Mr_PP_Klf1XhikpkogpH2DTXyKIiRSNtWVZ3Zyz4ARY6Z045cNwZrbHERZTdTEGPDAk01P3LZC2WdhRPtszDBZ922yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=jB68Xg56Nl6daaqcV-6c1Mo1evmH1aikA3tPjuBPOjt7SYzyUqRITU00igb7c-xSppwHrpubbliXl8EgbGdP5D1NaADm8ZZWnM9RzFlLsxBqhEH1kv-4xDl1nyEyTliyIXuEzExDQ64oV7S6ewi-nWKq9T3zgP5OiDo8_MyXBCayYzh2l_DSUFwyO704bl17hnC_wQZM1ODPWvV7y4RnfTwfOk4Esp68EbzqACAEN6dq4x2V1rs4D8Nt-24Mr_PP_Klf1XhikpkogpH2DTXyKIiRSNtWVZ3Zyz4ARY6Z045cNwZrbHERZTdTEGPDAk01P3LZC2WdhRPtszDBZ922yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCG7gFId7ivs3vO0-hBgAa9UqiiqBU4cfaWONdTXfLvIWeBDZIs5fBaMcgmiT5l8WODNmxD9TRTNdhjM18ARXFSlroByd1QYf7vzd3mFOcaCCRFJ4yfs1Ky-ptGrs3KKRTYZN9EgMM8_hXR32yYUis6sueRh44NOADHlNz7qI9N2-mkNw0G-wLhG14c3XaUeouKEiYjh9sui8yZY2DJJtg8mQFmgFUDVhzKibShveGI6KX2aRqT4Q6FJ7kB31YDLXT_1hG9ebLEozDFj5peqo270EML1ReathOzAu2hpDZOVoSQJ8rj6V6VBNffo_VuJkdmvTZZa45CpYXJZFWIp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=KROEROYmnbjYRn5OAGxSU__nFzXJFFpJO9UV33IEKHo6V8ZHhGHU9qXp-6n1onaXcYIc7yXcjA9Wz1USMQoJJ0NzQEG-vxkKFPLEnHoCpczx9mf8tN6cm14YDJC4re_9ADDKOt9p0ORrfoommMTihqiwXYGxyNTfRIngh-FFHbVPHAG9wlZE8hoKVgL0lPhVCPcRavsA9Qi8kDqdIC7W1UjjPX8I3a_bHZJiEzCknbIgCCOY34Zsk24huSSQLy7zMYgtJxqrPZV23yUjgwkmuxy3P7WSU9skU2jyUGewf40nwTTkz3g_SPTHl_C0CgKecDNLJWecAM6ij6ywaIhccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=KROEROYmnbjYRn5OAGxSU__nFzXJFFpJO9UV33IEKHo6V8ZHhGHU9qXp-6n1onaXcYIc7yXcjA9Wz1USMQoJJ0NzQEG-vxkKFPLEnHoCpczx9mf8tN6cm14YDJC4re_9ADDKOt9p0ORrfoommMTihqiwXYGxyNTfRIngh-FFHbVPHAG9wlZE8hoKVgL0lPhVCPcRavsA9Qi8kDqdIC7W1UjjPX8I3a_bHZJiEzCknbIgCCOY34Zsk24huSSQLy7zMYgtJxqrPZV23yUjgwkmuxy3P7WSU9skU2jyUGewf40nwTTkz3g_SPTHl_C0CgKecDNLJWecAM6ij6ywaIhccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4swPmHyId67Mgubd4_IeNeBkBlXgj95mWGWIUKZPalymjjcWavc-2MGNkGW9QleSRP4iuH68KDIoi19XdkfbEydXdchmUphLQtb_tqKVktqiqZtKr-YP5sWyWPNZYruf4vvLfvLjl1Q2RkQBmGf1m5aYeSBRysFHnN0OfbU2jiD7CJtRwAA9KsJ1kYnLbOkGTJt0-S7LcUmawF1HOAuC67nKPNlmIeYL-zgVmn-4-4hWE9LTTf60nO2OIzbya3XFsNRySHw0yH3SDeO9vh7heNVf-bXigxld2Xr5vdSo9_B-6nyaauSSZE-u5UcQiQdC4v7H-LQajRDLmtYQ43J5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5L6SvflQKLUYBVlXbEesf74Nw5Y-HDuFrP2KsGXM69ZhjsKP7L-S4IR6LOOSQmE9f65212hKpuuupomtv5di8HQQuJJxs33N_JIEQspm35ICrJj74340timlT6NccTY4juJmAypYq4rqu-85xGWEnSoVFXO_NOqflGCWE1ubDkYy-wAjJfgN968A1QEM0FreftHDxEZY_mOA845RZtSfeFELGtfpswsyT3c1Cs-sHUVTxYH1zzQ1VvMpwsZMgvHGTV-f5UxmUtFFVP4ntSeNGf5C97u733QhDEPLf4JjUAu42DyR-7aoQgpZAEh865vXwln6uxrSZTDjilELd7RvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=pvJsSEUEPT76jV6IWYWAK5RiWgcVEmxpGRdH2OLLWtAa9nW9G-NJVYYBUBkGc66k3uo3L1S_ou0J8KI48D34LkVOBlYLW-2GoHUSCwKtwkjX3L9q88FbRNTbvbkAJmBsJ0KQYNERMHkOJP0jd89fPuL0MJJRS9_xJFXBxEcWnXAqYlNSlMZC1-JtpPzzOtHxCLC26xNjijCtUeoDFnzeokg5By8OQvR3-USDhNewBnDdKL2ub7RdAVJiVLSylal95njmAtKtV4AHbGGydbWKpDDefix-aUDVMEbP-W5wZBHnoFeSNmdpyHmgLpTCig1Hwg6MOCfpkm0bCA4D-r09Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=pvJsSEUEPT76jV6IWYWAK5RiWgcVEmxpGRdH2OLLWtAa9nW9G-NJVYYBUBkGc66k3uo3L1S_ou0J8KI48D34LkVOBlYLW-2GoHUSCwKtwkjX3L9q88FbRNTbvbkAJmBsJ0KQYNERMHkOJP0jd89fPuL0MJJRS9_xJFXBxEcWnXAqYlNSlMZC1-JtpPzzOtHxCLC26xNjijCtUeoDFnzeokg5By8OQvR3-USDhNewBnDdKL2ub7RdAVJiVLSylal95njmAtKtV4AHbGGydbWKpDDefix-aUDVMEbP-W5wZBHnoFeSNmdpyHmgLpTCig1Hwg6MOCfpkm0bCA4D-r09Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Pl8YZF20eSGDPPrkj4BIadVFl8Pb6qdcl0anpQQX5P3PTe6ITawRmMraVihhL9SZzzIMlVnmfyDGejRfJqnI5-1TwQ7vE6URl11sZGgoBPjL6wdUK6Exq7Zr7sUzWzhBD5fF_dWtvVjoJsF3w7Vcm3dUOL41sd9XdJuROlFzVXgxq-YaFkdGPG2F2XMavIVlXj2BRRqirTiDBH_QakS838iHPvqS943zW1jVYIkHN4wYDkazh_e6psUHYfCeFqjWvhO4K0A7b6coS-kpsKAcAz0Si3fPwyPGIytFndCT3F4akvL4sgFwdH-VQChDK2cx3Ck-YW_0wd7GEt6mJGSokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Pl8YZF20eSGDPPrkj4BIadVFl8Pb6qdcl0anpQQX5P3PTe6ITawRmMraVihhL9SZzzIMlVnmfyDGejRfJqnI5-1TwQ7vE6URl11sZGgoBPjL6wdUK6Exq7Zr7sUzWzhBD5fF_dWtvVjoJsF3w7Vcm3dUOL41sd9XdJuROlFzVXgxq-YaFkdGPG2F2XMavIVlXj2BRRqirTiDBH_QakS838iHPvqS943zW1jVYIkHN4wYDkazh_e6psUHYfCeFqjWvhO4K0A7b6coS-kpsKAcAz0Si3fPwyPGIytFndCT3F4akvL4sgFwdH-VQChDK2cx3Ck-YW_0wd7GEt6mJGSokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=Vef9Lrfqfelt7KyHne29OgLfoMfxh-7ZRpFXF84BTDke4kXqmrVgDyb6UQU-kKliDEc7we7iK2QnON_5Xwrv-lh17CeQ8mIhyojrkLnp9B-EPOkmJDXVhcV5A8Fyy3Zoe5qv0RnfdCO9T33CNuTdGOe524kxEyRqoiKbPAy7IxRg2wlCknSMhyLfrLK7J6tPMV6InthaNHzK18m61muHJP-CyqbPjDXoBfNbnHdHBdJLTfRRMzLmz9nUmlJEMVZpei5XxATqxkCegtFeOCU40N_J9YC6ZxYEiG6wLiGOTxzal8ndeMSG_WQBqTCd3EAChCAPmb_BzYpWCC-39r-psg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=Vef9Lrfqfelt7KyHne29OgLfoMfxh-7ZRpFXF84BTDke4kXqmrVgDyb6UQU-kKliDEc7we7iK2QnON_5Xwrv-lh17CeQ8mIhyojrkLnp9B-EPOkmJDXVhcV5A8Fyy3Zoe5qv0RnfdCO9T33CNuTdGOe524kxEyRqoiKbPAy7IxRg2wlCknSMhyLfrLK7J6tPMV6InthaNHzK18m61muHJP-CyqbPjDXoBfNbnHdHBdJLTfRRMzLmz9nUmlJEMVZpei5XxATqxkCegtFeOCU40N_J9YC6ZxYEiG6wLiGOTxzal8ndeMSG_WQBqTCd3EAChCAPmb_BzYpWCC-39r-psg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=AdBD_bwwgy43lpryqMpaDi5uNccCwvLShmmZ5vZETDaDFh34l8MKIjQp_LeaMvfVFTrAVhjlb67VkxRAbEBzY9_-grMzCIvfl-c2OGvngYPNQCHLpn_agIdCC0mWGoHh-Yr-y4kQV3qK5ENuKXMCvJnOYCJpAd1KCNE4hneQ-tL2RY-RV3TD3wd_xbfzqEHmTIXDUVsPkBRVxzCffIwTRKuCSBGc56j1yjBjUI98fyJ6-rO1Udp0vzZOf8mOschnmYSK9hBdF4sOu6dtJ8QsPe6rdSBvv0o7XHAz41ulTIHlCCxsYsGHAAUA37wmptDy7Is7Se6E5fvjI28B494yDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=AdBD_bwwgy43lpryqMpaDi5uNccCwvLShmmZ5vZETDaDFh34l8MKIjQp_LeaMvfVFTrAVhjlb67VkxRAbEBzY9_-grMzCIvfl-c2OGvngYPNQCHLpn_agIdCC0mWGoHh-Yr-y4kQV3qK5ENuKXMCvJnOYCJpAd1KCNE4hneQ-tL2RY-RV3TD3wd_xbfzqEHmTIXDUVsPkBRVxzCffIwTRKuCSBGc56j1yjBjUI98fyJ6-rO1Udp0vzZOf8mOschnmYSK9hBdF4sOu6dtJ8QsPe6rdSBvv0o7XHAz41ulTIHlCCxsYsGHAAUA37wmptDy7Is7Se6E5fvjI28B494yDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=CJluNLU14HTQelozBp8nflqjk-stu6apK_BRTXkv0tpQoXM0uYJKpkdUuoqkZliRqcHi91aZue_po-rdicT9JpSa39aNWe3xwtTEXxBjRjmeN_pTqR2WJhHRw--95IxPxYKSQUZzUaJweryXa-cO1byPbHmwnk8uJSOHZGXS7zFhqLBHBFyNFhQ3FCapzkgdwjVpESUJqF4B5iXdC5-YM3r5KHLL-uIa7rHc-yJobJ4h_A0Ik__1aVrq1QacQgBfcxxO1mJ4ai4i8mxKZnOA2adal16QLl-m6cIaXdEnetlyH_mZA48JAXW2te_iiJIGU3i2P1H1ln8HQEZszrenMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=CJluNLU14HTQelozBp8nflqjk-stu6apK_BRTXkv0tpQoXM0uYJKpkdUuoqkZliRqcHi91aZue_po-rdicT9JpSa39aNWe3xwtTEXxBjRjmeN_pTqR2WJhHRw--95IxPxYKSQUZzUaJweryXa-cO1byPbHmwnk8uJSOHZGXS7zFhqLBHBFyNFhQ3FCapzkgdwjVpESUJqF4B5iXdC5-YM3r5KHLL-uIa7rHc-yJobJ4h_A0Ik__1aVrq1QacQgBfcxxO1mJ4ai4i8mxKZnOA2adal16QLl-m6cIaXdEnetlyH_mZA48JAXW2te_iiJIGU3i2P1H1ln8HQEZszrenMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WALg1w26dJDlyLnCg6yw-lTj2aaFHtN6SUf4JtGqmes_ayQMgnaOPCFCN-wn3_wfozt-SjO4buz59URH4OoJVeo-GQdfIFdBJezGNQEAI80Xs0oteDZ866njBzsa_Y3cmXtdUFCLcWyA0LIQ7p_nYUjF19r_gaYVlXtoHn0AC24FqXLr93RpY6r1QV9HizTT0YJgJmpTgVtL8bWpKd89hFoNp_X7Otn5tpmvrsEdA7sWOKNF6WvWQQZXOxyaR5hXOiYXKvt69ScRUN-rBV_ZNwyZ4xmrnjd4syfOdgR1wNlw-jISi3zKeCFWLJb39pswS_S9gMvxNJF1WosZO-AhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=Xbxi18oQzdCNzOfQsmGsHfmuBJCmuQIZHcLlVZ77B5Cc2ildRcrUEST4oYo3ivCANwHF6bo2WwiflF-nX8k7YSgGQFHEtlmMycvO1fsWp8Zmj5_MKAaV2QQaugS6aPkPdWiZGCSkR-PD-eYTS2v77Vf5rbp8fgFOm_sh15tgfTiDBRCgZ4y1watIAHiqHzuAuTd8RsaJQIkDvGj6AIKXQsqvqvx0tWALSFPTbkpp5UnxdUabHRhATqXPL-qzJxwKxi1I13TQvc9DoV6F5lfsw5bn1Yk05CjL8MI853YbJ-BW1mBCTbeaNrnTEgSbvdroe6dxSYTrNgE8lGd_umwIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=Xbxi18oQzdCNzOfQsmGsHfmuBJCmuQIZHcLlVZ77B5Cc2ildRcrUEST4oYo3ivCANwHF6bo2WwiflF-nX8k7YSgGQFHEtlmMycvO1fsWp8Zmj5_MKAaV2QQaugS6aPkPdWiZGCSkR-PD-eYTS2v77Vf5rbp8fgFOm_sh15tgfTiDBRCgZ4y1watIAHiqHzuAuTd8RsaJQIkDvGj6AIKXQsqvqvx0tWALSFPTbkpp5UnxdUabHRhATqXPL-qzJxwKxi1I13TQvc9DoV6F5lfsw5bn1Yk05CjL8MI853YbJ-BW1mBCTbeaNrnTEgSbvdroe6dxSYTrNgE8lGd_umwIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=PqZhx5c108Ml3OL3AkpyJPGHfiTRyz6e7wsf9YyIgx1eafQV8hVoUEHEOVh4pjIHsiTfyGdNq20Bw3wO8PnNApf-tXp-k6XlZ15TBM4EiSxX3TAIfu8PcbK2GsaHPnUslWHzL9eSJQLDfI2v_j_-DFuUt0bveOciE90_HxFSs5DShtSSq8LrSGHAXVCYRph7mrIfXkfsdIHGzRmYZ60mRs_zV8v6HsRInMnHQ-RaTfd13OrGMfUWkSB1ufr3QHN7iATsJiLAixf0_pLizeSGnt2tlSHoEJ7QNQ8Fdt_Js1k5BgrRIEkMTSPwGki4virH4x2fe3qwMP-HCYkfxfFwXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=PqZhx5c108Ml3OL3AkpyJPGHfiTRyz6e7wsf9YyIgx1eafQV8hVoUEHEOVh4pjIHsiTfyGdNq20Bw3wO8PnNApf-tXp-k6XlZ15TBM4EiSxX3TAIfu8PcbK2GsaHPnUslWHzL9eSJQLDfI2v_j_-DFuUt0bveOciE90_HxFSs5DShtSSq8LrSGHAXVCYRph7mrIfXkfsdIHGzRmYZ60mRs_zV8v6HsRInMnHQ-RaTfd13OrGMfUWkSB1ufr3QHN7iATsJiLAixf0_pLizeSGnt2tlSHoEJ7QNQ8Fdt_Js1k5BgrRIEkMTSPwGki4virH4x2fe3qwMP-HCYkfxfFwXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=jTTc9pgXzlZqlOwIk-O5CEz3lXx8Bbgswumwf6SKWU2WH1wAzwe10E8oDSfjW2Wlt4gt9xHutIU-uMPv1mvQp4aAk4rOhwYlLZfgLxF4IAsM-uAIvGitNC6--yeqXvaSm6RgwusccgyT31r3rtN5ljqPhOqeQiBqZvzMRIdo9X0Es4U2ae_9gUQoyH51PwCsg1hbrSrjCBG97yDsCscwwB4Fjigy_aU5tiCK0J_HZ1_Bx2HPLDuSlJElQ-1VNGYxU6C0i7Ge3-79IkNpDflLZh0d2Jt9ofIcabWAAgTx88oOYSgPbiOrqAgAS41S4sG6b9i16HRuWniaNmWPkdx4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=jTTc9pgXzlZqlOwIk-O5CEz3lXx8Bbgswumwf6SKWU2WH1wAzwe10E8oDSfjW2Wlt4gt9xHutIU-uMPv1mvQp4aAk4rOhwYlLZfgLxF4IAsM-uAIvGitNC6--yeqXvaSm6RgwusccgyT31r3rtN5ljqPhOqeQiBqZvzMRIdo9X0Es4U2ae_9gUQoyH51PwCsg1hbrSrjCBG97yDsCscwwB4Fjigy_aU5tiCK0J_HZ1_Bx2HPLDuSlJElQ-1VNGYxU6C0i7Ge3-79IkNpDflLZh0d2Jt9ofIcabWAAgTx88oOYSgPbiOrqAgAS41S4sG6b9i16HRuWniaNmWPkdx4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=fl8icQY_7-ajEjc_CRRkfI11PAQ3guKxNuxF42ilgmlEFg3F5s94jyDMF3JyPF0OZEuu5c3KIni8nS-Rar8EJKKZQ7WO5hfGnKxIDmnhSSue5E6DoSOql0M6aZdoLKdRhRONGjCLMUL04ZQVUpd4JBdUTD997rJo5IdARovGPF_crOmG8z1Rc4dRUgJ7DtzE8vzrGQhS6lWYrODsci_2QMawk8EO_fLVUNXnr6SOYBhEFtfQOd_ZFy7sr1ZXNU4Fv-hQT3AhN0VXcRc9Z-c4ld6n6k7H2g8F3He9zKmohPhl1-Q4k6ZuozVXNAXXreNAJrNfPQ8SE96CGj6JjZ-OFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=fl8icQY_7-ajEjc_CRRkfI11PAQ3guKxNuxF42ilgmlEFg3F5s94jyDMF3JyPF0OZEuu5c3KIni8nS-Rar8EJKKZQ7WO5hfGnKxIDmnhSSue5E6DoSOql0M6aZdoLKdRhRONGjCLMUL04ZQVUpd4JBdUTD997rJo5IdARovGPF_crOmG8z1Rc4dRUgJ7DtzE8vzrGQhS6lWYrODsci_2QMawk8EO_fLVUNXnr6SOYBhEFtfQOd_ZFy7sr1ZXNU4Fv-hQT3AhN0VXcRc9Z-c4ld6n6k7H2g8F3He9zKmohPhl1-Q4k6ZuozVXNAXXreNAJrNfPQ8SE96CGj6JjZ-OFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7mT_4ocMWn3n7Rykgy0t6QkNNa9-4CqifEZKyz6Ns-_SWxbuEAQNgjEui0lwi1Nk27FLmJr0w9Inx3nscmvaNsKz1HSAwyt_Q5SzvtwylJNrQCKfKiiMBGbVPFkYv2FJG3ncBwOaUofL4qdl-cwi7p7VIWSFwEuS0QNejibywpEO3eJVl20Hjnkc--TWF-_OlKC0NCKoIOHHq6258jYtu7de8-iVgIIXJvbpstTUsVaN6aAGDfbC7Rdt7YcKZiPc0GSKNgT1vxS2fd9UzMugTwdin0GALDwdu0BvYgb8looaZWgJjEwtlYjll2LQwPVtt44ZRYZbWMncwyvGIVopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hkL4OHHAuNWN7sv_CB9i0ZnmMDr-uMFipG-srC92DhTPZ7X-cYEjP_bz5c9DFvWuiIZae9Si2GveT1O3N_zdxnJKuMuLVDK72rHy7SX3GFw5eyQbPkL139ZIulwA5WrQjkR6dcoTfSQc_Y682ul-2miz-i3RwyKhfkck4uCa3gRfALwH9lYTXhIo0Tj-gzP6dKrm3czGfkCB07SxVFxfno5mMHeqnPIM9BSLUs6MPupq6JeZf60jlLMEDLRniaX7CgnFuYLBqGYD7uMC3qVjxsqg1U2R_a4qgijIpud3X8402Mz9wr3tFehZwxBPY7014KcCGEFhsdiIA2HoDZMXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=ACcQin0Cnv3oTF3DZgx96zJRxeXMctjBA05Lq6pKKvei23YuMaQNCCyYdFTeMoRnqOlPZUKdY23R1N-mRtJD3iAXeuBZnp0E5thfCOLTMw5-U_chWJ__Vq2dFAnWq94C-LYegcBFeyPAuXuI_EzjQw4cORYlT52rc4IYxY1woaDTn47ZTZ9zVaVAV13tftpvRO63fO5jslIU-exoGySojbsQz4hLEYbh3aScghLO0e2YRfPhi-cpPRkowrty560l7EaSgvKOrBCtY7ZduWuUafhlkoD-0yuE0Elv62OlGRJ2moBY8SwohOlHYbj1Mzl4jvHMY2v3d_IUjj0gWUwC7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=ACcQin0Cnv3oTF3DZgx96zJRxeXMctjBA05Lq6pKKvei23YuMaQNCCyYdFTeMoRnqOlPZUKdY23R1N-mRtJD3iAXeuBZnp0E5thfCOLTMw5-U_chWJ__Vq2dFAnWq94C-LYegcBFeyPAuXuI_EzjQw4cORYlT52rc4IYxY1woaDTn47ZTZ9zVaVAV13tftpvRO63fO5jslIU-exoGySojbsQz4hLEYbh3aScghLO0e2YRfPhi-cpPRkowrty560l7EaSgvKOrBCtY7ZduWuUafhlkoD-0yuE0Elv62OlGRJ2moBY8SwohOlHYbj1Mzl4jvHMY2v3d_IUjj0gWUwC7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
