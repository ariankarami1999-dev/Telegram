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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 23:39:52</div>
<hr>

<div class="tg-post" id="msg-662015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-LO-SIisnO-XUPWvskFG2Zo-gw9VqgRyghn3Ai2TZCNAOtWI6BKxGGThV1GYOdXRSq_hZGRZOj_xMM3dMmwUetFkLF5KQYEZWocE9p_gDL6PdnaGxTX_di3XGr0UcVO_nLTm_uOiVigkfKdY-ZZw63v8tuRzNNcGbkop9VxNLx1N_sKhaQcXa6ngrhR024Bh1NUI_z-iah9Szn9qN14hjoh-SZBz8Hybx8O3FJ5eq_miIGq8GiBBnr_MvUOWf22hsUOzE7NXni6tTOQUBhHash2SHhKiw_qqYsaTZn25POt8QvUNKntC8TIEngoaWxo0B-BLaaduvo1To7vOKCetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZodD5m33SKivKbqZ9hn22mKOp6XMGhW3TmENopgPAJi69agOSlk1PPOtTq7LT47qEkaqOptbQMJ1C9e8dc5nRNIgjajRARCFvkOmFq9Kuq95J6kp9UQqjw2eJGwvaQw3tB6fzoTfHWZ1QBvO9ymixY2wU2CQigM8fJZf-os_m-pKkjy6o3KoZh2HULZTO5zNY123iSlJ2QVW5_ac1aADgV--_wjHkv4nRIn3jPEmeosWzhMWiGFbmGP8_IoyCpaN2JCGWkuKq8COa3M7mV5Elq0lU3w9IbRz4KXD9nnBhfjWYwp9rPPxDXR2dvT0HRlBCALtarmWAp-9bN5F781Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcTTTvVPoSaaiOTVv50Vadl24tQAgNOWqm6Wo01NLJAt8Yvqjp5JO6dlPxrC-T45vWUDD-LOetq7quZP79YLqMx-K2-Py-G94-01bKkcs4VGhwL5dPqeDKm0wkBADqw2P6SPnX56geE8VrhVEWgNmyI0T71jNKW12PvzlQodSA6FKDtFMoVhFSEiI0GFLsqou-8wTi0SJsst1aLqfTZvpdUNhCm4RT9n_88_zR8jmkQzC9S6ctRGmchYaY54jzg1ZZ4DKz4AEgdqAqxSmhwgB7tEoZFzUxCJqTpatGL3x_sPCMjkzvc5aDqhaMQDhjUy1pJQjtxPOQTrZT7eK9Z4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJs4zULr0D52W9ysTLM_ws8QC08Zset6GU9A_maD6qOoGywRCwjdCjmeSodaaeitcTZeobqA_4DoT0UKopudkZI9-P8sBkXMzHffxxNCFf5dMRIemjj1UEe0bVK7NoFGYX3TW7Mmz_Jm1JnbKUYnFJKd7TAPI8-IISAIMTuTrrFrh5Bp6mOXTtXZ7371jupK6hotSrSAdyY27tAt17hBpJRJNL_7b0cw3L_cV7OwgWP-OYvEO4dVg0ViJoiCVaQ3bwneRz2IvpC1fMtVp1ihPuQbllKIitz9yi-XgD77IMJCpvHQ7kpt-tv3EZx3hn7iKEwXFXDXRGDQjXn8XXYSEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از میناب تا جام جهانی؛ حضور کودکان میناب روی سکوهای جام جهانی
/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/662015" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867650d109.mp4?token=lDvEhCl17lCewsm8Q3KiaqGcM4dJSKR4_cqHev-jA9B7vT2V_z69aBRzqiCMz_LaEvCxpB5d30SIEy3va5BlqppGLrBc6RZgXyxQls1TORrRwtmsN_GjC4RTaMdBX_6OG_vWTBdLHVBaS-ixIOHXPgTzsQKReyoiXlo7SGSMR8rjkt4PN-KGsQBETdIHgcqECdrMFdpKnjMMnIYCIDG7WCy3eJgGcy3Ku4Xy99mPu7hBcl1cZ80-YC72-lSXCWpxPmVVayFBRpBrAXtWbp3ifnaMyiJ6-d_Un62AS5CVUSix2p0dPHVtvxtF757o6IxzS7hhiivehNsieeqqMSA1JzyulNwFtJgwuV_caJFYeGtVJjWa7argt2DjYPzWTr6b0gX5Rd_LxcMSRU1XNOT78egj17rrJHSLhH7nMpllg-fNZkNE-7Bt6_NA8t3O9o0qocT_YRPSzDcJz-AXXBlt87GEX646E7DtGtLcmZlnpTSs3tttrGUQ6Egl7lXXiY7Nef8D5WHOV3DrlzEYniuHpRsoHmt9mg1y6omnkvCy_eWBHCYekxVfXYXe_smt4_uwQlG5qowzrwm_HrsT36zrpxzYWgM86RltqIP7EMuPlk7W1mCs-wztcDOmi_s1wZ0bg4BowID8cpGtOhTWIWXqYxsiYWHRuNtZLFwXMmHrq3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867650d109.mp4?token=lDvEhCl17lCewsm8Q3KiaqGcM4dJSKR4_cqHev-jA9B7vT2V_z69aBRzqiCMz_LaEvCxpB5d30SIEy3va5BlqppGLrBc6RZgXyxQls1TORrRwtmsN_GjC4RTaMdBX_6OG_vWTBdLHVBaS-ixIOHXPgTzsQKReyoiXlo7SGSMR8rjkt4PN-KGsQBETdIHgcqECdrMFdpKnjMMnIYCIDG7WCy3eJgGcy3Ku4Xy99mPu7hBcl1cZ80-YC72-lSXCWpxPmVVayFBRpBrAXtWbp3ifnaMyiJ6-d_Un62AS5CVUSix2p0dPHVtvxtF757o6IxzS7hhiivehNsieeqqMSA1JzyulNwFtJgwuV_caJFYeGtVJjWa7argt2DjYPzWTr6b0gX5Rd_LxcMSRU1XNOT78egj17rrJHSLhH7nMpllg-fNZkNE-7Bt6_NA8t3O9o0qocT_YRPSzDcJz-AXXBlt87GEX646E7DtGtLcmZlnpTSs3tttrGUQ6Egl7lXXiY7Nef8D5WHOV3DrlzEYniuHpRsoHmt9mg1y6omnkvCy_eWBHCYekxVfXYXe_smt4_uwQlG5qowzrwm_HrsT36zrpxzYWgM86RltqIP7EMuPlk7W1mCs-wztcDOmi_s1wZ0bg4BowID8cpGtOhTWIWXqYxsiYWHRuNtZLFwXMmHrq3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/662014" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0addaa1aa.mp4?token=AmoD_mc-Zd6_p9EIeJAWQ4_LDW59Qjn--x_Uk0Bpj6a9c9Nl6EfLoW6xrE8P1hE_Re2u81ZghSyE2erz6mhsAVvg4b37lf3I7bZBBiId7D2ykXFq5IomWaSt6mnDHXZ4ShjpE5eZRcJpOUYJzYX2tSIz0arDda0PwfjdBPTsv686gOpS6WkBr5qYFg1dFOtYeTIgB4tWSXB2ldxPXtmA6jqd-TudsfkIxRF1gosUmeC9X4hMox8EXwJRAD3pGg5zLYyJOJnJOwzbp1UWJjoUqmRH34Kuv3Yfq9-JSoiNmOjgLE0JtDODOscI27BtwhWMzEA_MO4WKxBv5mkfR_xKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0addaa1aa.mp4?token=AmoD_mc-Zd6_p9EIeJAWQ4_LDW59Qjn--x_Uk0Bpj6a9c9Nl6EfLoW6xrE8P1hE_Re2u81ZghSyE2erz6mhsAVvg4b37lf3I7bZBBiId7D2ykXFq5IomWaSt6mnDHXZ4ShjpE5eZRcJpOUYJzYX2tSIz0arDda0PwfjdBPTsv686gOpS6WkBr5qYFg1dFOtYeTIgB4tWSXB2ldxPXtmA6jqd-TudsfkIxRF1gosUmeC9X4hMox8EXwJRAD3pGg5zLYyJOJnJOwzbp1UWJjoUqmRH34Kuv3Yfq9-JSoiNmOjgLE0JtDODOscI27BtwhWMzEA_MO4WKxBv5mkfR_xKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای کافه‌های تهران در حمایت از تیم ملی!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/akhbarefori/662013" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
🔹
این دور متفاوت از دوره‌های گذشته است و برای اطلاع از وضعیت مذاکرات و نتایجی که تا الان به دست آمده باید منتظر اظهار…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/662012" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smaC3JTDcCN72OCRXbEtotryTQSJeot4Sq7CPvRjjP6aZn7lzMi8LszTrBpc1lCXoroMGSIz9ttZTrxA1e4Mxn6zPNl0_NydlBYw_RNLapp2wUzLHIeFBHlG2tU-jDhtik6Hx5zQ3KwrEwX0kJ7WUhKzaQnrCEJPvPQ39O6CuyQn1wa96kJ9cjfO5ljAedjJoOtOSxj42iRvhjz1ELsDL_6Y0CEZjfISd7ZTGahIGG9aXq8_QGBPJ0GiyIuaXktJhmCPK2kdBtVSqFNZ7WwJF5npe8SM9E5hJe9wq2dOSdq_i71h2jvYUSdi8wqa33FYQdjHKbuRSNvRIfa86pek3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی خطاب به سربازان تروریست ارتش رژیم صهیونیستی
فرمانده نیروی قدس سپاه:
🔹
سربازان متجاوز و تروریست صهیونیست ، کمتر از ۴ روز ۱۰۰ نفر تلفات دادید!!!، اگر با پای خود از جنوب لبنان خارج نشوید، حماسه سال ۲۰۰۰ بار دیگر تکرار خواهد شد؛ همان سالی که با خفت و خواری از این سرزمین فرار کردید.
🔹
امروز نیز اگر بر تجاوز و اشغالگری اصرار ورزید، با ذلت و شکست با لگد بیرون  رانده خواهید شد.
خود دانید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662011" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رایزنی وزیران خارجه اردن و الجزایر درباره توقف تنش در غرب آسیا
🔹
بر اساس بیانیه وزارت خارجه اردن، دو طرف به بررسی تلاش‌های منطقه‌ای و بین المللی برای توقف تنش در خاورمیانه و تضمین آرامش اوضاع فراگیر از طریق حل دلایل اصلی تنش پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/662010" target="_blank">📅 23:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
🔹
این دور متفاوت از دوره‌های گذشته است و برای اطلاع از وضعیت مذاکرات و نتایجی که تا الان به دست آمده باید منتظر اظهار نظر رسمی اعضای تیم مذاکراتی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662009" target="_blank">📅 23:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGn6asOspZ8Kacs-6PK6XQbPuXa0v7eBQYbJlkwRJHqFkCgX7qPH8OnqXmL1qFkPrnKR4PKhBnjtVa32xtgfqjZmLhHIIWKC3N9IArM-vNy3cAH4-uOFTcnSSk_L9vtvZsxYHvRLdOOsPU5jTlB7O7CWm35By5tiWFTMA2cvYENfBB8tN1_cIfkBtOf7c9icIbzNjWcPqjH_ve4OUMCmc-4UVEJf8-NFa5-BF95u6nZJQADdG8qgyRuRZ8cThAibI5RdGeI5FIPJkc02WR-8Hqh1qSJbGXtDCT2IfWyuloMOkY5N2aM0jxIplSdl5FDNkNXe8MCBNSAoYJr4K7bpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار در یکی از کارخانه‌های رأس لفان قطر رخ داد
🔹
وزارت کشور قطر اعلام کرد این انفجار در داخل یکی از کارخانه‌های منطقه رأس لفان رخ داده است.
🔹
مقام‌های قطری تأکید کردند در این حادثه هیچ‌گونه تلفات انسانی گزارش نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662008" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiadNTPltC2esIg3By0ERUZoNkCF696CfXpXvNSn6EMKbTLVXJZ9Q78aw_qtRIMc2r8wJnVSUe0wR9CIJ2Fkn0xLjp71Te8d8NLTiTU-NDuTvProOl4C9u6fX9BpS4n3T1mikxDSW5MPuvWmeuGQBVypI8KDJA7by88oBtt8JJFXJSaolW9wO4i4pjbduD0KnmDQZBVV5ZWTh_1HDm4HEVjTOVuJGwdt13Z-YUS_XMIy0zveAtSh4Dj9dLolNJOlkCPpQWC1UukMtgXkoAH3YH8jlwDL5Xw3YpMrc2Q3i4XfcgzSZoloGK5H-rRxs1ZpQS4j-F1-zVtUQZZyM1HQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات دو تیم تو نیمه اول
🔹
قرمز واسه بلژیک
🔹
سفید واسه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/662007" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8TS9uS-G4YKEAhbfOGCFR7gjHHzmpwvyc17giJ6VDanZs7RdDvApNhULmRamOL0GA9_E7aloLcZUB8DL2sHqJQKGb6u66V9FxY3F1q9623atq8XCsK1JHW2luPwbRWlB7RRf1C1ResCUzP3bCeiYPFsTKYwv8nCt6r0R2E3_0orp-sGuk6-FdfypyYIvlITOPf6fjf8bdLX87NCSrfVp6GMZSW50mHXB2eU7Qh6O9x7Zaf6Ez3fD6S3o3_64NYFdKM1X_HaizDzGbBqqL1yGQ7_O-jLA_10EwR5tnZpyJXe3XOT49VeW-xcr7RbJujn0_zAmUgp89G8WQ-uxPsfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار بازی ایران و بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662006" target="_blank">📅 23:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📷
‏انفجار قطر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662005" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT3c6MUnEDYojXvgX1oC84LS10npLng4I02azNTy00YtvLgQ1wdoS4KTnHwokWdzMvERD6AP8gPEOw73plCc25wuI-7Hq-qpTfmMl0dwpIRVmqlwG_y5FmJXNRNcNfna9zwcDx2LD7RFO-97BPP5FWEEeesHzr6aYvq9HpeKqonsjMMhNHdgbf28Opt_0O-lsU1lROiAIg--EY9UewQGw4_rHtUXVTbjFj-9cqBo1F5ynVy4JXmGsK1t-kNpZpU6EuXqEg_k1BT9VrxpgZ5v4DHjXaPIb1DV40ys8acMNNCJAswcZJ3mWQTTE7Gb9ak6tZIF5_1Gf4fHYv_qowKlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز از شنیده شدن صدای انفجار شدید در دوحه خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662004" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پایان نیمه نخست با نتیجه تساوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662003" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزیر امنیت ملی اسرائیل: با ایرانی‌ها، هیچ فایده‌ای برای سازش و امضای توافقنامه وجود ندارد
بن گویر:
🔹
ایرانی‌ها باید بمباران شوند، و سپس دوباره بمباران شوند و سپس دوباره بمباران شونددر مورد حزب‌الله هم همینطور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662002" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رویترز از شنیده شدن صدای انفجار شدید در دوحه خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662001" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
المیادین: تهدیدات ترامپ بر فضای مذاکرات تأثیر گذاشته و آن‌ را پیچیده‌تر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662000" target="_blank">📅 23:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=gaRKUMZ2zVGF3ACC7XTuebVBOz-RgKK-gAgBjGJNBfLUeH5kUgFxZ2LYpr1UHJtnDJZDE1bzXtkrkw0VFM5Arml5i-jmvDxQXSIb2f84-FtbA673D55X4gSpABZEwRq4B6_F0k8BU6ylbVO8TuOGlg71Zv63s84gQSNOl68z5bZcymJfwArjsKP24AIh_4VYeMPT7SLKJrUoUqPDjYrWAFAxmQ_OkH3x9COaD0YmrZu-hjIZYF3lKWTpTMn7FU5l3lUkH93lAZA7R4ZnZQ2Zuha7IyGrRBaFvlRUQFz0oeff03cbLEiCdVXenw7AtGRaMcdpZ9Qb-eFXIQQLfzV_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=gaRKUMZ2zVGF3ACC7XTuebVBOz-RgKK-gAgBjGJNBfLUeH5kUgFxZ2LYpr1UHJtnDJZDE1bzXtkrkw0VFM5Arml5i-jmvDxQXSIb2f84-FtbA673D55X4gSpABZEwRq4B6_F0k8BU6ylbVO8TuOGlg71Zv63s84gQSNOl68z5bZcymJfwArjsKP24AIh_4VYeMPT7SLKJrUoUqPDjYrWAFAxmQ_OkH3x9COaD0YmrZu-hjIZYF3lKWTpTMn7FU5l3lUkH93lAZA7R4ZnZQ2Zuha7IyGrRBaFvlRUQFz0oeff03cbLEiCdVXenw7AtGRaMcdpZ9Qb-eFXIQQLfzV_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داور به‌خاطر تعلل بلژیکی‌ها پرتاب را از آن‌ها گرفت و به ایران داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661999" target="_blank">📅 23:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58838dde80.mp4?token=LYDLp7YC3JyXnXl0Y0Vdf7sf853WHtQbZewhnOu_mHRktITZRZT6CvTdvp6k-uczh8oV9nexU1jbNDN4Dknw_0wiw9tA7QUdhUgSknL0tFJ7fgntDbd7BXwDFmzOINkEQpiLmWDDntuv8bkG_lYd_LUEmrAzjRZ8mvcGEhzi6GaEF2GTNe1YtjeGu5ZkfUAZLTD7U6TlUvcFW59HGOPU6lkNkGUsQ57rAuwAdaEsQdrRrgrmXiT9dUFt-VRVUhTxbf6I0d2cTCzH8HqP4q6uhKPKlVNRKVSvZXtCuKoX_-Zq8Enr_XPnteD3zsmElih8U_WCWjszNxgU8JVncfLNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58838dde80.mp4?token=LYDLp7YC3JyXnXl0Y0Vdf7sf853WHtQbZewhnOu_mHRktITZRZT6CvTdvp6k-uczh8oV9nexU1jbNDN4Dknw_0wiw9tA7QUdhUgSknL0tFJ7fgntDbd7BXwDFmzOINkEQpiLmWDDntuv8bkG_lYd_LUEmrAzjRZ8mvcGEhzi6GaEF2GTNe1YtjeGu5ZkfUAZLTD7U6TlUvcFW59HGOPU6lkNkGUsQ57rAuwAdaEsQdrRrgrmXiT9dUFt-VRVUhTxbf6I0d2cTCzH8HqP4q6uhKPKlVNRKVSvZXtCuKoX_-Zq8Enr_XPnteD3zsmElih8U_WCWjszNxgU8JVncfLNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موقعیت خطرناک روی دروازه ایران رو بیرانوند گرفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661998" target="_blank">📅 23:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dcb564df.mp4?token=LAnGV_kKSMWgsC6Ygd6vEv6Y1oKe18FhaGCCE_9WL7pC_v2bPgpWUJek0li2BBl42QjE6D_YkL8ToDZkPtveOe3CeoNp2CbFq9Aa_3PZ4AtTE-Q0dN2F0yl2oG-05SCWnkWj7QmjnbaQl_8YUbZwsg4qvToA_iwz7zT9rcp2Q9cVmRUX9JVPgMwlKi1q3500gSrzrFoxSNHJdchykE1ELHMTscPIdYyG1KQfnr6b5k80mHaBC1DHekqZGe6SDdmFQQHw-ZvY7sK_n-9yRq8aYoeij-IunCY2YgEVMUClylPhqm0FaFuNq76HzdT3700IRi4OBJgQRx8PH0llSnEHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dcb564df.mp4?token=LAnGV_kKSMWgsC6Ygd6vEv6Y1oKe18FhaGCCE_9WL7pC_v2bPgpWUJek0li2BBl42QjE6D_YkL8ToDZkPtveOe3CeoNp2CbFq9Aa_3PZ4AtTE-Q0dN2F0yl2oG-05SCWnkWj7QmjnbaQl_8YUbZwsg4qvToA_iwz7zT9rcp2Q9cVmRUX9JVPgMwlKi1q3500gSrzrFoxSNHJdchykE1ELHMTscPIdYyG1KQfnr6b5k80mHaBC1DHekqZGe6SDdmFQQHw-ZvY7sK_n-9yRq8aYoeij-IunCY2YgEVMUClylPhqm0FaFuNq76HzdT3700IRi4OBJgQRx8PH0llSnEHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی مهدوی‌کیا و جرج وه‌آ در ورزشگاه دیدار ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661997" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حلب
🔹
منابع سوری از شنیده شدن صدای انفجار در شهر حلب واقع در شمال سوریه خبر دادند.
🔹
هنوز گزارشی درباره علت وقوع این انفجار منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661996" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a51af7066.mp4?token=WirRNQLR1XQg6HdgRfWeEBJ2IGlzI72GwUJQU4QYmfFnnuBCLeP0ChFsIK-pDWH_Bz1W4Gd1512PUfUVMspy1C0OBcmxOzSe65Orx4g2llFS2x7Lw7-uu1NhQXjepWbCzQugyctn_e_bhPRhGpOjOIZC5sKG634T0DSulAq_g455aysBBUI323O2G6AukFjZX-4EIvFLkMgklLMc694HTGhq3ZAIz0rVR8gRXF9UToyXu2VIt2tQm-ZjJfPgxzIRSb_5Vuw6sxUBrXsQ3QaG1-F-LLwgMtkNurXtKS0OCU-MY8w230IR-z_e_s0ooQUr44cCrkN9IBEE2cAaEpaVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a51af7066.mp4?token=WirRNQLR1XQg6HdgRfWeEBJ2IGlzI72GwUJQU4QYmfFnnuBCLeP0ChFsIK-pDWH_Bz1W4Gd1512PUfUVMspy1C0OBcmxOzSe65Orx4g2llFS2x7Lw7-uu1NhQXjepWbCzQugyctn_e_bhPRhGpOjOIZC5sKG634T0DSulAq_g455aysBBUI323O2G6AukFjZX-4EIvFLkMgklLMc694HTGhq3ZAIz0rVR8gRXF9UToyXu2VIt2tQm-ZjJfPgxzIRSb_5Vuw6sxUBrXsQ3QaG1-F-LLwgMtkNurXtKS0OCU-MY8w230IR-z_e_s0ooQUr44cCrkN9IBEE2cAaEpaVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه ایستگاهی دی بروینه با هوشیاری مدافعان ایران دفع شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661995" target="_blank">📅 23:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbyCDITktkB0VQKLQ4jOZsuDJ7LiuDPmep9B0MNkisqcR8nydidNXLdEHbhsBvzlXhQGuuI_8dBvH2maEfK5X7HuSAIICHArr4DrhMV_wCIopjKrxhKZpu59pgSXclfxwnayTvuiBZ6uumm5QRGhHV1IrUqSrPYaARqA605SJu1fLm7EX4wN6FqcSTPnIfwuKPWRy1G_ddEefVgjeKF914HrCRrBTF6NWdtXdr0-9vjv03twA0IeLVkUd7n2PwajnxuCaPsYWpdFwX82s_RtoEnbBEuBVqD6EHhIQlMqNG2wpBph27cczIrCwzE58Utwmiu0n0D7MmOoIXCbZuOFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارجی‌ها تو توییتر دارن از تاکتیک تیم‌ملی تعریف میکنن و حسابی کیف کردن
🔹
نوشته: حیف شد که آفساید اعلام شد، چون واقعاً یه گل فوق‌العاده از روی ضربه ایستگاهی برای ایران بود. خلاقانه، مبتکرانه و نوآورانه؛ هر صفتی دوست داری بهش بده. انتظار دارم فصل بعد نیکلاس جوور و میکل آرتتا هم یه همچین حرکت قشنگی رو تکرار کنن.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661994" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
المیادین: تهدیدات ترامپ بر فضای مذاکرات تأثیر گذاشته و آن‌ را پیچیده‌تر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/661993" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شوخی کاربران فضای مجازی: الان ترامپ به صورت جیمی جامپ می‌پره وسط زمین پیراهنش رو میده بالا میبینی زیرش نوشته ایران هرگز نباید سلاح هسته‌ای داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661992" target="_blank">📅 23:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-Vn_z0zLuPBMjwDUoUfawm_t8dhj1AeU5BPXgY_ALFCRn-H8mdJAwtZvr2gdb4fkgzMGqdIw0ElpYLHbcj1x-6cV6ezja2jz2IzBNxbwwvlqa7b-ZQV4U2E61_sv__BKwv1GKTTpEhOHN452r32aPSJglUwRF9vTDLeVRN0uM_tnRLBf8bSpTV9pVxnaUoLmk3fnEJrmUoPwBpOZyQd4CcwwaJkVf1DblGoub91_q4Na-gOXtAHE8ILluHq09FPcK4WrMXgZw4hlZNCWiJF_YGOGsBemPB473gWZX0wm-9qlk89wjg6XHf93FIBqGWbDAjJdCzESs5pPhQ-aeusYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
فقط برای چند میلی‌متر؛ خیلی حیف شد! #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/661990" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfd45464c.mp4?token=Yf_Z86Am3OK31JoPcoceBMwnWZuHJ2Bw6kgZC88upp0HB8oJ6j8ADBuS0Jche6pfiFxvmE3UGF0jzjehJeyz_MLXngOoeLZMPOonrjGOR3Irw8S7WE9IYgroIImNwGUeKjBVf1tg_nedKLObYW7AtKtmhWmzvWJHA5i9pzzyKF2iA8prC50tgRb4_46Aktfe4d4CjDOtnUMvx3_1VG3ztr9nsY2LShlvyPyY8MdyBRyQ_XIOeDz7SkyFynLpL9G6byYiotKhj-2VibUoPUnRZ0SSWNsmq-udoD4rj2M7Ih1phEyfpJVU73OT2qK9SfqoHxadGHQce3cEC75OtG7ulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfd45464c.mp4?token=Yf_Z86Am3OK31JoPcoceBMwnWZuHJ2Bw6kgZC88upp0HB8oJ6j8ADBuS0Jche6pfiFxvmE3UGF0jzjehJeyz_MLXngOoeLZMPOonrjGOR3Irw8S7WE9IYgroIImNwGUeKjBVf1tg_nedKLObYW7AtKtmhWmzvWJHA5i9pzzyKF2iA8prC50tgRb4_46Aktfe4d4CjDOtnUMvx3_1VG3ztr9nsY2LShlvyPyY8MdyBRyQ_XIOeDz7SkyFynLpL9G6byYiotKhj-2VibUoPUnRZ0SSWNsmq-udoD4rj2M7Ih1phEyfpJVU73OT2qK9SfqoHxadGHQce3cEC75OtG7ulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه‌ها و فریادهای امیر قلعه نوعی به اعضای تیم ملی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/661989" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvykaINPU2OcfD7EeyN4rs99qtJIKcwPNhkhJryUhIVXVxxL-Ii9grGVSpDvdEdhKl3S_I_VHZFOgZUiR_tPdaZ85VQBhqTiCGryvZ2E8QtO1JUSEsUN70Vby6Nna6e2YHkf6U92Zzc96wSOlWhpMgSdIqKpeINlASGHyoFrkzMD_SSY5Rz66-kEvRJW5kDO3YQy_oxz8GF4x4IgUlS8URjtJfEV3c1rlWQI7saZdPTBNKR2FS8INxRva8lgnPJFamWQEyEfmmYlLYFfFdT-6S9X9GSkVT2JvYNrHtW-nCXEntiRx3h9DbQGNRez57Bv0AylflSyPVxyhW0jy6588g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل طارمی به بلژیک آفساید شد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661988" target="_blank">📅 23:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW_ZtOsoZ19_zuDF8iogaeRjLGcheyVWYEHwwPLHrO04ushKOeKOPxjl1EyI7URLPva62a1waevA2arYXLzarSXXEViP-HKmBIHHdzH1bulKuA2jnBNZYXStHPiao1emo-xEN_AF9HfEpzH6nTFfGO7LyBZ6iRD5LJ1bZHsQvHOUw4OxZ5ieq6ytb_iB3zp_a0yIlpyJMlOg4pGJoMYH8R6plmWJc23UOcepA8thsXOI8j0zgaB01gw0rkRotOsAHHJ-xV7uqA9OvhQWell_tp0OLwdxGfTt__v6a0S7GwZ0f4mZtvzrAuyIO0KkpZOl_qGV9V1mk8arPmO5BBvPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اختلاف هیکل لوکاکو با کنعانی، بلندترین دفاع ایران
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661987" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23739e048b.mp4?token=ck9pip2giJQ4tiip400VQqACsHcvq0aNm49aLxG2BEh7luqHzFgYixVbjo4r6wTFl9waUmwEmj-DXs2dHxT2DwWSju4bojy4IjaxMXDKS5LkQqpz2g2H3snEr-vTs8iSHaQcjFT1GGByn9CeQDw7iG8bsh4gudeqzYSRI23BIp8Q32xDNZ1ETIiFjA5O_oqOirRwnPE1jnYLfH5TbYZZAEJSzs6ZdHluQyGym5uHb1jLNytC-Smi9qYIznpAIDyEQbk6cCV__VseJYh1eFLspi_GJR4wDHQr8gl_PmFg2LJSCEcF46jraoyXAKozltbc7ddFiJs3njSDSWjbzY2B7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23739e048b.mp4?token=ck9pip2giJQ4tiip400VQqACsHcvq0aNm49aLxG2BEh7luqHzFgYixVbjo4r6wTFl9waUmwEmj-DXs2dHxT2DwWSju4bojy4IjaxMXDKS5LkQqpz2g2H3snEr-vTs8iSHaQcjFT1GGByn9CeQDw7iG8bsh4gudeqzYSRI23BIp8Q32xDNZ1ETIiFjA5O_oqOirRwnPE1jnYLfH5TbYZZAEJSzs6ZdHluQyGym5uHb1jLNytC-Smi9qYIznpAIDyEQbk6cCV__VseJYh1eFLspi_GJR4wDHQr8gl_PmFg2LJSCEcF46jraoyXAKozltbc7ddFiJs3njSDSWjbzY2B7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل طارمی به بلژیک آفساید شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661986" target="_blank">📅 22:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آفساید اعلام شد متاسفانه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661985" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روی حرکت تمرین شده چه گلی زدیم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661984" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73299ac475.mp4?token=sq9aadrsXJ76c2tQ56u9A1Hdz1dpmn4TdU96bJU1UnZU9PS-YTJZujr9skkMUDXKO0wZK75u25mnnqS89AWnZ3wljWriBvFN7mcu31cWyhYFkMPAN_RqX6v0xFKJ81LH1So6ycq_OY3xKZ-qLHLSAq9YJflHPKVXVxJk-q2XD5aA-e8VkCbIVSW68QxDgunF7XYktqM8DGTQ5Op5NlfY0OvhreEm5Dyanw44nE3Z1k5HaT0Oigs7NNI_q80B13zdZSU-BXe8m_BUMfXvGBqS3zqWjOPEFfoxDIqeqB95DmsIBzHcC_m8Epz_DdlhnhdyR60kDYOkuDNw0OuWbR0Q0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73299ac475.mp4?token=sq9aadrsXJ76c2tQ56u9A1Hdz1dpmn4TdU96bJU1UnZU9PS-YTJZujr9skkMUDXKO0wZK75u25mnnqS89AWnZ3wljWriBvFN7mcu31cWyhYFkMPAN_RqX6v0xFKJ81LH1So6ycq_OY3xKZ-qLHLSAq9YJflHPKVXVxJk-q2XD5aA-e8VkCbIVSW68QxDgunF7XYktqM8DGTQ5Op5NlfY0OvhreEm5Dyanw44nE3Z1k5HaT0Oigs7NNI_q80B13zdZSU-BXe8m_BUMfXvGBqS3zqWjOPEFfoxDIqeqB95DmsIBzHcC_m8Epz_DdlhnhdyR60kDYOkuDNw0OuWbR0Q0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عالی دیگری از علیرضا بیرانوند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661980" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477a09a103.mp4?token=HC_nf-xmcAD8Sicte4QJWnS-7eVwRvtygOGyw1HUamti3tH6ZVbdaZA0NQN064swHCrSSUvc6Cr5gEcjXFZfPFk8iSd3F2d0UInDiUqv8_IvVilmkw4ujdv4BXMuO2bRuhBHH99ntVCSVg4O8YNCH7VGblsHBB7YDKT0wFpjN91S4rgXAxQse6WxqsRvoeLdrCQ_ml_MdSPQb5fWz8Oz5-Bc_2awsF9wrVMK-AttT3iSWc8oam-TfWPABQQh4zBDs2tB_cXq_pXr2SPKhsXj5v2eHGNX7IMoBBbNR03SKrrWE6W6ZQ_hQIY7N0bsumf0Z_Da3wZuZWjsHArHmcJ2Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477a09a103.mp4?token=HC_nf-xmcAD8Sicte4QJWnS-7eVwRvtygOGyw1HUamti3tH6ZVbdaZA0NQN064swHCrSSUvc6Cr5gEcjXFZfPFk8iSd3F2d0UInDiUqv8_IvVilmkw4ujdv4BXMuO2bRuhBHH99ntVCSVg4O8YNCH7VGblsHBB7YDKT0wFpjN91S4rgXAxQse6WxqsRvoeLdrCQ_ml_MdSPQb5fWz8Oz5-Bc_2awsF9wrVMK-AttT3iSWc8oam-TfWPABQQh4zBDs2tB_cXq_pXr2SPKhsXj5v2eHGNX7IMoBBbNR03SKrrWE6W6ZQ_hQIY7N0bsumf0Z_Da3wZuZWjsHArHmcJ2Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش سرود ایران در لس‌آنجلس
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661978" target="_blank">📅 22:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f0643270.mp4?token=VlCzCyW5q4l5soAotk8QucrRlrmgQQ2UOYUsLQKYvNdPVJxhz7o0qFWmsJ2qaqxIM3CD2XP6LGGOypXL7VoLs1n_SGtMpyW3yVwwNY2jBZWfVvE9Ra_Ybdx1JnRG26aGqiaQBqcX4rEO5H5QeVRgLK9s82tLZp5Fu7yfLOTO9BRiAGKKduVgcKZsTfUN84WZ-0wxXO-5YF5u--QUJvVyJ8h4cswm5RJPiiOxL2n6GUZnksRoFCm25TtjHksPspCSvE56DwTYufSRK6KRuBIgl6rC48_gTwV6-fE8OSVdQcerzEcdTwFXmNRrR6D3U5sRkyG6tGOPKSt64OkVb1LK7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f0643270.mp4?token=VlCzCyW5q4l5soAotk8QucrRlrmgQQ2UOYUsLQKYvNdPVJxhz7o0qFWmsJ2qaqxIM3CD2XP6LGGOypXL7VoLs1n_SGtMpyW3yVwwNY2jBZWfVvE9Ra_Ybdx1JnRG26aGqiaQBqcX4rEO5H5QeVRgLK9s82tLZp5Fu7yfLOTO9BRiAGKKduVgcKZsTfUN84WZ-0wxXO-5YF5u--QUJvVyJ8h4cswm5RJPiiOxL2n6GUZnksRoFCm25TtjHksPspCSvE56DwTYufSRK6KRuBIgl6rC48_gTwV6-fE8OSVdQcerzEcdTwFXmNRrR6D3U5sRkyG6tGOPKSt64OkVb1LK7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر سعید عزت‌اللهی به شکلی خطرناک به بیرون رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661977" target="_blank">📅 22:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279d69b3e4.mp4?token=Vj9-71SwPK4GfdwX50Bqc-FG-jBrjZZOxcuv8nCyC1_INhQDaNKj22aTvdKrSQdN1s73FuGmDAVORMt0Mi0LJb7aeWazD_DIN8MOHO1vn2UcIIU8hk6tztd0NNfD-3X8muOEWZ8tFqkpcbqz_EmlMMEH8AWNskK5N-HMIOiQ3T-ns2nzMo7WUAxLYj-bYFANgXP4DkclItp04hU5gRqi1WxDxjfQH_Jl2s8n8TFLiu1yQuVJZ9QRdH1W6BGiBJUz7to3t0fUjbGzSSBYwY33MjjAWkpG-2r6_1dcZ9du-_zNeZSnbLgGnG8D6106dMzF3cLiER4R8EDn6TkndqZ-Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279d69b3e4.mp4?token=Vj9-71SwPK4GfdwX50Bqc-FG-jBrjZZOxcuv8nCyC1_INhQDaNKj22aTvdKrSQdN1s73FuGmDAVORMt0Mi0LJb7aeWazD_DIN8MOHO1vn2UcIIU8hk6tztd0NNfD-3X8muOEWZ8tFqkpcbqz_EmlMMEH8AWNskK5N-HMIOiQ3T-ns2nzMo7WUAxLYj-bYFANgXP4DkclItp04hU5gRqi1WxDxjfQH_Jl2s8n8TFLiu1yQuVJZ9QRdH1W6BGiBJUz7to3t0fUjbGzSSBYwY33MjjAWkpG-2r6_1dcZ9du-_zNeZSnbLgGnG8D6106dMzF3cLiER4R8EDn6TkndqZ-Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عالی تیبو کورتوآ مانع گلزنی شیر بچه‌های ایرانی شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661976" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چه فرصتی رو از دست دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661975" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9dbd175a.mp4?token=W_xVsmvpH6kddFejNVEOCN2OlOxRsYi5EGIfg2QZ3ZTvwwOr6ISKwIIrWCzwERmniK0ZRO_LvJg84Dy_KAGIqiTGfY-ekAHjf22xnCr6qUr0NYlsa2DYuy3KSqeUS7yPQ82c33wUNwUDdJkoyC36D4k4WZVAMONeKmofZ1gDT5goWWfWgLTN5Uw3OFIFIzMSd8SPicf4AiSbZdU3dS9wgfvAVCDfYtQgGQUewjCCrAd-d0Vsd1TAAYlOSd7ti6AfrxDVg-MRROvJ3JyXT8rDsLKnuQYN1kxQ7ad-dJXBo7jSX4Fw34M8PzoXL4rBJefx1na18FrkIpoHJnbr6jKSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9dbd175a.mp4?token=W_xVsmvpH6kddFejNVEOCN2OlOxRsYi5EGIfg2QZ3ZTvwwOr6ISKwIIrWCzwERmniK0ZRO_LvJg84Dy_KAGIqiTGfY-ekAHjf22xnCr6qUr0NYlsa2DYuy3KSqeUS7yPQ82c33wUNwUDdJkoyC36D4k4WZVAMONeKmofZ1gDT5goWWfWgLTN5Uw3OFIFIzMSd8SPicf4AiSbZdU3dS9wgfvAVCDfYtQgGQUewjCCrAd-d0Vsd1TAAYlOSd7ti6AfrxDVg-MRROvJ3JyXT8rDsLKnuQYN1kxQ7ad-dJXBo7jSX4Fw34M8PzoXL4rBJefx1na18FrkIpoHJnbr6jKSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش شعار فیفا به زبان فارسی در استادیوم سوفای لس‌آنجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661974" target="_blank">📅 22:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7675c5a41a.mp4?token=UlaNUy7vYIiH5tgSRD8iqXnMXhgUtt7yzmTkCHltW5wzGpCgAQPnEOgi_5yzHeM_-9CXTbwRxWPUw1vWWP260SDvreA-ZkgMaEulNdejTJiw_9x6StYQPVY4Fnh0ud1pjGF7Jcj_dHacVrfd2qDztjX_CS4xWkX5BUdaYoBZOUUaqMH8SPNvzBTZ_kc_rDn5Gffo3AF9qIvyreLP6F2jlrtCnXRNpzTb719r0By4hW-iRuC_lnAiNKRlS9FPnjpKmKhATfwLqbmxovUeN8iaP6zv062hU3PcbjaBk5eqA1qxDLKuOZxDqLVy84UNV1nO-djujh_eepwBVBOTOFj1DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7675c5a41a.mp4?token=UlaNUy7vYIiH5tgSRD8iqXnMXhgUtt7yzmTkCHltW5wzGpCgAQPnEOgi_5yzHeM_-9CXTbwRxWPUw1vWWP260SDvreA-ZkgMaEulNdejTJiw_9x6StYQPVY4Fnh0ud1pjGF7Jcj_dHacVrfd2qDztjX_CS4xWkX5BUdaYoBZOUUaqMH8SPNvzBTZ_kc_rDn5Gffo3AF9qIvyreLP6F2jlrtCnXRNpzTb719r0By4hW-iRuC_lnAiNKRlS9FPnjpKmKhATfwLqbmxovUeN8iaP6zv062hU3PcbjaBk5eqA1qxDLKuOZxDqLVy84UNV1nO-djujh_eepwBVBOTOFj1DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرصتی خطرناک برای بلژیک که بیرانوند توپ رو گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661973" target="_blank">📅 22:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a241d9438.mp4?token=UUUxd7A4ZczMfvT43_mSmxDM7Zk_c99JSMiCdqYrWeIZWDQmr6JwnWiM8E7Lpu9wO0Bw0q2ItVdSgT1jNYy3VBuXRn929kVTwF6pZuxTlmN4Nsph7O2bqj2Vc5eeu8ISTkilGA0GuL3W5CqF-WAtSFoaj0sGWLNDHgAQSLW0u6S_FjlfsbjqtfK-1Q8jZpv76RGJT3QLamP-SVqdJccl9cZuTG5zdwqIaYhUUzzuuNtavF8tPSJa-iItuTflB3PXNcAgdcic97vFnNaP588ot4jClCX_OMxi4zs24_eHLLKGeS1liRCxrpgOMFJ0p02vcrzbBhTk9FR31dq6Qin_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a241d9438.mp4?token=UUUxd7A4ZczMfvT43_mSmxDM7Zk_c99JSMiCdqYrWeIZWDQmr6JwnWiM8E7Lpu9wO0Bw0q2ItVdSgT1jNYy3VBuXRn929kVTwF6pZuxTlmN4Nsph7O2bqj2Vc5eeu8ISTkilGA0GuL3W5CqF-WAtSFoaj0sGWLNDHgAQSLW0u6S_FjlfsbjqtfK-1Q8jZpv76RGJT3QLamP-SVqdJccl9cZuTG5zdwqIaYhUUzzuuNtavF8tPSJa-iItuTflB3PXNcAgdcic97vFnNaP588ot4jClCX_OMxi4zs24_eHLLKGeS1liRCxrpgOMFJ0p02vcrzbBhTk9FR31dq6Qin_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
لوکاکو با انجام این خطا روی بیرانوند کارت زرد گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661972" target="_blank">📅 22:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661971">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
واکنش فدراسیون فوتبال به اظهارات دروغ وزیر امنیت داخلی آمریکا
🔹
ادعای مطرح‌شده مبنی بر اینکه فردی به عنوان مقامی مسئول از فدراسیون فوتبال ایران روز گذشته قصد سوار شدن به هواپیما برای ورود به ایالات متحده را داشته و از این اقدام جلوگیری شده است، یک دروغ آشکار است.
🔹
این ادعا به قدری بی‌پایه است که مطرح‌کنندگان آن به خوبی می‌دانند چنین اتفاقی اساساً رخ نداده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661971" target="_blank">📅 22:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661970">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شروع بازی ایران بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661970" target="_blank">📅 22:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ لالایی</div>
  <div class="tg-doc-extra">عبدالرضا هلالی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/661967" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
