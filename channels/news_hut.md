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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 155K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 00:10:36</div>
<hr>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=K-aZbR-aQ74zMYxXV_-q37zjnLHiDWsbNNL5lif56PHACMw9kb9S3EDR4uaUT5qNPBGIIUgAQ1xGYlegPcU2W2IeuoViSO2SYlst6Wf-y20V4Hiqqi5_lDyfwAE5XLaslROSboZRO3DQB6iqG765J5OA0AcRrKpySjuyRFiEAhGqGm2noSoftENfMNs2eFd3_JeQt2i9vO_cGy-qlm9AT3iDYF-XY16YV4VRqfLc9GG6YwEr0Na9ulKNwey7wLAXt0aeiZqp6Q0Lig8owWgqU14QwDud-zFhqE7sSQwt6goV9ynpZVGPJmgnH6-AkTmHuDOFIkNcCvqX7-zrPJ4BoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=K-aZbR-aQ74zMYxXV_-q37zjnLHiDWsbNNL5lif56PHACMw9kb9S3EDR4uaUT5qNPBGIIUgAQ1xGYlegPcU2W2IeuoViSO2SYlst6Wf-y20V4Hiqqi5_lDyfwAE5XLaslROSboZRO3DQB6iqG765J5OA0AcRrKpySjuyRFiEAhGqGm2noSoftENfMNs2eFd3_JeQt2i9vO_cGy-qlm9AT3iDYF-XY16YV4VRqfLc9GG6YwEr0Na9ulKNwey7wLAXt0aeiZqp6Q0Lig8owWgqU14QwDud-zFhqE7sSQwt6goV9ynpZVGPJmgnH6-AkTmHuDOFIkNcCvqX7-zrPJ4BoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=nAp_-TdFKaAm0orm7ozjgGO-UmkDojDw_6HwnIANPrBpOf2MdZBAt7tUYVRtaVTN8ar2-Hs93hd1auEhkzo5GY5sYfx_D4OzG0HXG3N9xN_KJ03DTGlHQzFgIXu_ie5j04wMY1J_vx8Yt4R9kqZw9bB1Ve71_OZP0-06ygZMueyM6A3o59ZdkQqdRUlqVO_SFZmdUmXtkBX0Kzf2TFMusOlBI5hokRhB7f9q6s9te8ysYnNxABw1AyjGa3mngoVUiAVr_rMDQoWvRhCCvVIvICjf_5_AfCmfAQ7J2mbrdRKXEkN_IVw_9UHffAJU-pQ0eel4xAYYqUr84s5RkA2nzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=nAp_-TdFKaAm0orm7ozjgGO-UmkDojDw_6HwnIANPrBpOf2MdZBAt7tUYVRtaVTN8ar2-Hs93hd1auEhkzo5GY5sYfx_D4OzG0HXG3N9xN_KJ03DTGlHQzFgIXu_ie5j04wMY1J_vx8Yt4R9kqZw9bB1Ve71_OZP0-06ygZMueyM6A3o59ZdkQqdRUlqVO_SFZmdUmXtkBX0Kzf2TFMusOlBI5hokRhB7f9q6s9te8ysYnNxABw1AyjGa3mngoVUiAVr_rMDQoWvRhCCvVIvICjf_5_AfCmfAQ7J2mbrdRKXEkN_IVw_9UHffAJU-pQ0eel4xAYYqUr84s5RkA2nzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVfxZn7nMI13gY2NnOMQOELkusOnEWHjjyCIBkvaBnpfblVh-wIrIe5sSS72l-8ek90ilZpORgMmaIXXwsP3hM3O7TgEQcWTQB4kCIM6PNwgjvQwQ-wieVer-GHo85ZJJT7R7IRrgcsdVWvKMM-vb-H44J5aufKOdypri9z8ba7bB1L-pGKlrAcASORTuaYU7sYafLsdACXbFAzyVDdQZpB0Eq6aCAUoyYq0Hf_piCGZ6k0dCwNQbsnwB2jvmTJHqUsZ3wMM05_UQAt7AgXGNvRzQsfgRhTNprWqN6UGsX5y42PFDcC5KkLTGF_wwupnUnxagBjom5fPvremLmDp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uov9ySljvgi5h6e3mIHHq6Osi6dcrAc5jQUdk2_1oaVMBiMK1gf9Ju5iwXQaOTqudgvB6Bs1_5XhXWx8R9l__Tj0xYRgzbi0aA3GVKLxnD4YH1JD34g8iotTyidoJ3-FINFC6RbGUIK6hUCNywgKi06HTZEATXuJ8e06jxv-vlGSqFW56ZvtbEzX4NvwV_mo9H1N_mo3Fg9jPMs-Mr25RhZTmDUFMfybVeKFu9zWMAMpi8dc8BEYvvxo8IPwsWLwaDv1NoHHKFDAciELegnUrTl92qqrQElILbspmNRCmIrRGD5FY1vkviO2RYpozenTjsdLCqdoko5IvfPHXatM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=l9xjaHpPPVTrluKEd7uNMZhl47m572h-vn7sRSfwEtHRns2CGVbyScEw9SGvV0sY57_seK3ubwshfsBVhKnS1NbLnTV2fkcP6fPBgRctaxthVZH_L4P-icOYjU-8k2yGcwKFFhxHIhXnCW1F5D2__AcYxezC-Gvi4eGeyley3IGpRGKa--UjWbfi8g44SEIwe1JERVTcpMKhjfzT6NqU5K6s7PFYcMlh41qYevEbr0XROorMjs2oPIZH20Ao6ON1a3S7MIw3e8f_WOGZ099cKD7u0Nu9HCsEnSr2FdXB0M4wbOGiCNsITWXuX46xbczSez7JJP0x4r0r7tvcAhPhbBow71zz_h2t0FTOCuSpzeB3-D9fUrAJxZ_1BJ3O7uv3viKNg1VzW_kl758Ye2b_wqqZi6bK3b4Ekd6vd3WWTDSaD1jUi2eUloc4l0XJ6sdkQ5hEYy0ZH7Fr_Lco3p2UtTXNqs3x1whj8QyzKngXiefH1oSeoO2-KIb_AUQBZbakXuHsIxKIP1ZjsWNVRCvMmAD1hHsL9bpLvPll2UqSWPn7y8BGwYtY6bS27p8G2ujyWhTjCAFvmJD9hwNhoHe7AU7zoOMzCncj2f620BREBXhbSgeODXeUJqy_HWq_JBsxzP5mob8cpnfU_P0gT-S5nJVNFcnvdOLS-XYrOb3PQ9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=l9xjaHpPPVTrluKEd7uNMZhl47m572h-vn7sRSfwEtHRns2CGVbyScEw9SGvV0sY57_seK3ubwshfsBVhKnS1NbLnTV2fkcP6fPBgRctaxthVZH_L4P-icOYjU-8k2yGcwKFFhxHIhXnCW1F5D2__AcYxezC-Gvi4eGeyley3IGpRGKa--UjWbfi8g44SEIwe1JERVTcpMKhjfzT6NqU5K6s7PFYcMlh41qYevEbr0XROorMjs2oPIZH20Ao6ON1a3S7MIw3e8f_WOGZ099cKD7u0Nu9HCsEnSr2FdXB0M4wbOGiCNsITWXuX46xbczSez7JJP0x4r0r7tvcAhPhbBow71zz_h2t0FTOCuSpzeB3-D9fUrAJxZ_1BJ3O7uv3viKNg1VzW_kl758Ye2b_wqqZi6bK3b4Ekd6vd3WWTDSaD1jUi2eUloc4l0XJ6sdkQ5hEYy0ZH7Fr_Lco3p2UtTXNqs3x1whj8QyzKngXiefH1oSeoO2-KIb_AUQBZbakXuHsIxKIP1ZjsWNVRCvMmAD1hHsL9bpLvPll2UqSWPn7y8BGwYtY6bS27p8G2ujyWhTjCAFvmJD9hwNhoHe7AU7zoOMzCncj2f620BREBXhbSgeODXeUJqy_HWq_JBsxzP5mob8cpnfU_P0gT-S5nJVNFcnvdOLS-XYrOb3PQ9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTohZW8wjm2EtGsK0flKrBe-WwZgSuqttwSNHzjK8iFqTcxtnOYJYct-Z7ZmaSCI11Q7JcQXIE8b1Q6EBJyRknqDAvfAPIOgh9EBfTZ5F83FkDitKDVPCk7wO7qblziZT4i51j9oyfT30BCMOUvb83ogob9D4RvAiRpfFJ2CVE-1zY1uniuNJW9UuWiC-tKJbosNwkXCH9B2MEaHc5MlGxHqu8AcXNdFpcF4EPnBDm6oKqI-kVq-CoemDrRSRqbnAwyU98mkj7rruhjeCYuji-XKi8FTYgvCLrJNePnJI4-BWEeUxyV4mQVSAeBT-HI-KftOirAUUHcLdfY-p-8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_OqoopYPj8H8xYW6nqRttfG73Wr2W7oM758EkYYu_fFDhSdg3WoVtbX3JZdeyZMZZJY2jpojCroNY_QJzGiX7aFIoPhWEBEIAWvr0GAAja_sxIwIaHnNC75W30nDZY2M8_mWLrXXU5-x34XaD_mlnp9-Im8iOCrAJKotgyGrihgLkmnUTFeO_AUo0_L08Vq2vQXOJKlLD0bKdIj7Ii7-oNu2qXBMQBTOPeiDZfAsiPO-5jZbLMXxi8dt7MLNGZnoTxlHwgc2u1v7OPcqe2UGB6-DPLEdDskWJjZnegB2NytdVYxGvCKScRiK6KHAEzK6mEYCVr2hSmsMa3qfLaoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AD9yVaPI6UnIBgEgc1CH4WTut6R9vJdMCs-HCFhlr26b9oNATC4acEdLsNKNbfd4tiyjLOAOOy1s6XGQa0cv5Pl_BSvDuCYGflZm2vu8PNMTMoxOZMAOPL9U1kFnXKnposf3dh_hGtNYX-Tr3xw02ENjzgqyM5jLxypPwaKzjoZOKe-cCFv1DD9TljWemOlQUfyLYz4v6XtN2nW8kIQ8gDO9ey69I0OZ4QocMIqua6-P-ehLvNa2OZkDLdBEcaV2wOYlq8T1t8DnjIQUDk3Ae-LmPSDUGMMKfoqMI_JKN2nS1698Da4UhC1L4ZMw56zaaJqVFPjSZoTLzy6Cr9-dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=cCNhD1LpKg76DHq8lhAhImy1Fj5daSeRNrd3udsLqBx8zE56k999YCGdVPRIjgLWkhfdYzNz00ErYO-7l9h1Bo5Qt40B3moEpzEMjLTwW2aTdv_p-lR0zO42UORkTRLBeAzbezTaGhZ7m_MqaR3_RT2oPeIwLi8BvP9Dhll8CSrDXsjWRtR1gusK_IiWlKZ54GOXQmLiAw62V7TpT53lGez9D3UjkBJYciHVhQVdOOtFqH08qozo3vCpmroNmt0vAdtXOi1Els7a5NKnMX8iEqpM6rD8l5ObMIBYqgzrNWXB6h_TZgvJ-osDeEd_u6ukh18iTGattYx0i8Z1W_IIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=cCNhD1LpKg76DHq8lhAhImy1Fj5daSeRNrd3udsLqBx8zE56k999YCGdVPRIjgLWkhfdYzNz00ErYO-7l9h1Bo5Qt40B3moEpzEMjLTwW2aTdv_p-lR0zO42UORkTRLBeAzbezTaGhZ7m_MqaR3_RT2oPeIwLi8BvP9Dhll8CSrDXsjWRtR1gusK_IiWlKZ54GOXQmLiAw62V7TpT53lGez9D3UjkBJYciHVhQVdOOtFqH08qozo3vCpmroNmt0vAdtXOi1Els7a5NKnMX8iEqpM6rD8l5ObMIBYqgzrNWXB6h_TZgvJ-osDeEd_u6ukh18iTGattYx0i8Z1W_IIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=dWak3anlvwtulfuhyIYqjzwmyzkHnjZMsywcYRLa8V9WJpLW1wClxtyOV6x76cs9nqvQxntY8Mtz6vilJk7YvggQRxjVQYUB1NClFNvu5hmD1nXREho5wpOlYJ0blc57ez0GIFUxHWEqF9eyzbkNP80fF7SSq1siu-C_JpIQaLReC3kJzcudhwOdDTGc8CwUxSxdZa7SZkgkSRpwt5n08q9FP26VRFwinx2WPncx1Wm02ZgRbRk4PokOHAK7aZbq50x-pOqZVwU-uB0FuQ32GUqmPPxm39xAv5xtvs2HcvsfVz7ukGwQgcbnGvjPJ76tlQ-sDWApUVxoHYCPRDFFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=dWak3anlvwtulfuhyIYqjzwmyzkHnjZMsywcYRLa8V9WJpLW1wClxtyOV6x76cs9nqvQxntY8Mtz6vilJk7YvggQRxjVQYUB1NClFNvu5hmD1nXREho5wpOlYJ0blc57ez0GIFUxHWEqF9eyzbkNP80fF7SSq1siu-C_JpIQaLReC3kJzcudhwOdDTGc8CwUxSxdZa7SZkgkSRpwt5n08q9FP26VRFwinx2WPncx1Wm02ZgRbRk4PokOHAK7aZbq50x-pOqZVwU-uB0FuQ32GUqmPPxm39xAv5xtvs2HcvsfVz7ukGwQgcbnGvjPJ76tlQ-sDWApUVxoHYCPRDFFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-KuXPZluBTFKxYJQZr_XyPa5t_zVRpaNKUvYjVPHsdaUs4dibDIZxNyHiPdkDt8-fFQDEkZWiylzLu7UpGriW86wfa9V4KHO_xExXAhgG1I5vqYwLJmQ3ooNiLP4SSQyzOFbv9K6XOlhwz-tRBugKwA2moyho1GpEKUU-Ruy63j-guNMtzZbpgPinjUjQ6k9qbW1AiTLOwN3g3h7kKO9AXkl8HhcPJlZL7N3F4ruK39f6VdVT2kjga1WDgp9Ofp4xUsT3hybMFtoINHXyKNQUqKRFTLepa6EC-1gESxXP-QOc2lAgUNN_bGzfNGWSFPnU1urJlqbSSarOhQSrltVIu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-KuXPZluBTFKxYJQZr_XyPa5t_zVRpaNKUvYjVPHsdaUs4dibDIZxNyHiPdkDt8-fFQDEkZWiylzLu7UpGriW86wfa9V4KHO_xExXAhgG1I5vqYwLJmQ3ooNiLP4SSQyzOFbv9K6XOlhwz-tRBugKwA2moyho1GpEKUU-Ruy63j-guNMtzZbpgPinjUjQ6k9qbW1AiTLOwN3g3h7kKO9AXkl8HhcPJlZL7N3F4ruK39f6VdVT2kjga1WDgp9Ofp4xUsT3hybMFtoINHXyKNQUqKRFTLepa6EC-1gESxXP-QOc2lAgUNN_bGzfNGWSFPnU1urJlqbSSarOhQSrltVIu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=nrbm8W9IOtB56hVaQGSaUAHFqec8ciBigNdbv_p5WN7hVbijoRJOkxsppv1zHIQnw-xv7HgYQdgodNIeZW-K2_1XhQkYC265wAAAUBY2m1CGBkXPGLru_P1wwD4YDw2y-oNaUtviocVpmtwe_EdDM6_u8B3pEHqaqQqOjrOWOkPjuSkGznJKVOAyffe_aY-6p3QQHEIwmKEqyVBHYapXQmiu0WUSk6SIhj12q3CGTs9FpchvGI0LwXRiuV7HCjbmvAz-slJtKL06fhGqKUou08bDMlDuMI0jDErADmax4u7NJISmtE1Lyj02I9xdPuhv7LIYY7_YkynqWfywE0Yt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=nrbm8W9IOtB56hVaQGSaUAHFqec8ciBigNdbv_p5WN7hVbijoRJOkxsppv1zHIQnw-xv7HgYQdgodNIeZW-K2_1XhQkYC265wAAAUBY2m1CGBkXPGLru_P1wwD4YDw2y-oNaUtviocVpmtwe_EdDM6_u8B3pEHqaqQqOjrOWOkPjuSkGznJKVOAyffe_aY-6p3QQHEIwmKEqyVBHYapXQmiu0WUSk6SIhj12q3CGTs9FpchvGI0LwXRiuV7HCjbmvAz-slJtKL06fhGqKUou08bDMlDuMI0jDErADmax4u7NJISmtE1Lyj02I9xdPuhv7LIYY7_YkynqWfywE0Yt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=hreO0ZkEBSsJAiAByssxAXVj6nZzpkFxrcFMLIV_gSZemdAAdAISD_M3M3mxLupIr7Xb3NvtGkmZcJ6I8wf8dElm-PT9GMoowOM0RFNx0O4RqRpR9mgjb5R9xJQtRV6vgYKOFHSXI0EzCpYsnTH0iMMJ-CoFo6CmBIiTZTRhMxCiDgxM04glvshz60f4yd-6BfPLqfMKY_c_kHl_X1gBquu0ewXigVndWrsude2oKVNe9bWP4yYBk97qpqHh4VpaYCCQF8OGlWgjj3iIQc4qNfZDI1zJ6-u8bBH2MaPxANUXMWanKiH7PuU7QwZN1bl5vmYcayN9tfab0h6vOWTq-rOrK_Wn5YGDdU_1s958_TS6qGadr-HasRzNSgtzibcWSSjal6zEpMzkvNK905CJln3RBurffDmbvLHFlaFt42cHQYpdhtiojmpbkyB668lNHCYa-Jrjbr62wGpqsUMikovIOiB80kXE6XAirkNvJ-V0_NFkxvYmRKwmX5r_tIsQ1g23jEzNpSOFYxxW1yM2aaVXVCnEh8YzyeCXOkXaStxQatx-KKjvhbMEKcN50ZFvfDZE0aY2NJSoxpSACdqEVL7Exd79zd7ikB2IUb54JGVYs1cR1ouGejrBCRFW0LZQJU_b5i5Rq129S_W_YrBq0c-5QB7heIf-NiGpT7zpCzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=hreO0ZkEBSsJAiAByssxAXVj6nZzpkFxrcFMLIV_gSZemdAAdAISD_M3M3mxLupIr7Xb3NvtGkmZcJ6I8wf8dElm-PT9GMoowOM0RFNx0O4RqRpR9mgjb5R9xJQtRV6vgYKOFHSXI0EzCpYsnTH0iMMJ-CoFo6CmBIiTZTRhMxCiDgxM04glvshz60f4yd-6BfPLqfMKY_c_kHl_X1gBquu0ewXigVndWrsude2oKVNe9bWP4yYBk97qpqHh4VpaYCCQF8OGlWgjj3iIQc4qNfZDI1zJ6-u8bBH2MaPxANUXMWanKiH7PuU7QwZN1bl5vmYcayN9tfab0h6vOWTq-rOrK_Wn5YGDdU_1s958_TS6qGadr-HasRzNSgtzibcWSSjal6zEpMzkvNK905CJln3RBurffDmbvLHFlaFt42cHQYpdhtiojmpbkyB668lNHCYa-Jrjbr62wGpqsUMikovIOiB80kXE6XAirkNvJ-V0_NFkxvYmRKwmX5r_tIsQ1g23jEzNpSOFYxxW1yM2aaVXVCnEh8YzyeCXOkXaStxQatx-KKjvhbMEKcN50ZFvfDZE0aY2NJSoxpSACdqEVL7Exd79zd7ikB2IUb54JGVYs1cR1ouGejrBCRFW0LZQJU_b5i5Rq129S_W_YrBq0c-5QB7heIf-NiGpT7zpCzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Z65lrQSDwLEtLGA9JQ7Kuoraql0ih1mBnTsfoeysPS4Gy_M9CNBJuAwxFKsCzy7bAVOQLlmNv5-ykcDumYQFVELhPJhQ6uMJlpN3bTxjJYz2a-RoNjsUBmrMHTah2PHxmSa2E_n2xDIDr_Msnn22CdCgDco9mgmUoDmlNwcKp2mXjpjlzQjhf4bkbzF_jfiWLIvhn5BHGZGrRceKa-k6Osvq8vA2CmG07vniAVVrsUJZjxUS2pccDZ5Egp0aeh2qfN13DS1GHd-BaLukYuOtpF7NhZAi43wxhIcQxdRNmbFb_ch5bM_wLRlLt-B82BkRgMnYv5KDeiwrKSwmJUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYnNGZSy6NM0kxP6OWe_MWD1etk49zmBwZ9kqXY7RN0PfmtUZtz7VSgQhLqYMhxcVXa6l9WOiWqVBmLAbXAfzscTF7PC-aYo-jBTdIbI6rkII5S2Gl3n00fYNNBUH1x9EWbLKyigTfn4cTeJ_ylhDZEgtl6HMXRkJN5lXDt2aJbBFXJzRIIzVjO4vLBNiGjn_KqM48QkNVMWpKImTv4oNk4JwFqmxJ1vMOwTq4XOiVDe1hN4DCaLReP11T72-02Up22b13F1Lzjy2G5z_B2K9x-Ucb1WkRc7lxXNV0qJLWCLvkq8Qn2nJmwkBg224nh9Karjwnd2WANgGojAn0WEI34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYnNGZSy6NM0kxP6OWe_MWD1etk49zmBwZ9kqXY7RN0PfmtUZtz7VSgQhLqYMhxcVXa6l9WOiWqVBmLAbXAfzscTF7PC-aYo-jBTdIbI6rkII5S2Gl3n00fYNNBUH1x9EWbLKyigTfn4cTeJ_ylhDZEgtl6HMXRkJN5lXDt2aJbBFXJzRIIzVjO4vLBNiGjn_KqM48QkNVMWpKImTv4oNk4JwFqmxJ1vMOwTq4XOiVDe1hN4DCaLReP11T72-02Up22b13F1Lzjy2G5z_B2K9x-Ucb1WkRc7lxXNV0qJLWCLvkq8Qn2nJmwkBg224nh9Karjwnd2WANgGojAn0WEI34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-1Yp4S9Ue66-D7Ym2yCu2WPztDJS2Ixh2o0yNABCJCMuilRg7rVER7U9iD0EmVNL6y04Aw3_6NVpWDRFkru83L_xcx8PRf7P-AjUtGIV3ba8-sSCYFFdjDjpELSe5DsR7XCHdYTYUDtpwBAKhic0PD__n9nacdQEKWEOkarlE8im7jZpVfjtU7CJikj238E0Fb596MXQ54PvCE6mFXkiREpY12Pt0d3DEsoyd2SoTsW68U4kaebbul7VJ2Fx8D052prYSdSLGzaVoKHYQ3_hw8NJpwPNoMmgee59I5tuas3WUihUhP-ghh0vWEStBsnIrf6hYMyL08TmCEI_kERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/OEIPAJc9r5PWJSde1W_eGMIA6L8irXsSXx467Hz9SSkGTCO5am6C-ToJaY1CMpyNTiws06JiiL6BPfeF2qOvTHGEpa72JDQ9bmTm5noYrBRCeP989DxPKKV0pJJcgYCnoTPMeyozSXWh8ck80N-1qM_KfG-yH64uYTbJi_Cz5otoWs5ZZxfIyTQbv9DYFJZwupjmzai5A6u6nfrzmlbNh34lyyug23Dd_QDluwVMAJFYl0cR5v6PucxT3ExLzQGhz4e66Bj5OjxsH6vscNR4BfV8aQp4HZHFwQd47K-0o_A-gdX21uZbxHSjd3cyBaOZjTxGbATQd4UbrLOsuecSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/jfeTqOL7tAK2hY5uFrElhvjFORhEo7pnkds9i6Xfi88cQ-k4uUCUTCtQA6D4uj-dYTAfDoELvXE1j1uoPS756pFgXZtXR30lAoSBe6ctNkKtT6dMKy0V7WAtFExgJ2Bi6ES4g4PRLI-7Hd1JATwuDpaXiSAf4O3anoTU6vsJb2-qg9S-o6DkQ2SDfoJRwgLEUjyCSn_URgA9QdIxwTrHuwd4n7Jj3mNtanM7aOMhBI9xznCed6xJ5SIeDAZrVgnP20mW-inPRnNuO8OsxCrL87kB8VAAVNOJq32nTJMYk7qZ6nXJII19uOGfU6fHNM6GuCRrPHCWIsl-OCLxv5HspQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l43FwaK9il68Ce9HkJAbVy8vE_x-Iw917uamSbHRjXz89GyLoFTJrwn8-QXBaskw9M8aYzc9Ydo6JKVrTVAWH9jywvsc1Kljb1CwMF5hdCw1h4pSPICo8cI8HvuaOeOHlf1eaqIz6hzLtMoW8w4d6JDPO1wSOB21DB99hwEflZweoveDDoMqwXAPjPx0tyxZ-jC-CI3uTYsJGV0V3VKzbPZ-483RU4MfeFB4_00qFsZofFrf_r9cM_qW2v0luzm4u1lHATpYQc7asIui4tk5_RhlDijWqZwtWjKqMzc3lLCH30KcL5jR5MpKcBV3fu-2x_YpbnzSmLI-BREj7IfY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pScCYD3_0dU19LtQFKnaskGR9rpnr93Q2389UQkSfxJ71wSgnBNGlZfHQBA1XCO9v0D6YzWcGFBccfQhf4nR9hmKnDDgrLZqzdzHMXmiwoz4i2zO6VH8g99bme16oimDy_LwBvUyNddNlfOuqU06J-FlEU60rqg98OfT1fH3ScFQN2TR2QbcLC8K300aATtBoYGAxU3blieXUp1W37qQ-6wRjQjiJA2VvPMTErCRbK93Rc1liNmz-bn3tlo1008yA6P0EmBmhEOP_KaqLdETKS9Wf90np9kK0OGHFIk05P20Xa8pTv-JHHzA-aTcOqzgWEVnDMTgNZIjreQQ8D4tEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHL300cIlVUaYCdNQVCb9e9LYYEABLRiXnnNjMqPfb6E6PTxZQnv3nIce7xKuRZJbKWXOAsMxkJk5OLEBD4btDsSRDBQMnJa_GmlGoy_Y6OFgMD7C89YwM_SAl5NYlAAfbAqfgBvOA5jzZvqPnX8lw1WbdLcNSIH2B8bLRrQpB1ir8oktP38Fghsjlpciga9-LN6NvaN4w0RQcbTGcnfj3N6weUbwq03Wv9ZL0LIZoweJiP2Kie9EJlaiE8vG2qfsnyxYw9Q1C8eg1JGNphDxSs8spqj9kO0dq9mztLdqCpEeWDvKL5oa8TS8yMgSTML7ETjAJ3fPe768K2sBbHHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMiydK4ANPGpw0Kf6FGyrtF0UYIqqknDFJkqlFPQJrERMkk-leuez9PxYBW4vAxVb8Nqxno4-jSoN917RvbReiHynIKvDuMSN7taulFpFlRb15K_jw0-qhshB1Tcbw3Uv0zfBcAIPE4EkX4R8xQcYIPJgfGo39I1P6WyVLvcHRU13olUiq_gHfwVw-TrROTPUrmesjRA4hKfsxhawmQqzgZZLttDohNyCI5trYU0H7cERebxebSpyyFZj81bQJYTMmviHoikTs1shHDe2ipl4OKk7nskv2djmBpZ3D42TZ6WBAeKTg2sqXS36Ki29agDS-w05RoH5to44D8rzExvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=Ys6tp-vkx6CsgyGTk7YbIDTk2EyKIR3nI-JXyJzKPTrtSu4gQDggJGwqBXFhGEzV3lOid6WxclTrD6kn9SB56jmXNpx1ultu4TOfjk0NnzKVAEMi2h-vLqUPNq7DKZM9FIQwYBa9dXv8EvMXOZ2ZufPt7JUoi7QpxRaeTtER1Hy01nI5P7wupYn1wVgLpE2lkkzj8RNTLk8WATRq0oThgKhDVcSXRKPnxSW4gjDweDCd5m4AoosfnaJz9VmFl2aJeHgPWCPYYQhd10Lk9bH1fE5J5HzqRuPn-5LMtSKm_bi1a-CzxX5hwc-FtAbe86a3ikwQaJBVmNoqUh8NURyUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=Ys6tp-vkx6CsgyGTk7YbIDTk2EyKIR3nI-JXyJzKPTrtSu4gQDggJGwqBXFhGEzV3lOid6WxclTrD6kn9SB56jmXNpx1ultu4TOfjk0NnzKVAEMi2h-vLqUPNq7DKZM9FIQwYBa9dXv8EvMXOZ2ZufPt7JUoi7QpxRaeTtER1Hy01nI5P7wupYn1wVgLpE2lkkzj8RNTLk8WATRq0oThgKhDVcSXRKPnxSW4gjDweDCd5m4AoosfnaJz9VmFl2aJeHgPWCPYYQhd10Lk9bH1fE5J5HzqRuPn-5LMtSKm_bi1a-CzxX5hwc-FtAbe86a3ikwQaJBVmNoqUh8NURyUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI4THY7zX1FQ2hC8X2wtA6a5KMda-Y4SjSne-U4moNSOC0D0TnCKvncIaEli5VMt7Wz0NCg34dacHP3ldZaDqI191CIoCj-q9D7UVAhyW2hjv1I2Ux2b1uwiAyW79FsexrEbr9k9A9HKMA7lyAcA8lc40fblWC0Ez3QiMubthTG_bHMA8muSg1CAaEMjdnbDfreEYToOfw5YpR9tzHskIPuSYCJ2Cm1eCiojg0-4lb3eRC7tsNty3VQcwuFloBi6ZcNjaw7Io3zR9WA03AXC24eSoGTktzUuTbWOYEB5T8NUlUzKDoUpHk-2-7ZJsreLAxPj6cFCD0vP0Kh63AmLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_Sru8OnES2mmXYYRR8t4Q1nsJAqRExvLM6JWhAo5BgSLgt6K4Pt0FjEU3S0MizCYUSU8o4qebsAwhD6WJNxJluZrysi4-6PPQFUNnwjYYxqHg-A_cO56kEcAdzJXGAHTGRsmSx4IdtaMm7cA4awvXrInQEsJi5qfDC_F5K_ktRjta_l1jjG9FEw0kfFOP9QRTGyiX87Zyb7se7S3TLMPWq-qsak1Xn81xvNhQN0UH0TUjZiEPlhFQxllEvIYnU9J3V70jZ7OKjbhYNjHL-Lb5deUajG1fmgbxcXw2CFSzpszres7n-PyPioNUv1bYE4zoL8PZhu5nGOxgM0SQj2fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvIcKFXRFfU7HsjkyK03zA8DJaIaYe-o_Ay-WoRrvswV1hhTvpu9yYpExz6oVHeIiyHYlWliC17OC2QIAOYkHfrrDUSweG8XLXt4rMiADkyfC5NqDj6_Rds41khXimqzFuwxB_vhcjB6_G6Ppq9Gl-G5xt_JyzGbqCGStlPBKpLa3pX8dZoN1vscGYK2mMFJRk8YpU7J8cC8lTtGskhkuWfzbva5GFOGNvGoZvUzogWPKhoqRvMGWsQ4nyoAJd62JtgjUcoDS-DCtd_F_CLvbe1U-1Gno5TizByn_9AHasVR2_keQzW1CAbbuFe3bkbHgqZe48ks0juqnSGCvzNtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=q2vBoJasry54QNluIUf-kcmxhOK-sQvKw_126yzDGiw41LDjMMUhUBXAuyc7ThEsDEVTwN74Gn7ViSXss1RrLHAB7iQ1b2QIvlq1G6ReCopc1QJhJOqA5MHIOyM4qmuX-u85dwsIdunwK4n6jkZtFd7cfTVg68TedG4xQFpAcE1W8oTXF8x4gcR6GOo3Y2H26Bbp_R-vRT2fads3aZ_35zmD90RZvC7AZNfnosmFIYwgaICv8_GiLZ-Czpu6YhjVzcrDiDx1Z-2sxJd7QnZER54aoQHFOHD74Qoms2C-v2LYfBlfsnu91zZ7o47IB1V6FtiSv4_wTigizzp3saepRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=q2vBoJasry54QNluIUf-kcmxhOK-sQvKw_126yzDGiw41LDjMMUhUBXAuyc7ThEsDEVTwN74Gn7ViSXss1RrLHAB7iQ1b2QIvlq1G6ReCopc1QJhJOqA5MHIOyM4qmuX-u85dwsIdunwK4n6jkZtFd7cfTVg68TedG4xQFpAcE1W8oTXF8x4gcR6GOo3Y2H26Bbp_R-vRT2fads3aZ_35zmD90RZvC7AZNfnosmFIYwgaICv8_GiLZ-Czpu6YhjVzcrDiDx1Z-2sxJd7QnZER54aoQHFOHD74Qoms2C-v2LYfBlfsnu91zZ7o47IB1V6FtiSv4_wTigizzp3saepRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=P9zR-lz1hH7dtoglGmfgCqEhE40wVhpE9zFe9c-d8Ku8KEvPFBPlQMjJI9_PyTw1wWO-lH0XAIHlLEN_qnS9Rz-nc-6TSjT8kMmRoInyvwgnl0fczMxGB_VeS9wO6JY9ECqlX_hnAPR7agGVm8cAq05Amdxn87Xh0vnMWekbWkjCaAtJK7C7OnnBWsSidXCzLN-1hwvSabbHeayF90N57VFLSFC_bhkLNyNzXkCPEVte3t7L_PxVIVS2nl3_cdXuV_1BtYrHNGI8cnUM-bvpBXma4mNhFuPWH6E_B7DrcKzPiSclfY3RslN2mFyc_DN9LCoGwHQBJ62U9xSqqicKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=P9zR-lz1hH7dtoglGmfgCqEhE40wVhpE9zFe9c-d8Ku8KEvPFBPlQMjJI9_PyTw1wWO-lH0XAIHlLEN_qnS9Rz-nc-6TSjT8kMmRoInyvwgnl0fczMxGB_VeS9wO6JY9ECqlX_hnAPR7agGVm8cAq05Amdxn87Xh0vnMWekbWkjCaAtJK7C7OnnBWsSidXCzLN-1hwvSabbHeayF90N57VFLSFC_bhkLNyNzXkCPEVte3t7L_PxVIVS2nl3_cdXuV_1BtYrHNGI8cnUM-bvpBXma4mNhFuPWH6E_B7DrcKzPiSclfY3RslN2mFyc_DN9LCoGwHQBJ62U9xSqqicKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ex6GrcPzxUgdJ1xj9ERTLdUUFHhD01L48C8VCxrAe33e1V6R7VGFjqRimxyuGSph41Atu4Xp_JJimFdJHff6F7uVCuIabjjaVbY4ZxBpfLbCrlDi938i2Ca-vBs7mDAol5kLHGZsoF9qvyQlQXhoZwSGhnrKUUYQQOD25qndfj5j2elYfpi4kfVBwMScfBbuCUEoOQXkAPjyEDnZEynvlkEmar651nZe-GQWDqe8X1fewNElC2WF8EYXuTxc5NkFNGUjoFYHiSWPe0hFGKCFD9KJCAtgP4HuGMUWIa_bk3XNZ0c7Foj5YVe86MbkbRXT45czVv__NIh1oyyT0rs15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ex6GrcPzxUgdJ1xj9ERTLdUUFHhD01L48C8VCxrAe33e1V6R7VGFjqRimxyuGSph41Atu4Xp_JJimFdJHff6F7uVCuIabjjaVbY4ZxBpfLbCrlDi938i2Ca-vBs7mDAol5kLHGZsoF9qvyQlQXhoZwSGhnrKUUYQQOD25qndfj5j2elYfpi4kfVBwMScfBbuCUEoOQXkAPjyEDnZEynvlkEmar651nZe-GQWDqe8X1fewNElC2WF8EYXuTxc5NkFNGUjoFYHiSWPe0hFGKCFD9KJCAtgP4HuGMUWIa_bk3XNZ0c7Foj5YVe86MbkbRXT45czVv__NIh1oyyT0rs15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcXzGgEOK4ZkeXBH_TfTMkJ_5MtFJNN4YLNW1lsIIL9oyEAY53V6L_RcImHHbm0gzsoxkXq097KueQ8o4vWO4mpZAb_EKo-k-N1k2cLJsSPP6efJR06_N1hhXoPcqVit_fD57dPCjp5LrAEfOOY0xA_h0RpqktJOwWGhFK4J43xVKHwFntxKn0hADVvGRtWUKEQ-UtMGuXcDbsanREg0SRA6plgTvLWmHWQZn3M4xA5cPx6wckH6-uS7SQzQJNzBWqTqj66c5DrrKOhOA3FstWnMqFCAg51zJXRxUg9KiZjEUeUJTIdTtljd3yuiH7_muo4f8FK_Crz6c8HWaaDR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNh0uVq3kkLrvW6AAOpuc_gPOjsJOHzP9EKkrPcg01rkeIFRw2qx6DRUGQywTiQxe3efxbkrJaD9SVKxuSWtNROV_jtjlLrO8o6lROzOmj-GkXhp7lW0_BuUzPZClbjfdP2ls907PncgSh5_TPD4r58vjaBcS-Igd2oqylGnia60MrPAhSuYMEnHX6L1GIE7KFe92aAPmvGHe8tc1O9_XNq95ETDFufXuq4tVO4bTAvMamHcJfpCLkYdaQQwgMUB_bjCnQmDVglJl4roRdJPS5LiMTt5Kqzplp8sb5xe_F8GVKii8QP71CKbUfJj6GDHlI1c7_eamc8gKdUxH1H1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVrxNoqFjBMhn20WFmmFuw1WXAHiF-Bpyj6ShJTZAqOkXuhTSeE4L2Ol3431honYAEicVYeywot0iYnsvc6FdHxPfKFiIa-F5rFzxOBnqmxV31LhGI_lG164rsBHPWlqie7dYzRpNlpVdLBzVlP3nam5lbwBccqko3Mr1VbxgKSqe7Fw_4nDClNkbH459b1EmYbxLqQP-cYLT56W7IEPWWFk4NfnL-LUBWoUQ_GRBm9yJRoQwex-CQ7GYEdmwKmHTMuvkkDdxKqg32tyRZc5rC_nwXFlVo2DGMnoe27p52sUwPAyvSfxf7Q46p396Om08nXqFqOt03YYRJYFLUERyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9ri4zcteLijr4qzbDxmoX5HdgPHwL00TpSqw11NZ4MblIvNFkyR_maKczMTbONsTnzp7MzXj2D7RopDLCzAFzEyoSbdFMOLUvuKcnoz-yj3ROu4p2MMN4-6_Zz-gdUcF41uSbFtVCN4LDVqz7e-vuv483EcSRflHwRYpTdEuQ-yurWsNM9v5VVFg6s0HXxbh5Kthcg8QyoFnWIewd93F1zscxQLljQLezBL5_cerYiI-J0hfOlBM6y8JzxldoMoRwxsqu37XiRAXzyuquUxH-mZUAxv3oFD9ZR6qPF1DfGtZorcaVZPOjo5WD5VWb9rUZiMAEbeCdkC70rnumtK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DIbU9MFgzXMHbMwleoWdcX5Q6NFM6bo7XTHnlqbyQRZ6HuidugcTjCDm7RIxyytJyrfubZmGbUZI6sPuSFoH73S-U1KHx_Q-Wea3u9JgTtQZo6hVFrlurkzMEVfJIoiG9Gv2Vd6gsAJv_t4sAQ33jxQYnQfqGerOvuT54aUK2fV2iZQLnPkSivDzak2k7_7EqtIbINgiw1q45kJIv_KuLPXSf5gPAMZbD6xUczGZHh29J-cNaHENkPc3GSSMYbepbp15FUSGP3l5q3HpaGUPq10j1Km8S5Aso_O34FRd1_kCo8dqoiBYqIQkjLT5f9g5aOfvl-hKtwkrWOuzdBwCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d5ZElVqC4x0p6kUJYKYqfemhd88ng4VX3axYpmt8cdfSm4YYxbhfC9Btf-xygEFvBwFx895vXlTMrnh3Dpgc4UZ_scDxztY786j2PqCkRtkGyEyRrhT-dG0o-x_odmLlzICdoQhWvDVwgOfLrAZPiNd3Wjb-hdhRRqjNYZ-Ste8eEDkWeZcQfIsgJFxCIcW1cl--VPK6QzxxkL_eM-i7EzBarh57ZtZugL9r-HuNPBXOBVsKKJBHwfW7wbHghfKlt0zCcdTPNcHDvht47GXcZXehhmc6kgcDuc6k9TE1jk3OInlKak9ggs_5h0OeMiu5imndDQb8jJtoOKCzmY1azA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YuNZ5qFFXKLjV-1d9oxBoE0yOPaPkrgyN5RqjaqdI_BSlbjxZKg-L_lxYGiACuGNH1S7mJQHQJlInY3LL3I2QAGbQMtx80mCWhNeh2fF-O6UWVrvYAsccrYSZvW45NksYPtrnzFMPRrdMq-otRbt-F1AK8fUKm5gp-d1-TuMB9n0ZQCMOlXGeDv9nLjjftHB8lQlpEzcVyhp2D-tI2rckEt4xVgx_IbgvKy28eb4nhDTns1IXOnRevupVUDWP-o_XMpGyARDVkT-G0niLFxf0yrjRFh3ncZ2YwOilkYFCA5tGoEbIa175UwdL4NxtHxagj2Lzk6WoI8vxF9vnigFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jnkg01jnXUIyFbrKlZGeq4VJ7NCPHWMNOBTehUkkLs2nzQUJQ9USkyTrToKMcTZkvnHSstIAfZDwf8Unsz7EDUsKj3FUbcPyLVmhcNlrxbxwcf-ZAMgNS6FAFgZeIfZ2wPwLikWa_MiwwaVDRHIDLHqdXgrtPrEkJQTkLBjxeFGAe00ybsv1nGrWfvGIb64ONAUlCCU3hlTH4__GqRZVUkzb9ulICNJmQndgK97Rpl9nHl9ICvRQcQF_-0CxsTHMwUooPZo34SY4OYg3Qcf0Uog6wOvHeccT1dnnxc6JZU7C9jsx1o-BzskmR_TBV4oI5i-om8kLxCWM91JZ5I9TzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ro9gXxHA070Ea_QxFOy_7GzyWotPIq10XO5l7A9TVsatI46D8aYcrxut43X0kMYrqBfuV4qNDrB59skdniCxUmWJ7tuk5tR2r7M4W8owlmWVXfWBsGnpopF_OnnmSvSpqrByQo4kjhocp5Q6pv_D_8ANYAtIVGmt_RUYAx3F4TwC7_3DtNX6kKe1Yy9f2VXQoF6hAckoA8UiYCtH_VB2qcKwci5huIvAHsy52Nnd3azXYX2tXsUve81ZEnZ0joXk9aiG-dKv_e-K1zSZcXitJqzuGd_TGvDmZxgjsbwj10vLFiQ2qTR14rgBsO5XhjmXiLq1wUB52JVkQCg7rcWWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ro9gXxHA070Ea_QxFOy_7GzyWotPIq10XO5l7A9TVsatI46D8aYcrxut43X0kMYrqBfuV4qNDrB59skdniCxUmWJ7tuk5tR2r7M4W8owlmWVXfWBsGnpopF_OnnmSvSpqrByQo4kjhocp5Q6pv_D_8ANYAtIVGmt_RUYAx3F4TwC7_3DtNX6kKe1Yy9f2VXQoF6hAckoA8UiYCtH_VB2qcKwci5huIvAHsy52Nnd3azXYX2tXsUve81ZEnZ0joXk9aiG-dKv_e-K1zSZcXitJqzuGd_TGvDmZxgjsbwj10vLFiQ2qTR14rgBsO5XhjmXiLq1wUB52JVkQCg7rcWWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiB2zWWA9O8WBjbvYcUgroCjp7rHnYX5iouAuMFYESQ8llm0wVJjtg5O03AsBPPwGrsSfrnpUWVaWgcQxSk7FNqWZ-MOpR6Wyx8gecF6pj7g0NGlpirkyWzS-n9bsjq8GpNh_ltN7FxTUbOGip5d6cDFTPeDAQZYiRZRSF8OgfROU_e1wS1r9xY8UoxZjmNhX-nKjcfYz7NT-EzuYBUJ_KZB2UsWxx9cUZQBITJfL2smqSFj3mxHV8rz4z5-VfRvWKgYI4BUrHa7D3Bexu_9PRuCqDH8d0T4fbl7PWxm6aiOeGoDbo26czFQTUIexuGdiCXogKMmT1fAhbXA-cbUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=oUvSRgmEGgviQKnkCAVjMFaLvv8sXC43QPKsnPYVgyscrVFU1b3dXe2LrQHPCoz9qPTXUkuoCK9ppNtN5ARJUXPTraQE3eUAtR240WUfYsO-aWf-rA04c6Gg5OszhsqRdaTO-fI8p691mqZVVkDMjZgqyIz_SSdnCaZ_YT9eijuyF9JJbJTk00xh7x0TOKj_tRfdzeeX5hWTu94R6pCCCd9RFwJOh2S1SQJDBX3ZzZm64CSQiU7kuYCNXxhLsSleF35d0uXbOS3sT-aeqKtWChCSqFLVKoZASByjlsH2m56qls-8yXwuv2Y7vX2TpBdTlxDZb1fblz_x4ABmcDEUAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=oUvSRgmEGgviQKnkCAVjMFaLvv8sXC43QPKsnPYVgyscrVFU1b3dXe2LrQHPCoz9qPTXUkuoCK9ppNtN5ARJUXPTraQE3eUAtR240WUfYsO-aWf-rA04c6Gg5OszhsqRdaTO-fI8p691mqZVVkDMjZgqyIz_SSdnCaZ_YT9eijuyF9JJbJTk00xh7x0TOKj_tRfdzeeX5hWTu94R6pCCCd9RFwJOh2S1SQJDBX3ZzZm64CSQiU7kuYCNXxhLsSleF35d0uXbOS3sT-aeqKtWChCSqFLVKoZASByjlsH2m56qls-8yXwuv2Y7vX2TpBdTlxDZb1fblz_x4ABmcDEUAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=URKIliIDH0W52Pz-jcxTCiNIQ-bx87f3OV7WnK-ZWwB2fRawdtNaOWFxrGlxOQvieaq_mPCzp5GUE8Wp6q_4QcXN9y4HJ-liAFX9m0wBYNIVPPuu69rDSQ__qPjBikwsMiTEiWIrcJTPFbzc0TYFP1BnxtaTevCykb5TSflQgf37Zw1PvPr-WYh9lCb1NabF9Y0WBYjdVjEeInrmVhKWdGVHMfxXjyFMk65gTuLxXULxDlSdqov25FGpobpbVjKOOrsJImo9SLfJ_A2IauukCvyYaszesFO5spk0dL8c3ek_nFBLTxO-fY138utQB02nzh9lIUgIjgMi1CYDDvikGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=URKIliIDH0W52Pz-jcxTCiNIQ-bx87f3OV7WnK-ZWwB2fRawdtNaOWFxrGlxOQvieaq_mPCzp5GUE8Wp6q_4QcXN9y4HJ-liAFX9m0wBYNIVPPuu69rDSQ__qPjBikwsMiTEiWIrcJTPFbzc0TYFP1BnxtaTevCykb5TSflQgf37Zw1PvPr-WYh9lCb1NabF9Y0WBYjdVjEeInrmVhKWdGVHMfxXjyFMk65gTuLxXULxDlSdqov25FGpobpbVjKOOrsJImo9SLfJ_A2IauukCvyYaszesFO5spk0dL8c3ek_nFBLTxO-fY138utQB02nzh9lIUgIjgMi1CYDDvikGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c84FNXOhjm4lHDh-fv1GAwcVZ9Fl53njng8zj9IHEuMnY1Sa6tlkJ4dNFwkuWRfjwy9pEImgWmvxnyXEP4oi-dOvFo2TuOFk_VYI5L66dYUFwavxPDQnd_tktfSLx9eMnGickExPZol9nVSYJZCS4785VmCTLCBz_8pkUY4incNJ663FWwf2YdxI6ivKdXR_rJV9kEzk3x-0Rqsq-vt4dy28q_BMFa5e45mEEb3yVVlaE9b6TeWUM9UHQbptkg5Uqnv52DhJJYuTHJrN7QnCy1njasVa_g94EA9zlmdxAaBcdmPHvuDKVKYMmxC5omwlzhDh82bt0WTmUi5Nax_DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkKlUMTo3N5CCmKZBenPbPatq9QI9gFLTNZr8kciFxinjlJq7q6phcP3WDT-GyIRt8hGYtRQnaSVu4bVjWuilkwb8pWZ2TPsKY9o2ssSQzeP2uEGtXGCq5rw5h4FyECpG90ZmhWWVH8255vpBGAr48JLM0TbHmFalUzYwTQ0LZZDcfhnFHmDxckpsKZLEZbuSGfJwolI3r173pJBsd-LiAqVehe3eBOuzoD57tVtMP5dLg9lUQE4huTMg9hCofa3_WNOGwrMhbRJkuGm4ZKeRBLkHLOcHM8nJZvuREXT4hz9OPp1TvZbwX9i3n5SOmdyZiFtrMTcGf-j5VTcmYnMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffpCIwHQjQdvGKj1uvUJguCHxf_CqlBMh3SZnwqUt-ttOpFSTsAPLVyuVmvKKEXMfZxxOCjMBntgawKxwFqMeHyFXhoAmDpv3DQoQYTgUGJrAqMCTiVS2O82ZCUNVe-ehRVZAEzxthJ4Wn9Jw7_JNCA_djDl0Ak_gFa86jyhdZ-vRmujbjwV-YHMs9B1Z58h8gBsmgvJwezbVQPR7xD_qA6vnCTpWUL0Jr8Ic4Vo2hqtyl5_k8TRe4RtbQs7iisjN3PE9R9-Cpahfz4YCSVMA8MKRtC-nbrYoyvXdmcQQ1CfiUcz3_breBNo2oB37Di_wyTWCSq0JPnWtIpG73INbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=LhQAcdP4-QGi8MUNwFfgJSGcsclw6nLtB7IRWe8oJlr4l2EHo89EF37xbk5ljomblB15a8SdPGju444MkUNyNLJabu3Avy5DsGPt6kC14aGZiDAxbEmG7KBQbOGODQfM5MqtRzW2Ce97pq9_4MpnNab-dorMB2wi688QaPmRkR8SzTxSyGgoALIbY5vWF4pyiUDoEmC-sQSv8v3VqNe-_TD90q9bB9pKJV7eYE0o8ZxwRNg8qF0maEe0kSQMgqFhq0q2Mf3w0BJMe0d53i08w9XKUQzZIEV4mF3flstApp9MAuCypfgwqFw8JZ5kFiGZtUDe1GKx2jxFWVVEal9EIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=LhQAcdP4-QGi8MUNwFfgJSGcsclw6nLtB7IRWe8oJlr4l2EHo89EF37xbk5ljomblB15a8SdPGju444MkUNyNLJabu3Avy5DsGPt6kC14aGZiDAxbEmG7KBQbOGODQfM5MqtRzW2Ce97pq9_4MpnNab-dorMB2wi688QaPmRkR8SzTxSyGgoALIbY5vWF4pyiUDoEmC-sQSv8v3VqNe-_TD90q9bB9pKJV7eYE0o8ZxwRNg8qF0maEe0kSQMgqFhq0q2Mf3w0BJMe0d53i08w9XKUQzZIEV4mF3flstApp9MAuCypfgwqFw8JZ5kFiGZtUDe1GKx2jxFWVVEal9EIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOWukOFC3lyRpvEIzEGlgztt0Aq0bQeOl1-oCgd8AvpRHi-utCvh-H1XchaBiEwt-MWvs01jdz_djk8jGp9o7Ji_TO66Abggcvx_Bw-IH1KSBOBsZd5fFOixJsTgxg1TyqC0LPj4vwOXJveBEu33nTbFwPf9eU8v0fnm0sjlsphKvxCDd_6W0qYdPFHmd1EmvIldncO3_kRnanWV1ZEVab8udDRyjb5Eln0FbE3X-uWUQ215UVcDDm1e0RBP7EFs_He6Qd7GwcgY-WyiOlIiLpNMWsuevoDB2-6X1lDKt2PU1axVTtuaL_aSrBvrwFl8oLLR14qJF2oOzbHn1vMoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=HeX2A538GTj3WMsuruMRJri6teahIgvWS_dDtfAkF5-YwrVxk_TbUmeieqQeZMkKcOPPw5_GNXXbRhJd7QDg6tlSLjQJk005ITD-psOVbXESDj_zAGhgNXio-y_i7f3QNztWBRo9kce4Dwllxr0OTAnaZiPy-Y4rg9M90cp9yd1bfpQAM0dS1QqtLN9T9xoqF5tMpExHHgE8mmeMBeIw4UHXdhQfq8uZXVdr_UkT7iNLvHhC_-AKLGQ60O_tCF3tMy088p5pqIryan47bTu8IhMTf2A85IUDG0xspII7gMqOKENZyi544W5he2U4trsUzZ7PHpfBBHIXLXdYetjvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=HeX2A538GTj3WMsuruMRJri6teahIgvWS_dDtfAkF5-YwrVxk_TbUmeieqQeZMkKcOPPw5_GNXXbRhJd7QDg6tlSLjQJk005ITD-psOVbXESDj_zAGhgNXio-y_i7f3QNztWBRo9kce4Dwllxr0OTAnaZiPy-Y4rg9M90cp9yd1bfpQAM0dS1QqtLN9T9xoqF5tMpExHHgE8mmeMBeIw4UHXdhQfq8uZXVdr_UkT7iNLvHhC_-AKLGQ60O_tCF3tMy088p5pqIryan47bTu8IhMTf2A85IUDG0xspII7gMqOKENZyi544W5he2U4trsUzZ7PHpfBBHIXLXdYetjvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEfC5NIWskLr_ttIhLivs2PpoasVWpl-w5y0sC2sETpZdrIDAyryOX9doFP1yS3P_WSRMC4MquPXrWgE-pHvS7njLe6C7uzQ6DxNOfliu3gz1k2g2SbSqdHrrRB-WQTXO3kIhePtd2-FyyP2SWuVdqQbwRrGKAKVk295V6MDDcwsNLxqqnyzySmKwbAR7Yqy1ftKsu8JndxHaaqDXEEKPxqlctdANiVTxg_AhYTvaMPPhVlx17_1t2AVabzftD5xhlPVSl4IuNJSRy4ZaAEkgC4RNEPmjesrHOLMlfAstY4fjAQbizfsz3tjlNmVzIzxrTLA5eaFXPpgjdlOAbelqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFPAYrfwJErl7nSRNfzxHW0AaLSdxmL_5zcYQGTGarh-OWkZNAhl94b-0ll0w0YKn9nkBLPWmokMq3cYKmahB6E9XNJ9xE7Hgmr7PNWlQiDbv8mpJR4ZV9GBJeADpDPlLa-oNF1IwUHNmjCpoE-dxQwp8D2tS0NMfHa7B7RFq_T_wqy9SavJBlJE7L4AviyyN3xVJxXTur6LKn19osWcc3FDKIFX6DnZPeNJc2tBxOqIImuu6YjHw47AWvEnfw_eMsGz-klQRT8QeLmrFxf8KMJqUDMxknGJWbvbn164JzLHQ1iiK96I7rl2XzBjcvoPtncRth0Rl7AlDvM3qEjCjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYBnktfXyY0n7huo1MGYDXdc05LnW97soAqOQPoHaNukKTzCu0wLH_j42qh2tYYAsh__8qnioISAL01Z5uPhKQZ47IG9fOUBHlC9-VZmhaq8_DR8sK9uTcXfGeo87y8P8GD_g9r843RgYYgFacnR3DLQQWMMz7tuqwMSr-Z9gGP2zY8Pqo7Y_hmFxfW29HGmXE2UdbtDXoereI9HkGLjjXIuUMcl0pcqw7NaxvO87N0EAQrAr05dMqmfbU9Q_f5oubmzLwyD1K8jjKw2ZVGEuw1GKKThQ8NrTUL2hd3gO2jhPokpd8baYPiu6CH8WYxwZCqpHWHAyNOYhHgwkA2vcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXfQhLARSTH6xPZ0D8Eyuta0x-kpGXaxx71pMiq337Z8eNgY_cFaYsScdq5wbTmq3DiwHgJjfP0N3R7315M3nYtT6n1sZiMC0jqv8qGTXm7jpfVAJNhvnVvdZ6aERyc9gnE3qmXkrRqS0Md0T2p9fZUjM_EyqaKkiwjeRxwj1SgwseiFAeqG0Y6iNPIC_todY16Sg3F45pD1Y0oG7pngibHqk84_Gix29BUVe71W_Aj8s-AxHcovlCvOugrdV0ps9lM3AD27M2OXgYPFC2LbaQ-2alC5PDSixUFDvV2sqELfSCbEwBLYzM1nJ5gEihiTF997CHoD8jtlwnhph_jS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZzIDiShAGX2oZGOjGm5e8jVSR4287oNbjtpCHIeWDYuASgdAASimbfDGdQUC0DzX1_ldReUKgSrDzfNJwFqKV0DkZ0ufdnkvWlZgpnLuQ1pp-qh9Q-5_RFFGoERMf-yrbAP_8cdfu8Rt_qg4fd353NhXvafYx6qc5vH8qh0NvWvqhSJCc4q7jS5rOZej-L6y0zrHV6XIS4Jbdd2KpMFAvd3IcVO0nrYiaEOkDyR1QKg8RAR5mYshMxvUq9TB9MVXInZ5CGuCaSaSfbADjQLiK2alpzLT8K5JHKlu71LP43BxASkOZtt2iGZC1jNyUpx0vcfMANv9O3wlLfx8CqckA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2EF6fcB438SzpXcP2b3DQV_xEZcj2wqAb2oE1V9BbbZ2q4BKoIk496nddpFOb3SQITykMkyHJ5an7-gl03qDnNk0iPBGMH2iPqdfAOa6XIrd5WrhG9s-QMDxCgnOgR1ybKTJQ127GqsT8lPd1zCsqUTFbTI2DvrcudawRNsTp4aUOP_1lymVRwmCEV9lb6y5LR2Hcq5daLP8h1fM-ivlZzDyEaY8msIfZjVGXjXnA7crY1gMnQU3mgSMmE-h4wAuSl3Xw23Zc1YE3MXLfI3P5lcEk1CoOr2myr8hOCd6dVeSFtANYxUsNggoyc3BcATPZJeecwU1B2hNVmNVFxHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV8ORsH3TFRDhcSDMxTJoYS6lLT85nzlw9nvj_linKl9HJSFBFRpaL0kPgJJVW0rSPfvuRvZHyz7fiBnAOyuZUZ3oumkueZoZ5lk_5MEnd8q9ePfIKXN_5DILx9G7fnYQckTEUTW4vTaCM1lgX_tlo59YGhxF6VvCrmlw3aGOko_MDrmsmWw9H3qpRM6UlkiVCI7mOXPQLpp35knJR7dcMBzkNQKJ4o2M5ZK5e6MLO2SmQlr9hK-J1js5vlFQ_KfqK_Z-woppKALWJnUVXZqmLd3PFIjwfqhT_pxTRHGLwoHJhhEQoyJVvFDpl-BGFAoBKg4W8fsNT3A2jNBqZ4ZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=SuFwsZ-4cd8mHCDPsG6_kc5OnUzaQmxhgCPA2h7EjCQ1uF2LLA1SdkbjQ0HCyUwKLWuuZOnQXTWDTFhee3yq9V7ksq-c-QoP18ZJEfjCEsL-mZVW5rGvP30FqzD2AbFzkObPNrdN5uf3BFR3eIqQ_MSOx6qTRwedbffp9VierRq76L4iRJGrlM7S26Pmx5sgx_VhhpDRbLnm5FQDhkp2tipE6d9azqY6M0gFfg-q3pwY2G0rt2icuHOG4SiSG6ZziLdEqmPVYGQzZa86Wds3s3Q5eBeQFXTpC7CSizcAQn58mNWrRdxWz6ekAUVsflhTV5Yepser2KMxhCnk6j0EtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=SuFwsZ-4cd8mHCDPsG6_kc5OnUzaQmxhgCPA2h7EjCQ1uF2LLA1SdkbjQ0HCyUwKLWuuZOnQXTWDTFhee3yq9V7ksq-c-QoP18ZJEfjCEsL-mZVW5rGvP30FqzD2AbFzkObPNrdN5uf3BFR3eIqQ_MSOx6qTRwedbffp9VierRq76L4iRJGrlM7S26Pmx5sgx_VhhpDRbLnm5FQDhkp2tipE6d9azqY6M0gFfg-q3pwY2G0rt2icuHOG4SiSG6ZziLdEqmPVYGQzZa86Wds3s3Q5eBeQFXTpC7CSizcAQn58mNWrRdxWz6ekAUVsflhTV5Yepser2KMxhCnk6j0EtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIe-DFx0TSpIuFp3Fwx3GfUzMCeBmiiOADAC6yLEgPCQs8s2kID7csiJOKJ4wptXGd78iHxHyybUARLrOpm8asdzFf1IZi_o3TVxfav9HqATizQudxIJj6Gbstcl02Igmk2DDcpqIwXTmcFuyY0lEriY09RCgglOh6Y65JgE4aVcTXx3YpVqfqzuu2pjQ-SsfCLfhOHXSp_UfLPTgGfyr9e3AzPF81-Xp5Nn8Yg08wFd0AQc-7gQZKw7PQap0aEF-0MW-gWlRQwKId_7KwZ9h-dL9jf17F1DfRaZmzAGjw0n48RHBE7kvWkcIgDQvNYzwsk4Zlznx9Xadqdbu7UzLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=ZyjBzl6abrJzhryxvwrwyo3wvYvnIApAGsCEjS2uXZRa4B5Sm3qm5g2JRhh1Z80ULHvH_mkmaDuKl-n322bQtXvm5aGHeVJdH6ZMYGuByBV58odtsZ7xei2JqT_yTZzh_9S5nYthlvQl5by6Yy5RE0l6pnmO6uf7oP-CZC9-aE8mBY_2FpteB437HJzy9DdByPSEbUJXNrUuUaPNA95aevEzTe_0-zINx45rup5qTo-UOGyj3f5wtRM5pgTJGS---34BNqax3ftXwbycr_bwxUb5tIXouwAoqrViVNA5zRE2qN5k0T7MyFEuamUxGQ7XUNoZ7RkoqFcEp8uuF_iUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=ZyjBzl6abrJzhryxvwrwyo3wvYvnIApAGsCEjS2uXZRa4B5Sm3qm5g2JRhh1Z80ULHvH_mkmaDuKl-n322bQtXvm5aGHeVJdH6ZMYGuByBV58odtsZ7xei2JqT_yTZzh_9S5nYthlvQl5by6Yy5RE0l6pnmO6uf7oP-CZC9-aE8mBY_2FpteB437HJzy9DdByPSEbUJXNrUuUaPNA95aevEzTe_0-zINx45rup5qTo-UOGyj3f5wtRM5pgTJGS---34BNqax3ftXwbycr_bwxUb5tIXouwAoqrViVNA5zRE2qN5k0T7MyFEuamUxGQ7XUNoZ7RkoqFcEp8uuF_iUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpo5g1OSc4EDU7S_UAkPrcxaQiG0DoN3lXGET9b0YMmj0xBmCrjvm5Ne4xcLNsjzZ-tHAyDeji8_eK0GgBP_PFTdkiA751tGLQ8J3rfDve69n0t5stDNz65bgQhq4Bw2EKGE07jf2eUfA-g7pd2PdZIj3NOuuKmlDCwRJT2-wvziS_MRhD9_rk4cJG_VQY0VQPjMDmXuDMssDXF1P908HOCA-1We6Zn7-wo7TynJVshBhjJHkeMQJk7Gh7J6O8Fm2Or-nCByXH6V-rP9r_wxCTF752_ga3F841t6BNCjmvF6VBDJEPn8UeArx2Bu3NRhRLusIT_Wv_KSI2sUnNh_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMb_me7AFaeuSASeVQo3ezg-306YJwwm9-NyHLEJMiMCCR00paWXlW5zXnq166H4z7hLH2wLoK2bNI7PhSYXpAnRS2BmzRwz7dWNlslWa4QV1DN2PQsK0BepaU1qe4QxP5vlmMW9XO-YMG6oLOXNBjlIVTi43o10PcJlbHhIgZ8z5tzugfwrncfDPfgPmUzWi-Jdq5Wjj73EKg-ZghH2YWvFa7ofqnw-gjRE8xPkfi7dqsFZS_4lYCjROCZMsJyYibrPJPtk9e4VgBdoqEhJ58OjiYEaxBe7KqbLfw_ywuYBkhvH2_b5vZUdvEQv_YlroMT6ANcsyf0UomiFJul02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smxiF1_IzAkSOmcWyKRjdA3Gfv4c2npkfKWkeY6UIyk-7DfLfnliBzmsK1CA6m0ELNHwSQyec7dTaf2WqnQjMUjUBREDM2CQ37aEuk0Vd-Ts7deceMBGajNY-EqOmyAKMooFhqajEG3qoH9EGLACOL2iXgKVfGDkvM6_n23wOUwCrwRFrufNlDN3yny2Q6JBktCpx2AtvBC0aYlS89DRMh0aTSt_BKxMdl_XxYdM4ISBcRduXhuqJjcGU4oleGjiCRCIOwIcJFtTX3pbIlkURWYheIHW4dvFsk2yegnMI0eIPP6gEez3Hu4gJzYA__k_xt-P7NQqLE-UgDYJLN1lDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhFV0XWTDQG-Cig2lWCPqYtQ4VphDURcLe5xcXrjavkEZ-ijtxrY6MfhKGEoqILEzbvJgy7oVy9UTjeuLMBe8vYNNUDmId3RyXWuiOQijphPmCcZAIpcyZ-ydQK1l9RsaupIz750A6nmRqnrL9sfPCCTIdV2XgiFtLo47FArfnKUPtPNZZxxZfctwwNwabazFxhmMckPg--T6Z-UJ2GN6xlrOJb2-kRZhXZS8be73MwQOrew1GR9wexuL0pkvZY5rIgMU4iOomQmuiQw75S2DDKLx3_OnyeERHkKwyoQMxcgC6PUwJmwhU7pyguQEukmUHenx7iwVQu9R7iutUP2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=JEGPadnMrlUoz-7-aJlfGjiQW0ElJLK5IFnU_TwLCiwt4HkmrWXP4X9cfbXBLmA_rDf61C1Prrrh1FRfLEtyYupQzkyY-pHpoTNwjzd04GOfeHzgM-QhuyBt940pCTVrTL-QWV4eNKQ5gWDuu9NZxlU8vAhi1oCPsW18QGu6cYVB8VX0ohSF2NWWtvoQ3ybNUxzG6zNDaVZjwxLXJEXFZBNLGqlbKc5FDXONbc2Wk9DRDoMZCDRzyCo4s5PmzVUv4fRXZfpMftfYfpPTZdpq3FWDa-KoAd71ODiHArbPE1kfnlOL0FhSYtBUkY8k6WD0S_tNeBSZMeNtDWivoaV8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=JEGPadnMrlUoz-7-aJlfGjiQW0ElJLK5IFnU_TwLCiwt4HkmrWXP4X9cfbXBLmA_rDf61C1Prrrh1FRfLEtyYupQzkyY-pHpoTNwjzd04GOfeHzgM-QhuyBt940pCTVrTL-QWV4eNKQ5gWDuu9NZxlU8vAhi1oCPsW18QGu6cYVB8VX0ohSF2NWWtvoQ3ybNUxzG6zNDaVZjwxLXJEXFZBNLGqlbKc5FDXONbc2Wk9DRDoMZCDRzyCo4s5PmzVUv4fRXZfpMftfYfpPTZdpq3FWDa-KoAd71ODiHArbPE1kfnlOL0FhSYtBUkY8k6WD0S_tNeBSZMeNtDWivoaV8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v6b1f0EdsumduHHsPkcbYt8hM8F17Yu1TdAyO1oel8mauz80rpBXcMAJMFpsAymS4zFDmjsu3fXTSUGVZqAs-udgVNeptzhObo455DNftXKyeo6vBi8e1aaYOUMdcIvanT8k4NwQBbNWdBm-vJ_w0k6XS0Ad68JPlzbL835K7Pvrsf63IwrmBcBuwYnj0cHtW782CopQZx8FgsRvyu6aGoj7r5Jr8O0MBivaacbF5V7I7txbOBxy-rWaw4hJRXF6TXgj1NJ9HI_tVohJaAfcmifpN8h1VlqsfQ45IynoE6g-EysotQBUjcDfQA84YfwXtniKiulA7FD-RuxxGjohQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTAZnvNouRq20Fj6q7xb8_2JRSt1yfZPlOascTHDm_Qo8Eph8vIz-46wCvLZ7xDFr2CvLSVt4i4KXRsQpEPchAtjX09lexYEtsNc7F0PtWQMS9dj_FhATd-MHYbzPQORu1vdl1YavlLzwD1pFT2OGU_wgtxHKsXLqBK4EbuANW9Uxkbi0yG0UgMmAsuEH0AP7ZlO3j1HOkbAJdzIf2lxHEigpoo90rFPWosgdZOZsOSfejJMyIZ-C7wt_z5DoYWUorGA5Z-Kp84DAmNnZ65cprgtzpAx4d6b4HuCmpMqHOTw4P2Gtn0TnS9EVPfmnu9vk_ut50ZlL7rDOOsSHtWs0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4FBeFr_uTKicfuzwCQp-RxkcLqKEawaVD-aNwHlRU_Ogv6M7vbziYlqgCcyAhqgMCJBzDzkz7zHoTZAUHLWgh16A9ijUDQgL5jeeknq-YfhFaYYI4Q3mXUJzNtAOS9PyFV98_oyB6A5-_qwO894pH-PadK-HNQWsBaZ7--qevZQ4Z_iOrNYOchI4t0RRWoylHpMhB4ZmUwELpiNR5bRoRPSSxBK9-orMla7inhQ_-SWQP2u7e9oO1AoTZhgTPAGcTaiRvC4rFYno46i-uVT-bj7xTrWXMKR-TWSx99k8AXDUmSkxz1ppJnGD7xKCKdIbuv-qChWSye3Wlo9zLky_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOlrAR5MXtZES1tuGd_sTUNir1wdb4PMM7ya9SFrRi7zIhSapDxsFgQEBA1gfVaDy1D4iOGACEqzgY2velfmU41SCLcNxNFUmf9Ia837LcihqKuy17hdaYFJ_-23G_s5bu_oSVaEMi0pSS9kfIa-HTC9c3IBgoKBquF-eEEdAXBBV155CVxhx3jqR-ztSmEv-LLJeHjRzkeHJqKPBz4EWxgbgBLCg6HYLlJ5E4H3nhGhYKVr12mJn3fVA1Eufy7qyrQ1KG1bPVuRme21avMnfl5pQUIxCHBkltxIkli8C76nhWRq305z3s_YnWFf3pd1xpXn9LkFch6BEBpbGGALcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
