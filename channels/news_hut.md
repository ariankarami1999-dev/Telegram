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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txE5BLGY47fqy4AdX46zKMrx8hN7TiTCWmMXUBZwcI5n-Lp9lld0B6sue7D1K3S10gSYwaQj1XpnCQieJDM6k0hmbA7U1X32HnPPwprlx7bdxW44ntKa4HyHn0PseUKSZSSiUIPzLWglTHvwMKe020kLhiKbymTrD6WsBVysiFODAj4zh5U0iwT3WNyzeBUVALPFIyswQVLYlOa7LdZsdtJak25WTlLBDVMPetNomVse1OtVGQLhPQDtFI9yWpjApLzqXP_mUCMciyFOC8QqeCz8-uNaRB9E0PXrxOJdryYecgo_xy_vV37k9pa8LVKKqpoIUs4m6yiVXbfaVxr5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93ZWito6W-WrsHfqGSvISSUuH7WJniT8ebdG-FuV-jHeAvzNrFSd0OhhwHtu2f7t9cMm9eVq3eRtnH1eEnTNQFKm4YJXExdv3HSlvhcNWlG65pqLfs1UGPI5hCUb_5alcaR671OpUBUJtUl8CsfPxoIPctM1t_3oJRInfIF-NqCRsH9Ib6d3TwSg0U5zskPSkFG4ifBSukdRyTEYMYOHLx4zIhBfVLo_oItRl9lpUgvKKUaZteIPyd4vVEg5z_5U60iWaXsbgsC1ST5Hr9sPzM1MVwt-rbN2eQQiGWRD0ZfHFnp3ysbqtJmLDaNF9XDjtynuUwX7Z_gCPg2NevsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCDizrkm7F0QVQGygRuz8lDk3HO_q0O9LdnTwIcdRvn7VmIIcCuKkjkoRPi8wSJEW4i8BSlcs_Eeb7fdOpLJWzgKPF30bIRHG0f4MKBAB_3SmalopIdKLqUKY_dCvhpVJvv6PmzH2t4DMC7f1DUwaynmNM7E8apSNcN_oUa56Dy6PBRsu53_Mfu91X2OrWwIXOS7X9A1fl5BlZspgUMq8VhZnqYY319HPJzKhnp77Orz5e7ORcwdLfoaOa-0htLJ70uzE9XVVP8GyOWEoCjIF-8M2VDT3AkLenUEnEsvr2Xo5nybgx8cIFR6f1vXNRzfY4jcscyoD5dlXZYAOQv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4wbAa83lLhsIAAQn-xuFxHMUi_UXjagHNMTYQfAVKJHtyu3Nv9jYPek1UM75eXD-zKh0LDA5HKOBbeKsqcXf20kP-QR3yzHNPeObQFunRSoj8RccV8_CYFvFqpLSxxUqWCl4JULUbqCSct96op23GvDkYCfRtA68ud9oiwIHSOq9mLAqqXc608b-gqNvM_VNty---NdHaNRLbpmFY__TaPYQtd6fl6YmJJa3sR1ha8Y6waxMMmeo80FsuMc6N8Fs1dFsIt9X8Zowz5mtNABzb7Drr4yTJygXb_R_0fIFixwSLJGL4-dlftHfbwwIi75u3P_NMGKBCPNOhiq20qI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOwvyS11wCVx61uBoi2kGB8_RlYuPCGma82SbCOlndw7uTHecLiUJIzXyLu4Web352qrxuUILMtyFt8sUvEdaDgU9Eq7hBR-7GNLZ82ABtJ62VWcNiQuKHaliWB4550eoV71k4jPBZOxLvbdFyZFvdFG0sHj3pDa2ZMYTLWF3orqVwfPC7t7kT8gCZbaLJ0KQOvtNnXk3W9SFFnVzrg42Qp8AVhEQbw8JVEFUbmXY1wKdKExYSWyNR-eG8SeHMGEqACbPZ9kdUOJoDZxgUZH6P__FE0IOxKFF3cEGXYxqPVSBGSvRhp5_tYtZfZLwJA1h0Y8tTdxfCxcq4ZrjomJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcNO7-RcT_5gBfObeXYIizj-LQAZarPu2z2NHIqgk-xfUQqxroIu6vjyue8XGEkahk4Tls-OOlZGDdBNjPPFCKUVphEEw56N63x8Kax31ANNy1nlimy7OTUwVmI2v4_PWn7FpDgcb6HvyHrUBXn9ks5GAl9VLGa8jEX9Ych6NPzrJSCJtU0nxzvABV-iCmEmD4zILCWf4Cm4LKggjEtt6UIXqiD1JO37QRbzA5yznTe1E-CSJ4nKTlzthhiTx6EYZConQmMmcfipStP5XhKIg_HyOp3O78N31LkndI_bRHfpqtK6t7NZ0cBSFBoQ7b4d9W5VrHSoTxWESBzF8bHozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmH4owHbFWD-M--BsWZVZoCZi58iB-XI5VRlTvAudeduMx7EjD-mTHtz3FGCL2Wo0PDmDbOAlksjtEhu2O0jev_RVjF8YTWnMgg60OCTV6pYvVm1lWpHPMpmIXab5z8tHkjexdrpKrcuRg5dQqNGw6lIwTEgV_wAULWQuDvVoQRyY0eQ93n5bTVcF0F7H-GT1vR_fF-MRxjBBUvScsAnaDz1RFK9Py90p_XM-cV5oAvtTz82-bu3MRd6Uoa3tA89MAs2F4cx1pxYA2ORg1_JYO5w-lvKQci1wkvhGWYn3NqBYjzulFSLaZvge9OMh1O0Fl4UHh8ym4IQ0bxgoRes9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uV8qJ3gtkDjSyxzPLRHWyCLFiq_5btw1Y1o5hzo3dVa5YaHqKa9ucpXmHDsXeabM8pBglpYctOHIg1rebqtmdxC-CLK-nS95SCm7Mx086Mrf2fqRP0HM15qo_c6UYpYAvYbi46-ru1ij4FOecZub6XUEtjsS-zMJAePq_gc3sMNSu7Qh8FeX_f05W50Jb4z2kjJ3hbfV8Mia_tGs8DfUNojHv1nkiaNhozcf_lYFQJstNgDOfPhF6ObAJE72ZxlSbiZ0nl3uJDHLrkwCwqH6MMgipaA1KQ2JGMePICWO_sxP7gzU4FRrt1SqV56LAXSmgjmhJzPBqq8FHFhSycNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k50X6ibtUa4Dwv3WyoH2WzJ-Y3XiW86yg7d8nZLflEiQPVNYoAc1yvKRUIb9l9JVPKWLgzbeODIIoS2cQif6lqeI7JyU-BVa242O_IBxvWaUzIHyKwCRavS2mDPlQutHII_0AYnBljrP3zBciO163CWaoIcQwxlaqGYsrh0h68blCO1_KR5lJ6tt1EJKRPd7HZK5N7DtEsH1Jlh35qqjrA0Yu3PGK3-NyODqZOctSOO1-pV2__RVj9TjsdNVcutcEnuJhZ23p_LpMfoSa1UoGfnPBYadjeS4Fo73i0CVQWydqDLUzVzE_IGHUuY1FDXCpPyAkhA-Y9pkxDeApNIRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmXCov9cKRlHXJSS6bMaO2WpSjpmuIOUCF-FSgZwAKzrD2FNsgH2VSTZ_JZLs3ZlPKMquMj2cTmvlweInALJmvtYn5g3JXuqNwaYhIAxH80RFqsqYiQKA4xsBa9IAu7DcbGmFfhTbk0g_nuZ5I_cezwlId7TJgCqbmwilZvoiKKFqibNg8EN8kVYztcRzfopyV5JnoQS9olQTl29g0JAvavm2-lOrg1SNNXQpgx0hQZCqnAq0GkCANoHOP4oFnpSQn8lMvEPsNCwGXoL4SogI4ykTB8jXX1HPacIKKOPxh6zTx1YnyZc2wG_KlJEmOmLOvhmIix9rYNrkPqrGk0FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMeFBfFHSrzLU17uxxVcAfD3PtJyWKK2vEg_yv8hMFmbfku2R-IbCY_40-fJgnQh_c-TgLAC9lQS1Qx4ztpj8pGMoNt9XuTXv6EN2oaNxbQSoERIRJzHnCZZkCwv0fzmD42C6dqlpdsBvJG0aHxdBYn1tuH6HHviDXWtDCiVHt39hLU1pt2TFI-yEdomgYhv555deUl9qbMNufkfbtydnWPBB55gtleQCrn1eIyeTErGiXolMB3gMDOrbSeId3FsFiVaaHMf5I9YdZrjcLGIvtLYBBasr0NC-VO6tGKNVrjhcTd-fAW7kzNaidnL4dmyYvUSTzNpbghxutm1fK0wLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te-SFGt8MYzOKl4dW0N9DDyMNKriPlfPlUeLklsLWoRiFt97ZLRBdLgUF7-KLRLmD7VUwsEZaDV4LP-d8VD5P4sLG6Q8BWQtjAZvOR7aMbZ5AZGALDEw_09PMVYiWc-GqaqRh4WZzWwP6acZkDoKGjtx_LV51xM8qA8Ec73XBT5W_gJFwXxy0XL0yk54le2AgvaJeyh7-XP-vlamKJ0dbfY8a3hPpcnLKDWUKYpYYvbIh_L2504ApB1GCUIiwP9bcTd_uFFKIEDF8ltJyGvx4Ur8VJ6IZHz8s9GsxJ1n6CG3Pmp6T4hCR4C7Y0W0EuE5bMlWjpDyMJKMsfh8NT9L3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Pj4CbHggnPP_3BvCQl3kZT6pDRgQWDsbZLlBRCrXxDP2pQo34gwhPPokBvk_7NyfyK90CwiqFdYv37XdAB507kROzqaBwMZAqM1duY81QtkWxgyeP7fi530dE4aVzB1h_5EEtjDBvcgFHseK7Q9Vxtcaq-34cmTymRPT9qCKf1IIJ0eEqFTE1_KwiBsnopRJujPrzvB35SqCwDFrNi9N0bkdP1nU5tRlziU4znCZzfZ1mptd4anJiHMaX3ji61he0UzMTuxjNQ2ljB3oDH-yfHnjh3U6vwrgym4VFUVOFTGSLwyRDkjMY5hzlXI4W5NY_yWVX6OJM0TpslTVLnsaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Pj4CbHggnPP_3BvCQl3kZT6pDRgQWDsbZLlBRCrXxDP2pQo34gwhPPokBvk_7NyfyK90CwiqFdYv37XdAB507kROzqaBwMZAqM1duY81QtkWxgyeP7fi530dE4aVzB1h_5EEtjDBvcgFHseK7Q9Vxtcaq-34cmTymRPT9qCKf1IIJ0eEqFTE1_KwiBsnopRJujPrzvB35SqCwDFrNi9N0bkdP1nU5tRlziU4znCZzfZ1mptd4anJiHMaX3ji61he0UzMTuxjNQ2ljB3oDH-yfHnjh3U6vwrgym4VFUVOFTGSLwyRDkjMY5hzlXI4W5NY_yWVX6OJM0TpslTVLnsaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=e7DF627GdCEm7E2sc8pjBxuCJsJ4lJMBy4a3es8EZkGgabRc8DHurd9310mNUeWNVxBJHDjUidGDOsNiGL6SO1qmBcI_aA-IKtvRpSMIQkFZfsL8bTs923Z1J--WRNZjg5lxUhIgk3he1YtAQyPOUDZQxfBOjEMPIQASOhaPC-z8BYeuDyNKh3JmAs4bGAqIuiZfB43MAqi4cZ4qlqmwKFoz0ybHHhwUtMkyL5sHCml-jP7dmuJDTp2ArznDpdpsi0Q-7LiDiJ9z8nisnRKGaVn1BuhHhGww34AZcUqdGU8CQUn3jqEF4gLfYPSxHfj_1qGkmqATWtmn8XKFY6XI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=e7DF627GdCEm7E2sc8pjBxuCJsJ4lJMBy4a3es8EZkGgabRc8DHurd9310mNUeWNVxBJHDjUidGDOsNiGL6SO1qmBcI_aA-IKtvRpSMIQkFZfsL8bTs923Z1J--WRNZjg5lxUhIgk3he1YtAQyPOUDZQxfBOjEMPIQASOhaPC-z8BYeuDyNKh3JmAs4bGAqIuiZfB43MAqi4cZ4qlqmwKFoz0ybHHhwUtMkyL5sHCml-jP7dmuJDTp2ArznDpdpsi0Q-7LiDiJ9z8nisnRKGaVn1BuhHhGww34AZcUqdGU8CQUn3jqEF4gLfYPSxHfj_1qGkmqATWtmn8XKFY6XI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=t-qWSsUJtC8vGuZHV90XVd3P7ZuRHB3XmcBhK18m-kpmwivkpeYU87NwQ9Rmsx8Q2kfiSpX413YY4MVk0rGbZ_quTHMioeGBxmIbETd7jSSUNKu3yQMbqEezj9zhjvHD8rC7Qr3iTfcujYRfMLKx5M-8yFc2aaaAL4tA-j05FZT50IYscp5rhOxyniahVu4kfXEv40LzTtM5s-Q-S4egGv5sFLnblFS6LMb0hDvWCZxnNf2_v1hucmlYqVKVILajoKrA7hteTvDWm_OkQA0X7qFu1MH1M78dslnY5IlwpZYstiiOO1AoLJEoCExjAgLyrE1gc6_P75eGMvq-HVlYFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=t-qWSsUJtC8vGuZHV90XVd3P7ZuRHB3XmcBhK18m-kpmwivkpeYU87NwQ9Rmsx8Q2kfiSpX413YY4MVk0rGbZ_quTHMioeGBxmIbETd7jSSUNKu3yQMbqEezj9zhjvHD8rC7Qr3iTfcujYRfMLKx5M-8yFc2aaaAL4tA-j05FZT50IYscp5rhOxyniahVu4kfXEv40LzTtM5s-Q-S4egGv5sFLnblFS6LMb0hDvWCZxnNf2_v1hucmlYqVKVILajoKrA7hteTvDWm_OkQA0X7qFu1MH1M78dslnY5IlwpZYstiiOO1AoLJEoCExjAgLyrE1gc6_P75eGMvq-HVlYFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=l7Is1It0axpbgA338X3WcJys3uPnIoNLy8FXI01c5zCCvJ0Tp8Lcv7xGi99-mZ2ttN6JsyV-VCnzZy2sv907f2bEtnE3ZZKgddl0QqW00xaqFqJAwPcozqiCn6oTsRkJj2vfZYEVt4vUo31dDb4XUOphvoHnruWyrqmWrqUSX5RLgm_tz__xu5BUkEQbzehJP8XWnBCss5793ocXaMomxtOA8UwEMHBtIVri56CBwu2G9bbEWGyMJrByO9HhF554dNm93gE3BbR_GDsjSiL8qo4P_sgie99WRsClu-jHcZfofbiFvn1VdIOvAi29_z1GuL7jx7o1ris2dRvOgIAmGZvuhQt4G2sQRcdl3SMJVcijpE0iJKshHS-9Fl_9ec6hL1i8PeW34y5ib-u3FuGuNFKtd4krFS0M0XFwTgSsb6qxMt3f-WAtRC-mgSeIt9isIY7O6Aa5Ak1lI9CyZ50eTc7qFUyfcgnBLnEu3M1XWvmsvjlS4Q7vIGoY8uhv4Hz6J9ipZnSpgAaacaqk4v-pcvSCUDHCYT6eKNgucggXbJTw1dvR9LgFf2TCcYQXSLKLlLVx6XJ0YmtX7Jab5uB7xFk2I0Xa_q65cfUJjIeBgvJjYnPPgHP-RdpXI75DC5v7-r8IvXjmzDvQ59l_7qX70uGlvxSHS-bg1vnBLr_Ctrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=l7Is1It0axpbgA338X3WcJys3uPnIoNLy8FXI01c5zCCvJ0Tp8Lcv7xGi99-mZ2ttN6JsyV-VCnzZy2sv907f2bEtnE3ZZKgddl0QqW00xaqFqJAwPcozqiCn6oTsRkJj2vfZYEVt4vUo31dDb4XUOphvoHnruWyrqmWrqUSX5RLgm_tz__xu5BUkEQbzehJP8XWnBCss5793ocXaMomxtOA8UwEMHBtIVri56CBwu2G9bbEWGyMJrByO9HhF554dNm93gE3BbR_GDsjSiL8qo4P_sgie99WRsClu-jHcZfofbiFvn1VdIOvAi29_z1GuL7jx7o1ris2dRvOgIAmGZvuhQt4G2sQRcdl3SMJVcijpE0iJKshHS-9Fl_9ec6hL1i8PeW34y5ib-u3FuGuNFKtd4krFS0M0XFwTgSsb6qxMt3f-WAtRC-mgSeIt9isIY7O6Aa5Ak1lI9CyZ50eTc7qFUyfcgnBLnEu3M1XWvmsvjlS4Q7vIGoY8uhv4Hz6J9ipZnSpgAaacaqk4v-pcvSCUDHCYT6eKNgucggXbJTw1dvR9LgFf2TCcYQXSLKLlLVx6XJ0YmtX7Jab5uB7xFk2I0Xa_q65cfUJjIeBgvJjYnPPgHP-RdpXI75DC5v7-r8IvXjmzDvQ59l_7qX70uGlvxSHS-bg1vnBLr_Ctrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=jKSdZXIBT1h5zitGiZSVHbPvjLVT2LauI5uFfj0sSUNhe3-OsKPJj-9UL3AOYC2UcVn94G5JEr8Zp_lnQpWc0v1tBB-aSk4J-_lQGKWkaR7VOFYEVvVxEIUPXduGsfU1eGR6RWqqBWGIMFzvg9_5gYCPeEk4aLNdSPBfTNy6KsUG0VU4Njkt-YGiDYgbSR7-k4bKe2KIYCBtoKN2V3lMsgRtx8nMdTqp6W5hnwrpSU6XNPPzlDSYWJU9LELqwP-wH9TBkkLI42ToV_H9mv2gfyIlmVoXU4MeVV8Sj1GPKS0FpgvI7SdR8QAiPD0rvz_NBNuaEp3sopT-2yNa0ZkC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=jKSdZXIBT1h5zitGiZSVHbPvjLVT2LauI5uFfj0sSUNhe3-OsKPJj-9UL3AOYC2UcVn94G5JEr8Zp_lnQpWc0v1tBB-aSk4J-_lQGKWkaR7VOFYEVvVxEIUPXduGsfU1eGR6RWqqBWGIMFzvg9_5gYCPeEk4aLNdSPBfTNy6KsUG0VU4Njkt-YGiDYgbSR7-k4bKe2KIYCBtoKN2V3lMsgRtx8nMdTqp6W5hnwrpSU6XNPPzlDSYWJU9LELqwP-wH9TBkkLI42ToV_H9mv2gfyIlmVoXU4MeVV8Sj1GPKS0FpgvI7SdR8QAiPD0rvz_NBNuaEp3sopT-2yNa0ZkC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7W3LAi43yHe5FM_3UzAXrNAWD-BM6yhAEl7LJjUZqYiTALrJaKubuqciiRkz9xbDnzgx_7qmakszYgeTkxesGvGEx-j7FqKkXr5RalaFeOc5izNycze0naaV4z73OZ8-I-Rw6LxL3Y96m_b-QsvOGCCi1KhcdiUmnweuH_qgskh4EeVFrJzxqAquY6XlxMe1w8ZQ6C6KaHYVKCXFKr8BBQlG_zEv0COnulTcqxVTSDUzZ2oWdm8JNyBPQfChdWow521EHfOoH9wXt5_oT-gOOVRbEAfSV_XUcSNFkx3Ymj9WgKygtyFAbDVQRCa-dHe0MOVPh66Ay2gVlkKsjn9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYRv5k1mal92-vPhhHgvqw1fqtBQxVo7I5UBNAhXTKDTD1w_HMU31l-Gfz-mHJ4kxS8tfmeIy2pFGCGguaaU--c0W-BMTUN6Q7K0RLs4zXQZpdOPrRnRQ5Tcj94azO_I4SNY-CmyXPZzIJAMNKYojwOz3sZ08Q4NKOzrpHh7K-OcEyFP2REN1cs90UNxY8_3M20-GHo0BgCyy1-hEayLZ4vGa6gBaZceH1psQlIwoQlgDiKhVyI3ZPfoqUtKMYK0DekXwyfk1nfDw_kwH0aCLFYuP6FoXlPvKwNcmJU_SHMp93bawWZOD8AcIEFh5gR5tbYXlHpCv6P1cZee_tvzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_WdqS54NqP_4EF7y53KHO7aFNt4Kj9ORjhxrkxXizNC1XEWVo2fjXMcQrgzqjaK-kiwjkP4Atg7u7_Qtx6lEnyGoXikiXpLil0SvK2dUM18Ps_jqURgZi9fc9_LasmyfSpOYkfsBvar9vBV-t3pEaJr4JRmVxyqwHxWkSN_mw2Mlkrx4asgcbZSqmFOQTuHPpVf2FswlUufRErFA9kwYB-ygTbnjBllehoOKrUUkJirSYjQvuOetcgOh6IxfSTKvmpe5WqmrG-GClX_AXB-w96AVjoSedIPJMXx2ORpLbs1g4ujNSspfpNwxXv23b0hKIzHSuGwUUunVVq1Nv40DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPlpAChVPEwVdiDtWJI2uqjKySQ7G0ORTBC3IYbxwdvxCEQ_GRncOCLbC6hL-ZZnuic5SWnt4KvznRkp58fvtfiKZv9mXtmsVqJP4odQnkvgUhBrE0dvXYp3z32hdCXW5Cjs3GxDqnt8UnBLFYw_aNlLuxDhaw-Yb6T3th3Bl7dVY8pELQwDld0x2uA95tdv3Px3vdMEktSJMuY-EWJFX8imDOnFqUxQTgfr_MM1SPjEzpN5PA6_-5PWvDI6tCnoXU7vVHOdIma2tUdAkgM-KlNbZ_jbDtjVYZ6jFJWSDcPrUEafhJONDNnJkA2Ju_UgRFwuSAPjikl9VfKVPeN9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=JsEuEKOMiRBJTL4eHCZlSqs5rqHsdqpCy6TKo_QVohxq3dHZAW9p5Mkx6uqwy-naMDWhqvgxWox5uoPgUMuowBoYTM7na87RTv0qEhr9jcclyV2oIqUxDq83vhxyiPArANVETWKhaBnoiUwwk9FevOUOWGIs3W4mEYN86Epgn9ZlvMILik8Mk5gq8qsAl5AkWQFR3toSM8cX_LUgT0xo-TSYuiWag5AjE3UatJjopVf4Ih1FkfYnyFLUILAEv85F1rqdVLeWbcm_39f9n77vxoAMMhsVU1oggvK1fjKWGaQMNqLK99l7CDgUYxEUr3r5QHSAoDbsItxWW6E4daMn0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=JsEuEKOMiRBJTL4eHCZlSqs5rqHsdqpCy6TKo_QVohxq3dHZAW9p5Mkx6uqwy-naMDWhqvgxWox5uoPgUMuowBoYTM7na87RTv0qEhr9jcclyV2oIqUxDq83vhxyiPArANVETWKhaBnoiUwwk9FevOUOWGIs3W4mEYN86Epgn9ZlvMILik8Mk5gq8qsAl5AkWQFR3toSM8cX_LUgT0xo-TSYuiWag5AjE3UatJjopVf4Ih1FkfYnyFLUILAEv85F1rqdVLeWbcm_39f9n77vxoAMMhsVU1oggvK1fjKWGaQMNqLK99l7CDgUYxEUr3r5QHSAoDbsItxWW6E4daMn0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvKU1gRyZfUnNu1sY-BkDGsBBN9oP_9bf-PfDzMV02as_iTke4G1-BnIp72o2YUT16JznH8kKcJNdP-Ok7KWnJi6dUk6ElmyRROx6es6TkGmVcKXD0nNQTSh1BnCJDGs2YIfV1drloCWsjbmnuWKUY5yDkayI0DG_svfC8YGpfMaTjOVwtiRsFUgmMzS7j6kFilEbqymmrciCh6zxjA8V-rWM9PZLWGuENk37ZLkuU5d_aG7i_gEox6D78OMRdqlMWTQJqN-uqG0MYE8t0FqFwhdhHxcLrKCglBLy-7zSxxZ42O2jV_SccV734YYknix627jOnFQkECiPFCI-ONNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=uFKtXtNWM9_pYk7bpX6-wppQ05ct-4Y_QQi3XrYKF6s4n3vYEKV5j49YwvIkp8aszOxzPATkpVMVilRvCziKL111Ujg95hQDDngd_FVc28fo24w7ScL7fFafeFAU_yUQxzevljCldJQe3OX7KEBKVO0AX0NObravrMjiExv0TWqWwDU6CMC4MQMa3lMy5UEvNEW19yIDletaFvXqsS7Bq4O4_hhorWH01Q5xa-F7hNzizHdFalM1F7Q4s6af-R9b--rKTAUcwsyaLpfYZaqMHmEOmxw0q_Z-fN6vWguwJN_GHAGtwqx9MwQ7QOy7H5WFCCQjiNqySwwKTLR3MbVHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=uFKtXtNWM9_pYk7bpX6-wppQ05ct-4Y_QQi3XrYKF6s4n3vYEKV5j49YwvIkp8aszOxzPATkpVMVilRvCziKL111Ujg95hQDDngd_FVc28fo24w7ScL7fFafeFAU_yUQxzevljCldJQe3OX7KEBKVO0AX0NObravrMjiExv0TWqWwDU6CMC4MQMa3lMy5UEvNEW19yIDletaFvXqsS7Bq4O4_hhorWH01Q5xa-F7hNzizHdFalM1F7Q4s6af-R9b--rKTAUcwsyaLpfYZaqMHmEOmxw0q_Z-fN6vWguwJN_GHAGtwqx9MwQ7QOy7H5WFCCQjiNqySwwKTLR3MbVHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=r9ziQaCB_e1oCQP-jIV3ZbSoOyS-X4C8U4CuodAguoyE4w-BJVH80V9HEKVgs6Ot9LOxD0Lnzrj7PJZ_Uq0KgrxXpp7DotaZ7YNMnXXTLj8RguhoOPPpen9yyEe8e1GE_py7uaAFm5zfIqRUlBMpqNCmm-IqHNKJtTgQ5SkWZjF01N-rRi_IqJpUfSLJAg66Js4RcHFsmCJLD5SgbgYM-cupOgff8BkTtaWz3qqdwtx5zxvx8TJs10I2cFZuVwzdWn4hz-YG_dN9AtkN0J3MjpFDebt_qw2ltCsUaIRYjebvaC-Wp6eINt_2fI_DWjPBKs8boHsAAyYhmxBz_5bJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=r9ziQaCB_e1oCQP-jIV3ZbSoOyS-X4C8U4CuodAguoyE4w-BJVH80V9HEKVgs6Ot9LOxD0Lnzrj7PJZ_Uq0KgrxXpp7DotaZ7YNMnXXTLj8RguhoOPPpen9yyEe8e1GE_py7uaAFm5zfIqRUlBMpqNCmm-IqHNKJtTgQ5SkWZjF01N-rRi_IqJpUfSLJAg66Js4RcHFsmCJLD5SgbgYM-cupOgff8BkTtaWz3qqdwtx5zxvx8TJs10I2cFZuVwzdWn4hz-YG_dN9AtkN0J3MjpFDebt_qw2ltCsUaIRYjebvaC-Wp6eINt_2fI_DWjPBKs8boHsAAyYhmxBz_5bJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=Ns-zSZfWAtbw2JJm3ALLE9xX_gMxxslBFgblsVXRyvvWu5esOFHYAXcjzGj_ot8x-qxyNY4_Oco-EpG-xhwVwvdXcs3B-S55yUFT1OEj0INt7k2m7wiVB-iJv0vqVMDxUbCSnnnaSWTj-OonRtYO_qJTF7Ba-XwWJ-faITiA9ovWX76XxnNVXUiHM2oepjrjrUmRkXy4iNDRqcBCaDsI6e5A5CRrAdKiemKLVFHXR73slmMmiBZ3Z2nc2Xm9Dnfy3-N2hpq_JTCWoovJTRNWSoiEVVFuwHbAlj4HQrFVUlaKoHHYo9onKoTNj-YZSRHw6qkqzFBxwy-sJ8bszAVweg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=Ns-zSZfWAtbw2JJm3ALLE9xX_gMxxslBFgblsVXRyvvWu5esOFHYAXcjzGj_ot8x-qxyNY4_Oco-EpG-xhwVwvdXcs3B-S55yUFT1OEj0INt7k2m7wiVB-iJv0vqVMDxUbCSnnnaSWTj-OonRtYO_qJTF7Ba-XwWJ-faITiA9ovWX76XxnNVXUiHM2oepjrjrUmRkXy4iNDRqcBCaDsI6e5A5CRrAdKiemKLVFHXR73slmMmiBZ3Z2nc2Xm9Dnfy3-N2hpq_JTCWoovJTRNWSoiEVVFuwHbAlj4HQrFVUlaKoHHYo9onKoTNj-YZSRHw6qkqzFBxwy-sJ8bszAVweg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=UAU468jQ6pcypMMNFmhgVZNdyb1JITB4YtL1AYrC85QU9arXbQdoQk5fujEVFcT4grhJWDYahfRxxgBRsZNunk5AYttUbNfXGq9wG4F1a4Jqa4AZGSBRRszvMjA8nYSYTBz0euZGQ2N-ApvVRR9Q9jaaeoSpnJostOl3ArsWX5NYe0gM6HEhp7OWLNj8V4QrPc6HiKGiGRUvP4yNKwkxk0ee_JSOvf7zoovB4Tf4sP0iMuVM38f6zCJtTB96WZ2k0iE0pl4q40sFVRLl7B6ox0x9Le7uCSnzo_-lkgIFfolLX31Sg-w7jPinWmXHdt8XQSo-vS6O1oEq-IuIMynLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=UAU468jQ6pcypMMNFmhgVZNdyb1JITB4YtL1AYrC85QU9arXbQdoQk5fujEVFcT4grhJWDYahfRxxgBRsZNunk5AYttUbNfXGq9wG4F1a4Jqa4AZGSBRRszvMjA8nYSYTBz0euZGQ2N-ApvVRR9Q9jaaeoSpnJostOl3ArsWX5NYe0gM6HEhp7OWLNj8V4QrPc6HiKGiGRUvP4yNKwkxk0ee_JSOvf7zoovB4Tf4sP0iMuVM38f6zCJtTB96WZ2k0iE0pl4q40sFVRLl7B6ox0x9Le7uCSnzo_-lkgIFfolLX31Sg-w7jPinWmXHdt8XQSo-vS6O1oEq-IuIMynLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL3K2CPfO-OMmo3PTSJNQC7wiT910L-ymBKPzyC4TyhI7_FsLFf9622wUe8meELHJTmNLoBzyRXr4DRiRv30dVHLXyOa8ESt7aes9FwwDh9bt3I_sAkxreBo4D7e5YQ6R4R9rriC7YYoCb5PhDFqohhnwA8NFgfev6TRQrGeuczJw7imN_BvEjGW9K8s8ffYQqcjHkrwHijfAwasFcbUV-WBdXpL6uABZBWUeTXluZUJ9kTLE_rqjLtAjxlImezWI_BvbG8YeVf3T_eB7DMJVE4RFc3GNKpfY0cZYGzv8ID92pr4564LA8QyKPwt3n67ILWPlkQ1UFX6e5Co4bcchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNp3FPBTw2zkEPaK3eUUDSa1lfxaPd1BZ4iTW_pJDMdr8dKmOSyj-pia_sE-YqHUHrFe-ltpYcOMPCS62s87x37zo6j2-LjYqBxEj7sfl4UXpI8kulNpXTZKgcexf4gwUq-RtSFUcNcxYPrQUhZjmsqty5hcI_mPJV12VmjNK4kzHRU0bmeREpAn5QEyOBd0OxS66qVDWj580XuncMRM-XgyJ0CO1hul3GmQt8-FVMRz59CrspogjocK6HsZr43UXSobBrT7lZCaPdHlPAIaOZkJit1JYxMKoqFpf1eiHs_pyKFrDBu6T70Sab-pC1NmliKe079CYgFW1LTpuIDOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKtDbGKEwqTw3HhzGOUC7Vbzuw0BYqC55nVl7oDG8L0gfTxP6s7KROV9iuKkRFIHPPuRX_5xRPWm0O_zTVyrwxf_Vnjr4ZWm879VZMl984WlAGg1U42LCR3rn5NoDc3vKWkntKaOLFGNKJY_hXTvmUguCEjGIuMD_GRvBvzBjdcWzd79uER8TBQ_gQfkYNOrisyqOVSLUhBo_vCcCAnCcoz_JxDoJ-Kfo40auXgV7gCzJ3cZ079QbeIJ4yuZed3Z8a-veKEMWDvljywru_VrJO0KoWLRkm9MyobSs0xvkWkigLQntxh6IHeyCPjVBKAXbhu3iQSYl-zEDQVOyfETkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=LkZlI80NZ_bYYF5dU-2RwKSUp_9ewGQ78cDnEfIDnNFidmAbxPOCyMdXKRm_bVxzvGvtfCxO-66h8TmtGn6B7_CekPqzE_3l5cu4QU57fUwyjJK8zDx8MBbWRNy2wOacjuYCTln13RxrXE-4Tyf5arf4UnetcsAK9SIIJfh-gFbeM8NOILk1Yt31Tk2yhEjG9fq1cjgGWWk7FPwyICYWGoGT4ItmxKWngbewPp3h3sJeAa3aJ_f2SjO0VFxLMy7KbAAJ6f0HXCx8ASxmuotEpedEs9NhlCK1lYUpV4MRplHq1gI7ZU93RccEpFwu7OjWRIzAecQb7DsxfKqQ0LHBnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=LkZlI80NZ_bYYF5dU-2RwKSUp_9ewGQ78cDnEfIDnNFidmAbxPOCyMdXKRm_bVxzvGvtfCxO-66h8TmtGn6B7_CekPqzE_3l5cu4QU57fUwyjJK8zDx8MBbWRNy2wOacjuYCTln13RxrXE-4Tyf5arf4UnetcsAK9SIIJfh-gFbeM8NOILk1Yt31Tk2yhEjG9fq1cjgGWWk7FPwyICYWGoGT4ItmxKWngbewPp3h3sJeAa3aJ_f2SjO0VFxLMy7KbAAJ6f0HXCx8ASxmuotEpedEs9NhlCK1lYUpV4MRplHq1gI7ZU93RccEpFwu7OjWRIzAecQb7DsxfKqQ0LHBnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Rr5V8WJFPE95tcD5kPqJUCBg2a4-NVbcMDAeSpk4LATv-fjxRbAXB0NpB6gqJ9J5ja1jMi26NskF3QKrvvbVJeFrFfoWzzhJJ0guf2Nv9nu_kmJxzekro343CoWxK0n-agfNbwZuYbaLv7EDbztfZ_CjNym3Rc7PcQLPbBnj5wNf1FzuinEyh18Dg1XWc8AopnBRIb6_nEDSU9bNfmXKIceaA-Bu5vR-UE6zGLex31xGAEOzHfxiNoq7erGIwDuAFJeOlakmkOspPT6Ji2VW0C-r5qFv004l6Wtoj3ocmrF1fkzcmwudksJgS5wNNz47NnaawaRt6DgRiL1GA5TagVU9a6QZBVP0X56vTR41JlvaVcUs8xOD6yOexllrtqN-0JVn1JdM8S5ytv6KUFD9oG0FboN6k8LJaEr3OIN2c98v9E8upEHghlEJETPwA0NEcct4FxUULrC-8Esga5CmOGkSRp_vfRM_3NrB0ajedpWBssYiZWLwMtpLf6LkyfSpdHQuR6v0SH0JkGF4sKLcbipEn0EMERRoYMmYu10Jl5QbpFzDDARaIF0rYwzxzVNBn2N2Yha4m52zmeHFhCORa-lNBNpLUGJJfcPv7iDKtZ7zbSf5O2lfUNx0oS19AjehT69hLjNLFuJnXoVc1gjkZnRGVQXtxV8MQ4RxYBQpPOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Rr5V8WJFPE95tcD5kPqJUCBg2a4-NVbcMDAeSpk4LATv-fjxRbAXB0NpB6gqJ9J5ja1jMi26NskF3QKrvvbVJeFrFfoWzzhJJ0guf2Nv9nu_kmJxzekro343CoWxK0n-agfNbwZuYbaLv7EDbztfZ_CjNym3Rc7PcQLPbBnj5wNf1FzuinEyh18Dg1XWc8AopnBRIb6_nEDSU9bNfmXKIceaA-Bu5vR-UE6zGLex31xGAEOzHfxiNoq7erGIwDuAFJeOlakmkOspPT6Ji2VW0C-r5qFv004l6Wtoj3ocmrF1fkzcmwudksJgS5wNNz47NnaawaRt6DgRiL1GA5TagVU9a6QZBVP0X56vTR41JlvaVcUs8xOD6yOexllrtqN-0JVn1JdM8S5ytv6KUFD9oG0FboN6k8LJaEr3OIN2c98v9E8upEHghlEJETPwA0NEcct4FxUULrC-8Esga5CmOGkSRp_vfRM_3NrB0ajedpWBssYiZWLwMtpLf6LkyfSpdHQuR6v0SH0JkGF4sKLcbipEn0EMERRoYMmYu10Jl5QbpFzDDARaIF0rYwzxzVNBn2N2Yha4m52zmeHFhCORa-lNBNpLUGJJfcPv7iDKtZ7zbSf5O2lfUNx0oS19AjehT69hLjNLFuJnXoVc1gjkZnRGVQXtxV8MQ4RxYBQpPOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmrvSX5RSEz4Atbo3Fng2j074UuTtWEnsyEmiGQtroF7VethxtAkSaE2YSajrA-ePCDu2SUEM5jZwef1uZWilsfQEfCpb-DnCGMsKmLDf8X-8bmz1cHt_EPaoJNxmmppoquizD9txdtVvb7qa5uA9JGALWaFtTPbCavPQ8ONmhDlpVwKgpSOQXlWBQSr-eDUPXiXtv4tIm-Hvw-BTjshb3YRJA_0yuWTX11Z-QTdB9n7-lNlwkh6wbzQFaHvXOV2gZ3kkJn-Dzct8sf5GFfAXBeyP4fzozxoeFn7DRRXYq9ix80tGas7ovgdXikL8-w5HVWt2YFUPh6NmKHu5yfmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRKi47aaFLKKfXbt8dyowuqYcEovDNEUqlaWKBcefIqX27tV0j1Zq5Hf9chjQ1Og3buvY06qtZoLkDQzXdDAywsTVCr801whPhaJfCrvgrXiqYrSPuJW_V69fS6CeVs1hnwtMhcvGDUmWMQme1d0qPzYii9YCKeqwUbmwBVexI7IkaI-TGZSJ5oBBDVBzvYX7gek5szpP-vVX2XCsmBvYFcMT_dRdVDfgDi6dgtfzgOyN0q8q4HiM0SP58mSpSTPwol-yPbqr3XlZX1wO1ZsAnsCiPjqvHcNvrHlAOfzmSUQ68zlLOgAN4zMM6Cnn20gGkOmrnUH8OQNp0ilOOaUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGXnBteeiVSFa4weWAnJM1anK4kxIO4mQHSXL9N1kjtKiDlTkHUl-2POhDoWpCqpvdmjSX9e79aIo3k_Ao--JeNFp8_YzIvUz9_FfdcXjc_RUR2KTNutK7YBgoOaQ1CUsCCdlhWCaQU9mACb-mQy4ydxtpdYHQCR6biCk2BPXidbxld3KW32F40O-4w2QtMvPbeLDDchglz_4wXwSqp9q1-44gjI7zrQQxfQeQ0s_aB83co1DyABrQUWJ8AKZ6JvV2JpxD44r9dGrNdB-r7u-sM1IsSv9RPni3gJ2Ga0W7SyCGrsCPxvS6ij03Yze0Ux4hTZS_CH3H85KFMzq1a_ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=sl4qHZtI8xwGkt5OXsLP_Xa-g_2tAnJnmaQN4_VxAV14ck23kosg6lOrAd9F4UgN1Is_ImFndN-9KP3yb9c_D0TQNRbb_FJAMuwmUojcXwCsxSXxadJspigIljCN2T56yI-KOmbh18vFuL8cEFPlc3fdlNSVocUpSs9iht3VTOkPDS9Isj8_4M9MMF7UpOcDNUGepSTE-WDLWVsfd-f68X82YrGKF87gs2iHPrnGeQ2xrpm9Taj6CxlfufVESrpnQlEXyZx7cjY1tLw1eIMrx41qn0_-ijzwDcLhMb8v191nmXU5f8W54Xi1XEejbTiCbI4cQQdfhkZZ_Tpkdn8MbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=sl4qHZtI8xwGkt5OXsLP_Xa-g_2tAnJnmaQN4_VxAV14ck23kosg6lOrAd9F4UgN1Is_ImFndN-9KP3yb9c_D0TQNRbb_FJAMuwmUojcXwCsxSXxadJspigIljCN2T56yI-KOmbh18vFuL8cEFPlc3fdlNSVocUpSs9iht3VTOkPDS9Isj8_4M9MMF7UpOcDNUGepSTE-WDLWVsfd-f68X82YrGKF87gs2iHPrnGeQ2xrpm9Taj6CxlfufVESrpnQlEXyZx7cjY1tLw1eIMrx41qn0_-ijzwDcLhMb8v191nmXU5f8W54Xi1XEejbTiCbI4cQQdfhkZZ_Tpkdn8MbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufkjtkEEbfpiR9q6BB_t6GVnFROM7GJ9pr9HhlMXtu3Ppr9-gX-bS-rguVGcGq3CccB5ONpMu4kXzZedM7pfT610nhow48dPG33mWHosflF1Y-z6Je0SyZDuVzcySI0IQkvZzDka9b6qYv-kY7vXdiBPH-Rf_Ok338m9VAc1XD7i7kiIeCL9217UOGi3uUTOZpRlhMPvKXsccVtbrseOEK-HdfoRI1kqU-0R--JjEIlJuALi5Em560HXdbH-iAvzw2SwmbArKT-3v3Z1YWXbyC5iROt1hYI-Dqd1tH8p90I1KlqROOc1BOKK73u9xZePjsdb4wN38gy2ket-b-x0vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=cPi9HsVg2P0KG5k9k8LuWL5r-Hu6ZVHC268DepqmG35B_wUoa4Y7yeeligyovg-0JZ7XXi4is1jqq7Vsvqa2P7hZU0BwH6hxtfarxBeomLLXXyb9tIVSk-VuPDWiO9VBkfNgxkgYcXY6r9MSzDiDCzPWUCIaIRsMSMRsra8tcczDpavYcPM1k_Z2PWD-GY72fuPZWpigoA2dMHx7DgRF4cmkT7tONET-kZDP30BaFZ6wgMA9-6_k__m-uQ5h_DJdXi8Aq4XwyAlpBdhh1dLG1TslCyB7tPCKVEGumTBkjdKVkrOhKAByavXttXAZ7zwjZ_5OEQQWw60Xx5ztO7vpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=cPi9HsVg2P0KG5k9k8LuWL5r-Hu6ZVHC268DepqmG35B_wUoa4Y7yeeligyovg-0JZ7XXi4is1jqq7Vsvqa2P7hZU0BwH6hxtfarxBeomLLXXyb9tIVSk-VuPDWiO9VBkfNgxkgYcXY6r9MSzDiDCzPWUCIaIRsMSMRsra8tcczDpavYcPM1k_Z2PWD-GY72fuPZWpigoA2dMHx7DgRF4cmkT7tONET-kZDP30BaFZ6wgMA9-6_k__m-uQ5h_DJdXi8Aq4XwyAlpBdhh1dLG1TslCyB7tPCKVEGumTBkjdKVkrOhKAByavXttXAZ7zwjZ_5OEQQWw60Xx5ztO7vpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=YHOyKPobliCL7l4un9ILo4RW7t8f-ALFQ_bUYLuxy_1k26y_gFGXnMm59tL7fMACFhxf_Mep-ADLAjci0m2MyLhpMcD-v1Vgp5-JH44oqq7NJt-UdezVimt-iQXCBr8_tQNZnXcG6oxiXLFctQfmU8z00vlQPCaLKS0b8HpvjvDURALOLXPdD2_eOM4xqctJAZNR21VDHKPd9ztkcw8TDnDBi3HL1fy-trxiCR-jYwI4x-J5nHmsIIgNDkSyE38-qHmdoX-FA6tw5-fho3Dei8pvjdfReZzYgfBa0OPkaPAftgQVS0x3gQsypDq77UKgjQU66HJIbqsCDBcu-V9vtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=YHOyKPobliCL7l4un9ILo4RW7t8f-ALFQ_bUYLuxy_1k26y_gFGXnMm59tL7fMACFhxf_Mep-ADLAjci0m2MyLhpMcD-v1Vgp5-JH44oqq7NJt-UdezVimt-iQXCBr8_tQNZnXcG6oxiXLFctQfmU8z00vlQPCaLKS0b8HpvjvDURALOLXPdD2_eOM4xqctJAZNR21VDHKPd9ztkcw8TDnDBi3HL1fy-trxiCR-jYwI4x-J5nHmsIIgNDkSyE38-qHmdoX-FA6tw5-fho3Dei8pvjdfReZzYgfBa0OPkaPAftgQVS0x3gQsypDq77UKgjQU66HJIbqsCDBcu-V9vtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=gTKqrfWhYnmZAnDD3mnIWMTy-LaLXKNPN5FRTVpCAAhSJ_iTOW6fbZXBesjtgfAXchrnrX1abBe0vCPU03IuQ5jBpG2QBjXtPibi56kL8TgP3nX4GaQYsIw0ijSyH35k_B_BRC-FUYM4yiIa7ip-Cd_SFgGEZQ4NNFZ9RvNWoVFiRITM9Bq3Vo6ycsxMIiMJovB52ZsrvAXuWejbcyvWz1QEAAzg1a_ZXCWheCVp9Tl0VeW-Nw8foWQh609BddVK7Bmmw8i3bNoWZyw7T5g4o01Tjgr4VF3lWRTS16NzmcrJpQ5ZYSltevO-y8v1vMhqiiudsxcfMcFhu0ZRbsCpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=gTKqrfWhYnmZAnDD3mnIWMTy-LaLXKNPN5FRTVpCAAhSJ_iTOW6fbZXBesjtgfAXchrnrX1abBe0vCPU03IuQ5jBpG2QBjXtPibi56kL8TgP3nX4GaQYsIw0ijSyH35k_B_BRC-FUYM4yiIa7ip-Cd_SFgGEZQ4NNFZ9RvNWoVFiRITM9Bq3Vo6ycsxMIiMJovB52ZsrvAXuWejbcyvWz1QEAAzg1a_ZXCWheCVp9Tl0VeW-Nw8foWQh609BddVK7Bmmw8i3bNoWZyw7T5g4o01Tjgr4VF3lWRTS16NzmcrJpQ5ZYSltevO-y8v1vMhqiiudsxcfMcFhu0ZRbsCpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRnT781Q7gEOCokqsTutr1EWG92zNC3NZhWJeVrha57s-TZjI95TTPFb-Iufog2E5849b0t1Z9VAarKJpoSvS8Xeistu3CV-okE6HW78oyvhPqSTYD34XctvZ-A_euRd9w0hrCxfOVkpPP-Kqk5InOi21wB8u23vcyjGecFLJ-lMWNNnt9ijPnvPLoExifzhyJG7AxiM3jALxZc1juMS-twVhsTYKLKvMOm8AiwG6ycKlJcf9IZlV29Bf7vk1CZMOrX7WsI-GR3j9YqoJVCsqUiubhhhhqC310ip8KoCKgoMA2U4yEqqktKaqB1h1xZNx5o0_qtPAs5afUWLz_ZS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=o1LmcisATjH6BFa2wk5l0OyloGYW5F2p78ZEbRwn1exOjDYWOcooT-HK5_Ej6awtHPJ1SKrrpRnlo4pvcd206mmr1Cp-swfB7XScobh4HsThljv_ALjHYiPx8gDZc_CcPQDIym-TYdWom6nMl68mxpLdEgnKAgEihuvk0OfJZnC_ohIR1ijBj3WTjSVKKld-MttI_8pUykRfeLOold8HekrdvC2ysasAQc6woc-2EuA9aJm3L5EsHoneWBvQs1LQxawKsmuN8zSt2xnS7PtKxTWOqs2HQtPE-7rKTdkGQxY2mB0cJvakOufhzHQIjB5RHXvc5DltUC2SlWsNZ6tEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=o1LmcisATjH6BFa2wk5l0OyloGYW5F2p78ZEbRwn1exOjDYWOcooT-HK5_Ej6awtHPJ1SKrrpRnlo4pvcd206mmr1Cp-swfB7XScobh4HsThljv_ALjHYiPx8gDZc_CcPQDIym-TYdWom6nMl68mxpLdEgnKAgEihuvk0OfJZnC_ohIR1ijBj3WTjSVKKld-MttI_8pUykRfeLOold8HekrdvC2ysasAQc6woc-2EuA9aJm3L5EsHoneWBvQs1LQxawKsmuN8zSt2xnS7PtKxTWOqs2HQtPE-7rKTdkGQxY2mB0cJvakOufhzHQIjB5RHXvc5DltUC2SlWsNZ6tEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoHBqkJ_ylbD-grzO37wdjnJ1Y1R_G6m1XH1H_yMk0842-gSlukz721QBlV-AIDiAxHV4ycpa60be3yqrUC2yYJPATUTk9rOxO6Q-og3cDGN8ih7p0rB-lfT7FrLzDg00Spc0MYVnhkrEAEr-MCjwxMExbR7v0tTomfyTJiL-gycfOUNYNq0NKHkov3NiLlrmt7ASSe6wJpekWCZDwXTJZ2RLDqLRnNtwOCGcmrCN_bsNYpGBYacJkFmVnhZxMuPN524L5idhBGusxd176tRKt0VFwZ1tYJAPG3d66hmORb9BEoWONAEAP7fKspPuHLp07HhaDEhCTDsUczjPmRPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
