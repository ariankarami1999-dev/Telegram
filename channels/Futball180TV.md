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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 294K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLt1KVheIGQD5Zb9fOe1ouZ_wIasXMXetC567a6SdC9wWbM1te_srB5aciFkdDDP8Z_BtOw1VBKcDwYSeSv3TwfVXg7IaDAsACNk_wNOlInqpTrCntZeFlToAbr7i7ykXqrn429BjOCng3CZesFi7EyZQlGXAo8z7bIMJZjh5x1EUqod2L5J3_YPWEyrGQiyhKsuPlWzim9C1sH9r3DAMuXjlt21Tl2mIFusWN5IUIN7ps9h6lCybGHd612O9mRl5xWnku1P82pyzzxed6PFi_rnc88cOsHxv13kgv_QrpA7GQPqZqc3auEBiy8uG5qR3z7xfkFOu6KVzz0WwvmfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین بازیکنان تاریخ جام جهانی از نظر امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 620 · <a href="https://t.me/Futball180TV/91666" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=QElmpET93eqHe-UQ_9MGjduDh2dWNjHmXQcEekyS68okEpUyfBmb90scU63Ak5__PYKYc41chJp_11F4YuXEjDo86oA5jpC8gT6z6015MIdSCAjxx5-3wI8ytK2HX6Q6kAbZw6pHTy94-tY9qKoxdAKEb3hHbUOMQ1ntRVtLLXzW7hLcRwt8yPkAABQXF9j4Q2x4tYn7sq9lL0qucoR5snGz-LiD72IEnFQH7lJ1jqPcny0Yhdd766jWCVbfCZP-kV4xDCs3xgXRSJnBOVoX4MQ7eGa2cXmEh0_cFsT6RNoa3NR3Y74UETzT5bk1yVxyHor7mW9o3uoDpYj07HKAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=QElmpET93eqHe-UQ_9MGjduDh2dWNjHmXQcEekyS68okEpUyfBmb90scU63Ak5__PYKYc41chJp_11F4YuXEjDo86oA5jpC8gT6z6015MIdSCAjxx5-3wI8ytK2HX6Q6kAbZw6pHTy94-tY9qKoxdAKEb3hHbUOMQ1ntRVtLLXzW7hLcRwt8yPkAABQXF9j4Q2x4tYn7sq9lL0qucoR5snGz-LiD72IEnFQH7lJ1jqPcny0Yhdd766jWCVbfCZP-kV4xDCs3xgXRSJnBOVoX4MQ7eGa2cXmEh0_cFsT6RNoa3NR3Y74UETzT5bk1yVxyHor7mW9o3uoDpYj07HKAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
بعد شکیرا، اسپید و شیدا مقصودلو، حالا نورا فتحی هم موزیک‌ویدیو جام‌جهانی منتشر کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/91665" target="_blank">📅 13:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=fOIl6YVEJB5OCy7KSIVgczXKL0lCcbRZrK77jhWJ95Dh-Ac05NUAwFS7gx6TD7enW59go48_pfj4dtDRcsU6DmJCjHrjT0QnJW3gVSxJZbhkM0OUui_b6HnQWgFXVbbAeGLR1lfb1djBT0L-7ufRuqE9tvB3Uv8HBIg6jgy1QJGmIvtQMneQg9wRzbd-pu2CVmIrwUzO9AeZoPCMaojdzEpQeXEHnxVBVFocpbw9PmCv9dwgrZ3964ZRZCji-ZbC_0xclW6XXkLPUWtYNAiRWDypS7iLlQiP_JHahgZxL9ouFxBW0XGPFStCnIvh_WJrJHR-WAtC-ngvGsyxHEAhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=fOIl6YVEJB5OCy7KSIVgczXKL0lCcbRZrK77jhWJ95Dh-Ac05NUAwFS7gx6TD7enW59go48_pfj4dtDRcsU6DmJCjHrjT0QnJW3gVSxJZbhkM0OUui_b6HnQWgFXVbbAeGLR1lfb1djBT0L-7ufRuqE9tvB3Uv8HBIg6jgy1QJGmIvtQMneQg9wRzbd-pu2CVmIrwUzO9AeZoPCMaojdzEpQeXEHnxVBVFocpbw9PmCv9dwgrZ3964ZRZCji-ZbC_0xclW6XXkLPUWtYNAiRWDypS7iLlQiP_JHahgZxL9ouFxBW0XGPFStCnIvh_WJrJHR-WAtC-ngvGsyxHEAhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
آموزش رقص در ایران با موزیک دای‌دای شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/91664" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4qf0ExhAjhX1Iz7D96vgE96QlKUoM-cSwbyXx1sAr6DLGZgf4f2DKiyMlRxJF-24hb7HG8ESwClZRw7fAtWrvN6Ns7nYmKgqAnt69g6rPxWPaoVf9WAhuoGQUR6jhi0iAVWGimshJe49oz4DyBfPK9ELHv2c7oRkL4O-HBVE4mogpafWYysDT0KKD4ScO_HPygif4SLhCpKOC1m1XE6pjIrWSWqpVapMHt5w0ERILQezExgzdoRGgbCaaXQeVjZxiSq-Fnq6_7qXQ533D0sBNPpRyFDCryedgkvSG6lfPVkMsqkfKrS0Jw7NGGqs5RiFEH2xMXaGdyy2rQs8E0e9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
✔️
پسران رگنار و عکس رسمی برای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/91663" target="_blank">📅 13:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d43531369.mp4?token=pkl1cYsPsg8uYdXEY26cYXHGSnEC5W2Cqz2s7Zq64_AhmH5mq1CT3Nbyq_9rz9ZRwggl7ula3SUkBwcuwaBv9CJQsEsQPttyhTfaXFQchFiX1iMHyyW_uZGkXljCVowKdcDZ1xatiPnKZFtNT6ebz68ddBN7rhr-UMsa-Od64KFBTR0MMAhVLisYwmPqxNTUXh9h7JbYQ6LYmYb2tXl_IeJWpUHH20h_tdHU-QsVbZWybNnFDyNcjU1eJawJP5nJy1gOBxfeW_e0QbblMGM0fmkp_QGtadASzZIeUA443ClZG6XFoX6J3AyVB93Jeqd4SPCww9-mDc2aW_7GfTvh2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d43531369.mp4?token=pkl1cYsPsg8uYdXEY26cYXHGSnEC5W2Cqz2s7Zq64_AhmH5mq1CT3Nbyq_9rz9ZRwggl7ula3SUkBwcuwaBv9CJQsEsQPttyhTfaXFQchFiX1iMHyyW_uZGkXljCVowKdcDZ1xatiPnKZFtNT6ebz68ddBN7rhr-UMsa-Od64KFBTR0MMAhVLisYwmPqxNTUXh9h7JbYQ6LYmYb2tXl_IeJWpUHH20h_tdHU-QsVbZWybNnFDyNcjU1eJawJP5nJy1gOBxfeW_e0QbblMGM0fmkp_QGtadASzZIeUA443ClZG6XFoX6J3AyVB93Jeqd4SPCww9-mDc2aW_7GfTvh2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحبت‌های یه خانوم دهه شصتی که ده تا شکم زاییده و میگه هنوز این تعداد بچه کمه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/91661" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91657">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSzCPpzsTSvyb0wPVb4KJ-fKq7QkF4i-w2ujL9q2CU04r7mg7GGv3efpN1PBksVL7nCROHiEmwxPHMbMDf82OxAkyKML3gp1TG-t2r8iymEA6gKkHP1p_Yl5a5iBTa2JU_bhW7XL4kMCkcGbgTgS0t7-CMfIdc6nUsZYSxHx6TTudWGMoCT-oaYJsO46CJ8HyRikoy0gD6d3_6IYgFtiIenVCzHoiAYPUkEHCiy-tolP9Iw4i9MVcGRXW49FlmLVXVzXcHDGPCuzeMYCjXvEX7VQnj0boC_D0gSxLisg6T0BWw-pVtaeCPxUECNEAmwMNSRCTOze1Q9unetzmquOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0rdN4OIj-6M36u8Ym3JNfquEDDS_zVLQftlb8wZJ-w94b5WNseQgLonRYMTZJRfrvXEo7hL6N2Gc-G2jGx2UCnwLUw6ER_Rn_AVQmDrY577Szjcbco7kVJTCNtp1zYxqAnkUY5Ucg0rQlkbgt8xEy1yumrtNlkyO668TqusdSP3VtpKjtQrvJg3Q0u-PWGfq33ml2Ok6XDWRZPiMYNCP0eMUr8zzoftbBV1o2O2brFiriT1PHRjOzoM0nvpyzWqC42OcqO7PaePtm2VeLTD_OgX_gmVkyc9L5_D21KeS2i6N4bcRzZ9hXEa0M2qiOsDn8CfaRb20OZpxeAYuRhHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZ4_SDufbp0C0znkt1uzW3oNUIxWMnUeDp681qa-wnoKJZOcb0JSW0O8wdxsucoKRAhA1-gyOTwngGFoo8-ERuAoFs5a3GF3b6iJzWqrGKY8bciCxN2Iy3pgv8PHqo-NwqNJzv4RUCML5qpFYxdJiufCOuaRVrANYOYO8cRIKApclEgV3dlp4A6ApWn_5yulaEkNYVLFqTt0ie6tpyvbTGFAv4--w9baPm5IC5PxQkzFdDfXmp4Yz4Ca-M8cnY7cRDiGmme-XE56y1iAYaHb4AsP8Nukiz5hPTAg3RK3uAMePUTIBVhs-xoeBm0bRhd-4GNfBZPhQWAh1gyywjZESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBJ7qv1XEbAd49Tr4N9W1LTdNwr2v0vhBqewPpzOabW0bHaomAIxmkFgFD0NHntGRQCNPwneSAn69_Zz6hZLVyLGpNiMsimpxBg6fzsi8CWF_tUM3ga29dk1zjSHJ71BUtcrd2X9uEcDTDNI0rd7cTl8pDwo_Km78xZ8sMxbGipOm2OU7aEMTz1_nmtOdvaghiCe7Kb45er6hODl6G6tKCN-Oiauymo2YUYsPjrtAGFGELXY9_s1lbeEM7IxLIrzY0u0S18vZxBen7d_ovST21T74_tf7ElAlqQu_FAIHS3vLNBnQUBidqyfGxKgk1f7XReqFl5XQyI8B_bvefrVlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
داوران چهار بازی اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/91657" target="_blank">📅 13:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91656">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ckeSX3PPyt6KG6ArsePDmGU9BWIu-bkZqt4zQCckLwQTMRMt_G-AIC6cBuAo4vZu5tLL4RBWC0PLXrG9dhX5s4CVCYJxH6LcY9qyropYvzWMQidOsKwuForw7qARF0eZJZqnDxBQ1ZGNTc3cL3np7bRgZD2HkbTSv5ql2fMVuOFrFeCEu1izUqrATVQF2wx8LVAkmtndxY6fDTCxzTHrAmoYbDwVU7TmKiqGRwuUW-1zTsdKQYKxInH2sb5a1Bsc9-MwZr9LFFHC0ZMx6I5z9Dtgx-oiOdZeb2CO6lsny1EjrxZLwl34uz-6rcWiNizi8EQsKlieTAo4wriGRWNWQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ckeSX3PPyt6KG6ArsePDmGU9BWIu-bkZqt4zQCckLwQTMRMt_G-AIC6cBuAo4vZu5tLL4RBWC0PLXrG9dhX5s4CVCYJxH6LcY9qyropYvzWMQidOsKwuForw7qARF0eZJZqnDxBQ1ZGNTc3cL3np7bRgZD2HkbTSv5ql2fMVuOFrFeCEu1izUqrATVQF2wx8LVAkmtndxY6fDTCxzTHrAmoYbDwVU7TmKiqGRwuUW-1zTsdKQYKxInH2sb5a1Bsc9-MwZr9LFFHC0ZMx6I5z9Dtgx-oiOdZeb2CO6lsny1EjrxZLwl34uz-6rcWiNizi8EQsKlieTAo4wriGRWNWQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری راجب وضعیت اولیسه و ری‌اکشن پرز
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/91656" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ادعای
مصطفی پوردهقان، نماینده مجلس: رفع فیلتر واتساپ و یوتیوب در دستور کار قرار گرفته و بزودی این دو اپ بدون فیلتر در دسترس مردم قرار میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91655" target="_blank">📅 12:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68f156545.mp4?token=DmpZzzeUfO4v8Em9rSvuJRv8rP14WKBNiq2Ch8q7QwXthe_kTrc3hjQMenj9dkpi_yp8W9YudQBjpmx9jEOoujrHIbdQDKm5jto-6Foy8Hnj6b3Co5DhLbTCQ-3EecmWBEmhHX_8BzhbUctn_JhLV_vVOsyIY_Ba202G6F-jlhIGfolEfRuSZ0LC0Anhyy8giXHJ7dluGAt4s33EtQ_XEzpxQJjzCcWdeC-N2H1_qJGfh-qHk_q9aH0mwenYe0re0gfoKvSWsPUNH_DwvvLqHSrf0koj5SMOx-2Rv1QunUcAUgny-ugwu5vRIJPyMELXMrrt6S0Kszjt1lSt_oT-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68f156545.mp4?token=DmpZzzeUfO4v8Em9rSvuJRv8rP14WKBNiq2Ch8q7QwXthe_kTrc3hjQMenj9dkpi_yp8W9YudQBjpmx9jEOoujrHIbdQDKm5jto-6Foy8Hnj6b3Co5DhLbTCQ-3EecmWBEmhHX_8BzhbUctn_JhLV_vVOsyIY_Ba202G6F-jlhIGfolEfRuSZ0LC0Anhyy8giXHJ7dluGAt4s33EtQ_XEzpxQJjzCcWdeC-N2H1_qJGfh-qHk_q9aH0mwenYe0re0gfoKvSWsPUNH_DwvvLqHSrf0koj5SMOx-2Rv1QunUcAUgny-ugwu5vRIJPyMELXMrrt6S0Kszjt1lSt_oT-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
لیونل مسی: «از نظر اهمیت، بهترین گل دوران حرفه‌ای من در وقت اضافه فینال جام جهانی مقابل فرانسه بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91654" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSQevP9AnUe18WI0DhatWxQT5YR6e2YpXrJGO3H5Ctd9j8i-5TZ9FYfOzaEYVpeNAo6VixHHCh5X7dexGKIzRvBDD0wK5v4Ar3cF9NhS-EeuCip99vaf0hv1N7HkHs7M5XH7GIboo_v18KSq-ZBWqnxDHswUt8NGJr8s6Ii37uWKrIMvOPoiyPG_IIbZltAyx2rb-eR1wxdMI21MZhSEGQOlP0u2FkOZntRc9hem9_Nfui4t-PPyOMjU0WDGu1KRu_9AvZilgr-9LUGVBQF4r43EHWmawEyfjWxxb11oqb2VclKLpocxnJc311UBFqF0hjzwaLyDpr0yz6U2cOYUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔙
هواداری که به خاطر نوشیدن ۳۲ بطری آبجو از کشورهای حاضر در جام جهانی مشهور شد، دوباره برگشته است…
🔺
این بار او ۴۸ بطری از هر کشور حاضر در جام جهانی ۲۰۲۶ دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91652" target="_blank">📅 12:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls7dlY5oklv5xZCw58DL2hnIxDGBqWWjb2yqjnunbt974DWn6QlacaJa8zjCeDO8RPOU-D8PT0h8Va4QPTdUdaSjD7CufYLxWLFFcIsg9CgObikyP_W03Yx5-U-EWahbvONZ6JYSYby_loAL8TXJeTiqObKNeXnXnJFEHyEQ4PRQaM8vB6YLRyEsf1PuQKLVj8X0-Fw46JdEAXeXIlGG1C8lrhlc6HXvUvBECaWiz_ms_I6-_S1capBFj3TY6usEWORPy5IVBJPbz-vOhy7Q2FSKn7C7SWk_DxfNlXJZpRCHS0yjKXC8Yxgk6fQfV-s3jBaoyuClE6RFcmAV6pQ4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژوزه‌مورینیو دقایقی‌پیش وارد مادرید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91651" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGuB-sgQ2ssfL9bUlQNbBybgSQ4R1Ar08yt0dYWvioemsVOlBLvEWQ8LqmWmAXw2nT9lFSADQR5DA-Xgy-yAgEltrZDtdA2bB9vfDMGMXQfDBriEPpv6j0l1J6OyWYFCFFVMlhN-w6ASB-QaJ1KJttEsWQR9zbbZdeJMBXrM9G2SYTYve6FOohaWjFf5PZCqVD08bNd-RgzzEr_6AaQsSaZVM-rPZYmE09k0DfVEI6jL35w5KopkbMl0zFxGSfkLBSr5u0BoYvDNmIvMd2IvScPQxXuJ1tGY6KiZvIzUJSesu-9Y1rAhIrXJyVcDmZugp24_dNAo9YfLjWW343GPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فرانسه در گذر زمان..
انگار دو تا کشور جدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91650" target="_blank">📅 12:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DgiYqHueVjGZPaA8lAdRLo9jvmlvxrWJdjq2Ws20cppf0tAumDtJrzwpCMXMhOQGjGwhmvpaSe093G1S4LMgerWDii4DMlI7aeO4VpTPRPPiF-SBs8jEnoKDs0ioxOV2_E7Th5gRati7WBPjS-kjnZGikdSyh_J9eHDj1p_mn6IsB1MwWNieHOniLC_Y5eVg0qsjJKYHfEl265PbgQWkK_7DbBN-WjJz0iZdTqtYIAtfTD_yUExDf5BfHwGjSZ0X1z5b_lyE9TnEX2269-X1Qumq3BA1VibPRtIRjt33_Yu51E0NLn8bRr4W_dsPM5ZJJsmKCsiSt06hIQW9V6E1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ دیشب سر زده بلند شده رفته فینال NBA رو ببینه که باعث شوکه شدن افراد حاضر در سالن شده و از نکات جالب اینکه تمام ستاره‌های دو تیم فینالیست توسط ماموران مخفی آمریکا بازرسی و تفتیش بدنی شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91649" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=bYCGRZVFK0fHUFDmI-9KqIn05yy-zRs5nmgJi467mp5wt7LxqwuO0PVZ0jlbEhGZeFPs_sxRLJx1mOG_0hyl4rZu5pe7wHjfQBB2KQ_iMna8BGRtOxpWcW3t3PQulCitz7QHyjp0NCaDaC58xOoBzwVcKXORngvL5ZC2JpxvgpIuaMc_brm07qPnkCJeXq5PuplmVPvEqaWZfhi1_HqDolTDnZQhu420_gXDJLHBtefrwWdq4-VsW8KDaXeiJ9qdP_-g1ucjh3CWTsxpkv6x4CUnOGa476KgN9myW9LXJnCiYHRPRhtYQr1I8CK11olRATQtPjW2J3MrduQkn6YQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=bYCGRZVFK0fHUFDmI-9KqIn05yy-zRs5nmgJi467mp5wt7LxqwuO0PVZ0jlbEhGZeFPs_sxRLJx1mOG_0hyl4rZu5pe7wHjfQBB2KQ_iMna8BGRtOxpWcW3t3PQulCitz7QHyjp0NCaDaC58xOoBzwVcKXORngvL5ZC2JpxvgpIuaMc_brm07qPnkCJeXq5PuplmVPvEqaWZfhi1_HqDolTDnZQhu420_gXDJLHBtefrwWdq4-VsW8KDaXeiJ9qdP_-g1ucjh3CWTsxpkv6x4CUnOGa476KgN9myW9LXJnCiYHRPRhtYQr1I8CK11olRATQtPjW2J3MrduQkn6YQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حمایت و تشویق کیم‌کارداشیان برای لوئیز همیلتون دوس‌پسرش بعد نایب‌قهرمان در رالی موناکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91648" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
🏆
برخی از درخشان‌ترین سیوهای تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91647" target="_blank">📅 11:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91646" target="_blank">📅 11:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9FSMOwkSoGXjMEk5P6jst4jE2B_p4xulLmZtuIF_svyLOCAX3HUSocCnE4k2XrHunYuHwPY_VKNhgzxwWlhQNCUUEP3aFkv-D4dsUIpZWX1Apz6mxBG-iD8I8akWziW1Sf-VjStB53tE5bFIo9RcR4WDuAnrYgfIdwSBIhglzlatqwBp0kUzOgB0qR8w5wuijq3du1um1THmyEvxn2oXMCNIP5IkGjLAVh5PP4BkQPRjUzX2pMP1yNwekIEOtmVpVYMv77XFvNmphl9EMfSNTqMwS2jRJ1MRQ48T6hdwPAy8ULi-H2Ee-MUPorHEYWvnpzyW118FCvFbK4c4tOMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از اتلتیک؛
بایرن مونیخ هم به جمع مشتریان یوشکو گواردیول مدافع کروات منچسترسیتی پیوسته و قصد داره برای جذبش تلاش کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91644" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk0Ta6J_AVR5LGRIdY4NOwQ1TXw5LRXxggFwJGmbUn9c7lgL-PiFHkLpNgtN0uL_uI1YnvP5DHqcBzcjIrn4-AW51Mc8EtTrKg6po8JeHv6y-QNfzwjpf1GhUKWy3TzeMb1mfuhzXJsreJebabfA4lCFOMk3ee79aGkqiMWWGXP54smhthSu4kyg_tOlD49-nAHqrw5bonDuyWz4LjcBb_Nwa-zIvoskYadiVNefWK7rI9ChlORxqKIEM0qJFUKt8BHQ8inZ62ELJiUSFsuG1aVokJkYcUqHpMDeKnpsGJxNLoR-pg8Vd2yK3Jjk2S9m3GCFkkuwRUywkOCRQo6YDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🔥
لامین یامال از زمان جام جهانی قبلی ۱۰ سانتی‌متر قد کشیده است. یامال که برای اولین بار در ترکیب جام جهانی حضور دارد، با قد ۱۸۱ سانتی‌متری خود جلب توجه می‌کند.
✔️
در سال ۲۰۲۳ که به تمرینات تیم اصلی بارسلونا پیوست، قد او ۱.۷۱ متر بود، اما با برنامه تمرینی حرفه‌ای و رژیم غذایی مناسب به سرعت رشد کرد و به ۱.۸۱ متر رسید. یامال که هنوز ۱۸ سال دارد، پیش‌بینی می‌شود تا ۲۱ سالگی قدش همچنان افزایش یابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91643" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91642" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🙂
دیوث بازی مرحوم مارادونا در جام‌جهانی ۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91641" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
ویلای ۳ طبقه علی کریمی به متراژ ۱۱۵۰ متر مربع در شهرستان لاهیجان توسط قوه قضاییه مصادره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91640" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=M575zIyRMC9RutKfCivLGtUCZ_GYf19-IrGqRWzA-78YWh0SHuZ0JdvEpsdO0HFuSjPeuhaJ9rWR-1EADMbZ6o6dolJ3meLjqIIde9GgeuHiYW-p3ZkJvRrWSevODU24oAPT9sB6giR7eI-LicJFvBq9L82GJT2Z1gCQGVEvjJZtJrNXEkWhrlO9saqsp5odSv2I0VG98vTUcK0PZx-jSDF27SeoBTjbw43BdLb-Ya3ZwOf8URjr0WgiiyMftHTBPZ1sdpdPaGtdkB1udmeQl2wQrAm0dqezZGbDLgpSWwrLIIj_oTuvZlMxOjoCS3CAc-g6c75XnfgL0UEQ00VUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=M575zIyRMC9RutKfCivLGtUCZ_GYf19-IrGqRWzA-78YWh0SHuZ0JdvEpsdO0HFuSjPeuhaJ9rWR-1EADMbZ6o6dolJ3meLjqIIde9GgeuHiYW-p3ZkJvRrWSevODU24oAPT9sB6giR7eI-LicJFvBq9L82GJT2Z1gCQGVEvjJZtJrNXEkWhrlO9saqsp5odSv2I0VG98vTUcK0PZx-jSDF27SeoBTjbw43BdLb-Ya3ZwOf8URjr0WgiiyMftHTBPZ1sdpdPaGtdkB1udmeQl2wQrAm0dqezZGbDLgpSWwrLIIj_oTuvZlMxOjoCS3CAc-g6c75XnfgL0UEQ00VUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
سوال روز مخاطبان فوتبال: یعنی آنتونی گوردون با ۸۵ میلیون دلار رفته تو پاچه بارسلونا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91639" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایران میخواسته یه بازی دوستانه با کشور گرنادا که کلا ۱۲۰ هزار تا جمعیت داره برگزار کنه که لغو شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91638" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUaDsRWN6fmYtmJOd3Coc2VsibJfKj1i33jvggOAUi84G2wQrWuGgTs6UrcnbxkEzl7leONUnSR0RbXzzQV-b3S2vt1U_eTEm1P8s2P7tTKj_5B_9_fN1JoprYFmIE0CcWSBtFoGpkOGCsH8HLpPjhqtYsXpco8GRbkHz6HfF9XT6-kXbx5mNAvPmSJZcjkYmDVfPVelbseEzIahEmMlInakOihqtEVaot1Bdn8_yoKMy1J_YF5fu08lPP5F_1FTfuQCBGECCemLt4gOvYQ9SYsHAFp0jWZM1HplbuilwQKUfmplJy9GGaaMXLbRC2kwsnzHkwyHKusJJR8AzkSGLWd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUaDsRWN6fmYtmJOd3Coc2VsibJfKj1i33jvggOAUi84G2wQrWuGgTs6UrcnbxkEzl7leONUnSR0RbXzzQV-b3S2vt1U_eTEm1P8s2P7tTKj_5B_9_fN1JoprYFmIE0CcWSBtFoGpkOGCsH8HLpPjhqtYsXpco8GRbkHz6HfF9XT6-kXbx5mNAvPmSJZcjkYmDVfPVelbseEzIahEmMlInakOihqtEVaot1Bdn8_yoKMy1J_YF5fu08lPP5F_1FTfuQCBGECCemLt4gOvYQ9SYsHAFp0jWZM1HplbuilwQKUfmplJy9GGaaMXLbRC2kwsnzHkwyHKusJJR8AzkSGLWd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از هواداران ایرانی بانو شکیرا هستند
🐸
😊
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91637" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🏆
🇺🇸
🇮🇷
کشور آمریکا خبر داد که تمام بلیت‌فروشی هواداران ایران که از طریق سایت فدراسیون تهیه کرده‌اند برای جام‌جهانی مصادره شده و حق حضور در خاک آمریکا رو ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91636" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2OW-6QLT1n0yTney98VATEGGALx2-Vnneb_ZCF2aPSCBDgO7_6orgT7cnoF7hraIAQ3nAF-oS7AAjiOoOeopH6IbhsODcYK-AmKRBS8vGw945DTANWPPpqFxAk7v6Dq6kCxQDIzYi_WgOvICuox_DYeQoYXB6DOZ7478uKU5--RG885o1jDRv8xwSEPQjvYeiRpQb2RuJAIkDxhWoD0F5qBmUZ1JfrnOLobFalgtwNimAMLKT4rJqUyFHR4GebYb21Y3KZt-NJZm1f28vAwJzCqtu5Hj3KEH9UOnM8Ab0Q8mHoXLXjIwSFqUZqTzPZdB43F046HZ8LQ6W9Hcz7NFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه مدل موهای نیمار در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91635" target="_blank">📅 09:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=eENhyrJWLa4FkKKFrEBviZqCcCrCJmCtrpRtgllfzCJAj5S5rqW8n31W_zWQfItAUn_UXVhlgiWuXMpUw1gRQjwmZkre5R-OJH4ie1vuzxnYcVfTyG_2dAEzI-A4yd_jZYtE2h3JA5gbbnvHTaoOAcjrEFH8hZyJ8o3IOR79S-zS-uhfERfnuU_zZbS06C25UlW5moH6qJ2MmtoQin6LvGXg2xIRtxb-v9BNXSOVQFLNDOp6d2lUobENAgVqKyz7_4KGwuEhcWfuKZCtAW2cK4RCU1pjAh3RfesrMobdKFek1NupQU9gAgKp6T9pvdqeSkN_6HSnPsMPkZpSA3ZU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=eENhyrJWLa4FkKKFrEBviZqCcCrCJmCtrpRtgllfzCJAj5S5rqW8n31W_zWQfItAUn_UXVhlgiWuXMpUw1gRQjwmZkre5R-OJH4ie1vuzxnYcVfTyG_2dAEzI-A4yd_jZYtE2h3JA5gbbnvHTaoOAcjrEFH8hZyJ8o3IOR79S-zS-uhfERfnuU_zZbS06C25UlW5moH6qJ2MmtoQin6LvGXg2xIRtxb-v9BNXSOVQFLNDOp6d2lUobENAgVqKyz7_4KGwuEhcWfuKZCtAW2cK4RCU1pjAh3RfesrMobdKFek1NupQU9gAgKp6T9pvdqeSkN_6HSnPsMPkZpSA3ZU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب و عجیب لامین یامال ستاره بارسلونا درباره دلیل بستن باند روی دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91634" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=mSP6pRjSqx6KHLVW5tAkJM_y6zHFchS9zx9WMdV0zc6qroCNKSyCScuMCP2v7jl8tNwVUyCwEK80rYLoud8Dcce9A5ApKUBnCN_M44hZ9MJiWVFaxmt2LaOGLvTrdkXnXmptSY4Vj0Ny1Hjq1FK9a0vrhxDePC0FY6HMMLrPgNM-1nS4aZVJUh_zv_nkXha5OluuZHNvBfaUvAvHzD2Uq4keHSKWGzfa7vZZ8Qfo0jtowRWc495OhIFiPlbGT5p5eOXHQ7r7U3JhFnodOBBAEx66SKadnCiHdZbf5HWiqJ2xuR6yP_Ow_aeHEAmcSppVe1XtK2VefChRM_MRyCg5RpS8Zz244M8Q_uyleSICHMEsglGk5-83_LH6mSpgUoMwYoS4awQHQp2D7f7kktAvjUIYw7gjdiQVKy0qtsj6b63ZwaHUPLhcJik2b03SUe72nTxMTUgiVJObzgKNMTVdLBjsogKOrdyoXt4R6bcEES8xVpdAt6WUEoXFvYwgSAb0l4sXgundU4JfcDwX1pGAqeysa1EkdNwniQbgt_cxdFrVallN5__6y_7iZ88nDBSm2Px69Ix7LSksQHiZfheYV9eXlLnY37BREbfkNrCYvAjQy93xqIIV4fXmMbdnUPxr0TCpsAAuaFF2TFfj_HA2KABr5RVc4ZiU1pkC0ResWRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=mSP6pRjSqx6KHLVW5tAkJM_y6zHFchS9zx9WMdV0zc6qroCNKSyCScuMCP2v7jl8tNwVUyCwEK80rYLoud8Dcce9A5ApKUBnCN_M44hZ9MJiWVFaxmt2LaOGLvTrdkXnXmptSY4Vj0Ny1Hjq1FK9a0vrhxDePC0FY6HMMLrPgNM-1nS4aZVJUh_zv_nkXha5OluuZHNvBfaUvAvHzD2Uq4keHSKWGzfa7vZZ8Qfo0jtowRWc495OhIFiPlbGT5p5eOXHQ7r7U3JhFnodOBBAEx66SKadnCiHdZbf5HWiqJ2xuR6yP_Ow_aeHEAmcSppVe1XtK2VefChRM_MRyCg5RpS8Zz244M8Q_uyleSICHMEsglGk5-83_LH6mSpgUoMwYoS4awQHQp2D7f7kktAvjUIYw7gjdiQVKy0qtsj6b63ZwaHUPLhcJik2b03SUe72nTxMTUgiVJObzgKNMTVdLBjsogKOrdyoXt4R6bcEES8xVpdAt6WUEoXFvYwgSAb0l4sXgundU4JfcDwX1pGAqeysa1EkdNwniQbgt_cxdFrVallN5__6y_7iZ88nDBSm2Px69Ix7LSksQHiZfheYV9eXlLnY37BREbfkNrCYvAjQy93xqIIV4fXmMbdnUPxr0TCpsAAuaFF2TFfj_HA2KABr5RVc4ZiU1pkC0ResWRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
مستند کوتاه و دیدنی تلویزیون اسکاتلند از تیم‌ملی فوتبال ایران در اولین دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91633" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237827913f.mp4?token=faLQwk4eTdvg1jOknneVEId69FSFQGvfVPI4SK0n1BVxGUPyyGcreThajHt0X9TlmCK9V2Fd2WAK9jyAjV_8QQmfqZl4yS4CBtVm5n2lLpXI-X8ia_CE57Avij9Bjd1oBeM3AXxkphJN8ZxOXNNoszhKWdP1GTcZN25gOWDJfU2OxlSvIKmupODPUkuii4b55MjdQS71Pfz4TUDsogV91yH9S4yCFlm_vqZiG6GW4rj95tzRFoW5mZlJ8NVHuVyW_Bmre70kqrmN0OM2K4Ll_PbWjq52N-eGBw1Kv4vYF5vzMychdrLpI9KuIrdl69erACc7RNXllzHLPy7oVNtuybvxyK-7JFtmUX8c1IAV_2JRzECIOpwc8GVK89hJvde-nUi87WrMBZOzjlNKwHCLdHhh6hLbkCb8kqKaSkQrijJKJQ_GSpgeYDfXo2yjrk1ca3HfqViXEIXdq3R2S3qoHF3uKgePnKNynwBtGT0wEaZ-fE7xRPSjFKq2lt5pv-35EzMQBshc2mIExxpLNDVQ4QB3Arm03HAZqx_LEXbRPweUYO34n4wPEqTwH_IYp7SKECKI7X1-4d6-PL5iVg7Eu-wiJC88x7ZdClQHIlMu7D0D2WbfAbzIKCf8qe9EVqlKUyrFcEaGGcJd2-Ox0hMsygPPIs167GWLPHsPpQS_lyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237827913f.mp4?token=faLQwk4eTdvg1jOknneVEId69FSFQGvfVPI4SK0n1BVxGUPyyGcreThajHt0X9TlmCK9V2Fd2WAK9jyAjV_8QQmfqZl4yS4CBtVm5n2lLpXI-X8ia_CE57Avij9Bjd1oBeM3AXxkphJN8ZxOXNNoszhKWdP1GTcZN25gOWDJfU2OxlSvIKmupODPUkuii4b55MjdQS71Pfz4TUDsogV91yH9S4yCFlm_vqZiG6GW4rj95tzRFoW5mZlJ8NVHuVyW_Bmre70kqrmN0OM2K4Ll_PbWjq52N-eGBw1Kv4vYF5vzMychdrLpI9KuIrdl69erACc7RNXllzHLPy7oVNtuybvxyK-7JFtmUX8c1IAV_2JRzECIOpwc8GVK89hJvde-nUi87WrMBZOzjlNKwHCLdHhh6hLbkCb8kqKaSkQrijJKJQ_GSpgeYDfXo2yjrk1ca3HfqViXEIXdq3R2S3qoHF3uKgePnKNynwBtGT0wEaZ-fE7xRPSjFKq2lt5pv-35EzMQBshc2mIExxpLNDVQ4QB3Arm03HAZqx_LEXbRPweUYO34n4wPEqTwH_IYp7SKECKI7X1-4d6-PL5iVg7Eu-wiJC88x7ZdClQHIlMu7D0D2WbfAbzIKCf8qe9EVqlKUyrFcEaGGcJd2-Ox0hMsygPPIs167GWLPHsPpQS_lyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
رفیق خوبه اینجوری پایه باشه. حتی وقتی موهات سفید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91632" target="_blank">📅 09:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Fifa World Cup 2010 (Playing Football Games)-[www.Patoghu.com]</div>
  <div class="tg-doc-extra">[www.Patoghu.com]</div>
