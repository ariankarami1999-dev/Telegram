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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 513K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 08:19:41</div>
<hr>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9kjejOc8yYSY0z2G3b3_Cd1aAZS64_YkrN7hBT2ExGvGf2-ff-FnBegpCy6r9a5Yhn8ewpkUV0Ipnq6AGfnugV6MhCD1B3ToQfmtgyXRLSuZniErvpfaA65NX2FENTZWIFIzzj2MmuRRcv9Dv4Y2W9EgD1zkHLsZ0kJjnyLgKWAxP7j2C8UWjxT50XZrkJ93lh2DqDrmgGn4ZOGC_iihj-yM5Hp6K1hT8aq7nlSRx9_skRoHN4_OgwP8NQbwHYwEPcQPSbkJy6EYNQLwUxDUlTKm9fwzvQqr_Uqu7tNEPDuZseGWT1cU_F-SqNYMPtlhAZDUanUvQa3moH2J6YVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ULDr2bO23KF1n2QecL3EVvh6rn4e0jSxb_2FX6W73GJvkY9e_zl7-Ff6NNyjYzUfKc05t-9JKkWQ-1F8QGmYtgJk5r0B8mJjNp1QSkOgcGp0_rOpYJ86KMneOWp361DzzH7eKCqCknEg3XxDGm4hOkvvYjBsNT3L-fnZ1z5rPCvzc6p-xpRvhzhmWDElC60IM5cvV8ZRFanN9FvJ2ShAnsvisvLO9VrFrffQxXsL0BV8w1EoAGWKZ136ua399U58jgShsB2DCvcl0L1z4x5N-p-ycYs4pm6_v_6tnreG-bfT_n3bI1BXfPL7kZD1E76jg8SfpbAhRxALZ43iFQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDY9e4LlpCO-exEFsAgtv2zINiYALr8NnRhuhSyCVc3qUrqz7mJmk9xY-DKwL6a67zk30PKUKCM0aRP4ecFe5bF4uG7fR0MX0M4qOAnZrC69BmbFIzi1RJNd1EESAmhB5r95RLxpddAXd4Y6J92MjogtPO-avcOixFe_iaHeNzyYKgLFzMemS5WY_8N43WWj_gI8wHNAu78rCkCjFJ8JSR5pzyxvwF0vLsNBSE1jOrDo_VbwhF4L7nM4Zl272Fn8OwBAVYeOKf9ikGg5KCIwsfHhXHfXkkHzevUXihLXwRIayNJ0v-Cv9ckG1sLZw8jJwgktPcK5zCx4lZviCX_GMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=nXt69RZaFTN5rRiO61Q6F6PvyzUsdh7YpDRc4GlOlpHxZq-pkzn5aFlP7o_oA34IL5lZaYswNm5Ryhz3wCU78Hqa3HlJZS6RLurTcrUnnzz3z_20b8aXdgWjh8ltf-dCSgP86GicL8IQu_9_LeVH3ImVyDizISLhyyft-Y9YyE4mdfghi-ZmZLEur-mP-xZf4zwvbs3WDBfRQSanOh6Qc7VFilc9xLiz9cv2adCm1zuhwU1fb39Ppt7eSjSzV28Pd7HTuZ0V1pm4-_nG7o4l8QacTvxphQKELHh8r76NIg0gC8tRpcHkVbtqBHxDKwFMEKy-RpuayqsH2hXu5Y_huQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=nXt69RZaFTN5rRiO61Q6F6PvyzUsdh7YpDRc4GlOlpHxZq-pkzn5aFlP7o_oA34IL5lZaYswNm5Ryhz3wCU78Hqa3HlJZS6RLurTcrUnnzz3z_20b8aXdgWjh8ltf-dCSgP86GicL8IQu_9_LeVH3ImVyDizISLhyyft-Y9YyE4mdfghi-ZmZLEur-mP-xZf4zwvbs3WDBfRQSanOh6Qc7VFilc9xLiz9cv2adCm1zuhwU1fb39Ppt7eSjSzV28Pd7HTuZ0V1pm4-_nG7o4l8QacTvxphQKELHh8r76NIg0gC8tRpcHkVbtqBHxDKwFMEKy-RpuayqsH2hXu5Y_huQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRp0M0fHlwhLVz3iEd5MrgXnb6VfdNVEdn1z-bODn5rDr_olgf2YXQzLR3p-GW4j3yo2HUawZl22mgV9Nr0HJVLgoc9t-06BDRVrJIlpIhjQClFtTn0tjU4YcW3rmLfbXatnR3-pMnGUH4xni0dSZ8H_jQxZ5AtRgbR62sdDHdsTaoan8utitydKYE3do0I2Iz3CAEZZLVIr9PqbmJj-QFlNx75HJ9HmcB56rS3_XWj4V0j2eD2NyGmrDxqprcYiBbXzc3J0MDuMbZpI6lzkcCcQY6yF1Vat03WD9J27bnpINd17kfa3SwZNPVZOnzNp8sQ4AMtWaEt-H0F2Goo2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOh7TKKAdpYcsHC11BjZy1TVaekyqeMBeT_XIzjGzX1h1YiY2xGK8aTpAXusztt6AM5TTcx9D38aio_54DmWTYmNEkl35NkfBCg217vx8FB1ivu9f-foK4JmUWrYsz796hyBdysL5LZhtSvMQKUL5zQKu2i1D8cb9MO9t0uOJ6-hUlendT32aOPTy7m6RRmWVhdCoiTlNire276wdJv3ZfNumvo9nvx5xtMhDcvX4mJjlBGo2QPiYlelz7K_EiDH9Djjh8H7rjDYOC_MfY4VDduWAvc1dfnZPXz0a7HgJxAfubN7lEdyi_smwgqeoaZgGMl6PPpPfGfD6SeBF95szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=qMMjDPYjycDNjCoBQ6N6m0bdqMVjJuEuKgHWFqv9ZWFYA-hAktaTlqM-cvE29EJ-fzPYM1l79lZotPnXLOxeja-zWMb7zMW10gSZmkIaNA6hZgGbOOC33bAl-pG0wIU_Y3MgU41Dx-ZxnbjBEP9if5zubn1VOrHk16Prq4Objj_xpePz5Z_BdYyrKoBAttEZ3HdceRizBx0-8GtTBvIjVjGmNHAjBvMNoBvKyc3PzkbBGHixr1igX-GWplONRUp1YYLNfUWkj3snhoG5aNo2ZtpDh_u-1TO7uWgLFqxZjbW8VxPJ1T9IreevoqB4WukHe8tGFhIW9WdGgOMVAWym-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=qMMjDPYjycDNjCoBQ6N6m0bdqMVjJuEuKgHWFqv9ZWFYA-hAktaTlqM-cvE29EJ-fzPYM1l79lZotPnXLOxeja-zWMb7zMW10gSZmkIaNA6hZgGbOOC33bAl-pG0wIU_Y3MgU41Dx-ZxnbjBEP9if5zubn1VOrHk16Prq4Objj_xpePz5Z_BdYyrKoBAttEZ3HdceRizBx0-8GtTBvIjVjGmNHAjBvMNoBvKyc3PzkbBGHixr1igX-GWplONRUp1YYLNfUWkj3snhoG5aNo2ZtpDh_u-1TO7uWgLFqxZjbW8VxPJ1T9IreevoqB4WukHe8tGFhIW9WdGgOMVAWym-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=sjTBMh0llkLePIYT9NIymQTuB7dXv3sNug3or2M369PhP1ON32GXQZds1qxJnIfffJ4EN44hjk7FpZr1Uj-oHK6UYb0sb8Pk7Hd2yyWMO2ipN_W9seFrzgPpffTOTrAbRv2Ao5uYLmOPhIZF7HpcBZ333vDbZnoH2U6CRMf4_bD6rAbp-xLvuDfoyVPv9KHA7opwllHfxe4_JCHxvFAUhc_H0POiJcZFbXwEYnZBo6YybQP3hKdvxLietoS3ub4yfqdLiYQNQDSxR7_JPTyRF_bd83dSJvH2VEGosskwrKqJvaAGEUGm7gGnn19Kaav3FvAdc_8qQwvVicY9P3UNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=sjTBMh0llkLePIYT9NIymQTuB7dXv3sNug3or2M369PhP1ON32GXQZds1qxJnIfffJ4EN44hjk7FpZr1Uj-oHK6UYb0sb8Pk7Hd2yyWMO2ipN_W9seFrzgPpffTOTrAbRv2Ao5uYLmOPhIZF7HpcBZ333vDbZnoH2U6CRMf4_bD6rAbp-xLvuDfoyVPv9KHA7opwllHfxe4_JCHxvFAUhc_H0POiJcZFbXwEYnZBo6YybQP3hKdvxLietoS3ub4yfqdLiYQNQDSxR7_JPTyRF_bd83dSJvH2VEGosskwrKqJvaAGEUGm7gGnn19Kaav3FvAdc_8qQwvVicY9P3UNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=L-P6u7LZEOVNpvkswGKDM9vHHMi03plrkErfVfoB34HyfhGwxS7NyFL64gFMqeHXk8Hm7Giqdlm67C2QORj_ALkSWkjRj_PA5bbot7llvW_gEpTg8MWJ1r8cuMpCvEluH2Sqd67PGmEnd63I8HeRcrE9gV-7QwinPqx4-YYB9duRd1cwfx02NENxWIEbYDnSMZFduW6Lw6CLwXk7Oglzp0z5nou7Cx8b48c6QzSbF4cnKN2b-PXjariiNdE7kTt_pVyOXlSMBeKFC0y6snMIjnR98FrItK9guOIA2eYUEf-LvJNVCwn3tlSSdqFSx9_IJyZPfbLgqZ2u918nEqj8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=L-P6u7LZEOVNpvkswGKDM9vHHMi03plrkErfVfoB34HyfhGwxS7NyFL64gFMqeHXk8Hm7Giqdlm67C2QORj_ALkSWkjRj_PA5bbot7llvW_gEpTg8MWJ1r8cuMpCvEluH2Sqd67PGmEnd63I8HeRcrE9gV-7QwinPqx4-YYB9duRd1cwfx02NENxWIEbYDnSMZFduW6Lw6CLwXk7Oglzp0z5nou7Cx8b48c6QzSbF4cnKN2b-PXjariiNdE7kTt_pVyOXlSMBeKFC0y6snMIjnR98FrItK9guOIA2eYUEf-LvJNVCwn3tlSSdqFSx9_IJyZPfbLgqZ2u918nEqj8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoQUekpev5A2rNCB0epsMpBhrIGzke-kvppxDhLL8XV1ObfYuvUYdFy_HsfztU9ox8B60sj6p3vk3U9pKbho0sMcCUFQtwWcDmM3qadaxXMl-nz8mXFTiQXJkMYhGn1JcybhEFO57hxyLHvz_neOBZhQMD1tT8YsbxAwZPMuqP2tKmtU0dxo2zpa_l933XDXjTZfR7kdvRyFnFCttMyrnkJl9L9Y5_hM9QmAHDEOZ70cq7Spim4g4-82TTrszr9JOXk9XZSMo7mL_7fYWvSI7unoh6IGAYcDGijU6gevuFyfgRKHtM3WHpvCZqmunNjrzPBGtfq8skol1bOLG3t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtrqpHQs9GHXLuhN19y53ogbx2SEID1iTtQ89mmaNPy2a6z8vNBSnlEbSSe4SW8rm8qfCIfsKsELqJzvYtE7cH4LqpCc-VVo_1q_hy-3c8pD51dB29JW5ZSJHhS6eMFs1cKEa4q5LdSQKBAttGnJV3egq5vy0YUFh9-3vY7cjfPTK_Lb1YcOLfMphr420M-Rv8MM-i1k2K6nIyKWSH_90E4AVVOl4mQ5uSXRV4HyuYEEpyBjPfjxluCUAOPpUqSNVwsdU-grqxqZAVzebxu4m-9gNUNBmsk8eZs6P9Fu5s8nb3jStHVxjT7uvf-RNFVRHxRFcF2aOLd_mDuJT3Nv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqq8Xro5QuI2OwgGP8NndRb-XitoknX7Pqdm_IzfyV26BlLRRIb2O6qI7itNRs9xSxDB0oJm5j3Ptr2yKO7nczh0R3tCltFoIT7AEagKgi_hF28ilTuktmkJTNi7fTQXQv5vLk6TPDDWe5lzprO3PF5unj5QF5IO2OOvScxtoBrBJnU3EnfChs2U7zbjk8L-Y-x0epw4lKRQN0_8kppH1o_p1eLyHBFhH36QX8kxSO08qlrqxcwl3Efdl60pg6TX8ScejpEh-wrVzzJJLABlh6YpBFhERcy1rW4pBJsPsDXhRQWymwRfnx5VMMQaNA7D38McW2epcbQFRVpy-xW6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV4AhkDlgPiOXGh0RpyFFn4TYJU3GRa310afhTpKgDtVHovi4P6rtL_vXKxJr3Wr-6auLugwyLSz5BNMIIXOADqzXTnwOo7aulEOeJ8klXsOOpVMCVoIt9nrPTQaYrpkGvJV1_oJkqFz4vY_wtMdy4l55a9O9Gb4veZ3uenprnnn3zsg-kxsBh7XZ2rmI__71bu5JNURnC0ja5oNpy488MtXVLEC6pcwVnu8Qj_h1peEk08ZlFbcThMLFeOzmS0oV4IQj8ewN6AemPFYjlPH1JXX6fOSzbhFOZEBT9imRLUHBrMpWMdppWltTVOqp7G6NSJU5WmC0t8V702uN2P9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHtT-y_X_cX6PRzTV646UW_0Qwt1t4pnt6_3gqtHwIQ3cqV-WJ2RvSDZfJmm5x79d5_X0l4LxDsHqTpBVpB75-2aVtpXeiIKU0Hxljrkpc67QExG7B035_zHjjyHi-0Hm-PS06xfXnKYUaZcQqd47alAVw9ELnWhOJLhyWn2j_wipNTpZ3hAgE7YLn7laKTEFuo9ngN9djxGtvXrXOwujNVxbJDbVe2gX_K9uDKp-jTbEIQn8jc7sX6PkuOrr9lM76ya4MRN6LoVBkgZVxf5-YiC8Bf-0-u4rqPcdE_YFSJ2xtHmDrVK3JOohaPkFHD-RY30HNCdLbv1GB6IKX_tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaU59IX1nwOdmzjysRtNLV8HW7yc09R04xuAC0tl7FqXKNVL4E4wx5JxfB1vn1f2HdGcdk2w1RDLdB3GsXjjjT19lnmy-tiL4VIPrppiwSL5Oxu4Fd9I_f17SsWXFdpcAysbJKXI7aKttLNPfhMycL9HuXOgdVnbqE_cVYUfjgPwyBMaUQARiBg19x8hxx6ExwHGCdXvNrd0J2ApYhgcxanxKugKr8bSUzKX2weeFFUCVlVlMX04fTs1hwCNJi-0Deq4RelAmIvxmsRbFOXnDman9OOrzpIOHMtRZCsJnFEGqSge2Ht4v6tGJy6zVs3fbhle1ejG4GmXnVnlFbcKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=kI3q8jT79zTzEdaALdaVVYlhVESevH2eZ3Z-uoAGMnaIVYslln3AzBoJJNJVqk4BsOt2XBcKxLroqf3tlHAsbL4HxFRtIiYjN-khrI-64DzLMDwS93Eu3FJGMBwgC5od3gM9GuZ3XD6Zz2TUXxWNBps7C7UATiRRldw7qytvtV75tvXtBaJKIcjxzQW923iWF04VtQ18eiNY-DgPwt-G7cHdcP3T-cK-iFWcPQisMsJh5vEXT_-bhfyckIpM2WXJ4L5aIZeeMpZNDgytQB0ZtNpLcbRKSiaIWws3z5sjkEmnM59fvVSJydXI73sgNx8qtQyWpBYJwrlFLvhqBCvhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=kI3q8jT79zTzEdaALdaVVYlhVESevH2eZ3Z-uoAGMnaIVYslln3AzBoJJNJVqk4BsOt2XBcKxLroqf3tlHAsbL4HxFRtIiYjN-khrI-64DzLMDwS93Eu3FJGMBwgC5od3gM9GuZ3XD6Zz2TUXxWNBps7C7UATiRRldw7qytvtV75tvXtBaJKIcjxzQW923iWF04VtQ18eiNY-DgPwt-G7cHdcP3T-cK-iFWcPQisMsJh5vEXT_-bhfyckIpM2WXJ4L5aIZeeMpZNDgytQB0ZtNpLcbRKSiaIWws3z5sjkEmnM59fvVSJydXI73sgNx8qtQyWpBYJwrlFLvhqBCvhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuYoRbeKAGV_KWH20t-IQ67KYSWGqsPQq9FHxgg2EJJic1mqD8VywvMr32cqbiE8eV-ldE1AY4jVwoCyJagoBPUVqa24qZ1XXXEu71m7tU6qIH9XdfZHD7CoyJSuHMSyzaytfqGZjFp84TK_-l2MsCX3eftDsuauxXOQ61EQu88XcVcxLltQejU-KrhtLe5Z2aH-Sh8RiOVXzc4W9kPGQkGna4l6UGS8Y9-j-iaiphFprctcSGx2xHbbyhFLD7D23-upfhlxm_11ex9eLhUiTwXoLPfwrWxQ0SlDUzR7INnHHsc4YaI4CHDD6xazNIPZ8B3oo-r1V7FE1KWNBfMaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGaMKz92BnP4hYh6pErfXqIjhIf7z3K4mMaxgzhBW1T_0CrHC0JrnlKLMxjMKpyyUvdOROq4r6spZ0XjJfoBxpSpaG5Cm8GRIQva-52a4OE3TKtuaynQXZumT7mVAi5EUcfmYer3krFxu3dZYtiXJ614Yb5GhTZvd3HaqJvcLLIG4tXfhNEICPDjSHH9nRm6LbKeuO4iAxlxGJME3uBTfc2ZN8xLsJ8xjnx8setKv7c6KEymCqReWDgu5SUexHncwXEwFnCDyPA7ejEubcGiuhYbRTOSRL6k-uCtG4PDa_CWXAdgQJlRryGnmQLIJusgt3D__efV0LNq2gYl4Egpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=JXqU0bs6vA6hh4vlVoe1j2yk1a4TH4QNyKtIgw0s45YFRKunRCDnlVX_rSsoletil61PkV336LypsFiP1jnyTsJplVvkVpIsUKMeCSz7GCDzR9baPRdeQmIpbdmq4hAYZyEFNAShjtuUxx3ZCkWH0xxf725unPp7YhkZRpmFBxB7MCyqT3IVltgfeAcTtTn8wNlXZOkLhv0kFVHrOCt36SdQpcoLQWBm5ZHVcLhxSxIlLeBtw3YgmFdP6bQJ2Y8Dl2XveSnzdOUqC8xrNK8pqbmaSJGxs7XaORX2AWU4eKVHa68Z6797Yke6B6a6-ei7BE3KOwIj_-jlgIR0BKs-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=JXqU0bs6vA6hh4vlVoe1j2yk1a4TH4QNyKtIgw0s45YFRKunRCDnlVX_rSsoletil61PkV336LypsFiP1jnyTsJplVvkVpIsUKMeCSz7GCDzR9baPRdeQmIpbdmq4hAYZyEFNAShjtuUxx3ZCkWH0xxf725unPp7YhkZRpmFBxB7MCyqT3IVltgfeAcTtTn8wNlXZOkLhv0kFVHrOCt36SdQpcoLQWBm5ZHVcLhxSxIlLeBtw3YgmFdP6bQJ2Y8Dl2XveSnzdOUqC8xrNK8pqbmaSJGxs7XaORX2AWU4eKVHa68Z6797Yke6B6a6-ei7BE3KOwIj_-jlgIR0BKs-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnnuawTSmKR1Vg6XsFj95d_yJW5ytBqiq68Sb7j6HrRl1ZQzu9Iwf-42ngBZcszpRfm8AOMaWbZSj3_SXRPqrrmxdT8bgsUEfZsP8ymxpEyK3jE1CGiz98kyc8sdUc6N8bCKlq_wcDQH4ja8tWL_qOmfLKH6xclOFafJrd0ZF_1qh5aKp-9oOODEnILFwfOodQ3Yly-iX-_MJHETwDIOtSyBFrQL3pErmfYq1fDOxBYC8TQrIQYQ7tmhahm5002dmoNsDbuTs4eSDXBqTR9M5WtHuWg9nNrNcUBzQ4ZyxhBvVJlREH8r4fCLwqLo25CZdPKv2clh66ECyjY7FrBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD5T5uYx6XUJjL6CWx0aKiX8Q3z4UszT5Qz4iODY1r45kG1GD0ezcjtWo1VQ5uqJ9Qoc9tZh3V89rnj-YsorOLD3B9SDpdojabEK3XLMgzgiz2xb1jj8cJwd2wY8t059sD7nvsg1sOeEMjWnigwQwQJ7ExPPfGcTtuFjKAA6LaYUz70co-qAFNm2Y8qvOahD_YMdGbJ4CtmUNjCmm9Zm3nX-r82sRF0w1JYAB8n16K013Q0zbkXmKf_BEZ4Bl7xWkF6aB97vvkMXXF0DpuBGJVx9NCCqxnMDfsyIxV6ZHKp2EQOCLAUm8N5bywm9mWYWzk4DpA8Vvs3trUbqFBYdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsoUfgiAF75vElDYJNd8KWBiSOfEd5p0Cvokgi8PozQo0yU-Q7CB2cWcEr_LmDQMIQTP3W4M1-wDOM3NDqjs2SdV2Ia8tYFC6VCbZ_5iTrt9tnhvJkjB3ue0pHsiI3QlAipU9i9lejGIEduV97gKjPE8TrtYXSKqSE2wXQU9JH_XCDmLk1OxWm6hxyQlVBl7JMDnXp40nn3Qj9IIblaxSIw4-ksnyv8S9Hvgtps00fFTaatBeUxvvPMxhx2IyOCgDNEt1rPp60854tIAiU8xoF0Su0H_Y2_hf_BN1gQghRwass6yqHWLN_vWaYcGfX6tsqEyHai2ZKwqYFcH9rmYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UskKSOZG_KPtQwf9H3YyWdYzJpDK0qmZZueZlbpuJrQ_u6VHKN0PZ278LeUmwRcmUU7YzQIKpgmMIlUlcsDfgkXcs0iLa_QcR0eCpdLKGJod7OxxoAoQCmVP8hiSYrit-ENq0IfhAUG51FP5DPKjRorCfKCzIb81BLm4rJU8L4-Rgeg5_Fhl2soUT0gccdM4XD4T_av5WvbxEb_HBboQe5xrsWe9BpKqkzxVNRBOxpgGbGbKFaiGefShalUYmsaaKY-qZOLbXtdALX1EtB710m8F2uq6jibQ8o3Y_Pd7lVzpH1-NyKsda2lw-KARRJ2pT_XF-8bUnzLQZoYl5q6EDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tb4pB8G69ARjLW3PP1Vahk4PAKNUDAJlgu1F-JjRVJRsvJEYevRKYkHvKwX-nj4ukV-3ZNmzS2ufsxk8uflm8XaB8nIasJ2Y-Se9kayiFbJ5u4DRBjOInwjAp9B0H_CBGSaUKGsiCevUzrWxMH5TkDpo3HayiyxZlOlU1IcXESc6zLevsEJeCT3xk4WiSTrSz7dklNMnyILVr1HmH278iTP5_DJfxdRE8scFfqXpEQvHcZy6r7eI4l9tGCzhns1QwBra4WiB3_jEY9K4Rcwgqwl0OWwJeIF9WGNUalBO7KTlls3f7OqcuwTyR7zSUS5yC7YJmS8YJ6FjgPaea7f29w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3v777_Jso9xRh8er61uLvpzUhKqKeGXcQ8rgD89w8nkUtOG5iK2eNDT00-uoOFMnEFelbb6RoHcMgwUzX9A0A4SIn69pOBaYy2qa0wE-3kEh7T6Nn-FCXkwPjBPqRuIA_d_rOCVyJli3rYs_r7bogchYNW-r_vccYweZlpixqwZ0_ad4dphQUfZJNfBDcm0OF5JTmYnfwCe5SdT1699Q2FU3R0i40yFGfKbdmXRAMVbh783n9BJ4Vj3ThXf0Wtaoeq2dmVRiUs05SqihSfGSUFxq2hBWQ3-siqIsjOzqXQluS1mSK2X_5dZuSt-ETYPbq7JGW08VP2sI3yaA2jsug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui0yjMm3Zu_G7dypiiDJsg8_6GQ75FHzuwTHQMMhomacq8FgKZY3FvZpqAdLZRVzYGxMJzVktfYWcYXGp3imXZjNMUF-Sx7ICIVWk06MuNAIHeM4SPzySDmuMmcwWlxiurlkZbpZMUG2HpHCy__Pyo972dvVv0PUp6OEk6dsSjD3lCkay-d5Whjeq-R8LtgFl80IaAEl8PH0msZ7wiQg2hbVmEZIrln2WzHqpGdFmMFYcW1Gd4_63HG7LBHeVfZtLJo7_LtxIkwmBUIAF2wtZaDHH09FJsxg1aprS6pL6ehg2fuaUr7xdILIuGNmF0TwMjD1JEA6_OyQIEh_-S4abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faE1UTWfzVRT-YUIB8NhxDVHpFO7zzfMMRg2D2hhioWxfsSg9if5MFl0jeXrGV3D-WGQTaFYZ5qFMO1EEHqFCp4zcemOUaAwexSe_srmLfwiE5xH_U-NjlGMEsnjbjgLp22x1SVKw4kaphVIkiKhl56V3nA2i6wP6UVuuQa_IizjieDjuZcAvVWqFzC4yYTN-s4GJEfdOYWsje46DlmQEPknzwTbVKPfTzmxesHgqVTPfx1y7Hs7hxFILoaOxAmE3S4vSScAkednbp0TmAyLbK1IXzcbTWde2DKi1IbJObs9qfMyWZE2u20xeKIDEVhSEG-TN_EgtD1cbqO7i63anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbqTszGhruKTcBZz6spydkSXn1EGrT2HrBnYAp4ZXlIzK7RWZYh63qZGypaJUCXcQS2dF_csmkj9grrTWUOYepiaJCjEW4jJfOBGo2QjkQJvn63pQAkJngFjscd_1u-bBAdqEGmwsw41omzgXHf7optN-F3KLZlfVNiPKlxIAbyYd00eHAk5dF__X4ZvLjudSyKz5wnwx6ZHWvxpitj7X6bLcJUAF2eyEY0IgH1CeIB_mLHLxfAZtmRDcM0aWUK085gvVRxwBkKQu7UeEGV4oO1q1ICGwX_H0omMbuSl1zG6T2iZOSmtbYRwzNeGUhCYgQTOc-XP0urG_vZ8uumJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=EvQUHJovoEeVt9s_YhP14hNWM7olpxTOyDqeLEvQZHzVAUdvlwtxQbKLr0h8EAqpI4j1k1cOzHdYwAWONTcwL533u8sDsa5l-jfa9-e8nVrOdAsUhPSSwPJ7FKsr5rdt_gLE5c6jTB5sRH08CHgoBNHcnoLs4KeivEKv_A-NS29IKV_GLNPZEcmTeI36e1ibYGSYAcKpDMJtOwv2slBLEalbkwB2FatScD3V4kwpw7SNZmDpagnm0bAZzr2x4oTHKIQQSF5Iix45szyll29-eN9QD8cE94-6JIUdSXblM-zvqRNCHk4EAAizZ25LtUmSdzctg1zrLvoPlvAe-7Khi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=EvQUHJovoEeVt9s_YhP14hNWM7olpxTOyDqeLEvQZHzVAUdvlwtxQbKLr0h8EAqpI4j1k1cOzHdYwAWONTcwL533u8sDsa5l-jfa9-e8nVrOdAsUhPSSwPJ7FKsr5rdt_gLE5c6jTB5sRH08CHgoBNHcnoLs4KeivEKv_A-NS29IKV_GLNPZEcmTeI36e1ibYGSYAcKpDMJtOwv2slBLEalbkwB2FatScD3V4kwpw7SNZmDpagnm0bAZzr2x4oTHKIQQSF5Iix45szyll29-eN9QD8cE94-6JIUdSXblM-zvqRNCHk4EAAizZ25LtUmSdzctg1zrLvoPlvAe-7Khi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALFpusfkqhS16RHYdF-9BX5WjbXwe2FopnxYuKyfbnE-aSh8RIxa1e_IYpPmFgmiSAimEXWW0xq46Lf-CZRLNnenyLisPH_YPqEDiZv4ZGWxsNwjo0quTtz7xmRBHd9yFp1x-ngyyVpCVHkWHA1UtnlAnfn6dBCpAxglA1p5GjTJazvluNbuEGuODsLpwugDRDDSbIjKcOp4FnkuIssvGj0bgRP1mqpYO4JTehiIW_8PYbI6tLAv98E5_MnLSLTR8apWYHOuFgdGZ8zTJDEBlZ9ixO4cquLKPlZO5qjyNJhR68bfA4EBHoYuQBWTRLrRvqZddUxwzYiEJtFsaV6ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=cEuv9crRk7QwiYWOyqdux6KeO7eKSZGND2AvAi1ESq6n4yiS2fgfUWobgUJ0YiE51KYP0eN8eSZyfFid-iTqGvy9Cp84UjVcNeTd0PCdFpN9XhYR9UfHYbWzxKUzYEh9H1EUeHmOTT7gFdXcj94eZdWk_g-tVbLzR22ZqQN4mVI_6yaqwgYp9X4Rr770iX8PFSplC5SQLv1iZE5hWJZFWIAyq_PTerSaAX__L74AQUoPvhPsXO44UX80eGKdyCZqm-twzExgg9ngc8DLiSCyk0R49SPF-HyYbRJsylu1ClwdzO-LTNl3W0U8rlzqFJ6948yIZlfQzVMW1K5EBu6lkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=cEuv9crRk7QwiYWOyqdux6KeO7eKSZGND2AvAi1ESq6n4yiS2fgfUWobgUJ0YiE51KYP0eN8eSZyfFid-iTqGvy9Cp84UjVcNeTd0PCdFpN9XhYR9UfHYbWzxKUzYEh9H1EUeHmOTT7gFdXcj94eZdWk_g-tVbLzR22ZqQN4mVI_6yaqwgYp9X4Rr770iX8PFSplC5SQLv1iZE5hWJZFWIAyq_PTerSaAX__L74AQUoPvhPsXO44UX80eGKdyCZqm-twzExgg9ngc8DLiSCyk0R49SPF-HyYbRJsylu1ClwdzO-LTNl3W0U8rlzqFJ6948yIZlfQzVMW1K5EBu6lkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9pEDN9Zi9HRiIZM2gElDM0ECUpu59RGwwr5IBS6un-ACM6Fxy6F2FQu0uDltJtWBLI4MBCKBb5GZQFB59t-Uoq_AIYmrTnpYEh3edoTIA9SI_Ztv3CzXNgbpVMPR_c91oy_zWxcLUbArhIKeQCgvh6nMvOBBG3UJBt7h3pdRL5E73pNgzlJ-elK2__hSp9amrn5R9es9EGD1tzsEWnwpcRx5u79jGGUf0axMegfGAOP0y9P95CyehxyJD__7LvjHq_CO94Bzr3m2XfxCZUGxSJmSRzNoB0NcsTCrpMJ4UOqgznzHswMMPpaSI6RklXx56AYMZvLxWyChoWTlUCVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=CUhNsuZPBSAIoP5RDLbCVfGHGse8a8lA6-STNq9ZaryTjmIAKabw3ZEV-CjoiBJiO0Qz1obQLwA8j6PLaD-Oqq7oaCiZkmRg053k3cccO1Yz1dbhqOx1N8pMZVyd2wiQusNc-A020GaJCSQcMgWyvseIJoyrWBRpke_d5t84SQAsIjA2PFcx1evqD-fYQC3M_BkmAW8z1vaz6YyANA7cZROLvje-a7-5fA3j4KxI6baxNekuMWJxecJ9UbKNeYkiDd_VtfIBZxMXGD_WXFq04QJKnNnsU-VvpYHJyqD1mMa4gh-iNN9N-Uvj80fnYQg73aRU9mFAhKQYNwErDS0CRlgIG8ktH9YsYJGA7b3tNZ3DprUvu41IXcvwWWzr6LoXOKizhHMEjtK5yrMtAEDsxRAH8uMCdnC4i1x14XItMoyQV4ZyjODt2PrkUieSQO_CnLlh-Hi_doGSKhELebVTgLyJd3sDyf-BpufuxdeY3zcd7Du6x7xV4FzHpUFjo7KNv-2Kf_yqiCyl1U0Kv8ipks6mL3ofUujuPpxqjxd2sTtfs39XTN7EfMCEu9QlWPGW9St2yLWJbyD3AUhn55A6AtVQFdeoHe38gJG4YpE_riBHTiTR_XOZykMqMO2ooc846tOckY7NarHyUv1MmmwoZTidd5vaHRzC5Q-O0dpD2EU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=CUhNsuZPBSAIoP5RDLbCVfGHGse8a8lA6-STNq9ZaryTjmIAKabw3ZEV-CjoiBJiO0Qz1obQLwA8j6PLaD-Oqq7oaCiZkmRg053k3cccO1Yz1dbhqOx1N8pMZVyd2wiQusNc-A020GaJCSQcMgWyvseIJoyrWBRpke_d5t84SQAsIjA2PFcx1evqD-fYQC3M_BkmAW8z1vaz6YyANA7cZROLvje-a7-5fA3j4KxI6baxNekuMWJxecJ9UbKNeYkiDd_VtfIBZxMXGD_WXFq04QJKnNnsU-VvpYHJyqD1mMa4gh-iNN9N-Uvj80fnYQg73aRU9mFAhKQYNwErDS0CRlgIG8ktH9YsYJGA7b3tNZ3DprUvu41IXcvwWWzr6LoXOKizhHMEjtK5yrMtAEDsxRAH8uMCdnC4i1x14XItMoyQV4ZyjODt2PrkUieSQO_CnLlh-Hi_doGSKhELebVTgLyJd3sDyf-BpufuxdeY3zcd7Du6x7xV4FzHpUFjo7KNv-2Kf_yqiCyl1U0Kv8ipks6mL3ofUujuPpxqjxd2sTtfs39XTN7EfMCEu9QlWPGW9St2yLWJbyD3AUhn55A6AtVQFdeoHe38gJG4YpE_riBHTiTR_XOZykMqMO2ooc846tOckY7NarHyUv1MmmwoZTidd5vaHRzC5Q-O0dpD2EU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLH0vlTCtt74XZlVDittRdo8jrrHlQrXzovUKWKPWjBfLLuNtz1dzp7G6FvIj-eb4mzm8goPZxXMJQKAazHrl4iL9wrducLyG-7YFzoFLf0BY7kzWlXyIKDN_I4ravn38yanfoeDtmWVACDLk97E6DkTZRpRiLnUEkgfUS5TSnYhvhQGk6PZAW6egTB4Bsg7xhvPi4tgReSiZP6VEVVz_l3N8knvUZgFUK0VGejJYf8UZdfDJGqO9RVKreEdUjJQ1ApYJp_JxiLymqQ5VvLuBLq53i63GmVY3vcjmHjnRwbFpLC4tOFSRO6SB4NuaYnxydHVRq7LohOVm_1Na2dziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaXOkvTu63fngdcMM_xTQMzbwcsF8ZoF4ivj8Lu9AmKqJ-SVph5PY9bnWtzmccZT7UTMHITnvjTdUB2BFXK3uGdPsTpxnIGAGqqxxCcJ1Dvwsw_zI-QwoziFeBmDhFkVQxkkcKZVTBu6qgNjKI6WvRlaJWydLJT6G0HE4pZGNux7HNz-a7ewKuo9US95NRaml6WoR0hiTRIz3WEpNqwSxNW0K_PCHbW-mP7JfYlAODa-NMzB9RqHRJXwfGVgHrV1yIJJhMob1HrnkXbaHPfCSyi9kfnXhBWlsiQVITe4dFPDLicJ3hZeBH2RQlZjgEuVH9GnDpaMJU7U8QpxQJvEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qErXcoTLANmqxBBWHQpuV3P028prtp6qLYy8zvrSKB7xVgNJwBtFl9el15ny2Agv0HO-e4U2WahZWAQRBxiU810naDWOw6bvLm4TdlcwB-R5uiuewox_J2jVvnP8oyat2FcFq_zWSWeYKMcyyFM72Kg1_SgHQcbskndtz4MSJf7SAigy-CA0IM9VfEqnJMz6cADJE5opsWHZhfldpWI_XVYVC44u_QdSJdBr5Ze_ic3uEupKcXfSRz6fMVU8BtLW56SDK7kTImYDEQpt-V_2JnRtXDCk4_pSTGTBhXfEErx-DFMaVn2CLysdzUWvKdtnVdF9TBGwz7hU9gdf1ZyZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkwZHE4IK-tosQtkmuXrA60s1FoxjccGyT25oTN6VLiGVbvIrs9J3jiHepZ1AyT8rgM3ow3kWKO92XYTqq9D31O9bExB9m_mRYzPjiP1FOi_gdOtTym6r_DQG5Ygg0bYzUalPDpWH5p7gG2xMFUorAXVPQFeEg6GZN-Mbi_jNiR9JdKghwSmzHbgC_f1K0pZtQWLtqpE4pLVAUyiNzTZ-TQQxZ6umv8IBSHvifaP_L1WhlWbOS2GwAF1UEKTHP8dmC_jS9YEqTy4mJjK0U7Lhf33IOhu9JjGbVxwJloWoju1qsPEr6YKFqmojvmQ4K494mdjtpQrcG_s731Ww4HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRjIJ1jphL5cj83AGn2TSXn9blCWyQtRH5ERWFkELLoxXklkZrdbpYYPSF8EAD-Rfr9LeWp1dSv4IDo3uf6D0pFp2DaKgqJQ2Hh3u_IcfUrF_Sp0-bla9c8xp2GIrTYHMVvSvwzOliZpw-fNQrpbP2_eBbcFwNKFYnxNmfE6Z9KKnc0RF-OG7_bYTs2G99hToq5OY2vcyL7LxqyPeLGMQ5rZbU3L3U6T-97fPLd7uukwZp3QQBeYAVSTk97DTUaFM8RR4kwXtcLJt8nzjnEv82AlzDm7EtnPi0uOnzEZJCrWhkQRYprcLkyGdvJu99hTQ9JtHobi5tEpdV2N-BnT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTPdY2MZZtpZL9mt6iY7NYc2GA5RIkhGG5DRwgRrXBCdnwvqgFFPtI_2dINaAh7S3MFwygjex9Wz4vKdkvBM1qizkKEY1roKata5Yt7vR9CtZTtLyiQI6B5Qw9SH4ewBpDXlzIdc-f2Ltcy3zHpXPbVS0kLpY0N0hvBMGbBB715pENz4PrfOhGlomBMs4XnuCo5IZDUjAY4Eieo1VmflPMeKovfmKeq4nWV9Neaa3nRiNiwZrppTxo7EJDzl-fEoOUPCyyHCIISKRLPsJd4xRE4RvJPy1oQTyeMcUE-IQWXmp2GUli09tWVUsuhckO3PIEj7v82w1tXPz2xAxTOa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=sGoB1zBwIsNQ_45Jf2tibZdtgZZqh1gGSN0D09EpStJ5AtItRkgppjhn_PzRl3khn20DIKfOomppSBBK6ejMhxJUWhspUazql8MppEKfWjZnEGjQKV64ige52QBQcpN8Va9xaKkMqEEO2OGsEUMUMN28eu91OVfycHxF6-z9mxUQ4x0nVpdTTpPWdG07rVWIMSBKc3XmOjs54hWW5qlh0MOHkB64aFPFRZZjDTDrRov5frQUjttkisl_Epuvu8qbqZf2dW1-A3Wz5QF6HAffUU0-G3DDVad_GN9H3U_cdR8qsj-GfO5W_ZnV0pshosp1TGD-JCYEtgpjUXZ5In8BWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=sGoB1zBwIsNQ_45Jf2tibZdtgZZqh1gGSN0D09EpStJ5AtItRkgppjhn_PzRl3khn20DIKfOomppSBBK6ejMhxJUWhspUazql8MppEKfWjZnEGjQKV64ige52QBQcpN8Va9xaKkMqEEO2OGsEUMUMN28eu91OVfycHxF6-z9mxUQ4x0nVpdTTpPWdG07rVWIMSBKc3XmOjs54hWW5qlh0MOHkB64aFPFRZZjDTDrRov5frQUjttkisl_Epuvu8qbqZf2dW1-A3Wz5QF6HAffUU0-G3DDVad_GN9H3U_cdR8qsj-GfO5W_ZnV0pshosp1TGD-JCYEtgpjUXZ5In8BWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsbfM7P8BJd_EmsuTar9qeWS3j27Q3oDmCICrKpzCLCwjlUpNnIsR9kzj0b5NxFVcNs1XohH_bqOf8-k6RH2KPL0rmWCa9n7L3DNxqLRr4-tmiODdjzNCfKpiCct3Ao5xXjCNbQV0ipCdRcBOMU6nrhrbNyzoyD6Y_hYdPIfBjuHmZ_IFsQhbIfB_K5Rk7HWN9eDFstsHNA2qF47xHlJiG3sGUCOanyX9OkVC8QILphLowrA-ojfHNEM8e4fhmQvl9piJ4vQrMyLEXWSXmPI1DNJfsn5D9kvlL4LzPm5GTIjb5jsHhC8tqTq8AuTCHC20AL_UPHxOGM7On_QYhG9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=GlfLo-J_Za0UArREadAO0-2ieYPgiztdJrFY-nG2rD2gkNCI3aSIR1xSwB3KCFqUrhwOuoWs39fvQVzuNb-HtpblBoHVFZoaDkDAd1GpLREGfRiNLl84ZbHLj-nw9KmF4uIYf_NyALEYIkOu9ciJY-x9OgqPtoJoM8p5qP6Jf6RJ4AFj3TzYV4aHxWX1pBosLBy9N3I-M5UQsZaMeVhlsUpijbUIerfeRAsJM1uB06_H3_r4WkXs0DRV5nmCf9KFBr2BbarVYhqUQqDvXyDDo7cN0_DSBpQuggvc6tZVzfJ9Dkg8vLPg31OONv4--W19M0pMV0mbe8p41iGLjX5A1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=GlfLo-J_Za0UArREadAO0-2ieYPgiztdJrFY-nG2rD2gkNCI3aSIR1xSwB3KCFqUrhwOuoWs39fvQVzuNb-HtpblBoHVFZoaDkDAd1GpLREGfRiNLl84ZbHLj-nw9KmF4uIYf_NyALEYIkOu9ciJY-x9OgqPtoJoM8p5qP6Jf6RJ4AFj3TzYV4aHxWX1pBosLBy9N3I-M5UQsZaMeVhlsUpijbUIerfeRAsJM1uB06_H3_r4WkXs0DRV5nmCf9KFBr2BbarVYhqUQqDvXyDDo7cN0_DSBpQuggvc6tZVzfJ9Dkg8vLPg31OONv4--W19M0pMV0mbe8p41iGLjX5A1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=sXhwosW7FBE4nqYUK5L4FlH2b8xmV51ug0Rgb9cZRHM6FUu0qklLDx_mEBAAfZz53uMB_nN8wQHzuKVO68ge0s590J4puvF4IiYDTCp6MhWV942-baWdcYEYBDmbBqHHdxQj9HE184EYMalzcMGRWt0EAXcfc5l8aJ2DQ4Z0M_xygbR5wNywnzSvC61nayVY0kN-x9HkUzW0PIXOgHef3QeufR3Nvk7O634DSKI2ZgCz-bmV4pddA0_oXUtRZpTl43wXe_HhOE6AltCnx8DEVIGHiZQlaPlMY0XmFUuEGZm5kDZLb7soUHwkoDScMk4DvWbdVrvsdboGR-x5wc8g6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=sXhwosW7FBE4nqYUK5L4FlH2b8xmV51ug0Rgb9cZRHM6FUu0qklLDx_mEBAAfZz53uMB_nN8wQHzuKVO68ge0s590J4puvF4IiYDTCp6MhWV942-baWdcYEYBDmbBqHHdxQj9HE184EYMalzcMGRWt0EAXcfc5l8aJ2DQ4Z0M_xygbR5wNywnzSvC61nayVY0kN-x9HkUzW0PIXOgHef3QeufR3Nvk7O634DSKI2ZgCz-bmV4pddA0_oXUtRZpTl43wXe_HhOE6AltCnx8DEVIGHiZQlaPlMY0XmFUuEGZm5kDZLb7soUHwkoDScMk4DvWbdVrvsdboGR-x5wc8g6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=ExQRjMadlB7jM75XgbplB-QBgOQtCt7xxJk9rZhKYBoZ4cQcBHzuMvtMJOdBjbPNvQl0lVCOlcbP2qV_0tYKYWyzm-eZ0YAtWsddnWkq-cbpcj3Y5G9Jdd5_heI_1V-xAxNKl3MS_Nx-qHKKuogkly8-ILFodShGWwn4n6g7la_MaJk90Skf5ulMKRkkRoJ1gx_8JAoFsjKxtt9N5ICsiSMBuWqVKVfKbkkMrjgz26W-W5wxlcZ_RdVpJQ59EMAbVplWVI-sdjvKrfmO9ImFEPCFmIgsuCBhjBGzAtjo5eV8Yi8otfdoChA8wEO0hoGnHKPRr4w-e8fLWxC9L485MYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=ExQRjMadlB7jM75XgbplB-QBgOQtCt7xxJk9rZhKYBoZ4cQcBHzuMvtMJOdBjbPNvQl0lVCOlcbP2qV_0tYKYWyzm-eZ0YAtWsddnWkq-cbpcj3Y5G9Jdd5_heI_1V-xAxNKl3MS_Nx-qHKKuogkly8-ILFodShGWwn4n6g7la_MaJk90Skf5ulMKRkkRoJ1gx_8JAoFsjKxtt9N5ICsiSMBuWqVKVfKbkkMrjgz26W-W5wxlcZ_RdVpJQ59EMAbVplWVI-sdjvKrfmO9ImFEPCFmIgsuCBhjBGzAtjo5eV8Yi8otfdoChA8wEO0hoGnHKPRr4w-e8fLWxC9L485MYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqgUwgP03kp-B-z7rsl7fnzHXireyGC_XxGGMRsKiZEC7suHiJGSXRHkv6lKdUghkEY4AqyfnmnbOuCfIiHNZeUkiefXn7bbgPuDO1XhWBwYGkHTJZzdS6w77xBDKOxzVV1RYiz6IOxgqWKTKjdMXsyZ3NOQGi7LQzUh4_NFAwKtJhpAY6xeLIGKAPlkltR432dPT_-X0Ezh_T7iSuV_nk5DaDA0jsJjfV4CpTTP9wVqcMrVLJ8W4dxrdVkJb7O9D-GYKKZHnrFq_OdVsFcalnplDpCbawaVzn0W16p_pV24dXW7QnUCkmb4apvBoGAB7W7OqBpnV6RkB6lgGoOapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fogFcyBio9lUkYThFY2SNKiq4ZT_-Z04ncr_uo2e5aAIsl1QESc9AxileS4L6fx7nSxgwB_seaFboS2SG_0d-ju5R1cbQezneGL-n0b035ye9yGnoLOcSQoOSoOk0kNVA12pzSn6MrtH7lXTQ3R2X6FpXRHHGwgMN7JgEaW7EDxZSLelRBexulY_y-u5Sn-QQsD5YuGCWbm9qVVfGOd1KW0A8E1nbnL4hGg9k-2xtXnmdVt6gG6l65aUWhO6aGqkpPMJ_0D5YicI-vju2irfVZyHUJQXh5onsom_ZiCRWRVUsVFOUnKO8ZfZoDfTeq4zQbj8nAUFfe0q8nCe_-D_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWTP5x2PZ5MPm1QZ7W2xZoyrqAAaaczL1pqrkkxii4zqcDut56F2Qj1jZ4LsumQcaVLjXAEw92NwcukbrxkBE6PblLOnTfkn3xl8dYFIPu3yILyg3UCItBOPYTH068gQ7jJZd5CxKBv99CVNsvBGe9zuahRoB6vERHVra-ShwVaL4rA0f02TNQ24CBJOvM9JltBFgTDShOblCEdsnHNX8kr_6ODHizU6sU_zrD7Ez-1t01qpjlrGIi73Yr3tmLfbRJ6YnYbpMWq4fM3dMcJbEcYqVwYv80toc2WIOd5fE_9kdtWVU5oos7unMtcR-orQKCvDxBJBQTjkWF3-K6-nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZ50GBxrOAub7attGb8wiUBPIyDX91D1cZaqW_JolU1kzQmvN1mtIyDNExCkK2IA38Fb7uBJvxfObmtONIYMLKyW42S91m4lM28WYTOK3obeaCz1p9oZBfuCfF6ekdWElC9pIUomZcnxcRyRxmv62ViPYBaT7bFA83rxuQ2CzvNYiOOGJveY1Ad9SwFOyr4cWkp1XPYz9jZ-9lyeZgTtN2v15O5pXSR8LMM_zzPHdrdWZ1E8KKwo07THTfRGnTGwlMtYXxIVwwqae0-iNufTYJCShRYHdJFoKGd0iWdNur4HJ1ZPLbqbDM2UM_5DxWaSRs27_QfMsKNrDlIujXx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUA1Krx_TXeOcPuThIbtGq7v26kmT7duuzuSpZyAYWq2UMi29ONOj4UkRvdXMy0wjGYblFPtUkShd16Ea8uRLpb1b_LIyLKGwoGz0WHJNmAHRhHBfe6SLd-_POyZbv-ZdDxHcl65hAnpbksHuwCKPpJedJ3fmOF1j2FwjJqmmF5YWngj3n3rt1rFU1q9eSU0vi1S8tU9Mad-ZxHnk68M7K5oLscvvHjj56rjwDCTT8Tx-HpNmgdiiJaF3LkilffRn5X_jdASTlxmQPii4Jzx4crr5ufZSUnBV_lm3HVZXM-V2BEakA6YG-KkCT7GMrjS56JwDGYGTcjO2aoEfQNuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6YAIKT-RPc988efvD5aLAJbVDROvoySyv46pg2QX_4dZXD36EWxxlwwrcbuwfkoloxqj5zhJgfX98MZTZ1Ob2V16WQV2mGmkCpYqiTqQ_vwp1iLX0Pfa8iG5IKXcjuGYzUttpmAWE22L8MwhZKylLCV7zmb53x0We5ZVSkV_RM4lMwuaYH5wAZxT3ldW5L5_zYLJ61t399KJX-NJSn1DmIhq11ENAQdNy1Mw7mbe868VbnnKOZQLjFMTGqKVFokQm18prl6HHhLBFPMOf1roFzjRahAyDYw2TjkPYmgihh_dDNg8A1Azvni4PC8VVDmley2bvPt83gGreLyoH0krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=Ow5hJscQJ0-7JYP2KuIJMN47Vl65hP5xnASsLrWTfIQCs8dulnyusvm13xYn0ym6ObN67Q75iessra8KQTCJMym3j4a8amf1yTeOfH4qGYCA4eHJYlIvPgKR3UUbmL3CZdlHKfGbjLcdNdbmMXKXUoEVclp01bJ1wUZMsSdHFNSweExt3ANj0Z_4CoCYMxbUehilDVxyn7iLwA5apvapT8vLDNmrZrJJ5z6n7ekzYgk15zsCYHp61XAtlWuFF7EtBiefSYnpx5ik1QgEmdU8-sNdh8Tkqb3P3ZBEUso2F0P5CZEXP-MiIxLiH2quDwZIYv1MzoKkn9A4ufCf9HbcBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=Ow5hJscQJ0-7JYP2KuIJMN47Vl65hP5xnASsLrWTfIQCs8dulnyusvm13xYn0ym6ObN67Q75iessra8KQTCJMym3j4a8amf1yTeOfH4qGYCA4eHJYlIvPgKR3UUbmL3CZdlHKfGbjLcdNdbmMXKXUoEVclp01bJ1wUZMsSdHFNSweExt3ANj0Z_4CoCYMxbUehilDVxyn7iLwA5apvapT8vLDNmrZrJJ5z6n7ekzYgk15zsCYHp61XAtlWuFF7EtBiefSYnpx5ik1QgEmdU8-sNdh8Tkqb3P3ZBEUso2F0P5CZEXP-MiIxLiH2quDwZIYv1MzoKkn9A4ufCf9HbcBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=dHOr-jIqZhf_oNa5hjrLUpv11ZlbAaj1xtmbmE7HVa3FxgZYnGmkevdu_JbGaURMugJU0XKJdvNSO248kPB2Zo_G71TN6pDXKpmwUuguBr-QEBG0aRxr4hHCxlbDmFRp89-Lb_Lg9FbQj4a2EIeBJtkrUgz01gr7qruUeutiFau2h3gLV2y0C053S4ylV-6yFSzYoVU7P_J-mXIAGimB-FQwctca4La69SHeL_wZIES9omGyIOvmgpq8BiHTIC-c-suiQJN1yoWEbUAECm27xm9c7mxTu39NTg9HrdU-ry5Om_pFwQp2D6uHez2Iuj_3ntFn9bvQ6DUrTLQyhIDULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=BEjnG1SKUOpp0FMKQznn3m92NPTqg2_GWCifd1LHs93zXZamN1hsXz0qIbZbKKJfkm03CBqpBRAoRj2Ef-yMMwHRWmFaDRqVFgSa8AL7e6C-mJrTWDB-d1sgcWv-rkeDLEEd3N8iGo0QtRnEF2ioKCSR-I_ewGgMb1M1YtrNMBcnFBMSJLK8UFEK42TAynRaiRerw_CmrKLlNPvAMg2_Y3sUQATZw-jS0FK3aaF_NQWyrb6TCNyl_ui_9Q-np7krtWx7KvchLMfzGlqVBwhNOxCZEm606nQXqPSRNBtjlzHFQj40PEYn1H0u09XHzca9Jt-Xm0omvJlK00nJrwBLjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=BEjnG1SKUOpp0FMKQznn3m92NPTqg2_GWCifd1LHs93zXZamN1hsXz0qIbZbKKJfkm03CBqpBRAoRj2Ef-yMMwHRWmFaDRqVFgSa8AL7e6C-mJrTWDB-d1sgcWv-rkeDLEEd3N8iGo0QtRnEF2ioKCSR-I_ewGgMb1M1YtrNMBcnFBMSJLK8UFEK42TAynRaiRerw_CmrKLlNPvAMg2_Y3sUQATZw-jS0FK3aaF_NQWyrb6TCNyl_ui_9Q-np7krtWx7KvchLMfzGlqVBwhNOxCZEm606nQXqPSRNBtjlzHFQj40PEYn1H0u09XHzca9Jt-Xm0omvJlK00nJrwBLjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1c-5FYF0tnKzQFS3ZE9b7JwJLtl-o284VGw2D6PPEN-NvUwL5LdlJLPCRuu42SAkEl0B6hmP3Z0kK5e8TwUEfv9Trbtwqb13UoTaQDtov8pdf-M6QprAghANjzW5w39BolPHdj2kNllXTXBwmA0I4S5Y6qj4BNcLsFv8wVKabRBLygpGVbdP_y9_ccehLeNl71gXAobDvOzToc0uYnMLP4xTaRW950aDCd7Fs9Ew8nq85aXnVESNpBDV22UdOlpMkrId_ceYZEcI7OSfoKm5gEc-XbeCV46KuVBnpr9FUZOepk_VtVBAzaqRyDSrOpeOhkvqx9O0cKlw9C5JbPIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focP4ZvXg9pcI9YNkmkUREW_PthfwYalGfixxZAjvUK8i30dD1NK2pAwhfD1CLTcT0fQ6XvqUfAelGmWqVd7SzMvbiCx0kcgd8jSv-R2WBKI7ld5zXIvF6c3CXUA2hUORWvgx7j-M-GxN-4SaBjWSlm-3vzfom_sVwAR0_FJjPHWhIWv7UXvq01qBkZiPsC0Yu8lkXShecnmvQxSTfSuShIsYVrkVnhD3NdMKEY2cik2qa1CSr2WTpf0TO-Xvdpv8s8MV0QGw6AFqxuRs-hIoKcBhgxv2uY4nDpP2sbcV6meSyZNBFwTNiaBGBjNRKNqx4-9R293QrTPlHzQgANWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH8OZErzAFjZEFkdOTFsBbCd6Q32TP1yMma7_Y3YYEreCTYGRd7abgy8UhZAUCGX8eGR2LFrfwSBpS6lBVHgGSSZRpI1kjD__2vftaEVsqY_MUp3xjNg0aqtJkNm2Bjklm7o_wh77oUPfT9GnI8JVIz4E9gxmsX9DFdQ1HWn6U_xAFbRu3rtDNAleoUhf-ZOzzJsP1jnC4Fw7lIaEGwU8HFc7eCwo4NRBJr5wn_bCj-qDapVJ7Mf3dOozidVS5PIn-9uMJQN1cnFiuSpmZK2erElCtxKGh4HcPdv8UwDtgqVn35LlruHDMpn3mjIV-5DTKvu6sRWzXkFfsAa62qMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rifAuipl0fw8nmhxVmheuniK8JiSUBFNp2WuRSEhL_p2IrtuIxgQbz-3rXJG16HwdRKeXvKTbPBPh4B4VbnKqNeZiSgbJ7f5iJJaBWf8VlT7Myscc1l0XyE9pNb04R7XLbRrHBMOO6FIdNK-IWRBHlqGbZtEAdCP3jhiYOGzG5HtHXWDvGultoCbbeh0g_jtuHFkCyCSWRD7cZ6C33cjpIxfZUIcYN22ek3LLLGx4xRypKfCoYcz7CirK7LVpyR-HqcVzvkeHSD-CDBXjve5ziXrXmEu8bnD2M7r_BVxbvWhjh016FmEE13ADz3LN0R35yN1eYbmSAPyiNAhzq0YhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhM-ElbXC_S1Inm-jezDLMl9EpBRX-JmDCpEXr2_ch7RxkGNJ5GFqWscC_o2pMoqm2XB2a2OZLOnznRUfbSfYnQe6z-L1iiOUk3QKB_C2A1aSEqs8vs_aQpRk2dRlDMcHUkVFa1PlDL_gPvcskdSHt-ijP8lb2bMZXPzjYAp0BCKIHtmpVNrUog9FySNyNyoxyQDKK7rDDOcWrANiZ8-VfzVKo8Lghp565gTHT2j7GOBgLf6ZPSRj6zuAzlTJRaEQNGfwqTLQ-GUkfJGy0NpMxaa4aBVoElHN8OJJKwHYODaPkVcX1VxlOIsoYWtE3aAT89v7VCqatuMF9jj1DhIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvGWCx6dPjqUuT_DH_3KdwDolMhRS0YrnjYyiMJpcNFzHmXvnvVaVaKiaxclCWVkPBxwCXkkvHnvMAj5DlFmWWjP-AmZwM0IdKP8FSivnzWm1EeM66G5iJJwARRdXwZ-Rpsr6UEMIqnMufxGFDtuyulBV0PcT1j-VVtgWruRE0fmBP7EYLmzIP8OLH7k4THCPnpgS8KEEjnF0z0QEl4GO8m4zdAH0jlTnb1x0fnBtC3hSq-1K8P91cpY3YMDAroUg7-saGMHCBqKjOu6sUw-7mT0SMQ33yolQKUtbz3sr9cPfQUeZ9AimqrPd-kYS0qZjo6DVPFvZ7g9zVpfpCduDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2wwm5hFLgYAgPqc-e8dUPJiHUYf9Dy0S1DXMR0vOBliRvGW7IYZHw5UHoFKROAB8vh6HRjiES2siHj1MFPkYaPfsxNFXp5VEX1qrnx-WPAOxdkyt_-Oe6vjEHwHbnCQG_a9x17akp1gD79x7JVWM6T_MItoHc-W03c9wM3-HpoUIibQ4IOegtvIXPPauQWraFR0yMz77bRlizGIfiPLYgVkfRK7PjyJesEFrZ29SiimXs1fABfFhxOvxHY1pUvVNWmgkUgVXo1qMT8Mzl3kkvElsDkFTXOkqUxlyzalyHUzOj-yBkwD3f5df8KpfAJL4rrJTn7eHpf8dGIZ8yVeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNg0sJhmfBFz9gLBNqfeE8G-YfIpdXDka5pewccW0OjBpvOaLsORZrKpu5tGCXaUfpspPTLo0QLJ7mgvBgnPicz9D1ICp1p5FN5nbySYvmTEWLWXSA8YubdOykW_v2FDIMOI5X8lYKK37wYqvoKLsbX2xWo5LypkoTqOJt3ex9mwbFm-JyHWa0mghvtmuYl6W2jfaRPjKZyoWZY_3HrF9Q4JkhsBSQheNFhUEL1bEFoTPo3gOrDjGv4vXFPdOSfcCKUH-Sr58t_ZAlafAmrLu6Z7hALns_q_gsYdlRsrLmZhcsic7er5Cm684MR8a1AEBwMInt5aHms_sM2UxdsQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttDMoD01tYM5BGFQ8nVqa7DNfKqEJMxt6x58Wtr-g0GrpYAHM92lPmdU7LSY8kD3uyUO44iseIZqwQxij9TWc766YAcFzvOe8jYEpkNKN3g-XdqhZQsU259B7-nuKo3TKSV-uSfTPoDqIGFuPNM6XTYa7D1oJKY74W1Kr5Cqsp7NGFJVAwG2D9c0iAg6fJpGuhuT8LndpMZ6tPPhPoCOoZQunfioShJ12HxqpiWACsuKuMvQi94a59g-nLcvvRtt0G-50mjZKgI4--jRGtILe6_ZhgBp9_UApU5ZPiWqEj2xf9uo7eUQOgpuaNeus-EU6Tf2w_lQ3Q32p8s6J_UaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=deFEEnhtv76dzFYiSIVgUG3La6CFWtrovq-jBXfRF5UzVkc5naozMewuaMhr347JU4hmc0gKVhUM-caCkWw8uDbQf74sCnJD5HvGnfhuZKWGrAgdROY3kpWLVwvaSbtXzMIypZi2IYF5e9Jp_-6fnWl7oP5UbaN7sNa_AS1N5s1d5nDCDXwTE1j5jvQfXdOI95PwGm-YoRtuMqSrDSu0TX7dwHtY9WHZhPtz6qCWS7Ftz1G9t8OiOKavCGQVkn_deFIfq0we_678t_imVpTuZ7kOnjdYJiJhSi9AKHuwHTnA23DnexgVHHy77b3nDVmZulpIrBnzRVUgmQNfjVMPaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=deFEEnhtv76dzFYiSIVgUG3La6CFWtrovq-jBXfRF5UzVkc5naozMewuaMhr347JU4hmc0gKVhUM-caCkWw8uDbQf74sCnJD5HvGnfhuZKWGrAgdROY3kpWLVwvaSbtXzMIypZi2IYF5e9Jp_-6fnWl7oP5UbaN7sNa_AS1N5s1d5nDCDXwTE1j5jvQfXdOI95PwGm-YoRtuMqSrDSu0TX7dwHtY9WHZhPtz6qCWS7Ftz1G9t8OiOKavCGQVkn_deFIfq0we_678t_imVpTuZ7kOnjdYJiJhSi9AKHuwHTnA23DnexgVHHy77b3nDVmZulpIrBnzRVUgmQNfjVMPaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=U4ZIIWTr0pkaKCNFauXXqU9WCn9afEoMU5OKbV-31IiUNPKm3ue2bZjfGsroTB2NhPVBYbl10YaHT3aVRPHOxpnnSx6syeVNKhmhjgUOYR9vKu_yPVBRmgA8MPb_iZczVeqkoRp4Qm9o0LEtUxHquhSU-y0_7WqaJQaWc9RGELaj_MjbT9dGSZgsQX9qoNUDhJkWzjsco4se8e8e5ptU7ntJREZddPpqaCcwf5PXPqsaCUO9VVYCkcHpMUmB2CI7nz01_ANHvzCzNx6Vc0GxtOx6Sw7VO81A9EakTtCdwiJhys1xnexqJCCLv-mmN1mSaDnNEFtBF4UkrUr3R4_h6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=U4ZIIWTr0pkaKCNFauXXqU9WCn9afEoMU5OKbV-31IiUNPKm3ue2bZjfGsroTB2NhPVBYbl10YaHT3aVRPHOxpnnSx6syeVNKhmhjgUOYR9vKu_yPVBRmgA8MPb_iZczVeqkoRp4Qm9o0LEtUxHquhSU-y0_7WqaJQaWc9RGELaj_MjbT9dGSZgsQX9qoNUDhJkWzjsco4se8e8e5ptU7ntJREZddPpqaCcwf5PXPqsaCUO9VVYCkcHpMUmB2CI7nz01_ANHvzCzNx6Vc0GxtOx6Sw7VO81A9EakTtCdwiJhys1xnexqJCCLv-mmN1mSaDnNEFtBF4UkrUr3R4_h6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz13YK0W_RND1ibdaYxk9OXe325ugznQPkyjkNim_hbZwjaYhcSmtS4fcTZU8cSllfodGoUxgqImu5VBfOl6UB2Aa5TM5dGrAdAqIovbtLSsxFNuLsEKeZD7peVVztRrLoaQ3wbKGl69SxsqgErI03iNxSgGqsPn7M-OypWdSB8VzW0fg2K7ms31skCCDzFbXVvtljrUEXT0boVzYSi-msvlMn0IGX5fEThOQLQGii_1Q-0LX6k3Gpie-E2MX_nHn-FIE3X6HShh5Gg5UdSRHuALIRP_Wddw793lSM_Aviv0Xaj_LKY46pMjOwIZPcFM9lJJUGJmIfX_9UdUID8oZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=Iau8eDmvLyqEmlSPmXE0RMTuc6JvcmKOdUvfgmuFXEixAW8WYLgrz02Ap03GlgfqVwgYgOJ7ORnuj-_4hx5Q8aiqaOptL-t02lWr-ZdRYuEXYC5J_D_74dhmYtJPsHseQwbttBlmEo0A5jdIO_uL2Mq0We5pSEpzUTsdbsLisAPiMogh8XaFQTzntJNXB3yY84bAm3OVduqG2QrdY1eJ-pYDlo360dFmhUVIB3g1D-ckgP7yaecsqRs9BdDsnqtBMEtlL_VRjO8NdC2cU_YqjE7M3_zw6MpnxPqry8Btiak6FqPtkG9rYJt1czZE_w7JHnoPVkDX7n8IJoelcV4x2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=Iau8eDmvLyqEmlSPmXE0RMTuc6JvcmKOdUvfgmuFXEixAW8WYLgrz02Ap03GlgfqVwgYgOJ7ORnuj-_4hx5Q8aiqaOptL-t02lWr-ZdRYuEXYC5J_D_74dhmYtJPsHseQwbttBlmEo0A5jdIO_uL2Mq0We5pSEpzUTsdbsLisAPiMogh8XaFQTzntJNXB3yY84bAm3OVduqG2QrdY1eJ-pYDlo360dFmhUVIB3g1D-ckgP7yaecsqRs9BdDsnqtBMEtlL_VRjO8NdC2cU_YqjE7M3_zw6MpnxPqry8Btiak6FqPtkG9rYJt1czZE_w7JHnoPVkDX7n8IJoelcV4x2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsdRP8tkDVFtvVDTlAFT6aX118AvcUZulgCKUHrY40S48_eX6xKGdr0QO4U5UJYWdahu_BzygpJ0l2BDsz4_Gmaa-wmU8Y4oHJ5rXqJ-l6HyQFvx3IrKGvWNvprzJ4JeMMTqGGO1HZ2hYcTWunLXcmTXF_zdPqVMkXZPq1G1PhRAawM7RBnZjHH_rEFDUnsNdJgb51AEf0lUwYHJCP8F27K9mVaTTKvisRVZTBm19u2K3YqNcxa9DGQpGk5xbfJDWoGYptRhb6VKOsweAX3xV-fymIJdGxPF6HNN8-6nMUMjRSL42fekbCwM8uzFvuoc6KgbsUnxy8ktvuvjH3Azxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=sK-xub_80cHUmsFnw5WVt9GAa6np3iFFGZ_GKEUuNk6DMIXDcgPVsYrg1DsCwNvrxwlpK0555kdSQrSqpkDwjcAIAMYx3rksoROCJ1pygWPaKmc7sTbrl1cCusuqSvayA2b588RLxxQ0zCnDLO8N2J2d5S-JRT5ydVQ6pqwZ7t1Ts38Pdg4M8SNLFs0-kCHroTvY4y6fadhHH1C3ZJfD4alQ9iOj7PnKBARSHyZ17rRIX2GaLsmHjUPjvG4FuIWxEzPyyYE8ah7UiZxPjnYB82jALO-Qx8rSBJKXJKryxHixVc8NjkrdT9I3Vz2FKP1rC3wXC1KWNc9dE4I4RijJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=sK-xub_80cHUmsFnw5WVt9GAa6np3iFFGZ_GKEUuNk6DMIXDcgPVsYrg1DsCwNvrxwlpK0555kdSQrSqpkDwjcAIAMYx3rksoROCJ1pygWPaKmc7sTbrl1cCusuqSvayA2b588RLxxQ0zCnDLO8N2J2d5S-JRT5ydVQ6pqwZ7t1Ts38Pdg4M8SNLFs0-kCHroTvY4y6fadhHH1C3ZJfD4alQ9iOj7PnKBARSHyZ17rRIX2GaLsmHjUPjvG4FuIWxEzPyyYE8ah7UiZxPjnYB82jALO-Qx8rSBJKXJKryxHixVc8NjkrdT9I3Vz2FKP1rC3wXC1KWNc9dE4I4RijJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=fPRi_oUDj1J8aUukdzHhXysn5NLcQTbl9sLG9saKOD-XC3SsC3jjwQ0g2U83xK4s6jfyJh2lWhyniqNc0gXzkyjc0eFK1yCUsAbMVTCBQalEKSU596UowW2FwZmVFxNf0VeaqycG7-rBfQNadrzihOsl4HPqXToB-x_0ohmxShlV3oMOYgu1SSUDsZ23FKyGOQdBF7HwVrhbga4W1ZN_K8CqKYzOAtYqZg6BtP5AYOBwEHWdXi0zxMDRyh0b0r34ou1y1CJFJLRYnMgg_ZX_INAVGncDcI0TR7PZJ5O0Qv0Lz8VGqgW_a4LloJO1Zt9F6jwtMyiVyE2jL_kr2As8rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=fPRi_oUDj1J8aUukdzHhXysn5NLcQTbl9sLG9saKOD-XC3SsC3jjwQ0g2U83xK4s6jfyJh2lWhyniqNc0gXzkyjc0eFK1yCUsAbMVTCBQalEKSU596UowW2FwZmVFxNf0VeaqycG7-rBfQNadrzihOsl4HPqXToB-x_0ohmxShlV3oMOYgu1SSUDsZ23FKyGOQdBF7HwVrhbga4W1ZN_K8CqKYzOAtYqZg6BtP5AYOBwEHWdXi0zxMDRyh0b0r34ou1y1CJFJLRYnMgg_ZX_INAVGncDcI0TR7PZJ5O0Qv0Lz8VGqgW_a4LloJO1Zt9F6jwtMyiVyE2jL_kr2As8rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrsABYGCvOe24fNIoWbWQ4w0Fi3LsOWXl930cF2aBdy6IVFHOW3z5PPYkSYc3Spl-nw-YtdzGfFwE2QVqQVz7S6LWWjjsNnV9efeW_pHkNsBm-toyBdq4I9FfwFAkqQYGXRqF26p2N4eCs6DQtLNU8k8PvlA71llaflYCunOnE5rjrS-wwIQ-gFPNbN896cNo9huka3L-GrkRelU6fWP4DNDKh4Bdju07XM5jaIXpx3LLKOyR6j3ooUi9f4X9ujAwxF-9kPmE_nka3OzGadBGVGz5JuuSxD7I0v3yaX7G5QGbvxqMpyoa2mrIskGxvxPZmQ4AKNEjwY656U_AvE-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oaLbc7NMwNhhCq7jBr3-vDsXkur8s9Jkk1vGnOU5nc9vwKUsqMTP0nckdNXwpPN_n5XrTBkdZOP1z6cwB3ww_B437_g-Vo1d_uQa-DQcSvY7cAb45UzxvxUxUNWSEAehsSm6VHZNo0spCROgVX88s94ITvH09oTSUz1Yxv3jchWswNQrKx6t1_78TOtvbapPYfYA7LSbGmTZLXln2BNSdhe5NUYfnPFdExeir7ZM2s_8nJJftjZFziXN8YpsHHErfNTjR2DjHmtoyWDy5vvGbk7F3HYQn0ATHKti43i5SGSeVz64rMPak8ypJfMhn29elDjn77RO4msaMD3LU6_bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EworTxeHLIgVIl096tC4fQEx3GpVu50-2LSszhc0u-TiyB2-Av8QLYkklZcPBjveZpOEULSqvYVCdHeZl8ectwFkVKBJdhgNa8r4o0y81FKVcaoSer7h8cJ5cM7YI3VaBRSirM2Cg357V0Ft8EL24-h4Ge3AoJEtXqpEyON10x47D0FxYnc5bfJ__aPFaUX4A7dYJFLWJcsRjjiww-pPSIQezyTvoyD9iSZ0yCM2fPKegt7Pd--A0H2BnVyec1e43WV1TnifYjWOfKNqNR6LbwVDTs82yWY1Vw7GYk43dENwA3B6M2i2QHcHjc-4gc1Ev03lMWGKtrnbBXAQ6F1wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFOaIDJj85yLg2eNKcQ-tjPN2gxSr7y8sdESZLQtIj7mgilNryJZQ35upTOhv7-K2Z7doNYx-mtAyM65D2o9rO7LyQS9ZfeMNDj6UxkxqpYdzqZ_Q2qK6xo4K1d-PIqFITrxAQgIpoxNavCkkBj2Ldey2qDSumM_SBicJmnzC4CezTQleWq1_OmblW-vRN1jzH-9ojr4e_F3QuYPofeMk0J8Pt0i4X5-Mp927MzlEMQcvONHdIrPBTKZpQgAlzfX1jEezlBqvJOPL094Ag-jGl-XyitSvb651UaS37ELrJuSMQdjMlFD28UPRbi11cPWeggGsDo06hxn4LMvmCl1ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5rj3goSUHMl8bdfttKQhQuwyuPn7GtZPTt0GwFUXY8K4WPe9wkyOIiv9uaF9xi7T-ctT_mrKVUrpP9mTLXBJEvTzeJFHx6dP3erdv_MBa4fOSSHH412ji7i8GCsi9b5CwoST8R8p4lFBoxiQWIlT9vTbJH6UEbNe5W4IIQhb38c-fiHY-LbEwv6yhmE39sZq1i_g6ammP35NbdzhA9DF92F0gKP8ksMBwIUER8os-BAzQAuoYcsq9RWfaUnQ7ofuZZ6Z4yql3rkU2BgDKGtua-pWogHMpYxOn31XSZ10xPUxPJVIXu9LafC0wpDcRHZSwQpSb-Z-INAX4cUhMV2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4n8TI_TWNsMUB_h3eZLaARh2OvBRrx4AzyNEzkHcJUbJamBsgYjtdg-EznqFeRmQJRrcQe6R8Xs6VbafK-92fK_Kc-oN7rFAa0lX5CoQQ9Q3nzujL80mvs3cmmtE-F7mzeJF1McIhQComBj8viVZ1-x9Gq5NMA_jw54xI0I0mGnQ3o-J3aTbjeLw3VEWl_sKcRJqkh7Cs7rr6YJm9YvpNbXcYzmzj4mZwYGcGuvRX-WNsv3LXYD9AJA8T0FHQIv18cf1uOhxtT_apvk9-KJ_bakbuXKfWMjypw3HA3B4_5DQM2hNscQEwAgKR0VSVTJwGSZR9BEaP9LZnqA7fL9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=D_1J1CT7JEQsXlfUchW-k1q1rePBLb-QXXRfVgy9z8ZyhgKxiu09l-1VnzYGlz-QGn_CDJ644mHW-Pb5EUdZ_aAoU8ZzkN2cT3rnUyERYnjDpBtVtsZburJdjBhgBQgtjkpSXO_F6BjmA3nGRX6zLaFzdGH5QgMsaOiSFf3Kv1XHgXH1OTtcD0KksO4Pn2GE821-mh3302r4NbjLazgbULtZEHL95d5mcy__5fApfihF4zU-714hPxVeMZjJ4gSSPE8axoitJ0UbE1RadGRTeo_K6FjsrfhK_djeriElCTEyS6rpi4t2kk5mPpJ3zKgxkL75qgs8AhcP_o4hBKIS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=D_1J1CT7JEQsXlfUchW-k1q1rePBLb-QXXRfVgy9z8ZyhgKxiu09l-1VnzYGlz-QGn_CDJ644mHW-Pb5EUdZ_aAoU8ZzkN2cT3rnUyERYnjDpBtVtsZburJdjBhgBQgtjkpSXO_F6BjmA3nGRX6zLaFzdGH5QgMsaOiSFf3Kv1XHgXH1OTtcD0KksO4Pn2GE821-mh3302r4NbjLazgbULtZEHL95d5mcy__5fApfihF4zU-714hPxVeMZjJ4gSSPE8axoitJ0UbE1RadGRTeo_K6FjsrfhK_djeriElCTEyS6rpi4t2kk5mPpJ3zKgxkL75qgs8AhcP_o4hBKIS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNFLV3Uxjfov4DJutepoF0kFZ5L5pXnQ642mgb_zU_A_Z0NhxdHCIY_ZM9y4dCUITGJnc9QEyFbK5am62oGRTH0UjLYS29k4SF6vmAA3CcP8ynmxmGZz155RFbJ_en_O5v65AyugmYFCTI2y9LUh3bUy5Aq62c1wvNIbo-tSZBroQpqS0ld6JMf7qWu7CemxL5ub2yUNw7djzBP9INyDYhFeMjKwOHydSov1s3zusXSt-tpA49tA72K75umDrgFzyLXj0J8bQztl3EIJrDOjBk6K8DbE9iOMdZ7KEjap2fYrkoshrOLazO9kXOsDxO2_RgPeskOIHRaw0qhl_KRN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdvXtGelpDT6xP1PpM1VZSXSQbpIL5bicFSXxzRSBGcNfz4l6lnuJtevgR-4Jw-xBHsvEu2uJLQo-GbxWxI0SofQfPNYH23mmZKj_9y2Ni7aNds1dpLlf3EvjExpXEgD2zjotVNamQGCTvi-cHq0QJ0JH4GvIs82zoDj5uhXw8ZpBst1PWUdzrtVFLp_RDsdOMCzInKA8h1YfEvvi6oHs_OUKoYcv1G3_HhjVt8PQ-yv-ctLi_7XrfSEyhQYeiJi6ySAi-BZJsmaniD-zvNTpjM4YWvlJ76Ai2X6YQBEh34cQlwj3azch1o7r_zEMOv1QGbmX3vXWNZxVef2yGjIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkmFCLtrtC9tHoTRTVD18bfHIqO5o1cia4twVkSYpo6y3eTiYBeK8la_t8asM8Q7mxLPvHf9nx7ggayDE7cpzqqHW1qmgMQ7uhnor3aQHS-QnTtX9KGcQDovUk2oPkbifyWLcst-TCzAHgbF4vTjcq7eCl62LkC2R6nOuSHGbTqJJinaQ3bkYekYo7GiNidg-jfo3dE-12TaJpNdgEwpinj-9bzHHM2_rDGgcXu6z1kZDcVNg2_hqeNFZO26dNeXtlvAT07EV9ao2ClTkRhniyVK5gG3fwQ_VdX2ZKx5ymnGIGvYoLVT-TbJjQohtP11J-HkynI1eRaJi2bCHFKtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=kCNEuR53f_irjmKP0w_rvb0Kf5TMX5zVVtx1b4awOt8DoGAozXoLGWGxvDBRQA3S36EnW7eBJmViz6NM1PuznROrsMcMZaeKyOnPaWHg5EEkFm_KvPMZVHYXJHZhxPcyqOGttMrguTU5Wr0SA3OfyUMh_vrUHKpPQ_kRVON-c7EnRb7x_dAQR2iN6bngCNQ_csUyHnkTqCVC5NkM10LJBE5NbuM8IZOXcb13a5KYJL2U9vT_oAFHRepqqD_UwHTWpp1KRlGa6npvm4XiNhQ5nvLB0QfjBiDeNFR-YOZaaruF0Bstv5KUNM5H4MdFO9MOJ33T5NX2L6OKmBekRicDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=kCNEuR53f_irjmKP0w_rvb0Kf5TMX5zVVtx1b4awOt8DoGAozXoLGWGxvDBRQA3S36EnW7eBJmViz6NM1PuznROrsMcMZaeKyOnPaWHg5EEkFm_KvPMZVHYXJHZhxPcyqOGttMrguTU5Wr0SA3OfyUMh_vrUHKpPQ_kRVON-c7EnRb7x_dAQR2iN6bngCNQ_csUyHnkTqCVC5NkM10LJBE5NbuM8IZOXcb13a5KYJL2U9vT_oAFHRepqqD_UwHTWpp1KRlGa6npvm4XiNhQ5nvLB0QfjBiDeNFR-YOZaaruF0Bstv5KUNM5H4MdFO9MOJ33T5NX2L6OKmBekRicDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grrQjNPsBiX-OnUpiHA76NclLMySzrSXAtBSaZMpixqPdGBgpP_YQQHM45wOF-1he_Ihe5eWOW2Wd6rV7BmP8CFIgAQo-YO_GYOQxIR0ZVOLteKrL13Fzm-dJ7ehbHcvVvjjbSKG2AUT4-gfWTmBccI5cuNHxrLaAMoW38RHU-T1epfOsR6yfkO3gU6XAvEoAkcmTfOEICLseVI1fGRT16Oeq_8pqAsMlzwQ94FWgXUv5R5KutxBndB21Eq-Qbgs51Ocrz6vxE4sLG3SpeN2VDCftxotL1P29KRGxtuM_xRcVyxhb9HH3BDL17AT8tKbh5yiTY0S2M9MxUG7V7HOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=bzqr-8TyjbliDBzIHRZoGA592i8MpbcNyVzhBCLOV7M-hOgnxlbELbyDAc55UMwwhm2Pom_zj6xwCutxqxGVUeR2pnIa9Wl3KzhJzKhDb1koAF-1npezlANAfeXIQOkUtwlRP1I1bFcCoVx1SNb6vRMIGkB_SZ9jSvPOBKSx_OJax4WkE0jEB-BL5vl9tF6iJewP255R19HmuYFhRCd48_FM23-6nl0jfTRlkGfUQmv9BR-sz50unMkvbbwrBJHH_IQJLqC_LtzErcgZp5psnCRMymvdONE_iClb6-K_widhoI2JaD39cAsa6YEF4UmDGlQDqwbB_VIVW2vmd4h4sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=bzqr-8TyjbliDBzIHRZoGA592i8MpbcNyVzhBCLOV7M-hOgnxlbELbyDAc55UMwwhm2Pom_zj6xwCutxqxGVUeR2pnIa9Wl3KzhJzKhDb1koAF-1npezlANAfeXIQOkUtwlRP1I1bFcCoVx1SNb6vRMIGkB_SZ9jSvPOBKSx_OJax4WkE0jEB-BL5vl9tF6iJewP255R19HmuYFhRCd48_FM23-6nl0jfTRlkGfUQmv9BR-sz50unMkvbbwrBJHH_IQJLqC_LtzErcgZp5psnCRMymvdONE_iClb6-K_widhoI2JaD39cAsa6YEF4UmDGlQDqwbB_VIVW2vmd4h4sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8NkLRYczWthmJbFHd05vBCN8xnVgMKyLzZHc3pjws6eG151k16lSZgfbnx2uto9fTACUtCXtxK5pUoOjYpW9p9qk8Z8CeJWorLILEnZTVunyoVN2Tu5IDPFbShH7zz_gf6cDgInHGdOFK4A93nnvM5ZeES49ZxuVu5j42HFMxC7c-W6FUt5AHZNZDPwNDJPeAfFuR7Txvi3IycxNCmyjlaKorKTVOLkoSwPT0aPjuv7ou28H9-Pw5jFz89o_WQEvpD9fZrHqgV7-o3uoCXIBiYy3unn3OsdQBlnl7UnwYo93at2VoCj4Q-cjA35YxqbAmGO9J-h6I48hNZaqyKxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYnApWXPGGUQB61jpLwHSHLek1M3yxpilWLRU6cWLvSWcV7W_Pv6UQkXlfjbI5qzyX2odtVFwAHILUq82HFlpWiU2f1fYcBoYq02LlTMbVNsnh7UWJWarMf7rKUHKET4rMm7eFDTq-buFhW-P8O77py4WHLyjJBE3I5mptNmDtlV1h0lABVOCZ34p18ujL_kt0JcHRKUnhl27HP5nRvIefy4X8gtJKE97Wbut7SWSnojRQ1kpUyGO461TuXuMdePomzLxTwXpMcXjTdP6jGyb--aDBkpfXTybiyw27q85QDo9oHKiBuJ5B1DBi_N5tyc_4Yx5YE3t5_DhLoBa7O8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
