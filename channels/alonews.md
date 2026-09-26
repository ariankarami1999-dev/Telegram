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
<img src="https://cdn4.telesco.pe/file/Ba70mH17qF5gSeJsIf0rVjuOb9zuzSqTcJ9ZWYCNaJSEbL28_wf6dADtwE6JSe5jaapxqEpYKe_npGHzgc-6CSmhK9OWZIqZKWCj58UMZzQke5sDJf3tQDF6mN97ZBLKPRbig7MYAicGsmOG7uLr93t1zbU0bq8hDXXZpFOSur4tMMmqpePiRq2wybgWFL-ooGizF2FeteTn1rG1zRmwaxnAG6krq2dY12p3yMbPK90KCPqXQi1Mqd9j30sHdz4trlqGdAZGJSh0EQNOCHLWxZiSL01yNnBdPX8KNa3v31AdBYrEvYZ9FvBQ1Oooh-xkSYQw_VbM3XtT4XQkqWZ_ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-149582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
العربیه: ترامپ به تیم مذاکره‌کننده خود اعلام کرده است که تیم مذاکره‌کننده ایران تصمیم گیرنده نیستند و با آنها نمیتوان به توافقی رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/149582" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر خارجه عربستان سعودی: تنگه هرمز باید به شرایط پیش از جنگ بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/149581" target="_blank">📅 20:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtdx53AunjU1_NSCu0gvGSsI-3_lPVyvPb1bKH7r8_uU_7zoUtimffL4ojxDvnAUfyhydagGrYyVZzMR58qeQqIf78RfY18Hfshjd_80nwR5-7DYpL3k8IYJ1m1eLlQ2p-5pWdJ0oW9oCdmpy12b232cowoOetPut8ovSWIBVe8OCBT-sSbeEGu8SnrBItOUY9bJ6xTwzxSqQxeCWfGmQnQINt00ZAn1zCjXTXfmVXVghgCmzsI6omBTUWgnGPdadGSYtUDe6_n4oTUc4TK7PJNqyHTlrJ9J1-Ttz7Cp8oaQCq-EkGtvzDFqGJR86BM7SulOvIIaPWWOYOPhxLZwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات برند های لوازم خانگی از مبدأ کره جنوبی آزاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149580" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
لاوروف: روسیه معتقد است زمان آن رسیده که به دولت فلسطین رسمیت داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/149579" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
لاوروف: حمله به تأسیسات هسته‌ای ایران، اعتبار آژانس را خدشه‌دار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149578" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روسیه: ابتکاری را برای برقراری صلح در منطقه خلیج‌فارس و حل‌وفصل بحران تنگه هرمز آغاز کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/149577" target="_blank">📅 20:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هیأت آمریکایی همزمان با آغاز سخنرانی «برونو رودریگز پاریا»، وزیر امور خارجه کوبا، صحن مجمع عمومی سازمان ملل را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149576" target="_blank">📅 19:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: در نیویورک با همتای ایرانی خود درباره تلاش‌های کاهش تنش و تضمین امنیت کشتیرانی در تنگه هرمز گفت‌وگو کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149575" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60465d9694.mp4?token=q4_NJ19w_hHQwnV2Zl8DLp0JGO--wgvU9lYf_JBzlWCh1h9RqKiWE6RIsqH4h8ZHRt0p9JkXrC-N4Hn6wkKHTZZoA0C3fkZiqKR5jM2apZGj1GOLU8x6ivjOeLjubuin1_ZaCVMXu7zF7dV0wZ-T9OkH1d6jzmornWjY0eTUB5BCIgkdrWIxkgej1xtlR7Yr_Ure7qBCHHo3UfTKWGJlOcl8XnSFJS2C4IeGoIPrQ5ijLo5tRVloHwpih5y1hUOXZ3mA-YPr8T-i9a0lJNPGftvhLM-RbmUjtjkviCMqb8og9idB7mNZlOG-fnQsA6tPV49s7iALIxmETVdW7MsnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60465d9694.mp4?token=q4_NJ19w_hHQwnV2Zl8DLp0JGO--wgvU9lYf_JBzlWCh1h9RqKiWE6RIsqH4h8ZHRt0p9JkXrC-N4Hn6wkKHTZZoA0C3fkZiqKR5jM2apZGj1GOLU8x6ivjOeLjubuin1_ZaCVMXu7zF7dV0wZ-T9OkH1d6jzmornWjY0eTUB5BCIgkdrWIxkgej1xtlR7Yr_Ure7qBCHHo3UfTKWGJlOcl8XnSFJS2C4IeGoIPrQ5ijLo5tRVloHwpih5y1hUOXZ3mA-YPr8T-i9a0lJNPGftvhLM-RbmUjtjkviCMqb8og9idB7mNZlOG-fnQsA6tPV49s7iALIxmETVdW7MsnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من از الزیدی حمایت کرده‌ام او فوق‌العاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149574" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
چین: از بازگشت آمریکا و ایران به توافق اسلام آباد استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149572" target="_blank">📅 19:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه روسیه، لاوروف:
ما بر آزادی فوری مادورو و همسرش تأکید داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/149571" target="_blank">📅 19:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عملیات‌ نظامی گسترده‌ای علیه ایران در راه است
؟
جک کین، ژنرال بازنشسته ارتش آمریکا:
"عملیات نظامی اجتناب‌ناپذیر است ... حماس در حال بازسازی خود است. هزاران نیروی جدید جذب کرده‌اند و در مواضعشان ذره‌ای تغییر ایجاد نشده است ... حزب‌الله نیز با وجود ضربات سنگینی که متحمل شده، همچنان به اهداف خود پایبند است. ایران در اینجا مرکز ثقل ماجراست. اگر این مرکز ثقل را از میان برداریم، نیروهای نیابتی نیز در پی آن به تدریج تضعیف خواهند شد.
عملیات نظامی اجتناب‌ناپذیر است. این روند شامل
محاصره، فشار اقتصادی و همچنین عملیات نظامی گسترده
اسرائیل و آمریکا برای پایان دادن به این وضعیت خواهد بود؛ عملیاتی که قرار است زمینه لازم را برای فروپاشی رژیم فراهم کند.
عملیات‌های مخفیانه موساد و سیا
نیز برای تشدید شکاف‌های درون رژیم و همچنین تقویت مردم ایران برای مقاومت و، بله، دست بردن به سلاح علیه این رژیم انجام خواهد شد. فکر می‌کنم مسیر احتمالی ما همین است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149570" target="_blank">📅 19:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBhf8AOnXDrqYp0gzYWllbzpbf52aE8nKgW9mragY3YQTdLechoV0fhLR_IM4-m8T-rAVWn5kO-P7f2WiVzCD4p8s2WMnutbBMxyflsiWizJ-couR2pp3t5Yggz6PL6NSuk3lfgYj5t5o_7gy27dVAo7tQ-vR2-Lx_3oNMHyPWxx2jC5TTispcrhZ1hfbUFlDb0s1PhYnCVqSIwpYMaOr5LnjsFIAyPPNQtKbv382jINuKmRtXsmFNHz5NKWsh-zgVu9oKFzjmUhKNqtFwxNPXiboLjetmxwl0G0hI8Siw4ylwwBYWsn-3u0TdMZ2SCoaF-N_6pgbQfdnO5hwNZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکوتراست، دنبال بهترین کارشناس‌های فروش ایرانه
🚀
✅
اگه
ساکن تهرانی
،
پورسانت بدون سقف
برات مهمه و
شرایط زیر رو داری
:
فن بیان و مهارت ارتباطی قوی
🗣️
توانایی مذاکره و متقاعدسازی
🤝
پیگیری بالا و نتیجه‌گرایی
📈
توانایی برقراری تعداد تماس‌های روزانه در محیط Call Center
☎️
روحیه کار تیمی و مسئولیت‌پذیری
👥
علاقه‌مندی به حوزه فروش و ارتباط با مشتری
❤️
💫
همین الان رزومه‌ت رو به این آیدی بفرست:
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149569" target="_blank">📅 19:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs_7MNiCg9cjdXKPWauF_Ii4HC8tIfkbPcmm5QUvpArmlycJVvI3xAcZDbbHG8NUxuk1mFK-s9ivAIgEOv_HlRKj-MqSEOCRkdmYU4xrqQf9N-_taXaazLAFUD1OqN7_WCrQAgFiBdF3lC9pkjZI8irymVgSu1IS6E1BTo425xg_zyGP39Eq67kGh1C195hE7AM-Em9C4IzorjLXlieRPBj9-4UnwbV5LM2OZsCz4gsfgP5MQbOS2j5flV3tBuUJt07Xn5mpW3dNCjIFtIdV6Ax_ZXPk2RL7P1bVgDcjbyeU85d4IOoV9cbaQ94kZFo4uON6byzwXyJLGEA5te1QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149568" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149567" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
محمد مهاجری: کمتر کسی از میزان علاقه من به سرلشکر محسن رضایی و لطف متقابل او خبر دارد.
🔴
با این حال خدمت این عزیز عرض می‌کنم حتما از مشاوران رسانه‌ای و سیاسی فهیم و دوراندیش کمک بگیرد.
🔴
نه فقط برای آنکه حرفهایش در خارج درست بازتاب داده شود بلکه برای اینکه مردم خودمان هم بفهمند منظورش چیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149566" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=erxj2omRzXFLj9BQIkQdSKL5slis1I120kdbLooCKp0NaHTH2oaoVKMbVfA2akQXLxKQT33N_P-MGelFZ_b6DBDsbO3rVdK1y2ef1YkQWp2YM4M9yc5KZXUfZBVJpPLWoBRMMvf_BgXEYaUI5b8yRQRn--e2FL8iCKgR4GfDEr16vtkHSWvKXoJ86DiKNwmJzCZ-QwIrxH0Bq8AZTz_1mQtDLTAQgGNqZe5U7l4jjY8rGHe-oXeEJ_Ex4LDs29-uxuS_N5xPhsEaUyesos1HxfiB0M4EEdFVvfWNMIFS9552R2A0tlricNyEatkxP6OIYvjmwc9A4jv91nZZNU7IdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=erxj2omRzXFLj9BQIkQdSKL5slis1I120kdbLooCKp0NaHTH2oaoVKMbVfA2akQXLxKQT33N_P-MGelFZ_b6DBDsbO3rVdK1y2ef1YkQWp2YM4M9yc5KZXUfZBVJpPLWoBRMMvf_BgXEYaUI5b8yRQRn--e2FL8iCKgR4GfDEr16vtkHSWvKXoJ86DiKNwmJzCZ-QwIrxH0Bq8AZTz_1mQtDLTAQgGNqZe5U7l4jjY8rGHe-oXeEJ_Ex4LDs29-uxuS_N5xPhsEaUyesos1HxfiB0M4EEdFVvfWNMIFS9552R2A0tlricNyEatkxP6OIYvjmwc9A4jv91nZZNU7IdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الونیوز خطاب به کانال‌ دارهای مخبر
😂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149565" target="_blank">📅 19:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6naUug4JrJvClAfVffDqsglbN3fVc8765d--6KHPj6fTGySYNYToQFm8yalWWaHSPQavSDwEyWA43DDUfa71IxjJBgevPPebJgJGf-PECiENFJHuWiyRajJ5BprEqNvcoj0n_RLBuEVLGuaBkLZbw0RK3S2Bwuw78jLu3m5ogiHKatuOuIqeJg3PCjeKUekw3icO5Tqgl39hbQAZA-Seovfzn2OhEFAXA_yWI78PVm30P4QHzQSQ6HHml0JXkPpBJv1aWLYooMw7Qns-O4OfyMLpvqP1gJSIUL7emn-YUt0h-iOk60U1BylORI9AmA1Npzu5T_avzp_CGIMzOfIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی:
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔴
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم» یعنی همون کاری که خودمون میکنیم)، به دنبال جنگ باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149564" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=l9YK6VEUsoQhv_RrGiho8rdjhEH8ka_OCYJbObl0rbYvLfCEyVe4qcEcC6Fvbk2HeGfZ2OwZiymixM-yMW3Hlra4Pie_vbZ8o2iP9H4I5faRnFmrhGRMN60YLtCmFUfc1Y91yu-0uA4ZIAQz4ac3p9Sn1vAz1rurqAiqFpim7tm382E0lnE30Ndot2hu1QFWc_lRf35aWgTeJYKFC9E2GIXfctEZupm1zCBUYAYI7_ZcxRR3aRQtDaAL9vtnSGR1b5S3ftpA73x98EUoJreXqOnKSN22LYE8taKVWBQ5br93PT4HJNMn1DOYw5xplsSWYaKn9ES3y0xMmfg14uE21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=l9YK6VEUsoQhv_RrGiho8rdjhEH8ka_OCYJbObl0rbYvLfCEyVe4qcEcC6Fvbk2HeGfZ2OwZiymixM-yMW3Hlra4Pie_vbZ8o2iP9H4I5faRnFmrhGRMN60YLtCmFUfc1Y91yu-0uA4ZIAQz4ac3p9Sn1vAz1rurqAiqFpim7tm382E0lnE30Ndot2hu1QFWc_lRf35aWgTeJYKFC9E2GIXfctEZupm1zCBUYAYI7_ZcxRR3aRQtDaAL9vtnSGR1b5S3ftpA73x98EUoJreXqOnKSN22LYE8taKVWBQ5br93PT4HJNMn1DOYw5xplsSWYaKn9ES3y0xMmfg14uE21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست
اکانت ریاست‌جمهوری ایالات متحده آمریکا در فضاهای مجازی که فیلم‌هایی از انهدام تجهیزات نظامی سپاه و منهدم کردن بیت رهبری گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149563" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maNOe2AfT2jyZv-fMkvhhM7Md8DtfMeCEnzvIaxMApBEOu2dwpjvWwyaRrT-A5PV9NI7UGixlaCg8auBNeqpE43cJgHR1SpLZ6mowtBbuixnXicAOs1dvikIN6KOfEXtYqbnROxTEPZg9Oh46Ld8TWZUrPhJ0zJFm1p42XeogWFivQftYGkskYGcwlFwpkSL0SPut9a1pf14TZpcri2AGwKoxcwFBFLG6CtS87kYDljVf38s8WIrEIQd2JhkNQAEgP4tWP8hs4gWxwzKDtjUspdPim1xRZjcEx8e8WtuBywphUYShEMR7HZfYJViLvvSPicrHel7CYFkHfNwhhNoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
واردات سامسونگ و ال‌جی آزاد شد اما محاصره‌ایم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149562" target="_blank">📅 18:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfuuHESYjx8eR05BPB5K6sLLhR5WMUYC4Ue0_teDufSHb17uYgIj_DAUjE12lXEnoZ09DVUxLtUa5ImPv7_gU88PWDkvNAHl2AbcoTvnXA3eBJSCX-aODZ8R8Szf5BTMm7Tvnxz69NtsqiHg0-r0PyA_ttKG4n1VXtNiDFzDfMq0U7Pm2JdoWJwvLBGkMs9zJRlWA9fr5fphbpWeHF6Gm2FHvN7Kk2Z4PjXZHOYrlJLMh901HYixE_ZtEljNfSeVC1RpEdUY1dN97I2EMAm6nOZEtuVjAhmG845ik83CMymqnNQowqld6s6RVIAV2giKWSMEBTk0Owg8baLjBCMQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: من یه پزشکم خب؟ آقا مجتبی تونست ۷ساعت رو زمین بشینه و بامن حرف بزنه پس سالمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149561" target="_blank">📅 18:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رسانه‌های آمریکایی ادعا کردن، نتانیاهو داره آماده یک حمله تنهایی به ایران می‌شه و اگه حس کنه وضعیت انتخاباتی خوبی نداره، جنگ رو شروع می‌کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149560" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e294531f.mp4?token=qvND9kDVJw02Vj8RNShhicn_nOEnoV4l5yfAXA6rtNlridEJVDyDBskSETrVSYGTnI3OSBZpccq90ylXOFMX6gOoQ2xHCv1CI1Se1kRrAC19djLr3jMK_olDVq4YW1F5F_vBSqSHRlDCfeOzNIm_wiloRCRoWFxWtUOLLgNUkc6dmAU6AopcgW7yBkNkpm3ypsEv-Qus2KjJzM3w2kpmZOL3RNkeEE1o_Lr5KqMMQ0Gbffd_NqsHS0bV7Ew4PN5QMMXRl6GzPd5hW2KMMIe9hjABF9vMurEAyqDOZxOi2dT_jKWxto11u93lywh66uBKleaftKpJ1CVPeNt8MzqQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e294531f.mp4?token=qvND9kDVJw02Vj8RNShhicn_nOEnoV4l5yfAXA6rtNlridEJVDyDBskSETrVSYGTnI3OSBZpccq90ylXOFMX6gOoQ2xHCv1CI1Se1kRrAC19djLr3jMK_olDVq4YW1F5F_vBSqSHRlDCfeOzNIm_wiloRCRoWFxWtUOLLgNUkc6dmAU6AopcgW7yBkNkpm3ypsEv-Qus2KjJzM3w2kpmZOL3RNkeEE1o_Lr5KqMMQ0Gbffd_NqsHS0bV7Ew4PN5QMMXRl6GzPd5hW2KMMIe9hjABF9vMurEAyqDOZxOi2dT_jKWxto11u93lywh66uBKleaftKpJ1CVPeNt8MzqQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع بیکارها و الاف‌ها در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
🔴
این‌ جماعت معلوم نیست درآمدشون از کجا هست که هر روز ول هستن از اینور به اونور
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149559" target="_blank">📅 18:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) : در پی شناسایی تسلیحات که نیروهای ما را تهدید می‌کردند: ارتش اسرائیل یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد
🔴
ارتش اسرائیل امروز (شنبه) یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد.
🔴
این حمله با هدف رفع تهدید انجام شد. در این انبار تسلیحاتی نگهداری می‌شد که برای آسیب‌رساندن به نیروهای ما که در منطقه امنیتی فعالیت می‌کنند و مختل کردن فعالیت‌های آنها مورد استفاده قرار می‌گرفت.
🔴
ارتش اسرائیل به اقدامات خود برای رفع تهدیدهای فوری ادامه خواهد داد.
هرگونه استفاده از خاک لبنان با هدف آسیب‌رساندن به شهروندان اسرائیل یا نیروهای ارتش اسرائیل، با قدرت پاسخ داده خواهد شد.
🔴
ارتش اسرائیل همچنان به توافق میان اسرائیل و لبنان متعهد است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149558" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الان عراقچی میاد میگه شروع خوبی بود</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149557" target="_blank">📅 18:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آکسیوس: مذاکرات همچنان سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149556" target="_blank">📅 18:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اکسیوس:
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
🔴
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149555" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: باراک اوباما اخیراً گفته است: «اگر برای دو سال زنان را مسئول همه دولت‌ها قرار دهید، اوضاع بهتر خواهد شد.»
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من زنان را دوست دارم و فکر می‌کنم فوق‌العاده هستند. اما این واقعاً چه حرف مضحکی است، درست است؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149554" target="_blank">📅 18:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ایرنا: عراقچی فعلاً در نیویورک می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149553" target="_blank">📅 18:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تیرخلاص ترامپ به تفاهم‌نامه با ایران
🔴
العربیه: ترامپ اعلام کرده که امکان بازگشت به تفاهم‌نامه با ایران وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149551" target="_blank">📅 17:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=PFKb3FQkHNmpMxO_EX931lCklEvIrgmCK1ZTn9P4-RQP1N4_bkXYzomYtNce5ejsXp8iLnnTStzqkY7KJLaPC4V_SroWHBb2Sv3lAn_HdynnVDunEiOd_tWeI7Uu9dT1s_nuFe5Bnz2y74eK8b27phOD_9i6xYfHSGDfzqGfzU_lNVot9eO5iX_965oIo7Bo7IANiywWGXsPHUkNz1VZaLrtCUMoTbg2vOvDADa5eOJdZURdcNu1JanHZQy7vpSQlys_IT5rp8xWSSpm_rXUEptaOHVpUOBV0GLdUpH2Pk3A5n1MbNX0iB_DVR0jMgr_HxoGMZxLwtk9lY2YY4FIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=PFKb3FQkHNmpMxO_EX931lCklEvIrgmCK1ZTn9P4-RQP1N4_bkXYzomYtNce5ejsXp8iLnnTStzqkY7KJLaPC4V_SroWHBb2Sv3lAn_HdynnVDunEiOd_tWeI7Uu9dT1s_nuFe5Bnz2y74eK8b27phOD_9i6xYfHSGDfzqGfzU_lNVot9eO5iX_965oIo7Bo7IANiywWGXsPHUkNz1VZaLrtCUMoTbg2vOvDADa5eOJdZURdcNu1JanHZQy7vpSQlys_IT5rp8xWSSpm_rXUEptaOHVpUOBV0GLdUpH2Pk3A5n1MbNX0iB_DVR0jMgr_HxoGMZxLwtk9lY2YY4FIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
اول ما پیشنهاد آمریکا رو رد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149550" target="_blank">📅 17:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3Oi2mSa2zmXqBEUU1jKeXjNSN5aar1Ul3zwBxxqQJXJZSPfWTsMGD2NkIp7c_jpYOzqTxttxVgmyTuFtsyxMwQpQmVj5Gk6SOIGm2V9SSvglcHFvdgEb_VZI79opjew5iPN8W4tqL2ZBKpSf8BN828wOXOL6Swf7ZPZlShgwgBQRDcv9T24NXH9KAzZG0xoQzIbINUOmV2GDfd_A-BF-4b1HGgDpJibD8dBHTT1YNDI0N7phuQalH7iLmeqrJnXVe4MP0P3nABGooRqiNQitZJBJJBxs0o1XLel6FMqpSMxY9RjfyV7vZs22NtF20OepRgvs9IBNrWNiAu4oJ-1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴۰میلیون بشکه نفت طی روزهای اخیر از تنگه هرمز رد شده و عملا تنگه برای همه گشاده جز ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149549" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=e-eWjW0xdxZeuLtnEm5apG0Nx9WBzX0dNrYH4KTjxWCa6dgTQkWu3qJ7nTzVO-AFQ2dPYoEX5W9SIxotIXjCTwrfdyyPvcuU99Rl1WBukkEg2tVEvzeBAFh7ybgs3gUhxrwLfbW9kFhkuoOqpCpANVRCK09pO4WhXafLwNAsorbrje5wtbcC0KkIBl9ZtUlUKPZf43QbGWlYvPe15aVpqo4pfdntnSIN6TO0lKEvc-awvSF2uurqeh6-Kejx6q7P6wb68RPtY3Ia6rTZPYhnEWUp6OxYalxk_AfPedN71UmzUGa6kfxLHp-YFyPdZSHbHW4LmLBGKif_RwOORvZOwaD5hYgt-MxsouhHcAscqTS6F-_yrJRCsSE43Uc0z2UwIptQdRRVldsUwDPyejEuVu8XskX5oNIBpepmvfuuvTpYW0dAeVcKmQMFx-QHC1LQNElYXHhol-8ghFQP3IZZGQAhcOciHF-GfBe6VZ_GjHvHAaSFLntd7mIjxn_8Y9y1xMuprc3iMc6jULEC0kr63dkbiYw2ltM9LUzy01Arw2LWEuPQFwHc2Cs1edApNoQZwiAttkqwTQ45WRq0sk09dhKfYMsy01Z92QQxZOsD17L7xyBulzfSToHtbLilP5TznLwqNiVpTCHrM66YI_5eaLsG-Are-_t00CjR3LFua2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=e-eWjW0xdxZeuLtnEm5apG0Nx9WBzX0dNrYH4KTjxWCa6dgTQkWu3qJ7nTzVO-AFQ2dPYoEX5W9SIxotIXjCTwrfdyyPvcuU99Rl1WBukkEg2tVEvzeBAFh7ybgs3gUhxrwLfbW9kFhkuoOqpCpANVRCK09pO4WhXafLwNAsorbrje5wtbcC0KkIBl9ZtUlUKPZf43QbGWlYvPe15aVpqo4pfdntnSIN6TO0lKEvc-awvSF2uurqeh6-Kejx6q7P6wb68RPtY3Ia6rTZPYhnEWUp6OxYalxk_AfPedN71UmzUGa6kfxLHp-YFyPdZSHbHW4LmLBGKif_RwOORvZOwaD5hYgt-MxsouhHcAscqTS6F-_yrJRCsSE43Uc0z2UwIptQdRRVldsUwDPyejEuVu8XskX5oNIBpepmvfuuvTpYW0dAeVcKmQMFx-QHC1LQNElYXHhol-8ghFQP3IZZGQAhcOciHF-GfBe6VZ_GjHvHAaSFLntd7mIjxn_8Y9y1xMuprc3iMc6jULEC0kr63dkbiYw2ltM9LUzy01Arw2LWEuPQFwHc2Cs1edApNoQZwiAttkqwTQ45WRq0sk09dhKfYMsy01Z92QQxZOsD17L7xyBulzfSToHtbLilP5TznLwqNiVpTCHrM66YI_5eaLsG-Are-_t00CjR3LFua2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من اخبار واقعی می‌خواهم و عاشق رسانه‌های آزاد و مطبوعات آزاد مثل الونیوز هستم.
🔴
چیزی که دوست ندارم، رسانه‌های جعلی هستند؛ مثل شبکه‌هایی مانند CNN که بینندگان کمی دارند، یا MSDNC که فکر می‌کنم حالا نامش را به MS NOW تغییر داده‌اند. می‌دانید چرا تغییرش دادند؟ چون میزان بینندگانشان بسیار پایین بود.
🔴
چیزی که من دوست ندارم، اخبار جعلی است و آنها ۱۰۰ درصد اخبار جعلی هستند. در دو سال گذشته، بعید می‌دانم حتی یک گزارش خوب درباره من منتشر کرده باشند؛ در حالی که من در انتخابات با اختلاف زیادی پیروز شدم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149548" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: آنچه آنها می‌خواهند انجام دهند، این است که تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند.
🔴
آنها پولشان را از تنگه هرمز به دست می‌آورند. بنابراین، خودشان خودشان را گول زدند.
🔴
آنها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد ماجرا شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را ایجاد کردیم. این یک دیوار فولادی است.
🔴
حدس بزنید چه اتفاقی افتاد؟ آنها حالا دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
🔴
و من گفتم: «بسیار خب، ما هم آن را برای خود شما می‌بندیم. اما بقیه می‌توانند از آن استفاده کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149547" target="_blank">📅 17:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است.
🔴
ایران با بستن تنگه هرمز خود را در مخمصه انداخت و ما بزرگترین محاصره تاریخ نظامی را بر آن اعمال کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149546" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149545" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149544" target="_blank">📅 17:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع آمریکایی:
ترامپ به تیم مذاکره‌کننده ابلاغ کرده است که بدون اقدام اولیه از سوی ایران، هیچ توافقی در کار نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149543" target="_blank">📅 17:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46292c4c.mp4?token=G1j5b_KT2H36X_NljiagX0voAK4C_URTxUyf_CM9C6w6hbBidInNMZhjMYnvQYYaZQ9_ag6DnptZORrlhxztEu2VPCIYjXOsXy0XL8e_3scJ9-2OMEsd057efoK7DTuITklrQRLy-XcBgN__Lkmbnxh4KCwdYOY6-CNhpMjOR3cL2QbDQ52h9TUZvtgpSpYiR-NO0xslBcd6KyARk9XVC48rM2pG_f7qQY69I5CGuH_n5Ir67BI_nmwWfqkehiXLHonk1koae6p-9ofWwnEL0t0Dt21Q1X403cbyMiJaxa0ij5VXJHk39Kgt2OAG0yz0-BBJ1_e2yqVehkbYTEH7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46292c4c.mp4?token=G1j5b_KT2H36X_NljiagX0voAK4C_URTxUyf_CM9C6w6hbBidInNMZhjMYnvQYYaZQ9_ag6DnptZORrlhxztEu2VPCIYjXOsXy0XL8e_3scJ9-2OMEsd057efoK7DTuITklrQRLy-XcBgN__Lkmbnxh4KCwdYOY6-CNhpMjOR3cL2QbDQ52h9TUZvtgpSpYiR-NO0xslBcd6KyARk9XVC48rM2pG_f7qQY69I5CGuH_n5Ir67BI_nmwWfqkehiXLHonk1koae6p-9ofWwnEL0t0Dt21Q1X403cbyMiJaxa0ij5VXJHk39Kgt2OAG0yz0-BBJ1_e2yqVehkbYTEH7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا: جمهوری اسلامی بیشتر از پهلوی، منافع آمریکا رو تامین کرده
🔴
جمهوری اسلامی اصلا تو وزن آمریکا نیست که بخواد جنگ کنه، مثل این میمونه از ارتفاع ۱۰۰متری تو ۲۵سانت آب بخوای شیرجه بزنی(مترادف گنده گدزی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149542" target="_blank">📅 17:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMlf0viM1EwiWx_8RPy0Kivi0n5f2uk0pat9O1ui8HulCO6--Dh9OrUBoGzNUHN2FzuT24paYEJKxiCM3ytSDvbZc4Hq6CbaG7jQVVQ2joNRdH0uhkhOBHXJCxvijUq8C_2JFd7lWOaUKf7xZJcEJ8KdpSxKp2z3TnIPrdCDGOHYcj8VtpT4cFhqOTot4hFE7bcuOSOagh7dagP-A2lBMtZzs8Dmry58FyduoVdq3EjsSV68pPG3UJ_QEhjn7eAldgFJIpymVGseIWlcTCLAsfujXjB3EOCx0LBPP2waNCvRoxnHmRvOjOZc-P2UE7y2U0IpTVDorSJhaq5feZDzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد جانجان فعال بازار سرمايه : سردار دهقان به ثابتی پس گردنی زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149541" target="_blank">📅 16:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
دو انفجار در تنگه هرمز در حال حاضر رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149540" target="_blank">📅 16:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8Bq3wjyL-VQ0HKMzgQJmRp-b_i40UnKvjBHxxRkhlC3ITp0RzEe9qbaIRPU8ft3sGWC1zt4lZd2ZbuRy9GU2-eb_z6kZ7sJNabSPEp5QFjSqvATrfuXrPCzGQK8eJxYQV8xUmrw5ryvm5SlN_1J0ZzIp4nL5hKg8rW9n-pfFfH6-MIXDWghu96t2TRBIV92Pb9oVONAnFkE1ZOd6yBDLsrw0PwL0Edi1Ql902oc8LNEXnujeRqpvFwogVHtEoOAItZKwPe-FwihOPZ0wadjRl4jU3oKN4p3rlbLrq9eoG6RJ7ODfJf9dgwy9CMWtI2s9yZqWVw67bqCZq9VmcAD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149539" target="_blank">📅 16:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149538" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض گسترده‌ای در مادرید در واکنش به آنچه برگزارکنندگان آن «هجوم ده‌ها هزار مهاجر غیرقانونی به سئوتا» می‌خوانند، در حال برگزاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149537" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: هیچ هیئت فنی از ایران به نیویورک جهت انجام مذاکره با آمریکا سفر نکرده است و این مطالب صرفا خبرسازی رسانه‌ای است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149536" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شورای عالی امنیت ملی: اینکه ایران در مقابل محدودیت‌های هوایی اخیر دست به مقابله به‌مثل نظامی می‌زند، تکذیب می‌شود
🔴
مذاکرات میان ایران با کشور‌های مربوطه برای رفع برخی محدودیت‌های هواییِ غیرقانونی ایجاد شده، با جدیت در حال انجام و پیگیری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149535" target="_blank">📅 16:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149534" target="_blank">📅 16:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149533" target="_blank">📅 16:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzS5XTLU1Jgv0q50bYHhxKOYWsrcWx-4XHAY3mI5h6GxACYdCZBZxKn6K83TgAiGs_XHwHpNw6yn4TTCwTY7rnzkk59-6MWYAl3LtqMHLK7k_Tls4vbnmcKHr_PYQvAbjniwBuQNC0Nvs4IIn5YSEguXiU-iq1OhV_aQjy_kF9nz_ZkcM5ToO1096I01fa52BOcgEBAbbMV4lMuNj2H5bax17C9GTyHajOLQDl7UHSHEu9ZQ97k8xAN5kAgqpxF3RjKS9yt2VLsOYqAbFt8ZXCEw1fsP0QUMZSK8BWIG43jHT1wARsMEoQVqqO4yJiZ8qQNjU3XLNAS1MOeHem68xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : اخبار دروغ نباید در کاخ سفید اجازه انتشار داشته باشند!!!
🔴
این وضعیت مدت زیادی است که ادامه دارد و هزینه‌های بسیار سنگینی را به کشور ما تحمیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149532" target="_blank">📅 16:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149531">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده:  آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔴
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده
🔴
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم های جدید و محاصره وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149531" target="_blank">📅 16:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ :ایران نباید به سلاح هسته‌ای دست پیدا کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149530" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149529">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟
🔴
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/149529" target="_blank">📅 15:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149528">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDT1KI4nkoYY0HF5c9orAnHGGki0DdIHkePu877LsPhbxnKA2tk-tU2Zap1jevhnO94TCUH5IkfVqIz9wbzLV6FQukj805LdrFsxSdtPbdpgekJucXlzIm0L066S28iNMZBsgOhNi4EHJUXwKSnU_yUhrihRGykYmzj7ysV_OGSR7YEJ624D-8HZsSaHNNtHv-iCv-yESyxcwdR6JYVpW_j-H5eXvadCtr-cGVvh-x-UeAxtN3fwbkOD5qeQn6rCd0stQJ7rDuwd32vAIsbVnwgO7_X2BCRfynBLNlIIIUyFZV9XEKN8juSkeFTtQcitmYeDVGhsJO4OHNHg_N8rjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروند هواپیمای نظامی باری مدل C-130H متعلق به ایالات متحده آمریکا به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149528" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149527">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyV8hoDOcYtk9tY4fZ-E1ijLOdLw5em5Fwy8X03Akc1zEeyUlv0ciFceIbyj5kzY-piZOGcDmiJxmr6zmiUZEPIW1qjuDLoE2Fx1-F812KMTBE2FtimReey7G5tySMxMrtzRUHGw9wg5T2Fmdax_yqqSpZzU1AnthoRn7aytO_5Q9YUVTcsSpmR4kML9d7434fjogWbWG1yekHYkI90gBGODCMI3dFg3ZfBqhWwfJui6RzxSJiE7q3MsnIf2kMqrGNcXM5GsQZWJy-FPe8QVAbCwNuGaJkalECpjhQMqtwFv5_jFaPi-fdL4Wh0KAOw7WJuLBfvtuKuLhztYU3HEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۴مهر روز سرباز هست، یادی کنیم از سربازان بی گناه پادگان بمپور
🖤
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149527" target="_blank">📅 15:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149526">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان در پاسخ به سوال خبرنگار الجزیره: چرا و برای چه باید با ترامپ دیدار کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149526" target="_blank">📅 15:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149525">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های آمریکایی گفتند، دونالد ترامپ، رئیس‌جمهور آمریکا، پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیارانش گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران را از سر بگیرد.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149525" target="_blank">📅 15:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149524">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / وال‌استریت ژورنال: آمریکا با بیش از 50 کشور تماس گرفته تا اجرای تحریم‌ها علیه ایران را تشدید کند و به آنها پیام داده است: در موضوع ایران یا با ما هستید یا علیه ما
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/149524" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149523">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صدای انفجاری در جزیره خارک ایران شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149523" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مدیرعامل شرکت شهر فرودگاهی امام : پروازها به ترکیه، مالزی، چین، پاکستان و مالزی برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149522" target="_blank">📅 15:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3v_etDHcdznT_WCgO9jie30FAqwvDVDorA2K9PjcqWFB0G2YIOfLTzbLR1MDjC9EAY9Ht4sbzv08U_F3othKRt4WhAEGATWxaOyi9jWmMvh1RPbqEywwosGinnYC66OSGRfRMDUrNN3dEDuFEU12KtlizWLovP5YbE0mKGfbZA-wMNrHrFpHRDcEWz1No3YPhdTq34MJjUlhNOg6r-kGPnW0jOKsf3SS1nZYS8AsRT0t1cFrgm7tY_b5HYrMEn7w679qIHKithpt9aZja7xUfv3Ez9ZoI6BjRb214lru8dmrQv2oIaF_OE0Y0WMq7TUtyj1aBiQoSgnfSxxxczKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbEmP-23LJ6_MCUGmxUm9QwM4sBlfUQFtPrzHiak_IqvIbJXEhLlSUy2yQ9e2YXF1GuUA-XU9QSUwn6Fcxu0PoavwKxxVB570GkR-__zX305SJMd5AImrppgrWZPZEhQNFTtPZm3tAqp3pZwv-Tci7zyrBqMVgYpNOJzM1eCrncmDKdcuTkf3U6YD741dpx8qw01unSPW4097ZD1LOeGMlmSnD27QVUBoZwXGGpisXvMNzxOeobKxhcTab9HwnmDSIFJRsC_iMsjmVwxeHVM2TT689rOrDcB5T2hAZy_8wArtD37h1ewIpO0kirZjNXFelWR5fJz5lFylidhvSStlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد "گران" روسی که بر فراز اوکراین سرنگون شده اکنون به عنوان یک تزئین در یک سوپرمارکت محلی در ترنوپیل، در غرب اوکراین، به نمایش گذاشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149520" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
۱۱ کشته و ۳۰ زخمی در انفجاری در شمال غربی پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149519" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
واستریت ژورنال: آمریکا از بریتانیا خواست مجوز فعالیت بانک «ملی» در لندن را تمدید نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149518" target="_blank">📅 14:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149517">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر علوم: دانشجوهای عراقی به‌زودی به محل تحصیل خود در دانشگاه‌های ایران بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149517" target="_blank">📅 14:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149516">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WizKl4D8ZgHYcIJYkfpbIWUHhc1ZfRuK0MZVMPFPFO1MpW-EwAu0ns2i0APXDRujCk_hybSiC1mUeq-sQB78H7b96_6Jt7YgNzDjit2fv98yBbZJi4xZlBnI7Sq0v1IG__zCivXhBYK-r5kEp3qf98S_0smC2gGnM3trPrhHLFabJsG8QrCfmQ1N1x1H7t8ywCjgRzELoanwkFv-51_i_6WZhGjSYAeRBZyD9pj2EcOieArD7JjcMvHZ5F77ZYBYtNfVyLFP6agcEMZouR76SWCCZfFT1HVsynL7ycHzOjGOW0LpcRK7Qt9IFUqYQ09BBUkRWvKXouYm1EeEpPQrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«چرا باید منتشرکنندگان اخبار جعلی، مانند CNN و MSNBC، اجازه دسترسی به کاخ سفید را داشته باشند؟
🔴
با وجود پیروزی بزرگ من در انتخابات، تقریباً ۱۰۰ درصد پوشش خبری درباره «ترامپ» منفی است و سال‌هاست که همین‌طور بوده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149516" target="_blank">📅 14:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149515">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نیروی هوایی عربستان سعودی، پروژه‌ی تصفیه آب منطقه‌ی الأکبوش و شبکه ارتباطات در شهرستان حیفا در استان تعز را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149515" target="_blank">📅 14:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مکرون از ریاست جمهوری کناره‌گیری خواهد کرد!
🔴
امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149514" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پایگاه دائمی پیشنهادی آمریکا در لهستان که «فورت ترامپ» نام گرفته، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
🔴
رئیس‌جمهور لهستان گفته امیدوار است ساخت این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل شود؛ مذاکرات درباره مسائل مالی، اداری و انتخاب زیرساخت همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149513" target="_blank">📅 14:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723913721e.mp4?token=sGLSSSlSeKt5PsyDeT_m3mSZxI8PtNaPJs4cvAhkcD5hFTets7OuhM7LsIAXCMQR9CZljQN9soiaVTuqVYn7gPlb4CegcAA02vz145Qu6TqzPvwlh8dEs_W5DH65UuFMeZX2S19GSaBLaStH-iQJuNut4SdS0VoymZBBtYu9W1M-UETr6JCV_og3kXLmMk7pZuh5ZlsJqoBQoMsJIWnRfZTzvUVEqXOmVrq8JMQ1KytwZ1BCmw2q_0upscoMNmEXq9rEwIz5yF271-XDmo79DYMAlmdmAQ1pJs6rsDEJ4NaIWE4uvGoHMAvM-wQux5O9jJChpPeOUTloQkAtvRFKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723913721e.mp4?token=sGLSSSlSeKt5PsyDeT_m3mSZxI8PtNaPJs4cvAhkcD5hFTets7OuhM7LsIAXCMQR9CZljQN9soiaVTuqVYn7gPlb4CegcAA02vz145Qu6TqzPvwlh8dEs_W5DH65UuFMeZX2S19GSaBLaStH-iQJuNut4SdS0VoymZBBtYu9W1M-UETr6JCV_og3kXLmMk7pZuh5ZlsJqoBQoMsJIWnRfZTzvUVEqXOmVrq8JMQ1KytwZ1BCmw2q_0upscoMNmEXq9rEwIz5yF271-XDmo79DYMAlmdmAQ1pJs6rsDEJ4NaIWE4uvGoHMAvM-wQux5O9jJChpPeOUTloQkAtvRFKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خیابان‌های تایلند زیر آب رفت و ده‌ها هزار نفر گرفتار سیلاب شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149509" target="_blank">📅 14:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با شبکه سی‌بی‌اس آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149508" target="_blank">📅 14:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یاسر الحجاج سفیر عراق در تهران در گفت‌وگو با «العهد»: مذاکراتی میان عراق و ایران برای یافتن راهکارهایی به‌منظور ازسرگیری پروازهای شرکت‌های هواپیمایی ایران به فرودگاه‌های عراق در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149507" target="_blank">📅 14:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پزشکیان به الجزیره: آنچه در یمن اتفاق می‌افتد به ایران ربطی ندارد و ما با همه کسانی که مورد بی‌عدالتی قرار گرفته‌اند، اعلام همبستگی می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149506" target="_blank">📅 13:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هیمتی: تورم نقطه به نقطه بعد از ۱۵ ماه روند افزایشی در شهریور ماه کاهشی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149505" target="_blank">📅 13:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: قطر و پاکستان در حال حاضر میانجی بین ايران و ایالات متحده هستند و پیام‌های ما را به واشنگتن منتقل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149504" target="_blank">📅 13:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه‌های آمریکایی ادعا کردن، نتانیاهو داره آماده یک حمله تنهایی به ایران می‌شه و اگه حس کنه وضعیت انتخاباتی خوبی نداره، جنگ رو شروع می‌کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149503" target="_blank">📅 13:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جروزالم پست: نیروی دریایی اسرائیل در حال بررسی خرید هواپیماهای گشت دریایی و ضدزیردریایی Boeing P-8 Poseidon از آمریکا است
🔴
در صورت نهایی شدن این قرارداد، اسرائیل می‌تواند از این هواپیما برای افزایش توان شناسایی دریایی، عملیات ضدزیردریایی و گسترش برد عملیاتی خود استفاده کند.
🔴
گفته می‌شود این طرح در برنامه راهبردی دهه آینده نیروی دریایی اسرائیل قرار خواهد گرفت و در صورت تأیید واشنگتن، اسرائیل نخستین کاربر P-8 در خاورمیانه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149502" target="_blank">📅 13:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149501" target="_blank">📅 13:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرگزاری چین: واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149500" target="_blank">📅 13:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ پیشنهاد آتش‌بس ایران را رد کرد؛ احتمال ازسرگیری حملات پس از انتخابات میان‌دوره‌ای
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، پیشنهاد ایران برای یک وقفه هفت‌روزه در درگیری‌ها را که شامل بازگشایی تنگه هرمز بود، رد کرده است.
🔴
بر اساس این گزارش، ترامپ در محافل خصوصی در حال بررسی انجام دور دیگری از حملات هوایی پس از انتخابات میان‌دوره‌ای نوامبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/149499" target="_blank">📅 13:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq1lGVk9sm0tZMd2GHLzVtD0H76TNcWtjbC_3jV1Vnv9kxUOXMseN1_KTiRUutMkMcdQxfHF1O8Tw_ysU0cuAn4r3EBt64utGvbTfZo6o7OZJrJN_EvtlVbqAowcB4lYsqeEgfxVC2tbu4xgu7pMZKGs8KgDDRLsRL7F6jfvpcoptVC-NTAU03mpWuby-dOXc2aAbE5HywNZE4l-mx79qw9RONdGUq1XAeoxA2N_pwL989_LqJSIiikWO2dSEPiwaOuJpbWsqWJt3w_U1HdBbuEHIhZKJURe80vk4SNIRp2Lx3MeNz_Bu_ddE_wY4eK0EihbAPlub9wtRgcmcDqxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d0cfc6e2.mp4?token=fWv_XAkmV8ES1d7nfIIC03zVGQEfG1N72116WPii8Y_Es-ARDRyAqY7cGhZcHJDIRki42zUjboLK8xifDlN4s-d2qlNw-LwYNRbnBQKgWo9c4xaJpO_gHbSuaPJ1S6GY3ke_bPnB04JlYQkhgUI_9bKLH_qvF-VB3skFYKW1OxK0rfnd4sYBd0bBrKP120qf272O7qRadygprA27PLX-sK7Ik8ruf6D2vwlOM2FMMTej9rPes8vdRSgeMH4MqPCjQGjhY2eMJC9-LnvdgfSgyVAOVcCWTQNJnl6m6KL5A8HP-NSM0X5SX_7z2q_uFP2hXvXFgBGKLYo5ILgvJdTMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d0cfc6e2.mp4?token=fWv_XAkmV8ES1d7nfIIC03zVGQEfG1N72116WPii8Y_Es-ARDRyAqY7cGhZcHJDIRki42zUjboLK8xifDlN4s-d2qlNw-LwYNRbnBQKgWo9c4xaJpO_gHbSuaPJ1S6GY3ke_bPnB04JlYQkhgUI_9bKLH_qvF-VB3skFYKW1OxK0rfnd4sYBd0bBrKP120qf272O7qRadygprA27PLX-sK7Ik8ruf6D2vwlOM2FMMTej9rPes8vdRSgeMH4MqPCjQGjhY2eMJC9-LnvdgfSgyVAOVcCWTQNJnl6m6KL5A8HP-NSM0X5SX_7z2q_uFP2hXvXFgBGKLYo5ILgvJdTMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوایل امروز، حملات هوایی اسرائیل منطقه جبل الرفاعی در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149497" target="_blank">📅 12:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae558b3656.mp4?token=fTgve1XIr1gWscHotJ4fwlU_yRvWIlZrAhBrD1VKJJmpOiM8z2nf-X7tLHNgZICWLqe0qijrMJLGkLG4uXk0XCrNaEvypRAYzF5Y74PeOgAqUC618iZv-0tNhUAaK3s_2Zr9POCAw9uUBHyxIIBwKNcgYPr31O_aa7gPWMnxhFeJfHahrgaOGShRIGaB50dLXRFj-LYqaj1BOXAlSEmHkXJknEhbouKnw6e-wsFjiAugtamAJDvX7vtfQBiZFtCF_qPnyyhFPSvPOU1lwA5u_5YSkQtKinjm6847IqAZDURHFqJ1MCv8l4PEKRNEVvm5MEDvIZDEj1_oWBejkVDDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae558b3656.mp4?token=fTgve1XIr1gWscHotJ4fwlU_yRvWIlZrAhBrD1VKJJmpOiM8z2nf-X7tLHNgZICWLqe0qijrMJLGkLG4uXk0XCrNaEvypRAYzF5Y74PeOgAqUC618iZv-0tNhUAaK3s_2Zr9POCAw9uUBHyxIIBwKNcgYPr31O_aa7gPWMnxhFeJfHahrgaOGShRIGaB50dLXRFj-LYqaj1BOXAlSEmHkXJknEhbouKnw6e-wsFjiAugtamAJDvX7vtfQBiZFtCF_qPnyyhFPSvPOU1lwA5u_5YSkQtKinjm6847IqAZDURHFqJ1MCv8l4PEKRNEVvm5MEDvIZDEj1_oWBejkVDDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو مشهد، آقایی که توی این ویدیو می‌بینید، ظاهرا یه چک رمزدار ۱۰۰ میلیون تومنی نذر کرده و انداخته تو ضریح امام رضا، به امید اینکه زنش شفا پیدا کنه.
🔴
حالا بعد از یه مدت برگشته، رفته بالای ضریح و میگه زنم مُرد، تا پولمو پس ندید پایین نمیام
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149496" target="_blank">📅 12:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
واکنش حسن روحانی به سخنان اخیرش: اصلاً من نه کلمه رفراندوم را گفتم و نه کلمه همه‌پرسی را
🔴
بحث من، لزوم برخورداری «اهداف ملی» از پشتوانه مردم بوده است، نه برگزاری همه‌پرسی درباره دفاع در برابر تجاوز
🔴
اینکه جزو بدیهیات است که وقتی به ما تجاوز بشود، باید دفاع کنیم
🔴
دستاورد جنگ باید کاهش احتمال جنگ بعدی باشد
🔴
ایران همچنان در شرایط بحران قرار دارد و نباید تصور کرد با پایان برخی مراحل درگیری، مسئله جنگ پایان یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149495" target="_blank">📅 12:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هشدار نسبت رگبار در دامنه‌ها و ارتفاعات تهران
🔴
اداره کل هواشناسی:از بعد از ظهر شنبه تا پایان دوشنبه (۴ تا ۶ مهرماه) در بعضی ساعت‌ها مه رقیق گاهی بارش باران، رگبار و رعد و برق و  وزش باد شدید موقتی در دامنه و ارتفاعات استان تهران به‌ویژه مناطق شمال شرق پیش‌بینی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149494" target="_blank">📅 12:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مشاهده مخزن سوخت جنگنده آمریکایی - اسرائیلی در غرب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149493" target="_blank">📅 12:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8a000035.mp4?token=ndFZtFJrUgzXRyblqmGD63LqTs5qsZRLletHaefCbyq3IQVILL3NMaIvKQSBpn_ol8-CcmBCtg785-trNhNnvQt7kPtAAopRCBb6IhXVoHrDVLiWz7B4R8O-EUvQ09XP85wSizKAgH1JHz9oWRDweuU4Nlefnl9oaujHv6Qfyl8lnIYREGF9c6UuraGmnLy7Io_rLBS0-dUYHgAzJO7CLerfYzU5RzHknyFE2lKJ3GaFMRiL_-ZeI_MYuxgA_oN8Pc0MHfyEhz3ixCrs0dau78I-quPJPap_wXMHAwM_-sBfQ_CSWvJNfWuOlryz4xB6qOPMXCCniW7psEJRosgAz2hlCJ5CdnBvGz39kjOe7dxQ4TqT2cbiDAmGVbxEYELIWWRR3ns9aokJc8-A3YAnGbvsgjhxegC8mMmZJUxqiv-70Eq0b1Umm1BT2xjcl17IfWuA5mLiRig0VY0ldsLeYlzEzGi6l2g6LHNJOK3zvXa62LdYt4p-x-RmhUFlJYHNe9W-V4jgNpy5fEzzEO5yfoQ3zgXbMCg_uLFRUIxkPPJmKGm42dhF9bnTLLtV-jjRcHtrPMp0wNQy3NmmZvqmxbHRuJNjEKYMk0WHZpChumhr69TSC3DSVweiFadE1JA7s0LeRCpN3oKxw9sJkJ_rGFK5kTfCk8GEwRLCQkNw25E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8a000035.mp4?token=ndFZtFJrUgzXRyblqmGD63LqTs5qsZRLletHaefCbyq3IQVILL3NMaIvKQSBpn_ol8-CcmBCtg785-trNhNnvQt7kPtAAopRCBb6IhXVoHrDVLiWz7B4R8O-EUvQ09XP85wSizKAgH1JHz9oWRDweuU4Nlefnl9oaujHv6Qfyl8lnIYREGF9c6UuraGmnLy7Io_rLBS0-dUYHgAzJO7CLerfYzU5RzHknyFE2lKJ3GaFMRiL_-ZeI_MYuxgA_oN8Pc0MHfyEhz3ixCrs0dau78I-quPJPap_wXMHAwM_-sBfQ_CSWvJNfWuOlryz4xB6qOPMXCCniW7psEJRosgAz2hlCJ5CdnBvGz39kjOe7dxQ4TqT2cbiDAmGVbxEYELIWWRR3ns9aokJc8-A3YAnGbvsgjhxegC8mMmZJUxqiv-70Eq0b1Umm1BT2xjcl17IfWuA5mLiRig0VY0ldsLeYlzEzGi6l2g6LHNJOK3zvXa62LdYt4p-x-RmhUFlJYHNe9W-V4jgNpy5fEzzEO5yfoQ3zgXbMCg_uLFRUIxkPPJmKGm42dhF9bnTLLtV-jjRcHtrPMp0wNQy3NmmZvqmxbHRuJNjEKYMk0WHZpChumhr69TSC3DSVweiFadE1JA7s0LeRCpN3oKxw9sJkJ_rGFK5kTfCk8GEwRLCQkNw25E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ای که فرزاد فرخ زاد دنبال عراقچی و تخته‌روانچی میدویید و ازشون سوال میکرد و اونا فرار میکردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149492" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9af12d6d.mp4?token=sIiQbk5WrUauXOWq3F245u1qEaOdQVZtLr1mGYO-XvhM2RTcqI8ENGFLGMXSkCh9VBMX6umb_IcHK9wCgdHHknt6ekAsh_xJZWmzq3Kt-7Sb2wPQW9fWwpU06w5eZ8EXrXEyJtscrCQPJ9WxJygHPoIN-rpb_ZFxlWKznpeJVgDmLPvRDEJcUcOq1bA1iYIFOk7MiSEKrCFV2JvtmaYWrU93q2TtZUinV9t2_pcOhtAHWsztacNO_WqGXkKqk-MxMtFTDvol2tbhmQ_oViZ7IR77GkRIcvk6o5imJ-QSx4jCmZkFtFHE52f9E1MGz_cdzmeCb-e9hElXHOvClcdr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9af12d6d.mp4?token=sIiQbk5WrUauXOWq3F245u1qEaOdQVZtLr1mGYO-XvhM2RTcqI8ENGFLGMXSkCh9VBMX6umb_IcHK9wCgdHHknt6ekAsh_xJZWmzq3Kt-7Sb2wPQW9fWwpU06w5eZ8EXrXEyJtscrCQPJ9WxJygHPoIN-rpb_ZFxlWKznpeJVgDmLPvRDEJcUcOq1bA1iYIFOk7MiSEKrCFV2JvtmaYWrU93q2TtZUinV9t2_pcOhtAHWsztacNO_WqGXkKqk-MxMtFTDvol2tbhmQ_oViZ7IR77GkRIcvk6o5imJ-QSx4jCmZkFtFHE52f9E1MGz_cdzmeCb-e9hElXHOvClcdr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: من در زمان بمباران در پناهگاه نبودم و گاهی در یک روز به سه وزارتخانه سر می‌زدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149491" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149490">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmW9t2QigoSZn-YIGzOF92tHBHpejzbo1pqTMGErqJdn68zBPJAJkaTtfx8cYXTjMAKPOimeoMvJWF-OBspNXjR3eoJ6ppey9P9Uhm_StOybCPu8mXTZRCeLPm3s_DSXJICseHYMxDc2QOHlkXvWPLI9WxDGh8ZQfhS_6zvF3cO8xGXBElO8KeEKgMHzLpebA5zKNR3sZ5iMEnAP_Srsfqjkh0_dfiheH3CscxScfg3eDyPlm3clU8qjk5iz5Z5MHCrZCOfOmLPwaOdlFzIdfj6nqmGZ7_d995v0oxtsDYFZcS275deBDmQP2k0yXbMnv7gxWGVQwk5a3HkV5Jic8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای تانکر سوخت از پایگاه نظامی "العُدید" متعلق به آمریکا در قطر، به سمت دریای سرخ پرواز کرد و احتمالاً در حال سوخت‌رسانی به هواپیماهای جنگنده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149490" target="_blank">📅 12:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149489">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ToQSUFhr8JsWlhRPa_cpDu4MG8j2pqogXXfVv3EQSIu7ElsvCcOpZESDHFZs3kCPvxUMytPZyCDGM8Gs6617UuBiDQpAc-6OTvSRU7_JbOMyBCnP-KOzzeqp_VHfpii1qurc-rSOQUKPXoqQ3QnIx3Li-CYVj3Bi4-CQh2yE3Wxgd3X4D2wvz8K81MjpYDuuBOMQxFusnmNgRwEFxVyWQAGwN14EsqRabiC_JtJCWk9SNhSFlCLWsKEEcfXRoJMvEcO2WsZ2Q6pRwJ2t6tViDPnPpU7DHLuGm-W2klEM6wiX6T9DFoh65mMVuOdt3U6ZdrOU6bPNghfTwoSjZTAZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن در ۲۵ سپتامبر پس از شناسایی یک فروند هواپیمای شناسایی ایلیوشین Il-20 روسیه بر فراز دریای ژاپن، جنگنده‌های خود را به پرواز درآورد
🔴
وزارت دفاع ژاپن اعلام کرد این هواپیما از سمت قاره آسیا به سوی آب‌های نزدیک استان توتوری پرواز کرده و سپس تغییر مسیر داده و به سمت قاره بازگشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149489" target="_blank">📅 12:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149488">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وال‌استریت ژورنال گزارش داده ترامپ در محافل خصوصی درباره پذیرش شروط آمریکا از سوی ایران تردید دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149488" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149487">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از مقام‌های آمریکایی مدعی شد یک ارزیابی اطلاعاتی محرمانه ارائه‌شده به کنگره، احتمال حرکت عربستان سعودی به سمت ساخت سلاح هسته‌ای را مطرح کرده است.
🔴
این مقام‌ها تأکید کرده‌اند عربستان هنوز تصمیم نهایی برای ساخت چنین سلاحی اتخاذ نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149487" target="_blank">📅 11:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149486">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با  شبکه سی‌بی‌اس آمریکا: آمریکا برای باز شدن تنگه هرمز عجله کرد که باعث شد تفاهم‌نامه از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149486" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طلا منفجر میشه
💢
تحلیل عجیب
🚨</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149485" target="_blank">📅 11:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149484">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=CdHxKHdSj9oi6KiunpV01eCTJq-ap2vs1Ku_DMRevLJQvyn4dgItCek0rCEhhqDn5sNCSZp5kR6W_4eFicsloalo23qaUx_rDeYnkbHS3WzDsE-YcIPF8BpvBEo7oOEEMkgr_z2S1323ZP3nI5r0fKzEprwc4Nna6DjE1GxEYXQQTHXLv7iTgNDFw59plYCDFUaJT3h2CSKu4ob8SgEpbIfGE7gv360v8ah4dFTidTw6Y7PKGsL0jC1uQG6XtBdRNFF_3z2wVdHy5rxmchyOx5TNSSPd_JVOBAXzwfrxD0K8EaBJxkiM-z0SdvS3ddAfbZ1HHQcU6ChY5OEZG54Fag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=CdHxKHdSj9oi6KiunpV01eCTJq-ap2vs1Ku_DMRevLJQvyn4dgItCek0rCEhhqDn5sNCSZp5kR6W_4eFicsloalo23qaUx_rDeYnkbHS3WzDsE-YcIPF8BpvBEo7oOEEMkgr_z2S1323ZP3nI5r0fKzEprwc4Nna6DjE1GxEYXQQTHXLv7iTgNDFw59plYCDFUaJT3h2CSKu4ob8SgEpbIfGE7gv360v8ah4dFTidTw6Y7PKGsL0jC1uQG6XtBdRNFF_3z2wVdHy5rxmchyOx5TNSSPd_JVOBAXzwfrxD0K8EaBJxkiM-z0SdvS3ddAfbZ1HHQcU6ChY5OEZG54Fag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از برخورد اتوبوس و تریلی حامل میلگرد در محور بیرجند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149484" target="_blank">📅 11:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149483">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149483" target="_blank">📅 11:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149482">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نشریه CNBC صادرات نفت خام عربستان سعودی با وجود قطعی خط لوله به بالاترین سطح از زمان شروع جنگ ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149482" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کارشناس صداوسیما:آمریکا تو جنگ نشون داد طبل تو خالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149481" target="_blank">📅 11:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=Yv7HxP-mEilZsTBAZcU--K3PnJq9BUepcjzBSvIJqNyI6JiTMORxbdmhyZSGTowGI3AHeLC5pQoqGii0PpAuX_z_n1aOwqtCEqLns7NGNVISoGlvsbcgq-pojjwW9mbdJug_Y0I43ypjZwg3HKZ9QTMY6m3nYLA9TolUW7PY-YIrOrp9RzVDsdhMQBc7xKnUCbuW3C3a8Ltd0T992Y51U3e1Vm21QD3vDAIk4y__cdS4zFCommeZrGfLpOWNFX8KpGY41qjB1hBrZCh_AuCohB0BBGygirdHFpldJbmqnret79Yc0pCbasbRefDwh13ClQzJSBkNAyXfiKjq6a0V3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=Yv7HxP-mEilZsTBAZcU--K3PnJq9BUepcjzBSvIJqNyI6JiTMORxbdmhyZSGTowGI3AHeLC5pQoqGii0PpAuX_z_n1aOwqtCEqLns7NGNVISoGlvsbcgq-pojjwW9mbdJug_Y0I43ypjZwg3HKZ9QTMY6m3nYLA9TolUW7PY-YIrOrp9RzVDsdhMQBc7xKnUCbuW3C3a8Ltd0T992Y51U3e1Vm21QD3vDAIk4y__cdS4zFCommeZrGfLpOWNFX8KpGY41qjB1hBrZCh_AuCohB0BBGygirdHFpldJbmqnret79Yc0pCbasbRefDwh13ClQzJSBkNAyXfiKjq6a0V3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با شبکه سی‌بی‌اس آمریکا: وقتی آمریکا به آنچه تفاهم کردیم، عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/149480" target="_blank">📅 11:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00db30387a.mp4?token=DinefgMBU7tftG9A3i6hYfAuRFpM04CJyFARBjCkyc_W7RfeWfuSmD0sH0U51xq6Tze9ei1EoYfKXPqq456VgHbG8tbayw_iM5Ib1bk1yR_fv9mgM-9srAQWMZ6N66UA7Az_u4g7mFu5VQAfG3l45-f3_PNTkLhWYlcYj920sz-gPMyiKEm_pSBskpCOWal-irG-vT5Bk0u5PmmVoh28vZfDJp_72JarBv54OJkFnCMnuBhQ86_7tIQ2pD_zu59kCnCQeMPVSpLvo2ibStg8rIudhkWK2gzZd-sMSXqSm0oexxkNgm9y3FVdE-a9N8e1H2oPGiUFqViA41oObr2fOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00db30387a.mp4?token=DinefgMBU7tftG9A3i6hYfAuRFpM04CJyFARBjCkyc_W7RfeWfuSmD0sH0U51xq6Tze9ei1EoYfKXPqq456VgHbG8tbayw_iM5Ib1bk1yR_fv9mgM-9srAQWMZ6N66UA7Az_u4g7mFu5VQAfG3l45-f3_PNTkLhWYlcYj920sz-gPMyiKEm_pSBskpCOWal-irG-vT5Bk0u5PmmVoh28vZfDJp_72JarBv54OJkFnCMnuBhQ86_7tIQ2pD_zu59kCnCQeMPVSpLvo2ibStg8rIudhkWK2gzZd-sMSXqSm0oexxkNgm9y3FVdE-a9N8e1H2oPGiUFqViA41oObr2fOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: آمریکا و اسرائیل هر کس که دلشان می‌خواهد ترور می‌کنند، بعد می‌گویند او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149479" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=R0q9U407M9FTkfvJzxihrfnUbykDTYlWyjJPMV91m6CtB9zKJ8liwzyjBy8_FpLOEMwynQaAixeOIqu8ocl7OWTaZCW22tf6MWoaLHH_yhz6DkHUOdMhw3TixEyOE6ymyM7ePA-fS_sdlmeA8sb2UDoF9srHkRPQjBaPGF945s9b5mtTkRyW_G5XV1KSJahMj8sjzC5-GTF09PzQr92IiV6isc_E7LKR8gg0ViampeOi3VIHXjhSQl_cgOm5xoVkTwLynGJ8uhThI00Py_Ybr2ILbTgkTJf1sdLTl5xc_3zet5R5eecU6o9CPfzp9bZuCYRwEcJ7DpedR7kgJlMzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=R0q9U407M9FTkfvJzxihrfnUbykDTYlWyjJPMV91m6CtB9zKJ8liwzyjBy8_FpLOEMwynQaAixeOIqu8ocl7OWTaZCW22tf6MWoaLHH_yhz6DkHUOdMhw3TixEyOE6ymyM7ePA-fS_sdlmeA8sb2UDoF9srHkRPQjBaPGF945s9b5mtTkRyW_G5XV1KSJahMj8sjzC5-GTF09PzQr92IiV6isc_E7LKR8gg0ViampeOi3VIHXjhSQl_cgOm5xoVkTwLynGJ8uhThI00Py_Ybr2ILbTgkTJf1sdLTl5xc_3zet5R5eecU6o9CPfzp9bZuCYRwEcJ7DpedR7kgJlMzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا
:
هیچ ضمانتی وجود ندارد که آمریکا و اسرائیل دست ترورها بردارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149478" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بغداد: مذاکره مستقیمی با آمریکا برای مستثنی کردن برخی فرودگاه‌ها از تحریم پروازهای ایران انجام می‌دهیم
🔴
هشدار می دهیم تداوم بحران‌ها، پیچیدگی اوضاع را بیشتر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149477" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روزنامه کیهان خطاب به پزشکیان:
چرا گفتی به دنبال ترور ترامپ نیستیم؟
🔴
انتقام از ترامپ یک ماموریت الهی و حتمیه، خون‌خواهی مطالبه ملت ایرانه و ترامپ باید کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149475" target="_blank">📅 10:39 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
