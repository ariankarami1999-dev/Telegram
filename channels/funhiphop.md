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
<img src="https://cdn4.telesco.pe/file/v4J_wmhnvi09g4PHGHxRke6JOJlFprpkYMSt1zDkpwykMfmF55yY05Fx_n5MifjboSFUPr_dKeFYVoAwKf1ldcWOmebw-MLgctbYFkUM29dxttgdhcA9KUTh0iVJF4ZoGiH4OENvQY5xrk5aQx_zR3C3XPiMBJIEx8omsYVykXF-32ZZh_KOpbolIv9yTBHz0_7gy0z8M5GnDG9er24s8-zc8mwjqhjdCg67dl2ePTAwyEpjpdW3U7Pn1QA0OD6lk1i82QbIq2FBzOeLENhv4lA1zIY63Ev_M4M1sBWxX6zZACZYpTrORaB3ZR9i1OzHwuIoerkPWGGFy9VufIc1xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyf1hdgO_EO_BwFhQ0UgO8QFMe3UtTjLq022F2ZS6FjFJKFdUt1OOaKNsqGIWPtnXw_TUqCiqFL7GeWEg-TuJMTAnaxct_wetwQn30YEsL_ZGqm1JTztIHmmNuq8MZ_IKQzrRnAddb8YoZFnUTM02RvDppYD_-QISuR-iRGnIYgVP91h1R8toE6bClpIxRo5LyGy1otz3tPJuzxlPRHRDcvaU7ykoQk8XzVNs-jJoqObLhN4j1b8dWdAhPrGpGSbTpP-8TUiJFZKEDFdzBf5bJKnbSvWTqW5pqUfzB9PZSxm8Lw66ImXhGI7PMiqy1ku7neosyLBDgn53pl8C6Vh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا نه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/84070" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه مردی رفته بالای ضریح امام رضا گفته من ۱۰۰ میلیون واس زن مریضم نذر کردم الان فوت کرده پولمو پس بدید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/84069" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152539b735.mp4?token=MmpmhS2V1EIscqjxJ6jeR5a_t1Zp6oqVXyZUGWIHBdWs4BidqPjh89sj4utvXoxsrCXxA3NSRLiOWFfh9kpnSgD6FMk7u1PnyE8pXoUMZTMUtaKJMuKJ67NC1Mk1NtjkVTdxG5vgZdqGlkPHqkFc69Ngc_KhvKEz6ljyXZYUmhEdUn1MZoQgXtl5yT4DCj2NSe8nBB1D6dXE0jnvirl29ybPjjfOrWgvbUtaSLxs7TgAJA80M5nGOrrKuOkN8f6SzcqBRF4O8tuc3FvKXgZQIEma_uNvs4YDb92wg1EKPmHImMX89EjFKYTZ84ddE41YRbdbhy_dxlOH6ZRfigxPzUK_TPXgBYHO0H6Y_WEcsdkAwgj1ClJtyr3J-kcFl43nx79svBgnLvaxvk6uU2gIBlp4WthfYUZZuQch0zQ8qtBgMLlmv_GATAkhSeX0vnTsgopfQZZzS1OfT3RdgE7svWUI-NcQTiOsV4so3JuvOphRjKWGvDu7AT-UqzqeomXMw2v2VYZPBg1szrQveP8gyctBEWcCJ8vzgSIZnnfSaJc4hxmMesW5-lJ_lAobsckgAN4GugEFku8EubHqIu6WDRpzmbnG7H8ht90cZnomfyRZjbmNnOXYroHowvrdlZ3EnF70KpO5eyGlzgp9VxDajeqsFHXWJmlFUg_r_Rg_Lyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152539b735.mp4?token=MmpmhS2V1EIscqjxJ6jeR5a_t1Zp6oqVXyZUGWIHBdWs4BidqPjh89sj4utvXoxsrCXxA3NSRLiOWFfh9kpnSgD6FMk7u1PnyE8pXoUMZTMUtaKJMuKJ67NC1Mk1NtjkVTdxG5vgZdqGlkPHqkFc69Ngc_KhvKEz6ljyXZYUmhEdUn1MZoQgXtl5yT4DCj2NSe8nBB1D6dXE0jnvirl29ybPjjfOrWgvbUtaSLxs7TgAJA80M5nGOrrKuOkN8f6SzcqBRF4O8tuc3FvKXgZQIEma_uNvs4YDb92wg1EKPmHImMX89EjFKYTZ84ddE41YRbdbhy_dxlOH6ZRfigxPzUK_TPXgBYHO0H6Y_WEcsdkAwgj1ClJtyr3J-kcFl43nx79svBgnLvaxvk6uU2gIBlp4WthfYUZZuQch0zQ8qtBgMLlmv_GATAkhSeX0vnTsgopfQZZzS1OfT3RdgE7svWUI-NcQTiOsV4so3JuvOphRjKWGvDu7AT-UqzqeomXMw2v2VYZPBg1szrQveP8gyctBEWcCJ8vzgSIZnnfSaJc4hxmMesW5-lJ_lAobsckgAN4GugEFku8EubHqIu6WDRpzmbnG7H8ht90cZnomfyRZjbmNnOXYroHowvrdlZ3EnF70KpO5eyGlzgp9VxDajeqsFHXWJmlFUg_r_Rg_Lyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثمره های اون میلان رویایی ۱۹۹۰ تا ۲۰۱۰ دارن میرن دانشگاه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/84068" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/84067" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=DPUfgVwwqegvGYLrWQ2THQGUPq_YqNipSpkqzIhKheAQ8pjQb9CcZLegkDKdUN-M1cfE05YDT5eojQDnTCa5nDkZNNaoqtylshhJq0BPmkpftCAT6Zq_Bf8MvC9Gx7flD9j33ahZT8qiHo1ZmEE-NcY8FmxRzcq7pQCmTSYWEOWoMGDgoOaLGsvRBXyj39q1vc6nTVabPP4Gn-l13noe3t9wRAKB28VI3IBetCP1jXXuDR0y5gNZ4A-As4GDnVRiWhOZl7RlYCLWnIJ3_fKJ9pWie7TRsYJtL13AECsdLp0I_bH_axUWL5wKE_DxV9KGYbVc2DHm2PRS9OYU-xSGFZRt07TEcSk0HXjEQHQbaK_3Sn1rGFuGcJpnpqn3Ok1HZihD6hEIHDd99-UY3w4C--k1SaxUOjypud3WCd_gRFPxIFju1OuW_NbGkCM1yJN0aj7ijKdTZKyE68IEIF8ZUYr1ieLEzt5K7bBvAgHaadI9xR0STG64tv0UHb52GoONoFvDi5OqHkzVTaSifO3GzfTy5LsEY8b5XpQvlG_T8qkSg_b1dcMHMpxyakSTcwO3R--VLIEPlae2aWWLhuZWELwkJATBKYR2sCKt8mh6tbBdlA2JFQlVVsyeloW8UaRcqJAHy4Lshm8WVWg4jmi0MfZdnjZgP7gvC8CLTBk10gY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=DPUfgVwwqegvGYLrWQ2THQGUPq_YqNipSpkqzIhKheAQ8pjQb9CcZLegkDKdUN-M1cfE05YDT5eojQDnTCa5nDkZNNaoqtylshhJq0BPmkpftCAT6Zq_Bf8MvC9Gx7flD9j33ahZT8qiHo1ZmEE-NcY8FmxRzcq7pQCmTSYWEOWoMGDgoOaLGsvRBXyj39q1vc6nTVabPP4Gn-l13noe3t9wRAKB28VI3IBetCP1jXXuDR0y5gNZ4A-As4GDnVRiWhOZl7RlYCLWnIJ3_fKJ9pWie7TRsYJtL13AECsdLp0I_bH_axUWL5wKE_DxV9KGYbVc2DHm2PRS9OYU-xSGFZRt07TEcSk0HXjEQHQbaK_3Sn1rGFuGcJpnpqn3Ok1HZihD6hEIHDd99-UY3w4C--k1SaxUOjypud3WCd_gRFPxIFju1OuW_NbGkCM1yJN0aj7ijKdTZKyE68IEIF8ZUYr1ieLEzt5K7bBvAgHaadI9xR0STG64tv0UHb52GoONoFvDi5OqHkzVTaSifO3GzfTy5LsEY8b5XpQvlG_T8qkSg_b1dcMHMpxyakSTcwO3R--VLIEPlae2aWWLhuZWELwkJATBKYR2sCKt8mh6tbBdlA2JFQlVVsyeloW8UaRcqJAHy4Lshm8WVWg4jmi0MfZdnjZgP7gvC8CLTBk10gY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند در فصل آتی فوتبال محیط امن و حرفه ای برای عاشقان فوتبال و هیجان
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/84066" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حاجی جیبارو بچسبید پیشرو میخواد پک فیزیکی بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/84065" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RogGRB34rEPoBNMWG6T4txf69jPJakHOGbwBs5JPbg1vRcBYfX8wuf8in-NSw45FWEr-7z1xGS73-0d6-mmBhIEJ3alVlBGvcpuOhZ_K1ekYjHQGuLVkedA-6wtKqNtLHhVkH9_LPG9OxJAsXPMGtHiymDsLm7a7QVm2jxb9XG0lhEbSOi_Yq0MpmhI2_BiAE_B995jpbfYQEKBOYD_fHmLlk41V-tYU-PkT-gQBRAvYJ5ic5WcCUTLNMAlvu6_Pxj4A1vBFQi61A6U05WwWyNkv5MFnrk-aqRW6N4QeodmIH-9H48eOPIEiS6uUpSbDg2CfuF1E1EnhJx9NQyqnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یچی جدید بگو پیرمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/84064" target="_blank">📅 18:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رضا پیشرو و تهی امشب آلبوم میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/84063" target="_blank">📅 17:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUvMVq0hKgjZW_dnetzYqWVcINYAfoCTcs7wBqva798lZxkG-Tbyd2vcUiLCfscVyXTs8Eh6P7qIETBmyo2AvKQa09MlFsKJPdxUZxsi7YXynNAKhDql4O-W-1cI0JqAJ9Iscv7tYMynWbPji7I87uxHd6AWNW1m_b3B5oLuLVq080ZqCaLB8B8GebIi7UdFGijwZJ0Eh_njaCqjKbVEX9pHLGkkgiQ9jxTmBu1XKSzA2ZinaZdzDglIPhedg0faYI-5as4ialeI8YRaKf3JMVgoAmIZr7iNcPe8FX0XHNJmd73YUYqVw9UktwbBlBjL_bWf0Zs1It4w6x7vlVN_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست بسیار شوکه کننده و بحث برانگیزی که ترامپ دقایقی پیش منتشر کرده است.
طبق بررسی و تحلیل‌های بنده، حتی احتمال تعویق هم ممکن است وجود داشته باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84062" target="_blank">📅 16:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">داریوش تو فری استایل جدیدش تحت تعقیب کمپ اعلام کرد بالاخره ترک کردههههه
🔥
🔥
:
انقدر پاکم می‌گن نشیبولوسعتاااان
🔥
او همچنین در ادامه‌ی بیف قبلی‌اش با هیپ‌هاپولوژیست، به او چند تیکه انداخت:
کونی، دکی فقط داکتر دِرِه
🔥
راستی فکر نکنی لندن پارک‌ها سیفه (احتمالا به دلیل افزایش جمعیت مهاجران غیرقانونی در انگلستان)
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84061" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اونایی که فک میکنن سیتی جریمه میشه یا قهرمانی هاش پس گرفته میشه، یا نمیدونن شیخ منصور کیه یا هم ایکیو زیر ۶۰ دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84060" target="_blank">📅 15:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ری اکشن خنده بزنید تا من یه جوک پیدا کنم و ادیت کنم اینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84059" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=sWtOOig3VhWsH9U1sluU2Dc4z41u4fmDoc2mM3nkBdgNmGwVgd4OeFoaJhmviUxse9RT9JVzumquUMlj5yAtSzIL6i9CI7HTJcbP_53yLVwKUWrn9v6I4osLZTnMDRbwbF284rb0sDjhT6Wf8FJStiACCpwFw7C_I23COtmHFZRpoIyz1HBLq8vvLgZGaHEK6Q50qxUB2VSR4cmzNDDI8jd7NoAtIqmLsgH8lfXS-YplOic7Zjpynr6FRNnCfEyoL0jmBJmrcwA_rfJHiiLNfDuRrTJeFKiwGq0e3TzYg2BdJlj8isZytWdXrXxyKluLhUYM_AUC-5mnAJLnwbc3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=sWtOOig3VhWsH9U1sluU2Dc4z41u4fmDoc2mM3nkBdgNmGwVgd4OeFoaJhmviUxse9RT9JVzumquUMlj5yAtSzIL6i9CI7HTJcbP_53yLVwKUWrn9v6I4osLZTnMDRbwbF284rb0sDjhT6Wf8FJStiACCpwFw7C_I23COtmHFZRpoIyz1HBLq8vvLgZGaHEK6Q50qxUB2VSR4cmzNDDI8jd7NoAtIqmLsgH8lfXS-YplOic7Zjpynr6FRNnCfEyoL0jmBJmrcwA_rfJHiiLNfDuRrTJeFKiwGq0e3TzYg2BdJlj8isZytWdXrXxyKluLhUYM_AUC-5mnAJLnwbc3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84058" target="_blank">📅 15:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=kkO5sb18jQwdYIK4MECDig_A2NrWmmf-mfdG2Ts0HxfDR5auquBlHpJ_uY-DeMjyB0EzsYyizisIraOqoB8RMqAsrHHkmPOXTYzERLEe788teqfXgPxxyIEcROGA6YxkpbHnJgFwHieSxjHgZ3BSpDb2KGVjRmTgFnRY2Gsgk53erVoWDx1CqtMgBIz1yVpXC-P_C8dU9RXOFu2_tmHvlTs3845gZmnb7pvPg7dAH5Fnnwp6tTHlgMVNuPaSny1l7uFUj9ja0tIDJfaKDF7a-jjZoua_xpQFy_AOKcrV-aZXlu4mtUiY9_BY0G2ESBtgPKnKWLPwFyDHUId2rxH0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=kkO5sb18jQwdYIK4MECDig_A2NrWmmf-mfdG2Ts0HxfDR5auquBlHpJ_uY-DeMjyB0EzsYyizisIraOqoB8RMqAsrHHkmPOXTYzERLEe788teqfXgPxxyIEcROGA6YxkpbHnJgFwHieSxjHgZ3BSpDb2KGVjRmTgFnRY2Gsgk53erVoWDx1CqtMgBIz1yVpXC-P_C8dU9RXOFu2_tmHvlTs3845gZmnb7pvPg7dAH5Fnnwp6tTHlgMVNuPaSny1l7uFUj9ja0tIDJfaKDF7a-jjZoua_xpQFy_AOKcrV-aZXlu4mtUiY9_BY0G2ESBtgPKnKWLPwFyDHUId2rxH0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84057" target="_blank">📅 12:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=ZprlLVkiQVqQf_TU4Y1jwsifoa_HSbhqJmuiloi3bVzgYAjupwsuR83ZgndLFST5TVJkhGlppXeiiK59UK-UB71-z4MHQwE-MSVWjHkbmgX2gmOGG_EqJF4YVdu7YuG0fRH5k6br5AmeiUwH_VbScgqbaCL5wH2dy3VuRaArqNzqU5ajk687O1dMYlHIivaNjrxKJlW-KpWo9cdtSAHkwF0eLBnDKBKWv4sYIcg4gQyxMKVct74JkBZ2aTPNFC30sKKK0wwEGUulvWxIcRQPfR4tuDkc5y5IJclVWXYBz0f5yS1WNEhIQyGdRJ0EuTK2mUVHdalriSuCaHHBTZr_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=ZprlLVkiQVqQf_TU4Y1jwsifoa_HSbhqJmuiloi3bVzgYAjupwsuR83ZgndLFST5TVJkhGlppXeiiK59UK-UB71-z4MHQwE-MSVWjHkbmgX2gmOGG_EqJF4YVdu7YuG0fRH5k6br5AmeiUwH_VbScgqbaCL5wH2dy3VuRaArqNzqU5ajk687O1dMYlHIivaNjrxKJlW-KpWo9cdtSAHkwF0eLBnDKBKWv4sYIcg4gQyxMKVct74JkBZ2aTPNFC30sKKK0wwEGUulvWxIcRQPfR4tuDkc5y5IJclVWXYBz0f5yS1WNEhIQyGdRJ0EuTK2mUVHdalriSuCaHHBTZr_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84056" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نمیدونم این چه مرضیه رپرا دارن، اونایی که تا سگ نمیشناستشون عالین وقتی معروف میشن یه گوهی میشن اون سرش ناپیدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84055" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=Hurup6ihW9XHY6z-1zx1p24WOkPf5y3UNoeeKh2ULcP-jHHEjn3BI2OJ3oACCH0e--Wmvp4VhZj7eIcOAlvxXMUSVipjOsPmpxa5B68UnN_g6zWi_IK9ZboR8nTg_DvL0vm8b0GBYhXNZtIBj7JcPIxfJRUTpQpatdGld_skhpYGTrB1Mte6ChLI20zUZkwo04CbrqrLNDEuayF0U-seLFixhUWGUWAInrqN5XCeFR-kGPQRV2rQPirakyNH6X2bWx9RTNc--72NRz0DmF7Vj6lelyVt-D7kiMPO5UO3baUBT-Xc3_7adA-h2BD85aod5BltIOHjZnszox6_N24DVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=Hurup6ihW9XHY6z-1zx1p24WOkPf5y3UNoeeKh2ULcP-jHHEjn3BI2OJ3oACCH0e--Wmvp4VhZj7eIcOAlvxXMUSVipjOsPmpxa5B68UnN_g6zWi_IK9ZboR8nTg_DvL0vm8b0GBYhXNZtIBj7JcPIxfJRUTpQpatdGld_skhpYGTrB1Mte6ChLI20zUZkwo04CbrqrLNDEuayF0U-seLFixhUWGUWAInrqN5XCeFR-kGPQRV2rQPirakyNH6X2bWx9RTNc--72NRz0DmF7Vj6lelyVt-D7kiMPO5UO3baUBT-Xc3_7adA-h2BD85aod5BltIOHjZnszox6_N24DVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی: بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده، توی تونل رهبریشو طی میکنه و توی تونل رهبریش به پایان میرسه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84054" target="_blank">📅 11:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTtv78NdI0e794vYxmRaXVxRWaBGubb26wtzkJq237dltXquN_xWb5ZQcgs1acrnifOPp79hwWJLtKRwWlnyK6XKDa5YONjw0wUvjJTwklBMu_X4MnKLxz4r-mBX-uwfznoH1Gu8clV89YdDbS2XGI3WasMKf0ObSILRgoPSCuAlqFnXb2lz3lQkoVxQlrRW2ukXkOuETD5YF_W7gfkAwljRvZfwv2dhJv439BpHTv8WcKyUoyZzjgxABBLDoAQWZekPaGIUH50zbw2pns0kh9AhtjBi8RO9-cyV86NAWejX55R2UCx2yP7MGLN4Pl5VPCLvdfk4vJlTNF2OMqT8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shgy9R9PMF-l5vLPxhD3Rx2VKe6cqsp0DTfq4HCqVG-c38TRirnnW-I5ge-5EV-NjGib2Vhqwlt5mT9zktuoqGbbFP74W_EuvAL8W_TbW-WuNNKvDlkbj_9kE0zEjF_eEDOADuTA2XcIwjBG_JnA41uV1dOFNEqvi6azmO3VJTkckvIOFqqeDZXRWh_PJxkmROxgQtoKD6txVVMNyJv5wfp-t4Nk0yslkyoHRMzdgcXLgIWp2z68vAYIlOEFHZcL1jQEsIS3xVG53KeiZryVDBK_UPv3qYKqgh_j7IvlF4xblpX0lZrJn3N-gDWAVLZJUXP_IZYE2-PjQjrLZvt2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THknNDrVtADNpxfDizMaU0KiDFHai_eM69zJquuJchLixLu9ET54Mpw2djbuvd3ZM9Kk0AVFzVP7zePr2U073XgGP-QR6LKySuUyIuL9ttY7XHk8eYJekaQeGUaKccNj3fbyCCUhNO_sj4XrBjgIZg4P9zpgCjDqJMd4py6bsHshG3tuK5XT5SkVoD5YSmldGDbZ0bwhsJVA6rXc5pMh14ykQjC3lTy-N9__gvk1EHIBEshONEowElIADTMEUbHj67h5Xo0dUOd_rNTQmDMIeWJb12gkSqfjJsjFLYylCGGTw62i0n5R74V6h1ZJrICpFun9A-9Qbt5aYel0iuuW6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت بازی آخر بهترین بازیکن تاریخ عجب چیزیه
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84051" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84050" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84050" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flo0brBbjrBT6IDgC7qXREagEYu5aFVa71JeJ9KpO3A7qsprquLi63mgfDu51bjVs5LFB-Qt8scivxn1fHvnu-Hd6RDz_b3rgwaAhMGMLPvB6wxcCd26DSC8xyYUueICfqY0UA44SCEaujKs_DJFc-U00A62w9zbu0aXjBF9aXvqAv8nRyuOQQi_o0ljpLCp6lM1CluY9lcFWY9x2HkjAQ5mTOXakwPHySpA9TAzfWDhkfWsgKo-jmBD4VUKVdGo9Y5R2CXQp3lvhg23i8doMdB_TTTUlzLS_dhdc1pOKqxot7C0u_1PVF84MlTAQ--2lmQI4CcVap7N-lwA2sRLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84049" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnZuwLmSbyvp_t56lRZy_M_7AjAG2MmoP5BkHCcgmqyzUAJipeg4UHCwOZ8K652WEkWJqPHKiPTLB1bhZimePCwWw7wv3cblROpTa5lAa2uqGXbFg8SPzD7y9cf0kJoPzayZcK0uug7y3ijJnHe7AYZXzbaUFUzIhD4B0cxzImpJCoSVLI8K8-xn61rpQhDsGnW7D36dnRmwFFU2_HhC0in0jE5cnI0cxWoZd1G7CXYeosdlK_3iiB48IONDrMCY1uVeex5vvoLzp1KmMWAZIoPyIxEYg_BrcMeZw30tFJ5h027VpfgeXcTmR6OZ9JXtPNu8JkxfN2E-nJ60T-3idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا شیر، ترکوندی شیر
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84048" target="_blank">📅 11:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=VwJvRuzUIDSnxY9WRBLZ5okKlKxgKFIx5bxdzBJ0CxlddRtadKJ09joSQ2iIEZXl82Cjs_NTIDcfPv4AvTkf3fM39I1Rodqwjaj3zY6iWQsJCrZAM0-FnpPWBpwsr0UJyOYBy6bpUfqi3KM_UrPuQDlwdW7AkQEt9x0zsbki3lxt-NpNlo14ocZqwOpSYxuYYBaZjnpGMpJqux10MI34tUS3NmDjuvdZDC5bjsRPIGJP4Doyl5axjytsLFrk93cfs9H0bYVWdZ65GpbfXZL48BaWSlPeFKrDzBKBViQE39O7C-oFZmDoYK5ZiYu07KZ7ILcCRjbBx0x2cC7MH9hgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=VwJvRuzUIDSnxY9WRBLZ5okKlKxgKFIx5bxdzBJ0CxlddRtadKJ09joSQ2iIEZXl82Cjs_NTIDcfPv4AvTkf3fM39I1Rodqwjaj3zY6iWQsJCrZAM0-FnpPWBpwsr0UJyOYBy6bpUfqi3KM_UrPuQDlwdW7AkQEt9x0zsbki3lxt-NpNlo14ocZqwOpSYxuYYBaZjnpGMpJqux10MI34tUS3NmDjuvdZDC5bjsRPIGJP4Doyl5axjytsLFrk93cfs9H0bYVWdZ65GpbfXZL48BaWSlPeFKrDzBKBViQE39O7C-oFZmDoYK5ZiYu07KZ7ILcCRjbBx0x2cC7MH9hgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا همه خفه شید فقط ایشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84047" target="_blank">📅 00:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEU3ltcNdwDeaWEkyDyboMqz_SIsp6suZbhmDjzks-Pk6gzDdfa0YcDGdEoq1IAuiN08RdwVGP2RklMUkMlj7LreLOBtWr2qd1i73O5GbSXXIKADt8xtC1aQTwX52kKn1OUUPBSYSMbfzHiJDXEb-1jlc2Es_ZqWX0-H3-JqOsHbY7nhnBziN9eDMW1KkKIXIUFaMYS9NvJ1CnGa3kHU6RvDdsACr7Mk-5F_VcEwYyylfsVW2mMdQsSS9Jqn-j-1yBbNm61ZMoK8be_KTXau92P4TpvR3skMNT45QzGn7_kTg37UhcgnTJpWNHTkMohGw-cO8RYFE3hZRBLVida8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84046" target="_blank">📅 00:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cywJKGlSfA9g6PxXdxHM7Fg49R7xdCXrjVmlXwOf_1I8R5srubyb7t_TCTMcCdnJhaaB3AcJtBMvzzJIktkhfzizrkQoHBQKTqVHHO7p-iR2aIZu3it7USq2I-hSLfffBj3cfE7PqXd0MMcAF5bgwIWdYIJ79Xmqjir755lERSqFTO-Ji0xp9ibr0YInV1UcZLHb2L62hkXsFYThfgVMuRVpZg8R9Gl2NCjUjggoQultrbq4aUj0MajNqPLAm2lG8grMJvEEiJSSTb9uoKAFnsrJRSYtuqWD9MITuZqMtcFokBXkqIU3WOo7ZX-S0xxPFPRbhGb8FOkq1IrVQ9HC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjroKVV05qCPi3-Ahep5UijLjmBXgpkqk3Azh5A4B78krJ_OML_8ySrkU65znKMH-sPUZc50ZYsZ-IFyVZiqwxGJhdWyQHHShKVucaY-8h9iDr0QOkc7FuJLltm0-BTkPRJSu-UgPAosdpKf8w8QWkA8i3uoFYexqp_Ck7Ng0ymF9aF1xLKIwja7j2Q3RiycJ9Uf5hPa6WJFOnWI81yPWqc3x115yTO41Jugr7KVS8u_5xE6CAzJdoLoMCmTms29HBd4ZoEOjPqlpGRauejmA-9g5jgKVs6bNUy2Q4PE8lN5ZypzT8QIy-K_0IqAyemk11Y5_cQylCx_QTMHSqnmyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط نزنیم حرف خالی
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84044" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwJzoGRS6O23N7gZ683vIDr6m14H93If84fITLZVW9ngtrojZuRp1YH_pi_G2dsHzn_d6zqEUzbEWqYva_321lG3jOl-hBwobNjwIp10n3qGy58-X99VUhUGo4DS1vvY00nZt2bEQzizOQ8Qw4yn2nxaiCVR0wE--CKj9YzfmYGKWSjCkxi26C1xJiJ8cidh8wE0uUYXXqGGG1_apkq7emreRlsFpKJ6S6J_uHEcsQEXRrF_CZtNvmUAqp_TZ0Ejf8QleQFnUiO9yZkggBSs1_tmaxNUPS3Mxsfn6lZdbVcPKMliW1Q46zXsA7jixYIKQaXnp-CUKaHR10fYMueP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بعد از اینکه پزشکیان بخاطر سخنرانیش تو سازمان ملل حسابی بین تندروها محبوب شد حالا بخاطر اینکه تو مصاحبه با فاکس نیوز گفت اورانیوممون رو میدیم دوباره داره ازشون فحش میخوره :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84043" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrpb_SePrE5zj_sZD5dMs_eTeLG_44lZCxo52c4-K-oEknk2wK57kMV8qv4rkPjSpNMMfNibiIu01_BB4-rHEiqszVaUXlvslb60Nrw-Y-6UBkR3N_G87R7JTo0Bk5efQt-pnHdOBg9qcanTkX4PntCA7R-BzlauPWbVY2JR0RAXsOkenuQTXT65msg6pq1L9rA92zzmSHSrWOP7XstVDVWRvMuX0bc3nuAy5xyNwneSmNmzrFuEFDNStiZm0cYHsrQbn8jLS2SY5Em01-acTA0rGiIB_US5tKogJ0jM7Nu-nE-J5bq5OqmiWtZTe7OR_XBZmCZqLdhL_lexSsJVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی دیگه پول نمیده فقط یوتوب
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84042" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84041" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC3CMgX9vH3hLZv01HR7gHDReMtO9j6lbNwggVv5EfWNttf4Nt2xjtKZ_PQ92DByDn5OQkvgPpEKl76Aiki6gW0i5aedce2etUcX_CLV6h4BLKR-eT6YIwjkT15n4s5JKXDJYGlJdI6SdtpqC5-mUnSR3f6scIjVS-nMV8QAuy6sWFE8gUQA84ILipp10QwupMnyQ0T4Dp6OIvUhudlL7SdHaJXctda3yOM313X8hGP8HMePQEbiiVT7QLEHmxx-FnF9GY4tPWggiMpwEPC7Mwb3tDFvJluipl9IKdXMrlBH1nDQDVZNACK3uImb8Zej323MVIhMb8e0I7sud_PYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84040" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84039" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84038" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx4iBnmODf4BnLbdcREufiUtdmT_RQvxh-M1OLQnRyjtgRagRbHfID4MANtZvTzw4ADTQU8ED9f6mqJ4vKEFP93QT_PRNw1QVx4toCGprIUP3RWd88wYvU2kyjm2dW0ALURJW-0HC19H-z9Y8XLuofD7MOpJevEK3eUtYkY5EmeYkVKeGQTIBBNsxnEG7JWazi3B38rgrR5ulREDM5_W0XF_9Azy8RRFcCwzWs43M6mJUmV6EFYYUsGOGh73arODQT9feh61tL0OdQeFbMo4PkC33GEDcZ3yTm_KsgRYmsbuxGBNMQYtEpzT4JZPOdeTPoMal7VrZddquFOoXoXm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84037" target="_blank">📅 16:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=EStLFZpkA7S5hCh772vdJAIhRa_iF5PGOZmtRi7he1IbficXkOPPxSqDGlAjZ2wxU_ZX4mcOi_uwKsjtDzXJ7SneNBduuuUVWvo5i9CaYO3PZtVsNVSkXmzP-RMfUSNslswy1Ah_RTmTK2joKpToLKF-gdaBD4e7NmK1c7YGpGGYXQIqbck6OgkA_BGyRufVABWS37l8rriufSjO16QTMtULbn1eGyOH9zO8ywtvvjwNgHMU5lNDwgVf7mqhFTMZhCaYpPJcvVN1Uyegu_O0pjdvhdgsojVEtyC4WPBG1kr6Jd9EN0ciD9DAKb_fgzWJt1LaXYbwoviSZdIKWM0mhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=EStLFZpkA7S5hCh772vdJAIhRa_iF5PGOZmtRi7he1IbficXkOPPxSqDGlAjZ2wxU_ZX4mcOi_uwKsjtDzXJ7SneNBduuuUVWvo5i9CaYO3PZtVsNVSkXmzP-RMfUSNslswy1Ah_RTmTK2joKpToLKF-gdaBD4e7NmK1c7YGpGGYXQIqbck6OgkA_BGyRufVABWS37l8rriufSjO16QTMtULbn1eGyOH9zO8ywtvvjwNgHMU5lNDwgVf7mqhFTMZhCaYpPJcvVN1Uyegu_O0pjdvhdgsojVEtyC4WPBG1kr6Jd9EN0ciD9DAKb_fgzWJt1LaXYbwoviSZdIKWM0mhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون دختر که دریک سگش شده بود گفت استپ فادر ایرانیش بزرگش کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84036" target="_blank">📅 16:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84035" target="_blank">📅 15:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84034" target="_blank">📅 15:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meogFLKU_L-OMcLFi3dL6LkkeS9hrBkSn3aTJr1wPTp0mDnuzy-_isGnjWclZjbj8w737awGaYV9dvIPQ5MWNrOaZHm1q8-7PqIZJ410Ba0vlWyoDUn7elwkWlc75DOB4ZzZ70snM_2XdoHxbzWHSHi9xkPSVZelJ4FIZgtOhJhAk5dzdv-cxj78pOkUyOe_bxRftHFzbRDKXotcFGUIsqZQwT3-J8UWHyKVVgkRmzm4z_ir88bark9R4Zvfc9HHUq5kr0TWpCMfpGxxfAudOI096iG6TQQoSQTMy_lsddcI7Hl25vVYHscwa_8YXbU69ananypPUsJ0DW6LM2bPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو با اون بیفی که کردی یچی فراتر از این حرفایی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84033" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXXPJQYiUIRygM-9brvrQDujGD81y6B7Ffk6n05ult2Y8tH21PXM2ZCTZLD4HxyzBEToLwrAahUOSMQdSaGKjp1kpSP32gWLGzCrjG_QemOs26ShulTr3IVm7eaNIrWASXanNLObx1xion6x72VfquHY5VljZnQATuHIi01TBYG6rLMGUnwBqGMfLLYYF0c749ri5O0V9RpUIJvVPUPqd5fxDJe9eov7Z0Jf85HE-Ag5X7sYIJhFbqYuzxVi3SQTUST9XWqIq6VXLtmISU9mBF7PgNnJ7nnZbt14nsAWlMGy8bmVjHyxXqpDdDIh76vtZSVYyzc-7sMC7CHLouYL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کصشریه دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84032" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">لایو دیشب رضا پیشرو که بیشتر راجب کصشرای کنسرتش صحبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84031" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/84030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آ
موزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84030" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgQQbQXqWlqpTZC3TjRfUDhdo5LOeGFz5_ybNCohOdFrDu6KWPKqVySnnGKsmaRc6okV4LNt3jko9O0ivZsrIcDgNDl_ezkXMCaywwawFjZKtz-Ri667ucHDxAqZW3wOj0GRwUGSR6EHtMScxfnPs5_-nwR2yEtoL5eAz1lfmtfuX41aCXfCbSRlm9RZ3Ss9LeQNtzeAzco0vZlV0wYnorG-LD96USaOf56aYhpao18ettwTqmun_QOV-KGuV9A8w2jAvc0YKJtvESFq53chKBkK3qDXSuJad_eaRb8IRK_Y2aM6MXpYxTqWKARpUM2FzwD96717-BVAt7FwrIDWZIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgQQbQXqWlqpTZC3TjRfUDhdo5LOeGFz5_ybNCohOdFrDu6KWPKqVySnnGKsmaRc6okV4LNt3jko9O0ivZsrIcDgNDl_ezkXMCaywwawFjZKtz-Ri667ucHDxAqZW3wOj0GRwUGSR6EHtMScxfnPs5_-nwR2yEtoL5eAz1lfmtfuX41aCXfCbSRlm9RZ3Ss9LeQNtzeAzco0vZlV0wYnorG-LD96USaOf56aYhpao18ettwTqmun_QOV-KGuV9A8w2jAvc0YKJtvESFq53chKBkK3qDXSuJad_eaRb8IRK_Y2aM6MXpYxTqWKARpUM2FzwD96717-BVAt7FwrIDWZIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
واقعا چرا ریتزوبت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
ریتزوبت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
⚡️
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84029" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOxkABdNqvxePUCDSTo50wkiIHOiOVjcXRcJ-5Ibd0EyT4LUV9P_eKhJedz5OHNBmZ_1-M_de08Zkxt7YO2vsOSvDzu49txHa2Jbv44zEVW3kE1_ApqFlMbZlaDTYCeyYeNWS0Zlo4e2v5H1NTeDKBUAiCqST0-kaGVDAWIWcq_o5PpKqAJdVRAhq8apFLHfuO4hk1Hz2SJWpwFAJybvXjS8hwdfP-Sibn0xdCOrzOjaWmGAZEU8VkiyFYh9fBchfsRgHdxnZRoBkNxY4Y5lyym8wj4v0St-EbKFQYMDzhwYKD96PPJIYSvf7d0fCclOUNsTH1Mbm-HKXh6ofG9LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌همه‌چیز من این فیلم رو واقعا دوست داشتم.
الان با چه رویی برم دوباره ببینمش و به بقیه بگم سلیقه‌م با بیگ‌شگی یکیه؟
(اگه مشکلی ندارید فیلمی که می‌بینید رو شاه مشهد دوستش داشته‌ باشه و هنوز این شاهکار فرا بشری رو ندیدید، همین امروز ببینیدش؛
اسمش: Léon: The Professional)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84028" target="_blank">📅 05:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=Q90awmHM8BKJMWuW5eCCY7tIXNsBCrTPXYQWy0xnQ6wNR1k4xLGnhwi611wbZxN8oqAC5BdtpVT6nREQn-5hVtC9LEME4yEn9-pQPV2L4ipGz4EgMp78DUxRw5S9p2ocGw217741PvFKcjeCd_N1mZw-RSP647jWMxLQj15FSfsGsLQHN6xtE3xdXS8-VnZbB8BUtPOrcDOEFD4RmGrw37VxO7ObxH_MMVNxS82BWNlM0GkTlykhAY5LVRp1yzCGAbMXwk2KVV4ZoIm1zKkgWvgrC8peBTO6TGIkA2eyaXTovWVmta8JDe62MtjLvs4UdUm2MGasjcMDa0PttCiBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=Q90awmHM8BKJMWuW5eCCY7tIXNsBCrTPXYQWy0xnQ6wNR1k4xLGnhwi611wbZxN8oqAC5BdtpVT6nREQn-5hVtC9LEME4yEn9-pQPV2L4ipGz4EgMp78DUxRw5S9p2ocGw217741PvFKcjeCd_N1mZw-RSP647jWMxLQj15FSfsGsLQHN6xtE3xdXS8-VnZbB8BUtPOrcDOEFD4RmGrw37VxO7ObxH_MMVNxS82BWNlM0GkTlykhAY5LVRp1yzCGAbMXwk2KVV4ZoIm1zKkgWvgrC8peBTO6TGIkA2eyaXTovWVmta8JDe62MtjLvs4UdUm2MGasjcMDa0PttCiBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84027" target="_blank">📅 04:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eia6Ttp5uIlrO6xm8S-tPNmiDH-iAP0nnrPKkzxRW2x9EDydzobNEFDJoMr9Tn5NV5D0IMCZ5WF_th4hvLxXY6pzkcWEN26PdTILyme-0RtCFWKfdzV8BgLRMEUFvfJUVVAU7E81O2sEqzORe8S3qAb5Ot3qCnK9j5FpUfzjLo1rAnrZ333J09m60FtaeqOvCinmu5ciOke8EonczdHh-DkW5ZuamyOg9kGWGd-Br7bGfh-UTka5Gcaaq87QKGOkDMaZKo2Y14SNRnHmeXTjQrmHI_P-Jb5n8Abr--juqyqEcJLXIGsAvFc7r3Dy4950F91CP2Um__9OHMVDfcNbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84026" target="_blank">📅 03:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکیان: ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود. آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند. من عمیقاً…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84025" target="_blank">📅 02:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d939cba.mp4?token=TS0TU3pKADeOOLVDfHqZt0NMyPJSr0AdpE7J9dK5k9_gKM5VSGqIOO7AbJmxB72q1N2N7l96RYgkIo9Y_xSQo-BbfvJbTzHPWkUhoswgXpR8kQ8H69mFkRsIoxPxX-FjnHedGRFqGLcEXePMtd3b55W3khED0MRV9ocJhsJQ9DkSKj7Z9Nu2xdz37pcUQYvTvmB7TdFmxeI1LmqNZBCZ-ss1jbQwhp8rqU2Qsa3dXKP8CJyzDak5jEE6iv3NwqycRM0YC9HKsw8Daut2_ce3vGBOknyWX81w3oci6X7-I301ww_hGianQ92DeZaezGKV1h9X3hg-DWOr4tmjyI2K6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d939cba.mp4?token=TS0TU3pKADeOOLVDfHqZt0NMyPJSr0AdpE7J9dK5k9_gKM5VSGqIOO7AbJmxB72q1N2N7l96RYgkIo9Y_xSQo-BbfvJbTzHPWkUhoswgXpR8kQ8H69mFkRsIoxPxX-FjnHedGRFqGLcEXePMtd3b55W3khED0MRV9ocJhsJQ9DkSKj7Z9Nu2xdz37pcUQYvTvmB7TdFmxeI1LmqNZBCZ-ss1jbQwhp8rqU2Qsa3dXKP8CJyzDak5jEE6iv3NwqycRM0YC9HKsw8Daut2_ce3vGBOknyWX81w3oci6X7-I301ww_hGianQ92DeZaezGKV1h9X3hg-DWOr4tmjyI2K6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود.
آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند.
من عمیقاً باور دارم که انسان‌ها نباید باعث مرگ یکدیگر شوند.
ما باید موجودات برگزیده آفرینش باشیم.
وقتی می‌توانیم مسائل را از طریق گفتگو حل کنیم، نباید به خشونت و کشتار متوسل شویم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84024" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=NuMmyJsQqQIv1jsd3FYMpWIAiJRcSE5ySgmu1vBv7J1dh4jfQ90LlNt6VlUFYx6pNNvKojsq8Ui9GYuMIl1CsC1WKIZbGBWKQdRnSKjspTeN8-84tuXYwUDeV8iGcTpSa8C7ZisKs8876hAvtV6wBYBGeVOybBt3kE7Vr_VadtTs_hnjIhPl4ign_JPZauYhPubYz5wdDyD1SAKrST782TZ-LykeZaZhaEps8tYuQZNgnTuqLCd3gxUJMzmXpqKhQ55FdKzNAgsNaQj0Pry7tEFBvHTTLeTyXI1yG0XBlx2wyeMqfwLO0tzgNK89_bc6-2t5HBkCEX4a5H9qvRzRKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=NuMmyJsQqQIv1jsd3FYMpWIAiJRcSE5ySgmu1vBv7J1dh4jfQ90LlNt6VlUFYx6pNNvKojsq8Ui9GYuMIl1CsC1WKIZbGBWKQdRnSKjspTeN8-84tuXYwUDeV8iGcTpSa8C7ZisKs8876hAvtV6wBYBGeVOybBt3kE7Vr_VadtTs_hnjIhPl4ign_JPZauYhPubYz5wdDyD1SAKrST782TZ-LykeZaZhaEps8tYuQZNgnTuqLCd3gxUJMzmXpqKhQ55FdKzNAgsNaQj0Pry7tEFBvHTTLeTyXI1yG0XBlx2wyeMqfwLO0tzgNK89_bc6-2t5HBkCEX4a5H9qvRzRKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما هرگز به مردم خودمان حمله نخواهیم کرد.
مجری فاکس:
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدرسه میناب حمله کرد؟
مجری:
در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
خیر به هیچ وجه اینگونه نبود، آنها همه تروریست‌های مسلح شده توسط آمریکا موساد یا کردها بودند که به قصد سرنگونی و ایجاد آشوب می‌خواستند کاری کنند و فکر می‌کردند ۳ روزه کار این نظام و کشور تمام می‌شود اما ما مقاومت کردیم و نگذاشتیم اینگونه شود.
آنها مردم عادی نبودند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84023" target="_blank">📅 02:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجری فاکس ‌نیوز: آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟ پزشکیان: هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.  اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم. اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84022" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5add83729.mp4?token=XbEG0GN8_aOQuCC4Yu18vP0z6Ggo3rmXmRnO-i6bdpnKvGtlyQFp3KrGUaWKMuBAff7djRKvMT6qx2R6oeTnIOTPWzVvmoq81M0jKVK2msGT5yEsZIUmCCn2W16el-n-Mftog7PVzPovkwRBsmSGb4_8sNHRJ-XVE6VDuO6m7i5A6_w0XsopR7YygFhR-yoFx8mcpivNLruD7EIncMkh0Jr_8z697g76Rl513QEXEmN_4wclzxl-34ENTGwN6jWs9XoAG8CMQX4jP0TJeLkcINKOgx6PfNzeQ6x9V5_dkty6K6ZFzHfr8_Jqjzg5738DfbKlrL4l1u24DJfTT_Qnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5add83729.mp4?token=XbEG0GN8_aOQuCC4Yu18vP0z6Ggo3rmXmRnO-i6bdpnKvGtlyQFp3KrGUaWKMuBAff7djRKvMT6qx2R6oeTnIOTPWzVvmoq81M0jKVK2msGT5yEsZIUmCCn2W16el-n-Mftog7PVzPovkwRBsmSGb4_8sNHRJ-XVE6VDuO6m7i5A6_w0XsopR7YygFhR-yoFx8mcpivNLruD7EIncMkh0Jr_8z697g76Rl513QEXEmN_4wclzxl-34ENTGwN6jWs9XoAG8CMQX4jP0TJeLkcINKOgx6PfNzeQ6x9V5_dkty6K6ZFzHfr8_Jqjzg5738DfbKlrL4l1u24DJfTT_Qnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس ‌نیوز:
آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟
پزشکیان:
هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.
اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم.
اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست و قانون کاری انجام دهد، این امری متفاوت است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84021" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پرزیدنت پزشکیان یه مصاحبه تصویری هم با فاکس نیوز کرده که الان پخش شده و با دیدنش می‌تونم به جرعت بگم که حجم و سطح طنز پرزیدنت ما، قابل قیاس با هیچ پرزیدنتی تو تاریخ بشریت نیست.
واقعا الکی نیست که چهارم شدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84020" target="_blank">📅 01:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جمهوری کلمبیا اعلام کرد که روابط دیپلماتیک خود را با جمهوری اسلامی قطع می‌کند. این تصمیم به دلیل ادعاهایی مبنی بر ارتباط رژیم ایران با گروه‌های تروریستی و قاچاقچیان مواد مخدر در سطح بین‌المللی، نقض حقوق بشر، مسدود کردن تنگه هرمز و همچنین جلوگیری از بازرسی‌های آژانس بین‌المللی انرژی اتمی از برنامه هسته‌ای این کشور اتخاذ شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84019" target="_blank">📅 01:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_BnllzCresX-5TyTeVZZ94WIskJyOfzckjPG9TOaJXCZEpG67kMu9IwZsOmQRzxnisW4qW8l79rzJeMHQIA6Jw-P_SWwRNc8X1CKO1XWgcwx2shvoOQ-KaNQxdfxWnqP1DQEe0FNLwmNLYnSdVw899_tNgnqSw7BQlTRVJJCfLvw2zypeMNN9kAG0GDKoYYaFcLFMeqjW1G0WLT1Y1DXkKBv14bQwIAEl_KmvWkCah4u0VbxsKlT-yAekFiq_xgG2GkLd7RDnU-UqHYyDsIGBYmQRyeYy93gxvbEgHFxuxxh5wP7daKNSHWwyO1XaeQUUh0oiSs0Ppr1djTG1pb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت مسعود پزشکیان در مصاحبه با NBC News:
ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از
اعضای خانواده‌ش
رو نداشتیم و این پروپاگاندای یهودی‌هاست.
برخلاف
ادعای روبیو
، ما اصلا دوست نداریم جنگ رو تا انتخابات میان‌دوره‌ای آمریکا کش بدیم چون هر چی زودتر تموم شده بهتره.
ما هنوزم به توافق اسلام‌آباد معتقدیم و امیدواریم آمریکا هر چه زودتر و قبل از انتخابات، جنگ رو پایان بده و به این توافق برگرده تا ما هم بتونیم بهش برگردیم.
ما آماده‌ایم دسترسی کامل نظارت بر سایت‌های هسته‌ای‌مون رو فورا بعد از اتمام جنگ به نهادهای نظارتی بدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84018" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=bZZxmYnydvtSw_eA1sC7XLsGzLmUCz83S06OQ7DUgMUBofP39POm_LfVbPiFJWryG53x7MSLYbyxw5LJweUUxP1GWdnPBn9eVtFCd0njvcl-ROiGQF0tmRAfpXIXejgmB6z0xq8NliT66NFA13cm0T0jAOoJaJeJyO8_VfhmjBWukJtIsJgEwl891tt9KHVAeUPJSSpMT0QVDpBGiL32k9lsQRetdhlcIVZsv-wqQg-473ejCctfpny_CUQvN6ohXfCPYHTa_YrDeUycfXWEepHhELpj6jhRGaINO6hRUT419vU8oL-e78VccWe6BCJXFTuZ2oSR46Jhx6DIgJgzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=bZZxmYnydvtSw_eA1sC7XLsGzLmUCz83S06OQ7DUgMUBofP39POm_LfVbPiFJWryG53x7MSLYbyxw5LJweUUxP1GWdnPBn9eVtFCd0njvcl-ROiGQF0tmRAfpXIXejgmB6z0xq8NliT66NFA13cm0T0jAOoJaJeJyO8_VfhmjBWukJtIsJgEwl891tt9KHVAeUPJSSpMT0QVDpBGiL32k9lsQRetdhlcIVZsv-wqQg-473ejCctfpny_CUQvN6ohXfCPYHTa_YrDeUycfXWEepHhELpj6jhRGaINO6hRUT419vU8oL-e78VccWe6BCJXFTuZ2oSR46Jhx6DIgJgzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده‌ی اسرائیل تو سازمان ملل اون استارلینک نتانیاهو رو برد پیش نماینده‌ی ایران تو سازمان ملل و خواست بهش کادو بده که بیاره ایران اما نماینده‌ی ایران قبولش نکرد.
💔
نماینده‌ی اسرائیل در سازمان ملل: 1
پوریا عرب: 28929853059-
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84017" target="_blank">📅 01:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو یدونه دیش استارلینک اورده بود با خودش، به دبیر سالن داد و گفت بدیدش به نماینده های ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84016" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=CTsrTlNa4qqmnCfA6r1AXDdF3o8HMO4SYZ2wcOtRmYnue_d49mECunpGJUrIbTTl1khweItWhmyCfcoF8lGW1gkrYJv0Hr1jiSN3uj6pjhjPm_DPEz16p3sIBIUEITeWxydlos9qSaO-uFPrUVek4dyeC7yyBFM52AvZUKSjzNTvIyAgobODKJGJ03VSAM5ytZ6Vo5QRX5_X2J7cvq181B_GA65ZpPtkMgQHKjGGVAFCWqtW3BCnOmKAnTEcH2NPS-Uds7Mt3S_Sza8dGBCnTLjJW8tSFTrRbRzSHvagBTshi_Je9wB5gKqR5Y4LSFYW76buN9Upzp5HTdL2PvTvN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=CTsrTlNa4qqmnCfA6r1AXDdF3o8HMO4SYZ2wcOtRmYnue_d49mECunpGJUrIbTTl1khweItWhmyCfcoF8lGW1gkrYJv0Hr1jiSN3uj6pjhjPm_DPEz16p3sIBIUEITeWxydlos9qSaO-uFPrUVek4dyeC7yyBFM52AvZUKSjzNTvIyAgobODKJGJ03VSAM5ytZ6Vo5QRX5_X2J7cvq181B_GA65ZpPtkMgQHKjGGVAFCWqtW3BCnOmKAnTEcH2NPS-Uds7Mt3S_Sza8dGBCnTLjJW8tSFTrRbRzSHvagBTshi_Je9wB5gKqR5Y4LSFYW76buN9Upzp5HTdL2PvTvN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره پروپاگانداهای علیه اسرائیل:
🔺️
می‌خواهم چند سوال از شما بپرسم؛ کدام رژیم نسل‌کشی، یک میلیون دوز واکسن فلج اطفال را به جمعیت دشمن (غزه) تزریق می‌کند؟
🔺️
کدام رژیم نسل‌کشی، توزیع 2 میلیون تن مواد غذایی را به غزه امکان‌پذیر می‌سازد؟ این یعنی یک تن غذا برای هر نفرز متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84015" target="_blank">📅 22:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=eq7NUvzb_1Ndl447FcxSS7q8j_SwkEaeBgtmv1PraPzHya1slE-uMbCl3MEKc9G7GxYs7VNWnBsguj7eeVwvQwWft5wKId5yKeQhNQs91voDibGOxTMN0WNmxiXOLjIBil2zi_5Fev7esBOXvPIgPTcDSHMrcu7telgJW0yOOn0atf9DwEH-2Yqq-2o823TmKw60qWr0FllVrgpzGk9s5fvDvxNg8zYbdRtLoYLPRrEWIWTwMR0_Kdek-cd_qOHrmTIPFr7tSOwceXgWsoYNrHcZG2m1lAxAMSP7vY1fKUF2f6fJT2ne9kUA1k97kLpa1BleruFQsXbyAY9Qj7oIRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=eq7NUvzb_1Ndl447FcxSS7q8j_SwkEaeBgtmv1PraPzHya1slE-uMbCl3MEKc9G7GxYs7VNWnBsguj7eeVwvQwWft5wKId5yKeQhNQs91voDibGOxTMN0WNmxiXOLjIBil2zi_5Fev7esBOXvPIgPTcDSHMrcu7telgJW0yOOn0atf9DwEH-2Yqq-2o823TmKw60qWr0FllVrgpzGk9s5fvDvxNg8zYbdRtLoYLPRrEWIWTwMR0_Kdek-cd_qOHrmTIPFr7tSOwceXgWsoYNrHcZG2m1lAxAMSP7vY1fKUF2f6fJT2ne9kUA1k97kLpa1BleruFQsXbyAY9Qj7oIRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره جنگ غزه:
🔺️
در حالی که حماس تمام تلاش خود را برای قرار دادن غیرنظامیان فلسطینی در معرض خطر انجام داد که اغلب با استفاده از زور و تهدید صورت میگرفت، اسرائیل تمام تلاش خود را برای دور نگه داشتن آن‌ها از خطر انجام داد.
🔺️
ما میلیون‌ها پیامک برای هشدار دادن به غیرنظامیان برای ترک مناطق درگیری ارسال کردیم؛ ما میلیون‌ها تماس تلفنی برقرار کردیم و میلیون‌ها برگه اطلاع‌رسانی درباره حملات پخش کردیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84014" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهوی جنایتکار بد در ادامه‌ی سخنان زشتش:
می‌خواهم خبرهای خوبی را به شما بدهم.
اینجا فقط مسئله زمان است که چه زمان این اتفاق شگفت‌انگیز در ایران رخ خواهد داد.
قدرت مردم، قدرت حاکمان را سرنگون خواهد کرد!
می‌خواهم شما با دقت به حرف‌های من گوش دهید. یک روز، و ممکن است این روز خیلی دور نباشد، مردم ایران آزاد خواهند شد.
رژیم قتل‌عام آن‌ها، با دروغ‌هایش، با فسادش و با ظلمش سرنگون خواهد شد.
این رژیم شیطانی سقوط خواهد کرد، و همه ما در آن روز جشن خواهیم گرفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84013" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=bwHpm3xZcGgUW7j9V9Wp7duUpDyYCk8sQK5w5FvmForOfUUNADXHbeemeo9ytzV0De-VmW6lUYjdC3avKjTm7SiiKVuPp7nMx2xl-XofqaLg90gN6GXXoWlwCUIXVWr-PGFeDBRMSnT0h86QTeAeaWv2lccC9m4os6CfbSYmUH8gB-g9wnT7-UO2hnLJY8KLja7xNyxIs_sBd_AGjpZKc-aj3rpceTPmRMxPW6jie8N4sxTTHWnxXhlJVXmM7V7ftrlsrgSRMYXRbjo6KjHi6DsEiRdTarq3_58cjctCtUPLLAl3uzqsMSsm_WbVGh4Um36tKj3Mmh1rVfg1SZC49w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=bwHpm3xZcGgUW7j9V9Wp7duUpDyYCk8sQK5w5FvmForOfUUNADXHbeemeo9ytzV0De-VmW6lUYjdC3avKjTm7SiiKVuPp7nMx2xl-XofqaLg90gN6GXXoWlwCUIXVWr-PGFeDBRMSnT0h86QTeAeaWv2lccC9m4os6CfbSYmUH8gB-g9wnT7-UO2hnLJY8KLja7xNyxIs_sBd_AGjpZKc-aj3rpceTPmRMxPW6jie8N4sxTTHWnxXhlJVXmM7V7ftrlsrgSRMYXRbjo6KjHi6DsEiRdTarq3_58cjctCtUPLLAl3uzqsMSsm_WbVGh4Um36tKj3Mmh1rVfg1SZC49w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی نتانیاهوی جنایتکار بد در مجمع سازمان ملل:
از آنهایی که اکنون (به نشانه اعتراض به وضعیت حماس و غزه) سالن را ترک کرده‌اند یک سوال دارم:
شما کجا بودید وقتی که ظالمان ایرانی، دهها هزار شهروند غیر مسلح ایرانی را به قتل رساندند و سلاخی کردند؟
وقتی که آن‌ها هزاران نفر از خود مردمشان را به قتل رساندند و سلاخی کردند، شما کجا بودید و چه کردید؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84012" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaYI2sAI_lC7Z8NkrkcYE0BJzkC3i-wtNpTmx7q0xy4-ILPS46xvvuucBVQwSSr-YQ0tMh7Kyj4IJLQHCcQ1qnNhPGD85fKJee9QgUsC0LdinXuITJJ20iAoHLbUZAj4wbHvHOTT5ReozJ45y9Sb-VGMcNmLpuyyDB-_k9eeOu6AvBrLl13US2scoZG8vPYzdcrbVHL8n7ea-v_8M6ZUVn8A4X5I3nq-8Q-zA4E98DlmqvFR4DY1R7QKIJ20_zDP1GUfbty3gFt6ihffvF74Nq2C1Gm7XGJ9avQtNQdfx86Xl9GmCpLXI1k9Suw-fVlE2US3yBP3pqAIcETxBxdLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84011" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84010" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84009" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXys6tt8U2To2mWL5qewzZGhaszCA8PAkVGeI0ICYOaojwmUfQHjQ0zm7OiRHqs2YDSGcKVOqE8aU8VPfzulQut_7c4tndSDtzg7X5LHns3bQqh0B60u-cLqNYfzjf0nK9uOCz7rn6lXHbV1_2IhDO80Mq26R9WhBHgIgNCyzXcQB6_Sj92vh0O63sAm4oiXjZmHPukU3YAzUFFExFHLUSa8KP1UiJ2p56yph0aZmHdZUICaHRIni9tbhFZqmtQJ1L2EEDP7aiYK1J4_MPuFUjsO6BudZAFshqRsdguj5Zz3B2QGAnsdS6DRlp-WTEdM8AOGPCRCXutoU4xKxbTzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
تیم ایرانی به رهبری دکتر عراقچی تو نیویورک دارن با آمریکایی‌ها روی یک توافق که جنگ رو کامل
(با بمباران اتمی)
پایان می‌ده مذاکره‌ی سنگین می‌کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84008" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد. SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84007" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSq5OvTNMo4THR4DWBoLAcdkd1hnXlJevys_wFNhAy3SlJgkiVfvxEOIVPosE5Y7d1QctI43qQFWxFrEohKmnR0GsTJBbOnyuEmehaPitVb0x2ktZNyvXQ3cnYmSnG-D82dIXeYy98fZw0svhbrdZQtBzYSjqIn9JRtIVHpBRVfpCbUWNd5MzHTJ2cQ5VoNphPPm4SZMPeeY9MgCfSQJhCQhU2G8YLmn-k9Fwux75fo1gIAX7ivWm61U4MXSBDMFcdIQs6yfTYpKrumj8YZXffnBHw0XzUgVYUnk_dYWbj3Lk5IDxxl8YLb8yjnWkUmf3EQjYYHgfrklxKnjOVdwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84006" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfU1nVJm9ZpaE1MqlgqEkVKYGQDZcNCnK316aiAcw0utmtWsarMl7z6MGXi7PbXjnSH-uVwlhg3f0ZEJvfVnd3YQfxBOmZDc08aMcp69htS54Ae_r5-H_8DHqSx_qo0kkAF2LFp-GaeKioyU5hCEgBnVnteGC21H8OSBGB0F4kK2A1T3ioVsdL4kPYPXYigeVk2oCw085WvkS9ip-AbG4bpr3h_OoPbJGyxZYcD9wG-ad5bCGB9y1QalBkCM0cMIr3aNpsdwY4udAuh4rWd2a-zbpNd0XsVBS122QhGe5st4S9ByXskTkvKYscWJv0-35_9Bn4NDUhtk9oMLiOcjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امیر محمد یک خواننده ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84005" target="_blank">📅 19:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqc9EjocpHkTtov2BbYIFTefn7krbWB4LNrB1lKlhRGFNnDBdbB3cgjLlJehk9fq1CCKw68Kw0pOxSk3DQOtD2zR4IsJfdCMAyQGwtEAU62rBa7ZMFnj16_mPjxj6xJgXE4gW-jbF4wK89lFXQhstVSC8bFYyBfITSHootY3gJkTpjarm0wm0t042e5KS3fbwQmfp2k2u5VeIRIe7tQGGDpTFawlU88hVg3Z1_4CiXELqbbLg_7wR8HsA86edUjFJQvyz_esFY-3ySAafy6axmL0NWPYq8q-ACRju8OR6e4b2UBST_gPSv5o7N9I2rrTXmoBmJ6HTyjRDSGq5KW34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران جذاب ژنرال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84004" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=g-yrVYcL6q6xakBgEYmbeW7BnfeqbiyZTOBq1cFq6dnnw5JqY0vgC-ico_FtLx8apzYRkFHwmWWBdkDSlujNtcYKP9o3bEUdCESXjuW_U_24sQyg2W64rPjOuhYDh9rynE07J-PegDC_asAN277NugQuRLZKZnBIl_murKyNtdrgYTzBBKgf3c-dqaim2V32CC3YzqXo5GeZtFYzkzfojfs5uyNQYfYZMQHVgd2tk7mpwquzQWRKLehliQ7LCm-PrPJdMKdGuRE_9WsdZFxRP7KW71mZJfWqZqCMlRw0Z2j5fh0KnF8dxWPXBKp0SYYCR9zA63SrhluVHGFxajvdIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=g-yrVYcL6q6xakBgEYmbeW7BnfeqbiyZTOBq1cFq6dnnw5JqY0vgC-ico_FtLx8apzYRkFHwmWWBdkDSlujNtcYKP9o3bEUdCESXjuW_U_24sQyg2W64rPjOuhYDh9rynE07J-PegDC_asAN277NugQuRLZKZnBIl_murKyNtdrgYTzBBKgf3c-dqaim2V32CC3YzqXo5GeZtFYzkzfojfs5uyNQYfYZMQHVgd2tk7mpwquzQWRKLehliQ7LCm-PrPJdMKdGuRE_9WsdZFxRP7KW71mZJfWqZqCMlRw0Z2j5fh0KnF8dxWPXBKp0SYYCR9zA63SrhluVHGFxajvdIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84001" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84000" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9MMgApiN5yGrt2uLluBm3y92LI8JSR8TqOpBU4AO9RTViIRXNNHqDhENsjpxtUlac83SnIHLgb-ks3zxQl5TEZ4WdfU7-peGxLVRalWke2rpKCoiUzuynf7XRrDWO9NlIgv8ejPaNlp9E5xhtYMU8MUqkN3WesBgzr1kz4Fv6gWvtsYU7Fkj7SUQUmWlm_604BvVbfNaCNBnu3WIoIx_N7nmcJd4Q2j8etoJhYEbGPdKSWin3HynQA9chzD5PGOwvkpKJCc_--Cmn6FwNEhtB-QxjPFG9NxkQBtdRHzsyVuh70GS0I8pk1u1qnP8rdPi5KMjVmZrFfiThJ1dDBbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسی به هیچ وجه
ترامپ:
دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست؛ بهتر از همیشه. بانوی اول شی هم، مثل همیشه، زیباست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83999" target="_blank">📅 16:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاید باورتون نشه ولی کوروش تو چنلش هنوز با پوتک درگیره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83998" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGWx2nqwp0a1DQgTsnwz0gfzIA6OnYsfB9jSwHnxERDqBdb63pMBzGPx085CH_aKvS495quhoiAiwwe_LeiVNDLZNDtV7uQb4mvwrLJ9R0E6FEQNL0Yjh6vF1iVVEzmp7tcCEiWXHaDQ5JkDJG9Lp1o5eatCQJ5ddq7r-8eFdNA4_WPAlp6T_HM27C8QH2HezAUdERAg_rXjvleHqjMGjqf8iHSG7JW-53nBvtwUZGqyJIoyEc6Q9NolxWSSHC-TBfItUag4JfXFZHKUJ2pNKClgt49pYrlZgowFaRNtOHTwooKhNCJ01tj8k5gSaCcRBrAsMTKNjCljPX1f9KLdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اینا تو وان حموم خونشون ناخدا بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83997" target="_blank">📅 15:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkVm6aexA0Za5FLdhEvMqdtDX8iMnPK4kvzjqJQhstoxb0zbplXxdJUcVBOTmse3M65Ki2ENKmXFrRTMUf59wAU1aFFhwHcXeeRpxZVSI_JUtn78YcmzftDDXu3macMxtwcY8icEzj9c4BQqQZQQ78Gakp4PUd-FL-Zno6rkrZoprJlO91seoiUuiQ4ZG_H3QxdPPnAYs5l6bJ1CLlYYL1bszeDq-hy5MDyqxYIKl3etPX1NgX5WDBq9YL1Dv5k4xZCA3OmBnTYDluJgUtMqAcL7gN69dtxh12LjeryJwqdjhd7SsxNdkh06MMdyr4dvwClNQZPDqI4-gYI_5dHwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد به سلامتی به کدوم سمت انسانیت عازم هستید؟
حموم؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83996" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پس پزشکیان کی قراره بیاد بگه گور بابای دنیا ما رفتیم بمب اتم بسازیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83995" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=kHaLIsNG65rLpdg7Ogbsvh6z-17r4f57hgOQvomF3kh-EtPp5tjcr0KeoW7ehZ7cmze2HQCtiAxYWht60hCLOZzI6dUaKGoQRHSQFMU1vJng9e0iuSFaMk7qjrpBeCnwpeLoJBBgLj27_Hxz5PQYS7qxTUlRQRae2gWWeazR2C9k5mNjZ-gzXrqjjMYwGOEAkKh1CkB4RMZBHb6JoKV55VijegSCTlMBbNODrrAqrza8SqXAXj665KvyHsFNfzlymIkUfyFBb6RcyVfMBUek0W85gAPed_St2fJAtaHJBWJM4Y360zLhNTSilQ2-6wMuVXB5AWhLmiIwypo3iuo7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=kHaLIsNG65rLpdg7Ogbsvh6z-17r4f57hgOQvomF3kh-EtPp5tjcr0KeoW7ehZ7cmze2HQCtiAxYWht60hCLOZzI6dUaKGoQRHSQFMU1vJng9e0iuSFaMk7qjrpBeCnwpeLoJBBgLj27_Hxz5PQYS7qxTUlRQRae2gWWeazR2C9k5mNjZ-gzXrqjjMYwGOEAkKh1CkB4RMZBHb6JoKV55VijegSCTlMBbNODrrAqrza8SqXAXj665KvyHsFNfzlymIkUfyFBb6RcyVfMBUek0W85gAPed_St2fJAtaHJBWJM4Y360zLhNTSilQ2-6wMuVXB5AWhLmiIwypo3iuo7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=iIiBqWs73-1g0_YWcFQOnHwVRKx4lFZ8TjQBAj1aFDa7OkmZDSPAFFC8C4I52wMUey0pFhdbix7juPK5E30hVxtCm2qd1hXtF1k_ZO0PGmAHubjHJlSwRAbJjCIlzZ7MI4M5N7_6OxuaOXdmALlxGCuo-lzmuJkT-4QUrwkFxBs6uZuQKDSRKIzpj88LRDPIDBXcy5Fx2lNI2GZxY7DnJjUjWWOgNNm3v5uFaATju30LMVefMG5t3ys6tzBtA6SlN4E7sGjmfVcPMiW2yI0oOiQeHETQIDuH6QQeDDLgJMKC-oLpSE38dPPvxqwTqZXpL2mg0haaFKX_OgWvrwqdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=iIiBqWs73-1g0_YWcFQOnHwVRKx4lFZ8TjQBAj1aFDa7OkmZDSPAFFC8C4I52wMUey0pFhdbix7juPK5E30hVxtCm2qd1hXtF1k_ZO0PGmAHubjHJlSwRAbJjCIlzZ7MI4M5N7_6OxuaOXdmALlxGCuo-lzmuJkT-4QUrwkFxBs6uZuQKDSRKIzpj88LRDPIDBXcy5Fx2lNI2GZxY7DnJjUjWWOgNNm3v5uFaATju30LMVefMG5t3ys6tzBtA6SlN4E7sGjmfVcPMiW2yI0oOiQeHETQIDuH6QQeDDLgJMKC-oLpSE38dPPvxqwTqZXpL2mg0haaFKX_OgWvrwqdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=Lm7XTOYjCEkl2xnwNKLXCW5pP3TWSAoxWjv1J1kcl4XKBO6-yhXLhMWhv2wA16Ru4V1KDSoCJKGRgB-UzjRIu0OhTEspoN6I6tYLf4qjg6qU-VtLQdrJSGHqKv3XQMGbLgRMYnVXL13NYnN4Z4tsNNRrYvMZgh_EWTBHRrDnyPOsWH1GzAZitmmqM5A8NK8nAwUEsPrRPHY-3LVmOEai9ISRJfu9gmrafwygFWA4J5r_PSh61yJmqrZa9JVkDnw9pNciAlqUB70Xxt_kamIwKXgKoaoe2g0QuqqryL_BHTwMcX91cUSPHCnlRdGypAUXJgBRF1RhoXjvjno1xRGrRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=Lm7XTOYjCEkl2xnwNKLXCW5pP3TWSAoxWjv1J1kcl4XKBO6-yhXLhMWhv2wA16Ru4V1KDSoCJKGRgB-UzjRIu0OhTEspoN6I6tYLf4qjg6qU-VtLQdrJSGHqKv3XQMGbLgRMYnVXL13NYnN4Z4tsNNRrYvMZgh_EWTBHRrDnyPOsWH1GzAZitmmqM5A8NK8nAwUEsPrRPHY-3LVmOEai9ISRJfu9gmrafwygFWA4J5r_PSh61yJmqrZa9JVkDnw9pNciAlqUB70Xxt_kamIwKXgKoaoe2g0QuqqryL_BHTwMcX91cUSPHCnlRdGypAUXJgBRF1RhoXjvjno1xRGrRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ22f_zxpamUEBnGZPbwCFZ1xF7TxNurTuclDukLSfeTv7HwJ6E3R6CH5PIpwe74Lc-rcs_Vx-KS5KwpuqmVWP5ape9eWSxrNOnj86xaGjIuXUBSc7HAws2mzwVPk62ktXKeBJIX-3sZQfIDESZ49gblWySdQv0val9p1pi89yKIy-oOrx-yP-WDz7Vjdp6X4n09fhpuCIsavPYMUCbhVGKmwxGC5jZvRF9Aqwz936Yw0wbBasvfwJmgmd7fb5aH9fTb-BMO4x0QANdon07CdGAmuSjuJrjaoVpQF24Lf0Yfrgo-ra2H5rjbuG8bqeybgz15Fhw_dnRMMXGn7NO8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvMlOFYkpS32cCaGlvPePmg3rYVXmwjp19NGvcTEKU81AMH7GCwyhLEHcfXrmrEV56MoqBvoZ63tr0piK3H57tZAzCeF17kemHR7jh5Jeq-pF6AUylsuzuwno_UkFzpZom-e6riWnXHbDdFfO3IeqFsYQbnmmrsWa0ryVv6xr7FXIwPb8S7FrRVHsNUYICIYw6dFvWicE98DxHTqSO0SCZ6VYJBy3r0JQXovf-i8oJxuV5rNLFF-QHRMcVSH3vy8bwJEMVHiTC6REEAiEqcOFuLXquY9PUul9PAxa5TKiBEoo7iRMLeAwvqCKeOEIFSXtc7ePvh7G1e86MxQUB0_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNkpBbgkIWeAbzhrxtjNYy1NX2efCD3rst8f0WN599P62oHUjeTYwc2_0u0-K8EEugI6dRRKAc5Y8iJ8qpJAz-Nb44RprGm_6fp9snSkeAwFBLrA89zApCEN8leymuX-HSlBtujPfvgru781m380UoUBnEKiJk6q3kwlzMqsTqwEAcaz0nxdj1MhxttYr2cVwDbVTu5D8K6sG3e0t9p8PzKV9owAUWN2LO380_JcKwODIitUjZUoMiyPjMhdS01AptHSZkZyRgMOP-qGmmVBWU3sne4VZF47dYflkwjM1jDy4zhqo8EVjZcuJDtLtYsne2psGeM6EjpQ7Rn7a7QW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogzuVybHYTxR1BIzJFUyJ88ZfnVKS_Zoe9UL2nOL9SpOmGIhK82Y4n1n43Q7L4q4rPn7_Xe5vu8DXxkI-hV00Mv1SAmJtwVfk5OB5jY_1o26m2CiXeA6kM-WKaTVbRLkspxBLaveKVgo5GdySIWSvABR7aHaMIC8KujVz6qs7cfSN2uvaVuUMkYiwTeunIdZxv51-2N8nxK1vNKDodI1GSjBthDv8OjxmZM83LsVObkLSSKDwidiuAbzZxRfkmSgOeAMx3fElsALj5ImV-2RT2iOO5RH0qmhoZO8UefFeVkttZbdN0KrHsHzrVcbpgaAu6Z4nY-51wgEFVzgeopq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM_DfJJVE25i6SLGvhjcROyfPKsM18sj7nYfqVfSK0YRSZqB2VHHcfdBsD4c-WnrAYA9RIAxqCYUCdlMTmMS_zaDJ7mK-sbO3ILg9a6ygRM9Yvec0u68fKZPRLnoeRt4_grwmnuv7_wf-dwsfeT8QL_VVmGen8hwjxtWGyYbct3ibQdIPKXtkeav1d2aJvJMU9jc7yVC4FMRVFld8EVEMB4P7-5ndRnnZ_um4IeZPZvF5DtGhgk8O582PEeTJ3wAbg5igQtuq56nOtusCON0XyprcFNQXR6vshTj6MjSTEzc0L1v3hh-tuGUSVFkLCApFE2RtE05kqfWW6twyoaDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=OITV4bEaI_vZLJlfOSKcNQ4oqv5PF2_V8m7Dd2so5Cz-nlgZAD70_CaabKx3TzfCy5B3j_39Ys2EiDoJE4FsTHYlMy_-z7t85E-eQP1uUCe2zW4tCpvl7lB8cSo7ZWAlHmo9tPAwF7rLsb2mnqau6Q5XMbyWt8UWp3vWamz99U3bYuMh2Fqaw7hxNgfqDDa8BjilAHgTCP3DdWr6SXcbapb2aqby7bbCQqSzLrhooRP8OI3q0YGUiSZl98pJ_TUXmv5SfzIrM06lGPAIWF74Cl8KB9hu-6YPc5IQqHgzkcCrU4-Tx_q0cHta7_y9MDNGfCfMEiR2eYnbl2pcohi0DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=OITV4bEaI_vZLJlfOSKcNQ4oqv5PF2_V8m7Dd2so5Cz-nlgZAD70_CaabKx3TzfCy5B3j_39Ys2EiDoJE4FsTHYlMy_-z7t85E-eQP1uUCe2zW4tCpvl7lB8cSo7ZWAlHmo9tPAwF7rLsb2mnqau6Q5XMbyWt8UWp3vWamz99U3bYuMh2Fqaw7hxNgfqDDa8BjilAHgTCP3DdWr6SXcbapb2aqby7bbCQqSzLrhooRP8OI3q0YGUiSZl98pJ_TUXmv5SfzIrM06lGPAIWF74Cl8KB9hu-6YPc5IQqHgzkcCrU4-Tx_q0cHta7_y9MDNGfCfMEiR2eYnbl2pcohi0DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIzqn35U8Ah-dXDmQ6j8gsltF3JwLK7Gyc7XyIz3Vgqownv64Wi_Q-tKbnMhmcoz21dffoSe_d2VFgg7yzs37dthtKlLnJSq1WQBQS-HubzGGObbKUhgNXd6tvWVlFc5g9aB122ymJPv3n70QeRegM7mqfDoUKJ19fjtugDec3S09Di288Jjl9cBsL-vTb82cFZ4FlIaa4xhYKDgCvrmFkQz31FKUY9UIvhtS2uQ3E-u5caX_nCmPeUB2Fr1wzePDeJkFZEwJ2GlGoIp272qIA181hnpF2sloH3u0qXgr3SztwK3oWQCopoVxbT7te3T5PMj2F-6jrYE0itdxq0JPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی دو روز شکل آدم بود باز طاقت نیاورد ریش‌هاش رو بگا داد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83975" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=eZm_6W0XghG59mFayOj4jKEM6d2U-zgvzOX935eGQmqgmQpO4DSK-oDCCNvWtMMGRsv_YUGQOtgj3cCceb9_KBscYMAIUSHOJzUjDELF7dTtK_tuLuxMYtYnz-l2yqwlJW3D-tss4Vs3sqJ9xM4zjARdPhr0GXIi0XCVSaT8WpOQ4zkQBIZcgYrI2ZNekTfxnJvfgHgFP_amXaSQgkX-yC0PuAzU9E5tB4RnKNpfLhAFaRHjBMt19qpc0zXcIHMpzHRoyla6QSmYyA7BK_A0TKn9kZEGRMXJLv7gXPE4gRRsOqib4-ZSWHyrIJEoGX8XnzvO8x8PPsF_7-HLe66M3KRAwdi0xnapCu1FUo1HZETXUP0JSZw1jv2XfKotRboIEwUzL7DrhciR3gs1cvGUwkkFmjW1ZEs-M03RYftcSd16cQ5nmUHUQd3Hna9S3pbSxxLjiG-s5pmYZM3JzaaHLNdjkAv6l7XJtM8S5xn0wG6oXk5-yJaky2N2lCDyn8yMnI8N6dFz9ThWFp5pCYVNGvSrmaFftl7iddTKnDK-DyqMLwZPx3MJr_IYE2giPmmlHaR202UcQ-xg4IFOLECiLVzgrMlpo88YIbCWPcn0zwlRZ65uWCxX-ZMo4HeBMtaRaXOe4GiNIg8Ez8_06KBIRWR2tYtaEgiTwUMPl4RyXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=eZm_6W0XghG59mFayOj4jKEM6d2U-zgvzOX935eGQmqgmQpO4DSK-oDCCNvWtMMGRsv_YUGQOtgj3cCceb9_KBscYMAIUSHOJzUjDELF7dTtK_tuLuxMYtYnz-l2yqwlJW3D-tss4Vs3sqJ9xM4zjARdPhr0GXIi0XCVSaT8WpOQ4zkQBIZcgYrI2ZNekTfxnJvfgHgFP_amXaSQgkX-yC0PuAzU9E5tB4RnKNpfLhAFaRHjBMt19qpc0zXcIHMpzHRoyla6QSmYyA7BK_A0TKn9kZEGRMXJLv7gXPE4gRRsOqib4-ZSWHyrIJEoGX8XnzvO8x8PPsF_7-HLe66M3KRAwdi0xnapCu1FUo1HZETXUP0JSZw1jv2XfKotRboIEwUzL7DrhciR3gs1cvGUwkkFmjW1ZEs-M03RYftcSd16cQ5nmUHUQd3Hna9S3pbSxxLjiG-s5pmYZM3JzaaHLNdjkAv6l7XJtM8S5xn0wG6oXk5-yJaky2N2lCDyn8yMnI8N6dFz9ThWFp5pCYVNGvSrmaFftl7iddTKnDK-DyqMLwZPx3MJr_IYE2giPmmlHaR202UcQ-xg4IFOLECiLVzgrMlpo88YIbCWPcn0zwlRZ65uWCxX-ZMo4HeBMtaRaXOe4GiNIg8Ez8_06KBIRWR2tYtaEgiTwUMPl4RyXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب رو بیت کاگان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83974" target="_blank">📅 20:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKsfERLxGVvrD4Cn0Vga-XPtIz9-nz-uaUkMtlthZfWYRm-hDhNGLj3ZPlphVWxPOdsjoaVVv46cHs1N2vWwnntiHEDmZOhVgFqA49Z3qfZxtXpuGtGj2-7nPx5uceB4BuMTkzSZj5ccAGiIZQbB9j9FLq2F1LkW0XUPfnm-mRQuUXC4oP80IZMpEZkgGm3Y1XupTrIVyDXkJr2RsuQIhI32I11HC7wHGXhE9wK51Y0u-XeNeQugZipymRtKXaA44pwqKY7ljup9DMHv-tHj52EAnmp7oZlpCJMM3NAX_d_gpxwUdLJFnK1YMlCEhYXw23jMnEaPWzT-Or5BNGPXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف:
رئیس‌جمهور پزشکیان فقط از طرف یک دولت صحبت نکرد؛ بلکه صدای یک تمدن ۳۰۰۰ ساله بود. او صدای قدرتمند شجاعت، مقاومت و قدرت جمهوری اسلامی ایران بود.
زنده باد ملت سربلند و مقاوم ایران.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83973" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83972" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=pQDvXNiMvsF9LUhb2vYSm57iQs46F0RKdM9FvavTCgC0ttGZC48CyM_72lP41j8x3jtLq1ut6Q716kkpjwRqET5ZzKfMr-9wBlLexCKv8BehlCCgWyDWm9_ekoFbMRlSo-B2AeSSg7OUN8-afnUSMIFjVGD-SCF9KK3t1U4bkzoElwrF2u84-GWTeXsYtPsRgSzh2yMMGViwmZ7BUL9bP08jqbaPJtLuWi7EjyFmzhAxSTUCN_tvO5gJdzfH8VEIWXeJzqycOKewpI4JNz3nW1eKPKfrcSonoPoQAaaxRz7zK7L5AXvKOw69oOYdPRc8mcckkbtYOOi8Uzc1SEG6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=pQDvXNiMvsF9LUhb2vYSm57iQs46F0RKdM9FvavTCgC0ttGZC48CyM_72lP41j8x3jtLq1ut6Q716kkpjwRqET5ZzKfMr-9wBlLexCKv8BehlCCgWyDWm9_ekoFbMRlSo-B2AeSSg7OUN8-afnUSMIFjVGD-SCF9KK3t1U4bkzoElwrF2u84-GWTeXsYtPsRgSzh2yMMGViwmZ7BUL9bP08jqbaPJtLuWi7EjyFmzhAxSTUCN_tvO5gJdzfH8VEIWXeJzqycOKewpI4JNz3nW1eKPKfrcSonoPoQAaaxRz7zK7L5AXvKOw69oOYdPRc8mcckkbtYOOi8Uzc1SEG6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
من فکر کنم تاکتیک ایرانی‌ها اینه که منتظرن چون فکر می‌کنن تو انتخابات آینده دموکرات ها پیروز میشن و اگه پیروز بشن دیگه ترامپ مجبوره بیخیال ایران بشه و از جنگ خارج بشه.
و خب جواب من اینه که خ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83970" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تسنیم:
عراقچی دیروز خودسرانه و بدون اطلاع دادن به نهادهای مربوطه و مجتبی خامنه‌ای، زنگ زده به ویتکاف و باهاش لاس زده و مذاکره تکنیکی کرده و برا همین باید توبیخ شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83969" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حین سخنرانی پزشکیان، نماینده‌های:
1. ایالات متحده آمریکا
2. بریتانیا
3. آلمان
4. فرانسه
5. اسرائیل
6. سوریه
7. لبنان
8. عربستان
9. مصر
10. امارات
11. الجزایر
12. لهستان
13. سوئد
14. دانمارک
15. کانادا
16. ژاپن
17. جمهوری آذربایجان
18. مالزی
19. نیوزیلند
20. استرالیا
21. جمهوری خلق کنگو
22. اکوادور
23. قبرس
24. ایسلند
25. مکزیک
سالن مجمع‌بین‌المللی‌سازمان‌ملل رو ترک کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83968" target="_blank">📅 18:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=mjlGp3ZVfpWSG9ATSIlfXPhq8XB_4CIioXWYQak76scdpVt32b95AVUot9IwpJE59wqCpCPYb1i0waHAJycCa9tGTDQkP4mYuFVJS_eXwSHKXiLIddT9ga7CDtq0a0toswZjJ_2SrzLkU0kpsBjRBy2TeLBpp3mP0GpoPgBHn2-HJT4ePecZTIfffR4IoJqxluTlWPralDRxPaSam44gsNsL60eQyVuGI_N9THT_7VgKKpbsrGJRUs9rcwVHVr8rGdkKAh2FeWU4mvBUUEazSXljOdzM4cfcby7eTFgWx5HUWlxfVMfMCpjtmGwahVlTp2NySTAx7nE_eFyhPD9ehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=mjlGp3ZVfpWSG9ATSIlfXPhq8XB_4CIioXWYQak76scdpVt32b95AVUot9IwpJE59wqCpCPYb1i0waHAJycCa9tGTDQkP4mYuFVJS_eXwSHKXiLIddT9ga7CDtq0a0toswZjJ_2SrzLkU0kpsBjRBy2TeLBpp3mP0GpoPgBHn2-HJT4ePecZTIfffR4IoJqxluTlWPralDRxPaSam44gsNsL60eQyVuGI_N9THT_7VgKKpbsrGJRUs9rcwVHVr8rGdkKAh2FeWU4mvBUUEazSXljOdzM4cfcby7eTFgWx5HUWlxfVMfMCpjtmGwahVlTp2NySTAx7nE_eFyhPD9ehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWllqZkABoTkTjPeIttYr5eOzEw1r9G-YZAyQge415FZzv-jBqF89970lRki8LeLgREXCjp5fIRef0sqRXEgmlhD3hvMjsvfj7uE5x7am0D7-pA6BVVKm1KYYhgy1cGXCAsf3ePL5NqoyhwRmFi1d4PbHuVlPXgJ-e2_XQ6dFaqgGIqpzCDwspgHeymrxyfNKhpn6NmaBYamheNxu9p9he3qiNKgm1LTyeCMM283F0BkZHD-9T0LIUQ-uYRY-0hbG85jRDudM8fw_a9ZZ58cce4oe3LFZOjb9UbPXVovR7qrum7cAtg5ixG0xEOM_dyE2s0Io6bV_gbZ0HQiJHS2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAR_g9MV-p7aa3tUKcTKIg6EPhhBsXR9K80wpHpJT3uieHbVCvh2k4_a5bG5_-5iYld17U69lZNtFMq_LjnAabK7SpR-fDuRGbeN_nMavcLCfVNaoO7LnXGcJVWbK-2EKF6uElcLEPLoYTdhzP2TcqcFjHGa_5fpzgGXnGSTgErZBauE0_gWHpRegERPWF0hkcIzaxEuPXSEl9bmIiYcTrexpNcQTToyiQVkCBwb5OZKEpJR_dhUXMuN5DxRp1XB4v5R0yW09ml1idQva_d-2nae8jZhdomMnZen0ULP4C8MYs4m6tzf5WY02h5d30Z2Y2pozSgUX6Sqmzkat1Aa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
