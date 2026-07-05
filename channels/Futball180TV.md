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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 638K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 04:45:03</div>
<hr>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efwdKA5DsSxMOFPuA3uA3_zyp_Hi9dRQpuXnVABTWZgRbQcK_nQr3lk4glQcRfAgYocrxQ1gtWQvMeC6MR5BZEuyqDsy0BDVkqm_GUnaRxe0gKt6L4jcCxlwsYx3zCJO-cHIcIUCqwQaVCoELnbMhfJHBgt_Q8va6wMRbUTkb-C8212KHwnRNk-ReqaeZuUKx8oeqSLDzJMAdwIzCPYSeXYTi9BidLosBY5Ur2BwdZeCqUL2WlOU-w8RSakJSXkt4L3r3d_h4K0KVjh5gDaB_i9udhH9iIX7jPazkYkzBs1X-dd_NOZP1ptw2XYHdGVspIUGcqfbuF-SO-4jimdteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrP0KP8bI5XfS_CyCMe5nK-sq1yYZCdg34bSqlaJpKAuJzTfdbLGPmbyIoHDX4DVZ6Iy41G_Bh_dtKKXUa174wCJtGHXLxHqj6Abvx2FnAv5R-J5SDFqkBcrrUtOiy3T1a818fm5fLnNgbSG9sMGuklj-Hjc5vmJEeUGjXFsUa5e15J0G1zJhMRthCg7e87BgEWwsJh-Km6zhvVwQzmSGT61yiJkA4QXp4SOtnZQwk6KpnKjPZy1t1kWorzgPumRRmcA7kCO2VHZZgk_HdQu2XCYAPr9NRAX67x_k2afRgpXdFKwdciYc_R3xuYdcD3Df-gmhlsYjRsEQ0cfzRzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wbEydqJJ3J3ChwWlMAA8o5H8lrwE5lCCwOAgWETRKmIr23tgmGReVaFltGDuDTZkZ-AOIXFtARAnhIJ6TJZuiUMIdAQW9pJoPprUnFzEXYNerx9SDiWRJBoUMeWjMu6wx6iYxhVpIwJshi-u4HbKhgTnhL_m6unMduFHQFTdSGhlqURUtHrup6LGWOsHctjFTC-lzLQmRTPoZT_MP_ALvc3wXI1598Qs2gC5xRQ8lIGMObUVqS7mb-9Ti5NJGpHiPC8KoBCmJ56obbuX21O-QZUIZw4FSj-Acl9rpMouL4v2LmrTHe1Bes4PpIqG8uDOgzaBN3C2MjyYhp5usgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUQgbwUbB6_83TDEUElC3k450HHRppv56eWYxi6yWz0VaEu0pI0Hd8Smvh03jcGhMkNwgIipwlqUwGSKb97pQooakAn-tKFl_T-gAOwBco_IKhXCJTQe5oAylbnB3PlPTD1BQ4YruhfmIOo-hBt-syuTxXyKQruDaqYH9GkCN2OTXrCn-Vh0rRY9k5-0SQlBIJ2amk1RDJgVP4LFLZ4pABr__RLpyoI0Qnwgu-mKpPoya-VisFJrdwntxCHGRn3y5UjpT1OKxbiW_APMjfDsCENTpjBFOys0FxmaFJ7lqbI6Pcukw0CAd9FSJqNihPcsFldBwDxvfPPY26Pn6kaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIA_X5Pb3Hll4BPS9yBquyeKixhZXZkgGjxJ7qd-HtwbPwqPpuhiocZX9xMsyQgPdJ83bPbBRJMonvFLpDxGzNCfarTPFKVJtaugdvQF_t-CfcNeef3d_cFvzn5UlDHJhUFJIvfPAymrhCELZiz-Q_qfSApF094CJu-mihG5LQzAS3GpgQxaHNzshTKcFPDITH_yvueHwn-rL9tAqwuoh1ZhkNFM0t1ZmlGp7jTgqFkniDRrTiOYPJJEM4XchSnic69st_1nolUynMvnC_UQfswnAuXDPswk1oNbHsSOkS2nSLBLUYHqSLX2z9k4RdbjG5Uf5TC6Bb3DtDasUYoiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KLyuThRYnNqoUwjenJBOclYzA3NAlfkpyO0BemSegRDgNazJhEkhiVUjLjKsuhkUEG4I_rCbY7gwGO68jF5T7-0VHouelgjgEjP8NbEv_zw9wDXq76_bCNKbenYoC9OT8LylLNd2Tw6zwXadC1lFtD697WbplPg5wH6G4vUU7N1GHaSzYUhErb4krBGwyGcOpAS22kEoZWxZa2vXMyt39zKUqJ5T-Y1VfhWyxfIbdT1b4ekkjwLv2KT8iEcFYK2nMKxH0O3SfiyFONsmjpS9Yi9RR4N8gUOU7NJHlBLCKuMau6V-lGbG3ESBL8cHaPjvMBIp08c_9vMwaqOkj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiKEu8PHllL7zOPfpRWVnzuhuhI-m5_0uTqNxckwfaiuICBjDxDE7c7A0SC0o22VtgV5HSL_QuMXtqlZtl5aGtp2UGWOF2aUr6vzR-M01Cvund3_0gUYw_by-FXh_6iozBjZfe6_IcxxUMOZcwX6OFAEpOFgeLNecFvxEooA4BfG-ZslqO1flGAt4GKKESVlKpcLRFTEjUOmM7PtmOG01q-_eMZVRCVAifhiv0eHEHiZCqV-i6RjYJjESkWVhry4fb_FLZeXkqRTfU2392mCfZSxfrHS4AsRwkYvXTgj71CEhkTqA_l8jJEczY2e82Iqham_shnundZKVmA6_E83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTLRXRVArKWiN0mtN2XsDrRmqRvIadihgDyiumINFVQInUZwLlrDqouzUgMBkeODVx2PWeV75f1Nn8_0zaUvs4tEFh-tAu-Uuy8xaoQfShCQetM2K0c2Wy8ii5PVClnf4qpEK6AbP8Eo4GVSTh1JqOv9q_XfxBecJUXrcfDp77XiUQRFKtIzrjdetjAwJOsg4VwcnzwoDp0meX2maOJGigl-BSI734wcvNbNEcDWHSuFGEjQ3L2ya_330qTSnbKJXMuHaCJXVTsy0v-leqMqGSg5hc2K8Vs1qlnlu5D1q8JPxTVvRMRpJ2jwPkEEN5V3SnGE5C_VLs71gMa_mhTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDATdFfoK4bUHhB1CMnwXK4NCmphtiP8VNZcnuLuMjcpuXs3eNi8PV4O3FwdcIrSbZe2VeE4RPRs42H0smVxYdGjKh3VBaMic-vhprGGxKfwlucVe-k0Iktj5hyN2akULUId8mUCgZfZHnKuRrbTyrH49EDlRnjyiPt3nYh70QuVsOMDZCTj5H0Z2Yi0x518MY8j7F6Lq-yfCNaolKMDYJuXxkq0kPqTCG6Cq2KPh_WiQcktvd11VOambA_kVQiBdYOzx2RQKwNMDsHWgp5pLqbSfe1QuLX1rgBCQbBgc4ds44I7asBbsdTtT3OcRH150ZOYOQhrG5U7V0PgEUmTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2PzxJE6NY42U1ocHU8T1bjS8eBc96OdyZgVwSVsM5_MjYcKlVl-gGFkdy-iZuYUciXtx6onojYcy7FR5BR_XTjN-6EkRcIkr2zPXSgZp2H1Jxm4xgQVNK79RKQTRLY-YSVxmdj-LPP1f6AICvhcGZDQaWO559-y6ZPYCDwQt86E4fyqLFopTqTCUmWdaz-ad8U1nlkptDLTs5XiS0e02kbvg7NqZURJPfE1C6Kf5wgpsUu95_tx39DWTYHmBQFc6m98G1xZirHXfUF8lIhl_eRh60XTAUuBxkXIc5BeRhOCIT4RvCYSxv-j2E_E9fCKhC6uTc61nNqtea8soGKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX5D2eNDu3JUsshuhQ6qG2S0Hm0w4XXYICebi9CQLYgtCZBn32q-_try4yKloIhBg_hZzoFU6JD_dLips-UOXPIsLUUyLqNbliMW5-fKOnXpkLTz_Zj8kUso8NJ8dQPvkUC4zerGB7sIVR36syjegcDnzBPbHoMCmkNbFc7bdXH91FQPd-OWrrp8d--ZNMrcYtSVTCXWulbZt3WAURtHc5d_9cBNxrg3cmQ990h1drtTJQ_3hQH9ADP42bwSwznS-SYA4YFGCW8IJakqDJ5UE0Klm0Ej4ckVdeFrer30b8HB-VWKFOu9ehNwSLPjbhp4I8A4J_VHQfPjN9TRG72BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcQxZ0p4L3rW8nCSnRCwBoJ0gz-cuR3WnRhgTsOu3WdzqRGO0g2r8dERoBRBta_cZpA_4Tc-Y_rfI56lBDivj6J1UujnkndH7ZyUCimR9pg-abOidzhKwzYThRUHAbEDSnvnHoGofRtsnOkWTYObDD53XMBfeuSHITCsVVadRqfkGbsxeyFTKTZls2U2GIp3X_mcJojM354RZxsCELqCPL4Nzf58gWhg1TdHa6lGcx2VWHWQzb663_gR_KqomTVoJ_U_qvcIHjubhYKv5alKe-uh6C1ZI9ZkcRFifsxDvN_de3fYdbSgREeDYS4GEl--3TfgtiZWEnf4ADedxk0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwnS_yr0tTWQwrZWn4F7ZpooAqZMgHjlf1HMULYoAAAlLPTYzHoNlN6kO4C6huaeKUYdnSzMndK_A8fewmv9YXz3ODr7u_GqaXDpd4POkQPzTAp6mt6Rp6eTqta-rO32H1YvFcrjCjaYl-bBxj76SUJIEm48csBQQwSSVaYZ0wXP7lnDnlsF7AbAMe5DvNSqzCL6OPoPF_cL1cXUnDYrQaeckWD60rqRqaClplvcFra8CkY3qwJilaJmCXctr1bxj-4qaZGlmqTBN6Xi0kjC9mO2uh9jBYTVf7tJGIqoIVcqJ4tw0Jbue6NowSUKw8T0KeCIig_JCPfyTAGsf7xv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKg6lEoMEXiXjd2rp_oliuFt8PyoMXCD6yA_Km3GExPnNU5HntOtbhNIIsFBeyPPLPhvadX5HAGRsEq1zTBVgodc_3kbTR346D5B5oadeDsS6In3cAoUtAfeF2DlmIUR2n_m-j9T1JDVedG1AG6Poso391yo_ieobtd3kA8vXdw4Z01fE0TcEit-mcqZeeaFuXdDjSq3NIXJWuYWboJtJsXCd2vCsWdvLLrYAREEHujOpIKbSbNPZAVNEcwk84A-_4z_yZbxbbgLXoRxqEfbmFsCe3u1SAb8GhIv5U2iKtEx_EbKbx-WyjdG6XUj3-VnToAbIoQKdRELOKnjItRTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKfZmp3U50RXITh7KP46uourlmoe68kL9dspzgUswiJoy7FI1LiEwXk3kBHAqk116TWMkiCay0JOJWehuUdgc6aEi1sOtZzBSgBQnfrKGjIHelL8VN_yrAJNgqxJBp81L6Svma8aWsxWwasAm6xcY0DvzvMvr2Q4iQOC1LFrS3GmrbVGreUf2-VKdxdqQ3b8qAX1XlEU_2REsLl1CgDjgQgZj5W7sX07mM2RZ3PPH4eMr8PGEaGyyB17-ewe5IoZOgmag04oMY75FXlLcc8BYeO16FQnzfpKbJQgQMdZWPYqNNAPrRZhMMUURFOW91_w2KFOhBgEhJybJDrd0711w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_O9lBFcc-pUrH7035w92qiEZtKSl_MK10EgM1PccnFpbmzG08iQxlFY92YIG7c7fj9N9mU-AjzD8eSVuu1cTv_2Od4wXB9a8JJIUiPEUsmFQZ-jW0wAzgwm7Cs0FbTpd8YFt0bX5hdIe7lZnIPNNgtDNax8g-bpssyF7E9rJg20NQ5owcTStMZdyFIeqQtifoaRGwOYr7NPRY8zuJoJnRSKny4VY1UIKmasV1gf_O5heFK8qWlyRtLV5kpxiwZkDyH2RF4Q3qzuwa5J2vzhuwRBqp5d2dxjb4amiOssiQ_cK1wZpJKFi9HvX7lxO9nX4vmGF2QlJXhVbJKWEGF0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFbDDx2vKT2NfF51Ddul0fCH7SPyia356kBP-t743TP4e8Lp04RzbphbXpGkE0v6jtg4jZmIpo7K2RvFm3pUNGcV2H5Su3WaB4SJCYmrgWYTW2pVygQ-LffHssN2SIyphKBSNB5mo4k8WaCLx69-H5SVu03toRnjXh7F561y2MfGrkBnK7F8i5zU5su9FhigCT7BkyTixAGUPkVn4ijj__6JavJ8u1nDFrFW7JpXoqTFB0Cy_5mOMzJmmD3hXsAWc5uWpMmPatPh2Bm-dZUKzilUO23H1PyLKgoKL8lF3HJCbzt0gD-AyWjO7uIqvnMLuiUHIgC8T5B2pitAsgn1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpANK-LJclw1xliaGxDotT1k6JJGChDBYSU_p5kDiRjCYK7UAbsQRFj3lEUMNVityZ8z5CLpecagfAl8nWbrs-jplF3icy82-LynLby9kPpGvgmC8hRQiC8s6XfwRIPCZI7WAMjzYJ3cwLsC-855hXEL7n_n8UJlkoAE02frSn9F1H25I9PUKL3gvSnv9SQY9uYh-VyqigsnvQZE3PKLp_WDm0EXAcobtvd1rScm44uYSIumedg6eBXBP9PJ1juJyzASc3MBKiKgWAIvXFNUyYqrPtxBpRf3IaKV5SPAsU35BMoCl7UIbBb2AgfdU7LrDTzJFAIm2VeXSn3hZ6BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkX1Ug81x9d7PciDJ6BTNu_PuSvUZ3cC_Tr7yS_1e73JVOW4Wl3a0WjyNiEGhQp_e513MowkN2LeuvuqZbPZh6zX5UuFSyeBfIKWSCal75PgOarRCX69XiUD12L2Lsj0HeEy3ymeUHgvLm0ER7a_06oTJXB5Oe4pKXyXM1etkNd5WCAIdDH6JeSeXrgJF4Ue1E7F4bnzcN4GOsVtY_nLUb7Llib4i3wNvyubeE7QUkAuvg28m6_dtc51IaW25ZtP8JljIT_oDh_KVzjl2P3I62xR9ZTeGHhpkUyKgeyWNsvM3QTFealLkwXaQ0Jx3B6vFA-QXNEYd55d3GJfNbcylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YaE6mqdRcKdbre8wdidYib8SR_BrHIO492312UIp3TVU9Xb_C4_0vq_34JVUoNi6i0C3XiFuxwmuze_TZ-EEC5c89ZQS0GL9DP8lFFiqnBH3WiURKNFML0cWnjVOM7MpS22laGSmn-R6zZ1uCd-8REJqxTQGL-Cox8qNnS6XhzQR2bBeqcr2zItTEXg_ycdf36hYMQ-VO7jE6dpgGaKaLgi3LTa6zLpMIzXJ69kkV8TE_53zfOWrjAXegdKL9huHjfku899ze6r1D0XwJZ-VP468XGkj75cDn6kHJv_TPQjJlJuZc2kLN0OxkUtqRSS-pWIdp2pAsbVYYDRCTUOhsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auhXF4FkNPemVB10LZl3UH4rdsoZFFxX-cNtza2vq-VaHiC1lbS338qj5kHb_HOZctrXQDVAuQrPqA9xLkUBc-oBbTT9mcdkMIalZwVojYYerhokKSMAz5__YCJqgZ-jMBqkIWVu66OknI5Ke8Qro0e7N3ZhSZkQv9CmIFh_Nt-ZJRDwDLq_PX2UYoN4au2LAPb1tn2__Wslt5na2wf8u4REp88R4L0bvST5jEncqV3nj1PTqKM2MSp_B-cruAgKbOncnTFee8itquTfva4wvm95eFH2FODmChsCZOb4D1-OTONwLAzXVDqdVuXAWcKlyrzOv4-lzTlztCyqOZaiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBxZSg1gsSe7A62v4__tpWjeaRWGoYMgTA13wcuRGd8H4MoZRIM9qkA0hfrIS_b5JTMD4jCG5VPzy2jDOurOV_76lb4keYmcYb5SfbAJdOmDihTv4pBEBcBF3FNlXJsovvk2bz-wAN0Pe5iKN13vvhFoSZlPdgKxvtLPolwL-vrZo7sPYfAM7z8FBgVScXPuAxySVogiZmj1ESH8U0Wv462Geu-s-TVci1d8l-wgaMJbMLgh1LBP4kg4SodM8X40jNkBCjG9GR8yrGD9gRrlG07ZZQr5QiFMUn7IGrOKdLO7YD5lAnK8ltChbw0lDuDKGf2x6wIymYirZmPI-Fw4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbfzw4yk-h9SVyLfaOX759i8Zg6SPz2-frZq3AkP7TJ_xxInDszHnT7PsvqY77xySZ0FXrCq0RmXi7sWu3AYL-5sxQTDACiotPYeaEg3PgE4GINJ9TFfwN8SdI55RMNd9nb0PHprSJvdI8ON6qf5buE1p1ZfYOC1O9mQYTlycnViIZO700VNucE1c-Y6OBDg43HEww6k8Njs4EltiHIF98POAGrNEFwKXeD3RDOh0gwKUwET4nHsCw0-Gag3Y681uzpsNPPGB8rkgi21kYC22VNHNEehB98mLvFDioTN9gQHvPKsyGAwHTEUICbF65_oGbH2BUB4uy7Q7XSONvaDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLV2WODLloKgns6GcmtV51s7OodlsbBGV-_cbOyZ2aZJCi75cRlf44cKGAVl55TYDDyAEh8etC8QYuF_8yC9EpVzrYZ8IrJZdhzQViDQx5zhDy16u-o7_gEWvNy3YnMBbyFFnu5Chp2qSCCABrmLLBlgymeLFGKcP916CunODHDw9knEy6mZbPElpqU8oEJ_nGnHHo3A-UYHYqcFQjfCYndqM1DbB61EQi8pJX302zsvz_W6dn6JLQr-tkKHypYaHQLxbf5uzQ6BuOcUXTqOJoKPItRyt2klZD4jc0hz6qaus9sP14J4uLmKRtzewmW6H4JWD5fgfxZo8X6RCif60w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmM5vL40pfpXixOUJ3VBOLAhVo5yN-Oev6i1TFMYjEznR2T_d0Oib0MaSqP50OdtQeO2GXdbYKD2zaSEdGZMck-rlAyBJ3Lo5PoYZq3MdfjVkOgR9e1DWIFZMYfrDb4l8BqVEdvVHraldpTyKURhEOLbFb-NAJt8iqbZV64xq7PzFLmcp5c8MaHOnBgqCxk6p4O67gKVu-ktt6TJvirYMLOpZURDC8yKNYBBFg9ZKx7fm-vdryWvgbnwxSC6O7g1IJEhlv2JSRjqOQSoGK3EFHalpjETDEPWHKBbXoQDaRbxBlLnoQQnfLAuV6abHJ1eGJ9lj7eqKMfu_fnlFM5HfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCOw2NIcp7F4jiOAGjN_BwgylMo1edYhDtzeLOxkmsyKsU59xevZJcnbqCaLnpKmZxkSBFpIBYYXQRySRpnAoFmYx63N92dSEKkTP44PQWxsbEHA9-xx4OFwLiWWoSLlSkZFzSLORjnuoyXn63wEXZkaLDsscW5vESuVbj_qBC4EtglTZqZ1obu1X7DAl3bQb8Feh5K63waW2rh_2ZOUZZ_m-xiB4TBoM0_8auepEyT7TRjIzJRwt9sbXLvbsweezvnTQKOXMY_kCIt2pWGBNDuXSWn4inP4uAayE7l0raSymDndpVDPl6IxbPsct4RaOPs-cq6Zs8msAVhG7iJIFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGi_3QVkHeLiOLng1USQ47LhoZowRSfePKKyzu8vEcckbpBx0Lo6xOILk4tf3R-FFYDa3IJFJsrHzQhIoIWyCDEvKgG54NdISvHU_G8dCGIA9P2j1kh8-VkKJvcDeH0H7AR5boygucp-q2c4Qobmj4cozhRZORVHqJ_29hhuy8RYHlk4fy8qnqJemy51lvULiK_kTbeMz7IGE_-_YEUDHVU9phXde0cDqNueBEYlrOtLhrH5PmW52rMK8JU1SiK8h0FsyDuINAv0g8uRcB_Dv92Yc4FfugYVv2ukJ48WE0nMoSFUPz6nWLKYSMZWVYu__goK7BvBELnxoEAkvpU4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTm7_jzuwx9uPZavbVSfYRPWlwsijsOW0sAflhoRig15xTM0H1u767UTOFzKATzRGUWolg-ZBQpkAkkYciskxX8oVnqk-O0NJwNr-QBAm5tO871BXcpJoOSus9GsXb8VGbcIWe9j9EnBJz2CTBNfTupxQHdtfYEcdhSxYMmlRwPW5iHN72fs1qlWSN6sb0pD_AF8W_KOaLK77fJYbRgDOtznwlt0ES0ymlLRUrTLA6TvebKg9d-g77_sB5xFvAsBsBhtTleqN5Ab-W43c3SfYPk9-v4tstdYakTNXJF9xohb0As8Qx0cNI2vEZIpfIU1rILmDY35dxGCShQI3QwGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYLIO2-8u_sPGiG9KarkZsHvVG0m9pv3V5-zav_qbVfNWLFsFLxVm4o5L3KCdLjGbr7fo2xeJY5vYEIf8BiaHXRbiPtabv2tuLXnCalUTLWhoeqTzHJVlm83uvU28-2_WFzUFSHTI4lK4axnCNqyrJRWsEGN2lgO8T9w2nrf2Xj2xi9nWGHSJzxXy9IdKq4c76ZdJW1djxIFCAY5ykrgf8NAgBy1nwaQ9xgeN2PZT70kyuwi5wH8H-HGTU4jT8mK7zFK6F-Z3WI-FEDBfL2D1mwbYwIulRdIVBIFThj2XXhND1wfxwyw09K1E0Br_AKB8PAiO1H2J-_Fo9ec4jDVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQK3u5HUxniqGJSw7HCmToLfP0W3bzPH64lL0ADVNSMoMS4gr8sqokHWXx3tdcRIt768Aepc3KvYnPgQS_7_fA8LZfeq9baXPxvoRosPeKEUI9-Pc0EDHzQNuuTqI46LU9PEKRk9WcdK2Fo8ls4Jpm4AhvEaUxxceW0miMuAYpxv5486II8eLXyoQJxeS-Bt-e4a_nUz3U7Akd9pFegsFbgowWkRO9d_uLucr7G1tHSjIEpCx5-TtG23DlqH_7SdyCMA5epqKmAswSNeGU8SqYT3E0GBVtM9VlKJLtP8yB3a1Xe4XIkta62w34BKbn_O0WWM6yGQpWGiW7QRUeRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdtnKQe6FL3oGEByMDJ3tRwClpJJIdfcL1Chy8YN68ICfRTloG70obCJOxvCq0KOO3aEr5xm855ymYzW7J5MtAx9ufhsnipvwmlDU0c_flcio3OYr2Z5otFhnrfLZomZAo5vlXBTuSyUe_J1_GB1nPNzh6wZaC_PxbiLOA4tcdslv0ri-Uo2hFt8YEKvoW_Zl7JVthk9CsRyMG65jHBWuai8RYRtpYOclv9v96maFr7s-ArCCufh7oj8skwPHBxyjp_GrRjIvhhcRdzmQrjraJHNso8coASU-VnSaWHc6bpuR2kQNzWCHcBCQrYlradrbe06UJ5YTKWX90IVrGlB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKiEVTVaZmGAqGfsRtcZj870iOU1uw6o5OIqj966hXD5BhNQoqwcguU9zWwL6P9isYN0qrCV5v6RgIaWUJ1-pmzUDY2FXL_uOhxx-8lQGSv1_stEKQ9mvP7vT_zNSRLMwCYWgWl7FtajBr4HYekhlIVpf49QvyIgQEofQJgVbKuS-YZ_SB9EyoHMHV4t_1gKnQE7QPVO2pg6wvzQhMQGEK6zDeajckt79GYWWFrrtP64-S3ceRjCdZv-RFRHCDIgjMgn4K3fHpDoQHA9q49a7TUe9MS-_b4j8Sqb0njTwL9zbowPzYu-CBdslcBp4boxaiY9bX59coC9cpqAorhlKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvTKNtPUQVtHfyPnG1XPcm3eBz9GMla3HEWl7u8WLfWpG8ytzsakjPDnZ3MzDHAl02Sj-mhbJcHOv5ZbmOTMqDPvjuufz1UXrbeonPI-Sipoegam_qkI7OcxNA9tqGuplbl8wP0kp51UBa0IuR4rS1FJL8d4a5VoSsrr4cJ5ejyJDdNCAE6zYayGie2wikkGQHx62L61-qaGVMHqnGdJUdEJXKAyHJM2UXib1FO-hVGKcVk3TmoCyxo0iYdDGW4H6YsRoNKd7SFExYUKabcTms1-jddZH55zM6ykV5Vo8haWmBHtNjcYx6e1PuX-sIgwo8GomoEkId_xBxCKkqHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwVlw3nzi9040asIQeOOJqXBNATIXBndOCHAmBPgRZBNfk6AAPrWIiTCOJLNxECpPJj5SoK8ZGb6BqJhIslWqhPjxvbsxcterPGuN2TNbxgE0vFGuLzcxzNjPJnO_AICQ2RUS1i-GxvIdATo92JrxrXkxFsVuiP0xyZY-6eNvK_WziUe2hdjrv6YwMkSS0EAXULla0wCS8DNvGb_JuYFfgX4smjEulKzWXU5_lt29Qz3CQIPIbCW6Jp8lQCJ9SC7k3qFWcCRd4N555fR1BlQIlx89bU_XMV5uT7OzI_X8t-n9-6jFuqnNuwPZl5bzNDKhZgHmEbIMnqME-5EHQSBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYjUdw-rTAieu-jA50wYl0D-jiltbAbkn8srEhdaZibN1VsR45mS9rV_aF3GeKreXr3U3khVpF5qoVrNhJMTI81cpKcjPnQrONu61MA1pien05KJ0TjBaKx5F-XP_2yyQW9q2OSnmo9Ai59YhCpoiudRGuebC0Da9pcUpTK8IbIQLZc6YN7eb2VTuJwSUWz3d6EjhTA8BMJzS5_tQSQ-TQf9ZGpI_oHNwj7r79E_NQgzxmQTFhxIc69ha7jShX_tw7o9RYa5Z6Rg3epQz8q7h_B0gIbn8VMVqJTzNqgJMnEQ8jy6t9banJejgKdmLvMsH5eS6anOAgQPYI1Cx-kAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTcZAw9fWkrjgdjsjBGf2MhjYXy4vwVBXdaxTuZrLVWizmSM-GpnkKmuHetHwAuKYssBU98X5XuKGHgl4AgG4cLxHgIvFFPI9U0qbD_OoGHnjZ0pMOGQy-VEasISIByLk63-gNJ0wWBwkeC-42PiSnuME2p85h4KH2SG8_p9LFbSffZc5v51UkYg_7QRvY6TnmUJzQYvhjAQbet71q-ZMRRX-4kfrD7TSQr4cDmp3mcQxEsvNVDGb3WrcaHl96oQpVtBkwwFUaW3n8iRrRDXbsUXvOCGMG_4dFTEArQWQh7jrRvUbjTkDR2BehAMW8JbMBBnRxdILf6M7AIo6VEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVs5bR-uSZr8stoyTf2z5SSXqeOGvSn6kezZeRcOWcDfh2FR6kDBguBUZyerG1trWnuNQgHms0JB7wa6HzbvUdfGrO4OshuAYyPVw3mPuka_xxCqV-MntT9sVl0WzEuAZBMkl0XVfgfMu1sIVe_1l54j9m4Sw3CJkWGWEreOpfPx5T0lW8PcJwQcom4_JrAsEAhQ7_r0_onPJCNP6EEOntuDE7iiHGMtHvYJYHJlQV1KIQHulq6FtAYIvYBo7fCNp1uVI24QU_qoQ35hYAimHqd-SZhf3Nj7Jt8e2aOGF8Cs8sU94lTxMF5QIk6IDUtOdm4FwvwDenD1I_6WriOhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsTuVSSBMVRB7GolJtua6U7gfbc69gSjeOStOObPC9TBhNd2z9BvO_nUf_eUbABGRaH1CjXctKQihUHKbf5DnjvhPha3dDoq_zB_Dds_y632RFkV7APmULVVmwDTqc5wqAkRECW3dWEpDOMvgMyx8Hh5AujrGAmgNfZzx4z39o5o1A6Imb-2-pKSITvieaU8vHd3O_h1x9_v5drkIU2c2Q3QoNQvNSJFUOMpHBSRxtBwHb0fbjPnrZtl6-E-0EQR2VhU-3XUeY5CLILZ-ZOI6ee0QzhFRY1ohc1MPoQ_dG5Hx8O00uZ0b2dTPCEiPpp0yXNjwOwaP7twwA0VThJnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG_nOxxOW1jXC76gyMClkuwOcBbvF5fH8_mkhzjFSTpDz3d-1TNQGSkq8TMo6zuzVwKwiNQQT4D842xbiQ0dLR_U0N4DIBjoSGlo0QN-8LgwWMipq5Q4Nqy2AcAWf3Rh46a9uIknWYNCS1kkmQaIFigmyFP-_ScARSny3tD46Qx_XvOjctX241pSKLqeMrduJG9ESkIYHkZLl9HWXZlUYE26JvkYjUfBp_QuneVxw7AXYNM4HOAaEookglDHbcfbENMVlIEKsUglKoqX8FkP2htxF82VVapLAcjHtjpsLlAX3vhtN451bVoPuf7dtsVpMHcOvUs8mpe3Dhc_SRB-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHjV4lWF3yym1aMZD_OCMGqI_O4xVS1W7LEzVvr9i2c0MQ_hi4WTrWzuamQXLxWckcZMTNPyNDd-JxvIttqcVM8VqCKgMAmvuZTLJepJj5jcHbUi7NW4xs0Nu6iGkx40sFZvqSFf24cAGnn-f9_ViSJwS9j4LaHSBXBqltPiDqw7gfVw3WD7Hlo1o2WUV3AI4h-Ssiw6Qfi2CUxlD28l7a8VmAcDooTl3DMwwa-KwtuLr8q5L-u45Wcz4Sp3brmcMTSyYlmM0Nb5frkHsRt1weu2xIGrOqDV66HD6TPGD52e0GYPdpISMwbjTAajpCvPdHBEs4VyWncVxptmee67uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEvEXDMVh9vQCp8WyUhJ_-ECCYqE3AGRlAxNnFSVcXIOaOuv1SZpEz6S_NJN42N7j6P0BVJVl4BzO_0mWPjnGyzBOMsDgJRaLepz6BGT26GmNvk1pRv5jN5fENyaHfwonk-7HsWDkhV8Uc-GYsHlcr24RtXy8Zu33App5X0ynDplNg_C0GMZojJ0c_rZagJwKsZV5rXRABv6oIVEyZpHMZ_zqR_6gApn68AwUsi2YpRvIecOoe75L-4SyPEvX_hwHSM640BGJ3iZwbXgBukxktd1Uc4POmp271QcGI8sGHeWJMz1NM5bg71FcR4HOd22PM7D7c0vDk-Ig7tE6lTN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=CQJf2EBjhezzLFePji_GOfRP4coU9xCWVK-kz_u2ytg92kCwKON7AFEnOv3OL17azAhe1ECw8ON5ChZQPajcu3AkAsLgQMoiWvc-FZQFols_CMLRv2WAqiAJeBwzuTlVUcgJ7cqc00QYLACKO5A5K-fp7ODQ1sQ1IN77yBru23eKlsPY7ypM2IyuOvhejbU8lYTJcNy77UnHWoCL8LTC-yKMfjHK2xB2xt9jqXbxyMgTZFyL0-5ZlcCSs6sfIo7IINTZmMOMSrjpq9AaIez-ZwXUzXxotkcSeLdpNCP89x0VSP8pZowQag-bG5GHUsBXKMrNIoqpw6O3_QGXoVrOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYYX4WM-zngWxgEC9hgbnMryHZ6OmcshBRRCS2yuDotjiUaufnXZATSfLnjs8_Jw5-gJWX0uEjwLiiefIOJttfRVo-hmo55C9mlEoTi9hjtFovR_rPtOwf9lCgSwBRv-nkfcDtDdwjJQjXzfb03yHJymmm69Vr-Behar3cymaeD--2cTHWCs_pgV7bqwnXHhaxYR6TFrmr6-hkmojcFn86B9Dj4Dgw8-eDXZL2IwcEII3C4DDGoQuqTGzXGyU8amxVsnty5ut59kLgELaHE4AvuZA6jIfd2a3fbq0tQnYFrPatbSRBjEZrxaghMm2CpRpjG9ekY7FH6wOfiKQCzqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=MpG2cjHjL1H0q8uApLXd4EXHMnUns4qX3Ai37ohDzDeiqzEuhOiS1UmRszAty-Ts4oabc16iyf2d61cp7PkJpY3mi1RC2p7RITkIikGURLRW58VYSbmP0dnsXJaTXzIIRiud11MvFEkeOTGDs4gyxtlcEILTWKSmBevkjOjm0mX9S6nSghT7dxTaZG5ebC3RScOyyhJZHTeKQDm0Y-nYjjEHWzQ-2XgfkV-VkpQ4W0Gldi-hWiWF-CN1VNv6m6zarLobTjtonTvk5UDjoa3840F94LiX9dVIfPT7mlXVFYp_hWI649SoLP-s-3dq7Ye04I-YHWbAPOyCB-Q7mQavLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4uAk76Tbn-BHMRB_2a9WrIbFRMBJUdvChX8g7Cz381EVjGU90b3oDz5mGfcYbiGdcxbxQcqBDlHAgT1EHCTu_XPY4YTvQ7OBQNFwiloNYOGTX3mwtn0A5P1r6E3ItlRGqdQyv0ORRgdrbmg_LTac4qOzM5QcxWKSnQ8jJvPejhAAeee8k1yu7CpcCS_fk-Nd4EaisW3mTxz4yH-tG6XRg6IynKfNANZq8AtR6PBw6tD88hbbNGqh-EjwsYSBbyyvV5vpVrm2S1E5Ht01RR6kkuEEihfgrn89bXpVoEOdrptObZ2jw5g4DnILzjQGjR1xusE00AB3Z1m3Iu4W-ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mcNLItQIXTnII-_uSMClNruOA3V2w4U5L2Yr9hNK8PTZdCejnvJsm-oL9NzUSaRtJBvRePPMURr2A-Kc22T7ONT1fjjhAbmqyuh5uKAlMs-GZhRweHxB6RtOGCnh8N5elfhp9lhkbvuHjtMdLgEjJJQ4Lo4Ha3ncmiz2HDw_xqsMST1QLTwd2Hy7M4CiEa2eCbtXsktNui-SMOTzhigPUxm_vVcIVhgmmKkjUatWRW95ZLfh9MnRYLo-YcZE5_OLpr670yBMiiw8QHk4MgJU7Nb9aUGgyGFp5REzFVJRiRpE601_7VEDZcWXdz4NyjbqNzm1_cSJLZOViIwNws2jlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=ROxAJ8fOpehQb_EngRa_pWqLTGT8-RpCIOm8poQbTajIw0_qynaX9SRTTK93yjWfj318Ic-Nec9QLez1TcrWBlY1ltQWomFzAHvEF8FranIg7K9wQO_B6yxdcABao7idoF9GuT5EA4FONbLcoWsJBJzpbLRS2kkDymSylq-bh73IEjpe5MCdbq5SMV2XSHH20fwdHHejcB1vYYQ57AuXgMXVEaUy-YQhYFVE-fOO9lX-CMBGQQ2YkhY8qudLZd3LVwe-87_k-HZ-XCI_EyjY5fFkknSUrcr2fpuAHTJfMaTP3fNBDG305riPhYUqTdkfmz6YNeH6yo6jCRTj267qVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcsse4UfEKd-pUZunvQEGt8vS9Jv5JBqjVJbPW5nU1OTin3vwf6DKIqrh87LL-xWMMxZS0DwRj9xNME7-n2CTnjtsVEbE3Aiw39R5IoJ21jqCRUGzEYo12pVuUMW_odtwJe46BPLHPrXqdKydClGbCizVaa_FGlv2eL8RrQI2gsuBeFSykQlbyuZMb0MTPKJhu7SkK8HkPP-7SQ6_aqMFP5xmNhcfONghvGuKp-U-sfN0SZ4P9ptgK07ylACBPJOu4m-lrr0KD4K67mFOFrC3AaQxsjcuNkMnK-myZ5n_11KNr04Dsc_7tZd8SMRxXeskUZG0zD2jMZE5TLSOlwmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcsqZNZ3bQFbtLeCZTI6gowxFmgC6EhB6a0p57mdp6Z_Za6shwMVA99Aqjs3MDwj-72kVVaDiMyRBbfHB04WGMZIefKq0ocApOIUkFZqfFC8GU80Z1KkEfgFOEo3-u8b5Q8feJVj2xz9fpA-qc7FR91tVXUY6wO_7ZtmW7ryIvAFX2scbStk3lAbnBoO4hsqH--rboF1MttjLft3B5-not68ubj2TPReT932pApdiGXR8ezQFGTf16luI03gCxLMy-IuI0iuJBQP1CfFFL3ZTvcR_IOXVIizF_fVPL_k8kmydXYdxpuHvjoOyXpVO3bBDK7BClHRGNcYLUxu5DgHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwvUM3VgqCp9ycaE8WbdgKBlufdVG7em6Wh8Cg3tsMA4NrNs47PVMuXfpyl7vSP9xOpufQgG9vYpDbdwriqX9vcm4h6psVbdzeBeaxEQdgBRQ3wmP5Q-4WODLFsfgKz08rtxOc0NvnftXhQbjEM-NZGUDg8-StBdpLgmrOyufu9wk2SwYa7IPK3hH8VD-UOuuZmSpknBIbAaPmV-ueNoD4URe4GsKMH5OTJDiWegQ1IMhw-BlYS1P7zBql9RURgBQKS-3kX9yTFcLbDPRVTfjDDGcz0418ggsZcr1kB4CnnRcZc0AKTlPF9rP4XgP4aa10O_xqrLWAIqm_-yQ1PtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdqfekM_oL9fTvyNa6IP59g2obFJ0zuJJmPr7eSCh39muzuNCYT2uI1HMxWeopYm3VKUTTPm1Bq8melbDE7XiUm20A18pmJAxu-Mp7vEz6CZGZd_yp1UN6uR0Bccm7Beu8sGnRDKt1RKtdwZR05lR9C6mwES3uNV992BDfc3kUr-9N-MdN96GI9LKi0xB0Nd_e9YIu30lZGaajIWXJbJ7e3Aepm7HlejfMpgHdpmoxAnoX5p_MZP7LsvQrZLof95HA0-OEs10hxv6Ow9-aNIvfBHEYcudAL2nsJ7tVtV9_NpGa1pgGX9PHsp1MyJYL0xquo0ve2G5UaH3KIvMhp56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIvv1C_oYgbDAlQbK9_yxQgsnD8STju052XY366bYp1yRoVzs2VIvMmEM-jBh9kZOeH6kl1C-dlXWRFIu_AIwEz1QXU0TTbcZ5BOxJJgwjCZAgKlGf1hIFIgyL3jmxX8LHvJ4CYkPF2Tz4DLkLz7Q-umqcWFjuClmPAkWeMBeLmVFIyVbijW87Z3ezN09CWPUGPE_sMaJpIKCiH8sWcDmw7qXHCikwwb7Qswmyo2UbeD7EIqTxkFFLk_8UU69EOGv9eVJuKikGcS6a9yH4857HLOJKNfjeERRQ3RTOUkv4Yi35TuiHOeGPz2so1Z9JzchEiAe-hp29BgGHO3H4PHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF5zJaNFeTTo-3w_ymFWvRhm2KDCeHjhSfggGi3UIBP7my_evtgFqcO7xZHh5mBolf_I6PJztBsBva5XNxYe4u5GODdTXJ8Yy58wsnNbNHmcSJdvrDgKrCvETqidS_HK2_IJJooiEw6_4bZF4QNRSf7NhZcgXzuR3MJVqdh28b4bKKjBSHz6Mjo7ufRTXFPwHgociQNFB9avkKAi9Y1gHT2QteJhmbfY-0RNNdzy2_WJKYVbIZFNqCz40pappc5Ic_lgaFn0iFP8fJvlxQApZji7pg4N8xHaLFIGG-j3fUJpbEk15Gx1p5oBbfUBAG3Ry8nrmB-lVD-2q4abIbOcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N38WORcAe2cCP9Ta_LjUYjRzrDsu-4UwERUdadfrhqLKX0e0unkblZ3vIAhPWQen_5u6Up499Tlwiu9Iq5RQHsN0XZqLAA_H_bYqV_1CLPjo1J4TKpi96njGF3u3pn4x6xtoSDDwLMsTypLdN6phnwSHl9ukSMTwQR_K0wp5Ig8F0LQUqOTKjbzj3AfUPdTTGh2FP0vTldlazOGdMVEDlqDM4V8vHrI-0GHgKydQ49V0O8MhL9opLAKjSOxiEm-5hlCE-0lix6qJe1aRCQv01RvdNswsR2jFt9uHuljPiTzteblCamNZFkUfOBj63R3AlY53FHw6n9m2Sh0XAZV2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtISIpZ1yqXac_TsO3JjbsexVUvZAKogMW1QihHNv5DMI5w2hS-72VeRvDDsZ6NovMFCTCAs-ZeUO0cJb08s9_HRKeVroYRvfwZ0RfQ4VkXikS8dYC017vgk476LOQWvvtleJTcFTwDfGqboEVwOiIRT3IIuq6bcaMKrcxHMZ_sFkvpz6h__hngaQA8h5aly2oOzUjpCKNaWwX5Xl3ztvWE-alucnRJ7B92mOCZ7FEyEZuUbRSEyKYHwgO9RiQ1ENUvoAQx6k9hTilb7YzNfJ-XNs-S1eX4fak6xE703XUdR5FScI70YM1SDkwaNWJJRg0VQ7yMzhWv8AbLR8No5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL8chZRAukZ9rMygwq320cS4thPmXbSq_VIzlNZGbp1RrvLlhL8OOMC47JVZP4TLeTHd0uitZB0wgvw79JhdIQwyWcx5UnK5NHd_XouaSqn_E-Cg0weVtfJDmwEOpnYz4vRPFLoxjeAA5Dsmkr7wnigv5BNntF7H3i0NNkOAKjHIYMoVw8jo92K7IdvoEqg-qUYeyHWJEalkhRgoy8Ufgl-SQhk5zgzZG7C-Pm-J_MpSy0Ow2zYqR094PItHGZ0O-tIOq9qvmk7rshH0gJbbCwO5RLhRaheTU_FABSR5Swaqk5SpGo3UmNBEME7yA0RNZTr1jAl08oLGS_MV0TdgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=DtSDbTKZ-QC5VJSrlSH7PmYja75j7_m4rPXK6zvMKS_jLFm0JVbkfs4ETstBmG_sdCuwx9l5F11f3VT2vNddpPX-7TajlaBO9Dg6f6eoYTzbQ9Ke7yaO5dk3faHAOY6jlGVJCbhsADhYd1Xj2CqLD_JZbQHxTU_h9Vi6aT4koiBT7MTGiS_-I6MTpCP1M_itS-rEeqhqgFYmOZ2HokivfX4UOPleFOkE6hQqonvzsCY7ajtwTTUVu9VllzxIKglzw4hKrJrc2ahY-hTKFtUNFCmp4dBIQnItETMB2M1iKzpuKvHcD5Lox_ODqCnBXbZqOGIyASnmdl08UtX_nqeoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=KXhfFO8G7xlkhjqdkB47IQ_G0yW7Qc0P07AJf3RKgePsiAnSHkKbGkEpBU3dKTIGLEjt5xiH_Y98OvlhV6BggCNLbWFc-K85wZIYdFUXXP541lk4w8tMyUtJSCZBoUKGPQx28tEP1gOAjS2JkibCWN5hQIRXYHVvx7aznkcQttpUj9rCJXH_YFUtdalmc8KwUVKngU-IaXcxAhyB7-q74OXVfEBuoPgXWy_HALhTGR6ZavN4UrYewQLNrsqQ-2gZKeXJIswLmzGLGpzSRqKMP9a72bI4V1EiQp7rO2j9xKpQ_2iswTmdqQ7b38vClG_RNx4CjDTKaVaJbXAYiRYg5ZgJrsxrR7V-5253Y483ahhQJzF_sstGI4_jAf1tjpBtL-Em1QgkapCS7B7aiRqOderWq6BE2ArdNmbOmPXxurDA-cj7TKVRY_cI95IYLVYqaITDzOWxEJQVAzX2a2q8DqmsnpEe8BNRlgz6tEKWuxZUWr52mXK8HkJ_ZJcFz2eMowDC-2kP8ikxTRlRATWf4Ousi__CR6lREZ7cbn9uzDo277FtPSsWP5JCVcoxeKZaFkP2-B_U-S2R_xxc9fTx3Z9QG04sOgH_UfJUqKtcDs2EWSjDNBCDuDFhQ7vD2PZYokN6jhyuOatGKk9BRMeoSGAiV8h21wh3ryownjAWMpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah4yNE-GwoHeRTC90eWPQakqqtfLDTAHC1mRGsIOcj8H2JLyrih64dDTFVTD-rXUWHj7u-FVgFDqP88J6L2o-KO8h4sSRQz9DFPOSjNudyhS6fTu1eJZlQNQV_JXZtFn_AyAqSenWrzeGSkeJsROZ6_vDPVYD4gGcWqUBsquTmN4JOPbu4aJxnl_O5Qm9SeXcbfa2iMJ9Yf62ILvteUC6cLHZ70cduCj7OoQ3dHy6LTzYyxUUkYmdsjUqnOEjKdpyMAoYa29HM91F9oq31kQLR9c5_DJVEUR4z5vcAqYhkrPLFtTe0ywSGL2W9MAPurN-ZSxx6x6nyovjnI2e_ad4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKtpJ_KJGDqr5UYabpwHqDQJ1R3qTszwn7NJIyWgmHMm0Y1k8MsY2ULQcu7Fe1XEwvdnHBn2ItxxsX0NTZVqL7_NYBktVmDgIvhRi1tvmyta92a3RKOdIExiD4d2A0B-NHvux5OQLDHThBRFhi1tRADgvMQ6Jj3HZq6Vrmmi-uZMqZkIqsJrN4Wj0zVF9vD5rIbm3fL01X26dMAuVUa-9ARZtCxKxi6jdFbQMcFnHVB9TO2AB8yzcUOWDynB2FzENKymr48H-gRL_WZrttviTppHSR4IliWkZ5DNfeLCEMtZUC7Rhod8xBM7TvJo8NWf7F0mT8iNN7yAG0gsrlOBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7hCitOpGaAzQUzFJKt3R57YP8i1wkJ1qthJUtLVefzdUDwgbEbnRKE2FJELdx4ifFLrQqwF8uEFjHkm5AufBToz1mIIxYHpH7Tk4Tr6xQfbOoGb2CY97l-ygz-DW0IEjfVH-_OGRgx8cTfjcG0W49pwjtrrCL8p6YAHIFz693XJKO6kYxmZeA1OJmkoR9gD6U1JouHQ3UyhReLi7GvfFHq9WqDz4hrR3nVVRl6YAaRO4hTY-oSuTkzWnDD6flTzItswmLv_-_v1yPXgI6pxdCeyWdnMqHp7foVNe9GNX-YAwmxlb0Sx9K7sVOpgRYOkGWVSSa-CmJNxm5iMUAq8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCdUIQBeGMaO9UHtk3gR1pWT7bM6EGcBWh99YNb-Y-O6VuDwFHiMen6MGGV7PwKLxNLuRqcn2buNLn5ZUIrJXNtXLKBBI3rwnywm29NBzCNP4xoQFsLjqXb6v4ebRFMsYC0zhtV66KapAI-nvMTQEPDdQS2jSsdJ8W5AVK3_HMiZB0GnmaDzPbPD-JLidyZn_np5FMFG_2mbilxNZfgKYWcIs2_nvfDcrQ7n_xqtvOJ_Kbj4SprpF9SBIPyVAcBm8hwwCSQQkr1GoDMRGMMQ0cgFVAq8y8Ebx5F3BBIz7hN8wIRC5pBuxdG9NaeybDwOxYzBL_r4YVw-vYzDKFn3xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
طبق گزارش سایت Score 90:
✅
احتمال پیروزی تیم‌های ملی در هشت بازی مرحله یک‌هشتم نهایی جام جهانی
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98179" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af013992f8.mp4?token=qZyUhyzdicKgkSmTT9bbZP8faRqFBUYq62ILZF4l8hg7gzGOhmNSzAB1wtxa4mkjWp63OW3DN6jPIEJbKI2vdnP2roeZ-vW306eRIzoLVHfZNPk1YZS4h709Dr-Yi-MMSnInUI8DJXmDE4iADZ62N3m_3Rj1FQhxgt_-4CflHOlRyrbkcRvOzbWAiYSYoysbRLatmyHU01QT1W9y_BPkk1K_xFECsaDf77Y7hOnT6imKhXHLkZTDoBwvGapwQmSuowzhyS6277zpK9_ZdzB8WRw8ORcpkPBmQ4X0aSKkUo2cZe0h2PJ_UgtdgZ_hNgk9h7FkYRMnqJK7UtSrqkR8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهرداد صدیقیان: چون رو جورجینا کراش دارم دلم میخواد پرتغال قهرمان جهان بشه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98178" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🙂
🏆
🇪🇬
شادی سم محمد صلاح بعد بازی دیشب و صعود به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98177" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgY4_Zi3ZLdQZcdra8_10vcybA94CC4E8a1N1UuFtRqQnARfqMRyikJR3dubbXN4pNweCPKSCZ5dDYQ9DEB92UMEp0xVQjBSGIY2M9wMCvpBdT5F5t66hsf_vygKY4Hura3D80ExZ6Hapoohjue4hpPWuEELBs8CRj2AjwdA5LGDkTTDUVeUmRtjwacxzKuiHiwGGl8TJ1UKMHe_rSsSF2F8YJ6b_JggmvzYKjI7NHVs_uXbCKwqY5csnBYg5PbOf0p8T72cpK8wuheJOD2e-4fDpyjOM8TGf8ehuJeEBGoNwoqvR4b-cpHXILhbFLFTVKYH4auLtw2GcnfwBmSVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
میگل سرانو:
باشگاه رئال مادرید اعلام کرده که منابع مالی نامحدودی نداره و انزو فرناندز، هدف مورد نظر رئیس باشگاه نیست. فلورنتینو پِرز، قصد داره یک معامله بزرگ و مهم در سطح جهانی انجام بده و معتقده که اولیسه نامیه که باید به این تیم اضافه بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98176" target="_blank">📅 18:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
😐
مهرداد صدیقیان بازیگر سینما میگه تونستم مخ دختر مایکل اوون ستاره سابق فوتبال و برنده توپ‌طلا رو بزنم و حتی برام هدیه آورده
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98175" target="_blank">📅 18:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98174">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gudfLJ7XJyeEgfLhUAwMtnpX8EkxjI9FMfP4NMFdMgXT3FrNiinpUadxEOq07AQISRq7xHrrUIRLo9Z9MqIkmWBmGUrYX0OMyqpVcMoXvlQsH0Lplg39ixDVLONNBP6QvxhNYfhi69vI7U33LQxetWdpCWmcr3V8FMfCCXaYaVHzBSi6rYVAAXfmW1TwoMygQ9XOito8ZLJ0PIckNFsCaOXuA71sc6KRnWcpCo4BnW_Pfke6TaSxB5Ob3f2LWcF0VMS-KRwTQsb3KIxdv2WoSoaXlDL9GtecMdsYSuWkjsAW-xpEPIp2mkD0bLj3Acz3qseU4C7EuJTK-sP49dedKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇭🇷
اظهارات فوزینیا، دروازه‌بان تیم ملی کیپ‌ورد، درباره مسی:
‏" به او نزدیک شدم و حتی فرصت نکردم زیاد حرف بزنم، اما او بلافاصله به من دست داد و گفت:
‏' عالی بودی. تو یک دروازه‌بان فوق‌العاده هستی. حتماً مردم کشورت به داشتن تو خیلی افتخار می‌کنند.'
‏ شنیدن چنین حرف‌هایی از کسی مثل لئو برای من خیلی ارزشمند بود. از او تشکر کردم و گفتم: ' ممنونم، لئو، تو بهترین هستی.'
‏ سپس از او خواستم پیراهن بازی‌اش را به من بدهد، و او لبخند زد و گفت:
‏' حتماً، آن را به شما در راهرو اتاق‌های رخت می‌رسانم.'
‏ این لحظات را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98174" target="_blank">📅 17:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZoNPfkkWFkPnksXzK9IwkYDilCZM4Jp5NZwpZ-a1stOeSpp-ugqaqZQjrRqPhrDdOk9Rfi4P0kZW99pmqkuf3zZzx1shzU3kb1_745F912rI5OmgATx9S7UYXM1JB_RURZ8RAHk7VlUdMSyQoq_blzSIP5jI_h610gAXLqFA1goamksSisEUeiRJ9lvJG9XJ1HL3tiVDD63OcUxxcFeWQSI8ZnVTN_k6vuffkf8RaxCaNPRklrBcYv37vXXe0-ZTIWJ58Sc6lCw1qGEA15RQ1CBWqxElZjfMoD632635STuqnzG-Rx4lJ8fDPbY7yIvQQ66WBChb10wzoD5DrQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=HUEJy0iJmBPUOspgyaIyHMzc2VSJDzaFvuSQY74-2LILiw_fQdLtteyiQbCYV5X4ylp0Y7UL2__I5K1IB16CX7u4B_I3CrFGyAOMWxHWjKKk833yjB7epOWbnBFfKHvG4wKYOd4feNvGYFmJ0Jx-fghs5hj_mhultTl1248fLnWwytFwXGOOlhmMDgYG_ChaVgPpSYewC1YkN2RwdB5T8xUyFinD_4vCKHbtSmeipf8F_vaeN5SyHtv0imV0kpGtVO5Y3Ec0M6mIAKHtIPna9g35DX2uSXCFsX-vUoNCTyK0FRqqJwvb5ll9dJvaD7zXThRAgeLI8pVIqYNTl7GD0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=HUEJy0iJmBPUOspgyaIyHMzc2VSJDzaFvuSQY74-2LILiw_fQdLtteyiQbCYV5X4ylp0Y7UL2__I5K1IB16CX7u4B_I3CrFGyAOMWxHWjKKk833yjB7epOWbnBFfKHvG4wKYOd4feNvGYFmJ0Jx-fghs5hj_mhultTl1248fLnWwytFwXGOOlhmMDgYG_ChaVgPpSYewC1YkN2RwdB5T8xUyFinD_4vCKHbtSmeipf8F_vaeN5SyHtv0imV0kpGtVO5Y3Ec0M6mIAKHtIPna9g35DX2uSXCFsX-vUoNCTyK0FRqqJwvb5ll9dJvaD7zXThRAgeLI8pVIqYNTl7GD0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98167">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=kGeRZ9PInc5kF5FJR0ZYrp1ro6FIUgGwCDZg5F5QCA4ln0acK-u-wi_RlWOHkFGn6568F1K3-eua7aBICVSvwwuSRw_7zq-PQtPVj88PRzJzUYSQTItSpoEWDTxfII14oS4HRgpriT_kRCeBgSZp9PvVIXFNRTFd1YzWcX5MGLb-eHc88K3Iwsjkg3D8alS6tJ2F4-4VtcDXiktylKN8yL9YP8lFCMIu1qkUaN-EO0g0YGntDlmjC0r7PFhqo_iGMyPTEtbDUfqgASXk7ROSx7N5ziJgu1TemEZe80YpwTR5ghj5PrX35fFS3UemyBLgIotNPj9hC6LlToucqmBtjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=kGeRZ9PInc5kF5FJR0ZYrp1ro6FIUgGwCDZg5F5QCA4ln0acK-u-wi_RlWOHkFGn6568F1K3-eua7aBICVSvwwuSRw_7zq-PQtPVj88PRzJzUYSQTItSpoEWDTxfII14oS4HRgpriT_kRCeBgSZp9PvVIXFNRTFd1YzWcX5MGLb-eHc88K3Iwsjkg3D8alS6tJ2F4-4VtcDXiktylKN8yL9YP8lFCMIu1qkUaN-EO0g0YGntDlmjC0r7PFhqo_iGMyPTEtbDUfqgASXk7ROSx7N5ziJgu1TemEZe80YpwTR5ghj5PrX35fFS3UemyBLgIotNPj9hC6LlToucqmBtjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
رفیقای من وقتی دختر میبینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98167" target="_blank">📅 16:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98166">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98166" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98165">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98165" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
