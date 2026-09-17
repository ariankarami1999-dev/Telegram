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
<img src="https://cdn5.telesco.pe/file/HqdC4bgWskGZJxx_xBP6jCuMbb4C5j_9yeTXCiyxqR9SQWXoPx3EyNJHXDGnXu7GmMT6Ew-Aj5ETYAqMyNxQZFWvqtK4nh7MKf0HZ3VveAgHQEPw8qH7ZTKWcUt8gwDxDrDzMYbJsdGFpfYfLu8ikOkN6W0je_4h94uvPHUndzLtg5FPxMYbPl5emUIZ7JV2GJbjILoOONsdSMzzdIDRDEr7oWr7-DhFqBf7twvb9DxvyvSu-bnOWHdxqZ_7TeeVOCKvcyALsiqYfmclFTSLFqizvY8lbUp4ebA85y64LGdK_cctn0T61R35CsO34BehtmHCe6x_KzZC6fb9atTTLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 410K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-106778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnBp8MhxebSL4riv00h7Tx7uqnELWNQUbaDM2jUv89QE73qjvkmyhCvpjasRaTh-mReciqmT4jrVrTSEEf0KkZNl6RTqmh7JUfxWl5lfRbVuReBJkJ1JeORzMRgTzmO-t28LeLHJ97sDAC3uU5a8gnjQ_uEltdw6dgY-UERNa1oY3ESokdXgHbWHLRaYKFSFm5OFyCE1nakEcV1nBeB-FE5gNq218sdKDh7ZvAmTt1sux3ssx4p0uBUKITsK4deEwJ0End9IvjgOjiMHfFRju9nWPGE_ndejxvrQBjYDXK2BCWzc1UwblwBjYMW7TcrQUG0cmNpXGSvrZ_6rwPNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
⚽️
هفته اول لیگ اروپا؛ ترکیب لخ‌پوزنان مقابل کریستال پالاس با حضور الهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/106778" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
🇮🇷
🎙
صحبت‌های جالب نوید استادرحیمی درباره عملکرد درخشان یاسر‌آسانی در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/106777" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th1VK9RyB4H3kj6vqFDexxESdBx-CiN4KhjELQy8awm3R7IGPFHL3cMtjT0h30vE68Jvn0oL5r6p0JdLLBI81Lc4grTk9pJaaxHmmgevm2dpErUmKALyMaKN5fPcfp5op817RTywLTrcJFQLlBc0u0CJuylz6EEQhpi2srVZJ8oZf6JU06C2dsAJQk0d2qCfDj4OdHMRJoqJxi58Xd9c-TjjAMFaXTI6IF6jubXckTP315jetIXPtY-l-99xVUXgM5INWik1AgAT8cWnEZqyvUiOeN1DFGAqroHm6R5SEuNijjDwii7X-oejk7TmDENqtLqs7MqTuVd6oWGeuj3ocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس؛ ترکیب منچسترسیتی برابر نوریچ؛ ساعت 22:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/Futball180TV/106776" target="_blank">📅 20:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c416616.mp4?token=DO6rAmM3S7g_-zOdGMYWeute3XO8wDdRZ7IhXJ4u1vEyBnJAA4izZYOw514S0lbs_H2MI6YYXgIUiCd4kTnqtMPuRhDGMJyp9ZCAtGxSHcVqgkb03IZZGVBXBHLOArdQClruYdIrRbVoYmAfERv7FGeZ9R0Bmi34A93guNOBEhanVe69QVYx5CQoqGrB-HRDNhzt3SvDXppSWushvmOP60fSo6dwQft29WHNFjIrdgiMbTicWdwZYWMR79jHeTcAF66zleURvBJ8QJrN_MSW8WL045ERW7SCFuhOj9FCU_g_L0ROEhb8qZNvefP5rP68uXsCOfOpzGpaIoQjp-w7PVI-mKI-FRh3vZgOESLJPS2pMbFj4znRYdU5eyvP5XAVffdVntrTLQSALOqXG-o3i8pyZ-CbvaJDCy0tlffr8_JyMZACRCpd_fpiHgTca2KSmx7rb5d6plP64GFmD8mTmdGwAoqaMhCMiHG5DGctiPFs5OLjkvEVu9cvLry1Po18FkgQfjrYZ6SM5XltGouVcUCjc5pMg3b9x6lyGV-tWZl-uf5Gq3CvZ_Y31Fp5dybTenZm6WTcknMjtFk3bYBZk0OXhh6XdjsgjEXfW26FEEOxqRfWqdEQjDb_UWDluipb7SyaCotSjpS4pPzX1guwz-QYtjSJoqkc8H_9Pzl8jpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c416616.mp4?token=DO6rAmM3S7g_-zOdGMYWeute3XO8wDdRZ7IhXJ4u1vEyBnJAA4izZYOw514S0lbs_H2MI6YYXgIUiCd4kTnqtMPuRhDGMJyp9ZCAtGxSHcVqgkb03IZZGVBXBHLOArdQClruYdIrRbVoYmAfERv7FGeZ9R0Bmi34A93guNOBEhanVe69QVYx5CQoqGrB-HRDNhzt3SvDXppSWushvmOP60fSo6dwQft29WHNFjIrdgiMbTicWdwZYWMR79jHeTcAF66zleURvBJ8QJrN_MSW8WL045ERW7SCFuhOj9FCU_g_L0ROEhb8qZNvefP5rP68uXsCOfOpzGpaIoQjp-w7PVI-mKI-FRh3vZgOESLJPS2pMbFj4znRYdU5eyvP5XAVffdVntrTLQSALOqXG-o3i8pyZ-CbvaJDCy0tlffr8_JyMZACRCpd_fpiHgTca2KSmx7rb5d6plP64GFmD8mTmdGwAoqaMhCMiHG5DGctiPFs5OLjkvEVu9cvLry1Po18FkgQfjrYZ6SM5XltGouVcUCjc5pMg3b9x6lyGV-tWZl-uf5Gq3CvZ_Y31Fp5dybTenZm6WTcknMjtFk3bYBZk0OXhh6XdjsgjEXfW26FEEOxqRfWqdEQjDb_UWDluipb7SyaCotSjpS4pPzX1guwz-QYtjSJoqkc8H_9Pzl8jpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
توضیحات فرشید اسماعیلی درباره چیپ معروف در دربی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/106775" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=gr4g88Odo5GPOJqLrwefMxA5JbPQwaLWGn1Oa6jCXUQkkk8k3tPAhJJIWO3x7HFhDpXmoVX6KtPYIT8KQ-mKUZ8Dkg3L6dgXl8Z5v9xl91NUQozA8_0DP71sgk_8AQQPB7sqw3EuwbpcdQXQjt2f93QV7wZH9cJTY_XqAi3qpjFokzC0k5tzS0Jsc6FIMcWBwMqA785wZxZFbEZ7RKRa_h9lUpWzpWS8NhUe3WuBBbvTg0v6FNMkKjeevvJwI8CAy8VaHAbwz7kwkV8N4LKc0e3RGcq2ECmJvW1kzKe9yX6taJ0Wcrv66gLwloLti1xgOhJJuBXuvZ6q452FlShRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=gr4g88Odo5GPOJqLrwefMxA5JbPQwaLWGn1Oa6jCXUQkkk8k3tPAhJJIWO3x7HFhDpXmoVX6KtPYIT8KQ-mKUZ8Dkg3L6dgXl8Z5v9xl91NUQozA8_0DP71sgk_8AQQPB7sqw3EuwbpcdQXQjt2f93QV7wZH9cJTY_XqAi3qpjFokzC0k5tzS0Jsc6FIMcWBwMqA785wZxZFbEZ7RKRa_h9lUpWzpWS8NhUe3WuBBbvTg0v6FNMkKjeevvJwI8CAy8VaHAbwz7kwkV8N4LKc0e3RGcq2ECmJvW1kzKe9yX6taJ0Wcrv66gLwloLti1xgOhJJuBXuvZ6q452FlShRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خوبه قبل گفتن یه ببخشید گفت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/106774" target="_blank">📅 20:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=neAcXEKJt92mxIZsBsHD2baIQSkNAUFi6ht7kqEdKp17sGZhbiz_QuspEq3X8utzuaerE9mCLVkpX6gQG75nDKHwBrqwgOc-YOF0nP119f44kPPbp86irZbIC9DMY3V6HbG_wKQQwAXSSonC_bEd0yEMeROCb5QwXarvGBUYO3YAfe21i9BeZoe9K74E75ehphqlQ4xM_rLkRISnKPsjam0g4MTN8ivH0LEFbHjc2KiWvL305MMck4Rrk51O-Tq9GkIF738SuvFHv2Hm8OWQAs6B70xwJvfIpVUcNjS1_uSwlkD40F_z7RdB4ldXP31xND0I4IBv_ATGMKoo_Rwp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=neAcXEKJt92mxIZsBsHD2baIQSkNAUFi6ht7kqEdKp17sGZhbiz_QuspEq3X8utzuaerE9mCLVkpX6gQG75nDKHwBrqwgOc-YOF0nP119f44kPPbp86irZbIC9DMY3V6HbG_wKQQwAXSSonC_bEd0yEMeROCb5QwXarvGBUYO3YAfe21i9BeZoe9K74E75ehphqlQ4xM_rLkRISnKPsjam0g4MTN8ivH0LEFbHjc2KiWvL305MMck4Rrk51O-Tq9GkIF738SuvFHv2Hm8OWQAs6B70xwJvfIpVUcNjS1_uSwlkD40F_z7RdB4ldXP31xND0I4IBv_ATGMKoo_Rwp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یه خونواده ایرانی عروسی گرفتن، بعد اسنوپ داگ رو به عنوان خواننده آوردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/106772" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrgyu0pQmzOeuKTMOFSP6fjmB97ekfl9t1hzbAsFT27hB3Q6Ps1HCEwi4HSDhN8RwBgoKpn92SD38RGWmjPTtkTxlS7n5HVqc953xVBxWsogJgl1Ov01wXkK1lNTa6eI03wVI_Cyn_2aVI0J2o1oPxi3zw9XFkGyl2yWtyhGuD-3EXyTk4Lrm4R7VVd5TP07VA9-uZpCvWFFBLNM4j9jrcy7XSl27qfLP30WaXLuGm1z04sfJEgw5_v41teXqZZ0rcYduuNbzixWutun5nzc0W3qoslh_wLbPxTgUpPY4Ssi5yMMRrgOUNA8j1oOLKCPPA34ZCFhncDBLhBSK0tby6SZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrgyu0pQmzOeuKTMOFSP6fjmB97ekfl9t1hzbAsFT27hB3Q6Ps1HCEwi4HSDhN8RwBgoKpn92SD38RGWmjPTtkTxlS7n5HVqc953xVBxWsogJgl1Ov01wXkK1lNTa6eI03wVI_Cyn_2aVI0J2o1oPxi3zw9XFkGyl2yWtyhGuD-3EXyTk4Lrm4R7VVd5TP07VA9-uZpCvWFFBLNM4j9jrcy7XSl27qfLP30WaXLuGm1z04sfJEgw5_v41teXqZZ0rcYduuNbzixWutun5nzc0W3qoslh_wLbPxTgUpPY4Ssi5yMMRrgOUNA8j1oOLKCPPA34ZCFhncDBLhBSK0tby6SZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇮🇷
۸ سال پیش در چنین روزی، کامبک پرسپولیس مقابل الدحیل. اون دوران الدحیل تو ۵۱ بازی فقط یک باخت داشت که اونم جلو پرسپولیس برانکو بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106771" target="_blank">📅 19:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=gNnBIOYymxAt_TkhmXmj1nGQBlnTPP7MAYQA0VMPZi1kXaD-zGo5v3jIZHa8UchY4mfkLBqmU4FLEjT_BjBu1IwEileHNkSRZ8uUzI1JnAn84nMeomWIzYO6szZbdBeAo-Z5fpeTMJFcygC7ltJh9nA8gfK6vniiPwUUAuiPXqOm21Wiovisu0o_0f3V8JU-UcV84xdnyVSNzcJdoq1CxGdMKZGHA15L6cAspJaTyg4sQ7a3N_J1jRzMmfxO4G6oz5aIJjclp6myaGsggdWT4n1hREpqdPqpH8IRCAKboU_DzYcOA5zP_50if4f8pMt-2GefDomWzW2suooSp3fzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=gNnBIOYymxAt_TkhmXmj1nGQBlnTPP7MAYQA0VMPZi1kXaD-zGo5v3jIZHa8UchY4mfkLBqmU4FLEjT_BjBu1IwEileHNkSRZ8uUzI1JnAn84nMeomWIzYO6szZbdBeAo-Z5fpeTMJFcygC7ltJh9nA8gfK6vniiPwUUAuiPXqOm21Wiovisu0o_0f3V8JU-UcV84xdnyVSNzcJdoq1CxGdMKZGHA15L6cAspJaTyg4sQ7a3N_J1jRzMmfxO4G6oz5aIJjclp6myaGsggdWT4n1hREpqdPqpH8IRCAKboU_DzYcOA5zP_50if4f8pMt-2GefDomWzW2suooSp3fzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایانِ عصر خامس رودریگز در تیم‌ملی کلمبیا.
💔
🇨🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106770" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=t7IG3VWm2oe6fCu06RdKDA5qbhg-Q_sv3zsykeQyNar3FXZr0KJPE51K0HYf8XRiVdjCUl8C7kzGztfG2WZpJHwMSoTd7QCbIdbcpBNj7rWmLMonp28lwbvXg-LhpvXPYhZEuucD4lV27jWMEpNIafG0ZZSdEuG6u4VhC380Em_WEhnMbEM7dSfIaS1BRNrBBaWc_2lUIXAqWZ7sU5lkuhGjQjLpuTjY5FS5uLJhFVpK_4fDSFGouO2TzpEwBUjNpNScbQU94uWRpqNWxKVslR-2S2bYFi3O0QDJX4CPLBzCcBqK2W6UnYsTzLQ9hMxsWcEBFuMALDX8NL8jBXyowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=t7IG3VWm2oe6fCu06RdKDA5qbhg-Q_sv3zsykeQyNar3FXZr0KJPE51K0HYf8XRiVdjCUl8C7kzGztfG2WZpJHwMSoTd7QCbIdbcpBNj7rWmLMonp28lwbvXg-LhpvXPYhZEuucD4lV27jWMEpNIafG0ZZSdEuG6u4VhC380Em_WEhnMbEM7dSfIaS1BRNrBBaWc_2lUIXAqWZ7sU5lkuhGjQjLpuTjY5FS5uLJhFVpK_4fDSFGouO2TzpEwBUjNpNScbQU94uWRpqNWxKVslR-2S2bYFi3O0QDJX4CPLBzCcBqK2W6UnYsTzLQ9hMxsWcEBFuMALDX8NL8jBXyowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
بابک‌مرادی بازیکن سابق استقلال: ذهن فرهاد مجیدی را خراب کردند؛ خیلی آدم خوبیه اما یه دستیار مرموز و بی‌شرف در استقلال داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106769" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_nwAJWRzqLJSrO-5_5hr0ug_9Fli4HOQZwyJBxjKSpnF42pxtWBYdpNYdjrEmoxAbLTMlJ1qKgogweIUWYD9xi7EtgAKreCEUp5YqbcN4JBvD5YIHoqRTmjDRsZM0OT_6NE2FsabG-CBwOR3N7owA3g3WrmphK4q5q0Dz1VQfeTdIEkBfn6T2qps5wLlM8JGNTZtgH-_W1DB7glRDGSXichXDfLhwNutCQ7OSd-Gn4W71-Wrvl4K3Lym5w5J0DPG9rEfKnDst8CEFfJqtTys56GxU1BnGcumlSnUqJhSk6fHM-VBfNXkxsWN1JqMGaq1tkgvH_UPBNx80ISkzDTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106766" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106766" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zihdd_Q1ZNA3cYxXPm8W3rqI2hFZE5PbZC6rOn7vfF5o375WWMjGIVoXhqoiJiFR4NyJa--XDS1bHmv-n8kpJ4d7YdVeOZXXXxoO-Tz9Ks0sjKNZ4z307U4ls0u6Uv3LXYbC1buoFUbswRiGsd7mwp5nhLi1Jd5ewg-RjcIfecszFTs8R2Nx1sGqtupXr3i-evue20pW1rtjCcqyqxKEJTUXgiM5q5uhBzQtZIYRD5u-ZLZg5_jGdAbNY6zb8uNsXhdSwHmyn4hKkyD-KGM2YIU2AVB38cswEHg9tV6VKE0QaSBJxtiVhHesFGOJJrFEkFMW2Tjmx9wKMvLNCE61iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106765" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=jnqM4q_XkTS0jLjlzAlIYMc4vrX2eK7zzoxEo3C7eJpMlJPFLVWyC2xk4B5KziaUIYnuOG8znIbXorCZ1DkXgy2lCOhhvuTw9sxcF-v8l8CD55bwtTisptpIx7MAhwNSXy-csn5PyoabXYLTp1dRjsKp44VwEN_fXAnwIrrxnByKHZbdSmhFqfLgWBw8lr-Hd6zWF6vGKBxcQrP5JpfqcWiv43QZ6dz8BhUnK9nMP8f9pxHYbFfM_S8LvDtycRFc11HiRgbQhL91copzcu0I8XZs2Xpbk3eLwGBL1wLTKl8K0GypOdCVP9DIFSXaeDQ7d0rMc2_NbVnhqYce7mC44A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=jnqM4q_XkTS0jLjlzAlIYMc4vrX2eK7zzoxEo3C7eJpMlJPFLVWyC2xk4B5KziaUIYnuOG8znIbXorCZ1DkXgy2lCOhhvuTw9sxcF-v8l8CD55bwtTisptpIx7MAhwNSXy-csn5PyoabXYLTp1dRjsKp44VwEN_fXAnwIrrxnByKHZbdSmhFqfLgWBw8lr-Hd6zWF6vGKBxcQrP5JpfqcWiv43QZ6dz8BhUnK9nMP8f9pxHYbFfM_S8LvDtycRFc11HiRgbQhL91copzcu0I8XZs2Xpbk3eLwGBL1wLTKl8K0GypOdCVP9DIFSXaeDQ7d0rMc2_NbVnhqYce7mC44A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmbddO631lmbAHaIdSDRX4I4_IbYF0QfUH8dImh3YzxOR2J_wnkhOsRFsXy77XHzP1ldk2u7WlWv6W-iO--35RkXXjbU8NLqZwlIyIpdV44GE_nlVwYjkIUe_0k5FEfcxWmj71vS9NuIHFOR0qyGSbT-dIbfAS_wiNZO9K5zuVGXGJFoD-56SdiHVWQ9SkNeAuBGjUPGUceThI47QuZRMSTNKTwWJLYoGdaj7bOMYwvxixZn7gWawTh75jDglIHEqUD9emZ9L54xqTrCdQxFx-Bq9HiCrLX9lLolRe0VvGQ4wTQ2ba3Ux3WalddGnkaaGUT8g23BzL6U4J9uWiV3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=sPVX7IXylE5n6nzH-zlwdsXei1skHwUswMSSG75lwzCSYN7Mz9HBfjT9_lWk73gwOZN_5dHAsWG8hu1sSJvCRRARnVYuuyFRMiaIC74JlODYEga2giATRywogW6rLsSmavaJLeRcOCawX9-85Jx7M7347JRJGxLVt2-BwJLw5xPc4KdZmVEHNHE_n9XFggF1iSDw-19__UyMUU4epmK5yNcuLtm8Xe_NkTUer8Tc6PUjSIMwETc-Uvnr-I49qEu4sigej64gaAmdtiWqK0G5gKT0aK6nxhuIVvRcX2_cUZ8qQy8pYSyGawYi1zneGL1blUITwW9FKot_HletbgrVmSYDSxUmr-U5ZRMRm3QJTcco2kEuVMDHjb1iCQHSnupKf6Or0PpjU-ydctL41VM9JFIdryDvLkOQwvv0NM5TMeJPILnQLYJ37HwYLteZyoTGfubDcRZsYAveOoMJvzf15BBqWFKYt2mw82YmVbrojPcjd9LU5kHNtb13Q28jcGjYASjPeo6sm8dWbFhNkYmwFj1iFq0meU1zBlis_psYrf70oyE5N2LumVQlCubY3sHUtfbOXSqgXXf1aU7MQE2nlIlcX9lEF4irBXh2hfoGFvRM7WHfH0XF9hiTFXC-j_qZeqUwD6oc3-g0GR3lYtW4i2qa9i3yaFFECkS8CFZlTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=sPVX7IXylE5n6nzH-zlwdsXei1skHwUswMSSG75lwzCSYN7Mz9HBfjT9_lWk73gwOZN_5dHAsWG8hu1sSJvCRRARnVYuuyFRMiaIC74JlODYEga2giATRywogW6rLsSmavaJLeRcOCawX9-85Jx7M7347JRJGxLVt2-BwJLw5xPc4KdZmVEHNHE_n9XFggF1iSDw-19__UyMUU4epmK5yNcuLtm8Xe_NkTUer8Tc6PUjSIMwETc-Uvnr-I49qEu4sigej64gaAmdtiWqK0G5gKT0aK6nxhuIVvRcX2_cUZ8qQy8pYSyGawYi1zneGL1blUITwW9FKot_HletbgrVmSYDSxUmr-U5ZRMRm3QJTcco2kEuVMDHjb1iCQHSnupKf6Or0PpjU-ydctL41VM9JFIdryDvLkOQwvv0NM5TMeJPILnQLYJ37HwYLteZyoTGfubDcRZsYAveOoMJvzf15BBqWFKYt2mw82YmVbrojPcjd9LU5kHNtb13Q28jcGjYASjPeo6sm8dWbFhNkYmwFj1iFq0meU1zBlis_psYrf70oyE5N2LumVQlCubY3sHUtfbOXSqgXXf1aU7MQE2nlIlcX9lEF4irBXh2hfoGFvRM7WHfH0XF9hiTFXC-j_qZeqUwD6oc3-g0GR3lYtW4i2qa9i3yaFFECkS8CFZlTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=OvF6vqKtTefManZpQ5VNECUSSP1diPMlc8SHwLnbnJ4n4Nd-QS9XVXX7PQbdfEfW4cWesm1YLZUfya2rnFiFL5UvUAR2_ZAUimpmyyOP6tp3NvP47-DFJ7Pjnfx4FqnQD59bGnfomehvMnfBKM_SmVKgUAkINAPeTNkOQNWm-TnVgshkQy5d2TKZLA0XeT9DmqhMQgi7Rg4oWVC3NDATa2eO7wXnA0xeOhS-m_94LuoDhPRqPzfzBC8_QR678oX2C9b1lsv_UVcHVTH0PruGSqMkTneQchdMwWyZt5eLuXeMmiBsaNWVObCOnHcQPyBoiPXUF6_fDnF6Ow4I1uUCB3qEb-fO11mSEF7CP8qA8zdt_KgsPyCpsLgdfsD32yFzqO2sJ5tiIr4HzuAZcCEf62FuzPn1mwDqu6S-yzTwWXKpRGg-iWoYvH01tYmvW2-Ug3xG38Hn-2Kp5OSABoD9I5P20bNZEE-GJLf8MEqMQJgcrvnwbhWe_bAOKG2cU0eYDXW7aLXB2-Byx1bJMJ0-PG7ZvBHaZ7mzVgGza3TOzMV_TqHJyRyWA11mZqExq6gfjzByPhIewPkxGOoJByCdq5UlIz6VTZQbJy1z7_KCOoAAP0Vam-KZnfDHVv3ZeynJtKW24SDUpj3lold9Jvn5v-Xs1aLqtSJqhV05KjtFtfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=OvF6vqKtTefManZpQ5VNECUSSP1diPMlc8SHwLnbnJ4n4Nd-QS9XVXX7PQbdfEfW4cWesm1YLZUfya2rnFiFL5UvUAR2_ZAUimpmyyOP6tp3NvP47-DFJ7Pjnfx4FqnQD59bGnfomehvMnfBKM_SmVKgUAkINAPeTNkOQNWm-TnVgshkQy5d2TKZLA0XeT9DmqhMQgi7Rg4oWVC3NDATa2eO7wXnA0xeOhS-m_94LuoDhPRqPzfzBC8_QR678oX2C9b1lsv_UVcHVTH0PruGSqMkTneQchdMwWyZt5eLuXeMmiBsaNWVObCOnHcQPyBoiPXUF6_fDnF6Ow4I1uUCB3qEb-fO11mSEF7CP8qA8zdt_KgsPyCpsLgdfsD32yFzqO2sJ5tiIr4HzuAZcCEf62FuzPn1mwDqu6S-yzTwWXKpRGg-iWoYvH01tYmvW2-Ug3xG38Hn-2Kp5OSABoD9I5P20bNZEE-GJLf8MEqMQJgcrvnwbhWe_bAOKG2cU0eYDXW7aLXB2-Byx1bJMJ0-PG7ZvBHaZ7mzVgGza3TOzMV_TqHJyRyWA11mZqExq6gfjzByPhIewPkxGOoJByCdq5UlIz6VTZQbJy1z7_KCOoAAP0Vam-KZnfDHVv3ZeynJtKW24SDUpj3lold9Jvn5v-Xs1aLqtSJqhV05KjtFtfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jscVdzDbDJbsYOjRWTyp7bDioksbcvGnQgzNjsUNpTcukrU5kl3F7ulT9AIqIQmQ4QqdLDQeftm8M0lTrU29VbWygWpp2v1BxPDLmfRM6pJ8Mac-Ub47sxc5tUVU7tzEsBrzcRCfSrgbyxSa3eJHaLoWBysq4vWJ0RpZF1nFGc2xiuPWmdQ_NFugniu-rlxQVxz15L5WR4dCY24plRQgSMv0DEjVHQUugPi5UNFzxgju0d1cbxIFYUF2bvpkhWrEYqFIp2lkZODQD6AaJ0CAgq-EZUq6qyAgXAted6jnro4x6Xf9kuN4qMUq0M8jBzxV8YIe1fuPg1nTH3zYUkprEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
سال 2018 که فرانسه قهرمان جام جهانی شد، کل مردم فرانسه برای امباپه دعای خیر کردن و نتیجه دعاهاشون شد این بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106759" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=U6maa61XQmWS1OVC-l7fhwXAGr20ExTl-IW4UAgF51l_ISj-XKHPyb497mQyBtUib3FMtbXKBvO_COFivDoGA7AEY5AC4nfLZ3T_32R-zqf0W5oITqj8kwFwwwdeZ12aoKWs8iVbYIGh9-qwaNUqAvehX0W1FUnYjIRGgGXCvQetgxVhKDcc2XEVzj8PaxeQ3Sei_dDYHh397B5XYh-Z9PuTpXNbHe-Aajq4gfvws3Sibu-bEB0GixCVuTvDTFriMJQZzOGQXMRWbR9q5B_HYgCHfvzBaYev0ZlNfiG-Zm6N_zkQWh5UepSjxgTvVV3Sp4NAtPni1IE4sbzFCoUNyEN5UJCL0FgrIpgio_r7gKhvQ7al4xm_xCXHQ0wN9QxaYZxkf-TB0YsCDeZwkYO5mKiNkc53wmKKU12swwfLquL0aJCVAmpOo4zx5JQH_qzoLwOZ4--CB3BUTMbDaPHKTWwNWtXITgQMGWIzbmBtDd4jWhjXjZesrG16yQEcy6L0zgy6GtRMgcHsb1Za_-K5J0f6QpDyMfvQJsnmSO2uHYyQmkdbtmBHhPVk32Lx_31Q2R3oB7LCTVsMkaoIOK4-8wguF4a4YQlcNkutWn31jLAzJqiP9ykqQdBkSnoMKv1Sn2_GoFStlA_J6wz6p5x0hurmmX0R9ivzfh_aF20dkiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=U6maa61XQmWS1OVC-l7fhwXAGr20ExTl-IW4UAgF51l_ISj-XKHPyb497mQyBtUib3FMtbXKBvO_COFivDoGA7AEY5AC4nfLZ3T_32R-zqf0W5oITqj8kwFwwwdeZ12aoKWs8iVbYIGh9-qwaNUqAvehX0W1FUnYjIRGgGXCvQetgxVhKDcc2XEVzj8PaxeQ3Sei_dDYHh397B5XYh-Z9PuTpXNbHe-Aajq4gfvws3Sibu-bEB0GixCVuTvDTFriMJQZzOGQXMRWbR9q5B_HYgCHfvzBaYev0ZlNfiG-Zm6N_zkQWh5UepSjxgTvVV3Sp4NAtPni1IE4sbzFCoUNyEN5UJCL0FgrIpgio_r7gKhvQ7al4xm_xCXHQ0wN9QxaYZxkf-TB0YsCDeZwkYO5mKiNkc53wmKKU12swwfLquL0aJCVAmpOo4zx5JQH_qzoLwOZ4--CB3BUTMbDaPHKTWwNWtXITgQMGWIzbmBtDd4jWhjXjZesrG16yQEcy6L0zgy6GtRMgcHsb1Za_-K5J0f6QpDyMfvQJsnmSO2uHYyQmkdbtmBHhPVk32Lx_31Q2R3oB7LCTVsMkaoIOK4-8wguF4a4YQlcNkutWn31jLAzJqiP9ykqQdBkSnoMKv1Sn2_GoFStlA_J6wz6p5x0hurmmX0R9ivzfh_aF20dkiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپر گل پریشب سوبوسلای به تاتنهام رو از این زاویه باشگاه لیورپول ببینید
🤌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106758" target="_blank">📅 15:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swzwFfJ6LsX6hht1srRvI1fPSAuwZf6ehIN07vzF6TLTNtXhFeus6ypQLsJJCP2Nsj221cu4i6PLQ3NgzdfB9jzejSa5Mt2Hd7CM87Y9T2iZYy1Xs66IPW_Jti90r_oelfJdgaB7N5FISnqnx-TYHUzT8qQZp_7FD6x0Wstoc7nZoXM7sroCwXVF61TW1EcN21pOnUqpzjRVwgKveaqisiDEhhFbKQfnteYdSIlGkqD6R0kZr_KO7RijXFJFqzll7AG7ygQuPjPE9LJqYnPXsbx7o7IiymTTe9y_ZSuJy_wVpn0zBmPs1WxTPv5KBDPmTNUPTD45syR0NoJIBRnnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙
کیلیان امباپه: "جایزه توپ طلایی؟
به نظر من، امسال زمان مناسبی برای من است تا این جایزه را ببرم.
بهترین کسی که از من دفاع می‌کند، پای من است.
هر چه که بگویم، مهم‌ترین چیز برای من این است که توپ طلایی دوباره به رئال مادرید برگردد. باید به سانتیاگو برنابئو، به هواداران مادرید، بازگردد تا شادی را به قلب همه آنها بازگرداند.
آنها بیشتر از هر کس دیگری، شایسته این هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106757" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=EfPa4ec9LGQEiL-l6m-b17HnASYyVzRPn3nOpW5m35FlyipA0ds0mYWz-SGXyxvsbBtjB_GVpEie9Gvki1Q7x-ZqBRIb2M8Mhqr5Shj6y1-iRzwoHGN5YTURrdPjT4w6NW_Yi5G92rmafp2s3kYLeG968Rv8_9uXpROmdnMBPiHCsIsHsFmNOqnFyrQlQstXteoBiVyABVDCYSRMIrIcBR5UBejzBwquUbNT9sbRGbT_3uoXKs03JW6frp3l4Ef9du_x5Th-MiBzeJCvNIFylnruX0cYdGQaLebyJfHe5Qr8-cr-TXmxFTDXDZtJKhRKmX8k3bR8XDfFZsuXIGTGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=EfPa4ec9LGQEiL-l6m-b17HnASYyVzRPn3nOpW5m35FlyipA0ds0mYWz-SGXyxvsbBtjB_GVpEie9Gvki1Q7x-ZqBRIb2M8Mhqr5Shj6y1-iRzwoHGN5YTURrdPjT4w6NW_Yi5G92rmafp2s3kYLeG968Rv8_9uXpROmdnMBPiHCsIsHsFmNOqnFyrQlQstXteoBiVyABVDCYSRMIrIcBR5UBejzBwquUbNT9sbRGbT_3uoXKs03JW6frp3l4Ef9du_x5Th-MiBzeJCvNIFylnruX0cYdGQaLebyJfHe5Qr8-cr-TXmxFTDXDZtJKhRKmX8k3bR8XDfFZsuXIGTGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
مقایسه فالوورهای ده ستاره سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106756" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDmgnS5bQEalceOawyy996MyZPYSl5dJ1FJ77vBloZvu5ZnQY4cfJC22q46mQDtUpZ-pI9DOe03tWDVq3G5gnfgFG_iCo-Z0wSZILdI5GwCbT1qB-jyUcPqEcakOpessoBIUg3XkwYsnjPBkZ1T9joQxADmgmgi3DqjRAx0FXZsR9ii_SHQRvXpfzYrU3v-6nEPUMhVtPPlvMm_vpek5WfvqwtmHiVoKuEyJj5Nz12CGEMmVF-4s8LU8BWQUPc6Ahjz_rOTjYP0m-8TfeURRnEsnWagcEB4Xr654Pt3weV4HmVXUUbyAHc8ycljTJKnTHXLfyHAA8sEMjogC8NSlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
شبنم‌علیخانی کاپیتان تیم‌ملی والیبال بانوان ایران به تیم استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106755" target="_blank">📅 13:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=i5tI6-X1SB9ev7Q1x_3LW9imtiPCvkmgzswYQxNcq5iB-OuHpdDlcUW521WFGinF-4pSzBj_fBKOjFPKa1zEPCbvo0UAKAyOxOYcOOh4sAkdOhf2UJe_HaX5RF--lcZ7JnVC-pLwonphS0FM5eqUVU7So6vXNZS8Ikko_qGSYGdda1lc3atJZjRCwF-rPj5XcE1IWPKES1O58zmg68hwtPktBh-NKGt9HgT7pdUPkrDvkhkjsQKsPiJuV8ZCJPiyMTOAQAmdpalFRqAHbp2Zj5Mqkgqn3kO4J8Dl2J5NYXaPkMs08-BrgEg_n8U9PmbWDLQPDRJGupZ7zgZb4gPwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=i5tI6-X1SB9ev7Q1x_3LW9imtiPCvkmgzswYQxNcq5iB-OuHpdDlcUW521WFGinF-4pSzBj_fBKOjFPKa1zEPCbvo0UAKAyOxOYcOOh4sAkdOhf2UJe_HaX5RF--lcZ7JnVC-pLwonphS0FM5eqUVU7So6vXNZS8Ikko_qGSYGdda1lc3atJZjRCwF-rPj5XcE1IWPKES1O58zmg68hwtPktBh-NKGt9HgT7pdUPkrDvkhkjsQKsPiJuV8ZCJPiyMTOAQAmdpalFRqAHbp2Zj5Mqkgqn3kO4J8Dl2J5NYXaPkMs08-BrgEg_n8U9PmbWDLQPDRJGupZ7zgZb4gPwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106754" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=rCl9x0y02vIqa2CXNLEzyOhxHC7KZn3U_TkvuD2q6LoLRZLj9kjKAFVpTu9VVmIJnoiAkBHJWVuXEEm2e8gYdHXjXxZrEZHM4NaotKLC5lXtws8DWW8vq0BngHbclQ2zrsH3uJBVJCePGrxRGn655HTmr16AwRsKTov8TzNY0H1CulIC1XFR3vJPsMjvqc3RId7NbbrscydJZ-GWNgDRWoYR3C4euQZxaQ581ibmncHaCqueXg1YCommwM7JnTuxilQQMEPMlqsAufLdwuQZfusD3nQRd8F6otr-FEGV3VfRJsE2ApkByrLvoRNOhT5t2J9CjplbY7AEEhnc1phRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=rCl9x0y02vIqa2CXNLEzyOhxHC7KZn3U_TkvuD2q6LoLRZLj9kjKAFVpTu9VVmIJnoiAkBHJWVuXEEm2e8gYdHXjXxZrEZHM4NaotKLC5lXtws8DWW8vq0BngHbclQ2zrsH3uJBVJCePGrxRGn655HTmr16AwRsKTov8TzNY0H1CulIC1XFR3vJPsMjvqc3RId7NbbrscydJZ-GWNgDRWoYR3C4euQZxaQ581ibmncHaCqueXg1YCommwM7JnTuxilQQMEPMlqsAufLdwuQZfusD3nQRd8F6otr-FEGV3VfRJsE2ApkByrLvoRNOhT5t2J9CjplbY7AEEhnc1phRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
▶️
✅
بهترین مکمل برای جایگزین کردن قهوه قبل از تمرین چیه؟ به روایت استاد هانی‌رامبد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106753" target="_blank">📅 13:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3wPLSzp3L64qqsfsiMlXxVtOGIUEVfIjKJvf2b-dXai4bfPAB9JCyb6KKGNoBNJMsT1WaHGMiAkL7MEyw2D4nVrurxzTY0SPSpoLn6GPeH8zgaiMdlC8mCEdJjLyJumY-zI-d6fqIPMqeHKLFJ065iKqbOKJsgGn3dLQpC6vkle9GAz7wnm1G37jp9sW0Q3wDPdP6aDV2rQBIb-x2g6bUvGAla_xDIbY4bOv3ypOd8UlDPdcoMvz0syMLXKyo0IFmKliPlfHoSW5S6iVMDvAK8LkEkNbztBQP2sLnxibvNAv0vvsQl2Hs3k9sKxcPrA6CL4LV3LDsihISShTNXfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyKkgXoSj2UbBNgVQSMV-AaaKOqGt9uFlVLqSzmU2s_oois7SWI0GJdxslAjl3rbJ8Qt5agJMnvzTRr_jbLJCx_nrSfykAbh1ULy5M0o-de8kfKIfrp-WBpGCGNK_LMbNycjfAjgwuRNZPcZVQN16EDbGI4SgoccjG1lPkUmqnmHzyET6HS80e-DAVDhU1Y__3Q1tkABDCClBpnr-5_59otNTpOWethbFciTHqMgrEO6FhpvGGWIP2XeiKRIQ_E-QWx9FoE_dWGCwAP46qUa87gs9hzKh6S_vX8vI6jtrtBl6__n7lrWYGt57XcyEaas4KyOaRs72f_FAcswpJHHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddepDEHH8_baNh0ur-ypsPOMKnKOM_7EidLr51yAeQrPugN1wz4fUbreDaBv8Yjdw1HkrX5Y7jSeCE86pbsDLGT0tp-nxMitDT3j4iZDytj6E7xNiNhiRMPypbNs28KzC49Vdtb2FI24YjSLak7Zsl51qMZoDLTQsJSNr73QvgTA9TJoo2O3OvIw6qYeC9K6GdsNyekOt6MDFaMZrkNRPzJxmJ6RipXR-nbeCJXUH6TDJiJnWZEpuxpV82Lyzv4gnOpsI6zRJxX1SvjMrM36WgajRk6eGMLnPjbn4rhap2_MnyVzqfOQV3Sx7xHrCnoObQ_SqPYcQNXs3NAlB07Lbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEi7vDRY9PiSnCw4WcnCbRdWrbAksjTruKbb1TW-x-RDp35qxbq2hTV1WIfTAAHf53kgDCLK6wXChECvs-FGiP55q4nW5-D2uofcs7Q59QYRzGtPsDhrAGG_u8U55zloLVDqV0AwIvOcJwhVX-qg_xcVgzaeJcFT7YrHY9sYGfaRiOy2Fy5JbFdST_gX2YollzFUX932UTNtQFJd7sRWZOZ5TIfL4CW98JzyzB9OFc86pkSveh9OY7BAg7enZjZ2nlxnRwqQz2NMRWZIsXGAmUNtV2m5zD8cmz5FvCPFwqV69SL_aAs1stYsdoVCZ9f5OK8r3HTMM_8drvnjdv7OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=e8puQ34Sy_lWLp_RX5gua4Baqpi2_XztYjgdLU-8_cGv-8aPS9myGM44qjLfMKetilv15uKWphPDgUVe2Mb6LwOmax_Y1PFuiLhLQSaQs2KFNkdVcghp_mj-vIIn2IXql6XNpRVvtcKjwxqZj0GFdoX_gMBsOz8ePzZmTAW7_DE_34Ux4P3FqftvtuJtsbU4V-cekrCmhfUFvpaGqexL8luiMVXy7U5kYeghLOyUym1bcJPo8rnRbs60LQ9aL2TolItpN9wTlV8vxmV0UGIlSv9B1k0D_oYdgtKlqD1ogwzIPG6zdvJ6ji9-KwWw-04N8QKSny8kcGV8LHYg9TBMmxuwZ0S0gn31UikiEX2SKQNHUkTF8P2vL4xrRsWp6_B6gLxbBAx4twlD0sSF2Jg_1BrlyMReTXlN4lSCns_1ubmO97CcGh6E4eXDxfYbyXLoA9hdPMjHM96bS2OIVot6tKUj8KG3bxNG2ZzcVyxCEoLr8e1ReQubriJ7TuikqcjkuWdnpQ-V3C6rXdq-_843s8p5iem94Pb8SrDOH3Hn97bUVH55WMpsTD2Oithd9zCnF6THg0-qyhkuHXHVdUWgcbds-ui8ZYvcDfIZN7njhWJ-mFjnfGHAtp_gaH4-eAozi-0_bx71TNLofTi9aGU1NCasOVqVFwXlvVbHelQQDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=e8puQ34Sy_lWLp_RX5gua4Baqpi2_XztYjgdLU-8_cGv-8aPS9myGM44qjLfMKetilv15uKWphPDgUVe2Mb6LwOmax_Y1PFuiLhLQSaQs2KFNkdVcghp_mj-vIIn2IXql6XNpRVvtcKjwxqZj0GFdoX_gMBsOz8ePzZmTAW7_DE_34Ux4P3FqftvtuJtsbU4V-cekrCmhfUFvpaGqexL8luiMVXy7U5kYeghLOyUym1bcJPo8rnRbs60LQ9aL2TolItpN9wTlV8vxmV0UGIlSv9B1k0D_oYdgtKlqD1ogwzIPG6zdvJ6ji9-KwWw-04N8QKSny8kcGV8LHYg9TBMmxuwZ0S0gn31UikiEX2SKQNHUkTF8P2vL4xrRsWp6_B6gLxbBAx4twlD0sSF2Jg_1BrlyMReTXlN4lSCns_1ubmO97CcGh6E4eXDxfYbyXLoA9hdPMjHM96bS2OIVot6tKUj8KG3bxNG2ZzcVyxCEoLr8e1ReQubriJ7TuikqcjkuWdnpQ-V3C6rXdq-_843s8p5iem94Pb8SrDOH3Hn97bUVH55WMpsTD2Oithd9zCnF6THg0-qyhkuHXHVdUWgcbds-ui8ZYvcDfIZN7njhWJ-mFjnfGHAtp_gaH4-eAozi-0_bx71TNLofTi9aGU1NCasOVqVFwXlvVbHelQQDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtRB_b90W_nUqZ6TTjyuMvnXVT_xFlspRmKoNDdcws4B62TqBQu7TocjgC23oOfSw5SwmrN4foaiGHieXetXcK_RdRRPUthbF61JXYvXW-LZ8JoamWHK3Oo0X7WlXnusIPaNCx6vl_qb3L3OlRqZL4IBMC2Rta61NcY4VDB29Wf2HOHCW_y55-_6xrINxGqwrIsFda6kB15D7fLw3qDWrrGnlcMQO-IaS_wXxSwW3YAeitlhhJ01BkCabhJoctbooDQXgOGjbY-zGSwiEOaQdnlT9OuxmJ1z4Br_nQkl8gVwmmQObRTHe6AMtFMlRs5aybXoBHPBuEVUkIEXPUaokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=vjru5yLFXBi6T5B65pLPelIrYnn3Qfd9Lsu05wofXl2TsrlfQMDJ2USv6YsVPKeYyzRzuECVRk3opyqedoHyXxz54QP8dCRYf5dKrzuqF28cW9IFg_oKUfxC5B5HAC-6rvAlkcqLAFQ1Plr9Ejyyl2AylrUv4HKzx4FlKnETfeDt572YQ14WxdErxMfCFxzf2ME9SFrtEZzcW0tp92iuGoYIgxCAnzDSeuF25qXC6SHohZCDU_39p0YlKUtbHirpW_UGEEVCBI3nu4309cbZYN0bEUQsSi40Yhkg5gU-rFt1ZK80SDGVJGGpxY_vy9v-BuVGCA8743baXMoE2UPAwK6iB-Pl4liiEU4WqjIPh0VcyOB2TH1tOIifGv107dltPe9Z1abx1nA2j2CH_CIRgfoEg_5E_m2Tf58Ef8hnq9jg_XqXfj-cdBAMpSoMfa66l7nsEc3OZCuQV_BOgn2m0t4dPtNNW2PD2na5HdlpRBdnxP6sFw0FLpTAmI9ruLw1vO0ffDKGR5PtVhDyYRfFr7cR2ut2nIEtDMIrolNyviAXfqgRnus-tYjkdyAiYgbeCP_t6K1O10GzFWoIPz9ajY3HMCk6P9kEjG8tKEh3oCUm3A2RjPiYcJUD9GIROUs00ICRSCaFl_xTNvv-mXEnSA1q7qopMIbihObJZDJwcZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=vjru5yLFXBi6T5B65pLPelIrYnn3Qfd9Lsu05wofXl2TsrlfQMDJ2USv6YsVPKeYyzRzuECVRk3opyqedoHyXxz54QP8dCRYf5dKrzuqF28cW9IFg_oKUfxC5B5HAC-6rvAlkcqLAFQ1Plr9Ejyyl2AylrUv4HKzx4FlKnETfeDt572YQ14WxdErxMfCFxzf2ME9SFrtEZzcW0tp92iuGoYIgxCAnzDSeuF25qXC6SHohZCDU_39p0YlKUtbHirpW_UGEEVCBI3nu4309cbZYN0bEUQsSi40Yhkg5gU-rFt1ZK80SDGVJGGpxY_vy9v-BuVGCA8743baXMoE2UPAwK6iB-Pl4liiEU4WqjIPh0VcyOB2TH1tOIifGv107dltPe9Z1abx1nA2j2CH_CIRgfoEg_5E_m2Tf58Ef8hnq9jg_XqXfj-cdBAMpSoMfa66l7nsEc3OZCuQV_BOgn2m0t4dPtNNW2PD2na5HdlpRBdnxP6sFw0FLpTAmI9ruLw1vO0ffDKGR5PtVhDyYRfFr7cR2ut2nIEtDMIrolNyviAXfqgRnus-tYjkdyAiYgbeCP_t6K1O10GzFWoIPz9ajY3HMCk6P9kEjG8tKEh3oCUm3A2RjPiYcJUD9GIROUs00ICRSCaFl_xTNvv-mXEnSA1q7qopMIbihObJZDJwcZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z60F07XAw1_5LiO8WdyGmS-JZ-ajNtCVphq6ObYotjcmWmjKgV1mjmNLRhu94LMtMuWcWGcnM9R2hvOugA-SwM3V37WsRNQwLD7t-v138ZkkW9PlaqJlwOUk4H1vgiLls9dhBra2jk4HUgJgWIlkVBnSZlmo0pgAIOqIlhEnwHua6TEWENDPCAmI7dqxU3VkM27_ebOqLRdhq9nyeK0Fz0QkxfWRNXvHFl_FY7YJCQ9Z4YGdITi7NgmbCXsTw07UVPUWhnXb699mctfWbNsMSZOrB_4OCMc2ec1XTXWxoNCGgTfMv9KzOVy-hzRnwMTW9byuQB_iRuZFkjKbrBMBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106742" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106742" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I35UTFdcbjdAJZJp9BCJMczxYuGBku9bLo6vpeQmtXzo4eU1pnIgnC96mIsCDIYJ5019x5ZjdSgO6nFvR-gmBW7OgikyzQjca8Uf5PqubF-sgD47IyF6RCU0_x5SNbz6faOaNUIiXWwEp2J-0xVxUqSJAVoPXMRwSs-o2FCYRfQAk8w-fE1i-5GWjuygmEuAIVeRHRm_144ncmZ-y4dk1wt9hua4NUaJxukKFF25y_VFsCLb4l5Juqrn5Z6OHVi2hMVVniki9LuoMGXctZhDXxOVHQ5LT4MJ4rYI8b6WKeiufzEu157ZyFGgIzzotYvoGXpVh13llYYm-EtZ53DjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106741" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=kyeGZ-k70JeG4JfTwRCU27Qh4ifPiC9y5HRtC7SHKJ7dB5U-DjC7c5HEoE9Pg4ciGIa1A10Onq9zFoIfq-7MIE7AaNOIRlMTuszS-9uNd7tkBNeqYIv8rNmPHNh10fPlPYTWEY9PlOaLG6vGJtfJmllkaABqS5d4qdajpYYGtY0Xh43RIDB50yN901NvLaK7Uq8Y7NkllLtD9J8MMDr468wjpC14Nvv7y1YVkCYG7ybyFfaVmEcFPtruQgQr6f13ax6QPOvbAYr8eCRs-uh9tbiy0WCpfUtKZlX-LJbyuxwMeYWIPF7jLD_XzUGMdOqe69XNlb-x-TAvTxqZak8ccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=kyeGZ-k70JeG4JfTwRCU27Qh4ifPiC9y5HRtC7SHKJ7dB5U-DjC7c5HEoE9Pg4ciGIa1A10Onq9zFoIfq-7MIE7AaNOIRlMTuszS-9uNd7tkBNeqYIv8rNmPHNh10fPlPYTWEY9PlOaLG6vGJtfJmllkaABqS5d4qdajpYYGtY0Xh43RIDB50yN901NvLaK7Uq8Y7NkllLtD9J8MMDr468wjpC14Nvv7y1YVkCYG7ybyFfaVmEcFPtruQgQr6f13ax6QPOvbAYr8eCRs-uh9tbiy0WCpfUtKZlX-LJbyuxwMeYWIPF7jLD_XzUGMdOqe69XNlb-x-TAvTxqZak8ccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
🙂
آرزوی هوادارای رئال مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106739" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
⚠️
خودکشی سرباز روس با استفاده از نارنجک پس از زخمی شدن توسط کواد اوکراینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106738" target="_blank">📅 09:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=LnY-kD9TR-3Eq8S-1pa_J0Kk88tie0MoHSTJVZLmufYKDs8A2BI0apuXh_UzcZOe2hCS1UuxJd_0uPYOWRgQ8tuA5w9Ma-j-akKKw3Xtu_vSgX5xiXD-JlzD0kI3ZgKM8adhh0Qpc9PHbW2T2XMtLUZLM4c2P5YEsYrZw8p98UWhybXZqw1noQc3NpFJfiJitV4A_TAnqWiAAsWQUnHLVjiKfcSSHAlIwWPQVshY1rdzG8mJbe-Xt0kNQYsvV5WZtc8VsG6_LyM-fOQsthe_MrmVaYtc_yn7jdByA4Lr5H34sYAN3lJMHbQrfnLkVbdGRzYava-75lIgfo2e7iasdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=LnY-kD9TR-3Eq8S-1pa_J0Kk88tie0MoHSTJVZLmufYKDs8A2BI0apuXh_UzcZOe2hCS1UuxJd_0uPYOWRgQ8tuA5w9Ma-j-akKKw3Xtu_vSgX5xiXD-JlzD0kI3ZgKM8adhh0Qpc9PHbW2T2XMtLUZLM4c2P5YEsYrZw8p98UWhybXZqw1noQc3NpFJfiJitV4A_TAnqWiAAsWQUnHLVjiKfcSSHAlIwWPQVshY1rdzG8mJbe-Xt0kNQYsvV5WZtc8VsG6_LyM-fOQsthe_MrmVaYtc_yn7jdByA4Lr5H34sYAN3lJMHbQrfnLkVbdGRzYava-75lIgfo2e7iasdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کادو ولنتاین سمی مسعود شصتچی برا زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106737" target="_blank">📅 09:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=lU8BuV3HYmYt_J0j3n9u_uioRorJJH-MEdRzB7fDQ0VWVejbprMYBXE7E1Rf8EwADtyl2pmuiPmU-O7C2jV-tycthlqqU7V2zZlAk4A9OWqOMdKBbQBcQHRaaNWtqz2rmwmFXN7BW7RsdrLmY3mPVBfBEmLgtUflyJCVf2M95-qNlrIFnUdJB3V4PJ7GYVMcVk9L1DKm8xKpvigmy9wGEY9lc1KazrWuYQDm5sjT1AQZWqPVTHPXz5vdKGBkh3-fqU3rjwoNUkIi8YE9SZd36_tvH65kf-Shmifeene5REbWzuO3L1nmyBPxN1Ske3qsusvrXJlOvKbjLU-Sqmutag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=lU8BuV3HYmYt_J0j3n9u_uioRorJJH-MEdRzB7fDQ0VWVejbprMYBXE7E1Rf8EwADtyl2pmuiPmU-O7C2jV-tycthlqqU7V2zZlAk4A9OWqOMdKBbQBcQHRaaNWtqz2rmwmFXN7BW7RsdrLmY3mPVBfBEmLgtUflyJCVf2M95-qNlrIFnUdJB3V4PJ7GYVMcVk9L1DKm8xKpvigmy9wGEY9lc1KazrWuYQDm5sjT1AQZWqPVTHPXz5vdKGBkh3-fqU3rjwoNUkIi8YE9SZd36_tvH65kf-Shmifeene5REbWzuO3L1nmyBPxN1Ske3qsusvrXJlOvKbjLU-Sqmutag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
یه زمانی نوکیا به تمام ایده‌های ممکن ساخت مدل جدید، نه نمی‌ گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106736" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Ast5JPNJPsL3mXb9c_dcHDh5s68sYgsWPbofGieHpZHC-JleGXBYPlVggowE6kt56u64w1cnAdVJoZoxXnqtfVrXVsO65uYlxj49TQGCDOrdHUqSuCv0PFhxVjRrojlfHm2V9x9kvqTm4J8dQ6kYRmRg-YDgAw6xaHb9Wgyxpn7Z19IyGs1JWJ6sI_H3JegKQ_-IzkCzJzXPCQJBzUYxfXBimRO7Tca8MKFojkBayq8qmHpDZvvQdKrRxOgO2smLDeUp9K8ae4G2uziKV8WFTHRxBwddt05dEHMOGYjyD6WCW6wSUdaI9r7SACm1JU7oeYAPrFsaaaGMmvMM6hBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🐐
با قهرمانی بامداد امروز‌ در جام قهرمانان آمریکا، لیونل‌مسی به ۴۹‌مین قهرمان تاریخ فوتبال خودش دست‌یافت و رکورد خود را بهبود بخشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106735" target="_blank">📅 08:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106734" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106733">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q623_85vlsd-neGn3fi_GnBY6KkAokEwOnIbsmkdvEtVnrvtf6B486A5gVRNAxrxiNUtrzw00QOm3UKEz9gjeSvVs6hfjYLk_Jx7O4jbvUACxzFYUisCY340-5GkKkFelFrGWD77i6CIpPwgORfxsJlT_9HRamAMrkKVSCMFRFu7cGxJtyvGsG7RaVCHtyFft-NWDt2mgQ0jXoi-5wxXUHskN5BGZBEAGvVTBfiWsvmazaIv05PdtfhFrH84CUvVdKJF12Q19IJAiDntz1Lt4OkfrVeyEm5cYyISr6-sKJaW0JjQG7pLW8odoXD9rwZ9HWTwQ8LwJS0pQvRr2wHKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106733" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106732">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6xAKMcJ-uZsVmkPNl-ncE47BjOii7YXCAxTlrn8L-L6dQLO45qBEItBsmDh9p4AollgJIbIBxp3V81UQMsVEG6jksnrtr-FbeO2dHwqHGipGvCdeByFRmrautn30xrmI6z3nEveFxyv-rjYElpPopy_KGB2b79g1LiNNaM9PFoxht4MjI5R70UHvlgAekFVqc21-bLket3y3iy4ntOR54Yqbr0Uq51OPhld2diTGXSRyvZgBsfljl8aeAhPj5Pnk3eUaY32o1hprAGMKoslwotF0NRjgKFD2DhL6l-00i1g_2T2xl40JVUbbCeyKBV8x2xrw0lyIZWcILvhtlKhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106732" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106731">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX4g0OHp03BhxMnU4cEU_rbrG13e2IWr9bVVTPBIt0Oo6lifL79v8HtWUjas-7eZNMllUk6wVAiZX-V1TvSOmWAX_SGJX0f4xeAerOoPPqELwBEg2CBbO4feRjqs9RtwCBeTm63PtI_HDvoDSXUhN6URjCZA7xdci7PpNya_oLn7_SeY3cEBf7B-6aV7EXzpwqKH8L6LiihXbLs1pLNjUV0AV3mhryLvvyJDBKpXOkH9KbdHvCbO_Soxz0RyJUsiOLb1bkrqK9fcfjBivgLASx6spMbQvifnFGYo_iLNLv01OVoLZUfNn-UQJNpWg4Psc-XGvXv8MnJ8bgHd3vYUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106731" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0sEfSGMmow7SwNv7UHFXxrMQ-YsXJyaOjz9fCYnBkJjOM7SfZ1RWtBYlfz1WGaBrpxXIWCpJaQJODBlPw1PQs1zVzM6wttjluxiFDXGEdfkJHDBn9rHYmeTr5UfAuiiOYpS7n5XLdc1CrEQtwkESwjkRNBHH9viTA7Y_SemJHZyGKucsHqTXdKdBnxCTCRkAYZzHxhnTixTHiN0_CdTWdyfAEikVfv0eIt4yti1Ty8zjJuhUvb5UuNarm5BVznt4nQjw7JryWaODGeGa6_KrG-1Ot-pK6koNur8z0U46dFbWwNVDXEwTAE_jHEK7YnOUzEOQof7aEFWgSv6xbS5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
شاهکار این‌فصل فوتبال اروپا بدون‌تردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106730" target="_blank">📅 01:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1vtGlGvIldsanIz0rTnZtpSbMBsJa6Ogs1SRKPTeQyN8lPCqP7zstLq3fu0CXo6HzH3NWteEgAJBMJbKxVAvCz6txxQbvqCCOzVEZHUshjXUHky2YrCmUdSoTnzrc4Ow7GM6RMo-xjZWbMrxIJqCtrVkWIkEj0N9mC8IyCjUCibw25QT5Mg2udRiLJyp3N7cal8Sjn1RC5m1Yl51eLwY5zvk4waQdqSQaIna0eZ3asxE5jFoV9aXEzPDWx9pJtlcnoqnSEuRrpok1PmC8KoDdc9yjC1wcAuGrL3wfHVzSxNA6MgM4jOAhWgttoQuxacl6qXuLUU8vSQrHvn3gtQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
وضعیت جدول لالیگا در پایان هفته‌ششم
⚔️
برنامه بازی‌های هفته‌هفتم:
🇪🇸
رئال‌مادرید - اتلتیکومادرید
🇪🇸
🇪🇸
بارسلونا - سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106729" target="_blank">📅 01:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI2ieldGOUUehGoz4ZLm8iaIYl_2f02DFk6i3sekoIzBEsX9rfmw2omrFWdNRgm1Usl8R0TzS14PaXNC3Y2nrF5pZ-VO1uQ05bfK6O3i44qxJrlLwMfSt-YQ8SIbO2ZSDJOF6-by2Pqw7u0_WAWTJWE05bsMIU9-jalymVISnozqXTjcaD12We28peWYhzbm8WVX6XhrkjoUOACj8TXKC5bSGoVwUP9olSTlTU7uEOV2HnAsXH36PibC9tdqjncAYg67dFzVJl5PUu9GNjB3dKfFN4h5Ze-Khd0TGuws6EM7n68rGsbgXCLNxSXFhsQJQitIT6A6pfX1O-qchIUr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بهترین شروع فصل تاریخ خودش را رقم زد؛ 7 پیروزی متوالی(لالیگا و UCL)
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106728" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLRbLcwLqQ3v-oj4kgMKTr6BtIX1XHzTS6ZRzdxachTFNN0ZQi1-B93bSwUetEgvPSLgQY3NghRv_97wiZPMAwZ7zHjryhpUw9ABoIaFq_BWtMC3iAnO0PVJk-58Ho4iznWOOm8qnewlOdwrkUu_GLuxyETfGR8zROnX2Xj5uJx0RK4Df-q7jDu-ojpZvmECoDLUYcjTrBdsCHI40rTbbZWuNQPUPjPtJhOAViJSQNZkq-qsJS7q6bUhDLu27sgYguhHgVvRTwBKcCsEuLdquEU3JpVSOwCYVO71QfRa7Hll0-ER9ZRdEABsh-WBBYkJMMUDuPUDEWcppp5Wa0Or9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لالیگا| بارسلونا به لالیگا رحم نمی‌کند؛ همه را گلباران می‌کنند و یک سؤال: بعدی چندتا؟
🇪🇸
بارسلونا هفت - سانتاندر دو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106727" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106726" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106725">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هفتمیییییییی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106725" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106724">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گگگگگگگگگگگگل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106724" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106723">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=AqECrJWV2VlM6ZtVjdtE3K4T9LnisL394l-6_dQ7pXEYLq8OJNu5zhdHa6BGUw58py75TX7ryukSeazY6U9ujiZv9fnM1CDO49nKZeLHlmvyLQZFuaskSp4No6JwMQ9TvSjVa4xvWwaSUhURPhvHXv0IM6gLwVcxcOAQpoC-1biw0N2HHqaOK3yTJOVGCLADlYC-DsegjIPdkv9nm0i8HZmIbfEFxuKKPQ8CkRxU-qsVNS4MLdgvCHU0o3w8iGyu7i_l4wRnR9NKpY2KHIK95g8utmg7BJlJBZoRUyCA9z2Nn4qpH-CNQbEnYv3Nd-_yHfcoJglA708LcY0L9gMFUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=AqECrJWV2VlM6ZtVjdtE3K4T9LnisL394l-6_dQ7pXEYLq8OJNu5zhdHa6BGUw58py75TX7ryukSeazY6U9ujiZv9fnM1CDO49nKZeLHlmvyLQZFuaskSp4No6JwMQ9TvSjVa4xvWwaSUhURPhvHXv0IM6gLwVcxcOAQpoC-1biw0N2HHqaOK3yTJOVGCLADlYC-DsegjIPdkv9nm0i8HZmIbfEFxuKKPQ8CkRxU-qsVNS4MLdgvCHU0o3w8iGyu7i_l4wRnR9NKpY2KHIK95g8utmg7BJlJBZoRUyCA9z2Nn4qpH-CNQbEnYv3Nd-_yHfcoJglA708LcY0L9gMFUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت عبااااااس چه گلییییی زد
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106723" target="_blank">📅 00:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106722">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پاس گل هم لامین‌یامال دااااااد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106722" target="_blank">📅 00:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چه شوت محشرررررررری
😳
😳
😳
😳
🔥</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106721" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گابریلللللل ژسووووووووووووووس</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106720" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چه سوپرگلییییییییییی</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106719" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106718">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یا مولا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106718" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=RD93h9ZG38hv5oLxbXD4c4Khn__593sa3elkGrP9L8_soAq3be1YxI3pDAD_72k_dF1maJkPYCOZ0x9d8x6c1MzxaSo7rjFWFzCv1Rmjvxoh-WgOnh_L-H_zfecbvimX1CEarD-dYIes5B65Ow0QLKv8SrHaMt4YNog4fGIbIBMY5qi58fMnOAumiiBMHH_JchcP19BzYKwW3TRgQ3PPuTYvfhdbc9EDoBXPgiPPILQMXGydmYxiqmOv1MZUdNZqFqV59fsg29n0lJov1X5MFMbDBBVG_KAshgFdgVvvuuv97RR9FAGdClXc973vf47mZliKiCE8PK5AFwFV3wzv6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=RD93h9ZG38hv5oLxbXD4c4Khn__593sa3elkGrP9L8_soAq3be1YxI3pDAD_72k_dF1maJkPYCOZ0x9d8x6c1MzxaSo7rjFWFzCv1Rmjvxoh-WgOnh_L-H_zfecbvimX1CEarD-dYIes5B65Ow0QLKv8SrHaMt4YNog4fGIbIBMY5qi58fMnOAumiiBMHH_JchcP19BzYKwW3TRgQ3PPuTYvfhdbc9EDoBXPgiPPILQMXGydmYxiqmOv1MZUdNZqFqV59fsg29n0lJov1X5MFMbDBBVG_KAshgFdgVvvuuv97RR9FAGdClXc973vf47mZliKiCE8PK5AFwFV3wzv6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌پنجم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106717" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106716">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106716" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106715">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106715" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106714">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=HNBjqBRNO4w4C4BEEEFiH1fvGUKVLwN_5kp9qKiRV7TLiXkUKrTXCx4racpBYCAUHOEqrTpHpz4eLd2EN9UVPGEwqR2JVfLxLYnjT-0-Eteu55XR_rkorupsyWxDxzp867E_oERG7SWqswMMyCDJ--cqdF0M72mGhLO4m9CU93Pu4rg6SnU2B7CIReqmT_qwrMU9ZUhylG1kF-PUdbKh6uns49ZCcN2BCYPSVswN6KPZkzvMKiCQKjmTtX5NcxzV684Y3iljSK5GQ0tnVegJQ1ksr00thXaTng6epd6_Ifqjt4krXKOxoU-2Pap5oxqbQ2P39onqGpikCEqb00XChYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=HNBjqBRNO4w4C4BEEEFiH1fvGUKVLwN_5kp9qKiRV7TLiXkUKrTXCx4racpBYCAUHOEqrTpHpz4eLd2EN9UVPGEwqR2JVfLxLYnjT-0-Eteu55XR_rkorupsyWxDxzp867E_oERG7SWqswMMyCDJ--cqdF0M72mGhLO4m9CU93Pu4rg6SnU2B7CIReqmT_qwrMU9ZUhylG1kF-PUdbKh6uns49ZCcN2BCYPSVswN6KPZkzvMKiCQKjmTtX5NcxzV684Y3iljSK5GQ0tnVegJQ1ksr00thXaTng6epd6_Ifqjt4krXKOxoU-2Pap5oxqbQ2P39onqGpikCEqb00XChYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریدمان محشر شزنی معتاد
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106714" target="_blank">📅 00:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106713">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رافینیا هتریک کرددددددددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106713" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106712">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگللگلگل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106712" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رافینیا پشت توپ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106711" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سومین پنالتی بارسلونا
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106710" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106709">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106709" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106708">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وااای عجب ریدمانی کرد مرتیکه معتاد
😂
😂
😳</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106708" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شزنی ریددددددددد
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106707" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeGs4TF37kN4BVfKVgRT0SUotZ69OOs6P4sw83e2H9uTTNeRsIJbGahCbjY1Wo4VOfzfOXpTmvUwztCSEjTBsm800bTbCoipdf_LEo4OZiwPRlzsqm5sl0J6FE_t-1NtHtPsvjn_Y0LedwT38u2Ghe_ZiMiKNQhTJORYU_H_AK5Py1R7KiZjIG1bJVPwb8eAyx4__xVZZv0i1LdnSX5UNwOq0sNaezRjG_ZO1UPL40khd0LDQ1vm3p332EZQ55CFdkXZI4a6GKCfHNrWwC6HN4if6xEKnvKe19WuYZq-Go6HJfROQOUJWZrj4Q82_faAjjmEnOUToDRMcgWJdZNzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106706" target="_blank">📅 00:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یامال دلقک کارت هم گرفت
😂
😂
🤣</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106705" target="_blank">📅 23:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=XEV_ZupVyCCiOsG6ZXVeKP6RZA3HzO3Y1udWJZol2yHp_9xhdw9mROg2KEkTyevMu8P8Wz2RZA4nV0Dcv917xy-jPF9XCaTufW1xqo9cU7Ho_KxiAgZMsS7A_LWQWFekBAKm4IDRKHp5zTfzZlhyvd5mt0MArs_7-YgbXswo2-D-h2TtUonKTQmNyBz85JNpep5eNm_xqF4Oa09gkudMMOL7_vpm0kQSnUjku2nlL1OihcjiPGPMYhKV5guoPlEix4AND--kIJtce_ihki-5EAVXN5fq5kW1elP5zIfgGsaRcsSMZc2GzXL_IDhxwE-lqWWzZXbXCCe6sCScVeko0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=XEV_ZupVyCCiOsG6ZXVeKP6RZA3HzO3Y1udWJZol2yHp_9xhdw9mROg2KEkTyevMu8P8Wz2RZA4nV0Dcv917xy-jPF9XCaTufW1xqo9cU7Ho_KxiAgZMsS7A_LWQWFekBAKm4IDRKHp5zTfzZlhyvd5mt0MArs_7-YgbXswo2-D-h2TtUonKTQmNyBz85JNpep5eNm_xqF4Oa09gkudMMOL7_vpm0kQSnUjku2nlL1OihcjiPGPMYhKV5guoPlEix4AND--kIJtce_ihki-5EAVXN5fq5kW1elP5zIfgGsaRcsSMZc2GzXL_IDhxwE-lqWWzZXbXCCe6sCScVeko0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106704" target="_blank">📅 23:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106703" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=N4o9aT_snzznmWI7xLMp8VVEkWks3yXjhi1j4N1ErGH1E_fwfKRmf9E5U0FDD2B0l7hfezjQOf0sS_rOuyOosDuLgxlG2vqAt5Z-fJVvHHvzrr74tskTjiLx-2306EylR9IjwGwT9SHY8CR94GFmnKJbhs573JNud-vRxuQs3B7yhd5gY7v5lhpJdbf3vi_M49QWsv0FdTO-wrEOBc-XCKCLchvIARAL2V4GvWFT5DTGmSysDsnQjhXAB4bHZCjDPj8-EB-CrJ4kQ0AyotrEUG6ti64_mgmUrWncdOyNzZGbZtfN13U3gPVqKsIipslXPn8Reh9cRxZUGtdn_pAOfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=N4o9aT_snzznmWI7xLMp8VVEkWks3yXjhi1j4N1ErGH1E_fwfKRmf9E5U0FDD2B0l7hfezjQOf0sS_rOuyOosDuLgxlG2vqAt5Z-fJVvHHvzrr74tskTjiLx-2306EylR9IjwGwT9SHY8CR94GFmnKJbhs573JNud-vRxuQs3B7yhd5gY7v5lhpJdbf3vi_M49QWsv0FdTO-wrEOBc-XCKCLchvIARAL2V4GvWFT5DTGmSysDsnQjhXAB4bHZCjDPj8-EB-CrJ4kQ0AyotrEUG6ti64_mgmUrWncdOyNzZGbZtfN13U3gPVqKsIipslXPn8Reh9cRxZUGtdn_pAOfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106702" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این دلقک توپ‌طلا میخواد
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106701" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یامال ریددددددددد
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106700" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پنالتی دوممممم برای بارسااااا
😐</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106699" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل سوم بارسلونا ژائو کانسلو</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106698" target="_blank">📅 23:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بارسااااا خوردذدذد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106697" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106696" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رافینیاااااااا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106695" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بارسلونا ۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106694" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106693" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پنالتی برای بارسلونااااا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106692" target="_blank">📅 23:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=fmnxUR6CfncNDDyawiV9MIMsJ2HJEGSP1uIKkrhxWH8HGOHFg77JYENPk-lJtQoQJecGN22iHUmd3CQgGoTUaImspfaZlb_Oom0COSxHJXsdANnq_5FpXt5eSidxpsaTLjTMyzcVr64Zay8I9rRpvSmyNEHCEBMznazYnjWpGB4gu3jt8R5KYEcpVmQFzbRmsvg9-QdGS_WW8vaLUZV4R3DCfdoJj2qEvNaYVS7S_oCaTTMS6JNSlShit2sGVQbdpZfxL44lq90edFGaFkpaQl9HItxFZdtpQv7Fn6af6O5SLTwVQc3Nz5szesVl_iAgQ1PpWVY8XxZxHwjgo6dc7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=fmnxUR6CfncNDDyawiV9MIMsJ2HJEGSP1uIKkrhxWH8HGOHFg77JYENPk-lJtQoQJecGN22iHUmd3CQgGoTUaImspfaZlb_Oom0COSxHJXsdANnq_5FpXt5eSidxpsaTLjTMyzcVr64Zay8I9rRpvSmyNEHCEBMznazYnjWpGB4gu3jt8R5KYEcpVmQFzbRmsvg9-QdGS_WW8vaLUZV4R3DCfdoJj2qEvNaYVS7S_oCaTTMS6JNSlShit2sGVQbdpZfxL44lq90edFGaFkpaQl9HItxFZdtpQv7Fn6af6O5SLTwVQc3Nz5szesVl_iAgQ1PpWVY8XxZxHwjgo6dc7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل اول بارسلونا به ریسینگ توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106691" target="_blank">📅 23:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJVzyrfDJTKHb0hSmSRklJBZzhskpG59Fcj-iFa-3Ph-e3V3gB5iv6OOcU9gEVHm-Mf7DmxntZcXql-raTN5S1lFxhdAYcReExSPzdZJ13OSHIhKfz0HoQWGaLRUUfZmRJG7Mkah-ltuxKPrVpeiL5n1XuX9x8JW4TtpXqDLpFsSw3Ygq0w5ZyBbOJokU7aUg7DwVl81_7FPM45ef60CuuO3MfW5Vj7CA4DXYc8XH8l05qCKw1JUdgloqyK1LQcAcjyFNrTHnc3GQWA9MYmJJB623Anaw8UxtvC9Y5n6F-nx1wgw1zWpZDGlYZCakaAZY5gW5Ws86OVW7I1pYGT_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل ریسنیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106690" target="_blank">📅 22:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POpxj3g3n1jxd_gOTfXSRqHgoIHbWV8w2cF_O0P5_vGDY7sI9nZIIVuxaeBdR9ucQBIqA074MCaaBpgFTPYkX7OTivAu0IaJLRrpBLXB9ZYbmK1xFyxn7aFBvswQq6MFKjdb7crNZ_HQPNELQKPATBYphHBDWWH5hutnEbk8qm5mtP4sPw979tEt3MXHCwysZkNyXq8OeBvljU42WJ43Gho-MpW99GzWnXJp3QI3_KFennUqf26zy4wnwnrbTaxq_DR_Wc0TQDjnk8ohdH3UXF-BFtAYAYL6gAeKxaiYWp8X3Atdsh9ta0BPt6F4ZMpAqr4MfnR1X3mkMXmAz-e9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇵🇹
لیگ‌اروپا؛ ترکیب میلان و بنفیکا
⏰
ساعت 22:30 شبکه ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106689" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=Zp42PUbcQF07oOaUlecz6FHJmZJ6W7Pww2NqqLw9el3LFPLGVZ8it4MPz8POqMoBr3YlGCUsBv8mf4kSgN6Og01jxmCSRczXjxgdBZiWno6zFek8CUOJ2QD6ZpXOhS2VoWmbIRvjP-vUooxbVNO9dRSlI3WaT3Ux1XgYkz20PN5VAuwrnUrwv6493n2PFudURCE69gjeWXAQUYly671x9cjcfAIx_kaU1L1d1eR7qjB_SekV_c28gekVhGYCswkyH4AC06yuHVtEuGhF6--gjSEO0iHqpkPUwadEhg_u7a8araL7kmONtsNXh0hK9yAdRSrwp27Qqr9k9anU3yTnKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=Zp42PUbcQF07oOaUlecz6FHJmZJ6W7Pww2NqqLw9el3LFPLGVZ8it4MPz8POqMoBr3YlGCUsBv8mf4kSgN6Og01jxmCSRczXjxgdBZiWno6zFek8CUOJ2QD6ZpXOhS2VoWmbIRvjP-vUooxbVNO9dRSlI3WaT3Ux1XgYkz20PN5VAuwrnUrwv6493n2PFudURCE69gjeWXAQUYly671x9cjcfAIx_kaU1L1d1eR7qjB_SekV_c28gekVhGYCswkyH4AC06yuHVtEuGhF6--gjSEO0iHqpkPUwadEhg_u7a8araL7kmONtsNXh0hK9yAdRSrwp27Qqr9k9anU3yTnKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
همین حرکت دیشب رونالدو که
کیرشو
میگیره، تو ایران خیلی وقته توسط بازیکنان انجام میشه
‼️
پ‌ن: واکنش رونالدو به شعار دیشب العینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106688" target="_blank">📅 21:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=shcnL8fiWcnFx0Idgw-3Pry5SW8MTLDUb_PbohZK7zMflUI1sLBo3e-F5HQ6ovzLOoD19__mt5v2IbrsMWc8AaSODOI7jEm02JWGD9x71E0J1uOwJcZrv6N7U5N10_9ssxYsFCsj0XyX6BDgazgsY9vIKgWt04hrXuUiCeVEjO9ys6Dm0pejNWWjyLXmfwo6qkxZLDN_Ixxgho7_zWY9w9oknlBxHcgJc15aKApqlZvM-5KD0kWiCiRf8Wd-HSO6urmcrBBERTnBOnMdvEf1hd6qcI4NdFP3_4PXdwOnub4HEYZuu7IiEFbSYU3gn0nWQY7vcYSIfoYxyVxG3orvkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=shcnL8fiWcnFx0Idgw-3Pry5SW8MTLDUb_PbohZK7zMflUI1sLBo3e-F5HQ6ovzLOoD19__mt5v2IbrsMWc8AaSODOI7jEm02JWGD9x71E0J1uOwJcZrv6N7U5N10_9ssxYsFCsj0XyX6BDgazgsY9vIKgWt04hrXuUiCeVEjO9ys6Dm0pejNWWjyLXmfwo6qkxZLDN_Ixxgho7_zWY9w9oknlBxHcgJc15aKApqlZvM-5KD0kWiCiRf8Wd-HSO6urmcrBBERTnBOnMdvEf1hd6qcI4NdFP3_4PXdwOnub4HEYZuu7IiEFbSYU3gn0nWQY7vcYSIfoYxyVxG3orvkjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اتلتیکومادرید به اوساسونا(جاناتان دیوید)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106687" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=t2lEZwL8kvW_x_7l8e5L7oe0TeKmoPNlD2FDsJZ8ENPyJzAVmWAgft05diVNDiBVS-7BHov1mik1-JBVbFRHxKGUzfEN2KliJhmJWvdvCi-K3LELilJBs5WcuKz2rCWxgJKx5dHY8ywevfXkII2PI9fzh55rIHYav7QED862MnaeWWlFN4op6dRJRmmQuRX2SQ6D2lazh39CgMzkFgn1mAWFGts4Zm-uwV1roSitCdKK52uxvfT4OHi-eryWqhvu2ttl_nQMUHVwdYF2sbqcZWG--L3GRWtoQHc-iYcTGZZpVTORHQYv_DOO9_rxvT3Sc-djkJgr6AjRo4XMjNWFBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=t2lEZwL8kvW_x_7l8e5L7oe0TeKmoPNlD2FDsJZ8ENPyJzAVmWAgft05diVNDiBVS-7BHov1mik1-JBVbFRHxKGUzfEN2KliJhmJWvdvCi-K3LELilJBs5WcuKz2rCWxgJKx5dHY8ywevfXkII2PI9fzh55rIHYav7QED862MnaeWWlFN4op6dRJRmmQuRX2SQ6D2lazh39CgMzkFgn1mAWFGts4Zm-uwV1roSitCdKK52uxvfT4OHi-eryWqhvu2ttl_nQMUHVwdYF2sbqcZWG--L3GRWtoQHc-iYcTGZZpVTORHQYv_DOO9_rxvT3Sc-djkJgr6AjRo4XMjNWFBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی و جالب علیرضا مرزبان درباره زنده‌یاد سحر خدایاری یا همان دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106686" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=lDwqksVakf_xDsm9p2mfdtYXtvpInHfFKssAs_4loZzLNGaLNwMf0aSH8DzsnYE2BFo4xIRobtB3b5D5h6To9_h0Yp9Aax-rqnk85Fy2U1qSe6WNI7ttoJnmO96rFnKhuCHgPoO75RejF3E7mbH_U92Dzx7BQj82CErm11yson4Pb762v3OMrZ8mF4v2LFI4CcTNwcX5384m2qKhexwPdf9nI4INHCRbsEqqdtKKgCesKXu51EMyXFlCWBREk1rewLXFjFK2zv2C5JwucDdL8i_Z4Np1L106-gXwUPA5GGx0KlSDw88b9HcaFobQt_nUZPG8Cpr0NWpkp73bBmiI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=lDwqksVakf_xDsm9p2mfdtYXtvpInHfFKssAs_4loZzLNGaLNwMf0aSH8DzsnYE2BFo4xIRobtB3b5D5h6To9_h0Yp9Aax-rqnk85Fy2U1qSe6WNI7ttoJnmO96rFnKhuCHgPoO75RejF3E7mbH_U92Dzx7BQj82CErm11yson4Pb762v3OMrZ8mF4v2LFI4CcTNwcX5384m2qKhexwPdf9nI4INHCRbsEqqdtKKgCesKXu51EMyXFlCWBREk1rewLXFjFK2zv2C5JwucDdL8i_Z4Np1L106-gXwUPA5GGx0KlSDw88b9HcaFobQt_nUZPG8Cpr0NWpkp73bBmiI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
ترکیب‌رویایی قلیچ پیشکسوت فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106685" target="_blank">📅 19:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=qKfcwgJIxj9FDEJdvUP-wZpjaQwuBETCAlUM3h_E_AVkfFTyKzlBwGDuQR6H-H7T8tvr5OZFCoWSZ2S29S1YYoXTRoBVyFSYZWzHuWBL9ey2wXav8mq1d5uWWMSH9dZmsWEzBSSco8ilLTIDAlIP0CaVhKVRWI-CZsnmjCQiFFJ-_GO5s--0Qoz6ZFrffPf0PLDVdCm_IxIlq01sa37lKhwdnGRFoP7zJ6uIl8-siLeifT00oBkV_cMgZlXXzzziR3A-Sow7iTNFSgB8a84oBrVtixUkBWnKKljjPkj-43z36mr4wEPU18kVYjFjyLXI043sHdVmhhpJuRedH7x0opOCCx-zcPXd5X0QJppVMkxQlGn85fU-9fFM0-aQIa1L8Qtp2fMdV33o4bR6pgfST3vWHcY9y-MKNJlXg0TiIA4oO9eu5fhUzIVq3KTsHY58XKqQTYtZXiQ3vbTE5YmwtR5uKJm4LlxDQdhiQFF_dzVmETF9AIca21XLcQ8ytutBAnZVSGRTA5QcDNL26CuStjyOVLfxE5XtI3Z-TEnRn2H0Cftxl0TG_9mo67MluLPVOh25TVJVy16q-ZTvSqRYs-tW5eQCXRCjUsorIilIr-8T4L3DIMN__0gK0-xvEE2Dj7B_F7HDbmcYaCohcDSCqzoVYo_nrFwkOKQOz2epY5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=qKfcwgJIxj9FDEJdvUP-wZpjaQwuBETCAlUM3h_E_AVkfFTyKzlBwGDuQR6H-H7T8tvr5OZFCoWSZ2S29S1YYoXTRoBVyFSYZWzHuWBL9ey2wXav8mq1d5uWWMSH9dZmsWEzBSSco8ilLTIDAlIP0CaVhKVRWI-CZsnmjCQiFFJ-_GO5s--0Qoz6ZFrffPf0PLDVdCm_IxIlq01sa37lKhwdnGRFoP7zJ6uIl8-siLeifT00oBkV_cMgZlXXzzziR3A-Sow7iTNFSgB8a84oBrVtixUkBWnKKljjPkj-43z36mr4wEPU18kVYjFjyLXI043sHdVmhhpJuRedH7x0opOCCx-zcPXd5X0QJppVMkxQlGn85fU-9fFM0-aQIa1L8Qtp2fMdV33o4bR6pgfST3vWHcY9y-MKNJlXg0TiIA4oO9eu5fhUzIVq3KTsHY58XKqQTYtZXiQ3vbTE5YmwtR5uKJm4LlxDQdhiQFF_dzVmETF9AIca21XLcQ8ytutBAnZVSGRTA5QcDNL26CuStjyOVLfxE5XtI3Z-TEnRn2H0Cftxl0TG_9mo67MluLPVOh25TVJVy16q-ZTvSqRYs-tW5eQCXRCjUsorIilIr-8T4L3DIMN__0gK0-xvEE2Dj7B_F7HDbmcYaCohcDSCqzoVYo_nrFwkOKQOz2epY5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🇮🇷
سورپرایز تاکتیکی سهراب بختیاری‌زاده؛ استقلال چطور السد را زمین‌گیر کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106684" target="_blank">📅 19:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6891deda.mp4?token=i5MYQaCY876ax2X8INYdz1CLv7AvZwRETzm70PYQ8R-dk8_vioV7b5eXv4RFN1gWBDcsZl1qyhPV5K5FwxnvXXNFOawH9eOyLQEmhEytuGYcubXE0dbF0DcPaq7gLIH4ujVZwgkA4DIefXg172Y0pacbWuPxzvLK7TBK4EGmtItRupTN5fJs6B3xCS41ryYwjaau6_kh8GzH5hPBVmUuQ9V8yVrrsADKs6ozjTpi9OAbotg7o7yRx-Lc01VCT-k2X9Pp9vtxZE0WCv6aaWkTmCrZSpwQWpBllbmVrBTkUWjMVdith1OuxIf0qbw7w2HV6kxT8_HXwQlJZTJzO-op8myItm2WNXCeZ_vPazfbwbRzThOzOYiIZvy-LEK9v1OfR43oKEBOAfKwWl99xolrOMEOPDCd9Zt5cAQeRuIfT-UBe7H76qzpsgt1DfnnfjpB11bdmq400nZmExHcJOKeRHEAL7fcU6BqEdX-chL5mJ_q1x0iO7CBzVtloXSKLLSEuYjt0hMvOuSvxPR0QhnZAN2kiPUi7o-YotZ1jF40eL3APyKslKJPYXJ7BMp6kdzTKwVRpBtskGF6bD5zG5BpHyFfVufpCDob-A2Jx33QA8dE0m3Qfs6cAK8hDRk2Fa3xGQsvoavbSTRSODOab9TN86JIHkQvbRFE5ZsSSOSWKWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6891deda.mp4?token=i5MYQaCY876ax2X8INYdz1CLv7AvZwRETzm70PYQ8R-dk8_vioV7b5eXv4RFN1gWBDcsZl1qyhPV5K5FwxnvXXNFOawH9eOyLQEmhEytuGYcubXE0dbF0DcPaq7gLIH4ujVZwgkA4DIefXg172Y0pacbWuPxzvLK7TBK4EGmtItRupTN5fJs6B3xCS41ryYwjaau6_kh8GzH5hPBVmUuQ9V8yVrrsADKs6ozjTpi9OAbotg7o7yRx-Lc01VCT-k2X9Pp9vtxZE0WCv6aaWkTmCrZSpwQWpBllbmVrBTkUWjMVdith1OuxIf0qbw7w2HV6kxT8_HXwQlJZTJzO-op8myItm2WNXCeZ_vPazfbwbRzThOzOYiIZvy-LEK9v1OfR43oKEBOAfKwWl99xolrOMEOPDCd9Zt5cAQeRuIfT-UBe7H76qzpsgt1DfnnfjpB11bdmq400nZmExHcJOKeRHEAL7fcU6BqEdX-chL5mJ_q1x0iO7CBzVtloXSKLLSEuYjt0hMvOuSvxPR0QhnZAN2kiPUi7o-YotZ1jF40eL3APyKslKJPYXJ7BMp6kdzTKwVRpBtskGF6bD5zG5BpHyFfVufpCDob-A2Jx33QA8dE0m3Qfs6cAK8hDRk2Fa3xGQsvoavbSTRSODOab9TN86JIHkQvbRFE5ZsSSOSWKWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
توضیحات مجتبی‌پوربخش درباره فساد ۶ عضو ارشد فدراسیون فوتبال جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106683" target="_blank">📅 18:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=NesiKlbQddS-gDzdU0eHQUG2Y_G-iyAsyiFSeyjv1uZzcqLaYkEaC3dz8ZmiQ3-43mvqqqwgqzOGcoqFV9pUoSOigtd8KpBjp8u5dGLwL74dyIr4nB8DZYMXynPRZqkhum_0A7KcSYAHQb8qWOmc4n7RoEfXpRhhYRinv_2zDVOISDdnqjqc5tbD7QQWjuKzyoTAjt-eWEHWhzE5-cuvMMZQeXQHHUQPaMfFr60IuzHqqwFen9SYvpojZW0e23zxnqzKJ1mbGptXWlf7vAT2dzEFiIEyrxUHyXEsbw71KCZ8fE_ZT33qBMeukmFuISLDgVBk-778OQVYipGFBTMpxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=NesiKlbQddS-gDzdU0eHQUG2Y_G-iyAsyiFSeyjv1uZzcqLaYkEaC3dz8ZmiQ3-43mvqqqwgqzOGcoqFV9pUoSOigtd8KpBjp8u5dGLwL74dyIr4nB8DZYMXynPRZqkhum_0A7KcSYAHQb8qWOmc4n7RoEfXpRhhYRinv_2zDVOISDdnqjqc5tbD7QQWjuKzyoTAjt-eWEHWhzE5-cuvMMZQeXQHHUQPaMfFr60IuzHqqwFen9SYvpojZW0e23zxnqzKJ1mbGptXWlf7vAT2dzEFiIEyrxUHyXEsbw71KCZ8fE_ZT33qBMeukmFuISLDgVBk-778OQVYipGFBTMpxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
قائم‌پناه، معاون پزشکیان: اگر بنزین را ۸۰ هزار تومان کنیم، می‌توانیم به هر نفر ۷ میلیون یارانه بدهیم!
❌
پ‌ن: ۳۰۰ تومن یارانه دادید، از ۳۰۰ جای ما دراومد، برای ۷ میلیون چه بلایی سر ما میاد ...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106682" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106681" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKk-sxc4UEBX_xE9vq6kmgVZ-VQ7OenR0V6P_xLWLk9zlOrg5ireOBoOsBJov6R0LCna0aAUiBsb8VHXi0AbXqyojbVotI8qqhSuzDbsXGpdTjpHWXtfed5p3yqcXqoVex-JKLM1Ky0e8r34WZoEgS2EWSyS70V-CUBQGuHFrVGAnFvhwL3IkUJbhrBxc--7-R7kejZD9Faz-etwEYm1yzXbm0HHm9V4O5LFg3Cb7pvVZrD7jqbkXMMND64hjarnI5PztoIDJrcLhmiLMHdogzSzjJKCOqpvP6uqoD0y4tIs8AnRenlqDezJeoVxFDrtzHAJmi0iJSBjhQRoVjuq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106680" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxhzeaX1LYRqWLLMEaR0pi1qKIOIGffS3ETlYKQGDapbPCackmou9Tbn9MC1oylLsPNNtsX_XGCbSxwW6vFL8bmg2QBe_Ei7jJeWXjvvCAncpjsEX7UH-qeFTYaCW6l0GmfeKzp6JqJw5ACPEcjwe0Gg2ePtAki3NCoV7sQMGaVBY5khzTLmPAjKqQu2H9YD7oP4lLYGnRZM335Y8JwiP-KA-N4c-yfZi_uJ8AOmnKND1MEOGMVzb9o82DRydu1duPdei9lp24yuXFJ1gGI9XvPz7s2ocwoX9_Mohf8i0Buj60iWNsvl52bqeTKOdVGCv86akddtJcCHQm5YwZGdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اعلام زمان‌برگزاری سوپرکاپ اسپانیا
نیمه‌نهایی: ۱۳ و ۱۴ بهمن(۲ و ۳ فوریه)
فینال: شنبه ۱۷ بهمن(۶ فوریه) در استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106679" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYATunyKxIXp4gKosNelN1KDWqc5gOLb1VKJR69mgnqO4Te4zOR3vS75ctl9bgaIuOueT50hNQJrSOMVykQ12whV5iHLeNWNHhDm4vMj7YKLWpAyFLOlZ9C1Sm8Flp-5W34RzFBNQV30v1GUKo5F5zwKN6P5_iMkH2OQtOO6dEW2MwYaiMXsKij4dvsUV7eD7mhn6fsWqR-_EWcMeQ2xXue6fwDpBNqrnJPwQ8uc7oJXGSzlY6JBsNFfDIOaV98-NTGtUlxiK5jzpUZ74sIKmcSdYI3SI5h6nBafBqFG_SRE_LlQFBlsYEjJf58vN3csX78ypYIlxnFb__kLw54Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه افتخارات ۵ نامزد اصلی توپ‌طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106678" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
