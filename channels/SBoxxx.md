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
<img src="https://cdn4.telesco.pe/file/qrNAujUaIoDg7SrlJQKdRsx7szXI8H091Y54cQpRkbU4oUOK4yxs_FX7jt2zw2Wd6TahTHIHmuxkI_3Spo5KHE6HDN2Hy0se1RJJXd-CHJ95mpYZ4ASt2lk3Zc8MYn7IiDDTFqpjzbU7OSjT_Y-HtGW80MjKZDJU5YyUh9sm5ehp8T7gh19rnBTOgQ5tpHuHVLrdyRYsRTKJeGTmqMjn6nSBUHyCJNsNT1V4Rdqwa_rQEkS7f68wGIKt1dJQzY-e3FvY5-GOVc4L6XwFHyaLuN-loaExgT9hFXAD2nhgIREdXK6WTzZEiC56cjx86edEYqiSPAXRPtsgY-5hqrpzhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">همان گفتاردرمانی همیشگی ترامپ است. به نظر من هیچ گفتگوی جدی در حال حاضر جریان ندارد و همانطور که خود ترامپ می گوید، فقط زمان حملات آنها شاید به تعویق بیفتد.</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SBoxxx/21569" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:  ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم و تا پیش از برگزاری انتخابات میان‌دوره‌ای، به هیچ وجه به ایران حمله نخواهیم کرد؛!</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/SBoxxx/21568" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF4OOH-6uYE-czYqfyMu53B1lF7YhaZZIxi--P7zTomRoC5vmqzdEWs58UM-eXg8vFVpv-XfRkq70px7B7bapF2ixwiX2UoCRBJ_mNHExcnm3YlX6CxHTpCktG5gbDUxumbrtQM-WsGaKTPZg45EmB24e50QS6JWFUUJTII8Jc6u1hIQji77oPkVX7AlN2SoXni5ftwIRs80YC-IGOYrsNb72rHDRgAssXUlruJZg_zUaUfvJwSqcDlQCHKRr0cxc8cX27EXX9Mh0KBCZ5yjSXabwdifLpe5UC41Rv7zrA2LfZ6-6lHVgmEr-cfz6FCAy6ouM4TWxio-wEDzQtd6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش کانال 14 اسرائیل، مقامات ارشد سپاه پاسداران انقلاب اسلامی خواستار حمله به اهداف مهم در منطقه طی 3 هفته آینده شده‌اند. آن‌ها معتقدند که ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SBoxxx/21567" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خیلی شبیه هم بود این 2 خبر که ولی خب</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/21566" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/21565" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/21564" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/21563" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpedwgxxpYgEZ9TqjsvsOAyn0FWI5zfVnaT5_KRLxCMMhh72WAhpniI_E9MswJeo9sY3DzeUZMmiupkqMex0f9WvxieDpooP216awGNVwJpJTe_tBHQb2YRItnrOcSLCtCKL0kOc7549KM6jFqlX-6n7jfM66tsGpCk8eOHuveZCmhRIz7mbkfUUb97MaxlOpTO9ZYd1jEBPOcjxXswAqb6-CPQYeEgxgpct4pjMAXGwtdXRTu6SVyGzDKVrkcqFVMB_KWL7mc1_9RBJs_ULEwAOIsHfQ5mMlRBRkVIoJDPAcYDewQMSI8BWiNs_ITcoJUvnY6TcYMaOPsoaQD_GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/21562" target="_blank">📅 19:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKwpp_JoBDJewB2H4JQV9_30dyNMkPzDLgLi9mFcBjxXVBWo1uSTkXDMJDVrv-hdg8gShEuhfzhU6XXdJzGotHe_LOvyH2MLfbSuHQ2E7zbkmgqTBspocXS0uKb6KYnD7usVNOsc6QFtIdh8W28Qz6AnA-Dfcm4A5Vh6MeyaT41HrZbDUQ95-Nw_hKA34Dg1YueGNHf2cXweOmxXvukPYRozsXBMHtcqdkUP3LktOV3k4AOOQX6e3btFMksDUCHuYY6AC4iGyu8wHjAicLOpUFEtTwi4AZLAOWYAqyn20dNeXfANb5Bz9CvsZm-TJVFSfqb5VnAdUK25NYfnkk-r2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/21561" target="_blank">📅 19:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/21560" target="_blank">📅 19:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJddqNnZhSYpt6jJk9pGdcnjBR8sRz7UCsaN0gs3LSFuNeBeigfWumH6W6d0B6I9nPnr_MSKicLdrOhh4vrCG6VTdjQBheieVu2Wll1RJ6pNloL2QsuoNkEc_TpeckIW9MHVw6u6LLe8eV7XSjmdR6N3FLbQCXICbxFrCzV75dVrhnHZkHugG33Gy9lAXk_YYV3_FzHHoqQvebpOjikllmhRLfAYmfCOL_tfuu0NUfdPeCa7s2nNdnFVgvXeGOR5QDCMZzhoJvqiQ57UlGWQGIhQNm8vrEDbGYTqA8XzNVbG_OKoKIKx5ACWY90OALUz85-V2ABARagO-FiEQJKvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/21559" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/21558" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBwarYpEseRdA1tgFndNOj-mPwEz-3JRfF0Tzun2uGmyDSxfGGlUsaJGZArKdHSz-1hagEQTa_lRaTyBbVEKVUQOp4nRX9W9FHpvHdCcQen8l4Y_VHU7_ROrSNJqpbngzcumLr1eDH3yM-HeEpZWqVTDv2KTY2tAUOqQDLrzItU0K3W6n3AdObFzWdvZNp_SXwFyCo_njbLKrPnxj9IBD09YdKvkvAjJRmPEabX8Ld1Sd5-ma__Z8JgHQMcZbiprbSyADqI0QBdl0OUIL4O10_H6Gb-R0LWyD0kGzia77LdfjhFZXiNld5Vxez5wLICzBgwWC8sx2bgmcsMhaCvDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/21557" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/21556" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/21555" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1xxPmfOrO0kxSz_vXu_mfAcrD0RbVSHyrTDs_7wlRZurNB-vN75fcr3DXEZjVdtYRLCxulb1bXXAKhD91vyYULFgZR7_z3S2ui-Xk8k1zoyW35dUA7Ayhr_sLJNqMZEltZa_b0GYQ1UMs_arhPPeiqaByrVDExaGUKMIjJCWYZt5lGdA7Suf4BrQyjmpLOMY-CIP7ExUMjFvPxMR0a_IuQv9D3Gqripg9XblTadokAhdA2Qr59Xo71JYIbLMKHmsT7TDbnnS1U0ADR29X7cc4ZmKNdyuyA3esT0jFLa20TM1CTH885s6VgqIqfMQKRm-GS2VifJA-I91ZpdjU0XzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک هرمز؛ آیا جهان در آستانه یک بحران اقتصادی جدید قرار دارد؟!
شوک هرمز با افزایش قیمت نفت می‌تواند تورم جهانی را دوباره تشدید کرده و بانک‌های مرکزی را به حفظ یا افزایش نرخ بهره وادار کند.
تداوم نفت بالای ۱۰۰ دلار می‌تواند هم‌زمان با رشد ضعیف‌تر، سرمایه‌گذاری کمتر و هزینه استقراض بالاتر، ریسک رکود تورمی را افزایش دهد.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/21554" target="_blank">📅 15:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر    در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/21553" target="_blank">📅 13:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صحبت های یک استاد دانشگاه امام صادق درباره اینکه چرا فقط تنگه هرمز برای جمهوری اسلامی به عنوان ابزار فشار باقی مانده است</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/21552" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21551" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر
در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21550" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxBfKxV0YNqRoJIIABqwksn5ULQjbFmBmTO5RLLkuq_lD25bmU2Lb7MdsDUo2hUeiiuPW0nqsUuUqUE9gZeH3FKdhI8XobJoLv5OzZ3QwXci0eTEADooMqvTxmagGu6e4qtgKyf3US4UEKl4104f6xCrni03idkk5oJfDK-aYlf1YnvbXAZa2X5cUiheQmmEqCygxk4CigFKcVtRvXTEbzcur7SGSNWez9jZHW-it5MvGgPkJDUpSMwIJbtY5oofB1LdL-n1eAxIE3blZEYjljYQBvzPK9xQkshTsuYAGxIBWxpGccv9Z8OrT63QmHok-3-PKnw0tCSUbES4ItwzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/21549" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiV4jjelLh3cTSZeRGy22K6gbv_iTjdvJltTyND232J9-2AmC8mITbsX9ndMVjboiMHdxMFIuXMF8fPuu3-SVk216Eq0fanPU1OrsPXj9Mptl4ooJlUA7geVY9oy7dACUeJeKR0SFRe8aZgu8bkbnqFv2BW2mMw_GhlRoVRW43Zlv0ynhYD3souZEp88Se1_h59JV2m7DMyKkxqT5eKY3s528tNT70jWDAy8WvcO-WMERw5lymj4CR-VFZPQvVThPC79rhCarjENLsX3y6CRfOMaI8fpToSKcfylTXy-vOMBSN4ajemEHHVCAgFZ_oEZzeN8XxaUlLCs5S8OiePRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده بیش—فروش قرار دارد و خرید در حمایت ها منطقی ترین گزینه است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21548" target="_blank">📅 10:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSpEwHbWUvyUPJYARHiR8j1ujVt2E_oegPCS39xGyqYVhC1koM1usyh3PzoTN_UowqkRsrqoXOz51n_7wnnNuF9ccE8GUGZP1Ogr2N8J1xBYH9jOVV1MaG66lsoNP1FxmEl6yqhQAVSuE-RcxdB0oXpza5POLBttpDtvovuyb4KPNj9CbO6goqcDiFDvbqFqTMzW-NHVejoJ1Oy4U5RrkTiOZUhLgz7tEKZ-q9PuVTd0SeDpQ1TVbwZjQATLjaCOX8_BB6dUql3wH8wTpGUt0xigbabH3UDPN56s0D5fy-YxJkQMM7UqUuNmp1j_XGxEj4aJdMHH7sDOyoocuOEWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در حمایت ها توصیه می شود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/21547" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.
ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر رخ دهد.
یک تهاجم جدید می‌تواند شامل حملات گسترده ایالات متحده و اسرائیل به زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران باشد که احتمالاً منجر به تلافی موشکی ایران و افزایش قیمت نفت خواهد شد.
مذاکرات هسته‌ای ایالات متحده و ایران همچنان متوقف است، در حالی که ترامپ و نتانیاهو، نخست‌وزیر اسرائیل، در روزهای اخیر دو بار تلفنی با یکدیگر گفتگو کرده‌اند.
مقامات اسرائیلی معتقدند احتمال حملات پس از انتخابات میان‌دوره‌ای بیشتر است، اگرچه حمله زودهنگام همچنان ممکن است.
— آکسیوس</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21546" target="_blank">📅 09:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران،  بقایی:
عمان با ایران بر روی مختصات جغرافیایی مسیرهای امن عبور از تنگه هرمز و نحوه ارائه این توافق به صورت بین‌المللی به توافق رسیدند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21545" target="_blank">📅 00:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایران، حفر و توسعه را در یکی از بزرگترین پروژه‌های غیرفعال خود، مجتمع زیرزمینی آبیک که توسط سازمان‌های اطلاعاتی غربی و اسرائیلی با نام رمز "سایت 311" شناخته می‌شود، از سر گرفته است.
این سایت در امتداد محور تهران-قزوین، در حدود 100 کیلومتری تهران واقع شده است. این مجموعه در دل کوه‌ها حفر شده و شامل چندین ورودی تونل است که احتمالاً به یک شبکه گسترده زیرزمینی شامل ده‌ها سالن و پناهگاه متصل می‌شود؛ این مجموعه یکی از بزرگترین پروژه‌های از این نوع در ایران است.
تصاویر ماهواره‌ای نشان می‌دهند که این یک پروژه بزرگ است، با حجم زیادی از خاک و سنگ‌های حفر شده، زیرساخت‌های پشتیبانی و پوشش سنگی قابل توجهی که از تأسیسات داخل کوه محافظت می‌کند.
بیشتر کارهای حفاری در این سایت بین سال‌های 2007 و 2016 انجام شد. پس از آن، به دلایل نامعلومی، کارها عملاً متوقف شد.
با این حال، بلافاصله پس از عملیات "خشم حماسی"، تصاویر ماهواره‌ای نشان دادند که تغییری آشکار رخ داده است: ایران به این پروژه بازگشته و با سرعتی که در طول حدود یک دهه در این سایت مشاهده نشده بود، حفاری را از سر گرفته است.
این سایت در سال 2010 توجه بین‌المللی را به خود جلب کرد، زمانی که از آن به عنوان یک مرکز مخفی غنی‌سازی اورانیوم نام برده شد. این ادعا هرگز به طور مستقل تأیید نشد و هنوز هیچ مدرک قطعی و عمومی وجود ندارد که نشان دهد غنی‌سازی اورانیوم در این سایت انجام شده است. هدف دقیق آن هنوز نامشخص است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21543" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21542" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قرمساق کاکولد با بهترین تجهیزات آمده نیروی دریایی فرسوده ما را غرق کرده حالا کری می خواند!
پدرسگ اگر شما هم کشتی های ما را نمی زدید خودشان داشتند یکی یکی غرق می شدند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21541" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیت هگست، وزیر جنگ:  ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.  نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21540" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21539" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">موسسه UKMTO:
گزارش یک حادثه در ۵۱ مایل دریایی شمال مدینه الشمال، قطر دریافت شده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21538" target="_blank">📅 23:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، ایتامار بن‌گویر:
ما خیلی نرم هستیم. این جدل من با نتانیاهو است.
اگر کسی در حالی که پسر من در ارتش خدمت می‌کند، به زندگی او تهدید کند، خانه‌ای که آن شخص از آن بیرون می‌آید را از بین ببرید.
و اگر دختری دارید که سرباز است، می‌خواهم او را محافظت کنم تا حتی یک تار موی سرش آسیب نبیند — بگذارید ۱۰۰۰ تروریست بمیرند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21537" target="_blank">📅 22:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار با دلیل نامعلوم در حیفا اسراییل</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21536" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— حزب‌الله ماه گذشته ۲۰۰ میلیون دلار از ایران دریافت کرد تا به مردم لبنان که به دلیل جنگ امسال با اسرائیل آواره شده‌اند، کمک کند، با وجود افزایش فشارهای اقتصادی ایالات متحده بر ایران و دشواری‌های فزاینده در انتقال وجوه به این گروه.
واسطه‌هایی که پول را جابه‌جا کردند، کارمزد ۲۰ درصدی دریافت کردند که چهار برابر نرخ معمول است و این امر بازتاب‌دهنده خطرات مرتبط با مدیریت وجوه برای حزب‌الله است.
— رويترز</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21535" target="_blank">📅 19:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظرم وقتش رسیده که یک بار دیگر بکشیمش.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21534" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام ارشد ایرانی: ایران هرگز حق غنی‌سازی خود را رها نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21533" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
‏حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21532" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو درباره ایران:
کشورها، حتی آن‌هایی که به ما حمله می‌کنند، به‌صورت پنهانی و پنهانی می‌گویند: «(حکومت ایران) باید سقوط کند. آن‌ها همه ما را خفه کرده‌اند.»
ما اطمینان حاصل خواهیم کرد که آنها سقوط کنند. آن‌ها سقوط خواهند کرد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21531" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21530" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgjHPDjS2P1f_a-oOC-5xJOTp7vs6hrZk-Q7w6d3x3wdVibmUQz5ExcRipv3yTr4GvfhykHwiG9zJnR4j9i-LZcZNV8TZFhL6Oz4S8vOinEAFw1osN9nQT3RVrb0-08GpwOx1qnD_fQV_yqP_Bo2BrRXU_l1vck5PjRI6blYta7BrzQ3RBN02RkbScdRR8knckzM-0eii0uU8WBewXn8aXzzZAknLe7gROXauqgj2OZfp41Mgm78STwFqJE_YsM0EifMhkn63clmdNRJwYrJGwXQZAnAPs-o4EDzH5KJtrl6wQ0hEufWA_Fxe86KQvi73WM9OfOz2B_AxJl4EyYW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21529" target="_blank">📅 12:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td36Us9MD0Y1TKedTfN2sLFB9pwTjcmufaIgs5w4Q2mfAmWKQ5WFpfXEorU3SQk-uh7hHe6KH_LY9GjvP1r0fgLHabrnpmUF2IxyrPeoDbgFV_XGYaPYUV_FTqXmFaXx48rI-y1u5wqQcjSNWLk6OEG5xCuU_d4o6fmM0AequVr3qNuj5weR_2iM3tPOSpcdkwFXLYIbHJ35qSQjELMHOCuKXbGxPS6FrSDwUr-Zzkw5nWNEikCeNhy_Gux3Ibz9h_Eou5MF2SGSxSotZmpPhlmric91zhnvJID7bnsMWjZByqHfAyyOXcQ5gvDhm4Q1FCKqetdaPI2oTvkscBd11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21528" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOcP2oshI92RoPwNVryUpOge_ufHFitxinD5r31yOkXThrYSX40aYSmHbAAi4yvW4nGBgVF9NrRtfrxOwH994Y1vb_8T1TJr5UnJ6nLU4Bk0Mw7X-NpUul13knj67MdEhwCSO7eaH5vPiP2eWq3_Bjk6PJi2r1QVM_l0SJEW9JRRu2OWwWigevZMF-ynMok97lPTKLOsu9SkNoWUYtZ48vsN96McbNISEooUrc3PjzybOF_TicEAOcAEwAEbdxeY4jy78FKkivxhLTPWut7EvsUl2R0W8jCPcTJ-6LzZOKXpV6ebLLi9h0qCDQhaLns_YGLI0-uFbbslzHpNLh2jvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC به محدوده بیش—فروش نزدیک تر شده و این موضوع خرید را قوی تر می کند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21527" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvQtKXhcF9JAUzKiDH7h1VJ0gr6NJrrJ-ls5UyvSgEPkWEYNS_pkPw3e3uOg_5tfmjRRNvYAaIlDlR3a1F1ujHJ2k2e9DCf1Wl0HGJU41WNK_nI77CLGjA5WjuOLRju76XFq1xhUbDZzA30tp-kZ_cwz9KVkAwNnuLsLHFC-7sKE3iJcBWkOia90hgg6j9YdTg-9wq-cBDTyQz9X17qagxoQ8u_ksSnANRs7U5NIrKFjJW6Cuw8pQ1OrPWvTj4yamDnMRk9lW24oJp_Lo5YHIcKTBL2EI6Zw78v5N2x1L1ZBQ3ytBehcPxN6R9eoE5n36D-3_GMNmwJ2TaqU5jJydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش طلا تا این لحظه، خرید توصیه می شود.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21526" target="_blank">📅 12:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVg_wK5AbjtmL1Epi4gcXq4pPYcuxQlkmGMhQEhhqSPYKP0_3wYpRyL_F4h39lvNZrpbSaoOVi-W_gq_6lPw6kf1zOheiSD61hpWzOZFM5lFj-IzXx9E9ul65AN_3-i1JhWoid-cTFh9ECfdXOfq3i1kubOCjCY3mcKA2LkVsXbxtUifWdDdHRmHv7kIyMdoXlNPuB7m8S0NN6LADIZDAdfFLNRv_JrFSkUzhudfGhLfVhCwJuWqQVK9DAKlWsI3LqfvBOANM3MZ-9fUA5shzFWVwdtP59mHOV-McC53CZOgU0e1_017zFXmBDnq2h9ggiuesJBvJ0T9T9qQkCwjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21525" target="_blank">📅 11:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ذخایر طلای چین در پایان سپتامبر ۷۷.۴۷ میلیون اونس خالص بود، در حالی که در پایان اوت ۷۶.۷۳ میلیون اونس بود
اما ارزش این ذخایر طلای چین در پایان سپتامبر ۳۲۳.۵۲ میلیارد دلار در مقابل ۳۵۰.۰۸ میلیارد دلار در پایان اوت بود</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21524" target="_blank">📅 09:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تعز به تصرف حوثی ها درآمد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21523" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
اسکات بسنت :
ایران وزیر نفت جدیدی انتخاب کرده،
با توجه به اینکه آنها از 25 آگوست حتی یک بشکه نفت هم برای صادرات بارگیری نکرده اند، این وزیر جدید عملاً چه چیزی را مدیریت می کند؟!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21522" target="_blank">📅 08:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6f6Sdc88ZO8FA-GH0Hdaw8PALhY6qzRWvdh980S8LAjBLmpe0tmC3gakx9ftm2n50l7yhsvHLmtN65Wr4QVCByDEYZfayQtX3L8_jprg7Uu9TUOOrqzXehF_ye2p2Ck_aqI0_5y_Ll47KhPYq_zWhoiM0GO8Mo_Ik2joSwgPWF7ZGj8KAkcDup58UG3tcuNgAWOLVkmvv3BXyX7unFmBA56wpNwZlTu8M5zrtSwnKT5URQpzwzDVvZDh1ZABO2M2hYCst24N0xB_bi7tb5MyRzehhJ2jv9dqR6XA-_0Zak_raUMQA-J0OOPeER1_q5_6cyivw-jnL6yAE6x-AFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خب بعد از اینکه به بسنت این را فهماندیم، دلار 40 هزار تومان کشید بالا که مهم نیست چون مهم این است که ما مجبور نشویم بکشیم پایین.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21521" target="_blank">📅 08:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21520" target="_blank">📅 07:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این مدلی بوده که اردوغان تروریست های جهادی ترکمن سوریه را که تحت فرماندهی «تیپ سلطان سلیمان شاه» قرار داشته اند به جبهه های جنگ قراباغ اعزام کرده است.  پس از ورود نیروهای سوری به جمهوری آذربایجان، در جلساتی با حضور رهبر تروریست های سوری و نیروهای نظامی ترکیه…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21519" target="_blank">📅 07:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آماده‌سازی‌ها برای جنگ میان اسرائیل و ترک‌ها با شدت تمام در جریان است Damir Nazarov  پس از به‌رسمیت‌شناختن سومالی‌لند از سوی اسرائیل، تحلیلگران این اقدام را تلاش نتانیاهو برای ایجاد پایگاهی در برابر انصارالله یمن و کسب اهرم فشار در دریای سرخ ارزیابی کردند.…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21518" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خیلی حرف های بد دیگری هم زده که اینجا نمی گذارم.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21517" target="_blank">📅 00:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دونالد ترامپ:  تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21516" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دونالد ترامپ:
تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21515" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کاخ کرملین: رئیس‌جمهور ایران روز جمعه در اجلاس سران کشورهای سابق شوروی که به میزبانی روسیه در ترکمنستان برگزار می‌شود، شرکت خواهد کرد و با پوتین دیدار خواهد داشت.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21513" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/21512" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
آنچه در فرانسه در حال وقوع است، چیزی جز مهاجرت گسترده و بی‌رویه نیست. این موضوع نه مربوط به مدارس است، بلکه مربوط به اسلام است که قصد دارد بر کشوری که قبلاً عالی بود مسلط شود! (رئیس‌جمهور دونالد ترامپ)</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21511" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیلم وزارت اطلاعات از ضربات به گروه های تکفیری در سیستان و بلوچستان!
قشنگ خاطرات بازی Counter Strike زنده می شود.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21510" target="_blank">📅 18:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبیرکل حزب‌الله:   آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21509" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دبیرکل حزب‌الله:
آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21508" target="_blank">📅 18:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21507" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SBoxxx/21506" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های عبری‌زبان در تاریخ ۵ اکتبر، اسرائیل در حال تدارک برای اقدام نظامی احتمالی جدید علیه ایران است؛ اقدامی که ممکن است به‌صورت مشترک با ایالات متحده یا به‌طور مستقل انجام شود.
روزنامه «اسرائیل هیوم» گزارش داد که ارتش اسرائیل ضمن حفظ همکاری‌های نزدیک اطلاعاتی و عملیاتی با ارتش آمریکا، خود را برای حمله احتمالی به جمهوری اسلامی آماده می‌کند. این تدارکات شامل سناریوهایی است که در آن‌ها اسرائیل یا دست به حمله پیش‌دستانه می‌زند و یا به حمله ایران پاسخ می‌دهد.
این گزارش احتمال وقوع حمله اسرائیل یا آمریکا پیش از انتخابات میان‌دوره‌ای ماه نوامبر را نسبتاً پایین ارزیابی کرده و حاکی از آن است که این آمادگی‌های نظامی برای رویارویی احتمالی در زمانی دیگر صورت می‌گیرد.
هم‌زمان، وب‌سایت «والا» گزارش داد که واشنگتن در حال آماده‌سازی برای اعزام نیروها و هواپیماهای بیشتر به اسرائیل در هفته‌های پیش رو است؛ این در حالی است که هم‌اکنون حدود ۳۰۰۰ نیروی نظامی آمریکایی در این کشور مستقر هستند.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21505" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فوری - قطر اعلام کرد که ایالات متحده و ایران همچنان در حال مذاکرات برای پایان دادن به جنگ هستند</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21504" target="_blank">📅 15:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترکیه و پاکستان برای حمایت از عربستان سعودی در برابر یمن، توافق‌نامه مکه را فعال کردند
آنکارا و اسلام‌آباد متعهد شدند که به‌سرعت نیروهایی را به داخل خاک این پادشاهی اعزام کنند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21503" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21502" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خلبان آن هواپیمای فلای دوبی هم که داشت سقوط می‌کرد هندی بود!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21501" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت امور خارجه هند:
۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21500" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21499" target="_blank">📅 14:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نشست کارشناسی بسیار جالب و دیدنی درباره روند جنگ ایران—عراق و فرصت هایی که برای پایان جنگ وجود داشته است:
https://www.aparat.com/v/goil745?playlist=27887251</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21498" target="_blank">📅 14:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انصارالله ادعا می‌کند که در دو روز گذشته حمله دوم به فرودگاه سعودی را انجام داده است
انصارالله اعلام کرد که با یک موشک بالستیک به فرودگاه بین‌المللی ابها در استان عسیر عربستان سعودی حمله کرده و ادعا می‌کند که این ضربه باعث اختلال در ترافیک هوایی فرودگاه شده است.
یحیی سریع، سخنگوی نظامی انصارالله، گفت که ضربه موشکی «دقیق و مستقیم» بود و به شرکت‌های هواپیمایی بین‌المللی هشدار داد که از ادامه پروازها از طریق فضای هوایی سعودی خودداری کنند، زیرا به گفته او این فضا به «صحنه عملیات نظامی ما» تبدیل شده است. ریاض تاکنون به‌طور فوری این حمله را تأیید نکرده است.
این حمله پس از حملاتی رخ داده که انصارالله در شب دوشنبه به فرودگاه‌های جازان و نجران نسبت داده بود و پس از آن حملات، مصدومیت‌ها و خساراتی گزارش شده بود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21497" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرانسه برای اولین بار موشک بالستیک جدید خود با قابلیت حمل سلاح هسته‌ای را از یک زیردریایی هسته‌ای آزمایش کرد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21496" target="_blank">📅 13:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2UXFKtKUMkHPkJj4o9jb4nJB0ejAL2H_6Ptgz-JeC-4rkkFbDYefouhDJ-8kmWAieD85RQFWmQxDTDWI_kT4sukYOLWE8LDDCipqoiBf6SRvZj7o4HFHKCZ6_lPnbioNpVVzH5B5oq90x9HGsfwFbQaqGAoZuL3_2KDKLuQhfA3R-elDUpb_xGeS2OMiNvsXEqPAFgqtvJLS8EH-VbphkPcK9Wxna_HTFhpP2jFu3wKU8AmWjIMtvyH2-FslhMObaK7WkYLz9jhLCpIyM7vdOfJE4R9OYOHvOspd6pzZYShntWiPuhG_leoO0M-n1O-tNvbrqLY8yJB2DUZhWsJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر وقت یک نفر که ذهنش اسیر تفکر فرقه ای نشده  فهمید که میان توران بزرگ با اسرائیل بزرگ کدام بیشتر به زیان ماست و آن را بدون هراس بر زبان آورد آن وقت می توان امیدوار بود که پویه های ژئوپولیتیک بر محاسبات کلان سیاست خارجی کشور حاکم بشود و نه انگاره های وهمی…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21495" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">موسسه مطالعات جنگ درباره کوشش ایران برای بهبود و ارتقای توان موشکی خود:
ایران به احتمال زیاد در حال بازسازی و ارتقای توان خود برای هدف‌گیری اهداف نظامی دوربرد آمریکا در منطقه و کشتیرانی تجاری از طریق بهبود دقت، برد، سرعت و قابلیت‌های هدف‌گیری موشکی است. سخنگوی ارتش ایران، سرتیپ محمد اکرمی‌نیا، در مصاحبه‌ای با رسانه‌های ایرانی در ۴ اکتبر اظهار داشت که ایران در حال بهبود دقت، برد و سرعت همه موشک‌های خود است. اکرمی‌نیا افزود که ارتش باید برد موشک‌ها را افزایش دهد تا نیروهای آمریکایی در منطقه را هدف قرار دهد و اذعان کرد که نیروهای آمریکایی تا ۱,۰۰۰ کیلومتر دورتر از ایران جابه‌جا شده‌اند.
مقام‌های آمریکایی در ژوئیه ارزیابی کرده بودند که ایران نسخه‌های پیشرفته موشک بالستیک میان‌برد خیبرشکن را علیه پایگاه‌های آمریکا مستقر کرده است. این مقام‌های آمریکایی اشاره کردند که ایران این موشک‌ها را برای گریز از دفاع‌های آمریکایی از طریق مسیرهای پروازی متنوع، سرعت‌های متفاوت و مانورهای فاز پایانی، و از قابلیت پرتاب متحرک موشک برای ارتقای بقای پذیری و اثربخشی موشک تغییر داده است. ایران همچنین در آخرین حمله خود به نیروهای آمریکایی در اردن در ۹ سپتامبر موشک‌هایی با کلاهک‌های مهمات خوشه‌ای شلیک کرد. مهمات خوشه‌ای در ناحیه‌ای وسیع پخش می‌شوند و برای بیشینه‌سازی گستره خسارت طراحی شده‌اند، هرچند اثر هر گلوله‌ به‌صورت فردی را کاهش می‌دهند. ایران در حملات قبلی علیه اسرائیل از مهمات خوشه‌ای استفاده کرده است که عمدتاً برای جبران کمبود دقت در حملات موشکی بالستیک ایران انجام شده است.
اظهارات اکرمی‌نیا همچنین در پی اعلام ۲۱ سپتامبر دبیر شورای عالی امنیت ملی ایران، سپهبد محسن رضایی، مبنی بر اینکه ایران اخیراً یک موشک جدید با کلاهک مهمات خوشه‌ای را در حمله‌ای به ناو یو‌اس‌اس جورج واشینگتن آزموده و این سلاح در نزدیکی ناو هواپیمابر اصابت کرده است، مطرح شده است. گلوله‌های خوشه‌ای تقریباً به‌یقین نمی‌توانند یک ابرناو را غرق کنند، اما می‌توانند عرشه را آسیب بزنند و به این ترتیب عملیات پروازی را تا حدی و برای مدتی مختل کنند. رضایی احتمالاً به حمله ایران به ناو هواپیمابر آمریکا در ۹ سپتامبر اشاره می‌کرد. رسانه‌های ایرانی در آن زمان گزارش دادند که ایران از موشک بالستیک میان‌برد قاسم بصیر استفاده کرد که برد ۱,۲۰۰ کیلومتری دارد و کلاهک بازگشت قابل‌مانور آن برای گریز از پدافند هوایی طراحی شده است. اشخاص مطلع، 3 حمله موشکی بالستیک ایران به کشتی‌های جنگی نیروی دریایی آمریکا در اوایل سپتامبر را در گفتگو با وال‌استریت ژورنال در ۹ سپتامبر «خیلی نزدیک‌تر از حد انتظار» توصیف کردند.
ایران ممکن است این اصلاحات موشکی را بر حملات موشکی خود به کشتیرانی در تنگه هرمز اعمال کند. ایران از ۲۹ سپتامبر حملات تقریباً روزانه‌ای به کشتی‌های در حال عبور از تنگه انجام داده است. یک مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایران توان خود را برای هدف‌گیری کشتی‌ها بهبود داده و خطر برای کشتیرانی در تنگه را در هفته‌های اخیر افزایش داده است. ایران ممکن است از شرکای خود برای بهبود قابلیت‌های هدف‌گیری خود پشتیبانی دریافت کند، چراکه به‌گزارش‌ها روسیه اطلاعات هدف‌گیری ارائه کرده و جمهوری خلق چین تصاویر ماهواره‌ای به ایران داده است که احتمالاً به هدف‌گیری ایران در طول این درگیری کمک کرده است.
ایران به احتمال زیاد با اولویت‌دادن به بهبود قابلیت‌های موشکی خود، در پی افزایش توان بازدارندگی خود در برابر حملات هوایی آمریکا به دارایی‌های ایرانی، تحمیل هزینه به ایالات متحده و حفظ ابتکار عمل راهبردی در این درگیری است. همان مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایالات متحده کارزار خود علیه نفت‌کش‌های ایرانی را در واکنش به حملات ایران به کشتیرانی تجاری، پس از حمله ایران به پایگاه هوایی آمریکا در اردن متوقف کرده است. این مقام احتمالاً به حمله موشکی مهمات خوشه‌ای ایران به پایگاه هوایی موفق السلطی در اردن در ۹ سپتامبر اشاره می‌کند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21494" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZbHAtcYwVyMEzD3I_ojIb7s-OZAY-z3qDRKPYdAo84wqrMr5RfukMMFyWb2Rk1eZOQKXKFjN3Vcm0JtHkTWQ4FeNiwhpKjCjm1rx08FZirrucDibcQsChonQTx39B1CBAtN1x-JcY6zkzg-2jiOVBVblXhgw_JdIGYqIZLfQpH2ubmS2LVzDecRQW7hnu5xs7e9u4XwXxwF-bAPedJSXMNnf4to2MY607s1sFCfBscYPSEOboWKcMzIci7zS5uMOVZfeMytf7EhYV8jsLAtcfXX8Yr-ftjbCkB7IPizYcIJ7l5_b312_fHSMjqP7zJN-Zk3r1VRKtsvUr5j_uLYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC فرق خاصی با دیروز نکرده چون قیمت عملاً همانجا است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21493" target="_blank">📅 10:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-F4QFg1D9cnirTGmDnBZPq3JTNUevNQNbU2W0voguwbPN2QBvQ8pwreucy09jv6GM9YvOGWav8wZZT-NeyO6Hy3XmhAwskeqeKhOg9Sykpe4ZM0pbbQadTpNVFEh4C2gZKLhB437lp9NaTwFxLDeZlbA6066uLXs5qAojGg6tWjZyhhYjBLjko7BnqiTnFdKUjVK79gQuRucgBFbd1yFM_Ew6eOtOOhv6n6vmJtLHCHPBG2NdqgUE7xOStVIcclyDstsFhB2JGnIBBUTQsBhlqWdssKneQS9IJpzoNSrBnvaoak8Oxq7FHDeg8oyWhgCUyaQbQHsPN1oeoW1g_4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21492" target="_blank">📅 10:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxlwtrCa7FqkyK9va5osSYyXOpwSN-mebx85nlYhQhmDGCfh5XqilDG0l6NUe53GHNtICQMF3xn7EAxl43kA1C1Jqzjoy88vcYL9KwYDpxIxTbYqtPykNAXkrSlmXvUqOeU-DYI7xmHa_MICNRO0VoK3xdU-wpXZ7G6QVH1jWDkr1Ir9k0WdAJgGGc3tuu4TpNUiFQN6TXo2be6b1M65Au-V5oJ8fhIMB5h5Pe1I3cGSYk8F2o_Gr54Obgc1OUSOZfFYBQ-fhljfltdOUH7cyuHG1yRrzP3vIe56Ic7NrQ2agfKAHu47QUw6O74oIYVyI2HYiOApDOtRk_Bt64NOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، استفاده از اعدام با شلیک گلوله را برای مجازات نیدال حسن، که در پایگاه نظامی فورت هود در ایالت تگزاس، ۱۳ نفر را به قتل رساند، تایید کرد.
این اولین اعدام نظامی با شلیک گلوله از زمان پایان جنگ جهانی دوم خواهد بود.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21491" target="_blank">📅 10:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwcB9GTuRiAhIzFSV9uUt4QbV_yGrPAVeqDpCz14NOCjzfchAHk71KncY5qSuR62jtsmvYS8fJvwdQpzDsifQXnQRzBIFZSmjSg6YuwvW0K0b2cVpWXDhmtUuy9HmmVdIzTq_UUit9i62mGovDYLSo9rCABAZxRX_u36JqDOMUVqYpFfKaTKdCoL7lHFRw5NYSW5HOoYnLh1k1LHbuftnE5C13qAi27Jd6gmQQ_2sWjLYebc790HkiuUe-sFb9mLjI0ZMZ9_3EqttXGoAw_l7TkPVZuF8qsf39T8HfD1UAXs0vJNEA0AyiOx2vAbXczqAhqsrLU7PisqLUx6KKWLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طاعونی که در روسیه از آزمایشگاههای قرمساقها نشت کرده، تا ۱۰۰ برابر کشنده تر از کروناست!</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SBoxxx/21490" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💥
«هدف بعدی اسرائیل ترکیه است»
پل کریگ رابرتز می‌گوید که پس از یک کمپین برای شیطانی‌نمایی ترکیه—مشابه آنچه علیه ایران انجام شد—آمریکا به نمایندگی از اسرائیل به ترکیه حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21489" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21488" target="_blank">📅 19:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21487" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👤
مارکو روبیو، وزیر خارجه آمریکا
:
«ما طاعون روسیه را از نزدیک زیر نظر داریم و آن را به‌دقت رصد می‌کنیم. فکر نمی‌کنم دلیلی برای نگرانی و هراس وجود داشته باشد، اما قطعاً موضوعی است که باید با دقت و تمرکز بیشتری دنبال شود.»</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21486" target="_blank">📅 18:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک تایمز:
بیش از ۲۰۰ پرسنل نظامی و اطلاعاتی ایالات متحده به عربستان سعودی اعزام شده‌اند تا مستقیماً به نیروهای مسلح این پادشاهی در هدف‌گیری سایت‌های پرتاب و تأسیسات ذخیره‌سازی موشک‌هایی که توسط جنبش مقاومت انصارالله یمن اداره می‌شوند، کمک کنند.
این مأموریت مشاوره‌ای مخفی شامل تیم‌های کماندویی است که در طول مرز عربستان-یمن مستقر شده‌اند و در کنار فرماندهان ائتلاف برای کمک به جمع‌آوری اطلاعات، تداخل در حملات فرامرزی و تقویت توانایی‌های دفاعی ریاض در برابر حملات انتقامی پهپادی و موشک‌های بالستیک، همکاری می‌کنند.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21485" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کلیپی از کشتار نیروهای حوثی توسط سلفی های مورد حمایت عربستان   در ثانیه ۳۳ فردی که گزارش میداد می‌گوید باب المندب عربی است و نه فارسی ایران!</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21484" target="_blank">📅 17:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=awjeobcTjfv0XQxiLqxM9wQH0P9Kamjg0jfWgKi-qC7JQIvR_zr2-wIiaid-4O-Bg1FwiStoE0jGzyb4B356NFNos-BmMZVbDkUi0BLRxNaDmYHMAT3rPBQm7o8Fq_KqtHRnWx7JyPoOUsOqoTjaJa2xvGCCQw-BD6flyPUd9zqP3av5oqPp4FWYauvNDEdpYkvlihpzK_IR2rR_zgNQwkrp2BPSNcl_uHx6FfyVEGq2pqaJ5L1hBI_JIlBdZ5sIZ8ZZoPqp4iWyWN9rlYelmhWf-EbNjK8ZvhZFbi5aXy0R-WsDf1qwcYRSePyxjoH6pqbRX_IjQWrE14eK8UYcOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=awjeobcTjfv0XQxiLqxM9wQH0P9Kamjg0jfWgKi-qC7JQIvR_zr2-wIiaid-4O-Bg1FwiStoE0jGzyb4B356NFNos-BmMZVbDkUi0BLRxNaDmYHMAT3rPBQm7o8Fq_KqtHRnWx7JyPoOUsOqoTjaJa2xvGCCQw-BD6flyPUd9zqP3av5oqPp4FWYauvNDEdpYkvlihpzK_IR2rR_zgNQwkrp2BPSNcl_uHx6FfyVEGq2pqaJ5L1hBI_JIlBdZ5sIZ8ZZoPqp4iWyWN9rlYelmhWf-EbNjK8ZvhZFbi5aXy0R-WsDf1qwcYRSePyxjoH6pqbRX_IjQWrE14eK8UYcOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21483" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">— مقامات اسرائیلی پرونده‌ای علیه یک استاد ریاضیات دانشگاه که مردی در دهه ششم زندگی  و اهل پتاح‌تیکوا است به اتهام برنامه‌ریزی برای حملات گسترده علیه شهروندان عرب اسرائیل تنظیم کرده‌اند.
بر اساس دادخواست، هدف او اجبار به اخراج دائمی آن‌ها به اردن، لبنان و غزه بود.
او قصد داشت ۷۲ اسرائیلی یهودی را در ۱۲ گروه برای انجام حملات هم‌زمان جذب کند، با حمایت از عناصری در ارتش اسرائیل، از جمله حملات هوایی به مراکز جمعیتی عرب.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21482" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21481" target="_blank">📅 15:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21480" target="_blank">📅 15:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-text">باب المندب؛ قدرت های بزرگ‌ بر می گردند؟!
وقتی ۲۹ شهریور(۲۰ سپتامبر)‌ نوشتم به زودی حوثی ها ناگزیر خواهند شد از باب المندب عقب نشینی کنند، سخت مورد نفد قرار گرفتم.  البته امروزه روز، مساله اصلی این نیست که حوثی ها شکست خوردند یا عربستان پیروز شد؛ بلکه مهم‌تر این است که باب المندب در حال خارج شدن از وضعیت اهرم یک بازیگر غیر دولتی(حوثی ها) و برگشتن به مرکز رقابت دولت های منطقه ای و قدرت های بزرگ‌ است.
پسگرفتن باب المندب از تسلط حوثی ها، در چارچوب بازآرایی ژئوپلیتیک ی پس از بحران ایران ـ آمریکا معنا دارد، نه صرفا یک عملیات جدید در جنگ یمن.
اگر باب‌المندب توسط مخالفین حوثی ها تثبیت شود و همزمان فشار بر هرمز ادامه پیدا کند، یک نتیجه بسیار مهم حاصل می‌شود:
دو گلوگاه دریایی خاورمیانه، به جای آنکه اهرم‌های مستقل ایران و حوثی‌ها باشند، ممکن است به تدریج تحت ترتیبات امنیتی چندجانبه عربستان، آمریکا و کشورهای غربی قرار گیرند. و این برای ایران از خود عملیات امروز مهم‌تر است؛ زیرا در آن صورت، عمق ژئوپلیتیک ی ایران در دو سوی شبه‌جزیره عربستان همزمان محدودتر می‌شود.
به لینک‌ زیر سری بزنید:
https://t.me/Karimipour_K/6256
#یدالله_کریمی_پور
#karimipour_kپ</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21479" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خوش چشم:
اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21478" target="_blank">📅 14:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لوئیز ایناسیو لولا دا سیلوا و فلاویو بولسونارو به دور دوم انتخابات ریاست‌جمهوری برزیل راه یافتند
با شمارش نزدیک به ۹۹ درصد از آرا، بولسونارو ۴۷.۲۸ درصد و لولا دا سیلوا ۴۴.۸۷ درصد آرا را به دست آوردند.
دور دوم (Runoff) در ۲۵ اکتبر برگزار خواهد شد. این دور به این دلیل برگزار می‌شود که هیچ‌یک از نامزدها بیش از ۵۰ درصد آرا را کسب نکرده‌اند.
لولا دا سیلوا، رئیس‌جمهور فعلی، نماینده حزب کارگران چپ‌گرا است. فلاویو بولسونارو، فرزند جیر بولسونارو، رئیس‌جمهور سابق برزیل، نماینده حزب لیبرال است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21477" target="_blank">📅 14:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اعتراضات گسترده در اسپانیا؛ خیزش علیه دولت چپ‌گرا و سیاست مهاجرتی سانچز  موج تازه اعتراضات در اسپانیا علیه دولت پدرو سانچز، نخست‌وزیر سوسیالیست این کشور، به یکی از جدی‌ترین چالش‌های سیاسی دولت او تبدیل شده است.   کانون اصلی اعتراضات، بحران مهاجرت در سئوتا،…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21476" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا  فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.  در کنار فشار بازارها، بن‌بست سیاسی…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21475" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHikEG3tGSJNGi85Zx8_Ss9otJkr8cUmWwEhmIfhmgBNzFkjztmFf2wp8oDRMC47ByVzPXAQH0CRDmLPeNLkTn5L6i1YNvJ_w0N0Ej6K2QOE_Kof7uRq4qA3kVxYCAGuGxFm63iA-cfZHoFhAqtxuplFcgjEmhrXY9THVL_I6cSvM6sRryuYlj1r3wtaof81fL86N5KmU4wYypqFXLv177c_-f1w1wY9v-if0Lnw1PnkICd4saU6UgDYEXoxtnJWVROmUiW6t5HvRVYeijJzz37mp-vjAVxsv38Ufek4LlSF_h-zh5i1XLf6ztT2HKzBl_ONXrr9bLHamLhU1ZnXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا
فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.
در کنار فشار بازارها، بن‌بست سیاسی و دشواری تصویب برنامه‌های ریاضتی، مسیر کاهش بدهی را پیچیده کرده و بحران مالی فرانسه می‌تواند به یکی از مهم‌ترین چالش‌های اروپا تا انتخابات ۲۰۲۷ تبدیل شود.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21474" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBOef-WL4iYLKOovtBd3w-cf7mCg_bjU0ztjkjZn3pjxjIvJMeviffpBsArp9Homi_NRtMlwFrBD1DQ3BO1hb9NH5CnJFHydXhPVTnoM_9ZW5nV8TTidci2OBV7DZ68a3GZ2fvffO_BnM4qORqqSlkMbb3DCj1ZvKf8_5I4Z36wW9HtGX2HZ3FVhkUtBRUzheCF4SaRef4qspSxR9rHrNayMXjq91W3LLD_hCBUJ6PkkMrdT35iaHBWQfdk33Rx35sY4hei4H7dMkuTYrvNpvKcbRWxa-fX542KU84YUZIqPd8gPbeoV6iXEZlkCf9AVvoKxeSc-j6k9qwenf4FlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله  به گشت پلیس در بمپور  بر اساس گزارش‌های اولیه و به گفته منابع آگاه، یک گشت پلیس در شهرستان بمپور هدف حمله تروریستی قرار گرفته است. این منابع از شهادت یک نفر از نیروهای پلیس در این حادثه خبر داده‌اند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21473" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21472" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9sZfllMIVDEjR67Rs_fwKp0gtgxgsu3aBSt30NIuXMcWv_62AdLnd5lUb9EPLzaP62WROl7jKbv68JyfJH-YgyUhxB_I9uDi4z3327DeuNgcc1sSS9gXpCrn1-FpuXsSsfEdzDhPNcJPOcu0vC3nRKyDCBnqBoRsOSzdedfekRViZ9fiGO_JfqikGgXp_gl4BELdsvO4NshEIMQ0gPL_M7buO0N_K1QtrM78cnyelgSRxv1ufyW5y_kxF8haewH9K-ia9h3iYbrgLWLps-vPt5Ax088MYJS_JrxG0_fRqDXRx2zB3qz-MSVa_utBQokQcvegjq224RYiMg988Jkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان در سطوح پایینی قرار دارد و فضا برای رشد طلا هموار است.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21471" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgZtgOMyyF3vieQ-ksSkyjlzoQcURzUdIwd1q-TRgrQQpouO2m955owyGkpgEIROspfFz5Dg7pJJdTuOPd3ll-YYBQe1vrDT_X1XH_62_Ic5sKAvlUj79MRD8s2k5GN1opbJ3kpSDIxoRcNqPzqV8p_Sl99roviVVp60STOgtJSbsN3nA2ba7abQ4RCraGhqPkX2AvCcqYeAZlOOMzoDstdkiV1Eh5lraQlc2ONHY5vlwZM-q9wTDlyLUA9JxvDZIWhLeXZhAFL0_bPdKPsz4TJeJzSK6D5vkPaqIXnJIEgceqKr4-hWm2Nw7KG3J6HXofKS881vsv7h4CwkYl3-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21470" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر اقتصاد:   تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21469" target="_blank">📅 10:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر اقتصاد:
تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21468" target="_blank">📅 10:11 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
