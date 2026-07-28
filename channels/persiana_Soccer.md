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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 612K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 00:35:05</div>
<hr>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBd1Tg5FWnuYi_lPYMdbwPI8w_y9qH3aDl7LE7h1orQcCdlYgucNh0NEUtmlFQpk5iFob0eAZnHmS8gC8IksAjxGx1g3X0SwUBIRUg3lsf3iC2Z7ANh8OyfEPdw3spELZNJ5V0x6bg5o7MNRIei-Lk6NhCzzJpgqIKr3TTrLXSnRQhBE2iPzm6r-yIDkQwUAkPmtc5W_tE4BzRrjMPSbsa8qvQeYnCdVFK043w1L-ODM82jKK_yF4EAULQJ5M3YpWgHF7KYxT95yaqLRjB1f4qMTXcaSNibh2432zttgSBdwYkwSpwQMwqWFO4aiUQ9mtpq3t-MVLENn7wuw-fsRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqubjHV_lnQmLdDOknF4DEc2j8o1HwRKU2fpjiFdGv3MByCRQX7ufX-hbxTWYl4yy9xwGtJRrKsun51-IkUmmG9_uXS59vM7kVeuvGDYAX_tCf_RAHLkOAogV2gKGtec59GnvaCWNImaMIytnjo3GLByUN3LUDyS4jFKVUPzF99KtMNB3kXb8l1pt7SxD0QFVuuwgm-xAf2jDZ29Fi3l_lnRvCW4A-7upMZCM1CVeQujuANOd6-pLNh74jg4hnO-6KcMCeX7Br-RIyTDUU_DdbQCCyuiEDnLsOT96g28Azi-OowH6a430Un3ZzDFGXSzbL3Sfo8_skb4dAsjoh_2EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1q5bmCKodlUCMLVn7k1I8omVSiO5vjtW31npy9tAug4BCLKY9yAZHF00L6Kk-7kz3Y3asCcA25VK2msixR_UcQEx0xrt9uxFZHI2EPb6SGFAYZqi_d_hzIooDrYQgRJ2hATFI81M8NEFyYUbzj96PUcv3MY8vNPBhmR51mAWbavXSIO_nd4lgoNsvDc9bF02xRzWwRK1ul8RfKyNfQJvq1O4dvIF79nASY_aGVMAY6N_PxNEcyKjYVsMRCL6hyZgTKX4aM17RNTjxbf7mOq-Szwz62RcNbsK7GeB7QA6mz-bdb6cxKQgLLSKM3yENYmNu7qK4H3h1mWuEoZ79wzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKgZBsWmbpUmzUA0BV2hc6rKrK7ss-6X3V5ii_zu4Ucw0OqZ4Lxika5xeyqjOC-nXoV-3_YiW1JSqngLU61QzBG1Li_LuTsYbHw7Uc25mrGRXYf3BCKWFPTHJl_CDhJ-goMxURbmpmfp3AH3qQq82mkERLbatkFc3nNaKn8kBt_oajP6VwaU9sm4B76ZuiqejQv43LM50XVzXzkuS77myQXi0bbOr4Lya3f5OOOOmP30tup0WcQLXVooYYUhhfmWhHCx6Nt3gXzhLA2j8DU8oclck-d9yVXYt8BGpPlZJ0Qnm_4FSz4UUBswe9lHSD12hz55qNn0U4dNEQIC72C42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=PJbW-h6YfxEEjFC-1ggOyKr74pCTA9cC-MOGV8AVda8urEo-WsCBLAVxT-TJxeGIXAiokREJ93TfJGP2u0ZTbJ-bnP8csryIWQtGJ9zChv0xGPh0l3Yj9hisTmw8cUXo_rMFYmon9Xf0M-8KKnB6ksSsc1dQGGWr0s_3NpC_3P_j3FjgpUGobopyS8VTc2vW_0hVtFxnYrQQRxrebYw30pR2_wPJj7kWEZUf5Gzg3w3r1SEDGZS0CWhlDIMrITCKrJWS7lw6EhkDGpiersh1EmEkPBIu-Rga2NXQJ8ypgKX3Xq9jbQBxhbzTBYRxGHaGiynRMyFZcplwXq4o76d81A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=PJbW-h6YfxEEjFC-1ggOyKr74pCTA9cC-MOGV8AVda8urEo-WsCBLAVxT-TJxeGIXAiokREJ93TfJGP2u0ZTbJ-bnP8csryIWQtGJ9zChv0xGPh0l3Yj9hisTmw8cUXo_rMFYmon9Xf0M-8KKnB6ksSsc1dQGGWr0s_3NpC_3P_j3FjgpUGobopyS8VTc2vW_0hVtFxnYrQQRxrebYw30pR2_wPJj7kWEZUf5Gzg3w3r1SEDGZS0CWhlDIMrITCKrJWS7lw6EhkDGpiersh1EmEkPBIu-Rga2NXQJ8ypgKX3Xq9jbQBxhbzTBYRxGHaGiynRMyFZcplwXq4o76d81A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBGD-1vLXLT-YuWc4wXvG0Nl7bsvvLntkt-WHQXYR8059DRn8TvoHKnPK0y1UV4SswswlKPGUtbLqlClOtSmdLeDSIQuMdwD-cO9kg2AayNhyVIbqhEdh-7sYoUZFrnxBfm6Z26ivlq1Z7T3nlPIDjH1_P_ai_nBn-uaC7lTj8yZTmJIXcrZk1UODaeRDD_wf0bPU1B9kbv-JP1AuAUMeRODOJYh5--aRHwnuSpN7bYax3qdkpCHl-74-FpxmOIKMjKgmI5vRHb2-sgddvY1pCdz8Qc47GpnLzuJ3u15XOEEUN2pzTF2Okj_c1GvsAPz0TVyFjz3a7RCiS8xdvDEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN6Boi0BK4aE9whbi7X1cFkrZoXw92FKuY5dju4DOyfnN3njwBV1D1mKqZ0V749tlsdm6GoYb1sAD0VTMrjpYvN0EIY9kydxQ3a4Crq-a7297Oc2YSnhSlVIPzaHYbp-Yag4PwJ6hcUJUBlUSuVJ5QSt7SHp4EtbURu9lTXp0odGTou5cEIaAjjOwNiSm2s3aKJzzqdSIbD19_XsS9ClC7dph3g7J_oIHYMtPuYHZ-CeuUmQghntHsCBkH23SJcfBNuvVkhSBOH7d2-dIAuoU857pxwFb7SKek7ocCiVpQ0K0UFXHx7u90bCqZwc8dgQ1APYIb7-8gUN0IADzxRj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHEOtgQr85qH7LNXXOncefKoNHBRv4r6XbwVmFjcTH8TIaxlM999F3b4PJ3EGwdo34CK91xBocWwl5y6jr0JkoXM8uaLlwsJlZPFP-3-Hz7uk8TPmNiDDSo5hCkFPHVitBw6mK4rwgtcMBit9pZMH3l9jVjjrgIolDQ1TxTeHTwUThh-5_m6VP1IaN02Hy-wL3b6PN8nSQ8CIsZ-iZdUGuQmMF_oN4YgtCfmaA1eGq52C_C9zYxsoYX7OPwQPGkVpsvJSGGqFDfka6JzPZgzB-OQRyI97wIH5rnmvMGRXWzJn9kXtnRxO5gWuPoRss6a-ULJSs1VTDfXEFZx9-4kYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiRt_dfbrkrcfMGsiu2bgx9hjlRmIyrHd3m1OX2Uiun5C0oIKN_J0FtJ_8uPFM-9klarHfy3eBpe325GXci4OK8ymiPKoGKEFyo9COqJUaE6NHdKJo80Lc2CZAGmMZfmrfDF1pmlFsjesda7jpPhR0oooBCcKWOWCZ5FY9KycudBxbMvQEQE9N4Asau7YmTZrvLH1jDcOUeTRlvJT9YPUElWkVz3MSYug25SP23qkH1fhE4Y2RzeAlDcOL1R9ZwJIn1VJT-pZH-hMae6odCyGQUVkAzbWXXArNqxFf-OnKG5y2pAqs_ybhm2Ch9UTvCmtm4uxngraXCVZ_DQSGzcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PPUgdLUcGUvtcVuHLIpQLJm3lf0TU8DFi38w-uFmgX1WQTCKt2SBgbLcWa2xoLPXLR1Stch8Qg_Us5gFmmIxaInmvYzBZKrbSrSZ05_CM8s4DEoSO6IHOaJuB2F5-aWNrMz-lIdYbcLPpi9578abX2xq0AWx1j4-bUXsMr7eP26ApV9DW2pEn3Qxs9KIyBL8Q815GAje2gynU0zB7hzqmlttTU0ny40lZ1hGLh3TZxJXdeCGk34D8GB47dcvyoAP_a9yjyizj6ejLELpHEr8Lg0vU3msofq6RJ_ZgDjKp34c4JO2CrI7kPCe4l-zY0hvwS-qSpLOZE7ixSII0q62tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PPUgdLUcGUvtcVuHLIpQLJm3lf0TU8DFi38w-uFmgX1WQTCKt2SBgbLcWa2xoLPXLR1Stch8Qg_Us5gFmmIxaInmvYzBZKrbSrSZ05_CM8s4DEoSO6IHOaJuB2F5-aWNrMz-lIdYbcLPpi9578abX2xq0AWx1j4-bUXsMr7eP26ApV9DW2pEn3Qxs9KIyBL8Q815GAje2gynU0zB7hzqmlttTU0ny40lZ1hGLh3TZxJXdeCGk34D8GB47dcvyoAP_a9yjyizj6ejLELpHEr8Lg0vU3msofq6RJ_ZgDjKp34c4JO2CrI7kPCe4l-zY0hvwS-qSpLOZE7ixSII0q62tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSU-iqctpaPQv3qxxts7Ojp5VopAYh9bjc4ml7gqesCihKPuGprpzcnKcKZPhg4RtWH3Z0orHy9K9aPEpIQFK-GqLdL45o42x-k_aEUsi4vNHCVHRZLDfRhi31BCQjRH1Jt6BwmhUFUaj8WsxXMbWD-COuHxbVBUBEh_D62to-oj6ZHbZrBE8GEZM179O40ycF8zKObxSMzZkXkABXM9vKJ001DkdZ_OD_8Hg9Wriad-0BbO-Z5ldHsD_AFJoFqfeD7GYYVpOHSzUM-CyiOTd6qsCR9tnwjj9AJ1wQ_AKYx43RBBIL4SAniPhfdYyt7x45ejkuWKUdNqwzH3kVuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6hrNUQD3F14akj1AxT3ljvqQPmtqb65o_CjPChGYV4_CcRsdQ-uOlyiqZyX-fqSGMY_aZSyVvhaJzCAuTDjJ1cfoIFB3yzpgF1E25eocdwB0zLLG-eVuSD8W46E-_6xvxuKxt69pSL2-AQwt7YDp-bdpYouQvevByUjHSuEexD_6VfAGnseirZ61lezqjRhUpZjCN3V1EF6rn0CoaKugkyBCzRv0sN7R5iRQdJvN_ZQxtu5qTZ8g3vNceO6pCnwdNx26qVhmw4lOp1eWwfJUIdqtUjMVKIXWaLeDv3HPRmgxa2vVJtnjyWsIJ-QYzOsys6PRoTEx7uj1_l1RCbGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOWuF1uw2b1K4hA62KWZ_1sZHILUNPxdpjLjpSeuOwGBm54GkQfYTwzxHpiv2ywdVE-scmFAsdWPI2iBZn-qy0zovWhb2w4izOzEIj5ZwJTBwUcltZlp3fV0DC65LiuAey-5StqnHY7WRejRTimYY2lxWtitmNujQ1-ClKz3agfURN-x2RUQWybcGoNbI5zMVAO-o4MgbQX0GRyvKD5pmLboegHMhqeCk9WiGliBhHfnGQyQOSM69WtDgyXGiZiAdLYQp4nEjPcmNAJLiIA0B3prMdQ_O25q9aiRrxAHSYAVrcdyCxF885qELSZr7AdrBiMSGxwG_FE5dzG4b4E3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpN5XpOsT_QRHp32AJMNql0ke3yHJ5N1iPMr4YjPt4aydff-yLbCwYQ3GMxgDQq2c8J72hiAed1TJDOT1pFsfXXui83yRrT_xBq5tuxh4AcIdNV-mwWSYEZ6d7ToassfhZ_NfqBOkb1BRy7Ekor7EZQZtNm9eYGY-37X8wsRby8qwjkZVLk8bIoCGy5HJwoJdXr0exEswLk2gQVDSKdTs4Edj27aXJzyjwxZTCJdSBdDh81W3MKXptP0dHye1MMZVEoxvtG32mFaAtUm7iaUFSoLNDHaRBE_i2QnSMbkfv_y4dctlwa0pGdFmQHTWP1SYu3pT1SM22peSw6M0W36qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHhqOy9m6ob3fr5ijjyMRhFttD3fx1MmQwc9LGmrFwFvBNNY_zpf-9_140WEuo_NlPxNS0Ya3e3VH3eqdr7qSXg1wFiLGgA1lS0IdLszLNDIJByI7T2aEfOGTV9wgAF_5T-L4NPaxubL48_2lV9UsV4_4c7qN8oXTVGgT1tc13dflEaM9-Sm5fL4186yaivTsYJLIQRkUdYMEc5XQGmnzrC-eIifIvAlKTto5z2T0KLbAqaJdQg46A7zcxYDP3OK6shUaZbCrc8Qi2LAOUCZL5ZVrO8X2Y30mEN9JepgLbPW_IE62QAhod8BmAkxGt5BjKxhJhWEl4GB6SWui1IbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTP0WWgiooWfTUGgsXCY6kvm2z4l1G8duRWdokHr6OkeEOJK6qh1ILcC8POeDZ5h3GqAw3sw4Np-SFUQ4uXOkbArObU1bgrzNQA0H0VZrvM4O2-kkdAhO1s9VQUOawlKi0Pf3YVSUsp6K18atbH4pF4_kNNDdPQ3QB_N6Awuf8IcaZLpXPLng94QcqSnNh38GSjSNBAopE6H5HPR7zF9jUeSV9oNaWHaCEpH4vQv47MAAm74OZ5PuTsESi0f1BK7toqP0w7u7yHoCpwfQbkFdSL1ik3jZe1ylposmZ3cPdB5hI1hh7ZEJx16wydoWxXV_T41xCctmZLp6E-BmbD9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dDJHf8ElTQlfIU9SP3DR4EzoubMjJA41uACr9yQLxs8aa0hqd0wMQmDPkmEE1t9S3MppFFHSi71QH2ascjnEXRsSdSHsrCu2TQWaC81yAVcJHQP2lBrnQouVogmVbGr5VGjy1wrR_fXzmtV09tRsM5OOzP0BJxcSB_p-W9xDixvaZegZLNHkkqKSc5SOE1siGL7rvPU3paiemFo9rWzSeRzbpd_zt_C1lzLF0_SGIMepyY5kyrX8-B4gGB-o88LLvsNtAQUw14l6zuZjXoiYAp6NHFdzIjozSXb0sjUyRNBr5ZomOD-bIaTLd3TZgkPH_i4iZtdT7Cs-Rnxp_krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TygFC0OghHbh1DZGDKMU-7YuKSvBObKUg2QPeEOCUz5DrEbdQwCH_LEibbJNoxVQS-fNM7ontFLiVpK8nHTp7y8QMl6Mh6AtbDswEao5tzCRe5NQxjDElqxMRoKtCO6dt6VgZO4QlHq6wZ9-7Bu6PUmdauXfjUrN4AqzJf1qSW9sCGQ5eXPr9aAN_hw5ZLKM7fpADrHI6UDKw4hXKKR-SXErXVYRCtgSRCK3MBdPau_elwot2O9jVLBBA0B3ICjG-M-Y28zL3J3h4CNLpStGHaOFqQYyrAprO9xcMEnIyRWcYuRN_PWnhMZ674uC1jlnh2PbMcecRAWoDNwstR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcHg-jxHzgFYIIZF1vt-mo05SEU605OoB2GIqYVxMXEjI2ZBFnUugydd5tS41-1rqun25317wvUMnQhNMJhrB5YmkbwMxOyxUGYUJVY64ktP3oXwh48jH4bGFbNS9p9hHVitCGryNihZHytDsECEWFFIClqTmPKO-wn5Dk_-W6lmEmA-Srgos7xZYXfBUNk8nCeyQUusySGF4M_7GydBznsvC6SzOtD_s_k2piMq3F5-g7vIeGWDC9obt9AqfsHlbCPZk-t5So_aBYyvD97y-YIpRb9GfptvzaOZkgC0e_-ZpEmHFwcCieU3G1rWpDpCzvaaYCiA8DMvBjM69r5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QclHNdLBiBVTEbLtWC-zNWhLhbIf1x0bggpXPW8Qz2oYnBQniz9bF40qz3JWJvr1V-j3nCYhuclUISJwSrt9I9urfZr6-7hoqGEEti-KTDhqyhRhnXZPb3Zsr703ZLEWw9qjQ6-DbPZ32R-gjU-b3Doj3tvoqXDLQt30oHgZz3IKis81GJSMd_8LLbQH8GjVc0vRMcZoo06ZfDM4rmnE_UInkUuxJZtY_0Mmw1FNFxHJg-2ztXAFYILFw30OOXaIZwNlW70mUZcmXxXs6N7O3EMlrhBDFI0XPfym2gtinVNzKgGtlHxt5Uo8F_IDdHQ6goxlPF2ahIUbQhrW7AemgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26700" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZgrqZ830FfA4cDC7KmXrsJv9aPRLpR5dmlRIb7VVuAkABhV0iuH5R4ODfMo3m5odAwvI_9Rqb2DW3BDXO3wDTqfohgVddOXjVTxTd0OmW4T3HEfEn9Mw-K_d-fPBZUX6MShIODUkDVuK7BOgzSFISNim6VzG4r-mi_OMo17mhbcefvownxltGlbmkWoYmxRHd5_ky9AD0IVqzyrQmtaTnhrFdnahuFz_LjaNb9lZrtSeO2QhSi8EjedmItwLuX8q0d2uhBAR-k6Ssd5EFU2Fb025sawt4MXulu3479_U2246wX4h3DNAviiRk9g8D1n2R2s7-twgr8beiYZIt6M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B357tKHCB4INedvy_8hxa-KwJZRMvDhJhZ_eEAFuPjwoDvN7MnPDhOO9SRGLMhvm7DBh-FEUwEt9fDI_1-pPh6nex6-Nq4h_fzrI34i0XYNEZLhmoJFvXZmSwwEV4OarV6WOSLVeT-zwnTYWicQtUTSEfKTSdnYQWpRdf1NlPgczikzDA6pThLrrZkG-RNvDWSiq4RKAKVjRhe-qX2Cxn81PSKYDXG_HCuk9YRxVrmRodW6A-wuGhDCawt8MCz1Zc7WD_-JArB4xpchleRvXpCZdO-FKoeyO_gf5F-DlSLzHbiSfC4-vrbMZR68ethYEiyvrps00eF1EHFmo1jjYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=iebvTlf-nvRnn_gCwmJqtT5o_G8w7FiS_UxsmFwHB6n6c1jOEiUL-o1A2NiDRMd0RV8MS-O-usfMIrvsqroKPXUCgBwfnmbClG5-FDc9JFFlFQGSDLASQhoVW4v7yVMl5ZptZwhX6Uee3bJ1FJaEDiKikp6k3Jn5pgkqbv4RbXzSjQz2IkbjprMOimvR7M9vfZClwC76rXWY5g4ytHuNPA8ArqHr0lk6w0VcDGmcqoKuNkea0vht8k8Qi-B5Gyzy1LIdal5kSSCR3EzhMqjTzTaM1uyqHdpCYVY_S3JO2w_dkPskEhnNPa4CqC0cx1H9whHkmxhwqsvQjqLP-5Kr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=iebvTlf-nvRnn_gCwmJqtT5o_G8w7FiS_UxsmFwHB6n6c1jOEiUL-o1A2NiDRMd0RV8MS-O-usfMIrvsqroKPXUCgBwfnmbClG5-FDc9JFFlFQGSDLASQhoVW4v7yVMl5ZptZwhX6Uee3bJ1FJaEDiKikp6k3Jn5pgkqbv4RbXzSjQz2IkbjprMOimvR7M9vfZClwC76rXWY5g4ytHuNPA8ArqHr0lk6w0VcDGmcqoKuNkea0vht8k8Qi-B5Gyzy1LIdal5kSSCR3EzhMqjTzTaM1uyqHdpCYVY_S3JO2w_dkPskEhnNPa4CqC0cx1H9whHkmxhwqsvQjqLP-5Kr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djEXvjreNQP7o05saEIpqEM8t0y7ho_BJj8VokyyOZWr66vPU684lO1Q26ywzDWKdUCCat-k9aLp0OCdtAqMvsv6i3SoHtD6KnSXbPjwBGWrP091m1IHHuVtSr8SkTNFobPoww1409ZLeXbfm5cyG6jh7Tv2wlJgBZk-qOlCV345oh5LImxldUHMBQIPMAjojblxoZN4NenKXImwOaBM5TwR8NfO4lI-RBuRAy3iwgNKSdvKZnhgsIZ8Um18wO3FLGQnECr_u0kHkB9c9r4aOqxTA0pWQkH9IOMqG5XLeVS9pDwpswWcjR8okCrWL_52skkWMMD-w9LMuCUu9kfBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYo4rm-_9rSg1751rEjybeFBLFLal7HCABN0iSdowpli8OZxbV6YxGmNBhRyr6g2_QOnq2iEA2I3ICCPGQuKPcjt1Ys8FSaaRwoktusrSLB5dgGByqiXWVScDp20DpCdGIBb1PvwlTH_LkcLFoL_ENUATDR-ptsnMKyGCjU_H9e4OGJmO0gYjeYprP8JprlY6bBxxxOhkXNUEHEvBWWFqAgOyFMLq6CuxkYEZWSjeRLxfS3oZLuHuTR1rE1c1PpOhjXUlEhBdmqdKZPm__ItC78OubjWuPxD3M1CvSu13weDNIBp3cCOHBdzw6A9Vs7Y6pEIZWJMKMx9At86wfhdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLM6VaobmqvN1u31WWwOxVkhC9MeDyAqFmPDnS9rElXG0wQBTTPHduJjJA2xaj7UM-nkW1wU1-MVTGA95qKMXB5jQSYEa0siZ-4DG9xps3a8GXe9VAZx76rdH8tMTNU2tLmQZLfNB-SWdpgd0FLFVuPEbKWPTMd-yz_V1ORJ9tUjdqZBGLNnTKXrhYuNdzpjaPehGGCqP2IZLjE67ghgXpMF8DDmT_moV9b_-E29rTVsp-Q_Zwb9fbFyL-a4jFys4brfUtUPZS-RhP8PbsTUjG0AO01Ljhs9h_EKDSEXxKISZTvSTuhNF0VrpdOoti7nFa9AXucV6KS1Jy5w4s4EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=rm2qGIit0r4ltYcy_31JFTUu72Kqwq7KSPUh8HBjKG4c1cK94icL-pOPUfQX56rDQ9NO6nB53yL-xdPJ9lAd4mauC37ctDQNNxriE6JooLuGTS60HGZ2MhAy48iEBkopzCtELAshEOEFQyUbjVna8nam5aJ2UnSO7hRYOXrJnlZ-eYsx6rWPJASJnVEqs3qTJWkKajOQmRYRDG1EU5KmQAqOrBOcRE2U4EXMH_4B-2hRgzgi-HCvKTIVkJnL8IZya9ODvxGDUTt0Nh2ZgLhzCq3HqTOYFGzzLtOyVBuGuibNO0OC5DmBR2iKfbYcItdEk5IDRk7_3MOZFcFpKVdYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=rm2qGIit0r4ltYcy_31JFTUu72Kqwq7KSPUh8HBjKG4c1cK94icL-pOPUfQX56rDQ9NO6nB53yL-xdPJ9lAd4mauC37ctDQNNxriE6JooLuGTS60HGZ2MhAy48iEBkopzCtELAshEOEFQyUbjVna8nam5aJ2UnSO7hRYOXrJnlZ-eYsx6rWPJASJnVEqs3qTJWkKajOQmRYRDG1EU5KmQAqOrBOcRE2U4EXMH_4B-2hRgzgi-HCvKTIVkJnL8IZya9ODvxGDUTt0Nh2ZgLhzCq3HqTOYFGzzLtOyVBuGuibNO0OC5DmBR2iKfbYcItdEk5IDRk7_3MOZFcFpKVdYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTe8NW62ZhnFgVYP0QGQtiyHjlB26z-vQ9uBLukXunDmjG8POWEBHu-_RGAD4VJnbYR0fz6umOede8U7QclRlZf-AYp9sQFpupV20UjUW_9LKJHByR9_PI8KnmgqbeIhaEANmpYDHQKFSVvB-QtUhJtFTO0NJJ8eOdqUXpvat9X7ZH1CCxdod7C_Vn3pqu4Cc7-aiEWbrlVkHwTrptJH7tadXoNnyRjBYjWGgF3plVivZvxhbAb1HNTFnC5626Rm0-YCThRu-nRrI5_qFyWkXGe1AfsSV2S-U20XAa3WrjVdo0MuRQ8-nryTyz5CGLognORPNpexqb8VL6iJhzaztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj9TXEvJxVLXe-Jd6wUWm_j9ddHRGP7vZvbyWm6ySO_0yeXEEZYY46UBlVsFu_i_wFYCyUJMwv7TJO1hV3qreKNHLcL6ttwN49b4avidN41dcPUMVkHDKbFKtt4WuGlGxA2FBzmCajd_cGVGQ9N0JuPBzUklCJrCDzBCHZYf3Y9xDPjusggJlUo1Qg5FxCNKlkQCEwqpb65b3Nn11GDjtSyY7YWIOX0xpXsB_V8OlluGksySeBGrw-s5Bom7usCIgrbqBjqXPCSkf0VeTrSL86Gne5xt9XFe5Bwx4m2PpymHusk0gFXYMvIMCIY_eYq_CkMMiL-9jkfDx_1iyaKfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8ilIPrNDWPeMDxPerXziyG7QEf4JONT6v6ftjit5QeTJfci7srcBCp3RAwAcKkY3L0M4AUlP4mnyTB-kZsEZrZ-0-JWRgzQm2SWzKabYoGBF9_oRByaUyvh_5krrTElBeLi0sMi-vNhgd1nK6AYGntPODivALWi0B32VfL1vikLlL48UPvDrPAB9UaNWePxHwsn_9nukShrCwY3zSfXKDNnAgaxyWKYiTTw7VjlEmNunAcmqLK3sZTPPEVokdjJiGWRrgOG4sCi9MoHcuvt0uYw_G7L5HeTEZlchsPBANvd99J7c1Mg4H6yXkgZfcGVcqz5eTdGtNK_jHHtWhcOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQzJ7vqbySwJtX73drekEBr4NsZ3ORs7wGjHTEDZ8iskghErLAFArD0HRPLLtYfHEdZ8TAXIsvmJgc3DwvwPPuLxKh24cMTDF6wxrleKUi9STJJDn-o7Ut3V2nieERAYM-E6AiJ9dauM_snGA7U-CrIlsbuYxZIRRaXx2ZXh-C8-SmonhqolVm0Qr_CoCzzJxAZowieV2zJzsGUTVbJ597rTXgm7SPjrlSIby8ZYR8mb003yV5Z9gOzbBFshY5bnoCiPo_UVfCbl6ac-7TYy5rHNp5RkBfVPZwOJdz1ZKLGh6XXgqM8lrgpkOqiK8UmH7RFxdMugkt7iBB7wxplBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RufdMzpJ_JscH7Ty77gZEE1WiZc9np4gNIc-igonI6PgdJgj2cKhDBLfesGTPy2JNkBxmc3pX55VPfl_Iuift2bSh8LQAdVR-rTCq-Hs64tT9gTg-7qDSM5m9JKvZaiGvlpLkY6N1eYFVY37y0UO7YeXT5F7il4wv-k6q_hH2Nbe62P7cCVnTSuzx3qOYrMvCpW5-JsWykSbOQu8DOfdaLkDrEV61mhezs12IC4XsHGFzneOx1iR1aS9NxwRi_FBJhvlyOgLtHnimIwNqzOMQrP0ggCrcheajw9P3AoLqvXwdkxWhJz7x1qHvsOVtBjg413EXKldHYPSF0w8Nh_rXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfJYr8yjMUNy7sOmGhS7dF0dvn5OlInBxfBPkXZ8Br1iJr0IJ36TWqLNGmGqmFPVZDtsyi_io8zhDlcKKKIEaUSXDKtGifFFHMTqk0-r7W3_DtgLmlo7yvLriIs8rZ9um9-5GYFRK8MRPEp5BMLtlFbuXjdbL-rsFmqCW6S0zEPJWtFRB4BuR3kBxilOEOGven13hvGloGZRR7aZQ-l46nMQn01DVA_Dmt9_9gkIDKmO9k9-ywTRFknJYSfYY7kM74CdCwD_lUbC4CRBs5LIsud6DOI8PvKov9MQOMSV3kuwZJqsdyli3clxBiQ9NZjJr8cP0mS6EYHe2NVTK2aFsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUKG9AjA7-UXR9H_WQe1gR4nUWRt97CgwGZ0L181ZgDbQfGuZs-nFWk-Fcw4NWfahChMCDPV77asGvL9_P3HePXCloN3C82aAxtaESVvj4mwCGgr2OCMSM1RfKq6aWq-WhP89dZu-D4ACi_1A2Zcyki_l6w4Xi9UhthY5SCxYp27NutAkXmOhLA0MMlZTP4_xeu8wMZ64xCH65wiEsbZ9BCKCbEryngKY4Ouuh_NiahSTScNCVFPDINlf0t2rIt0iYy2pA3wgZh5Lyzswp7bbGFv0bLYT5-mj6SE6XlWsYfGHB3yMl1DwoF9TWyEnwND8B8Xs2RF7gh6-VpqxyZ2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPwGmxS1B6ksBWazEta0fcES28m0-U3IiQEbak0YL_w8UVbOymFxklRtpQ0Nrm1t6vzLI6SkpIC8ARnixUVPog94LPjGojFmhmIDm57diWqxhQs3UPNkH0FDb7BgAnCyG0z_reZefzJfuVNF61DHUhLoduxDHnhQTk-kkSFb_7LM7wdu5r56p14i1xr-xeD-XBvP5JukMjBMvg8gZHv_WRI9657uB05jvXjX9_Cw2C0iMxpPTs9y0M3BilHXaWphp_CuqZihDN2OvoxMUnohgE0YHYiVNqkGiF4H7uYGUAzXrtF4DDSzBkfxr0V7-ktxLBBLvgdPw4Sq43UEJJXCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIJ2wdf4IoXbyxKAY1jzOMIfKp2-Sr4OzU6wCqfuRSxZ2iOowjbesxQuVvP04JzOSQAYvCilt43IBkfBL3yvCWCFFQxKEM11nKY4RoKDrcqXFUPQP7CXwcaOMFZg3vsmdF3VceUYzni9EkqVzvpYE2HpfeTwyqRAMCuCMncCBZeXj3iWQGbcd-tmYXPBR-VEMig392nxu7iGvvUWz4Q_FmBZCSoDDXvkxdQ086TBmL223dR97ardgC9v-l7ZKb2RZKUJc6pofKOYsMAJcKPqOiFSQ9kxer5mhoN6OuHbeW5Xwo6FhnAA7zBBStcEOfNu8PyUh3DB0-pZADcdLo8wnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc9IlSlWemWVNmjetQIS3ahen66oWCl5duW9QXlQtyhzvCOVG85bYal7Yn2MzX8DfuaIDVQP-qGljFS8-NhUO2WkAOzwB-pLNI2sEgCpTuygHnLP9BEeYuVJ0ms3c7odlyTAN5K4Ft6ut4ZT39B3zy3SO_a7s_y2IsPDHTy4D0NncHODsp9Jo_PqzhePUGqpsBKdl0rvuxzxQBratQEKZSb1393kMYk0OtBQcuZS2plGTQa3fXE19Prb5m5hH-euD2kAqjeyMoPb-d94hECi_BQHFWlzzkoml20E_PdqatHyXPAJxGSsVeCtRl9Ai5OcxxP7OSiTrLadUWoKmSjhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXOAG6Rl_mcm7HBzSGn8bQ8IeyJATwtVybUmoy3PL56aFd2TY3r0EAcpPBdz7vND8RhaNRSlx9960DgAT6Ucu5rhtiHv--7NYlTT59SIUZIehN74glBHlyJjnyGLTv6KBG2HydqodvxrPcFyfuDO9y-6F07vPAuxQ8Ul9BtaXA_94ts30f2flpTxsRpFwY7Mh19FCGAmlDd1huSmn1wUPMk7pubJOphSIgedNN3LOxV09N9c0hyuoS0KHxIIq9EdZ5zDwQx5ObVRiRE2wRYXK8FGlVMjXcwdRAdFfSty6hoAsCl9uVFX8WoP1MfS6hPFsTMW4MWolj2DfyY1xAQfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_opmX4xqw5oCtpz5ZmK436pRcoh7HlmTwGwyjws4WCjegElNExTA9-9qyt_mnbQeKLhgdOZjq8rk_QU0izyuhZ3VugtXQ74Zu7lgcd9wN_CQzhA7KnDQD6lmRVUmyb9XE-ccop3hl72blfow7ciG-oUt0YYr0jF7N4gfxdAfPBXn6bEIb3Npy4-VxaUiv9sHMMJIioK-ezojrViBQHrP3pb9BNce46mkDrVeBOkBb7Jqz0XbA72Bv9UGaSmuAm2kwOUeFKkDwqfjaDrsj91Pxh-3BdeI47sAcFt054m3CxvHMT8ZSpudfDxm7vkE67QEWOwrHpwgQndfRxHrLU3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te1yFflyFmKCea6OLvZOa_n-O887YHiAjujqGULaZKVD86P7k9BShDUxVDTTK3bh3zmc-GvHtKRPXJ81kIgMdZMM-5zJL7akSLSyLyylidZh0sNY4dOFrLxG_ASyNc7JOjuPy5qhMwI_eoA0s7od3NabdAtkpItZHPjc-K9_fcIeIGLcQy7er8mWEfkKeCARKBJq9vBE0w9wTYBUkyBh5MQiBGi-dDPCx2tszVyFz9swaxbBU5Wp6EOoZZWCx7TPuR_bD7oVtW7pKb3CLUIPdPoul9PB9wkQj7yjl1jwYzQ15Wm967JSmUwlOIRWbhuL_EF9d0zgwyI-1NhshjK7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxx6c27HQ8njdjFKQoIW1CmQBNEKmq3Q3h6zI1uynxitci4CfC3SpkqVI6yn1rSBoPMuhCezy6ZMZ-0mDDYf4xMU3Yl4SvAGmCjWaK1NL_UcOeDPMkinosV7bB3jn-BUj7i8I8sfA_bGWyEFBARHI_YBW1bH4cEwg76YleDwop8luxmuRmTImb-oiwj8_yBmdRawvNTPZbCgT4wlImyQkvv1SSmsugZzUbRjJDWSyGPWFIBaawcoVnaBzfejFtlR2zAjNgBlg4wpoQ9SZ1a0DsZ8TTmWxJDazcxxkY9GPO_s-CHHrPzfag933EsAX5LKHSKRnWcotCCrwoF3omPwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSOE16hrFtaLE2-_MqO_lJatpamolxCn8lsDh0amvgsibzLNx8Gnw0e4ysEOEDN7L8pLgF1Z5cN_x4q5AB9h7FN1Zrjuc4mLz3RXYEzqzhV37jAWfCC7DH56dNV0fOWksq0du8786ic4xL9i1BhmNdNl94kvwVrvptsNmSJUkY_SsERltv2z6PGMlFlXYVGqZxHwrjv5k-ICmKNB4yZybKa6IP-_zrLWEdeIIGqHIkW20fc_zUNNNL4tlqlImuNPyh8ZGhkZtqJIY_ldiCtndBzU2CkQYr64vWzmnLLkFW0e1MPi1IrpglMlsPGCrbwt3GRFt9gfJSOZmiZX-Af_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmdoNHRy_Duqi1o4NheSb1uQduO-1FRg-c-B5RNSRPhmNsoT6Sxr0y-IJibQov85RDdc-lqzglSkE2G0bVlMp9EPzsWlOM-mWvLzDZR6XjC79QzKt6A7Q1c452erpHvMMfMLO__0n4ci75CfL6YTUdX8ynxZxIZjtceRNVSGO9LIKymkumy20N4md-l_WIxbFfRcU2ZKwmlRllOLiLTfVjKULJxV_MumVPQE7ehvW4EzNWRCbq75ruhW1jJ9ADZ2qxmPvVULlPJcVR2UsnuL7HGn-4-mG_eyjKx3mifjWTw0vG0b_DhrNedqYKb5gqHACpx4HzX8KhyEh-AYVF8OVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZyOHWbQOczma0jeDmmD4uGO--5g1hhCdvL8Q-U1-5LHjb9aQkzDXEbMfJBdkrDzPiW9wZtxBzsLEjbO-8GVc6s1qx7Ti6QHjouL0W997B6ofYrTTpKnSrBFOvecufDviadhIOn9Bf595ywoXAiUIDGGEL-G6BggfBr0-Cf1h2etAn4aVLbXGwoUuAQaPExJptx79wx-YWYF_R2MDeAX6Pm4AMzUvTW7c3KlvqDa9lOWEuiALvUUMELGj-0Whk6ztz-bwtVddb1rpJo-mcslZ2E8_F-SCwi5jKGrT3fY8BTf6w2O-Vk2i0ggXD6d2appuat23OEp-hkA7zWs9eYdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=RGfsgq8zRnGF05PpSoCb2N33qdD4aVZkxBKen5cDEzB5PGVBAGb2nxfQXUFc1XsOrD_s10ZHgysJbZBhx5K8SwixQY-zlHW6FWSu-1U-hMkRgd3yCppfxXHXUz8HhjUhOO4Kf5rACycx8YgL6gapRBpc7ML87QJSYjekfdupWaFOlB5aJDY_T78o9MbrIoYRCGLMz6WDe4m022-mi8p5-o9aMlAWTl8iLprTJLOIwOE94TUSRGiHN3qNkomZqflrovkSk9xJKmz7kV_S_hUO0t2DKK_j6D31TW0GfyMh6UfOcvYjKKTllZ0qGA-YV1rSyUajSBH9dD82566UD4hSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=RGfsgq8zRnGF05PpSoCb2N33qdD4aVZkxBKen5cDEzB5PGVBAGb2nxfQXUFc1XsOrD_s10ZHgysJbZBhx5K8SwixQY-zlHW6FWSu-1U-hMkRgd3yCppfxXHXUz8HhjUhOO4Kf5rACycx8YgL6gapRBpc7ML87QJSYjekfdupWaFOlB5aJDY_T78o9MbrIoYRCGLMz6WDe4m022-mi8p5-o9aMlAWTl8iLprTJLOIwOE94TUSRGiHN3qNkomZqflrovkSk9xJKmz7kV_S_hUO0t2DKK_j6D31TW0GfyMh6UfOcvYjKKTllZ0qGA-YV1rSyUajSBH9dD82566UD4hSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUGMAP0c9G1u29s6DvpdMKyhEOhg6FWqh2FPs-_oIJMmmgqfRNFMyz_iVIqZScwyD3LuVlIs3sjlhg7Iplc-K82FBid0PzAL9UKQhK9q_y1XipKOsH3sBPldRMbewwe0iRs88dF-ca-ONuwCjAj_T0G-MdZbuNrCjgkE42mqyeLyZkYA8Acoqq_P-uNnszFFJV1oO06YHzX_vcehGL2jy2sdag6ra-3ZSpVFMFs0Q3GqfmgFv7RdjkyD8N20CyfspclUSqAplyxMz4DK8V4IDHGG0lq16erfZcJnDR5OQtiqATH1tKF_5FHZP1wccU1ThC63cB-xYjChP3zo7w5jLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaZkp3Qg6fd3O0VpGKXyhFtxvU7fENBhNMUA1YRyfoKKY8TTVDqV-C3sckku-igrMYktcndExnhUSBIOJRsMGLN8VdxZmLIvsWWgL7lOOq24fulq4eK9aXn6LqJxEw7IKBpMnVuerAm6n-XycYkvbG0n12iBEwre7piUXiw3fbXAX0zMsY1K9tFD8s58UJeVs6j13Q4MoY3Wt7DtpEOpNYSDbBX7HuHpfHxFGIj4P1h9YAoWmGj_LgOF-MJ2v6EIxWLvV5Tu-u3x7Vz2hhxisnZ1uw72QK-7Qn1Qg3q6rKQ0RtOSVXA3KvAoG_9AH4FX_d-wHWGDh98NkpptLqezUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEN2qiz53XKlRIKGDDgqmQQm-qNBPufwcdvKKj_UvyZJ7GKrOHVof-1OvYthHpijp_5RG6Yf8vLbV6IHBy3AOI9PPsQCvKlpC6Q-eENHIAJN-ru92LSLS2vndxvpxzpCiId6wWiuSvZIpOm8wV5Nb7idLKHgTslp6TpPUyOTfKyAOmb95-xZKzViXNrhBOYxhGI_pzAeSKD-DifEpNpm43PMDW5QHtWtPtJxiSf24tXxxpg626JPSK3cNvH6GfB2gOF4DbVgDvUsA9-Fksct1jfrKYvXUnz1dY5e4fLIwDw5bKF_3axQEr0_TAHgHxiz8q_jn4h9SaQa7Pj48AF7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmpYGqHC96Ys5i_oxQqOBQV3gTA9vvSdOvHOVWa3PdCms1Y4YYRktUrF34tLPInwg3fxKw0NHSMb-xeQ-xYBUqyK3-ZFcj0HkNzxjqe2KO0Kr8an6QULwvF_ulR6od2lNKqUaJkFl_0oNOp9IULVkBRt4SS6xNXhBW4Vusg-XsnEOfzdANymk38yICx3yKLoWMMZc7KbuoR4_kzrBIABvOERNBgZ2dLehcIDVM0KLTAcBD_LgVfzlndCsbZWwCLumZa18aoojTt24MXMCwXm-ks1pg_qzeVFGZgZG0oEplDef-BxMJRpE59Y74RTAhgNIURrL3zwZGhusmpqo8Q_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcMNr6jzm6oLSxGYfEjU-qBX7w80S0Tls1KKBi1zZDJRLfyXuZsADjN_z8W9HLvsDvqyPrQ2uT-a-GdmLtMIi-BI-p0FAdwdIrO8E1USs1ziFdCyUYmbyUltcp4Su1iWxMCsIo-JEF_QYxl3uZfKzehpYRsNC4qXWfWcPpjAzCzRbhMatFP6dui37D-ykcce0uGkboN_wwLP3YZUdqZAfExabcsbb1LQsdPMN91x49GBvoZS3g-XBHpshb3J5FqegqTEzho6emXSxvObqLLKvvpfGSfEJs4Zpj0ELCjdiVQnUocBbaW4P1ByCS6GScPVJ1L3QExymyKUPNFFYtVWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfljhlGvBV04KzrlycUc-_c0UI0fmfXxOWD74rbAjt_YP9GdzctclQiBTAxueeYdRc1w3y-3FOa8mmJzs2upLRjLkDVuXgaM3I_q0v8pyzWOYWImeSscCCqJlF51k5IENT5xXwazNISslbJ_FGLfqh-84xU_Hpyavf5gecwn9llAYBPO9DqneFhPGfTWYsr7U1sK4J7TjtJcskcGQY-B8348m6XRLKnrm6dWqUUTrsvdK10Nahv6mc36-dO9MZZ5A-z4ekoOuXmaLh5kXKfwhM20vV8fAsz8kRhQipEg_X_-w6u7SxQjDls_TAicgMA4fjh2eXi03rtCMO6Dam6xbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=mXqnD0rEd2kcvne-g3wW9V0khhcl0YIOidX_57TjYHiKzcWGuo6odQ-O8Jkg2e_BZLJgPE1VPO37kMtfbL8eAecOksLxyOaLc1ejFbg2GCOOsIHZGeoQlCGP3KJ_yb0MNlIw0dkRhPZytT2d08DESkixCxsSfcIFVzW_CjLPQJQEF-YrmynP9K6ScCw79oMIaFFaZkciXL47EGxltH-QoWJ37O04cNpx7wWpxRnTmQroG_jEIFUv4Verxp4iG0qk1gNjwVKMd53OFppmYvD7cbajXyuc-8NXHO5bgKNJ3V5gmrkq_EVAPoX7B__jdFCX7hcVWi0xOoMs9VJGycBASRMZMblDwOa--wDqLhormd7ZGs29OTs0j4jcyK7a1BZNjQY1WHI4RpP7Dnhm6YuZY9YEB9db3ilyCNZukF984WHso0Rc4lBnFrlV8w-eK6qpLqvjNtSlcCqXfWGJPlB9yYLEKUeduz0Fiqu9Shd5-vjHuh48_ruixSFkhfWIzZ8mRAAYTi3oUQgECzJd1CqK_I99KKQdElS0kGCbw-Xo-De0_Ay_-b-bIN0f5NbpByqvlo7XXjrZnij1hlC-VRtE4G4AwkyWg0XbUCxPDP2y71pFEmcaI9QF_Xit3rKqeb-cYPnxXO6R4Uhq2QTBQCyvqu1gNpRFmvpuCsWRfRw9Tak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=mXqnD0rEd2kcvne-g3wW9V0khhcl0YIOidX_57TjYHiKzcWGuo6odQ-O8Jkg2e_BZLJgPE1VPO37kMtfbL8eAecOksLxyOaLc1ejFbg2GCOOsIHZGeoQlCGP3KJ_yb0MNlIw0dkRhPZytT2d08DESkixCxsSfcIFVzW_CjLPQJQEF-YrmynP9K6ScCw79oMIaFFaZkciXL47EGxltH-QoWJ37O04cNpx7wWpxRnTmQroG_jEIFUv4Verxp4iG0qk1gNjwVKMd53OFppmYvD7cbajXyuc-8NXHO5bgKNJ3V5gmrkq_EVAPoX7B__jdFCX7hcVWi0xOoMs9VJGycBASRMZMblDwOa--wDqLhormd7ZGs29OTs0j4jcyK7a1BZNjQY1WHI4RpP7Dnhm6YuZY9YEB9db3ilyCNZukF984WHso0Rc4lBnFrlV8w-eK6qpLqvjNtSlcCqXfWGJPlB9yYLEKUeduz0Fiqu9Shd5-vjHuh48_ruixSFkhfWIzZ8mRAAYTi3oUQgECzJd1CqK_I99KKQdElS0kGCbw-Xo-De0_Ay_-b-bIN0f5NbpByqvlo7XXjrZnij1hlC-VRtE4G4AwkyWg0XbUCxPDP2y71pFEmcaI9QF_Xit3rKqeb-cYPnxXO6R4Uhq2QTBQCyvqu1gNpRFmvpuCsWRfRw9Tak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9ytnIW87rY6PZZQm-hdXEn8PMbhavMWE8ZlF3WQigrKF-joRLW2rQ6St_35I79tj88nKDFp4JdR8tz6y6mn8n-VL6XOMVjYIT4DuBbDSHfBZaI4dB1JizdQe0vDCg6W-UkwCsOabi8a_pabpct75xxZzM9lisVf0i3eqeGbu-0j_YXyze9zpTPVrE01qZeTNsIjgdrjnYYnGGeLJohDjVp60dxK_AfwaVc315_-cWalb7-G5Zn35ldehbx27oCmGzPsk3D_nxQsIKLz0Mjerv9H-jU1S4rRooHrFEhOHrVNzu_Hn7w_juR2ql9qYCxhhBjVp4OpdiQcJVXK4g4NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSxkccXY3pNb_9dAIxC1LwmwqdkjkAScCUsZS80xazn8aQepPx5JJ9tdPU-wnJCiJfp6W0K1MgyT0OCr9w64LiI-fbBv8-hXaENhiMp8mkvCguKMP2f5yNN23VtULeQXHdMFi48fKNTCmKKUtO5ytn0-ZNrcedqJihJRimrDPy9vbb3Y8XX3-aY0xOIV0X2R5G20KCd1Z7uqdxKWSFB1bfc9Ft17RFN0g8MB2iatjFAqml8CpHUYIsTCD0FDpzIL6vZqiSGMlj_Ml1syRVS0vj4Kqf1tBZiwM_wAA53P1McDsqDFAJkdxjuVCOwVs8d2_7lgd0GESIuuTGDvT_1Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mspMnUxYicZf14DT_XeSmXM9IuuOZLWKYf2WHUuxUh82Fqs4mskFLfkipgkv0T1yp_DSIIPbv-M5C5T5B5lvZxMf_x1ueGtVn18OiEaGDTqI6tNWFTZBbTSUMv7UkBOJElwhXHSJ8wc5B6WFQq77dfn8JBGrzyhHoV3ChCgfqVXiwQJBssUd7B6H_PR4_IUHyJrr4iLUO0-uriHFmELGT-roA8w_FrC9Iq2kPNFih4LLE6BamwmTR0wK9-sLXtuygALOIe4pANmnh8J_EELL25wB9lNYd6-5i8DvpAZDEOU5AtPTKf9159Q042-8cP4oPujjEbLdME5QAq-EfHB0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=Piq2jWWDplkTZiPtPtwzXpobVPZYrcFB8jd-bJ8MkELijK5a7pfjujPwKx_s8KCyJXKsyYFE4pa5FmiOZyac91Jh8f-6N94dCMG5ZZkGP8wHRsW2856QLzPqURqucxCTITSp-zfTrW-N3aAvurIToLfiaLAULj9tZpKfkZCmmCtvT5l9OZBsrt8O9IvgdBUmIJan7Go9W1MqXMuO69YNIBo2POeTuCihk8qxZ-OTJW3zgzCT6bNZiOeP-sUPHamOwk-0TnvIWhHTy4H0hmCBe2DkUBUSFyCFRbfJE_0ngligS4lwYdiKmxAk8VRQ8iNr7haA0s3t_bbL1VB4QhPpzwWTPn_kaF1QeH3hgxM4E036JuBoWrcmF3tGZMA85rnWVG8wJaZGTviBDokVfIs4rQmumLQE5hqKBy0gtC9qWonmFF4ers39SqumcntGF26eJnQpQiRNpkYibrpCrzo2QpnsXiMsSEXcRUFpQZrHpH1XXtFlqOG2J1Pvd6bT6_1xXAPZR2z5YHalCJDxe5ppykBubhOjhzoiye7rY-9Bu2_c8Z2SABU1zJ9pJXsnR2auvU2erW_chs7BYiiuP0QGQNnvR0Of0ydiKIwzSkZqx6dsDlCR_WVhTsYP5jRMGFbFPWLdJY9VUKrQhXpVBhRr6fRS8xFEHOR-o0pd2ZllwsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=Piq2jWWDplkTZiPtPtwzXpobVPZYrcFB8jd-bJ8MkELijK5a7pfjujPwKx_s8KCyJXKsyYFE4pa5FmiOZyac91Jh8f-6N94dCMG5ZZkGP8wHRsW2856QLzPqURqucxCTITSp-zfTrW-N3aAvurIToLfiaLAULj9tZpKfkZCmmCtvT5l9OZBsrt8O9IvgdBUmIJan7Go9W1MqXMuO69YNIBo2POeTuCihk8qxZ-OTJW3zgzCT6bNZiOeP-sUPHamOwk-0TnvIWhHTy4H0hmCBe2DkUBUSFyCFRbfJE_0ngligS4lwYdiKmxAk8VRQ8iNr7haA0s3t_bbL1VB4QhPpzwWTPn_kaF1QeH3hgxM4E036JuBoWrcmF3tGZMA85rnWVG8wJaZGTviBDokVfIs4rQmumLQE5hqKBy0gtC9qWonmFF4ers39SqumcntGF26eJnQpQiRNpkYibrpCrzo2QpnsXiMsSEXcRUFpQZrHpH1XXtFlqOG2J1Pvd6bT6_1xXAPZR2z5YHalCJDxe5ppykBubhOjhzoiye7rY-9Bu2_c8Z2SABU1zJ9pJXsnR2auvU2erW_chs7BYiiuP0QGQNnvR0Of0ydiKIwzSkZqx6dsDlCR_WVhTsYP5jRMGFbFPWLdJY9VUKrQhXpVBhRr6fRS8xFEHOR-o0pd2ZllwsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAmMVQLM3eVqfbGb0rZ1z1bqwy9AWBSTRNzspfP4r9B2M8x0jVWSdEX0QhFHUMNmEYeDEDjvK6IfOn8Vh2xHPil7sqRkcIDqYFAw3Mwb1QsRanI7aluxSAnfGd9NZL-r11pHNFfYxpeCfsEL7Fjkd-vPzjfbXg-Fnjl6ML0YyhHlCj8E78FeG63Ws07x6pKsJh-HgrXwZ6i2SZdV_RkGSSEEcjeg6M-bThuRIeVS-qNXI5Lpkw7ficiCEHXqh64nLVtNUhPbKgcw_0aBtSePJ9Qn8mdEP0pL-Q7S5qrxVbKGSMvOtip22w-hNQbsbvo9ODfWAt5RCH9gAaSehLm9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX46g1Fuz2iXadnr2BT6Gf8LCgQp76Zfstq0_Wg6dP1Z9dCEY9-vdjBK-5V_UOcmRCi3cK1W-HixwvLeyaM-drzWYeSJKJsMJO165Z9i3aYdEtSC8xVTaAmvhvogdBR3NbIw7hKBvS9D92g0d6XXy5qfGxhIGItZ_Z9omBjsFNBmm6JOeUUapfkkIIzYWs5We9eMgHROZbU-s1e0ryXx7dIjZaOT22A_j9w8FdOYghG71PcswZNjvpZkiOJuCcdqdnxUoE6CmM-tuzT4UcYjXiL_bWH1NZf86c4k-wYsRu_PM0jWYWrwQA5gTsunuVyxGr1B8lhwFN8FhGBoq7OAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=SmpGmQ1eE-X2eY36BIRHIDvA4ivW99sRDqubgSJbEjPm86FVuJpv_vYbOVw0MwLY-zuEiDutma5kgFLndrcPvWFs8ZVLBnGkmxm3bqA1FSOCjwgBiJgrgQlIGuE3qqNEweSDtLSR5JezOyllKzCiwjDa2XsCEiuKo0j0IXDxlU7GX7l6NhNqfqKyGA6s_CLRxyA22-yXoP6s_eq_Ri53LGVzItoosGGJ_-LAyoyn4DLqSNBTbcJo9tl4Sm6DSlMu8ZpSl_SrofnaQ9bpqG9CTTiZZq-ZaEBbbuchibYrd3qIZ-CHS5OO-6LXhu0nvRsw07fLYQoKTXldl6kN6tHLaJgzKoI7CiO3iQWIME-KdkWVV-oXAlvDgtclVWtcoK4zxSWXkzKztaQ0ryM-hmnKjNTMXVZm4hhaO6s13BuElyz3Ed9VAX_T5WUnFiIC9vjuOr_Nn4imHYjLReEXX0lj7IheA90BheVQe6hneLAG_VfriN-7frn2mbmqrARqoaKCFNAAMeyp0AUypRuCBJ9p9ZneuDUHgMpkX4nvp27ENPjNy8JPDzp98HZpJox-HNeYuU1X_A4WUsSOnXcXNIE6IoXcPt7WfvyXn3sD0UzZU3rR_jv6orfAsBooyobPpYiPmW5JMSqOGAMePEB-VNrUoD31ZuaxlrHSBpulSDABS_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=SmpGmQ1eE-X2eY36BIRHIDvA4ivW99sRDqubgSJbEjPm86FVuJpv_vYbOVw0MwLY-zuEiDutma5kgFLndrcPvWFs8ZVLBnGkmxm3bqA1FSOCjwgBiJgrgQlIGuE3qqNEweSDtLSR5JezOyllKzCiwjDa2XsCEiuKo0j0IXDxlU7GX7l6NhNqfqKyGA6s_CLRxyA22-yXoP6s_eq_Ri53LGVzItoosGGJ_-LAyoyn4DLqSNBTbcJo9tl4Sm6DSlMu8ZpSl_SrofnaQ9bpqG9CTTiZZq-ZaEBbbuchibYrd3qIZ-CHS5OO-6LXhu0nvRsw07fLYQoKTXldl6kN6tHLaJgzKoI7CiO3iQWIME-KdkWVV-oXAlvDgtclVWtcoK4zxSWXkzKztaQ0ryM-hmnKjNTMXVZm4hhaO6s13BuElyz3Ed9VAX_T5WUnFiIC9vjuOr_Nn4imHYjLReEXX0lj7IheA90BheVQe6hneLAG_VfriN-7frn2mbmqrARqoaKCFNAAMeyp0AUypRuCBJ9p9ZneuDUHgMpkX4nvp27ENPjNy8JPDzp98HZpJox-HNeYuU1X_A4WUsSOnXcXNIE6IoXcPt7WfvyXn3sD0UzZU3rR_jv6orfAsBooyobPpYiPmW5JMSqOGAMePEB-VNrUoD31ZuaxlrHSBpulSDABS_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/errHw2LkHQpSOqPwRQGKicx51M3PTVuyQ8uU9rKAupgFi3DZtV8ds0g4pJVhR1CNG8H_GuwVHnt9jd1gmDuXVbLegHS3RjnMCu3294zrpetNJBRbhZZw0Om3YNzxGEWj9Y45ElQYf3xpmAGjmSy8BHGl9YRJJEFurODtZL6f87vgRG5MDbubVWdFL9Jr_dgd_Mo7I_biTVabeGddkpiEW6nRNmObtdjdpXCZXPvsA4umoSjntYDmroUsjqJki4PLwrnPcM_3CqdCDh7HnVJP_kNIq-ZLs9jYDD0WSrKln6eoylhE_K5ysUQpO2IMWcjZcqcqhEGGEOjwPGWMtBeaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzrWvFsmnOSg5mYFm48QiyLrjDXB8JhOmGOiSBgcGGF-qi-_RfeNxFggfGaYoOp7P9WSe-M-pGH8RMWjil8tSyC5-B5vUivSaXm-sy6obQ4_qZPGbFzZMMdGQWXxBXgXLHAn3qRtSBQsQqVbAkxY98M_Wmieze-fwxoUKmOeywtKP5MHwdMO4FhoyG9lCMdb0L-3QShZsOravEjvaTlMFzqhmcL27vjvD8Ndy3Mhn-5-ON3LlfZsv2RYQrgZ-62iiUNHTg_OP5ZA4fjmjzxZ5QgHPMAbfHVCylm4XJC2SZSEzDMJcY-8isjB2xy9_hnz3m_QjZ0YizXS3ljUnBh7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3uPfyPsyJRQdVAL12XMH6Cs0w4LJqHl7nVuBkv285YqhOPkcNRVyjPUO_TAMFb6Be3QVqP6WkqZbDANfFZEIlLnXjZdLUNjTlvRBg7CFGtwzREczQCVx5YRlLOK5uDwwaZyOKaxraaV9O4b75cxP9WMVNghAsDzhvM7Bqhjl3vWA6a0hd5mhedgcyZQXslkElCy_thoEsdin__Y1zcWak-Cg8M2SAIsGGvyJ_pvNzbuSjC444JX_cy776nIsnWafbPGlbcCPdxEgRubpSLezz0Ky_bDDVbRsVi7PdH-n8_ab1Qlsr4b2nl_g2DCNROOGDye_wbP7J-uZkQF6Vy3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=bbf-fZu6f1UFIA-egsbI6b4aaOoupEoQtuSm6XAj6AsvugKOvZ6oWWQz9k6OOlpl4Hqgyu9jBLArGaMum_rgoB4UtGg2Oy9ypQFVeySWGaSS0b9EabB0tLl1HD3gwnbE7f3n1Da8wTyFP3e5z5WPKHC8Nsn2vX8RZ3zbtqX5BB5wNek8ufUpdnF17RS-gs4aYY7JLBcwJc5BHD4DDTxzBv7p5W2qzCVhH2LYI_RKCMX2x5RqQj_u54HNvtsvpkXGd6Jc64s-KQjB7Tk7fSy7IzZ1Vi-_iJHku7NYM50U48Hxnmv3V9iGneUyMdd40G8yDArWnovc_AGJ8S-azJfZNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=bbf-fZu6f1UFIA-egsbI6b4aaOoupEoQtuSm6XAj6AsvugKOvZ6oWWQz9k6OOlpl4Hqgyu9jBLArGaMum_rgoB4UtGg2Oy9ypQFVeySWGaSS0b9EabB0tLl1HD3gwnbE7f3n1Da8wTyFP3e5z5WPKHC8Nsn2vX8RZ3zbtqX5BB5wNek8ufUpdnF17RS-gs4aYY7JLBcwJc5BHD4DDTxzBv7p5W2qzCVhH2LYI_RKCMX2x5RqQj_u54HNvtsvpkXGd6Jc64s-KQjB7Tk7fSy7IzZ1Vi-_iJHku7NYM50U48Hxnmv3V9iGneUyMdd40G8yDArWnovc_AGJ8S-azJfZNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZPockorDLG3PGCEfWMIy936q2Hn-IwS9BqpnRHixpz7XLqRCzb_UK2WKxr12bI8rbQUvURfHfs1w0CEkvrJmIO4Lk8mFVZ-1l7qWGr4zziafQWfhlNT-JfN38d6f3tT7Vdrp41gkz9t1Jq3SdXK-Ou3LOVUWf4oQub27E5X8xEJiboD1QEmzilKJOa_3ny5HPfNBvbJls_NC1xZlgTPcFF29IMYoFFS0VFENLwycInghemcGecfmnSIAZQTYDcIYtW4HN8db2A7W4YtcEEHOx-cR-2OtvZqUrUVMEQAtjHSgudrSb-42u16W_wzjsBTxOiHssUJwUJVFdio0tX0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP_KlSKmCPUYtXpXbEplkUdmy8dn2yYP6ovfq6FDmBlK0Nvw4L5s3yCWaWd3uOK7hgO_h0vvk9W8juiwHq59IdPJf4kHagj-s0xOIL85uU4Nk79wIr__WpXgkTa1q-1J9GswqiQblqTqNJ-C20vMq6ca8EAmk7eaKcc_8xs84eRJ9aLhdIYI5WBng8zMnoHHWXwXOxyI3F28ByLUSbXDVuenEQTYXPm7fMWWx0xU9InkqRF48NFm4QL6xDTOrQuH-THQex1JC5Gvj4VaBoXRuqDt0ZfhaMlGiO2cJMi8oLI1f_q1f_NYXKJHohMgJbD-a2KK20HzQ25wnpEub9B1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InGASS7sCoUJO9dntGz_PYO-3l1XszGhyB0s0OvyK564u6lRSTZ2DEMuQxw_CLwPRF4INFa9TTvKw3sDFgYfJCgGAoYjP46bmeLNXV1eIZdyKY3VNfcX9XG9R9tE6I6MhTaXuxpaUUSFUPHVE5cB1HxztZ4N4kXpv_TkDIX2hd3Qc9fsoVcKfggx1pQb0R8YA9xEQ2BavfsJYs66ZR1YiJljkwKVNAtceBjzB3o_IccKAAM0mJOVznre7I5Od6Ha08PeyVrkNRCi4VSG9z61I2UrisMtvwIzbQqWy7RKD4D4u-8dn4WwBaUroC1djCgGwWstEReAx0FBd96gp3dIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=szdp-dIPZO5kEm2or-jyKHwqBDpZbRuX0AbaCYHqVGJ_D0fTjMAFRCpHg25hpKg85wYzifZwG2fqhWpqY_plceOL7zMCl1lpiMH8TSFmz-sp4MzCXc9SFjZl9sYmxd_6S2-2Ib_LuMkSjOM7vTCS3eH9TlWzUGVKPTlVygn0xLKUSJ_sGLjKkoYW18NLplhcwKfT96-J0Vj_X2e7wn-5bzj9wyRoODYja0vvzeUm-2jdbUGBknb9N2v5nCpT-pGjIWe3siyIVkMl0QvAbZVEIq2jKeqttVRKIPdaMo_99lAC-ObZJ--yb3ZWUvuqc3RyoXgnrOkOgHCIxfMCh4wN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=szdp-dIPZO5kEm2or-jyKHwqBDpZbRuX0AbaCYHqVGJ_D0fTjMAFRCpHg25hpKg85wYzifZwG2fqhWpqY_plceOL7zMCl1lpiMH8TSFmz-sp4MzCXc9SFjZl9sYmxd_6S2-2Ib_LuMkSjOM7vTCS3eH9TlWzUGVKPTlVygn0xLKUSJ_sGLjKkoYW18NLplhcwKfT96-J0Vj_X2e7wn-5bzj9wyRoODYja0vvzeUm-2jdbUGBknb9N2v5nCpT-pGjIWe3siyIVkMl0QvAbZVEIq2jKeqttVRKIPdaMo_99lAC-ObZJ--yb3ZWUvuqc3RyoXgnrOkOgHCIxfMCh4wN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D49KFXxgdV2eBdYkmb4erjx36-5hyw_9z-1b9jBPI_guMvDxE_mkgQLFY5hAJIz8UPRYjCm3mXTWD-cgph3aJKlm3TLUC_vAAdRNtryA-yBadRPURPNwRvTCJUKjigubNbdeX5vGX6QnIJ8GL0dGYyOfwKfIC9IDN7-IioHONiX0CYy3wWPGGlBbh_LzeFf4a96z3xiSjqq0no6nn35LuIabJuuYSX8Gwnfn5lk5wa1rK4ZhxOyjyNLJlBc27q3ZlOyLMtAMSUfEiVdfC6N8YXf3u_I5WWYVYB7HkmNJkxAnxcuqgQX_OTrciMrvs8Pamxxs8jliLXTSZUlPx_J6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0bhfGYv7aBoIRSnDGtYNe0N495sfJejeoBfh-Z6s33xnoyVnstyAo0PJa5C4aHVSb9kv85W9N0O4V8nGC73pa_HtYlDtJdqUCqeevRoKty9BqwaYHJPb8gMaN22JUmvDRay7bZIR1EkbUant-l16ul0RhJ9Jd7YVjUAyERUORFRLtb9_bFDtIF-Yf_1HC9CbFHKB4cuIEDS33w54Rei_LkK-RL3lysc3BAhykG-pa9S7DJL7ZXO9S7G-zkjwH1T8FQA0x73wT6E210o4vd5hzvSp2WDbhMqu0IdN5ZHtB-6UXVNyZ6YyR6LHpLSLpyuVTfcxsCJbjXg5knm_IEEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEF7EtWvYKg4eFSxcjdj1leDYvn-2DToV9B3SevQAYl31P4voyXi5qOHxxaQfC6wSP5HOkmayUxRufHukwZy6SnpBIKXbsKfv1RQj-1hOO8Q4Djh0FZlf7eq5Q6jTvnGQOZSpNhWeA8qhBOuhqr1zWE8Egu6IUCfhfDjjthZYX5_HfhTpv_mgaUs7yHIqWsOSRNl9ayBKEHDFWACOrjP2waREbT7q2Q_8jsaj1ad3O4xr4Boc-BaCCeoXunWEglqULydqwLK2QFR4SURInXCL4cZx5Awe7HJHoAHd261aQyFVP3drGxcgnWeqTXTEZuWIslnnzMl0csaqkUl0YdHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvxpULAiiKmDdYQaXzlG9QyJSMz63vkpTU6Zl5_EXdwYR-baDogQ_xTdqpvn7zgoQRDjGTdfV6C0pbw-lfN5J4fQTejjjiRv5pQeOIBEVsNwRhDGcVSdKLhZdA08EuRhh5WSHWVwa_63dvoAU7Y70K6nMvTLc9NfLC9N7L0yue0EhzDg9jjrUETdV8kpDROBb-2HzgNA7sLHn3ePsh7-Qcw7pVtYxZEBLcw1icc5Gddl2CFKmBhOG2jOHTMyfd6znf7imuMGktlyTIUS8JRduqux8qsM1fKdFfoh21beeORxtC0He1ehEOeG26-DCOei0qFjk5sIkGlO6asFsKMCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfyGCVCXp0Z9VKx8HwubbrpfxcQ4w1HFDHU7nl3zRV60TtOF1tGRSGElNL6PSTbdS3_QZeInx3BDqxvdm1BQMLxb9JHbof9finPEvZNhrmo8xPAQh1FXNYX3WdpWTXhX3gy-2c-k2lP2VAMW6Q6y9JSjg9xPHzegyWc5JYrwr5K-fIfoiZ7VSUZ8Ima0KJV1X5jRLqXQnFCWFFnHeNtrsfAI0egObZ9oP7K-R-KTy-arxG0GFSqVwjEC0NNt-6ipsY-O85pO2yH__sfQzx0PBfilMuOGp3QXcwuLnPoaMu1sjNjbDzBgGWZffSV0dURTPaZgXMBngH0HIMccUaRZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFbNO1F1dVShatakkod3oP-Q2SjTGCVZ6UVGEQz71xmgne7sN7kD9aA_iRGdOmd8RrzHVPaPldQdGOzs_N2L2fc5oH440OsP8jNJKqgUJcNMjpP8lJHk_b21zioYWw0QY8byk3TATjxKoeGAtSHr_3AgjSQMoDoY9lmD0L6mhv5CoswCHNuiObJS_T7-OaLQpoyjT2dc6_Bs_zvmcabFELyWM_EJicQyeqiECoIVipQobgYk_pggK3ceIFGsImjKnkXx5CkfAQpgsaXzs4PWCizjdpHI8L6UDwi56yEciDzoK-ipg6_tz1QoWsjxYsxPQ7_FDfc0KZCUES_fzKuS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3zcoWyBqKixqLxSisammZ14COX6lLXcIdz0xYaWh2D_HmIaKAXT_Ylno_tstkYBLSC-zdaRN7MfDs4UyIKjVaDixEXerGFZD00eYlzTBlXsrZQU9vNN_mfTLF1Cqie1dUSFE_LYOwvAXUlWP210xUyMCWHNhFocRX7K5wbrtbBKXGGUT3xuRJD8oXY4Ot0jOqD8OcdXWoJj5UGDwLfe58sSVlMdQBRzygXsWQ3ZZi_sJIBAU7lyPAsTVvz4mjIHmpQvJ6li2_2AUaJIAaWhHIeWSWnkbidduM19AoNbx6U4oJq4EBrxv80rD9GL8UWSxUbpkXByz47kYTgA-vstdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mteWY4lI9i1EZKoxeQZbCS9_1cIHGhwVMtjbjMagMb9MylNm7O5uejPMrS_yTdXBOY_pWAXiSdcbcByvaIWcw2xXHFXLa9aIjdvMouahuCLEMRslLLbJ-1EzQFW31sQlwPgxiF1Ozfh5dtiUwvrDNg1AqeIGCqHVHOE2GPR02YRz9E0f5fAyW4Qh2KZ0onxQBw2wSbLFTJSv5eofsoPAUEFWV_GbaVlCHPFryW1jAxws9vqW_wOzwBVyD59sy7Ecu3JyCc-5TVJUOg03O1stZaYtFGqNLeEc2JC-hwfjTEQFtzuitlUW70vocjxNjC0wP7ElDRW-lYK_a6x2fgiXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB06oty3tcO-TYhCQY3M6mhBkAO1yBsW--uMSKX-rr0c9GY0BhzxkQaEYH47x2gSuH5ruTv7GVqADdyMS7HiphpQ8C-l1YAyC9P31s9gQGLJz5NK7pE0QsPj8WskLCDrClPY5XbiwHfNlVDJCHznVqFz0KB_vjRTZTAO3ymJ9NmHweWDzWDavNl6W5bryF5UHxkE-XKXSQ1mNcKZ6vQEejQuUoPDCOo259ZjTTkIkkWdpqYlTg-mvurhkfqDwlq-4kFD1IJZSxEPrFwtcgjMJwuMF1DWYjtWn6-CziMKU02az0ErZKetdIp36hOiEtPXYg6oCFo_H7agFMJW-oGGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtqizr7lM7agt5kIFuk4iYS5HJblBQi4dEQNCoK3pu43M85OjFtu4ZXEtv8ghsZAEgiQMZPE71ITO7fpF0BTJjNzTUnWALfLH5xhH-n_4MadFnPZNTSbzOx0LZnS7K9xP2922ru_bvgx1O1aqcVF5eVj3stwBVD20dzrNc-h8Ooyu2aLQyIbfN1lHmXzduxlHWJbUg81aqdrx0jtxEmJ_A3kUEKVemKCLUa99Q2IJCNfVd8uBwBqyzt_PJmT_BJ3oYNsS-cRTh8S_ly2qu6zQnR3kqHFsRJQjL6Pz-5EQ6wqoMPigFeBIt75ipwBKc0CmevbkZgGWnuQuA5piZAW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge5C6mUDHFLNK2fa5WYJumqiz4Sq0rewtq04ohwldZvorHwFjhJgYgfLkUSVipUk_NrAmnqBTJ0k459bkSvWwLpG1yG39UDRf4vkRJYyOcE58G42YohW6CcbgAyGQojWH1pqfwqjqj0Uyn2qnDiDjOG0R29XLK3TARplamRNfNAX_3zIUAAS7xgKEylmkQuraMzA5dE8b8vfjDkn3mpWgg7FYarkiJiGpJu_ez6tygCx_VrplCJCB664iHqS22pxJlaDVSdK_T5f6N6mMiv4zevWmVOaOvzWDU3m_pP_0fuEKJ1TkL5myLhRHQOpQrvGy7v0Y2IuGzUVUsjd68cfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tefWvW9RrequtfgQBV1ub6iFnewbZ3a7I2okQsyB-BxPoytyaQ2-g5g8qglfYfBFHjNDCpxBGWkOp-QGLMWqt3tDrH8xIAnI2MuDVqbz9lfDqs_5M8_0ad2l8EywDh2zT752HaB3Jfsx28kH-8ZASrPx60Y3l8Oeb5B9e8Hs5EVFD2O_4N6w2Y4BdDS15po5jMc_W2vtx-nuVvYyIf0-h_034A9aNMeH7iaoJgDlA0U19rgvxG9OvcMrzTPopziSN6J6W1kzuhEho5OEFgFP3QIMdjwji_pHhi_21A9RxMkMqqGAaRJWjz74hvnd5XnL9YoM03BqdMG25HmUH6GoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO5Q27EYyHETAZhDqAY9QWgdgFqBcTURv7cZfwv690e3CZF-sCUTnYpXeOJ0k59Qi-p-tOrD1AfWnvgV49UmNVuc5h-EQPKuGfsakxyMX0YDVmZUMjFJy1n3q_WHsref4MpbrHSTN4KMFcA-wvlrggQi0TcBeJV-7HJltSBiP0wipDPZAPcvW-jiGSHcZlGHcMa_yi4nHWjEfnOO3d8gXG9ECZoDUTnADV7e0njdKXSlZxjbrZW7n-V4Wp3wR8gS92pQpfwj_EIF9CkwcU1dKLtlIuTDqdWxmSlLF1MwGI5ob5R_xodt1-xigf48X0q3eu5bTP6afMAePPktPKo4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi7vqXD5wkZyIk3-9O11nZGZGPbTBVr5hLKXc0C3HyC_3172styWVGRHqyNfDnuCX86VzZyUS6cvapn_WnLwXoQdvRm0BCXV30-zeMBphHgM-6glv-EvZbw02_K2dyN324dlBA0NcHMkFX-8wD85yh7Q8dD_h30vPV6gSd-xRM1QX08vNF6cmZtaqhdGLsnj0E5b5jUUJFelOj13r-bhmGtTPh23RUMNPtqgyW9PMHQIGwAwC_OTJiGIhb0RxhE8nJtmB-L2zon-0xE5SsWguaiNKTEe5QHZAVx20xywEp_3dM9vqJ8M_ja4_2BawWX4ptXSXlqbph76ZqTCEI6slQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdMMz8LNXWOLyt_lqetqqcUYM-Fj6jvzOWnde0AZyCwBKYnhWmkfz6fuDLszfzCwqShcH82K731s0zWdOGZYIxCQTvotD7TK8JFgHwq1LQL5CgxCnZTp5oEcSIn6i6--Tp_mqqAFD_HxLNYMjyCgb3fK6c14wQwB5wONT0qGm4WSc45YoIR5Dk_Q6Pz4WiSH4HZuJifWqnW_6QgGUyV0Vv-AlG_O_8YmZz1zAm5u_44YAg5gPW1al9k7AvaitpA8wII9wIJ_JC56rLLirKRnyHr-5IvB-SE5vJfctgfLaA5-rwmFX8VDyae3V6agOLfcyqL6WortHDEAq1WeUAPALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmf1kl6xEmvhNMDwpOtHHTDiXUAh58MCTr18OzjgVQKcpFdlMKDkI40eazqGpPkB0A3kpWR2ljSq0MdmPMhHFCtyWKkd40UByVUmnxSWKiR10b8gPsHL3uI5t_elBMtTmvM5_p2UIu_I-bwkKL1aMslk-POY3CU2OCE5zbGo0b0Vmhk2VkgfQedmEtRo--py8NdNT1nmgxxerNEOf508MmqSquxm-v5Qw1gpu6DNvTmTNVlKy-O5Mz1n9dZ8o4-FpTj5nx1o8eiV9jlsBLUuhfZSegjhIJJyIqyxt4nJRWjGIB_wDyudIx6ezcgq7rKxSMRq-lnnrSADqUmsma2mqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl2HnPPtsGUIEbpRWcQ5mtVRhD7UpUIcVBJ7t9GIRgW-Fuat1zU7yQDmZrk-Qj3rqfPvch004BdKYyI0FXSWcUBomFI7txqxfOZ_o0hbm61ukOMKkmvkzbd_9aj8ZNjTPEs8J-D_yMgCwr9_aAE-vt1C-oLw0eta41eQaVBP9R2No_z5Ae9yWR_T77stwhUV_bEugQykLUjnkcy4jJfrdbTBMVUTys16eDWuNZLbHSR5P3tHSkX2ySM9LMbuMiBA1psZwHvtx3wIbxgGHnRU66pkU5dk9uVnvfoMw38e6aoPmAf5zV3HnBfWaFmGSr_xOGlw5Rjm1QhgWtJffXBwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=DDIvn-td8tk4Nr256DGzaciHvZ_3TtusJViln9dAAjO2-bpQo1iNoPJCFgqUyENOtk4mf8qrSPztFTEbYyLaU9kvx4uiYj_v9cGmrqIGfLtSa1ksVFxR5iwLBJGO9sjHP6GLo2K04EmdyirLZdfK1qTslWKsI8wFuPAuH4JKGGzgkQiV7ePxjPEYWsuXMaG033KjY2L6ot7utspSbmkW4G_U3n2X18E5zVPB3KnuCN0UdOkneROj4x_3xXXP7s9bjo8_qrKTw2yMuVpof-BNyirlO-qOupnbgjPUaEzV_9sIAh3RoAzimZGbxA4_WxdT73A6YSMNVFzBrzKMLTXTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=DDIvn-td8tk4Nr256DGzaciHvZ_3TtusJViln9dAAjO2-bpQo1iNoPJCFgqUyENOtk4mf8qrSPztFTEbYyLaU9kvx4uiYj_v9cGmrqIGfLtSa1ksVFxR5iwLBJGO9sjHP6GLo2K04EmdyirLZdfK1qTslWKsI8wFuPAuH4JKGGzgkQiV7ePxjPEYWsuXMaG033KjY2L6ot7utspSbmkW4G_U3n2X18E5zVPB3KnuCN0UdOkneROj4x_3xXXP7s9bjo8_qrKTw2yMuVpof-BNyirlO-qOupnbgjPUaEzV_9sIAh3RoAzimZGbxA4_WxdT73A6YSMNVFzBrzKMLTXTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jS4uryC_WkTS9UwieLFP5ic2mfbjgx4setNDLw0D8w9YZl9w4COmeHDnvfhn8B6SDSEEVzqJtO1WuFImAPMV7bs_TXCjEqp64RTH2uZzwXgTJuMxoDf6Szzr-TttkTRZKVShwhvH3WBCI8SgvT5MhTfh1vNBn0GZMXwqmyXNLx5_uPPgFcfH8gdnU9PbIltphhAtPpuFFRbSNnByzr8EYtjfPgmVQ0gGQoVFbDL3kuop3iDpEASx1FsGknNoA0SZ6_R4i6gzHAJZvrrSOM8EdxwZUoJkJIuFDLhwBuUbl5CfDsgfIE4OfzUJ242iKNrFlPBl4DRceMNUSUpqSaoPr27CHfYw_AwFNQQDpi8t88ML_4hbk6JBUGr2Ley-sZeDYALjqtjokpYaVr2FE_NO1ftFziUgQrwLkUZMkLNgKE17wEFXBu59v0YQdCGotTXthI2cxYFNkUbhyKbhEb9A0Dz6PYxaSdu_1RypAYoUKZ2G9X3SVGE_cXu_qHKBhAaXHEqM2iX2ZY8d0yMQPymGhvHj5FoVs_cPS3Nrv-sBGBdWV6ETCHCflhsN3jX_U-WSBOAOnfFrICCnpQC3nvY-Behsu23GT5ja308_wP2os9cPGe3mYs7kO3C6h7JKPtuG4VR14H5O8P9hDFkso5DS2nNHINC3xT-PsUHtp05QmcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jS4uryC_WkTS9UwieLFP5ic2mfbjgx4setNDLw0D8w9YZl9w4COmeHDnvfhn8B6SDSEEVzqJtO1WuFImAPMV7bs_TXCjEqp64RTH2uZzwXgTJuMxoDf6Szzr-TttkTRZKVShwhvH3WBCI8SgvT5MhTfh1vNBn0GZMXwqmyXNLx5_uPPgFcfH8gdnU9PbIltphhAtPpuFFRbSNnByzr8EYtjfPgmVQ0gGQoVFbDL3kuop3iDpEASx1FsGknNoA0SZ6_R4i6gzHAJZvrrSOM8EdxwZUoJkJIuFDLhwBuUbl5CfDsgfIE4OfzUJ242iKNrFlPBl4DRceMNUSUpqSaoPr27CHfYw_AwFNQQDpi8t88ML_4hbk6JBUGr2Ley-sZeDYALjqtjokpYaVr2FE_NO1ftFziUgQrwLkUZMkLNgKE17wEFXBu59v0YQdCGotTXthI2cxYFNkUbhyKbhEb9A0Dz6PYxaSdu_1RypAYoUKZ2G9X3SVGE_cXu_qHKBhAaXHEqM2iX2ZY8d0yMQPymGhvHj5FoVs_cPS3Nrv-sBGBdWV6ETCHCflhsN3jX_U-WSBOAOnfFrICCnpQC3nvY-Behsu23GT5ja308_wP2os9cPGe3mYs7kO3C6h7JKPtuG4VR14H5O8P9hDFkso5DS2nNHINC3xT-PsUHtp05QmcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSFWoZU_phiek4Bgxs1Vj8-6khiF16mubaXc9e--fNcvdPFN3DrN3CDo_ftfJ5SLsNy8ZXXQZ1f5UzIKvV4PMsMqJw8nswrbD63BaTaclDrWDl-NaStG4IUNHzSeehsiYx8Ld8mL2ZArP7wot7DPmBwo0mMTAD3LIolvRgJ90aHTvNx_oi2KLugqIRHQhk0JD3BgTNNNmtDy8xJnxjIHehEzXCI9sPXziJS_AguOYy1GhWcKNXuChDDlniRV7zFC6WIQx8A-MJbjC4bCwCSfWJMtMqmknVSXXlCy2lMRS5_NkDLiGfW5_IHrMKtqKy8kWZIpddWv9c6juRFJlTjVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN5mTVP30BivxxfzWAed9JVm1A44elTAmVxfX4uuYV5L2Fbp0tCSSOw0NhXxS_r1KE0qcMgXI2xmj4mj-sjdon3AngR88xd1v_Kpy0lTfLLbBWjBpgrSNVQMWDM-vSRfkndqihb1wArZbnm2-BKdDW1wXXNjKgUt-f2AoknqzFiJci5V7kXGvhudMuw8fd5vICS2mmaRf_RmqAcYIDSP3CwjFAXw8xcAAKx0NNgnSc2TfFjK-a1Yqc16LBFuh9_qj_pvCceYC056yz1JRopHQIXrEz9DGNPLG-QB4KdRCwm50Ciz-_z6VbpiiYSoDE6UcA8Nqsl0ZC_GQLpUzBL45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7gJ8c8oWL8AapQEAvemySPHhg6xKCLD3XSJFYakD2XTo82gS5KH8U-MXHbD0IwtWJz4pUV7Bgv70M_MPc4JDhPtRgHveCtkTwq6QH-OdFYxVQ5A2zwa9RgcrAw_b0MZp-uBduHElgQokBG6QnWMpWoVtDazZorOnNlX1q8MRL1kYdnUDMCHOhFvpB_VuW5bQD2tA4xZ43gc-oGVeOPw_pOoyhZuFi0UIEr_lMWdDhJSwHYc23KZGrQU7MOIMYv1mCT1fkISp1dNoVV6t7W79H0pQxiSGYiTOSJf3HpsABbQ2PHlOt_Tfva5dr-cSfJaDyS30B0w8bqADDdLATxf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chO178VfHzC92WQvTM9U6LPGuv4u0s7R7YyDIASyCVAJKdB1LEw648rz2eB2Wrexaz2IlYF_gQOLVW0gAeBWdOZBfAiEf3bwauP3D2InvTDvZkpa6dckO7T3ZyVB1BsXTI6EwGahCZ0te1z_vO5AYmnnW1crEt2IS4Z3BnxYw_Khc8VrKc4x2vB4UGTWL7wt2q0uNyvrUwaK0R4G5KRbgAZK8me4B_djbli8xwfqLL8f43Kr7vwTSY-wILt_4lVaBsxFy1uldxojiKb55_8JxEyDhg7xcDA7fDIw7w7R2zos1soOrdeI1-u4pu-NTsYC4_34MOPT2Y1dtkdRSHVUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=Gp7-JMZ17DP4MbE6aKvJV8gcKmT6qShXc3G2GbHYoHvFC-pyUHq9VLbTCfWEgU98zWl74NP3f_hPJQxvOJfDiO9r9IVXhzSnAbtAKFq_a5L3FVwSVhPub6XbytSTdYbwbntmpHdh_Xn0xTMngu1wgS5t1zd8oML9DSbN6K6kh0plGQkXkqD7cWRA4YYMPzF2M3rBV6b5ELGjkvRYXK_LS9tEwoHYeV4-aCjhHL0VtmQQlYnuPDVJL5PnCIKy9SBemTdpAjHTvzEEBYbfsy2ZU90542zPk6DgTTo6EQP6dkAYLkdWcyjSN3B-O7cUoR-BbQD947iFEQtUi-L2FaAl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=Gp7-JMZ17DP4MbE6aKvJV8gcKmT6qShXc3G2GbHYoHvFC-pyUHq9VLbTCfWEgU98zWl74NP3f_hPJQxvOJfDiO9r9IVXhzSnAbtAKFq_a5L3FVwSVhPub6XbytSTdYbwbntmpHdh_Xn0xTMngu1wgS5t1zd8oML9DSbN6K6kh0plGQkXkqD7cWRA4YYMPzF2M3rBV6b5ELGjkvRYXK_LS9tEwoHYeV4-aCjhHL0VtmQQlYnuPDVJL5PnCIKy9SBemTdpAjHTvzEEBYbfsy2ZU90542zPk6DgTTo6EQP6dkAYLkdWcyjSN3B-O7cUoR-BbQD947iFEQtUi-L2FaAl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF_zhEjz4tMHrT39-jRnVtEvAL7y_32IYdPflQy5Tc9E80Di1WoC4--JtdhzeMfVso52QratfJAew1lkobA65AnPmdVs7jhANf-i8hC96IKH2s-7YQoMo-_7WUGlHVoVxtIS03eNQNWS8_HNKbvpoMA1NryzUDqcv6EmYOjADd4hSQSQX1J7D2FrUrHZrh79C9xIBJ4O0yQEeeK3DJZmE4F6o3FzlvfS_DfU5jygLBWUZpIGZgTu64F9veH9yT_bId-3NCnuuiadiheof0bw3F2j_MceHjYS9SbkRlntJcuHT5GlcyBGj9LsMcTHIr3Lr5jqpeJn06XbHMjYxrzS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
