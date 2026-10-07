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
<img src="https://cdn4.telesco.pe/file/ZgSC30HvIyvhDsv_lxGrRByua-BXWfGCrtKuD57wpkjCE0prJdpLMEW1c740U9e4yjNvMQwhDoIYxp6cHznwaINshV1gXDJ01OEGlEKG-0ggBkSAaqZ_hPZ2lpFMp3yg1qOltv8DS-5EE3hRAL-6iDhTmnFD6-K3Gs2EB4RsDXdlqU_ZPw-fFUASlAlvTIzx305BLOyayU71Sz4qdxD39hr9maGzthtZzbq0wJptxmTFdAaL7P2-cn0c-99TKyAe3zEAr8lG2bwaJ14zgIQuuAY5N6WesAlYlygW_hEOJDihzc36WOTZNBJFLpjxa4cReyqtz0wZF2_1xvss9Tz6Bg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-466939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر شب‌ها خوابتان نمی‌برد بخوانید
🔹
بی‌خوابی یا کم‌خوابی مزمن، سلامت جسم و روان را به خطر می‌اندازد. فرد بی‌خواب دچار خستگی، کاهش تمرکز، کندی واکنش، تحریک‌پذیری و افت عملکرد تحصیلی و شغلی می‌شود.
🖼
به‌چه‌کسی بی‌خواب می‌گویند؟
یک متخصص اعصاب و روان: بی‌خوابی زمانی مطرح است که فرد دست‌کم سه شب در هفته و برای بیش از یک ماه، در شروع خواب یا تداوم آن مشکل داشته باشد؛ در چنین شرایطی، پیش از هر اقدامی باید علت بی‌خوابی مشخص شود.
🖼
درمان بی‌خوابی از رعایت اصول بهداشت خواب آغاز می‌شود
:
🔹
داشتن ساعت منظم برای خواب و بیداری
🔹
پرهیز از مصرف کافئین در ساعات پایانی روز
🔹
کاهش استفاده از تلفن همراه و سایر صفحات نمایشگر پیش از خواب
⚠️
مصرف داروهای خواب‌آور نباید بر اساس تجربه یا نسخه‌پیچی خانوادگی انجام شود
🔹
قرص خواب، در صورت نیاز، تنها بخشی از درمان است و جایگزین ریشه‌یابی علت بی‌خوابی نمی‌شود.
🔹
مراجعه به روانپزشک برای شناسایی علت اختلال خواب و انتخاب روش درمان مناسب، به‌ویژه در موارد طولانی‌مدت، ضروری است.
🔗
مضرات بی‌خوابی و خطرات داروهای خواب‌آور را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/farsna/466939" target="_blank">📅 01:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0accde21.mp4?token=tgHWxxqd2R1CzDf9NaU3RXk7s_JdG3iK9-p82wGq3B8T5Y9NBu3lw3IS_E_L0xXTRXZiLqB3MyNNNSJUwrzseot_0pNEcDmUa6K8MN5zYMVvl5yOxhAiUiuzxNaLZK9eT5PSBLYQ1xg3qd9hOYIEC6jJ5V4dwmyol73WFr_hbb4PvkJo5LJ7oAQO0XvIdl4EUS1ay1yq7Hk1YG5vs2nRDC80hNMoaLxV7T-xYj4J89ZT-4Bq69MQ2XnS2pmaRH7JTdEvgQGo4DIs8b_dYY3Aovel1tHGlaXZ1SqpTavhIIccYJ7T1-povHuxwCMSmn4ZxgJa6ICHAjf1C-QP_l_eQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0accde21.mp4?token=tgHWxxqd2R1CzDf9NaU3RXk7s_JdG3iK9-p82wGq3B8T5Y9NBu3lw3IS_E_L0xXTRXZiLqB3MyNNNSJUwrzseot_0pNEcDmUa6K8MN5zYMVvl5yOxhAiUiuzxNaLZK9eT5PSBLYQ1xg3qd9hOYIEC6jJ5V4dwmyol73WFr_hbb4PvkJo5LJ7oAQO0XvIdl4EUS1ay1yq7Hk1YG5vs2nRDC80hNMoaLxV7T-xYj4J89ZT-4Bq69MQ2XnS2pmaRH7JTdEvgQGo4DIs8b_dYY3Aovel1tHGlaXZ1SqpTavhIIccYJ7T1-povHuxwCMSmn4ZxgJa6ICHAjf1C-QP_l_eQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تولد یک‌سالگی کودکی که هیچ‌وقت پدر شهیدش را ندید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/466938" target="_blank">📅 00:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3BT4odGdRhoJSTql3hIPGrDPPUdibACeyeNlxSFXuaXoWpX_ZM40FyqcRCccQh1BGFsFxrMR1hksEXBufrpfv_Oyjqvn5V2MtAiq0O0-qzsttpWfu2J-oPBY-lpw-1bxQMoNN_-16RXJWhrvRHomxk-tIEU6sUsbse32OaXqfzPmw__akwyeDY0-cRajHS_VL3Giav8wWf1xjQVzRUbRxmDvMkLJPZ_qZWDUn401bLKAcQzBF3aYyW7HtK105a1RL-6oEY0fGoJN_IEofmwJ6NXgyNgbBbaHusxxkVh2KMKaqkvZ366-1QHN5DK5c1O9fr8FKLdEjEEREGWa822bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-W7HSKQHY0klnwdx20gn2R_xT80p6xOnWgUF--X6jieZ3pkvZNtXMfGcj_Q0pSK34acgz8gXuO8qelsivcHtlHBI1vg75qkF3zIJMzO5dgdP1IzLssU5Q6-eCWWGbgMNOWwU8JCXvLBe6rGkQgqFvT3hf8Wf1Xsfi3V2gkoYjyWeprmLbt_M1Er_xa3Eb8HmYsAJ0qQtqOfu3avCVnZySPKSbY0I-Qe5fxpfI0R2D3wB5NOTzk6jjh3dUF-mX5Hu-Msvy2mUQIu0eZogs2xlaXn7crb6FB_4gmxMs7JpqUJUnT9rvcDfglx_Bm8gbZs6j8hOQoWVv5j3BrVR-ILYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXb2xPMo8jD1Jw0y3VKI2gSzYflCkITW3h26JHKXc_X2nzoBE_VkM-CWgsQrcZ8WhxHK2wT3F4f5cRWNXvMvGpukFqmwU_utLjFpw-cawBtxvmhDFLC01lixOwLjJUGqH5dELUrdOd1tPXCy_0a4jVyzg42AbePuHLFTY7SglnPTuGlmw84t2yvjx2tFk1LFJBlY_viF5nEAFwDX5dvk_4IMIm0dRr0Z3kvPGHdlaNRBQTQwtP6ChQufAyOU_oBAs9iXPZ636wz73W3lPMyb-EJs-Wx-vFiawhTkHdis-01e_xmYefidnH-MNhA1P9QkD1PWkAHSXHSPRIRLfiaL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvZT3e1f2WtfwpUiFwuv610i78WUt7jza6sGWySHNjfB0RPrjYeitfSoywwaxqTMzkJWhikfNy8bM17tey3ftiotR2nLXTkB1h2WcEz5GusMCLnRjjaIaVEG43TJVpqFCn3cFGe0N-zFAszaAYEN5AbmrQCewP7jN1OCERNR7PkGd0WZbU1Q8RsoyaBEZJMxRDVh7akxalM-ctGQ8u1veW9SrI3g0rTnuKNAjCK6_AWdgfSIcF4MW8ZtH2xlZpROg31xJHNPjHvKZsO694uD25cgnCy-733Dfx70yJBzrJONFg_Lt9noYYQsXyqhPOo1VHN2q_yVHoCCtyUS6orguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4J4FdQUiIm8Fx25mhRHYOCh3_Kc1JCj_MVfVPNLxUC4qBJ2KSE97bXcppFZFzLoDgUY5IdwxmFQlvcursxaNn5oKXCLsSbwALwrS3hSgJG8C5UUHDCkkZTqI8S83miPEVEtfa01bwU7KU0vCaaztYTIu2XL3K_Ermc-eoEfjrtdvfXtR9Z1SVwBFSn1LJ5bMvuk4TczT09SmDGRECNr7kHTTr25rPC3O5z317ta2jU0xk2-NkwGZgnSSHL4XimXvYZAhmCdHC5wUARmKBXXIIheHToSitMj9sMQrbJARc9w2WA-lYtTbwEII6e2c2IcuNMBpChnmtRX6Fqxnw6njA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0c_P3jrevkbM66a65zK_xsXuY6up_vTmplOfxMgxo47dx2Y7XqaoD6SsBhRDi23eLqkGZGUuNaTvTOaxOAwbKlDrzSyurxXYmyd09lWh9myn9Kri_zf-dJbtc_xg38TprDoZF-fmw0nfkHrbpfibe4xzH3mDLwQGFjUV9ey1KsZNW76k_xjQmkC1rpMDsWl9zejQJBoaUhrgg2w0TJJ2EfXaL7IFS3Gs7QpEAbzSbrILMiFnc9B7APsLSBsyDvsuFd_7CkgQNwDRntMbuALVIIgF2eonav-qvYa3uynErPVarCDtLUlAe7bQdytd-qFvVI01OjnZbSUk2_qQcgAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csGo7z5Vn8CMqwPY_EvLj-19hWKCUQJKm_KNg9FX-bjAC27qJLgy3qwHXounFw7QENhSi8S1hRDTLUriN-JCraj8G0g46AOIW86M3ArJqpMmjMQ3gMW6C7hcYT7rhFJR9ZOCrHNmKNTcnduyNBAPx6s5C6_CNMy0WZNfBKKxmNradKg1NwwaBEdtZxhjtiup9uhr_3dthz3LGvijyp1eFbzy8oLts2PsmEzCeSyr9WkbpRgqdzSW1Rpcf8H1WZx5lNdHkVAajR46ihutMJukw3kxHLVqSM6lHYqMoP5hYuex7h-a575LY2kTRtfIFxEPpNoH8kUfuN3H-nDLlVsA6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از سردیس شهید سرلشکر محمدسعید ایزدی در میدان فلسطین تهران
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/466931" target="_blank">📅 00:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCaPviWdUkoJ6NAvff1PuzLuhqfFhN7WmB7kSp9u1vcmUbzrgWy22VkjFGqVTGieZTMT6pT_OhMGThc0vOnwAlcjLdEr4KVkR2AKItQ1xtjlUTuum4dpdSVoDJwY5g7Y077W__plY4z1o-5uQagIVqy1NqSVj3VEgH0F8AiJkichZZRzUBzB5fUQ-63qnjatoucPB9m89A2Joj3ybUzX3BQeE7X6Yn-1gvSjC0w6_B93f32Kvh6jHH4NTq5eqTNJyXb-tmY93u3vsSwpAHhWbeg_ZQFdHCHRMcut6MeIrvV0TFkPDrBcx-ukTyR28V4IU_xVn1uzyG1Ihoa6PfGnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبلِ توخالی
🔹
روباهی گرسنه در بیشه‌ای می‌گشت که به طبلی بزرگ پای درختی برخورد. هر بار که باد می‌وزید، شاخه‌های درخت به پوست طبل می‌خورد و صدایی بسیار بلند و هولناک در جنگل می‌پیچید.
🔹
روباه با دیدن جثهٔ بزرگ و شنیدن صدای مهیب طبل، پیش خود خیال کرد که درون آن پر از چربی و گوشت لذیذ است.
🔹
با زحمت و ولع فراوان پوست طبل را پاره کرد، اما وقتی درونش را دید، متوجه شد که کاملاً توخالی است و ذره‌ای پیه و گوشت در آن نیست!
🔹
پس زبان به عبرت گشود و گفت: «فهمیدم که هر چیزی که هیکلش درشت‌تر و صدایش سهمگین‌تر باشد، فایده و خاصیتش کمتر است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/466930" target="_blank">📅 00:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVQ95C8TbI_k5VN2y69DOIFsYz9YE8ynTPvjLFgwsU0aLMuu8RoGY6iFur52_pcYOG3lw2I0sWpoXkQj8g9PwcQ1SlgfFVjQnDnCN68_EviW8o9KWmIZHymwtW5P8H_FPRF2SQ6cU9nWJVchz4XamnPHWGGg9qmRIHSm6QkHQfmJdhEi7FRQnKSmMqhkLtNI4qM20Hq_k524Xo7zLe0kWU6F5dhTmQ7BH1jqGSIl6Mexzoucqylps20MKF2Gijui4x-XxqNq6uFRkOLy300CMDEj5en2oFCW7-fUrGXd67EFpnLIveGKbaZmFKLzU-xooU7JLp4gzGtg6o7fVm_RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعات حساس جنگنده اف-۳۵ به دست چین افتاد
🔹
بلومبرگ: یک اشتباه در روند ارسال قطعات جنگنده پیشرفته اف-۳۵، باعث شد محموله‌ای که قرار بود از مسیر کره جنوبی و تایوان به آمریکا منتقل شود، به هنگ‌کنگ تغییر مسیر دهد و در نهایت به دست چین برسد.
🔹
محمولۀ موردنظر شامل دو قطعه از جنگنده اف-۳۵ بود: سایه‌بان کابین خلبان و درِ محفظه تسلیحات؛ هر دو قطعه با موادی جاذب امواج راداری پوشانده شده بودند؛ موادی که در کاهش بازتاب امواج رادار و تقویت قابلیت رادارگریزی جنگنده نقش دارند.
🔹
یکی از مسئولان دفتر حسابرسی دولت آمریکا گفته: احتمالا چین پس از دستیابی به قطعات تلاش کرده با مهندسی معکوس آنها، ساختار و فناوری به‌کاررفته را بررسی کند و راه‌هایی برای مقابله با قابلیت‌های فنی جنگنده بیابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/466929" target="_blank">📅 00:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7pFOrZjgADvxwoyYxzeFXth6IClh1zbtBLfCTv8wdAp68SVGrvU47uYVBzqSAbI8uxfOwR4EY0CYaqpOuL3jpuH0o6VoDuFERYiZDCRFCNmQijigHspYandP6J9tur0dtqNiekXfAfhaWt3S8c7ZPGQNHQ404ctNR8448zdfxMyxu8s5DFpUIwGsdwvl2WQNRGYxwdnr_9nInP1n2M9kZujKqPHCJFB35Ds2N3Csz_X0-QHM1J5UC4R2mn3IdEEjxW9bXqcCr9FEeLs-mK_2ki7pk0ppyC-y6HeJCA4dRnnMPElrJYNQKleCfxbnzm6AeSV7fBDCRAaYsQ2txs_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس مجلس: وزارت راه باید قانون مالیات بر خانه‌های خالی را اجرا کند
🔹
نیکزاد: قانون مالیات بر خانه‌های خالی نوشته شده است؛ وزارت راه و شهرسازی باید خانه‌های خالی را شناسایی کند و از آنها مالیات بگیرد و سامانۀ مربوطه را تکمیل کند.
🔹
البته من معتقدم مالیات…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/466928" target="_blank">📅 23:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a6bedbf.mp4?token=WZB2NyjYY3cnEfR9_4tzBbxkoGHn5ES0dlVi2kppOCKwj6rcJGhgsNxSzFhTScHYPSf2I2V2vR8L2x4vkooQOxdv1NKHxFdnsFFE0YflTRD1vpJr6asHAMTrFMMrMW5tU2A6Q-ENmdJX_4xL0izXJJ7V6T5wrv8_kDa6JhTHgl6FZczeChG-cO2iE2K8hhSqvMQGrOv4-7W9OzkYy_HHyyFsRNgPF_OYOOeK0Lgr2EI7jsIGu5S4gwgugxQNJ3WbMa5WYp0bqsbTW9pFLu020KYKi-VAdglEHVzHXAisF7RO5tzZ-nXBQoGWjYacm7gQgz-uXFMnoKKGACMx2fqrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a6bedbf.mp4?token=WZB2NyjYY3cnEfR9_4tzBbxkoGHn5ES0dlVi2kppOCKwj6rcJGhgsNxSzFhTScHYPSf2I2V2vR8L2x4vkooQOxdv1NKHxFdnsFFE0YflTRD1vpJr6asHAMTrFMMrMW5tU2A6Q-ENmdJX_4xL0izXJJ7V6T5wrv8_kDa6JhTHgl6FZczeChG-cO2iE2K8hhSqvMQGrOv4-7W9OzkYy_HHyyFsRNgPF_OYOOeK0Lgr2EI7jsIGu5S4gwgugxQNJ3WbMa5WYp0bqsbTW9pFLu020KYKi-VAdglEHVzHXAisF7RO5tzZ-nXBQoGWjYacm7gQgz-uXFMnoKKGACMx2fqrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: جامعه زمانی به آسایش و عدالت می‌رسد که درک مردم آن‌قدر بالا برود که عملیات روانی را به‌سرعت تشخیص دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/466927" target="_blank">📅 23:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2f555247.mp4?token=n8ykvEt9cLmD517FS6SieIev1MAzv_2c04iLd7Pcl4Xf33ds-aSAYfQb2TSpjRDPMZiGSBPr44DgtzmnB7e1xMgMDGvNyEt0tynTp7VJLQ2hPoraqHAtj8eXs_bCzO3iR0i4_jMw8eicrQ6lzsaaD_6zXVvsXfYyTqxHpX1ecM2y2ptXf7ZGZNepU_qqcYtT_cakMGxAJ9M5J6D5BlanSZ17S-Bz6hnJ97okk8KprDYo8Xq1qGuB08_NrhCvDaqPj-jZUyLv-7_RWx-uPHZewNYx8-ELwhka-ebfpBAu1Tm2c8j0rl5EpfrCeNTtg0ZlklUntd9Qd3E7EsmqCAVASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2f555247.mp4?token=n8ykvEt9cLmD517FS6SieIev1MAzv_2c04iLd7Pcl4Xf33ds-aSAYfQb2TSpjRDPMZiGSBPr44DgtzmnB7e1xMgMDGvNyEt0tynTp7VJLQ2hPoraqHAtj8eXs_bCzO3iR0i4_jMw8eicrQ6lzsaaD_6zXVvsXfYyTqxHpX1ecM2y2ptXf7ZGZNepU_qqcYtT_cakMGxAJ9M5J6D5BlanSZ17S-Bz6hnJ97okk8KprDYo8Xq1qGuB08_NrhCvDaqPj-jZUyLv-7_RWx-uPHZewNYx8-ELwhka-ebfpBAu1Tm2c8j0rl5EpfrCeNTtg0ZlklUntd9Qd3E7EsmqCAVASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح مقبرۀ شمس تبریزی در شهر خوی آذربایجان‌غربی  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466926" target="_blank">📅 23:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA7Z3Tvbg-dyNOeYN2iRuB79JBOYL5fW9oPRyrPWcIRSef5kXYOA7rzMc_uDzpxYNKLX2uPsYjmVMjp7c8zyNHPA2vHf_abKnDgSR9LglFEgRZpeV-gaGllIcqWbOT8u4xlM25dFxjMc1z4EHHmyHixkMoj8e_jQi3nxU1xO_ibQeHL7t-kvRWsaocUgehj5qP5aa9LmNqeoq6JYesqc-3t0D3Z9vdHTIrFwusjAST5yRWTCQRNdi_I1kZpRBHfSkOYbC4jh_-lDrvPur-BQpTSzvmjkrj7hA_EcGHT4AWGQS5VkXeUbVnw35O1dU63s5mxbUw-aawsBCWXcWk7ibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌هایی که برای فروش نیستند!
🔹
«در تهران بیش از یک میلیون مسکن خالی داریم که به نوعی احتکار شده‌اند» این جمله رئیس مجلس محمدباقر قالیباف است.
🔹
دولت می‌تواند با گرفتن مالیات از خانه‌های خالی، مالکان را به سمت اجاره یا فروش ملک سوق دهد، اما میزان مالیات اخذ…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/466925" target="_blank">📅 23:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236f2a908f.mp4?token=IPUuqdPBxNfWL226K6zv6-opAw60JZPPavWDg2kvB5ugF5nnnMKLQcZJUf_85QPLooORFfDoZ1CnKcdmg5q62NsrUgGNIiyC-8WboS1DETrNnon6rJaKlWFALbIamIh-JNWuGpCLkHevciiDgE3uyJjWzgQJdrijnxgSApqcpo5wQd1JmykYH15c9fX4e95fQ1FVC5O_v7MKHnt9v8dwRZb1AhC3Po3Odv0XmSQkmAwxXIrxfVgsuV2KYR8fnDu3KdI7dq_-fKbPk7lnXusMrmHYJy2LjFpn2kR3kQD0kXcUb5o_kLjpeWR6RWs4HjTRyQlSpIUBGKvT9M5koPauEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236f2a908f.mp4?token=IPUuqdPBxNfWL226K6zv6-opAw60JZPPavWDg2kvB5ugF5nnnMKLQcZJUf_85QPLooORFfDoZ1CnKcdmg5q62NsrUgGNIiyC-8WboS1DETrNnon6rJaKlWFALbIamIh-JNWuGpCLkHevciiDgE3uyJjWzgQJdrijnxgSApqcpo5wQd1JmykYH15c9fX4e95fQ1FVC5O_v7MKHnt9v8dwRZb1AhC3Po3Odv0XmSQkmAwxXIrxfVgsuV2KYR8fnDu3KdI7dq_-fKbPk7lnXusMrmHYJy2LjFpn2kR3kQD0kXcUb5o_kLjpeWR6RWs4HjTRyQlSpIUBGKvT9M5koPauEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش وزیر پیشین نفت به ترامپ: به دروغ پناه برده‌اند
🔹
ترامپ دیشب از استعفای وزیر نفت ایران دستاوردسازی کرد و گفت: وزیر نفت ایران استعفا داد و گفت این کشور نه اقتصاد دارد، نه نفت، نه هیچ چیز.
🔹
پاک‌نژاد در پاسخ به این ادعا، عنوان کرد: استعفای من هیچ ارتباطی…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466924" target="_blank">📅 23:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee18efaaee.mp4?token=GHAh3kw1kBiIIIx44dbPAvEgIAqdLnRnlFK2eGVMTpTVSIwoZ656v-0ProHUyoM-IEUcmLVcPpkW5rFkMAK47q6IL2HP_EgU8JQz1A_xGjesvbV-g_TH1jfNxADpDFim8_XClhvBRNGMTcdpaLeMSnIQa04ePV3uUCX8jv3ivXhYezEjSe4BXYiB_vg7wPoEeKcni-X8SaGCZr2a5ZddFQAauG0T5dGhkmeEkkk4goxqC_M5MB2btAcZ3w6lXugvBc8Ue7GudqTmsPi38npt5pRdQCNkhrx12Pe-rs0KWunaeguu8WlUHj1LxSH-GKGq9sdMSOWCdCOykqaUSjHJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee18efaaee.mp4?token=GHAh3kw1kBiIIIx44dbPAvEgIAqdLnRnlFK2eGVMTpTVSIwoZ656v-0ProHUyoM-IEUcmLVcPpkW5rFkMAK47q6IL2HP_EgU8JQz1A_xGjesvbV-g_TH1jfNxADpDFim8_XClhvBRNGMTcdpaLeMSnIQa04ePV3uUCX8jv3ivXhYezEjSe4BXYiB_vg7wPoEeKcni-X8SaGCZr2a5ZddFQAauG0T5dGhkmeEkkk4goxqC_M5MB2btAcZ3w6lXugvBc8Ue7GudqTmsPi38npt5pRdQCNkhrx12Pe-rs0KWunaeguu8WlUHj1LxSH-GKGq9sdMSOWCdCOykqaUSjHJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۲۱ طبس؛ میدان هنوز قصه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/466923" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6_1pF6xsbVoXluZhfbo9PYJInE81X0MaiYo9IfKOMkTXhlB02bYRt7NgBDiwZo0PqP0YylXzsPdp-dZ9VKm678YharOEZMYweaNpalQFFM-7Rjwac3sWgWT2meIBYqKshOBfYgv05pNm1kiTHaJQDTCXte-XLdztoWEZIMgVUzEZ9YFzcHR-YUzoEKWQFilcWnzGIT2MzNBLiFcSGNZa9zuA5FdJ51-gmlJG78zN7QiRrrHXoAy9wC_POV6s8wB0e2rQQn8R9oF0uPh79eMZLKsEEbaoyfmUxFCSQhrvrED9iquTdlKAHNws7PWKrhquGbQC0QarJapAhm6fVnHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار یک نفتکش در نزدیکی قطر
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/466922" target="_blank">📅 23:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از حضور رهبر شهید انقلاب در مراسم دانش‌آموختگی نیروهای مسلح سه روز پس از عملیات طوفان الاقصى
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466921" target="_blank">📅 23:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سازمان هواپیمایی عربستان: فرودگاه‌ ملک خالد در ریاض و فرودگاه شهر ابها مورد حملۀ هوایی قرار گرفتند.
🔹
برخی منابع خبری از توقف پروازها در فرودگاه ملک خالد خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/466920" target="_blank">📅 23:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd94d2bc6.mp4?token=si5AldqWxkEdN9N6BOdfYw3360tpRddXleHzgX9AelHuKAGImZoUdjaRFVI1Rmpq1TFLlZrJidNWrI8JtvO5NjQORQj_Ru1TSBXa4EwnvOgERFvUDjGvkrXhwuoR5cVJ7apIBodtFuaPyFxWrRjMW-Ihpv1OE8bytEqd9k_VAg8fqgcAi9afmCkNiKvmtC8ENZ6ZoKdKR08_BFIBgCEF5YrKTPfyoWF5exJs_trXFxwgi_UwRQqjotyiEDN7uk2vcDoFA0A5oA4_VQnzIYbUGvbAc4Izt1oSXN2DFJ-igtTl70t6uVH1um5vbzS3FalCBXyj6Y-Rgfufgmk4TQScKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd94d2bc6.mp4?token=si5AldqWxkEdN9N6BOdfYw3360tpRddXleHzgX9AelHuKAGImZoUdjaRFVI1Rmpq1TFLlZrJidNWrI8JtvO5NjQORQj_Ru1TSBXa4EwnvOgERFvUDjGvkrXhwuoR5cVJ7apIBodtFuaPyFxWrRjMW-Ihpv1OE8bytEqd9k_VAg8fqgcAi9afmCkNiKvmtC8ENZ6ZoKdKR08_BFIBgCEF5YrKTPfyoWF5exJs_trXFxwgi_UwRQqjotyiEDN7uk2vcDoFA0A5oA4_VQnzIYbUGvbAc4Izt1oSXN2DFJ-igtTl70t6uVH1um5vbzS3FalCBXyj6Y-Rgfufgmk4TQScKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا زاکانی: به مادرانی که در سال ۱۴۰۵ صاحب فرزند شده‌اند، تا ۲ سال خدمات ویژه ارائه خواهد شد
🔹
به ازای هر فرزند، ۳.۵ تا ۴ میلیون تومان به‌صورت ماهانه تعلق خواهد گرفت.
🔹
مادران برای ثبت‌نام در این طرح هم باید مادران به سامانه شهرزاد مراجعه کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/466919" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a605c86601.mp4?token=pHSFDsPbMRlrdWQs1ZQ3CaIHXF321t1zs9g8AvesBLS-bmL07mPPYOpiKcYDJJ69PRzIHcqSF8M0lEKI55yd4JUYdAiXDN0Ralcx6ubaljmB73c0uMsV5DPfUjU1cNMUP3N7iaw5pL9raUzh6tdbw_AJKGxV3uqDA9g6o33mhwzTqV7ZfDBzluEuRz1zEGqkVdttcXmcCcgo-f_F8gEbD17nFFt-I3UQPMPiOsJxcROCuqQuXpwUAo3vfgHMZbxVzD30xiHs8jm_plb2QsiPWmd61pq_cuI1MxHJS_ADtk4PfTCm9AnHklqefPAyvwWE2ij0XJ9c_XY1498nPVjWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a605c86601.mp4?token=pHSFDsPbMRlrdWQs1ZQ3CaIHXF321t1zs9g8AvesBLS-bmL07mPPYOpiKcYDJJ69PRzIHcqSF8M0lEKI55yd4JUYdAiXDN0Ralcx6ubaljmB73c0uMsV5DPfUjU1cNMUP3N7iaw5pL9raUzh6tdbw_AJKGxV3uqDA9g6o33mhwzTqV7ZfDBzluEuRz1zEGqkVdttcXmcCcgo-f_F8gEbD17nFFt-I3UQPMPiOsJxcROCuqQuXpwUAo3vfgHMZbxVzD30xiHs8jm_plb2QsiPWmd61pq_cuI1MxHJS_ADtk4PfTCm9AnHklqefPAyvwWE2ij0XJ9c_XY1498nPVjWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: نوسازی ۶۲۹ هکتار از تهران را در دستور کار قرار دادیم
🔹
شهردار تهران: قانون الحاق به شهرها یکی از راه های فاصله گرفتن دولت از فروش نفت است.
🔹
یک درصد شهر تهران را یعنی ۶۲۹ هکتار را در ۱۸ منطقه شناسایی کردیم که نیازمند نوسازی است.
🔹
در ۲ هفته آینده…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/466918" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع لبنانی: رژیم صهیونیستی مناطقی در جنوب لبنان از جمله اطراف شهرک‌های حداثا، المنصوری، سلوقی و زبکین را بمباران کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/466917" target="_blank">📅 22:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b957a1b42.mp4?token=Rin8Nu3SMwsj4TTQZzKmKQWe_0OAeeTNi7C5xJuoBl1Ur8gmny3Ys81Ur-YPxvJlB9OI5gwmOZ9fLMXhqpsQa5xC_rfVsqZlZTMGSfLPXfWOjTGKUpRXDM-L7UMzhYSU5HJoqPsN8f_PueqjvbhtTfb5oAx_9WpSkPhNPuSfyZJa5zoUaCMvqJ55cc5fGf7zHqK1m3vMrfV7Chx-aB2NDABfXr3BF3yB-Si4scXcWr1eGzqIOT3pYkOxBFO4CH2oNIZUPX8ptbr7CFtDjUfHj86RlhPtbcSZy43DIcIpRB1qda0i5zvhioAFmwxZqdhfN3VKwlEXuTsTtgCgohUcXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b957a1b42.mp4?token=Rin8Nu3SMwsj4TTQZzKmKQWe_0OAeeTNi7C5xJuoBl1Ur8gmny3Ys81Ur-YPxvJlB9OI5gwmOZ9fLMXhqpsQa5xC_rfVsqZlZTMGSfLPXfWOjTGKUpRXDM-L7UMzhYSU5HJoqPsN8f_PueqjvbhtTfb5oAx_9WpSkPhNPuSfyZJa5zoUaCMvqJ55cc5fGf7zHqK1m3vMrfV7Chx-aB2NDABfXr3BF3yB-Si4scXcWr1eGzqIOT3pYkOxBFO4CH2oNIZUPX8ptbr7CFtDjUfHj86RlhPtbcSZy43DIcIpRB1qda0i5zvhioAFmwxZqdhfN3VKwlEXuTsTtgCgohUcXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما از طریق واردات و حذف واسطه‌ها یک میزانی از کالاها را در اختیار گرفتیم و به بازارها کاری نداریم  @Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/466916" target="_blank">📅 22:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859d884080.mp4?token=fzNgVGQT7buqjWuvFieCesmnxCFMliSJ_TCsD1lCCufKctZN0GKN0NekMBqi1YqbnaAu2u5mUVuWcMxUwMbpP-IuLs1CCi2pBpDM-p9X5elmsunMmcYJQQSPWF3fMnkpv-nN87E750p_S78rhP9AAw7sBaeDhYVskQwkp_i9XilZYgsKzPUteCwIluDIvknw3uumCwe8HofT1NhIsQDr04-4kFWfFg9i53PwYc8JXeRvJ0i2esrYefbjfBdCMG-iZ0M-_AlJxOSPKovEpJzw-L88dBYc-LzftedLgCwIi4K6oPlDLUp6cspCnYT1ZTZdocyG9YUpMkY7nElp4txD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859d884080.mp4?token=fzNgVGQT7buqjWuvFieCesmnxCFMliSJ_TCsD1lCCufKctZN0GKN0NekMBqi1YqbnaAu2u5mUVuWcMxUwMbpP-IuLs1CCi2pBpDM-p9X5elmsunMmcYJQQSPWF3fMnkpv-nN87E750p_S78rhP9AAw7sBaeDhYVskQwkp_i9XilZYgsKzPUteCwIluDIvknw3uumCwe8HofT1NhIsQDr04-4kFWfFg9i53PwYc8JXeRvJ0i2esrYefbjfBdCMG-iZ0M-_AlJxOSPKovEpJzw-L88dBYc-LzftedLgCwIi4K6oPlDLUp6cspCnYT1ZTZdocyG9YUpMkY7nElp4txD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: برخی اقلام در طرح تورم صفر ۵ تا ۵۰ درصد زیر قیمت میادین عرضه می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/466915" target="_blank">📅 22:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شنیده شدن دو صدای انفجار از سمت دریا در کوهستک
🔹
دقایقی پیش صدای ۲ انفجار همراه با موج بلند از سمت دریا در منطقه کوهستک سیریک در شرق هرمزگان شنیده شد.
🔹
تاکنون ماهیت و علت دقیق انفجارها مشخص نشده است اما بر اساس گمانه‌زنی‌های اولیه، این صداها ناشی از شلیک تیر هشدار به سمت شناورهای متخلف در محدوده تنگه هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/466914" target="_blank">📅 22:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7e152513.mp4?token=VLy2_XmECogeemO2anxfwgyv3JNcedEP9R9P_rpipnjS2p2KjwQhARMAKuMDMooL9mMBpAbfAGEz_yCSNUg_ow3ABZBc0YSZbKfQbt0D87z8Ax4AOtCt3EQ3VQc8DCEiEMpcESoaM9d7bxHXf7cN7GBBff2f-8MN9uqJhZdWfzErkJFhJced5581BROK6v3PIx0qSljdvZ8TesDvG0qTGlyYeQTMn4DvRb-RNCvb2XXPSdMW7b4ZQWKmELCSJ--nNAXBDgbsv9KEK8kmhoFfhb2P3_kdYQB9UqrAkyCx9DMTTjV7tN_0NNiZO6gWrBxSwgEPTZaHAYD9Y8OsORVOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7e152513.mp4?token=VLy2_XmECogeemO2anxfwgyv3JNcedEP9R9P_rpipnjS2p2KjwQhARMAKuMDMooL9mMBpAbfAGEz_yCSNUg_ow3ABZBc0YSZbKfQbt0D87z8Ax4AOtCt3EQ3VQc8DCEiEMpcESoaM9d7bxHXf7cN7GBBff2f-8MN9uqJhZdWfzErkJFhJced5581BROK6v3PIx0qSljdvZ8TesDvG0qTGlyYeQTMn4DvRb-RNCvb2XXPSdMW7b4ZQWKmELCSJ--nNAXBDgbsv9KEK8kmhoFfhb2P3_kdYQB9UqrAkyCx9DMTTjV7tN_0NNiZO6gWrBxSwgEPTZaHAYD9Y8OsORVOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: از اعتبار شهرداری و اعتبار بانک‌ها و فرصتی که از بانک مرکزی برای تسویه ارز می‌گیریم، استفاده می‌کنیم تا این طرح درست اجرا شود  @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/466913" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک تروریست در شهرستان گلشن سیستان‌وبلوچستان به هلاکت رسید
🔹
پلیس سیستان‌وبلوچستان: در پی وقوع انفجار در مسیر خروج ۲ گروه انتظامی از ستاد فرماندهی انتظامی شهرستان گلشن، افراد مسلح به سمت نیروهای انتظامی تیراندازی کردند.
🔹
نیروهای انتظامی در واکنش به این حمله، یکی از مهاجمان را به هلاکت رساندند و تعدادی دیگر از مهاجمان نیز مجروح شدند.
🔹
منطقه همچنان تحت رصد و پایش نیروهای امنیتی و انتظامی قرار دارد و اقدامات برای شناسایی و برخورد با سایر عوامل این حمله ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/466912" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ebf243c97.mp4?token=UywsmsohU65bvg47xX22EQjWtgKUDnJbZaaL29-9F5327H-_XQ3J25uFbprxTRgLULx3UhmDWYpp688vDZn3F2ZrwzmFE2yRcpKRRcHLQxLtAr8DGcLtR0-gYb-XniA2hJmaFxz_St4JtPC7hN7XrpqzFqon5a2qecnbtg8qulUpSIO1bfnUfLTJhUkqhMqSX19Y2dOUyp4wCI6LbbqK5xmyIQkWNMqK6g_WQi3pMGc8ODaUISiAe6LJ_lWNtcnFz72QZkgDbNooDIMvFlUzvx7NYODnlLIj0EpF9bG2BhmKrhmh-AVKzQvYsbmsS6gD0MP-RYqTj_GYJDwuCvpRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ebf243c97.mp4?token=UywsmsohU65bvg47xX22EQjWtgKUDnJbZaaL29-9F5327H-_XQ3J25uFbprxTRgLULx3UhmDWYpp688vDZn3F2ZrwzmFE2yRcpKRRcHLQxLtAr8DGcLtR0-gYb-XniA2hJmaFxz_St4JtPC7hN7XrpqzFqon5a2qecnbtg8qulUpSIO1bfnUfLTJhUkqhMqSX19Y2dOUyp4wCI6LbbqK5xmyIQkWNMqK6g_WQi3pMGc8ODaUISiAe6LJ_lWNtcnFz72QZkgDbNooDIMvFlUzvx7NYODnlLIj0EpF9bG2BhmKrhmh-AVKzQvYsbmsS6gD0MP-RYqTj_GYJDwuCvpRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: از اعتبار شهرداری و اعتبار بانک‌ها و فرصتی که از بانک مرکزی برای تسویه ارز می‌گیریم، استفاده می‌کنیم تا این طرح درست اجرا شود
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/466911" target="_blank">📅 22:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هواپیماها و تسلیحاتی که بارها و بارها به‌وسیلۀ آن به یمن حملۀ هوایی شده آمریکایی هستند و استفاده و به‌کارگیری آن‌ها به آمریکا وابسته است. @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/466910" target="_blank">📅 22:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac456efa0.mp4?token=PjqIu98af2xTsN5RYJjwgrgkaymxweIgH00BkoZvblZLOcnaEv3DdRp3muMKs7x_vDeFdt5ZeV8ZLyi8HiwGJCmLEz1soB-mcYt4mLIzAD2Vp67ol3rXxMK9L3qHG9v70gUaPf2OYMlB6zxfDazKRBT_8NxY6-rM-bZWGc_E6BakvjQQHb-w9V7zxgDFFVeMeT6fGGkLeZxQIaeQHfNw5OV6QWKVZlL--kpL5awP3C2ahvem0RvolZ5i3ZBvWr9tjWBloO4_xq_uKQCYGY5OvibSn0nrGnqxU29AyQkTY_jbEh_kpRh_AgPX9PY50xh0jhYSR35s6D1YAawByoM5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac456efa0.mp4?token=PjqIu98af2xTsN5RYJjwgrgkaymxweIgH00BkoZvblZLOcnaEv3DdRp3muMKs7x_vDeFdt5ZeV8ZLyi8HiwGJCmLEz1soB-mcYt4mLIzAD2Vp67ol3rXxMK9L3qHG9v70gUaPf2OYMlB6zxfDazKRBT_8NxY6-rM-bZWGc_E6BakvjQQHb-w9V7zxgDFFVeMeT6fGGkLeZxQIaeQHfNw5OV6QWKVZlL--kpL5awP3C2ahvem0RvolZ5i3ZBvWr9tjWBloO4_xq_uKQCYGY5OvibSn0nrGnqxU29AyQkTY_jbEh_kpRh_AgPX9PY50xh0jhYSR35s6D1YAawByoM5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ۸۳ درصد ناوگان اتوبوسرانی را نوسازی کردیم
🔹
امروز بالغ بر ۲۵۰۰ اتوبوس به ناوگان اضافه شده است و علاوه بر این، توانستیم دیروز برای اولین‌بار اتوبوس سه‌کابین را وارد بندر کنیم و این روند درحال توسعه است.
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466909" target="_blank">📅 22:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2a0e22d.mp4?token=RC6kDGk4fNvWHpOcenscBrcco48Vi9Wy0aMY02AXP_F8iDa6AiDv3EMFYyihMQrtIMb_qqiPFVeZG_uatNpnbg6qQP_WOv1d7D8BEq5-YjXwXvhho4MWMWl43wAAugmDRU-WYwhzuYNSAPNO99UrktpxEjvK86qoxRkTWHZeBCDhrfJE9S88iTBqubvdDJrdJozmdR9g6I6KxD0dyEgfVhSpNSSnfFgbQfDvTj8uG68GAg_Ci1PDy24IK5QJcmDdHspLws0LfKS6wwMwlxPmw8msiaNQ0zZCpI4mOiLsbcJPSCofY9cf7HwIgHbgL9SfhkJmRf0TNwW5IspW20R3PT7U9CmDXBtGVNUaUD-uWb9L5Z_Bcdpj926v1wneDpRHEtM1khRHff1Dd7IaX5-D36hsKduJ8gs7a1uNcjL6fA4hXRF7xPXywtJPrjgK7i_fhhqkZeqka6pSGz1smGCsQ42PQXkkLSyoGKqnyDPw-mHBCtGjBewFD3VlOFbWde-XEXIg2TPwHbbfrw5dVHyKHvVO3WR5tvmcOwCwiDSvdK97PUI-622EnEN11haph_4BE7A0EHWaVaSes4rEZBOebRfVpp9Dctv67IIQSQO2v7q8XNL2LGubQoM3aI8DrxbxTTa6jWj1-6w8A7f4rCriqLtyipaoBinbQxTJny3oAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2a0e22d.mp4?token=RC6kDGk4fNvWHpOcenscBrcco48Vi9Wy0aMY02AXP_F8iDa6AiDv3EMFYyihMQrtIMb_qqiPFVeZG_uatNpnbg6qQP_WOv1d7D8BEq5-YjXwXvhho4MWMWl43wAAugmDRU-WYwhzuYNSAPNO99UrktpxEjvK86qoxRkTWHZeBCDhrfJE9S88iTBqubvdDJrdJozmdR9g6I6KxD0dyEgfVhSpNSSnfFgbQfDvTj8uG68GAg_Ci1PDy24IK5QJcmDdHspLws0LfKS6wwMwlxPmw8msiaNQ0zZCpI4mOiLsbcJPSCofY9cf7HwIgHbgL9SfhkJmRf0TNwW5IspW20R3PT7U9CmDXBtGVNUaUD-uWb9L5Z_Bcdpj926v1wneDpRHEtM1khRHff1Dd7IaX5-D36hsKduJ8gs7a1uNcjL6fA4hXRF7xPXywtJPrjgK7i_fhhqkZeqka6pSGz1smGCsQ42PQXkkLSyoGKqnyDPw-mHBCtGjBewFD3VlOFbWde-XEXIg2TPwHbbfrw5dVHyKHvVO3WR5tvmcOwCwiDSvdK97PUI-622EnEN11haph_4BE7A0EHWaVaSes4rEZBOebRfVpp9Dctv67IIQSQO2v7q8XNL2LGubQoM3aI8DrxbxTTa6jWj1-6w8A7f4rCriqLtyipaoBinbQxTJny3oAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«الله‌اکبر، خامنه‌ای رهبر»؛ شعار یک‌صدای مردم شاهرود در شب‌های اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/466908" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466907">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466907" target="_blank">📅 21:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466906">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
۲۲۱ شب حماسه سازی مردم مراغه برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/466906" target="_blank">📅 21:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466905">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">البخیتی، عضو دفتر سیاسی انصارالله یمن: زمانی که سعودی اخبار پیشروی در تعز را منتشر می‌کرد مزدورانش در محاصرۀ نیروهای مسلح یمن قرار داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466905" target="_blank">📅 21:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1219f7bd2.mp4?token=MPglVbBU1wRy4PvsMiiALJhdySE50X0u3dRYaoFyS7xPFpD1gX4gjVF5sFVNCEVTDI085KRGrRYSAS7m9YuVrn5j8A0GLYxO7al6w8F-TzxYvql_rFqo6s5ILPqZWtKF1LmI7fxEHGJPjTkCF-Mk-hON8Xqupz3vuyMm7yIFN0ljvCI35-nhrEc9NHTlsAXeiQzNcCbJWG2JBPLFnkSdYJLGdY6n4DjpBoXzjrLkXeU0ygJEjGKapna_Zk-rlK6vTxMWJMcH7UElngGaPU8i8k2_2FXf1Djc1Rht0yJd-Dqx_P1wEoZnaG0th-c-cwGnTLDzbZZn-7pnDIwT-JSPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1219f7bd2.mp4?token=MPglVbBU1wRy4PvsMiiALJhdySE50X0u3dRYaoFyS7xPFpD1gX4gjVF5sFVNCEVTDI085KRGrRYSAS7m9YuVrn5j8A0GLYxO7al6w8F-TzxYvql_rFqo6s5ILPqZWtKF1LmI7fxEHGJPjTkCF-Mk-hON8Xqupz3vuyMm7yIFN0ljvCI35-nhrEc9NHTlsAXeiQzNcCbJWG2JBPLFnkSdYJLGdY6n4DjpBoXzjrLkXeU0ygJEjGKapna_Zk-rlK6vTxMWJMcH7UElngGaPU8i8k2_2FXf1Djc1Rht0yJd-Dqx_P1wEoZnaG0th-c-cwGnTLDzbZZn-7pnDIwT-JSPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناباد در شب ۲۲۱؛ عاشقی زیر آسمان وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/466904" target="_blank">📅 21:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTnABHsxOxDbFRvTAJ-iglAKS36kz4Onv9R070AUbEdClLmy3AFPnbZCSFcUy4XRW_rHjIYvUeFtEK1xTwf8pno7eKPPxov3ykmKfrJur7XoeemzNNTmapRzAoa7KGp6JZeFeFBjaC237h9qg22FpuumQ_kZv-OVJdnpmg9eXySCY5uLcChhAyLXAhSmupNCV00aKDEfSliIPCskN4W7Z_9ejyU57Q-nOZXXP_yBF88CpTg9xdNqBOxoZOKJC46Q1jwSnpegrYnw20uiQQczS7XQkUWejzHJ5o0u3t9MDoAZ53nBL0j-b5BAk3KlmS77mjVAH04a8p_E3SKsVKByjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تیم سپاهان نقاشی کودکان اوتیسمی را به‌عنوان پوستر بازی با فجر سپاسی منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/466903" target="_blank">📅 21:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6abf3a44.mp4?token=fGTS9OUOj6wGGOHGuRm-MTAxPFgfVGRZ-wGwXoV005s7YlEg5pJ344sg0GIqVHpEE4yutpFh5MGfOPXDpfgTglbbZ3JF2o65VykMi-Qn0rtY8w7lEoZ1GT7ykRtrz-15iw4cDmEDFwQUlKznR5XKWdOpoXw1QqlLmc7FNIol6--6QLjLwsTgeJgkASmElOmwoqOuQi0BF2zSnfGi_8JYGKS0RI0pps_ZMFYbNovW7UxOFBkiiffZMbZOwpTsDNQUKpEE9sE7AEi8nXw6UqkRbsb1c-gy3nJ2gWqpq6916DG1fbAi1uYnyzQr5FnePHt3i59F4Yv3SG6VcSU4GxykZXwhpDNzG-4mVDzfSfebnfuFId4Bzb8-h6UFJ85dNowB0zk4iTSFqCzx0Ygk2YMM7VSf0cHb_DmXqQp-uSCGMFzz1qR1oZEDpme_0vdBo4xm0EKPQ0tr2fG_yXU5sHHG3CyXjwlNGwmEyFZMVeYRXYYEEOLZ1AlyH3vsAYcH1fYSinWShsYx_hfdV8124bDL5Q5v7pNQm4XN9_y5Tt682lDtf2Oimetc6-bC_3ZFq9uzW-1txcWwORptecIWUCON_eFs6tNBRGt1rQwVc9JT0eNnNXlrxgQ5NgWBPkM4yGJz4PagIH703QihfOEfpWQYXwA227AwkJu8m7hsLeN-8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6abf3a44.mp4?token=fGTS9OUOj6wGGOHGuRm-MTAxPFgfVGRZ-wGwXoV005s7YlEg5pJ344sg0GIqVHpEE4yutpFh5MGfOPXDpfgTglbbZ3JF2o65VykMi-Qn0rtY8w7lEoZ1GT7ykRtrz-15iw4cDmEDFwQUlKznR5XKWdOpoXw1QqlLmc7FNIol6--6QLjLwsTgeJgkASmElOmwoqOuQi0BF2zSnfGi_8JYGKS0RI0pps_ZMFYbNovW7UxOFBkiiffZMbZOwpTsDNQUKpEE9sE7AEi8nXw6UqkRbsb1c-gy3nJ2gWqpq6916DG1fbAi1uYnyzQr5FnePHt3i59F4Yv3SG6VcSU4GxykZXwhpDNzG-4mVDzfSfebnfuFId4Bzb8-h6UFJ85dNowB0zk4iTSFqCzx0Ygk2YMM7VSf0cHb_DmXqQp-uSCGMFzz1qR1oZEDpme_0vdBo4xm0EKPQ0tr2fG_yXU5sHHG3CyXjwlNGwmEyFZMVeYRXYYEEOLZ1AlyH3vsAYcH1fYSinWShsYx_hfdV8124bDL5Q5v7pNQm4XN9_y5Tt682lDtf2Oimetc6-bC_3ZFq9uzW-1txcWwORptecIWUCON_eFs6tNBRGt1rQwVc9JT0eNnNXlrxgQ5NgWBPkM4yGJz4PagIH703QihfOEfpWQYXwA227AwkJu8m7hsLeN-8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفانی که زاویهٔ دوربین‌ها را تغییر داد
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/466902" target="_blank">📅 21:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e84c609aa.mp4?token=bKXRPqb4WU6rQ1U-OD30kNigv4RSYSn-xaU8V0NjN9pNE3X4IF6Xyi8GmuwTwp4PHN5mC24E39MVvdpA7j3CzyZUy4YPtVQE0udikC0zEaSkT61YSNaEE0I_s8QOYsHXn9VVPPu-3t6PeLaTPBtPTq6qbIVqovtOmYWPcyAVpLoWT01BUGe8GWeggkdL-VASDZDem8sjviRziRVAWZEeecBKvuMv8todjYg9SEXOpFkVmC6hWZOlSWaNrAk2IdqsqwetGxqcGMLo-1R6ru9XyVs_6bqiFVDCqrMjxQs9jn5AaF7ZAmeZeIvxMcWshfsdHRp9ErFy8C1OxL2RieD3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e84c609aa.mp4?token=bKXRPqb4WU6rQ1U-OD30kNigv4RSYSn-xaU8V0NjN9pNE3X4IF6Xyi8GmuwTwp4PHN5mC24E39MVvdpA7j3CzyZUy4YPtVQE0udikC0zEaSkT61YSNaEE0I_s8QOYsHXn9VVPPu-3t6PeLaTPBtPTq6qbIVqovtOmYWPcyAVpLoWT01BUGe8GWeggkdL-VASDZDem8sjviRziRVAWZEeecBKvuMv8todjYg9SEXOpFkVmC6hWZOlSWaNrAk2IdqsqwetGxqcGMLo-1R6ru9XyVs_6bqiFVDCqrMjxQs9jn5AaF7ZAmeZeIvxMcWshfsdHRp9ErFy8C1OxL2RieD3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس شمس تبریزی در خوی
🔹
در سفر وزیر گردشگری به آذربایجان‌غربی سازۀ جدید مقبرۀ شمس تبریزی افتتاح و از تندیس این شاعر نامور ایرانی رونمایی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/466901" target="_blank">📅 21:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db8oBj7hbMNB7hxSrX8T2TlYfad6rctsbfktAQYoi68CtlXBAzttF8k3NfFSJAVJ2FbmLycqaz39k4_I1T5KLnlsgCt9zaJipwJEg9wt3lUxN1U1W_1U_cgakCgZvURqyaCdetS-zLk8Zq9ViyVu8kQcKUUB4y9Hm7_U7bNq7A0lhjaNue-vJ_oSDQ19iKD14_dJM8VrnxYfzP90zrViuKlfy5WulIv-J4v5OS2LN9VrS8g_3YsGJOLdE-oHiQrel_kzHLmXvbHUvaiarOMdEO73RnyjbkIdw3Q87iUQTbaZy2xEKUOqK5Awg3-eXRqgoTOAL2EPyjOhWJ5xdUC31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع مزدوران سعودی هدف موشک‌های یمن شد
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای متجاوز سعودی که قصد پیشروی به‌سمت مواضع نیروهای ما در شرق استان الجوف داشتند را با موشک و پهپاد هدف قرار دادیم.
🔹
در این حمله ده‌ها نفر از آن‌ها کشته، زخمی یا به‌اسارت درآمدند و…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/466900" target="_blank">📅 21:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889dea5fe9.mp4?token=KeTWDdZZMAf4tOvL2GXYbIaxM79HazT8Rgc3lVH6_eHhPXqg2zD1WonByD9nsMbLF5TgZFjVg_tvI-e7LikhdTNfFRovOCB2iMijSADEVyqrlZFXUK5VrGnh7gqOoIsZvKRJDZOkzvFtbebNeuyHlUxgKnngMyPj67V6ISWcrQ7Z55y5mZQehu-HppoFPhgV49kU38890-0XClOqR84M-K4uofWclGxO3nxmXw7wJFZ9_4jZHjWEmNH_rTZOtx9XdwwbhbXH2emhenTmi0azOkVLghgYD7cuJuWBTPXHRLLODmdcNFlLaetwkWdefUWyObL0GjFZCcFniM6ejBkdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889dea5fe9.mp4?token=KeTWDdZZMAf4tOvL2GXYbIaxM79HazT8Rgc3lVH6_eHhPXqg2zD1WonByD9nsMbLF5TgZFjVg_tvI-e7LikhdTNfFRovOCB2iMijSADEVyqrlZFXUK5VrGnh7gqOoIsZvKRJDZOkzvFtbebNeuyHlUxgKnngMyPj67V6ISWcrQ7Z55y5mZQehu-HppoFPhgV49kU38890-0XClOqR84M-K4uofWclGxO3nxmXw7wJFZ9_4jZHjWEmNH_rTZOtx9XdwwbhbXH2emhenTmi0azOkVLghgYD7cuJuWBTPXHRLLODmdcNFlLaetwkWdefUWyObL0GjFZCcFniM6ejBkdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مظلوم‌نمایی از تروریست ممنوع!
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/466899" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab936b32ca.mp4?token=gcBJKvTKeMdpiaRmXqv_4oyzWy2NZk1oV81ATwQKg_9D-TQjzWB5oxjeq4-8iOrAW5iNFiMAIVPhY-D_CoAZGpvjIrAayIisfRcMWmhzUyEOBewv2rCwaNX2bt_KFXZdT1ybxd4IxnG7qBNzB_rC1HGZq8Fl60TBhDhhzV95c41P1Ag_pcsZs9jWshMGiunAhJk1JhGfAe2on-wI3gv8y-Rb5gvFP9mtO3cbOaQ7kkRqeVdl3EFDVS_tbNyJhiRSFsJHeTBJu_f9-1A0rjjPGbM7fDt0Kf6YW9Skz4vCUl8bCA2BcMmp87zVHVZCEWoUhE2LxI1xOu68Xh-4CEcrYGJkG-HaYhd1I8Fqb0KGMO17XXbm05hu91_y5cLCvKmziNvbl-H2fMVWgqolnv-gcx6SEmWc24w51JYOQe-uqCyezJH65R5Jr1iobD45cxdPPwk669lmTr70pIB_-Qpmh9z56H6wMkLh5552qq0eaQyHSRdn1wXrkLIQaZky2kLPjappqWpmgXtGiDl4nGwfZJ5CSHNc979N2J3DQx5uj-dcSs7ItQhjzdRAfBGgpfOvlb4a5qt77U0-RqwvCTZleu7Hr9CHMBq4DdsPNOQwu8Lxdchd4KmUSNjJIO2omvWPqYbH3-Twcar1iKzwx1yluPkk2knhdshaXm_jfwatlk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab936b32ca.mp4?token=gcBJKvTKeMdpiaRmXqv_4oyzWy2NZk1oV81ATwQKg_9D-TQjzWB5oxjeq4-8iOrAW5iNFiMAIVPhY-D_CoAZGpvjIrAayIisfRcMWmhzUyEOBewv2rCwaNX2bt_KFXZdT1ybxd4IxnG7qBNzB_rC1HGZq8Fl60TBhDhhzV95c41P1Ag_pcsZs9jWshMGiunAhJk1JhGfAe2on-wI3gv8y-Rb5gvFP9mtO3cbOaQ7kkRqeVdl3EFDVS_tbNyJhiRSFsJHeTBJu_f9-1A0rjjPGbM7fDt0Kf6YW9Skz4vCUl8bCA2BcMmp87zVHVZCEWoUhE2LxI1xOu68Xh-4CEcrYGJkG-HaYhd1I8Fqb0KGMO17XXbm05hu91_y5cLCvKmziNvbl-H2fMVWgqolnv-gcx6SEmWc24w51JYOQe-uqCyezJH65R5Jr1iobD45cxdPPwk669lmTr70pIB_-Qpmh9z56H6wMkLh5552qq0eaQyHSRdn1wXrkLIQaZky2kLPjappqWpmgXtGiDl4nGwfZJ5CSHNc979N2J3DQx5uj-dcSs7ItQhjzdRAfBGgpfOvlb4a5qt77U0-RqwvCTZleu7Hr9CHMBq4DdsPNOQwu8Lxdchd4KmUSNjJIO2omvWPqYbH3-Twcar1iKzwx1yluPkk2knhdshaXm_jfwatlk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در سومین سالگرد طوفان‌الاقصی، مردم در اجتماعات شبانه پرچم فلسطین را برافراشتند
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/466898" target="_blank">📅 20:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osnh4enfMdArBYIcZhbDqmNnz2tKzgu_L3TAHz6rVk26TubpEd5r5koWjBA6H5kRZz22U9USfft2wfBcr3h4ZtBdEQEMtTOr9qNbNXueWRdoqXpwNL-AO_fZ7Y8Z70CcTDpAHLH1I6Ndi8e8I8DwxJFnl0ap2F8ibzS01nSEfje3D0MUuGQzEBKZYz0JKWsW7lqlVjlxnDOWEkAGPnl9wvmd45iLvNNZTrgbEzcnLN-yykXuhxQ8akhat77CD_o38EkmzfUjisEFvuEI7KAk0RbCTlAeaWDCQIwiAm2eLo_GYJOkUYR3ZwkvJrFhuPABEkNeG_zi_nArJK_2P8tbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از مجسمۀ ترامپ به نام «طاعون نارنجی» در پارلمان اروپا
🔹
در یکی از گذرگاه‌های پرتردد داخل پارلمان اروپا، سیاستمداران اکنون با مجسمۀ‌ برهنه‌ای از ترامپ مواجه می‌شوند که با لایه‌ای نازک از ورق طلا پوشانده شده است.
🔹
این مجسمۀ مِسی که با عنوان «پادشاه بی‌عدالتی» نیز شناخته می‌شود، رئیس‌جمهور آمریکا را درحالی به تصویر می‌کشد که بر شانه‌های مردی کوچک و نحیف سوار شده، در حالی که در دستانش یک چوب گلف بلند و یک ترازوی عدالت قرار گرفته است.
🔹
در متن حک‌شده بر پایه مجسمه آمده است: «من بر پشت مردی نشسته‌ام. او زیر بار سنگین من در حال فرو رفتن است. هر کاری برای کمک به او انجام خواهم داد؛ جز پایین آمدن از پشتش.»
🔹
این اثر هنری که طاعون نارنجی نام دارد، در مقر رسمی پارلمان اروپا در استراسبورگ فرانسه نصب شده است؛ ینس گالشیوت سازندۀ این مجسمه گفته: ترامپ در حال نابود کردن تمام چیزهایی است که من به آن‌ها اعتقاد دارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/466897" target="_blank">📅 20:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۴.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/farsna/466896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۳.pdf</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/466896" target="_blank">📅 20:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czUMn6ksr54wK3-ARpY9AudyxL28HdHqP3lrQlJzJ6lx4RF8i2Fon5uckyafrLgCTSsTIy6gIvFNUaw2QlGCy5tvKfeKLFeYYedvAKBNpKVQ2RPf8VO2uDgkokLDrt_CEVBJdc6BZ5G5tbtlTJSN6xH30lenowU9Bb1DIsi9rytCp01ZgqER_T3Dbn-Q8tbLy-UIbtyDdHf8Y5QhscqmJex0ioiSFdVIhsPUK9vCz9ZLVSAMTCwNJY5z4S4Fm-a0rhteBLQJ2NKgLqgvNZetx6vVAKvNB5asV1E9sEhChjCqVypRE-whQwNPllfu2JA1n_gOJOfN0oJbM9AymOjNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bro_bNjyXhVo07nGkiHtEdrUx_0y14NujAkJqtqAWx6aFbGZqo5LG7UEB0La_Se7hj10rN6UnCB04-C7E3vuKBIJ_4lXOkzKSGTB3pc7AzaNTJeabLvdo3xCf5RxTpE9BxoxOJgMahdBysrROWA4pLJC4YS1qxB909W_5epqbcR_7AQIkX5rqqMXVZq-sxbIqXLL-b2UkM1HMyHra0aOY5s57YVItN5moNVJo7KJV5LDfeH1Gjicg4my-X_LQrWpDkOZrBNMmqrOqJq5WkWTH5i2Bj0p61lRtiYRcFRM1KtVbM9nbxmRJBFEziiCrvVa263qb9SzIzkHTHoH_WsQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_sWCtrOQdR1GF3jN9_wEZBbWa3QDCT0Jt6MwM1jCTY9Hyhg_2-BfQGpdPLNkYRNxdULvEiAZCdst612WHkTr684qJ_xQA3i3fJjVvEZgfmxw2OJlSi-uRrguSW5EF8lWsZG4o-CjbqtPvLm3fiT-fl7LnF-N5LarSeeDzH72uaHFRXbIiOG4CyJEUczQASnBE6wa6EYXZg5dyrW1KFRXeGmpz4l38Ujqqr0pOecn3E_g9rMKPVuL_WOLPp0el_ppGhzXlwXSV2_dz_eFBECbIA_ySwy9J_5AfHibXo-qp6Af6xjOBvwxnASxLTcBcNzHchT8j8mtqP0cDWetvWFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkXwdsqyTbGxwC5qzrvi59qLlJeZwudQYhf3ob5ioSu2QJ14y6DsxqwIhEgivvtR1wxrMqraK80iSRFSZEVXfmmH-OXcYY9jbqVtsQxySFvgkt8V8KJVviCUzZkMozBNr626s3VllX3xth1SI_HJDqMawdu_JYHz-EZCamCm5ZsSI-0kd4DrL12cbbDltXoIUpBreUHuAxj7RhgHBhD4g29WtfmHyEPQVckqHIS1g3VNYEvsvNa1BlHk6sRRcjbsUAbOcvO-IkoB2KFZsFy9HGz4oLNfHfAnyDyD0UPCklHWfotbRPyn1SU4TmxzkL0ez8FW52qSz18wW-pf4ZOrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujqguPG8yr4nhQ2iF6DdIqPe-69rh211jZQqDD6y5P4xcmIru4QsBhvWW2PiFE8uufl82K5Q3CplQEJ9pMdYYnG8uwADVb-doRrQQ7-8Zi6Di8gio2mq757nueu1XssoqMQqQS2MeyT0v-sNG9ezwCpqxc8VdYx2xlSs51nLp8Sem3--bwSA6tPlNDNU6ZfZWuM8eGoJJOCHuK1C7QQRq1S58NgLsL1j0kxNCUh0kQtTOFstjRb9FeB4w44a9jVqHuT75dN7bUwhOrN5k-S-ogrEdpyrcjc3tH-lOmH2eSGsaeb98snDrC6AT7kO-WqajzPQqeNbqHjjltSe6qbXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب با خانواده سرلشکر شهید رضاییان
🔹
اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب، همراه با سردار حسین اشتری، مشاور رئیس ستاد کل نیروهای مسلح، با حضور در منزل سرلشکر شهید غلامرضا رضاییان، رئیس پیشین سازمان اطلاعات فراجا، ضمن ادای احترام به مقام شامخ این شهید والامقام، با خانوادۀ ایشان دیدار و گفت‌وگو کردند.
🔸
سرلشکر شهید غلامرضا رضاییان، در ۹ اسفند ۱۴۰۴، در جلسۀ شورای‌عالی دفاع و درپی حمله و جنایت صهیونی-آمریکایی به بیت رهبر شهید انقلاب، به فیض شهادت نائل آمد.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466891" target="_blank">📅 20:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e2c4a0c4.mp4?token=GxGUJRwYJ6pV-iBASlMyWVza12oEdoS32iNSNjXmte3IrdT8xJTwsk8V3ktIa54AzmZn9etlEsk1c3uiHHNkznVlKXXxppuzz7sIBvRvWURbukjJj84TCH4QbiLblOKPBgr8QZLUdcUG6TVqGKlmQ9lejTVK2yH8Y-7ktLxdjBL4-YiNCBS2uj0hW45jS81GMFum3FiLFy6QZEwNCz5fyymWLLDIU4yqH8cYHS5rrmazYTNz0GAyENr5j1vLp7dtpfdglcYWMOojyNNB8MGxWHPSRy-8DlwxY9plPsvJ_rj6503_1TDk-Xab4Wh04oH4MdzmHepa2HuSUYYVqi0AIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e2c4a0c4.mp4?token=GxGUJRwYJ6pV-iBASlMyWVza12oEdoS32iNSNjXmte3IrdT8xJTwsk8V3ktIa54AzmZn9etlEsk1c3uiHHNkznVlKXXxppuzz7sIBvRvWURbukjJj84TCH4QbiLblOKPBgr8QZLUdcUG6TVqGKlmQ9lejTVK2yH8Y-7ktLxdjBL4-YiNCBS2uj0hW45jS81GMFum3FiLFy6QZEwNCz5fyymWLLDIU4yqH8cYHS5rrmazYTNz0GAyENr5j1vLp7dtpfdglcYWMOojyNNB8MGxWHPSRy-8DlwxY9plPsvJ_rj6503_1TDk-Xab4Wh04oH4MdzmHepa2HuSUYYVqi0AIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ حماسی جان‌فدایان چهارمحال‌وبختیاری، دشمن را به لرزه انداخت
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/466890" target="_blank">📅 20:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🔹
ادارهٔ دریانوردی وزارت انرژی و زیرساخت امارات اعلام کرد که ۴۷۲ شناور حق استفاده از خدمات بندری امارات را ندارند.
🔹
بررسی‌ها نشان می‌دهد بخش عمده این شناورها مرتبط با ایران هستند یا از مسیر ایران برای عبور از تنگۀ هرمز استفاده کرده‌اند.
🔸
قراردادن پایگاه‌ در اختیار آمریکا و حتی حملۀ مستقیم به خاک ایران در جنگ اخیر، راه‌اندازی ناوگان نفتکش‌های شاتل برای تضعیف اهرم تنگهٔ هرمز، ادعای اشغال جزایر سه‌گانه توسط ایران در سازمان ملل، دیدار‌های مکرر با نخست‌وزیر رژیم صهیونیستی فهرست بلندبالا از اقدامات دولت امارات در ماه‌های اخیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466889" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس شمس تبریزی در خوی
🔹
در سفر وزیر گردشگری به آذربایجان‌غربی سازۀ جدید مقبرۀ شمس تبریزی افتتاح و از تندیس این شاعر نامور ایرانی رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/466888" target="_blank">📅 20:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دریاچهٔ گازوئیل در جاده آبادان-اهواز چه قرار بود؟
🔹
انتشار تصاویری از تجمع حجم زیادی گازوئیل در جاده آبادان-اهواز و شکل‌گیری ترافیک، در روزهای گذشته در فضای مجازی خبرساز شد.
🖼
اما ماجرا چه بود؟
مدیر شرکت خطوط لوله و مخابرات نفت منطقه خوزستان اعلام کرد که این حادثه شامگاه سه‌شنبه ۱۴ مهر به‌دلیل ایجاد انشعاب غیرمجاز توسط سارقان مواد نفتی رخ داده است.
🔹
عملیات ایمن‌سازی، مهار نشت، ترمیم خط و پاکسازی کامل محل در کوتاه‌ترین زمان ممکن انجام گرفت و در حال حاضر این خط لوله در مدار بهره‌برداری قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466887" target="_blank">📅 20:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRCP62M594kJgBxRbkObyrnhO8DAaZs0Axe8jqItVzzvpkviwj-gRAhEaWEjOZxsEnXmBViXU9Q_hUVvSXOhRBe_co1ArIbwwrtaGZoglifT1RXcooI-U-8noBBubmnAdJUDQfshJKDvIECHg0EkPg3QRmIrljGJ3TzRRKsPoZ-XlvlOq0aVeO5TXBWWXfefVhf5PLoIr4h9MiseTZK_CAvcI0HfBK1SMEzdylveuazadt1YwGewlLZZWuMCt4C2FSMdS25g8Yn36l_1-BqhIk2930ELI81JJZDoiaCPI9xLxKkFmE1K1IvHhQZ3GaZk32j2Vn45o7sECe50Ojl1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلای دبی پروازها به تل‌آویو را تا اطلاع ثانوی متوقف کرد
🔹
فلای‌دبی که روزانه ۱۰ پرواز رفت‌وبرگشت بین دبی و تل‌آویو داشت، به‌دنبال حادثه پرواز جنجالی چهارشنبه گذشته پروازهایش را تا اطلاع ثانوی تعلیق کرد.
🔸
روز چهارشنبه ۳۰ سپتامبر، هواپیمای فلای‌دبی از دبی به…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/466886" target="_blank">📅 20:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
رهبر انصارالله:  سعودی زیر چتر آمریکا قرار دارد و تحت پوشش آمریکا به یمن حمله می‌کند. خواسته اصلی سعودی نیز ورود مستقیم و همه‌جانبه آمریکا به این جنگ بوده است. @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466885" target="_blank">📅 20:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
بانوان شهرکردی جان‌فدای ایران شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/466884" target="_blank">📅 20:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466883">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقائی: عملیات‌های پرچم دروغین جنایت‌های آمریکا و اسرائیل را نمی‌پوشاند
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی درباره تاریخچه عملیات‌های پرچم دروغین آمریکا و رژیم صهیونیستی در ۷ دهۀ گذشته نوشت: پرچم‌ دروغین، شگردی دیرینه‌ است: اول صحنه‌سازی کن، سپس انگشت اتهام را به سمت دیگری دراز کن، و در آخر از نتایجش بهره‌مند شو.
🔹
در وضعیتی که افکار عمومی آمریکا و جهان از جنگ غیرقانونی و تجاوزکارانه علیه ایران به ستوه آمده‌اند و متجاوزان هیچ راهی برای توجیه تجاوز نظامی خود ندارند، آنها مانند کسی که در حال غرق‌شدن است برای نجات خود به هر تخته‌پاره‌ای از جنس دروغ آویزان می‌شوند.
🔹
بقائی پیش ازاین با اشاره به اتهام‌زنی‌ها به ایران در ماجراهای پایگاه فرفرود انگلیس و پرواز فلای‌دبی به گفته بود: گویا رژیم صهیونیستی و مدافعانش در اروپا و آمریکا به دنبال این هستند که هم موضوع فلسطین و غزه را به حاشیه برانند و هم تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران را و این‌گونه القا کنند که گویا تهدید جدیدی از جانب ایران متوجه منطقه یا جامعه جهانی است.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/466883" target="_blank">📅 20:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bilv1Z69WG5qpyeqgBc0edgQPELv0ydoeCOXNMF4perP2CUyvWj2gnUiTz2Xdug-5SNnQSgsyvhy_kS9hSHHdikz-JCyQ8M91JMh5D1iDUG_mQ4qD0gABYAI7jGFM7KOAV3h9LqArpFmGtK8HI3uMDeRDzt6NX224owDY_U5k7QbsDgMaQFrDB4Qj5R67BrrdEgPktPx3X7vijDU6Ho0xjW2kfVW1VnfFw6etcm1ExnLUonNjZGuc3EEbPphxfA3VTvD4jaAlwvoiLQJNNN4KQ3KlbOUK1vJJbU7NiYwJg4GQ0TB70RvBRhEyLNahC7wovV2Vgo_3lwj2Ss3R9EUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار تهران: اولین محمولۀ متروباس‌های ۲۶ متری با عبور از محاصره وارد ایران شد
🔹
زاکانی: امروز ثابت کردیم محاصرۀ آمریکایی ناتوان‌تر از آن است که بتواند جلوی ارادۀ ایرانی‌ها بايستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466882" target="_blank">📅 19:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اکتشافات نوین، مطالبه‌ای برای شناسایی دقیق‌تر منابع شد
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/466881" target="_blank">📅 19:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKEJ7Ehh2oAhrWBRXQsPyn26iYNK-7aPqbn-sDcY6XmmTTkH2PTT4vJdw-3EYorXd0QkWM3qoUmtyPeemTqPo0vze0aqaI3SG18Jb-xE2kHV8d5znfPB703xBHnPkMPJMQ4_GgSM1HLLZHniIfTBetSRvgNSXrFUage0Kh0I9_u6yg6uasFOSAuLsyGjZzStE6vwJ6xP6Ks2e8gXuTSeZNhNcL1W_vjZd7fTlHZOE3cw1PGHevktjsA1m2JMZiYxhkR2EXCHwrbMQw-4VFrusae6TKoIwrLkWdPrHKExpVV-LDiZKYmdqYEBP57pH5x8nlt4Q043NAs0YR8vgXZj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد نفتکش‌زنی در تنگهٔ هرمز شکست
🔹
رویترز: طبق اعلام منابع رصد حوادث دریایی، تنها در یک هفته اخیر ۱۳ نفتکش در تنگهٔ هرمز هدف حمله قرار گرفته و ۷ نفتکش هم پس از هشدار از ادامه تردد در هرمز منصرف شده‌اند.
🔹
قیمت نفت امروز از ۱۰۲ دلار گذشت و پیش‌بینی بانک‌های بین‌المللی افزایش شدید قیمت نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/466880" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌ احضار سفیر فرانسه به وزارت خارجه ایران
🔹
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گستردۀ حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد.
🔸
اداره کل حقوق بشر وزارت امور خارجه با یادآوری تعهدات…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466879" target="_blank">📅 19:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز آمار: سرشماری غیرحضوری نفوس و مسکن از ۲۵ مهرماه آغاز می‌شود
🔹
۳ گروه هدف ما خواهند بود که برای آن‌ها پیامک ارسال خواهد شد. پیامک‌ها حتماً با سرشماره مشخص ارسال می‌شود و لینکی نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/466878" target="_blank">📅 19:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uo39bRHe0ykJBiUqwyin8IvNNE8BqJH7z1VQbqlTWDz_hWqgQm-veE0dTBovNTCp3go1cxvIVCxqbYqrNrNJ3XUX-NkaaBhgm-AMcNEzHUWDvVatrAN07Pa_sWjbTQLg4evFtpoKUOlMqXKITG_d06oQQ51dWKd4mF6Mq11CbDPfx5N9I0sZk4Af0Qsh61mLRMn8swYf6mz1Sr8MJeikww9mC0astiJs1IS7XoTDXoNokniv-fbRj3e_rXbgJ43cHkhNC-73VUgeOQtR4vTHTMj7oHlT7EZmhPNwpK5AlxqLagn9Ig0FLO_VEjA81PL9qJHfHWBOcedQEebRgbq8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVGn_fMTn_gLxtTVTzrDY14umVCTG4dctfj8nrVfHmg0imMe9C17MMbUKjfcQU0utF_mQYoWUwAsJcV78E81HiazguEk6MX1GBKguEJfwnxxuF7zN5soAZVEdNioxRbaBPkdgr2GtKZ2QmkZgXY84NmOL6FkPbJ2_0JBxG6fJNSdWfzp6ZiV1dX_yDWZI4balzWdYr87RgjIu2V3uRJOkUj9vLHc8EGz4PplnU-8G-aDhp48C0MfpNr3UV_XlU9lzpMGiIEqOcgz--Tme6GjT6gwckH74tuB0PdP7TWj-0j3sgQY0AwwaF81FOhNiScx3Yz_D_eHYpzFUAM5r85FXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو بحران‌زده آمریکا با کارنامه‌ای پرحاشیه به خانه بازگشت
🔹
ناو هواپیمابر «یواس‌اس آبراهام لینکلن» روز چهارشنبه با ورود به بندر خانگی خود در شهر «سن‌دیگو» واقع در جنوب ایالت کالیفرنیا به مأموریت پرحاشیه‌اش در جنگ با ایران خاتمه می‌دهد.
🔹
وزیر جنگ آمریکا پیت هگزث که به دلیل مشکلات و بحران‌های ایجاد‌شده در این ناو به شدت مورد انتقاد قرار گرفت، به شهر سن‌دیگو سفر کرده تا از خدمه این ناو استقبال کند.
🔸
رسانه‌های آمریکایی ماه پیش گزارش‌های متعددی از شرایط دشوار زندگی بر روی این ناو اعم از کمبود مواد غذایی و محصولات بهداشتی و همچنین مشکلات مربوط به وضعیت روانی برخی از ملوانان منتشر کرده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/466876" target="_blank">📅 19:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: آمریکا و عناصر صهیونیست و بعضی از دولتها برای غرب آسیا نقشه طراحی کرده بودند که عملیات طوفان‌الاقصی آن را باطل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/466875" target="_blank">📅 19:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c86a2176.mp4?token=SL0614sf8EUNfYRwKK5dO-6k9HPzXlWTLSHFKrc6FRQ5j1dsdDhcHpS_n-DtuFSnMOOd_CQlg3EkY2RzBbqfDZ9tfGy3--430nZqMNMnEUMgqTOlhJeA5zpibr4SNJST70Y3aWOjm8Yba7VHk9IZ9ZXgJ_9VMdZm9m5fT-Dvw9JRoWYhW2nRLW6nJ8YiWClMG5TLarBwrmQtNxMAGMDQr-7ukCIo7_diqXiQ_JefHa-7AQrgBD9w4Bh1BqCtPfXGR4AJO-9Y12-b-x5U4S5fwOqey5QPaSu33X9_crEpUjPg1zv447mHsDfIEXr6gllJHyIsLPptnqCLSP6O6-5_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c86a2176.mp4?token=SL0614sf8EUNfYRwKK5dO-6k9HPzXlWTLSHFKrc6FRQ5j1dsdDhcHpS_n-DtuFSnMOOd_CQlg3EkY2RzBbqfDZ9tfGy3--430nZqMNMnEUMgqTOlhJeA5zpibr4SNJST70Y3aWOjm8Yba7VHk9IZ9ZXgJ_9VMdZm9m5fT-Dvw9JRoWYhW2nRLW6nJ8YiWClMG5TLarBwrmQtNxMAGMDQr-7ukCIo7_diqXiQ_JefHa-7AQrgBD9w4Bh1BqCtPfXGR4AJO-9Y12-b-x5U4S5fwOqey5QPaSu33X9_crEpUjPg1zv447mHsDfIEXr6gllJHyIsLPptnqCLSP6O6-5_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: ۳.۲ میلیارد لیتر سوخت برای عبور از زمستان ذخیره شده است
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/466874" target="_blank">📅 19:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: ادعای سعودی‌ها دربارۀ قصد یمن برای هدف قرار دادن مکه و مدینه، افترا و دروغی با منشأ صهیونیستی است. @Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/466873" target="_blank">📅 19:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
رهبر انصارالله:  سعودی زیر چتر آمریکا قرار دارد و تحت پوشش آمریکا به یمن حمله می‌کند. خواسته اصلی سعودی نیز ورود مستقیم و همه‌جانبه آمریکا به این جنگ بوده است. @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466872" target="_blank">📅 19:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هواپیماها و تسلیحاتی که بارها و بارها به‌وسیلۀ آن به یمن حملۀ هوایی شده آمریکایی هستند و استفاده و به‌کارگیری آن‌ها به آمریکا وابسته است. @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/466871" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: اگر کشورهای عربی همان کاری را با مردم فلسطین انجام می‌دادند که غرب با رژیم صهیونیستی انجام می‌دهد، وضعیت کاملاً متفاوت بود. @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/466870" target="_blank">📅 18:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b32e36c8.mp4?token=AJ9l-gD7gomVIxnrvfSWIhJfJczJWvk095csTmlHhaBAGCl-HSY1uOX1FC8EIq85AOyLJWnhnnCEMbJim0eSuHUjthn6F1hOr0BQH3XM8xbwmy91by9WEOdWOCAJZhXsqX2v1orgeO1MNTOus8E6XH7pqIVQoejQRBSrzd4bFiC6-d-fxaMba_-1A7HiMlhKav3g6gxF4ybM4GnnPdvlxCOS8zKf8hVAnOOtVhABmTFsugZTlOgwp8BFcZgesRgEBXEeCMPbFXkFmdqHJ7dZiQkovQLQJ1-F8-aI3Ie9VqD73DSbhVPbfyiTt7t7uJuNo54LWltraZcyHzbZN2y4Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b32e36c8.mp4?token=AJ9l-gD7gomVIxnrvfSWIhJfJczJWvk095csTmlHhaBAGCl-HSY1uOX1FC8EIq85AOyLJWnhnnCEMbJim0eSuHUjthn6F1hOr0BQH3XM8xbwmy91by9WEOdWOCAJZhXsqX2v1orgeO1MNTOus8E6XH7pqIVQoejQRBSrzd4bFiC6-d-fxaMba_-1A7HiMlhKav3g6gxF4ybM4GnnPdvlxCOS8zKf8hVAnOOtVhABmTFsugZTlOgwp8BFcZgesRgEBXEeCMPbFXkFmdqHJ7dZiQkovQLQJ1-F8-aI3Ie9VqD73DSbhVPbfyiTt7t7uJuNo54LWltraZcyHzbZN2y4Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسخهٔ بانک مرکزی برای مدیریت بازار ارز چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/466869" target="_blank">📅 18:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: جمهوری اسلامی ایران در راه مقابله با رژیم سرکش صهیونیستی فداکاری‌های بزرگی انجام داده که در رأس این فداکاری‌ها، تقدیم رهبر و امام شهید انقلاب اسلامی ایران، سید علی حسینی خامنه‌ای (رضوان‌الله علیه)، قرار دارد. @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/466868" target="_blank">📅 18:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نقشی که جمهوری اسلامی ایران در قبال فلسطین و منطقه ایفا کرده و ایستادگی آن در برابر استکبار صهیونیستی، به نفع همه امت اسلامی است.
🔹
صهیونیسم و بازوهای آن، جمهوری اسلامی ایران را بزرگ‌ترین مانع در مسیر حمایت از مردم فلسطین و مقابله با طرح…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/466867" target="_blank">📅 18:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: بزرگ‌ترین خدمت به رژیم صهیونیستی در لبنان، پایان‌دادن به مقاومت اسلامی است؛ مقاومتی که در برابر طرح صهیونیستی برای منطقه ایستاده است. @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/466866" target="_blank">📅 18:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی در ترور شهید عماد مغنیه نقش داشت و از همان ابتدا از تلاش‌ها برای ترور دبیرکل حزب‌الله نیز حمایت می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/466865" target="_blank">📅 18:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: تروریستی اعلام‌کردن گروه‌های فلسطینی یکی از مواردی است که حقیقت موضع سعودی در قبال مسئله فلسطین را آشکار می‌کند
🔹
رژیم سعودی در محافل رسمی لبنان برای خرید مواضع فشار می‌آورد و همه را علیه حزب‌الله در یک جبهه مشترک با رژیم صهیونیستی و آمریکا…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466864" target="_blank">📅 18:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
رهبر انصارالله: سعودی‌ها از مسائل دینی علیه امت اسلامی استفاده می‌کنند
🔹
بن‌سلمان اعتراف کرد که رژیم سعودی از تکفیری‌ها حمایت کرده و دوستان سعودی در این زمینه آمریکا، انگلیس و اسرائیل بودند.
🔹
سعودی‌ها از عنوان «جهاد در راه خدا» استفاده می‌کنند و امت اسلامی…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/466863" target="_blank">📅 18:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44953e3252.mp4?token=ObDFPDevIzlz_rVfD7ZSKpJbmcqJof9wwiIP0WrSj0w48FGOxbL8gsMTQSPSLB1zsPxc-X7h15z8Lld1GSxnIZgcttSoQ1DUF-TNtEcS6WFElGGCMLXmgJaoUxI1Vv8NMowIJq4OY9QKtax0l_KcXPBL77Yxq6BiqcpD5kVEhz_jnDaVIePTbMP5SIdNwu--esstsPKKSZ2H8CrMgFnA1Npk6nNf_wnN0WpIJYPKskN8z0TKF-3LxfdQOuMrl7kCp6pAO4fKQVxv2DaW0zQmNnnD5Fu9Eq08tLgKF25-9zphzG-Eucqr_Qpd0ZBqx1Y-hahSfiCxlok14-3E3eyTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44953e3252.mp4?token=ObDFPDevIzlz_rVfD7ZSKpJbmcqJof9wwiIP0WrSj0w48FGOxbL8gsMTQSPSLB1zsPxc-X7h15z8Lld1GSxnIZgcttSoQ1DUF-TNtEcS6WFElGGCMLXmgJaoUxI1Vv8NMowIJq4OY9QKtax0l_KcXPBL77Yxq6BiqcpD5kVEhz_jnDaVIePTbMP5SIdNwu--esstsPKKSZ2H8CrMgFnA1Npk6nNf_wnN0WpIJYPKskN8z0TKF-3LxfdQOuMrl7kCp6pAO4fKQVxv2DaW0zQmNnnD5Fu9Eq08tLgKF25-9zphzG-Eucqr_Qpd0ZBqx1Y-hahSfiCxlok14-3E3eyTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رهبر انصارالله: انگلیس رژیم سعودی را ایجاد کرده است
🔹
انگلیس رژیم سعودی را ایجاد کرد و نقش مشخص و نامطلوبی را در جهان اسلام به آن سپرد. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/466862" target="_blank">📅 18:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
رهبر انصارالله: انگلیس رژیم سعودی را ایجاد کرده است
🔹
انگلیس رژیم سعودی را ایجاد کرد و نقش مشخص و نامطلوبی را در جهان اسلام به آن سپرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/466861" target="_blank">📅 18:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای انفجار در بانه ناشی از عملیات انفجار کنترل‌شده ارتش بود
🔹
فرماندار بانه: صدای شنیده شده در منطقه، ناشی از عملیات انهدام و خنثی‌سازی مهمات عمل‌نکرده باقی‌مانده از دوران جنگ بود که توسط نیروهای ارتش و به صورت کاملاً کنترل‌شده صورت گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/466860" target="_blank">📅 17:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qkg4yzbl0ohO57E6IP1tjIChgfp0TYRIbZn6wzDj_NVMpDRArWxAlCCMObsk8lG5oxlOk3MNKGYwzdk2AKkhx1LnlihNam6wyRMr-E0v4REhCT7G-LIniWu9ziROjlNSRCXoztDQ7QYryPn0aogADiO-N3XCmSmH0ZLJhjrksilzNvphEYOH9Sm3tBdoAx6nVkIYiIuyoa3glUhpP_YDWTvCmQOsWPw_IEdyE8EM6u8L4VW2Kr9Gy_1E3NHqViVdrZ-yq2Qecfhh6u0q4-ctbrH15np5j8THeNmdbXhd2ilONvwfrQBVbVHolyc-DMl6XN5BiL15q6mpyg7S73PUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtxueVoItqfZnAZgDLCb3Se2ussMGSL_Xd8JlWokBl233H5lvpsruW6-7D-PpkFdJkLiGE_5SjggHpzYiYe0zL3cNdZs6FwrjxkVCloRSHBn02IuBbYsMsAWbOcOiz3Krtr7wwyySMvyhDvWg6Qp7K2E2pGXA8Ez9xAAyZqen2MO3dz25CRXtziPXJrYx8GnHEoy88x4DVCDcvzQPPI9xVcoCVpwqRKImBZoXGx14qnokC0o7NemQLtOEVpxK8RRs_sr8EjWn4pMi9lpb2b_gfbHfMSb9E3tyaoPBvmP3PqVn_8gLsewh_598aC2jEnRYJNgpUjt5G8On0LxMzGltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcTy5TFRs5HOAoeVq3-M7l3IBhvls5ZW8Lqx3RxykDY9S07SsMc83TQuMLaCUfwu4xr0vReHiFkQCpW8b36tFcN1cdxXlF6tnpseKsh_1TvHo3yHQ8nPO09zdtY6rpHVAgP9bfgoCA_eoPZq0yV45qv-8sZkH7U8UOp3qLNlKuulQqS_T9bg5B8x_Z51gOgbf_PqLWiA0HU__L9pfDZ3nUAZhTVslDTCL-4mZCAiX5dqQHOHeA2a4ylSHH0EELvdO9BLRcCDV5JBBA5ptMpr0_Bz6wC8Uo7TZoO58YMzg-9jilegwaWz_VUJtT8Snh-h3nSqvXP9KWCfIUX1FpvyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okxOTBpjTLYT97PZlfKQIxhPskPNenPcL05hIchD_wOockrvsWMNxD0WAgM9TtcwGfGI-tDPtAJMTGsCgKYkiTc37mP6uIN1PYpNTe9-RZtCjzWgiWkumZhkMxm3uSadLSSqm0fHSZMc0EcSm7ksZf6tM37gy8QsmYYW0NIe3dGPSPd5BAXMqiok2FYatvYMZf8PIrk3-ldCaAyZiAd6SzzzvQyN1DPmZjq9q3ysNfIpkURCjMZr6srsjzPGL-lAwxgJG3Yy5I_4aHXEHuiv2i_wkJuhTHFV87zLeICouJeWB9ip2NU8xu8HicKxoMqLvogrjCi3MLB01aDFYsyn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3SJmNQDYSJVe1CjrNH20sbbfoBXuI8-0Ivpoz7fqOzdyIUNJ-uPxLP-9_p6O9Hsx3bJPwEI3t8Yc7rU5OFeS-LoRUIhWMOlWsSNZM4ZaCssJNF6f09cWJ0NEsd0MOtNrowhF-AN2e7GXwRV6ScaFjFzIufS4niZsy3vlz6VfX376vTIv_XkKd8TuPl95cHp0XSjVzOh23UJJ5ifEpo8IwjeOQ4XooDvSr_8WgROTVQQc0BDahSy8VB9CdfmiqTVrfbmUW8X--s7eEphWQwLkcdpy93FoO0NhN_QWyB7-3TTqDsjI3Vr8dxTgEOSGXGsxnpE9NIX6bSPS3sT0YQm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJYyOhnT_zpB8HpQkczJj49X7QJkbvcrGdc1pto4moCoisoQ1jDAOnfm04gvzDi8aMLkz_UVG_DFVvxRO79Up8mqB6KD2_ytKbRtS8ORNf_ULzuIkVwRsU8nJ6INzvqkeeLNXD8nyfeJO5JVuTLWXV-q1AnkC6EgzbwFD92wDzDG2W5u0GHmLD2c2ZvXKfusBRg71kP0I-pgt3WJrezcctvjzPy_exP7ihpWvyp3ZJXZb0E7Qq4eOG0ZsOMlNdEbPc2zuS4Bvjso7SX_cdUhG1JlV0Yy6PEg7CEI47uKRrydHfBeA9Q7Ua4csx0bhGKHYHr8FLyd3ZeQipB149KN4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مشارکت بانک صادرات ایران در بازسازی قطب علمی دانشگاه شهید بهشتی
🔹
بانک صادرات ایران با هدف توسعه زیرساخت‌های علمی و تأمین مالی بازسازی پژوهشکده لیزر و پلاسمای دانشگاه شهید بهشتی را از محل اعتبار مالیاتی بر عهده گرفت. این اقدام که با همراهی وزارت امور اقتصادی و دارایی انجام می‌شود، گامی راهبردی برای تقویت سرمایه‌های انسانی و «ساختن آینده» کشور است.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#بانک_صادرات
#گزارش_تصویری
#بانک_صادرات_ایران
#دانشگاه_شهید_بهشتی</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466854" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyBQWrx-xwn5gae4TwLrmZbHN5Lqz78Icn9w37Mk9EUg1QC9mI_FXI0zASBpfzHO_177vLfbX242N5hezYRaJp829oisY21nBUWSsomj3SEPh8Wzj41ZRX2AP_gatcaciOkR4gLY0dRHLUlZYbGi1eBM_k2qqnfA3ocMqQHAjEDKCqolefgC9kYmtupJ6jivb6TBgaItWuTTtcpTnvYZ0Eky8KteVYU-9pN8SPHsGjv1kZd-2ZEW-EeMzwjPmH3Ya3JERou-Cdnf9MGtKBgvCC9K84y1I9M4hmD8ilYWZszmwEWt04GK-MOKYP5kODFoYV9VCiXXIJnDtTVckCTVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید اعضای کمیسیون اقتصادی مجلس بر نقش‌آفرینی موثر
#بيمه_البرز
در چرخه اقتصادی کشور
در نشستی به میزبانی بیمه البرز و با حضور جمعی از اعضای کمیسیون اقتصادی مجلس شورای اسلامی، نقش کلیدی این شرکت ۶۸ ساله در تقویت اقتصاد ملی، حمایت از بنگاه‌های تولیدی و مدیریت ریسک‌های کشور مورد بررسی و تقدیر قرار گرفت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5108</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/466853" target="_blank">📅 17:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/466852" target="_blank">📅 17:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1e3f4f16.mp4?token=Dep9FpUxlvBpu7cq2qjvYLoHShdZNtjt2wxnfm9mh-xXF7q6ZpVqp7dOvdGo4yPOIMZRCtgL_lrGVik-jTmtouFv-I24SwIlU26bNIY6e88R6m7Ygu-wAOXdME6UQNFMKVL2JzFF7IL52h8XzTbyh9aglYDN0LcuuHHkwlStrSnDG_XKAE42zp2NgpXrL_SUMCAanbD6bHA_2kwX0eXMAJwuaOUODhPJtIrYaKheyKUHt5nYV9l76PoJmZTicY11O06NSVSpKixb-hlb-dgp3Oud4dfDq4OM-Z5x1V9NL48RvH_EHZv7mpklakPV-UEkDg3tELCaT3uAlTKkSeNOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1e3f4f16.mp4?token=Dep9FpUxlvBpu7cq2qjvYLoHShdZNtjt2wxnfm9mh-xXF7q6ZpVqp7dOvdGo4yPOIMZRCtgL_lrGVik-jTmtouFv-I24SwIlU26bNIY6e88R6m7Ygu-wAOXdME6UQNFMKVL2JzFF7IL52h8XzTbyh9aglYDN0LcuuHHkwlStrSnDG_XKAE42zp2NgpXrL_SUMCAanbD6bHA_2kwX0eXMAJwuaOUODhPJtIrYaKheyKUHt5nYV9l76PoJmZTicY11O06NSVSpKixb-hlb-dgp3Oud4dfDq4OM-Z5x1V9NL48RvH_EHZv7mpklakPV-UEkDg3tELCaT3uAlTKkSeNOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال‌آورترین کشور عربی با صفر مدال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/466851" target="_blank">📅 17:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE1EOrJQ51TIxifZt6bS1eCU_g_t42vUmWynsKi6UjndWsYpSYoc-VDuPhF2B8wwcQ_1V5rzUHbNwi-RwZQryecVdOBUj-n2oaNs_JW_yjF5HBdeSI7uzV_Ke5HSpfiUX2IdPfv1iOzMm_vrbOwTlsdtHKvVFUZvJ6GVb1umnum47WU1QU18LKOkWVMl6yMEV6mIk-UvB8w2um_AaZ1a6fBpXMLJaSoDj-As0A5N96bkMesQm_MBCNb2fS5ggXQtXQTVRFUIJxMDp2yu31UOWm61L40EC4JApPuFDa0EssU8KCkMmAVFBo4anrkXFcwXWtxiJ2c7unqxGm_5nFyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج : هلال‌احمر در جنگ ۱۲ روزه کنار مردم قرار داشت
🔹
حجت‌الاسلام والمسلمین طائب: براساس تفاهم‌نامه میان سازمان بسیج و هلال احمر، مسیر گسترش همکاری‌های ۲ مجموعه از امروز وارد مرحله اجرایی می‌شود.
🔹
تلاش خواهیم کرد ظرفیت‌های مردمی بسیج و جمعیت هلال‌احمر بیش از گذشته در خدمت امدادرسانی، مدیریت بحران، مقاوم‌سازی و افزایش تاب‌آوری مردم و کشور قرار گیرد.
🔹
مقاوم‌سازی جامعه تنها به حوزه دفاعی و نظامی محدود نمی‌شود، بلکه باید همه ظرفیت‌های مردمی برای مواجهه با بحران‌ها فعال شوند و جمعیت هلال‌احمر در این زمینه یکی از مجموعه‌های مؤثر و برخوردار از ظرفیت گسترده مردمی است.
🔹
در جریان‌های جنگ‌های تحمیلی اخیر، ۵۶ مرکز هلال‌احمر هدف حمله قرار گرفت و شماری از بیمارستان‌ها و آمبولانس‌های امدادی نیز آسیب دیدند.
🔹
هدف قرار گرفتن آمبولانس هلال‌احمر به جای یک هدف نظامی، نشان‌دهندهٔ ماهیت حملات دشمن و بی‌توجهی او به اصول انسانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/466850" target="_blank">📅 17:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ساقدوشی سلبریتی‌ها برای یک قاتل وحشی
🔹
برخی سلبریتی‌ها با انتشار مطالبی در صفحات خود، به حمایت از علیرضا سپاهی، قاتل جنایتکار میدان علیخانی اصفهان پرداختند.
🔹
«مهشاد و علیرضای عزیز پیوندتان مبارک.» این متنی است که حامد بهداد به تازگی در صفحه شخصی خود منتشر…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/466849" target="_blank">📅 16:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThPrxFRh-9pe3Jwf5wC5jPwK0RCSQwlShw9Gr5pjy05VJmxTqfVlFo6WLJpds1EWXYFGfixJOExd-_aeg4zSK1-chX7F5LIO2sVts_q3HVUk_AdI2Gh2eosK8KC9lUHoY70q6IDeuuRA07A-5nBnrfSytFKEgLvRkY6cniEE1i-xM16TqOYjOKIXAlNuCzJyX5K6aQreYv_IN8p9EUM8N3ToDiiOAS3PcE9by_pfUWy-ef7PA8jlNB7wkN8vv9hMkRjri1q7K35XxD_20i7MZTBgIYckd15qShTscU9a2c76dxStB25NB7vsCXIZlkSAyBqVk33ycH4Sro4mr-FSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdr7T9nzez_1mXm_PdvVL-UTLWbTmku6pKqcDoTB3hvZEJYSWqlIZorS7Vzt2a3xSNoF9-A1hZWfFPbsSd5yQnGd-pNRZFC4mL2P2yHYMwYGP2HCkyX1_P8FRt02IvQlCAvboNjjM9Kup__9GmaWoark44su4uXqKvuYanlubxdBA_xs-HSZU9yF4AaIadny9S1wRd0VbE1qI2LPQSzkhxMinUc0CKm-vjR9cxtoxY7aZiggIbGfLVwBqBvF2e2QSbfaO-iUkdd8LP4V0n1LUV1FR_chUF0pc4sLYFYiY1MrfnjOmUdQWG7VTGnjSpeLCmw-bzEDNIGVk0TEdDRrzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عیادت نمایندگان رهبر انقلاب از آیت‌الله نوری همدانی
🔹
حجج‌اسلام والمسلمین رحیمیان، محمدی عراقی، محمدیان و حاج علی‌اکبری، بعدازظهر امروز با حضور در یکی از بیمارستان‌های تهران، ضمن ابلاغ سلام رهبر انقلاب به آیت‌الله نوری همدانی، از مراجع عظام تقلید، در جریان آخرین روند درمانی ایشان قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466847" target="_blank">📅 16:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تجمع مزدوران سعودی هدف موشک‌های یمن شد
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای متجاوز سعودی که قصد پیشروی به‌سمت مواضع نیروهای ما در شرق استان الجوف داشتند را با موشک و پهپاد هدف قرار دادیم.
🔹
در این حمله ده‌ها نفر از آن‌ها کشته، زخمی یا به‌اسارت درآمدند و تعدادی از تجهیزاتشان نیز نابود شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466846" target="_blank">📅 16:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWuzFew6gVBeT-x5Fwf_pLjYreLYpPH6bAzpp-XObjIapllwy8Ypv2-6q15Rmb25zULde2a9jUc2-v-mDaHuLQD5mWUtCZJL1uMyWDu4R1AW2lWPcfxsShlT7P57bVlbQX68jKS8nJfO7CwlG5y2pL5QMzOS3rwn-b5EiyYVoyCKuwwBN0Tld7M-BaNqlqb61exhSs2sBDd_8eXOV2mUKyU14nuTrTJre-ZjUuUDgnO1ij_GJkBt_m-RyzyMGmon5GGLFZmpHKEl66MBjaBIeyRq_w1MU2Ivp2erEGbLflqmRPiMTaPrdf3FJiGj3Q6pCgX6V0XFLwmIYbyjiOeAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF2X-g5FfQfFvvSehcCShwSK90Hv7Yj9IPMq-W097n8h3pNoZRS8VJu_K6ytfixbQmW3oaHzPRnH5WwUR7-1-882h3e0wAe9pd-rJYLgadxEMeGpb1uxkz6FH1TRQNh6LD_sOWLeS8WwrqfC5ls1ZcAIQS6R_bCx85yvJ3EMTRcQ3Ld1hfNYMSV_aPtRR1PEDbhurq0LCCQF4BSWfSaVPjm4mDuAbjEWjvmTLM5fSOqC9Ke-U1VRP30Qz1k97sNPVWHDBRtHUT2gVqVlpxBOm31TCbEF3NgXuveOTCJDSn7WR6-I9OI8W_D_KFcmAPKmfsGFGBosRr4TRxaHxaib2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همواره گفته‌ام که بعد از دوران دفاع مقدس ۸ ساله، دوران حضورم در نیروی انتظامی را بهترین دوران زندگی‌ام می‌دانم.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466844" target="_blank">📅 15:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کالابرگ دهک‌های پایین اضافه نشد
🔹
بنابود رقم کالابرگ دهک‌های پایین از امروز اضافه شود؛ اما پیگیری فارس از وزارت کار مشخص کرد، رقم اضافه‌شده تا لحظهٔ انتشار خبر واریز نشده است؛ علت این مسئله به نتیجه‌نرسیدن این مسئله در دولت است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466843" target="_blank">📅 15:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4khqLUMITWVowJctxuSoJBUsCGe5QvQa5qLhLVsHMUww3_la8rCCA7jDVUJPSfhvtUQE1KzN70Q1F-SQOy-bFHf5YlUN--TnH_PZWdOPGlKmv09bzBRtNqfn9RBqG-aJ8LTVB3ZPQ9vaHz9a0qYlcLbhWxNO3GpCcFwgoMWM_PviE-Z1CPKf7NxcX7Ndh9GC5l-YINnCeC4m9hNuZth_JYRcN7ewbFgEh4ZU3ZkR4_49s-hzwFu5JN_39ng52Deb-pYCQLeKmj8uRaBW9SQ73bWJ_mjkZwMSBe5fWKCX7bN_6gKVI9GwaEztqg5b_XQoTx0D-qa22tTiLR6XanbHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ نوبل فیزیک اعلام شد
🔹
جایزهٔ نوبل فیزیک ۲۰۲۶ به فرانسیس هالزن برای مشارکت در رصدخانه آیس‌کیوب و کشف نوترینوهای پرانرژی کیهانی اعطا شد.
🔹
این دستاورد راه را برای نوع تازه‌ای از اخترشناسی بر پایهٔ مطالعه نوترینوهای کیهانی باز کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466842" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419ab3f210.mp4?token=UiEnWtAoJnNnjQy6MyHy0Bvz-TjH3Nnz8LxSKx7fvphT9j4VbCX-D7I5pwamLcloiT95fFqY3DAsJAbyo2kzewlGa2BYMS-F2cuFjJH6WS_yz3Dwwn_t-y39W85EMy4puI8_6VjfM4WkdX6PPz2aQQ2kbXtwfieMWi-22GmVwwh6Lnizx2SLgfG5z-nSQOeC79mMuWXVP4XxQXq1HL8bng0_K4fGkrSBrPXyThLf1t5svr-feICwh_6nmP0w2s6Ff33Z-4t4FcgI58iFHltgMbTpAtwN2jiGGPLc4lCzPI5pflEKNMucEweJ8wUrePucxz57wvSGqQ-FxzRrCJ6qJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419ab3f210.mp4?token=UiEnWtAoJnNnjQy6MyHy0Bvz-TjH3Nnz8LxSKx7fvphT9j4VbCX-D7I5pwamLcloiT95fFqY3DAsJAbyo2kzewlGa2BYMS-F2cuFjJH6WS_yz3Dwwn_t-y39W85EMy4puI8_6VjfM4WkdX6PPz2aQQ2kbXtwfieMWi-22GmVwwh6Lnizx2SLgfG5z-nSQOeC79mMuWXVP4XxQXq1HL8bng0_K4fGkrSBrPXyThLf1t5svr-feICwh_6nmP0w2s6Ff33Z-4t4FcgI58iFHltgMbTpAtwN2jiGGPLc4lCzPI5pflEKNMucEweJ8wUrePucxz57wvSGqQ-FxzRrCJ6qJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: نتایج نهایی کنکور نیمهٔ دوم آبان اعلام می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/466841" target="_blank">📅 15:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پزشکیان فردا به ترکمنستان می‌رود
🔹
رئیس‌جمهور، فردا به‌منظور شرکت در هفدهمین کنفرانس دولت‌های عضو کنوانسیون تنوع زیستی، عازم ترکمنستان می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/466840" target="_blank">📅 15:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ielfZSzrGDGj40bW67Tfd9FZT4no_6cuFOAyptrmNvJHO_svY0rFCXHmnA0mDvfoGSvkrwVS41M8UcDGbhMbklSUJ8P3aC51yEFVpV_r16sj8kwtT5hdOWLnSpEakkBRCObufM88F84NkIVcni38KE2AtmApq8uOcu0bPJRNg35ur2Gm0JIEHxGelVYs0Fhgu1xcPz-gxDeli_N2XtMOfx59n5Qqem0TMZ25YJvM2M3OpHZX24CuThnra_x1UWEONnM7yYwh0TlNNAOqfSRbVPV8u7l04vwGdQ5G93y-HNmCiF61MaKSodGb08T3AXRJLfyyY518G2Sw8bQ35dGEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قریشی: بسیج عشایری باید ظرفیت‌های گستردۀ جامعه عشایری را در خدمت انقلاب و کشور فعال کند
🔹
جانشین سازمان بسیج: حمایت از جامعه عشایری یکی از مأموریت‌های اصلی بسیج عشایری است.
🔹
عشایر را نباید صرفاً یک «قشر» در کنار سایر اقشار جامعه تلقی کرد؛ چرا که جامعۀ عشایری مجموعه‌ای متنوع از اقشار و گروه‌های اجتماعی را دربرمی‌گیرد و از ظرفیت‌های گسترده‌ای در عرصه‌های مختلف برخوردار است.
🔹
بسیج جامعه عشایری باید علاوه‌بر فعالیت‌های فرهنگی و اجتماعی، مسائل و نیازهای واقعی عشایر را نیز دنبال کند و در مواردی که امکان حل مشکلات از طریق ظرفیت‌های موجود در کشور وجود دارد، مطالبه‌گر و پیگیر باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/466839" target="_blank">📅 15:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466838">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bff72e06.mp4?token=fGJ6VgqIieTod46m4D2wjtM-Q204VfDZv-4gcrKG5xEu3lKVXe7CvmoE_zM2NFut1X8zcQuwjO11rF95hDHzXFwTlcQNILabmfpUleSiqWohYRGUC89prMfo6_O_d1nEC75Ix0DBeO6NSSxYFebK2ZPfYJnUCEHVdBO4VbCmvNowqbtEhxvZXY2yqdprwbqfpma1jnQCm4g2YhHbFNNmrb_IYaDzHbMGpnx6PmqW_4sA4xsu53KRbPeOS_R8LOR_RQyOOcE0xM3wrazLogjg2fTcP5nHcikKjssk1VS4aqDAnEZwfaNcJJRV_L98kKRZAoerrDKhr1bldPjgEZWKNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bff72e06.mp4?token=fGJ6VgqIieTod46m4D2wjtM-Q204VfDZv-4gcrKG5xEu3lKVXe7CvmoE_zM2NFut1X8zcQuwjO11rF95hDHzXFwTlcQNILabmfpUleSiqWohYRGUC89prMfo6_O_d1nEC75Ix0DBeO6NSSxYFebK2ZPfYJnUCEHVdBO4VbCmvNowqbtEhxvZXY2yqdprwbqfpma1jnQCm4g2YhHbFNNmrb_IYaDzHbMGpnx6PmqW_4sA4xsu53KRbPeOS_R8LOR_RQyOOcE0xM3wrazLogjg2fTcP5nHcikKjssk1VS4aqDAnEZwfaNcJJRV_L98kKRZAoerrDKhr1bldPjgEZWKNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از دیدار سردار رادان با قالیباف @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/466838" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8U8p7see-iaFIxJkyR74KtqVc2vg8QWWH_hnoky__02TKBj1syY7aknHBZNmMGas06JAWpaMTu7X5Ff3v7Pwyotu5zvaigv1bkNpxE6jM3CSIxb8r73S9V-4pv0cWQ9RBBC2__oqBa22SYX7FqZ1MbtJe_Yy7hZKQf_ILHpbeOl3gMTUnxK-7YuUWTah34NFD43zImd_bMN3MJda_ncPSPF_ndwE7C8aMch_VOWm-7Mnk5HQJW9a4MCnn2EUTILZ_Og79MaHdHXQJDM6hGIedsbfufNvozqY63ZJtX0srDCrVrJEJxGZARc6piK_KYx4j60ralRS841vDLrohHvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA_ce-qZTZfBJDFYwPW87ioap_e3V8-isrqX-dHYzgi25Ql_dK87lut30CShgnxXArk1ATqmufQWbhyS2sgYWYDdFNlgRN7NE62fZ1BYerwPcL4CzebzPAWuTMuLPqn2tVx1-Q5tdPsC0BCB0ciNFdvEwLl96YYFqDPzlaHLV3wpQh2pKHjvBcOhjSEOsr5pBmbiplkZUcFXpQqVAF7ktwBH-kYYuRxvG5ZdCMFNUOs-RZ5UKU28baynOJLkqCt9rWd5EmDD_owYoIAYStGiwrMBlCcefoEFfVcAb5UT7PFKGpN0lUQ3rQr3vZhmEKU0yw4WAe7OBsEPsQSGf2lFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3P02hsCtNFuxqOeG_AXv6yRt8yFE3sje7FY9kFfxYQXFES_gsclyCbJeFcgQCRU8BQyk4Q3t1tkGI6jFf8kVENVyI_HfvNMRjAuOYI88Ybwvz60zSIoSvwxjVBiGOMaD3vAFTJINBmnZgEEnKMC5sUFFmGxT1KEFNxnB0yh9B8Z7oYAhzRbJOBq0Qiltdc4mPjen6SL6YX6GUAK6qU11iLJKnuts14h_rlMeSjTfuAY8mXM_3U_2q5vlttJrhhvJM4tiW46kOLm1E5T8ljVusdnCBW5zbCj-Of98sabQkmR9T64ZLrpYvhIRi2Z3BLw_r6GKCaD3bHjx69SuJ87Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5RPbRWY55Rs3XE1fmb2sb2IH4IAapYnLpvY27kF56bq7IonwgJp3Jae40kcD6--U4ok_pf_PC3uPVlPSeGUsTHstZmcyUn52MpZW_SY51G4wKGb-UoXmCuLuVN-edCvjVkFLQyWr6Id-lYaNwTOndbGkEKvwd0v5UzCG2WO8NxCmE3wMJdZTykox3dj-aMPVVdGdJeXVRCCgdLcRjo-gh9nTe7WgcjpTeJj9tq0tXPM_FnlrX0a3-K-xzZaN1AyU3YAR1nwcNgmgqmKFQde-tR90xjDJaP5_c7ZUzXrAn1ayzTB639dChWr3LRTzIoFdPF9Ydvc6k3-wUqZQ6LVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhVPIZDr-XD2wdLK_Z95kp5IzcgE9vD_8l9q7Y219AFK8UMJLj6XD1vNm42FMl9gFnd3dQyT0dDrXa0EBPcTssSVDV8_QtKAtD-n50RNhEje93qj8ee0Qsj3a6kUpjtwIDj5J9JoHJJtcFYUj5yX20jxVRB_JByjXF1izuRUXl_oN5WxeuFAyref9ufeJkG9IYe1o4luz2G1-FEOcS_8PuqQiPyvO9MAoJydxW60MVwaMuqgxA5_cBmfqRh5nWWlTprhAtyzpDN6JOsDr_Z0hRKABXh6YfK1h7g12NHWccfyiJCCLw7uCoZzGaB8YaB8yFsDid6FPvTEKkq5mwnmhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفت‌وگوی بی‌سیمی قالیباف با پرسنل فراجا
🔹
رئیس‌مجلس در دیدار با سردار رادان در پیامی صوتی از طریق شبکۀ بی‌سیم سراسری فرماندهی انتظامی کشور، هفتۀ انتظامی را به فرماندهان و پرسنل فراجا تبریک گفت و از تلاش و مجاهدت‌های آن در نقاط مختلف کشور تشکر کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/466833" target="_blank">📅 15:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گفت‌وگوی تلفنی پزشکیان و پوتین
🔹
رئیس‌جمهور ایران و روسیه، در گفت‌وگویی تلفنی درخصوص تحولات منطقه متعاقب تجاوز آمریکا و رژیم صهیونیستی علیه ایران، اعلام آتش‌بس جاری و برگزاری مذاکرات ایران-آمریکا در اسلام‌آباد پاکستان به تبادل نظر پرداختند.
🔹
پزشکیان: ایران برای رسیدن به یک توافق متوازن و منصفانه که متضمن صلح و امنیت پایدار در منطقه باشد، آمادگی کامل دارد.
🔹
خط قرمز ما منافع ملی و حقوق ملت ایران است. اگر آمریکا به چارچوب‌های حقوقی بین‌المللی پایبند باشد، رسیدن به توافق دور از دسترس نیست.
🔹
ایران آماده است تا با همسایگان خود، در جهت دستیابی به صلح و امنیت درون‌زای منطقه، بدون حضور و دخالت کشورهای فرامنطقه‌ای مشارکت و همکاری کند.
🔸
پوتین با انتقاد جدی از مواضع و استانداردهای دوگانه طرف‌های غربی، بر لزوم احترام به حق حاکمیت ملی و تمامیت سرزمینی ایران تأکید کرد و مواضع به‌حق طرف ایرانی از جمله در زمینۀ جبران خسارت‌های وارد شده در تجاوز نظامی علیه ایران و دریافت تضمین‌های امنیتی درازمدت برای عدم تکرار تجاوز را مورد تأکید قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/466832" target="_blank">📅 15:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d623562a1c.mp4?token=HywcRk4x-v2RAgi1VbB6Xqi5P8jQXgyDtMK5g2mhsAmjfMFJqksESWxTANCDAkWT2oL53RzPAEUDxVaJEPcjmFbw5ekyNqrlQwfbodIM8PwT2yzYlTtYwCGKCl1DIPZ1B1WHSxqcXCiiyd_pTwEEao-K9gDEOZWKVGt77p_tpb0kFtX8sdGxOlkSkZ-xDHO_ar0u2YBqj9-VHoI2XNAkyiRsbYHnysTkQHQYbounYQxfnAateQCOOn86DLwCCJYR1Ukp59-wudNw5oXZgYyc0wXZL2Ss_Fy7lxWSL4pGWBXRwIgfRED9mMAgT3W3TdqYLkOO6b1JJe8srIeR-w-DEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d623562a1c.mp4?token=HywcRk4x-v2RAgi1VbB6Xqi5P8jQXgyDtMK5g2mhsAmjfMFJqksESWxTANCDAkWT2oL53RzPAEUDxVaJEPcjmFbw5ekyNqrlQwfbodIM8PwT2yzYlTtYwCGKCl1DIPZ1B1WHSxqcXCiiyd_pTwEEao-K9gDEOZWKVGt77p_tpb0kFtX8sdGxOlkSkZ-xDHO_ar0u2YBqj9-VHoI2XNAkyiRsbYHnysTkQHQYbounYQxfnAateQCOOn86DLwCCJYR1Ukp59-wudNw5oXZgYyc0wXZL2Ss_Fy7lxWSL4pGWBXRwIgfRED9mMAgT3W3TdqYLkOO6b1JJe8srIeR-w-DEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرخ تولید تایر به‌تندی می‌چرخد
🔹
تولید ۷۵ درصد نیاز تایر کشور در داخل کشور انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/466831" target="_blank">📅 15:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5951552a87.mp4?token=CjlbtERLsMdiaME2sxiRlQ0Hx6MRA_zSFzbABE9kmG-kK-n33cCxoSz9YovBRAbIlCcEfvBYwbeGvh8gsZtghyBA25oL_GTXsGbxbwcRo9OuAC9mgdVmKloMVzZK4a2nogmi40CsfkkX3hk2yL1D4ia4brrO_UHmGgEsSouIUn2tpwZiHnFXBF9hpvkn0VWnLrquaNE8Qf6cLpu_AGIgPWZsAH_XRfpeyWskmuBXkDr8ANEscPCmETIkqjkBOOe1o5khFvX8lHnKa4KHn3ZjJSRaNwD5vTdjJI-59Zyy7BT2gZg5OdjNE6vEtVNvOWcyz48adYEyUcI1IFCqLp1DXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5951552a87.mp4?token=CjlbtERLsMdiaME2sxiRlQ0Hx6MRA_zSFzbABE9kmG-kK-n33cCxoSz9YovBRAbIlCcEfvBYwbeGvh8gsZtghyBA25oL_GTXsGbxbwcRo9OuAC9mgdVmKloMVzZK4a2nogmi40CsfkkX3hk2yL1D4ia4brrO_UHmGgEsSouIUn2tpwZiHnFXBF9hpvkn0VWnLrquaNE8Qf6cLpu_AGIgPWZsAH_XRfpeyWskmuBXkDr8ANEscPCmETIkqjkBOOe1o5khFvX8lHnKa4KHn3ZjJSRaNwD5vTdjJI-59Zyy7BT2gZg5OdjNE6vEtVNvOWcyz48adYEyUcI1IFCqLp1DXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزینهٔ تجاوز آمریکا همچنان روی میز کشاورزان اروپایی نقد می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/466830" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70cb544ed1.mp4?token=RsdeeDXgIGB25Z9vr50Hqtg4n-SKx8G-O7y8c1bKAyKQi7CmtgjbaQQn8cg7Pf9nkLl9MJlb4EHxi72yFzgFVb73VJ5aTI5hgNRMJvtFb9Ao9HBO17DVPBQig4TgQ_QBxPymt5uK3oPMPQeS0-7cBs64rQwl5lecE-W3WHuzl2qsWzK2O1H87GLzKbnmYfQAwgyYDz-_O3IEr1UBbMVFZwdygqkj6c34O_mPM676B6uHc68OIxmnoHcNOsRNGxIO0dOUAsx1EMfLEWyxj8LAj-gcAW_6qIQYvn1G73cbUa975iiDT9ekG86rO77VX7jbM-qI5Kf0jQPnmmqBMB8cEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70cb544ed1.mp4?token=RsdeeDXgIGB25Z9vr50Hqtg4n-SKx8G-O7y8c1bKAyKQi7CmtgjbaQQn8cg7Pf9nkLl9MJlb4EHxi72yFzgFVb73VJ5aTI5hgNRMJvtFb9Ao9HBO17DVPBQig4TgQ_QBxPymt5uK3oPMPQeS0-7cBs64rQwl5lecE-W3WHuzl2qsWzK2O1H87GLzKbnmYfQAwgyYDz-_O3IEr1UBbMVFZwdygqkj6c34O_mPM676B6uHc68OIxmnoHcNOsRNGxIO0dOUAsx1EMfLEWyxj8LAj-gcAW_6qIQYvn1G73cbUa975iiDT9ekG86rO77VX7jbM-qI5Kf0jQPnmmqBMB8cEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزی که طوفان خشم فلسطینی‌ها به جان صهیونیست‌ها افتاد
🗓
امروز ۷ اکتبر، روز عملیات تاریخی طوفان‌الاقصی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/466829" target="_blank">📅 14:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee8e50e3d.mp4?token=g9gA9-Kgp5CViT5yWhygNcxnE5NgUjEptJVFsyw3g22e8aEZJowOWIjNV5S85LShFZsAvRU7EphK85MxmtYrXWn5YD0hhbHneb55RlGgyJPKouTLYJTQc4qtqEAkdPOBzvT0NFk4HUPoXaa-_UQNv35twZcdwDxWPXeOllyZeY2vU73Z5Om3IssaHjwuua-hwYMBOjXkg8bq0L0lbZpq0msnPn8YRwG9AyUOQRNvoRGB6kY7ICszzeoLcCXqoQLgV0UpBtBoRZ9p3sR_K3sPEM1DwLhVbWdL_EwlUr7ygAz5MUkhPHRGbgSCEGYuatexX0pXFUNuSeh2f3aozY2zng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee8e50e3d.mp4?token=g9gA9-Kgp5CViT5yWhygNcxnE5NgUjEptJVFsyw3g22e8aEZJowOWIjNV5S85LShFZsAvRU7EphK85MxmtYrXWn5YD0hhbHneb55RlGgyJPKouTLYJTQc4qtqEAkdPOBzvT0NFk4HUPoXaa-_UQNv35twZcdwDxWPXeOllyZeY2vU73Z5Om3IssaHjwuua-hwYMBOjXkg8bq0L0lbZpq0msnPn8YRwG9AyUOQRNvoRGB6kY7ICszzeoLcCXqoQLgV0UpBtBoRZ9p3sR_K3sPEM1DwLhVbWdL_EwlUr7ygAz5MUkhPHRGbgSCEGYuatexX0pXFUNuSeh2f3aozY2zng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصرف CNG افزایش یافت
🔹
مدیرعامل شرکت ملی پخش فرآورده‌ای نفتی: با اجرای نرخ سوم بنزین، مصرف سی‌ان‌جی ۱۲ درصد افزایش یافته و مصرف بنزین ۳ درصد کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466828" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a7905108.mp4?token=fKrTDzMV6Mz2Rxi4TljBgpzMYGaPp6bEDTU9m5gnn7VYa9VHnT7XNX2nJgaqx5cvbYhoaBgHeu9ku9bweROK1s2Viuz8Na8box__iemXbl2efk4oh6Gz7rI8-G5Qohr4vRjy-gdn2tQBY1ECWdgpU6ZfavKFsyM9KLH2ZX1rt684rBR53wGprojkdEWaEhEGtYeH1yAyMxMDrmOtWWhilTu2AMaWM5EBX-2lhNTiIeWaVZvtBfjZIoGpw6Tw-eiCScRWSmwXd5E9YEC3DVGtNO_EQBZZcs-XlcX9dtcGxJLZva39d2fk7Wx9xqVY_Nu_MAdyBQcqaMBCjMgFaB6buQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a7905108.mp4?token=fKrTDzMV6Mz2Rxi4TljBgpzMYGaPp6bEDTU9m5gnn7VYa9VHnT7XNX2nJgaqx5cvbYhoaBgHeu9ku9bweROK1s2Viuz8Na8box__iemXbl2efk4oh6Gz7rI8-G5Qohr4vRjy-gdn2tQBY1ECWdgpU6ZfavKFsyM9KLH2ZX1rt684rBR53wGprojkdEWaEhEGtYeH1yAyMxMDrmOtWWhilTu2AMaWM5EBX-2lhNTiIeWaVZvtBfjZIoGpw6Tw-eiCScRWSmwXd5E9YEC3DVGtNO_EQBZZcs-XlcX9dtcGxJLZva39d2fk7Wx9xqVY_Nu_MAdyBQcqaMBCjMgFaB6buQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقشهٔ فرانسه برای مداخله در ایران که نقش‌ بر آب شد
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/466827" target="_blank">📅 14:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37d1fb097.mp4?token=EMizuBdf9mwXeVjqNfLrQ1Ru0PvBVBLgO0gJYOBiDAcY02R6z3YTIXRd9Dq__6nfzWUblS-YS26qWhJfkKk-60ByrhvwdhVablcDO-oqED02eOoB7AqW3y4jT1yJZQkJfwuAJaQLFz-4HSuNMaSS2aoztQyiti_-tlcK2gAmQOhSjJyV7TmvmEp0j59sBwdKqKKjGJIkpeR9Z93AE0veAWwvqkjLPCi_5oYyGGxj6KAUZQGb0pDRPqQGeI9r5_37_axN6yLBbGnk8ETy1AtQFrq11OJDc3X2JsABnlohNwWpjFimIrqnJwn8d2-gi0Hh6Rl_Eh5FHaYmdVQ77gw-hjWtw_PQsKSUGk3RDH0ZGXpmKAt_CiK1kQe0a1Aijelz11ot2B5OfxNKw1VYmSyHFmJ_daGKpEol5LyG7llGZ6AlmKJWlQfFkDJwgM63awbkK_MAOKGR9I5rufcR1ySltz60liDMbGY7Q4TbdsGVObitD589i8Ju4wJd_G_0J1TJswvm4O4fybhKKQaV5eUrCDdtZs1Su4VZg9Kgp9-u2uJpr-Y7C-Dn8XfwpnU-Q7W1pKojD9Gk29NfIrUF5UKoi0StahgvD_hx6AmhmbinixfW6pdfeqUgbbLwPjXSxpAwxRieFKQrEFMhClXwR75ejsHEmQw8IjfRGGs7Ww-6lBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37d1fb097.mp4?token=EMizuBdf9mwXeVjqNfLrQ1Ru0PvBVBLgO0gJYOBiDAcY02R6z3YTIXRd9Dq__6nfzWUblS-YS26qWhJfkKk-60ByrhvwdhVablcDO-oqED02eOoB7AqW3y4jT1yJZQkJfwuAJaQLFz-4HSuNMaSS2aoztQyiti_-tlcK2gAmQOhSjJyV7TmvmEp0j59sBwdKqKKjGJIkpeR9Z93AE0veAWwvqkjLPCi_5oYyGGxj6KAUZQGb0pDRPqQGeI9r5_37_axN6yLBbGnk8ETy1AtQFrq11OJDc3X2JsABnlohNwWpjFimIrqnJwn8d2-gi0Hh6Rl_Eh5FHaYmdVQ77gw-hjWtw_PQsKSUGk3RDH0ZGXpmKAt_CiK1kQe0a1Aijelz11ot2B5OfxNKw1VYmSyHFmJ_daGKpEol5LyG7llGZ6AlmKJWlQfFkDJwgM63awbkK_MAOKGR9I5rufcR1ySltz60liDMbGY7Q4TbdsGVObitD589i8Ju4wJd_G_0J1TJswvm4O4fybhKKQaV5eUrCDdtZs1Su4VZg9Kgp9-u2uJpr-Y7C-Dn8XfwpnU-Q7W1pKojD9Gk29NfIrUF5UKoi0StahgvD_hx6AmhmbinixfW6pdfeqUgbbLwPjXSxpAwxRieFKQrEFMhClXwR75ejsHEmQw8IjfRGGs7Ww-6lBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۲۰ تجمعات شبانه حال‌وهوای متفاوتی داشت
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/466826" target="_blank">📅 14:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20587ffb2.mp4?token=HzUO32thaqIyDzKXFjDlSj7TYJzeYBx005aXgy6vjB04hv3ZWbOw1DYcrc3GuCbHRK2ljr0XxUEkWWuzLeXS-FDRApCGxXTXQsuHobovE91RFCnfVePx_wlxWW7-TRuIB_xXWjS-wK5B4ms_x3zBC626xNupkQ7xS6kPpXZQWTz7_YIcVi6di2tFxOqLZi9qseyntMqfIdb41xiHwjtvsuEH4NDRyNRj5qcQi8HwdfqXLEQ3i4eUcpTkIrfWMojhIw2vMc5B0Y9rlNhPq5uDMDUoTmoHQJYF8t5A0EZPXgspvw5HYrJd6NVqCOZjjFcMd5kRWY8l4uP228XAHoRX_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20587ffb2.mp4?token=HzUO32thaqIyDzKXFjDlSj7TYJzeYBx005aXgy6vjB04hv3ZWbOw1DYcrc3GuCbHRK2ljr0XxUEkWWuzLeXS-FDRApCGxXTXQsuHobovE91RFCnfVePx_wlxWW7-TRuIB_xXWjS-wK5B4ms_x3zBC626xNupkQ7xS6kPpXZQWTz7_YIcVi6di2tFxOqLZi9qseyntMqfIdb41xiHwjtvsuEH4NDRyNRj5qcQi8HwdfqXLEQ3i4eUcpTkIrfWMojhIw2vMc5B0Y9rlNhPq5uDMDUoTmoHQJYF8t5A0EZPXgspvw5HYrJd6NVqCOZjjFcMd5kRWY8l4uP228XAHoRX_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران سالانه میزبان یک میلیون و ۷۰۰ هزار گردشگر سلامت است
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/466825" target="_blank">📅 14:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMySwLh9UfGQD8nOZWfQQD2HLOGT_DZ_fwv4XNP4joi4lRwz8PZvR44EVuefASPIH4SwCU_ZakNtCfmrzYHKPzXtlp2asIDwhgK_LZ1ITyJwEaUA8MvrOcc-wveQVP858fYyXpwmmniPM5S2UCZXr61iBf43fiCwhVOmVe69dvwAOUFWpkkOGkvKbG5gf_C_IP4PkFzwbwwzwGt3sbyDBAN-XltOHuUK1RPQmBWTbEea1j9_7rxcwx-79ZITM1FviNjry2fW0PPQPTJdf8xRDD9x_bnpDiBNRtcrmOFFX59XwKG9pDhFuFR9ihQtW63hwNBDpqfc9eP3jN3vfG5pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: در یک جنگ تمام‌عیار قرار داریم
🔹
در شرایط جنگ تمام‌عیار، دولت ضمن ادامۀ گفت‌وگو برای احقاق حقوق ملت ایران، برنامۀ مقاومت را با قدرت دنبال می‌کند و نباید اجازه داد مشکلات موجود به معیشت مردم و چرخۀ تولید آسیب وارد کند.
🔹
قطعاً بدون شک مقاومت خواهیم…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/466824" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
سردار نقدی: هر زمان که رهبر انقلاب مجوز بدهند، برد سلاح‌های خود را متناسب با نیاز میدان نبرد افزایش خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466823" target="_blank">📅 14:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
سردار نقدی: برد محدود تسلیحات ما ناشی از دلایل فنی نیست، بلکه برخاسته از سیاست ماست
🔹
برد تسلیحاتی ایران با تصمیم مسئولان، رهبر انقلاب و متناسب با نیازهای ما تعیین می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/466822" target="_blank">📅 14:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🔹
مشاور فرمانده کل سپاه: تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
🔹
حجم نفت قاچاق‌شده بسیارناچیز است…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/466821" target="_blank">📅 14:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🔹
مشاور فرمانده کل سپاه: تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
🔹
حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
🔹
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/466820" target="_blank">📅 14:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سرلشکر عبداللهی: دفاع از جبهه مقاومت تا آزادی قدس ادامه خواهد داشت
🔹
رئیس ستادکل نیروهای مسلح: عملیات طوفان‌الاقصی فراتر از تصور رژیم صهیونیستی بود و محاسبات دشمنان جبهۀ مقاومت را به هم ریخت.
🔹
۷ اکتبر، راهبرد جبهه مقاومت را از دفاعی به تهاجمی برای دفاع از مردم و سرزمین فلسطین تبدیل کرد و به گفته وی، روند افول رژیم صهیونیستی را سرعت بخشید.
🔹
حماسه‌آفرینی‌های حاج قاسم سلیمانی، سید حسن نصرالله، اسماعیل هنیه و یحیی سنوار تداوم خواهد داشت و پایان رژیم اشغالگر قدس را رقم خواهد زد.
🔹
دفاع از آرمان فلسطین و جبهه مقاومت تا آزادی قدس شریف ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/466819" target="_blank">📅 13:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScMzOxpf5LCiyGWbiSqVcW2j6wc3YuEFPZl2gQ-1avrYldqmGUmWV9nSxQ08MTPY3A3Y98p2QOd1b00nCTvxBYPFunixk8SnzT2OiMxN-GjdzaVivrO3kVPXAEV_CBOTohwrdeDlnus4NptQSSajxMBr4aNAjXXb6qwQch71m4FHARLALpXGMof2zl9KLgwtKThaWxQJdSKvExXt3zmE-Z4JySoxkONWxAbFaMlb50EqxbBFq7jE7vn6hkw6Y2-8Pj8ye518FlngC5U1bgAQYnC8nuaiA4RXm3cL-XpbT1tqs3I9jIFER047O_WXb9lsZPsuntFm5FhXoh0IiOcJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
قالیباف: طراحی دشمن بر اقدامات خشونت‌آمیز در داخل کشور تمرکز دارد
🔹
این طراحی و نقشۀ دشمن نشان می‌دهد که که اولویت اصلی ما نیز باید تلاش برای ارتقای تاب‌آوری اقتصادی و تامین امنیت داخلی باشد. @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/466817" target="_blank">📅 13:55 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
