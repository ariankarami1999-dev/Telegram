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
<img src="https://cdn4.telesco.pe/file/t3h_Kn7O6Qa7Jln5sqyhhffqYivvTDahZdHkDtOvB0hxj8D0RuUaioMUsFV1Jte4tGDR1FJrQuok27wkFufUwIF0evFCRBnkbvneiiGsVKgOb2dcXJKFRzOsUhGxuMARgo0c0-jsbwCpXy8PXtkA4i7BG2qtIHnor58Gs5uhMC-nsoNCLgQwX9hbcJiN8EtAEf8Wf4VK_5sA81p0L39zR6AHP7C1aJAWEh3JTDXX-EtFP-P0ryyRwpvdtodT8GE47Hpi4MqdEARpPMkWLRklk7PuIL6jhaFi0so2cU__JoHKv-n9GuvPXdV630a3q0esDg0xJsac-JKm-OYBCcMMzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 119K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 14:46:36</div>
<hr>

<div class="tg-post" id="msg-70275">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=CIHdD6jjc2lBiJRZW-w-ZQarzWavP-jPgs_ShGt18HKTH0EfafubY8-b15J-svmE6hA_4ovhePC4cyfb8jkoWszhfcIlRsX3EBqdUKBEw6y9yh61U2y092c_wAUg7kamkl3m5kNPpCMtvILcNkDS1EyuPfshf3kppSajmE38liM_PlpSTHeMB2DRhSeh6X6gtDJnJlGUxFVoRHf9AyjBtXvH60Nbk46-fb_u1j-Gr24W9hQId-HRO2_e7ppGPJemfyrGWorRYLVcJPHRRWlmVq0LUkav7Xhd0z4DcooZg6p-mu6L81TMD_QCOmDSW1kikmSAtQhbmng4FbdUGkZelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=CIHdD6jjc2lBiJRZW-w-ZQarzWavP-jPgs_ShGt18HKTH0EfafubY8-b15J-svmE6hA_4ovhePC4cyfb8jkoWszhfcIlRsX3EBqdUKBEw6y9yh61U2y092c_wAUg7kamkl3m5kNPpCMtvILcNkDS1EyuPfshf3kppSajmE38liM_PlpSTHeMB2DRhSeh6X6gtDJnJlGUxFVoRHf9AyjBtXvH60Nbk46-fb_u1j-Gr24W9hQId-HRO2_e7ppGPJemfyrGWorRYLVcJPHRRWlmVq0LUkav7Xhd0z4DcooZg6p-mu6L81TMD_QCOmDSW1kikmSAtQhbmng4FbdUGkZelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش سرهنگ سعید راستی به ویدیویی که از او در اعتراضات دی‌ماه منتشر شد:
تو جمهوری اسلامی اگه دیدید دارن یکی رو می‌زنن و تخریبش می‌کنن، بدونید اون طرف کارشو درست انجام داده؛
تو 32 سال گذشته کار من فقط مبارزه با ارازل و اوباش بوده و غیر ازاین نبوده.
تو فضای مجازی اومدن با استفاده از هوش مصنوعی یه کلیپ از من ساختن که توش با مردم درگیر هستم؛ در حالی که اون کلیپ اصلاً مربوط به من نیست و سر من رو با سر یه شخص دیگه جابه‌جا کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/news_hut/70275" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uw_g8Ingc-2FJ7SBV4KAGyV_zJGhYlXezAXhPpSewWokMnCMtlylyi-SA083_NzLkWy1FSSSyzL5cMYSVZEB7Cqv51rhtU1CFpLxPTy8KPzjQtG2Aqtra39iKZUV4692z7_CCVXb0jvOeCI5eG0hRxwLy2qE3BVkPNylalZn87oHoTF8ZNh86R-sKih24ekQF_7-RlvVIlyjMBBVZ2yXos4g6biZTQno_Eo9yfJVc2BzD3Do8Lsmt36L1f9KQN06Gpkn9b0wuYncf7LQY9l4DHNZCYAtP2uKBbdkVVX_NxTl_5KIgo5IC06LLa6bAltTn7Kbgb9an7TUc4o1evjJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev7dsKLwKCcqv9wFxpbyP53g_y7A30mGsGlF85ZEqJQRqVoHkAQNCNwu-NbnM5XgMDw8aRGCESOPOdyCR5R6jUJWuAVaD1K1ZHYpJDiLGAfqyWUT4ps1OJGdFnkUpYwqXe_ryO-t42-Lqw-6FBffQYVjA0EA6gif81Wibuh6q6jOcZMnDQhuoCXYK7VH_ILRnd07pufK2rbrY_3D63OxTK_8oJ_eYkNZ667IW_RxX4brI3E75UcpCdrsh_KuZ2t_EwIyoXSRpWDT9OK_FbsW8Sq254aQtoG2Ggd1NFmcmz306EH24LcxYnTnBVAmtYhhW-v7mUXCnrsNuzjDYaVRfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=jpBxeH3PBOdRewc1HqF2YX-t73y42pf3aN_Y7pwAwuQjEqAPCUFL9cbkT8cfE_AFjoMeJmklh6Es1ShJ-nrYNiaurQP2MtHUB2dSrsatSlnnPHb5o0ktXAdrzz1JW8by-MYxYaPVVVVvT2ZukpQJX3ObMG_Xrtx225oW4jp8zUvzHHxaE7o5HkiLnO4QJjZMv6weEQ8lv8EOFLx2JtVf3uj03wgAQTAZUul4nTBd2LXtbYz-oZBjBGP2KboB-_OP9C0sS7v_4R2quu_k5uc-DCzkgFjHlxTecP1Bc3wl3ldYIgcsnjTfPJLE9PUJBzv1ylH44ysEMIpLlydOdsfskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=jpBxeH3PBOdRewc1HqF2YX-t73y42pf3aN_Y7pwAwuQjEqAPCUFL9cbkT8cfE_AFjoMeJmklh6Es1ShJ-nrYNiaurQP2MtHUB2dSrsatSlnnPHb5o0ktXAdrzz1JW8by-MYxYaPVVVVvT2ZukpQJX3ObMG_Xrtx225oW4jp8zUvzHHxaE7o5HkiLnO4QJjZMv6weEQ8lv8EOFLx2JtVf3uj03wgAQTAZUul4nTBd2LXtbYz-oZBjBGP2KboB-_OP9C0sS7v_4R2quu_k5uc-DCzkgFjHlxTecP1Bc3wl3ldYIgcsnjTfPJLE9PUJBzv1ylH44ysEMIpLlydOdsfskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
امروز تولد جاویدنام مهرداد مشتاقی 27ساله‌ از اراک دانشجوی رشته معماری بود.
رتبه 200 کنکور سراسری
مهرداد 19دی تو اعتراضات اراک با گلوله جنگی از ناحیه سر مجروح و به بیمارستان منتقل میشه تو بیمارستان عمل میشه ولی به‌ دلیل مرگ مغزی جونشو از دست میده.
روحش شاد و یادش گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/news_hut/70271" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO6z-07wCTeb0CAXqySzTocLU3uzrpTE0BH7yEUcZs3DzGh_-CnKtYU6arhjrVkyXLaELof5FwgEdCAijO4eY0gkgJGdIsVC6ymneyB-Zl-UNdAWJKWDDQ_YaPK9BQqJjZ1H8zXWBr-EemH5p72WVwvuDsYxWLWkPLORxc3B95WUnYWY0OA4Ei6SYGoxTyM-Gbkeae-9UyJ3wDM0n4VGCxUPvQNrBgWf6l2W8oNjcLIKg7KVwHirR1xbHJYvcwoKdtHPQVXJ6jr3HAiZ52lrk7U3bshx0gc1229N95zNasX7OacCmwSuqOxjOI-_Oo1vuc_x9JNf4g33fPdAWI6dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/news_hut/70270" target="_blank">📅 13:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCoX1FeFwLB1bCX1mlS1OONkUagRgaWc7znB03h8UVukZfCyV2NT-YwhCgCzMSDTQ9BiuxUvgi-yglDmCskbJThKhnA9_F5dicwXvHzwjfU3pVK47UzMM7fY322ntZqYVwznxe77S9UwchuOQloUMgTzK3FXgm5dIzVcrxR6PYRqj_E08Xb2VNkry9iVSJlz7SdEh2T4fhL_uaEHWx6SbCp5POM7sZ5UC1y6FeyuT6Nyr1vU6Ze3Zm0YRSjZv0tbrR_Q6mTSEevaHDT8y1QIz4UnS6z9tOdx8yyngLl2JaDLJK1_Ov-WrITU96ALdKzbF4YPrQLCnZZRMX44oKCzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فایشنال تایمز:
ایران در صورت تشدید جنگ از سوی واشنگتن، حمله به تأسیسات نظامی آمریکا در اروپا را مد نظر دارد.
اهداف احتمالی شامل پایگاه‌هایی در بلغارستان و قبرس و همچنین کابل‌های زیردریایی در تنگه هرمز است.
مقامات ایرانی به‌طور فزاینده‌ای وقوع درگیری مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حمله به زیرساخت‌های حیاتی ایران می‌تواند دامنه جنگ را به فراتر از خاورمیانه بکشاند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/70269" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=bOWNAnIPvnQjMxaUZZGJTOCdLJx_kf5BOHHJDreiTjuedUb7cPrcOJykPs7R2n1bENW5LfoJSC6VRz--RKKwRZIDjokpQS2DwGgQ-Lfa7-2XvCcUrnRNPRcrdaotAWSpzBKsgpOvtE2XAepPRu2oxWng9wxD_UwDeFnGxhEBD0xC7bJ3mYXq9mEHHodahWhtggQGgul6rkD4i6_tUYzeoceJi5GGART03JYyl39uCuCo3r8wV4in2a_olpfmVqxPxFyNoRMktVM2ovMj_uxRoTJjdN3U6BcayVsbEj6tZZ_tE_BRo_LOMJkeo8zqFkDpeJASMknTAFx4f5bUub-_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=bOWNAnIPvnQjMxaUZZGJTOCdLJx_kf5BOHHJDreiTjuedUb7cPrcOJykPs7R2n1bENW5LfoJSC6VRz--RKKwRZIDjokpQS2DwGgQ-Lfa7-2XvCcUrnRNPRcrdaotAWSpzBKsgpOvtE2XAepPRu2oxWng9wxD_UwDeFnGxhEBD0xC7bJ3mYXq9mEHHodahWhtggQGgul6rkD4i6_tUYzeoceJi5GGART03JYyl39uCuCo3r8wV4in2a_olpfmVqxPxFyNoRMktVM2ovMj_uxRoTJjdN3U6BcayVsbEj6tZZ_tE_BRo_LOMJkeo8zqFkDpeJASMknTAFx4f5bUub-_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنسیس مدل 2013 در امارات: ۵۰۰ میلیون تومن
ارزان‌تر از پراید در ایران...
@News_Hut</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/news_hut/70268" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/news_hut/70267" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcaGJqR_Cw29mcEIkD0aSDDotcSYqeM0vrPvC8PQax-Lx08ZvOrljJNJIDbTFVCM1OAyhtYrXn0Il-2lsfWVdEMfOFp4rNy8PlVXPa-Tw-j0sE05wxuIA-UHmwWKsDGMjwFRw1QA6RN7URVnp96BazIkWgv7VoA7LbLRS6H6aBqoenjAluRNktJR4fgHZignfkfjGVPhA9XnyRONU9LPO9cCPuuehIa1387ReO4xfu95s4swtjhXzs0QvITky03h8hLG69YEbdd2NMd_3WzXYkQczuqByKrRgLDCcgH-xCRPtj_a7BcrOrv5kv6aUpGM1clcBXBIgy73YAkoGiduYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r28
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/news_hut/70266" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=pmHAINNGB5QVw_i2LoDNGzkXjH7M_zIa0I6FfhXoZHgZky0cNEDFqMV5fcul0dDawf0shfGKbh-ODlzAnNc8LZUZHW62cqsiPa2ZDUusz1Y1C2nFzP-nfmW2sd-iWPpr7y7Jd-bES9RwtI8ObKahI76mtFNutE4iUnTroYTsRkyHHDQVEMBAvzKu5VmoVBAuy7bRMkXXrP2nOcXhZBwe_2VrENSxVpmExrZiFMQIOpVv-mOUHItLtmpXkJILH_KoCKDktLUhxMtNFb4xyXTavr2ZJ1yyswvMaJZ2uXapj0V_M7r1uXW276HWpfANGAsAI6FsfYN-xEzRNxUBYpCWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=pmHAINNGB5QVw_i2LoDNGzkXjH7M_zIa0I6FfhXoZHgZky0cNEDFqMV5fcul0dDawf0shfGKbh-ODlzAnNc8LZUZHW62cqsiPa2ZDUusz1Y1C2nFzP-nfmW2sd-iWPpr7y7Jd-bES9RwtI8ObKahI76mtFNutE4iUnTroYTsRkyHHDQVEMBAvzKu5VmoVBAuy7bRMkXXrP2nOcXhZBwe_2VrENSxVpmExrZiFMQIOpVv-mOUHItLtmpXkJILH_KoCKDktLUhxMtNFb4xyXTavr2ZJ1yyswvMaJZ2uXapj0V_M7r1uXW276HWpfANGAsAI6FsfYN-xEzRNxUBYpCWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی وایرال شده از بازار پروانه تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/70264" target="_blank">📅 12:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=Ddz1RCXbJVI-19JqKqtJDFlIDurID940_-hc78ENIHg38d4c7Zj0A1_TO4UzGTR0uC1xtmolpSbmyj4VE8Lc1cWi_UQghFhv42MX6jWBhQBK7nSkJ4iXJCFKZ5lUqV4Bo4G-4nkvhmYshbjp6Esw-YYheoXOTj6VgKtjjfG0XhDCTb1o0Dax1YiqRlwrIQFVOHfxjbXB7pt40dTslR7tpbgoYxtqdVWG3_LUW0Wn0HOE4w2CT_6go85ctSUEAhIyM4dk2RHJIcEopAZMrSA5grwrfoZW37k7ByDO0Sil2eHCLeOzEp05FHgEJgehe5dwgwO-XaXZTK1tguIKaEVNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=Ddz1RCXbJVI-19JqKqtJDFlIDurID940_-hc78ENIHg38d4c7Zj0A1_TO4UzGTR0uC1xtmolpSbmyj4VE8Lc1cWi_UQghFhv42MX6jWBhQBK7nSkJ4iXJCFKZ5lUqV4Bo4G-4nkvhmYshbjp6Esw-YYheoXOTj6VgKtjjfG0XhDCTb1o0Dax1YiqRlwrIQFVOHfxjbXB7pt40dTslR7tpbgoYxtqdVWG3_LUW0Wn0HOE4w2CT_6go85ctSUEAhIyM4dk2RHJIcEopAZMrSA5grwrfoZW37k7ByDO0Sil2eHCLeOzEp05FHgEJgehe5dwgwO-XaXZTK1tguIKaEVNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن‌ رضایی:
محاصره دریایی ادامه پیدا کند از NPT خارج می‌شویم.
خودتان میدانید این یعنی چه!
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/70263" target="_blank">📅 11:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=jtHBX1A3kizpl6vsO8QAPKSzxAoK7RudrBj2AWMrjPp0Vwqtmr2urYrGkHjAj-nwOSQW98EbWiMp-4mlg25ZqKbDvhqZ33E5lapadw7PZrUqfQM_f7vwSw_vxEZbe94fuQumAAm6x-lD4p22G_RdSDcXbFn2IJMJhbuL9-CKlKCgvc003_CM59gv6N695lQ9x-zECdaHORz8jhQaI4UiEDb7TBoDLrmwn-tPRqMVOaBALnmkAeO8dAw8tImrN9J5T2AkCeFDjHbcIO_7bUOn_p-C08Gi-ZX4DNNqvlzF94O2MngKSwxIIUc0oTTixPCmg7qB6SbLEQfDorDUOhQ7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=jtHBX1A3kizpl6vsO8QAPKSzxAoK7RudrBj2AWMrjPp0Vwqtmr2urYrGkHjAj-nwOSQW98EbWiMp-4mlg25ZqKbDvhqZ33E5lapadw7PZrUqfQM_f7vwSw_vxEZbe94fuQumAAm6x-lD4p22G_RdSDcXbFn2IJMJhbuL9-CKlKCgvc003_CM59gv6N695lQ9x-zECdaHORz8jhQaI4UiEDb7TBoDLrmwn-tPRqMVOaBALnmkAeO8dAw8tImrN9J5T2AkCeFDjHbcIO_7bUOn_p-C08Gi-ZX4DNNqvlzF94O2MngKSwxIIUc0oTTixPCmg7qB6SbLEQfDorDUOhQ7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
جدیداً تو روسیه گزارش‌هایی منتشر شده که بعضی از دخترها به‌صورت گروهی دنبال پسرها می‌افتن تا حتی برای یک شب هم که شده باهاشون وارد رابطه بشن!
گفته میشه؛ بیشتر این دخترها از قشر مرفه جامعه‌ان و اگه از پسری خوششون بیاد، حتی ممکنه چندنفری با یک پسر وارد رابطه بشن!
تا الان چند مورد آزار و سوءاستفاده جنسی از مردان توسط زنان هم به پلیس روسیه گزارش شده.
ظاهراً پسرهای بااصالت روس و همین‌طور خارجی‌ها، مخصوصاً آسیایی‌ها، بین بعضی از زنان ثروتمند روس طرفدار زیادی دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/70260" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c416662f.mp4?token=nhHJjl4TmfwucAAO-kBIbWmax75M-GgoE2xlEGeWIA_tGpa-XdAEk7CSVQMFGq4psa1gxEawIHJLeOvE1aE20H6Wy9vgCB0AP5WAwX8bsjqrOBB46u0lGRm3EowLR8o4U2Yun8oU1xHTy95P7lxRkNil3XMsg82lR725IDzA-Q1pisVMZkX_jgoMQx4GuN7ekkhC9e8dxERHgzRZ52QYmIeYzIHbQUxJZnP1BPXnqzvFhikQ4lZPMNZnipYG4uUilQwNzYuBRMbXLlsuL4bdyATC3ElzIDVMYWqseY6vnBMQ_xfywVra4qfX78WS557BZz2RlYjvmO8tSMZFVXyv3gBxySIl97Krc9pNaWCwrc3cwsO8s3apMXx_cCokPDYw7psIXDWezThTBicXnljxEQFU8LYmoqL08e0_5j1M8_dNgl8r_dU34cZ9l9INddUbMRbGoJBI_GCVXw1e26HNxKwZwPMr3np04UhLTjyGik3oZkhE-IsQHevgyF54-6Jr5OSbplUMr7uMxV3WcOrvyiSiOoKn7ju-1quElAL2mvNtyZa_5AoV-cez0ss0XE23WrDlk6mBq9QLh2xBN0K44rxQpjsG5rQHCK4MPjlIEaMJPAj6vnLbudLfJn58iESXSFkfynJ2uQiLaEjag8lGAqapFvC8Tjq9IlyXc-70cR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c416662f.mp4?token=nhHJjl4TmfwucAAO-kBIbWmax75M-GgoE2xlEGeWIA_tGpa-XdAEk7CSVQMFGq4psa1gxEawIHJLeOvE1aE20H6Wy9vgCB0AP5WAwX8bsjqrOBB46u0lGRm3EowLR8o4U2Yun8oU1xHTy95P7lxRkNil3XMsg82lR725IDzA-Q1pisVMZkX_jgoMQx4GuN7ekkhC9e8dxERHgzRZ52QYmIeYzIHbQUxJZnP1BPXnqzvFhikQ4lZPMNZnipYG4uUilQwNzYuBRMbXLlsuL4bdyATC3ElzIDVMYWqseY6vnBMQ_xfywVra4qfX78WS557BZz2RlYjvmO8tSMZFVXyv3gBxySIl97Krc9pNaWCwrc3cwsO8s3apMXx_cCokPDYw7psIXDWezThTBicXnljxEQFU8LYmoqL08e0_5j1M8_dNgl8r_dU34cZ9l9INddUbMRbGoJBI_GCVXw1e26HNxKwZwPMr3np04UhLTjyGik3oZkhE-IsQHevgyF54-6Jr5OSbplUMr7uMxV3WcOrvyiSiOoKn7ju-1quElAL2mvNtyZa_5AoV-cez0ss0XE23WrDlk6mBq9QLh2xBN0K44rxQpjsG5rQHCK4MPjlIEaMJPAj6vnLbudLfJn58iESXSFkfynJ2uQiLaEjag8lGAqapFvC8Tjq9IlyXc-70cR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو وایرال شده از کسی که کره‌خر خونگی داره!
به گفته صاحابش این خر گرون ترین پنیر رو میخوره که کیلویی 100 میلیون تومنه!
حتی برای خرش موزیک میزاره
خرش رو هم مث بچه ها پوشک میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70259" target="_blank">📅 10:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚠️
امام جمعه حاجی آباد بندرعباس به خاطر افشاگری علیه مسئولین شهر به دادگاه کشیده شده و اون رو مجبور به عذرخواهی کردن
حالا اومده عذرخواهی کرده
این نوع عذرخواهی جالبه:
من از بانک های رباخوار و از قاضی ظالم  مسولین بی کفایت عذرخواهی می کنم
من از روحانیون ساکت که منفعت خود را مصلحت اسلام می دانند عذر می خواهم
ما گوسفندان از گرگ های درنده عذر می خواهیم اگر گوشتی به تن نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70258" target="_blank">📅 09:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=n3pKOa8nzxn1OwMWTrplCBbVSnkxmMRmPZe8qtNFW7G8ihFq9ZALD9Jr7ZlRu_sfBnXTlroA8JgfS7vXNbQTCaIkvqzk37PH_nT9AzQJtMD0xYTFksn_gkyNbyors5tRYf76D5JuVHYN_8XVkcDYxveM22r0Fuf9eYkrPngjjyQkpBUloLkkpcpgCZe481T491eTwCulovw-fmzEUuwDfPe-4OBsHgEYZHKH6ppR68Z_kQGb9Rwb0f4t8Pevua5QpxY2q4JRXtYVL4e73tno-2l6Fo5-I8iGC0uRta1U0MAY65pmhls3rKwrV5ESdBogsSOrYwFbjdjmd8FL37TQlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=n3pKOa8nzxn1OwMWTrplCBbVSnkxmMRmPZe8qtNFW7G8ihFq9ZALD9Jr7ZlRu_sfBnXTlroA8JgfS7vXNbQTCaIkvqzk37PH_nT9AzQJtMD0xYTFksn_gkyNbyors5tRYf76D5JuVHYN_8XVkcDYxveM22r0Fuf9eYkrPngjjyQkpBUloLkkpcpgCZe481T491eTwCulovw-fmzEUuwDfPe-4OBsHgEYZHKH6ppR68Z_kQGb9Rwb0f4t8Pevua5QpxY2q4JRXtYVL4e73tno-2l6Fo5-I8iGC0uRta1U0MAY65pmhls3rKwrV5ESdBogsSOrYwFbjdjmd8FL37TQlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی :
رابطه ما تو این دوره با کردستان عراق و جمهوری آذربایجان خیلی خوب شده؛
می‌دونید چرا؟ چون پزشکیان هم ترکی بلده هم کردی، زنگ میزنه با زبون خودشون باهاشون چاق سلامتی میکنه، اونا هم خیلی خوششون میاد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70257" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=Ck79SeeRn5keMiTmzRu6IYvcYupOTZMi-LU0znuEhmxPQWS7VCa2EreJ3b97rw3lLIzSq9-W1d0S_rLTKZlvpbFjiTblSiAK9xa2Cch-7FY8IDSBzyHUsbqpASsL9CCoRIKgBrg3ikxvmZgWokzDcwFHnzI1BGeVOAdbXZsJef0ydtGOb-ITgwya3LFQBb1eOkqlAnXY5rufdm36YvXNlv19Vle5f482jrXEcbSqaXIKsJA-JShnEYEpYoQbOcdreH-oJ1cb19DknQZgUT0sOVeDIn7FjEfsITpw6nd6rwFKB0jWI9CockbKbn11b1U_dQRYUyxTMVXskB6LmH0WnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=Ck79SeeRn5keMiTmzRu6IYvcYupOTZMi-LU0znuEhmxPQWS7VCa2EreJ3b97rw3lLIzSq9-W1d0S_rLTKZlvpbFjiTblSiAK9xa2Cch-7FY8IDSBzyHUsbqpASsL9CCoRIKgBrg3ikxvmZgWokzDcwFHnzI1BGeVOAdbXZsJef0ydtGOb-ITgwya3LFQBb1eOkqlAnXY5rufdm36YvXNlv19Vle5f482jrXEcbSqaXIKsJA-JShnEYEpYoQbOcdreH-oJ1cb19DknQZgUT0sOVeDIn7FjEfsITpw6nd6rwFKB0jWI9CockbKbn11b1U_dQRYUyxTMVXskB6LmH0WnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیشب میدان شهرداری گرگان در آتش سوخت و صدها نفر کسب و کارشون آتیش گرفت و نابود شد!
حالا دلیل اینکه آتش نشانی دیر رسید به محل چی بود؟ بخاطر موکب‌ها و تجمعات شبانه تو ترافیک گیر کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70256" target="_blank">📅 09:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!  پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!  اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70255" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70254">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=UCrZa5qY5HlQct1SYVsmJPMhhVos0tKWWzu0-_8JP18zXhyjID801ko_-YnLPYjRaVEwEcN1xVABQeSldRYczS5gFiazM4E3fzfgL1zrGF1eK0p4SAfMijz_cFCIW0TqtDU7u_X9P_5IgSkEN7Ilp6PqUMRzaRuBvbaie5qaCFw6tFUk7GMlEZOyP9xhnjwSuS7skknxvGsNuGwAirzp_VX_TvF2FsnZuD7In7a3mRwV0lln4-UXFlGWzD2r9lPPN-AtHDcf_YAR3UKhuZmC8bxmv3C2WlzI4oXHWAQJpttesjBaaNdOK9uzjVMX4fuVFCxVDdBdaUoJr77rgEAi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=UCrZa5qY5HlQct1SYVsmJPMhhVos0tKWWzu0-_8JP18zXhyjID801ko_-YnLPYjRaVEwEcN1xVABQeSldRYczS5gFiazM4E3fzfgL1zrGF1eK0p4SAfMijz_cFCIW0TqtDU7u_X9P_5IgSkEN7Ilp6PqUMRzaRuBvbaie5qaCFw6tFUk7GMlEZOyP9xhnjwSuS7skknxvGsNuGwAirzp_VX_TvF2FsnZuD7In7a3mRwV0lln4-UXFlGWzD2r9lPPN-AtHDcf_YAR3UKhuZmC8bxmv3C2WlzI4oXHWAQJpttesjBaaNdOK9uzjVMX4fuVFCxVDdBdaUoJr77rgEAi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!
پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!
اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی بازی‌های مهم ایران و اروپا
✅
بررسی ترکیب تیم‌ها قبل از شروع مسابقه
✅
پوشش حواشی داغ و اخبار نقل و انتقالات
✅
پیش‌بینی‌ها و فکت‌های جذاب فوتبالی که هیچ‌جا نخوندی!
دیگه فقط بیننده نباش، فوتبال رو عمیق‌تر بفهم!
👁‍🗨
👇
عضویت در کانال:
https://t.me/+nbm7Tb2pz8VjMDlk
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70254" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMdSOjA6AEXQgo05M9YzCy6FvX8XoWI_0cOOp2Ish5RClDztdHT8tXS8h5o1wbwGhlcGBxa0FFx9hrQTDIoOYTlj6tW-0EKrrDyIwrFnurfYij5xYq3pVb3n-Ms02jFRfu_NsruMVe-RWLNimWVtWo_SUaLo21IsI_4AV2uHBG9eU0xkJz6LS_SDhzbaQLMyz1CwdYmUFBA0MN6PNurpqkNsv0jdzJGLtQCcrJu9YdURgL6pJ5mCljJngNNibEgLC-NMLAlc_21ERAk9UGBnKrSCLuA7jU5NT-9DdC0Yr9e3NrFptcqqn82YYnEmungPK3m_2UCLvAl2HTVjQzWtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه خواهر جاوید نام امیرکیادربندسری به خاطر سوگ از دست دادن برادرش نتونست دووم بیاره و دیشب سکته کرد.
روحشان شاد و یادشان گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70253" target="_blank">📅 01:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70252">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQrlXjMjwjTs-yCbHfIl_ebLQGPC_ccLL26KQIwMinyhX-mLCacg80U0q6S_QnTmMgguuQLe-nYEhgvp8fj3ShPkUfyArvVsfIkB4poQEKpk9v9F9dpidiMQk3pf_6ZAZ-F7UPUv-CnAluoHuaivQau8mYtQkJK1MYCgrZRB77de2Kt0zxjGP0XGBJUklLb3IEalJHkY7xbfbTLIsfmoDrb8KMUQr2ZEBJZoEO5KFW3-FTaNLfRLces85Dx9fV64OaCxeWUWnRNUfWa1LflbVKq4s8lkfX68s7LTrrdkqpfvVtRfWFYDm3LzA72ppEDiJBSNvH_RGlLsO5gtPz4E6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
سی‌ان‌ان:
دونالد ترامپ به فرستادگان ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند؛ اقدامی که نشان‌دهنده تغییری عمده در راهبرد دولت او در قبال تهران است.
بر این اساس، کاخ سفید دیگر به دنبال «ضربه زدن فوری و شدید به ایران» نیست، بلکه قصد دارد با اعمال فشار مداوم اقتصادی و نظامی، رویکردی بلندمدت را برای «خفه کردن» این کشور در پیش گیرد تا زمانی که ایران شرایط ترامپ را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70252" target="_blank">📅 00:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=dfHmN6Ssgvoda5bYX3-GdPNQdLAWEPRU6qhs0co6Iu0x97iAGr6vJhkHKkldJe_rcxmqBLIAnymrf2kPhYpkOiAbEkmSaIrpyIZZe2KtB6JRGJNc34xwFcjJbWPjOoU7RdrPbH59Kuotd6dWPEUL9tP8FsVPYNxWZb8JsIzLvEqwyyQOgayWA5kYLKqycMbPOAiFU1ecWm5A09ItJrncYjSuHVvj3RQzI0cfBqxjlYKgenVdCYG0u4YFxIDi3EvhvIveVvsdWxvrbdLhSoJu7kwiR-3FvpyEXYVtrF3KTg6IQcL0qAVx2xQhRFsS6iL12DfwBKPYgpYHdkBXJvsuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=dfHmN6Ssgvoda5bYX3-GdPNQdLAWEPRU6qhs0co6Iu0x97iAGr6vJhkHKkldJe_rcxmqBLIAnymrf2kPhYpkOiAbEkmSaIrpyIZZe2KtB6JRGJNc34xwFcjJbWPjOoU7RdrPbH59Kuotd6dWPEUL9tP8FsVPYNxWZb8JsIzLvEqwyyQOgayWA5kYLKqycMbPOAiFU1ecWm5A09ItJrncYjSuHVvj3RQzI0cfBqxjlYKgenVdCYG0u4YFxIDi3EvhvIveVvsdWxvrbdLhSoJu7kwiR-3FvpyEXYVtrF3KTg6IQcL0qAVx2xQhRFsS6iL12DfwBKPYgpYHdkBXJvsuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل اسکادران ۱۹۰ بالگردهای آپاچی خود را به‌طور دائم از پایگاه هوایی «رامون» در صحرای نگو به پایگاه «رمات دیوید» در نزدیکی حیفا منتقل کرد و بدین ترتیب حدود ۱۵ فروند بالگرد AH-64A را به شمال انتقال داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70250" target="_blank">📅 23:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=G8HhUzMR9eqjOBp-Xy3EyD8j4msVINd3h-0D_qKwZ3S3WCxbrhcguCzpraV35gVjo2vPyjd0KNl7d1AGFFdBHQu_1Akzg2sIkvORXah8aA0Jrv6DB54e8DSMd4qO4xCbPnE8cw4GMrctb1CMZVwKViscARw6aNdnr_EYqrTQVR2U3uftJEHnwWFUFlhX68MZ-_dnAOM2ANSv2qQB4TKxjieBQTje1Dg0Fwd9bDGmVdLTN-6Q5R3dBDqQrB1-AqCKG_Cq9OoaDkGy6rl-MvwZyX6zY3FL0BjflZVhJWxUH6EN5ShkR0wde7nlScTwVn7YMCsxVnXUTBnMA0oiI_5Wyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=G8HhUzMR9eqjOBp-Xy3EyD8j4msVINd3h-0D_qKwZ3S3WCxbrhcguCzpraV35gVjo2vPyjd0KNl7d1AGFFdBHQu_1Akzg2sIkvORXah8aA0Jrv6DB54e8DSMd4qO4xCbPnE8cw4GMrctb1CMZVwKViscARw6aNdnr_EYqrTQVR2U3uftJEHnwWFUFlhX68MZ-_dnAOM2ANSv2qQB4TKxjieBQTje1Dg0Fwd9bDGmVdLTN-6Q5R3dBDqQrB1-AqCKG_Cq9OoaDkGy6rl-MvwZyX6zY3FL0BjflZVhJWxUH6EN5ShkR0wde7nlScTwVn7YMCsxVnXUTBnMA0oiI_5Wyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف با قلیون رفته وسط دریا با یه دست داره شنا میکنه و قلیون میکشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70249" target="_blank">📅 23:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM597xXSoC5xJhGagvcyUQc5DrbZew_NWTMp3QUVoKp4O42eAxzlH-RhOATSR_gZqPDLv4wBImgn1xMmsss_-DMTc7BL8k7cW7PuGCIaylJeq1BsoDt7vBbfAtnJU3_HqWupC0OnqTSRVD1M7YrZY1B0dj7R58WT7GN3aHI1FxbGtILg70ZS6Bn3QP_5gagX_060Cxv6SCTEf6oYBgeIhSnQEI3FhrdpoyefHXqA35tmd30HOk9oHFIIdq_3zmW3CU4tNqHiiRFq6e_nFL8lV1BywP2lj64KXP8k_IhAdYwBeSt7FigB8LZB85HjiKU1M4RJbCOc74Wwexj8O2A91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
شکاف میان ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن بر این تنگه، از فاصله ۷ هزار مایلی میان واشنگتن و خودِ تنگه نیز بیشتر است.
به نظمِ پساآمریکایی در خلیج فارس خوش‌آمدید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70248" target="_blank">📅 22:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9JiWqgDngensBIIJH8SeT-sabn6TVfdNfHF8RIQP153-WPedz10tduomFY_kiufdPZMzFFc_YTLnWb5bWag0bUoywlUZo2YcRQVTXdYGOBEinYIge15AgLUer2cTwb1fq0BaMNxBJfzJuAHeWX0AUHpArF5EEVm1DZlGE1hSaEgEKa1y6VK8dQvW4RpYY_ayuA03lMh7OE_d4vY9fk6BBZBYVcCyMgq97u1RYVuv-m5iGd_IFg9MxYIGeuz1Zb3wXZT76ocp3z_RR8noV33cFVG4S5RQcepehSRp76lRzH-ODguD7olnDhB8aZ70MMVYAYcsiX2RshyklPscK9YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ های جدید کارمزد خدمات بانکی در سال ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70247" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6qV8U43dbGGeaP-l0eUUDwFNKmqYVJNp3KMd_uQeovHzHRE1doClV5U53axHzGHaAq4XgRkFzPbged2rPMBYseXblrWGZOZmJ3xmhwi2D48lwRsnJ7jtwe88141hIb_bUBzZ9c9sIOpauFyEKfGmZaCHnxtwAPoFH-bmKB8wyZzNG6_lNwCcSrg_TUrf-6OId4SeJy9TYa-vqZVp24ngCeLmBSeZU79c_1JGKjVWJos6iA9EqnhxUgJtXz77ehWZWQqh-PZol90-4InHMjgcgYyeJVOSTk3VXSXKJRA-8YDAVHmWKmGXRAQJMX0BZVNih84AtadCVDjSpl6uhMKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکایی‌ها تصور می‌کنند که با اعمال فشار شدیدتر بر ایران، می‌توانند امتیازاتی به دست آورند که هرگز بخشی از توافق نبوده‌اند.
بِسِنت و هگسِت اصلاً در حد و اندازه‌ی این کار نیستند.
دیگر منتظر نباشید که این گروهِ دلقک‌مآب خرگوشی از کلاهشان بیرون بیاورند و گندی را که خودتان زده‌اید، جمع‌وجور کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70246" target="_blank">📅 21:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70245">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=BtR8ERF8UZtxcQOoACOYkEtotDdYTn5WZrKpjSO5NK3Y9ioB0UvTZvai-y9WuMLfuwGs4WLNY_lzlp_VtQT3iFC6DmQxYpNiJb-L9avQLTON-O1CJsBuG616jTmiBituQ7BLOfCZFOn5BRn2bv_BIHxdsU1EVGjKm14NwsaBu6J7Lxsr985rGC3tePQYIPoXu0wiUxiffDeR0wfjyUVHsdusxwUIICshpJcNJrkuiU6Z5gnTxcFyxOJhw1shDMrxgGsX2GTsNz79Uxo1Ewd2NxfDmjQkcdt5LF1zM1QdJNSuLYnpKexARrVtNRDFLaY1bN4hAhtFYTxNBtGSbgBwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=BtR8ERF8UZtxcQOoACOYkEtotDdYTn5WZrKpjSO5NK3Y9ioB0UvTZvai-y9WuMLfuwGs4WLNY_lzlp_VtQT3iFC6DmQxYpNiJb-L9avQLTON-O1CJsBuG616jTmiBituQ7BLOfCZFOn5BRn2bv_BIHxdsU1EVGjKm14NwsaBu6J7Lxsr985rGC3tePQYIPoXu0wiUxiffDeR0wfjyUVHsdusxwUIICshpJcNJrkuiU6Z5gnTxcFyxOJhw1shDMrxgGsX2GTsNz79Uxo1Ewd2NxfDmjQkcdt5LF1zM1QdJNSuLYnpKexARrVtNRDFLaY1bN4hAhtFYTxNBtGSbgBwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از مصاحبه اختصاصی دیوید فراست، با محمدرضا شاه پهلوی در سال1978
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70245" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70244">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQNX5I19dGs9Tgj1YRoh-r8sEQIC_i0QpJwH0kfoKx0opzbM00wXxBTKvacHRmIBpidwSD2oI8Rk9kdfER3sFkdUZixexb3imLtcj4WLu-E1T7rV8Bq2X_RqbvAHC78NASgqAZuX16_hjBeBGfmPmxDAchJSDHy_OA8bS5sfZQAZAWTb7a4KnHVD54QYa9-LuYWMda4IsleA-ErV_aY956n3mmsIybIJWC01dXcR20oMHe9CRQUflP546xOXW1n8tjgrKLa1yDnnengwIq1U49KEPE3CgMOSe8UIgUi6p8OwIMKtGoGU8FMx5XCBPE-fipZloQ06BVBlQpKRhtpdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70244" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70243">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwuAAJL4kCeB_I-k_sJrbd_aV9iAXhf_ZLDI4NTHRQSvefDDLDqp6rWR3dhmVFZNNwFEpgwxizHcsJBG-9UyA4R_oOYphKqLkfSSoxBU1Yhpo82kUB3tBwopI1y0D8L2Rbu5pPxo-x4GWUTEJioPvbM0eu37WWZFbLJ8oGSTtN2OU-pWPaBYTdbOx_-C_vgs3VkatTS8UxOuHQuyhwRZVDbM-qlgSjpLfYpNRq-sZm2Q17BiwzkCOZY-K8oCNQJaLp3u3CxSKW1RJ37L1YrStCHoNX_h83EnaSrnt85xrdYySAQj9jYC-DnUP5lQZjCSVSAGI6E-b1C-TZrr5NXm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مهلت ۶۰ روزه تمام شد؛ ایران و آمریکا در برزخ جنگ و توافق:
خبرنگار الجزیره می‌گوید مهلت ۶۰ روزه تفاهم‌نامه ایران و آمریکا به پایان رسیده، اما نه مذاکرات واقعی به نتیجه رسیده و نه جنگ تمام‌عیار از سر گرفته شده است؛ در این مدت، پیام‌ها و درگیری‌های محدود ادامه داشته‌اند.
به گفته مقام‌های ایرانی، این مهلت صرفاً برای مذاکرات توافق نهایی بوده و به معنای آتش‌بس یا پایان جنگ در همه جبهه‌ها، از جمله لبنان، نبوده است.
هم‌زمان، ترامپ از تمدید این مهلت سخن نمی‌گوید و مواضع تندی علیه ایران مطرح کرده؛ وضعیتی که به نوشته خبرنگار الجزیره، چشم‌انداز رسیدن دو طرف به توافق را مبهم‌تر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70243" target="_blank">📅 19:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70242">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=WtkQKHWc3FHT3pZHxt_wUfqJpkI42CKqDchdS_RU_8qnJWewMFB9op0adY0JdA7T9UnUkwfar4ElfncPJ2BQOT0StjlLtGrk32tb3xlZtt2Rm3Th83k1bm_V5zdMyz6iEQxXDF3dpz3VXamiXv8BQh-8F3a15OeMY8JnqKp9yodElvyM_7q81xmOjvnoxwrjcXtlhf7uCvFkZ53SwCRCmjAw90O1aOunr3H5aXtT_an2o-Bgd9ZxtsvjqdJP-TdnhXMucNpASqtgVhgUXVTVeH1M8apWi_KV8413N4lmIJyanErqq62qih6M0FXwWEgoznnxwfiBjKdjdr17Qw_a2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=WtkQKHWc3FHT3pZHxt_wUfqJpkI42CKqDchdS_RU_8qnJWewMFB9op0adY0JdA7T9UnUkwfar4ElfncPJ2BQOT0StjlLtGrk32tb3xlZtt2Rm3Th83k1bm_V5zdMyz6iEQxXDF3dpz3VXamiXv8BQh-8F3a15OeMY8JnqKp9yodElvyM_7q81xmOjvnoxwrjcXtlhf7uCvFkZ53SwCRCmjAw90O1aOunr3H5aXtT_an2o-Bgd9ZxtsvjqdJP-TdnhXMucNpASqtgVhgUXVTVeH1M8apWi_KV8413N4lmIJyanErqq62qih6M0FXwWEgoznnxwfiBjKdjdr17Qw_a2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
اولین جنگنده F-35A آلمان مراحل مونتاژ نهایی را پشت سر گذاشته و در تأسیسات «لاکهید مارتین» در «فورت‌ورث»، وارد مرحله تکمیل نهایی شامل رنگ‌آمیزی و اعمال پوشش رادارگریز شده است.
مراسم رونمایی برای ۱۸ سپتامبر برنامه‌ریزی شده و انتظار می‌رود نخستین پرواز آن در اواخر سال ۲۰۲۶ انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70242" target="_blank">📅 19:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70241">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70241" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70240">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7I6ZHzzZq_t2O48xBQ-oe-tEAJfHrSQDB0BXLiqlqyaOh8JESc01ZOw9AKmENfsANaibDTtx4KmdPBPL94pmVFunDbg0my9Zsegt9uDGVbeAVqEmIr5tFTftDSwB8u1HNk4AMsb0ylbrHDzOQIEdWICkjospZFjvqYHsnl7Gyjrv4RDWH4my5dHq8zkfu2BKwK2Kt0eSjNeBsaYbI_zgNWFNhWRz9BTqF2PcSzk9MdGUHynIZogbng0Z3n32sIKhcrqdIopSmacj_X4hTgoiadJbJ7MBqQ6VUHdGIqdYrK8xVPgF851rC3IEiucJ-vdhzjVIM6Wh3--84-yVtr1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g27
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70240" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70239">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0QS1SUenRCvLvTsFBlLkD1w8GUk8ShyHJIsvEIXg09DtXGWVejAakXxfw2ghMViLGmTiR4_U-HZlt2MQWl-r0F_WYlo9v1fe5h5QZ3WD7Im6wqqtRUJjGZZUmSjNWv9gE4OBmnpfKna-rfoj3tDHdw29fw8Ka1F63cy2oTM8BlljxOqJE4NtQHYSNhWsMXsMVMicypqpCmJOczpGjoycDlXcCBy7nsAtd45Ty5B2Qbp469eO0k-N8ddRoNIK-VN7wqC3a1J_BGaRaH0WiIUeoX69MaqO1g5d_r7a4ymaxPIllIxdflYGGbg6w48lyHs43cUCrrxue1iS20uhbpi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70239" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70238">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=BArul_8aoxBAe1NpFcHiUl1vtzRUu2M0mp641Oc6Zq_cTQlFCkvlCUmqH00e3y1Rd1URo6yNaLyYGCkUoZvn4s7ktq_pFG2Y8XCTGGJY-lM73T60eh7pYSIuNskpugb8ILrUcr4UxfTnGNkoEQ_Qi2A8HzWPwYsV92USGdQzyEYk8302r48eD5-sBcCq-KVREi9rKnzLqniVhDBnuA200DIkhzv-rlT8-8LHzsdGAV1uTKPZ5qyTGIch63qqLGON0RNY4jWagUtyWvdTNfrawzy17RPggiXd4mL7nnZoZFJDipFH2eKiOOpr_lNe51ZvqHJF-D4TEWwNiVHRzthYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=BArul_8aoxBAe1NpFcHiUl1vtzRUu2M0mp641Oc6Zq_cTQlFCkvlCUmqH00e3y1Rd1URo6yNaLyYGCkUoZvn4s7ktq_pFG2Y8XCTGGJY-lM73T60eh7pYSIuNskpugb8ILrUcr4UxfTnGNkoEQ_Qi2A8HzWPwYsV92USGdQzyEYk8302r48eD5-sBcCq-KVREi9rKnzLqniVhDBnuA200DIkhzv-rlT8-8LHzsdGAV1uTKPZ5qyTGIch63qqLGON0RNY4jWagUtyWvdTNfrawzy17RPggiXd4mL7nnZoZFJDipFH2eKiOOpr_lNe51ZvqHJF-D4TEWwNiVHRzthYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خیلی جدی: در به در دنبال یکی میگردم مشکلات مردمو حل کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70238" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70237">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aV8AS7G1dtTloaBXwhmKQqPfo7pkRdK1_D-wWj9koTEs7jk88RDwB8xDGbcsYwSqPF8S0k66Fw5tFmgZXv__obQ-DQdX9m_wvnqYFqch6VjELVBf4qh8TDJpuIs61ZG-0GmI3PmedNcoJPzvvRvn8eysY4ZL_O0bhHGIAKP4xKhx3ciPnfT5kmVO2eIFFqCozD0vy16334uODUz8J57UffbbdiazRdlMdExugXTWo0hEsISqdquRr3A8Lygf403pn3Bi02t_8lmeRKS0egCc4Me0HYXvD2fnDkgqFginVTuN7Y6nckGj2JW8Uav1NduWdaGah9vn4UwdwcP82Sqlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70237" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70236">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=I9pwKtmvlsB7zAtGrTVtre02_086B9fVk24sZ-zsxf2Th2GbAZAEqY8_j9JvmtqhTQ7QoTIqwL4T6tl9wy1KkyoQ8DZG7RpJLxyJZpYRLlZUsQnu0vKlCGn5YdcKzYMGm6-UV9cpFF3Rui_tEMTe_gpWRd4G2CDwlm6wAsY93JqS8GDjY2zL5GOF6KCd-v09_xkp9NYX_71A55QllRCenRN5ObCpmI5cFdwTSXhYxvBFViZAFPcS6CqZ_UE_Hee0pC8Z1GH3x77fEUhFc01jDpKCy7TDYqGfoZvEooR2FwelGrzvLjx-7kZRsoVBgndwuVJleUtJrTOVT6B4KL9lWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=I9pwKtmvlsB7zAtGrTVtre02_086B9fVk24sZ-zsxf2Th2GbAZAEqY8_j9JvmtqhTQ7QoTIqwL4T6tl9wy1KkyoQ8DZG7RpJLxyJZpYRLlZUsQnu0vKlCGn5YdcKzYMGm6-UV9cpFF3Rui_tEMTe_gpWRd4G2CDwlm6wAsY93JqS8GDjY2zL5GOF6KCd-v09_xkp9NYX_71A55QllRCenRN5ObCpmI5cFdwTSXhYxvBFViZAFPcS6CqZ_UE_Hee0pC8Z1GH3x77fEUhFc01jDpKCy7TDYqGfoZvEooR2FwelGrzvLjx-7kZRsoVBgndwuVJleUtJrTOVT6B4KL9lWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینطور که قالیباف داشت از دستاورداش توی لبنان می‌گفت ،
شبکه خبر هم با زیرنویس جواب شو داد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70236" target="_blank">📅 17:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70235">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=FhVxR_mNsptkKAIsdye-GGKDKx19qWJNfdVUfp8oLN-ZbGCTW9gAPBdwyzs4NyZl3eXw7J47A8QamfhrVmyKaFiNbJ9u8yW_DJ04bm3tozBlleHN2aiQquLdRBtIz02lPFal3jnjUBb1hrjWYMCnTLhZB-pOrHUAWqI63YcQthF5BGr7sNl3JckYy_jUhHFTjQtHR2rrAc8v41gXcr1R1GiMkMJJT6MdMQ3n7Vmx2cLxxPZnBDzXzrkO318rbSWmcfLRUUjzkTUHoOsQxkW3UApv7R7RddxxHr4E18Rvr7RIGt-a2f71gfElTwVUNIcq3AEGN0E_UkEzzeP2B50Q2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=FhVxR_mNsptkKAIsdye-GGKDKx19qWJNfdVUfp8oLN-ZbGCTW9gAPBdwyzs4NyZl3eXw7J47A8QamfhrVmyKaFiNbJ9u8yW_DJ04bm3tozBlleHN2aiQquLdRBtIz02lPFal3jnjUBb1hrjWYMCnTLhZB-pOrHUAWqI63YcQthF5BGr7sNl3JckYy_jUhHFTjQtHR2rrAc8v41gXcr1R1GiMkMJJT6MdMQ3n7Vmx2cLxxPZnBDzXzrkO318rbSWmcfLRUUjzkTUHoOsQxkW3UApv7R7RddxxHr4E18Rvr7RIGt-a2f71gfElTwVUNIcq3AEGN0E_UkEzzeP2B50Q2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز هواپیما C-295W آمریکا در ارتفاع پایین برفراز اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70235" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=wBvaXJVtTjAY_h2FH43URKvrkot3yYvav2VJbR_CMWeJ5xpg8n7vLMxIhJ14CgpxAZ-3a9-VgCNIcsrdmWEL82c3qVFAVpOTBZ_PO5MADhg5tbhUFmpSazfZslctQvVVPUiUpCQkS5AQAhtMqRHh5gFiTP_OUBaHEEtX9rRyPmVtsd1SmRdehN9OUVb5uexbcB19ckeEB6uDFbSG4ALOkWP60Ov8Nw4FVCdp1pkz2f3ZQnNuuIu-cAY6lIX00lURiQptwQblQLVFyQeKyTStOUbQm1dmT1oYC7fsYIhazpFB4dhoO7sJdIOfvfq16LtVUq6HG19fz3Pba6HiKG25dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=wBvaXJVtTjAY_h2FH43URKvrkot3yYvav2VJbR_CMWeJ5xpg8n7vLMxIhJ14CgpxAZ-3a9-VgCNIcsrdmWEL82c3qVFAVpOTBZ_PO5MADhg5tbhUFmpSazfZslctQvVVPUiUpCQkS5AQAhtMqRHh5gFiTP_OUBaHEEtX9rRyPmVtsd1SmRdehN9OUVb5uexbcB19ckeEB6uDFbSG4ALOkWP60Ov8Nw4FVCdp1pkz2f3ZQnNuuIu-cAY6lIX00lURiQptwQblQLVFyQeKyTStOUbQm1dmT1oYC7fsYIhazpFB4dhoO7sJdIOfvfq16LtVUq6HG19fz3Pba6HiKG25dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
هنگ سوم عملیات ویژه اوکراین، شهرک آندریوکا-کلوتسوو در منطقه دونتسک را آزاد کرد و تقریباً 30 سرباز روسی را به اسارت گرفت.
کسانی که به مقاومت ادامه دادند، کشته شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70233" target="_blank">📅 16:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLCSnsjq2aSGhWXXAkwzrM4DBWdTjjmTwT1E9z6R2atVpqjaAY98srxZVF7pRRGlqCh3GCs6Ffx_GtxHKve_-3khPdVXHTV1B-_BnmiqTqvy4IHh5d6-y3A5smgORgGoZmi5-KE0gUdfagvSjJeM2hLyotDASUjLySlCTKZnU1uGckrskMMAXdzAos5SkBbPLMjfjbdhIF_-coDlu-Y0eFysADRqG0sZos1naHVyPTEZsXeiKNJcmx8goLu--oWw1y4Pst6aI1D0CszAbsmE9p8cJxjQvyCJOooxtZmJDqC2_b4ECy3c4kgkyEtkWDWdvORopUJ3hbPOPW51Jcw4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
معاون وزیرخارجه جمهوری اسلامی:
همانطور که ترامپ نام خلیج همیشگی فارس را به صورت صحیح نوشت، به زودی توهمش درخصوص تنگه هرمز یا اصلاح می شود یا توهمات این متوهم را اصلاح خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70232" target="_blank">📅 15:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-0dHcU_SX9Tyz41wDjwSbsqC-x25NsVHPc1ojNKTiawxB-xO-z1K03i2p_Sc6gIN3_RvBoD48T5reu_MblCLNLVPocFYRyGsJ-Jvb0UdJTl648vwSH8G2Uu6LzWGQ85RR4ftgrBheh08bjgXK6w2X3i9U59K1y_pRyVcokH2S9a-PBZbGrQWMg2qFqh9_6vBih7ZJyzZsSkzg9n6BZ3St3cuv3DCNETOy6TWy5mkVRuJduKBmXsdUD90iwYpKEsl4-TBz-TSERMkkQXBg3sF6GWKagj_lgTh4J61cy8QhMA6KKXgmz6Foq523a0g6D21zY9WHUi4tCq_sGiywrJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
پست جدید املاکی در تروث سوشال:
تنگه هرمز قلمرو جدید ایالات متحده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70231" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06cc678393.mp4?token=ikuoD_-ycaaCsuJlH-1itM_Fn5ngpxh29K0nCsh8aDHRdLmyiK_x4BAEEYkYqLBf26mV3q5UC7yXJ-W5-vTR-x7Fm2Rc7wFqJN-o-X1zG2LH_L9FgAckQewFIgeYhUv2S9ZcerorNUGycehr8AmIEtIrqM9b-AEHtoMBoqRKj-b324qvBqBb6v3gdjNFqasBAqJNjbDZcnt9OL6w-yCWufF0ST5rWvE_2GnGJu_SG0d53Embsg2yzqJzCFRAZsB-hcBrOH1A0oZgZy6mutSqq0P3zbnKDtkYJTuJ-jd9mVUsxeanx_Z3Q_gWm0OJ-6JRHaVlCc6oKJMPyZPXfBfEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06cc678393.mp4?token=ikuoD_-ycaaCsuJlH-1itM_Fn5ngpxh29K0nCsh8aDHRdLmyiK_x4BAEEYkYqLBf26mV3q5UC7yXJ-W5-vTR-x7Fm2Rc7wFqJN-o-X1zG2LH_L9FgAckQewFIgeYhUv2S9ZcerorNUGycehr8AmIEtIrqM9b-AEHtoMBoqRKj-b324qvBqBb6v3gdjNFqasBAqJNjbDZcnt9OL6w-yCWufF0ST5rWvE_2GnGJu_SG0d53Embsg2yzqJzCFRAZsB-hcBrOH1A0oZgZy6mutSqq0P3zbnKDtkYJTuJ-jd9mVUsxeanx_Z3Q_gWm0OJ-6JRHaVlCc6oKJMPyZPXfBfEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جعفرپور، مدیرعامل مخابرات:
قراره فیبر نوری کاملا جایگزین کابل مسی بشه که اینطوری سرعت اینترنت ثابت تا 80 برابر بیشتر میشه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70230" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6829188988.mp4?token=ZGXuVBZUz9800uwQRJrvUPQ7pAJES6K7FvMXPZOluafOX1GaFnAFaZtb33r9AiP-XdxP2RfZ1hc_6jRwJot307azaYhdgJQjsVszt2F4p1T_SX4xllQD2vkh3kIGYsBwLqZwAqQ8GAsixTkq6Wn4w7-AA7QsMfmU02U8e6KuwiMU2gsShFaUXpsv5A8gfCWi3t3K7faDECPnt2kv7NzJzGOof2ahHo1V_wiDQRZitQovg-MGY68sXm7SuGbzlat4_YafrThz_67jk2cKWpR5KHoyQJTX89JiycnTPyCtEWTAPC85mBpjmjJgMUkpoZk9eZgIsdlxuRqjrS1vW10j7K1NLtMRNIt8yQctO0N5tB0NpKFgrbeBhFtD7JoqO2VO1jshzwJiHKHqJVBJG3vkVy-JDt1k2jRFSGmnpvZuIHC-kromMnejSa59irNHIf1XK4ueqxIrV7lrfXOkUWBemjt9VelCBMooy-m_t1i0FcmJc1fzOXrIcdFKC8Q4nIsOMpcvpHOtLGlmQuutepqU2lj-tcrj5JTSZSFBksNnfq3AXw4Gack9TODyYLLSOgbSb59Hua5uczDC8SK3gqwdTyRApCtOxwAhnMkYSDdxZKNLAYoSAPp-smg8_PGljomIOjdqu3foVQrZLjJsWQPo7AyX6UhXcJO8vbkxPURGvFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6829188988.mp4?token=ZGXuVBZUz9800uwQRJrvUPQ7pAJES6K7FvMXPZOluafOX1GaFnAFaZtb33r9AiP-XdxP2RfZ1hc_6jRwJot307azaYhdgJQjsVszt2F4p1T_SX4xllQD2vkh3kIGYsBwLqZwAqQ8GAsixTkq6Wn4w7-AA7QsMfmU02U8e6KuwiMU2gsShFaUXpsv5A8gfCWi3t3K7faDECPnt2kv7NzJzGOof2ahHo1V_wiDQRZitQovg-MGY68sXm7SuGbzlat4_YafrThz_67jk2cKWpR5KHoyQJTX89JiycnTPyCtEWTAPC85mBpjmjJgMUkpoZk9eZgIsdlxuRqjrS1vW10j7K1NLtMRNIt8yQctO0N5tB0NpKFgrbeBhFtD7JoqO2VO1jshzwJiHKHqJVBJG3vkVy-JDt1k2jRFSGmnpvZuIHC-kromMnejSa59irNHIf1XK4ueqxIrV7lrfXOkUWBemjt9VelCBMooy-m_t1i0FcmJc1fzOXrIcdFKC8Q4nIsOMpcvpHOtLGlmQuutepqU2lj-tcrj5JTSZSFBksNnfq3AXw4Gack9TODyYLLSOgbSb59Hua5uczDC8SK3gqwdTyRApCtOxwAhnMkYSDdxZKNLAYoSAPp-smg8_PGljomIOjdqu3foVQrZLjJsWQPo7AyX6UhXcJO8vbkxPURGvFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
هرفردی که با تصمیمات خود باعث نارضایتی مردم بشه از دشمن هست و تغییر شیوه کالابرگ حتما در دستور کار قرار میگیره
ما خودمون نیز در میدان مشکلات اقتصادی درگیر هستیم و راحت ننشستیم
نیروهای نظامی با اقتدار مجتبی خامنه‌ای تودهنی بزرگی به دشمن زدند که همه تعجب کرد
دشمن از روی استیصال اومد مذاکره و مجدد شکست خورد
خیابان محل میتینگ های انتخاباتی و برخی کارهای غیراخلاقی به اسم تجمعات نیست
تا رفع محاصره و آزادی پول ها و رفع تحریم های نفت و پایان تهدید و توقف کل عملیات ها در سرتاسر جبهه مقاومت تنگه هرمز باز نمیشه
تفاهم نامه باعث شد تاب آوری مردم بالا بره و از نظر نظامی خودمونو بازسازی کنیم
افزایش قیمت بنزین تدبیر نیست آقایان دشمن بر آشوب و اغتشاش از روی بنزین حساب کرده مواظب باشید
صداوسیما دیگر قدرت سابق رو نداره و عملا در رسانه شکست خورده حساب میشیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70229" target="_blank">📅 13:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=V0LGCEuSNomQdCYmddthQdn5CZWiGZMI6Xa4tAmqS9gdPF5C0laJQTC7ZFQ0yQlRRpDYy1m0TAin_U1rPwVoccASPaFcKWM9y3cvDqmx44iNkVzJiWbehkB2cDuJvjnurHvSbvAH4osF0_fQJcKfnjfMVhYWvkiClZnM6CHuzbTIP5FsA2Tn_EmxxajRl8PLDLbYrq7H3Sf0t0-95DpcWXGrkjhvUsvU5jeqBfOjFKsh6D5CSqmKb-hfG7tUvWI46ijyF5REvGWgUSBOp-K-XwutAHpfRxcXp2FoBoQj11lwexFEq2-CW2kRki6dUSMCfDtS7qA6mKrZX4WHsevREA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=V0LGCEuSNomQdCYmddthQdn5CZWiGZMI6Xa4tAmqS9gdPF5C0laJQTC7ZFQ0yQlRRpDYy1m0TAin_U1rPwVoccASPaFcKWM9y3cvDqmx44iNkVzJiWbehkB2cDuJvjnurHvSbvAH4osF0_fQJcKfnjfMVhYWvkiClZnM6CHuzbTIP5FsA2Tn_EmxxajRl8PLDLbYrq7H3Sf0t0-95DpcWXGrkjhvUsvU5jeqBfOjFKsh6D5CSqmKb-hfG7tUvWI46ijyF5REvGWgUSBOp-K-XwutAHpfRxcXp2FoBoQj11lwexFEq2-CW2kRki6dUSMCfDtS7qA6mKrZX4WHsevREA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تفاوت وحشتناک قیمت گوشی ها در عرض یک سال:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70228" target="_blank">📅 13:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=KMd7H1uwEwYfRla40skhpcRoId351u6f450wGT9IZBi6OE0UxP0gxq18I3B6V06881Q_KFzHjUQfgcjreasNV8XSUxpSW5wRYwCP69Qvu0e6OY03GGXWlpI1hV21pViL3K7Scz3zlgSWDWG-y0dMQePZLewJS7knnffwJZyh4aPUa6jsQLMHsHwFHLHOoZrzU_Yik9CkgVY912DovWTSeVZUkZzoy-gDkAiRskQqCWlmKYWQ5LXMErqgPgucdAHCYku312tLHPPQmu_29QOdDrEYVAMYvI3CAumIPxHeOSYCi22x31lX39gUS1UDJkLD_xU8eR84gAjfpbx3_kBhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=KMd7H1uwEwYfRla40skhpcRoId351u6f450wGT9IZBi6OE0UxP0gxq18I3B6V06881Q_KFzHjUQfgcjreasNV8XSUxpSW5wRYwCP69Qvu0e6OY03GGXWlpI1hV21pViL3K7Scz3zlgSWDWG-y0dMQePZLewJS7knnffwJZyh4aPUa6jsQLMHsHwFHLHOoZrzU_Yik9CkgVY912DovWTSeVZUkZzoy-gDkAiRskQqCWlmKYWQ5LXMErqgPgucdAHCYku312tLHPPQmu_29QOdDrEYVAMYvI3CAumIPxHeOSYCi22x31lX39gUS1UDJkLD_xU8eR84gAjfpbx3_kBhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
محمد‌باقر قالیباف:
قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه ها و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70227" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90eeeac0ea.mp4?token=fQTbBRIhv8jdvoyYK5yA4KuAnR0YRvQrU-yfnf3uQ40sYP1JR9cJUNB1R0ua3lgoaCx8fDXhbWML2oGUrCMWaP7q1FDDtyW0r_i2QmOnu9bnQ6IyIHVEoJstBHFkaQrtw8nRf4sanUpwscrPtXiejyb9lufLu47Kghmh9fH_9OtEM31eOtEhgXx9wSPl8O1vH67nu_HI5TjmN3qL1mydyZQZOWXZgd4lppdkom8fZ64u-5llMeK9F0mobXEQ4-KSdn-kXBvfzUDFkDLj8vsHiBYvKmeEEbXQ9cTkdPKGXq5qsWmuX4sHpxSQ3rl9bow-CmtIoI2Ka7iOA_dcmIUWhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90eeeac0ea.mp4?token=fQTbBRIhv8jdvoyYK5yA4KuAnR0YRvQrU-yfnf3uQ40sYP1JR9cJUNB1R0ua3lgoaCx8fDXhbWML2oGUrCMWaP7q1FDDtyW0r_i2QmOnu9bnQ6IyIHVEoJstBHFkaQrtw8nRf4sanUpwscrPtXiejyb9lufLu47Kghmh9fH_9OtEM31eOtEhgXx9wSPl8O1vH67nu_HI5TjmN3qL1mydyZQZOWXZgd4lppdkom8fZ64u-5llMeK9F0mobXEQ4-KSdn-kXBvfzUDFkDLj8vsHiBYvKmeEEbXQ9cTkdPKGXq5qsWmuX4sHpxSQ3rl9bow-CmtIoI2Ka7iOA_dcmIUWhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند چون یه گاو از طریق ترانسفورماتور دچار برق زدگی شده مردم با چوب دارن ترانسفورماتور رو میزنن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70226" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/70225" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70225" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=CcR4wqit_Sj032Jo72TO2poNR6xgrJJ3naR7rxhH0oJUEHAH2e1eno8utB-zlqFu-HYbU8nAS1UYly3NPR-6DD7ApkjgiZxOJVnlZjJ42ETIHENEy3kGLT9rxaHMZmeo2z2e7eksGtc-Qp5WMYo-jTRYXJ2PLcaiLuFCQGfkdfS4rBA2L0pspb2GHmmdCjWz9Nmnw8Y7cwSdDAGqvNoAbMcdpm9yuME00dpxkNA4Zb8OuwMd-wKoXJlM_elI-W-Z2zbdVJxEERXfrWXH8bu7N64b0ZXR02UyJqfPUTgL3wyJtfRkxLu9-t4-lrpUHwbcsHWEefHj2_0-YcF3wmbvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=CcR4wqit_Sj032Jo72TO2poNR6xgrJJ3naR7rxhH0oJUEHAH2e1eno8utB-zlqFu-HYbU8nAS1UYly3NPR-6DD7ApkjgiZxOJVnlZjJ42ETIHENEy3kGLT9rxaHMZmeo2z2e7eksGtc-Qp5WMYo-jTRYXJ2PLcaiLuFCQGfkdfS4rBA2L0pspb2GHmmdCjWz9Nmnw8Y7cwSdDAGqvNoAbMcdpm9yuME00dpxkNA4Zb8OuwMd-wKoXJlM_elI-W-Z2zbdVJxEERXfrWXH8bu7N64b0ZXR02UyJqfPUTgL3wyJtfRkxLu9-t4-lrpUHwbcsHWEefHj2_0-YcF3wmbvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
😅
😂
😆
:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r27
@betinjabet</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70224" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c5472e37.mp4?token=Z0h-9JLUwqLyVxAA1L_kEzK2iCULfOBo2a6LA1DbUQ3lD09Hb_0h9UzW7xL0kXGah9hmvjiNQ5qORd5O6saMrCh5BJjMpCRa5h9RMx5L8Icb0jlsKBBBjCATIKWduFNEOnmA_dpBKStTmWKCslMAfnzGwxEyDLjdQhjLkfe_MCe1GK9vOE3BT3H5pT10H62R4ww1jlvfrnlAXw0pBHQp00KoPuAVmCrMRkMBTrSZ-WM_9O5kEKMZdP8_7EWXoR7-OLKIlnAKfRHxqtorsvMcUNK9saA7EUgnK4enN-mQ457uLW336SYQV1D3A79fONA9fR6z0GelZkrxHcf0QBHPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c5472e37.mp4?token=Z0h-9JLUwqLyVxAA1L_kEzK2iCULfOBo2a6LA1DbUQ3lD09Hb_0h9UzW7xL0kXGah9hmvjiNQ5qORd5O6saMrCh5BJjMpCRa5h9RMx5L8Icb0jlsKBBBjCATIKWduFNEOnmA_dpBKStTmWKCslMAfnzGwxEyDLjdQhjLkfe_MCe1GK9vOE3BT3H5pT10H62R4ww1jlvfrnlAXw0pBHQp00KoPuAVmCrMRkMBTrSZ-WM_9O5kEKMZdP8_7EWXoR7-OLKIlnAKfRHxqtorsvMcUNK9saA7EUgnK4enN-mQ457uLW336SYQV1D3A79fONA9fR6z0GelZkrxHcf0QBHPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر فلاح نژاد: امشب یه دختری دوس پسرشو آورد پیشمون که گوشش کنده شده بود؛
گوشش تو دست دختره بود،گفتیم جریان چیه؟
😟
گفت دوس پسرم به حرفام گوش نمیکرد اعصابم خرد شدن گوششو گاز گرفتم از جا کندمش بعد دیدم حالش بده آوردمش بیمارستان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70223" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9e0c9bd0.mp4?token=RkJ9jYyD5GgWmMNMXVbhIUUGprnPdr9M-i_cj9YGfb3hNViq61GFuux-a47GZSCUZeBeNFzsrDhjsN6Thoud758WoOWsffS0ByQ2LmplWgjP9355FhTWsNUxruVwELJecMoT_RJofUAMY9QgOMbDDKVArYhoMWo46-zHTRJBDCtmGFviV2uux529CvuUthr5ltb0OZKyA-6X2ppVjqmZZ2n3DOg2EO7SvVFjuALzgX16XwxfS4PqAK2yodROJix-3D60dQnZgn_vqwCgXNxUczGrsEGCG2Bp1qgBF6fY-KTFZ1bX8aCRxjf48Q_t4dwKM_Lt8F5lZnyLIZBl2B5ypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9e0c9bd0.mp4?token=RkJ9jYyD5GgWmMNMXVbhIUUGprnPdr9M-i_cj9YGfb3hNViq61GFuux-a47GZSCUZeBeNFzsrDhjsN6Thoud758WoOWsffS0ByQ2LmplWgjP9355FhTWsNUxruVwELJecMoT_RJofUAMY9QgOMbDDKVArYhoMWo46-zHTRJBDCtmGFviV2uux529CvuUthr5ltb0OZKyA-6X2ppVjqmZZ2n3DOg2EO7SvVFjuALzgX16XwxfS4PqAK2yodROJix-3D60dQnZgn_vqwCgXNxUczGrsEGCG2Bp1qgBF6fY-KTFZ1bX8aCRxjf48Q_t4dwKM_Lt8F5lZnyLIZBl2B5ypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی الیگودرز لرستان اومدن کف رودخونه شهر رو اسفالت کردن!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70222" target="_blank">📅 11:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=YkDSxpQUtJsYBCoJvu4YGXNQMs5wSGsEI62FSmzkYiM6G79lj3bFvnlIaRVJ4hA4mF1e3LXHJlEZqvpfi7IKfOm6HAvODUlkGUra7SmWT7Ofi_chcvQGww4WdkLzoaQTDfGXCsAvhtQDVQR92UkboAnkILzDqXDI4G1SIcqoz-qqLJ1e9qZT9Q8QlLIIbUKyhb7MHo1FC-YFucaebFOtlJwNpsUIpcnG4fksQB-x3iIldb1eth4XK3OO4pg1a28xWhHBVAve5XaRr7ZGSOp6o684FMSr8Bh5f_ai-0xb65eqng2q25HGJuCR29XiH-QFmLLI6ufCfuHz9Dg0_S1a8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=YkDSxpQUtJsYBCoJvu4YGXNQMs5wSGsEI62FSmzkYiM6G79lj3bFvnlIaRVJ4hA4mF1e3LXHJlEZqvpfi7IKfOm6HAvODUlkGUra7SmWT7Ofi_chcvQGww4WdkLzoaQTDfGXCsAvhtQDVQR92UkboAnkILzDqXDI4G1SIcqoz-qqLJ1e9qZT9Q8QlLIIbUKyhb7MHo1FC-YFucaebFOtlJwNpsUIpcnG4fksQB-x3iIldb1eth4XK3OO4pg1a28xWhHBVAve5XaRr7ZGSOp6o684FMSr8Bh5f_ai-0xb65eqng2q25HGJuCR29XiH-QFmLLI6ufCfuHz9Dg0_S1a8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایرانی های حاضر در ترکیه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70221" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=N0flmHDFNqUNEpZK6UQ6Hy1wmsp-Ttjyi6wHTKtybZ0WH3ZIQS_EY00iepGNQ9E2v3Sm0pFIkjcXQK4Ni38HQ0bW0gAdpjRlnG889z04Uuz5UizZA4brWRrQ2gHmSJw5ndx5Z0AG6tJY5v4ozdMjFLE9_QiKLkVLrdGrr6IOyZk9EOArqC_msatU-ZTXXWoALJsGh6MazDCerZFpYe1t8wBKp9jq8QMTdGBL8hBIj88nhqRhkCdlITw9NmkDe2HkocvNstriG_NXpE3Q182-B7S-92BUE0IfrsAzc2zlfmlmWIFnBYumqzIA8DJoOWIVcTT8SgHF4JGgoLTmERlFtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=N0flmHDFNqUNEpZK6UQ6Hy1wmsp-Ttjyi6wHTKtybZ0WH3ZIQS_EY00iepGNQ9E2v3Sm0pFIkjcXQK4Ni38HQ0bW0gAdpjRlnG889z04Uuz5UizZA4brWRrQ2gHmSJw5ndx5Z0AG6tJY5v4ozdMjFLE9_QiKLkVLrdGrr6IOyZk9EOArqC_msatU-ZTXXWoALJsGh6MazDCerZFpYe1t8wBKp9jq8QMTdGBL8hBIj88nhqRhkCdlITw9NmkDe2HkocvNstriG_NXpE3Q182-B7S-92BUE0IfrsAzc2zlfmlmWIFnBYumqzIA8DJoOWIVcTT8SgHF4JGgoLTmERlFtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
وقتی میگن ژاپن تو یه جهان دیگست یعنی این ؛
اومدن خیلی جدی یه سوتینی ساختن برای خانما که تو تابستون بپوشن و با خیال آسوده برن بیرون تا گرمشون نشه یه وقت
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70220" target="_blank">📅 10:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70219">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4716008946.mp4?token=NOhu7k0k2mxxS91zLpyFewBl10QYVFIF5km_MHe6k9XoEuPlwNL6meZifUcwaHpo7JIy5re7toVixQZpL4oN0Tl0upqjx3fK3NBEDAyPYZ_7-9HeuhhPH6t6kBR9EuFL7o5L8BC2h7HGKhBZlAE7Z-0W3G26qCNSggIEtaAihIqAvrKpdhVDo7tgXOPi84Pk8KMh_ZNC6HubrMQeL9FkLUSk6rxdOtrpbomWGbBqsf-vDM077UQxG0HgexWIa0ntqI2Y0SiUJqhA4VtpJiGRnEboVo31noPdulb6AwmWE5wL1iIfJz8kPJJGjSQvBnDvsiWhQoEeKb7_XtBsUBK6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4716008946.mp4?token=NOhu7k0k2mxxS91zLpyFewBl10QYVFIF5km_MHe6k9XoEuPlwNL6meZifUcwaHpo7JIy5re7toVixQZpL4oN0Tl0upqjx3fK3NBEDAyPYZ_7-9HeuhhPH6t6kBR9EuFL7o5L8BC2h7HGKhBZlAE7Z-0W3G26qCNSggIEtaAihIqAvrKpdhVDo7tgXOPi84Pk8KMh_ZNC6HubrMQeL9FkLUSk6rxdOtrpbomWGbBqsf-vDM077UQxG0HgexWIa0ntqI2Y0SiUJqhA4VtpJiGRnEboVo31noPdulb6AwmWE5wL1iIfJz8kPJJGjSQvBnDvsiWhQoEeKb7_XtBsUBK6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلاغ کینه‌ای؛ سه سال است که دست از سر این پیرمرد برنمی‌دارد.
یک ماجرای عجیب که این روزها در فضای مجازی دست‌به‌دست می‌شود؛ پیرمردی ایرانی ظاهراً نزدیک به سه سال است با یک کلاغ سمج حسابی مشکل شخصی پیدا کرده
طبق روایت منتشرشده، ماجرا از زمانی شروع شد که پیرمرد یک جوجه‌کلاغ افتاده از لانه را برداشت. از آن روز به بعد، کلاغ‌ها هر بار او را می‌بینند به سمتش شیرجه می‌زنند و سر و کله‌اش را هدف می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70219" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uflAbnx1y7453Le2fMaGhvGQBxSKp-QIs6CHF6YuFvoYGM56vbngi6kpaH8JRh8mKQSuqVZHFfqHrBWxhNb329mpO-GFNlSiv7CgRkQva68u1EM0nEBuEdnqpkkGHahS7jwUPduBHCi1HYnkCXzBNdrVejyDr3zke1m6wvXO4nLcSRXedvoLhHrQyOilpehWefYi4uD2BUK2uB-MbVwXAJ3X80gCykhCJwmY4-drq6a3Q02P-LBLzwRDWPzAbAF3qjbVZS_Uc8fCfoshvWIO-VlLeq2Zi7jXoNjW6MDt_2eebMgSp0MzirZODqipLzFbfpqTYxVaqoGYLKLW4jFoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ساعاتی پیش سپاه‌پاسداران به یک کشتی در حال عبور از تنگه‌هرمز حمله کرد:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک کشتی هنگام عبور از تنگه هرمز در مسیر خروج، مورد اصابت یک پرتابه قرار گرفته است.
این برخورد به موتورخانه کشتی آسیب رسانده و منجر به تلفات جانی برای یکی از خدمه شده است؛ سایر خدمه نیز تحت امدادرسانی گارد ساحلی عمان قرار دارند.
تاکنون هیچ‌گونه پیامد زیست‌محیطی گزارش نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70218" target="_blank">📅 09:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=kLIabfGPzzsTs_IDhLWzi_THo6PdMn0pdA_EUKh2_Zfoap6aXFXak9bSlkpVF3gLHpbnwJt86QeHlkWKqukOibMzvgIF2IlbcS7Nm7ORYJB50SihK674lrSC4J1via2kuiF95Ts0TmbAvluEbzc08TpCl29hw1DtsnUbkIZkMb4-LDxRJLewn1vdY9ri7aLsfuANo-lAt9awDF2-i0XGPpZKz8kGR72ZlU9hSYjVe4JHa_Utp5ecRjHGX7n6e1xm1cqRVx6k5yaNhE7JjmdH7NqxK8259G2ZWUxqG84Fh4DiDea3LaxDXLlUV2aYXBsPRa2as6ZxMas-5plrwlNBpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=kLIabfGPzzsTs_IDhLWzi_THo6PdMn0pdA_EUKh2_Zfoap6aXFXak9bSlkpVF3gLHpbnwJt86QeHlkWKqukOibMzvgIF2IlbcS7Nm7ORYJB50SihK674lrSC4J1via2kuiF95Ts0TmbAvluEbzc08TpCl29hw1DtsnUbkIZkMb4-LDxRJLewn1vdY9ri7aLsfuANo-lAt9awDF2-i0XGPpZKz8kGR72ZlU9hSYjVe4JHa_Utp5ecRjHGX7n6e1xm1cqRVx6k5yaNhE7JjmdH7NqxK8259G2ZWUxqG84Fh4DiDea3LaxDXLlUV2aYXBsPRa2as6ZxMas-5plrwlNBpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بخشی از صحبتای دیشب ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70217" target="_blank">📅 09:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31325063ce.mp4?token=vwz9TwPXaB8kLT1-iwP-RJpi9RG8JT3HKFwtUdZ396JPMlejoG83jDDMe22jFTGZMLksrtLTNgcXNtWIK-C1C9ae-sH-vkdfv01kFkt45o9_KlSugPIFuwCgj2BgzdUxob0nGMQsR4y0i9w8HftjHABxn2-h8_BXhceA0e1HCPBOBYQ1uQF-tygOP85okocDcH61LQfXJnakDPOAAii28Q8TvGQJkbXOyXii-_yFM8jxQMDECWSJfzpmmuQMEpqjukOUZsBNvaMY8o-q75u4RyyxD92jEOVe2UEURDLpf1TX--PwD3ix_ozLzIcNpOjAFHT5XovZA1vXV3VzWHjbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31325063ce.mp4?token=vwz9TwPXaB8kLT1-iwP-RJpi9RG8JT3HKFwtUdZ396JPMlejoG83jDDMe22jFTGZMLksrtLTNgcXNtWIK-C1C9ae-sH-vkdfv01kFkt45o9_KlSugPIFuwCgj2BgzdUxob0nGMQsR4y0i9w8HftjHABxn2-h8_BXhceA0e1HCPBOBYQ1uQF-tygOP85okocDcH61LQfXJnakDPOAAii28Q8TvGQJkbXOyXii-_yFM8jxQMDECWSJfzpmmuQMEpqjukOUZsBNvaMY8o-q75u4RyyxD92jEOVe2UEURDLpf1TX--PwD3ix_ozLzIcNpOjAFHT5XovZA1vXV3VzWHjbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
گزارشی از مجتبی پورمحسن:
همزمان با تایید تماس محرمانه دولت آمریکا با فرمانده کل سپاه‌، ترامپ، در پایان مهلت ۶۰ روزه برای توافق، از تهران خواست تسلیم شود.
اما وب‌سایت اسرائیلی وای‌نت، با انتشار جزئیات تازه از زندگی مخفیانه مجتبی خامنه‌ای، از تسلط سپاه بر جمهوری اسلامی خبر داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70216" target="_blank">📅 08:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70215" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=lG2lmpAgoZrdwm4DMYPOuAVe5ummJyaDk11iBAjKSQtS7xUiuXmwEgkls1Eb88fo17P7zHm_3VWAFNjISeTdZKS3v-_FuOuYsbaHSHHW_o20grFBqMTbaFyR4zJQ6jXx7mkSpYCSFq0uLO394KEDcF_To55Ie1q2ZX_oIMOjrVHEt2-6NBu1uYJixPQoZuDGdyKsm722LkLQXelUYmuvbT_DX0ViG8Mw4KXC0wLFWU03mwcHB96_br4yHSxowlUE9E8k4SkwbFKtQCU1PAPcgdtgvK1E_veO--3055RQOUj_n98pVINICF3LehDBXx9dq-WuyQNzkIvYdr621ssFQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=lG2lmpAgoZrdwm4DMYPOuAVe5ummJyaDk11iBAjKSQtS7xUiuXmwEgkls1Eb88fo17P7zHm_3VWAFNjISeTdZKS3v-_FuOuYsbaHSHHW_o20grFBqMTbaFyR4zJQ6jXx7mkSpYCSFq0uLO394KEDcF_To55Ie1q2ZX_oIMOjrVHEt2-6NBu1uYJixPQoZuDGdyKsm722LkLQXelUYmuvbT_DX0ViG8Mw4KXC0wLFWU03mwcHB96_br4yHSxowlUE9E8k4SkwbFKtQCU1PAPcgdtgvK1E_veO--3055RQOUj_n98pVINICF3LehDBXx9dq-WuyQNzkIvYdr621ssFQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70214" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgVp16Yeje2SS6WIjWhDMRjALupjL0QLOlbZWtfC0UWXkxj-0HBJmHZVepgxj7TFLaU2IyEzOaZ67-mQ0YW4vU1Czk3_oLhC6oKsV6WhmlUMJiD0dFmKz2iutAd9Ik3Ith_xmcA-XJKq1OtG71LSxAsbbFD2ZoMchKuM95VWUoovj5HCw0vl9ck11m100dJgzg8k7J275t4MRd1HG_gARzuMpcckXxNk7Et4z03nNrBnE5IQaxeXeuAhpSQKIEgQhb8aH6fdqbhttj1IqPH48VSrBuv0O02ohj_hURNJc4oZu4Ed_B-F8Xlzp1zvGLixl6aLb_SEBQ7JCcC1EXVl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید املاکی در تروث سوشال:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70213" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70212">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=JSQ-9-hvt2ujW2UnZC64gZ4Iy3ux0kHd4k91MlJHPOesce9lH2Rtal3thS-2RTggP0kPIqH-VRpAZefzY1A8ofiW7Cp9XPdtNyjIZnExW3UF0D-yk3ruL8PNHaiIibbups4sgf1FbeptNYwOgDlVEAtNxF39G0ilQQ_fdk3oPr7tAc2lWmpT6v07OOGpJQEEcIHZ4eLNtJriliE-lfFusV6q0fBkCJ9Vx9IzC2wHw_N1OmF-BQwMlZmdDdrYfaJkJg7x_d_zxMtNiXBCcsW79L01e_ZjHdYCjGpFZ016oXwJX440WU8WEZWxSbom8Lzpn4y0UGmqy3_gi-juKHu9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=JSQ-9-hvt2ujW2UnZC64gZ4Iy3ux0kHd4k91MlJHPOesce9lH2Rtal3thS-2RTggP0kPIqH-VRpAZefzY1A8ofiW7Cp9XPdtNyjIZnExW3UF0D-yk3ruL8PNHaiIibbups4sgf1FbeptNYwOgDlVEAtNxF39G0ilQQ_fdk3oPr7tAc2lWmpT6v07OOGpJQEEcIHZ4eLNtJriliE-lfFusV6q0fBkCJ9Vx9IzC2wHw_N1OmF-BQwMlZmdDdrYfaJkJg7x_d_zxMtNiXBCcsW79L01e_ZjHdYCjGpFZ016oXwJX440WU8WEZWxSbom8Lzpn4y0UGmqy3_gi-juKHu9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
جرد کوشنر درباره ایران :
ترامپ فعلاً فشار اقتصادی رو بیشتر کرده
اگه ایران حاضر بشه توافقی رو که درباره کنار گذاشتن توان ساخت سلاح هسته‌ای داریم جلو می‌بریم، نهایی کنه، ترامپ حاضره یه توافق خوب به نفع مردم ایران ببنده
ولی فعلاً ایران دنبال انجام کاری که از نظر ما منطقی باشه نیست
الان آمریکا با بخش‌های مختلف دولت ایران خیلی جدی و بیشتر از همیشه در ارتباطه و گفت‌وگوهای خوبی هم داشتیم
البته بعد از این همه سال، اعتماد زیادی بین دو طرف نیست.
ایران داره جدی مذاکره میکنه و این مثبته، ولی هنوز به نتیجه نرسیدیم.
ترامپ هم عجله‌ای نداره و وقتی توافق درست آماده بشه، می‌ره سراغش
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70212" target="_blank">📅 00:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70211">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20632f388.mp4?token=iN-CN5GLW0c6lQilIEF--8qkzGIuLbzpCP1WU30WfkTWO0VxyiFn-b8gHChuDoj6aSgByflFwL_DyhUBfQD4AoCBa_JdHs0BKMUUeICFz0Gn6Qx83O2ZBMrpEX1XGp8FOTu8UHxgpILtCwCuSGQXb1v3oVDe1WXwviB0_dM3dR4MfDSSjEN5oPaudM-CbA-TkZoYKEb7o2XQA5_6hENW3_WGOa7k2zjWnr2W0tLi32muV_uUrwFJOkRU8BCccihlafSVe-mcQOgT565vD30tBE38pPVpC42PZYIl3zyWhMwOBYWY8C5fULXIbjl6SFODBHLAtFst40G49aW6TM2UIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20632f388.mp4?token=iN-CN5GLW0c6lQilIEF--8qkzGIuLbzpCP1WU30WfkTWO0VxyiFn-b8gHChuDoj6aSgByflFwL_DyhUBfQD4AoCBa_JdHs0BKMUUeICFz0Gn6Qx83O2ZBMrpEX1XGp8FOTu8UHxgpILtCwCuSGQXb1v3oVDe1WXwviB0_dM3dR4MfDSSjEN5oPaudM-CbA-TkZoYKEb7o2XQA5_6hENW3_WGOa7k2zjWnr2W0tLi32muV_uUrwFJOkRU8BCccihlafSVe-mcQOgT565vD30tBE38pPVpC42PZYIl3zyWhMwOBYWY8C5fULXIbjl6SFODBHLAtFst40G49aW6TM2UIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
موسوی، نماینده مجلس : بنزین ما اصلا هم ارزون نیست؛
اگر حداقل حقوق مارو در نظر بگیرید، برخلاف حرفایی که گفته میشه ما بنزین ارزونی نداریم.
ما با حداقل حقوق، میتونیم 130 گالن بنزین 3 هزارتومنی بزنیم، ولی یه نفر تو آمریکا با حداقل حقوقش میتونه 750 الی 800 گالن بنزین بخره.
ما اقتصادی داریم که طرف یخچالش خراب میشه، میره زیر خط فقر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70211" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70210">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7953006a94.mp4?token=gYZAaCVGD1pOUnvBnHlf81SYJTI1hTEzvrRf9qEkDbAeYV3GejCyitu__dPzq3-vxGbDY5uXPrlM99mHQg18-hoEPzAUVYKNW67R8K3lqH-9u5JaPZk6ph9BZO_DRav8jqZn8aoJRjKNL55y4l3fMQq4V0r5RicPTukspAKq2nw3-h05Nybbnb-UCGUZjAOBgEm9ITT4FeJn_6f8tribe6gEs6U9CGSzEobEnLUZwmzAjqnrqiShpXr5egGmLzao6trMGo6CkcUsZmUFZQ7-lEa9YxE2IQFhz4Ug8Qjmlt095dCMAjVxgBhFC4AKpNaxFMwiib9tdwrfQNr7Sk1xpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7953006a94.mp4?token=gYZAaCVGD1pOUnvBnHlf81SYJTI1hTEzvrRf9qEkDbAeYV3GejCyitu__dPzq3-vxGbDY5uXPrlM99mHQg18-hoEPzAUVYKNW67R8K3lqH-9u5JaPZk6ph9BZO_DRav8jqZn8aoJRjKNL55y4l3fMQq4V0r5RicPTukspAKq2nw3-h05Nybbnb-UCGUZjAOBgEm9ITT4FeJn_6f8tribe6gEs6U9CGSzEobEnLUZwmzAjqnrqiShpXr5egGmLzao6trMGo6CkcUsZmUFZQ7-lEa9YxE2IQFhz4Ug8Qjmlt095dCMAjVxgBhFC4AKpNaxFMwiib9tdwrfQNr7Sk1xpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی، نماینده مجلس:
درباره احتمال جنگ زمینی با آمریکا گفت در چنین نبردی «جنازه» نیروهای آمریکایی نیز به خانواده‌هایشان نخواهد رسید.
تصرف یک پایگاه آمریکا در عراق، کویت یا بحرین می‌تواند سرنوشت جنگ را تعیین کند و به آن پایان دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70210" target="_blank">📅 23:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70209">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=g8tX54cpkVPhVQh93w2Vx3Sd0gJC_1rExtSoVSanD9sOPCi8sYLGVvk9PD3A-oGk3t69yU5BBQdA9wzpGUPXB5WHSlzYmrrScxQFLAX6eAzXk2I-JFwa6flPwdvJM_k2QIqFDSJNgleZi2tcsZ8XDMo263G9RQWqxljlwHfrf6x0wn9AmGxwEI84NQm4c_9U-0DiL0-jdJWB6JWLWLUKsYCXLPyxHswHzmhNQTfIz_ITJTHHiZR2Mx9dl1RgjncrbqiSm4roBwQDnAgY0WXozVnqXzJfZCuDRXh6y_rbiL19ly6-Kgdz5Aex9e1OohKrYvzXQt8P3LCJKvigeK1I4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=g8tX54cpkVPhVQh93w2Vx3Sd0gJC_1rExtSoVSanD9sOPCi8sYLGVvk9PD3A-oGk3t69yU5BBQdA9wzpGUPXB5WHSlzYmrrScxQFLAX6eAzXk2I-JFwa6flPwdvJM_k2QIqFDSJNgleZi2tcsZ8XDMo263G9RQWqxljlwHfrf6x0wn9AmGxwEI84NQm4c_9U-0DiL0-jdJWB6JWLWLUKsYCXLPyxHswHzmhNQTfIz_ITJTHHiZR2Mx9dl1RgjncrbqiSm4roBwQDnAgY0WXozVnqXzJfZCuDRXh6y_rbiL19ly6-Kgdz5Aex9e1OohKrYvzXQt8P3LCJKvigeK1I4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری لفظی ترامپ با خبرنگار سی‌ان‌ان:
🇺🇸
ترامپ: ساکت، ساکت، ساکت. خیلی بی‌ادب هستی. ساکت. از کدام رسانه هستی؟
🎙
خبرنگار: من از سی‌ان‌ان هستم.
🇺🇸
ترامپ: شما «فیک نیوز» هستید. ساکت باش، ساکت باش، ساکت باش. تو یک خبرنگار جعلی هستی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70209" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70208">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=jTKXTrZzLZovo0DocUJTn5T8QF2YU8vgQgvazUiC8ioDk42oNBeiZLQTeC_Js4BJGRdsiBu8-NE3FtpMeokliCmIX70hVwtZkbuX1F4pabh_5ynhgoipBRbNuCrevhxjMQIwHL2J7d0uESJJ5b8sR7P7VePsz_PSfqxh6zNcxkk9qDe9-6PQFY4WlhwrVghdVH9UAi9hzjyTZxkULRjHN5xkYhxN-HQVhLMtfBxfnbDKjPmvIkIscLFgrz55f7qQjh20BtQgpoGJ75rpHI31ZifI8diQtgOFJkWk0OXdV-RIISfAKf0q-1u-R5DxOSgbAEsebunZqQoxY6xbd-XapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=jTKXTrZzLZovo0DocUJTn5T8QF2YU8vgQgvazUiC8ioDk42oNBeiZLQTeC_Js4BJGRdsiBu8-NE3FtpMeokliCmIX70hVwtZkbuX1F4pabh_5ynhgoipBRbNuCrevhxjMQIwHL2J7d0uESJJ5b8sR7P7VePsz_PSfqxh6zNcxkk9qDe9-6PQFY4WlhwrVghdVH9UAi9hzjyTZxkULRjHN5xkYhxN-HQVhLMtfBxfnbDKjPmvIkIscLFgrz55f7qQjh20BtQgpoGJ75rpHI31ZifI8diQtgOFJkWk0OXdV-RIISfAKf0q-1u-R5DxOSgbAEsebunZqQoxY6xbd-XapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:ایالات متحده به دنبال تمدید یادداشت تفاهم با ایران نیست.
ایران در مخمصه‌ای بزرگ گرفتار شده است. وضعیت کشورشان آشفته و نابسامان است.
ارتش آن‌ها به‌طور کامل شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70208" target="_blank">📅 22:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70207">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=BKboW8_G7s-yxTOT4d9P77WVHg5Yu6EL4e_aXJe2hDOeJuH1xHvS_asmKPq0GzxqKptqjc7-yo_kMRSfrbH0HFbXyUIxAeyCAP5HxpRPOenM6VX4StTLV2w7GVBnWwRSeAXHdiWwN-j-dfhfu2P69TZ3pwRY5UfH2N-PGeAqyYIQyxEw4I1uLoDq-vTC2Tbr9Vse-zcebY2IpAR-G-K6XlRCHT9dwcnrDYQtIBC8bFFlLrM76w71Vk4V3fU1mPjI_ZBbvcSQfBKxjqK0EEHzq11N0jFAmdQNgvlu3YY6nFxmidRf23gsM6HAoVbRxILnxuzBwRlnVZ2W2mYPs_WVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=BKboW8_G7s-yxTOT4d9P77WVHg5Yu6EL4e_aXJe2hDOeJuH1xHvS_asmKPq0GzxqKptqjc7-yo_kMRSfrbH0HFbXyUIxAeyCAP5HxpRPOenM6VX4StTLV2w7GVBnWwRSeAXHdiWwN-j-dfhfu2P69TZ3pwRY5UfH2N-PGeAqyYIQyxEw4I1uLoDq-vTC2Tbr9Vse-zcebY2IpAR-G-K6XlRCHT9dwcnrDYQtIBC8bFFlLrM76w71Vk4V3fU1mPjI_ZBbvcSQfBKxjqK0EEHzq11N0jFAmdQNgvlu3YY6nFxmidRf23gsM6HAoVbRxILnxuzBwRlnVZ2W2mYPs_WVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، آنجا را به شدت بمباران خواهید کرد. آیا می‌توان گفت که صبرتان در قبال عمان — که یک شریک راهبردی است — لبریز شده است؟
⏺
🇺🇸
ترامپ: فکر نمی‌کنم رفتارشان خیلی خوب بوده باشد، اما ما خیلی راحت از پسِ آن‌ها برمی‌آییم؛ درست مثل کارهای دیگر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70207" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70206">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=Duq2d-Y-eAsztWsJNCF-KjP8mgtz5yX3rbIFUqCVnluDxQ1BiBu0U1bYMxui9x-tOLkSnXhK9LfgoQa6vHguDDUjgxZMG9bxPANZszWes_X4BeYYRfweJINUuJ51UWGz0tJgIWm0W0EmzzArr7i6kjgAzs3sBadHGND7e8IPvqnfkL0GLoRzdCDhebjCgyrX3U6139XoQDrHNKasq8kbIYQcTYCMgD0wqqvhlgtal1WF_l6k4WWqvhdSXaUtR4ztoDwRitWFie8-PGCkUfkoaYDiSkcWJL3vK7pWG3nP2tD33OmnZssWkHRGE_7B_KOOd6P0g8K7M0NJ5SP-bN-gSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=Duq2d-Y-eAsztWsJNCF-KjP8mgtz5yX3rbIFUqCVnluDxQ1BiBu0U1bYMxui9x-tOLkSnXhK9LfgoQa6vHguDDUjgxZMG9bxPANZszWes_X4BeYYRfweJINUuJ51UWGz0tJgIWm0W0EmzzArr7i6kjgAzs3sBadHGND7e8IPvqnfkL0GLoRzdCDhebjCgyrX3U6139XoQDrHNKasq8kbIYQcTYCMgD0wqqvhlgtal1WF_l6k4WWqvhdSXaUtR4ztoDwRitWFie8-PGCkUfkoaYDiSkcWJL3vK7pWG3nP2tD33OmnZssWkHRGE_7B_KOOd6P0g8K7M0NJ5SP-bN-gSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: اعتبار تفاهم‌نامه امروز به پایان می‌رسد. آیا به دستیابی به توافق با ایران نزدیک‌تر شده‌اید؟
🇺🇸
ترامپ: بیایید ابتدا کارمان را با رایدر  تمام کنیم؛ بعد که تمام شد، به چند تا از آن سؤال‌ها پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70206" target="_blank">📅 21:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70205">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz5AVaXjbCQM6yERkY4lkYweDqTzIlETagLao1BiBfQpufdjJ8i9qs8fiGF-hKIilGEwre_UZBKfX9l0OHQlICrDp2rTnlclVYHwl_7pwQy9V0fcZzdXNuM-8zIwg4MnMBCeAC0_Gjzha7XH_vmS13SIr5d2cXpD2Z6Zt_mAWkLy9dfaNEZyP0CAihh4LdH8SflVPVqVD9sOpKKsfayr9rSsHXWapEboucpoaFueuOHrMI98Kl3PWrF93NpWQOmclxcNIwz87Ub9e7wmyTK4OVprDvdmiHqBZwhkN2FGpzFOKCiG-SPSuMuJbrbxY7W4CDXnou20C-9Kk9_4LXgHeHqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz5AVaXjbCQM6yERkY4lkYweDqTzIlETagLao1BiBfQpufdjJ8i9qs8fiGF-hKIilGEwre_UZBKfX9l0OHQlICrDp2rTnlclVYHwl_7pwQy9V0fcZzdXNuM-8zIwg4MnMBCeAC0_Gjzha7XH_vmS13SIr5d2cXpD2Z6Zt_mAWkLy9dfaNEZyP0CAihh4LdH8SflVPVqVD9sOpKKsfayr9rSsHXWapEboucpoaFueuOHrMI98Kl3PWrF93NpWQOmclxcNIwz87Ub9e7wmyTK4OVprDvdmiHqBZwhkN2FGpzFOKCiG-SPSuMuJbrbxY7W4CDXnou20C-9Kk9_4LXgHeHqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده و حسابی گرفته رو رامین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70205" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70204">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=L5ogIoV2Fnz1wyJJWJTm77oEBqxtgrqskgAIvRO-iXmvMshXsbARll5jsvXGNPquvN99bT8QrF2YAIDOw2-TqllI8FygJ46pqCjKiZHedUl73HiZbyBK1OW_mvxnLRYEJ6WlbBw7sRBV4r9lLaLvogX5CPCYArQhm8Amquu2AkOvtAfRQwjYBtfeC2nO5b1uVPWEGGDmU5zItRvJXf6BehtmeeVBzGgFvLlaB_Dosyi2O32SfN-r0DFs5klwUDrjRsNBf_mMVOcQIuT629LxQ1veMSUN6vwNM9HbCEwxvZHbX9WAIF3BlDVJ77gJKr3QGQbbkLXMwzRMoTprM5tZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=L5ogIoV2Fnz1wyJJWJTm77oEBqxtgrqskgAIvRO-iXmvMshXsbARll5jsvXGNPquvN99bT8QrF2YAIDOw2-TqllI8FygJ46pqCjKiZHedUl73HiZbyBK1OW_mvxnLRYEJ6WlbBw7sRBV4r9lLaLvogX5CPCYArQhm8Amquu2AkOvtAfRQwjYBtfeC2nO5b1uVPWEGGDmU5zItRvJXf6BehtmeeVBzGgFvLlaB_Dosyi2O32SfN-r0DFs5klwUDrjRsNBf_mMVOcQIuT629LxQ1veMSUN6vwNM9HbCEwxvZHbX9WAIF3BlDVJ77gJKr3QGQbbkLXMwzRMoTprM5tZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما اومده یه برنامه ساخته به اسم«با عرض معذرت»که محتواش تمسخر ترامپ و کابینه دولتش هست و قراره از اواخر مردادماه پخش بشه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70204" target="_blank">📅 20:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70203">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
فارس:
یک نفتکش اماراتی در نزدیکی قشم توقیف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70203" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70202">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=W6Via_YRFop1hzW7ZoI_grO7dMDAdHDO5eRjqWk0ICuSe6qFFtMMUl36ZJUDrrHEwTD_QCX5Pxf_qIlSZwhvYp8C7edbj_IZBH-H997O5MUzMyxn60Jc_ueGSC68IKbtIh4VNjNI5Rcv8HBOVmojQ2u90SUI6Ue2IeoZhcH_TtBcLC0fPxnrXrVrvtGq0ak42kY93L0VgH9yI6QQf-gya461Ja4kpMhcn5QJ7rW3LIW33qmOlLFhZaCDeqCyTccdkm_rLztlbt1nOzQkBzPcFITol8FOxUDx1SjJEUI4VOt2leE0B1sAOtY3OsgCPiErQp8MKNszAVtbw-EpQdED4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=W6Via_YRFop1hzW7ZoI_grO7dMDAdHDO5eRjqWk0ICuSe6qFFtMMUl36ZJUDrrHEwTD_QCX5Pxf_qIlSZwhvYp8C7edbj_IZBH-H997O5MUzMyxn60Jc_ueGSC68IKbtIh4VNjNI5Rcv8HBOVmojQ2u90SUI6Ue2IeoZhcH_TtBcLC0fPxnrXrVrvtGq0ak42kY93L0VgH9yI6QQf-gya461Ja4kpMhcn5QJ7rW3LIW33qmOlLFhZaCDeqCyTccdkm_rLztlbt1nOzQkBzPcFITol8FOxUDx1SjJEUI4VOt2leE0B1sAOtY3OsgCPiErQp8MKNszAVtbw-EpQdED4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جمهوری اسلامی، شروع کرده هر کسی که جاوید شاه میگه یا به مسئولین توهین می‌کنه رو بازداشت کردن!
یه نفرو دستگیر کردن، حالا جرمش چی بوده؟ توی کامنت اینستا به مسئولین فحش داده
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70202" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70200">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvQiHkpICcqut1QvUWC-A_DY-WWRe5U74Y5dxU4q38eujvyMjrAC9oP4fJRigAHZ-HkCJw4wWwn4gTz76OvmsvKrJHmErCYPfA8XRqIm9tow1G7jSdBYSVxBBNjyO7Ol0wWLCpzGaqlCZ1veAYhQXY7FgnRRlqdTKlaIUKEb9SreSigTOfLdOtCYqvbBL5Iyt5S_rylA4a6R5Chv6fFUgPnBwIWdWki5WKfc3h0LKlgwNmAqE6sZmRLXx8VbeD0f0EMS_Hj5LBxfgWtGj157bdfJQvlFAUY2R8ctNUfLYBvNKGStJDMmHedX9e8pfM15640hhQEqaaVbEqRMMNLtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbiyJFdYAAMK8N_pAdSnBVU4tyno7R-afsZFMY_NPaMaX5rc_oW5fbSTSwMlorIg-RH9phbI1OBzcnsz2ycuhcEUVBUe2aIZVUzHWN-uIHYDSDRUlqabAAFYiMmt5Sp61Y1Nv2xDPojRaVzbolmlmek5FiyhwnMd8bSlfB7EnPvdR65LYE6kgjsNDEc7f1QUsvJU_FQr_PKFjqBVXd_UadRKIfR5sN2r52wYuqOucYNgoUvG3gM8Tzr1qZsRW_c-ssIvruy39wKWtn9YahLv48asYig32EB96Dx9Xj3cbiIcePC-f0fQ8XSVyfE1vk2WcM1j1tLi_hJ_v-A33y1t5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
استوری های جدید گوهر فرشاد و افشاگری های جدید از رامین
رضاییان
:
جول فرشاد: رامین ازم میخواست تیری سام بزنیم.
رامین ازم درخواست محتوای جنسی میکرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70200" target="_blank">📅 19:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70199">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=FENpjdiw69WweBEHZ7ffZumpNslekJ3S-PV6Sl_oEem9nuppmknDKnwjHGAbEKKVoiKI-FOlhYPlPGpZFhGFdiOUREHfllBF2NAX5xGBy01OU-Sj_tQxf6vAkufcb2Qa-HTyYo0MF3RXxXtz9Rcd9i7VfFZAybxdyQPQVQiTom_2B42nR6m7lz3Jr38fVsk-AEEPZY4PlWrx8Vt-IN-9ZlQ9zTXhQu40oFsC4yIGqubZmX8RUJETOCTvnAsRNLDpYz5fdzqniw61-5ecPAHAv9cCDhJYiP6cluQ1RD8NQNyTxOmq17PwbwdSLxztyaZn7W1l2Bp83pAJC1ht__FbXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=FENpjdiw69WweBEHZ7ffZumpNslekJ3S-PV6Sl_oEem9nuppmknDKnwjHGAbEKKVoiKI-FOlhYPlPGpZFhGFdiOUREHfllBF2NAX5xGBy01OU-Sj_tQxf6vAkufcb2Qa-HTyYo0MF3RXxXtz9Rcd9i7VfFZAybxdyQPQVQiTom_2B42nR6m7lz3Jr38fVsk-AEEPZY4PlWrx8Vt-IN-9ZlQ9zTXhQu40oFsC4yIGqubZmX8RUJETOCTvnAsRNLDpYz5fdzqniw61-5ecPAHAv9cCDhJYiP6cluQ1RD8NQNyTxOmq17PwbwdSLxztyaZn7W1l2Bp83pAJC1ht__FbXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
فرمانده کل ارتش:
«اخراج ایالات متحده محقق شده است و آن‌ها دیگر اجازه ورود به خلیج فارس، دریای عمان و تنگه هرمز را ندارند. همگان باید بدانند که پایگاه‌های آمریکا به هیچ وجه قادر به بازگشت به وضعیت پیشین خود نیستند و ایران هرگز اجازه چنین اتفاقی را نخواهد داد.
تنگه هرمزِ مقدس، یک ظرفیت ژئوپلیتیکِ خدادادی برای ملت ایران است و این اهرم قدرت هرگز به وضعیت سابق بازنخواهد گشت. یکی از میراث‌های رئیس‌جمهور آمریکا، فعال‌سازی همین ظرفیتِ تنگه هرمز بود.
ما از وجود این ظرفیت آگاه بودیم، اما بدون این نبرد، آن ظرفیت فعال نمی‌شد. هر هزینه‌ای که در این مسیر متحمل شویم ارزشمند است و ما تحت فرمان فرماندهی معظم کل قوا، با تمام توان از این ظرفیت حراست خواهیم کرد. این اهرم قدرت، یکی از پیش‌شرط‌های پایان دادن به جنگ به گونه‌ای است که سایه جنگ را از سر ایران دور کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70199" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70198">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70198" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70197">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6mZrKPMfmlz8FFrM_adm3MA5xm99xEHMxT3TlQgf16U60V7TIr9fW6LqWPEm4jZotzzFI65i5BYqsrUBTqixeIvp0HDEh7U8Io33nB-juRxwlV48lCoG3E1-N6UbM-HFCm8aZUNLvxL9p8KSjBVMMS7p1sKxqP9xieQxrg_DqnTN6UywCk8dF09E3GLS4sJGSFIHJLAeHVV7u_9Zu-EdyDS8FzMvoRyFr5mgIDY1zQaC8ygWyYV-PxA7LlPMqreHZwAY9BUE772-VEOmEeNNIaTl0EWY8kBBQKx7mz0_Sv9_ro4Aaqn4TL1AQrLD0QywEAZHcpkMQAi4lKNv-jt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g26
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70197" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70196">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIgEeIoSWBIyxPQWTbCMrLIbCX_FxkrgKByUxb1bDP6AevLCDWhG2pWa1St4b5QceeG32MeHy9cge4JD8zKaHHf3tTIGUspIG4N5L6aCQawfwW8DKJSx4OanWUuh2DqBE_PgMQ7-2T_dtfhSTPhRJjJ8e7cXVXST4bSLAp3H4MT5L19WD7dfJJWqEBxwXDAGjsIvdy9x7NW8tBoPsIrZufKqPY7glwxeoIoqF89egEVinis7_1b6PWRWNRtec7wXXPA234nM9vUnMNaTHEdwVdgifGJ7ChPVI__lF27I-2F257_vwk-Q0a55sWI94M2Jj-4WoCXWeb_dk9j9CaMs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز: ضرب‌الاجل ایران به ایالات متحده؛
ایران به ایالات متحده اولتیماتوم داده است؛ یا به دیپلماسی جدی بازگردید و محاصره دریایی را لغو کنید، و یا با گسترش دامنه جنگ مواجه خواهید شد.
به گزارش رویترز، این ضرب‌الاجل — که گفته می‌شود حداکثر چند هفته مهلت دارد — از طریق پاکستان و قطر به اطلاع ایالات متحده رسانده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70196" target="_blank">📅 18:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70195">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=MgyDCc1UWX7DUY-oLzgPfRzFEWDPuSb0axqA08irpqyf17phCWgtTuteK-C1GaWfKVLA8ejZYSBtMCfZBFtBIi25nbV-S_IDd08N0ZQOEhvskkOVPKKJgjyyotaykyz_bm7KBcJcZ7Qg72ev4Aon6XKdRy1F6_zsliPfWWcuHCjg9EoUvbOg1HmN8OvvvGUpTc75wwpZdzg-kIOjGX0hw-rE4MEoFL4VXcPKOjS0dqwx9DKC16K65d19WPDfzRxow86o1JTDTGMiOobIkDihEZrfwcdwvs9jcGaniaSJYENWvw5fXL5fbjhIG8uu-Uwv1grVXrOhza9EIB7QiNaElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=MgyDCc1UWX7DUY-oLzgPfRzFEWDPuSb0axqA08irpqyf17phCWgtTuteK-C1GaWfKVLA8ejZYSBtMCfZBFtBIi25nbV-S_IDd08N0ZQOEhvskkOVPKKJgjyyotaykyz_bm7KBcJcZ7Qg72ev4Aon6XKdRy1F6_zsliPfWWcuHCjg9EoUvbOg1HmN8OvvvGUpTc75wwpZdzg-kIOjGX0hw-rE4MEoFL4VXcPKOjS0dqwx9DKC16K65d19WPDfzRxow86o1JTDTGMiOobIkDihEZrfwcdwvs9jcGaniaSJYENWvw5fXL5fbjhIG8uu-Uwv1grVXrOhza9EIB7QiNaElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اخیراً عرزشی‌ها این فیلم رو با موضوع «فیلم لو رفته از نشست مجتبی خامنه‌ای و پزشکیان» به مغز نداشته بقیه عرزشیا قالب کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70195" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70194">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:  ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.  ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70194" target="_blank">📅 17:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70193">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kboQcojhg2QWyDEWInPlkbVvSZW4DhAZ-Ywxh229xXIST0unLpKz-JucBFipI0xvXpBYVX0Jnw3d5n6bjTaJBglyVcaxnBOBHBDeAhjJItefvz2JhCQIY3Fkq8vAd1iIZy8PoGk7hQIJfwbHeDLtRpRalXkzyIOH0afm0FH20GP86TSElddt6mjSG-_qesKtcZiLr6wzoNIqS9eJzgmVa2UPb915NwwqR4yl5mrv940mISY_xDgP1mRlZ1TvA5Wf_y8WGkdDEatMQY96dkFbLww96xf5HDzT39h6uHq91rNv2HdSJbUgGy7Uy2lvtB552Tl7Uk8ZVv630zFMFowJYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kboQcojhg2QWyDEWInPlkbVvSZW4DhAZ-Ywxh229xXIST0unLpKz-JucBFipI0xvXpBYVX0Jnw3d5n6bjTaJBglyVcaxnBOBHBDeAhjJItefvz2JhCQIY3Fkq8vAd1iIZy8PoGk7hQIJfwbHeDLtRpRalXkzyIOH0afm0FH20GP86TSElddt6mjSG-_qesKtcZiLr6wzoNIqS9eJzgmVa2UPb915NwwqR4yl5mrv940mISY_xDgP1mRlZ1TvA5Wf_y8WGkdDEatMQY96dkFbLww96xf5HDzT39h6uHq91rNv2HdSJbUgGy7Uy2lvtB552Tl7Uk8ZVv630zFMFowJYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دزدی خونوادگی یه خونواده از فروشگاه؛ از دختربچه تا مادربزرگ، همه توی دزدی نقش دارن!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70193" target="_blank">📅 16:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70192">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8wotCSMyFZl0cO2AXRYKrSXcpbCaoQTzUJwMlJn5GzaOsjEED6W5TbVfLbpUSmUvXtt7m3vmgwFVncIanjs01vIjeWxqSp97mDyMsR0QDNjfRC61CTJiQf38X__jl9uMTmCYvAitI6ijMsLa7B0YA640g1ZLyDGkGTeeQ3HzmOhTkbKIqGrI63LDBIgzlbJsIYIDSM3EPtIdYxyLAVXJiCyOqO8g7hmG_ECnj5opIdc8M9M7LE_6l8qzyuy1CHC80ciqD_b433T42-HWnvgMdMK3kXvk-IRBh1yekVIaKFUJfopD4PSMc7TTTb4viI1yYxaZJTANEwPne7oWwZiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس‌نیوز به نقل از ترامپ:«اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه گفت که اگر عمان در جریان تنش‌ها با ایران در تنگه هرمز سد راه شود، آمریکا آن کشور را «به‌شدت بمباران خواهد کرد».
ترامپ این اظهارات را روز دوشنبه در مصاحبه با «تری یینگست» از شبکه فاکس‌نیوز بیان کرد؛ آن هم در شرایطی که مهلت آتش‌بس میان آمریکا و ایران رو به پایان است.
ترامپ گفت: «اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
ایران هفته گذشته اعلام کرد که در حال مذاکره با عمان درباره چگونگی بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70192" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70191">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=Jxp37ZPtCkA3Il88CrKlrKrgOrQlJw8eilOrVBVco3CVBJcpumjRk_BOyKyFVuSFKgQ2PlLehzMZ3duDb280qzZ0v4C6wuectzs9-3iu60CPHXl-vtC9Zg6Z6mxviZkfxZSCRSGlds2eqgzg6nxjbdTJKdmMIvP-cXgUqpJCTCwUl1mRQpilK5GAZ7jzAxF9Z2BDgZOkzl-IMbkAkya5W9QvwvoLNlBmu2yB3A_iZoQOoFu263aseJwnUUDHnu2YZyA7CP7rPvRKndZj1fyqmLrb1AX6JwI7SRzN4Bef-U3iT16GVGfDTSINMM4xoF6YWH9zuwwaJqjNbQUXAkthkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=Jxp37ZPtCkA3Il88CrKlrKrgOrQlJw8eilOrVBVco3CVBJcpumjRk_BOyKyFVuSFKgQ2PlLehzMZ3duDb280qzZ0v4C6wuectzs9-3iu60CPHXl-vtC9Zg6Z6mxviZkfxZSCRSGlds2eqgzg6nxjbdTJKdmMIvP-cXgUqpJCTCwUl1mRQpilK5GAZ7jzAxF9Z2BDgZOkzl-IMbkAkya5W9QvwvoLNlBmu2yB3A_iZoQOoFu263aseJwnUUDHnu2YZyA7CP7rPvRKndZj1fyqmLrb1AX6JwI7SRzN4Bef-U3iT16GVGfDTSINMM4xoF6YWH9zuwwaJqjNbQUXAkthkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یولکا؛ رهگیر پهپادی روسیه که برای مقابله با پهپادهای اوکراینی به کار گرفته شده است.
این پهپاد با تکیه بر رهگیری خودکار، به سمت هدف حرکت کرده و با برخورد مستقیم آن را منهدم می‌کند.
مزیت اصلی یولکا، هزینه پایین و امکان مقابله با پهپادهای کوچک با یک رهگیر ارزان‌قیمت است.
ویدیو، نمونه‌ای از استفاده این سامانه در جنگ روسیه و اوکراین را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70191" target="_blank">📅 15:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70190">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=MLnPEDj9xt9ktAy3AQRkHy554Je3Z_ysG3rsday8StNiquUQ_KeH9iFGmTOcr2l1es6u13yxZpwyZmzwowH7i8TM644nKNg0MG79h3zv14u8jSvkhkWRFp2UJg_9mE-_ZtoKvn8zE3GnjcvQ5ELbbWCte3ICg6KETuomnDWmnvzx31QonNSujnT-IXMPGyg1zRQFu8bbO1YSeVg5fKWA3CV1eTv2JLBvbmox3tpaB8DR5POgKtjXzQO8xJ0vvglN4ijs8m6qOFgG3aHCp8cELo8CAczCLsAUlD8asdPFSBNeMFKbnC9PKccWycTDLshsRmvjNCinXq-fWZnZs9pE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=MLnPEDj9xt9ktAy3AQRkHy554Je3Z_ysG3rsday8StNiquUQ_KeH9iFGmTOcr2l1es6u13yxZpwyZmzwowH7i8TM644nKNg0MG79h3zv14u8jSvkhkWRFp2UJg_9mE-_ZtoKvn8zE3GnjcvQ5ELbbWCte3ICg6KETuomnDWmnvzx31QonNSujnT-IXMPGyg1zRQFu8bbO1YSeVg5fKWA3CV1eTv2JLBvbmox3tpaB8DR5POgKtjXzQO8xJ0vvglN4ijs8m6qOFgG3aHCp8cELo8CAczCLsAUlD8asdPFSBNeMFKbnC9PKccWycTDLshsRmvjNCinXq-fWZnZs9pE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70190" target="_blank">📅 14:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70189">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=D7DYNO3kXjcmvmp38F2WV7rUaPycpf9lHY75GCyjRO2w9HB9sILvBUxH5Bfz-SBA4kTKBxegEQTKd-k75ugFr1vm_FUjZHWrvpY9uTM3hNaLvEBkQo6xt7se20494dGpyoEos5y7KAiASrPBVKH67DUpD9t_prCjZyxoULOCBoZK3_cJvJnK1aht5RLrCvboTC-wx8dWNSZ7aeIwPUDa8Df0kjSvQ3QS9TlcRf0ujaUAZTbYuZmTrvmc8r3x8spwjDAxThYh8MOGs7K9A0w-Smgez5Gs_UIcobm29aIRFtxR0ooG9wdY1z7H8WXViBH3BWNJSSf4PbXm8JXu-oOb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=D7DYNO3kXjcmvmp38F2WV7rUaPycpf9lHY75GCyjRO2w9HB9sILvBUxH5Bfz-SBA4kTKBxegEQTKd-k75ugFr1vm_FUjZHWrvpY9uTM3hNaLvEBkQo6xt7se20494dGpyoEos5y7KAiASrPBVKH67DUpD9t_prCjZyxoULOCBoZK3_cJvJnK1aht5RLrCvboTC-wx8dWNSZ7aeIwPUDa8Df0kjSvQ3QS9TlcRf0ujaUAZTbYuZmTrvmc8r3x8spwjDAxThYh8MOGs7K9A0w-Smgez5Gs_UIcobm29aIRFtxR0ooG9wdY1z7H8WXViBH3BWNJSSf4PbXm8JXu-oOb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
اگر عمان مانع ما شود، ما آن‌ها را به شدت بمباران خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70189" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70188">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=fi8ahb6nLEMOMgbWdu8Au70v2NOf0PF8-nDl7AxBHp-_3mLjcLp85AFWT_HOCvtAnAFzyyFC5IpCzdi6Gaz1t1U6QX2ZAvgOdW9CIUXGAHt6g9LdRZ59P3UJZIindJB1juix8n-f-kDJ4bxbymP2rZC8Crg8ZqqqGKsNtDcdVrz6I35yW3AHCyhesZpr6p1kAMp6Ei49KHnWP1LKNJyHkZMdzCZ2mCnbZ-zHuAO94jaY6FvP5-mPtx4RMclclfcoEmsOb3WARw63i5GKjJDeqjobL7WGxbQy-Egl9Ws8YnRaRQSM_XAd998fRZ6Jb_Sq6oD6AtDu6df_HPYnRmr87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=fi8ahb6nLEMOMgbWdu8Au70v2NOf0PF8-nDl7AxBHp-_3mLjcLp85AFWT_HOCvtAnAFzyyFC5IpCzdi6Gaz1t1U6QX2ZAvgOdW9CIUXGAHt6g9LdRZ59P3UJZIindJB1juix8n-f-kDJ4bxbymP2rZC8Crg8ZqqqGKsNtDcdVrz6I35yW3AHCyhesZpr6p1kAMp6Ei49KHnWP1LKNJyHkZMdzCZ2mCnbZ-zHuAO94jaY6FvP5-mPtx4RMclclfcoEmsOb3WARw63i5GKjJDeqjobL7WGxbQy-Egl9Ws8YnRaRQSM_XAd998fRZ6Jb_Sq6oD6AtDu6df_HPYnRmr87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70188" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70187">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO6lYaw9XVVMoAtWYJgUiBXsXk8pfcMo5qDkyWMUMkpczeQFsJ_eM-po84IVN7-Txs7OuQwnYknLCtXB0rUIfqeNbdr0IeSq3BzAqSA1wsi1Mr6gMhZ2pyBycV0aMo-cwtXgNKoZYsSp-4N_PcK4wH9E1b_M2hfJrpP8eI-6fJ-mRAQFYKwAYKiYg_pqLTz0Dast8c5DbNgcHpgImXsW3HZlXAkqTiwyhLJ0KdXobqd6F3RVDgFhrqOhiZZNzuLlwh1htA9p6kfUo0800L4TL8njCv_O8Qhig5m_IxjAMOpfSJCkJacOkH_3yqWoxpJyLLvLPvBAi7LQQwmWqcDHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ترامپ در گفتگو با شبکه فاکس نیوز:اگر عمان بخواهد مانع‌تراشی کند آنها را به شدت بمباران و نابود خواهیم کرد.
ترامپ همچنین وجود یک کانال مخفی غیررسمی با سپاه پاسداران را تایید کرد و در ادامه گفت «هیچ عجله ای ندارد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70187" target="_blank">📅 14:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70186">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW5Xu8yWZR_LjBufSbCfOs2PIi5jbkhHumPChUZaOnLp_jeUivSN3hwUIyqjdE_pdSotYqDa9hY7aq--WALQWY5qViYnamFmlBfGx6Cx_HpfJ1mUsoG6ENfs28wt8Tih8joX-rny4L-ZKDcrmhHQvPU7O2x95gbb2MViks_IIWGfB5l0bMyLtUh9eWJH3G5lPHhUAavajZQVLBCqiY62xenpljjwn4L4k9an-fgb1wbKWY6EpC3UJoXNnbsmSHTpFkt14yz0xvForwGeV3A9sd7rF2Bw7mDuERoyAMXOg677jgCP0tV588vwnmCnktcNDoN5DYrh1XbhjIFerGk4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
📰
وال استریت ژورنال:رهبری ایران ظاهراً جنگ و درگیری فعلی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی گسترده‌تر و طولانی‌تر آماده می‌کند؛ هرچند ایران همچنان از نظر اقتصادی و نظامی با محدودیت‌هایی روبه‌روست.
🔴
آماده‌سازی ایران برای رویارویی احتمالی گسترده‌تر؛
بر اساس گزارش وال‌استریت ژورنال، ایران پس از آرامش ایجادشده در پی توافق ژوئن، به‌جای تکیه صرف بر دیپلماسی، روند بازسازی توان موشکی و پهپادی و تقویت ساختارهای نظامی و امنیتی خود را دنبال کرده است.
این گزارش همچنین از افزایش هماهنگی با نیروهای منطقه‌ای، تشدید فشار بر کشتیرانی در تنگه هرمز و دریای سرخ و افزایش تهدید علیه زیرساخت‌های انرژی منطقه خبر می‌دهد.
به نوشته این گزارش، جریان‌های تندرو نیز نفوذ بیشتری در ساختار نظامی و امنیتی ایران پیدا کرده‌اند. هدف این راهبرد، ظاهراً افزایش هزینه هرگونه حمله احتمالی به ایران و تقویت بازدارندگی در برابر آمریکا، اسرائیل و کشورهای خلیج فارس است.
در مجموع، ارزیابی مطرح‌شده این است که تهران درگیری کنونی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی بزرگ‌تر و طولانی‌تر آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70186" target="_blank">📅 14:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70185">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoJ4JDf4zZRkpBM_0If45e5rMWbPGdgQrqXn3tNu6n8fIlvvpXStJEEDZXSx8yCGe7kPwe3mzCiehkSd5FP8aZ8Rjko6BFOICbfh6nzQGjNBAI-yFgAgm6tnGTwaJcWo25-7e0m_qftaCcB6hj7tj5SV9qR-7QpAR7vZDITURyTdEx_TT7aJbkRAHqYtA-EFITXa67zZ3aofVpJiKY2wNrHHoU21yiYphKLeu4L9JB1XpW7FWIbxHUtiRH5vkxhwvJK9pcVDbC8o5Wm0w_gA063HcVVi75t4yP3f8n7DuQVgFfw1o-KfqpCgq391dRaf75WFdEOtCk8DnZqbJ31Oqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
هدف اصلی این است — و همواره چنین خواهد بود — که ایران به هیچ‌وجه و تحت هیچ شرایطی نباید به سلاح هسته‌ای دست یابد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70185" target="_blank">📅 13:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70184">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎤
خبرنگار
:
آیا جلسه‌ای داشتید؟
🇺🇸
ترامپ:
جلسات زیادی.
🎤
خبرنگار:
جلسه‌ای درباره ایران؟ پیشرفتی؟
🇺🇸
ترامپ:
🚶‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70184" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrcYiLyfb7zNlOUyAFEU1wtacGBdn7Lj7y4KMckUYeq0XFGO3v07a5ZkoT5aWfakPmHaVZkMnpT41NHygT4gvGKtviHJMr99YNzBsju7igWyRe67WbpPWRJSOw4Q5HHeLhrL_Ft5VP2mKJMZwDi79vSX8CBBijVsH2FwjxFKfz4uoE33YVs4z8Njp9LuFiWv8ENgA3xcWeQLkG6w2PKK63SlGTO0RO-ihW9iEnhYbc4zKkIYMJRQTHoDxi0_c3BXP6gveYQGrC9NkchkxAjIGTZaVJ4-gzY14tbuzNJ0mSTETNdhhoME2zVjCpBYbkjQFt5CcYuIsPaNGUtq17Ycuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم؛
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ» را داشتیم که حالا وضعیت جدیدی پیدا کرده است.
مهلت ۶۰ روزه در واقع ۶۰ روز فرصت برای مذاکره به‌منظور دستیابی به توافق نهایی بود و اساساً چیزی به‌نام «تمدید آتش‌بس» وجود ندارد.
قطر و پاکستان به‌عنوان واسطه پیام‌هایی را ردوبدل می‌کنند و با ما در تماس هستند، ولی این به‌معنای مذاکره نیست و تصمیمی برای شروع مجدد مذاکرات با آمریکا نگرفته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70183" target="_blank">📅 12:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70182">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=SMST8-WA3YrfAXIH38g8ApIFShcS2r5A4IVVo8eSNHXN92_y2x8-uQvZxE2zzz06X91I64p-NzCwZytc14aI-LToZkKNE9I8xpBh_gu5UqTFIY9MJL3teAClSCgHj9h70r_w6CwXEFngtoHWKQIJjqkgvcl4rpyM4hHDrvq7ZbFHqC2LxVmEw7eJ4opuhy0OeDzHe90bGwcWf5kjt6bBd4qg6IrViSzBwTDY-XS3RDoKnq4n605gQRB8D5ftq2uQ7GfNKo0AL8_4eEHSyq8jOFH3UkDQjGxr8DB64y_yh6vZp_71m6cUQXW8SWWJJzwKXSe5h6-QNvu2ZQmhWI2ZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=SMST8-WA3YrfAXIH38g8ApIFShcS2r5A4IVVo8eSNHXN92_y2x8-uQvZxE2zzz06X91I64p-NzCwZytc14aI-LToZkKNE9I8xpBh_gu5UqTFIY9MJL3teAClSCgHj9h70r_w6CwXEFngtoHWKQIJjqkgvcl4rpyM4hHDrvq7ZbFHqC2LxVmEw7eJ4opuhy0OeDzHe90bGwcWf5kjt6bBd4qg6IrViSzBwTDY-XS3RDoKnq4n605gQRB8D5ftq2uQ7GfNKo0AL8_4eEHSyq8jOFH3UkDQjGxr8DB64y_yh6vZp_71m6cUQXW8SWWJJzwKXSe5h6-QNvu2ZQmhWI2ZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که دانش آموز ایرانی استرس کنکور و بمب و موشک رو داره همون لحظه وزیر آموزش پرورش و هیئتش
😵
😵
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70182" target="_blank">📅 12:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70181" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeMKADuLU77vxWfqIBiV91x63tmyvcRNfwg8Ge6vPg25Q_ILyUAG34swpG1l-pK-5s_oj0HjplUUlnVO-64kvxrR_ZFT-whEKFqf9a1FoET-ggqRjhAxzrDEmeo1w0e_PbEg-utGMd1ZzyMAud4lTY6VvNvNSE8OeOcrf3hgqExNFreRu-JCYMZf1q-dcqG25CfC-a-3gT7Ljbj0StnakXzfbEumOGlY84H2sEC3hteRqE93S6LmLxJWD9g32nCYdFPa0axxWBdBiavuGSs82whaw2dvoyg70dn2Qk9DRPQfW3ypZIPxDPxJmJb5YQ0aJt34JORwo2aaO9xoxss2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70180" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=Gl2MDj5nlwVvwKPKyrD6nmIQFskHxp-_94bCV3gxLt-ns0__AetLGa_sWCh6N12WOMwfTzgciOqdDx_AFE2yxKYq-anUanTg69IU23-oRvAiNlxqDlWAGCDyX3FGNmrr02OfbftY9_zDHEKxpi80VLSEf-PCIcTZvpeQgZU7Kw10jamyFN40F7WtcJFkQbxQSrbwga0H1ITeWdJB-u7wbw7GnjRwT9OVCQ4dwCL8tActcFH953KIBKIWvvBx68JcdYUKxU7hZFK4SIn8NgWnD5y3O7dOzyhUPKGDBNyH7uue86x4o_UW99Y1whKMx143D9oSk02WpfdDMVlgpCQ7hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=Gl2MDj5nlwVvwKPKyrD6nmIQFskHxp-_94bCV3gxLt-ns0__AetLGa_sWCh6N12WOMwfTzgciOqdDx_AFE2yxKYq-anUanTg69IU23-oRvAiNlxqDlWAGCDyX3FGNmrr02OfbftY9_zDHEKxpi80VLSEf-PCIcTZvpeQgZU7Kw10jamyFN40F7WtcJFkQbxQSrbwga0H1ITeWdJB-u7wbw7GnjRwT9OVCQ4dwCL8tActcFH953KIBKIWvvBx68JcdYUKxU7hZFK4SIn8NgWnD5y3O7dOzyhUPKGDBNyH7uue86x4o_UW99Y1whKMx143D9oSk02WpfdDMVlgpCQ7hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
کارشناس پدافند هوایی سپاه پاسداران:
«در روزهای نخست جنگ، ۶ تا ۷ فروند پهپاد «هرمس» و «هرون» متعلق به رژیم صهیونیستی به‌طور همزمان بر فراز جنوب لبنان در حال گشت‌زنی بودند.
با هدف قرار گرفتن این پهپادها [توسط ایران]، شمار آن‌ها در جنوب لبنان به تنها یک فروند کاهش یافت و بدین ترتیب، آزادی عمل بیشتری برای انجام عملیات در اختیار حزب‌الله قرار گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70179" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70178">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=WSZe8SMsl2V00PUQ8E1OrXU0fHkn59j9eNNJd-mSuy6R-wtTr2HtDYr7Z7UGS5KMUtlOF7VaG0kkMNqPzo1MTb4Xm745AUT9DHeqCQ5VhZjlHZ-pvkYSGmm3OXhZtkfnGEAKAMCHHIQMMJBH4G8GaJE0HIiD327x6nlSL4-XQW-qki_gJ5UfkZqAvPrh6zBeR5w__6oFLTraZVtajDwG9JFohjpDMFwqRXHwjPUKjotHzKy1Jnn6h4uWNglnpBOMGNTaLQBH2qTC5hlUHDJt9ZoAhXYAM638SXkFvEp7IqpEGt22ppjKTe5knd0ZrAflSxFhGvgJL8ctqQHAAQf_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=WSZe8SMsl2V00PUQ8E1OrXU0fHkn59j9eNNJd-mSuy6R-wtTr2HtDYr7Z7UGS5KMUtlOF7VaG0kkMNqPzo1MTb4Xm745AUT9DHeqCQ5VhZjlHZ-pvkYSGmm3OXhZtkfnGEAKAMCHHIQMMJBH4G8GaJE0HIiD327x6nlSL4-XQW-qki_gJ5UfkZqAvPrh6zBeR5w__6oFLTraZVtajDwG9JFohjpDMFwqRXHwjPUKjotHzKy1Jnn6h4uWNglnpBOMGNTaLQBH2qTC5hlUHDJt9ZoAhXYAM638SXkFvEp7IqpEGt22ppjKTe5knd0ZrAflSxFhGvgJL8ctqQHAAQf_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ممدانی اومده یه ویدیو از خودش منتشر کرده و برای شهروندان چینی نیویورک، با زبان چینی صحبت کرده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70178" target="_blank">📅 11:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70177">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=LwKbyCpfwFvan8SLkrHRt77llZZbTu8Ka2P8CmwZkktg19MdjdSKlOziJ-KB_d-xkUNgF_9FnPw3L2_YiBHZ0Tc8V5nQyE1nI0peBaygWNus-EBVfxwLUqIFrlWMjkOK1xZG_uFzAaBdy29gTalLndCV2tXqoXN3vWm9ScDKK-94bAJvGxrFNZj5rJMlbQY5NVXrcFnfl-kTry-UClwLbrE0M4C7g8CHcpibRh8HDW8BP-ViKt1Mp04QdyQ55Cv9XYqGPC2pdJMW6muAuByfPtdsHFuYv1usn6VDmHkV6fAfZX8UgRSq1OH1sQOovBaFyUARRICIpqnFDRAGWrx4s4k2OSqJWLYxLm9oA7YoGi6sflqE7eQ4u-DwadYMa9h39fKXrEIvWQk6jPk-5q0xhviEIEH6YMcAZ4d9ZMdBMyIfOpS_HgDbnS5UP09eLfacarjKZ-msOZKspivnjGSAaacRuzFkzpXU8Umm_EzTLKYTBFU-BuDjgTLwHgcMrCZiVHmqE27hTOrNhkksII-UOoW5ivpvbvnsL57f1bwz6Bii9jP3A0um0gm39vHi0vKXEYZ01va5nDA3JuILoSLwiW5u7mui03cqbHdvcI_6VXr7dJyYtUyoBkYPa4wXTSfMgnQ16mL4GAqgooGDlMVwUYtlMknvO1z-OySZt8ueIIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=LwKbyCpfwFvan8SLkrHRt77llZZbTu8Ka2P8CmwZkktg19MdjdSKlOziJ-KB_d-xkUNgF_9FnPw3L2_YiBHZ0Tc8V5nQyE1nI0peBaygWNus-EBVfxwLUqIFrlWMjkOK1xZG_uFzAaBdy29gTalLndCV2tXqoXN3vWm9ScDKK-94bAJvGxrFNZj5rJMlbQY5NVXrcFnfl-kTry-UClwLbrE0M4C7g8CHcpibRh8HDW8BP-ViKt1Mp04QdyQ55Cv9XYqGPC2pdJMW6muAuByfPtdsHFuYv1usn6VDmHkV6fAfZX8UgRSq1OH1sQOovBaFyUARRICIpqnFDRAGWrx4s4k2OSqJWLYxLm9oA7YoGi6sflqE7eQ4u-DwadYMa9h39fKXrEIvWQk6jPk-5q0xhviEIEH6YMcAZ4d9ZMdBMyIfOpS_HgDbnS5UP09eLfacarjKZ-msOZKspivnjGSAaacRuzFkzpXU8Umm_EzTLKYTBFU-BuDjgTLwHgcMrCZiVHmqE27hTOrNhkksII-UOoW5ivpvbvnsL57f1bwz6Bii9jP3A0um0gm39vHi0vKXEYZ01va5nDA3JuILoSLwiW5u7mui03cqbHdvcI_6VXr7dJyYtUyoBkYPa4wXTSfMgnQ16mL4GAqgooGDlMVwUYtlMknvO1z-OySZt8ueIIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک شهروند اهل فلسطین:
لعنت بر ایران که ما رو به این روز انداخته
عامل تمامی بدبختی های خاورمیانه و کشور های عربی ایرانه
اونا ما رو تحریک کردن گفتن حمله بکنید
اونا باعث شدن نزدیک دو میلیون نفر اینجا آواره و کشته بشه
کاری با مردم ایران نداریم اونا هم مسلمون هستن ولی حکومتشون خدا لعنت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70177" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp5JmF5qd1_1glut7VPpwJ92EhDqeqrxN7i1-hMP7ppSWia23KAek9_jQDNtSfLNRk-r93Msfp3vjjTAmKmwN3_MAaURGM5vTRe8Sgj9DY02fzJLMhrhaBH3LSyIAdQWbSQao66Ny9Q4dN719QKqsKPKJ1pvB6YbYWlGttp2oB61Vs6JFkzkMZ-EDcBiLdOzuWhhFm_WVpv3DyrJnSQw-glg0HefMeUgejofdDgGY7Unq9iepXbSlSgjvg8UFWRP_NeOcHLSmfrsTjxyX5XmyOUH_JwxDXPBmWb6gvocIh3N1NjAnlxPDSiBVI7GAKYoXDesh5Ms7t8EMat6TDLtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168e601701.mp4?token=ACEog7m6g3YMg6bOyhAgb0a6dhBkHj-AglAJkwQz0Awa8q8gDAxK46g_YWgHvB9ZxTzceZSM2VwkHbrkyNmmmFABAgnLlabwaf2LbbLQ3sudx_wFFUDAoz9mKlTpCQccjdLWXrUq7dYQq6iJd8d43SJ_Ul0Dw9RPdmDFWUc53GEPDR9dqbQU4cAYi5cHc2feKXrIDJNXT6b94ThMnSoLbWwaQmeLgnkfIbLvC2Vw4fTKmHyAC7TND_TEju2klcV641DrKAgpM3COP56G65LUjqGk2qgPBqHsD-0MaCiwCP7uxnvVoY_85QkeO3IedJ2GrtYd7StcVwG_TZerydIefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168e601701.mp4?token=ACEog7m6g3YMg6bOyhAgb0a6dhBkHj-AglAJkwQz0Awa8q8gDAxK46g_YWgHvB9ZxTzceZSM2VwkHbrkyNmmmFABAgnLlabwaf2LbbLQ3sudx_wFFUDAoz9mKlTpCQccjdLWXrUq7dYQq6iJd8d43SJ_Ul0Dw9RPdmDFWUc53GEPDR9dqbQU4cAYi5cHc2feKXrIDJNXT6b94ThMnSoLbWwaQmeLgnkfIbLvC2Vw4fTKmHyAC7TND_TEju2klcV641DrKAgpM3COP56G65LUjqGk2qgPBqHsD-0MaCiwCP7uxnvVoY_85QkeO3IedJ2GrtYd7StcVwG_TZerydIefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بالاخره عکس‌های عروسی رونالدو هم اومد؛ این دو زوج خوشبخت تو همون اتاق نشیمن خونه‌شون تو پرتغال ازدواج کردن.
⏺
جورجینا میگه اونا عمداً اتاق نشیمن خونه‌ رو انتخاب کردن؛ همون جایی که:
صبحونه، ناهار و شام میخورن و زندگی روزمره‌شون رو میگذرونن...
اونا میخوان 30 سال بعد، وقتی بچه‌هاشون به اون میز نگاه میکنن، بگن: "اینجا یه اتفاق فوق‌العاده افتاد؛ مراسم عقدِ پدر و مادرمون."
+اونا تو خونه‌ای ازدواج کردن که تو ماهِ 7اُم سال تحویلش گرفتن و ساختنش هم 7 سال طول کشید.
+تاریخ عروسی هم 11 آگوست، دقیقاً دهمین سالگرد روزی بود که واسه اولین بار همدیگرو توفروشگاه Gucci تو مادرید دیدن، اصلا به همین دلیل هم کل لباس‌هاشون از برند گوچی بود...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70173" target="_blank">📅 10:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
📚
كارت ورود به جلسه آزمون سراسری کنکور ۱۴۰۵-۱۴۰۶ منتشر شد
؛
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت و چاپ کنند
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70172" target="_blank">📅 10:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeQv6TDPPHUQwt7Ex0kvwKvdjLAq27Ls0PzgaRLfIRH_fla7vtradQSrpDj9i1nS8GNp40Ys1p1ULAY9jBH5Ngr0tYL9U5U7ctYe5esxG8-SeXvja8XcR1Xr6S4DqFfEFPFL0tbHNdpRl1Zi9nZtQJNz7GF_x9UW8Bp2KppSFslPv9khRzaSXgvOT-G9b0py5eHQqiM7dgSWOt_1hSIGSwfGxHo06--8fxpEqpRs-7jNkrcBR-jEvm8pSGLCZeQw5cvc2FCyCoTvbBiFoxqSH7WZ-kxQbzcwGJ2IT37H55b3Th-Ty4_ZElnVQswEDzlVGBlCOJDFnIHIQeM4J_a4PUNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeQv6TDPPHUQwt7Ex0kvwKvdjLAq27Ls0PzgaRLfIRH_fla7vtradQSrpDj9i1nS8GNp40Ys1p1ULAY9jBH5Ngr0tYL9U5U7ctYe5esxG8-SeXvja8XcR1Xr6S4DqFfEFPFL0tbHNdpRl1Zi9nZtQJNz7GF_x9UW8Bp2KppSFslPv9khRzaSXgvOT-G9b0py5eHQqiM7dgSWOt_1hSIGSwfGxHo06--8fxpEqpRs-7jNkrcBR-jEvm8pSGLCZeQw5cvc2FCyCoTvbBiFoxqSH7WZ-kxQbzcwGJ2IT37H55b3Th-Ty4_ZElnVQswEDzlVGBlCOJDFnIHIQeM4J_a4PUNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثبت تصویر یکی از مرموزترین و کمیاب‌ترین گربه سانان جهان تو ایران
:
ویدیویی جدید از گربه پالاس تو ایران منتشر شده؛ گربه‌ای فوق‌العاده مخفی‌کار و گوشه‌گیر که دیدنش حتی برای محیط‌بان‌ها هم بشدت نادره.
واقعی بودن ویدیو توسط منابع معتبر تایید شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70171" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=ZLxBmuxzM6UCJjxfd0PE-OITe7JRY7WaFD5VZOw60UgFtHxfurczmKuHzGm8wbFFhi4yIur03FWvRt2SMQm_PLOptzrmuTIIp-KFewb-LRXnS4eX3iZO5xDq8deDwu_6bjGnhgcy-0oMLXIN68RDzstfJeImre0WuMY9x9x2HyrIC82J5nl90uTOV2FshqLzN7sCG1xmwyCBeRBMRmRsbavNQXs3EKuNfpb2bZ5rSmUr1IpD90hqfGbYGw1Im94heTpQ1-ctFaEqthZ_vpLKMAVBhXpiYAaR5rz1IyhoKm-60RNTitgETX2QDbEjA9Q7AYozrtfcfsgT7iPsk7WvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=ZLxBmuxzM6UCJjxfd0PE-OITe7JRY7WaFD5VZOw60UgFtHxfurczmKuHzGm8wbFFhi4yIur03FWvRt2SMQm_PLOptzrmuTIIp-KFewb-LRXnS4eX3iZO5xDq8deDwu_6bjGnhgcy-0oMLXIN68RDzstfJeImre0WuMY9x9x2HyrIC82J5nl90uTOV2FshqLzN7sCG1xmwyCBeRBMRmRsbavNQXs3EKuNfpb2bZ5rSmUr1IpD90hqfGbYGw1Im94heTpQ1-ctFaEqthZ_vpLKMAVBhXpiYAaR5rz1IyhoKm-60RNTitgETX2QDbEjA9Q7AYozrtfcfsgT7iPsk7WvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
آریایی‌نژاد نماینده مجلس:
من تو مناظره ای که داشتم در وصف مرحومه مهسا امینی لفظ نامناسبی بکار بردم از خانواده ایشون و همه منتقدین عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70170" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
نوید محمدزاده که پست حمایتی از فلسطین گذاشت مردم گرفتن روش حالا حمله کرده به مردمی که بهش انتقاد کرده:
قبلا از فلسطین حمایت کردم و الانم کردم و درادامه هم میکنم.
چون اصلا با اسرائیل حال نمیکنم و تا همیشه فن فلسطینم.
ما حکومتی کثیفیم اونوری ها میگن اینوری هام هم میگن وطن فروش
کله ببرید تو زندگیتون.
به بشر یکبار فرصت زندگی دادن چیشد که همه تیم کشی کردن و چرا انقدر باید راحت تهدید کنید ؟
من نه طرف اونوریام نه اینوریام من طرفدار زندگی ام.
میتونستم هرجا که میخواستیم در تاپ‌ترین جا زندگی کنم ولی اینجا موندم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70169" target="_blank">📅 08:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70168" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=doBLlu6Y_wXWnXo3v3IGnZV3rab1HCIm9fX4m6WXs0z2i-S1IBY7LH3d1nLD_2haNzXvjFr4sixNAfm0WQ3AI8pvhhGGDZLamNDBYqKX77ZzTWCNx3MnX56ww1AWDZxBd3TKAdKb7QkWiXnCJKuGvDN5X_j7dqxW6Tt8PKxQbSYhx8YlEbCgkBlzOSvFhieYDunKJIzey8SQHeGpqjDHiMbke1AxE1zgjtgJTlWvlDJMLWCg6MkyzyqEquSCWlceIzdosLnA4NyrPbnxRDVXtuB7oOrPkLH7ppQXoBa7H-afwIMvYI3XR5WVJlnomeFx4gk7UHFakrbJss8kAEO5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=doBLlu6Y_wXWnXo3v3IGnZV3rab1HCIm9fX4m6WXs0z2i-S1IBY7LH3d1nLD_2haNzXvjFr4sixNAfm0WQ3AI8pvhhGGDZLamNDBYqKX77ZzTWCNx3MnX56ww1AWDZxBd3TKAdKb7QkWiXnCJKuGvDN5X_j7dqxW6Tt8PKxQbSYhx8YlEbCgkBlzOSvFhieYDunKJIzey8SQHeGpqjDHiMbke1AxE1zgjtgJTlWvlDJMLWCg6MkyzyqEquSCWlceIzdosLnA4NyrPbnxRDVXtuB7oOrPkLH7ppQXoBa7H-afwIMvYI3XR5WVJlnomeFx4gk7UHFakrbJss8kAEO5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70167" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj6Unvwz4ZlBF8XA_1wt-KFEdVHYz9ShA-0--_RizN_Vh5h4XdN_zbWMzgUOUamd0pHIr7z199tAc8-YNp2KDBJHOtK9qCeAwFYV8Yi-i807cY3LUfX0xM5C90hfHaKc45wRkoI-9YskDoE4HCObbFMte9V4Q5wcN-T1shRLjzsnn8WW3HVO10ra_pMkIwWBebsf1T8KfEpAdNeJiqdMMiPInEPkXEjXJCXXuFNvxm4ETVDwjOBcb8EcbIYncHUscQBSKca6wta2PwJvM0gaIfrJS1XiQ2Unz_JWxIca8t99MLUJ08cPpEoYu87EJrufOEBstAwznDmtjgOqQY1YpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
❌
مارجوری تیلور گرین، نماینده پیشین مجلس آمریکا:
در جلسات راهبردی درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌شود:
بله، درست خواندید.
این واقعیت دارد. من حدس و گمان نمی‌زنم؛ من از این موضوع خبر دارم. و این شرّی مطلق است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70166" target="_blank">📅 01:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paiSvsMgGDXtHThuF9Q09zsHamTlXO9Z3ujwqw64hvvJd2XN-Z9d4odO5a7Z5bIEzI_mDZtqeTnFcdNMgElPCHgXHPnCDf6FrvxTws1RXbpRlgiUFGNxedb7uS0VRnoPdTD2zvsDiHaC4PYmy5rc5H_cbqNC7z7Np13xyLmxu9y_zsnGnHvKtE1l4vkZSFZ70BbJSvVys697GXm-dUOM3jgY7Oh5YeWlqvciqNhdTHeUa7wdVIsNOTHgUw-eHs8b3fsoVwkCRoQvccTVG6HL8Va_EWXc3CLXcf86VuZiupCDjQVSW0vhlBv5yNnot-G1r8Xgk7ToJ4G2xx7MErWPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
ستاد تبلیغات انتخاباتی جدید نتانیاهو:
🔴
مجتبی خامنه‌ای، زهران ممدانی، رجب طیب اردوغان و نعیم قاسم را کنار هم قرار می‌دهد:
«آن‌ها می‌خواهند نتانیاهو شکست بخورد. نگذارید آن‌ها پیروز شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70165" target="_blank">📅 01:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0izbxLxLhRpjlrS9Yr2rWq0ynYn17zZe16uhpX5vdpj3GNyA9GCHD780eQday4YBexES1BLwWKDQe8kaQn2Vj3A0cCASdR1Too_kAPJjUZL1ELYM-dBOXKpgphSFV4ZeaGF854M2vO7chedXdnnr2rLdrjCFYOuZ3-ZH1CjhVCjXRwvFaKrSLCLkn3IF8Ipfe6kCKAxA9s90NlVZt8kW3qsr3rl4vsyCudXnht5jg5YaIUsmecwjrSURrQEcFJjaVJJ3tnrtiUe3Z6UyXQgQj9t_8Nt2x3_phGkQ7E_QHi2GqRg4w12Z68e2wu_7HiNnqLQjZDgfB0TEGAZ7at_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
🇮🇷
#فوری
؛مهلت ۶۰ روزه مذاکرات در چارچوب توافق صلح ایران و آمریکا در اسلام‌آباد به پایان رسید، بدون آنکه توافق نهایی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70164" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
