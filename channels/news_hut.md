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
<img src="https://cdn4.telesco.pe/file/I4aHwKbs0rQ6BbiQKC5zczX10670ykBkK0copiM2clwhZTrmfDGnA09aCgXaYlAA9P8G2sZxHRPoPgdHOA75O0XdxO3DRDd2jzsQoQgVGUOwmJERA-Igelhss8akD7FlPsRwswqBUn1Zj8HEniBl5RCV3hRhXfk0CsG5kDQeFdsPWwdpkgfvDnHHW-JUT9owANJxOQNv2ZHi2hC-wvdYzD_mQRubXccffui-45VDM6D6qeucbJLm9Gvsz1UlLnG_xro4hROlkHy--PrutSMfM-jJ71-Nnr4XtHjkprS-6rqBl79OmwoiLr7b-XctKqs-qYiYeD81SG_7tQyWHwLl4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93ZWito6W-WrsHfqGSvISSUuH7WJniT8ebdG-FuV-jHeAvzNrFSd0OhhwHtu2f7t9cMm9eVq3eRtnH1eEnTNQFKm4YJXExdv3HSlvhcNWlG65pqLfs1UGPI5hCUb_5alcaR671OpUBUJtUl8CsfPxoIPctM1t_3oJRInfIF-NqCRsH9Ib6d3TwSg0U5zskPSkFG4ifBSukdRyTEYMYOHLx4zIhBfVLo_oItRl9lpUgvKKUaZteIPyd4vVEg5z_5U60iWaXsbgsC1ST5Hr9sPzM1MVwt-rbN2eQQiGWRD0ZfHFnp3ysbqtJmLDaNF9XDjtynuUwX7Z_gCPg2NevsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCDizrkm7F0QVQGygRuz8lDk3HO_q0O9LdnTwIcdRvn7VmIIcCuKkjkoRPi8wSJEW4i8BSlcs_Eeb7fdOpLJWzgKPF30bIRHG0f4MKBAB_3SmalopIdKLqUKY_dCvhpVJvv6PmzH2t4DMC7f1DUwaynmNM7E8apSNcN_oUa56Dy6PBRsu53_Mfu91X2OrWwIXOS7X9A1fl5BlZspgUMq8VhZnqYY319HPJzKhnp77Orz5e7ORcwdLfoaOa-0htLJ70uzE9XVVP8GyOWEoCjIF-8M2VDT3AkLenUEnEsvr2Xo5nybgx8cIFR6f1vXNRzfY4jcscyoD5dlXZYAOQv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icxYaxT0dPbYtk6Ex6DJiTIGM33z2zh0Gae5ldKlw6uB7EGb9E8Rv3B7fFu-mkrK59Gy4PSM_ZxGM-xZ-RfkFLsNzGyXa8wjKpn22kUKKGcpJijQl9Fr_dWZDdbHGY49uwLopaUj7JNkZ4SbGuVq6NDVm_SCc76v8YRIDtjrdsz0O8KT2YBB1g9o4kfT0L3Pw_BCVbfLc-t7wFXzvwKXHbf8_qfq2SFLMTsk07jQ_JqDDe6oYshl1VvFncGeH3lCE9cmle2V3sBX82fhxtH3ToWKyNeCTuo9R2Co9c-2joLPP4E_ZmmmaiDnrkDAZH_R8OjsH4EhW6-7LmfaPmf7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2Bytnx-JfVnaEo-4uyRYhFQNMi7Zc30JVlMSC_oVWkt9EhG3iunWi7jeBLufd806y1-voY3xna4mbyLYmaZVY80xNaiytoDdyCIbFs1yAVEZMbTWER3Ol1vsAffIlOca0meS32LOyGcD7A6G77tdrseGZMNflqQJjv2aQuE1cfXpttbBrxv75Pt3rShApg1BLAIwg939ZscvsDR_ptso-h0BhjQVIv5JrQ0gryJPqCkRaVNWCJKT1OMt2UZJJ6RqT-0n8Ks7U9D_GXGn00Eh4qtivukcr_iiPJMso5JTCV1QLdbbM5I15Ff-mhsAMhS-tZk6399vL8Ro82t5NQcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMMB4Bm5kr1_zorJPOi0MCcWf5jq53bsPm5V6QD66n7ZotwBUmGhEcUl5W7W7pXrDhSG4xb33xCInPGjIpEyPwwGmdXCYxm3dI3uKXMAALDDFXHPFdCK-uvriTA1ed3lPraE-ZEm_TWORFJnTRAtdR4l4-_A95i9bhlMP2y3pxnjILwv0CDOAHV-rXDD6v1ihMRFhqIfM6bKmvel0Cqh8TcLO4GXnRhYtAow4M2RoBB3_nIKHrRi9IoR3qvkbaNDWFugmJWw5bbei6S_5_8m-v315EoYKhjcvHCTaLHa9eUGS-1pHXEct6Xzi-PNDpUbWlaMLkY8NUV8xOj390za9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=vZ8zd1JT_hU7av4jYl5RNZzuTMNnZcQmDt2K3b6cX3hJNYMekZq666kiJ6tEE47_iO2SCjQ5bGssTR_pmMtVe-zR5cHfd1KtsYq5TiHS0MfJ-DlJ6ipy1_yCvhx52Z2Vsb6bAygCHkcPxJa8gnNc2qQKbRxHnfSzd86HuqbN3fDejs7PnRzNtJf1II_qG-LiNuKcqYicvU5uAkEwHKRp1Ph2FXA30hn24na-hzOF8RCJG8DoEC3Dz5EszhocTVz2dsKhNKaNsaxiPxFOH93nNOtp_ioXBif8pKA_tsXACfPWaRmb0Ilqe62M3PUS3DBII4pNZAJ9S6sGUqJN0uBUUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=vZ8zd1JT_hU7av4jYl5RNZzuTMNnZcQmDt2K3b6cX3hJNYMekZq666kiJ6tEE47_iO2SCjQ5bGssTR_pmMtVe-zR5cHfd1KtsYq5TiHS0MfJ-DlJ6ipy1_yCvhx52Z2Vsb6bAygCHkcPxJa8gnNc2qQKbRxHnfSzd86HuqbN3fDejs7PnRzNtJf1II_qG-LiNuKcqYicvU5uAkEwHKRp1Ph2FXA30hn24na-hzOF8RCJG8DoEC3Dz5EszhocTVz2dsKhNKaNsaxiPxFOH93nNOtp_ioXBif8pKA_tsXACfPWaRmb0Ilqe62M3PUS3DBII4pNZAJ9S6sGUqJN0uBUUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=iS5c20PnR4aHpgYA8Qab4NYuegsEuzdMYEyNUzCPlvJrTJrK0hKA0r3OPJsOQoWzZyklGBWwlb3iQ6-F5CxC-EeEbL95XG89GJEFZjcCokSfjSV88JdlPmgfBMaPSLpsBn5wPMA2wEFsK0r-o6nUSueeJtrn8inSVmIBtNddOCr7P0_IZAh7lwFY7tmDPwU4BwLrHXgAVb14UvBbWRMQimQbh801ifLK6wX9fkFG5oRHQ8QV-e4T7tGVmb254dM-eLA7cThwKwnfXDe2Kn38ZWf_i8bCvjZkJpeFKbXIcrhqMu3GvMPew37w8Lom6M5WAVz2P7Vr48O038d2-JY9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=iS5c20PnR4aHpgYA8Qab4NYuegsEuzdMYEyNUzCPlvJrTJrK0hKA0r3OPJsOQoWzZyklGBWwlb3iQ6-F5CxC-EeEbL95XG89GJEFZjcCokSfjSV88JdlPmgfBMaPSLpsBn5wPMA2wEFsK0r-o6nUSueeJtrn8inSVmIBtNddOCr7P0_IZAh7lwFY7tmDPwU4BwLrHXgAVb14UvBbWRMQimQbh801ifLK6wX9fkFG5oRHQ8QV-e4T7tGVmb254dM-eLA7cThwKwnfXDe2Kn38ZWf_i8bCvjZkJpeFKbXIcrhqMu3GvMPew37w8Lom6M5WAVz2P7Vr48O038d2-JY9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4wbAa83lLhsIAAQn-xuFxHMUi_UXjagHNMTYQfAVKJHtyu3Nv9jYPek1UM75eXD-zKh0LDA5HKOBbeKsqcXf20kP-QR3yzHNPeObQFunRSoj8RccV8_CYFvFqpLSxxUqWCl4JULUbqCSct96op23GvDkYCfRtA68ud9oiwIHSOq9mLAqqXc608b-gqNvM_VNty---NdHaNRLbpmFY__TaPYQtd6fl6YmJJa3sR1ha8Y6waxMMmeo80FsuMc6N8Fs1dFsIt9X8Zowz5mtNABzb7Drr4yTJygXb_R_0fIFixwSLJGL4-dlftHfbwwIi75u3P_NMGKBCPNOhiq20qI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=kv7jU3x-urEhVpXMwK4P5HH9GCL6uQXMDesa8WBsDFHb2NpNP2jTMPQD4Gnk0_oiB6O_VuWHeBv1LXOLmFiTvxZuFIwSaN9O693kCJL4mpeliCNeF8E_B7-FzqsZJGVZeGYPHGTJMxVWlEFK8qy4SXf3EGGaA_5I9wMk8_E332cpCrlZJhExWSf-cbKGQ4s8V46KdfDEO2gnJMfQWZxn4nBknzg64HzxZd16qyRQ8vM8k_xIEvHJHp2pGFSP0amdBU8U2s02Alq83tiV0lvBicYBL9wrmLwF1oZO50q7j5ZheidMkDGGVFBjGGUIJk9cd-c8VUtwPy3tY-r-OxR6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=kv7jU3x-urEhVpXMwK4P5HH9GCL6uQXMDesa8WBsDFHb2NpNP2jTMPQD4Gnk0_oiB6O_VuWHeBv1LXOLmFiTvxZuFIwSaN9O693kCJL4mpeliCNeF8E_B7-FzqsZJGVZeGYPHGTJMxVWlEFK8qy4SXf3EGGaA_5I9wMk8_E332cpCrlZJhExWSf-cbKGQ4s8V46KdfDEO2gnJMfQWZxn4nBknzg64HzxZd16qyRQ8vM8k_xIEvHJHp2pGFSP0amdBU8U2s02Alq83tiV0lvBicYBL9wrmLwF1oZO50q7j5ZheidMkDGGVFBjGGUIJk9cd-c8VUtwPy3tY-r-OxR6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ReS2uwHvgr-WNk3n_KjS2LzTThPQeD2VE3mFmGoMVD2ymxsJv70oBlAjOPWG4d8-4Tl5R72qkfguO5wqGqJBu14mAgRSIARptorGTcUluhUS3OELWxZV2z6yOvBtZBZvYA0s7szK0tP7Hf3KeRVIqRHzXqXnOvA0GyMeLyiZAIhIdn0bLLsE-bEVyYyEZLz_2I_kHTEhQRhdPtfRauAOXJ-_fVKQGUUeyapAhqJEHnwzHz3qypO79Z29n3RpOsAPyuR6jzvaSXMKhTFdyZhbHr_m01lyOCu2RUY4Eo1ZTx0G5poiyeybMfuSYIE8we8zEXWZZ0o_KlBMOPHcesXdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ReS2uwHvgr-WNk3n_KjS2LzTThPQeD2VE3mFmGoMVD2ymxsJv70oBlAjOPWG4d8-4Tl5R72qkfguO5wqGqJBu14mAgRSIARptorGTcUluhUS3OELWxZV2z6yOvBtZBZvYA0s7szK0tP7Hf3KeRVIqRHzXqXnOvA0GyMeLyiZAIhIdn0bLLsE-bEVyYyEZLz_2I_kHTEhQRhdPtfRauAOXJ-_fVKQGUUeyapAhqJEHnwzHz3qypO79Z29n3RpOsAPyuR6jzvaSXMKhTFdyZhbHr_m01lyOCu2RUY4Eo1ZTx0G5poiyeybMfuSYIE8we8zEXWZZ0o_KlBMOPHcesXdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOwvyS11wCVx61uBoi2kGB8_RlYuPCGma82SbCOlndw7uTHecLiUJIzXyLu4Web352qrxuUILMtyFt8sUvEdaDgU9Eq7hBR-7GNLZ82ABtJ62VWcNiQuKHaliWB4550eoV71k4jPBZOxLvbdFyZFvdFG0sHj3pDa2ZMYTLWF3orqVwfPC7t7kT8gCZbaLJ0KQOvtNnXk3W9SFFnVzrg42Qp8AVhEQbw8JVEFUbmXY1wKdKExYSWyNR-eG8SeHMGEqACbPZ9kdUOJoDZxgUZH6P__FE0IOxKFF3cEGXYxqPVSBGSvRhp5_tYtZfZLwJA1h0Y8tTdxfCxcq4ZrjomJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqheyrFVst-q9D_aji1wKjr4J7iHox_aZr7a-kIMefaPa0ekwWua0IV37-w0T3Iqy39atWewBRyXNMwVSsmSiuLiD_cFlaQwuDfNq69UC1u58eKDa7UVQKtvWelzrnCuMBcQaF-ZJOHrhJH9jBAXoAV2mGufIxpSFOSyLQNL-LnzVFJ1dIrLhXlrkHyd_DAm7M9rQ19oRO57PFirUeX5aWMLnwuWmJ7RpLxIoh8spgmgAM9vPRSP-xV8oC6Zzh7jKAWXdoXdMnbC44UAgvpm7HFid4lxX1qeDUqGw3UgbUspsGzamtMU3KYdZo-pOAZyI_zkViF5xg9ENarjcx97cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcNO7-RcT_5gBfObeXYIizj-LQAZarPu2z2NHIqgk-xfUQqxroIu6vjyue8XGEkahk4Tls-OOlZGDdBNjPPFCKUVphEEw56N63x8Kax31ANNy1nlimy7OTUwVmI2v4_PWn7FpDgcb6HvyHrUBXn9ks5GAl9VLGa8jEX9Ych6NPzrJSCJtU0nxzvABV-iCmEmD4zILCWf4Cm4LKggjEtt6UIXqiD1JO37QRbzA5yznTe1E-CSJ4nKTlzthhiTx6EYZConQmMmcfipStP5XhKIg_HyOp3O78N31LkndI_bRHfpqtK6t7NZ0cBSFBoQ7b4d9W5VrHSoTxWESBzF8bHozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmH4owHbFWD-M--BsWZVZoCZi58iB-XI5VRlTvAudeduMx7EjD-mTHtz3FGCL2Wo0PDmDbOAlksjtEhu2O0jev_RVjF8YTWnMgg60OCTV6pYvVm1lWpHPMpmIXab5z8tHkjexdrpKrcuRg5dQqNGw6lIwTEgV_wAULWQuDvVoQRyY0eQ93n5bTVcF0F7H-GT1vR_fF-MRxjBBUvScsAnaDz1RFK9Py90p_XM-cV5oAvtTz82-bu3MRd6Uoa3tA89MAs2F4cx1pxYA2ORg1_JYO5w-lvKQci1wkvhGWYn3NqBYjzulFSLaZvge9OMh1O0Fl4UHh8ym4IQ0bxgoRes9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=aomL5uQDokHyEeoL7UIZDVPvhgGkmIiEdsN5vRIkHHPRFaw_J3lX_QUuFuAcm6M2bMtLPGpILbgzmAYLIC7XgyX_Litny7nEIkZ8VvGZOd9X4nzV-_R3z2CWWGdSZP3gLxHFrRfBzA8O4WSA-X3MISjuDMqRzkeYca0dQObDtyPZMNRF12H24HXX14EO-0nFdMG5HYXqT2S1SuO9h0cjap9lwuWn10A-aDCk9ia_ksoxJVnBszl6g2Ty7O1Gp8JscXl70812I0sTji_7q0xdlrGvYpKQtvWOG4EztATRWuLxfSH3Cb7mcGNXzVuWImGGkPwOLfq-H2MZv2Zj2DFcEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=aomL5uQDokHyEeoL7UIZDVPvhgGkmIiEdsN5vRIkHHPRFaw_J3lX_QUuFuAcm6M2bMtLPGpILbgzmAYLIC7XgyX_Litny7nEIkZ8VvGZOd9X4nzV-_R3z2CWWGdSZP3gLxHFrRfBzA8O4WSA-X3MISjuDMqRzkeYca0dQObDtyPZMNRF12H24HXX14EO-0nFdMG5HYXqT2S1SuO9h0cjap9lwuWn10A-aDCk9ia_ksoxJVnBszl6g2Ty7O1Gp8JscXl70812I0sTji_7q0xdlrGvYpKQtvWOG4EztATRWuLxfSH3Cb7mcGNXzVuWImGGkPwOLfq-H2MZv2Zj2DFcEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uV8qJ3gtkDjSyxzPLRHWyCLFiq_5btw1Y1o5hzo3dVa5YaHqKa9ucpXmHDsXeabM8pBglpYctOHIg1rebqtmdxC-CLK-nS95SCm7Mx086Mrf2fqRP0HM15qo_c6UYpYAvYbi46-ru1ij4FOecZub6XUEtjsS-zMJAePq_gc3sMNSu7Qh8FeX_f05W50Jb4z2kjJ3hbfV8Mia_tGs8DfUNojHv1nkiaNhozcf_lYFQJstNgDOfPhF6ObAJE72ZxlSbiZ0nl3uJDHLrkwCwqH6MMgipaA1KQ2JGMePICWO_sxP7gzU4FRrt1SqV56LAXSmgjmhJzPBqq8FHFhSycNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQxbL0Rwfd2Imqs1L1czWbLK2lRo46iOAdrQqIsRrPOJNzVQHC5ccahFNTkXsLh7mm3X54GLX2qOQDir0dfYNikiBHnrmTAJ3xuVngvrKeejI_yz_H_Tk0worEyd8tIKIOO54GRRSA7GlIDNTXI04GA5O0pzXKOhBJRnknEjNyxGZv3tBQrRp8EGexKqM_UdA85isJDbQjNuerhUiPG9Ny4iiJ6iHzyHobqQMh0jm-7gc2wNnqwKqhtId05ow8xh5VV0fgUZWGZfa2ALOcKWNZR6J_gsJCAa-daNoLys7LIitWpxHo_g2PInCQQ_oykv10clbxKAZFjLfJ8I4MXwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkIj_0f4SeqwWJdMXJK__eYkDPVCPv4ItN9NDpRjKWuqHYuJ2HvWaf-EfEL9S8XfYJOHvmuaLRtM80FGnUA_T4cue-6evp7_caeU1dLRjLsw5s1rNqrz6xAY9bSnRvh1uCAL8ccrMCQJrlkSSqjyzk_A19TuuZtm8cHuYa-ixXp9E8DazZ3e1viQT2klxcjv42dye3mO3WpDlPuJXlkjttjcoa72BiaeWd-Y14PzB1wLhhJMeeFdhUPrJgIi1nk-jKBKuWzNbna3aG5SURKixGZ5sg5SjyUTCsJA5SqB9doLzlTU4-2Xzhx9WLoKO8FdNeAY0MiLPq25FLHgc6GtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUU2mQORgp_AJN2zNIVxnUrERf52O-F3bcwAD9xqHVA5eeydJDb5VX71JFdiL0J-pK5Y0QlvxDuvVZewV7bSD4nsJSil8X9_fPNJF7hFlDAcZmHzPexh7ZRZOrz6Lc6z6wv3DGkhtzeFEeQ-a63qN6cBPy5ERsz9Zq0rujuEtU_gXYZHsamOIp3sJka-QOTfeX5FMQ_15cWd7hhwg36eWZubo0KQThCIPBRSrhv0IRXDLCgCdOHuRq5VVL4QoUeqifQd0sahjTKdnlewxTl7rMQnPRN6vMXpqXoewTejp_eTUUYStZH14M1Zq2J9bWy0OUGpjpG4FCWHWqVXyPmWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPCPj5nTFM8wbiTN9jVOUwQJeiWt_dLhQZu7o2LWdNiWpKVM4LlYKm2I4HlmfNdcz9XTE7GWYRyn_83A40rs0Ba1nQ_sb_W5t9QUFZmCGd97tZLbWFieIbE97qUOcK4mHy6ju0IGPqGsjQJ5iamfMuYJDcfJ74rlyx4n70lq8HrQ-XrwuWoo9xecTvtGUFnH4pAjD5DUcX8ACXpxDX1lUkEJlcf3nJ6PcR4U2vIVeIcdgYLdHD3KDRwXyIdje0mvNUJrq6rVuxd622muNh_eSqB90IK81oMmm0xGYiXx_QhCNAmL8E6l75UD3DEq1Q5qABDgH2sMm1pe0vfz1NyJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=DbFMxmImcELN-d3JilLxNKfKigZOYAya5acVFkKQNxNcXEF3YtUbgPoKf_HlidSHJH2547w4zmTIwS_b7kGyznqJO-ad7ELE8VDio33IlYcaZujjjxk8NA2x-VnaKShFeUCoTv12_flVnZbyPOy_ZJawpIL5IxShtEqfiCAowhPjId_NKQ-YZY7tzyuv7kFSAHlA_hRHJWj28wnHC42W07GBt6l-Bi_tg_4BGT-P_djj0TLUFB28y15VEpsTQ8GQt0NU3efe55BHFFKoqVb_pVoJ1xyPXdyPeqDK40iQWoRz_U6scGAMav5L_J-6YAru1Gp4cFQ6dqVnPDEFXTDq9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=DbFMxmImcELN-d3JilLxNKfKigZOYAya5acVFkKQNxNcXEF3YtUbgPoKf_HlidSHJH2547w4zmTIwS_b7kGyznqJO-ad7ELE8VDio33IlYcaZujjjxk8NA2x-VnaKShFeUCoTv12_flVnZbyPOy_ZJawpIL5IxShtEqfiCAowhPjId_NKQ-YZY7tzyuv7kFSAHlA_hRHJWj28wnHC42W07GBt6l-Bi_tg_4BGT-P_djj0TLUFB28y15VEpsTQ8GQt0NU3efe55BHFFKoqVb_pVoJ1xyPXdyPeqDK40iQWoRz_U6scGAMav5L_J-6YAru1Gp4cFQ6dqVnPDEFXTDq9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=EouT24E9BTItyqPRPlM83Mm7YILtVTnCvX7FDyUsEZA59X9SSSwoTdEpkJrlk3vVG3dcmF2y8tmYRX3Mul6lWpMdlm4WaNg8te2-vTEPeT0Z3Xnj1-ZmXOIvD0iml1FC5j5l5v_fOD6blHUxwpaieZ94YsxzG4waOE_G14BDpgsrrcipWT0ZJs1RAFQCggXwsT3kDq0Hdbh8yoNAOzkRU-Y0vbxcHfSqrv0m_hDga1L9DZmkqdNJhPHWOawd_1LT485niLD_cChtJe34FMOOz1bOBLtLrSBIzBTECPEKh8FkIf4zmHk3oBU52yavXw4RPm0ypvgf5onTn-Y-vG3_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=EouT24E9BTItyqPRPlM83Mm7YILtVTnCvX7FDyUsEZA59X9SSSwoTdEpkJrlk3vVG3dcmF2y8tmYRX3Mul6lWpMdlm4WaNg8te2-vTEPeT0Z3Xnj1-ZmXOIvD0iml1FC5j5l5v_fOD6blHUxwpaieZ94YsxzG4waOE_G14BDpgsrrcipWT0ZJs1RAFQCggXwsT3kDq0Hdbh8yoNAOzkRU-Y0vbxcHfSqrv0m_hDga1L9DZmkqdNJhPHWOawd_1LT485niLD_cChtJe34FMOOz1bOBLtLrSBIzBTECPEKh8FkIf4zmHk3oBU52yavXw4RPm0ypvgf5onTn-Y-vG3_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=scGsm2voy_HxpkElT7aomQrnENDBov9iaDvyjl-ElpXzvuJC3DlyvuNLny2oZ44puae2vUnMUssEmsGj38M6mXmpQH4jUhqywJjWQlV9Wb8To-0wTJXMyi0CHDuEtArjuJDieepcdhRpVVg6n4hFalyXVwRjNmAJocrelMzu8tO61kgqDnAa_0ecWqviVPidUUEfNl5XxcWYKJr6juI_HvmAXhHUCAedPcaFRzJZYT4wHnD5aKDEO4_8VuoYPD8vfr9HPVLF0lFH4GmxCXF8t-_KVAmztBIRsP4YpU1iAtFiB6C6eMy41i1TTlELvS_bnuX_YVdGMf8T1xWHuvKRDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=scGsm2voy_HxpkElT7aomQrnENDBov9iaDvyjl-ElpXzvuJC3DlyvuNLny2oZ44puae2vUnMUssEmsGj38M6mXmpQH4jUhqywJjWQlV9Wb8To-0wTJXMyi0CHDuEtArjuJDieepcdhRpVVg6n4hFalyXVwRjNmAJocrelMzu8tO61kgqDnAa_0ecWqviVPidUUEfNl5XxcWYKJr6juI_HvmAXhHUCAedPcaFRzJZYT4wHnD5aKDEO4_8VuoYPD8vfr9HPVLF0lFH4GmxCXF8t-_KVAmztBIRsP4YpU1iAtFiB6C6eMy41i1TTlELvS_bnuX_YVdGMf8T1xWHuvKRDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YKRgt_5w_CKyNkp8VETJ1K-kxezXlnbd98XbUyU5WxrXRiYlLRe4gmFSBMfnJ2ysEYIOPMQQTlko0ipnmgNKnxg0fU_1NF57xRewL3Uu6lusVdJvE5IvCyUvrmcreGd34S1Zpwk07oBzw1f3zi6NZQaIV9W41hp2J6sH3aDq0_rAX2TUA70TKXlullf5hskYghD_iyQZeKKylDQLsa-GOGytKhwGW23d4Bx1m5nRnar7csd4Ot3QR7bCKE4BhQJvmvnXkZ_mKf0FmJn4yLh9RxQyv0KeSmC07zDmUyHoDlPwLWynSpxzIbIkWMWWG8-Gt5S6qqdRXZNFK-jYMhFWF4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YKRgt_5w_CKyNkp8VETJ1K-kxezXlnbd98XbUyU5WxrXRiYlLRe4gmFSBMfnJ2ysEYIOPMQQTlko0ipnmgNKnxg0fU_1NF57xRewL3Uu6lusVdJvE5IvCyUvrmcreGd34S1Zpwk07oBzw1f3zi6NZQaIV9W41hp2J6sH3aDq0_rAX2TUA70TKXlullf5hskYghD_iyQZeKKylDQLsa-GOGytKhwGW23d4Bx1m5nRnar7csd4Ot3QR7bCKE4BhQJvmvnXkZ_mKf0FmJn4yLh9RxQyv0KeSmC07zDmUyHoDlPwLWynSpxzIbIkWMWWG8-Gt5S6qqdRXZNFK-jYMhFWF4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=JXUTK7Xw90NS1nCwLyxoHqekfbeAB1zpF3vI3ZNExqCfdv4T-wi25qemSKz0HEdalAXx4T3Bx5F0RthWh2CYCV5beG58eVvUuzhOjc62ozxIHzA9C_Df2hBU_aUqA8nniEbaGOcsDQz0-Tk8JCm7mLYoViuCeIg7EowAMjj2PqFSjTRY5kpLSHKueFz6ZQY5DNpQIuqXJs4pE_x6cLijdFvIOaU80pXwFohTdSNY1GfjRqmSnqsjO7KtpgsqsYAhYr0JBNsi3E88vRAxMuiDz_W0-VKubdSLakpHmHuIZtvLwRX8JLMdfa3iLfGhoCnkk0W1__Tbpk7j5iOhW86WCDBABJqZYnBmJRsF_C9WQieiz1YeL37JqboPt7hsn8adTpI7YRLAN4CgicZmKkW4Q14g82W9IIu1ZDIUyWPlgAnDATY8NoMeM9hQm0rqyJSv7OkDd_aL6EWUk2_86aXJ7EGtSYrWMMoaht1D7qaIx6v9PBP7JKkD9DKsvKbqyi9h6SCaO2pUKMkThdKzWpoGdh4nKUiFlUaA59xXQFNaFR6jopQAeKBGoni8EAm7SNQDqb5A9AAL6bNUriCNQfNByBlPVTR8BHCf5Lb4synOMn-a8OhSHrLUmRPg7zQmI1YiKgtO_L6WhnvkbRRxKBQPD2SO5hvl5b81L58haoiMYW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=JXUTK7Xw90NS1nCwLyxoHqekfbeAB1zpF3vI3ZNExqCfdv4T-wi25qemSKz0HEdalAXx4T3Bx5F0RthWh2CYCV5beG58eVvUuzhOjc62ozxIHzA9C_Df2hBU_aUqA8nniEbaGOcsDQz0-Tk8JCm7mLYoViuCeIg7EowAMjj2PqFSjTRY5kpLSHKueFz6ZQY5DNpQIuqXJs4pE_x6cLijdFvIOaU80pXwFohTdSNY1GfjRqmSnqsjO7KtpgsqsYAhYr0JBNsi3E88vRAxMuiDz_W0-VKubdSLakpHmHuIZtvLwRX8JLMdfa3iLfGhoCnkk0W1__Tbpk7j5iOhW86WCDBABJqZYnBmJRsF_C9WQieiz1YeL37JqboPt7hsn8adTpI7YRLAN4CgicZmKkW4Q14g82W9IIu1ZDIUyWPlgAnDATY8NoMeM9hQm0rqyJSv7OkDd_aL6EWUk2_86aXJ7EGtSYrWMMoaht1D7qaIx6v9PBP7JKkD9DKsvKbqyi9h6SCaO2pUKMkThdKzWpoGdh4nKUiFlUaA59xXQFNaFR6jopQAeKBGoni8EAm7SNQDqb5A9AAL6bNUriCNQfNByBlPVTR8BHCf5Lb4synOMn-a8OhSHrLUmRPg7zQmI1YiKgtO_L6WhnvkbRRxKBQPD2SO5hvl5b81L58haoiMYW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=dJURtavaNn2eAhYSBSZyXbQ3wTBPDWeHFoJGbN4e45p0G11I1lFwmjUY0J2SSLXvHZp9W_MzATZuML8wcziiYYKWHZER6Mg3pezK9OH_YUEf5Ltmj2CvdadxnHXR8FWMab3rZFdAbFWMqk2wxyDPwT1Cjr0-eQRWn-cLIBofgpyawBnzCPSQVGAzH7Kl-Mcea21artbIABC1K75WU2hG7O8S8E2Akp-b8WsOcw5llkrtYSi1tlh4rExQWT8iOk5Dno5seGFjgYCvRFqg8wZAfp7LsQdKy3UmxGegANlDAywxGoCVULv6d1P6YYN4Uv65QQO8j-D4_zv6WL4PlqSO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=dJURtavaNn2eAhYSBSZyXbQ3wTBPDWeHFoJGbN4e45p0G11I1lFwmjUY0J2SSLXvHZp9W_MzATZuML8wcziiYYKWHZER6Mg3pezK9OH_YUEf5Ltmj2CvdadxnHXR8FWMab3rZFdAbFWMqk2wxyDPwT1Cjr0-eQRWn-cLIBofgpyawBnzCPSQVGAzH7Kl-Mcea21artbIABC1K75WU2hG7O8S8E2Akp-b8WsOcw5llkrtYSi1tlh4rExQWT8iOk5Dno5seGFjgYCvRFqg8wZAfp7LsQdKy3UmxGegANlDAywxGoCVULv6d1P6YYN4Uv65QQO8j-D4_zv6WL4PlqSO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUVmwPnbckHTtyoQf4e9hMdOBUE-v58dyy4TyJj4ZkPb0JobCVVBcmXeK15flJVtwdMbacB66S0NenxKy86CEuxsQZhxD7aHqRk0CjEDs35INLAZuEkaA6nr3j3GoD_QrqY-iSJ2SzpWBJp4I0_XkVa4dqpK3jV5hatfsY5VlSeACZ5V3Xv-0qSJWDb7M-IiiDItyTpS0dggxgHN6ljkZBZ2_WvJrjofPhCHGUO_NMlIIZrW6ZHB3mtlpv9hGE53LYJv9JgX1UshPMxgfJiEpJAL5OLk4QCnimiPcYRuW8SYgcdYC-Mn1-JpQAukb0jIBWCoOjHtV5ebo2Q-9XooOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byV36nwE0u7aNit0EbTjQk7Gs2WL0ZcjdDntWIcc0VeuCkqee2po6QDdnmgr6Po7aYL-tqVMLMEFCjArxR3RfBgOfoRnRELVbYPCudKjJpUOAaB9NjJy7qBHY7qXTahUcAYC6oEkKQgAvclnkJI4JwfvDNQUy6yca_7x2aKwEYJ8CSmBHrJsNqfUTY_BUYFm-I1vW-ETcJk0-T3y8VtTAx8Aq1gbyBIBn-px-iv0MbKzHkoOSdQV1Ozlucl3Q-ioAF047SndA3_4n0x26SBBOLcB-4NItgh1sgzRogxtbVthZVo34nywX63n_ZhbTjemcF7aGyX6M_pkHShlNHBQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AATYoGWyZ7ACVho_S8Q8G3GcTtHugM32WLX_J4GoLcofw5_DUmP7C5aqybIML-K2-9XEFETNVTIFNO3rpsNNY4fUSmQ5IUpUVl5sU4N0ISw4kEDrgLtorfm-iqKLn4dopKQdC94YRlWzvzfCTHJ_UA1_UjU25nDHL5SpxPV1ryrx0sKBXczPS42rhfcfoUVhCxxK8Se2jEG06h69n0eBf7xCLzkfK-SGLjNzaYrSFrVff3LXFnfEPsYAmJyJGWIPrufkhVCI5nN0BzhVXBhr2M_1jRofrIFvsqlbEsNhd6Z681XQJMOpWa-951-61a5oW_WTnKqo6shNW6Cvn12tug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnmy0R51-6MMnqUsE-UF858HqVQKwqeLfMAgPzApYJ1dAWh18tOAg4pGOZACzB0F9W14AwePaJiLrFBhjTST3ruoyQus04kiqJsMrPkcu6lS_KFPCXHonh6w4Aa1A7TtmhrIrEvzlNAAQaTeFabzArVTsZHH9j6Qkb4A1dE8BxY_3fpCcdAn62CkYuaUQ2bu8TnRTNIwei_FJrCzOflHL4z5xo_qsbmP21BKETOaoZiQDGBzFA8QWPZ-0eYmxq9KFev0wJBqfRGwr8Nr8nBa75mXszVHzh0JR4Pd7WDQnxTd2L2le85d7ALBbE4oecr0OYFcwjob6-6IN7ooyTmGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSvYn5s2PkciMA_eevBgUvL0o8QVg24h9jo4ETDqWdjH67GqDSWC9i4xCEPu2fx-2my6KWTD80OYkJDpZwrGYcXEFOBGhxiOXOB2MNwa3N_xmK-nlLm_lK3GAmqqDE5LU_E-JjtJMT_f4RKmRqcAp_pt5VZJwS-vEjfk1JjBssZgHrorero6WuAIEz2DENkUbHx0VKbwmDQGY3-x_iujLWwCfRyi5VcNVB2lmPWn21gcv6eej8G-LknJYmPzNLDZ58cds81r1etHz8xiB7Y8AxTjxShLed0zaiuPft_QC1zpZ3YomqTh3104_dYYXJpFJgA9oAC-D1A_GnolvAokCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=r2Rc5mLpi8sZhxwdmYYQVrleT-GA2wWzkN4skv591zGtGFXCIplj1iTw8EUZ7xnqsO7uxYvJF6rJmKbH1IQEEnmSYHP-N43kq4xB-B1yw3LF7sDR7lsi12_7ksNOnzY8PPu0YRJji-bsNZ6-OHmWMjF40YiVLuIh5VIKpi_jO4uAwMRhxB76NqAGX8WXyLUy_5gxRpfKwGt0EQ-hx0RcWML9I3F5sToWNr2FheoUpyplmboCJO4pJlB8R3TAoIHWN_GJHfLgg656QLN42LCZgdYcyHZyyaQUFnaKXXzG9j1aXM1Ez8LePZBx1dG6mLqcNnxJhVesRFmdg-fd7sX3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=r2Rc5mLpi8sZhxwdmYYQVrleT-GA2wWzkN4skv591zGtGFXCIplj1iTw8EUZ7xnqsO7uxYvJF6rJmKbH1IQEEnmSYHP-N43kq4xB-B1yw3LF7sDR7lsi12_7ksNOnzY8PPu0YRJji-bsNZ6-OHmWMjF40YiVLuIh5VIKpi_jO4uAwMRhxB76NqAGX8WXyLUy_5gxRpfKwGt0EQ-hx0RcWML9I3F5sToWNr2FheoUpyplmboCJO4pJlB8R3TAoIHWN_GJHfLgg656QLN42LCZgdYcyHZyyaQUFnaKXXzG9j1aXM1Ez8LePZBx1dG6mLqcNnxJhVesRFmdg-fd7sX3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=g0eGK-8v_jGvEBJbXwnwN-pe7rnHeWfwbOO_AWySr_qw9uECm3biW81GgZRnoRLWk4tNfS_jff3ZhbZB5pCwH-_jFBYqs4iPWUitb7u48Bbk02UvzLj000EQ_4ytJvgrhjTg3_yMaJEYvZzrBLGMknsYZ62pzrUILwu3wk4A2oJR2Fz6TolClQb6H23X8BTru3gJXTqC3G1_m8Gri9WfSSV-5VC66UYCzAXDa-gjvwLyuCRa9A6oS3TArndX9T3MdjzWzUK-mCQ8XF36XbT5ikbnzjTGQRhAaa4oQ4kSRISn9e6EYRq47JTf681Ex6w0dQmyLI3YkPIMmHh4faeaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=g0eGK-8v_jGvEBJbXwnwN-pe7rnHeWfwbOO_AWySr_qw9uECm3biW81GgZRnoRLWk4tNfS_jff3ZhbZB5pCwH-_jFBYqs4iPWUitb7u48Bbk02UvzLj000EQ_4ytJvgrhjTg3_yMaJEYvZzrBLGMknsYZ62pzrUILwu3wk4A2oJR2Fz6TolClQb6H23X8BTru3gJXTqC3G1_m8Gri9WfSSV-5VC66UYCzAXDa-gjvwLyuCRa9A6oS3TArndX9T3MdjzWzUK-mCQ8XF36XbT5ikbnzjTGQRhAaa4oQ4kSRISn9e6EYRq47JTf681Ex6w0dQmyLI3YkPIMmHh4faeaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=JMo98KmBEQ2VOWqBz1NxE3at-18BPThKfU-35gX3ufA7toJU9o4DXe5IVxsr-gxMkiZ5FLsAjvfxcwjMtKdZaFAZCQyb3gmwkD0BZHzxwFyvgPEDjPh2_6koldmcf9U-e317agNpBX_2EwHY1Z4Tf2yjKSmrxrm4MnFz_nNrDK8SDXB1yvY1LXs9xAap0a4X7dOQ-8_Jb2NoWAUyiQftg_oR3ks78_4ZCFveJG4UpWRxDfv3f3c3xFhMMyhRtDTab3aVGQ8wBX2GenMsfeQDUXelxJoKYs1JwoW1EqIlYXPDmDnc2mnSvfMbcYUt5-ZX9aKPdxIi6pqe9D58_Xz17w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=JMo98KmBEQ2VOWqBz1NxE3at-18BPThKfU-35gX3ufA7toJU9o4DXe5IVxsr-gxMkiZ5FLsAjvfxcwjMtKdZaFAZCQyb3gmwkD0BZHzxwFyvgPEDjPh2_6koldmcf9U-e317agNpBX_2EwHY1Z4Tf2yjKSmrxrm4MnFz_nNrDK8SDXB1yvY1LXs9xAap0a4X7dOQ-8_Jb2NoWAUyiQftg_oR3ks78_4ZCFveJG4UpWRxDfv3f3c3xFhMMyhRtDTab3aVGQ8wBX2GenMsfeQDUXelxJoKYs1JwoW1EqIlYXPDmDnc2mnSvfMbcYUt5-ZX9aKPdxIi6pqe9D58_Xz17w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvKU1gRyZfUnNu1sY-BkDGsBBN9oP_9bf-PfDzMV02as_iTke4G1-BnIp72o2YUT16JznH8kKcJNdP-Ok7KWnJi6dUk6ElmyRROx6es6TkGmVcKXD0nNQTSh1BnCJDGs2YIfV1drloCWsjbmnuWKUY5yDkayI0DG_svfC8YGpfMaTjOVwtiRsFUgmMzS7j6kFilEbqymmrciCh6zxjA8V-rWM9PZLWGuENk37ZLkuU5d_aG7i_gEox6D78OMRdqlMWTQJqN-uqG0MYE8t0FqFwhdhHxcLrKCglBLy-7zSxxZ42O2jV_SccV734YYknix627jOnFQkECiPFCI-ONNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=CY5XeqmN-l2sqzqxlk2wOshFF8LjOjwBg3L2QllcUvXd_Fbc6KrlG6LzWqS2ALhDpFIsI7J_Tycca_J0n62kdze-17TVPxTYAkNIUyZQx8xPfkYiJg3PSuWWClMdVeqRdY7cD4QB3G2DX4qulT62WeaTbh9Sgaf_9P2rjrYmK_kFPUzfnNJct1dJ7rVPp_SpujGrzaHaDdfy69xRaimvdeC2Ov3YfrmITLnJT-qwfzgq0N6q-qrow4lJRD6XlHxPf9HxBiahi3bzlDQ8h9jmXwhRM7PhKtgKUAHf5nbAO9IErYqVgykizSF77wikXlL4b6Kh1DQ9qeSSNZKLx11SGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=CY5XeqmN-l2sqzqxlk2wOshFF8LjOjwBg3L2QllcUvXd_Fbc6KrlG6LzWqS2ALhDpFIsI7J_Tycca_J0n62kdze-17TVPxTYAkNIUyZQx8xPfkYiJg3PSuWWClMdVeqRdY7cD4QB3G2DX4qulT62WeaTbh9Sgaf_9P2rjrYmK_kFPUzfnNJct1dJ7rVPp_SpujGrzaHaDdfy69xRaimvdeC2Ov3YfrmITLnJT-qwfzgq0N6q-qrow4lJRD6XlHxPf9HxBiahi3bzlDQ8h9jmXwhRM7PhKtgKUAHf5nbAO9IErYqVgykizSF77wikXlL4b6Kh1DQ9qeSSNZKLx11SGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=vMImSr4hOWKJ-CrujQXY7okFHBIqhrA2mhIfl311GInWtvtbH706JnEYyPOn6ZzFxKUvRXrLHRJvTeUHbEXHE6FqaImMWhCdTi3JrWoX1OHs8RD-59doWjXGCFDSPLfurHzhdE8PyFSFB-jNl-uRYfGOb-qjnri-9CSI3GPZAPPIKE62hoQ87XS-RZML8mlUjlHL6IQ_PY8Qr-FQZmU7GQcmTRxr8ABobNANvLQgmggijElfHq6HiO629I5AQi1FMLUrHyhj4C5IBAK4hAM6mD0B08Egk7RJMW2JpVXMGXcOHYsduvDHwH4Dk1GwYhinvoLccZPCFQkGb8IpSGU6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=vMImSr4hOWKJ-CrujQXY7okFHBIqhrA2mhIfl311GInWtvtbH706JnEYyPOn6ZzFxKUvRXrLHRJvTeUHbEXHE6FqaImMWhCdTi3JrWoX1OHs8RD-59doWjXGCFDSPLfurHzhdE8PyFSFB-jNl-uRYfGOb-qjnri-9CSI3GPZAPPIKE62hoQ87XS-RZML8mlUjlHL6IQ_PY8Qr-FQZmU7GQcmTRxr8ABobNANvLQgmggijElfHq6HiO629I5AQi1FMLUrHyhj4C5IBAK4hAM6mD0B08Egk7RJMW2JpVXMGXcOHYsduvDHwH4Dk1GwYhinvoLccZPCFQkGb8IpSGU6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=dC9P0xsKnhN2uV-2GHKrts0DhMwwsb7P7H5Nj94JLG67ZYzqEGO-8uD8MpxJh2ezLO6AO4I8tShBCAZKeJnMu-wVfYDoFecW0kw2i_fx2lS0bflTbFPaXxKewanSHEUxm1288H2HxAkH6mjp33N5_q6XGNFvqC6dRR77IhxdrZqRKp0-U-kVgQYmmsRVTllJ8mGYjBNNfD3qjsWtiUdmFrT1C_CleghSRs81EqDIPZNajOhuvWpxQqjzU-VJbNGz5fCkZiq2jysOdeELfQARnnatZzCYgeMcjHm8I8TK6jjc0TbDMGPO1lPe4kH-81XkUFAP8FOAI9PeR7qMLaU47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=dC9P0xsKnhN2uV-2GHKrts0DhMwwsb7P7H5Nj94JLG67ZYzqEGO-8uD8MpxJh2ezLO6AO4I8tShBCAZKeJnMu-wVfYDoFecW0kw2i_fx2lS0bflTbFPaXxKewanSHEUxm1288H2HxAkH6mjp33N5_q6XGNFvqC6dRR77IhxdrZqRKp0-U-kVgQYmmsRVTllJ8mGYjBNNfD3qjsWtiUdmFrT1C_CleghSRs81EqDIPZNajOhuvWpxQqjzU-VJbNGz5fCkZiq2jysOdeELfQARnnatZzCYgeMcjHm8I8TK6jjc0TbDMGPO1lPe4kH-81XkUFAP8FOAI9PeR7qMLaU47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=X603QNgfgXJXe3PsC2UjrG1aG61LkvpU9VYyZGylwiQOEyNaAWmRWfVaY63qF-xMou7OGIquWtUFdKwirsgA7UTor3HK2T_coQnkdIA0X1wWQF8QpXWfIb3OdTiFr5bgdsGU2TSa_21lspS8mnwlDqLsZcBh_3c436D7x6jf8uB7KSA0l7oa5IAVSlA2IHfHb5J7y38y-FHIMUaJJ5L0WbOztipi9g9i4_YdfHUMeOK6bCgnqSaFMfWdDW9o6zQZAI4BLVnljr_iBnPH40-GEeIbYEjiuRMjfTTXSdS_URI931cDVa5BvfGOk3MeSg7rvtrdqQ-l8fJllMAxuz3_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=X603QNgfgXJXe3PsC2UjrG1aG61LkvpU9VYyZGylwiQOEyNaAWmRWfVaY63qF-xMou7OGIquWtUFdKwirsgA7UTor3HK2T_coQnkdIA0X1wWQF8QpXWfIb3OdTiFr5bgdsGU2TSa_21lspS8mnwlDqLsZcBh_3c436D7x6jf8uB7KSA0l7oa5IAVSlA2IHfHb5J7y38y-FHIMUaJJ5L0WbOztipi9g9i4_YdfHUMeOK6bCgnqSaFMfWdDW9o6zQZAI4BLVnljr_iBnPH40-GEeIbYEjiuRMjfTTXSdS_URI931cDVa5BvfGOk3MeSg7rvtrdqQ-l8fJllMAxuz3_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=PWZYt7ktO8XcLbJWF4UsRe0PQxm1fkBHqG5p-B6_YCQR3dv3ywca61dPTSu26XVtZ0UQeRykiNkQ8fVDLiNb1JIUpUuZmrgOZOuGdVhTqPUY6TORKGhJ_SERW6XMS9UX7M8YorcGaczEY-cPSq965tbKI18mSfuRyeVyZi8A-bQw2TzaljxtrNCCws495czGsqnREZDyFo6XM9JZRnV3LJg9DAdMZi_bfK6N8PRFnuTa8037cc52J9es_9cApHhY7Lwu6QY5l9wTC-3OYz4mm1NTK84nuLYc9tyX_FKKTH1xAFlAfFrq4nE23ruJRyr9fPVNqNh5thI2CCri5U4bHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=PWZYt7ktO8XcLbJWF4UsRe0PQxm1fkBHqG5p-B6_YCQR3dv3ywca61dPTSu26XVtZ0UQeRykiNkQ8fVDLiNb1JIUpUuZmrgOZOuGdVhTqPUY6TORKGhJ_SERW6XMS9UX7M8YorcGaczEY-cPSq965tbKI18mSfuRyeVyZi8A-bQw2TzaljxtrNCCws495czGsqnREZDyFo6XM9JZRnV3LJg9DAdMZi_bfK6N8PRFnuTa8037cc52J9es_9cApHhY7Lwu6QY5l9wTC-3OYz4mm1NTK84nuLYc9tyX_FKKTH1xAFlAfFrq4nE23ruJRyr9fPVNqNh5thI2CCri5U4bHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9YnwecoMPz9TVFyN-vT8gGTo9z8XeYNFyP_FbPmlQSrHCZcTijP3xUt_-xeqB4I6LfFfFDxjSEXShaW-GPZel3QewpTUn5BYhtI37ZTrZ_auSVlb9Iiel1B5rFjbabJVUH_n4V-He1PznGdE-h1cvkNy4xYm-FvkhlXfytbgQ2ySzvXsS1SnbjIKFLHkcc3coBHjxtuReJz7a9TvcFs0zzr-mtx467mMdvZW7Tmeb2V1OJL25jnDue9H52hDtrJpkdzBuCl3VP9idCqTBf9oKJJNT7kJ7YrUFFRwY_T3h80dTrodq0uSW-i10-y6oigTsSE2sDQo0J5Cx_X2icWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXJUB5hmkfr1zD1i1061UVKr8ZKCYr-d8Ul4znF74hZiUQ1su5W--WMjUxbJhRBR_28yyzlvs8O79blSchL2TVxQeOTQ1VmuCdbVwM0MUc3ItyQBa_2qtWpBa82xX_ccxeCzjX631slqPInz5VQk07J2oiKN0i-XJbH-cjNMLJDHAIgRv9Uw9IAtF1URwROl0yW0HZSKPFrTv9al_mXk7PTQMjkBEJ-56uc2gdH4B9Fucqmj6pTV7_w7eOycRl7L9pHN1AYRWTHnH1vNOYdpS1rBS5yZk-DpJ2tm7eAffFeUVX0RjBYHlc_OqnOJohV6_CAyLQMbrwawOqAFqLx3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKtDbGKEwqTw3HhzGOUC7Vbzuw0BYqC55nVl7oDG8L0gfTxP6s7KROV9iuKkRFIHPPuRX_5xRPWm0O_zTVyrwxf_Vnjr4ZWm879VZMl984WlAGg1U42LCR3rn5NoDc3vKWkntKaOLFGNKJY_hXTvmUguCEjGIuMD_GRvBvzBjdcWzd79uER8TBQ_gQfkYNOrisyqOVSLUhBo_vCcCAnCcoz_JxDoJ-Kfo40auXgV7gCzJ3cZ079QbeIJ4yuZed3Z8a-veKEMWDvljywru_VrJO0KoWLRkm9MyobSs0xvkWkigLQntxh6IHeyCPjVBKAXbhu3iQSYl-zEDQVOyfETkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=L1da9MB40NaYESmfhU2M1KO_qWjK-IKgSJUMrlpfQp-OxJXg8HSuIVlfHUNR2aA6AA2LYMAFSWJ8SBHCrf1tqhYTCiveLR3bl4PvkKYMjrSB8jNsnI2heRvTloUSzDCImAZzNAYuMxGda9scZPI-pvlaB9m8Zo8PffImnZuDHsPYk25sDunKplpGcfw3beKGt7xo29gdhWTPx6YUJY5mlT63ruUrwFRAo1HVSYJsBr5chi3vP9hiXEgE7hE8WFIlmXXLb0Rr0cMlkZcVDhrizJShwctpFUaq1dGGzVAkuOdKBwJEV5gm1iypTiW0T6x6V_M7iiD6aiQMXVzrTRSIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=L1da9MB40NaYESmfhU2M1KO_qWjK-IKgSJUMrlpfQp-OxJXg8HSuIVlfHUNR2aA6AA2LYMAFSWJ8SBHCrf1tqhYTCiveLR3bl4PvkKYMjrSB8jNsnI2heRvTloUSzDCImAZzNAYuMxGda9scZPI-pvlaB9m8Zo8PffImnZuDHsPYk25sDunKplpGcfw3beKGt7xo29gdhWTPx6YUJY5mlT63ruUrwFRAo1HVSYJsBr5chi3vP9hiXEgE7hE8WFIlmXXLb0Rr0cMlkZcVDhrizJShwctpFUaq1dGGzVAkuOdKBwJEV5gm1iypTiW0T6x6V_M7iiD6aiQMXVzrTRSIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=RFcsTehrUANr3HkzYfBlTiFnjGZz3rR1G1F-GOXkrYICjvu-IlzBMqW2jiKq-S7MStAyhktX2iZGPlI5vizPc0JgiFjA4rG04nXPnBbv5GP0dxc5UrjqAbbyjfJcuiq0w--1tCd-PgZcKNhfecwcMiCuCtzO5FEzkLfhui2lBEiXsgvE0y82eld4W0rjr8iSj7yB_0qUxiNPyoH3AvQLPQ1QGsYzYbdQLwbxMS7JeI9dJYK7b_4syAXrM2OGtBYZiVbOUW2fH5R4aCooQKs1oQozoXpIphsyjWVVnbT6ul228_J6DSa8sMO9A0C2dMvKNFXFhToxuXIIU1tr53HDSzFwoLzXyjp-wqnfIVKdj3QYPR_VWS1a1Eea4LhPlfGKZvq21ESNSgJMWezsbRZCWig0sMvQPnsK64nIPnQ0AfY_UyjfjQbYlgRqUeYz1dEeRY4ewlVGGg42XRwbrAeDknrf0oA67XAZ6WjXYjj26AfD2r1TVJ7g7G2TWzQG3Mp4_CRO9-IWXzpIxJZEAMS2jcgpE1tcZAWkEiUuvRBqmXXVf41pfjxrg9HqBJWiNpU_1j5c2qKAc9xPPWFi7tCTWtQokFlPqFaIyfOYute8LF9kYoEheJlBvUS9ENTArz1uHdr-8BHKJK5nHUKN_qdBkyHY124ThEEl-O08Bshr0NI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=RFcsTehrUANr3HkzYfBlTiFnjGZz3rR1G1F-GOXkrYICjvu-IlzBMqW2jiKq-S7MStAyhktX2iZGPlI5vizPc0JgiFjA4rG04nXPnBbv5GP0dxc5UrjqAbbyjfJcuiq0w--1tCd-PgZcKNhfecwcMiCuCtzO5FEzkLfhui2lBEiXsgvE0y82eld4W0rjr8iSj7yB_0qUxiNPyoH3AvQLPQ1QGsYzYbdQLwbxMS7JeI9dJYK7b_4syAXrM2OGtBYZiVbOUW2fH5R4aCooQKs1oQozoXpIphsyjWVVnbT6ul228_J6DSa8sMO9A0C2dMvKNFXFhToxuXIIU1tr53HDSzFwoLzXyjp-wqnfIVKdj3QYPR_VWS1a1Eea4LhPlfGKZvq21ESNSgJMWezsbRZCWig0sMvQPnsK64nIPnQ0AfY_UyjfjQbYlgRqUeYz1dEeRY4ewlVGGg42XRwbrAeDknrf0oA67XAZ6WjXYjj26AfD2r1TVJ7g7G2TWzQG3Mp4_CRO9-IWXzpIxJZEAMS2jcgpE1tcZAWkEiUuvRBqmXXVf41pfjxrg9HqBJWiNpU_1j5c2qKAc9xPPWFi7tCTWtQokFlPqFaIyfOYute8LF9kYoEheJlBvUS9ENTArz1uHdr-8BHKJK5nHUKN_qdBkyHY124ThEEl-O08Bshr0NI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwV5Ve3b2ew7D1RH6SM26ktlFA7sB3JOTJGA5dGGjTP2r2SYRfr-ijOiXpPnB5mPXfqYhmcIsu2wqxiZn5Oh5MTl7BpOnku4gXqRKDywcZfZx4ECzDlCSxdQg8VzUSz_ravzhxBNh8ZLshKsYec34IbDbIzZbGxty_kzDsrQE4V79pcWZo60eHDeofUWOkJJw0_81m-HUCTRa3zzdAvVqvIebFb2O9sfO5wduUsFNVqunqpTsCegIL4u6qPkpQLj7XKXSAAAmUu929nLoxVHZjmxRQTPhkAbf_BfMD2b1B7Oa3lQr8CJ9pvNAmPJLu5YxufY7HNoJSJmPVtUteNbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA1VRRx7e7yln1zfacuLRKpnR4MTWwxuZy3tYpIZo1fsjkYq08wZhemv1tEdbTGliqXLP2KoFHzd-hoZCnr9hE15XlMXbVD9YT8BuV861kA7wHdB4JL_6_IBRG9eSqqAC_zsNxvmgx0L-8sN1MTofI4L9IE9D8pe3e574KbCTFt1FCVshiRNh--5vplwPyTjpvSmJ7pslUGEkw3smelVy1TjU8XEbW7qnwPdC8FsV-dA3lw5VJBBnT78sL-tyNj1A5COXEa63s_O0HI6e2DVHwFZT0CdSxgQnApro2g-GpbWqZ9C9KY3iU6yyuEcZsQ-H0Obbx6FCHggc_oMphc3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETnNOhVALso0Psev8p7oow_kgI56BRRTuigEk8E1Fs5glcNuds7ss5_3jZNWMcyofB3PIvm4tAsDP6BjYgEe9ck1IKp_6n6xWgPmLDhjrW5q-zuEMZkRoDfTbwD_ec708ukhqaLyKpaxa5PyylEKCOpF2UZ_RaYjtP7kBS13suXQKrA5_3iicU_htpM33ZMpPvLSPqe3NvWMArK9__fg2-TRu0C4ag2ZoabEU5qGbcSwn5r_UjW4AKHv8_cmeP-rXJQClW1AO2V42AHOIycZeC8fJ0jRQMdv_anS5LCsLJwLkusD4tMvyMK-JlRi3-edT2jh-Ctjf7WalEqhqOqRQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=hsem0qp9TetkJGGpKbccAluPAy71TjmOP4R44ynVvWDmHGkGFA1nLCL8wK_qNBYLSQIUNKodRpNNREIjJDguIafrFXJGA2--rqhkZBfim8BN9hUqKcjJw87n_sXcCxW1sUMkQzyAAYGNcoWBoJDIAA5AkPKDxvy6M2u3m9nthKmNw931bmAh3X-BCPMII3TzllF9lZJxwoA9wNhnqwtbamzlLiupgGPj8eP-X8VbmFAvv-jVTpSLEqnlB-O_ZPOEqFKyYkge886BkaomzzF4mfvy4G_ATlohEN0LcNk0g5kJJYj3fqDE9SSTjjF9477p2LwFYY3MntTTJuMwWaKdHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=hsem0qp9TetkJGGpKbccAluPAy71TjmOP4R44ynVvWDmHGkGFA1nLCL8wK_qNBYLSQIUNKodRpNNREIjJDguIafrFXJGA2--rqhkZBfim8BN9hUqKcjJw87n_sXcCxW1sUMkQzyAAYGNcoWBoJDIAA5AkPKDxvy6M2u3m9nthKmNw931bmAh3X-BCPMII3TzllF9lZJxwoA9wNhnqwtbamzlLiupgGPj8eP-X8VbmFAvv-jVTpSLEqnlB-O_ZPOEqFKyYkge886BkaomzzF4mfvy4G_ATlohEN0LcNk0g5kJJYj3fqDE9SSTjjF9477p2LwFYY3MntTTJuMwWaKdHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoEUkIsVtGK9icK3tM0z04apIVHYxLn1ApuS0SskbknzWK4EcjQle_kwKZ8I9nBxXPdDk1nZOxKBSv6dKYGwELOk_DBsqs8a2Th38KsaQKsP7y9TmQI-w1cPF_m_SClUUFWvO0SkjjlzgPI-VFyanSwzeJcXlpYCyEnVTWLjWCitMIqYHo8j7cM8-i51bW3kf6BBnv-Nn5HIj9F85UR6bLJRCxNSU8bPbatrk6f-gTDm3kQsy7awamtNWYrRtS8D6mA8yyp1fRiQ6TPi5JdiyQlra5SHqxvaAAe4pezNo5tUIkwxnNUbN1VVXa_UMuuNTJAtwpMJ92j7oT7UmTvajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=apFGpEZkN1hJpFC3TMShHm_bnFO4ZH-PfX_KbE-BLNgyoGqpq9WE9yB2EHZ6K_ApjEht4nBGWXKy99EdC0cnJkzxSmgcuK1OZpTvehMhIWTz7mN-1Iidi4GNh6PBZJAmnTErqko-G5FoQNCRUg2D6-cWez06Y03dDAVRGnCkLPBKsKQ_oT5hQZUB8OwlI45nwSae-JxS8tXKKEKnCM8ygQ0pEf68MrjGnIAFw5BpAV-4UFEAO3FYKB-ZcWWGGqrzHvdJLcJAz74IHOD-dbufiAg2KQuaQMDihO3RV5drn-sk1DuYIp6kVXWpKCLbnGUFjJpQDIO8GB2zNPwRtkFCwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=apFGpEZkN1hJpFC3TMShHm_bnFO4ZH-PfX_KbE-BLNgyoGqpq9WE9yB2EHZ6K_ApjEht4nBGWXKy99EdC0cnJkzxSmgcuK1OZpTvehMhIWTz7mN-1Iidi4GNh6PBZJAmnTErqko-G5FoQNCRUg2D6-cWez06Y03dDAVRGnCkLPBKsKQ_oT5hQZUB8OwlI45nwSae-JxS8tXKKEKnCM8ygQ0pEf68MrjGnIAFw5BpAV-4UFEAO3FYKB-ZcWWGGqrzHvdJLcJAz74IHOD-dbufiAg2KQuaQMDihO3RV5drn-sk1DuYIp6kVXWpKCLbnGUFjJpQDIO8GB2zNPwRtkFCwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=Kf9Y3om4Uv8I3nWzMe_OxR7TiajG_yJTs2SYLP__FHBOtDuvAZaHKPbT-r0J__tnZ78wwOH7qRCNtvu0ccaQJe-QI3OR65sEa2s49oEVV7Nj-LRB4OXox61nvQz8QtMelw5xGjCIKdpbO5pI4wRH6953xx-S1di8l37Et3rdtvcpK_xRKoSokkQ3TB4zQOdTyxsxvq6HJrUH2deS31mOQXtidIu2Vy1KOqSnH1mNR9QgKfdRLUZRrLgDOYL94V8PnxRFJyGssxwJ1swVEkdCHoTy1qcaCI9VNO0ovc04nv4CEh6tdlAS84bgIC1u0mSiB9zas82v22sqLUTyqAqInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=Kf9Y3om4Uv8I3nWzMe_OxR7TiajG_yJTs2SYLP__FHBOtDuvAZaHKPbT-r0J__tnZ78wwOH7qRCNtvu0ccaQJe-QI3OR65sEa2s49oEVV7Nj-LRB4OXox61nvQz8QtMelw5xGjCIKdpbO5pI4wRH6953xx-S1di8l37Et3rdtvcpK_xRKoSokkQ3TB4zQOdTyxsxvq6HJrUH2deS31mOQXtidIu2Vy1KOqSnH1mNR9QgKfdRLUZRrLgDOYL94V8PnxRFJyGssxwJ1swVEkdCHoTy1qcaCI9VNO0ovc04nv4CEh6tdlAS84bgIC1u0mSiB9zas82v22sqLUTyqAqInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=rkA31RjRg-yEPhKmSe9Oyd-YTJsGuI8AlY3qpEYjTc2xImLKzXTKMNeFXKq8eyqkHT0q115TVuAmpJBSozlndx3TnCKj6v6JYGAxgiOIzWIQWJTYtLOiXuRnVbV_j5Z-zdWIMfwN8lPcQ3x2nHvWHu5iL4nf-Otwz10az52GToBmjju9a-N-yuywTuPMcHa5nD-GFUhUrs-rZGHNNAPojOuXZ1lCAor9xQYwF9dkwkWeFfg0mp53Ad1CnlAYyt1ZpHo8nMzN4Z1PuJc7OCG0lugX2QEuYphbZGFoQrdNF6k1OAKt55YN4oVtxgkdf6Qq9RCiG95-WvUvdZRaOpapjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=rkA31RjRg-yEPhKmSe9Oyd-YTJsGuI8AlY3qpEYjTc2xImLKzXTKMNeFXKq8eyqkHT0q115TVuAmpJBSozlndx3TnCKj6v6JYGAxgiOIzWIQWJTYtLOiXuRnVbV_j5Z-zdWIMfwN8lPcQ3x2nHvWHu5iL4nf-Otwz10az52GToBmjju9a-N-yuywTuPMcHa5nD-GFUhUrs-rZGHNNAPojOuXZ1lCAor9xQYwF9dkwkWeFfg0mp53Ad1CnlAYyt1ZpHo8nMzN4Z1PuJc7OCG0lugX2QEuYphbZGFoQrdNF6k1OAKt55YN4oVtxgkdf6Qq9RCiG95-WvUvdZRaOpapjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdBg16aKM0u-rUOYK3pkNNPox1TkWMkb6KuiQR6n3buvyVNRa3_tTMWT3uIdA8Ddh42ap_cbQGLhht01ufjcDC2MzfVOVI0PNha8GSi50ydE753o8tfWOZl4Yt4tEN-3XPIEYF6JrcM4vPHhPN3TLl-qjdoSikrp8luSOhme6XPhZ6-MSLIRBiaHAaLl8WOH5f-Ntb1_73SEAcU6tfu_6CgCeksVsOpatmQe0j4HsYBB2FfWP4B2Chtn88kXfbC1r5BKBJ_p4AasljdzqStV1sUDUj0R9xgKyxG7NTL0G34EQFJUCuuPhM73VTYk6KnRCoxqo0-OsKCeuMZ8UT9s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=fTRpJRsplGF4SoUrtWXnhUoRchNpcyPnF0fbbqhfuNYdVH9dLZ9i9mXkpzZ4V7O0RFKIY1hep2du-bPbD3WRVsoqaXu23v-CMks58k51v1YrCOefSrMle9Cmnj9UhUSCyClst6aFHw4-G1wsMzmaFKWVAuOytDdg3A1X0Ysp2TNdikPqHo9f6xHi707kRkhxKFio_Ys4cSRR4rx18wImiIF18L3kyGNAj5tHJ4f_yWZAzBMiCnvO_uDQRrPdcGBma5_PwZo6vpI1cYz--6Si6-RgwAFpMe2bnZucKYFXMvjkORBlrHZa1QehDydGuDpC-SGBwIWIlQpYcgDU1DS57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=fTRpJRsplGF4SoUrtWXnhUoRchNpcyPnF0fbbqhfuNYdVH9dLZ9i9mXkpzZ4V7O0RFKIY1hep2du-bPbD3WRVsoqaXu23v-CMks58k51v1YrCOefSrMle9Cmnj9UhUSCyClst6aFHw4-G1wsMzmaFKWVAuOytDdg3A1X0Ysp2TNdikPqHo9f6xHi707kRkhxKFio_Ys4cSRR4rx18wImiIF18L3kyGNAj5tHJ4f_yWZAzBMiCnvO_uDQRrPdcGBma5_PwZo6vpI1cYz--6Si6-RgwAFpMe2bnZucKYFXMvjkORBlrHZa1QehDydGuDpC-SGBwIWIlQpYcgDU1DS57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRnT781Q7gEOCokqsTutr1EWG92zNC3NZhWJeVrha57s-TZjI95TTPFb-Iufog2E5849b0t1Z9VAarKJpoSvS8Xeistu3CV-okE6HW78oyvhPqSTYD34XctvZ-A_euRd9w0hrCxfOVkpPP-Kqk5InOi21wB8u23vcyjGecFLJ-lMWNNnt9ijPnvPLoExifzhyJG7AxiM3jALxZc1juMS-twVhsTYKLKvMOm8AiwG6ycKlJcf9IZlV29Bf7vk1CZMOrX7WsI-GR3j9YqoJVCsqUiubhhhhqC310ip8KoCKgoMA2U4yEqqktKaqB1h1xZNx5o0_qtPAs5afUWLz_ZS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=mPhoaNbLx1VipLjX2uE-diicfjHifB4AwCq0JCCirO6VThQ8DuMIGGc6vuj7CJAfdH9OufVnIEQHH3RbP-bzq6yW3GiSrEMfUSA0ptVb9obzyR_rvJCUL4PqusNVkkgRuJXWsFgGOiEZzBEDBLvf3mCEapqd-2kz_vCquQoz8cqKFtgIoTKPJBf8lRguCftUujSWhab_WZE37-EJQH_NzocHIhgL1Fj6My_Hq5RSu4pY37Gz1HY0kzMxLphqAJssEWBkqtkG3a1einZV5H1PAlLmcioj-pFxfwQL7l4DqIk7Av_vIIbRj8e5U7pRR_2XAr5VQbJ9yGlqUjhi9ZB7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=mPhoaNbLx1VipLjX2uE-diicfjHifB4AwCq0JCCirO6VThQ8DuMIGGc6vuj7CJAfdH9OufVnIEQHH3RbP-bzq6yW3GiSrEMfUSA0ptVb9obzyR_rvJCUL4PqusNVkkgRuJXWsFgGOiEZzBEDBLvf3mCEapqd-2kz_vCquQoz8cqKFtgIoTKPJBf8lRguCftUujSWhab_WZE37-EJQH_NzocHIhgL1Fj6My_Hq5RSu4pY37Gz1HY0kzMxLphqAJssEWBkqtkG3a1einZV5H1PAlLmcioj-pFxfwQL7l4DqIk7Av_vIIbRj8e5U7pRR_2XAr5VQbJ9yGlqUjhi9ZB7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxMv1zkkd6R1Xa_T48nbtT0MkttNOG2nh51RIkIoaukutTUzgXigH4_KBR5Vzk6OayZghihgI8Tkn_gSPQujVd91V50YFy52DSts880jhcUPjGXmGjac6XLdu02S-7DOclqyy5pAmBCdPYI_O5fbz6MkyMHrjdC7fq8h28GY3Kpt48j0a5JhUnPErT2ldNGs7cb2DlYrk3mVRuaI__Th668WKjSRDhQL3R1AykALtfZhxH4RW8OxtsjUI_XgrPtvgfkEKP1BWVTNL6CgfnvO0ppQQ57rfQ1nR5Mrow3e026TFUy_EugRqhft5nGyXWkZeAjvWQ1efWcY1G496g3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
