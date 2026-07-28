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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 144K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 21:37:21</div>
<hr>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3VJf2AHOds4t5Y6OqXwn8igGQQjXeC5ulU6ftmOAR7t6pi-tyUEYTf_DqzsjpHhOfVa61WxPM_p_g9-rguNjNqrhlDniKpNL-VA4baS3NUkPuD01P6xKwZ2YoR2yvxrGahVwHmRjvSU9yyZe4KHVljKxkleKR60vRz0Ov3b4TDHV160jq-tfZph4lV7CDTzYxEJ5yQShj6_NGv2RXuPXnbe-qfsi-OH3eUGykmbpVRodx27RKal97SBe-DhgXnEge6iDu1QamrVWy3luXVyPTY8T60_qtN-BkB482o5Ic-nKYaPKleb4BAnvHP4ieVBK88jf6DIBzOCBMs92rQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1NRc_RjsXBMseCDrrznSjALBWXozTYvD9dsKPHMQUgAQqK8tLvE2l9nqijdKnHWajGHuSZDAmxLFvu0MUYO46UfMzPMqfwtnX-OF-BbP48ud5qCGpC5v8nnxNV1PY6zwnNcyxch8Nx-ao93ICKONA_iX9tYa6VINHc1SM5LVJSu5DY4gyLa1Om39tfkSHRNJq2MjwKTBly06kahkTOs5CltQwnvNAOc-LiplDsjwG9u6vh5hrMdzMJPt_pdRMpY9FtP-4Zo8AZTbSqWUXs69461c9I5-6pWIyAZf8-q1gmZwxgBwvCmhs3x0DnQrAsjJ0iULsgvOiN2EKmIBoHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFoNV80J59si8gH975sWja7wnBr6HdwRB62NoyPe7BHd41oVW-QgUhdAqxhZj-wMkGO7ipw0nLFDjZSLwmIUZgXX19D4euO7LhQm4f89lA61h_lp7gOZXLgSGDrRyV7vv4l8JwEK0mchC0Wnau9M0yH_aMbB0QR1v-cNyHyl541udJVt-vrLgGGW-HckQ-5d94jloK_QUyzimvC8JmkcItXEzi7ABnMuwe4cgkgqCfKJH-5doeGZ0Y0GzrftCJDEnDQSALmbQu8sgRNbyrp8__KHMhHHgPyhouP3WqGlY_KrrugvlwvvNVIbtlewNOfIXPHoHHRtTEgwzrMbKMAnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_vpNPdi1bar7Cp9v29IZsx5RAV5K9_3LO7hijc7PXuqaftRfccDZCS2ZTZiJhOJGrM1A9nRpbJ3fIrSMHzagXu8dt1JHnUb9FhGm-i-pN037xsRnUvA5T6kkRCbqBrXV5WAkGiN8N32P7JL86SOCdJZg8Sz_Ai59nYjzLcG1yUg2ZxsP_a-rpJ9eOwk_Nwe-86R_yZN9CS_tkih51jZ94QgOk9qaLvhGfU0eUnV2QZKPP1ykx3OSQY-q9-nNZ8NpsVAl8s2JPmmMUwVrJyliIkjFScpdn9vrcTnhHF1yxMp6GVzeGpIoVy8jbHpYR1yXL_U6j7wqa7_sXQ5nFNoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5CNlrwVWJWkb-7uhQcbASBHQ3TLpJVpKThZKxyEgm0C5o1arqBT6vA0BwG0MSvbz3mlDU8nIWvKgRPO1u44De7Rvp5nCJc6NPP5yuejFtiDDTezPW8klrzXhOGsrfborG4iFHOqOs_Lu5fCQw1vfd1j8P8wzGCEMIY_YWBiajzYt-93NelY6YiMNBKL6bWRkvTZLpFrPVDuTr2kD0qWBAAlAajxQC3WEYTZXEY4Q9VSih55aBTfEVQuFknsRx2IXQH2BTXT5g11ry8uxKShgI1d6LOcy8IBIiqLq0pSd9R5Ppk_ydcCzpRSh2uX6gkySdxccazQCNVjSXgk37r9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXAkiY75luyi5wJMK5BHo2Kjwt2EtZRsvBmQtKWwSONFV07v1kXA-l_cF7XKjxHtdve_8rALHV53u0YVqzFV1m1ErggGEJYpuKPKXI2zwyUTL_XhGpIRpvFgtSjNCQoSWjZaMmdRhHsRSP9Ivt4e7NOuHNyN4jv6qTxpSGfcvybyOGkbIVg0LyuKiypNkbSFHAI1zgPB6UAGDaJTV_ltEXBbT2zp1Fqp93283y5aEWwWB8nrhp1X29MvQ8yziXimdYlekxOnnZtqRMBOKbP180Sh3PWu_HcV_lyAi5kRUDuWZEgbFBQmKrXEo45LR6S-1_8OOdT413OYKK_3UtU2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG5IqvMM2cHc4AVjR5ot2hfbSteYgrHZsOE80pMshCKiqcpxz2587sN6TSkswhQ2e0jGhTITgaNxymd2BuGVzyhLgxqLWHlY2JhWSsCFAnK2gdoyR4RyoIs1jD-3H4pArntdO-_0-ck89DXKjUFk90E6KbwMy9d8C0qwroeIWp8ONawPWe0mgYZ_Soe4AJ88KAf2BhvNqkSWQgZomjXS_Ky4Gvjidus_2C6RSW0VSILrC2BA934jW34Z9UCqxFPnuefbWxl1TepCJ6IykDwPoSS0E-dC6hOKHRe7h89gbhZwb0H_vAFMcJFA_5n-sBnk7CERAN3FnKqhHf2-KI3iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NokYCFgi3cZfUO9EJ-vUh6XiSurSBIVnmvCqjTUInouHcQXswzwMp3THw35X0NlcDXhOlXt48genrQxWoWcTrBNAogX_Y4whI6IQB3xTox8OBZUishnVf84T6ZcWdDI5Xf2btXqZmoPOcoGKswpVHrEVC0-WMMhj_1CjcK16wTRDTWpcey4W7SExv3TYrFVptpjEJigo2icYtuxJndTZ0z0VRB_pAOFsB_mHcEela5GhM0wmKJwDJrBkY3ws1nSjY4Gm6EUGJSzHdV5XsrzkeVKWfw46WbzRE4mqqyOlIQO2MbHvuS4jCY6IPn9K9DkmSusyLPqWzoFXP8szBa8ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGAECeL2tBt-oLCGYrrvaTKpWfPdb2gn1pYVSzbhFKXWhk9p2blQ8keDDGNwTAHNqFLz1PUyj5FpEYL2lFLj-ru1L69wMJbxWx-xY7bXUmwIoSHUHGMBr2_cTusPEXYuO1gZBBbsP2x8rseDP-OyUGfFFCzIHMANgfRpHNL2CQO0qGGyJtabfL-8IletdLyS0TbLBbRYB37oOIiAJ0bzs22rj2og77VZI0IXTZNlWEFQ51DvnHJcnW8_fZBNrRUlezxaK6hyb5zqkhXGTA2vPlBFhR-96VCciSFoO5DKpY51EW-95OalcORFL2vS6BFJBKELawgJ9SST6HjTVmhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phX78U6n2bxjwRoDbD6iqE2mgLc-ZCvaVfvraJFCdjcgwZ1T8obkcDqLq9N4Bxkre9FgPPjYaXSA3paFXoU-6OPu0CzbIsG2WqI4YZkQvwupz5EZ_jZ-WmDfAbdeGex0cpmhqW0HueBTEfhKj8OYOWk-lbfZP3VXN58s_k7whhWKCcIeg3k9mTKirUm0oppr2w64SRVHbXXbmHXkODQzE5c8tuG3JPJCOmaOjEqbNYcJNtmfyS71mWXgZLcnR0HtYmdqJTHlOh_cY_Y2lijbiitCos6vfkfS9WxCc-VAgpM-ki4dvEGQhlR64Zhymc1hMUYZSZ4k-44HrcN52hzoiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_lmp0HDP3X7lmOuMIKxNuQRGuvjzMyYe12Np6Qu6HmJROxNPhP-kG2uHrhyBN6oEkPiIAH4rfTE3X9XRZFmCPRASsUncKybG1MeteEm60XZzJ-qds4TcEXPxOcc9ab5miGLklAtan6wm2_tC1pL6VrfgKK1zwhOt16GVMAPd-crQWClHc_Zc2wHtMWMUHinAgsU16AEhLh08pN7SllYXck9n-vzGDyVAyp4GrWlMXOU_0BBZ3C1WoTCEESxn_C7TlZS2h9BWwKm9SKW4a2PivBacaAa_UNQzjdcqb_Iv8XbdBpzdY4rDPXlZMxLrERJVmJBXw6v2wBxxN6SSJOkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e42QB_shB_-LWoQqHcnaJOj3BDt_swirSX1dqtpnLdavAe69nIAmXeihDuuZZXtH7pnz2VUDUgAyfM8022UtGjg9HvqUbcN7ZF50eWYNzxqcmvYRJp_S9J6WSgDd-ex29ypp6e_eyKZWQJno9e3zHDb7mF4vMvugLs9bBqWmTJrxiA_ksdaJH0ob25X1F6X7taR2QDEIcx6WIadFEfrZcPOBFxn8-OBZzL3675aGMUdvcMD8VtdOkAeSAWtfAalZzMeigXwAslcGXB1SOlH-9sWVAl5Q-5-ZO92zLZ452EZsfi9jNrh8ECyiCnj2ZkphiFAqmucK528gaxYEKdufEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=G6kJchGQLLymU3oydRRbywBUasz6k1sp8BcXMw3P7S2O2tGE5cRvUYoe8OH5huKffGVFI0HZb-7MHn-7y_JpJAEW5hsprrSOy1E7X8vkWX5h7iODCOqibAKQCRn8HvX1lQs7YUvZR7P5QBNscyXwWa_aXO6elIw3Hd0Qq1QyKYUGuAXqKE5OraZhyi6JoiEAA-idZCMK7PHkSy7CPiFhuIAk11K7iVc08BePHGpApCi51rSbWVbaw64Xwqu24pj0c3e3g2pYR-iWyHGn_RdTlK_IkgcO3xcUfyEzf_mzYNTZkV7HTdFjHJi1eOi8PlXuxOL8cPWZrKNo6_X5TATnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=G6kJchGQLLymU3oydRRbywBUasz6k1sp8BcXMw3P7S2O2tGE5cRvUYoe8OH5huKffGVFI0HZb-7MHn-7y_JpJAEW5hsprrSOy1E7X8vkWX5h7iODCOqibAKQCRn8HvX1lQs7YUvZR7P5QBNscyXwWa_aXO6elIw3Hd0Qq1QyKYUGuAXqKE5OraZhyi6JoiEAA-idZCMK7PHkSy7CPiFhuIAk11K7iVc08BePHGpApCi51rSbWVbaw64Xwqu24pj0c3e3g2pYR-iWyHGn_RdTlK_IkgcO3xcUfyEzf_mzYNTZkV7HTdFjHJi1eOi8PlXuxOL8cPWZrKNo6_X5TATnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP5TU5bKWfej-pn08orWdChtYArDrZWGNL0gYOZpVIoEmn4tGJdMtxaxBZeDJS9lix_d7DFwEu7zuNNiU4nW5R_29_gdPd0DFzzPNE42e7ZKFCiBU8FMJcABmEdhgrMi3lIJW7N2rkjAvMhflYaOfDRVbojb2MX0xK6DnGuaU_SpfEJME66uY2CDBR5uzGvu3t4VyNrZeTFA8Tmb5YfQfCVsslyLg0dwlyPY7qmLKKE85YI0NQI9M5yLeXbadCvvqbIE1LV1blkNta3d149u13tt54y7-n9qSfVARfhOYIhdkfaCBRrER06fVw_MvdpXXiT6Q0ZZG5DggMnQImg07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=r_uR8OybMicfgLtd88RBq4O-njs4yeGnRM6Mi0pntyDJpmJr5hQ8BYtmHgLL5L-3zym0VpkbVFp5fddLobkLDrc7dP6C9bKj8uoVjxhSLEq0Z4Ux1AXRvBTMifrD3Ley5ikS6iNCpWG4RxhVCut4AEHUoIf8fNuX5-P9kc1dqVbFrVqXBnmfVvSFRdw-Dydd8meI4ECu7j63w9ea-RI3rA8D5pBKlvEhDKhqNsPyUZXjB_12lrwVYl1Xz9u2oIlUfiOiW7SmR43eV9cr-SbEiTnYHHyejjr3aM4EZSR-PoyILjkp1tQzugoO67zz6wCSO9b5p0apfqeT9-ltMo73gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=uAcEDYXXlZNt6BJKD4Xz23QHXgLTKLy3ivWPgkJlT41sd_dP89qgQH7nc5oLbmF1UxryoyFO_2EkMvYe7IW4gEG4DEeHNlUywTmFRFWxzHf8JPPmPJIdPn442VFIgn-N31vBebY2GMsiPYdkdToV8BKjRuYah4YygsjZNwQu-p46cwzqDmU4KaD70BdeaquwtwRfLT-5WzZ3JhMD3Oo0g1CvgOtNurqFZpqkYErk-v9Fc25CrxecB9l7RU4Re4-XXeCc68roFNPPBSiuRAMQtF-pbj-uWhm-16SSUBEuxevAgwbliWReYZDd8KESRcBAg5GQdbaPhNkQngowaP-Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=q543NOSQMZcKlxNVkCkBNt0t_kJnAze2lA0Ot1Bhu_dKUgmjgAxsS6k7f0QISivE_IjMe68hqU7pqmiMw8UOUBIg2cPSb2UgMmRWDAIXZALVt-63jrGdHhaR6SOKE76mYruekF3VCmPUskZGHGzcYDjsR_kDGSQdrov1w73ZTLq4Ro_QfT8mcCGLJOYtd5GHsO3WiQcEjodp7cpqY0NSZYWJ30io7fcnbHYi4COYkAF1rX5f2s0O8NmijjmGWScC8jScgkf-lvLAYeVkPVrCOH0-c3qGT2gNojhyGbUCQ24MuVW9q7uf-eyIHn0eq7xTSFP4AQibGz_bFsvfh9gecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=LdDO2DIFqWXa87NJhgdKnqmeeFYmEtODOI-1syvaj9ftYXIH5ph2miVI2zAK6AMnrnrGtRcvgdcVtCEBM_tSo43FBKY0upcSWWdkt7QLlFq3-LLJRtbLU_O3lcmGsKHouSIqiNKzXNulEsYDeRiLgupWtkEom_0i4VbCwLcp20R48_kjZBLKLLa1NzkKa-kjH6EW9tkVnbhUz1h82BotyBzyHTNTdCTzElVv_40YnIOoyJ1VPaUjvspF77MyPNOQBdQ9OlwCrhnG8A8HH2x4AQj6PZxfedI2fIXDBXUaZs34HOwUpQLGWZpXJUM4MJWqxtpsBy1fE7I2LhlD604Jjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpgrscdclrRlV6IL0KWCzuOdVdmQmASYB2tU62jfyQoTg443iVoX6lLSNWa0MCigrtdstwY_C4nB5uLxEPPshf36wpVUsbXjx1hDnqiyw070he2gW0G4swqgnMgPCXqkNdGCZjvoA9m7EFoZiZ5SLzPsyOUWbcx_RJUK6TyJZjZxchuPEIrtUw3QR_j6fAasxdgQvAzclNFyQpPZNLWzMcaMFQNkFHg9U91d-DpLr6WbnAJDPzuclsIrqybCOGF4ZLlMHJ1qdSk-2iyp15xIEZYEXIZjkwcx21nOenm810v7vRk0MbglFcclprqxZpGGoK2Oi1ExncR1LPE30TU4z8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI1r9kyB-BGimgd3u_V8qbuZ6lgljMH1Hm2VNxDk6geMvqzm5mRqP5ysZTJkj7JTSwMSCFka2g_5CeC-CfLd8tvpgdUHjWQTmicfprl9Z-uN4Da05hI8dVizD0saVAQvtjKnXq3xIhxr9fog7a_gyxf7LY3oN8werZr7vgHOHIZetCjVIu8CN-4G8paotgYxf6AWBQugiiFkPhh-CXcaVJj220IuRD80FC60cxviaV5AA6bDnELvQCDqNAmeZ5KpZ0hDXWm0THaOlpbTq6awA_DgdGOPEaeVg1lNVzxECmP47h25Jr2qGwoEQ6bOmgDD2a9c_yP7ALi7zqE-olWGEOBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=kROOLPFGEUn_psGUqApgfe1w0lyOmwbjDALwEn7AZ4vQolgsyImwKYaWI08unHPoqtCz85qHANSU3gRv0ftDG-clShlkBttiKgG57p3DWP-Mk4GyLA0dze1TH0R7iZULN8cfdQ7jC-41Cr6yAyvnE1aIXDJSCv4ZLyYvvmyi3hPJkEtvyG6cARFeyqVrTqEORcnfhzue_ZymQf2rH6QmRq2iu5R6JOc_bWXh5mFT5D29NEIi55dUAEJY7OfMLWmSGTZtcsmGZSA4eLgmQUvddgiVpQRCtZ0n6H9vIIja0xnViP1HWqaXKO-eu8Vp3ZlhRRILGTAK_EJ7-WhttUm3b38hn1mVIZJ-FNE875lw49Fp1cwJpa17sB2bi8uZ1Eex1d81k-PNlhLwA3C_5ZRcZri1VIwMxCQVqdEWm1zDi8L6p5VrHdTGiHV1t6WsaKkHrUygQ4EvHxSMVCq3DEHMfHYJ0QGLPlF_8RWPPTxW-hWQPTUK6qfd_UZkkS7hyyl7C89PEyn7O4zbHjf-s8bkPgAE61Sn0HM8ja3IMPyj73vit3LIudfggmmeYbgPKqib7Bfer1RNwr4eGd12eJrZC2Sa9tonKs90i7Q7PUBrLwsEDJQV2Mh4kpTZyleBkDqIR4LCmW5a4otMy72Mms4sUKi7EVkn5WoPnXdOBj4lPBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2LJ8gRU7eN-HBxowpaRj5oNuEN_mpJrj6S33x88WoXFTCm8pWb5Ziqi39bvbUQDyv5IvtgE4nqVIyN3bw6rKreiOPDo_ErcO_PZLsOVKnWPLl0HWQ1fB28KY93uuwg4F4h34vWgP5fGfaNXM0I17IwPPP7xIsxbsKoOf8CKJr4Ptu9QHJWljZnaAFMj7G-4FqpNiwhuFnvJGzoVleU-B_8p_fmNfu2h1j0lu5vq6RoX9uWtdCACYrcF1ZsUChSAv0AOJV98zb7m47MpIaVVfIU1H7XTXeqy2zIddmO0oWlDozBRcSG4wet5ELvxHZujdqRjNocobNNgMjqNbnEQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI1b1wQl3UKNjlFIIGai6wefuKMBc5o1ZIXmWHuUU3AwyD8jvHG2_ZYOzYzWFiLgf2c5rqc3hj2VifvBD9M5t26Fej0mk9fO_ojUOIAzF4oEr-1yVdiLtg-dbMhQCptMAXhMuEBasDw08Z7UwAUwdImEPeYX5duRsYbGJ756WSgC1CkTED4v3DG_YATxP0uHI9m8MN_o3d4JX-i0u4V8RxYEIoKy3zPYyYQyPjd6LelkRh4oMwuzgxe9v-LhtCA8PKUP9dL7NYV8GLgGft0VLpLKCMbyQSzkX0cALo7Yn-li1ODyKVLv6kVziVqF553ackyx92JVx4foMSkvdXJO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ZpzFaMG-z8-aWWaI8O56NdRUR7mh88z47V_IF--_DZMi9d6QtYXtpkdHLxDVLPKjV0i3LuTWBttK8W4QEJVWRkMrZAVYig4NmUXL6fgB_U5WUqW3qtRTnh3cApk8_3r43FHjj-JJZGGCeizXbJcXTrMsEIuABfA3MJeiq48427EycwkNkbV1te0IVsfX9rwdWE2cgZGPPetvBGJZiS36MH8e5aNgdPtnYl73z73vBuGBo-uE3sZynnqpAinCUGiu0ueNNWz1ex_0TtJK0jnrvS6MyO7o2fyPshsHqly7QPVB3OI2vXCKLFhoRvGiOksB4qed3KCYdGn2hH4XgtbnUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=ZpzFaMG-z8-aWWaI8O56NdRUR7mh88z47V_IF--_DZMi9d6QtYXtpkdHLxDVLPKjV0i3LuTWBttK8W4QEJVWRkMrZAVYig4NmUXL6fgB_U5WUqW3qtRTnh3cApk8_3r43FHjj-JJZGGCeizXbJcXTrMsEIuABfA3MJeiq48427EycwkNkbV1te0IVsfX9rwdWE2cgZGPPetvBGJZiS36MH8e5aNgdPtnYl73z73vBuGBo-uE3sZynnqpAinCUGiu0ueNNWz1ex_0TtJK0jnrvS6MyO7o2fyPshsHqly7QPVB3OI2vXCKLFhoRvGiOksB4qed3KCYdGn2hH4XgtbnUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSKXfixdPdfbk5i_O0GyVU-5T7VCFSQsA6DvBBqiNGD39IecTWLgYg5ZERMMgGJdBVWTgoX87REh1SQXFOm346cVPDkbhGGW9p-8fI3AZHeCXy54ytRrSHIpkkABCM_Npn2wNAG1vqPXUY6EuRHNrtSg2fmASiPcsIZIm4zhNAFazd7P2MuoIa7iQFN75nRNxrWv5s5IBCSr5eN4NuZxFGCGThPDY1CkpJPh-kZ0QW1TukC600s0cxAE2FsIw4OTjkfi_l03TtDZQeZMCYONs-Z3TjEEPv4wFPg8t7aLFhcg1n4-bRT6egr3C24PKnKpkCfxYUyebS0dbdoMFjkvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwq1AWS12VTaiz_uaHQUU-Nk8zNEps31Kl-OP6E5suYJlflBGquvMmzwvJ4-JhZFKsnVi9IiwgbXatG7P6HRf7N8K1hd8MJM6jybae2yRmvANjAGcUJkggWUtUaoCZ-OIZGu0dLzyyb7ztcyl6TYyix6XjugkbCH9OP8qKgcPU-e3RSld1U0QP9j1SVuaMBHhq_RBKEkfCmLtLkb_44CYTgejEfQUZ11aix0r2UJrJI6ulZTQXAp1uQ9T7zp2KFjPJ77QtcICmwkDvOXO2QsX55R1EK2_v6cwtF6RfcL2vo9kJQLRuJNWjNvk1q5bmvDXfU6Z5xp5uH_kOA4hCyGfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=SLQNdL7sRwV1q-J8LEqa-r7oVstb-jTh3cET0SuDU_cbveB0MC3rrmjfEd6QtdWQbscOuHeNpbwSam-LxN06YyrqONTd14AbLYOXdu4xkjpOwTwhRBJdFztV4H87yiJ-dqp6SWKlMktSKCybh16ii9A8Pp1BErbsUbNa3rOpJdANHng13r1B4GeNhhZr-7ACc5ut4tOp4FNvA7t1HyX3deZEaKtK8ziROTqJZhzbUPa7sPG6UtX16kRBRYtvFcac8fLJ7k36WB5IQUN3aUIoH7gUZRuyi3jgVDJX_8Gq0xNRE-aFn00Onm4LLcpMWwo-Ny_8WqdL4ic4pstXFHEwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=SLQNdL7sRwV1q-J8LEqa-r7oVstb-jTh3cET0SuDU_cbveB0MC3rrmjfEd6QtdWQbscOuHeNpbwSam-LxN06YyrqONTd14AbLYOXdu4xkjpOwTwhRBJdFztV4H87yiJ-dqp6SWKlMktSKCybh16ii9A8Pp1BErbsUbNa3rOpJdANHng13r1B4GeNhhZr-7ACc5ut4tOp4FNvA7t1HyX3deZEaKtK8ziROTqJZhzbUPa7sPG6UtX16kRBRYtvFcac8fLJ7k36WB5IQUN3aUIoH7gUZRuyi3jgVDJX_8Gq0xNRE-aFn00Onm4LLcpMWwo-Ny_8WqdL4ic4pstXFHEwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g67oPA0tcC3Jg6OsmNxY6mM3h7lPi5vAvYSJVDRknfpIV015JTD2g0pv2ekJz60x0GB6WzxPdgOJkeUsrCKCyxjz8wX38mKp6MqiVzJoCbwJz_jPlj9ac-zqr0dvtnpk3wcxbdEyJW6CbTOO81y6dO3SVfewZdsdcjb2V3N3lTmq45dCLU6_g5p-3l3HzmoAfV9T9wOBYTAiVBTb8kALsmYp6Cd-KMuS4PpHCAqc3p522XwIXQELmGyUP0A30XGWax6bJTBoYOuK3pDw5KxjkhvSnvaAb5-Ekm-vlaZW2LHvYPDfy7p8VkU9AHElWgLO5_k4_4PTBGfSh23GB9sZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=HKC9WnQ1JHLw3r7OD7Y6-7mTES8KBqUT-xrGFFyGHlf6ba16JZMx0lbgGaqQe1pS4qedqOLhL-oBBDLBNhtX1Du2CzetU_fnNOFWfdrDn38KP0Dw_EUXG81Y4a_TQWLNTrMkfPzuoESaOOOz4xvX31VooW2muZ19RAsOrRs2u4mT9_7DLEJnmSGuI5M6mfQj7l-WI_NTNsdgzMAxBIQVPR6ubzQI46pdDU_twhWl0Llgd-ncSNb_UqVvRnXyue23NgAxRZyOOIAbtKRO9FYeBFI8aUc8CgQTRgS9lz8-yFHDvcgBfdzRT7QqEqsOZYk2T2RNd14l2i-EH6UhtseHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDsOUi49uqkvvdItTp168P5_y3a3S0H7as3w9wvU6myyzo0AC6kykK3sqNFM_dZ4R9OdvVVXyiwQpwaGaC7B8Fd72mkssKtRe9tXM2cmwGmde8KZXnYHkTAwVdgyOUc9e08UK_zY8FuhIVE_6YXsJNDbeKQlfKptp0CkCb7RZj9sxymg-aZkttmMukwBO2cYy1i-Thilm5_XsqJd9QCGYP3zEQ04nsKukgDOBdy24qi1kn-LoroxEItPT6MbmNuWRigX8tce_Db2uE7bfnjlY7gMU57iFCBhw0COJVsFGRamPK5G43qkIPE0JwPBxCHlPihm92B5rzdKmnIXhDCBBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=T1D6Gfm9iF57sN4lmEryRod8NZiRSg9luxWIGoBe1OJy_chSGp6QN1zE5joxX_mdVTUJLdsYTLMivJDIo4K6hZwNe01gphMZS0VV4SE5vLJ3FTYU5Pg_HtmeIYYZ-lNeMaX3izeSp0qEcq7d30pgwm2srCyhgoL_mDJdOFxRT_rClHeJKCyhNIg8Ww2vwtZRfcnhwnENjCxX9GuLR2GPkgI6M8uTGi1coZ2dKu45dppB_kLmCACSOHM6hhZsIq3j4W1AjQqRVMMeafMTHfueJ_gYjpLD_Rk8oYJtgXx8R1vgpxFnukbgE1Up-7kO9aI63BT_9FyAdq_EOK8de6ocBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=T1D6Gfm9iF57sN4lmEryRod8NZiRSg9luxWIGoBe1OJy_chSGp6QN1zE5joxX_mdVTUJLdsYTLMivJDIo4K6hZwNe01gphMZS0VV4SE5vLJ3FTYU5Pg_HtmeIYYZ-lNeMaX3izeSp0qEcq7d30pgwm2srCyhgoL_mDJdOFxRT_rClHeJKCyhNIg8Ww2vwtZRfcnhwnENjCxX9GuLR2GPkgI6M8uTGi1coZ2dKu45dppB_kLmCACSOHM6hhZsIq3j4W1AjQqRVMMeafMTHfueJ_gYjpLD_Rk8oYJtgXx8R1vgpxFnukbgE1Up-7kO9aI63BT_9FyAdq_EOK8de6ocBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=D3mEu02wim_6apEOLSoYMhhVdg-l_K7K3NgqX1ccJmCVJ6bJRuDW53MP2jJDl-3yOo9w-9HxwScdvmMNB20GmSpeXtL7GMNS373B4FZy9dymKb8J-ZLTmcZyQPb9rEwTxsuS-7I78xDNq0sJtFKAyeyz-KIzDaEObvNVwHONcP8CkAv9_rZUuPZ5C_lgyB_UlaFqWtHRqbNS_kFXVFCihZ0_xs3stX00JizajX4AB4sxwuX4hBeoUvTyiiXY8uybLNtHSFT2EMQtnJ0PJhUFU1UAA3WipyCgZjQuenJtfBGI0slHlvDekNGWuipsjPu6TNB_5IwQ9cJH6oacR6YQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=D3mEu02wim_6apEOLSoYMhhVdg-l_K7K3NgqX1ccJmCVJ6bJRuDW53MP2jJDl-3yOo9w-9HxwScdvmMNB20GmSpeXtL7GMNS373B4FZy9dymKb8J-ZLTmcZyQPb9rEwTxsuS-7I78xDNq0sJtFKAyeyz-KIzDaEObvNVwHONcP8CkAv9_rZUuPZ5C_lgyB_UlaFqWtHRqbNS_kFXVFCihZ0_xs3stX00JizajX4AB4sxwuX4hBeoUvTyiiXY8uybLNtHSFT2EMQtnJ0PJhUFU1UAA3WipyCgZjQuenJtfBGI0slHlvDekNGWuipsjPu6TNB_5IwQ9cJH6oacR6YQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUcgIYzO_jf0vA_MhN1oOIggD922ZxKOe4rdIaTtGXUDmVpk68ispyO1x6jCMvruoXq8DsCuLfa1I97GdMbASc3W1V6FycVAHJQP_vrrLkTeCcU_6Jcd1r2MnjE5-_MdY25p11m0Wy3M9p_TB_rNFHAZzCfT_EhMMXiH-rwct7eazj4mCARjxY0S3W40Y-hza1JZQZvoclZ352nKYXhZ57ASxxaGU1-iWEafpp8-HcqjLfwMHyKuS2Vp8DpZMUXMxd6w9tP1wMlmxgH8ufwryGpqGwRwNBN838E9TFu9_4Ipz00-T4VQYHDLEDFb-0mAB6urTKDdPbdRUWqL-XTB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPZYThiN_ebumfLUEl9DN428z35Y6SCkeUaJz5DQuSF4un4ezYIN86s60wbyN6WDAcVZprNhJ-PvsPzOAU6ChZNQh-hhU27BjCL_Ja2sknUGVgp5pStRKEwLc9NO2uKwfuFMJcNq0zSm0F9E8a4RNjn5ArpDyo72wzbnrlnzZ8y3PGLbkPrVtyo_3UIxTjFuV-jPQYwd9epHIpzc3Tvv2qF1KSyyKQLPai_6cgRNQrXIMoHPN4IusOvTDNWpPok9FOh1rXqc-9y6lbHx-GsOySgdEiRe92TQRqodDfr2FfLjHgrJlTZ3t8ry5MEeLdbTWwhwg1_ndzfTleIfSiexng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKSQWoKR7YPxUgaHG32rh-uxmTXXIZnSvlI5fYWypDHb9OQ2cteKC6aH-UOD02PNvB4zvt6G7Nbyj1pwciVPjJS2XkZvGk7CZSw9yaRKJexIINaI4asQB1FZI5ekm3ykqPQJJhQAyq3AX2ryYHZvTwRAgSAZk3DSdVWwerANvJbCE4cZ4JmbiZcNyL5HJs043Fkttuupb2aqL-WRPl9XlJtuU2nFER5RolnTRInft9I1wSHMXNUWD9DxjQldmhXpt5bFVucsYnolTBJyeWhKDtuVggi2VTMCeqRzEXXYxS2tUdGSvmlYPLY9214Y4hB-p0fKDo9EHfAD9M9J1lhhCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=eHPGVTZfPuiEt1pUC2-sIEG7z0JdvIeU1Rre9of2JqtHjQz-S51Aw3pkVVckvhnJ84Po_TSzDP3yVxoehvMCvZBfsby5iNRkQxwPlusW6D3f9i75yCqUNj0eFnUE-gNZJlgClzzxq9XsMcKChcjDalOz7FydCdNMd_6ycUqzCovc1l1z7-UsJdMOOIfWVkjILUFQA7_NbgyXBkEvADk8nGQ59l6kW8VTXIK6tVV1v-gJKRwubVurt8k7Spm3kHyDlOmez66wty7zj_mNwKomWu1-sJkIJkHY0HCA4wItdqvWpQWRL4WaoNxPkmDWwHTtPMw8vUSoc3CqMLr28EjtFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=eHPGVTZfPuiEt1pUC2-sIEG7z0JdvIeU1Rre9of2JqtHjQz-S51Aw3pkVVckvhnJ84Po_TSzDP3yVxoehvMCvZBfsby5iNRkQxwPlusW6D3f9i75yCqUNj0eFnUE-gNZJlgClzzxq9XsMcKChcjDalOz7FydCdNMd_6ycUqzCovc1l1z7-UsJdMOOIfWVkjILUFQA7_NbgyXBkEvADk8nGQ59l6kW8VTXIK6tVV1v-gJKRwubVurt8k7Spm3kHyDlOmez66wty7zj_mNwKomWu1-sJkIJkHY0HCA4wItdqvWpQWRL4WaoNxPkmDWwHTtPMw8vUSoc3CqMLr28EjtFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=CutEgTS7LIH4s-_dLk__e57bm23AO4FMmwD7VwcMr5-Re9W6Hj3eYgvKM2JMZ-BDGl1PkagIF4vCNMbCKMGoqiXUsBMk4CHqzPWIXSfNnnWS_ljGYmnX8pl8FcaMLDwBWB6N9JdG5pMIAwehkY7F6We-xQgzyO8CGSV-O8kd2kMN6Ip-epxcNbvIce8CSja_qQ1JozQ2IWiwBS6LIWKw9XPeC2Esf5wceJRKrqzMC6hFzT5v8NdTz-IgKtg2Dof9Bs_pzAQkaIHLOouuAnz4lxTbNiarJ9byyAZv4K-lnZVsXmDH-5m6NHB6Gn3MtmEBz-d3I-q3feb373DjfDmzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=CutEgTS7LIH4s-_dLk__e57bm23AO4FMmwD7VwcMr5-Re9W6Hj3eYgvKM2JMZ-BDGl1PkagIF4vCNMbCKMGoqiXUsBMk4CHqzPWIXSfNnnWS_ljGYmnX8pl8FcaMLDwBWB6N9JdG5pMIAwehkY7F6We-xQgzyO8CGSV-O8kd2kMN6Ip-epxcNbvIce8CSja_qQ1JozQ2IWiwBS6LIWKw9XPeC2Esf5wceJRKrqzMC6hFzT5v8NdTz-IgKtg2Dof9Bs_pzAQkaIHLOouuAnz4lxTbNiarJ9byyAZv4K-lnZVsXmDH-5m6NHB6Gn3MtmEBz-d3I-q3feb373DjfDmzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eZiCB05IiOLQKaaqF8s4JbfH81a00lcjMWS-v67Tf6zMh9dkmvnNQRzXwPSnzVwWrp0qPv-Tf1hRyf7izseHJOzZAlIIm-nUUDO80iRm0-yGgL0fqjbbX2x-00AEOVb2ulzfLGIVsTrBsPans_iXvYxvnc8S9P8rBoWdSeeH_kMZfmFFfzi3tq9VwPvYJybG4PXXvvb3NvIqJ7pcEHYiQO0Rx_9whP7fzLeipYtqZQTiOVBet3WhLcVhSeelDJguacK1x3PzTQhEehvRR1xgODNOgxOhPZK7dliU_KjtDehA2CLAbKJZZdWhAT86Rs6-IbXg1VeX56VJEQ61X_-LlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=eZiCB05IiOLQKaaqF8s4JbfH81a00lcjMWS-v67Tf6zMh9dkmvnNQRzXwPSnzVwWrp0qPv-Tf1hRyf7izseHJOzZAlIIm-nUUDO80iRm0-yGgL0fqjbbX2x-00AEOVb2ulzfLGIVsTrBsPans_iXvYxvnc8S9P8rBoWdSeeH_kMZfmFFfzi3tq9VwPvYJybG4PXXvvb3NvIqJ7pcEHYiQO0Rx_9whP7fzLeipYtqZQTiOVBet3WhLcVhSeelDJguacK1x3PzTQhEehvRR1xgODNOgxOhPZK7dliU_KjtDehA2CLAbKJZZdWhAT86Rs6-IbXg1VeX56VJEQ61X_-LlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-rXNOyd5WUeFqNPsirfNFbEOxAuZ4Ojga7lSvfalccTw11BDC2JvvZp4HHZvJEuEnaYQ8Pr9F0vSQuf3Q4fc3xeiIKTJElf6wC87Ymsd4-birL_iU1p1taLo74yz3WW-ijsr5oTzhPAjNZopGfPx0VIrsVky7K1ziLVh3yb4MzvclwGDQQ9DXMQ3-tcViuMN6Qi4w3ZCVma8nr0bQ4lBo45gQfiO5rUBWyP2E1J7EjU1-VLNb023GJqTCDuAC0RaMEZ9DN8G3q5DUag7ABKfVQe-R5tUa_gx7Pw6cIgbq-DuUOtR_m0ysRnm90zasl1Nm5aPbCqXb6zTTpJWTldZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjNs2-JiwQZ78Ihmgj-IVgnkUVf5Qpd3rVXd60yvnMypuoS9kRVk6mlRERwC1CjHnGrcQ9TkZg7HCHBvaqOMzf7djFTnpnZG6G-ciOSMxAkgEDc8hibSYmz4QBI5TFk1CjZAomgZHTw5iXCr_RKfAPF93DXvUJXQR_qp_BKntQneWrdPoFioFmuqkrfD9s-BnPgZO6NQT_VUvJB3kVZcniM5-rzY9Hud3q58rczh0WNdNicjmE3zSW6PF6P9s1vtwpV3J-pKw846JiwV2TmD1fEqO6T_YcBZFkeS3Art6K7j1gwuzt19loDyAtkU4RIcLXYmzb3L-EkF6Olimwy_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVjAlWD6Q5iuzIfCXB2Av3y9z330oDvKctCqYQWMYBg5lPLxpnIBA5el4KMPw3PwnSnWmqTIiGo1B0Pfhx01yfOk3yxFqP-yfvPLU-S1XjfziR6jh1i1uitxFeVvwSvj6nx5UzjIqaTxpLzOSlZ96BzGMtJxv1FcxWTghQ140Dv0HpuH50xeTLYqkd7y5FggZUE0sCyTMwdld3-OXR7qXAQvPb9jRkO5n5oY-L8QVYE2hbNuqArEymszofns5FiVhOfxTjchOfpEYg_WWIEI3w_Ps8yZ7Q17b0RmZEv3MjiZy2eFjXzPa2knuZlOlBf9HJAcZDbNsPJs_QmFigXguQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=TaXGRJyCM2mg9iFEODItjnTBBSX_P2iZxjUwDfuCWmqlj_lFl0tHe75T1DWFyKg3uetE0KVgxtf15NEALAQQpIPFgSC6PLrljcSJPPHLgvHpCk8b1oaVvvheITLaz7ZZD2oa_gsKGo_GBb9GExhNlxMwcdAhBOucMSfCl7F6_mnSl1Ie4wOscP6fQ2Ewf9FJ6KhFbEs0X2dnzVTlVBOYfs-LNzBl25A83ZOlyc1Xdyss9KFRPyWN9HRQaM5LKFSyQJo55U9Sr3IhnQv-ZDc1HcfkgpCsHFFHWK-CKsUz0PcvPdcHoAQRruZEO7vAtC6BSA-JkGXG3-hwXoXJhdHPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=TaXGRJyCM2mg9iFEODItjnTBBSX_P2iZxjUwDfuCWmqlj_lFl0tHe75T1DWFyKg3uetE0KVgxtf15NEALAQQpIPFgSC6PLrljcSJPPHLgvHpCk8b1oaVvvheITLaz7ZZD2oa_gsKGo_GBb9GExhNlxMwcdAhBOucMSfCl7F6_mnSl1Ie4wOscP6fQ2Ewf9FJ6KhFbEs0X2dnzVTlVBOYfs-LNzBl25A83ZOlyc1Xdyss9KFRPyWN9HRQaM5LKFSyQJo55U9Sr3IhnQv-ZDc1HcfkgpCsHFFHWK-CKsUz0PcvPdcHoAQRruZEO7vAtC6BSA-JkGXG3-hwXoXJhdHPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvr4ZC8nPJ4MLbkIJJ4O5_DgZirKBxGE_5D5Ch4p3aGev0v453rkeXy6mHtj8StO6PX8LXWpwJ2PA6zdLN0_WvKXrzH8qW6fXQsQ-lmAHW0Jxfr8c4PhM6uNOQ0rCd8f0nMsn9oEi-_xYgzZ3-o053d3CqBDSGvH95LwI_DHAcOW-vb_NDL1ApQ2UcvVPRAWZR8kofa3-LYiqsiJ6YkAX50UBMEfL4AhtddZC6HCDq0fBbFmB0ukihfAGST2y-VbMFgmbI9DXCWxqMyLXCg1n6tGyPzBwmCa_ItD3uaZ1S8DvnwFrSY9rhhHqcHq2wNLFjpak1d_GUeOZilWN2Lrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=PYgzD2SA7zlgW-UtPuxe4uRvUiGoaLW3Cd-ln7-eOfokWO8lrQq4o8kpwJO56XK94o2ocf2SK61ITEM8SiI34D1dBuA5_TwzNVeLR1jNMhcCgpl-Bj03hzOOZQTtC-09CTEbNqyGLC5UYIEuzzukGTHIVs4uFJPEsQ2JBngZ1Dk_Cu5yDfB91IJ2UC1gy4aZaoYm_V2q1r-6lsD_VTz0c7-MQrBELFdFKG_pwTrYDhm3hYZCtn4p7nX9fdRj8Y7Ii8fNNQyXOYE1Mcl_l8rVj9ilw50dxWVkhBTCjaXNUXI4obWwGp3CzDut2_tWg3V3Gig-X-RxjnAEYT-rc7zYIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=PYgzD2SA7zlgW-UtPuxe4uRvUiGoaLW3Cd-ln7-eOfokWO8lrQq4o8kpwJO56XK94o2ocf2SK61ITEM8SiI34D1dBuA5_TwzNVeLR1jNMhcCgpl-Bj03hzOOZQTtC-09CTEbNqyGLC5UYIEuzzukGTHIVs4uFJPEsQ2JBngZ1Dk_Cu5yDfB91IJ2UC1gy4aZaoYm_V2q1r-6lsD_VTz0c7-MQrBELFdFKG_pwTrYDhm3hYZCtn4p7nX9fdRj8Y7Ii8fNNQyXOYE1Mcl_l8rVj9ilw50dxWVkhBTCjaXNUXI4obWwGp3CzDut2_tWg3V3Gig-X-RxjnAEYT-rc7zYIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UldJZyTtPJBmnEwss7aJQiUn_LEfehfStrZAu70XaveLC2H-T5MfXjB7RwUF8VABdZghje2X4DAx585Pp_BqVQ4doZKcf5FMP6Bdwld7KUmUvTbjCvUQVwQgpJeQYy2c0s0_58aZ9kjAAgfmSuI4RNQAupZvakCEj3KUSjDgCyFWzS8AHWb1bSWIPk0lzYtMRbn7bMtkvKKXH14h24d-eXOifEuzWwbiD5kdTRNnHh6GqvLMDVOSAeINKWbt_rbrYeH4huiOIxH2hiroeWIhJGGEz2OZMvTyb1HOxex_-WVfnBFmzyXkbF_KX2KX8bQdqS_3K3I--RLQzm2O7cPVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=tIOcI8-utx9U0pxRtol6yeF65PGAnqbt7IQRJa4bEB_S_z7t_j9VnB_X0iFdIW8ghx_r2AIz96ysYxFn_imRE4yWbq-D25l6ZWsWVIsaY7ZqTtBn3hA5R4Fdt1OjzG9YnoSfocYOMM6W7F6FML6kN0tLTU0AwW3Qfg6VeodPPilAPW_TVXuhv0_r6gjWOHRpmTohCnya0Pu0fR3amoxO3Y8c80ecaYIXNuGas3ON6Vw2-GemLBXWWLWW56V-KRg3AZzXxlbPID14J7PQ18yIzWM1u9qtok4mBcJbTP-bYrbTiXNQ7cx9-KOmQqUu7bqgHhcvI6_4f_m6Gb7etYAjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=tIOcI8-utx9U0pxRtol6yeF65PGAnqbt7IQRJa4bEB_S_z7t_j9VnB_X0iFdIW8ghx_r2AIz96ysYxFn_imRE4yWbq-D25l6ZWsWVIsaY7ZqTtBn3hA5R4Fdt1OjzG9YnoSfocYOMM6W7F6FML6kN0tLTU0AwW3Qfg6VeodPPilAPW_TVXuhv0_r6gjWOHRpmTohCnya0Pu0fR3amoxO3Y8c80ecaYIXNuGas3ON6Vw2-GemLBXWWLWW56V-KRg3AZzXxlbPID14J7PQ18yIzWM1u9qtok4mBcJbTP-bYrbTiXNQ7cx9-KOmQqUu7bqgHhcvI6_4f_m6Gb7etYAjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7ZesMxUqep9py889G4ewUOiP5ZWF5mrRyw98D_M2vdrhw0oplzXhV-vacNw6EpY-EdErY0qTSxam7XI4q0pbwNUw75ivq_zDBmHlXdPDj5JdOfmPmiWX3gxUPblrS_vSO9Orb6Q5xRznV3fdvgMU4AayIhKcrWs4L3JoH2UaELiLMDCZYnzy3T7qa3_c6iGGEP4QyXfg9jufc-zMRrXVtkBwU0JUJ0azNWYNxiuTtW8eueARM2lokOmw8WshTz2HUju3rIcpRXcdBYFQFfSOWQ539UIC_v91reba9PZDhzdGMOi3xeMAVP5-zsTbJP7-HxzYdxQRr5kOKAlUvzaXEak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7ZesMxUqep9py889G4ewUOiP5ZWF5mrRyw98D_M2vdrhw0oplzXhV-vacNw6EpY-EdErY0qTSxam7XI4q0pbwNUw75ivq_zDBmHlXdPDj5JdOfmPmiWX3gxUPblrS_vSO9Orb6Q5xRznV3fdvgMU4AayIhKcrWs4L3JoH2UaELiLMDCZYnzy3T7qa3_c6iGGEP4QyXfg9jufc-zMRrXVtkBwU0JUJ0azNWYNxiuTtW8eueARM2lokOmw8WshTz2HUju3rIcpRXcdBYFQFfSOWQ539UIC_v91reba9PZDhzdGMOi3xeMAVP5-zsTbJP7-HxzYdxQRr5kOKAlUvzaXEak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Vj4z6K1psnp6m5Xr6VWz38vX7Q9NY3GGW6WK9AvlImlcKVcFLx0Da_Jzm0-C2FovsLvP33U4PX35ZGMfKfifg6GYWJ4W-CkLlcHexxlXsDo4jj_4wEoTphfW3kiqx2T1s_0dqkfXm7eFGFMIYeG92oegEBnfxQx-K0MhpF2fYJuAk218WxztxS7UlgDtwFD4HQVlOcT_EVPi9D25hl6IYafQrN1BwLD4OSeHEMi8BwXmzgjK8dOWKcAie9PWZafnioZ2It2eVOqokoopcvdxBEJRVBEGGg7xJppjccrlGqZnWaNMJDsuwjXg3rPTmqxJSjdh9GmsNukr2frY1IUtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Vj4z6K1psnp6m5Xr6VWz38vX7Q9NY3GGW6WK9AvlImlcKVcFLx0Da_Jzm0-C2FovsLvP33U4PX35ZGMfKfifg6GYWJ4W-CkLlcHexxlXsDo4jj_4wEoTphfW3kiqx2T1s_0dqkfXm7eFGFMIYeG92oegEBnfxQx-K0MhpF2fYJuAk218WxztxS7UlgDtwFD4HQVlOcT_EVPi9D25hl6IYafQrN1BwLD4OSeHEMi8BwXmzgjK8dOWKcAie9PWZafnioZ2It2eVOqokoopcvdxBEJRVBEGGg7xJppjccrlGqZnWaNMJDsuwjXg3rPTmqxJSjdh9GmsNukr2frY1IUtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=R8hWrdJpVFPwr4GVqMoOlgcsI50yGApQfkGb6W8jAqX-a5T-ygsDqHFn1M_FOczYX2QmnZTrLdZ2Wpr3jeisxxuiRwbveQk-Hd0rJ2SQrXUNSWpbU5aL7qKnXD2miaK7Vaur5J1WTHTuDWFHNfTo-nPNTvMQFsxVNWdBYf0YnUNrnOm5AaIk1YGxP2nduoYdwFPm1sLRy_UAq2CC-TZMRtlTnhVvWJcW8oz7p5U2XXxqowblzkQW-amOS_Ff4VLrSP-eyIDfGhY_XQtObjht-Z6sdMBft9o3JT5ZU_EKM1jdkhOaDFh3zfF2VNG017rcIrIDZ_YTxsLHf65d0RTDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=R8hWrdJpVFPwr4GVqMoOlgcsI50yGApQfkGb6W8jAqX-a5T-ygsDqHFn1M_FOczYX2QmnZTrLdZ2Wpr3jeisxxuiRwbveQk-Hd0rJ2SQrXUNSWpbU5aL7qKnXD2miaK7Vaur5J1WTHTuDWFHNfTo-nPNTvMQFsxVNWdBYf0YnUNrnOm5AaIk1YGxP2nduoYdwFPm1sLRy_UAq2CC-TZMRtlTnhVvWJcW8oz7p5U2XXxqowblzkQW-amOS_Ff4VLrSP-eyIDfGhY_XQtObjht-Z6sdMBft9o3JT5ZU_EKM1jdkhOaDFh3zfF2VNG017rcIrIDZ_YTxsLHf65d0RTDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVxnCnBQsy1hjoOe97rTf2lxYGQtCaSDFkYWgBhHbrF4sQykIVtosOdjlgbqBrfTYT4ioreKtrYvsnDG7gosNLrdDeCsJ-EfVwWn7VaNhOgXU0YB_JqVG4GL16mwdJl7YRFNyRnWBXPxOgwvWllunNGtDFdB6lWC7NmZRxzeLrU8n340fQni5TVSOe4236ldeJbS47DVMOG0fr8DoK0bgL57RKlAdv2pDrKXU0Uf5tUsnOwqGnb6BhhuZi96opVBTWnniEji--sHD871--cigdJikGBOh4n2RJVqulEZDjFG3MOXPXlq-0kIh67EsQiFk7nA1PnhCoKaf43ZJgXdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=klnJBTh44B3N1S3fa8uxXpK8vtwGcuZYOtipAF2U3cdUvQfdJGz1AxzpcOhjECXKe-Hia9tH9_yMICrw39-dfTjQNp7rjFin0iUhppi4yLPKFAZlhfZ2zC_iY3SxTExZBybYSp3lspGKpCCGfeOp5fRUUWngct09Nm16p2uNC1-MF9VH84AqaGdyDI5d-yj1YLmvvamjGNxEFToqxdbFXgY4gCSkrnB6d_xN82LiAvu-4nD-UCu8EbxS_kajxOyO661dFjJhqJaFDxj1pIOFDvMnTKyaHX9YgLaUbdYnIPtT7MhjsgpJO5jvNvAO0NNdXc2tHEzusOozFFnXdnBRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=klnJBTh44B3N1S3fa8uxXpK8vtwGcuZYOtipAF2U3cdUvQfdJGz1AxzpcOhjECXKe-Hia9tH9_yMICrw39-dfTjQNp7rjFin0iUhppi4yLPKFAZlhfZ2zC_iY3SxTExZBybYSp3lspGKpCCGfeOp5fRUUWngct09Nm16p2uNC1-MF9VH84AqaGdyDI5d-yj1YLmvvamjGNxEFToqxdbFXgY4gCSkrnB6d_xN82LiAvu-4nD-UCu8EbxS_kajxOyO661dFjJhqJaFDxj1pIOFDvMnTKyaHX9YgLaUbdYnIPtT7MhjsgpJO5jvNvAO0NNdXc2tHEzusOozFFnXdnBRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=RE-pPKFdzuiNGaB3J0dyp3FV5CKlvRnH6RkDmf91CVNsa1g31f67Yk6Q7T-zfrQmRQQMq74tPeuxEy2GMMqRmAskqcbGeyatgl4pAaQGE9Ccqk2In53ca_KfE8aG_4OLSOWb07pbwzNDmxiI5PEpk9G9nJ14ARPQ6dH349N518wM8Cn7Mh4qiHlY1nYcUMuWc0cKyw_04vn_5oIlOcEu1YAxrWDYYnsjV1zZqNppCML7cm9uJZ0Kl8VTqcTU-iFESsRbM4ZHzvzeGIQcyyn-cYsOMTaIAS5fBMBHioOuSSniEqeJlAqESazQkBzXTgkwyCXYvb3qVc_FQELSVCdIhTNk27WG90Di9AuwXH-pUjZyUC-sf_PgzFYC7eDl4WgChJ0qmpdhHPrPbyP1rODH607LIA_CawwxuoRUS6gMRFt8kIVjiqU-wCOdKT-ZY0CwVisqhkT8OQwpz5aQE1YjBzu9VdMCXKjcvACx8XefesrFsimFgIVnmD2K4caS1_Ui4QsIXCP3Hs8lZjwhCHizRPXW6WYX89tOUEWBMe093zyxDprSbg0jMfjbBtlc93XvpZBucTJ1awDPMUnCKziGvMu8tBsqeIJCuTJLfmAgaUmXuLAXy-flQ1ihCUCa-QppJ-wV9y7oZu9lQ8DveEnK3_MyBogzQC9TQYt1KrixQBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=RE-pPKFdzuiNGaB3J0dyp3FV5CKlvRnH6RkDmf91CVNsa1g31f67Yk6Q7T-zfrQmRQQMq74tPeuxEy2GMMqRmAskqcbGeyatgl4pAaQGE9Ccqk2In53ca_KfE8aG_4OLSOWb07pbwzNDmxiI5PEpk9G9nJ14ARPQ6dH349N518wM8Cn7Mh4qiHlY1nYcUMuWc0cKyw_04vn_5oIlOcEu1YAxrWDYYnsjV1zZqNppCML7cm9uJZ0Kl8VTqcTU-iFESsRbM4ZHzvzeGIQcyyn-cYsOMTaIAS5fBMBHioOuSSniEqeJlAqESazQkBzXTgkwyCXYvb3qVc_FQELSVCdIhTNk27WG90Di9AuwXH-pUjZyUC-sf_PgzFYC7eDl4WgChJ0qmpdhHPrPbyP1rODH607LIA_CawwxuoRUS6gMRFt8kIVjiqU-wCOdKT-ZY0CwVisqhkT8OQwpz5aQE1YjBzu9VdMCXKjcvACx8XefesrFsimFgIVnmD2K4caS1_Ui4QsIXCP3Hs8lZjwhCHizRPXW6WYX89tOUEWBMe093zyxDprSbg0jMfjbBtlc93XvpZBucTJ1awDPMUnCKziGvMu8tBsqeIJCuTJLfmAgaUmXuLAXy-flQ1ihCUCa-QppJ-wV9y7oZu9lQ8DveEnK3_MyBogzQC9TQYt1KrixQBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=WDejCMjjgIKeLvWOgTkDEKxZFY24l8twPzsGViPgjsoxZUBKZzppRACYpYFNtg7IpKMkzgE_lZy4zqPqtq0ujNjnH70qSDJ08EgpZXniNTUkFF_GG958flTz_Zosf50EYzKb-GrDbjAfSJhbVo6__T6zNgV8ON-v4jlBQE3yG8kzqJ7zbfg_lBmt17tRZC7dAvFLIRhRagdKe9qpOXYIWhAPBYwo69uGl53gwuUNJ8LFixl1IopgzeXLOaEzJhG_VCQsoL9UGIicRWhs84hIskJijvKUh5i_Xp7Hvra3BYu-5YzdMbqgVcqmPxKb2b_PUzGho3DEPXLPn0o-ZB_szFr3V6_LAkEQKzKCIuAkJq3azwP5GeJJvsBm0bBgq3FrppQmUCP_Xo232kXwaxx4aS9NzSN-KfBGYDEfKQwuqOmiOjqBdXFLtgt-0R6hmuOp8vJVNsN_ZFYdVbqbFN6P4dTgQrpA4ODmnm3I-0xzIBgGcH5fVJtgUGsP3O5thQl4YPfLmivNTCIsZ_QDGJs9aWZQYYKIIsfKRHdWiZ-6cX9Xh_cjOebQew3eaJnzXhA-BWlZXSt6rZKTPZaX8ENCfeyR_4DnD00ZxjpPINeerxHHHONzpcZeZmKNfHbsy9a11ii3t7SSnnplDZb-2Q-euodPtZ6N9y1KzNhysP-ikpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=WDejCMjjgIKeLvWOgTkDEKxZFY24l8twPzsGViPgjsoxZUBKZzppRACYpYFNtg7IpKMkzgE_lZy4zqPqtq0ujNjnH70qSDJ08EgpZXniNTUkFF_GG958flTz_Zosf50EYzKb-GrDbjAfSJhbVo6__T6zNgV8ON-v4jlBQE3yG8kzqJ7zbfg_lBmt17tRZC7dAvFLIRhRagdKe9qpOXYIWhAPBYwo69uGl53gwuUNJ8LFixl1IopgzeXLOaEzJhG_VCQsoL9UGIicRWhs84hIskJijvKUh5i_Xp7Hvra3BYu-5YzdMbqgVcqmPxKb2b_PUzGho3DEPXLPn0o-ZB_szFr3V6_LAkEQKzKCIuAkJq3azwP5GeJJvsBm0bBgq3FrppQmUCP_Xo232kXwaxx4aS9NzSN-KfBGYDEfKQwuqOmiOjqBdXFLtgt-0R6hmuOp8vJVNsN_ZFYdVbqbFN6P4dTgQrpA4ODmnm3I-0xzIBgGcH5fVJtgUGsP3O5thQl4YPfLmivNTCIsZ_QDGJs9aWZQYYKIIsfKRHdWiZ-6cX9Xh_cjOebQew3eaJnzXhA-BWlZXSt6rZKTPZaX8ENCfeyR_4DnD00ZxjpPINeerxHHHONzpcZeZmKNfHbsy9a11ii3t7SSnnplDZb-2Q-euodPtZ6N9y1KzNhysP-ikpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1dJIUB19JWiOTjxXbLx2yzYVIu6tmxi9SGExtAOipddkjKmVZkHW9w3xFVk7t2OGtyRLjErQdHU0BbrgaEcYkxSbLmnT6jrDl7x7SmqQCu5X4s0OXPWAmqlo5Bh_-TWP2YygWiI7pztgHEQ-jZpznD-DH-ND1oAFhAdPShXRfpd3srcvtiBNTc6bJ0GknwaPqZcdtSboNCLjgvOlNdB1-O7hrYuD74vtJx44C83pPpveve5P9Df_iJukn721grsq3nubS1dd7V-9Z8Niol3EuDbE890tGR-yPAZXheXSQJkq3wdsVS1tj07q7gTrqbIQhVJKWL7I_yVqo6UKR3zqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXegxye4AqsI7agExFU45EYPcr4Wp4XWtaviJrjDQDFD8FkhByPkzObz6OvAqImy2wlaU45T6vDB6jFm9REoIdDsvtvZCb6zQK3m6jvXge1ALUFdvqKJ4zzFdjcDiDyZuEzEKVX5dBZ4beDM-YxladPh3sm0qwxOsiifh8x6TFzF4w4SJPbwtGJM3WH8iuERnwvLomwUZHs_oASUyRLZstWrD58QDigkHB7wDZfxNNLwvv40vqxhPjZ8sjA250ZJlLR-xS9l7h6qk8kdpf1pp7jgjLLqcuo1Dauih5LcwzN0o1nfrDX5V6sQm6K0xVBkXI9oVxvjrxCJ_p2JvIOFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_bXTZ_4eZn0VlQYY9Vs7tt-ezAnASSv_z8e11OZ5JHe6UmCYIhSIcIDfQMdMY5srjF2dSTN5eJ5aBVIV7McytOlUT8KrV-AL_fMftdYpqdsAA-P-HiJ9GdbeOueL25vJ-a_GqrePhef44Yzo6BqYPG2MA-0gGIZi8PSVcMVUH1ixnyhdVnMBcwy_pLUHaO2qwpelEn-apjScvDXiWdF6bXyeYZ4p9W9JVKota-yc7uaTEqgkMHr3KFtSKCKSvfKUFjPfCDzHSXS8hF0rvnVJOU-Pxn1SM_oZOtD253kTMoQYNWbf8LuoC64Pd9Oj21aGONThSOiL9RqrHpfwFUkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=UWI0RdeViUVNa-_M7atw0KxsnWzWNlL9-ARpHuDjY-NamCmSy5xC_t4JlHK4RrrvgGCMqJ-hlG2SCC7TLtkRRBF8I1QZbC22ivk8oeqv_a59hAjcp4OnPr_x9Pwxa-Tw9aNe4TbjfNfPpPgFfirWEpix6lug-O1d6l6JpISWPjs9nO9QmkcsxUIumI6xUdAGcnKcDfhU6F37MQECtgd8DO-cjW6EL50_uoPc1-eP86WbyZto9_qvefZPycdyMxJRaS9Gq4hlXZxHHWQ4PvY_DrJ5IBgA1bGdQKP39CCLlH_VyDgaQk_VagbH4zKXSi3I1NL_UvgWDRSXC-bvsN_aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=UWI0RdeViUVNa-_M7atw0KxsnWzWNlL9-ARpHuDjY-NamCmSy5xC_t4JlHK4RrrvgGCMqJ-hlG2SCC7TLtkRRBF8I1QZbC22ivk8oeqv_a59hAjcp4OnPr_x9Pwxa-Tw9aNe4TbjfNfPpPgFfirWEpix6lug-O1d6l6JpISWPjs9nO9QmkcsxUIumI6xUdAGcnKcDfhU6F37MQECtgd8DO-cjW6EL50_uoPc1-eP86WbyZto9_qvefZPycdyMxJRaS9Gq4hlXZxHHWQ4PvY_DrJ5IBgA1bGdQKP39CCLlH_VyDgaQk_VagbH4zKXSi3I1NL_UvgWDRSXC-bvsN_aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=ubzQEQ3OneM8RLa_yjJTnVTrqK6LIFm0fhWNy-9Cmt9i_xG_66qteLzcTU5ESC8mdbl1-VbACaG03JAtCymJKvgjKqB_QT4SBajx1AsPaNjmWOHuefi03Fu5DqxGYFQez1W1xeoqYjVT6axweGTKNL4d8PAPhJxUbdBkmdWCKQv0ykNFvB_WRNbwt1HvCgYEFmiCldQ9cBu3AlHVTIXtuva0jZdgNveZBmoQtmn5RAz-dyicKrk0gxsKtnUhpxDEx1Ji3NXHMmaoqmv_Yr93q14iHlN9_kOEHDz1RG7KAJe7wgNEA-zzrflkj1cGOwHmOhcNsVU3GhzF5_qBl_kSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=ubzQEQ3OneM8RLa_yjJTnVTrqK6LIFm0fhWNy-9Cmt9i_xG_66qteLzcTU5ESC8mdbl1-VbACaG03JAtCymJKvgjKqB_QT4SBajx1AsPaNjmWOHuefi03Fu5DqxGYFQez1W1xeoqYjVT6axweGTKNL4d8PAPhJxUbdBkmdWCKQv0ykNFvB_WRNbwt1HvCgYEFmiCldQ9cBu3AlHVTIXtuva0jZdgNveZBmoQtmn5RAz-dyicKrk0gxsKtnUhpxDEx1Ji3NXHMmaoqmv_Yr93q14iHlN9_kOEHDz1RG7KAJe7wgNEA-zzrflkj1cGOwHmOhcNsVU3GhzF5_qBl_kSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzYQ5sfrq8Db9yJg09vGiDLNOAzYYEJDbUTVM6Ocv2XzSF6yLUEv7rbOrcRen9I3gmdUg1J-2pqHZkRV7ibeT-F-kEGXb8UDLbJ1H-Pk5QMDQY4porOP1KAiWGigoTrGB5FWJ2YQqOHOE0OfKRrYWBTJWAzarlwkB70GJi9e2rB3ummhRFUhkH33zP81rB51m57Uj7QuiiM85aoVDHCcw7Jo6rcJ4bxhSisZQH7MD5YhClIABx5ElfPFwOzzCfyyJFWPLQshq6ixDXRtEWyRPr4o0-zh4ENki8fKle7-RJ6zfbHPMRu_ipIJWfpsGxec-9HT_gy09nNJjo78wDH57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0NWeB7FV6icrTVIKVQm_BYDmn0XCpbAKPf36WYk2mKlabXFdfWk7ofdo0R1ZUcx9rqEJ10gfVckhH2BoV-HX8WfUPdo2jFzJPJcp4faIUeaIu4pEtWlCWXX0mjYQ10aBiPKPt03fIWFSTszSB4iBObMX3bmEPa2-f-CZcjvsxhcstOVrAYrsIQcLRXFKNEUJy5Kb9cnSQxF98XwAVJ1nLEzG54Mn-zLuZ6qVsadaiONLk9KwuUrdbKj1Xq0f0ZU2W-RJbE6XjmXnMD7ZJYhL9rZCYvHNpKlXEy9hNJF0CNGP-31bM6YjIs62rjiI7JZyyd0uogqvYLnIFz5xYWWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBWy3W_U2CccptgeLb5HLMBs9K7UOpATqUrKeZN68KgRcw1gjEhDPSlI3y5ZhZ0ETh2R7AOhaHz7DmLFGHsroBW_Caa0xu6LtKCLSSLu9x_yjoqOPOFiJLaOXUO1wcnK_Ih081RnxOJ5kJ47u1BiSFSFVGUjZj5us6qO2zDYldsmIEBEIWK5E-WHLRrSHdHd-iCTE32Z_UGpU1ih51Dk0FW-BqS8eZ9ViDybB-Mk3lJDVt1GCABn_LKZBcHDgGsqdE1n8hJd8uU8zlgfJjnPywYFGs8cnHt7lAtW3vPa_Ccl4YhjaWx419reiOsDA2AhtPQaF-bs2CmqxiFSzHGQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=XhXQAx_WDU9qllQ3a503eZ548hJZsnzz1zpiYRwPjnJqr3F0buyS5iEE8UPEsrkIPopdc7rupumagYyrfsunyzVPd9JIcm6BYKDZLnaAVNwJ-Zt4vnEBPTUgGYVoAD8jYX2q5zc3CKEF_zxNP6UXYKtjxXVhA1asUQBR7l4QV44HQUjKPyZCypixioxqwT1Hv9EJ6zw3vcvMVeTGW39x_uk1oLucApcX9b8UCkmDqt2YLFZlETKuxJ-WJFosnJpk4eliT9XqXi0ONPreHMtlPKDRNrQe4nMZCTzNrPj5AOzRB-iLz6Y5JwKp_NDvjkUV4Dq8LsVkWvKxWtvt6zMk5C3mgLEi2wgMyr0y8zrfSsbAPKlE1lwFWGazHQfwvUaS9J8ufbOghaFLje9w_8WLivZ7LB8AKOnuvR3340oF1ZKONtnDXKfxHvaq3z9oCYNwojcgJWpnM1qqkIkcmSyWdyACxVd0ZRxu9igYBl7i_B-yTnrXjV7NTUPAcWx_oSaz2YLe9LEzjZlY4XyK6xE7On6DTj6Pho3JuhIghK7Z1ZxiCjczdG9lChxma5gjHD0rVMzhoaoDcTuU96kxYKXqkbeqvTSEsJkyVdVSQbjvudpA9GuPVKOXsI44yng0HPeLosmFHjR3_ocjDbP1lQ_q7KlnaP36QlNhSpdeJHY4OWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=XhXQAx_WDU9qllQ3a503eZ548hJZsnzz1zpiYRwPjnJqr3F0buyS5iEE8UPEsrkIPopdc7rupumagYyrfsunyzVPd9JIcm6BYKDZLnaAVNwJ-Zt4vnEBPTUgGYVoAD8jYX2q5zc3CKEF_zxNP6UXYKtjxXVhA1asUQBR7l4QV44HQUjKPyZCypixioxqwT1Hv9EJ6zw3vcvMVeTGW39x_uk1oLucApcX9b8UCkmDqt2YLFZlETKuxJ-WJFosnJpk4eliT9XqXi0ONPreHMtlPKDRNrQe4nMZCTzNrPj5AOzRB-iLz6Y5JwKp_NDvjkUV4Dq8LsVkWvKxWtvt6zMk5C3mgLEi2wgMyr0y8zrfSsbAPKlE1lwFWGazHQfwvUaS9J8ufbOghaFLje9w_8WLivZ7LB8AKOnuvR3340oF1ZKONtnDXKfxHvaq3z9oCYNwojcgJWpnM1qqkIkcmSyWdyACxVd0ZRxu9igYBl7i_B-yTnrXjV7NTUPAcWx_oSaz2YLe9LEzjZlY4XyK6xE7On6DTj6Pho3JuhIghK7Z1ZxiCjczdG9lChxma5gjHD0rVMzhoaoDcTuU96kxYKXqkbeqvTSEsJkyVdVSQbjvudpA9GuPVKOXsI44yng0HPeLosmFHjR3_ocjDbP1lQ_q7KlnaP36QlNhSpdeJHY4OWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAc2X72tdciqZLB1l2pBtFDaNSRO5D09Un-CfIMOaEsXCFji_FmW4g2NaZNbZSlRdH8SY_-fhzCySiuPDqXGcpj1sMpHg_d_NThDWxRrKYHfkvX3UjGZbJLhMVRxSbqbBR12ornxUX3x89P8So9MSb2JapNL1o-9TMtS-baDKaKYJHDmHR12M273DLYP4OyDUJV2hF_HHKypmle4KF7juAQzQwRP3DAFYcimsB8PlYYRBiff1hN7Wuk3XF4jcA1gbttJaDJdn7EhYA12KFtDnerNzRwHASx152LPEBg_US3bOIg6SqF4n8mtdD7cQJ8AHqDvPaY0eEb1nvA-q72E4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=cWLmqUGfXIrxox6LY34hPXirI2NILd_NTd_38Oz8qXAy4Cp4G1YNrOobFDNy3Y8eqH4b9k6JQcbkrNT-jlQRYuhsBWq0PZVG9-6OgfNRX4k-uhbqOfa4_wM5T-wwV3F5yvGhJuygsTJXVC9A-Ftz_JdjS8dfkmb0XbMSwktExhfP4FRpUWSgyGD1-0r0hK0a72-OL9xVr8OhMEUhLfGaoAjm1OlC0Izt4yoqf3FBvdCPRjD5mL6TKEciSPYdFVu7C2AAKRTqZ1HQ8ZFbMWhejqFe5IGvVIMAQdJe_RH-MMGb0BclMsdUiqRsnqiVTRcxda5OkyqMojMMw3Sm4CNk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=cWLmqUGfXIrxox6LY34hPXirI2NILd_NTd_38Oz8qXAy4Cp4G1YNrOobFDNy3Y8eqH4b9k6JQcbkrNT-jlQRYuhsBWq0PZVG9-6OgfNRX4k-uhbqOfa4_wM5T-wwV3F5yvGhJuygsTJXVC9A-Ftz_JdjS8dfkmb0XbMSwktExhfP4FRpUWSgyGD1-0r0hK0a72-OL9xVr8OhMEUhLfGaoAjm1OlC0Izt4yoqf3FBvdCPRjD5mL6TKEciSPYdFVu7C2AAKRTqZ1HQ8ZFbMWhejqFe5IGvVIMAQdJe_RH-MMGb0BclMsdUiqRsnqiVTRcxda5OkyqMojMMw3Sm4CNk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrofXHDgX-XrzvTIUukFPcHLmVum93R8476jcUNFgCStk8ampwN208TNoNb8SC5wtRJ6oXV5O00WQyzRGZe11dNeBPlijRcnW0ezTHyJU6QTtsgh1IpVLPfb1MlQrMbLZ0IN9W4Mmdv7tOL5JGlFvqYTB2nEJMjziBE3n2uMcDnkweby8CDo5746KuZPsrcppXosfBfKuKtOWgkRTb3HIsEHtzmD61TUEjGr669oy3sRe-jpg4teIKVBW8sx8viFN-Hy_ZMTCFYs6_qMY_w_S3fM-OZQZESn1oJ9riwhy089a1EL_7AHppXnN-oPE-3Q9YgtkiqWBkBaJHo2JZZwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gb6IKQkknDLc01yCH4X7hgrZnnLAQqbAocPY1YQxSsTtEHs8LFbj1aoY_QZ1i1vaou-0MEWRFaz7RDuaAXUC5bPNaA1UiQFvsS4S_lJVLWF8RoCFNQaO1eZTTsiYjO8NwayR8FLh8pxHlxCygzQKP1WK5sPb-8CuSdTj5RzQpWFpq-D0Z_S5BX4GdBVrg9oLNFFII0lkyQlKzlQljTvVHXo-kM_5REESEoQwIa7Egrz-4Y7-TBGouT3jtg5pULq0w1-84Tz6ZyQ6nJjDw5EayXsRLV_BeoZS9gdASFYMY9mppzpYAykVXTzutI1uSgkeXcqga8mpjGe9BLV-wstmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QU_PXRqnIbSSczDL1ZyIwKpTmUk7xzv7QFhCcSBCW1LrmVS-S7R6AOZplvVMRFsJ338aQHmi74vCVpRQC2g9k4643eAv81VyvrFhjgYw_CnoUkN9eTKi8uKX6YR0TRFdhzqbrQw2SHtVRMg5GW6C1RxRck__dkFPB5k-4L9oMoAlnctXSSQzgfVi4SRrSAIhdN0L8_Zm7H-W7OZhkgWu1cxAz7DPuI3416q3-wf0_ZOclHX85XjkXDyE7yRrWkhjrQuq3RoDTjxxTxPuzUMwdv4MXwKF8G1aJYYEI9hcL75860Krj_SGF7_PkOzG5oW5XPs7J_5r7Py5ItxBxP_Q0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=IslM9pgMWiEk2HW53lNWgAL6ygbfJAxOjvdvQ7GN_Ro40SYPvf-C3-7iv-Vc12lYjYmlnGA2-ZzkFSsOktMNemBE0YxWDkN8Qeqt74dr1ZLxa5WZTaWjWOeek-8gAGaiALathUqqWvxo2nu33id2nn9oCcYfIkU_XZfUQy_aYOyNG_70QtKaf7naaeBONCDHqbK1zZ8T0Oi7N8kU4p6pxumC5MCLwFfSXvN31_QpyvjArS58lQFSwSpRGf3a1TmPduzdeUkB4ZOEKSWZ9MSvj3U5xJnA2OcQ4UwarxLWSvxF1yo6l-eBkMiWTlHU_h79KB3PMOE6Vhkwfta6EbI-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=IslM9pgMWiEk2HW53lNWgAL6ygbfJAxOjvdvQ7GN_Ro40SYPvf-C3-7iv-Vc12lYjYmlnGA2-ZzkFSsOktMNemBE0YxWDkN8Qeqt74dr1ZLxa5WZTaWjWOeek-8gAGaiALathUqqWvxo2nu33id2nn9oCcYfIkU_XZfUQy_aYOyNG_70QtKaf7naaeBONCDHqbK1zZ8T0Oi7N8kU4p6pxumC5MCLwFfSXvN31_QpyvjArS58lQFSwSpRGf3a1TmPduzdeUkB4ZOEKSWZ9MSvj3U5xJnA2OcQ4UwarxLWSvxF1yo6l-eBkMiWTlHU_h79KB3PMOE6Vhkwfta6EbI-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m41hL6A6C0EbZ5oIKf2_ZsJxLljtUGVavwXb08K1-tZC9Zfny4LnNzyLFKIADbitaYzM7HGlo9TVb3dV2A7N-qa8j1kmElllpehUN1QnpyR0meHzxelUNGcH64iGAhf7gGG29jDOShftjwMtnBykiidTFeePOrQNhLKY1l2BIVMvsapC4avWolrktoHb0LjmgF1RYDlcQT0a5Y6FMIVRBMlpg63jrQ3N0pqbt9fJ4Yaur_oiWmZnRXjokhciy-zu31xGYvF2pzVekqw5iXp3MgHK0DRZ_VAYYs1dq2Qza9vEUBu8dF5Y941lQLEdJAFrAYsBDy53Xs3ZkH3yMZ-tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY_agTCjOPWlng1L5SHUXfNGU-oZoC3u3E2ypqtrbRtz_Fq8_dd33-ZQlDFc0pv7rqEthEARKFLEWgrpnnt4WrrTwEZgzryskpHiYfgAwbWzotDJs1tqYtnfkw_xtCplpTp9CR8EgFx0aW5uTZk6-JWI81jwYeuaszVL6i0qsnLmh40H4XGKgcxZlZr7KqSR6MkV8JBxZCZIMWtofcJkn0mlGoqT_tWDZ9Bxs1NpFa36gtJvPrcud_CymuDwUapVDplrf-FVU_DXCA4AaMlvzvoGgV2ifUvwZYs1o7dSAG5MuNCRCkj2WrHdR6isfkAQ0XPnUowKBE7ZPNZxPK2W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEhs21HcT37VvbwTvXc6aCiNyeSWpeeWJa8XMzYcECzxy7rBABQV5wAalFAHK38TxsFVllpBg_tqP_VIwQ40jFE0MVbzBrC7pZKT2bDa5c0ODozpMcPoRHVxjiuXzzjlDne1foDUPCbAPtTnhsgjHuA39rGtJdY4oGNHmPz_NrbJyx5nsBnJ7Wzw8rfYzXOloAx6zd5-mYGehY_uTp5uDiDzw-Mwp4C3SoV_L4D05whnsVoGUnBf-gCI6cyuwnZ_8Lr2CmzeYdyCq0-SR0t-CMiPCy0g6g7D5h2g69BWX-jOV68wBtz4OQCyDK-S_ktDa2E7sXI5GGZFcgLWwyZChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJg3oHfbQJ9VbyVchTMv6M2n6daokd0ZbeC1BeehQxpN2w0qpfTfuXOAWtzGHG29IyVt_Gbw4pRsmJm4CFhDXPI0RYjQi5e_g94DYYaqk6OFAAJ5G-Vav68x56e7h_Gkf8iNYeF_cnN447YD7FnMIRpkxq-XhVk_Ig24OYgBBQXMYRL40QAXJjferA6xR-C3tNJg589jSkjlqi7mPd_Jo21hbtO3nIkoLk-AftKH2jnHeJ5LvezeXL37vnP-sm_gWkfFfQSEID--9xrXkP7WJDG8yk4RT-RR27C8YSd2YB6w8Gxhe6fVlLy567yvAWKpgpahYrCyG7QzRMcJtaVUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCNvIuC7x1EocXy3I9iBn4ou1Xu_LNOGctRlg_GdYlZ6OIFiLgox9MY7vkwE_9LG-txnnIoDcwSp_WNAU9xrfINRpT1eS5mw50ZzaEQ8GXE2oonhpVGwsv7ReR-ZxIGTBZmwo2mjISYJgynYYaM_H1f5l7_gDT8LiHOo_MptIteTtt0DYwq7kZ9heU6UCYBozxtIZlTlPKhOsPt2kPHDDZioCJrWNDWVVSgkgcaNNybl1nO5SzNCxYLoro6DnuEvkdSvXT3Xs2_HWIkEOMMDTWHRaBWt1OZt_nzu2g1qeIhrXsBxEU8Toiw1XBe9HzA2PDyjwUEeXh_lJf-LoIA3tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGMOKf_-ZlCbeW_bfADRZ9ynzxH8xHrISGA6IfMXIUm2PKuM9Vs6u8ANSbOuisZVciTWcjPHFrNzqVaeAtEZunSnHeiM68Qiqb_mBeSabZlgLDHzgmTgt-9XEgSb7-r6Y9PHZnXX2Pz5kmpgkmqJyDSNoh4huqe_Qwxc9z8jFpbxZvDP2n28xY5xFMhjdK8Q0BJCM03cVt9A3yRUggKJFiMVKouuxjZP7EJzZxkYk4N8FqQAH0ZQphU_4WyYk5zLQ-jCrbVvH9XYglK1rdmm802m4ohh68J5Jlv2IUdkgYiLnVVPK9dGlzxAvrM2RNFaCqFA55khq_X5wxQ7gPfpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrC8c1FY5HUMTI6eCVUlJK9Xr4xzuJdk6ctOyS3te9Q_Xx5eVMoVIrr4jPetiA7FY1VDvrI2MH6Bgn73YwZ7IKrFfAmjJYTr_ce9tsaNjvuuSd1DuvsEdKlP7lfdfgk9vW10OcUwJTwwJWvUzG18m4yPhcP1WhkBp6cEIP53bnkpG4Gf3E1icepAI91jFnJ7KcIbtNBew3ZGPBt6UzYmaY1soBdD1CQoqAwjQZw7GK9WiwaEV7jQ-ZNBH1nVxoknu_T1W-6G0i0CwL7iC92C5ViF6SRDVzRQmzdXQtp3yl3UGWoyqWmUtTVeFGtoOAv9zn6xJkqCLaP93mT_iYzi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUsUeuLUyTxmCuSLWzhCEBsmEuB5nbRE9a9BYS9avQja1ZWNRHgHtRMXTNeei165gb1HxLOLBSWpMTYEtpgGz6IH3CiSq_UckETEDxqPDXhkhR6Umz__JIcav7HZHdvUMDn6Vfrsu3LPgQWTzSe3wGLtQ-3YP9z1UP4BY9J-0WdwP-EC8sXbsqoTdkMwjfW_Kh8WNqqZVT-Pu2MYjMNoFl1s-JauO3sjjWE6o7oZjvEzriuO-XLTJu0L_mA9029_waesWLWMfc7o34Oa5mk3q75OB78UujzmS-qnmhN2UWhAaLpzRlDwfvNXmlcqMeGy4bxZUrK5sfhH6Mey83sQrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdTAviy6qOIbGp0SOFVU9pGTjwfseNY4Out83pcsTgeZPQv0HDx9Xuc43ofdssv-iQ0pBdZkMIBlDKIjkwWuPKUYR_K4mRO4aOmsOAIzxf7J779aucn_EOpuNtqq-EIWt5epFnfdZ2hAc81kZgfw9eHZ_WyTo3ziMRk6N6x6Knj-GjzPKaYri3mxkNjIJdic4a9cexNbYATC9JJsv9wa_T606ccQBto4FOLiINcH8vxJH306Z-eGVuc0_LcwQjAd2TXNspkJhFvxoXemWSaY4aBqaMYcN0k1IdDGeHgHu8hH2VWx0o-3UqxDMaEzy2uFkisVsIXI1AXUIOJHMRUHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzvuwbwQW2q3N9K4uCfV7l2xxvw2iuibdPWFCKe3jXgwpAPAuRANEhA2C84j-NAxlJZu3AzwcnNoP14QB4s44qKF2RnYdxumaQjlDdNS5cj5xcMkijvkDsqi3P1lfNKvf1kEHpH8e4V0vnJbg3hLHn_63Dn1P40AvLU_gx1v-BpTHZQri2Q6_E_0pULEhcP_d9Os4FEzqbIyAlLLBXJAXxS8NeEYJWjofp5UB0EQEOMRznTeNRSlXZhRU0Q1a5mMO7DUmRoZtwg9Op-wxU-DKKeTApYrmXGkTwVE6FCwFtt5fQ8A2SDC2oJb6V-JQSVerygskyMtG1GTp1cZlPfENg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8naFzBVp7lZ6o33IRH9iT0FjPj23GvPhqv9V07AEhd78eLejbnSP0VucRS1tB9nA0mtgY-9ebNy2qmZB6kBzfV-JaCMfunPdIt1F03bInrlLzge6rXl0CobWEMyLJwP7w9sf3x6uGZM24JKV7IrAoMBAcsvCmKThDqQ8_UAx1W8uJHe1ctYDC6LI9KI8lCHBBZ-xp-DQsCqS-LoDv-jLQiLwhNVsT4OcpC_-L1V5rKjKxGFpryGGgzHAQOoHM9QnXzdwMa-Q_JvmUKp4jQ0xeMYnLFl8SK-KE8rCytxDHHmcmUW-JqFun23axgUNhLPbrWEZjk4O3-HAAwsBC0tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1OFcK2rqOxsPkBqfVjru1ENXFu2AhuPrB0dKtw9Jo517ZFxIc8eb6A3Cz90tXYzNPo8P2sCcKa8GSgj7Pg-bWl3TTyWQ5D0jSd9x4nJQXN_40cmuClca0i2oCcNj0rV65xKJOVrFzGiqdqLpsd5YPh7KDCIe4FQHdKF2NkP7Y44_l_Nu2w3fTc-WZ9toWCy4M5xIKS7newn6NJaYUPTC9tA0ToZCAomhki25cPHR2LlFgY58Ep7oibL8Ovhzy--a6Rif01bR8Ucop3OvjDxzrvXdadM7NxDiEEcT_YKvP_pMEsKomiHzrrwwzJHV8m14vWXtA6d4snkHFhvpC8SOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvI_9zBD-Hr6qsLVGWDENhCkM3PHv99fTIvTURJ6COuLsE0Cr2HNJEI3fKkAuDu3MgyxtMUZ2k2Zl7SJyhUlOV9Nikb2g4sKnoBLbuT9g0cX7y-ok9VGG1i2AhJYsMRCvE64ryS7oVN3b1PDxRl2zGD9jRtSnOctnqGiqeFxad2laxkRmklfFQbiuWk1XUHkDr6o1Mtgs87Il41nsZxF7SS5BSXcUV-SAFoe_Lov8iUuzvZYZv2wd4Igm3ZeESlYqflcJV6F6034ZugIoGN3p0yaGxnw_FVTIpOIRMVK6cGdGr6gOQQ69Nv6lKFG0E6vh_cohuGHakdvLucaZRG2cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ-UJxy3Lhcj8KLGwXOCNSQzq6GAUWTzVMQgltWWO_L2nYmQ4ahcp2OaPaWY5G3ype7mGOZNx9C62fvtdgHR_SE8OPv45KT0jgYoFkZ0t4U3h1raam-nRc4znaV8WmMn0US5dYa8MkJ9Cr9bYK0VD_cKOjzV0kl1uw1J61WspAxCxsxUbm7aS9RA88-mGULOrgjij9Qi7X0n_gKbFc1zyRkLIuvehD5otdsHVf6o6W5XbTaPYH-DrgelpUUw6xAsrZ6QA9sWXR-B1MARzn9JIGGkrDxo__l9OScamj07D3UflqNVfsK28hgtmb1JZ_EdrKNNjGyR6_QLPrfLPbPW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=EcMN_iqVbC4V1Hog0JcnegYjcOpmpYWT5wdbDWxcUmPE8kekU0fIKdGLI61sqyWZW5qHJhGddJQHg89cEmiK3MKaWyIvRlPyKEvhEpkWUCl7ERYFCqcL5PPPM2k-_-e8OVRjASejDYxNnaNJuWfF6VHDiE9XSf6Di_iac16H_rZsXIkB23D0wsMuBW0K4VPEdDxtc0uIPSBanlUQcVTcp81OATc9604BLf7t3nuIUQEHtkUU1IT1hL-2XPd2682ccYridYDe3hin3BmOGoz2WpqJPClQRUeKYTuONITYKFwBcRXnp0knpK1LRii7_nv0jIXJ6Sfrwl1VQTOgCy3lRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=EcMN_iqVbC4V1Hog0JcnegYjcOpmpYWT5wdbDWxcUmPE8kekU0fIKdGLI61sqyWZW5qHJhGddJQHg89cEmiK3MKaWyIvRlPyKEvhEpkWUCl7ERYFCqcL5PPPM2k-_-e8OVRjASejDYxNnaNJuWfF6VHDiE9XSf6Di_iac16H_rZsXIkB23D0wsMuBW0K4VPEdDxtc0uIPSBanlUQcVTcp81OATc9604BLf7t3nuIUQEHtkUU1IT1hL-2XPd2682ccYridYDe3hin3BmOGoz2WpqJPClQRUeKYTuONITYKFwBcRXnp0knpK1LRii7_nv0jIXJ6Sfrwl1VQTOgCy3lRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsMVifLiChygOK9xUUi4549eEjJW61iiS2euIhDq1Ze7KgiHbu_aDiajYcBdvdt3eC7-_2-h6Dq-NJfE6nI-ryS2yo0dei_sIC9PESVcTNWOzlCO3C92WwQMfRgzU0d_Sp8RFVenGLCYEscUe1s4dm8HIHL7-wOAQoHNJ5rJy0g_-HTbg6VWfGBWHUOEyCAADpPl_6d-8eJytsaJEHGooGC6ehywebPmk23IOppEewpR6965WztHDiwLf--AV23FVkLvgmMpHi7Rqb9BX4SRMG4exoF1VX5fWieLhkGNxYkLGAacj8WUgYvjsMRkDkAkgwO0G4Qck2D_6Haq1mROIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myptt1tXyRnYrdUowL2tVqRjXzq_g_h3QHRqkzPky9qTg_uH18sOQ59GJFEIdxIptxzsk48u5I9wGkPc36vY09ZXwOAbx02BfkbMSX-lBfa2_95vc3QdpxfUrHkoVeQ-kYedJTA_BOvOU1bjIkUl1vJui09-BlsDb8clM62nS8lUUNCyN5PGG_cgHAHkriS3LuX0LWhxu6G6JK0gDEr3GTfaJuouUrR2y6GdNk0cDPlLCkUu414vwZJU51EWj51tuDwR46Cq4d3eztDTljgRkNwHigcMqHVkMX-4PoORcy5Tl6j0rbtERo0cDTnF_5zorDVdc5LViPGGex5VgkGB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uebmoOy0qhT9bGvOcTRW8uBjy0kZLfukBpZG8Pv7lN3OxYBQdNh0CywUnJ9yhkgL9KUTdVMzLCb8eHOom7Y9bUeSZgc9_-SuWCgTyFRONnRbi8La87NtIvsBA0bBZ-fVm62tNNdqG-2texVcG6XmeUv4FmVFV-zo76rISX7pYEs_vi5cPoQJN3lWaiaCihOTYBuj-leVC77V0sNIwmIiNtxqiUz7DGTwKX4seIc4krD_EWPLEV3w6txF8uzq5sJCXZYqaBA7j6ImCjVasA-ddRTTWCCCYs2y4XWqAJGx6wy1NCxbnpfRfMNBYb8dVN3bYVp7ecJxvU0QRlN-Px27PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3eAHf47ol4eHScNU2T76LSgnYypMaHyEH-UKeEWGoMEF92Ca-tsBHbM3j_hXvhNSDI3IvwK5J-zzo1Q1Utw0oHZz33kKJsJiMC9sKffDtjtqMQGISjIICOJib5Wt7D29vgnK1Ubvmz6D81WOnZUjB1xEIUFdP4sctbvhuEGWyxPRPvqkswC0SW_4xLRwNsil5pihOHfrxgUnPTWqRLX6ym99s3wE6uUs4dwSJRH2g2eo-Zx6U1cqKanNZkZQYy4R3hePL0RK9UUlVcdgtAZW4sOSaYQFPFpfQf9029xDnu36SlT_4_bpNWMlJEf-j3KGXhgxQcIt_blfRpxCwl4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=VNmIa71Vot1wWCmN8E0b9n_UsYs71rw4Tanfrxj3Fl6MSGWSgzUh19xpKJ28pOR9ayamUgL-7fIL8mfoHRN_AL0ax9mun8MCaWNVTU0ntecJd1_Q3u1e2DGbp_Viwd0uPsGM0u932TWpbjp11knstEUvw462bXydLl99j6ZUdWeLga72ibWBZYZxQSWHMuMqISbXVrdsHxX9XK8CuFc3JeLT46HB-RlNJcEFg31mjfJNqAudtgLje4VClqWG74h8xCp5VcXesoDjHDbk-nsbbKDpbVSxQPZMgwMGUZS2qPorma0v3aPLPIp6KG_1Y4iwMAIzbpllhh2mbjvf0t05Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=VNmIa71Vot1wWCmN8E0b9n_UsYs71rw4Tanfrxj3Fl6MSGWSgzUh19xpKJ28pOR9ayamUgL-7fIL8mfoHRN_AL0ax9mun8MCaWNVTU0ntecJd1_Q3u1e2DGbp_Viwd0uPsGM0u932TWpbjp11knstEUvw462bXydLl99j6ZUdWeLga72ibWBZYZxQSWHMuMqISbXVrdsHxX9XK8CuFc3JeLT46HB-RlNJcEFg31mjfJNqAudtgLje4VClqWG74h8xCp5VcXesoDjHDbk-nsbbKDpbVSxQPZMgwMGUZS2qPorma0v3aPLPIp6KG_1Y4iwMAIzbpllhh2mbjvf0t05Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=MhAdcn3LwnS8OZSqhVktNwBR1LUNKU98DFbxGjmaSyEN_iMvqck5isfPdlW_fEGYASZtQJpHc-XlIbv3iSaHM7HNN_SM6ssF8fJtwj1zyWG5y_d_MeeW-2xxP49oyaR09cBSM8v0pnG0nqvVw4tHIMKw9ebH5ska90beC4L-7gG6fUzcLt56nUELeeYEomw_eJEuaqEQtAm-D2Y5Iw30Ajl7oiFCZ8FVRCF8tacxG9xD5rxyaluSXUa_PXeRJYnb1UfYTYJAHrs4-yrBgmwVJjDk7Wm-47R4ds5XomxAjht5PaR3HhxnxWRtT8--q8by4Bnc5jhNikEOTq_9WKlbNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=MhAdcn3LwnS8OZSqhVktNwBR1LUNKU98DFbxGjmaSyEN_iMvqck5isfPdlW_fEGYASZtQJpHc-XlIbv3iSaHM7HNN_SM6ssF8fJtwj1zyWG5y_d_MeeW-2xxP49oyaR09cBSM8v0pnG0nqvVw4tHIMKw9ebH5ska90beC4L-7gG6fUzcLt56nUELeeYEomw_eJEuaqEQtAm-D2Y5Iw30Ajl7oiFCZ8FVRCF8tacxG9xD5rxyaluSXUa_PXeRJYnb1UfYTYJAHrs4-yrBgmwVJjDk7Wm-47R4ds5XomxAjht5PaR3HhxnxWRtT8--q8by4Bnc5jhNikEOTq_9WKlbNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
