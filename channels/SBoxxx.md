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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 01:09:45</div>
<hr>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ستوان سوم وحید عنایت از نیروی انتظامی امروز توسط شبه نظامی‌های تکفیری در سیستان و بلوچستان به شهادت رسید</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/21570" target="_blank">📅 22:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">همان گفتاردرمانی همیشگی ترامپ است. به نظر من هیچ گفتگوی جدی در حال حاضر جریان ندارد و همانطور که خود ترامپ می گوید، فقط زمان حملات آنها شاید به تعویق بیفتد.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/21569" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:  ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم و تا پیش از برگزاری انتخابات میان‌دوره‌ای، به هیچ وجه به ایران حمله نخواهیم کرد؛!</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/21568" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF4OOH-6uYE-czYqfyMu53B1lF7YhaZZIxi--P7zTomRoC5vmqzdEWs58UM-eXg8vFVpv-XfRkq70px7B7bapF2ixwiX2UoCRBJ_mNHExcnm3YlX6CxHTpCktG5gbDUxumbrtQM-WsGaKTPZg45EmB24e50QS6JWFUUJTII8Jc6u1hIQji77oPkVX7AlN2SoXni5ftwIRs80YC-IGOYrsNb72rHDRgAssXUlruJZg_zUaUfvJwSqcDlQCHKRr0cxc8cX27EXX9Mh0KBCZ5yjSXabwdifLpe5UC41Rv7zrA2LfZ6-6lHVgmEr-cfz6FCAy6ouM4TWxio-wEDzQtd6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش کانال 14 اسرائیل، مقامات ارشد سپاه پاسداران انقلاب اسلامی خواستار حمله به اهداف مهم در منطقه طی 3 هفته آینده شده‌اند. آن‌ها معتقدند که ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/21567" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خیلی شبیه هم بود این 2 خبر که ولی خب</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/21566" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/21565" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/21564" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/21563" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpedwgxxpYgEZ9TqjsvsOAyn0FWI5zfVnaT5_KRLxCMMhh72WAhpniI_E9MswJeo9sY3DzeUZMmiupkqMex0f9WvxieDpooP216awGNVwJpJTe_tBHQb2YRItnrOcSLCtCKL0kOc7549KM6jFqlX-6n7jfM66tsGpCk8eOHuveZCmhRIz7mbkfUUb97MaxlOpTO9ZYd1jEBPOcjxXswAqb6-CPQYeEgxgpct4pjMAXGwtdXRTu6SVyGzDKVrkcqFVMB_KWL7mc1_9RBJs_ULEwAOIsHfQ5mMlRBRkVIoJDPAcYDewQMSI8BWiNs_ITcoJUvnY6TcYMaOPsoaQD_GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/21562" target="_blank">📅 19:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKwpp_JoBDJewB2H4JQV9_30dyNMkPzDLgLi9mFcBjxXVBWo1uSTkXDMJDVrv-hdg8gShEuhfzhU6XXdJzGotHe_LOvyH2MLfbSuHQ2E7zbkmgqTBspocXS0uKb6KYnD7usVNOsc6QFtIdh8W28Qz6AnA-Dfcm4A5Vh6MeyaT41HrZbDUQ95-Nw_hKA34Dg1YueGNHf2cXweOmxXvukPYRozsXBMHtcqdkUP3LktOV3k4AOOQX6e3btFMksDUCHuYY6AC4iGyu8wHjAicLOpUFEtTwi4AZLAOWYAqyn20dNeXfANb5Bz9CvsZm-TJVFSfqb5VnAdUK25NYfnkk-r2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/21561" target="_blank">📅 19:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/21560" target="_blank">📅 19:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJddqNnZhSYpt6jJk9pGdcnjBR8sRz7UCsaN0gs3LSFuNeBeigfWumH6W6d0B6I9nPnr_MSKicLdrOhh4vrCG6VTdjQBheieVu2Wll1RJ6pNloL2QsuoNkEc_TpeckIW9MHVw6u6LLe8eV7XSjmdR6N3FLbQCXICbxFrCzV75dVrhnHZkHugG33Gy9lAXk_YYV3_FzHHoqQvebpOjikllmhRLfAYmfCOL_tfuu0NUfdPeCa7s2nNdnFVgvXeGOR5QDCMZzhoJvqiQ57UlGWQGIhQNm8vrEDbGYTqA8XzNVbG_OKoKIKx5ACWY90OALUz85-V2ABARagO-FiEQJKvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/21559" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/21558" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBwarYpEseRdA1tgFndNOj-mPwEz-3JRfF0Tzun2uGmyDSxfGGlUsaJGZArKdHSz-1hagEQTa_lRaTyBbVEKVUQOp4nRX9W9FHpvHdCcQen8l4Y_VHU7_ROrSNJqpbngzcumLr1eDH3yM-HeEpZWqVTDv2KTY2tAUOqQDLrzItU0K3W6n3AdObFzWdvZNp_SXwFyCo_njbLKrPnxj9IBD09YdKvkvAjJRmPEabX8Ld1Sd5-ma__Z8JgHQMcZbiprbSyADqI0QBdl0OUIL4O10_H6Gb-R0LWyD0kGzia77LdfjhFZXiNld5Vxez5wLICzBgwWC8sx2bgmcsMhaCvDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/21557" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/21556" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/21555" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/21554" target="_blank">📅 15:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر    در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21553" target="_blank">📅 13:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صحبت های یک استاد دانشگاه امام صادق درباره اینکه چرا فقط تنگه هرمز برای جمهوری اسلامی به عنوان ابزار فشار باقی مانده است</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21552" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21551" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر
در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21550" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxas4O0ENsOQJMmfLQGRN4B5MHuujHdPK_1IIxsYv85xzjbdzF4S0Cs-wApsnPlKZ7YAjvKSVV4cYI24dI4hmL_tELAoVvWgUkIQtPqGz8m0Fe2gTjIUva-Ttm9_CEGPiwC6qEGbOPpMHrAoyFVifwwZCyDYEf7W5N2OPeUooVSlmB6WOubO0wYum7Z8qiXJzPj4pGIU_yzFiMFn_YEBAboUo4_F-PW8eBg_kRwHPM2dSm8NmhQl4pZtX19-Lgg9tNhObvpTM_0YwpheXifmZsW6VfeW4UQPGO5uRfS1ULDplwrMH9Wt7nip9Aw2qFcadN5-1zyCyhqIXAe5t0zqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21549" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPeBxL3wlNUK2Lxt3VqX3jgfaNfEeslXlsW2BIO5DN9IR4OlFyiMKv1iPt-HXQQjfQsUNf8QjmvGPAKyGnwEe1zF4vn9dxBH22IvQLsKhn55QLsLRGwWdScNTjHCQns6W4Dx6sqPBBRQYJ_bWHzFE10mpG-fVGk4L0CSJdTujVn5dEzeuG1vxefO-XLWW-OgTeYjnzXweeKeh_sP-2f3L8k4AH9KHEpwZNy3dEvfoEWIaalR76SjncLENm09_WBV-lgGAx0qC0SEjCDlhWGBlP5yBUG82NPm7WU7udemLK2DZmymJi5k7FMjprU9Yb8K_y_sBatkcLdkaksgesEz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده بیش—فروش قرار دارد و خرید در حمایت ها منطقی ترین گزینه است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21548" target="_blank">📅 10:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eam8uXfxkWJ6ZINaTIg6Gpao8PQheDEu7FNwEIdB7lC5bxNbdCdrH23WQE5dTDnPD2QsjZZXdVU81-LF1lgDTBWwGnS2DHkIYVvlBqVeuIK1L7ELNStoOld07SaUQCIFFyQn9y2Sq9S9d_G1YnV2M0RYb8e4ln2uYyOP--Fd9BSnqpmDg8oc7y-lxFfRq3wUbjkuzlyOjC4rb8p6H_S5jfPpM_72HXp0vmHRPOZQvl_-tYIRN-cHzelGM7YyYSQocqNQZaAdk6F3zpxwuMV1MIlxZ4XBM2xrXFJfvnzsLCv0vlAhojtcsUkRFNjSKwWSh4pFf8PptEIt4fKHq59jBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در حمایت ها توصیه می شود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21547" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.
ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر رخ دهد.
یک تهاجم جدید می‌تواند شامل حملات گسترده ایالات متحده و اسرائیل به زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران باشد که احتمالاً منجر به تلافی موشکی ایران و افزایش قیمت نفت خواهد شد.
مذاکرات هسته‌ای ایالات متحده و ایران همچنان متوقف است، در حالی که ترامپ و نتانیاهو، نخست‌وزیر اسرائیل، در روزهای اخیر دو بار تلفنی با یکدیگر گفتگو کرده‌اند.
مقامات اسرائیلی معتقدند احتمال حملات پس از انتخابات میان‌دوره‌ای بیشتر است، اگرچه حمله زودهنگام همچنان ممکن است.
— آکسیوس</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21546" target="_blank">📅 09:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران،  بقایی:
عمان با ایران بر روی مختصات جغرافیایی مسیرهای امن عبور از تنگه هرمز و نحوه ارائه این توافق به صورت بین‌المللی به توافق رسیدند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21545" target="_blank">📅 00:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایران، حفر و توسعه را در یکی از بزرگترین پروژه‌های غیرفعال خود، مجتمع زیرزمینی آبیک که توسط سازمان‌های اطلاعاتی غربی و اسرائیلی با نام رمز "سایت 311" شناخته می‌شود، از سر گرفته است.
این سایت در امتداد محور تهران-قزوین، در حدود 100 کیلومتری تهران واقع شده است. این مجموعه در دل کوه‌ها حفر شده و شامل چندین ورودی تونل است که احتمالاً به یک شبکه گسترده زیرزمینی شامل ده‌ها سالن و پناهگاه متصل می‌شود؛ این مجموعه یکی از بزرگترین پروژه‌های از این نوع در ایران است.
تصاویر ماهواره‌ای نشان می‌دهند که این یک پروژه بزرگ است، با حجم زیادی از خاک و سنگ‌های حفر شده، زیرساخت‌های پشتیبانی و پوشش سنگی قابل توجهی که از تأسیسات داخل کوه محافظت می‌کند.
بیشتر کارهای حفاری در این سایت بین سال‌های 2007 و 2016 انجام شد. پس از آن، به دلایل نامعلومی، کارها عملاً متوقف شد.
با این حال، بلافاصله پس از عملیات "خشم حماسی"، تصاویر ماهواره‌ای نشان دادند که تغییری آشکار رخ داده است: ایران به این پروژه بازگشته و با سرعتی که در طول حدود یک دهه در این سایت مشاهده نشده بود، حفاری را از سر گرفته است.
این سایت در سال 2010 توجه بین‌المللی را به خود جلب کرد، زمانی که از آن به عنوان یک مرکز مخفی غنی‌سازی اورانیوم نام برده شد. این ادعا هرگز به طور مستقل تأیید نشد و هنوز هیچ مدرک قطعی و عمومی وجود ندارد که نشان دهد غنی‌سازی اورانیوم در این سایت انجام شده است. هدف دقیق آن هنوز نامشخص است.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21543" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21542" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرمساق کاکولد با بهترین تجهیزات آمده نیروی دریایی فرسوده ما را غرق کرده حالا کری می خواند!
پدرسگ اگر شما هم کشتی های ما را نمی زدید خودشان داشتند یکی یکی غرق می شدند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21541" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیت هگست، وزیر جنگ:  ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.  نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21540" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
ما با نیروی دریایی جمهوری اسلامی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
نصف پایین را آن‌ها گرفتند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21539" target="_blank">📅 23:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">موسسه UKMTO:
گزارش یک حادثه در ۵۱ مایل دریایی شمال مدینه الشمال، قطر دریافت شده است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21538" target="_blank">📅 23:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، ایتامار بن‌گویر:
ما خیلی نرم هستیم. این جدل من با نتانیاهو است.
اگر کسی در حالی که پسر من در ارتش خدمت می‌کند، به زندگی او تهدید کند، خانه‌ای که آن شخص از آن بیرون می‌آید را از بین ببرید.
و اگر دختری دارید که سرباز است، می‌خواهم او را محافظت کنم تا حتی یک تار موی سرش آسیب نبیند — بگذارید ۱۰۰۰ تروریست بمیرند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21537" target="_blank">📅 22:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار با دلیل نامعلوم در حیفا اسراییل</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21536" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">— حزب‌الله ماه گذشته ۲۰۰ میلیون دلار از ایران دریافت کرد تا به مردم لبنان که به دلیل جنگ امسال با اسرائیل آواره شده‌اند، کمک کند، با وجود افزایش فشارهای اقتصادی ایالات متحده بر ایران و دشواری‌های فزاینده در انتقال وجوه به این گروه.
واسطه‌هایی که پول را جابه‌جا کردند، کارمزد ۲۰ درصدی دریافت کردند که چهار برابر نرخ معمول است و این امر بازتاب‌دهنده خطرات مرتبط با مدیریت وجوه برای حزب‌الله است.
— رويترز</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21535" target="_blank">📅 19:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به نظرم وقتش رسیده که یک بار دیگر بکشیمش.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21534" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مقام ارشد ایرانی: ایران هرگز حق غنی‌سازی خود را رها نخواهد کرد، اما جزئیات غنی‌سازی می‌تواند بعداً مورد بحث قرار گیرد.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21533" target="_blank">📅 15:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
‏حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21532" target="_blank">📅 14:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو درباره ایران:
کشورها، حتی آن‌هایی که به ما حمله می‌کنند، به‌صورت پنهانی و پنهانی می‌گویند: «(حکومت ایران) باید سقوط کند. آن‌ها همه ما را خفه کرده‌اند.»
ما اطمینان حاصل خواهیم کرد که آنها سقوط کنند. آن‌ها سقوط خواهند کرد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21531" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21530" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/modjddpGPoUcqf7NcgtDjE71I5JAIubKkX1rxb9TRx7Ok4DEgXYHUxBMRpy8h4prH3us74JfWJtf7MdXHUqSEyfkqBFwGXHEb2ahCaEL_wIFur3H3nY3iwj10L2KmVBscCIJqN1FLLLp0hXKgb3P4980-VMzoKKGlosza4t4BHdSyVtvAnXruO5iTzfA3sJeBqFvHYAJQ6iXMDzkQOewiOQF1ajL73GVlRx3CNM4A-mII3ICEy2Z8pgoNc5WTnXuDPw30WnpX4Q1l_xkGC-Okqn0tksVHVPvc_JOzRa2KkSsHY496xzqB7BZEKNiqdZCE_IJy1qQZX_tCTYZEmtBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21529" target="_blank">📅 12:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klp0UOWeOZVApzWDRxZ36dQXWWMQAHe8P2qnomY1P4VpU5m9zqg6ax1P8QJP2Z91XeUlx_TzYo9Z4axzTS9Gf2Twkk2CDqtmKht0Lfr62Leq_WN5Z4YyE1AOd51G5fkFI0trvCoiQqnLF_aE-KQtmxf35M9JWyad-3YYYChMYD26_QWCCmEQghlLhiW3U7w1ABs0HFHEnOAQgSQu7UzEfjTY3jc5STD2XmGUwp4evx8FZ2weBy20hrXNF8CEyAAdHg_ln_MQrrJvmGtMcEDJ6pKrcFZU0U6ZG9xjjc1n24AiveanImTlmfHtz_04kyrkPKXFVKgdIgWfHkliWxGJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21528" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_53JnJnDFJKqnLI0-FJBBillDp2ZJHZoqXXqqMk7UPdB16Q51k9AAIxizqSrrfvDolUYJjLB1QfxAVk1iNSPaA_cld1z_IC1ENyX5SiPefrBwKL2tiX6CPoKGlmbMdvnsItPqieWf9LN8UP5ruu-n8_pz2lCwxvIN4qyT_T5xPFVljM7e0jtT0gPvfN5_G67a7OtECGFhkerYY6JHFRMq_yC4Q9MeqO752I3zwxrYepBWglJw4SI-gibx6kjTJt4JhmBQdMsm5Q4eQRWOBpBVzHQ1csD6-fTfCIQE2n-68qU7ufDgoo-W1TTTP47IqyM4K-oDLVplUlH4NuybAcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC به محدوده بیش—فروش نزدیک تر شده و این موضوع خرید را قوی تر می کند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21527" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3MdT_GIIKcqWsgfFjLj3QjYfpVKe7g_RZThEx3FvcEGgvVcqZ_jH8TpFbMEjUIo8KntYeqKls_I2GNeoSzfzYY_FS4Mo_sVTUxuOBEzVp9ES7Sc2hQDd9j--rBxAQsXHT-LkYKX_ANpeufTox3rDf94L0ol_OcJSh-3ryOjS9PPi_eV2wqagXxUpR2zIH0s-NqQdUb9n9NOfiMe7fk_1Ww-zFnionsIuTck88mdc2UwD865nm0o4Jj1TUO_XfibRVHpkbbU6i_o6omj_htOvFLb1ZvWRPi8GOmsyzyzWzLobGCJ6QlXxxhq5ZG98X0fIEHM2S8AvMT1odFAXJAAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش طلا تا این لحظه، خرید توصیه می شود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21526" target="_blank">📅 12:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRvReluLBIBj8AVUlS8JyojvT7SA8NXg9Z0Spxaq1oqOSsP4yT-FB-2jxjRy4yLP-mrUatG0vAtVQ3dCHsX3M6QEW0JNzh7rZ3qGsC0euKaf1YesI4Ly6eRemAIILy6TWldG0hqXLjVRWK2pkLOyS-MAneq3kKxGRWxxJKWs_OYXAisgRuGrQVyFn_EjqB75VHT05U5zdY_Z83qZVgyFBW32o423A0Jflud3LpnnQiORV0W9W63nxDoie1_juDXmFZrdzymJh4L8fUsRAna_12oABfSqwMu4bTMSlyiZyBdrxFz-brE9Ue1_1xVcTGwwZzaFa2v-vLFqvhdJ9DxJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاره پیروزی اژدها (نماد چین) در جنگ با عقاب (نماد آمریکا) در میدان فاطمی!</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21525" target="_blank">📅 11:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ذخایر طلای چین در پایان سپتامبر ۷۷.۴۷ میلیون اونس خالص بود، در حالی که در پایان اوت ۷۶.۷۳ میلیون اونس بود
اما ارزش این ذخایر طلای چین در پایان سپتامبر ۳۲۳.۵۲ میلیارد دلار در مقابل ۳۵۰.۰۸ میلیارد دلار در پایان اوت بود</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21524" target="_blank">📅 09:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تعز به تصرف حوثی ها درآمد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21523" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
اسکات بسنت :
ایران وزیر نفت جدیدی انتخاب کرده،
با توجه به اینکه آنها از 25 آگوست حتی یک بشکه نفت هم برای صادرات بارگیری نکرده اند، این وزیر جدید عملاً چه چیزی را مدیریت می کند؟!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21522" target="_blank">📅 08:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn7T-eRTttA8Ky6kBcUZTqCoSuii6yEz1mzTc3gDJqCkVmaD9x1vZ3occEzsiLx7hlrhuZcLPyAtgjT7I1f5mXSufjFNXVxMap4pDJXpVAYlhFVUSDGmyWIU0E7B4g-m8SjDhAyJXm_5SjVCSjNdpDJU4zSsUdsAiVKrDa9VO_MEVzsHfCjImS2RZa_Ypksz5QEiCC_fyZzw3L9NUsSMEcz0nAlqXwo03bPGl4PWdvbJxtA65L4yLcAp4eJqd_6kyV8L4Rz8YxNFDdqKNQy_MtfduyWYiU-z2QlLnH82VWs46ohQhDnyKa0xBjP9cY-dyVZSR2rPxdO8zYa1M4uO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خب بعد از اینکه به بسنت این را فهماندیم، دلار 40 هزار تومان کشید بالا که مهم نیست چون مهم این است که ما مجبور نشویم بکشیم پایین.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21521" target="_blank">📅 08:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21520" target="_blank">📅 07:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این مدلی بوده که اردوغان تروریست های جهادی ترکمن سوریه را که تحت فرماندهی «تیپ سلطان سلیمان شاه» قرار داشته اند به جبهه های جنگ قراباغ اعزام کرده است.  پس از ورود نیروهای سوری به جمهوری آذربایجان، در جلساتی با حضور رهبر تروریست های سوری و نیروهای نظامی ترکیه…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21519" target="_blank">📅 07:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آماده‌سازی‌ها برای جنگ میان اسرائیل و ترک‌ها با شدت تمام در جریان است Damir Nazarov  پس از به‌رسمیت‌شناختن سومالی‌لند از سوی اسرائیل، تحلیلگران این اقدام را تلاش نتانیاهو برای ایجاد پایگاهی در برابر انصارالله یمن و کسب اهرم فشار در دریای سرخ ارزیابی کردند.…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21518" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خیلی حرف های بد دیگری هم زده که اینجا نمی گذارم.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21517" target="_blank">📅 00:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دونالد ترامپ:  تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21516" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دونالد ترامپ:
تنگه هرمز به ایالات متحده آمریکا تعلق دارد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21515" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاخ کرملین: رئیس‌جمهور ایران روز جمعه در اجلاس سران کشورهای سابق شوروی که به میزبانی روسیه در ترکمنستان برگزار می‌شود، شرکت خواهد کرد و با پوتین دیدار خواهد داشت.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21513" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21512" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
آنچه در فرانسه در حال وقوع است، چیزی جز مهاجرت گسترده و بی‌رویه نیست. این موضوع نه مربوط به مدارس است، بلکه مربوط به اسلام است که قصد دارد بر کشوری که قبلاً عالی بود مسلط شود! (رئیس‌جمهور دونالد ترامپ)</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21511" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فیلم وزارت اطلاعات از ضربات به گروه های تکفیری در سیستان و بلوچستان!
قشنگ خاطرات بازی Counter Strike زنده می شود.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21510" target="_blank">📅 18:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دبیرکل حزب‌الله:   آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21509" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دبیرکل حزب‌الله:
آزادی جنوب لبنان را پیش روی چشمان خود می‌بینیم!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21508" target="_blank">📅 18:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21507" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇫🇷
سفیر فرانسه در تهران به علت برخورد خشونت‌آمیزِ دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر به وزارت امور خارجه ایران احضار شد</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21506" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های عبری‌زبان در تاریخ ۵ اکتبر، اسرائیل در حال تدارک برای اقدام نظامی احتمالی جدید علیه ایران است؛ اقدامی که ممکن است به‌صورت مشترک با ایالات متحده یا به‌طور مستقل انجام شود.
روزنامه «اسرائیل هیوم» گزارش داد که ارتش اسرائیل ضمن حفظ همکاری‌های نزدیک اطلاعاتی و عملیاتی با ارتش آمریکا، خود را برای حمله احتمالی به جمهوری اسلامی آماده می‌کند. این تدارکات شامل سناریوهایی است که در آن‌ها اسرائیل یا دست به حمله پیش‌دستانه می‌زند و یا به حمله ایران پاسخ می‌دهد.
این گزارش احتمال وقوع حمله اسرائیل یا آمریکا پیش از انتخابات میان‌دوره‌ای ماه نوامبر را نسبتاً پایین ارزیابی کرده و حاکی از آن است که این آمادگی‌های نظامی برای رویارویی احتمالی در زمانی دیگر صورت می‌گیرد.
هم‌زمان، وب‌سایت «والا» گزارش داد که واشنگتن در حال آماده‌سازی برای اعزام نیروها و هواپیماهای بیشتر به اسرائیل در هفته‌های پیش رو است؛ این در حالی است که هم‌اکنون حدود ۳۰۰۰ نیروی نظامی آمریکایی در این کشور مستقر هستند.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21505" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فوری - قطر اعلام کرد که ایالات متحده و ایران همچنان در حال مذاکرات برای پایان دادن به جنگ هستند</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21504" target="_blank">📅 15:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترکیه و پاکستان برای حمایت از عربستان سعودی در برابر یمن، توافق‌نامه مکه را فعال کردند
آنکارا و اسلام‌آباد متعهد شدند که به‌سرعت نیروهایی را به داخل خاک این پادشاهی اعزام کنند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21503" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21502" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خلبان آن هواپیمای فلای دوبی هم که داشت سقوط می‌کرد هندی بود!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21501" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت امور خارجه هند:
۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21500" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21499" target="_blank">📅 14:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نشست کارشناسی بسیار جالب و دیدنی درباره روند جنگ ایران—عراق و فرصت هایی که برای پایان جنگ وجود داشته است:
https://www.aparat.com/v/goil745?playlist=27887251</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21498" target="_blank">📅 14:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انصارالله ادعا می‌کند که در دو روز گذشته حمله دوم به فرودگاه سعودی را انجام داده است
انصارالله اعلام کرد که با یک موشک بالستیک به فرودگاه بین‌المللی ابها در استان عسیر عربستان سعودی حمله کرده و ادعا می‌کند که این ضربه باعث اختلال در ترافیک هوایی فرودگاه شده است.
یحیی سریع، سخنگوی نظامی انصارالله، گفت که ضربه موشکی «دقیق و مستقیم» بود و به شرکت‌های هواپیمایی بین‌المللی هشدار داد که از ادامه پروازها از طریق فضای هوایی سعودی خودداری کنند، زیرا به گفته او این فضا به «صحنه عملیات نظامی ما» تبدیل شده است. ریاض تاکنون به‌طور فوری این حمله را تأیید نکرده است.
این حمله پس از حملاتی رخ داده که انصارالله در شب دوشنبه به فرودگاه‌های جازان و نجران نسبت داده بود و پس از آن حملات، مصدومیت‌ها و خساراتی گزارش شده بود.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21497" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرانسه برای اولین بار موشک بالستیک جدید خود با قابلیت حمل سلاح هسته‌ای را از یک زیردریایی هسته‌ای آزمایش کرد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21496" target="_blank">📅 13:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lANRgySXDs1hI7KTGpKpevYbt83ivbReu5pjMOit2o58mfrMKY5fSr0H9Red1GobDQ9J4Ed3gojS0ClsPIkRNhRl6zgvn4p76P8jHhp0PgKFOyawUB0eIfEnC0XwlStysv7pw0A4TNs3c_D1f2TC5OHtpKNtyFCivsRkVoUz7dkuQNlzdzrx_600z4JZ-UzY_BeMAxVnjl5FdD5GZmktZ99TxRt6LwUmZ_G07GGxsg1esi_5cMqYayk9iGLgPjruwKfeuRYyUfbZrlH3r0p1OyuhQSkdLUCycC3CRpxTqJvpGWSdUUDqfvbvHai07tzKbJ-LiR19qyogRiSivcKQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر وقت یک نفر که ذهنش اسیر تفکر فرقه ای نشده  فهمید که میان توران بزرگ با اسرائیل بزرگ کدام بیشتر به زیان ماست و آن را بدون هراس بر زبان آورد آن وقت می توان امیدوار بود که پویه های ژئوپولیتیک بر محاسبات کلان سیاست خارجی کشور حاکم بشود و نه انگاره های وهمی…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21495" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موسسه مطالعات جنگ درباره کوشش ایران برای بهبود و ارتقای توان موشکی خود:
ایران به احتمال زیاد در حال بازسازی و ارتقای توان خود برای هدف‌گیری اهداف نظامی دوربرد آمریکا در منطقه و کشتیرانی تجاری از طریق بهبود دقت، برد، سرعت و قابلیت‌های هدف‌گیری موشکی است. سخنگوی ارتش ایران، سرتیپ محمد اکرمی‌نیا، در مصاحبه‌ای با رسانه‌های ایرانی در ۴ اکتبر اظهار داشت که ایران در حال بهبود دقت، برد و سرعت همه موشک‌های خود است. اکرمی‌نیا افزود که ارتش باید برد موشک‌ها را افزایش دهد تا نیروهای آمریکایی در منطقه را هدف قرار دهد و اذعان کرد که نیروهای آمریکایی تا ۱,۰۰۰ کیلومتر دورتر از ایران جابه‌جا شده‌اند.
مقام‌های آمریکایی در ژوئیه ارزیابی کرده بودند که ایران نسخه‌های پیشرفته موشک بالستیک میان‌برد خیبرشکن را علیه پایگاه‌های آمریکا مستقر کرده است. این مقام‌های آمریکایی اشاره کردند که ایران این موشک‌ها را برای گریز از دفاع‌های آمریکایی از طریق مسیرهای پروازی متنوع، سرعت‌های متفاوت و مانورهای فاز پایانی، و از قابلیت پرتاب متحرک موشک برای ارتقای بقای پذیری و اثربخشی موشک تغییر داده است. ایران همچنین در آخرین حمله خود به نیروهای آمریکایی در اردن در ۹ سپتامبر موشک‌هایی با کلاهک‌های مهمات خوشه‌ای شلیک کرد. مهمات خوشه‌ای در ناحیه‌ای وسیع پخش می‌شوند و برای بیشینه‌سازی گستره خسارت طراحی شده‌اند، هرچند اثر هر گلوله‌ به‌صورت فردی را کاهش می‌دهند. ایران در حملات قبلی علیه اسرائیل از مهمات خوشه‌ای استفاده کرده است که عمدتاً برای جبران کمبود دقت در حملات موشکی بالستیک ایران انجام شده است.
اظهارات اکرمی‌نیا همچنین در پی اعلام ۲۱ سپتامبر دبیر شورای عالی امنیت ملی ایران، سپهبد محسن رضایی، مبنی بر اینکه ایران اخیراً یک موشک جدید با کلاهک مهمات خوشه‌ای را در حمله‌ای به ناو یو‌اس‌اس جورج واشینگتن آزموده و این سلاح در نزدیکی ناو هواپیمابر اصابت کرده است، مطرح شده است. گلوله‌های خوشه‌ای تقریباً به‌یقین نمی‌توانند یک ابرناو را غرق کنند، اما می‌توانند عرشه را آسیب بزنند و به این ترتیب عملیات پروازی را تا حدی و برای مدتی مختل کنند. رضایی احتمالاً به حمله ایران به ناو هواپیمابر آمریکا در ۹ سپتامبر اشاره می‌کرد. رسانه‌های ایرانی در آن زمان گزارش دادند که ایران از موشک بالستیک میان‌برد قاسم بصیر استفاده کرد که برد ۱,۲۰۰ کیلومتری دارد و کلاهک بازگشت قابل‌مانور آن برای گریز از پدافند هوایی طراحی شده است. اشخاص مطلع، 3 حمله موشکی بالستیک ایران به کشتی‌های جنگی نیروی دریایی آمریکا در اوایل سپتامبر را در گفتگو با وال‌استریت ژورنال در ۹ سپتامبر «خیلی نزدیک‌تر از حد انتظار» توصیف کردند.
ایران ممکن است این اصلاحات موشکی را بر حملات موشکی خود به کشتیرانی در تنگه هرمز اعمال کند. ایران از ۲۹ سپتامبر حملات تقریباً روزانه‌ای به کشتی‌های در حال عبور از تنگه انجام داده است. یک مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایران توان خود را برای هدف‌گیری کشتی‌ها بهبود داده و خطر برای کشتیرانی در تنگه را در هفته‌های اخیر افزایش داده است. ایران ممکن است از شرکای خود برای بهبود قابلیت‌های هدف‌گیری خود پشتیبانی دریافت کند، چراکه به‌گزارش‌ها روسیه اطلاعات هدف‌گیری ارائه کرده و جمهوری خلق چین تصاویر ماهواره‌ای به ایران داده است که احتمالاً به هدف‌گیری ایران در طول این درگیری کمک کرده است.
ایران به احتمال زیاد با اولویت‌دادن به بهبود قابلیت‌های موشکی خود، در پی افزایش توان بازدارندگی خود در برابر حملات هوایی آمریکا به دارایی‌های ایرانی، تحمیل هزینه به ایالات متحده و حفظ ابتکار عمل راهبردی در این درگیری است. همان مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایالات متحده کارزار خود علیه نفت‌کش‌های ایرانی را در واکنش به حملات ایران به کشتیرانی تجاری، پس از حمله ایران به پایگاه هوایی آمریکا در اردن متوقف کرده است. این مقام احتمالاً به حمله موشکی مهمات خوشه‌ای ایران به پایگاه هوایی موفق السلطی در اردن در ۹ سپتامبر اشاره می‌کند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21494" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZtSZGchb_cK94dJW7n1eUOFMWaddfFYV6Fy3yJ73Ijwjy3bbMnnrSN1p0_ql93CTiEnSpdyHz3xjJG9EAnaf97fKRTY6r13mnCmmPVUexx5hS9D3T8vX3jwmQZTX0mcfqyLV5UuqFm-NF_sVwPR3swwzNFX70nJYTkVZRCNcXwZbc-pKX4o9DFZewKKMMZauSRfr7vpFltdJt9lnCefS7SWqbVAqmZXoMJu9tZOCvU7vEnQ_DcYTeOwGVdzMWfRCXk7UnGgVEL7byBWfGb2x42rf4kjGtvC-MXpoYz2yIccL_7CuvfI03xjjOFx3_JCM300w-tybj5J5VFL8ix7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC فرق خاصی با دیروز نکرده چون قیمت عملاً همانجا است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21493" target="_blank">📅 10:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMnZQOfBB8nfjZ77entldMhA3-hKxFUxbl446s_hM2lDrzkwlnKQW0wB9NnLKbnEjKXGEVuJ7GsT24TFYRYpyvcxDlBwFm2OTrCKLWUZxZb9LKtCSL2rnbfzMBVEWG0lOh5xlPTEwGWv1-WVN7356o3soPCPQlVcpKQyJSNGtg9rbgTA4psjtrUqa-U3MM12f2heZz1D8RXJMhxtM2_fsDFhz8QH_1y48__ILgfOFfINrdJ3LA1M61lJbTd3acJiXZZeTBeJiy5mVjHFc8fXl26zPuuosRYIxYgST_FAqreBKncFayNUsqY0DUUkbDkD4ejESIgoyqy-w9y7luWulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21492" target="_blank">📅 10:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP-cFQFWPv-iF0dGg_AaeUSXlZ_reVcWeXheALO4GfFkGpyZeofMZY_ZsdNyLfshUR8TLd_36XWPeqRNI1gcelaPd8N8IFc4Xb_wKiAslKCdWJTU3zi0MT3fela7exvpLe-1iBp2_wbQDB_RXE032SfbRwYisPcqs7oi1HPwMiUoNgmd4fp_pwjfAsnM7AU6hXQ37zTA0x50lcR5WWHc4EqtDRtD7YJsFhDXzlkn26rMFxJju-CgWMc2JIv_sEfg_R_pEQnfoRwkA7WeBJZGuNJeepallQ3QSQWTRp8Hlu9qXEK2Iapeu9UJYr-4w66ypXtXTNJ1G9fn1fJt9VnrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، استفاده از اعدام با شلیک گلوله را برای مجازات نیدال حسن، که در پایگاه نظامی فورت هود در ایالت تگزاس، ۱۳ نفر را به قتل رساند، تایید کرد.
این اولین اعدام نظامی با شلیک گلوله از زمان پایان جنگ جهانی دوم خواهد بود.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21491" target="_blank">📅 10:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biIGS3C3Mw43jEpbxP3g9dBR5UsdcNH4jrJATzDk673629OzA8UIvALRwugAI6WSU27p30RBxfbU1Ds7j0c676FrGVtsTs3HF3coPAUWH6bhDkOIGEWQYELj0uxz7vom3hz71rL53pDpHzohkdIykA__5m1M3pgfxERGM8pbqlOIIWJTqIFtqVfpUGlrKT4nCsfT9B02b0tXBLTFFZ5euRs8KXFBZpuwrMkE6oTDGCTRuF2BLFma2rMAyaafHtenySG-b_9dUTZMeH-6p2LUoYOjZO7EfISHwZujgaWY_YmukilgO0vRAiLaBmbXRj1horrTBTC_zXWXh1rFb5D_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طاعونی که در روسیه از آزمایشگاههای قرمساقها نشت کرده، تا ۱۰۰ برابر کشنده تر از کروناست!</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SBoxxx/21490" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💥
«هدف بعدی اسرائیل ترکیه است»
پل کریگ رابرتز می‌گوید که پس از یک کمپین برای شیطانی‌نمایی ترکیه—مشابه آنچه علیه ایران انجام شد—آمریکا به نمایندگی از اسرائیل به ترکیه حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21489" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21488" target="_blank">📅 19:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21487" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👤
مارکو روبیو، وزیر خارجه آمریکا
:
«ما طاعون روسیه را از نزدیک زیر نظر داریم و آن را به‌دقت رصد می‌کنیم. فکر نمی‌کنم دلیلی برای نگرانی و هراس وجود داشته باشد، اما قطعاً موضوعی است که باید با دقت و تمرکز بیشتری دنبال شود.»</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21486" target="_blank">📅 18:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیویورک تایمز:
بیش از ۲۰۰ پرسنل نظامی و اطلاعاتی ایالات متحده به عربستان سعودی اعزام شده‌اند تا مستقیماً به نیروهای مسلح این پادشاهی در هدف‌گیری سایت‌های پرتاب و تأسیسات ذخیره‌سازی موشک‌هایی که توسط جنبش مقاومت انصارالله یمن اداره می‌شوند، کمک کنند.
این مأموریت مشاوره‌ای مخفی شامل تیم‌های کماندویی است که در طول مرز عربستان-یمن مستقر شده‌اند و در کنار فرماندهان ائتلاف برای کمک به جمع‌آوری اطلاعات، تداخل در حملات فرامرزی و تقویت توانایی‌های دفاعی ریاض در برابر حملات انتقامی پهپادی و موشک‌های بالستیک، همکاری می‌کنند.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21485" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کلیپی از کشتار نیروهای حوثی توسط سلفی های مورد حمایت عربستان   در ثانیه ۳۳ فردی که گزارش میداد می‌گوید باب المندب عربی است و نه فارسی ایران!</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21484" target="_blank">📅 17:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=aWGZ-tE55XArm_d5XFLIgfFyY2FPqpLU3HC0cql-u5tDJY80qkJ8PvCENq2pAdHX2XyBRWMsMo7v4rRuo4xyJrW4o2C32tNDAcjqfT6IQlZoXsJsMLiYoZ1X6rB_swrD_zPz6Aq8lc_7FIT4zRaYKF5xvW1gfTMwdu76MspifqxXAU2--CbXRJorM5ugUTRsU-UhpiqqKhf-dd0MQoWcw_bNg3Y6JjZTFjK7A_MjUbcILbfUvl_2TMkOl31QCM_ZR0SxJTM1_crJDaoLmE3kQ8BngzaGUFfK9jobaX47Nsh_7Fvmbdn5kGrMUg7ke1GlHAIgQnoEWdQjVXA9NPvSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=aWGZ-tE55XArm_d5XFLIgfFyY2FPqpLU3HC0cql-u5tDJY80qkJ8PvCENq2pAdHX2XyBRWMsMo7v4rRuo4xyJrW4o2C32tNDAcjqfT6IQlZoXsJsMLiYoZ1X6rB_swrD_zPz6Aq8lc_7FIT4zRaYKF5xvW1gfTMwdu76MspifqxXAU2--CbXRJorM5ugUTRsU-UhpiqqKhf-dd0MQoWcw_bNg3Y6JjZTFjK7A_MjUbcILbfUvl_2TMkOl31QCM_ZR0SxJTM1_crJDaoLmE3kQ8BngzaGUFfK9jobaX47Nsh_7Fvmbdn5kGrMUg7ke1GlHAIgQnoEWdQjVXA9NPvSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/21483" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— مقامات اسرائیلی پرونده‌ای علیه یک استاد ریاضیات دانشگاه که مردی در دهه ششم زندگی  و اهل پتاح‌تیکوا است به اتهام برنامه‌ریزی برای حملات گسترده علیه شهروندان عرب اسرائیل تنظیم کرده‌اند.
بر اساس دادخواست، هدف او اجبار به اخراج دائمی آن‌ها به اردن، لبنان و غزه بود.
او قصد داشت ۷۲ اسرائیلی یهودی را در ۱۲ گروه برای انجام حملات هم‌زمان جذب کند، با حمایت از عناصری در ارتش اسرائیل، از جمله حملات هوایی به مراکز جمعیتی عرب.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21482" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21481" target="_blank">📅 15:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21480" target="_blank">📅 15:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21479" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خوش چشم:
اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21478" target="_blank">📅 14:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لوئیز ایناسیو لولا دا سیلوا و فلاویو بولسونارو به دور دوم انتخابات ریاست‌جمهوری برزیل راه یافتند
با شمارش نزدیک به ۹۹ درصد از آرا، بولسونارو ۴۷.۲۸ درصد و لولا دا سیلوا ۴۴.۸۷ درصد آرا را به دست آوردند.
دور دوم (Runoff) در ۲۵ اکتبر برگزار خواهد شد. این دور به این دلیل برگزار می‌شود که هیچ‌یک از نامزدها بیش از ۵۰ درصد آرا را کسب نکرده‌اند.
لولا دا سیلوا، رئیس‌جمهور فعلی، نماینده حزب کارگران چپ‌گرا است. فلاویو بولسونارو، فرزند جیر بولسونارو، رئیس‌جمهور سابق برزیل، نماینده حزب لیبرال است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21477" target="_blank">📅 14:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اعتراضات گسترده در اسپانیا؛ خیزش علیه دولت چپ‌گرا و سیاست مهاجرتی سانچز  موج تازه اعتراضات در اسپانیا علیه دولت پدرو سانچز، نخست‌وزیر سوسیالیست این کشور، به یکی از جدی‌ترین چالش‌های سیاسی دولت او تبدیل شده است.   کانون اصلی اعتراضات، بحران مهاجرت در سئوتا،…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21476" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا  فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.  در کنار فشار بازارها، بن‌بست سیاسی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21475" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG3a38yVphcqwOYGdDhAFXk5gKaALzEl1lFUkHhYK4qLHS5EOF2Ol-yKR2-Mrcod3Z5K599b88rPHtQnJh3D0xHkwasMsbpgpHxKbIfpBafzaAPz6-LguIROca9e2lyQreMhav--gnSxWJy5Icjd5iR5q0FEANvQC1HzeRPj9HIUaOEJ7b3_XNx9ks90MiJMX7jWF2a-H3UnhcXCi7GeV0TBxgvx5k2cAnngGGEGfLARcbn2wLuBcwlh3Lj_iTmF7kbBNVl_akY9YVtlI5-R_2s_fU_a4e8pVNDerT5LdQ4kQQA_pZ-65i21J6EJjOFh75YgEq5m-u4Kla8CvtgGrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21474" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c48w5dMdG1Gb0HLhQ3u3-YUW91ijrLq7BxgetCcqjclSH8QbWCSsdZXAj0mXjL0zRIGewIRgbNjRFfWGEHKcWXg2LXc4OFrVDQMqyNRGjwjE0mIOSYDIurMJ1KM9nsMGkDqto_P0C3YZ_1d-18_YYFybNnRyOqda8xhh9qdiE1XCfJJr4vt6msrnxz_Vwd1X8pg_d1wB6gM9k_AIbITu4ah5TWdBajccCP7WiL2lWueREqZ_GC2t_LiSGjjDQWzFcfDhuBh129SpenEVCklKG0tITx45PZJvydvz2z1GQqshqknrLC9I1mBHC1cv-oG0G4BLqyZOh9f2HyKoRoQEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله  به گشت پلیس در بمپور  بر اساس گزارش‌های اولیه و به گفته منابع آگاه، یک گشت پلیس در شهرستان بمپور هدف حمله تروریستی قرار گرفته است. این منابع از شهادت یک نفر از نیروهای پلیس در این حادثه خبر داده‌اند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21473" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21472" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPBYifAloDofwfGnmYWbiUhgtD2QL7zFRRJmI2zdrCn2vkMH2JE_hhfij4VsfReLqsOf7n_h02L_fuzqv5k6aJHmuPff1IH4GwVAhhCXmH71_eV6ajMWMZLtCKf4ZIF-whlY6CuJZ-vNq12WZ5u5GTKMjZu8kctGOcdfIAWDelIZb1OORYmOI2h6UQUaHhG0eWpq21R20Vofupt9ctd86f7NMTwxGPpV0JGyJFjud59743V8KYs8cOEgSX2_c6prsPjHWfpSTXZpX1dKUsnwxkGWQkE4NV4Dmg8oCi7aJTQuRSthlxyF8Fis1Zo1k4DuWJjhKe9XRhidrtA-Aw0qdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان در سطوح پایینی قرار دارد و فضا برای رشد طلا هموار است.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21471" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia34IgkR1TOaOWqZcFzuQVg2fWfOUNJVbQCiV3iBvhW5vjgsUeFpFAdiSlnz9Y2I9Eq8CbWJ_-kjqp_WXJ6hjuuAMuGRpyEvOggTLUcEY_WDF79rOCv7re8_ohtz8nBE5wVhqaFQCkZwZj0kJXPOngdiFoFLUQUujmothppQ9wWFXZ-pKoN_ZBZ4KlPNXveXdqeBLQx_DUXd5EDHu8kT2_ZDljg8kl60cntQfPlZhtDTWyfhkRqguH3Oq-WJ3oJeLvy4U1vV7fpvCeWzbmgeDoZsQ2MqpyYOviYRohjMMNhDa5wSVMQpL9HJa4Bkq87KdvWWbU2RzjnFzOY_HHuIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21470" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر اقتصاد:   تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21469" target="_blank">📅 10:12 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
