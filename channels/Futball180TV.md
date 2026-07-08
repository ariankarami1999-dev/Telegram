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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 612K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-99053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Y_TdKVRwfsSXg5OwRG6t7b_SaIYPB7iduvgcR1DSDOv1p8YDzq0tjs6HNNYBDRC4dHRIzdSn5OlVYarIR39gp8Z96ePE4wwLFActboUOVHSGn9HF2cTluv1mN5pGrKymKgtQXUCgdFMmk3F_OHRRMaa4V6PNHLw4KpoaiT7evm2zXF91ZMcvSSrQIqcy6GIRTSh-nb3_03k6N5fsCdJBTHIhezQVF_O0qVosXpMKAkJVSFluPBrciT4-Ze8Z7cD0pxVjupEMXlAW-_3HpVw9BYMsx5xNlfa7jf_b0Cxf9y3zrhrftdI6bziFMo9QtR8oJfA0bgnhnOxdWNSrxeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عملکرد لیونل‌مسی در ۹ بازی اخیر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/99053" target="_blank">📅 18:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipTIlFvut0dbNqbuEWVoKUKedSTLv0vCJYjx3K_6TGYyPjq9_o6z7cDXKLPF3JGugzQQt0xI1QFA5TS0MVBYRchtxC0V-1kbTI1pW_Wz-DYIG3BA3D89cRChuVdmOIM0TmYznn2qlKyqYQyEA-dZpfkRVS_thy2am8gD-4BEMMsK86SKWXs0yfbP5tBjuaC3Bvnyrn0O3bz2SAmU_3C9oW2eqZELksDdx3Xrh_maUkh-3Awy3A2sSeUWALUlJeLDw5FCa_cGkJsf7UfO8fFgBk8SO97Xsnjd_yB8vaZTR2XJO8IHgPcQAL7VPK0VCS2RX1COsueloIiV6HjuDs9Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇬
ابراهیم حسن مربی تیم‌ملی مصر: هدف فیفا برنده شدن توپ‌طلا توسط لیونل‌مسی است درحالی که همگان می‌دانند لیگ‌آمریکا را نهایتا ۳ نفر تماشا کنند و اصلا سطح فنی خوبی ندارد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/99052" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇦🇷
صدای وحشتناک شادی مردم در خیابونای شهر بوئنوس‌آیرس آرژانتین بعد گلزنی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/99051" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=aUS3pD2XHX3E-KkcLrehIXWzhAWq4lM5Vvem7cAbxtXG_dHRUbEPAoUmO9t3yQzJrZ4T3KaP7Rq5nlUPIh-APPB4Fqt79H4kG_KWGV2IXKanbzN_i6m2m_73NsxsoUTf_KdHLU9uoFXiHL2VcDc-Zv4XVadYfU9Z7F52-BZkVjL5PF_dNmq9nE7MGpV8g1T4w1G01AMGXe9wfgPh519ZGOYEValwUXF1kClJgCggy7YajcbUaBaW5cAMAyd6yFGB2oAohZRcquXgOQgwKxR1oLtUw5C9AIRPalCbQGc1I_zqhhgXWnO1daNjubF0tvo6D9lxsegID6fvVc1hJwCEQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=aUS3pD2XHX3E-KkcLrehIXWzhAWq4lM5Vvem7cAbxtXG_dHRUbEPAoUmO9t3yQzJrZ4T3KaP7Rq5nlUPIh-APPB4Fqt79H4kG_KWGV2IXKanbzN_i6m2m_73NsxsoUTf_KdHLU9uoFXiHL2VcDc-Zv4XVadYfU9Z7F52-BZkVjL5PF_dNmq9nE7MGpV8g1T4w1G01AMGXe9wfgPh519ZGOYEValwUXF1kClJgCggy7YajcbUaBaW5cAMAyd6yFGB2oAohZRcquXgOQgwKxR1oLtUw5C9AIRPalCbQGc1I_zqhhgXWnO1daNjubF0tvo6D9lxsegID6fvVc1hJwCEQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم‌ لائوتارو و همسرش بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/99050" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99049">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: پیت‌ هگست از ایده ترور مقامات ایرانی در مراسم تشییع علی خامنه‌ای استقبال کرد. ممکن است دستور یک حمله تمام عیار به ایران صادر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99049" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی از نیمکت مصر در صحنه دریافت گل‌سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99048" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
آنالیز‌ گل‌سوم آرژانتین مقابل مصر؛ چه ضد حمله وحشیانه‌ای زدن و انزو چه کاری کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99047" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh6JE_Q-v099OYVXm28hZZfkHsP0a2ETFOoWlfkyR74yLSp8kzjkUP6H2XucTqmZfp4-DA4JJY2B5_cVXUmm8vn3BSbHkY2Wgehcl4mXxPkweoXEmcJh9UJzv5ycdqjfRwz8yjwBEotuniGPBZx2AosU6wzqKs2Lp3ksgnHyI7SG4OvSWjKVT1uQTahnGXcY17pbdZXf1YMNJrliBhpxJUOCp7DD4begsB4nnYt0fAZYiYODMT0xmfjLNgqx9beM3odREPPyXfHbfn4GfEUwM_YuTOKKEYS2AY1COgPesCLuYU1E9H1QPijf6agddeXhtgh09bY3JsjPsG4SmtlZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLlu8sYmgcJWH3FAF0fD05s_sIPUzz6uF0hFQED4rSV6PL2EE_yk4kmmeQ_oXl4uOn4y66Y1ckFjFJqs40iXtYn7B51pVbw0WafLijHWzD4AxqvgaF-icvwJ6C20skQ2iIoZK0RJbh3w-9Bav_Y00WPeUq6WDI3lHb_WNDqMiqXk_ccrbmAOUo_LxOVPflwAHtlJxeJlS1Cf77HvHgucJShNHUA6wk4rgXaWkjykwDBsWp2gB898n2J8jl2xNRJZnu28CyIqun0RlkEaJMwy0nUWXXq3HnU13dr3VjcCHt0nF6MPjvPjRzgqmM8M_iO3EKhcbkpZNDVyGCibldMtsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بازدید روبن‌ آموریم از موزه افتخارات میلان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99045" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
🇦🇷
هیجان بالای گزارشگر تلویزیون آرژانتین در صحنه گلزنی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99044" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLX9c0RRSZWOxo8MUpJj6p0Z3gszoGnDvJ8XjQK-FPLzNCZ-kIIb5_wMEy4uh4dc8s-VkHvDgppjMgoR46F39hWBLfV6_L86kDzdsCUFSOvrFGbvXHnLeC_KrjvjmAz7yI6JXyPg7vZLxjxbH0Tmmj7WjqcFpdEYY3TtYS5HXveyJFg3l26j80hEvT3uI1ac-SlAg0yWu7f_N_PleAZWDMXVw21iJYkfrlrQT9LFFg0TFEUurezi2RBgKvtXtaGDdYCn3PfW7_KvhONm_UEY4pyqsLsddpe8Iwg_bO32MWWjuZPRQc0cwnydF5IdA6QhpBd3wK-Pusa3nRv1JKbQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🇪🇬
تصویری جنجالی از داور بازی دیشب مصر و آرژانتین در ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99043" target="_blank">📅 16:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=X96-1H2nVfoZXcpuYMmaiSPLL_NCFMVw44qRCZ8KOZurSarWCqfN8d7ItLOIarmDroitxuMf-364BRKbKd4jrKiDg3dCIPgK3vVVWOR99djFhS97ZUOU2GinJkRC-7adFqcK0FH9KQ6t5B6sVBadRDtZiY8pQu8iXZd7nB-3qC5RLaWgj9-DpXUzjJWRPvoPF_xiZp2A7YSVECBpmDJQsDKhudEKPk1HFTo5K6UrlHuhMyEmuiC4fjj2rGXluqNrKL0nuwbrMzddeolVsHpZdOY_KVrAb-wc-4DLJKY4CrPJdlDTiWsxB1YVO7cJSpb4mrSE5cJj4rOaCXsH-R-bcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=X96-1H2nVfoZXcpuYMmaiSPLL_NCFMVw44qRCZ8KOZurSarWCqfN8d7ItLOIarmDroitxuMf-364BRKbKd4jrKiDg3dCIPgK3vVVWOR99djFhS97ZUOU2GinJkRC-7adFqcK0FH9KQ6t5B6sVBadRDtZiY8pQu8iXZd7nB-3qC5RLaWgj9-DpXUzjJWRPvoPF_xiZp2A7YSVECBpmDJQsDKhudEKPk1HFTo5K6UrlHuhMyEmuiC4fjj2rGXluqNrKL0nuwbrMzddeolVsHpZdOY_KVrAb-wc-4DLJKY4CrPJdlDTiWsxB1YVO7cJSpb4mrSE5cJj4rOaCXsH-R-bcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🇪🇬
تصور اشتباه مصری‌ها از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99042" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسخل‌بودن که شاخ و دم نداره
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99041" target="_blank">📅 15:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
ارزش دانلود 1000000000000
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99040" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp021JLC_ewVeGP_w3ai6feL2j4OoC5tSG2c1gf8MqTHOBwfQ0XP8nQzDcjGIS3UkbgX9k78sHKqCdqhXzeksXKwcIhGLVGz6C4yFRCcL-a8pODy83U_unJ7-0k7DsrzRytWulpicx1jLL96R36T8CfNERbNmEWA54-178hFyOObWA6U66AyI_QqBb1LsQcIj0ihP8MLWInh4dUKdrchn5-u_NC-taCfL-xlVFJLDd1ZyjrLvJTJz2z_TB8neS1r9FzvkAleLL0aqvmX9IfPkh7fbeP6W1XqfyP5NNeEVKmSDSOoTxDFo35uapm0i7ApYZY1vBHReIEsyQDap6uyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین پاس گل تا اینجای‌ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99039" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدرو پورو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99038" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99037" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99037" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99036" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👀
نظر دخترای آمریکایی راجب بازیکنان منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99035" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5LW7wThjKzTwUzDwCknV31_GdbhWpE_y4uZaQaAXv751pzQc5G0G2ShzL_VItiwepsssYunBWZkYx4cwaw1ohZWkawWHmt95G5DgxjUIJQCSLZiJ0IS_8GeuJYGue55PFq5OuwsvwuOIa788PK5TpXFAInO06vC5QvZwJIPF4bz_z6mCVKIMMWU7BPBAWRBaoeKQgwZBmRt26kHKSoeequxjsARwTxNRZqJiwtkftHjA3c_sF7dWmnqMIie4rVB1VzkWRGq9zFzQ4TBGsvMYm6D6Pgwn_dCeowwEl9zNZJL5qbcVF-g1N9WXJYNvCdC61hrndfQqFM0UATWBwoASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
تیم ملی کرواسی از جدایی زلاتکو دالیچ سرمربی این تیم پس از 9 سال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99034" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=MOnwfpWrO1Py29GyVI4yvjE8klnMgTl2J_S9j-JJIp4i6yaTfMm-w6yeqVIjkT-Pv8jLDWb7Uq8clGWK9UE9gqhsp6kbYNd_jkLl0U7GQ9ygCrcjQFDnf9BXZ4Cg8t7ZqwYTqYyBLDI4XrqgGUdszNJzY2bhKw1XDeIA6JmYiUvBZfQAfHoCC94EaFFKLKs-GdF3S5HzisQ3B9GwB7j9xvCVRymK9sRN3er6K5rXGqDMequGRonDfIFgGvylBgNL6e8Wf_Hpi7HXI5MzJeaxCJl11G-g5dnyk6cgxiSsRZQ8oR3isWQ-suMPIBF1CyO7-S-hdJ3h2yJAfznaweNJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=MOnwfpWrO1Py29GyVI4yvjE8klnMgTl2J_S9j-JJIp4i6yaTfMm-w6yeqVIjkT-Pv8jLDWb7Uq8clGWK9UE9gqhsp6kbYNd_jkLl0U7GQ9ygCrcjQFDnf9BXZ4Cg8t7ZqwYTqYyBLDI4XrqgGUdszNJzY2bhKw1XDeIA6JmYiUvBZfQAfHoCC94EaFFKLKs-GdF3S5HzisQ3B9GwB7j9xvCVRymK9sRN3er6K5rXGqDMequGRonDfIFgGvylBgNL6e8Wf_Hpi7HXI5MzJeaxCJl11G-g5dnyk6cgxiSsRZQ8oR3isWQ-suMPIBF1CyO7-S-hdJ3h2yJAfznaweNJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تمجید لائوتارو مارتینز و خولیان آلوارز از مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99033" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdqI739o4PiSNGosCy1o8U6QkOtP5_Cy2pXwsMVXkzLsOkKBnwWYUEq65kDR1xvwScFvFbQl4O0Iy7jX2MfzxTSaYcN11GhOxpPlj5Z_kO8AtPMZ947GAYKLxZrPhCRADsESH-uxoUFek4sDeGhs9u4lWdVaWH5XIOAcbOhN_IO2MxL44VTZJTIRYROTGdgWKkvpHtEAOVYOFCM5zFWxf51gd9_JwEAi9oEc2bEoteAnThGKXf4Ym8aaBWcfGDuTRvpQy2RMBU2ZCUHJKE_Vw2PauWWN0krEafUO2M4PqCiW4D7Sy9XcwYQJU-Ptt12tUvpjQ9A1gnRL7CIL2_cAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وضعیت قلبی برخی از طرفداران فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99032" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99031">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=K4yoEpqwZ24v02HUizEClFbRrmfcdarzpx-yhKN4L8lN-lXlxoQHzkBUt4wMcBcj1Gh_mcY4jMxMd7UVfTBqJqzDYahb2_V6tIONJufF9QDgy4FSZTLRqflwx79_JXtPTdfH-aRcOp48wZY1eBEV1kAJpNKbsKmcA635T9u7JTfzV2gyTiMq_v_-QXop6J-wqIyVUNDcMTW_kqytwLlqhQ3bko4NqM3Q4Mj_PIwqEsdDH73z89u4ZfKtay4Xkest3OdISmsOdzqReAUTgcigX8ibIBp3wz7f7LicXYhDo6OMkJdNeTdrXHRTMZMOLkvFy_aBkA8fCC1hM7BblQygLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=K4yoEpqwZ24v02HUizEClFbRrmfcdarzpx-yhKN4L8lN-lXlxoQHzkBUt4wMcBcj1Gh_mcY4jMxMd7UVfTBqJqzDYahb2_V6tIONJufF9QDgy4FSZTLRqflwx79_JXtPTdfH-aRcOp48wZY1eBEV1kAJpNKbsKmcA635T9u7JTfzV2gyTiMq_v_-QXop6J-wqIyVUNDcMTW_kqytwLlqhQ3bko4NqM3Q4Mj_PIwqEsdDH73z89u4ZfKtay4Xkest3OdISmsOdzqReAUTgcigX8ibIBp3wz7f7LicXYhDo6OMkJdNeTdrXHRTMZMOLkvFy_aBkA8fCC1hM7BblQygLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ ابوالفضل جلالی بعد از مذاکره با مدیران پرسپولیس، بدون صحبت با خبرنگاران، محل جلسه را ترک کرد. گفته می‌شود کار او با پرسپولیس را باید تمام‌شده دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99031" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifH4DOq1XJTy569CYaI5i-LfHvxhmgWOxMrWUhy3h7WSumzHKQ12IfcLUh-Xe9vczIUxhhZ9jcVbBz7GN4PRjLrqcvj9btsIx9YrW4G5qGjtLZhzsUMbpmS3S4MATM6o_rfAA2eNpyQyPMgb1_Rb527JOClf-o2X34JvYpCjZJDlhjJwBwMDCYzUvLjHbOKxHLLf_1yUuDus98sGosDWxYWA9Hth3OgfcwT8y4QNEEf9lZCcL1UjsVqROQoYnf3y-8RBze2muMScg6uP6aInzU5KHLzMu-BVVUuVzKLQsDil7eeKpyYHVnro6iIscV0wAYF8AxEa48anDR3u-S4wBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇦🇷
#فوووووری
؛ بدلیل توهین‌های نژادپرستانه هواداران آرژانتین به اسپید، فیفا قصد داره فدراسیون فوتبال این کشور رو جریمه سنگینی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99030" target="_blank">📅 13:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=SxNbn42o3s1P1-BiP36DGvCICsfSHRD1mbrkxWXWWQKPJdqFHz15S1YeQe2iuwDmo9tsScwivxYraY5Fw60Ao5zXTOZXKAg11_6Zbr2oZ6-BZkodLGFGpLorlbhEJKZZOEeHTJfy4XEv_kemvCrVRrM6xkNqfRejHa52SQMhRVk2gQb9w9raouXmk65fdtY3GS_1UQlY4hXoYDnmx7nqbvmJigleA9MkNj4nwWAsX5LpzpxkiyMMzJAlz1H3P4jBR1FaMJRZLHoEy4-OmwzGmkPc8zFrqjCCmFjw6Hmt3G0BBhck8c81VcPl-pGZqETumwC5RjUg7yiZNByRScrh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=SxNbn42o3s1P1-BiP36DGvCICsfSHRD1mbrkxWXWWQKPJdqFHz15S1YeQe2iuwDmo9tsScwivxYraY5Fw60Ao5zXTOZXKAg11_6Zbr2oZ6-BZkodLGFGpLorlbhEJKZZOEeHTJfy4XEv_kemvCrVRrM6xkNqfRejHa52SQMhRVk2gQb9w9raouXmk65fdtY3GS_1UQlY4hXoYDnmx7nqbvmJigleA9MkNj4nwWAsX5LpzpxkiyMMzJAlz1H3P4jBR1FaMJRZLHoEy4-OmwzGmkPc8zFrqjCCmFjw6Hmt3G0BBhck8c81VcPl-pGZqETumwC5RjUg7yiZNByRScrh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🐐
نیازمندی‌های خونه هر مسی‌فن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99029" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⚪️
#اختصاصی_فوتبال‌180
؛ آرمین‌سهرابیان مدافع استقلال که از حضور در تمرینات آبی‌پوشان منع شده، پیشنهادی از گل‌گهر سیرجان و مهدی‌رحمتی دریافت کرده که در صورت توافق مالی، این بازیکن بار دیگر به سیرجان بازخواهدگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99028" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99027" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bzr0OuGwvOv50IX7Z9pn5VXdPjkpD5OcNqdDk-qNLx4n50CIu5GljgPdSl-RcgJvGsCEZn4pj4ZeuQP7ni-kP7_HtYgqdMUgRJ5EgmgB_pwQ-Aza1tmH8XCu7vckuwQrmQxM847EMTkNwKoBgstC9QREPDld6BrQCUlwGVpAqVqEWRxVoC3YKbN0C4NrdctNduWcZYOMdBodmH596Vni-9usbU5MTCv9v9jBWmTavZ7ZQq6pbxLXT7uJ90VWxd6Bdv3Za3UUv26onNTQRKVmHxMlOYd0dwgBB991qhHAP-o5f_u1ImhJDNzLYdZTdu9Uu6FIZOO2U-vK4l9WHBPF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
جمال شریف، داور بین‌المللی سابق:
- تصمیم داور مبنی بر باطل اعلام کردن گل مصر، تصمیم درستی بود.
✅
- تصمیمات داور مبنی بر عدم اعلام پنالتی برای مصر، تصمیم درستی بود.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99026" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ2lQ6NPOhFbU3BcJUMq5I7a_5B3BJUSeSB7PcviSkR0k60paxCWUiOfb61F25SfJqB0WwlXObylD-lS-vlbaaYfAdxtHzNcMtXqexjzi56aiUepgHWp7c6WuK_hofIeTCQDMzlO7_avFJjiUfpx50VylJFWdHmgrCBPpV35DJ_8ga1xATUfvoWFTqonmp-6cuTxPzcNdk36pqKsYk_6bQAJvIQrKPc7eWp64fzcL6NXFz7w9SuZNPA2z4Ne4kWj3dw6JvGmkhqzLhc9Ii8X3mOLbTT_YVANR0ONEZq4XWiSkBFT77IE_et8ucW17G4737FiG_EPi-_HMcQTb1-HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
تعداد دفعات اخطار (کارت زرد) دریافتی تیم‌های راه یافته به مرحله یک‌چهارم نهایی جام جهانی
:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس: یک کارت زرد برای هر 7 خطا
🇲🇦
مراکش: یک کارت زرد برای هر 9.8 خطا
🇧🇪
بلژیک: یک کارت زرد برای هر 10 خطا
🇨🇭
سوئیس: یک کارت زرد برای هر 11.5 خطا
🇫🇷
فرانسه: یک کارت زرد برای هر 12.2 خطا
🇳🇴
نروژ: یک کارت زرد برای هر 13.6 خطا
🇪🇸
اسپانیا: یک کارت زرد برای هر 17.5 خطا
🇦🇷
آرژانتین: یک کارت زرد برای هر 22 خطا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99025" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=qcCSlorhrvzvgF2HZzyl7BHTVG9J0Rybp3nqfS4pouqxo5sup9cc7iZAet3XX1dbhS9V2JkA7AuW8dojUud5tx5MxJEKbhnMUWp7nGd8Wv3ekymZDoL3q1Y_eslD9TbCQPkwyeYURfbu0lnGjx8vUDqfwvRmkmTCY6JMv56u8mfCBZ9NUyyjh_Dynm0hggvCH_P4M8IMZIyi3ZQdPeL3IxkaOXk37evNe8-lUKhVoWnpL1G_S0OP0zrXC6M6FMh2__vrWol0TpILyTYntKDZf0H17PrOS0uw95klQzOmSKujJE7GpXdLVeSCqJv6bynVX-KmmSmiMvTz_i3DPbq_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=qcCSlorhrvzvgF2HZzyl7BHTVG9J0Rybp3nqfS4pouqxo5sup9cc7iZAet3XX1dbhS9V2JkA7AuW8dojUud5tx5MxJEKbhnMUWp7nGd8Wv3ekymZDoL3q1Y_eslD9TbCQPkwyeYURfbu0lnGjx8vUDqfwvRmkmTCY6JMv56u8mfCBZ9NUyyjh_Dynm0hggvCH_P4M8IMZIyi3ZQdPeL3IxkaOXk37evNe8-lUKhVoWnpL1G_S0OP0zrXC6M6FMh2__vrWol0TpILyTYntKDZf0H17PrOS0uw95klQzOmSKujJE7GpXdLVeSCqJv6bynVX-KmmSmiMvTz_i3DPbq_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره تاریخ فوتبال لیونل‌مسی
💀
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99024" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=JU8z50IGXz8PVYcZOIbgk0004isHYAQ3e0PeK1wy6YXXVm04SE9YVWr-7Eiye7y3U2A6puqwo8EE8GNla0wuu4nHe3YD4vbF4dsUBjnp718-e9DEIB9ivqXCl0iJG8arOi54-9FxRp_ooX5KL_eAEAQ5ebQbRSIUayWeIlqON6a9hHTzqGjfgU-GrYRZ_VQ9IrFCMaRy99zckfWELhCd95kjHQ7JWmgexqnSEt5jGItn--Z1CzJVL2S_urE4xy2gzQUOT3cCy0oS4ZcGGwPVKRe-yDrq8DE7-ZLVKPILiuWPUXL19fRrPtEKGrxm9hsLZGS4-qFrbz8EQUcqZh-Qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=JU8z50IGXz8PVYcZOIbgk0004isHYAQ3e0PeK1wy6YXXVm04SE9YVWr-7Eiye7y3U2A6puqwo8EE8GNla0wuu4nHe3YD4vbF4dsUBjnp718-e9DEIB9ivqXCl0iJG8arOi54-9FxRp_ooX5KL_eAEAQ5ebQbRSIUayWeIlqON6a9hHTzqGjfgU-GrYRZ_VQ9IrFCMaRy99zckfWELhCd95kjHQ7JWmgexqnSEt5jGItn--Z1CzJVL2S_urE4xy2gzQUOT3cCy0oS4ZcGGwPVKRe-yDrq8DE7-ZLVKPILiuWPUXL19fRrPtEKGrxm9hsLZGS4-qFrbz8EQUcqZh-Qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
تو یکی از لیگ‌های سطح پایین ترکیه جوری داور رو کتک زدن که بنده‌خدا نای بلند شدن نداشت
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99023" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇧🇷
فدراسیون فوتبال برزیل حمایت قاطع خود را از کارلو آنچلوتی اعلام کرده و این سرمربی کهنه‌کار به فعالیتش ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99022" target="_blank">📅 12:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=J8pNtpGkSRtwLHvHf8p0pVjXrAiAji12C0TLaGj9oPnenzi7CqDsPFudejjYYR2IzUknNUOeCEEQHh6CutIVpPXecgwmLC0KYiCRbpNu9rfJxWWunz04Wd7XmRm8BCodzEeIRiAOHGz24oXSP-eLemzSCP1sr3PwNIUcieohg0g90ggQyq439hCM3ycG17MA0TWn3XoyRPC5jaaR720bZkQNknxN4ugUXEJCQ-bcJteru72QTDE15Va0SoLLAb9aNan9ROPQU0KNV5mLBai81adJCibGFwx1lZCyaNQ4lS3IFiJLL-EpaNidVrIJ-9adB4rMfsNqCFHrJcMUodJj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=J8pNtpGkSRtwLHvHf8p0pVjXrAiAji12C0TLaGj9oPnenzi7CqDsPFudejjYYR2IzUknNUOeCEEQHh6CutIVpPXecgwmLC0KYiCRbpNu9rfJxWWunz04Wd7XmRm8BCodzEeIRiAOHGz24oXSP-eLemzSCP1sr3PwNIUcieohg0g90ggQyq439hCM3ycG17MA0TWn3XoyRPC5jaaR720bZkQNknxN4ugUXEJCQ-bcJteru72QTDE15Va0SoLLAb9aNan9ROPQU0KNV5mLBai81adJCibGFwx1lZCyaNQ4lS3IFiJLL-EpaNidVrIJ-9adB4rMfsNqCFHrJcMUodJj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
لیونل‌مسی با این طرفداراش محکوم به بردنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99021" target="_blank">📅 12:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99020" target="_blank">📅 12:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENIITlLlJKaCoFOkCQGDtRy41pVhMBTtrurPTFIDKq57yk2jaT-NhikpNR8EXAtPVwGuFkkBnlDKPXPzBa9AEA3Avi7OVLsq98VBbUGWxRee1J8tj2dlDdlahGIzatLyxP3bOtw6m-qDJD5yuDy1vgvOI7MGm9zvwXz9x3sbDQUqXtiCcrWyTsquhwYoLNPd4cTvCUbbkDyvje8UXcYPwUPiaH5IIZZ9c0iTWy8ZxSY1wAXuDXd_WdugZTJMe6dbAPqvvraQdIl-UBeFFquUU20afRc1BNuAl0dO8PLc0NdnP1O2sKn-KlbrJwuIaagN4vkhvAVTm3G4b0GD-EKIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز:
منچستریونایتد به اورلین شوامنی پیشنهاد قرارداد پنج ساله داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99019" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOnKuG2utZDmdFxMlIDkfnRkRH-GlBEDsQQjbF6QowDB3x-7IWBReSt9KDzO2sG1p7ey1e3ahnDTN52YI5GJqnnKluIxdvM2Qw_Vn1OhDginPGiOk6flfZgQ4Wq6VnLQ1RQSb6ldnaqgQUHNXOM0JKyXK5lia-J2_v2hB5XP9nZ69qQLbfXs2YdjqBid2a2kvqZehO9KmRBvY7eeoiTdbWCV-2YwK-HTfcHsBIghj1xnYo5S5Rh5UAWtR9n6V_zjQzQ7lmCFyXA_NEtXQseGWl0Tz0cu4SATHtJ_93mSTaW7DiJ6ugPAZF8f3sAUdSxEYgoengNTNKe9WzdMsBbq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند
🔺
مصر شجاعانه بازی کرد و باید به آنها آفرین گفت اما این سناریو مانند فیلمی است که از قبل نوشته شده و برنده داستان هم قابل حدس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99018" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99017">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYEtGnJ_5lg17obi0YEJt7FinufdCql4awRP-uHoSLh1Xd1fRbwi-VDhEAoG_YRx515ZvxvAt_zM2R6maSTtkCogT7y3NTp7WL4mDMR3_Sd7_9kz11TCXaTBEM5de7T3Ezvurc2oj9M2kS959IQ5urBJ7pNcxVHebVsppuha5usRr1SXf5azxWH9TeSKg5rvRCbUxitfPm_FwHba5NpscIxLWxx2r3AXCMt7cYqFVlZpCogpCSFdjA1mcVQR10ayuIICy3uXvj49gRDZdnz4xpS99JtXF4-7qQo-7aL4y29i5R_u7oJKFkZT8CXHu-P7Bhs6EPk6Qsu_RXF8I9zcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99017" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: تصمیم برای ادامه مذاکرات را به کوشنر و ویتکاف واگذار میکنم اما از نظر من دیگر تفاهم‌نامه قابلیت اجرا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99016" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99015">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99015" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99014">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99014" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99013">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد.
🔴
آن افراد بیمار در ایران، چیزی بیمار در ذهنشان وجود دارد. آن‌ها بد هستند، من آن‌ها را دوست ندارم، هیچ‌کس آن‌ها را دوست ندارد، آن‌ها شکست‌خورده‌اند، وگرنه تا همین حالا یک توافق به دست آورده بودند. ما رهبری اول آن‌ها را از سر راه برداشتیم، و حتی رهبری دومشان را هم. آن‌ها افرادی بد و بیمار هستند، باید از ریشه نابود شوند، مثل سرطان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/99013" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99012">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J57A29XGKfpUATq3ZCXCPKi1QFQ0HkgeBNm0c9WjKG9ZOTc-dcxlWh554dFafe1JvtIWXIgVvXeXatZIDtLRW5RZUsyLijhZ_eN6L0YtWQhYBq7CT-8oK4vN2NbVWH6sLsQTwVDmSPgf1EVt1-4964ErSGuYZzeIdJHbkfTqw8DemhxLFwDvi2KIzwv3dkNpW3heD0gmwBQoDIovlzdZ8-8S41j6doWxFzOvy7Hq8lg4x9qX4WspGyvSRvFh3uo2mfNSLqyx5yMkJNi6mX8U_0bLYjGweeWa8NEdiE1JTYC3ZBVqftb9wQhTLAqRZzb30FLGYeylfUHlvZI4Jk3Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیک: رئال‌مادرید تصمیم گرفته که در کنار داشتن کوکوریا، آلوارو کارراس را نیز حفظ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99012" target="_blank">📅 11:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv5umIhJ1oy_hjT_3oTmSMWs7yDXQyaytFNiV_1GSkanFVdRgUwa1Un3N7sU1htsz7THXh33oEFL8qc9d1o7YM8fcwRzwL-ADUApVgTB5nTpltOnmx446V1uKO2HOvZ1rki2gRQXO27lOzy7s9aOViwgyjE0sdGGlCuAvUfKQ8xnVYi6DVpUhbNDlylXwC43v6CDMgh6LguiNdnF6ozeAXBUJaw7sRuMMQbaKsX9dkwgxnrHgiWo52i2bjzJ6i79fVbtJaJQ6_nRspBCjE6EQaU-RTtMOqAbRvlES_ppbPxzGrkNr0-be26sXq_AJGTFTb9ppt-VhA1lAtuBNjzPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99011" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37082570ef.mp4?token=qTqFPGe9JyWZwiI589usU597OYJKbSmBW0VZju2SV4Ce9ZJI2cOFt-UQdLJnR9eZfrMFr6mN1N5eDWzsIfDl6EIUKM690I3HTG9WD71P1fXO6Iufl1x5vsNNWau7y6C8PwFkNV4TICl1wb1pnfdq6A6Nf6zmTgDikUEob0PTYHvALywUI1nX4WEPBhO2zWCnVP5auk0rhJozk7khjYWIBX9YqpDUqA45IaaRqpP3KK9t2LhMq7DIngkAHTyBIcTrZ109C8_f1hn3mtPpPXn95_w6gA5eXD7FiI4JbRlUo0OY1it5w0hwwUAjq4Sld_QqE8seQWjey_v0kqaZrha7LRPZUN0_KPmA6DVUHO1xBvtWXkQLoutVlLKmBYV9--z5ZMxpF7f9VlopcLEEP8c_FAeMglTkDKsF1aY5PGcWUC4xerI_NEJjt1GZKCG3mW0eH6nwUF_d-06ccAqC5JBtNnN0D8sfBxnAAJULGUAKu0841vQP0Rq4fqo-y5cJc7hF7yw3SDYTLwjm5o_z4SxJOFSN_FchH1GtKw8tFO3bAvx1F4JfOhQ3-_MrHRKNnF4FhcprXM4aSiMtTIIZFFbD0mS3DbniXt3uWR0oIH3vN4nlsfjIeWrXRPBmtvtcnQVieM57-PB_HcdsuMDlxl65_dAmvDgSnNCpelQ4kqBHD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37082570ef.mp4?token=qTqFPGe9JyWZwiI589usU597OYJKbSmBW0VZju2SV4Ce9ZJI2cOFt-UQdLJnR9eZfrMFr6mN1N5eDWzsIfDl6EIUKM690I3HTG9WD71P1fXO6Iufl1x5vsNNWau7y6C8PwFkNV4TICl1wb1pnfdq6A6Nf6zmTgDikUEob0PTYHvALywUI1nX4WEPBhO2zWCnVP5auk0rhJozk7khjYWIBX9YqpDUqA45IaaRqpP3KK9t2LhMq7DIngkAHTyBIcTrZ109C8_f1hn3mtPpPXn95_w6gA5eXD7FiI4JbRlUo0OY1it5w0hwwUAjq4Sld_QqE8seQWjey_v0kqaZrha7LRPZUN0_KPmA6DVUHO1xBvtWXkQLoutVlLKmBYV9--z5ZMxpF7f9VlopcLEEP8c_FAeMglTkDKsF1aY5PGcWUC4xerI_NEJjt1GZKCG3mW0eH6nwUF_d-06ccAqC5JBtNnN0D8sfBxnAAJULGUAKu0841vQP0Rq4fqo-y5cJc7hF7yw3SDYTLwjm5o_z4SxJOFSN_FchH1GtKw8tFO3bAvx1F4JfOhQ3-_MrHRKNnF4FhcprXM4aSiMtTIIZFFbD0mS3DbniXt3uWR0oIH3vN4nlsfjIeWrXRPBmtvtcnQVieM57-PB_HcdsuMDlxl65_dAmvDgSnNCpelQ4kqBHD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این 45 ثانیه رو ببینید بعد بگید هوش‌مصنوعی خوب نیست و بی‌روحه. خاطرات زنده شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99010" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=fiIuXlJVJ3PPdW1PghiL-j2nWMzzIm4sz2EC0dzTPMf9K8RK4llhJ8gJjm8XvkgKt3Izlvd2P4Pmmf4JrAW3R9xG4Fh8eEvcTt4ri1MAky6D5k9sNIDFbJvPd7Erjdbpgibg2pmNEaETqTZSWf3lToMOA3Y2q7Z2twyvVlR663JHnRUo8GHMx_0VvxpEBEgCmlBcllOnl8TSU4Q1BPc4W-zQrpzk2dZP0pZ_zYLFVxF5xHjQlU6SCZqeVrvuirkOQ7cVtQdJ1l5OiT2dsgrx1LTOFwzZHV8CEJCUbDO5W0piT1PnmZGvWb0G4os_VD0mIX2-CNAIMF1wsHmML-ooMLmh0Qtbiy-0Y7qwP_QTsIW_g3PLiO5g2TtThFH3N8Nt2PPHc0wSIc1auiWPObjWOzVOkJY9Wmwr8WN_WTlAm9q48HxBgUTf6Z9T3m7d6vlMbCaxB_IgdJ_pop3oGalAH-Pjs1WTZDS98GPS9wWoGNdjND6GO4YesHrbbSCNHn3JOsTXTjS-vLsH-_26BkPPvMKU6SJZRKbr6SbfpvbrmpC0vVlo0lfI4kEL6brOcqlzj8s2B2XGWMCOPWsuJNLyaXE0ERGsM6CjHe_z2HEVr5o4wIPcbs0a7KMGsMCg5D8GDpdau7lu8n58pwP5jisaCNsi_sFrHwNKRjBOEFJ9q6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=fiIuXlJVJ3PPdW1PghiL-j2nWMzzIm4sz2EC0dzTPMf9K8RK4llhJ8gJjm8XvkgKt3Izlvd2P4Pmmf4JrAW3R9xG4Fh8eEvcTt4ri1MAky6D5k9sNIDFbJvPd7Erjdbpgibg2pmNEaETqTZSWf3lToMOA3Y2q7Z2twyvVlR663JHnRUo8GHMx_0VvxpEBEgCmlBcllOnl8TSU4Q1BPc4W-zQrpzk2dZP0pZ_zYLFVxF5xHjQlU6SCZqeVrvuirkOQ7cVtQdJ1l5OiT2dsgrx1LTOFwzZHV8CEJCUbDO5W0piT1PnmZGvWb0G4os_VD0mIX2-CNAIMF1wsHmML-ooMLmh0Qtbiy-0Y7qwP_QTsIW_g3PLiO5g2TtThFH3N8Nt2PPHc0wSIc1auiWPObjWOzVOkJY9Wmwr8WN_WTlAm9q48HxBgUTf6Z9T3m7d6vlMbCaxB_IgdJ_pop3oGalAH-Pjs1WTZDS98GPS9wWoGNdjND6GO4YesHrbbSCNHn3JOsTXTjS-vLsH-_26BkPPvMKU6SJZRKbr6SbfpvbrmpC0vVlo0lfI4kEL6brOcqlzj8s2B2XGWMCOPWsuJNLyaXE0ERGsM6CjHe_z2HEVr5o4wIPcbs0a7KMGsMCg5D8GDpdau7lu8n58pwP5jisaCNsi_sFrHwNKRjBOEFJ9q6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇮
کشور شاد و بی‌غم فنلاند یه مسابقه راه انداخته به اسم حمل همسر که میتونید ببینید
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99009" target="_blank">📅 11:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=Ng0U8t1APg2QiQEqJvNeKjnehI9zkrfwQfw_PMS8w7zFVb5FfC52GsZ257Wr-TaIuTQuniMnTcheXmbW4_VrEV7iEsOXL3DA2RwnZ9JnNapvbh46N9h-NB7tHYNW8pp4tZvkcDJuHkOAEw0nuV-e3YCQPcNnU5nu34JgQSvhk5rIVET0XUiLPTYi2fFbZZY9Fj45GVdmyrET9pOB8WR4EOlpjCYekGG2M7cVXaqBsQH8hQRTRIFpQQAv1aCAi__3n2izjbM8iImzkYTOFpDeuaIeYPL0qAHuQWm5KvHX-O0g7wIHKUyGVl_lTyJPHxaX_V_9dZ6nybGzKKDIMx4Ufg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=Ng0U8t1APg2QiQEqJvNeKjnehI9zkrfwQfw_PMS8w7zFVb5FfC52GsZ257Wr-TaIuTQuniMnTcheXmbW4_VrEV7iEsOXL3DA2RwnZ9JnNapvbh46N9h-NB7tHYNW8pp4tZvkcDJuHkOAEw0nuV-e3YCQPcNnU5nu34JgQSvhk5rIVET0XUiLPTYi2fFbZZY9Fj45GVdmyrET9pOB8WR4EOlpjCYekGG2M7cVXaqBsQH8hQRTRIFpQQAv1aCAi__3n2izjbM8iImzkYTOFpDeuaIeYPL0qAHuQWm5KvHX-O0g7wIHKUyGVl_lTyJPHxaX_V_9dZ6nybGzKKDIMx4Ufg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
تیزر تقابل جذاب انگلیس و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99008" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYPZa6H7UeYXF0fopgDOwPU-7XT-SYQzAaE0J_qw34-1qHwoxKeyQS-Cr5mtxtKXl9sd-SrmR-H1Y3BdSSZOC4RLn7J0XLGUAqE429ancOVItC_F2TJ5OkvzVNG-Ljr-AUSCVewQKEYKr8v48PWJq7x8tnowgFqj9gyHwyPeGaDfcSmej1oEA2SpKh3pa9Ld0_RawVk29fxAaEnEW-qUw9rQ8QBWEzf4r7OX71uSezjCkCch07YcOkxMxTPa-nPxANuV2boSKk8WagmWQNxWhqoEYH7xeJd00ACClrZsB6PEef-Zum4foJ9mELZLdIOJZdL4BzbGmE2St_umfBioZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
♨️
مونیرالحدادی ستاره استقلال در آستانه عقد قرارداد با اتحاد طنجه مراکش قرار دارد. این بازیکن که با آبی‌پوشان یکسال دیگر قرارداد دارد، به استناد به شرایط جنگی ایران و بارداری همسرش قصدی برای بازگشت ندارد و احتمالا با توجه به تعلل مدیران استقلال بزودی قراردادش با تیم مراکشی را رسمی میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99007" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99006" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=sE8j_LRfgR6-VjqBN_RWLEVdd9ZyP01U33XFRNAAqUvy3SCFiWyfNrkvnUloWlzmkE1Er6zjWrrSxkxGJ4g_-7r8alhO0EQCT26TWzY4J-XBYlqRo3LDyI4NINLaKGO4nBlYJUq9PJOQJz16I_h8hcHzK0rHZA24ohdtvcFQDoWUW83kOjRXDXV92h31QvnaitxmN-RvdK9k-A06XhwLJkjuAe4fLeuc8Kx93MF426Awd-cMdCf7nNvmV9cYKl_ZJ2WkmMTyo6MYrE0vAj38IWvCVQukgYAzfJsLzt_yG8_sARAWyOJrLGJmxnnMyy7D-38DuBxRZytZiMV6RipkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=sE8j_LRfgR6-VjqBN_RWLEVdd9ZyP01U33XFRNAAqUvy3SCFiWyfNrkvnUloWlzmkE1Er6zjWrrSxkxGJ4g_-7r8alhO0EQCT26TWzY4J-XBYlqRo3LDyI4NINLaKGO4nBlYJUq9PJOQJz16I_h8hcHzK0rHZA24ohdtvcFQDoWUW83kOjRXDXV92h31QvnaitxmN-RvdK9k-A06XhwLJkjuAe4fLeuc8Kx93MF426Awd-cMdCf7nNvmV9cYKl_ZJ2WkmMTyo6MYrE0vAj38IWvCVQukgYAzfJsLzt_yG8_sARAWyOJrLGJmxnnMyy7D-38DuBxRZytZiMV6RipkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تیزری جذاب از نبرد مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99005" target="_blank">📅 10:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVncmD2tX5Vv0bbAVDocW-mmSjS8NUbQbOpw8bds9UJE21JmvqRRxHtDAjRKWkrMahgssqBvjmXhh2P9ua-iKq3dr9UPtfW1I48doax0sWIQwupGxTROlnBi6eiXaOFSaX2NAlEm0RLPLrjoMzgYfgyH5G7cJk_08HBHT2rfBSclrNeB2SimRWCPR0H8ozhi90ey4K395rZQRHKJm-wfpGNeBjFmsQmgrnPMysmjNu64DGU4ix8hjkEk8FoQEUSAdHkU70WuJK2gL77RgGE-yyJlLLJ3FduxV91DekM4sNI-KYoWH1JOlozhGTMKTd8dYmEuD2lOituZsTkCDbkc-gzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVncmD2tX5Vv0bbAVDocW-mmSjS8NUbQbOpw8bds9UJE21JmvqRRxHtDAjRKWkrMahgssqBvjmXhh2P9ua-iKq3dr9UPtfW1I48doax0sWIQwupGxTROlnBi6eiXaOFSaX2NAlEm0RLPLrjoMzgYfgyH5G7cJk_08HBHT2rfBSclrNeB2SimRWCPR0H8ozhi90ey4K395rZQRHKJm-wfpGNeBjFmsQmgrnPMysmjNu64DGU4ix8hjkEk8FoQEUSAdHkU70WuJK2gL77RgGE-yyJlLLJ3FduxV91DekM4sNI-KYoWH1JOlozhGTMKTd8dYmEuD2lOituZsTkCDbkc-gzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
لیونل‌مسی ورژن جام‌جهانی ۲۰۱۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99004" target="_blank">📅 10:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
❌
با اعلام کمیته جهانی المپیک، تمام تحریم‌های مرتبط با کشور روسیه لغو شد و این کشور میتواند در مسابقات مختلف نماینده داشته باشد. بزودی فیفا هم معافیت‌های مختلفی برای روس‌ها اعمال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99003" target="_blank">📅 10:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99002" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=XceBLz3cWlrB8Fp4UCziM3DFzsyFOotZReHJq4aOpfQBjMMCaaIWGxeYRGECv3yt8K-DUMRu_wgjEvuTfVTTXO5lUub3RvfamH27A30fsWxZ8mvEjt8xEhZa55zayrBPdLg4E638MCl97BjHlYES1quRPmIHk0HPW_2qEEG8CLxHMV6reB9OFB97XfsfY4_QxkM250NA77m2SUk40JOLOLxYKSFklYt4PCtNDXsK_MKzEu0Wgkqzi3tV-g1zjy3cNJX0Xqox3sI5D2d0dQ2cP5D35-EIedBXmpMd2k4KbIsVxY0_y8iVis4g2EU0VFEJPY2H-A7TBfojQfaU0euXsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=XceBLz3cWlrB8Fp4UCziM3DFzsyFOotZReHJq4aOpfQBjMMCaaIWGxeYRGECv3yt8K-DUMRu_wgjEvuTfVTTXO5lUub3RvfamH27A30fsWxZ8mvEjt8xEhZa55zayrBPdLg4E638MCl97BjHlYES1quRPmIHk0HPW_2qEEG8CLxHMV6reB9OFB97XfsfY4_QxkM250NA77m2SUk40JOLOLxYKSFklYt4PCtNDXsK_MKzEu0Wgkqzi3tV-g1zjy3cNJX0Xqox3sI5D2d0dQ2cP5D35-EIedBXmpMd2k4KbIsVxY0_y8iVis4g2EU0VFEJPY2H-A7TBfojQfaU0euXsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
دیشب هواداران آرژانتین برای فشاری کردن سرمربی مصر با پرچم اسرائیل تو ورزشگاه بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99001" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSUtDpB9lo4NUF_7TQJ4zBiPzhUH4Umb81xXMpfDsWS79f68FgE7ckM-BhQl4tEBQH6HeTmnttUcXlb6y9fqFCIlT0EUNh9crCGAA_0mar4wk0-wRilej2TVeA9Up5JalBhrfJ6Y9OD_VmhkTeQAOT5YVzjudql2d_UqFFn7mglWLHxR2tJVWqWDEuF4qnZ7yiPrzlqSJfGPeb5lLwCYazzpEhiW3hWJgDxoXn7CV6yZ-fOWfEDb5YyweRsuI3nYr-gZQyFbVfobHc5sPqkwRxG_KBIB7dM4zX4eoPiaVLcoqWzxiivdaisGtQNrENdoM3A-F141-y0vUNXw2QWn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🏆
🇪🇸
مایکل‌اولیور انگلیسی داور بازی حساس بلژیک و اسپانیا در ¼نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99000" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=Lou66xPMU7cj71o6bqMrTMWzu2JZjeNdu6PRJmpxbBN-UUH9JikYo0CKw-aPnWewAYh1BpC05gp7AP5UCuWsI3xw1kQniClezdFJVuYndEkpU57JdPivsnXrOqCYUCZmHJKV3Rsu456QJ7cWIz5VWVA6D4VaBo8RL79tcWBnq7ARIfo85SD8ShJJc0zv4STGLueK0qW6z2yaEuOQaim4UaUW0mVkrMDXkWmpnK9o5FwyppdCihY5vlWu2Pr_xXXAqScRRKgxS16C_sNs36ls7tkkOJmriiimJrZaCZMlET2sK0U4eExj2B6emQGXXylxdkJRbo2REFv4XRV9ViZ6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=Lou66xPMU7cj71o6bqMrTMWzu2JZjeNdu6PRJmpxbBN-UUH9JikYo0CKw-aPnWewAYh1BpC05gp7AP5UCuWsI3xw1kQniClezdFJVuYndEkpU57JdPivsnXrOqCYUCZmHJKV3Rsu456QJ7cWIz5VWVA6D4VaBo8RL79tcWBnq7ARIfo85SD8ShJJc0zv4STGLueK0qW6z2yaEuOQaim4UaUW0mVkrMDXkWmpnK9o5FwyppdCihY5vlWu2Pr_xXXAqScRRKgxS16C_sNs36ls7tkkOJmriiimJrZaCZMlET2sK0U4eExj2B6emQGXXylxdkJRbo2REFv4XRV9ViZ6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتین به یک چهارم نهایی رسید.
🔥
🇦🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98999" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKUgfDUtngvO8xrKOcLYHKDT5e_-5NV860SeRDmL0CSIM3LiTNxJx3tSyDRWA253xlS1GVa6a9KDoNnRZIX7630JGPxJ8PczVEiBzNtBgpmnclVRqcCfYc9ldbsNRGV5s1me2lXwbSZT87lYlBsCfs7qIfQumy25NAyAa4sDDMA3Mc6SK-AXJOFHTgD-WW8-8BZEDZ819uuZHicfxTOC36Ea7DyBX90_qT7HQwpogtzN5EVjvgEd122cPZWPXO38J-gF-pSL1zacjKWyURN3ZiESV_BuIBBPi5fIP-O2jLmhUawjNK3qW-QqwU_TSPPdnZIiz4mb_8Oh8ComdxtnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO-GlPESKAk2oG3sX-xzVRNI4YY1NbWDDCynVrj4mARlJ9C8dU1rak922Tj4U7Kcrfse6S1LvsZzkbWjsU_ynMhtKID1UPOhmne0DwrFmxPHBkZUctTUO4Yyl58NuYTkiw55vsbjkG6X1Xia4N5OpMy8NlSm16WrCDNQAuEwU7S0PNTlLT9qNC2YtdBNmJLhkV2ImQjCmG9qy00Fjpyl0bDFRGn0qo9XQ2amuBN3HmyCpV7dsUfEaSJLg2ZTSKq5s1QQriS94Uu0XDn1FDqDmFb9Bsed50kK2j0FviMyF7atWGUJZkpANokJGTzzu_MxK6piv-t2cJT_lLL_2qsLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=ODwjU5WbwLTqZsrweZ83togwONNn9nzEtCxrpySjL6qODuueqHk9ub__HjsCJa8kogbZBha4nVqNZMMLSphUZ9QjuR2BOCzAt3n7Vch5NExdZx_93R0hul2fs2V0PWbPAB7_27CkaBh0rUekZgWv9pAN2phVDM0Nwt9rQY4Uhu5P9a4RZpANkTvG-1SjGaVdTG35glm24ArjS5B_mvPoy_gR_TuxAexcBUPcebZcXWgYPkrc-0l1054W9zHFXxDIPgwbDJNcJo-x0NoUuw9NxSR7-X9w1ktr3xmmWbWmBT30Z9uKAxE2cv9-6IXIgVJnFmyPLauZhmW4Rri4-AL8rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=ODwjU5WbwLTqZsrweZ83togwONNn9nzEtCxrpySjL6qODuueqHk9ub__HjsCJa8kogbZBha4nVqNZMMLSphUZ9QjuR2BOCzAt3n7Vch5NExdZx_93R0hul2fs2V0PWbPAB7_27CkaBh0rUekZgWv9pAN2phVDM0Nwt9rQY4Uhu5P9a4RZpANkTvG-1SjGaVdTG35glm24ArjS5B_mvPoy_gR_TuxAexcBUPcebZcXWgYPkrc-0l1054W9zHFXxDIPgwbDJNcJo-x0NoUuw9NxSR7-X9w1ktr3xmmWbWmBT30Z9uKAxE2cv9-6IXIgVJnFmyPLauZhmW4Rri4-AL8rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای خیلی از پسرها، فوتبال فقط یک بازی ساده با توپ نیست بلکه پناهگاهی است برای فرار از شلوغی‌های زندگی، جایی برای نفس کشیدن و رها شدن از فشارهای روزمره و فرار از دغدغه‌هایی که شاید هیچ‌وقت درباره‌شان حرف نزنند. وقتی بازی شروع می‌شود، برای دقایقی تمام نگرانی‌ها، استرس‌ها و خستگی‌ها رنگ می‌بازند و فقط یک چیز اهمیت دارد، عشق به فوتبال و تیم مورد علاقه.
🔺
فوتبال به آن‌ها یاد می‌دهد بعد از هر شکست دوباره بلند شوند، امیدشان را از دست ندهند و تا آخرین لحظه بجنگند. و در این میان لیونل مسی برای میلیون ها نفر از مردم دنیا شاید بزرگترین تراپیست دنیا باشد. برای خیلی‌ها، تماشای بازی مسی فقط تماشای ساده فوتبال نیست‌ ، تجربه‌ی آرامشی است که در کمتر چیزی می‌توان آن را پیدا کرد.
لذت ببرید از سالهای آخر بازی مسی
🩵
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98996" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=Olnwt9a6wmh4CLmZUpsSQHyOxyB7Vn3hK4eSIqEF-bdZgLiXm3AqF5cdHBlodr9LG2TYwHbjw0MWGiVQmrfcnZgHQY5b0h2MtmvENe-N5filepIPuLHf9D2XAc-xVBed92iJRJrr6OwESxQRL-ow5t6aBCn505RDtx2r1KXXZdbX9nS5SwLY3UdnK0FUVEL9TpI6mJQ6VKp6PHX3Kx2B0Fm6i5chBM2y-hvnX2bnbJTdwG8W0o2dJlhtkESfI6SuofcgBQBKBLdbFTHlKzs6ZziuwZRxTebeGMv8AVNtl6phREZnHCr-NJTrwxJ_i_xz5I8kWagLSBhU4J_f9FFL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=Olnwt9a6wmh4CLmZUpsSQHyOxyB7Vn3hK4eSIqEF-bdZgLiXm3AqF5cdHBlodr9LG2TYwHbjw0MWGiVQmrfcnZgHQY5b0h2MtmvENe-N5filepIPuLHf9D2XAc-xVBed92iJRJrr6OwESxQRL-ow5t6aBCn505RDtx2r1KXXZdbX9nS5SwLY3UdnK0FUVEL9TpI6mJQ6VKp6PHX3Kx2B0Fm6i5chBM2y-hvnX2bnbJTdwG8W0o2dJlhtkESfI6SuofcgBQBKBLdbFTHlKzs6ZziuwZRxTebeGMv8AVNtl6phREZnHCr-NJTrwxJ_i_xz5I8kWagLSBhU4J_f9FFL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
12 سال پیش در چنین روزی تو جام‌جهانی ٢٠١۴ یکی از تحقیرآمیزترین نتیجه‌های تاریخ جام‌جهانی فوتبال رقم خورد؛ آلمان ٧-١ برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98995" target="_blank">📅 05:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR6y7UJB5bjwdVAuCZNEC2BIYgQsndkC6mkfnO1gbp6kcwCwnX7rOuRLk-1YdFu2ZlhqkVb_jMa8F7RMYZjVUKvTyD0yFbO4_Z1vPr8Yw4PwP5jLWoJjofq6q0VV1Z_Q-J5uNcILOtFZwx5X7junckZpXxadssMqnFUU64yPVx13ndXOiAQo4UYogNqbUUhGdFZJ7BwKzKBg4erEQbmifhowd9_ouH83fTU4LXtcRHhCTNrR6dEVo5hhgmCFbW5dXBRBoqDR_Ws4iM4oBF7M_j-FuK-sNulceu3vepSYxoI3vPZ8Tdr8ihF5khmMqFZyfga3RZN5OPI9otkUHvDN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
💥
لیونل مسی:
«من گریه کردم، چون احساس کردم که هم‌تیمی‌هایم را به خاطر پنالتی که خراب کردم ناامید کردم. اما خدا برای من یک اتفاق ویژه دیگر در پایان این بازی در نظر داشت. من خیلی خیلی خوشحالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98994" target="_blank">📅 04:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHoVBoVzDDZngY7eeCcv-TuuInjdJfq1gUdVPy2vNxACDInYPe48ZHxZcewDW7bbJoYmEu8VIrpXG--12mDeVbmo9BamikTO8PPJnVXTne1GsGlM0chBAh5poFu-AG7VzYE3bjfJhJGxRRad-0dDxp7r9NPCwIOaYxyHBXeZjw5ls8LkjLs9jxuz4hkm7mZRtG98uaw0Ur3qX5t4nu5QnsSJ-NDidh8HvPflMvBVDb3EhnuTlQqXDRqQRw3iUPCtDei6cDKXpJHtilK8Ux-ds2IYemSDxzyme9Fqg6EaIqy1H2hmhB-EGdMTvhPDNJ4YbLPu59e3GLEQwV4OypynXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC4S29JAPm5tbH9eQ4nhs01MNq4rMiw96GpM-5maQ0-CmkswXFiSnpFEoYwvu47CUhNMNSYWS843NghNaS6iE34qeQ_3FtjDvA7FR8c76eQsaAlbmYOYhFHEtmKjhkRk0GLDYO2V_CywoB13j1CXffwGlf022GAs7RYf-m44khv5tUZk3obv7TJW7N-5bBcP5Ebp2F-USeOX3gE8cIpyag_5w_Wvtbdaxp4S27eoIMiyH54HFxkbE6RSUKDiOpbgh6-H3YbzOQB6oGqu332tfIz9JLuCsYf4MdhIUnMPjSclRKxku2LeOPpaALe0W63SlFIbpkp_HNc7Djj_ILRPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmB6BLgFFkAt7zUADViSNnEhkjaPgxtJY_s4K317iRsSTTzmpNHTzmXGf78QyDKVH04UBtmzGi_pTOhizDrjRU4-VpoH4efqwMk5pyR7xU3xMDfxzI6DQGW4hbw3AnrXFD3i4R5eSSqZNu3KcL1VV76iGt1ZSRKYZ9eVwomv_JunIDI2EC2Q32m4AfeI5CJydiVrmwWsg6AkiBCWhpFPFBfPYyMHnVlohxKuvgdHCqKmJi54Ef4okgLTSGsT5Xj3Dr9_nvAkrrBGcQjSIn6s74fxcY3HSThR-gI8i5mDNStQ_dKG_0dyNU2VwrXKIF_O8AAiTH0f0JublkQIJiSjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7GLH-TYARG9VkvmrG80I2tduW9VVAFUlxUEbRBRHvuovhnujAf6KNuWH2p4JgZAhdhwLcLg3QE6qZlPa-wps1ktmyXSbLJ_Og7R_Ai16WabEX24YIz0RdvJcUOaft1nw2Wky57UHv-LCpmrZZmd5WwvYBvSC4-tVA41mEiCtSYlj9Ys-xDsXuSzL4nB2Z8P92v3ziBUlaU0ZVMNGrVB4OC-GYBMckyZvaPx5NDTsD2Lk80fBHVdskkmA4jcuoxjUSNPyWQHwm-oFDnHcANqdlI8pMQvjqVPXQYzD_uB6c8o6e_VJPMHnLRdSkvCkAa5kKxDbiO7NbbjpdMfvDQwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98981">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کلمبیا نزنه حذفههههه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98981" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98980">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/Futball180TV/98980" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98979">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگگلگلگ سوم سوئیس بالاخره شددد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98979" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/Futball180TV/98978" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98977">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنالتی چهارم کلمبیا و گلگلگل سوووم نشددددد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98977" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/98976" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگلگلل سوم سوئیس نشدددد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98975" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/98974" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگگلل دوم کلمبیاااا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98973" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/Futball180TV/98972" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگگلگل دوم سوئیس</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98971" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/98970" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگگلگل دوم کلمبیا نشددددد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98969" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/Futball180TV/98968" target="_blank">📅 02:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگگلگل اول سوئیس</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98967" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/98966" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
گلگلل اول کلمبیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98965" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/Futball180TV/98964" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
پایان بازی سوئیس و کلمبیا
بازی راهی ضربات پنالتی شد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98963" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeYcu_kCmAjljpZyvdi7tVPIzlvZpcw3BkpvEMSOiejRK7DiKppYSOBlvI2MdugIayXEW_tzBJOnvbe-qgCeiyk942V4gWk_5gK6vGT6BtO81cFb_wFoA4tWf3_ur4v-vi6JntP1py8vdJGeaDVpn05SsylrmaM-ypPoJCA9YlGx9s3coeGEilOYxiGZw2tENs7wiNhON33zfecAH3usH2C2tq2VCTiCCIcN0wvDQKTtilsVHNche1rjAb7Zfymfv_V7FvzJ8iNZbMbSC_f_r5OV7NyLw42TBxq9vRkLW-npq5-PBz647rvAzv_uyANrZH2ARhuaVEkJOGyzeXLgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلمبیا چه توپی نزددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98962" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارش‌های محلی از موج جدید حملات آمریکا به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98961" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ گزارش‌های تایید نشده از آمادگی همه‌جانبه نیروهای سپاه پاسداران برای حمله به کشورهای عربی و پایگاه‌های آمریکایی تا دقایقی‌دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98960" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وقت اضافه اول هم مساوی تموم شد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98959" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=ij-E_iYXNcVW4bvT-DrBS_VFdPSrN985_yrCJ3RR4Cvyf7VXxabJk61DSG8Hk0yjRT_VAJ5HD0xCBa6303kQ9tbx6YLb-TwUTCqLrx1hYBxX3uyLxQkDBxZ-UySvQ7vwUGchPjD4vM5E2Yxc9sIVeXS9JutFYN5cONbv1-ZntTLyELSTryA0FF0X9BbNGTNj1k5DaBPzGHVydxUmCvE6_8V03jzTc_-SELTWjDwXHTR-89GKIBjxQIWo5_Rqe4smJMpfhWyKgEmEhQXkYPzeTvdQywwrcYIf2RN2QTl5LnxeT55uxOGim0HXA8druuxMohntHtPWFdIZa5aLbLGXvSbq9zggC8wqfICvrpcsYZ7FPSInPMnQ1mHBUwx_uSSk7h3XwRowzGtq1cM1AL0raojfThhiJmqRjZxsPizBjvsUZNy65CMveulD_wFiFa4BVmpS8EkhayMBBQE5grNpR98LKiSqfRhzqc-KbuAzv29nsk2wefPnrenJ1xVdRgDzofO6SYn9IjVzV1sRSARasufy31utkrTWbxaSIfkZ1vB4WtH5KdoJrJ0ml_DyYKioQDk9hEPmFFi1juR1XXH0P2AUKLGbxdaMdkxWzYJpqO68GYPAB4CUfm6X5-Jeh9JEDK6IMwbgqvr-2ceebULhqIsLpcchw5qhCLWllcL0rjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=ij-E_iYXNcVW4bvT-DrBS_VFdPSrN985_yrCJ3RR4Cvyf7VXxabJk61DSG8Hk0yjRT_VAJ5HD0xCBa6303kQ9tbx6YLb-TwUTCqLrx1hYBxX3uyLxQkDBxZ-UySvQ7vwUGchPjD4vM5E2Yxc9sIVeXS9JutFYN5cONbv1-ZntTLyELSTryA0FF0X9BbNGTNj1k5DaBPzGHVydxUmCvE6_8V03jzTc_-SELTWjDwXHTR-89GKIBjxQIWo5_Rqe4smJMpfhWyKgEmEhQXkYPzeTvdQywwrcYIf2RN2QTl5LnxeT55uxOGim0HXA8druuxMohntHtPWFdIZa5aLbLGXvSbq9zggC8wqfICvrpcsYZ7FPSInPMnQ1mHBUwx_uSSk7h3XwRowzGtq1cM1AL0raojfThhiJmqRjZxsPizBjvsUZNy65CMveulD_wFiFa4BVmpS8EkhayMBBQE5grNpR98LKiSqfRhzqc-KbuAzv29nsk2wefPnrenJ1xVdRgDzofO6SYn9IjVzV1sRSARasufy31utkrTWbxaSIfkZ1vB4WtH5KdoJrJ0ml_DyYKioQDk9hEPmFFi1juR1XXH0P2AUKLGbxdaMdkxWzYJpqO68GYPAB4CUfm6X5-Jeh9JEDK6IMwbgqvr-2ceebULhqIsLpcchw5qhCLWllcL0rjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو دیگر از حملات دقایقی‌پیش آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98958" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=UpOAWUu9dspJhCrboUsqFMeK4ynQdV1XH2NvJt6YraSqfUtq2fMC6NWxMJZ_NUzYA-hd9Voij3tFpB2-5g01J4ObtTnkRboD3Guu_anzTmZonB4RRj_r9zXzgGKTJcj43J1ZnqMpWgTV-PPmTiX2BerOdHMo6iXYjLql4q6tOno45J6WPkVSMDQs-wR6PjAWShpzkSteenhe8_OooPCoCGVJMcEt1RqgdTBVwDmFH7LiCjhE6aD5x37bR_VCtSyHUf5aht_tD6-pXn_5_NBesEOzCjEeL8i-Jii2gxx9sJ0FRM7y5E4B7x8oQBsmgStpmbnatfGCQgQy_AMH4f8ixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=UpOAWUu9dspJhCrboUsqFMeK4ynQdV1XH2NvJt6YraSqfUtq2fMC6NWxMJZ_NUzYA-hd9Voij3tFpB2-5g01J4ObtTnkRboD3Guu_anzTmZonB4RRj_r9zXzgGKTJcj43J1ZnqMpWgTV-PPmTiX2BerOdHMo6iXYjLql4q6tOno45J6WPkVSMDQs-wR6PjAWShpzkSteenhe8_OooPCoCGVJMcEt1RqgdTBVwDmFH7LiCjhE6aD5x37bR_VCtSyHUf5aht_tD6-pXn_5_NBesEOzCjEeL8i-Jii2gxx9sJ0FRM7y5E4B7x8oQBsmgStpmbnatfGCQgQy_AMH4f8ixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو‌های منتسب به حملات آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98957" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98956" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iraF6VUSAW-TLdFDGcYXfwlGXfytbT-v6HIKKQx5o7x23gm00sbkkCvTCMAlMdiedd-ZmQBvfFKOiQ1X9VaFOb0FGnnmYuXTARmReHbGuV8cGMc-ZjV2PdoZbGEVfIvIf4m55QNwwHeaGF1NYbhulQoP4IYdD1kGF7GwJQle34Dd1JPVdaxIaQ18cuoHDNEdC1PPApZ7i8TnKm_xrxXL4mDofjeKsq6v44e8BCBCu5Extt0OWn8dzvZbTLYc0hyJLXQmO21Mmlrthy4ZKapLZA44aNim0_NPFJyI1GUspt-10kvsX8f9PkK_mgr_yh6JuF1ZCPJcckT8D-XkI3GYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98955" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98954" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98953">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پایان بازی کلمبیا و سوئیس در ۹۰ دقیقه
باید شاهد ۳۰ دقیقه کیری دیگه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98953" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98952">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینقدر بازی اونور کیریه که اخبار جنگ واجب تره پوشش بدم براتون
😐
😐
😐</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98952" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
