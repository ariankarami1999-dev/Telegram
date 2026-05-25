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
<img src="https://cdn4.telesco.pe/file/G32i1L-CwRDauijByrqUHRckxnw3ihRQ8QjFdgp88XPK8_MYbxroweIDAx3LenJx-nq-iKEFzQF0OgRVeCOzahfsZRzZrE5wiDJXcqrNrU79IwxvHzwZt2bloFL3o71BRVHE2kcE1nUpz80jGUWm5wyf5Fky3tfsY7_DdJ2WMZPN5riFoY4YLupZywAZbTh47gIjrVGfeUgWsgsjtqw4eCnCaKDpp52c9-y97a7keEQbU0rr6-4_wWEMGSt402EA4PwrwKidSNn3Q44UNLbbgm1XTwg9s6bhgNoUwlgMfS6yFiKdnJEOMO0xKJdKUX_h8qPEqpoq4igOz-TD_0VmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.88K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
<hr>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پدرسگ میخواهد دو‌ قران از پول خودمان را آزاد کند چه مسخره بازی درمیاورد!
بسوزد پدر بی پولی</div>
<div class="tg-footer">👁️ 64 · <a href="https://t.me/SBoxxx/16632" target="_blank">📅 18:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من
پیشتر گفته بودم
که ما ایرانیان اساسا نوادگان ابراهیم نیستیم که بخواهیم به پیمانش بپیوندیم!</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/SBoxxx/16631" target="_blank">📅 17:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:   از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند، یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ…</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/SBoxxx/16630" target="_blank">📅 17:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:
از رهبران قطر و عربستان خواستم به صورت اجباری به عنوان بخشی از توافق احتمالی ایران باید به توافق ابراهیم با اسرائیل که همان عادی سازی تاریخی روابط با اسرائیل است بپیوندد و آن را فوراً امضا کنند،
یا یک توافق بزرگ در خاورمیانه شکل خواهد گرفت یا هیچ توافقی در کار نخواهد بود و به جنگ بسیار بزرگ خواهیم رفت.</div>
<div class="tg-footer">👁️ 571 · <a href="https://t.me/SBoxxx/16629" target="_blank">📅 17:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🛑
در جلسهٔ ستاد ویژهٔ ساماندهی فضای مجازی ، اتصال مجدد اینترنت بین‌الملل به رای گذاشته شد که با 9 رای موافق و 3 رای مخالف تصویب و برای امضای نهایی به پزشکیان ارسال شد</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/16628" target="_blank">📅 16:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در منطقه بانو پاکستان درگیری‌های سنگینی درگرفت و نیروهای امنیتی پاکستان و شبه‌نظامیان طرفدار دولت با جنگجویان طالبان پاکستان درگیر شدند.   گزارش‌ها حاکی از تخریب یک خودروی زرهی پلیس است و چندین نفر از پرسنل پلیس کشته و برخی دیگر اسیر شدند.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SBoxxx/16626" target="_blank">📅 15:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1rAGAqXr3kJNdYCQUPE6DbyVyy7NcJJ4vCnQ6XS5jInky0XwklNj0i9U5TmObA87ocwM4L44jx_RY__gFeM6RDbN-XEpZ3v8VB-eXkYWsRgemNO9io0gI7mDLZuljsUmsrM7ICZnNynhDh63jlVRNpTFHZmPkym-502wr28jZDcoENZfwpKjp1fcj9GcqEhMJwvhf0p5-KCuQPYIHhXoVxf44ZoQbm5DKP1fVqkZW770WCmbf8toD4Tqv0DrC7qqW5IQm_sg5nIh9tiu0AKNWFuIkJzQDEg3OmkQYs_K6iAs4BmZ1Gi1H8G0XNlVkslX5ycYJeLmN2QKVqTWW1wcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SBoxxx/16625" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay2C_WZF6QGy8DBuoCPvA2fzZx2KokcR2rMvucT1yr1aMTnFle9R6mI0wQlYXo0QepIkZLhhcsbI71NZWlK4K-NELw3ictYBRzLlbKOczCWHUrnY4dVijS_TsK3BvClBCVjAyjuakuyHrN06TMvMdO8j1PR49ZMVZM-RoejV_FcnHc1HAYuHh6rDd97a0LsDWnM8FvqFeGKnTOvhuSXS7p2fxrZiTHhPz5piDzWm8CCLu5fIuTrwALXkTDGbRHwjIACQiHNVr-ePpTmOTYWZ-G1LMXFrVs7cn8yXheXRf_4zX6NvEEnioJhtvN_u-9dcF0JVw4i7Njbmb7o0x8EaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!   حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/16624" target="_blank">📅 15:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkCMjUh2o_M5fnHYIJbqSaOJJJgaBpnr0q6TTs3LGDSVWXJokO-Q7LCtvFUwr9qH6pbK-g12bW2aqtedeCcOTy1s2thCpLiXLTm5GgtxfSulmrgyC3szmxYAw5LQ160uhM0McmAs2OILBPK4IcMpB5JCwbctMlNYjXz-btokrTBuowg8CNCE8VBNBtFAHdbkREzOh_jnT1L_1Jt8kXxtUqaxrX8yBXnoZ7_s98X9tX93cQsI9F5RXxMDdBVNl1xF-FvirkHeyjKTOPBrykfl8c0r4WIiz087ntpF6PE-BDXqvfbuq_Pelm0ugGLRKag8yGkHBHpA4llWESMmzObozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16623" target="_blank">📅 11:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16622" target="_blank">📅 11:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران: تفاهم‌نامه ۱۴ بندی بر پایان جنگ و پایان محاصره دریایی آمریکا در ازای اقدام ایران برای تضمین عبور ایمن در هرمز متمرکز است.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16621" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارت امور خارجه ایران:  «اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.  سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16620" target="_blank">📅 11:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارت امور خارجه ایران:
«اینکه ما به نتیجه‌گیری در  موضوعات مورد بحث رسیده‌ایم، درست است. با این حال، اینکه بگوییم این به معنای نزدیک بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
سیاست‌گذاری و تصمیم‌گیری در آمریکا از نوعی تردید نهادی رنج می‌برد.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16619" target="_blank">📅 11:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق متدی که پیشتر گفتیم سوزانده!</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16618" target="_blank">📅 09:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فعلاً ترامپ با یک مانور و بدون دادن حتی 1 امتیاز قیمت نفت را 5% آورده پایین و خریداران را طبق
متدی که پیشتر گفتیم
سوزانده!</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16617" target="_blank">📅 08:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این دیگر چه سوالی است؛ حتماً اجازه هست منان خان!
حتماً مطالبه گری کنید و نگذارید دستآورهای ما در جنگ تحمیلی سوم به خاطر سازشگری یک مشت محمد something به گاج برود. (سبحان الله خودش هم که محمد something است !)</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16616" target="_blank">📅 08:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb4_CYijIWfeNsaSa_w7B3oIERUVJc-vQRbX-wjkbv-WRQoL55D2RJ2t5sPJvd9ay8QYE661qSmHpkkQNyAZJYYJfsctUbsaju08siE2gUhFbXN6TJGQpRSIoQyqFJ4gtWL-5qxW3nXt56bPHTKcqKogOvzTq362MgIKpiT3lgRaVG-oyooFFfpT8i8bfFqj15ppIO_uV8GUJ32BQWsETXaBZwC3vZA4LXYxoeVfeQT32ZQCbUEzP_MeTssSJiBvuGTTFmlcECAJa97pUbytjCMBJUis322ZFUj9UQBPWVaIPPyntqv-jB-7bJoRnoSVRKW0th_w9lI0atl0-xu57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه هرمز تحت کنترل ایران باقی می‌ماند با وجود ادعای ترامپ - خبرگزاری فارس</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16615" target="_blank">📅 08:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ حاضر نیست هزینه خرید اشتراک هوش مصنوعی پرمیوم را بدهد آن وقت میلیاردها دلار پول بلوکه شده ایران را بدون دریافت تضمینهای لازم آزاد کند؟!  سبحان الله!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16614" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRyl524JoqFp6dVX4T7Eu86kfz0EQ3ST8j2gIKwMtpKXn1_vDDeRfA04kaeGMwh1LatS5lI7KkVXNtabOBPvcrpUKi27EJx4Idv0Z1U8kBcyB8t7-BAUQZDj_BUcWkA2sctyoh8wC0zhfLD2aBt1ubhsM_C_CKcsAeU_c2PsX9Frn1VhzjZC6z7stBr7-3GK8RoWCd1Vp3U7luYcj-_CR4vJDO5FImAj_cqe3GZeXbb76omSpW09VBkagNP8M8PCZRRioLcmgTLJyJ_flP9OHmF5sX6jjwDpLLT7Jf8i7OUg5T0ArGnQfNbrcSPJyS7nCj3OZPwszzSS4EFDgNOPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ !</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16613" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اسرائیل تنها.pdf</div>
  <div class="tg-doc-extra">347.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/16612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16612" target="_blank">📅 22:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg2J63tniX_INvV01wJEFIyW17cQIpME48rpvtSYoWuh_t-1FRdETyOoMqkvMpmoAKg1Od5eyKcAWfQZlbehZDFKdHYBDq0LZXpIgToLMHO6xcj27jq5D1bQHOQRx32WduZ3oD4t890TJNHVXWvLu4Kb3QjtcmprebbVB_kb4ftz9sw0gcpEWeagCA0m_4hsKbl3F53F_neODi5lSjFx8jQjUzlgo9GsCck9d__I_ltIGfMbTZR0Yr_Y4SMOwEp3kc_VR65SL7UT9q1LzSBumfQ3RMYig6ijPKSP-rGBO9_64DmS-jmEInz6VwkirwMJcaVcYmjco_hcEEIElv3HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16611" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=TR4LYf5jUvmvpY-Oa09KzYoS4eC2miBQWZjqEPU82Rf3cjKxHi1YYUR-3DqaPzCTUUxQoPDQH93wdVbiWqHVsSBylUxbxt-uX0wbrNsXZ6zKokhuOTVcXZ-6cDamIYkZXquAowtcNzZ1gwteQA3ZFTXksOEODVxvrvpkvgd66EK_dmnhksj91PRvCcZX0oQnzPcXaxItpB-rX0iiKjbmNhGzpbU_MLEgz0SnpRutjZV8JvTgbZASMBgkxT6E6bMe2ZZDF36atJOKzI3k95hlA7CHUux1QZPTCQiIZ_mUFu7bmHGecfBtRDpiXau55w7snocjaYP--YDaROko__RLNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=TR4LYf5jUvmvpY-Oa09KzYoS4eC2miBQWZjqEPU82Rf3cjKxHi1YYUR-3DqaPzCTUUxQoPDQH93wdVbiWqHVsSBylUxbxt-uX0wbrNsXZ6zKokhuOTVcXZ-6cDamIYkZXquAowtcNzZ1gwteQA3ZFTXksOEODVxvrvpkvgd66EK_dmnhksj91PRvCcZX0oQnzPcXaxItpB-rX0iiKjbmNhGzpbU_MLEgz0SnpRutjZV8JvTgbZASMBgkxT6E6bMe2ZZDF36atJOKzI3k95hlA7CHUux1QZPTCQiIZ_mUFu7bmHGecfBtRDpiXau55w7snocjaYP--YDaROko__RLNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا توافق در حال ولی خب شدن است...</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16610" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ
