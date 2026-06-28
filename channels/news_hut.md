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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 23:20:52</div>
<hr>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1vSYvEDcq0l4ZKUSn0z6sN-oYHQmCv0-V9H7aFVKPdulX9_Pas3013MzLKtywWtjEufUgjWjBzfaGdddh5xziVLc-v3yxEtej6Rikgw6wT6-zfqiGE6Xko0FzUfBEqKcSdcXZvBtLYl45N1mVKb-18w7RE1uCH_A9iGjPnif3Wfhk1LUdkdkR97B3icYxq-8djgmMT7Mmk_vqffFg2YCBrWpPnqe_o1mcFLVIjd2YYHxFTAZEVr8SWnZn5WhWI87IC47et5pzO5y-2_V3ecPWKauncr0fl5HSVgVP9poDCbXf_mvKuTOVuaYUKyGhWiKw4yYbdAJg5C73ka2DCcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvnlZH-QNiC2Ltq_mHe9ekVhgGZ9lDrAMKIgTJmpRs53XL6p-KKtc0B-F1ljXS2z374u5FIgI8Lu71XhzACIX3Z1OqOn326mzpM3NUZ5RbxXNdGVDFx0o7J_cPVHKakX9l6Dy3uKgUKtTYJePR1-C9QxEJ0jAFEXnUckbJUm6KsdGLf01MResvarSBmvw7KddVgJusXcfUZ_9oSYwG-1wTP4fPDl63SXnuV6RpatNe6ndJ5YD2R-qiDeF41-XJEzHJHDRoBRhA3F0Ir9YDwftswOZUi-4BSHxEfJMh-llgeE0-D38eIrCETKTymbiST8rHQHffxaIeQZ9yfkQoqF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9G-ZtQ3Lrncz9vtTI5IPMhWmXqK08eNnO8USvvFS6AscUQjOGZEtM4ia0B-ozEj59kyhLE0cytUt_gJ_PiiKyGWAqb9Fif9Bi_E2qeur0GxC2o95x8xW9-oyzwGyTxStnq7OdgMTYTjED4jAKU0m8GM-GOy98MQuvujnHyF8-mtja6fu9wOq44mnAWQdJzklpz3NQKIDzbutGOK0olsZ-usIzFlhKz02m9eyWZCV-zbBKCrbNhcLv92HRodA-luTbmQwEsoNmHDIh9ndxfFyoSgGJDJj4_sHv6kFfnqRAglMS1_EbaD-OwzTpDdarok1D5ktjL3i3OtkGxG7R1GfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txE5BLGY47fqy4AdX46zKMrx8hN7TiTCWmMXUBZwcI5n-Lp9lld0B6sue7D1K3S10gSYwaQj1XpnCQieJDM6k0hmbA7U1X32HnPPwprlx7bdxW44ntKa4HyHn0PseUKSZSSiUIPzLWglTHvwMKe020kLhiKbymTrD6WsBVysiFODAj4zh5U0iwT3WNyzeBUVALPFIyswQVLYlOa7LdZsdtJak25WTlLBDVMPetNomVse1OtVGQLhPQDtFI9yWpjApLzqXP_mUCMciyFOC8QqeCz8-uNaRB9E0PXrxOJdryYecgo_xy_vV37k9pa8LVKKqpoIUs4m6yiVXbfaVxr5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93ZWito6W-WrsHfqGSvISSUuH7WJniT8ebdG-FuV-jHeAvzNrFSd0OhhwHtu2f7t9cMm9eVq3eRtnH1eEnTNQFKm4YJXExdv3HSlvhcNWlG65pqLfs1UGPI5hCUb_5alcaR671OpUBUJtUl8CsfPxoIPctM1t_3oJRInfIF-NqCRsH9Ib6d3TwSg0U5zskPSkFG4ifBSukdRyTEYMYOHLx4zIhBfVLo_oItRl9lpUgvKKUaZteIPyd4vVEg5z_5U60iWaXsbgsC1ST5Hr9sPzM1MVwt-rbN2eQQiGWRD0ZfHFnp3ysbqtJmLDaNF9XDjtynuUwX7Z_gCPg2NevsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=DEJnCqf3548-JaBv-NjEXP0GI4yMGSbNTEYxv4QrNDcIahAa_F0wTwveBTHxLFbEmjFwYQQLEKypDH72Jb1l9OfTaDjsqEcJPkHwZ96dw7hDLB8yAX0RqYNLdCZItohW-1IZnuv-NW0bfd0WPcgP0RqxFgGAyv7LhcHIS94rG0QFjEOwR3dWDnUYmDXV0wNOPoLaj-8T4Kn_xW4F1LHzX6rWZzG0ySmPqkrCcw4DdmTSmmOnJpPjcZleYXfANUOFYUyzQiH2boe8kBjsYmg55Uj_R0Q3D_oeSjob_joIrr3PRrIscbWBjWz0U7_WhP9x3Oqx8bIihvmFu86ivR3DNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCDizrkm7F0QVQGygRuz8lDk3HO_q0O9LdnTwIcdRvn7VmIIcCuKkjkoRPi8wSJEW4i8BSlcs_Eeb7fdOpLJWzgKPF30bIRHG0f4MKBAB_3SmalopIdKLqUKY_dCvhpVJvv6PmzH2t4DMC7f1DUwaynmNM7E8apSNcN_oUa56Dy6PBRsu53_Mfu91X2OrWwIXOS7X9A1fl5BlZspgUMq8VhZnqYY319HPJzKhnp77Orz5e7ORcwdLfoaOa-0htLJ70uzE9XVVP8GyOWEoCjIF-8M2VDT3AkLenUEnEsvr2Xo5nybgx8cIFR6f1vXNRzfY4jcscyoD5dlXZYAOQv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4wbAa83lLhsIAAQn-xuFxHMUi_UXjagHNMTYQfAVKJHtyu3Nv9jYPek1UM75eXD-zKh0LDA5HKOBbeKsqcXf20kP-QR3yzHNPeObQFunRSoj8RccV8_CYFvFqpLSxxUqWCl4JULUbqCSct96op23GvDkYCfRtA68ud9oiwIHSOq9mLAqqXc608b-gqNvM_VNty---NdHaNRLbpmFY__TaPYQtd6fl6YmJJa3sR1ha8Y6waxMMmeo80FsuMc6N8Fs1dFsIt9X8Zowz5mtNABzb7Drr4yTJygXb_R_0fIFixwSLJGL4-dlftHfbwwIi75u3P_NMGKBCPNOhiq20qI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=cwPPv6HFBenFhf-DZJQ8HbIT3h_l_thbc83iuT4x8JnFUMRAOqjhSZVYcBrRmGLuHu3QWgGG5TvpApGEqv7uwBxNFb2EHTYH3YIAFdh1h3kFU7L_QK9NVF51H8wsk9qazV3c5b4UfY2mSglJBjK0-B11Mpt_9cja5YaXZzWTXCbPu_F2Sg0bv3DIPYPTTC6Y9KlQvwjnqmNGvA5Y1BICYBihC37vYSqFPbibQdvYtFffMVUVpXhbDb4VHOY9EEtC74s3x3STm5wS9XoWy2l5DI4IRbLwUHFiARhTEqA6jakAn2jIfuS1QfSidgCr0imWSXF0Zjr-3-N1a5PxXXxwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOwvyS11wCVx61uBoi2kGB8_RlYuPCGma82SbCOlndw7uTHecLiUJIzXyLu4Web352qrxuUILMtyFt8sUvEdaDgU9Eq7hBR-7GNLZ82ABtJ62VWcNiQuKHaliWB4550eoV71k4jPBZOxLvbdFyZFvdFG0sHj3pDa2ZMYTLWF3orqVwfPC7t7kT8gCZbaLJ0KQOvtNnXk3W9SFFnVzrg42Qp8AVhEQbw8JVEFUbmXY1wKdKExYSWyNR-eG8SeHMGEqACbPZ9kdUOJoDZxgUZH6P__FE0IOxKFF3cEGXYxqPVSBGSvRhp5_tYtZfZLwJA1h0Y8tTdxfCxcq4ZrjomJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvCwQJLLgXZNQQ9Psz083q9YmI2wsqSh-Kpt7hqdS0as2iAavupsxFfPAuQ_waD1UM8svB22vuuBcNeOlr8U115sR32EU00qm5YtZiJg0LIBuMGu5IfMo9WTSglu6jDlWp1yRzkcBA47CM7NmYpMmNM2QpbasDJc440vzgxFnTAkaMWHYvIWKppb7a9xfAayE2nocZoDZ5r6LjQtvTEkTIsbhf_zXC_v_nvgC3Hszrb9Ib09Q9vixel7fJgzxZuJ2I5g-KOxyq0Crcep4dFWCkW4sSC6SDdQhod9PHKL00zkS7u1bmuOyqo9Tud710Nm9WmCdnsZLDNuzAVfjgaCwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzbaPc9l1h1aO-XnPCwxIc7al81C75rdXk2t761WtZv2VxPp2bCdaRwvPSkdEiNEwkOJVBzRLr1sxzsYW8s9aaVd5MUeyx5SEAUKK3uRwWtChgPuU3PuU7dTh0vP-xRuGj3J95a6eZA3LeuOXxCb-hUuxYTO5pBbtZAfrlswjFDgpM6wdqXfVSzIjWhZTIOtYv5ZZCQxB5JsOWH1Sm_ei-8_YalFzpQYO355WnHeMbHAl-HdWXGnA1WNTU3gRV5fjMz4LD88GUG0IfYKT_SneMXzm-THX-Lel1CP-ORbJpNg03MrHVUA3HeC86pxsSVY4iCvvlrE8LforgU6OC_rgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw84z-g3D7O7DSbEJA3GTowrcLaaCvGPtZJgrH3z6ocSUSLogAcBN4wlM3b7RKp1AM5N_qn-32UoU5Z5u8BXtmxKTlOLQi4iqQz-bqNQGVKrZQgsIkHalGBXHKLJxLWJdQvUpdqIYThCWMxFUa3XMAJ5OKIlz6srGE_SBVvCRQXugQDWAqad3ZjgIMYhuQLYFMCdyYpsrytDATCvm6jikYVvGzleqlt_rgZFsEJjAPOOMsvL42bJDJqSOa_gqQ_hnr0WfeHufelzamYFKQAv42GKBYIgXVdaBMO0q50zHf8d5dsqwi4NUGdji8lzWZh_Y2x9uBqMR0F-0fg2kLeJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=rwT-ZtoSpywIUHyaO_OQIeaeHIH3LIm-Dx-5-s7aJiEwNKMmapdymcCuRINFlPkVnjR739IaSNIdURMaD4cEkREZqmkXA7lSTDt_Wz8bSTkWerwZmKrUPp7LNsYkJGUP-BkiMEVBo40_CT5VMFxqQ64G-rJ9BpmxpVBNaw8tEgxv3Y4wG7kaoXJSxqPeXCgoxXErCKE3J8wzFE0YoK83DWUkFIagEiuvusudJWOLnZJFY5JzftrjwRI-j5aDbQY9jajAIgShI2Rcl3-IInVkZu0WaqaPhoXcVyhLCIwA8EuCXZGHDKbnuSxUFIrhLCzBrwzvFxsLVDXDCfrwzsdlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=rwT-ZtoSpywIUHyaO_OQIeaeHIH3LIm-Dx-5-s7aJiEwNKMmapdymcCuRINFlPkVnjR739IaSNIdURMaD4cEkREZqmkXA7lSTDt_Wz8bSTkWerwZmKrUPp7LNsYkJGUP-BkiMEVBo40_CT5VMFxqQ64G-rJ9BpmxpVBNaw8tEgxv3Y4wG7kaoXJSxqPeXCgoxXErCKE3J8wzFE0YoK83DWUkFIagEiuvusudJWOLnZJFY5JzftrjwRI-j5aDbQY9jajAIgShI2Rcl3-IInVkZu0WaqaPhoXcVyhLCIwA8EuCXZGHDKbnuSxUFIrhLCzBrwzvFxsLVDXDCfrwzsdlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFOu7zTcAI9mi-G8m722o81RirF6DUSoWUtqSucEML7td6XQjPZmwjA9xGyTAtlt1lY7mjEOv5mMuwwGT_wlfXKYVyYhyUFjXMUKy-mluUuhByyeBvuLjhLuaJ8JKAG3XtAbUniIf9o7cU-tRzhWbzLnhcfMDShSm64dWhs_ICavrdehQmhZsR6iqP4ezaaJIhhJC6U6rWYEeUuOXlXzn-nGd5hTWs3F1rAd_xcmdPi3TNsdauPwQooj1cG4mXJ7xUxjcb27GVDuyVD89iHNT7yzZQ7SXH5qnNCfDXfehTAisqi-XRRsGQyC9gGv4vWOFIuunS180aHuZMgZ77I47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyGi_zR6Lc4zPY-tiltDzs2OboyZRbiCW3dbDvLiy99KcpprQzLJsvHIGXjedpN9PHQ02Gb_36GAe8_gKrOORXY98PBdf0xBIL1mYmCoCtTsfBgL6xZtviHGSDu-9tZV3KwkdZuZT4faUqhr8F44fDbfN9Gkbe9s7-tbMH5qw6z6v1k-REzswvPLQoY9WwtYDKihFRUlkEAeTwDKuZkn0-gbYIF76JfxkVAvNCZqAbHw_f3iwRzWqL9RWdocV9I1S9hRdqcc6lAbBKh5ItMKpHPkGbgc7M7W1pxX3gqfjzyMP1C5LCQNLn6yHWsv5Ec_UqsTpUyu8ZlB8zeOMC6LNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLHnVXYBOrdN0lylPjdhN1qW39ji_8VYtzB_HzWmln-TTJJKK4NpDuu8U6PgilO7gmRDMwOcjzSoI77HRpTZR75X6r6igaAHZL3yNVLFYzBtvAVkKbvPKWPZ2XEh9JOFWuT0ChuX7nCXjEj7RgB5V05UMGw23ldupf8nZIvGU5NEPiBe6w6uAamFqXvQCOdV3Me9OV3uihcwoe68JaDdZZ3I7J9a0vSpdziOFGmcXs_UTm1EFTmAFoU_JvvVDa85adWzuEXnI_hXh1K8iPOjXQxR8jYKUzovenZSzIjVfFbxfW2L1afQ72-8ERQT1as5KuV_-4CAPj8RhyvHDc7yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ4-7MyNgb_btxfOvrOd5Bm4fnF048EEFAhAii_F0QXeEMq7YB1xjS4Q2fYFcpdlkFa2_P5jNViNj_sv81G2havrIPHlZ0upBlfSAgZQLvh6TDV5u3ClA0F_VjNBVLsIOEqNC2z1UuLxIyaVFtfb7EaA7Z_OjubboIN5hJTq59W8W75lpS7Dw_H3NLSf-H5n0BEFgX3_2xGypuFTYWOPZZbRIdrqOSadZkaFCS5OT9XlMZaIcJFwSFG6XSQ_DIVCgaU7mtFJmHr4e9SMw7UJJimGsmng-GmHZfoslstRyb1EsVdmJuwpiWlDvd7Xb9q7KrmCVXmQfXQnNl75KG4HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFNewqvDj7Purw-w1RiLLt4rILpNWcAYF-sJr_ptHwCwbI1bElfrhdQCOCZvEXTDFXTS2s598syNowXC29IzytBAPFd9KGQ9czpkW1roRw23k51Xe6lG6BzkOCHnYawU9XplGwb-dbhl9SgP3ZmqiEpRjMu9t4UeukntzYFm8sRUTVML6CTeyXWYN23H9rJymeK3cyDOtFRQJa_aB1Iaa7iFsyRhzmIM3pu6QjrWUeKR7pPgbhNUw4Ase8dlfEMur3kRyvRFEBMdXdyA0jRCW6qnmdxDb2hgPp1IzEBZSApt7L8MwnJ0xl_7jBZYUK2ta1o2U7-_umI4sq2EuTDlIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Vt3JoGZBLCaJKHCIdyzChZn0UC9n0BR1POciED6PGlrl5xroxw9p8ebJgk9IZuWiEUBUtTkdww1QZC0GHAX_zrxXMp_WIs4PHxaV1eBYnjXe8WMtYAp5lkn1SWiRx30T_LPyv8A_DvieWgf_ZrR1nE6nZWT-SlWhp1NFWaiiz5jgyPo9Sa06IawVPvoqBoeQKaH4ywMa4OelXLRO8isootUKD36wVgpdYjfqtA0yel3LRymmfvYBrKe_h6SoEv09pzaJB-5xJVyrwoXqLTr7Gp_NIEVoX-bCj2IHKBsJmSAQlXh75_f4_byKDopbYBBnVO-c3HDQCvKrWjUQ90OOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=Vt3JoGZBLCaJKHCIdyzChZn0UC9n0BR1POciED6PGlrl5xroxw9p8ebJgk9IZuWiEUBUtTkdww1QZC0GHAX_zrxXMp_WIs4PHxaV1eBYnjXe8WMtYAp5lkn1SWiRx30T_LPyv8A_DvieWgf_ZrR1nE6nZWT-SlWhp1NFWaiiz5jgyPo9Sa06IawVPvoqBoeQKaH4ywMa4OelXLRO8isootUKD36wVgpdYjfqtA0yel3LRymmfvYBrKe_h6SoEv09pzaJB-5xJVyrwoXqLTr7Gp_NIEVoX-bCj2IHKBsJmSAQlXh75_f4_byKDopbYBBnVO-c3HDQCvKrWjUQ90OOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=j3PWU5IM4ptHmn9moNHPkrZnJfncvXzUPanVvYzP-TpW6mR2078I3pysaqFQGgkuazZ7JHPavrEbh1K9Ghnb4UXk2mhOkBjLqfSDadAT2w95W9vkQqgv35kAENEgpdiSWmZhErRqVG6en_GJ_FQH3xYgfZ5-gs6NLIu4bAZIvw9CZmGUyM98NeII5Rz1D660LNAcV2-wejD7B1daLXiZwTcO3dWlZhchOXM5OGe9DVeZLALWFOAxpJMWLLc22_aW3b81BWjTt2aj4lo6kH-fXyIdiQp83Ru6ibchlybNgr9uJAh24h6ovBpbT9wLj2CULr-peSk_QYzgSirgbBl5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=j3PWU5IM4ptHmn9moNHPkrZnJfncvXzUPanVvYzP-TpW6mR2078I3pysaqFQGgkuazZ7JHPavrEbh1K9Ghnb4UXk2mhOkBjLqfSDadAT2w95W9vkQqgv35kAENEgpdiSWmZhErRqVG6en_GJ_FQH3xYgfZ5-gs6NLIu4bAZIvw9CZmGUyM98NeII5Rz1D660LNAcV2-wejD7B1daLXiZwTcO3dWlZhchOXM5OGe9DVeZLALWFOAxpJMWLLc22_aW3b81BWjTt2aj4lo6kH-fXyIdiQp83Ru6ibchlybNgr9uJAh24h6ovBpbT9wLj2CULr-peSk_QYzgSirgbBl5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=bAOYlN8L1ne7l8Kyb5xSkgV7iy3JaEGGF9ywFYrgZmLlBOC9TLLdcSe-So25mx_5xJhoeQRipHncyXlrWCHWLtYlnGAPirtmYgmNH4OCP8xoM9-rdYl__4ML7A-xtxkVCSfvLYYLilJaMo-KZ49v94ztRrZH-Qu-CGMPYnpKkF7c64qTUGgIeZGfN0FHpFLZBOuGF6qrHgCyi8fW4FI2_nc_d1fLVWHRYlH1kWLC9Bwup6DnF4RB9eaj_u25OptRjOrQ4pq3yZAA9r47YX_J_wApZicqQN8v9y7ozNXYT46cD06bjG6C448XN3YLTItx7zwdGyxRqcHAzM2cnWNJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=bAOYlN8L1ne7l8Kyb5xSkgV7iy3JaEGGF9ywFYrgZmLlBOC9TLLdcSe-So25mx_5xJhoeQRipHncyXlrWCHWLtYlnGAPirtmYgmNH4OCP8xoM9-rdYl__4ML7A-xtxkVCSfvLYYLilJaMo-KZ49v94ztRrZH-Qu-CGMPYnpKkF7c64qTUGgIeZGfN0FHpFLZBOuGF6qrHgCyi8fW4FI2_nc_d1fLVWHRYlH1kWLC9Bwup6DnF4RB9eaj_u25OptRjOrQ4pq3yZAA9r47YX_J_wApZicqQN8v9y7ozNXYT46cD06bjG6C448XN3YLTItx7zwdGyxRqcHAzM2cnWNJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=kj6ww8LReBN8LKIS4PZpzkXgrA1anfSpYI4_fYHCdFru35PP7nVBnSu9ZG-Hkqdij1kZX2UMXSIZb5PBfZr2obneRuA3KufJNXxSh3r_pmkIKKswuNsdQ4K7qIV4hOumEh_YZm_Q3fdu1WT8rANJYF1xFgcf2JfpkNljts8EOm8g0MH2Rl5AgtEGIJ9Zuv73gFSgJYWMBLUDcCpj0Q8qv_c_diR6nFRsx-122M7_qZmXyg4JoO3_xd2Et7zf_iJCiYT2FxZnSKgynFD49W9AFSFTbok89T4FgOWBiA36a2HI7hUoSakEYyRrFx2B9M4W-2Qwa6n3JYOh2dRx3vYQZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=kj6ww8LReBN8LKIS4PZpzkXgrA1anfSpYI4_fYHCdFru35PP7nVBnSu9ZG-Hkqdij1kZX2UMXSIZb5PBfZr2obneRuA3KufJNXxSh3r_pmkIKKswuNsdQ4K7qIV4hOumEh_YZm_Q3fdu1WT8rANJYF1xFgcf2JfpkNljts8EOm8g0MH2Rl5AgtEGIJ9Zuv73gFSgJYWMBLUDcCpj0Q8qv_c_diR6nFRsx-122M7_qZmXyg4JoO3_xd2Et7zf_iJCiYT2FxZnSKgynFD49W9AFSFTbok89T4FgOWBiA36a2HI7hUoSakEYyRrFx2B9M4W-2Qwa6n3JYOh2dRx3vYQZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=faPolwphrwmmPmXcuiXRMnbc5g3da7lYvXaH5jiJ0g9naewuJUmgPxpmxz9WzfXG9CJfyZTsWlT62MhChLuqVxtLniLMLYccT6Xm6KFN2f-QqZgYguo1OoN6LXSSOCUb_qNjUT4gpSWi6TLw7zBAsqbadADJ69Clf0rYLRFJHFKsPgYkBDIQDvIoBMlGbCaYjEkPf7_TA6MQTs4tZ5XDjRqQbjP_WsjelCFsbmJ9TBH21-q3LOXnZDu4TrAXqXd2sMH9yngOEbpikTpTk7KvgBovtFUyZ5Xiyq465lBXazLDWQY6wb19YLrRhrbXm7S07vNMlLRR5hM3D9EDRuUviCY9NcCbOaYHL0f17BAYI26ZIs_QIWcbPi03XBLrEI954Pyy9pq2hvXA8zAppuHg4irv_YmFO0fcWjLeNP25LndYBiQrH8C-TU205TT-8Razx2SftHl5to410IKKlys2e6p2EaOpt1_urwe_9A1RLNDkTIT2_pPBM0dkVVfxW-pvuqSbmDdNbp6Wf9PD3GpClfdvNK3hKJbpfDCkvcuFUb9VPF3q0jauwtAhXA3DxV64vOvRYTg_4HUZ60vLRLiFi8ntzpnKuJHZm9dklSnYQpbffQUv8k1ZAe3wNnhAuXa5hLMGTvJP1mH8bgPGBJNt8dMY_QtUJaDw_WcDjoD2U7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=faPolwphrwmmPmXcuiXRMnbc5g3da7lYvXaH5jiJ0g9naewuJUmgPxpmxz9WzfXG9CJfyZTsWlT62MhChLuqVxtLniLMLYccT6Xm6KFN2f-QqZgYguo1OoN6LXSSOCUb_qNjUT4gpSWi6TLw7zBAsqbadADJ69Clf0rYLRFJHFKsPgYkBDIQDvIoBMlGbCaYjEkPf7_TA6MQTs4tZ5XDjRqQbjP_WsjelCFsbmJ9TBH21-q3LOXnZDu4TrAXqXd2sMH9yngOEbpikTpTk7KvgBovtFUyZ5Xiyq465lBXazLDWQY6wb19YLrRhrbXm7S07vNMlLRR5hM3D9EDRuUviCY9NcCbOaYHL0f17BAYI26ZIs_QIWcbPi03XBLrEI954Pyy9pq2hvXA8zAppuHg4irv_YmFO0fcWjLeNP25LndYBiQrH8C-TU205TT-8Razx2SftHl5to410IKKlys2e6p2EaOpt1_urwe_9A1RLNDkTIT2_pPBM0dkVVfxW-pvuqSbmDdNbp6Wf9PD3GpClfdvNK3hKJbpfDCkvcuFUb9VPF3q0jauwtAhXA3DxV64vOvRYTg_4HUZ60vLRLiFi8ntzpnKuJHZm9dklSnYQpbffQUv8k1ZAe3wNnhAuXa5hLMGTvJP1mH8bgPGBJNt8dMY_QtUJaDw_WcDjoD2U7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=RhbSh75GrzJZ9P_7UsGAJ0aeok4yZcgp6YAqdOibJ_5ZNBxJbiSgNkddb-ogsbvthFE4GlekOjfWRiVVaujTElXnD2BQb3finm4VvHRxJbZTh33mmHZ53V61wIH1dMT16oAyhYP6UnqvgRIoIHFg2kD2kCbOdz4NK5VgSZfgJZivdraX-UMEaywNDbuf071DEIlTaPNAXkrdBXyZkGRAIvYHH328wb_OQHKmpKsT2YgNi22PHHNdjEYOnRHFCQfNgtOYjnESZhQQt3zDMdy604vmVCGUyDArKsSwmW-v3oEMww06XvOQPXUGrfXB5fR5glw4p8k8fPT1O0jdmi3tAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=RhbSh75GrzJZ9P_7UsGAJ0aeok4yZcgp6YAqdOibJ_5ZNBxJbiSgNkddb-ogsbvthFE4GlekOjfWRiVVaujTElXnD2BQb3finm4VvHRxJbZTh33mmHZ53V61wIH1dMT16oAyhYP6UnqvgRIoIHFg2kD2kCbOdz4NK5VgSZfgJZivdraX-UMEaywNDbuf071DEIlTaPNAXkrdBXyZkGRAIvYHH328wb_OQHKmpKsT2YgNi22PHHNdjEYOnRHFCQfNgtOYjnESZhQQt3zDMdy604vmVCGUyDArKsSwmW-v3oEMww06XvOQPXUGrfXB5fR5glw4p8k8fPT1O0jdmi3tAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_raW3xWYr3rpcaSu0qVFPeZfbJXjiqPliFS-maTlV1SM0oFquiSY7b8NznQ7MH6A5pbeJOfhJnZZyoXdCUjl1bYF8YOE1Y7x7q9WS0qzZeYhfl_L0DaqYpxU3ZYNEyv0cLQeupWmQ4H7Gk7lrvKVc_wRt2HuJLaW-ze2YPS-fvOeKik1WF9Fl9exn3edl_9pP77_dLc8dbm3Rm83Y8hA9ctqZXcGh1j4G5zRqwGpuIyWo4Djo1y8jET6xppFXTNBa2T_zUeQ8lSPeAEnBVzXaEQZPMKe14mzIfhK8z1C73xM9a3LN1XcaqowlBBUvVCwsaB5lbwlGarqxy1sclIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtEDRWoBw5lU-ffKPIlHQmRDxvZygJu9wOuN6Xy5fXZ8YqVx7CpTtl7tNoYQoelNmGrC2mFWd_dzBTlLOWE44N-CQP4rRiU0JO1NYFweQ-NF0juE0kTw67Gjt_fnKqn1Xq5CwXBYvfy_-okllEuw5NBvbZvUncuAuL3NDr6MHWjtUILuNinIIyrY_RXnVJWHGMiIuKAqpYVDB_i9cG_Ty7ze_31WErvaZoCukP0r_k9H1F_IRXFYcldjVsY6dRDP8DXnHWkrqnwidCg2iCbhHqL8d0aJQ2SGJ6TpHexoykAWo5Ivjdi2w2FLo5xTdobWjmWimVwzSLLQmg8ph58sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJhkxvfga6FkiniH92G4Dn7XoIPKPzr93lAgxu8sZEpbw1EWlpvlwVa2ylX0CeaCPosKE8ishPrC6_0HNKwb-EopnOdF16ZrOibYxNopqIb8CZQTfHVSS8oBGWHLifBu0Xz76X6I7gOghtwPXYqXqJCO-WiRAPZq3Un0KX4l7ACwuDP0k8zD96Bqw1kCSaO1vktmitI0Un_amidoTvSvwSEie-B623A7I6rmg34ZxlWK374LfbxU4cxu_4qy-uXyeth2iVsleuQOdB1eZxSHbrO30hWcAgFHNZL706pq4ObKD6dpwEaubd9KWrUqAPBL7qmfqiJlkbV0KbDX6S698w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbf-15SXHipDzgBahb_AYK-1hHQfsp7UyhTacwaltFMym4PNsLu0r6ls8cOQBc09fXcx8yXwx_5eft0p50tnBGjlbYaDZPXGSlw0rtdGl-_3daYFw6JOaoaIO3DwBXQy11AknMDw5UC6HOVaofKo4mGgtEKI_bbTFbN3VYjh2trO8Rz6PswjzLbmOEmQ_Ji9E2v6dHUWbBIRuE8wIvrM3PEeHqn0oD1BLOQevWUj434E_u6X0dBuSACTXQSF-CnjnmFkatP4fN6Kbz6kz86jV-maJiDVLvu9LCNZYBmNh2D1VN_rBTM9WMG63xNXQivlC1cfnEHZztO1WMZSOd_VHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAeaofHLF4loqR-kqMJB3mA7gBzaVwAgXNJe1yKJPRV8ngWrfYP7GOvASyMoxw2H8zxZyS22KrJrRsrlA1c-AnFEVx84ukMbB_7KeUnixX3pusF0tMoiUpIJAYE3wQ6KXnYKV99yjlA98RgQlK7THEOQTeSdsw3wKhYYA12UVihApXKBTTKn-9NtT7GvtYnt6uGiLfaXgFlr6ARYrj_Aq_O8Gw5Vx4i40OEnR3DozeP27IU2ODubdSWdALkiXR5wOHt4yB9A-kANpXfbJUhkTcH0auT-iQY6A5I602iqtVcOhhxG8hT0sFv-2LnPRnP7d9Qcb6h-0W-jWlVZEQU5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=LRSLL5-cROnpB2laUp9SEfEQ3Jt22hNC3NaB39t9ScdgbR8_fxGMFEvsMdiff06cVx3dNo_eqz13ZsfiKlvLN8N2u-ML-pt0asRouxP09mAHWLRJ8NRaF7vLu8aCAbVQxeBZ3qHx_Rv7830gjcJcoqnm6U3CBJtLi_GcRCP-wSc-nobTNPvnSyzgUaXKcklS5sEVfD-fEAde6uRkykWmoTgR5C4tGgGLE5VWzA1xhlbLUDAQmzfjmK3udkC1MxdPXMlwDzVGP5MyryikZd8hzlxGbCobJ9UC7Vr_JclEJQlykCQK16Mf7GYSqAfObmnO9YLUZamXC7O1RRnaLhpADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=LRSLL5-cROnpB2laUp9SEfEQ3Jt22hNC3NaB39t9ScdgbR8_fxGMFEvsMdiff06cVx3dNo_eqz13ZsfiKlvLN8N2u-ML-pt0asRouxP09mAHWLRJ8NRaF7vLu8aCAbVQxeBZ3qHx_Rv7830gjcJcoqnm6U3CBJtLi_GcRCP-wSc-nobTNPvnSyzgUaXKcklS5sEVfD-fEAde6uRkykWmoTgR5C4tGgGLE5VWzA1xhlbLUDAQmzfjmK3udkC1MxdPXMlwDzVGP5MyryikZd8hzlxGbCobJ9UC7Vr_JclEJQlykCQK16Mf7GYSqAfObmnO9YLUZamXC7O1RRnaLhpADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=JeSOVEVq5Z0wWndo4qh0lDpmeSxuCYwg00Krqp-rj-dPaUZo_lAjvktOL4kMMu0tQPC6TiiQVBrfcwpSVDRrYXT2gEjJ7TjWp1jM3OxM4mftTFz0VdBSmAFAzn3mRUfJgnp_tO6BsFcGEnapKA-1GbDmq-5k0-ZCaTdVKrxzu44IH02LepzMryjcgdyHkfJU7qdDA6O-OXOb1_FWlfAv9UrLZoymKEOqnbOgJJOVUWW0Fhzf8P-zgEVG_W5HNKAH_40jW2Dl0Cht3RSmsmHYrE9RwWRSiJ4lCEK-0QgyhNRA-NxFDrD4O3DE4ilgOnA1cicxSX7s0xaFWAmouhEpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=JeSOVEVq5Z0wWndo4qh0lDpmeSxuCYwg00Krqp-rj-dPaUZo_lAjvktOL4kMMu0tQPC6TiiQVBrfcwpSVDRrYXT2gEjJ7TjWp1jM3OxM4mftTFz0VdBSmAFAzn3mRUfJgnp_tO6BsFcGEnapKA-1GbDmq-5k0-ZCaTdVKrxzu44IH02LepzMryjcgdyHkfJU7qdDA6O-OXOb1_FWlfAv9UrLZoymKEOqnbOgJJOVUWW0Fhzf8P-zgEVG_W5HNKAH_40jW2Dl0Cht3RSmsmHYrE9RwWRSiJ4lCEK-0QgyhNRA-NxFDrD4O3DE4ilgOnA1cicxSX7s0xaFWAmouhEpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=nkvoJPW9YK7xbWjkTHTy33LkM816LLHO5qCznovAn4919cIMjOH4iDjhCP6ymDDRgX4IUss-Q6MuYPlgRDhnUemwxjlG0CiDDogdtPGUQesGENSNP31if4F3b3jELIs8zGnnpMPnQWcleh62lKhIjwXN46jC69sdHYK85TapzV4lH1b-sL6HqnU9Hl69pk0b4noAyo4q-7xw_51tCgGqdTQ_QxOhpnGh6_s85Ln4AzrVhIhHKSvpAsP_dlWz0mcVKpDK-4lHePQ-NkC6A7b9IygB3Tf2ZUvTfg0bwNK5B_AibeU4uwUZWfr_2WjNq7Bk51G324kr0rJN45D3YMbREw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=nkvoJPW9YK7xbWjkTHTy33LkM816LLHO5qCznovAn4919cIMjOH4iDjhCP6ymDDRgX4IUss-Q6MuYPlgRDhnUemwxjlG0CiDDogdtPGUQesGENSNP31if4F3b3jELIs8zGnnpMPnQWcleh62lKhIjwXN46jC69sdHYK85TapzV4lH1b-sL6HqnU9Hl69pk0b4noAyo4q-7xw_51tCgGqdTQ_QxOhpnGh6_s85Ln4AzrVhIhHKSvpAsP_dlWz0mcVKpDK-4lHePQ-NkC6A7b9IygB3Tf2ZUvTfg0bwNK5B_AibeU4uwUZWfr_2WjNq7Bk51G324kr0rJN45D3YMbREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy8czo8801lboW0w88YKUNLtzj2Zk-fF5-Wk6-AlRdLlqdurfG6zXQHiVtfLQ69Ge_p8kY7QRkg8NXhV-SzWQCzWsFfEul7bbqP7aPRk6PFN6Ge5C5WH5WGkOaezSK0fRKlkZBYtuR7H7SUQMr_eVnEu-J0_ClfMoFvsmRQSU-3QN8oC_pyWGXBShaN8UchK7ttYzBn6jNIxRVUyXsMSg9GDZ7SKEtveDvxYjo73kpc-cNzMiNmPt35NV6LtcMQlt21VBfVUIbpOqKrSUO7lpYFvjcwgM0U6HN5yIBTbxYlLD9No3pteIwBoBaru1HSyKBbrmsKR_FBJb5HMZDVwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=u4i2MukRNW6bAW34j91svQ_QJP6_hKF5-xpD6R2r8UuSz6uHNBkdYsXb-IFOezo6EZ28Lm7fyh6ESLK5J56GG6eSMcB0dynd-R0EWKX40t4XvJiZYqfjQSDpUV35ipikZ1q0DU3oe26Q-6ur3MHXkiP0o3kGhsdFJXIgf44lyoF2HNbDtJ4sdNR5t7EExlV2APEtjYumyBqHrlnrtX_kPFocH5yGFIu5_sBUFi0fhBmdKB0l5atYn6UB9j9b6ZfXJqk347SSYSQYFZw8pz6M5YyM8pBgi8jkLWDL8JtTU3VrBZaiklouth69bEXrPZMcFuZFRa5Vc2j9AKJOBqHvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=u4i2MukRNW6bAW34j91svQ_QJP6_hKF5-xpD6R2r8UuSz6uHNBkdYsXb-IFOezo6EZ28Lm7fyh6ESLK5J56GG6eSMcB0dynd-R0EWKX40t4XvJiZYqfjQSDpUV35ipikZ1q0DU3oe26Q-6ur3MHXkiP0o3kGhsdFJXIgf44lyoF2HNbDtJ4sdNR5t7EExlV2APEtjYumyBqHrlnrtX_kPFocH5yGFIu5_sBUFi0fhBmdKB0l5atYn6UB9j9b6ZfXJqk347SSYSQYFZw8pz6M5YyM8pBgi8jkLWDL8JtTU3VrBZaiklouth69bEXrPZMcFuZFRa5Vc2j9AKJOBqHvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=vh92rgGOOhZdjJsLAeVBbaI1msqTRaMDMHmUjjjIY-gXDer3yL6DAxzshdI-bLQKQJy9etvl0tg8BvYYfOryUN1LGv8pHPoRJuZgneYaa3LsrvtiimeBU8M-o_-T_ZrHpZ1Fs4pOudeAEYxYxdxsUmLk4k2SPV4RlE8puF-u6yiyl1FxfyRHQurgHTdsx1rSW4CcNBHOeCewXerGvNlj3cjertgYsBQAzquDX35h0zbrYnJfk5rKzfTjKzpyZLZS-18o5i8kLAF4sIJQ2__1gysRzLLlDoe1-DfARXVmeQYoinUYNedVhqUp1L-w8Z5ou23RBLQdCURump3IUjUsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=vh92rgGOOhZdjJsLAeVBbaI1msqTRaMDMHmUjjjIY-gXDer3yL6DAxzshdI-bLQKQJy9etvl0tg8BvYYfOryUN1LGv8pHPoRJuZgneYaa3LsrvtiimeBU8M-o_-T_ZrHpZ1Fs4pOudeAEYxYxdxsUmLk4k2SPV4RlE8puF-u6yiyl1FxfyRHQurgHTdsx1rSW4CcNBHOeCewXerGvNlj3cjertgYsBQAzquDX35h0zbrYnJfk5rKzfTjKzpyZLZS-18o5i8kLAF4sIJQ2__1gysRzLLlDoe1-DfARXVmeQYoinUYNedVhqUp1L-w8Z5ou23RBLQdCURump3IUjUsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=PtuC_xc27oSUnYn_-NGLYZw2QwfrK62sTTsSrwCKW0-H_O-I7f-iETLnC_zDexDrA4g2yeNri4M-Av9jLtPLroBNYO29fI3WrD1r_LorPcf98vBBEvas9EEsrl2NGeYLNMb1isuhTKsWyKMToasxe2xe9xrBxk1HmX9YsDPfYW0Ebo5BLm3f9wX0bngvCBSLo15jtzY4K24UetsYP6RZBo2cxnx3CnHbi4yPHPMWWmh5G-7fqwYMjdvoYv65YE4M2W1D21RnU30Cm74-0AP6Pt1Ywtlg1PC2XQOw6WGH2IuWFvRzp6l_8S3Rpm_C-_-6lB9g859J69eUm_8gRaQVIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=PtuC_xc27oSUnYn_-NGLYZw2QwfrK62sTTsSrwCKW0-H_O-I7f-iETLnC_zDexDrA4g2yeNri4M-Av9jLtPLroBNYO29fI3WrD1r_LorPcf98vBBEvas9EEsrl2NGeYLNMb1isuhTKsWyKMToasxe2xe9xrBxk1HmX9YsDPfYW0Ebo5BLm3f9wX0bngvCBSLo15jtzY4K24UetsYP6RZBo2cxnx3CnHbi4yPHPMWWmh5G-7fqwYMjdvoYv65YE4M2W1D21RnU30Cm74-0AP6Pt1Ywtlg1PC2XQOw6WGH2IuWFvRzp6l_8S3Rpm_C-_-6lB9g859J69eUm_8gRaQVIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=ez-ZAnPPi9wvVdTHnkeY3i4nYr0Zjn_OmODqPewM_rtk_Zc1EQDK-TuJPVx-uacIwY6FSAm3ySxKllc1TK3FcN6Iqb7i8EdUzFaWXpS9kktCzZoAUbUSOSxGh1P-aJWVXOVynk0iA4YdMXrDxTdh7I1-cwe6Gwfw9QRzfBR-bWMZ51tfij1W8GqyQHAFWUXk1tIDEMQrkpPO5TCbXOvwuR8LEura3sCAqAw_FliDpfV88BKBIcrOzZZmge0L39c2fSNRSu_1eRvHw854_WtdCUFYgxz8bQjRZCTwg4VkY1FZBENG-7GLCszd2_6LK-HCmAqEjsU1quvTgQFCBijsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=ez-ZAnPPi9wvVdTHnkeY3i4nYr0Zjn_OmODqPewM_rtk_Zc1EQDK-TuJPVx-uacIwY6FSAm3ySxKllc1TK3FcN6Iqb7i8EdUzFaWXpS9kktCzZoAUbUSOSxGh1P-aJWVXOVynk0iA4YdMXrDxTdh7I1-cwe6Gwfw9QRzfBR-bWMZ51tfij1W8GqyQHAFWUXk1tIDEMQrkpPO5TCbXOvwuR8LEura3sCAqAw_FliDpfV88BKBIcrOzZZmge0L39c2fSNRSu_1eRvHw854_WtdCUFYgxz8bQjRZCTwg4VkY1FZBENG-7GLCszd2_6LK-HCmAqEjsU1quvTgQFCBijsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=erCEnHAoVV0kwZf5mDNP4Po1yz3fp3bcZ8YkLxu3EmncZOb-oYuPSp3uzyxayR3JlmRq6PYurnu8AU6mdhvgQNhg2S-Wf4NwMSPyzSvRvl4ER-OIMNJQfZR7a4ATzOaG6LUrkl0Ov-Ab6a4Y3Yq99QCRzdnybCZo9DjoT0UjlHIXY0_AFMcGqqOXH1mWl5ATNnehMjwXL1rpgWOPAXOYxuniMSJh6de5xFsTNsAGWIam0540xKmQomObQRKO4-nlfYT6T2P04iPrFLFI4TWzTdq01-n8igKowY56u_XRqiMfDBS0Lcmxd_FS8DKN8vSxFNjZ0Cu0uAssUlCwnRlzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=erCEnHAoVV0kwZf5mDNP4Po1yz3fp3bcZ8YkLxu3EmncZOb-oYuPSp3uzyxayR3JlmRq6PYurnu8AU6mdhvgQNhg2S-Wf4NwMSPyzSvRvl4ER-OIMNJQfZR7a4ATzOaG6LUrkl0Ov-Ab6a4Y3Yq99QCRzdnybCZo9DjoT0UjlHIXY0_AFMcGqqOXH1mWl5ATNnehMjwXL1rpgWOPAXOYxuniMSJh6de5xFsTNsAGWIam0540xKmQomObQRKO4-nlfYT6T2P04iPrFLFI4TWzTdq01-n8igKowY56u_XRqiMfDBS0Lcmxd_FS8DKN8vSxFNjZ0Cu0uAssUlCwnRlzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHg13jftPBmXDdiFlyajH6HNG-3r49E0zc9M7XSvQVrcrMGaRvcmfNwlsBqRgaWuEy4buTKxWmLaztA3r0tQ_nKJKE8S65D9RiGWSGY1fSG96KC37ufvfjUy9xqrM2BpRQD5KYt0Vbmn_q7XZSsJe7Ac6K_UZ2vTp6JX3wUn14X3i4gXHmKHUKOGVOKuIbsaroh0hrR_g4AtG_6W-bJKSGKmmpNwDKPSXuHK1MdGAyQtaglfYBqX7yitmGE3AnfjkmFAsLj3P8uDPJwxLzX4HiK3YISFr14nXKlFjwnwV19lOvMxYKmYk0ahRTOuj5C1q3QUldxkA-3AsdQdchklVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj2eDw5rsNEWfuQT6dQZ4QB-w1mO8N3-lOm77QzYAGoBaFUKF9-1IrpygfO-dxnklWuAlDkO6PgjXMQSSVnhIA4uXds-zo_wIXDjPn9M10eWjpM6xoZsDAz91aMTIwuLfzg7Ji8KTf2VJybJKVC9JE4GFPx9wbMn7wrREgmkldm2cHLIWT_RD4WKYX650BsKrWKDyUkS7rb9ScgMy7msyvhkhj6IxSObHeu2DtiGC51RDBxdFBq5SasedC994lcZ2HqLaPb5VQNQO-w74uNQ6HvfWdN3LAyg1EQSjEElVDo1i6bId3_asMC3_-ZXmonaMJ3nDdEY8QYxBN65Aj85nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-L0Lc5cWrKiVev1OF2bgP5MXbpCbCYjg71-vUqvIo7mbEPUUagH0oxe4OsZtNNTqRZuRVv6Lo4J9Nkx-oaRZHaY4o4oZqnXeqzXWbzrXAukZQR-ekTIai0VWCXyKuOUHDaIn_p6Hg7nR3VTSzIjcfpYTlvTbz-YWe2oG4NhHC_ZcLr514wLKkfLJzwAHPBJpsFbybRxbs40MablGSxj7XG2aQj3XXgC5G7mt3xCsh_1NF0K3oSnPGGMZPi7Z-EKjXa5Hq1O4g24zrYknnMt2D92IpZBeLkQdPyUlrfnAO9OAtpBHc3B7AMQY3bIrhoPkWlmX45ASAIX2CPbs8RPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=h9JHXKFRJG_f2I0UM91W4qENWD_xnGNr0t9X3d4xwom03mqfEYuv-kxOQWL7wldox2PF7cT3c2HxXSdsCK0NW8ELtIPSDoX2kNDQ90UTZrXVD3SPWFSuxOR2XksjVGMP9F3jI6fLj-cwdk8ZDM5cS1VYu3wJlYLCYTmK_RM5AR9ur_BEVGzypEldWSA5qe1EKqAWdnrn8_QIcusrKuMeL8Ofr7A_l62ouViOXzNeIGoACNHs8ZEhE9U6IV78YtWM2epmfXX2ff3EZfxg1EK83awWx1LL_eLjV3dhvmEQy58WYQ6vF7bC1Q2xhctBi_FurO5211fYAjO8UGNXbIPOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=h9JHXKFRJG_f2I0UM91W4qENWD_xnGNr0t9X3d4xwom03mqfEYuv-kxOQWL7wldox2PF7cT3c2HxXSdsCK0NW8ELtIPSDoX2kNDQ90UTZrXVD3SPWFSuxOR2XksjVGMP9F3jI6fLj-cwdk8ZDM5cS1VYu3wJlYLCYTmK_RM5AR9ur_BEVGzypEldWSA5qe1EKqAWdnrn8_QIcusrKuMeL8Ofr7A_l62ouViOXzNeIGoACNHs8ZEhE9U6IV78YtWM2epmfXX2ff3EZfxg1EK83awWx1LL_eLjV3dhvmEQy58WYQ6vF7bC1Q2xhctBi_FurO5211fYAjO8UGNXbIPOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=PMqss0hMaMGUZeg9W5SRhl1sPchBT8zMuR3RAX62wNqExQ4cBRYB4J0_cNkxiuirxoNW4_XVhiqbJu_sNDFo6xAt-0tJGYqpvNFxCGlDnHSIAdrYAcXxGCVAeweXhtlW4WG51rKzpsHZwIp0l5zw2XcWJvW0TnzvBm-ZPbuIY17MFgr_QtQy9dN_MWrqjwcf0rJUylxnR1kq7N4RntbASdjZc8cG8w_C-tl0kfZYcHSv245Of8eRTgFEqL_3d7Ok8wYmPoJjB22XbqfXRTU7Z22hFFAlGFuW_91r0iPAg7cB_WbihgVbyWLC6arFasAxQxCe49OM9diGxmlrVa-3zJk1B52AgyhvZk0SmwV7Zr4cvlOxmKKrElC2DhmPU5aphJNv40VSbdzece7FxWIUTA7zM2ZdfWx5XqJwqbgOKK2UZJF_VoKnAis15lyhN7FckkqudE6QIf4oSw26_Gj7qGu7x08cCUoxxLQ9dQFe-nONWBnM914qAV01TpXWJznKZiLDlt1c8V3S3P8_X1S-J5IvvBprVu3HwpE-Mt2Xfik55BXUEU24spKHHDHHqepnZQKkjA8RsO7638xLqXUdZMulaSJpcEuOk0Xe31OG03IhPqVRMnInWNwaw2kvnzEwZeNI75Glxp7KsDl75CDYa9CizzLnMzr7KqcvYWZxrRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=PMqss0hMaMGUZeg9W5SRhl1sPchBT8zMuR3RAX62wNqExQ4cBRYB4J0_cNkxiuirxoNW4_XVhiqbJu_sNDFo6xAt-0tJGYqpvNFxCGlDnHSIAdrYAcXxGCVAeweXhtlW4WG51rKzpsHZwIp0l5zw2XcWJvW0TnzvBm-ZPbuIY17MFgr_QtQy9dN_MWrqjwcf0rJUylxnR1kq7N4RntbASdjZc8cG8w_C-tl0kfZYcHSv245Of8eRTgFEqL_3d7Ok8wYmPoJjB22XbqfXRTU7Z22hFFAlGFuW_91r0iPAg7cB_WbihgVbyWLC6arFasAxQxCe49OM9diGxmlrVa-3zJk1B52AgyhvZk0SmwV7Zr4cvlOxmKKrElC2DhmPU5aphJNv40VSbdzece7FxWIUTA7zM2ZdfWx5XqJwqbgOKK2UZJF_VoKnAis15lyhN7FckkqudE6QIf4oSw26_Gj7qGu7x08cCUoxxLQ9dQFe-nONWBnM914qAV01TpXWJznKZiLDlt1c8V3S3P8_X1S-J5IvvBprVu3HwpE-Mt2Xfik55BXUEU24spKHHDHHqepnZQKkjA8RsO7638xLqXUdZMulaSJpcEuOk0Xe31OG03IhPqVRMnInWNwaw2kvnzEwZeNI75Glxp7KsDl75CDYa9CizzLnMzr7KqcvYWZxrRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke_nbdiTpzzqUGH9GJXMYI8NT8RcK0lahYxqzf9lhEADT9JizNrNArWU5flmKoxYzV8hALQI5ReT9QaaPMrw4Bz1w95Wo9XiG-qylqnKft7DhEtDqJ8nd8aqULUP_y7m21Qmf7kvyjJiwkyU5yVgseDr-qTk9cUCkBpe-Lc-agSCkfj3CI1wI-TOCJHpIuHuM5CKNQGSfwGWvjk3Ox9jhB5Ni-F1rYIhfsRZeshKjqhzAa31FaqVYTdl0H7FF6ArevOZ0GTfle73N_RJzauFJoIPbNVodIGdiZhUusuydaTsYqvrzekDy-WjNRFzZqUKEKWd7g1EOkKURS5fStAIfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gugz9sG_kYMtlloHloq-KoEbSZ2Y2zzsv12180_YZfNt07liSG73xVwOp_vxcM-Ph7DTsAWI5wSCJJtzYdxp7z94IUV3D3tEdMCi4pJ2NGtdMgXefyOM973XSVcS5sqiza9c8bNXoqzZ0dTy8IXKI49xQ89Gd8YqQ-b7usXwz0vZ3eUp6LrI_eX3eqhmNpNXKxgVRXWsrA816NK8md2MJEhwSi68Vq0OngTpbJOpcJllfxUiv6KU9dPu040SFJXuI_tDkowvskHkajXm_5pyyWAbkXKe02yk1r8jSnSxAkO2Fi7WV83zqzqQRJNGORqeZiUqs3x9Z3QnsT2u415hlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOEx2uaK4EXADQqhiZX1MCM7gqiZVyr5JDu9G1hTXV4Hmsvl6U9_TUtH3IjV6YLTqjvwtbFYtPAWh9swVmRdmOAYHGtQ9LdBSH5x_WrGXLTNwWzSHEcDXHA3TFPlcw3f3D0nuJL8PTJsiG2XRE-iOyCJ760RihRLb1aTlmMmkaLfrApCbVzyXhJ3c5eH__SHkN8rqlxBwFSWkkTdgsX0vdEkaAg8hQgPILVx_tFUVGfwovcaV-xnMWZwp6iTGd74Tw0d5wJCAQGzhooFJ1rmbIceumN8XAyknPelml3jy-bFPd32eorv6AqVg6mVvYa1DujcRFSaWL9DB47Ewy2okg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=QnmYIlQOhf1vzwA49U5-7aDMtTSGR9xcpjZukGIj2qBSJ-7l07nJsSbhQAaeNc00RGm_Opp4Wps8UIfMkDXSriwxvfqNuU9pl8sPDEyPknw9ssiumUV8Z1YMxHcX5zaqz2s5NGRQN0X248Xwx7PS0_QvQTu9_Qo0RBflFla5jJSjVl-0T7MWf9s0vOSm9xCwKzkjUhfO8UoqF41oFC-VchuiuJ0KUv2MGQGlLODzeyUd1suPOfeBnl5H-U5hDgZJKzWACww4AOeeVde87nMnUPpVQ9z1AYRnBxiNhm8yl_qXDANnBMJAcwYFuBSmbU9PwwrZfNujj1wdJXnvWgh-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=QnmYIlQOhf1vzwA49U5-7aDMtTSGR9xcpjZukGIj2qBSJ-7l07nJsSbhQAaeNc00RGm_Opp4Wps8UIfMkDXSriwxvfqNuU9pl8sPDEyPknw9ssiumUV8Z1YMxHcX5zaqz2s5NGRQN0X248Xwx7PS0_QvQTu9_Qo0RBflFla5jJSjVl-0T7MWf9s0vOSm9xCwKzkjUhfO8UoqF41oFC-VchuiuJ0KUv2MGQGlLODzeyUd1suPOfeBnl5H-U5hDgZJKzWACww4AOeeVde87nMnUPpVQ9z1AYRnBxiNhm8yl_qXDANnBMJAcwYFuBSmbU9PwwrZfNujj1wdJXnvWgh-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy58bPCV3AglgcSGhF8OYyxTbqwSTwgugfmQjubHpqB1XpGcnNpzUp4Gz7tbW1rWOKKRa2jq903GP_x0qzUiLuqABDrMYgUFE6gy4XTmoqyxsAw502UstnZP5XwEl-3je_JvDPH7D60DlrSw0vAwlrJiybMTKCsf91v4JBk2eDk8hEOZ7HwK4UINAJFFnKGn0fkaOetRbft9Rc1w-YwkfWGfV81cC_QSy5fmBuCg65dbVdzT6-oTQiSLuSW71YkVgJHujp8KFtmgyCyPMbWplJZmPnsP3JBL6EnemnYxWeF4hQg6BQolYT1NCnpJ4Qxr3F75-ttmikP9N4GaK61DNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=oZvFQ0alRQecO1xVG6lwqOxYLfYO-ipGimVP8Vdw2vyFCKOFzUtSPKKxrOSee3EwogsyZFLW50zgimlWI4Ukb4Qp72n2W_UUXp6bj7GQzs_FmlhVOrZv7tUYZzz_npgCwBdlNrfEnMbmew7T5SsBZFhLKK0lw5_DHS38dJVHRPMpa33uD8ANy3k172E9acAzY1xMKfsgaARcPsr8anhX8QLbj_mWfkmV4CGO23-tiUFAEqZVzLbYxZk2yufdxgolCv1AF9ou0m25zL74HQRBAWw0hbc-YURrF5acd_SwQHcGqUiN7vo0jsl9OX4ULstORAAHaXDLiYxm1IBPDw9haQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=oZvFQ0alRQecO1xVG6lwqOxYLfYO-ipGimVP8Vdw2vyFCKOFzUtSPKKxrOSee3EwogsyZFLW50zgimlWI4Ukb4Qp72n2W_UUXp6bj7GQzs_FmlhVOrZv7tUYZzz_npgCwBdlNrfEnMbmew7T5SsBZFhLKK0lw5_DHS38dJVHRPMpa33uD8ANy3k172E9acAzY1xMKfsgaARcPsr8anhX8QLbj_mWfkmV4CGO23-tiUFAEqZVzLbYxZk2yufdxgolCv1AF9ou0m25zL74HQRBAWw0hbc-YURrF5acd_SwQHcGqUiN7vo0jsl9OX4ULstORAAHaXDLiYxm1IBPDw9haQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=HQ8jgAZqJBGFxKfMXEmRBI2jC85-bLwIStaahufL5cpL5JrPIe6wqwehSWlKnHIqo3ubYCVs8itlCcvrTUaYCTOeBbEXiRpkQfGMdQbC1j6x1XJNk-YnB7Pdoya4eKTu2kHiZGOhTzsiQD88c6KzUU-7EnSbALUgd8YbBnypf9XiOpKxFbYUR52oabu4AK1PbWxV8CiL-hE1aPDBzKHobXZIfWy0hiZx5pWqXbop3W9PjGqj5h--RhuKCt8HKEeANXHHvPsMSVlOLxMzbMxY7dexSRoVpGWq3kS-UGZj96QcB6LYY2NP2V_8mCQn-XsaEbntxkXciSdZqbxRA4YhKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=HQ8jgAZqJBGFxKfMXEmRBI2jC85-bLwIStaahufL5cpL5JrPIe6wqwehSWlKnHIqo3ubYCVs8itlCcvrTUaYCTOeBbEXiRpkQfGMdQbC1j6x1XJNk-YnB7Pdoya4eKTu2kHiZGOhTzsiQD88c6KzUU-7EnSbALUgd8YbBnypf9XiOpKxFbYUR52oabu4AK1PbWxV8CiL-hE1aPDBzKHobXZIfWy0hiZx5pWqXbop3W9PjGqj5h--RhuKCt8HKEeANXHHvPsMSVlOLxMzbMxY7dexSRoVpGWq3kS-UGZj96QcB6LYY2NP2V_8mCQn-XsaEbntxkXciSdZqbxRA4YhKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=OrbAlK1-UCdfJktCrNIqTNwnKuNjhqSntgDPgiVpbPzPxRdFNd7t3qbjuKhPERWLCSUlu_0j4BxqhqKdVVSPmmqb7hzNKVxOvUPuLRG-P6ea8YzMmoCtU4U9zDfdZ8UBmbUgH3yg3yGlr1-Mz5a03aZahI47uhDIlyoptgEZ2R-A-WjknEnSR26ItzFjC99lZQMugZW2zXiJ4_E_np5c3PhDPBN0OhPP4pMYlVzlNpUSU6XRGvY4-ixdXxZknWe4dcycMAQoShh0iKUFm-J9MzWBXsUVrGSX6_nKtWeJJxf4rHMjBdyMSz5oGYE_YdIQj_KeNMGhiW6nj5m6cwp9fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=OrbAlK1-UCdfJktCrNIqTNwnKuNjhqSntgDPgiVpbPzPxRdFNd7t3qbjuKhPERWLCSUlu_0j4BxqhqKdVVSPmmqb7hzNKVxOvUPuLRG-P6ea8YzMmoCtU4U9zDfdZ8UBmbUgH3yg3yGlr1-Mz5a03aZahI47uhDIlyoptgEZ2R-A-WjknEnSR26ItzFjC99lZQMugZW2zXiJ4_E_np5c3PhDPBN0OhPP4pMYlVzlNpUSU6XRGvY4-ixdXxZknWe4dcycMAQoShh0iKUFm-J9MzWBXsUVrGSX6_nKtWeJJxf4rHMjBdyMSz5oGYE_YdIQj_KeNMGhiW6nj5m6cwp9fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_j19lq6qaqsstdPAyBVUZGraC2LCE8-NZsCZHyIPl4gcRx8A27eW56IC3FmvOuyuhTBHmpaAw1IptRhcnc_abUIXxmsXaExu4mLKovk5a_2vmcuF_39j-oWsXh1mhBMvEA0fKPxWX7cyaR8t79tBFeiE0ffuG34XcNAHTz4n_l3Isz_Av1WvWpz8W9ZMt52dNwZ7HF_1hodO5pHcy25KDJXSho7zh2s4bZqDlxgf7B8j7E3V96S299TCBcQROmRf74l1VFhFpIlkLa74eSPwG3qlvkprOuGcTVPfGlHM07GMkNFOv7XI-erN9NX9ZAZVu4n38G85Ff83pc_rvn0Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=jKDp50zHnDNUG0CBEsKgpz4WBVLCSZL6bZSRn_pSvGWl9CDPhSDJzko9kGRmubBr3D0jnECF53hXrgDpBUDsjW5KYbK7j51LTOIGDedLBaSpptEO3lZMCYj33jMk05mkpcAJ6QTwYHLtxytoFAjykieBeG7wHP_cj8cCy_vR_2wQBPfYoDLDTTX_eKKlz9yQfwUXfA939ACwZaTKE01POfK4gfTq0fUcn2hDKDaMXnYhmUmKCZlvPJ1qJwESYChgCB2TAyDDTXRMsXCfXSrqgpAeMRvN95czb01HyRuTFlXJmULRB7rJ8Qm23KpZ-C2AwW7ha7P6uoBe4AHWM7CDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=jKDp50zHnDNUG0CBEsKgpz4WBVLCSZL6bZSRn_pSvGWl9CDPhSDJzko9kGRmubBr3D0jnECF53hXrgDpBUDsjW5KYbK7j51LTOIGDedLBaSpptEO3lZMCYj33jMk05mkpcAJ6QTwYHLtxytoFAjykieBeG7wHP_cj8cCy_vR_2wQBPfYoDLDTTX_eKKlz9yQfwUXfA939ACwZaTKE01POfK4gfTq0fUcn2hDKDaMXnYhmUmKCZlvPJ1qJwESYChgCB2TAyDDTXRMsXCfXSrqgpAeMRvN95czb01HyRuTFlXJmULRB7rJ8Qm23KpZ-C2AwW7ha7P6uoBe4AHWM7CDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
