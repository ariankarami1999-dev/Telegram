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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 05:10:33</div>
<hr>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrVzNsGF9DYPeAuTCD8V0LAXO-Nf24jPpEfQqI5VB3q7x-R4gyrdMFaE-z8YZ17VbXcuH9kuU0FVXS6E_7auLFYc1buSh1p81ftQGGMLfjULJHRjcRPY643GRBMWA-bTGEoRgGDg7N85kWLCh_sIHtRTlm0tjGivJJlwxOXuCIsvLXWxg_gVrHLwvpX8otXkvo5teY7tp7enmBd1HoXIay1fOrOJxWSa-Bx4o7KQ3tTGqpfT9kaNBFrTKLoENiLbJ9epP6hfge9gJAx9t0mLaIhABiZCM5AEV1KT-OaGEJsoul-g0VVMpqN3b9bddt69N3vKdgzsb7KYi-98BSkJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwIGjLTefaBj-KDLC7SBtIyTo3jIxMkYHTJoJyyFRFYEQzMLZ5uv6HkG9g6ZherRi4XuUR5VMTcJHMmLBtN48yYVJZcWHgboxMxR7pmRC-n2HTH07MNXakUz4dZqft0yETzToN5Ik4wCcs8tq0DC54W-ShoEnuxRdSrg1Ym8jNZkhrHdpVqRuJAwrsYseykbyF-SznhHRqrOHingM0LmrSQWN8SVL_SiOhrnELNynZ5Oea71mhOaGiTyYH5MnR8cW1Y3z192Cc9JXdrEAClN82M1dfGKj-mIVcmQ0Qc56iJxJl8PSwJPwNfGznmBMEdsnRhbyD8ScSn1vEfvTA4bOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugDXjEZHUWrUrwPD7QnijDh-mnINI-xy2Dnq5yq2msVoMfueZykgFkId4EnBcGb-LoghI4CRhsnVuMDnXu78nvJsrWaSvmuSaDwrLhFWC-4lJb-O2Vv98mbWgxYkIStlsGVPy6nt-UdiuMY4ceZLVIEYJwrZckh0oJerYj-dpYFE6VhdoMeb7iMT6up5JfaUtoG1W415u1zoZ7_gDXXF84D-oPt5OyQTpnDTgD3cZp7ef_1poR1EQmKQ-QgLTasC5lmZnF0bn8HrKYl3LVsmEekJGFbRkD0Z6UAPJaxsgYXqtGGr5HUcrtJ_87jlfWC5pEm7a0tvQULMQgay_U6v6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI3Y33jxpwdUI0CahZ7890zmzCwkiUr0CnOhq1FtOpOlFBm6GcxupruVhAFaTJYyOquJzYQN_LxjV7cLEBGZ5KV-d1_y2fJlFimZ9kxFQ5_ZAyq-1Usz-CIlol69qoFbF1jV6XOw-Etm883T4yrY5bkgsJnopqbBJnCvMVdfBGL0ls_pOzUq1M611R-kAekmUafnodY-yviMn-5psxA6psD0zDopAt_1cVV63hylT5JV7kiQshjBmkT4LyFeQDn4Sutjkw9JByEJYHfje3dS9VT4tFC_okHK5-NlgpId4cl06_5EkcFiw8ekjvYQHqjVF0LjWR2t_jZZaf1nHUf3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17467" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Y_fId2-qBIOrrGE3ELkL6-kflWKssb8-Q6XUAYWYmoC8RV9ex3xpPAF-WHXVOZj-i-olmXbh5z89qiaaZeS8fexcnDIx_A0uX1eeHrUA4C74hNxeFAmIO6h8M3pXrAa7rb6qvCIwNLBow6sm_RTTv5CIWQtjAAKdJRMHu_E8ZK1VJCZbusiVpNnVW8WXOGHn3r5tezER97HSNq-N-vyyYPQH_yKnkqVnrTQz7gwGlWUWptLYVsTF7FZA4AbktPTMxmgR9T7gNFyrybzKAwfaJgCGlziq63kX7WDt-CYOmSrOj4wa6uW1ZGu6xeEIEbFPqmyfdmdYZYcQYEawMTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت را دوباره بخوانید:  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  پس در واقع تنگه هرمز برای همه باز است جز خودمان؟!  سبحان الله این که عکس چیزی بود که میخواستیم!</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17466" target="_blank">📅 18:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me4OA9SApeGgYRStKf4ntevr7MP57tGXlutev6bRChLcjPHfXFAh0liMD_mGvMQ1qdc2Sk1Daz29LiVyaF2ebQhC3geupnzEAGbmGoEdo1KKOWwGTyf7ZsMXEcYfXkmPUsYS94CBHU7Lni5EHzmUYMURxHmnBbwUa0Z_By9n-mGdkD3RHXAi0qEhI4OzC_Icq2VIFwQTvoJQOzcMKCQJyiUKaEWrzVx-bzxjT0E1iLy4_YVPOdazgwMCohkR_jBrgozrWXv7dKpHgSfIeuz5yL_UKuGl74ZxEeKLlfUy-7ij6wOId3idyg7RJj9g-wNLMXocqkNxywoO8PACvYh4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxuphKb3wXAnp28D3F51SR669ALocMb5Pvz-kuXF16n3jWW8rQ6AS9ePNSgDaZEezSWfBa0PRnz6fBWMBz5RTGr0chKt5wL0ZGsFBnZnfRzdonYvBje7-kXQmezlvJQTo_UheTHmGoGOtV5X-Q5hcP6ORCpgWsJ_fN1vXAhrZFVxkUzSZfzayHi82QhxW55bN8osOfZ_LTkt0JtpTPny5DNCepS4inG2w4V0SpRlMUOqhOq_BpeVYGiLJWx5XmWc94MN2mf9LTOT00T9ayycEIKRZG15zW1LgU_OpQnxQST3IMRMtMTknlVvF_OhjbHn4w_L_WgHD3J58B95MuFZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=jIYILmrQoQIlBv9oY-crJ4nnhWvP1ZJo4GGmJ2iz_pGDo9tXbqUrBSCvgEYBphWNbePSlzFfeuCyUARzdjuN9AJjoz5nDmw4qYBSg4GQqmLXljr73Ovh-0C7j228rHqx0Ia8uwID4JwWuk-sN1DUkS35KwbRtzMeubWEUHthf1XK_12NG_IsWiU-azAHBnsWMrBlKcfQ01a1bFphJGCncbBU5My6lIrwJLtO6X_oaaKla4n2IpbDuEIOcqbMVYR0maAiAVuAnwlB-CVjm_mJNVAdHnURffmdWWwheOzJcE6cngxuEl4WLvwH9Va4CdzsrDR-T0feCV5fKiQaKRQ9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDYI5rLuHOa3pk0Um87yViAW_n18AolKvrBuooaD1A52CyCyM2wgS0z6V42mrH9fc7xV2XRZ-PuBo4O1wXrf_SdtI583Y3VoCps-5Zmp0u3HUymgvJHs366CCetoCIW0lh6x9GaWtnnQnyQOoLgP5YSpOf1RNRgIhjK4f5rW7UeV09VDrfbSZwsZUC2rqTH7qH0GU1kS20oCZS3qvNxQpyeOgC3FsoR6cM5Hq1nafH_Nxzo_b_f1dfTd87HruHm1-3ZCc0K6LwK_-Aw7XahO83scrq6rcskY4hGqZzLUXxBJEHBr3dbtXkR1DDE1TMWDKiIpQdBT1OLP3zk8Ded00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPZyQHdMM8DF9bR8RVaf-n9cDa4w51P2dXVjX6d3hOLckCiQ-Hn4U-S2ygRGXDWrTHwzq2GA_ddae0OQch4fDDc3kUzfe4TAFY32CkVLWP-_FzkNZ4n3JrAEpWC5hkoLc86Om0ryvH0mFS9Ssimv3bPa1FQVYykMhzuoAKQrf2wL4XcupgrhQ0tHpdBNHUJnAQMcxzhUMDXvS0yjtcSbClhZkfu_O0Jv9DxM2hcQhykWkDMZSrlSg6bYQXS8XoykHDRZH6-e78qR5ODJQwpQVHjfaQicnI8-VyW0Qa0s7rH9-L6dT4RD3NJkQYpZTeLJBHDH_FOVzQ8I6kmjNBjtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R39nDT3gRHgF4g6a2QqQL_NFUYX_nm9uYIbEN8f2BcK8-gfWi7et59uqO2i-OpI9Bhp334xGcol87hJ9R4dVatNERrsKqgoIk54-QUE54HJ4lJbIjznKlMbnu3XlRXziqdW15qeHkzkx9KJFTi4NWQUg7wPR8aRywQUVppWe8Sbrn4bxXz8QOI1YJTcqFYW7xiZpXFMvvijt90ZA8v14R0WSsJHctfM2b62QBqmR8XZCaBkWjODPRzJF6mpQlaLGOb4B3svvylslVjcqzda8gOh5BxOo7faOYlZ1iPcuzIuiqCU58wCgPPoY54ipPXWa6YcpdVy9mwxkWKloEjC2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLYTCoHWqTLg-M1A4c_l6e-tLdLXe9V1okIu8odP7YuXMP4gyxp_IMg6OrkNIhmBulZOVDrP0S5UR0V5GwpHp7RkPwxKwnh8JPMVnFu0uCquwF0mq9k2yD8Q9p7rHz7USSnHD4G_coOrbXdl4mTWV9ji5mfTP7FqeU8WK71g4bMitOnSMITFNn8JQrCJVET4RRa4AbazPdWqJnLZ_OZkzgZpNb2jedQVLdiqwzx-KqMBfDRFeiXDZldY2Xs8Qw2eDHfePboKjmG2rDtAG2nca5ecpvdi5Tsl06rkDJGWkiJmBa9zTX6deLm_fth4FkSdH-ykw_xXfqCJ17oLtb1PRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17444" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTVoeL1eNqwuTdS43yh1bU9XzUxX-6nfio3Bj5diSzWQp2KuOiNwaWF9oWLb4XA-X5Dgz_ZkQLOKHbRRwjMqGC9QVdKiqyaLyvYgG2NPE-hoYILtTeP_Bcs_9BeSHKJP8GXuroB9VARokTa40ug-Vbkip13NtJ43FZJAdXWwG5vHw6XJYJuwvrP2ksU2ScJFqdztuWxA1Pbfy9ayZEmLbMfltXGx3NnfUclfsSOPmThprPlspS8YvzsrPUyyDqOO763rLMtRXfCr0vUBClmWyWAb0Z_nLxGnZahOAavMxHYnfT0AeJLzbNL5v9DiqCVLP5-bD-WtBjOP1iruTWj84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17443" target="_blank">📅 23:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حسین الحاج حسن، نماینده پارلمان لبنان و عضو بلوک وفاداری به مقاومت وابسته به حزب‌الله:  «ما به وضوح از سوی ایران مطلع شدیم که لبنان در آتش‌بس گنجانده شده است. مقامات ایرانی به ما اطلاع داده‌اند که اسرائیل طبق توافق از خاک لبنان خارج خواهد شد.  ما هرگز بازگشت…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17442" target="_blank">📅 22:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17441" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام:  کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.   تا امروز، نیروهای آمریکایی ۱۳۶ کشتی را تغییر مسیر داده و ۹ کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17440" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm8pXnRI7bCCp_Pu5rhXyPaDqZqVMfrYAiJs_FoaeIYCiQrMp4XorhSCGxnknmsGe2LiaSvfP5hRGHciMRSHFw6TMcJmzNQLfNzmtNY4s8bQ33wiz-lNeZb-F06tzGqZeuEb17Mx9rPoXYnW39Ds0aCiCw0oSGMFjE2rAVW3zmBql3ybeb66k49hm-WjI8r-JsbkmxR5aA9Lui1uBFccLoBMxcc-Qp1p55UzKj2adws13DQU_iJLqKcVdTaB-EcRymOK41f5JztJps9DgWcTHJtnhs2jZwNaAHn0xJ1iDppTcEzQwAf9y0xZUIM0NtFvq0NsONA9XDti-KrD0cw9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
نیروهای آمریکایی همچنان به اجرای دقیق محاصره علیه ایران ادامه می‌دهند. سنتکام از ۱۳ آوریل تاکنون ۱۳۹ کشتی تجاری مطابق با این قانون را تغییر مسیر داده و ۹ کشتی متخلف را از کار انداخته است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17439" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— وزیر امور خارجه پاکستان، امشب برای ادامه تلاش‌ها برای میانجی‌گری بین ایالات متحده و ایران به ژنو، سوئیس سفر می‌کند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17438" target="_blank">📅 21:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مثل این است که بگوییم شما نزنید ولی اگر لازم شد ما خواهیم زد!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17437" target="_blank">📅 21:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf_7ufQnU1_Osw4XWt9rajC4Tyt9wpnoaJbOhhHINwZgBkmfu6d6bGhyPt0pCfvA41AL3XnevtEun-Pexp3kTujiJLlzMaBOP1Cxrppm_FGbMaz0YYp2XfTIwZUndRbsd4xsULOyKRb3f4WlV0ngnIX7GUwJkNlwhjYqMTI9q4ZRPT5YEg_UKGUYigMmZSzzwEM-HGZ7hx7T4FfAKvoAggLBAiihnTVWSfLNahYHwHH4IkZM55pgTctOn2Tk3MJf-RynmdkT1MCqb97Nv7Y-ckkomCvQmMqyE0iDtoaiUY5puf8z34VqhjUaiBsAHaCP5fzpLHd7gaqF_mFuS50e-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17436" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:  ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17435" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مسئول ارشد دولت آمریکا:
ایران متعهد می‌شود که برای همیشه برنامه‌های هسته‌ای خود را کنار بگذارد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17434" target="_blank">📅 20:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقام ارشد آمریکایی :   احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17433" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقام ارشد آمریکایی :
احتمال امضای توافق ایالات متحده و ایران ۸۵ درصد است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17432" target="_blank">📅 20:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17431" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقام آمریکایی: هنوز به خط پایان توافق ایران نرسیده‌ایم</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17430" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیروهای  اسرائیل تا چند کیلومتری شهر نبطیه در جنوب لبنان پیشروی کرده‌اند و در انتظار تصمیم رهبری سیاسی هستند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17429" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خداوکیلی راست میگوید!  الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!  پینوکیو با گربه نره و روباه مکار بهتر…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17428" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MguZereDGdlJ-NBqz8am00jAZijaXa9HsQuflDa6P56m38JyQaGfFIZAnAfH_k8EIwGOhMPC90lqR6p0ArI0y_ZE8RkjHzx9mau8cjhsl1lr9_XLlXV-Y3ukB-NH1pDu2aMFl0bo2n3Jo4qvmxSg5R66pk08CqylHUT0vicc1KAFqmCiXA9Rj8gfqocoOtjVe417uPhpOQIAzM32dXiPNN-YliDIzgODpIyc-icsRwZ3YGYanlA-ohZKuvO32s1MBKjq7Oz0z8aXUyR3XL03e8uh9NOLgCetgGBRDrCWNZpnMblxQdMVpy3SxMpghHr7mAujqERl6J_FzUVmerWqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی راست میگوید!
الان بیش از 150 میلیارد دلار دست آمریکایی ها داریم. آن را به جای اینکه به ما بدهند به صورت قسطی به ما و اعراب با هم میدهند! بعد از پول نفت خودمان خسارتهایی را که خودشان به ما زده اند جبران می کنند!
پینوکیو با گربه نره و روباه مکار بهتر deal می کرد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17427" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه  اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.  این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17426" target="_blank">📅 18:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">توئیت جی‌دی ونس درباره موافقتنامه
اولاً، ایرانی‌ها هیچ پول نقدی دریافت نمی‌کنند و هیچ بودجه‌ای صرفاً برای امضای توافق یا حضور در جلسه آزاد نمی‌شود.
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
t</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17425" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5lNbJxuIAjT5F0ytqRQlWH48dRGQRw7ZcFtMprBbHtKB_eMrTsY7nFw9YYaSpBglbLqFX6Djax0szkZ1nj6xUioJR-XXsun5Cwf2YIWlBIj2hxYCF1T5H7OxXLhaAndxC4FFOILMPXVxUXS1ojRkyzvyibvUuoCW1MS1ytOVHrdldOjWNIWr_QDKYcsxVMMHF7xpn8ESuvj2AEA05Au_TqaEwM01EZobPIRdknLTX0Wo__uEFCxf9EJ9h0PaFK19km4yC0oC3ZsNop7i8afuvKRR7nfDC6x7FDNdRhlGSHMxJdr8Z5gd5wyIAO-AaGfFKvoR1VwFmZxzpxQrg3zBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه دیدید یا نه؟!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17424" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mc9-QUk0oJAwXXNoqX2HAPrumisEwtA7sH7WEbZGOX1e_fC_3PUxgJcUFwlGtC3IQsl37SB5H2z1tapt9VEeaUv6uma3osuQoVQy9u-81rSLL5cpnMba7nJS0vnTxeg2w_MiYOE7LHR5hRry_r3It8_a8YlOmILwA9AjG2fQ1GexmBnDFRbNBdDSTNmKC__WWVUghEQ4DIRcRSS3SpY4J5WpdS-JubeEGt84XrG-oDC6ODk4ZhOFGOPUzo2Q3px3Ecth69o49djOXHWcOMByl-fsskQxlFssygcgmyNT2QK51neNI_yHeVK6sEWgWpRrz6Mu88Mf01q-logyNgdQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17423" target="_blank">📅 18:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر خارجه ایران عراقچی:
تفاهم‌نامه اسلام‌آباد هرگز به این نزدیکی امضا شدن نرسیده بود</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17422" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17420" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فوری | یک مقام ارشد آمریکایی به الجزیره: تنگه هرمز باز خواهد بود و هیچ گونه حمایت مالی از گروه‌های تروریستی توسط ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17419" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD4kUKyak3KRzzs0SYMV4yqfOdrGEVD_cIvy9aqRFGa1qKYHY8jso7sNGXukFuHAB38YWjHMaWvSR_mo1D38L3T1IGkWFTN0ehdtpZQTpnVdq15yBx2cKTHqVVJkcW2exGZySW58u2bWjMdSANZvZQ2KblqPe-RlcWwsH714mu0vSwZgEsoP8_C9s3ovPtuQWJ2iHOIOKdzpW5M92_OzPncry6yLpWGppIRK2YI3c8jzE1EFite7DQKRWDirQ5InICwompTyW5cXLm2ha_jz9qAh9wEI2wESktvDIw5ruNZh8Yxfc57cGAgpNj5sf8kXDMILU71UP6lM6STZ5Wb-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17417" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6EaQqV-Nrvk6wO5zCVADyYvdXY1faXdpaPlx5oYqrXBzr-8QpQkFnL_BGnkbFMtN2r5WdQ2c0oircVJpDnXOR-6nrk0ufCsYmoajylynOtZdWKZK57Dg2rqXGGwzGbWg6lVRLxQaGfcKIUmd34Keslcl8p8oDRYos484zjQ3QlzzIuoPVlIsxwprQ9r1oiGHqIA7P6Pd6kK0WYBfnsFoARZ2aalRvyyZZf2Q7j80AsVW_nkWRT8_uz_T_xVYGOMfeai1VWbKzAr-9EifJ8TQtHl9cMhAGQN5jpiroOoA9QkRSiFad8hVlLnnJDh4Qu362e4mmdnTq1PD1BXQpZf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOf3435zOTm3xTDSE9YhEyK7H1NZR75-UrHQ44zbobg3rZg4MbhZBGaOhwTIV3N5_TM_I0fcW5KKnBtL86dVg5psg73J8Io4QrHkdEfs-u1-BHQypQTmUAFOe16TrRx3WBBTDqEsV7NvIMLfK-rUwtbIaq0NI00c_yvI80lqOWqJUigk2JgPtHblW5rwzbH5teWB46BbeDF_knqgpzIS2dYBiM-S1csUELgQpZuvKrJo16ddKuO7vcZf1MFdZ-HzH2sDyWKr_gQUCZUx2WGo8rdxX7K4nsNUmjWrSj7DwSinuyyjprbaHAbBiwbWsCvZRFp1REHYFtaMdz4e1GDNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Erq3LOvEbeKTgX_S8V2hr_mOPNCXhyi_0SBzvzEjWQwI7EwziQVrzX5PN0faUpMev0YAWb-JTzC_s4p6RSq9k1tqbp0WK3fIq44kE_fx-7yb_HSQ-ygwkE-XnzUoINVlNWBkXDKK4pf3xRB9LGMwJZN--UKZFXW__bNpMuTVUZWqfrOIVx9l0PqaAzIFB9IP50h7Eqvxq0O7qjI6zO0LA74QVM765Y0AWl1xnYVc1bd5Mpk3v6R1CopG1MOvWZC8WbUuqI8gxvP0k2zQ4cqiVqS5WWtoJx_2Vdl27WPGOqXf07bk9ermePiuQpfP8koSnasAVip3eq319GJIkffsog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkvQCP7zKIPhbaYSfPrScH-T6FtQaqPZIbj3PUZXH7YcXrIp_MZI5qRqSQpizB1ZB0FYz0E840QTyRiA6OZSXbzI-VbKRDf2K8bHFuVrIggdseQcdEL2snmyWGpZTVPVFV-Su8WIwyp6rxOmqAdJT6Q4zf8qQsDUNrkiVzLKaT7cTRciDqvIDGDsQ9QgrljKsBcLYCFK37dPN4cvyqKYPbgPfXvfo6gWwLVEIapsEaHM3ND4gXuGqGv-i3GNdDW6PwtT3D3zGuvPUwEswtZwkp_1rwPmGNggPFVkQJ3yATT78daovwD_QVfNFRANSVttBmLcQTpr5_ftC8ACLdSsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRsYS3owcBIURbRGQvSxw_VcCktxgl0LitE4U1MRPHTjsSBR5_dwyV_0XvMZCXufso33DhoNx0eT7nac4h6MBpgz5F1X0K9JxaN3Vv_t2BrsL3LeDrpTWGvb96ZZL3eDtzTNmCIMUIxlr0hOsRug5VvQ2TpdisVZX7oYKa-7nAuQ13_SWe_ji6PoKd98lNginbI88RpJIBGPj_sqZTkzu0pdWJRtG8o9PRhqAo6pJMYSpppv5h7Ctq0zH2EHq7ShobhA0VAp6OxEl65JfUm_US7zvFKN7ZqpKw2HJ1GQBEklVd43FhtQSgCyL_iZbNGR1HdUlngp1zlETy5YYSrcqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امیرحسین ثابتی:   کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17411" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این یعنی توافق بی معنی است:   اسرائیل باید اطمینان حاصل کند که در آینده نیز توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای را خواهیم داشت و من و بنیامین نتانیاهو، نخست وزیر، به ارتش اسرائیل دستور داده‌ایم که بر این اساس آماده شوند.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17410" target="_blank">📅 18:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر‌دفاع اسراییل:   رئیس جمهور ایالات متحده در حال حاضر با توجه به منافع آمریکا، از جمله منافع مشترک با اسرائیل - برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای - در حال پیشبرد توافق با ایران است و ما از او انتظار داریم که این اصل و اصول اضافی را در حوزه…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17409" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب این نخستین آزمونی است که باید گذرانده بشود. ببینیم در لبنان آتش بس می شود یا خیر.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17408" target="_blank">📅 17:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17407">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=Q5BwmqwpKHbn4UyMCDbanz_GE386l1zEQbJfEqqQ4k0l1dmjXjdyeUGkr7eLCODuhO7ScML5WJZy3DMr5yvK05UN3HGcFycZDYElcqagiL7N5JatVp4bBdzPdrUt-V10WmZ2BHwuJSIWo9h4BJj4fVPNgiZ3MbsQSsBgdEchSZAUnJ7FhRKVkLHk2QrgPQpKK0TYOE98Ml8UstT5RA-B7dEYI3dwilpdsBjbNYPgo9cgVdtEJ7tsAI8-YhwGmdjXK3LfPN1Ayea2a-BdL0p81hhlDUH_IOLO6LMcYEvYC3O9UYYGwoueUsW6JqRpYwpdMfZNYMFhOJUBMk4GMwGDrK3gDzhOAzSr1r2knxL3e_x7U7pzsj3rk6_wpiKDqsBbyHP_HpQfMmgKJRu5Y9WnUraoMZqKGFJEL0173R6WJLMTd2JTmVyM_y0Rou71HHm7ddKu0UJ1srXSpfVQiBTpLmFF5VcGbrjm-Zz9qTPWPIL_FEChGzQKgJywV-HjZuOi1cBoeb7g9QMGmc47pUtFG4Q2aMvJbjC7PXm-FCnrpvrEUfAU_v2_PHNhZU-_3sUtwxNUq6UQmogPTz50pJit9bcdMPc-UsV2myP8cx3OhE9SDf3NVNY5YGq5fIESgvUNoW0Qcyi1647-eQc9MgW9tv95OsSmvz1YEvA83_AS5go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=Q5BwmqwpKHbn4UyMCDbanz_GE386l1zEQbJfEqqQ4k0l1dmjXjdyeUGkr7eLCODuhO7ScML5WJZy3DMr5yvK05UN3HGcFycZDYElcqagiL7N5JatVp4bBdzPdrUt-V10WmZ2BHwuJSIWo9h4BJj4fVPNgiZ3MbsQSsBgdEchSZAUnJ7FhRKVkLHk2QrgPQpKK0TYOE98Ml8UstT5RA-B7dEYI3dwilpdsBjbNYPgo9cgVdtEJ7tsAI8-YhwGmdjXK3LfPN1Ayea2a-BdL0p81hhlDUH_IOLO6LMcYEvYC3O9UYYGwoueUsW6JqRpYwpdMfZNYMFhOJUBMk4GMwGDrK3gDzhOAzSr1r2knxL3e_x7U7pzsj3rk6_wpiKDqsBbyHP_HpQfMmgKJRu5Y9WnUraoMZqKGFJEL0173R6WJLMTd2JTmVyM_y0Rou71HHm7ddKu0UJ1srXSpfVQiBTpLmFF5VcGbrjm-Zz9qTPWPIL_FEChGzQKgJywV-HjZuOi1cBoeb7g9QMGmc47pUtFG4Q2aMvJbjC7PXm-FCnrpvrEUfAU_v2_PHNhZU-_3sUtwxNUq6UQmogPTz50pJit9bcdMPc-UsV2myP8cx3OhE9SDf3NVNY5YGq5fIESgvUNoW0Qcyi1647-eQc9MgW9tv95OsSmvz1YEvA83_AS5go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط سیس پیروزی حماسی اژدهای بندر را ببینید خداوکیلی !
ولی ازش خوشم آمد میهن پرست است .</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17407" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با Secret باش خدایی کن!  با Secret نباش فقط برگرد!</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17405" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نفت بخرید و شیشه ها را چسب بزنید که ناپاکستانی جماعت کثیفترین دروغگویان عالم هستند</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17404" target="_blank">📅 17:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=iK23T8LlnJ7RaSVWj2UuafNLotB8wc15gGasdydafCAzkdH89nmRfSfN8VlQWzTFM0jiKSAs03VBG-qU9UB7tZPLhJUjH4bXnRHbWCNEXCRO91tfW_wGENPXgYXsLequd0czgcbtoa1pc2glRRr4AKXzKsQt5xD-T-Cg8pWJjRt_D2BmR1RB7GNFIsemrUTr7xO4IZzmrqPFvW8dBGjv4otCOzX-2L_TdADsXVWGMKfLiaRiO7TFun5WNU2yy2KekVGlkDYEEmS_qWeSNlS__d_I_a9LUntlGtHY1lEtRxUhstGFQfG46zhav_45oJacYQwFYD4-NboFNQFOZ7w5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6ec42ab9.mp4?token=iK23T8LlnJ7RaSVWj2UuafNLotB8wc15gGasdydafCAzkdH89nmRfSfN8VlQWzTFM0jiKSAs03VBG-qU9UB7tZPLhJUjH4bXnRHbWCNEXCRO91tfW_wGENPXgYXsLequd0czgcbtoa1pc2glRRr4AKXzKsQt5xD-T-Cg8pWJjRt_D2BmR1RB7GNFIsemrUTr7xO4IZzmrqPFvW8dBGjv4otCOzX-2L_TdADsXVWGMKfLiaRiO7TFun5WNU2yy2KekVGlkDYEEmS_qWeSNlS__d_I_a9LUntlGtHY1lEtRxUhstGFQfG46zhav_45oJacYQwFYD4-NboFNQFOZ7w5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17403" target="_blank">📅 17:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شرایطی که ایران به اخبار جعلی نشت داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده است، ندارد. آنچه آن‌ها گفتند، از جمله بیانیه ضعیف و حقیرانه‌شان مبنی بر داشتن یک توافق، هیچ نسبتی با حقیقت ندارد. افراد بسیار بی‌آبرویی برای معامله کردن. با آن‌ها هیچ‌گونه…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17402" target="_blank">📅 17:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17401" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Buy Oil</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17400" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17399" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">The terms that Iran leaked out to the Fake News have NOTHING to do with the terms that were agreed to, in writing. What they said, including their weak and pathetic statement on having a deal, bears no relation to the truth. Very dishonorable people to deal with. With them, there is no such thing as dealing in good faith. AMAZING! Also, their totally rebuffed Drone attack last night against Indian Ships leaving the Hormuz Strait is TOTALLY UNACCEPTABLE. They better get their act together, and FAST! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17398" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجری فاکس نیوز در مورد توافق ایران، به نقل از یک مقام کاخ سفید  مواد هسته‌ای نابود و حذف خواهند شد  برنامه هسته‌ای برچیده خواهد شد  هیچ یک از پول‌های آنها تا زمانی که عملکردشان را نشان ندهند، آزاد نمی‌شود  تنگه هرمز باز خواهد بود  ایران هیچ گونه حمایت مالی…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/17397" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17396" target="_blank">📅 17:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17395" target="_blank">📅 16:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایران وضعیت تنگه هرمز را به سطح قبل از جنگ بازنمی‌گرداند - ایرنا</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17394" target="_blank">📅 15:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17393" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل هیوم:  ایران موافقت کرده است که اورانیوم غنی‌شده خود را تحویل دهد.  از غنی‌سازی بلندمدت صرف‌نظر کند. آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.  ایران باید متعهد شود که از به‌دست آوردن سلاح هسته‌ای خودداری…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17392" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">متن کامل:  خبرگزاری نیمه‌رسمی مهر ایران فهرستی از اصطلاحاتی را منتشر کرده است که گفته می‌شود در پیش‌نویس یادداشت تفاهم با آمریکا وجود دارد. این خبرگزاری به منبعی نزدیک به تیم مذاکره‌کننده ایرانی اشاره می‌کند، اما جزئیات به طور علنی توسط تهران یا واشنگتن تأیید…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17391" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgspNK7_LMTH13IjIRoNjKEriHPRYgGRQa8UsyhsI9jd59h2aR1bg2R6MxR6l7CKxbGXwF8X6N-b5cozazWG7kC_w7l8oNi-FNJKJDXpBYx7UJmC1x8T5jAT4wL0oThTwfssQV9zaLeQfZQ9YSMw1ehPlbw0rXtsP0khgfb3qgQVnB13HZUMMJWPGVHMElfGJWvdSzVmCAGe8X1ZJhHljOVRpsZCSkxN3A0t5ocy153G6qomGyDt7dzkeZ6cceO5nYrgYsMBFZa1l_FXt0pSUMqfgorYqEWV4vBkCVF-GRmpgfpHbBiY4J1-TAgTm7TdGlo1JCG3mDYVAirsgnlWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزودن شدن 1500 میلیارد دلار به ارزش بازار سهام آمریکا با اعلام توافق دیروز توسط ترامپ</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17390" target="_blank">📅 13:12 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
