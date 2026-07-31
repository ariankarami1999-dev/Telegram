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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 508K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJAhr05LZaBk5oKwHpp0bYN_dHbNaQyz8XmxlLVGX328HrqaglR5RPL-T0Ii1Fe5zDL2ajJmK0qiNbddeqGS1bAbb-2n0pFHhEAXp_8x0G9HnhSV_biaUkHZ_c0xk8NnXngSP8aIw715IEj13cboQhX6uc8F18n_pq6M8XfenGsVVJPOOuSj-Y8Z5prfIfIrGN9-KexbzefKLZ9QEBPq8cTmFr1xYJlSPLW_ecsjakNTe3mZ2smpiSS48QpojggfQ7Ep1niN3ERQuWm3mNXiJHJPFkXNpH7fqUlBe6hdMIhO6bYRdJLaHQGV5DrDOlVaLzPSfmazYDCsGaEkEpLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pasn1V423e2yE5Au_5YJF0N7Jlg2ktOj6hO2mIpcrJ764GEF4ZryXwUTkd7G8KDt4trGYzeRw08aINH8XloQOOy9XeNxkdygJYYy8MalFH5_SVfey_CYeC2xwk5lD2ybXEEElktfEh1WpOFR4a6m11iSLlDe_IRFbT_CNoZKvP5noaOW8lwcdfwxq0EEnn_N9EplGy6ide4DXpggv21hEyNBGzKyTRV-QxwZU7kIilly3Rewke-P7Kj9ooRihIFcJxgETLt-BXKQDs-am0l_8zRv7k9OopfTkyRHUPsm9ZRT9YrUNMgyfTgprMmXFF1sTDi-a6SPX9ksW6QpP8f50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=AmdQv9Mm8g_l3j3TmGsalN-aoG9lDdSH0bmErIyqjQ9_nhf9Uy1-lGqTlNfQg-Xlq50EfQz-bOFuCYdnkvNZhmb3Yw6Lo7ldEULN2iRnJcdiK8YOb-1oWTOlyCk0gv89bBAv9Gqz8oRnPa1H3mHUAqc7soK7p-GwiF9JmS1TsEGACCAgB5SKCirfe4G22O5x69gPCvaz8Of1NvrPeGjwrCM_C-N_7QSD93nsOiX1gbO7hh6hFp_Ye8MaGKZ6F8dwOnsBRIHBTeztRD73i-UtaoLpJNxBqDimYMInt2R0zzKZsgsz_1dIzQYo1FOVhF9c4zEzwWL-4dmu-O6Cu6PCQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=AmdQv9Mm8g_l3j3TmGsalN-aoG9lDdSH0bmErIyqjQ9_nhf9Uy1-lGqTlNfQg-Xlq50EfQz-bOFuCYdnkvNZhmb3Yw6Lo7ldEULN2iRnJcdiK8YOb-1oWTOlyCk0gv89bBAv9Gqz8oRnPa1H3mHUAqc7soK7p-GwiF9JmS1TsEGACCAgB5SKCirfe4G22O5x69gPCvaz8Of1NvrPeGjwrCM_C-N_7QSD93nsOiX1gbO7hh6hFp_Ye8MaGKZ6F8dwOnsBRIHBTeztRD73i-UtaoLpJNxBqDimYMInt2R0zzKZsgsz_1dIzQYo1FOVhF9c4zEzwWL-4dmu-O6Cu6PCQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opCd1VFSW15xEgcBW6YJbJknArSUXy7EfzriyoZgcGHCxAAQyDLN5fmTOWq7XP_eYopItp4D2hBMp6f3CisT8MZXN8p95nY6JwYDdUYovURFgiP1zeuif_pj1lMr4mGlTgEqMhzLZlmZx-Zc8smhmwRcS5rpNgQT9rQJxRh180RD3mAVXATLwtC9wid0TQmRdkinHPIjuD17_o-_8uSCj_nKM_wSYljcYPoG9Tz2FTC-HRs0_T9oBksJuXC6Lw0YQp2t4i3NkNesZ1EswVBo9x9ztUdWZCdTnmp4Xur-0ZagijAVT7bAd2Tx3P-ajz5X83zsez9-fx8pIOw2C7ErOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HqdcUXfQm1v0M5NiPy9CDp9c4bkVvrYhaKqcrPOcD38jMrt1me9sOF7dBVQp-gVmGhorfVCZeqMkNzgxZ1Nl2-GnecM9lU-EEqe1v1qimldDYj5WUCLpYyxJ3rihSPIcF7lZoU9SLlGw5OYVWBX5i_Jy-7BXXN4Kqnfw7qN39qVGKoOn_SVbtkkDni0z921Enw9ooGrm1Js1Pa6cDyMFcEpAsq4GxhsHt49IsOXSizHgNTWN1Cm8Xh0n-mOzlYirBq6a6RAomLVQn91FBa4jH66VW4BSLqJ8LYt-vneeCrtGbukI0pYfzqZ1XEQHvFYK_EwfLO-QbZTcKej_OG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1OiiTiAzpQE9z4tIIarAGBsZLubtLzpzz_gtv6oPhGkCN4pEZH3PD6MYw4nVFqPiQ3p5VXqWuMJdcYxcqdVeX0hD-mP9FLqrJSHep6qfCIRoIWKtEZfTkusblUSmSiAdQF9om7Pnq61dFKGbkjjL3aQdLPqzlf6P6eAzqIoWqAWlilqGa5c_cETZh0z5EwT4YDPUjSwB_mcrt6Db0WTWncBXqOsKdWy84KqeTxYlwy1EhXzaGBj9ROE4xqgw9S1Fkc4gVuAfPQTrJc_byNajYQoEG633bfSpI58-6crbxvpCIfTEl5liTYoZ7ju5o41J2bROz5kQgTfPP-HNoIFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq-0VXPVp2KNEzL2HBUrLP5QK-RWmC5B5AWV67s6rePpeAuMDO3pDexGxT3kXxFJ2WvCMEe9zsZt5UiIh1POgp8I2Pl_fegZW0AecYlS26chqSGCM5x7Qy6YvyOZnc3ZMTX_TeOziMfnQu4rQSv3CJ7KEajbG9Hb6hTfSMOZYtz46tYlPajU4HwEIiiOwBRkHLRtaljtxdFbMqFV7m8w82gDr8qyrPCxMRoVEhsu1T4rCZeYwx75CwdwPvwOVJq4DdWeoIq_nAnEmT5_bXNcwKI_zukk_980cbJ-N9Ww-i5DBqh6ZsfysMB4S9mfj3dQCfONk3jQPti54Z16PrIFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNG5RdvSPi8u1ASpS3YfgBHZFBwKhILKWZ2pD9_iuzFQhTwVY2lsIiXUX2F5HOtr5fUQpz72k2C4LoyYQELL_AT8-3DjxybKxUvMncYkGGmWWj4B0emGgBQ5Lv9Nt65s8xNJKFB-W7HYITVG4hEPD_y2UjFJK74N6wYmwoE0sadFvosPu5IbfNxbja-JPjtEiGFHLlJuoxYr-eYCeekUDwx2arLPR1vW2noP1MSfG0g0yfp69c7SIPlZxXJQz-j-_F2ag3INGxMy0rhFA_ZKnrxypUK7XJpXbA5zCxIuy5tr2xHJt-o_s53XqgiU7Q_oezwGhUlS_xyr66-rsF_Ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAyZD0fMXqr9TqhztnbA_tpX9MNbRDl4B7a2Rd4cIMazhFVCZZeCM3nqzBykjg1KjfjZXAOVycjuavd0FVe0O1y6LCkYFf-hXsQGUSxiCk4gk8d_1e1-CCwVK9OQAv7ayy_bbGcY-9k08CAeU9RcoLm2Gjh_6e3Y3FFcO243meLaYLkpwMsqcSLEZvqcxpsQZ9zMnHslpf5_zPn2B7yO9KVvqoZNRZr-HEUSS6D7b3jsgjVx5BrsAN4tmo8xQl2cvmT1XHmkcmBQhPEGUDzecao6eBRvIcoqOgvADfATzvA3ixHuXjVOnsE0x9R9lDAq2YJPkMWD371CBANiju8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBRzI5io77aSJ4atP-ROH80g7vDE7PCdw4DlAsAhThWrDG0kGViyC3GrMl9kEP14G0IWoLg7RSds1spO33gz8ulsihmXyOAaqIbEa1K9yUmSQrlu5G0BeBh5mKmoVt9jQDfbuBWuvzaCXgbXMw-etB0W_nCpUjpDsqzcFXsSkfkTij4mTF6f766FXRoaAfEwT3TqTaOhI7NANr2YOjmjKIFDghXxtTzFGizBXNKR0bW8ZnoCInB8knIV23RzTK868XJaereWYUs9u_PbTp_uDC_4cyHQDHeqi8y5N06EPe_HEsviiNaTL8pvWoRXcbuLlGK6KFba6-nqeg9F2H1woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Qe0UW7ry8ViU6hKg0Y_BUKAkXxPU0dNEJ9l96vyu0ouQe7I8ErWwNh2IVZoXNWqiNRxWThAluM9KCh3FO4YHJszGhOXjFvI116wKFajjYer5rtbGkrXiBDC0Q_SyBI8fNmq6Rq7_xw_rqPrHm64FOej-LD8g-nQnrNpoAT9N_JoB4sYul__B9mcQYTIrOUvykiXt3k9Kf9WXBovdQuDpu6MGkOL5OBJ5ylSbyn0S2oSr3Od4N0ppgk_WhwY0ejVC-ViFlFI77e-q8QhbrZMCN25QinOOmfaPHxCB-rCEhlgL3liYlcsSCucJhRT_SINNorEBWKx0DJwDsL0Hms7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8qIWCyleJRdKB6tVvTkOa41IbCNeJ7pby18dqoEKVs-esrrPGOrCIuPvzFNnIesC9CZDO6DbM70DzI5rSYmQ5DEA2FhJdakSHDMP2hjwVkYN5JuMdAiGj7_1UJC-KUJ5N9VImplYPjUVga64RzqtMzAisSaqX6kpKX9kXVBJETDfq4wqy_B3U8MQvCB8PaE9z2E9M46JmACF0grULJH-UQ3-Q35tiP3-Ey1OpXo075ecScTkr1SSV6LDit4S55y6bjFy0NMWmdgzZvKDiLfO5lWS1Sf8xulxYFEOgFmpK2lRvuaLsbBxnSWMuWKFgdAilxAsnfmh8MlLx8WZTYIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZiYK-7JxQ5JAt24REBfX6p-z2mFRmLq0Op64pPYS75nItESM5qFCNycAyqysPghDVVKbcV6aZV_6ar5TyYERRuahuM7GTNl0jZ2OLIknZzklQrMk5Vg0FkUJG1PFiWAB0njw2NG1Zs1s5AZMQJnPCFXkGSAWNvOqY60kDQ1jHr843p-4tkLxpJ1ElEJOXLMMoAfFcDERNKZOL6dFyV2v1FaU5mPKdK0FdWPm0iUMnpbVmwErXbCarKDGRaABUdc1vPu6f4r83_bqnVYrbZRU9zV5Dt1Gv8zwH34slFJ3g7V7phq3h8a9nNvY78-m2ZYP44w36lnA7PFNa600Aq4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTcvSAD8FEF9bd36t-v2h-jYCEjvqARmEH6fCILiuiyiwepIbrmtB5IxzQPlFTa3ogsaCB4dWOqnQpPepITVZJ8tLFEVtFFW3HBRIUq6W3hctzIWqBtZIJD1xLTnvEFlPegMWHThjZJ9UqS8vgFhGUeoI06f-2GHwqU6KHgVgXaY3JeCc0Xt_gxOHRO-x27oh0B5qEyPKQQ0aawWHRNbo57vtxFkw5ll10J2DrXo9L5SXPMPzJqoAePyrkTbNK57NRcMPQ5gucq_UndZ8M24NpPrTg3az8Bpqiiucfagr7jYCui-hEfakvK3Nz1FtN2ZQFiJX7hT1exN_vSwxW5EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSJi6921B9EfUAfWDcGskbw15JcMCFEVjFKEdMpCd6MYh0RCjUsjB7NmNMe7EsndHg-6SgSqzZqMkfCQv_0ywAcVtTuBz4GOUEoUptz1wc6GRe1514zdvTHkOh4Kk8Q_Kj4mfaJnVx7GMsWux5GrOrYljJUkja1UAoO_Jxznys02S5I8H08LW9lS8G4_0EQfCOZDgPM1EVJQNjMA9r5aeTU_0c6_OvzSWx48JO82VFiU4LMUYYpRfa1gThmmsDNyAfwuRrO4XePkptt6SVR09yPGeDOn_pxXITaZdfK-jRydunkBVllOYG02gbR7jwoy3ImewDD6AJ_HRnn5DRIrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqDpH5M5NX0_RAB2X8LHChxv6AnmEeIOdIwdSjHzLyAZcCj7icTvH8ocQZAeR4ZWkq5T_6T7FHzGBPDH3SvhM2ufp1eZzcdRz8lFXivCi3VYHgPE3bzZ1bMS_OwOj6DcWPYvKM9VP5WS5T0uEMKMpSf2fmKWkBP5mP2h1FRjVPK0BUKsIHvnCWxwJS-CzQPeX5m2oWowhbasJJwzZvmXcxmQd9EwcFd4ROfSneSVRbzq3aYJgXdNxeFx-evLiU3EwL1OyAoCpcA3CAb6KRkD-etbiXKrJsCtYINcfRumSFfImc8mLgdJvJ6Usi3bueyFCXDl5BBY7oQ96kxFhZENzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HISrN8-TZZvfekThLd0nnki5xAHr7G2Vjn4XN18g1GstHXzjdqXecv4esEHDwjE_J1mqmZRyLv-QsGhmHEKMQFa9r_I5O8_fxe8pq5bHiJ2CwHsBqyTg6qHMfFkwqdPGQ6_PQM6GQ0FY7PRGpQbjLSROl2TIKFj8HQujj_D4_gySBYwmlS4fXWuv9REuBCmTqm03CTrRX_Ecxh9gf8iJDNrzDTE95uNPEadRmwKRSJ63WxoJfMlsYX3R3ekhihY4FGRUIrCVcIZaKVqQNe0Fkju1dFRX3YJMAY8bTGx_GYNN8JyFy29taucnjhw3p_P-fEIFoZpEEup92r5Ijar70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p81RHJGNuFTl2HMIPVGUyG6_Skd_WkFK3fkqvC3Emt6SkwEXIim0Rz1JeCBHOQTXkjmRGjaT9KUl_EhsiorZ4WZkv23CTixoJ9dO-ZDAbwc6iztcmbWtJEai1_OcGeCOQN0KiORht3HmNCV9Ith3HTZIPJBFlhNm7f369AJDokomimCU2VA8rmUPfKtD-3xGfTTD1scFWXN-HByj4YBhpkt-GWK2Y8eeSY5GX1Zz8ns04XMwnci92hIulJy2jZgsujFLCBaRq0H6jMwbZE4kmKfZlFuAafjPSRnZN5Jvz6LkdTWQ9NiELms8FyZpO5pMVpP9eFWeX70L2KbYTZ7ymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHwFcDHMp2wBbiK2JF9ErBGXAVY4KJL7ojrHa0TX_v_kQX0L9MNn6WtxCrotCZh7OgPJ15spZ2hP5B-CxZnkg9IUCr5b-vwu3xUVPNl0IwNJ51Zbomf6Jy0HShz95s7A2xpE6HfosHXLVsjyZZe0vz7QcsZGt3wrhWZJubFEiQ8v8e1v5ClcZlWDOHGazj-cCcsPFoXuI3JlPlOxmh4s8yVQEtj6fZtlqS-ASMfVGgH4UFu21O94u5Rc0HkfWjwc_XBNSCw85KSE-3rxgASC6mWakRxfTocPZnmvdvBBcle0qCXmuVhhHiDQqrOiatxDomElRmPmnfwpU8OIncNb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywlk-lHzeNCeoeNN_Jiqx2xrNkirD6Vu503ukSJHy5a53Fqd6feQcP956JIBaM8h-1nm5YfqPTwkrWE5iNbrywnhDt5WdB0TygfginqH89hg8RWGb2zGKrxYSdEFOP0pQE4QCnGnTn5LSzFliJQX4A1egRiJbQzX5D85R9R3Aivzo_Yg3xKElYIysI9HX9nDyfGeY8IcDO0SW4XfftbzaIEykBFOhCAClljRSOpKBXvYzshWo8npqy00R0jkrW07_c9WQ19OSBXTcTDGHPabEyn2R3xYr4wl5w2WOE8gcGRiLnoWn5dKLZ89VEsYtu2jUROeeH2DE4vI5E9wPkjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteR7XqaN5FUFgLlu8vFNX0_Ki3NNllHo04vCpjlVF_9v8CtrAun7pD-xHWe7QOkgiMnBaseSRrWEvLWswUyIJeCwsYQ8_5n6UaVNNas8JXlnUL8PV_46GNPwTJnLvj_82i5Su6Ql-IxdRrRe995HYPnL_Qq9h2Adpr4aI2TQ-o166-uNthzenKVnND1yNxxV4PzHwDhB-tZbzxJKRQdULi0KupU8mPMtqm_JE0yLd4FfDZ2hCSAo2nzrQN3ltkg9cgMi2JAspz6nMR_z6QcwsDVNt-r9aRlbI1E8dUOQPN6s8LNjl99oqOXxwqs0RBT3_o_FuOcb2SaIHxH77NqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFsubHB4HPc3NDVspKB5sf82GciA4_ImB1xkQ7AJ4WJJSbJ07irfQbVBXuWkj0tHYLbJreKFgHcl_hdB9qEezM1b115qxmCYoDzFm4NIZ6S3KpSmlWACwg8V8UGv9lJ1BiWDgUv1wxZAm0cze_9OGayhuHSNri5SM6mLSOqqYaUayALeQKrKb42utQe1ly27Ddlebd6edBZeBT_y0Gf6BQMPp7L72UauCYwXwruToBs-iiMePAPsbwjSYkLSm5aY-fW7IHxEq3zPMragAJPF1MBHwcpATyBgJrSlwP5iJ205qeVsLC4ysmpxFMz2XO1L7UbPyfmFtVe7NpThfDXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEa21qDjvPNymo5eVKG3lZGqiez0UlkjnN0mpIVk3Qiwd5bYndwl2PIta-khO34wh9rjNLBTGqnY_lZb6qIovCj5VZtzuMEkonEYU2wPuJC4tcAx-DeTSP-vTYnaUX5-YDPgOUsSbXR2C5Cjq_9UJ_pS75eD0HNQz0Qqbi6gx7EeO7RNg_FUPcA0DSh_EjCKAzNk_jgjl00jOJYCjCqhVRwK3Gqy4UJgEWuiMvV02m7UVrojNhMerYcqm5o-Af5WdEU6_CF8RrLiQTIflsJdROsXRL9txCNwEMKgUIVhoW70HYuYRx5VsoHMlm6zNpvzfvO2WGtsvfnKNAYCSIAPLj3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEa21qDjvPNymo5eVKG3lZGqiez0UlkjnN0mpIVk3Qiwd5bYndwl2PIta-khO34wh9rjNLBTGqnY_lZb6qIovCj5VZtzuMEkonEYU2wPuJC4tcAx-DeTSP-vTYnaUX5-YDPgOUsSbXR2C5Cjq_9UJ_pS75eD0HNQz0Qqbi6gx7EeO7RNg_FUPcA0DSh_EjCKAzNk_jgjl00jOJYCjCqhVRwK3Gqy4UJgEWuiMvV02m7UVrojNhMerYcqm5o-Af5WdEU6_CF8RrLiQTIflsJdROsXRL9txCNwEMKgUIVhoW70HYuYRx5VsoHMlm6zNpvzfvO2WGtsvfnKNAYCSIAPLj3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=VX2cStQbCabSMoj0B7M6cleqVFLuU2aWv9NZU7w4y2Et1YLAV2P4hNmCEkZ32VPJiYYrXIlZMYsLydj3Ae6VGhpNtM3_bDkQKzg_bOPWTnEmusn3_zhiyYE7Yv2b9MuW25QsccXG2Zcjnro49hPOXrKRQJW-YB9a0uNU4Xb5Ic3Wy9A6Y40agi90SlC1ouv_MSEoWWF86ev6kGN_d1iymmYuxRgbhuP6NWFgql119LLiWvODdxSK7tYjyMxDerrI8mn4BUm-Z5ZGR0SYHWHxszmg6Jo_JA3VuxnL0nCtwk-rrxvfaxr42WwUWOCBMYxbikA83AbutP7FnjM_0bZcCES3oX9THuKvz1jH8nlDrAE2cCdUBJPDeFAK9kBpR0SQzpk5xBh01UvhmsnFA0qrmLYAiPQpgkr4-oyIdfF4A3oIIu2JmmG3xlDpXWzMHLhJGvTnkn-PcUoT17vqrcLUaxX2I7Nk9FMLu_yQTrmQr8X3Ihq97-CsfMSw5lUpRTT-xJptvJ6nUMHSGhf5EUNtGMeZNHwJM_1LeMf8AkT5nY2dIjro6gm39XL9bLsStaX9deiGaoGumEtpbHwnakWIOXPkMAdq7b5c7Ou7HlVJplDBrdAj-i7jBlQGeLK8DiuigWb-DBRbqH9_rXXPXCRjhXNhcqvqeZLxtpy1g_BVlHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=VX2cStQbCabSMoj0B7M6cleqVFLuU2aWv9NZU7w4y2Et1YLAV2P4hNmCEkZ32VPJiYYrXIlZMYsLydj3Ae6VGhpNtM3_bDkQKzg_bOPWTnEmusn3_zhiyYE7Yv2b9MuW25QsccXG2Zcjnro49hPOXrKRQJW-YB9a0uNU4Xb5Ic3Wy9A6Y40agi90SlC1ouv_MSEoWWF86ev6kGN_d1iymmYuxRgbhuP6NWFgql119LLiWvODdxSK7tYjyMxDerrI8mn4BUm-Z5ZGR0SYHWHxszmg6Jo_JA3VuxnL0nCtwk-rrxvfaxr42WwUWOCBMYxbikA83AbutP7FnjM_0bZcCES3oX9THuKvz1jH8nlDrAE2cCdUBJPDeFAK9kBpR0SQzpk5xBh01UvhmsnFA0qrmLYAiPQpgkr4-oyIdfF4A3oIIu2JmmG3xlDpXWzMHLhJGvTnkn-PcUoT17vqrcLUaxX2I7Nk9FMLu_yQTrmQr8X3Ihq97-CsfMSw5lUpRTT-xJptvJ6nUMHSGhf5EUNtGMeZNHwJM_1LeMf8AkT5nY2dIjro6gm39XL9bLsStaX9deiGaoGumEtpbHwnakWIOXPkMAdq7b5c7Ou7HlVJplDBrdAj-i7jBlQGeLK8DiuigWb-DBRbqH9_rXXPXCRjhXNhcqvqeZLxtpy1g_BVlHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYSPmZ_SsFeAxwmSo4vsamWfYnq3H1uumpz1i-OxQZqkBUMwhC76gv4F0h6DF3RqgQjDyYeNfUPKq6Umcx6CBW4_sHaOOVFeqLv0_o0M_u_rE8QaQ8mtwzAkjCBHbAU_jARtxWHUM1TOZnnMakjlPsdCa6KbTH9gugVWE_f7M7nJt7FjvWBqBynPghr6fmfLmxu82iW5kcLsddWkeK17DVqKY85XS3OUUKrKgrxWAY4u4fy6qD_bsIWKmG5EOopdqDTozE7UIRqJUe3afXRgZ2ger0_K-J36tv2AGQetA3VKw77zTVm-qVyaM6k7mX1X36J5YG4Up0LSCnXYIE5ESuFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYSPmZ_SsFeAxwmSo4vsamWfYnq3H1uumpz1i-OxQZqkBUMwhC76gv4F0h6DF3RqgQjDyYeNfUPKq6Umcx6CBW4_sHaOOVFeqLv0_o0M_u_rE8QaQ8mtwzAkjCBHbAU_jARtxWHUM1TOZnnMakjlPsdCa6KbTH9gugVWE_f7M7nJt7FjvWBqBynPghr6fmfLmxu82iW5kcLsddWkeK17DVqKY85XS3OUUKrKgrxWAY4u4fy6qD_bsIWKmG5EOopdqDTozE7UIRqJUe3afXRgZ2ger0_K-J36tv2AGQetA3VKw77zTVm-qVyaM6k7mX1X36J5YG4Up0LSCnXYIE5ESuFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC50pjBrfnV53MidAZ83lbvxmoMmkLrDHzbhS3hdTXBbsmZoEJxjKCBiq0hflVaSOwWwHhEvB0n1Pa1FVuyC5KIJc4a_lN_gQuJvlRtsIHCtBTJqWdRxNml5CrI9xSbv5sMFdNY54hmHzbC9a4kYcz-5eIHRbS1HevOG6R_FteB_G9cwlVcXnvYayF2l2Ja3mpnGFryIEXZQLPHU7uAdZF1jkxzZD9JhL1x7_YkIgDiSxtEJdob2ezcD0SVBu3k5IOH9sDVKKygcAcG-7wqZ_ePob_9yBwqyIuNJBL8dSKBsyfIA84OkDJIZbNHS6XCbxMd823slRbKLKHJegL0lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=GRRIFkZYJn8bZkVl8b9-jMx0czZqxRUgURAt03o_UGZvo_JIxct9SNxJd7WgAd5deTpHPrJwTxtRcns9sqBGqpmCaeDN4KNsqtDHnRaOj_vHbOTK6r7Igxl77woUCIbjdA9jLaFAOjPZtwK4c_nZmKb1X7jxURfGETZdzAB2LzioYKoTqbRtERZJTFTEWPo-tlk9bcVSsB3Z9mOpubUISl2wToCjkm_jXozLdx1GdAQgEmlRBv86POwhJhuSTtLWkWCXyp57p1u4Tmklk1uLD9snF3SyIJijVCLP7TUrXIridU3wI9dbmwUJGX5naN0s6zKHL0AMYoTuBPnd8TA7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=GRRIFkZYJn8bZkVl8b9-jMx0czZqxRUgURAt03o_UGZvo_JIxct9SNxJd7WgAd5deTpHPrJwTxtRcns9sqBGqpmCaeDN4KNsqtDHnRaOj_vHbOTK6r7Igxl77woUCIbjdA9jLaFAOjPZtwK4c_nZmKb1X7jxURfGETZdzAB2LzioYKoTqbRtERZJTFTEWPo-tlk9bcVSsB3Z9mOpubUISl2wToCjkm_jXozLdx1GdAQgEmlRBv86POwhJhuSTtLWkWCXyp57p1u4Tmklk1uLD9snF3SyIJijVCLP7TUrXIridU3wI9dbmwUJGX5naN0s6zKHL0AMYoTuBPnd8TA7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=sZdwTBotRK8yb-z06hMoKK11S4dUazsXd8c4Q3O0_A84aXz-13nRRw2gCFBoOlFsscUqbYyCDd7WdXlUsLpPwNRgdUA_FX0e8OHSBGUrlB__WAAN2yqZ4vxmmeV-QdYiiNo0CI_Il2ya9H21YF4dC6NzN9luVx4_LpezUMyF93atwfH1Llo2UQuRy1XAmZMeuOXodzwveJmQP8IQCFkUPHjJY76TJy5RSBopu7hT_3F4Re8pO1WDiU0F6QanCAEGQDzMXourC_eex1xSnM4DJO05thuA5SB2hsiYZI0YBRDBoiwtuxFQ36ampFlKzKLd5ZJicSEOi9ZL7Ss_e0gIjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=sZdwTBotRK8yb-z06hMoKK11S4dUazsXd8c4Q3O0_A84aXz-13nRRw2gCFBoOlFsscUqbYyCDd7WdXlUsLpPwNRgdUA_FX0e8OHSBGUrlB__WAAN2yqZ4vxmmeV-QdYiiNo0CI_Il2ya9H21YF4dC6NzN9luVx4_LpezUMyF93atwfH1Llo2UQuRy1XAmZMeuOXodzwveJmQP8IQCFkUPHjJY76TJy5RSBopu7hT_3F4Re8pO1WDiU0F6QanCAEGQDzMXourC_eex1xSnM4DJO05thuA5SB2hsiYZI0YBRDBoiwtuxFQ36ampFlKzKLd5ZJicSEOi9ZL7Ss_e0gIjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmt_n1SmGbVzkkE1qWtKjYaBxdSfopkaw3lhHeQU4yEZ--vNGwnT4N7KdwXfPQlSh6iID6Cmb6-L-fvTCZDhGL6fSS6iRXMu0UznYoAAKz8IaBSvQS49bn-wMnLeMHku-XsBba0l7YmaD42QEKYR2J4zIXGX0kCu8pUr9szN3ejP0MnG7ilPpuu7RangKLbE4FrV5MXlDFMOi3g8KI75FYwYbSGeuZ3fwC1MH9WBJpFFnh0vXsPxayy7NuHa5cPmcz7yputJvR7FFZ8NK02luqZaAXfjO5nLsQveNC2EBa2uEzkW7VXF1n6ye2rX4sDWTqVL3ElKE8fL8ovxUfQdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laP4yYUHSSwYc9Bzfh2bBl0ZnwHtyNcK2nAk2RFvWNPSEwvdx9Fe02csrGurmyTIJPryZzPSbO3Z95zDKDo_2saEFEvXiiD656nZXwNO45ZMvX_oz4W201vN1lhPes8DauLiiZK5n795o4klZ4HfmZn2d4Rs3RdpFh4ZE6smWbGMVocXa-1N4U8vJdgE30svhejWNyuzNlZl4rqPS0Re4dW0IsuXPMPMxDRpmLoM_zOunsQzDKFYu4Sr9wmryxuYs83284VjH3_0i05UUkR2QXDi1pG4OZv8I2TUtrS5tk2SznoQWhVrIPYb8OK3H8p49aW542L8PdYqN9lSuLcWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nA1zYtNawZWIqY3-ap-a3ssZumjb_P3NFTXrUv5qWXNQAxMwyQCsyN3Fx0Bnt_yryLDd6urTPAYfGuO6WHHTCi_wTWuAC9RY4A6ZM4ytM-bA05zP8QL2s5PV_AjzfCSpEBTOME98iJdqs72hFOQDvzb9kIj1NnJYUEGqnbtzup_bPdGIbX4BO6q2m2Xa8r1Rg4M84wcLSx1xUFok4iiX13cGQfBXO5tTGCAjxvxkbk4NuLgMtr9ncpyKHyoPoIlRBpKb9471XY0LX1wZfEKMErhNdL4wjnmsWvG02bwW3vs4H3BArFQroVwcMG49oUjOEnXMS2PWfC459Q9KFEe4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grMgd7bwomgJYlpbYZdcGGx9dbtOL6uB25prpM3vWDBv_lVZmeMK8F7Y9GOupP6WXEazzsMVUdGWIw27YQMifKFJ3uMPfm1QmkYDR7oCctIuc3q6Q_kjGphxgqgy53eMfT4TUK-5YIGng-Z-jrg5BVHo6bDBhYvALIqSek3WMlHkViBnHBoB1yO8xW4lQILk-ylnhKTMXa5uI88FDTd0k-pyc1aVrigeQBTK8wQYbe3exBIxrv70ETotZXfpWdKLC4M5LNZ6UlLWdDnnmxC0vbVvN8zcToIIA5av5w21fKo_OxjXe29ovv-HmavBR1w0Q3RWRADZSICqJ_npKJp0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDao887xOgdAxyC-PH7EaUP4EczRqNYxk-hLQFA3KWJ1ZyfrjL2yLTnmyygKJBEQv-Nt0c8ap256Ziftm8lM12_mmVfQg1vxiRqb7nL41qhNtkMpNHY_hZHZwskETpJ1VSJ1Z4uUSXQHJc24UI0lwkyIya2cNJykVK3P1d3OpXchhHwLE7Ksufe2uqmCfhSNKtbiivyYtDPMgwIBB4bzWvFG-V1GkB2iGVaS3yndZFMxLGubjhVOXJ5qm9R5iJQgnVCrOFuOhY_k3hLyFPG4lcjQeYI6zOjz7XZsB3BAcFXwl7LbR_HBHAXOVmoHI3tl0GDt4sxjLSXBbTfFFkn7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckzvb4vQbE6PcpKVP6iAAMgylaNGXwYnb3F5GO0gcFCbJFcZ2ZMznIz82qwQslXSwhjkqCMySdMbNkd93vnSyOB2EEs1ANKz5G3NdQgi5KUpWo5_VepV7x94h7zWvUtbRViCRyk3pSEIpaFeH5xXgtguBj5uAXXasfa7pQ8ja9EfWKfsibB-fKWP-VvLqZSiSNbzRGwMUgymACHlxRJjVemUfMbBwJRJsPrF-qtFvqlJrI-5QmG5TCIIVq4c0YyglOwYRVptbljtKemboOU-WGhsIRxiELYjWfr1QcBQfLKB-PHmYQuh3ro3Z5MFDEBcYK-VL-Xj7n42JXD0kDm1uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNT2xLrk1nYy6qomaqIoG43rMzkJTYvsgYLvuZaYAhFhTbLoyvAw-VafBoDsstP42ZL5uPkaiWN4t3ONDzRXacbE7t5rhWPtgT_GmwxOQq70KA-6TrGBOgV5I6CD5JydFJsT1gjq0CRRQnphEczoO86EFSBiWQmqdvyHrh7OpuYRFFbowf36Xc8I6mNdZhl4UqQ8fYB_JWQ-1QzHLp4Gj1OvWqit03sT0y6BCpo16x4N0mTiGO4cCc-7JntbNj8-1Bq8HbVm8LD55SYyUP1_MuoC1xY7J6GkYYSETVm0r9X4qKuXZ5u54iCrnvHcU2M79VIGGJksQvhR_vXjedznK2eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNT2xLrk1nYy6qomaqIoG43rMzkJTYvsgYLvuZaYAhFhTbLoyvAw-VafBoDsstP42ZL5uPkaiWN4t3ONDzRXacbE7t5rhWPtgT_GmwxOQq70KA-6TrGBOgV5I6CD5JydFJsT1gjq0CRRQnphEczoO86EFSBiWQmqdvyHrh7OpuYRFFbowf36Xc8I6mNdZhl4UqQ8fYB_JWQ-1QzHLp4Gj1OvWqit03sT0y6BCpo16x4N0mTiGO4cCc-7JntbNj8-1Bq8HbVm8LD55SYyUP1_MuoC1xY7J6GkYYSETVm0r9X4qKuXZ5u54iCrnvHcU2M79VIGGJksQvhR_vXjedznK2eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4pVYT6UwVCs1XeQcuWIL3j7dC6ulx4oDLuagKirXpuKP5v1ihYIBOh7_fpRcm_sfUGUEFJ0FJgOL9Et0CO_kqLCQUvFLGIdpvqzmjN5ryNuw1D76nESLH_Ub4BSfL2pBR4NOvo0wDd2E9rn6Dn2EU6OllPfLrpNRdgJ2vDsaLNVE1fBjA2iJ4heWV_OKHQ-AxjGu2lf8cRFT-3PlqB121o4Ah1iVPg2CqQPWcdQOlU7zVPs5k3wkRA24dXzwu_yCXReXmGFCs4IIQURxlkfWkCKEPf6tOGelVrkv-BgVTvIQM-d-cqn7QH-AUALPfQYT-TZMqCIl__RPvSXuF29bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQDh9e1a4K0YdDNWy86uYxQzEhb24uatq6L6YvNNeV-lxYF-3Mb5w8tKnEWMC4J_jLypVz1pvSM9dwswaWwLm2x_1n76XoacrF86F10ZZHPaZeTDiP9_lTySFV5nfrW5O6aDr5bWno98WpyFI9JMwB0N0svluqk1EqCKIQZuNvOHdaQY5kbb68pHJApMMIrKsJBmj-XpDRs0x5nwCn9oMY3TZjsEx8PdQlOgmpLHkFlWvOCDNAjfJTN4ZUhjucDtO25CQQneTqEr6fj60P1uBQg4goTNMdjlHV4XW_thy2mpxX8cj3z4bbfOnoOcqau8elfbipjmr2aGsR_289dqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=bqd8y5Dm4HJBUvWuSd0oYEsMoDGUZ_G9BF-khn83dXLuwS6N1OO037w5Ee-qm733JYpUk0OWZwDSRDzvqnRkFLRwwSd_E9zIszqFbi1dE26qmPJJVdVemXMt8RQNZOtCXqisKIBLsq4s4Y-x-vugwykr75fNhamIS0Uklpx0l4wSehBNtv0WaBqxFenMs8n_3xHD-KAXAWucVdTD2gHP5A1l2n3bsqRz6c2bpYGKaJfktklcWplm2XgrlTlHu8iJAJc7mILq5ojUpEmFdK9RH-Dsmxz3lGYIacSQPEfBe8Ke1n776mICZIAgjisF4jK5zTaGhzPpyayWlgI9MPiXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=bqd8y5Dm4HJBUvWuSd0oYEsMoDGUZ_G9BF-khn83dXLuwS6N1OO037w5Ee-qm733JYpUk0OWZwDSRDzvqnRkFLRwwSd_E9zIszqFbi1dE26qmPJJVdVemXMt8RQNZOtCXqisKIBLsq4s4Y-x-vugwykr75fNhamIS0Uklpx0l4wSehBNtv0WaBqxFenMs8n_3xHD-KAXAWucVdTD2gHP5A1l2n3bsqRz6c2bpYGKaJfktklcWplm2XgrlTlHu8iJAJc7mILq5ojUpEmFdK9RH-Dsmxz3lGYIacSQPEfBe8Ke1n776mICZIAgjisF4jK5zTaGhzPpyayWlgI9MPiXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAtZeos7laVHs-6zkgX-lN1AxClqjZn-HpUfOR9SocK9IDw2reNAPeBGiFIGCztUeKwd4ddlJ7VoP5cTIJ6PZUR6ZsWXj_rgjkOj6BMYBhJwwacReNubRwHQcukPAg6qaO16qHwZh7q-uPDzzQOhPZ5bwe-BPlsOCnX23hkCyKMrtnqX-aYYz2OkgmM3O1f4-j9Unln9k6fmusPTJmNtBUTf59j7YOl_elcJB8DmOyN67vfXd5Vh_BlBbmyMbytXz4-B-WdFIWjT4_-k9tePqJiYCJQ5FmaM-ZVBE7cnQZN-UTwf2roFKFqZZQBNb8lpQ2GIDeJI13PUya0O1_1zIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsrSLwm5sgtex9ivTJlKx2V7JSKYyYMwxSZmYWr5N8WPl-Bz8UmfEWc_rGaqp1z2ffvrPRFfZUhAKRfTrIpLbSDgOlVP8_9GsbqpPQP1mn6dHuApPXcTz76XZ6SRg7zrReXc4GtUkp-X5x9-Ex4IS_BRI9XHuw3aOcpGH0bwBxXVRhJ-sZEuh2kno5MKk4qPbNth2-D5A3N531JJTY1it-56OMzGLHk3Cnwmgb0vMK3UeAymPuUV2F3ZaDwcya7-QEsW_mQIoL5n24tLceyEfA8qS51rBIV00f9opjaXfzTBVGuUCce7AEGIPPwbVhJJtCNvmEGLRYU-zA4c32M5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VitiU_tOcK59ePw54qHg6OFk1zes15-fUlCGFBDL2AeB302VapgKNAMxEBEFwYSui0Pr6nMHLaI3-HBXhfHOcvprlEN0T4zzvjAudIw7S4YEYXjNFBxzPwLGZvr90ckjEJSIpP3svAPgXAfMWp6FUB1Ev5FI9lKIQPBjvuW1jffnQnfiay5wAbAF1zEC07hbKKAW0Hk3VN_Nk8LJMMO9BiS-TmnDDvZ63rHudwNpg0fTEQaB2yob6PEgBLc6w6EZ-ocUtxWaNApVrH6CwdhdL9tD9uZB52MQQPeS2v-FCiqYJter3_NhhIkQ3cTMxYXqS7LjjrN8V3LMWXZp429_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Via53qjnttBVxRxZCLonHqqLYPvMERXpCLfI1TEd0n5sNPmZomfIl3-u6WNyz_kWZQ01D17lLoR0US_HQkTXE0PH5uauFn-g8uuXBTafI4igQUSe6iCkwoGIFnCu4yXgQ2EcEp-b3ckFyyA7wFMxUdpqXBGmOlOAylxmKObb7uG3yymwAB61RwEX_2FErvCmqMKAC4cF7RDP0RCLs9YevVyobyI_38pG-fjsYjS9osVLF66xN8_IQwSsUrZ9tW1nR-QkPnJrrTcWP_zNuomeE23sTfF_MMd2PpJsyvZ8AvX6zuGNvj9uSOQaTJI-VxpUNwHtlaEvTk1d4DVoX2gglw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUOcW6HNWZY4pM2tn2jgtEEJ8_mRuczTqk4iDvpX2tnoA57atMGFNCD192wIBx2a3DL8Uqe_sduRr13TdGwF46Z_zoxg1dptPi2mQK4mocQcSm2Hz8d_4Z6KidnDka5Vm87OPujTN0ZN0iqCTskgj4ybn3YQmlnIyMSd_8pT6sL_6Xq4JH80jsjPtslRzksBiAz4u4aQij8wYZYX7l1mvNMT4DIqt3raHThvHDErrA_8SfR-prrdJ8itNiwmhjskA3yH8pbKsLwA58Nu2od-QjH2ZuJJ7Myn0pCizUAMPl1O7dtTa1rSl4cKAB9GqAY5V9clU4dSiCXoDxIfbAsgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT7SRX4g1rjSjaQzI7-10-uBuk6dZg3cP43jEISuMmI0pR0K8C2xeivexA3lpEzr5kUIDChvDyIoCdevTF6tITJWO-bPof77RsGMbOBbFDR2ozM4vEyaNHChjV-Zb9ZSHBDhYOTA5ieGzbeM8EAR5LlxNzOzp_vUPlfcPXPjECXO6hm_6KBE2s28kXkeu3xYPvahWj-UhPEUdqUSF1eBP7qsrFlaTwmRiKZgD-BuDAXVTx_CEmztG3I6-4g9BUYt4ZnLYMo-AduCYom-HcGkymkbkPLot6DOuYWQ0WXtZQKBkrAAusmLzyPcGf-lRmJnIYSe7KFda5uovlor1enoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HDUHlNCrW-uzDNYkVZWy67jd5hus4Jb5hcYcEcNeZ51-P1clycmX2uagOlfTM1gIDfZewx-C7zVUUdlcFu_2SVIbaLrQaYlfKz5iaTU56N9yPxq2KeJSXT1oOZkA9SuR_f0tC3Hy4jChbFS8KopaxpqB8flTUuVb8nO3XY7CqeOgroydwTSRspd1Pq8mc2WnaRWQwze6w7g8ND09_0Q70fHHyemNnq0xb3wVzAE1Vl_MFRG18_0HtUkA-j30QP8cVxoyoRzPgB6iUjddYu6eD3ApKO-2oeRlh6-90ivT56igCs7Lf-gsBl6adwHlV0SRdhh6mN2Uw-36y9STSZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpTZzVo1RlZBlXEk9nWxPi6GsBF5pUNOrwu1YO8ptcj24O4-DyR7IxoymKawmDobAX-JNF70DNq1ezI7bBN-jxYHh1YgP9dINwZB5eS-3TK5ulVDlktY2Kzspq0YSHI1U-wFTkMepCLK12MLdiFUInmtVG9oFSth1DiXxNnWDcwJIsbPJi3Z3uxTaWLiEF89SdZ7ILap4vMQpUH1IJ4BTzDk1EL14Y3lFcCtsQbOG0IO9cXaGtjOYfBVXG_isJIWKVrG5QSXMYYuG4Pe-RP5v_9QeT4KByMrS5CuOcfyN_xQIlSk4TyCWyuHKwir6RYjJ0wld5r_qS6gGAIFieWrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njdYbb58eXr3drL1rycUOJ8uAwVAgRJIvJPqakDR5m0R0WzHwYIpvCJZ5Wuevrhj9-01N3-j7QZMWlbW2_W65IEvnjvoPhKnlNDB0MGEPsMV2S64vqdKH7lm2jbK-Pz_XuNqUYCeuEb5uqXbjg_TBmbzw4oYiuVZAh51v3BaxC9zeh3_xem5ObSWZC5tWA1_0oCATFuAxnFmIGFSn89PaJqGCMWgbxPVUXMCuNgWMM0wc9P_57HG5kTt8hs_QCGeckOijIH2S3aauqQaiRLWTNVkvsbtVuYQeLcjPcmYsBrK0OavTUK2qiz8mjf9kiGYF7VafetBT0cmtVCvybGP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctuWmUG58ygqt4H_RIVMUCPkZKwQLJJHFdyqtFZmQQa2bLtO6ho6d1MAGmq0CvVvvdTQz8ZyBtGk8bIyNc7qOrOmTGgcAz6vkhkd4wl7yeNBwPElGLBeIDMhTlDKI3Cfm-jMtVxtV96bY8VtubzZswa3q8Uby1Gy-LxAkKuh3ZarFG4k-4hHM3Jij1XTVHWpjp-3DQ_cKkDU074cYcBQN5_3adi_95EPCRBwl_pXOK2jHOkEuzRGeLsFC6ZFqC1tGY-W9EuybSgOH_CImO_VJqLAAG2AmwJj54fM72rM3vXDUOhDYR5-eVy1rknIYfRxzRC5ryCs690oX8llSRUL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=cWVobbcO8PV0-YuQ-a1YajIcEPxVZAyZwuyp3gKuHJl8PZuE3Cx14C8gIawV3pwEBUe84Vn5cTKnN37Z1UkWHuvbO6Xrc-jNbcKZIZAarq8fIaFptINq0kVBV4XERla64m6s58_qFKwnCK22sU_cXRmlX5ejSkIBUeW-pYC-vEf2P2fNUCodjxdB-JKQQbhl8hwapAYa50vXhkvv_dRdY87Rk7jQz9Tl-Ei3xUrZD__VmRpvMeGMq7uuypJnwB9Lj5thqX61O0Ep32CDtXS_jYheO4k7UJeb9a-It5GkBzJIJ-moN5kaixEYEDwNkMhrrUO1lMl8l_cTiN2Cx2oZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=cWVobbcO8PV0-YuQ-a1YajIcEPxVZAyZwuyp3gKuHJl8PZuE3Cx14C8gIawV3pwEBUe84Vn5cTKnN37Z1UkWHuvbO6Xrc-jNbcKZIZAarq8fIaFptINq0kVBV4XERla64m6s58_qFKwnCK22sU_cXRmlX5ejSkIBUeW-pYC-vEf2P2fNUCodjxdB-JKQQbhl8hwapAYa50vXhkvv_dRdY87Rk7jQz9Tl-Ei3xUrZD__VmRpvMeGMq7uuypJnwB9Lj5thqX61O0Ep32CDtXS_jYheO4k7UJeb9a-It5GkBzJIJ-moN5kaixEYEDwNkMhrrUO1lMl8l_cTiN2Cx2oZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlZqTcWpOWP4v8Z2VXdVcRQztKkPJRTFe0IGxaOmWyvJUcuxH6083IbEnr-7JEg71_NPNwzQa1CQZCAyJ3ldOf7UuNkD45quZksWKTEYbvaHP82eS9QJoECKJHKbQkQkgZ1HR400xYL2adAFkRF3iNkPnq2Keeg3Ba8Zs-YHyDfL5qzLjtRdiIju_BUatfcQOCYfJ7Ulf_UWBzvksz9eJwTMhAOiQSbgNbhmmO7A8QJkTOYAoSwf3CJHClDJwsYM2edx82PQYtOZzwwN3p5_ek49qW8RJz7gZft5J0h3KZoUvviogZP2tkMrQEOuFbWwnVDhXtmmRFe_mZc5ZZOa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxiLOdFxBs0c299iDiEE6dUIqCmONGiX2Z4DkTKLTTx4HLmX2N24OzdabdpCgGsU-5Ako4Q7Kjw6IPijoh4PQs8P_3y7HnGUX9LPrwZ8kNu_Y8hve9SArHUHRv5SSZS3_-ORdU1swX6xdixNsJbFnZf2s_1VvKda3XXZNs2jVL6QfblieYZa8UuL-HF0-b2ur89EUWNZPoFeVxPa9mxeomUqC-OopcOv6BFtLOn4CRmFurirRP_JYC8eIj8FFwRQ2Cxv_zOP5i-UGO-Td34-7mkAU_GiF8GdaJfMvKbjcDvGR70sFXRADC-FqUAJiLHzGZnF0XpRN6pjUo9RKj_50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkG37_Ux5g_WWJj1Sx2YCWXiqKfKQo9oZUshusVWN0ypci2en-eFgFoyYxyss8Nvqppeq3JzHyBfeh2AwO5GSceEW04vhd4fqbwIh_TQVzD9GQyohZ6uD8l1acYND1BbFjwwokNcVcYKoCKonSKahXp-SlPxkTdTMnc224uRQVWKoHbzP7k0CGv8AWIeZPXSZDvXIVWZML5CCe27E562d75HGVz56_qC7HY_6NnXNrShVokj5aOwJ6m2ZNZeBmJPitKSGVi1-Df8B2f6H66HlcpQQKQaU3Y7pROM6mawnGXzAh4uM87SYAZByL1QCnVg3UaG2ER7HIMDExMysQfpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nghTXzVb1zBbO_VBG6X_XL4ifDOIiLpm9byoSYPv_ijxntWD1QQGxEaLm-kEYwb5yinQU0ZG1vje4BgnpRo_ZWVGzxSi1yDTgQqrKgPbl2zpFuD-nIG9hnV16pXLGUYeK51lsgFPOy4y-qLJNKuA2Q7K6_cLfxbB83Kx7L8QGpmdkezbvKNBcjDrZnVHY7WUeUNzH2d6vIMSULEa-7AbwkQmmSJZ8L4yby6mDmBN_c-HHE0znsB0C7Oo3aFEzMB_oFLmetbTlSJB7G8I0GpBhypi18tyLgaCzHPN1TGEotzdY_-o3KzAhsPqnKATxB8cLbRaHRxSDjhDlUWqwFubFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=BTMBpRUBU626m05Kr7mXbYM9f9jgKcUBtydmjYZ2fkGN4MNOangvfefkKImcIcWL87C8_yrEvUkRwBfFpDmX71jLHU_yl85KbI8_90SL_EIACn-KLThIHXCBH88al43LgzDmMEvoQeq0O8Au63UUGxeIhBrM9kFqe1kce-7mLXhOyIY2uKT4vYXU-lAGUhAgFKA_lyT8P3COxgRo_fe6oiZvHBUcuqqo9hRmNuAkEwpGchpC-CqjOTQYYUmp6MNr2Oz78nCqPeWLfVa9-Bu2NhBH6LqpRbCDWgklcdkU956lqTDqkYWlF4z-16e6ltPTUE2tDsNDQM2jtU78cGj0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=BTMBpRUBU626m05Kr7mXbYM9f9jgKcUBtydmjYZ2fkGN4MNOangvfefkKImcIcWL87C8_yrEvUkRwBfFpDmX71jLHU_yl85KbI8_90SL_EIACn-KLThIHXCBH88al43LgzDmMEvoQeq0O8Au63UUGxeIhBrM9kFqe1kce-7mLXhOyIY2uKT4vYXU-lAGUhAgFKA_lyT8P3COxgRo_fe6oiZvHBUcuqqo9hRmNuAkEwpGchpC-CqjOTQYYUmp6MNr2Oz78nCqPeWLfVa9-Bu2NhBH6LqpRbCDWgklcdkU956lqTDqkYWlF4z-16e6ltPTUE2tDsNDQM2jtU78cGj0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdnZ-Jz2a1YmP72-XQsBApBcLb5dpKqTryN_ecl9HitXyx2c10g1ZANzeoCMlCZ9M6YHxKgHzp2QXjnmSt6lJ9qcIAp_hu-yIwIc15GolguHATm6dUq2qkOxcWT9txvQNZEIT4pDeGa-0XuytOpGx5nN9MFpHjTZsYDAa3WY8vvOObhAy-_e-f-6DrUhE5AOCT_RIcPX9Bepy9rlZYMWsinIwLE0i7RiQYqZKcqE6a9XwJtoJQEcdiketWGN83k_N6WwXGdMt7n_aN-zEWb5aryCtc7nCt8Tf6k1tX7M11v6alfH23zsXEx4f4oXS3YgmlfZI8AyTa4QcHxH90s1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGtMNuCRLGR05c4g1c3nx6SO397_kOcFCMBAf4m1LJiOMEVyyRXbNGrvExe1w8TX84yMd2fGEW2TMuKWxbzCuVBzAx0rfziga7BjH1x1gVywwZB5k-YrthJqbwz4F8Yq1GXI2mZZC-Yp4dh33FHxgwu-Ap10cSGl9bQbBero3HCwrSN136vPxfg1im-dSgHiftKahNiHcy28P9ljhJVdf3q-C9ntl-Kp5hIuiPX-1VSc9RC-0LuOe6MkmRMCEEfS4qnotmcZljs03rAL1nAbWMzw6bdRCGZH2_NlWHxJmuIy-Cc8teKlBn8rHQHXPeW2jfT5D8Le-b9_rJa7A_wO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=r-DwWOvNNZsoGy7-Tm__O1c2twJq4UiCWNNL-kTMDrDjGQjSa87o5UGcYH-b33a2J3aFNUgWmOkyM7io0XnAWHLaZGuxXEn5qISnIihHHtocwEKWZ999k0Hk1omqoQBCx4GTscvC7_pglILEsfsfivqcwyAzOobOHpfpEwAPeh7UUX_S5PGNBFkzyoRRGnFdS85BQojV79s0wkBr2Y7IbaD_2FV2p-McnNA20POrUuPodmmaHgH04O2IrX694PPdIddbe4XPbO5WXWP4WS_UQMjxfye7v9sXf_Vk7TNS5YHvtlrXRcm7Hlc7MkrqH5A9BgdvLoeWYNyvDkLffvQfIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=r-DwWOvNNZsoGy7-Tm__O1c2twJq4UiCWNNL-kTMDrDjGQjSa87o5UGcYH-b33a2J3aFNUgWmOkyM7io0XnAWHLaZGuxXEn5qISnIihHHtocwEKWZ999k0Hk1omqoQBCx4GTscvC7_pglILEsfsfivqcwyAzOobOHpfpEwAPeh7UUX_S5PGNBFkzyoRRGnFdS85BQojV79s0wkBr2Y7IbaD_2FV2p-McnNA20POrUuPodmmaHgH04O2IrX694PPdIddbe4XPbO5WXWP4WS_UQMjxfye7v9sXf_Vk7TNS5YHvtlrXRcm7Hlc7MkrqH5A9BgdvLoeWYNyvDkLffvQfIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoEbKJIaXiSS9RuX-yQv5g2BJq_mQU7o-cR_yReNoBK12SsQBV3vOAt14SC5d_Ph50-hDcHrICZFT5Ch5O4EnfGJa5GHDa7jYwulEdN7rwJcnjva5nOtwpIQj9AtsO-Z0wqzuIbdyYawqE80m42QJlXiaMhWlMTCA3GCbcodPodV_q9Eh2jGgEpEeRGAjrYmxHANYLlg69jlfmCSUnPkLy1nQ4hqXudoPE0Jsxq32RDLOnUQmC1Trzgg2w_o0NL3xfR7Q21Zm1Gyc36sxf9BbeaBvVazi1UjEcTbeY3sMfZhAQzyvJ2EVUYBxqxKh271eQv_QABWsZ1X3o7SINwjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=K_PCOW03nyPf1Q39gIgMJTowWaWvG6QdzIZQ4YMbTgmYIGB6wfuxPN-PsFGWZGNx38Nugh3x4W8HPfz6brNRdkmU8Ux3pX7p2ud6o00j8xMeWE5-k-2Fw5xyOXRJtH34cwT63PltayTfS77KbtKO48nq6b_mhwvDgXKLxeQrG3TQqSOLioxgqAMN8CB80H4L9WSifor6H6n2ofXgXMWNNzSX2ieYfs0b5K3wALuG84f6Sx598gKfS008gmsR0Kg4F1YReWuZwxeGatAVT3394EZpIhu3KhqlGGUqG0X4qJMEjyx0PLtKohdnaOo5VCWt6ndXkl2pdZUlzxsHxvn-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=K_PCOW03nyPf1Q39gIgMJTowWaWvG6QdzIZQ4YMbTgmYIGB6wfuxPN-PsFGWZGNx38Nugh3x4W8HPfz6brNRdkmU8Ux3pX7p2ud6o00j8xMeWE5-k-2Fw5xyOXRJtH34cwT63PltayTfS77KbtKO48nq6b_mhwvDgXKLxeQrG3TQqSOLioxgqAMN8CB80H4L9WSifor6H6n2ofXgXMWNNzSX2ieYfs0b5K3wALuG84f6Sx598gKfS008gmsR0Kg4F1YReWuZwxeGatAVT3394EZpIhu3KhqlGGUqG0X4qJMEjyx0PLtKohdnaOo5VCWt6ndXkl2pdZUlzxsHxvn-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyNsh4RwWiG5ubZar5uI7aGuXbKp7Ql6bnjHhQLcGkiq4pLhsjRg2gPh0ddYXaIe6_oPFaPTwXitrC2uaTWTKmxbQ7epGY4lIY3I72sz03ZyHWKDsLzu6Gn5VKWa_FvJQlwrRvESOSlSAyH8y-QCnrP2OxFr0L19Cef69LDkOSAudq-Vsc675hsUpWVZr1yPqylyIKZcw5xzLjFsCYR-io4MAjQ7ZeLydHNLjmQnAjZ26VfodKlz8VX6DzY90QbzmyrIDRmA9ADHnt8ccBSZlAS3Zsc3ELDMxHyNxSaZwvyQbavrD-O0bKs6GKvNRk2i3DKkuBRkO_D1JySAYFkOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZDr5x68aFsf4avVgle9pc-6AYeEVJPI0S1EH80ZHpoRnYZWve5RIAMT2Dy33hN2LVhW9leMC8E6UiAgwQ0hsoxOgM25gaNeZGJhkxikriKxRFk2vLClr-RWteLsmmeDk4sRPq8YGo2FiOAPesh9H6KH5baXoOM-zWY0II1pXifwEecziHg0aaPQ5fI2MPYtY_XSSSQGpZXxqrcbcXfwfPq3CZKlsYbD8te0bMqcjPwpO7MC-LNeWhYcqbOwTeryQJ9s3iV_KsYr2sg8eRqnTvY5u3maaezWOwFkhStnfzyeeliQZZCoNKa9aDqStkSasF_g_58LirlDiJr10WsCTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACv_v4yQU6-KFTGxUjXJdyCE6CRmBPRTqslLClDVWo4_kKJX9VZx4F2JXV58-wAYehaTKigodGLTiSt_aPJO3I2eF_oM2qivPcoW3XJqqUy2VlS5eZJczqYd74ere7NrSsVsgMQGhb8pldr6BVaAQBtDbvof5obCrEgwu1xFbvYVxx76brFAC3sByPyOoDukBLZuJeGaWB-pwRanKTJrJvLHXv46rstYjxEgjB0aT803Ei8wpfipHaKP6iH02Zhby7Ku5gU0yBxPD9oQE9ee8uM-kS5OHOgxAq-s8fyOenzsqzcRHx9J2xOQZyD6yAmjT7vs8GwZ_YuF-EXafokd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTqwxlWemjmXt6UsZW_kmPOqL9r-8o8y3uPhg7XQuV3tJF2bwAHDMOylyKCEV5B7H2HzUDOp4URybeC4BjAgbZlb_EIDrb99Rq_0kTAiGUoTQqzXf-f76W9cH8nv7mGb_9t1TG6sMxjpa_w4zgZGtWF3PMRCxEbtuoxiojhzBkPFf9YjzSb4jPbksp00xTqXyHM_O8P0WfHQOskS9KP_GxKMzaPNoK32P0lUqaGqbGwUBQfj0MB-l2B7iUXvppWRSFCIBeU-dcUGjNgnv7uqQAvTKn0-v2zCMvR3MpxQLRmpOGReVXoSphuJQzzyPN1Og2dKC5DLqa0wwd0NnVoAzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=mPP757NsRhhn3cyIDFjCyxyKzICdBpZ9yw7-FNu_0_BAcCERn2QI_LPt5dJiM-SBAtEDi_EBGBK0k6JupqOV0jpC-9ivTK8xh_znNZBr-dyME97rZFYNNgg47u6Rw6poKvcvyXK9EifJNlV7iCXrPOYOv_H-HrQSC3BjtH1OD4mw58hDt2gKylbT9sx3T6uJ3AJ4XdwNVn-nGbBrZwLoa9Yp60gNfcb4h87GKvDUMmPBfeAvv1wdQrbFUc04bgCpo_O46Uj3OUWKJrVrIrtrCZ9BsQEVJ8e9OiGUM6UTRP4AS4gvjdRKz3lLZOTUqmfjVgAUQGye1fz3fkeMSc8dYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=mPP757NsRhhn3cyIDFjCyxyKzICdBpZ9yw7-FNu_0_BAcCERn2QI_LPt5dJiM-SBAtEDi_EBGBK0k6JupqOV0jpC-9ivTK8xh_znNZBr-dyME97rZFYNNgg47u6Rw6poKvcvyXK9EifJNlV7iCXrPOYOv_H-HrQSC3BjtH1OD4mw58hDt2gKylbT9sx3T6uJ3AJ4XdwNVn-nGbBrZwLoa9Yp60gNfcb4h87GKvDUMmPBfeAvv1wdQrbFUc04bgCpo_O46Uj3OUWKJrVrIrtrCZ9BsQEVJ8e9OiGUM6UTRP4AS4gvjdRKz3lLZOTUqmfjVgAUQGye1fz3fkeMSc8dYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=R3-oLfBTM2RMqMK3mUZHTc-YiS7FOxcAXgViTVq_G_7KwX31tM4y6Um8CF0UMD7p155KzAVoUYxcUtHyx8AJfNAvyFsnxpqxbkzuyAqkYNr7y3Kyt_1kDHeYeqgMsmOF-EALJcCywg_hPFKbc5u6e-6z59RJCx-HHtaMKkl_0-Unm1hFCfD2asUhdfldoNNpFhLfZCOU3QyIVwNPA22FQnOIAnfWnGB3F9FkCh8NBEgKNbVAb29805T-aZwXj-n-6tNbw-yS1lBCT6c95xO9pQJhEDzNs0--ITTJ-kjw90hfPPvmA9OzaK7EAUR834ctd8YqRmwp3vo7sa0wwn3koX4r13lwsJyj6wRDzBn98T7zirovNle2-XD9Usq-zcxXcmgzgGso3WOldX_pAG5jYTWieflNu1uBcFzc8rWZhkQvxKivTh31vYFNi7b7-Z1E7KssfOF0Ze3E9a985Jnjrq2XAmA98uEG4NmvYiWdQeWknM4rw-pvZ0wiCTBPtvcqrGBZ9YIgaKpQSWvGkKRo-FbpWVnOyUrSU5Nr1OR5ctab_OA4IGeT9jR9bT8BHMarMBv5G2Bong7LZX9c752s08f5YHnWBjCVE298DhON5Sp6E7KYFTaL3014Dg3HSnS3ecnAsW7FY-a3xT9zAqHyx3QeFvYuhGOKeBB96F0qEwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=R3-oLfBTM2RMqMK3mUZHTc-YiS7FOxcAXgViTVq_G_7KwX31tM4y6Um8CF0UMD7p155KzAVoUYxcUtHyx8AJfNAvyFsnxpqxbkzuyAqkYNr7y3Kyt_1kDHeYeqgMsmOF-EALJcCywg_hPFKbc5u6e-6z59RJCx-HHtaMKkl_0-Unm1hFCfD2asUhdfldoNNpFhLfZCOU3QyIVwNPA22FQnOIAnfWnGB3F9FkCh8NBEgKNbVAb29805T-aZwXj-n-6tNbw-yS1lBCT6c95xO9pQJhEDzNs0--ITTJ-kjw90hfPPvmA9OzaK7EAUR834ctd8YqRmwp3vo7sa0wwn3koX4r13lwsJyj6wRDzBn98T7zirovNle2-XD9Usq-zcxXcmgzgGso3WOldX_pAG5jYTWieflNu1uBcFzc8rWZhkQvxKivTh31vYFNi7b7-Z1E7KssfOF0Ze3E9a985Jnjrq2XAmA98uEG4NmvYiWdQeWknM4rw-pvZ0wiCTBPtvcqrGBZ9YIgaKpQSWvGkKRo-FbpWVnOyUrSU5Nr1OR5ctab_OA4IGeT9jR9bT8BHMarMBv5G2Bong7LZX9c752s08f5YHnWBjCVE298DhON5Sp6E7KYFTaL3014Dg3HSnS3ecnAsW7FY-a3xT9zAqHyx3QeFvYuhGOKeBB96F0qEwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=UX8_FpCMb-d2K1UEdw4b2GC23gYUcLjSgP-2UU5U63OlV6z8bHBJq3-2aT-G3J8mm5iPulkB_FYGA4lGyMELtbUiuFCgFnUhnPON1fjpitb3JukMhQZybCzOCYwzJNvZx6SxkYRIY3Hzkf8kIdGwhqkTyg-HwMaww33xjnMpPiKDKnx1OyATZ6eyC8ITjL0P9ChhBm8Ol2Br4C1Bkr5q1S4sEc90-VZ0BukHEsesSX_gMkTbHyG1CJfeo5K7adhArRnQEoLWyMDevKFSB5efg5B_lOWueejgZhFAPtKKlwWiGXtNOznz6OMQLAZPXyfbV_UO8ykSQ-XJK8hj4DazGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=UX8_FpCMb-d2K1UEdw4b2GC23gYUcLjSgP-2UU5U63OlV6z8bHBJq3-2aT-G3J8mm5iPulkB_FYGA4lGyMELtbUiuFCgFnUhnPON1fjpitb3JukMhQZybCzOCYwzJNvZx6SxkYRIY3Hzkf8kIdGwhqkTyg-HwMaww33xjnMpPiKDKnx1OyATZ6eyC8ITjL0P9ChhBm8Ol2Br4C1Bkr5q1S4sEc90-VZ0BukHEsesSX_gMkTbHyG1CJfeo5K7adhArRnQEoLWyMDevKFSB5efg5B_lOWueejgZhFAPtKKlwWiGXtNOznz6OMQLAZPXyfbV_UO8ykSQ-XJK8hj4DazGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dbb-8GYOiz7KiBE5pwavROy-vQgZwTJQTij1Vq2jx5ZbiRS814LZLlMKQasCFj5zaHswPIb2MEEtFcLdcrz1DL5xDWmkFiA2nibuxiNC93_iZQG6hEgoZJeQK94ToRoblTq-Y4fZEWb7OXGxCIEcXSWo6czQPsvovMhiUcwaJofBijo_dACozN3JcZ6ff-UPWNO8ikf2XgQwaQnWgWEAi9TA_wk0Hyw0AVAvnqfO24VaAfIzC6seiJ-GLTf7SwzVrE_9ICyIzPBcvjvAHBInlKW7ACFJlYEsD9mcbgB7FJPuieCyaRqatBK0zraHsZT7SGLohEtzNgH6xXo6tIsUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=dbb-8GYOiz7KiBE5pwavROy-vQgZwTJQTij1Vq2jx5ZbiRS814LZLlMKQasCFj5zaHswPIb2MEEtFcLdcrz1DL5xDWmkFiA2nibuxiNC93_iZQG6hEgoZJeQK94ToRoblTq-Y4fZEWb7OXGxCIEcXSWo6czQPsvovMhiUcwaJofBijo_dACozN3JcZ6ff-UPWNO8ikf2XgQwaQnWgWEAi9TA_wk0Hyw0AVAvnqfO24VaAfIzC6seiJ-GLTf7SwzVrE_9ICyIzPBcvjvAHBInlKW7ACFJlYEsD9mcbgB7FJPuieCyaRqatBK0zraHsZT7SGLohEtzNgH6xXo6tIsUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAYES-3LuCoT-61ZNcJ6hx4SBMFA-u_eWyTT6-w661y0gOU93_uW_nTjfbtxvHM1UG-dcpKjCEBf4tuw2Wv88ZQJbfAoin3EfYlvogU0UBlnh9HvYVZAVr2rT5FqayMX3b1DyFl7Spmvx7WTIyWI4R79PeOWgq8Z88_UsW6lTH8iRMQPVDUiOgw4Zm0fuTq6vK-DtQ2DZkmEfzr1g2231CSFK-uiyrQimZXxUsxe1Lfs-vlsp9p9qeSW5_VDUYRVLCDlSTE4CkqyAoa-Mh-LP4Wzek6toT255z-6rQRlWVyn1cH4QriRW8TWLrhbos0blVp9JBJuOjo_D5Zqu-yv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=jnvyYo4LKjEldyQHv9eWnFbC2fYB1-4JiEV5GKzB9sF8Y7UcXFwF2br0JwiTb-jRSw1V39HJ5WI6Emi0Iw-lJAJjqkl2WDdPlRLeuY5b9yBN8Vi48kagKT3hDZgdsV8qmizu61cVDd7wTaorBYKkdGy3SzdOP83axAEXNctMW9-PnR_hoa_V8oefMoxYZfccZBiOOpPYo0tWEiC2HUUz9Dm0X0CSE-M2Hmc89PhuEniu_CjvsfOvo68RW7LyocVXy6T8tRKsMqpeHSi5oAdJu0L6WUEyGh8PXZGUwJnUjkdmo9G3daBp2HfaUHPBuTXHPV58kVn6u5yQ5pn1Ufx7gX29nUE25k8XglxvLHEmChV-fQtzi5qLqghofxQEa9al5iB_tyDuWKflXfganI6roEZ0kjg5I5G3v_i8oiUhLMcp5XbTDLnD_OQ7Oowk90p6cmPNSUp3kg2_-ED3FDxmCTf5YCR5DrTQ9AFPKBP6PbJobOiluolVdIR0kl_h-Rb4T9pIv8SqM4NTh9RkOPZhLIZs0jYmleK3eCBUtQZMBVZOHaHRAMgPXklWuN-rk-EqIZYTgDI_CgAomJI9p5UgS3dakEiNFFLhHwRAk1zFUYkeTxRbUeicBj71KN5E4wkna-opgakwuazjX30JMpdlV7CFpJmAR5-dSCqpxTcx1mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=jnvyYo4LKjEldyQHv9eWnFbC2fYB1-4JiEV5GKzB9sF8Y7UcXFwF2br0JwiTb-jRSw1V39HJ5WI6Emi0Iw-lJAJjqkl2WDdPlRLeuY5b9yBN8Vi48kagKT3hDZgdsV8qmizu61cVDd7wTaorBYKkdGy3SzdOP83axAEXNctMW9-PnR_hoa_V8oefMoxYZfccZBiOOpPYo0tWEiC2HUUz9Dm0X0CSE-M2Hmc89PhuEniu_CjvsfOvo68RW7LyocVXy6T8tRKsMqpeHSi5oAdJu0L6WUEyGh8PXZGUwJnUjkdmo9G3daBp2HfaUHPBuTXHPV58kVn6u5yQ5pn1Ufx7gX29nUE25k8XglxvLHEmChV-fQtzi5qLqghofxQEa9al5iB_tyDuWKflXfganI6roEZ0kjg5I5G3v_i8oiUhLMcp5XbTDLnD_OQ7Oowk90p6cmPNSUp3kg2_-ED3FDxmCTf5YCR5DrTQ9AFPKBP6PbJobOiluolVdIR0kl_h-Rb4T9pIv8SqM4NTh9RkOPZhLIZs0jYmleK3eCBUtQZMBVZOHaHRAMgPXklWuN-rk-EqIZYTgDI_CgAomJI9p5UgS3dakEiNFFLhHwRAk1zFUYkeTxRbUeicBj71KN5E4wkna-opgakwuazjX30JMpdlV7CFpJmAR5-dSCqpxTcx1mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=HKdE0nAnTUEOqo4fYnAc4I9wAsEbzyaiM043l4MW-nGuAdeuVbxxSwk1m61iuv-WXlPNzyrylWxtvzcxHE6yqO7YpGMcLjJInAAYdzomT6VTNL2unZgYnIk4av2u2TT2YX-eqYeb8w5vxxCHsmXhWP820ydP5FqqsfNvoPIpNvjjfc7xa6diZmVmS7r5pxJBlOZvgVjxx_N8EzJ4OwUh0vbh-bMp5qfD8CBq7rKphqK9NegUhKbOT2DSsfkLmxZdw2aQ1yRSWSx0CVf1bXMnyJQw58U-CxtBzPgwp4ASsmrNAhp7TP2fXOEKDRiVOaX-MJBDHBfQ4aXBcYry1f0d-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=HKdE0nAnTUEOqo4fYnAc4I9wAsEbzyaiM043l4MW-nGuAdeuVbxxSwk1m61iuv-WXlPNzyrylWxtvzcxHE6yqO7YpGMcLjJInAAYdzomT6VTNL2unZgYnIk4av2u2TT2YX-eqYeb8w5vxxCHsmXhWP820ydP5FqqsfNvoPIpNvjjfc7xa6diZmVmS7r5pxJBlOZvgVjxx_N8EzJ4OwUh0vbh-bMp5qfD8CBq7rKphqK9NegUhKbOT2DSsfkLmxZdw2aQ1yRSWSx0CVf1bXMnyJQw58U-CxtBzPgwp4ASsmrNAhp7TP2fXOEKDRiVOaX-MJBDHBfQ4aXBcYry1f0d-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLSOX13YxLNeJzYYvWf-jV-4OEwBbzr114Kwv3flv0YBpc2Hu-b2QmIPGpOxOIbEALfsTz_MYtxI9KfamwJGRrtAUY0PNIqYfLZ2AYXJCY6N158MtPCZQ6O67hXkKpXjlu9SlmL-1VDHwafX1nRt_ISFAKPRZ-NiWG5d43ioB6TSLvE-8ap97-7nNSWbtbqlRXjY2p-npNZWc3qrqU2XUJcVlU6zhoobywEqiwryo3Ig_BjLUKKJUJKx5xCvuPC_RG0gBelEqQFjMK4ZTTwxJKWNKpFnEu6yaIMB3Qq5oXFphJUBf3o_SMkpgTfu4Nl9Pv-h5nFLr1CRBCM39qIdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
