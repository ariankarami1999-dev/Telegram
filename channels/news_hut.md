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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQTmxReds7fgMeWH9GnXjd-JT4rmg9K2NKc6oLpyi0n6KoIMkvRT4dGsk6rTVIAJ_TqX6AjK18z2-XDYYje6Ls1uFUgOfJ-teHqVvZAFE5eAU2wgf4PNPBD9ZHmQcFRm2fcomp55ecGSvF6MYC3YuQGiqLwbTqufnbYi3Pzfv3S4kmodOuRxSjiMp5yS-AHX4c777pVxxhA0H_OkPhfcEdqnNjlmIZvRdJNOCuhVCZmu96GuPXcwoPASPD2_rNKs_C8mynKpY9z50BKujZrHOWTz3AjVAY9viyNe76uYCNRQC0ZzWn1dJCJ8QrhGcASEPylrqpzycLebbZynRdR_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAbO4NI4_Y77orqeebYQsDAtVOA7MP0CoCqceRAS9GvQ1oNwFLpnjhZkvd5TkkCVCRFTHIdldapDJ2JsbrA3lEgkxGeQqaitlZuROPIOxmQxYJuIa0DEVWnPXpeQisRqw9uEwAezPODsq0lTV0Z1RaWJohJ-4pSNGKS65b-dterW0XRK6y0Z7zHhIlO-G28PZarN3tSCBQRuRdJnPYobacAKoOiQAlwaEygg1NJZmLt59dLDS4FTys9M0GQulLMIYlo-kshzjt5ZO2ybBN1O8m3wdEDwopYR0ixrKxnR_5XuKXaZe_1zh-eSIZE4voSBn23VCbUWoUEOcEImpcdeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=hnZyPUz6kp9Ln-Tz3Oqao6qtVhB0m54oGlbOMvergnB2rPH9SrmxPw4Rg01chztPa9IJA5Otq3dW_QDP-L2KV9XAtuV59p-G66SpuVbJMWJSkel81BkGrRQX-e0NS7LG9EfSgra9pSsjv0dcxn6tt-pY7gbxF8hc5ux6FtRjI1vEiTDYdg62qlIKDNQcoGCpYe_hdqfX6DDXIKHy0VxkrOJbqr6yJTSKGBex03Tn0cKRrXInPBGfY67Y_dO-Yn7-qxy3DxdfiCMIMXI-mwjif66KK2tgY--LM89kXOtLuRwgQoZAijJHkCoRjPx2BIa-ytaINOX1wk6BXppRyaMU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=hnZyPUz6kp9Ln-Tz3Oqao6qtVhB0m54oGlbOMvergnB2rPH9SrmxPw4Rg01chztPa9IJA5Otq3dW_QDP-L2KV9XAtuV59p-G66SpuVbJMWJSkel81BkGrRQX-e0NS7LG9EfSgra9pSsjv0dcxn6tt-pY7gbxF8hc5ux6FtRjI1vEiTDYdg62qlIKDNQcoGCpYe_hdqfX6DDXIKHy0VxkrOJbqr6yJTSKGBex03Tn0cKRrXInPBGfY67Y_dO-Yn7-qxy3DxdfiCMIMXI-mwjif66KK2tgY--LM89kXOtLuRwgQoZAijJHkCoRjPx2BIa-ytaINOX1wk6BXppRyaMU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=p3q4-pSEF-bYsXOi1VrZTg61iCzIC4xXyCsQwRlEcD8vDpjF1OGYslnRhVMGrCNpf-r6QchvV62RAkCGvCbLdwEK3QhSaZP2O5iWAHz0Ck3esqM3WnyNrVUN7Mt8usM0GmySXOs_8RBS0f0r0YKZpr9Kho5tWgwmUkOFBA2IqkiGQ0LGo0YRV6QYxU8TpbcizM4MMg3MbSBllibWBIT93kVabmQ0OYBRz3M3qgn1EeMY2j-3xtGmDmzVQDNk6GU2Xv0sj4bbM0326svHd4p37zs7PSsM4k8Xi0melUErbS1ASQ0F7EqzeYMAfU1cIxGnKyuUNlBoWjMH9NaKHHxveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=p3q4-pSEF-bYsXOi1VrZTg61iCzIC4xXyCsQwRlEcD8vDpjF1OGYslnRhVMGrCNpf-r6QchvV62RAkCGvCbLdwEK3QhSaZP2O5iWAHz0Ck3esqM3WnyNrVUN7Mt8usM0GmySXOs_8RBS0f0r0YKZpr9Kho5tWgwmUkOFBA2IqkiGQ0LGo0YRV6QYxU8TpbcizM4MMg3MbSBllibWBIT93kVabmQ0OYBRz3M3qgn1EeMY2j-3xtGmDmzVQDNk6GU2Xv0sj4bbM0326svHd4p37zs7PSsM4k8Xi0melUErbS1ASQ0F7EqzeYMAfU1cIxGnKyuUNlBoWjMH9NaKHHxveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEoa3z83DhAmzHX79exkK9qm8caMwF6_7-43V3W11mOpO16TUjW6oYvzNnOtBDb6sFSBgN5grLxLYFwLspNngtuW_HLTrfFibu3cy5gjzKo4A1C3iu2XY-VJ6Rn5kXgWofx3NdaiaZ2je0neZlXIJ61Mi5eFItEexiZDzp3wX_syg9v2EpSgvSZtzmOYO7-7qDNa4dwyIGhQ9lAiXIVL558iP4TdrLO0DW3pcI3ZvaCiR7XEpLpeBlpyIZl86JzVPeR8h_i-lo7OzfT7_TdAidV1Um67Ni2jm1mm9dK5mSqt1quvtRQ2AwcBDkYTnEuxnCyjfbisRhx4UnTQ-QMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT0CMqL5pPY3arsHSxgGKfOSv2B5DwmznjC3YRpW0B_11eqtUwcgQqVSwuvY6_mV49Sd_9ZA2SogOD2z95i6b8lHSjoYGMJffj53FxnT4yfyeyIJwqFmYLWJkao3xDolM7fNNmBP-f5P9ZXq5dE9z3F8FY7blInvMXqlLVRw3KkJIbppJnRf5qofylH29tF9BbQNWq8av_FVr8dXk39XmG8sL6nX0M2y6AprRWs6fhJJFxd8Dz0bHg2jn3H52GnHr5aDMFCOItYnIN5u56wuAmx0jZ9bf9F2eS-Ps93GMewhegq6XZjskDUV8xBxcJI5soJxjHBp_TtP5w9ZheuSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1tDxlaxzjR2YB9JxyQWxuEnwLhHabUAIQq8wr0VnJc4sZ7f9oaXx_v9rf2svFmKudl5VVBzBIkXlMttV1rZojBaKnbzGnnyXTIcgEu0gvjgKec83vxZkUcWSfJy60u8c4IDMGnCa_H8NpecIDQuHGXgHsWquRatVx-0UaWDELHqTAcOm3DyM6AF3uMPG7GIw2kAMWzuM9gskdP3FxZTCBwQlvJMPLVismSd6uupipiV9EobYGeqSn8vN9OOq28jQ2-rYFpOPlbNldowfMmW3jCwtITuQynlhmK_Q0QSA0ehmwvFTv30hR1EwCceKd5-qKgQaazAAR28nicUIAthvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WN0bGlbrSHUJyW6kt4JZqOio16tYtgn-N_986P2CLZ6WD8sVzWkvK2cyRKnhU4Hj6GM-VBotYuYhr15GFiC1lTNZIi9YvH-9YMoJpGDiuW-16XhGi0mv9WgCvaPuPHYJvnAcVGBZ7s1K1NYTR1q_BiPNKojfGCc6Af2Eot4sjW-4hZxclMK5p9Q8CUsEuopM_gSNzZm5G_nNxP43APECVIfa85hFycQOGdNUphM1-bZ8gG2gkqjTcErWdFaKJuvQfXlJ0-VYySnjNgw7N6OvmijbESp9MVydmSxKifioA_If50yNbHDIMoutogHnKUtA0N-j_lBE_unl4FrGq6FWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vttN1s0h7TKAf_frPo9ce-a21jC_c17SLTwQhVBG0taJvi4X1AXXDdU3-7jv2V0Pa2vvFJ33B8c51eaxSYE3o1e2bGt08o8TsDbf0iuxubk4wdArABpN7jtouZjVCCuEitB2ifnWAmefH_yqNtzL6mo8kXcwdEvBipLpE-b1swXtbxINLOUdn0VLXnJDg1gZOesVEf-VGp6Ylabxha90o9bJQnELGu-rHqM205RP1IF6RTMRP98Xg86D-dTQuOaoAqtEs8GK--fRUvMKzAYGBKEUxz3ksxyZU7VPU0p0nUZlDhJLsFrFcT1zIEgdzdnswXIW8BszWixdc28NZ-GZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1l9Dk0teRffYIOrRzaJyBf6438qW_BiOznbkjB7lzPaWG3YHEVcTXVW3tTvzgO5VS0c470NKQoHW9mOCXVVbe5vlxI2JUydgl1Dx8TAA0wLtTkvSr8c_1y7F3OVIlIV03HZIyVOtHV46AMV2izfitqEGQaN3p1iLyaTZyNXAd_zGsVzFF50HTy53Hxl8sP-023u2TuRZ1HvAXE0eOv0dQ0K757FntZdiiu6bDhiYEX2kBpgYW8uuPQ3oAwUm9abjSpLYDBzhRFWtaQpRWWEaA30YdAn1r-0vBPEAm5Ovxi9dlHlov6pGYrIDJTANR_pgJvcdgxcWHgkSlB1A4DUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBNu6-r1vNZT0xopJwSvuwU3GNhfoJslOgjozCwj-hMH06B3b0sAmdX4h4LRs4y0ppL0OXQ37cjN6FKea9Gv5lp-sBxr-qrCOYjsO8Mz80PeRoL4gRfSB1jMT2C3HmORTz0u0VlbYfkNPykIqqiUAQZPzCMHmSRrIXG5-pbj3lDViuSQsRWunoAe45_77GNwWxrBjsSqKuS32ZgvyPMbEz0B0TLJ1nty_4FmoDgS4h32DYM1irfAmdzwiAhFCUGJ-GKfFei4Axgbh7FkhT6F5ECOMgXJMz_evk2bsIxjMcwqHZlsj0r_MAaLfE1Mppc5BkL9crcizFLONKewo0XVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=drDi35fRLUsZ1fnsGfZvdxLIv1W8RYUvuFRIIccdPytYsbAPX-gF8WdaNIcbE3NWUpyWVUgrO-PW6pGgkV5cuH_gIxmHc1AbxwCCjDaVzxv1XnqHOC8EaiNIpV_Z7C6VBmiWDiFPU-EQvCwQw_EXbXJIgW6HWDfrfJlK6S7PdDkQo-ZqHuHICiG4JC56SedRxTRg0-WUFMHNDAaJMyTfKtsO5NjBWzOz-Nb7JINv8aEZPIV2c7gDjWCPW3tik45WG7A7VQEz2j5HG1QuyBYAfjbDc3BBogc5PPI7RNPUGX81zDRJqADpdDUI8TkwnfVr9wNffMRml01C216ic-0Qlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=drDi35fRLUsZ1fnsGfZvdxLIv1W8RYUvuFRIIccdPytYsbAPX-gF8WdaNIcbE3NWUpyWVUgrO-PW6pGgkV5cuH_gIxmHc1AbxwCCjDaVzxv1XnqHOC8EaiNIpV_Z7C6VBmiWDiFPU-EQvCwQw_EXbXJIgW6HWDfrfJlK6S7PdDkQo-ZqHuHICiG4JC56SedRxTRg0-WUFMHNDAaJMyTfKtsO5NjBWzOz-Nb7JINv8aEZPIV2c7gDjWCPW3tik45WG7A7VQEz2j5HG1QuyBYAfjbDc3BBogc5PPI7RNPUGX81zDRJqADpdDUI8TkwnfVr9wNffMRml01C216ic-0Qlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrpEpy89ylGlEspXl2ZVkF_yoPMf9mv-tC5kXTlVZosAP3cFI8tHCjqchhwlFN3rzx9Mbds2_L5WUlBiuaNiCNrRvaFwfaWJB4uEcVhJ-PJhOlOHa_LBfZRRXvAKTs7QUPWW283OEZGssQcHS-DdGc9XvbyQKfiBdIAzB8v76LorqvKBFwm_8gYZofhuUYVbkE35ZTFnhNvQcAk7q22tffVHYOEaw8HWQ-px_unHkSc_cvyY71N1Bd-zka3t8OIScOZysBz3V1FTwcy1dQgaMihNyqIHX4MRmkrJbYIKKFv02Z-hGfTNau8w0dfkaX7Pghau86QOdT-0oi_JCQSvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGUn5v1VkJXbjS8hlflw4WDgDsSQMLxGfyT4zYMKSmSzAXhgIfrxbQGm4bM_XCerCsfcMgf89i-cZpsalpPVc9D_1wC_KeQI0VSTXHLwhYR3ZHeLmpp1eIjSYhonEFU6xKmepB-7Am-lcJfd_51OAAWNeVK_-EBWIPr5IZWHVZKlBcR-qMGTLHsl2udbWbexGZcFq1tgxSEWM2C4lHMSVIlxFN2DOO6C-nQR27eP7mEzyTSmZfLAu2gx1oCEDprpyenujFklMUS6-R5H3huKSjfugmJI2nvmBftwY9GeUOaS851bf9UQjxrYluDMUWpYliXgiA2zmxqNHL3rKKf0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=UqdxEBHUwIbaM9aBbG8IWvgUjiTnmaaA040H1foovjejX-hThb4OG7TnM21CaAiH4-3Z01LBR19stOtDdI2h8JXyGyqMQ53_GIkk5JweKwB11CERumPcwZ_XgSe_j2xcNTqD79IXHXHtG_nxIZtcixvJoyA7Sm9eKUxK6Sf3XEb1tt5Mjx80hbt3KQcmp0ScJIBVxFsVjTAgCnFB7RIG3cx3V76tT9X_CscgSBHjbdQ-coPj6zohQbfNCJ73kAsLz2SOn6qL9KbIJYYPrIpxe9hrekuGhKYHzpeYd5UIFzW1isUzGRCap7HGykK0uQMZEvS8iCRNzzLz5iLIuREoLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=UqdxEBHUwIbaM9aBbG8IWvgUjiTnmaaA040H1foovjejX-hThb4OG7TnM21CaAiH4-3Z01LBR19stOtDdI2h8JXyGyqMQ53_GIkk5JweKwB11CERumPcwZ_XgSe_j2xcNTqD79IXHXHtG_nxIZtcixvJoyA7Sm9eKUxK6Sf3XEb1tt5Mjx80hbt3KQcmp0ScJIBVxFsVjTAgCnFB7RIG3cx3V76tT9X_CscgSBHjbdQ-coPj6zohQbfNCJ73kAsLz2SOn6qL9KbIJYYPrIpxe9hrekuGhKYHzpeYd5UIFzW1isUzGRCap7HGykK0uQMZEvS8iCRNzzLz5iLIuREoLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apwnlEu1_j8HaNH08LTWhG4RI-XGOtzmgQt1rNPAwLjMUk9CnPBxm5YtEo3AAnV2N1mfK9MFMbZxF6pkSJpFtDTkvqWctf-I22ZkS16iazP_xCIkVlY-70Cl_NPcDqsBClqylc1OTDxdKInr4le3ikW8GpARpZH6wXAEw8IAUiPljfYuAx-x52wgLdLmBT6OZBL919mY5E-1C8PRuMYh_Yc-k950djpo0r7oqGbAsROfcF1ezUCfDaOXvuTZ7B0hE_Qh-3BLJBQ1OI9qw9CzJpZm-X8TYEgNC0k1gwYtKmfGGtety0mXNUN3J3UClG5jhwHWMXBQmsCQhH0OjjYwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AP0UV5ViNCAVYCCVUOayEllxnMfWnneAoDMcVNrZ-HpollezI67TLHx7p1yXqjGJoy2SmK5NzVtV4wzbvQ31O71ROTo8op_P74BeDcmXudZWSx_hArlVm3YGxi-psVLcr5tHmVI63LtoGAMZHPARSbynPz5USpMpEdC6nms-mvZIcypROZ0sL3zAgrZDKUgoNw9Dc_r2a8IlRFUG6ksDRFPbVBP5BSHoDHDL5BbTV2_8v8qSyZrgaFaRsEMDoA8AeAYyL1TlryF3Tll4iFLOgT1_DnH-GTUnDSSlE-fGeE7uQG958e8lvqWcNRwgTIh8B0S7HmwW-H7mFoZNzKouiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AP0UV5ViNCAVYCCVUOayEllxnMfWnneAoDMcVNrZ-HpollezI67TLHx7p1yXqjGJoy2SmK5NzVtV4wzbvQ31O71ROTo8op_P74BeDcmXudZWSx_hArlVm3YGxi-psVLcr5tHmVI63LtoGAMZHPARSbynPz5USpMpEdC6nms-mvZIcypROZ0sL3zAgrZDKUgoNw9Dc_r2a8IlRFUG6ksDRFPbVBP5BSHoDHDL5BbTV2_8v8qSyZrgaFaRsEMDoA8AeAYyL1TlryF3Tll4iFLOgT1_DnH-GTUnDSSlE-fGeE7uQG958e8lvqWcNRwgTIh8B0S7HmwW-H7mFoZNzKouiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLMKkZns0LC9yOYztZa2VCyyLnmPTttlaEvCMkDNVxvlxxyiSKMrwGYB8uyuXWMhj3bkoLT1NV26XwwvwGyw_9nGD1ReeMQ_Yehs9bBX4OGtvusEkOVQJ4j6YuypMoXQLd65USn5fDUozGuwAn5MVJ9klgJhc2N5qsSYfLpGmCYLAVVrVlu2_82rQ-Xzl3n7Ex7B9ZpndiyUL_ndIQNZnAS6d3j7WD6cQSKOdisogMyGNI6cy5uzPpEcZ2SXIdqQ0GlRypOmEkw_KlYoiblY2Pz8imJXSP3SrH3SVWrzPhMVNykW-Yr-dkd4prXi36l_N9VctQYdZeAkYQpZGDVnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=KR36KgQ5F8AQYbgAWPsqo2CyMxx1EJOwIrxg_OAO2X4TdaouMNH6_8vb_tZr-pfgmUb2fQJCkf_ucjl4_FcqF3t64R3eKTdSdT7eJsJ2EeV_SQ9VgasO0kqAS0ZFr1q1EyPUEy6nhlp8jP0nmwPnApx05-kypD4kSoLo0_oeJLImduhY2-tio-hB7_Vuyxluo6-KJfGNAPtFUeTeXrJ3qS7oqhjfcER_zwe7EAESFq0bA8aRmDvDgEKZbiGUagOACmFxIjmrOuGNZXuL9sqoyhdU2AhqbP5jLOFkV0uv_ni4pcSfZggvUbgdoha9rDhZYojEovrvSPGu6g-U4VK7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=KR36KgQ5F8AQYbgAWPsqo2CyMxx1EJOwIrxg_OAO2X4TdaouMNH6_8vb_tZr-pfgmUb2fQJCkf_ucjl4_FcqF3t64R3eKTdSdT7eJsJ2EeV_SQ9VgasO0kqAS0ZFr1q1EyPUEy6nhlp8jP0nmwPnApx05-kypD4kSoLo0_oeJLImduhY2-tio-hB7_Vuyxluo6-KJfGNAPtFUeTeXrJ3qS7oqhjfcER_zwe7EAESFq0bA8aRmDvDgEKZbiGUagOACmFxIjmrOuGNZXuL9sqoyhdU2AhqbP5jLOFkV0uv_ni4pcSfZggvUbgdoha9rDhZYojEovrvSPGu6g-U4VK7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=a18lnevPwwJOfnm0CKjUuR-PEnAwv-uZpqD_xiNHlLmP8uhXxvGmX729W7kmurqesnqowLkRVUrc8Jg_jsEX3GhXdZTQc2AQC9p8zqF8mdou2wCxQw69ihTE10Ggzh7AN6nHi7m6U0VlWMEvbVm3OhXEalLzDNAaheyCwHY9z82YRJEDN6MnL6eHUrGZ9BmCUi4six9YcYJaimmssjhCN3a1eHUvXl3uZwgul_5ss-HzcJ8QcR8_Ygt5vfyxpkxtNcZ9wvWIvPLA2YlDBMFDMAwxHcTBpoJ2jyXurjFIbp4MZnNq0_MI7LfhCChupkMsvmhqYH0F3ya2tkBUF6se7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=a18lnevPwwJOfnm0CKjUuR-PEnAwv-uZpqD_xiNHlLmP8uhXxvGmX729W7kmurqesnqowLkRVUrc8Jg_jsEX3GhXdZTQc2AQC9p8zqF8mdou2wCxQw69ihTE10Ggzh7AN6nHi7m6U0VlWMEvbVm3OhXEalLzDNAaheyCwHY9z82YRJEDN6MnL6eHUrGZ9BmCUi4six9YcYJaimmssjhCN3a1eHUvXl3uZwgul_5ss-HzcJ8QcR8_Ygt5vfyxpkxtNcZ9wvWIvPLA2YlDBMFDMAwxHcTBpoJ2jyXurjFIbp4MZnNq0_MI7LfhCChupkMsvmhqYH0F3ya2tkBUF6se7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY-E6oYEkHGAGBzOvLZfriS-THLsLljfcmPoNcw_sZCK5YDUP2htaIdEEtVgFF8vs9fbPIIQulLYfQ_2LBOfW1Q4teJQ0JFJmFpAvwsLotdf4dOwfhZrpY3QngG4H5QLFcyjVedSNaFqT4C7IZqgXYTOb-bHvqPuGJBNKVo3EZB8JvTpu91d2cdAYlXq6H5IpZuYXcv6UHdM9PRgea7uAt8pMgmCKvBTZX9kMMimXHLXJfmi6GJid6JeA915OMdr7UF6iYW-bN7B7Pa8nmmOQpyYcGHMtHTS4yc_hX1dTOqiTLYYgP3gxeAZhBhof8nPlt4KYv5c-Ph5z03s7ZP3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhgtZL5kB_r_xTdW40yC7gtZX-hqJIfJFaUhl4tcAcx_pdytsPoJkYfzlu_wumnSu-c-8wpNQ1kiyXMzs3b8IrabsTV6qse-_31RrQtCGzwY5z2PylO9-c1vcKOR2cCOpwA6BhfQMjsldqF_IrNpr-brHQuHyvRLEr8YmKqeq6IJ103OACYbYv5O7hAZlm2pMpQ30fuvgp49d5NB9L3ECUj-lJsj01Fu8UKUDvRIjxWECbmSz00_EXViOY_5AVuO75UAB-CP74FkOZXzmKOiwR8mA--kadCi0kQnR07K6Rss2ULg-UlVteQ8qm7cuB6SxLmyYslawhRGtdeJnQfek6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhgtZL5kB_r_xTdW40yC7gtZX-hqJIfJFaUhl4tcAcx_pdytsPoJkYfzlu_wumnSu-c-8wpNQ1kiyXMzs3b8IrabsTV6qse-_31RrQtCGzwY5z2PylO9-c1vcKOR2cCOpwA6BhfQMjsldqF_IrNpr-brHQuHyvRLEr8YmKqeq6IJ103OACYbYv5O7hAZlm2pMpQ30fuvgp49d5NB9L3ECUj-lJsj01Fu8UKUDvRIjxWECbmSz00_EXViOY_5AVuO75UAB-CP74FkOZXzmKOiwR8mA--kadCi0kQnR07K6Rss2ULg-UlVteQ8qm7cuB6SxLmyYslawhRGtdeJnQfek6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUUGCgU_E_WnluYVPuuGoazoPbQMj2gWpBU4GWRwoayTxLXu6R9EaLizp-DJkRneTu2D6ZdXBcZUwpU4di1QRkIac6p7NQewFatlVPB0tFj3-motIFP_EsiUL7JpvfP20eNA7qfbo5Kc9ISrdomlenpOXhZyCTC8f5UOKzd5zIwkpzfHTqbZWpaEC_gXOaZnDC4ZbGJaN9EhRN2--51oY0l9c5UTIfrlCj_CNQjRDOLwKUINbu_KZJI23M5vlPjtpm4-mp7zeBelqb_fw_9YoGViEjKkrnjBVOXMB67N_HLiy19URyqrJF9ZdBOAvkuJXRYsuVNQy51fdSl1uQMS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHbLwGUZmzAVldtGtRIfv6Bgj-ywp9_4akcCNcWxRW9rYalBoXSJ603-ju2Ktdqtl8wRZHpTTtyGEuI3iaxVlcMmPHLYLVBvh0aVVVpSUggX6XF3fjserNVixY9Tu6siCDfUFykb07WgiA_NJ1bmMwIvQlWp4E-W03Px04NH4F7pa3F7qADRM5IlQPRV7XfVHxD5cplGclK717OrT-TgQAZao6OOwFVAJ06djTpdOJNxQOYR2nyVevWEdzRLxWm1JgWIxQLpu3XYsFnU5ksELIkvbkYE07n21nwATd0V2cPQHAMdWzcYu5ZNPZM2FQsmXq0SxM5oT5BBfkB7Sgmb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=jDEGDigWN8BESjgCAVPK09vxt7wNYNwOdYNJgtw_i_rU2bVmuteZ69J0QIrcJ-oUNWafU9hJs3nGDyXDPtVEKDrTlVD46g2xjDJqpLpH-ryjGK9w5CoWQ0RLvLHPxTYiZI1vLfJEzJ0ioUZF_ECA8JhbHA2XAoOWcYzRZU_fCgyyTTUDJZ5HLLmatWQBiwyvR_dX_kx9KW0gVFCjwPITPKQ1X4Quqz3GWydYBsu9hGyb-VsyHOSg72cgxfrGOqpea7QZvLJedXVxX93RbbnsMlxDdJ3CmKISBjx7RxYnyAFbapg2xYo7HpBtDkgIuLcJZEUgl2XCXl-1DvTAuP-WxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=jDEGDigWN8BESjgCAVPK09vxt7wNYNwOdYNJgtw_i_rU2bVmuteZ69J0QIrcJ-oUNWafU9hJs3nGDyXDPtVEKDrTlVD46g2xjDJqpLpH-ryjGK9w5CoWQ0RLvLHPxTYiZI1vLfJEzJ0ioUZF_ECA8JhbHA2XAoOWcYzRZU_fCgyyTTUDJZ5HLLmatWQBiwyvR_dX_kx9KW0gVFCjwPITPKQ1X4Quqz3GWydYBsu9hGyb-VsyHOSg72cgxfrGOqpea7QZvLJedXVxX93RbbnsMlxDdJ3CmKISBjx7RxYnyAFbapg2xYo7HpBtDkgIuLcJZEUgl2XCXl-1DvTAuP-WxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=D4lB0mlf_1NPRo7XNPgZsP_5rIXYXyaqMPLqRQkXwykO2M6wMcUCVQaUkUvPPwKTM_f7Rd3ImpfdOpRN9Ssenobn7em2utlEkXS5cEAf6SdBJC7eHGAowJbOaO2nSwdxiAaSP8zzmO08P4_hfumillQhawuO7FRC8r356U6SbF3b9ul8hDcsYEJ_CjVhNK3Q2AbQscDjt4L0fUS52Lnrich6O2xwS8G73MbKHLY9qg2dWGgUzG17i0WQMbiSxxR1WJvBgoXwHCEsCUeuu00MhS07lZNBaDQRVHk5XC07JQ-VLHoF8y1Ktitdd3blcXu381OaIcGLSoSoOKy07c7l7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=D4lB0mlf_1NPRo7XNPgZsP_5rIXYXyaqMPLqRQkXwykO2M6wMcUCVQaUkUvPPwKTM_f7Rd3ImpfdOpRN9Ssenobn7em2utlEkXS5cEAf6SdBJC7eHGAowJbOaO2nSwdxiAaSP8zzmO08P4_hfumillQhawuO7FRC8r356U6SbF3b9ul8hDcsYEJ_CjVhNK3Q2AbQscDjt4L0fUS52Lnrich6O2xwS8G73MbKHLY9qg2dWGgUzG17i0WQMbiSxxR1WJvBgoXwHCEsCUeuu00MhS07lZNBaDQRVHk5XC07JQ-VLHoF8y1Ktitdd3blcXu381OaIcGLSoSoOKy07c7l7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=Ci4cl5V2nGPn8CY-xgwZix_rZCizF2-CWJf5e1nRlOesrkXwAy2bDEhpQDTldgs3N4oEvnfsAbre8k3pqVNLjRqvvHO3iw1cm7aIMuBtJNmM_VGyS8HWPZeaFPJYlsAgEOHiCd8UgKhoTRkMdarB8wAjCF3KMz1Ry9tqxk1yiCQfsQSCWrDRfyyA-JJOI6eYtOpo-7UQ4Qo369bnQ9WkZmdu9Pq0jNB-OtKgiFVxcTxQHlGcd7T6mYUYClWIOOfV5hnmhTKFmc-VXO2LPWIvGcc_7ncOOySSgQywuXiE3JcIGXQpIAeFLFXUNIi6ICuOsdOB-0pXJlL0YZaLm37_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=Ci4cl5V2nGPn8CY-xgwZix_rZCizF2-CWJf5e1nRlOesrkXwAy2bDEhpQDTldgs3N4oEvnfsAbre8k3pqVNLjRqvvHO3iw1cm7aIMuBtJNmM_VGyS8HWPZeaFPJYlsAgEOHiCd8UgKhoTRkMdarB8wAjCF3KMz1Ry9tqxk1yiCQfsQSCWrDRfyyA-JJOI6eYtOpo-7UQ4Qo369bnQ9WkZmdu9Pq0jNB-OtKgiFVxcTxQHlGcd7T6mYUYClWIOOfV5hnmhTKFmc-VXO2LPWIvGcc_7ncOOySSgQywuXiE3JcIGXQpIAeFLFXUNIi6ICuOsdOB-0pXJlL0YZaLm37_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE2zUgT1N4Pg0SLmnZC7wslU_xSuGCrxKzxCxcXTloGFhWnyCBZK2lBFxoGSSUYvpl9vvkRMmkZ7YKVZzUDWweVS3lEk1rW4iiGWSm7v7GPM70d1wkbEpMvm2bZZqj8kh9nJ3ySFHzTePrKfjSJh2_s_mkIAZCBVrYIXJ4K9Jukl5-1Sj1vz3Cei8uAxP1MQMOifCD1PvdSXOKhjMgpP-Bojc3Oh9nokbzKDUeekcElhiDLzwvd62B5DPavbI_jksI--5vPeA0tqe4GiX2wn6pv40_NdRZeHiaCx_GiPG4dcRRQS6c0By1FSNAsO5Hjs5StfF-mWiSNGHtSqcRzGnZAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE2zUgT1N4Pg0SLmnZC7wslU_xSuGCrxKzxCxcXTloGFhWnyCBZK2lBFxoGSSUYvpl9vvkRMmkZ7YKVZzUDWweVS3lEk1rW4iiGWSm7v7GPM70d1wkbEpMvm2bZZqj8kh9nJ3ySFHzTePrKfjSJh2_s_mkIAZCBVrYIXJ4K9Jukl5-1Sj1vz3Cei8uAxP1MQMOifCD1PvdSXOKhjMgpP-Bojc3Oh9nokbzKDUeekcElhiDLzwvd62B5DPavbI_jksI--5vPeA0tqe4GiX2wn6pv40_NdRZeHiaCx_GiPG4dcRRQS6c0By1FSNAsO5Hjs5StfF-mWiSNGHtSqcRzGnZAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=T3S74lomhaLlE0k6xnkc1DQi_667njKKaaQVHsp78fnmQ5SVSi3VVIMjzHN68eZV-SpBlrcZUeBk6_XSP7OcUVFGmQntXoIAPbk2ktLpfvD8-jaxcgSX1FRvHQTUdM3dfnH3x7VH3z-2zfN0E2hZZYfXWhDOMX4hjONv-s6qv2PdoS2xUYmpZwP1IuNF1q4tyshIIL4JlMh6NEvOSHufAsGCpugZos00u0hMoaKtcD-iMjbjzxMJdcEZVC_Bgwq2F6006wotzLopCk5OBjQ4XLsnQ6uU-fTTfA8D6mPQEFPPgx5iUnwCRdeOR_LUARVbgCbjK3g4SvpmyWgz6opGmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=T3S74lomhaLlE0k6xnkc1DQi_667njKKaaQVHsp78fnmQ5SVSi3VVIMjzHN68eZV-SpBlrcZUeBk6_XSP7OcUVFGmQntXoIAPbk2ktLpfvD8-jaxcgSX1FRvHQTUdM3dfnH3x7VH3z-2zfN0E2hZZYfXWhDOMX4hjONv-s6qv2PdoS2xUYmpZwP1IuNF1q4tyshIIL4JlMh6NEvOSHufAsGCpugZos00u0hMoaKtcD-iMjbjzxMJdcEZVC_Bgwq2F6006wotzLopCk5OBjQ4XLsnQ6uU-fTTfA8D6mPQEFPPgx5iUnwCRdeOR_LUARVbgCbjK3g4SvpmyWgz6opGmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=KTyefsxAhpkiiI8g2JqVWjR1V0pEA27i-KUVBUuPoxDoego-Sv1YRRg6KmrCNnR5LPV5my12J7u7cbe2XjTCteYBAiQfM99WTl3Ep-e-VkXaSyWRVOll2o7c4p_OdRpXK62IjtCXmEpgqosUQG9ByrKckU-trjpX73ILFPdWLppiVDEAavbtPX1xDFyNeHBxjyDBd852aL7zT7zAsDqaIlWIkRhIiDX4AdIEY84GwrMPmJzL8AePz4BEBA4epNECmhyPOm-4tDx2hzGccjBQ3fMQqzcmkcUpcBis3B9uq3hc06cgJejrCGoPBYiLhH1TXj7blqXJbHvLJFP2fn5Jug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=KTyefsxAhpkiiI8g2JqVWjR1V0pEA27i-KUVBUuPoxDoego-Sv1YRRg6KmrCNnR5LPV5my12J7u7cbe2XjTCteYBAiQfM99WTl3Ep-e-VkXaSyWRVOll2o7c4p_OdRpXK62IjtCXmEpgqosUQG9ByrKckU-trjpX73ILFPdWLppiVDEAavbtPX1xDFyNeHBxjyDBd852aL7zT7zAsDqaIlWIkRhIiDX4AdIEY84GwrMPmJzL8AePz4BEBA4epNECmhyPOm-4tDx2hzGccjBQ3fMQqzcmkcUpcBis3B9uq3hc06cgJejrCGoPBYiLhH1TXj7blqXJbHvLJFP2fn5Jug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igNCzddCbbC87LFX9W2pX8NIuxE_e1_JWyJ6GlvWUUvggEL5bcz38eMnJmYgt5LJaWunDv6EZ-StggQuVzWkgnLHA_RLQpzE_iKuyYWTSyse7gyYbL1kOLv9E6gJOZ-Kz1_rhaKhrSSRvBgmx4in25WatwFtYOherPL4hLIW8iukZ5L0OTinjTZTMwdbBy8dqtE1Mzjig1C7qGkQqftjeeHEllv397P0GjjgUnB-1gtusDVffZcqAKpkTmFkeGPkIv0J1Iea1A8AIbTVpgwS0_Mt2HzRqTDYBO5AYHt3j4jgwtf54lQ-hYllnd_k7KLvzLRgv384RBW5yM0ihZCljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uihqoFK1QAdHeKqLNw8KFOcUmQ--bY3-h_DbkpKsjqNnlWVjEBi4h7VnRIeFNrC74DCx1peBeAMyFY-S0gJuJqkdhS1cSWW8uvrfKcMjOjwcEZMS0e-llh4EclY9n2hdULyBRudkrHwo61MCzUn8bnHyD5lBUI23J3Scg6fFwaVn-CpVddY_DxeCOUkxMZEf1h3Xsqjt8RjHqd-X-haW8VEW--UzggKLo-mFbQgpctpgqotj-9bVJcUR82N_96AiFb2eemr-Z6hcL55Mhj3OPu25Iv4DQel4QNvwOMzlM8U5wotHqDKx0nlcLzFSFokcrC37o6jQUO8rm1zH45gt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=F1KzSEEWXmXjMmRsF_c6jd-vWtXmgA4lOBEEnNG78NQWXttdPPLdZVfxrHn6tP-WGsmlUK0ZNJJqYjMltU4Kur2h8f7llcyxEcLY4HIbC9-svIvLt1FDbIuurq8DB4Tjh_5C6WolTZOrJFMhsN1YY5Ouid-MNZrDwTZQT4gskKLOBa-GPqbCRPOpiK-LU68Rq1sm9QLTKfKl22eHhr50UdqFZeobB8nc3WDV8mUukLiMMBRN7hbiaZBdQQHnZ4CiN7k8esGizgtUBesP2E-ADHrziqOG4I_RhyssOQP6FIWbBVNbB0TFJ-3o47Cg-p9hVd00NJ34rm4b6u_eU1qWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=F1KzSEEWXmXjMmRsF_c6jd-vWtXmgA4lOBEEnNG78NQWXttdPPLdZVfxrHn6tP-WGsmlUK0ZNJJqYjMltU4Kur2h8f7llcyxEcLY4HIbC9-svIvLt1FDbIuurq8DB4Tjh_5C6WolTZOrJFMhsN1YY5Ouid-MNZrDwTZQT4gskKLOBa-GPqbCRPOpiK-LU68Rq1sm9QLTKfKl22eHhr50UdqFZeobB8nc3WDV8mUukLiMMBRN7hbiaZBdQQHnZ4CiN7k8esGizgtUBesP2E-ADHrziqOG4I_RhyssOQP6FIWbBVNbB0TFJ-3o47Cg-p9hVd00NJ34rm4b6u_eU1qWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=rG_kDyOYJIDP9s7Tl_s2yrlhX1UVgnI3XhfzLDinK3OwrK8slpn_IeNGP8X_8fgEjJHXzt2ottxojoll4maMvyM0K_KZ3U_FrbKpU97PSOi1lel1aLodziS28gRFtRMl21I6s9BKn516f3bjQjEcsO6uEvdt0NmtStJ1yavU5CH3tNmDJRIE_H5ocXjHy7AKJmzcHg_HrNanqmMnH0szToN1s6r_mRShH3i_zSGHoA5CJ2s0uw2DGphXFIqfKh3FFuAALHzArqiqx97fHB4Gdrv1T5aAckezXA1f8c6LJcqKyWrPvd6u1xVQj9HMNSnXx0VuElBrNOQs6FOWNI07RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=rG_kDyOYJIDP9s7Tl_s2yrlhX1UVgnI3XhfzLDinK3OwrK8slpn_IeNGP8X_8fgEjJHXzt2ottxojoll4maMvyM0K_KZ3U_FrbKpU97PSOi1lel1aLodziS28gRFtRMl21I6s9BKn516f3bjQjEcsO6uEvdt0NmtStJ1yavU5CH3tNmDJRIE_H5ocXjHy7AKJmzcHg_HrNanqmMnH0szToN1s6r_mRShH3i_zSGHoA5CJ2s0uw2DGphXFIqfKh3FFuAALHzArqiqx97fHB4Gdrv1T5aAckezXA1f8c6LJcqKyWrPvd6u1xVQj9HMNSnXx0VuElBrNOQs6FOWNI07RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ijsDwCbz7yGnYSA2QvHGZJGkPh7Wh5yVyeYRMw8d7M-eO46qlhj3I2U6c1N4ju2EwTRdoTtylTlML4vA1ts-NE1ntSsMD6gxPZvtOJbNp_CsAfvNYwTbG9kNwDy9TxTlfnFPnopbh9-ADinDO-66QxlyMtiI7o_Z3GeAeA25JBOXCuI4Y1_7Y7uakd4wNqwKTjZdxmOhd4UrL7Z_918_3FRHr-i9RxfuEqaBJjZX5XbkgpmageXhm35LXmFyoeP4SKr61AvyjmCwGLv6kTSlp-bDM-5koLDGm6Varzrm15vprRxtmn6M5BUZDjFh0S3sgk1GC-OhwycrrTkPm-bqUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ijsDwCbz7yGnYSA2QvHGZJGkPh7Wh5yVyeYRMw8d7M-eO46qlhj3I2U6c1N4ju2EwTRdoTtylTlML4vA1ts-NE1ntSsMD6gxPZvtOJbNp_CsAfvNYwTbG9kNwDy9TxTlfnFPnopbh9-ADinDO-66QxlyMtiI7o_Z3GeAeA25JBOXCuI4Y1_7Y7uakd4wNqwKTjZdxmOhd4UrL7Z_918_3FRHr-i9RxfuEqaBJjZX5XbkgpmageXhm35LXmFyoeP4SKr61AvyjmCwGLv6kTSlp-bDM-5koLDGm6Varzrm15vprRxtmn6M5BUZDjFh0S3sgk1GC-OhwycrrTkPm-bqUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=kPdCY6fLfpMd2RA_hv2hdtwCoVKqmXR6vrcKgzHnc0aETHE5Mycie7VeEFE_9DhVQF11y9cWGw6aBIOrmuC846zcQ4CHxTvsC3uqdclty3a6PvtgexV_v0UGA-1DXdVLYEHC6Y-wIQtPTalYTp9q8jUkoUR4MAPVzwH8OhIr5WrwSs1XIz4dBIyDZGWOqLq82GLiA3F1XThkoaafdzvFmz-4l_W1AzdvwQ9bzM3LYCXQw8pe7SxceM9yy2fnlWgl1r56WDfeoNpK-hPn8-6LDsEL7C80I5EtjzBiaH9xiPHvZHjIKTirdlv2AVjJ_RLqD6yUCwRQy_QKpQgWWTCP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=kPdCY6fLfpMd2RA_hv2hdtwCoVKqmXR6vrcKgzHnc0aETHE5Mycie7VeEFE_9DhVQF11y9cWGw6aBIOrmuC846zcQ4CHxTvsC3uqdclty3a6PvtgexV_v0UGA-1DXdVLYEHC6Y-wIQtPTalYTp9q8jUkoUR4MAPVzwH8OhIr5WrwSs1XIz4dBIyDZGWOqLq82GLiA3F1XThkoaafdzvFmz-4l_W1AzdvwQ9bzM3LYCXQw8pe7SxceM9yy2fnlWgl1r56WDfeoNpK-hPn8-6LDsEL7C80I5EtjzBiaH9xiPHvZHjIKTirdlv2AVjJ_RLqD6yUCwRQy_QKpQgWWTCP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=EOjBXYZxavokXLeUuQJ2FzJmi1JpJQjFm653WBnAyNys9bjeehEXSh6yeVGVkGBiaLpmexLHbBsfqYwP3_3mOkrkpp8i9ActBW1TycsN1sAtlw5B5C9_BySWVTo5LgCeCi9j2lcRKpBNeKc5VRzZvIJci5Dm0Qoodt7zgkV2Wm1dbX1F6_KT73jO4amGBUgGNFDpgZt32VaYf6SJFHuM8IjBcAHR3CGC6hutzgy8TJ44i3C3DUnHm5Che1wslHPo0bZqncfnyN8Q4PKUcmg60R50WsiY3wpzp6dEMLIyZ5fRQMyyS2h75lM1HUqmaBUfd2WlJ69TmX8yjZOOBfeB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=EOjBXYZxavokXLeUuQJ2FzJmi1JpJQjFm653WBnAyNys9bjeehEXSh6yeVGVkGBiaLpmexLHbBsfqYwP3_3mOkrkpp8i9ActBW1TycsN1sAtlw5B5C9_BySWVTo5LgCeCi9j2lcRKpBNeKc5VRzZvIJci5Dm0Qoodt7zgkV2Wm1dbX1F6_KT73jO4amGBUgGNFDpgZt32VaYf6SJFHuM8IjBcAHR3CGC6hutzgy8TJ44i3C3DUnHm5Che1wslHPo0bZqncfnyN8Q4PKUcmg60R50WsiY3wpzp6dEMLIyZ5fRQMyyS2h75lM1HUqmaBUfd2WlJ69TmX8yjZOOBfeB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A6BV206f1FX0i4cE1BgJ_oL0Se722RBNUCPxWhP9jWOKqQltbgwjJUmMwfn5V9rewuP1V2PgffmA-Ei6PJhuoqUJFp4swIBiSXAF42KU6NYjXmJLEWVxOjO2ZoeZQNF3WbHrtvgeYk_6C_fEaOAtnSWF7jpOLAwIJOHTtYhay5JYcVp2JmqrNL39SQiGXjTga9Of_ZdhKK5uw9Uun3YHD_rt5c0ljMcURcWwpQ0evYL_cqrIN57ftfAHH0YdUGP_UQdEoUJpMQM33q6gbMvJFF1fDMfkcHnZKPu2s9Cf680OJ5U2uvVFIsjvhubkw9ocFThQNuMQ04WC0hqTsWCK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=Y-EO1NbSo9noFz84jm9IV5OMqjPddjx4mZY-Zddd_p7iLawm_pbNsGaEOtNSi5fU3AGiXaZFpvIkYdfgKyTDAVbLIgYqkVdI9NLGqTryl-Tz-cNPX7CSTJsLpD7TAEbDoyMX1clpzT4XxQ86P13kivNUo0W7SLCEM5Bq_QdGk9nREjhTlGGQ2j_2DbSwyMnxAHuM7mJ18Z-rnKrCWWYW9h9rgEnZUjn0Tp3nU8r3VsG8VrVNnC7Oxl9MFiw5n3j3mHOXah8xek6Z2oECIrK8wwySvg-ZIycICwAJ_phI9w-jCJqeNoySbItndhF16Vg4Anm3wPqSyQPyIzcjZFOUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=Y-EO1NbSo9noFz84jm9IV5OMqjPddjx4mZY-Zddd_p7iLawm_pbNsGaEOtNSi5fU3AGiXaZFpvIkYdfgKyTDAVbLIgYqkVdI9NLGqTryl-Tz-cNPX7CSTJsLpD7TAEbDoyMX1clpzT4XxQ86P13kivNUo0W7SLCEM5Bq_QdGk9nREjhTlGGQ2j_2DbSwyMnxAHuM7mJ18Z-rnKrCWWYW9h9rgEnZUjn0Tp3nU8r3VsG8VrVNnC7Oxl9MFiw5n3j3mHOXah8xek6Z2oECIrK8wwySvg-ZIycICwAJ_phI9w-jCJqeNoySbItndhF16Vg4Anm3wPqSyQPyIzcjZFOUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=Namj2lUm_Gd14hsLRsQyn6C-xwL95OoKnoG98xt_kqcYY-kEAO53d_tzg92qDcsFL9_hW3UQmQrdijr1wSSDj9FofmleXGSrFIS-Vk7fZi8s_3bp1P8hKbkSSoze7dv8VNLsGfXWUw00IuIRFgJtbXd6eG-3gCV6W-guxTUEclvA0E9cdHNteQ3f2gvk52oLZwCxpP42ZvRhjM_qWHQJ6m5jiuzInCO065rKX7yXgn9KDcydCA_uttQk0jB3dA2Ppgc5JMkmRDJjRic1cWk25px3rw-F0NJWSDlA_BJ3OzbHYwRqNLX9CFwsw3JGwZ2dJtrerAZ3_0rGsY1In4zyCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=Namj2lUm_Gd14hsLRsQyn6C-xwL95OoKnoG98xt_kqcYY-kEAO53d_tzg92qDcsFL9_hW3UQmQrdijr1wSSDj9FofmleXGSrFIS-Vk7fZi8s_3bp1P8hKbkSSoze7dv8VNLsGfXWUw00IuIRFgJtbXd6eG-3gCV6W-guxTUEclvA0E9cdHNteQ3f2gvk52oLZwCxpP42ZvRhjM_qWHQJ6m5jiuzInCO065rKX7yXgn9KDcydCA_uttQk0jB3dA2Ppgc5JMkmRDJjRic1cWk25px3rw-F0NJWSDlA_BJ3OzbHYwRqNLX9CFwsw3JGwZ2dJtrerAZ3_0rGsY1In4zyCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E70F3HiwGHjcGD13ETzMW7drOsFi9Nx2WCBVv4fMMv3rzSlwpumE1MejmugGRobYXwzJjUyS9dhI4Rt1bH7_ODUIxTIJQoE-Sf0J_hHMV6OV5ifMUm3ewiuiDwDWcBOwhLL2925cKJsJj6DUwmq_XCcFFStrNpgKpdFcZGAzFzMVGE22-Fd951cD65a42p8cmtUXMMVsxW5xHEvEG6kSVAypUadzB8Esp0oS7GTuny_Vcv5tAmcMHXoAo014Q7M5GxlDr_vENu0lORxM3-8W-1keA-TLTvXRJzuHHyn9rizPY6Zb73C-7rMAWN9ZHFvqoVzpDWGrNpYFUYmvytvvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=N945pucnYJTLYKLzEMs8CN01AZ_EmBfGn2FUYUxi1q9FDuntWrLoaPaAulTRZYbbBOc48S2NUlsH3W0JXJ4z8vDG8xYPtCMXiZHvd0ojGiI2h0091mIVjr9oUTd0F1dBeqC9KT0qZZ-d76ljZ2tSWoEEDAxfCiERnXO3XNbb2rCue-630upr2YgSqhduJWFGlMe1V3ThEldZpUDJW-Xua-rluNJFEeNwYcfd2KGh47kTd_6TSTy2V1rz5Yg2o1zFUxd1Kzbz-FjeOZ5xc8ml1DxUc3PS4FZ1jOwNViENRf3FHQAsdkqKmEPlvJLRySqLlMqAxta2hYFUB4NU8bGV-KhaFfKQ4s8ta2u6J6k2_TlA0V7Zdv6nXxoU0YKTg90Y20REjSiRrtgWlxnWNqU8UsmFaUUJg9tC1kNQLaGvFjdeNI6ZtgJYXpdEni-PTq9iUzLhe3-XlHUfOrTEnlX1ENFrDhA6YjfWY2nHzjmOxWopE9W-8B3HsBFUYxSYazmp3MHnOF1duKRXxPNutGO1vW-SCQ8JCrMakYPHsQh1Ep5tpNDYTJ_0MeB2U_fp6fQSM2UKFxCHwdc0352ExrwQ90yjF039LXN-9wsci2PyOIsV14q1r99s7jsFwm8AGj3x7Tvomf8qj-10YIQf2Zcqk0Oksd9RytSRazfc3wc-Yys" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=N945pucnYJTLYKLzEMs8CN01AZ_EmBfGn2FUYUxi1q9FDuntWrLoaPaAulTRZYbbBOc48S2NUlsH3W0JXJ4z8vDG8xYPtCMXiZHvd0ojGiI2h0091mIVjr9oUTd0F1dBeqC9KT0qZZ-d76ljZ2tSWoEEDAxfCiERnXO3XNbb2rCue-630upr2YgSqhduJWFGlMe1V3ThEldZpUDJW-Xua-rluNJFEeNwYcfd2KGh47kTd_6TSTy2V1rz5Yg2o1zFUxd1Kzbz-FjeOZ5xc8ml1DxUc3PS4FZ1jOwNViENRf3FHQAsdkqKmEPlvJLRySqLlMqAxta2hYFUB4NU8bGV-KhaFfKQ4s8ta2u6J6k2_TlA0V7Zdv6nXxoU0YKTg90Y20REjSiRrtgWlxnWNqU8UsmFaUUJg9tC1kNQLaGvFjdeNI6ZtgJYXpdEni-PTq9iUzLhe3-XlHUfOrTEnlX1ENFrDhA6YjfWY2nHzjmOxWopE9W-8B3HsBFUYxSYazmp3MHnOF1duKRXxPNutGO1vW-SCQ8JCrMakYPHsQh1Ep5tpNDYTJ_0MeB2U_fp6fQSM2UKFxCHwdc0352ExrwQ90yjF039LXN-9wsci2PyOIsV14q1r99s7jsFwm8AGj3x7Tvomf8qj-10YIQf2Zcqk0Oksd9RytSRazfc3wc-Yys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=LdmcufD_94YO4UFpEjuk78FR4ZlgssJND_ziJ6bJTQkosWm8Rhr0i-vaIQiENNgiCL9HMZDMhQM61hWp-levskrxGsSYqbRkYbcnsGRrBpYK1wX6CttdJI7I0r9W3NC_10TSsb6Gy6MdgBY6jnlAvkuEB3KUIVovo-jXuTpeEq1cNNoGp0STyBcDspxXJwbHklcMLA2M-OuwHlKbOyrCRoKxQOTnAr2Xt0Pop1cHmA5wBZ-j0xJCgSt6H8v0JPIPV8IOPZFnaTbLs5xlcr6V6d8rg5R2QuOAbGczY-3z9s9yHoBL1j5TaukIZ1iKrFqMmaTE2CakbXluynnXZC3nxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=LdmcufD_94YO4UFpEjuk78FR4ZlgssJND_ziJ6bJTQkosWm8Rhr0i-vaIQiENNgiCL9HMZDMhQM61hWp-levskrxGsSYqbRkYbcnsGRrBpYK1wX6CttdJI7I0r9W3NC_10TSsb6Gy6MdgBY6jnlAvkuEB3KUIVovo-jXuTpeEq1cNNoGp0STyBcDspxXJwbHklcMLA2M-OuwHlKbOyrCRoKxQOTnAr2Xt0Pop1cHmA5wBZ-j0xJCgSt6H8v0JPIPV8IOPZFnaTbLs5xlcr6V6d8rg5R2QuOAbGczY-3z9s9yHoBL1j5TaukIZ1iKrFqMmaTE2CakbXluynnXZC3nxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTYdQ2zo4bWbrWBEaRya4LAuxJ7Av3PkhMROnJPXWiFamQVz0mUszpXUsYKrkhgtoo8HnUj3JW8Fj9m3rIOnXfMKCdnkgrYrW-zw1mgp3k7p6HXSqYcVGZbBCJRAJSgQPcc6ruF8Ktrvlj5TlGTFT-B0ogq0RmIRVGjhE2qnCETV0Oyg_bG3GfUt_RgK6BvLt4zoxIt5jEBqU4dvsG5QQJTAqeLV_Bk52DsP4_KT8jV_TeRYzsImcZMA04fqWXtsSH1S-93YrWUTk15FPcYP-eFzzR7wx5Xg6t5Xe5FbzgYcllxCrnvhC35GvdS5ucx70D6f3pJDb8szztmaWnykPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv_DA5WhginfnKSTZdR1R8n7FbgDHx7W92BefY-uudcv1c4rW32tVkTAg1UyOZCEmQc9zcFXB_3D1Qn0IY4OuEgljfzFVF1lvEcPoWOS4Yd4DSprN_L6OlNJ3fqtsPA6EkqrXXyqHXYay3RUjdTy8vC6krgcXgWj4h0UVFgtQimIz-_evsEYiVXJkFgboyMqTYvn7cxMupXXGGkIbR7GXTMnJV21xGAa4Y-An7NCenkyw4DfSHGa9O1bMtwkcZCTLfnjBdKmCs83LiR32yveGpD11PxPrGm7GLoxxZVqBqRFnyLR2-jNAumtS_6kD-9DnePycIHE2ho-MvgSnxvdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=Flk_1gQ_Qs6xkMHR7k6FE08F_aOjBT1D-Z3BBPaQy5zhtqJGJ7stkmc_WM3cW73VxhCwIwKzA921n5D_M2U5tncpdZvESvAsg_9x3xZlePAZ1lt_aqESHEfxdXHD1BEDr56mM_zJWKAt4wSdKmrcEVVQTBhDACcZGb1tk3iK1LVe1OnSODJDfsKB3WIvsXAjdI7c8QiQp0C2cmKB6MT9S8Po_54SPGjIzCGPAy5mmmlDNZFqpmdrVJ-Ickfbol7r8oD78khIhHOTsl9iMU4eHJR5lKLz6Ce9YkWhZHADhWHt2G5eB-Ylg60RgAmcTNFY69945vI29S-zaGzCm3qwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=Flk_1gQ_Qs6xkMHR7k6FE08F_aOjBT1D-Z3BBPaQy5zhtqJGJ7stkmc_WM3cW73VxhCwIwKzA921n5D_M2U5tncpdZvESvAsg_9x3xZlePAZ1lt_aqESHEfxdXHD1BEDr56mM_zJWKAt4wSdKmrcEVVQTBhDACcZGb1tk3iK1LVe1OnSODJDfsKB3WIvsXAjdI7c8QiQp0C2cmKB6MT9S8Po_54SPGjIzCGPAy5mmmlDNZFqpmdrVJ-Ickfbol7r8oD78khIhHOTsl9iMU4eHJR5lKLz6Ce9YkWhZHADhWHt2G5eB-Ylg60RgAmcTNFY69945vI29S-zaGzCm3qwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=QaeQrPREbiUYo43B9Zypq0xy5i-Ad67nC9gaE6xRqjCYDSkue-L2dGehoJGpUrFzfBVMPZQyZLjoUKWdvdJVAIekzcXbGhp-blzwlrtytB-ie3k-a1UUe16VXOFImsiPudZrmYGLXMkBRRZ1HItzTDRYWNWPgTdP_OREVzfJKS4gqHwspnSDHSKvdEDiUgavJqoPiF_WwkxyxD7jMD3nJ-HossisjzxdZ0_Na2g7CZ-ImzRKrw2gdr4F2WlpTJJH6tUhgWWGfZJRwihiUkKk763iHK0ZXAgErgEV8BlW6Uo2fzdPRhwZcWQDZ_yUn9KcbuawYOxBZSDhwe6nlnI7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=QaeQrPREbiUYo43B9Zypq0xy5i-Ad67nC9gaE6xRqjCYDSkue-L2dGehoJGpUrFzfBVMPZQyZLjoUKWdvdJVAIekzcXbGhp-blzwlrtytB-ie3k-a1UUe16VXOFImsiPudZrmYGLXMkBRRZ1HItzTDRYWNWPgTdP_OREVzfJKS4gqHwspnSDHSKvdEDiUgavJqoPiF_WwkxyxD7jMD3nJ-HossisjzxdZ0_Na2g7CZ-ImzRKrw2gdr4F2WlpTJJH6tUhgWWGfZJRwihiUkKk763iHK0ZXAgErgEV8BlW6Uo2fzdPRhwZcWQDZ_yUn9KcbuawYOxBZSDhwe6nlnI7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=DGWHPeFElHAxEPu-3wC6L0il3FQP62QeTtp2wRK4tyaB7LZbTAr_VDB7ndkvZFm9Ewjk2Zrap8mYZRQu054wWAEJOj_6P5v2qyjjTqVqmDO18xPRgEj9j3NKmmCv5YYOm6Cqu337HBEn5GnvglQk2bQl4mrlSzrF4bqjje30K5MF4G-CyG3k_Q5P8AlVrw3CfI-GhRH2UmFEk3mGA55AfTMhcfhH2roGnKL7D5JFECcXVoqO9Y7HI-zIFTYE35vmUfaU07A29kQx7sbwAjTUvLWg-t5NDVEV7Byg6ppr_EpH_ocn2pMqZp8hjTL037m3cQviORay6bK8jcXxxuMh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=DGWHPeFElHAxEPu-3wC6L0il3FQP62QeTtp2wRK4tyaB7LZbTAr_VDB7ndkvZFm9Ewjk2Zrap8mYZRQu054wWAEJOj_6P5v2qyjjTqVqmDO18xPRgEj9j3NKmmCv5YYOm6Cqu337HBEn5GnvglQk2bQl4mrlSzrF4bqjje30K5MF4G-CyG3k_Q5P8AlVrw3CfI-GhRH2UmFEk3mGA55AfTMhcfhH2roGnKL7D5JFECcXVoqO9Y7HI-zIFTYE35vmUfaU07A29kQx7sbwAjTUvLWg-t5NDVEV7Byg6ppr_EpH_ocn2pMqZp8hjTL037m3cQviORay6bK8jcXxxuMh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrRAk_MYvKnEVx-HC1h4ZyTQPA_RWWBihJeCOJra6fDNHJjp5Don5ZTjJ9kRka55HNzMIE5QvWq9Q3klLwW0R-0JlNqWKsbTCoJz8QGcMG07x_j0F4-aaTH9ClzWN-xllHISNlZTcayUSsV0WnYaioJsjTMxVKp3KszLAaDaIXXKjmKUW28fC1F5uydgIfXCFX-WC5_MwzGv8leymgBLsh9Yl8YL4mB7qRECE1Ah32MwyiRJ25zo5ww9R_RWjoGrrR34j6kUt7Edp04qP7vduf79U3Tz4pA08mD5OCfBO6GasNVebpDWGR6tLf1FPsuwzVNy4dYtC6b4cciFUkRTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=Nvyh1_pkv3RxM8cBCiRCi-2opjY9bGys6UDd_VDXnetv09mS2Rr1u4yKy-ZmbjyGuY8Z2HrRvHmpdOKQBDfLvV3itIxjlyZLz4dOS5WDWDHGgflQyeEo1Z5pGX4cdP2FXrSpVgXxvCHrMZ0R9VhjbZOebKFrTY_IRF3eAPWB1oTL1kB7TcPHSKeAMCir3W5YCxgAE-RlKvA6sqfW_vU4yzmDSuVaFqMPLZdqE8tNM0Ufp7Ag4fe6mKGpS-YZqebLLK0ZwRnSPXlRdDg3_xi4bJdq_IRe2S5kvPcNy1-8x4s22MYxzE331f3OKW7to9fQ_BVqzaHymHYfXAVojf_J5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=Nvyh1_pkv3RxM8cBCiRCi-2opjY9bGys6UDd_VDXnetv09mS2Rr1u4yKy-ZmbjyGuY8Z2HrRvHmpdOKQBDfLvV3itIxjlyZLz4dOS5WDWDHGgflQyeEo1Z5pGX4cdP2FXrSpVgXxvCHrMZ0R9VhjbZOebKFrTY_IRF3eAPWB1oTL1kB7TcPHSKeAMCir3W5YCxgAE-RlKvA6sqfW_vU4yzmDSuVaFqMPLZdqE8tNM0Ufp7Ag4fe6mKGpS-YZqebLLK0ZwRnSPXlRdDg3_xi4bJdq_IRe2S5kvPcNy1-8x4s22MYxzE331f3OKW7to9fQ_BVqzaHymHYfXAVojf_J5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=YFl6PLAWDKboSDzLaw3HBcWXI2LdsmqKQM0L3U7VJXCTb0rRKrrndxKzzN7fKfgc4EjlUovcqtcI6StMRMje3VkQCxCxa7uMQ69OBFRCUA715fZIXiyC8JEvyXKTchENa73h19oejqqIhr6wcQC1poW2OG2apAjxjTxGYUclx1yiR8C3qO1bAe_uCe1whZAvdqnO24JfPJ9s8iBxAnx5fpi9XA12TOC-Ua6FrUrwTWJ1pF6mwLnIlWV6QeURL7OupYIGnM6k-4En80tx_eP6UJ20qadVdgilmfnX_x1MrbMpDnOqpQ9DVp9o2V4nREM4bJTV_oCkonGrGc4BrH-y1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=YFl6PLAWDKboSDzLaw3HBcWXI2LdsmqKQM0L3U7VJXCTb0rRKrrndxKzzN7fKfgc4EjlUovcqtcI6StMRMje3VkQCxCxa7uMQ69OBFRCUA715fZIXiyC8JEvyXKTchENa73h19oejqqIhr6wcQC1poW2OG2apAjxjTxGYUclx1yiR8C3qO1bAe_uCe1whZAvdqnO24JfPJ9s8iBxAnx5fpi9XA12TOC-Ua6FrUrwTWJ1pF6mwLnIlWV6QeURL7OupYIGnM6k-4En80tx_eP6UJ20qadVdgilmfnX_x1MrbMpDnOqpQ9DVp9o2V4nREM4bJTV_oCkonGrGc4BrH-y1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=O5QstOZkp1YVj7aXCmVpokJFg_4yowBWh3L5t0Vv_MbVswOD4lFmTc672eJsTaYAI84TsnAkVbIhV84AT2aiG7eRH9hG-5IyY_iWGPGQRpJQ8-Xz6mJzhaQdB5Jd52mufJCDMFvIN9MwSiUGFDuep60tsPPUZsISoOSuPIlPNtdL8dP97DcvxwNHbkxlz6N3WdxyDx2ztpJFJsc3GmKA9kqBhjviMeLG_0actxp02nikMGpMnwt4StTMOz3xy5qOeHx4xVTh4SF-HR8h_WsIO8W4s4HPeo88OotB84eBiPfy2LWVr3MretBZR8czutHHltRluY2kMESxJmdzikRw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=O5QstOZkp1YVj7aXCmVpokJFg_4yowBWh3L5t0Vv_MbVswOD4lFmTc672eJsTaYAI84TsnAkVbIhV84AT2aiG7eRH9hG-5IyY_iWGPGQRpJQ8-Xz6mJzhaQdB5Jd52mufJCDMFvIN9MwSiUGFDuep60tsPPUZsISoOSuPIlPNtdL8dP97DcvxwNHbkxlz6N3WdxyDx2ztpJFJsc3GmKA9kqBhjviMeLG_0actxp02nikMGpMnwt4StTMOz3xy5qOeHx4xVTh4SF-HR8h_WsIO8W4s4HPeo88OotB84eBiPfy2LWVr3MretBZR8czutHHltRluY2kMESxJmdzikRw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q24VaWVW1Xh1hx_wQG8BWIaVqz7Htb02llXbDqEzC4Fzy__vq9Lspk1czQf0dVVHdyXt92GQNwfFwuAiCslpzkFHvjdVFhiizakTrqTZbQYeRT0mtc-gp393sFa2_ZKCr6aP480N-G8XHthoB7QCN9sf4UyxUUKLqVrMW4xvuM58c-SNf99xr9g9TBuac-1tUdRmfL2xilZf1PNRnLCojd5KvqJ62ojEOwOT6NxnEjNm5zrbil6pLZvBOSB0emPcnwhqkqVJ5o2biH_GzcAAmWHfPLB01KUQwsxHKv0UIcuy_pBw2V7vpM-1aka47BbiC9T7yUBKViD4e1wG0-M8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCnUavfW4D0Q4SdYRONKqwbOW99S-aCLgkNWiptuatDAUYFc-JaItUOiJtknH2Cf6Wi-yFVES3YyKAVt65nhTi4nBzC5PZ4hSknvGfJy-yV0FVTh9PRFUStTIeIsNya8yRPfzicbJ1QIASr9AXexSVxBONArFr0OtfTeTZUhl63TfwDKWaZaKkYLis2ln0f68O-Ym4cOr2Vox2NTx6AdUFOiq23e6Ryi-RWo6W1VQ-c1rNQqRaiq9VO88MAEx7KyhrP490ZUKmth8LbtDyjfr8gKfAecw3ElnfeIappT0vXTxeivN06Dx89mKKM-_P8WSwOhFI5yOYnzcTxt0W2I-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7PhkLggMq1egVl6RnzU-frggUk2IkkFt6xm1jWMFgLAjgLf7ZdqyzJfiJYWMRY8kngX90ikbsotTs23OLvuXsdn-bXNJF6eJDZ8MpWBFIX1I_d5fqM5ou7k83VTvy_b3gjN8tmlXGQFepe6-VvGzVGDPXVb9hf2BDXucp0vov8-Uflhwpkjx5rt_p8Q6fAHBq19w_AjN71hFyT2E5t0uWPloEpDrPFbx2kjcBAqIel64d9kvZzKOF0e5LpbaGx6EEeTy3mccsDw3bYnl8JA96fxT24mDj7Bc1lYXLUHD7PwN8BSndEzX0pymOeD7XJyar3qYrY_2EHuYYJIO6u0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVFmwXRnD7l31NW-W_4hPtH60zyFXHqik3d7bSFyJdb3399Zzq0FpxD-PGWuByjz83C-9yN53F2z5_AX5T1MsEYILWmck_dV43_Qx_ERkFlv7TduQ9VZeUwd3yL5pWtBV3WOKSWYqAeQfgfBdG1svjYGHH9BtBvCtAn8Hyu01TMZNvk9rxWvaOT5tEdiUXgDpwiBYb1nLaRi8YOitdVdVCytV0WjA2kwdYEZt99INvIEJ7-2mH4cAE62BuiJxtRxcYQE-JUeVdJnOIh8Cc1llq0HHUhDCETdYRNebWJ6aNBxUc4zAi3XHj998ianP7um-fI7hNd4bxWT-eJYtSb2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2-7s7Aekci6TYcqBtikqQklsCRSC8PAxPxivAeSyQ19IKNddfo-DImij-rkOKInr6XnBS7kjCkv88yyaSD8ZHBjSw6X95p4snTBIlDcqFb0Dc9D0YJ50xNGwNkFuJ_Hfj-KVLTH0SN-eEHoMETxDK42AjaRM4_-tcFuITUuPVnJfy4x9RkZ0dG7bHDKMMfRRYPUH2w5KuS-QMHLEb6eulCxulJyruUC2CFlhb8HdCksLE1-Ui69Hm6mPwMBTFhbps_CabN9GTZFL6mCV5bimSWjc_FFDBPNHYo8icrul_hjNlqX8jWRkHbkUynfb4P_t4goK2qTPNOjyr-Wl4ciSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa7-NibGNDkimyZP8x0hS4-EI7USUYT5aNqCbYdlcsZJfNO17XZai4Ny9FmAk2yeOCeqmWTKjCDmSKMea2qF1gYlSuufzlA0uPkGDoMVvwFTrFvifXNeImfwtHT6cfLU2eUPsKaLV39uLrMHxpzX-nk7BhRnw7hDuonf-nZTqyVGy6yHdbETcyIaGxNa6cAq1uLQKrofOtDmlBTh3u5mXWfSFoEtX72CJx3EF3VJtLkMQsMynOnpHsG6oBjG1WMmM4AcHNAUdHdu31eldDAJFY9SxQjrb4nViy4tOwv47iMkzSzeaYgHlhnd24ITI27t7AZMfKh0Ld6URWj0jjaCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnsdTfEN-T0orQbVNYXTF7bKfd_6RQhuCuBsg5TgBIGeZii7TMjNLJbjQKYMdK6IzrWsddug476gkqnPc1sBl9wBS8WqS9xPbKyr5cOyso5-7z3s72uAUb0P8pgNXH8mYhKpzVLEDj2riPTWyp5AMRsJJXj3LcRRE-wWA9KFz4yLTtDvA8nYfJW2i7gDIy5YrTCnGlc7VXZOTtrC9KEx19yBLATu-uA34f07AwjZgQgS9IDHQ90WjV3s1BK8F65lCXl1j-_abU-q7hqn0Qr0rlCIlHCGokbjIJiex3M7mhRQqFATU8897Y8pZeoAZd78FLznYmBI7xxamG4LfUrdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI7kWnkXL8frVEVf5cN9nzPBs_d3HkndwNroaMk-TRcpI9D0QqhTFl9azGFSwZH3kDLtCzwRuzalfMxm0NHp9ZTd13i5OEhlZHPUBfrxZ5VIACF9l0SBWcQKxz2-CWwNWUBUMbkYLgowtdPODQU2YshYGEnV1_XK9PwFbts4PxEo964gQWP8EK9vd0OVe0RGuXBb5ViKSuKSsQ8oTmgu8XG54f6hOwmPSOX-2TIKyRAzp4dk7TFTEXKoUoih0suOEYDyUuGlNRSt77AvDe1NMcmwzDpKQX7mntm-Od-b1BveZZ4YEdh2c4eLVy6AE6IPDpxlRkXgfrBIBp5hCZwYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=Kri86-OWySxWWgP4mUAJWWWtGkbk6F1Uc-RXytjHmaNFaPrE6bEVUuEnGX_5CuDJQcmcQFdfSiIqmCa79Zd0BA6frSD3a06Q411fex5gRv35TGg4TmZSLSGFY1M-MTq2fOkAmctcSxZ0M4xIpP7GksfmO40Z1g91CXN01JIweq8XfPEV-YM8UC-i55tFhkdN36CVIhu2pQSilO5Hi8-9IPgk5yi4VjDXGJNmuByf491S7JUzd2d3hhj7wiTRcBipbNMn6En8k40yp__Akx4lKDTyHutEViYeqaqIgowjIP0SzYsNLIhnPvPnhrSNT0ThzjYCLdsbgLgQBsZKplwh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=Kri86-OWySxWWgP4mUAJWWWtGkbk6F1Uc-RXytjHmaNFaPrE6bEVUuEnGX_5CuDJQcmcQFdfSiIqmCa79Zd0BA6frSD3a06Q411fex5gRv35TGg4TmZSLSGFY1M-MTq2fOkAmctcSxZ0M4xIpP7GksfmO40Z1g91CXN01JIweq8XfPEV-YM8UC-i55tFhkdN36CVIhu2pQSilO5Hi8-9IPgk5yi4VjDXGJNmuByf491S7JUzd2d3hhj7wiTRcBipbNMn6En8k40yp__Akx4lKDTyHutEViYeqaqIgowjIP0SzYsNLIhnPvPnhrSNT0ThzjYCLdsbgLgQBsZKplwh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=vNsR0DklgEHhoTLGkm5H1jOGaOjBGUGttVqxzEc8PQPxQOoCttz4SPDYswIt-VA0nV3ORI0sVYHeTLvLIm2JJU9eIekkYFM10RvPqHUSHjAmjp37_JKAbNUNMFfXk5_PS8Z8F7rC0PSnSkih-CBx0Q-qEQnNcQbQ41LRnpTJ9IrPrI3Cndz4DonhARqjqR7mFZaN-lNrQUvvcEtRj2TOJH-qp0v3SrsrP7FaXZQcU7NB5nWAxrkZWjnpVUMMevZuw1MVYxrbyUJ49RDOdX3DrWLOA1Fqp8Y9tayuR-DHlGAn4kW1-C3QjW5PDyJFMloSSyOAraCH2DykLtlTQAITPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=vNsR0DklgEHhoTLGkm5H1jOGaOjBGUGttVqxzEc8PQPxQOoCttz4SPDYswIt-VA0nV3ORI0sVYHeTLvLIm2JJU9eIekkYFM10RvPqHUSHjAmjp37_JKAbNUNMFfXk5_PS8Z8F7rC0PSnSkih-CBx0Q-qEQnNcQbQ41LRnpTJ9IrPrI3Cndz4DonhARqjqR7mFZaN-lNrQUvvcEtRj2TOJH-qp0v3SrsrP7FaXZQcU7NB5nWAxrkZWjnpVUMMevZuw1MVYxrbyUJ49RDOdX3DrWLOA1Fqp8Y9tayuR-DHlGAn4kW1-C3QjW5PDyJFMloSSyOAraCH2DykLtlTQAITPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=dZ423IHpGgIlg8R1EPUYwgF4PlE7OrGHbcBN9tgIl77LnPuBWMm9V5vNg30Sx4Vk_5tD8DizvcuJnab8QJBnRIOzk9pfVL4c7uMFo4jrWtUQ8IhH2czfD70s9f1xHxAnWWV8TekHNTATXNfEXdYhcaelkvhqoGPA0vfaS8roGGD-CcwgXL95EIelCb7e4jths9i9deJtAep_oxQS5LDPBLi0o4Vq1kC3MQR3q1C1nmW4jtIM-qdcPqJx7nt-hATNn0-vjIO6kse98bd_ejGylcj9tNQE5LY5qNzNbwMZDi1MP3DG8bGZsmAYh83WNApjHtYMyyBQDcFtYMDcs76fUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=dZ423IHpGgIlg8R1EPUYwgF4PlE7OrGHbcBN9tgIl77LnPuBWMm9V5vNg30Sx4Vk_5tD8DizvcuJnab8QJBnRIOzk9pfVL4c7uMFo4jrWtUQ8IhH2czfD70s9f1xHxAnWWV8TekHNTATXNfEXdYhcaelkvhqoGPA0vfaS8roGGD-CcwgXL95EIelCb7e4jths9i9deJtAep_oxQS5LDPBLi0o4Vq1kC3MQR3q1C1nmW4jtIM-qdcPqJx7nt-hATNn0-vjIO6kse98bd_ejGylcj9tNQE5LY5qNzNbwMZDi1MP3DG8bGZsmAYh83WNApjHtYMyyBQDcFtYMDcs76fUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=Iv0Dny_JLk7nfKRqG4v545S4HJ86TrrXi1uNNDHIPdQ_jDXdnLdIM8ceFNPsN_N3BkItY8fejjGmjrS6KeT9TFB1IZC5sjkcoPhzNj8gXp-B-ORXSYg0NqOeZBuWUg71oTw0c2IOUNzyVcZCEQ01ErvsAl1dvt__lF9r-3VVrP4dVv5UjerfaRkfVzQ19rOv48k-qEdBMoaYl1tSGJhxD-X480KFsrDxY4GUVtBeNok3EGY-Y8dpSSWcegjLmL0F1_blcIwUYd1ZtjyH4am6m3tT_36-QKZieb175yPDUQodC6b27epJzncWvfkt4H-lbLPSdTCCKSyTzjLkt_QBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=Iv0Dny_JLk7nfKRqG4v545S4HJ86TrrXi1uNNDHIPdQ_jDXdnLdIM8ceFNPsN_N3BkItY8fejjGmjrS6KeT9TFB1IZC5sjkcoPhzNj8gXp-B-ORXSYg0NqOeZBuWUg71oTw0c2IOUNzyVcZCEQ01ErvsAl1dvt__lF9r-3VVrP4dVv5UjerfaRkfVzQ19rOv48k-qEdBMoaYl1tSGJhxD-X480KFsrDxY4GUVtBeNok3EGY-Y8dpSSWcegjLmL0F1_blcIwUYd1ZtjyH4am6m3tT_36-QKZieb175yPDUQodC6b27epJzncWvfkt4H-lbLPSdTCCKSyTzjLkt_QBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4J1a8sd-PmvU5Tc_c9cajxFeZix0pz7DHn_6wgEh-PfIjbcWUj8RAQiOLZCuP6tpL0AOCltuJdtHyKQdwBIusHXBDuk1gyrirXymw8zGcVGtgq9Vd96EdENAUImC4mTPRXI7GBn9-dDtjHXAyD7Bfad5-biJaRyB9fjwiSJ77ZiW-0RFpVMh8LDy3ysZzf7yC7U2DlWPW_1otr3UAfLpVQHMi3_sKkSTm8uXEZ0uEAe_OCYDcJRb90bQv4Kcyi83biaZs5NvKwe6XuEV5yWZV-_DLM57wWfn0Xwufqye0Gd2CcL31xyiqXVQcyqTr4LRwDMDsy2Bn_P-n_k3yw0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcl0n1TQoUh8TK6DkISA5ndj3CfpqenSev1-i5cLCH2bhexcUmyvvO3_4TWP7hQrkS30pVD1YBf8e0YKIFzxAVrX8Wpg2HHYQKAIastLEH9b6_LbU3Rg99t89h1NVgDWBgmtdUzUKvNBa2Ysb6qaeyDZAaNkxtOZvBt9VHT3qnUsGqC_oiD5Tghkzd4IcRG5ftfQ6oQ3g2biZMGrCDKQ5C7JeDQNLtp7i1C8824meXeRBviC45rY4WEEMWS4XJK-D7FmQSNUZcm_kGIS_76DpB7voD5lfYqjwI6gagsTH_OSlPRHBZbyQ-JRXQfZxklukqhX2ZBQtvhBToquKu9iqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLm531ElN_f62Q7Dkg76oSYQtygREk_oqbiWmBPIk6yd5iS8A0MJ0v_25th1ZpscKvSt3aAXy6fiflRBy9Fdk1PcBjI5Aez8XKf_T6rKsdUFNI_kZVnpafI92_wADJZ1uqFKoySzy6AFRQijQrE-Nl9vEZyL3tX6Pow88q3VTba0Gh1q5nX8RFgME2zrT3ukwRCvTeTrapEIwAwb7Zbjja0hrRndoCOuqXnmYQLqPK8ic9gTgVPesvPnmw8K-59XlmQiOIoekqZb51e7K8mY_iv3X3BfBljgjLmIRvvC_wU2B_n557WqOEfBk7PpFHNmBQqXyko4oKieAK-Q08CsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=FaiGWYziZ7_uuBZK4qh4PKAXub8-H9iX_8NpAKN7yOLHHLdUKY1KKgFSy2QiHirL2_tUPCagh-_hGvYIE8HThI_-0NgiDKL-XJ807GWWP06x8RGUAKGQN_3ArbRe_D2iI3Mvg3tqRo_UjfTLIEgjPQWf9lHX9Q2OU8wwJlGpoPAfIsZK0D5Gc_EL7tCq2nqUyHPBuqyWPQQZxPQLoeBqSjhNrTvTbVEfs6x7nzOo1ClymQkwI2-P3A2mEsOlakMJHMGhb7Ob1ScfV9eojo7nARsXrNt1whJXzpQaQhnbcSX-3AD2VLEHI01nPPVsdYBVX-lq8MZ79AJQ5rguTvZueFa2noScLn0A6QgpmxxaiPSu2gXw3ym70ftEjtxLSruSz8Gb6CQbFbFwmhYH0v8E0KCrijnPq04LYyRkUm7M73D-Cfd6AmF1e7dnmFHwZrPhdIrmFegKU5FB0PNv5TGtvBTVy265vpTE7Ld9Ah2rUS27UrhS-Xb5Sy5hvblENJcq-pCpuVCeXxSLI3J9Hx1WhU4D9MxEAShROsHskh2oSO4StP_bTCar4iGbaRLCD9To6ZoEEES5DUnByJ4QYzqfihX5sLscI0-U9dSOMBzizsKY7maMaXUMKUo_pRBvbga_BJmkpIfAuVTtxB_UKVHPSHJlxHl4fTufEMLma_peQLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=FaiGWYziZ7_uuBZK4qh4PKAXub8-H9iX_8NpAKN7yOLHHLdUKY1KKgFSy2QiHirL2_tUPCagh-_hGvYIE8HThI_-0NgiDKL-XJ807GWWP06x8RGUAKGQN_3ArbRe_D2iI3Mvg3tqRo_UjfTLIEgjPQWf9lHX9Q2OU8wwJlGpoPAfIsZK0D5Gc_EL7tCq2nqUyHPBuqyWPQQZxPQLoeBqSjhNrTvTbVEfs6x7nzOo1ClymQkwI2-P3A2mEsOlakMJHMGhb7Ob1ScfV9eojo7nARsXrNt1whJXzpQaQhnbcSX-3AD2VLEHI01nPPVsdYBVX-lq8MZ79AJQ5rguTvZueFa2noScLn0A6QgpmxxaiPSu2gXw3ym70ftEjtxLSruSz8Gb6CQbFbFwmhYH0v8E0KCrijnPq04LYyRkUm7M73D-Cfd6AmF1e7dnmFHwZrPhdIrmFegKU5FB0PNv5TGtvBTVy265vpTE7Ld9Ah2rUS27UrhS-Xb5Sy5hvblENJcq-pCpuVCeXxSLI3J9Hx1WhU4D9MxEAShROsHskh2oSO4StP_bTCar4iGbaRLCD9To6ZoEEES5DUnByJ4QYzqfihX5sLscI0-U9dSOMBzizsKY7maMaXUMKUo_pRBvbga_BJmkpIfAuVTtxB_UKVHPSHJlxHl4fTufEMLma_peQLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=B8UfoXq2wYVrbpU4CnDda0UnA33t1uJ5JWK6eV1UnRt5SEfTSAj_9ZsSWnHO_kPm5ZfIzqBGxSfNcZ4mBli95WKBItNnlDdVB8mySPXXV2_6FlJAOIxvfdAuylWIYQgbCCAguS42-CnDWwaCDz9gp_Dzmj2dkXsviZx2nUpL984T4-K-n7PO7UtN0NsURKZpYs4ZlEqo5_iljUoP1AIK2Bd25TVsxO0P3cWob3uOdViRJe497EHyO5nqj5ZQAxi4vcp1LfAfjNdb0Wg9YSl8AebFihObgf-hsOLdTjmVMQ6-6ocyOGYM1GzeMe8ufiv05Fve_x4TBa2Bu3d5TVfB7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=B8UfoXq2wYVrbpU4CnDda0UnA33t1uJ5JWK6eV1UnRt5SEfTSAj_9ZsSWnHO_kPm5ZfIzqBGxSfNcZ4mBli95WKBItNnlDdVB8mySPXXV2_6FlJAOIxvfdAuylWIYQgbCCAguS42-CnDWwaCDz9gp_Dzmj2dkXsviZx2nUpL984T4-K-n7PO7UtN0NsURKZpYs4ZlEqo5_iljUoP1AIK2Bd25TVsxO0P3cWob3uOdViRJe497EHyO5nqj5ZQAxi4vcp1LfAfjNdb0Wg9YSl8AebFihObgf-hsOLdTjmVMQ6-6ocyOGYM1GzeMe8ufiv05Fve_x4TBa2Bu3d5TVfB7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMjkh20MJaZteNnVcVL0SGJxhZH4sWv7HHeiAtrB-IQ6lzgjGzpKrwlQCWXeS1XJwaKH2QfQ35CO9wvpkqA5sFVQDr31v8Q6YQov46hA5Hs5IBpFh6uiofEOia0-DY_K9l-AqEvi6hMLoUC2q3v5Pz4d4Xv-y6ZIRCOBZlR2nwwMIRGiwnLyf4ZZ4escpLpDCgSb036fiDyR1OavrxIFPMLYAgHGS85_GqoFoUs4CZn3WjRH2gmz3XM5xhhUN6WpZEmGo_H70JcNR_APenkW1F_SGrVdynh3nyWbvX-_X23c3bd7jW752MwFvaASAGC9TgkXOQTR_NOsKPfYNAl3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=QqOCp7vG6ecc1ZVds_7u1achO6xNipVEaN-ysLNDxhcNN02rfkZ5XWDE7_DyYjNTNpXwtJw-UNi0UBss4kLt583lgQH58B1d360aOzNqsqosTFAu1HrSvRimaW6U-8d2FDTHy9g9JpUWYyjKeJ8SnoBcDrZhkXKSWLs5XDMzbucbc86I4OayZkpcv-T-DdzEOo9a1kB-8eBMdw7cQiHgusL4RhhSgypmt6PfzbYttKfklIdJQzxJk68KYM6PYDJopc5hlttN7AW_e2F9_fp9NsAK4oaFNvLeqMzJgXMN5h6vKfFfJUH_yIiM9oKAalzMAsmSvqLtaDb-O6x_ATC4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=QqOCp7vG6ecc1ZVds_7u1achO6xNipVEaN-ysLNDxhcNN02rfkZ5XWDE7_DyYjNTNpXwtJw-UNi0UBss4kLt583lgQH58B1d360aOzNqsqosTFAu1HrSvRimaW6U-8d2FDTHy9g9JpUWYyjKeJ8SnoBcDrZhkXKSWLs5XDMzbucbc86I4OayZkpcv-T-DdzEOo9a1kB-8eBMdw7cQiHgusL4RhhSgypmt6PfzbYttKfklIdJQzxJk68KYM6PYDJopc5hlttN7AW_e2F9_fp9NsAK4oaFNvLeqMzJgXMN5h6vKfFfJUH_yIiM9oKAalzMAsmSvqLtaDb-O6x_ATC4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=pCw35z9kpCQnu_DzbU0MnjgyVuJKFMr94zbGJwoCUHcYy2QtBJzNa92GLj_3I60OX26hxXZvWBWp2s24ZGXj0ebVPoR803IeuLOUwHzE6lGtu9urbWtw9e6ttQqt4T6JH8MxhZUhoyI_k7DJ05ELMMC1vH34fuKI7X3GM_GfmWxljMygLCsrWULPJRkmOr-Tk-4gBCGsELZuRew5BFjUvb9AuL-yEMBNhKOx26AJYSo_LJpP9P2wxq2mdyMdr9J3oL-sOEoHZ7FY2nP5ekQ-lbyZ9UrMn4SvqioofdaVsTW-U_dmnMZQpDFPKNNy7p83GzGjAXcWTEU2Aj81V3dRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=pCw35z9kpCQnu_DzbU0MnjgyVuJKFMr94zbGJwoCUHcYy2QtBJzNa92GLj_3I60OX26hxXZvWBWp2s24ZGXj0ebVPoR803IeuLOUwHzE6lGtu9urbWtw9e6ttQqt4T6JH8MxhZUhoyI_k7DJ05ELMMC1vH34fuKI7X3GM_GfmWxljMygLCsrWULPJRkmOr-Tk-4gBCGsELZuRew5BFjUvb9AuL-yEMBNhKOx26AJYSo_LJpP9P2wxq2mdyMdr9J3oL-sOEoHZ7FY2nP5ekQ-lbyZ9UrMn4SvqioofdaVsTW-U_dmnMZQpDFPKNNy7p83GzGjAXcWTEU2Aj81V3dRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMZeHavwCQagvybCUOSZGlcdOITCkQzI9WGPdqL5UuhSJv3P5lBxQU7rRnvknLopNcIjMu8d1-r_gDKUl2R2ZVFSas341dFeTnNmcSMPPNeEjU_qB1P23xTXujblLi4ezfArlBW7F4ZVa7zaMmyA9-zDNePoaoEJcm7-ACgNcscj2Y_1iY6cOUSMou0Ss9ISiNaIAPbcToPKOM4PTH05ixYs8COsZZ56nXaGqL_kUO7TAmieXv0fRaSgWbtVcNlnX50Nh0gxTzEiZIMQyIZm52iMNpQgah0BjS-gbMXDopkoonUDp5Wr3vidpNxL5DNCnOMIEVuQrnrStoWXcyqpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saV4B0X9TrmKyPteF8XsOGArcaKIlZfc_9qV9U0Ddw4NFVlyURsiPZ9jqdt0P792GKcDrPXcebfc2iAwnFvMZ_EXPlmzMR8AviLeFo4IITKSKVL4pyyrXeotNDTh4Pg12Iegbk6_dMyVbEoe66uDADv50vcKyUhEfQlr6-gV3x-4Jt2RoZtocuJEVKCFZ-xyfesnXdjS184WP2iiXn_LIn7piCbx5GbDCYR_lx_W5QXW_bQW0RoG9AKFdsF-YFdtyBf8WEuqr-qvsizx-96pm70WJyqfyb9J8xM1af2h09QG5fqO5COORFfSOas7uco4RLw4ejLp94720FjBIv3cJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv5vH7TVnFWYjcS0RWJeKY7RcOYs11A6j3PRHh6yNvszKJxJ2YReqSLw-hI9walRF8DI_HwiO-cPUJadC2CKrml7sCTxYi9TsYP-PNHLFX51F6O4hQOurqt5vKUYU3VdMoFJOEa51h0ZkIU2IgdGxssI_1tN65wdVekojBXDXAvrdXCGwFj1OCwAWqomg9uYvui1dixwifZjtg4aagG8wdtdkj0cWhMuahBcZT23nyED4iNMEmPkFq0s20d_BcGChyUIJTGaUXE4KrmEdUG3gjmTTx7tscOcJYOPHyedDBotnZt6kHuYOGDGLvuAMlqRsDtv3LSPy1OVWmglrvYygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAoTlDw7SgS9-eE9LpN5S-R5yqjpMjm8rCDet3eFieSAariwzsubHVPSGY6s-tSuJLLQ-47Jr7dN35qS2Uui2n5CxF-ma3yBV5CrMRDHhO3hERk8LuJZJqigYYeYw1XahmO7K7XIHS_b1u4hhgkQ4ARAWhD30kY4vVnxr8NK3HSRChoiTuvFjXkxLdgp4j9ekwwRT4yrX3BzYfgftXcNK3SP0ZJ_ZFKta2Y_qhkpy-NT_fs1bfMVjTeux1lPMUaCOFmptuUZVT3q3_Uu5DK63vXLUixbbWHwLv_2fSwP78jFDe5AHDn8_bXGAb8VAGbPBPtuzNHNIpIrTZiILtIOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=rYd6YlttBZpPmcZlouFKM6eO-lFEeYyMdsbAXphgA9_2QNhtICVAsI4L9bb3ySbgkZfRZR7vRGs3_awgx-p44qnqSZPrCkSTtxTYU2ewIOZOgmKGFd24yCfq1Nj5jT2U3fm1nlyX2NG91jWb9sG7R3mhPDgzYrAGqbzltKXM5oEN5jmLBM1LLesaLnLcPRYZW7we8vHgv7xwBNPlbGJvYNK8Fc7cYDEU5OKSHWFm75-YNKXB1R__u7wfs5U1-AJzYT3OorcHCPCRTkTmzzbpn_FsEbeT8WUcodLj0f_Yw8vmo4gqlIgRZ1Sz2I5cUYMikYIgFTSyGj-LlkFR5ycBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=rYd6YlttBZpPmcZlouFKM6eO-lFEeYyMdsbAXphgA9_2QNhtICVAsI4L9bb3ySbgkZfRZR7vRGs3_awgx-p44qnqSZPrCkSTtxTYU2ewIOZOgmKGFd24yCfq1Nj5jT2U3fm1nlyX2NG91jWb9sG7R3mhPDgzYrAGqbzltKXM5oEN5jmLBM1LLesaLnLcPRYZW7we8vHgv7xwBNPlbGJvYNK8Fc7cYDEU5OKSHWFm75-YNKXB1R__u7wfs5U1-AJzYT3OorcHCPCRTkTmzzbpn_FsEbeT8WUcodLj0f_Yw8vmo4gqlIgRZ1Sz2I5cUYMikYIgFTSyGj-LlkFR5ycBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLFQxIBAGNdDpGqEf0gRGWAQivVKsz5v33aOgRrfoPNe3EjLm-X_zMvTJFGichv9MTTU1QS8EgLKKmiuuf3H9pc_NHiuc1NXrmOiJyOSUg-EWEJ_EnT8W5fwJsMXUTG_mOFB5ECreSuhI-L3cvmVkmXWAOwq3vYH4nj9xxrRdu7XxvTwPBMjoZxgI1ih8-uQDpDCH_beab6Fhk0CRSjhBFhgDhTIEHdSfDRoFbLx2DlbRjDGGH404bFnOIve3OY6zP0jARJ0QAfd6p8AD7ABqM5gPpcEGU3Hzr-4dHDFcAiLsf4m3bkop5S6zky7BCja3V5Ea0zTJnVvCh8GCUQQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
