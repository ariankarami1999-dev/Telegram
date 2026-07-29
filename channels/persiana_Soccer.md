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
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 05:18:31</div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1q5bmCKodlUCMLVn7k1I8omVSiO5vjtW31npy9tAug4BCLKY9yAZHF00L6Kk-7kz3Y3asCcA25VK2msixR_UcQEx0xrt9uxFZHI2EPb6SGFAYZqi_d_hzIooDrYQgRJ2hATFI81M8NEFyYUbzj96PUcv3MY8vNPBhmR51mAWbavXSIO_nd4lgoNsvDc9bF02xRzWwRK1ul8RfKyNfQJvq1O4dvIF79nASY_aGVMAY6N_PxNEcyKjYVsMRCL6hyZgTKX4aM17RNTjxbf7mOq-Szwz62RcNbsK7GeB7QA6mz-bdb6cxKQgLLSKM3yENYmNu7qK4H3h1mWuEoZ79wzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKgZBsWmbpUmzUA0BV2hc6rKrK7ss-6X3V5ii_zu4Ucw0OqZ4Lxika5xeyqjOC-nXoV-3_YiW1JSqngLU61QzBG1Li_LuTsYbHw7Uc25mrGRXYf3BCKWFPTHJl_CDhJ-goMxURbmpmfp3AH3qQq82mkERLbatkFc3nNaKn8kBt_oajP6VwaU9sm4B76ZuiqejQv43LM50XVzXzkuS77myQXi0bbOr4Lya3f5OOOOmP30tup0WcQLXVooYYUhhfmWhHCx6Nt3gXzhLA2j8DU8oclck-d9yVXYt8BGpPlZJ0Qnm_4FSz4UUBswe9lHSD12hz55qNn0U4dNEQIC72C42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN6Boi0BK4aE9whbi7X1cFkrZoXw92FKuY5dju4DOyfnN3njwBV1D1mKqZ0V749tlsdm6GoYb1sAD0VTMrjpYvN0EIY9kydxQ3a4Crq-a7297Oc2YSnhSlVIPzaHYbp-Yag4PwJ6hcUJUBlUSuVJ5QSt7SHp4EtbURu9lTXp0odGTou5cEIaAjjOwNiSm2s3aKJzzqdSIbD19_XsS9ClC7dph3g7J_oIHYMtPuYHZ-CeuUmQghntHsCBkH23SJcfBNuvVkhSBOH7d2-dIAuoU857pxwFb7SKek7ocCiVpQ0K0UFXHx7u90bCqZwc8dgQ1APYIb7-8gUN0IADzxRj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHEOtgQr85qH7LNXXOncefKoNHBRv4r6XbwVmFjcTH8TIaxlM999F3b4PJ3EGwdo34CK91xBocWwl5y6jr0JkoXM8uaLlwsJlZPFP-3-Hz7uk8TPmNiDDSo5hCkFPHVitBw6mK4rwgtcMBit9pZMH3l9jVjjrgIolDQ1TxTeHTwUThh-5_m6VP1IaN02Hy-wL3b6PN8nSQ8CIsZ-iZdUGuQmMF_oN4YgtCfmaA1eGq52C_C9zYxsoYX7OPwQPGkVpsvJSGGqFDfka6JzPZgzB-OQRyI97wIH5rnmvMGRXWzJn9kXtnRxO5gWuPoRss6a-ULJSs1VTDfXEFZx9-4kYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiRt_dfbrkrcfMGsiu2bgx9hjlRmIyrHd3m1OX2Uiun5C0oIKN_J0FtJ_8uPFM-9klarHfy3eBpe325GXci4OK8ymiPKoGKEFyo9COqJUaE6NHdKJo80Lc2CZAGmMZfmrfDF1pmlFsjesda7jpPhR0oooBCcKWOWCZ5FY9KycudBxbMvQEQE9N4Asau7YmTZrvLH1jDcOUeTRlvJT9YPUElWkVz3MSYug25SP23qkH1fhE4Y2RzeAlDcOL1R9ZwJIn1VJT-pZH-hMae6odCyGQUVkAzbWXXArNqxFf-OnKG5y2pAqs_ybhm2Ch9UTvCmtm4uxngraXCVZ_DQSGzcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSU-iqctpaPQv3qxxts7Ojp5VopAYh9bjc4ml7gqesCihKPuGprpzcnKcKZPhg4RtWH3Z0orHy9K9aPEpIQFK-GqLdL45o42x-k_aEUsi4vNHCVHRZLDfRhi31BCQjRH1Jt6BwmhUFUaj8WsxXMbWD-COuHxbVBUBEh_D62to-oj6ZHbZrBE8GEZM179O40ycF8zKObxSMzZkXkABXM9vKJ001DkdZ_OD_8Hg9Wriad-0BbO-Z5ldHsD_AFJoFqfeD7GYYVpOHSzUM-CyiOTd6qsCR9tnwjj9AJ1wQ_AKYx43RBBIL4SAniPhfdYyt7x45ejkuWKUdNqwzH3kVuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6hrNUQD3F14akj1AxT3ljvqQPmtqb65o_CjPChGYV4_CcRsdQ-uOlyiqZyX-fqSGMY_aZSyVvhaJzCAuTDjJ1cfoIFB3yzpgF1E25eocdwB0zLLG-eVuSD8W46E-_6xvxuKxt69pSL2-AQwt7YDp-bdpYouQvevByUjHSuEexD_6VfAGnseirZ61lezqjRhUpZjCN3V1EF6rn0CoaKugkyBCzRv0sN7R5iRQdJvN_ZQxtu5qTZ8g3vNceO6pCnwdNx26qVhmw4lOp1eWwfJUIdqtUjMVKIXWaLeDv3HPRmgxa2vVJtnjyWsIJ-QYzOsys6PRoTEx7uj1_l1RCbGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOWuF1uw2b1K4hA62KWZ_1sZHILUNPxdpjLjpSeuOwGBm54GkQfYTwzxHpiv2ywdVE-scmFAsdWPI2iBZn-qy0zovWhb2w4izOzEIj5ZwJTBwUcltZlp3fV0DC65LiuAey-5StqnHY7WRejRTimYY2lxWtitmNujQ1-ClKz3agfURN-x2RUQWybcGoNbI5zMVAO-o4MgbQX0GRyvKD5pmLboegHMhqeCk9WiGliBhHfnGQyQOSM69WtDgyXGiZiAdLYQp4nEjPcmNAJLiIA0B3prMdQ_O25q9aiRrxAHSYAVrcdyCxF885qELSZr7AdrBiMSGxwG_FE5dzG4b4E3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpN5XpOsT_QRHp32AJMNql0ke3yHJ5N1iPMr4YjPt4aydff-yLbCwYQ3GMxgDQq2c8J72hiAed1TJDOT1pFsfXXui83yRrT_xBq5tuxh4AcIdNV-mwWSYEZ6d7ToassfhZ_NfqBOkb1BRy7Ekor7EZQZtNm9eYGY-37X8wsRby8qwjkZVLk8bIoCGy5HJwoJdXr0exEswLk2gQVDSKdTs4Edj27aXJzyjwxZTCJdSBdDh81W3MKXptP0dHye1MMZVEoxvtG32mFaAtUm7iaUFSoLNDHaRBE_i2QnSMbkfv_y4dctlwa0pGdFmQHTWP1SYu3pT1SM22peSw6M0W36qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTP0WWgiooWfTUGgsXCY6kvm2z4l1G8duRWdokHr6OkeEOJK6qh1ILcC8POeDZ5h3GqAw3sw4Np-SFUQ4uXOkbArObU1bgrzNQA0H0VZrvM4O2-kkdAhO1s9VQUOawlKi0Pf3YVSUsp6K18atbH4pF4_kNNDdPQ3QB_N6Awuf8IcaZLpXPLng94QcqSnNh38GSjSNBAopE6H5HPR7zF9jUeSV9oNaWHaCEpH4vQv47MAAm74OZ5PuTsESi0f1BK7toqP0w7u7yHoCpwfQbkFdSL1ik3jZe1ylposmZ3cPdB5hI1hh7ZEJx16wydoWxXV_T41xCctmZLp6E-BmbD9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dDJHf8ElTQlfIU9SP3DR4EzoubMjJA41uACr9yQLxs8aa0hqd0wMQmDPkmEE1t9S3MppFFHSi71QH2ascjnEXRsSdSHsrCu2TQWaC81yAVcJHQP2lBrnQouVogmVbGr5VGjy1wrR_fXzmtV09tRsM5OOzP0BJxcSB_p-W9xDixvaZegZLNHkkqKSc5SOE1siGL7rvPU3paiemFo9rWzSeRzbpd_zt_C1lzLF0_SGIMepyY5kyrX8-B4gGB-o88LLvsNtAQUw14l6zuZjXoiYAp6NHFdzIjozSXb0sjUyRNBr5ZomOD-bIaTLd3TZgkPH_i4iZtdT7Cs-Rnxp_krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiTx9LiDBK65kKy8ZdOkyF1DwjQWzpXW1jxsBUqBrKqpk84dv6-DJwXIRGOEDaOtm_3k7b72_R4K9L8GemVnomy9URqL-Vznsq_5sd5_n_Jp-5Yt8xYDmK44aVLN3ZbkpZp4-ObBrqp5VDwgoA9_oiNSYG94X8_NoYtH9_Iot2wmo4erNMncBcgVqbB_mRHV-7DD9x27laPvyhHGTUx7ageM34kJt-OA8wXQqVm2hrcxX9_7U_GSaA2LKVl_OYGGcsqp0kjyZdRpwDRyy00HYdgyuuXOUUyfhA_hgtJ9aiR4cU_oam7HzrauoJXcp6NC_btILe66xWF-qipx3xZOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26700" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djEXvjreNQP7o05saEIpqEM8t0y7ho_BJj8VokyyOZWr66vPU684lO1Q26ywzDWKdUCCat-k9aLp0OCdtAqMvsv6i3SoHtD6KnSXbPjwBGWrP091m1IHHuVtSr8SkTNFobPoww1409ZLeXbfm5cyG6jh7Tv2wlJgBZk-qOlCV345oh5LImxldUHMBQIPMAjojblxoZN4NenKXImwOaBM5TwR8NfO4lI-RBuRAy3iwgNKSdvKZnhgsIZ8Um18wO3FLGQnECr_u0kHkB9c9r4aOqxTA0pWQkH9IOMqG5XLeVS9pDwpswWcjR8okCrWL_52skkWMMD-w9LMuCUu9kfBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLM6VaobmqvN1u31WWwOxVkhC9MeDyAqFmPDnS9rElXG0wQBTTPHduJjJA2xaj7UM-nkW1wU1-MVTGA95qKMXB5jQSYEa0siZ-4DG9xps3a8GXe9VAZx76rdH8tMTNU2tLmQZLfNB-SWdpgd0FLFVuPEbKWPTMd-yz_V1ORJ9tUjdqZBGLNnTKXrhYuNdzpjaPehGGCqP2IZLjE67ghgXpMF8DDmT_moV9b_-E29rTVsp-Q_Zwb9fbFyL-a4jFys4brfUtUPZS-RhP8PbsTUjG0AO01Ljhs9h_EKDSEXxKISZTvSTuhNF0VrpdOoti7nFa9AXucV6KS1Jy5w4s4EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=HXYPPv7FkdAmrcwdGnQEgJVVmYtL2Y9n1GeyETmyuWiKSRglY82ZPG7Ykgi5tOevgP6gbB4orGK6nefgOL57ShWJvZOZEJiOEzwIkbX5hn_Oj1baTe7dIiNoBj5m1nji8KomoA-UcZsbTjwsdKdUPDbAGD3lJEwcSIGITxHAvLfzhvEgshqEHPvhBmf_Pvp5wcFju3_IK5ur2E2wNFf4ZuJ32MXbGep4HU5hF9jOh8X2xT0NwRcUHTDtnqV3lnZoXCo5wZswpqFVFr6w6XDd9E-0YfBQ71712bUVXtcLPUV5UnQg4az023kjT6Z8eZMLbDxwC0oy6viupwyzkggazg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=HXYPPv7FkdAmrcwdGnQEgJVVmYtL2Y9n1GeyETmyuWiKSRglY82ZPG7Ykgi5tOevgP6gbB4orGK6nefgOL57ShWJvZOZEJiOEzwIkbX5hn_Oj1baTe7dIiNoBj5m1nji8KomoA-UcZsbTjwsdKdUPDbAGD3lJEwcSIGITxHAvLfzhvEgshqEHPvhBmf_Pvp5wcFju3_IK5ur2E2wNFf4ZuJ32MXbGep4HU5hF9jOh8X2xT0NwRcUHTDtnqV3lnZoXCo5wZswpqFVFr6w6XDd9E-0YfBQ71712bUVXtcLPUV5UnQg4az023kjT6Z8eZMLbDxwC0oy6viupwyzkggazg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rffbw3JWzNhrGMjjzU1hdHscV0o8VBRXIniYK-fF6q5vAu0tUyG-qdBkuNE0sEDBT9YRRnyHJH55q86XFH5BygSFjpMkC2GmS0OiN6xC3EQjrEMCZKz0fhUzLk1hE2OLasoKpSOdr0Ht7PCZ08VRVbCAw0sP49oGkUEG1ALFFh-NYoOk4g58EwTmONhfaVxf84TFgqjC5BRDhCt4Nz3JvYqtikJchxthBUmjsU0Vckbv_lQS7MC0gQgAVpOAcKf55Ot_sT7hyEwVlIr2zFaQmNi-v9XCTGriSi5Ubac1HygXEuFvZMgLO3aFqENnRhvzemX80eDH8zWedscWeR8mdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj9TXEvJxVLXe-Jd6wUWm_j9ddHRGP7vZvbyWm6ySO_0yeXEEZYY46UBlVsFu_i_wFYCyUJMwv7TJO1hV3qreKNHLcL6ttwN49b4avidN41dcPUMVkHDKbFKtt4WuGlGxA2FBzmCajd_cGVGQ9N0JuPBzUklCJrCDzBCHZYf3Y9xDPjusggJlUo1Qg5FxCNKlkQCEwqpb65b3Nn11GDjtSyY7YWIOX0xpXsB_V8OlluGksySeBGrw-s5Bom7usCIgrbqBjqXPCSkf0VeTrSL86Gne5xt9XFe5Bwx4m2PpymHusk0gFXYMvIMCIY_eYq_CkMMiL-9jkfDx_1iyaKfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQzJ7vqbySwJtX73drekEBr4NsZ3ORs7wGjHTEDZ8iskghErLAFArD0HRPLLtYfHEdZ8TAXIsvmJgc3DwvwPPuLxKh24cMTDF6wxrleKUi9STJJDn-o7Ut3V2nieERAYM-E6AiJ9dauM_snGA7U-CrIlsbuYxZIRRaXx2ZXh-C8-SmonhqolVm0Qr_CoCzzJxAZowieV2zJzsGUTVbJ597rTXgm7SPjrlSIby8ZYR8mb003yV5Z9gOzbBFshY5bnoCiPo_UVfCbl6ac-7TYy5rHNp5RkBfVPZwOJdz1ZKLGh6XXgqM8lrgpkOqiK8UmH7RFxdMugkt7iBB7wxplBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5h9fhC4uTd0dJmnb7FrqxZ81csrOAX1KGgTkUHxJBynVnHM4pzsAPaUg-tklzNqGIQMRspU0qCZIP8LaOhEF9EU2JENSPtm3xnxNAzMxdgzTm_-u0Oau6l0K5WNsljslTpQCApU4wHVz6zg8gvXaQkofieNlTXJgb1Cx3HPer7v4d9rB-FQuM3pVu58ZrpBBEtfYFvwl5nyKDZEy7Wryu5DuQj_CMzcRApbGShXuSy81nxGv2T00Hu8baSh9DAgHHSnsBep4fP8wQejsCVfpUgzb-lCMlWp7seXFiqcPW1i2jLLyHaO4mqXOjQ53pAlthbblOvrskfhFI12uTraoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3HZuQEYX4nNEa5yWg2v3F4kMXDjHVMVkdmrIGW9D9aA0hkV6k_eqYdxMsQtu5kj7vusq0ZAVJ-KYEE9bdzTLt9uICXfYpwGTxpSPx3A1LCWZYIaO2NLoNbWhG66KJrPTKUMlinmsljdxdMPoZkMhM2AdFuWWyA__nQXGu87-pBRbDdQsfmxWcaKE3LBYPo7yFiooihBWZJHHLh8qiolzpaPA0iIDXqgYdiK1G-OOCPHHttSVQte2i3_b9tYrHl2VlwQndaJ5Z4Zw6hKw_6IsVXg0rF3N4F9sqTQjwSH1Ay6pyil0jHHQKQ-x4pJF9OUwHQl9yRs6TmXTI03WAF0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWRGr6tR_6zVDg3Zf0XfvXKW-mY17kMmPWUd2NSDOODSqIlpsclbMJELLxY4OK41vbND1GFc0kqBL4ZrMBMwfFsMKiUa3UKOokm7tCvTgSkW0o_-FlckGlzysstHlqiuDzDDqvNIZfWuVnyZBuyZHifoNssksnhScL9oqgSejrYjDJD1j7rWrnnDHargn-_z9h9AZvVOdQ4qw3NMNSoYUR5f4LDlNqIBO4Fzg_tQtN5J_Q0yIZckgfsJD7QrEhIoYy7IffOpgyqpNg46Qo2aC2GFoUOmhqz-dTGhj-u_bMZrI8NgWE8JwqcMj8nsl3NfXHCgxR5SPjuJ7jpIDOHHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKxO6ygZLq1nSqQuoHt8e8jSuawDtjUpd7nrUeF2vxsL7uh9HzFLRb51wfEy-O_1YBNldscGGAXS0rr5FEcaa_E8tktjHf2Icf7xTtzRFZ6Y_cE0KNjbEVvN5TEFBVILCBBKeeBftQjkMPjOlj-HTlYjyZ0_wLK9IbQuBsy9fl0PpYwN7G9xqhTAA5gFMuGERw6EMCX0MqlcmfxKk9umlbR5WmKmggrG6moQTaeu_tOcDhra1C98Y5bTxVf4Bya7oBs9NswCBwAKPaIKjccPGnzjVCZ3FdIdRrdH2Ul28ZSAu5S4bfYoDUHrvt-auuoPLbBlfrOr2ZEuWFXqFB0TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJpaNQBWaBuaU0YTpsANvRcS_4YR_1mCow2A5YMro-ofuJoJheofcAsk_HJi35QNrFoh_gCDXyItCw3XykA6mMZ-lfgLcidQMyXJI_V1rgxqJ0GXOh7We7XkLBtt4f2pXSM-Q8yTAJx3BP_AxBhFLxwV_31TgtbfJWrAx01ABDRivIeTTa02k29bMYvkI0PUxrQXmLHo9q7PjVHF1xADVa7yyMnJC5my473fiZOFugRFvIIj8bG-H-3v4Wnc1vQgzQCQRZ7QxdNQtzrZjqQR9quCa2GOpGXqxNBiKFoNCYOuoF7tl_XO5Ud4HPTwGnxISVsppVFQojCJxwMj_KVaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAP-GtxQi6GlW3C6zhdVl1BktLDfanhEgJy7fSPzyu-5Gs4Jx5g_DBvx8n4efI7CBEXCPX4y4MOog8am6RFpvHVwTPjrFTJJJDZ3Tj6e-EuCaZPJTo2EJycra8Jn-9kF-OJgzTgg1NYR44MmL6lcXYuf2lBh9G6GLdW3obggOIzJKuIQZHJYZPUZm2tl4OjudtyRBEElOLkMAqh6KXSHKjDkGvetuBoltv72lO_mjdzmsS3dqO0TpchpsY3re64Lw__L4cwAWXv_tjDro8rtKTj_kkRC1lJH09sT9_9UcVPBBC8WdQDi3HRXghRfEYdvhJLRhsK2kobq0xp2eGTldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkHDGAQuZWyfNfLjbm6QxLIgH6nAAQWC4Ve3Kvqv53v1huJ-ZlLwGI1rhOunx-BQVX5gaSFzDHm4ZGRH6YwCdGrK6fqLQ97hkAwDbAuTUpsXCB0OsqG0XixbVrdbNyx0-X8vW65RiIQn_gfGU-R2atQ2ShdYf1lcN8Z_8LtX0LT6uNqoGtNjciL_8AxZ2nsN1Sj_HBKItZGh0VtVTJW-rovx8-B8z9W4K08Ysk1SL_B_Xrvh439hvP4-0sxrRztK1RPuHYFGvJBA-yzdnk3xX79xyincfgI8uOqwi9FcIIxhptAxRacyArJ25DugkC_0k1xTGkMBedjC6_VtyZ9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3vAWHg4Bth-ePONmA3JF9zkV3NZ_OV1_J_zKvDdRAtGwR08dYs0KfnnXWYG9OVGoYdOZ1eiP172vvPTllSObP8nqnWsK17qvvOimhKtiOe520HEyqGLYyVNSL24Mm0YmOqXZ8LcntqlNi5_MEpi-XVcrXLF0gm9QunY_94FZ2FIAvspBk3imPhCbn03caaqqnvaB0ESU_ySuzziWwgDy5fmJNyKsqh35Lzd54WVrwWmCJnCY8BJ_NaGyzpQAZ96DXg2G4LNjgbSCN0V1aYbac7xl1ewmAaqRtxhTC5K_Is0YBSWNjRiJ62tH19lyOJtrB066xNC3ecAflhtJeqjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWbTkxZY9d4tZKJATs-PLg8yDq3Q2gQtzfgiDGr83u0rmoJODdl84y_VguknJ22MmvLkhbdwmFaHvt6zCuJZ-gPZUDxmfjD1PALLpn25d7GtrdztYscY50L2adzCqNfY1P2pMUBrR8glTmvV-B6w8B1BldqHZKB7AzlJ5y1e5asIIWxJxnAim-uoWyq-wXkWC_i9kmjFqF--6vuoCXQyAQb7rHBflSgKLfLV427wpvABDpLqED8II42twV4XzXBrbpsPxBNqEEX4980eAzyM-79Sod3Eyr85qTbC7Ypj1EDfZ5TR2qUmLGCYa9p6PLblgMH1NQUa0G5J-TyvFeiMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVEE7J8GFoyiE0uv-pndJsLjaZLkLzN42UMMTvh6nLf_CwOkDDmFdrFis6MoEKRAsl_SHjdYyYiXlp9SrlKZHMFnQghX5rjTIk-SDcKwM0ZE-UqjgVTsqVsq_v7ZF4xPrUSaX-P1UzzVBLeke3Mu0SrLyL1-OAuG6c-WPvNoAwGGOxo2Rw1O1_Zrg_IRaPqWWTtl7y5ASlcfOWVQw9FS5ghw-BsbjYbdFCkm7pfyWo73jvlfPPTnEYSCdnwv14CJZSa_9C7euRtkxkLgEjsjywPuF1a8EgwbVhS85utrMgA7zESV_U91IahVfBh02wFUGGvNozo7xEWLt0ZuS5bFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5CPlMVuBury-WEX37T1eMJxM2lNOCGAAIkyGbguPe7RdmGKa1BzSIee8mwAw0oYuMLMA83NKoU_jNMj2tcjtUO9ZFdAg_DeUw_gKaWdhFBhcgPSaL7JQByGi8x87U7YB4MCFXGPb9gYe8aUGswwAJ_c6dp9rJpXSQ-czBMOwdB4GFeVqeXAUPiEvY3m1drkO9sUKp70B3PZZTXw3yT6j2ghvBhvOGrCkYNxDTmQ1Mp8gL-9F9g1b3YiuR0ZLYKL9u5LlCf0hW3F9DQr0qhZLciBtLXu-7AANCf2NjpIhT2oyAqYIo4zQLS5awj-PJrKVWLqxV59Sbt_Z6cCeLq8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsFUYzsW3YWrDqUsXeiVh2JDD9lgS5UFlpZAf9dTLVCv_d2iJmkMO-RH_1PqudQMIhV0CWBOo1opmb8RW6gOMr_iQ4dcppFzuTtxt26XHDKfUWtmfhSa5KkRR4mKzppwUPfDSTiIWqtHdtcNZpgbEwntwar5-1l_SuPN5IijfyyLgAa4NcZlZ8sicWp5dwpUrF_B-RAgOM2Itz5pIesHRp0x-9dt21DCzPiVN8WpNAh43AY7-NF0WWaxjnnUNfB668XlV7JbqTNJewviKdfa5TRmPfugku83hs1g98DHMsLg4IHqDz9QE43mM0FQV3rqWEN6zMrEZZke0AgTbOGpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXCIoZe0UO2UVleG_w2aRptHbBC1TwMhGCqRseT64E7j5GJmOGxCN-6CWDeo0sdI2zouqOrt4InJJ9ll2P_CEijL5tClXbxlpi9TcVHIo5cgY_yd-0Vq8WlDNwbT7gA29QP6ofncSxzyW3wfMc0jXysPcHfubaptRSc849g_Cp-HadtW4k1ZO2rSFMJrmW7N9HvL_Rzo17zf0uAySQ2UozxwiK_3j6cTmDbapjr2O5Zx2Ka4y7H0L80QpjjT9ikPJHC9g2SRnp8LnxqA2kbw4LOZzkFEtyKTbaUWdxwA3nTqtMW51wpwgoFTbcYPCwj1qrfU_ut-2TlsGXeACtpBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=ifTfWmd1p05nbCDXCEr7XD7cdy8zTGkVUzrQQokZz58RkDN-gSNVfx79MmZPQrZCChW4zfzUR076pYyb53bfQLbQCtmS7z2rGMyO_qBEFwpGukGy-iBFD8GtPcQyHEwD_3IidP6P9kKUdAsmVnTwEAC_-GwgOxPSdd7JNWepAN-FE2FWwcROjx59kHtVpHLErKCaex1QmAaaHgcb57JU3srBuOQlhvmZmn1H4iETIKJxXAuAV8PUdhfN7LTbmHprTxZSLYmzoxFUsyH6jty2Yn16UxMaflIG8EtfpwZLFmeDd7zPTdPXM4zliBc4CEULoapyhUFdrj3Wj_j0rSuxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=ifTfWmd1p05nbCDXCEr7XD7cdy8zTGkVUzrQQokZz58RkDN-gSNVfx79MmZPQrZCChW4zfzUR076pYyb53bfQLbQCtmS7z2rGMyO_qBEFwpGukGy-iBFD8GtPcQyHEwD_3IidP6P9kKUdAsmVnTwEAC_-GwgOxPSdd7JNWepAN-FE2FWwcROjx59kHtVpHLErKCaex1QmAaaHgcb57JU3srBuOQlhvmZmn1H4iETIKJxXAuAV8PUdhfN7LTbmHprTxZSLYmzoxFUsyH6jty2Yn16UxMaflIG8EtfpwZLFmeDd7zPTdPXM4zliBc4CEULoapyhUFdrj3Wj_j0rSuxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeDre-UdD9qCz3M8Qp2ZlxKQThbjSIrW4Ia8xYaYRTtPRf2WP7JPFKZ_Xiq8TEpkg0pJn68VSO5V9yq1hHQtkOd4RWn7ifEWGn2tJ-h7S4Hb3dr-hQ16ddPAy1QaloRryFfSdQtzX42RVEclw8ay7cPptfFjjfT2Su8BHmgC7U6N-Kd1ujrSGnVzptHTW18Xwy7geNGHwOxrSYNgV48dAzo9Trm37piitCC9RNm4ECUqE10hbGA_r27ETolNeA2E8IrechgUP8JNMEK-kO5PSbtBS9SYExNx9CuyX7aq-pgcoXf48Fw2ZbU0c3srTMy1LujeIbSAVQFH2KIkUqLFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myy3EPIyEOC2jFmpyKrJYMnNC5Ug6vpN6XbFuOSPGA2zOwp_g6Mo_B_rcIElC326QsedjOH2f85GDcJcma6ZJZpkpM6H2c0nxEC7V-k5LeHv0_7wZP3Cck-9g9tNL9-BDT5_zQxSyG4TT2F8jIIOQDaX4afnx7oP-XghQY6N5mQ4LsisIDJMdAbRT_Lp7UkENvcslpeqJ_e6czqajefO1Iw20Xu47nKHxpt6P8r800EaMHi2IJPldcuI02l-Ow5XwokqZFWOM6RALK0-RT1AR9M9EhLDMKhdwtjdZy-b6LUcKtOVc-UNycb00XozjHyfq02S4UT2hx8XcTQLj8LjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1vrWZypajPHVVk38avi9RicZjIOvyZvEsT5TVWhvi9Umxju7FCJcg0ls_-59o9nbrThzwTsh94TwUxQ1zzbBSxRgxuU8cKXxQ-6Xfv509d4yiTy1p4RI_a7OZQumLSFUz_KKGi6V5ji3FYh5GthEx3pD0KeGFPzOQAVVXn_56reNoz5g238MKUIqRmSnxvriDvKu9Vb0iu6ObhW3nz_qeL0NoQf_gLm1Ss0gP9wRytKpsyA47CRT8H4NQ7_K6u2rEHuwTKRsrI_ifQFRKfftVuVve9SJQ_FTA022fcqmlxGjUlAHtFBhwmGNuJfCQLfIt8sNKL2VtlBv68wWjhM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6PXY76uBDKpZGtfg9efZhXhAMUc3MvavRsHc6eeg0CseQK7D9NKtwEgJ5tv_dn0-4jCi_oZrmGZS9ytpvHO7QWtDAyzWChsKQKL1DVntgOmSIZ4wbnUnksezbzF3327QsOwLXbH66PCHQvbsGIUCOrb6jw3ww4K9ArZdnjC6Z8Ajys75aqCjxJ-eCnXEhIRAgrjC7sDIC6wxpessAHQ9PIbaeiNVDWm4faaFa-Qb0eR2v33tQTnUQu4LxSQXkWgkbVK1hOZlBahR38Jt26pCiUfN_U-OiWvhlMYHYaJ3CuGc53mJ3Wsfb05_D93ViNk4TeGOZaEQ4EdrP6rLOd2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_tFGplr0VzHzGoy3UL_nvDdf8tW4384Qbyae9bOCibTPDhymebAGjELXtS-sGHOtVtGngORxvayZAD2dIotOezh9jKXUCJX3s1BnMmfxCNRyAIal3dC9qciHXgR3EI_Y9z2Iks-6Wf5NVFuse6o7ZUT_n5HiRorD__s8h1jnitwjBEnFzLkyTIa3GQvCWG_b349m-x-4Oepid7kVWjElRQ1HZdp-rCBhIF89VGBN1IjgUgIXp3eRfYqH3NshOliWLZqURkEfU062rGYwdlnYOpFJ7DLc6MdAGapQKyGWrNF2xHyX1HcVieI8JdmkRYHPd650SdnR-22zsgRFeRpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJXqP9PI9oOdX4OcYFTwyI9aO3m2fepmUotYjeXQdqQhZlbVhHS7XudtpPcSbHTKJ5zxFhJm6DzKKkG4Gz2NRrz-JGJnsatWtnMGBd4YY4z9sTpW1Wd_5XzUzhnEjJk9vWLv8MZ1Mm3a_k_J_w20DHaRfs0IAIE-ctOY2vO8s-jUHzyEwwo_8w_zWxOj05U60tMDj9LXntovpxnPWDyZTlDeW4X6ZHNhUxCNhL06HaPRGQMXJsvr7rBpz64OpDE2PYhXmStILJMGIXmZiuBnRNInxUKqj4uGqpkBQEAua86kVYZ3iJhAOm9tvp7ffhp-QdeE1wnqkGRedcDnV-8miA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=aaBl4yBDjeAeYfxtaWhQeFtubt2BV-X2RasuzIVjgyAUi-nM7SaBRn0-UIoIttb4cUpsl64zwFiaHl6YBpB3ybPxJTpZkveRWmkwytwEcBxSeHIoN58CBC8sbCRpjVZS8giQzRoCEu3wOi1BLCikxNgzGJhhtxH6oPK3u3sN7zsrE2A-uBDtr_6cRdLjXkxaZBvsed_a617hgfkdF8wSMad-dqe1xdKO0GPNYP05FGIWJ4mRI9O-JjXHBEQPMy2EvDoJ0WFETRyDQqrGFEEDN1wRLxiPVRuEJ5sVjKpMoAWXLupQmSIvRZ9oEY-EZbwH-26MxyWtshdI0ij9b4AehpwIN0qryWLK9c7znpb2icbNPnuvCXf7cYdylsuN8rONP20pUQfhb7bWhORyNLmUzppO0_uSVUuPvoN3EC_9uIl5DmOJ4IRv25JKRCoplMNYw5Q6D8fMz405fvJQ6QnmMZnH7SgI4VXdfo9APUCKlV1rDwXGUwi5Kq9qImcrs0Q2NlXHFMGNu9jTqVVEsKdPpVz1cMenPulAnLB9I_j31sh_ua1yecgGZz5C7G9cqLTxYne-BN3gW0J3rmasT8R8CaxAjllhHJuwabJA1v4U2kjK8ZGGihPE-Z9kgvRuHfoamlovz0L1gRRVK0iUvlCUA6G-uQUxuKXJ_G91f6x_HYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=aaBl4yBDjeAeYfxtaWhQeFtubt2BV-X2RasuzIVjgyAUi-nM7SaBRn0-UIoIttb4cUpsl64zwFiaHl6YBpB3ybPxJTpZkveRWmkwytwEcBxSeHIoN58CBC8sbCRpjVZS8giQzRoCEu3wOi1BLCikxNgzGJhhtxH6oPK3u3sN7zsrE2A-uBDtr_6cRdLjXkxaZBvsed_a617hgfkdF8wSMad-dqe1xdKO0GPNYP05FGIWJ4mRI9O-JjXHBEQPMy2EvDoJ0WFETRyDQqrGFEEDN1wRLxiPVRuEJ5sVjKpMoAWXLupQmSIvRZ9oEY-EZbwH-26MxyWtshdI0ij9b4AehpwIN0qryWLK9c7znpb2icbNPnuvCXf7cYdylsuN8rONP20pUQfhb7bWhORyNLmUzppO0_uSVUuPvoN3EC_9uIl5DmOJ4IRv25JKRCoplMNYw5Q6D8fMz405fvJQ6QnmMZnH7SgI4VXdfo9APUCKlV1rDwXGUwi5Kq9qImcrs0Q2NlXHFMGNu9jTqVVEsKdPpVz1cMenPulAnLB9I_j31sh_ua1yecgGZz5C7G9cqLTxYne-BN3gW0J3rmasT8R8CaxAjllhHJuwabJA1v4U2kjK8ZGGihPE-Z9kgvRuHfoamlovz0L1gRRVK0iUvlCUA6G-uQUxuKXJ_G91f6x_HYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feit9T9SmHLHqOzHWaCZFoxv3_VeIZeM5gu--fH9dk16r9vk7t9pATT7frV4zIpCH_HM0E9EUAqpRd4sJzIDpIOYaXEYKR2Qi8sRvdt8YCT32vmOXsCEsOUY1Nv-FytHfYAQBxVvlShvEU8AHwjXFmiHy0_jutBXO4QY0ArvwvZl98Kll0E7sb9R40ZxPLOSRvzMLK9-O5KmW9ohDhRu1fbuRa-7oMU4LVL1IcKuuULEV8tBcRrXcwbLXsEv8OlDhsNxAYL_pzQ_cLtUGzUzgch314k2OV118lKIVGu2Og8vgOFCyZPCffgJ2u7dPXK2cgVxTi-jrPEff4CyBUnTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVV3ydlOVweO4lEegx00dUtGw2GKLaLNqEhPRgkl8wmTRtyWFNAyA0FtkNMfeIZ8WsA9UcOotibMJQhLspbh-LKzwb54WvDIpbZbobQUpQx3REdYVivie_TubuCGmTjGQzUadaVHwoUXprtAt7auX8qG36h0mU1Lfu0Qv96uTIcSQnDyLyFFbyV1-0sceNof46LwVXnFrSYY3yU0MTpA3RWwC4buy0VwL3vxfWImApoZCGQP1FZtTG7kz8H5OoJArOlY7ZDTidt_sTrHr0f-RRthAzE8yN_PCD_CM4qsBC7PgovNFNoD5B9RdDTB0ODVSZkt-QN6zz_yjG_dY_UcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULZNHWxl50nOaFZpPmfesYfjrChaC0gPxyGHWcTn8bOb2z--7JjPqmcy4tFj3qY8HIr2wIDoh9zPd5Y5UQlp0dLfQybLcOtkWdI1r9gZvuLExGotaiuKcsLRcB7klVTOFWoua53s9_1umFhwOJUUwc7lhTawQsIiPcZN7fcQ1d8ysMYMHm-mpcSHJiKI9qd_a7Ec92Lz8kCwe04HSkxmoyLDTv3jbeD_twEsRlIOC_p373sCT_7G8tT-LZjOWTGOeKaMxIZ3yjZgtFhjZrJACQlZqibGm0QX1JpWHjYs-wmKv1Q5J5RtrckrAu3q1vRRIHoEtBVckcICHTwmaM6zRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=tNJCLr3otyN3V42KIV-WqhI5f7laJnAwlx6i2CyrPaorHy0aeWnxlmmyQH9UCTyf6t90Kp2qBCqQrpqu_Is2m_LaTARnIYZ8kWA9AQFvRIGZYNuOgE_t_cWDB0Wkv8IS8skX4Lu7vX1c3Is-BEgEG7Pc9nLxRUEit3gDyhbaZS28m4OykTx2XyqZHtVadaIfnBxFpCjlANfJc9EasSC7SbFrvxQP8pT656YYdfVrRabbYcieqDdrvm3NgRzAMHN71hEL08y30q4ySSlohDKMbA_QApZDm8gMoAtvTWHVg9mXj8pGY-1s-y-YrhlhUH5kLtNinArXJ8eBfz1puFomOBU5-fr_-zHfHAyFRs1JoSx7o_zSt7qu1ATkTg2XuleUNFkRLKN5fAJXlvGQknlhEbRfoqGcZy519xo5qfPcLC0SEWewgXNaVkrl4aFqepYBQOmMBJYcQr14UPQCXqEJvGJPNIRyUtCzcCpgy51BI8LUZwZGmHgystP4Kn-xBa-NwAfHhgg-6zITYbwy1ci-nlkxeiNMpM8txqIkt2sOqvRVEm2JeJ80H1jsUKSd951nBGUbgYASoT_tgBYxYK2h2vB6eM-iXqtZTC3WDRx9YW6xnKCReNi-INrUVFwdqk6M5v5e1-RUHtgqUG28bpefYEMXrUaAK5oIKumsNxspEDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=tNJCLr3otyN3V42KIV-WqhI5f7laJnAwlx6i2CyrPaorHy0aeWnxlmmyQH9UCTyf6t90Kp2qBCqQrpqu_Is2m_LaTARnIYZ8kWA9AQFvRIGZYNuOgE_t_cWDB0Wkv8IS8skX4Lu7vX1c3Is-BEgEG7Pc9nLxRUEit3gDyhbaZS28m4OykTx2XyqZHtVadaIfnBxFpCjlANfJc9EasSC7SbFrvxQP8pT656YYdfVrRabbYcieqDdrvm3NgRzAMHN71hEL08y30q4ySSlohDKMbA_QApZDm8gMoAtvTWHVg9mXj8pGY-1s-y-YrhlhUH5kLtNinArXJ8eBfz1puFomOBU5-fr_-zHfHAyFRs1JoSx7o_zSt7qu1ATkTg2XuleUNFkRLKN5fAJXlvGQknlhEbRfoqGcZy519xo5qfPcLC0SEWewgXNaVkrl4aFqepYBQOmMBJYcQr14UPQCXqEJvGJPNIRyUtCzcCpgy51BI8LUZwZGmHgystP4Kn-xBa-NwAfHhgg-6zITYbwy1ci-nlkxeiNMpM8txqIkt2sOqvRVEm2JeJ80H1jsUKSd951nBGUbgYASoT_tgBYxYK2h2vB6eM-iXqtZTC3WDRx9YW6xnKCReNi-INrUVFwdqk6M5v5e1-RUHtgqUG28bpefYEMXrUaAK5oIKumsNxspEDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjTX04uYdBNSGxUONQUvhc4giOvyC6D4OyoATEm7QqdKWudb41md162IF8lseL_ZUaBAYR0JELoFjprG41AA-3-JY6-CN3fow1VkK06GObWrJdyafh7BcZTg8gQaDFcN9bq8FfkImw3sdEkyX7sJpVwIFC07QpaaGhYj7jhTRfxaRMS5hK54z9VAJ0qGSy4X8pFAT6SesHaGvmHN_NmFfYLBJbW-NvFViIKAsrDipaqXghJhkQ5RsBhYxeG7rQJx5jimDE-mFUwVMdqHfSzI9vY0e4r1PgUyuVPOrUGrtjbG9LbEfaYHGwRvMILBuGEFuSVnpdqHAz5JQT0GE5m8Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHHdKZkWsZj4p4mD_rJtcgLfv_x6R-DdDt4SxnC_Z3rlR3ZLEYdohg1D68YAFa1817ibAZ04qQz8UielqJOn7unJNp3Xb9rnVoFDWGU2G8-fApUvAZiwGvLw6BnWxDtf7_vbxvRyZchp2lJV0ZHT6o1nUkDEzDS4Lc-m8skFWRUdwBexkKcqHCGCl2FCG3KyNsstdurosf0fGBwzZHX78OOBr1yEWV8aAAXcFBu94TssQdXZHVhom7KBdgPpoEegrg3yO9xtcLKhWRsrizyWp4A4eCuSjXhtyn4wIHCLsAjl29hpyU1ap3erz2Dqkt2SkXZA5TsoHLi6oTANxWT90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=ssQkzcc43gb4T3PlDXkzsax5dkpXQoVhrLkX7V5_5X5xgRJC_E28O6w4OztiV-gxzqOZNsirQ1mob6wn3cVTGISeGgnHOwnlT0HVyfJvT5ab9HJR3EwK8-niFkGpD1oXnfSFDk9Mo5N3TZlrulHTJJgw-QtaKYwoAau5oggY0EHythafOVtz41CSQRywcnm-EruVbocEhOg3TnAKxYu584WJceASP_KA8GruF7GzmkOyfhw50LRxTYcc-cir3_fMFYeQHoFaTyTXS8MQvbHLEQb_OgunaYxyHqZjNnYiwXyIjTRr3fizaGylceUjAx_qyU_9yD7H-bxxF1Fh8bZMjglcqgrliEh56zoz3Lyd-MXJiCD8UllQohuICblAqPyfEVtlrlSHqYP5JvpXDHpbBhkIziJ15dsrhZa_S05DrPWzETGEMbFFsI2OHAYeeYy90FZqsNDwmwXYoze3jsBh7c-zQs_3aJf5W5k2i1dwlOIuOjpWt_KA3KdIGMy90zF2xXtTz12CroniuqtcSqPg1C2txmpFXouarbUclWD9ZbkDthO_rFnUSQBsu5FkULKSH2imXBa5UGAyubpDmrsviGU--CyQ8tNgQSxCmv2LWBlN4q_8IC_F4QDjPvwkFz5mAHR-bPPYFO9m14WCWQcZjZdE0HM5zriv4SQAMYlVNE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=ssQkzcc43gb4T3PlDXkzsax5dkpXQoVhrLkX7V5_5X5xgRJC_E28O6w4OztiV-gxzqOZNsirQ1mob6wn3cVTGISeGgnHOwnlT0HVyfJvT5ab9HJR3EwK8-niFkGpD1oXnfSFDk9Mo5N3TZlrulHTJJgw-QtaKYwoAau5oggY0EHythafOVtz41CSQRywcnm-EruVbocEhOg3TnAKxYu584WJceASP_KA8GruF7GzmkOyfhw50LRxTYcc-cir3_fMFYeQHoFaTyTXS8MQvbHLEQb_OgunaYxyHqZjNnYiwXyIjTRr3fizaGylceUjAx_qyU_9yD7H-bxxF1Fh8bZMjglcqgrliEh56zoz3Lyd-MXJiCD8UllQohuICblAqPyfEVtlrlSHqYP5JvpXDHpbBhkIziJ15dsrhZa_S05DrPWzETGEMbFFsI2OHAYeeYy90FZqsNDwmwXYoze3jsBh7c-zQs_3aJf5W5k2i1dwlOIuOjpWt_KA3KdIGMy90zF2xXtTz12CroniuqtcSqPg1C2txmpFXouarbUclWD9ZbkDthO_rFnUSQBsu5FkULKSH2imXBa5UGAyubpDmrsviGU--CyQ8tNgQSxCmv2LWBlN4q_8IC_F4QDjPvwkFz5mAHR-bPPYFO9m14WCWQcZjZdE0HM5zriv4SQAMYlVNE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHb4fE8seqvUwWLso90IMpSBTnnfPyuUO440Yo-6RYRL2ahzxXA2X7qQDdeUL4L0UzrXImUMfmBgwiALUQnJLxy1WwNWfigGk5T1Mg7q6SqszskFj9qwMaydHvHW5SvPR4yKWyCYFqWYkdjx8-TL419bBEArlgbNCr-exdGoLnj8SOim7zf-AC6HWQI_m4kAAwXmWTcXn8U652yubA8cSuc15Pguv0lzp5yAyvZcYNVt3DRFaVOuPmrjDBT3lmwTJ0VUyZxQQMAOucurz_8x9ej6fFXst4GhA-2462QbH05w4NrvmvidccgpEvhREY952ldUFhZoNYZKb-b4YuOazQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVPqEzSdI-bC1lcVUDAH3CdIGjmV6GyDSqwy37bxIzIgNAPL-GNjBjGmOHw4Psu45NctO63ZqQoVZKmzakR-JcgzLN8wr2BOzQ2uoxOul2N4b6xLjLMqAla1nasTWyCcYZbfDq_1npTs8YD2mCL7IUVT_bxW5p7jw9OhRbR2SF2JVkyJ2XODitOz1ZR5MQLqBTJKc_1SxmE4ujke8J7nKXJT8MVQomeFYtmU1KMTzf9NSftS8H-pkCGn_L7dRMBL-oC4Gk8HC5KwF5972rJnGk9auYKQpJ8g3csZzWPOx7OFOW4nxaH9AgVK4sP_Y31Wd6kdsxHBS97Mn-8UwiwUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=eTH5f2jbl5gC6dQNpaGFryE75tAhUjwb2Vg4VLZ6rFovnatj_dF0XanrsJIuDHMTOBWvKXcDQ3yqBI23d3EqXyJhB7UDYH9TlQr6WxbbnIPqTT1EDhzpmsOJfNUt8PUPZBT0j1z7j5gZUdiL44n0RIEoCmWgkRuWp6E2RfppcTaiJr5FY_ZQF-vczoPjxIIjBm4kfMpUmx1LgsttKHkLAq27kJ2u16PaxK01rentkjWjLZAu9IRMNvIZVenUhNgFf8QWF_Jb0IdN3pmwcizXLdNN6xpUpEwbNS_VEW0yZ-sQYQt1nALOnbCW4g4vcegCUVGp1SFVVoKuEPOPkNhrKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=eTH5f2jbl5gC6dQNpaGFryE75tAhUjwb2Vg4VLZ6rFovnatj_dF0XanrsJIuDHMTOBWvKXcDQ3yqBI23d3EqXyJhB7UDYH9TlQr6WxbbnIPqTT1EDhzpmsOJfNUt8PUPZBT0j1z7j5gZUdiL44n0RIEoCmWgkRuWp6E2RfppcTaiJr5FY_ZQF-vczoPjxIIjBm4kfMpUmx1LgsttKHkLAq27kJ2u16PaxK01rentkjWjLZAu9IRMNvIZVenUhNgFf8QWF_Jb0IdN3pmwcizXLdNN6xpUpEwbNS_VEW0yZ-sQYQt1nALOnbCW4g4vcegCUVGp1SFVVoKuEPOPkNhrKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz5bPUJSePqThGka5EOHDRB7EFM1tvw3BmDtfPaE83T5ftmEfWr9gTNUHuKfQumH1Bc5EoZdX3nhJuDDHXnilP_Rx1QC7-7KpCMtaC2S4UnxCKUXsGlDkV5gb877xOvyPmTGjc-7FrV4GztlU6yJfEnWaqBLdww3xdyxHY40lwTNf-EKqw3V7ntGji6pb1OdzXAxVy12s5AT3hAW7qD4ayZPfjWB7Qaug8-wg1IglunLdVBYKkKp65d1yavbOt9vG826N7c7zpJElIS5ojUfl-_DFV8a-j0Qy0hb4CAseVE8SogY76yv4Igt18iz8TjpES2bt9g_VSm57ec6xGogOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpxQs5Zi0ctaM2sS_X9SOubg7Pdkc7m_xACN2Vky18lQacsn6o2Ij_BtMLbpOpB1XM0VWNPPP71HDuQAPAxaSIgN-i78yruDeZCIOjstVeELGPmbHWv2jsxJwqP1Nn0qHYDbisaC56g2gcd7T2nlv4dLOasPSZupUtysdefVkGPP9iAFYTrfCW4bMWthuf3pDivdTiC_F-T2o8_QpguBWs6gzprMkbR-B5jr1jQIL22w4MhP3SZASrJkpXBJpdaypf57pMAt0MQcm5Nj3NgxuCLypcLRkqlcszmwMEFmiqcGFgqyR4QInWJpT5URdqGRDJ-I7a9SBLa_x-sX76udYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSOVXAhGLs87RJyt2ZNThMQaWztIMYoKY9vlJU_khizHeqpxwh_skVQs_ZZsh53Nocb7aaGmrJ0hB8QNw1FQb5qg2B0tu0Kh3FPhn2Vj1U_l2aqaZJkByQUQHQKJxxP8FdFQF41udYCvD-cW_-eNpspPsd0-RoXrWzjMgyrY7ZWDZCVdpmlSqfuJrIgyZ1z4LtT_oUgHOTCSQGyEILpg4iWfNNt3IEd3CB9jmVr5WzO98Lvo0HNmespVMx1Q1TSllGHKSPT_WKlZhuvGcsfq5kbYGAe4uT-jcwrEyuq9x8iTHOY6U0p1vobTADSPUiY2cIgTwZjZi550Br9lxYOb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=Ry8cRGbEIk1jqHWE34KlqJEDZ7SGouA6omMjxNl662epiGWFfT1Lqklvls-HUbiMb0nEtrLnwNwBtGzgfcza4mkkr8Tqs5vFIutRuDu6_wMxevLsKoUMBx40vOSOYMFVuy_s5RIPy9rkjU6DyQY0xqRl8FeIpI7DSvgbAiKJ_5lz0axFAdPveWNMxe84psbma56lkQAvRD67OblCtIAw-RQf3C6a8znoWkSTHd0eQOXQOXf7SBzsjAZMAldpXvfi8XZlEVQ_XkrLzGeeN1ScpNFR3ZKSGwuRMgHWSBgPZnFMlZh3yKiquUkz_JJNDxw26PHdwG3s6nLLDzWT5NXwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=Ry8cRGbEIk1jqHWE34KlqJEDZ7SGouA6omMjxNl662epiGWFfT1Lqklvls-HUbiMb0nEtrLnwNwBtGzgfcza4mkkr8Tqs5vFIutRuDu6_wMxevLsKoUMBx40vOSOYMFVuy_s5RIPy9rkjU6DyQY0xqRl8FeIpI7DSvgbAiKJ_5lz0axFAdPveWNMxe84psbma56lkQAvRD67OblCtIAw-RQf3C6a8znoWkSTHd0eQOXQOXf7SBzsjAZMAldpXvfi8XZlEVQ_XkrLzGeeN1ScpNFR3ZKSGwuRMgHWSBgPZnFMlZh3yKiquUkz_JJNDxw26PHdwG3s6nLLDzWT5NXwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fiv15YICYu_kXCdtI-m7qChXdaO4wIPl8-YmSsrW7l9k3akz9gblz6uceg5WFel9S4SBW3gYQNXqe6du0q8hVArj5I_Jv8z00sFCsiHLtStbdrOmiVytELjRRLy93f3jQqSzugtLlI1gT1F9Hmm9koPV8LlmW832EMagA2VHUrF6Lv1CwNqUbQIRqAH8CMtXAmQ3EqmKV-PnrOvddVF_ZcKFyd4KzQEWdRb9QMKTsW5ortVuwB89839Yn9zX1GGs-6nktUUtJLmjpGWbJzdDaycxrs-BSM9NPanxpUNODXXvNxRd62NRdVDuw270NZjOyn0Un3WbFy4105iphdgEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHNuYqySPwurN7ri0kWfc99_ze9FERrhZ_Au0yP_1vTYQ139b0jc4tTvVg5-iVpKD2PlyJ_HE30dH0Li435bWGakDZvAcEqDK_q3Xc1dN1eXrmrzKX7shb8d7I-eTZygCXRgsL48mko2-0OlqbI_oEOENJ7ta0ujL25iGFuJjvgmMNx9YJxyqyDVhTgm30L0SUuXLGmCKx-auHxvIC9rMyQS8-co6z_WcKwXduCKIYmwFf8PNz6uFQ4lX4lQdMppbVoYa0dh7JP_xf_-M9vj0hlK1pLI1zTjtBgjnriDOfSQLlwKjS09TGOYDlIJWDiEqKKcEffzqtXACHdtcQ-A2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl2K03D4ajGywBHVyS_U0JbdQLc1r-2i1idieUaIod-8t57e5yCdgNgBKZ9IK5OIgPvU1HvT_tqueCa_beNffsDOJkS0AY2WuyOIbcx0BFRuTpcqrih-Xf_Rspx10K8pD9Z819stS-ZGW9h1o5lBjVlKn9tDtNAN_YMdL3IhQjKREnrXVDt2mP75MA6vCHCkx0NUoLdu1cdls-p8mi8_URDqJf7SbtXUOGnZ4vEbInTyEKb-Rxf-WrfguBtI921ebcu73GVZFvC2L17gz9SYcCW0vHD-vX9CmqOw_KFQoZwzLKOArPzKGRfCttJ8EcZgaWROuuZ0s2zeKUy0vJBpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGfq3KWuQ5Lun3rWNKRNjGqSwqUN9zVsm0X2imyOM3JFwioVjRM-dfchMpzc6BawkaededJ6araOIitiVLWOXzvn4uy83ynULF1i1XTDREqEox5HGRMaXR8CbC6bV1bF1qAccWJUFWozS5fRexxiJBZdACH9441e0lPaLWXScs_VEcMZ9MnoZDygHQZAThKnw7EZeG8MO1eSMF65uTseqKKYMy_Z517F1ECq-PcpuEx9F5VzoPuDkA_Uhy1MQ8bpCl5d_CzTLqLRz9UhbgmGnP3qG6eVgt2Bwt-XZtN31qak7eQs7uQrl7eE0nKf2fhbanGbgbX0WWSyJRBk2BL7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvQYY09H1KnfmfVswlQOZPU0mX5z6E_oyNzejFFG2DmQTaLm-vH4m5pTjpizuZSQrvoIQuBQ_tk7xyeglE7Z25VTzKgAIVyWQSxlQ8Bicx8kw41V3DI2je0_BcsBHn_b5vYthQhudHJb7JQk3QgrKhY3sqm8xedmYViFKgzoWUgADw_kMRTGUKmVzYRkYGvwkcMt8VBJZatSpstMo3bpluyuEhyMu37ryEJ8IJ1VXDJrPhlHpMej2AQcS2Xxbw3NUL6D0Kgyt12DYunyon8grwKUMC-6TNx9GhCTtA1BM0Fwsv5zVM-Yv8mH5sY4RI4-NiUFQgm1iwuzcLPmBqZfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JemmroUMqIofuXcSDE3QxIPdyg5uqJmFc4ribX400bgWbS5XmFINLWK1MW6cOEihEzbsHVe8zAJi-W-9TkxxeQqwBbjJijTClOD0bq6qyq9dT-ih8JTUOTHQtASvyNY6BvDVt3goH8VG06q4NbdPQmi9HRDVNELGPJeqlUhns1cFdtMMXB4aDcGErquhGG0ajhS4xws_BNXIshgRFiK7s10f7SX4i0T1xI8anhv9unNmfnJ5DoEbOn3Xh3uyOpHiD0MUGeh_3aKTaU32kuzVohMxRMA72Hh9bnFt5I7Z3dfqPnITcHdTpX-rpSGDtLB2Dld2ltWlXwYPT-y3t1ITVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8rcfyoskO6mpcdnH0H18gfqepD_nO1CUhs_dDddTorZ7bgKyiDMP3UYOhWS3KOATO9Cx8IycNZJwtYjodFz8gLVoD42ZlOY7JrQmC_x8fFBGtEVTt0X63lhp_T2ZtbAlSEHoymqR5ZrBEwZAaSRlH18fYsJWXN_yBucZWZErq4Zt7Xs0dXIuX-ssr8LfhAQPHxzzpDxsj2FV6oz-xZ5aUwv2LNTnm1ievCa7QGFc9wi20oISPAXqxLa8lC1NPOXS03ssmxr4cFFFscuY0u9kb6A54hUu78IkN_1GuZrKqmUh6_ySYP1w-uz3Znpy4H8fD6upGSk0Q8AeOfMm9IgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVwDZxnQT4jiHv2rfElxkrhQrSD9ZtFTCB3EyYH5ijI3hKhPNypx0x1m0aq6GLqi4aa9Yu7Sv5w4ZG5AgujKbjunOmdjmam626nmY9xGACQ2qNn76Bi9iigjV_TKFD-XgQHfg9-FVin3QXE_6VffbmvjnRL1ZQ9QsIV0GXFTb9tatoMMYI8YWIvXMhc1_NWHUO1QWCUOR_YPyuminUDsv6-cGLfaBXLPQ8wP-tgBd8ab2QSY_mNYz6UnIShqBDQuXEld6o3KbonfckrMd2bbMe66GPdI3iBPUpYbAoLPphqjzUt-v-yRYEoPFiWigFmrBVSu4x7tVxr4uYqllOLQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWYP7k9mRq6No44zhkO6n1Hy-sWMaaUtRox1CAkjeKTxVoIwUKuTsoGFYP0VEhKsEFlOZ3Z2XE8xkcnE7ThBivKRGoX5IEYh59IYEiGCXHAQFkxISeBr8Am87ap0oCJb-i-h27zvYxvREpGIH2mm_bNX8aL3xhIKT7zdghKs2ABTqiikGKvfrei9wkl7JTZ64-eNJAu26aTuT45-QwI4QA0YkgDCYzUGXrJ1YVGi-w2WaA4LH_nSds-IXsl-gXvg-BzBAs44FnE8FEVm4AL9Po9iXwpf8BQ17Ac7LNdSLp4A8pMqgiaDgm7kD9QJYk84MNRGFqRjzaDGxjFfvHXhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ-WnqPL97R2JyEmL-voSRtV8fDHkUYm-kEpWNCUBGW4OYhZTBfxMzcU42O_ZeMiFvmGstlHhHUbvlsRPMk74u3JMcvOitRQr2s0cTnC-E_DyTZjNwM5OHnruUpLd6w6Xr82dREiMtUgGOfcz1kAkiaeFwv4ysk_ENZI0a99_Jo_T93ZFA5vCmHa-JtugNV5U7RgTS53o6PpDC-jMDhp0WBFMnGNImTxdq5BQp_7Ul51eOmdqGlQeR2rVOIIFxvmDw7ylXx8J8PrVjV8EEy81pDIOU2cSF-tMT9GZt34UQx8YbqfTIZZaxzMKvjY-iUaioWGE2tqXPWXzu20zU8qBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5tAbM_qdT6_ZGjXBC0yA3qumvknhu6L_2K0O_hJv4X9nG4mtVO8SJbH-yZQ04QHOEPlVuSkFcauK7HwbeGgKnsjZCe4NFESTwFHz2t5Tdx8OmmahFsyISiGyiayw6Vqp5W-fYF62HUBZTUaJSQkM7xZffhJeLBCb-bjcjiIoZnKIorOdgnSdZuq-Re8s9DaiQzDIBasozDFQ-IzPlutQ4gx5fEJ-AnKK8vrxvzwUldS-vwC4-jY-fEtNKZv8M9NNIJhqbnvWkuaDRAybalECEagsLk8wZBVBbmQMyYHw3EkUNrKdmeMIkjWdgz6YThwF1_p03TEkJjJFlmXsZk2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tefWvW9RrequtfgQBV1ub6iFnewbZ3a7I2okQsyB-BxPoytyaQ2-g5g8qglfYfBFHjNDCpxBGWkOp-QGLMWqt3tDrH8xIAnI2MuDVqbz9lfDqs_5M8_0ad2l8EywDh2zT752HaB3Jfsx28kH-8ZASrPx60Y3l8Oeb5B9e8Hs5EVFD2O_4N6w2Y4BdDS15po5jMc_W2vtx-nuVvYyIf0-h_034A9aNMeH7iaoJgDlA0U19rgvxG9OvcMrzTPopziSN6J6W1kzuhEho5OEFgFP3QIMdjwji_pHhi_21A9RxMkMqqGAaRJWjz74hvnd5XnL9YoM03BqdMG25HmUH6GoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vedhHX2BlLqqe7Dk9w_xxWQo6AIO2eKoHZu45aVLl-m47z9gRKtiLsqu_BMZnyvW9FCCZgr0JXepSqvPa4YY9rjUEhnDwH8HN0WniDDMondmYC1ZmkeMktXmXHqlE5hbe4bVCMYJV5CC0Ed2ENGqDFGrDdKhZPJvdJ8Y98p9SQZK9ZigpBAmR39oSP7YZtRDfV4etF81TgFqWpffgwWnQJoyi2G0enYEoTeajFDIEJuzARdEWhoCA_aNmOuKP8IogS__iF4cuNdvXQQl9_3m0OFd6IXY-DdlzYET813SoboIFV5BLq-5xEiZGSI-S722ri0RosK3272o6X9Z3ya2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQMGdv67YHjL_-fLO9CBYctgxe1AoJ50dldMnB4j1Pw6vduRwtMzhJ28zjQzTK5N52n_GSlLW8sBMYcft_yg_ycFrPLPW0rjcIBh66-a-vZffEZu3jLg60vbb2VL0p8MMyxV8lyjVGvo9WviE7IwVGUYvVGlHuPhWg051xKW7Js1Tzg-0gNZwJD1_LwZkOkceZrbyO_lxUo1pAl5yxlXuaAhICZZjGxuEl0Pk1yp8EOvmktI1M9gbUvOKWEV_n-FeUoCZDIVnQidb_GPk_gMpds209ew8UCiRCWVIt2buczmfiCnJpI-fcWa2l1ph7UbWFdV73m4c18K1elaHrMYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqxYaSJP1vTIu9vhnpBevxx_uxxhGVs_q0dsAUN8Kj2kuZzgWx3SHh87YzSjypMjpWhpTksRTzU_vXsawagp6YMWQs9S0iejxbF5D1nNLLprfrrwlKPFPyG20YJe8g_Rk2HrbZrjpWOGTvFGSV_O5GTSOUPXIeaLmw-kd32g0dEAPda2wmUL6LxJHt4frzSbtvly6UaPj2WJd7hfMpSldmKav1StFXWzZ9ESJLvi2eLLA6dVR6bRdFZPkm3pmag2zHiGVvLgzHqgkVkFkXk_H6beAiTRpP2wu6x6xbP2NTr3-sRzDJe1hmiq7tBAhugXo42ZO2IFT2d0gsFiFeB5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYZpAm1RxnmN8T2Rasg-7sQfbS_E9QlkJCOh8EPMG22QeKwz5ivnxgMpd0jWssAgL0JRd-MYX2DWL2mL3LAvTyeFS9Leoy36vOGWrtz3yuix2FiGDThVGWOb5lzEfafmpbAfUcy4SXG3vWQOYzWcDh3Cll_Uga-EXHkE85wiezWu2qrzlDhguKpRcmMTqexTAH2E1kFM1sJZlvDAFwIsUwwQj0eRhSfHeqQ_knVXPLGAf8TVDGpJvbsIEdbGqmZBVJxHlHb2PibKmtq9XJdUm7UojyJoCrh_e_pbI_NUtPvVzTyzeCHO5T6QCCaCTz02L3dSAnOWqxT6kqOaoVeUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toh6M-EPd9lMo5zhxSpU4rXKwO2aSMYvtqJEsoJh2gq6QqEGJutPnju7H4-Zbnj6RHRJi5RYCf52YsAbEuZUvBiXBrYCr1m1oTx_rLgYu5rEE_hjm7rTfu4bzgkA1ohjS1f9BD5LbBhojBHsM62-8iFrQFaw7_oOSaGRsf10RNSJV2McWl4afR3ZaLZ9psLvu8CUrID_PEKrm8DML3_N-zqwvy0-xd5UGEMR4643oe6yFWhhEpZitGrockyPrayS996plZAPlvq4UCAYjODw7Wzg3BMighBYBTNk5GwWco_2BBfpbJEmvdk_4MHKo9BDfQlNgIdg3stg-Ogb80XLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=GADkQPB95IJAQUH2qBxJmAe_hJ_3zpHXFJLZn8RvQcwKCYZtkGvoGJHtN2KaWqBKqZO-G4s7l2j0UIeqUg9hCga720APJq7_IrFoV3U-oMgrfYsaXqd1NrRCob3VP02wCTGZWgWCe5dxoDbd2nbZ3QIjCZ3pOCPcXm7VqL9aE-z0f2BoVLa6JYS7_vyIQ7WWq3ZSqHbLT7JkuFRjLcDTH2wjp_UejGwWKTl8m4d3bZonWeFx2D4V8AxAm-zrjRSthqRRddyjryzcjtVtY8ehCV8FX7pF7xjdr_9jLkz-DCCd2KbBjJRty5OOBKwhgtBxpjzLaRTlQs1ETvcQSctXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=GADkQPB95IJAQUH2qBxJmAe_hJ_3zpHXFJLZn8RvQcwKCYZtkGvoGJHtN2KaWqBKqZO-G4s7l2j0UIeqUg9hCga720APJq7_IrFoV3U-oMgrfYsaXqd1NrRCob3VP02wCTGZWgWCe5dxoDbd2nbZ3QIjCZ3pOCPcXm7VqL9aE-z0f2BoVLa6JYS7_vyIQ7WWq3ZSqHbLT7JkuFRjLcDTH2wjp_UejGwWKTl8m4d3bZonWeFx2D4V8AxAm-zrjRSthqRRddyjryzcjtVtY8ehCV8FX7pF7xjdr_9jLkz-DCCd2KbBjJRty5OOBKwhgtBxpjzLaRTlQs1ETvcQSctXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=S02mSPqeCVftwOyr7NRJgQffFZ9vDXAW-7l8pXq3rViKaGMUmdxIM5mlGkaTR16h57djtva4jsKqmFpJO3gRAjenM_IcSmNRaJ4ZDqxFDtVr8t5tQke8fMKE_qKZkLH4m0KIQeE2c16TQF5kttnlit92dbDilCwb3I1w73s2f8mYZJ5xLxJuod4iY54zWdx4UfoZF47cADTGqy20zKuhr_H-pCFVzPJJ4Z2I4FB0mAYSPevLD09I6zcC2_EDnnNdY8_JI3HALWXM-jpA6PyFz6BJ5NHCLf9YasCL_T-hTDWMsSUMLMCnNNSyBRL84XJjGY75eLBaikCZDrBqyKYk9BJoHI-fAxRxe39L-i5oRb-74oWSHlAIjboNZMmAdTVvswnzSCYi5vkJZ8Bs_qhtxRlYh6Lvp9DdVft7fWHZeE-pcQGOyu8Vb82v__2G6bZdXEE_BJtk0oiY0z-wSXfyzKER_vkEi2uabC2HTSSLd93Q8gTIfuKzqCRLlzOkOIzbdhRRt-ZnG_qqBcWHiYeGDUpCkVQt4gyO75-2JwfimQmQl-C76s1X_9qK_RhDNEMiBIS4Ojv8BJdTfqX6v-VJ9HsCx8WfWmVRgQ0o-EBPaNbUNwV7y3x4Cd_SO7qmMpTXnIUbH4OOLdxHoTlk_RHnpLNwH8ueqE9ROQgx3NxIfcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=S02mSPqeCVftwOyr7NRJgQffFZ9vDXAW-7l8pXq3rViKaGMUmdxIM5mlGkaTR16h57djtva4jsKqmFpJO3gRAjenM_IcSmNRaJ4ZDqxFDtVr8t5tQke8fMKE_qKZkLH4m0KIQeE2c16TQF5kttnlit92dbDilCwb3I1w73s2f8mYZJ5xLxJuod4iY54zWdx4UfoZF47cADTGqy20zKuhr_H-pCFVzPJJ4Z2I4FB0mAYSPevLD09I6zcC2_EDnnNdY8_JI3HALWXM-jpA6PyFz6BJ5NHCLf9YasCL_T-hTDWMsSUMLMCnNNSyBRL84XJjGY75eLBaikCZDrBqyKYk9BJoHI-fAxRxe39L-i5oRb-74oWSHlAIjboNZMmAdTVvswnzSCYi5vkJZ8Bs_qhtxRlYh6Lvp9DdVft7fWHZeE-pcQGOyu8Vb82v__2G6bZdXEE_BJtk0oiY0z-wSXfyzKER_vkEi2uabC2HTSSLd93Q8gTIfuKzqCRLlzOkOIzbdhRRt-ZnG_qqBcWHiYeGDUpCkVQt4gyO75-2JwfimQmQl-C76s1X_9qK_RhDNEMiBIS4Ojv8BJdTfqX6v-VJ9HsCx8WfWmVRgQ0o-EBPaNbUNwV7y3x4Cd_SO7qmMpTXnIUbH4OOLdxHoTlk_RHnpLNwH8ueqE9ROQgx3NxIfcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSFWoZU_phiek4Bgxs1Vj8-6khiF16mubaXc9e--fNcvdPFN3DrN3CDo_ftfJ5SLsNy8ZXXQZ1f5UzIKvV4PMsMqJw8nswrbD63BaTaclDrWDl-NaStG4IUNHzSeehsiYx8Ld8mL2ZArP7wot7DPmBwo0mMTAD3LIolvRgJ90aHTvNx_oi2KLugqIRHQhk0JD3BgTNNNmtDy8xJnxjIHehEzXCI9sPXziJS_AguOYy1GhWcKNXuChDDlniRV7zFC6WIQx8A-MJbjC4bCwCSfWJMtMqmknVSXXlCy2lMRS5_NkDLiGfW5_IHrMKtqKy8kWZIpddWv9c6juRFJlTjVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgRSCC4CuThBZHe7QldSV7KS2LmoLMjMLEu70m-Rx6WFIyyKMX3HORYYZjbDosyBix2qHczZ7YevWERW_NFZDt7YdMmoefNNnvkjj1FvN8wz3IQgod8XaeqUPTSE9mqKTG6wBONUECIynv10-dd2H-DbVkOYSkik73BlzS5iHyme101kXTzso5UEftW2O3s1HrIhES5xxs7VSwqH0ajDiIrfeZIufcwX4a_YA5a9UZn_fsdTaW07_HfzGqcua76ZVOrlj1DBLEnRNXyRI1iIULKKzBwFDoO2CzLvangHxVdjo01j2UNqai1W7zkdfOEOcrqisLXmc_ovylgiABV1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3iQg_x85XSkNQyYSPJjswvm6WUVdUME1-xO8mbY7y6YeROhZpSg3KteTdpIeLMoUmjSD-uyt75vvpCeRf0RA6ompb-nkguSHOqYF9f-Q4Bq0JrIVB8wftnxZ1zH-ZH4MVI6b1-6w2JjUMn1NkkFuI8cW6GiMN5-ep-4oo3PIxFyzBtll9SAKciw64HZ9PesXwf6RhU5-YAHEJPNftAPQhmuN0zps8zrPgM-z5CwzFwMFRq27zOzp7DFAUwKkSGIIGLPOMEHfS-1kFllTBTbzDT3tRHFcmqv8gNFb2k8iP3xUE7szyNFwhFkyAtw6YBMNy-re1FIDxst_N3w-r-ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=umb9td-R__U495eo9Rp9hdrlv9tA2_dgOrD7kOIA1JpfP7wRM-D1oQepgz94rXDjBRAkSRJCEi-9Hs1rxYI2dY5SBSKFCDNx2rLlOKFcgwXEjyUHo6DeIcPeA7TkYRzwjtoCW88ZUOuLpeAh9gXzBo5Ay3O8duOP-WLyRVJQYA2xmT9AKUv_78JwNKQV8VWHvfQHyhG32BU-wt8kcVigo7cQIpz_mASX1Pr1oMecaDzSTrxGrC8xfZLRFz00Obg2lLaXHzUclq0Ld9nJpwBZJYWdZQU4LB0qwUNl1XiHkR7ON9zlmMJwFvUue4gJNA8m4V23Hj8GtYXI4_qPwVXPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=umb9td-R__U495eo9Rp9hdrlv9tA2_dgOrD7kOIA1JpfP7wRM-D1oQepgz94rXDjBRAkSRJCEi-9Hs1rxYI2dY5SBSKFCDNx2rLlOKFcgwXEjyUHo6DeIcPeA7TkYRzwjtoCW88ZUOuLpeAh9gXzBo5Ay3O8duOP-WLyRVJQYA2xmT9AKUv_78JwNKQV8VWHvfQHyhG32BU-wt8kcVigo7cQIpz_mASX1Pr1oMecaDzSTrxGrC8xfZLRFz00Obg2lLaXHzUclq0Ld9nJpwBZJYWdZQU4LB0qwUNl1XiHkR7ON9zlmMJwFvUue4gJNA8m4V23Hj8GtYXI4_qPwVXPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF_zhEjz4tMHrT39-jRnVtEvAL7y_32IYdPflQy5Tc9E80Di1WoC4--JtdhzeMfVso52QratfJAew1lkobA65AnPmdVs7jhANf-i8hC96IKH2s-7YQoMo-_7WUGlHVoVxtIS03eNQNWS8_HNKbvpoMA1NryzUDqcv6EmYOjADd4hSQSQX1J7D2FrUrHZrh79C9xIBJ4O0yQEeeK3DJZmE4F6o3FzlvfS_DfU5jygLBWUZpIGZgTu64F9veH9yT_bId-3NCnuuiadiheof0bw3F2j_MceHjYS9SbkRlntJcuHT5GlcyBGj9LsMcTHIr3Lr5jqpeJn06XbHMjYxrzS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