:
اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مثل معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و راهی واضح و باز به سمت سلاح هسته‌ای داد. معامله ما کاملاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره نشده است. پس به بازندگان گوش ندهید که درباره چیزی که هیچ نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من باید سال‌ها پیش این مشکل را حل می‌کردند، من معامله‌های بد نمی‌کنم!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16609" target="_blank">📅 21:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxL1DkdOjq8K--5w62UvMKmOE1Cpr1_-BQGynOWwc1bQsWbs8x1GXzSFdszsgM7Z0KosfqHLfSiXP1XbZR-I7rtccL6NOEuuPErDxT7irA1q54iM7XvJrtSpvsena19I5jQAkBXB4yonPpyV65YG1NlxdWsTuvpJTpZVVV3-ONHYYIGn4mfHXpqgpm6BhIAUOf1moUHFmQ1s7kHPP9TJzy8_3YLGeWC6PBdMzcnsx7MoByMCS6q36si8sIJJv-2TYOUJ6uUwKn0_dtJA0XzEG1UxRZo5akSMgTZ5GtWiehCBr6n5zYLhrAOtEt4syBP2jT9k6WGYul2ojmrH627-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16608" target="_blank">📅 21:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvl5pNJrCmKJv6gkFN-SC2qEJttbWagMVFtXSWdrCT1akiZpYALnnKAUsAiJ46KeUSbxJIIs6OFu0XcONTzpfRfVaUxl-nxcxKYJ1qpH3IhaUHbWuj4bl2TbUOw0J0i3qbU0jLvkINioV51_jYgVU-JnaHBkUM6EBalF51OwhLLokSAIG7JAVxhVjgm_nCw3m21ujjh7ESCYbvL82VmL4m-3xVlBd-Wl97gqTNjw4j9WyyxcXOM3KDltyttNnuQgdK3-WGAR_x_FF_eitxtXr_uoRYtodkYr4vSdp5Z3uLUBSXflH0AZAaIhiM5uuzp4gahaPSKb71Nm337yYULQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16607" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16606" target="_blank">📅 21:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«ما آماده‌ایم تا بلافاصله به درگیری‌های شدید بازگردیم تا حکومت  ایران را تضعیف کنیم».</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16605" target="_blank">📅 20:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=RUql1nBfTRdochj8QV22wHwvUGZdtqtOYq9bvWctahEjm7shGi5wG_CzasD0VTByZQ0MYhLRhPtC5AXTDIy__KerqgcKYw8TqHQh9FKiJqmZWGvNDcZXFb6-1yHGiU5iwvMCr4NhB2aClwku1P8Qq7Ba8EbbeWnblKPbBTEiCNdh7IC-5i64LmHUYPy3zTMbw5kSv9QZxKDJDj3YFWX_X5nt8hlrqV6CNjuvmY75AfMIk3LAQ201kSEIaYjVW4QHcN8SZ3aRC1RMMgEN67aVn0sGr3wel-IIJ08waKPwTJoWAPhYjDV877FpmAwicNoqHxdioaDF1-NfTmolBEkb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=RUql1nBfTRdochj8QV22wHwvUGZdtqtOYq9bvWctahEjm7shGi5wG_CzasD0VTByZQ0MYhLRhPtC5AXTDIy__KerqgcKYw8TqHQh9FKiJqmZWGvNDcZXFb6-1yHGiU5iwvMCr4NhB2aClwku1P8Qq7Ba8EbbeWnblKPbBTEiCNdh7IC-5i64LmHUYPy3zTMbw5kSv9QZxKDJDj3YFWX_X5nt8hlrqV6CNjuvmY75AfMIk3LAQ201kSEIaYjVW4QHcN8SZ3aRC1RMMgEN67aVn0sGr3wel-IIJ08waKPwTJoWAPhYjDV877FpmAwicNoqHxdioaDF1-NfTmolBEkb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
ولادیمیر پوتین جزئیات جدیدی درباره عملکرد موشک "اورشنیک" روسیه اعلام کرد:
🔶
کلاهک این موشک به دمای ۴۰۰۰ درجه سانتی‌گراد می‌رسد که آن را به سلاحی با تخریب بالا تبدیل می‌کند.
🔶
هر چیزی که در منطقه انفجار باشد، به ذرات ابتدایی تجزیه شده و عملاً به گرد و غبار…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16604" target="_blank">📅 18:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">-طبق گزارش آکسیوس، یک مقام ارشد در دولت ترامپ اعلام کرد که امضای توافق امروز مورد انتظار نیست و هنوز چندین جزئیات باید حل و فصل شود. هنوز در مورد برخی جزئیات رفت و برگشت وجود دارد، برخی کلمات که برای ما مهم هستند و برخی کلمات که برای آنها مهم است،»
این مقام ادعا کرد که سیستم ایرانی در پیکربندی فعلی خود به سرعت حرکت نمی‌کند و برای طی کردن تمام تأییدیه‌های لازم، چند روز طول خواهد کشید تا توافق نهایی شود.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16603" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یادداشت تفاهم آمریکا و ایران، طبق Axios:
تمدید آتش‌بس به مدت ۶۰ روز
عدم دریافت عوارض ایرانی در تنگه هرمز
ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد
آمریکا پس از برآورده شدن این خواسته‌ها توسط ایران، محاصره خود را پایان می‌دهد
آمریکا برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد
تعهد ایران به هرگز دنبال کردن سلاح‌های هسته‌ای
ایران متعهد می‌شود مذاکراتی درباره تعلیق کامل برنامه غنی‌سازی هسته‌ای و حذف ذخایر اورانیوم غنی‌شده خود برگزار کند
آمریکا متعهد می‌شود مذاکراتی برای رفع تدریجی تحریم‌ها علیه ایران و بحث درباره دارایی‌های مسدود شده ایران برگزار کند
آمریکا هیچ نیرویی را از اطراف ایران خارج نخواهد کرد.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16602" target="_blank">📅 18:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دونالد ترامپ در تروث سوشال:
یکی از بدترین قراردادهایی که کشور ما هرگز منعقد کرد، توافق هسته‌ای با ایران بود که توسط باراک حسین اوباما و آماتوران رده‌بندی شده در دولت اوباما ارائه و به وجود آمد.
این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. اما نه در مورد معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است - دقیقاً برعکس! مذاکرات به شیوه‌ای منظم و سازنده در حال پیشرفت است و من به نمایندگان خود اطلاع داده‌ام که در آن زمان که زمان به نفع ماست، به سرعت وارد معامله‌ای نشوند.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت و اثر باقی خواهد ماند. هر دو طرف باید زمان خود را بگیرند و آن را درست انجام دهند. نباید خطایی رخ دهد! روابط ما با ایران به یک رابطه بسیار حرفه‌ای‌تر و پربارتر تبدیل می‌شود.
با این حال، آن‌ها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه یا تهیه کنند. من می‌خواهم تاکنون از تمام کشورهای خاورمیانه بابت حمایت و همکاری آن‌ها تشکر کنم که با پیوستن آن‌ها به ملت‌های توافق‌نامه‌های تاریخی ابراهیم، بیشتر تقویت و تقویت خواهد شد و چه کسی می‌داند، شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16601" target="_blank">📅 18:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.  به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16600" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSirus</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbk6Qc7mWIwrfY3dEU9qVF1H5pDnLCtqkU1X_eHCM1DDFCdVRpZsJKPNMwPozpk8N0pfu2mHdAEG7R16L-A7jsF4ukOCsO7fxH3ga9PWTYJ8Gh9meCaySyDjQQ5fdtVqk_7qZkKMrON0REd9HFq39LMkBB13aqEAgfhqfWaa87HUh0Xt3CRtxB-7hV1FCr0wJJewjOetReGeLbIfAdqWjN7E4prH3TPs7xnoB3VBUSx6N3TVENoy3CGdvd6tzrFbhbS-SMEhqBy8NzvMb7J6LeRRlg0itL6j6stcp5jO-SoyBHcY18s9HS-M5wUzmSQMKLxgD9VYMkqN1hbJvLktgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر چقدر مظلوم بود و هست، چند سال پیش رفتم و هنوز آثار جنگ با صدام باقی بود!
یاد تکاوران ارتش و نیروهای مردمی گرامی
و یاد زنده یاد سرگرد خلبان محمود اسکندری و کابین عقبش ستوان اکبر زمانی که با انهدام پل اروند عقبه لجستیکی صدام رو قطع کرد و مهمترین نقش در آزادی خرمشهر داشت؛
خرمشهر را خدای محمود اسکندری آزاد کرد...</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16599" target="_blank">📅 15:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسئول اسرائیلی:   ترامپ به نتانیاهو گفت که توافق نهایی با ایران منجر به خلع سلاح برنامه هسته‌ای و حذف تمام اورانیوم غنی‌شده خواهد شد</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16598" target="_blank">📅 15:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16597" target="_blank">📅 15:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16596" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16595" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.
به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق یک مکانیزم آزاد سازد، اما اکنون از هرگونه پرداخت از پیش خودداری می‌کند.
تسنیم هم گفته  که اگر مانع‌تراشی ایالات متحده ادامه یابد، هیچ تفاهم‌نامه‌ای امضا نخواهد شد.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16594" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر حادثه تیراندازی چند هفته پیش در آن سالن را هم حساب کنیم، ترامپ دو‌ بار خودش مورد سوقصد قرار گرفته و یک بار هم افشاگری درباره ترور دخترش مطرح شده!</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16593" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16592" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
اعتراض نتانیاهو به دو بند از توافق ایران و آمریکا
🔹
نتانیاهو جلسه‌ای در مورد توافق احتمالی آمریکا و ایران برگزار کرد.
🔹
به گفته شبکه تلویزیونی کان اسرائیل، نتانیاهو به ترامپ گفته است که نگران دو بند از این توافق است.
🔹
یکی از بندها مربوط به آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16591" target="_blank">📅 14:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdx7yLlPhmdn1GMe8BgshyOdKvYZote0MSqhR98DLOVqtw2Ybs-0RLXlfDwANKvClmZXy2zlX6zpxAIxDJSDacP-NrLSAJGnnRhozyWByflFTC0J_G4cgRUa0l9MB-atumMvkfbFe_wXqF_n6vZVITWxjgkcdZjGimioZmegxTv4p7xQJ2JXngjIqF2gKtMuJk3lxlDkYxlDFoyNDYEYMJqXuKOjUMQCV601uRJ52M9mfrG_cWfYDvjKq8-ZegbXiQvlv1qaFLAlqonrEyWXzVuknkgN7Da-9daE78E8GYyjQocIgebRWV6hxvN8JDxuMT2WiIMr7fDq0-G32oFSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16590" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16589" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک مقام ارشد ایرانی روز یکشنبه به رویترز گفت که تهران با انتقال ذخایر اورانیوم غنی‌شده با خلوص بالا به خارج از کشور موافقت نکرده است.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16588" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16587" target="_blank">📅 11:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16586" target="_blank">📅 10:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از روند مذاکرات
توجه کنید که این گزارش پیش از توییت شب گذشته ترامپ منتشر شده است
آخرین پیشنهاد متقابل ایران
تمام خواسته‌های کلیدی ایران از جمله برداشتن «تهدید آمریکا علیه ایران»، تسکین مالی، و «حق» ایران برای مدیریت تنگه هرمز را در اولویت قرار می‌دهد، در حالی که تلاش می‌کند مذاکره درباره برنامه هسته‌ای ایران را به تأخیر بیندازد. پیشنهاد ایران ارزیابی مرکز مطالعاتی (CTP-ISW) را تأیید می‌کند که حکومت ایران معتقد است در حال برنده شدن در جنگ است و از موضع قدرت مذاکره می‌کند.
آژانس خبری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی (IRGC)، در ۲۳ مه ۲۰۲۶ گزارش داد که پیشنهاد ایران به میانجی‌های پاکستانی ارسال شده است. ایران خواستار پایان جنگ در تمام جبهه‌ها، از جمله در لبنان، و خروج نیروهای آمریکایی از «منطقه جنگ» شده است. برداشتن «تهدیدهای آمریکا علیه ایران» به معنای خروج آمریکا از منطقه خواهد بود که هم اهرم نظامی آمریکا را حذف می‌کند و هم یکی از اهداف کلیدی ایران، یعنی اخراج نیروهای آمریکایی از منطقه، را محقق می‌سازد.
در این پیشنهاد، ایران درخواست کرده است که تا زمانی که جنگ پایان نیابد، برنامه هسته‌ای خود را مورد بحث قرار ندهد، از انتقال ذخایر اورانیوم غنی‌سازی‌شده (HEU) خود به ایالات متحده خودداری می‌کند و تعهدی برای برچیدن تأسیسات هسته‌ای خود نخواهد داد؛ همه این موارد از خواسته‌های کلیدی آمریکا هستند. آمریکا در فاز اول هر توافقی، اهرم قابل‌توجهی را از دست خواهد داد، قبل از اینکه حتی درباره موضوع هسته‌ای مذاکره کند. این پیشنهاد همچنین شامل خواسته‌های ایران مبنی بر لغو تمام تحریم‌ها علیه ایران و آزادسازی تمام دارایی‌های مسدود شده ایران در فاز اول است.
ایران در این پیشنهاد تأکید کرده است که تنگه هرمز تحت نوعی کنترل ایرانی باقی خواهد ماند و اگر آمریکا محاصره بنادر و کشتی‌های ایرانی را پایان ندهد، مذاکرات را ادامه نخواهد داد. شرایط ماکسیمالیست در این پیشنهاد نشان می‌دهد که حکومت ایران معتقد است از موضع قدرت مذاکره می‌کند، زیرا خود را پیروز جنگ می‌داند.
مقامات ایرانی
همچنان بر مدیریت ایران بر تنگه هرمز به عنوان یکی از نقاط چالش‌برانگیز در مذاکرات تأکید می‌کنند. سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، در ۲۳ مه اعلام کرد که تنگه هرمز «به آمریکا ارتباطی ندارد» و ایران و عمان باید به عنوان کشورهای ساحلی مکانیسمی برای این آبراه تعریف کنند. روزنامه نیویورک تایمز در ۲۱ مه گزارش داد که ایران و عمان درباره سیستمی برای دریافت هزینه از کشتی‌ها به عنوان «خدمات دریایی» به جای عوارض عبور بحث کرده‌اند. این اقدام بر اساس قانون بین‌المللی دریاها غیرقانونی است.
آژانس خبری تسنیم، وابسته به سپاه پاسداران، در ۲۳ مه گزارش داد که ایران خواستار شده است که تنگه هرمز به مکانیسم و «رژیم حقوقی» پیش از جنگ بازنگردد. تسنیم اضافه کرد که ایران خواستار پایان محاصره دریایی آمریکا شده و اعلام کرده است که مذاکرات تا زمانی که این محاصره برقرار باشد، پیش نخواهد رفت. آژانس خبری فارس، وابسته به سپاه پاسداران، نیز گزارش داد که ایران تنها متعهد به بازگرداندن تعداد کشتی‌هایی خواهد شد که از تنگه عبور می‌کنند به سطح پیش از جنگ است، در حالی که ایران تعیین خواهد کرد کدام کشتی‌ها مجوز دریافت می‌کنند و باید از کدام مسیر عبور کنند.
ناوگان سپاه پاسداران در ۲۳ مه اعلام کرد که ۲۵ کشتی در ۲۴ ساعت گذشته با دریافت مجوز و تحت هماهنگی و تأمین امنیت ناوگان سپاه از تنگه عبور کرده‌اند، که نشان می‌دهد ایران سعی دارد خود را به عنوان مدیر و تأمین‌کننده امنیت عبور از تنگه معرفی کند.
دونالد ترامپ، رئیس‌جمهور آمریکا
، در ۲۳ مه اعلام کرد که تا ۲۴ مه تصمیم خواهد گرفت آیا حمله به ایران را از سر بگیرد یا خیر. یک مقام آمریکایی آشنا با مذاکرات به آکسیوس گفت که مذاکره‌کنندگان هر روز پیش‌نویس‌ها را رد و بدل می‌کنند، اما پیشرفتی حاصل نشده است. ترامپ گفت که شانس رسیدن به توافق با ایران یا از سرگیری حملات «پنجاه-پنجاه» است. ترامپ در ۲۳ مه با رهبران منطقه‌ای برای بحث درباره آخرین پیشنهاد ایران گفتگو کرد. یک منبع نزدیک به مذاکرات به واشینگتن تایمز گفت که انتظار می‌رود آمریکا و ایران تا بعدازظهر ۲۴ مه اعلام نهایی پیش‌نویس توافق برای پایان جنگ در تمام جبهه‌ها را اعلام کنند. ترامپ گفت که او تنها توافقی را خواهد پذیرفت که به مسائل کلیدی از جمله غنی‌سازی اورانیوم ایران و ذخایر اورانیوم غنی‌سازی‌شده آن بپردازد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16585" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16584" target="_blank">📅 09:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در ۳ روز گذشته:
— افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی
— تیراندازی و ترور در اطراف کاخ سفید
— دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16583" target="_blank">📅 09:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله انتحاری در ‌کویته پاکستان  ۸ نفر کشته و ۳۰ تن دیگر زخمی شدند  انفجار قوی در نزدیکی یک مرکز امنیتی که مشرف به ایستگاه قطار است، شهر کویته را لرزاند.  منابع بیمارستانی گفتند که ۸ جسد از محل حادثه انتقال داده شده و ۳۰ نفر دیگر نیز زخمی هستند.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16582" target="_blank">📅 09:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16581" target="_blank">📅 09:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sylxu_Y39MLf463wV6r1OkS5Ud-sahMxMgY6QPp9wJ-IpnOstutw8yDhPrye72TexPTtXt7qj7wFQvkw0OTywGe_m-DJ_jOfI-YsBrRXcSq6d8D1No1tZpMS7t7aNMK0MTVri0m4DEwCVLYyv4QJZ1ZYhqwDic9oIhgSPD6u8N0EhargcLjOCbm0j5hYlAiKNHiW-Qr6lLqUWScB10FPm7EA_KntyCiIPirw14mPn-5pjVyKzm69khTooDeotC0fcTklDD5kF5e4rNjmqKnTlLKMj7QGIjkLwp-_yk-xgqzE9-N34qwJOL5jXw32Wb2z_c8yUESOeWNx_lhSxivK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاهک موشک اورشنیک روسیه تا 4000 درجه حرارت می‌گیرد که می تواند فلز را ذوب و بتن را تبخیر کند و خودروهای زرهی را فوراً نابود کند.   برای اینکه دید بهتری از قدرت ویرانگری این دما بدست آورید اینجا میگویم که چگونه این دما با سایر منابع گرمای شدید مقایسه می شود؟…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16580" target="_blank">📅 06:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16579" target="_blank">📅 06:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewwyamLoRCt10muksx6t20b-2PlheVCf4VG4oHuS-saXiIR7q3xCPdSFwYxKJWrhFenmkCBvxUCG91Oymb14o4_VczbGny-vfkGaz3HvBHSUdkNM5-tPCCZBtTZqGGd6hc5ZosbWbgNld3rDCBAWXgVdvcam0ZnwOUL3hGzKwT3gKP2tipmUe0_hgDSN9ZA8MXwIYjduSOjocboRsPWU2ifvANuN3NUyNdf8yhVifzk19OnnxAoFIaIBEoFqiWBSj3afWtMaije-0z_LrM2kTpGm5ikWQ7hyvNwZ0wmFwgY3VEbVuAfnKLNSrSlWUZr6BZv91PSVa5waJ0T2mLhqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس مخفی ایالات متحده بیانیه‌ای در مورد حادثه تیراندازی در اوایل بعدازظهر امروز در نزدیکی کاخ سفید در خیابان ۱۷ شمال غربی و خیابان پنسیلوانیا شمال غربی در واشنگتن دی‌سی صادر کرده است:   پس از اینکه فردی سلاحی را از کیف خود بیرون کشید و شروع به شلیک کرد،…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16578" target="_blank">📅 06:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16577" target="_blank">📅 06:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هاآرتص درباره افسرانی که در لبنان می‌جنگند:   وضعیت ناامیدی در میان ارتش به دلیل افزایش تعداد تلفات ناشی از تجمعات حزب‌الله گسترده شده آن هم در حالی که ترامپ اجازه عملیات در بیروت و دره بقاع را نمیدهد و عملا ما فقط خانه های روستایی را منفجر می‌کنیم!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16576" target="_blank">📅 06:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انتشار داستان طرح ترور ایوانکا ترامپ و همینطور حادثه دیشب نوعی پیام هشدار به ترامپ است.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16575" target="_blank">📅 06:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">واقعاً طرح پروفسور شریعتمداری جواب داد؛  اکنون که تنگه باز شده دیگر وقت ترور ترامپ است.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16574" target="_blank">📅 02:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16573" target="_blank">📅 01:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توافق صلح آمریکا با ایران شامل بازگشایی تنگه هرمز، پایان محاصره، آزادسازی ۶ میلیارد دلار از دارایی‌های مسدودشده ایران و خروج نیروهای دریایی آمریکا از اطراف ایران است</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16572" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16571" target="_blank">📅 01:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/16570" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYT7HX5AnWpV6dTPKvrsB0C867LxzYcPEpLtNfDmAtZ2dAIurcWH4uDuMEpNvC1rJ51kxCgpCplFZxlJ6VFgXG0EwYZEW_DjCkh0Z0563HdQbusVpU8NiVBdbV3tlcDbAM35cSyH5Z_AtF3ZekV0qNOicUnOKuw9w1yQuHE86Y0hF1NoYIkYXgD8v9Tt2KT2hne1K-HRG54vuda7cypWB32E2YqA7x-n2rxDvIlsRGfpV-Pqhydu8A7y_PAxWGhvxPRpPh0l3f_Mr-TgDEw2WxdarxhGE5SWEfFBS1rekJrgLRGNHCOWfPbEkaHlw5fgQjz8Wyyl7dj9KWapy7UX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16569" target="_blank">📅 00:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD6XppaX0uIxT41qU3FE9sLYhzfjYfysZ2k1iSyetTEvqTryYqs7WXoyc6Ycxlchnc7tRcEnzbhvU89xIoPOQf_n77ZElNP9g4kELMasms579g5fvn1YvJ2TbgGzRyeIESI0RN-VfZNNb-Qj8Uc_svxhnLdc9bjQ3chUYIk9J1sAKxCZFrg0fP_Chng1wboDOmmkgqXjDolMRZ_Yc2nvyK7f8XVWS7uhk4BcPsQbKyeABUzXApIHBFiA6PBXK_ilTRcytO6HPlKofQxAcVnrbxAPsoqLGgw0c0OxxTeOyq2yr81dn-7_bRyLD51BnXsKsMH3NmJEhYb8LMVl_jXIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...
سبحان الله!</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16568" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:  من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16567" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان اندازه خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/16566" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
۶۰ روز تاریکی
❌
🟠
۶۰ روز از شروع عملیات نظامی ایالات متحده و اسرائیل گذشت و اینترنت که از ساعتی بعد از آغاز تهاجم قطع شده بود ، کماکان در خاموشی مطلق به سر می‌برد و با طبقاتی شدن روند استفاده آن ، شکل و شمایل یک اینترنت با حیات نباتی را به خود گرفته است…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16564" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
ثابتی ؛ نماینده مجلس
:
جنگ نظامی مجدد قطعی است ،  حتی اگر آمریکا تسلیم شود</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16563" target="_blank">📅 22:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">—مقامات اسرائیلی به آکسیوس:
« نتانیاهو نگران توافق مورد بحث است و از ترامپ خواسته است تا دور دیگری از حملات را آغاز کند».</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16562" target="_blank">📅 20:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ادعای جدید روبیو درباره مذاکرات:   شاید خبری باشد، شاید نباشد!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/16561" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👽
ذکر نام "ایران" در اسناد جدیدی که وزارت دفاع آمریکا از پرونده های UFO منتشر کرده است :
4 شیء ناشناس پرنده به صورت گروهی 26 آگوست 2022، روی آبهای ایران مشاهده شدند</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16560" target="_blank">📅 19:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
تقی پور ؛ نماینده مجلس
:
جمهوری اسلامی ایران می‌تواند کابل‌های حیاتی فیبرنوری جهان را قطع کند</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16559" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idhTsmsOIO-_s1ccpEE_n18rEKGBsY4plm--Vgn1ApGvuTVOT_4J9Xwzjx6vyp9DhMtj65Xrij_4ywoDAqHxkpGxB76A0wEoqcPQtjQXebl_Ggg_OHFFanhlNK4xBWLBL-8Fq0WQGjqYwMhHY5lZr18LfXpwGrgTIOPPWRQHE_W6um7sCSS4D-Yhb_hW0EI1q90zY011B7p-YYe0zLplsXCqCGg74qK8SQ4xl18OxhzAxFaNFLmZpJOVcYcKFSNTc6obi7AoILjgDskN_brwJ0z6iTQtrIn6fkJfmBLgvg0zrxH-2VDCAl4S5VnNVtGRPcva_3BiVQh9QKuRduoKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16558" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16557" target="_blank">📅 17:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، به زبان عربی:   اگر دندان‌های {آرواره}  یک شیر را باز کرده ببینید، فرض نکنید که شیر در حال لبخند زدن است.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16556" target="_blank">📅 17:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7S_FBgZr69jVOlcorQgzfBgX9nBIdTVmHehJ0gXG5gsVmuuNeZq0CwkWTq1E6aXmqngpXM22ymcze83tbEYZZ2QwMJlvb88sTEHvfoiKHvwXAz1wKXXcto28aMMnfK4xKsLb8AufF52DBwPBevrMQ7LjTgDxoiXOokaPJtNs948EiBZnCy1InyrV_R1uDqlqbRPgdyfChBTmfn9pyvoIeTPeQmfXyPOSnDn4OCRHzyyx3z_xsblDtm9Yqc1szrbspcDw2TxUnCafgqIgU0Ua_LtsKzL7gCYFjtk-ojORTOHIvj3oVNk_QturfPTZmbfIrnBWL9FgHvTkflrSwxg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16555" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16554" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16553" target="_blank">📅 17:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">—یک مقام ایرانی به الجزیره:
«ما با میانجی پاکستانی به یک تفاهم‌نامه رسیده‌ایم و در انتظار پاسخ آمریکایی هستیم.
تفاهم‌نامه شامل پایان جنگ، برداشتن محاصره، باز شدن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه مسائل هسته‌ای را شامل نمی‌شود زیرا پیچیده هستند و زمان کافی برای مذاکره نیاز دارند. پس از ۳۰ روز از توافق، دربی برای مذاکرات هسته‌ای می‌تواند باز شود.
پیش‌بینی شده بود که رئیس ستاد ارتش پاکستان تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی با واشنگتن رفت.
برای ایران امکان‌پذیر نیست که امتیازات بیشتری نسبت به آنچه در تفاهم‌نامه مقرر شده است، بدهد».</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16552" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nToYM33vqsqZhpawpc20VtCnYEJIetGi2x7lbe1_CXaQ1G6ZAG7eis7QBV51O21jJmKNIYkSibCtZo_-nyoaDfBC-mVc-7rzVpONdp8ujELdNI6MEWsDnRSjlVTv3p0yeUBfgswtKS7rfQiQ_LPddCHtgRbZ5oYxDRAwihwvWF0FLsWMN7FshudiWaBJZI9BvDPN2PNCTvguqLRFHo470LADE2tGFKo3Lzp5OYiGe5rXDjDUMlA2if_XKQuGtQI2DKOC7pWXBfRJXmy0OUlG3sOaBxgVF-twEDqWx5dDDJjR8aVCfP5VPHKOReab3bFt1Shm5toiyzLd96N8I6QozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16551" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpkxtJsI1k5bc4uIBsVbaoZE2EmRz42jgzp0ayXOT0Pw1d0ZslJKkJHvxcexf_aae0vW1O-vchoIr8xRNlY0vkvTYvPGHKJFcA2tnCTQKw0FLVuek0JwmITYCEl8Lkt84QPA1MXnGjeI_JHGV6049Qs9_CWoDpJtyR1oRlEmrwFG0OMuDZqiBfYGo53L4OcXnQS4Uwe3eomPSvtcIVYncd1UOOPX0vu1dOg6ep2QfjmLNCrpgI_5tYRFV410wQrh_5LsCXFHz-HGN-1LOvp2ETA5Kt5v5nC_qjb9nLIqgdIMwqxyFJC5ThvlEZoFWxp6ZYkg8_RiREkzNHpLju-ZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید واگرایی میان اقتصاد اروپا با آمریکا پس از جنگ ایران
داده‌های اخیر PMI نشان می‌دهد اقتصاد آمریکا همچنان در محدوده رشد باقی مانده، در حالی که اقتصاد منطقه یورو به‌ویژه در بخش خدمات وارد فاز انقباض شده است. این واگرایی می‌تواند در ماه‌های آینده به یکی از عوامل اصلی جهت‌دهنده بازار ارز، سهام و اوراق قرضه تبدیل شود.
در شرایط افزایش تنش‌های ژئوپلیتیکی و رشد هزینه انرژی، آمریکا به دلیل استقلال انرژی و عمق بازار داخلی مقاومت بیشتری نشان داده، اما اروپا به‌دلیل وابستگی بالاتر به واردات انرژی آسیب‌پذیرتر شده است. تداوم این روند می‌تواند به تقویت دلار، فشار بر یورو و تغییر مسیر سیاست‌های پولی بانک‌های مرکزی منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16550" target="_blank">📅 15:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16549" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کارمای اجدادمان که سهل است، کارمای قابیل دیوث را هم سوزاندیم در این زندگی</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16548" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صبح تا شب این وضعیت مجریان ماست در سداوصیما ، در ماهواره هم که فقط صحبت جنگ و حمله است، نت هم با گیگ ۵۰۰ هزار تومانی باید برویم تانکرترکرز و فلایت رادار و اکانت کله زرد پفیوز و حساب محمد something های وطنی را چک کنیم ببینیم کی جنگ بعدی می‌شود!
بعد این نکبتهای انگیزشی میگویند بیدار که شدی به دنیا لبخند بزن!
به … عمه تان لبخند بزنید قرمساق ها</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16547" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16546" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N56vYTgAfTjnOdp5zy4hAFli86Kxt2V9izHPpv-Zir1PjKK2LI9fcx3RkVeFx1G0dThXbT2tMlGiUMyG-wesBV8XaLosedTPbGpJQW83NkzKg9iRKK2fvgeD9dpq_GQDLTnsjk-g1q3P7ajr9WpJdkJ9JDVn8TODUkW9ISElAJf4cjn8PCjnvxBoaiXRN5yCwXxcGCtyk9hXT494VX0sm1P5K-A78-tRbKkmmfVzccPRo_4kNYZ9ZrBvmp5acNDZ_wfF8pe5oiEEgi59nNB7sqzTmWJzteBy6DI6hWoYaHM0Tx7cpBuIVZKGyqldviw7b-MvxAhrBCDXXguCJwxrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16545" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ اسرائیل را از مذاکرات ایران حذف کرده است!
به گزارش نیویورک تایمز، این واقعیت که اسرائیل «تقریباً به طور کامل از حلقه مذاکرات آتش‌بس» بین ایالات متحده و ایران خارج شده است، به یک «شکست خوارکننده» برای بنیامین نتانیاهو، نخست‌وزیر اسرائیل تبدیل شده است
نکات کلیدی:
🌏
دونالد ترامپ بیبی را به عنوان متحدی از ایالات متحده می‌بیند، اما نه به عنوان یک شریک نزدیک در مذاکرات با ایرانیان
🌏
اسرائیل از شریک برابر کاخ سفید به «چیزی شبیه به یک پیمانکار فرعی برای ارتش ایالات متحده» تنزل یافته است</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16544" target="_blank">📅 14:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ژاپنی‌ها آمپولی ساخته‌اند که می‌تواند عمر گربه‌ها را تا ۳۰ سال افزایش دهد.
یکی از دلایل اصلی مرگ‌ومیر حیوانات خانگی پیر، بیماری مزمن کلیوی است. به مرور زمان، پروتئین AIM که باید بدن را از زباله‌های سلولی تصفیه کند، به سادگی از کار می‌افتد.
اما دانشمندان تزریق‌هایی با AIM مصنوعی ساخته‌اند که مستقیماً تصفیه کلیه را تحریک کرده و با سموم مبارزه می‌کنند. این تکنیک حتی در گربه‌های بسیار بیمار نتایج قدرتمندی نشان داد.
انتشار جهانی این دارو تا سال ۲۰۲۷ پیش‌بینی می‌شود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16543" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📡
وزیر ارتباطات دولت
:
این نگاه قیم مابانه که اینترنت را خلاصه در ۲ پیام‌رسان داخلی می‌داند و برای مسیر اینترنت مردم خط کشی می‌سازد ، نگاه قوه عاقله حکومت نیست</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16542" target="_blank">📅 13:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.  البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب  از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16541" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">استعفای تولسی گابارد: ایستادگی در برابر از سرگیری جنگ با ایران؟
تولسی گابارد ممکن است به دلیل سرطان همسرش استعفا نداده باشد، بلکه به گفته مجری TYT، چنک اویغور، به خاطر امتناع از همراهی با برنامه‌های ترامپ برای از سرگیری جنگ با ایران این تصمیم را گرفته است.
ت.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16540" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هیئت قطری که انتظار می‌رفت حداقل تا روز یکشنبه در ایران بماند، دیشب پس از دریافت دستور فوری، ایران را ترک کرد.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16539" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.
البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16538" target="_blank">📅 08:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.
اما جنگ اصلی برای چند ماه بعد خواهدبود.
در واقع این جنگ کوتاه را می‌توان یک موج B درنظر گرفت که از سقف موج ۳ ظاهرا فراتر می‌رود اما هنوز بخشی از موج ۴ است
سبحان الله!
این هم نتیجه مکاشفات و مطالعات ما با گیگ ۵۰۰ هزار تومنی در روزهای مثلا تعطیلات!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16537" target="_blank">📅 08:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsYt1YF7ByUBJd2W-RzGaviiJ_rBtHCOuq-Y-eaMD5ZkcCleXhV60XA_GESftp87f_1u6GS0OxbkfFdXiOfgRqOpy8V95ExezjZupwpKkygN_-UOMt-P6_kLUfm2vILpJD4Wx0dEarLZWXzmBFINONKexQwEYa3j_W6TYrzIwfCUwZgVNAtyUkm_k5M1TsK_iUYBZSX88hGIuQEL96AsXjBWPJGKOp3EWiOLhuC8sABof-2B1pPhb06DW9jKtrNPjIsUUICQBOHMqymTTCl7ngNBf059cAlukhMsHM0aoDczMzhzy-DyA8AlpBkzwUvkMSkvKykydQTh25LTe1C8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری ایالات متحده دستگیری محمد باقر الصعادی، چهره ارشد در گروه شبه‌نظامی عراقی کتائب حزب‌الله که توسط ایران حمایت می‌شود، و انتقال او به خاک آمریکا را اعلام کرد.  طبق این بیانیه، الصعادی حملات علیه منافع ایالات متحده و اسرائیل را هم در داخل ایالات…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16536" target="_blank">📅 07:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM08AJ8sag0VC1Dxh8V8COW1TPMJqIxVHPOF2SmvF-l1gvdTpFdIkrTUE25QVHPRL4uh7h8SR6I3kG36m-EztOFjuWV6qh93V_q0NYQXTS1sMPusonguUSoofwetQX7xAg4XMRhpJWxDtypzauRgsm3G6HltZzkvI1hMEEWKUIAHzGnTnNSzceNxJV9PbVH7SHta66wnCwOHb93QAPXsXZFERwFcmrMbIln2G4Mf3QrX2GN-PDUWuBQ1gdM-GFvtYUKNtohyHgkCxRe2vsFJixF_e1JgkkV62zCVLTRLWeLAZuODY7YMHw_jAlMvm584r3Gyb0vLb3aSHPVQZ0tLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌بی‌اس در یک پیام فوری اعلام کرد که دولت ترامپ در حال آماده‌ سازی برای احتمال دور جدیدی از حملات علیه ایران است.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16535" target="_blank">📅 05:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک مقام آمریکایی که در جریان تلاش‌های دیپلماتیک قرار دارد، مذاکرات را «رنج‌آور» توصیف کرد. این مقام گفت پیش‌نویس‌ها «هر روز رفت و برگشت می‌کنند» بدون اینکه پیشرفت قابل توجهی روی بدهد.
یک منبع نزدیک به رئیس‌جمهور آمریکا، ترامپ، گفت که ترامپ در چند روز گذشته به طور فزاینده‌ای ناامید شده و احتمال یک عملیات نظامی بزرگ نهایی را مطرح کرده است، پس از آن ممکن است پیروزی اعلام کند و جنگ را پایان دهد.
میانجی‌ها در تلاشند تا یک توافق موقت بین ایران و آمریکا را تضمین کنند تا از حملات جدید آمریکا و اسرائیل که مقامات هشدار داده‌اند ممکن است ظرف چند روز رخ دهد، جلوگیری کنند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاشند تا اختلافات درباره برنامه هسته‌ای ایران، رفع تحریم‌ها و مسائل امنیت منطقه‌ای را کاهش بدهند.
هدف، توافق جامع نیست، بلکه چارچوب موقتی است که آتش‌بس را تمدید کند و اجازه دهد مذاکرات گسترده‌تر ادامه یابد.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/16534" target="_blank">📅 00:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWhsPTgONkdtNjZHbANl7qSXw6ok6hdt1QmyBtQKlO2X5YKDZ2wTAglU1QfwuG1ofJj7mHgsY9mHgElKb-AtX4ItlUBOw3ElnlmIVl_-bA_17z2kWfxH7St2e0PcXSsRrRSun5JbFBleWgPD7uGuTacOIhdzHd9e72GqsDX-8RluYsjc8MwpYCo9734jHL1zxDpsVzXbdqfiFBUnhaA9oxmgrDJlFO82VLYJjMDweHS6Q-MHsWbYK8txhY7Wq7C9vgunpRG2Weiwcn6vdV2gMyzekJtkPpW89vT2hqbANrSdaxOradOmGAKEc-VAAPcFjUIPuVjrK9I-sw5I-aP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کوین وارش رسماً به عنوان رئیس جدید فدرال رزرو ایالات متحده سوگند یاد کرد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16533" target="_blank">📅 00:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب به صورت رسمی از این طرح رونمایی شد.  در واقع در این طرح که حریم دریایی نهاد تنگه خلیج فارس نام دارد، عملا بخش‌هایی از دریای عمان هم شامل می‌شود که اساسا ربطی نه به خلیج فارس دارد نه تنگه هرمز و صرفا برای فشار خفه کننده بر امارات طراحی شده است.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16532" target="_blank">📅 23:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایران: آخر هفته‌ای بر لبه تیغ
۲۲ مه ۲۰۲۶ | پیترو باتاکی
مذاکرات درباره ایران همچنان ادامه دارد، اما اختلافات اصلی همچنان پابرجاست. قرار بود امروز ژنرال عاصم منیر، که بسیاری او را «حاکم واقعی پاکستان» می‌دانند، به تهران سفر کند، اما بنا بر برخی گزارش‌ها این سفر لغو شده است.
شکاف میان ایران و ایالات متحده همچنان بسیار عمیق است؛ به‌ویژه در موضوع برنامه هسته‌ای، انتقال ذخایر اورانیوم به خارج از کشور و همچنین مسئله کنترل تنگه هرمز. طی روزهای اخیر گزارش‌های متعددی درباره اختلاف‌نظرهای احتمالی میان واشنگتن و تل‌آویو منتشر شده است؛ گزارش‌هایی که حاکی از آن هستند که بنیامین نتانیاهو برای حمله مجدد به ایران بی‌صبرانه فشار می‌آورد، در حالی که دونالد ترامپ با احتیاط بیشتری عمل کرده و در تلاش است از طریق مذاکره به توافقی با تهران دست یابد.
با این حال، این احتمال نیز وجود دارد که چنین گزارش‌هایی صرفاً بخشی از یک عملیات فریب و انحراف افکار عمومی باشد؛ تلاشی برای پنهان کردن اهداف واقعی آمریکا و اسرائیل و فراهم کردن عنصر غافلگیری برای موج جدیدی از حملات که این بار قرار است سرنوشت‌ساز و تعیین‌کننده باشد. از این رو، به نظر می‌رسد آخر هفته‌ای بسیار پرتنش در پیش باشد.
در میدان نیز وضعیت تغییر محسوسی نکرده است. آرایش نیروهای دریایی و هوایی آمریکا نه تنها کاهش نیافته، بلکه در هفته‌های اخیر ده‌ها پرواز باری تجهیزات و تسلیحات جدید را به منطقه عملیات منتقل کرده‌اند. این جنگ هزینه‌های سنگینی به همراه داشته و فشار قابل توجهی بر ذخایر تسلیحاتی وارد کرده است. تنها در شانزده روز نخست درگیری‌ها، بیش از ۲۵ درصد از ذخایر موشک‌های تاماهاوک و حدود ۴۰ درصد از موشک‌های رهگیر تالون مورد استفاده در سامانه‌های دفاع موشکی تاد مصرف شده‌اند.
بر اساس گزارش اخیر مرکز پژوهش‌های کنگره آمریکا، تنها یک ماه جنگ حدود ۳۰ میلیارد دلار هزینه در برداشته است. همچنین ۴۲ فروند هواپیما، بالگرد و پهپاد یا نابود شده‌اند یا آسیب دیده‌اند که ارزش مجموع آن‌ها حدود ۲.۶ میلیارد دلار برآورد می‌شود؛ هرچند نویسنده معتقد است ارقام واقعی احتمالاً از این میزان نیز بیشتر است.
در سوی مقابل، ایران همچنان بخشی از توان فرسایشی خود را حفظ کرده و گزارش‌ها حاکی از آن است که در طول هفته‌های آتش‌بس، چندین شهر موشکی زیرزمینی را دوباره فعال کرده است. در چنین شرایطی، اگر جنگ وارد مرحله جدیدی شود، نمی‌تواند برای مدت طولانی ادامه پیدا کند و باید ماهیتی قاطع و تعیین‌کننده داشته باشد. در غیر این صورت، طرفین ناچار خواهند بود برای مدت نامحدودی با وضعیت کنونی کنار بیایند؛ نوعی «جنگ سرد» که در حوزه‌های اقتصادی، مالی و شناختی جریان دارد.
کنترل تنگه هرمز همچنان مورد مناقشه است و حجم تردد دریایی هنوز فاصله زیادی با شرایط عادی دارد. همچنین محاصره بنادر ایران که از ۱۳ آوریل توسط آمریکا آغاز شده، همچنان ادامه دارد. محاسبه ترامپ این است که ترکیب تحریم‌ها، محاصره اقتصادی و فشار نظامی در نهایت موقعیت مذاکره‌ای تهران را تضعیف کرده و ایران را وادار به عقب‌نشینی خواهد کرد.
محاصره دریایی به‌ویژه فشار قابل توجهی بر اقتصاد از پیش آسیب‌دیده ایران وارد کرده است. ظرفیت مخازن ذخیره‌سازی داخل کشور به حدود ۷۰ درصد رسیده و همین موضوع تهران را ناچار کرده است برخی نفتکش‌های قدیمی را به انبارهای شناور نفت تبدیل کند. طبق گزارش‌ها، دست‌کم ۵۰ نفتکش ایرانی در حال حاضر برای ذخیره‌سازی نفت مورد استفاده قرار می‌گیرند که نسبت به آغاز محاصره، حدود ۶۵ درصد افزایش نشان می‌دهد.
ترامپ بر موفقیت این راهبرد حساب باز کرده است، اما این رویکرد ریسک‌های قابل توجهی نیز به همراه دارد. زیرا تداوم این وضعیتِ «جنگی که رسماً جنگ نیست» می‌تواند پیامدهای گسترده‌ای برای ثبات اقتصاد و نظام مالی جهانی داشته باشد و در نهایت هزینه آن نه تنها بر دوش بازیگران منطقه، بلکه بر دوش شهروندان عادی آمریکایی نیز قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16531" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