</div>
<a href="https://t.me/Futball180TV/91631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏆
بریم به حال و هوای جام جهانی 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91631" target="_blank">📅 05:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGZHgjvLEzsjqWOseNdtApL8PpHjlywiOuLMobG3BVnB3VW0lguQe28xyevD9lSSglcWYUPeU_ejP5CBrMd30ZzAiPQKu-aS_uo_gVV91QgHwkCTPY4NTcjvGVDDxVlR2cMVY-5_uPDCOT-Ir1gLFGQ-gIWSQKq3c6Xdn_VjxHXsGNpt3JrQORFH44mT4oM9iAr7duqJRAN3p8TQYDy07DBkvHNxai3dsHtwn39mKr3pKQ0F1kKlXhftDDuIG_lssf82BvZPZvC5LmNXpDXtGAXA1dSvbcK6LUaSfe2MssQFwRW_GjuMj__Dd9frvQHs0Tlx-oYIf2CcX4DI_HpN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از موندو:
🟡
🔵
الهلال و النصر پیشنهادی به ارزش ۸۰ میلیون یورو برای جذب رافینیا ارائه داده‌اند؛
با حقوقی چهار برابر حقوق فعلی‌اش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/91630" target="_blank">📅 01:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axnusDTOn-2RnTCPSJI8jPrt1yg1X5k-_kDWNEmX3AcyzkwF_CUCDNjFwgKzfWldBRhwOtToKWJamJsyBb6t7wGBKXdlcGdkxO019SG9qO3rSVevQ3jUUZom-gqYvI-rV6WzIYeky4ZgMvHO0GEerMlJKEA7dTQ3g3Lrd8NUI65FWYm8W01QoFEkZoa8pONHF7rhHQQLIWjn1gfcfgm5mrDlBfxAk-k8VO1Tn51PI1Zn88tNmYEaGRPeC1LBoOk0f3KDd-yywxT8PPj-CddG_Jkkul-zf3BWzjWG5yQkM4YeKcs6FG9UcYaKnE00HKfucX8WaTaxnVWpXfJwC4Ojvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
رامون آلوارز: بنظرم بازیکنی که پرز قراره براش 150 میلیون دلار هزینه کنه خولیان آلوارزه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/91629" target="_blank">📅 01:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-owQfa3GqvnfAU_EPZpuHMUaW6zzIphoRPBoGlRZYASH9r04Nt45XycuCnlK2NByNYSFNvP96t6ZTlbIvHJhyYYqFojwRZo0dr_JhU26FDBh26uGgNNUvR6hZ7lBVzf07oDRwwufbSzqgCGwzFSmcVp4ht0Ct9dhy9YrtyqS3DGcJz4Xb0JPiQ37JN92BbArFltIpi1kd-NCv99fZ9X44kBhGxKxAOKzKBP2UEvfR-HeLQKONoF1WiIHAywQ0ybCpuluRyG5UJycJpwk6LLiOyfIHvjMss3MVBNarIKfc8hfzrhvJ5sXffpwf_D_bpy58hK4sCTjG3r_wQilC3hnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در کنار رئیس جمهور پرتغال قبل از سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/91628" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.  او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91627" target="_blank">📅 00:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce3S86d4NHoMhtXY984QG7-uBWQbQA2ACEtaLndL0MG9Q77aboZCcHO6Kf9L97ExtS1UtevmPGnvz0sN1W3HT4MDjf4gAEVC0FqwxPFshXozQPw3OFHGuINWdbEpdGpXDe5koUNfJ6Orwb0dsfGpEGIRNshQdFI9s4z8LsO_pOvrCS_nPmA8Gz-Pkq7zNp8dbgcAnkSgd06Jy-Y6-3lBAgxfCKFe5UFzpTaB238tKkQH-PIJEMsMwL7U86e7GOgIb5pDrKN7XspibJ7qKfq3RWAFs-hBoGpTzmGgqSgoT7EAOgRQ4HKfhRzOanaWuhKVnugRI4VGy8lIUGY4srpOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📣
🏆
ویلتون سامبایو برزیلی داور بازی افتتاحیه جام‌جهانی میان مکزیک و آفریقای جنوبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91626" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElsghVIuqVHEHeZnfYcV4mvMg849JMCX9svP9QTDYmPxckSpxwJQXG94bJcj4vjw88JgCdp8inBqE1DWn47l4iGYIxm0YKRsO-3tQyKuIKmltpIxUhCtK4oC24Loh6_DnK2MV-vKbtauPrxogTV2bHnugeOxXvgtks0zUqFK956P845C5EeEk8qHGuLjYwrKFy696IR60twN1uDm0T6-Nyje0kLq3sLjnhfmj8mbQnZkE26EsMDxvBw0eFhBvvfpaJwFj77R5rbOU9AiDpmpu9L9Uo0c3LMebW46Gjgf6Dx3x_OlwrTYcCq1zC8gqD_XxsAJ6lQjdKECrhBBl-gJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POV: Bitcoin in 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91625" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj_F9GxFarOoGj3PXhz1t6U3nmA_DTAQ8WLJtio2Ptb5LgryRDD7toQI4_l1mWS5vUZJS_nflhsUMiP2yhZPp19xrsNtqhZ-mrh0eLSUOBooL3MzmC_oafI1EXwsMctkgR-hTbrfHAhoCc-a1S97PpPoETjw__qzTOg80TmwHMMFr1gc8QieZa9ey0CrcribAxa3RKuyRugRq0EZzjMPfFX6z5jq0qj_L1o78EDUfaLwtg3bjN7wazJh0UUEKEoF3xIMg09NnMy7lcYROfhwoqPP3IL-itJa3wP5wZGmZ3tV8ssjtxbw_a5MoAL6uh0rmCdACmSVFBEDUunvmwnalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب: 3 گل 3 دریبل موفق  4 شوت تو چارچوب  4 لمس توپ تو محوطه جریمه 5 شوت   نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91624" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YNWxawSfCZzna0AhwbL7MllvMv8TScNc5NcjoSzhujwqn96Z5GpEmLRxxD_b6SO9M_eSQXkujFzmZprWaWYuRQktBwkynWZUB0cvqVniWwvCr404V3VZUw4VsFc40TVk8XTwlbEdz8Wsed2Xwfby3GUt9HMu--XfJXUV8rP-nawVJpc9lipLISr33Vx7qgnvmr3B0synrBTshe4q2zpWQZ2eCeW8ZssvMHX8MWSVfwT3vW7pRZFrIzUIkC97T1cow1ilUBgqnf9rSoW1GuwJTGm2ky166XQCpwhLhP1Fj8deI1kd9gpEBCAGr1FYVkqGBEvYW2N9xkra3yCJEBfBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب:
3 گل
3 دریبل موفق
4 شوت تو چارچوب
4 لمس توپ تو محوطه جریمه
5 شوت
نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91623" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر گل اولیسه و هتریکش تو بازی امشب
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91622" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5ZSjKqu0cD3vR4wZjI70_cBpX4kmVGlU-fIyhHZOmAeONFbPadRz06QLf2UsbiyFS7U89QlC7bo1YoeyaEljgUOtT73Buk3OFxpA52rOsOb4VliSt8WyBlnF4YteMI7TuKy0Qe6ucG7i0juCltBySK_XDX_JOXXQXgi8pWuBLrtVBwWgi5Yryf-Oh2IVQDjKabe5kXzr-QRYHjRtA091bohnIch-Je388U9s88M5vK4SDtq2x-YaxLN0kHvuKZmhplEB5Lx0XpVDQEpnuYjyKN6UdlsoLmo1PAW-nG_wp8WQVXOitV8rHLkLbqXg7jCAswfmfxgJEGDdtKU5xtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه توی ۱۷ بازی اولش برای تیم ملی فرانسه ۶ گل زده و اولین بازیکنیه که بعد از داوید ترزگه این آمار رو ثبت کرده. ترزگه آخرین بار تو سال ۲۰۰۰ تونسته بود تو ۱۷ بازی اول ملیش ۶ گل بزنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91621" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91620" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سرگیِف بازیکن پرسپولیس به تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91619" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91618" target="_blank">📅 00:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck9E0ynpUWXSRXvCM7Z3H-lIw-gDRhF9xFaaqXNl9XchEO9WwOdPVPZQhfluIQTI8qMPzvUt7pvsRvCB3B_5yKfgpIjsILq9oRw13nsqlQdbKiKXYWUyA72NTh3RAvFQdSGmxItt2j4PtsVABDJkuHYUqSO9x2rJWtDF4S0yktJrVV--o6Vkq9c5G6ZMcoYhp-AsgFHYNwMroYmQvTJJ0ZKrwNCua4MI7Nn9hDCz0tPjwCDerqVlK2OdZEoPGN6U9zUHMxrmloCGpHWEKy5SFJkL3KTRLtfra8J5WzF4R1-j9XXBmsQHR3gfKe4s0TJsEfR0n69SNOnN3PRNjEc28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.
او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91617" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzfwOOpleA0hJzAX7_rE3TWYIeuNkMNDXmIdZVVkuN0OLulIoy0eM-8yMQPCFU5-Pjw6mQ7Y_Y95JfPM8fjt4zst-GsYYYFGhRM2peqHfQKinDLZd4KECe-dLhg6xIX2skaV2rWA6Xwb5HKZvjotHErI6pnwawt7HRx8NTeuq8W_CGs8BTKWnqL0d0ZrJwcyq4cHrff5ndGRX2xhD3ecsG0UvLnotNmPss00HUoVQ-ULwouIzpajrBMEm-sBFZTRNH6wo0v5GpP13dpxNGWl8scS1vePP1bKk8Eb9UhrFmlZN-2HNmMwM_hI4WWfepjLWsA0eHuqYZtVw3_lMq4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91616" target="_blank">📅 00:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REJ-XEr7NPp09pFxyreKqe3xIBYy9wnXxA8p_MBk1psqfD2dXs7cvPnOdUUj9LatXon4BT8WCndnWHWsO6zEcj8qFcU9e9Lec6c-i4PhGI_y0pv95lJiStm2u7Fx7yJ0RA4nCq_PHl-DbsRiDc0Nx-Y3plUNl2KlHus0XqrRCWC5o3qloDCtFp59f_PMplGdXgUmcz6MB2B7LAAMj_ikJAI6d8wYpFVV-_SuhjTTKbXaYq8EBub6JwfddxKK4fYUiox6qW7j3GoLMknEt2eDAuqr5lSA2vqYy519eDIeu8s8jiVrSr7MvPi6XCGhYcmJXR_2GqCNadNSOU425cBpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ گستون آیدول خبرنگار مطرح آرژانتینی: منچستریونایتد درحال آماده سازی اولین پیشنهاد برای جذب رومرو ستاره خط دفاعی آرژانتین و تاتنهامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91615" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی زد اولیسه
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91614" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔥
چالش جذاب و ترسناک‌نیمار در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91613" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4-Zz99jOCwq6m4SHY1uHigB08pwOUcPtZlbYU-F8L10bOmz9Z_lUrXMdfzttHH6H-wd0Xnv6gi6lFTD0SAZXnSBQpv1FWupHiilDHYT3Y-4LIXMBJkRcvXxhn_8mirwek0Pv4ar2USdpPS7dp_8WJxBIPcSRs8IGJ0M8qaCueW-u1reGn8HPysxoVzHdVQ4S-PmBlrPU2oOY2rHGSNGj--v0x1VQqnGOUzZvYWFUsWNsCI9hOvIZsrFJNVeNFohg7DXDdQVPLZZoqg7vlxvrHN184JG_wjpUw5Iaq5B7bO3CehyEyp1XfDHkPzFgrpT58mEEyAylk1Pud_qW2pavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91612" target="_blank">📅 23:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUWcSme6V_lQrYaAuLx11P01XAO1XWyWhM3k6MMOxlwBtax0mJfGF9-Jd982wRiCl8PKcSIplXUubgvFjD9p51i5rwJ-ak4DkBojmzChF8vIvTprGqpZnan90uHL2V7IRr90CPq1tWXfQrhlE_T4ZFguJNJltTGlfqw0Cn-0riZSLpf2oc3vuCMXYf245ErsK18X_lAa-9lqBs7wUerp5UxIUl3VSCAT4wJqrhBN9ZqNFUCbMcmzeYq7ZqCYq3bCMBJjfQ6Ws55uP957SC_3LHLSZNMnGpaxnIbRotEfD3UqCStkQKlvLpiBlSspmP9pc1USXS8mUSEIZInrKqzQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91611" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-u6drWgG___NA6L4vXR93Lfy64EdagUnH1wRR5figihyyepMSBvXQMNIIFefV97T7zOEwpqtvde_aHxNfj3Mb-T6xk351QaeWymLPFiNRsWFLpTKBwTDa5pA1A49JBP362BlZmjQlBxcCbPtIjxRX-5mhl6wygz0bwD-OiKzBPE3OIjl3Onm5NRZZfjN2Bt1CD6nPZA9aQ8_dd8s1apNHT7nxXQmKyZRNCN2BKewhnbzFjXmDtdj1e-FnM8io9JPLZZWBw_C8Ao9lPbqQz2t6VCiFKXszz4ZyRlQVXuxJljN4JszW5B5t_uJFwn_6MpWTPH3ss2KRdZqtx6ao-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اولین خاطره‌ای که از جام جهانی داری ؟
🎙
یامال : بازی آلمان و برزیل و فینال 2014
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91610" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT-dgQwUjmOTyBLP8ZwFgWfK4InpZrxzlKnoF5C8r31SilmiX7K6dpP87V4IykmItrhiyf7UGElKOX2HlK9IUc9bEexQqMrWsAbLBRgpUkFBD_hHL8sobchKd_FCc8LgRukgLB_o1JJxzYQE557FimB6GakFbeHcyhx9GWMcIEAVC-AD_gSGwC9yW6iXfnVuXJNIlJq-j3GpS11zmU6S49RozIwKsu1hkUSQT7sIfoQPDahiD6xmiklE9xJ1u7CfjuNx4NJyHylQaFl6QJkHqxW32IPwpjGzn0ALdR2GP0sHnvUlr70piG8lkF4niV7ZR6ZIgav3_-e8bvAgD8Wt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کیلیان امباپه دهمین بازیکن با بیشترین بازی برای تیم ملی فرانسه با ۹۸ بازی ملی شد و از لوران بلان، وینسنتی لیزارازو و کریم بنزما پیشی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91609" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم اینترنتا وصل شد گیر این فن پیجا افتادیم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91608" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این طرف تو جام جهانیم ول کن گورتزکا نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91607" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار ریدمانی امشب امباپه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91606" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUoUt_SJj8C3eOn08m7cHXCjki7V3DCbvs-FPe3lw3p_IUd21L2S_PqIc85zAamD26na7meJI4n5udXTZVBLpJxcSw0NUlAFtF_umKf5LJRKZLxmQV6uC2Nvj-DegNU5g_oIGakInYzNWiCwi7b3tm76kvGwVplKvVB6pgKafFg-TczhmlJJ0qF8uNVSbrGK_7OO84kvwcA-y1sL5gC8YepFdOFMEbQQPWyihGpastIl_l7gdYX3VNdKkcHQR4tjY4U-xO0dpU7TYfrjH-HTFF9hH9v4PwncIrS8FiM-3Sso30d7TEaFG1ciJOgP5-yjG67nlcVrrpkGdj9jpdMFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فورییییی
؛ در نزدیکی کمپ تمرینی تیم ملی سوئیس در سن دیگو آتش‌سوزی رخ داده
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91605" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زلزله 7/8 ریشتری‌ فیلیپین اینجوری باعث شد این 3 ساختمان متصل به هم از هم جدا شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91604" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=PrY1705QeT6xc7ABfIBrsRKpFbU1LJJEliu1qNbeFb2ZjZmaxrLFLCennajiOBRSP-69ed3gNS6T9wH1huf9i9xz8S47YS-yxBum-FsWmhaglMjGEO9rKvhY-91ecof26roNDLuCdcrYS39cxG-TdbRw3u-1iw_lIeXugzI7Zj6PMIbXn4nhOvqDuPEEYdrmoXq2E87u5wIqvT2BX82UNCJZ82I08ufJY8vhA9agJQ_Qb-75sPy2hWzQ87UrTzA4JyTRYPuDAxh8fcZONxXGxQ2qdWFdVFeIj_gAceKX8BmTmYunzH6nZYEq87HgZN8sXv_yelUCOuuQKz4eF-PFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=PrY1705QeT6xc7ABfIBrsRKpFbU1LJJEliu1qNbeFb2ZjZmaxrLFLCennajiOBRSP-69ed3gNS6T9wH1huf9i9xz8S47YS-yxBum-FsWmhaglMjGEO9rKvhY-91ecof26roNDLuCdcrYS39cxG-TdbRw3u-1iw_lIeXugzI7Zj6PMIbXn4nhOvqDuPEEYdrmoXq2E87u5wIqvT2BX82UNCJZ82I08ufJY8vhA9agJQ_Qb-75sPy2hWzQ87UrTzA4JyTRYPuDAxh8fcZONxXGxQ2qdWFdVFeIj_gAceKX8BmTmYunzH6nZYEq87HgZN8sXv_yelUCOuuQKz4eF-PFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ایکر کاسیاس در مصاحبه با روماریو: «مسی خواب و خوراک رو ازم گرفته بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91603" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf-0_kS-zuW-bRttzzi1Cu2Cbjr06IVpOeGB3GCng1tgbAxSg4JVoFuvG2IG0xvLxY3asmUOkKS7qqi39VvkGTFYFhI8-L_yjUtB97-dJtbMO34HyNBZ0oCvK7cPprzs8ikAbFHMZ6l8FYXrBADFu-aF5KlbzTaojhG0pQ07R1GrFgCS5zl3faV6bOTR4z_qtUl49VXTbrNEBynR2WKZTx7e1q8eRvAcEw8mJYS_z78vvmEWJf7xngh_-9GWafxaL-DlaGmHCZvDViNprCB2hB7DE9qRRUBBupVZbEIvZxtAwguWgV_Gz3r3RooWcg_ptlo9v8HFsF1B4t-2MNRSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو گیمارش:
«برزیل هر تورنمنتی بره مدعی قهرمانیه. پنج‌تا قهرمانی جام جهانی داریم و این اتفاقی نیست. فقط باید تمرکزمون رو روی هر بازی بذاریم؛ اگه همه‌چی خوب پیش بره، دوباره قهرمان جهان میشیم.»
🇧🇷
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91602" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXq15R6Jo_kCu5mlymoTzQDJYy0uYNqBMoCdz_3FUlRRZwPIGj2BL5JFq2mz2XgdCeZaNslTPqets_sLLt1U5zE-7EVuZhMkf8Stc71KJPvyvnbHCVoCfcPfr3fnsPcrX3JTtwlVTCtS6lgm4h9CIw3xYO8-zhoii6cGEW4tklSZ8IMeWbLxDzXVnDmLdJxa14Mhch3Bo4yq1bPqQNWZlmgAqfV3WKc2HU-5YuvzykLmPmhjBeaP0p150-5onQJ6CNksALe4FkoTbypz5h0_6vZ25hoQZmwb-RM4Ok-GfBdfUv6AFy35Tc08BgKJvNPePNhO5hvJxkr6gsooFu0qHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDhdnTG4K8xUXaEpeT7D6KCFMXYAOtQWkyo1Rj3cBbUWWUkztBKgWnLQ0G-P3ua43zRaii_GngtSXW1ilN-jPf0eDJBcneyLix_bD47XlySRDwCim7EXviF9tIW0GfsIjIe7OuG6WMAbjU30wwgh5IM5hiIMiqGDjpSEPe-_BJYJ-Gpe8npf-mCUjsWS2pSijXqvyOkLOqzD1SZvnwiuZzw0GN10lJXDd3VJldOCFf8uKb9n0q5lvhNjI77fpG4k08L5IFRTwJnBQNywLcUuQprWk9MSR7JSvJGj4NhRx63kXJ-mbfFG6gQO00HO-dGC1UEgbC5LMDJM8Wui_ZFwtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91600" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYO8_vrVA5qOnImAiDC_F6Jv0Ia285JxDhyUxsSk3YX3fwX8vQANUWXay61F4oVvosiKpCUO3OXfAgFDuXUUaIEA5TJPzvljsYSdHOr6rStrWM_HuUY4KHlFBJ0T5zty_91TeuyNXnNHq0zU2cLKO2NimwaDm2Hyb4DRNr0EaONiyzXo_JQt1l8RP1SFeOQruylcfBt8uwe11x-NEMPOxZHesYbB9WVPYAE4Kq6B0eALgtZ-rcvfFqEt_gylO8J-qdxNkg7Hb3KqGoVexVkSLudPx56QnA9kIzDWhpg4pVg9kO4-puJjnWFxibScjpQWSrjn1TxJjZmzQay3sYK7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91599" target="_blank">📅 22:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q61Ovr9EXDIlncjpghHPTI5QN563ApXdoetAeIIVCZ4Qp04RrtGI1CnHSFrhPPIyTi3qRGH4VhWHWrq6yBHSJT3AyGZ0cGin5vRcnZDHatPDqDNAr745GOIH-3AfefgAw6cSdW4hB1faIX25KBB-yRJ6bp1ZFJrHsADyZaBWie_CxifjSbqcTsYpd-Q3D4gDCiBKJfRw5gASGK7IVVpu4_pvrpFpYKVwz2XfQbjhn5bl5mYM3yQsCf2rE4L8C0PtTvs6Xz1ZFJYG82tEZZ_8VAT33IJzzmJBn4STFIY7ZWeU7mVdfMMW_FPuOM6ktys6msZ9-EsnVZuE9IztlVoPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل: نیمار روز دوشنبه MRI انجام داده و آزمایش‌ها نشان داد که درمان او به خوبی پیش رفته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91598" target="_blank">📅 22:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkXjQHc67SSBEygb77z9tN-2gAkHxawtDmHnLH90DPMQWlJkafFScfTdi6goWOisy5jkaTOZQftjsMgi_H9GrEA70CX7bQP1A3lmHfvFiZGmCO999cu-BnG0ddDfJ4GJzeEpe09fDImudeD0lbvQ32HtY1yR0009PPb_lGT-rlqOCq22lC75ljLNwtuNTOtNMeALSakdV3MHXGlCFPbJJyGv_A2s1kxEGLhrxSHXXLUpKGHsenI2zU6E4EgXsG_3X4Pga5kJeBPmhmoI3UPwJZTaylqiJq72DNKkcDonB1WEaq-SmBgXmG51Ay9hbLunkzkveqHbGOrvZp26QMohoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رومانو: برناردو سیلوا تصمیم گرفته مقصدشو بعد جام جهانی مشخص کنه
❗️
بارسلونا و اتلتیکو مدت هاست که با ژرژ مندس، مدیر برنامه‌های برناردو سیلوا در ارتباطن ولی خوب هنوز با هیچ تیمی به توافق نرسیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91597" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVPwXO6f_bx7EVKFL45ZlOdIYyOQxbNj4TakspW-ej8S4BJCXfM60OHUNb0qiYGYScNbRF9YKs_mOhMYpKIIjFXtbPFeNVH9laQaN9blHQlrDdWw28g7q7vNrx7__ih4n7_HsLYgvnsmEndf1FWhLwwB2L3TpENsGMuVkChyi41ZCyHSfkXBibejrby2cqhEat3KV2XZ3528ocwm73CbNRDEptpLDfXUQW3z5B-M1dN0RzIqKrnArDfITcImtJLOxdaSWkJ_veSxLJ9G4x9DStfvGbfdjfZH3Ny--4-9W6ILdSmN4jwR6UPSLJ0px1TW5A_eqkkMvKmp8EpLjRnEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ مسی زیر نظر اسکالونی داخل تیم ملی آرژانتین در 7 سال اخیر جام های بیشتری نسبت به تعداد شکست‌هایش داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91596" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یورگن کلینزمن: در فینال جام یوفای سال ۱۹۸۹ اشتوتگارت در برابر ناپولی، با دیدن گرم کردن معروف مارادونا قبل از بازی، شکست خوردیم. همواره او را به چشم هنرمندی میدیدم که با ذهن خود درگیر بود. این ویژگی در داخل زمین برای او یک مزیت بود اما در خارج از زمین او را گرفتار مواد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91595" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqgoU6GylIxWN587D5RqvgY2YwjSFYj1UhwdDG-lfyQr0W0DuNwlKop-YsZFWrvdqyviSEz-Sjjtiy8abx6N93Q7t3GufhmXtIoglvCab5ZYhrplfnHHAXkEvu5JPVJcHNwg6X1PQbc_VnGfhyPViP-AFix6yKf4_r6gCmxjqpzwouPDNq1C5K23nG06neElG8w0XIUQYOjwYl-1ONTBxZDCbpCv6tiSaHXn7RaSiQX1c2cdqF-9zl8PEv6R-UdCm9U-0h-qCOR8kgAkerigycdbgIBiz2YfKgzAXqV2dCBMHs_U3P5xVtNpPdjYHoaeJS47eWOFeqZIUrZ5O4_1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91594" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxN4rUHtrkna6dO64o5FP4tBqsmt6ZhJEDZX_iIMq2W5EDPhmj4qyOfZGOvOwbDIQMJdxL36sbjXzCUBIXjXvmnXeP5Ajf-VRH6Nwaky4rEnoawpCLit598lKvxQfcVt2eyD5mwPaOqt9E7HWMHYdSqSnNQnbfrAVBVeHVr3aGNqb6d6cz_PIxia0WVmiA6SBgHM1wFyrdbStdJ6hT6Wq5dxu8AF_wTHU8lY6aofGN_5uBA0ZiJLDMkIXVtOHf4rEsKeWfWlTl68L3s8znHJYeDqjjO3-uyZktD9Yk2QIe2C2NHXrPXownmCQickzq4E-EDBdbkW-kUvGICFLrLF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شیا رائل ویتست، بازیکن آمریکایی تیم بسکتبال بانوان استقلال، با یه فرد ایرانی ازدواج کرد!!
چرا اونا میان اینور ازدواج میکنن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91593" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxJwFLu6PWpLDDQ1lciEOLFapHQLOf63FDLVF7uLk-dyo1JkzF_AJRYPc7z7oQZ6cXajmts_HOlgY4N9Quf1SihFUlYJ0PCnTWrovFU7SN_9M8mT1YzAcfI-fSY772xxsnSU05Y_AAolO-jnBQe0op8bylxkwhgOWQnuhvvNxDXTtJKcFIjS-miyUScU2Zk7Gtxl_bzYdblw8RL231ArOtkwJsZfR6de6rLV9tuHE6KWK8F-MZ3-Ziw-aqjKn0sI_gRKIMvIaeIx4Gc-5PMXF8Hxynjc4lXiqdpgXUZ1pr2MvIJ69W187t3DWWA3vSim07CK4dm55R265etW9wLu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی: به مردان میگم دوستانتان و همسرانتان ممکن است به شما خیانت کنند، اما عشق مادر بالاتر از همه چیز است
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91592" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91591">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDGezP5QtZm1I06lZaRQi-uiECHH9b8SV27LGRP83HrEEAZIOb2CZ1bLFzb0yuUjPJrBBEUGv5EWGBbcjV6lJgxP1RAhHr4FHSLo9bR5e6t7pb6I8b94pEmjK-vHtEQlRg4VIC3HAd-3APd9NwZ7BNqUPJcDUzMKBizAI44pfdsP0cLX5Gr_8p7E7oiNdhpODvccXrb-nHh4Ww9F8Ra1fv8s7Fy7YbKGfUZUN_0ll6beDvLuAVwqOLrmuZYGg6e4C1JbhrUP9N7hQ8eBYhH3bppjvPgRlvskXXQS2pGeIBnbQ_6H8z6U08lG-y76A8QIQYIaAJVBrE_SPb8oioo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تیم ملی ایران در جام جهانی 1978، آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91591" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91590">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYkkkNMLUY7gKthsMotb_uvntu-Wx35kZpgSbS9j5wzCw7frKWBQRF_XTVpHBTWnpURWnUXkIKuDwa-TtxBvQXWdpJCKtXz2Sla8XCqkAZEFjoF6_H79yXl6IuQQQecMdB8Jt_EN_p2symHyIzbUc3wQAt5HNQcDDGEUR9T1Tr_SpyMNrhkzlVg_z-HBsRbC4aR3kIztB_x0w87pqp862ueyqpmNeiYIlYAl1YJ0FjK69QH2DZMCzv0Ui6igz-i66etfnQJX2TeayHUWNipCpFtEvIbLRocmUXIKWku3Rr7OurerMvuY3_3htJhDUQles8WTqqLi8KKWeOUKCiaZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان ⁧ جام جهانی⁩ ۲۰۲۶ کیه؟
‏اگر جواب رو می‌دونید، وقتشه که در لیگ پیش‌بینی جام جهانی «همراه من» ثبتش کنید!
‏پیش‌بینی‌ها از امروز، ۱۹ خرداد شروع می‌شه. رقابتی که فقط به شانس نیست، به تحلیل و شناخت فوتبال هم بستگی داره
‏اولین پیش‌بینی شما چیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91590" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWXXrtY0Ts1Y6OWU3cWB0wLf7VBT718b-1YI4ifu7XzoVlLzxS5gPHv-5GwaYq_9K1esuA8uk0s6shofGmZS6e8buL8lSCB3DSfjRpL93CKb_K1gI3AgNL0HmxEc06GHpykOKqAFVTiZowl9gnfez3NAsDBXVoHnekESlmJCX8qkRB595QymGJ-TKyeWe_50mRWogwxHkKsOw9FUtWzMMqNoVCcZ9aVKrhPfMEb41WoRtvz0ebE1OgKBj07D-G-QYLZWKcLzElP0ZwxmvgyCfjF_g3iz8zO6o4tz2UYLvOpQinEKSjDNE1wXSmC3VfPVQZsuWacScfLyRZS6yDs6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
اسکای آلمان:
بایرن مونیخ در صورت داشتن پیشنهاد 200 میلیون یورویی با فروش مایکل اولیسه موافقت خواهد کرد
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91589" target="_blank">📅 21:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkey2wqEqyMRNGwDlrQOef8gX8TWJlMk9uwFE56C0V-JmMsWYnlXfCayYyIW4sypMK9YlmCJCBFiYvi56a6nqxdAuYgaSO0U9RkNVGn0IO_7tcKUmj7_4jY8H5GGgrpYb0xoCC-OygScfJCPp6LAzx5AAEd8J8eEHcL1pmxkcFg_sudMgnOU8Qe1kQHyk0Fu0rFvaf53U4WFeDQnW2QVbLBKCkYb7SWJM3xyS_MZKrFz1pON5xtFeeS0BqMCRPFqtFh1uc0dyZDkXGLnIp98-JqOHZj4o_JvQ8aAr9F3cUrmjhvkipLB-4f-hR1AcQk8yTDklFdhQCsntdyvmvGyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
تیمبر به دلیل مصدومیت از لیست تیم ملی هلند برای حضور در جام جهانی خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91588" target="_blank">📅 21:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🏅
تاجرنیا و جویباری بزودی برای کسری طاهری و محمد جواد حسین نژاد اقدام میکنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91587" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91586">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_ln4a1yYfDs3NzpXfOr6-RPBg4VDc3c60E5TL-N6xs1Y0jcwitgXXTImWyQF5tlWCbHSNNCqPDnqbcYNTYxUbjuOFbNB4sAnGop2Lr16dnX_4hxIJgWYFtfbGWshh1DZ67v1w-4ZOm7oobCQO5-RIJVm3pjVo5ZauoY1zUCd5S8jo7CW1MsSCpKCd19yC_fHEhmy8zFkUMrfwCPRe2qizBws8G7Lox4UB3KCTdW8CF9rWnxf2cz9_DKePspg1pzeQFPlX_BzDP_Ax9PmUVBKibVBtSSkbNjCRNGLpei-VBeu0v-4wz_uH6kT81d427gSu-Y5URzdl-bV91AD6nXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب ازبکستان مقابل هلند با حضور فیکس آشورماتوف و اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91586" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2mM-Y22TbCMpG_sWrKYdoE_8nB9dRAWSthMPg6u-PRtjoQWfedUzgSOVx2VK3uq0uthCIph2XAR479O60g0oa1tv9Q7vGvvGpW8YsRuvLgH-Lc-j9e3o8QjMmBX-EXF8j7lag0anpB4_6GuWKlHVPgYap7csRwop_M7NXw9oUyG1gf6emOYSGPtuP7c_1pn-RlutcB_XU_Slr5tC7-XGIrJhdFqpEPxmbc4E3xVcuEomosFS6c-7OVxWn0YjUHvI04eugUa9asVgsug5RBuVIOfkdUatNpAnqwwp_CVUgx7niVMB7TmJIeBK_imb62CucfGihLwe4EDSndA-ShIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91585" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlnJrrhLIgfDAE3vxRxn_iPBa2SY0QC0KpQmV7llyLo92AHEIPQ58QcBlBocNraCfWu_BdYeviBDNG590LTpOmfaHh05R8se1glRT8sdDZWUlRePMW1f6Z_wRohIA1RwPKVjFMrHoE-nre4HRfYehU2vrXxS7HUQ8vscqnINQsFEE_JqpovDW63eplHYR12C6UOTxVQdY-eCxq53sgqhyf2YOcFuBir7-0yMP1RHLKHrCEC-02HCDVHacuAqgrP8MDB5L4gJ_bKVrBbTmw1IAj0Zg-9e708wouT-5K8e68GtKFFQiVCdEnTYO3sscYZ-Hqj58nIw6VEM-iCkEq6yJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنایی که بیشترین دقایق بازی رو در جام جهانی داشتن؛
لیونل مسی قلب‌ها در صدر
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91584" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jos7uu4iLiL1ZCVPpb0w5OhzM23JG8NvrYMhOIlRU5UB6Zdua7V67Y-KZD9Gtfs_PnQs1zopE7EAayL9qANBmpDIwPbOU3ZGvVmAAVWT9j7sb6VedzU9pAIcRT_SqIX-1uAMVybdlNhX9XUf0ErgYTR-kUqt0NURDuILlMl7cVZA9vAcocgsnXKJbmP9bIWTzSGtM27GCasWRzns_lMwnDPqZT7p8EEU_XNy6LPspipjTLWe539LDSY52g8NuJk3xZriHSvAorJb9sdxIjXw4ENOU9z0dh_IQ9NCfOl0rLv3Pu7B2ogDAlhFqOVFX6ko5RSkUHkoqdImdFvN9TaarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر سپهر حیدری هم پرقدرت فعالیتشو شروع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91583" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdfWRQdrlofPTGrjxNy55POFcNEi1hQ-O3hRhqpkBuCKkkOp-KqxRwUlvAuH2OEAnD093CVrNA4j9FLIVBDsu_1xOZxWzkHPsSINLLqxumhPkcsaICZtgz6OkNk6HDhPV0HwQp4mMLm7qu0uBbdcGyrYsPOtQWjXQ7eWaw-mzpk6cd035l1sFp1DqllUa-MZzP1VctBi9oRikezV77wX6Tm8Y0Uz_gP08dP0bVDDLkLYmtcqioZFC-MvWQ0Nt63J8HvTHv4zJPatqaUNsV8JF2DPeLjyHX0I-mSZ-SN3RU7irNb2yN4sM35OtwhWZoMA_XinQgL0T9oAZhizlQmzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9iOJkTzZGgyZlF_qKMCVeiDsTdv7jNP7lm6I8uCEBizKq3Q4QvbiaRrtuoYYfLfkqTV6laTNTjWDoF9gZgBRwdf8DVIMtI8yYoMA0cgd1P4WCOYsbHLPJ3ktVvYGl8VUecM6-yxoxX3aamsm0c_ySM-3YFI-W3sVt3Wasfds7SuSMmIuubjQ0GMNKM-XpjykxvKZHtVW6Rz3rfT0rpuObbu19f8J1hV08YV0z3D_LYn7AipZQiPYcE0YpFOh7CkFHQaD9kLVNAzVhPLyzi41IoQymLrabty2GrD00eHdd_0pUE54jrgO55LxUBQLyHEGKE0OcPJcTKXfEwCAePDuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه. واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91581" target="_blank">📅 19:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cXw1wcMSbF0zswJ44ctDh_Mx5dfciKQ9GyNsYCR3aKYU0FiSMphf0jXMJnAUAvO-V1_An1rzUWosBvpqVAWyvaNmYcJWOKHxSRok7xUixfAd4lC0RIJkJKX1fsA2wCLP9KJ87j31ABc6RLZ7oIjYigYlNRR5HiRDCc70GCi-qISSZzn1UxbEPYU6ObEMIHGp2Pt4aBc4h6l6-Dq3akuG_DCrPywRSDj0P9IvSfwT5x1RDAgZULb6N6qscca0riffjK2TZgtP2scjZZST0g7i6cCtGzW4b6nut_Dh5aMj98lALQtonRew1tNzEg2X5K0t4bBlNPrwM0JrLeaLvxdX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cXw1wcMSbF0zswJ44ctDh_Mx5dfciKQ9GyNsYCR3aKYU0FiSMphf0jXMJnAUAvO-V1_An1rzUWosBvpqVAWyvaNmYcJWOKHxSRok7xUixfAd4lC0RIJkJKX1fsA2wCLP9KJ87j31ABc6RLZ7oIjYigYlNRR5HiRDCc70GCi-qISSZzn1UxbEPYU6ObEMIHGp2Pt4aBc4h6l6-Dq3akuG_DCrPywRSDj0P9IvSfwT5x1RDAgZULb6N6qscca0riffjK2TZgtP2scjZZST0g7i6cCtGzW4b6nut_Dh5aMj98lALQtonRew1tNzEg2X5K0t4bBlNPrwM0JrLeaLvxdX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد مقامات آمریکایی با بازیکنان تیم ملی سنگال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91580" target="_blank">📅 19:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odm_lFGkwkjYIFmnsvfnM6UmjBU1Qt8lRMTTQSLA6L5XHSqAyvhJFq70QapzfX7lQ59upvzY7moVWGJRriwnfFaUBZGjPhypiH7uP0sj5VTrV781p9H8Xv6ZdaOr6oOr6WjLL5aa1WOnFA-Y-k8XLOPsSAujmfRdrnxanNBHn_1gtK2VgLWTfdP6NRKK3ZzszZqyvFNdsoLVJ6vlGeURjJATJk8LIuVxVSv9bsfiUf70sq4tcdz3nSSN1CwqeOIbGl2_tJcIKLgrx05hnui29gYRTut6BowGyGIbYeSqE-RIS3cxLQNsXmtVqT5puCXU6UwEfCKQ5I0okGa8R8vwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
کادنا سر:
رئال مادرید پرقدرت وارد رقابت برای جذب برناردو سیلوا شد. مورینیو این بازیکن رو میخواد و اکنون این احتمال واقعی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91579" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpWk1ljyd9PlDeBoCm7eVu6iB14_eZJBbaATyG3oDrLO1qPWXmMCGCZsP0Z93W495saqKiB-oRVBBuODDhG1jw0YoOv9JfOrsiE1LEyFdTHJSIZYRmn6jVz4WyYbBkKKASDw0_w6x9-hxBmPa_fLXTYqGkOgfh77SkUuk47AlLQHF6R68VFXs_aoYp5by2g9aVo6w4bzl7KNEVnHt-fnwX2ya8YnQ4vGbBU2CWvWqQL4Ubf_dM9GfYjFZKPINxfPRF1g8_AwIQtLjzg3phMiUeIp5hQ1Y2DFWLWpJIdsgfIixnN4GUQRY5fCmqs-i-KltAaRxvyElsULImiU4ieSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJf1VKvLw9lN04SX5i6RN6UbE-yWeKTG2wWJdo5HGugadpdMKqMab_Uu68CjeBU2in0wU7nQhykdSpFduLh_KIhL_D3vuxM2tSronBoyQ4ImsEk9BOEVqtWtJwJ_2uSbIwK2aa-FGe8zxi_9KC4Os8WdYqh17giyGZtoIp7-OHczT5njAqZg7gKLBkFrpOA8st1pNKcv2dgJbNxpOso-h2Vk05GONB3Pz9U2NWex594jTVlGzc_8C_xC5pd_YCVDYzfJt4RrvYd21Ga76bmusvm-VoapR8MmI6_UG1sODd_FAt7eQRp-xjElGyViJuZKFAyCH7cKltnes-BWFpN9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twT5i5pPNljtWtFNVc_m9H8kz40KNf0qyZQ7Nrl5IwSWLus9xWG93TMZHKx_Lthoq8InX48AoNmB6nATpTn85NP5QCMW8uM39PANjPHcqYQaSeVJdu9oP7n2vS0PbduyWa6aAcOVmZ5bkGZ4-CvQBeQ8CSVI8B6XP3U7Toh-CdxxR6LVF9zm57AebIuHfWVGP6KtYPwfH3oPtQ56xkWV-Sqc-1T8V4V5xApzyRWnKH9JByDOmtQ3xANtuxpspSFqSPw0j24fPbyoO4JkgF0LN0PXgkJpheu-SEcK_t5t3HXQV3KvK3x5MA6qs_U7WBOGOeEagyFeGbct7-j0EuQm9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله دلیتای عزیز هم که معرف حضورتون هست تو جام جهانی مجری خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91576" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=Yyj3sAROEfn7XlJHSz7HWVvpBC7Wb0LNCXmk2pmL25gNV3JLJOt9_3TgS84XNYTAaEOxRvDIr8mm8RTdGT46G0tQnx43O20BWpvR-ZUISo6QyyqeZAZlDWkA8xvkksY3UqSvrducKLWqbHKOu5Fd1BxnPgCiLtZ_7rNrq6gfI-3rwNg86lFRVlloPbdpjAkNz57b_ijNAihcsDycA1jig7ULxpuBpdDDNjnShNK4yL2_vWeLz8m7rngfDT67SeOciR2K3S_i_iX1yeUcbZYgU6VWLhCE2bN0Xmzr9gQaCQrONVN8qbjVC52j81sV6W60S7KoWPZqZsNqMeXZGZ0BuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=Yyj3sAROEfn7XlJHSz7HWVvpBC7Wb0LNCXmk2pmL25gNV3JLJOt9_3TgS84XNYTAaEOxRvDIr8mm8RTdGT46G0tQnx43O20BWpvR-ZUISo6QyyqeZAZlDWkA8xvkksY3UqSvrducKLWqbHKOu5Fd1BxnPgCiLtZ_7rNrq6gfI-3rwNg86lFRVlloPbdpjAkNz57b_ijNAihcsDycA1jig7ULxpuBpdDDNjnShNK4yL2_vWeLz8m7rngfDT67SeOciR2K3S_i_iX1yeUcbZYgU6VWLhCE2bN0Xmzr9gQaCQrONVN8qbjVC52j81sV6W60S7KoWPZqZsNqMeXZGZ0BuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمار؛
بزرگترین «چی میشد اگه..» در دنیای فوتبال..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91575" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=JD6BHoI-L9fa7zgkCSPfP9Y0DH761Ls-pe2R3QiNE2aUAuAQAg9R0VJ4p4li6jWKZ1OXPE2H2GXgRF4kacLRA9aTyQgXM9alXb1d66XttaFUSJm4O6WIy4fEXkoRgePwtsufpBlmncVNtDWBanEx-2pY8OoVVfGKoWjsKLP7DHlL8C20KrRhmTUI0VwMXHxKgHTVsw_EOlmigdpzBE0qGyjHup4Jt1R1tI8isxSmKN4Q9yGrhf1dU7lEULjUZ6NfMoFwgfpjeNfWbCL8EvsgGQGkxgGrk97xyvaqkSU88UVc88Dy7et874Z0NRMI3GD3h3cQyhUAJUiacuxcvvbRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=JD6BHoI-L9fa7zgkCSPfP9Y0DH761Ls-pe2R3QiNE2aUAuAQAg9R0VJ4p4li6jWKZ1OXPE2H2GXgRF4kacLRA9aTyQgXM9alXb1d66XttaFUSJm4O6WIy4fEXkoRgePwtsufpBlmncVNtDWBanEx-2pY8OoVVfGKoWjsKLP7DHlL8C20KrRhmTUI0VwMXHxKgHTVsw_EOlmigdpzBE0qGyjHup4Jt1R1tI8isxSmKN4Q9yGrhf1dU7lEULjUZ6NfMoFwgfpjeNfWbCL8EvsgGQGkxgGrk97xyvaqkSU88UVc88Dy7et874Z0NRMI3GD3h3cQyhUAJUiacuxcvvbRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91574" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8r7snYZnFYrdha5LOMCE87NnGnmKBWSrAgRTEQNi-GgrdUi7I969rmZWx17EWzN7a7fYKOtHb-KlzP_ZnGe0umNTJ7HRjLBTQNKKMWxSnmpYSQrOJqkkbWakbDYJwmQ530i5ACTfOWLe_jhF_ukm2uFdh8973_oDvPcKxb8Pt6zFABkVMh1CIMhqz9hkaViD-GgEH5ceBszDp91xpn3bwJBSAY92i0s2QPNsbrTSzTnBjpCMwBgCts9bqd9dpGhVGVBqjHomR0t1wYszfLCZnmvg0WbANI3gATWpPMKLbbMzXd-FqJejKVhSJ68KGmclP1xhuNKISCjzHlpW59zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdeLqBdv39MD345RG1_N8RPBO8YCK5nsaBbU8MkVqPQa-wKYqO5s5kA-5AvRu70yihi-z6QXS82bwmvP0IS5DoiHZd61VYhk8ag5vfNq_SpEXpccmJ6sqdn7ZCKqxGPGCurVrzfK_Mw7pb0GaR-8RkhwwHankkWMAiyT7I-7AMW-9SWDsGgQKpIeTpivkkLZ0WtOqQAp61WfZTsxPvMVVj1COPTV9Ptu2rhwa-4ircWLK8tFldayHsRe32eLYWv4joz_C2s5whyVCVrPtiaCC1qReUgdJsv1RN9mGatTuxWbOmXL2ib7uE2Xj9yAolReeru38nrfMjCmeZKEUqY6Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91572" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLUMa8oyGo0-rHy2558k1OGNTL8azjVNtEGGYqSq8OJnnHuFyXlrCGbtGEeLq1VNRwlfAfRuowRS3wPd1cTwdSHMxlSTcmq5_0Lwu3qVYV9RPOp9ZI89IfVPP3eRWGHeaseOL9yE_febijWUlQ2Z_3iXB86Yd4bEYHWOQdvgqwrvj630kEGdSSpWkWyNIJsDO3UWXxxnWMPCmHsqG_hiXwZlTzErsUC0KpMkrL6AJlrg1u1QIiVoV8HF5Tv0YM7gNybTuhCsExudiT3f0V6VNxwJ8RbJmNGeQ2voUW6T1QLelwreiX0gJ1GP0MW4Clr2V2oWEBiQYJlAqADwnxFS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کروس : بهترین بازیکنی که در دوران حرفه‌ایم باهاش بازی کردم بدون شک کریستیانو رونالدوی افسانه‌ای بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91571" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRZ8IUkIfV0VG6O1fE6gMn1STLaTWo6iqJcy25Z6Gu2Ix0hB2s5o2Veedy9H1q9YDEFXo9kIfdDQkPdtB3Dl33MPVELGgQo8tuUpfIn54gzC3FMEKrVYB1dHdhDCd9RgWwT-2sH_WmeAvA_cUHQsq4gFtjILlPn50QHEs_5JqTU9y66SUpR9E6IvTH-ezs54wyeXqhWf9shEgrqkbmAw2isMK2o2BJYTV3GJFEEjn9vuflfsV0xt_Y9CRNYIgbf4ni_as4VOngFQ9METeIgYbo_xxZW1FcjMneD3Cf4pduBhynVvaq55k6Z7hJY1wwi87R2clw7Cdomxiwi9YBnzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
دیلی میل: چلسی ۱۳۹ میلیون یورو برای انزو فرناندز میخواد
🔵
مسئولان چلسی
میدونن که رئال مادرید به این بازیکن علاقه‌مند است.
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91570" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=ePI0jEcXSPPu41m_L44lagLD11wbZtGliSq-UAyuVz9E0CmBRCpW1Wrx6wIwvwKScyuWUAkF5mK-9YylOxll5bRws5Dyey2P7gouWdNpKng2r1PW39KgxKZ8huA2yl9Ou4FmpFzbcNo0wak-hiccNvQ74GGkXMsXqY-c-74ljlYoM9UqEapdl9rT27PbNds6KsPJQhDGvYIVwfJaW0mVs3s9QSBN4oQHzstSyAhayCJe-YgAWXdLIJdKWKc4prj2Ww7XYYoUuMiRStavq-F3hi9IB8P56pQ8F6HfR-KRLjBYbLmh8GsrkwJdiTPv0Y5mTDt0qTr7dnD6isPjkZ95yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=ePI0jEcXSPPu41m_L44lagLD11wbZtGliSq-UAyuVz9E0CmBRCpW1Wrx6wIwvwKScyuWUAkF5mK-9YylOxll5bRws5Dyey2P7gouWdNpKng2r1PW39KgxKZ8huA2yl9Ou4FmpFzbcNo0wak-hiccNvQ74GGkXMsXqY-c-74ljlYoM9UqEapdl9rT27PbNds6KsPJQhDGvYIVwfJaW0mVs3s9QSBN4oQHzstSyAhayCJe-YgAWXdLIJdKWKc4prj2Ww7XYYoUuMiRStavq-F3hi9IB8P56pQ8F6HfR-KRLjBYbLmh8GsrkwJdiTPv0Y5mTDt0qTr7dnD6isPjkZ95yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
هیچوقت این‌صحنه تاریخی از لیگ‌رومانی فراموش نمیشه که وسط صحبت سرمربی یه توله شیر میارن رو گردن مربی و همه خایه‌چسپون میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91568" target="_blank">📅 18:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE9ILqGyvT66HfqZIiPKpK2kveWz17sIE5YkxJsBNL3BTHDr-OE2usBy25LFMUOrHQnrEGTPoz7nNx79lLdXL5YGARcpugx3vHJntBVynwZVhSSMEY5TgFJMLjw4hsm6z2tRxpeuU_OtEgN1dJPIm6PlmqqQicLJId_v3Db-PVJsvofHf3hMQxnTGCJ19ek91sbTQEU6sZQuc651x7RZZ063qrbODjY_K5sJdfvhIf3ctwgHUIOR5LWxN_mw3zjDkzTJ5F5gRAx9zFL89kMZ4DQiTdPiexGur3Hn0ZZzON1wBjHzxk9oen7qsnRxTD0HBPXHPINV9EtfTvQ6dLYuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه قاب تر و تمیزی حاجی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91567" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=TCXR6wHc6t-HxgIIrOGhCx9RztALNpWdsx3VNtS3OCXgjH23zQG_eIo7hR_QiEWoMjtbEvbUSC0DL4pVrT24DC_VcETHQNqJJIwpyzEB5B5U5vQ5NWWW8WqAmSxGhVaRXH-PBzZNU6gzmoI6mrA4LaMo78gFRXewgLC-ZPXdflTFsLWj4OiWSM-psfYE5mlPRQtESubv4oJf8uHAJs1PGnjT3W9mdrEK8QnaxuiaRFDCutnpdRkwBOFyIYmk590wIKRrAJ22iX3NJ_YrGjwAYyE4bZyEPoKIpP5kB0fZgERNr5nbtLB6HkKhJcIG8SMiJTU5fxYCZZzqll7WzpQdGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=TCXR6wHc6t-HxgIIrOGhCx9RztALNpWdsx3VNtS3OCXgjH23zQG_eIo7hR_QiEWoMjtbEvbUSC0DL4pVrT24DC_VcETHQNqJJIwpyzEB5B5U5vQ5NWWW8WqAmSxGhVaRXH-PBzZNU6gzmoI6mrA4LaMo78gFRXewgLC-ZPXdflTFsLWj4OiWSM-psfYE5mlPRQtESubv4oJf8uHAJs1PGnjT3W9mdrEK8QnaxuiaRFDCutnpdRkwBOFyIYmk590wIKRrAJ22iX3NJ_YrGjwAYyE4bZyEPoKIpP5kB0fZgERNr5nbtLB6HkKhJcIG8SMiJTU5fxYCZZzqll7WzpQdGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نیمار جونیور ورژن برزیل در کوپا آمریکا 2021
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91566" target="_blank">📅 18:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=E_dO2Ogn2twg-U9bLfgX5kVJOgbzVfKkfF42IBeYeGxTF-3CwRH46VEs9Ne6UFY9WjvLIen8LBFwic0otscuUo6s5puKyKPNAOQ679KndymBQuxHLZ8vRwpJEA_LKSo4rJ5ZmajDeXX8EVaWKkURElRA3AmInY3jvQq1bE3ACYyHgoeEQfFuVzZ6ukrzBQ6wTS-9UtQyvmWKnUJ0zGJAmfy92pFs8t53pjfPrgWHjSk_w1a5WbWWqMv7_LtwsqVeLQa9aC_PMQHBP1NpjVPPudnffL73RwGwetvAlr1_WkUsNYz-xw61w_Lq-OHlze-LLdmR3y-6snCI7asb7jFtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=E_dO2Ogn2twg-U9bLfgX5kVJOgbzVfKkfF42IBeYeGxTF-3CwRH46VEs9Ne6UFY9WjvLIen8LBFwic0otscuUo6s5puKyKPNAOQ679KndymBQuxHLZ8vRwpJEA_LKSo4rJ5ZmajDeXX8EVaWKkURElRA3AmInY3jvQq1bE3ACYyHgoeEQfFuVzZ6ukrzBQ6wTS-9UtQyvmWKnUJ0zGJAmfy92pFs8t53pjfPrgWHjSk_w1a5WbWWqMv7_LtwsqVeLQa9aC_PMQHBP1NpjVPPudnffL73RwGwetvAlr1_WkUsNYz-xw61w_Lq-OHlze-LLdmR3y-6snCI7asb7jFtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۶ سال از این ویدیو سمی بازیکنان تیم فوتبال منچستریونایتد گذشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91565" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX89DumnurZk8mDE9eUF9gGzjW5kRX3o5hUG1X4EY6h1jUnFLFuKXg4TM_BWvv6OvjQc_qo2oR8S5wwxls5UDiLaxRM65dRyIU38_iY6zvRWtB36F_-jW-gNsmGsWW2bUKVFdHE5kmPsGFKt6zyRdkSeaSB3GhNpkqEiOpw4qI3GbQ8ctB3Cocd2khrbCU46kyU8Xi6u0_fb7eDqZjmwG2g__qrDombi-XSvkqqd_RNiry1PdIkJlKwPBqo0mi4pg6AZNnDzr4yumNvoLgc7fLZJeQLVzG2odfKseuq0EXYYYQOOc9QGqia6IjfhIxtFHJRxzv1q6n9tTmRLpAcEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
متئو مورتو:
روبرتو مانچینی در آستانه کامبک به نیمکت تیم ملی ایتالیا قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91564" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=Bh75oyMmRDo1IRkJ62eUPjx2LdtzWf145LGf-VUeZ9MhEeT3_QxztbpRhylJ4oYN5WAGihMQQ50065grH8eaE72YmUJKwmdBEA67S5jxmfA7m6qNVK3VT8ZBrORPN9TMk-IMypiWf2AC2cRuhHpxbpQFmauBaJOugLQMP7CVllNnM7YeBe31h0wt93uPsn5V4nuAVyoJh8wxiEb-gs_r8j8uL7YlztrsYvUV94Z_L-GkkZIsfSlS0ufsCXJ-Go0gA1BvOPWEUxNVlOFX_M8y8WiUh_dAFIyt2snWCE546ceGkD2ZxmNFto3MdtIiBSJcqKNwfZaA9pbM3ql6Th9-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=Bh75oyMmRDo1IRkJ62eUPjx2LdtzWf145LGf-VUeZ9MhEeT3_QxztbpRhylJ4oYN5WAGihMQQ50065grH8eaE72YmUJKwmdBEA67S5jxmfA7m6qNVK3VT8ZBrORPN9TMk-IMypiWf2AC2cRuhHpxbpQFmauBaJOugLQMP7CVllNnM7YeBe31h0wt93uPsn5V4nuAVyoJh8wxiEb-gs_r8j8uL7YlztrsYvUV94Z_L-GkkZIsfSlS0ufsCXJ-Go0gA1BvOPWEUxNVlOFX_M8y8WiUh_dAFIyt2snWCE546ceGkD2ZxmNFto3MdtIiBSJcqKNwfZaA9pbM3ql6Th9-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اتحاد و همدلی بازیکنان اوکراین و دانمارک در صحنه بازی دیشب و سکته اریکسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91563" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeyOpkrmU9Fz7AkMvdNvl4hKgzVGlCLHzHZTG7I3iMcdcteikAXjtNAYLftamZFGBB7-I86YgFIBZsB4TA5fYksIhVCBjPRdHJedPN42EK9_16WAMTnSZz_dP5ETqxr-447Fq4gbK8tKcjws2_ysgf_99bA_1F_pOUaS0H2cJkdKj2QaD4ahv_5SQwtuWorkRRMo3w9FWrqecdsg-Wf_WZrKOMZe5nYFPlB8zUK-uPoI81MB6GqrX7urgw-AfEM0BtmucGBT7s0u3RDzq6jnTY8q_FUZ5fWBSrpMuijsFrbnYjPUS2cLpKBCvuVzpFycN1gLYRYz7qhpN5jLvpLyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۱۰۰ میلیونی، از اینجا ارزون‌تر درمیاد!
😎
💸
وام بانکی از اسنپ‌پی
با ۲۰% تخفیف
خرید اشتراک
📱
💙
✅
تا ۲۴ماه
مهلت پرداخت اقساط
✅
بدون ضامن!
ارزون‌تر از همه‌جا، آنلاین وام بگیر
👇
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91562" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=DfQP69mCfaiw8LLYBRJs9L_MxHK6kOUBubS3qZlN7OHOrLuHk7nSuRK8hM5bN3M-Aw0QlK--3TFD-uyr8Mkrj0c8EaKMsD7myZzsrhV8AXVQVSCYiZ-1dVg7KC45oOlJMhQFRXpXjB6_3EFOHLkS6Ie40aD_6kmu9lOQN1JElquMymD6tvEQZJpSNkyABbci5ZE_wiW1U9zL6_yLq79V_ltc34SqTBalnNM8Xb45wnm4hrSSSbpNGQNSkqXhPs9c8RP2-U3Q7XYT0_WyWoeUVKnm3HaYkt9MRP1hZXxkWRz2J8J_O7aj-oM0G7mPdJA5p7WOdLzIDqG4FU0nXS3NHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=DfQP69mCfaiw8LLYBRJs9L_MxHK6kOUBubS3qZlN7OHOrLuHk7nSuRK8hM5bN3M-Aw0QlK--3TFD-uyr8Mkrj0c8EaKMsD7myZzsrhV8AXVQVSCYiZ-1dVg7KC45oOlJMhQFRXpXjB6_3EFOHLkS6Ie40aD_6kmu9lOQN1JElquMymD6tvEQZJpSNkyABbci5ZE_wiW1U9zL6_yLq79V_ltc34SqTBalnNM8Xb45wnm4hrSSSbpNGQNSkqXhPs9c8RP2-U3Q7XYT0_WyWoeUVKnm3HaYkt9MRP1hZXxkWRz2J8J_O7aj-oM0G7mPdJA5p7WOdLzIDqG4FU0nXS3NHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ناصر الخلیفی در شبکه الکاس قطر : لوئیس انریکه به مدت ۸ ماه پیاپی از مرکز تمرینات باشگاه خارج نشد او هر روز از ساعت ۸ صبح تا ۹ شب کار می‌کرد؛ تا جایی که نگران شده بودیم مبادا از شدت فشار کار دچار مشکل روحی شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91561" target="_blank">📅 17:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3Rq5BNLOPUY7nVFUQXRl7xOXCkCtmJR37MaJ6UkQ3m6i942Ox6x528dCzSmoFH9NmfOLvUpB59f3mGQSDxgD0M90dwjAQx7iXT1hzWCqJKNgiy7ZgyIL3l_3ibuv-mgXjXZvPORNChSI_X8eHd4ZQOehHX-xEgu5KCeJ-h2BVxOfny_fBPE2INbiFvMRWglw6k4KpUDOUDFJg4aIQbHiKVnPamoYwYwIcKXJZ4lnA2vQSVF6zHlA64MxxcojY1oslwtmS-IxVARdJ-w0ZcsWQ257CnC0xY66tBJsT-cYBZ_xR8WwggCBlGrn6gq33gBIOo8zpr_6iaUUyh9QfmUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ur7e5HwGYuM5cOZP8B0uwOrCGD4XKbar-EdhAsTuD59tH2hTKn3Xj1W8q56FQfoP5NdeNttooUwed5K12CbbP55Jy6zgiAKb4jRGWHiu3djN1I_IOdpTOwvWVwNYMrlbk84hiKg9DbicOZPJw3ashunsarmC0uXIX1jDahS7On3YKzSVl1S6_uuteZCgRgQV2kPWNn2QaJs5jKvKQn-9XFnFJKG8SdE2ZTjgeQ3sDf7RnbAywidQD8BpwCMxQ2ZS-Pu6Ln_K_nOg_gNSIyDy8RxFxMc2f3vA3CjLZJgsm8P6nWUnYo2qP048Ka2W3OIwvuGB8Gt1RlLaBNZXXr0k0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله وندا بهتون سلام میرسونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91559" target="_blank">📅 17:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSIriQUqPPYZdcT4lBbzq3E60tMt2QdCRT1ASkcf1w0mTxuQ5DAkc2zjx9eiNw40SnxgRzNjxPSYwCVPwJEr76NdSYVJ1WNYlq2BIpJtetQLiDz1Xyv1w8UDa3Pnsw6CMxrvyzoiWsOxLWxsVBm64RqXEAmCmGKJBV2yoCsVbKGP8Fhy-q9Xp8hgqP63qI6rkjy2moWIHKWQdXMfiRnYgKnETnd7_h4-xocqaRn6mFGIHiWoHDVpLw3vBsu5sg0JTpxT9ND3xcN8hvunGYu2NNl_1oSuVmcsVcDYSUqanOPTvpKZz0TZlkDZha6mOriYOf6ik9Gh4FVfhyWb4RYawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91558" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2681453adb.mp4?token=AbcbeWnzXn27arIKmED0L4jp4sh0WNbIghzKkoIkyyFMqKmG-VeM_NOhjOOWhKDPrCgnWG9ua1bQcKxcYgWAIuqXiPL36BrH2RToBjmkWMGelWle1TXkeWdgp6-wK3_eL_D8vtWCrOqUvJBo8QhnpVus9OeZYjbXraLSGeBfZbYtcjWsLS8ULI1GXHULyYiJ1zXaet1LS_FN58e0Drr0NrJfzCW6SGP_P5s27aeXYph8vgPSbOoliZVKlyTYwI4dft9CYZjHd_RbrK8onkcT-WWiWGzcu3_gT_i7SCBjNwJ-bxb9JyhVMF4uDDY_1VGdqg9y-TmiNxuVp1lcGfkhYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2681453adb.mp4?token=AbcbeWnzXn27arIKmED0L4jp4sh0WNbIghzKkoIkyyFMqKmG-VeM_NOhjOOWhKDPrCgnWG9ua1bQcKxcYgWAIuqXiPL36BrH2RToBjmkWMGelWle1TXkeWdgp6-wK3_eL_D8vtWCrOqUvJBo8QhnpVus9OeZYjbXraLSGeBfZbYtcjWsLS8ULI1GXHULyYiJ1zXaet1LS_FN58e0Drr0NrJfzCW6SGP_P5s27aeXYph8vgPSbOoliZVKlyTYwI4dft9CYZjHd_RbrK8onkcT-WWiWGzcu3_gT_i7SCBjNwJ-bxb9JyhVMF4uDDY_1VGdqg9y-TmiNxuVp1lcGfkhYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧑‍🎨
اثر هنری جدید حمید سحری: تاریخ دوباره برای اسپانیا تکرار میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91557" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP7VsKk-D9fjDJPdPMf8aLToiOWaid1wm05yQZz3yBdZeeLz1BjXWfkgkU-OfycUwCXnnAL6RHC-f2_PJMx5hg_pNUtTKAnSyX7duU8tfOFwZ2d14MfYkfMA4-zXYmlOfqbSay5neIAffRwz6DfY9kgexB1MNGzepFeiYKYahdlj-HBT438MjNgvagSwuUtn9_HoDjVSbgpLGcQCaH8ADT4f3OuvPv-Jz6gOumzkjSs96VAHqvzlURL0PUChU5tWM-r0lqGhrva9zeaUXL9bIPtAKA4sd2a0AX5plkxsGm8lpf4xw49XwxA9Q2bkQhouoZ7gZg1luSYAfu4ceiYRpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زین‌الدین زیدان:
🔸
قبلاً بازیکنان آزاد شماره ده بازیکنان باهوشی بودند که بازی را به شکل دیگری درک می‌کردند. حالا همه چیز فیزیکی‌تر، منظم‌تر و کنترل‌شده‌تر شده است اما فوتبال بدون شماره ده شعر و شاعری‌اش را از دست می‌دهد. فوتبال بیش از حد فیزیکی و تاکتیکی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91556" target="_blank">📅 16:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
اسرائیل دقایقی پیش جنوب لبنان رو زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91555" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.  امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91554" target="_blank">📅 15:52 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
