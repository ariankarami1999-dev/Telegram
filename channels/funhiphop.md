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
<img src="https://cdn4.telesco.pe/file/OXfZBxJXwcQA6tYk7B0UZw5IjDh_LArjxR3rICAipzw3hukEOejxiFFb4PXc68sVWrYuW3z3YjMXQyz-zGPH9EHElvtiKcKlW1glvfWolO-NbUVBapvobXd5uN0SnlDc32HkiYXj3f1sCjMAA9mSkk3tWA45KCtj1kE2l0VaMxymeaoYhXejGKsswmaupSrtRIaTUEtNAMikbtOgDXzkm1-cEXJ0lHyRxTrTHd151-fLRb4wrNZcEaeqACldGrN5LltsLTsGLNwpfOpWRNnO9EkK3xqpMgBPXXkiSHPsqngEOfjS4Jb9h8dsT93iwNaPA4y5oNKYJCouy86JB5X5zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 193K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینهمه به یامال فحش دادید گفتید بزرگتر کوچیکتر سرش نمیشه، تهشم همین یامال بیشتر از هم تیمیای رونالدو به فکرش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/79564" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ببین تلخون چه موجودیه که برا اولین بار حس کردم ادرویت کارش خوبه و بهتر از کسی بود که باهاش فیت داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/funhiphop/79563" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFWpv7ZUxS9SCXtBiowiymnH24X4GPQo9KogP4OnskzRMGJGea-PZtxp-_QMSU2yRhZt7eOMAzO0V4oOP0gSc8KphJ7Ga0cpTnKm0WhtzJXMu_aA4YHCetICOzAQaE6MqfY7V4rBI9Ql4j0R7ACZWpLghVaEShKMtq2BbJE1wiH-JI9suIHMm6IBNdyfdx0YppIqk9WPxCoZvnT6H7PzxWX1ByktQl9mztQfRcWjQ-fwa-mrKCRuI8muGRWEGMdB1A3XLhDKTcA7R5t8nKSVgELNH7x_d805cc8vSoStOSkYQF2msqGvgq2G7W27pkbzBfkDbMvUaGj6aWBUsCXQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این رفتار لیدر طلبی برونو فرناندز که حتما باید خودش همکاره تیم باشه بعید میدونم منچستر هم گوهی بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/79562" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/79561" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عجب یک چهارم جذابی شد ولی</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/funhiphop/79560" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بلژیک ورژن فوق تخمیشو برا قلعه نویی گذاشته بود
از بعد اون بازی همه رو درو کردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/79559" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام دوستان صبحتون بخیر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/79558" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHExtvZ9Mt69LWPsMyEWHb3SGBNy_aZn1AsMDo0ZsE8eQyw9la7ebVJjpd1hPCZGFmBCwFWWyfWRyJ9RNCQH_woNjzAYjESKEFxKLva2tbWRyoaVUSud7ALO7s3LAVCm0tAvZz_k9fAGvHnOG7ArBB2a-sO_9xMXGCjMN-BITMz-r7-trYQLxgpfqXShtlR2I2YTMKbls7TXDq1J5MqTyc8ImcKEImp_TiKcSRBwWpeP15eOBMeuuHRzbot8qb2QLjGENs8TdWWo9oBKbk2Wmcud0o8nSZdiXZJhtbGGUlwKxdIqZ9sC-luPSnAY-aOyAFZB4txvG2FPcWKHE4aupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ذره حرفات به قدت میومد هم باحال بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79557" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYoGh7yKGkjIYeAo9bL6rQtirTHo6WaKQiy5pWyfc7jFErDnKa5PiNG-7KvgbUMBE1-5-rlZOcRfeoSRd1WRJBeFbthKhlA7tIPCZitwzaK7doX5fLGL6oJH60zyy9-YpLBpzNI9aFPvkweX1g6o2PMWbDKQXBz6LwqnuhCW44OqExPb6dnshcknjbtKbCX62keO0UrMlAvRUVDA65srjNN_DR5JB7suXgqqUM5KHrFfhQx1OPMn6MiSPUbs5CWF19BgfFCVx-0lAveuXS3umiqkLy2RE1LOX9wCnjfpk4uq79R6Isc5Q_OKxUZg1goN8KfsaAWoWnmGvGi6OzJgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfiv8rhi8IuAplyxVgIWZtxTKSTklIcg6ZuWWtlhWXEfLmHNDNhtI_fHMgwau-zpOmTM04POuCiWw--10wiRJj3Bi7QkFFY-Glj-I4-tdsV_UiP8wE94wl-pt_bWsPNtXHa7qylEEJG_wIRWPESjJ5DsEqMlFN51q7GTBovHnbMEIYCf7UX5JPVa8w_wEZ1KPOoNatrO-vbZXk-FqDaalSYZhMr15Pcn5u-mmVEhQz5lXOSBVvrV2gr29qwJAH3dteU49jyZiC4xg5qFdfOufR7WfN72QNMI5-JyVHG9n5i5icdBcFCTqduQWuT7w6uP8ZZzaN2qoD15Kd5V3rn7Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فک کنم دعای خیر زید یامال بود که بردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79555" target="_blank">📅 02:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن  https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79553" target="_blank">📅 02:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79552" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب بخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79550" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEliAS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVxq9SUGbxDWs5rKXXBSa68_F0juU1BN12grnHOWQiOVUmeurWr_5Nl826mM8wQ0iacmcyu1BYnCyEvgoZo6UHM1RXU4Ami3Y_hKGSO-zdt0FN-Mf2jb2iaSA9TSGlBeiM4SYKoNe6cUtbqLsvdOKMuydjrV0TI9tzUhjGla_W3OEpUf8j-3aJiHcSg9n2RdH9DYmU7yCfiPm3_AuiprQrMupRmtvdMY1StX96CU0DonZtuJTmsiMDxI3dS_ANqfA33GDnNNmlkpD0PqYBHcaoCeXyPtBVK1YYRubh0uIwgIC8-iZE5asKkhFa8t4FtZcA4M-VM01KOv1gQJpkgUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعصابم از تیم تخمی پرتغال کیریه پاشم برم فیلم ببینم:</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79549" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79548">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان رونالدو فن نظرتون با خواب چیه؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79548" target="_blank">📅 02:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79547" target="_blank">📅 02:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHadi(idk version)</strong></div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79545" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7stEHgwAodYv3Kmg5Pmc6PfvHoDmPjJ7D6M4OgQ8cXlSEMSk26DJaE2fWw66yo4r0BpKRcZMAJ8LYIbuV2kTX29LOIIeS4Cp0JVS_LysJ1ef93bBV6e6YWgNGRFRMwFe3cHYrti7JxElj5H05IrC13DmtvJXd3gDXvScMfQyShw4bL0xeOshYW46Mwy1GjV7IJoPb5vuEGVZ_asozyeLjGclAb2tTCaR7Hr8e3I-JuTGKLnOIvetdAUU36rsCfORzC2SDtLC91iUmWsP_xDYdGHGkzu1FUTQbXghr0YrQEmYq7eZmsew2_1tx-Ew-ceMpeXcD9DzMIEbT2VMwfJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79544" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79543" target="_blank">📅 01:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIQj54CThA0oQW_iZ_ROdiEJFsfwWUkSkiXO8l-OdNWzJhsG1lMznCakxV3guUwE70Nm33Bf0-0ir_ifjQcvqs1ZjRzkklA-VigeycIjp4BP-Q-qodBRlLBxUdwQlbhKRwJ-Zi8B4MtNmyi5cllFoYJOC8Nk4OLGjUgBmd2dXa09QGkG1xapC_7n2R4rfkKhropmuqBDKN87mf2X7xgNkjnICSnJ4YgSYAtbVLGISMRL9ImEid58rNXRD1X9Au8ugR7yLHkKWASzPlh6-hfznp4Y1GR8uwMPfRk8WJndFHAKIcqtCQJeWvFzYbfmGnb_HpCxdlYd66sQYuBUrhbcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیاد گرونم نیستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79541" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شما یادتون نیست(منم یادم نیست) ولی اسپانیا ۲۰۱۰ هم همینطوری بود، خوب دفاع می‌کرد تهش یه گل میزد صعود میکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79539" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کاربر Mmd به ائتلاف تحریم پرتقال پیوست
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79537" target="_blank">📅 01:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7PSVx1X_6JV69nsRaQxAsnND7cQdnLq72zKJy39ssIyO7PLxiC37-fBiHlo-XxzQoEykREeB9UJ1LKYbOEFt18Ryc3q_AOSKMBv5EwyIpDlqVYwDUje03IQzK3-HsdU0Ph5atapr-gkpDkWjs_eoOkOz6eusqXlvnHx-TjrfthUm1BUFyBlQdZDU-qKogqmvRLmzSV0ubohdQB54zlCmUGF_InD9zfvm42yBiK78qH170Om5eFhxLAq-Rwfl71HqcVPSQFGHJGHsgho9dSV5b-HVZ7DGq4L-eHM03Jq6CKI82fewJACvX0jKagk2gDx2ZZb807j-7o4a0q4Ybl2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا داره مارو میکنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79536" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رونالدو بعنوان سرمربی جام جهانی میگیره
بماند به یادگار 405/4/16
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79535" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOQeWjSB3kYLu-I7g9MNxx5sX-nzCGx98RWITiairJQFInmPYn3_WsPbYXp_IR7UA00qwRlGJ5Q60trdfhbDQFJSFKxD5AsxUKhS_K-ZbAVe6yjMFYw3sv9Q6YDGlOZ6zk4XL2dcYkK4wszYpMND2dNFutcJXsbQ3_qHnpvrCNAyNcoHimvttkT5P6xvz4mCJJdvBSi_vdZ0lYNxOJ8l3twYZvdBT1qODsybxs5rWbjR2P6bo4AlJYcZ_l9lgLJ5_bQ54-tWNOl8uzzpEEjzluYLjT6_lgstltLVLyJ2DyOid6zVGWbrfn0QTMev2CcmGvIpv-0tYFt26ZVEp15xRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا ۵ تا بازی تو جام جهانی انجام داده یدونه گلم نخورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79534" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان بالا برید پایین بیایید مسی و رونالدو ۲۰ سال تو یه سطح باهم رقابت کردن و الان دیگه داره تموم میشه، با کوبیدن طرف مقابل شخصی که فنشید نمیتونید کارایی که اون یارو برا فوتبال کرده رو نابود کنید، پس شل کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79533" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عزرائیل فوتبالیستا داره در خونه تک تک اسطوره های کودکیمون رو میزنه، نیمار، رونالدو و به احتمال زیاد مسی هم بعدیش(
فقط رامین رضاییان مونده
)
جدی جدی دوران طلایی فوتبال تموم شد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79532" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLgq5zd-VzPuebneykTG0B0vyaKNzmPeTsqxQyybZ7BOJgRZq0W00acBwVxa2HOUtXi_CQn2f8S9bwtBbvTQ0d7r8DDypRbAzxLQzkcdKEZ1pAJTxV0REChCXX28llHj0LlUAgeekqUvxzk2ipjEJwaMpGNcmAJ08iyrBLjPvKJl40J2BMrsGPT_xKf9N9nmYLKdgKXHzEdD8PthBiID-_PDV--Mkw88LVuexFwAG8yo2dRzW2HT7lv5Wg8PaKjE1DB83h1WCPQ2ue5kYTsv0YqR67tc3G8ElULxREervyiJNMjwl1F_MC2h-6Js0NoCMcfjiiKmzlT2z6Iso2sMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79531" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBvxWGjS2CPwz-H00Oc8PiBq46o8t47viVuoKVHzhR76xM8PEXb-f_F9K99ANt5KwKH8XR6guHjQ4ce4Jd8KY1wpBLuQEPcfAI_KQek7uicg7lyYgSSRpDXU0YSotk7n8zRthfOVUhQmaKQW9xbJOFRbT9CnlOcfu3-QON_bVHK-D5JBgYJMm2XO8bB7YHC1kVj8WYlYwCcfHZ1ld5gIQhRq4j5jeUS-N5yjGlN-etFr9wJWjl0QmvzlQu6aYgMY_SKoO0Efbv-MfPwxKD3QWe-DHQlH_ltS8Y8qm67OMJRHv0AtcyM-koMkyyTtAu1yF8mV_UMTT0K_wr1HrOf78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای تمام شوخی ها و کری ها، پایان ۲۰ سال سلطنت، ممنون برای همچیز و خداحافظ برای همیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79530" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=Rdc1f5AOOHljxiUfkhL6GZbZJXZ_iQJ1N6A63_6NUzAaGWo7yEzRgw9n7QOUobaFpuqWiTZemHTZwsuw4JJVsZ1cTjrGwAXRzOXKB-HIixAD2Ql4lgzb88LBE5q4_hYLOX2SRGTJIqDlsK6_zk_lst2VdaSxPtWn-PlOXnT7gGWipZKDJf3VZfN_2797177flsLD4Yls4D7gGuKc4Y9bGfDDeJclVRMS3_2pV4uw2z9ykGDxAIngGYQNvs2Sl01snBfQfGqvNKwZFGayeAg3vPBHbZAxLfC6_UE73x2gZdFOx6Xxs-eUw-Lq94f6T9UcVcg6BvVWJVjF2XolYyksig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=Rdc1f5AOOHljxiUfkhL6GZbZJXZ_iQJ1N6A63_6NUzAaGWo7yEzRgw9n7QOUobaFpuqWiTZemHTZwsuw4JJVsZ1cTjrGwAXRzOXKB-HIixAD2Ql4lgzb88LBE5q4_hYLOX2SRGTJIqDlsK6_zk_lst2VdaSxPtWn-PlOXnT7gGWipZKDJf3VZfN_2797177flsLD4Yls4D7gGuKc4Y9bGfDDeJclVRMS3_2pV4uw2z9ykGDxAIngGYQNvs2Sl01snBfQfGqvNKwZFGayeAg3vPBHbZAxLfC6_UE73x2gZdFOx6Xxs-eUw-Lq94f6T9UcVcg6BvVWJVjF2XolYyksig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79522" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79520" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd9RaGxEgc2rjJuNgcQSnfdExqMPwY9zfLDDIuUwIXeImsibowu9qgJHQlyy6ykpzpUjUmXlG08lrSng6KusvC_l3hPSwk-2f4pnoljVGd9C0f9noBRuo3ioi7VvPp-Qbv2HVuP6b-8Ujis0gQmhhmDSAN6SSPXOIQ1ITiouIqrefMhbiLiNx16Vsx4lVmhoBECXFgvFNrhXCsYOYjmhowBoZTtFYeVV2205QwQp6FhatVxLwNXbgqvpWVqmHS8GgYB_TpAznlQK3YKqzYZYbEKDP1fcJ2CLb6tlZP0cGSpIi3S_kbzHecrWE9RA8xhmk63gBJMasKbJLkdYgwli8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع علی خامنه‌ای توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79518" target="_blank">📅 00:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یامال داره گرم میکنه بیاد تو زمین</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79516" target="_blank">📅 23:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بابای یامال مصدوم شد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79515" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYpG9vxzYRyC9_vTaJKSdL_nIDnWpcNy-VRpTbdnEYA9Fq4KUuec_QDU6unowv2cX7XLbirOZDLWqtF-W0jKp6FqKFhdvz3est1nIeYMwsjnyxQhiinqFEksUsEBCRnjr_U1dG1CBjj8AgA3h_-guyc4K3_u6NCJJ_81QmkZP2yrnSv3GhHIIteXRWs1aY3_oJIcMZLVRySH7Fq94vOh2RI4vOsQH6g-57rQaEUw_BmY6f1EtePgDzRnk1OET3--LcMbfBI3_TM9Evfuk7rrBEUDtH7v7QR7kMYoqepO6HdMmL5iklYBEz5wOcUHI5vshjbeZ0DCSY-UhKXxUiPFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AghZqQZkEmii8luIpWC_PrB2RbaxLGSZhP555mzcep2TgD6JQqlvaMlxIhkEkDSowU8SXu50GjUbZLYinN4E2lnzZwRYTIwV8Oe8PYXWkCRhK8eJ-vkh4j4d9LXzoNOVKot69MEp4exaxLByDBpQGb57SiZ2nGCF9IdtmKHO_AsXaYwDoIMR6SCjZ98yBzU6f1dOtkUztsxTSs_l1uYYOtR3MSNXsTBlXC0JVelpjGw-nkbDbrcJkcHeqAUqDhm7szmGCmlLrSXsA8h-79Z9GmuHQmOw_068Ptqd6hUrLik3UmnpxjO33av7Xq9SIZEn2YdNR8thNtFbFvKcechfdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلیفه سوم سلسله عباسیان هم امشب داره بازی رو تماشا میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79509" target="_blank">📅 23:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امشب حتما ی تیم صعود میکنه و بازی صد در صد ی برنده داره و ی بازنده و احتمال خیلی زیاد هم بازی گل داره.
بماند به یادگار
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79496" target="_blank">📅 22:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktA-11nFuA08eailmV-efmzCx1UWq6XDloR5rtGxcImiIIOKlQdwezY_HGOLmmQb-1cOLXSgTTrGyGv-5VKYFXda8oTqj63t6yClz6WOutx1InRMZqsglhKYEx2dQK0EpeK9USrFiEJsGixCivresMUERBWJZWuo7tFJcjyFV8vPQNBbmBR2zmwrZnmneZ2j6exIQn3fxoyETQlE-Jdx4qUTnUjYJOa2CWsL1T4PfYDQGQOe1SfFE74HkL5bx-iPFNusNv7GZf6-zF9pWaEkNgeBJA6JtOXdjLCTgDpno0Su4kU1-kJR-g4isS4E3nofyBGfKZr42K2kLEFhmRnMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی نکنی کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79495" target="_blank">📅 22:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTlXAbWsCExarjcI2eqpIGVGzyesNoI8vcv8Y8ZDwaFYRUaqYd7gZFg_tTHhllWXzGFOWjuEF5OdoOt_VhjZ6pDr5xpVj202uoEZtuT7hxodgkwTUpLP9V7XMPCKNespkr9220Zuuk4IO_Y-EZNBeLlqpMPWff0qFbVyz-SmW9ThWPHzeHNdz-OOHGRGVlG3iWOVlj9cMME_zA14Fl6ksOqB5C9eShwaAacRIDhbQ1TYlXJl-IzysfPS2WDIyGmRG3OeIor2Fd2rtlWNw9yw7jCzhbvPtQ8AtBQwAzzXqDxb58RC62cexsyILYStd6BssoTa5PrRcNlZWbN4JvcAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79494" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx4vcA2M2fQCQTpgRBE7V4H7b9FmIZdYm5eGngu--G15H8miYtj_ZGMs-lBlx41M3CFCYbo0Exhw7EHRgWsejHj91y7NyucA_sSYGhtLch3sa7nmyqg7jncmACKjSqSZ7orACky8_I-VRwnmx9yqMKuokNmVzD_jdTpe8ekEiVnrLPZRXTfymicIegYgmF3_zHQppyCW69crZsiazrJ3QBFy0D3ZKhHugNoS-OZGmkRrOf54bmeZmDzuubbtGMpH2PzKwqGxoZxfeYRMrOkTW5A3Ktxv3QNjzfBe545hAphruglZY4rMxEvr5Ccbbug3A9xnNvUkQIep4RpQIKTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79493" target="_blank">📅 22:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط 40 تومن
🚀
20 گیگ --->
❗
فقط 79 تومن
🚀
30 گیگ --->
❗
فقط 118…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79492" target="_blank">📅 22:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79491" target="_blank">📅 21:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ژائو نوس امشب برای رونالدو بازی نکنی مادرتو میگام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79490" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otzmjCi65UWP8cdAF5V9jjCvdpVLxetCkDzYY1vQvgOxtD21ozWBHr9l68pGyQttVFvkgm4LreRlkjUhqyRe3E1yq6_bOMtMOQIEWBikMRmvgUM74dOXwapltDsRf770cXLA5X5ORmRCpqDDMNmTwv8vKPPDtOHgUl9I2NJ44YKPWx-27dvGJ69eNyD7orG5bUG07G2rGoHAqEgm1GUoeaBBYm8G3s5iQumo-R0Lcv2uXGxhk3qApacWoN1INO9k8WRSmJZ4cwhLxQPBjupE5Rr7_7oMoMjEohy0_h6Ncp8NcapzKTTc8OypbYHDvPKqMpBqDyLbr8K1pS2lK8sabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماغ بیرانوند تو گلوی کینگ گیر کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79489" target="_blank">📅 21:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiLpnLWt3eRL3urXFu3QeTPhVShM42Li1l-tkv45wRAlpKSPYd1awfhJnXKrqcDS0p1Vafc6JgXZztocFfJQe2IwUiPeeWow76AABO9rduvMd8lcoWyRhlnOwKVVrlCebzJP6SkpBABkIMAAzzeth-FHch1He4Edk71qVT0t-R9Rk8JD-Vnvc8SEL202fNpVnq8pY4JcazHCTgmNPX0QR2rYHXf1gLbA4WAF_fqOZrXcR1nXoleoKvTUlnrwrtOWazRoRbXd7vk_-bm_vxZKuao1yVi12ZqM_7rv0vgu65luXgruJaNC2bpWU0iRlSHuJJFR-EW-wDRYdGfjfcRx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب اصلی پرتغال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79488" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انگار این ترکیبه فیکه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79486" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGhviELBrVWaysVL7NUknJN2eph82G3yEEUbF57bYUR-vlUo56PQKgiW1U89jnAYXLN7N-NfP1S0c3CCX7boD8RCPJ1lh_SNtA_2vWhXaUWg6MbaIzabcZTTLtX-iD2fk2MjtPkSS-L04M6K5Y1E84TaoqJGrrhUNyQFay8OeLLTQS-ytSEh9074Rng6RxXox6Quim__y5Ux9lfP2Q8aVjbvz4GBvjctO3yqMBjYaiQTukMO9bEdQm3ai5LwBFVQU_rX4UVTa47LgUtmIp43Yn0wl7P3_o18AwC_qWz02YezKlV_i5BNSdTkQ5p7MsvOIk3xURr8gldengRAOlDOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8Z1_c-K9swPALzLZU4gZyvqCQPyQ-pFodG-puBRs3qOum83CyFfAlQBkO_UkVaWckJq5alX8ahMWDPvSZY3f0ZfuPILAGcPx1dR0lRUHEYNstYhrVmSO9iRkrwtwCb9JeTHPedQ88Pq6LoRUn17qJlTN7SvM3vdu53aNatNQ6NsVcuQsHoL3MLd-PmHBrzO7jFJqNMJGHbWkVUlTVbp0g1IxMhGi5vSal12PFFdS9MyrIVVNYJLiTXV-JOB_EkQJJsSRLQpNyiwwizUy0Zul-GWFs1737E7feTNQYnNjvLRe6ZHuoltRiSQL6DoVNh06cr-88KUb9P_00l3Ltfw-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوس بدبخت چرا نیمکت نشین شده جاش روبن نوس پیر سگو گذاشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79484" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مبارک رونالدو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79483" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoH6mGjZd9tnWDfsLXP8uW9ebAap_9S6pUB7QytiFSeqV22VinvHI3D9AmGod4rX4ueC2yDOOSQ29tx5b5odb6vVOjjDsEA1hu5ZeZya71tHZ1mRSljHnrOwiSygh7ixiZpPuckOJfV3ID44yb-fLPZISAjgiuo4dGHwGpOIzvCrCwmvLVIRAOEAhA7JCfVFCmIu_wzcT3EqCyAQ8Hdj7ZIAWchHT-eXtoHuHeas5LJy0Ab36FLTiUC5THjk3w_IIpUiiCxZE23DgIlszuq1l1h7MwrHDmIheHk1BjT00VGRbPdTg3VwgW2adveLdXPLyB3RwQYhVYOrmlgDQ3Z_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبارک رونالدو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79482" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clEGJ_EFK4AC_elgA03ar8a1Om_6s1d_S755zv3e59DgVSnaC_aUXRbajv5_5WAUklKpeMzoM4tW2vy7ozixCMRZrOR_HIbj7QRVsDCvbsMN-j2MQ65l24GYdUEvSdaDtepv_PO_k-67L8SGNtUnAhkWoT5nRUHZHitj0P61buP_vHkq5akbz165uy_GcZllcrsyocNjf9KIWA6nkSa48vsh5bV9qwUm4jtDHaP8OGr5XOrB1QP_-klofMGtDXNSpXlVbtZJIBQbHGoM_BJN3BNIrWKik5D1A9wAd5ZudRx7n-AXi3EQ-BPLzS7-wIhmb0_d4CwDv4eWzUzCmmbP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79481" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osGwRmaIblYvmlYIaubyf2_HNWlobEl_fyg8sNwe4Fhtq0XqNxVEpXLIL8WqZ2Hfzx37PRwCb4P71EqSgY4VfyaktzMXtSFS4R9h7WXF6-isQuVPTvDyD55p6SnpiJGfi65447EJsyANLor0uUl3ocGDTsfJ_DNmEipjXarSw90tAtOYUzs_dwpw-Ej5n5R8DAqgOFq5bmM5VnsJ0gxCQciGhqhdbH7p0tmfchra0x_QAr6Zn4DmfXkBHc-EMap4uIS3E2DJtVKxpHZq3Bj8SF3bEFeLjMd3w4RHj6jY8FkAfkZbAdIMu52d4DJa12-7qjFRbvv5p7_BfEBrKMu4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79480" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcyV0OYyvOGYiPzVCfafY4Q7vDcMG4CDym6h86bAFsGWRU3KfuCa7nt9Moe7klm9pBl4BpLihDvHF8HaJhdKluFQzVWOInucX_C6bFW2qiwa-7UXJEF_JBDgiYnHMNrI208VuMRCPFzAlYjRP90sQfn12_nWEXUitSTdBq8PXcY6lcPCtmFNBRmUSOG0CnNuTgN4mG4A5g-KL2aDB_gnB7qnfBrjsSvhXQNNcKYuJj1kp65jntV4tP6pFpVtSsGWB5askS0B6ebd1MXpLVgQiurXVGwbNARtHb1Ubog5AYs66d734RMFiUnZCvS0WDaIzgGzNimGHMEzi2aOH4hFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79479" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79478" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حماس قراره منحل بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79477" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoNh_9IYQvIcv53o0U_Zhs8QJTLfvBdiwNAwPgKi0ck4Hm9u53-LKWH2hWhpoz9hX-4zcE_zs3prOfBGfC5Dd4t9D-i61e44D8fGl0FM0DofX30sgZIUEUu0HuUGNZorPOt7bg4HGLTUgsAE0TCTGCeBgJGa1Z9CteYKYRm9vggUgvyamqnbPSzbwkVdInB1YsxLgpX2MxqDFRxnKrU9j1A69FL8PqlmS5zWVrv9d1J35-JScQ-lOycWsnpoableKrHERhQ30ufnfgfYWcMIrXfSUSyYjiH-KYcLrdXfkcscwLwmhQCTUioCHu3TJlSIDB3GTYRZzxwjHQXI5zaUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت هر تیمی پوشیده اون تیم حذف شده
امشب هم که با کیت پرتغال میاد تو استادیوم
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79476" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOzsceQjFuuxMiqJSolbVFJlkmZiPW29xVrI6_vadVWMs0gfiDyxtlM9qqso_euTioZeVSghjoF-2bTQhhqz5DGadsi2-_PFT9x0XEa_2k7mRDG5DbsUEoA6Fz_dwGbUMfdofn2HK5QJCxqLjGccGItg-KV9lYW6DvpunqjfM43rnhzjfxwfDAI4lNYTp9FYft6NAV8nP6rGT5M_ebCK16L6_JwmsgEqcSCV7ubdLnTZ_6vXySgSW0zXdURAYRPGnrk7eYud6yHQ7Kxsk6BKY5Qifl1O7EE4Ye7V__nA4ljjzvBAl1brsXi5YyCQXW6fQGncaHfWdExh0rBfeQUlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79475" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیس جدید دکی به زنش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79474" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddb338012.mp4?token=KmGxd5d6sUwfxZSeSnAUmiD9C3mjSGJbC9EeRuCK5oGU6XgN7F5fP4CKv038f4mNhC_nvteA4isZBiASUXeGmd5Dex2046n9Qvu6v1ocNznvJB-7GQSFLCHAHMOSPpe-w-QulRBKO-q0xTfKlhtAhjkwhIBfJssTcWj3UsYCqqN0bqFjuMq37EB-MwRyqe9V81fjO_do5ItUB1GtLg0O5hxLflVdY71_iqzsKoHotHDX0GrrNQgGTg9oMBvOcBrx-p4uDQoL_OOdSQCm-KcK3VK9hQLdH9bCKu4Y1OdtAkAusQuMv8CRHM8-ODW2ovx9gKJVEVpHr4Yp82NllUZU7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddb338012.mp4?token=KmGxd5d6sUwfxZSeSnAUmiD9C3mjSGJbC9EeRuCK5oGU6XgN7F5fP4CKv038f4mNhC_nvteA4isZBiASUXeGmd5Dex2046n9Qvu6v1ocNznvJB-7GQSFLCHAHMOSPpe-w-QulRBKO-q0xTfKlhtAhjkwhIBfJssTcWj3UsYCqqN0bqFjuMq37EB-MwRyqe9V81fjO_do5ItUB1GtLg0O5hxLflVdY71_iqzsKoHotHDX0GrrNQgGTg9oMBvOcBrx-p4uDQoL_OOdSQCm-KcK3VK9hQLdH9bCKu4Y1OdtAkAusQuMv8CRHM8-ODW2ovx9gKJVEVpHr4Yp82NllUZU7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس جدید دکی به زنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79473" target="_blank">📅 17:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=QxpzEQ21HRbcT6XRweda9K5pBaWLV5uFKxkN-yyvOCu501FVG9abnZ-QN1UR1zx7qUQkBhd7E4dVu4gPHLvugzp3bvrnU3qNhA78t0tshS4hasFaB3elxZqk1nil1JKrWH8brqDrSzrQfWv5p_Xx_VTiEDlKbPZIWmr4fKPLLRKCxyM2kX6LOehpgaBMmkGFZkQCJWlYYQuvyTb8qoK9vH9Rfk_XmivS99onLerAtKzBBVcqUTHJvzWDoGgK_H0o6chdwa1kT7_WgPc6dACQnU3ezODD7gUMzn9Ix74uC6z_pGl3MUW1QCtpCy7ae9B13sRmN6pS2AAaSC0Ioh8YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=QxpzEQ21HRbcT6XRweda9K5pBaWLV5uFKxkN-yyvOCu501FVG9abnZ-QN1UR1zx7qUQkBhd7E4dVu4gPHLvugzp3bvrnU3qNhA78t0tshS4hasFaB3elxZqk1nil1JKrWH8brqDrSzrQfWv5p_Xx_VTiEDlKbPZIWmr4fKPLLRKCxyM2kX6LOehpgaBMmkGFZkQCJWlYYQuvyTb8qoK9vH9Rfk_XmivS99onLerAtKzBBVcqUTHJvzWDoGgK_H0o6chdwa1kT7_WgPc6dACQnU3ezODD7gUMzn9Ix74uC6z_pGl3MUW1QCtpCy7ae9B13sRmN6pS2AAaSC0Ioh8YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیر دیگه حرومزاده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79472" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز روز جهانی بوسه نمیدونم چیچی آمیزه، به همین مناسبت روز دختر مبارک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79471" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مندز و یامال کدوم سگین، امشب رقابت پدری با ویتینیا و نوسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79470" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6FBNWKyvppr7fy5Jafb40n331fXN3zFdrCvMnAy8rO2V_0_y2MDY2VhiiNt8VvmF4j_PMu5SEm9W1iJaMGEHmrNXaOJpB3ClxbwgEnXvW3dvDDGLWUqvkbquqOuLiPAqyo1bbqzAr_y--fgDak_wKjT84sPkfC9pVX6POANiOqzXv04TaEi8AoCETXI7cjYECrhDl1q0v_MlCCKkLLGehkjk3zrodKUdHYMH2h3BICPme_ad9h0rXjZME2YszwmsrkdVzmZaTvv4s3CdwT6zgtt9DMu9uFXSgRicT4PKrCucE8wdTCh4r-YNz_N-py0GQf7oY5qLxvZidlEBqwlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مناسبت ۲۰ تومن بکش رو بدهی دکی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79469" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCoNdpH5W2rs2dCrVHPASvCCBtHd-cwiAJ5AV97flKwWQBVxFpdyN1qjDRjxRAWi1LvCFncF1ognpeFlGv8VQgoAJOlnZ0IWeiKM_L3zqudwkHKx7xiefUaFuy_Jq_8O19AUtlDFs_-BfMPi28DVOFKtp4ZAbVUyxZtZfyXfO8gsl594sFBAhhinY69STK4HZo578LaygLcBhwVKJdlSLYqUuoTifVUsv5NR5BBNkHntGt8P4Paz3SvRfqKpdBuCU1PElPnWFz6rEBlo0uL-uFED9T23qjObOHYZnpB-WztMFacwVlkDUH-aJ9Ch3OSdcgIZeBNDcBmfHOBN0QCYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگ گنگ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79468" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqSPjUkkJliyClbobFEtwbPxbs5we8a9QxVk64CSRgBV00W2u3G8orW3XsW6kFjZLp4xWYd1wbHGDCVXnXgfW1Htm0acP7Xn46eNHW80nRUwrufQ4yWG0jbdnlYTPJatne9f5Cak4sFB-qyaH_lZ3JgT9AG1eg3UxD_UkZw-NHCEPqRbzWMzRTBFuJNhZdqLSWTCF-j6ootDPFg1gYX27u4uDn4nfMn-t6TKaRNbEhFD2YemPI4Yk2U5st-xGtSA3tEidJRnKeW7s_woWSDG41YGS8CYgAE9bVqZaLpNXyBA6RhaTnGQgoF1KyS1tnansxiNWw8PU583jAlRFgPDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام مجتبی بالاخره رویت شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79467" target="_blank">📅 13:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79465" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صبح امروز اسرائیل در طی یک بازی تدارکاتی دوستانه با دولت لبنان، حملاتی به مواضع حزب الله در جنوب لبنان انجام داد، این بازی با نتیجه یک بر صفر به نفع اسرائیل به پایان رسید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79464" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لاپورتا کصخل کینو بیار برا دو سه سال پولدار که شدی برو سراغ هالند</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79463" target="_blank">📅 13:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop | Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79462" target="_blank">📅 12:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGR0lOkS3jnTJFcAow4BroXvsDtT_fl8qC0ToqpZOTKiCw9erQK5juo69SE2RdGkjReUe-rLMOItznkvk2cifV8mcP88BmcIiGNf1iwZErc0z6mAYpA30llLugPDV6P64oEPML7FSuacUTDNy2mP3qoHKqi63xbGHdclp1ECfhZRbntssMV70qepqhYj6IwRyPQO_YLAEtGmenXOkp3MTXo4RZ8pgdeI7-dC7xretnPeTG0S4sVxkqH5zIIcfcFZe9-SPZf2Ovb8C9fagrzaKcF3v1nxlKjEHMs77mE_r46Y86oUGNPWuuMH7ymKNW-sH9CdTJeXN3-zDsHafUUdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/79461" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میدونستید وایکینگا تورک بودن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79460" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حس میکنم نروژ انگلیس هم میبره</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79459" target="_blank">📅 12:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJG1nLeAK8-lsrrehtsXM2NasxJXNOW_lKoEDPQiqzl48HKe2IAaK0OjYR39-yr6XfmY4xuHEfVS_NE8gQIDj3U6h4iZu1H2cd7JmZcAKmVYO71UBV86W3MUuwy9CnSbHYD3CSeI12s4_yqeBnFUn6FHNPNisE3VNpTkSw5kBougTbjL6zf4NkqsjK_8n96FXWwGUUdUvF7crpdAsQj1T8onQ6sKOr4JZIpzBvxda_oNILvMDcengmpI93voErym_ak-y98QASJY4tqR_wfHR3_eIWiYu5q8R6ZxpEHkEHZ7Ops0L6wcxxOt7TfrNBbqnvTd_MNmbqpIUonAmXeNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lI4Li1KERHgn36iEyT70kA8ZmXeO1INSSM1SR9tIFoOfc11ubC5L8hhR2nlNhNFgEzJFAoM7lcF6dph0fkLVl-KA_mcjyxybUhe8PS48vchipt7gwUDjsuB9QcwGGEA6zpcEM_6KCZmACmDO-cXHzgN2BxHo8MFlbHowTopjvC5rzMwDvQ0vVBWLmHbp6yjgR7VgDA2BrCDNRx8sfhfM9msZtcCxqH3qIyw1pE9F5nexHtHEMEb2cawE6zl9vvRDTiCBaOVmy--ci6xWAFHIH5UWWNODUKyYsX0CZtUEslUe6mEPV6XT6K9JjymDbruQFMAsJgn4Tn_6Fcm-7a5Cpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا این حساب نیست نروژ دیشب 12 نفره بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79457" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOI_aWzfy8zkPQY0YUN1SBu6hrEmGYnaQU1gLpk53Zhzwxl32CdwNjmUY91FdL6bJdyY-vWrGELHLlEuCep6g9i133i5AfmjO3Ee6ApNRGC8vD810ttB1HjIuMxDQ3o5rHy3C6GOYuL4yo_6npCTqGf81Eb1fmqvCkElLT3czkV7gtLekHlw_lOIDt0YQqwBcJOWI8C9Qx9KXzUc8HUD7LsMEqj0t8q8tMim-iCCUaQYLPDhWExKe-i4OgUmVjV34d6EaUH1788ok4Dm0LvdWZYoNI0MMXT7P8-4D2yuiBU-uU1uhiF1UlsZhM7b81-lKtSxWL0DgYkcMrydclWHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ ورد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVoHGFHaDZppkGPxzNeW3Hu4GlLYTWg6rk_jK2hDW4fK0Pss8zQprH7_B57vah1Rn_8mAtH0fkwF0XQGxEUfYfA8XsHCv16TeQvHw6Aq0VjnAcq241KbtPBx2yeiV3qoJYIj4BGlW2GFZ9T0cDfDdtgOpVqytjGD9Bos76rxCvjUH9VzXsc3J0inZZ1W8XB5P0CL1AKZdZ0FaWDJo7qjH5WptG5xMs2oWg5byuc_E6w4UsAvSBQNT7ry0UjqhkEjmWv3Kgn9EFEjtzQ5jibV43bTMjfvIVE53e9zy4TvRsEyK5NDUxA_djvuvBijczASOI7WVA6UKJLV6Zhg1LpnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79455" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چه بازی بشه بازی رده‌بندی فرانسه نروژ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عجب بازی شده انگلیس و مکزیک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79453" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE2dkaafq0_xZGeIBRYOUXZchfd4XnDU4yyIh_j1myPfwL7O0mCPK7f3e95UYfNWx1R1VUIAeVnzS5PyHB1d5GsRhyfHZY7Cwyqjb7-V6cFPUZWOtIW7IpDoQbrJnvKmj7eZWgk9IqZ80K7Aw1bnDRo3Zf-CFAebG3Yw_-AXXyURqqySkj9vwmD5A5bWjWUqGr_ThzWtoYuAs9HbLWnY9jjEANVT7Xlnoo35wDIA_D0CXVJWRys5fZBE4aY7scScKddCfOkQ2CzD_5bcjZlaUQyoh4Gnr4dOfnf5umAptlE1i4CWFH7rLQs7Ux39z0h9cAB-561hZ5HJ5sc2u6S-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا تو امشب نباختی، ۸ سال پیش باختی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79451" target="_blank">📅 03:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استوری جدید علی آقا دایی خطاب به کارلتو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/79450" target="_blank">📅 03:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONvL1CigMk5JUa-38YivW9d4t7mBoD6GXNdnpUgQZVFIgNDHm2kKd7Fl9DxsuggJsAVTYslkB9T8POcj0FfGR-aYvAhfkBb4UBQ7Jo5nC-pGbCptgE8JW1fafKV_uSS7Osn0edFs4YweEDlSIB8BVKn3LwlQajr7Vj9cOZd_bc6k_cDe4QGBCerNGr_86k1vZUUKYfSGykPGshms-ilSPjyiTluA1rDoajnMGWW-_gdvwL8a-oS-8s9qh3CwdgbjqLHm3FN3B4sVIeOLg-eN6A9_8QeUAEuuU2v1cp0_htpi14_tqCj-P4g_G0yoYd-1OOy31FBhCoTbbZ-E6sAGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79449" target="_blank">📅 02:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هالند وقتی تو سیتی بازی میکنه، بین بهتریناس و جلو هر تیمی که بازی کنن دست بالاتر رو دارن تقریبا، ولی تو نروژ این شرایط رو نداشته هیچوقت و همیشه بار تیم به دوش خودش بوده، دلیل این که قدر موقعیتش هاش رو میدونه هم سر همینه حس میکنم چون میدونه که جز خودش کسی نیست که جور اشتباهاتشو بکشه و ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79448" target="_blank">📅 02:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79447" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EILHAE806wlLgQRZNjVBrQBEzzlF-HuoflFvb_gtKROcu4jsJDtoeQtwy73uvtaY9F-Ve0AwzaEGKxMBmXjI820zXgU6ys_2fBGxxSIUAqs6NQx6UflOiNderykbu9y33py5g4EYwkOx4tcDL3Nd8uJgzf6NoRu6SvYd0S4MSRNPweToFfeJ8UZyEEc3_qi2DPTDTX3MNF1DfXlxWnURe4TlsibSKrXljvLhxkuGTO2ICJ158luAs4Btyf9rro-PLkCtFVUtnlGfAi0i4iWK0Cy9Ubn9qDgwA9I-6tMNnrKD2OFhCd-un5X_5CVT1qKycKRhYqpCQFR_GU6FM918TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اندریک وقتی یک تنه رید به امید مردم یک کشور
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79446" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بازم چیزی از ارزش های نداشته‌ی نیمار کم نشد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79445" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیمار کصخل تیمت وقت نداره وایمیستی اونجا میخندی و کری میخونی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79444" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2q4iDe0-jn4m1Yb0wyTles9MCwBOrJhmnOlAoOWoZ3zf9iq1g2mDztUxcDoODM270pVEJuiuz1n65z9HPXqGc1ab9mG-MapliOpp2teO5UmL29tpepWnyIr5RDBofW2l4tAEuNGmxBkp2o9nIqHS4FobTt1pby-Wz4Hy5UoIN9lQ-nRdLTpVswr1O_QfRboVGpgdq9NKTfKgbuhL9p1sTY5r3yQJxOjM9iU7qckEUfvpi0j5FviU5j0-KIylYqz-coGVBIeohuEEFQdxj1H5B956mq8gBZX2E3LXTqFyld0ru-fTJ0D0z92syL4alKR0w8Tvpa75omZ9wjVwz404g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم هالند هم رفت تو لیست برترین گلزن های این تورنمت کنار امباپه و پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79441" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ریدم هالند دبل</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79439" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وینیسیوس
😂
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79438" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مهاجم خوب اینطوری کار رو در میاره
هالند تک موقعیت رو گل کرد اونور بازیکن های برزیل انواع و اقسام موقعیت های عالی رو به باد دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79437" target="_blank">📅 01:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیمار، شاهزاده فوتبال جهان که متاسفانه پادشاه نشد به بازی اومد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79434" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کارلتو این سبک کصشرشو تو تیم ملی برزیل هم اورده</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79429" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انگلیس به این فکر کرده که بعد بردن مکزیک چطوری قراره از مکزیک خارج بشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79428" target="_blank">📅 23:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رضا پهلوی یا مجتبی خامنه
❌
رضا پهلوی و مجتبی خامنه ای
✅
بیایید از آخرا فوتبالشون لذت ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/79427" target="_blank">📅 22:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDYes-2aXS8MbWSnSgH31qZakuszNi-FRIC3TcfdUXfMBtI-8How9uQkeGSDa_KRA3A75px_3I57U-x9VWYxaOOsYlD8J2p3oObuz31Nv-q35_GYWZrsQmZjTLCeB5PkbxoMMhR61KCn5FSknCr3GyoCE2QMmfR7pguYC347f9C-QsMzN6ASsZDeGA5nWIdZXBbNeteHDn8NWF-oGWcBHba4jNaJ1DG6geiuPIUuxu0fKCS9qPABDk1rMkNxZVk9AuzGK_ET-9g3DngZFPJdQcx0hdqMOb2SBd7oHJ3bOL9ze4klIgsScLuu6YHmcgW_5igLyxFj-BpGdUT2RPsAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراماها توی ایکس از فان هیپ هاپ هم خنده دار ترن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79426" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQSCMCiHqLVx1-vdZrAff1MjqMHxR35FmymgzA7VeKCZEfJ_gQUVhlu-MWERwXcTh30hfm4RVM8IbAdSTCcHPEelVSeDcTJyVhYyoWBte-yzXm6W-JB7eQVHJI2b5gTk4fvqD1Ut8jroEucAbk2Vd-Tc38mu8VC-XfxJTuybBXsIlTvqWWd8H1uexJBvwl7CsisDGNrPQMtEzpsRFH98JT1JYj1OcqZzNkb319vnVPYjJeqtmjiDF14363eRINtY04IWkjvI-faer_q0wIcehQ4KCCzd3JqB-0ByVWTVpAu8-QseAo3MzsG4ztMbnrtlYxnI1moMiJdimor-yqpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا،تو بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79425" target="_blank">📅 21:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بدنسازا شروع کردن به خوردن کِرم، چون تو هر ۱۰۰ گرمش ۵۰ گرم پروتئین داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79424" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi1z2w3LZPNTCff1iKA-A0wn_OcL-yUNS2wF6lSNjon445a0orxCHHhm3afJDWf_UP8guvnHUp47yE_2WoiJLx3K6AEtb2qIpaDLnffqBIeeMLbf8Nbo3hdIkFtswZCOx2tuQjkBZQBlfkFIt9hUugfgDo5PuoD3xt95lb4ziA2d2cKedUod65ouIG9LV2ldnEI3RNPqqrMWrAVSWoBwIBbQYlc_n6xyT3mAoJu3uMPrIErOQo6-AeYqH-ekmZ8G5Ksp62uRilJHa_CzJcHsNdNsx8TgOPqfjqZJY3_ncDcyVcGv5XJU0jiLyzCd7me8-u0Gt5ysjDrdhCQRMe-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بعضی مراحل GTA6 باید برا لوسیا مانیکور و پدیکور انجام بدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79423" target="_blank">📅 19:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79422" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه یامال جای اسپانیا مراکش رو انتخاب میکرد واقعا تیم سوپری میشدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79421" target="_blank">📅 19:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Du biat guta guuung
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79420" target="_blank">📅 19:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzQp5DrknU7TbBwBJ2myJDKZih-CbqQSGRNbd7bG7VzEoFOof7oCT7zRepzSpE7Au0oJNapTMundw5-7j6lmpXxbPRkcDg6fK-FvR_-V6XZNsg980V0y8TNSWGuDKF_TvoTqwcOFAMTFy66nBbMPfc6jMUORLOxTj3tWlcLGOfvUt9BmLsXd3mGVHanrhJeZHYpnaRod6Yr1VNwq_ZlFHBBXGfpjVmZ49b0SI0nRreOBirLZcYw0A3eDQQDG0L3nfvFSVvEBKtLYWZOKZRxWB7zWMZHJxGJNpbLntpWXmzAewf9Az41UrPgkwUuGD2FYWql7Hp3LChgwEhLVqkHwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79419" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBbCOlsY_f17V7sDexGRCDZrQ7gesS1MwKAvcpF896hlkB8m3DEqCOLdjDqCSG6JwfbsTmUzBYYrz9G-TXOLnbDs_liUBef-83WmJN0ZaZ3LtcmpPkFtG0JmeONiSXanaklg_oRy7L-ey4IVH9r9wgcV_ZhboEaS-I4MkTW6eIbVAL_-NrQ8RJgyNdIm2Wt4C0dgJyxvJ-YsvViaqiCh8YX_ex2QN4K52haJIPFgicTh8bTjm8o1qfKlDUItz72-93QFE4BRk6wiBiojEo88O_jAiSBA3qfH4CFbJfQ1Mt0k7VA0v_HJStc4Z86CVe8N0sk6JU6Wp1DIH7j-9T8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین تهی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79418" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MketcFZKIEYbjyBnvJhlL8Vnuyn-4jzwk0Qc1BovxAzuipp6Z68CRZQAL2p5R9c-TvNvB2zegWV6bJn31m6M_G7dnsaGCa5rWbXkhA6D9juq35TEuD8xs5PfesYD4dWIp3ibbMc36NODYNc4K-UPkg254uuUiwt3ONxZJuwlGuzgsxzeFwr3jFk72gEgiRbbjpC6fk3R_SyX6CPL-q1men08ncVOmGCv3Sv0vCJN-dJhNxNMroX_mQ4NCvh6dHuWyZhNNp7W5bub55gSsYCsAgdRyxLHGrVX0gdwGeYy6PqOxKYQ5UFMIfbSHBVX1CWAnSlSUfQv_WEe5mjpyF2jeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJnmgGMKBXI8W1IUvNqxLf5d6HVTfzqy0ZJyFe4hbIcEzy3vTPog93pnf6uEROQuZs0Fo0p7JZmLFjQvgBQ0p-xutIUth2OQIYa_2pUWuU65wIttZ1z1Il9Pby4GUIh0GNcsnKxtFBAsp37fwLI3LBYJsIw6ETcma68Fh16GeFx-aP2aso1-hH3mWvdLrsd1ON2goiGzCIx8Iq8Scc09-UjN6q1TpwWBrFUrAdDubShiB-auhvGbBtFG0HqG2F8qfmTWZ_aG3CVk36piZpAhTv9yRr_Fqa603ed4Y_9EnKrr2tpUJWuK0yaxTLNoToJ4I2ej416qb16-vPEUeC0DwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت جدید ووزینا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79416" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
