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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 519K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmba4M9vSkL-k4zOEo7LSrwY9V3jrGWLtEipKeLy_nKDTQZz6ZSq0s1OyEHA0cjI9c_zrL5NkDjgiDLir-R0C1RRmIjAEfU0umD3cZvPyVzAWifnlaIAkecKNucr2eJhVG-n4Dw9rE_SCMSutkmqjBrYJJt6MlvhZ4EX3cfnAjf056bYTW-gYpj7yNoN3aV3Y2gESLL6Np6fT_p0_J38zzTsPBbqNzMr6DFpVLmNO6-GTQywInex54IrDfoKkoJyOQ8Tk3ggRFJIngJaYTe_lFwxDJ2ezEQGJyZxHVXOTwLWUkDmvC3dmoNLO0YvsDB9o8V3tzWuCTOvok1myXYyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyDUNfHCSIIgkHAuh-k-XcXJQn7HJvZfrlsBH9QM4-QnoOg6G1t7IA9rWaViKq0xcEeVf0PVt2priac4Qy1mrHiMI-9A5uoRYm2WJw8LGyeflohxJhNCU6s7nml-oIUcnVkdPb15vGUSsEsI3G-2sCb5sIDCtvQGJY77M0-MBRtvO92O2C9jbFvradES2vzTDEUE1msa16fTf36D6oVX7mariygXrcva4Id0ksuoS9XLWkEF4m0idjhrpYMRWicfkta1FJKUu3gcllyeaW_oUDSnRVNEJ80HfWe2SMv5fLK4XtjsQzMu-Y7ETZXvEjABS_3qPGDcZSYbIcVzY_Bhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfBgxnBuEnK1aFhxzYI1ydQGfF6b5KpzFtpsqUXy99ecr651qbHYvvWpBJfghX42SGgzTKhJA02n88LIqttLWfYJI7eo4v8mWgTIu6X4D5La4sWT9c6UBLZGOAwDUF67TZGMNdBcJ92CXnc1Higrxdezz8pNwbi4rc-v3s2BKaJIdyAI7S6Nj-sr3yX9lfLBnwY5fqUGSKVHVy41qtSqpgXkh6w5ZHCXKyekCvYl2y6P04bq8jF14XjlBtmGDzcVSkqT3VJC7PQ4_xXC4rk7JC-C6dqNjcGmBA6YOr8EhHdti3GS-WhWqzTFEpf5n7tt_KiSOT-GnX7QM1HjpVP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOsPkChsUeRCu01aoiCtAWvm5doPpnhoScF8EigadQHHG3hRX4FpEqbtBJnhz6Hm0jKihnC6NDWIBPy3_qZb2w-rQOQVJUuukQOudCICuhTbPXrf9EDytEdPsC3tit-_jmTUB25NIvOJuv1BOV72HtUX8EKVbRYpcVk5Yy-7CWwgpAAKMvWw_jbrSpmwVjC7ytmTz_gk4IHlQXvYBPqcud99smLPGn7MkZ9ZaLTYduqd8biQeac0uvXDwu3Zvb0yjuDS7BHU0sYBRGXOQ7_r9h_R2L5OVT51rarNQZxRgPe0az2xflZkLd-ylgN2z1edeCdFvqa4Gy4rpN65kQQF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVoIofhK-aXnxWKvYDk-7j4sr4Buqi8g25osgx_BSBvcQ6j2IWS69cmhqDxUN0uCyBpdT91yhHkGOWFVliS6LT9edajnaSA8Zn7eAr-BWDE7JDyYMaxMHuBepc1q9e9Doo4k7TzH8p8WkPqcKgoBjZ4_G_x4kW7EkWVkygPTxD3qC_oKzYfhyJZYa21jAagyKV1HPMJVwBaPvkjhYpHbFrC3fKRIV9ZbKtzH1ZTSPsfggGsCdIssLnWMhWgZXSgWGM38DBPAErvBzcHyGjkfHYkYOghqepX3lZDIxk7eJrUkovsuSqfWFSkl9PGUmBFtjny4KJMLqUopdquY7eIPyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKPgOiakNKl53N_qnR4PubCQ0NNZfoGA2v0SFO7aQIwGCd0YPgI6DNTzke_pvg3HWnuX0SKz6O1nqjNtwoOJQ351uWanMcqQ3hYGWDjH1Xc-YYQjqPqNPbM4AveJgB42NhAOFjS8-DfSpSADOk47N2_fPulN2W-aWWhP0sv23RPt6h236jVTOyDdDV-peK1nATxE5Kt07DRoN8IM17dpTAi_zl1fwQaLy9QMSLwWPPgfISP6m-8021_iwmY7iLR0LKEHEJeV7ZGBZuDDIS9BNL_PX7WHv8SQ3cMWYjyYE-0MnqtDp64htpfmDZCFYEtC27no4_tna985woq9lIWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbGYpkD1jDEFQrZgnMmyLjxGDYmuF13BxasyhjYiQbMMvqQic-HYG-G6A9hrH3Xh77_crjvsNHJhe0Y2IHc-cilYwqZxaLoiIFmY_JMDAEsFzu7y4zVlzMdtqCjQbgrisoZaBUFvV3MUoB3fyF8repY8HgLoYfp9splQrl3NQo4525V8i7_n_zqq4BEr_EmdcWka5hahPswmXjGW13Bxi8_kBymtVsu749uswA7ooTqrMSjL3sb5hkMNZJma0nKH89mAFteEeCKPxBo65ydKIr8CXdGaK-OEIgy9dmtxIeD9-uqV4NpSL36E-3iUQCP2pxWQuE7EnheINW6o6MrunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZySUpoedLvmValKfuRzVO4_ywSpLcv1IxkIU7w_llg-lYT6zveoEe5kKzE8b231KRSxTl9cQX6Fyd7RAsrx8nhl8xRsfpPj2PaTqF1Z0HNj8QRyxcvvT4WaWWwJm1LtshCMzApAaNTRWdGS0CaQlCIi2nm5kM7mBq6py4B-lMZxquuHcfDpKxZSni3ROBI_WbfTcfCwdJGmw3Yj7_eUc8ZAj9O9FNXakwu4cnPslYXJW04ulorb4QWP15A6Q4EKViv3ldtiLHQ3zcRWPFekxZ-nnLdaWOCYfr_sm8gsCW-q6nhaRIYGK7Kfc4IdkCpRRUYfaCN43GFiiNpt18G1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLiA7rKCKMSyb88wfeHFDBDLu0NvWpAG8WAGyYLr333ZzlvZ2efoHZhc8VUDi_bbiaNdj-CQarCbvCW-A-9T6seGWy3g5Twwnsy0ul-ANtgRQ9nJ1uvr8m0nirMn2W03kn7tT6NNZwoo08AxoLWnX4DP2n65sUBhCBIL_LU0KuxnRJCL91sFzbnLss2PMiewLvTkmCISEY0kKNHFA6Apc3YVUKic8-gsUlQGsUYGXeM0e_xNe0WISrfZ1CiUIDfm5sWYqe5Kjzo_bJ2F3Nu7tVoE11crd5lG4XO0U9DNPqRsmbMlF2enRKQfeyxHW4SVtJBfKAQAJ5WPz_ZNgWpacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVf77KjXtwBH9q6JF5AsNT90x9Prs4Nes91JWtfpTKE8kd76X4c9ya00aVopC-1Ya_4uLExJnG_dQGze2ga_8fXQ2n9FmWiGyBhCTa6phJEJ1eP8KNCSLesHBUzlXsn7oCvXoE9c9PmcE-EqmYxN7F5NhO-SoOZWaZ4WEQeQiGSt4SIg9E53nQzlqpO6wVuVBK51hmRkRlAokCKUquodhNGnRvegGUyTixZCtSuM3QBzcVvAWMT4p5mlRR-L5Hi0GpcMqJjN8HETchmCi5u-61M4BlDtZMgTlT48fkVRtvkMl2LftBgkW-Qa2WLLZ4PRLat5t9Hh0h07f0squgKvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKPGpCIyeI0o5nrw2pQ1OKWnUUBgAAv0PpOoLcbR_U0k_IBHzyBQWemXH5wm3BMZGDCE1CuN3QL-4Vj1dDlCMGEd9KKjZsZvIUg-eQ3uW-aqNpgaJ6cu7fEHm2cu8CDvb9KqfTtweSkyzknS6iuStj4RwMKN6rmPV2hPfmtkNkAQRNEboZgEWyDsNGk960jaSXIlsKkwbQ9u1SibmPYX868k_zy_5eEDmLJ2mVT4nErcqd2_Lecb9qpc4e8oKPoqKQrGQ_OOs0s6iGK3Koq4Q7QJi6y4S1SQ-UDSTTX_MXDWMDnv54zNChGrPbSEsea3MbwzIMnjqyYn0pKPxzubcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX90uO7T6MshIvu7FOR3gU-ovvc0yVVPM32mteDbyVundhx44bvYPchc5PCZ9yEm-sjn0IVEsPVOabRfCnaqGsSNNJVNSNrUoyiijWyn_QqIYPM1V3s_HxcvivH4avCkZLcedJ8u0-RrZpVOH_XqssHBDXOrl0ZGA4XPf-lYTDqyq9VFEnBAZQL8xJDY8DZ-gWbQTm2vtx9wsphjgJaoeTib4Z891QODX3FybZ4bpTS67iWFaxOiDPHBQOug9jR0KY9eabC_0FK-EIU9BP-FlcZsGNPvASxr056xh7nfISccQz6AMuwt_ywrd3zl6KS94TTFqt0jpBXMxaotcK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-X8xnqfWVgskM_qz3Y2Aa8OBr8WvYO08UIh3iSXXufuZUOui9wB0Ug2bkiehnMcorCEaP8oAzolDJ0pF9iS_m2-HJaT3sSmeefKtsfIpqg77dXFkw60aajQLxV7lS3NXQkPJTPuiLACzW7cHMcxzdBXEuKzY1BUWB0vZm1JBtXNHjMNc2ugXEWCQZPxQVv4OltlGGscGNKpc29VuzntQ6AQOJuzXknxq9gZ3MwOEvcdbs-fwPJeLbn30sDWwhuzYyLiaB-GPjAez9ZsWeGTmwnaddNs7czckZyakBUdhl2_JwaHIxhT34D91VW7AeZZSteS8YJKgbr6LkxKOtGbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGmlC5OyxO4AcjgRs_1YZ376tJwB8okr8aqyE5Qa33nOGBPTt0iyl5a8UjfDCDyoS4vJdDAq0WloGKjut3NSctXAncXOfsVpaDtgEXSy8gwgKqzXChYd6r5TkrrMlUAaNOCbtPHwZj29L67ors--6ACZh60kMETMMPpRJceT6Niu_CuVFWouWrzFQGQLqr66sXTk4Vwx9yD4gIHSNGEdEp7IhI668Vp9l3nPiQB2QiQqg74avcSeGMKPL96Gcwp800fRbgJ54sWsfGw4KHzaSIgku4rHgy6XEMzK0_pKqk23JAz1n7iM1r2uyW6VQm4gPb5DHn8vITxQX8Dm2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=AVbwaLORhizx-gZtQzi8wqh1bDjjk5UeS7OTAvpgYZxtAhDZvFVYwD7RgLluc01XgRcKZxQLmLzijfdSExpX9SblCX6jDFiVuCqPsDSdVLIkE-nQL6olknC13kCdwrdwg3u_i_uhowgsmdDyF1gP5dmZbghdTJZYK8Y6nCPhJPIcxP302nN5ah7SvDVLDq9muxDupB56UML3cOSZO1dA2iuQWz687qYdBCY8vH6CZRZcrQEVpdtP-ZHRcmujxUyivp4XNw71tQK5byr1cQ9BncHCNmmi3ckfacDNnKcNWT55WLJS9QMUgKSgu9vazK8FjhPR-FVbQ_juDai_ogj48A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=AVbwaLORhizx-gZtQzi8wqh1bDjjk5UeS7OTAvpgYZxtAhDZvFVYwD7RgLluc01XgRcKZxQLmLzijfdSExpX9SblCX6jDFiVuCqPsDSdVLIkE-nQL6olknC13kCdwrdwg3u_i_uhowgsmdDyF1gP5dmZbghdTJZYK8Y6nCPhJPIcxP302nN5ah7SvDVLDq9muxDupB56UML3cOSZO1dA2iuQWz687qYdBCY8vH6CZRZcrQEVpdtP-ZHRcmujxUyivp4XNw71tQK5byr1cQ9BncHCNmmi3ckfacDNnKcNWT55WLJS9QMUgKSgu9vazK8FjhPR-FVbQ_juDai_ogj48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=MAx2GaLsmEgt4dDHKnAVHoAFY6r2O58iyW2nSpPeW-lX1ybYrojevnaZEb0zdecX9Y0lPMZ86qkznntUv83nC64Oo3EpDKRsSkFnWkc6Gr1IzNeeJa0WtXmEPjmQtMrEFZwYq1cugvF3iG4mVqoCBpnvYrY6_eEnw7kY8zdlJYLAQJjgno8bT9nIT4Ng0Ijzh_WstamBrK6QB6sFKJeaqspo-fW2VENa-jknt6FTLSpcrb3ef8nkJpDkvobPiZILK8QKt5rMYnRWjQY_kE-uWouiR38ZXAdbaYAaHAw1MfuZ_UNgLbU9us6bKRwGmET_GqCbaS0MM1jrhWrNoeoa3G8KtGhSwnyBLDXb97OKd1U7WgZoz-mCPuXePhKJn_koNzFwwO6TuGdrjjbl4HybRS_5QqLXqI7IZzw_bzYTbyvIwgHdp33jHo8m0clfNYWbnjaJljjLK9zJv1lk6Yy_TLxm93pPo6b9Wo9B_0gtnvXR-aj7rYFKs5rodYusVxP_DMF-4xmnNdYrMmryiEXFVMRyqn8Nw8MkiHzlPeUJ9ed4Uy62EhpdRRGJYjy5NdtVc-EOxdmvjIkd7v2lC-CJSB40Fn-VKlfhZQs1b7LOOnaTmqVxPXc_JvgIa9X84yzpYYZkZFVUG_O41zFj6z-jepQ9ENlTBO7V4Z0FMIRjteA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=MAx2GaLsmEgt4dDHKnAVHoAFY6r2O58iyW2nSpPeW-lX1ybYrojevnaZEb0zdecX9Y0lPMZ86qkznntUv83nC64Oo3EpDKRsSkFnWkc6Gr1IzNeeJa0WtXmEPjmQtMrEFZwYq1cugvF3iG4mVqoCBpnvYrY6_eEnw7kY8zdlJYLAQJjgno8bT9nIT4Ng0Ijzh_WstamBrK6QB6sFKJeaqspo-fW2VENa-jknt6FTLSpcrb3ef8nkJpDkvobPiZILK8QKt5rMYnRWjQY_kE-uWouiR38ZXAdbaYAaHAw1MfuZ_UNgLbU9us6bKRwGmET_GqCbaS0MM1jrhWrNoeoa3G8KtGhSwnyBLDXb97OKd1U7WgZoz-mCPuXePhKJn_koNzFwwO6TuGdrjjbl4HybRS_5QqLXqI7IZzw_bzYTbyvIwgHdp33jHo8m0clfNYWbnjaJljjLK9zJv1lk6Yy_TLxm93pPo6b9Wo9B_0gtnvXR-aj7rYFKs5rodYusVxP_DMF-4xmnNdYrMmryiEXFVMRyqn8Nw8MkiHzlPeUJ9ed4Uy62EhpdRRGJYjy5NdtVc-EOxdmvjIkd7v2lC-CJSB40Fn-VKlfhZQs1b7LOOnaTmqVxPXc_JvgIa9X84yzpYYZkZFVUG_O41zFj6z-jepQ9ENlTBO7V4Z0FMIRjteA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=rZDc3unrBECEVQiHMfiKy1k-1o79z6nE25f6ts0EnANyk57otB59F0WjBOs3l1lk3HomKnP00aRZ8CCrA8Axw07K4-Fs2f7ahJmocSOhL_4zKnI1cv7k5i3FkCJ_V-KVLrWZkIH7vcDoOMZ9urkxJdtMk2b5eVMAVgM0CTCIItJYelaDTX0wLzB5CyfbbidxMSA_h1qbJDTEGdk1Qf3yfgfe2OSz--0OkRV2lD0OoXqXilBBGGwDVhLYaLfaruCwGXaFhDY4RqQ1-Fr-IW51sF26GbtkqUiiO2YwrZgTZlODDwYuvEzQZJSbBF16Gun3BEHawiA_Fc3SfHlnJ-odMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=rZDc3unrBECEVQiHMfiKy1k-1o79z6nE25f6ts0EnANyk57otB59F0WjBOs3l1lk3HomKnP00aRZ8CCrA8Axw07K4-Fs2f7ahJmocSOhL_4zKnI1cv7k5i3FkCJ_V-KVLrWZkIH7vcDoOMZ9urkxJdtMk2b5eVMAVgM0CTCIItJYelaDTX0wLzB5CyfbbidxMSA_h1qbJDTEGdk1Qf3yfgfe2OSz--0OkRV2lD0OoXqXilBBGGwDVhLYaLfaruCwGXaFhDY4RqQ1-Fr-IW51sF26GbtkqUiiO2YwrZgTZlODDwYuvEzQZJSbBF16Gun3BEHawiA_Fc3SfHlnJ-odMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=IDgA-5Hfgq0STuJ9ac4IzHzKGiWczy2taX20S80Zt0YgYF6vnRGzVw-9Gw7ptNVThiA2WW5E0qvWMDfxrU07gsFMVHRgaF3JZ4DYWoQL29xjl7I6xMX6p-SAyPI1zu0TSAn7RbzcdQ3mC06UZrnbCj9B_n0sBhDdDOU5KZG2GIkjyIqvKhUZRIxWSNzL5JC2_Ky2SaqGB7GQi_SpnbMuV7ded0FS405HlmnuiAZqBY76YBDx36rhtnDOH540f1yIMBswgjxroLjOJ3BI1LEBeuadimjiarAeHCyTdl_wvyFT3zC7Okmk0xvZFB0ejNAh3nR3vcd9MxWkIW6M0XfE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=IDgA-5Hfgq0STuJ9ac4IzHzKGiWczy2taX20S80Zt0YgYF6vnRGzVw-9Gw7ptNVThiA2WW5E0qvWMDfxrU07gsFMVHRgaF3JZ4DYWoQL29xjl7I6xMX6p-SAyPI1zu0TSAn7RbzcdQ3mC06UZrnbCj9B_n0sBhDdDOU5KZG2GIkjyIqvKhUZRIxWSNzL5JC2_Ky2SaqGB7GQi_SpnbMuV7ded0FS405HlmnuiAZqBY76YBDx36rhtnDOH540f1yIMBswgjxroLjOJ3BI1LEBeuadimjiarAeHCyTdl_wvyFT3zC7Okmk0xvZFB0ejNAh3nR3vcd9MxWkIW6M0XfE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u99O96Q5oUOgmLKhCcYhQYuQVJBt2F5HWs8dnfN--t9KX6kQMjDELnJylnYTsTKdMVbW3rawO2nei4frPO5oM3BY-2ewO6NsonemhuFMwqAYTnDHARGc8cEMkNckAvIrlGz2gplNqFCT_rJeuj2HyBBvybeZVjSiaQik4vCIoIftvfelfXsdq13froFqecqn2Z1-SRmyqcV187oFppcQBZ1lE1sd06A1sxJjf3-8652vByPOEapu5td-bJgVDBe5aicwwlm9V6Waz8A3z03dj-rEQXYXdN5aXAOLy3tPxpsY9QS010qRVY3iB6JPfpAuJ7hskzpiGO4xyoZn2j50Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=o5kim38HDGTgNQpDYV5NAwruElU6cEK4BOszbFqjl44Ysvyp8PeHXrTFV4zhki_2yRUrb8TMASQwJ6FIo_LWvrafqJd3wFoyBPI8sDtZEyGvXeHp4YicMws-MiyS9UlWzX0wP7cEdUwhdIk5prwUqFnczBSuzsCFUISTNGETisYxMrQWi9sLUD_zO89BRHNXBXdfBJLssQIOpvGAEC7HKU5M-LqxwyFgKasYDjL90GLifycQBSqHUNHy6GtdvMFib6h6S0CPZ9-vl81K4QnkqCq0YAiHDU3ke9j5cKVkUuxQ8Pdb4WbH5ivElMqY1E4LR8_wL9Bgiv5a6rRBuXkiXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=o5kim38HDGTgNQpDYV5NAwruElU6cEK4BOszbFqjl44Ysvyp8PeHXrTFV4zhki_2yRUrb8TMASQwJ6FIo_LWvrafqJd3wFoyBPI8sDtZEyGvXeHp4YicMws-MiyS9UlWzX0wP7cEdUwhdIk5prwUqFnczBSuzsCFUISTNGETisYxMrQWi9sLUD_zO89BRHNXBXdfBJLssQIOpvGAEC7HKU5M-LqxwyFgKasYDjL90GLifycQBSqHUNHy6GtdvMFib6h6S0CPZ9-vl81K4QnkqCq0YAiHDU3ke9j5cKVkUuxQ8Pdb4WbH5ivElMqY1E4LR8_wL9Bgiv5a6rRBuXkiXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=J-au5QoY81VZF0U_R9seJ9jAUmHT4WEgbDn1XGuIKgJ2lEMb1LQVTFeRHhEVHVE-04JqHiXdQCTvdpx_GB1Nm2cd-gF7DjSxDf64uXSEEb5c88ofLzsyujYzJ_2RbbFtoDy6HC2SQ3rKMyD1VRUL766oBmgIOAlu0hkNMzYkruqQMfAFRBbvsb2CeN9C-SiKX_xm4a8WZ8JqS8u5rBda8BArNzbZzX0BhyjCSlZKd5cq_s1Xt7NcDfkZ7rq6GDdRLJtG7AOQAF-w6itm5TnPS74Qeghg1Xfxk5GcG3iSCgnEW_BQ4FREPLxvWa4vbBQ3DBeS2QAjutxRmT7dmOUWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=J-au5QoY81VZF0U_R9seJ9jAUmHT4WEgbDn1XGuIKgJ2lEMb1LQVTFeRHhEVHVE-04JqHiXdQCTvdpx_GB1Nm2cd-gF7DjSxDf64uXSEEb5c88ofLzsyujYzJ_2RbbFtoDy6HC2SQ3rKMyD1VRUL766oBmgIOAlu0hkNMzYkruqQMfAFRBbvsb2CeN9C-SiKX_xm4a8WZ8JqS8u5rBda8BArNzbZzX0BhyjCSlZKd5cq_s1Xt7NcDfkZ7rq6GDdRLJtG7AOQAF-w6itm5TnPS74Qeghg1Xfxk5GcG3iSCgnEW_BQ4FREPLxvWa4vbBQ3DBeS2QAjutxRmT7dmOUWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=fTh4goCKXsBLvhbxU--fwOvSvnurjwekvj942jx7Uwc1sHYXLJtbSGoAX7KqbBaHai0w4BvR0OtXsOdsOI70AXy2AbV6ompkQIbWBVlT4YBYAGARIobNgRnq8wgDgpO-_10_LiJByLqTNrpXWTAu-KUMmVztg5GtMriY_mD7jVI7aER1MAxzTWklMeQpJaT-kCwybLeuw0Izp2m6LpxaUmipdZ49utrffrPRp_SeVNxTKSLAmYkuKPw9RJdddCWEW277x-3snAzNXPEnfa8cs5tlvgMuqbEFPisCAw5AhDenO7uRpbwWSTqFb4zXGyl6N01_UXBE7kqhXwX0y6uySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=fTh4goCKXsBLvhbxU--fwOvSvnurjwekvj942jx7Uwc1sHYXLJtbSGoAX7KqbBaHai0w4BvR0OtXsOdsOI70AXy2AbV6ompkQIbWBVlT4YBYAGARIobNgRnq8wgDgpO-_10_LiJByLqTNrpXWTAu-KUMmVztg5GtMriY_mD7jVI7aER1MAxzTWklMeQpJaT-kCwybLeuw0Izp2m6LpxaUmipdZ49utrffrPRp_SeVNxTKSLAmYkuKPw9RJdddCWEW277x-3snAzNXPEnfa8cs5tlvgMuqbEFPisCAw5AhDenO7uRpbwWSTqFb4zXGyl6N01_UXBE7kqhXwX0y6uySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=jgbDEJPUZmJiBVlYnXoM-zxgQ6u7cF5ztegOJs_3UOkFKrq_v3lbGBe3Gwjq6BY_GQnEvUk78lngQvIqbTddeZ6JwDjxPbB7fFKRqj5ftV7kcyV2_ui8uE11OqHBIBo5x4n3a8wEHxyNrWqOYh4LdpbFvNTybwe5tdgeeaADt1hCjOf3EqBoge6nSTACVpdxOUm76K_CRBifJCBL9yMMl3Gqna3VC_tACWeVJ6AnPiKh4RkmdmkTK8os8MPqbAxRd8UNPjdVd8RzTptymGbmE2aUI_odiA0TPXXHKcHRaYIeNaDjrGUClghiQFxrFYV_dTIFB7qOS4oKC43W7Hmmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=jgbDEJPUZmJiBVlYnXoM-zxgQ6u7cF5ztegOJs_3UOkFKrq_v3lbGBe3Gwjq6BY_GQnEvUk78lngQvIqbTddeZ6JwDjxPbB7fFKRqj5ftV7kcyV2_ui8uE11OqHBIBo5x4n3a8wEHxyNrWqOYh4LdpbFvNTybwe5tdgeeaADt1hCjOf3EqBoge6nSTACVpdxOUm76K_CRBifJCBL9yMMl3Gqna3VC_tACWeVJ6AnPiKh4RkmdmkTK8os8MPqbAxRd8UNPjdVd8RzTptymGbmE2aUI_odiA0TPXXHKcHRaYIeNaDjrGUClghiQFxrFYV_dTIFB7qOS4oKC43W7Hmmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=SxYpCgenVINkGcP0TGPlI3gF5ds8Bzau9uewG8qyqk6n9UOil-_EMZKiSbQq3CU3S1K9h3VMvc2G9rQTA7a2HCc9GBmxNFIB_931gj-i8O3ofURcUm3gXTWqSBT4OqksBqxUCrBoBnz66bx9wVP8O_isGCWdzLJUxnmw5DwV0SMe5oZfoR7plHi2fmM3y4M139ZHGzjahS8ZSVFExPsgUvd8ZM-1QAoQC25r2mfjh1zCuhmvZ7p7YfCyVmzXJJuJYpxyBhoQMOBv1EYR9krldHojMwJSKb_w1ftDlwAAizQZyCTHP8FivOD5TDdRcmvg7DBBLYeYDvnucGGbe65t2xlpMF8ejFpEITItO8C31wOWaXw-CCKvoDD2UJYNiea_F65jX-0bzPJFjEBR4HYU-m3iAir93LRt_j9zqawIDFVONn4HIkMKN3TCdXL4O_PTjlUtLdfZluQ9TWS6w1e6gHx7VTTL3W4xd0elialzdtBwbnWMuGy82479ERoDSUTOph3bNEDA4s55L-vPxKHBp3T239-kgDTLnZKLsMnkHTYmS5p-Rhfw70PUPH6-nIdoMtEy0OFP4FLEW3GQrylycwjLPUEndhnGVn2376x63HLRwozYmpM-3tc3VCaI2RXsUL1IQv3rHXjQf2PIkgnUTuptaThAVHCdp_QOq2uhQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=SxYpCgenVINkGcP0TGPlI3gF5ds8Bzau9uewG8qyqk6n9UOil-_EMZKiSbQq3CU3S1K9h3VMvc2G9rQTA7a2HCc9GBmxNFIB_931gj-i8O3ofURcUm3gXTWqSBT4OqksBqxUCrBoBnz66bx9wVP8O_isGCWdzLJUxnmw5DwV0SMe5oZfoR7plHi2fmM3y4M139ZHGzjahS8ZSVFExPsgUvd8ZM-1QAoQC25r2mfjh1zCuhmvZ7p7YfCyVmzXJJuJYpxyBhoQMOBv1EYR9krldHojMwJSKb_w1ftDlwAAizQZyCTHP8FivOD5TDdRcmvg7DBBLYeYDvnucGGbe65t2xlpMF8ejFpEITItO8C31wOWaXw-CCKvoDD2UJYNiea_F65jX-0bzPJFjEBR4HYU-m3iAir93LRt_j9zqawIDFVONn4HIkMKN3TCdXL4O_PTjlUtLdfZluQ9TWS6w1e6gHx7VTTL3W4xd0elialzdtBwbnWMuGy82479ERoDSUTOph3bNEDA4s55L-vPxKHBp3T239-kgDTLnZKLsMnkHTYmS5p-Rhfw70PUPH6-nIdoMtEy0OFP4FLEW3GQrylycwjLPUEndhnGVn2376x63HLRwozYmpM-3tc3VCaI2RXsUL1IQv3rHXjQf2PIkgnUTuptaThAVHCdp_QOq2uhQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=v4O0NNJWIVn-a_Le3ZJk8Z8t9esTx06_d43psEik5ebEVmoqfmEYmuRX-x-BcCHvpPyeiouKGQZ7r5k1h-B4gyd-BVoWyIlx5IpshBMt3b0Vk65b-ptzVD6ZcH8cTuBlw4zqsax6-a2jasgkWSNUah5qqeNs2_7m6u_DmVeHKwJIKHHzmLJoQEUvmcwfKW2cgGwClqnmc5Om3qHH6eL4Osb9P-LgAOllmkpTZkESXneN7ZQb9Q-_nmWpo7UO-BHSUgx1W2Rnsnv_xOIlh31HtvPoB4YOTn8kUr1OZL7ONpV_DP2hBAlaE_mHligz7FmA7WdApIw4XpRXD7RpJwD6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=v4O0NNJWIVn-a_Le3ZJk8Z8t9esTx06_d43psEik5ebEVmoqfmEYmuRX-x-BcCHvpPyeiouKGQZ7r5k1h-B4gyd-BVoWyIlx5IpshBMt3b0Vk65b-ptzVD6ZcH8cTuBlw4zqsax6-a2jasgkWSNUah5qqeNs2_7m6u_DmVeHKwJIKHHzmLJoQEUvmcwfKW2cgGwClqnmc5Om3qHH6eL4Osb9P-LgAOllmkpTZkESXneN7ZQb9Q-_nmWpo7UO-BHSUgx1W2Rnsnv_xOIlh31HtvPoB4YOTn8kUr1OZL7ONpV_DP2hBAlaE_mHligz7FmA7WdApIw4XpRXD7RpJwD6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaiRJIqVqpcDELI2f3dbfXqmbBjCS_erjFwGuRcClH5mjshcthYemPFjP7lC5Cf-HS5Slti8Vfd4ir2Ox4hInOxvc5r_GIb2KjLbnUZ4nO17TgE9dmr9yZl_7bquWo8z1poQjEShm0lDlmg94AG_QSs_joaIa-BmQB38DdWT0EhDnlr7lAelgfX5M3BKIYEssfRYzsC5LnGZCtdQD_saR5rzveHWtnjnDAkxGlmCXtS8cS1Ivf_TaelzVSlIJEZLDkbVPrlIvgQ9hBKNQ0HxTqPEAAZXSL-DFGUGGVulVsF8_CWbjOisRMqgYnMLTsBJQjnHxHEIDPIGbcZAFaOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAvIVQGOg4XmkB_C2MCSrpaIIqt94QA50PB0IRmUS3gOZYp427xiCg_ad3UKO8LEOlxHPiRUXHAc-d-ZLtMc1y0nBRtEdV3m8hhOewCTXQ2BkhIMR0tm4qPfKPdu4g_IGH-nTe2h6PixuGIPKD5HtRxs8bDeE0PSHKxshoK1JWs83Dkp-L7gT1NSrFy2Ni8Lz9NWN5zjzpc7YT0ORfUQQa0YYVfWsF4JezGqBEkv9MqcTSY9kLIvvW4F5ExNmJSxTC_UlS3ICoiLoRa9OtqmacJSD_4T3FDfGVHWb74C2CmMh1_J_UOprhzhDPW9PT3VL8dzvebGP_yC73ulvJKT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybq1YgKOGHULljLy9Qek0vILtHE98QARS4DjLwh7gm0cwh7q9jw7zKTiqanvTIKyIcQgg4z6NC_1YVcsXAZb8LaUPfjaG9WhaLewRFyClATUp46DUbghb8w9LJgB721redL5mX1JnH-E3nEt4mBxWw_XZ1rb_tRx-CX_GPz0AiQbNW0NQHaYyIsKz1EtAlfjbu2deCzbvGoeYYhvEc_SYUy240SHK5kLoeWk4yaSMjS_cFrE-mC7cBts-kVQ9zoWCzbDom4o0J1z1HCxEN0RMi2zzAymLW8E6oou4skMt6hF4ZYDz1dl2AhCgUoO_5MYfFazCKIeVCTVKtSCtz4k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uox_YV19fAFDhI2049w9ibmGW1jnmNoY8ZivgNdSZ-sXojkWYFd7yXNc3vqm81j6b3-nSp4E4HrCQU_ORkuGVulZEbtrzJuMAEoOlpJEwXGlx600LZ0MLM2ZSQetoSylTD6VyjTJcaYGDgcWlccFN8locHJlgMTW353vavOeFwjLRWujwYaExtEPA3Fex1lz9dzMCLavy6Ut8vDbXbb9YjhJIINkDoKmIj8kulKypQXcniMe-DpLQhzPWHPUSbX9v7My60ZZfUaTBdJvsjca0dwhboMALIIO3Qliih8ZG6vFU4hTVv8vG1a9OWBEg68vsJf7toiK9nbFwAANUf7CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5PHv0NJ8x-JaOtIAdjT9RSDzY7WNb77cBAF1dMjyETgfYC92feMGQpOxMS_lXKYsihec4QaRvJ-TkWyu_UcZFhm0sadnayH9115ncPDhohaVoCuxxliutGvWtDfdS0G6b9zknSY-WroGjNEOmvUPDQfzYb6qQLQ_rV43PJbSFAXKMv77CEauwv0jf1dX8fCfmRCMtlLeFH-XEX0GPKF2CFGuJKHx5CdKziXXYvr_wa6tl5JjwdP_D8h4uwd7Y8-POrPXyLyezcVFbhHUZOkbyEepypdHhrDzjUq8QQronXn1wVWRCzL-fLXuiUYfFstB7XtAmjoZVnWKYdPn3l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvtkGU0_NXASOWuTkYJIuuD0qA64xd6-Go08A6GmGpUtL_RLEn9Bec8IUtSVSCNUz9iTZdldWzGZzwqdoWV25jcZj0eko70uKXz4khNfLs3wgovEp1Yqc_J7Tt4Bp9uCngUii5QiJY5yOVseL6WDUDRTPnyaKC8WN9f6hnIcS0L3c3vyPX2KlybTnO9uxzNqpdc9ims-jG9QiOgBNBp_QEUzIrgraFgrMjyn1OYZyWTKVvAjIlHiQD5QsgkOSNE4qVoCAH_53UIaKe6BAAK_mNtIIQl-qbX1PM9jfEPhL5cGrwKMLvgXPj4L2pgtqzt3HMrnuE4lqC63usrrYKIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFQKwf0uF94f8BBXeH1L2g2iyl8xPKQYn77uLysDb6a5XCCQlFV2XUeqqwQc_aqmPC50iKC7LggCdujJj1nqu7aBvYfo1H9mAeZ_PZzx6AmHodZ2t93uS9j_6NZeiunxB8jVqDpVto5BzQGkaRtX6IqID2umHOQJd02dqNtZm5cTfUbqOShIDILLS9PqXonpc_imtDykQ5eZX3KcGbKFN-YGbE4fFjLX2kghyeR7MzpJ_13v21mzsyUHZMsF0uS7bfMcaPnlb1VjjLcBaQnwYyjfr7kM02o7a2iwqRQ2U9WplxkHGGDEh4P2WUm8AivnO8f5DAIAvM3UmP6GsC2ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqE1rhQiQyLSfxIOxLNP0tLw6K18norjXPGhHerSEsk02qGBGni3DIAWBKqDsPCtB8waOvg9p7XkiXhivWVMvGu8MMM8qIuf-2tlgD4ESKVLDgbcuw8Nc7WOts4MAC4-TAXsNFWdIf7JE-AAENowr4rnD_yfC4pqimpvezUIplPFra-3Fjo6b6K_tYyQG7MlnoGhuTVsIUWz518TlPISvLSN8_pnLlKn0N2TsgHeIbMGB3FZX6Z6ztGYyfyUHoSZeBFRHaUe6v3kTK9LLp-Z1rDeJnybiCs2oFqU8dqvSUdbOneIyWcH6PeVjJPrfUYxAlkUVyHPCRpGDmIiL90Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl6QqPbWl7YqCzswsPqy_Qsrxk0fN9ZcBXSbHcEFBqwjEWKQkjWbIObN3p-kqngdoHpSwpKWwAOWHa8YluPlip3jHa8uKMe8yO7iOmzA6BMA3uo-YGF5vyZqNchsItyTqnBnIXKipgavDiII6qjvvtWewwcdpKWvqLxxK7HrGrn3KirCIFTblgFUvrWauNU5REn0BZ6f4nWON1fU4R8nmwXaaqir8nqFZ3D-X1M_-IvBokl03FHUJL1Cz9m6S2XT0TPcA-RyFUcpZEfUwewdHG4PrgkyOmc3D40-D-x_K6-Y2HT775h9Gq6iAIAebHuUDPnNf8CKefc6O0T3Ppc29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJw3IIvR7Sg_6yBbNbNPCcJkoutsWUvqzVqIjwnp8HuhdVlHj9gn_oFcRimM3cQXpGPbnrziLos10i_FPA1ScN5-JmOcjNxCWFt_8gp5UM3BbSR5qsI9nDybVUp714dQRwJoNNmi445OTOoMdmz4aBe9OVB-XnoLdjIR8BukhxasY4LrvyVeSHkdGFPrX2m_CE57oqEdIfrgHtkQfEAZS2Pfz6KD6Qh2Rt5soAWj-bIoxOoIruBbWX4Ckl5nDK5YjA0w9Qg4wp4ODkVhYYp-Ix-oBFVvvW3xnO8GUoW1t9-EzSRFMIMfkllNtpIkPk9r5LCkCTrBKYacKgadqljgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMHDI35b7aVIq7AxfUbrM4lsrXxP-ZBoYGQvOGYLpYeXVqHYFOcCBCRRW7VDc4MtWt-bxe-tjQg-IerhlV9fGHHhfOMYp_ybqAaOHSZ7wow4TL76zVCo6j1e4802HVL7W3IgPN-bnIrjGd1h9IbtNSBbUcZNq6CjT-ycOlHNpEicWWqr0snSF_phkP45FFxAFdm10FFjcppfW6DQXKS_b9z36owRfxPDFLNK04h1dQhu-pA1B71BOjfXQ1TuiFhPx9ihsxCfA4OKl0oXZiFJCb8xMypO1INe9O7yBFkIvCtsQT4nA_mSxB2eC3ngekkCFBhhlhVllVDnNwvKizyENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2-W7fRvIzK9Wu79wytTgnU2xwRwnE74KMpUGhOJyBRKEqBiKsl1uuLmr4P7_u0k_UZ-5ilmB3iug8SHuhyBN890SBWd-0yHkhGf9EsXcJvpns7ZWCShJc3MIiZ3C2VTGsp2QTCFabRY9HHLtykOKZO3rI68Yhvd_N1Znz2Bjy5dmrCqYkoG-4HagL6vRK43nWaeewjKGaHgYpLJBbviY80jBNvsbWvslswVSA1vmILzWJGBxg0JYz5T7EI6Uml3nHoSyDT0E69aQvXpt2-_g2j57pDQy4SEjciSVjsy29Ft2T_QM6EDtSCDfGcOlj0-pHgBOzXCz46bU4Zvm6V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDC3ZcEJ2gnKRi_FfQNEucxVLqT7s7yjbF8vz949Ie3WZag1Lt-vF3bt8jWVDD2evy57d0StpopOJOvt5YKqVuyGHqFFxqmkLiSUY4xdBgbgkd4T7vs_qBOhHoIO7MtOzd_NhwUFrS9SfFv1jZpH9cX1LQLcDtZR0vRiA7rM7lv5X85VOOzJD32e5H5dN-g1wp6Nk4NwTwLzF0FT4NEmHEW4VKWc_82Nrnypn5MVMuuSYhKeLER8h2Hl0RttZmwNnr2vftW8h20QCxJNRQ2O9sxWvfF-d1BgNI98Eq4M3J0IvahcEs9JgI5jwQ7CfhC6HrQjVQvCTwcxV_x0kPP4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoB1q3kMznRyryeJjeQwnzF8JQBSECU1sGa8CMa2t7-Ja0oFx9UasmF67E6KswvEt-EsADMHumN7hA82FrwN8vqbTtuTmLkE_NsZoG4wJ6wizgLNdOI-pTuTz8COk9_nmOWu7VESTNwnjStPQEGoimp0a0x54oGitqtv_kpl0XTThnvYgdfYkhm4PWsxpCgUcY-_uNpm3Or1dTQCHo3IjHE8dJe0TcfjMd3BqUePCymLyTFse3Ad_ASWplF8fNmcB2M4bAPoqQEPccySk1RSvnGgQTdUutbxL1j3dQx-ZSw5OTTdy_O0vYDoEhzFN8byGGF3ZSsm3jP7Ikk-t1AERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnRxG3dneRZHaKe6PE-ToRSPbLYAqpxX6ZCbg8qPDATlwECuReJ04Dg-tx76umHjHQmDrxfrYGVpyXJkPGJm_HsAH2Bwye5a77r3DDDhfyNz41qyQ-1AvfbyZgvR_WuHxP10XHbcixPiEX4tV5Qw_G0vfGLPPF-8dIVkJDqO90-1Mw7pXyakPCsI9pb_jds8TIcqi-PlhDsa4ZVXFeTJBZ533OVVUBCPdUywRx3TFKf80MEI9TTcyiVlVr5mwa1AlXUhabV5y0YP0i4O-iVylSt5zbrv7OqcSo1zvxpp5oCTDDNpFDvj-UtXezCjLiU7BcAueUjFCEr_XWOWUR2sDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhDpXUpySQh15Sh2eItdqXrsUDmoWMyRTioOEFMnr-VEVYn6QpuuO1_xCkB1g2kBxK64OdMokfzdGqda8aydWGSAs4E3lf3TRkY4q5kyqZ1sVnFGw9927BHclvidZe8WRnlm4o5jQ8pqJ1dyN-GQxDJvZEj1n9yKSxw7HYCoPyvUpYwoBVe98GtJBoMpg16oEfGs2x8G6hEW9cVrD6hjIO3yIag5_ApFRu9enXlsqkiUQ3CRnLQEu8cgLu_DK-lUInkXBhc5pwqIMEEYffno-Z2VWp5wMx4zim2L-BKYrKsQx63xycz0CjDO3qTyRqIBfjSPylKOVgxExceETvhacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9Xpt-HcJ6pDL8sgKeHzSlNc2SZuun6qfRYl1mK-gdwFpaCGR25eFKwcsKinNMGtRIUY-nioBOCySCk5UaT6Mpl_uNA9u3I8pU24GNmrepamJg_0a00se6BSAtbh1lF72bkQeeBB_RGJKGq6tW3JYQBnKL9RHjF8c609-fifUVNyvt8YEybFLmgDltztww2iIT-H_1WpidzkqNU8_XLOhhP3QJ3dIEfhicbJLJebI_H5nfK38UKUh5XSvzls3ki9tMnD0_uCdcWh_U08kwd8PdYiR-7_nNqMXYXCu3xifHUuX8MijQMa4LmeLXUxfBUiZdI3uX6941BKFXF9uI0wtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1v7-8ArdYUwClyZfiBqkX9j2laUpp8PqftAjl4uo0sKA1laBXhIdGt0zpHD2_jtP7H0UeWapIrPaQQhfe7cxyPxtxJyZPnqHYmnfZ5raRmc9lHgB8C6Pz5hKovylUjhFaZvmjtDUyUQeCn_VrdogbIOpWv0USx8r4ZjgG66PHoJFlioAoCY2HqMtl_JJ4lKkQu5BkNjpdkBepQ2E1Ne7jcy4uK1v2ANs1-JvqOMZkO1azLx5-QT3MYUaRW54-ptyyhBzCJ9dN8EP1WklV4sElgg5NxnXURXnTcSBAPH1n6AdsOj1REn5Y0EeIWpLtaE2mge_nO8W4FOmOMIVGBpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyVV_ktfWSYo1Bj0qm6pPYrCoGuAxVobgs9cqIrtsxIVjD3_tk9GJnj5S_Comj1EgzKFqBLclKeCb8j169oAJfLQJOLxBkDoye3Lc5xPwwmr4FfA62lvZ-qb91TG7skO9Ai_QNl7SqciK-1FiQebf2k9ZqtyQIxQK51wcVQlseBT1Qb1QHKQsI86brw800FPlY8rckdO08LPZKRLSC-zzE7tgSuE32-tZ2-IeKniC1IvtaEFpINwAnlkHOPAZ_hb6CZo8rl2EyqJyAU4DBtGZh1WDSrTm34gVF9ibGh1MHRxIHtOe9XfNVo8NZVb_Gj-l4rNy-B1-7TOX00v73xdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUTumRa0NvoNtLdcVhsdUCG1Ni-pPpsVtgXguN_5BZEbZt_X17e9gN5_CjIqGPn42xL8vfhNxWwN6LTgtz5WaCafVUHK2g-Rrro-9CTi8ltj5vXMx3BNIIVM1RorjCE_kH56HP-MWJdARo4N5LkBhzZGssjlswyWHOeMlBD22FXE77p-yIEHYLCkm5doGXYYjtto08s21lOfZTZhdMrig5x5Jn-7A7FuEbzHVLHPAFYKSo5qHlF0i-4Aa15r_P3zqUol1I0Cgjm8yX0tZKmA6lxd-IXwljizEgMMdYzIHG9Of4OTTPNfVQvp0bfS_RzB2pAmX1dGxjQ_r3gn-sZC2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW2aIZ573Jhujqf54FDb06Mc8jWmAixhrF7mT9GYUovVNBor7sHQ_ovFGkgdnQGIyec6nqKL4r8tc9kdy63bQTGxNncG_WUAaTEKKn9rBTMOAjgQqukm4MKfY38qO-vvLa_7r7APRrL2kKL0mbFcPS2x3JDKgRBv0cYMD84PkQsnjMZ4mu5l-_9VG0RPzeH1h4Dc8I_pLMjWYY3doTrxwNdk1lhOcAWPUPBmpx0pm9Q_cvLCWrJJ5XSzmmv3t3KkCBEnfsM-2hD46kIV2Z8jciihFtvbrA4W25iKPmwMTNEKlDsih0ZNHR3zvkQoxwgEDXEJ7y6al64TpeYo4FLx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJKNNcmvPadKx5XsZ5EfqznpCwlauBBMCp7krrIZfa8DodaPplPKOcjvdfazOYnjzcREAQxgeKXBRP_hNkPOAj_Yksn-C2c7LSjy2fTQ2wlL1JRE5nId22KqkA-sYtS35hEvaDrj9uso3Lg4Isr_bLP_TxqJ2iF9isCpu249Y7pkHJpn-dUxm_73lPp8cGZcuiseXocgPKmptpRCwMyF8AWU53-bi-lcTFLr3vIldvUXVWNYgHouJR7bX2kP2Wc0Xf3rK01uLWiuHgShND-CA9snno-Sf5Y5u0ubLg0NbIBM2jKyb8387T9DOuaQTIYtmYSkE8dMh7jCbI7_kGYE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=kCnDSxHGIlFDgMB2mFiBbBty28m1QeFWIFVSz9OCNJykuyd-djXnkfaXbRYMTTA9ZB5JQpMM8Orav-NUitjok9kBvPhV-RQtfc3BXTYuMVjG8I6xZIwFpouLr82lzUZjgeIWfSLkssv8kCnl39qLd5uzR1_mg7VhXR--Mpwbr6pRdTi0ra9M0Mzgsu4vpTu0jGu067DkNptpgFc2U_BLpRRgRuxifSHeaXMF9_IBSnfazMnDj7BX7T5Vb5NgzHZclgpBSdERNEVTIhcMGwrYaKLTFWQKffwtrJqqZIIgHyZpDyCUoJHgzOJppwzA1IbzlNv3KK9U56ky7QzTZag0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=kCnDSxHGIlFDgMB2mFiBbBty28m1QeFWIFVSz9OCNJykuyd-djXnkfaXbRYMTTA9ZB5JQpMM8Orav-NUitjok9kBvPhV-RQtfc3BXTYuMVjG8I6xZIwFpouLr82lzUZjgeIWfSLkssv8kCnl39qLd5uzR1_mg7VhXR--Mpwbr6pRdTi0ra9M0Mzgsu4vpTu0jGu067DkNptpgFc2U_BLpRRgRuxifSHeaXMF9_IBSnfazMnDj7BX7T5Vb5NgzHZclgpBSdERNEVTIhcMGwrYaKLTFWQKffwtrJqqZIIgHyZpDyCUoJHgzOJppwzA1IbzlNv3KK9U56ky7QzTZag0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fodq8C8LTLIewzY70yQvG11Ye5PSuX0kG1BFeSRsSOlzOl0ykfbqYO2TOtRxCWbL-JITOydmlji4HaQxnYM3DfMi2ISvSermeVn9IcJB6Kd8d3EInlELoQxC9Zzjr2AtrC9T6Bm-ookZW3FI1JoYHE55pmeCriBdIMVEScg6eF49QlAC71aEbFFJnnMG5MB5fwmTuTuJyKXX9enMtLsBwyo3M3-Loe7q5KSkR2r61w1jOaOg4Icsz5xFyQwAOiWyonLAOyN1cqm2JCMCUBM-nnONENy8ODoG_fKWuR5mdFKbO1Jk--fNqILkxAgpSEdmmgVHChhQBtVJMXYE-BsDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVvYCh5ZiRIwIbUZo_fMcd9TZY96JL5eirPj9dSTehogag746iznaE2Eq2BTUKIeEItmUMadV9fDuI2uxrFO1UNSZ_I4kSPUpvCzE3KrE-Rng1eluHo_d5l4lV989qyWdqo8N-OweoADbEREv2G9WCeWdsWuYLXRqgEGf0Tz-XxppyKAs9lO_pSnLK6FGieW_uVGSbvNqrmnlxvsxdiURrNkDnKPHxF9fDfA6VabAP4bALo4xahJH3vOIm5nyg8YV7W66xwSoS6Wy_3c0V_6H35dGyLXhqjdjJaf6aMA2_IEkxCs3o8g0zcuAELdvNuJgNDMpOReiAWp6stxk0gfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZnz80_LPZaxdKCCH5Id3GtXB4OLSJLdMeh8Q0XorRC_Ysge1uejX09757pfF1v8J964VFE6D8LxVtOsBP5x47PhN7hDDzBAqTCEz0Hrm-9K_M7qiTOrrYEGOL1yjp9MTWlLtimGlUITM-B2VsdIkfN_8DcmD9B7nC5FItFsyDwyURz1WFt7fzDvjnT5b7wBweJ6s2LnEVMKW7AA-3xLTxCU0wO5LrzNF5wwn8hFeJpCIjKdduU-EG_omxXO_YWt9-zMihgaXR5JcwXE9t9Eh3w5FZePABY0R_XXhJlFNKbnNoDW1gKgXYrtIUX4vJpJwcAOhoKmBlqm1WTy4OLn2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjyc1IW2npIVZZ6lrwgSVzGKoTzk8hM3TXOQ6FXSXw0knhNyrXzSqytlre_beMciIZOqOt_MRzyVt11o3tKEPH6fkBcc4JUo-qNrMDS8fMhpizJEEz7ekpWBpIO-luYOrU6to3Sfz3MqupB9YJmxCEUaFuukb3Tzmf3fOsYLGFepWqV--oW_UMDA-KSz7HzQpuHVELG34fp3JCGuk-LOGEPR9d8mabmVs_uudgabFeIBO0mBjjyGoSy0rMCeK58NCVbyaLtZKCvHccXVsHZKPSOC2wOv8tp00qIy39VIfiUNPu8DFcpWPIHRDlCDGKWq-5s3f4gZnaLNvudujqP9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsF_jZliw1OMjgMrkiFn2w7XkR0kEhRejk8XfmaKcfAwEpMX0-Cbt3qjqFkvfi1HK0Wa3JYRvEnYX-UrheAA5qHGyms0p52_vdAaFd452NOcnvC-TVRX7BKpDqgQRIA5NbSv9w3mrK9c2b5PSctRnTqwzIuHf9ZxLFqeLZ-PZI62QwzBHwZdz266RIV6wa5ocByik-ITxR8tx-QHG8ZK5d-icPxMwyMoWyG2ZdtOFoLeZES5L9xfetaF3p3Ua-ShSnev7VORyw1jezUmyPZA0hVNxFLbY9NgrkjfVDc4_OcnARWgGn4_JKgYtogXDXokA3hTG_tAsH9A_vguGFk8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8D9LMsf3TPMk0v8tAZuUH5cKZ7hH_z3tlW2-DbsjKg5kBulvzq3YgEVjb5mxnuJpYW6kHh7yhNGaQSFDvB5xagkksQ4FN0KTnujoz7XSk6IiWbofGg3s7r5b89E7Ht3Jpc-qo2BkeuxcvAmfkwvQYI-J0L07jaxehl9zR2h55W-cv_QSoPI7rdikiZ9YsUmKapKixhdD0QjitfT2WW_AQgy3dWOunuvVR7rwGg38haxMqH8_Nr-B89yrFHcrJw-OWNzeVNUOHZ07zzVMXF055IsSHThlhsx9wGD51ioVRCwn2zDftqRacLJ35bWxUMfKx_zlS_WDQNO4b7YMTFvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHom66wUWIw-YbAp-g4UyzkglbI5B4ddjUlb6PNqsv0d850kjY7o-c7SZ2eicwQXPuGYLNPuRRgIlHMcCtKWmfrsBiTNvYwejH80c6iKNb9pqnS3tfxBhqpEct3s2kYDCsLsfnYXdZucsrJcWjD7AGvqDAqcO577bj7X8J4K8yf0JvFvUL33PqiTRHkGqRskgyuwlaXh4vdzXq0YUAvm_mVJS6hMZQ5h5KZwE4wlQULDoQSdwiLzA4t-kZCgFpFlkGp-_Q3pySOVFHYrG9Lj9xHS4HFLbNoen206gbJU2J059HFbRu-Dn_HhXb5x4auh6stAHl6nraGsL__AmDYS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5TOsUEugd2UhFyul5GZU-0ZdjubiaCeRsz2p-pKUtYo5RrhsLuvsksHn84QzZWPrLeSx8_cPlNqypdQNBYK4QTG5KkYC0YKZnE3yhGSWP-P-fT-qBBVd0j2eyzA6MqxLS8e9yfJhOIdoSsuUxOznuL9fghMlOQbJoQWtp-dzPKm50bLt0kBrZ6qBDDC5OJZ9mM0VBYosn675rOtH5EsbLakL0x_IVOwRGm0anPORl4BVt2oIa17lioPzKS07XK8CHEJPlyuKQIOQZuhTA1UMWBNR9kskrV1P0gIK166ghHkRtDxD7i6oiDSZM9rdsXqqLD4Byc7MbhP3qiB117p_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzRLUSO2HFKJDI-Z2t9lQSoIEJP95D4Kf2atmCsRj1orrF4RNFfwoQK44KMLqC1lsMfpHY9SCmKIYnMWKbkJCemLFoua6qsoQVLCD2nNXPX5UiXeNsYHac1nTyz4HfaHivGGo75zhF1muOIJq_gL4viEYvHX-D7tx2BHMvwKpV4lBIr5Pi9TPFXmVYoob7AJN-0o-CMB-5s_XiRRf3dnPmyMNvK1iCTsrSiuT8tojYXLszqoe60Qk9IPnp7PqeLQ1-nkWHei1azp59ioaxoA-DTp797wnwTlU06nmiq13LU1UIbH0MWWuV8v4pIG8D_4Gn2fwYVlclnVNmxH9PXUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=Pg8rmimbAxKa4z4dZKeBWhF1u6bioy4XFp3pmKfbdlWCvrWcZJm7-6c2TRPfDc1Q5lAguSxrtOGfte81Kn52UuT8wXMJk-wsRf8OkTv4PPs1mVlZBrJ-0ZRxCzMBjPGZ64vvCMs_6w1FRBawOqLg7LUioND7UkIv09olO_ln2dVY7ehQvTlf4EqyQCLYIGncbI80W5zrixDlfD_pvsOkQqqFNDV_Opa3HGVJYKhzmv8i24RNhhVyuNNIBpeIoHWn-GMNztE3esk7TH5tXajj7AoIqq9aoMeJBCPfWWYA69dmLLt5I4vFltpDBEJ5ig_OsRwZTXoiWImfxsNUJNI4bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=Pg8rmimbAxKa4z4dZKeBWhF1u6bioy4XFp3pmKfbdlWCvrWcZJm7-6c2TRPfDc1Q5lAguSxrtOGfte81Kn52UuT8wXMJk-wsRf8OkTv4PPs1mVlZBrJ-0ZRxCzMBjPGZ64vvCMs_6w1FRBawOqLg7LUioND7UkIv09olO_ln2dVY7ehQvTlf4EqyQCLYIGncbI80W5zrixDlfD_pvsOkQqqFNDV_Opa3HGVJYKhzmv8i24RNhhVyuNNIBpeIoHWn-GMNztE3esk7TH5tXajj7AoIqq9aoMeJBCPfWWYA69dmLLt5I4vFltpDBEJ5ig_OsRwZTXoiWImfxsNUJNI4bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQvkX1f1XvNMNHpMwAUC3sA6Qb1a8-xJYXLhLdZOLJBz7WFjmbtTO6lHDBFejW42wkUxyymWbptB4UaUJdZM6ye8gzcB1sDgt36SGEts6EKkoRv1jOoYvocB25IYzBVqSxuqzZDIdyFJO5d3q4tdFdkqbdnjfB8ScqN6cNNrV7R5VqToXJYJhMd5ldXuaM-EjGG5IUAnh7GhT1ryG-gD7NieQM22tMW5xXm0L3K-MbE1HKttc2Y793wEvpycqVw0jC_iyk7LZgSyYi7TKsTnGeLbM1Mbe1NQk5rjpH8hwS9sZYSIuxjjSAwDcOTr9JToydmaylgcZLwNlb5Upe7wvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZq8YbJ1sFbM7DskpT-nAOSQaNuHTXMgtslv3w_kMug8zKq6zBvtA3rZNRRfwUxLV1SOU_HZZAcPuOWgqbh1LFrngRb0aSoq6yDugu2Scd1hwe0fi-hD3ndIut6dbx2zTs9TH-RBH1HN-WhGIP3rCiJTcDUNo-X0rcgNApUwOWAVaDp9QqYC9zmRicBOGTysJO4gng9SCnRAya0CyPGXrP8G-H3M7bwHG-QjGQm-715SK-gVVhDssgvSGNEYcqkL4QYfKaTdZNKvDgcv_Ff0nO_Hwgvhth-EJJnkyhQMsai1TtExfJoAwVfO7Hpur2EQlox2YhD3B5K8B39-FA17Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m30k2Dg6FSiaGJd5ScWb9ohHpVXIK6qfJthya3hWBtMFUoAbEUF9_jk7ko8Kz_StzyYeT0_7SR8HcsbrJ6QK3pNzGHN4vS6Gzz1d-Vdw5alwpBWVxeNC8dG8Nutfc7ro0TtdmgpVpZhxYwr766Gd4QrfrywWkYo_s7RyNk2Yl1LHSegZC0nFCl42EX2brMo0rG7X9OljFeQZPLQ7OV__CKsatHoxxLx0XgQWmHSwCJmXp_Q-fiLJxbjzDquY0NTZs-Gqhrb4gIDne1R9A938Cy0jGaTDwYzVrCSACa_15CQF39gvRL_JDl6EmGaGadPHJZfeMPvuds3bwTWtLp9BlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=izSNGAOaPWclTlRZpzpuaZjLWijOWSyB0LbzQ_kMnrgp_OcK9m6ap1xoR1Edo2HfbAZotUtzwOsZ4A9QLKrbbEua1mazCDMjE5uBqmkTKVsWwvTDNh4a2tX4khMlKlLTIED15Rh6f3ot6_LC3Z1BUkUB2Fiquuqn9HJMyOAO9EcNSoe45FF2I3FO6oUznSiKMd0bPDt4KtyoGdg-_WQEzhnZbl5mioxym0k7ABATUWbaHPB4ky4q0Y9vtdDGsngL5ImSl2ygetxqs_m1xqnhhcMZICQkocIZ0-AF42R8RZB_IA_CHNt129AVeO3n9T7T3A1ja69TnPfk2vL9cDmjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=izSNGAOaPWclTlRZpzpuaZjLWijOWSyB0LbzQ_kMnrgp_OcK9m6ap1xoR1Edo2HfbAZotUtzwOsZ4A9QLKrbbEua1mazCDMjE5uBqmkTKVsWwvTDNh4a2tX4khMlKlLTIED15Rh6f3ot6_LC3Z1BUkUB2Fiquuqn9HJMyOAO9EcNSoe45FF2I3FO6oUznSiKMd0bPDt4KtyoGdg-_WQEzhnZbl5mioxym0k7ABATUWbaHPB4ky4q0Y9vtdDGsngL5ImSl2ygetxqs_m1xqnhhcMZICQkocIZ0-AF42R8RZB_IA_CHNt129AVeO3n9T7T3A1ja69TnPfk2vL9cDmjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi_dq9cEdVMhwlDKsbmCYHpf8_QzTKz645nbWsCx6VBLbi3I65t0VimNMRNfxU-Hovc6_IqHY2ACh7gNUaD6UuY-6fH0H-YDw1uHZqXLh7HZiqjkAf4bfNEBKrNBkBgnJHiyp6yxQmwjx1dgcmRRQDXea5hMJnYaJbFRUpOfYyJqouLnMHzsGSdkOoNota3MYyjKC_4fGKHNm3SBZTb2EpfGZ9k6A2LlM9oHzGl3iLunO8NDlT_MSaq3MH3PSYSePEshewTniYjQtnvXtuRVgM9vgRfMG_MDzXAzPIScN-T0fJwwm37-xP_6JV560TwhINEIw2KzyGr8Kii89QcuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gONZov2I9wvH-d50OiSNXE7a2IkDl-7p-XEzfuOB5jj2v0LlxndeBsd4ZfoRKhcqmI63FEdDXsfDFuD4jmEaYC0GuK0716XG_b_robH9U17YQQiYmRqJxYAyzE2_f5oQrDLFRh0sjfTog4NLiN75D5FN3QcKfwUQuVAufZe3bNPlCB6oZPmVNzqBLgTEZAfCoo29IIzng-hJXypAx4r7gim7Sr9PMH_4_KhKhViHUym3rjUW0XLsxlB84ax9wldMmcDtIpgwO7o9NEUZXQaowx9Y5jHmMKNFAkDn7gmb6_OMgPqhyco4kVDzI-u9y7L9ErhbqCk_eI8aGyO1S1ZPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S73uKdOMN-NaW3YHMUcK07H15TTRU2IRa1VAdIIHIlTA_GcFAgWdHuvgMha5RCMyPOz6jQrI0EZ9ZP2maQOwS0rtf5KtXASP8kMn6ZDgwqdL64fsgNkgjI3ligf6UW-PO-K7MZpkz0nlFURs0ITF6AyTeQ_AZ2BlIPkhIeWMER9XQCRAEQoKiQ696Yre2pa2rvrA39IkAaIFJISf1IFN_q-BnJF2aOZK9Et2YrWvd-bVIGJf_lj6fq7WdUUbE2LNDRltMANJYeHVOJ6TbvVKtZnt-3HRD3FOAYawuNLtxBQGcm5Iaur6Pblqhq0dqNDYUoUQfv-0f0jUZe9g7XMP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=SB0WYOyRti83Z3AvLbAT7FiXRpIKCvBofgp70LGLPVMqagounwT3BjFP2xyl1RSwClBa3WOU1Y4OD7PZJr7UL0rcL_ekZcf8Gi1JI5TVBJkthMW4-MLa6WQC_jhiCgGu0ZRC4-mmaKQHX0SX3Q9jaNOnK2NG2apQTql-u2vFIMqJ_TF36VUG1p3_FDz-wxjzhE1KOxhsJ3D46dFpWUyUZM1JNhSWIsHcxek_KkOr6DTGbGjZRlS_yQCyVsEkXXWixqjY2tfnfRfuKiRUBFF_mU8-K5-LdGqr-FmZv4_EnuGyRVEI1xE6DTeaaCfuiqNtjrDh8ex14B7Xy2rGCrIx_Uk8kYIgQ8pjnNBZq6ASQdc3FOVLjnqLOzOKM3V4czXlCmkjiHA2Kldy36WynxdpDqrNKWeFSyFEZAG0zcj9jECPdq6EIfsThZ8cczMZRaym6eXMBws5GwKbDZpNAY4JRz-4e0dOpvaEZnjKw04-A9wbDfyEbbcwn_pbDH-ZCF4VxXdQTz9Oo0XwfYZM3jhoKqD9S6lbsxFm76JT7YIf9YQyxnmcJWgSxZsPd-QPBw7seu5EwjKANaGUgUuyQfYGaLUj9JY57lPd1eW02KnAq6Au2juZzDD_BwmfYDgiP1oejNF8vB08FHP1WDHQK0KssCMlGeVQaJOhiTP2gG2AEWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=SB0WYOyRti83Z3AvLbAT7FiXRpIKCvBofgp70LGLPVMqagounwT3BjFP2xyl1RSwClBa3WOU1Y4OD7PZJr7UL0rcL_ekZcf8Gi1JI5TVBJkthMW4-MLa6WQC_jhiCgGu0ZRC4-mmaKQHX0SX3Q9jaNOnK2NG2apQTql-u2vFIMqJ_TF36VUG1p3_FDz-wxjzhE1KOxhsJ3D46dFpWUyUZM1JNhSWIsHcxek_KkOr6DTGbGjZRlS_yQCyVsEkXXWixqjY2tfnfRfuKiRUBFF_mU8-K5-LdGqr-FmZv4_EnuGyRVEI1xE6DTeaaCfuiqNtjrDh8ex14B7Xy2rGCrIx_Uk8kYIgQ8pjnNBZq6ASQdc3FOVLjnqLOzOKM3V4czXlCmkjiHA2Kldy36WynxdpDqrNKWeFSyFEZAG0zcj9jECPdq6EIfsThZ8cczMZRaym6eXMBws5GwKbDZpNAY4JRz-4e0dOpvaEZnjKw04-A9wbDfyEbbcwn_pbDH-ZCF4VxXdQTz9Oo0XwfYZM3jhoKqD9S6lbsxFm76JT7YIf9YQyxnmcJWgSxZsPd-QPBw7seu5EwjKANaGUgUuyQfYGaLUj9JY57lPd1eW02KnAq6Au2juZzDD_BwmfYDgiP1oejNF8vB08FHP1WDHQK0KssCMlGeVQaJOhiTP2gG2AEWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi395KIgQxxrMiAB_iDvuz37rf9kVBLT4T4t4EEdC7iBbuE5iUt0K-wYpq4XdZEn3nRbZzYZkeIVsFUOCoCmi-b9-DswM2y2qAeXrBEPlfP-PVQFt76E4nnzzmu42dF805IAXtdMtPcwrh41YRWgSRQPjXMTdox-aUTbByQnvI3W-KFolO6u2BgvF23ubOKzpwIa9YY95Qo6wt7rAEzzB3hufs4EiWnUir_sw6Y-ba4QzULrLZAQvStDMyObQkvAz_eENseGxIB1EfoZvorbVQryOIxdaOsbsGIdQ5hZ00p3e_DNLPpXXa57Ndppmg30QJkc1XQWMYIEToXGozfMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxM9SEcV0Nwq_QgXDvlJzbjZHovbT-Lbhuzz-yKg5dTJD8yBkku-7AiBBUCGF9vBu9PznOrL2gkJ5YpLu01Du1lnRNgNy2JBjeO_3VKyascTBHrhR5KLRT5yNXtXW5KR5O5ytp_KbuBjoOCfF9yTFaGV6eUtK5PCpHgYEjSN-9FvziG6_Og_NFVDCIyFMrhcwu4wdt1YJv2BMUzMxOrnBX9fJ8N2ZFmYOs77wvZHoI-_VKtqie3Ew07fBG3Uj_JoMCggEPdLDfwy691HeQP9SBeOFSwJQtstPfpx7QKtg3jGOdd1ppdXKnKUogW2YOkNSyLqNLas1-KJthMVVHgpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryKhgevOGB1LjMkcav5yqi54c2synW-m7a_ptESbmMhCmn4xFT-BnFdLnNlIOgOKLQhhP__DgL9xGGQ_aUlOkOAVgfeJ-_cOKCZnR5gyncDmSwSN_YPWmrVviwXWyjfyOY3p7gROEWVCFq0YGjYNpoM4blWCIYFwRQbAeH4GVX1l8ZFKKyVO54e6DmbBStlLUxIKc10LmfLObZio4DfsuwIAvlGIwNXAde5sBbcBGNcGlWzrmi64I9mesLNuas7PSuh1Gr578owgRGhI_sBgtmUPofAXFAqvhda8Xy7x-oClcbUd4t7NDzj6qQXL_OgzxfK6aw5HxWQkg6zrGfgqUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=OW96LxC1ENMZOapYi_fWvIPoe4a_hUWReKTpfIfiGSTbhpWJ9oR0nsT3tZk3-BCOI-j6q4hxLuShaOxfvVyfyXFJeUdmMjfX92ZCvXNZ8DSCCGjyG_jYSqApwluSbEIISPng-sy6zHYReamtHYrhlKYiKK4nnt25x_VEKyJvoyKG0ZZ-h4VjV9ob9Qqwv1u-xlc_BYzAQEHDQODqQxlei42w4lCS1aLn4kQtMmQbBsrp-vqehhLqsCniTM2pLBPksjb2QAZ1quIGty3MSFf4FJwiNlj0du6ZmAx3dCts_tW520GbkYB0TB5_-S4q7sWR1sEMy6REH0VXyTmni7wRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=OW96LxC1ENMZOapYi_fWvIPoe4a_hUWReKTpfIfiGSTbhpWJ9oR0nsT3tZk3-BCOI-j6q4hxLuShaOxfvVyfyXFJeUdmMjfX92ZCvXNZ8DSCCGjyG_jYSqApwluSbEIISPng-sy6zHYReamtHYrhlKYiKK4nnt25x_VEKyJvoyKG0ZZ-h4VjV9ob9Qqwv1u-xlc_BYzAQEHDQODqQxlei42w4lCS1aLn4kQtMmQbBsrp-vqehhLqsCniTM2pLBPksjb2QAZ1quIGty3MSFf4FJwiNlj0du6ZmAx3dCts_tW520GbkYB0TB5_-S4q7sWR1sEMy6REH0VXyTmni7wRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tuv7M2bRwyTAlhRvdwK7C8lOt8dExy2Z3duQ-ybVZVuBvLpDVQRyfEfZYfpAiT2SXxHfwqFFZ95VFwAAX_lZJenrvrAk9xse3xmORxeS-BpDtC0Hnv33lU4AekU0e0MottTDOEKzpTTlz9Oth0SZCx_wStGFj8x2rH0UKEU3gLH-kvmvWQcfWwW-Ej50MyUBhdYjUakHP1LdvxIkLihxZbwn7InGKEqt-U5P-IDDKFIaTJx7O-4ZQutyBfZ1Qm8KcqzUT_qL76-62138h0Mdw5A_2Vl0E9B4s-RkSIhiEJ7QObGym0IMiQ5Zzb3xvmiKVYdDdr8wq0w8y24hewf4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itIyRoyTZQ6ng0O9Zc-pJhzt4ErSBKdHyXMmoDzq7SnB-Mh1OM58T6qfmtmqASf0Hl6osIEmcK4vHVydIWaHAYIeJqIj22m0TUT-cY8h_8NayB4IzDZEX_h3W0aF21vyMqXroG71MKqdqy4S2a_ssNbzkYyNRmLaZWnqlf5DdXLuZZFS0yWN7Kye6bbbfoqUpu_5sheaqX_tGdDvhsVZs5DFSEBp26BSexGCUzUrNN9te7Tj_auauEUzFdtKm7jnMThoU6WPBV_4K2hNU0nJ2fAvNnB140uZG-dmO95SUEbDvosj64gV6c6Pr2_tvVSvpxsZBDSgpb9bWjnm2hwcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmG9CgVyfcgqknkymI3t8xP7w1bQP74lCD1Y9vW15A2XwPRk9TmAFa6ZcgbE3M6o5ECBD7A7V7oiqters8rKcxqz-xj9K1STZtyxnWDeodvschoN3TDprZoBi47JvhLTNbRWri8sY9sxKBeLlBG5Aq03mPzuBMejKZtfkTL9u999kI_6r6dIMefiojnck9B9NQC9r3AC8jXMUuc6BRzM1rABFkcCNFrJ_wN17BzsCyETPeWJY53QK6SQl53hpUrfXjKtsDrOuL8RNNag_CB0YRNEmP67BDjMjBkalLvEz6EGismrRDbAydpUPNEt5CDY3d1zE2V2pc0T0qms5g12Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB-rQ3t358p9gFlmt9xuJDZdvGbsqchtdvmDXD2yKNZTQVC79nygmn7CkZprNDKntE6IyitHo-jYUt1WJSoa08XwAl0QEMHQ56p8K3kJ5y1x9k7JF1bL2MywFOt_zurgluPxg3mrxOmRBDuyDax0DjufIoY4OefFNtC2J9Yp8VpSFRjkmFzGJy0nJ7U9lCeDxnhTdrPDzkP0_35CMbCZsqlyhanwHdtxTUlEalvQrSnrJbl-LeX5nbhF9nxifixvcNoVd8-8h-JLzXVqHwrge7AhJs976d5lkH6m06yWOsRZ0X7Q_tRgEpFUJkd7nygCO1DqOGEbJ5XsmX7qbLQsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=PmUf5IvwJ2K0oetf6lc-SSmc1KFNrePkH3kvuzEO50rQ-NrIFAvRtAmkOlStbPeWt7JfOH9EL40PlY6tSZW3qOXuRbCm_VZwJJvRM6PoAe2kKCKaD1hp5yRokc7MJmpy-VXajAyeSy6PWgX1TZeUUXTdSuDAwsw2yQce18lNqhUnggytSPxLjgLLN9udTp5IhlyCc9VlDTf3WfjbW5Og6GBYm01wIlmegHQRIUzjcTpRwKQLcKnoHkccxgLzANHNXL5cM44MpgZS8988VUc5UOGPKNokds8mAwO25NblWGjVyEWy3xQEzJ113MYBU2eyLj6x7bkpN-TzlxBE2yayoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=PmUf5IvwJ2K0oetf6lc-SSmc1KFNrePkH3kvuzEO50rQ-NrIFAvRtAmkOlStbPeWt7JfOH9EL40PlY6tSZW3qOXuRbCm_VZwJJvRM6PoAe2kKCKaD1hp5yRokc7MJmpy-VXajAyeSy6PWgX1TZeUUXTdSuDAwsw2yQce18lNqhUnggytSPxLjgLLN9udTp5IhlyCc9VlDTf3WfjbW5Og6GBYm01wIlmegHQRIUzjcTpRwKQLcKnoHkccxgLzANHNXL5cM44MpgZS8988VUc5UOGPKNokds8mAwO25NblWGjVyEWy3xQEzJ113MYBU2eyLj6x7bkpN-TzlxBE2yayoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZI7g20tPumyP49qmWhtKX4QPtC1UQE-S1qL6JSKYh70ho9jSiJDRtjHUg9ta-GhqDlwOnJbzOTiQRJTjmO2A8tCMrdwDbeCq5WO9yw0d_dBq5Dude5LZWzQ3RUTVgme_IQpalThd-pKVeyAQF5j8DUvFokcI6Ud7uJ7Dr4Y4TW6qqjSV1f5G2ZiPyBZqFtoUmPrxyAkE33Kg9kvr2lH9aSQ36SlulwOt6pr1NiHepi--frAhn_KLlHK-of_jGIEUbgNoBeLzM3kxA0Y4F-z8oxmjTAZ68q0WWZl0QIEBq-jMKMQRRcMvYF4DNY2lOK66DLI0LEgZd_NArKSJeVSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgjzD7cn3R0tOtbO0LvAUQGGPEkrdlQ_pta5kFw3HWfkQSJWpVrBrqH8_VzCZBucmY3MKVBz-umxDPRBUXhfVrac3J4vjqDrB8sz_U-Gc_ZAnkTaH17JfAae5LBhzMXq9LyBX1VNB7jfKwPKRc3-1hC5As2QTvW74ERH4ukFUGzLVDc30m7-obLhtLFQcEP8FqSEBdA1IhK21pvciqHHGiZd19s1J5TfG22Le1Ev2by0VRtL6PoPxSDUmVd7sI_i53bJXrhjgIIMsQlP3r7wEB_-ASYrDKo8eSQBMXR8EpeMw7ZsCwxdMRlK2ZVmDDCqVhtMU835rNGklv6jFnIjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZ8tJxoioFSiugOIWccHNX-Wn0cmxJ_IB1gg-l2aTU5RMtJ8OAZpwIuLNZNZc86c1dkANWvFlMBRpI-rOjv4lYGlElGTmnKaDDy0UPr3drnfzkbubYRZCy8RAT4xA5xkQ-eVNBU0AZUHNnFvzM2vGrYobaZ632ewiTPUUd3XabiV29CfLE569v0EoEt1Kl7U-xxXf_YSJs_A_52aUT-nwngvU74eEdI1w3hEEPrZANDnDurjabJu7GUyYMniOV4jJ7KhkYHu9-NCQaSGWoGd7Aw8RSXbi2dP1GXcyLEgiQYEbpkIXc4sCSNENnbuTylHbMHMNDhOq2CGRKBH5jbutQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEC3BCEY0mslQ95nWOSVONU86-UmuTu6Zk1_9kzH_qWv7TxTHu0xchdNYGI0DgQ3yXT4McccYs1RzkkX1bpfhgDEoGEJigEwIYPJnjVMEyIyKLO76tL5_idoLwpark5PHxytHtWrzZkzk9Rt8NCwv_bTCcMDbXJYimqpQ2KpIickMneLZxatic4IOrovjimas0CVreW2HeGBa7_KoVYQAUSspauPH1yOUd8yvcYmj5fxZkMpBUUpDroUOer4fj5vBuD2hL98lT-epTK9sYG00iKNYTGa0KiLWLyh021SWsGR-iyCQ2dHs3xIXp0YFdH6Sm8KpTNNqjw2kxU-kLYaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOUBfu4fHp1mrtp7On2ZYlMWJ0a0U28WOJgVuDHx2EVM9kr3r5SQcRJPDuaTON7O2dgnTQGK9XBKwawdjh1a-RTjoyD_uIHkBORiUctqQA79XAXrq-pIMzGnjfLrwDpZbdsQqCEawVA9K9GAHk3acpxoactQTvhjOryCTPf13e0_Dk4A-2ms4819n-K2kx1BUwqjGZVxpvv7KD_uYNaXulCb-GtU2S3_15H3L4151r8pMR7PVoE7lp9vqlhnEnhMrwdkQpe2TPQkodftCrrQ7T3BAMAPiHcnhI6LZBDYicjx1gEw_YI9pSvtDr4qhpcAQySbmCDdm8KzEujdheyQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwE0f9dfzUgtDNIMrTt7XnzY9ypaXsmx_l8nVkg4MwwsEfTlYNXZTydNVBxWNiI4yfD1-0vhkjgExkH1w2CI-kZwlE9gK5azCyD4v3Tq6B6ClGEx8ZG2GNrsfaGHeGZqA_cUKg9bjv5duNr-CX6tU-5OT5RS63uEnxejFGh-N7b-jLtlqnVOFy4gJmP2YWaNt7TBSqzCMVGL-kJYGM7gOPsgHJ-M_HPkAiRL5ngRRhmlS9WVCfJR2QGJZUAgx77LG1mXMJRTwO1ooxg3O7vZQaO5JDvJxfQcIv1nANnVd783ej98_EFKXr42ASfdtzpOveUkClJYzlGlf-BZCZ956A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hv_UC9EzB2NJjAOlX3HbSQINtbqj1g58MzZ82MIY4_PY8iHI5QIl9pECELWcbam61fcT3yoGPKIA0VfbEjk26OnZqXUKPcsmXjzVkrd0a6g1_KWYwTJzeGeVn0Aay08cA6FbrHnxW1sovxmNI5_tNTDjCBR-t3nO8YBCMutQddNKNcPSaDwfGbzg8Ct0M7lIKs1wJIWETKYLf_Dpip35VBh2F97BvHJRdWp7XerH5D6HozZRunXj2UEZebbehwQCEjILXXFsST0DlQI-f9YznhVrPznr8FKNSA7OeDsv9ral5u70C3JFY0FCJKHiYuAuy02LwySgMs2Wn_JRc7cGeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFr1a7iSXHMK9WamFELZIIablbcXlSJjOgVb-jH6egTAnZ6FUkTphWv3dRrkgILeaPV-zCQfFdkhiHOmOgc_jOA5YrTdkmYhr-zJeSMrMU59GF7aCOB4pDYPLloZH8T0Ka3YMb8Dv2QaB_zZsl3wdRNafAtpFU-HEUMjYiKz27W1v38CIlCMAHvDp_0kUxfby5qYRlnCX23Ltr5bWOvKBT8-H6fEUpn4hGyKAYX-ZYqbc4QfTNLCFDvibqW2a2IaAh2VOwrDV2XWMNMrB9QhUu529wIB2uCYF2Hw6T6LybJMrg_aE-LIfUS35eOZW5pTpSZXLze9MX9Ku0PIcXPw9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERmRMb2vfNHMQSllmtW9SYLF68NEFDfj-3HyrLefLurmFvkqf84OAyJ939r2qH4GTZvfibeFf8bxz7mze3WKRdGjVkDTuRJYnw4KOI9b3xKfDXkNw2bQQpEicKDrxXhIEOVH8s9Vb4N1kph8Vsw7K87RBZ_rz_3WGALuBOSEhClM7Wk9GawwwdKVxqaAhL2fy9lcy5tBFDGk1yj_wRfEcfgMecU5I5eF_ZZ99kPjWJaXBFLDK9N0SnIoN1aQpq7USlUfkVxqiqbzBAPY9DMtmhyKcd7x0RPj2So7vD7MpSFxyYlyUegqauBF9q5FLDiilNKaMvkdS7j1n_wNcT7SYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtvPKgddJsn50qaKYgsFN4CiodwnJ1vMtt5F05AfrUqUzffG2DNNxKMHCS23wsgSZYHYKFmIWQQu-kxlRr4GoDqrqsXHtffrYXvnDJ_cjFF-5L2_X2-eWao9wIc9ql5Lbq4m9hEnHX1nYNO_8CNqyhq0a_i_XwqkOQ92giNmHzYjNjS1Oeve2EO_nedu60A7DnsrPUwJrPPm5eMIkCkDs36y8iTfAf6OZkr1EuU_rMf_JTIeiJJdu5OjOjIx1MEEfr6DgVtb959QHt8zBucKUMobbxzm9a_8P3-cU-zqABiB4KFDIZZIXWvUyoZJPB_xPWfURWvsV_eKAdoQ3fr-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o340dcLXUMb_XbyGn9Il7dt-vcpzx4LdixjyDd_I5ilJ6GwTpi5eu-e6JyDVA5Bn5-LIW71U0opo9HGb-MiKphHACXjd3UpNAAZNlHrcAfQtzItOnEs5BnlgUfuPgOdIEyHGdivZN2ZjOwnMYa9tB6bJq9wy0tJgCWh05UhCPG3GB2Q53HAMokONvuDPG1VfAlxEIGWQoT9nu8t22F3aGgC_tho5GfIN1tCsTIHDZatIdIJ-eoIixRRq48CEj1KW_kG_-1Ktfq8Qxve0VdH3KEtCHSmJdziVbamb2rjNsO1JuAFLuIZs8EmNNM76A_31TU21qctBp3uE4kRS1PzCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSPKOyFVO-pH-e9CRpMonolnGlRFvqPuThyULkjrUEto9RSHUQiXnWVoEVNHCUc6iFz4mMYB8DLO3LBZQxMvobTly34W6OoU7NCW1DvjyRPOigC1-TkP3LHnKMz7yW5oCelRAN-Pe-drslxQh1S_ilyXlUeKkpKxfMx4KKqq__kj-gQSPxwQLscMfjgiO_pGk1fN80M3UpeZgAymvcOiBGLbrq8j178hQs2d8yHXUL8rWWpNwRMFohcY94Wcd3t0me2SvMqaUXG_PQfFlYxrP81KhESoMhFyrSwxPg-pxFDRMyEEfZ20C-4H_MPh4vk1_QlgZ_xZd5AwDDQibvAZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
