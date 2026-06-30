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
<img src="https://cdn4.telesco.pe/file/YfYmMYGlAljqFMpz_7R2JV81bwOUIDkDdeyey4huGmcQ0afAsCg8QLoi3VayvyQo69aulDPI_lzzPp5dt8uwk0_JBK4TAueq2iadNzoqLCJAA3-rUXCJiZ11HUQjQCt4eK__zrOSazy3-e47cfCfhyuVCDHB11p9DRRfsvoC391PDpAwiUyHqx5Y-xZYO1xatqjcnKyNme8AJUbKWdVT-VLuQUSpfpLrrYD3cwk7zi9-DRDoXelNnvkUwyhA6K_ECiN2UH19lKvt6yNxg52bQJE62M2TeA9p-ZLELDPDJsFIb06Bkov47iybr45KfWBa_xG6X31rhznsnt-RZD-kHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-445611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/farsna/445611" target="_blank">📅 13:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2GWgajw-Xg5N2OJ0DWI48mVbe1i1AA5rU3SqxZBAQvGtj_k26LQ-4Zoa-6llRySw2d0CTmEPYftSEXvExu8jX09pMBu-ABjaotE1ZaP5AF0OpzuFTCl4WZE7d6bsiKmxQ0z_YnO56MKiXbBWkRutZ0j2iEuLZe9oPXFED5dOnHcMfYPBJGlmbNrFie4QLsc8Mfojd64qybq4mT7DC9c8umSjOGcxP3A1WkUXAzE6ACdhEhfaQwbGuQaTBgq8_M51YTknmWMiUox2bU8zzuQtKE7GsEEAaIjY1fCFuDRMIZcIvuoT8I-VtafZmDx_D8IwoM11DATscSFDYH8ob0GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج تودهٔ ۹ کیلویی از یک بیمار در شهرکرد
🔹
منصوری، متخصص زنان‌وزایمان: در عمل جراحی یک بیمار ۴۹ ساله در شهرکرد یک توده به‌وزن ۹ کیلوگرم خارج شد؛ این جراحی با موفقیت به پایان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/445610" target="_blank">📅 13:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Q2ur1TrjKD1PDVwfAE6P3vS9tRK82ViUdl49_g-HzH25sJ46I1gpNWy21FW7jcRBgKwIezI_A8Eyf_PY9fmSjERbRcljDv1F19rcT1olmldRAQ5w1kFsLlR1_f-sx0IAtaF2mzcyDMKz-uB_QC7B2zvJACgT66lXUSpV1RHJFJxb2Gx2XmRDimc6B3ylrvf8pQ1K9kLVq5seYgjNIKqG3ajAOHyXgv5wPGyKbzS1Gp91Pl_4V4ABOP31TaBQ1LNgE_2jizpvxPkkQ3kFxt45KuDiw_fBvp_g3236Wkg9UVwqJF9tMY1LyF4CEof6ojq0Cnt5aVEcOiMWDx0EuT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺️
#پوشش_بیمه_ای_زائران
و شرکت‌کنندگان در مراسم تشییع رهبر شهید
🔹
صنعت بیمه کشور در راستای ایفای مسئولیت اجتماعی و تامین آرامش خاطر مردم، تمامی شرکت‌کنندگان در مراسم وداع، تشییع و تدفین قائد عظیم‌الشأن انقلاب را تحت پوشش کامل بیمه‌ای قرار می‌دهد.
🔹️
به گفته موسی رضایی رئیس کل بیمه مرکزی، کنسرسیومی متشکل از ۷ شرکت بزرگ بیمه‌ای (ایران، آسیا، البرز، دانا، سامان، نوین و آرمان) تشکیل شده است تا پوشش‌های بیمه‌ای لازم را در چارچوب قوانین و مقررات مربوطه عرضه کنند.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/445609" target="_blank">📅 13:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGc7mRlz6-hJHu5CAUieMlL8hbNRXxfb6q7lfbTKgC0OlnC86zXOznZVp2N-6MU7NXI388f0nWmWwPdzdhJIbgjxO4VTPPFuJy4nCdvnXGzGGdWQZ1A3i42x2mw3oBc7Ev3yJQK1AdQ509O5vBcu43rebC3lxDJGd04ujDPSRMxjXr5-J4_wWEAbu64_f5pt6JUcKO6pPmY5JVYoScBDOVvq5yoi1EOejwtqBQJVJUEmWdzbfdMQIjPVkTqclGhC2m72b4sfxt9BjvOXsN6gx4ySQDhtPF7n4txH_tfNkw444pYBlgEuo3Fav6130AI9CbuGOkX-P7XqaIJsdSrDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت بانک ملی ایران از توسعه همکاری‌های مالی با پارس‌خودرو
معاونان ارشد بانک ملی ایران در بازدید از شرکت پارس‌خودرو، با اشاره به ظرفیت‌های این مجموعه خودروسازی در سطح ملی و منطقه‌ای، بر حمایت از برنامه‌های توسعه‌ای، تأمین مالی زنجیره‌ای و تقویت همکاری‌های مشترک برای رونق تولید، اشتغال‌زایی و نوآوری در صنعت خودرو تأکید کردند.
بیژن نصرتی، عضو هیات عامل و معاون بانکداری شرکتی بانک ملی ایران، در این بازدید با ابراز خرسندی از حضور در پارس‌خودرو اظهار کرد: «خوشبختانه امروز از نزدیک شاهد پیشرفت شرکتی هستیم که یکی از نمادهای خودروسازی ایران، منطقه و حتی جهان به شمار می‌رود.»
جزئیات بیشتر:
https://news.parskhodro.ir/news-archive/id/5082
#پارس_خودرو_توسعه_تولید
➡️
@parskhodro_pk</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/445608" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/445607" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445606">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/445606" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445605">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/445605" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445604">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس راهور: از هموطنان درخواست می‌کنیم در صورت امکان از خودروهای شخصی خود استفاده کنند
🔹
همان‌گونه که هر سال در مأموریت بزرگ اربعین با محدودیت ظرفیت ناوگان عمومی مواجه هستیم، در مراسم تشییع رهبر شهید نیز در هر ۳ شهر تهران، قم و مشهد چنین شرایطی وجود دارد.…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/445604" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445603">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twga028AO3x1m9qxm6h2KokxTm6ZHSTD2RlalBM3raG1jmhxQ7mHZTg2GS1triUhedwknyzs6Reh0709udKWahu7NxuWr3axmNy4p5EumM2rcl9g0USEfzoUgwNxSYlzku2mo9ziejPkDzS5fqfKWU0bJK6ETCzFCLXhY4vfgTh1kNc4TCeOW0eb8moJqnUtTMpamK4yU9OmqrgI0m86igRDsMIs4TifSjo5tBh5uHdE855KJwmDrJyJ3hxXYbN8Q9JeQudsPdr9RKDoPRXcVDDRhVtOjwYivh7Q8HFxE6DgV2eizg6yskXi-mwyHOPqKNUdo3dfE1JHGn7iaNlYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/445603" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445602">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمادگی مردم قزوین برای میزبانی از دلدادگان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/445602" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjDiMGoC0t18B9LuZIJevp7K38NpHtjcgKWaZO7boFdWsV5cnArzCkgQugfDKoT10Ntx04EvGVfcTGNIECkRkT8Bo2CCPMdRzdEdpSFga_6_ALHHrme-FZd6C9ztGkd5A91yzQBqEatM8rB8jgUKuqyLfbYxDHLvdV5U3s-hwRavRls8yGdKcEMT_HYd2mfD5oT-9FSv9Ckvj5U1I4IC3nTHAkb2nW_qzBAJYOlRgPcw3FP9Y8mnF_Xk0kvSLXXwpyXkuiM8m2DNjmikV33keaDELoS6Tp_neaOCvt6jh_R5TaXdUO5g47VbQPuj-PHcTpaqlAWsxVRgzQ_JMtnNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش‌از یک میلیون ظرفیت اسکان برای تشییع رهبر شهید در تهران
🔹
استاندار تهران: برای مراسم تشییع رهبر شهید در تهران، حدود ۷۰۰ آمبولانس، ۳۸ اتوبوس‌آمبولانس و ۳۰۰ موتورلانس در مسیرها و نقاط تجمع مستقر خواهند شد.
🔹
همچنین بیش از یک میلیون ظرفیت اسکان در اماکن عمومی آماده شده است؛ برای مقابله با گرمازدگی نیز اتاق‌های سرد در مناطق پرتراکم پیش‌بینی شده است.
🔹
بیش از ۶۰۰ خبرنگار خارجی برای پوشش رسانه‌ای مراسم حضور خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/445601" target="_blank">📅 12:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445600">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/445600" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445599">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7BlMv3F9eHVHpZ2gtL_GIfB3_2oVZxCL3yvDdmmy69zVPtGKxJfTuI6L_hhTYQaojHt1d-lwbZnTPcnGpzdmFsmrBhNBszlPaipzqL7Tt2DeRL9N5mIGluUfO7dIHWVEcCVgQpqtXyvd4MOEVymeKkCjZdAKO7haYT71oLNqG1_Ab3vPtjcIFZpupJhF6LhIF-cEiBgkHyFfn_c_n7L5BkBO8WAkiCPMpNLFbZMy8O-lB00eQAm8bFcliNC3SKz2lvKlBS3V6BTo2O_H1xlYDjynfpBt_ynwrnUxsAkMfs8mV5VPxRL1efArOh1_h9BzklJoYBV4rVPOcm2opv78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متلاشی‌شدن یک گروهک‌ تجزیه‌طلب در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه: درپی ورود یک تیم از گروهک‌های معاند و تجزیه‌طلب به مرزهای شمال‌غرب کشور برای اقدامات خراب‌کارانه و تروریستی، این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به صورت کامل متلاشی شدند.
🔹
این درگیری در ارتفاعات مابین شهرستان‌های مهاباد و پیرانشهر و با پشتیبانی آتش ادوات صورت پذیرفت.
🔹
در آن درگیری، این تیم ۶ نفره به‌طور کامل منهدم شد و اجساد ۴ نفر از اشرار به همراه انواع سلاح و تجهیزات در اختیار رزمندگان اسلام قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/445599" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
🔹
در حالی که این دونالد ترامپ بوده که برجام را پاره کرده و از آن خارج شد، اکنون مقامات دولت دوم این رئیس‌جمهور اذعان کرده‌اند که برجام «یک توافق واقعی بوده» و تفاهم‌نامه جدید با ایران قابل مقایسه با برجام امضا شده در دوران باراک اوباما نیست.
🔹
کاملاگر داو، نماینده کنگره آمریکا، بخش‌هایی از صحبت‌های تلفنی روز گذشته وزیر خارجه آمریکا مارکو روبیو در مورد تفاهم‌نامه ایران و آمریکا را افشا کرده است.
🔹
به گفته این نماینده آمریکایی، روبیو در این گفت‌وگوی تلفنی تأکید کرده که «این تفاهم‌نامه فقط یک تکه کاغذ امضا شده است که می‌گوید ما به صحبت درباره صحبت کردن ادامه خواهیم داد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/445598" target="_blank">📅 12:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: مراسم اقامه نماز و تشییع پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود
🔹
نماز توسط یکی از مراجع تقلید در مسجد جمکران اقامه خواهد شد.
🔹
بسته به فراهم بودن شرایط، مراسم تشییع نیز در شهر قم برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/445597" target="_blank">📅 12:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴ تیرماه نماز بر پیکر رهبر شهید در تهران اقامه می‌شود
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد.
🔹
پانزدهم…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/445596" target="_blank">📅 12:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پورجمشیدیان: تاکنون بیش از ۳۰ کشور تقاضای حضور در مراسم ادای احترام به پیکر رهبر شهید را داشتند
🔹
سران ادیان و مذاهب و دانشمندان بیش از ۹۰ کشور  اعلام آمادگی کردند که در مراسم حضور پیدا کنند.  @Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/445595" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/445594" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzR8mD4y_qnWzm-ZUXEMfd5AkidCTafnjIeNZxN0Mz2VK2pcinhQurCTJem-kAMvJ0jaMP-XxHe36-nphvoLtJVn2DqZ77zreeH2mgig1T_ac6I39r99N4mLwhPfCwm9sheJGozFy37N7bs8n4O35Q4dXGEw2UCYTrnT3XmZ6ejoLsyYUx8xZouRAZDf7HfBXg5yXkPxe7M2zlU5JxK4RSQKtaCFbTTOKdcikPybOA80155XmqlPkvsEB8LHgK-8oJSHvZ4jCD4eGJkQXgwbBTmaniRGtDYwNQTynWEO9NEr19BHnj-lk2U7VdbUVUKoz-URpHOdNWT0Cp4I-ljqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزاد جمشیدی، مجری تلویزیون بر اثر سکتهٔ قلبی درگذشت
🔹
بنا بر اطلاعات منتشرشده، جمشیدیِ ۵۶ ساله بدون سابقهٔ بیماری و در اثر سکته فوت شده است.
عکس: امیر رستمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/445593" target="_blank">📅 11:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت معظم ایشان و رهبر جدید انقلاب اسلامی، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، ظرف روزهای آینده برگزار خواهد شد.
🔹
برنامه‌ریزی این مراسم ابتدا با لحاظ ملاحظات شورای عالی امنیت ملی و سپس منطبق بر دیدگاه‌های دفتر و بیت شریف مقام معظم رهبری تدوین شده است.
🔹
در همین راستا و با مصوبه هیئت دولت، «ستاد ملی برگزاری مراسم وداع و تشییع قائد اعظم امت اسلامی» به مسئولیت و محوریت دکتر عارف، معاون اول رئیس‌جمهور و دبیری وزارت کشور تشکیل گردیده است.
🔹
این ستاد با مشارکت همه‌جانبه نهادهای دولتی، نظامی و تشکل‌های مردمی، مدیریت و اجرای این آیین باشکوه را بر عهده دارد و جزئیات برنامه‌ها به‌زودی به اطلاع عموم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/445592" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای پارک خودروها.pdf</div>
  <div class="tg-doc-extra">1.2 MB</div>
