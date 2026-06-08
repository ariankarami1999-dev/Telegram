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
<img src="https://cdn4.telesco.pe/file/kMA480aO3f68fndHC4hfG6R_FWf5dLBG8Gc3gO4v6jfzcDIhmnQWE4Hb3HdGdWwuXe-NLIsP8dO8zJ2yY07hL8dvPOgFsHTQMcYR86goavRIV4yZEdxbV4b3c1BZKPuYERw7PlZ1-TEYoXFc6rHOpx8KE6EhFB1QYfQVQMrlE0-vKYaQmjsIm0FooRTTuMzsws5dEvkTgUhX9VCqpZu2VFNV8ZtktZKsTmOyPgR8lsC9rjB7sPY7Q8s_o5gdkjF8DDj3vtu9hhHNs53rH_1BFJftUEtTYobIxlGoXH55tAWy_8npmAdarsrfjuo6DoHTRhxRCg7Gcud9kPWnySH9WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-440777">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
قالیباف: قرار نیست یا فقط جنگ کنیم و یا فقط مذاکره؛ بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/farsna/440777" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440776">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
قالیباف: پیشرفت مذاکرات در کنار انجام عملیات‌های نظامی در خلیج فارس و موشک‌باران دیشب رژیم صهیونیستی نشان داد که ما باید درک کاملی از هندسهٔ میدان مبارزه داشته باشیم
🔹
ماجرای لبنان ثابت کرد که میدان دیپلماسی در کنار میدان نظامی می‌تواند دشمنان را عقب براند.…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/440776" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440775">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
قالیباف: اگر دیپلماسی را صرفا گفت‌وگو در اتاق‌های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می‌خوریم
🔹
از طرف دیگر، اگر صرفاً به عملیات‌های نظامی و جنگ تکیه کنیم نیز نمی‌توانیم از حقوق خود به‌طور کامل دفاع کنیم. @Farsna</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/440775" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440774">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
قالیباف: صحبت‌های رئیس‌جمهور آمریکا دربارهٔ یادداشت تفاهم، مخالف بخش‌های توافق شده بود که نشان داد آن‌ها نه دنبال آتش‌بس هستند و نه دنبال گفت‌وگو
🔹
باید برای دفاع از حقوق ملت ایران پاسخ قاطع می‌دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/440774" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
قالیباف: ما نه می‌خواهیم با وادادگی پیش برویم و نه با شعارزدگی بلکه باید با اقتدار و عقلانیت ایرانی به‌دنبال یک پیروزی مهندسی شده باشیم. @Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/440773" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
قالیباف: هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی با آمریکا
🔹
به مردم عزیز اطمینان می دهم که با قدرت از حقوق مردم ایران دفاع می کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/440772" target="_blank">📅 21:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
قالیباف: نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند. @Farsna</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/440771" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7701fd0c2d.mp4?token=HJaRMvq-fFYTDtmhFmwC598fQuATXycLU57XeUcULx8et0rBHzZzlEcgg_9ElLvNG6i7YhmJ6lMfL0nUClPBkIuKLWfDobIjX8anCpGMR1kTkwjywPz9mdJp8D6CQmhg5sT7-FEdaw60CLRic2y1B05udZwp-rn5f1EphRnu4hOwWINeFd37uZURxrG338hevP2aOuEy_3TJ4hBjPNmDw1PJnJxysZ4iPOdsoHzzdyxEDhSnowxGpXJibFOzHyGtMdnzagcZPYtBtAX8i9j85uzTsC2m2s9dLpf8ByXZ5KH-cL2IBLBmFF8DV3oRqq0eENNkvGrQIAJDVAuV8VPwBaII4OqgtpBzRT_RGObuSN5zgMfRHsdvrMgx_z9Gz3p006xqKHWKZ9G8xpvpw2FMxIWiLKWxuTw_jmkVSEfYZnWMy0to52UG-lD62HWO4mO0BbLfTNk0HklW3E_c33-vQ08pfYNabyf6cVcTrhx3gSlkypRhuLOPx-00I8eOnof7WNKXGptPprtpv5TeOsSJ3CYUmZdXKXUqet-yMjNz3Yw4G_a1px0suoVakARmwYxg5Nq-1E9sHciOQUeZTIOliU0kYVKiWIadRn--EzyjT7PezPd9wx9wRaQzRT0y6x66CjQJD28ntL-pVGtsoX0LkYJzWjhVcAutlIiEwGCBnO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7701fd0c2d.mp4?token=HJaRMvq-fFYTDtmhFmwC598fQuATXycLU57XeUcULx8et0rBHzZzlEcgg_9ElLvNG6i7YhmJ6lMfL0nUClPBkIuKLWfDobIjX8anCpGMR1kTkwjywPz9mdJp8D6CQmhg5sT7-FEdaw60CLRic2y1B05udZwp-rn5f1EphRnu4hOwWINeFd37uZURxrG338hevP2aOuEy_3TJ4hBjPNmDw1PJnJxysZ4iPOdsoHzzdyxEDhSnowxGpXJibFOzHyGtMdnzagcZPYtBtAX8i9j85uzTsC2m2s9dLpf8ByXZ5KH-cL2IBLBmFF8DV3oRqq0eENNkvGrQIAJDVAuV8VPwBaII4OqgtpBzRT_RGObuSN5zgMfRHsdvrMgx_z9Gz3p006xqKHWKZ9G8xpvpw2FMxIWiLKWxuTw_jmkVSEfYZnWMy0to52UG-lD62HWO4mO0BbLfTNk0HklW3E_c33-vQ08pfYNabyf6cVcTrhx3gSlkypRhuLOPx-00I8eOnof7WNKXGptPprtpv5TeOsSJ3CYUmZdXKXUqet-yMjNz3Yw4G_a1px0suoVakARmwYxg5Nq-1E9sHciOQUeZTIOliU0kYVKiWIadRn--EzyjT7PezPd9wx9wRaQzRT0y6x66CjQJD28ntL-pVGtsoX0LkYJzWjhVcAutlIiEwGCBnO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشرفته‌ترین سامانه‌ها هم نتوانستند مانع اصابت موشک‌های ایران شوند
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/440770" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود.  @Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/440769" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/440768" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW9ezrNIjojpcE9EqTd92KkTS8LNR6x-ZfXShx_TfzSOUMo95uWSEEPVqT1ERmjZYCymLwAHbMO_Ok4B43RTQ5v5NeUeiV5BeW_jouSgu7HDFtLOkMznARb11om3kgliY_h56IVh1t6YofwbQfXP5YmEWgvMCt-sx1wFehESoMRtmY3KFGEsSHP_HRZfL_GfX1hqo844mNSnjQPR2mW6MOi-HpLtbwvFEHxO3ThgV5c6-1QDKm1e_ZQ2LVrMlxEGicP2vzp0QpHpuX8YjhYTGRxSlG8GVzV4174tx_IqmNgOmjx2M9-y69dP0V0L9MR87XYES-gOJe1qXlO9Ir5gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست بزرگ در پروژهٔ نظامی اروپا
🔹
پروژهٔ مشترک ۱۰۰ میلیارد یورویی آلمان و فرانسه برای ساخت جنگندهٔ نسل ششم، پس از ماه‌ها اختلاف بر سر تقسیم کار و حقوق مالکیت فکری، رسماً متوقف شد.
🔹
این جنگنده قرار بود از سال ۲۰۴۰ جایگزین «رافال» و «یوروفایتر» و به نماد استقلال دفاعی اروپا تبدیل شود. با این حال، اختلاف میان شرکت‌های «داسو» و «ایرباس» باعث فروپاشی هستهٔ اصلی این طرح شد.
🔹
هرچند بخش‌هایی از این برنامه مانند توسعه «ابر رزمی» و سامانه‌های هماهنگی پهپادها ادامه خواهد یافت، اما تحلیلگران توقف پروژهٔ جنگنده را یک شکست تاریخی برای همکاری دفاعی اروپا و آرمان خودکفایی نظامی این قاره توصیف می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/440767" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncmoM78rfx0tXGuZTZqRepETuOiReW630R4V7pWMRlfA5VEgjhfHccDUvvGK1FXkkINFF3QWqfiule60TjDPJ-zai92B5eQB18DbzH-Ah8jpzeuShMCtOXfdTL-Tg4DpHuo0hfbCSI_IjPgyjdtD_CIFqLE6LzSxFbJeYHW_NLdYfeBtn86A61AlzghYM_zq_Ha8ZQnhuZK3lJ4obWqoZgN9rjs65RqM0xm-KJn4j2RLPfTxmJDKT1sblmzyVB9uPxlvkctv9uQDnVz3LRAuclJo0roQeji_UnZVYHP7IaBfkHiO0Q5oDYDiB93ns6OcOSVXoCDi2AwjTmkFC2Atqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMWETf9Jpx8kFbZlxOmZJ4ZnKiHm4k3gO_gp-MlEOovi7ZpEaWARRw3mr9jK8vTNex8ZVWcFoww9NhoFnowYzd0aUxNw3EQ3WyP0NpM2HzDdkRhX6O981Q1VW_zuAIOIsOIQTWffpzQmhTTR6HKymmmgeTfcPFOR8sRWYCjtv-O161Y7EOmS3WKqH820BrZEhXoIYJB87n0b8I-qBDBiNZ5jc-utqpYiqZ4Rt_z53Nsy-bYCwxQjZWlKGc42IMPuDJDiFJD1FafIEtSgZaTLKloXA6AMrSdz-bICGwKG4KO4qTQf7XN9qIZGr_msf0VfLq3cZ8N1qp8FX4sqwqlnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUvKXNKdTJi-fJoR4NS2uwuwRDA2LSFKzujxjpOqx46i-G2o2pHvq64KnFAHnLE1wuqzKMcBmPDrCUIpA0Q_2ZoZ1kgyfIDoz1IVgswnrvtAxe-5MtgAcGPtD-s8GCWQ87IxOTvba8Caj1EI-EZGK6sTo908iXWj0S_opUKvvb0xXL2gkb4YQCMMAB8Gf5JyJfQU9JE567ZP-JYztUG6aFopf5UDIzJJ6EuD3swLKwlmbhBP_ESTJ1FN__uHiV8QHrIh2vDzKvMGob28wIVrEPkomY7AfJO_JC3rc9QXmpKMsz7Hmix41VZSNMs1SFFzVGHB6giVUR7rLOg2Hj7S2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-JIHsNE5Bbw1wDiYQKR2iRfLrcok7ms40ulYLuOurt13LWTZoT5Y_ESDIxfMcqnF8pQMlZxAKyGfQ-G18hXRIt_FHVU2xMjy9leRdiRyMtl79zAh1z5jcN_9UjQG8HiBxukdf9QtPPwx_9tiqr4hT0BaPyQh7rF4AQ9NtJKi8NrHZQ1EFemV4lTQIJYGk3Cr8laq3kHbHkrPm2PpXW20jkNF20_HTts7_gBrBJAa9A5zZy01WbXKF8SaRkYAA6Z0q9uIz2XEx6zevgrhcUcJ3pwjZsBmhdYBEUOOtasr6DK3uElugau_qHkHRKecUP5wJs4Du0MYU0aBkfesHUIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uctiMVVngr71-VLRiSj9v7_t-TfkdMEgumzVBr6XJ3eyedoOBfn6pV9eU44LULYWap7shA8_H08vQXNs_9c0X-0GdhhNQY6ON7t_XsqocMEFrzUJRdXwMFmH-e08bppU-xbrbfg83Qg-KHAoXMEZVlsOaNsm3ODAc5NXBPGmbTsce4qCnkQo_r7K_pdxfxXvZsPaXtTOt-c1BDuQ5MOmZX6JKnuAEIKQt3CJjK9fVepe4l5YAMME1bIg4-ksgvm3RFP7aaOnMR8U8VxMwmQGqMaFpWe_IDer_XbslgjI2FuskclX01Y_A6nUi8TXum1sOKvhkD_i0ejSsDdVW0YrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IuyHb4NjK6oYBXlsklxzE4hq7U8zkHjcIUSJ5dBUIeROgVrRT7u4beGxp_ntqciEoJwZM92cn3RUEFbskMgaHg1b9YqBixxtzeb8Jr1Mpvfc_mvUOPe9rlGa9_brfUtLjylY6jHOfLyRz4GNyuEmZ2_GqwDVr_cE_2rpVw65ia9LJ-2zOw4ztelfymWMLI-DhajzEl3Wbje9lNytCK6RJSviwTl8tkJDW-wP-ztCZbsMsLy1Xz6jsc1l6L2gZXKEZND3NPTbYgxkq4V4Xw1-o4KP3kiEcdcHslqZHv2U-PRmzeNNVEhsowKUWFqpac139DlubeBP6W8p4KUd5cqJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moz519lcwLxoFhuWyUFWtcTCTcWTVUbEzVlOQzt0qaeN88qr-rzxqJukroD2UNR_dwzAwn0y-CjJNc6KvN_TH6pxi2gyJn11NNCsK2QDhGURPDhsgRzqg90PtnZnHOenNhzyjhgxNuX9pEWRytRWyxTQVvV2ie0s-f7WvZwBDplhNdS64XIsQA-GQ_1BRq_vE-sSTe0a2H1BpDt0m9a4L7uARLsIu9_IxDpZqT72kH-2Ds_aDYotTGVmpcisnevfN0HkSc2BRlI0jGU5aZyJAng4wc7f94YpJLp3-h51WKSgJsy8f1cd77mi1TmAB-VbRbOOSFhizdJTOhNaExIa0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: جام جهانی قطر بسیار منظم برگزار شد اما حالا به‌خاطر اقدامات آمریکا با یکی از سیاست‌زده‌ترین رویدادهای ورزشی مواجهیم
🔹
از مکزیک بابت میزبانی از تیم ملی فوتبال ایران متشکریم؛ اما تیم ایران هم باید مثل تیم‌های دیگر بدون تبعیض، فشار و استرس…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/440760" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIwCe4FvR5vnJBdZ7BzJjKLIaAYnuMe7ZPeDRko8XbLAJPUgdgmcwaaBaJ8UrFOWmmGtNwHVYqM3ULhUEKAzXuDfFUsZ6AeyKCPR4lZzq5wqOO8qfnL0nCJ81lu-7kbxNS3WL9NE8QM1NlEuhSwoK9gt7S92rdBxktfCbwmBYttUDdG_79VSsf2eVA-4VAtmtrmq6wt3DH4bc_xGsmKs9nNYzNyBIDrABzQuxbZ1EqitaQQlLYR0SqnsjGbm-oo_u_veoWVnn4qn3cYBAkco03gpVxYzAEjoyb0UvZIKSoB9BLjqM_0OLncF-vHoDoIWoBcFS689BczfjWPmSI4RuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
موشک‌های ایرانی به کدام نقاط اراضی اشغالی خوردند
@Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/440759" target="_blank">📅 20:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هشدار روسیه به شهروندانش دربارهٔ سفر به اراضی اشغالی
🔹
سفارت روسیه در تل‌آویو برای شهروندان خود هشدار سفر صادر کرد و از آن‌ها خواست که به اراضی اشغالی سفر نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/440758" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440757">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسرائیل هیوم: آمریکا در حملۀ اسرائیل به ایران مشارکت داشته است
🔹
روزنامۀ صهیونیستی «اسرائیل هیوم» گزارش داد که آمریکا برخلاف برخی گزارش‌های رسانه‌ای، در جریان حملات اسرائیل به ایران و همچنین مقابله با حملات موشکی ایران به اسرائیل نقش پشتیبانی ایفا کرده است.
🔹
پیش‌تر شبکه CBS گزارش داده بود که ارتش آمریکا در حملات اولیه اسرائیل به ایران پس از آتش‌بس مشارکت نداشته و واشنگتن نیز دستوری برای دفاع از اسرائیل در برابر موشک‌های ایرانی صادر نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/440757" target="_blank">📅 20:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH9OWzjCU904yR12daVytAoato2ARQvAmYKQPU_yuGwriiUt8Vx_NEaxzS5wLHiuRqV9b-DVwez2i-iL-MlIrNDI8BgPoE9zqOrC247Cug2JPOap-RQd8_xd2xu2yDNktDioJcIzks4tS-vkHGlrMp3UYH4qL1hBBKI9SB4YNeiRtsu9FkJ58ej_fBpf1NG6rkiG33plM7u71sCsvFA6NQ2jYH02RnmaN0GDbIWtDAdVrLhoBHFFUTzvUooNT4sVYF0yxLZRBDIs11_vjNQi4QnpyvvUfyb04Xsyk48fJngEuxHs5yiIMRaXWmjyHhVqdgR7EfFJI8vJeEDkwZAdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سوپر ال‌نینو» امسال برای ایران بارش می‌آورد؟
🔹
مهدی زارع، پژوهشگر حوزۀ مخاطرات طبیعی: پدیدۀ «سوپر ال‌نینو» ممکن است اواخر پاییز و آذرماه امسال، شرایط بارشی متفاوتی را برای ایران رقم بزند.
🔹
براساس الگوهای تاریخی، سامانه‌های بارشی سودانی و مدیترانه‌ای همزمان با این پدیده می‌توانند موجب افزایش بارش‌ها در کشور شوند.
🔹
«سوپر ال‌نینو» یکی از قوی‌ترین نوسانات اقلیمی جهان است که با تغییر الگوهای دمایی و جریانات اقیانوس آرام، بر وضعیت آب‌وهوایی مناطق مختلف تأثیر می‌گذارد.
🔹
درحالی‌که این پدیده در برخی دوره‌های تاریخی با خشکسالی‌های شدید همراه بوده، پیش‌بینی‌ها حاکی از آن است که امسال برای ایران می‌تواند به شکل افزایش بارش و حتی بارندگی‌های سنگین ظاهر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/440756" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع حادثه برای یک کشتی در دریای عمان خبر داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/440755" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G17WZFlvyFhpzlvWqBx_PLvWbbvehCGrcT0LK3gNBN2EDU00iqNI2GWB0P8gZYv_71wO9Vd2c8W3jUgcalhbdB_YNH9ty5wrRqNrsZuJsEUE6Fa5pzL8U9ikmP2wbJFp8-VHgOk7jadQqkaksylF3ubZGpVkOsIWVeW3pD_movFcDOQB7qJhf7_4GJyUqvCINixaqs81tWn_KKLUKrS6Uy5PCWCDlwuj0GHXYMo_X4mvqdSL90pJKhJxhNSwYJh-9E68ePlUQXaNaDtAtBozsPOyJlknrGMkJ0cllAGb0FmoEcdEDX0W5QEncKrQki__4Ua6WYCKlGo5T7OTH2o7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بهترین داور آفریقا را دیپورت کرد
🔹
در آستانۀ آغاز جام‌جهانی، حواشی مربوط به کارشکنی آمریکایی‌ها دربارۀ ورود برخی چهره‌ها همچنان ادامه دارد و در تازه‌ترین مورد عبدالقادر آرتان، یکی از مطرح‌ترین داوران فوتبال آفریقا، در بدو ورود به آمریکا با ممانعت مقامات مهاجرتی به ترکیه دیپورت شده است.
🔸
این اتفاق درحالی رخ‌داده که آرتان پیش‌تر در صفحه شخصی خود نسبت به کشتار مسلمانان در سومالی موضع‌گیری کرده بود.
🔸
این نخستین حاشیه مهاجرتی مرتبط با جام جهانی ۲۰۲۶ در آمریکا نیست و آمریکا پیش‌از این «ایمن حسین» مهاجم اول تیم ملی عراق را به محض ورود به آمریکا بازداشت کرده و مورد بازجویی قرار داده بود؛ همچنین طلال صلاح، عکاس عراقی هم از پوشش مسابقات منع و دیپورت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/440754" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
لغو تمامی پروازهای کشور تا اطلاع ثانوی
🔹
شرکت فرودگاه‌ها و ناوبری هوایی ایران در اطلاعیه‌ای از لغو تمامی پروازهای کشور تا اطلاع ثانوی خبر داد و از مسافران خواست که از مراجعه به فرودگاه‌ها خودداری کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/440753" target="_blank">📅 19:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGl9Tm9vM8jQFSKEtQ9EO7USmddTTS0l_cX5PBzHF4w9nWL2dPA01PJtDnqnTxW5DfNtuUaCCc-c1KmzX7vjojT_8FihFDBlFDBnJlp-_Q3nLDwziWFPvIdTZ73lPRVD-0OjHVMzfjOxCfmCHotI_YCYDG45thJhVi8TeI66IjI2wpcpax7PE45mzPZ0GXyRbmNPf6Aqeu27BqMUj9ybwRE6A1v8wgpoPqp_OcQdP8beKPdw6rVbJ9XHPn93qKUlevJqbqHirEWYLJo8PLtXupq9Kg-L431Gfbac9pAmRssPPpIADvDiK10VEeerRw2-y3nd92vI0z-XvStB4sFyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان نتانیاهو به تلاش ایران برای تحمیل معادله جدید بر اسرائیل
🔹
نخست‌وزیر رژیم صهیونیستی امروز دوشنبه با انتشار بیانیه‌ای گفت که جنگ این رژیم با جمهوری اسلامی ایران و حزب الله به پایان نرسیده است.
🔹
نتانیاهو ضمن تکرار ادعای همیشگی خود مبنی بر اینکه ایران نباید سلاح هسته‌ای داشته باشد، به شهرک‌نشینان صهیونیستی ساکن در شمال فلسطین اشغالی، وعده داد که امنیت را به این شهرک‌ها بازخواهد گرداند.
🔹
وی با بیان اینکه ایران و حزب‌الله قصد دارند معادله جدیدی علیه اسرائیل وضع کنند، مدعی شد که مسئولان رژیم اجازه تحقق این کار را نخواهند داد.
🔹
نخست‌وزیر اسرائیل پس از پاسخ کوبنده نیروهای مسلح کشورمان به جنایات این رژیم در لبنان، خبر داد که در حال حاضر، «در جبهه ایران، آتش‌بس برقرار است».
🔹
وی با بیان اینکه اگر ایران به اسرائیل حمله کند، «ما نیز با قدرت پاسخ خواهیم داد»،  مدعی شد که حزب‌الله ضعیف شده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/440752" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d899f7a8.mp4?token=SA86rtq8x97hJYw3EV-IqkOxGr6fjbaQpo7X1WQfgY4aWdxLqjAXPLrqkZjyAjyE6kdsbUPvkK8WfiSUl8_oxnKxxa_TOo-fZfuyhnz8ZT6OOqe8QdcS5dB8fFxPigs9tnmAxE04H0xb9gYPmDqrwKDsJgKr3LmdXrgqJHQ1ZKqxDt1Sir3GVyuv-XrGXi7PbFp3VdC39ehGpKH0xMhtp3beM8FpHNxNcIacruU6EkngesjlYpFsnFVc8AGCaAt3Xm54XiTiOffFvtStIvn8OBCj9JNO9EWuKyIACOsvfJVJTNdsEf2P1OKUpPWpcGxVpNR-8ZR9QRN70pCTnkV0xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d899f7a8.mp4?token=SA86rtq8x97hJYw3EV-IqkOxGr6fjbaQpo7X1WQfgY4aWdxLqjAXPLrqkZjyAjyE6kdsbUPvkK8WfiSUl8_oxnKxxa_TOo-fZfuyhnz8ZT6OOqe8QdcS5dB8fFxPigs9tnmAxE04H0xb9gYPmDqrwKDsJgKr3LmdXrgqJHQ1ZKqxDt1Sir3GVyuv-XrGXi7PbFp3VdC39ehGpKH0xMhtp3beM8FpHNxNcIacruU6EkngesjlYpFsnFVc8AGCaAt3Xm54XiTiOffFvtStIvn8OBCj9JNO9EWuKyIACOsvfJVJTNdsEf2P1OKUpPWpcGxVpNR-8ZR9QRN70pCTnkV0xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: احکام جدید مستمری بازنشستگان تامین‌اجتماعی صادر شد
🔹
حداقل رقم مستمری ۶۰ درصد افزایش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/440751" target="_blank">📅 19:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwcmBb5HpMhhv0YujyEa4supbCSyqDZeffmh8EpZcfRHQEIAh5sJQWarsj_l8ai5UfOVwVNztsP83qSUhgujqLunZlYEHJC0vO6c6XO3SjeAMO6YAnQzQPfZEV2HADf_zSdT1sJSn_rlOiZdKGwdOrLovW1pxUdYlWiPTqdPIWzy145x4upOG6xKF8ckATQl8Xn-CdJNI9_nFmOw016z-ufWLpUM9U6vihiKreQqwQcDm89pOJ86cWQ_kBQ3g_1HeAzRT5dC_AoDWXOeT1f550ZEbJWV-tuNJuKJTTOJTKs57FgRxTIOveejANp-UpxGlQwUV49l1a02ns7FMnT85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
معاون بین‌الملل وزارت خارجه: به اعمال حاکمیت در تنگۀ هرمز ادامه می‌دهیم
🔹
غریب‌آبادی: ایران هیچ ارزشی برای تحریم‌های اتحادیۀ اروپا قائل نیست و به راهبرد خود در حفظ حاکمیت و اعمال حقوق حاکمیتی در تنگۀ هرمز ادامه خواهد داد.
🔹
ایران عضو کنوانسیون حقوق دریاها نیست و رژیم حقوقی مورد تأکید جمهوری اسلامی در تنگه هرمز، «عبور بی‌ضرر» بر پایۀ حقوق بین‌الملل عرفی و با رعایت ملاحظات امنیتی و ایمنی دولت ساحلی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/440750" target="_blank">📅 19:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط ۶۰.pdf</div>
  <div class="tg-doc-extra">3.5 MB</div>
