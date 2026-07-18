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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 165K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 19:15:34</div>
<hr>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDV184eVIkPI6SNjnD2NFpflAbZyPfC7ALcq027gbTNocz6hf_CIE77haylsB7DSyAOZQ-33-TkyD1Utffg3yxQrj9tEmooadiVbEGUNiuvnzyLSa_WQbkC2KAWUDoZFvBjDx6Xk_KlbkYBmNsxtrDfPX2fqVobf6RFWBVi5Us8ffCPfGeo1MAHpgPgsIzeSNcGwpc0nPBF6g0VXIVsIgkoIG-Ud5ZcV3KBSRYSdhRg9MK47Zmn1Nq27yvnjyXwtpJxNZyW3QW3i1lsIITAztOr2SY43ESlUvOF-p70Shk5ZR4-D2N96vZWTmr_NG7X9odR_k67OlVup5x4CmHuZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdXZvt0YFoAcUTb6JfTryZTY7_iTx85LyqBTOqlb51jGRfuZ3QdPoj2p5UD_wMA3sHc3z6mPHlYUB8SlAgTtBU_3FGo0vI_MsZT9Ru7kCHc_ODVFI86mhmJYWqoh7zpUrE2CWHRXRWKCf_WRBmli4it-hTnnUL3NZlTiwQ_34g8fWVaaYOnXmbOuIXnw92NWY3a7LzkoaXFKjAq1GwIJEzefdY42A6izZP2q7cnWFcGnM2ptCBaZ2EmHSchLv2DTKbpZr2I0g9x-Vt4sStnFL4vN-mZvygRn44ZhUvY40EgBdyhHfrcSF4UT8loPDvEicWJCZbPI1q0eUy7KxAVEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH_kZg4aJqLDV1ZOal--A7rXcC1vPUTM9T5VS8i5sR3db7ZkveBCfT1dSBJbMuXR_abNAQVqRWjJILGe-yCnSHTT0oQKgNzgmjEUqWMOYUoTsm2gZZq9Bb4RCrK15XBtWJZT8375SZJVgUFGjQOEcCPMvAuWwN79sKY2LtLI2cNhaHM4yD3T51OySH8yUpXD5sgWIcymlVp9GcuJTj21UDe5QnwNE6INNQVzZSB30Zn9AUzjaCA7RqCID0WBREVKbWqO4Je9UhD5MOJv4rXP4dyswpW7-nV66m2sE6G8-lKX4mFOX-jG2RZgBIpkAJ7y8gfqzeTb8U80pTH703w_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5fxder5xo3R_LS5qV2gv2j9VoaXnmogtYgBOmgNpgl8lvcbzbvyw_4-wk0xuDsC_Pa8_SlAnKYjcLhycrO22nG2lKla2uOALLs3tz1ZP6LeUBrZdqWp2K1ws9AY5auIqGwdScr7ia-sNDfhpeLLqbd662reDgBZ5FDB-X9v-NeRS0OZmTQkf6Rn8MeYP3yVswsDfCyURhCdau1vBL_AMBZvW5VqMo_PLcCo56w147SimLVR6VCPZlNx29_NBV-1sgDih9-y382fJ_6eyByXSIYHlgQADVGJiIxqzF1Hfp0QVKlgZ79D8vlh2hxfLZr2OoDiu2qfT0KFgHdVJqRmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtavAkhN2b_CCSb3_DPpvyzdbOXvGSNZR3wuE3c9C5x7snQs0iBRNqp5-pKxdCD8d4Bn0NCLfD1O88U3LCjDPYEqzMamL-eG7YmmuoY0HgITsbxjaM1KGBV1BkGUpWCOqFHdbpsvGwmT0FIexJp1iNK2F8mWeoDc-xlk2F5AMBQR6VjaQu8w3pRb3SfewBXxQjfdSIq4jPZBxsV2McJCFE7cIx2pyMjLyOaXCrcOoJTiX2YMyR3TU2FQjMOsrk6HEyoDL9px9LmXVrgxdFDYJ4TjYj6OlJlywIEp8CWmUuR1tPS7usOjJ-CXw65Qb9PoKrf8ILgSLuoTakPbT67jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BVlUA8Eam1yHTSz_ICmqDPmEgeNDAuVTbcqU3xLvmMo-rAMwg15KwNGxj0j9zVAkn-D6vh5NRH0Lu84vf7pDNsQwiwcY52lTuihzV5rOfM9Izol8L1rGOSsbmQqtpuH-q9X5eo2Kim62cwNFW08Yf1-tFKSPTKEtwdCvrLB1-CoQXvx4ZEVuSZUDql7WdXiNoHTfoZLxBAXXpuNdYQPHV2ASdP7eBuRsvJLLEAzdlIZILw6BKsq-UalyEoqXd52jTFCcQHrN8QoOsaKvgNhoOgb5FuMTjHrjBZXaOcRttLUy4eAKvcbuu7RCbeW8g8CFHp2xjMm4sfpCx7tl4gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMeNRZMKmdsZb_ExCKl6Z2pgucjKdIrzC23aVd7Lg16ipJiIaZaxsHWfJpHoMiI5r1HTj71c4fddEKV46XKX4_5G8TGRHw0MKS1rbp-B9SmSyk2kvcilc8pZLJMAILJNFmfLC7Dg-p02ZWev8YZtvghFI9YTE2KE0o23DxQ-CiclCaHWpYuGyUvi3ZTMQYtMPM3lSBBkTPTGZgKm2olFKYxy22ZDjVbw0FxDkG8kZu0CNvZBPUQnQXZYVhPp-cEMsrwaDKm4qdl5PWpNX5_nViHd9PO2wDcOFEXH9cPqwNaPNiNnX-W7xEPJIpPcVRBSgsLXQD6Xb5jraEcBDr0mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXlHzIOtycVEuzMaSyfjhTQ_k0vkOM397zePhw6u_lbEw6m_jlTRAiLMkW-D9VTW5GEG1xUnCnowrGUGD2tMzz9STfNzbX42lNPsmMi68hMJKTVIbk6NhNETndSaLzKQXjhbjf6z7ifIIoK__uSrTELnJWfK0ljB9qoIOLGfgDxIWKJcym1Zk8nSpEFTlR43HVfa2EIfmt9zYbo45PCVlqMoTit3RcaJvsG0fLU4e90Sb_vs_005FEDk9SHz9fEh6cYO-LowPT6dJQmSH3nWVmlF8bxRjbJAldcRtheadU8V56BLy0L7tKgOpSO5C5l-f0hGK_0DCIVQTGi--i5SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAHwWZcGQk9bTEPIAfKPO3pOndfQQwHEouwbOs6WPYwahNTkINmELN1cbqQaE7BT8UbCMaAS3wMzWBhNo8rZQjVR3BVuzRNCPNKEuRb7hB0OHc4-lI5_g3NSpLcHRjQqhXnjIuyQpRGwzpQK4z7RTeoOYr0hM91kIHzhLrVH6ugo05QGxZ2mjgDH5Ahw4D1NAPiJS_mOnvHIiNFoliLQmPRBCdX5NIYG50M7LHzlFRGJSdrbV23MK27soloafsPzsgtaPQcL9NMl3nSMC7Gs6lwAova0R-1gvYuxAqyiz0Axqj2GQyWgkp8KTZgxTzO_NaiHZ2ALJCDIRZMp38aBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el8YWblstOLTJChyvfOcg93SjeaCVsL_hZRF93qlInHSjDF0fptgLupC8aPPGy--pvq4yMMNt3TVLZajI_6yt_-wk-NSATPV6TWcYhXswi46Nme-BZADsVxVaJ5XdJmABjXGfI50wRV9gKeYt7j-u2Jb_4utMKk83udfpY1dQdtGJtlvwHNqnPSA2gWHSnWKtjErk3QV5W8ZMiINvrZOj5rv_6AUE6t-7frPqi4hNne08EXa3qIqSu9klgShUCuTGPWNpvurBVXik2LBuRJ3xzUXjbGOOyEmGh2LFyOeILZNsUw640yF2G5gX2vyEz5cXqKxTru8ZTpFDCLKl6zcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4uTcxfBc32O5E4ovfMEV48s-U0QFHiUX6aMXqb2qzTZa_mEeOhYCz_5_XIybc8hwMwHTjH2-1H0ajk6tOXt3Tec2iNxxKxpehJy5L_CZWRNNSHohzfLp8UEVFk3CdZZOOiQ9gOCfoNtRvwbuMant9GigFICOf31d73Y0dAM2yNv6-Ws2VGa5lZGhaCzNXFxXapAAHoAPuc9fQyMi6xZYGEL3IITyyZONuxrV793sFNzD0i9VKDHU8skrau22kuYM8QGFcwiMsyKauyEtiaL1Rk5fd86mekrjAu5TVQH4U_CZYUgCQIiyyTM5D4TCut0Jm-yHgGMZNEPgvUdMUEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyuwIALnLlAX98F-sGSUruOR0pd_SUKcpBWnVvieWuyhZ41saJDTRKF2X8vcERDQ_6jSGRaUVEJcGiKgcCFKmwp4nEIYIeAg-jUb-2xu70Lr8vdvUs7FEHluGzpd7iP90yrSlp-tMqQIJeXfU3zYspne5JfQ6esjCk5xVqp1es3Ilu1kN-dwC3Ez7_ypYhBaLcyw8G5sA03UfHjvCLbrAaJfrZ8CdKcNepsEtInQ_dek1bdxRYIxUL9NS94hNzRgVdsH6nzKllnD3GmXG5jFgG0C5F768t4YBFhxCfS3KvfHvGp2yD9UB8NCSomR8Sn6vCoETbzEIWPsLnWiASh3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfd_Q6YNJP1grjpJv5GKYLKv2JcpWdEfV1g-3V7WNoatHRXzM8PF6IsVM3OYuTbgzNHVbD-eKE3FcTDZCAN-DLM1_bN0g7HCeLPraSarEtyRdiVLlCVptpqAtzV4dBamRp9T4LG2XmS7bJN6erHaxbWt2EeoZcczktfqUrqibUGoJysfYqS6tB299qXg8UpcOL53MOf71XeH_E1Qy1IZNZOrSlnJN_CW65AMCqxvq2MeBeKpWPm46CuBzSdj-uXYOCVbjs9z997NmcmPoCD1KUDhw-7rEAoiPU1ky35lCxnN_24AMn6nHj8SySwgnHeDQ8DZEkKPKgn48-dUPWewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld_XHD-1Tx6e-hHC2j1Wn4orUZ2s2nX3uzqOkzLTu7gac-AZC1wbuhCbpMiNYgeWG2f_gKP5v9bqsx_iHg9Vb6i16L9iNEjQnr68-lAB6IlxbaNekjNdD7Zwe_kchic7zdUqKHf5k-p-JS5EBI0O25MVD9jTQneQQcEz31gZ2i8Rtm9DvKeaJsJaMe5iwWzF0_xaoN-wAD-lCMmlQ0_7O0cQ6LiTf8kUcjCsV86qZodepeXLLHy6HMJV_JPmxQ1qEmTpdWpLNBXstkto7Puyo9GbwlQsPHsLKfkF44e6vhgqugjyTdyNZaDsbsOKhqhXCeHAHr4slDXtH2YJhXeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM-LWNTjnmcyuKiYgL5dsoS4G-ezxUb2ZLdLJk-UR5GEP2PWjbVRMnEKk5zuvCfulzlh-3xWBhi6eRS495rLoJEUUQb8kHDOEG9fXF4l59RkpNvvI8q95Ya-tmpo8ZU2wR8RvAztmFYmglnTDZpgrpg4uy0wRI4eDSsPL1rx6w5Lw3s6wFidrT5I3iUOM0Hjmaf3X3iqI9A-tXbegRRpF5KCoASuwgZqOr4BldazmQaLDSQDPP8AU-O4pWClKgTIkjMxU_Pkg2PJlPNeRw7TLerShNKE5ziFP99Nv2IyKZjrpl_OBQYp-re-eQ1HuNZoS9gOs699yISU9uC7EWXxsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=Cwlekyd4fB_4Khk2s7RxZSAr2KFbeURQO4SSTQLOSrlsBH717N7t81pt3F1J-SCDIl1MA4i_-4le8HFPyaTdk4lMjnOmDNfUNIMXj-TibW4DvyZcoJJip89XqVIzN2y0DYKpGA0_LoSrUVVL5xFbz1qPIbnezDqKxRLxRnJcV_ndvyuCxOT3W1Vkd4XnmoPgspO6qTMqcZaHAyuC-DqWCxgbhrF3zEEa6Rrt_U0VgpJlYwie7Zlb3FjjDzWl0NlLkRA_nKJSDxCUS4sZwPnESJTbqle17YD35ThC2TDJCACUoGhz4d6r-uHD83cEDI6zJpg8hObWf2-K2Tm3ohJdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=Cwlekyd4fB_4Khk2s7RxZSAr2KFbeURQO4SSTQLOSrlsBH717N7t81pt3F1J-SCDIl1MA4i_-4le8HFPyaTdk4lMjnOmDNfUNIMXj-TibW4DvyZcoJJip89XqVIzN2y0DYKpGA0_LoSrUVVL5xFbz1qPIbnezDqKxRLxRnJcV_ndvyuCxOT3W1Vkd4XnmoPgspO6qTMqcZaHAyuC-DqWCxgbhrF3zEEa6Rrt_U0VgpJlYwie7Zlb3FjjDzWl0NlLkRA_nKJSDxCUS4sZwPnESJTbqle17YD35ThC2TDJCACUoGhz4d6r-uHD83cEDI6zJpg8hObWf2-K2Tm3ohJdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUYtBvOfJ6oGNNVAh6ky6lH_RiRM_H6ziwcNYvlL7pPaAShJgc--Ea033F2tgfHgyiU2DJiXFEI5MMTTFYz_tDu1305_Ykj27zXggYfC4gogCVDePovfz0WwDb_ObbJKYuq1n_MmQCO8_KHvvyZDUGlaq94o92S0JXbIyhejFtWkGtKPu_O788-LI6DcLDub5V24Cl1re45ELUhdqohs8rA5sFcWExIphWnGJu4kCURNtBKF6n5-aoawWzw4oBq8daHniOYZfZ3zSUQ7ANFyNNaOjvd_6foTulu23t21P5TFpr0o35HNp3YqD80BvQuV6QLMbbsxMKjJjqvw262M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukc5xY3X8N-Igxm38ElgksZJQTh6xWI40ghjgxMxxAo_1lWFuoOQTIkk0hgdfOikD-T9y8EwdH4Jlw9i4JqXgLgghsilwOpdcB2OyZyhYMgPl02qYNvL1B7ZBK0LLAB97ZAL2N40dzjx3KEbUa21a7CkbU6Q8C0K4Q7oG8libZTwlH13JYRlD6kafFqmy-x2iYLQulV032GAqGOlZnrbXfTkMP99mDq_fYMuhGTuhvpjJayDaDUw_XS0UCGqDAl1AQlNI3NKk9VkeXb1cTSgTsvn_HbOb0D2PThyhQgv0aGgMUTz6Dul6-hPJceL2oLJHWLXC9xLzRxasUvfIgwpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNw9CcZIWh5_KdQ1b5BKMYG7AEiyjuXAO428TQJUmM4KJqv53dF5MCBs5DJDmTy0uaLRwHVQY1qrwoylCD0letT1uOWPzWWGFXQT4hgEQOASLyYFO6qzIuPFByYqZMJCUBpxXFhPIDM2M2ttzPjjf6yR9pghuZ1QbYP-fAuROfZ4JG7NB7QJIcua-7peFZfbVzDgtjOpuEuHXR_pRNVyglgwfhqP3Ww8qsgyxhtcDFqWS_aDJXQnrjZrC-rJZKue4BUq3-NaC17H3hCIfzcJpkPuoAgD8-kENZu3lrbJ2raNG1OT6CkcFkZGgwSYKLa1A94Dl5vjOmfLybY9aE1x-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXMXEEVbf-OM1pbIxoFchx43DhbRVWuclZ5K6h4eKamuZDNA5e_GLyrS8rJxpLzKexK5F3r2PtscYchCZGlV1cQ8TIGyFfuZwBjjV_BurstCT-26Cb0F9C2ZLnD9sxXKKDl2fJMdYlZ66zBAuI831xTAdJUtXnUAHHwJUxoCeMe4py_6fDomlka0lgzlcHpITHpDO37tvkftlCETZxVFr2xyW77j9bASnUx3j8aJUEMmmLT0l52lDmetOUjQd9JPiFaypZ_TJDLNt32VByclL1GLIU3eU-WxSrt3hv-28pXSsHEqWXuRc1hJmYlGoXTgJdyJRX8JvT3-yP4ivywDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAg_heRiA2-kcg-7OnD8cxS0YJsXkFQcfSXUQZG-xMcIwKW5AslVklVPEYLMlhACYTttwe5bBlYegYOg6BRO4I-K0niSC8ZK5V08l1enkxOEeg5CFBe19PhfkaXUduIJGPq_5J40a0_4eCbzDNxn0IdGpRCQE6t2od5Rov0jLZ5MVwyy70tzK43Q7M2MyZGnlaZpf2OAFqikxWaiHHNwaXhlfn7Tr3aBBI0cEPoGoH5I76pBDucRYKQBCiON1Zsr182FdkHNmNZGrEH9bQThFPak4Wd82nqcE9dfQqUdflBU14DQWVnVWIf63mUtKctZcMLzcbbMpLhHTI4zX6YVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=S3piqNxIN0GsIx0vmZtDaFfL_r02GPBiEI0rRHN7uE1TEzTS21J-kVigEU-iFas9dUefREhNuVyqbS7jmDdteXCkZg4earcDpKBk_z4Gq_jma7BavkeAqU2mimwJx7K27Tooavz7jdHs8wzWOkEpjgWGlsOfThGhwsyTfhJJPTA_T1vACgNzQTFh4-Do1wDmhwK-U5f1SZN1trGg6oS54atKVeHpk74V7DhTAfRkFEbsKmfvz3r_Bhy9mFiMMGqtY7CpKmxnSurZh4il6Y8jghVJfPa8wIJUPkpgoGfN7Rk-nDj4oItHvehi7TQWBMPbNozG1iSjuGpjZQJqVJFCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=S3piqNxIN0GsIx0vmZtDaFfL_r02GPBiEI0rRHN7uE1TEzTS21J-kVigEU-iFas9dUefREhNuVyqbS7jmDdteXCkZg4earcDpKBk_z4Gq_jma7BavkeAqU2mimwJx7K27Tooavz7jdHs8wzWOkEpjgWGlsOfThGhwsyTfhJJPTA_T1vACgNzQTFh4-Do1wDmhwK-U5f1SZN1trGg6oS54atKVeHpk74V7DhTAfRkFEbsKmfvz3r_Bhy9mFiMMGqtY7CpKmxnSurZh4il6Y8jghVJfPa8wIJUPkpgoGfN7Rk-nDj4oItHvehi7TQWBMPbNozG1iSjuGpjZQJqVJFCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm6DqqBK62HFx7O-2vs8SP43a0X1MJUswm5x06PjROvMCZl403dxqofmVcC73oDpgZnZUP_mPW3jUoARSlU-PlIXRvdnfXZ9X-2nSYddpmbIQQ7hZdUiqedzz_jrfu7-0No1GQ591OIhZCfJ5S_F5Jw-1puE7z4hrhQLfjMFX36540nm7a8GzEKDct6g3ThtUMe-eYYC4CTZ-vXQcQHpePyggxKAwSwDghJu-rzaYuZTSBgKotpCVmOpsnnPifhHuPSJhnZQSeECAM1IQIal3QdACEqtCe2A62wTVzYLxeOTT-oW1z7kpufjXu_fBB25tlXOragKdYPdLXvBW4rtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXVUaIGRgTUAKjY3Nm10_hLCHDt78wtfsryd02P2kAHLBrn2r376ZEo-O04k6Xss0q_Fzx4db7z_iAUArcxf-UqlZBO6OCaKkI8zz91LQkMjZ1FiwIg4ynTEbkPRPCoFNfPg92Yr1WFIIXBpePkWEYkQPRV9npb7vihAk5iumElw7SS53WgRY59Jil_4bwWf25uJoqQxn7V4p5MA_2DSwIQD9VTdrzB8p3ciDCJIVj4qzcoA1KIozBHah8_iKEJYZHnO186c95jjCsMkqXVMIN5-xavtUokrWfUsD23n_PzNh4SVswb0MFbJyV8-oELey-4y-0Zd5DjcwtX2c07gJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_Oke44SkxVR7zhxWQ9nzYmljvHqa02w_HO32B6W0hTY6jlam0qDFY-lwMBqbHYNMA54ixgUrncxFRe1ZwRwBhaXbOBNzxkA_4WedG2VcgM3PnQhVhkqfH2msmVsXBFp2fTBLbC4-FdDtkx8VUe1aDSmaduAbgUZhz-659oRM_ucy0qp0-m7s76QSgagmPplDzXpU8SnTdA08jEeJKtVahpwr7OkdnMARnH1F3Ffk7vnC0jaBN8A2FE1785AIb-qkEDmHKmXvdmf5ctdqKyCZkPfZoZrb6ZeJwuwti3dYVrCteXo4mD5sRUIgnEdOqbpHzcr2mpI00OE2Oj9JdO5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8b1lCaUGTi_ZuTsFwIAbCH9IsIJFUCDncwr0ACkWMnxpP_7AEigzciwjES8n2r5JqZcvIqWh6vhFp_usO7OIhs8NZIwLX-KHLv29X_nCsVoNbfYHBgfkoxd07W47pOR0hBwb4CMgu_Yrvivo2fN2u16Mj4AjFr1uIRpubvaB4gWSho7h0P3pd4KEpRtRocKrNOfGzCsPC2PMwBi5YZWZCR40oYRkDgTikgRtDXxFhvDsyXpSuOSHp64jKE1CIlaucafRZi59AgB9-oEMn01rcXeJ1I5UGR5yn2wPnsW3TSFpIBpEX4oMoFr7QNR7BOzwC619l_sRm8PJizwEeDhWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=IYnT1GYkeKIZgoYvHCI8w2BYbEfAw647PHE1e0qajUhdABRf0oxjXrDct424OgPuHi3eybHkWFstNpcahHjVGYbU35DvX7bCjbbwi_kfYjHSKF3hD_Il47grMo-cJt695i_6d1qSL01OCv4QnHsWLrBjprXVfZhxB--sQTfy7JiyR5ZIS1qwtSpRSL8JPwbwGRfB4683bO7towmXu9dIOFGRJECOKCEje53GjDUBAzM7ygy8m6pDpEQ5qeB61mIqS3X9X86lxYpKPlgmVxffK4odFx6qm5G3ENEwzVq6lrNcjvmZBL_IOxBbCOJVT8HcCz3AEFutRDUbsPP5QXnldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=IYnT1GYkeKIZgoYvHCI8w2BYbEfAw647PHE1e0qajUhdABRf0oxjXrDct424OgPuHi3eybHkWFstNpcahHjVGYbU35DvX7bCjbbwi_kfYjHSKF3hD_Il47grMo-cJt695i_6d1qSL01OCv4QnHsWLrBjprXVfZhxB--sQTfy7JiyR5ZIS1qwtSpRSL8JPwbwGRfB4683bO7towmXu9dIOFGRJECOKCEje53GjDUBAzM7ygy8m6pDpEQ5qeB61mIqS3X9X86lxYpKPlgmVxffK4odFx6qm5G3ENEwzVq6lrNcjvmZBL_IOxBbCOJVT8HcCz3AEFutRDUbsPP5QXnldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMXZrwO5EFJ6xMF9Yt6wj2Aiymn2I1UuHDrft6F-g7Tlc-AnTXQC1lmjGv63rVuMY_sPGh0tp1uOetQNeRx-QtfzHuGcw8U6kPy3KOgYu5jMR4PtHLgukiAY1oBEdTxTZFIm8UNS3Tx6RIWlWztNHUHeShfRyH_qO_LmSxACBegOdPFmqwpORW5QqWgDeUmWWAzSAEt2_RysFqMtFhaJmzHFsfSLq4bseN_nBt7Dxnrn5bJeNAut_wGT5Vl77HyXk9C3e8ng8IJBa2bJ-1CfodJtJqCVhC0wqlwR8gJvQU2VU49jgAxgZk33RwvZx8IUMH-S3ft3C2a5dx5eMbf_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=kVal2SYZnR-d4H9v2EYlOCEpZkvP8TIMLQWb6CeYLu2iho00Q_Fy2OQuf6QcSxtAGyrKvrg9-8JLdGNdK3pCH0z6YKi7mOA4W2OKA-D39YVW2BLi4DxYASFP1BT0md_I7WBS1FzmfZtgxkH6QCrXCrscLCgmJs9UA9btJScGQNU2bWcFUSqWL-Qi6gKu9M15gcVA5qoWn7lKQKgzqtAwXTothKas61s95LwHHhuUyyR5c6P2DvvDrhImMwsOLaAjc2aDhOZrLx5Iu8PtG8y53c9Dftvbnn9Hf4YtWv-E_u9uB5qHRZmv3SQ19uLvJ8gGJxp-IjxmQ51mLsx6VFbSfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=kVal2SYZnR-d4H9v2EYlOCEpZkvP8TIMLQWb6CeYLu2iho00Q_Fy2OQuf6QcSxtAGyrKvrg9-8JLdGNdK3pCH0z6YKi7mOA4W2OKA-D39YVW2BLi4DxYASFP1BT0md_I7WBS1FzmfZtgxkH6QCrXCrscLCgmJs9UA9btJScGQNU2bWcFUSqWL-Qi6gKu9M15gcVA5qoWn7lKQKgzqtAwXTothKas61s95LwHHhuUyyR5c6P2DvvDrhImMwsOLaAjc2aDhOZrLx5Iu8PtG8y53c9Dftvbnn9Hf4YtWv-E_u9uB5qHRZmv3SQ19uLvJ8gGJxp-IjxmQ51mLsx6VFbSfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=UaAJMOsDOyNSGXwDgX1HbOYHWabE5W5kMPorh_YBveX1XtMyt_eqy1j3i7my-kNQ6T361CCMTYG6ki9KTxFHjVmiy1IpDxdAxFKPEaZNlM_1BoKmo_5a61JcTvJ6WqKlo_IkyeOJill23ECpQ40z-w2xghQPCO4yWTcDhNcbku4wrRkr2-h0GO9gJJA3kOpqBz9FJWtViwNW48c7VY-TBzzQvkScetIc57XBEo58QfOgqoMwIqXESRAPpavuS8aEkgOsFqHbnJd4p3W9gacgeWoczN3UfNBBdCYb1yHVeA3H2dy9EdmxzBiWNRn2P4T-GZQVNATr5jvI5XSHRu9KcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=UaAJMOsDOyNSGXwDgX1HbOYHWabE5W5kMPorh_YBveX1XtMyt_eqy1j3i7my-kNQ6T361CCMTYG6ki9KTxFHjVmiy1IpDxdAxFKPEaZNlM_1BoKmo_5a61JcTvJ6WqKlo_IkyeOJill23ECpQ40z-w2xghQPCO4yWTcDhNcbku4wrRkr2-h0GO9gJJA3kOpqBz9FJWtViwNW48c7VY-TBzzQvkScetIc57XBEo58QfOgqoMwIqXESRAPpavuS8aEkgOsFqHbnJd4p3W9gacgeWoczN3UfNBBdCYb1yHVeA3H2dy9EdmxzBiWNRn2P4T-GZQVNATr5jvI5XSHRu9KcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=TW1hicQmPz5tR0fWRQWY6jtrFMnY1b_RtnIKKl1jAApxzKet8p-nNgbmbBxd1mCZZ5mbv862O74HtqabLwGM-FqX493bMQs5YaW7lNXQMebbKIpjNAY0paFcimmhQmI3yHCOHg9Uskot74ZS8Uoqm5pplYOQnOQAxCM4iv74xmM4n_nOz_ulJu5YAstOTg2xKzyIOBIGkwuRmuMVWNJqdXJzqTGIqes0Wupu7AU2jnVOwn1ZjLr8TlMGVJwa_QydT82JxcL6F9a1fCBXpmsKeasRP89g1reZX9jiYlgrKnTgMhfD-ukCetVucOiUumwP0afCO-mSUk9xoat0gDlaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=TW1hicQmPz5tR0fWRQWY6jtrFMnY1b_RtnIKKl1jAApxzKet8p-nNgbmbBxd1mCZZ5mbv862O74HtqabLwGM-FqX493bMQs5YaW7lNXQMebbKIpjNAY0paFcimmhQmI3yHCOHg9Uskot74ZS8Uoqm5pplYOQnOQAxCM4iv74xmM4n_nOz_ulJu5YAstOTg2xKzyIOBIGkwuRmuMVWNJqdXJzqTGIqes0Wupu7AU2jnVOwn1ZjLr8TlMGVJwa_QydT82JxcL6F9a1fCBXpmsKeasRP89g1reZX9jiYlgrKnTgMhfD-ukCetVucOiUumwP0afCO-mSUk9xoat0gDlaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=DtSU7KHwiKTZm6NWGUrNA-AzaT059M1wF4XZCEWlwM8cppm-F18IKTH6Jx6Rny-7cYTCPtJlBA_tk7CaorWHQjG3oHjFtyFdAaGiEiSAlZnrZd-Vk1Qmz4uLLNyEXBhJvejuFIeZQFNwsu2cz8UFYD_68pu2Ty4DkNLyUnVgv7JHD1oE0QUhJIzRKFX-PQy-zFeLH-Axi3Xs9OxOTNO6oOYOTdKN4N0saat8YwhMCVqV5D9jYgu27yvS2lFaBPrtadBdcUiYNFp0kocw40urVQ9_eUsL3oGDnKkH_jaljOCKYuilnWM52UuClwEmn0UJlPRowGrcZwxw9HyIxriARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=DtSU7KHwiKTZm6NWGUrNA-AzaT059M1wF4XZCEWlwM8cppm-F18IKTH6Jx6Rny-7cYTCPtJlBA_tk7CaorWHQjG3oHjFtyFdAaGiEiSAlZnrZd-Vk1Qmz4uLLNyEXBhJvejuFIeZQFNwsu2cz8UFYD_68pu2Ty4DkNLyUnVgv7JHD1oE0QUhJIzRKFX-PQy-zFeLH-Axi3Xs9OxOTNO6oOYOTdKN4N0saat8YwhMCVqV5D9jYgu27yvS2lFaBPrtadBdcUiYNFp0kocw40urVQ9_eUsL3oGDnKkH_jaljOCKYuilnWM52UuClwEmn0UJlPRowGrcZwxw9HyIxriARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=bnwS0pTdIWqtIH95KGWUf5bAFCP8ZsmNp7okN5L7pIp7BeFuu1IBce-Mzvw0dFeWS-6-HZki1367KBrYBwEo-VCR2XcGdJzvXU8aLPUuGW4jv9WvwG0RzLMJYCJInjQAbt82lpIsxgyPxZ62ViOu7lhkcag0j5_CiAf5FSfU9RjxVJZRX3UuqWMnfNprvPvO5GZ85OPNPpxyk8gow-hPXq5pemTKGf3W6K5Pjw_PK5XsMI1LQaajnYm51IqCvP1RYr6n_avY1tC-c6n1zagKO4RTdcYBxW1n3VxhXnJUeU_8tC-G-0w4JpIZkkis5QiGZ-7gJy7R4qImOwv0tOuQhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=bnwS0pTdIWqtIH95KGWUf5bAFCP8ZsmNp7okN5L7pIp7BeFuu1IBce-Mzvw0dFeWS-6-HZki1367KBrYBwEo-VCR2XcGdJzvXU8aLPUuGW4jv9WvwG0RzLMJYCJInjQAbt82lpIsxgyPxZ62ViOu7lhkcag0j5_CiAf5FSfU9RjxVJZRX3UuqWMnfNprvPvO5GZ85OPNPpxyk8gow-hPXq5pemTKGf3W6K5Pjw_PK5XsMI1LQaajnYm51IqCvP1RYr6n_avY1tC-c6n1zagKO4RTdcYBxW1n3VxhXnJUeU_8tC-G-0w4JpIZkkis5QiGZ-7gJy7R4qImOwv0tOuQhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=OLquMeR8od0wispM3GkTBQihXoR10i946idA6kWJEFc8iu38G2aMBy-9OMZe6v_kq8kBhEB-511a6eosD-lpUE8QtsbT7KHWZoAn6En2ls5TxKhTyiVKd_cHe7A8CHf82Iyyg5URRzuqQ3K941J4Y1NRRGefAyzqtPpKy_BnfesNSHwEw3A05A8OYviUZ0ygPTH1uex2Ai_YL-BQNsWwkVfjBaMQsRoB9MkSjFnf7DdxHF9uhrVxbBr6ISn1JvZhnpidqOyT90VJ6S0tnqTcH7mSRyT84GEq99j6-UCBH-G4HZMpOHHAWqBB4vKr4PgR5BejjJDeI95QSo-P64HUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=OLquMeR8od0wispM3GkTBQihXoR10i946idA6kWJEFc8iu38G2aMBy-9OMZe6v_kq8kBhEB-511a6eosD-lpUE8QtsbT7KHWZoAn6En2ls5TxKhTyiVKd_cHe7A8CHf82Iyyg5URRzuqQ3K941J4Y1NRRGefAyzqtPpKy_BnfesNSHwEw3A05A8OYviUZ0ygPTH1uex2Ai_YL-BQNsWwkVfjBaMQsRoB9MkSjFnf7DdxHF9uhrVxbBr6ISn1JvZhnpidqOyT90VJ6S0tnqTcH7mSRyT84GEq99j6-UCBH-G4HZMpOHHAWqBB4vKr4PgR5BejjJDeI95QSo-P64HUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=kLnh2RREgzFu3GoChbcv9mpgmb0d7NTrLGuY-vdKSbirwbUTfMnlRL_Q3ULve8HHeyti_z8YKFJqf_VLUaIZpsm0QdiIeuN_1qE6KmQacDfdW7Lm0r3OrjuXZxqKxcGjDEByfyMLJYnxenRhSPjbey8MMCFo-YkGfGidk8srEIgFKw25jhzE758iA0v-dmuchXq1wtJ9X5PH-OoEFS5JqIMsOSk6usnuRoMPMX1yKutVavKQkh0Pq-ULLTL8KMNMzXmla9mFY-aMnXfojuh2IaaSvbRcOEiYhMTQPjs7y5AZQm9ste-S-gFZBEdbZQMkEE1Yhx_xvEMAK-ZUIpTczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=kLnh2RREgzFu3GoChbcv9mpgmb0d7NTrLGuY-vdKSbirwbUTfMnlRL_Q3ULve8HHeyti_z8YKFJqf_VLUaIZpsm0QdiIeuN_1qE6KmQacDfdW7Lm0r3OrjuXZxqKxcGjDEByfyMLJYnxenRhSPjbey8MMCFo-YkGfGidk8srEIgFKw25jhzE758iA0v-dmuchXq1wtJ9X5PH-OoEFS5JqIMsOSk6usnuRoMPMX1yKutVavKQkh0Pq-ULLTL8KMNMzXmla9mFY-aMnXfojuh2IaaSvbRcOEiYhMTQPjs7y5AZQm9ste-S-gFZBEdbZQMkEE1Yhx_xvEMAK-ZUIpTczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCVzXM6MIhjNj38j1TnhRzvaUs2ROELQP7aQWhtRWgKfK8SPH8Ll8CNgfOJqHVHAPOHN4Evmr5iKjx_bNlofGKFzE3FAOuJQx5EvWmpXm7tJJTeuf7y2crorLcktMUsPfcorKMaK3OJOqOlXL4r0fLjJXAYKDgMwBHkW9QgYtc5oiC-bKsj6tQ7Wh0zK3LDVXRJNIjU5yK-bPiFhZm4CjJKorQdIPFmEnuAKY1UgeQd0ZQm2sWYZ9StXxpGasQ7FP7gfPyfiX6YAE7XRYU7e0ksfVLW-WJ0RTxeWpnstxBn5Mz2hgdDDJtjsFAC5N66bDYx0sydLl0aj0CgPEu4edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzUptIhnLlz2Fp-Xw2mLFJOSky58WYnm1Yp8Z9lCGil5MSTuss5fbt0hwqFVCkAxpCPRjiafcj6juqK5mSgDm3xMDkF7wvw8wf1FQoTSv_X1u0FjQzNVka-k71NH7czTt1BklBZTwl-KdUdZ2-TkZ5WGxpfHxdLR8XT1gG23zt2lJ1h0GEpxG83k3gE7EA25ZI8Q-Vbw9QImHNf51htRpaJvKrITUzle815NY8RIiKMMVNY5X7faxjAcZ-9u8-YbzbaN-7yfZyQFGoFs1vgkfHUylYtHdsjSqOqREZBFvt_nZNpBR2ubEXV7maUbTTZpttK8Niur2Meykmj7bX3tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfZdXMk5y2yGWfND_63bzFFYfDF2oamFb6_xiNAjFGuLa9TJv60mlWmagoo9zlqyASULUyMORFVB-TunGrt_eJQ-4KSMOjSaAkmaL3PtC7wm7dfmhll7LGq91OTF5eOJyFlR5XG7VOsksp24BCQQ97Sb8hBPCityH59ICLwHPnyHaBhAwpCBxv_TSJGZo3x1azFMufWK1J20voJ0VM3eN-PPmGf1vFISBTPNg2FeoRfYJGTlaWT5rajuMmQk4o7iNSJQRQPl-_VxGJFiJwhjSUxB05fQ9Njk40Tl06NmNYCuBxT3DNm1NNLWHi68mGZRydgdEpEoklSiuUezb7uYtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=ZByFqY1Ynh8iE6wKjLWG7wA5HsBPvAuVCEWB2u_0vkUBt04cwT7PONWiRrQRS8LF4_Im2u1GXADItc0YzxWkshyz2YjYUEfINiaWia_2DejsCSx_ftjJM2Nh5tTYALDnt9kqhfvhiSjtPr7_bNbYv6BI3b9dc082CCxk6VUe5d8WtViCTCWB_Hglf5IeaLTcfxGxxPRW1ipWxcMteOTerfpwzirQfeH4KheDnoqCvuy_FP9Jzm0AR8heyKurPVshniXTmrk9R00kWlBMjAyePUZ4wzgh3Buzr_MZ9JWPazuq9EX9qlyJ2_i_8cWecHmFa8blSO-W8vdP9KGhFExMZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=ZByFqY1Ynh8iE6wKjLWG7wA5HsBPvAuVCEWB2u_0vkUBt04cwT7PONWiRrQRS8LF4_Im2u1GXADItc0YzxWkshyz2YjYUEfINiaWia_2DejsCSx_ftjJM2Nh5tTYALDnt9kqhfvhiSjtPr7_bNbYv6BI3b9dc082CCxk6VUe5d8WtViCTCWB_Hglf5IeaLTcfxGxxPRW1ipWxcMteOTerfpwzirQfeH4KheDnoqCvuy_FP9Jzm0AR8heyKurPVshniXTmrk9R00kWlBMjAyePUZ4wzgh3Buzr_MZ9JWPazuq9EX9qlyJ2_i_8cWecHmFa8blSO-W8vdP9KGhFExMZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=v_6aCuQtihK86nNZZ7f5vA1HJyNyShmIaMtEovaYUHaId0FPR9Hkdoc9roF3ug2b4uNEBl0hEoUPEZ_72M0ZALvz2iRM4SEux1zneyBXH9NafpZP7t2wsZTznZJ-Yjea3IAxboHxjss97vh8mLCmtahKwkixwzZU12Qe1RdDnMA3V3620TVB0bUseF5ajJFTdkwsO_IgTJ286xrYu84S_bOrrHKPhUh07HQQs_D8IFsNgVwObZdUn8i-_yfeuVSME4okK1zDejFCMgT9UOEyJpv3p4KBu4sz-zkJWn_IXq_tEXP-jx4EHJkLZilZ7rikoYVHAjFyYubI_KRcqnRVikUY-ocrMZRKK-0A_OfAtsFhKscBYJLP_GSdFDOy6uMMjGs0QbQjRcoRveLzzrt7HFFdXC-x-MAkbHV6kagp6mT5czjyrnmNexiVVnuLSx9jfOCjQ8GPhzo3Z0tIOyDBhLkge3tgf9Sz9AR9gNm--Wv8L39vGP4L8kUxxjNFfVmU-82hR5gMiqnOFV9Ae7eD1ONsHx2_A9e4E_NG_w1gCqw3jfLEQ8J8ZOZ7ERZz8c557B_i1kwtlTaI-jDRFKaD1FGVMX-1DzZgY3G6JpC2-BbHcSwqc36q0tNk5nESZsTRoAsHwYJ8ZMBmlwxFJccycv8VKV1np7eTIRordluGD64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=v_6aCuQtihK86nNZZ7f5vA1HJyNyShmIaMtEovaYUHaId0FPR9Hkdoc9roF3ug2b4uNEBl0hEoUPEZ_72M0ZALvz2iRM4SEux1zneyBXH9NafpZP7t2wsZTznZJ-Yjea3IAxboHxjss97vh8mLCmtahKwkixwzZU12Qe1RdDnMA3V3620TVB0bUseF5ajJFTdkwsO_IgTJ286xrYu84S_bOrrHKPhUh07HQQs_D8IFsNgVwObZdUn8i-_yfeuVSME4okK1zDejFCMgT9UOEyJpv3p4KBu4sz-zkJWn_IXq_tEXP-jx4EHJkLZilZ7rikoYVHAjFyYubI_KRcqnRVikUY-ocrMZRKK-0A_OfAtsFhKscBYJLP_GSdFDOy6uMMjGs0QbQjRcoRveLzzrt7HFFdXC-x-MAkbHV6kagp6mT5czjyrnmNexiVVnuLSx9jfOCjQ8GPhzo3Z0tIOyDBhLkge3tgf9Sz9AR9gNm--Wv8L39vGP4L8kUxxjNFfVmU-82hR5gMiqnOFV9Ae7eD1ONsHx2_A9e4E_NG_w1gCqw3jfLEQ8J8ZOZ7ERZz8c557B_i1kwtlTaI-jDRFKaD1FGVMX-1DzZgY3G6JpC2-BbHcSwqc36q0tNk5nESZsTRoAsHwYJ8ZMBmlwxFJccycv8VKV1np7eTIRordluGD64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=OxSgz2cp6b02BY35lhMsfnCHpA-q2xbUkIz7oLb3VFhj668srIJOqM8LF-inhiqvRFnDRpGyKMKVyop574-uApWmSovsWGehO_9o-6M7X48vW3VzFzJ15GFvQTJup9CNCNF-Ovg7Gw8D75wN8v5Xa4o21K-x2CVl2l0nMYmWvUkKM39on--pA65DlYNVNR5mKuenl6-1cF6RGv0ncp2sTQ5aVkOhHkTZLUGa7zI20OuuBESe0S0ZbOMBFfIJV8PGnPNPGDL4sf8-vBlsjckLUON0kPGeJw7iBMLOrcFCAwKCL4-Ygvk6d1Lzpg5OEADOBrlH8dunXQz9b0JqNPwk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=OxSgz2cp6b02BY35lhMsfnCHpA-q2xbUkIz7oLb3VFhj668srIJOqM8LF-inhiqvRFnDRpGyKMKVyop574-uApWmSovsWGehO_9o-6M7X48vW3VzFzJ15GFvQTJup9CNCNF-Ovg7Gw8D75wN8v5Xa4o21K-x2CVl2l0nMYmWvUkKM39on--pA65DlYNVNR5mKuenl6-1cF6RGv0ncp2sTQ5aVkOhHkTZLUGa7zI20OuuBESe0S0ZbOMBFfIJV8PGnPNPGDL4sf8-vBlsjckLUON0kPGeJw7iBMLOrcFCAwKCL4-Ygvk6d1Lzpg5OEADOBrlH8dunXQz9b0JqNPwk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X46uf5NbXAAjo-baKTlfSVV2jDKEITcGVeq1wcOpvzVLuzpbGRnn5JfoYwLb_wj4I_Ewtd-D82PdkhrhTRvmxNIaRX43JeJiVZGi2GXUK7R68db1h-fxtUy2a4g-98yiGaZu9EZldyROMo_eAnmgcLmpQe2zKj5ExLaV7Hije76OlwjvMQiTSgfcLNC3cnzj-6QSca2SznbDHnXLkkWU_XKMPsw9nyq6QEhmDRlwgBuc76rw5YHO7sfJy1aBsX2BfiIsuzjBcavSP7gd8fKPCm5p5BEk8f4gAehqJoUSHr3F1jtb-ZH3wz5DVfytEoz6-2KxN1Y4nvwmM_7kbRtDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxxW6IhnbWsY7lSNgQvCULP6uneyz7wcIgQ7Qt0UI3U5HmBGrCw9U_bzNnEZhDWimDDymzOiSOiQ-uPlmwpI7NKAifx-qTiqcx1yoXRyMpw3h0qfRwCsek1qhCBQEbnN2XbJgQTRJ_t9UHdeYCg5HFG8Kgs9rvJ9t8lnAVBetIzDohNcC6XiRASKdFoshExel5mq4zYmfeuWV8EmsNf6R8EFEYgeR-6iL30Ml6WP4A61DJuj1lxuoQ24V7oV0o9IOhdFulTVPE5bqY9snXzPDIV8RIckioQa--eztQsZsj65vEKrp88d2saom7j2ZOZ-fNhAV-hKBJiQxOLduVQYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=mMfJHo3QUNIWF9geRAQ5Zo0m85FyoyD1QYDdRD8Jsq4lDUzeMe3E692qSfHdGkk5w6k0KJnCQAXgzard3cmMtyPn-eFLQp0yA-SEie9HBFtt2XX1lqUYOo18OTVVpyjgZxMGuxe28ePBDp_1Bgx1jaLvbxs4c3fHzwqbR1rIhB_uRYy4gA6B8vemHiKEAMo2Uwyizh01kTVvJ0GzBBnPFCxxSbVvOfryeqlFbd7w_VU1ZsZtn5pOQuv23P4Dj_48MJNw_bUeNIXnLP9Z8UuzXUVNRiMk3SUU6Yx2C4hb35fiSeweZzmHECHg_3kdQ4y4aEZ78dQae8a97KYE3SnFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=mMfJHo3QUNIWF9geRAQ5Zo0m85FyoyD1QYDdRD8Jsq4lDUzeMe3E692qSfHdGkk5w6k0KJnCQAXgzard3cmMtyPn-eFLQp0yA-SEie9HBFtt2XX1lqUYOo18OTVVpyjgZxMGuxe28ePBDp_1Bgx1jaLvbxs4c3fHzwqbR1rIhB_uRYy4gA6B8vemHiKEAMo2Uwyizh01kTVvJ0GzBBnPFCxxSbVvOfryeqlFbd7w_VU1ZsZtn5pOQuv23P4Dj_48MJNw_bUeNIXnLP9Z8UuzXUVNRiMk3SUU6Yx2C4hb35fiSeweZzmHECHg_3kdQ4y4aEZ78dQae8a97KYE3SnFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=soBiUxm1V5KZzpDcRaYQlXGJTyPnrDpXynBhb92YSB7WvyPc81qYb7B6Jhox16xSd-ikMdrlNmgwktFmM-DhvEOXF5NF_P8_CqifcfAOW8mU4523guelUwcEg_XarSLS2dzOJfQzHwY63aVYzom-WdydcuRxvd6Tvnrl_cJIE523qrn0oZBPwpJSaGqWJ3Y5Tk1FIpi65vkPKMIUwIg3yXwqs3jOzXFdGUSUziohwq4WTWickDXGCGSn5LpKUrtXb4BAKdp3z1P6yvv5ZM1Yy4nAC7U2cBFN6oDdvRA6uXFY0wzWkF4368wfMO9M4-McIBVUFL9QL3Jkytng_sd0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=soBiUxm1V5KZzpDcRaYQlXGJTyPnrDpXynBhb92YSB7WvyPc81qYb7B6Jhox16xSd-ikMdrlNmgwktFmM-DhvEOXF5NF_P8_CqifcfAOW8mU4523guelUwcEg_XarSLS2dzOJfQzHwY63aVYzom-WdydcuRxvd6Tvnrl_cJIE523qrn0oZBPwpJSaGqWJ3Y5Tk1FIpi65vkPKMIUwIg3yXwqs3jOzXFdGUSUziohwq4WTWickDXGCGSn5LpKUrtXb4BAKdp3z1P6yvv5ZM1Yy4nAC7U2cBFN6oDdvRA6uXFY0wzWkF4368wfMO9M4-McIBVUFL9QL3Jkytng_sd0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZvJeozXN8ynKqEz_TsLaUEslT3eVW4m0Qf2kdgvLkhKSpyq-CGSWqkjR4r_XnJuCCoqmrB1p8Z4Y-jRyhajARmBANMRaM8QwcXtvB5RIU_53jfYeMyiuZgD3e9m4owLepzxhZgy9z5VcIxJf0Lq3Ky1HzBlL_e7jIM-UBmKX7Tz3Zuhb5WuxxxsJNIRlq-vSMWA3I1cGbFyZYBoaumxxaetgs2ZUX5Fyc8HvxcpjCuQZRj7Wrjk8_ol__iudzpNtZle49SrPDl1NlsBQ16FKvEURI0ySTcV3wXOK7EUKTBq51VS5pzyMAVOK6hNCW77chNoFLGumIV4jjCraq4Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuYcs1NB28sDxq4YS1e_A08rRms77LSTgzpXYeBYgaZB5wDD4OHzj8CYcQwhEi1ASz4gtYOASrLMOG7R3o4YkgWvlAk66gcJWF3OoIs6nUxoyEuckWpcUK0g-Z73S-Sa6ploiQVz2obt7RdsclMEgUyHsLWtzmcbyBGn90mxlgXYrRhkMAdEd1JVZnK5eDgXGX1etn0-pjDzYO6fzfEmeTCuznI5g7yW5bsl__WvvuPg4j_w1_o89PRXzQ7JCnlUB1cx-Esj3jd06tAp4xoXGv2t1zYUSA7wHOeI4nH-WtzkvMNdj3TqkoZSab0SlOHJ4g96xk3DK55gDvmnxFjbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=Rf4eya6J_sxrS79bVej_0umYcJfCAKG_zmdjG7qvEYzjHY4uqcfP_vzVCtl2kLPoj39CTvP2be0B8Sy5BegTgfA2dQXKEuWL7d9rdni1eRLXv681n6D7nkmN5D3VVCmcQLHtENbRfxCZlM1uEw9uhen_a7iW_qzMDIW-CVMpkYktTX2hQapBf_sIYEjCr7_Pfg-KBxWxL7IBb8ycFkOEPtPiZgSD5kYZ5YC264c3iDyk8lnJI7s677s6zhhdSBz2KmWAOQfVeDJSx0GotZ3JUeODOluufI6sbD-m29n9HvcZDbJvbKVSMJS6QdC9b4C8U1jm21751HqTvi-gV4xQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=Rf4eya6J_sxrS79bVej_0umYcJfCAKG_zmdjG7qvEYzjHY4uqcfP_vzVCtl2kLPoj39CTvP2be0B8Sy5BegTgfA2dQXKEuWL7d9rdni1eRLXv681n6D7nkmN5D3VVCmcQLHtENbRfxCZlM1uEw9uhen_a7iW_qzMDIW-CVMpkYktTX2hQapBf_sIYEjCr7_Pfg-KBxWxL7IBb8ycFkOEPtPiZgSD5kYZ5YC264c3iDyk8lnJI7s677s6zhhdSBz2KmWAOQfVeDJSx0GotZ3JUeODOluufI6sbD-m29n9HvcZDbJvbKVSMJS6QdC9b4C8U1jm21751HqTvi-gV4xQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=Ef5JsWXFfbKFFNUp2wbWOMFTXc-WoxzvFMSZP4DZqYzVJZnByyNDI7XuZKKtio-PfaFl_ZwWwsoX9O1PKwaLsrcmRPazx6ZlkONywj8X88K_Z3RzYC4mPSvC58lwYaKh_ytY-USqHzV23nSwvjXzNmh169Wnf2LeyrXQRigwW0NXHPxsQaOO1TaXZ3n-50O0GSMwUhAON3-Sb4k-fsP22tu6aTDsbCJtbWVIGi4U2VDZGv1GxJwvqJeWRvymLHbojNCzbkhAy-nqMBj9vkST-9M9IbNheGCbBtgObdxVYlhZsKFahsMnhY6hKbMOmqT8GfNJpw-KZ_PRaheT2WuNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=Ef5JsWXFfbKFFNUp2wbWOMFTXc-WoxzvFMSZP4DZqYzVJZnByyNDI7XuZKKtio-PfaFl_ZwWwsoX9O1PKwaLsrcmRPazx6ZlkONywj8X88K_Z3RzYC4mPSvC58lwYaKh_ytY-USqHzV23nSwvjXzNmh169Wnf2LeyrXQRigwW0NXHPxsQaOO1TaXZ3n-50O0GSMwUhAON3-Sb4k-fsP22tu6aTDsbCJtbWVIGi4U2VDZGv1GxJwvqJeWRvymLHbojNCzbkhAy-nqMBj9vkST-9M9IbNheGCbBtgObdxVYlhZsKFahsMnhY6hKbMOmqT8GfNJpw-KZ_PRaheT2WuNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=ux9rbVcZhPEtWm_lRFW02GK6xUncTUXl0J-yBgwUYaMH-bQs5XIxTmFQol_67LJlBIh7yAikQIJyW88dE76fOlybKtyVmc-66ZEZid8dmT96gEbaNUy9RqvCRFgUnAsOR0Y-vH2Bl6O9VdZ6bV4ZSQuCTLzQLbzujJwjFoslKw7tYUw01ou793bKVM72L9iLhfNyr4dact_i7tz-6kAx32aK-jhxwKgbbjWmdMU_gL8M4jqCXcrQaMcDxiq3-li75o9dipFGu7EO2X-YrVVdOyWocUHxPHdqLf37DFA7-O7VRFixEGJuyylqTEW95IyMACDNXANmpJACqMH0_RMyug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=ux9rbVcZhPEtWm_lRFW02GK6xUncTUXl0J-yBgwUYaMH-bQs5XIxTmFQol_67LJlBIh7yAikQIJyW88dE76fOlybKtyVmc-66ZEZid8dmT96gEbaNUy9RqvCRFgUnAsOR0Y-vH2Bl6O9VdZ6bV4ZSQuCTLzQLbzujJwjFoslKw7tYUw01ou793bKVM72L9iLhfNyr4dact_i7tz-6kAx32aK-jhxwKgbbjWmdMU_gL8M4jqCXcrQaMcDxiq3-li75o9dipFGu7EO2X-YrVVdOyWocUHxPHdqLf37DFA7-O7VRFixEGJuyylqTEW95IyMACDNXANmpJACqMH0_RMyug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJLl_RpHKBB6B8REXDCpWyjLJM6UUcQDzcyD9OZHOp4-aMtfQs1Lv2kgt9GuFPHIu6vjgxYraaITsMY-RgsOkRakZ4oGGynin08-PAfTZmZEdVBzdf2PFx1BYYMtbptZWaXDOKInb_nTOcZsTV8FEzmDr1huGRZl2Z5ObYyFIU-BcAQe3KzyzrR3y5gKnFtt3n1tLVkFiy0fEdZUOPne8qYfYaFYHxavHrHxAuZ4L92jQkGQ5QsXkoe2yJCJSJhdyZh55eBklWMzZUNUN6QptwBeuq5Acu1rdkyW8Wcrgf9D3BXWV4r2WLPQS_UYc3jT7S3g6B8PbpfuZugwy5PWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWR5eM2VysL2ji-dDoSbAGLIKhpqxXx8s-Y8fqMR3DVU8kW_qr_muXEiJouMQJ0BJ9xTAWsNwiBBWRW5YwVEPjMQB-F_F3sT38zsGs5b9ctjysv0P2opUIdXzsze1s_Hsxv_sAceFZs4QJycfY9Zm_q8ooB3WFmy5_UCEGK0jSfrstASdJwZAwJmr6yvASeB9r95MrGbFvR74SjBWBLPSBhf4ltRBTuTUvmHiqoJPI78SnbVeyANWwA-Ivesd3fAWAxsCUaaPUVJF32fXHipNenkAjCc1yRIQjXpPsyMzjyhWEnwiAc3txXpS0wDTxbfXSc9nGQr4Z6OOJjPgeVTvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9rkns1uaACzW0V9r20Y2Y6ml2dOyq5pFp0P55ENQ4WgsjJdiCo_0kWA793By4_p23evmB9qGbt2tkAcKCD2AtQdneBOZqaNUpnIJ1orJmqU0sK36pnmZ_uiIX-YzVRnGu9FcwRtV_BF-ghSBcCQ_U7mzvyejxCi3axsLdefoHSTT0u7caQzdnruUcpq2dYRIRPPN72U_LMR77ePBvAk-0-U_8tRmVLEosCiTX5q72BdTY12onwo1qyFOPCIMwXb4PrZqg0DANlIQhWsRDjeCZ_8DrjKDP8TaIWuq_YLUMBOOsxOuN9lw8uuLni7andRe2fTDFC9TNC2tGroL_P94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbeP2DQL8MsLF4_1p3pQAClG1Ra7Vd3zRXQazyCY0u2SwGT-BYyKOsP0B8Yl6mPNtHPwlHJJLyhDuGR_d_2Hnm9PpV_KTeC3dXotzIc98ITLIPFIg6hMHE5O5uodegg5i7XkgHxrMjUc4gbPwAQpD1Sr1oqZbMD3KFyaKp24nPgTPQ53BZBr8UoCy02d65y_RltV-zJqk1gKmwf-puH7hPTuCf84unSBUvrnj0ea00Bm7QFY4X9VpkQQ51I65ERvo0XyQTUn-8t3h0XBfWWBJNYxOBuHNk7jSgfQzI1vB6M_TCbyQVD8clFY0IDWyUVUiGYpFcuJNp1bRrWT9xE8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbRSu19CR6okESPGUdQ3SXoyzzg-O5inzlQMbIV-ecjolEE4W9ExKftrmePofinQ52bxel9a7-2S9idmfTmlZFA5ajebaDNiYNwCL-rx2CviML-GNT3c63Lx-kErV29o1CNmhEF8FUeMaZP7QU_17N2Df8OI_4mN2jruyyVUavoTuNXwvGUTjWCnUSi_kWy8wPZ5ARAYAo6A2PhwWVPQ9cbeQniGlCQ7FkLPRIRNg37dvMz8F8yUE4O6Q4oLCE_167tsn1TnEFR4IB9pdj2-_hi60GjjB_o8eyOSp5Yn9XGpTUwasjrQ4qx5Nbd5WEFB1oh2Bf7qDKtnzrdwNTdsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=A6tBgGgiaM0_iGqUCkagbRyfsBxD7N2IIOlpzHg2w3H1nI6T_UQsUj60qakti5LFx_oai5UWYt4uayMLfn4Rruo9B31pUypQQBxEDeC-ndDV7-SnvsOkI-F3nZ3DNpwo4wOn5TLqrWOlVGNzwtFppgVBUpQcoqyjQQnqip7GTTjIBOBFEAemM6G8m7HU14QS2qf-q8DsHS-HAm9G5g2WBEFFGO9MNvad6_dScS6NmzaT58oLw2m4ZA17a1BE2N5duE_uNpn7fPxFZ4bZSg9E419QXzhQgdJl5I09XVesEOlYjacyLz5WDJik2GOFOH9Lg_UvCjDTuWVpnDhx-jexPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=A6tBgGgiaM0_iGqUCkagbRyfsBxD7N2IIOlpzHg2w3H1nI6T_UQsUj60qakti5LFx_oai5UWYt4uayMLfn4Rruo9B31pUypQQBxEDeC-ndDV7-SnvsOkI-F3nZ3DNpwo4wOn5TLqrWOlVGNzwtFppgVBUpQcoqyjQQnqip7GTTjIBOBFEAemM6G8m7HU14QS2qf-q8DsHS-HAm9G5g2WBEFFGO9MNvad6_dScS6NmzaT58oLw2m4ZA17a1BE2N5duE_uNpn7fPxFZ4bZSg9E419QXzhQgdJl5I09XVesEOlYjacyLz5WDJik2GOFOH9Lg_UvCjDTuWVpnDhx-jexPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
