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
<img src="https://cdn4.telesco.pe/file/fFAGFRpolZR1WQSVV6IGYMwwxEaRKNgBS_lFnekThVtFj_Gbzrcl1seWFVQ4jvUu9IIyFnfpFmHVCEvUCVaIG7bk1_GpdEDkXhejmfUYGQMAJYbuncPHYDpZDFSok-35VQuDfC5yIqOwiJd82WvllL8w891hOv-n3-IymlAY9C3qDiVzQwQOJGDrsf2RGzjSkom5j6uKMDOcpgfQOQ6GIRPmPdCc99tXbmAOhV4UiUox_E8cJT6XGRdAejG0FU2ECDaI3NwGv1zeRwBcfYfru5JAg2txRzcaprPlMRRRumWOOoqJPQGP36LTvlxqOQ7uBnMdNebh1AS9qb5_9st_Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 01:41:40</div>
<hr>

<div class="tg-post" id="msg-681572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTsi5FXb6kzGDyaLuzEZEVj5SPXSkyNDLwh72Z_pYyeoeNB3rmOX3EbrDZ-1LcBIu7tq8LmRAA6XbkQhfvLvJobVMrX-jnLHgI9t3DWNYVAggpikUPt2ANwdYCh3J0tf27H5bDFp-b2gMjUbQeUGmH97pW5jdA_D0wrWkqwFBE3EzGlPuMsToSeC2AjtV8LpJuY8y4jmJxEXM7ORKxi_bPK89uruM25gUrFKop3gfBla-oYtLTWlyCBmstz_WQuewdCK_nA_ZGXr1D9QfqpjWLtvRW3DXHa9TlZ8nvBPNfwpyXv9dojMZjaoEEGpE4oCw3SQOh9hjlM-cRSGQQT_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/akhbarefori/681572" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSt2o1H-ZtKNxamatR3HZKr3bJgcIiZn-bmAYPHGRrSoZWv-gMq3sLQ9Ax3pQrLWnjoek5Jb4Vquo40LzO-8TbsoUdMIOYDrVJcd8fUc483nsRAkMwTRnng3Mk1zt-xtG_OpImsy3Frqcf4HyQgdV9ou7CFp1qm-FHvxkseAFBhAp_uw2BoPxpWrySsjUxXkJ_KMZ-LNNjOy3lQtLapfwzu3mY3WMHfALCaE2ZejcOK1-7qGJy_d_JSeXm1xChBg919EH68XRzIsMaFG7nl50tmEQxS2lSeaAEH0Fmq8nMKak9rcZ59KkDwbAhNRcAgw7917uNSdsH53YVmSNXgGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ بعد از فرار با کانتینر حمل آشغال مواد غذایی از ترس تهدید ایران همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/akhbarefori/681571" target="_blank">📅 01:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI8p9x_INacqvzcbLTzbGGgww11k7rEdTqfQi7A2qGq4q6-9llXj4huGkqFvzwgkeJDWDkvCE4_46nmfpTD4FeWi3YytqwpZ03NSwEt_Z05ca2ayBD8IEp1nbljz-Z3eRzMetmb8vqb772TobCRohFV4hmrOBPSSVhM30dGw1DxAOt1VgYD_1U-vqMdX8bBFtBksJUOJTsU1Cq_L4cZmudMzPgjjoDsOcXVrEkMSdEmWaflSEdFxSn7VXEsEMXvndokGNN_gF6SQAZGGMZ6uWn-LwucOTfqzTA1aWt25WD4VJKDm6OnARPixHvgBk3Sw1U1O35XLA4p4AQiKCM7caA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم عزیزی: رئیس‌جمهور آمریکا باید نگران امنیت خودش باشد
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس شورای اسلامی:
🔹
رئیس‌جمهور ایالات متحده به‌جای ادامه تهدیدهای بی‌پایان درباره تنگه هرمز، باید نگران امنیت خود باشد.
🔹
ممکن است شرایطی پیش بیاید که خودش مجبور شود برای حفظ امنیت، در یک کامیون حمل مواد غذایی پناه بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/akhbarefori/681570" target="_blank">📅 01:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2a870060.mp4?token=AtsmykZ0ehqvkFBRA88pWAlw5H-HlyBP8-e_dA7jqOdpkTUGsPw3CbxYtJFkSX9lL2ETD5QZIRr_E_2yv28ByFXrTAywxGPt8XvOUmkKt64asE9gWV5M9jjJdFxfWgWQgzc7W3YdBOgB9-Le-mEUmpe8xhgTCepTat_aDdl_3VTHUC3rlv7ZiFEE8Vmhk1ZP_Fj_-WivcsNmpix_9qlXnu54Dd_37wNs4_wkv0TFMdAAqVNuL8EUJMxqakvmNucMMwG_c0XLan02Pmw1ufl_3H2gIq2lzG0XBKzzvWS8_nEeB4AO8r5EVfrpi1cUjs8jdNtxkUuY1Gy9MenBEbyb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فارس: روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/681569" target="_blank">📅 01:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع لبنانی: جنگنده‌های رژيم صهیونیستی در آسمان جنوب لبنان به پرواز درآمده و اقدام به پرتاب بالون‌های حرارتی کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/681568" target="_blank">📅 01:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a538aeadb9.mp4?token=X9T8xy4i8yeyAa-7VmBexS4HPDZv9-3NXgF5sg3Lgdp2TJw4BLyO611eMJgJGwRoqWe0b4PlZL13E7kzjegUYrJDxzRbQY94qktOV9Irk-FLBjmiwyaud4lpN_HHAn1wt5xuoZD0BUNcI_756rbqMPnQQRIanZ4ribp9esJAAPbnVoTReflmPACQ79OEDSmayvj3oBhq_ZRJD072aRWUUgvRnDW1vgoEl-8ssfOKAsxOAcvc_PB52l1-3VHiWxPXWtynVDPAOGtlzFNuDgJYGScmlqNmcWz7Wnq1QhmoZXu9nG20MipG08aDmnGSlDG-i4NyDV0wUrnAIqnXJNZkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سبز شدن چراغ‌های قرمز حرم امام حسین(ع)بعد از دو ماه عزاداری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/681567" target="_blank">📅 01:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-poll">
<h4>📊 کدام طرح بنزینی دولت را بیشتر می‌پسندید؟</h4>
<ul>
<li>✓ طرح اول: قیمت فعلی؛ توزیع بنزین تا سقف ۱۲۱ میلیون لیتر، سپس توقف عرضه</li>
<li>✓ طرح دوم: سهمیه‌بندی بنزین بین خودروها؛ مصرف بیشتر با نرخ آزاد</li>
<li>✓ طرح سوم: سهمیه بنزین برای همه مردم، با امکان انتقال و خریدوفروش</li>
</ul>
</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/681566" target="_blank">📅 01:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سومین طرح پیشنهادی دولت برای بنزین چیست؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
🔹
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
🔹
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/681565" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/681564" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d76db735.mp4?token=h11cBVkYhz2fridAWe8ZGLarGeTV9147KsJlO_bWNlNrzqJMcKn3fQge0k1gbpjjUv7AeoubII6MpvBLhO418Iekhq9Nptq8QiYRXdXK2_ES2duVtLE09VW1-sEOSEHvf34eNVOrEo-vL5FmVWRfl5tzkBG_qpPHBgqkc4bv0mFi0svA2cJs8fj9_swwBTIKjoydrZ4BtPvPCVBNhACCEgLASZGjtkk_s2fB3k_rVAlQuk3L7Ght7X3sJqUtFbCdx8UtT-5PTNsJXiFpA9kw2W3eKctLUYW9A8NZS4roL-5gAQPRYMTaq-ZSfr6Lpvqz3T0fdgx2rFHtSVOusR1yjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/681563" target="_blank">📅 01:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTJZ40_d0pLzdRqcuv4GJ-cRX022sy2s4BoOFkoFLQV_wHIGq63sfd56AIQCW41fji9aL2XqdCZiDPt6mkw7syBFaAUbGiEYINmjVBNFxwcHUP0E8QRhxKvLbRInudyOuSWtUOzCIryxQJ1icR_SfRor3oHXbgDmV88ixO41fw-F3BmdL-ZR8O8EZi8GjOJWG-SStfR1ARPZF40oOkg1NgoJX5HZWMc4tG30Iyqwqxs-6Bg7nkjcMUQjnJy6QlpT3eYi-J0X047KnlGI-othi6CQgv1jqEOtJagaU6-2M98RbC-ct1TM_1tNvXWBVg2TSp9yl6VnvOU3naSexbIvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌بی‌سی: کاهش ذخایر استراتژیک نفت آمریکا به حدی رسیده که نگرانی‌هایی را درباره آسیب‌دیدن مخازن و توان عملیاتی آنها ایجاد کرده است
🔹
ذخایر دارای یک کف در حدود ۱۷۰ میلیون بشکه است که پایین‌تر از آن، «محدودیت‌های سلامت ساختاری حفره‌ها و زیرساخت‌های پمپاژ، مانع از برداشت‌های بیشتر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/681561" target="_blank">📅 00:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پرواز گسترده جنگنده‌های ناشناس در نزدیکی مرز سوریه و اردن
شبکه المیادین:
🔹
دیده‌بان حقوق بشر سوریه اعلام‌کرد جنگنده‌های ناشناس، پروازهای گسترده‌ای را در نزدیکی مناطق مرزی مشترک سوریه و اردن از ساعات پایانی عصر امروز انجام داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/681560" target="_blank">📅 00:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع لبنانی: جنگنده‌های رژيم صهیونیستی در آسمان جنوب لبنان به پرواز درآمده و اقدام به پرتاب بالون‌های حرارتی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681559" target="_blank">📅 00:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUf7SUnzKmx53O0jib3OJdvOL5Dw-lJBeKQAts2cDRE1TQAm3M_gau18wNu8w427rjUY5qet5ZtaZXjRxFJeXTPq_uR2sPNgNLdRhkoe_joCgeE206EvtC29r7MJVWXALgYt1YO0N8Bmo2uoMinrySAsQyYryJoUCSCAnpJSbHH9RniXKgv5C_YnFMuGfWD8kVXHua0VYWkf-D14of051eO8CKaU5Ap9GpkGyNjf6hh40N071Pz4KfjCcPV141Yz7wepc_bS1a4qizgSF3BrG4mIV3CDHluwcnW3u8VhZVEzfZaeILIjcwZDzEwTabe0HIERf2pSY2OQK_RTWx9DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ کلاهی با شعار «ترامپ ۲۰۲۸» بر سر گذاشت و نوشت: پیروز خواهیم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/681558" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe93a20077.mp4?token=jSoaG4WBy_3DjosVzLtvBS-mTeM-oycyZQ1NOVIuPcbPNQoCEehF0ZmbQL_1wB5GpimnKukrDbW0NWLRK05TsRy1ZVOcJJ-rZZg05G5Vt8jilkBbiCc0Uv4q1cFHSWA-CUIuBk-DOGWFnkERGGOjoo3NZErwmI_kkmzJCbkx2TsbQc5LQDQ2hgKIFJbRKTN1Z-WUGMM1by-GHehLF6hX0MeiA9SnnMYsJOoCu8dVey7VXEdNmqWDHYI5FmJCrqkzjAjVENP9gPFpK3Njc0o31sUDtMlAuuRZt4dnSeKhPITletA8GdzFTfU56hidS_Gf8Ro8LIb4WeMjUXw4HSPdtZBzDiCSlEsXPC5VQnIeJt_DggmjgF5zwx6RfTLXSXMOIY2GrY8bnGa9_U75-PYXcRZyi-TqAZ0GRvIrQdNRCXZ_xmf0dVndS9ppKm2W_ujp1x9PMUFnycz9ArfsrPb9bv_D9oIbzhvmgpUxbxU_MTBIawaiQ68GD6toB0NhsUi0pSvqTftoqUcWXBVH9YJ8EU5R6WPSwwTKHIt_EYaxB6jhg4jqfbGndfwxZKSyi7L8KS2AYr_YNcMTI9y_oIf2_Ut0EQgl2Ukm2fBaWsmI6s8A6Q_33GPMW_Y8EIAd0fP8amNrQfDhBKyvxRET3XmNXWClKxkK6AZRXNzR_2f0GSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل و بعد از لوکیشن‌های فیلم Terminator2/ فیلمی که هنوز بعد از ۳۰ سال کم نمیاره
🔹
جان کانر قراره آینده بشر رو نجات بده، اما یک ماشین از آینده برای کشتنش برگشته. خوشبختانه یک ترمیناتور دیگه هم هست که این بار مأموریتش محافظت از جان شده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/681557" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZUMywnymp2Vo6Xis8za8UEHz8sHkIuu3tXJ8nISNQJ6FBUtgonznvauPpbEZohFX51922fxKq3lebdwnu4OtPdsBDyRFc7vP2r0pcA6BcxEiRzGckTfRAjqLul_At6lhvN7xJ5GLcNrgClOrLR8p7hTLuRCRAjr7upobKfnHx05kEvENo8L9YIUt0WwVOvl3Ovb0LyCxu78zmh7KRi4cRlMXfIXccZweF6LIrYOmt164PF7ywdfdl3JsSvhQ3HXHs-d7k-Y6UQDfN5NQ_cdoY2_i01UkkBiUyI42VjDwuU2dFn2A4AnPpjS9ycVo3WkFS4gFFhjWNNVXf_OjRo4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/681556" target="_blank">📅 00:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPv8a1ac_TS2RtZ2zlqmh10PlOaA39yNO_TiN7Z2jm1ZpxiZG-mrkKB6W8_SXwbJLcFXOlV9T6mWtZtM9TZh3XrhI2yrNqf2U55wMgVlPavhUNXAAdhm6myj2ceW1ImRXBsF7CtL8QuQEQOxkfdtZLNsiDfKBaaxSSUSxCBOzO45c90LuflgDJtO78Vr9WO5sHN9duCnPVqP_dysaXtE9E-JXYaOCQz-Gz6__t69lvVvYdbfgp4qjJXQ-remZP9WMJMp-VwQbll9wFPnmQ9psloyDXZQcS6rX9EowJT-lOG8VxY4s-Hn1svMeRrZzMNzXjhvBKyNE_oc0Ebecs5b6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/akhbarefori/681555" target="_blank">📅 00:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
اسارت ۳ خلبان ایرانی پس از سقوط جنگنده‌ها توسط نیروهای قطری
👇
khabarfoori.com/fa/tiny/news-3237866
🔹
سه طرح جدید در پمپ‌بنزین‌ها؛ بهترین روش سهمیه‌بندی بنزین کدام است؟
👇
khabarfoori.com/fa/tiny/news-3237983
🔹
کارمند اخراجیِ اینترنشنال: هدف اسرائیل تجزیه ایران است؛ چه جمهوری اسلامی باشد چه حکومت شاهنشاهی
👇
khabarfoori.com/fa/tiny/news-3237989
🔹
طلاق مخفیانه بازیگر مشهور فاش شد | پایان بی‌سروصدای یک رابطه طولانی
👇
khabarfoori.com/fa/tiny/news-3237659
🔹
شغل این مداح مشهور طرفدارانش را شوکه کرد
👇
khabarfoori.com/fa/tiny/news-3237906
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/681554" target="_blank">📅 23:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9f8143e5.mp4?token=G8HFU-R7vAVSTiLf3FWjz-ASawl_xJGzAJlHJQsMwpKInvX0Fcn3m94RbYUo9AuAL-4qX7lwjU1FvHgJA94GokeS8Yoj9zAbD1CWHAuY0AZka8a3KF5bxLkzNP1EMQTnSJ2ifAQKkbxGRXYmGDkzAwocw2nPtpsbz8zfdjcn66CB3UfT1MnOOJXqwfzReOOcGla1StQJzNJ7wghA3J77B3lIxVnQjd78MPMZq7_1oO4Gpw3HfKWoS9VKwLIbH30x0V5W9yDEptNQaR4qf4xKFe8UxP_fTj5e74y5zeL-gAHDieN1tM2rcUU2llJA-pHsiZzAjnDPwm_9hC2zubf_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت از تولید داخلی مسئولیتِ ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/681553" target="_blank">📅 23:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
طلای جهانی دوباره خیز برداشت
🔹
طلای جهانی پس از یک موج اصلاحی، خط روند نزولی را شکسته و دوباره نشانه‌های قدرت خریداران را به نمایش گذاشته است. این فلز گران‌بها پیش از رسیدن به محدوده ۳۶۰۰ دلار مسیر خود را تغییر داد.
🔹
اکنون ۴۱۴۷ دلار مهم‌ترین حمایت طلاست؛ حفظ این سطح می‌تواند پایان اصلاح و آغاز یک موج صعودی بلندمدت را رقم بزند. امروز طلا در محدوده ۴۳۷۵ دلار بود که ۱.۱۸ درصد نسبت به روز گذشته رشد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681552" target="_blank">📅 23:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681549">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dddeac06e.mp4?token=lshtcS4dS5zCVpgsu1xQRkpgXCOKM_zmzLYyExTl5AH13zj9M1mDzDQ6WhqJR-9qitQHOXJarMuk9nJL7-zNR37XmoI1q1EXn5YHDYuy34iYwhHzuRkPdxzh-NZ3tpyBVpk_ROksDlHpRDn-f5VbKjbhAqNNtGmigfFsKDFOvT16JUbq9WsIKcj1WiWC4jObWX5yh9ERnsWAT_Qv6XCM0fIJY0ZRLhfWsBVcjjZKRYFF4qfJCDikmyH-2HvPJ-I9d5BVS8GXyKIDVXKFm9_Agqt0VwMSOU653JeMSzHo_fAZOPAR0M5l-kfZqlc4MR39HKzHZ6wLC1qViO757z5STA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیوه خاص مدارس ژاپن برای تربیت نسل آینده؛ تربیت کودکانی با مهارت‌های واقعی زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/681549" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx_XLi2tgD1sBRXUvicM738ditdRnv4spvUvqnKh8RK7yYhXAdz0cZSeTfX-7uv9UlVICatSAOeY5pgl3Hg06Ilpddk3wwAi6NspQL-8ho8v8CXMWQ3rTLyNCJniGhOndV6gkg2QBaE9w9ZXmF2QicSNHX8fk3T6dAa-WgFKCoJdt-b8Fb5kEcZe0kTwqfoZotJTCC7DHo5Of5vbwLlthpULfCunTwS7On4nAOZYQK5-nWFopPUk3Vwa8i_36dIDXBXKxvrqa-7iC7Inu9e3oOmaeneGCF6o3xL54d07W2xMaSoWKAzFxFsGUxg1SLEaiTfF4LxLifQ4L2QWcgQhLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین پالسی: بله، جنگ ایران واقعا شبیه ویتنام است
فارین پالیسی:
🔹
ترامپ، دوست دارد اشاره کند که جنگ کنونی و درگیری ویتنام شباهت کمی دارند زیرا با وجود لاف اولیه‌اش مبنی بر اینکه کارزار ایران در عرض چند هفته به پایان می‌رسد، به طور غیرقابل مقایسه‌ای کوتاه‌تر از جنگ دوم است.
🔹
با این حال، برای هر کسی که امروز آن را مرور می‌کند، سخت است که تحت تأثیر این نکته قرار نگیرد که این دو جنگ چقدر با یکدیگر اشتراک دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681548" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1b618029.mp4?token=HvCRN7-zeKRHR9R01wnyZBvMX9peuzpgDx-VM3RxZrYfblWubErRqWfQNkpR3JYVtrqGWh4aJk3UXixny5z_dLJVRdGEw6bCetHhIE4ZZGpKJEm6Q2t-72PFsCYYyRyfpX07gvIBoD7jUrkjZ-PCQe8B3cvLbaNy8bGVfIyHV3IjTOcqIoef9rOVpH2KBoh9uvkM6GWlYA6aYaYyLCNWnz706XYEc_iQAylVqhA8vSfPrzh7yDLeAzvpg2IHwiRHXttitsxcLx5s7h9D3Me209wEIqxq5ntOIhZvzPCRytW4fKaWo1PodTpT4FT93ZzWb6AQNwQ_Qp7gRZ1uhhq1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول روس در راند اول علی اکبری را ناک اوت کرد
🔹
در مبارزه اصلی برای کسب کمربند قهرمانی سنگین وزن ACA علیخان واخایف غول ۲ متری روس و شاگرد سابق بوایسار سایتی‌یف در همان راند نخست توانست امیر علی اکبری را ناک اوت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/681546" target="_blank">📅 23:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود هندوانه و خربزه ایران به عراق ممنوع شد
سید رضا نورانی، رئیس اتحادیه ملی محصولات کشاورزی ایران در
#گفتگو
با خبرفوری:
🔹
عراق هر ساله به بهانه افزایش تولید داخلی برای ۲ تا ۳ ماه واردات محصولات جالیزی ایران را ممنوع می‌کند.
🔹
امسال نیز از ۲۰ مرداد ورود هندوانه، خربزه، خیار، گوجه‌فرنگی و بادمجان ایرانی به عراق ممنوع شده است.
🔹
باتوجه به مخاطرات جنگی در حوزه خلیج فارس، کشورهای کویت، بحرین و عربستان واردات میوه و تره‌بار ایران را ممنوع کردند که این امر منجر به خسارت به صادرات ما گردیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681545" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور: گفته می‌شود صنعت خودروی ما نوزاد است اما این نوزاد ۶۰ سال از عمرش گذشته است به نظر نمی‌رسد مشکل از شیر باشد و این داستان باید تمام شود ‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/681544" target="_blank">📅 23:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای جروزالم‌پست: آمریکا دارایی‌های مسدود شده ایران را در ازای عبور آزاد از هرمز، آزاد می‌کند
ادعای جروزالم‌پست:
🔹
واشنگتن در نظر دارد به‌تدریج دارایی‌های مسدود شده ایران را آزاد کرده و تخفیف‌هایی جزئی در تحریم‌ها را در ازای اجازه ایران برای عبور تجاری بدون مانع و بدون عوارض از هرمز، اعمال کند. ترامپ می‌خواست ایران را فلج کند اما حالا به تهران یک پیروزی تقدیم می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/681543" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okZGllZa_zTubz5n84dbt6St-wCmRZd2qzf8dCU8fzxajdeeUU1Hz8j7XaHON8mN6xMJ-5g4n7ZjYl2ZSM-Xch2EhRHkIG5mv3vM2eCNSL22k1ZownJbJCT3N-eCDQV-N0VexbFzv8vck4oTcqCn2sWM4qKLGb06vSrRRpC18NHDBgCwPfEafrmkxkvXLpK6-n8XUdFPInCekwMngGckSExW9fM2-A-H9gtG6mX0kR8U1X7uTJa2b_5IbUoXp-UkFs6baShMQ1K_XHUDMmmWXj537we4anqBbnv5-mhsjggeY51zvDlSNn3XLHicJ5RfcOerugGtJWFhu-qEP1mpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب شده بودند.
🔹
این ملوان گفت که به خدمه اطلاع داده شده بود که غذاها با هم مخلوط شده‌اند و افزود که لوبیاها از جمله بدترین غذاهایی بودند که تا به حال چشیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681542" target="_blank">📅 23:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: حدودا به هر عضو خانوار ماهی ۳۰ لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد
🔹
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می‌سپارد.
🔹
قیمت دوم و سوم در این طرح وجود ندارد و سهمیه در کارت بانکی افراد شارژ می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/681541" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: وزارت اقتصاد صرفاً مسئول انتقال سهمیه سوخت به کارت بانکی است
مرتضی زمانیان، معاون‌ وزیر اقتصاد:
🔹
تصمیمات مربوط به سهمیه و نرخ در مورد بنزین در کارگروهی اتخاذ شده و هیچ دستگاهی به تنهایی رکن تصمیم‌گیر نیست. در این کارگروه دستگاه‌های مختلف سیاستگذار، اجرایی، امنیتی و رسانه‌ای حضور دارند/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681538" target="_blank">📅 23:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b849fac5b.mp4?token=fvDpqauzVmw3iVy2ygdIESnGyNlA2ntnn5uACXkRZDu8crTKoGNVHJL8QIrLjPV0H10emkW_QRPMCkiKTb88iqyAFJNX9jjhtSMiO_vib5Nm9U6ZaLiRYogDBS08yHztWgrKyGU5iHcjxXes54v4JIdc7gffC8ZbZkUUxsJ_tD8KfKHGeWi0l35uEcxge9IKo6OZAFCxArx8PAxOjrmPGITx0fsnyLeaF-znGibbpICs1yhmjCFO7llRgDBum8_2gahBXsl5dsCG5rCoF0s3HFLGEgPrcgfsrs6OCVslV64RVzLguSi4mMJ4v58Zcjqs2ICA-pS7BteTH03rFcaR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b849fac5b.mp4?token=fvDpqauzVmw3iVy2ygdIESnGyNlA2ntnn5uACXkRZDu8crTKoGNVHJL8QIrLjPV0H10emkW_QRPMCkiKTb88iqyAFJNX9jjhtSMiO_vib5Nm9U6ZaLiRYogDBS08yHztWgrKyGU5iHcjxXes54v4JIdc7gffC8ZbZkUUxsJ_tD8KfKHGeWi0l35uEcxge9IKo6OZAFCxArx8PAxOjrmPGITx0fsnyLeaF-znGibbpICs1yhmjCFO7llRgDBum8_2gahBXsl5dsCG5rCoF0s3HFLGEgPrcgfsrs6OCVslV64RVzLguSi4mMJ4v58Zcjqs2ICA-pS7BteTH03rFcaR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
کارمند اخراجیِ اینترنشنال: هدف اسرائیل تجزیه ایران است؛ چه جمهوری اسلامی باشد چه حکومت شاهنشاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/681537" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqnmtGu5plCf8nk1_fsYthbGIrnsuXj_QdWlRt3wSv6vyp1U5ZfHUFkF7UpcyrkrzKjhhZEJy-VNF4O0CDAxf0VCBQivqc9hc1O2K5mRT-bdRDDFmVaYkAhei8App03QkEZuWSiPAfxYpvF8TdCQskwR3NocFD-0tUINC8jEJI5zywZZp_XJWCv5Aj4M6yc2KZY-iF7wxP0g1NPWu_P32lwQjMPVx1mlwXrM-XZsUFtLFBIvvU-sEzp1AJ2Vl1-KVOVRCKe73RcuD5TuMs2kCK8YK30_CLVjmoPNrWq1iP8Rr819wxqMwjUR0JcmxQLTfdJJtdBAS4JP_XJVHs6dbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهیه و بازسازی ۲۰ خانه زنان سرپرست خانوار آسیب‌دیده از جنگ با حمایت اسنپ
🔹
اسنپ از آغاز طرح «این راه به خونه می‌رسه» برای تهیه یا بازسازی ۲۰ واحد مسکونی آسیب‌دیده در جنگ ۳۹ روزه در استان هرمزگان خبر داد.
🔹
این طرح با همکاری مؤسسه خیریه «نفس آفتاب» اجرا می‌شود و برای آن ۳ میلیارد تومان بودجه اختصاص یافته است.
🔹
بر اساس اعلام این مجموعه، خانه‌های هدف در شهرهای بندرعباس، خمیر، میناب، سیریک، جاسک، بندرلنگه و رودان قرار دارند.
🔹
در این طرح بیش از ۱۰۰ خانوار آسیب‌دیده شناسایی شده‌اند که ۲۰ خانوار از آن‌ها زنان سرپرست خانوار هستند و بازسازی خانه، مقدمه بازگشت پایدار خانواده‌هاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681536" target="_blank">📅 23:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh32AvUSTNk9jFfdM3LKkvQfmVRrJeFqxqAtPcAMFvp_pYaqI0Z6yvgjpHXa7l9TzekFh_nIGR0pwaFaDQ75cmTz9KCqknHDtA7war-ysuloU3tLTEumc90DHJn5ogg0xfHQH8lJcMpBxjNZOjFOLBuf0HS9T70U_aI56k5meCVek3N3kGIiN_Gv6I-wxXNxMZnTv3SKMHhmFcCHKtDdGdmQErvPT73TEbk15BzeaxkhZ2ys8PHCiDZD_cjFf2-Da30tx7jaQoP2CUgDGPmYeC37I4pSeMvKNN9_CQIsfnG4N3mSIwKz3XH_rUlaM5ocR_vmnRd3nhrctzq5t9p04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ما نماینده کل جهان هستیم، هیچ چیز مثل ایالات متحده نیست
🔹
واقعیت جالب: وقتی دونالد ترامپ از جهان خواست تا به یک ائتلاف دریایی چندملیتی برای باز نگه داشتن تنگه هرمز بپیوندند.
🇬🇧
بریتانیا: رد شد
🇮🇹
ایتالیا: رد شد
🇪🇸
اسپانیا: رد شد
🇯🇵
ژاپن: رد شد
🇫🇷
فرانسه: مردد
🇳🇴
نروژ: رد شد
🇨🇦
کانادا: رد شد
🇦🇺
استرالیا: رد شد
🇩🇪
آلمان: رد شد
🇨🇳
چین: بدون پاسخ
🇳🇱
هلند: بدون پاسخ
🇰🇷
کره جنوبی: بدون تایید
🔹
واقعیت این است که آمریکا در دوران ترامپ به طور فزاینده‌ای منزوی به نظر می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/681535" target="_blank">📅 23:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اعتراض عباس خورشیدوند به خبر بازداشتش
🔹
خورشیدوند با انتشار پستی توسط پسرش به انتشار خبر دروغین بازداشت وی توسط اینترنشنال اعتراض کرد
🔹
روزانه به تعداد افرادی که به انتشار خبر دروغ اینترنشنال اعتراض می‌کنند افزوده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/681534" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM3dfAoP8rOFr7JFGiclRvL7NYhLVtOa6BeVCeyUjfszGontXXm804VuP1gvf21Ed7heOMjeMGmoW_gBrxSZ-9Y6I7vOYPLVxNgua9bwTFvH4Vcph6t6LV-uENv_Efm8yVEZmkffHbTKrnWrWhbb6sy_vil2kEAjknbWNTfEF0gVXVuEWLvYqNYOG8kI4o8uRB_-OkPjr5Uu4xTZd59qJJP5gSoY8KhPOzDlnnlEVwHuSPVKemDlKTBJjMIJcPOJt_y9v4zMjnmcR6ZG_W-ubRtUHK76O7LhnQ15f53b_c7RunLUNsQcQU-IW5q1d4rhPk7WheIVmtypHCAr8O6W6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ردیابی دو لکه نفتی بزرگ در آب‌های ایران و عمان با ماهواره
🔹
محققان موسسه آب، محیط زیست و سلامت دانشگاه سازمان ملل متحد تصاویر ماهواره‌ای گرفته شده را تجزیه و تحلیل کردند.
🔹
تصاویر ماهواره‌ای نشان می‌دهد که در آب‌های نزدیک جزایر حلانیات عمان، لکه‌ای نفتی با وسعت حدود ۳۰۰ کیلومتر مربع شناسایی شده است.
🔹
همزمان در نزدیکی قشم و هنگام نیز آلودگی نفتی در حدود ۱۰۰ کیلومتر مربع از آب‌های جنوب ایران را نشان می‌دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681533" target="_blank">📅 23:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اردوغان: ترکیه تمایلی به عضویت در اتحادیه اروپا ندارد
🔹
گرما ادارات خوزستان را دورکار کرد
🔹
واشنگتن پست: کشورهای عربی به طور فزاینده‌ای از نحوه برخورد دونالد ترامپ با وضعیت ایران ناامید شده‌اند
🔹
سازمان بهینه‌سازی: دولت طی ۱۰ تا ۱۵ روز آینده درباره اجرای یکی از ۳ طرح بنزینی تصمیم‌گیری می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681532" target="_blank">📅 22:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681528">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyzGLR1mOl4tkCxTT_FFxtvPwhlfS7r1KHFsXwAVzvLoc42k3qik8oSSHb297mHQCzq2XV5X7eo1A-IDTktIRRBuAHKfc9UMHlHn9W0McQB-_a-BotjQOJh8TfJlDjDQpm1avcLaf8YX37w4y36ZTXNcJx0cpXlquRdeAfhOhOM8lGrMpfsQHhInAfabpxJnX16JuoX0cEXmtOww4v8kJushxo9H2AJFl7om_eRYRCXLDcJDXfnKelD8sbEeL10KL39ezDACklCN-nwUFdfPsmLePcjwDVVa9Bjs2hSENd4rgiI9SlNNICf9-ICOM5Jr9MoHf0tDDBej727PqeZLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZO74JXJNSdlZfhctcmDFCwFagZ-qZgk4qDxgOh-_52UcllW-w9upvRXop7S0B493CkxDghpAy5OrSZKEwW0c62cMkYrvR6ktU3Om0Jpyl7uOC6nnGZ6FaWsYVq8yom5heq3bMPnlz5voILUs_QGbvcOF87y0SZmXElswGdAFB0KkbFyZTlthbOtRvFckMEo4bVAmKY_QSY3vM6zxo0aA86SEoOvnU6MxH3c1ultrnqeF4a9N9Oa19memi0kASiNgiSJsCZvGKPVXTksS3JJsz0WBdRwmjitR0mn1fwFmmtiqvrM2IKQuyKPJJUMlZ5Le23PMJJLslSHz5jh0oxENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHIfxbtA0gnLQLsXOZw5CUA0FBYKyxTNpJ0UWH5y93v29Bnkkzj2LLvmZFZ_yrbQkSM_tNKO6H_dKTO0byqQfoLvuCXPBNwj6a7i2ly1V7JL1Ab-46C8UoEgDijyIzi8wXVMP14tIdumQgLk9_4k7vdNutfvvfDQCGpS36ud9mwJlfRQIiUsJNidArRk5-i8RXnwM54vL8Qg-60jcibB6DfLPlW5-CvSNzGwR6sMe6Clga51gLod-jGwZ0Ya1ji27Uza6yRKjVA1B0l55WNQKmK42bsO4n73z0bLAnTG_AqNKKvoL1FHuOkDKgOiIbn0CSMFb4Fd3zZgbg65AKAAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzDTvWmvs6XZw2YjTa8t1vCzzTreFzJt0n0U-kExA-x2p9Q2r4W7jggFDO6GOj6kP-buaeVJ8OyTv7Uqq9XNklpeaTb0Z9Rx4KrmRIVszSlzidCmDE_RwR0CXILe429daZ_Z62OUeOp1U8wOFnZSjTH8dbVtBm7W-Lmi03QiNBiJgd4L2K2j3XqyoHHIqXRBQaTKBnFpuRq0uOEo3ylyZBT4lWY8z9URgdCepmZJxUqRvQ9CwbMRAy2-xaYhPyRFsRHOsa1Qo-1EX8UPSgaqs1z5INq3M4X9xQb3Qbk_X1Ae3knbHJJ2NM3nt8KRhHOR_rpC4BDQpmPyVupWbA0rBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ ماده غذایی که با فریز کردن، عمر دوباره می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681528" target="_blank">📅 22:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=WgcehSSo76coRMKbUvY7vwYfzNaE4QoWTOXBYuv4Ebv7a4Z9aRpI7GOXmAh5Af5dd3R_Z-7tVPGhLTY6Vxex3aGgn1CbMPyvaJch8InDEeEPCQPKpQkX3YqzrSRtzTAyGWEzN8vgitwZQkMgQZNd_88mG7TXbO2DY7WdTS3BXayjT4QaUswCMb3YXfBF6QA-hJ4rBQrDz92DJLJcK4WVCkApPCu6tLBEAICla9oYMYU2zxIgm5UrnBbEvmHvOhS_OXquw_SvZHtut3eynsMClbqUpTEbkQKQg0VTlHlCctsFg65DfcJiVONtxlyIzRF24JGKGgwIEMnOP1brHGlVIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9baec4ba.mp4?token=WgcehSSo76coRMKbUvY7vwYfzNaE4QoWTOXBYuv4Ebv7a4Z9aRpI7GOXmAh5Af5dd3R_Z-7tVPGhLTY6Vxex3aGgn1CbMPyvaJch8InDEeEPCQPKpQkX3YqzrSRtzTAyGWEzN8vgitwZQkMgQZNd_88mG7TXbO2DY7WdTS3BXayjT4QaUswCMb3YXfBF6QA-hJ4rBQrDz92DJLJcK4WVCkApPCu6tLBEAICla9oYMYU2zxIgm5UrnBbEvmHvOhS_OXquw_SvZHtut3eynsMClbqUpTEbkQKQg0VTlHlCctsFg65DfcJiVONtxlyIzRF24JGKGgwIEMnOP1brHGlVIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/681527" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
جنگ ایران برای این غول‌ها پول‌ساز شد
🔹
برخی بازیگران اقتصادی از جنگ ایران سودهای چشمگیری به جیب زدند. فاصله قیمت بنزین و گازوئیل با نفت خام، باعث شد بسیاری از پالایشگاه‌های آمریکا در فصل دوم ۲۰۲۶ یکی از سودآورترین دوره‌های تاریخ خود را تجربه کنند.
🔹
همچنین درآمد تریدینگ بانک‌هایی مانند جی‌پی‌مورگان، مورگان استنلی، گلدمن ساکس، سیتی‌گروپ و بانک آمریکا را در سه‌ ماهه دوم ۲۰۲۶ نسبت به سال قبل ۷۱ درصد افزایش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/681526" target="_blank">📅 22:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نیروی دریایی آمریکا: ناو هواپیمابر لینکلن ماموریت خود را به پایان رساند
🔹
پس از ماه‌ها بحران در ناو هواپیمابر آبراهام لینلکن، وزارت نیروی دریایی آمریکا اعلام کرد این ناو ماموریتش به اتمام رسیده و به‌زودی به خانه بازمی‌گردد.
🔹
اعلام پایان ماموریت آبراهام لینکلن…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/681525" target="_blank">📅 22:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b9fc2e1d62.mp4?token=k-7a5_UPreR_-ORzV-bGaLEDpC7hj7ZfYz5ozV4-2rVMB8BtEiiZURTDwwPDVDQpnmVX_SNf7wGhnuuGWr1TGAYy7NgqeFowMgxQ602eUOgMUj33oYFtpWxlBkOiU5c_DVVg_cpdOEevZNm_Lt6XA_EkHw2Mg0FgeTKVABC2al0Ht5PHi1LrJxSWo_d6LpuXUyZgXWMx-73iSsStDLvzLkCoxxetMLfpcq7daGHV4xa3QcUfa651Tmbdkicx0n0cma9WzBddCqG4sx2xGMZhmjXSpfn4D_lIwuUTxrkUOv7De3ePmRKjygoEfynTFgKw-ztqwLcgXG-sdoq50a7Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b9fc2e1d62.mp4?token=k-7a5_UPreR_-ORzV-bGaLEDpC7hj7ZfYz5ozV4-2rVMB8BtEiiZURTDwwPDVDQpnmVX_SNf7wGhnuuGWr1TGAYy7NgqeFowMgxQ602eUOgMUj33oYFtpWxlBkOiU5c_DVVg_cpdOEevZNm_Lt6XA_EkHw2Mg0FgeTKVABC2al0Ht5PHi1LrJxSWo_d6LpuXUyZgXWMx-73iSsStDLvzLkCoxxetMLfpcq7daGHV4xa3QcUfa651Tmbdkicx0n0cma9WzBddCqG4sx2xGMZhmjXSpfn4D_lIwuUTxrkUOv7De3ePmRKjygoEfynTFgKw-ztqwLcgXG-sdoq50a7Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل‌پیش‌بینی‌ترین شیء در علم فیزیک، درست از همان لحظه‌ای که یک مفصل دوم به آن اضافه می‌کنید، به‌طور کامل غیرقابل‌پیش‌بینی می‌شود.
به آن «آونگ دوگانه» (یا پاندول دوگانه) می‌گویند.
به همین دلیل است که دانشمندان هنوز نمی‌توانند رفتار آونگ دوگانه را دقیقاً پیش‌بینی کنند.
آونگ دوگانه‌ای که شرایط اولیه آن حتی تا یک‌تریلیونُمِ درجه اندازه‌گیری شده باشد، باز هم ظرف مدت ده ثانیه کاملاً غیرقابل‌پیش‌بینی خواهد شد.
کمی درباره معنای واقعی این جمله فکر کنید.
ما معادلات کامل آن را در اختیار داریم.
نیوتون آن‌ها را نوشت.
لاگرانژ آن‌ها را به‌روز و دقیق‌تر کرد.
هر دانشجوی کارشناسی فیزیک می‌تواند آن‌ها را روی یک دستمال‌سفره اثبات و استخراج کند.
هیچ بخش ناگفته یا گمشده‌ای در فیزیکِ آن وجود ندارد، هیچ متغیر پنهانی در کار نیست، و هیچ عجیب‌وغریبیِ کوانتومی هم مطرح نیست.
فقط دو میله، دو مفصل، و گرانش. همین و بس.
و با این حال، این سیستم پیش‌بینی را به تمسخر می‌گیرد.
دلیل این اتفاق در چیزی به نام «نمای لیاپونوف» نهفته است؛ عددی که سرعت واگرایی و فاصله گرفتنِ دو موقعیت شروعِ تقریباً یکسان را در طول زمان اندازه‌گیری می‌کند.
برای یک آونگ دوگانه، این نما در حدود ۳ تا ۵ در ثانیه است و در برخی آزمایش‌ها حتی به ۷٫۹ هم می‌رسد.
به زبان ساده: «هرگونه عدم‌قطعیت ناچیز در زاویه اولیه شما، تقریباً هر یک‌پنجمِ ثانیه دو برابر می‌شود.
پس از یک ثانیه، خطای شما هزاران برابر شده است. پس از پنج ثانیه، میلیاردها برابر؛ و پس از ده ثانیه، دو آونگ هیچ وجه مشترکی جز قوانینی که از آن پیروی می‌کنند، نخواهند داشت.»
دامِ عمیق‌تر، ماهیتی فلسفی دارد.
مکانیک کلاسیک قرار بود معبد «جبرگرایی» (Determinism) باشد.
لاپلاس به زیبایی مدعی شده بود که یک هوش به اندازه کافی قدرتمند که موقعیت و سرعت تمام ذرات را بداند، می‌تواند کل آینده جهان را پیش‌بینی کند.
آونگ دوگانه تنها با استفاده از دو چوب و یک لولا، این رؤیا را بی‌صدا نابود می‌کند.
جبرگرایی در تئوری برقرار است، اما پیش‌بینی‌پذیری شکست می‌خورد، چرا که اندازه‌گیری‌ها هرگز دقیقِ مطلق نیستند.
شما نمی‌توانید یک زاویه را تا بی‌نهایت رقم اعشار بدانید؛ جهان این ارقام را در اختیار شما قرار نمی‌دهد.
بنابراین، حتی در یک سیستم کاملاً جبرگرا، درست از لحظه‌ای که حساسیت به شرایط اولیه از دقتِ اندازه‌گیری شما پیشی می‌گیرد، آینده عملاً غیرقابل‌شناخت می‌شود.
به همین دلیل است که پیش‌بینی‌های هواشناسی برای بیش از دو هفته با شکست مواجه می‌شوند؛ به همین دلیل است که آریتمی‌های قلبی در برابر پیش‌بینی مقاومت می‌کنند؛ و به همین دلیل است که مدل‌های مالیِ بناشده بر منحنی‌های هموار، توسط واقعیت تکه‌تکه می‌شوند.
آونگ دوگانه، چهره صادقانه بیشتر سیستم‌های پیچیده در طبیعت است.
پیش‌بینی‌پذیریِ هموار، یک استثناست.
آشوب (Chaos)، تنظیمات پیش‌فرضِ هر چیزی است که از اجزای غیرخطیِ کوپل‌شده (به‌هم‌پیوسته) تشکیل شده باشد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/681524" target="_blank">📅 22:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS9F5MHXH3C1LkQ1Bz56dIare8l2WXUYBQiRt2dNbzB1qW_dNBq9W_oU6a3OalCaKTv731iWoJiPGIAG_OIsx1oVzoj1Imqllqe8671z92HF2XBNuQ3yDUgsYrfwy5gdEh6XOnSFtD9OI_e7eBHGFeiAaaxPqQfEHsQAJhjuvImYjszgarFyAxxPOgb7w4iOjyUyEm_qMxEElLG4-a1kzrZVdLvR4z-dd1SMRFExi7FjYzoXJcBY363uf23rWHMqJ2LhugYjQ37uX1w_KdXDo2kxDaey1QRDEi84xGGg63PIqqAd8IbEKr_74xzTroP1ObZj1Td1vSvRZjotuiylhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان هفته اول
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/681523" target="_blank">📅 22:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تبعات گرانی تعمیرات؛ تعداد زیادی از خودروهای در حال تردد معیوب‌اند
علیرضا نیک‌آیین، رئیس اتحادیه تعمیرکاران خودرو در
#گفتگو
با خبرفوری:
🔹
افزایش هزینه تعمیرات خودرو، بسیاری از مالکان را به تعویق انداختن تعمیر واداشته است؛ به‌طوری که تنها در صورت بروز خرابی جدی به تعمیرگاه مراجعه می‌کنند. شمار قابل‌توجهی از خودروهای در حال تردد از نظر فنی معیوب هستند که علاوه بر افزایش خطرات ایمنی، با نزدیک شدن به فصل سرما می‌تواند آلودگی هوا را نیز تشدید کند.
🔹
بخش عمده این گرانی ناشی از افزایش قیمت قطعات است و اجرت تعمیرکاران تنها حدود ۱۰ تا ۱۵ درصد هزینه تعمیر را تشکیل می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/681522" target="_blank">📅 22:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4U1wSR1ICLHUr81sLz_W578kkjd6XEARbSGrmxA2em6sPXZpQY0He603KGI1k3Q6fvtFDT6ct2mnm7DrEata7xLAvkRiM3WNNeJSyVAbNiVD_TJs00zxWi2swNDSgvA_j-4LEYEls9JBs-2YR9Mc1JoSuTbiffhiBL2OL9JjGQfuCy42DG0njGudSd9CptGeCQAhq7yihoW4c4o-UEVxQsI6nSrXwdjG2oYuGBrWeFORF3AlP6SvaHmJe9C1UScLt3FFmD_dECvH_Z3v7oLyUJVGsiipJivLtTrZ6aAmZESVE-7YVLe-29R_xCJqdbb1mD8l3DP-CEjCVOIH2N57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در جنگ شناختی از کجا تغذیه می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/681521" target="_blank">📅 22:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار باقرزاده: ۳ خلبان ایرانی توسط قطر به اسارت درآمده‌اند  فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح:
🔹
۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
🔹
«جواد صالحی»، «عبدالمجید دشتیان»…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681520" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای مضحک وزارت امور خارجه قطر: ادعاهای مربوط به بازداشت خلبانان ایرانی را تکذیب می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681519" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18db338ef0.mp4?token=gUYdNvnJdKvModOEwFqUbwO6WRZkqHM3RgFGJw-mgRSuEnkD_g8qbsx5YTNMhq8Kok5nx0IulLqtjDBJSwh7gWuWBt0G8rSUkHNmooITXVogWJNBLMoA33YtXyYV_wdLrwghKaBbwR6DvZ9mVElAevtNhbf4LlZq5QRhfnBs-HTP6ycFj8rXXDyA03SXf-c7OgjaMu-_D1FGmbwC6ReZSxLhtefROGYA3Rxm6tX1VqzFVhBOk9f0Rola5gGpyFQqgKO3LL5Dj35Uvk12-7tQK9r0iKNQNl4BS4SfT27at6D0WKn94x7wSop92VWT-qMdlEpHSzsdOgZ0Nt-oJ09JZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18db338ef0.mp4?token=gUYdNvnJdKvModOEwFqUbwO6WRZkqHM3RgFGJw-mgRSuEnkD_g8qbsx5YTNMhq8Kok5nx0IulLqtjDBJSwh7gWuWBt0G8rSUkHNmooITXVogWJNBLMoA33YtXyYV_wdLrwghKaBbwR6DvZ9mVElAevtNhbf4LlZq5QRhfnBs-HTP6ycFj8rXXDyA03SXf-c7OgjaMu-_D1FGmbwC6ReZSxLhtefROGYA3Rxm6tX1VqzFVhBOk9f0Rola5gGpyFQqgKO3LL5Dj35Uvk12-7tQK9r0iKNQNl4BS4SfT27at6D0WKn94x7wSop92VWT-qMdlEpHSzsdOgZ0Nt-oJ09JZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی میوه‌های خشک مثل نمونه‌های بازار نمی‌شوند؟
🔹
یکی از چالش‌های تولیدکنندگان تازه‌کار میوه خشک، رسیدن به محصولی با رنگ، طعم و کیفیت مناسب است. برای داشتن یک خروجی خوب، چند عامل مهم تأثیرگذارند:
🔹
انتخاب میوه تازه و باکیفیت
🔹
دقت در فرآیند شست‌وشو و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681518" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تنگه هرمز یا برنامه هسته ای؛ آمریکا از کدام سلاح ایران بیشتر می ترسد؟
🔹
ایران از طریق مساله هسته ای بیشتر می تواند از غرب امتیاز بگیرد و قدرت منطقه ای خود را بیشتر کند یا مساله هسته ای؟ کدام یک از این دو می توانند عنصر اصلی بازدارندگی در استراتژی جنگ نامتقارن ایران و آمریکا باشند؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3237925</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681517" target="_blank">📅 22:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بازگشت فرودگاه بین‌المللی لارستان به مدار پروازی پس از ۵ ماه
🔹
رئیس سازمان استخدامی: فقط نیروهای عملیاتی و استانی استخدام می شوند
🔹
اسماعیل‌نژاد کاپیتان جدید تیم ملی والیبال ایران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681514" target="_blank">📅 22:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
یک پسر ۱۱ ساله پس‌انداز ۲ هزار دلاری خانواده‌اش را خرج بازی کرد
!
🔹
یک خانواده در کانادا پس از ناپدیدشدن پس‌اندازشان متوجه شدند پسر ۱۱ ساله‌شان بدون اطلاع آنها، بخشی از پول را برداشته و ۲ هزار دلار آن را صرف خرید گیفت‌کارت برای بازی کرده است.
🔹
این کودک هنگام رفتن به خانۀ مادربزرگش، پاکت پول نقد خانواده را با خود برده و در دو خرید جداگانه، هر بار هزار دلار هزینه کرده بود.
🔹
خانواده برای بازگرداندن پول اقدام کردند، اما با توجه به نهایی‌شدن خرید، موفق به پس‌گرفتن وجه نشدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/681512" target="_blank">📅 22:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE0IlQGeeN5WUneEa-JqTsfzQw80D1sn9iwoG5zvDyx2ollkf-I7BvtVfYnlZvh2bgLXI7REKuRzBVgFKr45y8mIBWlqfs8KU8SzQHsR9BAbyhPXbSZUE38yy_NZ9aIPaSGoIc2Yp_iMlybKnF9H9a_PfX_leoeKDuO9rBTTk7gMVMfefXU2tEpL2U8a9EvR2Iid60taayEwxzpp_DkeOHqZFbwjBnTzJW4naRhhK0l7pGsH8BCYDbEI70_qfCn19wuMb5xFkqsNyJmDmVeGUOW_-glC3eFi8AlFdlOi-s2nNwdljC2g3WCdpc4HB7O8simqmxUDd5EE96rQ8SsKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر حرفی ارزش گفتن ندارد؛ گاهی سکوت عاقلانه‌تر است
🔹
امام علی(ع) در نهج‌البلاغه هشدار می‌دهد که زیاد سخن گفتن، احتمال خطا و پشیمانی را بیشتر می‌کند. ارزش کلام به تعداد جمله‌ها نیست؛ به سنجیده‌بودن آن‌هاست. گاهی یک جمله به‌جا می‌تواند احترام بسازد و یک حرف…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681511" target="_blank">📅 22:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916213bf74.mp4?token=MnVisPy1dXMJeIvuG6bLlfnutR2Cqt9wyUuBYp-im_Cas8kzAbH3KaR4iKFH-8r8KdtQ2gm2JjpPHynWns355Ay2csv3idf1CArvfVRyHE0Q5bM2kzlv5DBIvlfyw1qRpkHrMzu8OXKQ1TyHRgLLqdtUQONnMmgOq73iYuXFeluA_L0A27gCAIXzy67G_mZ3HxLmqsF39RyGY1dJNE5okmUoP6FKtWf6zOXYD8ampx1z-ghxRCRMUeLz1qxMcNZIebYUBKuzUTgdxkAkkAc3REIOYVD5tve_noiplGCI1RiSKOkgdPHCrSLXBEbYjWnYk1gaobXmhfuvkuOdMvf_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916213bf74.mp4?token=MnVisPy1dXMJeIvuG6bLlfnutR2Cqt9wyUuBYp-im_Cas8kzAbH3KaR4iKFH-8r8KdtQ2gm2JjpPHynWns355Ay2csv3idf1CArvfVRyHE0Q5bM2kzlv5DBIvlfyw1qRpkHrMzu8OXKQ1TyHRgLLqdtUQONnMmgOq73iYuXFeluA_L0A27gCAIXzy67G_mZ3HxLmqsF39RyGY1dJNE5okmUoP6FKtWf6zOXYD8ampx1z-ghxRCRMUeLz1qxMcNZIebYUBKuzUTgdxkAkkAc3REIOYVD5tve_noiplGCI1RiSKOkgdPHCrSLXBEbYjWnYk1gaobXmhfuvkuOdMvf_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی نگاه از مرزِ دیدن عبور می‌کند؛ خلاقیت متولد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681510" target="_blank">📅 21:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بقائی جنایات امروز اسرائیل در لبنان را محکوم کرد
🔹
سخنگوی وزارت امور خارجه ضمن محکوم کردن جنایات امروز رژیم صهیونیستی در لبنان، حق قانونی و مشروع لبنان برای استفاده از همه ابزارها جهت دفاع از کیان کشور در برابر تجاوز این رژیم را یادآور شد و بر همبستگی جمهوری اسلامی ایران با لبنان در مسیر دفاع از حاکمیت ملی، استقلال و عزت این کشور تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681509" target="_blank">📅 21:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf7fe58a0.mp4?token=u9OXgU3tE7sRhGYRZ6xlzTMbpPsp7YKelp3Nsrdb0dsEjAHl9mJJvxTUOmwwp7w59QcPHaSkrG7Ot-gEwCdk7UTJ604Ba5vYt7s1ydOOvp47VQfRBrcuuuYbexNjmhwr8PQMkc8dZvphvaSAhjMMbp1BK5Ein6hjd4DBdp6xSdPyNyYhIQwY2NhgmoUMEBMBxEZpdu-S9qQtSLboBRqCgYflTSIaTYPZp2eXZcPuNhyXilidftV1Yd4tLFpwo6WngFWMVl-85-Je55Rp_MpcOt3CKyG4u4r9DYDkmb_edfwV_o1h-2fzZS2yJ6DUA-BUXEWbz9hhuHJfb5iMLdPr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf7fe58a0.mp4?token=u9OXgU3tE7sRhGYRZ6xlzTMbpPsp7YKelp3Nsrdb0dsEjAHl9mJJvxTUOmwwp7w59QcPHaSkrG7Ot-gEwCdk7UTJ604Ba5vYt7s1ydOOvp47VQfRBrcuuuYbexNjmhwr8PQMkc8dZvphvaSAhjMMbp1BK5Ein6hjd4DBdp6xSdPyNyYhIQwY2NhgmoUMEBMBxEZpdu-S9qQtSLboBRqCgYflTSIaTYPZp2eXZcPuNhyXilidftV1Yd4tLFpwo6WngFWMVl-85-Je55Rp_MpcOt3CKyG4u4r9DYDkmb_edfwV_o1h-2fzZS2yJ6DUA-BUXEWbz9hhuHJfb5iMLdPr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌وقت نمی‌توان مستقیم پول به کشور وارد کرد، تراستی‌ها به خاطر تحریم جریان ارزی ایران را مدیریت می‌کنند
!/ تلویزیون اینترنتی مدار
گفتگوی کامل را اینجا ببینید
👇
https://youtu.be/BNd_H49d3ic
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/681508" target="_blank">📅 21:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC2OBL3hkZWUX_jJBYEVmFGSPq72hugLczuPc2q_knYKC90Crje2iakG-2hLgp2RlktXPjxpjrWlEltkPL89dWF8cqsPtDwL98VMPiREtwYKzvxiRrJVISF66hZN-Va2hU5UzGVM1RNo73f51NtUzCaiWtajUeM0mXkEtQ5DbZsbR1Gq9uAhNUgFLYsxR9aMupzbtvAsqJYE8rRkJaoAx5e8EvtPxcur-wMS_fA17WmnnmGaC7R2FInair1PPLyW0Cak0cRq-YSwwahnNHLEA13M6hEWaYn0ixll04tMeNS7CjlNRYZ4kNJypS3eQ0hmeQBVpcu7Lm1c-2RK7IiUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت شاخص توسعه انسانی در جهان
🔹
شاخص توسعه انسانی بر اساس ارزیابی سه معیار اصلی «زندگی طولانی و سالم»، «آموزش» و «رفاه اقتصادی» محاسبه می‌شود.
🔹
ایسلند با امتیاز ۰.۹۷ در رتبه اول شاخص توسعه انسانی قرار دارد و کشورهایی نظیر آلمان، بریتانیا و امارات نیز در رتبه‌های برتر جای گرفته‌اند.
🔹
ایران با امتیاز ۰.۸۰ و کسب رتبه ۷۵ جهان، بالاتر از میانگین جهانی ۰.۷۶ قرار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/681507" target="_blank">📅 21:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-AWlNCuSsuBLvuBCySeOk_1Fer-DXc9a6qr0MCQOvtpZq-1fDjtB5Ofwa7cCHc78foJdHfMpzGc3CFVhC-PgsGAfPagDdrP-ymQRkxpCSS7PaXvZWgU6lqzIbxoe0O6mZKNp3X6aMASFGIinKL6NLBXrDILG0rNe1Zenf-qrU-nASkXep4G9trDIphSHVhi6VyC7PFEtByhQejblAmyRzIFB2bX5qgfOjH1hJgIRiC8jjfLZ_GdcxY8ecY-WrbpBnipLvJCKxtZgAstWe7To2F6jHW1G2T_K1P9II8oPlnRHrWQf8KsJSB-KHtnRBqBqhyiIN9hQ1CmT2SGvPL8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم پرسپولیس به شمس آذر توسط عمری در دقیقه ۱۶
🔹
پرسپولیس ۲ - ۰ شمس آذر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681506" target="_blank">📅 21:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa0fd153b.mp4?token=j2O5sZz3fccw_Di4fYmyhUPjnAHfhYy6tmxokLsiYvPHWw17o-qBASN679WeTVix39nS-TKCiMzzEINNMA6lHwIpro_qCn5g1Kv2GP73qnxxU9dP3yMfAWFaOBFYzWZEyAddtZnL65qYRcApC_4mCKVqJFiN7j3KSsNIu0MvTVDKbdICp3OM1MVRaYwO2B7b1br_oIBSS2Mu9WxAY6H9vDxjOt9vPPwB-ZB-jJ77W_6ALBlbo0SqqxHWvLBTIfg0MA6_whO0J_C3VFbZeTdspZe13k9-A2DzKuPsrJu3E5rm-nZ5Im6WCQtBTsT2-WXmyUvcfOknRwdtffzucDc0mzP6PsIeX6ZTdBvTAQNRnVdta1RXSRKxgrUhYT1wpV7KLuKHILw7nAoZJpOy3rKXBXNGETTM0SuS0jV8dt8KWn7LU2ZIE_AG-dGdq_pOp2wmoPekoHIsHeQmbjMnGFJx5Bo8kEx3aHbHIBfpRyEmarGxoSzqYzw3S6wjy55-W-XtUTYSTZjRvShbFXHSt3YM0xhKXVD7tmWi1iMkt_40Dpc-Z78rtQU0EE8h2_sstL1DJK5_Dlm8O8_9wQlZl_C7dTixbiKTK-UeembuqdX9y-Q9h42mRliqw1Ro82rPFiYK6YCKPFJ3buWywOslEKbIR3-7_c_Px9ZMHEn1OZD0Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa0fd153b.mp4?token=j2O5sZz3fccw_Di4fYmyhUPjnAHfhYy6tmxokLsiYvPHWw17o-qBASN679WeTVix39nS-TKCiMzzEINNMA6lHwIpro_qCn5g1Kv2GP73qnxxU9dP3yMfAWFaOBFYzWZEyAddtZnL65qYRcApC_4mCKVqJFiN7j3KSsNIu0MvTVDKbdICp3OM1MVRaYwO2B7b1br_oIBSS2Mu9WxAY6H9vDxjOt9vPPwB-ZB-jJ77W_6ALBlbo0SqqxHWvLBTIfg0MA6_whO0J_C3VFbZeTdspZe13k9-A2DzKuPsrJu3E5rm-nZ5Im6WCQtBTsT2-WXmyUvcfOknRwdtffzucDc0mzP6PsIeX6ZTdBvTAQNRnVdta1RXSRKxgrUhYT1wpV7KLuKHILw7nAoZJpOy3rKXBXNGETTM0SuS0jV8dt8KWn7LU2ZIE_AG-dGdq_pOp2wmoPekoHIsHeQmbjMnGFJx5Bo8kEx3aHbHIBfpRyEmarGxoSzqYzw3S6wjy55-W-XtUTYSTZjRvShbFXHSt3YM0xhKXVD7tmWi1iMkt_40Dpc-Z78rtQU0EE8h2_sstL1DJK5_Dlm8O8_9wQlZl_C7dTixbiKTK-UeembuqdX9y-Q9h42mRliqw1Ro82rPFiYK6YCKPFJ3buWywOslEKbIR3-7_c_Px9ZMHEn1OZD0Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باز کردن یک بسته اورژانسی قایق نجات تاریخ ۱۹۴۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681505" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e4cdab3e.mp4?token=DXH6str-zR0fo4prD74DS5jDpRUhiH-r9OEDGnZgiih2_k1duEMCkgBubpCDsnOEuZhHIZwagMx8MGQZmWTrXXvFCMud26ADSa9dgpOLjrtsD1nSNZp20w6oN1tin9VSXX3wAy7U_yHN2jsRY17FsmREewusp8CV4HgG2Yb9CvOmiW5Lmu4vvyHDlmTFmZ1TzanaFVVMrGioYsWGz-_gJtdlxaqj8-r5p8o16Kh_Cb26EZe287tFqgmNEPqM2c5pLKdDOtjSlxNmCeuF-yfOVBCpZ6-y3nK9UgMgfXNcRQbDExO3Q1kNBbW_fH5llejumONm9Hm-MHflcu40MJ24gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e4cdab3e.mp4?token=DXH6str-zR0fo4prD74DS5jDpRUhiH-r9OEDGnZgiih2_k1duEMCkgBubpCDsnOEuZhHIZwagMx8MGQZmWTrXXvFCMud26ADSa9dgpOLjrtsD1nSNZp20w6oN1tin9VSXX3wAy7U_yHN2jsRY17FsmREewusp8CV4HgG2Yb9CvOmiW5Lmu4vvyHDlmTFmZ1TzanaFVVMrGioYsWGz-_gJtdlxaqj8-r5p8o16Kh_Cb26EZe287tFqgmNEPqM2c5pLKdDOtjSlxNmCeuF-yfOVBCpZ6-y3nK9UgMgfXNcRQbDExO3Q1kNBbW_fH5llejumONm9Hm-MHflcu40MJ24gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه بخش‌هایی از ایندیاناپولیس در آمریکا به دلیل سیل شدید
🔹
شهردار ایندیاناپولیس در آمریکا از ساکنان خواست که از راونزوود، راکی ریپل و سایر مناطق  به دلیل سیل شدید که بدترین مورد در حداقل ۳۰ سال گذشته است، تخلیه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681504" target="_blank">📅 21:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تایمز اسرائیل: آخرین ناو آمریکا از اقیانوس آرام خارج و به سمت خاورمیانه رفت
ادعای تایمز اسرائیل:
🔹
جنگ طولانی‌مدت ترامپ علیه ایران، خروج آخرین ناو هواپیمابر آمریکا از اقیانوس آرام را اجباری کرده و منطقه را موقتاً بی‌دفاع گذاشته است. چین از این حواس‌پرتی برای تقویت نفوذ منطقه‌ای خود بهره‌برداری می‌کند.
🔹
تحلیلگران هشدار می‌دهند که برنامه‌ریزی ضعیف و استقرارهای طولانی، خدمه را خسته و منابع دریایی را محدود کرده است و نشان‌دهنده تغییر استراتژیک از آسیا به سمت خاورمیانه و نیمکره غربی است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/681503" target="_blank">📅 21:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423009927c.mp4?token=KaAxe_kuukLHzhDoMbsJDHiQRuOzpvr-GfygFEnFxuTXQ7C_qitwgqadl7aD7no6My02tlq_dkR9_N9tk-3sIljBwXVFjLKNCdNC9B_Em8u3fjuZcstXb80YoFDjaURPukfaD_LsreaGFkFVMAa54wg1fSvGzuGcJSpiMTcJwDcJGYPUbXnTijyr4HAxJYwX3WobqHlbEjKq1GbZECu2RDboaZ1vemCwnOfLBEIvSR-vctlPY6-ZZC6Am5i13cl49c8ONRMc-PFuYfq_yYz-Xfr6zlvqkJZBJSG2-bAETuh68Tcq8r8HuVPhY9ntdZ3eCVNNv4r5KpH3ep3YSnaKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423009927c.mp4?token=KaAxe_kuukLHzhDoMbsJDHiQRuOzpvr-GfygFEnFxuTXQ7C_qitwgqadl7aD7no6My02tlq_dkR9_N9tk-3sIljBwXVFjLKNCdNC9B_Em8u3fjuZcstXb80YoFDjaURPukfaD_LsreaGFkFVMAa54wg1fSvGzuGcJSpiMTcJwDcJGYPUbXnTijyr4HAxJYwX3WobqHlbEjKq1GbZECu2RDboaZ1vemCwnOfLBEIvSR-vctlPY6-ZZC6Am5i13cl49c8ONRMc-PFuYfq_yYz-Xfr6zlvqkJZBJSG2-bAETuh68Tcq8r8HuVPhY9ntdZ3eCVNNv4r5KpH3ep3YSnaKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقابله نیروهای امنیتی مراکش با هجوم مهاجران غیرقانونی به سئوتا
🔹
موج جدیدی از مهاجرت غیرقانونی در مرز منطقه تحت حاکمیت اسپانیا، سئوتا، ثبت شده است؛ جایی که گروه‌هایی از مهاجران از جنگل‌های اطراف تلاش کردند وارد آن شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681500" target="_blank">📅 21:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYm28UWFG0maBgCPU2eEkRZoC_Mv1tVJ5qsPdaidR-4T5OXLR4zSfkACsuGnsgKDG6hesLFX_ah3jBJG2BeEUtz6D-iQVLG3hSHA8AJ6gyR8Kl1F9SqXRJjXlTn5lB9j4DjMa-SPAYPf4GFA87W075fD1rwZtkEP83LefGn4vykfC4LX4WZRwSqqePy0b5_MXG_uEVFxZXl5fq7CYioEd4zF58wkqPa5NsLoNnCGL3Ds-Ka5oVGffuKP4WCgwCtEJsWZ5KCstcWgb5Bw9tX7mtTQb_gOtpBPnNBDcsatioeukdbb3ggCjfjBpNzIZIusjuizXKJdVx9Yn4SX9lmTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نگران تمدید بیمه نباش؛ ۱۱ ماهه پرداخت کن!
با امکان
پرداخت ۱۱ ماهه
، می‌تونی هزینه بیمه رو راحت‌تر مدیریت کنی و همچنان از
پوشش کامل
بهره‌مند بشی.
این طوری :
بیمه‌ت به‌موقع تمدید می‌شه
هزینه‌هات بهتر مدیریت می‌شه
نیازی به چک و ‌ضامن نداری
✅
بیمه‌بازار
کنار شماست تا بیمه‌تون رو متناسب با نیازتون و به‌صورت
قسطی
تهیه کنید.
👈
تمدید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681497" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7w4Lki2DH0IMlz_n4WxxFZXfeAPatg8I4pb7YOGFaujJs26SDEChzm8VcCgtfC-HPXtj_7Eiq1wlcde8p-qa4rueUiQrfbcLCzZwHwgf8pdKjoFiHnQXFXMoW7X8dzgnf6HwNzZB2__CbbDlmZ5laQ2WK87xx3sR6qhvNUTK6dztg3SM6QWJS4l_s3vVamQcHl04ZMFImdEw0ZCuvKjZUp4uKALr8DuF2QRpDyrS-CKpEJOd-EdCYOoF9aC0ImNH-lrKL0s1xoHZqPwI9vS8PvwCSRxqCXfz4BflehpB5mGZgXAVai_UZtdZSRqeZfJFu-_5psXC954bTHhqus7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد رسول‌الله (ص)
🔹
کارگردان: مجید مجیدی
🔹
ژانر: تاریخی، مذهبی، درام
🔹
بازیگران: مهدی پاکدل، علیرضا شجاع‌نوری، محسن تنابنده، ساره بیات، مینا ساداتی، رعنا آزادی‌ور و…
🔹
خلاصه داستان: داستان از سال‌های کودکی پیامبر اسلام (ص) آغاز می‌شود؛ دورانی پرآشوب که مکه…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681496" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزارت علوم: امتحانات ترم تابستانی حضوری است، اما در محل سکونت
سرپرست دفتر برنامه‌ریزی آموزش عالی:
🔹
امتحانات مربوط به دروس ارائه شده در بازه تابستان بایستی به صورت حضوری برگزار شود و برگزاری امتحانات به صورت مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681489" target="_blank">📅 20:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681487">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgKtx4I2zb8jMNHlmDaUURRnQYxvDtNUV-G9dm6iIn6nulXaYz5cRHg1L-kP9Cl7kl8wC5szvMhYNy4_1ac0r9_z91CJbf6WTTqIYnUZ2YTAo5ch_2i6LsYVSivx87fzn4DOYKus1ZPhDNMVbSyzD9OVruR3uIndotdEpxPX4kPm2gpAg0XVP0diQ0tJM4wXJv9Q6aSL1yTEKWPg-Atnu7OMoPkT97FAhl29CWA3-9yDHLMzC1jR3xMWM_3uhg4Tyi4dF47xdMmQLuVh1_NjqDdFjDt6CJWDpLZyjHbZQH67eM5wnuTK-isj8zJErozMOEzxqYMf4KKTJ2BDpBRcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک رسانه اوکراینی: ایران از زلنسکی می‌ترسد
ادعای کیف‌پست:
🔹
حاکمان ایران، زلنسکی را «دلقک» و عروسک خیمه‌شب‌بازی غرب می‌نامند اما شدت واکنش آنها چیز دیگری را نشان می‌دهد.
🔹
راهبردی که بر ادغام تولید اوکراین، فناوری اسرائیل، توان آمریکا و سرمایه کشورهای خلیج فارس استوار است و می‌تواند هزینه دفاع از متحدان آمریکا را کاهش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/681487" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681486">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روزانه ۱۵۰۰ دلار درآمد ارزی ایران در مرز افغانستان از بین می‌رود
رسول نصیری، رئیس انجمن صنفی کامیون‌داران تایباد در
#گفتگو
با خبرفوری:
🔹
با وجود اعلام حذف عوارض متقابل، کامیون‌های ایرانی برای تردد به افغانستان همچنان باید ۳۰ تا ۴۰ میلیون تومان هزینه پرداخت کنند، در حالی که ناوگان افغانستانی با هزینه بسیار کمتر در ایران فعالیت می‌کند.
🔹
در شرایط فعلی، ناوگان ایرانی در بهترین حالت تنها دو سرویس در سه ماه انجام می‌دهد و بخش زیادی از بار در مرزهایی مانند دوغارون و ماهیرود به کامیون‌های افغانستانی واگذار می‌شود. گسترش ترانشیپ در مرزها نیز باعث شده روزانه حدود ۱۰۰۰ تا ۱۵۰۰ دلار از درآمد ارزی ناوگان ایرانی از بین برود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/681486" target="_blank">📅 20:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681485">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وقتی شیطان در لحظه مرگ وسوسه می‌کند؛ روایت عجیب یک تجربه نزدیک به مرگ
🔹
00:08:00 تلاش شیطان برای انکار خداوند هنگام جدایی روح از جسم
🔹
00:38:30 نفرین شدن توسط فرشته‌ها هنگام دروغ گفتن به مادر
🔹
00:52:40 خوردن سه سیلی برای سه دسته از گناهان
🔹
00:56:45 دعا کردن و قول بازگشت به دنیا توسط روح جنین خانم باردار در بیمارستان
🔹
01:07:00 علت نارضایتی انسان‌هایی که در صف‌های طولانی، نان و شیر و خرما می‌گرفتند
🔹
01:10:00 تأکید دختر بچه سه ساله به خواندن نماز
🔹
01:16:10 نمایان شدن خورشیدی بزرگ با بردن نام علی در اذان
🔹
01:18:15 توبه قبل از تصادف در شب سوم محرم
🔹
قسمت سی‌ویکم (این چرخ گردون)، فصل پنجم
🔹
#تجربه‌گر
: سیدهادی سجادی بلالمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681485" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681484">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دیدن این ویدئو می‌توان تاثیر پیشرفت علم در سلامتی و کمک به انسان در بقا را درک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/681484" target="_blank">📅 20:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj7mbPkaCpIUYpki-WkcMQx4NByD2dSZL1NjA_GPGz8uTrCaN_Yrzyhc9MeTuXsGFcSAMeUDm1AfjWIVcWj0ii8dVnXwcJm9KqfmNtf_q-2bddR8cNbgXBSY33tGp8IDDiMcU5gXDkVDuWqy8uwR2nGXvPPkiVY1QHu1wV8m63R2JgnJ3TUeFa-Uy9GfajnE3FVz3pLFT9aTBnhpP0VCH_fHjj5DMq-SInlfn2ySNcpqhAmODXdwwCyG1VnRqhOUmTC70NTxi1hcevNCQmZI7Jw93wRvGDm28NepFHpKf-aFUq5TojDbzhMMlmbXNoSkOzVUMzz5-BqP-wrUjYSC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم مراکز داده از میزان مصرف برق جهان
🔸
مصرف برق دیتاسنترها در سال ۲۰۲۵ به ۴۸۵ تراوات‌ساعت رسید که معادل ۱.۵ درصد از کل برق جهان است.
🔸
پیش‌بینی می‌شود این میزان در سال ۲۰۳۰ به ۹۴۵ تراوات‌ساعت افزایش یابد و سهمی معدل ۳ درصدی از مصرف برق جهان را به خود اختصاص دهد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681483" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmniZKa5rYietQ7MRPglZRDGkNXEv6HYFEHW5HQaF2AFubdTaQRp9BekKdi5TfTApEzjsUZ7NajDgbv7SQN58mH9UCP875W92NykCjdGjN0MQuIbw-GqnaxQruO6UQyPJAe1uK7UkpHl70hy57xvJn7yEMAOUq0_VDjKjziSENke_Cx4Kox-5wXZFMWQ5T6uAOD_0-C2rHJGMaZ0WuLcOvi8iVtf2u173ip00RyKuUC7ySMwd_cDfPysmyPeMQ8aIPh-D_c37g56O1sqWxGU5Sx80-eJ2XpaEGDciHdesuvFcm-Xox6QQ5lWVr9iW4RxTe_8nATSa8Pd1cf5HKNMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم
🔹
رئیس جمهوری آمریکا با انتشار تصویری از خود و رهبر کره شمالی مدعی شد: من و کیم جونگ اون خیلی خوب با هم کنار می آییم!
🔹
با وجود نگاه غیردوستانه در این تصویر خاص، تصاویر زیادی وجود دارد که در آنها لبخند می‌زنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/681481" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9f8e13d8.mp4?token=O1PuZfRaUSPXDHTlKuDHMvvniYwd-EdOC6aUzNEbLO74qiDptfT2l4keuzNaPgodPIjzPqdF3l6R9YoOKtHmFfS278W2-qbGZydOnPAyMhwuqZ4CHe6ZKyBmcmgjVtpIAGRhQp81NtppxZhkdS69zrnr0oly2wZoHC1NSBmEBVaDmLEIlQvCdYGYK9d-RGkKqsPyuNXOO8ULc69vrtZa01Hs-po9-nnsNxmi5a1CN6vBbNYHtClQnM2OHGxDWHadXPPO5oFlSRsIWphfiZmjq07n2MeHVY_XY1tdXlHTuijMHWXyBwlIsrfJzUcUg_VU9tzpnoMbQ7NA_u1Deu0GYUq2u0xEsZbn6q6FEZ0wuwnzES9dEDfcJ0WZtFsLxRGSllGtdaRUhZyEyEgL4Fdabq_tYc11IKrbtGRaeVOukBfJ_EbnYBro6jZYCznQNAQo37VRxiEk9MnQGl9UiptoXgtPtEA-5dlvYYz2XOKlumeIyELffvrPwl2Z9hBKqf20aX4Esqpdyy8_-Ys_TVU_ubiBjVlJ7HCMtUqK7clhLQ3u6ywHaX5EcvRj9BF3ILD2ibx_5H-kYYp3_hF9KhdIh4JmKrV7UZ0My8NjjKsLyurVfotTPRFc04wDX7Jmosgdpe1NlROmNDzGsLIGdQKRcbHqjvyuDlwzfBDr7m-Ynew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9f8e13d8.mp4?token=O1PuZfRaUSPXDHTlKuDHMvvniYwd-EdOC6aUzNEbLO74qiDptfT2l4keuzNaPgodPIjzPqdF3l6R9YoOKtHmFfS278W2-qbGZydOnPAyMhwuqZ4CHe6ZKyBmcmgjVtpIAGRhQp81NtppxZhkdS69zrnr0oly2wZoHC1NSBmEBVaDmLEIlQvCdYGYK9d-RGkKqsPyuNXOO8ULc69vrtZa01Hs-po9-nnsNxmi5a1CN6vBbNYHtClQnM2OHGxDWHadXPPO5oFlSRsIWphfiZmjq07n2MeHVY_XY1tdXlHTuijMHWXyBwlIsrfJzUcUg_VU9tzpnoMbQ7NA_u1Deu0GYUq2u0xEsZbn6q6FEZ0wuwnzES9dEDfcJ0WZtFsLxRGSllGtdaRUhZyEyEgL4Fdabq_tYc11IKrbtGRaeVOukBfJ_EbnYBro6jZYCznQNAQo37VRxiEk9MnQGl9UiptoXgtPtEA-5dlvYYz2XOKlumeIyELffvrPwl2Z9hBKqf20aX4Esqpdyy8_-Ys_TVU_ubiBjVlJ7HCMtUqK7clhLQ3u6ywHaX5EcvRj9BF3ILD2ibx_5H-kYYp3_hF9KhdIh4JmKrV7UZ0My8NjjKsLyurVfotTPRFc04wDX7Jmosgdpe1NlROmNDzGsLIGdQKRcbHqjvyuDlwzfBDr7m-Ynew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا طلا می‌تواند به رشد تولید ناخالص داخلی (GDP) کمک کند؟
🔹
عبدالرضا عسگرخانی،هم بنیان گذار و مدیر عامل داریک (انبار هوشمند فلزات گرانبها) در نشست تخصصی با عنوان دارایی دیجیتال،فرصت سازی و فرصت سوزی در همایش چشم انداز اقتصاد ایران 1405، از نگاهی نوع به موضوع رشد شاخص GDP کشور با کمک تکمیل زنجیره ی ارزش خدمات، پرداخت.
🔹
خلاصه ای از این نشست را از زبان آقای عسگرخانی بخوانید:
« ما به این باور رسیدیم که رسالت‌مون فراتر از یک ابزار معامله‌ست؛ باید ارزش افزوده‌ی واقعی خلق شود، ارزشی که به رشد اقتصاد کشور هم کمک کند. و این اتفاق، تنها با تکمیل زنجیره ارزش امکان پذیر است.
🔹
با اطلاع داشتن از اینکه خرید طلا یک تصمیم استثناییست، چون سرمایه‌ی مردم حفظ می‌شود. اما نگاه ما به همین یک قدم ختم نمی‌شود؛ چون از منظر توسعه‌ای، صرفِ خرید طلا کافی نیست.
🔹
برای همین، انبار هوشمند فلزات گرانبها تحت عنوان داریک خلق کردیم؛ حلقه‌ای که زنجیره ارزش رو تکمیل می‌کند و تاثیر مستقیمی در صنعت کشور می گذارد. »
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681480" target="_blank">📅 20:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafc011c98.mp4?token=ANDF6yUw99Six8yuRlBoHgPf6Y2XtCjv0ggeudMvoakdDGG3xDlbJGNNiQ223mgr2_UHYEq8ofbPFpZHjdhK5Bd_Dtl121PXQ6qpY1SlcfWUREMpYOVN-5yy7Vjh20kPZcdBZ80q_mLheVUXDJvoJwh_XNIZeUplLW-tUpQvCTP71JdliGs-gkJiyKawFlCCXs7bMrQDwMibffKheiOgIwscCIUVHLVwup3Jw0Q_E0-SCddsN_AxZRfziaQansP2BUkuXeGoYQoOxDx5tYcR5wg76hQHePfj87skucE4eOa4b0PZdmbUHtV8RCvnJ6GGVhz0J-m9UWJY0ZHpMsTyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafc011c98.mp4?token=ANDF6yUw99Six8yuRlBoHgPf6Y2XtCjv0ggeudMvoakdDGG3xDlbJGNNiQ223mgr2_UHYEq8ofbPFpZHjdhK5Bd_Dtl121PXQ6qpY1SlcfWUREMpYOVN-5yy7Vjh20kPZcdBZ80q_mLheVUXDJvoJwh_XNIZeUplLW-tUpQvCTP71JdliGs-gkJiyKawFlCCXs7bMrQDwMibffKheiOgIwscCIUVHLVwup3Jw0Q_E0-SCddsN_AxZRfziaQansP2BUkuXeGoYQoOxDx5tYcR5wg76hQHePfj87skucE4eOa4b0PZdmbUHtV8RCvnJ6GGVhz0J-m9UWJY0ZHpMsTyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زعفران خوش‌رنگ و خوش‌عطر می‌خوای؟ این روش ساده، رنگ و عطر زعفران رو چند برابر بهتر آزاد می‌کنه
🌺
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681479" target="_blank">📅 20:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leRHJGB5J74Jq3xIPX-cfCSXHgYbw8-I3akzR6UxbZoNZIsNsYpdeQzc5ARPn08Gq8kKbneqfl7ezSGVMFQUkZ1cmMHaYSs_VAPGq4WtcuNmlcRilba_zdCBP3RK1eU0BPq1_d202G2DKqF74-JiXJ8IEFOM96-k0ckpf17khJnkexXPgfYTV4libwUdPijFh5TaeUPRB4C7Ux5Oz3F7DyvijrpoxkOnVPhqyXsG_hgeR8MqjE4GeVRwGxn55n4uo1qiX0qMGKfb5kc2EOpVFC8N7mb35ENfpMbSvXc75KB4DerrRXSKLP0XBfLaEY_DmbAP2UL35RO7RXL1e36c9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلوف پیروزی در اوج استیصال؟
🔹
ترامپ در حالی در اظهارات اخیر خود از تداوم فشار اقتصادی و کنترل اوضاع سخن گفته که تضاد این ادعاها با بن‌بست میدانی در هرمز، غیرقابل‌انکار است؛ واقعیتی که اِی‌بی‌سی نیوز به آن اشاره کرده و اندیشمندانی چون جان مرشایمر هم روی آن دست گذاشته و معتقدند کفه معادلات به نفع ایران سنگینی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681475" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a7791576.mp4?token=k48bHoQ5_SXnsiNkJ3wT2pOWHN2GMAe6VxPLsztsGfKwkMKEMLlN6R2AIauCUhb3sA5N8SO7BWK_gAr8N9eXJr-QewHo0TyRGgiggg_OMRgOY3u-aqOo8hFwy8izEHNXOIxDO8qmZS3Sc4uS2iowP-bd3PQRr4jJspU8O_TwsCJQr5O37pWk5f-QN1_qLUQYX7P-TuR1GmA8bTjD6P8vq-ljYk9qAOqImegyLlHP6GbVLWT6kaGmByjsys0KbtSwkC2UnGCbv2eyQIHhTMyvpHVhuiQ0QkvuQuU6elBwqMSv6xoUFtIpz5vcB-Ql0o0Fh-3HyvSVbVTw6QCMFOwrPzlUlwxzSOOsgzuKV3DOPEketFagM4ouu6epekgk75Fcw36ga8r_N_98KzYFMv3d7_-8lxvQVxE8kPB2tPikJnub8_IxZuyp-hf4hm1DyKDaSnEaNOlcif7VnbtYlaRaqjOArFkmpYcjqXOsS6LfuBJMdqr-xRSvZKO7Qkrf8PUGCCR0vE0HijVQAEB0yRixg30y3qdeYExQVBNHGxyrv0XtVjN60rQXEROd1VUGJ3GDE0zAQ0QGplcuyCP6NnSK0hSC69ehMnAezGAr5Qmytk0cJYZX2mSBxihufIFJelK6TrUnwusoozbmLIFw4u4mndTZ0m_ZygWNOY6NUcizC04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a7791576.mp4?token=k48bHoQ5_SXnsiNkJ3wT2pOWHN2GMAe6VxPLsztsGfKwkMKEMLlN6R2AIauCUhb3sA5N8SO7BWK_gAr8N9eXJr-QewHo0TyRGgiggg_OMRgOY3u-aqOo8hFwy8izEHNXOIxDO8qmZS3Sc4uS2iowP-bd3PQRr4jJspU8O_TwsCJQr5O37pWk5f-QN1_qLUQYX7P-TuR1GmA8bTjD6P8vq-ljYk9qAOqImegyLlHP6GbVLWT6kaGmByjsys0KbtSwkC2UnGCbv2eyQIHhTMyvpHVhuiQ0QkvuQuU6elBwqMSv6xoUFtIpz5vcB-Ql0o0Fh-3HyvSVbVTw6QCMFOwrPzlUlwxzSOOsgzuKV3DOPEketFagM4ouu6epekgk75Fcw36ga8r_N_98KzYFMv3d7_-8lxvQVxE8kPB2tPikJnub8_IxZuyp-hf4hm1DyKDaSnEaNOlcif7VnbtYlaRaqjOArFkmpYcjqXOsS6LfuBJMdqr-xRSvZKO7Qkrf8PUGCCR0vE0HijVQAEB0yRixg30y3qdeYExQVBNHGxyrv0XtVjN60rQXEROd1VUGJ3GDE0zAQ0QGplcuyCP6NnSK0hSC69ehMnAezGAr5Qmytk0cJYZX2mSBxihufIFJelK6TrUnwusoozbmLIFw4u4mndTZ0m_ZygWNOY6NUcizC04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه آسای یک زن آلمانی در آتش‌سوزی ساختمان در طبقه یازدهم
🔹
زنی از طبقه یازدهم حین آتش‌سوزی در یک ساختمان بلند در برلین به داخل سبد آتش‌نشانی ‌پرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/681474" target="_blank">📅 19:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8908695220.mp4?token=sZ_iMLpjQ0BEAQJt9ToPxX-c_UI_XA5loIGlI2Pu7ajgYhgJeGnGkZP7qLFbz2wCAcEnbXYPLUA-zoqBY_vrpjBcxJoqRjnjOeLcNgL_44CpVrg_gSbnVtJn5rHVjog1qqPmvt9JpHYkQO7aDvsBXWHyuoZ4EqthfPPkOw_ESN0JvbI41syYrxeTp51lsNAlLGNPFYg4OXwp9rN9EjKxn6UrwRxtIYZkbwaJYhXw4N7sBKCAede12rPWte6PaMY_okhh5BcE8YKy0RbBAksh-w7NOPFGW9TlIJ2HnAbCSW2aNl7N5H0LqtWL5nkxyIf2Asbm5Bl2mB8zYA0MB-CJEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8908695220.mp4?token=sZ_iMLpjQ0BEAQJt9ToPxX-c_UI_XA5loIGlI2Pu7ajgYhgJeGnGkZP7qLFbz2wCAcEnbXYPLUA-zoqBY_vrpjBcxJoqRjnjOeLcNgL_44CpVrg_gSbnVtJn5rHVjog1qqPmvt9JpHYkQO7aDvsBXWHyuoZ4EqthfPPkOw_ESN0JvbI41syYrxeTp51lsNAlLGNPFYg4OXwp9rN9EjKxn6UrwRxtIYZkbwaJYhXw4N7sBKCAede12rPWte6PaMY_okhh5BcE8YKy0RbBAksh-w7NOPFGW9TlIJ2HnAbCSW2aNl7N5H0LqtWL5nkxyIf2Asbm5Bl2mB8zYA0MB-CJEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به شمس آذر توسط عمری در دقیقه ۱۶
🔹
پرسپولیس ۲ - ۰ شمس آذر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681473" target="_blank">📅 19:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOKWFht1fV5yo9N4WFoUtPngP9uu1i8FZh-ss0W8hyiJ9IA7ZIDBGi0RnEtNjYA-lPIL3Gn-SlNSUOKxwAzIJdAC_CRD6dOrUlwMGAiEIPTjvKZFvZvWB2wlV0uz6mjuwrtBEKRzL8jkMmOOC2np6Ydz36xfPWaNOhSCsQZNGVaXCiUD7y5bmEbUafYM7KmMfMCULyhMnoyxhCp_xSRNHGG6Q27SWTCixd6xSHT3BknvUKQZc09y2yhqC0Wa3NtHjVyXBHKK5wD0P6SEimY2k-fcEzj-Ddp9gLSEMZEiaOws2vMkqXmoKXiA-CAegJ6jh7vd0s35D8oy9-yjTo2Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴میلیون نفر در سنین فعال ازدواج مجرد هستند
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از دلیل تجرد خود برایمان بگویید.
🔹
برای حفظ حریم خصوصی، صدای شما تغییر داده می‌شود و هویت‌تان به‌صورت ناشناس باقی می‌ماند.
🔸
روایت کوتاه شما می‌تواند بازتابی از تجربه‌های متفاوت مخاطبان در این زمینه باشد
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/681470" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
فایننشال‌تایمز: تبعات جنگ به گردشگری ترکیه و قبرس رسید؛ هتل‌ها مجبور به کاهش قیمت شدند
🔹
فایننشال‌تایمز گزارش داد نگرانی مسافران از ادامه جنگ در منطقه، تقاضا برای سفر به ترکیه و قبرس را کاهش داده و برخی اقامتگاه‌های ساحلی را به ارائه تخفیف واداشته است. طبق این گزارش، قیمت اقامت در آنتالیا حدود ۵ درصد و در مناطق گردشگری استان موغلا تا ۸ درصد کاهش یافته و رزرو تابستانی ترکیه در یکی از آژانس‌های بزرگ بریتانیایی همچنان ۱۳ درصد کمتر از سال گذشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681467" target="_blank">📅 19:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYgMPRNVflzx1eqdq9GsL9LU-PcTzSVJZbc_v-gAqKooz-JgOXreNXja4OfMaCGA6rOLsgaccTMmSpRj-7mbyJEJnHChhxXJNAPUqXWdcJOQoofane3lUAXV4RG-3Kl_d6vSG6SyjVY0jqp5Qs0i2Bf_e_KPgAFsJVxqVodXy-NFY-92dMQxADrdHqrc6WKRrwm2jjgWmy9tNxVN4E6sQE6mzr-VsRXaaMi7zaeWSpI9S_W88uYbLvDocYBKUUCUML0zqkMVuexTnkb3hLb2_JmPJTWJHLVZBTPPysc3z96aR83TLYDR5Fn6HPXqkSmLFodobP-jr4ZyO5EokHR7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQIQpexUqvaYb9l7QwhPDviX06deBImfkH9KChCbxQsUBI8apUYL2SmBTk0P5tiStCCEoeea_oqRfheAzRBcdFX3_h_R4fAXJm-vSArt2F8fcp1iPrsLXcq883LuYm_bC6ijif0SLqQLlHpt_ttYTZsNh1NEaJV5db8rwcymMAI-c0lUX39G21XJRe1JuKwiSB3w9mnuAWx7fwRWMuHALIljlsuuOi3zt8LKXcl0ueNAhPaWZXfBgkCQOJpVpfHylVNi-5dN0y_CsYiic_ExilbDrPT2wOoIuNWKwuom3lF09bEVX4wthdpPHWwDK3rjKv-Xk0qr_DTIRP45adkPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELg2PdhhowxqpWLagK4RSSwY3GkrciLlao8j5CutoGjFa0wagcWjhbKV42T4IYuH_rk1cu54JvzIZdt4RCGKvANFTqhcyy9cKCdQLIMIXXDeo-v5_-m2ANkcVQNijH-iZ7bWpaAQO2r8c2EQIfts5lG5_CtE7IRrw4fx1ggQLro96lGkuvreqrpvgZbY5XwpmzhmyX1E00-U_JYl0-RKszxsa1zZu9saORu1-xMzWtzZfZC3EuXZqBxUV1RRr-89G1uug6auqvvzfNdvOMiw2_tb3_w3l5ZwxtgYahB0PfVqL1kyWPK8xLAay3u2nOLjvusyZfjI_afYbMl86JhJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hp2KMbQJ5NFpExkLb8GrKMPQSX02bq8pqJvOLYWw2T6PU9vOn9iA4NYhR-9Bcz4HepPUMF6C4lfNCAOoFMGC9FmvSexy-TGfsaUhGz88jdZoi6NoxwUIgo83SrwfGEXnUeWH8MoBRx5LEItN-BgZISNuKmmIed6cNU6PWIvhdleCnZXH1kd3PCjgZVcqhYp56YE2igTZVapwtqVc98cQK6NrYHQsts-hghUYQLIATJNhhGtRV2VH8hbi4exxfhoRXlp4UJi7gsSRQAC4HLKT-SRi-e-HsQuky6zeytEmP2nrH4zHUx2u583RG5T4f-tOBf1pZF2iudzHAs1g5Lyqkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر بخش از یخچال برای کدوم مواد غذایی مناسبه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681462" target="_blank">📅 19:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQX6YcZekz1Q8y-4_el3OZ9jrs7bWfi23rNEzJ2clLtEsHmSeyAVBo22qj3n4cqHvrtgqukI03-VZeiuTjtrzhZcYpubwaqd4a1i5pamRvVokUZaB9Mm9GajvZ3pddy1VgheisuJcMa8phOae_cnJQ--YHHSh_4WqgoB7O_DTY_fMvMSPgQz4GN-KnSOEHb5DjaBGxFZyqBWQQvwBKrdrkpPCRAozXaf2ZgBmQOI7B8Z6g_tJkBMVank-S0SPzi57ixUJ6e7IZ6DS-rIsyKgfQK-Qp8UfUFJCA6MyHYQh9zs08BzwffG0qrQ8Py0dUPP-XpNbSeEC0Po0mNtBREatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت‌های تازه از جنگ رمضان در فصل دوم «سرو، سپید، سرخ»
🔹
فصل دوم مجموعه نمایشی «سرو، سپید، سرخ» به تهیه‌کنندگی محمدرضا شفاه، محمدجواد موحد و آرش زینال‌خیری با ساختاری اپیزودیک، سراغ روایت‌های انسانی و کمتر دیده‌شده از جنگ رمضان رفته است.
🔹
در این فصل کارگردانانی چون حسین مهکام، دانش اقباشاوی، مریم اسمی‌خانی، امیر داسارگر، علیرضا صمدی، محسن بهاری، سیدمحمدرضا خردمندان، امیر ابیلی، علی طاهرفر و حمزه علیرضایی پشت دوربین رفته‌اند تا هر کدام با نگاه و زبان خود و در قالب داستان‌های مستقل، بخشی از روزهای جنگ رمضان را به تصویر بکشند.
🔹
این مجموعه محصول مشترک سازمان هنری رسانه‌ای اوج، سیمافیلم و مؤسسه فرهنگی هنری اندیشه شهید آوینی است.
🔹
«سرو، سپید، سرخ» از یکشنبه ۲۵ مرداد ماه
ر
وزهای فرد، ساعت ۲۲ روی آنتن شبکه یک سیما می‌رود.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681460" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT5PHl0I3ZEvCODWuPm10OlenbGTD91fX_0hyd3FQ98Acb57PEwr-seTC6heK0GcngJ1JpkJV-GJJw9Z0sk-tQBSF-CV-Q9hWuKuaB71_sY0tI5UIaFnbiftHZT1w7yb6LlvLE-GgjeCa3dtG2NmEHrjOOFFzf0Up0kk-4YyfH7ObXm5ePveE4AFHkkiSLdC3Iocm6tQd4EwBCxXBEsi_iOhHze_wsiNeJdev-glHEze8ygXeB5hmSIihd7M3O9DUTwqdsjirB5I33aT4cD812BHdg7ryk2GJ6glNV3bbZ7kYx2eWgGd5mfJBoffBSkJqECuN56wd1DeUgwBXIP9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: برخی از روحانیون ترجیح می‌دهند اسلام را فدای خودشان کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681459" target="_blank">📅 18:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469a082088.mp4?token=cIF_DGc-t6Yw57Hdc1MUq8RWH-lmJ4FZ5lh8g3oomUKuC8DD7xV_mx11ea7VTgwx4aHn1LejA7zZfV4oBnSrS0KHvDpk1ZA-eTWN_pdacSlwjhrwg-NiBa86fbvSBL8fYre4t7XK6tCol5YQ0JTQlP97E1O0N5SGvTsvo8yk1sdfyF7LIlzEvoZvcM4ISDyZxzPRgYWttLA7XP2XeZANW5TcL1ly_3aiwp3YNINK8ttxADnvvndAvB8lEeqwGtcCCXBSdrRS2MeNEOdQ4-I10g3hmQB_ldSh1PNNb6HdwDMEYWblCAU6K_qoaypnfrW8ffw5VTcElo-13xILxC4Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469a082088.mp4?token=cIF_DGc-t6Yw57Hdc1MUq8RWH-lmJ4FZ5lh8g3oomUKuC8DD7xV_mx11ea7VTgwx4aHn1LejA7zZfV4oBnSrS0KHvDpk1ZA-eTWN_pdacSlwjhrwg-NiBa86fbvSBL8fYre4t7XK6tCol5YQ0JTQlP97E1O0N5SGvTsvo8yk1sdfyF7LIlzEvoZvcM4ISDyZxzPRgYWttLA7XP2XeZANW5TcL1ly_3aiwp3YNINK8ttxADnvvndAvB8lEeqwGtcCCXBSdrRS2MeNEOdQ4-I10g3hmQB_ldSh1PNNb6HdwDMEYWblCAU6K_qoaypnfrW8ffw5VTcElo-13xILxC4Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان پنتاگون به انهدام ۲۴ پهپاد MQ-9 در جنگ
کارشناس پدافند هوایی سپاه:
🔹
طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/681458" target="_blank">📅 18:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681455">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681455" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور شبانۀ پلنگ نر در منطقۀ شکارممنوع کوه سفید دماوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/681454" target="_blank">📅 18:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
گاردین: انتقال مخفیانه ترامپ نشان‌دهنده نگرانی جدی واشنگتن از تهدید ادعایی ایران است
🔹
گاردین گزارش داد مقام‌های آمریکایی در اقدامی کم‌سابقه، ترامپ را در جریان سفر به ترکیه به‌طور مخفیانه از هواپیمای ریاست‌جمهوری خارج و با یک خودروی خدماتی منتقل کردند؛ اقدامی که به نوشته این رسانه، شدت نگرانی واشنگتن از تهدیدهای منتسب به ایران را نشان می‌دهد. با این حال، گاردین یادآور شده که مقام‌های آمریکایی تاکنون از کشف حمله‌ای در خاک آمریکا که مستقیماً به نهادهای امنیتی ایران مرتبط باشد، خبر نداده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/681446" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC02MBL9zlkh6fWZj6TnUYfI8mdKPKhuFiZ0facf03wUReJIpC12pAAZuXJCkWTt3gWfsI71pd5ss8JulSNB41-PIDC2Yl-gAJ9fPdxYbCrRn0ShY4Yk-MvJmBEGVzL_GVSRUmbAoabnSbSgce9tMyS1bd9yb0fiM0AyQnoMO_LIhiKY0gsLKRVDwyN54ClrKNu7-CqurchmVxY8DxLEBEWXYeTVNjCgbK4SLrGLTOh7KUlkkSDsYM9FZQXOmpaOswe38HHKxw53Sn-i-Ako5_m8JNOE-F4H4ax9dx_6gCVZn7Hz_Yfjipg53chTWOcES84yRYGLuiKmSBYYn19Iqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روندا؛ نگین درخشان اسپانیا که جسورانه بر لبه‌ یک دره ۱۲۰ متری ایستاده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681445" target="_blank">📅 18:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDeg6GGuEuXhpX_E-jkosvYlfjYzz8U_ID30aFjyeB-065LxXc8D-vvOyjZWOqCj1pW75Rx0mlne7nNrU1Ska--8wOFs_wMxGKzquhfPzxZdq7ma2MWUwV05NafvMDuVtyBmdjVcgVrC78T9t25EwSxe5U-X823kPXO0LvLkqh47SIOJRIBdR_qDp5oGp69RUVvSKAKGr3_FOzG9hXlqbsAQZH4TU5sza2PMZf7OVp9_Z00OKzemXgVMikkb8pDV2Gqv3D8kibs5kfQQQ8ANspksuLmlXnHfePaAgSKi5ePU3h0y0mjOPz0EvBvemOWjDnVW3e6N3XgmolNaQ9E0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندی که نامش با جبر، الگوریتم و پیشرفت علم درآمیخته است؛ خوارزمی
🔹
محمد بن موسی خوارزمی، از بزرگ‌ترین دانشمندان ایرانی، تنها یک ریاضی‌دان نبود؛ او از چهره‌های تأثیرگذار در ریاضیات، نجوم و جغرافیا بود. آثار خوارزمی نقش مهمی در گسترش علم جبر داشت و واژه…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/681444" target="_blank">📅 18:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6tQEtSk_8bhXPRjC1WksVHYeuHrfgQsipA9HjjKwyvQR0yvR1XY7SLC7ZkEBkcfp7cZND8oL245fVy_yjWxnZASKO9z6BzZf-4kS-W8Jd47H6lvSI8ja9OVZ9MYqBg8erW-W5i9dlG72Yaicz7hWwYXbxhMEW6Xmnw22Kw8BjIVHTf_sy5_-CIlV5nzcW9al4jmabl79it8OV6FnitwyAMG8OWTZf8SGGaUJKA_GCGFaRyyXVrRrepySYCXLxl0x1nCx33mK0DLyzBV5nYhD6VD5oXC5AP5kg7sV_fuchT1m69NQJDB6YwapV98RVJReOT7RhJ38q0q7-CAIeYBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-SsE3EK_frSKLgopMG2VdZ4Rq76IZzF0ed0RQHdBJx-0ChOt6Ch2FuvSfkpqQNOAIJZ0BLPgdhMvYlQ6zJlAsUfYXtMK6hci_1wIMLkLnjKLGAHmOIhRb1cVQEo756DARp3274n_-2_BqDRdVQ-lx4cQOosqTlpavvfGI27O9ERHs1IPdsndSruGiNcV2XSh5fQUn8HA6pKbaamNlLWeNnz7By9G6zw7g58q_Fb2CVeG9h-HhC6ct1UT62zCY49mhfAP6UbLAXqcEHUCodJNaJ25xSDmqJLDZXiHFdZovyeJPnHO_4cSch289mtQ1Sv9O9wYLJtpN8JibFPZF5CMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آدیداس و دیزنی کتونی راپونزل طراحی کردند؛ سه‌خط‌ها پرنسسی شدند!
👟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681442" target="_blank">📅 18:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoyHmQ9DHh-aTQZAUnhTuU7YcWHxik4PSLGHmnTqkNOCpc3MIfydrJ86QKyF7ptQ-XcF_XVFblONC-F6eA9uMraXedkcOYgJvUE5N9EdDY47LGRBGK7L1puRSfvdsuMcsp8XmXQNKG-ycBpsBLsJIeS9JJMNODqSNtwoi_7-EvKevzIGXBpq36cCyRUwbl4nxUAwXzQ9Y7H16XV1RopxbIbCo1jWnINeAt60N6fci9hY1f6TPogEXLUNQFZFlgh_W6VsMMTDbemhFyo8eUNgNTb3N6gHILl5Uz5lt-O8oz69-id0jJHpGapsvARAy8YbPscStWx42LN0NJms_ho0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر خطر کرد
🔹
ستاد کل نیروهای مسلح امروز اعلام کرد که ۳ خلبان ایرانی پس از سقوط سوخو-۲۴ در حملات اسفندماه، ۶ ماه است در اسارت نیروهای قطری هستند و اجازه تماس با خانواده را ندارند. اعلام این خبر با واکنش‌های تند و تیزی همراه بوده است. مسئولان ایرانی باید با لحنی صریح و قاطع، خواستار آزادی فوری این افراد و فراهم‌شدن امکان تماس آنان با خانواده‌ها و نمایندگان ایران شوند. دوحه باید بداند که ادامه بازداشت بدون توضیح روشن و دسترسی قانونی، تبعات جدی سیاسی و دیپلماتیک برای روابط دو کشور خواهد داشت. قطر نباید جایگاه خود را به‌عنوان میانجی منطقه‌ای با چنین رفتاری خدشه‌دار کند. اکنون زمان اقدام است؛ خلبانان ایرانی باید فوراً آزاد شوند، در غیر این صورت ایران حق خود را برای اتخاذ اقدامات متناسب و قانونی محفوظ بداند.
🔹
هشتصدوسی‌‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681440" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو تله مالی پنهان که هر روز تو رو فقیر تر میکنه! #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/681439" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اسکن مغزی؛ سگ‌ها احساسات چهره انسان را تشخیص می‌دهند
🦮
🔹
پژوهشگران دانشگاه وین دریافتند مغز سگ‌ها می‌تواند احساسات مختلف چهره انسان، از جمله ترس، خشم و غم را از یکدیگر تشخیص دهد؛ چهره‌های شاد نیز مرکز پاداش مغز سگ‌ها را فعال می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/681438" target="_blank">📅 17:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آمریکا هزینه جنگ را از طریق متحدان عربی خود جبران می‌کند
جلالی‌زاده، فعال سیاسی اصلاح‌طلب:
🔹
ایران بیشترین آسیب را از چرخه جنگ، آتش‌بس و مذاکره دیده است. صادرات و واردات ایران دچار آسیب شده و آمریکا به هر صورت با هم‌پیمانی با کشورهای عربی، زیان خود را جبران می‌کند.
🔹
مسئولان کشور برای پایان دادن به این زیان، باید اهرم مذاکره را جدی بگیرند./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681437" target="_blank">📅 17:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIvSF91aoxRvFSI2W30AfieA1oin4sQgGtQdQ4UOhorJMcPUW6owQh8FXEYQDsnkAAPQTszO-R6B9i1KQ5OdXlrN60QmUzRzmfMNJMmYkv_69XM4PCqimu0K_zBKrsj5gtMVuAAJ9yDyhEkDQlaiDodJUhnkhM5y357OAWb7FAObsJ9ufRuize4YS3uFilUUoZItborX8sf1Ul-Sy_1ekHPABJJlkP1t4m3SwDdgbaySwaYPSAfZOOu6zdj1xhoDEV6rphfHnDL2KwBjklTOazlgp_NePuDWopOF9-SvdfcH4CiIvJk-_OsBJ7URxleLml22_tozjzAzoMmLcV-FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/681436" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار نیست هر چیزی که در اینستاگرام ترند شد، تبدیل بشه به معیار زیبایی ما!
🔹
این روزها بعضی دخترها از سن خیلی کم سراغ عمل‌های زیبایی میرن؛ چون مدام با صورت‌های فیلترشده و استانداردهای غیرواقعی مقایسه می‌شن.
🔹
شاید بد نباشه گاهی به جای پرسیدن «چی رو توی صورتم…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681433" target="_blank">📅 17:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEyOXclgbvIKqU47mcNnAZp0rnrPLSYgJtkftL0K0gaeVTZPcODnCaz3IeDpDbb2XnIOkF6_wsSnMR8DIve_AAYdH9l23KhAvyA9yADeITrgtS0kjydKfDeJnnAUQGBA2OiueLQeOOm--AHvBBBhycSe-HXwR0VLkwUR21BZtCQzll7LRNg-cyuf9HySmTGGWKhh-Ji9FaK5VcBfUuQ7HvZCxGXUtGuWt3zD9EgLkYhb7U7UM_h-bixVr2-yUuIqqytvaUdKiXdjobta1kh8OZGqw230aY52NQ9UmAb5jyj_0VwDIwspQ91mz8fH-T3s_UFbJqNv9TIlTqOfaHberw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترنج ۱۰۰ همتی شد...
🟢
دارایی تحت مدیریت ترنج از مرز ۱۰۰ هزار میلیارد تومان عبور کرد. نقطه‌ای مهم در مسیری که با اعتماد آغاز شده و با مسئولیت ادامه پیدا می‌کند.
🟢
برای ما، بزرگ‌تر شدن یعنی مسئولیت بیشتر؛ برای تصمیم‌های دقیق‌تر، مدیریت حرفه‌ای‌تر و خلق ارزش پایدارتر.
🔵
ترنج؛ ۱۰۰ همت اعتماد
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/681432" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU64dRK9SnBqLXsnRsmjzvASJdzUEFUEz_CC0kUKSxts3oJ6v0IznC3UhzIEI-qdd8J1Xp8Ko6gGMxXKBT9hkXn-HNMSIxisa7bv9s9auHyMLA1CC6bJBgI5XCwuq3SxpoQjmvI7ZyAzsg2MOakxhTnCXoTn8IYwxvnPfJkhAsvaP68eaCBC96fKElc_-t-3J51J8aOntBFXMZVbxSn8hmcBHh8At0L2EaW_mEMAlryiUhY6PKzrEGci1oq21cSZwbuV0q1M7ebSKr40i9INzWfajeJswuXopdy4qN_Y3tvzGcSnAA4CgpU5grKby3N3U2XNMUChHi8NhRxgoDmZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدت دریافت بیمه بیکاری بر اساس سابقه و تأهل
🔹
به افرادی که ۶ تا ۲۴ ماه سابقه پرداخت بیمه دارند، در صورت مجرد بودن ۶ ماه و در صورت متأهل بودن ۱۲ ماه بیمه بیکاری تعلق می‌گیرد.
🔹
همچنین برای افراد با سابقه بیش از ۲۴۱ ماه، این مدت ۳۶ ماه برای مجردین و ۵۰ ماه برای متأهلین در نظر گرفته شده است.
@amarfact</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681431" target="_blank">📅 17:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نادر سلیمانی: رضا عطاران در دوران ممنوع‌الکاری پفک می‌فروخت و در سیرک کار می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/681430" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنجاقک؛ خلبان ماهر طبیعت با قابلیت پرواز به عقب
🔹
سنجاقک‌ها می‌توانند هر چهار بال خود را به‌صورت جداگانه کنترل کنند؛ قابلیتی که به آن‌ها امکان می‌دهد درجا معلق بمانند، ناگهان تغییر جهت دهند و حتی به عقب پرواز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/681428" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ذخایر جهانی نفت تا چه مدت می‌توانند جنگ طولانی ایران را تحمل کنند؟
نیوز دات کام استرالیا:
🔹
اختلال در عرضه نفت ناشی از جنگ، حدود
۲.۶ میلیارد بشکه
از عرضه جهانی را از بین برده و نگرانی‌ها درباره دوام ذخایر اضطراری را افزایش داده است.
🔹
برآوردها نشان می‌دهد ذخایر دولتی کشورهای عضو آژانس بین‌المللی انرژی، با کسری فعلی عرضه، حدود
۱۸۰ روز
دوام می‌آورد؛ در حالی که بخشی از ذخایر راهبردی آمریکا نیز به‌دلیل مشکلات زیرساختی قابل استفاده فوری نیست.
🔹
این وضعیت نشان می‌دهد طولانی شدن درگیری با ایران می‌تواند فشار قابل‌توجهی بر بازار جهانی انرژی و توان کشورهای غربی برای جبران کمبود نفت وارد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/681427" target="_blank">📅 16:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز از دید شاهد
👀
🔹
انهدام یک ایستگاه توزیع گاز در منطقه چرنیهیف اوکراین توسط پهپادهای انتحاری گران (نسخه روسی پهپادهای انتحاری شاهد۱۳۶).
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/681425" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681423">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpmZfHKOxXfmZPWwut5AEP7hMMaVwHbvePazPf9uMqTxdI5fqlw0O_7GUeAYHi_GhNwhOivr-o1e-aY77J5fvF9zA5xgZ9S9viJUwMO6BnNErf3iwrZW72CLvAMKAkpZ2AqWxeII6kzoxOPrl10GcAZh7NDbqk995hjTSwUxTL87oQ-0RhAFGDtO0Lc-AnKLqJhk28vdq-3O32m_hGIWQDgwytcqs54fseEM3_eSCT4sCHK5vYlMVxlJzUymt04Bsxo-eUwAAAsyoeLrqCWf91A5UcSpMIlJAnsrLNFY2_AQ_CS10gruBdZWn0VQgj1xp0DzuIB13gCRSNPf5UPz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/681423" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681422">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpzK9rPl3SMwGIbuNi31drlJwFNPTtosJ4zsBUJa2PxX0NbzB-stX27ZSQUNbAvgVxy3_Fh5jUYgfN_09oAfETVdPeWsEatpnjinQ6SvThXAbG2vq0DmUB-tp19G0QIHC9fdxTHK37OFQ4dFUCWTW32JJBdToyN3xFFGzUnTDpWvqj6r2-9UCYRnIeaIMjv8-fTMWb7SyHf2kWfHzT5K8It7jpWfdXw12lHr4sdOBHM2HBRiwixxMNbN84tmu27-1p_tzY-Kf74zCEZ6ieT6FWtULBUWQnTL8ZtZyE_KHzlGe7OPRoc-mRQeOLwdgNGGQlwOmjsZ95ClpxQKZcLTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: تلاش آمریکا برای ورود اتریش و یونان به پرونده ایران
آسوشیتدپرس:
🔹
با متوقف شدن روند مذاکرات میان ایران و آمریکا، دولت ایالات متحده تلاش‌های دیپلماتیک خود را گسترش داده و از ظرفیت کشورهایی مانند اتریش و یونان برای کاهش تنش‌ها و بازگرداندن طرفین به میز مذاکره استفاده می‌کند.
🔹
رایزنی‌های اخیر مقام‌های آمریکایی با وزرای خارجه اتریش و یونان و تماس‌های بعدی این دو کشور با وزیر خارجه ایران، می‌تواند نشانه‌ای از تلاش تازه برای شکستن بن‌بست دیپلماتیک باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/681422" target="_blank">📅 16:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681421">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بقایی: توافق بر سر نقشه تردد کشتیرانی در تنگه هرمز حاصل شده است
سخنگوی وزارت امور خارجه:
🔹
با وجود کارشکنی‌های آمریکا، گفت‌و‌گو‌های ایران و عمان روندی رو به جلو و مثبتی داشته و توافق بر سر نقشه تردد کشتیرانی حاصل شده است.
🔹
این اقدام حاصل یک همکاری جمعی بین‌دستگاهی با محوریت وزارت امور خارجه و مشارکت فعال بخش‌های دفاعی، امنیتی و زیست‌محیطی کشور بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/681421" target="_blank">📅 16:18 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