بارونی تر از یه بارونم
بی تو مادر من نمیتونم
اگه دووم بیاری یه روزی شم یه روزه
خدا بزرگه شاید یکی دلش بسوزه
🎙
#عبدالرضا_هلالی
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661967" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoTfCXc5-tdmx0K5Oep1RJKDtlyHn7bS_OjsA1RGKM6dQXLn-MsscHmE9iteeJRTawuHqAPnk-SZFNhTSu90IectSJbqSN19oYvMtImP6GR9RlODdSW3e9kN6Ajx3gUsF5uOCelVWRvjRY0DwqnLPztavyvHUq8QbKkmFs3ll_uFJWyAbUQD4daqbfg15X1fzny7MqxWPTvGubT5_qc-2D-_MUdeQLffBduvk7l5eDm813qGws-N44lOzUi70AR4iFY2z0TV9jX1ROmQdFJZ4xUmJGAf3fTQi60YdCG5OECmW-W_aOT11Iw-ni6xi_hndsGvyqio3eNn1UPRVdOcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byjmhT0Dc4heafErssTWIqr59cpUrHf9CuULkaO3X6oIAdgtKqReip7PEBUHlu-0fUZ-RjiPL81qGMUEB2GaUZPajE958wsgMWny6uPv889nIa15WgBQz75baIkQ7Mj0i4mMQwLqpnHAXm3b4NM0BeL-pwLnSPfO2dHkgp1Ipo6-3w5HY5Z46So9lgsZm5g6UJFO8KwdNeNhBaGYcbPQj6d4cek4dRlGElnxetCNOBXh3Mb585zU8f4DvO2GNv81C3Yemh8Laj67GkI17mfF1JyDBDyYKc41xOp5vxILmprmjeQErfCxhZryLO9hllv8VPCcMdI2GfyRN2iidwryIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وضعیت ورزشگاه پیش از بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661965" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzsK-VvgL96cPBcEqdFJudyVZ2Ydm5zAMzpb2_mwn3aNpMbzjVgvZdAOQZWhpP6WaQIuQkUzkXRLJKGcFgJEO65p1f-AMfs69Q-gsES3C6wOTbco4-rsKGM63gKjbMgveOvfw-z6X49b5VkQdE5lgYVY5Gpc4EOQCrAW6pviZLDu2jUjH_SUGIheQB0ho7NagChO1A08EUH1vP5Iy0jZEcEkpS2C_dIq6yzDFon_b22kbF7aGX-e5eUaeji2hcM2MIRkjSjJsJeQQhFat7uGhAtFj6ZSkHaPyA9memQY6OkiwJ3NWqRFZq0Ope4xxeeGDHfl2KRQ4ZWxngfIR6tiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنیا؛ گذرگاهی برای رسیدن به آن‌جا که جان آرام گیرد
🔹
امام می‌فرماید دنیا جای گذر است نه اقامت. انسان‌ها دو گروه‌اند: کسانی که دنیا را هدف می‌بینند و آن را قرارگاه می‌پندارند، و کسانی که آن را وسیله‌ای برای آخرت می‌دانند. دنیا همانند پلی است که باید از آن…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/661963" target="_blank">📅 22:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98beb6aba.mp4?token=Wl1hv5FPZykvqLUNXlfKGVz9g5UbKA29g5rwPVXvbCo2kwp5jZFx99gt1y9HcuIjVNlcyt0u5IWSRvZ_ab3mc31iUarwwPh-Qo3ICNIuz-hmq8JKx98gdbaKfOYZ4xXatL342lTLr0A3q_jyyS_MvNH1AAG6196dh2vqLuD84oukk3OTSA6lIYfHw49p9wu9xeZ5XoJXEH1wTzpO_yJk917KnbVnFoX3P7P1Eq2Yvg2iYJIAOs9_bOeXrLi92IV0OGiEMEl7AvYkisfrXPPrj3wYGqrVWdNx6ys38jI27wGh8FPOeE8QNz-X9yWxB1IuIlCBj_kG0WC3oDFQWVYPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98beb6aba.mp4?token=Wl1hv5FPZykvqLUNXlfKGVz9g5UbKA29g5rwPVXvbCo2kwp5jZFx99gt1y9HcuIjVNlcyt0u5IWSRvZ_ab3mc31iUarwwPh-Qo3ICNIuz-hmq8JKx98gdbaKfOYZ4xXatL342lTLr0A3q_jyyS_MvNH1AAG6196dh2vqLuD84oukk3OTSA6lIYfHw49p9wu9xeZ5XoJXEH1wTzpO_yJk917KnbVnFoX3P7P1Eq2Yvg2iYJIAOs9_bOeXrLi92IV0OGiEMEl7AvYkisfrXPPrj3wYGqrVWdNx6ys38jI27wGh8FPOeE8QNz-X9yWxB1IuIlCBj_kG0WC3oDFQWVYPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم ایران در ورزشگاه به اهتزاز در آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/661962" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم، انجام می‌دهد
🔹
و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد، انجام می‌دهم؛ هیچ‌کدام درست نیست. #Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661961" target="_blank">📅 22:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLcJlFzC8BNhUZhikicffOae0sos804UC7EuhyECp9FGLtCKcSA7UrslKFDm03iyfUfpRKRJFYc3MH7NBC1gOY6zuNBFzJDY76aAqjyejr3mURHbYqtuTY4zcLZxjpIenG8uBKBI4dMzxgwyv8lRaS2CETQriALU4Psl_wMu2YgxIfP6zU-258fS1NfeVUyKFoh1OsL-_l8fIX4ixXkHucbTGxV-RLO0PEzaWS1zvjPYwfVoHoeC4GH_XwJwO7H5650_e5_RRbKQdhNcRjRgfHuDTX5wWIolvUemKswZXfiSGrZ8-gnVC94MqMRfjXuY5IFQEHSNI-N5TGBy5NUYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت هوادار مکزیکی از تیم ملی ایران در ورزشگاه سوفای لس آنجلس
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661960" target="_blank">📅 22:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2ddf754c.mp4?token=PtcOzNUKm5q9e-Rf23N-FHquIEBVZefFQLhBkcEQdRUPlopJnaS7eBm1h5jhmcI0W8eREavuHj-bOFu-tY0csUiE4MZcKDBtYNanaFBxl9wL4jWaqMhFPLXN74okDiH7Sput90wNhDo-uh_vFioqKZkBhEfq-WzJ15Qo1hld2QkK36wHiyZtdf_sOHTYX8UKpX6hDDPpWtJeVwEH6HQ3T5hYRx59t-qCd_2UDzK7ebUCn0yKh3TuigeQHf08PRk6vT-mZy_-yzTMo7wUyiBDeaB8nx8q4w4zQA3y4eVvFxf90B1Zqk5orKH5wrs8lkWznEhmWzUrkAerH5w13Cs3OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2ddf754c.mp4?token=PtcOzNUKm5q9e-Rf23N-FHquIEBVZefFQLhBkcEQdRUPlopJnaS7eBm1h5jhmcI0W8eREavuHj-bOFu-tY0csUiE4MZcKDBtYNanaFBxl9wL4jWaqMhFPLXN74okDiH7Sput90wNhDo-uh_vFioqKZkBhEfq-WzJ15Qo1hld2QkK36wHiyZtdf_sOHTYX8UKpX6hDDPpWtJeVwEH6HQ3T5hYRx59t-qCd_2UDzK7ebUCn0yKh3TuigeQHf08PRk6vT-mZy_-yzTMo7wUyiBDeaB8nx8q4w4zQA3y4eVvFxf90B1Zqk5orKH5wrs8lkWznEhmWzUrkAerH5w13Cs3OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرم‌کردن بازیکنان ایران و بلژیک پیش از شروع بازی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661959" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/790c0b912a.mp4?token=L5IUtgkyUkADQd69G1z04fj0Rcmu9sKnufpJdo5d3t_0vpdvnLaPV2IHWyf27xMQz-OWP4qZjBuW1adeF-FfBq_INiSBiK6cPb5QhDKBsm8ICtPVw5hi-57GewiHpJWUKyoRiJ3YN676LZzRq0Ode3Y6fsGqKhni-F3dtFo6wWj_phu8KoU38DHrnXolrmkQMFtm3HgOY9O7-ta8P46BPcPZxENscAVCn15CHb-VaJJNQEwBmzwuRyLX0heZlIODHCo2pMVfGIx2pCWtvNCoScuhkZjgVtAQJ0rBrJqsZHXBtSkkp0JP4Ar6FNeZQnOahFYmODTTaHvOioTEI8Gt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/790c0b912a.mp4?token=L5IUtgkyUkADQd69G1z04fj0Rcmu9sKnufpJdo5d3t_0vpdvnLaPV2IHWyf27xMQz-OWP4qZjBuW1adeF-FfBq_INiSBiK6cPb5QhDKBsm8ICtPVw5hi-57GewiHpJWUKyoRiJ3YN676LZzRq0Ode3Y6fsGqKhni-F3dtFo6wWj_phu8KoU38DHrnXolrmkQMFtm3HgOY9O7-ta8P46BPcPZxENscAVCn15CHb-VaJJNQEwBmzwuRyLX0heZlIODHCo2pMVfGIx2pCWtvNCoScuhkZjgVtAQJ0rBrJqsZHXBtSkkp0JP4Ar6FNeZQnOahFYmODTTaHvOioTEI8Gt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مبلغ کالابرگ دهک‌های پایین حتما متناسب با تورم افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661958" target="_blank">📅 22:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم، انجام می‌دهد
🔹
و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد، انجام می‌دهم؛ هیچ‌کدام درست نیست.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661956" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85284b726e.mp4?token=W2pynXlGYa-1M-NGUPMVGAYqEUA7SifaAMQLG28OH58JrIHwqwCZsg53i7dv3jLLfSb9DN8yaMsyVEmqRNGwYubgVeyZBkVJ8fZIAp2yOI-bneUfqzCh4FxycR4iOlVs9LuTn4thtVD316aRH60Jfj4v8dXqwSprRPPRTBwOEP46bghLisG2ooaeCXsJ08lQZdCHF8FX9YKbZwGR8dAJR6HIDRacoVnwSww0E3me1btvzYpLZLWIbvXJMWTgHjLXLY-8w7oaWp1Prlf0m3ZZ0ZJ1xxHwWAfe4TeTIK30U9O3b6zEJEAaK-ehsJD2Jp77B6cliZ1qL0fzVmGe7FksIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85284b726e.mp4?token=W2pynXlGYa-1M-NGUPMVGAYqEUA7SifaAMQLG28OH58JrIHwqwCZsg53i7dv3jLLfSb9DN8yaMsyVEmqRNGwYubgVeyZBkVJ8fZIAp2yOI-bneUfqzCh4FxycR4iOlVs9LuTn4thtVD316aRH60Jfj4v8dXqwSprRPPRTBwOEP46bghLisG2ooaeCXsJ08lQZdCHF8FX9YKbZwGR8dAJR6HIDRacoVnwSww0E3me1btvzYpLZLWIbvXJMWTgHjLXLY-8w7oaWp1Prlf0m3ZZ0ZJ1xxHwWAfe4TeTIK30U9O3b6zEJEAaK-ehsJD2Jp77B6cliZ1qL0fzVmGe7FksIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم ایران و فلسطین و تصاویر شهدای میناب در دست هواداران تیم ملی حاضر در لس آنجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661955" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
توقف موقت مذاکرات ایران و آمریکا در سوئیس
ادعای سی‌ان‌ان به نقل از یک منبع ایرانی در سوئیس:
🔹
مذاکرات میان ایران و آمریکا در سوئیس به‌دنبال تهدیدهای روز یکشنبه ترامپ متوقف شده است؛ با این حال، رایزنی‌های پشت‌پرده برای بازگرداندن طرفین به میز مذاکره ادامه دارد و این روند به‌پایان نرسیده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661954" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661953">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ قمارباز: از اینکه اسرائیل قادر نیست حزب‌الله را از سر راه بردارد، ناامیدم
🔹
نیروهای اسرائیلی بدون تخریب ساختمان‌ها عملاً کار دیگری از پیش نمی‌برند.
🔹
در حال بررسی سپردن مسئولیت این موضوع به سوریه هستم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/661953" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUY5Q2PtMO1Q3K0xOpW2CQ-mxsRLJAtpev6ohzfbV3wyTMxwms-da522DeYkhP8RKaL5PEgQqsh5i36Oq88pz8YO6LUZnGbd-SkqmHftyPKYKEXa4qmLdPnFPE5i58lrWjk_jTV28gdeeyM3mIuXyf3d5B3myKP1veWHOdxnMYv2zLi9XiVKaMH-nNh3iDZO6gcTP_ND7u4psMyGaxozEbSM57JfRlTjev3Ul6DWc7qpnAqwKDtfTGVl8faHi2tisCrDxu0zu0ZFVPbPRn0xa-H_GYVyvmVf-HOOHlt_T1OuON-7tvgO7vRSGTQhzNxqD7a2LJ_pG7E_eSJgAFlaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با دیجی‌کارت دیجی‌پی خرید کنید و پول‌تان را پس بگیرید!
🔹
دیجی‌پی به عنوان ارائه‌دهنده خدمات پرداخت، با معرفی دیجی‌کارت وارد عرصه جدیدی از خدمات شده است.
🔹
دیجی‌کارت محصول جدید دیجی‌پی است که ترکیبی از خدمات پرداخت شبکه بانکی و سیستم کش‌بک را ارائه می‌دهد و هرجا بخواهید می‌توانید از این کارت استفاده کرده و تا سقف ۵ درصد از مبلغ خریدتان را پس بگیرید.
🔹
گفته می‌شود در صورت توسعه خدمات، امکان اضافه شدن قابلیت‌های جدید مانند خرید اعتباری نیز به این کارت‌ها وجود خواهد داشت./ باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661952" target="_blank">📅 21:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
کانال ۱۲: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود./انتخاب @AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661951" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uF1Czo3VtAmpoW-l8kJwR0yvRql63KC8J7vLXZmswlYApA8CkWZiKJBT8im2JtMfRNZ2kLulBM3Zm_dElCX_TLp4mztDB4pMTR6ymrXc4iC5yhoheIxy-V9LqzDdMmnEzU9F59cDC289r9UJ9iYgBje_aQzJXfYS-mPoDp3WY59PhV5RK8lL2u27-_VQ82M6ofHMxjnuvHhEgWwvuUuB1IRwBanzwWqmYiO6KLE2MTxQId_ieOwv2mCaj12H3F9yq3HA-6KOKeb7TaFuxxNdyaS9GBCZ573Hi1RSiO-VMsB5EKjD_7pmhEXaQljQ7wI4nAGLmME2LrJukmxRKM35Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsP9QwFAAsPtvWOsze28XXMnJ3Y6f4DZWHJaZcwrGNI_NSU4Fi1xykiA8L5irXLUtVpu9qg3o--O_kNnMMsgwLfmqahkNgn-Z390rT5BGxw_chEdewp4npvcEYMRlpY2Y-qXkrlq8VmFC9FdPJAuF-GnJo2-UorYYjs1ziZ3wv4wuXUvJ8O6rB-swe-djf924u_tbNOmkVK30LgoINNwT2c6ErcL6gZ_QyLBHjIYc7_TvrYX-dTKZeNwWANndBnuKp355J2ItHU2MIv6PUHOFkZQ3gVUmKT9QgY39p7sRO9JEX-vgqK1rdHOICH0n6oGADXalW-Fmcq4DbSPjV7DGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میکائیل و محمدطاهای عزیز، فوتبالی‌های شهید میناب؛ بچه‌های ایران تو لس‌آنجلس و روی صندلی‌های ورزشگاه به یادتونن و به جاتون ایران رو تشویق میکنن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/661949" target="_blank">📅 21:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
شبکه کان اسرائیل: ارتش اسرائیل شروع به کاهش نیروهای خود در جنوب لبنان کرده است
🔹
دولت ترامپ از اسرائیل خواسته است که عقب‌نشینی جزئی از جنوب لبنان انجام دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661948" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اهدای پرچم گنبد حرم مطهر حسینی، برای تکریم و بدرقه پیکر رهبر شهید
🔹
عتبه حسینیه در عراق پرچم متبرک گنبد مطهر را برای تکریم و بدرقه پیکر رهبر شهید به سرپرست سرکنسولگری ایران در کربلا تحویل داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661947" target="_blank">📅 21:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جولان نظامیان رژیم صهیونیستی در خاک سوریه
🔹
منابع سوری از نفوذ یک نیروی نظامی وابسته به رژیم صهیونیستی به منطقه الاصبح در حومه جنوبی استان قنیطره خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661946" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-text">🔴
امشب یه اتفاق عجیب توی بازی ایران و بلژیک قراره رخ بده!
این کلیپ رو جدی بگیرید و مراقب قفلی زدن روش باشید
😁
#ایران_روشن
💡</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661945" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ادامه‌ برنامه مذاکراتی هنوز مشخص نیست؛ واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس‌جمهور آمریکا مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661944" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e68e530.mp4?token=myfx3vjqUlXaTLVUbPZ148-Rp_qxnb0sttwDZJCCiR2R6E0O-xcY8LFs_f6BhQlLNlsu7PIsNvGdJWHTETklwpfEueIAskz8PdJqDjDWAnbiFouBM_lIYykaBtL9b6m7IzAsy6FBfmAyCfNx0wCOiuD_y6pptFh9v4AOAjd0EKqEAto71NAMqPzu5-pkOPeht7p-hpOKS7xJ4b65hM-CMl6jdQdZ5JHiLUy0eixGr8-PFSasHbQEB1uTEXnhsbzpXI3p0mPYuXqrw3D35gbR3l-zVLze6c2VrG9ZsOMU-YsUgB519U6Zxqgpnti-iHzQgG0tB8e0QZ_OFkZZWdFMl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e68e530.mp4?token=myfx3vjqUlXaTLVUbPZ148-Rp_qxnb0sttwDZJCCiR2R6E0O-xcY8LFs_f6BhQlLNlsu7PIsNvGdJWHTETklwpfEueIAskz8PdJqDjDWAnbiFouBM_lIYykaBtL9b6m7IzAsy6FBfmAyCfNx0wCOiuD_y6pptFh9v4AOAjd0EKqEAto71NAMqPzu5-pkOPeht7p-hpOKS7xJ4b65hM-CMl6jdQdZ5JHiLUy0eixGr8-PFSasHbQEB1uTEXnhsbzpXI3p0mPYuXqrw3D35gbR3l-zVLze6c2VrG9ZsOMU-YsUgB519U6Zxqgpnti-iHzQgG0tB8e0QZ_OFkZZWdFMl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات آخر در ناو دنا دقیقا چه گذشت؟
🔹
روایت هولناک یکی از پرسنل نجات یافته از ناو دنا در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661943" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YylRNuW-jP4hf48R0zRkTAAcFf54g6lo2vEoKlbWGPLudib9LAIMMjHgZ7JBenCUWHEYnw4r4P3X0QplBGmcgzsKCl14-l_WkVknjMR8hKf7_knt1Zdx_G03gTzNGzdGkn04fMMFrVl2FAnANf8sGbdfbLxC33X9FiYDutCWMXYnn2UuL_sdkI2sAaOABBd3zsbq0KMMpI8FqStItlXIRsISlBBlUUXyVIfgZDOdFw0uh-OY8AjUW2XRQCrc5EWWHB2xI8QyAoZfsHK4J6CdeeSI5ggelBTyIEyxAY5Fx2rAr0tqeu-ygkkM9TS9D7z-6b1zT7p1DT8MM9B5o8NooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچمی که معاون رئیس‌جمهور آمریکا در مقابل آن قد علم کرده است، پرچم بلند آوازهٔ جمهوری اسلامی ایران است؛ همان پرچمی که آمریکا سال‌هاست در آرزوی براندازیِ آن، نقشهٔ تغییرش را در سر می‌پروراند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661942" target="_blank">📅 21:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ادامه‌ برنامه مذاکراتی هنوز مشخص نیست؛ واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس‌جمهور آمریکا مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661941" target="_blank">📅 21:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOMR2_jerdMjHFhaRyMKoaP24xQyUd9CNXOZ7RSdYLLHGoWtUg1ipMJOwqnRobSRUxwUBbOKx7Wexm_27WxHUqDJaPCFXju6ODWLC3-5X10wnZ1Wo6_sA4Jov5YwF5uf54RCUf8ceef1dQEfdeGrRuW-sOGGtr19wO6_jXWZBYyFmzup955G9TTxPl0PxECi1DyDewgqW2pGthbcJD-P4h-Pyk2vdh-K3wdAyAR5S38VO_xeeOQr0KOd5yqt30QhYe_JupDcZBDxCGYZAvLqHI1O77KeDqm0NWreJGT8RIPaFeO4sGReYtphLrEEJqcETuYVmcTPbYUlTM-CNsrYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RM8CqTyxM5Czbiq86nZHjUotjcs86GHLu4vF_6hN4Lot1S3eVm2h6SUrsLWYI7XoN9eXOPicPY2uCgMDUsg3dDk5T4yGqncNOZzFq8oIuo1wlwpQp_TFPYRF_XHvKe5SL8_WM6qFIkYe5dyQ-Ie7aoVtbo3CtUlWxPdIwvckJe076x7UPOC5-2dxKC83an7DqRIzDN0D5lvvwksmEYbhDk-v4VVvAB4aNXmmgcgG9El_9zsZxZWvV2Pd2UdRrDYPOzED1iEt4q1L40MppK08qnQz3zFUdTQ53jQj2tgdBLGdffMv7UdrRosDx9kPKi4M76trVXQkX55SuKlOld4RwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1AClHakAgv1Rk6WCYeYFHgn_PNyBqX62whIxIR8CKMbMFaOnuer8M8dmklU3M4bAex5DM_0jTy26M81NB0964t2i8NMEyIphY-wykcLjCwsxctaerAS6G7x0Wv0HenZ_o4kxbkGetfeI-EHfgyEeAtcJ6SRfyIvPue68y7AtKJ-Jh7FHzmTP-IfnG2wZEf3k1yK27jpZa6TzqMPckYO8ykZIkuL9bJZ7Gliofbdf1-ZkhlfjeMrwUj9y7_vXLpzhJkpegNheupX_8lxuT2zn8hl2-J-p3f6Y2zdf3L-QRAXfniYLZvokhJvxPKTWWTTNvyRHaV3oW9QVzrojEBSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw7LtKIcMa5kngG9ZQ-XGcr1t6OJEPhGo_rUMZnwelGlCIwnA3PAt4ww2okued0-nrgogZjOuO3dxs3_52nB57k1oBZO2KF23pFfI2JCpe0hs6-_Th4SSEzHnn3sJMGp516e05PSYe9KLd-tQZ1-g0RQwlIkFow1WWHq6q367s8sfZ1_kSNZf76kUgDyc14NcV-4LWddm0a6fVaU2d6NGLxTzaQE-oC1FquSn2jGfq36LNA5DGZ8mTV9vqZ9MxILX6PwLISF-CSo2W8Wh2GcABdEJYlGoZ05N5s9ihAo0And5PBi_jZxqATCG6ufudnV2v8H6bmCpvPw8G8yZcSqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_JTvxHiZyhZg_F5CUpqltr-Leblh3fOggK1TqObcda-CBaxHjH4QuGI-ia7o3bWpX3jj2YWsquWJrcZ413BQvVgY1OSQ-Tc-Phax1P1QXUj510Z9vLarcgjwYlq8PxdFHOlWptYpvow61O7Qt8a54dMDZWtwyryaoJ--CJA5YeLZcfjWnKhrq61vWTSRN9PiXqiUtHEi-tkqdd-g60Ac5jAlr30Xjm0XyyIat808aucT-kdQKfjSzCExPbtL5HTSCWH_J6POD-_u91IMd0g3Le1gPB0PDQQZmZTi9w_6HsCdxNV7Yxy-D1hEogV53KKpztokihvfSqoJuz1ImGusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bS8zGNzFewjGxj0qyronOjUvKW0nq8YXFBCqQm_QqYnIMa1qyMxuzfksQvhjqfn4vhoU4Gmfd12-ycYT49wdFE9X7fu05PfZuY0oSwMEUZT6o_EcJGy8mjHQA0-p5hXBuN1vxytFDw7R1Bcjs6OPDhHU-4S_3aKxGR_F4PNNJj4lrtkbF1LuhkYUINhunl0NBpcPHGwqV2Qpssv8E2s4l2eIoHwst1m5iaYAV-s8qv2aRNmRFReDQfpbS8vJiSnOCJD4-sP-0EuaTuALc6OG2azInn7qqp_rGdr5XykQrS8j80MC8Wdzf4T9ezbImPjk4BhS8TIkmYtnh7aEkcFszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2YaV97Nu3ezSHqWAcn-zDcpT0WXWHlLjXU1FXF5Qk1RK6CEtr9cUD3IiKxCphoTwosob8vocnWc2oaNFRukS-5w6tOQ6oFVzjjKgnRAbzdjAR0zcqjdwqEPbKotHLlwui--Hh0pxEGPEewWf-B-Sb0-52HkMVUlSTB-X4rnx-y1ZxHLVfF55MehPQf6ERfaK_ouYM_UGyPpi2ZAEkw_j0fN7412ipAaJnMmaesJIHBXv_ei4Ie3dtvaOintoYA49mMZmaSYkVaulB5Dd9zb20yRFbx0OJ67pmXhQj-KcjpqF_ndKE-Q030EQUgkNO2C4SC4NNuJA6EAK_4dKtCM-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از رختکن ایران و بلژیک پیش از شروع بازی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661934" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8fazJhRgsPyinHoKOFzPwD8raCa6gzpDaUfi39PHswgFiOZNR9QtfWWA07qiSi7loFm7wU6KwcIFCBYdHVRFBwHbpWKde7UKjB8IHyFjQXvgNKZ7JP3Wj4-d4wqO9iv0vpDSy2wqccWKnxnVTXEWKyecqt1hD89F9j7sWbTFT-q6_59fY15bYzgeYH_2pa_vbdbBHF4Hj5Xer0PEzF7MPTFCaGCSFTJMAqu1MOW3J1B2lqAV-1ABeKWwWmckAv8zQqOICOBfmpUmvXKGBZVPwoPO8VgfJRBt9HsfFFLwizBXPB9a3aCHzmT5qYdbaDzEVHxz_1HwR834TrHS88nfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایوان؛ غول هوش مصنوعی جهان
🔹
ارزش شرکت‌های فناوری تایوان به بیش از ۲ برابر تولید ناخالص داخلی این کشور رسیده است.
🔹
دلیل این اتفاق، سرمایه‌گذاری بسیار زیاد شرکت‌های هوش مصنوعی است که باعث افزایش ارزش بازار سهام این کشور شده و چون هنوز به نتیجه کامل نرسیده در تولید واقعی جایی نداشته و بیشتر بازتاب انتظارات سرمایه‌گذاری و آینده این حوزه است.
@amarfact</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661933" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f5f3735e.mp4?token=ZT3qreQH8ytVY7VgDSgMJMmzhBas-BrSTbBnX9bXGOZ8wN2Pi_Melx09xxWg5pg-jodS-iWsBYKuStgR7aN1wcoJmYdhOnu6ZtO4U1r6hVnMQ-wUybDKtPs47U0TgT1JsyecU2W8f_iS9VxBco_V_1Rw6vH8GcqbW_836RAThrMrwOFOqzZ-JJ1CDr8pLWDJHqFVAM_6mnewfOfcm4T8vgSswFZnbp49bEXChFfuYBc7H3pEnAlVGTHINGi5sVoPvupOGhaPWIjXDRqbZKYxGiiAmbuaIfb8_m0umpVN1il_HKb1vdo-sRtM6HHLGfFwozxudn0eScswXQdZsHDebi8tNR_PucGEjwbfbDS8MxpJ9o7ilFbCUQIUWikmybg51Y-POB548Id0IJsvY9oerRQaPMEwHSV-r0EGo2Lc8JsxG60poKZa-qW0Q3ZWWgFHLD8j93G07Izg7K2mG6753Vt_lV737BrpagH-wMFfogwwHCFBK6iAsgw3laL2M4WH-TMlgtej-8553q1n8Gybo-vHI5zxDPLb6aA7L4C8hH4OB3YsAaD-PzWTOJQuFyBE1NlOwQyNhceIxQPQ_Kln8-aPDbQHcaN5l-HUY9AYcN_uysb_i5QQe2DPnukJulA46kejR2C3UASSFUx8VEGZWNcVUE5bF6ohaSnDjcvxuhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f5f3735e.mp4?token=ZT3qreQH8ytVY7VgDSgMJMmzhBas-BrSTbBnX9bXGOZ8wN2Pi_Melx09xxWg5pg-jodS-iWsBYKuStgR7aN1wcoJmYdhOnu6ZtO4U1r6hVnMQ-wUybDKtPs47U0TgT1JsyecU2W8f_iS9VxBco_V_1Rw6vH8GcqbW_836RAThrMrwOFOqzZ-JJ1CDr8pLWDJHqFVAM_6mnewfOfcm4T8vgSswFZnbp49bEXChFfuYBc7H3pEnAlVGTHINGi5sVoPvupOGhaPWIjXDRqbZKYxGiiAmbuaIfb8_m0umpVN1il_HKb1vdo-sRtM6HHLGfFwozxudn0eScswXQdZsHDebi8tNR_PucGEjwbfbDS8MxpJ9o7ilFbCUQIUWikmybg51Y-POB548Id0IJsvY9oerRQaPMEwHSV-r0EGo2Lc8JsxG60poKZa-qW0Q3ZWWgFHLD8j93G07Izg7K2mG6753Vt_lV737BrpagH-wMFfogwwHCFBK6iAsgw3laL2M4WH-TMlgtej-8553q1n8Gybo-vHI5zxDPLb6aA7L4C8hH4OB3YsAaD-PzWTOJQuFyBE1NlOwQyNhceIxQPQ_Kln8-aPDbQHcaN5l-HUY9AYcN_uysb_i5QQe2DPnukJulA46kejR2C3UASSFUx8VEGZWNcVUE5bF6ohaSnDjcvxuhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور بازیکنان تیم ملی فوتبال ایران در زمین چمن ورزشگاه سوفای
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661932" target="_blank">📅 21:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/811b297717.mp4?token=E2F65jIGk5LGmYsPbldcoabvk_OICXVL3tC9Ms1vsB03_VO2YBWnQ70Ud2S6RfXDASPq_p5tUw690e33mKFzvSW-TJdc3fvp8AXZFN4A0W4GNrTgXYekpKklwcDoP_vr469vnAs2QdwZsTwgtjQsg2f6LGtsJLQifjBlMc7Hhpo6q5qh0ZeTqaJgI4TeI5MZ6tCGOsWH055G1pZq_KOBjyIFN5QVKHe3_C55US6z8Zv3zJP1IjnvtBf3F-3GIz0POopBVM39szt8WzDZSkDhKJ-nikxj7p9Moa254OLv6EByfIhWz9Df64Iqq4uPWGkU-WlkXbF8ZbcDFBPe_C_7PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/811b297717.mp4?token=E2F65jIGk5LGmYsPbldcoabvk_OICXVL3tC9Ms1vsB03_VO2YBWnQ70Ud2S6RfXDASPq_p5tUw690e33mKFzvSW-TJdc3fvp8AXZFN4A0W4GNrTgXYekpKklwcDoP_vr469vnAs2QdwZsTwgtjQsg2f6LGtsJLQifjBlMc7Hhpo6q5qh0ZeTqaJgI4TeI5MZ6tCGOsWH055G1pZq_KOBjyIFN5QVKHe3_C55US6z8Zv3zJP1IjnvtBf3F-3GIz0POopBVM39szt8WzDZSkDhKJ-nikxj7p9Moa254OLv6EByfIhWz9Df64Iqq4uPWGkU-WlkXbF8ZbcDFBPe_C_7PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی در هتل فردوسی مشهد
🔹
عصر یکشنبه، یک اتاق در طبقه ششم هتل فردوسی واقع در بلوار شهید مدرس مشهد دچار آتش‌سوزی شد.
🔹
بنا بر اعلام سخنگوی آتش‌نشانی، این حادثه هیچ مصدوم یا فوتی نداشته است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661931" target="_blank">📅 21:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی کند، به مذاکرات باز نمی‌گردد
🔹
ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661930" target="_blank">📅 21:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در انتظار مصوبه کارگروه
احمد فاطمی، عضو کمیسیون تلفیق بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به کاهش ارزش واقعی کالابرگ در اثر تورم، افزایش مبلغ آن مورد موافقت قرار گرفته است.
🔹
به دلیل محدودیت منابع مالی دولت، احتمال افزایش ۳۵ تا ۵۰ درصدی مبلغ یک میلیون تومانی کالابرگ مطرح شده، هرچند برخی معتقدند برای جبران کامل کاهش ارزش، باید ۱۰۰ درصد افزایش یابد.
🔹
زمان اجرای این افزایش هنوز مشخص نیست و اعلام نهایی آن به تأمین منابع مالی و تصویب کارگروه مربوطه بستگی دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661929" target="_blank">📅 21:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c6a83a78.mp4?token=VavZrAoXKTKCML9XIudLkgJ_akm7MetEczdxelxx0USAqvz-Gi18TpoRFM8ab5Yk0PTGxsxWfclP7XRdK7E1_ILdok4IgZityxRR6Hs3Bpfa36_Ov8QG3qgKjTQy0JK9VMn1Yd2tpvHtxT8Ma0UW8_MI7hAJBvh0PR5GdVyd77O2XStlqFuRAeu3Y2HemvyK8FidheEhriG5neeKF31AFkHs5NpcZUEPPGfMeojza6Q9clAwV_OEf-uzC1tnzP9pgyfgWAmYTdqYEFGFwRpKbSbAuWsbno9hu7RdvogBkakcsUkSNH9ux_xB8GVxFuSwvdTz4-BI1Zd7dZaUIT_cfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c6a83a78.mp4?token=VavZrAoXKTKCML9XIudLkgJ_akm7MetEczdxelxx0USAqvz-Gi18TpoRFM8ab5Yk0PTGxsxWfclP7XRdK7E1_ILdok4IgZityxRR6Hs3Bpfa36_Ov8QG3qgKjTQy0JK9VMn1Yd2tpvHtxT8Ma0UW8_MI7hAJBvh0PR5GdVyd77O2XStlqFuRAeu3Y2HemvyK8FidheEhriG5neeKF31AFkHs5NpcZUEPPGfMeojza6Q9clAwV_OEf-uzC1tnzP9pgyfgWAmYTdqYEFGFwRpKbSbAuWsbno9hu7RdvogBkakcsUkSNH9ux_xB8GVxFuSwvdTz4-BI1Zd7dZaUIT_cfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ورزشگاه سوفای محل دیدار امشب ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661928" target="_blank">📅 21:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قطر از ادامه مذاکرات ایران و آمریکا استقبال کرد
🔹
محمد بن عبدالرحمن آل ثانی، نخست‌وزیر قطر با استقبال از برگزاری نشست لوسرن و و تداوم مذاکرات میان ایران و آمریکا استقبال کرد.
🔹
او از پاکستان و همه طرف‌هایی که در شکل‌گیری این تفاهم نقش داشتند قدردانی کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661927" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حزب‌الله لبنان: ایجاد منطقه امنیتی توسط رژیم صهیونیستی در جنوب لبنان را قاطعانه رد می‌کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661926" target="_blank">📅 21:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtepqy4dexHVvyuQGcKFpYpg2HK_M34X0C-a1S0srsNGeq8XYztTPn3RVJ212sH24dLdNZTyjxbdpOORWUdaTeLo4eruBOBj3YKdd7VWJOpa4L3SBk7sHnx-opaSMCI9Aov4k3e1jkNzeFJ2c-O6T64x7Q090AX5HuM3rzNDsK2VANySUUTbTwezxoAfIawHcf5vggD7i_Dd9JZRjoeyYHACmNzGmxy3XXnXNYlFYe8DQ8PdKXQ1PwfCaicOf2qnq2cRjpvsA577nKMLAQWYIGf0JmGQZud4VS0Luc8QlN_CDjpzKOpBhBo1UlL9Zl4sKEnKmEinTvO3-cPsqnWUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🎁
با اولین پیش‌بینی‌ ۵ گیگ اینترنت هدیه بگیر
بعدش با انجام فعالیت‌های مشخص‌شده:
1️⃣
امتیاز جمع کن
2️⃣
توی رتبه‌بندی صعود کن
3️⃣
و شانس برنده شدن جوایز میلیاردی رو به دست بیار
👉
برای کسب امتیاز، راهنمای تصویری رو ببین
👀
هر فعالیت تو رو یه قدم به برد نزدیک‌تر می‌کنه...
📱
ورود به همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661925" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hukHz9ylk1d7i7itHBkiHVjQIEVl9NDN-SV0IklWO17mp_7EnfvYyJfJj_QHgqWHU0_2bsgr2d3pGAqPhFr4D4bXSTe0zjZ7h40G_KxGp9kW0W1RO-9KzrTAe8zI2ikSp8MucbG4BIPLs1M6MRrU-OTYuUfqM7vvd-KXTPptGbXjGjFj2-FsHp-DhV8Qa8NvIFracqz2mIAYn8DdUx9RWtVZnCCHZX7a7ltzU_-WWNHMhkV493HVmw-9qwSmDaQrYcHaikC-Hm5rN0NzBnoD0tnEJsiKFVPoaUZhlP9WtObZFy2sLgIxGFfRAYrh2j5RZo_LtCQ07vtK7aOqGyFYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخته فنی جلسه تیم ملی ساعتی پیش از آغاز دیدار ایران برابر بلژیک
🔹
از توسل به حضرت علی اصغر (ع) تا یاد ایران و شهدای مظلومش در میناب.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661924" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaqTmDmdfTQ6J1cDWmCR3kVjYm_k6D_to6kyP5qwNsfo0pca1ys5fhVIOQrZhSGnTLvU0VRCqc8dSZkwyzyOOZzGhEpNCn5qazrpgSncMxcXinygIc3SR6-2k10iJe3d0ywizioE4YcBTDgzw3Svz_j4ozEGdvAU3TKmC0-LNoq4ZAnrYSm0vXbEeChNA9QVpXfBW-lZmBltihno1wfFKpaDCMiCRE0gHMBWWyMK_vQeSmg7BK-sr3IiMfYn7YP4YV6eYyZ5pRz4a0Sa8cps1b2b2MH0rr2TWwJH7j0FJFfKReMRgfK_QOWa9bi4T46xAI9ZmxiWw7oLtPuppWRxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با بلژیک
🔹
این بازی امشب ساعت ۲۲:۳۰ در استادیوم سوفای، لس‌آنجلس آمریکا برگزار می‌شود. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661923" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وقوع انفجار در حلب سوریه
🔹
علت انفجار هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661922" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661921" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شبکه ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی برای کاهش تنش تنظیم کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661920" target="_blank">📅 21:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
کانال ۱۲: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود./انتخاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661917" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
منابع العربیه: هیئت ایرانی به محل اقامت خود بازگشته است، اما مذاکرات برای بازگرداندن آن از طریق کانال‌های واسطه ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661916" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=GvR-GNR9KJ8m8fPER9_l9SB7fczCi8xeYesP72TvNZiuk1Kb2UfNb7GIV1kYoDnQsPvWJx3pECSR_tChJ0bPZPqxsud7JEIR_zP2_ZIWB818tgyi9DiiHv5dyARRzJHYvaYZSB_oz3ptnkgSB6hPjjGtxcVzg4T1YrcAYOSGifGBgWjNc1ytTKmnVNSBLzp8EMi94GHn5IaVq5t8vj4VHt-cb9f1lj8rza2u6NJ25KZAoM4oIdNV3n91Mx38qpBz09WCPqHnUuY6esM1aTXadBByeidpltrVaUW_grqrYkyT7sfz4JjsqQiKD8bDEqcbQ7lvmjWpoOSfqxO8noIflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=GvR-GNR9KJ8m8fPER9_l9SB7fczCi8xeYesP72TvNZiuk1Kb2UfNb7GIV1kYoDnQsPvWJx3pECSR_tChJ0bPZPqxsud7JEIR_zP2_ZIWB818tgyi9DiiHv5dyARRzJHYvaYZSB_oz3ptnkgSB6hPjjGtxcVzg4T1YrcAYOSGifGBgWjNc1ytTKmnVNSBLzp8EMi94GHn5IaVq5t8vj4VHt-cb9f1lj8rza2u6NJ25KZAoM4oIdNV3n91Mx38qpBz09WCPqHnUuY6esM1aTXadBByeidpltrVaUW_grqrYkyT7sfz4JjsqQiKD8bDEqcbQ7lvmjWpoOSfqxO8noIflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین دیدار تیم ملی فوتبال ایران در جام‌جهانی، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی ایران و بلژیک را با ما به اشتراک گذاشتند.
🔸
شما هم پیش‌بینی خود را ارسال کنید و در حمایت از ملی‌پوشان کشورمان همراه شوید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661915" target="_blank">📅 20:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8TdUjpM7eunD8aOotZ8MikD6vYbfEuuDfQsO2XPziZpPfTbGft24WJV1n_2x2uzPgzv5MMsy3m7oShhXmuC-5QQM0N2QJpp0UhqdGBEwqXUAg7k4VZ5OjLyfuPL16lLMnjbqcDo_OXSynOs_Fe5Vq-UM5awi6C62jGdVYtKmFgaA2OldV81JbNM7Pq-SLZEHHX9mKrvFz6ojUme56V-NlNs-Me_ZSrAERo0XXrQqPmN_zHwl__feDGNEAP0mwmAZ8yGPbE5zQdoqV6vYCXquEcTWAf4kxdSe2rEIJBqF0Om4T2iCzQfQZVXv_3A5_w4RIUXn7zbIrUy9mDYtHK_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب تیم ملی فوتبال ایران برای دیدار با بلژیک
🔹
این بازی امشب ساعت ۲۲:۳۰ در استادیوم سوفای، لس‌آنجلس آمریکا برگزار می‌شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661914" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3LgykSF1h6p5Cm5oo03oLY618bWkSBMFLpd5-xSaKRxDOaErvDtDeqy7Y2OX-F02rP_IZLGhhm5q8LrGHaqfqU9k5hWvQYE5QA4-_g5v7CfzOrSQ_HWwzIfi2QHsQGnU_NeO8AL1jPzxl8bod9Us7lOTAaZpW-BmYAA1DCk85JJv7BA9-acqWkLwrIazwzuJawPS7QoV8BD9y2TKqIZ7CrViHYyphWrZI1zWnTn9QlXLKZshgjmbDq4_wBUwHWr34oFKlP-FvZB4CMZ_GFz66b6x4GnYrnSgcbbM0-1jJPsWvnnhgA6U25I-9ajOYGrMH_RDHUbllIUlnMFt4Tz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاف عجیب رونالدو در اینستاگرام
🔹
رونالدو در اتفاقی خبرساز، با اکانت اصلی خود زیر پستش نوشت: «تو بهترین بازیکن جام جهانی هستی، حتی اگر تیمت به تو کمکی نمی‌کند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661913" target="_blank">📅 20:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012eab6938.mp4?token=X7Y6xk2eSey2hi-fSIT32ze3iO0g8ft2X6BsYKqfpGV0sl6rOgPIaKC_ZaNkyEKsjnvxwfD4uLmrAsCZB-UOjaMvPF6tEjIdbKLb40K9h13N8vP48z9APxmzkF5ApriJr9UixUZNGQONNpD78TF9Bbt8YJffBWX4NUHDRqkYO64e-GhRtd66RomVW40jVHSXhIDbwZCGRnMfpkFiz-IgJneIpc0WGsXCmpJbRrZ6XcDMVAT1OU1pdMWIcnuM5vsa8sliWJjfnoaV9F4C-ZkxqW4XYp5B1LMDGWzFAE2AqIdNRFoLW_2qyQ5r4N5ZHkVvBD5T7G7TV93sv-1RrG8lxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012eab6938.mp4?token=X7Y6xk2eSey2hi-fSIT32ze3iO0g8ft2X6BsYKqfpGV0sl6rOgPIaKC_ZaNkyEKsjnvxwfD4uLmrAsCZB-UOjaMvPF6tEjIdbKLb40K9h13N8vP48z9APxmzkF5ApriJr9UixUZNGQONNpD78TF9Bbt8YJffBWX4NUHDRqkYO64e-GhRtd66RomVW40jVHSXhIDbwZCGRnMfpkFiz-IgJneIpc0WGsXCmpJbRrZ6XcDMVAT1OU1pdMWIcnuM5vsa8sliWJjfnoaV9F4C-ZkxqW4XYp5B1LMDGWzFAE2AqIdNRFoLW_2qyQ5r4N5ZHkVvBD5T7G7TV93sv-1RrG8lxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخالفت هیات ایرانی با عکس مشترک در ژنو  یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
هیات ایرانی با برگزاری مراسم دست دادن و عکس مشترک با هیات آمریکایی در آغاز مذاکرات ژنو مخالفت کرد.
🔹
در پی این تصمیم، پخش مستقیم و مراسم عکس لغو شد و نشست بدون حضور هیات ایرانی در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661912" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e38b668a.mp4?token=kUdgEu0T48sV4YypnS1plQ3vgaK663B8UU0qF2dQUSkugW4ioh8IfY4nCfoMWHj8PMEKq0PpEyE3IVv0wq6XZ52lrS3J_uk52TXWPAv94LLIfv0XlwsurwjLiJzG46Xrqj0EYJEhkwgI9dBOvS-M6ZezVKwM57sprf6uoQ-otCS9muwhqNZp6kYzs2t9ct5PZbCfIM-uPYWrVPjeUpMAJpgZD1FJzAy2I7T1nYJ26eYjG5etJ2oP73sF8rXiuMmmupE9dyxIUhChaBu5jODs44VOfD8YD-EqhxFB7mJ9uRaoaxicNo5MfbqXU_y1mil1C3B_BlBwJAYtuTtw-ByspZL7nua6BvElccVJreb7vttVvRsfH7_QEjidxRzrSThOrz7GOsaBYbDyj5QCdUJ8WBvxsDkjRY8tzEC_Z7NRy0bCLDaFrV-HxJMuluYc9OXXbTB93yUSOIs10Ac2w5F_qIO79kqhujKDhglASa6NwXf4IqVTglpzF-3ic1evPH8EJwnmN0ByGVZm0V54JB80749iZlo2kQ6DFixmvMR99QpnOKn2r4uQ0UeIZxjQlasW3klsjcShTiv_BIa2I-NZFfuTjkUTkueLs_m3n6jcHt7DRU31cKkKUjkcTwQlaOHDz6FkZMQuVUJ8LN5chOM424OTIbQrwVjYUeafPaN5oc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e38b668a.mp4?token=kUdgEu0T48sV4YypnS1plQ3vgaK663B8UU0qF2dQUSkugW4ioh8IfY4nCfoMWHj8PMEKq0PpEyE3IVv0wq6XZ52lrS3J_uk52TXWPAv94LLIfv0XlwsurwjLiJzG46Xrqj0EYJEhkwgI9dBOvS-M6ZezVKwM57sprf6uoQ-otCS9muwhqNZp6kYzs2t9ct5PZbCfIM-uPYWrVPjeUpMAJpgZD1FJzAy2I7T1nYJ26eYjG5etJ2oP73sF8rXiuMmmupE9dyxIUhChaBu5jODs44VOfD8YD-EqhxFB7mJ9uRaoaxicNo5MfbqXU_y1mil1C3B_BlBwJAYtuTtw-ByspZL7nua6BvElccVJreb7vttVvRsfH7_QEjidxRzrSThOrz7GOsaBYbDyj5QCdUJ8WBvxsDkjRY8tzEC_Z7NRy0bCLDaFrV-HxJMuluYc9OXXbTB93yUSOIs10Ac2w5F_qIO79kqhujKDhglASa6NwXf4IqVTglpzF-3ic1evPH8EJwnmN0ByGVZm0V54JB80749iZlo2kQ6DFixmvMR99QpnOKn2r4uQ0UeIZxjQlasW3klsjcShTiv_BIa2I-NZFfuTjkUTkueLs_m3n6jcHt7DRU31cKkKUjkcTwQlaOHDz6FkZMQuVUJ8LN5chOM424OTIbQrwVjYUeafPaN5oc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب هفتم محرم حضرت علی اصغر (ع)
🥀
عمه بی‌تاب شد از گریه تو گریه نکن
دل سنگ آب شد از گریه تو گریه نکن
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/661906" target="_blank">📅 20:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0731c4b28.mp4?token=a-4cOLXqZiU7AR552QLSVwdWXnSTjaI4iZ16-2RleM1nOm7DRjhPeiKl4WZdfu2H_xlKWoGkT0CvT4PEEsBCuiVq54qENMLcqEVhPtXr1fdS_SzpgWkVHb0oqDB1f_NjxahTMqCtKVK5Z659Wy_g-o1QbV5YZXX4Tk3VCIKLSnRdk-VtMX9zmRypRWK_kU13agL7dsp0f9RxHNfuj47D_vYOaYeUtnYZPMNINjnsuzVVytBQ8ewYSQQxWbIzhjERseiPf3glsS-9q7nmzWOb8eCMhOB5wUfqNwJ1HbVJloWp9Mx5hfysiIhXZBhggoH65O0MRKfYQ2WzA7rhcQz5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0731c4b28.mp4?token=a-4cOLXqZiU7AR552QLSVwdWXnSTjaI4iZ16-2RleM1nOm7DRjhPeiKl4WZdfu2H_xlKWoGkT0CvT4PEEsBCuiVq54qENMLcqEVhPtXr1fdS_SzpgWkVHb0oqDB1f_NjxahTMqCtKVK5Z659Wy_g-o1QbV5YZXX4Tk3VCIKLSnRdk-VtMX9zmRypRWK_kU13agL7dsp0f9RxHNfuj47D_vYOaYeUtnYZPMNINjnsuzVVytBQ8ewYSQQxWbIzhjERseiPf3glsS-9q7nmzWOb8eCMhOB5wUfqNwJ1HbVJloWp9Mx5hfysiIhXZBhggoH65O0MRKfYQ2WzA7rhcQz5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم اسپانیا به عربستان توسط حسن محمد التمبکتی ( گل به خودی ۴۹)
⬛️
🇪🇸
4️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/661905" target="_blank">📅 20:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661904">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005e3db47d.mp4?token=frDAM8lHw_mWeFKvE-8gQHbuKqMg4q3GdNpprzn1y-vLWVL_tvi5fH-J0ffTTS1v_qKtYgNdljgSUIOQhEcoW-ux6eSCL3jfUYyKIoNsxUStQBahsTE32OclbvgyE9xaSAQc1oAXNshPO_OiXs5KuMtG3b24aK1XuwAjojhFA00pABTPo1zN-OiNB2lywefDzuiKd9H_Qr1Zu3gGhURLPd-_Y9UBf0YSwEhInYoKnBcZAYj-7MRvP1gCOnsrDGNFETZSGODsuZuZzun9XIvLiaGNKNHp2mvpNjZfbNBaBIMD2vGCKHoQHOg5qIQce_9Yqf89Vfw4V6d5UtKatwCQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005e3db47d.mp4?token=frDAM8lHw_mWeFKvE-8gQHbuKqMg4q3GdNpprzn1y-vLWVL_tvi5fH-J0ffTTS1v_qKtYgNdljgSUIOQhEcoW-ux6eSCL3jfUYyKIoNsxUStQBahsTE32OclbvgyE9xaSAQc1oAXNshPO_OiXs5KuMtG3b24aK1XuwAjojhFA00pABTPo1zN-OiNB2lywefDzuiKd9H_Qr1Zu3gGhURLPd-_Y9UBf0YSwEhInYoKnBcZAYj-7MRvP1gCOnsrDGNFETZSGODsuZuZzun9XIvLiaGNKNHp2mvpNjZfbNBaBIMD2vGCKHoQHOg5qIQce_9Yqf89Vfw4V6d5UtKatwCQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔥
قهرمان فرالیگ شو
🏆
همزمان با جام جهانی ۲۰۲۶ وقتشه خودت رو به چالش بکشی!
⚽️
در مسابقه «فرالیگ» نئوبانک فرارفاه، نتایج مسابقات جام جهانی را پیش‌بینی کن، امتیاز بگیر و برای کسب جوایز نقدی روزانه و جوایز ویژه پایان دوره رقابت کن.
🎁
جوایز روزانه:
▫️
نفر اول: ۲۰۰ میلیون ریال
▫️
نفر دوم: ۱۵۰ میلیون ریال
▫️
نفر سوم: ۱۰۰ میلیون ریال
▫️
نفرات چهارم تا شصت‌وششم: هر نفر ۱۰ میلیون ریال
🏆
جوایز ویژه پایان دوره:
▫️
نفر اول: ۲ میلیارد ریال
▫️
نفر دوم: ۱ میلیارد ریال
▫️
نفر سوم: ۵۰۰ میلیون ریال
✨
هیجان جام جهانی را این بار در فرارفاه تجربه کن.
📲
همین حالا وارد
نئوبانک فرارفاه
شو و به جمع قهرمانان فرالیگ بپیوند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661904" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAb_DlFMt8Iv9azAGgjkHWRD6hZCj8PsKpxUTXHrYPkJ3juP_LMReYnA1BTJDe6Q0y2f--pMo450LcmeInjvgyPUBxMda3NBlPaSSyuCK6WYBQQujH93ygMeCZTN3lBryfqQIaw2LXM6S7hx1TpjYI8UyA3rIocXmXJlceDVTdJqMqKtyw7a8BBXQVtJM9Bg5uqkAs8_rN9Lt__83QrjuxOPRUxq9WEhcw2PJDkZ_gP6QFkCBqMO-YaQ76Sz2beOEYg0Of7ta75_dgAeaqKdkXPrcWzsn3ngGX7SDYhiVE9RzKCkDvtbZycayMpRkRmhiDKb47Qb2v8IbzWbfQNe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
خبرنگار اکسیوس: یک دیپلمات حاضر در مذاکرات سوئیس ادعا می‌کند که هیئت ایرانی محل مذاکره را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/661903" target="_blank">📅 20:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
بقائی: نشست سوئیس بر اجرای تعهدات طرف مقابل متمرکز است
سخنگوی وزارت امور خارجه:
🔹
نشست امروز در سوئیس برای پیگیری اجرای مفاد یادداشت تفاهم ۲۸ خرداد ۱۴۰۵ برگزار شده است.
🔹
وی تأکید کرد آغاز مذاکرات توافق نهایی منوط به اجرای بندهایی از جمله پایان جنگ در همه جبهه‌ها، صادرات نفت ایران و آزادسازی دارایی‌های مسدودشده است و بدون اجرای این تعهدات، ورود به مرحله مذاکره نهایی ممکن نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661902" target="_blank">📅 20:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
روایت تکان‌دهنده یک تجربه نزدیک به مرگ؛ از بی‌اعتقادی تا بازگشت به زندگی
🔹
00:04:15 شاکی بودن از خداوند در تمام طول زندگی
🔹
00:08:20 عشق ورزیدن به امام حسین(ع) در عین بی‌اعتقادی به خداوند
🔹
00:14:00 سختی بی‌اندازه جان دادن از بین دندان‌ها
🔹
00:29:20 آرزوی خاک بودن تمامی سلول‌های بدنم در حال سوختن
🔹
00:36:50 ناچیز بودن آتش این دنیا در مقابل آتش جهنم
🔹
00:46:10  شفاعت حضرت زهرا(ص) برای اشک‌هایم بر امام حسین(ع)
🔹
00:59:20 توصیه تجربه‌گر به انسان‌ها براساس تجربه نزدیک به مرگش
🔹
قسمت بیست‌ویکم (خاک و خاکستر)، فصل چهارم
🔹
#تجربه‌گر
: باقر حسین‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661901" target="_blank">📅 20:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
یک منبع نزدیک به تیم مذاکره‌کننده: هیئت مذاکره‌کننده ایرانی در اعتراض به تهدیدات ترامپ محل مذاکره را ترک کرد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661900" target="_blank">📅 20:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661899">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تشییع بقایای شهدای مدرسه «شجره طیبه» میناب ۹ تیر برگزار می‌شود
معاون سیاسی استانداری هرمزگان:
🔹
بقایای تفحص‌شده شهدای مدرسه شجره طیبه میناب روز سه شنبه ۹ تیرماه ۱۴۰۵ تشییع می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661899" target="_blank">📅 20:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان: تقویت معیشت مردم اولویت دولت است
رئیس‌جمهور در جلسه هیئت دولت:
🔹
تقویت معیشت مردم و امنیت اقتصادی کشور مهم‌ترین اولویت دولت است و باید توجه ویژه‌ای به وضعیت معیشتی جامعه و افزایش مبلغ کالابرگ شود.
🔹
وی همچنین با اشاره به تلاش دشمنان برای تأثیرگذاری بر روند مذاکرات تأکید کرد وحدت و همدلی در کشور شکل گرفته و با هوشیاری مردم، این توطئه‌ها بی‌اثر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661898" target="_blank">📅 20:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e1e49a53.mp4?token=Qu21mbmrjJ77qyLA8an7ORZAvdw5q4yHMiiyps1K3_HNIljW4Rmg4jNKyo702yAsNZjv6dceCBO1aKUp28DuwuuKYYRyFxabIqe-RXiTaT_xT6m12bjbbwgMKYacWpb49FymfM7Q9HBzvF-etw50gOLRIqnILJnasjST8cHhM29EP596Fu2oFOuVJLeYfs4Wny5rqEkUotVx1j6tO7cy2ftft-RmC1N5kb7vp5STh6q8SCXu6FwbUxW1K8PtKLlRqRWX83bHvdaNWKdYUIKuVOWAxhAhfX6AG3kbTParfcyFlgRSnfWWqeyMnqNOuyizXqBgmv9efUTTUudA9-lIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e1e49a53.mp4?token=Qu21mbmrjJ77qyLA8an7ORZAvdw5q4yHMiiyps1K3_HNIljW4Rmg4jNKyo702yAsNZjv6dceCBO1aKUp28DuwuuKYYRyFxabIqe-RXiTaT_xT6m12bjbbwgMKYacWpb49FymfM7Q9HBzvF-etw50gOLRIqnILJnasjST8cHhM29EP596Fu2oFOuVJLeYfs4Wny5rqEkUotVx1j6tO7cy2ftft-RmC1N5kb7vp5STh6q8SCXu6FwbUxW1K8PtKLlRqRWX83bHvdaNWKdYUIKuVOWAxhAhfX6AG3kbTParfcyFlgRSnfWWqeyMnqNOuyizXqBgmv9efUTTUudA9-lIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قربان‌زاده، از اعضای همراه تیم مذاکره کننده: اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661897" target="_blank">📅 20:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGFeNgx4xGWzwmWYNxe1qnH8h8-YktzxGPHpJmXpUGurmwAArnl4TvOB8-WsbWtVUY0vM-taWsTcED4bRPpn86mUpyczIKSNLmtHuGiAeBlvnvSeyz-B3bjnMt7nTf_-rY9sZTliGYeSsb8TqSQ2k5HvWjM3YJhl_WykxyVjneRIqMhZ-8DK-zVtI1Zo0I9scI8_YBrEL4gZlgGNkkTLi4KBFGvspw8hOny3QHWKi3TpYFpsUpAa04ItmJ3JrL668PEbdTrepkWWH99YlswOj1zWY37BRpc5gvPyodh0EVrr1CqZSIUO8CUFEomzUELgngT4Ugn_NPGZ-7MQ0alLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dovkrVENBIZhaCLl-t1tgylRgzRDrt4yO2LA-r-918w1fXrz__0lt3uGaATakS4jA2V3y0YgIu2GIMpNlDUuK9yrVFYb1zI0P2ZuG606CDLp-me3gxKzPYSN9SdRWZ7v_-pJU8dGp9L-MCPEMSkpDdGLjCSXs0nLHlJ_h2fXBhudaGHJ-wdwOUsukQytjv_Xh_U3lx_7Kdj_WbWuaYfjn-Av8wabE7sRaE-HN9eHEWDTcILgURz14IoFMSO7tsPVN9laFYV9NtQcni6MKSA1dT6eUrh8noOcrQfOYo8SMEG-KEwOo0B-aKA-3lYc54xNMtuiSJTcQfuv2gg78GQHcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر دختر نوجوانتان می‌گوید «هیچ‌کس من را نمی‌فهمد» این کتاب را به او هدیه دهید
🔹
احساسات دخترانه فقط یک کتاب نیست؛ دوست صمیمی برای روزهایی است که نمی‌دانی دقیقا چه احساسی داری.
با تمرین‌ها و پرسش‌های جذاب به دختران کمک می‌کند احساساتشان را بهتر بشناسند، درباره‌شان حرف بزنند و با اعتمادبه‌نفس بیشتری با چالش‌های زندگی روبه‌رو شوند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/661894" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
یک منبع آگاه: تهدید ترامپ مذاکرات سوئیس را متوقف کرد و ادامه آن را در هاله‌ای از ابهام فرو برد/ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661893" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e1d1264f.mp4?token=inovEzCN65UZrkccjZoAAtfibfeqkbpQMggP7Jvoi8rUluBpggnyXyqTM0mf7OF5XE_iLoLSxc2t-MR_5Pd47uLHv7yTENqB30hX-h7CWgOOyOqhOhN3wBbwQe_2jG38YLg916I-301twlwPs5-Zkhm4APbhvHOATp8LNrK3eQSt--IqI3-FcDK6bLXQis-aO_DogsuOi_RJlvuilVqCYz4dmqgDaw74HSyq4bwUfHUmWjIBlm5EqitNkHr8e6bzX7Q8e4E-fQ40ipUVMrKa57bxRFu3NfBlH78o4LnrzBG4cDlEzt8Ff9gfp7ypDwfZ5QyWjB3KpjmEp2TtglJzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e1d1264f.mp4?token=inovEzCN65UZrkccjZoAAtfibfeqkbpQMggP7Jvoi8rUluBpggnyXyqTM0mf7OF5XE_iLoLSxc2t-MR_5Pd47uLHv7yTENqB30hX-h7CWgOOyOqhOhN3wBbwQe_2jG38YLg916I-301twlwPs5-Zkhm4APbhvHOATp8LNrK3eQSt--IqI3-FcDK6bLXQis-aO_DogsuOi_RJlvuilVqCYz4dmqgDaw74HSyq4bwUfHUmWjIBlm5EqitNkHr8e6bzX7Q8e4E-fQ40ipUVMrKa57bxRFu3NfBlH78o4LnrzBG4cDlEzt8Ff9gfp7ypDwfZ5QyWjB3KpjmEp2TtglJzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم اسپانیا به عربستان توسط میکل اویارزابال
⬛️
🇪🇸
3️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661892" target="_blank">📅 19:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b5b33a66.mp4?token=J2-E2tZvnUeXFeWTDszEHQUTzuQ5DU3yw1Sbhx8yX7H2GQYm0QLFlRiDTUiPiROioWB5lvSvDUjhhC4Ug_Ic14b7M0yAXCzJ1KKg-FV11RoRRwbfUySX-rUk9_IS71r6Wes5Ij2JT45SU6byimDw9apG3MysjZSXE0Ip0Rj9hSJKolUYvoxFzlT4UimjVqTLzyGwEQweuwBWrnSbeoLd-kHm-3naoNN5eRAOO_4YQNZugIoXtkSupBwdEOLbGi70O4fBFH-bD-GSdrfe32uzMHknJXW0mu1ATVUv2d9d-9-fdunG24ZGgvXOPSAXSfU5AivFadOY4yddoDSkpAtMhYMzlgDNjSx5hwQHnwn39w-SysPN25BvdkkAO6ONuvWRuX3Hr2D0uETsgUWbfi4Ns0cE0JN5WuIjWi5Xko4RAHU-O1lNDwoQ70bveohEFrYFcwzZxS2KXtmUVIKG3xEu39ZGddVP250ksej4X_OqnQYIK8kolqQhvqMmJrUdnoJHY544Siv_bcL3t0VCl_dRkCLywgkcnUjqizdcjGWT2dROgY3f7-m-30ZW6x6Xbk6aeUrTr3eC_jpfqNZdSsEQsNUlj1Lm7IQ8u4Zn4Z6YDD4XRlyRwFnDCmc69E3kjTtgF0UupH3_I_3FS22Y5Vo8BAKVC4fF9PU_Gh-zWBOG898" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b5b33a66.mp4?token=J2-E2tZvnUeXFeWTDszEHQUTzuQ5DU3yw1Sbhx8yX7H2GQYm0QLFlRiDTUiPiROioWB5lvSvDUjhhC4Ug_Ic14b7M0yAXCzJ1KKg-FV11RoRRwbfUySX-rUk9_IS71r6Wes5Ij2JT45SU6byimDw9apG3MysjZSXE0Ip0Rj9hSJKolUYvoxFzlT4UimjVqTLzyGwEQweuwBWrnSbeoLd-kHm-3naoNN5eRAOO_4YQNZugIoXtkSupBwdEOLbGi70O4fBFH-bD-GSdrfe32uzMHknJXW0mu1ATVUv2d9d-9-fdunG24ZGgvXOPSAXSfU5AivFadOY4yddoDSkpAtMhYMzlgDNjSx5hwQHnwn39w-SysPN25BvdkkAO6ONuvWRuX3Hr2D0uETsgUWbfi4Ns0cE0JN5WuIjWi5Xko4RAHU-O1lNDwoQ70bveohEFrYFcwzZxS2KXtmUVIKG3xEu39ZGddVP250ksej4X_OqnQYIK8kolqQhvqMmJrUdnoJHY544Siv_bcL3t0VCl_dRkCLywgkcnUjqizdcjGWT2dROgY3f7-m-30ZW6x6Xbk6aeUrTr3eC_jpfqNZdSsEQsNUlj1Lm7IQ8u4Zn4Z6YDD4XRlyRwFnDCmc69E3kjTtgF0UupH3_I_3FS22Y5Vo8BAKVC4fF9PU_Gh-zWBOG898" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
پاس گلِ مردم ایران برای تیم ملی
به امید درخشش و پیروزی یوزهای ایرانی در جام جهانی
🐆
💙
#همراهتیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661891" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced4c2682d.mp4?token=SiaGPOYLd3BBmB6aAUDBkUvEjfdh8_WuhQ-yh8qE8NWeJP8bXqzl7aUCowYBMwOK82Dp2Z0dxizhQcIkbLqNwOVdCbVu1aZhQHxkncJn6RIqTDwX_3kBKZm0L2MMTbA556cDL3uW1Pzk1ApdTx26k6K9q86lTpTLfRnBMdR5zz9OZZxu8UeSWeV_LKrJODEaAonLh9dgreMJUtylZPbfIP38nyvFYChtimI8VN0SnRptcvHjo_UHpfr1UuG19XJ_VYHLWIKcIDjqHM6ysnZbsPptJOjkOAGcwNf7QJcxQWjNCzy-TrL9FWyJkg6Z13caeor-KGbcbGLLIRurRp8lyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced4c2682d.mp4?token=SiaGPOYLd3BBmB6aAUDBkUvEjfdh8_WuhQ-yh8qE8NWeJP8bXqzl7aUCowYBMwOK82Dp2Z0dxizhQcIkbLqNwOVdCbVu1aZhQHxkncJn6RIqTDwX_3kBKZm0L2MMTbA556cDL3uW1Pzk1ApdTx26k6K9q86lTpTLfRnBMdR5zz9OZZxu8UeSWeV_LKrJODEaAonLh9dgreMJUtylZPbfIP38nyvFYChtimI8VN0SnRptcvHjo_UHpfr1UuG19XJ_VYHLWIKcIDjqHM6ysnZbsPptJOjkOAGcwNf7QJcxQWjNCzy-TrL9FWyJkg6Z13caeor-KGbcbGLLIRurRp8lyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به عربستان توسط میکل اویارزابال
⬛️
🇪🇸
2️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/661890" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
