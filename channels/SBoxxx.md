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
<img src="https://cdn4.telesco.pe/file/SPa-D5OLL57pYtgNAoE0dESiATPbMYya3OqxespyHE4XzJlUsEK-sH8czMmMw4W-GakefxqIK0almOXC_LXvDbFFDbyX7H3qoK1thKfnjyLGwvYs4HZqk641-L2xFn9zYaBleOp3vzNbtDnOD3kLBjxwNr3OIL6wy84xGAOc_bm1OjTshqMhRtxyQdvIY9IOhT18bg6g-RJhIteMDugP13EqFyhnFI-EbCWzSyeP7DpHxTrtNIAEC8aNj3d-yO7alMtdWjiS8jekBqs1kHSrlbmjQ-asDdyiN0a6dkPfUZUkPDbrLTCRN085xjHXsL_k9tAZKC5tSOck9SBptoVFlA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV5jAQsJMAzK7FKWlUHhvFkDskl5iMrvfUePvgb8tzZGvIkXG0CxhAijMldRwvVxHt6maWHSqDK3eEewzv1Jd2nEeRrr-0RqXec9ILbHy_rSQS_BXRGWLM-5OJf5BrAxGLEJbRPJdljLQkHEC4ncdtOcPjukxlKHbHc-eRbs_ebdfmIBri6BIEge3omYh0bLjLGfqJEJeM15jKkJoJWRJu6-5hvG3fKbUdSpXDMuW8-yMmeeByjTrzaKcwe7l84K2lxty5mA7KvQ3FsPBByJILD9kgfaIYDWr_RSCQWBuImu3HJj9yMsUvh2oPBSwClm1RJFgC81vFNDSWpglWZv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5xolQFDvTwvdiU6YkqsIJASrs4ON94gXmzydlwr43mX5IZy6gynCZpwHDJPpYW434I72yRlTA0zgk1_mAryZn1VzMJdSE5TCmNB5DfAABtfcZV-lGiTwTvsM3FeYTuTYccjCGd2wOUo6lXusYPC20YjZQrj9dGFzjorNxPwvqU_eVn_Hzy2P2Zb8DMdkFD4en_HRKck9zXEgUZxzwIjYdkeMMaVGrAqqOWnUCiT9Yu5AlS4nsH0O5crFsSleKF_-CIJLYKmkuZ73pF-dc4BkBHAhcG9S4XkqJ8GsMdLHKdhlAaAwPxEpsPGCFOVSN6ga4soXKyJGzVunYdNwqzb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrVzNsGF9DYPeAuTCD8V0LAXO-Nf24jPpEfQqI5VB3q7x-R4gyrdMFaE-z8YZ17VbXcuH9kuU0FVXS6E_7auLFYc1buSh1p81ftQGGMLfjULJHRjcRPY643GRBMWA-bTGEoRgGDg7N85kWLCh_sIHtRTlm0tjGivJJlwxOXuCIsvLXWxg_gVrHLwvpX8otXkvo5teY7tp7enmBd1HoXIay1fOrOJxWSa-Bx4o7KQ3tTGqpfT9kaNBFrTKLoENiLbJ9epP6hfge9gJAx9t0mLaIhABiZCM5AEV1KT-OaGEJsoul-g0VVMpqN3b9bddt69N3vKdgzsb7KYi-98BSkJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwIGjLTefaBj-KDLC7SBtIyTo3jIxMkYHTJoJyyFRFYEQzMLZ5uv6HkG9g6ZherRi4XuUR5VMTcJHMmLBtN48yYVJZcWHgboxMxR7pmRC-n2HTH07MNXakUz4dZqft0yETzToN5Ik4wCcs8tq0DC54W-ShoEnuxRdSrg1Ym8jNZkhrHdpVqRuJAwrsYseykbyF-SznhHRqrOHingM0LmrSQWN8SVL_SiOhrnELNynZ5Oea71mhOaGiTyYH5MnR8cW1Y3z192Cc9JXdrEAClN82M1dfGKj-mIVcmQ0Qc56iJxJl8PSwJPwNfGznmBMEdsnRhbyD8ScSn1vEfvTA4bOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugDXjEZHUWrUrwPD7QnijDh-mnINI-xy2Dnq5yq2msVoMfueZykgFkId4EnBcGb-LoghI4CRhsnVuMDnXu78nvJsrWaSvmuSaDwrLhFWC-4lJb-O2Vv98mbWgxYkIStlsGVPy6nt-UdiuMY4ceZLVIEYJwrZckh0oJerYj-dpYFE6VhdoMeb7iMT6up5JfaUtoG1W415u1zoZ7_gDXXF84D-oPt5OyQTpnDTgD3cZp7ef_1poR1EQmKQ-QgLTasC5lmZnF0bn8HrKYl3LVsmEekJGFbRkD0Z6UAPJaxsgYXqtGGr5HUcrtJ_87jlfWC5pEm7a0tvQULMQgay_U6v6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI3Y33jxpwdUI0CahZ7890zmzCwkiUr0CnOhq1FtOpOlFBm6GcxupruVhAFaTJYyOquJzYQN_LxjV7cLEBGZ5KV-d1_y2fJlFimZ9kxFQ5_ZAyq-1Usz-CIlol69qoFbF1jV6XOw-Etm883T4yrY5bkgsJnopqbBJnCvMVdfBGL0ls_pOzUq1M611R-kAekmUafnodY-yviMn-5psxA6psD0zDopAt_1cVV63hylT5JV7kiQshjBmkT4LyFeQDn4Sutjkw9JByEJYHfje3dS9VT4tFC_okHK5-NlgpId4cl06_5EkcFiw8ekjvYQHqjVF0LjWR2t_jZZaf1nHUf3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17467" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOskdqbcsjwD23pNj_JJFONw76zmoHdbr-45hvu34FX_F9D0TZxs-r62KK3UUrSgkfzcKof1wqLh9nSnwZjcYJLtXBIren4eDUMNMqxNvb1YpM9BylAgJel0DB9r4jSo3Dept2gRuvDaCNnuhzzgIwD-jDmCBOwzmzUR6Wg5WrgRZzjaYSNfPGTyPqdRmEpRQ_qzOovJMv5ZqANnQpImNRupNBll5g3Z3Ur5uM1yqED_ObeXZd6nENRktvrIOh00lERWvDZtRD-ls54-chdvE8ME-IOwgD_3_zWdcoyDP6ANzBi-EX3IBrBYE9JKUypda7zvTTMdq5wiI0n9askxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت را دوباره بخوانید:  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  پس در واقع تنگه هرمز برای همه باز است جز خودمان؟!  سبحان الله این که عکس چیزی بود که میخواستیم!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17466" target="_blank">📅 18:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me4OA9SApeGgYRStKf4ntevr7MP57tGXlutev6bRChLcjPHfXFAh0liMD_mGvMQ1qdc2Sk1Daz29LiVyaF2ebQhC3geupnzEAGbmGoEdo1KKOWwGTyf7ZsMXEcYfXkmPUsYS94CBHU7Lni5EHzmUYMURxHmnBbwUa0Z_By9n-mGdkD3RHXAi0qEhI4OzC_Icq2VIFwQTvoJQOzcMKCQJyiUKaEWrzVx-bzxjT0E1iLy4_YVPOdazgwMCohkR_jBrgozrWXv7dKpHgSfIeuz5yL_UKuGl74ZxEeKLlfUy-7ij6wOId3idyg7RJj9g-wNLMXocqkNxywoO8PACvYh4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxuphKb3wXAnp28D3F51SR669ALocMb5Pvz-kuXF16n3jWW8rQ6AS9ePNSgDaZEezSWfBa0PRnz6fBWMBz5RTGr0chKt5wL0ZGsFBnZnfRzdonYvBje7-kXQmezlvJQTo_UheTHmGoGOtV5X-Q5hcP6ORCpgWsJ_fN1vXAhrZFVxkUzSZfzayHi82QhxW55bN8osOfZ_LTkt0JtpTPny5DNCepS4inG2w4V0SpRlMUOqhOq_BpeVYGiLJWx5XmWc94MN2mf9LTOT00T9ayycEIKRZG15zW1LgU_OpQnxQST3IMRMtMTknlVvF_OhjbHn4w_L_WgHD3J58B95MuFZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA_0wJdCwME5RFmFkZJN4hky1Zc1CE0HHCzZN2sJvgSyfm3fgu5egLKOFld-HzqTuBdiXh2nnSQy_APETkGRGHhxOqMfIPTNVEyyUvi5NGz1QTVf8FB2jR40bGm7TX8TPi6MSNW9V_27I20rPMaudSiecw-QvZpVukWNJyYigbGC0blBiNmI2nlbioyRxmyGGtz4HEa3JrEt4K1FefWtPQ6IV_LyvRXpKIKSXvVQZ3w3461WAPopgdPT6dStxaKXm0qFcb1Tsax3aoloyHFEmubfCTy2Pr0lAyPMCZJA254GztScd81huDlgA4URQIir2ozDyvmn_39f0VlZH7Po7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg9XSy2QFnpVsU-VXxFFQh7aiKiUbWeK8v2M8g4S0C7ms7hRVT774iuig5ZOdKknG0JSb_Mbitp-xPg774LhU8nI-9BsKU-9J1v2VnqYoFURqAp2f87wToZhTtZBA8HBL1V5PonsOtzf3C9fxiNECtbpqmtFncnGsyrgn79_HYwrgqC-SiO1cTeXy0KFhT3wo2rbyi4Nq8ekT49gXRfqlyAksMFW1sP5gb59Jg_C3OGLZoLk9f7khZjtYtex9cpCjSqL7N653JClRIwsWegf0zwQp3i22iNpffBlgtlAWrLrC1DA2hc4nsVBepTjc6_IrkuEYEOdC1zBunxs77pUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtWqft3BniQZIyyKHATzOTmAz8rY3lKEm1540cvdLczxLoUj_5lrqB56U7SjXIXH9W_afpUb6X91eKSgg4l2E2UXVf7hG9KsasHys4VuCbaMlDgs3kSrCT-pxpA0alo-KxUdDUI4q62ov_oYBSpwQXSNSGbdjjyvWONRhup6hu9o6LDyv11sPaRNxp5MsIP-fZiFLAHg2T1coAtSImR2xjLuBWf9JxOiebhD_KqixEQ-bszNPzovSWlcw7wApjuU-3AUDQt0mi2t8QsE1A2cS88l0oC5D6OWLMcXBH0Mn4g56sg_C_F1ALnoWZzs2SlTO0n_lwYyvwwwbTKk2fGq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK4JY5DIS5t-h1-ZGs9JeS_BCzebN3ZRGxvOZIkPJ0ZkJRVF3ZVUWCfgHUUop4mo0A_61__9cyEcT_wzNJY9DxacpCs2Nj4jI9fplHx4D7qmwPIsVYzHdbRxv7dsFbYdW2loIMA_eTVUSbndn497dPmh_MzURm1sLxO7OCY8wxLWcygYYbYM7QcC8I6ubb9CUNG7TTQlrui_A1Jr_YmGwpHhRRzPPppcTBJfKEwaf0h3VMFApjSODTZ8CQRDST_viaigtkF4tiQ-vnUw5ZBzqM2b80HZF1S9MjAimTKNeBoUkIsSTxWl3kR-OSnDVnwle1JBBtwNx_zEFpi6lMP8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17444" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do7oM7-itTGz7L5_WbD7ctyPnRucl6TONN22H10AxaS2rd_30GhtU7zblu-BmZ6gcOuzC9JNyYYbycWAXP_0luULJeAdOrAgA8KuNwdrZHVkKtWt7Quu9PhDnoxy60B4SNEOhJyEFnJWXlwykmEGX2EXUdzT_6mJf5F86nw9S3qFmGVGJbKv0KVCW1GU_CKE5TR5VSxzpZnUWaOltSI9cpB6zr74xooswRTogwKy2m2KTcxCgsWVYgNIavLLM84ja--HxTVyWjW2l7jaWYAf4PN6z4OFZf30Jd_w5r0NMSUK6yF5D7zlbTPjTmMS_5q7alSVzOZIfWgUlZFKn1DBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17443" target="_blank">📅 23:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حسین الحاج حسن، نماینده پارلمان لبنان و عضو بلوک وفاداری به مقاومت وابسته به حزب‌الله:  «ما به وضوح از سوی ایران مطلع شدیم که لبنان در آتش‌بس گنجانده شده است. مقامات ایرانی به ما اطلاع داده‌اند که اسرائیل طبق توافق از خاک لبنان خارج خواهد شد.  ما هرگز بازگشت…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17442" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO7XAAY1kgWz2J100sehUK6w0tZMzzbefBjaohxwf6IWKw4M9PKRTmwcZPNYMwmcg2XYJCNonZB0M4Z0-Smzd8WP73oSG4f6snj3IYC6DaWpYhakbGLNLgHE6jOzrLNhn5R2Fxl6aDzljqLC6rKLMrQwggNM1PXMQRcpXV3qtFGNGG5f2upRMnbgfgaOk9_nu94NObMQ3SaGMPlSX3eKhzk15KQvhWVaSwDYYBe9bEg8mtxzb8k8Siazm7ZKxBVD2gzr-ijhUlzntSL7tU0_x3RcC_qNsoVytQkHZfjpbRcg7DQtOiA-EcDRrZLwBTo-U6lkzBPT_K_WOwa9jCqDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rpc_bcawDon1M_cvTXGy3oBer5O2th9dSzpLl8UztE19jQdlU0gkA-BbU3FplTo_1RAgdHZOIs0ue4G_YDk4WoPcNMKsjO1JCQEpzOgp6LEizA4hr-BSL1UUOB79Ek4wPyR-pfhQymEQXtrJ393LP3uvbNcfwSNdoPvWqjkGpCYXBqmRAuEH38tASrgeXT8iwFTItRwP7XWdF1xBeWCyt7rXHdnVa1sELQoG87Gkwusy1q5D8fcKARBUDzAAqw1r2ygUQIDjh701dqWH1Qoaek8Brx4hyYxOzPTLMAxF63K3uhL4HEk9wn900GfH9dzjvu5ZYVpFZmbXBPdtr7FysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3GoXa5Cp5PkDjFwR0-xh40xvi6KyiyWkL_lvYb2zUs5gjJPfmi5Ou75lWCoZOWMU1vyOLewsP3Sw4cC4ObQikbnEofSGgZjtUf8-7pecKFuId19U1Q2alLvSBkhRiBxoBGFUDNZ0F0vHUYHuc1VL4upMapN9NvsuukqW5CMCYj8kK6UO4xhN5Q4WfjYh1TrxxB-XD6kDml_B1dsuEmT0JEPGAd6UqHoEsSA-hHwZyljcYLOvGiXLxzAo3gHrtmrLO50nDL_UXhZv3luKmMQrVcwFaRScyF_S6Yjcq5fPa9w_nacKpC20junwWAfM3y0kYIOZO0zYpNJUInaoQjiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY95vlC7OY_6U8c4QkW3nQTsK-q-ukwuQ8Q2sCuvM62TPoPUCYrJ0aDlX-AgnzrDmz_hT59Ua7qFzlKQuJpEJwhxREWO65Fji_ksiuQBqGGwk27oY5w2lWGUR3up0Bs5VAbEe7H_JXZRM4JIusuqQPRmiwDfLqaAZUyJEYBUV-c16hUdESCYk8y3zkGuUKHLANGx4jmu8CgeQaQggrtDfa7YoFdgbxAxN6Ja3ZPFB9wWIAor1OY08EcrwAePTYfM6XHmO35UIqy4r1yi_s0yX3sFKzf8029-3k0C0i8FjkoxggC9gaesn0Nm-tbrnZpRRhc6-DXrQ8FP1airl12z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOU2_x4cL81hEsvtD15xPlhAX2sg0-D-pU4FxySJD83AFjsk_XszUiYcqT032WvwnVHn9TH-0xfRsWcpfissBiQ35FDVjALWv6xo5vNl1MOuKIZmvZjHLclZ0Q0u-jsnOlLNyCT3uGnSyWu5B28FvSEslo4429g3Ta0k564HE0O8-XSIuhA39wr16RkZaliPBAXvwCscvg4lFElutLNBySPvrkHpdNNr-pkrfDQ8pigQtzHUKTzZ3LacWmfRrT8RQahMfBiDBvQg6YJ8KtYAWJQwbqeSkmNXMlEr83bJ1w9yztwc1uDB7o-83_uuZi9MqqGRfuyXxcwZ3kQUCm3oBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17420" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17419" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBM53ra2LUpiYBKXcuviZc2AWu5urMD-x8GACuloeaJvftUMMKLOdPMxt5TmpbdhicDCCU1a57QHo30HB5EggBK3MQD_7kkJ_zqMCND93L6LwC6FC9sD7E24tkCgR6rwh7SfT9hOh8P7Lzb61Gfi3z2XZnOK9Bmvxgp_nMc2nPgneBk80OhxP8Sl6iJybiyDpfMu8dS4-9Bzx5Pu6wii-g9v5DLuWNepkK-zO1DJaNkXq8Knp542lXBUn0-CDzT6NNo1VCN-R5vs-Vfj_nM-EU-XExk6cOKHAOKvAz9XJ0XYmxsDgbCkYXf-cjtKIDPTCOm2_NzzxYVV75lYp6IkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17417" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9dLDS5mPgj3sRR0qbUeXkBsWAGSbWArbLrELlTCBVvZaTMW0UOm_MN46GlYO8DU5aetlO8YXbbMQMWe2xeDWYnWarEp-OkdMqGIdNx9zOYgaJyHbtsEKBVAuZ4Yh-eKisqdWLAXs88w6tre-pl8Feen6c57GpBVU38np0fW1dNnFM1XGae8jFH0EWGtZn_ZzWqxecoZ7B0Gs7diPtGqjykJc-uLe5oJDl2S2MQD6H2vdRArntePdBmX9IZMkTdXb-6k00vZvsnUoo8JEr4mKFkf3Ldi1fqgRG3TT-hi-enn61OXMPoCh3TQlPFsL4LGVwXcrp95CZNCPutgV9FnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGfNu5dChynxwCFQzTrRxJdvi9VwRoqcpypf1Pdi_1-BuhOWQXfAXPcAdpZSoRV6b9Gs6aHdFdSsJcYkNUaPSqjGZCfN2wsmsjjQ5Qd5oOH04BeyU6fs0e6AvBJ5K5R0eZqt352EodVgUBx4yH7GiMGsEH_z4RGDQ7T_U7Nc7pZvxBagZIuyVcGbTz_n7ZABHJEhtjwEix6CJumMNtqEem1KN6S179f00rAHmXV_xhK9QEZL35upn4JlQf0ALwJf85dnypH1rRTL7loWkDBJQIJqcv3Ll2LV94YOXR8quFrnmae4ANt0mtFezr56JyMEK84N8VT2tzpTr9g86hR5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VT9C5X2gIjFHqJ5V8_cJP7wVGFw8RmMPct4eq8R9LuDXR4TpLdX-YwrP8k6BpvEVrTTgA-ohqKri9FIQzh6n4_NamGGFHlZT8Jt60RLSTlQ2rNzJPUR0CQo_La9d7WWRx0R0N_FNzMZNYE1WQUJZ_pl1jVeNUKm203HgT06yBzCVcmTUrlA8_VUY5MC_rCio-2xn__ED5Ydp89OB2h8PzA7I-p94pwxV83bXXCaHBJ4cp19vv-XpYDJmmGIThHIWLxJ5_foxd_16erCggBAvl2MfZOI6CnRCbZf-aha58y0SKUe6tK7VJzpvnXz6Z4_DPA9dHvnU4l_UuUKQ4Dg-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo6e3t7IDN2dru_xz_iD3wRj5DFyIReP2T9vOBz8-s2u0Zi1YerF0q0Ozmx-YwbiYSZgSC5nFguLfVNLoVBm744A_YH1-7Jag0iIzJ8lJtsBQOMkOl6hFp2RWBAlSx2EKhjIy9SweUTQH-ovhau_MN1SAEskkH3Ikb05BKg4-dnJRTeTgmWJOi8ZG2DDYbWfinsDTaZ8xOaaSx29QZ1FbmNJtyiG87HOvJL7r50UJAAhRNqahdl6T6pIsdSVNKJeegpkKMyZziLFmyIu0-Ksr8BUtNLqqG9z3HMQpsQ42PUcaehXfx6osu0GAT4sSEYwypF5W7hHbWXHT4LKnmAsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElrgESzPY1NzT7v8VlYnmfBmowBOBS2qP0VaMhu88inqhtluNsAjfL8QpAfyf_hWRhwqn7aMdPIMRU_US1wOB6P4jQOa1xXkv_X5FO1q2uzST_jgK7aaEtob42_9uNcR9hYGh4uvMsCsdO2PmL0bG2KcaO1LY-FoFl13R5vim0rHik4iIRT-SEwmfhRbjvo_Hy2l6UfzItkea3Rut9s0sohpL5OTAMC7UbljfuimDFE4WsI8K3Dzrm9jRVAze2MBWnQtTUVlR16IBeCCaVOeabiJKdnCgpPDvsC4r3Lzm21A43B6P6WP9wDNk6B6Vt1hzw9F6wKFqLdzXXwNlntJYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتفاق جالب در ژست‌های قلعه‌نویی؛
⌚️
ساعت "رولکس اسمورف
"
چشم‌ها را گرفت!
👀
ساعت 10 میلیاردی امیر قلعه‌نویی در فوتوشوت‌های رسمی
#جام_جهانی2026
سوژه فضای مجازی شد.
🆒
این ساعت از برند لوکس و مطرح رولکس معروف به مدل
“Smurf”
است. به دلیل ترکیب رنگ
آبی پودری (Vibrant Blue)
در صفحه و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است، این نام روی آن ماندگار شد. در حال حاضر قیمتی بین 40 تا 50 هزار دلار دارد.
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17412" target="_blank">📅 18:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امیرحسین ثابتی:   کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17411" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این یعنی توافق بی معنی است:   اسرائیل باید اطمینان حاصل کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای را خواهیم داشت و من و بنیامین نتانیاهو، نخست وزیر، به ارتش اسرائیل دستور داده‌ایم که بر این اساس آماده شوند.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17410" target="_blank">📅 18:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17409" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17408" target="_blank">📅 17:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=CucYGWd2cslrzr-ySgPsGXP2yDeWfoYGvkxHL8CTi96KhgdHqQzfE5z0clnl0eHopkSlLrdR5Nr_o22KuxCODVnggKhn5QpgrIprlxH-A1UAR2VFcKKMiEPRicVPHmy1vR_bMshn8e3-NhzoOPCCmBPpCuKkbiVKsPFp8BB0XAbjk7YIuUYJA5H2XxRPJVQ9Te9EQbmc6H0K509gryH3t63YJzAtYlNZq-mhnkAjrItL0utjqL2oq1RmNWN4h3Yv-OWArAD5rO6yDvLsixQGmVw_EFsJEs9jjl1OvQ2GORyHqKlLVYm0XDUGfHd9QsdoLoIiuaic5O3vfibIDVKDxbkpsMd9wL2NNSiSBso6tmbau30ZI8PkcTomBsDE2G4XZFN93Tw8HIjgjNy5sGisnzS3ZOiC0UJlBbXXtceV3IVjztq4g8MIslg6-tduUsXvWsRItdpxdAV1TNRx9n1prRu5GHZ9c-2gJLmQYq5m9IzoexbXRMX5kRq5Yv6zN6s58SaQU0bVErYusZZk8oylO7lK9z4T_BGyxDkVH-lYIXNhGBSIcb49Tb3pwFaG-K3UQD5Zz6gJituxtf-1q3Xwx3hCnLMWnrb5A_fPdZZ9NwD9TfVth23n25cu5JBQRt2WhDYiB6EuxO9krcCnLcrhjyagTRriN1S-706-IIDM5ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=CucYGWd2cslrzr-ySgPsGXP2yDeWfoYGvkxHL8CTi96KhgdHqQzfE5z0clnl0eHopkSlLrdR5Nr_o22KuxCODVnggKhn5QpgrIprlxH-A1UAR2VFcKKMiEPRicVPHmy1vR_bMshn8e3-NhzoOPCCmBPpCuKkbiVKsPFp8BB0XAbjk7YIuUYJA5H2XxRPJVQ9Te9EQbmc6H0K509gryH3t63YJzAtYlNZq-mhnkAjrItL0utjqL2oq1RmNWN4h3Yv-OWArAD5rO6yDvLsixQGmVw_EFsJEs9jjl1OvQ2GORyHqKlLVYm0XDUGfHd9QsdoLoIiuaic5O3vfibIDVKDxbkpsMd9wL2NNSiSBso6tmbau30ZI8PkcTomBsDE2G4XZFN93Tw8HIjgjNy5sGisnzS3ZOiC0UJlBbXXtceV3IVjztq4g8MIslg6-tduUsXvWsRItdpxdAV1TNRx9n1prRu5GHZ9c-2gJLmQYq5m9IzoexbXRMX5kRq5Yv6zN6s58SaQU0bVErYusZZk8oylO7lK9z4T_BGyxDkVH-lYIXNhGBSIcb49Tb3pwFaG-K3UQD5Zz6gJituxtf-1q3Xwx3hCnLMWnrb5A_fPdZZ9NwD9TfVth23n25cu5JBQRt2WhDYiB6EuxO9krcCnLcrhjyagTRriN1S-706-IIDM5ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط سیس پیروزی حماسی اژدهای بندر را ببینید خداوکیلی !
ولی ازش خوشم آمد میهن پرست است .</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17407" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17405" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نفت بخرید و شیشه ها را چسب بزنید که ناپاکستانی جماعت کثیفترین دروغگویان عالم هستند</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17404" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=ll_T7ebinUTwhDurJ1pWum3XztXA68PtPqXIsq0O1-pmdlxqh2BP80NrTH2inU5bR0R59B3Zq07oewho61KWZFbrif-RuoxtjrXOEnB-Dl9RSLMEQllyLEK3HrW7Lp79MlCUNfpA1s8HwAOmsfiz24m9L5djNEak8zPqku4YZJdgRZbCupULLvA2OVZPQujY8p2I5TmvaCBKs6TO1LAQmtO_GlEpZDmpzaf3o8uxRPzBeyHQGUssKpRhtOqbf1-09SJSWR6dDgxE_edgMZVSL2gJVWSrLjAzPMnWT3iFWWaeV2cGPj23qU-2Oayis7KGhISdkGq1m7rsK0kdyLanrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=ll_T7ebinUTwhDurJ1pWum3XztXA68PtPqXIsq0O1-pmdlxqh2BP80NrTH2inU5bR0R59B3Zq07oewho61KWZFbrif-RuoxtjrXOEnB-Dl9RSLMEQllyLEK3HrW7Lp79MlCUNfpA1s8HwAOmsfiz24m9L5djNEak8zPqku4YZJdgRZbCupULLvA2OVZPQujY8p2I5TmvaCBKs6TO1LAQmtO_GlEpZDmpzaf3o8uxRPzBeyHQGUssKpRhtOqbf1-09SJSWR6dDgxE_edgMZVSL2gJVWSrLjAzPMnWT3iFWWaeV2cGPj23qU-2Oayis7KGhISdkGq1m7rsK0kdyLanrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اژدهای بندر به شما نگفت ولی دونالد قرمساق گفت که منشا صداهای دیشب چه بوده!
یک کشتی هندی بدبخت حرفهای کله زرد دال بر باز شدن تنگه هرمز|ثابتی را باور کرده بوده و میخواسته از تنگه عبور کند که سپاه پاسداران به آن شلیک کرده و می‌گوید برگردد  و هندی ها با ندای :
Sepah Navy ! Sepah Navy
!
You gave me clearance to go! Let me turn back!
دمشان را روی کولشان گذاشته و برمیگردند
این به قول اژدها یعنی
نظم ایرانی
!</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17403" target="_blank">📅 17:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شرایطی که ایران به اخبار جعلی نشت داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده است، ندارد. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و حقیرانه‌شان مبنی بر داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. افراد بسیار بی‌آبرویی برای معامله کردن. با آن‌ها هیچ‌گونه…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17402" target="_blank">📅 17:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17401" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Buy Oil</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17400" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17399" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal with. With them, there is no such thing as dealing in good faith. AMAZING! Also, their totally rebuffed Drone attack last night against Indian Ships leaving the Hormuz Strait is TOTALLY UNACCEPTABLE. They better get their act together, and FAST! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17398" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مجری فاکس نیوز در مورد توافق ایران، به نقل از یک مقام کاخ سفید  مواد هسته‌ای نابود و حذف خواهند شد  برنامه هسته‌ای برچیده خواهد شد  هیچ یک از پول‌های آنها تا زمانی که عملکردشان را نشان ندهند، آزاد نمی‌شود  تنگه هرمز باز خواهد بود  ایران هیچ گونه حمایت مالی…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17397" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17396" target="_blank">📅 17:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17395" target="_blank">📅 16:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایران وضعیت تنگه هرمز را به سطح قبل از جنگ بازنمی‌گرداند - ایرنا</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17394" target="_blank">📅 15:44 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