</div>
<a href="https://t.me/farsna/440749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/440749" target="_blank">📅 19:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBqV-tb9D7hlmu9MQnjZlqBFofqEWFsU7UcoYjj7dHC07Bik59IWAYX4PwfZBq7GSozR_Bz_zMY5hEf6omrqWMLMO7SuY_9yjdjIsW4miDcXKKHW6BkxSGx-r_A1TyLKVGZjV7yJJXbBf1xCr5zUqv9UuqRc3C2fRJ24vhlwpzKmXQlDpIuazvobmEC2Jq8O3BXF_DhYLtbzuPhKAvQPGrWNa3g7y-6gj8QbnU4KFDC-hC7Hv7UXmjoD37ch_8QCkP_PeACdLrnzFdt0_hvC1F8TResjRWj6kg1YlIYG5Z3UrLolQxkyVHH_d25r3ddU588r3wpAVwvKkeoC0Fbjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی: جنگ، بازرسی‌های آژانس در ایران را متوقف کرد
🔹
مدیرکل آژانس انرژی اتمی: آغاز جنگ علیه ایران در فوریه ۲۰۲۶ باعث توقف تمامی فعالیت‌های راستی‌آزمایی میدانی آژانس در ایران شد.
🔹
آژانس نزدیک به یک سال است به تأسیسات هسته‌ای آسیب‌دیده در جریان جنگ ۱۲ روزه دسترسی ندارد.
🔹
حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شدۀ ایران از زمان جنگ ۱۲ روزه تاکنون تحت راستی‌آزمایی آژانس قرار نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/440748" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440746">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pteyT3hkEjli_FPWS1QnBM9TizA8D-AUDyCQTIMWSP_sGdm3rDQsGkNDPnXkrRfbhGqKA6I-o4Q5x79OihqSR43dzeIkavqtdJzHB5Rik4zU2Lzln3KHsvowjPLf4_4O4APqEOgb0h-7k6mQJdmQ6KdbuRRiwtXHqlXM-poNseYoeNvM45u8Ck2f9ff4JMLUG5s--Ngqlt-MM0rBllqbTOWefHMn7Z4uFy1K2FQVuCOQU5dDyzt4kb6lohDkZctkzpzfV8deaE22BiXBSvu4KRfC9q-D2SnxBSXG1o93Om5Dw0E3FKXubDc2CB-LURvvLzKkCNa83hiwOkTYY2kvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازوکار قیمت‌گذاری لوازم خانگی اعلام شد
🔹
براساس اعلام سازمان حمایت، قیمت ۴ قلم اصلی لوازم خانگی با هماهنگی انجمن تولیدکنندگان، کارگروه تنظیم بازار و سازمان حمایت بررسی و تعیین می‌شود.
کدام اقلام؟
🔹
ماشین لباسشویی
🔹
یخچال
🔹
یخچال‌فریزر
🔹
تلویزیون
🔹
سایر لوازم خانگی مشمول قیمت‌گذاری مستقیم نیستند، اما باید ضوابط و مقررات تعیین‌شده از سوی کارگروه تنظیم بازار و سازمان حمایت را رعایت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440746" target="_blank">📅 18:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع حادثه برای یک کشتی در دریای عمان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440745" target="_blank">📅 18:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLWCQns42AnN2Z0b-JKhPhNXExxCw3vpF3QqLQxl37DgvMer6dUMmq6_ngh3ilvirbIqojgWGNo4VkTsmNmZJOa5sMZo-yWF0UVNV_7EDUDoQ2paWaQ-blNjSY1lF-THKy_ZsqhtdK-WNkbju-5DFR1WVpW_IUr0H7RQ3neL5nv7Bs9VIfXfVpGzVQDa6EvWh-ryQHZPH05SczkAZeuHdXex6o__0Jk-923UeBigZi6LHUVW1yePjRSPEZuVCDYFBT4RQfjhINumo4rGKDLS4OOioS5NoA7gje1wTqO5xVh2Bo6p36GhPxNYhH9HhyFdA8EPTZ-V632sceOCgSn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف: معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را برهم زدیم
🔹
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440742" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW_KwSCpOnUr7opWIaSD-e6bTnW1x2KvNH1sUmNnd0HTmaE8T8S43dCjcujQE1Fj8LVeC8Xzcudl1MQ2hh047mzHv40uwyt1TTn-03C7Rty1650So2d5ytz0IvxlQDsSPLvH4r884BSqWXZk7L3PDac-n5gedLWiMu9qzFlR9oQQsFJAmu5a-Qc4G4p26qljQ4e-M9_naPHyHy5AgauKUuPQBSmn4gbLCWlyLAaPg366gT2i_O0_bvwp6-vTgKzpUHg7NT2z5lyndplU8Ona58GdmMm0CCV4MpUgs0xYd2IuMfIs-sKtwStzG87WOJbH2zB9kL4Jm6jcKWfYrdMltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم سالگرد شهید سپهبد محمد باقری و همسر و دختر شهیدش
🔸
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۸:۳۰
🔸
مسجد امام صادق (ع) واقع در میدان فلسطین
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440741" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f1a255f8.mp4?token=ao2MWX5g8W19_0KFJ_MZUT5jTpQkTUowZBjB5w67JhmcupVAbYZgLpw1_ioALT_4YjsHAgRl0YVCDPG_IJoiSnUXDKjX-aA9s9nATEhc7xLpp7XWfrB7z-nImGJdCcmlJq4Caa-aBz7tl-GmcfIP1eKcjzwM8f2Sw91mSyb0O_oGUA5oE82pzak396u91lA3jk173yNfY1qQzuvzcEiyinEzLv64A3MGh7a2WPvlsnFUuHzX3ktFWuV3s7mcWgn4PA9uuCDE7Oq9hb_noaWU0tChyfCxMiNQn0pu0pJeiTBadj4543Ocot6qWt7XHjNoEu25t8GDWCQatJXUiDMJ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f1a255f8.mp4?token=ao2MWX5g8W19_0KFJ_MZUT5jTpQkTUowZBjB5w67JhmcupVAbYZgLpw1_ioALT_4YjsHAgRl0YVCDPG_IJoiSnUXDKjX-aA9s9nATEhc7xLpp7XWfrB7z-nImGJdCcmlJq4Caa-aBz7tl-GmcfIP1eKcjzwM8f2Sw91mSyb0O_oGUA5oE82pzak396u91lA3jk173yNfY1qQzuvzcEiyinEzLv64A3MGh7a2WPvlsnFUuHzX3ktFWuV3s7mcWgn4PA9uuCDE7Oq9hb_noaWU0tChyfCxMiNQn0pu0pJeiTBadj4543Ocot6qWt7XHjNoEu25t8GDWCQatJXUiDMJ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله یک تانک مرکاوا در جنوب لبنان شکار کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440740" target="_blank">📅 18:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybr3gt0iMrFSc8Hb4f_N5rF0EWxQp4CcvMC74tdIaR8JWRtQ0YDsxnmPv2fqnL1UKmsmR5I4bc7s0inLyygPLtmXyYLQd14GjJM7UCR8vNBGyWZ5qqcqm-egQx1TSaQfohwIJ4nqYuRLOTu9qKuJgY3mnKP0UblOMwvU5l8a1JU3OwF3H7grcoQCNqW5SazUaCML3hGN8XFIxVddZtrgAJk7_WG1ooJ3JusGP-cMDbdGQm8sqGVpFbdAk63Ie2j9ZKvTop9rTA6N9tfMsglzdqf3ptWoeOLQufNb6sIYKMOiZPSKcZHxcJyfuGzse-JtVEgBsYG0bGsRc2FtiefVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: اگر ائتلاف آمریکایی-صهیونی بار دیگر دست از پا خطا کند، منطقه برایش جهنم خواهد شد
.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/440738" target="_blank">📅 17:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌‎‌ آخرین وضعیت فرودگاه‌های کشور
🔹
روابط‌عمومی سازمان هواپیمایی ایران: تمام فرودگاه‌های غرب کشور تا اطلاع ثانوی بسته شده است.
🔹
درپی حملهٔ رژیم صهیونیستی در شب گذشته به فرودگاه‌های تهران، فرودگاه‌های مهرآباد و امام خمینی(ره) نیز بسته شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440737" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حزب‌الله: با یک اسکادران از پهپادها، محل تجمع خودروها و نظامیان «ارتش» دشمن اسرائیلی را در شهرک «الناقوره» هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440736" target="_blank">📅 17:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwnfoMKOWKB5br_Kjv9UkhMWSgCiAQN71WzwgC7rINeuOiYbImBzu_2JH59wr4TgOU9fdguwL8SFYAxCjYELh3YarqBHQmgO8N1MVvqBygWkk9XGajUIqo4_u-Yp7iEb7tnzbA0zsv6rUIekkjmiyx3c-Ix4fNJUbb6UI0qcHmG1FXYHEeKcE8ZPuQ9C0mj62EnPMSdoz_-wjB54IIZhiCwok1SHEnnFtbdmk4qXVfz9NsMaK30kez2iNNAbDTE0Xzf5S4jM14Me7pZIdnNTy7iTIGWZ_2dDUnQVmMZSGokcu1NWh_aRPYdaanqP2tDQ-ROUDU3aDcEbjGe8VeBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم اولین سالگرد سردار سپهبد شهید حسین سلامی
🔸
این مراسم پنجشنبه ۲۱ خردادماه، از ساعت ۹:۳۰ صبح در حرم مطهر حضرت عبدالعظیم حسنی(ع) برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440735" target="_blank">📅 17:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پشت‌پردۀ شایعات ترور مقامات نظامی و سیاسی چیست؟
🔹
همزمان با آغاز حملات اسرائیل به برخی نقاط کشور، موجی از اخبار و شایعات درباره ترور، مجروح شدن یا هدف قرار گرفتن مقامات سیاسی و نظامی در فضای مجازی منتشر شد.
🔹
تجربۀ درگیری‌های اخیر نشان می‌دهد که این اخبار صرفاً با هدف ایجاد هیجان رسانه‌ای منتشر نمی‌شود و یکی از مهم‌ترین هدف آن‌ها تحریک جامعه به تولید داده‌های ارتباطی است.
🔹
انتشار خبرهای تأییدنشده دربارۀ مقامات سیاسی و نظامی، معمولاً موجی از تماس‌ها، پیام‌ها، جست‌وجوها و پرس‌وجوهای غیررسمی را به‌دنبال دارد.
🔹
این حجم از ارتباطات می‌تواند برای سامانه‌های تحلیل داده و هوش مصنوعی، اطلاعات ارزشمندی درباره ارتباطات افراد، حلقه‌های نزدیک و مسیرهای تبادل اطلاعات ایجاد کند.
🔹
همچنین انتشار چنین شایعاتی، نهادهای مسئول را ناچار به واکنش و تکذیب می‌کند و در برخی موارد می‌تواند به ایجاد فضای ابهام، نااطمینانی و جنگ روانی در افکار عمومی منجر شود.
🔸
کارشناسان امنیتی معتقدند شایعات ترور فقط برای ایجاد فضای روانی و التهاب رسانه‌ای نیست، بلکه می‌تواند با هدف جمع‌آوری داده‌های ارتباطی و شناسایی شبکه‌های انسانی منتشر شود.
🔸
در چنین شرایطی، مهم‌ترین راهکار، پرهیز از بازنشر اخبار تأییدنشده و خودداری از ورود به زنجیره گسترده تماس‌ها و پیام‌هایی است که حول این شایعات شکل می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440734" target="_blank">📅 17:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9ad04539.mp4?token=Op4ouAgQXruCF9fXENTl_3oXuvpwO_la2G53MMI1CdC3vzpFE5Z-Ol4kDFzbwXIQ-P-0gpqy-uVOcBKCWQZ78j3x_x9HZLwzHyB0GrNdccA7ly4QBNNc7y2WoLt6fmDG_GaDlCgjz0Du_QLSKXz8DPt0Yaxn9VvWkCW1I0QEvQCYyk0xFLkppGSnJJl1_hbc5m4FILMmggLgo4cj9Du0SKNjowfgCpWeL0I6q0m38TqImJFeVoOrDGX6UnSDuL1eDrGwpFuP_ju_6QZvZo68XHga6ICmL3_e1jg_49A91CabGFRqgTQqthppwd6ryTVYQWBq9HlMOBI8ApiHF8yBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9ad04539.mp4?token=Op4ouAgQXruCF9fXENTl_3oXuvpwO_la2G53MMI1CdC3vzpFE5Z-Ol4kDFzbwXIQ-P-0gpqy-uVOcBKCWQZ78j3x_x9HZLwzHyB0GrNdccA7ly4QBNNc7y2WoLt6fmDG_GaDlCgjz0Du_QLSKXz8DPt0Yaxn9VvWkCW1I0QEvQCYyk0xFLkppGSnJJl1_hbc5m4FILMmggLgo4cj9Du0SKNjowfgCpWeL0I6q0m38TqImJFeVoOrDGX6UnSDuL1eDrGwpFuP_ju_6QZvZo68XHga6ICmL3_e1jg_49A91CabGFRqgTQqthppwd6ryTVYQWBq9HlMOBI8ApiHF8yBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز همای: اجازه نمی‌دهم با من مثل استاد علیرضا افتخاری رفتار کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440733" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71155f3d2c.mp4?token=UotjDACJoPa4MOLlkZvypf8ZFk7sIgtFyjmGrLKVnJIF1udLNeh9lgaPtJOR7nFmQCOTvaLDsW2uNFZIWA9PfyvW4XFRz2Pgf_r3C_EqydktaLEXgdta4FapUhwdOEOGb-LaOkKmeZSQN_H02IzwSc7g9btgidQBLHIcSQSeqa9WYYtHRf14uzpNmjNT4Xg2CMRNHbnz1w_yIpRHFqkBpFBRYiO4clvyPW2hu7nt1xC4PfrhDtiVvhy_N1lKvvWRT75e3pqPuNicAUySPvhdioqzCoIDZeTQt28qx46_71HKzsr8ROhDmfW-C0kkh6db7Uu0al7b-yHX8DbhmOWFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71155f3d2c.mp4?token=UotjDACJoPa4MOLlkZvypf8ZFk7sIgtFyjmGrLKVnJIF1udLNeh9lgaPtJOR7nFmQCOTvaLDsW2uNFZIWA9PfyvW4XFRz2Pgf_r3C_EqydktaLEXgdta4FapUhwdOEOGb-LaOkKmeZSQN_H02IzwSc7g9btgidQBLHIcSQSeqa9WYYtHRf14uzpNmjNT4Xg2CMRNHbnz1w_yIpRHFqkBpFBRYiO4clvyPW2hu7nt1xC4PfrhDtiVvhy_N1lKvvWRT75e3pqPuNicAUySPvhdioqzCoIDZeTQt28qx46_71HKzsr8ROhDmfW-C0kkh6db7Uu0al7b-yHX8DbhmOWFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالگرد اسرائیلی یک ساختمان مسکونی را در غزه هدف قرار داد
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440732" target="_blank">📅 17:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f601e1d28.mp4?token=O0RumWm7ZMenfX1Rx7_txrd8-q3qirbzp7g13FPDvk6cB_adjUbXHkN4v20p3_GFXsCk6BUx6_aNBN3kjB6HS3C1w3aF6CJOwl-ZkLEdUSEguRbvSSj7WOOti-N6zLKzYHFMZc17dN8s14r0Zhsn-0pO7hlHkOMY7ooqqUxSl117zpiX6rbKTqPTW84YskVb6FWTU5ySG_V3v2HtYS5C0DwNpggkezvjSjFAE18Gxhc6_EYf-jKOPmwiV1kbphHvQcdJTh3bZwjM2CDuB8YNc30zAchSq9T45uOqH9NMeyjxQJApBI2msTnfcvFqB9Cj5bMMx13DxoPwkKI684kMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f601e1d28.mp4?token=O0RumWm7ZMenfX1Rx7_txrd8-q3qirbzp7g13FPDvk6cB_adjUbXHkN4v20p3_GFXsCk6BUx6_aNBN3kjB6HS3C1w3aF6CJOwl-ZkLEdUSEguRbvSSj7WOOti-N6zLKzYHFMZc17dN8s14r0Zhsn-0pO7hlHkOMY7ooqqUxSl117zpiX6rbKTqPTW84YskVb6FWTU5ySG_V3v2HtYS5C0DwNpggkezvjSjFAE18Gxhc6_EYf-jKOPmwiV1kbphHvQcdJTh3bZwjM2CDuB8YNc30zAchSq9T45uOqH9NMeyjxQJApBI2msTnfcvFqB9Cj5bMMx13DxoPwkKI684kMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: تنگهٔ هرمز مال ایران و کشور عمان هست، به هیچ قدرتی اجازهٔ دخالت نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440731" target="_blank">📅 16:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63423f1479.mp4?token=V687PabyQIyJ5DzzTBaXSgXH9Qjzxx1uDig9xi-z4DujuyKectaC8OEXyyyHcMmp-Iuos8-UQiwf_5EBh6WiTD3XJG-3WasGhqKQ5xu0kbqvI15rpHt9zKnl6qCjV_5fIR9QB342FItg5PvH2udbumwNmGHTi5R5OJhH05Afn_4_jv3EMaR64Ae6PzM3KpmDjCC8Yfzq0YhbvM9JYzwtGv_qJVsiS9IR5ndZ4M1sUx1egPez1xcMYgW2kHTwJXhk878wyrmO65sI8zSbf72JwdoNGCPO0nmVa4jZORmG-j9A0foQE8kcNrZ_jaBEcR2bjhpQzSOUkMguUfeqWWakow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63423f1479.mp4?token=V687PabyQIyJ5DzzTBaXSgXH9Qjzxx1uDig9xi-z4DujuyKectaC8OEXyyyHcMmp-Iuos8-UQiwf_5EBh6WiTD3XJG-3WasGhqKQ5xu0kbqvI15rpHt9zKnl6qCjV_5fIR9QB342FItg5PvH2udbumwNmGHTi5R5OJhH05Afn_4_jv3EMaR64Ae6PzM3KpmDjCC8Yfzq0YhbvM9JYzwtGv_qJVsiS9IR5ndZ4M1sUx1egPez1xcMYgW2kHTwJXhk878wyrmO65sI8zSbf72JwdoNGCPO0nmVa4jZORmG-j9A0foQE8kcNrZ_jaBEcR2bjhpQzSOUkMguUfeqWWakow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور چین وارد کره‌شمالی شد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440730" target="_blank">📅 16:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLhy7YQbI4ZboSVFVCeaEC4cvHKrlyvBY8lncieKsW_wwbM4klxcM9JXVwnuW390sNo2S3O61SbYEVshz0OMJBVWHtbIL2_RE7zeh8O5lmYJKuYorzeknMvD16lRT-nl8ttaieCkxsam7Is9IzHyiP6OcNu5ZLRt7-nCQUNAaI3rTS3D1eYc73qOBTgGq-GSYJTUkYxdTWC6Y3gh9-VvfX6Vm23jzBjx65Os-bXHy72-8yQM4Qx4aesw4NAyhzBYZqOiilfOb7HNrZw5JmH6eCaXWVxD_IfM2NuoNXOVaMM8mzR-C3O8ADjElLnWVxz0_y-xQ5BGiq0qY7GFQ1ZTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال سیاسی به FC26 رسید
🔹
سال‌ها پیش، زمانی که در برخی بازی‌ها تصویری خاص از ایران ارائه می‌شد و حتی حمله به ایران به شکلی عادی‌سازی می‌شد، کمتر کسی به تأثیرات فرهنگی و رسانه‌ای این محصولات توجه می‌کرد. برای نمونه، در بازی‌هایی مانند بتلفیلد، این رویکرد با فضایی کاملاً جدی دنبال می‌شد.
🔹
امروز نیز نمونه‌های دیگری دیده می‌شود. در نسخه جدید بازی فوتبال EA Sports، اطلاعات و ترکیب بسیاری از تیم‌های حاضر در جام جهانی ۲۰۲۶ با جزئیات کامل ثبت شده است، اما تیم ملی ایران با اسامی متفاوت و غیرواقعی معرفی شده؛ نام‌هایی مانند «شا‌کرمی»، «افکاری» و دیگر اسامی.
🔹
حذف نام و تصویر واقعی برخی بازیکنان در بازی‌های ورزشی اغلب با بهانه‌هایی چون محدودیت‌های تجاری، حقوقی یا تحریم‌ها توضیح داده می‌شود؛ اما نتیجه نهایی چیزی جز اعمال نوعی سیاست فرهنگی و رسانه‌ای علیه ایران نیست.
🔹
از سوی دیگر، وقتی یک کشور یا یک هویت ملی به‌طور مداوم در محصولات فرهنگی جهانی با تصویر ناقص، تحریف‌شده یا غایب نمایش داده شود، این مسئله می‌تواند آثار فرهنگی و هویتی قابل توجهی بر جای بگذارد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/440729" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f18b8d73f.mp4?token=Cl182jroFH_uF_0YFSBSZK2gUaG6TXAQHKnX2_RQCEl28W6hK4km9-EUIPNi1vYyhT071L5o2Zjb9-eLBl-XNOh0wplaN2E8DJGigUD0Y3dpdEenqhGsZGN3DbG1Ybh6Z1J1CpLWVo58xEi8fGv5XYd2hP43RworIA_iwFimyO4QIFP5alO8Y6jaCtYNNz7VmpB1TNPAjUi0wFBrQ1nkBiTYDmHE3JFzCT8M9Fee3YDG3Y9YewI9mZNhPcl2CePC9KpHMrqO-X-JIrHVawa309iVsdDRuq0CKf3al4beRtf7g6yf2EV0xeb9vW7pKOQVH3hmQI4S9Ypr0S9nt84fmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f18b8d73f.mp4?token=Cl182jroFH_uF_0YFSBSZK2gUaG6TXAQHKnX2_RQCEl28W6hK4km9-EUIPNi1vYyhT071L5o2Zjb9-eLBl-XNOh0wplaN2E8DJGigUD0Y3dpdEenqhGsZGN3DbG1Ybh6Z1J1CpLWVo58xEi8fGv5XYd2hP43RworIA_iwFimyO4QIFP5alO8Y6jaCtYNNz7VmpB1TNPAjUi0wFBrQ1nkBiTYDmHE3JFzCT8M9Fee3YDG3Y9YewI9mZNhPcl2CePC9KpHMrqO-X-JIrHVawa309iVsdDRuq0CKf3al4beRtf7g6yf2EV0xeb9vW7pKOQVH3hmQI4S9Ypr0S9nt84fmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امنیت تل‌آویو به بیروت گره خورد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/440728" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831f3f3a87.mp4?token=hZm5klNVBX2LQonmGgTlY2zWhCEcfWCb-aZDu1iTZ3G8R5NRWP9Q2N7fWlXvRaG81w6NTo6UQOBq4d3XKyl1nhCjIDFl5i47GsAFFVBGt-05fGZguUh2AHiUu5QE23UUeWoHHREnenpv8EXtqUnaBEEBQaX5nCaZlN2kGrYdTHQ8tVKgvIL-vp1yGYl1Uz0TDcEChjx9DXg4ZgIzDbVqGoEZDUcNUU8HsZsIsP9RjLoOkYJjxFluvYBYfDWVzA-rZvDAJPd8y7LOEn-D26wOESGOytoDLJxBDidHcq4NyaBpX9OWnKEpdqYefe2xkKQPgw-QhIWB-l0lpx1vhLuSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831f3f3a87.mp4?token=hZm5klNVBX2LQonmGgTlY2zWhCEcfWCb-aZDu1iTZ3G8R5NRWP9Q2N7fWlXvRaG81w6NTo6UQOBq4d3XKyl1nhCjIDFl5i47GsAFFVBGt-05fGZguUh2AHiUu5QE23UUeWoHHREnenpv8EXtqUnaBEEBQaX5nCaZlN2kGrYdTHQ8tVKgvIL-vp1yGYl1Uz0TDcEChjx9DXg4ZgIzDbVqGoEZDUcNUU8HsZsIsP9RjLoOkYJjxFluvYBYfDWVzA-rZvDAJPd8y7LOEn-D26wOESGOytoDLJxBDidHcq4NyaBpX9OWnKEpdqYefe2xkKQPgw-QhIWB-l0lpx1vhLuSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های بی‌اختیار یک دختر بچه‌ برای رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/440727" target="_blank">📅 16:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440726" target="_blank">📅 16:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhEJtlERNOLqVldSD8-565aKb6hglPlDxCWFJAPjNP5-ywHNG_9M4qqfZn-7DhCu5q27SdQImAsE2lmrX58SgofPKR-qR5ocIVuzY-yjGpyyVXxySGX0OqGyOsteCQi6CUmzFH6uC7cwDSZNemt0VZSbi-hLDKc-oDA1xb6jxfSp2RQ_b2kGZO9zuU-duGqSTTJLm_TvI64y40Rt8BdAZgw2II_vyrjlUnJa2Ju47y9p-vxq8Rg6mcxauElpsJ9gTWZh8K8IQ47_Rv9BOSIw5g1CYKbjzFohjA5VYqkkJFPT_1Q_dzlR_qT3zOQVyOB7xPsZmcbixnUfH5dteHYdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAAnR9SPlFakpUmNZxbiIajL7H4ys3Y1tgnjdU2HYT2wNFlc_lmyOiNAogQSIEpGj_WBQEhgtp6o3dBOFPVYoFDpsy1XwsNxLr0bruma0TI_ozFdvWt2HW8Mbiev5telQCyhLKgvu5NZvEEOp61XFGv8VgEP__mYnR9jRQjDgrTdjX-tS64oXicLX884qsbHdBPoTtfX_Q1yPoTAwmxrgLF2KU4u2bwTftuUTJUFjKC6owR2SRQvyJx1NDshtRuPKEJE5oe1MruyOb5Pv8wveW6DpDJtwOMH6vSdRX4U_8syGs37ANUr-rXJY-fpsWQCIkYTAfx6v5ILKynsGy7fug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9ecefb81.mp4?token=rx-ulupRQTzV0blGA0uvcGXRAzPnGCfaQdQHXAlN4uqg_1sbdtfHvXIJqRTybsXtqdj1S_2FvxF3LRfp4ruQW9mQmqtDXxY2al_ejVeNasXBPh4NGoSEUnPF69nNYBpEeVPIecS5QFNziObxjkr6_F-NDHdKkmQWBEalqhf_EJA0AFx9Iqtbagwrgh9Dica2HkBtFyL-d-ft5Ww2dBVzudwq1L5g89WsWRRukh_YkV08-Rz-3OxJwz85zHX1lPGDOxRskwq9DwHeSercJUJSfjuI8gRVGXutHg-ImzHJP9s45hb2ysr6_tf7pcLg46mnv03j33YJYMKqbaLdvHHItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9ecefb81.mp4?token=rx-ulupRQTzV0blGA0uvcGXRAzPnGCfaQdQHXAlN4uqg_1sbdtfHvXIJqRTybsXtqdj1S_2FvxF3LRfp4ruQW9mQmqtDXxY2al_ejVeNasXBPh4NGoSEUnPF69nNYBpEeVPIecS5QFNziObxjkr6_F-NDHdKkmQWBEalqhf_EJA0AFx9Iqtbagwrgh9Dica2HkBtFyL-d-ft5Ww2dBVzudwq1L5g89WsWRRukh_YkV08-Rz-3OxJwz85zHX1lPGDOxRskwq9DwHeSercJUJSfjuI8gRVGXutHg-ImzHJP9s45hb2ysr6_tf7pcLg46mnv03j33YJYMKqbaLdvHHItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حمله هوایی رژیم صهیونیستی به  محله «المساکن» در شهر صور و همچنین شهرک‌های  الخرايب و كوثرية الرز در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440723" target="_blank">📅 15:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c159decf7.mp4?token=tXX-lB6bciEb0qsP9C3VgcmbyYUypTxuZmlgT8o5FO-qyTgKj4OpUhk1a6DwzuS32EaWGNAPkvtMrcrBiTelr0VmU-tmZcKJQSuFECLouq7JzfAdM3V1zir61HiB7a5r_hPWn6LnwPX6VEy9_2oru9XS-54ozEGhaqS4RRfOWT_kKXnJaFr_PwhPJdb4HqRBzhUuDhYvzZld7SCdhQ9p--YjFht6qQikqtw_bVB8ywEp6YXFh8Ea-jol-N4--E7kn776CszKjA7FkajeR6dlYwuXUEwsxZlfMi-1t2ZAANXr7c-_Hue6Zpg3nTNzMPoOdRAJQBSHVfz-D2g_VP1QlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c159decf7.mp4?token=tXX-lB6bciEb0qsP9C3VgcmbyYUypTxuZmlgT8o5FO-qyTgKj4OpUhk1a6DwzuS32EaWGNAPkvtMrcrBiTelr0VmU-tmZcKJQSuFECLouq7JzfAdM3V1zir61HiB7a5r_hPWn6LnwPX6VEy9_2oru9XS-54ozEGhaqS4RRfOWT_kKXnJaFr_PwhPJdb4HqRBzhUuDhYvzZld7SCdhQ9p--YjFht6qQikqtw_bVB8ywEp6YXFh8Ea-jol-N4--E7kn776CszKjA7FkajeR6dlYwuXUEwsxZlfMi-1t2ZAANXr7c-_Hue6Zpg3nTNzMPoOdRAJQBSHVfz-D2g_VP1QlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله پهپادی به مقر تروریست‌های تجزیه‌طلب کرد در منطقه «کویه» در استان اربیل عراق
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440722" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzDwMNoL9qR_P_LsF_5efti1LxXX3ocjqH7fWGQVXYLfwiwMRLp5ORCBKriNgI3o_Lk-ZIRp3-LGiG_nj_6-2ARxDbDKWGOCdTfEDAsdM5OXaWsLkwV8tAhc8zttg9ZRXaMc19-U9mHB1LrTMp1Vi1V0rtglrrjrCGOvMcwd2vEDouUc0IUXRtiaZTgOce_Syd4FD8ocZlr_JMwNJ5CQthUkXejvFFdB72_My2EP-ktIhHKt8FC2rvarO2oPW20-FuejN3rhyGzY26V1WuNMQVbwGcaQlVdsY0HJVWaqtH6-8Guqn-iv7K7XuTlJCK8PJNxid6Yq988YLK6Qh9W_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USUDrpMxdJX58EJ2L1Gq7VnyWH_MeeCcSLH7P8bGtVET7L9pMDs4nrmhxrEXRd7gUJAgk5Ph7UZv4wlJ2jyoDMP2Q3QReS9vdSaeWw6fawb3BQ_yYNc5Oz_1grF2wObJhNBseV5pnW7F24fMOs8noNwkSP3kJsvQrJCCvZJasLcqZM35-gqZn0fIUrbyRxPZXNfiM7UXWrqqRQT3Ttdhvk9Aw-47J84bOLkRJqPeNl89xU1p7OikK9l4U-B5jFr6_vc1K0bP2o8GxYsaiHZQ-FG6S1lwiMcToMPy2U9UZc5RtuxdLmmM8guCxYkrhTei9Dk4EpuN7jT4cVk1nWV6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JROymc-lZTOJ_-awrx56ewtpQY3ExC9-T5zMFUzZZVc6uwKah4uTc5F1hEBOLDDrb6sqpbh9VVirB7FSekSFn7OuBSdq6OJqbCs0b2j8z7DYvnZ_mKF11qzsiIOU9HerBVXsHYVpwJqoWO_x51Mf4k1JHGBkixVLLt9ixwBBcol-a9cQxdE3w7xqR8HodSLMZQIqnbjZNizCT6y0t6iLcb7H6F5MFtNo5WFWZKH2_WosIKniej_6fQeu5739oN0BLOx6ziPZsHBAwW6E72i3hq1xqHHVjnjvmPwxEOSFnUJZ_c8amPtpHVE_m3eRZ_Abm5z4BGDn1J4g7QbkqK2ENA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هشدار هجوم مارها در آستانۀ جام جهانی ۲۰۲۶
🔹
فدراسیون فوتبال سوئیس با نصب تابلوهای هشدار «منطقۀ مارهای سمی» در اطراف کمپ تمرینی خود در کالیفرنیا، به بازیکنان و اعضای کاروان این تیم نسبت به خطر حضور مارهای جرس هشدار داد.
🔹
کمپ تمرینی سوئیس در منطقۀ کارمل ولیِ سان‌دیگو قرار دارد؛ منطقه‌ای که زیستگاه طبیعی مارهای جرس است.
🔹
فدراسیون سوئیس اعلام کرده برای جلوگیری از هرگونه حادثه، از بازیکنان، مربیان و کارکنان خواسته شده از ورود به مناطق طبیعی اطراف کمپ خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440719" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlR-Qh9o5MAYGiqGFFDg8zYWfMxWw0BeMLYpbZAHfwVjtgkdfLuhC20Uz2MtMjhtLaz-VAfNKZYCMtZemb7DPWMILv1_8-qKQW_BuM1yLKKPm9mzYXOtzdNC38GTEYjSTgMjmsrlr8fEh7v-Mulx5MTuMyUEv5ByIJL4Rjj9-Xka3bmu1ANvOmnSdyGtPM85a8Sq7a9OJiRcpPhb-hsniUEAArih4iVJ5d6m5tb5mL2pbrJL_oqR5NrgrGcXU-uj0yG3wRp2pTYMGOn0YaW8zl1O1vWSz0ws6sNqrmb-ujcHhf3-cGlrJ1Wpoq4cy-IGV6hj6HP_LCGDQsNEqfSdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ موشکی حزب‌الله به شمال فلسطین اشغالی
🔹
منابع اسرائیلی از به‌صدا درآمدن آژیرهای هشدار در شهرک‌های شمال فلسطین اشغالی از جمله کریات شمونا درپی شلیک چندین موشک از سمت لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440718" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr_lK_nLjfNbWMwLR4f-ZVljaOpsm8QmqWNf30oGSxyqrsGC-zVOo4wtJb_QZ80Y54lo9LI9EhQoDdl9bMKiUUuV55E0f5gDTPNZIoBsbJNRzUDbtVaiR5Y9lAaXKNLIwuHq-iPBGOX8y8A7Efo3M0UhK8AHZ3e98LvV9B1U9LJb7-Q4bVDUcgeo_h4GbLbtLZZW7r0vfKXTjz1s8Mr5ZQvdagh-nNlPbVXlLldhBMe9k9ARIhiivfuD4cDPn2NHCDsu1jMX9CNrsAuGTsKxgKHCT48n_ELGV6XMMEcO2vC-zcNqxflH-tD70OeucKNaayo46tMf8UrOhtHbgoWMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش: در صورت تکرار شرارت‌های دشمن، اقدامات ما شدیدتر خواهد شد
🔹
سرلشکر حاتمی: ملتِ کشور دوست و مبعوث شده ایران عزیز!
دشمن در حالی که میانجی گفت‌و‌گوها در ایران حضور داشت بار دیگر با عهدشکنی و نقض تمامیت آتش‌بس ثابت کرد به‌هیچ‌وجه به آتش‌بس و توافق پایبند نیست.
🔹
صد شبانه‌روز مقاومت و ایستادگی‌تان، تجلی اراده ملی، اتحاد یک ایران منسجم، فتح قله‌های تاب‌آوری و پیام روشن همدلی و اتحاد مقدس، تحت رهبری و فرماندهی امام خامنه ای ( مدظله العالی) و پاسخ قاطع ایران یکپارچه به دشمنان غداری است که استقلال و تمامیت ارضی این سرزمینِ پاک و عزت و امنیت مردم شریفمان را نشانه رفته‌اند.
🔹
به پشتوانۀ شما مردم همیشه در صحنه، بار دیگر با اعلام آمادگی کامل ارتش جمهوری اسلامی ایران، هشدار می‌دهیم مسئولیت تجاوز رژیم صهیونیستی برعهده آمریکاست و در صورت تکرار شرارت‌های دشمن، اقدامات ما شدیدتر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440717" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_0n8qYNnSuwlcBTjPMbLe01nR2ABSQG1wLf9u27z-6C3HKzJ7qnmAP6E-wHqaj_PtfaUsHHZCD4-6u7HHB_06HhUiD-Rcs_kfZyWMFTkjMI8L9ADhfZ5D_Z9H-aekHsKLERwjptLr6ILJUNdklM7fisIqP6JScpq0nNfTQcb3E9o7_uBnbSRMc99QzmziyNze0rgjQ1lvnKwoXBLGxD05cs8AIvpQCZNJMz0DAS_vmShBChh0hpl52ZG1QMwKw5B9Cwcto9OghoxCw1ucdzR8-XeBzLR5sU7DgNfPGgFVpn3aBSbzx801C1Z1v5gJ8oEmgO1DYdfprmVYQfD2Uq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: در برابر هیچ تهدیدی عقب‌نشینی نمی‌کنیم
🔹
دیپلماسی و دفاع ۲ بال قدرت ملی‌اند؛ نه میدان را ترک کرده‌ایم و نه میز مذاکره را.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440716" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFiIR4I3zJWFXXmbOZOPNKlK9wAVpKI6ad_krgCtIaNzM7WYZffC-osEvRg6LxKy2d6sCHq_sJ0NZJIbtQ3BkNUeC2vOz2R9KF1IQxI8mHp1cbcQ8xFgiOp9qNLoZ-UFLPNlrw0p9ud0vddu0bQPhF_N6BGex2VOR9ZNCFEnwZSnqED6UYmLzKlkXdzRCo_nS7qqL6zk-lvDm4UuY1IZce6kiNKGASauJgWS6t6oF8bcSFbqnvk9Tdcm04cdbXwLUYOcGNT1l5O9CG0hNFhCwyU1tEAkm4eTgm5KRql3rt6svKT3MJd4kdCvCm5Hqr1QW_lLmm_8H8ESGf8iz7cyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
🔹
۲ فرودگاه‌ بزرگ تهران از صبح امروز تمامی پروازهای خود را متوقف کرده‌اند.
🔹
روابط‌عمومی سازمان هواپیمایی به فارس اعلام کرد، این پرواز با اجازهٔ ایران انجام شده و این هواپیما با عبور از فضای شرقی کشور به تهران رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440715" target="_blank">📅 15:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farsna/440713" target="_blank">📅 14:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی لجستیکی حامل مهمات و یک دستگاه ارتباطات متعلق به ارتش دشمن اسرائیلی در الشقیف با پهپادهای انتحاری مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440712" target="_blank">📅 14:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز و کنترل ایران بر این آبراهه  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440711" target="_blank">📅 14:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/440710" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKmtBS7iErYP1zZWNQzcmdxauQdXf1umflnnW0uFQhQ5ZtcCN5YRPvhECTTEPcV_gQ7IdfAjSAi_U7Ue7qg_pRu0AT0BQD_B4dXV4B4EGLkQCRIBk-dsTC2mjdSRqMkvrGZWXvK402_fIvPWJO0Xir897P7ri06cRtg-o_61HmWa2VdqNvJ7JkosknGT--fpehOgSiY6j38u61Lze8M6UPPzdpwpvvzgwpo4FFP_iD2DO9IAZXj3Gul8I6_92XR_2-APMe3tnSiPK0Vmeg8gl8RFBHpjj3ngkO-qXdq1nMEVVBJUR57fw8waFKxVr9BrlWFioWPZESz45u783AZRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و ایران باید فوراً «شلیک به‌سمت همدیگر» را متوقف کنند.   @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/440709" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440708" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9M9YNgTtSHtR5hyc4Y3nDAT9VG2LaeW58fhFDca-b2V_j500KnGlJCfygS3xmcbTZB7TVvel9hnncl4rDXJpwvrDS2p6fMkMVBNmXOBCaRVO_1-w8pXBXdnxqtao1csiVPnxYAOEHG5vlQez4JP-pU2myrTeDzmmwPk8xLTi92HXUsXrR_OfEuaLwSnTJpnKS531j2-C-YofMZfULzPIZXKA3DPmiOm_8_KYtskXgb-syCGiYxiufMq7Fjj8G9PizeN_kaS-iwk3rJMVKt_ONK1VLD-zCOKtqxbR2x8AqEgZ1DtPC8ZoF0SMvGHM0-r-cgZ67vWXwjMQ35HB5ydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/440707" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در نفتکش هندی در سواحل عمان
🔹
مرکز امنیت دریایی عمان از وقوع آتش‌سوزی در یک نفتکش حامل ۲۴ ملوان هندی در ۵۲ مایلی سواحل عمان بر اثر اصابت یک شناور بدون سرنشین خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440706" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی بازداشت کردند.
🔹
در جریان این عملیات‌ها یک سرباز گمنام امام زمان با انفجار انتحاری یکی از تروریست‌ها به شهادت رسید و یک نفر دیگر هم مجروح شد.
🔹
از مخفیگاه این تروریست‌ها شمار قابل توجهی سازۀ انفجاری، سلاح کلاشینکف، سلاح‌های سبک مثل انواع کلت کمری و نیمه‌سنگین مثل دوشکا، نارنجک‌انداز ، سلاح‌ M16 با دوربین دید در شب و سلاح M4 کشف و ضبط شده.
🔹
وزارت اطلاعات از مردم خواسته هرگونه موارد مشکوک را به ستاد خبری وزارت اطلاعات به شماره ۱۱۳ یا درگاه‌های رسمی ستادخبری این وزارت‌خانه در پیام رسان‌های ایتا، بله، روبیکا و سروش‌پلاس به آدرس vaja113@ با تیک آبی گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/440705" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واکنش تحلیل‌گران به چالش‌های اسرائیل و آمریکا در حمله به ایران
🔹
دنی سیترونوویچ، رئیس سابق میز ایران در موساد: اسرائیل با دوراهی سختی روبه‌روست؛ یا واکنش نشان دهد و خطر درگیری مستقیم با آمریکا را بپذیرد یا عقب‌نشینی کند و به ایران اجازه دهد معادلهٔ جدیدی شکل دهد
🔹
رابرت پیپ، استاد دانشگاه شیکاگو: آمریکا و اسرائیل بدترین دام تشدید تنش از زمان ویتنام را راه انداختند؛ ایران قوی‌تر شده و این یک شکست بزرگ برای آنهاست.
🔹
هری سیسون، فعال رسانه‌ای آمریکایی: ترامپ دوباره در صحنهٔ جهانی تحقیر شد؛ او ضعیف است و نتوانست مانع اقدامات اسرائیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440704" target="_blank">📅 13:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/440703" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU0rpkZmYssXr9cvdhCD_n4ZkHrdmZ4fwF_jvoxyw-wq9BIVmrokyrbz6FIY3HTUOoqkiH-TiP0nrOx6KalPw-G29hn7O8XdO1y0YCrJQ76-bTDl-2kqRqluXTye7o8LbZTTB8jW2uMJPiIU7VfBMAroku9l-BiOLC6tYR3Lziir0sJXQEI7hbABciUE2UtWswyKffkJaynwgKPitopaaSpBOaefbHdiH8fpAbuZA3tk4dFVkuHnH5bUTkcXDeBd2y0h2cxYbHYMXcPAB0G2H6N7mzPmMIp2P8WwFbJgNXJRtlBxV0A-32uvuJWPHiew7tRfDGwV508aja6ZU26oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: تا لحظهٔ پشیمانی دشمن سکوت نخواهیم کرد
🔹
نباید دچار ‎خطای محاسباتی شد. راه آرامش و ثبات از درون جنگ می‌گذرد. اگر خودتان را برای پاسخ قاطع به دشمن آماده نکنید جنگ درب خانه‌تان را خواهد زد.
🔹
نیروهای مسلح ما پس از سکوت صحنه نبرد، بر قوت‌هایشان افزوده و آسیب‌هایشان را هم برطرف کرده‌اند.
🔹
ما قوی‌تر از نهم اسفند آماده پاسخ هستیم و تا لحظهٔ پشیمانی و تغییر محاسبات ذهنی و ادراکی دشمن سکوت نخواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/440702" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWP7v6P8zxWiOIA4TSMu1KwCV7aE-1xtrWa0agxVkRQPOoV-l8YVcYTNsWcBaHS6QztjUBQ2yYh1Keexds7Z2v-XVfulgCIMH7AWVAeW__DiBD3roOnE4VBr-KGVV7PNk-355gEPiMyv0sMCbUdK6GN_GFNeXmoGAVDUeirHts9itJXYVmbMeKyyB2-z6K3wdYbXC2ZITJUQ-vnIF1IL40vQQVaGf2I_DOkAVyfDrmPHQajdBFFMFED6apCO0Ebkd58SCj4p0yPbNckI6OIEhzctld6MKG3xFP2uaJHVg6LJwWIPEBuGPgFU3ca3ekt8kS-UPKXU0gqddyj_YEqO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: پشتیبانی از نیروهای مسلح با قدرت ادامه دارد
🔹
سردار ابن‌الرضا: رژیم کودک‌کش صهیونیستی امروز بیش از هر زمان دیگری به افول و فروپاشی نزدیک شده است.
🔹
تا زمان تنبیه متجاوز، لحظه‌ای از مسیر دفاع از منافع و امنیت کشور عقب نخواهیم نشست و تمامی ظرفیت‌های دفاعی و پشتیبانی در خدمت نیروهای مسلح قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440701" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440699" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1934e5bb.mp4?token=Lm-ZCElchxC38sJBkS9DSlEqxtIZN_Y7O0gXYPqRmOY1GogELeV7PNIqUm2BhQpMYb2Hy_iX5v8acHC60BfK2eIy7MKY76ZiPXvTD1aXoT5QVlqet_ir_WMXUzkbe7yZXXOBtdPGW7PeMqJcTgHvnWnrU4cn41YgVXGseZM7Yo4RQ_6cLGbJ0ZrhO_qDOEm5X5BYSgIkB2-rijQqcGW2ZYa-ERTTBj0fCpK1_VfCbSZ8kbBoBgXrU9IBi58hrXLQfE_26CRoR_0131L7lURs25G25P5qIrIU7I3fH1e6e93x6hhtJhlny61Oj-LILcxL-aHltTf9vRQF4kPeZ2uh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1934e5bb.mp4?token=Lm-ZCElchxC38sJBkS9DSlEqxtIZN_Y7O0gXYPqRmOY1GogELeV7PNIqUm2BhQpMYb2Hy_iX5v8acHC60BfK2eIy7MKY76ZiPXvTD1aXoT5QVlqet_ir_WMXUzkbe7yZXXOBtdPGW7PeMqJcTgHvnWnrU4cn41YgVXGseZM7Yo4RQ_6cLGbJ0ZrhO_qDOEm5X5BYSgIkB2-rijQqcGW2ZYa-ERTTBj0fCpK1_VfCbSZ8kbBoBgXrU9IBi58hrXLQfE_26CRoR_0131L7lURs25G25P5qIrIU7I3fH1e6e93x6hhtJhlny61Oj-LILcxL-aHltTf9vRQF4kPeZ2uh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دادستانی کل کشور: انتشار هرگونه محتوایی که به تأمین اطلاعات موردنیاز دشمن یا تشویش افکار عمومی منجر شود، طبق قانون تحت پیگرد قضایی قرار خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440698" target="_blank">📅 13:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
انهدام پهپاد دشمن در غرب تهران
🔹
پیگیری‌های خبرنگار دفاعی فارس نشان می‌دهد پیش از ظهر امروز دوشنبه یک پهپاد متخاصم در غرب تهران توسط رینگ پدافندی پایتخت رهگیری و منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440697" target="_blank">📅 13:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6qKRumJWW_cdKRewSn7PlgltKjn-jGbnIpA3t4uMnyYSO3jh4O8wuetdkuf2bvscajqM3FpMggYeJfWSqDQowJOvjLGW42SIYRVEsaSrZCKFyRLNmn6viwbW3VmzPrGsDkBrM9-CWwV6MPlsBi3tejanqo7TnS4pf8duiKDpQEwv2yeJFA5blbyFz1UqSkO0Llrp1zIxtB20VNsh9EzXwxFWdwXagijyTGhKjMDMl0gZu9sJM_n2AUYGLwZZqS-jo3web-iMgdBvZiU31CWuy8ZMqTS13V_J9lOxk4B25YZ-0OjNefnjsVyzucAE5-O0voSiPOjE3UihVrSdbEMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و ایران باید فوراً «شلیک به‌سمت همدیگر» را متوقف کنند.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/440696" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9OJAtsPMX3f-_F4iwalZoFbz86XFYp3WduylvuP3VhVcSttGbE8WKovWKvFZ69NoDCLqTYTKzyw5Fv0F0m1mebhzRdhTxV5XlSiLL4tIzo-ImPFMjxeRFGIH_0fZCw6mEzq1UqjzysPYgJ32Oybo180G0NpCR2jCnAdEshbLw9JcgSRNGxALTQdKQQHqBkD0EkmVjnEFNhS8b4XEQzWwKgTJAM7bipkRLmbgloJmMw7A_zuzgKC1GYI8s6xOylPpcYVUWR1HZKgZ5K_lqqp-TccVxj61rF6XdmUHltShgFyCnLuv7N148Bz-WC9QEB3N6n1ho22oeDAC1_YO9GJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: تهران فصل تازه‌ای از سیاست دفاعی خود را گشود
🔹
حملۀ ایران در دفاع از لبنان، صرفاً یک پاسخ نظامی نبود؛ بلکه اعلام رسمی یک دکترین راهبردی بود.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/440695" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
دادستانی کل کشور: انتشار تصاویر و فیلم‌ از محل اصابت پرتابه‌های دشمن جرم است
🔹
با عاملان انتشار این تصاویر برخورد قاطعِ قانونی صورت خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440694" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
دادستانی کل کشور: انتشار تصاویر و فیلم‌ از محل اصابت پرتابه‌های دشمن جرم است
🔹
با عاملان انتشار این تصاویر برخورد قاطعِ قانونی صورت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/440693" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe2032c8e.mp4?token=u01zHdrqU2Dtl-DnSrO-AjfAD1DSxGi793UprJSlJfUKO0RwHibnMCrMqdsmWe5vn9NpnU_G3gUOxyansQAv81j3_MdqSEjcr6HmtIog6LjKXJMTcHWTsoNYCJmJeMp9uy-r4x4DFo5I2PrGvp7TKL4kBWdmitlk6Nau7s1PPhtWa-BRNismbyWbxc71LH_n2-jgk_ikVwjl_fJd6UOXtgo7pECrCSzj54gzXXVInmEd7QSgNuEa7hTLPHvy30iB25G04CQnm9-qXpiCtZwuPfHoDnhMdee3treDwAT4NKkzGiQQITly8XVUKUJFhLyiP0Hdpak-UJj3DO-r-KoJRi8EhH2-FoKqVqR7jPb9ZoJsQyJSgmTnfbuu4Sw6vjtQxvulhv25vzIXokCMNAsQpO5csyiqm8NNv6LU9NWgwo_wfR6yu10AeqMUn8fdDp1c4N7zi-AzpeueJ0KOeQLtXKqiUSZQfa3nEBXVup5DfmpxZTlsCCaQSLb0FdTysDEfW-haFcS69RjsACEkBF2-lQmNXwmlcDY-nHB8tJNwBcSvFjaMjj1KbbwQ9_q3eR76LpKK9ifh0qflOFa9iaIdVbNShp6S5_Od9YWvAxmQUwM5RgAHMMVp_y494APDaqlvz0_CAoTOToFARZa-MHM_WlZfunYAUkaN9vqaVpkBZRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe2032c8e.mp4?token=u01zHdrqU2Dtl-DnSrO-AjfAD1DSxGi793UprJSlJfUKO0RwHibnMCrMqdsmWe5vn9NpnU_G3gUOxyansQAv81j3_MdqSEjcr6HmtIog6LjKXJMTcHWTsoNYCJmJeMp9uy-r4x4DFo5I2PrGvp7TKL4kBWdmitlk6Nau7s1PPhtWa-BRNismbyWbxc71LH_n2-jgk_ikVwjl_fJd6UOXtgo7pECrCSzj54gzXXVInmEd7QSgNuEa7hTLPHvy30iB25G04CQnm9-qXpiCtZwuPfHoDnhMdee3treDwAT4NKkzGiQQITly8XVUKUJFhLyiP0Hdpak-UJj3DO-r-KoJRi8EhH2-FoKqVqR7jPb9ZoJsQyJSgmTnfbuu4Sw6vjtQxvulhv25vzIXokCMNAsQpO5csyiqm8NNv6LU9NWgwo_wfR6yu10AeqMUn8fdDp1c4N7zi-AzpeueJ0KOeQLtXKqiUSZQfa3nEBXVup5DfmpxZTlsCCaQSLb0FdTysDEfW-haFcS69RjsACEkBF2-lQmNXwmlcDY-nHB8tJNwBcSvFjaMjj1KbbwQ9_q3eR76LpKK9ifh0qflOFa9iaIdVbNShp6S5_Od9YWvAxmQUwM5RgAHMMVp_y494APDaqlvz0_CAoTOToFARZa-MHM_WlZfunYAUkaN9vqaVpkBZRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چاقوکشی در نیویورک در آستانه حضور ترامپ
🔹
درپی حمله با چاقو در ایستگاه پن نیویورک ۶ نفر زخمی شدند. این حادثه نگرانی‌های امنیتی را در آستانهٔ میزبانی نیویورک از بازی‌های فینال NBA که قرار است ترامپ هم در آن حضور یابد، افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/440692" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
سپاه: تجاوز دشمن به صنایع پتروشیمی را پاسخ دادیم
🔹
سپاه پاسداران: رزمندگان نیروی هوافضا، در پاسخ به تجاوز دشمن آمریکایی‌صهیونی به یکی از صنایع پتروشیمی، دقایقی پیش صنایع مشابه در حیفا را هدف حمله موشکی قرار دادند.
🔹
اخطار می‌کنیم؛ دشمن صهیونیستی با اقدام…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/440689" target="_blank">📅 12:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af6ca7cd0.mp4?token=s9zStDfeWWpl4fJBol1fhYJYBmyxCSxyuEteWQE5wHISlRJnt3uovbx9qUD7eGhzOd4fFiYVSA2gbGDElp6FsUT9_jv8C5B_7qNkPpBIVUbGY0RVSj2BP3axcCcU8uz2qAz0wCXqsdGyucMZeudauPddregLXrfAeob7vuj0VCZAStTJF9jeY57R_I7K8XpRFd1MNmZCKJanWaPu0QMnZO3nwBzZ5jWHImML5DONlSS605AcrJEg1QQx3ndxctJ8IyqKUd4UV2smpadabJOPswxVn-lY2SvEn6XACeOqpKxuoax_GPTMihmZclZ1O70O8sYVeW1cWoGWOcdAkxlAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af6ca7cd0.mp4?token=s9zStDfeWWpl4fJBol1fhYJYBmyxCSxyuEteWQE5wHISlRJnt3uovbx9qUD7eGhzOd4fFiYVSA2gbGDElp6FsUT9_jv8C5B_7qNkPpBIVUbGY0RVSj2BP3axcCcU8uz2qAz0wCXqsdGyucMZeudauPddregLXrfAeob7vuj0VCZAStTJF9jeY57R_I7K8XpRFd1MNmZCKJanWaPu0QMnZO3nwBzZ5jWHImML5DONlSS605AcrJEg1QQx3ndxctJ8IyqKUd4UV2smpadabJOPswxVn-lY2SvEn6XACeOqpKxuoax_GPTMihmZclZ1O70O8sYVeW1cWoGWOcdAkxlAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ خواهران منصوریان به رئیس فدراسیون ووشو
🔹
فدراسیون ووشو در بیانیه‌ای اعلام کرد که پس از شکست سهیلا منصوریان مقابل رقیب خود، خواهران منصوریان به رئیس فدراسیون ووشو حمله کرده، به او توهین و اقدام به خودزنی کردند.  @Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440688" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch-s73nTkup-Km7IRgUkOA0JqS3IzOLTYWfe85jkN6oYiL0YS5d5IhuGnaAoA-uDBOOse0fG7twcvyxWXN62RodWGnVRIZrdrplIl95OH89Dr63NlAW7BWEwdqCgGwWjJUTbRaFW_z_SYtX9RSc52yZbT2o8qZjXrMOXbmapCGS-p5fX7nwy7MWBb3hZklK9338Az3V3xJBIWmsfrR-EJs1RE6SRdXeWEp4Lm0hAha5rv6YIfHnddomkIDFF4i_Mpu2cTPDeV9T0VXJA6lHHtWvaDc0-k3lHmc4k2nzogLAZCaEcXyVmXjcQgW-ox-OIQFGRZkxLoJ5g30ar-mF9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت عادی شعب بانکی ادامه دارد
🔹
رئیس شورای هماهنگی بانک‌های دولتی: با وجود تنش‌های ایجادشده، شبکهٔ بانکی کشور با آمادگی کامل درحال فعالیت است و هیچگونه تغییری در روند کاری بانک‌ها و شعب بانکی در سراسر کشور ایجاد نشده است.
🔹
در صورت تغییر در ساعت کار بانک‌ها در روزهای آینده، شورای هماهنگی بانک‌ها اطلاع‌رسانی لازم را انجام خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/440687" target="_blank">📅 12:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6142cc848.mp4?token=iBuN1VT7wRhcSA9wpVeakikYFvYlLyTU5lL2Tycvt8TWmbicafkmNjmOSbqpEK9cYUD6_nxF4s4laUXkdPJ2gf8m-WBUDxxCt-dExuIXcKmD37-I6SIvyaxLBomJuaME0-w9PEFhccXBlrX8OSM-G1sJor7zDN4vOpiA0QK6ey5KBA9_g9uzlCau_vNZ3czb5vBj985h8-iB4szbkIyF83xF4acqvPXf6v8_aUo0ab2GWcsbX3YaeXAXPAkIv2vUfUCtP9oUIvuFFNfddcuLDp3qZmws7fLN1upyjZOTYJf3qIAhBZPj3YFsPVmEhS36nuSv3TOGSs0dhbGusBUceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6142cc848.mp4?token=iBuN1VT7wRhcSA9wpVeakikYFvYlLyTU5lL2Tycvt8TWmbicafkmNjmOSbqpEK9cYUD6_nxF4s4laUXkdPJ2gf8m-WBUDxxCt-dExuIXcKmD37-I6SIvyaxLBomJuaME0-w9PEFhccXBlrX8OSM-G1sJor7zDN4vOpiA0QK6ey5KBA9_g9uzlCau_vNZ3czb5vBj985h8-iB4szbkIyF83xF4acqvPXf6v8_aUo0ab2GWcsbX3YaeXAXPAkIv2vUfUCtP9oUIvuFFNfddcuLDp3qZmws7fLN1upyjZOTYJf3qIAhBZPj3YFsPVmEhS36nuSv3TOGSs0dhbGusBUceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز
و کنترل ایران بر این آبراهه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/440686" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد. @Farsan - Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440685" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIQz8N418-g-aBFEaYPTlNsCQzfEV6famFjour-ZzZUQZhEUEDZSAPuL-BbM_m90snYUCxGg58cyT7QUU8o4b7hdpetiW9Ohk-ftQ6akQ6w8k8CTODAXgalpOXvQND1uLHut5b3DLK26Rloc8OClgIXqoD2u36YJYdZJEU78ixsmmvMVzs3WPpMaxFm3Nrj1MbIikjV_i1sUY6DNHh7FEmdv7DwggCLoG8LZNATIcQSpg1lbhDxYU9xQJO25eW903BiVsFJRe3-alZCOFYO0628qu52ib4bd8YWbGPklBSk5tQRUJrv-WiEQYrue_7cpNB4RzaMMdnmrPivSZ9Vlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش الجزیره از سانسور نظامی در اسرائیل پس از حملات ایران
🔹
در پی حملات موشکی ایران به اراضی اشغالی از شب گذشته که در پاسخ به تجاوز رژیم صهیونیستی به بیروت و نقض آتش‌بس انجام شد و امروز ادامه داشته، شبکه الجزیره در گزارشی از اعمال سانسور نظامی گسترده در اسرائیل خبر داد.
🔹
به گزارش خبرنگار این شبکه، ندا ابراهیم از رام‌الله در کرانه باختری اشغالی، به‌طور کلی در اسرائیل بر این موضوع تأکید می‌شود که در گزارش‌ها اعلام شود ارتش تمامی موشک‌های شلیک‌شده از ایران را رهگیری کرده است.
🔹
با این حال، به گفته او، تعدادی از رسانه‌های اسرائیلی از خسارات در برخی مناطق، از جمله در حمله نخست دیشب خبر داده‌اند؛ اما ارزیابی کامل تأثیر این حملات و میزان خسارات به دلیل سانسور خبری همچنان دشوار است.
🔹
در این گزارش همچنین تأکید شده که در اسرائیل سازوکاری تحت عنوان سانسور نظامی وجود دارد که از انتشار اطلاعات حساس در رسانه‌ها جلوگیری می‌کند؛ از این رو، برآورد دقیق میزان خسارات ناشی از این حملات همچنان با ابهام روبه‌روست.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/440684" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEpaSgn092HB3gFHslxV3k2RAgkoZ5CRbRJgsOJaVjnDRNQqgq5m5_-aI3U97BVfJmwiWp2dn66uKERBkFHREtRIA_BMqrLv6oa0OHh9eNC_lXsnDcofD0UlTygDS-bTvg1vXqRE2kycQII69ioaselXFtoMZFVwZFs5G3eULhC7WfnmNN0HzhqFtBNhIN7Z3Y8EPoJu_CEJe2LrSuammrkDvmcMRpEHqyi_R3W7QiVZlFfYXqKMBQHEA64Dgn3xowQdzFT9yCLSVqPdnXFwn9_kJvoSuwHJNkj8j39OzliTlyqVksbkLacz9WkIVlFHro4ZZMCSnaxvD7k4fBhBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‎ حمایت دولت از رایگان‌شدن مترو و BRT در تهران
🔹
معاون اول رئیس‌جمهور در دیدار با شهردار تهران، رایگان‌سازی مترو و اتوبوس‌های تندرو را اقدامی مهم و قابل تقدیر دانست و گفت این طرح می‌تواند به کاهش آلودگی هوا، ترافیک و مصرف سوخت کمک کند.
🔹
عارف: درآمد حاصل…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/440683" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7rPdGdi5wddg4zsAr3ccwoxb8TD9ez1d58nGn8E9zWTfyBGve3O-IGDCcLqqvydMMmOkXrpFGJK1WA6ICZoyaieJjqPsgY68dKzGVYosdSogbzBknd6eEABzwuyTu4PBCORht4-_Oni6FnX3yBz69T_5vSTh-9RXaqszz5DGqiRtRc5ulqIL00MPWndHDTviXYdYl7Y98wifAzwseM83Ukwr8C6Bw6bwPTGBvdBboNbeZY2QP8rAaHgGBtcppnGJp4QzD6LUmKeYyGIibqSM6lR2XyRTNpdXuRJP5-zPhO6NhJuHPtxyE-1zHuJrNgxpW9EEVrkdI0LezJl3yG-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۰۰ شب مقاومت، ۱۰۰ سال امنیت
🔹
سازمان اطلاعات سپاه: اطلاعات میدانی از ضربات شدید و سریع نظامی، امنیتی و سایبری دیشب به سرزمین‌های اشغالی و نشان‌دهندۀ موفقیت ۱۰۰ از ۱۰۰ است.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440682" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعلام زمان شارژ اعتبار مرحلهٔ سوم حمایتی از کودکان دارای سوء‌تغذیه
🔹
معاون اقتصادی وزارت رفاه: اعتبار مرحلهٔ سوم طرح مذکور از امروز به حساب سرپرستان خانوار دارای کودک ۵ تا ۵۹ ماههٔ مبتلاء به سوءتغذیه، تخصیص خواهد یافت.
🔸
بر این اساس، به‌ازای هر کودک در خانوارهای با وسع اقتصادی پایین، مبلغ یک میلیون و ۳۰۰ هزار تومان و برای خانوارهای با وسع اقتصادی متوسط، مبلغ ۸۰۰ هزار تومان تخصیص می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/440681" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440679">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در غرب تهران
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست؛ همزمان پدافند هوایی در برخی نقاط تهران نیز فعال شد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/440679" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440678">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e4a03961.mp4?token=DifpPB5a8IBkih6ORdU4okSfJ0F7-lwTiguM2R8-sx_FMQipN4uRNwdloEbEcIdpBesCCro8BHZX739ygDKiY-PRrCJYWvYFBWBM2sYH5Eqs2qz6sGEN2xKmlCUKgHKv9KL1lyH5I_jZX1YMvnB4zL8_gsxPZTts49Ah1qLE6S_uBdtzQBTf-Zh-rVM2H8D6jwTtj8CboQc_NDFPc0OetE1aWrKOwQzly2cCrW3p3eNZmRT-xybrtW24_CIVdpSGabY8ysPpFVEsRV7zUbDBbQacCteboGoxw4xBiWGm0jX1VgTmWEnhecFQSiN2Eg6i_o9lHTL8-S6bydl9FeMMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e4a03961.mp4?token=DifpPB5a8IBkih6ORdU4okSfJ0F7-lwTiguM2R8-sx_FMQipN4uRNwdloEbEcIdpBesCCro8BHZX739ygDKiY-PRrCJYWvYFBWBM2sYH5Eqs2qz6sGEN2xKmlCUKgHKv9KL1lyH5I_jZX1YMvnB4zL8_gsxPZTts49Ah1qLE6S_uBdtzQBTf-Zh-rVM2H8D6jwTtj8CboQc_NDFPc0OetE1aWrKOwQzly2cCrW3p3eNZmRT-xybrtW24_CIVdpSGabY8ysPpFVEsRV7zUbDBbQacCteboGoxw4xBiWGm0jX1VgTmWEnhecFQSiN2Eg6i_o9lHTL8-S6bydl9FeMMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیچ مذاکره‌ای دربارهٔ ذخیرهٔ اورانیوم ایران انجام نشده و اخباری که دربارهٔ آن منتشر می‌شود صرفاً گمانه‌زنی رسانه‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440678" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440677">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
یک منبع آگاه: در صورت خطای مجدد، زیرساخت نفت و گاز منطقه هدف قرار می‌گیرد
🔹
یک منبع آگاه نظامی به فارس اعلام کرد، در صورت ادامهٔ حملات به زیرساخت‌های انرژی، کلیه تاسیسات نفت و گاز مرتبط اسرائیل، آمریکا و هم‌پیمانانشان از جمله تاسیسات انرژی منطقه‌ای هدف نیروهای مسلح ایران است.
🔹
این منبع شرکت‌های نفتی و حوزه انرژی در منطقه که سهامدار آمریکایی یا صهیونیست دارند را هدف مشروع ایران دانست.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/440677" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440676">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7fc74cda.mp4?token=deXxcsPrewVNEjrI7LluVicpq4YNH4STOvVVEkziQzprRPvxA2wnwNCVAvXLPr5f9iWlJY0rlEU8QrhRcK7NTZeQRlwLEIRAvbIp4i8Jynnk4DH5F7nVdp3ufVIknEV5PjDjretjVBUztZ1Zu83fOjET6yTY_n6WMF3Djy3rD5swnfGBso81UviVw6G0bj9WjjkuaDfXzNpGexqteV4iirdk1ZpG-BQ8FzFBswfgOUajHn0EUIOtji2WNgIiiIoLJ6WJNWFcWIKJ7XZ5VUh7b4Vp3pOAuNa2AA397V9HsofrC4aKQa7QfbIOBDC-yLkXUTM_zbegsAPnJzgP38vaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7fc74cda.mp4?token=deXxcsPrewVNEjrI7LluVicpq4YNH4STOvVVEkziQzprRPvxA2wnwNCVAvXLPr5f9iWlJY0rlEU8QrhRcK7NTZeQRlwLEIRAvbIp4i8Jynnk4DH5F7nVdp3ufVIknEV5PjDjretjVBUztZ1Zu83fOjET6yTY_n6WMF3Djy3rD5swnfGBso81UviVw6G0bj9WjjkuaDfXzNpGexqteV4iirdk1ZpG-BQ8FzFBswfgOUajHn0EUIOtji2WNgIiiIoLJ6WJNWFcWIKJ7XZ5VUh7b4Vp3pOAuNa2AA397V9HsofrC4aKQa7QfbIOBDC-yLkXUTM_zbegsAPnJzgP38vaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حمله‌ای به عربستان انجام نداده‌ایم.
🔹
نیروهای مسلح ما به هر هدفی حمله کنند، آن را صراحتاً اعلام می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440676" target="_blank">📅 11:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440675">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حریم هوایی عراق به‌مدت ۷۲ ساعت بسته شد
🔹
سازمان هواپیمایی کشوری عراق با صدور پیام ناوبری (NOTAM)، حریم هوایی این کشور را به‌دلیل ملاحظات امنیتی، به‌مدت ۷۲ ساعت به‌روی تمامی پروازها بست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440675" target="_blank">📅 11:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd7978d06.mp4?token=bhHagxE_QsU584kkvccHnjbHSpcIUzidrywmZkF3WEolBbdX6fCuK6JVxshLtoal01THKkdfKY33tDW49flZgeEVT46Sa3AsV759dS4Lb_i3HXOsApikC_-6yGNCqO54VNyx9SyMAsFaATbeAsILllS071SqSAoluYqPi0u18wqMLLnfwlKkV3Jp5K-Vi3CRqR_57ldUd0ZWcFUEW96VhJ7BUXIcVfnUTec3R9Xsg3HhN2MiMKBeEeIKCQMtg_4eSq2ihisJz6H1Qs00sin6kxDT4pT7fbxI2pcM87LvBsZv9hl0vNSMIoikS47M3zpyjXEizRTFnOzV8g6paMzKDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd7978d06.mp4?token=bhHagxE_QsU584kkvccHnjbHSpcIUzidrywmZkF3WEolBbdX6fCuK6JVxshLtoal01THKkdfKY33tDW49flZgeEVT46Sa3AsV759dS4Lb_i3HXOsApikC_-6yGNCqO54VNyx9SyMAsFaATbeAsILllS071SqSAoluYqPi0u18wqMLLnfwlKkV3Jp5K-Vi3CRqR_57ldUd0ZWcFUEW96VhJ7BUXIcVfnUTec3R9Xsg3HhN2MiMKBeEeIKCQMtg_4eSq2ihisJz6H1Qs00sin6kxDT4pT7fbxI2pcM87LvBsZv9hl0vNSMIoikS47M3zpyjXEizRTFnOzV8g6paMzKDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌عنوان دوست لبنان هر اقدامی که بتوانیم برای کمک به صیانت از حاکمیت ملی این کشور انجام خواهیم داد.  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/440674" target="_blank">📅 11:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc4d44e05.mp4?token=ouFRQtWa2aWmMxZChv5jVvOusUmwqFyvjJ-Zpo3ZgOZ4Kxco56AmqAz4IT8-dKBSHumNecYnuoNR_CQgjNTtxAg5a6EQunGCUdnEUHpgbz_590hjNudTrwGXGuU-NrGoOIRABXEMBQgDNoAQ0UsMx6mKuS7XnJs5aiNa6B-CIrNb_PBaEqDnieUJxHTPNElizYKWvcHwPDuhh-T2HhKj1AmSnxG1ot5Ay5QvMnkdC-c6zNUn2f8dyRlTEByyuQbRw72vMieHYiLx7gUA1gpSsxr-mFBXArYjyN0uJHKRgDXwswNMLVG5ydW9ZJ53xjcpMPgFnUanoefbs-Ietiam2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc4d44e05.mp4?token=ouFRQtWa2aWmMxZChv5jVvOusUmwqFyvjJ-Zpo3ZgOZ4Kxco56AmqAz4IT8-dKBSHumNecYnuoNR_CQgjNTtxAg5a6EQunGCUdnEUHpgbz_590hjNudTrwGXGuU-NrGoOIRABXEMBQgDNoAQ0UsMx6mKuS7XnJs5aiNa6B-CIrNb_PBaEqDnieUJxHTPNElizYKWvcHwPDuhh-T2HhKj1AmSnxG1ot5Ay5QvMnkdC-c6zNUn2f8dyRlTEByyuQbRw72vMieHYiLx7gUA1gpSsxr-mFBXArYjyN0uJHKRgDXwswNMLVG5ydW9ZJ53xjcpMPgFnUanoefbs-Ietiam2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از آغاز آتش‌بس خویشتن‌داری فوق‌العاده‌ای نشان دادیم
🔹
ما با نقض‌های پیاپی آتش‌بس مواجه بودیم و حملهٔ دیشب ما یک اقدام دفاعی قانونی بود. اظهار بی‌اطلاعی مقامات آمریکایی از حملهٔ دیروز به ضاحیه نشان می‌دهد که نوعی تقسیم کار بین آمریکا و…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/440673" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdca724ace.mp4?token=Ih7Ibj217_5PR2QErbs1cyrweL9vz40Ty3qu-ZOAeppmztZl9n-rGCZ45ePlN2BEFLJ1jKjkkKJW3w5FCiRnm0kYM_bPki68CI9wq7B4-haOdFKU7Ip1vWISvhBjHTSpXtBAYcgpxHGkRJQxxuUvUw1q0Zm_d3gWPc-d5gzFE5Jm0-n6KcRDIIMMNVDf6GxHLaV2s1iiyKuhvYIibl3UE7u9i6kaIq5UmWtxQeTacYsQtcnKAVofU5AE_sT8OwyyiTT3Zj8bv3LKjfZFHzDtx_Qf3-ntZpRLMyOmvqB0OPd20W-9p58c3RMjWVLGsgDfOQv1qMcQrqpPOqnl1M2dLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdca724ace.mp4?token=Ih7Ibj217_5PR2QErbs1cyrweL9vz40Ty3qu-ZOAeppmztZl9n-rGCZ45ePlN2BEFLJ1jKjkkKJW3w5FCiRnm0kYM_bPki68CI9wq7B4-haOdFKU7Ip1vWISvhBjHTSpXtBAYcgpxHGkRJQxxuUvUw1q0Zm_d3gWPc-d5gzFE5Jm0-n6KcRDIIMMNVDf6GxHLaV2s1iiyKuhvYIibl3UE7u9i6kaIq5UmWtxQeTacYsQtcnKAVofU5AE_sT8OwyyiTT3Zj8bv3LKjfZFHzDtx_Qf3-ntZpRLMyOmvqB0OPd20W-9p58c3RMjWVLGsgDfOQv1qMcQrqpPOqnl1M2dLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تبادل پیام‌ها متوقف نشده بود و حضور وزیر کشور پاکستان هم بخشی از این تبادل پیام‌ها بود.  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/440672" target="_blank">📅 11:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b45b849b.mp4?token=ESpyaLMIro-2zbOXgaWAKqjwZzhgX64PI6GsEroohfNurPmFp1zU7ifRxdV9eJW5r3xsPGjoJzhJult_hy3ge2xmICCqFTz3eWR4Rp4cgaOrdHCnX1Ci0L0cVlRGCN4j6Gw2fDkIs1zXtAoM24oSAvCSOS3bGDFam1CQv6iigrlMzzr3KeFQiVwMxXMxleT_FltfbtXwUzBPmHYPVYEKjTQGB2CSCtgSlQh-jhJTnR_EyyTwQ0YVen-_kau6uKKb9UtdywqEV-MitlRBk5ImDWK4W7QaJzpzw6mRSmdM3h-nX8uqubqna-kVKTL3r8X-NcuUsii7A6uUD8YSn6SPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b45b849b.mp4?token=ESpyaLMIro-2zbOXgaWAKqjwZzhgX64PI6GsEroohfNurPmFp1zU7ifRxdV9eJW5r3xsPGjoJzhJult_hy3ge2xmICCqFTz3eWR4Rp4cgaOrdHCnX1Ci0L0cVlRGCN4j6Gw2fDkIs1zXtAoM24oSAvCSOS3bGDFam1CQv6iigrlMzzr3KeFQiVwMxXMxleT_FltfbtXwUzBPmHYPVYEKjTQGB2CSCtgSlQh-jhJTnR_EyyTwQ0YVen-_kau6uKKb9UtdywqEV-MitlRBk5ImDWK4W7QaJzpzw6mRSmdM3h-nX8uqubqna-kVKTL3r8X-NcuUsii7A6uUD8YSn6SPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ادعای ترامپ دربارهٔ آزادنکردن اموال مسدودشدهٔ ایران ادعای مضحکی است
🔹
ما از هر طرفی که نقشی در تجاوز علیه ایران نقش داشته طلبکاریم و این طلب را به هر نحو که بشود نقد خواهیم کرد. هر تفاهمی صورت بگیرد، آزادسازی منابع مسدودشدهٔ ایران جزوی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440670" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df649b271.mp4?token=Ze0siHXhpCPWwYBVGvXrA4L2vumptCAHmabtK8rlikilPeQP_3sDiXD6QAX42kn6ZfP3G4DmCgAABZvT1gm9My-jQQ27AjXeD5je8hf3u5Lwyzr0bw_uq_D1ZJ2ztkgCjIn_QS3v65a_gWOo8UElWlR2NHdq-jTAVYchrH8-3lt0P2PMmNWe8k-kWSmHqVqcjW_Pzsalfdu6B0H1tIplpPxVV8MZfcZ3S1ZtCLUGqrB4RRlfS7WOEr5FEtzM2C_NVCQ5ftiu4uD4jkdDRhg-KeZOzBxGojIcFP82QpygNyRbgKxM1T6t5qCGPRaZOeVIH2IpTchBtGGYo3iIg0HZAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df649b271.mp4?token=Ze0siHXhpCPWwYBVGvXrA4L2vumptCAHmabtK8rlikilPeQP_3sDiXD6QAX42kn6ZfP3G4DmCgAABZvT1gm9My-jQQ27AjXeD5je8hf3u5Lwyzr0bw_uq_D1ZJ2ztkgCjIn_QS3v65a_gWOo8UElWlR2NHdq-jTAVYchrH8-3lt0P2PMmNWe8k-kWSmHqVqcjW_Pzsalfdu6B0H1tIplpPxVV8MZfcZ3S1ZtCLUGqrB4RRlfS7WOEr5FEtzM2C_NVCQ5ftiu4uD4jkdDRhg-KeZOzBxGojIcFP82QpygNyRbgKxM1T6t5qCGPRaZOeVIH2IpTchBtGGYo3iIg0HZAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: تجاوز دشمن به صنایع پتروشیمی را پاسخ دادیم
🔹
سپاه پاسداران: رزمندگان نیروی هوافضا، در پاسخ به تجاوز دشمن آمریکایی‌صهیونی به یکی از صنایع پتروشیمی، دقایقی پیش صنایع مشابه در حیفا را هدف حمله موشکی قرار دادند.
🔹
اخطار می‌کنیم؛ دشمن صهیونیستی با اقدام…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/440669" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/440668" target="_blank">📅 11:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28575da85.mp4?token=uoyw8aHJ-N1e61w-Pf0A0Ag5OTodB2Uy1CLtTZC5idfRYYhTtr10zSbpnhlQlM1XABLQWZMC_PVDJhTYbOY-tYjRXUCHfAFh-FM3p14woFdPnELDsx5B0ii0-YSZUKQB8QF9_xKPT2lg1aHdUt0ZOGXSeBPNvSVfofVxRfpiU418-eO8YU_WGt8Ra-YuMvXtXDAMR-qOsrgsAARPmS05M0BpMY6sQwg_GaibYuCa2SDIJ5Grj6e50uT50Fodrrh9Exj7Vwi1J6DmETiFZlfRA9VW-UQsQRLl-XcFpwCb1RcM2GfF_QtikKCpBuwYrb70BrG9-vguX0XcTGxyxammcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28575da85.mp4?token=uoyw8aHJ-N1e61w-Pf0A0Ag5OTodB2Uy1CLtTZC5idfRYYhTtr10zSbpnhlQlM1XABLQWZMC_PVDJhTYbOY-tYjRXUCHfAFh-FM3p14woFdPnELDsx5B0ii0-YSZUKQB8QF9_xKPT2lg1aHdUt0ZOGXSeBPNvSVfofVxRfpiU418-eO8YU_WGt8Ra-YuMvXtXDAMR-qOsrgsAARPmS05M0BpMY6sQwg_GaibYuCa2SDIJ5Grj6e50uT50Fodrrh9Exj7Vwi1J6DmETiFZlfRA9VW-UQsQRLl-XcFpwCb1RcM2GfF_QtikKCpBuwYrb70BrG9-vguX0XcTGxyxammcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به دولت مصر: ۳ سال برادران و خواهران شما در غزه تکه‌تکه شدند اما شما کاری نکردید
🔹
ما مشکلی با مصر نداریم؛ اما این که مصری‌ها بخواهند با تهدید یک کشور مسلمان تحت تجاوز رژیم صهیونیستی کسب اعتبار کنند، تأسف‌بار است. @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/440667" target="_blank">📅 11:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdbbc4f19.mp4?token=IQfW-WVdAKK68PJ_jcHL6_6UIQCy3-OxgmVMcbfg-dqzKGnvOMztjj3CIlPTZ4O1VErygR461zUfuS5dp6vFMh6-RNFpxPJRqcaFQJrU1judhDjzaeAiL4J8RKlY29xPH0RW4b68F-uVq0UpXNhM9OMYv1zy3hEamalaPq5nhzFbvbTQnuuqy07F-kZ6DpeDzbzC_RGHCZ9bzgZpPH7G4DZK4DzR6tfRj9l58ur8LOQkXcNix6Db_tkiFLIeUikqTZzeT3a3HX4lgCAziW7f8lbQ1kFO8h7sqUP2MaDERonNFXj4Qow18vnpaM3bomlDngbad4BA5Rv0VSxA_HFeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdbbc4f19.mp4?token=IQfW-WVdAKK68PJ_jcHL6_6UIQCy3-OxgmVMcbfg-dqzKGnvOMztjj3CIlPTZ4O1VErygR461zUfuS5dp6vFMh6-RNFpxPJRqcaFQJrU1judhDjzaeAiL4J8RKlY29xPH0RW4b68F-uVq0UpXNhM9OMYv1zy3hEamalaPq5nhzFbvbTQnuuqy07F-kZ6DpeDzbzC_RGHCZ9bzgZpPH7G4DZK4DzR6tfRj9l58ur8LOQkXcNix6Db_tkiFLIeUikqTZzeT3a3HX4lgCAziW7f8lbQ1kFO8h7sqUP2MaDERonNFXj4Qow18vnpaM3bomlDngbad4BA5Rv0VSxA_HFeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: گروسی همچنان رویکرد نامناسبش اصرار دارد
🔹
در صورت صدور قطعنامه در شورای حکام آژانس انرژی اتمی، به آن پاسخ مناسب خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/440666" target="_blank">📅 11:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پروازهای فرودگاه هاشمی‌نژاد مشهد لغو شد
🔹
سخنگوی فرودگاه‌های خراسان‌رضوی: با توجه به شرایط پیش آمده کلیه پروازهای فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد لغو شد.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440665" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17be14ac20.mp4?token=aYBI67nQJWtKNrucbJdsL704q9UY7XsQbLiZms4uteIQIDHVt1gWwDxNiyVBtQvPnn0X6FMRQy4yW2pcCVAp_Y_1K9Go_fhRY_s3lWDGzlBi1SND3gIh3kqyVBrhNjxn4NvfivUEHkMq-yV12PPvf1fptXfJ6FRMyjvd4AT0iQ91T1nhHNpccNjux-oAkXSyDMOu4yTvKD4INd2bbMak7RczriXUvCnJmWUZd2nki8_PvEGzINJDneSB4krZzLoaMMHgjx4y7m0-kNdF4Z5HXtjtGKJr2lEPG7dqpYIhwywSXP2JR7DjoC40OcirAltFMtIzd4faZsJ9thVBDLdEsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17be14ac20.mp4?token=aYBI67nQJWtKNrucbJdsL704q9UY7XsQbLiZms4uteIQIDHVt1gWwDxNiyVBtQvPnn0X6FMRQy4yW2pcCVAp_Y_1K9Go_fhRY_s3lWDGzlBi1SND3gIh3kqyVBrhNjxn4NvfivUEHkMq-yV12PPvf1fptXfJ6FRMyjvd4AT0iQ91T1nhHNpccNjux-oAkXSyDMOu4yTvKD4INd2bbMak7RczriXUvCnJmWUZd2nki8_PvEGzINJDneSB4krZzLoaMMHgjx4y7m0-kNdF4Z5HXtjtGKJr2lEPG7dqpYIhwywSXP2JR7DjoC40OcirAltFMtIzd4faZsJ9thVBDLdEsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آتش‌بس به‌طور مستمر و مکرر توسط طرف‌های مقابل نقض شده است.
🔹
ما هر وقت لازم بدانیم برای دفاع از امنیت کشور اقدام خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/440664" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440663" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e040c786b2.mp4?token=fjfIqJ47tjwbAKYJEFQp2MmjypWSv6N-dB4EMyJtF2heg9ogtm9Iu6zFU6ydObBP5SGo57mHSIsgHq5S8CAscnNOTfEPE9Fqcs4Q91jEJoKb0XJZjfNgzbbOgKPUXBNn-Ax16-viu19hZXkjkbfTrmlXJNeG_Rm3kCQ2OodhSRZrn3qWMC769CNHC1TdyuQWnV75UiqDIm43mS3E-E-wrCNS0yZONsLZaxTxjs3xCrIYjuxWI71SjekUOrJqkpDS08ewnXLswOI11mP5s315V7gUmkRxMCyK6rGbhpbwWIV6ju27x1NC4z8zrmfWII19By74S3jierWNfHSMvR3czw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e040c786b2.mp4?token=fjfIqJ47tjwbAKYJEFQp2MmjypWSv6N-dB4EMyJtF2heg9ogtm9Iu6zFU6ydObBP5SGo57mHSIsgHq5S8CAscnNOTfEPE9Fqcs4Q91jEJoKb0XJZjfNgzbbOgKPUXBNn-Ax16-viu19hZXkjkbfTrmlXJNeG_Rm3kCQ2OodhSRZrn3qWMC769CNHC1TdyuQWnV75UiqDIm43mS3E-E-wrCNS0yZONsLZaxTxjs3xCrIYjuxWI71SjekUOrJqkpDS08ewnXLswOI11mP5s315V7gUmkRxMCyK6rGbhpbwWIV6ju27x1NC4z8zrmfWII19By74S3jierWNfHSMvR3czw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440662" target="_blank">📅 10:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عامل تروریستی شهادت شهید یوسفی در زاهدان دستگیر شد
🔹
معاونت اجتماعی مرزبانی سیستان‌وبلوچستان: در عملیات اطلاعاتی مرزبانان در شهرستان زاهدان، عامل تروریستی شهادت شهید یوسفی مامور انتظامی شهرستان خوسف خراسان‌جنوبی در شهر زاهدان دستگیر شد.
🔹
عامل پس از چندين روز کار اطلاعاتی، توسط مرزبانان سیستان‌وبلوچستان دستگیر و یک دستگاه خودروی هایلوکس نیز از وی توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440661" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440660">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=S9BWX081feu1k74-ys7NfKFggyiW-L5InMOlQUaJmiPTjq7rL84YzZOyLGP1iXwBTgM65i7qyp8a_cRwHaS5Zt7w-EQ0VMrbfGemSuHIwRWMVSqrBeYHajorg2Mb7PTaxAj0JAhpDCDxY507f8xGn2Oc94-pZg6rTr59i9hG5ibvNqGkD0sCi2tUaiyzc-jhTxdkxiNANMywl_ZNiDaJNBKzf5GfVNn9E52uwtJUkx-4hF_vzRnR8f5AIVkYmC89LOsUKYhUq9DQMWpofpjAQ_U-qyDJzJ0C3qoPftbZ6QqBMX6Z-GdB8cLWIvN70Y7OMtrdkprI7T3KWTd2tZroOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=S9BWX081feu1k74-ys7NfKFggyiW-L5InMOlQUaJmiPTjq7rL84YzZOyLGP1iXwBTgM65i7qyp8a_cRwHaS5Zt7w-EQ0VMrbfGemSuHIwRWMVSqrBeYHajorg2Mb7PTaxAj0JAhpDCDxY507f8xGn2Oc94-pZg6rTr59i9hG5ibvNqGkD0sCi2tUaiyzc-jhTxdkxiNANMywl_ZNiDaJNBKzf5GfVNn9E52uwtJUkx-4hF_vzRnR8f5AIVkYmC89LOsUKYhUq9DQMWpofpjAQ_U-qyDJzJ0C3qoPftbZ6QqBMX6Z-GdB8cLWIvN70Y7OMtrdkprI7T3KWTd2tZroOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440660" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440659">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893570ccfc.mp4?token=tBXd-X6y2d7bHlY5T4LFSd1uScrG0dYiS1yBPG0cejl8f9xR6f0FxFncnwDmJ0DOcbu4nos6ZrtzCAxDWXwz78GSc324oMG0Iay7cYxlTV4sCvmFLLQGDomo1DM99y9GQHaLrezBjh_ZHytg_MS_Syz9zHDC77KEBIsc9jsTXd-1_AGi-ua5Zn7KUMgV12rDCCpvl4LLDDdaHR7cXh5_3JIZwDN8h9XzlT3Iqgk04gSAtRIZoxRQS6ntmonIdpPvorWa1zPIKGR6RYVVEWE9FC2kWITnSjWI4s0y1fX9tn0EAwCH5LlJ_0Vly87PIAgq4WQBnEtBziXSXH4HPuVnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893570ccfc.mp4?token=tBXd-X6y2d7bHlY5T4LFSd1uScrG0dYiS1yBPG0cejl8f9xR6f0FxFncnwDmJ0DOcbu4nos6ZrtzCAxDWXwz78GSc324oMG0Iay7cYxlTV4sCvmFLLQGDomo1DM99y9GQHaLrezBjh_ZHytg_MS_Syz9zHDC77KEBIsc9jsTXd-1_AGi-ua5Zn7KUMgV12rDCCpvl4LLDDdaHR7cXh5_3JIZwDN8h9XzlT3Iqgk04gSAtRIZoxRQS6ntmonIdpPvorWa1zPIKGR6RYVVEWE9FC2kWITnSjWI4s0y1fX9tn0EAwCH5LlJ_0Vly87PIAgq4WQBnEtBziXSXH4HPuVnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها با پرچم ایران به استقبال تیم ملی رفتند
🔹
جمعی از ایرانی‌های حاضر در مکزیک و بومیان تیخوانا با در دست داشتن پرچم ایران به استقبال تیم ملی رفتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/440659" target="_blank">📅 10:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5w5YkY31W3UbkPgKSq-2HzLqS73d8RVXU9DL2ksixl1NW0_mip7wDCwX7UQ8EnQt6Ug9Ok8XRy3qcuQiORiMxy1Lyi6PQm-lPP7EOQ1JoOejRkYCMtnQ8Vm4E_HCRlMpLheABml6u4bXLimKODqHih2Ig7ymaeAakCKeJP6baek_KCulHULjKZaljXAiVlqShNL3WhuN6poVKdiWdNA6duQh3LzgMJJK8egXn9ZlIMZjhdXEMxh3-41Badb0vf90PgiCYZWIxCwga0u8MaTZaOQHFye4yIWff0iVO0KcPxYnztRlwMDfRONM1Lb_KDD56ijT6prDqsituEFV2K2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ خواهران منصوریان به رئیس فدراسیون ووشو
🔹
فدراسیون ووشو در بیانیه‌ای اعلام کرد که پس از شکست سهیلا منصوریان مقابل رقیب خود، خواهران منصوریان به رئیس فدراسیون ووشو حمله کرده، به او توهین و اقدام به خودزنی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440658" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
