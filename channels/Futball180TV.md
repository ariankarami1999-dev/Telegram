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
<img src="https://cdn5.telesco.pe/file/muwyYlAKgTHgX7doJwtD_7EUe3ubadYsESr8WNOq6D0pgSupA5uSj2IVfTxFgZTk4V8UYG83Zol6jnvvtVEdzcJkncc_GlfI1Uxfg8agMlCHsQWKhiORi-q5hNi3lKGs0ZvXaQ0ujnAfXwVQhtaoGsn3CA-CFhlMdNGR9EE7sx6Wg-59OtlE1XnbmpiG0tAYvbYh5Qu7P0m0C5MJptieXs1Zq8u-WZeYn-0vKbpayg2cyueTTHz-f328pyFOKG3V2ls-4tJFHKbrarybaDAER9rflqnUYQAvj6ah_2IR8iB8PhlGs61kLnQEEQkQQx75geQhwscsFz_HxfF2LI_STQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 467K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 13:17:22</div>
<hr>

<div class="tg-post" id="msg-103773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89232eaaf.mp4?token=l9o5F5OZrdKRZgX4DWDU0i5D8XUocrFpSN-McNsHwXJK2nSFkYhawnjRfvqBlbT7Bj85XS9iRSSX9BFgz4xKJEnBLg46YhKFt_dXczPqmYNPbgoVdoFA4mwmDTrmlBsHvghFotm55B_z5UIYmZovagp-2i9rEgKIY_DCMWw_Ce5TAjQkTYdeAOLCJ2SImoPbpb3hl2CRBlMEYVVLjLhA9w5lom_wXoyqAhVrBhy4MhsPUzZMxl1s9fr1Do--SSwRC1J-9-gwusViL_qGYPYbby0UW8levH1Gti61RUPVPxLQHvLg8CsAt1ouyeWuRgipGxGj6c4_u9scQ3XDKMSclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89232eaaf.mp4?token=l9o5F5OZrdKRZgX4DWDU0i5D8XUocrFpSN-McNsHwXJK2nSFkYhawnjRfvqBlbT7Bj85XS9iRSSX9BFgz4xKJEnBLg46YhKFt_dXczPqmYNPbgoVdoFA4mwmDTrmlBsHvghFotm55B_z5UIYmZovagp-2i9rEgKIY_DCMWw_Ce5TAjQkTYdeAOLCJ2SImoPbpb3hl2CRBlMEYVVLjLhA9w5lom_wXoyqAhVrBhy4MhsPUzZMxl1s9fr1Do--SSwRC1J-9-gwusViL_qGYPYbby0UW8levH1Gti61RUPVPxLQHvLg8CsAt1ouyeWuRgipGxGj6c4_u9scQ3XDKMSclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین تلاش های لاپورتا برای جذب خولیان آلوارز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/Futball180TV/103773" target="_blank">📅 13:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYsR-2J3LLXSWZjwhGw5CBFaPMRBxABsleq4Bufow0enXYFMO_uvu5ia5eyulyoDVZ2E2DIFanEn0xx3Ux8_TAJMb5vI8AsyAoP_kU6BS7CwbO0X4R1OAqrchjCr4ltRuQGvCfrGia8ZaQJzm-9PdUF0BfuH-tZRB84EF_a2jw2H2Rr6cF1v4heI5yZ7eZDYP8iItQFv0pmMXaSNTEfFtMrBrzDMZQndvh3-gyR_03bkgYATEzpqItTK-uN9Yy5LRi17xytnhhjJ6eoXReVgDqp43sm3lSzAT0Vv2PY6LOlTT8l40NyJ3C2Zt7HQ2cP4oHp6KHcflZ2-DdrGkKQrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جرارد رومرو: مطمئن باشید تا روز دوشنبه رودری بازیکن بارسا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/103772" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇫🇷
#رسمیییییی؛ پاری‌سن‌ژرمن از عقد قرارداد با فران تورس تا سال ۲۰۳۱ به مبلغ ۵۰ میلیون خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/103771" target="_blank">📅 12:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWsGAzunRKhnQxGJgIiuiBSyItBjHGxUfYoVZS7fMb9T8EtssU0CUQhYYMPzttQR5oL2s7JtvMTb_CxAdDS1m3Xmd69ynlkh0C74i0MfrsfV_Ybtc4BzqeNL4caR3xhFZ5wecqY0Mla1KvfffXsuA6viI1PiaAPNWBJCk3RKHFMFr8ND8nsNToyYL1j2bIuqxGhqHmJqxu-MvGvL9EqBryMg6CG0cz42VAogPfkMjuh5-jh4_g-MaY75EgDPt57n1potgEryeZZltxdK9RhPxBi170vBLR_E5Eyo6sV3aGC1zl289y8EUGO-eSUlZ78_TnR0ECIMfhmrUW4Rswy3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#رسمیییییی
؛ پاری‌سن‌ژرمن از عقد قرارداد با فران تورس تا سال ۲۰۳۱ به مبلغ ۵۰ میلیون خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/103770" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Lau8rKbRTXHCwDKsSB8K1UxhCMPnBS-hEQnZhXiLLThgItPFMag-E7w7sgjSlT6gTruZ98_HlC1tCNlyDNoQ4ZFA60gA6523NHmv5LIzMgjsQj8I7HJwF4Zl_RtTXCE7gCtErJAjrZ3yoYk8CKL71ccX0N2rmlSlYWUeoUG285lJgNl2pqUzYxwTo3xbvIVvPSwcJHB_7gb1odnzfbTiwsAMtQahXuDMTetSfR74zC87K0cNvfvN7nULzwqODP_0oH9X_lERo59yKU3lbskBRcQf_UYK3JBlFwauZ1jP7W1Bn9esTlnyhEdPDs19fuabeZiySTPq-_p79Mb2NOTVzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Lau8rKbRTXHCwDKsSB8K1UxhCMPnBS-hEQnZhXiLLThgItPFMag-E7w7sgjSlT6gTruZ98_HlC1tCNlyDNoQ4ZFA60gA6523NHmv5LIzMgjsQj8I7HJwF4Zl_RtTXCE7gCtErJAjrZ3yoYk8CKL71ccX0N2rmlSlYWUeoUG285lJgNl2pqUzYxwTo3xbvIVvPSwcJHB_7gb1odnzfbTiwsAMtQahXuDMTetSfR74zC87K0cNvfvN7nULzwqODP_0oH9X_lERo59yKU3lbskBRcQf_UYK3JBlFwauZ1jP7W1Bn9esTlnyhEdPDs19fuabeZiySTPq-_p79Mb2NOTVzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
:
🔴
۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یه نوزاد شیر خواره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/103769" target="_blank">📅 12:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBlcpqmk92aoBpeCnIGIo8j3LXtYT6AVWxih7xTonmgIkAdSkNT0Osub0qg-qjEQRn_M9vjvB3NH66pi5kSi0Fgg7VWxty2wi3y1D7AL7GHiH3d4skjWtICVq7h8lz1lIuZkgngtunxQfXN_tuJ31ipo6Aw8BRQtvUigm_q2um8r5ataKUubKsHkS7HmgphpJqRcdKh0eXGY2U8jRNGzFd6PWxBlEubL3cFq5X8IxqfRBEzodqQOds2FmTXZwAC4WgQZLxodWkaRYlCVa4C38cKmx7WV7kAS6NprUkSpH5ykYtMmll49ZLKGZO0u8Clmf-T4BI7eilseJ-IS6esajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار دیدار استقلال و مس شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/103768" target="_blank">📅 12:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d46239908.mp4?token=cfiujMEwWeHvKs80kBEtTdeH4ZlomY0-aWKpxk0rWjPjcK-veZ__YoJkPOsOSbVLZ9cjTk7akz3jQM6JZQlg9e4-6TLByZEPC6knFxiF7RF0aZUHnDAtHhGcs0a0JcwOb7aBq4HSN3O2bhmFsNz-n_oM0EW2nQhzpsym-GS3EOqNHYU1ZMDWOZxTH1ja-gNC3i0t47Nk4n14tVnesrGwiakmfm8X9Q6Q9hgzBvZu4NcxMOjT5iiLAKwKiQMQ-cKF1xLIdTinpnVnkRVCoSUPPKLguF4jz8VT6D4XKHf-75U346FVeXZLE34uqlAca6oAdHlQE96QhGAAFNJZ7JAkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d46239908.mp4?token=cfiujMEwWeHvKs80kBEtTdeH4ZlomY0-aWKpxk0rWjPjcK-veZ__YoJkPOsOSbVLZ9cjTk7akz3jQM6JZQlg9e4-6TLByZEPC6knFxiF7RF0aZUHnDAtHhGcs0a0JcwOb7aBq4HSN3O2bhmFsNz-n_oM0EW2nQhzpsym-GS3EOqNHYU1ZMDWOZxTH1ja-gNC3i0t47Nk4n14tVnesrGwiakmfm8X9Q6Q9hgzBvZu4NcxMOjT5iiLAKwKiQMQ-cKF1xLIdTinpnVnkRVCoSUPPKLguF4jz8VT6D4XKHf-75U346FVeXZLE34uqlAca6oAdHlQE96QhGAAFNJZ7JAkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال کنید کار کنید کار کنید حال کنید ورژن جواد خیابانی و محمدحسین میثاقی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/103767" target="_blank">📅 11:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1z9BpRCYY28ZL7IPabXl_VUSxOm_CF1iaJxex-LM5tep8XhFOG2-m9EpiBAFGeYJCnQJl8Gjaerded0A61554pQ9HiRJ1COTC-W_S7zITG9a1AnDWtvDBnMD93Lk0IEhVzhSvzsSI9lLV9K1foXUflPjFMrOQ_CjxZZbiMc1bLsq4gjaww7m4Eua7IZ_y-6wa6s-3oWLh8HXNp7tSFQJ4UrcgkKcHzeUU92JZ0mCVsykvZ30nKE1rVQxGkjrAk1dt1Kdzi2fXC1vgllgOiXE7u0cz4GGc7U-_A-NaRVwFJPLNu1a4R1CRPbEhpgRQFEfSEC5u-S1A2RNLVlm7uqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از ساشا تاولیری: الهلال با پدرو نتو بر سر شرایط شخصی به توافق رسیده.
🔵
چلسی حالا برای فروش وینگر پرتغالی آماده است و خواهان حدود 60 میلیون یوروئه. الهلال نسبت به رسیدن به توافق کامل با چلسی اطمینان داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/103766" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-DqRNXc7Yb0BkQh13-5VtB-pPSA_kl9JDyJNq5BkX2xIH9SnUQHNrNje48eJ7E9r5Lm8SdKfvFwme_A98w9cw9x0ZmeBDgv6PTs8Ip5kwaNDcyrg6wOtfm-6_u0LVztqDOxZgyjK8GGSLs41FyJzEMakv07bXiUr83r0N_p3Ha7HZ9BTP0Lh0wUFXmjhnBk_WXl4s9NfQhl0Crpu7KeBZNPRzV7uTX0tEKg6j4oOgEf3sQ1jyzJIZVmIotMhBlNpwczYyA78tzufFLvjbMI3DXnSmsjPT0vf62T1Ugx_At2rfGk5hLsdHnyPN4huXwJz7tOx88PxxGkqFAqj2K4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز: بارسلونا سومین پیشنهاد خودش به منچسترسیتی رو برای جذب رودری ارائه داد و بنظر این پیشنهاد مورد موافقت قرار میگیره
🔴
پیشنهاد جدید بارسلونا به رقم بالای ۷۰ میلیون پوند میرسه که به خواسته سیتی بسیار نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103765" target="_blank">📅 11:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxU3Za4v9jL23NMWH-BDpSW13fra7zbZqptqKmdlRW-q5ynbT6DJEUrEcECPOSXdDe5jSmRBHK_hrfvooB0IxujskQ3CMSqBHrL_lnZmqvhSniAG9Afd3LDeFCX7GBc7fIr3mHV8PuqMpdgbPFNDmiA1kHYmiHNyU_XynJEkwKEuAsFWJ_pn6nUHYiSwMWrcPD45Z7RzN-BU7sQGMpCdKO_hNJt2aRUrgwYtzfP2xOisosJwdQGBK8PR6WbTJguoEmzRS87JEXjHfZSqx3DaJ1935-fa5fXpZM3JW7pDUDJc_y1u40Q2doa4YSKU9jvyJTMQzrESKbuxufrKC5102Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
مهدی‌ترابی بدلیل مصدومیت در بازی دیروز مقابل پیکان، حداقل ده روز غایبه و بازی مقابل پرسپولیس رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103764" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8788296ec7.mp4?token=D1KnAT_LXRrzv11-0E9cHL_Dn3IeccUBP6F837VxxHK27-g5nR_yxfMUVUZLQEuCDIgdgkiYlQzQlETkCFCgadlQZerOeYLhATIZ5EXjAYltqzleIRYlDDHX4fOBJKOk-I4gh0AlOu3lr2wiLUzt3SQye1YQhuciYO8YjemkWea6A4WVbG5qWfIAHQ982z2RaF7CvXCkyObrHLvaBResTivD4MSqh4Pnh6sKXWRz0bIRsKcETmNE0Pdk8FdVBwov7YAqBOjLaTFeFf2BSUz7I6QZ7w2AJFIqDoKbfmc1q_nWHJejNHEMAKYS7Kl_0G_3UQO1KhGHSCidPtyJt8y5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8788296ec7.mp4?token=D1KnAT_LXRrzv11-0E9cHL_Dn3IeccUBP6F837VxxHK27-g5nR_yxfMUVUZLQEuCDIgdgkiYlQzQlETkCFCgadlQZerOeYLhATIZ5EXjAYltqzleIRYlDDHX4fOBJKOk-I4gh0AlOu3lr2wiLUzt3SQye1YQhuciYO8YjemkWea6A4WVbG5qWfIAHQ982z2RaF7CvXCkyObrHLvaBResTivD4MSqh4Pnh6sKXWRz0bIRsKcETmNE0Pdk8FdVBwov7YAqBOjLaTFeFf2BSUz7I6QZ7w2AJFIqDoKbfmc1q_nWHJejNHEMAKYS7Kl_0G_3UQO1KhGHSCidPtyJt8y5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇮🇷
🇮🇷
سیرک لیگ ایران قسمت جدید؛ بعد بازی دیشب نگهبان ورزشگاه شهرقدس در ورزشگاه رو بسته بود و مانع خروج استقلالی‌ها و مسی‌ها از ورزشگاه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103763" target="_blank">📅 11:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279e38cd4f.mp4?token=CQruVqdvn_DVfLm2_xssXlImfAXdTfsYA03VJgCzzBsnxBCfUIJneR8QF6aMr3ECFOP90JuQYUag_-vIYGQl1b-kJN6s_lm5f6NkD691Sv4xnbURuI1q-4OgFkPNS34RC4DMY2Janiy36FGRGe59bGAJPZ5shUEZqlDXQhulfPcqGuXd_4DxURQTrMbcWLMJXBMl6gk34lg64d-iCkw-R-HCjf80vB3dQLQMmmY2bxyT19OQ-hTFqwJd02seLCtkxFZgVWx8TOxaCHcY9ZqH_ZGX_xPup6bNcJLG6EfW6Ai5UtcT3QSKu-XNKCxJ_1JpM0fT7zKqDkQgsdCkUfjEqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279e38cd4f.mp4?token=CQruVqdvn_DVfLm2_xssXlImfAXdTfsYA03VJgCzzBsnxBCfUIJneR8QF6aMr3ECFOP90JuQYUag_-vIYGQl1b-kJN6s_lm5f6NkD691Sv4xnbURuI1q-4OgFkPNS34RC4DMY2Janiy36FGRGe59bGAJPZ5shUEZqlDXQhulfPcqGuXd_4DxURQTrMbcWLMJXBMl6gk34lg64d-iCkw-R-HCjf80vB3dQLQMmmY2bxyT19OQ-hTFqwJd02seLCtkxFZgVWx8TOxaCHcY9ZqH_ZGX_xPup6bNcJLG6EfW6Ai5UtcT3QSKu-XNKCxJ_1JpM0fT7zKqDkQgsdCkUfjEqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بهزاد داداش زاده بازیکن اسبق پرسپولیس: اصلا امکان ندارد آسانی و اژدهاکش بخواهند غیرقانونی برای استقلال و پرسپولیس بازی کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103762" target="_blank">📅 11:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAAQkyaRYgLmrP8OIKYJSw5ZDo1c5C4_dCdbXsEJJiDgV6-MtO-Re_nr_MNMddaovZgRyxQY8RHxEIiNzSlSb-uqtv5oAG0AmLRWz26pxkpP6Glf9frpF-H4F11IhcYcpeDs0hDefYe8ganBKp0G0ibx_nnlm3VXJgH5PFelKK6UIXi2Xhg_awmQOubnwqf9OF1Xh6M3H2aSl_MrxKSTGle2eK0Lkp4n0UbcYPg72r6UzDSquuy7jX7Wtf2pJ8CcVPhAHODERJU8FYYYDBFCWbeQcwAjO1y0oN4M09FeXDZ57GXPtnpRr_H808gopMtCmNN_LmfA04kmnwybkWCeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-میخواستی بهترین بازیکن باشی؟
زیدان: همیشه دوست داشتم بهترین باشم و براش تلاش کردم. ولی بهترین نبودم یا حتی جزو ۵ نفر برتر هم نبودم، شاید یکی از ۲۰ نفر برتر باشم.
-پس برترین‌ها ازنظر تو چه کسانی هستند؟
زیدان:مارادونا،پله، کرایف، دی استفانو، پلاتینی،مسی، دو رونالدو و فرانچسکولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103761" target="_blank">📅 11:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6e913cbee.mp4?token=hh1w4QPLK9iPZeEO9m9TVZ76RQqJL8sX7cS7a31EIqraUGQqEX2YXUiupG2FPw3byv5sLycRpuHpZMVI4vKkquJmnBDt1_txj5WM0I5EK_ZdH2-ghD28lO9zv_lLU0fyMGb3Qz6zTCjLk72xDq4tSfLkPa-qom4zJpAfxTaguovqx7A7iy1FvoYgiVdTi-HKaFiEkK5k7Db0VdAIeq_9HO5akoLgW6yOJRbD8Hg4TRutM4SFLd8vy-KJEjZMyJcCPf04jF2WQs4wr0K33gB2pD2oxbsEkWw9TIq8Iyp2oJbBrmqtlgWYJKAFV3-0q02dh8P1WR-ou7ZcyYIIPfgj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6e913cbee.mp4?token=hh1w4QPLK9iPZeEO9m9TVZ76RQqJL8sX7cS7a31EIqraUGQqEX2YXUiupG2FPw3byv5sLycRpuHpZMVI4vKkquJmnBDt1_txj5WM0I5EK_ZdH2-ghD28lO9zv_lLU0fyMGb3Qz6zTCjLk72xDq4tSfLkPa-qom4zJpAfxTaguovqx7A7iy1FvoYgiVdTi-HKaFiEkK5k7Db0VdAIeq_9HO5akoLgW6yOJRbD8Hg4TRutM4SFLd8vy-KJEjZMyJcCPf04jF2WQs4wr0K33gB2pD2oxbsEkWw9TIq8Iyp2oJbBrmqtlgWYJKAFV3-0q02dh8P1WR-ou7ZcyYIIPfgj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
باختر، کارشناس حقوقی فوتبال: تا زمان باز شدن پنجره و پایان محرومیت نقل‌وانتقالاتی، باشگاه استقلال حتی بازیکن آزاد هم نمی‌تواند جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103760" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103759" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/103759" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqQ28FB6hZfrorinGQjuTAB3vs5Z9MVOJi6gc6DhGilhcs2mBoaehJVRwrEIKOglYXRzYdsJEQtgbKmIJt0ZVa6YcnNvvId_sI31szUqeIQ5b2SO4D8RBhz2zQSOqRtkxjOaf6gRa9sTgijkwrd0XIeimVzli0fi_gafiPca4slybZnyGLiOan5RW6-YMrRb_LQywFhO_1QxULCn2gCnjskFbpyq2RUDyzRcGeqAK9_ezXMr4_XKNhziMUXancbBXfMA9ydTvGAT-9O7PxPk9y1uo4BcwgXdMcDa4DKmXOiTn38iUGqblnCF-v63zcsP_cUFAQ5blhGdo1SxNbY-Yg.jpg" alt="photo" loading="lazy"/></div>
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
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/103758" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⏸
🇪🇸
موزه جذاب و رویایی رئال‌مادرید که یک‌ایرانی ازش ویدیو گرفته و توضیحات جالبی داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103757" target="_blank">📅 10:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQeXiLZoCFNgbzM2WXJxZZXo5bZynGPDIKLn7LDaszkJnimUWbzFLcMRCOkKNSkPkRWJVifoi0mSpOFr8lvQp_YuE24MtTB9pFnwdG7QIPW6g9jk7BZk8bR0R9kWcVoa4CQDvWWoyMyAXiK1Nr2PoZp-Bh9A3BCNHE9sMn_yG_lUAwKdptkU7KiS5yjiBMSA89yTIGRrBMs-syj6_LbuHH5TCwrBGWR-M7lbOHXG4ocjVrFmw3JK802JlCIJg8liVB87ew1WKCngulh-svg0rGZyZ7x_EL2Ukmii8wSMRBtND5Gn3FBBvLlwN_j2Ev0cq3FQD-_NaihPj6xFTFCu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
پوستر باشگاه پرسپولیس برای تقابل امروز مقابل شمس‌آذر قزوین در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103756" target="_blank">📅 10:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js5-TBxkYQLFBU8liLjQUe9EcKdBLEI6St1hNTK9rPHZQhTgINavL3CFzN0lCCm8YP-mfaxOHYm7ikwModbt50TCaqE2gUisylu8Y3CUxxbYQMK2kMZRq-lcAlASLmn9z8mFwznCKxl1e87SyPOkprOONd0ql6c7pHO7SLNGxkJ8xke67-iwAGewowlFou98fFSd8Th-w3gVj4ElAVRnFmXF5PE3Mr6nsHHKsHW9ROvOAZ5L7myWE39kVjrAOgaCDsBI33otPoiWPBpsOz03PNsB0kxAK-qBNT0HbM6iyAMVwp_Prze1fMPJodRTEHYjjz_jvGwZzADY8--CYDepAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو: کریستین رومرو به اتلتیکومادرید مبلغ 40 میلیون یورو  HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103755" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1dILyA5LRDJOsPB2GODIb6iodMf5ugaR_094elZSfEpKxWY_tWgyOJhv3RMFxP9DFclHdsRL2Uleat9EK5dpWMfbi4b8i_crztMInMnpyX_gfhZX2o01gnx_65_dheeHCa3rPnS2rpCtls3Y5YGAPuR2i7z70F8O8kOJ9UNmWdRsx-6TppC9m9K9lnnQcxg9bqy2Obl8PQtn9W8w-TGRrhrzSHQpZ0o3zVUr6KjLqRWY9gc_VinUPPDpAV1IGIrS2nbZtOf1DjwCao0hnFQe03yIzbQoncSCGNbJ9z1g5CPn9kWyCbWY0biV-5CfSAHAOE1kOsJmytLp3q0tiAUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از از متئو مورتو:
✔️
انتقال رودری به بارسا تقریباً نهایی شده است.
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پس از روزها مذاکره بین دو باشگاه، مذاکرات بین بارسلونا و منچسترسیتی اکنون وارد مراحل نهایی خود شده است
🔥
🔥
💸
باشگاه کاتالان به دنبال نهایی کردن توافق در ساعات آینده با مبلغی بیش از 70 میلیون یورو، شامل پرداخت‌های ثابت و متغیر، است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103754" target="_blank">📅 10:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb15999303.mp4?token=f55BJwtgzWFzM1MtEOWA3izOA6UpuXVPybWTOI11owwOTtkUJXTLlq-8Mppm5lGG5PlQeF8YDbdmu1drp44NqIFx_wvP6ZhRFTLNR459gZXl1gEsE7mIgNxF-EXN87UrJypu-PdatDFBkQpP9vBvF5V31NrLd7c0Ucc-g_4cEYP7dhmdgP3j2cLVuY21YdYYzgskusm7mncAq0D_LXfkJtP2LGruOsncZC-vQeEwfFtisHzKYGlunxea7-qICfWxD25rEOyy3JrLMg9Tla0PZTtR797rGqbUF9qGp8uZ7yKOZJg11E7rj9jdsYYHs7O4tfUDSyYQZRRTzaLT3ruXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb15999303.mp4?token=f55BJwtgzWFzM1MtEOWA3izOA6UpuXVPybWTOI11owwOTtkUJXTLlq-8Mppm5lGG5PlQeF8YDbdmu1drp44NqIFx_wvP6ZhRFTLNR459gZXl1gEsE7mIgNxF-EXN87UrJypu-PdatDFBkQpP9vBvF5V31NrLd7c0Ucc-g_4cEYP7dhmdgP3j2cLVuY21YdYYzgskusm7mncAq0D_LXfkJtP2LGruOsncZC-vQeEwfFtisHzKYGlunxea7-qICfWxD25rEOyy3JrLMg9Tla0PZTtR797rGqbUF9qGp8uZ7yKOZJg11E7rj9jdsYYHs7O4tfUDSyYQZRRTzaLT3ruXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇫🇷
آخرین‌باری که بارسایی‌جماعت معتقد بود یه بازیکن از تیمش رو به PSG فرو کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103753" target="_blank">📅 09:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔵
✅
گل‌های دیشب دیدار الهلال - الفیصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103752" target="_blank">📅 09:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=uYLxGHU1A08MhAZwbuawqRTO5fkVdd0pHzukdErV_fP8yvvqbxSyfCi9j-Un5waMV9czb7Pcz1zPnbmYWdsD9DpMJB7aHdESe6p2pzZCY-z8Kwk1LCqoRb4ECpnNLZi9Wchq6G2JzFFqYMLfe4VvkvRgHt47Pz4yehPrfqooIMzQ_UtjVCto_IqkTfN1lCoamxQr6UiVShG1kDfO7YmMdRT38zieVt3rLd7DVl7rRy_AR6KqJ8EnINXhr9H0IfjR0AzFhbjj6RK6mtrRjGAec_Wjl9YW8KDLoEDHvptqEp-b8FX8NyekqsUminodzZI2w3kK-8pbNJDBLxA6mzH6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=uYLxGHU1A08MhAZwbuawqRTO5fkVdd0pHzukdErV_fP8yvvqbxSyfCi9j-Un5waMV9czb7Pcz1zPnbmYWdsD9DpMJB7aHdESe6p2pzZCY-z8Kwk1LCqoRb4ECpnNLZi9Wchq6G2JzFFqYMLfe4VvkvRgHt47Pz4yehPrfqooIMzQ_UtjVCto_IqkTfN1lCoamxQr6UiVShG1kDfO7YmMdRT38zieVt3rLd7DVl7rRy_AR6KqJ8EnINXhr9H0IfjR0AzFhbjj6RK6mtrRjGAec_Wjl9YW8KDLoEDHvptqEp-b8FX8NyekqsUminodzZI2w3kK-8pbNJDBLxA6mzH6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
دیشب وسط مصاحبه یه هوادار استقلال، رفیقش میاد انگشتش میکنه و در ادامه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103751" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9408795cb7.mp4?token=bhWzCgZOVGWRferOW5970hry1BjWwxG0VI_qHeEnQT4xNHxHSg-Uy2siY4gfkGH2hLneyPBUnzGW_iao7tTM1KaF43Rzwez9hSqpBsbwNtvIjoiPV0Kt855DARX4a8c9Lbh5io7D78ddHKyAxzL8FY1gieVkjaRheBFaVo86mI3mMobAxeKKzSn0wLJPkNqgbvoXe7Q9S9JafE5MNwE6JcWNsW9kstY3iRRbLIb4aCm2yRRuYrLqldQz35iYQQ-WHtybBVEHjqhxyHonh5mdUZSik9703CfN81iNSfAxpzRPWvNqQAKtl_34oV7u7vKxOzpXxvS-NIotHU4n5sSL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9408795cb7.mp4?token=bhWzCgZOVGWRferOW5970hry1BjWwxG0VI_qHeEnQT4xNHxHSg-Uy2siY4gfkGH2hLneyPBUnzGW_iao7tTM1KaF43Rzwez9hSqpBsbwNtvIjoiPV0Kt855DARX4a8c9Lbh5io7D78ddHKyAxzL8FY1gieVkjaRheBFaVo86mI3mMobAxeKKzSn0wLJPkNqgbvoXe7Q9S9JafE5MNwE6JcWNsW9kstY3iRRbLIb4aCm2yRRuYrLqldQz35iYQQ-WHtybBVEHjqhxyHonh5mdUZSik9703CfN81iNSfAxpzRPWvNqQAKtl_34oV7u7vKxOzpXxvS-NIotHU4n5sSL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
محمود فکری: پرسپولیس سال ۸۲ برای جذب من خیلی تلاش کرد و هرچیزی درخواست میدادم به راحتی در اختیارم میذاشتن اما در نهایت تصمیم گرفتم در استقلال بمونم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103750" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040b76d16f.mp4?token=GNA_a0kDUPMSAj30mDfpgm69ail5I0dFtsW7UX9MthN2wsDbxCWZsOTLIVGgk-9uUFsreQaE1jBNPrhX7PrF1Y2F6P_3yReqpTyZ4PVbMTc3uwBtIMvNT0rlb3yE9uSL_RORntIT2XEoZC117IhtL_1I4QJE0v3VW0T1QDhQ4sy4qHY68YbZVAghsyt_OcsPphT1zNBgprCZyjXOu2htmiEeAt2HNxWO7_MsFghgmr7LYVFrJzK-Yo92kOGY4uvSnP5jfe7hceXROYnJTtrhmW1HwV-aOLGdFrAlyPlkS-Lf1t1koQeKRTO8WrekbgfQjOV6DWVIZGyIs3QXqoLXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040b76d16f.mp4?token=GNA_a0kDUPMSAj30mDfpgm69ail5I0dFtsW7UX9MthN2wsDbxCWZsOTLIVGgk-9uUFsreQaE1jBNPrhX7PrF1Y2F6P_3yReqpTyZ4PVbMTc3uwBtIMvNT0rlb3yE9uSL_RORntIT2XEoZC117IhtL_1I4QJE0v3VW0T1QDhQ4sy4qHY68YbZVAghsyt_OcsPphT1zNBgprCZyjXOu2htmiEeAt2HNxWO7_MsFghgmr7LYVFrJzK-Yo92kOGY4uvSnP5jfe7hceXROYnJTtrhmW1HwV-aOLGdFrAlyPlkS-Lf1t1koQeKRTO8WrekbgfQjOV6DWVIZGyIs3QXqoLXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👍
اسطوره علی‌دایی در آب گرم گامیشگولی سرعین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103749" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGcDfDPFf4l0TDpW85u03bkGapQy6rmYMk1gc441PTFN4kidZ7emDc_bY7HAnv4kUz9XmwKAFNJhrN-1Y5yKQOgzGwN66f4paKansxggJnhAE-DpEsnpuHIRIhyz2u18IjIKwqa-w0UIDIT1uFOa9FfGzSA2z9I6Qhrrj850w0JbUnX-_IIRjCvqgQc_1g-0M-k8RvyHIdgjKVcZJ2Wvl7rAbSsTBGc102efPjgxjuw7IZqXq0hprqWqCN7mM9Feh2AWcnRRHGUwscMll5eMo4g4Pzh0eUm89gs5f68bQtNSKzSNB-2m5C-i9q7D_vHW5346qMIudELg3QIJTVVphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: طبیعتا درباره یاسر‌آسانی نگرانی وجود داره اما چون بازیکن با اخلاق و خوبیه ترجیح دادیم که بهش بازی بدیم و با علم حقوقی خودمون امیدواریم مشکلی نداشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103748" target="_blank">📅 02:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205c3a5736.mp4?token=fQqiSo-DhGkz9ljqqQErBnRsDFuGn-qLIix3hGNiwlMymMJL0nzzFP8qThUDyJbR0zg9_EKvW5mDOhcP29bMe8IQaEHohMNjJulVPJkb2MoxPqZR051yyoUrlS4gyN6WZDh1g9S2w4fJF8s1LsfSr12bqmXWoj5eqMBBUnY3ZutLJQluhOCGZNhwTMdDdoI_MokaiAnwG8Ndq7SINaJRsnUTurwlKx3RsJEk7CwYBXojaUfzRMH32MhpAwDj5_oO9-toFE35ggsXHUC4TGAwg1wRWUiC6u8o5Cpg3kduk9Eh-C8ukijJBGZ8dVLtFgHqagn0nQPk9fX-MuD4vLqiHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205c3a5736.mp4?token=fQqiSo-DhGkz9ljqqQErBnRsDFuGn-qLIix3hGNiwlMymMJL0nzzFP8qThUDyJbR0zg9_EKvW5mDOhcP29bMe8IQaEHohMNjJulVPJkb2MoxPqZR051yyoUrlS4gyN6WZDh1g9S2w4fJF8s1LsfSr12bqmXWoj5eqMBBUnY3ZutLJQluhOCGZNhwTMdDdoI_MokaiAnwG8Ndq7SINaJRsnUTurwlKx3RsJEk7CwYBXojaUfzRMH32MhpAwDj5_oO9-toFE35ggsXHUC4TGAwg1wRWUiC6u8o5Cpg3kduk9Eh-C8ukijJBGZ8dVLtFgHqagn0nQPk9fX-MuD4vLqiHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
لحظاتی از عروسی جذاب لوکاس هرناندز ستاره تیم‌ملی فرانسه و عیاشی بازیکنانی نظیر امباپه و اشرف‌حکیمی و ...
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103747" target="_blank">📅 01:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d121350bd.mp4?token=JBT8CcSbYBSyUYyFdKvbtSrvk6JINwo2y0cIbbAMjkFaHKUz8ki60dB87LlWhUPgYVEPMgl9uA_EY-0jxCzMN_ab84aOi90gYROsVv3kRjlt3C1DVJ8owoIuyyQ5ZBUVedUAPt2IWuQgYbfS6ud-d0xzPmAUjQllAHCOOioRiwYuInsYy0TF-6vXnFNlaHOwWyiCRz7ayL1hD4YbBldtcgBtpHHMyV739LUwYCpweXpP5bbB_zqE4fYonXTzIpRY0nxxC4lMIQ2AxHCLnBauXpdslhtF8dMydC5GklXz53JDCOD4AbU8hHbbliNE5lC3brJeVzmFWKGze_9TDbdRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d121350bd.mp4?token=JBT8CcSbYBSyUYyFdKvbtSrvk6JINwo2y0cIbbAMjkFaHKUz8ki60dB87LlWhUPgYVEPMgl9uA_EY-0jxCzMN_ab84aOi90gYROsVv3kRjlt3C1DVJ8owoIuyyQ5ZBUVedUAPt2IWuQgYbfS6ud-d0xzPmAUjQllAHCOOioRiwYuInsYy0TF-6vXnFNlaHOwWyiCRz7ayL1hD4YbBldtcgBtpHHMyV739LUwYCpweXpP5bbB_zqE4fYonXTzIpRY0nxxC4lMIQ2AxHCLnBauXpdslhtF8dMydC5GklXz53JDCOD4AbU8hHbbliNE5lC3brJeVzmFWKGze_9TDbdRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
🇮🇷
افشاگری پشم‌ریزون محمود فکری درباره قرارداد رامین‌رضاییان با استقلال
❌
باجناقم، نظری‌جویباری به من گفت از قصد بند فسخ ۱۰۰ میلیونی رو‌ داخل قراردادش گذاشتیم تا از استقلال به راحتی جدا بشه و دردسر زیادی نداشته باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103746" target="_blank">📅 01:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eac5b5b3e.mp4?token=hPDIT_vBbqMz19F6tgrzp09P3QAL_jMQU_Z70C1PPsuj79B7OBzHQmMcZEpaKcFwvUG-1l71Iw4Vkn5nIqbowemveYlaK2nXOvuCE4iarAisUznYVufesFjOx1W2dWd5UIBSlnho5VN5m66n0qIfdfW8TLK2S9p6Zq1G2ARipL2gpDhVXj9Lh9jtpBGRnM-DgSFg4m3CtqyBOy1GCyj0uszT4yP_nXgJ3TNaTaytbNcp1KBj5gyQy3Cn62xo7iA8ZdFAgoelnyQJFQjV3KDusn-_FHfQhNTIL2h24Jg9khdMKKmd8mbgmPMeECOAekMDQ3O_pvjuAzjkFWv4db-_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eac5b5b3e.mp4?token=hPDIT_vBbqMz19F6tgrzp09P3QAL_jMQU_Z70C1PPsuj79B7OBzHQmMcZEpaKcFwvUG-1l71Iw4Vkn5nIqbowemveYlaK2nXOvuCE4iarAisUznYVufesFjOx1W2dWd5UIBSlnho5VN5m66n0qIfdfW8TLK2S9p6Zq1G2ARipL2gpDhVXj9Lh9jtpBGRnM-DgSFg4m3CtqyBOy1GCyj0uszT4yP_nXgJ3TNaTaytbNcp1KBj5gyQy3Cn62xo7iA8ZdFAgoelnyQJFQjV3KDusn-_FHfQhNTIL2h24Jg9khdMKKmd8mbgmPMeECOAekMDQ3O_pvjuAzjkFWv4db-_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🎙
نطق جدید از استاد محمود فکری: با حیوانات ارتباط داشته باشی بهتر از اینه که با انسان‌ها رابطه داشته باشی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103745" target="_blank">📅 01:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e109a43029.mp4?token=rCjQtFNAbIP4mhSRlzG2vNDiY_x-o_TC4QxfjfJTzO1f_bjjHy_-NdyItUx5WlisD485pLNxge8yOYIGXF5_1IY4IAuWEH1uNRQtVmnP-UOxSRiE8sJKp34TtMOtH3H21QLpb8YGCxSU3J3AfjMIMeEr3CTXKxmx9XRJO0ElaIPbbxZI8vbkv33duGjelBNXekp8TaG2i-Bu0xnBJT_nO_C1URYr-7AlwrC-rfWJTgL4vb_F8DAnMT30Da-Yl2ZDIHyM5Vhz9oqrD_h8q-2Gjo0hzIlZzURu4Q03yL3s_Zxho-EmJ9UaerpfPcvBHlf2NRdk9yzoY_GceTP1NtB95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e109a43029.mp4?token=rCjQtFNAbIP4mhSRlzG2vNDiY_x-o_TC4QxfjfJTzO1f_bjjHy_-NdyItUx5WlisD485pLNxge8yOYIGXF5_1IY4IAuWEH1uNRQtVmnP-UOxSRiE8sJKp34TtMOtH3H21QLpb8YGCxSU3J3AfjMIMeEr3CTXKxmx9XRJO0ElaIPbbxZI8vbkv33duGjelBNXekp8TaG2i-Bu0xnBJT_nO_C1URYr-7AlwrC-rfWJTgL4vb_F8DAnMT30Da-Yl2ZDIHyM5Vhz9oqrD_h8q-2Gjo0hzIlZzURu4Q03yL3s_Zxho-EmJ9UaerpfPcvBHlf2NRdk9yzoY_GceTP1NtB95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
✅
استایل جالب از یک هوادار مهدی‌رحمتی سرمربی گل‌گهر در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103744" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c593055ab9.mp4?token=CQK1TR8RD8tJTvlpswERVGb1cjNGRscmR2pxlF_73cFVtlE4GisU6RMLbspKjCZG74Wb-E_NuMfgL3EQaaH5Fl0CSZciSALFVz4hSzgeLEzW16OVVzaNytL0RLDCdgABVBXxRRY_YmBwJRCIthsptjdv9Pwv6NAPWWOn32CIZcsUQg3wxvBDdguK2_GhhtkVsMdhdbpejv07uVGTaSJ-PtgtYNBDYxqYp-EmrSSTRtphHpFJ2_B6QeQc-kOmkOAavE869GTWhkbW_9tEEtqRmYZTM1pWDvry88iU6_KJDhNgeBKSEA2XV8GvGjJM9kkfY3njnAq9Tkcbs2gfxmlx2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c593055ab9.mp4?token=CQK1TR8RD8tJTvlpswERVGb1cjNGRscmR2pxlF_73cFVtlE4GisU6RMLbspKjCZG74Wb-E_NuMfgL3EQaaH5Fl0CSZciSALFVz4hSzgeLEzW16OVVzaNytL0RLDCdgABVBXxRRY_YmBwJRCIthsptjdv9Pwv6NAPWWOn32CIZcsUQg3wxvBDdguK2_GhhtkVsMdhdbpejv07uVGTaSJ-PtgtYNBDYxqYp-EmrSSTRtphHpFJ2_B6QeQc-kOmkOAavE869GTWhkbW_9tEEtqRmYZTM1pWDvry88iU6_KJDhNgeBKSEA2XV8GvGjJM9kkfY3njnAq9Tkcbs2gfxmlx2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری جنجالی عبدالله ویسی سرمربی ذوب‌آهن اصفهان: دفاع وسط نیروزمینی رو می‌خواستم، منو تهدید کردن و پرسپولیس بردش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103743" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404f90ecbd.mp4?token=geZlQ0bRKCLXbKVwIjvTt40HGNQiOBrjfIJa09n9QNmxmL6DlqhnGjK15ztdbJ7bWOeSrwFACFoB3TCNowFXp0WoCeVfklsElNKwhc71JRXgHDF4PXA00uxX9kQpzU7FfOvX5gwjnUWM7k5OdD_fPam_91Unuj1MOQViy8Rh0gc2k6gOyhQCE6vJo7kBGU4s9-oid6uLTX6GWmiGQvrD_AWDucgbHQAzFq1BT6Y4q5OULSSQYoZ7RU_bgDNd7jxq2OpzG7YRkBMonv4XtfKVqZeRMU6U4MoJshMJhIZmjYZi8qrZ32Mbj_zFUA9xzKhylavlsatmkLkM18AEnMMxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404f90ecbd.mp4?token=geZlQ0bRKCLXbKVwIjvTt40HGNQiOBrjfIJa09n9QNmxmL6DlqhnGjK15ztdbJ7bWOeSrwFACFoB3TCNowFXp0WoCeVfklsElNKwhc71JRXgHDF4PXA00uxX9kQpzU7FfOvX5gwjnUWM7k5OdD_fPam_91Unuj1MOQViy8Rh0gc2k6gOyhQCE6vJo7kBGU4s9-oid6uLTX6GWmiGQvrD_AWDucgbHQAzFq1BT6Y4q5OULSSQYoZ7RU_bgDNd7jxq2OpzG7YRkBMonv4XtfKVqZeRMU6U4MoJshMJhIZmjYZi8qrZ32Mbj_zFUA9xzKhylavlsatmkLkM18AEnMMxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آنالیز محمد تقوی از برتری قاطع استقلال مقابل تیم فوتبال مس‌شهر‌بابک در بازی امشب لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/103741" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htQpSWObXhrGHkgTZ6_sn5_0xscMPjD6A5-GVrzj2QYXZu_0RtkFc6DZTkPAML4LQ-dvUUMzDTq__OVYaAKdwLVtDI5ufG_rNsgcSBASfbvZtjlZSnDEmY3Aq16tV6uONKeRnngyYconppwdR1yx71MpNdEgwp7uOCTEpGiYnvcaapJ0K-jNe-7lDzjRegA_KrMrbsZznMgY3pPzujSYFb5wSfBCfMlLyLDMLIvbASy8BEWt2OAXsQH2KA1T6m4euTQtM0jSVwmrKhlsdRRPyRuzNlKHCbrOBXw4yXU2mdQTEgVrAozBEf4T-xVcdTmrQ_lCcZA_-rynkj0TwTmWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
داکنز نازون همچنان درحال نخ‌دادن به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103740" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103739" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=YvpNoqJ86zjXYB8E5TLEaxROHRkwLgRk3dFqE7tCYSvV4oOA-tctwFgkzSPa6nJXBMGTYFx16cToXbwff6K557vzSwAEq1agRXX1paN-__xY-a8O2eaNoYcdfCLLRvGM7OSDxEPIAWqnlugu3cX19gLeAwecTQEeiIpeCQVlLNsa3lZdHMOrh7R6Gmh7wOqQdm8vKLnPikH2JTUtWuC7WPJELdxiNF3ktM9XvAmm1saHcg7QJaGbhvLlq1DMQ_k-to_1RCe7nTRPwfgUhNbS-hCdYLJu3LDmbjh5wdf4TbgeM-cMiq86hxpfsSy0HaWgblBzktFyAJUttdAutqJIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=YvpNoqJ86zjXYB8E5TLEaxROHRkwLgRk3dFqE7tCYSvV4oOA-tctwFgkzSPa6nJXBMGTYFx16cToXbwff6K557vzSwAEq1agRXX1paN-__xY-a8O2eaNoYcdfCLLRvGM7OSDxEPIAWqnlugu3cX19gLeAwecTQEeiIpeCQVlLNsa3lZdHMOrh7R6Gmh7wOqQdm8vKLnPikH2JTUtWuC7WPJELdxiNF3ktM9XvAmm1saHcg7QJaGbhvLlq1DMQ_k-to_1RCe7nTRPwfgUhNbS-hCdYLJu3LDmbjh5wdf4TbgeM-cMiq86hxpfsSy0HaWgblBzktFyAJUttdAutqJIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a23
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103738" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3aa311a1.mp4?token=p9XDwqAyvDKI9GioSgAXZOy3z8NW67cq1W8KP6_NjuMq9cCtBVQBrorSBBTUjX-F8diK1u_8j-7Dz-SukfsQ_G-R8oQxflKDiXrtvcPTgoqpbcTps2toSCyKF8pTAr6m4mc3ElPs55A3GvzjVwo1Yn7OQu9noRrJgcLnTliVZ_EYFzfZMB0ceL5sUg4ZyZ1Idoz6tcQii1QSa5Ew-RnxZvRVtINnKp_vXzb6oLLEiDblO6pZpUp1WQ3Yr2tQ2MUGfqPr4LEUwnThmdQqkKOMEKWSkzLXqWGKObbsMT2OI7Zg5Tu1pe5V0y2lRj_UvP66o8XpiLDlAxdElZj701agZoG9nppDNxD1sEC9b7sFTU_WqO5TtHERym_hoxXHJT5N3tQmxQvpe0nasu950NlKWZqULN9E0ifHatdeKr6Aqm67omyXtaJKgo6eheH_vWDEmWaUWxApP52DtXrpd-rmbpbAzVUQ8HjWm0Xjb0P8WLqNP0zAxoQv4N9sl6yUttlXnp2K128d-hl8A_XwyCIeSJ-4Elh7dPEei_DOEGuzap5s2MuehGnc8WVxwo7cHB3hrFCjXcpeiUqd44kKaPTTGMsJcrsvd8yfZWOMxE2-inaACBWckKBGeXfJSQx8XT0FcMBBSdyTtzDJa7_l5cdHu0feL5fJDKM-kBp-yl3V9us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3aa311a1.mp4?token=p9XDwqAyvDKI9GioSgAXZOy3z8NW67cq1W8KP6_NjuMq9cCtBVQBrorSBBTUjX-F8diK1u_8j-7Dz-SukfsQ_G-R8oQxflKDiXrtvcPTgoqpbcTps2toSCyKF8pTAr6m4mc3ElPs55A3GvzjVwo1Yn7OQu9noRrJgcLnTliVZ_EYFzfZMB0ceL5sUg4ZyZ1Idoz6tcQii1QSa5Ew-RnxZvRVtINnKp_vXzb6oLLEiDblO6pZpUp1WQ3Yr2tQ2MUGfqPr4LEUwnThmdQqkKOMEKWSkzLXqWGKObbsMT2OI7Zg5Tu1pe5V0y2lRj_UvP66o8XpiLDlAxdElZj701agZoG9nppDNxD1sEC9b7sFTU_WqO5TtHERym_hoxXHJT5N3tQmxQvpe0nasu950NlKWZqULN9E0ifHatdeKr6Aqm67omyXtaJKgo6eheH_vWDEmWaUWxApP52DtXrpd-rmbpbAzVUQ8HjWm0Xjb0P8WLqNP0zAxoQv4N9sl6yUttlXnp2K128d-hl8A_XwyCIeSJ-4Elh7dPEei_DOEGuzap5s2MuehGnc8WVxwo7cHB3hrFCjXcpeiUqd44kKaPTTGMsJcrsvd8yfZWOMxE2-inaACBWckKBGeXfJSQx8XT0FcMBBSdyTtzDJa7_l5cdHu0feL5fJDKM-kBp-yl3V9us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇮🇷
پشمامممممم حرکت عجیب و خطرناک هوادار استقلال در پایان بازی با مس شهر بابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103737" target="_blank">📅 23:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇦🇷
15
سال پیش در چنین روزی
؛ لیونل مسی در تقابل با رئال مادرید موفق به ثبت یک گل و یک پاس گل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103736" target="_blank">📅 23:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f450f285da.mp4?token=v5Ru0Jw9zYXUx6d7McLTPILxqVJiRmEtTYz0c1IPirML6wgKpVp8NfAXYH_vHMp3lE4ld8QxNtmttHbh2Q8-DMbQV1ZLFFqXYBHWGz0K7WQYJA6UmuXZrLEIiwLDdc1dO6f8zvzG_wMPxHVzoTboT36_24hHiqN8OMyH3pBQuH5W4p7FRpk0KYzfaqAtj37TUb0cNA1mF6YlVkSKA01hOt0Za5Yoe2xYrepV6hDdK7vUJsnp__p_6tACBLLvb1ZYiR1NqHErndA54tZSGUwDZ8Wp_SFloop37MygKaf19-iWeUaDX-KF1CfdvLLIIw3TNySzEXwdylaNyCMt81VSu71JjxsmJKi7F6zbffjYJ3MNrmBmPlIX4hAlbvdocoOBLrNBhMZX7P50Z0nfjuvKU3fCEiY_Tocabg6KCKbnJMwquWj2ewIGVauqYszEnb4lH2Vb1lp5LG0Y4jhqRRaqF9FsDj3gSmSJq1aiIy1wlVsesXwpTmZibgMiffoEUpdEFNaTYERDhz2wW9SP3rRjJFQIKt54kkArCCksaW1fQRsET_lfZss-zBZeoQQXjWlczr4EerhoP5oD4javVPRRfu4DTnxaVf6lAyWZ8nyj1F7bvJJR_0Uq6PSHM-bW9tsySdDxXv1IUQvC_7nvzVEfm3VhofXnEgzTeihGFavhZBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f450f285da.mp4?token=v5Ru0Jw9zYXUx6d7McLTPILxqVJiRmEtTYz0c1IPirML6wgKpVp8NfAXYH_vHMp3lE4ld8QxNtmttHbh2Q8-DMbQV1ZLFFqXYBHWGz0K7WQYJA6UmuXZrLEIiwLDdc1dO6f8zvzG_wMPxHVzoTboT36_24hHiqN8OMyH3pBQuH5W4p7FRpk0KYzfaqAtj37TUb0cNA1mF6YlVkSKA01hOt0Za5Yoe2xYrepV6hDdK7vUJsnp__p_6tACBLLvb1ZYiR1NqHErndA54tZSGUwDZ8Wp_SFloop37MygKaf19-iWeUaDX-KF1CfdvLLIIw3TNySzEXwdylaNyCMt81VSu71JjxsmJKi7F6zbffjYJ3MNrmBmPlIX4hAlbvdocoOBLrNBhMZX7P50Z0nfjuvKU3fCEiY_Tocabg6KCKbnJMwquWj2ewIGVauqYszEnb4lH2Vb1lp5LG0Y4jhqRRaqF9FsDj3gSmSJq1aiIy1wlVsesXwpTmZibgMiffoEUpdEFNaTYERDhz2wW9SP3rRjJFQIKt54kkArCCksaW1fQRsET_lfZss-zBZeoQQXjWlczr4EerhoP5oD4javVPRRfu4DTnxaVf6lAyWZ8nyj1F7bvJJR_0Uq6PSHM-bW9tsySdDxXv1IUQvC_7nvzVEfm3VhofXnEgzTeihGFavhZBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
👍
صحبت های زیبای آرتتا در تحسین پپ گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103735" target="_blank">📅 23:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ii1RafpQm1MnPCGLzJcm0NrsnOovlIwApnR4lhdMWsAhVDwEzy6kHIR46BR8huhQodEGSrZJZj0AP9JSrO_pQGB6pKAS8mpG9MvEUBY8mx2CNGDLI_tFqEl2VZxKuqk5QuUfVixHkWxW8ud8gogodyphl7sbCZrWyXseuo2rBANqxbGS_TPNBP4kSy9nCM-L1I7922nFUGYNfJ_DHIbIJWIDUMHGcr6GtJDk7P950CFEAtpYIMzmCoJdiKIHAZ7ApJ89a87NgHVXSPCpS5oDnHuqUMscQIE0DafbM4zD5FXb92AkEh9nZQRszoLO1Eoshx1GIzKTryxVe3th2SVCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDytDzOzHa18D-WU0z2Hr52xyoks1D3A9AAVHKoIUVKmb95dGvvXqwtAPFIqrxmqFYuT2hx2sekZl8EQL_JabeGqDUVi8-6Ju6vl8VlJYG8__YmYwaTKmtuCd9VNvNyaNdsECBpQX9tdhAfwG0TM3hob67RkEuelFzPUUoU1oLv5aB5Ygj1CF_c8a6d_IDcnqDaysJGqBHrC3aqilMsbRdgyhCmMJT3PrXh2U0i2Q4YK6js5Y-LxCSXVZpvkeHrKsqE1cyMu0JrapMZnpcjuAnCJXjDtNLTNGL0Xfu44WrO7JmvgsssqJ81RT48MdoZvPDRRmVN57IOpDNuhk1k1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV8vF2hck5aVI8Klef4Omia_8NMKnWIrcp7fTS3mBGR7KR02LMliHBEoQgKvFoi-d7ca9NttnCx7whjPD9dbWNib2PC7qgQF_lCYdtwVitjURJ62MUHkdVUCwoBFz6zTPILuom4FztcmPo4ufUbmqtW6rd8U01QgBg9oIPEquVDWtyClTnBxK9CXFsZzx_eJZfl1olWSiKk6-Sn2v5pDDETxOs1RxRnDoX86pyHk_0VETidv5ofF9AJrFVB2PJiL4g5VNHW3m9wnY1c0nlQ1SwNPllkJCrtPl5yVwS11V54ggg3rtrwe5HqdCRag7Oi3x-rXk_WbvL_zwhyLgSotVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😢
😢
خب برگردید مثل‌اینکه رونمایی نشده و باشگاه پرسپولیس نوشته COMING SOON احتمالا فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103732" target="_blank">📅 22:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL37MeL3l4jZ1Unqh3kf4BOu07wdb2irziZbg8JRkd_7UzMDvMCLYuoDHrf4D3IiXL25EJKRsSNMfRjUrKrPA6flNGTbImPMdPMaOIFIR4n0xE_MK9r_UHfSNMmFvhm6pznVzYamEm_vWQkhyS7CSfFg_nkCYe0e_SGTemsDoCW6GDHgzh96Cld_iQSSGLWyJ2GCkNKfJPq6Q7mENlPbhTJZkoMbU8IqyzKEmfmVIeIEkJrWkCwfxLoQNmH-mL6tUZxMhWVrR5XWcy3bGH7mOtB7XiZ3xwbUhF0yMh6EKJ1VBgiDIkopLQlUP7V2JlZnpwBxCUtNRzz2aWzNkRWj5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
فووووووری از الکس کروک و بن جیکوبز:
اوسیمن خواهان انتقال به آرسنال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103731" target="_blank">📅 22:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbF5ULmTubizprSWif8f3t5sUOrlKdiVqT0wnUOBAJreUcN6gM7s6PbJwjkmYbQx14f8pBHmmv0X9yKF4QoUgwp0Q6guAUR8JKP1F4jqu6wiRkmMyN-sG1fs6PNamEYAqwhANoIn8k4QskW6xOWc2ShxCxTPNSZW4lGenIs_9kTPhtrIYj5TjrOKcwRaX1HtB3hXOr6MvrLhyR74LTMtY3BPuIc-JwRuW7kbDs3ZMsEArfa6bF2eDN2ZYoifZDZHIsRWAaFF1umwRgbZlmfON7qNmWbx7dcGcpjo9oF4lKu3SZ66gSvq3qK9fLLkTGzTwOItP-XC_ec8r-txhTKskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UH6oj11DPByaGYDPEcwcfRSQwDz98b65eKLxs_VHlxLwCDSYDILW6rcAbmQyCRMjMkhBnyt-bIbZQguQgUODEZzQpqpuQYgnndoJMJJvG2FQ6jwkmq6tX7_IAYM5vVCqyAnxUG8dFAPGPHvAWn5jFqssNO4KIO6Fd4CnajnW4QVYEvzcymOoqAKuNirg9I9QNQnMvd3mPXXoZ_wjbZdbCme6eOxAVrQoALUGUGZS8De64dlmz7HvqMVaD-xsAQWYbTCt3OsIGWI1KMQzBUX2bupj_ARKAB8XTxC-wJQ9Mj1g6VweN3J0LkJjOs8AyGPvJFqO_dyU_PrMq35Q_IZYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
💍
جزئیاتی از توافق‌نامه از قبل ازدواج کریستیانو رونالدو و جورجینا رودریگز فاش شد،
این اتفاق پس از مراسم عروسی خصوصی آن‌ها رخ داد! این زوج در تاریخ ۱۱ آگوست، در یک مراسم خصوصی در ویلای ۳۰ میلیون پوندی خود در کاسکایس، پرتغال، ازدواج کردند. آن‌ها یک روز قبل از مراسم، توافق‌نامه‌ای را امضا کردند که بر اساس آن، دارایی‌های هر یک از زوجین کاملاً جدا خواهد بود. مادر و خواهر و برادران رونالدو در این مراسم حضور نداشتند. فقط پنج فرزندشان و چهار شاهد حضور داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103729" target="_blank">📅 22:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo8kGwkvqEiin71BrtVBv7ahEJ4gxF1-sHVFg8fTUjQVUere3WA7KhWXmSUT2fUngSJqxDrJSuaoEH7FPqkgb3hGcaj4wUBIDlVAWPBdRvUxPb-V6CDjvvq_7Hv24FQ027cbecjEjlHu3HAxvv1qpL1hf5sZr5Wh5DaNnx4JDV9f4XbXp88O0-mjTGPULdfvCa_XYgGdz4ioU3Z422rGTxpHObh6NlhGyD-InX0uhukYfZCIr4UhShIZQ_G1NSUiOBYeU5yTmEEUv38hUosh2n6LjmDYjPpOMORF_korBoauPi7NfPMyZi77F0UrxOPs0F_3uDDLXWCvPxlSMOss0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
نتایج روز اول از هفته اول لیگ برتر ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103728" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
#فوووووری
و
#رسمیییییی
🇮🇷
پیراهن فصل‌جدید پرسپولیس رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103727" target="_blank">📅 22:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc09573e8c.mp4?token=opps1Zc0ca2whaV7UKM4FVW155raiH-QMHEnkatt8ZhtJnk7Cy-VO3e5evtOcN9NHrvoa1-IZayB9wvC_0G6MnAOh2OEw-VUZXI4x2bRy9Zws3tpZpvh07Gwxvn6iPY9byJh_VLhM55JFMNOCe9zr5z_cRJA0FeWyy_jhF1NeMoAvXyEpfeVLvsWp5Q99XzXDo1f3j1Z0Fgb3A1fAWDg5-qb2eFSnqa3AOLe9uZQfGrTDSzNpvhQ9ypamYy04RR3A8_K0GEYaYaR2tAO0YTCqC-q58Nt0XZqp5y53S5T0QJPgT-oy83Ka_RWlac9_61fq1_qmi_y4bKSDCLKF3feJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc09573e8c.mp4?token=opps1Zc0ca2whaV7UKM4FVW155raiH-QMHEnkatt8ZhtJnk7Cy-VO3e5evtOcN9NHrvoa1-IZayB9wvC_0G6MnAOh2OEw-VUZXI4x2bRy9Zws3tpZpvh07Gwxvn6iPY9byJh_VLhM55JFMNOCe9zr5z_cRJA0FeWyy_jhF1NeMoAvXyEpfeVLvsWp5Q99XzXDo1f3j1Z0Fgb3A1fAWDg5-qb2eFSnqa3AOLe9uZQfGrTDSzNpvhQ9ypamYy04RR3A8_K0GEYaYaR2tAO0YTCqC-q58Nt0XZqp5y53S5T0QJPgT-oy83Ka_RWlac9_61fq1_qmi_y4bKSDCLKF3feJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
یک‌ویدیو بسیار کاربردی دیگه برای رفقای ورزشکار و بدنسازمون که با توجه به این نکات میتونن وقت خودشون رو بهینه مصرف کنند. سیو کنید و برای رفقاتون بفرستید
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103726" target="_blank">📅 22:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شکایت مس شهر بابک از استقلال؛ احتمال ۳ بر صفر شدن بازی
باشگاه مس شهر بابک به دلیل استفاده از آشورماتوف و ماشاریپوف و اسانی با شرایط غیرقانونی، از استقلال شکایت کرده است. طبق ادعای این باشگاه، این بازیکنان اقامت و مجوز کار نداشته‌اند.
در صورت تأیید تخلف، احتمال دارد نتیجه بازی ۳ بر صفر به سود مس شهر بابک اعلام شود. همچنین گفته می‌شود بازیکنان خارجی استقلال تا زمان دریافت پروانه کار، با مشکل ادامه فعالیت در ایران مواجه خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103725" target="_blank">📅 22:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
شجاع خلیل‌‌زاده: گلی که به مصر زدم، آفساید نبود
به نظرم گل من به مصر اصلا آفساید نبود. وقتی کارت قرمز را به خاطر صحبت‌های ترامپ بخشیدند، ممکن است برای گل من هم حاشیه درست کنند
خوشحالی با عینک؟ آن عینک را محمدحسین کنعانی‌زادگان به من داد. قهرمانی فصل گذشته لیگ برتر برای ما است‌. بازی‌های سخت استقلال مانده بود و ما چند تا بازی ساده داشتیم که در آن‌ها پیروز می‌شدیم. صد در صد قهرمانی برای ما است. شرکت در تورنمنت سه‌جانبه؟ اگر فدراسیون چنین تصمیمی گرفت به آن فکر می‌کنیم. به نظرم ما قهرمان هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103724" target="_blank">📅 22:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zww9gm8oZmHTRqFqrbNOYGjtwJpO3_6UzOign__6ZA0PmDxM9a9E5Lf9tBUWsDEbNS1w8jycOSjYxtwAOfjC89FjwqHCEsMklkwnFcd-BUcrZ6TL-WUaZvktzbJwZq7mPf3Y5aJEoBKj_q1AlAH9rfwIyZ-_Ax47ibSxLAzaTx2EzEDKEH_u7AfN8HHUNdfQ4mLYt049ux2VX24ITL7BoWNwq1X9272l1TstgJEeSEX2Z52tuOzB29iNisq6X08V4UmxqnWwQDwbdPgc2z8ASxVPKJCXn6Q9F-ZRlPPhnX_UMgYV_vuWqoCcv8tzIUj2bfSgXPwojqlH3gdBELSgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
چیرو ایموبیله برای همیشه از فوتبال خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103723" target="_blank">📅 21:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f579bcf7b.mp4?token=CdYXRm-btIAHhBy01hgi607s_kE2iAlwDKWRbGtxfUS40ySTAZhfqHt27ebK7AiOPG5WF30FybxW5QgRhRSWKrKkh0HapqZ2rWy8L9I0DcpYq4BKjEUcid0q7SSzkFr6udb7KSz_4wb83cda3E5DvnJuB0IG9QGiJ0SswpG7AF639qnA8-lmzpVtrQYT9uQCNiNVNNphqdl5u3fyTc06VPEzz0FwbHVKiuSyy1F97_kWl4xR-i-tP2_0JBrzJDFvKBGAjNqDRX4WFXfdvKkB32gZFE-VjilhpwA08nnAxq5XQ40t3WcuZcq0Zo6eh5mG4gfYKXGBbEfMMQWvBJ0GZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f579bcf7b.mp4?token=CdYXRm-btIAHhBy01hgi607s_kE2iAlwDKWRbGtxfUS40ySTAZhfqHt27ebK7AiOPG5WF30FybxW5QgRhRSWKrKkh0HapqZ2rWy8L9I0DcpYq4BKjEUcid0q7SSzkFr6udb7KSz_4wb83cda3E5DvnJuB0IG9QGiJ0SswpG7AF639qnA8-lmzpVtrQYT9uQCNiNVNNphqdl5u3fyTc06VPEzz0FwbHVKiuSyy1F97_kWl4xR-i-tP2_0JBrzJDFvKBGAjNqDRX4WFXfdvKkB32gZFE-VjilhpwA08nnAxq5XQ40t3WcuZcq0Zo6eh5mG4gfYKXGBbEfMMQWvBJ0GZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل چهارم استقلال به مس شهربابک توسط اسماعیل قلی زاده.
استقلال 4 - مس شهربابک 0|آتش بازی‌ آبی‌ها در افتتاحیه لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103722" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97101a20d.mp4?token=oYIVLdswjdZ14j80kOv3f_oeuGr0U9Mwpr5KlIVrkZ6Vy05EaaCEdAMwmGcnBRUbBKBuNsLsZYTZB81iDBHGZyX5sA_GXanLH7HLRPk9QJxbpEDwK_3fvDcZx_NovMzLy3zjmAmNE4VuAz26_G4ZmWppr8Fc8dkU4UCeGY6IdeMAWEPX2AEXpQ0DoLcyJz0ej1ejWcch_TjFQbDfan-Bn6KJ0J-perpqkuQvzPCbHJT2Abrji3YI_iSUMAOm0bk1E9_KsSaWqfiVe5mfMyfNCjdYPuVRCqgNJ3q0V2iyGTCSD1P0mOxLliCc2Bq8ygam4oSc2hMZHz4Wf8MRAUmEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97101a20d.mp4?token=oYIVLdswjdZ14j80kOv3f_oeuGr0U9Mwpr5KlIVrkZ6Vy05EaaCEdAMwmGcnBRUbBKBuNsLsZYTZB81iDBHGZyX5sA_GXanLH7HLRPk9QJxbpEDwK_3fvDcZx_NovMzLy3zjmAmNE4VuAz26_G4ZmWppr8Fc8dkU4UCeGY6IdeMAWEPX2AEXpQ0DoLcyJz0ej1ejWcch_TjFQbDfan-Bn6KJ0J-perpqkuQvzPCbHJT2Abrji3YI_iSUMAOm0bk1E9_KsSaWqfiVe5mfMyfNCjdYPuVRCqgNJ3q0V2iyGTCSD1P0mOxLliCc2Bq8ygam4oSc2hMZHz4Wf8MRAUmEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گل سوم استقلال به مس شهربابک توسط محمد حسین اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103721" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G63UObcMKGbICUsMe-6sIhF8fkxhBhMqwwatmSX6EMC8nl1OWW1zyvgv4VesmnUaKnEUXNcTDrMRuitwm6xgRoqWDyczFwdADuUTb_d7LwODUhPuRmE2_bR3SXr5-7JK95E-hIbWjeSceBmi0pLXF7pJfkSzCRf2FK2-NkWQUnbYMIBZhwI6-vf6CF6-x-AyXMHzr_cDd2lsm2EowSCaMUz0_OLvt80o_4F3jq--27vz9wijFh_VuIAMGjfQwQpIWLoBeuCn4XZTQyi3iKtDv54yM-sNtguw47erDo17QvMN4nc6z7RtmOx2QOIZYYfvfLTeMymMVSoNTzttwvr6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیاگو آلکانتارا: قسم می‌خورم در شش ماه اول حضور داگلاس کاستا در بایرن، همه در تیم فکر می‌کردند که او در مسیر بردن توپ طلا قرار دارد.
🎙
رابرت لواندوفسکی: در شش ماه اول حضور کاستا در بایرن مونیخ، او در سطح یک برنده توپ طلا بازی کرد.
🔺
و همون داستان همیشگی؛ فوروارد و وینگر برزیلی معمولا دو سه سال در حد توپ طلا بازی میکنه تا وقتی اون روی واقعی خود رو نشون میده...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103720" target="_blank">📅 20:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec243dc76.mp4?token=RDjRu8pHKHYIwTiPQVzS30Ag2Pbyhb5KXzi_AZ342iHXUVaaFPO6Wx7YYRPQeX51TPA9ZxGcU-RMU7KIANm4QPb59RCqb6VA6EKWzIXJeS-BNXn7tFA5vtp9611GUJwfn7LY-POrfJKlM2LUgXWAsjM2f7BIvjfFeop0e1R5UoBUc11iplC1cpx7rU7EkZ-3w5LLo1O-AKBeG2YpHb0yTlMn3xyfZpyRXOCLwBxoZvyvccU6HF3HJx0k4vxmdBg737VV4rDyCov_cFbXIOkAdAlaPnzKxOWvu_8YvcD3sCkxFV9T10I1sEXhB1JM8Q-HBMYvfLkNUelAalEvD_UJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec243dc76.mp4?token=RDjRu8pHKHYIwTiPQVzS30Ag2Pbyhb5KXzi_AZ342iHXUVaaFPO6Wx7YYRPQeX51TPA9ZxGcU-RMU7KIANm4QPb59RCqb6VA6EKWzIXJeS-BNXn7tFA5vtp9611GUJwfn7LY-POrfJKlM2LUgXWAsjM2f7BIvjfFeop0e1R5UoBUc11iplC1cpx7rU7EkZ-3w5LLo1O-AKBeG2YpHb0yTlMn3xyfZpyRXOCLwBxoZvyvccU6HF3HJx0k4vxmdBg737VV4rDyCov_cFbXIOkAdAlaPnzKxOWvu_8YvcD3sCkxFV9T10I1sEXhB1JM8Q-HBMYvfLkNUelAalEvD_UJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به مس شهر بابک توسط سحرخیزان(55)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103719" target="_blank">📅 20:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
🇮🇷
دلخوری تاجرنیا از تراکتور و سپاهان به دلیل اعتراض به اهدای جام قهرمانی به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103718" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKFoWYv-yeWNWLqShfZM5GLi5d6A2hzmDK9iZf_XDvbjjjfmIrcP8FhW7rU9fHa1mof2p8Ozc2OqRyCTgpnhxw47EaUqxE_lJLm4ijvHRYGhBtm3YqrOP_7keutRnO5qo0qdRBdZ6EhnVN3mhYd-ULwLZC4NX_5ZAFfrKiHy5jLW-UAyzymISKiXOKjBicn3fUU2VPhqF60m7a8UHcx7fFMo3FmFLKpJjwYhjkYn4NqP-MVfw40u9uD3z9UBYLW5pTI--Q1MVoIiJkRBMrxm6aKPCoqkFn8KRIXGwub_b529QxiGgd1IeHQZtDyF4XQzi1HIdmrlckrnShSei_UYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
ترکیب الهلال عربستان در اولین‌بازی فصل جدیدش؛ الهلال رقیب استقلال در آسیاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103717" target="_blank">📅 20:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvSgpawQFUJrRnQbFSe9WHfaJG00irABI2onwBMkshPMV8t54SY_o1V90pPYKM7qDazBdTAujfoj6YcfS-QG8CKMHV2rt-z8dMhwEP6bSMpAEvJrwkgjViFc1G5XCWHQuRCkltgRqlokUT6d0XxU6514KYzIiB9wTSaYvZng3JXReKOpanRJfY_a_HWw-B-kJgj8kuqwvaUy-dD_1RyssEKz035wYrVWuJE267vcopYkGSNbG74BNlcbkR2Sws4O8BB7KundfNbLKaXN5XIbR3RKjDFnIZ8EjXJ8bVtSQN-eeYcONcyMve002tFI80eoGEUAlDbyhVziCfDZ7oSQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن B دکو برای بارسلونا در صورت عدم جذب خولیان آلوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103716" target="_blank">📅 20:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c31f4579.mp4?token=p1a8MfHZoiuuKuXIKdSOwEOc5oKSAB2RowYgrHk36Y-TotYa-Qn4GeGsldGIVbgh_v6yVgMHOvzk3BjWl5pRN_TbGckJ3uCOtryiJ7ix7y-stk_ECS_utO1hiAG4FAMbh82nNtCYrRAdgoDEN_6aP11bystHvUtxMm1cT1JIkQE1ZlRY4hhUSaqRele84RuBcQL9ptAY1yfmuS4JvPz5ECXKCVCCQkd4UGJeaxz3ru6Vd_ZEg1Nl7tQ0aeR8N5hh0uUwVMNBRwQc8NxfItjl8f83RXLIj_FUEWg8XKgPmPzYnMek3YtgxeBjOUaRkZJmRbaQKxpmQfenGRHWFj0zGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c31f4579.mp4?token=p1a8MfHZoiuuKuXIKdSOwEOc5oKSAB2RowYgrHk36Y-TotYa-Qn4GeGsldGIVbgh_v6yVgMHOvzk3BjWl5pRN_TbGckJ3uCOtryiJ7ix7y-stk_ECS_utO1hiAG4FAMbh82nNtCYrRAdgoDEN_6aP11bystHvUtxMm1cT1JIkQE1ZlRY4hhUSaqRele84RuBcQL9ptAY1yfmuS4JvPz5ECXKCVCCQkd4UGJeaxz3ru6Vd_ZEg1Nl7tQ0aeR8N5hh0uUwVMNBRwQc8NxfItjl8f83RXLIj_FUEWg8XKgPmPzYnMek3YtgxeBjOUaRkZJmRbaQKxpmQfenGRHWFj0zGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول استقلال به مس شهربابک توسط سعید سحرخیزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103715" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHbhRdXFGhkmqMpsdyut49Glb8g9KaHOV7LNAifUhrf6tKB-w2huygWGz32BQzYpFXqOdCwzXx3YY4fjGPT9o_snO1mHUBw6WcEpQDe1O0TM6tV3EgHqnxJYv1YCucZbynA5-ftekzzWuf3Vw-BHzy5IYFB7oAPZO4_BdKDXbUx9aUj8mvOcp5aQkSKooowqwn_uUwA1130Eh6ipw-A9WoTH_3FV4o9V_D10QZdE8waKGGjjkWqcl6n7Riv72lRtY6AxlBQikRWbjYY3EBvehS0-kirKioN20wh-vI4EHD20J5ZlsXfaZKByxhfCSzrcsdAPfU6msli-lTIiApi28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتنهام برای خرید ایشون به منچستر سیتی، 85 میلیون دلار پیشنهاد داده
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103714" target="_blank">📅 20:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUsdyH5apNpZImG45Cm-pTxQomIysUi8HI0r1u1wEI5IoOJCyeQXw2vyNKuMtfcok9HsUQsiwBAu7PSN3pJp53UnoX0jpIEpo0dSRCeXfhthuD8szSFA9wXY2CteIMtgbEpxU3J3h0rc4zj-z2MvWlKY53Dbq-tdJ2VV_QUtv5QaAaaIRz1NhC5X50cKUbV6VMJBNWr9Qz-358qsIIyj74Tr7curSaRxL0521-6SUX8CZ1QfjdRYLbeOa5XaQ5F6bZ5KZvWcnm2WvcCMXfAfCKfGBhY_-Y8TDW4iUINH2Wtrsh8ggG7D3JjDkI0U78pBmZMS0PQ0pSibkpf1KbUCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
رومانو: چلسی هیچ پیشنهادی برای انزو فرناندز در ساعات اخیر دریافت نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103713" target="_blank">📅 19:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813759dd72.mp4?token=VrucrlUIdapeBT23MwmZ6JtzyJwy15CT-3X7s-zK-6zBTtSKhDLAEAYcfnHZ0xwN2jlRpCxaevwy7Dpr4Cd4CgIUi_MoCuzDFrVk3xtU1fgWjRjNJ3vG6N9Gg2znyaP9Guo6DWGP0gzCABDiiJfGdPYu2xo-0-5WFJ-BJab2dESWfcs6iha_BuxLBlYhQeFSZ-xQ8SilPgV3XKTJ0v6PC0ASwGvGHrhEEyBECWAjKqG1ZK4cfmYzjMIl4ydrZNQgsHikE9WyQnyHtidm609X9kpUBf8LDUN9bqu-psHsJl2ax2aZWiXh4nBXBV9BrcRx4XJQ4UniV-ElxuNXz58VRiS-R_C915FZLNCQg0IG4-mMVZrYk9p6S1guQYPFGQISRzcQHFnAwUPkAHTei5WOX6PqGCQc9P7s7_uQ7wbnv0pWc7ZREmR8d4rBMFvjBQ9gSy054CdTKbIn0s0Og5w4AnrmR4NcgmUExaJJEz-DJxV7f-CtlGxMZzS2b_2H6Vp9mQFPP9HaIj1PUwjOC0Z6GCxMX4_gsj7v2z84h4kS4t8m4jJx-llWPQeLE4nwyn-G9-q-6mwvnUIOmcNjBFL1J2AegAwAp3Mv5EajASi-ksnYcavqKFvzpqiIdVonGjto6p2TsqstVpEMn4H4yRZaLoVn5cBSJ66ciW6B1EjIYfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813759dd72.mp4?token=VrucrlUIdapeBT23MwmZ6JtzyJwy15CT-3X7s-zK-6zBTtSKhDLAEAYcfnHZ0xwN2jlRpCxaevwy7Dpr4Cd4CgIUi_MoCuzDFrVk3xtU1fgWjRjNJ3vG6N9Gg2znyaP9Guo6DWGP0gzCABDiiJfGdPYu2xo-0-5WFJ-BJab2dESWfcs6iha_BuxLBlYhQeFSZ-xQ8SilPgV3XKTJ0v6PC0ASwGvGHrhEEyBECWAjKqG1ZK4cfmYzjMIl4ydrZNQgsHikE9WyQnyHtidm609X9kpUBf8LDUN9bqu-psHsJl2ax2aZWiXh4nBXBV9BrcRx4XJQ4UniV-ElxuNXz58VRiS-R_C915FZLNCQg0IG4-mMVZrYk9p6S1guQYPFGQISRzcQHFnAwUPkAHTei5WOX6PqGCQc9P7s7_uQ7wbnv0pWc7ZREmR8d4rBMFvjBQ9gSy054CdTKbIn0s0Og5w4AnrmR4NcgmUExaJJEz-DJxV7f-CtlGxMZzS2b_2H6Vp9mQFPP9HaIj1PUwjOC0Z6GCxMX4_gsj7v2z84h4kS4t8m4jJx-llWPQeLE4nwyn-G9-q-6mwvnUIOmcNjBFL1J2AegAwAp3Mv5EajASi-ksnYcavqKFvzpqiIdVonGjto6p2TsqstVpEMn4H4yRZaLoVn5cBSJ66ciW6B1EjIYfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
🇮🇷
آتش‌بازی هواداران خیبر در شروع مسابقه باعث تاخیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103712" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=N_Ej8GnqKxrwmp_rZv7qwDqXGGYCPaQJAR5zCQZBctw4MfXrYgPVRWah3BcPiio7brIM0E3N2TlkTVrLxeBegTmfMW_J_3PqUDEaXcYZSHmBuA7an8pw1RbxnkGZfH9VVux8tyjRQiUNoE-Lz6DDySHMeL88AyBdoMJV3g_D1A3H-92xJ9jKUmU_K1s48vgl1xfh2jYBoaEhAkC4uscZnaPcKB81h7BAo0K59bZYj8gjfNXyP__g2CSt7qxTYNekLDE3T1JKqrhqgHOhguTDrUFRpPagN-kZzpV8E5RiClUnsqSslHJJzaUwl2OsVE1foFyybNgwFHgpmP8KzD8LDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b464aa2d22.mp4?token=N_Ej8GnqKxrwmp_rZv7qwDqXGGYCPaQJAR5zCQZBctw4MfXrYgPVRWah3BcPiio7brIM0E3N2TlkTVrLxeBegTmfMW_J_3PqUDEaXcYZSHmBuA7an8pw1RbxnkGZfH9VVux8tyjRQiUNoE-Lz6DDySHMeL88AyBdoMJV3g_D1A3H-92xJ9jKUmU_K1s48vgl1xfh2jYBoaEhAkC4uscZnaPcKB81h7BAo0K59bZYj8gjfNXyP__g2CSt7qxTYNekLDE3T1JKqrhqgHOhguTDrUFRpPagN-kZzpV8E5RiClUnsqSslHJJzaUwl2OsVE1foFyybNgwFHgpmP8KzD8LDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
وضعیت عجیب در بازی فجرسپاسی و خیبر خرم آباد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103711" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت.
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
⭐️
بانک ملی ایران، هوادار استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103710" target="_blank">📅 19:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103709" target="_blank">📅 19:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ose1sJxeC_EubEmSy8UfZ6_xBNGmL2N8Iks2gybbVoh-eWw7vKLd6IuTSSf6AJgHNO27Wq8PegIdl0EZRbckingIYnqS6vaee1OXevhITNd7dWIiQHcTaFg74i1u-rZM3W8a3tRYdBAcOcomsPF-6xWR4i6i3fsbS8p_nFtn_f2uszcVHu3yokGBHlHLGfxXrvK6l4tcBIpbLy3ioeQEm-ATh88znpCBxCD4u9mfnTYJtrN-6IRb8V8GmtKLdgQtIjaD3oG290BBc9GfTmPenSUr72NOBMdcOk-Umsiit4erXaTN5yQzM2yjM373Gh8uR1B0ifzWnUq50O07M05d_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103708" target="_blank">📅 19:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLnzkXUa0GL9L1whqpjgIi_Er-ylFKBgXJMGUJViVEtovOvHEupJZPXXg5drDyPSTMnO-epWclSkT6l3SBVf_fvcINt-IUSwOhsf6LExk6kxGvI6RzROZZ_eAD0E-t8OuFl-wb8H1j1zH64Z7kYhRV6IWSNSj6o_FAmX_ajAGsO2kmiS4nrQhFuIgb8LZMglWMhC3LhCAhYwvSKopurshcObPUAXcLZVjGlwODUXMv0Hf8F8wdl4dM7Ru9Wj4_xj2gQOSly9MQxBJ9J5c1QQaM18S61AdbOOD0E7Wfd_dyMboEBONECSE0hEp3G2Gryrvtw7w2K5b6kTdTT53_5iIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ پایان‌مهلت چلسی برای فروش انزو فرناندز به تیم‌های خواهانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103707" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔂
🔵
فووووورییییی از اسپورت:
بارسلونا در حال آماده‌سازی برای ارائه پیشنهادی به ارزش 80 میلیون یورو به منچسترسیتی برای جذب رودری است. این معامله در مراحل پایانی خود قرار دارد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103706" target="_blank">📅 19:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdcCDTraQog1ibGbIVIOkqqSP5O4j-lukkJlBTNVTXd_IhqKhgA8AdwaCesILNNYtqufBjPwYIUzDZoGjXgrNeCuCeh8EKAj9bOFvSkEK_bUyyllD3EJbnO8sry2V5tKMFrb9R3FDSlkidgJZnO0slw78EwNj7c4Cv41cv4IvWNo_kU8Cs_7vIPvGd0BM2r_zMT6sOD9ac5pIPHaCNNJz1b391LD02a4KuYb0sdGWmhbJSHcI9i7F4MJAFaYBmXrXPS3_0s9eoo4nt1YNZOnb5wEjfUPQUVi5C9zN1y23a4MNqj5GpuXQ_D4tr9zubwD2AQ9KIxZc7AISddt1PPxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
دیوید اورنشتین: گابریل مارتینلی پیشنهاد نجومی گالاتاسرای ترکیه رو رد کرد و خواستار ادامه حضور در آرسنال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103705" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🟠
🔻
فوری از فلوریان پلتنبرگ: گالاتاسرای یک پیشنهاد 45 میلیون یورویی برای جذب مارتینلی به آرسنال ارسال کرده و در حال حاضر مارتینلی اولویت گالاتاسرای در این پنجره‌ نقل و انتقالاتی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103702" target="_blank">📅 19:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563373a8bf.mp4?token=rvawsgTQ68bJ6b1n1qF1HQzufYnyEs6yZKqkzH4jfqnnEZTFlAJEFKJ9tgKPCP32dZOtIFVvqWKAfFCgO_okp-7X4OedPSylwec24wqEMK3zu7q6ljFWdaMYbOq_RVxGRRawzhi_ftPdO4g5d5AmB7XU4MzYknO7xLKLwYna34rn1L-2Rqtj-gTvFC5itHuUBbkqEhN2SIecYLEaxbEaawwEjvcU8OboWRryQJEPqjsiHpdtxpqF5GaBVC5RIJcHYS79rmx1gjkrzkk44W6UcSq72FkxTl-g9jS-XJCNXIaBD0V8sM2NbJOU2-6Qeqr9R7WFzjl3AQx6HC416QPQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563373a8bf.mp4?token=rvawsgTQ68bJ6b1n1qF1HQzufYnyEs6yZKqkzH4jfqnnEZTFlAJEFKJ9tgKPCP32dZOtIFVvqWKAfFCgO_okp-7X4OedPSylwec24wqEMK3zu7q6ljFWdaMYbOq_RVxGRRawzhi_ftPdO4g5d5AmB7XU4MzYknO7xLKLwYna34rn1L-2Rqtj-gTvFC5itHuUBbkqEhN2SIecYLEaxbEaawwEjvcU8OboWRryQJEPqjsiHpdtxpqF5GaBVC5RIJcHYS79rmx1gjkrzkk44W6UcSq72FkxTl-g9jS-XJCNXIaBD0V8sM2NbJOU2-6Qeqr9R7WFzjl3AQx6HC416QPQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: از فیفا استعلام گرفته ایم و مشکلی در خصوص بازی کردن یاسر آسانی وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103701" target="_blank">📅 19:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
⚠️
بنظر یاسر‌آسانی باعث بگایی جدید استقلال میشه. تاجرنیا رو آنتن زنده سر این موضوع به خودش ریده و داره ماستمالی میکنه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103700" target="_blank">📅 19:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ92V2L_h0BnhbdViCSTLDqpYVYbsv7WK0mhlov7jflpMaLW2eZSWx1pB449oHdelw0JVaLLPn8aJxYX1G7_AYrbj5tfobsoQuLeS3af9QuvSpsKNa1MIoo1sBSxlfS3Bv7r0aVRTB0qFsesh5pCpXeYyMLSMIxA35Mb9pUpZ3HHb-lEsUPvFg8zYfQL9ry9t4SZTNTUiNOJKtbiEWnIQFoeRU_5kCvX5poriGgZB7_eyRmLQb0SKrFXzSNV_i2C3D90wKm4YE1aj0UoMYAhDd4GsWKo59jDbPwJXThZVxsG41MgWdLrcyAF5ovWelzcFckpGO_Q0tK2qPuxOH3ooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
بنظر یاسر‌آسانی باعث بگایی جدید استقلال میشه. تاجرنیا رو آنتن زنده سر این موضوع به خودش ریده و داره ماستمالی میکنه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103699" target="_blank">📅 19:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZoF-dOQC2IuPX-L2BMppc9F7PLE4Ry9Z0GFOquZq-oP3VVkNs2wRCi_JFR3ShE3qDNHVmfgIweviBzHZp0mDAKfq_qB6COoK7zkprwMDt6YN1qBzSIaatREbNGskmj2Xo2cWZXtUpoySWNWBS3eK3mVVdRX5U4B5gSh8B9dmouO5XnCAVaYtweEP4kBii_IDEbW9Hhgvpo4je6Tb_qsDv5uztsHeMKQrRmn83537aEezyiNXqxY4uO89Eo3Wd3NmgGXKaSEtHCzxfdL4nreXs1UwV6hBoQncY0y3ttcO9RhjYqMXWtI8oo1jyVkW7WGYcVppnGcx8MOj7z8n88TBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🟡
ترکیب سپاهان برابر چادرملو
حسین حسینی، امین حزباوی، آرمین سهرابیان، احسان حاج‌صفی، آریا یوسفی، عارف حاجی‌عیدی، امید نورافکن، آرش رضاوند، مهدی لیموچی، محمد مهدی لطفی، رضا جعفری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103698" target="_blank">📅 19:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6cddcc0e1.mp4?token=QbCg_WMTXI--nRTSAlYeUtOxJfa76kxDDTw7tgBZdZqFoUPf6Zz_aS7nk7yp4DPRkZL6sr_t9wQT6Pa8c3zJUFgKgDpY6JC5sAXb6k_CTqzx9arT2Bb_PjDl4X6MtwrjA6SFuKh_mFLUMesH0CR9RfxrI9MiTV7zLlysMWVIO7hPFAwYuw5Lxgys9NTwehFveFW5-fMNTJkQORrLb79pEA5dI1Z88xRYe2kJqvIewVnzV4WeS_Fl0Fl-_g3awPM-MdT88j8Q79vKfmspWwfvnFCdcAIytmL2WFsK9Ak1bD-bBngDXxxsw_y2Hfs0ilNAzbKPQQtRc7HBzhPgSd8r4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6cddcc0e1.mp4?token=QbCg_WMTXI--nRTSAlYeUtOxJfa76kxDDTw7tgBZdZqFoUPf6Zz_aS7nk7yp4DPRkZL6sr_t9wQT6Pa8c3zJUFgKgDpY6JC5sAXb6k_CTqzx9arT2Bb_PjDl4X6MtwrjA6SFuKh_mFLUMesH0CR9RfxrI9MiTV7zLlysMWVIO7hPFAwYuw5Lxgys9NTwehFveFW5-fMNTJkQORrLb79pEA5dI1Z88xRYe2kJqvIewVnzV4WeS_Fl0Fl-_g3awPM-MdT88j8Q79vKfmspWwfvnFCdcAIytmL2WFsK9Ak1bD-bBngDXxxsw_y2Hfs0ilNAzbKPQQtRc7HBzhPgSd8r4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل‌شهریار مغانلو مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103696" target="_blank">📅 19:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaEZXEHkZ0_efXcTg_nNhudRmvGQ0cLP4XwvMT2FbKY8KlbIaU34Tg2pmI0CqxTwPnfG0eyhhgAj2NKy_nurT2biJQcEIg0xuU2j-jdWCc1VzaRz_97iOZ3TzYYmI_kOXzNPWNHHiV_YqlMh2nPLVCSYFIdN-ojKOVllY7VKwCYeZcqLwQXqw0BogfFaIlKj1jbOCtoHQ_EotXFEhAuHPOdxj4kT8WB1_qeTK2z-M3tE4R3oKr0-8B0owR4EeD2haOiYhEhe9Yx_Hu638GVqdtkOxL1E0QNsOVlWZ8AivJknwPgU3ClIuwu7rPxZMivzeoMf6g3WR583WcyyIPQXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی: احتمال بسیار زیاد انزو فرناندز در چلسی باقی خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103695" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998cb72ead.mp4?token=lEUZxJl7-ck-QgJ5Kc0K_aWnxVJQnH9rAk-nRCCIwczFnpUk89MC1JRDprgZmUspLuekGFpIBsJY4TTeI7sP72OcOpvyPWXx5cEfqB5DB1U1p8_rlog4vOeVX69aeBVnyarK5raXYd-xd_E52zslsst-F6pZZxYU4ZZ7YVKuwhI7sbPWy7RCZ8hMopNxg4JQpaiXEtqMOPXJlroq3cJRjcT_AeX6cMyt72-FaG6GqIhUhrYfwEsyHrEMnNz_-bs0m-VfNDaBUUV2VszMzn79xzBGX6NVLfTAFlFszEx3GpJ9AfiFPNc1x7xDH2NNyuu4ytZut4RvIOORhVXrQ1f-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998cb72ead.mp4?token=lEUZxJl7-ck-QgJ5Kc0K_aWnxVJQnH9rAk-nRCCIwczFnpUk89MC1JRDprgZmUspLuekGFpIBsJY4TTeI7sP72OcOpvyPWXx5cEfqB5DB1U1p8_rlog4vOeVX69aeBVnyarK5raXYd-xd_E52zslsst-F6pZZxYU4ZZ7YVKuwhI7sbPWy7RCZ8hMopNxg4JQpaiXEtqMOPXJlroq3cJRjcT_AeX6cMyt72-FaG6GqIhUhrYfwEsyHrEMnNz_-bs0m-VfNDaBUUV2VszMzn79xzBGX6NVLfTAFlFszEx3GpJ9AfiFPNc1x7xDH2NNyuu4ytZut4RvIOORhVXrQ1f-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول تراکتور به پیکان توسط مغانلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103694" target="_blank">📅 18:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ff06fed9.mp4?token=tzN4D2MbvBGGSFdnyph-dcu-I8ylw6dXQAzG9qUY3nHRJsRAB9DFhfJ1LwTNFAAi-e83RT52oGJ0rAfmd5zfGHPYp6ZecTLXIE1BMxFOQwq1z0tIEgtopjUQKGdHMIKYeKmdIJ1vbS-GIn7EC8EQU4ijx-csIkX7tvFJUbQOUrI6Bnk87gF3lnv73bdB9ox-AivMqXwfuccdbNZpGjZnpdWyhjA7Su8SaqCl9sNwcKKJ8zlaojbDQOTn5XHMjo-R2xJSpyIUHBMsuikly7hR6-94uqjpxIYKU2c-KM_somQOVyvDUV2vAumqHuo1tcNSE8ByTLX3PK0G1WSuMy7VgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ff06fed9.mp4?token=tzN4D2MbvBGGSFdnyph-dcu-I8ylw6dXQAzG9qUY3nHRJsRAB9DFhfJ1LwTNFAAi-e83RT52oGJ0rAfmd5zfGHPYp6ZecTLXIE1BMxFOQwq1z0tIEgtopjUQKGdHMIKYeKmdIJ1vbS-GIn7EC8EQU4ijx-csIkX7tvFJUbQOUrI6Bnk87gF3lnv73bdB9ox-AivMqXwfuccdbNZpGjZnpdWyhjA7Su8SaqCl9sNwcKKJ8zlaojbDQOTn5XHMjo-R2xJSpyIUHBMsuikly7hR6-94uqjpxIYKU2c-KM_somQOVyvDUV2vAumqHuo1tcNSE8ByTLX3PK0G1WSuMy7VgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
😳
نحوه ورود مردم به استادیوم شهرقدس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103693" target="_blank">📅 18:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcbfdP2yqn4OCaNSoBBFTnZDivWOHTVcE5NC3f_I-BOqOoZmi8qo45ffhsdJlPnfOBjthY041JeOICkI1V8BQwiQYKnsbbjHr0mxMCldi-Kolb1Ch315NIl8WGi7vVHZyzgnDB_u2ovEuVArlqE6f2ybOnydlHVU88nr_eFqRsmaYPSCV9iJUXOz12Meq3qtztVbNBZ0S6GBQcbSxnITFwIRssq_teUndhEgvA3ku54Sbzkx-z1XoIB2EZwcyswWatR1ZXYugRRxQ9eESAl7z-1VWM4FgWGHTU52rLxuxr4i7e0byvWNVx7ikMBTazUclbQk4I2EwpCvZwFls1R5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازی استقلال و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103692" target="_blank">📅 18:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ2LnUBFnA8oFU8m7zu6gyj0MTAu9miqZyiB9FhjFVoWfelVuCsY4KeJsfw6Bnpm-cxzHF-VQLclFFTfCoC0h4gs65yhcaHHvg4n89sFnY0EXqXFP0ln-3056IRZ3V4w28eNS-cGf0fiyXXNyvtvDARAa1GTf2Rr8GZVCHB2lbdj-X9CoBdMz3HBEdK5dRLip8LIbHK4EzHj5Liyb1GmAh2TSUaS7wDayyQBJlgYf0ie94rhEM1SxHDRr5YAe47tH2XmooQLZWiR_zo_HOb5N2DybV9vm31CYlDZqW4NrCRnyLwJc0Lmz3rR3kuJC6Jg7UND3LteRqZlP2MV5qGxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب استقلال و مس شهر بابک:
🇮🇷
🔹
حبیب فرعباسی، صالح حردانی، رستم آشورماتوف، سامان فلاح، امیر محمد رزاقی نیا، حسین گودرزی، عارف آقاسی، اسماعیل قلی زاده، یاسر آسانی، علیرضا کوشکی، سعید سحرخیزان
🇮🇷
🔹
محمدرضا قوی دل، فریبرز گرتمیف محمد تاجیک، محمدزبیر نیک نفس،…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103691" target="_blank">📅 18:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbHpI6zEv7MyS-Eg9FVAegtYhQFCvL0QyEJrHJY-hZNkIpKNC8vnonpdEflDTlf64Mytk8_qJWtkbsKS-8EKS8J8lYXYEunsYjZBAXxHSBRBgGOABP2vF8A5ALm0iA9YQfWMFLSPrSAkUzrR6i2XkwUmtYZ_d5usRAcB2jQGb7L5Dqgk8-XTkeTxd_QxfDgenRaBAsacnhRiwHBJwtG7Yst8yVppi-BL4zTn50J0Ek8xaldPYYhwfkuuX24VD6A1ZX-iU0I2CYvIsZR1NloTPslc7jopbLHmTBq-Hy_2jatGVym4i1QU9g3kix21-vgtm-ED-WtjtchMfLDbv6Fq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب استقلال و مس شهر بابک:
🇮🇷
🔹
حبیب فرعباسی، صالح حردانی، رستم آشورماتوف، سامان فلاح، امیر محمد رزاقی نیا، حسین گودرزی، عارف آقاسی، اسماعیل قلی زاده، یاسر آسانی، علیرضا کوشکی، سعید سحرخیزان
🇮🇷
🔹
محمدرضا قوی دل، فریبرز گرتمیف محمد تاجیک، محمدزبیر نیک نفس، محمد آژیر، اکبر کربلایی، همایون افتخاری، سجاد جعفری، محسن سفید چغایی، امیر نافذ ، امیر روستایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103690" target="_blank">📅 18:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvGBJwuqirL-WasGBzteEqY6a5QI3eMUwEhvWBF15cSdTKOpPEdvL9_n3CPKF8V4561pFizs_w2R10Ok0_KGmOGRP57416JRuSABmogr0V9DG4S5OyYEe09jA1YMr1PlSakQfl6Pn12UY1J1eIODScFKOzG_SSheApsntD0BprK3LRyfYhYUcGBmWG-T08dFvZQQRUTyndXV_cspN2Ad4Ga1-34YbdLN56vnJOSq89m_MqGHoAlACcXy5JLLAL7oXvsl3FcrgtxUL3rteRnwLt0e3HwoMWiHU-bx8G-H-RZnWnt1OWMub9MtTqbvwOTkczKwBCTc9obKl_WsD7Nt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
اسطوره لیونل‌مسی در تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103689" target="_blank">📅 18:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e29123671.mp4?token=sjkyDGFBqVb-RGLm2zkcgfdAV2ceFoHmH6Gb99UQ6C6ZGH01NXI1fdhqWFBdln-8V-kLGLytjOpqG1l3oWCXcq8A4e2vIDOWG-PIWrqRJnLKmFqqIiFLiWyo0t7uc8qs__-kmWS79kjKVwh2UkZfFLf6IxbwQfh4UUwaq1RWz-NMvDpwSpujW4zEkcyMk2z99LFzyirks4sqO-uXwDBtC_skM22s811XJCMZFVnGkCuy5sXYyZF8_ZgdxHE_v1Lk4445D4HR1CgQn6P_oN4Satz3evThhGPieQE_b6Zl_K2f9hEEv7VzND3haomlatizHTOhS2T6f8-es2LzfagrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e29123671.mp4?token=sjkyDGFBqVb-RGLm2zkcgfdAV2ceFoHmH6Gb99UQ6C6ZGH01NXI1fdhqWFBdln-8V-kLGLytjOpqG1l3oWCXcq8A4e2vIDOWG-PIWrqRJnLKmFqqIiFLiWyo0t7uc8qs__-kmWS79kjKVwh2UkZfFLf6IxbwQfh4UUwaq1RWz-NMvDpwSpujW4zEkcyMk2z99LFzyirks4sqO-uXwDBtC_skM22s811XJCMZFVnGkCuy5sXYyZF8_ZgdxHE_v1Lk4445D4HR1CgQn6P_oN4Satz3evThhGPieQE_b6Zl_K2f9hEEv7VzND3haomlatizHTOhS2T6f8-es2LzfagrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
❌
واکنش تند هوادار استقلال به جدایی رامین رضاییان
: «رامین رضاییان خیلی پول‌پرست و خودخواه است؛ مسی و رونالدو هم این‌قدر پول نخواستند که او از استقلال خواست!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103688" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103687" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O353jJtWZj4SMXWLaFxDdHeCLYUeMI3aDWjLvPBTI3IGpvktI30wFHMx4f7tF8B0Qkk7jjn3Dww_TlCldtoA10Un93ouwui2binXtg3gYR0yKQnnJ5B1hec5UDrxhWt4WIxGRmpywaDkO0AXJ96ybTR--mOTt0leUU5rFXvd05abHVB-8e3pC69e793-xhw_Vr7zCi0ECDQrp44IOos_GP4Ivge4FL0wxPyz0iAVSmV1HrAWu-q3P8NjdhzcNMq0lcEoFW3kxYEuKt16IEtzmc40NgGUwI0gZhFE010gm713uRRKXn6VQWfN_oowAacbYEBtGW6WoKOJFQzA-VqOhA.jpg" alt="photo" loading="lazy"/></div>
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
g23
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103686" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94bc4d128e.mp4?token=EhyeCtcugMMKxoZiQnOGXF_ngQmg60Nu9pyyD0meZXmZy5xfMGbJ2rTTS4RhRSpgOvyl1lHMTcgtjL-lQ_a7cpXb7fUf8T1TuxuW4tDh3WiZdkP0pQYCePO80p1ka0WEcrGtxwkNytCg95qnMk3uu1YMdQR8aP1VNgjx0aJZunGpcxiHMoqbzkgsvmgE41JH49z-RasIlwGmESoz_3MUgGCFu9D7nTd3ODESE_OR0cKiwoh4IRIBFQ0CU5Kym570gYBWCeNuljBqbwLDdSVCzc0ZG679RAzE-jE2nFEB331F_0L5XOpkdWCrXj0URHYBnBeExMTP5u4WB1yGTqF_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94bc4d128e.mp4?token=EhyeCtcugMMKxoZiQnOGXF_ngQmg60Nu9pyyD0meZXmZy5xfMGbJ2rTTS4RhRSpgOvyl1lHMTcgtjL-lQ_a7cpXb7fUf8T1TuxuW4tDh3WiZdkP0pQYCePO80p1ka0WEcrGtxwkNytCg95qnMk3uu1YMdQR8aP1VNgjx0aJZunGpcxiHMoqbzkgsvmgE41JH49z-RasIlwGmESoz_3MUgGCFu9D7nTd3ODESE_OR0cKiwoh4IRIBFQ0CU5Kym570gYBWCeNuljBqbwLDdSVCzc0ZG679RAzE-jE2nFEB331F_0L5XOpkdWCrXj0URHYBnBeExMTP5u4WB1yGTqF_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
مهدی‌ترابی در بازی امروز تراکتور مصدوم شد و نتونست بازی رو ادامه بده. تراکتور حدود ۱۰ روز دیگه با پرسپولیس بازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103685" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a978a537.mp4?token=EVU8spkl1s-CAW1qXczEuLiZQDFRPPSqTzUxe246VKNoKFM7OyPAdam1hssmZkwVemv1DouG06RysYffhvlaa86QxU5Rn5jtNnFJi4gGmVVJm4ndEytqthr-UkaV2p6l55_Vdjy-Q6xCGEljxq_VG_ie3ywbnMA1wSJvLsKZmFY8aCtSOoEdauwgEMtu_atQsJN8r10778rahX10gY0hi3ZyA3XrHO32Wd9OcVU5sh3szc6EuhhhEbp7D5IfQ9QJCxNrAuFC-p2eefOJ7LCwSJQ1KiMrVRp6gFoyotHzTiurh_AVy9bbAqAQBA7ce1IFHRGFqVSi_b085r74QbLF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a978a537.mp4?token=EVU8spkl1s-CAW1qXczEuLiZQDFRPPSqTzUxe246VKNoKFM7OyPAdam1hssmZkwVemv1DouG06RysYffhvlaa86QxU5Rn5jtNnFJi4gGmVVJm4ndEytqthr-UkaV2p6l55_Vdjy-Q6xCGEljxq_VG_ie3ywbnMA1wSJvLsKZmFY8aCtSOoEdauwgEMtu_atQsJN8r10778rahX10gY0hi3ZyA3XrHO32Wd9OcVU5sh3szc6EuhhhEbp7D5IfQ9QJCxNrAuFC-p2eefOJ7LCwSJQ1KiMrVRp6gFoyotHzTiurh_AVy9bbAqAQBA7ce1IFHRGFqVSi_b085r74QbLF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
آبیاری موکت‌های چمن‌مصنوعی شهرقدس در آستانه بازی استقلال و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103684" target="_blank">📅 18:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTCqYXbJ1rX4AILkfIAwbMn6MwL04vm-OMNZt1lMzrRiK8Wi2LHkl_QEOPwdh1qqzFVR-N9AJNQBHeIX6ls2FYEKHEmNxnc1otnpbDLIQ5tf17hrFhr5rAGPyS_3ckxI-3sRCuZX0adJ4AzE7wlCMlkx6Cq-kxyALBrHnuQMT-FkflOx28S0aM1IxKDsLzHjK4Z3Qn-QALQiLe-sDBGMuBpSZbe-vtrkVsdkh0bggmf4DG2cXbsxQrldzr4FSJkq7fqa2P62PMxtnyVh4k_gGBVnxWNvCCCcMTO8bMzLg6ZewzEQXxpE-SsktQqjmeHXER6E-Q6BU3Z-ZsaV8HUfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚽️
⚽️
فلوریان‌پلتنبرگ: تاتنهام با ارائه پیشنهادی خواستار جذب گاکپو هلندی از لیورپول شده. تا این لحظه توافقی صورت نگرفته اما مذاکرات جدی درحال انجام شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103683" target="_blank">📅 18:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39bb1f1755.mp4?token=nGWnYrbBN1SZhacpl-0Gz4I2jeLHqONil-xA0tjsao1kJiVpZnPa4WedyH0-CYFU05iaSWAGKQpMUkYkA4fxSvwk8HetlJkRk2EpaQ1HThswDiFRhCXaZToy2oZeJjWH7Y45JJC8bc0rZGU_Ms1jCTez9kmCQt1u4_CMdz5o_UIe2AWEbUSUkXgvNxSRJq78Hr5N5B9dZvOT_sfVc0NKWvw4i2TfaODN3IS3fMUCoReEhhnMIKOkJeINYSlTgx2dlFufCSYTLuklF7y0cl-MjdYvTMu_AIzsMKPuLY3ovpfPByLI5OYRewJIo_MaInPnk1DsM4Vm88nGLJxDVVnY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39bb1f1755.mp4?token=nGWnYrbBN1SZhacpl-0Gz4I2jeLHqONil-xA0tjsao1kJiVpZnPa4WedyH0-CYFU05iaSWAGKQpMUkYkA4fxSvwk8HetlJkRk2EpaQ1HThswDiFRhCXaZToy2oZeJjWH7Y45JJC8bc0rZGU_Ms1jCTez9kmCQt1u4_CMdz5o_UIe2AWEbUSUkXgvNxSRJq78Hr5N5B9dZvOT_sfVc0NKWvw4i2TfaODN3IS3fMUCoReEhhnMIKOkJeINYSlTgx2dlFufCSYTLuklF7y0cl-MjdYvTMu_AIzsMKPuLY3ovpfPByLI5OYRewJIo_MaInPnk1DsM4Vm88nGLJxDVVnY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه تند هوادار استقلال به عدم اعطای جام قهرمانی لیگ‌برتر به آبی‌پوشان
: اگر تیم دیگری بود جام را با اسنپ برای او می‌فرستادند. هرکی بماند به دل می‌گیریم هرکی برود به گِل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103682" target="_blank">📅 18:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=JZ7cQSXSzjOJ1rkGsWdPRz9Ru8DXcj_T3RZd_Je3zpiE3FOMuSK0Qt4SjE-qB_aR0SS01EvZCLGMR_L7RGTiPOiCMOSVVw3MP8Lu9NlOhdDaACcF782gNp18TRpa4PJM3wGcwEWJBzY1whdqdrnj9DXwXbyNpG-eqfJDOl-kfPH_bUhihU9hZybb1sZSgpcVslbikn3IHq8Ekauum5WizzOOHJef8LV3WULqZnmGSP_-gckSyhQ_vN0luRqgouxQzhgPB50quwj0HZOjfiYHwqC7hIieGFyb1Vnh575_hobVHHKsHnZrAcUL0INuPUj91BrAU7S7MLiwF4IDrrzUDw_BMrEZu4M77q-d6rmAyLMxxCIIGJh_Ku6HOmYPKitQLGwE3TTRxwqcv8QEqquJMkYkBEYtjFT50qJ3urvPHFa-VwZ3bi97tFaqfwxmGspnBm-G5cNOVhRLEZHN3h5IQXOr1zAV3VG6QIV4dgj-rg9jTp4WMjCWMNuQdJYRu6eCXzK8xsjfpGTFdUB3xF0HThlSjdD7VV08evwGo9wgZnMFu8Sfg5t3-92CdNld2hRnVAnLMCaZE3N2leb2stU9nwmobHZ7lg7i6rheg5Fzw-_OndEKxWdJS8rbKRBc4rFSEODz9-uPD5c1r_4QWf3zpvxn5B3iiELQ4PBJvuNQU2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8c8204fa.mp4?token=JZ7cQSXSzjOJ1rkGsWdPRz9Ru8DXcj_T3RZd_Je3zpiE3FOMuSK0Qt4SjE-qB_aR0SS01EvZCLGMR_L7RGTiPOiCMOSVVw3MP8Lu9NlOhdDaACcF782gNp18TRpa4PJM3wGcwEWJBzY1whdqdrnj9DXwXbyNpG-eqfJDOl-kfPH_bUhihU9hZybb1sZSgpcVslbikn3IHq8Ekauum5WizzOOHJef8LV3WULqZnmGSP_-gckSyhQ_vN0luRqgouxQzhgPB50quwj0HZOjfiYHwqC7hIieGFyb1Vnh575_hobVHHKsHnZrAcUL0INuPUj91BrAU7S7MLiwF4IDrrzUDw_BMrEZu4M77q-d6rmAyLMxxCIIGJh_Ku6HOmYPKitQLGwE3TTRxwqcv8QEqquJMkYkBEYtjFT50qJ3urvPHFa-VwZ3bi97tFaqfwxmGspnBm-G5cNOVhRLEZHN3h5IQXOr1zAV3VG6QIV4dgj-rg9jTp4WMjCWMNuQdJYRu6eCXzK8xsjfpGTFdUB3xF0HThlSjdD7VV08evwGo9wgZnMFu8Sfg5t3-92CdNld2hRnVAnLMCaZE3N2leb2stU9nwmobHZ7lg7i6rheg5Fzw-_OndEKxWdJS8rbKRBc4rFSEODz9-uPD5c1r_4QWf3zpvxn5B3iiELQ4PBJvuNQU2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
هواداران تراکتور امروز در حمایت از بیرانوند، علیه اسطوره علی‌دایی فحاشی کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103681" target="_blank">📅 17:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuPIsGDcjHxgfE0LhKht9KTjkAIgJlJfAlEe0cwIZOdzugBwvrw6DKuHgwksNz_ChgCTGJ5_-GQvZP_npe8AOXyCPpj-_d3m-5N-DGrq25xyC2PCSNewrg-Q33Ellk_0kWCosXJaO8GObD9kkldPUScSgO72a1lr_eAkP3CFMStytOQ8qio_aNecPgGyIFVoJA7HiTM_OR9NtIabHaQjOfnyPdMg0KHAoftFwPFMgcG8pOJM2ujv3D3I4DzNsolC4SbcXx6SO6bAlCxVNoMwYdNj0y2tS1maObMfHamtg5b8i7QiQJgM6wiu6ZYur0_GvlX1uZ-SiTsqu1KUN9GHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN آرژانتین: خولیان‌ آلوارز از هیچکس عذرخواهی نکرده و همچنان با جدیت معتقده که دوران حضورش در مادرید به پایان رسیده و باید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103680" target="_blank">📅 17:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8BEnwXde0KBeELypgwxk4XeEEs4wiwfWrHvhlYop3Jynmh4K8yGWn8kJMcBKlmSJ92kYNgWKve2rJ5Dt345xcs6vtHDmv7f6VBeEPrvMYNOTdKVCuXX5X9PfzL3jEhT4qnxToMxTQkaBScksmxhyew8jZRTp-NZ-SdNwV7s77Z6votRb4Ii100mYwfevf5PyhuBD0QEQLH2YcN9grpgh5jqfQSrARdMqh5BMs1Phbw2e1nfnRZPLBs_8rNFkfjFLCw4qp1btxG0uc6KhvXJH3BFX9Gt85INinlLyUwoUhigwl2W979KB-tIWSK82sI6ZMALRmaheCpbVDALeOPZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه کادناسر: خولیان آلوارز در جمع بازیکنان اتلتیکومادرید عذرخواهی کرده و اعلام داشته که ۱۰۰ درصد به قراردادش متعهده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103679" target="_blank">📅 17:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2bb45d8cf.mp4?token=av2IZ1pochQg8N_C31iiK77HqY5LmTnU1VEJ-GV-41FKLCWVgyOn5_AYtin_tcEPteA02oVPpDMQd52Id1UrWS5z7PZJjUQJxMoUSg9ziI4bwlVozIUYe9bz1n3eLAx8DflTc3AMNSPfAzDvVUM4MG8fnlFamUtssZOQR1HAJk4o7l6fj_E9cQebAlZEKoh9-VNDMOtyMq_l4-GRBtvUmNX0kA9Si09cU6ExygUGC48FA69zb_xj40NAyGqxJlbQEpNvqHjxoiNOutRoLpBkDLoO_oYTr0XK9ArW7JIikIwnY8eLIDW_ilPXZODAKMl7YFhi1Lhj_-mjmGvnNQjqNko23YVTdlp1zkR3kikALHtNtKKOQ1f6saT8fcwPB4u14DaKdiU-cH2vy1wBaAwy_r-_OE0GHKXLQL_OjO1-xhMFE6Ibdo6Um57x8-sp7YjOpgu-SjPnTIqk8-37_G45u7V8B6vDEic3mv3i5i8ld_VmT8EKomDdCeS_CUOIOVAjUYuDWV3jgOPD6ApjXStbF5R4uewA2cjH6bxs48-uSKpNBp6U2odNdwBy6nZIH_o2cZMNFfM3jnssUgZqtrbtPrk6iRHmMwHxQEzToikOhaFmvAK_XaoKYXHTVWAe5TbeoKgz0TsEk5fhKsm_VnaC3P-KIWFGfcEzYsWSfZ3NdpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2bb45d8cf.mp4?token=av2IZ1pochQg8N_C31iiK77HqY5LmTnU1VEJ-GV-41FKLCWVgyOn5_AYtin_tcEPteA02oVPpDMQd52Id1UrWS5z7PZJjUQJxMoUSg9ziI4bwlVozIUYe9bz1n3eLAx8DflTc3AMNSPfAzDvVUM4MG8fnlFamUtssZOQR1HAJk4o7l6fj_E9cQebAlZEKoh9-VNDMOtyMq_l4-GRBtvUmNX0kA9Si09cU6ExygUGC48FA69zb_xj40NAyGqxJlbQEpNvqHjxoiNOutRoLpBkDLoO_oYTr0XK9ArW7JIikIwnY8eLIDW_ilPXZODAKMl7YFhi1Lhj_-mjmGvnNQjqNko23YVTdlp1zkR3kikALHtNtKKOQ1f6saT8fcwPB4u14DaKdiU-cH2vy1wBaAwy_r-_OE0GHKXLQL_OjO1-xhMFE6Ibdo6Um57x8-sp7YjOpgu-SjPnTIqk8-37_G45u7V8B6vDEic3mv3i5i8ld_VmT8EKomDdCeS_CUOIOVAjUYuDWV3jgOPD6ApjXStbF5R4uewA2cjH6bxs48-uSKpNBp6U2odNdwBy6nZIH_o2cZMNFfM3jnssUgZqtrbtPrk6iRHmMwHxQEzToikOhaFmvAK_XaoKYXHTVWAe5TbeoKgz0TsEk5fhKsm_VnaC3P-KIWFGfcEzYsWSfZ3NdpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار استقلال: کسانی که چهارجانبه ما را مسخره می‌کردند، در سه‌جانبه هم قهرمان نشدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103678" target="_blank">📅 17:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meaS92gPmI4eksCvbZpdtsLdSXYEbDQEjLtS_1RjvWuVoUPTa9dVtGSTVxvFxOaC2TxK7IGJFOa4uVy7fJKdoidlsx9e6y8xgmGZpDABLsiQVUA7OWWYgDyRydy7HAiUHDFSlMnp5s11Nu0X5XgXiTjVKyZrNcTcP9i47O_vjWe1znJbT7BKDjKlWNSPy3bNSeWu89CU19UT6wnWM3ZVPQvkpBwlAVhCA-uJDTAvWU1L9pWYPB5uHMsl6rdhRDsL2ZhMof5f_TzvpAzVEIEMOkQlPrY-nWesNNyniCNMy3J68srzCMx-etvSK_vgY4mywXmoYZgd4mP2Rqv4GlUUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه ای بین آمار کلی کریر نیمار و هازارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103677" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23868bec2d.mp4?token=Xq4Q7Y7SdapREVoy9Qd_2-Qjeum4fjb0xZyAzpXIXp6w_CuQ2tNSU1_VOFAokELPG8fuPUo0Dxyln6-pBQj5ntBudvq9SYS4a3DKjqd5NAqn9uaibp8yRCL4DcLgswikLqkIFaZZeSwqFa5R3bAGkWEaPMnECfEQ7h7zEVBUhFKJlfG9VE9pCx4vnDmgvHhWjg6ub_OwzBfUNMkSlcfZGGmZmRHceDJxgLOk5cinUYBoLRJjjp4F4rZqKsQghjzzXjAU8wq-WOTG2ZlMB76MSbhBKGBGB_xD_18B3JmHXwYzUs9Fpg_2JxjBtciVC02KjuAwk2h7bCfYw_7r4_dShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23868bec2d.mp4?token=Xq4Q7Y7SdapREVoy9Qd_2-Qjeum4fjb0xZyAzpXIXp6w_CuQ2tNSU1_VOFAokELPG8fuPUo0Dxyln6-pBQj5ntBudvq9SYS4a3DKjqd5NAqn9uaibp8yRCL4DcLgswikLqkIFaZZeSwqFa5R3bAGkWEaPMnECfEQ7h7zEVBUhFKJlfG9VE9pCx4vnDmgvHhWjg6ub_OwzBfUNMkSlcfZGGmZmRHceDJxgLOk5cinUYBoLRJjjp4F4rZqKsQghjzzXjAU8wq-WOTG2ZlMB76MSbhBKGBGB_xD_18B3JmHXwYzUs9Fpg_2JxjBtciVC02KjuAwk2h7bCfYw_7r4_dShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعضی‌وقتا ممکنه ورزش مانع سلامتی بشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103676" target="_blank">📅 16:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d03b913b.mp4?token=DeonWTBshapUU7PT7LJZqsPCHSVtcPSEkt634Bc-_LS0EIpIxpMUZ3F0yQ2QEWh1hDcGqZvxuK8vgY6Y1d4vSNuT0XPzPdsC8_BkExFf8STJkmVXywtjvq2XXUJYJ9MGdlh9drv5QkGJy4dwG34jBbR_xzA4cCCOYom2D4VrQDCIW5Uc5-hU2H7-EUL5uvxstO30HO1rf76yPkcMVr1z61oitzEXOLesx1XmuFTIDs-t-z-uwOt6lvLsorU08HBkxSFLF6Q7xC_s4IN3Myvs5kOmTaXdiyIymzFY2bV_n6ChnjhUqHfBc-GCQtNuzyCm5aEk-4QQIaDAK-6VJM6CAYEm2fNilOzVziq1tzVLB-bwJxEiDRNdCSavbvjV-Do-TzOVX7nLnP6om37jtsCxvjg0ZexbQ4g97eDHrrxUR2HdwvIizpBlpt9HvmBbZX4VTfw5mDw9jDfaLOXaCEIXA3CkHUZISoag_Ct7v8J-5S9tyWYZdl1iieOYKL54BbSCKZe4MhzSALrcVuQqukuUAnWSfoerWGhuirnRU-QND0H6cwoApE19AyqDzLVppBBNc-_E4_xiMUKmcKEnR3Q4uyoh4ZXVZotgXA3ZLXXseSnLe3LWxU-cE8L2EetvTkU9EFSLgucOBPMjO76ldfnuEUVPJnPhttiZhqAMPmCzb8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d03b913b.mp4?token=DeonWTBshapUU7PT7LJZqsPCHSVtcPSEkt634Bc-_LS0EIpIxpMUZ3F0yQ2QEWh1hDcGqZvxuK8vgY6Y1d4vSNuT0XPzPdsC8_BkExFf8STJkmVXywtjvq2XXUJYJ9MGdlh9drv5QkGJy4dwG34jBbR_xzA4cCCOYom2D4VrQDCIW5Uc5-hU2H7-EUL5uvxstO30HO1rf76yPkcMVr1z61oitzEXOLesx1XmuFTIDs-t-z-uwOt6lvLsorU08HBkxSFLF6Q7xC_s4IN3Myvs5kOmTaXdiyIymzFY2bV_n6ChnjhUqHfBc-GCQtNuzyCm5aEk-4QQIaDAK-6VJM6CAYEm2fNilOzVziq1tzVLB-bwJxEiDRNdCSavbvjV-Do-TzOVX7nLnP6om37jtsCxvjg0ZexbQ4g97eDHrrxUR2HdwvIizpBlpt9HvmBbZX4VTfw5mDw9jDfaLOXaCEIXA3CkHUZISoag_Ct7v8J-5S9tyWYZdl1iieOYKL54BbSCKZe4MhzSALrcVuQqukuUAnWSfoerWGhuirnRU-QND0H6cwoApE19AyqDzLVppBBNc-_E4_xiMUKmcKEnR3Q4uyoh4ZXVZotgXA3ZLXXseSnLe3LWxU-cE8L2EetvTkU9EFSLgucOBPMjO76ldfnuEUVPJnPhttiZhqAMPmCzb8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
آبیاری ملی‌پوشان کشتی‌ توسط دبیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103673" target="_blank">📅 16:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103672">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33945d4986.mov?token=AUp8x-z7fdQKqlnHqmbi3uGggB5caI5C6JJs-p3yz0bKvBaS4Z_JmmFnP0maOCeLYfLQ_IvfeV4IL1qUxfzjH0AYuzIAzcuvh12LhqwReF1HUzfz0jAeBMUsO6-n6XixVOMY51plOw4DxKf_h05Fc2uA7o4bPX283OorhVqc8MVc6glL6kbfRrfXe8-BCmoHu5C-r34zlV1FEhVW5KUL3Wn5OfKihGlUr8OttAgNMzWPyo5txq_YfHpKRTC9iXLISKCPV0Ep0p2PzCj8afDiFrcsqYJzAL8S8vMiOIZgWtcm7j48f5tG4QQ2pgCBm3xsmcwABmtxmp3acET_xWeOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33945d4986.mov?token=AUp8x-z7fdQKqlnHqmbi3uGggB5caI5C6JJs-p3yz0bKvBaS4Z_JmmFnP0maOCeLYfLQ_IvfeV4IL1qUxfzjH0AYuzIAzcuvh12LhqwReF1HUzfz0jAeBMUsO6-n6XixVOMY51plOw4DxKf_h05Fc2uA7o4bPX283OorhVqc8MVc6glL6kbfRrfXe8-BCmoHu5C-r34zlV1FEhVW5KUL3Wn5OfKihGlUr8OttAgNMzWPyo5txq_YfHpKRTC9iXLISKCPV0Ep0p2PzCj8afDiFrcsqYJzAL8S8vMiOIZgWtcm7j48f5tG4QQ2pgCBm3xsmcwABmtxmp3acET_xWeOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
حال و هوای ورزشگاه شهر قدس در فاصله ۳ ساعت مانده به دیدار استقلال و مس شهر بابک در هفته اول لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103672" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103671">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk8J4HR-tdbd0ideF5r6qnTxt3SZ0-9F85zp3peFU_EyOnXEXiHkcMYjz_G2oslXnZeFp9Eai4kv9UxoVT4jDmRTLGfddv3egL--syrYwUMWYg-oUgLi90CZ7Ud8TPZW6UZt6oYuLfoF9rpVpcCGmUMT6cz_hFIr4gFClpgkeTayfDJ012UcH26vAuV1gPqY7ptDfET8Xb5fkzBqrnZ3-XFd-QkmEVByjzJm5p-GaJ_JxmksYDq2mS7NaCm9B8p64lAZ-ADTE2VrQ6-W-Njx_13g6e4zLwgqbVpJ7uBYnmqm5kveCz2sgj8YGY_JxnfVXw9tGsvDpI7RyeeTYK7UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
🇵🇹
فابریزیو رومانو :
اسپورتینگ لیسبون به‌صراحت اعلام کرده که هیچ برنامه‌ای برای فروش لوئیس سوارز در تابستان امسال ندارد و او را بازیکنی کلیدی می‌داند.
اسپورتینگ از ماه ژوئن، در پاسخ به تمام باشگاه‌هایی که به سوارز علاقه نشان داده‌اند، روی بند فسخ ۸۰ میلیون یورویی او تامید کرده است؛ حتی نامزد ریاست باشگاه فنرباغچه نیز در ماه ژوئن برای جذب او تلاش کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103671" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl01_rQuSTvecKFuVx7m2YAtZxBCjSsCYrF_rpjEzf158HEjcc1ab9DhZgEnB-azvAc7jNOstFtJublQXCip7v3sGGRlJgVpxYFwZhATCOqXOhuaTLMLRRLI8MY_LtoGpOxIMLQAVHkyWiBIOHZftpDxbwRu5DjKyJrpN6MtiFjq46d0YBJFBCWMiCpgRTfhjvzVaTkpVRD5TwSZDrfu0btbXIaFdZTQqaBXdHOeiwaG184vEKM93imxbxBmeAa_9GfO2MpGpmMHtH0pjlMaUhsaERkNYW28zhN2TqTOYEb9ukNs8m_KbCSRn7fjinkCsW36Lf0N6LEY9WHs_1V4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
استقلال
🆚
مس شهر بابک
🇮🇷
🗓
جمعه ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103670" target="_blank">📅 16:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103669">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e235e80b49.mp4?token=lB298Q_ChQKSo256Tmt-mC3t-1y9lfTx72jB5k6AffDaX6ABg1c3MJcHy8qQXfffHu9a4uyy1wQQiAchtVXLhZtOtX_SIobI8SsH_NwzNiilrDS-K6GWgDTdoN3neFM3h1aQW5uyb4Qt01CDz5xxGf-xmHwIbi_25JHS_tKYtK_GRoNBnM0cL4X9ckpAo7N14SjP9IkQoCxhn1Wj9UP_yZ2rj_ARbKMt0vzBt0uTD2Sdrhxj1wW9onv0i6twqpARs5D8VQYs8fnGQoGpcXxw-J_xRDRgxzglCi4A7kvUg5UWYqUc99qcGLN6N7aMaxPm_zcG-HN0eMY6EXgRHWBb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e235e80b49.mp4?token=lB298Q_ChQKSo256Tmt-mC3t-1y9lfTx72jB5k6AffDaX6ABg1c3MJcHy8qQXfffHu9a4uyy1wQQiAchtVXLhZtOtX_SIobI8SsH_NwzNiilrDS-K6GWgDTdoN3neFM3h1aQW5uyb4Qt01CDz5xxGf-xmHwIbi_25JHS_tKYtK_GRoNBnM0cL4X9ckpAo7N14SjP9IkQoCxhn1Wj9UP_yZ2rj_ARbKMt0vzBt0uTD2Sdrhxj1wW9onv0i6twqpARs5D8VQYs8fnGQoGpcXxw-J_xRDRgxzglCi4A7kvUg5UWYqUc99qcGLN6N7aMaxPm_zcG-HN0eMY6EXgRHWBb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تمرینات استقامتی و دشوار شناگران آمریکایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103669" target="_blank">📅 16:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103668">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a17a82813.mp4?token=JMYsl8JlDsjIKa6TPvnru0feHl9hHmNKp5pn2faC5CDX-3M1G0LOt46XoW_H6hFzago7aZIhPeH6Uka6p67ZPLq28UYLq3hlbhjVqEDVsAFCKaZCrhaejzLVyt_UD0bHk9boqJYvCCc9RWvay3c86E0lGl8m7CX7mo-CtBTbwPdpPhIxdTt0koHv8DNzzIRWFvNhdo9ZOCZzhZVUt-UZp2OZt4eCPc27BVjzKlScae82Pg8AuJ5vvp0BJEdD2NHg7fbZzJeBgsx3tB9rikRmQpoIp_2Ge-SmVfd1-PYr7TaZQjF7g2UO9-Nbs5p9ymx2U_PfGVdSM8anMi8AfHXaYzEyi3vL9_QHu-_xqE2hVkbxXZ0TRqfFeow2zeOTD9EVNNMWu2-t4wo92MENPoi2XRMU3w1IO5j2S28zDeLhG4K9PeltMyvAbPFArq8bV3Lz6VcO8XaLVtv6oa6Lmz9lOcmIjbegUz15QSL3_f_ODDdY89HUDyUQbE1Z2NzoNJi0DfMRA6dBWdkzmD7FQRRkaIgYARaMBlDyJmUhun31IDJrvtIqTYEyPkZCfbEmY5WeG9eL3UmqzFnlZFlyzkRoPgpWm9rQJSEU8ToG0fm0bD9mcHJ6H2wZpQug7swf_mZlavFwRXfU2QPyYrcHzgzvVdn5CFOTTvyQgnl75H-f2uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a17a82813.mp4?token=JMYsl8JlDsjIKa6TPvnru0feHl9hHmNKp5pn2faC5CDX-3M1G0LOt46XoW_H6hFzago7aZIhPeH6Uka6p67ZPLq28UYLq3hlbhjVqEDVsAFCKaZCrhaejzLVyt_UD0bHk9boqJYvCCc9RWvay3c86E0lGl8m7CX7mo-CtBTbwPdpPhIxdTt0koHv8DNzzIRWFvNhdo9ZOCZzhZVUt-UZp2OZt4eCPc27BVjzKlScae82Pg8AuJ5vvp0BJEdD2NHg7fbZzJeBgsx3tB9rikRmQpoIp_2Ge-SmVfd1-PYr7TaZQjF7g2UO9-Nbs5p9ymx2U_PfGVdSM8anMi8AfHXaYzEyi3vL9_QHu-_xqE2hVkbxXZ0TRqfFeow2zeOTD9EVNNMWu2-t4wo92MENPoi2XRMU3w1IO5j2S28zDeLhG4K9PeltMyvAbPFArq8bV3Lz6VcO8XaLVtv6oa6Lmz9lOcmIjbegUz15QSL3_f_ODDdY89HUDyUQbE1Z2NzoNJi0DfMRA6dBWdkzmD7FQRRkaIgYARaMBlDyJmUhun31IDJrvtIqTYEyPkZCfbEmY5WeG9eL3UmqzFnlZFlyzkRoPgpWm9rQJSEU8ToG0fm0bD9mcHJ6H2wZpQug7swf_mZlavFwRXfU2QPyYrcHzgzvVdn5CFOTTvyQgnl75H-f2uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
🤣
ورزش جدید هستش:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103668" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsH5jbwF0lFMGjZDF0LXz7n6RGW26eNUEN06wyBGU4zQTCJtrGORjmLzDxOrdtFreCyOPTcOu8HmFRtq2hBNV38Y5bf_AbWUsbib0kiL5F4oQFnTNsgvVI_FwwQxtmCb7ZWA1zTldQsoEI2Vz12Y98hb6FQrmOjxTRgBi5O_aac4JS1vsX-9h5huRGhs2zMRks99VSsvDoNKOAduI-paD7nzz52Xeot-WbLIXb6TBPtrzoUjTplXeKJm6dk52kDehk3Fpd9rfka69JRz-CChhnY8L4gu7ZkAVpW83_WCkmqS4NdxOw88JUaz5iIttYAwTJ75TFoNQxkbt2b72EAUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
به‌مناسبت شروع لیگ‌برتر فوتبال ایران؛ مروری بر فهرست‌پرافتخارترین تیم‌های این مسابقات با صدرنشینی قاطعانه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103667" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LchuXUmyGrcoakW7e6ySz6FrBaY9kYuTs4b6Jen-IFLkfSriRby7YHs5Ke7HbcYLyI-I8rgyzt65GWcpg1xtPekE50F1vDghHFhhlhx3qZO_rQv8dSpOFe9kxII-uc_6HqB-0og_03xiYVT5OK93n4Ktw_rOnriQwSUz2wY9EUvOHPdjCsw6ROdhVsM6j1cyZocxK7U9PujriK_anVtUtqqy6vv5WB3m8lP3UvUyZc6ZDqtIc3Y34cqNGGxZb9K1XhhYfkl94i6l5QSCk90lmg9kMIieE9CMT6up8hgkyTUtahE0uh_Q7k9pRVZ4CcXnw8dg_uXvITBTQHNPyxFTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽️
فابریزیو رومانو:
میکا گوتس وینگر 21 ساله آژاکس به پاری‌سن‌ژرمن پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103666" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxz1jLEAxjgCx7gl82rROMJP14M6TLcg5c4uxxRLLgq0OmFtNh-y4js28alb7xnvM5JSUL2uJYb_OUzxkOn5oRCpcP4tAHyeTqT-gHuzGBIGNeVCwUD8jQq82tGEhVHVs0EV7etFkF2HCLrbPW4HctcYxhl4avtkjwxqgAeqKhUebHDXVEc5lhc4LcQUXp_nEBAX_E0kzbSfWVNpPyKV2As1fRBViwukqzdWjNbIk0Pd1hPgX1RD8-2Jg6nzGnSZWNuwXz06Y3Fkc3TRRpkGdextcKbMqAYLjBs3nyeKcjRcNMeFIDJn6aYRblNusq9Qe8i8xi1-tM8PaFJe1QjIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
⚽️
آمار جواد نکونام در تاریخ لیگ‌برتر؛ ببینیم امسال قراره برف تبریز رو ببینه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103665" target="_blank">📅 14:50 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
