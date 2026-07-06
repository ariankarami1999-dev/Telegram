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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 07:13:44</div>
<hr>

<div class="tg-post" id="msg-667204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2WVgAicSVarPg3-yx7fxKfenLvxCDsmovnO4koEMn1_xgPDIY629NF1zA-0XXvyBlXpFedsfRImppn2n_tg4fwhlzIQmQvlVYvLNo7b9qssDlz83c1hFLxsZAEUMFMbXZMYMd0H14yr0GTnHXDFa0kPiEKHe-b-CAiNoxEUcep5g430vsAnPo8SCZpQ50tfr3D1yfB-ogz4_jD5VVEn30IP1gSw0WQ5KHmPNTO1jHrKL4eTSoR_oNvuuzIQGqi2v0wukQ9xwzZRHb4_iYX26m3qt0iDTID73qH704jHBeIIEt7vfOdyUzNQgMGNcKhCpIgXvcxPgm5L6QoH19m-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوباره آمدی اما...
🔹
سر در مسجد دانشگاه شریف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/667204" target="_blank">📅 07:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=R11BFAlE2tIOQ0fkUJEnYQLu9j_oJms8mNzsgqVkMlZMgkldSS0fQ3u1as7uYevb0oaecqnBgUThegFd5DL20-Ef3UP_ub4HXVvZoq6G_cBcbySauFmkj4ErntRLYQJTyFFR6M5Yvr-DBiOeFWv67DH9e4SHLdFtjkhUBNv9wfCXwcsTxik5ELm94dTr56Y2cwNp0wDksxAaB7cBCwbGVSJqDaEJPhU2M-vJIAZaqdGXP1D9Pm1jgvW1UQKltP2oE9H6rbhXnR5l8XcLVP6uY5HMheKHxG0tt-v1KAyiUMVkNsNoExTriGqiRrUv77fnVKpxdIVbgpI_30u77yW8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a8c2c68a.mp4?token=R11BFAlE2tIOQ0fkUJEnYQLu9j_oJms8mNzsgqVkMlZMgkldSS0fQ3u1as7uYevb0oaecqnBgUThegFd5DL20-Ef3UP_ub4HXVvZoq6G_cBcbySauFmkj4ErntRLYQJTyFFR6M5Yvr-DBiOeFWv67DH9e4SHLdFtjkhUBNv9wfCXwcsTxik5ELm94dTr56Y2cwNp0wDksxAaB7cBCwbGVSJqDaEJPhU2M-vJIAZaqdGXP1D9Pm1jgvW1UQKltP2oE9H6rbhXnR5l8XcLVP6uY5HMheKHxG0tt-v1KAyiUMVkNsNoExTriGqiRrUv77fnVKpxdIVbgpI_30u77yW8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل عظیم مردم در ساعات اولیه بدرقۀ رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/667203" target="_blank">📅 07:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb326d34a.mov?token=a6TY8YiqiSqqkJ9qYc-Mp5uQJUVCEXxR0DE1LmIB10X4BXhNHjMPI_qVebbMEYZPzSQ0j_rAAsJ6C4uxvo949t1Pb7RDlaD1NIWL61nB1nd-vCsDuGRPvNBbqFrozCAsqEI3dljNYCY5ITEGgcRskan4gu5GKu8lyX4UeQY-fXhFPjSZfPkfgOC87mGXIWeNClde7Tz5smycHxfq1pTHX2dRxMKHMFbbFP9g24prfxeznga5sTb_4ypjB0HT8EOf7CidWSsrq9F3xU7ssci8kHFqWM4LlegETRGGKl6jqQ-leqizO9_KbA750LWgk_lpJXyd9jFAVy4pgQFderqjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb326d34a.mov?token=a6TY8YiqiSqqkJ9qYc-Mp5uQJUVCEXxR0DE1LmIB10X4BXhNHjMPI_qVebbMEYZPzSQ0j_rAAsJ6C4uxvo949t1Pb7RDlaD1NIWL61nB1nd-vCsDuGRPvNBbqFrozCAsqEI3dljNYCY5ITEGgcRskan4gu5GKu8lyX4UeQY-fXhFPjSZfPkfgOC87mGXIWeNClde7Tz5smycHxfq1pTHX2dRxMKHMFbbFP9g24prfxeznga5sTb_4ypjB0HT8EOf7CidWSsrq9F3xU7ssci8kHFqWM4LlegETRGGKl6jqQ-leqizO9_KbA750LWgk_lpJXyd9jFAVy4pgQFderqjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش سرود ملی ایران در لحظات آغازین شروع مراسم تشییع پیکر آقای شهید ایران - میدان امام حسین (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/667201" target="_blank">📅 07:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1cc2b76ce.mp4?token=XDt181hpJL9-1vL_xn1ZyzkpIZh7Ij46OfVnO4acBwvg_MP3e2y7Lsk1MwYnDyJ0Bl9piIbiN_XUk6FoHcQH6Nu27QYxGDbnZl8Dy7-_TjuU2rgjN-wO0B80k--Esappz3YOsNbuGIjRYeyb18G-St1WUSQ3dI2ijTiTxdYBFoKtbe756YxYKxJigeTXF4iCKOkKgnTQmRprP3XK2dcShFOkPeVwxWx2eEodlrdKxFStTCnCcF-QyfzTMrPQxoBSc2e6_orFIWmxoW0xzUQfb4Rkid_0UIi1qM8Zup88QRtdQUN3X5FZmTaSSVZt16iIJh1xWOOzYd4fIYn4qpsaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1cc2b76ce.mp4?token=XDt181hpJL9-1vL_xn1ZyzkpIZh7Ij46OfVnO4acBwvg_MP3e2y7Lsk1MwYnDyJ0Bl9piIbiN_XUk6FoHcQH6Nu27QYxGDbnZl8Dy7-_TjuU2rgjN-wO0B80k--Esappz3YOsNbuGIjRYeyb18G-St1WUSQ3dI2ijTiTxdYBFoKtbe756YxYKxJigeTXF4iCKOkKgnTQmRprP3XK2dcShFOkPeVwxWx2eEodlrdKxFStTCnCcF-QyfzTMrPQxoBSc2e6_orFIWmxoW0xzUQfb4Rkid_0UIi1qM8Zup88QRtdQUN3X5FZmTaSSVZt16iIJh1xWOOzYd4fIYn4qpsaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های بی امان/ من با آقا خداحافظی نمی‌کنم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/akhbarefori/667200" target="_blank">📅 06:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28b1dbbfb.mp4?token=ZPZatSE1cJsuEwi9_DGS_CuzaSu7fPHZ3AlyT61HCs7meJyRsLf8gkwPBcBGD42mToHY59Sz1YzMDQXJnVefIWN9WqeKr58PLSLcqnfb0OsxH6EYHvbcd1jT29pAo7S8VgQY7YsJbicRZ-KHMghh6rnnFc4NeobI9_b6f69Gy1-LRmT2vt9P5b9C-Sla0uj9lVxRFzfYxMf34k9fdFBPhh7yGT4PSybY6qXXXz2OC0gic1dlJKvJFCsJA4bidravgrREKwWVyncz1gv3xy1mNvToAgDQYTvJkNTAHayE6KVKIIXhs9CTR1RuhTDFyH9ew7gV1jar83dhFOQJwzS-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28b1dbbfb.mp4?token=ZPZatSE1cJsuEwi9_DGS_CuzaSu7fPHZ3AlyT61HCs7meJyRsLf8gkwPBcBGD42mToHY59Sz1YzMDQXJnVefIWN9WqeKr58PLSLcqnfb0OsxH6EYHvbcd1jT29pAo7S8VgQY7YsJbicRZ-KHMghh6rnnFc4NeobI9_b6f69Gy1-LRmT2vt9P5b9C-Sla0uj9lVxRFzfYxMf34k9fdFBPhh7yGT4PSybY6qXXXz2OC0gic1dlJKvJFCsJA4bidravgrREKwWVyncz1gv3xy1mNvToAgDQYTvJkNTAHayE6KVKIIXhs9CTR1RuhTDFyH9ew7gV1jar83dhFOQJwzS-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من طرفدار دو آتیشه رهبر شهید نبودم/ وجب به وجب این خاک مدیون تو هست سیدعلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/667199" target="_blank">📅 06:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e25cca93.mp4?token=j9vuV8ufjmKIVc7yH8-8L37nq8PR14Q6zWBn6-9dYsmoBvhMRL2CHwlEQ8oVLr9t2HVCLrnGWUCc4MeyexTh5_1nS5YbYwjtLiPOQH8iZjovmvJ6DPld464Hnv4XQlT0QNZhrJd7JJzkklbXFuS8dYGuuBuovNmJfNwoecNiHQg_0yvishxDtX4QMfsgqIW-twxtI0BS8wrtccpXD3WN5GU5KQpnuBbG1H0NZLqsjSG7tNLwab5eJzgS_ewzzhy8nXtbQDAbpc8OTdjzc2QyokS4ICO6m_Kv47wozA9ci1fFWzWBa5l-VQiEQMmcNIbrfvUijhDOTUlopbEs1wucFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e25cca93.mp4?token=j9vuV8ufjmKIVc7yH8-8L37nq8PR14Q6zWBn6-9dYsmoBvhMRL2CHwlEQ8oVLr9t2HVCLrnGWUCc4MeyexTh5_1nS5YbYwjtLiPOQH8iZjovmvJ6DPld464Hnv4XQlT0QNZhrJd7JJzkklbXFuS8dYGuuBuovNmJfNwoecNiHQg_0yvishxDtX4QMfsgqIW-twxtI0BS8wrtccpXD3WN5GU5KQpnuBbG1H0NZLqsjSG7tNLwab5eJzgS_ewzzhy8nXtbQDAbpc8OTdjzc2QyokS4ICO6m_Kv47wozA9ci1fFWzWBa5l-VQiEQMmcNIbrfvUijhDOTUlopbEs1wucFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به عشق رهبر آمدیم/ حال و هوای شهروندان جنوبی کشور
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/akhbarefori/667198" target="_blank">📅 06:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM4xOlrZVHM0AORSwGpDBCh7GRAP4gz4HX6gczH1L3btwyyxHNs0EEm3vFbr4k6mDUFdl9z_YxoPYDJ-ILHFKaSzo0BKDFofhddgBHIud7ohmny6Hhxn_OLCWdpftxAj1oFX0evxGC4o2ab4qZv-QpI_ixnxLkPiMbFAZBNCyFKd_Y0Jct9g-KXuXrA4J0c-xCcmh0QE1bdGllqysRrUZn54KN9JbacgpK5daa5h1QoGhyMJEcttV8EphspLoi4xtzXNNp3ypKhDX9sYhDgbAlu2rIcJuqdv0_pNS6LTeH2KZ2Es77f6hEyVl7eo5n7DexkGnf1xRhFZWAT5IzvK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم غیور ترکمن هم خود را به تشییع آقای شهیدشان رسانده‌اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/667197" target="_blank">📅 06:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj5Nl7yMmXw0JcPOuikPaP4bnX9agWMRT-U2dMJ67f5t_KiEX6UBVucfBNY6tOz1TnaDmdenBky2PTwjwalmpQbMPZOeDkEnJMItmSaiF9NkDFEO3pR9AJMNIs8nXlBE-SDeV9W3P6-5AyJ3GVxI7Q8do0O2rt9Umy4LGjBNXklsWefbXea7Ndxz0fcDWKOrTZHd_UaP0MBH1MRnLE9c2klWnIYtNnJgXDrz111gYLeZX3ksm6Qk2RQfl2GzV8B0FiWoXryPldOzQObjWQ84CX9aQhgUOO5pm93LdN-XuqPUTLnovNuXCTLAai0MeIc8PirOk1DUrmshK-I4pUEESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر امام شهید آماده ورود به مسیر تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/akhbarefori/667196" target="_blank">📅 06:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f092cc8d5.mp4?token=oOPz9hFiyMB0UKj2z7BZke5p8heqk-Kl5eh1TPpTVy7hlcPFBlCV4wnYU_v4d1jXqZ7VtcqXCfnnLoJNanc9ptg3GXmhZqEv4xY4TSn0AN3Qp_SIiD6GoeYiL7gXCv7guCG9Z-50r2chkQP1uSzEwxIf2hM3IkhOUzFdHO0tAYaZ0vLSH1g2VKDAWzaxBL3V8KZKYgjf2W724p7hXu6-ISq62NHly1Uku4rQrxOpveaH1hfBoSpGkSTRcxhH1-FynjJZOLEjuzhI7qOPFRK35tBqsiOKpPiddFEInts9_GVrjMc5geHnzZS-Jlev-AbF00NFVigoLdGcVJZPRoWt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f092cc8d5.mp4?token=oOPz9hFiyMB0UKj2z7BZke5p8heqk-Kl5eh1TPpTVy7hlcPFBlCV4wnYU_v4d1jXqZ7VtcqXCfnnLoJNanc9ptg3GXmhZqEv4xY4TSn0AN3Qp_SIiD6GoeYiL7gXCv7guCG9Z-50r2chkQP1uSzEwxIf2hM3IkhOUzFdHO0tAYaZ0vLSH1g2VKDAWzaxBL3V8KZKYgjf2W724p7hXu6-ISq62NHly1Uku4rQrxOpveaH1hfBoSpGkSTRcxhH1-FynjJZOLEjuzhI7qOPFRK35tBqsiOKpPiddFEInts9_GVrjMc5geHnzZS-Jlev-AbF00NFVigoLdGcVJZPRoWt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از مراسم تشییع پیکر رهبر شهید: بسیاری از مردم، شب قبل اینجا بیتوته کرده و خوابیدند که امروز صبح اول وقت در مراسم شرکت کنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/akhbarefori/667195" target="_blank">📅 06:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acab75d995.mp4?token=Xfh5E0cwwPGo9AwLnn8vzbJFouVxGTu5uwpNSeuDiHvD1aA7aEKRfuuITXBqI9_odcW_Oge-I4NJ4PlfVrWqYnrcg65uNVLURqnxfbCIwtvD58o8Bt1sjGqkbcrSjOYFQyl0J1hnwMi80fnQmSxXh2QwbiNBPIph21biRNIuxcz8GkNoaADGxrcKWmks4QOCqLclJdoxZPrL3Qvv7qNPcxQ9CfI9hCye5NmYtEEbC2B1Wxl73LAPfmibq2zJQEvMOaVDZASo64qB8X_OAQDFSe2kYVHvjAHPMG9AZM4BHcXOQ7sPXzDYCPKJOonQO_N6sIqTbNu67gbkXRivL97mvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acab75d995.mp4?token=Xfh5E0cwwPGo9AwLnn8vzbJFouVxGTu5uwpNSeuDiHvD1aA7aEKRfuuITXBqI9_odcW_Oge-I4NJ4PlfVrWqYnrcg65uNVLURqnxfbCIwtvD58o8Bt1sjGqkbcrSjOYFQyl0J1hnwMi80fnQmSxXh2QwbiNBPIph21biRNIuxcz8GkNoaADGxrcKWmks4QOCqLclJdoxZPrL3Qvv7qNPcxQ9CfI9hCye5NmYtEEbC2B1Wxl73LAPfmibq2zJQEvMOaVDZASo64qB8X_OAQDFSe2kYVHvjAHPMG9AZM4BHcXOQ7sPXzDYCPKJOonQO_N6sIqTbNu67gbkXRivL97mvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام مردم در مترو تئاتر شهر برای رسیدن به مراسم تشییع
رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/667194" target="_blank">📅 06:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki4Vbd0lGnve8zbE2QQpaYjvnL21MoaNKFqfsGF1XEHerLJECmJaUeIn4Tz2jhGBVQjabIv8eMTKcmyctd3ISgss6UhK4lUj_K7B8TPf24ltFeTuWyBrHZsZdWC6CzBrZ_vL5vCq6KT9Y_rr3oBiG0GqkGgxBdx5CmS--_rzpsXsLS2kM_Y40E8az7pBIMIXVL4R6cqMP8tYw52yPGzu9ggbS7gUnpDGr7I1kiAAB8tY4ChWeFv61A81GuGIrUEQiHd2CF6J0u6hFqqnkyWLis4Z-cvxsSczixaSaJJmk-P5aPcg0P80-C5h0rJsxSS1RRZKVwdAvo-xCEQPoZjBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در انتظار پیکر مطهر رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/667193" target="_blank">📅 06:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0687ee45fd.mp4?token=VBd7it__8n6wY1j35rnljUMYxY8Oqcyqi_QNf2I7dI4VoTqowcLioTe-N4EeA6scSrE0v9EcQc2JHlzdxxVnnvWvCuPXuyJlsGL6Cf4Qz5xilPWmMIsR0GQCBWoGzKIOFENPow2irdCc49V_M_cCiw2hPiY7aOiOp3mI631Uv9CB4XgLVJk_7Kupi3XUsB8PYdNQhD3sJAZVjQG97qgdIiVS7v-ixxIMl4ulBRs3chvlbP64DDb50b_RR2p-OREDG6Q4VMO-Uf7WxdFGGA6dPymasoosd0VPbUrCANjD7bIdw4Zmi33v9Yu27MyDy9ssXxFEgB1oaaCZg5sNLVjaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0687ee45fd.mp4?token=VBd7it__8n6wY1j35rnljUMYxY8Oqcyqi_QNf2I7dI4VoTqowcLioTe-N4EeA6scSrE0v9EcQc2JHlzdxxVnnvWvCuPXuyJlsGL6Cf4Qz5xilPWmMIsR0GQCBWoGzKIOFENPow2irdCc49V_M_cCiw2hPiY7aOiOp3mI631Uv9CB4XgLVJk_7Kupi3XUsB8PYdNQhD3sJAZVjQG97qgdIiVS7v-ixxIMl4ulBRs3chvlbP64DDb50b_RR2p-OREDG6Q4VMO-Uf7WxdFGGA6dPymasoosd0VPbUrCANjD7bIdw4Zmi33v9Yu27MyDy9ssXxFEgB1oaaCZg5sNLVjaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری محلی جمعی از بانوان در متروی تهران در مسیر رسیدن به مراسم تشییع پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/667192" target="_blank">📅 06:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تمام ایستگاه‌های مترو در مسیر تشییع باز هستند
شرکت بهره‌برداری متروی تهران:
🔹
تمامی ایستگاه‌های واقع در مسیر مراسم باز هستند، اما در صورت افزایش حجم مسافران، ممکن است برخی ایستگاه‌ها به‌صورت موقت بسته شوند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/667191" target="_blank">📅 06:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2507931cec.mp4?token=AClt9V0FU1N7W2_c6GlQPLFozt_VBdjAdllw_t0AcdybIYdCw_QkqLSLxCeHWc2PkHuBpmx2Q90df3BTyQB8466Zisa3FYkq1Xlrz0l_eE1NoEmn7WX3ruScY-CVztTW_UHIJecBBgUu56HtCgmjOuc3XMGspCI67zsuJQCR48KIE3TdUrGjcfr6I2Tc1q-DC45rqpxtvMX1XYo_Jq6ZufewIfmRyobJK4dJtmhbscv8g4QISpLoZV1arqmKqZPBXxIfpGJ6l9TBeK9fs4axjfyw4ih65kqCP5_zITouPSXSG_xRYwnpePuprdVW2iJiFIQ8jDcPjmOIAGMRvnEAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2507931cec.mp4?token=AClt9V0FU1N7W2_c6GlQPLFozt_VBdjAdllw_t0AcdybIYdCw_QkqLSLxCeHWc2PkHuBpmx2Q90df3BTyQB8466Zisa3FYkq1Xlrz0l_eE1NoEmn7WX3ruScY-CVztTW_UHIJecBBgUu56HtCgmjOuc3XMGspCI67zsuJQCR48KIE3TdUrGjcfr6I2Tc1q-DC45rqpxtvMX1XYo_Jq6ZufewIfmRyobJK4dJtmhbscv8g4QISpLoZV1arqmKqZPBXxIfpGJ6l9TBeK9fs4axjfyw4ih65kqCP5_zITouPSXSG_xRYwnpePuprdVW2iJiFIQ8jDcPjmOIAGMRvnEAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید در مراسم تشییع: شهادت رهبر از رفتن پدرم برایم سخت‌تر بود؛ کاش نبودیم و این روزها رو نمی‌دیدیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/667190" target="_blank">📅 06:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa553a8435.mp4?token=hshURN2k3opnqFVfdqs2gqUsXeet0ukQp-TYWABcTs_xro7i5c5cguGkDUADF01mx_bBhjidt88T90sAQo5iMW_jBdSZ3xg4ZNpbBU_g1_dXnJ-Fb6fDu2qgN-lnw-3YqBXQ7Z0vVQuWc-2KdmbQ0UrVlc2mG9qyR9_AdF4ti2jfiyTrElFnfe7pbpfF-SPklBayz61OAUBaSqHA37H-mGnaKNDqJUGm3Jc5vCqM6LmBaOJdzfY-Nho6udP87WDVznFfXcJuHO1vqlG8a-_V9wl8BopoXCVgL5Xw_uoNN76MRGhthq5kSg9m4llBuxpwOsYbWxFayGqxhcq_-UPSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa553a8435.mp4?token=hshURN2k3opnqFVfdqs2gqUsXeet0ukQp-TYWABcTs_xro7i5c5cguGkDUADF01mx_bBhjidt88T90sAQo5iMW_jBdSZ3xg4ZNpbBU_g1_dXnJ-Fb6fDu2qgN-lnw-3YqBXQ7Z0vVQuWc-2KdmbQ0UrVlc2mG9qyR9_AdF4ti2jfiyTrElFnfe7pbpfF-SPklBayz61OAUBaSqHA37H-mGnaKNDqJUGm3Jc5vCqM6LmBaOJdzfY-Nho6udP87WDVznFfXcJuHO1vqlG8a-_V9wl8BopoXCVgL5Xw_uoNN76MRGhthq5kSg9m4llBuxpwOsYbWxFayGqxhcq_-UPSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور چشم‌گیر مردم در آغاز مسیر تشییع رهبر شهید انقلاب در میدان امام حسین (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/667189" target="_blank">📅 06:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f61c4280c.mp4?token=Jvw1rI5CptH35cfOSVJBZjKLxqE36bVxGDbTqxU_Rj5NTCYnJgMwyKbyxOF2h3n0bM1X1fKf8mfdwKUtD9wyaAmif8nobXL0MrWq5rpxVQHBjaTdo48066wUIAOVY71OLT1AHUA4XaQs0EVq58NfPJdmkrH2ujRDXBOi5zVKtU-oRURtmvigpRfIU2mmmoZMueiDzpJjKszrcbZBW2ERZmSeKX3G1v0_eKpwoWQyNM12PslgFx_qmbSvFtVQlBT8QXrTyiEeV2-aqjBjMCfQlBCND0ZCh00EJYqtz14ZlZE4L2qooZj5IwuUpeQgI9P9jbfpMKkHO6_9d02LSkg_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f61c4280c.mp4?token=Jvw1rI5CptH35cfOSVJBZjKLxqE36bVxGDbTqxU_Rj5NTCYnJgMwyKbyxOF2h3n0bM1X1fKf8mfdwKUtD9wyaAmif8nobXL0MrWq5rpxVQHBjaTdo48066wUIAOVY71OLT1AHUA4XaQs0EVq58NfPJdmkrH2ujRDXBOi5zVKtU-oRURtmvigpRfIU2mmmoZMueiDzpJjKszrcbZBW2ERZmSeKX3G1v0_eKpwoWQyNM12PslgFx_qmbSvFtVQlBT8QXrTyiEeV2-aqjBjMCfQlBCND0ZCh00EJYqtz14ZlZE4L2qooZj5IwuUpeQgI9P9jbfpMKkHO6_9d02LSkg_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور باشکوه مردم در چهارراه ولیعصر
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/667188" target="_blank">📅 06:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01380449bd.mp4?token=D78GUxdndNG20XF3a-BpaiVEC96Rhv6tIZ3FMIyVb_0vC9ZS2s_SdU-PtoHTAxzJVl95HDoPYnuQcKMb1LM0G_ZilmjyhDKwIN7riXl0drmQM1hKUTsV44Wcq5ABueeRmtquZX0-BOXpyhWEM4zFhcsIbTMnaA5PYH-_3b1es_olBWspdCrz3w3grFnalfDuNgIdKezCONdwVaxHINtYKZ7fxDs_9cBZ5tHj0ixjp3BYWaR5WyHPXCtyvapq9thUpf3Dg0Js1x5M8hq05LvGoNZ35-lO2GkzbmBbwxaWrMAmdBHKR_1ZuYFJUAUROq_9cRmAdyoeZIniZdERQRukuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01380449bd.mp4?token=D78GUxdndNG20XF3a-BpaiVEC96Rhv6tIZ3FMIyVb_0vC9ZS2s_SdU-PtoHTAxzJVl95HDoPYnuQcKMb1LM0G_ZilmjyhDKwIN7riXl0drmQM1hKUTsV44Wcq5ABueeRmtquZX0-BOXpyhWEM4zFhcsIbTMnaA5PYH-_3b1es_olBWspdCrz3w3grFnalfDuNgIdKezCONdwVaxHINtYKZ7fxDs_9cBZ5tHj0ixjp3BYWaR5WyHPXCtyvapq9thUpf3Dg0Js1x5M8hq05LvGoNZ35-lO2GkzbmBbwxaWrMAmdBHKR_1ZuYFJUAUROq_9cRmAdyoeZIniZdERQRukuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم‌های سرخ انتقام در دستان مردم حاضر در چهارراه ولیعصر(عج) تهران
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/667187" target="_blank">📅 06:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74df919fa.mp4?token=qLoKHIxKOylggInLbYoAHWAeSaNFwDDggbKQ9KHb5C9kzXAi3QLA1iuUh34ZN7R9iJtfT-QVOYbgeRFAoCRGAezkNjhZ7AXDCqJj3bYUXQeKFSs8fEM7fpBJSfw7RfSHeErdhT3dgd-5e6zDh0xHRw0mpJU6sdjbZeBBn1-Jl1j6KodtoKTE0ckjqW7fiXUKV1vtK9s_eucmrUVem6hSCCOGq4dL0VBHfzIyweXkrcsWH_nCzKXonHFTDAY2LjhcrBKgSqJxgr4cbQDl5__V8y4TVoPHLyHDv6-klrR_lg4lNdc5xRtZfBOwgakKlqRC5kEkD36IUtnsVupS5-3-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74df919fa.mp4?token=qLoKHIxKOylggInLbYoAHWAeSaNFwDDggbKQ9KHb5C9kzXAi3QLA1iuUh34ZN7R9iJtfT-QVOYbgeRFAoCRGAezkNjhZ7AXDCqJj3bYUXQeKFSs8fEM7fpBJSfw7RfSHeErdhT3dgd-5e6zDh0xHRw0mpJU6sdjbZeBBn1-Jl1j6KodtoKTE0ckjqW7fiXUKV1vtK9s_eucmrUVem6hSCCOGq4dL0VBHfzIyweXkrcsWH_nCzKXonHFTDAY2LjhcrBKgSqJxgr4cbQDl5__V8y4TVoPHLyHDv6-klrR_lg4lNdc5xRtZfBOwgakKlqRC5kEkD36IUtnsVupS5-3-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از حال و هوای مردم در مسیر تشییع رهبر شهید انقلاب پیش از آغاز مراسم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/667186" target="_blank">📅 06:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsaRS7jEDzIoz11fWDYZp0JHWVw33ELaohXOtpegGvJ-06nxbexeM1tnzjOutMwfKuwfDNCHg9KPPdhemzhRrHNbypYDzrYjI6EBJBeiDnL-tt9M5Tj978IZbym0-NzF1w_oVvuVt5ivC43wBJt6UUvGzrBHRk1bID1qVyHo5FTLQs9cB57ix89ZsTF9S3bAJ1FOJEkIxzbhh1rLt_bnQoFzu3-Rlsi7_eUDpwrhQhcZBDfwfHRakM69K_MngsZ5GSYhJk_XNV9YywaGM__8lMi4sHHBM1r3laywOkMB-l-9AnBOuz__esPuPohqIyibXEX96t1xqB-1X6ZbhzY7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز رسمی مراسم تشییع پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/667185" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=uCxKwmllyYEY4liEWOQSh24Ff-VkxsMF0yXxFC62FWhClKCSI3B5AioPxVViVGqVuyyahXOqlr1ues3Ss64KvwZp64_sPBZQVcQgzxqffwZHx3olX0IYZr5pkh_e-HjNeHnSP69xnKF2Vu9OXv9iOOzcTg01FXblxZ8Jq28CAxEuTe1Dek8UxEAEkGs8hf05qGoAju52-3Q8MWLoWDuAlkf7BHFPfBEYSauqxftwfnjHsnZeRM5vJ5TX14deOAxZlmy91EihuXdKYXvxrMm-f0HdwMZf4XSUxWXPU_T_d4SbT4vIiUV9SzT7t4FsKFhyEkp9oYSW5TXEvR_CkNy70w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fed9d9e34.mp4?token=uCxKwmllyYEY4liEWOQSh24Ff-VkxsMF0yXxFC62FWhClKCSI3B5AioPxVViVGqVuyyahXOqlr1ues3Ss64KvwZp64_sPBZQVcQgzxqffwZHx3olX0IYZr5pkh_e-HjNeHnSP69xnKF2Vu9OXv9iOOzcTg01FXblxZ8Jq28CAxEuTe1Dek8UxEAEkGs8hf05qGoAju52-3Q8MWLoWDuAlkf7BHFPfBEYSauqxftwfnjHsnZeRM5vJ5TX14deOAxZlmy91EihuXdKYXvxrMm-f0HdwMZf4XSUxWXPU_T_d4SbT4vIiUV9SzT7t4FsKFhyEkp9oYSW5TXEvR_CkNy70w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای میدان انقلاب تهران، دقایقی قبل از آغاز مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/667184" target="_blank">📅 05:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab7ce01d28.mp4?token=Neli-d2rnut2NDkiBPFP0t6sazDoSwDOnIEGMoTiDz9GoOr88KEdjd7UswUgB-X5dtvviziMgHpZWUP5_pY-A7tKSaPKF0GmU6l_hgvNyFtrDtxMdZU9Cl8SZ0ett7_YoErhoDo5dYZnjhs_PMeyu8P9M7dZ1SaTKCu6-MLzW3xf8FyrSV9xWPphSUa9uhTmzQr8aypNYiiR-eUyyRVWKq56J6UnGWPLJ0nhXhtY_QVlGtawYjcnLUZsk3iJ6Kxv7uAllcZWNZYNM-h080TccceMowPv9X_BrxCTZrVB4oDNyqw98LIzm_MhuJybr7cYyCx-AWtvd3u41fltcyUI9W2Dst8hG5GDv9O8APO2FddISYabBwFUCS9hwWclPHow8aEVVemrk21g9-6ZUY_l8A81qglIQQrxkUjvB66UZJ4Wrv1Bj6lgptRgoq7WR28uYW9wPK9ainmvSzzTU3dridm6nnMvFF5TR0zvSCFOQ43ReDeaHwLm6WfYMb5T4p8fGkmI2mrWk0p3HlH2_6jZvtafm3zTPrMvDe2-CYI1SUMErRQqoKiFpH8Y5wzp-jxdkUnHnVbvaqwFcOaS8nTSJa0E5YXpQR0BTZoG29SdRMderhSeAwByeHyDjOeRCsdnfF2-Ug5UBnxnQ9zxNCkkx7ACmOrse7kGyg3qmCdPrR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab7ce01d28.mp4?token=Neli-d2rnut2NDkiBPFP0t6sazDoSwDOnIEGMoTiDz9GoOr88KEdjd7UswUgB-X5dtvviziMgHpZWUP5_pY-A7tKSaPKF0GmU6l_hgvNyFtrDtxMdZU9Cl8SZ0ett7_YoErhoDo5dYZnjhs_PMeyu8P9M7dZ1SaTKCu6-MLzW3xf8FyrSV9xWPphSUa9uhTmzQr8aypNYiiR-eUyyRVWKq56J6UnGWPLJ0nhXhtY_QVlGtawYjcnLUZsk3iJ6Kxv7uAllcZWNZYNM-h080TccceMowPv9X_BrxCTZrVB4oDNyqw98LIzm_MhuJybr7cYyCx-AWtvd3u41fltcyUI9W2Dst8hG5GDv9O8APO2FddISYabBwFUCS9hwWclPHow8aEVVemrk21g9-6ZUY_l8A81qglIQQrxkUjvB66UZJ4Wrv1Bj6lgptRgoq7WR28uYW9wPK9ainmvSzzTU3dridm6nnMvFF5TR0zvSCFOQ43ReDeaHwLm6WfYMb5T4p8fGkmI2mrWk0p3HlH2_6jZvtafm3zTPrMvDe2-CYI1SUMErRQqoKiFpH8Y5wzp-jxdkUnHnVbvaqwFcOaS8nTSJa0E5YXpQR0BTZoG29SdRMderhSeAwByeHyDjOeRCsdnfF2-Ug5UBnxnQ9zxNCkkx7ACmOrse7kGyg3qmCdPrR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای چهارراه ولیعصر تهران در آستانه تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/akhbarefori/667183" target="_blank">📅 05:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
از تهران تا بین‌الحرمین
🔹
کلیپی از الحشد الشعبی برای تشییع پیکر مطهر امام امت در نجف و کربلا.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/667182" target="_blank">📅 05:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57253c680e.mp4?token=tL17cDYrI81Ye5trFVV00zLgPs7Ha9Vjxe8iNS63GYzS1OLQGrs2UwLhVsYHdAAEitIlKHh9zGOKxcUy69FhBqTf60ZSyR9fI5AdfdmU-Bosf_4uB-kkLrnqcLGQ1D5KcXk4SgJorSVHAu6uPDV0Sv0kX6CBmIbsQLwQJzn49kZ-RUjCk_xgMeqUsFmVRaAg6MqXghAxkIB7N3K8X-3b9A7L5zr63c4neDWDpnmUdh6466DveE-2cE98IlLBSVj8P3jmjR4BaiXxnElED6TMPZhIOjlYjBI2ErQ_e0JQCfehllt1eyqpX5UKNCBhElwsVFKlvUgdpdv_npB53Dxfbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57253c680e.mp4?token=tL17cDYrI81Ye5trFVV00zLgPs7Ha9Vjxe8iNS63GYzS1OLQGrs2UwLhVsYHdAAEitIlKHh9zGOKxcUy69FhBqTf60ZSyR9fI5AdfdmU-Bosf_4uB-kkLrnqcLGQ1D5KcXk4SgJorSVHAu6uPDV0Sv0kX6CBmIbsQLwQJzn49kZ-RUjCk_xgMeqUsFmVRaAg6MqXghAxkIB7N3K8X-3b9A7L5zr63c4neDWDpnmUdh6466DveE-2cE98IlLBSVj8P3jmjR4BaiXxnElED6TMPZhIOjlYjBI2ErQ_e0JQCfehllt1eyqpX5UKNCBhElwsVFKlvUgdpdv_npB53Dxfbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متروی صادقیه و مردمی که همچنان در حال عزیمت به مراسم تشییع پدر امت هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/667181" target="_blank">📅 05:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مصطفی راغب قطعه «وداع» را برای رهبر شهید خواند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/667180" target="_blank">📅 05:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66553d540c.mp4?token=A08_nhYTy4zlErsvFSlia9xw4okaJvZf14MILTTS3OM546u_-RawOx7pc50vm8Qgf5CSl0OG0oN4nUKKcSHcldiv_ijg8b7KgmqRguavJM-yyuqM5-tiESOwg6bbsyBo2_Xpofc6v805i1hZnYhDsU8EkTNh7r-3ru2F_zWnkTUSHnlp5ZDqZh7qU_WqtjWaGSXqjlsiNk9wPEQFoSKcYyfcqVwUHbjOgWQNafzkUyiNkKAPDl_VCIbQl68Hg2RSw_oEf0_Vgc5ctNHnEW-MWeWoj287YziUom-Appt1Ls5eMlpDXknqZXOhPh3Qs_HpZyy1G2F40ivaTt4Ei_Us5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66553d540c.mp4?token=A08_nhYTy4zlErsvFSlia9xw4okaJvZf14MILTTS3OM546u_-RawOx7pc50vm8Qgf5CSl0OG0oN4nUKKcSHcldiv_ijg8b7KgmqRguavJM-yyuqM5-tiESOwg6bbsyBo2_Xpofc6v805i1hZnYhDsU8EkTNh7r-3ru2F_zWnkTUSHnlp5ZDqZh7qU_WqtjWaGSXqjlsiNk9wPEQFoSKcYyfcqVwUHbjOgWQNafzkUyiNkKAPDl_VCIbQl68Hg2RSw_oEf0_Vgc5ctNHnEW-MWeWoj287YziUom-Appt1Ls5eMlpDXknqZXOhPh3Qs_HpZyy1G2F40ivaTt4Ei_Us5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترو امام حسین و‌ خیل جمعیت برای شرکت در مراسم تشییع پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/667179" target="_blank">📅 05:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=jn188P2VVXKiwa4yrDYaeCA3bhbTpVP7yZ8NPhF8jk0mNIhbnfQe1IgBrkoHDsuKvaPsVwm4A_v-PMmJpcKdE0axf3oqrHsEJfbfUkUWgxHePiYvBne_r_0CTkDsVqK0WH6-EHQaFLYZekHzrTmzeveDcWsgEyAql3jVZuUuo8l9a43srLTiA24vTTDOU_SFxQIofX2mIoEn_T5jV9MLMcjjPOwDo5ciOCIWisRyy8PeVjOplD0Zx4EGPQr_CG90o5rL6F_nqqHadKDnx-6ery27Qz4ZtFufoD5TNuwr-mW8IGZDeFkqmgBb7eRgR5CojqREuIkO2TsyaRAskDtbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d4b48290.mp4?token=jn188P2VVXKiwa4yrDYaeCA3bhbTpVP7yZ8NPhF8jk0mNIhbnfQe1IgBrkoHDsuKvaPsVwm4A_v-PMmJpcKdE0axf3oqrHsEJfbfUkUWgxHePiYvBne_r_0CTkDsVqK0WH6-EHQaFLYZekHzrTmzeveDcWsgEyAql3jVZuUuo8l9a43srLTiA24vTTDOU_SFxQIofX2mIoEn_T5jV9MLMcjjPOwDo5ciOCIWisRyy8PeVjOplD0Zx4EGPQr_CG90o5rL6F_nqqHadKDnx-6ery27Qz4ZtFufoD5TNuwr-mW8IGZDeFkqmgBb7eRgR5CojqREuIkO2TsyaRAskDtbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان انقلاب تهران؛ اندک اندک جمع مستان می‌رسد...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/akhbarefori/667178" target="_blank">📅 05:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYBBLjLnCWh9l7odr7wJSddT30B82XfqJ1kPJt9n0HT6oppQT2n06jQN9MJlxKU_Fqf-Bc-illfUNKOPbCfbGQKWvvOPPoo14cpLtwZ_7luMIM0oOdbuWJHGON2e04Sa0dxVCLLYghVmvD9ScOrh1zKnoFq3crJJE7l-xy7-o2zCXQ_DmXlwdK0tfyR3yNd0vm7gU-R9KUg5QOliNJhAlfSmyG8_ii7evf5GegYx07v950Altsq7sJCsYiS8fu_lLKk8eBVpb7bjodUvGkba1g1oGkVygUrJOIAst8rtFc8xpw4TmBJyiFyuj8FJlCUIZ1_fWvthNvJHlJbab4FaluhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYBBLjLnCWh9l7odr7wJSddT30B82XfqJ1kPJt9n0HT6oppQT2n06jQN9MJlxKU_Fqf-Bc-illfUNKOPbCfbGQKWvvOPPoo14cpLtwZ_7luMIM0oOdbuWJHGON2e04Sa0dxVCLLYghVmvD9ScOrh1zKnoFq3crJJE7l-xy7-o2zCXQ_DmXlwdK0tfyR3yNd0vm7gU-R9KUg5QOliNJhAlfSmyG8_ii7evf5GegYx07v950Altsq7sJCsYiS8fu_lLKk8eBVpb7bjodUvGkba1g1oGkVygUrJOIAst8rtFc8xpw4TmBJyiFyuj8FJlCUIZ1_fWvthNvJHlJbab4FaluhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌های تلخ نیمار پس از حذف برزیل از جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/667177" target="_blank">📅 05:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFsANP34isTcfh8AVuchcvecqZWY4UmuNLOZl5lloP3J5CfmjzU2pbfXwfGHYkqgcOpF4qtuliFwEygmOXHDrxU80WrBEgSkIb_z6dQiSLLo_0ONq7y5Z4vPN1jRhYpDiGs5GkNsWkeQWmfjF4RwsGDI8nanB8uTzdvoNKqyJnODK2kQfgVsAes4A8epzt12B0sJ30JpDBwnq65Xj04K3qn3cVTsC8iwvGR0_JbpZhRGS9Fc1R50iHiQaZdH7ZzNFA7KNcMrB5BEo00_8TDy_La8BFht4USgLUCg5sUIcVpa9wTQjAbEjNMXkyAN6aB3UnnUVcOj7jI6tjl_BWe8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برزیل از جام‌جهانی حذف شد؛ نروژ به یک‌چهارم صعود کرد
🔹
نروژ ۲ - ۱ برزیل
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/667176" target="_blank">📅 05:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm-v7rMDwbD5JTFwkjmHyUupF_O2JyS5hbtrfmyBktTjiBudVSbqOPhbSeLDlzyiMDwMmvbrbjcH-LhDIBow5Wr9b-d_lEICP9Ai9l5BxjF9opKPpMFjuJSa4SC9sx6ufE-3-uI2FGsydzDgczpvsdyOTIKiAJwxlRCt0TOcZ7BJTN0FL474iyAeDmuVrqZ8c7EHY1bgyNiIwTz59zjX87Rc2R8yfT5fSVwYzkIPvbb8Tdg2V-bDL_tk06shGTkrGVjWRxovECPflBl2yb59fba9FXxkPHmomF2e-746R-A07NViLXENK-s-lYOSHX0yvvM4lUVBb860ZCYIk2z7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۵ تیر ماه
۲۱ محرم ‌‌۱۴۴۸
۶ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/akhbarefori/667174" target="_blank">📅 05:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIIfDpukWI00pKc3O9oDOGcKIuo43RuZSP-sTqgXdbloRG_TTN21M0Uv0tIDJWYlHgqGL2SdoWvJ4rrfhmET_4Hrs-jbvjLwvkpuKYNc9XM2C8QBcee4OOPSc_Ljk8G4svVX0OxQt4HUAi-s6rBznWNoKMEB0HC6-YKFqp4I8fQTic_n6kFVrcpRF_GTuGtwEG1Ah8a8DUDDFE-g6gKYkO5cOW9A86lFNzMapDRSmB5A7qEbvR5WgyZK9s8adkrdBR0t6WyJYOncd-YRCbJLx6iUWbOYdQIa4eHQa6MDcP4YTxYq_MTq2bb7DnANvAipuBtq22jW1ny7z1nVcHMWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
بسیاری از صاحبان کسب‌وکار فکر می‌کنند...
🤔
🔹
همین که محصولاتشان را داخل دیجی‌کالا، ترب، اسنپ‌شاپ یا سایر مارکت‌پلیس‌ها قرار دهند، فروش شروع می‌شود.
🔹
اما حقیقت این است...
حضور در مارکت‌پلیس، پایان مسیر نیست؛
آغاز رقابت
است.
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/667172" target="_blank">📅 01:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjfXaj4zASIebPP1lLQNB5Q604lDgNQ_cJw-gyJ3QvyAilWp5MOCfAdkarGLqzZhjrWIzINFpXvSSQS0ZhMwRrYJ9D-ozlsjVdUg8smDHExcSuoluGj91ZxfNaddOg_a7JULMePr6CNiIKgj3NWG1hlRKPZU3CnzWJRdZCliY5Xth4Xeyi0Yb8W7z4xwgmE0zm5fAf8iD2lmqkL-PEU6_gTXOCx3JHAik7BOQEdKnlzbbvu7UPgorrcGwehfU6WFllla5f8-hkkwdz1XoWlhC055wTfs8oUn3-Y6vlc3F5NOMVTmcPZCiPPbSB4raEAYsp-AKL-CxlzdP_WTRQ4hQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/667171" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7930bc7d2.mp4?token=DIbwIC88xFB6X6cEvRJ6yh1hoXkajh8l71ZkbF5qAFymPgLo_8XnpVSGp0zMCTnUM2aJct5s3IT5UsOKZFL5XV4g4IBgJoFzd8szRA3HNCmvI5fjfxTG2kqFA9djbn78WL9gSH4_D-T1AZeAhYzyAzvynfoy3w8AhoedUbsC14iQW5ox-Y9OuCtmeoFTs-Z6gY6hX7amzxZ-CqPeG6WemGFB-1Mcj1OhucHVXbcXOrIy1myrWfcfZEsGPjNgUILQgakxGjbsiX8EDPKB-lwEvvAqbXEn6M1wIENFSicf0L4sHkBqGjW8Fud1lT-nyshFf9OjFil_FcZLofWWkjQ7VENUh27aLMJjDxwhQAvgV4tb6Vuo6_K4tEt-kG6v0HMUMTeYoQrMRL0pxoWJ66pFUlu4hpiq8QAdKT4oQ484A3dd3iYm3DvpP5F4Akx-pvsxrIhvStuxneMQNLhONkm97u7K2z4-BMoVdaSgs7CoPSArlbfh-1GaWXUtQlZhcocYHKe4oHPjiOvJbcY44cJKcRS9B6p_bHRwraCOb9tr57DNXpjkWvJHWUwGlLPJkx-cIFj1FgYL0lbaUaTbLfk-QtHCP9LUSZFlZ930oIOpomwJwxBfvd5Mm2yDVA_8DxFIOPbNmKPJToT3-MPePKwamd7aI2-IyIIEHNKWZ6IB_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7930bc7d2.mp4?token=DIbwIC88xFB6X6cEvRJ6yh1hoXkajh8l71ZkbF5qAFymPgLo_8XnpVSGp0zMCTnUM2aJct5s3IT5UsOKZFL5XV4g4IBgJoFzd8szRA3HNCmvI5fjfxTG2kqFA9djbn78WL9gSH4_D-T1AZeAhYzyAzvynfoy3w8AhoedUbsC14iQW5ox-Y9OuCtmeoFTs-Z6gY6hX7amzxZ-CqPeG6WemGFB-1Mcj1OhucHVXbcXOrIy1myrWfcfZEsGPjNgUILQgakxGjbsiX8EDPKB-lwEvvAqbXEn6M1wIENFSicf0L4sHkBqGjW8Fud1lT-nyshFf9OjFil_FcZLofWWkjQ7VENUh27aLMJjDxwhQAvgV4tb6Vuo6_K4tEt-kG6v0HMUMTeYoQrMRL0pxoWJ66pFUlu4hpiq8QAdKT4oQ484A3dd3iYm3DvpP5F4Akx-pvsxrIhvStuxneMQNLhONkm97u7K2z4-BMoVdaSgs7CoPSArlbfh-1GaWXUtQlZhcocYHKe4oHPjiOvJbcY44cJKcRS9B6p_bHRwraCOb9tr57DNXpjkWvJHWUwGlLPJkx-cIFj1FgYL0lbaUaTbLfk-QtHCP9LUSZFlZ930oIOpomwJwxBfvd5Mm2yDVA_8DxFIOPbNmKPJToT3-MPePKwamd7aI2-IyIIEHNKWZ6IB_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استانداری کربلا: هزاران موکب در خلال مراسم تشییع مستقر خواهند شد
🔹
شورای استانداری کربلا اعلام کرد که در جریان تشییع رهبر شهید انقلاب قرار است هزاران موکب در مسیر تشییع برپا شود.
🔹
بزرگان شهر تأکید دارند که این رویداد باید در شأن و جایگاه رهبر شهید برگزار شود و تمامی آمادگی‌ها با بالاترین سطح از نظم، هماهنگی و کیفیت اجرایی انجام گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/667170" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c23eb2f.mp4?token=g-D4H5_mqDS2LxnDzeymtorTEPuq0icViHMojNXPdGzWH7vC33d20CVS7RL3sntRtxPq6ztlCRy2VnrYHmGh3rESsaQOCc-9MpOcvHmxuDDmc_Gb9U-9aB38rYyWSZJpqTY9onjWH7yEKSNRh0Gh55rz8X1nBn4uAynTcOQNK8eBX7QEXARAyj8lmCu1xPH8yAPOLzjMH9ImOcwCJo6goZefi-rCm-pSV5B6e17JTTitu1JKTI2WBzvusQeAhWA9NM3fi3UksLhK9U5k10eHpLuK6uhqv2KXMIAjSTNmq8Jn-sdfkOnRkJ2fD4RiUCSwMBfdWEQf2UGnwUkVm1DbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c23eb2f.mp4?token=g-D4H5_mqDS2LxnDzeymtorTEPuq0icViHMojNXPdGzWH7vC33d20CVS7RL3sntRtxPq6ztlCRy2VnrYHmGh3rESsaQOCc-9MpOcvHmxuDDmc_Gb9U-9aB38rYyWSZJpqTY9onjWH7yEKSNRh0Gh55rz8X1nBn4uAynTcOQNK8eBX7QEXARAyj8lmCu1xPH8yAPOLzjMH9ImOcwCJo6goZefi-rCm-pSV5B6e17JTTitu1JKTI2WBzvusQeAhWA9NM3fi3UksLhK9U5k10eHpLuK6uhqv2KXMIAjSTNmq8Jn-sdfkOnRkJ2fD4RiUCSwMBfdWEQf2UGnwUkVm1DbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ده‌ها صهیونیست به خاک سوریه در میانۀ سکوت الجولانی
🔹
حدود ۷۰ شهرک‌نشین صهیونیست تلاش کردند از منطقه جبل‌الشیخ وارد خاک سوریه شوند که این اقدام به تنش و آشوب در منطقه منجر شد.
🔹
ارتش اسرائیل اعلام کرد این افراد بازداشت و برای طی مراحل قانونی به پلیس تحویل داده شده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667169" target="_blank">📅 00:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de64ccc53.mp4?token=a1k4l1oPBYWZmP-k-XUssITPHw4hXU1OJVqA7L4jsHPobCx89BZtrrlAZRiQH47bvlxMz-VyC7Y87ykPHCOearpuAFXRchaEh3HVR-8nebodStJUbPLQU8NzXaYJPttaGw_rOwO8sWOE12ek7rjGbb2Epejog2puDKJxBOwRi-K_wLnQdKY9RyfNwokdE3D3-CLD-0fySPLhcRC0H7UZqin6sm7KNAOCU6oDSq0o2vPPv3gfajBYNsL2UhGpKO2hg6d-bbZ4cGtVGVBEZnIYiDgcdzERTte3Z0TQYi5b5XKkmUOx8tPA2o7dohp6ZKW0C4pQ69c17I8RqKHzLfSJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de64ccc53.mp4?token=a1k4l1oPBYWZmP-k-XUssITPHw4hXU1OJVqA7L4jsHPobCx89BZtrrlAZRiQH47bvlxMz-VyC7Y87ykPHCOearpuAFXRchaEh3HVR-8nebodStJUbPLQU8NzXaYJPttaGw_rOwO8sWOE12ek7rjGbb2Epejog2puDKJxBOwRi-K_wLnQdKY9RyfNwokdE3D3-CLD-0fySPLhcRC0H7UZqin6sm7KNAOCU6oDSq0o2vPPv3gfajBYNsL2UhGpKO2hg6d-bbZ4cGtVGVBEZnIYiDgcdzERTte3Z0TQYi5b5XKkmUOx8tPA2o7dohp6ZKW0C4pQ69c17I8RqKHzLfSJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستیانو رونالدو تایید کرد: این آخرین جام جهانی من خواهد بود!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/667167" target="_blank">📅 00:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1509a3e0e7.mp4?token=BBKWhujuWziXMqThAC8c30GS5elzEP6uzTQTY60ixcqnXRgIwmm9yjoWX5EGhXywNkdkj1YnyWMLcZQOGJ8z4iq_B5V4xNGRVF46JWCHkzm3x7gAW1uWGPbNKmKFtmC323_513vx3v6L-u6BfbjbIGb4TL18q2NWA77VuQEN5vE5MnLe1Ol5Hl1kwGXxS2BVfyXb6XkvJ6vZXHgbo2ydykaiDXDprjLow_iKXWIp1Sbw5fEwtVBfrQw83Dt9_Ir8lpVfnCdMokH6NO-rXe5XwdpPp4iOIx_V-98g88XqgXSnWcW7e2yroZNA2cVxho5uCS40Wow0zgHSc0w3gITVEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1509a3e0e7.mp4?token=BBKWhujuWziXMqThAC8c30GS5elzEP6uzTQTY60ixcqnXRgIwmm9yjoWX5EGhXywNkdkj1YnyWMLcZQOGJ8z4iq_B5V4xNGRVF46JWCHkzm3x7gAW1uWGPbNKmKFtmC323_513vx3v6L-u6BfbjbIGb4TL18q2NWA77VuQEN5vE5MnLe1Ol5Hl1kwGXxS2BVfyXb6XkvJ6vZXHgbo2ydykaiDXDprjLow_iKXWIp1Sbw5fEwtVBfrQw83Dt9_Ir8lpVfnCdMokH6NO-rXe5XwdpPp4iOIx_V-98g88XqgXSnWcW7e2yroZNA2cVxho5uCS40Wow0zgHSc0w3gITVEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه تشییع پیکر رهبر شهید در عراق
🔹
مراسم سه‌شنبه شب در عراق آغاز می‌شود؛ دولت عراق میزبانی رسمی را بر عهده دارد.
🔹
صبح چهارشنبه، ساعت ۶، بدرقه و تشییع مردمی در نجف شروع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/667166" target="_blank">📅 00:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
نتانیاهو: ما غیر از آمریکا متحدان دیگری هم داریم
🔹
نخست‌وزیر رژیم صهیونیستی به سخنان جی دی ونس، معاون رئیس‌جمهور آمریکا که گفته بود واشنگتن تنها متحد اسرائیل است پاسخ داد.
🔹
ما دوستان دیگری هم داریم «مثلا کشور کوچکی به نام هند که ۱.۴ میلیارد نفر در آن زندگی می‌کنند.»
🔹
برخی از کارشناسان معتقدند شکاف‌های ظاهری میان رژیم اسرائیل و آمریکا بخشی از جنگ زرگری دو طرف برای پیشبرد سیاست‌های مشترک آنها است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/667165" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احمدی، نماینده مجلس: بیش از ۳۰۰ خبرنگار خارجی عظمت تشییع رهبر شهید را به جهان مخابره می‌کنند
علی احمدی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
حضور بیش از ۳۰۰ خبرنگار خارجی، بازتاب‌دهنده شکوه مراسم تشییع رهبر شهید در جهان است.
🔹
این مراسم یک «قیام ملی» و نماد همبستگی مردم ایران است و برخی روایت‌های رسانه‌های خارجی نتوانسته از عظمت آن بکاهد.
🔹
برخی رسانه‌های خارجی با تعابیر تحقیرآمیز درباره تشییع در عراق تلاش کردند از شکوه آن بکاهند، اما حضور پرشور شیعیان عراق و تمهیدات امنیتی حشدالشعبی، امنیت کامل مراسم را تضمین کرده است.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/667164" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شهرک‌های مسیحی‌نشین لبنان ادعاهای نتانیاهو را تکذیب کردند
🔹
شهردار شهرک رمیش، اظهارات بنیامین نتانیاهو درباره درخواست برخی شهرک‌های مسیحی جنوب لبنان برای پیوستن به اسرائیل را به‌طور کامل تکذیب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/667163" target="_blank">📅 00:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712f858aea.mp4?token=duynfYm7zT_tH2OWh2D4l8YmvLIdsAl_AHsZJeCzXzy7QqO17ipHCSrl-oQuUIr4Op0jDVeynQ4RqtUh62JcwuL45b90lTeE-0vRAKJ7zPKB_OHWCGnzARjB9m_Pz6OIgMdmsSQZqlVCy8DNS6pYbK_S0K46uldjNqe9cvr70pbdW32FcWLmaKDmgzl6lQMDAogzMpGy9TBbc8MvI3QOFeZL7iwMK0RXpZCJKaPxCrOjlQZEMej1p5h1IJCVhGUsNx4N6g6OrfOvejzzFqlCz8WgpQJ7D2mtJar0b3aM27YZ0HX1yvaFwq7y1MXedbobM4nWb9NWKxfOqUtHj7gPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712f858aea.mp4?token=duynfYm7zT_tH2OWh2D4l8YmvLIdsAl_AHsZJeCzXzy7QqO17ipHCSrl-oQuUIr4Op0jDVeynQ4RqtUh62JcwuL45b90lTeE-0vRAKJ7zPKB_OHWCGnzARjB9m_Pz6OIgMdmsSQZqlVCy8DNS6pYbK_S0K46uldjNqe9cvr70pbdW32FcWLmaKDmgzl6lQMDAogzMpGy9TBbc8MvI3QOFeZL7iwMK0RXpZCJKaPxCrOjlQZEMej1p5h1IJCVhGUsNx4N6g6OrfOvejzzFqlCz8WgpQJ7D2mtJar0b3aM27YZ0HX1yvaFwq7y1MXedbobM4nWb9NWKxfOqUtHj7gPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شنیدنی کمیل خجسته، برادرزاده همسر رهبر شهید از اهمیت دادن رهبر شهید انقلاب به نماز اول وقت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667162" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5v-3KWaVi2QBR6DxJZZdW8aQG4SyjsGwUn7AwgX93sWwRjsabtAzniqYsC5lp92xztaUFKWZkkl2Tib-uEq0guJGYlKh_0LmdSMaJ6h5xRQhdthldUCk0Tdb_MaHM2alsQTr7DathpqIo34WD-Fg3wVDwS4KP2mz1M3qPQK3M75YB06k-AV5nDMAiVT2Xj1QyqR1N_PY9YNnzOjCPU8X3IrGStNMYWSHJQuCHs0jN8TO0IpebcG6Q0fnq9vTYG5KrxThzML6b3WzywMVUO0rAgF8EMLWNo_jLFnjATGPehG9wW5jiAO2nvn_4aHZAUCqDvC0Dq-Sb-ogQmdtiOzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/667161" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد! #جام_تایم۲۶  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/667160" target="_blank">📅 00:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
حضور فرزندان رهبر شهید انقلاب در مصلی تهران پیش از اقامه نماز بر پیکر ایشان
👇
khabarfoori.com/fa/tiny/news-3227938
🔹
نخستین تصاویر از بوئینگ‌های ۷۷۷ عربستان که به‌ تازگی وارد ایران شده‌اند
👇
khabarfoori.com/fa/tiny/news-3227986
🔹
پدر شهید ۱۴ ماهه بیت رهبری کیست؟
👇
khabarfoori.com/fa/tiny/news-3228074
🔹
شرط رهبر در جلسه خواستگاری از دخترش؛ شرطی که شهید باقری کنی با جان پذیرفت
👇
khabarfoori.com/fa/tiny/news-3228078
🔹
عروسی تیلور سوئیفت روی روان ترامپ | جدال رسانه‌ای بالا گرفت
👇
khabarfoori.com/fa/tiny/news-3227857
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/667159" target="_blank">📅 23:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=qFb-wP_zK859djjhMDfantqGjBzDXQJ9Ks4twKcyZPvrUeh68Avs8pu8tuNusCIxQbYB8uioReHNUBm-Rby2DfO9tktVGl8Zqf8tW3QcbDRzE_biSKVy2VgCvTHHqwr_feGVfa4q5PiRTaJTnx4SVLC2zE1c9eN97WZAj7Tg6TMSXZ7eRpBqk7pUx6P3vPMIg9qC3kbkubH7W7K1xyDd8PjQgxz_ok3b1DYH9b7X8ioSCmZMKuyP3Ec9B3dg5atVAE72g1st9Eml9M-tiH9tBt7afvn66t9T4h-xrrQXklyjQJIt7FtpL7D7Z1_7c0mNE3wpD2hIRA-54qTlsm8QTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=qFb-wP_zK859djjhMDfantqGjBzDXQJ9Ks4twKcyZPvrUeh68Avs8pu8tuNusCIxQbYB8uioReHNUBm-Rby2DfO9tktVGl8Zqf8tW3QcbDRzE_biSKVy2VgCvTHHqwr_feGVfa4q5PiRTaJTnx4SVLC2zE1c9eN97WZAj7Tg6TMSXZ7eRpBqk7pUx6P3vPMIg9qC3kbkubH7W7K1xyDd8PjQgxz_ok3b1DYH9b7X8ioSCmZMKuyP3Ec9B3dg5atVAE72g1st9Eml9M-tiH9tBt7afvn66t9T4h-xrrQXklyjQJIt7FtpL7D7Z1_7c0mNE3wpD2hIRA-54qTlsm8QTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان: اگر حال‌وهوای امروز و دیروز عاطفی‌تر بود، فردا حماسی‌تر خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/667158" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f653a1574a.mp4?token=n3L8kclby5DIJVI9CXcn-GmM7WDG-5iLgCM2Gy10gMls_l7tpAfyqCY0VrTd_VQxZuZNQMokNYuCpzrDjy7sz0_zRgFhJb2NfxmgBifLo5KJnnxE9QNQz0I7kpAoJhRxxtByD2kcFj3rC0-wPfe6yEJd5CtXTkYe5Sgu_rYUl13qVibA_zwR3rcpC93H7mAkUDYMnN5okQFQvnj8zUWIfUPe4b9wv0a7_y5psMB0WNN7UPw0WH8cbDVjvNTpw8FOrIRW_wOVfhF97Dtb2ihRpeNOdio6wIc9vpdDFWtCCUqJmyhl9MIrozxAXLJMEnRTO4Ji3LJQeVpHlISCfPuOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f653a1574a.mp4?token=n3L8kclby5DIJVI9CXcn-GmM7WDG-5iLgCM2Gy10gMls_l7tpAfyqCY0VrTd_VQxZuZNQMokNYuCpzrDjy7sz0_zRgFhJb2NfxmgBifLo5KJnnxE9QNQz0I7kpAoJhRxxtByD2kcFj3rC0-wPfe6yEJd5CtXTkYe5Sgu_rYUl13qVibA_zwR3rcpC93H7mAkUDYMnN5okQFQvnj8zUWIfUPe4b9wv0a7_y5psMB0WNN7UPw0WH8cbDVjvNTpw8FOrIRW_wOVfhF97Dtb2ihRpeNOdio6wIc9vpdDFWtCCUqJmyhl9MIrozxAXLJMEnRTO4Ji3LJQeVpHlISCfPuOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آستانه سفر دونالد ترامپ به ترکیه برای شرکت در نشست ناتو، گروهی از فعالان ترکیه‌ای با نصب بنری بر روی پل هالیچ در استانبول، خطاب به شهروندان نوشتند: «کودکانتان را پنهان کنید؛ ترامپ در راه است.
»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/667157" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b7d7fa8c.mp4?token=tmS6lrjVCOYIcIzOFPPysnXd8mH8kraofYIs1ugIqExw9rWjcDtiBLzDhX3PXSdXFnpG69FGAkj0PDmF-KEYhRMmrcD2h164W2Bf7Vp_0RC16IJUDZqpwCJdwHYrfztFt0pEMUIgPtby0bp7xxOID12xpWeyY7DxK9fqla1Qp1kyY3S81infx-FBH2HMz9y4bIFRmnUUxjkCoDxSSXLNPQxpN7TYu5Eu7k3MSsZ7_ISKWasa6jJ37hkp1GTpvOkA-i_yYefyrkXRTN5l3aBgr8rNZ6iwoswlSV1PKS4dAkva1MEH9FWqacnIBA6xs37EvvkYRExn0WffFSqUwX6IFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b7d7fa8c.mp4?token=tmS6lrjVCOYIcIzOFPPysnXd8mH8kraofYIs1ugIqExw9rWjcDtiBLzDhX3PXSdXFnpG69FGAkj0PDmF-KEYhRMmrcD2h164W2Bf7Vp_0RC16IJUDZqpwCJdwHYrfztFt0pEMUIgPtby0bp7xxOID12xpWeyY7DxK9fqla1Qp1kyY3S81infx-FBH2HMz9y4bIFRmnUUxjkCoDxSSXLNPQxpN7TYu5Eu7k3MSsZ7_ISKWasa6jJ37hkp1GTpvOkA-i_yYefyrkXRTN5l3aBgr8rNZ6iwoswlSV1PKS4dAkva1MEH9FWqacnIBA6xs37EvvkYRExn0WffFSqUwX6IFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر دفتر شبکه الجزیره: مراسم گسترده تشییع رهبر شهید ایران پیام محبوبیت مردمی جمهوری اسلامی را به دنیا مخابره کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/667156" target="_blank">📅 23:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=k6xpp2cNi2ibIVOg04Xth41B9VSGGC6xX1MmG4C4k4vVEdhIaWfO9O8T_Ztum56e-2ccZeltzwJ0nACK2oqFNYZdXL5xvPGD7BcrCUUlRVX8weH7VK7CEW4Sfr4tZ4ps7Nh80Yedqcfu8tVpc2rwWJcEOHvZRhlVgggRpiBFGMZgT44w3HB3Gvq0qklM1m6s6JGCGsH7O9hACsrd6cLHDtV5T7jkrxDxeSdpd25pJny2UEMvdqY_RGUNQYRitzKu6rNrbjSAhv8vKUrR3DftA5RdkGK9dLcmF2HfGrg648joU1h3izSGzNVwkWcrT58eDwgUf5_nMaf8qzLjz05lkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=k6xpp2cNi2ibIVOg04Xth41B9VSGGC6xX1MmG4C4k4vVEdhIaWfO9O8T_Ztum56e-2ccZeltzwJ0nACK2oqFNYZdXL5xvPGD7BcrCUUlRVX8weH7VK7CEW4Sfr4tZ4ps7Nh80Yedqcfu8tVpc2rwWJcEOHvZRhlVgggRpiBFGMZgT44w3HB3Gvq0qklM1m6s6JGCGsH7O9hACsrd6cLHDtV5T7jkrxDxeSdpd25pJny2UEMvdqY_RGUNQYRitzKu6rNrbjSAhv8vKUrR3DftA5RdkGK9dLcmF2HfGrg648joU1h3izSGzNVwkWcrT58eDwgUf5_nMaf8qzLjz05lkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت علیرضا دبیر از دیدار با رهبر شهید انقلاب پس از کسب قهرمانی در مسابقات المپیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/667155" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121998aac7.mp4?token=MTA561ewsNKe6MntV6Ej8N_KvuYMoKl6IMiqBHk8cXS1GNHPPtt4_88P1_WiH1dgeCGQyw1DOEIaxlLUOlgDGvMdk_ohoysJlltAjrzwKGByUfuYGv3Q7k-7U6KGPlefv5Y9tXCwPEk5NJvP6GsfTUBSwxKwaz5Jc89ylePLkGNrO4zI4Yd73Uzy4EYZWQ_SDGNPzhNPbRdMbHB2EflkkYJGSGemfUDmZ8CR_zpkHtX46Vj1oX3_ScADy1-oi_funMnI7xZoaR9NkE01Q-zFOJtXqqwkRhVi6fkVqVz1fvFwZAQnsoL7WedTgGH0Bs48T8iZEhH950MxgMoPEkGBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121998aac7.mp4?token=MTA561ewsNKe6MntV6Ej8N_KvuYMoKl6IMiqBHk8cXS1GNHPPtt4_88P1_WiH1dgeCGQyw1DOEIaxlLUOlgDGvMdk_ohoysJlltAjrzwKGByUfuYGv3Q7k-7U6KGPlefv5Y9tXCwPEk5NJvP6GsfTUBSwxKwaz5Jc89ylePLkGNrO4zI4Yd73Uzy4EYZWQ_SDGNPzhNPbRdMbHB2EflkkYJGSGemfUDmZ8CR_zpkHtX46Vj1oX3_ScADy1-oi_funMnI7xZoaR9NkE01Q-zFOJtXqqwkRhVi6fkVqVz1fvFwZAQnsoL7WedTgGH0Bs48T8iZEhH950MxgMoPEkGBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آماده‌سازی جایگاه ویژه اقامه نماز بر پیکر «آقای شهید ایران» در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/667154" target="_blank">📅 23:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کانال ۱۳ اسرائیل: نتانیاهو در حال حاضر درباره خروج از برخی نقاط در جنوب لبنان مشورت‌های امنیتی برگزار می‌کند.
🔹
زلنسکی: طبق اطلاعات به دست آمده، روسیه در حال آماده‌سازی یک حمله گسترده دیگر است.
🔹
برخورد قطار با ۲ عابر در جوارم سوادکوه/ یک زن جان باخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/667153" target="_blank">📅 23:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: ثبت جهانی مراسم تشییع باید توسط دستگاه دیپلماسی پیگیری شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
حضور بیش از یکصد هیئت خارجی در مراسم تشییع رهبر شهید و استقبال بی‌نظیر مردم نشان از انسجام ملی و جایگاه ویژه ایران در منطقه دارد، بسیاری از مهمانان خارجی از گستردگی و نظم مراسم شگفت‌زده شدند.
🔹
ثبت جهانی این رویداد تاریخی باید از سوی دستگاه‌های دیپلماسی و فرهنگی پیگیری شود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/667152" target="_blank">📅 23:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J50Hfyyu0F4XKDgefEXYU7Ty0RSRql3fDLyv3bMtAsDZyFEZOCIN_mOKTQTbMqJa_qHye0th3a_OpCD14Hl79xVZx3tVc4dfQweolpMCND4ttTvw54cLpx82ynuWG6L2hT3ikOQ5gN_BMS-jw10Qfokueg85V30oHKvQ8i0KVwm3oxbOnLsNAdbVjkyO4YOQKfk8cQQBWCBj0L0yKYN_on6NrYRMMUsb5ui1V5BpChZSaSSw-TGmI93wtylX1mpELdNUtqzEvXIfsTFBQ9vnnYv9n_KmfdzCh-lpLFLqApIpwSooSCCuZeM_rgYg1dDMGgxU2fRjQVrWkSNbYuw4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارلوس کی‌روش از تیم ملی غنا اخراج شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/667151" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d850eb03dc.mp4?token=Wos90CHeLBQbk0tSWsxgzQqeT4AR4X-k2kDRJroPdgckDrZG-HOaEE2Bt-KAHmsxHpNx3W6FpqwEpWUMaCI1j9crKgZh-G2u-OtpJMlCqGc2GaUUosMVNk30S5pQrIdPh5Jd_f60zBRcbUn-H95UZXZxmYowfOwHk-LO3ILy0mGT8_SNEPaAZ1jtnwgVcljFY6BGiIBfTWz5yZQjDesCUOi_-d8f43ht8-C2yWPdWWWSNwMDz4v23R3d4JsJoXGl0Jdm8Ll7SAWBK1KH6ZHcdN7eqzvGmCQm3u7VkfcwW2krvp5j8763tYV1cgRxDUfkv5ncF0aCRfmUvBgFChE6jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d850eb03dc.mp4?token=Wos90CHeLBQbk0tSWsxgzQqeT4AR4X-k2kDRJroPdgckDrZG-HOaEE2Bt-KAHmsxHpNx3W6FpqwEpWUMaCI1j9crKgZh-G2u-OtpJMlCqGc2GaUUosMVNk30S5pQrIdPh5Jd_f60zBRcbUn-H95UZXZxmYowfOwHk-LO3ILy0mGT8_SNEPaAZ1jtnwgVcljFY6BGiIBfTWz5yZQjDesCUOi_-d8f43ht8-C2yWPdWWWSNwMDz4v23R3d4JsJoXGl0Jdm8Ll7SAWBK1KH6ZHcdN7eqzvGmCQm3u7VkfcwW2krvp5j8763tYV1cgRxDUfkv5ncF0aCRfmUvBgFChE6jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصول اولیه برای ثبت تصویر ماندگار از تشییع
🎥
جهت فیلم‌برداری را درست انتخاب کن.
🔍
از زوم دیجیتال استفاده نکن.
🚶
اگر امکانش هست، به سوژه نزدیک‌تر شو تا کیفیت تصویر حفظ شود.
🤝
موقع فیلم‌برداری، گوشی را تا جای ممکن ثابت نگه دار.
📷
تمیز کردن لنز دوربین
همین چند نکته ساده، تفاوت بین یک قاب معمولی و یک تصویر ماندگار را رقم می‌زند.
✨
تو فقط لحظه‌ها را ثبت نکن؛ کاری کن هر بار که دوباره دیده می‌شوند، همان حس را زنده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/667150" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2451fa3d0.mp4?token=ACnistwovfI9NLlHRFNRCTw_7L6MCpqB7N8shtm1T03_AWmQ0bxNByh-cUc32kz7U7ctJ8ajAR4n_lsHIj1HVupjMDf5Gp4-bVs5Pocn7F1DfEUacFCmAaedXSNiyIgBQBVuPc1WNigRycfRcfAFN_ldbyIWGyxS5oZEx1uTPIq5yrhKNGB7xaTihb77Zp3dDFl9VsuR9aClbvRjhBNiUcuKcvRDSmzBZD_NuI2COnsAGpSRpaBj-PmYWa51_gfn3HAcaLO-eTSkmf94GtGlFd4Dt5v7H02u4GsVNDGwD9_GFEYJOSdTfALJinuLJTNi3E1GukTpiJGNimUYm2QjQAZcngkvOsYGm8DSbEkddez9JOPKWQ_GymfAgKj8elVwHTpcENq-lWaYPbOpq4c-6kZtx2uAs3EMi3oO9wNSl6Gu9-ZbFKizSGqiOU4BILFCd085QzxK72lPIsES4NZQsrigpB0_N92O__FIbxbtSdoDWRF9I5N_a5XfuoT4yQTsw4oLoBXASzT9q_hHbUseK3XKdb5aZl3ibI38AB_eSBMAGmrzO3FERFWi2m3ctgaI7Vx9e86SG2EbDULTy68wCW5LhzNfZpBWOCVRjN4MvAs2adkXcol7iPLZUpU1pfGzk9LHUwdCOnb5nVm9suGNEX-hLjFmr1pnXJ-8Xi4mRN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2451fa3d0.mp4?token=ACnistwovfI9NLlHRFNRCTw_7L6MCpqB7N8shtm1T03_AWmQ0bxNByh-cUc32kz7U7ctJ8ajAR4n_lsHIj1HVupjMDf5Gp4-bVs5Pocn7F1DfEUacFCmAaedXSNiyIgBQBVuPc1WNigRycfRcfAFN_ldbyIWGyxS5oZEx1uTPIq5yrhKNGB7xaTihb77Zp3dDFl9VsuR9aClbvRjhBNiUcuKcvRDSmzBZD_NuI2COnsAGpSRpaBj-PmYWa51_gfn3HAcaLO-eTSkmf94GtGlFd4Dt5v7H02u4GsVNDGwD9_GFEYJOSdTfALJinuLJTNi3E1GukTpiJGNimUYm2QjQAZcngkvOsYGm8DSbEkddez9JOPKWQ_GymfAgKj8elVwHTpcENq-lWaYPbOpq4c-6kZtx2uAs3EMi3oO9wNSl6Gu9-ZbFKizSGqiOU4BILFCd085QzxK72lPIsES4NZQsrigpB0_N92O__FIbxbtSdoDWRF9I5N_a5XfuoT4yQTsw4oLoBXASzT9q_hHbUseK3XKdb5aZl3ibI38AB_eSBMAGmrzO3FERFWi2m3ctgaI7Vx9e86SG2EbDULTy68wCW5LhzNfZpBWOCVRjN4MvAs2adkXcol7iPLZUpU1pfGzk9LHUwdCOnb5nVm9suGNEX-hLjFmr1pnXJ-8Xi4mRN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کرجی خطاب به رهبر شهید: قول می‌دهم تا پای جان پای ایران و انقلاب بمانم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/667149" target="_blank">📅 23:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=k-FHVMPOkulo1fIw2h7GygSpYSpoA7Wcu1Fxvj2ibucvGRB0LL9IKS-SKFbcNyd9qiOlkvniZ9d1TqV-W7Kq6ApehMQG6emeexLhORnh9d8ouxROBNuP_KW4WPVcMTXfJfhz18G-W5sjGGqab3rxUHrEDdd1Z3UF5HAXUJ5aJvGn8D_nXRHIz7CoFqTnazS0iVfwJInHgnIEew1UFZa-MHuEOsIQsmxxPG2a37SuJLcfWNWAsBy272aB2mWMh1uJYKEx4gVViFm2_YKroiVxg9zMnC5mi3DGQsfgOGIU3YPyTngxuHENCj3I-pj6YJcOD8QMa7j4foTN0OEqCUV7Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=k-FHVMPOkulo1fIw2h7GygSpYSpoA7Wcu1Fxvj2ibucvGRB0LL9IKS-SKFbcNyd9qiOlkvniZ9d1TqV-W7Kq6ApehMQG6emeexLhORnh9d8ouxROBNuP_KW4WPVcMTXfJfhz18G-W5sjGGqab3rxUHrEDdd1Z3UF5HAXUJ5aJvGn8D_nXRHIz7CoFqTnazS0iVfwJInHgnIEew1UFZa-MHuEOsIQsmxxPG2a37SuJLcfWNWAsBy272aB2mWMh1uJYKEx4gVViFm2_YKroiVxg9zMnC5mi3DGQsfgOGIU3YPyTngxuHENCj3I-pj6YJcOD8QMa7j4foTN0OEqCUV7Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام میرهاشم حسینی: مسئولان در صورت تکرار تهدیدهای دشمن، پاسخی محکم به آن‌ها بدهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/667148" target="_blank">📅 23:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429d9e230a.mp4?token=GTFgqmZ8pjNp6Gfw2wAICdvzgB79QDHzyVfyUAziiDBFGcQ3UMvmykHjsgoEjQ0c4YhFGw9Bk_e_8SWA_1BZ1fgSl-_I2C5ucZQSNiVyR0bqc0wbXlE6viOTtHuAxonKPhkisxMdJd8HRVxDkeSmNzcSYnxl8xs2Vk9FFAj4-6Y6R4JQbB50jFA7l1POiLG2cAGdlV9G3dVJRUZIbsTkWHySQbuGBoqGX7Q6LeI43FdPuV6RkE4uLJ0cEoBhf4gL57TDnf81-8lRiGcwMr3PwY-SgZBg0USf0KK81TG3EYyCxddIkVsJNDMG7IPx1O9pnR_6ykfNwzOpSLL-0s8Vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429d9e230a.mp4?token=GTFgqmZ8pjNp6Gfw2wAICdvzgB79QDHzyVfyUAziiDBFGcQ3UMvmykHjsgoEjQ0c4YhFGw9Bk_e_8SWA_1BZ1fgSl-_I2C5ucZQSNiVyR0bqc0wbXlE6viOTtHuAxonKPhkisxMdJd8HRVxDkeSmNzcSYnxl8xs2Vk9FFAj4-6Y6R4JQbB50jFA7l1POiLG2cAGdlV9G3dVJRUZIbsTkWHySQbuGBoqGX7Q6LeI43FdPuV6RkE4uLJ0cEoBhf4gL57TDnf81-8lRiGcwMr3PwY-SgZBg0USf0KK81TG3EYyCxddIkVsJNDMG7IPx1O9pnR_6ykfNwzOpSLL-0s8Vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
️
به نظرت این میز کار کیه؟!
🔹
خیلی دوست دارم با چنین کسی ملاقات کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/667147" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
خوزستان سه‌شنبه تعطیل شد
🔹
به دستور استاندار خوزستان با توجه به موج بازگشت تشییع‌کنندگان پیکر رهبر شهید از تهران و قم، سه‌شنبه ۱۷ تیر استان خوزستان تعطیل اعلام شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/667146" target="_blank">📅 23:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d26df7cb5.mp4?token=jW-8ypI384t52HhU3wKIXAgtc0o87HRDYMU0DqwcwRLjeE83aL9pc8_dB0OoVba3bSkJDuO8Nkdq2L9JS6m8HgSjXSjd5sBsD4L1LN_XjM7MOXaEstRr_gkAhi19oBsQ-_tmONjvTObNSQ2QUWjdi0jZmp-MC9UNAqfnM7tEHstNHCxf4MEJdQKRte69QwJN6UkCknpOF1-aIq5Ql3wKK-8jKg12926FYQwJmESSDKdEwgrFUfAe6DTNaWspDiIRCo35mqBNqO0yiv8IuoifBRRuWaMeT1MQTOsfm_GiHeMVhYIJnuf_eP1PWBDhiUYrQ_vBCuMgmi4M91F78SD9IYjox7H4RaVMhEKsUb5EGj6lCyelu43Zpz9S_oqzl5UuMKpRL4Au8FT33qy7nPTAjUm6URjoWKIvGEQegrbBCcxIpanV_z5riyEkUxcGolsaLZzGKMZMkh4zBHjmLXPxaf90RdnpSx295LrKVgYrkLkWnUHTHOODKtIM58b_AoD3WOKOv8Lif7lAXFLHSKX90ShjHz_4jDQcExNYhjpDDEWm1CSblujF9Bzy-HIJUvZrAjwltPhk-Q4q2q2kzKMmATFPXSLpeLwCBfAl-YjFLlRudOa5ERme8DV2KF34HD_qgBMlJ6Rgf0qw_FcfevfeDn08u6twLtDzTk9VUL8OSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d26df7cb5.mp4?token=jW-8ypI384t52HhU3wKIXAgtc0o87HRDYMU0DqwcwRLjeE83aL9pc8_dB0OoVba3bSkJDuO8Nkdq2L9JS6m8HgSjXSjd5sBsD4L1LN_XjM7MOXaEstRr_gkAhi19oBsQ-_tmONjvTObNSQ2QUWjdi0jZmp-MC9UNAqfnM7tEHstNHCxf4MEJdQKRte69QwJN6UkCknpOF1-aIq5Ql3wKK-8jKg12926FYQwJmESSDKdEwgrFUfAe6DTNaWspDiIRCo35mqBNqO0yiv8IuoifBRRuWaMeT1MQTOsfm_GiHeMVhYIJnuf_eP1PWBDhiUYrQ_vBCuMgmi4M91F78SD9IYjox7H4RaVMhEKsUb5EGj6lCyelu43Zpz9S_oqzl5UuMKpRL4Au8FT33qy7nPTAjUm6URjoWKIvGEQegrbBCcxIpanV_z5riyEkUxcGolsaLZzGKMZMkh4zBHjmLXPxaf90RdnpSx295LrKVgYrkLkWnUHTHOODKtIM58b_AoD3WOKOv8Lif7lAXFLHSKX90ShjHz_4jDQcExNYhjpDDEWm1CSblujF9Bzy-HIJUvZrAjwltPhk-Q4q2q2kzKMmATFPXSLpeLwCBfAl-YjFLlRudOa5ERme8DV2KF34HD_qgBMlJ6Rgf0qw_FcfevfeDn08u6twLtDzTk9VUL8OSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: آقا انتقامت را می‌گیریم بغضی که در سینه داریم، تبدیل به خشم می‌شود، خشمی که باعث نابودی آمریکا و اسرائیل خواهد شد
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/667145" target="_blank">📅 23:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2984b64fa.mp4?token=S_eUBWXbJ0o_50E0-gm9VPI96ExNciN5uTW60E59K2cT5p7sh74jne5C6yBRzANBTIICAjfHB0DJ4kHT1zoN4gSiYIPkzNmjcVOZvsMU_QPB7Z9OmbmLy-JHB7S-KJwGZRetveQcvgqaB3t3kCQK1PuqeCpv9Xm2wRKkWeQxm4JecWUXCYYlXCvYZvQroQ4EItdTSD57Zk3Rfgv665tUoYThYaCL-TYAJ5PY8cQFIgUUI-uogfQbRJuT9xMw6dHiizv8-vQA_P2aH_5_13BzSmJT_kusJ86gT4GkLNu-otNuxe3t08y6Vm6onslMKoTzA5pDpbtJU6c3L3eXZnyZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2984b64fa.mp4?token=S_eUBWXbJ0o_50E0-gm9VPI96ExNciN5uTW60E59K2cT5p7sh74jne5C6yBRzANBTIICAjfHB0DJ4kHT1zoN4gSiYIPkzNmjcVOZvsMU_QPB7Z9OmbmLy-JHB7S-KJwGZRetveQcvgqaB3t3kCQK1PuqeCpv9Xm2wRKkWeQxm4JecWUXCYYlXCvYZvQroQ4EItdTSD57Zk3Rfgv665tUoYThYaCL-TYAJ5PY8cQFIgUUI-uogfQbRJuT9xMw6dHiizv8-vQA_P2aH_5_13BzSmJT_kusJ86gT4GkLNu-otNuxe3t08y6Vm6onslMKoTzA5pDpbtJU6c3L3eXZnyZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیین وداع با پیکر رهبر شهید در دو روز و در مصلای تهران تمام شد و مردم برای مراسم تشییع در پنج شهر تهران، قم، نجف، کربلا و مشهد آماده می‌شوند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/667144" target="_blank">📅 23:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=OIe_nX3h9dZ4ljcukn80wvlzciMIlmkB1EVF3b6nAwNEnlSVKa47qTJOu-OFGdHS8_oTfjn1xnH9u5Y9LqAo1Us_axxcYwyLEyaXn7Tng1KX2aLvv8nLQB56jSlm1lLHcYy552fnBCQoOo5D7QfFSOyjlhe_XujhpH5fsbPlzgYpRJEdv6wNSTY3_XcbvGc6__SW7vJugYP4ZPaLmpegYuCGozI106-DTO2tDyy9-HougmoRCuiSqujORdCGfmGqSS25WA3k5mvPaSw8xqJYyzHkN7ctKyTLQRYnAXbG9tKjH2oDoZKViD19nPJA4nwiUMrD8ImVdqJFO6JqsPDOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=OIe_nX3h9dZ4ljcukn80wvlzciMIlmkB1EVF3b6nAwNEnlSVKa47qTJOu-OFGdHS8_oTfjn1xnH9u5Y9LqAo1Us_axxcYwyLEyaXn7Tng1KX2aLvv8nLQB56jSlm1lLHcYy552fnBCQoOo5D7QfFSOyjlhe_XujhpH5fsbPlzgYpRJEdv6wNSTY3_XcbvGc6__SW7vJugYP4ZPaLmpegYuCGozI106-DTO2tDyy9-HougmoRCuiSqujORdCGfmGqSS25WA3k5mvPaSw8xqJYyzHkN7ctKyTLQRYnAXbG9tKjH2oDoZKViD19nPJA4nwiUMrD8ImVdqJFO6JqsPDOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: خدمات ۲۴ ساعته مترو و حدود ۴ هزار اتوبوس جهت تسهیل رفت‌وآمد مردم در مراسم تشییع رهبر شهید فراهم شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/667143" target="_blank">📅 22:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTkMh-KbjwOjbQIp2cpXH6Qh8gMUhamfgnLPbPMkdEE96xTKf-uHu1sYvXUgEO9Xc4v3yBSYv5eofv93kgMntTSMfwf9JStYaICgEYOzIoXdGXI5fVCeMhGbT-3X-Yi1R_wpSKXeX2GTsOrbWsAwuiZZLnwDDZWQ0HreNa78UdmeznXtUntPfK6iqVmjrvgn4nfaYA4kbBHyXffsgs2zwXBpTW-PsTH5M-xNNvBqOEICS7hmGXCZk3dQ1fqkCCPZwpCROKPLZokalikhQ5J1-4X_zG1M-q63RZHUt_Nj42nORWh-ZamiHBxIRgKfupOoCii75gFD4OCPYJxaZCealQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: خونخواهی امام شهید، آزادی قدس است
🔹
رئیس مجلس در دیدار با رئیس شورای رهبری حماس تأکید کرد دیپلماسی باید با تکیه بر توان دفاعی، دستاوردهای میدان را حفظ کند؛ وی با رد به رسمیت شناختن اسرائیل، تصریح کرد که حمایت از جبهه مقاومت ادامه دارد.
🔹
درویش…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/667142" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس اورژانس کشور: بیش از ۲۲ هزار نفر از خدمات درمانی مراسم وداع با رهبر شهید استفاده کردند
سعید میعادفر، رئیس اورژانس کشور در
#گفتگو
با خبرفوری:
🔹
تا ساعت ۱۶ امروز، ۲۲۶۴۴ نفر از خدمات درمانی استفاده کردند؛ ۲۰۳۳۱ نفر خدمات سرپایی دریافت کردند و ۹۵ نفر به مراکز درمانی اعزام شدند (۸۴ نفر زمینی، ۵ نفر هوایی و ۶ نفر با مترو).
🔹
در ۸ بیمارستان صحرایی، ۱۷۱۱۸ مراجعه سرپایی ثبت شد؛ ۵۰ نفر به مراکز درمانی منتقل شدند، ۳۵۸۸ نفر به‌دلیل ضعف عمومی و گرمازدگی سرم‌تراپی شدند و ۲۷ نفر جراحی محدود سرپایی انجام دادند.
🔹
عمده موارد ناشی از ضعف و گرمازدگی بود؛ تا این لحظه مورد فوتی گزارش نشده و ۳ مورد احیای قلبی‌ریوی (CPR) موفق نیز انجام شده است.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/667141" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aab6bfc91.mp4?token=rbICBQBLIkIgx6In0QSgsnNt-YI1ScpxoCpdxZNVujnhWXZfhYUJA_CcAalz0-NbWt50K7OGKy9MjxDa2IdQW28z4KcxbJEbAG6L7lvIuXcOVN5oGPeRC2UpRxgXXmO_Xld125GEEldHtjXlAvduKPwTz1YjT2hTeg02AbDpfdFGDS154ZLhqtO0oUzLIYqpCE4KhqvxtNn5iBaUWUm9oMMDTMls6Q-sTaZ8d8btV3-Lw_RCA2-dhXocRh8gobrhcwQsXZmZqBq20f1fRBzzemG4sPJX4Uj52cjxB81tSu0iXEI7BYvSFJE0uWxQyd0QMjviHUMLoic2zZNmNVBEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aab6bfc91.mp4?token=rbICBQBLIkIgx6In0QSgsnNt-YI1ScpxoCpdxZNVujnhWXZfhYUJA_CcAalz0-NbWt50K7OGKy9MjxDa2IdQW28z4KcxbJEbAG6L7lvIuXcOVN5oGPeRC2UpRxgXXmO_Xld125GEEldHtjXlAvduKPwTz1YjT2hTeg02AbDpfdFGDS154ZLhqtO0oUzLIYqpCE4KhqvxtNn5iBaUWUm9oMMDTMls6Q-sTaZ8d8btV3-Lw_RCA2-dhXocRh8gobrhcwQsXZmZqBq20f1fRBzzemG4sPJX4Uj52cjxB81tSu0iXEI7BYvSFJE0uWxQyd0QMjviHUMLoic2zZNmNVBEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مرگبار کامیون حامی نیترات آمونیوم در مغولستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/667140" target="_blank">📅 22:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad1acec64.mp4?token=ki8nAtgmer4vZvXf4-zrrI4KCVexK4DFI1sEHa2R-AcylvlWppTx-_nKvkngiCMGG_yqbZyEDPhixOeOEP8gu-k2GSocV5hq4x9NXSGGCO2x_flxpiTRPWvhoqUWubPgCVNL_CzXKvETTvF0rwLzpXSuqXNNv-rrBBvWJNLmQIh8fRtxPcE805_PHgFRx9nHc2VSEJKNB7SYAGAh81Jv12YlNLwv516uGyV3W_cOJD8MmX5oUp2SIkDgveHguHi7WqZRMmW6Gx5B6ll1TNXo-gDLFjtUjdddQqJRGJXNXSmTwl92DoHgD1jH9v6FJPV4SnFHYrv40UtjY9n-f3VGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad1acec64.mp4?token=ki8nAtgmer4vZvXf4-zrrI4KCVexK4DFI1sEHa2R-AcylvlWppTx-_nKvkngiCMGG_yqbZyEDPhixOeOEP8gu-k2GSocV5hq4x9NXSGGCO2x_flxpiTRPWvhoqUWubPgCVNL_CzXKvETTvF0rwLzpXSuqXNNv-rrBBvWJNLmQIh8fRtxPcE805_PHgFRx9nHc2VSEJKNB7SYAGAh81Jv12YlNLwv516uGyV3W_cOJD8MmX5oUp2SIkDgveHguHi7WqZRMmW6Gx5B6ll1TNXo-gDLFjtUjdddQqJRGJXNXSmTwl92DoHgD1jH9v6FJPV4SnFHYrv40UtjY9n-f3VGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایق پایانی مراسم وداع و خداحافظی جانسوز مردم با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/667139" target="_blank">📅 22:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=YHVdUTkcy32MSpJhxew6PFYXuOvlR4J8t-RMecv1eUQtcPxgXA5RZOVghYKcCKE-l1gIZmH6rVucJBhy9FAYgI4ybPLbdd8X27B4ntOEs1t_KZkClbhFY2L9N6Ba7G-cMuVSX_8im107X9hlI4LtXS-cVSOEKk_Qd5yFnD04z8TaXyFIkoM3y7YRn7lhBh1fDstqZ9jEk3-wn8bml1tapDtT43c9-_UWBju7lbWynXfrcE71OuqgUY8NXr0eMNx6VRsIr9rVc1TAm_y4A2x4bX7z7KrIU2IUWmP5rKwEARnm4EcEcHwM1BfdgEvHob7q7RaDozKiFE_He7tMPsX02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=YHVdUTkcy32MSpJhxew6PFYXuOvlR4J8t-RMecv1eUQtcPxgXA5RZOVghYKcCKE-l1gIZmH6rVucJBhy9FAYgI4ybPLbdd8X27B4ntOEs1t_KZkClbhFY2L9N6Ba7G-cMuVSX_8im107X9hlI4LtXS-cVSOEKk_Qd5yFnD04z8TaXyFIkoM3y7YRn7lhBh1fDstqZ9jEk3-wn8bml1tapDtT43c9-_UWBju7lbWynXfrcE71OuqgUY8NXr0eMNx6VRsIr9rVc1TAm_y4A2x4bX7z7KrIU2IUWmP5rKwEARnm4EcEcHwM1BfdgEvHob7q7RaDozKiFE_He7tMPsX02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: حضور میلیونی مردم در روزهای اخیر، نشان‌دهنده دو پیام روشن است؛ نخست، وحدت و انسجام ملی و دوم، تجدید بیعت ملت ایران با آیت‌الله سید مجتبی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/667138" target="_blank">📅 22:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc53a66083.mp4?token=SWy-yxBYS_-M_5qAnHjHoej7WEkwoi0dn9ItpvAm1sfU9W--K4SWpvwdOXL3E6e7mC7Z8-KnUsrABxtUg5A11FlQgTvYUVRCt_KwYFeZRL_71ziNtxaBlAn_Yi5QqfLX6IqBM3G6ZoKmRjJTZUwU0BU7VGGw198BgR8Y82db4MljF_iQGXGiDsNkHM9gLkiTZV4DoHc2yQZVz6N0AULlLULDb36APmwdE-BxMwwLk6VkqhxDB3GrIzrmTgI2PDAzkrSOx0E4_XdH4HrwD2oQAVt16uOmWjH16wZDuq9Kxi4yKHucD8CEhZ-hI3DOIGDP9hQ4Tb38m1qHH9vpO8o5CFRVnontnu9ccSsu7cO3PToNu9-NBgxWmwt032leA69I52IIhgVmx_-64veRvhRc8V76rLUNsiP1X8HOSdrvWVOjbFRvjJ2eFwqD5IiE_tThjSr4p4qhIcB1Q8_9DdG7FSnYaWVW9Te8jBCisJelb87DqYtARCA6KhNBjpPI00I5J5icmWMbpAKNPiPWNDUK0Eq0RD2DyQYVTvYB4wIgnS1uAV4CsM4q7sOZXzk4k9JF9GmSrPqbvZqleRTQkA4rVJezfXZKjDIxZzuiSgKZ7g-e8NLE22owVyGwyHkQsYUQMlsXTXXwKgtXyFGMgkiw3IqbFx77t-2KlDqSZfv2MtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc53a66083.mp4?token=SWy-yxBYS_-M_5qAnHjHoej7WEkwoi0dn9ItpvAm1sfU9W--K4SWpvwdOXL3E6e7mC7Z8-KnUsrABxtUg5A11FlQgTvYUVRCt_KwYFeZRL_71ziNtxaBlAn_Yi5QqfLX6IqBM3G6ZoKmRjJTZUwU0BU7VGGw198BgR8Y82db4MljF_iQGXGiDsNkHM9gLkiTZV4DoHc2yQZVz6N0AULlLULDb36APmwdE-BxMwwLk6VkqhxDB3GrIzrmTgI2PDAzkrSOx0E4_XdH4HrwD2oQAVt16uOmWjH16wZDuq9Kxi4yKHucD8CEhZ-hI3DOIGDP9hQ4Tb38m1qHH9vpO8o5CFRVnontnu9ccSsu7cO3PToNu9-NBgxWmwt032leA69I52IIhgVmx_-64veRvhRc8V76rLUNsiP1X8HOSdrvWVOjbFRvjJ2eFwqD5IiE_tThjSr4p4qhIcB1Q8_9DdG7FSnYaWVW9Te8jBCisJelb87DqYtARCA6KhNBjpPI00I5J5icmWMbpAKNPiPWNDUK0Eq0RD2DyQYVTvYB4wIgnS1uAV4CsM4q7sOZXzk4k9JF9GmSrPqbvZqleRTQkA4rVJezfXZKjDIxZzuiSgKZ7g-e8NLE22owVyGwyHkQsYUQMlsXTXXwKgtXyFGMgkiw3IqbFx77t-2KlDqSZfv2MtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاموش شدن چراغ‌های مصلای تهران و آخرین لحظات وداع امشب، با روضهٔ حضرت سیدالشهدا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/667137" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ویدیو حشد الشعبی درباره تشییع پیکر مطهر رهبر شهید انقلاب؛ برای خداوند بپاخیزید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/667136" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
درخواست رئیس ستاد تشییع تهران از مردم برای پایان مراسم وداع در مصلای تهران
فرمانده سپاه تهران:
🔹
با توجه به لزوم آماده‌سازی شرایط برای برگزاری هرچه باشکوه‌تر مراسم تشییع قائد شهید از مردم عزیز تقاضا می‌کنیم ضمن همکاری با خادمان خود به مراسم وداع در مصلی پایان داده و اجازه دهند تا فرصت کافی برای آماده‌سازی مراسم تشییع آماده شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/667135" target="_blank">📅 22:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02553b7c3e.mp4?token=HE1-gDV5_6PI5xddjOvoQ8-3QH6C_rY0QcoZ-dKhQDyQm2WZLOVSuOQvV1WEBHBbXVLgOvGzVBxJhkZtn-i3C68-G0pG8pBySsDWiX_6Nc1Bq96dgv-VxQ_YR1SBsEH24qFA_ZMTqYMXmBx_IvDkLleyJQnYQAGnt7CJhfp2rJYsnwZQeCyRim_NgGsSq1LKfiyoPzSbNY05KqvxL-U6vvIUY5NeGCj6WPesZ8aquLsYwX3fgCdl8yaOJU0nx3Vm43Gvgh-u3Q5nASV7AtaIXN2Tn7IlhVKdmnzv0A9FTjt4YazkI6Ue6UMBoYnIhXPzkKH74-RLWp2UUrsrVVFym2w5KVzPV9LpNcMexZAch0EZBSy6Z_dAL_-QpGgmFFyKr-H1E0uDrCzkdKCr8U9DWJ9xIzcaN9pKcqxQhmm6KaFQXWvR-LVN3v1_EHouQt4CE0ho8TCA36TPNiLvGcLF6WU569hxkao2jlscmhXuGEjqlYqrhTYEm_VstkQ_w73_-YcfAKYnBzKnBw0mxGffjkX_odAQ9UJkwJYbTNUz50hJcFSWa3VlHbkJdjWPhtOxx3fwJr9X4SZsj0Jx61XlIIrbi_OsUDTAvdb_Td1GW6DRgeuLgO0mkKBs-D9w6cpUEEo4a2cQZCVRHNVBXy9L1riNYvnQ-lHoht-ia16JiYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02553b7c3e.mp4?token=HE1-gDV5_6PI5xddjOvoQ8-3QH6C_rY0QcoZ-dKhQDyQm2WZLOVSuOQvV1WEBHBbXVLgOvGzVBxJhkZtn-i3C68-G0pG8pBySsDWiX_6Nc1Bq96dgv-VxQ_YR1SBsEH24qFA_ZMTqYMXmBx_IvDkLleyJQnYQAGnt7CJhfp2rJYsnwZQeCyRim_NgGsSq1LKfiyoPzSbNY05KqvxL-U6vvIUY5NeGCj6WPesZ8aquLsYwX3fgCdl8yaOJU0nx3Vm43Gvgh-u3Q5nASV7AtaIXN2Tn7IlhVKdmnzv0A9FTjt4YazkI6Ue6UMBoYnIhXPzkKH74-RLWp2UUrsrVVFym2w5KVzPV9LpNcMexZAch0EZBSy6Z_dAL_-QpGgmFFyKr-H1E0uDrCzkdKCr8U9DWJ9xIzcaN9pKcqxQhmm6KaFQXWvR-LVN3v1_EHouQt4CE0ho8TCA36TPNiLvGcLF6WU569hxkao2jlscmhXuGEjqlYqrhTYEm_VstkQ_w73_-YcfAKYnBzKnBw0mxGffjkX_odAQ9UJkwJYbTNUz50hJcFSWa3VlHbkJdjWPhtOxx3fwJr9X4SZsj0Jx61XlIIrbi_OsUDTAvdb_Td1GW6DRgeuLgO0mkKBs-D9w6cpUEEo4a2cQZCVRHNVBXy9L1riNYvnQ-lHoht-ia16JiYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرده‌ها بسته شد و پیکر رهبر شهید انقلاب صحنه وداع را ترک کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/667134" target="_blank">📅 22:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تعطیلی روز شهادت رهبری و تشییع در تقویم ملی/ سیاوشی: ثبت تشییع رهبری در گینس در دستور کار قرار خواهد گرفت
اسماعیل سیاوشی، دبیر کمیسیون فرهنگی مجلس در
#گفتگو
با خبرفوری:
🔹
روز شهادت امام شهید در نه اسفند یا روز تدفین یا هر دو به عنوان روز تعطیل در تقویم ملی ثبت خواهد شد و این موضوع در حال بررسی در شورای انقلاب فرهنگی است.
🔹
قرار بود که مراسم تشییع علاوه‌ بر کشور عراق، در کشور پاکستان نیز برگزار شود ولی به‌ دلیل برخی مصلحت‌ها صرفا در کشور عراق برگزار خواهد شد‌.
🔹
در هفته‌ای که صحن علنی مجلس تشکیل خواهد شد، ثبت این تشییع باشکوه در گینس در دستور کار قرار خواهد گرفت.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/667133" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9295861970.mp4?token=otzezvGHGonPn2bUmqM9ICxB-iSkwcf0k3zwVIutGLgjO9uCfFyRQQWRl7c-tznYpMKE1roy6_tVVp0krmTxJ0Es1FPG--m5FrLN8BjU6AGdxW9Jl1d87aqWSQ9rIjiPht0Y-c7lew5wuyjQygBANQYV2Vznu_1dsbUJ8XLYn_hycEqsi8Vxz2l47lHv_dI-4pwk-7_dlCtJRgwaSzRAghZRkNi-c6Tb5RxnReDH9C8_yTmIRj2mUdiKzyt1wie6Wlw8ZZD39Zg69HpIzCGa-b8Ztn2axhWO3VT62cCnEuWVDSexYQWj_EqKwnF8TRqjjkNaz7LDhq8zTIUBMzX2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9295861970.mp4?token=otzezvGHGonPn2bUmqM9ICxB-iSkwcf0k3zwVIutGLgjO9uCfFyRQQWRl7c-tznYpMKE1roy6_tVVp0krmTxJ0Es1FPG--m5FrLN8BjU6AGdxW9Jl1d87aqWSQ9rIjiPht0Y-c7lew5wuyjQygBANQYV2Vznu_1dsbUJ8XLYn_hycEqsi8Vxz2l47lHv_dI-4pwk-7_dlCtJRgwaSzRAghZRkNi-c6Tb5RxnReDH9C8_yTmIRj2mUdiKzyt1wie6Wlw8ZZD39Zg69HpIzCGa-b8Ztn2axhWO3VT62cCnEuWVDSexYQWj_EqKwnF8TRqjjkNaz7LDhq8zTIUBMzX2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام رحیمیان: تنها مسئولی که بدون وقت قبلی می‌توانستند خدمت امام راحل بیایند، رهبر شهید بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667132" target="_blank">📅 22:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667122">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf6YoVQk6FfUNG9Xk0vAo4qtkUkeV3YAq73sZOiKLzxdrBU2Ym_Q-Kf0hvSDNB-Jyw8oCBYj19kkS5CdkyY2A33Ibv7MBfG661Pz2PRFTz1xnr-4jOVydS_Vl-FiRtY99-nieKikR4SWMl7CoXuZuBhqkS0-tSmi1atlUeWM6md38aMCcLqTlo7KYAsjyxYL4KFUVGZabpZuTd-Z99IwjIr23MwMdTzNtL1on_I9UFq0-PNGdPz-lWbbirgre10pK_SGIx-hTPWZRW63zKvQA2b9KWe0kusEdwdXqyovwsSyOcto7LcNqUNk8v5qRqRfGzwUfGtZFzjlBEcwedPRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmPO5Um6d2PHpFx6DQJ_vWbAjGXoqFpCEjspJJhn93NOu76y-Erx5h2R2__EswzjVo5MpLVgBx7xDWmAoF9AtuR8UWR1uVVhEk00e6SXgepgyG_uSHdikPUuOcg6w0unvu1Sz4A-2PfGs_csPSWdpKbX4W06LBICbRaU_osq85qo5ObhLtCFsD72L5gELrnvOeDIiset2BwurUZl3YO7AIx7TKngig76AtfEVGEO7g0QES2dyTydgSFoQWacZA0YwLoBJlVV5dcL8-jVaKXdisg_w6f5ouFW7MHZuMUAHA-LzzSaCTvbo2cMkZzLIKk0_-yLSSrRA3StiRxET0K90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRSIEQCY6NdWlrdLuS8rCau_VLo_XF8lN8GdDG7p1tRLPm1NIV4A3T0QZIHqMHiCuqKOU5f3ePgkmQWZjAdO6OMNqxq0rc-KM1cPGbsX6VnwofBQkTAtwr96F1Hz8Pir7iner-RNKHpeNzLq-ZT5N3vTY_G07c6OxCMP_EDXXNTIvjzLdYZBE0bHZ85C-BI3XOL0ySVRmGgdNvuc3oQzE9IDkMUHt3nneppvaGpAGV2e62Tpz-O08oBCB21-3Qy1ET3qT0tU-b1By4jQHFsDUNbyYDQQvGn7byu6CjH0xuqtzIsIlZpRY54jsQmrNMCbEy1ZmOiuR-L06sikZcdHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMkLji38lxzj3DDJRk59A6eZCufEpdTAQv5scVsHBhEEszq2o_1BJoeDX0bIG1uCEoeS8nFU5P3gd4dX8jUAM8Vx9oxoqhEP7zIFVk9Y1lvHm-GiztY81oAgnNC7ZhtH1hz3Z0DhwGsVZofOBZdByv8iE4xhA6nSa55A1QdxfBVjT_ABIGHZlsPeDvRYLWqwahjucul6Ry2z11KP-L068fPfywKThgxVxYuz0fAVWdKeCBZlTPFWfr3f6NXqZ8vFkAgc4UWLIiGG_vZfBjPlAiWJLxtwA9lzTfBRliUyyMPvROjvM6ucJScVSx1X5CoDqNZE8F-uNMERsg4ZqqRzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_yzThXuUO9rX9FaTM2AMCdcBAyu42KPKuBl3AJvxryi-ZUfH3CEDVDCWtFBFUY0f8ln3J8CDgT1LlNiM3QQfxVlcPiKcB4CLr8rxRqR5s3XObvpK9VKur6iV67IaYmPULb_GKSfQKweiXMj93MXaKB0EqTQYlpOWd7gUSQ7UkV1-y_dpBXl4JBJ7dqW6511UMvNMMQQmGbx8rfa_tai8sK2bQBwJBQXqb7M_F9ax-BpuC_wkjn0TGEYtRsEg4jETFTgJE2o15DX140OPZimsNf6yheaU5zY-pFTEDMdAHa7GoufYbq87sk1pe493vRFj2PToFVrmdzBtzvv6X9VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSsiwEaVSAyUec6ui2mWZ1SKqDiK0LFHSkXMNBgwKhXjTSB0GzoI9uX1SbAtr_KGhOJDq3EWMpo2SsITSTCx5afUstwzhnLtmsdIzydQY9QUbP5SBTvkvBgg-zMi35suR8J8tUZdDCQZsgaU-KwzcpOsIUpOR7uS2uvSTRnxDHUEAdybSMan1F3sRe92-CiCNVcOLcGJ2BQVMhns9hwjIsuG7EZvjvGv1mXddGnSCVobCad18h_Fgc4uc1b1apzvNXEPVg6kCASA190-1XLRI-DRpT-R9l_xZKhhL0IsheCL_aKDIlyKsGg0xhCZ4VfN5yC7uwGo1odfluvCY8Ur6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJEc0hbEowqh-kUoYOhWgYCSqLIB28FCd9yCtSjj8cKPQl2Z5VsiCzNU_4st3ZFaUVJli3OY9pdgnELGJyg10LBfzJFYgr3glcyUmioBKIoxaPAA56bGkTBxafCHbMRBy2cJtdf8rkNCiaHa99xHEFeAX3_QsoPh-W6PjpiMHWwYramqQ-jSuM4hCHVUlPHgHEWmIOFPSRWfD9qRnFdvPcnmzCZXZ1bO0uxXLJYXDlWOd2retkMTBdc0SQGtv-2ISi481BZ4ilj17ZqlIDcef5Qn-I4XSmhSljuIW4uyEvLbDXTgn6DloQx-DRv5gxRFCZ4PZxrYyutJMJoA9BS7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbeCsoJNGEL4P7Tho_pwvBuj64-mZ6JAR9wumB9NP2Jk35CrdsFl3M2v-rP7xZhQmobolLuurgY5NH-UFdLKMfYnzoydz4l3EtxVwV6rSFt4p67BilhpK3i_d4HKsaXRjD-5iCBXMyFlHEjojNLz7po8gvYQV9Do5m6fq5hbe0syC9UIaUobm1kJDgts725E3B1YGgQGYCIWzt6einbVP7UwPDdsUdJvYQjrOLeDTJ2rOFsRLhTI1CQAZ7EJKtMvX4us1OaGxz2zx7800_VPAH017Ht3yl-S32XVcU90Jnh5z8sAO-EP3qAEYvUNqmELMfjCsfPttkIftL3y_z82aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFW1Xwk0YEqCMcF3q-BK4GlrlRO0RlH8mTqCLlHbIMxUkG9pNlG7IHicYsUUf6MM6AhRAcCCon_XYKInIGHlSXEdJ5aE1c2J7n2cS4v1tUY0pNmXymagRlNLlp81C_1fNC9tYy7YO9Lq3R3gT168tvueuYUA8_5xlwiQw6xAp7R0TqjVQUFEe9R7Hnr311UEJQJdXaGnVYcieniDaqyRPPEok9aSPVnzNsRua-KvOiqPdcaedO9uAx-FQXGeygQKVzEci690lKP98FzZWD3KSBIkr4bk3jjSoqmp4N7HOD1cW-Ez3WNUFTlDR6gW8ji9EBG_15wA9MZgNKHjvLywBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5c5ok9snbTsop4qd9Y2XNvzanlMSw8MZWYZlCTmZm8o9hgxv5PTbovJJOdU_gOv4Gf0KLEemsAEsfDERiF2wCZrbfwCS9PI2vMUzeP1nG2Jf-yAtQx1Pd7Se6-Vdgt16eDJM3BZtm-Af6QrZ4mdW-HrAzNTwanOchwtTvyXCK3noBI146_wA_eI7l5igwhzv1sTAD0wjU_mVrOQkwxSlT4IoPkvnUlze3gYqHrAue1UojsTc61kou4fx0ZRFAO82AD6ByImCO_l4O6S87rP43utSnrCcJhQvjvDJT8JS3Ovi6AvSJLm5tzBnUVwf6fQu1Klz4xV08LRN-gMfbji3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از آخرین قاب‌های وداع
🔹
عکاس: زهرا دمیرچی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/667122" target="_blank">📅 22:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elzqj789zpZ_BcfQmVwB5634ABlatec7q1ll6_kN0AiG7tSPaQREQLmUVvmMwFWqwtmr5_mcIXbOJDZpCZeCyJHSuaSfRafE6mzSfF2RW8LhhDrxE-Zda7mbImxIsKYFrU4dKU1i3p4K__PSp8T0MmRlahVRxKsosSBGugRYxPPHpFfCNDFSOVllLZez9Ll_ivcQVxQx_yPHiCdlSmvnyzCp8jFa4neYVv47_pQepcjbfw1ZButzCTm0bPcegezh7jmyDbeMjIZvKhk5dAYUmhFJwylQo5JIDL_vA_qn0tDDeMp7aM3rmXdzHjgiYlin8i68AkZ4z72JQFM1EjKxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت نوجوان ۱۶ ساله فلسطینی در اردوگاه قلندیا
🔹
وزارت بهداشت فلسطین از شهادت «ولید ابوسنینه»، نوجوان ۱۶ ساله، بر اثر تیراندازی مستقیم نظامیان اسرائیلی در اردوگاه قلندیا در شمال قدس خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/667120" target="_blank">📅 22:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB-g01J3o0U5_smbmIAntynJ5Q6MCWpTPrGL-rv0kFR253NyG7SwVkVTPV0agXJOyP1sLS8RnkdWrEmm7bi1hMgVQ_uUqDR_Qw0UoxDcvKCjpTI634Ev__7kUFEfFlN3FlMZyvMgirN1z5u-Cm_BmFOJ3SXBlGYskerkUJEGdlvQTLzglxsCzW5T9kf1-XnsOwEGfcUVftcuS7phd4QMAmtyhEw5UT7X88xdd4I9jnpATSBGf7uu1sT24sT44PJFRVHY3U25qs0gaDOmIQGBfud1qyfzOJID5GJYAgFEiS26UgvWlEut73C10sD5ab3VbG5nQ2MgBOw6Rj5C_uAX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/akhbarefori/667119" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTX_zlrJ7ieHjG6uM09oVrVkm9T-iqydRjIq89P5IS95ct_wIP0AxWe8PVPoq9ultzTo8SZj38FrULOAgf2eZuO-pngYS0OY9MH1GZsO0k3e5H2Wm3eTpcJAKB71ukEXQWehCmBxL7Ybj4vk6mkDbqsmpngASbX3I6v7-7DU1wP-rnRPci9VrZ71J8jlgjFgPguO5Jq8o994YmLZkix-HX02lGLrXrt9Rc1Ul0TCsd4n23H_a-knnJO4rgWlf332D6BUe-TYIPamLSFk1BweQ5-qTEIpYy9TUqBE0GSvdFMXN6z0aMv99yfIpNrqcm0YEkYPkoUWZ7sCS6ybX1dGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه فرزندان، عروس ها و دامادهای رهبر شهید انقلاب را بشناسید
🔹
رهبر شهید انقلاب دارای ۴ پسر و ۲ دختر بودند: سید مصطفی، سید مجتبی، سید مسعود، سید میثم، سیده بشری و سیده هدی. حضور سه پسر رهبر شهید در مراسم امروز وداع با پیکر او بهانه‌ای برای مرور زندگی آنها شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3228099</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/667118" target="_blank">📅 22:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=jqYv-170fm3JGGarPq4fXrjakL17pSm24TKiA4Nxv5s8F5J0-52sKORqA_ss0ieQ5kmgnq7NgsUuwTguMbRgElusYnqVlgfnsNxSyLAw4dX4NiLi56Uuqzxpg7DIl4unM2U1-LqfK1oWcoNsXqpv3NLYq_cp6SiUL9rCAyU0S1Ryz42jktBGbSlQPUmg9JiWvnY_AS9Bm-dfr_6E1MpJMroMOEkVzBDoPBK8va-vLZPiN0MuOFb6bpHixW9sRsHikuo-pG_COi17e9x_ixoJQZbA-ph43VQc3fixdBRiGLFqqGoBrdhICQ4uOShs6T2YwlEkxQBtnC0hiAXRUy1jEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=jqYv-170fm3JGGarPq4fXrjakL17pSm24TKiA4Nxv5s8F5J0-52sKORqA_ss0ieQ5kmgnq7NgsUuwTguMbRgElusYnqVlgfnsNxSyLAw4dX4NiLi56Uuqzxpg7DIl4unM2U1-LqfK1oWcoNsXqpv3NLYq_cp6SiUL9rCAyU0S1Ryz42jktBGbSlQPUmg9JiWvnY_AS9Bm-dfr_6E1MpJMroMOEkVzBDoPBK8va-vLZPiN0MuOFb6bpHixW9sRsHikuo-pG_COi17e9x_ixoJQZbA-ph43VQc3fixdBRiGLFqqGoBrdhICQ4uOShs6T2YwlEkxQBtnC0hiAXRUy1jEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات برنامه اقامه نماز و تشییع رهبر شهید در شهر تهران از زبان استاندار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/667117" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667116">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سی‌ان‌ان: تهران مهیای بزرگترین مراسم تشییع
🔹
سی‌ان‌ان تهران را در حال آماده‌سازی برای برگزاری بزرگترین مراسم تشییع توصیف کرد؛ با وجود گرمای شدید، میلیون‌ها نفر برای وداع حضور یافته‌اند و آمار مسافران مترو تهران به ۱.۳ میلیون نفر رسیده است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/667116" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667115">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cd5a04c8.mp4?token=h4BzrqxtgW86UDHWnINFPWX9Ouavq9qJ5mx28s1IxhXinEMSYAr2-ExNGhbAhHP1-Dm0Vh_43LZ9Po7MFucCAEDBwICgadLDqnGL5qvlq_Ml7PgOG1wucmSV7fj3w9IkJEHEJKWkRnp5vxtzRgLHX9JOhB7Nri5lfpbGKFthImP21ATjrowr-bAHmo7yhApraqwlUfFV9C3efJ5ay6jveksm94r-oLaypfkVpNFTL1echytBXd806yMFQtS1N1k1nRFSgq2AQPY0w_HUhEErbJ_rGp2D5-Bf_nc08bDpdx1OLR7gx2z_ieZVwAIDXfCYFcnj1rCP4gs3cXXwef_2pC_lcmCySPoeZg9gMqN7f_v5jBJ7Y6ejwJ5mkuwah0dtgkWu3yHHF815lUhCFVaDCY32QvEE_EqFBUr5_uMmhLQzt5AZhK9X0P3HHPVRz7l3W0Ib6_-rdev36Fvg7Gwa3IJ_3SA7J0B9tDCs2T-UQqFr6yxY0tcX5Ro2toiebkjRGI6dWX6-k_WPp5iiwB9kZZPlWYy0z7xuJ0hV1bY_j5Sw4Xi7rTH9tOp-S_lYYcPyKXm9oChoM1mVcEkfdQqNKiejYCTcq4Y9N-1pij6xGvMgbfW3RUFNUIxzkqp1FBw-8y8eIBAgpE90TT5i1qtHULSwrGwx4vEBpTpiV_9IzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cd5a04c8.mp4?token=h4BzrqxtgW86UDHWnINFPWX9Ouavq9qJ5mx28s1IxhXinEMSYAr2-ExNGhbAhHP1-Dm0Vh_43LZ9Po7MFucCAEDBwICgadLDqnGL5qvlq_Ml7PgOG1wucmSV7fj3w9IkJEHEJKWkRnp5vxtzRgLHX9JOhB7Nri5lfpbGKFthImP21ATjrowr-bAHmo7yhApraqwlUfFV9C3efJ5ay6jveksm94r-oLaypfkVpNFTL1echytBXd806yMFQtS1N1k1nRFSgq2AQPY0w_HUhEErbJ_rGp2D5-Bf_nc08bDpdx1OLR7gx2z_ieZVwAIDXfCYFcnj1rCP4gs3cXXwef_2pC_lcmCySPoeZg9gMqN7f_v5jBJ7Y6ejwJ5mkuwah0dtgkWu3yHHF815lUhCFVaDCY32QvEE_EqFBUr5_uMmhLQzt5AZhK9X0P3HHPVRz7l3W0Ib6_-rdev36Fvg7Gwa3IJ_3SA7J0B9tDCs2T-UQqFr6yxY0tcX5Ro2toiebkjRGI6dWX6-k_WPp5iiwB9kZZPlWYy0z7xuJ0hV1bY_j5Sw4Xi7rTH9tOp-S_lYYcPyKXm9oChoM1mVcEkfdQqNKiejYCTcq4Y9N-1pij6xGvMgbfW3RUFNUIxzkqp1FBw-8y8eIBAgpE90TT5i1qtHULSwrGwx4vEBpTpiV_9IzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب عزاداری خودجوش نظامیان ایرانی در CNN-News18
🔹
شبکه CNN-News18 با انتشار گزارشی تصویری، عزاداری خودجوش نظامیان ارتش ایران در حاشیه مراسم وداع با رهبر شهید را مورد توجه ویژه قرار داد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/667115" target="_blank">📅 21:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667114">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
توقف دو روزه سامانه‌های «ساتنا» و «چکاوک»
بانک مرکزی:
🔹
سامانه‌های ساتنا و چکاوک در روزهای یکشنبه و دوشنبه (۱۴ و ۱۵ تیر) در دسترس نیستند.
🔹
خدمات کارت‌به‌کارت (سحاب) و پرداخت لحظه‌ای (پل) همچنان به‌صورت ۲۴ ساعته فعال خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/667114" target="_blank">📅 21:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a9c5b3a3.mp4?token=jvigH2jGa7WTlUuOCIxzo08j66ZpMf7yj-dTgRj0HL4NvO4UG6W43I057OxRg0MMsIOcGpAEug0pU6-lD6eMBI8LBWRIPc5QpEkbaolKVTp2ib03-7dH3946NjkuJdMT6eiaQeheZdNM-IFk5wSuJlbncCWJxQ9bdw76Oqz58cz5WS8jBkH92MkuVXSzeEhOZKRFAdbB1GDFcuSdLInKqcTiJYKhKNK23f7MpcUhM-3s1KZY7ct5iXec0tz3_aJK9GVSj30EQw8qpnjabVg_Hw5P7V59vOavAbx6TQeCES-E2XQje14YBCXkOG4FKd4NHnKTdrGGZIhXF1lIPirx6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a9c5b3a3.mp4?token=jvigH2jGa7WTlUuOCIxzo08j66ZpMf7yj-dTgRj0HL4NvO4UG6W43I057OxRg0MMsIOcGpAEug0pU6-lD6eMBI8LBWRIPc5QpEkbaolKVTp2ib03-7dH3946NjkuJdMT6eiaQeheZdNM-IFk5wSuJlbncCWJxQ9bdw76Oqz58cz5WS8jBkH92MkuVXSzeEhOZKRFAdbB1GDFcuSdLInKqcTiJYKhKNK23f7MpcUhM-3s1KZY7ct5iXec0tz3_aJK9GVSj30EQw8qpnjabVg_Hw5P7V59vOavAbx6TQeCES-E2XQje14YBCXkOG4FKd4NHnKTdrGGZIhXF1lIPirx6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیتی که تاب خداحافظی از رهبر شهید را ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/667113" target="_blank">📅 21:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024795ab39.mp4?token=Py9kxumtzNCGIKmLhjbbVtUPhJceW0bS-S9FdFuLJxF04lSgFIgRroMtwEM7qrz3Tse_tjgAMcFZjWRw_VDtYbXmooL0JZf0j1RcieMrnHVPm25dz7aluhGatQIr0QjIYZZzNE6EvBkBjAh_MSTx5bNJ4WKfHxBR52yQIZ0_-eoYwCwWUDXQGtP3uAURpQrou3QzLS3Rb6VdWHShkFkRRNdh0z-uJh0gQgXYAvwUVNYlvz0HsP6psDP-bQrNwVlAmuzcjus9hmc4WIRKuAfYKMUaOKDCHkJu0omSpHz8CLyUmyieX0nVwISa65ntowzrjH2FfmBBh_bQGmToE8-WkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024795ab39.mp4?token=Py9kxumtzNCGIKmLhjbbVtUPhJceW0bS-S9FdFuLJxF04lSgFIgRroMtwEM7qrz3Tse_tjgAMcFZjWRw_VDtYbXmooL0JZf0j1RcieMrnHVPm25dz7aluhGatQIr0QjIYZZzNE6EvBkBjAh_MSTx5bNJ4WKfHxBR52yQIZ0_-eoYwCwWUDXQGtP3uAURpQrou3QzLS3Rb6VdWHShkFkRRNdh0z-uJh0gQgXYAvwUVNYlvz0HsP6psDP-bQrNwVlAmuzcjus9hmc4WIRKuAfYKMUaOKDCHkJu0omSpHz8CLyUmyieX0nVwISa65ntowzrjH2FfmBBh_bQGmToE8-WkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سازمان آتش‌نشانی: در صحن ۵۷ هزار مترمربعی مصلی، سامانه‌های مه‌پاش برای کاهش گرما و رفاه زائران راه‌اندازی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/667112" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
پایان مراسم وداع با رهبر شهید در مصلی در ساعت ۲۲
🔹
به‌منظور آماده‌سازی مقدمات برای مراسم تشییع فردا، مراسم وداع که هم‌اکنون در مصلی درحال برگزاری است در ساعت ۲۲ به پایان می‌رسد و زمان پایان آن دوباره تمدید نخواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/667111" target="_blank">📅 21:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fc9fe1b8.mp4?token=b32cS3V2Lu4CVESIxYLjiMPqevnpQvfRz1ZYEiqeIfAQZLO_vJzfHdtoIAzvzxaEnoBRh0z45YxDv4vChh74_uO_TcsHvGmiJVKN0HZEQEhrbJGOzrP4eM1KYCqLauOyR7S25ttIZa4VYwp4jzA_fT6YAhV0NSJJGl6XXlYqaBfBHjCV6iXg8vvj-96caP_r8d7z0nT_GNdACJDjv9kU9WgTvQBiuw6Yai1fqcuZhcP9iupjtTKbqxedYxgfjN2eePN9GEcGXzVIeePGn_R7WSGGsZvYMFIThIn-Jyj5wNRxpAIgPoAbmxruSwbtDsyAAlUpSD53j4YXkpvmV9qjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fc9fe1b8.mp4?token=b32cS3V2Lu4CVESIxYLjiMPqevnpQvfRz1ZYEiqeIfAQZLO_vJzfHdtoIAzvzxaEnoBRh0z45YxDv4vChh74_uO_TcsHvGmiJVKN0HZEQEhrbJGOzrP4eM1KYCqLauOyR7S25ttIZa4VYwp4jzA_fT6YAhV0NSJJGl6XXlYqaBfBHjCV6iXg8vvj-96caP_r8d7z0nT_GNdACJDjv9kU9WgTvQBiuw6Yai1fqcuZhcP9iupjtTKbqxedYxgfjN2eePN9GEcGXzVIeePGn_R7WSGGsZvYMFIThIn-Jyj5wNRxpAIgPoAbmxruSwbtDsyAAlUpSD53j4YXkpvmV9qjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رسم همیشه که در دیدارها کف دستمون حرفمون رو می‌نوشتیم که شاید ببینی و بخونی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/667110" target="_blank">📅 21:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=DNQA7LqYDWVBhusJ5BzSuqyGjRt98LKfZhYnuBmVcf1apptkxLvjkIvUkt7kfz6voEBaZSetCaPRTM4XrtMmQhW6x8pmpBpccFdNvW5xJEFwO-ewfwHeAARszJE5zCKs79Ophnf8twvOBuPsZ1w6ayAscEBxZ4x2-ctbqbPU6XckqktqJI2ytsLmmMeB4ozwvz4K7dR-wJwfd_D2LOAup-CQGOC8QXJNtFgbx5VaV_9nfZVfFwgqfAKm22tolg3rmTRvP4tAm9cqlnfzs_rdbJB-dRftb0W9Dox31NBZHppEQAdqxF-X9AzuStwWzSV4YGQRsMTVJosGY5CPAB6tGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=DNQA7LqYDWVBhusJ5BzSuqyGjRt98LKfZhYnuBmVcf1apptkxLvjkIvUkt7kfz6voEBaZSetCaPRTM4XrtMmQhW6x8pmpBpccFdNvW5xJEFwO-ewfwHeAARszJE5zCKs79Ophnf8twvOBuPsZ1w6ayAscEBxZ4x2-ctbqbPU6XckqktqJI2ytsLmmMeB4ozwvz4K7dR-wJwfd_D2LOAup-CQGOC8QXJNtFgbx5VaV_9nfZVfFwgqfAKm22tolg3rmTRvP4tAm9cqlnfzs_rdbJB-dRftb0W9Dox31NBZHppEQAdqxF-X9AzuStwWzSV4YGQRsMTVJosGY5CPAB6tGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر محمدرضا کلانتر معتمدی، پزشک رهبر شهید: رهبر شهید زمان جیره‌بندی حاضر نبودند بیش از جیرۀ همگانی استفاده بکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/667109" target="_blank">📅 21:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NItlnBB_zSADIwZcRJ6hFd8VL9_1eqKmBM3HXineBrY-ZpFpCowizCb0H8Fsog9IYCucK3-9qmP5lmNDgCA1aektmM6m0inW58M0tLA6DteQgLzg6ShHU_JI8pHzuoGeh1waW4_a2DNiZqeLj3t3VBj1FzLLos1h0xsamzlEJG6yVRbtIdQkF5gKKOpipfRmg-4Lq-XRFol36abZuoRESTPaYVJC_HGBw01L0DVIVCsZ5NEqWjWXK1681-cECcbMKnilb9-qUStl-6ffIt9CFKbToiWes6aZh6m3RWb6hgS025AEVx-zMatynhIf-k8zbH59bLTf4ZUxk7LC1_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اللهم انا لا نعلم منه الا خیرا
🔹
مردم عزادار و سوگوار ایران امروز با حضوری گسترده و آکنده از اندوه، در آیین اقامه نماز بر پیکر رهبر شهید و عزیز امت شرکت کردند. این مراسم در فضایی سرشار از معنویت، وحدت و وفاداری برگزار شد و حاضران با اقامه نماز، ضمن وداع با این شخصیت برجسته، بار دیگر بر آرمان‌ها و مسیر او تأکید کردند. حضور پرشور اقشار مختلف مردم، جلوه‌ای از همبستگی ملی و احترام عمیق به مقام شهید را به نمایش گذاشت و این آیین را به یکی از ماندگارترین صحنه‌های بدرقه رهبر شهید در حافظه تاریخی کشور تبدیل کرد.
🔹
هفتصدونودودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/667108" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
قالیباف: آمادگی برای جنگ، شرط مذاکره قدرتمند است
رئیس مجلس:
🔹
تا زمانی که برای جنگ و شهادت آماده نباشیم، دیپلماسی قدرتمندی نخواهیم داشت؛ چرا که دشمنان با کوچک‌ترین نشانه‌ای از سستی، به جنگ روی می‌آورند.
🔹
وی همچنین بر لزوم همکاری کشورهای اسلامی برای خروج از سیطره آمریکا و اسرائیل جهت تأمین امنیت و اقتصاد منطقه تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/667107" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس از حضور ۱۰ میلیون نفر در نماز رهبر شهید انقلاب خبر داد
جواد حسینی‌کیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تاکنون در تاریخ اسلام سابقه نداشته است که ده میلیون نفر همزمان در یکجا نماز برگزار کنند و این بزرگترین نماز جماعت تاریخ است.
🔹
به دنبال ثبت رسمی تشییع رهبر انقلاب در تقویم رسمی هستیم که با باز شدن مجلس پیگیر این موضوع خواهیم بود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/667106" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667103">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnQjLeM-4QsLOxpFmEE3glWBnsRLHKFPdBjGq4_UoTYEPCeZ9UTdHjlVtX4CXg-yZxYAcE_zAMixb7RmwR6O5CfoCFE7TrPYWw6zhQfMNEPCPFpWWJd3M3RuRWPm8GNy62pv860o_TmQCHMPeP94ApNsQwo0TcQuA1qGHe1rKro8VVFUyXrdNvZXo2ci_tA4Wmi9irzrfk6-3z00uGrROi2V7YvpWesFMuDn-rhfMxAPKBAZtlc3ZagxyeEl2uhC-AfOrbylGDFpJYhEhDgMG8RHi-Z1b-IGCWj_xoieCLp4jX1c-daS6rtWd7MloTVbI4767Sqy5lmRxti7KsX-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
پویش ملی «آخرین دیدار»
🔻
جهت ثبتِ تاریخی وداع با رهبر شهیدمان، از کلیه علاقمندان دعوت می‌شود روایت‌های خود (عکس، فیلم و دلنوشته) را به شناسه زیر ارسال نمایند.
📬
شناسه ارسال آثار:
@akharindidar_admin
🎁
هدایا: شرکت در قرعه‌کشی ۲۰۰ جایزه نقدی + بازنشر آثار منتخب در صفحات رسمی پویش.
🇮🇷
آخرین دیدار در بدرقه آقای شهید ایران
@akharindidar_ir</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/667103" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667102">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
فراخوان مقاومت عراق برای تشییع رهبر شهید
🔹
ابو الاء الولائی با دعوت از مردم عراق برای حضور در مراسم تشییع، آن را ادای دینی اخلاقی به حامی همیشگی ملت‌های منطقه دانست؛ وی تأکید کرد گام برداشتن در این مراسم، پیمودن مسیر تمامی شهدای راه حق است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/667102" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7HrCaDp0EfkSoyc9Mlb7oRLueh1eWnvo8ErYHlTioZgP9H1drdOl_kW3Yo16l2wh_khQjoNxXdR5UovNi4ND7m79gniKi5p2iwArtZMQRaKdbxoa-ACfT6aZWWO8RwH7vjWjvaL63lJP_ZAZvL7p19su-DKm-ARCmQQTVXXepEIhiUtTMg4Vxg73SNl7T16_AFhI7MAyAwugpUrdV5Oq2hlRUKvg2JPDc4olLW4NICj6I7iKx3ael44hQ0Xq0V6wdhLMcM_rGa7mBOCMCxg_KA9SS7WrDxKotwt83xhRlqRucT0UID9MJbZXRaWU5GYRMQEVWfST0t6YAOB7SkRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv6xms9hTsFp6S7gLMyQZlEo04KGmQkZXgPNEsvPkw7c0gPo4iCa59fXvI-YAnd8fsZd2SGYgk1nqG99qXpf2B0NILocoiWyssvWl0o5OXFwg17haeiAftHT8SvnEFMMHana-HKPGUau93kcJP8SoA3eOR2iEftnkuClAsnDsFq7akP00DJgNRTDTZZ8Rd7FUSBuc7VMVq8uxvfyZiivN5gQiUUjzSOjLDaD0GpOikr9OD9zgjF0aCQplz3U1o8vcBzlVpuGzGfHnQD1uRBVLYQkBZiozeJ0KC5oZ47QgnbmjsFtUJXfSFbN7Dapa10opecVGcERrZDrtvlw-tN9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YESQLgquApgR5Nous6mr9m-Q1gHhqZqNSvu6osc8t8iKEdJ7_BCSZyuVc8ClkMOzkQYnVoYAojyrq7a2HDdxpOLIvuuw77aD1bSjK5G1-HY8wf8MTKNNcVKMOFlNRVO9kB4SLxG247w1VSVy9gz1xZJK6k911C4OQEaT4_r4KYsuNOO1WLO-hvxPPMZ5XMRgAD2HYHHuTj9mtNrGYxQpMLNGXJTB9XqqCE9tVd0QFofzjKnfNrZ_BQzx4xbOWxoeVqgOu8ikmZW4ZBD8YTCCnpUR24jzbBc2WH9JqSAdv3B6G2k3FCf0dwo7JoEE5AY0TSyTD5YZH5uJSdlaLI2z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OA4eiEI7KkJaiNMaViJ0H08H_EzyGch0fntl3bbZrDAZTHvZ-TLrq_ccm6NfQqYOVQcqg9fjWasaILKGxYHTEzAXrwGxCtg9z7u-Zr76RbxfZrBz6g_y1XyS7GN4M-0EenGuEwvdj2E3j9VTcal0r535C5JV5lDG0TjOzJpzYaPuGG2w8S4H9L1f31p6FJXNrZEzdAQNvJxeuHIUr-QE3Qkety-nhE0uD4DhFlKFv1egrOL19SrJghYo_STCn4A303o1KS7jeEHP00WB2nVByOGjpZkVbORF88dobdf2MK7YG37NCu376AzKWoWMn3IlToaUnnKwGIU-WciRSDR7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzwXcI3-7wzAvk7qN1NCs8dnb5i6MHweBGyEA6stCH0X6XdWAT3j43UVbN0ZJxaTLIUrp9ACVtg3E-JKM0Eo94pAXJKd78NqwrTk095NhErIT_SMVRja8juCd43L1KHtGj7Hyiy5IRAblnADZpaW2A6mFXw6r-8ngqUGZeVT-vW13AfOjjvpPyMZVcFn0UuSBP0RZdkGSRv2trlazjwVL5t-uyhWb-EE42SFPM7j_OSNwX3-wIlg3PKqn6z9BGINBatlOHlNegXUsanesx2ApVgpJRulZ6fEh7Ec1BjSAIa7CydlnGpn19rX_GPmXsiMB1SsnGF7ds6pg1bnPleSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCQ1q8tXzPKshW9BrwjQhVLARZiyemsnErU-EoxWQv__bAyLCx5ALE5RFUiU_UbNGWmonxqkFsrgCVwINzwIMfMmkwuMS2gFuqF7wazyzFaAEsEIBFZGGJSQEx1XMZTsg7A9x-vzAb0KmbuPPVZr2S6OQet-tuueMoupkCaE2vSNpG7VITIMqJ-2N1jdA0BtNyjrc2_2LeYGpP36yYuZ0vemL2vG4qLtCey8dH6_M8YpwV-23JyZK0n347PzZHrxwoHCqBGbJnx6VEw9fqZ8-H4vtrUXAUSWi_lvkynkJgd6GWw-wfkUF0iHVBZUSm0Hk9HgrDuGu3NcvTIJpCSgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxjy7Xvo2uf550qR_ZqQw8xdh7bt7TuTAP7UlcZPCHwfYCMKKqaLHcmlAKUlpF0gZ88G2zpGz-EGfEMD6yJKLYFacw4l7eDLOO85M2yUi9uiGEk6J_sXHwdKYRRhpi2nlDAEdZlEe_zswi_n0A-O9Pm3ooYYcEmIgmqQgicZVp8xQbktjDLtbao4enfp3euyX-kl-8rjfY5BTJNk15b__Z02TNprZCBLzPpAiponoDWuAhvS_lK6yJ6idQv8AJoCEjkdf6WiP_IsIe0I_8xeqOBq_o_97TDjfkS0PX6XX5dxb2c3w3scIzPNs0gg8SfV590FNE61MWxrAVoHM-nO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMmDXwbrEN4VAk1KMAVfzHp3uQJ0aPERbNOAHjYQ1eF7F-5_w37gx6cKXRxZkmC18_EFA3HEFkfE2pp8l4bNL-MoDl63OXAj0z5ZfsKBkxQDPeNZBPS6OFt7dYvM9YPfvILmLUfOiP4PfC-GtLQiO0Zu56Np0zduKBSe3HKtDx9aio_bTkNpetPBPHUbZOfWftuPDvP7OKhAN77AxoGIGVVt7Az6oGpua2nk7ZQd9GuDS-8OYSDK_47N2vpxHMMuQtU_Tvtoil4c0YQ-KDACxs-m0VNHw085uPJO5Gf044B37hYPk7-lXaiiWabKszn9J39zQJ5EYj2kTslO3inCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWfAkacIAdto6vw9CJrows7PM1fchVbtERt2aui-AJC3Vrx4H_DA5fqKCtzvsB5PctCaGOYk62mcgjf9eSpMOOuC2r7U6nMjNCTDnWGCFfZvuH5xWkDPD2O6LFhOeNrJ9rXLhM7soPTLRdQ0fxXeunK1lv-49BQEIxi94SyvBWC3YxUSFEsDOyiBNNL8xKgS2mdPZ8OgZAT5My_-10oRdtsRTV7uwCUk5VqxNqQZ-m6VvAyjdLLgROnH5GUrG53vkX4To86HNlSCcW8SvwWt5VXTifIEKRZMp7us4BLiLdKliER_ntwaXLHH3mzvhR-m9Q7YgOy4TRCpYnqGyYDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj1tH7KDW04IhzTk--6pe_bj05m15-mOBXVagGoHsSGH3D3dN6Xm0S4wMHmQkaFqZ1PeEFvuKP57hVqkSTz9OoDMDEv8fMhvpfXplNDwRrjVliaoiqWTpVhJyiJEHO9T1SaT1EVYosXtO3u5b5sGBkz1Z-T1QLJHLpveE3d9LgXpfxxwB2N-idNeMvIhAmtnUezT5q8dxaFc37W_2NO1jRDH35JL3Zi8oz93DfdnYZAr6pC_ocDh1Fe1GTugpnvtzVoL86pp4N8P_PLwTgO86l60yPBHKTaNziXngoFRhVTeGXhmFbWLRmP_NLaIjZM--4-zVCicdteWFZxTCCIp9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دومین روز مراسم وداع با رهبر شهید
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/667092" target="_blank">📅 21:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WewQLNVlWE_o1h7klW89EuMF-s2iO07F8fvalUHwgY2J-M9Fy6i92syDqyRwGWwxAsxKrbFq88GhsBOEVzVXv-JkTcEOeYnqWRtKtY8J5Ev8G2z5Z48pPNj-q27i753NcDg0hLlTbes2wJRJFrBDEwlVDZmT9l6pY_johoFE8etv-ZCOp8-DTbLhQ5VtCulHIW6Yb1NfebTN0P4vDJ0DwGl1cvgoudJnRvX9LjtCVsMtOsLuKgSaLA9odmM3ejYNTt9U4c7o17D9Gnw0v0d5z4AK9T32ZO6FeRXZL7mPbypUJHQRKUTEiHgnH6-XGxz_0i46TkJd_Ve4OvGgudDe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی مستند: روایت رهبری
🔹
«روایت رهبری» مستندی است که با انتشار تصاویر آرشیوی کمتر دیده‌شده، روند انتخاب حضرت آیت‌الله خامنه‌ای به رهبری انقلاب را بازگو می‌کند. این اثر با بررسی جلسات تاریخی مجلس خبرگان، استعفای آیت‌الله منتظری، نقش امام خمینی(ره) و مبانی…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/667091" target="_blank">📅 21:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAIRRxuDovesg__AQ-tcl0ZarHanp3fSdbpigkovRlN3gDpwnZT8o-bkHgYfKE_kVkmWLOEuN38MdBi2t7tUt7RFI3bwLKe3UNMNR118TLjs33abbNmve_faaZrqS6cwjgVyRUNW7mh6wIJcr-ieRD_qoy98TxMNnHzY9DR8Crj46tJuwdGVJ0yBZC4EqP-_4cD2AODqFVbkCyoUYH0YHrjAIZA6yN2DGEqQN8KqDrowSTvTwEaNoxmokdHq2H01EOpZe0TvqnopdY-Ird1rXr-SutJNraRMNM_CoV_0M9jpf9OUDsk63LFffhiUz2a3cWoaGq1pXMbU9h5phWhwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد!
#جام_تایم۲۶
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/667090" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667089">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
زائر خوزستانی مصلای تهران خطاب به رهبر شهید: شما همه‌چیز تمام بودید و با اسم شهید نام‌تان کامل‌تر شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/667089" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667088">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: همۀ خسارتمان را می‌گیریم و جنایتکاران را رها نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/667088" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667087">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
زائر لبنانی مراسم وداع با قائد شهید: برادرانم در راه مبارزه با  رژیم صهیونی شهید شدند؛ من هم گوش به فرمان رهبرم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/667087" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667085">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
🔹
به گفته برخی رسانه‌های عراقی چند کارگر در داخل ساختمان‌ها گیر افتاده‌اند و تلاش برای نجات آنها ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/667085" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667084">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
از شکار بی‌رحمانه تا تحول بزرگ؛ تجربه نزدیک به مرگ یک شکارچی
🔹
00:07:00 در شکار به هیچ موجودی رحم نمی‌کردم
🔹
00:19:00 علت گریه نوزاد در هنگام متولد شدن
🔹
00:21:50 معتقد نبودن به نماز و گوش دادن به موسیقی شاد در روز عاشورا
🔹
00:29:00 رؤیت افراد جهنمی با بدن انسانی اما چهره حیوانی
🔹
00:34:00 مذمت شکار در دین برای تفریح
🔹
00:35:50 تغییرات رفتاری محسوس بعد از تجربه نزدیک به مرگ
🔹
00:44:00 متوسل شدن همسر به امام رضا(ع) در میان قطع امید شدن پزشکان
🔹
00:50:20 تطابق رؤیت‌های روح در حالت کما با واقعیت در بیمارستان
🔹
قسمت بیست‌وهشتم (شکار)، فصل چهارم
🔹
#تجربه‌گر
: محسن حسنوند
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/667084" target="_blank">📅 20:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667083">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
محسنی اژه‌ای: در برابر قاتلان آمریکایی و صهیونیستی کوتاه نمی‌آییم
🔹
محسنی اژه‌ای با تأکید بر حمایت ایران از هرگونه قیام علیه ظالمان، تصریح کرد که ایران در میدان دیپلماسی نیز رویکردی آفندی و مطالبه‌گر خواهد داشت.
🔹
وی با اشاره به روحیه شهادت‌طلبانه ملت ایران افزود: «مردم ما عزادارند، اما ماتم‌زده نیستند.»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/667083" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_BNYgIK8Z6WIAGN1D420uey2jxMFzuxvtNvntkGo4tKx0zwku6MmPHWFTNCwY5riQNcDIciD9FWsayFAz5RydAUjz3tLaZBtFMJjkN3Qfapt9yzy1P7WGnFQqO2ESb9PpCNn60hXsjxIA7Cuf34hWQdZNNaETVrj9MEZvS5Hp3Z2D4H0XbixfMkRrgAE7YCTkq2hNr3ENdD-5LuOW4s_z69KkD88T6Oiz_BYhjQs7H2XZhu6EVFrSxEagB34sN8tt7BBJuDHqngO8gxRvFx_XGTmkFQ4aY11AfobsURlpdqVNRSlGHhfOz0hJoz1q1fOunSfrpum-PFM9m90l5CGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jk3nrxqQ9742KpYIlkiCmNQvUFCJ-UkejFq1obTvZxutPROZjLIyj_QDpRt1-X38kzjB9lkPXAe0x92DAmcbHfBbQs52DXwzs2Razp0PZyujjZDo_6CFxfaPPytoqOV4GCjfJ7sTmOk_gKMtHv7lDkARYrVEHuNhLCDK3Ox5DKFls1wygF-iUbzdXSTJBjzhlOzLkyJAQzCA6hwtng3WexmnqnreOmY7emHsmwyPILkUBB6D5d3YdvNhgeNCoACqmIkKvogmmk-ToTl0GhbeDp-ijxPeDpQsMYtrAUIqTsB3sPHZW1u8IOPJpbZ7aWsk8bOR46fpu907xrjQsh1vKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aL9-gteGjMURqgRqgPmIMYU846Vj7x1UPujB4vOOj0zEp6BAFipBlVgofTJSPcJJrkh8OBTgL4ROjPES-yWSOYn0r7nEOXKWrvb4a4LDIRreh6HwsPfEe5e8qcHe5JIGwfYmH7OUs2c-niAdfhbWNKX0Mdb3-KAnRuV-pKSlOfzTYU5s_pBChsAAHIOPnksXHEu9zqdNzLl6fzQ5DW2OkN_2jhBSFPr68vAmYhIvdyaE8FeQbcruNUp6048ocWquLwb3yRtRj_GqWmX6XJ0MJDA4DqqFsKlG6jRTBeg6bHJ3E_rpHMSrUh2vWBSGImuS4QkahHJlgTjG5CxgMqHwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTJsV0BH6BNoXpmqzOQ2PKa1tM0vJZTg_S6geHk2z9edq7p3t1EmqJQ7ECwWpI9Do39HCU8BQ1SyZmlwJnlw_R2jFdS6OuCGSU2Di6EMSTRz9uanAB7eLc62tj27qCxvwz4Z2joFYXkKaZ2z11x-nrLmfcBWA1fqSrSFvefBvaa2l5G_XaMR3zRQfELxcYjYYEyzv7Ztq8jSooq9GIw8FKdd4Hz40OBEKPAS1pqgPH8llDpEAhuk_x2RZj0RWF8Dlp60guhRS2j0KULd99Vk5_r2TRGZ77jRhztcb7mxg4GBbW5Ywl7ZuM5Bp3EfQo8AR8i9ILVkQbmfKOrKBqZYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcRc3kbm_McYUi9USLmW4NUcoNV0CarBFxgP2dZ-T-ixgPKplNfNaZO_9BuJ23MGEikelbRIlR6PtCdiWN3OjWVyz5e64kX-qRqR_A2xf9mgkLj2HO3fyO9JeSfiDE8O3T2WrQRvWkq-CN-VSbhEn9O6L39hFTedyMp1LEOXgN12ZdSgAuHwhaWSczvVQtcnhgV7CSXSHZFeMnR74VVT-uQQ7e7k0MuUwQyhW9SYS-NSki6Brz4GJjyqWDMmjq9n5K2kcJoT7AXKug3C2B2YsK0BEsYqwsQ0ejGlc6CrrnKsdBOoeE7AGXZDO4K4naVEBgcMnlq2eirPkuSUzdNANw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با پیکر رهبر شهید در مصلای تهران
🔹
عکاس: محمد اکبرپور
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/667078" target="_blank">📅 20:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متروی مصلی مملو از جمعیت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/667077" target="_blank">📅 20:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4o36cVBJdLNEqiLnYvT4B1r-QmlWIjSJSBs8SZVW-yEffMMudpuyNZsDV_Z-ko5wC4F1eajInuo4E82fga5No7xbhccW3Qrk-Jfng9tyTz1Cv2oM0p3ZNb-__Bw6klRC8Wqo22ccqptEK3V9Avhp1VjiXGKvtX7Bzaibsnd-VhicaLDIF5PTjLDyoFzxuvGI2OwjgbhsXkrHoXBviU7Y3sQCoeQRTAsq4_9WDC9WkzG9nAYBe75KNVWiQ6jvhatmFfQFUVynt-9wcC7AxYMN4hG43MhwN0XGqJUhSmpM_LcAkEr9UhvfBGYgNh0dnmn8q2eqSd_h3-LmKEUbqCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه شیکاگو: ایران؛ قدرت نوظهور منطقه
رابرت ای. پاپ، استاد علوم سیاسی:
🔹
وحدت میلیونی مردم در وداع با رهبر شهید نتیجه اقدامات خصمانه ترامپ است؛ ایران اکنون قدرت نوظهور منطقه است و به‌سادگی از تنگه هرمز عقب‌نشینی نخواهد کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/667076" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید آخرین غروبی که تهران میزبان آقای شهیدمان است...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/667075" target="_blank">📅 20:18 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