</div>
<a href="https://t.me/farsna/445591" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
خودروهای خود را
در مراسم بدرقهٔ آقای شهید کجا پارک کنیم؟
🔸
۲۴ پارکینگ با ظرفیت بیش از ۲۰۰ هزار خودرو در مجاورت ایستگاه‌های مترو و اتوبوس برای مراسم تشییع رهبر شهید در تهران در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/445591" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی قوه‌قضائیه: ۱۵ نفر از زندانیان اوین متواری هستند
🔹
بعد از بررسی‌های دقیق و آزمایشات دی.ان.ای مشخص شد که ۳ نفر از کسانی که فکر می‌کردیم از زندان اوین متواری هستند در بین فوت‌شدگان بودند لذا ۷۳ نفر متواری شناخته شدند.
🔹
۵۸ نفر به زندان خودشان را معرفی…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/445590" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445589">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/445589" target="_blank">📅 10:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/445588" target="_blank">📅 10:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445587">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارجاع پروندۀ تخلف یک بانک دولتی به دیوان محاسبات
🔹
در بررسی عملکرد شرکت‌های زیرمجموعۀ یکی از بانک‌های دولتی ناتراز، مواردی از عدم رعایت صرفه و صلاح دولت در اجرای تکالیف قانونی مرتبط با مولدسازی دارایی‌های مازاد شناسایی و پرونده جهت رسیدگی به  دادسرای دیوان محاسبات کشور ارجاع شد.
🔹
بررسی‌ها نشان می‌دهد در فرآیند انتخاب کارشناس، قیمت‌گذاری و تصمیمات اتخاذ‌شده برای تهاتر دارایی‌ها، اشکالات موثری وجود داشته و در یک مورد بالغ بر ۱۰۰۰ میلیارد تومان انحراف در قیمت احصا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/445587" target="_blank">📅 10:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445586">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/445586" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445585">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCZUHxq4WWJMZ_q_96WHn-9qyTkNZonfQLxkUjqDOKPsaRoetrVhQMw0w8UjJccV2vKKsYv4ZB_qWuecd4xg6k-ATNVyOEr7q7We-uExlmOxS89esA81iLLIOtF5p1E3QTyntsVZnrn2vuybzLkTGSIovqdIoi9PWSFxjD_H0qCgx9Uyj0Z2QvQvoAu4xc-9iEdbJiUqCC1BgWwXeGnaQowuTEMpKJDwuwLqOiN8I02cN0znQP6VZpAYFRZh3dbJ864Z4xl9Jsn9r2dcjxK7QlCyaGNIFr6P05OBuOkt5Fk-JBWt1rJTuhrAQ9LIY1XPDogfxfaAoB_p_NjAA2dLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌ شورای‌شهر تهران: شایعهٔ مسدودشدن ورودی‌های تهران برای مراسم وداع با رهبر شهید صحت ندارد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/445585" target="_blank">📅 10:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445584">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZw9AF6XTjt94GcU3yot5gtuAVb_eAnMfFhyXTsNC_J5ch7DUFMS70YXna2q6bddlj6U0boFmsANn06207fkRop1DPqVvPyV1w1uYJlhLza0ToRwn7cMOYXY5TiAPAtXj7olzz_G1XqfgFXm-CwOpJC1iClDe94xZ3FDCgm6X1fHJzwL2YhHBNHQAal41ZhNo1exf52MHYmaDhebfhzNWbm91a8lIqCk_tJCCr1clgQtv2cKO87YOtfKosMUAHEJs4_QLxA-qSBR6mfCu1t7YZzYsW348yyyygGzsL8YsfBj4fyw_sXCsedXl9z2vP5zFIvoA93ylhNbmusf_FQWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: بدون تردید به نقض آتش‌بس پاسخ می‌دهیم
🔹
سردار ابن‌الرضا در گفت‌وگوی تلفنی با وزیر دولت در امور دفاع قطر: با اعتماد به برادرانمان، به دشمن اعتماد نداریم و دستانمان روی ماشه قرار دارد و بدون تردید، در صورت هرگونه نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت.
🔹
تنگۀ هرمز نباید مورد سوءاستفاده کشورهای فرامنطقه‌ای قرار گیرد. حضور نیروهای بیگانه نه‌تنها امنیت‌آفرین نیست، بلکه موجب افزایش سوءتفاهم، بی‌اعتمادی و ناامنی می‌شود.
🔹
حمایت‌های آمریکا به جنایت‌های رژیم صهیونیستی در غزه، سوریه، لبنان، قطر و ایران موجب تداوم حیات و گستاخی این رژیم شده و موجودیت و حیات آن در گرو ایجاد بحران و تنش در منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/445584" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع رهبر شهید نگرانی اینترنشنال شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/445583" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamW718f-oLttuZHx4KnSsnou_rMsH6ZQ7eZgPSsjRA4fRhdchkPQdLO_OXR3IqeiRLDASBRrpqt-HNjj2oium6YXqIThm5uqWT1VDjZ6tHD0RHQ2ToT_Hbu3LFvvzxc9tE32c3D4_ekFJQT9P8CG2zgHsCWc0UnuSQWiv__gFJBjI8rtoEBvZMpWb-Ztyw8TlNWmrRkxGtjpBrNu8aIZceH_1GiqCnxiRAA6CBHqjdMxgQvkdOi6WqZhRYxVVxQTdMXXzP1twiQYl_NohBqnJ6HIdv7fBWFlXyi6Tr3xqrOLwzoFA76aAjZ7jVhaP8-uBrp4v-OdIRWVp3S6xNDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌ به جان پالایشگاه هندی-آمریکایی افتاد
🔹
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔸
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/445582" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445581">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات جنگنده‌های اسرائیلی به جنوب لبنان
🔹
منابع خبری گزارش دادند که با وجود توافق دولت لبنان با رژیم صهیونسیتی برای توقف جنگ، جنگنده‌های این رژیم شهرک «دیر سریان» را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/445581" target="_blank">📅 09:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445580">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNM7TORR2Tee5LaCxaEO5wpxQB7Z4B68pD6h30OrpDaPtSfksvDPzXrW7ddrCOGOFpPkmIepjP0bZvNzajrPzfccB90C22_87Mr1t_FH8NaqNa8iUdY6NZOJD11dMcnLv_OVrfBE7yj2KFyauvY9RAlguMgiJTTivfpzTOaMXT7UPxfn0wYJNuASqvgJGXGfOPO303gyD-_nv6-VSmr4Ldgb_Tpk0jSBGz8LKO2htBN56HxrZECcmOKOJfTaZX6yakDlcexhXSw9lYfoLiCqr2bz1fE-eCh02oUCr_hJW0-5sVbMj8ghYjVfe3GfslvG7rJ5RfRq92coALffwovfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با همتای فرانسوی
🔹
وزیر خارجهٔ ایران و ژان نوئل بارو، وزیر خارجهٔ فرانسه  در تماس تلفنی آخرین تحولات منطقه‌ای و بین‌المللی را دربارهٔ یادداشت تفاهم اسلام‌آباد و روند اجرای آن با هدف پایان‌دادن به جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه ایران بررسی کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445580" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445579">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فردا؛ آغاز ثبت نام زائران اربعین در سامانۀ سماح
🔹
ستاد مرکزی اربعین: نام‌نویسی متقاضیان سفر اربعین حسینی از روز سه‌شنبه ۹ تیرماه در سامانۀ سماح آغاز می‌شود.
🔹
زائران باید گذرنامه‌ای با حداقل ۶ ماه اعتبار داشته باشند.
🔹
با اعلام بانک مرکزی، به هر متقاضی ۲۰۰…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445579" target="_blank">📅 09:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445578">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شهادت ۲ پاسدار بومی پاوه در اقدام تروریستی
🔹
سپاه نبی‌اکرم کرمانشاه: تروریست‌ها با تیراندازی به درِ منزل پاسداران بومی، ۲ تن از نیروهای سپاه «شهید برهان کریسانی» و «شهید خالد خالدی‌نیا را به شهادت رساندند. ۲ نفر دیگر نیز زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445578" target="_blank">📅 08:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445577">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c169c30dd.mp4?token=Dp0Jz96xYFZVljEn5CAEZV7e2_fH79ZfIM7VDGte5JeeQH3QTB54YpsbFRtBun9o_68wdJ0WYnFvsAcUQ78D2OyKhzitcgyrT4HwhDEnKbeW6Zgpx27y9M6R4OkFNfnVDc_amATRoEOTcbp3PoFPe6zg-8Y6pj9gZoCbnMwl0J-vVnOoYKQ9C0UnSbv1g-aBtgrYF6RWfx8MVnfb5nCBm5cssXz-vu9AFlIMtWjQ5WdfcZgsN8sQrnEaB-VCvnMGbATK4wrubKoXuEM0oeKQ03gVFokoSoSAuA7BroyK49X4kESIRtnAJpPfa2axuT7QUHQg9FSHTuuttHmps17uXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c169c30dd.mp4?token=Dp0Jz96xYFZVljEn5CAEZV7e2_fH79ZfIM7VDGte5JeeQH3QTB54YpsbFRtBun9o_68wdJ0WYnFvsAcUQ78D2OyKhzitcgyrT4HwhDEnKbeW6Zgpx27y9M6R4OkFNfnVDc_amATRoEOTcbp3PoFPe6zg-8Y6pj9gZoCbnMwl0J-vVnOoYKQ9C0UnSbv1g-aBtgrYF6RWfx8MVnfb5nCBm5cssXz-vu9AFlIMtWjQ5WdfcZgsN8sQrnEaB-VCvnMGbATK4wrubKoXuEM0oeKQ03gVFokoSoSAuA7BroyK49X4kESIRtnAJpPfa2axuT7QUHQg9FSHTuuttHmps17uXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی قاتل سیارۀ سبز می‌شود؟
@Farsnatech
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445577" target="_blank">📅 08:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445576">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9120781946.mp4?token=YZ7p7L_VDKLHHSY-o2SukmlPRY82ztvbPK_9dDu2NcbG7wyIrio2KnighFm16W53ZLxalKY9Df-dFe7MSUrQ_0mmTP6sNV-pzuMXGs4R5kINnz2U-7oBxqp1kwtraIZ-VNo8xC0U9vEsQs5J67-JDGvXBo_Chmt7FdmG7stzb8rcpSiNV0RH0-2zHUAkJUHoEHnYZVLAdYboLpNu4yFRYAh-QAp9NQydH-qCmjguhPtV2m4gauWftyMLEs1mibk5vcw7gcv4SQKxM3MKUBHTFVjJ49othM-hh_vUZirue_KkOWbkLD-f3LkiKl2aX0G_BIcukCcCw9EwTZ6fAfABsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9120781946.mp4?token=YZ7p7L_VDKLHHSY-o2SukmlPRY82ztvbPK_9dDu2NcbG7wyIrio2KnighFm16W53ZLxalKY9Df-dFe7MSUrQ_0mmTP6sNV-pzuMXGs4R5kINnz2U-7oBxqp1kwtraIZ-VNo8xC0U9vEsQs5J67-JDGvXBo_Chmt7FdmG7stzb8rcpSiNV0RH0-2zHUAkJUHoEHnYZVLAdYboLpNu4yFRYAh-QAp9NQydH-qCmjguhPtV2m4gauWftyMLEs1mibk5vcw7gcv4SQKxM3MKUBHTFVjJ49othM-hh_vUZirue_KkOWbkLD-f3LkiKl2aX0G_BIcukCcCw9EwTZ6fAfABsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمار کشته‌های زلزلهٔ ونزوئلا از ۹۰۰ نفر گذشت و ۵۰ هزار نفر همچنان مفقودند
🔹
عملیات جست‌وجو و امداد در ونزوئلا چند روز پس‌از وقوع ۲ زمین‌لرزهٔ ویرانگر همچنان ادامه دارد و کمبود امکانات و تجهیزات سنگین، جان صدها گرفتار زیر آوار و هزاران مفقودشده را تهدید می‌کند.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445576" target="_blank">📅 08:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌ استاندار تهران: مردم زمان حضور خود در مصلی را مدیریت کنند
🔹
در مراسم وداع با رهبر شهید زمان ثابتی برای حضور افراد تعیین نشده است، اما با توجه به میزان جمعیت و شرایط فصل گرما، توصیه می‌شود مردم مدت حضور خود را به حداقل برسانند تا فرصت حضور برای دیگر زائران…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445575" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445574">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbVZx8XYEgvHj5BNtEdVGuX1KfcxTNLmuVI8EIr2o2z9eTe4MP2W-0kex7pZW2C30rP8B9KnmN9JZXwEIerx0geCoPT_TM2zlxePS4HUPO_-zom-297OBGgJDy4Fbl8VY2RnlGcp0I8PzKeQecfJjBXTIyuDREy61hoB1cZShiflgE0-boRHsGiUFLfkYAWRyBUv2sRdyQ9uLOm2yCe2H2CrIkmFSp0VBALNqMX220NGEP8mT_2Fsj1qA49yRHjtnyn8lWpwXZGy_4b5KFg9MAmxPwgOCmrDYROCwsY0Q633lQHf-GYc08NR-XZummfBb7NfVUH6q5_WykQpTjJOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
سجده شکر مراکشی‌ها بعد از صعود
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445574" target="_blank">📅 07:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445573">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgPRhq2OMsSTnH9QOIZzsTSZvK_SrBCWNyl7rNSR9LcOcGrg0Wqwy9a2JvHYPdhOWUKC0BuguApwxHPfvpPgeIwEa_02lAZOXAzLaCQ1hC9goU1g2OiaQuCdVGCqAiW42w3oDh92QCzEnzBPiqZilz0zCC9qVR_Mhd8tYH9OYxoAQB5KGd6FVl45HCKEd237BGNJ0-totFzi-Miqno91upCD6c5nSPqnoucCkNcdSgn-hUYehJIRa9u_JBLbdnK_RnxIydSa7r9Jn9TIonFYAJDtV8pB60FYqTRPyL7r48GDzrCska2tPdhwACGvcbJx4dNjgPhGCC_XoecCr7UE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با برتری مقابل هلند حریف کانادا شد
⚽️
نتیجۀ بازی: هلند ۱ - ۱ مراکش
🔸
نتیجۀ پنالتی: هلند ۲ - ۳ مراکش
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445573" target="_blank">📅 07:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445572">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد
🔹
با فعالیت سامانۀ بارشی در دامنه‌ها و ارتفاعات استان مازندران، از امروز تا چهارشنبه ۱۰ تیرماه، رگبار باران، وزش‌باد نسبتاً شدید موقتی، کاهش دما، رعدوبرق و تگرگ در مناطق مستعد پیش‌بینی می‌شود.
🔸
با اعلام مدیریت بحران مازندران، اسکان و هرگونه فعالیت‌های تفریحی در بستر و حاشیۀ رودخانه‌ها و ارتفاعات این استان در این‌‌بازه ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445572" target="_blank">📅 07:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری فارس
pinned «
ادعای وال‌استریت‌ژورنال: مذاکرات این هفته ایران و آمریکا لغو شد
🔹
رسانۀ آمریکایی وال‌استریت‌ژورنال به نقل از منابع آگاه خود نوشته دور جدید مذاکرات ایران و آمریکا که قرار بود این هفته در سوئیس برگزار شود، به دلیل درگیری‌های اخیر لغو شده است. @Farsna - Link
»</div>
<div class="tg-footer"><a href="https://t.me/farsna/445571" target="_blank">📅 06:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445570" target="_blank">📅 06:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پایان مأموریت اوسمار در پرسپولیس
🗣
طبق پیگیری‌ها اوسمار برای جدایی از جمع سرخ‌پوشان با مدیران پرسپولیس به توافق نهایی دست‌یافته. به‌احتمال بسیار زیاد او امروز، توافقنامه نهایی را امضا کند تا جدایی‌اش به صورت رسمی اعلام شود.
🗣
طبق توافق صورت‌گرفته، باشگاه پرسپولیس متعهد شده بخشی از مبلغ قرارداد این مربی را پرداخت کند و در مقابل، ویرا نیز با امضای این توافقنامه، از دریافت سایر مطالبات خود صرف‌نظر خواهد کرد و ادعای دیگری علیه باشگاه نخواهد داشت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445569" target="_blank">📅 05:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445568">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlE2WRN5zK3aUwvrA_Qm7Fv49H_cZXTEfdb8gAKKFiKyofiD5fxaQYXeTWZIYXDpsSMNaRva6ixBj2fJGC7DBiEgdo-sc5TfbfdCVE2FRXlpYB0L7HHNrf8htrLv2WjfuBMVul1ynACj9cU02WtUSEpleBZlIH3y0_E1oN_iNIvpeQNA7qcxm11MNPt2gHWbpkUZBVeIbpqJyIy_ONLTL1iYrnBVvMmP8b8cVJrI4T4I0uLgve0w-GmAkr2GEIxgodcT7fx4Yx1iREW5o25KDLkSBCs70PvnCTlUK3gvhtfNuyzRk2QYEAeAM-N-1N600UWvyRo1yHicP_YeogntcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ستاد اربعین: هزینۀ بیمه زائران اربعین امسال ۲۰۰ هزار تومان است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445568" target="_blank">📅 05:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445567">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez3nOuTzlSWTOfePlUhwePb0xSNxZQES_-9uLNucCBKGRiGefUKnFC2So3O4k1G6Zi309cNIK_4H-d6RcO8S5tdJzv3C7s4nzZEowwfsiSZatT32Q-En3sFCPmV-L7JFTYn7qjWBhV-X6EPuds-yG9ntn8dGwpq4IzL9y9kvE_DsHBtBRCe7KBakYo_YOmvOIKwMlJuwyHyVC5ohGSMqbu9Jk2QubRbmXnAkTCNF2-gfjGK37_WzwebAGRfcBVERh76FeZbtTaHsQI4ZpKc0oalDfYkjo14S-k8tt7VNH920zLRIDvz9IABIbxGXHIstofJQ1vPklVH9TgWWUnV0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین
🔹
راهداری استان البرز: به‌منظور مدیریت تردد در ایام برگزاری مراسم تشییع و وداع با رهبر شهید انقلاب، ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین آماده‌سازی شده تا ضمن ساماندهی توقف خودروها، از بروز گره‌های ترافیکی در این محور جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445567" target="_blank">📅 04:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445566">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام کاشانی: اسلام دنبال چشم‌و‌گوش بسته قبول‌کردن افراد نیست
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445566" target="_blank">📅 04:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445565">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGHUE1okRU37Ta5Z3G6h1weTQiTRqvGPZlvcwkXPO6fvd25YSbOutqAENGeh22UEI0E0as1doOn4Ca2F3S0kyXiVKixBvCSL-5zp6iCvfjXBFAqmAnhw2JLbkXdILeHYxGnQ8kahCaX_SkLtLpP5opZZCViADzRITBcDNAmJtrNmcjmrYXBVipSEhj0y-E7ESIicnGfnua5LaQvhhWuKSpmwii4QRpuTCVR9KpXRAyNgvX4KVoOjjWMyY-yafFzB54wsnJ1hm31-oK87I3PWuJy_ecOKF5JlhTymmVNkl-w-j3oR_wMtcMT2BMKHkqTYbWnwFPSxkMaJWaC1I4Z9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات زمینی و هوایی ارتش پاکستان در امتداد مرز افغانستان
🔹
پاکستان از عملیات زمینی و هوایی ارتش این کشور در مناطق مرزی با افغانستان و کشته‌شدن حداقل ۲۹ شبه‌نظامی خبر داد. @Farsna - link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445565" target="_blank">📅 03:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445564">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seHapIieHXctRH2y5Pb7EIkB2pq-RQSMaA5dG3oifNNPbhZTSo2wHu-UTmljrFkL2qETomq5LNRt5D4hEvZ0a6CvWf1om8h1YrCfuvYv6HpJ5-DJdi-qz-dRm0zBZbFHMFLOt7yaOdMK5Wl_J526cESPdrzx_HVi35w4kH1p_14k4fIWc2BuWczI6wuYatWBZeKnU4tyuPHR4VIzhgUCmnaFvDdfIF20wLmsNZeLIoJQMo8NaeGGxHRa30GiJh0XwpYylsZsXsj8oJ2iiYf9yS8ZthqncNb9zLsS7QfjlGUAjZtiPiaVPDb1Mo782pXZtlWPdYbJnMJ1AaqioydGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: ناتو، تسلیحات دوربرد را در اوکراین آزمایش می‌کند
🔹
وزارت خارجۀ روسیه اعلام کرد که ناتو اوکراین را به میدان آزمایش خود تبدیل کرده و از آن برای آزمایش تسلیحات پیشرفته جهت حمله به عمق خاک روسیه استفاده می‌کند.
🔹
به گفتۀ سخنگوی وزارت خارجۀ روسیه، ناتو در حال کار بر روی سامانه‌های تسلیحاتی پیشرفته‌ای برای اوکراین است، که جهت از کار انداختن فرودگاه‌ها و پایگاه‌های هوایی روسیه، ازجمله آنهایی که در عمق خاک روسیه قرار دارند، طراحی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445564" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445563">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDRQ6Oa1Uv1Koak0uZ8XBt20GcfI5mkGA_iKEaNh7hCiKmO8JwV8PvGmVbFNearF2dXm0HdrQCxyUcABm4MXemOgWmS6nPKCDW1146INADfRa8T3BzatBeHqmTjJGhnp6h4v9YfTVGYcCJ4YrBZFiLGmgyrMpty4lovfIBYHfW0nCAxEcYbttYgxJS8psqvlCv1Oi9TKixj9q7W0384S8UFEk0ch8DK5DMoRhei3XwdznO0t3SxVEbhGecdYpsEMFdr3JqF4Dhz9IzJt04i4RJxyDAhNwmy70640pSMc56DA22CHRYKZD7aii24uiwDWM1lQdEnqLEtclZTjXrXK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شگفتی رقم خورد
حذف ژرمن‌ها به دست پاراگوئه
نتیجه نود دقیقه:
آلمان ۱ - ۱ پاراگوئه
ضربات پنالتی:
آلمان ۳ - ۴ پاراگوئه
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445563" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445562">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSV_aLPuJIxIatRC5EF3FMeoPQEn-OSsVMnBS8H_Koft-bnEI-rWMSNGvLuv5JBwS8LYNCGWKLPO7-t6KtNCQoRieIOTuLAQgWpZczhXZs9iSYRj69011ldB04MGHQDh-Ts0-rw691dJYkaNrjCzng6sgtLc9sigT2F-jLiMn_rGuFEz81R6GCMEgyrzsy8uT1bBww_NguAEDLQuktk-1lwR_nsB7vDvclkGPNLLOWAkURk-OLmmUQk1xIqRjbpqjNRn3INZe4u04lXdWI3SjXG9mr9MBttxpY_-sLU_Tnr_38Oom20IYlWOJe_o67xwYujwCQFx3ZCa6SIlw7GePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش محوری پایگاه موفق‌السلطی اردن در جنگ علیه ایران
🔹
منابع مطلع به یک شبکۀ روسی گفتند که پایگاه نیروهای آمریکایی در منطقۀ «الازرق» در اردن، به‌عنوان یک پایگاه اصلی برای حملات علیه ایران عمل می‌کرده است.
🔹
به گفتۀ این منابع، در مراحل پایانی جنگ ۴۰ روزه، این پایگاه بود که به نوعی نقش پایگاه منطقه‌ای را برای عملیات آمریکا علیه ایران ایفا کرد.
🔹
در این گزارش آمده که واشنگتن هیچ چارۀ دیگری نداشت، زیرا نزدیکترین متحدان آن در خلیج‌فارس یعنی عربستان سعودی و امارات به آمریکایی‌ها اجازۀ استفاده از حریم هوایی خود را ندادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445562" target="_blank">📅 02:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445561">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLLaHBf6u2Rt8iYKRxym721fN5db4kBa-gShZAPw7pbGNXdI3L2ZU2y9BLA7zHZH5qnnBglmqDhFRrEpOxQ3dwsZKWuaiCJrhvc4IqmpkcNSJjhLhDeE9j20ZGoST0JrlOUYuPAHzmI6JP2XV03bwpFpXPekZlEACePCbAnaliUsloipp0-8NajTE_RP615DACoHW4V8vRmMH7wGp9pxnOQ4Io9H2kSPT-qR-mGCxk1-RwlPmVZERX9hdcpy6huXWPae_dNwt8bIxCjp2AbICxO4dScmfaGi3Sw6tt346TohrCu7d8PlthgkXQi8JENL5SYljV50EcGDBiiW6Cgxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر عمانی هرمز با اخطار سپاه از کشتی خالی شد
🔹
بعد از گذشت یک هفته از رونمایی کریدور جدید عمانی برای عبور از هرمز، داده‌های دریانوردی نشان می‌دهد که به دنبال اخطار سپاه، این مسیر اکنون با توقف تقریباً کامل تردد مواجه شده است.
🔹
بر اساس اطلاعات رصد شده از پلتفرم دریانوردی مارین ترافیک، روز دوشنبه تنها سه فروند کشتی از مسیر عمانی در حاشیۀ شبه‌جزیره مسندم عبور کرده‌اند.
🔸
این درحالی است که از زمان اعلام مسیر عمانی در تاریخ ۲۴ ژوئن تا پیش از این تغییر اخیر، حداقل ۱۲۰ فروند کشتی از این مسیر تردد کرده بودند. اما به نظر می‌رسد حالا اوضاع به‌طور کامل دگرگون شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445561" target="_blank">📅 02:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445560">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olqLIrP56sSdqpajDih1sL_igOxAtAh9iMmo7pxL8ZqFt2QO4C2wIsCZS3Npe5nIGFr1yaefCMj8ILjwsyhSA91dWh5vwc67MjR5kvp5bdEop4Tl39TRn6DKNKqiZKjzk1u8qLziCEkcyqFSwyxITQGZ6YaDIVBrOilP1x-cnJJJbkwXRzdx91ZqnVNzD_3hnRH5A8wxtF338FEdnpO2-hSjXtsE0jt3p09SoAaH3VZOA0QXe9gAsrrv2ivGz2jzoG4GMh2N3hwsSlB6gNIU79IiaK_ijYtj8jVorlUaebbqW20yzSjSf2J47LDePiAUuPx6b2sVc78TtwFOk0l24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این سلاح‌ساده، سربازان هم می‌توانند پهپاد شکار کنند
🔹
پهپاد رهگیر روسی یولکا نشان داد که می‌توان تهدید پهپادهای انتحاری را با سلاحی بسیار ارزان‌تر خنثی کرد.
🔹
یولکا با سرعت ۲۰۰ کیلومتر بر ساعت، تا برد ۳ کیلومتری پرواز می‌کند. این پهپاد با سیستم قفل خودکار، از فاصلۀ ۱۰۰۰ متری روی هدف قفل کرده و آن را با ضربۀ مستقیم یا انفجار ترکش ۳۶۰ گرمی نابود می‌کند.
🔹
برخلاف موشک‌های دوش‌پرتاب که به سنسورهای پیچیده و سوخت جامد نیاز دارند، یولکا با قطعات تجاری در دسترس ساخته می‌شود. این یعنی تولید انبوه سریع و ارزان برای مقابله با حملات فوجی، بدون نگرانی از اتمام مهمات که مزیت نسبی بزرگی به این سلاح می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445560" target="_blank">📅 01:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxbsri2LWJhq9E-9EdgBHTP62Qrt64utEFCgr7W-yY5Q_EWSHBA1J5O1MbVDCumNCKjX4TiddQQDr7gQ4fGTo652CWcMQqY-WCOOvNO46GQ25myVqj9SD54JjMJPo9tLUlLP_XOGo_frTop-4z16Ih62BKvZPtKjcbU6hBo-HWUs2Z8s9AOwJZqIwHgw4xYQtKLLpS9E0vR4YNcZ6nw8d_JMiEZSwvUtEXArlZymVPDsigiywMsgv6Cz-AyEswiZu8hQZOPVk__bniLpGJpmyCxaaxgA9nYIHCBEdTR3_4v1YUpNLMkiPO2BXt3dgnb6qDjvgzUFOPB0ht_8ClJc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPAiAQj0Y47Bkgijv79fbHzxsR84othD6Lx4VLvLg8vAPPz6AUc-94Ph8d4tgTt5D_SMQTZUpXosUYq6Z0r0Bq2QzyewiLI9FJMR9nZtY1_rH_H2OmOo6ktWnzU3eGWuoseIf4EGbI4kMLRZCMNI81qTCUOT-uuuTNaxS9gKUzsXs8f6S8sUMLTzcCmzUc-fl70FnnMaN_sdOgEvKcL-JmaotMecMUyiypmVQpGQVCFvWVPtN5LwCGuLnHp6TSuD3GPu5umaKYvIjguQ1dXpfgyLCOFav7ZD4ai-4bCWKMEwjAIeO_2hAIHOLvCJVQJbv6z2Ck46Zgh_264PyhfEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImYCPq-0D1Fl_Z_xGsWWjGaPm8KDUZEbGYa6q_wWPrxf4rSOGc8ZmF-JVK7gh8Y51hNFJJCI_yt4uZYCN5lJr0QYkcwQvrMtM5QnxYmvc0TtsKCxhuBrMPp_LbmzIc2fKBtXsmRpCxS0RvHyBg6ExFi899KWOAdRr5TjtWQ16St754ooFjXi0AUilyQXzFW2KSODbYd-r-7nogZWIcsE_YeRnGfLlZcxQAPP88Ma89aCCNixDeTWR-5uXdT73BZN5TTcaIeE87ogcjHTNDBnatdNXizV_IqlIy9pO0JRuDY5E2Kv4DkTP043y_URdyMUtqJ1YqOIawWh0q4H14qyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feLAmCUIE3Oi-dNIM-hK9RaaziOEETRksix1_A6Q8-9JzEb1aBMEwDDSIg8ipXuV8Idqq9pODMOeSbW6SoAFUmZ2uIqV4WeJaA36h4fo1YdY-LuBaGlsdlDztmg4y5Ya-1Pz-sWPj_T3GmOfoKitNN8bYxBSpQTSpBQ9llUsTp9mxBsxVnzJGmjUsf-2FlPdkV9XykHtFKPpwb4jha7GUoULvioZUBCSKNu1K76D7D6_4xE7TL9Y8JXPWgHw0v7Ex5yg9HdgoOaX39NhYbl_YfZb31AqzP1l3dR6DXbSxMrHwetWVLJIWziEerTH8WeqtxRtpeopw1Hul3lH9YckCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGCISpwTdCIDzH3WL3L_GtSLrI0S9vwFad7VD5kLD-p9mW1TOboRlNj13NnAA4BAqVKR8Ga2MG7bue0-Vf94YHGI-n8eq2_hY5pNfAdUBVKdirAEsjjsLdjMbeLan4JMCG98bicoNtlHH5oOwPIKN4ucU-SdJdZJ8OlkW1zVHHiTUn314cdD7MiX0YJQifw73MUOYnyMGykUXtBe1npuCHP_MD91hgO2KfK6Iy6pVfj3deIbUvcu1izgV0-htuvlX2CMc0bs0kLQkTyCHVf-fbvmC3XkwCAS1pEll-4mUa4kQQIvJCxgHxKAXib7fA7LuKcTcdY-tECVdOLUkGABpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445555" target="_blank">📅 01:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS7MQJZDSjSRMLmeLEn4kr03LzQCip037gBoZ5nl6AbXmp-IiK95YDu5_eLXS72w-3d6ACHxNGgvBKYYqA6nT40FNBVw6yugYW2oSQ4ao3gsnaVESIXyzkeWYCMGsHH26RghHL9Ku1RDNYcgJfk8byIIEOnVypnHn26QYNsT3V7e5c7N1tOQYoM88Ht4JWQz6fwgM3osjssMuRrYtZM6T-WPgiwGI9zAo_sRl8MTUrRYPbvqYK4viYGyVj-DNhbCe9IMsjQaNKdUU7GewdMI9QcbvRB_4IYLQSAzeA1gw02eu98_W7xl3eYDq29c7htKwLbVC57_s2zgnE8gq-Okdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksCLHyjxsi5SE9o4bGEzWtAb-Y9eWuIBKlgmqTA_xfh906s1CHuke_pbVl44xiMY_ofJARMDXyF28o-41ntfpsm6yBagtFytGD-Yb5FQzx1tjY1ary6FLkfJ3__yRLO_CR1zFaqhcwdyhlhVthbBERBfsEkFUPxrNfzo9cis0W7G89up6alUfLBZEKC2xVsQS-dNmUzoR99srMU_YAgyah0oFQEIaWuyREH_izE_dxgxOAMMfYbkvcU6aC-vJhsb2SX3oyf1MGAwbi5JOS7o3lSJVupZkJfVL6_LQ-T7zxqD4m64B62O7jHEX4T4JO-H3AKtpsGk9qM2R2m0OUshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYJl7Fh2iJsDNbOGj_y8urquy8yCqQXmp7u2HCzZPNIVhU0L-cYKSq25tyxGr6DrvCOhzl7y6nMZA0IyczqBAgt15afBeHZCNIWcsI8v5Fg70LDJ-j-GWhQUH45Lb_F-L0CDRE6MoXvuS_7a3yDAwZO7AqPrGjIM1QrxNYb-9aNvxfZvSUIKpotPBoLcRXZfHbAzE201qjMTHvdk8trsw9Z-yzCLa5qpIHtLBktgK9abmYjBkRc6PbnKgeUgOw3Ijxu-J2NOjSmEFhJLN2uAEBP4sM6LnPKfpDvR7G-GFxw9CB95SHHorSaMG3h62DN5zMfaTTB0ZoydoQjscDxidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJiZRtLVj2ZufKAJSZdDFnArqh8WF9qVqiKO-fKvUOOrRtzHB9MSuYSl1IAuLmFAHBw_yZK5GfHrby3xhMujXO9_3b8vg_zmHlp5ueddss_KvOml8e0NTjJW5gsCu8g-C-J5wjb3Q6Orn28v-xun8ScUu6GJBtKyFjz2g970FNNa_j3pTMVu7_gyYu-mf2P4KQjnoGn2x4YxohK1pDQe-BdQ3Rj9D9v46bfDLFOY0ZObWsoSJVKZqKQN6KGMhf3ot109NsH0xW8y8yKJL-0v0uYhPWhpgwNErD0zDsOr9Au3joY_0In7ZnC3Zajix13Rj0xbCcBndsXdg_1NYH-h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbipsB3ja54ZUL4XJd9NKVjfanmSEfJwmT99lt2L1M7Spf2YnBpBVqYiKbcO_zCg7XBZUvIsRUuYxq2QAVsXIyhbJuI1RJ6p7GwTDQWKEKZ9AFpf6IDQh4XH_9RYECkipgSbBonstqLEit0DBYl5ajD6vwU0tILIfbmJdOGtF6M_SU3e0SpUFNAbc5_UXHocgz8bbxV0Rew_ut7rXGX4Q1q5b4MkguWUZDERToGAoMnElOP8StbJVYTk4sQ08EVOs1OwqnOFCc5F_X-hnnc8SSyZf9DSa_DmXtyVey_5uSKwTr4U-PJg68WE2fyE6MM-gML__yr489NXOMb7GoYRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GP0FMUXGyB3tubQ7vihFTDF97pfVMBRu8K4ZcS8Hsf_4ETak6on6_eWKmH0xPCmyJbsBoUeOwFk3kCrdm8L2qzh_lJljDOwQksjX7hZSV-qt2eJ81hhwX5QN4tRjtsezTaOIH0OhXmxVwd8_xXld1nxZJu2J0PgVng0h-r8amKc-3QwqYGQvaTc7FTqDd8BG27KSBIYfiX1TooBkes55w3NYS2ONMYazWs3zDl1Vh0giwoCnG4hFSX2UT2mFCTBtIQvMp_XiJTCit7lcOGtR4tlQVwb9OqgAJwDs9PqjI8xFbaobbDPqYjw6FzAIzdLc0w5GBK2s7lusRLqYlvhdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhCZFHoGg5129TIz_UQkCdbMZV3w1J7DsjjQo0exmFeA3rBu8IkThd-D5NNC6mNs6kO8OOvgRypwARgysqS3cjGMMmyXObm_Eoy0oltaX1YlcQXIN0VGjWpaQBb_ruXiGZb0eV9MlzVg8aAt2vDGFrDo7a-Y_vGmh0Tuy5rUO5vxvbx5kOHQcqi9kRnQiK1uXGtHvEzjSkA-d1qWLYeX28eNot_Y5AyYv75f4hw0JXTVSOrQc7h6hFCdzhG_ZP4D3XBZgI_ecs5NLepHPomGT1eX6GgVsJpd2R7IS365PFzurGOsZBQXos2rJLbX70FW5mqkZH1gQgGGQYFyr4qEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZAnoi1JM6fdQC_ndoxNiLtZQrDVc7psugg3VdqaBYFMDvlY46YwuXnhncXZphbKcVZiRPmyKDHDWlRSNWQ8WB1QTI-dk6KLTWDB0lF1bcOk9LUANtI7PFsyCFVP-zA78q52qIYrXYHlcjv0GRyL1_gzPk533enTCnBFx0DEyRkMqzhK8UMrIcxmt6rwUVjDFOtNLOqQ42k15kyJgUgaaqMKiPdvKwmwBSqNX7zqr-cn5drKT5zcVzvDTBMEASjyw8Jy498vov3s0-hmDLkIZ9mzstjvfcyPUJPkQG72GfAPpUIPezCR8OFJD5x-agp7rEZvPs2SlVHnaP4pevO82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTpKHpo07uIn9TsoOYaXQxoZ3CpcN7i8q4OslBwwP_uxSuStaC6fstR7U-3QL95IZ_V3oJLjped3--5mPQ3O7Jl8x1lu6B-vJa_e9_ZCIIVSt8U2KHqtuisy6HrLF5CKHuGtzSHdXZTdovcdCPaqowlrG2Y0D59MGAOWLRxh-FyxBgmP9Z-pCOmC6ZspJ9NoIi4l6eI_r-PoHLgLtPqvVRzBrazMnbFz0HIZowpvytOQZQEu7mP_SFG2ohe8ZiQbg-TW2P09LWqwYoDh2s17xNvoSBadLC7RjtYR05nku-bb02NWhDLqyWzCE0k4ocUr-nNw8PHvL9BaJH9jlMJ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbuzpAWkEt1tbSFiG8fPr27mjZwE_ybOUCHgosLz3RNUjnN_krIm-my3AArlx_p78k0IvXfdmWkQSGbmcsJSXjTrUT35BQuziBT2ilq1cvxsB6ygUpfRqCJUMOUaAJ6XJcYzVCKywXZAfbitOioRcnAnMEg6bsCzLS1szXdzqnHazFayVvhF1qPW4GK5xQdkE86zQa8mOfLoiQGfD7HtAxAZ6MHTI7MnxXuvDd-V0HmAxZdLXiWVYzpvwe5OoowvITYUz3SMPm34pu_BLv_v8SaeAihZlEuFk-wf-FUnb2c9_2PVbAf1EGeXAFUSQdoMAvK4uPsEugRp1_Qic2N8yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445545" target="_blank">📅 01:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات رژیم صهیونیستی به چادرهای آوارگان در منطقۀ المواصی در جنوب نوار غزه، دو شهید و ۲۰ زخمی برجای گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445544" target="_blank">📅 01:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445543" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۵</div>
</div>
<a href="https://t.me/farsna/445542" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۴ – کتاب آه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445542" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445540">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445540" target="_blank">📅 01:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445539">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH5JxljXYLhRPlyuGCaqQQey6CALgZnP1onxS96sfU9JGNDsVXJroMcBcMvdXVOaChSY4hoBIXPuZb_N_OB0HnpQBxnmPl-gIYx_sfb6IAzzlbV9gjWwOG1bsNwhfgpgMrnyInD7ozKADkc_FNVMOQuVikkPBqiKLFOtQbYmOUzKj9eIf8UBmcC0R5bnhqj3eV8duXcrdJZzJuYK7aJ9ckeepHyr47ZVBNsnoAN61etyC0aoQCc6jWIuvpfrSBihGVhDTUNrVEYZ4ofYNZJorkBLYDrq3OhhHBEv7i9lRJCmNCBIlYVwyJUjgX2psvKB78t5Llduztqn-g0FATBQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریشه‌کنی درخت آزار و خودخواهی
🔹
در مدینه مردی از انصار به نام «انصاری» خانه‌ای داشت که در گوشه حیاط آن، یک درخت خرمای متعلق به مردی دیگر به نام «سمرة بن جندب» قرار داشت.
🔹
سمرة طبق قانون حق داشت برای سرکشی و برداشت محصول درختش وارد خانه انصاری شود. اما مشکل اینجا بود که او هر زمان که می‌خواست، بدون در زدن، بی‌خبر و ناگهانی وارد حیاط خانه انصاری می‌شد؛ جایی که همسر و فرزندان مرد انصاری در آنجا آسایش نداشتند.
🔹
انصاری بارها به او التماس کرد: «سمره، وقتی می‌خواهی وارد شوی، حداقل یا الله بگو، در بزن کن تا اهل خانه باخبر شوند.» اما سمره با لجاجت می‌گفت: «این درخت مال من است و حق دارم هر وقت بخواهم سر بزنم و اجازه نمی‌گیرم!»
🔹
مرد انصاری به پیامبر اسلام(ص) شکایت کرد. پیامبر(ص) سمره را احضار کردند و به او فرمودند: «همسایه‌ات از تو شاکی است. از این به بعد وقتی می‌خواهی وارد شوی، اجازه بگیر و اهل خانه را باخبر کن.»
🔹
سمره قبول نکرد و لجاجت به خرج داد. پیامبر(ص) فرمودند: « این درخت را به من بفروش.» سمره بازهم قبول نکرد. پیامبر قیمت را بالا بردند و حتی وعده دادند: «این درخت را واگذار کن و در عوض، من ضامن می‌شوم که خدا در بهشت به تو درختی بدهد.» سمره بازهم با لجاجت گفت: «نه درخت دیگر می‌خواهم و نه درخت بهشت را؛ فقط همین درخت خودم را می‌خواهم!»
🔹
در این هنگام رسول خدا(ص) که دیدند او از حق مالکیت خود به عنوان ابزاری برای ظلم و آزار یک خانواده استفاده می‌کند، رو به مرد انصاری کردند و فرمودند: «برو آن درخت خرما را از ریشه بکن و جلوی پایش بینداز»
🔹
بعد از اینکه درخت را جلوی پای سمره انداختند پیامبر به او فرمودند: «حالا برو درخت را هرجا که دلت می‌خواهد بکار.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445539" target="_blank">📅 00:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: در طول هفته جاری هیچ برنامه‌ای برای مذاکره با آمریکا نداریم
🔹
حضور مقامات آمریکایی در دوحه ارتباطی با حضور هیئت‌های کارشناسی ایرانی در دوحه ندارد.
🔹
کارشناسان ما برای پیگیری تعهدات آمریکا از سوی قطر به دوحه خواهند رفت.
🔹
هیچ نشست و برنامه‌ای…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445538" target="_blank">📅 00:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: اگر با عمان در مورد مسیر و ترتیبات تنگهٔ هرمز به تفاهم نرسیم، در هر صورت حاکمیت و سیاست جدید ایران را در تنگهٔ هرمز اعمال خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445537" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: رهبر انقلاب دائم مردم را به حفظ وحدت دعوت می‌کنند؛ از «علی‌الاصول» برداشت غلط نکنیم
🔹
بیانیهٔ رهبر انقلاب باید همه‌جانبه خوانده و تفسیر شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445536" target="_blank">📅 00:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445535" target="_blank">📅 00:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445534" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImYkW63G6j-EcHxi6wcob23hC_f_2lwtVKhMkXAfmDzvYfxqUV9l53ioIuHdl8GfKhQ4--c8wdWloq3DnamJ76aoc7fmFeoZM7ruVd64ZcWbz-c9jPNf-Lm0Q-LnC67AEkTtYt2saEQueTUaAr9lbXmT7I5EZClM-5CRdTtg6Ohk1y6Q1ATERWneCRL2RDpw_LM2j18E4qHpn67YDhExpmak-NaTHaP8ubxjHFtpeCH0uX6hj2Yg6-PB1oWS9L6tYOH5GCwuNXgri66rHXL7XGxRnv9yWy75crCLViIAcO7r8sReXsS0K4PbVF5haOh2vHopWnjvNV5o9YpI-jYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: اگر طرف آمریکایی به تفاهم‌نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
🔹
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445533" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۱ شب ایستادگی هرمزی‌ها در تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445532" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrJz9knxI5LqF8R3RegdCLkrHTtk-3AVaSwP6NEoY8kzgTYLscvNAWIm2N4BR_DSLvVpHgLezg6WMqVco6T9Ej03m2nJoOV4dZnjnWICxfKbmexBQ7Zu0DZnfQJ6jOVFSoAoNueXo3Uc0PvGF1rrPCpJ8mRBrEw_U2tqZyIzIxMEBtGsEdq2IjJJKpAxtOvcgWeb5OfvCU0tpEACU34ydBKIevGWGnKT-2dzXskiQkG5CtCtfZ9TUIRx7uq8QdbHo1FkyxW_PWjIfcwBpWctVv72BQY4IpML2iEI3ETPTwaPqCaeqM2HBqXBN628i7TU0i-jBH_CVOCUL7DYfIQ34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عذرخواهی بازیکنان ژاپن از هوادارانشان پس از باخت
@Sportfars</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445529" target="_blank">📅 23:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانه نیشابوری‌ها به عدد ۱۲۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445528" target="_blank">📅 23:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzOBXu9Zp1ozTGE7ppiWL6F0xhaKCaXBQpK31OTCSr8C15ulO3LO-fAZCo5bJO-0YU-bLWM_-XHdz-ht2P8p-Z-poPzYBpaobfDZO2NEEXKSw_oFBFkwXaEryRc4Y5yIhU5E9U_uo3z0Ir_m-yYkl8lVPdOy9elMUsew0VpeATAcBb9JHiTngRuG3EK09xyLAuWV9j3qah9I29iFxmOxpEYB2affQFoH3zdqNoRVyCeBwIe7aTdsctF-wRA8HCL79c7ADrgU9qHJR_cbWRltdYI-JE-SBlJdEru9hEO6hPFw0i81VU0nqxMUWTatzsW_nn_S2DwoWunKhOslydYM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا توکلی شایعه وخامت حالش را تکذیب کرد؛ صحیح و سالمم
🔹
رضا توکلی، بازیگر تلویزیون در گفتگو با فارس: من حالم خیلی خوب است و شایعات مطرح‌شده درباره بیماری‌ام را تکذیب می‌کنم. متاسفانه دوستان در درک ماجرا دچار اشتباه شده بودند.
🔹
مریض دیگری داشتم که با شرایط دشواری رو‌به‌رو بود و باید تحت درمان قرار می‌گرفت، به همین خاطر برای پیگیری روند درمان او به خارج از کشور سفر کردم. بحمدالله با لطف خدا و دعای مردم، حال مریض‌مان بهبود یافته است.
🔹
این هنرمند در پایان از پیگیری و تماس‌های متعدد دوستان، همکاران و همه کسانی که نگران سلامتی‌اش شده بودند، تشکر کرد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445527" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله تروریستی به یک خانواده در سیستان‌وبلوچستان
🔹
ساعتی قبل یک خودروی شخصی حامل اعضای یک خانواده که درحال تردد در شهرستان سراوان بودند هدف تیراندازی افراد مسلح مزدور دشمن قرار گرفت.
🔹
در این حادثه راننده به شهادت رسید و همسر و فرزند ۳ ساله او نیز بر اثر اصابت گلوله مجروح و به بیمارستان منتقل شدند.
📝
نیروهای انتظامی و امنیتی در تلاش برای شناسایی و دستگیری عوامل این حمله تروریستی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445526" target="_blank">📅 23:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b364cfef50.mp4?token=FCKUI53k_fKUJtawp8XTBSh5Tn5nWUFBwGH9NAqO05ezVzyio6yOwsBl-0FLkPkmJ9cB8lb9KE8IztKSJKeZEhevpzAyOPL0XSQtBU45MomvQ1bW8aIC4gcXmGen43QXjIbkw8homaiG7tmpP6Z4yIK2DLZkSWv1N9t7LezIvE5jda2T7WcenSSlMGeWQWAEH63S4J3SkL0uWJQ9wHWODv6s11oFdEJDCY0qT7b7Jv5_Q6SAJvsoQ0E-yBcu4_71y729lGDwDYh8ZDZ2AhWcU8-rGyTITcR5kg2ltI8aqmqcBWXCLfdAwILEDc87vWPjLYAf3LvkFdXxJGEDwfReoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b364cfef50.mp4?token=FCKUI53k_fKUJtawp8XTBSh5Tn5nWUFBwGH9NAqO05ezVzyio6yOwsBl-0FLkPkmJ9cB8lb9KE8IztKSJKeZEhevpzAyOPL0XSQtBU45MomvQ1bW8aIC4gcXmGen43QXjIbkw8homaiG7tmpP6Z4yIK2DLZkSWv1N9t7LezIvE5jda2T7WcenSSlMGeWQWAEH63S4J3SkL0uWJQ9wHWODv6s11oFdEJDCY0qT7b7Jv5_Q6SAJvsoQ0E-yBcu4_71y729lGDwDYh8ZDZ2AhWcU8-rGyTITcR5kg2ltI8aqmqcBWXCLfdAwILEDc87vWPjLYAf3LvkFdXxJGEDwfReoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوتبالیست‌هایی که در آمریکا آواره شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445525" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe93f5b28.mp4?token=pb1BzKKBI7ZlkkkNYIXR712BRzsrTuwjQbWJJLIlnGT2PUkchzYxqcfNoloxOAPYRg0wkzKZ5tc0mn2CdBzv94g9bTyA65F816yL787lg-ppPHauHzeOetQUTaj96Z5N1yUxo0pCS8TPrKOUZiQIq6OaJDFWfzvivS2MTrDdje_6XvW0w9YjSf6pIas4z12hIXfAlgINqgF8x9V897T2cJaP8Ob4vfv-5jQ9MUQlTy36t8AQiWamC_gkDBYlrPxtMqxwY1njiQPTFLhjPsQrcPtMOkiVVkvHZ6kZxuE8MxXYy9nPjcudV96d1c9EkirxWJ2oXY3gHCxKizIpHr4T2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe93f5b28.mp4?token=pb1BzKKBI7ZlkkkNYIXR712BRzsrTuwjQbWJJLIlnGT2PUkchzYxqcfNoloxOAPYRg0wkzKZ5tc0mn2CdBzv94g9bTyA65F816yL787lg-ppPHauHzeOetQUTaj96Z5N1yUxo0pCS8TPrKOUZiQIq6OaJDFWfzvivS2MTrDdje_6XvW0w9YjSf6pIas4z12hIXfAlgINqgF8x9V897T2cJaP8Ob4vfv-5jQ9MUQlTy36t8AQiWamC_gkDBYlrPxtMqxwY1njiQPTFLhjPsQrcPtMOkiVVkvHZ6kZxuE8MxXYy9nPjcudV96d1c9EkirxWJ2oXY3gHCxKizIpHr4T2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445524" target="_blank">📅 23:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4911f76bd8.mp4?token=vESmycQ_QkO7nTtjvCUCKhWJlavllLF3-M4otLzC-2uCIpcGTHhoI90-CBEdPfUV6p_iGws9_crxrv7fQJdRsIgjxWX9jhuOGjunoYWpVopXAsg0-5AZGYhkg_j_Bh8NJjWU7pTRvPSDesvzUmrUCtudL0cTEchg5WlxMEiYoQgOTCG640kdmC9L2UyOSY9zSEJGPIBnhqaIDSQzNZgmOT_AY-yFJyOKjMLZ6UOZ24spsLRYvKYRCeRT8ncqdoM2t4e-10OflqYp1yyatMGj_vvWbZ0N4mfxkP0_eVnTn-6j7qKWKaEJ4kZH75-k39yZk-rDiA7hdU10d-NJ0dIaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4911f76bd8.mp4?token=vESmycQ_QkO7nTtjvCUCKhWJlavllLF3-M4otLzC-2uCIpcGTHhoI90-CBEdPfUV6p_iGws9_crxrv7fQJdRsIgjxWX9jhuOGjunoYWpVopXAsg0-5AZGYhkg_j_Bh8NJjWU7pTRvPSDesvzUmrUCtudL0cTEchg5WlxMEiYoQgOTCG640kdmC9L2UyOSY9zSEJGPIBnhqaIDSQzNZgmOT_AY-yFJyOKjMLZ6UOZ24spsLRYvKYRCeRT8ncqdoM2t4e-10OflqYp1yyatMGj_vvWbZ0N4mfxkP0_eVnTn-6j7qKWKaEJ4kZH75-k39yZk-rDiA7hdU10d-NJ0dIaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مراسم وداع با رهبر شهید انقلاب، امکان ورود کیف یا کوله‌پشتی یا وسایل حجیم به داخل مصلای تهران وجود ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445523" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf0QXBR2iZ88Ob5MZJ74yK0USwv44Buh85Be1FrW_duZN9QxIitCYElu57HQU6HdIAAarMf3eWZxkb0kjHG1O6MYB_uydRmjZu2rF1Q2S5qe_wGKFmH-N4kKyqgDJnmMeq0n2vd-0yXrJvOKtkXAz-gVDivZf5LXAn7kVBD-0fro3osehvZkHk4q7OwwY5EVvl-81QNU-F3L8rfj43MgXsm9KGYLUHr2fI_6dw7uHfjZ_Pn_yIkYk718dg68VW-JbMujh0MjAO3NEsHfch490p2GpgghTNAVecxEgyh7GSmxX4rkl8f3pMYxifJLVSlz7tB3cqBoGftAdSRr4Hmf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند، گفت: «فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445522" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJfiTo0iO1NSZkOiQls_FbCn9YNiy49rEppSvZJvcQP5WaMhVm_xrDhbYMvTSoTlxTEcBobqIE-xXcMXFygCYx_OEvT315E7Eo3IxEEdLR1BVliwvEaSE24NtyK6UQgu-l0e1C0Yvw0vkYLtLP3qMiiqeUFWGLrvMsr7lZZiAoBSLhkQwemTqQ-npNZj6Ru1v3goZWXHl0WmXdf9iA9EpNVRSxdqoaymktxV_2EbXESsDIkpK_SAkdnbe_6iA8I-jhtcLbjGfBgAS4mKv53-C8MtgnB87wP-eRUX5dA3xM0VZAwBrHtJa4wX5JZpFJoMwgBrT_0J5yHEntpxYZRWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان اصلی مصلی و هر نقطه‌ای که زائران می‌ایستند، دید کامل به جایگاه وجود خواهد داشت.
🔹
همچنین سعی شده با الهام‌گرفتن از همان جایگاهی که امام شهید در دیدارهای مردمی حضور داشتند، همان فضا تداعی شود.
🔹
فرایند برگزاری و اقامهٔ نماز نیز در این طراحی دیده  شده است. در واقع، این طرح، طرح وداع و طرح شهادت خانوادگی امام شهید و خانواده‌شان است.
🔹
۸۰ درصد این طرح پیش رفته است و تا روز ۱۲ تیر به‌طور کامل اجرا خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445521" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY5heYlpfcYq0xOCm0_5Cso1X2-fNyn-pPOO9nn6fsQvI7E5gnWewu8H07VemNy8lfajtDZllMtEnZKktVzpVlajp80Hygxw4xMEpnH3gb7gxRwm9SJI3yRHHRaAGm9R6H-30bEzs1yncSGluEo51iOuIvgQTwiPNrCFcKGzxaYnkMsQxhQJD8gGhWOT-ac0J1kmmDmrPyDL2FXGON6lpotczyImLzoyYVJI1qe_qNTozyLIvwBwZ65fpGTpGqgMq0bfhqE32QEp_UHc_9t9o1MucuUctLImF5UAFvKaZodeO0MxO144JO_J-mgyWpJoIlQNjFwwbep_erjPMXcLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
برزیل در دقیقۀ ۹۶ گل دوم را به ژاپن زد
⚽️
برزیل ۲ - ۱ ژاپن @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445520" target="_blank">📅 22:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c2e900f3.mp4?token=SdPcoLMGYpMpkc2qNdsz5fmS57sx5IzNZKdWMwsHHFwUwZm4RvZ23D2GF-7RfLewviUnpnX3DZPBbhd3TYz0Ed5Fud360tn63l3L6MQbcHlkCgyu67hxpWnIA8hwJSS1Xkx4WR27XoBfewD4a8k_w0y7kCdY9u7HGkXWGdrdAaPcBtlZFRSQc_9xQqoh67BaBywIh4oPgIdBgjYeXos5LcautVzL3gPe6Yt9igCl_S1Xo-CTEO5eVaKi7xBE_0KWIrOfpXGvg-1mtp3-B6vYVfs27cUD8U_mNcARyoc7_mpB1Pc-vCNfVPmfpbVJSgIMW4W7y66Grq8KAVcDJdNh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c2e900f3.mp4?token=SdPcoLMGYpMpkc2qNdsz5fmS57sx5IzNZKdWMwsHHFwUwZm4RvZ23D2GF-7RfLewviUnpnX3DZPBbhd3TYz0Ed5Fud360tn63l3L6MQbcHlkCgyu67hxpWnIA8hwJSS1Xkx4WR27XoBfewD4a8k_w0y7kCdY9u7HGkXWGdrdAaPcBtlZFRSQc_9xQqoh67BaBywIh4oPgIdBgjYeXos5LcautVzL3gPe6Yt9igCl_S1Xo-CTEO5eVaKi7xBE_0KWIrOfpXGvg-1mtp3-B6vYVfs27cUD8U_mNcARyoc7_mpB1Pc-vCNfVPmfpbVJSgIMW4W7y66Grq8KAVcDJdNh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برزیل در دقیقهٔ ۵۶ گل‌ مساوی را به ژاپن زد
⚽️
ژاپن ۱ - ۱ برزیل @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445519" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqCr1CP1neVu0dI3BL1cPVmmAjDbKMYFRAuCDI-K7h3i1jy_U1bdkrL44OvgL1Z8oCsIHNRvChDuLDRNIp7pjFO_jKKKe7EnxNOPsEOw1R2LfVGD4p-5T8lJIzeF4XiC3uV54hUFJZMpU7F-3JISBIr8Yi1GBvyAoQZc6XYRbL88qRlELbmV2hxULTp1aokbgnVMz0-_rxx1YGBDn4B-y5H-7HMRmLq7-NimDRSCKUFRHLnCbN5g2sZd7DDwIma4zm2NiA_cWgZQzkwkSciQIOdukKQj2vFFFgQJR7x40CI2FbZJfcTz3oBSTxgH5Zr4BXwKgauH36K-B5G_4qThQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند، گفت: «فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این نقطه هستیم.»
🔹
او افزود: «انتظار دارم هر یک از این کشورها در سکوت تلاش کنند تا توافق اختصاصی خود را با ایران برای عبور امن کشتی‌هایشان و تضمین بازماندن پایدار تنگهٔ هرمز انجام دهند. حدس من این است که چنین گفت‌وگوهایی همین حالا نیز در جریان است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445518" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppE0cf2FhCzLIGt6rU-xyUkeapMGIVG4mREYDS8pbAlCS6HI7nl5haQqXssDV92sVG8Uk68YqmSQP1aih_XgxN9eCdDZVNH5ss73DxowAEKmy9JqUqWI-UzmKmWrE86i-rVXQa3rCKZ2xFQZbgB0bGAqTfBBN_Tqwt0tkN7lHvTK3VPwqAH8o8VCTWteJTG3wHePfHTAohQzmmqtBzmh1HqlRCjog0v6_VwkeeS8UnwVbT4D_3wxTe4P5H2SMuwES6mkByKNNDuF8PEy7nxhiHhD6zv97hdyV0Q3W2_4RKZinNeCQLYUVjWhyJRCkT4ApwnWByMN2ZrM5rWrDnzdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پرسپولیس به آسیا نرسید
🔹
پرسپولیس با باخت در اولین بازی تورنمنت ۳ جانبه، از کسب سهمیه آسیا بازماند.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445517" target="_blank">📅 22:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409336ec31.mp4?token=uDm-ePQWUV7QVRIM_Wgf9UaD9obPH9u2ubgB38u5eusY0GfzJwy5nGxLyCdhvdMN_GrjOVK_FfQcJCGLgBRhUtXlurfCSOTsJafxwy8s9eko6OKmrF0ju_vdVVCyipGsHFDNWYDQSGOOgdCcu7X8gjsvGItsUB1myh05hZXhEb1R8ImbyxTsggopUXI57OU0zw0raHXoJBU-ZLTSQOx5C8e1zYlS4w1Z8mQVJekbUuybO4HBcDNg7xrTaOPePRS_mEdzTJz0bE_3Q0H_VubpjupZvnuziMxGs8p9oPsCXGAgrsn4ne2MP_AasANxQu4upuiWudboAr4BDvSGm-Yrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409336ec31.mp4?token=uDm-ePQWUV7QVRIM_Wgf9UaD9obPH9u2ubgB38u5eusY0GfzJwy5nGxLyCdhvdMN_GrjOVK_FfQcJCGLgBRhUtXlurfCSOTsJafxwy8s9eko6OKmrF0ju_vdVVCyipGsHFDNWYDQSGOOgdCcu7X8gjsvGItsUB1myh05hZXhEb1R8ImbyxTsggopUXI57OU0zw0raHXoJBU-ZLTSQOx5C8e1zYlS4w1Z8mQVJekbUuybO4HBcDNg7xrTaOPePRS_mEdzTJz0bE_3Q0H_VubpjupZvnuziMxGs8p9oPsCXGAgrsn4ne2MP_AasANxQu4upuiWudboAr4BDvSGm-Yrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445516" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwS_i56ugYGsFvv49YfbfKMSJE7iKPIrYNlxCtHF4kvwiEM_VdyhigGzLFAs0f38zjazf6RCL_OnEx2LgggF95NNBRJwgSwvk32I8nb_9aaeHGIhoiBizjdI2M00GZHr7vo-F3a0gP0mrFD6S1cxa6HyWKPLBZcCb3L15QljvNoLmvYT4RcScqMDQEsEZhhrhtnZi5Z9nS0x_HZ3td6jQ9rx-RZyIoc_x1nE56O_PDJj-FU1tZ75TID9IzXJvwnmfS9Yb_genq4Jk5p1gI50D-vBmTxWcIw-EWJiTTnLUswMcQoSrMtxk2HJvRZM34fF14N-mmA0FbATbhscPv_8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤓
بعد از گل برزیل ژاپنی‌ها وسط زمین جلسه گذاشتند
@Sportfars</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445515" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376a0180e5.mp4?token=WX2oCc-glLejKNiZd1SEKhqt8vZt9H3voot1jWAzNtZy_wikdu1G4VTDf4SIVMGwer1hTbQPkUkMqTILKOVvqr0tQrr0XRCdHe7hzqxx82CBpuzpurGSqbbHDbkWYdpMMSvDFEBXqKOEfbpaBUgnzzz_CJbS0Rf_2IyszpFzzIJy8Az4GhuOlC0hFMmoVmaX_YuDi9CGwwNUKNjm0-ju6JKlUyrkYt_40bSQjOjeavjVzDqC18cZS_Z25sMKbx_Y_xtduEXUN2LYFcqZ6EPPDLCHgRV0qDiphgvzFU9RZNdK9qYMHbbqNfhlR0BzaTGDT3QsF1tKPbHYwbz34vXJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376a0180e5.mp4?token=WX2oCc-glLejKNiZd1SEKhqt8vZt9H3voot1jWAzNtZy_wikdu1G4VTDf4SIVMGwer1hTbQPkUkMqTILKOVvqr0tQrr0XRCdHe7hzqxx82CBpuzpurGSqbbHDbkWYdpMMSvDFEBXqKOEfbpaBUgnzzz_CJbS0Rf_2IyszpFzzIJy8Az4GhuOlC0hFMmoVmaX_YuDi9CGwwNUKNjm0-ju6JKlUyrkYt_40bSQjOjeavjVzDqC18cZS_Z25sMKbx_Y_xtduEXUN2LYFcqZ6EPPDLCHgRV0qDiphgvzFU9RZNdK9qYMHbbqNfhlR0BzaTGDT3QsF1tKPbHYwbz34vXJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ژاپن به برزیل توسط سانو در دقیقه ۲۹
⚽️
ژاپن ۱ - ۰ برزیل @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445514" target="_blank">📅 21:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
پسرم کارمند شرکت تجاری تو دبی بوده، از روز دوم فروردین تا امروز توسط امارات بدون هیچ توضیحی و جرمی بازداشت شده، نه اجازه ملاقات بهش میدن و نه ارتباط تلفنی و نه حتی اجازه گرفتن وکیلی تا الان حتی صدایی از مقامات دولتی هم در نیومده.
🔹
ما معلم‌های غیرانتفاعی اکثرمون کمتر از ۸ میلیون می‌گیریم. مدیر بیمه را از حقوقمان کم می‌کنه تابستان حقوق نداریم امنیت شغلی هم نداریم ولی مدارس میلیاردی درآمد دارن.
🔸
تو رو خدا روی این موضوع خاموشی چاه‌های  آب کشاورزی  کار کنین. ۶ ساعت خاموشی چاه در شب از ساعت ۱۸ الی ۲۴ و قطع برق در طول روز کشاورز رو به خاک سیاه می‌نشونه و بعد کشور رو وابسته به محصولات کشاورزی خارجی می‌کنه.
🔹
زمان جنگ اینترنت خانگی قطع بود و با توجه به این موضوع هزینه اینترنت روی قبض لحاظ شد و مخابرات گفت دستورالعملی برای این مورد نیامده. لطفا مسئولان پیگیری کنند.
🔸
من اوایل آبان ماه پارسال باید ساینا دوگانه تحویل می‌گرفتم، هنوز حتی فاکتور نشده!
🔹
بنده مستاجرم و برای وام ودیعه مسکن ثبت‌نام کردم ولی هر بانکی مراجعه می‌کنیم می‌گن برای وام ودیعه مسکن هنوز بخشنامه نیومده، آخه یه وام واسه یه مستاجر اون هم  با سود۲۳ درصد که این همه اذیت نمی‌خواد. اگه لطف کنید از طرق کانالتون پیگیری کنید صدای ما هم به جایی برسه.
🔸
تمام پیمانکاران علوم پزشکی بیش از ۴ ماه هیچ دریافتی ندارند و از ۱۴٠۵/٠۳/۱۹ هم دسترسی به تمام حساب‌ها بسته شده یعنی اگر امروز هم این وضعیت ادامه پیدا کنه در بخش پیمانکاری متاسفانه با مشکلات غیرقابل حل مواجه می‌شیم.
🔹
پیرو اختلال ایجاد شده در سامانه‌های خدماتی چند بانک کشور هر چند روز یک بار مدیریت محترم این بانک‌ها خبر از رفع اختلال تا چند ساعت آینده داده اما دریغ از رفع مشکل!
🔸
من یک مستمری بگیرم گفتن ۶۰ درصد افزایش حقوق دادن، در عوض حق عائله‌مندی و کمک معاش رو حذف کردن و کلٱ ۳ میلیون به حقوق اضافه شده که به بیست میلیون هم نمی‌رسد با وجود داشتن بچه دانشجو و محصل با این گرونی چکار کنم.
🔹
روستاهای اطراف ورامین بیش از دو هفته هست که آب ندارند و هیچ مرجعی پاسخگو نیست لطفا پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445512" target="_blank">📅 21:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b58c6c32.mp4?token=WrOzXY-tlkrPo2b9yssMtXfaDKwxnTPUrY2GzW6RqcP2tKyUzFnaBtevchlP0x9-0MHoZat0Y5P-fh22ao10iMvMX0qdChwRwPl8xy_9nKSwyr7v6qHOU1Xk46sKjbGlbnz1ci7suh1MYCaBNApNQ1ArVmNiSctbNoElfrlWq2vNEX0-XAz9Qi6oud-dHI19KHXK_jaioGW-1OR-YQFdHM5wVIX_16xgfUJ69Nr8DloIHtBcBt1WCrE3oA8u2J2JLQfbr523mn6Lfup8XeVoTt7vIszNz04QQGZCvhTCRvWw3d-WfIGKTY8wt4q3hJi_02n_yjcm-UX32xVpxNI6FUHDyS5b8mXkwZGHjrEo80r-eSylhu9fH-Hoqw3q70BTOqXIeHeasCvachbH6pI2dAhDWP0xt7_2BA2-7qdi4OQFJukoD3uHN0gg7p39I68r7lDDm85MXPo8EArPR-yt6m9XiJZ_Hlqlf4GP4cafhD2ty4jCcOSNbx3Odb_5l6y_DrFXN9gvHmues2CnHLZERm2AyCsRI_g19ixVgrIX2P3Ru5bAPmgRM5Pru3sEvUOImVdhEdk9rDa4MS4HkN6xeKFVo3e_UowMOJnKi4GsDkFUd5W7fkVYhKP-Sn689kUnB25qck2y6CFCQVVYGXrtsjt-h-rtVNJONfw7XZpTXqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b58c6c32.mp4?token=WrOzXY-tlkrPo2b9yssMtXfaDKwxnTPUrY2GzW6RqcP2tKyUzFnaBtevchlP0x9-0MHoZat0Y5P-fh22ao10iMvMX0qdChwRwPl8xy_9nKSwyr7v6qHOU1Xk46sKjbGlbnz1ci7suh1MYCaBNApNQ1ArVmNiSctbNoElfrlWq2vNEX0-XAz9Qi6oud-dHI19KHXK_jaioGW-1OR-YQFdHM5wVIX_16xgfUJ69Nr8DloIHtBcBt1WCrE3oA8u2J2JLQfbr523mn6Lfup8XeVoTt7vIszNz04QQGZCvhTCRvWw3d-WfIGKTY8wt4q3hJi_02n_yjcm-UX32xVpxNI6FUHDyS5b8mXkwZGHjrEo80r-eSylhu9fH-Hoqw3q70BTOqXIeHeasCvachbH6pI2dAhDWP0xt7_2BA2-7qdi4OQFJukoD3uHN0gg7p39I68r7lDDm85MXPo8EArPR-yt6m9XiJZ_Hlqlf4GP4cafhD2ty4jCcOSNbx3Odb_5l6y_DrFXN9gvHmues2CnHLZERm2AyCsRI_g19ixVgrIX2P3Ru5bAPmgRM5Pru3sEvUOImVdhEdk9rDa4MS4HkN6xeKFVo3e_UowMOJnKi4GsDkFUd5W7fkVYhKP-Sn689kUnB25qck2y6CFCQVVYGXrtsjt-h-rtVNJONfw7XZpTXqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: دشمن تسلیم عقلانیت شهید لاریجانی شد
🔹
دستیار رهبر انقلاب: شیهد لاریجانی هر جا مسئولیت گرفت ترازی را به‌جا گذاشت که کسی نمی‌توانست به آن برسد.
🔸
همسر شهید لاریجانی: ایشان پس‌از شهادت رهبر انقلاب، به‌شدت دنبال شهید‌شدن بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445511" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445510">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOpl_To22VESfXQze3Ar4jyDoSCN3rgq-kwyvoJbEMnuNfSk97OWvjZcMOE4w4CC4kuzbxIPl86IOH3O5B10UuYyIFfnGySZj5BuZba87F-TjrguWrS8Mve8E45EBxQzTlGvhXRYenU2I6H0yLNDbVezx-1MgAAWhA6BTMdAot98xFl5PQlTo8iF2KGay18a1v5r7_Qt7GGt0l4F_Dr1FzflMm9wn-ffU0taUUuwcmfr6SQDgEvx-N_LaoUY-uhcoDU60IMlIfRlsy2auoyNLxvHHILge5B00Jm32TT-QbKjHBNC6rNfyjHYk_biGxsU3C70vR3N6Y2UQkuOWhy-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
همدان، میزبان پروژه‌های جدید توسعه شبکه ایرانسل شد
🔸
با حضور وزیر ارتباطات و فناوری‌اطلاعات، سایت 5G ایرانسل در شهر همدان و یک سایت ارتباطی روستایی در شهرستان بهار، به بهره‌برداری رسید.
🔸
این مراسم، ۸ تیرماه ۱۴۰۵، با حضور وزیر ارتباطات، نماینده ولی‌فقیه در همدان، استاندار همدان، رگولاتور ارتباطات، مدیرعامل زیرساخت، معاونان سیاست‌گذاری و استان‌های وزارت ارتباطات، مدیرکل فاوای همدان، نماینده همدان در مجلس، مدیران استانی و جمعی از مدیران ایرانسل، در قالب جلسه شورای اداری استان همدان، در محل استانداری برگزار شد.
🔸
پروژه‌های توسعه زیرساخت‌های ارتباطی ایرانسل در استان همدان، شامل افتتاح سایت 5G در شهر همدان و بهره‌برداری از یک سایت ارتباطی، برای پوشش روستاهای باباعلی و قشلاق همه‌کسی شهرستان بهار، به نمایندگی از سایر پروژه‌های ارتباطی ایرانسل در استان، به بهره‌برداری رسید.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445510" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbJNaeOMmkcss8p4kkskvnqKKt3JKR7Mqks_uWAjE3QgILJ_ilfunLPHNjKOyAmOK3zPhC7Dj0tXefxbbNDOywRCNIfR6ttOxIIwwJ_QSzD9nyCA-eGoKo72kTCQdhtVI2tzG05kmm8TnA9vRryE_7En6GNG6V57RvV0lnftPslzn8zkjYOMLOjluDsX3osR7_bCF5dfAcyE3DeKJN0SiMJ1p5hg6_3NfeJFrdaLHS3IfUK2Zzep7GUWCrYOG0pd9BVn2HQNHzEAfORnKtZj0TNxmHm-7W48G-jza8fY3wpjaPL-FgnrHYISV_-2rj9NWWQeZIYt28sR0ki_zVPdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
😎
بانک سرمایه در مسیر بهبود؛ موتور درآمد سمایه روشن شد
⬆️
رشد قابل توجه درآمدهای عملیاتی
⬆️
بهبود شاخص‌های سودآوری عملیاتی
⬆️
جهش دارایی‌های بانک سرمایه
⬆️
تداوم اعتماد سپرده‌گذاران به بانک سرمایه
◀️
بررسی صورت‌های مالی ۱۲ ماهه بانک سرمایه برای سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ نشان می‌دهد که این بانک در مسیر توسعه فعالیت‌های عملیاتی، افزایش حجم کسب‌وکار و بهبود برخی شاخص‌های کلیدی عملکرد قرار گرفته است.
🔗
متن کامل خبر را اینجا بخوانید...
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/445509" target="_blank">📅 21:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/445508" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53498f66b.mp4?token=cHRKoyNuO3GbPgz2GSNprOtIyJZXbqzqedfAAj3lthcBqHc23Nz1vjgVrnYrrRKuYydFhzvBtFasMF27l-A1uNqn6k2PCnyPXutNRkjLjCm4dFoFGEXrQa_Bx2hCV-3BB-eGme7k0TDujHMmG9TRoxTx0p5bDi8GMVbnHhQ5pap8CGhWCOMIqPKiIdLnYCBSxmsdWl6gML8_7amGYduBbXslKfxRswNc5ZOEVRdijEOQRe7Z9H7kxxElfy7abUrArnH_sXkdJpfHtb7G3iDMx4MENpWzrlTBgvR3zlRxrYNF-GfqsjflaDjrILI2eTVO0CpTBJ0gVtI1NyFGcdmr5a0eePDN0P7RjeRZLk-knZ99K--iSMINJEWbMnN3_ahJOJkOtWRdjMPfTJ0_Rhnolwrxtr3i5RK4IG67C0apCo7IIK0wYKYajIrJIQTsjjirs7-lYBse40pMWLaMVRj3u1fha6Ko4QsxTILECOn_80J9kgzbrUI5z2ZgUqItSbIfe3BaaIIr3gkCu88XNp9YV4IFmiL3EWLKMsjJhieGoho9XsX_X6gHlP_Tqpk4bAwBwbvQyRCabYFwhc9zWQD4xCzoFJobMEw7y1l8qH8OAmX0HWO7rTrRTXtN-G22kPdY2XkczqQWIBWa29K0Xw0zJpMobVqXsfkLVSPQ-YknXO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53498f66b.mp4?token=cHRKoyNuO3GbPgz2GSNprOtIyJZXbqzqedfAAj3lthcBqHc23Nz1vjgVrnYrrRKuYydFhzvBtFasMF27l-A1uNqn6k2PCnyPXutNRkjLjCm4dFoFGEXrQa_Bx2hCV-3BB-eGme7k0TDujHMmG9TRoxTx0p5bDi8GMVbnHhQ5pap8CGhWCOMIqPKiIdLnYCBSxmsdWl6gML8_7amGYduBbXslKfxRswNc5ZOEVRdijEOQRe7Z9H7kxxElfy7abUrArnH_sXkdJpfHtb7G3iDMx4MENpWzrlTBgvR3zlRxrYNF-GfqsjflaDjrILI2eTVO0CpTBJ0gVtI1NyFGcdmr5a0eePDN0P7RjeRZLk-knZ99K--iSMINJEWbMnN3_ahJOJkOtWRdjMPfTJ0_Rhnolwrxtr3i5RK4IG67C0apCo7IIK0wYKYajIrJIQTsjjirs7-lYBse40pMWLaMVRj3u1fha6Ko4QsxTILECOn_80J9kgzbrUI5z2ZgUqItSbIfe3BaaIIr3gkCu88XNp9YV4IFmiL3EWLKMsjJhieGoho9XsX_X6gHlP_Tqpk4bAwBwbvQyRCabYFwhc9zWQD4xCzoFJobMEw7y1l8qH8OAmX0HWO7rTrRTXtN-G22kPdY2XkczqQWIBWa29K0Xw0zJpMobVqXsfkLVSPQ-YknXO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۷ سال هدایت ایران توسط رهبر شهید انقلاب از دید رسانه‌های خارجی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445507" target="_blank">📅 21:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMoSuwI8JAOL0UdKFnA3CocLSAy8IZt1G240xAWn82FT43GgFq1HWXhaUm8tsDzsPgAr7UpeXmQN8sgtQMm_Edyg2zPB_tl4G4xx6ChwAVXyoLFZX93AOJhp5gZ-cB3tRkmg4J7TX4aS1RQA983GeUE99cLv2WC0JRwO3vJsv6_IgYJypZGNzPTDAhxTbaDSTJznsq6GKfMnI3tQFFkmTBLsqawJTwRfOmWXDhGZtQ3rie0QMmrKOJ0hqhlgnYBRuw9GB9qNNHV2aKZ0Du3xZj6P2-Yxys7oNgZeWvMWvChKPe2sbpPsMQATyfIjmn25ZNhY_hsdRhf8QTQcyp0log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید عارف از بی‌توجهی بانک‌ها به امنیت سایبری
🔹
معاون اول رئیس‌جمهور: اتفاقی که برای بانک‌ها رخ داد را حتی نمی‌توان حمله سایبری نامید؛ یک دانشجوی جوان که فقط سه واحد رمز پاس کرده باشد هم می‌تواند چنین کاری انجام دهد.
🔹
بسیاری از کسانی که در شرکت ملی خدمات انفورماتیک یا بخش‌های دیگر فعالیت دارند، از دانشجویان من بوده‌اند و بارها به آنان هشدار داده بودم که ممکن است چنین اتفاقاتی رخ دهد، اما به این هشدارها توجه نشد.
🔹
توجه به امنیت سایبری برای دستگاه‌های دولتی دیگر یک توصیه نیست، بلکه یک دستور اکید و الزام است و مشکلات فعلی باید هرچه سریع‌تر برطرف شود.
🔹
برای بلندمدت باید راهبردهای جدی تدوین شود. متخصصان امنیت سایبری در کشور حضور دارند و با دانش و فناوری بومی توان مقابله با حملات ده‌ها برابر بدتر را داریم، من تخصصم این است و مسئولیت این ادعا را می‌پذیرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445506" target="_blank">📅 21:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adaa31060.mp4?token=gjFJo9FiWkvXABOs14838AtQk_zxcnymNLWhhwDaFvdVItsDjADC4XuZl1VN5lqxmDIYcyvJJJmnxqB_mX-VeVCasiEtJJo9gpLFAxjYsr6u6QlteFWx52DSCdXWnMFqTgobrKgRmHwnCECpTZJMrR3ly-1fmdrcK1E5iwPm87iZB7qITp7kbsrGixwLvABIBaZYc7CR7fJLOkc9ZYINE0Itry-g2B8_klog2lLlZFP27fD2pvviM_xkURcXldWr8BP_Mu08uWgsFZ7mZmUEbiGLcifAIY3-vIQNNDWA67jXqpuYn3YwEsmBZmpsE2v0J3rLZeKJ0x5JB7bt1gYNfl1J8_W3trVYLYmICVrZFOZNT0IRRfmGxs7hDBbUKQ4CBMAHMBjR4Kq9DT8KeVQOeuv_uq2H0s4hm7Zi_9lzLF-jaXlx2B28tSixHjQbnNSrv7B0_IMJJ2QNX1udoQs3T0PSZC62ZfXyJxGF9aLnSrTqRhrKJQBv7e5tcUZuUyW4VSFmMN6DnMSkk0Hz-txrGaVL5TdF7BnlzbASwN13gFmmzeizsXYb0tHOXoafFv9A77EoYvfU02SDhX_o8-BVqCIyPMTvhOoh8Q_HEINkqudqcRsNe7DalEQ5un12OA9Kiv9OM7YJF-hpkHJNfH8k-5boxj4hLbX1GAv_aM1emLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adaa31060.mp4?token=gjFJo9FiWkvXABOs14838AtQk_zxcnymNLWhhwDaFvdVItsDjADC4XuZl1VN5lqxmDIYcyvJJJmnxqB_mX-VeVCasiEtJJo9gpLFAxjYsr6u6QlteFWx52DSCdXWnMFqTgobrKgRmHwnCECpTZJMrR3ly-1fmdrcK1E5iwPm87iZB7qITp7kbsrGixwLvABIBaZYc7CR7fJLOkc9ZYINE0Itry-g2B8_klog2lLlZFP27fD2pvviM_xkURcXldWr8BP_Mu08uWgsFZ7mZmUEbiGLcifAIY3-vIQNNDWA67jXqpuYn3YwEsmBZmpsE2v0J3rLZeKJ0x5JB7bt1gYNfl1J8_W3trVYLYmICVrZFOZNT0IRRfmGxs7hDBbUKQ4CBMAHMBjR4Kq9DT8KeVQOeuv_uq2H0s4hm7Zi_9lzLF-jaXlx2B28tSixHjQbnNSrv7B0_IMJJ2QNX1udoQs3T0PSZC62ZfXyJxGF9aLnSrTqRhrKJQBv7e5tcUZuUyW4VSFmMN6DnMSkk0Hz-txrGaVL5TdF7BnlzbASwN13gFmmzeizsXYb0tHOXoafFv9A77EoYvfU02SDhX_o8-BVqCIyPMTvhOoh8Q_HEINkqudqcRsNe7DalEQ5un12OA9Kiv9OM7YJF-hpkHJNfH8k-5boxj4hLbX1GAv_aM1emLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم به ملی‌پوشان فوتبال: ممنون که تمام توان خود را گذاشتید  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445505" target="_blank">📅 21:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7ddad6e2.mp4?token=hMOjdKTQhtNcMErUmELZg7LjMHkrLoIk39p_9mlra3uotAUPvL_XOCGJZf5oDD6EogikLai69cgZ6HwA6OpepjnNFtwfb7BbdqcgkRVcBjbtluL18OHxu7AR4c2PoZ9fgCz_TgEyGrpwqbQaNCOv_yTOS_K4ZYKyTgcBYLKOzzNx3aeeOW5FixfvnGyH97KhSjosQ5bV95k7ubI8v7YCbZcpZYXIv4AFYRadppNryE2tRQ4DucrGDfUwUq8nvmo9CgwIodUjz58XHceEsRL1vUebP1eFqagleHJbSu7DMzjGTo_AGENBvIjU273Kw3Colv5WhgWyVnrOCscc0yTsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7ddad6e2.mp4?token=hMOjdKTQhtNcMErUmELZg7LjMHkrLoIk39p_9mlra3uotAUPvL_XOCGJZf5oDD6EogikLai69cgZ6HwA6OpepjnNFtwfb7BbdqcgkRVcBjbtluL18OHxu7AR4c2PoZ9fgCz_TgEyGrpwqbQaNCOv_yTOS_K4ZYKyTgcBYLKOzzNx3aeeOW5FixfvnGyH97KhSjosQ5bV95k7ubI8v7YCbZcpZYXIv4AFYRadppNryE2tRQ4DucrGDfUwUq8nvmo9CgwIodUjz58XHceEsRL1vUebP1eFqagleHJbSu7DMzjGTo_AGENBvIjU273Kw3Colv5WhgWyVnrOCscc0yTsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ژاپن به برزیل توسط سانو در دقیقه ۲۹
⚽️
ژاپن ۱ - ۰ برزیل
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445504" target="_blank">📅 21:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۱.pdf</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/farsna/445503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۰.pdf</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445503" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔹
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445501" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445500" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های مسدودشده ایران، نیز فرآیند اجرایی‎‌شدن آن درحال پیگیری است.
🔹
در این چارچوب، همین هفته هیئتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445499" target="_blank">📅 20:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aad982d1d.mp4?token=e8D8oWDZjhOqXqV98x7IRDuAGS8uuDq7JffKOunSDFSuMXRHaM1fRx4OTVWKtn752zkXAR_tpcO27Z23eqfzOhYyPdi5hKIC7xEa8rF31b9bM9qMsrrA2-z_Cu3XDMD4kWPYcVO3cc8J66ITkLAxhH3Ofl36IZcEVYXP6f5xXtpId3At7mXUe1krDjhA5KijWfYXApg1nx6uE0-0GbJ8KXg8ccXd7aky0Y8bkNI-OH07D_ejVHpEXIpOdSmo8Sq6UN38Oa1lJkocp3KC3gMoz59XmVEDwR7BCyNKwXq-lJxdobQwU_9aAVzGIRRRpu67aIdA8OVZXY2uZbQ3DzjZBmI--1FiI9DI-NSpqZmwQAF8mM87HH1xdyY55LLBTtUD6g6y4Ndy3wR-cZzD0GLVJz9cOie3bgKezvl0jrY91o83g8g1aQsJADebZ0j9DT_vCHVJ9JtPQMPrIllC_v3oHeV_hCQVd_guKAEorA69wRyFXKmibXtVsiKXEH9PYxP9m6PrcpFipls9Z5yQgAfSjn4eQxNhmTZ-57BZ_GlFjLxwQZsYP_bRP6REQUO0_tRUKBeK_bEcq7hAQYBGZs53_WZA4dgWLp6LeWRvxQoK5jWxmgpm_ETzbp5jr44pn9YeLlkNXFR5U2AqwJEA2Sfz8ZIXAmvGnMihKGE3YrTzWfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aad982d1d.mp4?token=e8D8oWDZjhOqXqV98x7IRDuAGS8uuDq7JffKOunSDFSuMXRHaM1fRx4OTVWKtn752zkXAR_tpcO27Z23eqfzOhYyPdi5hKIC7xEa8rF31b9bM9qMsrrA2-z_Cu3XDMD4kWPYcVO3cc8J66ITkLAxhH3Ofl36IZcEVYXP6f5xXtpId3At7mXUe1krDjhA5KijWfYXApg1nx6uE0-0GbJ8KXg8ccXd7aky0Y8bkNI-OH07D_ejVHpEXIpOdSmo8Sq6UN38Oa1lJkocp3KC3gMoz59XmVEDwR7BCyNKwXq-lJxdobQwU_9aAVzGIRRRpu67aIdA8OVZXY2uZbQ3DzjZBmI--1FiI9DI-NSpqZmwQAF8mM87HH1xdyY55LLBTtUD6g6y4Ndy3wR-cZzD0GLVJz9cOie3bgKezvl0jrY91o83g8g1aQsJADebZ0j9DT_vCHVJ9JtPQMPrIllC_v3oHeV_hCQVd_guKAEorA69wRyFXKmibXtVsiKXEH9PYxP9m6PrcpFipls9Z5yQgAfSjn4eQxNhmTZ-57BZ_GlFjLxwQZsYP_bRP6REQUO0_tRUKBeK_bEcq7hAQYBGZs53_WZA4dgWLp6LeWRvxQoK5jWxmgpm_ETzbp5jr44pn9YeLlkNXFR5U2AqwJEA2Sfz8ZIXAmvGnMihKGE3YrTzWfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تذکر پزشکیان به مصرف غیراستاندارد برق در سازمان استاندارد
🔹
در بازدید رئیس‌جمهور از سازمان ملی استاندارد چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/445498" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHEJWQnt7glYNEtAIR0YCGBCH_nvbhC9XDLcYG2v0dptLT8FcrAbRf5NjKqSN3egac9hBm74NnWg2neuBJpGLs15jFmxPJo7cNpnlqSYpYkIwgTJGd-bY-p-b2PjPSeO7HUwp4Wf8X1SpT4JFYXm76MOm1fD47KWqBQdxpA4194YEjQTTh3zDejv1lWyyVNf6-sRe8Guzu36fePD3bz-3C1HDTyaLHSf-WisjdEbnfHiUKxL5qeUpaLR8yuP6Pp2wZbw9ru-iNJbWOSyLQgLmGyY2mPNxXuDHZqvQinSjiJSbhpxY_2Fm4Fo3SLU8Tj5Uq-kWkwLwEd8f6bmaoiMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و دریادار دوم اکبرزاده به مرکز درمانی منتقل شد اما وی به‌دلیل شدت جراحات وارده، جان باخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445497" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=dU94GBO3JAvSPpCaBm7sRm-w_s6JLE0iS1MzhLhiXO9W3Gdh-sDZWgVx-z1W0v12a-hy0L6R4leSKlbtM2IHBoKorAkYj12WiVy3b8y6JkKc2YpoKq-W3r1S80Php0h2hrj2XY1IX0bpQeaFGmDXNtysdGKiaTV_zkb5C0ZvrqTlIoL-4lxwxJrtqLyfVOeyIL8GCRPHXAK9A6EwuxEv7hXWL6LrVZEN7vEC9--vq-V3Rp_7xWp4sZm4LcUlRATUOZkLaj4XzD4nffS1reqEUypDsAJbUfNI9tkG1ZmO9YvpXoJYvOl9EjkRhvDvkyjMpDeM_Dv2xfbmYHHMEEFB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=dU94GBO3JAvSPpCaBm7sRm-w_s6JLE0iS1MzhLhiXO9W3Gdh-sDZWgVx-z1W0v12a-hy0L6R4leSKlbtM2IHBoKorAkYj12WiVy3b8y6JkKc2YpoKq-W3r1S80Php0h2hrj2XY1IX0bpQeaFGmDXNtysdGKiaTV_zkb5C0ZvrqTlIoL-4lxwxJrtqLyfVOeyIL8GCRPHXAK9A6EwuxEv7hXWL6LrVZEN7vEC9--vq-V3Rp_7xWp4sZm4LcUlRATUOZkLaj4XzD4nffS1reqEUypDsAJbUfNI9tkG1ZmO9YvpXoJYvOl9EjkRhvDvkyjMpDeM_Dv2xfbmYHHMEEFB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو، عضو رسانه‌‌ای تیم مذاکره‌کننده: فروش نفت ما کاملا به شرایط پیش‌از جنگ برگشته
🔹
ما قبل از این مدت‌ها ارزان‌تر از قیمت جهانی، نفت می‌‌فروختیم اما حالا بالاتر از قیمت جهانی می‌فروشیم.
🔹
همچنین حدود ۲۰ تا ۳۰ درصد بازار جدید در فروش نفت پیدا کرده‌‎ایم.…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/445496" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt3SKvLpk6ZoVL2JKATErbCWBFePgjJX8Hswej19lESz_YPyqggrgp8fFIrKF0gL6OO_IOxBof2508fpeFEBBHol1SMeBm0zgzvIhxidk0mHn3hXOPvqxRnqqqaTU1psgzOfCp_jYdVTFKcEGuZbe2DCIBak5fQm8SD16ePFAhjFCNa_uEDq9bbmdKjVmh-jRCSOE8s7KxqkWVA6vwXQyDIS4e6W8LvAWlniSkcNvybWN1s5ftS1JTwZhUlMkRJIU8SA_HYL8gNyrYAmeucSCTLjcmEcvDpZBG64sy6yUDoeqIl7kO5WTJquOXtM50i0aCXWq33EDK-QjcOIizQi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت شرکت اسرائیلی از مانور قدرت نفتکش‌های ایرانی
🔹
شرکت اسرائیلی پایش دریایی ویندوارد می‌گوید که یک نفتکش تحت تحریم آمریکا با پرچم نروژ در حرکت است.
🔹
این دومین مورد در یک هفته گذشته است که یک نفتکش ایرانی خود را در ریجستر اروپایی نشان می‌دهد؛ مورد قبلی یک کشتی حمل گاز مایع بود.
🔹
این شرکت اسرائیلی می‌گوید که این شیوه جسورانه آشکارا در برابر دیدگان نهادهای آمریکایی و اروپایی انجام می‌شود و یادآور نفتکش‌های غول‌پیکر ایرانی (VLCC) است که ۴۸ ساعت پیش از امضای تفاهم‌نامه از چابهار حرکت کردند و محاصره را شکستند.
🔹
ویندوارد معتقد است که این اقدام پیامی دارد و آن این است که ایران بی‌توجه به قوانین آمریکایی به صادرات انرژی خود ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/445495" target="_blank">📅 20:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون بین‌الملل وزارت خارجه: مین‌زدایی از تنگۀ هرمز صرفا توسط ایران انجام می‌شود
🔹
غریب‌آبادی: «ماکرون گفته در مین‌زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند. طبق یادداشت تفاهم اسلام‌آباد، مین‌زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازۀ چنین کاری را هم نمی‌دهیم.
🔹
شرایط حساس و پیچیده است. توصیۀ اکید می‌کنیم فرانسه آن را با تحریکاتش پیچیده‌تر نکند.»
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445494" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
