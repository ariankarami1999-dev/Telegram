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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 194K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no2yZW2qVKzBBkbQudfz4bBVT1I0xPxg8Q0OMJqJXgAdcbwJdFU9Wno62fti0oVc7kev8cQAEPsl1U4nq-pAxIkQQIWqUUNTFXnz0di_EurHIIz6RgxWww3Hahugyd_aF4DgabvrY4ilkFoJoO1Qcu0vW25I4zefA6_qlFWvsu3r42uktMTyDGGIHhWUGGCROsx1-R3-RMOnJlkILm9TqMO8WSVhqHbgwV5KFNWEieoyVUjmEnOv3FArgjiXgqf9cDY_D1cvnhzMf_SpFynWnFmVgZHMgINMuXCB568AuE3PNfPmXU68NpobLChF1dhR_6Ji6L11aG9sSoQD6IHP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی: اصلا منطقی نیست که بگویم من اینجا رئیس هستم و دستور می‌دهم چون همیشه درباره تمام تصمیماتی که می‌گیرم با مسی صحبت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/Futball180TV/91080" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnyLuufDvWI-LHajq8u4gZfm94b70LDNERZDihnsrT-KXfRNHv7U6ackWP2LU4O64ZBSFd9mmLc78sMeo84i5xYBX5_vxZpt_xR9nNBzsItaC0Y3bKG2ey_BuhpX-ixPzk8gS71Fqspi1tERaoYS7HWJ8rI7A5Bwh-_Ec7zGy8O9h6tunQmMW56ghABFsmADvOc9d0g8Ylf9NCRrQbr7vEvblDSY18osHMRkTUjHQskFax3y9N4oMuW_USpSwv4rohYRWIsB1P1nvStlMZpIvCFJ44VB3owkZ7CEJnaFzshtLlYAKcmKJt1iH_RCkXejEsoykQXKnzF3Azsdxszftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فعال در جام جهانی پیش‌رو:
◉ 13 گل — لیونل مسی
◉ 12 گل — کیلیان امباپه
◉ 8 گل — هری کین
◉ 8 گل — نیمار
◉ 8 گل — کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/Futball180TV/91079" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=VMjbumn3-AkjcKkw62kUsS86-MNxqWviKek6shHjhqVfTKFPzw-Nrq6_xHxPsL0R8yVkvCgn81VolcwxAPMeuneak9JFyOqEvPtvvGLfpQMoL20MVlZdysZf1YgaCpjJGx2E_3xrFBlfbCk9xvki2z5fcEOe6jL11tOnnngYd5PJd2vNiqLOLrbx80yGMxCUbHkYZqywXvkt0mnLUjjMYeE8V40o8p72t0eBiFNJgVFbUJKFyv667mT9bnJxVQOZZIuIsrz46gBfqNQDZWVaaSk8UwHA39riMa9dH-Yt-MUjNfXz5tUnah3lcOy4oRyHgQJu5zgc8NcAOtLVnuar9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=VMjbumn3-AkjcKkw62kUsS86-MNxqWviKek6shHjhqVfTKFPzw-Nrq6_xHxPsL0R8yVkvCgn81VolcwxAPMeuneak9JFyOqEvPtvvGLfpQMoL20MVlZdysZf1YgaCpjJGx2E_3xrFBlfbCk9xvki2z5fcEOe6jL11tOnnngYd5PJd2vNiqLOLrbx80yGMxCUbHkYZqywXvkt0mnLUjjMYeE8V40o8p72t0eBiFNJgVFbUJKFyv667mT9bnJxVQOZZIuIsrz46gBfqNQDZWVaaSk8UwHA39riMa9dH-Yt-MUjNfXz5tUnah3lcOy4oRyHgQJu5zgc8NcAOtLVnuar9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/91078" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
رویترز : ویزای آمریکا برای ملی پوشان فوتبال ایران صادر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/91077" target="_blank">📅 21:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlRrDEkQjDnfuTFrKWX38tOceA2yBGEReM-0-QurDCx98YejsKt0k88rTKsSG4zDmTivoh6D2T8aAlmHQNXHz_MEWuxLuTw7crlnPGRD4e1KPJpJegfJmhIg7w7NxMHoqSeoIxa2hoSPwEafwzs3Rrlj3QxNshFheGiCxxacm9b4fYvzQ_3okIddXXgHUvWAJZheDY1hneHySvub_Wb0QXH7wgkDSmAp1XHpMpsyzpA1oi7X0XZQ6kv80-UBzKXP5ODHRqWJdzqnHCH3ZRLNCJ2-YWm2CRpttgscKWmXeUnVAXCZD0LlWtLVWREkrIr9lWFpnwiWjfrcDEDJ2Th1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک جام جهانی هستیم و این پرامپت جذاب مخصوص کساییه که میخوان همچین عکسایی با کیت تیم مورد علاقشون داشته باشن..
Ultra-realistic TV broadcast screenshot, identity preserved exactlyfrom reference image. Young woman sitting in the crowd ata(اسم تیم) home soccer match, filmed by a live broadcast camera.She is seated in stadium chairs, leaned back, looking off to the side with a surprised caught-on-camera expression. She wears a (اسم تیم) home jersey with jeans, casual match-day styling, relaxed pose one arm resting on the chair. The jersey should look like a normal full jersey, not a crop top, not rolled up, not tied. Around her are other fans in stadium seats, blurred. Keep the crowd mixed and natural. Add a scoreboard graphic in the top corner subtle broadcast compression, digital noise, bright stadium lighting, and imperfect live-TV framing Telephoto sports camera look, authentic televised soccer crowd shot, natural skin texture, no smoothing.4K.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/91076" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
انریکه ریکلمه: بند فسخ قرارداد ارلینگ هالند کمتر از 180 میلیون یورو است ، اگر به عنوان رئیس رئال انتخاب شوم او به رئال مادرید خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/91075" target="_blank">📅 20:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=BaQbK3ERWmP4d4oVMBvs8SkPSYeuc5FWKQqJWIz_vXknhEqSoXGo8RZZNAE15_tGgZ7j6ZEOaVO9-z8t_Vehg3OWrmVcrJDCQcvUhRbKC5pNXcy24Cz0LdiYzj0UBc83NgK-fDGPlLC76UXE0oy3MBRjg4J4mYZrAEvbvaOCJFx3rT0RNaEb5LugXRJo-PSyZBB0Z4NnZKwIfR6fuKXy7tuQ-RhvrIolkb0yV_lbvrs_3SpkFpVqxBcPQfPOQruwkh5dgTzOss93j39ilZPxYMcjWKqlX8qr4bLK-75wpcSbnLhAdtU_Ha0oxnRz8ULnY2ap_O92owpK-HzDTh82Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=BaQbK3ERWmP4d4oVMBvs8SkPSYeuc5FWKQqJWIz_vXknhEqSoXGo8RZZNAE15_tGgZ7j6ZEOaVO9-z8t_Vehg3OWrmVcrJDCQcvUhRbKC5pNXcy24Cz0LdiYzj0UBc83NgK-fDGPlLC76UXE0oy3MBRjg4J4mYZrAEvbvaOCJFx3rT0RNaEb5LugXRJo-PSyZBB0Z4NnZKwIfR6fuKXy7tuQ-RhvrIolkb0yV_lbvrs_3SpkFpVqxBcPQfPOQruwkh5dgTzOss93j39ilZPxYMcjWKqlX8qr4bLK-75wpcSbnLhAdtU_Ha0oxnRz8ULnY2ap_O92owpK-HzDTh82Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
وضعیتم اگه یه سال دیگه ایران بمونم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/91074" target="_blank">📅 20:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aphckmaqQcnm5otirqOPAlWPQKVLubxU4Pw9uf8HjIP3E5Bj1Zxfu9xA7-8dAb2K4jZeQK_n6IVphyiXcZFECVHAZeorrMMarWfos-Ly-j40Hp6U7mm-tT5PX-iiGd633BajviQeZuEZ4_OK_KH3RhDR0kAP1hdxj8G0T-Pm2gwVR90WQtUIMsLQVtQBH0i9dUdnRnH639AZsfrD1Z_Jj_W9dvCiHAPG8rOkPSr7VafaLmNcPnzzCi0XpwKfq0NzZ6I_XffOOftbCrtYDf5hA91c8QN5ZjGO9G304IOTf4GO0OM1gzi2qbMqWCyrj9ZftVSTzcJ8FpbCgrpOE_alMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6A3P8CPbe3-oKuDO8fw4HSNtKW73Y8h3ndNjBLB6I5xaY5xGS9AC-UNwtxFJbcm5L3A5uo1_oehh7khC_WBQuyrptvie1wHKfgthH1wXZpd6R7U_AoMY_VLi0zAKMoOzRkuPxM2RKGmxBb8UohUuNHBIQj1tAAVYN9zxdGhufwMi0B9z-dnf4OHmqGNcde_7PFLtgYVrOgLLUKmkV5yIafQTsGDybE5bRPAjY3oycUQH0quhl6Cjaht4jmAfdONZyEvayysoSzbdt8fhMxGhxkquq_rwPKNn49mfMrP2qSKgZpGVhvwYAkosLWxDp4Ns6IZBx06108yAG3XWGrX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMEkrP6a75pYAysLaGAaq-rguqZrCXOSI6UXQaE_q93HVJWdOq_RMXv_dysnlbXbX1rahrUN5Z4Kwhg_PKZHy5TFRwZBgzWx8rE2NbOFlHhsjyj-v0bdIllZntEnF6YFba4UzDgTD4jrihS8am694_wlXCnvQby_L3EfwIMz2pqWRnkF5a1pKea_nuO7__K7dHGr7YqfxztMjeSETHu1JPUx3gPADFnp_NTsVffh_8hSjCINbP6BtYuLGXWK9XGDVRrc_Dlex67bWU6igmGMhFTmjXbrJa-33Bt4QWk6dF0ujzGZEp9b3yqJ6cl-mzLLE2JT5n3nBi2BwxQgFRpdSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap3Ol1pMRuatjxgNk2u5xTY4OHtKDabYo3JlOZdkFVNlnZ6iCwel-a-jJoB4a3hIf4DjPg1QngurG-JtR7FvZ0jghbXobFvBpfIRJTPwySWRZg2JxygI7Hy_J-JqEva38fHf7R1Bp851Zvn8tn0cKGQ3RJoW0tIiif-M3km9MoytkSyiXqDrNximDKlIr5cSAuBuo3HbgC_RcV-GY3fU1Xj2Tkps_DhediqkgwW5eJOmKV9XL79VyIEsP7HF4GGVuGW6130ed2FICmifO3devkvldbKx8b17k9pYwLeD2nDR6Vd76Sf0Zdgfb7WzG98UOL_eFu5Acc1oVCurDaHX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F384hMYZLKCC_-DcridnrbhhaYTZkZABmGqm6p6Rbbf2JqI1t3nnVrPZfxHThmo0Rx1eKOxgs0ACp5LF0F0X6xd0O_ziD1lTu7pKhwJ7Il3BkNBYoF84gYXTwzx9_LZbzHus9-jluA9ftQssxOVaxWAp002mXmkLLClztXXK4imq99UIFFifV8iljj4EVe69ouLMFaBpFNj2DZ7OkRuxWy99JGG1DPTT4r5UgvFshOJ7JwhIjyiw43sJ6jVwVsG4ccChJ1eQDkYZBenIJ_EuMJI-ThBeMAD775CFHtxSOU6Rx65eMG1eg_LUlfMQvXD_pZ97VkmYx-0NXE7NZAWOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7uoM7b8AQU-RQvYFA89JoBXM_ky2z7HRAwnqVDeJ3_gK_2LCNdt0R-Y7Z-4OGwAD-g3mczkTKsYL_1h2789ntbHyrNWzuBSZeIsLjKJipBkOQxDRCQ7Wyd7Y-_uKk-QzJkwUo57dCl5958-WzAcE69V4RnuIAB6W25tNvHeuAc24wbAqT98OHZSM0nchQPvSy3LjCzTSJK8WDEJJ6ZiqlVABXNbBxstKjTkvWfbWF512LQIholBcsNnZ5hdSc-qmGxMmcfIROXSFsX4_K-s8mntdWzxooqjrYapnJVC7cClLYV7NPn2ft2D0uHqUo1m-Rf9cpbSPQjno1MEuvva-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-JlucDLONmNQ9VhS5KOWCOxHCWoRkqMheosxtaU6RMYmejwbe4AaiUFUoQal8HzKlGnIPyiqdGnALVIjW9W2mQ-hjNDbXnr5D49dhR2Yxp-EfIHLsbeMZRyxAiNL9UosYEXWOYG1oxec_8bFPpJrNe2f05o6LUomi5Vkxd8zbPlX71Fv2uuxCaVuslAazMqojIqW5puqb0safU5dGU4-FCXiL4NZBW6Lk23SezglFEp8dZQ_mcNO-IS8zA3KQjTZzrShrQ04LlikXcKJ8fs20GuviBbB377V26UYlXUgMUDYX9h_UHYvorXR4CUp_8vFD-pEmrpTTHyQ0fXE079GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miZltfdfdHugk0inuA3dGJ4rH9QH9KrYcq_C_S-g_tHMc97e31xpWQ4ESrYbVTv2n9DyJuSk9sY0Dhssnx0y8ZyImnaRjLt9UJoYaXEbUBV4XcVkOnIKeajWJRDHTWM8-DK95VGKDrNUDFLVaOG3TIunRGjLv2iO10Wv-Qw2RKLB_bSD5QzqKTRaSl326A5zZmoPtEH3zAEZdp7GRFYCyEl3c-XDkO2VoKWl2MCM514s20vSdA8joG3adIKjdITd-8kQ-ezu1AvknI12sz5NaIoiZEG9n7BNz-foAD0D5iysaNFkwB5WRUs8OP6zypyo4M6ZS7Iu7LNVVwWPywFLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5Vpd_FTwhxARr5QGPi-J7jb0qJUFpQ2xQbCGmtzOkpBSdE78jwEMCpFBSmg1kni0T9Ty2pwrNUDYlq7XsRCLDmMoZ2EQ-PzxBKpxEi3H6-QgAnihkmHQWRElhK4pvSHAjgn0n3f-RzogLXUWrSeosrTs8tgPYjexWEqU2fHwEqNmQ2jG7n4rCiSKXzt4lK4nOZGlvjn83HttBJZyMCgmAq_AWWtsIP84DxWWUB-TIskzX3zTEDE25CiZAPOtYI7n5gLQYWFEDKMOejWRqBe9KglmYCbWLUAXAnEG2wYahTk3Amg5jdu0QRv5FU-Or7QiMRjC3cQHdBSG365hKSJSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdHNBeHy90jzZtq_Tz1jDDsgiyN1Aft-tfw7SP-v5caKRyTxKOwe0rK_zA-72A0rlzMK8AR9imJrh6V9E4dZWuFx75blWTNb0mxCL0C1iCLaidDDuGEmNQtIp5krNr9iUfKci7kJnIC3uCgE2AhfZ1HoP_Qsy6qM1QeND-YtvFtPcnbAne6XaIDL-Rf_sfDLypfO29omoCLAaR4I937qFqXgeRjwkRU3KFs6iOe7bYHB1hsGtvJHZI8LbJ9nJfPcZvqowrynK81LiALYBshQ8bm-B7vqT7xMY24AoUNGpWZNmLMOthoer1JwtStGfhB8CfBR54CdJ53R0O7IOTSqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0-AG7McBPMdLRv9WvUSaF00mxY8vYyAP4lDdfXKI_VaZjN03aEDyC_oYQ_unY6SdfwGisAqXTMwTiKCTir6w3mHNOpUnDratlBoUx4SibBi2IN2HCMcF-pNKWbGujVv-_jsTmlVDOAw77yQEyE0AFGeJnkiS9wxvZGL8JzJa-fzFbcv8_zlAmF3oSgI2lzMcsnirk4QBJYyipmHGnOQtrVNCeHORA60BYPK-E1P1Dya6mLxazvjZ6ifPqq-vUbghka7NlAaIWqMCn09rni-5S9BMk0vVcEsDa3QR6nQkcEt9HNcz_Adv5kK2xMl9djF5PIfRfYzN23w1a6DTgCU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fZTntVvx8S-Kd6RuktWM9LzF9gsOuIgcE4Zz2b_tMFI7MBLIyXrtdcclj8kTXb94TeSge-LWAqFPpykik7EKGYSlqtjYx-qBESsNLGAXtVdPMlWnCyIPzrWzkMrxLUjzUagRGBbKHlDpbrxzl0OOfsuzoycX0kvIE0Y1rbnlsZQPtxDQCdchTQhvgwWrpnc7GoBOJ7yICrFvmYmiRWs3hG-jHVIxjV0bi7hRHPjvd-ygV2J97oceqIZtLyj7FS-huzaeF1mvvQi1UlXKjvrc62G4BeWb8hwfC8nbmsZdfe7bHzPDHS_TrSNXxF1js2oYyXPhMS3aDANf4-rpQcLQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVB3qOm2gmblbapcme6IAniEPl9nY-ywYYqRE3ArH8rwpsMXk9HrWLo7D5i2U9_GIUHHGG-jaiiNLES9NaSeTTAW_TPRfVMD-_84clrMLuJtDIP2F-5knP66IpRGvXxtVr0vayM8n75igDtxLFfjSgOU1GdaLMT8vPEb1MsFb5bo0au0ClaHJN9zqPy16PslUUo_rAcgcTJczDdXGxHv98nUXPypUPiqrxv-GVONJzk8W_yUWWo6p3b0Wk0rPt4sPtykegVEoqk7l22xyYeJajynd0jzehrYrYL2AbX0KyoqonML2g5yeYVwGxjy1vEDTLkGjHcGfi3SJlX7pBW9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNt3scJKMfOMzOA3BvurucTfsb1Aa1hqs13WI2qpX9kiKYlIr-eqntjPjL85TDnqbf6BSjOcobeDl2VyIgjCPBwHlxx5QczkyCxQqVCipI9iWUf8_rDY9KMEPToH6P9dkTpkCQZVIuNeisNeFG4qNUTjT5K-pcWo4iuyd5VOUazjqLGrbAr_mxGu-oGRNCxJqzWIxwooZN8jIZwbE5XIUpBlcqNGTM6wg13QSQvzsyz1uMzv-Z9aND1nsvfddQpsQtGKGiXT-PZMLYfZBAjgkape8jjfGuGlACs_iakr3iRWT0x22lhjzTelw3_TMavP74JbmZmwZA7HQ6lJ5U8qyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mKLnBm1HGIsuyKMCM0CF7ANrJKKXI5Gq1MnYFMmFj9n9AFE56V_glBfUA8KylcxrHipendiRiFicZUJ6yswKEWtZpOZBJMw_fMpDEmH4Y57ffdi6sk1T-tz6ndxwg78Tz5oa68NDxb_9lT-trEmvaM9IRT5gAR0BaZSBKHx-cau0lNEnNj2lvimrUJVRbl0V2PCdA3C8_8-eoCJ-t6bynzBwKZCkO7keYbFm91LdNSgcaIUgnsaAKsQ4w_wpLyl9TxxnA6-fCENvjYA9LqIEjZiurMxighdU55Lt5W9vbuOyLFqlisNJD89TJkAfXwHzV26Z-knGz5SCBA1wZo7s1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mKLnBm1HGIsuyKMCM0CF7ANrJKKXI5Gq1MnYFMmFj9n9AFE56V_glBfUA8KylcxrHipendiRiFicZUJ6yswKEWtZpOZBJMw_fMpDEmH4Y57ffdi6sk1T-tz6ndxwg78Tz5oa68NDxb_9lT-trEmvaM9IRT5gAR0BaZSBKHx-cau0lNEnNj2lvimrUJVRbl0V2PCdA3C8_8-eoCJ-t6bynzBwKZCkO7keYbFm91LdNSgcaIUgnsaAKsQ4w_wpLyl9TxxnA6-fCENvjYA9LqIEjZiurMxighdU55Lt5W9vbuOyLFqlisNJD89TJkAfXwHzV26Z-knGz5SCBA1wZo7s1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt4RW7olhqfVD_mVNUe01ya8Y6d7SW6VtsVSyswS1KRDKpJYqU0nz5D2f7B5XMr_yQedomd1zhVcRnS7ir3S1y_7kUXMTBwktkgLCYpvHAd8X7gNXCu9yFXPpSHuH3lopEJcQ-L611JCUqAQgLkQOJsmT0m4649BzeqkdjO9meoB4M5o_aEDGOigogUq9g9K18K78PgtO96MDceKUNCVy-Z8j2lh8NGrYXbXNamvZqlj1p9x9I4cbQ5y5ZxhIyRCzSw3Ga17qAL317niQYVP3-0x_Fm5obkVMeAtJTJI5ck8XaY7J5C_zA0i7xuHywc33Hcz5Gazko-kRFiaPZcKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEaye0KnzEWVHmfc1S5055vVlw6iHTultptwEZbxyenmMnfXSyjybKugfql6_KGNR5hvcVXEOcpntlx9XT2XE2stTl5fwU4mJWegsNymhmJEpFMFVA60z8hjyvZg1270jnN0cwvzEv4n8LDB_2hxgmI9xsudVcvaQCyJl3wj0y8zzSFofs6uAZgTOSwHOZHfrFsjdKC34rTFQZhVEhKmJZvBnJ8SkG8Uj7EaFwvJ32MC_Kt3_f4jZSYfVfqsYJ5ITFtY8DpITfX_jWtd5uVSRqiv2OO68S5C-zGoiY6JkktvBBJdXptx12g1OeF5uXf0ugEGY0P2pjehrfzFfSjyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUm9h5Ds6ruhpzNTEhL3F9le8bgA1Qy6kOZm6kSB83jKDRSC-xR0QzLRw809IzlV5l1XGKEVk6SqHwDkntUcCoTwld2eNKWgfrWoGrraZDqYkxI112D_otR9ku4NxKnIFPy-46Tp6Vzs_o8HZGrq8adGENrFfVcl0J4wmYYolLbf2ElmDMJnMgFy1qSrRqOWeEO8zfocUtIdQmESukzYSM_zorTP98nOGwZLJDoITTrGdtmB8ZgGDno-X1D84tTMrhAkhkVxoYihp40_zFLG7g-YNd9PXjJxrAWgXPhRGbR7DDGggJzDNWPuiV4fYJwYEgS98mYfe5QkbfnUCfcOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_faNCsC2ivHnZla_mukdk5hPg5ZygSbfS-M1NslFGUTig7WhsKiuqKX0-sHxx2Mi9zTpG6sNCJYNssEONMuJIGT21TRLZXC0i4w0z__uqjE9gPHFq2Mg67vZLrrF8Kz1TuhLQhyo5u_mIfaiy2TkZlql0SD46LGyLy-UK4JJyRgdKVO9hJlnT4Z6kk7MqYtAiIEd4OTipw96Ff0BsDwEY5Q66QcmJ-tGoesaEtaHua5rbe5FuRKLKd6QOCmfYvJcUaoUXegJokEVbe83TQlOOz0DJ4XDuPlSVcduodzEjwLITu_OV7Ny1mcWRD59CK6Mz7eB09qa3XPZIzf-o47Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDVo76YQX28_xVZSsSGVEezzgssvJ5Y4GNYxjMTri6NMM88tG4QlOI99TrMhB1epakKz5q6YS2nxj5PS-yj7k00hST9_SwlfikBW58PX-uP3KG9Xtaspe6JVHtzKd6G1pRY8dcU0s0i-HpVD1wVW2GycyRDr-HBz1Dr1p1zXQZ-tugWpe6kVXz6X3mB17kOFlkCg7mE0IRSm_mvkwLAlYEJw6D7Ls3BWm-3NEby_7th_jrBAsYIMGEQS9ODiS9zGDRaGhbQm6e-vZ8-1lKy4QbKiX362TaOuB6sqoA74bbrMGmnIKNyL3_r3ekQg9R7KRvWiQKdFTy1rjd6vxDXQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joTnyOdphdsnuEyQ_6Q_o09csT6vF3qxvx8ooVKT8wI7XrDGIS17hJTOOWh9xc6YEBf0UC2sxjcUaiBDJiD7xINyis0s8XiSzr4dTe3acD7wslgotg-MxvQjnKsqjCk55OYE9yspb1xcpko475yg124awObyojXb2sNle0ECtcZM5XFdr63_5AmXNLjC7kccu4lDO-YYMyeaYXEs6DjuFh9s4kIat_teoB1ue0IqFGdvXYBdZK9gwpoRnccKVvSOqOwnuyln0Xq2954kW2mfNmlzpzLLKjUDB0MWwxbF6RTFSskjIP3axAY0748RBUwjDzihGVGNouSL7ktl9Sq_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8frmYVv8FV-xuQHuyjGiIcWEFLAH4dT2ohBBpR6Hj_PQTBsPnbTCUBOKAQ8iw0wttOt5E17PN-6kdn3DhYYI2bWeYqqkIUbyfNp13NLYzWpEbZuOS7TQuKBCcxIrMeMUoHSND9kwU5eWR78jIdJ37U0HnkIYze0mHNftbyEND76qxiNfLJffkJsIg_VIyBV4V4DvRxxH_TV7dzLGiyl943i_MPlfIwtPOSXf6buXmjd0hRUlAtZXGwDmu5eM7ZpPZdLzxN-H8LQgXpcFKEei9_jYSvM25JyOW77B0pVNLd3Gwfr47YTbtJqvO2a1jNIRTg3NdOlOeBME_q1cmpGdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هازارد، استعداد سوخته
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91042" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ujkvYav_p1cCxKVUkAokXo2O5lQZHv8BqlL80IBr-en3Rn2hCP02Ol6nrQiOx3RIU69ih8n21cmga_H0vdQ312x94-ywBwcEbNTmlqgvo5U4PYj7nmekKIvniuav5ahrV5C_Hnh0-yJiXbEknfDwPNbS_2F4bcbNVYfGHWgD5wimLZzUHI2iRvUFo5ibWaqX-KZNAANexwhW9JPEseOtqLe3OAXaPyR4SHjcHWDL9d0P5oR2xquBUOar0rp043ZmjSW643k8PjNJ041aCol5x_QquxXBu3ZwBVlixXUJ9y6Z1dTHStcXgfpVPj8n4zZYDkXwGT3odX7G-p1roWI3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
یامال به عنوان بهترین بازیکن فصل لالیگا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/91040" target="_blank">📅 16:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxBmARQhEIlqkNfpEnwA7iWWOwhTzsk7FlXGdax7ayXd5QZPna3wioaxzawLh7HSOiowKCs99Fszj-pXv-cCCWzjpcPmJxZAVQTK8RZI4NGlllxpDrTUOMsZBXMvScTLvcZkQcXqDzTOwNvOhYy1lcC4MXmg36gUdULw-IsIX4li7uXhmkHEjiGxqVI-vkrIYxs1pUGy8hbzqP_8js5-6FDsa5w00OQIHfqF40EpReoRPrrRC2f3M7nF5TaJOpj2a9c62qHvd-4DXrJOWezz6a_NKVzHYdnnZS-A2yrPn4FjulD7zTBz5j060piWhgFZ5H_mb5b7EB6I5olRXBoICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فووری
از اسپورت:
اوسیمن به بارسلونا پیشنهاد شده است با این حال فعلا جایی در برنامه‌های بارسلونا ندارد و اولویت آلوارز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91038" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMM7LU8izk4BPVmFJrXSw2pBMlZl2uKSNCmnJHMOTqO92Pj-8D50q3XJNWQl_7vit9wb7Jm7dVpv3iStKPrQzIpEvIPYIiB8MHijDSvxHn6aJQhQX37_IJnFLAGTcNptwuk6NWQGK1XzYj7FYbcADb1kjUeavJjYFg3utxOHSl2dYNwjCWIONr0hVrP53kH_tWndadP1ibI_IH9-waC5PLA7qh0PEZpCqfi-dQIq1bXwDxTuELe0I7Q-KdGIY8TVb1DsHYcbg5UyvYjxF9VA9OaAyiavi5tn6klaz79bI3S0rFQwXwdJonbMiQz3nTXubJDkMWLkPAKast52EQt1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه زمانی حس ناکافی بودن داشتی به این فکر کن که برای سقف برنابئو 600 میلیون یورو هزینه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91037" target="_blank">📅 16:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUToaF1yXLA9SWyStd9TPd9JuwK0Wp_OwLZVQyvLOwFACdMlX2Wf3ZUPrIKootdR7ppfK6BKcxfBYe8TWbLsVgcg7n0-5UBP9XRmXgPpo3wdeUdqyR8A-mwqmQOUKk3gjk_OI8iRt14IroMywhIuFBmR2nSwiddoqUfqTy6m3-rvFOQ-kBbrw6SqWpBjj2PIljRzjukATmJ-U-MBmlCy0nqMAXA92gVLBNDUl7xhJSaPq4qxHCfSJ28t_61WsKUgenl4jJtiwQz2Xe7_X5GnXZLhRN2Iq33RJ-mVtDVkO7zQUR_armDGDHO8jQIUbN0Jjk9JZmLCmAl2G7rBkxeBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل لیائو: من یک چالش جدید خارج از سری‌آ می‌خواهم. لیگ جزیره را با دقت زیادی دنبال می‌کنم. اگر فرصت بازی در آنجا یا لالیگا را داشته باشم، واقعاً خوشحال می‌شوم چون استعداد من در آنجا شکوفا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91035" target="_blank">📅 16:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01837206.mp4?token=qyfnA7kStMsnpC1MPzRDS5Cg0EYSnxiomHA5sqUaRMsLsE98sCg5PiNbSKIdjwk07o8mBWVaU61EQZi3oCIvmis7r2V5da7dU_9qmNj7CXZZsETh2KD7PxhC2LY5Mk7aiJCnmaTb9toiA_kedVyN_6biSoi0J2wDXgTfbm7z98TRbIkcAsUd3XXc2pfMbrf9K9IA5AVo3KVGd2wHHX9HuBhw9Y_rWuPGFT9C1v2zvg-rSLp8dj-dcMJnaov-Q7J1IyMufmnrHZZYA1jmCxZr1aVJTRMI5QQUp4eb4pgdWkgDq2v7xAi9VO43L30f5I-EC6eFOKqWSazhoGeHHZobJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01837206.mp4?token=qyfnA7kStMsnpC1MPzRDS5Cg0EYSnxiomHA5sqUaRMsLsE98sCg5PiNbSKIdjwk07o8mBWVaU61EQZi3oCIvmis7r2V5da7dU_9qmNj7CXZZsETh2KD7PxhC2LY5Mk7aiJCnmaTb9toiA_kedVyN_6biSoi0J2wDXgTfbm7z98TRbIkcAsUd3XXc2pfMbrf9K9IA5AVo3KVGd2wHHX9HuBhw9Y_rWuPGFT9C1v2zvg-rSLp8dj-dcMJnaov-Q7J1IyMufmnrHZZYA1jmCxZr1aVJTRMI5QQUp4eb4pgdWkgDq2v7xAi9VO43L30f5I-EC6eFOKqWSazhoGeHHZobJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
🇮🇷
یه هوادار مصری اومده به سمی‌ترین شکل ممکن ترکیب تیم‌ قلعه‌نویی رو برای جام‌جهانی گفته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91034" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaVuLc7EDU6jRuWcyjpcgYKrSQtrfupO4CTRJItVeER2Wmqpukf3lOME4BICbZV5zG-vVNF4GrsYOttmGjZwsJWC9BSMt8P8t2qx6r4FeAluBO_Nptj8ioM-suZTdJUSo5EFiXKvP7xJz73gZDKU_9DWa7In60340j0dSj3k7xgvVXyd7b5F3OyZhrW3UYGDF_APhTLK0ch22F9HJJTebbrQG_7zJVyxtW0r912Gq-idCTaI47eWmkX3tPIk5XXs4gkhQ1NiqD9Cl-swTLmAEE8xurRIniSkx5I_iAcrP1GSBFAKwSTh0Ik8dVP_9MJ8PvPcpVty2I0bbr3kXBViXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه لیونل مسی در جام جهانی 2026 پاس گل بده، به اولین و تنها بازیکنی تبدیل میشه که در 6 تورنمنت جام جهانی پاس گل داده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91033" target="_blank">📅 15:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk_E7A8NXmyXR7J66JN50okU6UICElODMsNeswIPb4qFmY7nFgY6aZFiTohrbpu8Z2v5ZFqyu8DAFQD_agkfVHAmGAZj_YJufDZHPUyvb2Ak0msFcIcvxc-1GZgFPESSDRwBdkGwYWLqQPuyJPTFV-fG2mGu_J3qlr22aDb00j5kDTnbKCDLpt9Np7j4qMHqPgHs5ZbY8Duwkz7nmrCgnKSW7dZcsdXyjlrbnUl2Zdb3YVrTBqDS6aOfuR5tJqEDHlREXd13kDsdWgQBvOsLDnKM01lBZENwpdbplOc2p2SvXkEaTN6DPOVBLWRaOFnrvhMhrOW2kmqzJbLbCn7MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی: اندی رابرتسون رسما از لیورپول به تاتنهام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91032" target="_blank">📅 15:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltCqq2vdc9f0l-Pnl-EeKfLraYGclKMcGfPpwsZtOtglTkHyOWLpiFWdhbLQy8M-EUxfbqg5nmlST-FA7GWuf3HbRA-xo96cDsIQoAtVoaPQ9qkxAPTxlMQTSA1BodZ4PIEtkZe1vw9kjBLZ_nPFv_m5O4EHs4E-UND3VUFmU6xzdjOrH63zg4v8cq7Y8Tr7P-ClHhpp4n2Zo4xGsHn4fZJ-cY64pQ4e-BpuNjFiVXriZq-OZt47BVgwJKvGtZMA5bCycpPWOY5177r8qd4dI8wKrTuXZwdot_JtUOvhC7GYDrzObVoojPfOM9sylX28BmJLiF6KqgZ1slCgBve0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇫🇷
#فکت
؛ در جام‌جهانی فعلی، ۹۸ بازیکن متولد کشور فرانسه حضور دارند که فقط ۲۳ نفر ملیت این کشور رو دارن و برای خروس‌ها بازی می‌کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91031" target="_blank">📅 15:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ از یه عروسی توی کرمان وایرال شده، مثکه رسمه فامیلای عروس اینجوری فامیلای داماد رو میارن وسط و با چوب میوفتن به جونشون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91030" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM6eKXM_mT4N1JwDhws7HWaw3cKcxaT5Rbo2WYSzPy-i3KhWUUqmj0idDzJG1IyGzElqRmnYTVrTALgRQ_I1klnxNqZrIrpWeci3HHEvxVHVYuYTLohL0HFk4CfafeVEU6PoSaYq_s-2d3nfRFa7IgL1ftBELbO_avOma1t0T5F24gorXI9O-4jXqtDtBwBTwblNjSfvgKZHZSjUwjRlV6PKsD_iQ2sxjuL2UXIBfOMLgTz1gHuImXMJz8jXkwsoFFGufFC50bwQRCRtaqBaLFpG73tA_mo70m7MX2ypX4L4dqL_7-5OCm4HDjDqJ6uKb7Cnu43jhEnNCw4hhdpUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXEY_dMMHQU6PgQ5b7joglU0cS9Fwkm1q8pZRcn0HcNINYIfCHVkSYGzqmggkjmMV-K6kfalopHaXr9N3_KSHkmdKQtEUSvs4vIHMdLkDUZ_9aMmEubsQKYivaPguTgZy6oRbOuMpqZ_7NLaWquIrgMGijXhJL6e_kdBWiv9Wg3zAxnVmjwLXt--XO83bwisxoPLluo5r5L0qiXn-NbjuU2XNQrIU3sQSC8mRyfxLJNEBOk2D-G2EquWNrxtE4E2yqsQFoswm4386RxGTa8QJm8sng7jUInHCsEd-PMdjouVQV_t3zXXbOs7RQH6mz69uvYOVGzdX40qvM6rDhuxKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🎙
🇧🇷
جسیکا توگا، دوست‌دختر سابق وینیسیوس جونیور: «بازیکنان سیاه‌پوست همیشه از نژادپرستی شکایت می‌کنند؛ اما همیشه زنان سفیدپوست و بلوند را ترجیح می‌دهند. هرگز با زنان سیاه‌پوست رابطه ندارند. چرا اینطور است؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91028" target="_blank">📅 14:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=LrkMRZrL7M8x4jSKF0iVw1kk_xTztQGaKaGuJNA9miH7kfO-opqRCGjZHnZVAvsOR8C9bg92ap8jalKY3QRlD8YJptrTfxENX2a-4oLRqAy0DIN5IgTCOAnk2PqtZy3xEuMz_rJGCR5LPee0cV007Eiy8sKyKngwP6h1VQUMWsf_NXIk1z2ebTt7Cx25yvHJPreZc3fr_VPFQxtjIasqE2MDl7H5ImG9GsqcR9Cko0kbbciAKwEtGwwicvKiA1eDZ6fV4US1dLHiQptAyOFEapCKwAxWsNuLJqyIpvOyYARXiNMCozD0k5MVcaMsI5NIZGVP0rQ_bmSY2k_ygTIYjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=LrkMRZrL7M8x4jSKF0iVw1kk_xTztQGaKaGuJNA9miH7kfO-opqRCGjZHnZVAvsOR8C9bg92ap8jalKY3QRlD8YJptrTfxENX2a-4oLRqAy0DIN5IgTCOAnk2PqtZy3xEuMz_rJGCR5LPee0cV007Eiy8sKyKngwP6h1VQUMWsf_NXIk1z2ebTt7Cx25yvHJPreZc3fr_VPFQxtjIasqE2MDl7H5ImG9GsqcR9Cko0kbbciAKwEtGwwicvKiA1eDZ6fV4US1dLHiQptAyOFEapCKwAxWsNuLJqyIpvOyYARXiNMCozD0k5MVcaMsI5NIZGVP0rQ_bmSY2k_ygTIYjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
امیرحسین ثابتی نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم می‌کنند.
❗️
اگر دوباره سایه جنگ بصورت جدی روی کشور آمد باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91027" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امباپه در ترکیب فصل‌بعدی رئال
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91026" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEafMEN09GeMpLdPEZ3Z9r1SZOnUqsbvzdb9Do0JU42z4ZSWSqXMwXcwpjn4ep3sD9aPf-2UGMkS7pK8U4_DQP5r8Kd1HHyWAfYWATxrn159FW52DnNM-fU6A_ZpnTfJwC6vQdLXp6RKWu6PvEIF7IL_I6VqXKO4IpnLtKONawMhscc6B_A2gCUasgYzUCyHYc8gyc9yTI4Y-YwdRbImlcVyNPzR9CB_TNX7tY8FvLJ4JJ_V3NAqHcOLBkJxpRgmk5SC71tPZGsSQprIiuQZf9XECV2xIatEvH2NAASsaOo6P9-684kkp_f7sb7QuvqarCer1Vkji8FzNggvwEv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تلگراف: با وجود تکذیب‌ها، فلورنتینو پرز برای جذب ستاره بایرن‌مونیخ رقمی بیش از ۱۵۰ میلیون یورو پرداخت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91025" target="_blank">📅 14:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91024" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFonJw0zwgzaCxfZ1EEsK8EiLxuViwWEQxZq0VfI_wdtC2mM6_6p4cfeeqc37q26_ajJcuXok1Hdk829VsSdeYaeUCV6OICJx0SN1qO3PH4xrB2eOE6MisETbmbZMso9tYAi6UVOvBrsOGxoljqBCi2vwqLaVtrV8pxzKoM76W7DMeSKzwqzKrry0FTBSRS4_WqgZJ3SwlIyLxm5cIQelXh5GEu2eRAl063sVCstrKr8mXLThtsLPNBARIb4d0okrw_rAZpt2Un1VhQAflNcaFx-1KxH3ddTAxeA9xEVb9cYvPLtPT7rgcMWIm36AfLE-qjaAp0RwQfw_uU5Y7lmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91023" target="_blank">📅 14:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0gVuPnKY4_nw5FXYX1Tb9B8-4BVj5D4V2Y0_V4DLfL0_pp-1vZ9P9W73WbNiJMBRw7KOCvsp2ryKjhfFTBEJViok04Wf9x6ihoFMEhzm8eVzGn3IlqQ978uKxJk93wmw1ammC9rVJvXncNWveppChqemCl4CNifFTuP2zz03sKqRNetRILOqaG-RBznO0yyHS74nfsx1ozFTkDM_x4uOnIw_W5vhls26mmDn6GfDsAGxGkdGuhvRhKrL0ZekQU9gm6UjoFOzOIUAnymKdSBkJ9WQrkCUziv6DwYylHK3G-yo-JH8f9eCe9FWCmLdUWjN0vNJMt4FA_rxoGNFBD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان هر چند وقت یه بار هوس فحش میکنه یه استوری میزاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91022" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهریار مغانلو:
میخوایم با ۳ برد به عنوان صدرنشین صعود کنیم!🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91021" target="_blank">📅 14:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=EH3DolpqabIHUNPRvy4FnNCpLW92CY4BQR6vydvJ5IAY2LaQUBd3STIjX08YVOGioTJW4QmC13yrpm2_eoWAYsx2S_SURGoMdJDYvELIVqI-vw5KLdVrWUY-aOQ8dMg15KD6ruCj71XuMGnVOj5DQBPd33QsPsWkePP_DyxL9j-HllK6z5c5JNmEMfTsKj01SkaAkgjPenYRokDD890ayBQ3ODLZ4-MQEQTSBPGhUWcwXIwWwRtyiIz25WWsb6vHHv8hcTTujG652ax7mM06cUA3ySYaYQpO-fZA_r6T8JTr29pwea4sshpuvLOikLWoacQCTjPPVPEZVZlo3qYuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=EH3DolpqabIHUNPRvy4FnNCpLW92CY4BQR6vydvJ5IAY2LaQUBd3STIjX08YVOGioTJW4QmC13yrpm2_eoWAYsx2S_SURGoMdJDYvELIVqI-vw5KLdVrWUY-aOQ8dMg15KD6ruCj71XuMGnVOj5DQBPd33QsPsWkePP_DyxL9j-HllK6z5c5JNmEMfTsKj01SkaAkgjPenYRokDD890ayBQ3ODLZ4-MQEQTSBPGhUWcwXIwWwRtyiIz25WWsb6vHHv8hcTTujG652ax7mM06cUA3ySYaYQpO-fZA_r6T8JTr29pwea4sshpuvLOikLWoacQCTjPPVPEZVZlo3qYuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
ویدیو منتشر شده از زمین تمرین کمپ تیم‌ ژاپن در مکزیک که کیفیت خوبی نداره و باعث‌اعتراض شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91020" target="_blank">📅 14:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_zhLThUCgLUcLSt66kU8WnJ3pBcR9l8eliSR4_DDxX4wz0L412zlG4LiX5gLPVjmD6NOopu-cgAJrjjCoFcsTWLf6l-5H809p095pBfwGnlNp3hyhvO6OZOWKKozG1NeoyCLA0qR4MAqMWwnD9x0-eQM8PMy2xT5KjuVzmcfcw2Z0OaR3HnyUUTtYXwf4ROZSb4gJiHn3CbpJPRbtOh9kCTI2ewYXFyw7V5g_NMSxigiiCEJESjS2-MZl0JIBos8-efEeDu0kEkfvpizmnMQ_WfEUpC5s7PnUB3CyolwICSXjcKYqqeLci1-wrjW1KRnyfogysPrtct2yob3FLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMSatLVANNzK2GSOQpXe4EVirt7yL6ZUAKSZtY7LLGVQOEXeM0sWvMK-ZX_VNRCcH3QqqOzfch31Esgwgm8WyoJOKK3N2l5Qr0yLWeVq6b7TqKJ-gzt3ZPqPFUtxVKTQutA2g__6Ah2tx3sgXCDGPcegd9pcgu_iqyp1djbsa8XIKJibJIgGyZ82iUlhw94t6lVaEeVgD6Ly5vHrkX83XWMcM82yAw6i6gew7hdLjk6cSMTlmRZm9NhfBnWwJQ1oNRXlI0RDi5FnXmsxwBrJgkoCbybRu9VJinYZvnqiwQuyHbu3itVnv3sbT3Sxjn2BO04CaLXn4QXs1207Gms5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3WIfoWrSKHjs36gg7EDQTPNpnx5p4v3fhhcUT5fwa6Mn9k7TSUDTYvK4a-vVvkZlV8ky8nbAW5IkRdYamFSKNDIokmGwM66ZJ00bHvghrlNWbkV0HgyTLFl0K883Iy3cUG_n9w9gctrVI3PrpeNf1dps0TzxxIwO6iqDyZ3ZQMNB-KaP24jaSs8hRVfBOvy2MfKhdkyrSaxLPBAh2J2wdRVni6lnCJvjhxoNHbe2oyQNnga7tUHLnCJC6HIn1Isuj2fbWdVEKAKEPDwDtvrfg9TfMTUTp1J4XG4MpQRKmudwY57xAniFVBy-Inb0lCDkDPNMILZlKz3oVwcL5oSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpKvy4mS6412Qk_sxcfOpX4DhdKY7Jw9ToOCtw-2OE6rOTMR12OL0AbuYs6Zpu7qqEQN4qSYalHVyATjUkoJYfT_ha8jeJdjL0n7DFsPxw412qQtNwABTYg-wv3Ecp-CxUFA5Qf9IpvTPtN1VmcRRXm3QXaL9a-JLVp7Fo-BwSbUwupm_ZTqdYuZIMnfYiLJvZ1L7lZ-LLqUMbGo0j81uCk16kEmaLOVPsNIKLQ7wi4e8-GEmf4_mlWDqYCOQwDuLPkOpA3WRrAzKMFtAnmZWg8KI_9QWVQkMrbMXAErFtaQfYmmXH5CTq8F2KixbPWLhBFb0-CrHPLfXicZPo6Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWI5hk24p6vse_uJd87UPhkr8fDUqBxlQes4ZNMDRx9zWIQBx7gTVfnSgtLJWMEhPoGG7zAlMZqSYfnYZYuLRVAkz9G-8oSW1LmfUwBZmk_L5er7CdIVeTvWSwxsDMG0ZH6Qh2_0WkqLW8gObnR2njHIN8sotsqyPa7lyoZgQ8zyD8vSlGdgqJm0zCTw3WtawyI5JKX3ZTBGqchfdw4R6g4Xqvb6HIykElI4vvi0u_-ShgkNeQE2GUlV8kzGMALUxxubdLf1hudSSsmxjeTM5fUqrviD3vMBDHwRSLqbvOp_eAtuwTa-n7eSBFly0uGmjvCq8_RfY94IS7E-Z-sJYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
هوادار روسیه‌ای در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91015" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=YCMqEUWDVXDi5GbAmiBj2JJPkxCEo3B8B_PfdWk0HoM2RrY4W6jV3zpXVxWRc5KT4DXrUKk33ibsMb_GTSSS03PvQFFEieNEiZoqpw2DAUgN3278JLk-VBN4iXquSgQv4J-BlbTqYskXQ1RR-xzlXlizJrno5FXzKf-41WMjJ1RK4P4TBCnp_qImZ9b9KyU3PkyV_GtkEY6uIMQX8KJlpI69Nv7ThCBwZamNr4vjWhDJwTiDHA62DnXDAoftGJzTLKQh675XNPHoZr5yiRzcyILI2WQe5VjlaiE5VlIZfRqb41rgAP26xp9CnFCwRgiv5NOnZh8PPGX2vLIUl7ygeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=YCMqEUWDVXDi5GbAmiBj2JJPkxCEo3B8B_PfdWk0HoM2RrY4W6jV3zpXVxWRc5KT4DXrUKk33ibsMb_GTSSS03PvQFFEieNEiZoqpw2DAUgN3278JLk-VBN4iXquSgQv4J-BlbTqYskXQ1RR-xzlXlizJrno5FXzKf-41WMjJ1RK4P4TBCnp_qImZ9b9KyU3PkyV_GtkEY6uIMQX8KJlpI69Nv7ThCBwZamNr4vjWhDJwTiDHA62DnXDAoftGJzTLKQh675XNPHoZr5yiRzcyILI2WQe5VjlaiE5VlIZfRqb41rgAP26xp9CnFCwRgiv5NOnZh8PPGX2vLIUl7ygeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
بانوان جذاب اونور آبی موقع استادیوم رفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91014" target="_blank">📅 13:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=FeMLfEnYhq_AjAkPlHSojNanTUzm32pFwbfvebp33Cx8ZfOqM6N_lCY0CqrEMOUwZ2QqE7-GFRV-Bq7NYDObZE0HXtZazatQldvN_MmFPJpMZ6gpaMC1GPkxEpkfd9Fwsdypy7_iMsCInPYk8Y7D217YxSMTTbvhvAs1nFalRMq-_1atZC3IjJpmPLvZBNdVmfxzayTOLbuJIzZX11N4R3-2vn-dbEYFjmn4mIciUYV2Avb3znNcDnWB1vqC8lwflmPITGTxMRDmznzYe3Z-NHkhQbyqgHUu5UjOoln36T6jJJ9jZspWhmOtdpF6h-Xv1K9KhuxyAs3h3fewwl3-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=FeMLfEnYhq_AjAkPlHSojNanTUzm32pFwbfvebp33Cx8ZfOqM6N_lCY0CqrEMOUwZ2QqE7-GFRV-Bq7NYDObZE0HXtZazatQldvN_MmFPJpMZ6gpaMC1GPkxEpkfd9Fwsdypy7_iMsCInPYk8Y7D217YxSMTTbvhvAs1nFalRMq-_1atZC3IjJpmPLvZBNdVmfxzayTOLbuJIzZX11N4R3-2vn-dbEYFjmn4mIciUYV2Avb3znNcDnWB1vqC8lwflmPITGTxMRDmznzYe3Z-NHkhQbyqgHUu5UjOoln36T6jJJ9jZspWhmOtdpF6h-Xv1K9KhuxyAs3h3fewwl3-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای‌کاش اینترنت وصل نمیشد اینارو نمیدیدیم
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91013" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOgEFmqALz6rI--BhD6kOrLS0CElFGwoJvlP-oOyTeKSWlBpPm0XNwSAD8GjWrqkKqjD7M6F6LMOFLVk99RHGeNuvrQ8Gy54xbYJIBNDv_lSF1vIgU5sNhy3qx4XbPnOpsXBrDHvnO_kmB3eNnUfLWtc-VmhA3HID_DPzSqla5MoR10Rfz1PLH1NAfNmH_3MxdQZjIODhB71i87faf9V5PF2qW-NkaBqybSdhO-qY69KP7QQzFmmDpmDFK23W95Xq1Vecv4yxH3uCJO8I5F7WD4SCxym4kytCq7xebiUz-aKOhgyMjjWSRBMUEm6aipIR9G4dNE5rlSm7fhC03Y38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇪🇸
#نقل‌وانتقالات
|یوونتوس درحال مذاکره پیشرفته با اتلتیکومادرید برای جذب سورلوث است. در صورت خروج این بازیکن، احتمالا ولاهوویچ که قراردادش با بانوی پیر به پایان رسیده، راهی مادرید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91012" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
‼️
🎙
افشاگری نیکبخت‌واحدی از پشت پرده بازداشت مجاهد خذیراوی در پارتی شبانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91011" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=b45YrJE9pnGVHvZhpm7jDraiEac6WrIro2Yh39_VZ3AhmFVg_-qRJ2TNvHmNbQkSSzyWcxP6x0ltImeOIZG2SnSmgbUjqoFdx9_-JvLJcghRhOTS_E-At2HWK-178OhTll6ziIi-JulZts1v6DQQJ0HhYHUHUUV-REdToTnkzx_1OQaMjebtvVimiPVimfnQonUxzyCKEETe-gCD21tEiy2ckIMgke9nUP0IV8V24pniL9SEdeBHYEy7PXNH-ErLsmzlgf2vMDIOn1EkPEbS8asD2DMkA_67Qo8nspe3UPKBve-dIl8it-o0K_LgoMqCzph6WMx1fxiArC5jXMKthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=b45YrJE9pnGVHvZhpm7jDraiEac6WrIro2Yh39_VZ3AhmFVg_-qRJ2TNvHmNbQkSSzyWcxP6x0ltImeOIZG2SnSmgbUjqoFdx9_-JvLJcghRhOTS_E-At2HWK-178OhTll6ziIi-JulZts1v6DQQJ0HhYHUHUUV-REdToTnkzx_1OQaMjebtvVimiPVimfnQonUxzyCKEETe-gCD21tEiy2ckIMgke9nUP0IV8V24pniL9SEdeBHYEy7PXNH-ErLsmzlgf2vMDIOn1EkPEbS8asD2DMkA_67Qo8nspe3UPKBve-dIl8it-o0K_LgoMqCzph6WMx1fxiArC5jXMKthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیدا مقصودلو شیطون شده و میخواد با پولای ددی مورایس موزیک ویدیو جام‌جهانی منتشر کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91010" target="_blank">📅 12:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqMqaC-Q_JzCL5AzZl4MQcfUu5FCg4dtsBRv9G_fyos2Q6_Yoqw_igsil_Ke78cxD6-8t7p7-YPwNQseuuKmELXHXAxyGfs_MCNf6QaOwlzKcCdOcMLm5jGDLP-RvR318j3kLE0DHLJ6wJ468Gc52ofOMYoBf3O0zBI_WPHUg1wDu9MGhu412Fz3Kslgw-8D11ac49ZEC6ZHA1PAQrU1K-tfUrWyYILl4Anx56RHKiBxH4RdYoxgrOpBwlZ4y8J05bgxbbLg_umhp8pcqvccFWCS89b6QyZQ7U-ahJ2LxtrHQhPG36TxgdQulIGWOI_qtmJsGL3wsYHoNJoxfxLE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇫🇷
#فوووووووری
؛ روزنامه الکاس‌قطر به نقل از ناصر خلاف: ویتینیا و نوس به هیچ‌وجه فروشی نیستند و رئال‌مادرید باید قید این بازیکنان رو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91009" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=lwjv5mbB8S4hYOM59uMQ6Ysvtj0yiP1GQG6sJKt7eTn7WjrSr0J1NyMfMqSINky25Z8d0jcMNWo57F0awlDOEzX1s_VUnPkuWIKozmlTbpoPddX437rCY3p4gLHwstO7o9pAHOVxTqarCrtsMX8lGuX3W1df1EiaKSopQWmcAtJjN4R-JUS7RdIhEaieyq8YZj68lZNs87skQR_xcfriYwdG6J0paAUZyAfNETORKnH5U5lHRUd5EAWYlaFo8Qn7isrhtGpzgfOHhJ7LqUj9kRonF45t-8FePISLIWJmQwAZl35OXNEqAIY7keeI3W77VWlz4uAnn40DsPLAnNYprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=lwjv5mbB8S4hYOM59uMQ6Ysvtj0yiP1GQG6sJKt7eTn7WjrSr0J1NyMfMqSINky25Z8d0jcMNWo57F0awlDOEzX1s_VUnPkuWIKozmlTbpoPddX437rCY3p4gLHwstO7o9pAHOVxTqarCrtsMX8lGuX3W1df1EiaKSopQWmcAtJjN4R-JUS7RdIhEaieyq8YZj68lZNs87skQR_xcfriYwdG6J0paAUZyAfNETORKnH5U5lHRUd5EAWYlaFo8Qn7isrhtGpzgfOHhJ7LqUj9kRonF45t-8FePISLIWJmQwAZl35OXNEqAIY7keeI3W77VWlz4uAnn40DsPLAnNYprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صف کشیدن بازیکنای عراق بعد بازی دیشب برای گرفتن عکس با لامینه یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91008" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohKDxAVaqufbF7OUKPzHXjKUL3LfYjvbtNlaceBEgQQ34ICZG0_duVd-m9u9UXIb2zx9-Hb-TaRyw9vSCcGxISRbs4kcZOP3h_2E_UAnq5vtC1iM9nUD7lcaJkvIDRWv7R6hg5BTuMeMk98F66JV12lKnSHjisJYdkOgNBNSCsGDbm7hV7GECs_Mc39j3FQOReVBBUPbpfI_V8cTmVnZzsBldABBH07r4QIAdpVMMLhXWgiYneRyAbB4J2H3dfhTahi7AiJQpPRo5yblIfLmiOEcetJBS0vEcY5eh0FVZl8DKR0WPTEgI4AQbqKUd69x2WmgNkHrSx4bb7lZ70swzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر آموزش های آشپزی هستیم دوست عزیز
☺️
🙏
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91007" target="_blank">📅 12:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=gX4Xm1yYt6REObxnwIFH_wN9fVPVBabcKnIYP2VO_WDFNedIPE5zXI7RjLO3XZuuokNRysJsppY6HCcFMzbgA6pWxzmxpmjxuUKrjg5EgFj2ygP1qsa5sei8iv3fLieTBYDl-2-UvWzqi3ynfUR7zBenqfXd6hMsVWLsXqTxLu_kvVqrtc6peXpsm7r3Wn6x-EnvrMVJrohDgAywz_OENfqKBScjo55n9xbq2T24t_3lgwT_mxwDH8JuVLLnLkiT0FLIpbPonhpAGxYSYek1y0KdlvUcSi6PXBANrv0xv8Z6b0bShIIkFTVA2nYDNJ7AZnpzjXRboT6fa6IpbOq8RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=gX4Xm1yYt6REObxnwIFH_wN9fVPVBabcKnIYP2VO_WDFNedIPE5zXI7RjLO3XZuuokNRysJsppY6HCcFMzbgA6pWxzmxpmjxuUKrjg5EgFj2ygP1qsa5sei8iv3fLieTBYDl-2-UvWzqi3ynfUR7zBenqfXd6hMsVWLsXqTxLu_kvVqrtc6peXpsm7r3Wn6x-EnvrMVJrohDgAywz_OENfqKBScjo55n9xbq2T24t_3lgwT_mxwDH8JuVLLnLkiT0FLIpbPonhpAGxYSYek1y0KdlvUcSi6PXBANrv0xv8Z6b0bShIIkFTVA2nYDNJ7AZnpzjXRboT6fa6IpbOq8RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور مکزیک در کنفرانس مطبوعاتی یه توپیو انداخت وسط خبرنگارا و یه خانومی انقدر ذوق توپ داشت که با کله رفت تو کف سالن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91006" target="_blank">📅 11:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Gj8DoFDhymQLQqlPxJHIO9i4nsoNwHreNU3tVAB-UOSB1HVy5u522e9kxUuo4JCh8vt0EZm6ajlktMSivr58z8a-Q7mFqDFCOoV-bIBiMvGxg8Kr2yj6e3iwHsjpwiB2KPR_4QVqjSa1GQXXdfdYgWmfCXVzjoqtVTHhZl7TiyA6785oVoEW2nimiteYEUm7t9lV-pB6mVbM1lO1d19fz_u5FHFfam8E_U3PnDmcAfF7cVZ5oFqpOgmzyGg8DcF-lAfU8t3ZAiEEE-jixwivcQCTF4f0hB5Lasuj9vG3agmz4tyIl1VN_thPncZk6zavI67mXao0KFJ8uKtqc4yPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Gj8DoFDhymQLQqlPxJHIO9i4nsoNwHreNU3tVAB-UOSB1HVy5u522e9kxUuo4JCh8vt0EZm6ajlktMSivr58z8a-Q7mFqDFCOoV-bIBiMvGxg8Kr2yj6e3iwHsjpwiB2KPR_4QVqjSa1GQXXdfdYgWmfCXVzjoqtVTHhZl7TiyA6785oVoEW2nimiteYEUm7t9lV-pB6mVbM1lO1d19fz_u5FHFfam8E_U3PnDmcAfF7cVZ5oFqpOgmzyGg8DcF-lAfU8t3ZAiEEE-jixwivcQCTF4f0hB5Lasuj9vG3agmz4tyIl1VN_thPncZk6zavI67mXao0KFJ8uKtqc4yPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور با انتشار این ویدیو نوشت: و شما ادامه خواهید داشت...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91005" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pybpRNeyE1_VcN6fUeuhm-VGYjnZry27EKCM3nuI05voaravchufZrK9_yBKfSL0sFX_mIVPSyZF4yeHobza87HQFxljrQQYnoMKathPXOVkrEVzZ-Dgc726BQRfa69Fv-fDoeYT88MnPIw_VriCA2SfseJef8ao3usEeIe-KfTAwaeNzaOBdX-fGJQN8_gY0C0eZhTkzP985D25G70GXoALlV6OFDBIJwrHFH7948nIf-udSSShP63KjGS-q0BpYvNL0ZL295h3tlxNoy5jZID3ZByOeD8k4-XSG5ER48W58qbZRn-HOzS8Ri0cu7RDbDuJlaem9URXpIBcdztbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91004" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae875521b.mp4?token=AaR4qWrXCFOZp6MczcgRrknjzqpgwUZVdprO-D7UEiFUdiz6E3hbHMY90PI-727xBN8SOE0uHsKzt1nNZVP0bJVCja0zeODVP7T_MhCGw885ADFss25Et6QN614prM9hEls-T381OzMEHAAPCW9LrQQ7wfEDRKaOBq97Y8hrHVcsZPcapbdooTnfZAu2-vge02rWY4OC3iM3iNXZ3CwQNQGNd75dLnffpyz1xe_MxGHVLBJvz31X2X9j4EPP7AjeSTy7K5xnoOHZsRaui0TdkGizAc5W2ZjqvPlrQoH7E9PUXC9sIDbLBT0dErvTPgmvunfsGwwgrHkYhMbSG6sBSVWWsfFT1NxFvVfoKBh4noo2VZlKAfP74GsG2IfLR3BhGDeculyDFPi5z-jCP5DEOD3Kod0HdgldDnRBfmcoA5osUc3OIxY0BLWmyBW_COhe6JzR0Hq8SnjaSwVQu3NMTVvqRM2YbbvrfolOWJNDbWaS3wW0uYldWc4EMjwRE7y_aoSd8a6NeEWxycUdWMMKjT6BjDNQ0l36oFME3pBLlww9o5LxksWlJIfu_mVYbcVn0_CqpFEbTDwm_J1wW5rq8ZUAmR4WOzjKg6gvrIWCMWiSXTFgUjO9iEEBtiXM1mCnVBuC1YAgRv_8LV6bhuzd2a0hPWuOW01jUk5ENyM31L4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae875521b.mp4?token=AaR4qWrXCFOZp6MczcgRrknjzqpgwUZVdprO-D7UEiFUdiz6E3hbHMY90PI-727xBN8SOE0uHsKzt1nNZVP0bJVCja0zeODVP7T_MhCGw885ADFss25Et6QN614prM9hEls-T381OzMEHAAPCW9LrQQ7wfEDRKaOBq97Y8hrHVcsZPcapbdooTnfZAu2-vge02rWY4OC3iM3iNXZ3CwQNQGNd75dLnffpyz1xe_MxGHVLBJvz31X2X9j4EPP7AjeSTy7K5xnoOHZsRaui0TdkGizAc5W2ZjqvPlrQoH7E9PUXC9sIDbLBT0dErvTPgmvunfsGwwgrHkYhMbSG6sBSVWWsfFT1NxFvVfoKBh4noo2VZlKAfP74GsG2IfLR3BhGDeculyDFPi5z-jCP5DEOD3Kod0HdgldDnRBfmcoA5osUc3OIxY0BLWmyBW_COhe6JzR0Hq8SnjaSwVQu3NMTVvqRM2YbbvrfolOWJNDbWaS3wW0uYldWc4EMjwRE7y_aoSd8a6NeEWxycUdWMMKjT6BjDNQ0l36oFME3pBLlww9o5LxksWlJIfu_mVYbcVn0_CqpFEbTDwm_J1wW5rq8ZUAmR4WOzjKg6gvrIWCMWiSXTFgUjO9iEEBtiXM1mCnVBuC1YAgRv_8LV6bhuzd2a0hPWuOW01jUk5ENyM31L4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شکیرا از ارتباط عمیقش با جام‌جهانی میگه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/91003" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVuzzdLlD5j5xBpgjh1Jz_7nx7kyN2RHwJHnrDJbS2ei-8n9NCZLif6gPh6Aklp_LVyW93Df5oZN-ZX_a1VJjDdMpmKa8Nfgkh_UlyArUvcyYUj_C_q0R8NT8Nx1nebij_KWN_vJgJ7vC9isnS88KNtbqrSONTO_o8lFUR1AMCvFpSsfU4dZVZWsqtOFuJf8_EnXEXzRch9KTNgF-T9TmaVldKNRl62MjaPRaVHFacqyMjLfIo-brQk7nY-ER2VgWedXN_iTU3Bmesgwp4ztFEO8O4Q9tRVCBTUNndCSjbvJRZAP8SieZ8T7zWKFNiGCjQTjJhnBi-stMkqv9NzwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇲🇦
پشماممممممم؛ رسانه‌های مراکشی میگن که یاسین بونو گلرشون در آستانه جام‌جهانی با نورا فاتحی بازیگر هندی ریخته رو هم و به زنش خیانت کرده که شدیدا در کشورش جنجال آفرین شدههههع
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/91002" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=VIZT3akWKr2ZR0FN48b3Q7dQpnpS6k6iFPnvOdLo5v_CcfdP8Rx6JEbhEO87mMLAyVqtqyQwYcnXkwyOY5_kpiyr6LyHwjeTMEhNYJKJIWtCvi5h-zxgUIIPb8bUtV6HOXME3E_g8MoapUAvVpl0HIkfjXGKoWv9Pmfy6OUrCbB9mLoqUm5c_4zdKFl_OAIYaUXuocNKPfDYyR2qgviWbKKQwscC_vGB2nfDm_aZHVl_fIbEQAvzGvla6kw-NKmU21gu0Egs9VPBZdOtjMMgEg4ck-eZRwBXkDczQDdIIzkEq9tW5YGMuREtiEgKPZV9Z2R2F6e41Dw3ZkZncMiX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=VIZT3akWKr2ZR0FN48b3Q7dQpnpS6k6iFPnvOdLo5v_CcfdP8Rx6JEbhEO87mMLAyVqtqyQwYcnXkwyOY5_kpiyr6LyHwjeTMEhNYJKJIWtCvi5h-zxgUIIPb8bUtV6HOXME3E_g8MoapUAvVpl0HIkfjXGKoWv9Pmfy6OUrCbB9mLoqUm5c_4zdKFl_OAIYaUXuocNKPfDYyR2qgviWbKKQwscC_vGB2nfDm_aZHVl_fIbEQAvzGvla6kw-NKmU21gu0Egs9VPBZdOtjMMgEg4ck-eZRwBXkDczQDdIIzkEq9tW5YGMuREtiEgKPZV9Z2R2F6e41Dw3ZkZncMiX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو مراسم اجرای حرکات نمایشی ربات کنگ‌فو کار در شانگهای، ربات کسخل مسخلش در میره و با لگد محکم به شکم یه بچه میزنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/91001" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZDmWVgC5wWkVEipl_eryt_5CKPLLSzB0umPekl5JZltqtC1ch3nOfF8hqzFPB4eGkXKEHFB-SyZS-Q90xy_HPPBmJpoMCoOlDrWaM3_QUfR22olbC-8vyRoSOxd3GEytHePzwMCjlXn_Y7pPnx7CAlgsgtIAqy0jmhsJ_zbXCmsnt5ACKDuMHOtXP1qxcKxJOYVqBCETJYmSPoaBPurAmM3UTfeNXuc7cLRBQhaEyiGss3DIVi3ZhV_w3_QabfoghsQfFNsVrSBkJcJ3lnO7L_NpyJJ_ghJGD80Qhj9PiNPS9OsUBbMinmfEcj_paIpXOyBHlyC6tX59LorzOUlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دنیای امروز به بالایی میگن آفریقایی به پایینی میگن اروپایی
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91000" target="_blank">📅 10:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=kpLicTDZYdgoMb8kilCmYeRaUOcep1m8j_OJmUjX2Sm6a875KDN4M7v8VQw6yuS24Cq-jd-cSXCbyldEML4Yl88DG8JQHWTdC5HKsNFohqqEKgex9Wh_Blhw9EREEkAaYc7LohduvGYGcjsjAc4I7RfCElkKYJ6I18Oo56ATaWXpisK9k3pwDQxO9njRmYJZHwdzeMWoD3sXkMJxDxzoeQQA_EjovcOKGMbHd09mWo1UVGiywTqfJoWbIQoNtPLeSNW1OYDTrrv1SpQrBjA5y5i0XwCgWtzqZ1W-P2IilnkniB1Yg8eCqbLQwvoxx4AEoIhpEVBe07fqnkXG6vEBgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=kpLicTDZYdgoMb8kilCmYeRaUOcep1m8j_OJmUjX2Sm6a875KDN4M7v8VQw6yuS24Cq-jd-cSXCbyldEML4Yl88DG8JQHWTdC5HKsNFohqqEKgex9Wh_Blhw9EREEkAaYc7LohduvGYGcjsjAc4I7RfCElkKYJ6I18Oo56ATaWXpisK9k3pwDQxO9njRmYJZHwdzeMWoD3sXkMJxDxzoeQQA_EjovcOKGMbHd09mWo1UVGiywTqfJoWbIQoNtPLeSNW1OYDTrrv1SpQrBjA5y5i0XwCgWtzqZ1W-P2IilnkniB1Yg8eCqbLQwvoxx4AEoIhpEVBe07fqnkXG6vEBgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇿
عملکرد دیدنی پسر زیدان در چارچوب خط دروازه الجزایر در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/90999" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgjuBGM6aHpBI_1OdawbxxM_SxRXTtJggX0gf98PAMmz5W06HeadW264L8bw2FIdokbm6HwsfjqQh2FJDqsMqXw3e2zmskm9uJxq2R_1-7J-H-OPvVFtVp_-HN2EwbeQ0YSi9PtO9JiCP9yPGV7kFIQnqpdVqUZvzUeH_wJdI-R5RTcBz9grtwjEephIbw9DN-yI-ZuYhD2pPDHVezypJvZq53Rn4S5LXF8uqmnmPCgVVo4yQV156TPqRfrd4q1TPBY4yDA57H5zZrN95N-INuCyeUEnn_kAHqmk5O_BAWNuGJUzZ0NLjIy0WNk7HACCk76-YJMUE3aVwFz8pugYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/90998" target="_blank">📅 09:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLu5qnJWWAYplfDb-ICEyccrhjPbezzza5lYcwUvhQx-StxycBrxfQxbvLqww5g9kisCZyOuZ2nrSKqZiMA_sUHZqy5iJGQ0Q-C8Osli0__sBRlWo_kUUgk3m9mL91gL_SnScVm3AZ_5USWoJg-gP6F1CYczNdalGVcSLlPN3qhDhYQXl1vUM6wUTWWDhnUP4Ud0T1xc9J-kumA_yXTwF3BPEvNRooUAwo3VkecfXdGfF1MJOdxcgqQcrEnFArJceC54s-Gn_3_qAaDF0ZCEGUpaIs6hCQOm4MyRchQuUySNlxDIp0C1-xiC8L4SxN4LvUR3BjGqCu8mSQGgZhOdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/90997" target="_blank">📅 09:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=r8ItDj3QNW25XSj9DG3Cmcq7rqjvrFGBuvI4KPfShIn5jJMpjEEzcJdcJ6qBk41Pa9jhznHH0e84_SX5HifBXPO1hUibtnX1Ut8D-pvBVYkxEzINT7H9gFilCBrsbwq9fAon1ggLyE6CGGwjDvLjT27-RmciKOU03Izhu1AJ0H-nkPWzYheoMIRRW-fXmtvNznCh4YgbqSMiCUL5EY30Zz8z0ZfrlMHTAnqRWDqjrts0829da8DRRx9_PQONWd3_eGxjJtxGm1CgKK-_d6Ida8ahXKn0pJH-rr1xaf8wQW0HOyWLQIqC2FyFlePMGXtveHnjSty4RE2fYU43C3ImGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=r8ItDj3QNW25XSj9DG3Cmcq7rqjvrFGBuvI4KPfShIn5jJMpjEEzcJdcJ6qBk41Pa9jhznHH0e84_SX5HifBXPO1hUibtnX1Ut8D-pvBVYkxEzINT7H9gFilCBrsbwq9fAon1ggLyE6CGGwjDvLjT27-RmciKOU03Izhu1AJ0H-nkPWzYheoMIRRW-fXmtvNznCh4YgbqSMiCUL5EY30Zz8z0ZfrlMHTAnqRWDqjrts0829da8DRRx9_PQONWd3_eGxjJtxGm1CgKK-_d6Ida8ahXKn0pJH-rr1xaf8wQW0HOyWLQIqC2FyFlePMGXtveHnjSty4RE2fYU43C3ImGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت مردم ایران در شب‌های جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/90996" target="_blank">📅 09:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">▶️
🏆
گل‌های برتر جام‌جهانی 1998 فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90995" target="_blank">📅 09:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65885deac.mp4?token=hDY_DErLxImW3Ucs8zm4Qu9Cq4YovFNtGQM_MevZKQpAvsR2ZxsK53Jc9oup19hXPv8wj5NMQmSjtqaP7o6OhScOUN86grP1oSJ9s4xjmYPG94OWOza3Vrlij8t2CQA8TzxXDeX20RXdm23XOCYxAhhRdiNXjsu33MCaaWgBz_6kqx7n2hK1I5nUXxtggka1IWj3lQ5eqHcZO9Dw0qax20Wc2l2Wrd7-DoqarSxgRZbKdW-d_y81Fm9zHageYqDV7BrQh5tVhb3M_8UT4Uqr9_LH4Cjzk5qIRzWjz8F4asGKAQt6hsXXddyw2rNEBvCXgOS6dsb6-2cKb-zJGptRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65885deac.mp4?token=hDY_DErLxImW3Ucs8zm4Qu9Cq4YovFNtGQM_MevZKQpAvsR2ZxsK53Jc9oup19hXPv8wj5NMQmSjtqaP7o6OhScOUN86grP1oSJ9s4xjmYPG94OWOza3Vrlij8t2CQA8TzxXDeX20RXdm23XOCYxAhhRdiNXjsu33MCaaWgBz_6kqx7n2hK1I5nUXxtggka1IWj3lQ5eqHcZO9Dw0qax20Wc2l2Wrd7-DoqarSxgRZbKdW-d_y81Fm9zHageYqDV7BrQh5tVhb3M_8UT4Uqr9_LH4Cjzk5qIRzWjz8F4asGKAQt6hsXXddyw2rNEBvCXgOS6dsb6-2cKb-zJGptRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چون از پست قبلی ورزش تو خونه استفاده کردید، این ورژن‌هم ببینید خیلی خوبه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/90994" target="_blank">📅 09:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD01XePsrArOBC2_4eXvsWnkNIbwwboG3oYsicmYH8mU2F6o7-uvALTDZG9Sz_qaPRJiTJgrZRXcFJ3CsV1JgHtbT9CeuFmSFRw5z2sPIGyaXk4-IoQaelkf7jQk-p1LzA_powelgcoo0Kczkl1h4xSeOcxc129bVkFjnUhPpTsNRefrwYgHqhF9TacwmaF8522YEAiZUQmcB0p6BESs5PFSgKeKfhqw5YH41zkFRNFK9xCV5u8VBDQHCSSThPO9Q7_gOXCtp-aCvs_tIweFiIN3mRyQOnrk7_iNQ60T0WTva6I51BY9vhzvM6gy-rdKJPeVSPDZK2GAIi5uGTYxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهتون با قلب رنگی‌رنگی شب‌بخیر میگه
😎
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/90993" target="_blank">📅 02:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خوب بسه بریم بخوابیم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/90992" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
خلاصه اخبار امشب اینکه الکی گولتون نزنن. خرید احتمالی پرز یکی از بین نوس و ویتینیا هست. گزینه‌های دیگه بنظر بازی رسانه‌ای جهت وایرال شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/90991" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbjVgrSJx9kqCxiYRyXQpsbJ2g8YUUAJFiywdmpMNVXZEMadHh3epNthPkGa7nxO9itwquOdS783_0_kANtTnwlloc-pPp5h22Oj3ZDqmUM_HjvpaWkUA47_LyLnuQD-XWzP_ME0k95suI7jQI5Esi1wib3sTjWT_P9NkVNP48g9vSN_O7stiDDsiU0ax-6IsMhJlViXVKnzWfL3EJzz7B7FxmkCwr54DzQ4GxUDz_F2BpgEqdjXqOFhle1-sehL-XKqzU5B3Lq_l7BxBcBU5JfDjiuXcxOldwwCf7MphC7cLmnYnoWDbDJdLFxq1tpY3hKdSamRMbr2_NB2WsP6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد ازدواج آنتونیو آدان و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/90990" target="_blank">📅 02:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/90989" target="_blank">📅 02:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
مارکا در سال 2021 :
🔵
⚪️
دو باشگاه بارسلونا و رئال مادرید پیمان بستند که از یکدیگر بازیکن جذب نکنند، پیمانی نانوشته ولی محکم بین پرز و لاپورتا که بر این اساس هیچ‌یک از این دو باشگاه برای جذب بازیکنان تحت قرارداد، اقدامی نخواهند کرد، البته این توافق شامل حال بازیکنانی که قراردادشان در پایان فصل به اتمام می‌رسد، نمی‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/90988" target="_blank">📅 02:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaItvl_FcgFSiT4usWYV-bu-2_cNY__4246z09xsTGiNnQfEGnjoW-twZ4_UxQWfdAA4T4rGieYvD76td-UisI4GaP-yHUKKd2324IypnGn3h1uDckMpXBpUVHfSyekhjImLpIbgnjSTJ7L2xTHFgMaN5oEFirCwy0cm7adbjw0TKrfCTpitanvQyNBSvYvZZV0spaxSVmAnL1aUSx1McDY1BwDUUOvLxRU0tkzI0ElH3yQfShxE4kRZhfxZ9QNaudUkKt5Zu_GKNFZJEohpv3Sw0Oedcv56iJ5ddGjMmYVZDXaVEvRmU1pN_grOJr6g1O6LAi0_HfEy373m7YxEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#رسمیییی
؛ فیفا رسماً اقدام جدیدی را قبل از بازی در جام جهانی اعلام کرد. بازیکنان اصلی و ذخیره در هنگام سرود ملی در دایره مرکزی خواهند ماند، هر تیم در نیمه زمین خود [مانند تصویر]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90987" target="_blank">📅 02:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0Ze0RE-gimG5_MEChLHsGBqIIOf6zdwK7GzqnBODe67gAlswpVBEnuZBV7hmMJyO9AXU89W8oMkEVuM1dr7CvtDTX2CcgNT1DuZAO9OHtbpbi7HwMIrLsKszcQGXsPsGZPjulQApn-7AeU3zN573gETjMeMsoJdWMumPmyMEO3kPzUt6_uAxk4LVceUv2lNETN2I_RRTkRPmjnuzc2PK0TA4T-zi6r4GrP2F1DcHAicGl2-cjUMG6HdVVP4kDxpIh37PMdoGFpRGG2h6Wh6wH8O16isypkYrwH_jY9WcrL4XGgfEe1cUwQ-JDXsbLoPgcIhrpI4VYfxzzCCZ73RFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😴
😴
محتوای خواب امشب رئالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90986" target="_blank">📅 02:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWy8m94Ck2KHEG5lYR0YgO6xII8sOLOJZmjulyqvr5_nx5VelwcGWOG-c1K2sIT_HMZTL6EZed1dgk_Zt77pfyZQx1eES0kWqa6bBdakDV216Fxm7uUpv24dx60UtOTdeB6j-oRQxbIXKKNpIXe7Miz1GYlWeMartZrnd-iFo8Iz-QF0kMOmxppCdnBOXdI6cfXK4pjI7bT2lCpSmSPemnyGvnrih9I6UfQVa4gWk9beLl-i6LP2OEXIHK610OIi8-isdsNtNrK8mokzgaHCkM__l5TpC7JsE9dKXisASop2JOKf-VxXQhhFPpRu5jowctBkl0cawXX4ExrIUV7GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90985" target="_blank">📅 02:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90984" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فووووووری
؛ رومانو: پس از جذب کوناته، رئال‌مادرید شدیدا بدنبال جذب یک مدافع دیگه رفته و حاضره رقمی نجومی پرداخت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90983" target="_blank">📅 02:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90982" target="_blank">📅 02:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez9ebkmfd9gMfnZKDvB7tBgRSF3ROs_-eostAGPxZkNNWAo8kPUHvj1IhT5i-DOdNkc0e_BHEY8FeutCpW-KjTHREy8hRpV5ExrcmJqGTD8ciOMpLbeBPY_ppWBnHOAMaFXEH25z_jJvWJ6Qu_BCtYQllt_AYF6u3zEbIOO4dJq2vhQsdy_mzcivxA4Id4S_loER3qx2mxIzBOGp5xvldM0wfge_NwQE_Gdc8midRrq21cz1o40lLT92w5TzRm5YJedpRCE0S30Peo4JMrF3zSQjH5yCOp660MzTLP136vxBjoIujvCwHBrNU9EV3E0VM0FZP3yYsdeRgxxTmICP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90981" target="_blank">📅 02:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
فوری: خوزه فلیکس دیاز گفته گزینه‌های مدنظر پرز، اولیسه و نوس و ویتینیا ان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90980" target="_blank">📅 02:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
وعده های انریکه ریکلمه قسمت n ام  : اگه رئیس بشم دلبوسکه یه پست مهم تو رئال‌مادرید خواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/90979" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/90978" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تمام رئالی ها منتظرن رومانو زودتر از سه‌شنبه بازیکن مدنظر پرز رو معرفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90977" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X5MF19MnVpBo619gXpILLgcBFS4m3cojXxunC1RhkXT8rjGtldNLVINNlyTxSXVFObBTafPpZWFvN1rAKDdTUn4X_0p6-m-xlg62nJJsX9qNZxMZtQrSkeCIA7ETq2Vq3Fj07edwRf9VFPQQbOw2Xz-FzU5TCFDt5pv_NxsjI6c3L9-wTW5uyqNxxhhQys35Kk10a7ExrKHe_CObBPq-Oc6WDicY9PfvlTVM2eaScE3o8ZQF1GxrpJp5zxojZkWUBjeLG_R27RAidqQUjtQ5vkpSa48j4C5zfiM6KAmy26K-J8SPSvVsNrMHFnbSLCobF8VfgbmjD4jAG1BSYx3LHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/90976" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⚪️
کوپه : این 150 میلیون یورویی که پرز اعلام کرده پیشنهاد اولیه اس و در صورت رد شدن قیمت بالاتری اعلام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90975" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vljUmY8vvVegScn6DpkszMK01NCL8YYeObp60FisxVsWyOP3ma4srBrTJ67lEaOhEKOwDW_eWSidkUdhyxBgiAFG8cUqFtxZATivDNo0QL-uAjrltgkzAadEiZwtVqouaG9nCKny7qPbKk_57vnbAbi-3MUf339HA1spCNz0_f0JExR0WStcph-ZwOkuohevtSlzn-XXW7V1luFe1aAUJXbY8W9K5GhY7tb5UuU0D4eJGtGHpt6ACyOm5skk11ng8te0zzF6eP6MPA3DgpHZY5kFBveEHMxIY0k2T5KzE6foiRvZuJepoWAyS0CY56zyScSealHhpxEbwh61aqaz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90974" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc0BVy1wJ6heCSUTVWuOOxNxt6G8ToWPfG4PttcnlSvc5X4_XZfv5v07YBONu6r2_HeRQlbffN3qo1F_IVU3vBuBij-bVSjoo8-z5uSTsyZ5fpmsmeEGFQTnjEWuDYv-J2WaJWDrondKm-QwDlqUn5G55mMFHnyFhVM9C6Oii06oGk-1fq9eMPlboo361vXG4Bil2YihjoqyEgQGyKpTACtV7v1fpSR7GAAGF-nQ0aPJ5vUKmUz9xCCLG9yiDGVEPfNy11Z9wjxdo7xHyFWcIA_c6NhvO2t6VNqkZJNQFhC_MWTlk7YKpqEJ6-4D-JNce63oneS9hZIEXq6gf-_uLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت جدید اتاق جنگ اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90973" target="_blank">📅 01:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bSnKrWeqSe7hh5igrvZRJi-M1DxVnVMbA1S3Oj9iZGbp9aZzw43pBu8r1co_8ASniN47gwR1VJiGxr5_qrD5MTwHr4BmqtfylVFU8-Y0_6ndsZ989TrzTOo2R4JbP4a_N6-s9rxZ2yDwzW2AVSMo23-zWa6k1DwYC4UkE1cZwwAVKxm4f9PCo-v2UPyjZVBZWawdTqZ6ITJ6w2T15RC5oji-CJIparupDwhiCMr4yGIqFqZSzkYYfiTUsJSV2_m6opyK7o346-v4z4EqYK8xRdXxqnpYnSWFrcdy9OID2r7L1HPb37PjgqOMlRxLjSKfmGktLXXebvSb8H3OKbPczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90972" target="_blank">📅 01:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXsuTA7xX3n-qn0nfBR6vQRYgg1FFivQlux-YNYXeCWEXLa5wW4ZK68PyxM2GcbhnefKRBITKj8jYL4fYBE2wEacUSeFjH5UycWN51Y1QEtlufV5jfA5z2HytEM6PXZsNHTiyjcjKz9QIOQTTNQRzPluHwJjF3GeyJoaslxV-0zTdlL2hjhO0nAI2oQKINZL-h0r_eOxHWJrF-dnBqbneB6Vq1TAizNdL6hGlesMhgv17tAC6d9kKDWzE1miVi-OhZlWf77NFc3tyNIyxNCimUmtd1hyfdc__E4bjhz5PLoQfsoSWTAl6vd2O-QhmIJMcox0XMoteqvLSo5veGmYdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
پرز نسل جدید کهکشانی‌هارو استارت زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90971" target="_blank">📅 01:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ولی خودمونیم ها   پزشکیان هم موقع انتخابات ازین حرفا زیاد زده بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90970" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90969" target="_blank">📅 01:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKxnbWoASTKLo2q_Nw0AQuOFbwfMNu3u2Bqx4nbh4IE-hO7VK8sROomkRRWSGTjclSs8ipo4oFHoErS-md99VgNJ80LyT0WKhsdYrlwrUSLEN5fLvkaVWBRHRQwpSgI7fqst-QudZkboGg2X_jexnWX3VooLaScNOBi9_eIs7bB-U-UWn0ljRMD6yPpBTduOEJ649oQagIXIr4_Tk7WSFU4lC4jKXWTkdMKOu6BThKoPm-eoyYy5KuyVfJd1WWlesiZI61tuWsMhJJ3pNzw0Ya7rh7Kq0gXLK0vsD8KiWTlIPmUwzRzUDUKq5TWcTLOo0_KcK7kjOypj9beh13BeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90968" target="_blank">📅 01:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لاشی دنبال پدری نباشه یوقت
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90967" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90966" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری
پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90965" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XRW7qu23SEXmo5G0QkWSVfceAUzJs7d-VF0nTA6M2RbEEZHQwjX7k6l1ZpQ8UCbgcKQkaDPBIFWmOgPKsTa9TT19stc5X-a4BFJ_dA6hGOBkLXxY34ptkh4KuIIgbTFQWGksp2bzCODcWuYBnNNleQS6rD8k-K8hOJ2EAxRVWx276W9dz5G0hrFDft7eTFCMG__0BTGUQn40_cuei8abTxSBowgzhSdaDru98DNB-Wb_nCTa9EWM_3vvspTftHjj1jOElGRy7ahEYiOsZDVaKRw9ZqrnfVMxYseGtlu70Ycr2y0YJ-6GiRYzQOIyPitel_lKkH_LU-XzpKZ5tOX49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فووووورییییییی
بمب پرز لو رفت !!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90964" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0Gckq3nLhBTTmThAflhbrirkGhheoRJ2Abcxeg9BTZExDZBgp0p0EiSun_Vc6GFW68UrXo7GRc1r_uRLtx9kR3R0UtbxOcgyWEM6TYOASrZqtF2yruGeiNEkcjA1QnDjapcN9r0n1vMvWlX86NNCbse3vZ49-ckOO8c06BCb0yHnqNBVp16eUsXXI6DeMtnYwdLsioM-ntn8IryTQbtwsGLFU1fMJe4ARkYc6JLQfsww0kpo3Vm1iiVJx9Dprm8Tcy_8kc7wVroNOTXoxWsHtM-A-KSM3D0Q-vfu38fhHRD-FMU4RnVgSsro6Gd6v-QIVdlC6NYcoL5BTf85AT4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90963" target="_blank">📅 00:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90962" target="_blank">📅 00:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90961" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
