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
<img src="https://cdn4.telesco.pe/file/e5yBaKnljrCZL8f-XmngXq-2B2E1Q0NSSzMSzE5PcZ8g1-NzrM1iZ3Y96Yt1J3sek7RqP1Vkw-ssWEioNf54qZ1zg17LrPuUz0R4NwCGduwQV3Ex-_IrpZE5Rw-83-Mt-zKp1iFM4VDdtWkbcWsOpOKOvZQgse7NURtVyPr_Vt9pweyTqO6dl3QYiPJhoQexCfTjMwcKkIaNPEWDD-WkhVA-axK1c4p95axa2MWypfRCVc_efsuCKJ22dvvj6VtpfywzR7Cr96YWMxzXmlJMzwCPntGV5fmr_rOHTnlqzMEnaozpICU_aiPoVw0l-zUCJJBh89_Ptb3mRGZXSx4GQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-691780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1292afd051.mp4?token=fgxBHlbGkxoCW-qU-nBgboW7XZCxozp_8dmI-Hxv4SVvazvtIBYKNpk6B0ju9Wpkl15PSWfqWd9YgS96U80WlhpTbYMyoYm2L_GgETqco4e9t_AOpRGsIy3t-JkCyQv4XM1v7tcHa0t3-02X4uDZJ1ZQQ3NLYgL8fkRmujn-OzvWMHVKEjvBlM3utJBNepNiiex-X1kq4lHC9UjiUU2Y8h9FljqzfxIWMNNWYwZhGyk7l1QjvkROJtpXxbhLmV47P7ZPhyHNZH0KaKftZOD-LuFnv3oUey1bKCHY-azNAggt60fpHFuplTwIPQf_Xg2EhoJ5MUzlva7_YU-z3ylbPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1292afd051.mp4?token=fgxBHlbGkxoCW-qU-nBgboW7XZCxozp_8dmI-Hxv4SVvazvtIBYKNpk6B0ju9Wpkl15PSWfqWd9YgS96U80WlhpTbYMyoYm2L_GgETqco4e9t_AOpRGsIy3t-JkCyQv4XM1v7tcHa0t3-02X4uDZJ1ZQQ3NLYgL8fkRmujn-OzvWMHVKEjvBlM3utJBNepNiiex-X1kq4lHC9UjiUU2Y8h9FljqzfxIWMNNWYwZhGyk7l1QjvkROJtpXxbhLmV47P7ZPhyHNZH0KaKftZOD-LuFnv3oUey1bKCHY-azNAggt60fpHFuplTwIPQf_Xg2EhoJ5MUzlva7_YU-z3ylbPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشم؛ تکه‌ای از بهشت در جنوب ایران
🌊
🔹
علیرضا وهاب‌زاده
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/akhbarefori/691780" target="_blank">📅 20:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a39522b48.mp4?token=UPcgZu0-5i4TxSS8wb5w3uKhaQjwigOAKZA_if8E3STF2CiO7Mf62HnZnvVMDx51Py_GAYWKD8GkMWYY4sRQpWVO1M3No2AyLYTvGD03WJwV4VnbNNJWLsrsqOvg3sOYKegYC835fekwM1ZHzvTCZHONj2o4CPqXoeb-NFmhfeLorVKYd65fnX3QJS4-2V9EI5n9-XY52eRcewqRFS3wvF146J3Nm6ysrFlgbjN45Cu_G305XqUSBuA18IxP5e9Ahiw805aihhcrI4dcnQcmGfPK-JZQ6EE6PYAYVptJmrP78YQ3i1OYVYu4EVsZKQOL4RnCvDpYbk88mreavmtXClzEsTPVkmVkwRHP89vt-ktieIiRzTzIkuyKfUPO6ZPMfCZ7zxVqykgPxGwunYG-jJ4_230uGb2DBtiu_g0kTQ1DaEGzSbLR5VDKZn6CN7xF81p5s3DHTnGVUInbpU83uS2fSJmXzn0mvElP_DVDe2yyGQ09an-oOiFcKtbjk8PrSuiSsYmi1-D0BTRQe1NaK_upGcglfx6zrstaR0XNBmDhkz3vGPW7Ft4bSCGeGgGvlQuz4Xb5svjmr17GQPW331Y6maUOJqPYAJMESR_6I5lKKvi3fYVvrjpjU6jHwbc4wH5OSPGYdfwSg-t7z34rw0dVLbpWhCCmHfgC8j_DzEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a39522b48.mp4?token=UPcgZu0-5i4TxSS8wb5w3uKhaQjwigOAKZA_if8E3STF2CiO7Mf62HnZnvVMDx51Py_GAYWKD8GkMWYY4sRQpWVO1M3No2AyLYTvGD03WJwV4VnbNNJWLsrsqOvg3sOYKegYC835fekwM1ZHzvTCZHONj2o4CPqXoeb-NFmhfeLorVKYd65fnX3QJS4-2V9EI5n9-XY52eRcewqRFS3wvF146J3Nm6ysrFlgbjN45Cu_G305XqUSBuA18IxP5e9Ahiw805aihhcrI4dcnQcmGfPK-JZQ6EE6PYAYVptJmrP78YQ3i1OYVYu4EVsZKQOL4RnCvDpYbk88mreavmtXClzEsTPVkmVkwRHP89vt-ktieIiRzTzIkuyKfUPO6ZPMfCZ7zxVqykgPxGwunYG-jJ4_230uGb2DBtiu_g0kTQ1DaEGzSbLR5VDKZn6CN7xF81p5s3DHTnGVUInbpU83uS2fSJmXzn0mvElP_DVDe2yyGQ09an-oOiFcKtbjk8PrSuiSsYmi1-D0BTRQe1NaK_upGcglfx6zrstaR0XNBmDhkz3vGPW7Ft4bSCGeGgGvlQuz4Xb5svjmr17GQPW331Y6maUOJqPYAJMESR_6I5lKKvi3fYVvrjpjU6jHwbc4wH5OSPGYdfwSg-t7z34rw0dVLbpWhCCmHfgC8j_DzEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فؤاد ایزدی: هرگونه کمک، ترامپ را برای تشدید محاصره ایران گستاخ‌تر می‌کند
کارشناس مسائل آمریکا:
🔹
ایجاد مسیر خروج یا ساخت پل طلایی برای ترامپ تفکری کاملاً اشتباه است؛ چرا که تلاش برای کمک به طرف مقابل جهت خروج از بحران، تنها به گستاخی بیشتر و محاصره افزون‌تر ایران منجر می‌شود.
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/yRIXrUwC5Xc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/691779" target="_blank">📅 20:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a49f5f07b.mp4?token=EF7sR5m9_WKwrWSdB9vFL-UvrMuDGe7CGwsAim-O5TbK1DVrU5XxymqnZ1sfseQ01ZwU7BLvkAZBVe395b-DFnalODM7uxfuH9WCP0OJl69PabRiy0NYtLuYAxEdHHsbt_0weJHdQcckKDwTYCxFd67194egrcbs0CC83D7rf-vnRCySbH-7m_CNg4IW3jx4i2g-xO_herLq0GrjCHkemHC64OjiHMZ7_n35DUjgI6bmf6hDliHnGydZjxFTe2xIaZE2-kdP1Qm1-YOmSKnCbOBYiEXN3oYkXopXsExgvYzR1tEfHaXtefCNxea1NlQ44Fi-GCupY2k2q4ATMq_ttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a49f5f07b.mp4?token=EF7sR5m9_WKwrWSdB9vFL-UvrMuDGe7CGwsAim-O5TbK1DVrU5XxymqnZ1sfseQ01ZwU7BLvkAZBVe395b-DFnalODM7uxfuH9WCP0OJl69PabRiy0NYtLuYAxEdHHsbt_0weJHdQcckKDwTYCxFd67194egrcbs0CC83D7rf-vnRCySbH-7m_CNg4IW3jx4i2g-xO_herLq0GrjCHkemHC64OjiHMZ7_n35DUjgI6bmf6hDliHnGydZjxFTe2xIaZE2-kdP1Qm1-YOmSKnCbOBYiEXN3oYkXopXsExgvYzR1tEfHaXtefCNxea1NlQ44Fi-GCupY2k2q4ATMq_ttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری خیره‌کننده از حرکت یخ‌شکن هسته‌ای در قطب شمال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/691778" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مشاور عالی و جانشین وزیر بهداشت: مشکلات تامین دارو درپی توقف پرواز مستقیم بین ایران و هند تشدید شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/691777" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قیمت نفت بیش از ۴ درصد کاهش یافت و نفت خام برنت به زیر ۱۰۰ دلار در هر بشکه رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/691775" target="_blank">📅 20:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc4b1140c.mp4?token=stu7E3uJcZZRU8Uc0gC332Bx-xDirsyj6RY5hmL2JiGks9CSzROc_zJqkyYE7HzZ6mZM7qrzPojd12KhZCp3YaFU_NaUo1S2i4GuXs4uXhFhJ2k976BpeASPgTTbjMxuH9rbJbI-Pn0fPrmPepYlJQ64d6en52Dw9vhltlGndmGIPI8wqVM8DNr8WWBhqjAEUeRFP23GCsurMESWV2ghVDCdb0T8z4Y6sbY-Ud8-fPprggmdruZEflFOlOIRasGisIQtDKa68-m-P204emlo-90OVo4A88PDGc6iwKZ-Wgay2IUllcYxJiwzwE0fge1lKzvD6QK68lLzsAI1UFwSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc4b1140c.mp4?token=stu7E3uJcZZRU8Uc0gC332Bx-xDirsyj6RY5hmL2JiGks9CSzROc_zJqkyYE7HzZ6mZM7qrzPojd12KhZCp3YaFU_NaUo1S2i4GuXs4uXhFhJ2k976BpeASPgTTbjMxuH9rbJbI-Pn0fPrmPepYlJQ64d6en52Dw9vhltlGndmGIPI8wqVM8DNr8WWBhqjAEUeRFP23GCsurMESWV2ghVDCdb0T8z4Y6sbY-Ud8-fPprggmdruZEflFOlOIRasGisIQtDKa68-m-P204emlo-90OVo4A88PDGc6iwKZ-Wgay2IUllcYxJiwzwE0fge1lKzvD6QK68lLzsAI1UFwSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای محکومیت بهاره رهنما به ۸۰ ضربه شلاق به خاطر شکایت سیروان خسروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/691774" target="_blank">📅 20:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHH6C9YOwpUkfjCKn2RgTcUgS1JsXp_ne5EjZx_GSnlMv_PdnrRV_Fzzc0EXpCY-N72S_PSVbLw0MmDKectN3pvJt9IA-sKJVVV7cu93OJEO39c3RVmTVobw5v04rjBWOzeY3-vwzT7_K1fx1UmWZgiQbrR2-mBcNng6L7ZhoNvOI2DRqJT_0YMcNTsXZXzihq2Seoqu4Ky6RP32itPBKhvEaxqAhSAM9pSvRV2Lx-vTsGNRBq7ICfjHYqXwxTCaoM0Mj2agsLA8GojTOdTPrP5an6EAWsCFZLoBmh0SPxa67vBlhgld0z6YQSDzXV0m8IbH6lGhnpso2AP43tOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اینفو_تیتر
|بازدهی یکساله شرکت های فولادی، از ۱۶۹ تا بیش از ۵۷۰ درصد!
@Titretejarat</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/691773" target="_blank">📅 20:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">17-1 Ane Manaee (1404-02-02)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
ساختار اعجازآمیز سوره مبارکه "محمد" در تبیین دوگانه‌ها از قله حق تا ورطه باطل [01:06]
🔹
"خوش نیامدن از حق"، همان تبعیت ناخواسته از باطل است و آغاز ضلالت [09:54]
🔹
تماثیل قرآنی در توصیف تبعات سبک زندگی حیوانی و زندگی الهی [15:08]
🔹
فروپاشی طواغیت تاریخ و قدرت‌های پوشالی امروز براساس سنت‌های الهی [19:03]
🔹
در تقابل "تبعیت از حق" و "دنباله‌روی از هوای نفس"، معیارِ شناخت، قرآن است [21:32]
🔹
بیان قرآن در تفاوت بهشتیان و دوزخیان.. و توصیف بهشتی که پاداش متقین و تابعین از حق است [28:10]
🔹
مقایسه علم الهی که موجب تعالی وجودیست با دانش ظاهری و دانسته‌های سطحی [38:00]
🔹
درک واقعی از دین و حقیقت، یعنی قدرت تمایز میان هوی و هدی! [43:33]
🔹
روایت هشداردهنده؛ تحولات فکری از پایبندی به اصول انقلابی تا انحطاطات اخلاقی و تایید همجنس‌گرایی [48:57]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/691772" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGh3FB_xEH1nXJywU27xe9GSpUoFi-zxiQidIn7DhbF_u1H7VUQ8NqlpYxaPNK3owo1KUP2vDbpbtUzUbjIl7KX06diF9UPNDu1M-rKFDaaL2_i_WNAM2wWZUsiSXOTPKzb6fdBkU8COQMSuuKc5FK4m58SFqijMBBwUuSvpHIE1PI4qCwE6UjWFuJLyT71sSfyDT7AsjknpKtTApqILoUjKEf2YwfsfeFuPvpLuye4ELe8qyPno59q9i51VNyXm45UBDT3ZlHJQiuQRJ7cOjOyjp6V2vyw1MOSTlGKvV0pHnrZ46HxUWrXeSXnqX6W8qwKye1x_LgLU9Y3eV_zeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیروس ابراهیم زاده درگذشت
🔹
«سیروس ابراهیم زاده» بازیگر پیشکسوت سینما و تئاتر پس از تحمل یک دوره بیماری دور از وطن درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691771" target="_blank">📅 20:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691770">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7df9eb7ef.mp4?token=onhyBcCaVxwlitAHdsVlK8VRRty8V6VQiIRkr0QPA4AT8cUhkeRNDBoPrUm9LntdvikxIyNfLJFLWkBUmZ6s712vkxQyYga0mkek1681dPj6syEYlOg0mN8W3MBVuSVJg8RBhqiSK-86PcJh1_dqS3c3VnSo1yDavV0sYarDnkACVTga5rksAyK3vBojE7BY_D4z1uugx0SW8FI5LFuxB0239RH_7B1SduK092amcrmk1Sx6I1x0k_u0BGlSahRqV5N1-tJm9lIAzMPlFdmx-o09bFwjzXiYIZ-WOXKLY3rt--GhykBVjro93e4VnqpGQideMDXrmluVpWSKdpPdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7df9eb7ef.mp4?token=onhyBcCaVxwlitAHdsVlK8VRRty8V6VQiIRkr0QPA4AT8cUhkeRNDBoPrUm9LntdvikxIyNfLJFLWkBUmZ6s712vkxQyYga0mkek1681dPj6syEYlOg0mN8W3MBVuSVJg8RBhqiSK-86PcJh1_dqS3c3VnSo1yDavV0sYarDnkACVTga5rksAyK3vBojE7BY_D4z1uugx0SW8FI5LFuxB0239RH_7B1SduK092amcrmk1Sx6I1x0k_u0BGlSahRqV5N1-tJm9lIAzMPlFdmx-o09bFwjzXiYIZ-WOXKLY3rt--GhykBVjro93e4VnqpGQideMDXrmluVpWSKdpPdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای ساده برای تمیز و براق کردن ماشینت
🚗
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691770" target="_blank">📅 20:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691769">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آمریکا از صدور ویزا برای گروه رسانه‌ای همراه مسعود پزشکیان در سفر به نیویورک خودداری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691769" target="_blank">📅 20:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7cb34dd6.mp4?token=k50WGqZwNKU5gVukO9OuoTNxSx4NY_dLyJeqs2_QAuNk2QOQ5Et5muiyRg9KSRlgSv_FHyKsgwmvKX2_3o9u3ELqke6VdpMKrK6b6plXovAWfOLohejhe5C_dGthIW8qUQZBy3mU7bmrM6HO2d275AFfdF3jPfpVSQ5wpVETilmxkgyMILkDV1UO76Ruml0cJxbT-AgbMf2wFTTHTOAhM8f4QR1pfQbs6oYbMXX4l5WdmdT-mb662LKTHZNLX_s9GevJ22oCTrQCa-fuBkThpn3VwM0Kn1qUjFeyiYLd4hutw3Tu_tqphjMueSTecoZc3_sWYU352Emj08QKM2h5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7cb34dd6.mp4?token=k50WGqZwNKU5gVukO9OuoTNxSx4NY_dLyJeqs2_QAuNk2QOQ5Et5muiyRg9KSRlgSv_FHyKsgwmvKX2_3o9u3ELqke6VdpMKrK6b6plXovAWfOLohejhe5C_dGthIW8qUQZBy3mU7bmrM6HO2d275AFfdF3jPfpVSQ5wpVETilmxkgyMILkDV1UO76Ruml0cJxbT-AgbMf2wFTTHTOAhM8f4QR1pfQbs6oYbMXX4l5WdmdT-mb662LKTHZNLX_s9GevJ22oCTrQCa-fuBkThpn3VwM0Kn1qUjFeyiYLd4hutw3Tu_tqphjMueSTecoZc3_sWYU352Emj08QKM2h5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚛
اگه درآمدت به ماشینت بستگی داره، این فرصت رو از دست نده!
🔥
فروش عادی و فوری نقدی  زامیادEX تک‌سوز و دوگانه‌سوز مدل ۱۴۰۵
✅
یک انتخاب اقتصادی با سوخت دوگانه
✅
خودرویی که هنوز هم یکی از پرکاربردترین انتخاب‌ها برای:
✅
باربری شهری و بین شهری
✅
پخش کالا
✅
حمل مصالح
✅
کسب‌وکارهای میدانی
و... محسوب می‌شود.
📌
طرح فروش:
📌
مدل ۱۴۰۵
📌
رنگ خاکستری
📌
زمان تحویل طرح عادی(نقدی):هفته چهارم دی‌ماه ۱۴۰۵
📌
زمان تحویل طرح فوری (نقدی): ۳۰ روز پس از پذیرش
⏰
شروع ثبت‌نام: سه‌شنبه ۳۱ شهریور ۱۴۰۵ - از ساعت ۱۰ صبح
⚠️
ثبت‌نام فقط از طریق
سایت فروش محصولات گروه سایپا:
https://saipa.iranecar.com
اگر در حوزه
باربری، پخش کالا یا حمل‌ونقل
فعالیت دارید، ما را در دنبال کنید:
🌐
www.zamyad.ir
📲
t.me/zamyadir
📲
instagram.com/zamyad.ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/691768" target="_blank">📅 20:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niOv9nhW1WxkCa6NQbf8kXeOuz4EZ_VZ_dKEqxpLcFboJJ9_gfaGVXAOceXZ7Nfnt57THeh27PDNNT-S-cgvrqpchYRIbrIKStcowjwzKN9Z4DS-bBJ6_j8zjAt9lPDuyWfzBwKpn4yZwkhzE6b66GKCUGeJUmji9-NIVAPngLrn8OnIf4b64JzxDU33pG_aWPNekEOgOFj3E-jW7utfwT-U0_Nah8jiAyofRMLQfjoP57hE8GoiiwUnBPmdghXQGyMLG2xgmZnzARztggKqTn431XJ5yaHMU8NNGdANJdhG3UwzyPPGLa_QiFCiC3sMb_AZ2q65LVY4xiksjq3Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه‌های تلویزیونی بزرگ ABC، CBS، Fox News و NBC توافق کردند، پوشش جمعی خود از در برنامه‌های ترامپ را متوقف کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691767" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054bdb2c4.mp4?token=lg52Xvr_JV-kbmecfvio5lXNlLfnpVdvAC9YzDbSqav7ygk2JLfFZ2nTVYzW6lARG8msawzR1R0CBZezwTgmeYLR72_D8djlegT4moHDRLsDPcmpaXtp0mj51XOzSKN0VQPbj4VdVbcEt3w8WyuHPDc8caaHcDcKkVYfmbwr58OdJgacsXAAbtz7AGV_G5viQ3h43u7AodtmgMQx7HTYPOM2ksnRQ9IDTldza3QeFcRHOEqC-nCUIrfYwVTdwJWDXR_Dw6vSqunPEbJp1Ww0H93v26B7xwi-9J9ynWN5xRAy60iEGxG0sfbAvd_8B-O2f4XligVggokElKIGSk0t-Sp32U-GJOme7JxJBQjxn0jcWvKm2PPRq8b5YXfgS1e5fEqTZ0nKWK-Mg6mFvGCPrQvhPYsEJLUIVM-zTt57k7dnrmigt51av5VaARw9XdnZItW-OyZHzubk6zdPysROGHhQdLYhdHiblGFdqqD2k8SwkkXdS4jbK5jdXX275kYpaQ3o7ImvjUJesmvEZ2-_WRtxsjfg2WfxiSbj0VKMmYwiDuHBgDpocSH77pL4AFtH6C_p5ylxV-iQMlNbX43IWWetwN1MbJUa8usDVJDdv-h84r7dbjyGgxBqlt7RXVWK3nHEvBM0ZURawa-p3QPjL3v5AajLz4DW0CksdfT2It8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054bdb2c4.mp4?token=lg52Xvr_JV-kbmecfvio5lXNlLfnpVdvAC9YzDbSqav7ygk2JLfFZ2nTVYzW6lARG8msawzR1R0CBZezwTgmeYLR72_D8djlegT4moHDRLsDPcmpaXtp0mj51XOzSKN0VQPbj4VdVbcEt3w8WyuHPDc8caaHcDcKkVYfmbwr58OdJgacsXAAbtz7AGV_G5viQ3h43u7AodtmgMQx7HTYPOM2ksnRQ9IDTldza3QeFcRHOEqC-nCUIrfYwVTdwJWDXR_Dw6vSqunPEbJp1Ww0H93v26B7xwi-9J9ynWN5xRAy60iEGxG0sfbAvd_8B-O2f4XligVggokElKIGSk0t-Sp32U-GJOme7JxJBQjxn0jcWvKm2PPRq8b5YXfgS1e5fEqTZ0nKWK-Mg6mFvGCPrQvhPYsEJLUIVM-zTt57k7dnrmigt51av5VaARw9XdnZItW-OyZHzubk6zdPysROGHhQdLYhdHiblGFdqqD2k8SwkkXdS4jbK5jdXX275kYpaQ3o7ImvjUJesmvEZ2-_WRtxsjfg2WfxiSbj0VKMmYwiDuHBgDpocSH77pL4AFtH6C_p5ylxV-iQMlNbX43IWWetwN1MbJUa8usDVJDdv-h84r7dbjyGgxBqlt7RXVWK3nHEvBM0ZURawa-p3QPjL3v5AajLz4DW0CksdfT2It8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از پیرزنی که با واکر خودش را به رژه جانفدا رساند تا مردی که با خالکوبی اصرار به اعزام به جنوب برای مبارزه با آمریکا داشت
🔹
دو روایت جالب سخنگوی جانفدا از تنوع و تکثر مردم ایران برای دفاع از میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/691766" target="_blank">📅 19:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24930f261.mp4?token=pIniFqm0EQTVe8xqDc4oDPg-DlMjBRd0qbRAkL1hkdAorDMZEheo-kLLHvOkqbZJS-vkqx5NgHxnSq84I5jpQhHRKEOob3K-bnHu1gDK9PCIqjzRG-toCdBp-VyzYEiLejhdCquIEAOV9CLArmQ27Ozy7EpXtQtVZtX9hN7g0KJYSuCiQDVdEN-ij_FQDp5HyyyzWC49MRI-OTHFaFWIXruAaHHNpVsnBWalBiG3x8QrnACAL0KRtgeJCPn2AvhWphvMSKpKl1_p4EcYS007wvvR4xhkOXeCqzRfRK-CrA4tIjGq6_C5dzTQXQVqSsMpaRUVMqzujwmNw0ojs7umig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24930f261.mp4?token=pIniFqm0EQTVe8xqDc4oDPg-DlMjBRd0qbRAkL1hkdAorDMZEheo-kLLHvOkqbZJS-vkqx5NgHxnSq84I5jpQhHRKEOob3K-bnHu1gDK9PCIqjzRG-toCdBp-VyzYEiLejhdCquIEAOV9CLArmQ27Ozy7EpXtQtVZtX9hN7g0KJYSuCiQDVdEN-ij_FQDp5HyyyzWC49MRI-OTHFaFWIXruAaHHNpVsnBWalBiG3x8QrnACAL0KRtgeJCPn2AvhWphvMSKpKl1_p4EcYS007wvvR4xhkOXeCqzRfRK-CrA4tIjGq6_C5dzTQXQVqSsMpaRUVMqzujwmNw0ojs7umig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنگام کار در اطراف دستگاه‌های سنگین، فاصله ایمن را رعایت کنید؛ یک لحظه بی‌احتیاطی می‌تواند جان افراد را به خطر بیندازد
⚠️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691765" target="_blank">📅 19:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین دلیل شما برای ترجیح «طلای فیزیکی» به صندوق‌ها و پلتفرم‌های آنلاین طلا چیست؟</h4>
<ul>
<li>✓ عدم اعتماد به سامانه‌ها</li>
<li>✓ احساس امنیت و مالکیت</li>
<li>✓ عدم آشنایی با فرآیند</li>
<li>✓ کارمزد و هزینه‌های پنهان</li>
<li>✓ از پلتفرم‌ها استفاده می‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/691764" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fc1181d5.mp4?token=WpuysjGG_hLJZqsFqu0Ne2fy8XSvPP0GlcXdJUZA4ULM8AU4broCn-3UYvPn8mKkQ93XU9jflgWR3PE3cxLx5GirMBzvxgjpAyjItJYl7Ym81rswfcL22wGvQow3PlYSxmfy--GYmlTwvcavEWANDIadXKc1Q0NnCUuY38E6E1Cn4VTOwNXfDImYcb4y70C76Chi915RpxQVIN6gIFF0jZGN_FTIpUhH1mpi2X5t_871xYxYupa_W8r3N6w58StTYBI3BmxUAybaL2ixaQcLV4tETGyDudDYWrZsuZIy7ZAWaqML6NyeG_hLU6V6eCoNJZ8vqMQtgXwG8MLt35inCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fc1181d5.mp4?token=WpuysjGG_hLJZqsFqu0Ne2fy8XSvPP0GlcXdJUZA4ULM8AU4broCn-3UYvPn8mKkQ93XU9jflgWR3PE3cxLx5GirMBzvxgjpAyjItJYl7Ym81rswfcL22wGvQow3PlYSxmfy--GYmlTwvcavEWANDIadXKc1Q0NnCUuY38E6E1Cn4VTOwNXfDImYcb4y70C76Chi915RpxQVIN6gIFF0jZGN_FTIpUhH1mpi2X5t_871xYxYupa_W8r3N6w58StTYBI3BmxUAybaL2ixaQcLV4tETGyDudDYWrZsuZIy7ZAWaqML6NyeG_hLU6V6eCoNJZ8vqMQtgXwG8MLt35inCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به معاون ترامپ: تا کی قرار است آمریکایی‌ها این قیمت‌ های بالا برای سوخت را بپردازند؟
ونس:
🔹
تا زمانی که ایران صلاح بداند. ایرانی‌ها عامل گرانی سوخت در آمریکا هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/691763" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای رسانه بریتانیایی امواج در مورد جزئیات شروط هفتگانه ایران برای مذاکره با آمریکا
دست‌کم ۵ شرط از ۷ شرط در تفاهم‌نامه اسلام‌آباد هم مطرح شده بود:
🔹
آزادسازی دارایی‌های بلوکه‌شده ایران
🔹
پایان جنگ در همه جبهه‌ها
🔹
عدم مداخله در امور داخلی ایران
🔹
توقف حملات به خاک ایران
🔹
رفع محاصره آمریکا علیه ایران
🔹
یک منبع سیاسی ارشد: این ابتکار جدید است و هیچ‌کدام مستقیماً هسته‌ای نیستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691762" target="_blank">📅 19:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691761">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مصرف برق فیلترشکن‌ها ۷۸۹مگاوات است
مسائلی، دبیر سندیکای صنعت برق ایران:
🔹
در حالی که مزارع و شهرک‌های رسمی استخراج رمزارز نیز وجود دارند، بخش قابل‌توجهی از موارد کشف‌شده مربوط به فعالیت‌های غیرمجاز است.
🔹
بر اساس برآوردها، مصرف برق ماینرها حدود ۳هزار و ۷۵۰ مگاوات عنوان شده، رقمی که تقریباً معادل ۱/۵ برابر ظرفیت نیروگاه رامین اهواز است و همچنین فیلترشکن‌ها نیز روزانه ۷۸۹ مگاوات برق مصرف می‌کنند./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691761" target="_blank">📅 19:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691760">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
هشدار وزارت بهداشت درباره واکسن آنفلوآنزا   رئیس مرکز روابط عمومی وزارت بهداشت:
🔹
تاکنون واکسن آنفلوآنزای معتبری در شبکه رسمی سلامت توزیع نشده و از مردم میخواهیم به واکسن‌های خارج از شبکه رسمی اعتماد نکنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/691760" target="_blank">📅 19:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691759">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e691b28e36.mp4?token=VNz9EZlkytS8xhHP48MOcaRm54esK_p1oMnggEud9la5F7m1d31bFWFsacykuy6Rrt0xiZQLnFcQFMdHKauRqOFqjv97k5y1h1v1JXwF0bnoEgQuu8np2RggBI05radkP9FRspnXERRzoVo6f-XwkG8A_xzIfaJU7dnmXmHcPeRRnX502PqFqdVOJB0zYI_jAeKLOHTqiF8QFGG89CXvO2EkuUXEE4-kx5V0z0dwdWIQ4acan1gA_dhLTqTmd7c4thXGFkVgES5-YyUtB_Gny1px8Yo_bH43ej_fppdi3oTfWWOzwfmx9yz2apR5-vOtqUZCbLdUKFlL_fSacThouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e691b28e36.mp4?token=VNz9EZlkytS8xhHP48MOcaRm54esK_p1oMnggEud9la5F7m1d31bFWFsacykuy6Rrt0xiZQLnFcQFMdHKauRqOFqjv97k5y1h1v1JXwF0bnoEgQuu8np2RggBI05radkP9FRspnXERRzoVo6f-XwkG8A_xzIfaJU7dnmXmHcPeRRnX502PqFqdVOJB0zYI_jAeKLOHTqiF8QFGG89CXvO2EkuUXEE4-kx5V0z0dwdWIQ4acan1gA_dhLTqTmd7c4thXGFkVgES5-YyUtB_Gny1px8Yo_bH43ej_fppdi3oTfWWOzwfmx9yz2apR5-vOtqUZCbLdUKFlL_fSacThouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اعماق حلقه‌های زحل، قمر کوچکی به نام پن (Pan) قرار دارد؛ قمری چوپان که به‌خاطر برآمدگی عجیب استوایی و ظاهر شبیه بشقاب‌پرنده‌اش مشهور است
🪐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691759" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691758">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQg5-0xVmcbDUXKxBGiuAhLFRI1KGFSiilxbrebCyCsN0SfA4iT-Rtr8OzgKkVk0iGUVk0pcJrVqJYHjqRSdt51C9DIvgNiiw-6HZTfUs9Bc4AZi6uaZdyewqU9Px9RvnbVCpnTsId45vOdQv7z2Oj0PNRV7-firPsrw5Tk6E2WHPsiUWf0qFecMmF5j0doAk_LTRgvVs8VoRB7QjYYnvxFXunwkr-wNDvXidrfrS-Rii7mQI7kXGmqIymqI6k0294-3psfNUxH6VzvPB8h04LwhAD1adJVDFWYpQj3vFazxCrjit5722IBib6uXy-Fyj15vIm_MqVqEP-vWtMhS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه فرانسه: ما تصمیم مقامات ایران برای تعطیلی مرکز زبان وابسته به خود در تهران را محکوم می‌کنیم
🔹
سفیر ایران را احضار خواهیم کرد و اقدامات مقتضی را اتخاذ می‌کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691758" target="_blank">📅 19:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691757">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای مضحکانه نخست وزیر قطر: ایران صلح طلب نیست!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691757" target="_blank">📅 19:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691756">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df374921dc.mp4?token=XSIK3JNBQqO-ZJzIoVfefL6yqeIbuyUDdUv-4X_z0BM7CQCrHQMTZ0cg4xkM5LAf8a2i-LFSoH4m5Vrd6aDs8DsfgLnvTgEiSPtFKDYbZ2Ao_YXf2hmXin99mXn273ljVuabjBlTy98wpPY2Lr9YU0r2wxucLRL5SpRVwOd4-RB3J6ACRIGYwtew3FNz9-QlBZpwlguHmClPSlH2PM6DSagUg7MyDVnI2jy9C7p6fypBy260WAJkahPV3OdWJLXSLxY4-GXQV8BAJ2Ms1b3UBttMjP1hMxern_Ko07qRtkIJXOnRMnzRswdKXVJAqvdpbVPJ-WSrWuGW1J7g2KHHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df374921dc.mp4?token=XSIK3JNBQqO-ZJzIoVfefL6yqeIbuyUDdUv-4X_z0BM7CQCrHQMTZ0cg4xkM5LAf8a2i-LFSoH4m5Vrd6aDs8DsfgLnvTgEiSPtFKDYbZ2Ao_YXf2hmXin99mXn273ljVuabjBlTy98wpPY2Lr9YU0r2wxucLRL5SpRVwOd4-RB3J6ACRIGYwtew3FNz9-QlBZpwlguHmClPSlH2PM6DSagUg7MyDVnI2jy9C7p6fypBy260WAJkahPV3OdWJLXSLxY4-GXQV8BAJ2Ms1b3UBttMjP1hMxern_Ko07qRtkIJXOnRMnzRswdKXVJAqvdpbVPJ-WSrWuGW1J7g2KHHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند بامزه گربه پالاس برای گرم نگه داشتن پنجه‌ها در سرمای شدید
🐈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691756" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691754">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np6dGwePE9kbXDVeOb2HgcYkKdh3sDl0T-vhgI8T_g8EPaQklpwAewfLpKN7MiGab6qP6May93wl4LieCwmaXt2Jr1In0fCnHBQ5ErEcwm9YA9UU8oPCAAfwZLDMS8KLTXAjPZGqZxLiIizmiHyaFmuhHTzHsySOne4T84l23sZsY960gTrN23r9TQ9aFJFmxpe-Tu7fa9OWxkjF0q_EqaD2KZSdwEUgm_6rEL-XP8K6cPHwyuUZfD02o5Rbl5vX4zIvDl73B9oR9gs0ErSyJi9DH1Ugu6fm6pmeXxWbGCytA4zUM3lJoq31koHFIO3VHnYcXrEtAxjHZa3BNMctlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpN0K156AKa1L_kknZY0iKh8udTthOODNIcjFb6vIR61P9VPqmgfg0C0fvEHHT0AgD8OBqpCe_BAwznyAh1WaogcLdSn0ml35yBfrEbHhSQV7_Iz02HakEU3sPxTdD2i7AAAta0o8g0oYqKLTyw2F1rpyRU2b9TkjtaCuA6eh-CZTJrP1Lg3CHakpFLEXOhlVPd18ccwKpT7ZFjO_WbuVAca1EyV7Z71IqUT-wAqQXG-Vezi44Ccug9fRnmQ1PckfXK9zWyHESsgb-7SGLBtdAAxdhxHfyo1yD8U2UpcmOoAoKHdE2V5OdxgnWd6gGVbkxRQ_sX6b-P2kaQIWr3X_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گلایه شهروندان از نبود شبکه فاضلاب شهری و خطرات چاه روباز در کرج
🔹
باسلام، حدود ۲۵ سال است ساکن کرج، انتهای گلزار غربی، خیابان چمران، خیابان قائم، کوچه محمد هستیم و متأسفانه همچنان از شبکه فاضلاب شهری محرومیم. با وجود بیش از ۵ سال پیگیری مداوم، پاسخ مسئولان این است که فعلاً پیمانکار نداریم. در حال حاضر فاضلاب در چاهی ریخته می‌شود که دهانه حدوداً ۵ متری آن باز است و هر لحظه خطر سقوط اطفال وجود دارد؛ ضمن اینکه این وضعیت باعث تجمع انواع موش و حشرات موذی شده و مشکلات بهداشتی جدی ایجاد کرده است.
(محمد شاهی)
📍
استان البرز، شهرستان کرج
🔸
ما در  الو فوری همراه و صدای شما هستیم؛ چالش‌ها و مشکلات محله‌تان را با ما در میان بگذارید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/691754" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e9f43c61.mp4?token=U12PRbcyJEoQZHVem2q1RCg342jt0q7j7Us2XFQXYwhqIKYzxQChzdPQRQzh9TQx9i1qVoEj4C6-tQi2lwU-czpnznefnHQBZm4EK413tsf7GmrpscfrjnurHyeZXfuGUOedMoKoJUnIqCe9fWhwP9crSHISqMFfk9BM6NzSdRs1go7AyxJcMFX3-WrOhKN-JBiMJUZE4ZE1X3fxaItD_I7OP94b15_u43mpyvdm3cS2RbrJSdFj5TU9E-_d8KJKJw7s5gGPbsYmfuRkH0iSe2Oho8S1yNJwJToauCu-2U2yOl0GA4rFboWgo4xo7wPubnUX053ArWEmCg8Mnw104A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e9f43c61.mp4?token=U12PRbcyJEoQZHVem2q1RCg342jt0q7j7Us2XFQXYwhqIKYzxQChzdPQRQzh9TQx9i1qVoEj4C6-tQi2lwU-czpnznefnHQBZm4EK413tsf7GmrpscfrjnurHyeZXfuGUOedMoKoJUnIqCe9fWhwP9crSHISqMFfk9BM6NzSdRs1go7AyxJcMFX3-WrOhKN-JBiMJUZE4ZE1X3fxaItD_I7OP94b15_u43mpyvdm3cS2RbrJSdFj5TU9E-_d8KJKJw7s5gGPbsYmfuRkH0iSe2Oho8S1yNJwJToauCu-2U2yOl0GA4rFboWgo4xo7wPubnUX053ArWEmCg8Mnw104A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اراجیف معاون ترامپ درباره تنگه هرمز
جی‌دی ونس:
🔹
با وجود وحشت‌آفرینی روزانه ایرانی‌ها علیه کشتی‌ها، ما همچنان شاهد عبور حجم قابل توجهی از نفت و گاز، از تنگه هرمز هستیم.
🔹
این در حالی است که بر اساس گزارش منابع معتبر دریانوردی، تردد کشتی‌های حامل گاز در تنگه هرمز به شدت پایین آمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691753" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0083ab04f.mp4?token=YWpVOdVH3fSDwkVPW_IO2yNahgFXPCzkWJ387PmrpVy6X6IrEFONzc4zXuuSv4ZqZ9SoDs79MJEx_PStnCqOqdizEB3mZV1PE2Z4Igm2PR4fzFSE4JCKKliBXf5us4oZT3TsDhuP15RYaSiSjdWwg6gRAsWnVMnexz3bSaauv5E58NTTTOkHYvlp_LDAuza0rwqoQxJ0YIaBBy8BZHrF7Kt5ux9NZlnC5nQDtzE9ppkyXeLDFQRtURT3IXBXw6nyumLHQOsmWUZhRVEHhtzYcN1etxl-xAYBfylB0LLkcEHkZBxPs94JXIzUSJqJ3Sq9pa-aVcgKTS2c6EY0iA420w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0083ab04f.mp4?token=YWpVOdVH3fSDwkVPW_IO2yNahgFXPCzkWJ387PmrpVy6X6IrEFONzc4zXuuSv4ZqZ9SoDs79MJEx_PStnCqOqdizEB3mZV1PE2Z4Igm2PR4fzFSE4JCKKliBXf5us4oZT3TsDhuP15RYaSiSjdWwg6gRAsWnVMnexz3bSaauv5E58NTTTOkHYvlp_LDAuza0rwqoQxJ0YIaBBy8BZHrF7Kt5ux9NZlnC5nQDtzE9ppkyXeLDFQRtURT3IXBXw6nyumLHQOsmWUZhRVEHhtzYcN1etxl-xAYBfylB0LLkcEHkZBxPs94JXIzUSJqJ3Sq9pa-aVcgKTS2c6EY0iA420w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کندر را بهتر بشناسید؛ از خواص این صمغ قدیمی چه می‌دانیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/691752" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmtEWdRrmQXbX4HH2QUqwdkXo8h11DnjcU5PgEI-aGDuUboEZzDRvQL93ICZ5prng8qMF1zDOB6VJ79RMZOEnU7_tHZT9EKochXXpY0NGP9w-yDgGeao3MrmJwU6G6tyEw0a67ISKxkzBo3yh8X9J97xrduIeGDBGnxGFlcxK165L1D-tZUGdwouKQFRG2izTAXFEAMgb2vncmIhlkSTik1Y_90yYqP0UHi19xEealOQZGoYsWn-7OUDXiZfWrJ_awNmiCuAxKcKb-0r0upu9L0ROcLwga6gnPE9I_9eVkrtcxaCvVWGs1HM08aKRqRqUt4BBoc_kvKS0z4F4LPxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به مطلب نشریه اسرائیل هیوم؛ وقت آن رسیده که واشنگتن خود را از این غل و زنجیر رها کند
🔹
لابی اسرائیل دیگر ابایی ندارد از اینکه نقش و نفوذ خود را در سیاست آمریکا در قبال ایران آشکار کند. در نشریه متعلق به میریام ادلسون، که بلندگوی این لابی است، صراحتاً  گفته شده سیاست آمریکا باید به‌گونه‌ای باشد که در قبال هرگونه بی‌احترامی یا تعرض به اسرائیل، آمریکا نیز هزینه‌ای بپردازد!
🔹
وقت آن رسیده که واشنگتن خود را از این غل و زنجیر رها کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691751" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
عربستان به دنبال حذف ایران از جام ملت‌ها
🔹
گفته می‌شود برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانه جام ملت‌های آسیا تعلیق کنند. این یعنی احتمال حذف تیم ملی از جام ملت‌های آسیا وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691750" target="_blank">📅 18:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
هواپیمایی جمهوری اسلامی اعلام کرد پروازهای تهران، مشهد و اصفهان به مقصد فرودگاه نجف طبق برنامه پروازی در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691749" target="_blank">📅 18:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCUlxHUuI-DTuytNMWejMyHe5UbOr8a_RbpioT6uXwZt6ciALL6lN3Jtgro2EPpkfNl2PulI_PqbFHqEF9RRzs9OriZsD7S45R-tbXOUyQ9z0eVKiD-5AaW6dG8wUAn8qOdLBaoey-lEIfYqS1fObuILdeg0CVm4na5nYSBKz-z6UFqk35aZ1F82xxjjxV9XU47fYYIs6FHZD7D-fuqq1WyEZ6Cn4cjbmNp3bUxd7xyPZc2ewvwVEt1rBJ-Q1Hgwnx0dtN9z7MMs2aqv5A38Wqqq_2JzsGwUVO9ps-lssfp9kwPnr7Gw33OCjgfp4YKRT4fiYNpP3vbgSlZVMGHyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت جدید برای کاربران | خرید طلا و نقره با کارمزد صفر میسر شد!
🔹
به تازگی متوجه شده‌ایم کارمزد خرید طلا و نقره در وال‌گلد برای مدتی محدود صفر شده. کاربران برای خرید این فلزات گران‌بها دیگر هزینه‌ای بابت کارمزد پرداخت نمی‌کنند.
🔹
به این ترتیب، هزینه کارمزد از فرآیند خرید حذف شده و مبلغ پرداختی کاربر مستقیماً صرف خرید طلا یا نقره می‌شود؛ تغییری که می‌تواند برای خریداران این بازار قابل توجه باشد.
🔹
بررسی‌ها همچنین نشان می‌دهد وال‌گلد به‌تازگی همکاری خود را با بانک کارآفرین آغاز کرده است؛ همکاری‌ای که در کنار صفر شدن کارمزد خرید، این پلتفرم را به گزینه‌ای قابل توجه برای افرادی تبدیل می‌کند که به دنبال سرمایه گذاری در یک پلتفرم امن هستند.
خرید بدون کارمزد طلا و نقره!
خرید بدون کارمزد طلا و نقره!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/691748" target="_blank">📅 18:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رهبر انصارالله: تمام تلاش رژیم سعودی در این برهه، وارد‌کردن ترکیه و پاکستان به جنگ و آوردن تکفیری‌ها از سوريه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/691746" target="_blank">📅 18:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: رژیم سعودی، فرودگاه‌ها و پایگاه‌های خود را برای پرواز هواپیماهای جاسوسی اسرائیل به سمت خاک یمن در اختیار صهیونیست‌ها قرار داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691745" target="_blank">📅 18:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فایننشال تایمز: آمریکا و چین بر سر تمدید آتش‌بس تجاری به توافق نرسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/691744" target="_blank">📅 18:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cucza4pX6RVosXAQVlbaoZ9PHYN4j9OF1UniAVR4-deO0J0DKgjc5by8BwATPxeVcS0PUm2tqQuSXkbEuz_7Puh-GRzQPzsYc1wtV3G14hAV9Vt-PJI53vT0YGdff7EVUNIi2xrZ2oZ8DOOy_9fLbQJNuw7nNu-Bpt5PaE9_uxRNBvhRWbKblZSFVOHUOM82vqsE3JfStA-Ak_4xDEB9uqmHn-psn-dupx4xA_WWPZP6unbOWUh-ICp5PQ1Dihsp8tJ2u8pmrxzd3P87hpO0Ha-QBw1PscAf7YUx104XfmikdU_rAumRrAqobmdWBPw028c9NREQuzCcSLapf9RgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوتمیل تیرامیسو؛ یک عصرانه یا صبحانه متفاوت و خیلی خوشمزه
😋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/691743" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf82d6f38c.mp4?token=b8KsLFDspjqUDEi1AST7E8eAU8lZKFOSmVYFU-A7CL1j9aAtkoX67VzmWW9Ykl8mhERlF8CTZSI0oM5roeXmwWXRFhYEQ4c82760EZJc8UH6pP9qEbCpsaSU_YgcPI9_RU__NKfGJqDj0cTSuSOaoN1sny3-IFkZ_vg1xiJMr1J8wS6KCcJ_D3bnR9O8QPp_ktkVmUiPConpBXJk4kInDoIu_8xwSG5rbTW6LylAHP7-kmHDJGprIckkKAkCyvl0Dj_83d4iu39xEfS6HFb8Sk9ADyaI5fY-1D5bdauAyb33Peipz6IfP0oqX2Cb8WX8LzgU0XzG9IskVrWAfw4kpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf82d6f38c.mp4?token=b8KsLFDspjqUDEi1AST7E8eAU8lZKFOSmVYFU-A7CL1j9aAtkoX67VzmWW9Ykl8mhERlF8CTZSI0oM5roeXmwWXRFhYEQ4c82760EZJc8UH6pP9qEbCpsaSU_YgcPI9_RU__NKfGJqDj0cTSuSOaoN1sny3-IFkZ_vg1xiJMr1J8wS6KCcJ_D3bnR9O8QPp_ktkVmUiPConpBXJk4kInDoIu_8xwSG5rbTW6LylAHP7-kmHDJGprIckkKAkCyvl0Dj_83d4iu39xEfS6HFb8Sk9ADyaI5fY-1D5bdauAyb33Peipz6IfP0oqX2Cb8WX8LzgU0XzG9IskVrWAfw4kpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله وحشیانه عربستان سعودی به یک بازار محلی در تعز یمن
🔹
«ضیف‌الله الشامی» عضو دفتر سیاسی انصارالله یمن اعلام کرد که هواپیماهای متجاوز سعودی، بازاری محلی را در بخش «ذوباب» استان تعز هدف حمله قرار داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/691741" target="_blank">📅 17:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: با چین درباره ایران مذاکرات پشت‌پرده داشته‌ایم؛ نمی‌توانم به شما بگویم این درگیری چه مدت ادامه خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/691740" target="_blank">📅 17:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شهادت یک مامور فراجا در ایرانشهر
🔹
بنابر اعلام منابع آگاه، یکی از نیروهای جان‌برکف فراجا در حین ماموریت بر اثر حمله تروریستی در ایرانشهر به شهادت رسید.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/691739" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان با چراغ سبز و مشارکت مستقیم آمریکا و صهیونیست‌ها، در یمن جنایت جنگی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/691737" target="_blank">📅 17:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhPRdICAH8ScH8BGhOQ0V4PhhebiedeIb1Gs1iB-3LX6F7vTvd-g6idCt29kGC7hS0aQw17VjbH5S273xJy-hfppfNr5oAtZsWiMPaIC3e0sWGqWfQyg0x-nuJ55DYAq3Njtb2xuz-IeJoSAUs2IEhxnH-BlqtS9aaOVA5etfqZE7DOJk7y4LAkeZ66BkncAvLa7h02p7J4O7yESO7_-YvP53jJLZpEFDOA9FfHVSoWi_oyEVLDNTM4Kv_WeWD-ZL20XALckuFPDYKk05AeNiPHCzKgOJx2OpN_Y14XPjMGcMnTaIotvts9_L7CWgZ1RiTZxvlJKn0-gJ7GFgfxFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های پنهان در «پا» که نباید نادیده بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691736" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان با چراغ سبز و مشارکت مستقیم آمریکا و صهیونیست‌ها، در یمن جنایت جنگی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691735" target="_blank">📅 17:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین دلیل شما برای ترجیح «طلای فیزیکی» به صندوق‌ها و پلتفرم‌های آنلاین طلا چیست؟</h4>
<ul>
<li>✓ عدم اعتماد به سامانه‌ها</li>
<li>✓ احساس امنیت و مالکیت</li>
<li>✓ عدم آشنایی با فرآیند</li>
<li>✓ کارمزد و هزینه‌های پنهان</li>
<li>✓ از پلتفرم‌ها استفاده می‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691734" target="_blank">📅 17:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyHOaLNlWWurACaLW4aEqhXAqT_OnAnql3SObNwRy7FyUtFmHeCBVldiKQ8ehs_YVGbfqWG3m89Xo3pWIrC3hp7_jaTYp0ELVjOEP_Ial6ZGC2knfeAFBFNkn1AnwG4O8DE7-6sNYo0xrOCxm00tXzKH4XR2ReJguB2-8Bbl7qchjwVc7eElRk8yAcmi6Zp51z94837vBed7WoRxSEybdwRXTLBM0b5Wbp6SdGcawSHl_oQzNiMpaC8XO2CoDIW-ImpdvmoLy4xTYP_sMxD2Kwjx9r3rGY2v_ZpWrh0Ywgxug6V8fPmCmre28xKLRMmJtm89n7qTQU-gTgYYQrrzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواشناسی: موج بارش‌های پاییزی از روز پنجشنبه وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691733" target="_blank">📅 17:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2tl_C_U25tgIez29LGb8xdx1KcUi9HSfJEFneTROi6qiymuBHfSu_eyuK1WZuPZZ9gztZ8d7UKiBvtp75A-5AUHbNQimHVgjUT7GEKIF8Z_CHBLT8ec-l3dOvY-fDrobJW75rD20PIlo3bF4f2KhEmm_6J8ExaiAkZHJIap3xqWwXX-Ycu1O_V4rtbp9mkGY-unuVRMTPGWorQAsNgdNoeO1a6S1HlhfyzcWT2eaHwRmQ97UQbs2_WaqhnadSU--S6LLXij_Adbrc5hskLb3y4rQ-TRnOGz2r3eLUb6ZLjoSwN4l_nZch5boedoaS8khf7Vr7NbL8-mJBCESnHQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش قیمت نفت به ۳ درصد رسید
🔹
نفت برنت ۱۰۰ دلار
🔹
نفت آمریکا ۹۷ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691732" target="_blank">📅 17:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شهادت یک مامور فراجا در ایرانشهر
🔹
بنابر اعلام منابع آگاه، یکی از نیروهای جان‌برکف فراجا در حین ماموریت بر اثر حمله تروریستی در ایرانشهر به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691731" target="_blank">📅 17:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a79612931.mp4?token=PTrZhKD8YvTbsyMpRfbnVWtpk63l_iKOig2NeceS6SeB3sqh69douRz46o2FqtZS3xW7iRgxi3SPOuKnXaZBZIPivNCzc_GQ9E4DYONAFfGMtP01xuU1a_vq7-N7ccGJezS_9a3cBUK1UegMrPa3jOImLtCH2DpA-8Z2udfbApK7JlCx7SV678ICNAnjRFidMeRuxZ8gJuCJyn-j6GaaG9QIlefkO6UbZlSaTEaPM2154D87SmC-Lzt7pSAuV1NL9ThcvhPyeUKB7a9jPUZKm7iz6X__uwqDnaQr3iEAneHDu6gRYfyMtGUE4Sxn5S3ABAAbeq-TR6thO9lsepskfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a79612931.mp4?token=PTrZhKD8YvTbsyMpRfbnVWtpk63l_iKOig2NeceS6SeB3sqh69douRz46o2FqtZS3xW7iRgxi3SPOuKnXaZBZIPivNCzc_GQ9E4DYONAFfGMtP01xuU1a_vq7-N7ccGJezS_9a3cBUK1UegMrPa3jOImLtCH2DpA-8Z2udfbApK7JlCx7SV678ICNAnjRFidMeRuxZ8gJuCJyn-j6GaaG9QIlefkO6UbZlSaTEaPM2154D87SmC-Lzt7pSAuV1NL9ThcvhPyeUKB7a9jPUZKm7iz6X__uwqDnaQr3iEAneHDu6gRYfyMtGUE4Sxn5S3ABAAbeq-TR6thO9lsepskfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/691730" target="_blank">📅 17:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c109d1fe1f.mp4?token=e7FX9jsLt0MjyqaAmWdUOajXsAneJWXKUoiHgzCo6gyLAPqfcmtfj4KxDp2y0QE7cbRkNa8BpGOID4LLk9IppHxyLGtZfo1jK8Ui5KJKyCm9xIfi_YGgKnzaY2u039qWUfQFCjXxFwjfFbI-jrz8kSxyJnJ6TqOAOxq1RTHYvEZSDNetKZomCaZjDuXRCVpmjVumkr9cAcRWZd3MjfnakwtdQs3PYdry_nHVX-34nh1wqCfViWM5nxv_QJAELSLjCVjBg9VFKVeHTwkcusTubUK8AeY7x8dWtQUPGspXFd93cpdDt8xUZmHpf2fVFky92kGE3dz96BcUFVkEgnrHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c109d1fe1f.mp4?token=e7FX9jsLt0MjyqaAmWdUOajXsAneJWXKUoiHgzCo6gyLAPqfcmtfj4KxDp2y0QE7cbRkNa8BpGOID4LLk9IppHxyLGtZfo1jK8Ui5KJKyCm9xIfi_YGgKnzaY2u039qWUfQFCjXxFwjfFbI-jrz8kSxyJnJ6TqOAOxq1RTHYvEZSDNetKZomCaZjDuXRCVpmjVumkr9cAcRWZd3MjfnakwtdQs3PYdry_nHVX-34nh1wqCfViWM5nxv_QJAELSLjCVjBg9VFKVeHTwkcusTubUK8AeY7x8dWtQUPGspXFd93cpdDt8xUZmHpf2fVFky92kGE3dz96BcUFVkEgnrHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دستور انتشار اسناد موجودات فضایی را صادر کرد
🔹
در پی اظهارات جنجالی اخیر باراک اوباما درباره وجود موجودات فضایی، دونالد ترامپ به نهادهای فدرال دستور داده روند شناسایی و انتشار اسناد دولتی مرتبط با یوفوها و حیات فرازمینی را آغاز کنند.
🔹
ترامپ در این…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691729" target="_blank">📅 16:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
پزشکیان فردا سه‌شنبه عازم نیویورک می‌شود
🔹
مدیرکل روابط عمومی دفتر رئیس‌جمهور از سفر فردا (سه‌شنبه) پزشکیان به منظور شرکت در مجمع عمومی سازمان ملل خبر داد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/691728" target="_blank">📅 16:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691724">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkVroOGVyr860ibar61TZvWjf4fuFT_1TRfuhFkRrFeXVAzLmQXQ0OGTqUD2qMTNkk_X_qeFazDZoBSrkfHPvdAZBXsDXCdGmNLnrYbU2h_3D73JV-xy7B-pPdiF0xNPgV5ehE51Vpu8a978W-1IwDOxKzpbDAxIlKOxilUK4BadklGqz5PMEPll2k4-EOBgzQZCJc34f93JdsDb-VLj4eQA14yj7Hzem-8MhOCO--u87LQtCa0GL7AwRjdSd6ZgaKSE3VnnK1xq_RiYsZlAMS_gVEup-FAIAlvYnA9OolzAKPKpxYWEgLyU8H3nwoBeDVg2-vIRSwQAcvf3q8C7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAhCqwoKq_gK_nJ4ZM-57gaVwaz91FIvQ6vau3uzpdv_WLKnbso635A4L8LzYfIDiArJT4mYnS6A1K0ge-coLLghEY5xao3JsAzFwRNeUruLF6W1iY5YHXLGH681BrB2_eJbX771pmH1IkYH6gUDht-Y_H1dFjRFx5hSrgzSOM1UBc1xX6XSn2z2lC4JysxASjKrRV4YCGONBcfkP0PYBM0uo3pFUntqAiWK_BBDIoc54hk1OxT-xGwnKS_7xczp8wEn7OPwCTogjsbfjINrGLyvHMSaa08U6rjBvcT0mdh5Ll9djn1QoIdQzQjgm3tJsuPLXKgg1Ef6Mi8QCAm5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUvDQSYYcid1zRR8hFxo5bP83AVHNuTzgaSxlHyJit9xRPCpsxwfxqTcOMBqH_i0X_02FhPNJEFIt4L6OIqLq2WJxa7jWZ0IfK4BBLy6j6b3OM1eHb-tLpDOcWfnCq2lLqPpl4I28vA27USPCv0W_-OzcfNZu7L0m0F8MK0BEN9_yzVHEDXGH8A6yzptVQP3UAlacAqr2gSJgBAef_TiGKSPS59hJ257E3d4fbVQ1_rzCvMW-PiuqcYKi2p-OYh2nWjGL30lY87sAOkpzfKLX-ArGBu9hsrY6_pqtha2mA-fxzQutz7qSmaa7yVTYeqBhOJFBvZd13-g_LPAVEBFIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4fc52ddd.mp4?token=Ee0uqoc6FmKMAs6NSv6w9hqEnfs3trS2U74DZI2BiAvSfaGM0Gyn18Gck5wSMFkAQ2lSSVTnfBKAxxO9Tvis0X8OCUodfG9bbFCNwGUotdwrro51ZkTIWC75XgpJlVAUFUZueDC3drixawd2BfTD93qkQJJSrLAlYTo43q4p52J10ur8SE-lE-nmH_jR1_NxuMCqiwnvhkvUIjZ7qjulJ-oJgCrvpVsMCBFmPWaMxMpD1Gl81c4s61htZrbYutfT-9wMyvpkja_9boajvvrbWoCxuaSqgTGKbk_rUsUTy_USigNq2cPI8FTSOEH_Ia-zhSWpqcYU4HIXI4W8QorYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4fc52ddd.mp4?token=Ee0uqoc6FmKMAs6NSv6w9hqEnfs3trS2U74DZI2BiAvSfaGM0Gyn18Gck5wSMFkAQ2lSSVTnfBKAxxO9Tvis0X8OCUodfG9bbFCNwGUotdwrro51ZkTIWC75XgpJlVAUFUZueDC3drixawd2BfTD93qkQJJSrLAlYTo43q4p52J10ur8SE-lE-nmH_jR1_NxuMCqiwnvhkvUIjZ7qjulJ-oJgCrvpVsMCBFmPWaMxMpD1Gl81c4s61htZrbYutfT-9wMyvpkja_9boajvvrbWoCxuaSqgTGKbk_rUsUTy_USigNq2cPI8FTSOEH_Ia-zhSWpqcYU4HIXI4W8QorYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگزاری نمایشگاه کودکان میناب مقابل مقر سازمان ملل متحد در ژنو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/691724" target="_blank">📅 16:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691723">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17217aebf0.mp4?token=FMy_KoJl7uxgUU5EqHua5BMPjTI0sFPgfdZuMC1VHkisDar2aB5_wHyC0liKJm88FS_tHNgv6ePdFzze48zGSZyI4nFM6pUH4dYFLswLRa4wpXXDn1gGUeLcM18BgMqODPlclQgLN0Vcm2_2gInHdnlRNXJcS2cS4zrGwBbXtv0MCuZFCuKjLtElEJlYchWxbWMe-MKEiszrYh8Dib9_dvBJWcwiCqWdMQI2SVLmY8XVkP5e96_B3vjYCHP0WwrRvlBlAI_jg4QvWmCtNOxG1e3rk6INvDuDgvpFwQr_7rO1_ytxaT6ayPlQ9oT2xKXMZxpK7tkfJHElpjjC6Fgb04emmHNpT6d6rMc1gPVf4aBcDt431d4eovW2Srl1yS2ihRsHf7vjZexmizcgJSx9mopYNmjy-yNBTHpxchqrZyRJU2zu7rERJnqjJbik7a2tfLiIRwMmpm32JzYK-saPWyLITC0iYxc7LTiqgSwBgetIB36D2l-cOQmn-nr7e2EnZ9F2_GFzLC5Sd98mt40Ox6gJkvO6bKctXMOIVcyAI9yfcgOBLbzU3SAGBUTmsUlX22BqXEvhsDOA3s66lxwh7sHqv4OhgmZwYtxD8ji4py9L_tEYeiwRg6XPAO6VFiiJSGpqSsj6PWRlUd5jpdgwlpAPNVBrFRvD0Yzv4pk7iiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17217aebf0.mp4?token=FMy_KoJl7uxgUU5EqHua5BMPjTI0sFPgfdZuMC1VHkisDar2aB5_wHyC0liKJm88FS_tHNgv6ePdFzze48zGSZyI4nFM6pUH4dYFLswLRa4wpXXDn1gGUeLcM18BgMqODPlclQgLN0Vcm2_2gInHdnlRNXJcS2cS4zrGwBbXtv0MCuZFCuKjLtElEJlYchWxbWMe-MKEiszrYh8Dib9_dvBJWcwiCqWdMQI2SVLmY8XVkP5e96_B3vjYCHP0WwrRvlBlAI_jg4QvWmCtNOxG1e3rk6INvDuDgvpFwQr_7rO1_ytxaT6ayPlQ9oT2xKXMZxpK7tkfJHElpjjC6Fgb04emmHNpT6d6rMc1gPVf4aBcDt431d4eovW2Srl1yS2ihRsHf7vjZexmizcgJSx9mopYNmjy-yNBTHpxchqrZyRJU2zu7rERJnqjJbik7a2tfLiIRwMmpm32JzYK-saPWyLITC0iYxc7LTiqgSwBgetIB36D2l-cOQmn-nr7e2EnZ9F2_GFzLC5Sd98mt40Ox6gJkvO6bKctXMOIVcyAI9yfcgOBLbzU3SAGBUTmsUlX22BqXEvhsDOA3s66lxwh7sHqv4OhgmZwYtxD8ji4py9L_tEYeiwRg6XPAO6VFiiJSGpqSsj6PWRlUd5jpdgwlpAPNVBrFRvD0Yzv4pk7iiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«این همان آینده‌ای است که می‌سازیم»؛ واکنش ایلان ماسک به ویدیوی هوش مصنوعی از آینده فضایی بشر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691723" target="_blank">📅 16:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691722">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
قطر: تعمیر راس‌لفان شاید ۳ سال زمان می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691722" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691721">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مومنی، بعد از دیدار با وزیر کشور پاکستان: مرزهای ایران و پاکستان شبانه‌روزی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/691721" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691720">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: نیروهای واکنش سریع و مخصوص ارتش برای دفاع در مرزها مستقر هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691720" target="_blank">📅 16:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNXUJP96CsMZAldOmdDG97rlbmj34-u5M0G6WRFPMc9cD0PhGyWEeyRcRarZVLYo6ksP0LQ6nJQX_NuAdDQvVZ7rW0iLmQkRnVMJdnw6B2YVK_4iZFt4CeTo3QGpjBfHBXlH6LExRapFJew2_uGTosCwTe2qY3Hc6nprz2CW3AAqGsC3F4Yb6r7GmOISK2p4SpF7Umxp0jFk8MGYPtGPDvpxz0mPrHp00pZtH3ITzqLzMnIT7EUzJgG1xeLTuNxNZxk0uIwzwH24_FZXG4o8Yb4CgNPZj5VR2gNQt3SQ1iL9oj_SGoeRI2OBJsc9U0ELHPuXsqPzLevlml2PM2Y08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNfZ3549_NsioQh24ncIsqwQQfQpuE3RlnaNn4FWS2zlQLHLSx-izHbswVxX_cKjC7Vhm8FN89KWHtSynsFf076ROrIS86JtMuOpn4E30lbX1MVapM7XmRVLwtnHeFLchXwRTJWwCidSzmloQrGOr_wHuf5tJCqFck_Zo05qzySlDMCdzrP_VtMm1uZaNe7EdJNll4EAGPdCXxNBJEXkMfumfWF1j3QQXZxd5O-mXcPldM9G3Wsww7Qm2uZms7K-WlzSxIHHf2Vh-Vz8C1dM__0TYS-b6f3FDDgVvoH1x347axsv_vqxFKBN-E5L9VRD_T2UAihSTSH9xHKU9gT-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQAMwk6EyCVBxLgd_sNwRBF3dkX4zlbGw_T2G0YeCgOCjZj10JRFA-JSzexVIkhDAOiu3_WQvB66O8MhjXqP4J6cjJ89JXMnq3YWz890lUDdNQRQ1HyYiODUGMGaYzXB_6Njm0Ztb5EjgD4iKYGMbZbJquMRbMUhQsIckkJrophQnrryl_J7kv2NHPhjQmlU7qfPZ_a3AGCiVyyuf2ClFLK6jhM5CMtQzHyoHFU7vkr4L4xWYoXsZH1ocmErnNLQZl3DAoBhY1A5u2jH7ysgWXI-B3K3BUxWd_navje1V9FrkLebMI-sSU0zqv0A1DsSfGtd8M--LDJk3gS1Xw01TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uum92rN1G4552ZsyEIDV4_RBnZUXL8MRere6GeAmU-zTqOyC_Zwet8hHvpaNqPdF0OzEysrIVplksBGbMDWi2jxTqvfHELrqRb9CjOUj7UDRo1eUibp5ctrNb6jtqoqRICqJr81o4ICc097ju7qoMqzjZGUUMIa5Yn-PNtbkWgjnw6QeLED9VO252MAqXsQPHBZnU-vTFNgss5e5Xz_xEb8ITzA0iCRp1p-kEfodzVaRtC6C-eLs4agl7eIqTOi_rawQcZmuBN7eoYoZ2f8w0W6Rak_dmoJS67xcrrGz4GCVuRSr8TqarEEUZ9AjldqvPGt6lb5fYlvzKPv6vLAs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgfkxgwEIcYh8kena3vE9gMXTg9ebBOnQGkEgGJVkYvbaCMKq5oms0hO0MVzQ15Her3bvR6iomzrnCd01GSXugA8bYhYvItdLHjd2H5gMmoLQvXAIXPKB_iEyOdkqHIDqF40mGh_w431QLYFJHHLv7b_u-do_HVg_FGJ5rhTUdKFblw67aVsFLRl5-1V14mvivHaWHnTdVXkOD69a9DyiGvMDV7brzGBYN97zv6ynbT7ugswjbOp867rLlne9Jo1Q87BJ0lkcj1y-qOHfjZFG2AXwll2f1Hbev-nbC6wui10wXkqTINsryqN2w4bNyJ09eQEQkLjskZ5uq3znSAhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMDop64hurt6lckt4oWaObngXnM39F-ysYqnF0ho__7XwFw6NSS60ylQmsP7qkqcnxsjf103vp49BR21jssjTqOSTVr0IXVp0vosPE4MHab8Z85zlwyTgeQS9_YQTNFUc0TXNpkzVRgPHPDhFayFvVjIpGz-TPWCV2OnseXlHDUfkOAuDNiyeSXsI7w4WEJEmcwtr-E2jfXRPxPG05EOH9K1PVxe3Ia71balTH7rVozw1V_ck0kgkzYLFj_g8BOAoW1ONWMpOgMXlwnvgtvwPeuKIe0pGsGr9cJYCRwLSx8Totqk-0rDHVoG9026FV34EnZJVzW4Dwf_zBTz_vdHEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته
🔹
این هفته بازارها چه مسیری را در پیش دارند؟
🔹
از بورس و سهام تا طلا، دلار و دیگر بازارهای سرمایه‌ای؛ کارشناسان، روند بازارها را بررسی کرده‌ و از چشم‌انداز روزهای پیش‌رو می‌گویند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/691714" target="_blank">📅 16:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/528f1dabec.mp4?token=p4DAlbykxuft2dJB3YlN2TV1k2V6s_hArWVZBgoFYRSmFhF3PcWoklrBD65mR5ZPNcxCaS4W-xIDPMfXh_d9QDJEOsUgnoOkeTj1BAplSXSRU7cOkIaAod-LsUyJMRAqOrCHeJMQFAZs6j9e7M1SsxATtUuQ1IGYWJjOZVgHD5Y-GHuaiLkB47AOqu2v9HUwLl0jUjMyLp6fnjdAgjISY8NnaWRlUx-hH1iEEyrpAwMEwl2TFU0bTvKHeqI6WscEKB91m4rgzaZmX-Wbov5i60mo89NpwpBH-bFJULqoBi-JfceOZrbzOmSb9dj7h-7glBuLbwPTqvHbH8M0mVpYcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/528f1dabec.mp4?token=p4DAlbykxuft2dJB3YlN2TV1k2V6s_hArWVZBgoFYRSmFhF3PcWoklrBD65mR5ZPNcxCaS4W-xIDPMfXh_d9QDJEOsUgnoOkeTj1BAplSXSRU7cOkIaAod-LsUyJMRAqOrCHeJMQFAZs6j9e7M1SsxATtUuQ1IGYWJjOZVgHD5Y-GHuaiLkB47AOqu2v9HUwLl0jUjMyLp6fnjdAgjISY8NnaWRlUx-hH1iEEyrpAwMEwl2TFU0bTvKHeqI6WscEKB91m4rgzaZmX-Wbov5i60mo89NpwpBH-bFJULqoBi-JfceOZrbzOmSb9dj7h-7glBuLbwPTqvHbH8M0mVpYcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز   سپاه:
🔹
لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔹
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/691713" target="_blank">📅 16:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گواهینامه رانندگی ۹ برابر گران شد
🔹
هزینه دریافت گواهینامه رانندگی که در سال ۱۴۰۰ حدود یک میلیون و ۷۵۰ هزار تومان بود، در سال ۱۴۰۵ به حدود ۱۶ میلیون تومان رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691712" target="_blank">📅 16:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa8rKX3f2uli_SrQusP1Hr-plbYPbZ_lL1JxYDrzkuFiPaiRI7EUf5tVOK8c_hkXhVX0RfMNrZF1_jS20GOd_tYP0IUJH9_4ZV2_rAfVD0AXNP5MtirEEypN_1NxWRfqsBe7SAZayZ1qCUflz6iZqonOP0Gjbk91eW686qIa6sDfuMPvnb6gNTjDURzLVTdwWZLZcDdqmdre6XZ0bI6jetsNHWOVZTr6yaz1CiHe8wXPhFEU0QaMflDTs8fOBp72PWsq2lR1nonxnOLKeLnV8n4_ycjdZJhDQHIrYEXE-O-sT-4o18IbOIsCcXDPLLGSH-rFkuIVkyOCpdd3SBLfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۴۸ سکۀ متعلق به دوره اشکانیان در دورود
فرمانده انتظامی لرستان:
🔹
در بازرسی یک خودرو، ۴۸ قطعه سکۀ تاریخی کشف و ۳ نفر دراین‌رابطه دستگیر شدند
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/691711" target="_blank">📅 16:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0cf18812.mp4?token=m9O91RMggbTvjtKYf94WVxo2h0LW34v0CXR-jH4zZ9LaQPvkjtoZ5BIOJKRtnVLvQj-fhkCygIzezIFSI3YGufthuilOGYZOSUUFmvrue6p_xjholWBbJ2iWRj8aXMwcUZOEpOGsuYFVst0XLX4HuBvF5UHZ7Hv6Fu247FS6tSdDqzgEi4ThZNbsPNjkzhS2b-nGKVw56uw-ZUwNbCK3pbjA1Tq1VfnTzg6B1ZQbB9VmFpsgXQC7MFgiwrQH74hVp9B0-dTm2Cv1Gb1fbENX-pBC1QlsHY6EX60pxD-exG7QBGSTNW-7PF3iUlqnFP6dXoRvlMtnhQl1LLdCgrfaEReExEwnj6gXmupLLtjK_36UjJeZ-Rl5YcT1rYiLAgT-FW1RysGg4nX4vv6c3D0gTXR8roaxjnWseQ17YCI5ACqq943uyVg1h2WShrofDwDIdk91vNOqdJNmHGwc2b4dQa-yOVv2bbvf13yWONb6tG0xQHgnMc0FWx2pORVLMslO5rhyadWilmuSt_aKcjeKJEoONXkLpbXtUKj_7oyqsa73pEuuRWXeYLJv7QyPSv_ENF64jx8mWxLTDE-QRr4nZsq8NO8lFXw_FEHmTEtCcflS1JLsnsij4DJ9rSuYIMWfjtdDRT4nmJuhLPvLtgxgHncqcE-2Sca3gTliPsQ8V-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0cf18812.mp4?token=m9O91RMggbTvjtKYf94WVxo2h0LW34v0CXR-jH4zZ9LaQPvkjtoZ5BIOJKRtnVLvQj-fhkCygIzezIFSI3YGufthuilOGYZOSUUFmvrue6p_xjholWBbJ2iWRj8aXMwcUZOEpOGsuYFVst0XLX4HuBvF5UHZ7Hv6Fu247FS6tSdDqzgEi4ThZNbsPNjkzhS2b-nGKVw56uw-ZUwNbCK3pbjA1Tq1VfnTzg6B1ZQbB9VmFpsgXQC7MFgiwrQH74hVp9B0-dTm2Cv1Gb1fbENX-pBC1QlsHY6EX60pxD-exG7QBGSTNW-7PF3iUlqnFP6dXoRvlMtnhQl1LLdCgrfaEReExEwnj6gXmupLLtjK_36UjJeZ-Rl5YcT1rYiLAgT-FW1RysGg4nX4vv6c3D0gTXR8roaxjnWseQ17YCI5ACqq943uyVg1h2WShrofDwDIdk91vNOqdJNmHGwc2b4dQa-yOVv2bbvf13yWONb6tG0xQHgnMc0FWx2pORVLMslO5rhyadWilmuSt_aKcjeKJEoONXkLpbXtUKj_7oyqsa73pEuuRWXeYLJv7QyPSv_ENF64jx8mWxLTDE-QRr4nZsq8NO8lFXw_FEHmTEtCcflS1JLsnsij4DJ9rSuYIMWfjtdDRT4nmJuhLPvLtgxgHncqcE-2Sca3gTliPsQ8V-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پلیس انسان‌نما به خیابان‌های چین آمد؛ گشت‌زنی T800 در کنار افسران مسلح
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/691709" target="_blank">📅 16:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb9131adf.mp4?token=M0Zv6131aph5lnCj-d4MU6haLoeVL7dPKQ3OoLmwABsKtISCPyzU34-avw2I-OcOu5YOknevxXp97Xr00JrtV9NIvE6z-KVpdX-fv1Z6t9KHAvx-LJdoBnCyQATuBQhGJiqbsu6TRKsVjUn4TTCjHHqgKmxb9mXlsKekg1H0PNT6SSB0B-ozGDSkY1zGT7gy6K3jIduyAeOGQK3VCIeIi59yVpRE0594NOH7GCdb8hoJQKotE-kuMCAtJlrNJnPpQbpYxQFYqwtA4TRJZV8S2c-iZpsXb2ydZaoudfyKAo8CIhPNNVYqg0iYUw-sNgWcqLwcO9RGBVj2fW4boyeNLig5drP1KcqKZFtW0aY49S52_snTiD5PZwsJo7O9l65FxQQTSJ0OJCR7qx05Y4o4y1H2RH5Oov3g50_UX373uNSot9E9xA9siUqW56oc-s5yzTBS7QahpS_VYBKYjVhOghoCvdslP7P98bVMzobX9s171pOsxIIfyjdiJyVMa2xAazLbTmDPYF61xfwW1EOMLo41gQ_yzW-RJkdGJWiMIF56QtFRQkatJQ6N51EKz6-dtk380j4fG0ePBK6zsqwVC-KXVOvJF8fplpiTpIxPQKOjyyT-Ni682msRTSppcUEvt6EE6OzBScupoWab_j_hpUepxwrN71J8m-pBN5Z9VpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb9131adf.mp4?token=M0Zv6131aph5lnCj-d4MU6haLoeVL7dPKQ3OoLmwABsKtISCPyzU34-avw2I-OcOu5YOknevxXp97Xr00JrtV9NIvE6z-KVpdX-fv1Z6t9KHAvx-LJdoBnCyQATuBQhGJiqbsu6TRKsVjUn4TTCjHHqgKmxb9mXlsKekg1H0PNT6SSB0B-ozGDSkY1zGT7gy6K3jIduyAeOGQK3VCIeIi59yVpRE0594NOH7GCdb8hoJQKotE-kuMCAtJlrNJnPpQbpYxQFYqwtA4TRJZV8S2c-iZpsXb2ydZaoudfyKAo8CIhPNNVYqg0iYUw-sNgWcqLwcO9RGBVj2fW4boyeNLig5drP1KcqKZFtW0aY49S52_snTiD5PZwsJo7O9l65FxQQTSJ0OJCR7qx05Y4o4y1H2RH5Oov3g50_UX373uNSot9E9xA9siUqW56oc-s5yzTBS7QahpS_VYBKYjVhOghoCvdslP7P98bVMzobX9s171pOsxIIfyjdiJyVMa2xAazLbTmDPYF61xfwW1EOMLo41gQ_yzW-RJkdGJWiMIF56QtFRQkatJQ6N51EKz6-dtk380j4fG0ePBK6zsqwVC-KXVOvJF8fplpiTpIxPQKOjyyT-Ni682msRTSppcUEvt6EE6OzBScupoWab_j_hpUepxwrN71J8m-pBN5Z9VpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه چندتا بدهی و قسط همزمان داری، حتما این پنج مرحله رو انجام بده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691707" target="_blank">📅 16:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یارانه نقدی شهریور دهک‌های چهارم تا نهم واریز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691706" target="_blank">📅 15:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد
/ الجزیره
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691705" target="_blank">📅 15:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزیر نفت عراق: بیشتر نفتکش‌های عبوری از تنگه هرمز متعلق به عراق است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691704" target="_blank">📅 15:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رئیس مرکز وکلای قوه قضاییه از توقیف تعدادی از کشتی‌های آمریکایی و رژیم صهیونیستی در تنگه هرمز برای جبران خسارت جنگ‌ خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/691703" target="_blank">📅 15:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
استانداری هرمزگان خبر غیرحضوری شدن مدارس استان برای دو ماه آینده را تکذیب کرد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691702" target="_blank">📅 15:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
واشنگتن‌تایمز به نقل از مقامات ارشد آمریکایی: هنگامی که هواپیمای رئیس‌جمهور چین طی روز چهارشنبه در نزدیکی واشنگتن فرود بیاید، ترامپ شخصاً برای استقبال از او حضور خواهد یافت
🔹
این اقدام غیر معمول است، زیرا ترامپ معمولاً دیدار با رهبران خارجی را در کاخ سفید انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691699" target="_blank">📅 15:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برخی نان‌های سنتی طی ۲ ماه افزایش قیمت ۱۰۰ درصدی داشته‌اند
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران در
#گفتگو
با خبرفوری:
🔹
با وجود افزایش هزینه‌های نانوایی، قیمت گندم یارانه‌ای ۹۰۰ تومان است و در حال حاضر واردات گندم و آرد برای بخش خبازی انجام نمی‌شود.
🔹
قیمت برخی نان‌های سنتی طی دو ماه اخیر افزایشی بین حدود ۸۰ تا ۱۰۰ درصد داشته است. قیمت لواش از ۱۶۰۰ به ۲۷۰۰ تومان و سنگک از ۸۷۰۰ به ۱۵هزار و ۵۰۰ تومان رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691697" target="_blank">📅 15:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFnkhwIKzZhRoUxosSRdX55ORgE0gyp35Jp5KLKePFtRXywwPjZhS4-gloIZtwTqSXi5p0C88C14yqDKjJR6IvFvj95JpwWHRzv77kmSBvo-Z88T_D2PqpFENIImuhLE53X9hE56qAcKnCmDW-8mTghs0J4vjlaOLzgFJuVV-DAEvwCepz-euZ1WdTwXFLlQ_6crPFY0EGoqZ43L0HnnIu-oW6YT4MUZyApct6-nIPSjVoLYHdF6poDMLb1KsAXwfPFrftg4LE4DjXL3hOOWAQtg4dXa1FNB1gDGdt9LOpGPSzEFl_XoArB4Fx3wrC_-gtYt06-6urCkF1FlN2ZO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
هیئت غریب مدینه برگزار می‌کند؛
«مراسم عزاداری شب شهادت حضرت فاطمه معصومه (س)»
🔹
سخنران:
حجت الاسلام دکتر ناصر رفیعی
🎙
مداحان:
حاج سید رضا تحویلدار
کربلایی حسین عینی‌فرد
کربلایی امیر برومند
⏰
دوشنبه ۳۰ مرداد - ساعت‌ ۲۱
📍
مکان:
قم - خیابان ارم - روبروی پاساژ الغدیر - مدرسه آیت‌الله گلپایگانی</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691696" target="_blank">📅 15:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سخنگوی سپاه: ­مراکز اطلاعاتی آمریکا در تیررس ماست
🔹
تکنولوژی برتر آمریکا در برابر توان دفاعی و تهاجمی ایران رنگ باخته است
🔹
نیروهای آمریکایی به الازرق اردن فرار کردند اما آنجا را هم با موشک زدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/691695" target="_blank">📅 15:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6bd26cc9.mp4?token=Dj-9Mg2hDsn2FiNJ88XlxlUI_wBk2saGfETpHLvjTkHx7SyPygnKYrU02iGCfB0TSi9lhcdooEGXRMwRLofb9ObdsDAAtz2c5eNJHyJDcuYZquD5rBnzCs_D70aj9cpHGKVmOqlTWRryzfx5SJOIWafSF3hVdN9OC64QcjhbGs2Tel_4yLr5sqN_hDJmib7hv21eS9kek9voMMlkAswofybGbnZ7TTlkgCPyI_5HyjxcuZBwurOB5Y56p-C738w62B4TkFLh9EGGhe-BKsOY2u-1XrmpsuBeYSqSMzXuyY3d4xQ_qWItFUUb3GBL-IoulqNRotanMD9GNLfanH23RgQOiYtHAlYCoLXGuEI5qXfQ6oDghA69K5xwXOWA7nufkpcTg-yilIIB94gz_wB3BWbWa6mWb8Qjtb2Cft163E4qByKzvjnZXpoCJzFukupAR85Wh_Gj-7wfYPcZ_xuHGPfkZ5JuNb-vRRY6pJ_8-gWXKgCfmS2qQY1JLue87lrfyXj4BKHnMD-l3ab1P_plO8PqxaDc_FZLdexKx0r_jTEuscxVKvDYNDCKpOAXja7G8muRfzmW-OVbukO1biTozeoxg6BDN206cYAbdtZvHqVtfl9DG51SAqfMirzl4fvVlMXkkIWB41UyHSEBqUts0h_q1FP27dFvy_GDgXyjx48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6bd26cc9.mp4?token=Dj-9Mg2hDsn2FiNJ88XlxlUI_wBk2saGfETpHLvjTkHx7SyPygnKYrU02iGCfB0TSi9lhcdooEGXRMwRLofb9ObdsDAAtz2c5eNJHyJDcuYZquD5rBnzCs_D70aj9cpHGKVmOqlTWRryzfx5SJOIWafSF3hVdN9OC64QcjhbGs2Tel_4yLr5sqN_hDJmib7hv21eS9kek9voMMlkAswofybGbnZ7TTlkgCPyI_5HyjxcuZBwurOB5Y56p-C738w62B4TkFLh9EGGhe-BKsOY2u-1XrmpsuBeYSqSMzXuyY3d4xQ_qWItFUUb3GBL-IoulqNRotanMD9GNLfanH23RgQOiYtHAlYCoLXGuEI5qXfQ6oDghA69K5xwXOWA7nufkpcTg-yilIIB94gz_wB3BWbWa6mWb8Qjtb2Cft163E4qByKzvjnZXpoCJzFukupAR85Wh_Gj-7wfYPcZ_xuHGPfkZ5JuNb-vRRY6pJ_8-gWXKgCfmS2qQY1JLue87lrfyXj4BKHnMD-l3ab1P_plO8PqxaDc_FZLdexKx0r_jTEuscxVKvDYNDCKpOAXja7G8muRfzmW-OVbukO1biTozeoxg6BDN206cYAbdtZvHqVtfl9DG51SAqfMirzl4fvVlMXkkIWB41UyHSEBqUts0h_q1FP27dFvy_GDgXyjx48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراشه مغزی نورالینک، صدای مردی را که توانایی گفتار نداشت، دوباره به‌ او برگرداند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/691694" target="_blank">📅 15:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
در پی ارتحال حضرت آیت‌الله العظمی سیدموسی شبیری‌ زنجانی در استان‌های قم و زنجان ۳ روز عزای عمومی اعلام شد و روز ۱ مهر قم تعطیل خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/691693" target="_blank">📅 15:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpmA3gY3WhF3lCmDOmXMSmLo_hkYItiWfBg3_tf6vP_cjgJfAFv008xAMZPxdIkQJQ379bA4ZkWTfzIwbUJ0EQcHYaU7Tl7Xsoil2F7T1FHEfEHoA9CJDyWAucpjK7oufHN4qL256Q9TY7YSyEjT5cARyPqTUC9jf0Ndu3OzdTLv-xYMCLiy0PLzUMyXzP0ygrtEoQ-q6vJuO5p46159W8Lre50E-HBwxb3oKgiqLzdrzKL4XQ3NN3DyvPeAxwT9x_Z9wWyNwnmViczTTV2XFjUgu5XiroyPS9sK5SbjPL-AwskRjOQGvs-E8f_Ro5PYxBAvcXCrfCQits3oEgAPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اجاره بوفه مدرسه حسابی داغ شد/ هرچه دانش‌آموز بیشتر مبلغ اجاره بالاتر!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/691692" target="_blank">📅 15:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddca2fcfd4.mp4?token=NMVIny6pI6uOEbjYBk998BphZILx1t2hD_1qqfvzFAcrbK6by8FSxTW-Q4ouUhNWDkdJhGGJXx8_DqCuANCTfiUjnhwsw2hht5Q3DV5-1fRlfmUyBUttI_g3eqkQYsSgOCqMWhZtsCujSjL-QYQ3U_c3McVaqM1v5MnIlJhBbHvGCsbhywIHz4dUSqgm2J7IZ86ZeTPtUaXjqpk7peCo6jazER4aGGCtgxQWNkWPxAK37mX48DKgyGfv-aqceS9IohuL07OfG_8Lxnvfawn-en1n_NKVzVZgi8FE2p7z11gwc6GzbgKmFJgd4_FYpi1eJXwgNL6ZTpT3VJvs14_hjBHyLoJmfGTkUxh9mr_UZrIccvZO4yJM73bii-woQ9oxZyn7fxgNrbhSOl3tY1RTxq1R3Zwkns8mViGDmL1HAJK3fD14-hBjiGqKjD7IHAM2FV3ktsk5_FWStudXqlztnV9s0bxzATTaFQFZIQ8WVYRhqtFJem0foGMjsilZQHz1O-hNKlkwS6l4elJ9hSZEaiQKlb3yvK8owzf_k61hiqOLOpykKf54HZZo7qAJ6FvjFUsMa8qfIt_iD63oCoGEvvS8Q2ncsUxlefdgIMH-D5uACq6byTk2K3ca4se5u5bM8-QvXzPc1J0M8bObpKk0nEtNkQtS_8cW9h6BCGFbX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddca2fcfd4.mp4?token=NMVIny6pI6uOEbjYBk998BphZILx1t2hD_1qqfvzFAcrbK6by8FSxTW-Q4ouUhNWDkdJhGGJXx8_DqCuANCTfiUjnhwsw2hht5Q3DV5-1fRlfmUyBUttI_g3eqkQYsSgOCqMWhZtsCujSjL-QYQ3U_c3McVaqM1v5MnIlJhBbHvGCsbhywIHz4dUSqgm2J7IZ86ZeTPtUaXjqpk7peCo6jazER4aGGCtgxQWNkWPxAK37mX48DKgyGfv-aqceS9IohuL07OfG_8Lxnvfawn-en1n_NKVzVZgi8FE2p7z11gwc6GzbgKmFJgd4_FYpi1eJXwgNL6ZTpT3VJvs14_hjBHyLoJmfGTkUxh9mr_UZrIccvZO4yJM73bii-woQ9oxZyn7fxgNrbhSOl3tY1RTxq1R3Zwkns8mViGDmL1HAJK3fD14-hBjiGqKjD7IHAM2FV3ktsk5_FWStudXqlztnV9s0bxzATTaFQFZIQ8WVYRhqtFJem0foGMjsilZQHz1O-hNKlkwS6l4elJ9hSZEaiQKlb3yvK8owzf_k61hiqOLOpykKf54HZZo7qAJ6FvjFUsMa8qfIt_iD63oCoGEvvS8Q2ncsUxlefdgIMH-D5uACq6byTk2K3ca4se5u5bM8-QvXzPc1J0M8bObpKk0nEtNkQtS_8cW9h6BCGFbX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: علی لاریجانی چند ساعت قبل از شهادت، افطاری مهمان پزشکیان بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691691" target="_blank">📅 15:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691688">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXS-6dZDu9Np8SJBTuAHRkjUdq2CFQqRucX6H9y8h-mSBNkBQoeyCTi5QTKFl09ubdYpn_MXF-pGryHIh25yIRZ3jNGT76xd4CSH6hkYdSgQs9CDRsj9cqKLRBZmhHPgWTEUozQFjJcSSJhQwNKk7lqosHsUmxCQseellPpP-YJzN6rWrNZf1VwiIk0o7Cc6_fqHyaSgcMbEYf5UN_WqXuYxyn04FSL0-JlHt_jM_4uQgPvL5io_1uuli59USymiEU8IfbbT-H5eVm9IE2SSG5nwFbpXFxlVphLLv0cX6wTQszg4wI7-aycHdHydv-b2REicbNuvSr8KqZrbBJCR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4RZZgjJY9dj9vrPswR9yE8riYGCJsAurabfFktazg9w4I_3y8FMIKZFpnR3Br9HVat7cemV9XkqM0mlG3mxXS6CvtpFH2I9-dZMSAKcWV3m07wYRqtszwQiBCjte-cGqcwQyzgtETvEIYA9j5-_wBOBcRh_5R8M6ZL8e0nLUVhoCeRfwBUbx_0xvkcQhp5wu9vkVkCqboDBb7D5dgmFD2520x8r3FnZBweqncMncRDij_TiiGn7699_5ujf8aNITUKLGxPUlblKRLcUT4-4noOoWGuiFupNqTbHcttsaXUTW1Yg51wzA3rh8sOhj8XvvjBO2B7Am56j9Ga2D6LDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6OwC_1YtGx7emKo7tz9LrlsIuToEFjxHZhqmMzXplDyiMcW_zjzLpWA1hEtJzXCZ39lC92r0-9CSpZfr7Okg8kpUxUslTLpYHzH7ZhCB6_enpUkT9a_3Nmn2gatDlJwtjpeVzu2JubWdVxlXmDW1g99bGCbZsdmhDWpT06xy6gyK-8_tk1hx4_vAhQcGOagbKZHgJApO05glYKxm05-gXcqSEyDT5MILCTHT442CJTYIg2fi8LsgB55zIi86NvWUO1CEz7IM6HP2w4nn7iKxdWa6aNr18CyMMOCt1xJKnroHIjQq2s6q_Um5HDtEoApdYZG5BMvi2yBXlQTs9tBHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از یک پژوپارس که برای قاچاق مواد مخدر استفاده می‌شد
🔹
این خودرو که حامل موادمخدر بود حتی با شلیک پلیس به لاستیک‌ها هم متوقف نشد و راننده با رانندگی روی رینگ به حرکت خود ادامه داد تا وقتی که با شلیک پلیس به راننده متوقف و ۳ کیلو شیشه از این خودرو کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/691688" target="_blank">📅 14:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پزشکیان خطاب به دانش‌آموزان: بچه‌ها سلام! می‌دانید که شما گوهر هستید!
🔹
آدم، مفت به جایی نمی‌رسد؛ باید تلاش کرد.
🔹
من از یک خانوادۀ معمولی به اینجا رسیدم. شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691687" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پست سردار آزمون در واکنش به دعوت شدنش به تیم ملی: خوشحالی امروزم مثل اولین‌باری است که دعوت شدم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/691686" target="_blank">📅 14:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بازنشستگی رونالدو کنسل شد؟!
🔹
نام کریستیانو رونالدو در فهرست جدید پرتغال برای بازی‌های پیش‌رو قرار گرفت؛ این در حالی است که شایعاتی درباره خداحافظی او از تیم ملی مطرح شده بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691685" target="_blank">📅 14:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691681">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFwy5WNzC2XSKeJwO3YH5mrh_clVFJGQcLgIpJ2f1nF-I2nzIE8t8XxaZnykaPAG3DGnwjiw93-wB256HLjZIpOY5NSmsYXx0ms-yJx1ZirRACn8nQSuFd861YZ8BMeCr5NhPr5sR9uYIbegFZEaI32eKEHSU70uMFcDp98GVgdCkodYREtFR8BMvpAs3k-Z01m9LtJLQfdUpzc9GcXm6T_S1XCbjFr_Qywv8GK97VhUcwnYfi3UTGaTmgbkEakKNm1FRjhcY5BZsTQfWIhun29OTobyoGAOfREth845-nioK5Exc0fwfv881z4GmgHDsOZNrlHqRGf_zh99iTe-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4Qn93HcqV7PGCFRBwYd8AlAyVp577zdm2hkLaNpjmHfInXs6E6ZPn2aV5ctJCBqj3if10iS7jmnzlnLlvepJygAy-twV_e6yrMO897h0bBFU32HBduGLf2CmQv7_8Hu78vKekFFlznOCwh6iqjkXwbro0FblxGQs7QdUEIQ43Eb3bgcF5-DSNCyZPKDGEScvpcDse_wGU1gQEDJobBQnOxocCDuNFDKb83fSGXujZpCsAZsjiwdflFXnu554T5YGPjefu2-A0bu0Asq6CDKCnOB29z2FNaJIE8OsDxHTHroNCLkaa_JSoUnXkEZmZ084tMtQAPifaOqIVBQ0LM1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owQhW7mqVgTdVHUNQh4C3btXZZO6R3iWPs5K8itlXSc5xPBc-1PDhAYEQfUY-CA9-VxIQIurnTq-gAodYZJ0qKXKWOKrkPTM_HrCid0eFuvlS4eczoIRqEvImtZOuezZuIrV51KhBDRABTYGLPR5TaBQ5TNNf-VKcNPMaT1w63Lgvlf0DqPsX7Dz7ChI4gbyKguNUosDcU0sdQdMn9FyJureSvNCvg4imHjgK52svMjTVU655TFwxYovxh7_jWSilmnY3R-lh9wz_hfJcbyszhrJ-R8LYUKwTViD5zsD_J7_OgG17gNmY85ffUXZYnj5p-wwECVszAs9uZLwkXadBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/As921LqzIjKrQXgb93K-X0tebX5w5Y-SloKpFbbgdrBaZGUb97gjh-e9Ju_KSKX3XmIQ2OcKz1JS7CsXqJkArYKzg38lno1rluE7-_IHKTW2dG6FJxn9C8eOfY9UiRqsPpIJkdslWhey07EbC0Ssv2KqXTJVbylSyczHQbayC-Fb-l74Vc850IUFpElXlKcryyx3s-GzD0n9DH2yHBg5JtIGScD6EC5mzgPUlgiIJs1kQx2LauPoLPU67N006MLrAgxqoi_RYRhFYHXgD2aGWhOjvh1eQWm2FJu9CWObk0O2ZCnWpxn1ttBCo4xsq4vzQMPO20szDRkNRWJgjp7L4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نگاهی به خواص درمانی میوه‌های محبوب
🍒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691681" target="_blank">📅 14:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96c752487.mp4?token=Xjl2qN-OvJ2HbtA5AhMpZByql8pWebRm8APeJ5qe0PBmG9U0021XXAc4iQrXIEzhvvPdFvCxK76JFEPuNDwNUjd7CdS40bhCewMWnrvbVD0PJJfr8i9Fj8__J5B1ZUIcDud3y0pHec_8okqVE65eTh1ppy4C4r74_Hv2KgVZ2Q-JuvJjXNyfFJUap20l8gHnpVdp0zcfFdhTIiipa_T2qQjzAe4Y9vUBfx-4MYvfZ0n9sC3WC0vzzbOIpXRAiraD_MekGkuHmmR8Cmv2OY4TCBRplF9LBJ2GZqHw0c2QSQIylMGrPryHf10hG8PpnFuong_l84QByzVKAzJdwiR_0Y_9BitesrAsdUh5z629fFOMXmcDH33jZAMed5cnIGZuOF_U3CqqZEc9qUHxQVEdygY2MPTaECDOsNr8IN_bRFkR9C30L7oqnCkI4KXrmZAVjkY1IbzUrKsqLRy5hbrs6NskzNnOIfjmGJcfG5KJwZmu6J2wXiHzqzH_nRO_FdGHPKA2b-mZF1qPJ9LD3dP116yS5pHAzuGz83fDQse05rW3a3k9s0bG4XWhS0DPKetx7zNZjXC7kLCwXgTgVhGZMDdjzF3p9yHzaRd9P_eGjwqjtVUfI6ITSNUPSx2Pf-qGpUzf_2fJZ4ADxK1YQZI948kfUpEQSYw_KL71b_CS1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96c752487.mp4?token=Xjl2qN-OvJ2HbtA5AhMpZByql8pWebRm8APeJ5qe0PBmG9U0021XXAc4iQrXIEzhvvPdFvCxK76JFEPuNDwNUjd7CdS40bhCewMWnrvbVD0PJJfr8i9Fj8__J5B1ZUIcDud3y0pHec_8okqVE65eTh1ppy4C4r74_Hv2KgVZ2Q-JuvJjXNyfFJUap20l8gHnpVdp0zcfFdhTIiipa_T2qQjzAe4Y9vUBfx-4MYvfZ0n9sC3WC0vzzbOIpXRAiraD_MekGkuHmmR8Cmv2OY4TCBRplF9LBJ2GZqHw0c2QSQIylMGrPryHf10hG8PpnFuong_l84QByzVKAzJdwiR_0Y_9BitesrAsdUh5z629fFOMXmcDH33jZAMed5cnIGZuOF_U3CqqZEc9qUHxQVEdygY2MPTaECDOsNr8IN_bRFkR9C30L7oqnCkI4KXrmZAVjkY1IbzUrKsqLRy5hbrs6NskzNnOIfjmGJcfG5KJwZmu6J2wXiHzqzH_nRO_FdGHPKA2b-mZF1qPJ9LD3dP116yS5pHAzuGz83fDQse05rW3a3k9s0bG4XWhS0DPKetx7zNZjXC7kLCwXgTgVhGZMDdjzF3p9yHzaRd9P_eGjwqjtVUfI6ITSNUPSx2Pf-qGpUzf_2fJZ4ADxK1YQZI948kfUpEQSYw_KL71b_CS1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر سابق پنتاگون: آمریکا توان سرنگونی ایران را ندارد؛ تنها راه خروج از این فاجعه، عقب‌نشینی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691680" target="_blank">📅 14:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کیش و ماتِ استراتژی پنتاگون؛ بازی خراب‌کن آمریکا کیست؟
🔹
از تحریم و انزوا تا فشار نظامی؛ آمریکا در برخی بحران‌ها پله‌به‌پله پیش رفته است. اما یک‌جا این نردبان تنش به مقصد نرسید؛ جایی که محاسبات آمریکا به بن‌بست خورد.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691679" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزیر ارشاد: ممکن است در صورت آماده‌ شدن مقدمات، نمایشگاه کتاب به‌صورت حضوری در آبان برگزار شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/691677" target="_blank">📅 14:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای رویترز: کمبود جهانی گازوئیل احتمالاً تا سال ۲۰۲۷ ادامه خواهد داشت؛ ذخایر رو به کاهش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/691676" target="_blank">📅 14:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
شبکه عبری کان: سران سعودی درباره نحوه مقابله با انصارالله یمن دچار اختلاف شده‌اند؛ وزیر خارجه عربستان خواستار راه‌حل دیپلماتیک و وزیر دفاع حامی اقدام نظامی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/691675" target="_blank">📅 14:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgfm7W1oog1D_fn4dAJOyFXbpNcUtWYO-k1TaKvhfg5IFx0pZUzTjmnYo_DxboU02-jidEy5Pnxe1M2WzXqBNOTKt7xKWZohwSZAyUFiIYPrmRe17x-uApWE725dCUXF6djYLUobZR2IC-tLIirlZMkhKum1LRg8O99eed2M2oxbmEGmwE1vzzKeYmvcyKBhicNhOQ1Qoz_ZYcl9thvkWZQ8d363WVff9Aknijn5PY_i7p_rY1F-iydIpqUHoQdv3HtDcrXkzClNx5KCf1fXTMuUC1Cadib2C9l1dq1hxdAMmz3hXAPO58jRHiDtweWs6dk__jgneGRGFE8KIBxYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست لژیونرهای تیم ملی اعلام شد
🔹
علی نعمتی، محمد محبی، سعید عزت‌اللهی، محمد قربانی، مهدی طارمی، سردار آزمون، دنیس اکرت و شهاب زاهدی هشت لژیونری هستند که به اردوی تیم ملی دعوت شده‌اند.
🔹
قایدی، سامان قدوس و جهانبخش، غایبان بزرگ این لیست هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/691674" target="_blank">📅 14:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل ازیک منبع در وزارت کشور پاکستان: محسن نقوی برای گفت‌وگو درباره تلاش‌های میانجی‌گرانه و پایان بن‌بست موجود به تهران سفر می‌کند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/691673" target="_blank">📅 14:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNXXs7vU6aqnk-DbtxfarptrJ7JlKCDn19OlGMrTk5TWwn6i6KCGK2ZmrQOP5Ez8oPgiJ7HDZzx-DUroVGvgoY_W_K2gkTf56O7EBi294USLlynQ_Ac98oTCnudUBdUFXHLbfuszHOMUXnwq8DthDc6GnGJJp2zePzecPivQdTj_yxxGiD-knlTTfq64qKV6ICWeOlk3MGG1XleO7r50zVzoPNIyvzuKhjdZdyHz9RsUwTl8_TJ6J8BYBXQ0K9LqD_ZkOkwdKl65_GUD6otLgQvYK_xonjidNRyg_oiiW4KTxxxzwAjrTP083Q1NVhlkrEoW5nAg5pQl-3pjoIGX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور بانک کشاورزی د ر IRAN AI 2026؛  گامی در مسیر توسعه بانکداری هوشمند
🔻
کنفرانس و نمایشگاه «کاربرد هوش مصنوعی در صنایع و کسب‌وکارها» (IRAN AI 2026) با مشارکت بانک کشاورزی و به میزبانی دانشگاه صنعتی شریف؛ با حضور مدیران ارشد، متخصصان، پژوهشگران، شرکت‌های دانش‌بنیان، استارتاپ‌ها و فعالان حوزه فناوری آغاز به کار کرد.
🔻
مشارکت بانک کشاورزی در این رویداد، گامی در جهت تعامل با زیست‌بوم نوآوری کشور و بهره‌گیری از ظرفیت‌های هوش مصنوعی برای شتاب‌بخشی به تحول دیجیتال و توسعه بانکداری هوشمند به شمار می‌رود.
🔻
این رویداد تخصصی روزهای ۳۰ و ۳۱ شهریورماه در دانشگاه صنعتی شریف برگزار می‌شود.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691672" target="_blank">📅 14:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1b70ad80.mp4?token=AF22bweI2y1fPBhYe-N1sB98QcfrwyB3ZYKVKbyWkzRZECydjZxuXRUKtTHOPmfcmpI46a7geSYbrDF6kdj7ku7VS1Xh53VXW8sRU1Z7W5iIVCmjgOAB8njGHMDlb3wWmZJrfIZ0A27MvY3mIPhf6J9zssg0PXsiLK0vw35F3BXuKQkFPJ2QGw-5lEXTbOaHXGdHPlQaevbpayeEvlYpKcSCXUg7tRMw_VI0-BDFkpt80VAxV2G2f0Z4yGPBNlB-pmcrzRNxUfnjBu1UqnF_SsUKNyuL5nuZdtCuYQURGPxB0V64zHecQTaND2nIh2IfJU66yZnkBVvNm6i0nnICvl2T-L7druJHEyTLg-1asXpg4Qz8YYLIMDRPMXcFYP3UxUim3nZYN6RnH-Csn_4xSrC4jyAZvLzW5LKO0SHAK6xkFZigO1lgi-2VHxFm1oyNfi1iRxyf0ecT4udha20iaD4-pwHO2BDE1e0u0nAQ24WGFPGxnaGDl9sTRaVPDJgJZDfOapMclQTIidV-vCGYddHC7eQNDNQHFRvFyhiHa598WpeFhFXmFj4a0pb-rTDb0osPxsn_IP0OGE5f-nN5kn4eeG4pOeogbuqu0vDb_skWrmk2elQ2bo4puqkt9jiwlUHELuw-E4XeXvHzBaF9SHCfQM_FjwIkoVQEjCERFY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1b70ad80.mp4?token=AF22bweI2y1fPBhYe-N1sB98QcfrwyB3ZYKVKbyWkzRZECydjZxuXRUKtTHOPmfcmpI46a7geSYbrDF6kdj7ku7VS1Xh53VXW8sRU1Z7W5iIVCmjgOAB8njGHMDlb3wWmZJrfIZ0A27MvY3mIPhf6J9zssg0PXsiLK0vw35F3BXuKQkFPJ2QGw-5lEXTbOaHXGdHPlQaevbpayeEvlYpKcSCXUg7tRMw_VI0-BDFkpt80VAxV2G2f0Z4yGPBNlB-pmcrzRNxUfnjBu1UqnF_SsUKNyuL5nuZdtCuYQURGPxB0V64zHecQTaND2nIh2IfJU66yZnkBVvNm6i0nnICvl2T-L7druJHEyTLg-1asXpg4Qz8YYLIMDRPMXcFYP3UxUim3nZYN6RnH-Csn_4xSrC4jyAZvLzW5LKO0SHAK6xkFZigO1lgi-2VHxFm1oyNfi1iRxyf0ecT4udha20iaD4-pwHO2BDE1e0u0nAQ24WGFPGxnaGDl9sTRaVPDJgJZDfOapMclQTIidV-vCGYddHC7eQNDNQHFRvFyhiHa598WpeFhFXmFj4a0pb-rTDb0osPxsn_IP0OGE5f-nN5kn4eeG4pOeogbuqu0vDb_skWrmk2elQ2bo4puqkt9jiwlUHELuw-E4XeXvHzBaF9SHCfQM_FjwIkoVQEjCERFY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست ایمنی فولکس‌واگن؛ آزمونی نفس‌گیر برای سنجش ایمنی خودرو
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/691671" target="_blank">📅 13:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691670">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bda6f6e69.mp4?token=iyVVqD3QQZ1LZaBTfw02CF0UzMQAbNUJ2Jl0U3K1US3M6-tdoiCDZbC_ykD4ZqnZDvvGYq-OJn7uTl9MSbpkPC4p2VKrHC89Xuy-jPyDWiZYjj5mtmCcVeBOQXCWprSU4AMhdJ6mPxFSpJuHTP4GwRoqlGVYammREfJXDwIMJnVZBTcfa8gwD4iSTjXARm2jZCRL3MXUbKyNUcQUZpLFhLm0Wst2gNzYdn0puAfPjAmRaxHssivSip98OlkJDPXwvzw6TwKt9Fu5Ze1MxZzCqXRSWvXsdavgcNF5ekFSEDQcs3NpHZ6Sx3H-zU0qkd3o3yUdvJJ7KjF9KdS4tRnyzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bda6f6e69.mp4?token=iyVVqD3QQZ1LZaBTfw02CF0UzMQAbNUJ2Jl0U3K1US3M6-tdoiCDZbC_ykD4ZqnZDvvGYq-OJn7uTl9MSbpkPC4p2VKrHC89Xuy-jPyDWiZYjj5mtmCcVeBOQXCWprSU4AMhdJ6mPxFSpJuHTP4GwRoqlGVYammREfJXDwIMJnVZBTcfa8gwD4iSTjXARm2jZCRL3MXUbKyNUcQUZpLFhLm0Wst2gNzYdn0puAfPjAmRaxHssivSip98OlkJDPXwvzw6TwKt9Fu5Ze1MxZzCqXRSWvXsdavgcNF5ekFSEDQcs3NpHZ6Sx3H-zU0qkd3o3yUdvJJ7KjF9KdS4tRnyzoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان وحشتناک شن در جنوب الجزایر، روز را به شب تبدیل کرد
😱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691670" target="_blank">📅 13:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEVnS6csDv8Ocd-WqkWiJ_-UCUVLCDjjx0FEhChBE1wMHkiVDHs4NSSu94JpVqIjgH0omqjlG-84lJS-5x-1zsBTiONDZmFtE8PGRLVqt9XYeYGqSxn8BwQsFqEW52YC2ysAFryNk72S9NbaceP0EdxdjDIVSj9mQXae4cVcBQSBYzwobBlQMhlLUacQ3uWfhKA2V09H5QUD6U94t9iDzeWno9VmgNIBlMkhd-o8NJjoDyStBEJpdhjncsHXIeXuauKTdq7b5j_1C4UHjQzYEIQMYgU5pVg3BthyGBj5MFzWh8P5Z8cfdU4Hya6J32Yjr7IoeeNZ7HkEZojExfNJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/691669" target="_blank">📅 13:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آموزش مهارت‌های زندگی از کودکی در ژاپن؛
حتی خرید کردن هم یک درس است
🛒
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691668" target="_blank">📅 13:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b630b6a5d.mp4?token=JB_WqeynRnVXXPEfpJ8w02LJyN_AoIBO3U3VaXB810-USCew4nXMnsvAwzKLZNm1Xpf5eJ81_tZACiVXmPz87qaS6cpHRCEBbyVszTnlmYtSjqSbD_3KwkWLr6g46ksTwnZ86bTmiEB5LulPaigvyoo9Zp5XXV1rMgBsGe5DuiBL711h36zQtvbez0OUXJWgp51XdtyH0z2LzwqnmpXj9HHua2Ody8NGRQlBNQ1ro-nZikXb6XzNnC9vqL9_i4-3ybatXzXJe1W3H8qaX5O2a_GU4yUxoKNR8zhwe7MRJKSCBqekI6QR5iXMrOfG_L7lGCa4oCQ3erveWhM-1-wpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b630b6a5d.mp4?token=JB_WqeynRnVXXPEfpJ8w02LJyN_AoIBO3U3VaXB810-USCew4nXMnsvAwzKLZNm1Xpf5eJ81_tZACiVXmPz87qaS6cpHRCEBbyVszTnlmYtSjqSbD_3KwkWLr6g46ksTwnZ86bTmiEB5LulPaigvyoo9Zp5XXV1rMgBsGe5DuiBL711h36zQtvbez0OUXJWgp51XdtyH0z2LzwqnmpXj9HHua2Ody8NGRQlBNQ1ro-nZikXb6XzNnC9vqL9_i4-3ybatXzXJe1W3H8qaX5O2a_GU4yUxoKNR8zhwe7MRJKSCBqekI6QR5iXMrOfG_L7lGCa4oCQ3erveWhM-1-wpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا به ایرانی بودنم می‌بالم؟
🔹
حرف‌های شنیدنی حمید شهرابی مسئول تحقیقات خانه آمریکای لاتین در تهران. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/691664" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بیرانوند: اول سربازی، بعد استقلال!
🔹
قراردادش را با تراکتور فسخ می‌کند و از نیم‌فصل دوم برای فجر بازی می‌کند. او قصد دارد فصل آینده به استقلال برود؛ جایی که محمد خلیفه را هم جذب کرده و رقابت این دو دیدنی خواهد شد./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691663" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: آمریکا تاکنون شروط شش‌گانه ایران را نپذیرفته است
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
تحرکات اخیر آمریکا و هشدارهای این کشور درباره احتمال لغو پروازها و بسته‌شدن حریم هوایی، لزوماً به معنای آغاز یک عملیات گسترده نیست و اگر آمریکا اقدامی انجام دهد، توان آن محدود خواهد بود و نیروهای مسلح ایران نیز از آمادگی بالایی برای پاسخ برخوردارند.
🔹
آمریکا تاکنون شروط شش‌گانه ایران را نپذیرفته و ایران نیز بدون اقدام عملی آمریکا وارد مذاکره نخواهد شد.
🔹
تنگه هرمز و باب‌المندب همچنان بسته هستند و ایران بر ادامه فشار از طریق این آبراه‌ها تأکید دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/691662" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L49alU10fmipaEOba5W61z4fbMJ9n8QFuKHGxU32EULs9u3v4QUL12-VVSRGdlgA4F_7AzxBsibjIaHV57vUPxhN9DUDfEZot3IN0Dqt7LXVvxtXZWroVOzJHnqq5TUKkU0kLVLFBDAn2NL9urlsCpCqbfsyBLfbUbsv6f8ZUhSmIBoW8DXG8ti-3j1_IMA8OWRk8OKaVy1jrzO7fq7UXqSZWbBZsu2J2Osm8d0iVT2k8wbtzu2D_Qnf1RngZR3EvFNfv-jkqJ3ciYAgzSNr69s2ozjhGEZ36ZellBzDV-7mYf1uuthM2TSouGMqpeijFnHprp8ITzO6jRZrKJZxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مسابقه تلگرامی هایپراستار با کلی جایزه
💰
به ربات تلگرامی هایپراستار بیا، رکورد خفن بزن و
بدون قرعه‌کشی
جایزه بگیر:
1️⃣
نفر اول ۵۰ میلیون تومان اعتبار خرید از هایپراستار
2️⃣
نفر دوم ۴۰ میلیون تومان
3️⃣
نفر سوم ۳۰ میلیون تومان
4️⃣
نفر چهارم ۲۰ میلیون تومان
5️⃣
نفر پنجم ۱۰ میلیون تومان
💚
به همراه کد اشتراک یک ماهه
فیلیمو مدرسه
برای تمام شرکت‌کنندگان
شرکت در بازی
👇
@hyperstariranofficialbot
@hyperstariranofficialbot</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691661" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک نفتکش در حال عبور از تنگه هرمز دریافت کرده است/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691660" target="_blank">📅 13:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9248c71c9b.mp4?token=Q9zYTfdDwBRCYE0PKTRs-n1AlwB7Y1EmjYQnE2nZzuqiTO_7B43O2fMQDi-hHYefERgbmpOJ0aDgtQ1aDPb_PzUOIIcqy-eaJs_WcPa331A0y9oh6vXk7LczVvKyc6Cqkql2Dd55A-CgIMU484M3JP6lDJ69Jjz2aUA_6HBkSwL0otBWoEVEtxRPGOqptYYOIRDLO_1--b6OkgXqhNk8e7zlAe5c3RXJlJCzoFl5vFa-wjn8OYL5C6MLAka0U4HqvtTFKeUROJqR2nuoTkzdxF8cPHTOPlN3DkI4nkoEkZxDVm3YmLK5DAsKgz8IdSYRSCMefakxnFyHJqLLf6NDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9248c71c9b.mp4?token=Q9zYTfdDwBRCYE0PKTRs-n1AlwB7Y1EmjYQnE2nZzuqiTO_7B43O2fMQDi-hHYefERgbmpOJ0aDgtQ1aDPb_PzUOIIcqy-eaJs_WcPa331A0y9oh6vXk7LczVvKyc6Cqkql2Dd55A-CgIMU484M3JP6lDJ69Jjz2aUA_6HBkSwL0otBWoEVEtxRPGOqptYYOIRDLO_1--b6OkgXqhNk8e7zlAe5c3RXJlJCzoFl5vFa-wjn8OYL5C6MLAka0U4HqvtTFKeUROJqR2nuoTkzdxF8cPHTOPlN3DkI4nkoEkZxDVm3YmLK5DAsKgz8IdSYRSCMefakxnFyHJqLLf6NDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحکانه نخست وزیر قطر: ایران صلح طلب نیست!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691659" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
لیست لژیونرهای تیم ملی اعلام شد
🔹
علی نعمتی، محمد محبی، سعید عزت‌اللهی، محمد قربانی، مهدی طارمی، سردار آزمون، دنیس اکرت و شهاب زاهدی هشت لژیونری هستند که به اردوی تیم ملی دعوت شده‌اند.
🔹
قایدی، سامان قدوس و جهانبخش، غایبان بزرگ این لیست هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691658" target="_blank">📅 13:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک نفتکش در حال عبور از تنگه هرمز دریافت کرده است
/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/691657" target="_blank">📅 13:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
کاهش قیمت طلا در پی تنش‌های ایران و آمریکا
رویترز:
🔹
قیمت طلای نقدی با ۰.۵ درصد کاهش به ۴۳۵۴.۳۰ دلار در هر اونس رسید؛ قراردادهای آتی طلای آمریکا نیز ۰.۸ درصد افت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691655" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVZs-yUpdUjHzUlw3e7doKdw4tNCGbq9vGikpAm6jyZ7muXH6e-OTgb5X9aU-bO7XQzG0joQE2TSWo3uVcAEDB1E_NYIO1IzlP3ztxALiCiqyN8bwZeo4H6gpKobtl4vyssUwActtXVqdhHfreSl4zU2yr_CUQ7GIPKCxm7ZkzY1twtWea0IMkGimihsjo38nFFSYg8ASnb75-DEwmrzfArTu1IbWz9VmTL-9fsXjmVECehyyOuPCqWLKNxSlZ_6927-fI8elQJ_4JJZE9YxY2y2EWXbIydXc1ZQ4jg0Q7s88MelQQsxdAwYc8X-3PM-ODBxUj8YaMD-K9VodesF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت نوبیتکس از صعود ۵۰ دانشجوی دانشگاه شریف به دماوند
🔹
۵۰ نفر از اعضای گروه کوهنوردی دانشگاه صنعتی شریف با حمایت نوبیتکس، از سه جبهه مختلف به قله دماوند صعود کردند.
🔹
این برنامه با شعار «بیش از پیش» و در ادامه فعالیت‌های مسئولیت اجتماعی نوبیتکس در حمایت از تجربه‌های جمعی و جامعه دانشگاهی برگزار شد.
🔹
این صعود، پیوندی دوباره میان نوبیتکس و دانشگاه صنعتی شریف بود؛ پیوندی ریشه‌دار که یادآور سال‌های ابتدایی شکل‌گیری این مجموعه توسط دانش‌آموختگان همین دانشگاه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691654" target="_blank">📅 12:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5d47a6c0.mp4?token=EykrBByDMYhWrzDrGexoBVh1ZUy_FTtRlDeC4smzlXayGDMDl-4UGnqRh46ba_RlVA3x72JHl5MjeGp9c-4I7PXIVzLDvvCWoD-5gFljuOiDB5rx4zTmU-oVyCW-clw0lW-DhWY_V7Ss43t681Y9hT69VBOTF9RFUCXppg4rIXga39SF78kTlXoJKzByWlJ5Iyz-s_61GksPbPo1fOWHR8HksKNlqa6MDV2y1AtZHgVr_uMZUWz3HSNtcmofDMfO5UjJhX60v4IjnFMq_Gq0z_scvxREcoGnBWEPYFTiVF7-zW5PJIGBjy8e2lfvdUVq3xSUMvlVW7DTAa4rY4haL0lDK_UG8hkMJD9JgL-4eNu_jGH0PEX-SYmoMcQs4BChHKWpItWTtBJTT24G3R4ZlnRnE4Inj3x6REKf8QyyXTJiZa2cpwAez-pZQIheB6TPkrbZKEEzpTMOwHm6N2rdTVu9fUYyAVq2CipkBAH9o2KeZGwBCVNPhdKNwOHwt4oMhbB7Zjm0mkDMjZkLDFw2PZGWtTR94RsBB6jmgh--j09oOqJB0N_UYw6luP1tMfODRLj58rqhAwLauyH0BZZDe8uECzcWOhIPBg_7syZeSRRfSBzm8P6WBVU_zjEeGBLZcT8btcqNLXT9ZFFRjOZ9CrXHD_x5FqlTIUBrGuUzpmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5d47a6c0.mp4?token=EykrBByDMYhWrzDrGexoBVh1ZUy_FTtRlDeC4smzlXayGDMDl-4UGnqRh46ba_RlVA3x72JHl5MjeGp9c-4I7PXIVzLDvvCWoD-5gFljuOiDB5rx4zTmU-oVyCW-clw0lW-DhWY_V7Ss43t681Y9hT69VBOTF9RFUCXppg4rIXga39SF78kTlXoJKzByWlJ5Iyz-s_61GksPbPo1fOWHR8HksKNlqa6MDV2y1AtZHgVr_uMZUWz3HSNtcmofDMfO5UjJhX60v4IjnFMq_Gq0z_scvxREcoGnBWEPYFTiVF7-zW5PJIGBjy8e2lfvdUVq3xSUMvlVW7DTAa4rY4haL0lDK_UG8hkMJD9JgL-4eNu_jGH0PEX-SYmoMcQs4BChHKWpItWTtBJTT24G3R4ZlnRnE4Inj3x6REKf8QyyXTJiZa2cpwAez-pZQIheB6TPkrbZKEEzpTMOwHm6N2rdTVu9fUYyAVq2CipkBAH9o2KeZGwBCVNPhdKNwOHwt4oMhbB7Zjm0mkDMjZkLDFw2PZGWtTR94RsBB6jmgh--j09oOqJB0N_UYw6luP1tMfODRLj58rqhAwLauyH0BZZDe8uECzcWOhIPBg_7syZeSRRfSBzm8P6WBVU_zjEeGBLZcT8btcqNLXT9ZFFRjOZ9CrXHD_x5FqlTIUBrGuUzpmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک معجون فوق‌العاده مقوی که استخوان‌ها رو مثل فولاد محکم می‌کنه
🍹
😋
مواد لازم:
🔹
۵ عدد انجیر خشک
🔹
۷ عدد بادام درختی
🔹
۱ استکان گلاب
🔹
۱ قاشق غذاخوری پودر سنجد
🔹
۱ قاشق غذاخوری کنجد
🔹
۳ عدد خرما (اگر خرمای دانه‌ریز مثل خاصویی استفاده می‌کنید، ۵ عدد)
🔹
۱ لیوان شیر…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/691653" target="_blank">📅 12:56 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
