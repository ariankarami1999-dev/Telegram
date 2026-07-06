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
<img src="https://cdn5.telesco.pe/file/DBUGyP9XCfgTskyw8EO2l4-RpnBK0_ZTVJWRtCI5E91WaIR6xpo2WHurdDurbgmH6xqcmllNw-UjnxmcpsO0d1oe-1Uv_yAmQrWuBOdtwPYAJWXva-WTUxitvYs0kQIZINNLH44h-RgFA8sccEI-2Ny-1zNJW6tXAbmlcBXP4gcDJqHGpolqv1_Yg051_vs4Jk95oaTlPCPveQkVazjw6hv1rsWx2bZXGe8TVociXohw8qF4np_vMxbtuyb8oyEO4EgAY87W5l98c6uyVxzLceXbO2eltfrEWo9rT9-s1wI87MTfZAZr42z_vwEj994isPXn70fnvwK6ZJIIXmt-Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 628K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-98567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=UoBzsiwTWHTL_3wits3nCqGpybthtiwyFgxG7x0mxRLj70vISo5_EbuHWWccP-x7Z-UEkIKkhJKueunMyBVuYbJLmbH0oL39bjEElU7j1zWG8Rwtve1bMw6yRH9wkeCUvkToY_G27xvSfwEbr_VhbxKCNdHAYO7yINzjQp28s0lNsDIuuH3B6VHTDffHfMOeuvJQPzTv4OaqTHP2UPpZ0cHrYFEgy-uCpClFDrQAgeBsX6Nugnh8ymRLlKipoPtrT52lYruMDfw0YvXsU1QIBV55-wbhLRfp4-DuuG3TzcBqQBP2DOw8lVT7uInUizcEbgswngpaTbTWktKgVNJ6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=UoBzsiwTWHTL_3wits3nCqGpybthtiwyFgxG7x0mxRLj70vISo5_EbuHWWccP-x7Z-UEkIKkhJKueunMyBVuYbJLmbH0oL39bjEElU7j1zWG8Rwtve1bMw6yRH9wkeCUvkToY_G27xvSfwEbr_VhbxKCNdHAYO7yINzjQp28s0lNsDIuuH3B6VHTDffHfMOeuvJQPzTv4OaqTHP2UPpZ0cHrYFEgy-uCpClFDrQAgeBsX6Nugnh8ymRLlKipoPtrT52lYruMDfw0YvXsU1QIBV55-wbhLRfp4-DuuG3TzcBqQBP2DOw8lVT7uInUizcEbgswngpaTbTWktKgVNJ6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی برزیلی‌ها بعد شکست دیشب
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/98567" target="_blank">📅 15:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgGIXUgXCnZni2gwJnckjVjTPNAsVvtWoFlJ9y4iL_f7RIQZ_0OPcu4NpcGCBhVtzZYn6_pRskaxfhz0T7hjUX4hJvQqixl39WkK2EOxaW5AWIcqLn8U-XfcSVHrZqChmrBwMz-_qPtReychzJoUUzsMTmCkSJrN6OaUoxLVMvoIWMQZdCoFYC00YQc53CuQ-5aUcJ3MlwyiYmJoEv8TkuXMAUabVhhNKMc6a0s2lBbSfi7t2Dq0LFHGuVqVzgqmV5_kxSJcbJlIhNbFwQy72BgniR-a7H7vuJlRb-dK-HER94kqsfgT0u9sLM-xG5SLUcTTFRzhAluk-yMbfg9guA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو:
کانگ این لی از پاریس سن ژرمن به اتلتیکو مادرید پیوست؛
HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/98566" target="_blank">📅 15:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=u47PXxohTsmaq1EoVw0IuYiJ0EHuRQUVr7Vf071RzyUUIIi_IjtqTucqK78W73kZLz2dbVyqcVZg8C-bh5Qg_uWOwtzGmDHIu2s6-0P--9qnOpmYrgFHBgc2hE9-UrdHZxAL9IjK1PJJJ5xdjNLfYvAsLc6U9CP0d3sHw8ybjKauADr4xYu80a-SfUg7YajHzr1RxM3zZIm-6x2zdS-bh3Iyb1ZpMaWEAsR-0YQ5VedbZQXnqb7auDR1-8hAt9sJbkSAqomjZSkidDDScGxeqHIzlPKZ0m8C8sQussLec1jmmGnkXL3OEiq0bTx8nPoQ24sBa5isHc5ABmkyEgZEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=u47PXxohTsmaq1EoVw0IuYiJ0EHuRQUVr7Vf071RzyUUIIi_IjtqTucqK78W73kZLz2dbVyqcVZg8C-bh5Qg_uWOwtzGmDHIu2s6-0P--9qnOpmYrgFHBgc2hE9-UrdHZxAL9IjK1PJJJ5xdjNLfYvAsLc6U9CP0d3sHw8ybjKauADr4xYu80a-SfUg7YajHzr1RxM3zZIm-6x2zdS-bh3Iyb1ZpMaWEAsR-0YQ5VedbZQXnqb7auDR1-8hAt9sJbkSAqomjZSkidDDScGxeqHIzlPKZ0m8C8sQussLec1jmmGnkXL3OEiq0bTx8nPoQ24sBa5isHc5ABmkyEgZEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
دلیل انتخاب گیمارش بجای وینیسیوس برای زدن پنالتی از زبان کارلو آنچلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/98565" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98563">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlMtebpHaH3132DvvEvTjMGvOXJ6bm2-jLxZexfP2fBJLN49l8RqtLL6G7vKcDc3ndsFG87jg9Q14OL0Pu0dl01dnXr-KGpVfejU1Uh9lOQJNGZuWmRo64yMJ0wpto1x5xQdmWEuZeWnVViiHstLDE5ZqOxUBs42lu8LzU5gsj_AA_eLJpICLcMrN7T8bLiXszQsDfcCo4P-E79_J2v5jp_EK_oDJpOgQ3VD90UqojEx4wMXg71YVrZI_GZYHFzZoJjyHiovXeykIzKc51FvkT7cZE_WUJApz08WvIbJhpHH_pd_BRndQiTJlVvgFhi4Vw0i3QSeUqDexStJT6_WXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oT6iG9MGdkSreyHYe6gXaI_LQ0q-kCDIV4J8muNjXn4S0gH2k1uMFTlOMFFTrILjzm-dvyMCWxnFeI3cRjbKGG4WxDGidFrslQr1o5KM4mBRco14lNRWFw0hmDKQ_XXAM-i4bEnEQbhYoBTvJLLRmvhw1igb-NofZ9oZMDgLiDKtTHhKqizCgoNh0iUkphg0Ly_y2jyXlPHu032C7DxuEBldHpOOzbXlD0VTsAQa_zBEW4T-4f90NCQquECc7tPmVAibFHLLB3vAl6MjC-DcX2-9PekWenGw4f4iWRUQPPlAJy2ChhmOzifJKbr3YUhZF9XCGwNQpSY1CI9sOLenog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
لوگو ناپولی برای فصل بعد به مناسبت 100 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/98563" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98562">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/98562" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98561">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/98561" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98560">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=jgjK13AYbtRrxTxpreB21Fp9kknYxV2oruMDCJ5ps5LcuVytHuI0SHWOZ7hLM2AZzbR1KpskIhOPHSi6BccJyRHFcciUpEMcZ1KOTRS3mayHqEREiLeEu1Xt2Bu51k-Cryd1oO9XdtQ_w9RDOkjd7rwR71vEKgTwpsV-go6hOtQQID__xbPTvx5gmat6I3rmIg6pLmH1dBOG9IU7HjcE1Svm4PVrc9uz6T4kGvQY3-hKmBNdTv164orLIo5ESQuh3SmCHwrjzNMdpv2-gGPgcVWNpCojL4M9GGKjJX8_WjDBB9E6b5WLpq3WC2FoI-yATrmMP8r2sZtje5fJqamtng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=jgjK13AYbtRrxTxpreB21Fp9kknYxV2oruMDCJ5ps5LcuVytHuI0SHWOZ7hLM2AZzbR1KpskIhOPHSi6BccJyRHFcciUpEMcZ1KOTRS3mayHqEREiLeEu1Xt2Bu51k-Cryd1oO9XdtQ_w9RDOkjd7rwR71vEKgTwpsV-go6hOtQQID__xbPTvx5gmat6I3rmIg6pLmH1dBOG9IU7HjcE1Svm4PVrc9uz6T4kGvQY3-hKmBNdTv164orLIo5ESQuh3SmCHwrjzNMdpv2-gGPgcVWNpCojL4M9GGKjJX8_WjDBB9E6b5WLpq3WC2FoI-yATrmMP8r2sZtje5fJqamtng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
کثافت‌کاری رودری تو تمرین اسپانیا که یامال حالش بهم خورد نزدیک بود کونش بذاره
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98560" target="_blank">📅 14:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98559">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=Ho4ZkNbfwoEGcUUTkmO9ny5lsUZ1Lt-CXmszkJPBL9sjgYuPKgtTE5t08Jljgl49hSilPm-xyuv3zwYFuY7u1tgA1cz02Zwv22pbRHe-rB9JwA8nF0tos5VJa2e3RftlHX_XcQU-i5Sr1FmsyZbKCdWiWDbc2OQmrYlu3jecb6147SdlcpstezvYqfumDpEJ-XoAgleqWvpcr0g5W4fL4yfzKIOfpA51K96cbgpcYK8SUPqO7iyBxrts-8irgjp1FYdCaBB1BmXH-HkpVEpKvz9R4P3CHQwklzm7t1kjILF8bsMxqFIOBxWgk9NhiuaSCIpI7mci_4ir80b7fn1EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=Ho4ZkNbfwoEGcUUTkmO9ny5lsUZ1Lt-CXmszkJPBL9sjgYuPKgtTE5t08Jljgl49hSilPm-xyuv3zwYFuY7u1tgA1cz02Zwv22pbRHe-rB9JwA8nF0tos5VJa2e3RftlHX_XcQU-i5Sr1FmsyZbKCdWiWDbc2OQmrYlu3jecb6147SdlcpstezvYqfumDpEJ-XoAgleqWvpcr0g5W4fL4yfzKIOfpA51K96cbgpcYK8SUPqO7iyBxrts-8irgjp1FYdCaBB1BmXH-HkpVEpKvz9R4P3CHQwklzm7t1kjILF8bsMxqFIOBxWgk9NhiuaSCIpI7mci_4ir80b7fn1EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
ابتدا، او به عنوان داوطلب وارد زمین بازی شد تا پرچم آرژانتین را برافراشته کند. چند دقیقه بعد، در حین پخش سرود ملی، دوربین‌ها او را در حال خواندن هر بخش از سرود با احساسی که همه را تحت تاثیر قرار داد، نشان داد. و در پایان، او مانند یک هوادار دیگر، تیم ملی را تشویق و دلگرم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98559" target="_blank">📅 14:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98558">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRMjMwpb6BhOVXWGbd4JLIaSh8WdNhHz6L4Y4LlQVL8N0wY0BNfuJyGGNhOki8UVzXLt8psC_grHuoubqWQc6NYL6MnXRqLkJrjHDvpm4DaJufsTtqwRhw2jUkcTrgN25pRkFbjONPEmwoeJdxTNboTOYB23ue5CLBXcHmHYoJ7jhzoZOnAH6qO6AuMtst751gk2iQsHzZqu3GPinwFHlveaRsZr32TusKRS4QOPTe67o1uUsmEhJUoBi4E9LSaFzxFclmhLQX5OlVr7c2ADkmlR89_66jHDYXqkWOazlTPGkJO4Lxm8VqQcs_IKVAOUyIRnUgcrx94SkAV0MRKFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
فلوریان پلتنبرگ: آرنه‌اسلوت گزینه جدی سرمربیگری تیم‌ملی هلند است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/98558" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98557">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=Msmsva_c7ChV77mzMb-7fBl8EVKYXiKDPYXugj8jE9aSnYNLdfp7hMlC6aZBjzEcPfLIRkHEBLZ7pgn7j2ijc-huXKqnsxazWnX9xcJoIyokU9M9OECa8VhRuj8-0r4cdLsblB1RANvH8PYK8WfjviBAbKTZPl0EVXRXsXtudeyeoBTlLIY8JcmNe6S9U5t6JrBG6CaiNzLBjmTI5s5NmXkeOJkEw2GK2TFlvtuWbII0hLu5m6BEq6guLmdYBLWFpJ5odmLa-XP3NBn1QhE-rMAfCPy8BrMedcTddwQvO_pOj7SzNcgC_5_THXmFwkD_nAaOdR32SHz98ydfg5ny0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=Msmsva_c7ChV77mzMb-7fBl8EVKYXiKDPYXugj8jE9aSnYNLdfp7hMlC6aZBjzEcPfLIRkHEBLZ7pgn7j2ijc-huXKqnsxazWnX9xcJoIyokU9M9OECa8VhRuj8-0r4cdLsblB1RANvH8PYK8WfjviBAbKTZPl0EVXRXsXtudeyeoBTlLIY8JcmNe6S9U5t6JrBG6CaiNzLBjmTI5s5NmXkeOJkEw2GK2TFlvtuWbII0hLu5m6BEq6guLmdYBLWFpJ5odmLa-XP3NBn1QhE-rMAfCPy8BrMedcTddwQvO_pOj7SzNcgC_5_THXmFwkD_nAaOdR32SHz98ydfg5ny0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
فیفا تصمیم دارد تیم‌ملی پاراگوئه بدلیل نقض بازی جوانمردانه در بازی با فرانسه، جریمه مالی سنگینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98557" target="_blank">📅 14:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98556">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=KP7KX_DufFGPOLnL5XztSDB8npvwyEBCHTekE_6NZqcXc5ny-Uc-6BEV0zO24t68uTXLSPwO4RZ_cf67UjxP2nEIQ4JTAim94qyVm5l_d0o5de_mRVdxFfbRvvfrydM0AsGaRK877oYskmFKlSgv1EywpbPkaWrWRfOLjFK4kLkVs9vIli4RzJP9XRRNxgZ2mM5CMXcTEVdvMtZzIFsk5MR41kEwKsaf0DUqtaET4goyn88ROclH3OWOTf5VTw5bbeadZeiljeIjoZjI49Fe3qkgqhFImB5kKslpN8DkqZMSphFNAgv0U64uK6kawj4F7CaUvb0hYuf0-jl3G9z9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=KP7KX_DufFGPOLnL5XztSDB8npvwyEBCHTekE_6NZqcXc5ny-Uc-6BEV0zO24t68uTXLSPwO4RZ_cf67UjxP2nEIQ4JTAim94qyVm5l_d0o5de_mRVdxFfbRvvfrydM0AsGaRK877oYskmFKlSgv1EywpbPkaWrWRfOLjFK4kLkVs9vIli4RzJP9XRRNxgZ2mM5CMXcTEVdvMtZzIFsk5MR41kEwKsaf0DUqtaET4goyn88ROclH3OWOTf5VTw5bbeadZeiljeIjoZjI49Fe3qkgqhFImB5kKslpN8DkqZMSphFNAgv0U64uK6kawj4F7CaUvb0hYuf0-jl3G9z9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات دیدن فوتبال با گزارش عربی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98556" target="_blank">📅 14:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChdTaPQN77_x7qDpDK8DqA315a6XRNFYfDo0gqI7mdFLvZ-GX1MdgqoPRSdLNVq19nP3LhuO0wwX1s7goxnJi0vKi2Qm0GhAcCrJ1jVB3H6h8e5JBMp4o_NLIuDmEZae8UIhqiUalfQXdcynTTX-aU3TZ7fBaGVpcXHDHbXdZWNnFWimvPjgx1SCI6XiElOMFE_a3Wp-RcNtIPro5FexMhwaCRCnsObLNoQvtoEFoaJsrDOTxTB7I3dHfGyQ0EQrmqF3PMPr5nal6YiRFxbaApCV43aZfpJOy7PUimx7D801rWQfGEPnQmNiHrGup58YKraVMtPlochCQn4siX-nNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس‌توخل درباره قضاوت علیرضا فغانی: فکر می‌کنم قضاوت داور بسیار ضعیف بود و همه سوت‌هایی که زد علیه انگلیس بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98555" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98554">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=TZAPSuLAFUtMvs2vIQ3vDCU0pJ6pAJSQWhONSAJgk304grB5W8qv68M6NSa4sorzZgWtpRynhEgFfir61ajOUvpk5vWxzo4wi2XsmwIAKs08uEoD8P5V11SEv2WK6Hjhf1rPHx1FqYSa40IOVxawNXjk19MMTStaJU6huDMkTi1z_0-OfXm1kA7UrmakFKosAh6j3f_slQsQ3iESMJ-NiNiGaYXWPVTAF3nOwmodpuKF5jnJA5ywBLXNJuJWWpenNgjMjBMMrDseIi7KFhEu9jO-lRVeGIXVPG5aBhxQn9wB4tqM6_SEDy5RWS_amUhAY0-W0MR6L-b5t5ez_7MnF622xcKXS7MjjjSh16BdJ1h90djK7bDCUd-bXHAH8K01UyD0oK_7GqfNRR5jr_0wGihPBe513MDlNx8Fejlk4wXul9lc2xLUmYFYGUzm8as1AoHN0dGgOWoed2gfuf5FZZCbgvwdr19EiCBL8xc42lK4HIjx2QTMFOFhFv1mN_QzSIBU_wqZVE7Q2vGCKAnZzjQTYdrFlZADR0uXSSU7hwILyL4eCRNLiafjLMFeLH3Vv7YuD9SpQvoMbmi7ajYl_vXqrhwiuSClHL3Sl_sHKIqoKlxgu5p0UDOSA9llYyYffDSVZTBOd7p1mZXBI5ybl15JLD7sd3IAUnfqAk1Jrh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=TZAPSuLAFUtMvs2vIQ3vDCU0pJ6pAJSQWhONSAJgk304grB5W8qv68M6NSa4sorzZgWtpRynhEgFfir61ajOUvpk5vWxzo4wi2XsmwIAKs08uEoD8P5V11SEv2WK6Hjhf1rPHx1FqYSa40IOVxawNXjk19MMTStaJU6huDMkTi1z_0-OfXm1kA7UrmakFKosAh6j3f_slQsQ3iESMJ-NiNiGaYXWPVTAF3nOwmodpuKF5jnJA5ywBLXNJuJWWpenNgjMjBMMrDseIi7KFhEu9jO-lRVeGIXVPG5aBhxQn9wB4tqM6_SEDy5RWS_amUhAY0-W0MR6L-b5t5ez_7MnF622xcKXS7MjjjSh16BdJ1h90djK7bDCUd-bXHAH8K01UyD0oK_7GqfNRR5jr_0wGihPBe513MDlNx8Fejlk4wXul9lc2xLUmYFYGUzm8as1AoHN0dGgOWoed2gfuf5FZZCbgvwdr19EiCBL8xc42lK4HIjx2QTMFOFhFv1mN_QzSIBU_wqZVE7Q2vGCKAnZzjQTYdrFlZADR0uXSSU7hwILyL4eCRNLiafjLMFeLH3Vv7YuD9SpQvoMbmi7ajYl_vXqrhwiuSClHL3Sl_sHKIqoKlxgu5p0UDOSA9llYyYffDSVZTBOd7p1mZXBI5ybl15JLD7sd3IAUnfqAk1Jrh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گوستاوو آلفارو سرمربی تیم‌ملی پاراگوئه: با انجام بازی خشن جلو فرانسه، میخواستم یک انقلاب را در مردم‌ پاراگوئه امتحان کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98554" target="_blank">📅 13:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98553">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afvOV5PnABY0QBq1RgaGcdEK8kN-R7eaaVOK3BT4G0sM7bCf_Ng1sMYROj_MIBsrmm2l9id-lAZvW_w9xrPA2wv1xssdN7wlnYXLirnQKRinehhu90_8hjqO0aSIBc9LjOomb9PI3u2hIsyGnXS-7zeiSqMhj2hBhKwolgO32c2mW_ihP-_y1kpAGS7sGmIMwEbf_FQ4N29rTc8Wl1LixiSoHN9YbEmpWoeAaWXpetIyhoVMhhya8lJa8betxLpH8mNcXECWhw1ky9eKHtsnrGStvakssjEQHTiT2tkHgo3QFXDK4Rigk-xTaCYpbkE295WN21VF1aUbWujgG-wWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاتنهام از جذب ساندرو تونالی از نیوکاسل به مبلغ 100 میلیون پوند با بند تمدید قرارداد تا سال 2032 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98553" target="_blank">📅 13:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98552">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98552" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=tIODs3iETqK7S4eiKxYX86ai9MJCyv21SgCSDfrvViSzLOPKVARU2YkWz8UYR_woy3c2zN-wVl4tiGnjIfskwCUFrHPxTgTa7FiIxJ4n_DA0exAltGBIX4dVXnW6C7JIkZxLFknG7ciZRRMPZVNHHgL_fBRui3bTgyKfoMU_SwuvP2FZyfVmGFUSvqggUZ5dBTAVbvmCt5nUZW21yr3lczVY11f7u9fz7n-89DixzaxM0zYsNpK1wqCcVb5rY3B_j_oOwjYv9FH2ZC2Dcn5-gUnOwVeg0AH-JoV5gtxxmnLbjvJxMKwYiV2_1WXtdQqIoOLX-TM5qq-J9dbxGqJpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=tIODs3iETqK7S4eiKxYX86ai9MJCyv21SgCSDfrvViSzLOPKVARU2YkWz8UYR_woy3c2zN-wVl4tiGnjIfskwCUFrHPxTgTa7FiIxJ4n_DA0exAltGBIX4dVXnW6C7JIkZxLFknG7ciZRRMPZVNHHgL_fBRui3bTgyKfoMU_SwuvP2FZyfVmGFUSvqggUZ5dBTAVbvmCt5nUZW21yr3lczVY11f7u9fz7n-89DixzaxM0zYsNpK1wqCcVb5rY3B_j_oOwjYv9FH2ZC2Dcn5-gUnOwVeg0AH-JoV5gtxxmnLbjvJxMKwYiV2_1WXtdQqIoOLX-TM5qq-J9dbxGqJpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحنه مصدومیت دیشب هندرسون از این زاویه که احتمالا ادامه جام‌جهانی غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98551" target="_blank">📅 13:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=blXlulK5jg2IhfglIM-BpZICJulOuTfXMaXM8FHyPBxhyI7EUDqyCoBga8Bc1DIKAfIfur2z12CneJf3VOM4xQM15HNjurh6aUUGMbaYkZG_dpVfD0RP1qZ6z671rF669Al_HesnPVB-Ot7Z4KEb7SYGxR43riiCt2xng9qwQndmoDYho4V0p6TM_NWY7NUaGNFolG6b39vW9bqLehwC-UX-1YdSbGpGgsgfLzm4S54SSTvCoG16s6EjZ6yrtF9plrhEByPxIr-k4PbCR1U0BtF5cFky41CR64--pWLHGTDoXJusm5acid7XqgndfMS3XevRgm3zwZfJTiV_djD67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=blXlulK5jg2IhfglIM-BpZICJulOuTfXMaXM8FHyPBxhyI7EUDqyCoBga8Bc1DIKAfIfur2z12CneJf3VOM4xQM15HNjurh6aUUGMbaYkZG_dpVfD0RP1qZ6z671rF669Al_HesnPVB-Ot7Z4KEb7SYGxR43riiCt2xng9qwQndmoDYho4V0p6TM_NWY7NUaGNFolG6b39vW9bqLehwC-UX-1YdSbGpGgsgfLzm4S54SSTvCoG16s6EjZ6yrtF9plrhEByPxIr-k4PbCR1U0BtF5cFky41CR64--pWLHGTDoXJusm5acid7XqgndfMS3XevRgm3zwZfJTiV_djD67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر ابوطالب درباره حضور احتمالی ژاوی روی نیمکت ایران بجای امیر قلعه‌نویی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98550" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=nAElG_LuXL_6D7cDEIlb3o3UfGNMaf78iOMOf0KQF76vCVHcFTALnuJJqeXJ-z7hpMadfHKej8Gazzc_uJttf4kXSS0o-y_SYj-LdLInDSkRlrEzAG8QplmxpskxxKu1BwZIA_qAdVDF35xGnbVBmJ7bT-7w82kG4eUVd8QVYk-1m8k-bRigh8PRJJAu64tkf0LDbE9gxYLBdOMojq-A2qTupfKAPzgHlmbgaTpfUCc94h44fREcYpNqohf3q0Mgz-84tO3j0rlpOtvU_c7Iv-E3f_ITonBBBKivU39odcGUWubBfzrpkqO2BQYfpCSxrqfcYi2ILAD03bWSLXwUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=nAElG_LuXL_6D7cDEIlb3o3UfGNMaf78iOMOf0KQF76vCVHcFTALnuJJqeXJ-z7hpMadfHKej8Gazzc_uJttf4kXSS0o-y_SYj-LdLInDSkRlrEzAG8QplmxpskxxKu1BwZIA_qAdVDF35xGnbVBmJ7bT-7w82kG4eUVd8QVYk-1m8k-bRigh8PRJJAu64tkf0LDbE9gxYLBdOMojq-A2qTupfKAPzgHlmbgaTpfUCc94h44fREcYpNqohf3q0Mgz-84tO3j0rlpOtvU_c7Iv-E3f_ITonBBBKivU39odcGUWubBfzrpkqO2BQYfpCSxrqfcYi2ILAD03bWSLXwUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
🇲🇦
بازهم تقابل دیدنی فرانسه و مراکش در جام‌جهانی اینبار مرحله ¼نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98549" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVWNpbkna7uw6agWPjqVvTqwoNFcuOuFR3hlEXSG2KaeVVsaXUIKnB2ZJ8afBWbDatcSQAphPkXiiHIxsP8MQTWJwePl5uTdDgiEdMUXDVjXiP5fhqyqBb40quI4GXn3Gw134ZE1a45YFk6XoCsb4LsMAkepmxqOOo7ehg76m9CZffD31Rpj-epsChgqUKSNrTxmeIJixX1QlHso6I14aCMDhFFgonA1HSJf6mJ-_IFKa1leMkVyzSg0DTotb3m-TG_2dOUUA6H2LPA49ckqhw9V15wzMUqJ6K0V6Z8K-zWAVHMLTGti4Pits7p0dROyZS0hnc4vIqhMoJslJ0ltNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلاسنر سرمربی فصل‌گذشته کریستال‌پالاس هدایت ناتینگهام فارست را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98548" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=hf6O6RQzvCUfrPgLnBYXEchK-x0_-a96i84tLhxncpYFdl1F2YhJ1h2kYC39D1fC0ibHImNYAqSk9i3gC-C47eQ-I-K-4J4PEkd3GPFEvH6qy2S6ohJJC335ToijlQB5Wy9f274YoXSje77SlwpSyVbGbu0tNv-rFrsmCJR3JHZ36-oHphG3AA7yks2jxrkonMEa0dAvJcXV0rW93gFgO0dDIAvSS5jb0hmOW_03o_6h6p-YzNFn9hXR4LjLaFnLp3bhz-pcWHEe0HENdQhwcKW1ow6t4ef8QSNaRAkuDOXWGmGphwmOGTqxJyrZ9cP_IoSW4UXZWfgZX2sJyZDntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=hf6O6RQzvCUfrPgLnBYXEchK-x0_-a96i84tLhxncpYFdl1F2YhJ1h2kYC39D1fC0ibHImNYAqSk9i3gC-C47eQ-I-K-4J4PEkd3GPFEvH6qy2S6ohJJC335ToijlQB5Wy9f274YoXSje77SlwpSyVbGbu0tNv-rFrsmCJR3JHZ36-oHphG3AA7yks2jxrkonMEa0dAvJcXV0rW93gFgO0dDIAvSS5jb0hmOW_03o_6h6p-YzNFn9hXR4LjLaFnLp3bhz-pcWHEe0HENdQhwcKW1ow6t4ef8QSNaRAkuDOXWGmGphwmOGTqxJyrZ9cP_IoSW4UXZWfgZX2sJyZDntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
شادی مردم نروژ پس از صعود به مرحله ¼ نهایی جام‌جهانی؛ آدم واقعا حسرت میخوره...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98547" target="_blank">📅 12:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effa95670e.mp4?token=AH7KgAclnv-mv7DDYjeLIa_zYjadkC7PMOVCgCeeGuc4J_FgoaU9cVIBwftl1prZkV7GePyohedLeHfHge9hTMNLHRmxeRldNMCrYPpru7shmOg2sTKWGpW81EyfNB7Io-KGbI6Qsq-eM9ii5MdtybN7Y-7pJXiBKPVOHUwQzVn3A95RlfJAAQpkjX8WIsxYhxI3B8wTLO6O0YYUH7iapvJp_4A1m1xs244idHkuN1-Dcljjm2etQkjInFqLawuA4gf_QKm7qHfKiwG53CeCnywtWj28N8dOosuGHxqetEiDLcAHCVNPbWMVkdi-QirxnJ1JJHmFRZUTiACGLwb9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effa95670e.mp4?token=AH7KgAclnv-mv7DDYjeLIa_zYjadkC7PMOVCgCeeGuc4J_FgoaU9cVIBwftl1prZkV7GePyohedLeHfHge9hTMNLHRmxeRldNMCrYPpru7shmOg2sTKWGpW81EyfNB7Io-KGbI6Qsq-eM9ii5MdtybN7Y-7pJXiBKPVOHUwQzVn3A95RlfJAAQpkjX8WIsxYhxI3B8wTLO6O0YYUH7iapvJp_4A1m1xs244idHkuN1-Dcljjm2etQkjInFqLawuA4gf_QKm7qHfKiwG53CeCnywtWj28N8dOosuGHxqetEiDLcAHCVNPbWMVkdi-QirxnJ1JJHmFRZUTiACGLwb9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نروژ رقیب خودش در یک چهارم نهایی رو شناخت: انگلیس!
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98546" target="_blank">📅 12:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=RS1j3UE-45IqWmLGaU5MaGfCHUgY6gujkvddmFJ26X5NOWLa31QPDAGcn8FY-coRYTXqlZrwPNyZZ_mVbivv0fNo6Ab_-HvufGqTWZlVLcgImvqx6sUJjtkxkHhyea-6dGox7a5CfR-PBNY8JS8myMofb7PM4BLskK_iShucKVPCLwqcGfW0WI25h4Sde373Y7-oQjVL1mENrwLsPOOXVTulPiG0VClvq-p9Rj_Mc3m2gPx6KGq69jbOkJe4SyiwtefLH0OeLsuUb7RVMt5C6aLMYZRb-zT5ICvzOF8LyUG8tfnJ0wKocdptnY1Uji8ulVgenbPX7grQslG33f1k4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=RS1j3UE-45IqWmLGaU5MaGfCHUgY6gujkvddmFJ26X5NOWLa31QPDAGcn8FY-coRYTXqlZrwPNyZZ_mVbivv0fNo6Ab_-HvufGqTWZlVLcgImvqx6sUJjtkxkHhyea-6dGox7a5CfR-PBNY8JS8myMofb7PM4BLskK_iShucKVPCLwqcGfW0WI25h4Sde373Y7-oQjVL1mENrwLsPOOXVTulPiG0VClvq-p9Rj_Mc3m2gPx6KGq69jbOkJe4SyiwtefLH0OeLsuUb7RVMt5C6aLMYZRb-zT5ICvzOF8LyUG8tfnJ0wKocdptnY1Uji8ulVgenbPX7grQslG33f1k4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
خلاصه که هیچ‌مهاجمی نمیتونه مثل رونالدو اورجینال باشه و گلر رو دریبل بزنه. اندریک و بقیه تازه انگشت کوچیکه اسطوره برزیل هم نمیشن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98545" target="_blank">📅 11:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlDSuqrMBADR5zL11YqDBD1VJd04i8t8lRTNS4lHt_k5MWfh6obesnQgGnkr069eBEUktdcijhELIXSFWICzWnJJ3mfqiRaYoNzMOlST0H9rH5yQdF5HKRQUj8fqGh-X0XQ-vYwspIZm3uxRaYoil2Qa6MjyB4asp_pwJCJ8-UBD9C36EQ_z_3qabe4xEnjv7TiPxkQTmhA8aYYa42oCXbU4sVvdo5_ANndA9NjrFTQad7uth2RQsfcU0atgCIPNZiAgmfUUku05gds1O1mxnPYAgjbjay2g5iTVQTv8YsZDnSGIuroVxXPsEgaivSpnPcMvAGy06GdrqR9pinWXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇧🇪
بیانیه فدراسیون فوتبال بلژیک: لغو کارت قرمز بازیکن تیم‌ملی آمریکا در آستانه بازی امشب نمونه واضح از نقض آشکار بازی جوانمردانه و دخالت قدرت‌های سیاسی و نفوذ در فیفا است. شدیدا این تصمیم را محکوم کرده و پیگیری این مسئله را ادامه می‌دهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98544" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f91878075.mp4?token=TXS8XUy-tRawyKgM5mWJDrBwMgtf3iJct89EPqv2onfrKkRVoCajnIKenMEVX0JKmoJOZQIJX7AB4N1oEr0yYo3tc0we3IsEuf49C-Wpqx7hGD1YBaMoRZjRiBbxbJP35DuRnFplZq6R2ocMrnjBHIWpqDG901h9cAaMWK0oO4TIq7mo0jCTX958wWf6a7yiY_r8EY3DOoJmpCsChSgyMDUGtxa7ea9MCbU2N3ek6d9fZA6Auen5mFGG_3jToQTDw5AeisMpJBw2mqSoE7wgC1M_ACCBkuLwKM-3BJeOIGOsEm-f9gXtOiWu6ir_Gjrd-KIqu2piG8EW6OnMWma4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f91878075.mp4?token=TXS8XUy-tRawyKgM5mWJDrBwMgtf3iJct89EPqv2onfrKkRVoCajnIKenMEVX0JKmoJOZQIJX7AB4N1oEr0yYo3tc0we3IsEuf49C-Wpqx7hGD1YBaMoRZjRiBbxbJP35DuRnFplZq6R2ocMrnjBHIWpqDG901h9cAaMWK0oO4TIq7mo0jCTX958wWf6a7yiY_r8EY3DOoJmpCsChSgyMDUGtxa7ea9MCbU2N3ek6d9fZA6Auen5mFGG_3jToQTDw5AeisMpJBw2mqSoE7wgC1M_ACCBkuLwKM-3BJeOIGOsEm-f9gXtOiWu6ir_Gjrd-KIqu2piG8EW6OnMWma4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🙂
خلاصه اتفاقات دو روز اخیر جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98543" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=jTg2-WtOwD13ld4ba6oTLPKM2-Lbp-esFnhbkFiQoXBmGR_ZGM3iEbRfh2Na92aYZRwT_Ip_GtFHW0y6RZG7f7mdg6AWMqpEcgd-Rhni1SkAVpRC7W4tXrNkUz-ujOp0yUD7nh3-Z1WryxoAqknviCXz_44Yad6Tc1ikKnTDIbe72T-C0nIeFzpUGvEQU_pxojHvCR1Cyvwow3aY7R4fL_uJ-d3HXwb9lsIzxGdra-Cn87xeiXMlEkjtK-nI0no62JQS8E3SimMtv9yJWbbnDS8LvXdiQT6PQK-UG4UuFhmQtjscHpLzGlXrl6HYxeuAThamLpDqksulhTdZrM5NpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=jTg2-WtOwD13ld4ba6oTLPKM2-Lbp-esFnhbkFiQoXBmGR_ZGM3iEbRfh2Na92aYZRwT_Ip_GtFHW0y6RZG7f7mdg6AWMqpEcgd-Rhni1SkAVpRC7W4tXrNkUz-ujOp0yUD7nh3-Z1WryxoAqknviCXz_44Yad6Tc1ikKnTDIbe72T-C0nIeFzpUGvEQU_pxojHvCR1Cyvwow3aY7R4fL_uJ-d3HXwb9lsIzxGdra-Cn87xeiXMlEkjtK-nI0no62JQS8E3SimMtv9yJWbbnDS8LvXdiQT6PQK-UG4UuFhmQtjscHpLzGlXrl6HYxeuAThamLpDqksulhTdZrM5NpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
پشت صحنه‌ حماسه‌ای که دیشب اساتید فیفا در بخشش بازیکن آمریکا رقم زدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98542" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=jKB1VdOpj_NMPO98UJLcyWMmdyDi5zFuu0xufHtnBugjYdPATGzctEtX9W-ZaTjXSIxsyKknQsM9hZCx-2xOug_jihK4B6KqE8uzm_gf02TscwGqksuwGNwWxdcT8dF6NI4QGI6eciB0VcPaSFYqLzoWyiD_fEMz5q0rMn3kCx8ADSTpeX8zB-hXYwur4yQkvL-yH-vfKxxGT7kA2ZwDL9fHI4Fc8kCJd5rqY0emJ51QcqXbjye-QGL23cyfE9M_Cwjh2tK6OledLKUkFnGcOTCuOLHFXBEksnL5oTEyAC5iRUzMMCDGydFZWdY9TdOoidE7uPDwMBdj6ijHj-2svQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=jKB1VdOpj_NMPO98UJLcyWMmdyDi5zFuu0xufHtnBugjYdPATGzctEtX9W-ZaTjXSIxsyKknQsM9hZCx-2xOug_jihK4B6KqE8uzm_gf02TscwGqksuwGNwWxdcT8dF6NI4QGI6eciB0VcPaSFYqLzoWyiD_fEMz5q0rMn3kCx8ADSTpeX8zB-hXYwur4yQkvL-yH-vfKxxGT7kA2ZwDL9fHI4Fc8kCJd5rqY0emJ51QcqXbjye-QGL23cyfE9M_Cwjh2tK6OledLKUkFnGcOTCuOLHFXBEksnL5oTEyAC5iRUzMMCDGydFZWdY9TdOoidE7uPDwMBdj6ijHj-2svQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇧🇷
توصیف‌های عادل‌فردوسی‌پور از نیمار...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98541" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f587817b79.mp4?token=RTQTtt4EvibwzbHHiaCEOa3pKqJbSrPPD0j8levbXwN4xI5QscJ1AlPcvEC8Vboq1icngL3_w2mj4FnmWtkaLs7SKr9T9F9R9O85N_PIdEhsBtW6JWiSSNRdMKw_WAdbB6Fz7TdWp4bYd_Aa35fGJf6_wcyvbWTZ6iMGX0h8A349XKSu_kslLpxrRZR0GIh2requbXgSRYt6xHX-nJrhiq94eNmAAnLMS3tOeHi3ZBt0NmYkwhQrHb2a-s8N-b-CoBP4eIqL5vGdJ-MsGnxNmOtgnFtOPZSDbPv-T05uwznHw_dmLw4VZg7Kw3_yTqcFVJPePOEqzjx_21RagLyuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f587817b79.mp4?token=RTQTtt4EvibwzbHHiaCEOa3pKqJbSrPPD0j8levbXwN4xI5QscJ1AlPcvEC8Vboq1icngL3_w2mj4FnmWtkaLs7SKr9T9F9R9O85N_PIdEhsBtW6JWiSSNRdMKw_WAdbB6Fz7TdWp4bYd_Aa35fGJf6_wcyvbWTZ6iMGX0h8A349XKSu_kslLpxrRZR0GIh2requbXgSRYt6xHX-nJrhiq94eNmAAnLMS3tOeHi3ZBt0NmYkwhQrHb2a-s8N-b-CoBP4eIqL5vGdJ-MsGnxNmOtgnFtOPZSDbPv-T05uwznHw_dmLw4VZg7Kw3_yTqcFVJPePOEqzjx_21RagLyuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇴
خانواده سلطنتی نروژ دیشب بعد بازی با برزیل برای تقدیر از بازیکنان کشورشون وارد رختکن شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98540" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=PXkn2bREbhku_kwVxIcLqZUjicyDZVbLEDlFRDJFTR3hSf5cay3GewX3_7PdbIA1_CHZXoxMtBByMN-A6-W97Gup_986zF-OrAQ4ogfGv1BYWWSdUhEzgqwef82-BxyjL6KwaQRmk4ON936F5OoL4JteX-5u__1KIDevskYuhNw1NKWcuFAmuKRtmZV_HsCe5QiRkz1v6lUdBzEH_m3AEQwJoGP8KZXeNXs-S22gSzgsrsJmlGaWW5_FYW2K6_voa0DGTwDhK2s9Gp9QxaR3p2pXnoK7EXsD1yETDHlCflBeumeN0vmXqM-J8zDg-hlCiHQXbqrtMfXXkc4S-4qz8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=PXkn2bREbhku_kwVxIcLqZUjicyDZVbLEDlFRDJFTR3hSf5cay3GewX3_7PdbIA1_CHZXoxMtBByMN-A6-W97Gup_986zF-OrAQ4ogfGv1BYWWSdUhEzgqwef82-BxyjL6KwaQRmk4ON936F5OoL4JteX-5u__1KIDevskYuhNw1NKWcuFAmuKRtmZV_HsCe5QiRkz1v6lUdBzEH_m3AEQwJoGP8KZXeNXs-S22gSzgsrsJmlGaWW5_FYW2K6_voa0DGTwDhK2s9Gp9QxaR3p2pXnoK7EXsD1yETDHlCflBeumeN0vmXqM-J8zDg-hlCiHQXbqrtMfXXkc4S-4qz8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف برزیل از جام جهانی به دست نروژ.
🇳🇴
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98539" target="_blank">📅 10:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=twTEFQjioGmSuNmPBMyw9pmP1rkVu_dGqdKUlT8gnHvbUIStS6rhZmiSFqQ1JFZO2NkN1UzQfMAAxjOm1R7J9RNGujRcdWmFKIC8nMIpKsBpdnoDL14IxjD2TW3-5Rk1dmikDlK1bXb3G4G6VK8pSXMdLGbhfkzjvIiS7L-P1-Vah02Du6hDniVrlvJvH-TFDeu8jvTDT-Hd_7EfHq4N2hC8aN2bidtukRVBZZhbO88mFJev1FU8qcvlSfcO2YxRKGLjTUodMEXrBSN_gMGj77rW_xAZXldFfEaaz1zxd7lWcSITG3tiXbvMUuSi482mMvSKpSZI4wm5RcVCwB-Vh1xowPeMwabwJVzdrHBkbdus68BNVm6fcUm5DmnoOwqhAeKkOfDjRFRs48KV-0nfq3L-XiijffX1oUd91MQ_kKcPKorvxpJgX8J55f-A5Qjm4iRv6Wl7ekbYPnr89-7f7W-XsFxzH6RFAQWk1V85lTSLy7BbEELmBbKKQCBw8mihigG5lYehouT4L1XF6FvEf7AusBh5o7Ey1TzScQ87blPvtSAWpiXlinNsL9pnzsK0pASqlZmvoLUyQtp6X7B7KKam9EprRAIORIWWkD5Y9bV9Jnlv0NqXsXUo3TXsvPSv5w7FB_nW80xcOVzzUxQj29uM_2Gqdum-vF78Yw4GFnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=twTEFQjioGmSuNmPBMyw9pmP1rkVu_dGqdKUlT8gnHvbUIStS6rhZmiSFqQ1JFZO2NkN1UzQfMAAxjOm1R7J9RNGujRcdWmFKIC8nMIpKsBpdnoDL14IxjD2TW3-5Rk1dmikDlK1bXb3G4G6VK8pSXMdLGbhfkzjvIiS7L-P1-Vah02Du6hDniVrlvJvH-TFDeu8jvTDT-Hd_7EfHq4N2hC8aN2bidtukRVBZZhbO88mFJev1FU8qcvlSfcO2YxRKGLjTUodMEXrBSN_gMGj77rW_xAZXldFfEaaz1zxd7lWcSITG3tiXbvMUuSi482mMvSKpSZI4wm5RcVCwB-Vh1xowPeMwabwJVzdrHBkbdus68BNVm6fcUm5DmnoOwqhAeKkOfDjRFRs48KV-0nfq3L-XiijffX1oUd91MQ_kKcPKorvxpJgX8J55f-A5Qjm4iRv6Wl7ekbYPnr89-7f7W-XsFxzH6RFAQWk1V85lTSLy7BbEELmBbKKQCBw8mihigG5lYehouT4L1XF6FvEf7AusBh5o7Ey1TzScQ87blPvtSAWpiXlinNsL9pnzsK0pASqlZmvoLUyQtp6X7B7KKam9EprRAIORIWWkD5Y9bV9Jnlv0NqXsXUo3TXsvPSv5w7FB_nW80xcOVzzUxQj29uM_2Gqdum-vF78Yw4GFnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
هوادار برزیلی بعد باخت از شدت عصبانیت هیچکی نتونست جلوشو بگیره و تلویزیون رو شکست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98538" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=a-KKGbXJF_JIwgftdeF-o84bZlJ4Xz9GwjXOsG-fmS1051E0aAtXyZweabL-wQ0iAEPnIc7lv6nxP2ThNFQzjWhaHxtZprQIC7ZB9CgfHumn_QkP9KjkcwqRDnuOV5RYWqnx6ln08699yNYZhGvtBil5Ip0IXq2ZWasCEL3syjt32GiJtk0WLf0mMu5ikyul3_kmGTJw_33QDmH8_PI57BHtB61NcsFp7ar0LWYOnY1tB_U4X8UqyH2FLwzVY0zvd1yifbZ3rtdzu1oNrPWH96adAJ8bKMIvrb0UGSAg2W1UP2URywQ1SW7nPOOxmg20ZYBVsNXLPzaDLyVGtJv9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=a-KKGbXJF_JIwgftdeF-o84bZlJ4Xz9GwjXOsG-fmS1051E0aAtXyZweabL-wQ0iAEPnIc7lv6nxP2ThNFQzjWhaHxtZprQIC7ZB9CgfHumn_QkP9KjkcwqRDnuOV5RYWqnx6ln08699yNYZhGvtBil5Ip0IXq2ZWasCEL3syjt32GiJtk0WLf0mMu5ikyul3_kmGTJw_33QDmH8_PI57BHtB61NcsFp7ar0LWYOnY1tB_U4X8UqyH2FLwzVY0zvd1yifbZ3rtdzu1oNrPWH96adAJ8bKMIvrb0UGSAg2W1UP2URywQ1SW7nPOOxmg20ZYBVsNXLPzaDLyVGtJv9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گریه‌های شدید این خانوم برزیلی بعد بازی دیشب و حذف از جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98537" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=dlUyoYbIumTvy0SaVmeyKBnDOhUGJuYGjMeBjTBfkLCUkXSiLAYgICtm6MmxubyhzFmKRoy2MALETl0agKI9ulaqAJVAaG0fVtDuTtyCeoO-A79keIqkCiDBXRU6ZWMJCgSnQQgVDrDB_kCnq4AVUt1s5hiVoDOU29RcW6kgKLH_i8OkCfnRhEYGpFDQRxsNSNkSP727-YxnNmxeOxW_LvLdq8bRWE1Ic9J2ti4L5ZXi82nS5vg0yhUXV2nQscfRnDbMQ8zjG67uQfoWgSTqzvFCZpm6MqEGEuR-CQHM68VwbqPRoxRvrskMJlbQX0qSvQFYxG48JcpnNcyfaoc9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=dlUyoYbIumTvy0SaVmeyKBnDOhUGJuYGjMeBjTBfkLCUkXSiLAYgICtm6MmxubyhzFmKRoy2MALETl0agKI9ulaqAJVAaG0fVtDuTtyCeoO-A79keIqkCiDBXRU6ZWMJCgSnQQgVDrDB_kCnq4AVUt1s5hiVoDOU29RcW6kgKLH_i8OkCfnRhEYGpFDQRxsNSNkSP727-YxnNmxeOxW_LvLdq8bRWE1Ic9J2ti4L5ZXi82nS5vg0yhUXV2nQscfRnDbMQ8zjG67uQfoWgSTqzvFCZpm6MqEGEuR-CQHM68VwbqPRoxRvrskMJlbQX0qSvQFYxG48JcpnNcyfaoc9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
حسادت عادل فردوسی‌پور از وضعیت مردم کشور نروژ که در رفاه کامل هستند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98536" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap39wv5sTn5sSavHNNTB3u_Q_HZTbAZ3RNSCJeuQ4qQajpY5zvfGq9RkOIe6X2VC7KcDVKPR_lPBMysqf6qKsTjt3rCnQhPyz9jBRpm8ELZSzaFsOV-tnipwjpMYkZqMkN1473dTh4ZSc2_2rXSaTJWNhgqHgJOofr_qH15C1ao42eiQaClH2cBdrq2pDFpjty-zoZ_mJ-afQqOUdSnpSLAtrTZgCdIkudqBHd9cBGSwkBuz-uNG6fLZ5HozoH1U4HT45ll6x_qCyfX2tzQDYzfuZtbUG5mOVbn6QzZb7x6wOm-HlI84KSD-I4WDZRrr41F9GK5Qd1qEls2sMwdWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون پخت و پز همیشگی
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98535" target="_blank">📅 07:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZmONiu9Yf2CVmUrqq1K5sqD0McwELbisBxh_q0PHyQMOcUEP5Q3DCNgTupyAqDE5juFGVj3MsroM7zJc-huej9IxAexJOljpuCJBXHzAR8u034bXdEBFLtLlajPguGZAqFtdwncYyNjVMciDf4o0LlGSt-ZUsPvZfg3rhJBc5rrmqsUWuc1oV7mmL9KGcKnQl9YLQ0l2ShqCZ-nbeuB6ckQYQQTWhne2bS0Le3f3-zBDYXXtam_MFj8x6cSkkT4Uzg8Y32upVx2t0SH3R1tAXOiyp9FRrGzqOkvPoRJy_VdBFup4993K6YDDmyLHqBADmmehgfeplAPMZeq4EDcnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس در جام جهانی 2026، یازده گل زده که ده گلش رو این زوج فوق‌العاده به ثمر رسوندن
🔥
🪄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98534" target="_blank">📅 07:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4010363319.mp4?token=tE2oWYqkJAYRgWtho-kb5Y4EREIlaOwMSMCdEYTT9SUDXvmdGV4ocyM-QVfj6Q-dTYJODmSsO2Thd1-2RrHKVEUNyHywwgMsSmy65MkDSQDysb7MJsyMRKnoUxfbQ8W8RHacBoiYqxJMOrubBt2bJrKVCQ0QJbh8YU3YrGan6hR6mRucEZEiRM6eY3SK_BEFaRDgiePYq69JcUQsk8uOieU4_xWtbKNddYa8iMUbJYC4ir3cA_Cu_o4QACOXkF2LsvOZUDxxzljIXTGz5QNopBikLG0XH26XnfqT139GgDxx860NtmYISj2ZCoz-m3-Ap-Oaw-jnQf-Xs3aqyYxliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4010363319.mp4?token=tE2oWYqkJAYRgWtho-kb5Y4EREIlaOwMSMCdEYTT9SUDXvmdGV4ocyM-QVfj6Q-dTYJODmSsO2Thd1-2RrHKVEUNyHywwgMsSmy65MkDSQDysb7MJsyMRKnoUxfbQ8W8RHacBoiYqxJMOrubBt2bJrKVCQ0QJbh8YU3YrGan6hR6mRucEZEiRM6eY3SK_BEFaRDgiePYq69JcUQsk8uOieU4_xWtbKNddYa8iMUbJYC4ir3cA_Cu_o4QACOXkF2LsvOZUDxxzljIXTGz5QNopBikLG0XH26XnfqT139GgDxx860NtmYISj2ZCoz-m3-Ap-Oaw-jnQf-Xs3aqyYxliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98533" target="_blank">📅 07:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsD1ZVQuDr-RUoke6kbrfcmBTl1RzLR2_NaOikbRe3-pX7l44LElbV5XMuS5jXcE1qO8FACznbROykBsGm2uB8HeOOV_NU7E0PENweLv4ysqhgY_mCb02Sbv8zGNxV23IvJTZVUs1OsuDqQoknTFK-tHqiBsU0640SN_g75BjpBICM7VQJ8yTHCpVJnoemJo081XLt6w-N47BWJTFbLl-ApTF-Hb_bjkOADukd6FkhNOoPQPAUWF_h6blrcMugZ_NzBBHgTrCExT_KtcHmSwKHvh1fD7xSMLWfym2dm5q-W9Geo1tFPbuqQ06_mYhpYhCxqQLbCUzKMiZb4QMaA5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جردن هندرسون هم تو حین خوشحالی بعد از صعود انگلیس مصدوم شد و با برانکارد از زمین رفت بیرون
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98532" target="_blank">📅 07:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ffd81e61.mp4?token=IogLxJCS0h2-gznXQ4S0doXHK6egXDwjisXo7JoqZujpadwocNID3EiCEZc3WtqPm8twv1UKUq8ZtSY92vjxf9Z0O1NocR3Dm6SnGfx-8Lskxtgu2sHESV2fQ-Cqf1A8qvEWwYMY1IpnY2bqFdHystJjBCRE4-UxN5ZEE-EIHI3hPMS82MA2cDxE3YtgcYdBnD55u9Cd2s3T_JDgyU3oJFsK1s0BTpKvcDGvPxw0vRgDnEY22_kH_68b3bXukKX6GNnx8pE-patP5y4zPXo_GXn_Qoz6yP0usYrSD9T4G91h5qrc1LxFBlurrPWMUWItxyxOTxS7YtqprF1hJJikqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صدای هری کین بعد بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98531" target="_blank">📅 07:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhnO2Uh9djf9aLMfe7ErUVp8ixNP63YcdM2Kcjo_XJ4P9dP7AmrBVdK3yAQR7Vu7qs7xWW783Syq0wW_nUnNzjSLEvhcfK9joVzYUqrOPF0-DyxOkRzi10CvYF5ssMG5EY9ICZqH53uQusnzPUE49yLbabwCdMvxzw3mBZsu_k6qgT38oFMo8VzLnqE9vNqhFlt79CFFJdTKOMPELfIPikPII_umTu_KmZvVQd8XGRAMJphsG-bIjO6ql9wxPnqrk6kz27oYSsUhjN1t1ExLV52SlJOkwgorerF825M2tbg4K92wjuSPLf-NidfoHNpXmXdExCF805BNFxTtM24AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ۱۹۶۶ سابقه نداشت تو جام‌جهانی یک بازیکن هم پنالتی گل کنه هم پنالتی بده به حریف. پرینس هری یه پاس گل هم داد و همه‌کار کرد تقریبا برای خود و غیرخودی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98530" target="_blank">📅 07:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rXQV75fEfROjT6MfyRkwKTuUfaLwu_JUwSSyF6qeTefA9ZoulmldsqU-c00JLN_6dakJfl9fbNm7HKkEJSsugKqs-6Bw6_EHxzai5PY8Sg0d_UW98vMAC-GYODAPtJ6M_beVhWQZ6myKM0JhKtCzi2HpirLP2tN869EWiQsRJrGPTZJVpNtpHtH_B_gK4tnVBJVfpGGHcbfsJrzuMzQPJNxmmuu-ToarlGAm55b6WSORQRYNG6wLx-Q3HkirbeMJd0PoqmXw4owRxK4JRqUVg8dIcnoKSZbOj4rls9K74igVDVJ8WXZMVkvSeWYyiCUVUeIpBZOhrIw7UC1xd_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دونالد ترامپ در اپلیکیشن تروث:
🔻
‏هری کین، بازیکن انگلیس، یک بازیکن فوق‌العاده و بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98529" target="_blank">📅 06:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sunOhVr0-69f_nFiWhxiwz5AyYAXvSBACcogkbj81r1PgDeKJo1sfwmLvwAVIgmTF_DIHRxuMM3kkJBzvY1xQPP98wmU9zQ4bVIzlSrOVt5G6--ZfSEfH-8hFTkV1u4scSfLyd0o_XBAQqvKDFbbanBQgbB3YQieDvYl4niUTaMitqscAN5aeDIc9p7OUdC1ggapXHN9RT7n_rxYOvBLh4Ik2diQsqD7KpC0Pcrwn4wjnONh7s_GX82RREuRwRqPOVXXXDBT9Ukvjrd55-X43w1JZBdrChiwXiTjXhA6a6NIfHjNBWLAEDOw9HPRtwKON18mvfEk75MS2gMt2k0p6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
دقیقه 36: انگلیس 1 - 0 مکزیک.
🔸
دقیقه 38: انگلیس 2 - 0 مکزیک.
🔸
دقیقه 42: انگلیس 2 - 1 مکزیک.
🔸
دقیقه 53: اخراج کوانسا.
🔸
دقیقه 59: پنالتی برای انگلیس.
🔸
دقیقه 60: انگلیس 3 - 1 مکزیک.
🔸
دقیقه 67: پنالتی برای مکزیک.
🔸
دقیقه 69: انگلیس 3 - 2 مکزیک.
👀
‼️
یک دقیقه سکوت برای کسایی که بازی انگلیس - مکزیک رو ندیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98528" target="_blank">📅 06:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YONJhCJoXmsddesSfAKJlccGXVtsYLnG9oLWzNcQNKYMN2ehsDeU3evfI_ar9nUSj7xWJRqwRhDGI1AjhgtEYw_NcbQMMRKVTBgGRygHdvfJ8pL8uZFvW7MLof4le15MTYQCtisz0ht_KimCn2ge22NPwGb7ajpnzUxW15XXtnsT9L21jM5WUXZNBIBdZByQkhpeyjhSgz5fhurrQNHyCDKLj-ZEE6PD8nlx2xp6L-RsRbXb9zr-nlLHkJZasnQEn-1QvR9rEzg3N6VY_7o4GteiKu6YbvUS1wXpLS8ZKBLEbnkAogbMP7UmGEE4wsCsKsN9l9bBzUNbZs-5sIhYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XI9g5nl8PERz3cOl6sL35NnnE7pNwLFEQz1FuCUW3wO6b9C_7cinkBipj4thFLnuvaAYH-LSa0isDvc61cn4XBJRLlSIVjbRRdpBqHt1gY3z3lioFvPYxsRi6fUlM_3h96jkOrmazBtGWiQMrwJhUmqWQNLphCNbFdkmeqS9-1kSadxSncWHnwfv4l-D37zNtn03fDSXkoxh5y8N5zZsaSX_QopiZGRaJECJQJseos9OOBobM8Yx3Fot8lGAOJk9jhiwdl09hxV_gGcidFEdY11-H4Dm3xFFg4FrcFjjbj1i6S33WAxNMx-pA8_rxu7eG7TLx7uqVvtNpfFQpEeG8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوچوای افسانه ای هم از بازیای ملی خداحافظی کرد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98526" target="_blank">📅 06:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtE-H_Wa3C8NHodV2TJH39pECpQ4EH6nBymMl44bWVwzogwtUv9PDToQLYyjHUPJ920Xp3B6HX-RmdmLYRsfcFGyRwvNLR69OPygMctR6k_GG0zuNt7kDwYS2WVJwJtUB_pHptTTMjVmHEM0zD-kXEcviU3_R1esUW7It_eAJHezDjROOaUFU_InXbfObsVPcqFiItlBWgZn7kSpCi07Tt805KrVzrJyoxWufRKB0-s_57GB9yL3il-0Cbq1dCC1MrIb69Ud2yDebGZwlAX9bdGeHyqrNyFyPYX0C_fXr_jxqmy-SIbg-9el2xlsGm89eGrKXyn5AbxdAh3vwdHQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
هری کین در این فصل در تمام رقابت‌ها،
73
گل به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98525" target="_blank">📅 06:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEiLyBYej_83iZtqsSb4VRXmDLfTmxtCtsiK0co_Pfd0GvDGnFID4FGvPXpSQ0ints47JBA2uWKCW7XKBbq8jUN3AgzSFtE710kF4VvBdOGqTsqu3qJ1ElgyHDJqpLNnIPJxqwBULrobFGNZABMGNSOvPDeBuEkhnrSRp_Usxdq-nSIb7HOd6q_0YbmrU3xWWs4mC5tXzdO5GS-i3kfqxiZL64HajnzPUi8hIIWkKJvFL9GX5Y7g4YtZeWSk-rVHeyc8ezmuHhA4IlWchb7b15VzUI1e1a2tcrRAQyZ1vG6g0il0nbkfer-K9H2cmS5ObUmrn6V4AoXUQ3saUkekLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
واقعا مکزیک با این آمار هیچ‌جوره لایق حذف از جام جهانی نبود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98524" target="_blank">📅 06:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ-B43WVwvs9M3U9mf14sfzHTqKFcbpNYyX5Rs_3mdefsxULSPvOfYrfSX5har5UT85JnUt8cX5zoFJIJWGI_uFxlJLwXb7iAS7Z6UVccl-qZwUDK2l79Ve8jt5mkQLri3cO1_Pglu_PB3Upz6rh0ur5cBp2Ju9H7gj3BNsiYQhmeT10zx_GbBZuEMF8LgDsVdg1olcFfirVuUax4wQt_Yfm2FrIgMWjerxpVbC3oVwdTgKlSc7p_E_eTJRExuQcnjxj6mI2GqqpzQdDdDjQZ1zRyUWqoU45JsZ943aZhpxTHkXVQoC_ngGthbLda57paljloU-A_OD-IEQg7NdOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇳🇴
نروژ - انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📆
یکشنبه 21 تیر ساعت 00:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98523" target="_blank">📅 06:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz6uHNJSeFXP2NrmlwyVmF1OTWrNhKSyFCnXXQUePDDmps1ELvqPd9AaLtGvCGeH3HQE5FOXqLr7lrtPLz2g08aYjRl_S1vmoUL5ro-af1Yn7KUFLLgl6MvFu6KdwmhfSlac1lQ5VKuhAr_5XJNDST9AZ_pfltEo0_eakoOulXsL5QyCm4FyeK2rkapwJBq32yT-6kvMxk-OHlB3g6JIzLH1Hc5njsFqbTIl4zLjBPFbTveJt0EBII8h6U5dv2TnC1Lh7oIRowp3YY7_OleW_rOF0nVkuKqIqTi4alclOGDuWhB8sU9fs8r7A4tkjGaowD4XDL1q2smny6rhD2T8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98522" target="_blank">📅 06:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikOVcuBDHQ-RcPAltV2sNHeXrxkwyVbCfPyVqnyZ8j6RRNuEaYcxfOv6YJGgiNJYzjhG2r3bUVxwLiqOv2ZdSCA94DfO2fKI07H6zKE7oEbVinY7l2i6DhpuSWZIctKSF3DXPnUBKJcetES90vXDUfbq2QJOViycypPgvA92TQpCmgGoIb64xFeiUmTUUTUvnPLxVt3-pFRnwvF3-YNHVyE-4xerymd2LMVvZd8E0Q51kigI01gaiO8irdRfNj1W8ACoSDzH6vomx4cw7R7q4kduDEnknrACrW-v0pPqYkMqMMN988b4U27SQ_nEV877_2mj3c92mjIjp3meEf92NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد انگلیس ۱۰ نفره مقابل مکزیک در جنگ فراموش‌نشدنی آزتکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
3️⃣
-
2️⃣
مکزیک
🇲🇽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98521" target="_blank">📅 06:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">11 دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98520" target="_blank">📅 06:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98519" target="_blank">📅 06:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حیفه این مکزیک حذف شه از جام جهانی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98518" target="_blank">📅 06:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98517">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihCkpT3f5dt0XI-F1oQ-FY2dg5db2WTfAz8y_qjwv4HU16DU2UBOMnjN7OXf3X353G-42CQjpTz9rzZacPFU8DX17GFjpNsmlV70tpfEl1xlVsKqTlNqrPOARRi8ErmyGD9iDgqLX7KsUDFmBTh6wegumLKVef1aEv97lhNjEX2a_XCgnxDU9HmMEbSyXMyuuKH2LGANfIo-DFTNJrBKJD6K7O0X9awJhqyhTodfW2cQE0QFhIzORV3Uq-MX9YsGuiTn3I0iJGQntGkADAN_sPUsSZuMbrS8GJwnY-ofg0PIRlHTBFaIBMhrOQ58tivq1g3L79REfaH5tOEXoPT4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی تو بازی انگلیس - مکزیک:
⚪️
اخراج کوانسا بازیکن انگلیس
⚪️
گرفتن پنالتی برای انگلیس
⚪️
گرفتن پنالتی برای مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98517" target="_blank">📅 06:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98516">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=V5n1uBHBLWXl7kIbi5KwY4BPTbNi7VDVMHwkCoAT0eYBWbUk2MLPcyCPrlOC6la0eoAU98tYcmLCDmCsp0WiCpwXc-T0XMJ1wlYEGT0TlGYA4LFvwGWVbwGdsT424qrWR9GKkVroiQVzo-VyFpKozXR8z-QuGp12u86CuUHhQAgDhmP7sh0lIYKqcvZEC5NhGVKE-4knYGdNMV27MkTtjUb1sTFG1fQedblG64NCA7p5jrhS4zPEO0c0x2fUyf6l358jO3yk07APHUnbJbpAGsTfcAhD0JCU9uksPcIM34O4UUW5kVLuLOogIq9a4vYxrrqnj5UqcdsSDCWO2FH9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dfb50be7.mp4?token=V5n1uBHBLWXl7kIbi5KwY4BPTbNi7VDVMHwkCoAT0eYBWbUk2MLPcyCPrlOC6la0eoAU98tYcmLCDmCsp0WiCpwXc-T0XMJ1wlYEGT0TlGYA4LFvwGWVbwGdsT424qrWR9GKkVroiQVzo-VyFpKozXR8z-QuGp12u86CuUHhQAgDhmP7sh0lIYKqcvZEC5NhGVKE-4knYGdNMV27MkTtjUb1sTFG1fQedblG64NCA7p5jrhS4zPEO0c0x2fUyf6l358jO3yk07APHUnbJbpAGsTfcAhD0JCU9uksPcIM34O4UUW5kVLuLOogIq9a4vYxrrqnj5UqcdsSDCWO2FH9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🔥
گل دوم مکزیک به انگلیس توسط خیمنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98516" target="_blank">📅 06:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98515">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فغانی رو بنازم
🔥</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98515" target="_blank">📅 06:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98514">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه فوتبالیه ولیییی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98514" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">3-2</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98513" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلللللللل برای مکزیک
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98512" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کین کارت زرد گرفت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98511" target="_blank">📅 06:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98510">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رائول خیمنز پشت توپ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98510" target="_blank">📅 06:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98509">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98509" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پنالتییییییییییی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98508" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چه سوپری شده این بازی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98507" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وار داره پنالتی برا مکزیکو چک میکنه
🔥
🔥</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98506" target="_blank">📅 05:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فغانی اصلا تحت فشار قرار نمیگیره و شدیدا به بازی مسلطه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98505" target="_blank">📅 05:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=VmvFh1CDpae29aNNGWiFSM6Y4zKVKZ5LriRCZl3UnZSKsp1zhgIZi4eF1s1KrjlHe6OulkUFxdRe0OGUgzR_EahBn-i76FEUJBbkxoazg5cYa4QQ2kQdo5StMbu38DHAvNN4UiiKlMKOg0gu1G6Xe2fVcw9pgpGdQ-4sM2G_4BZzD5KbnbKmf8K-rn1mrUKgPB2tsyBiVEOmJXsiy-HMtrN_YhMgzLvhavK9IxarHQ20shIm5WpXsH3Bckf3BDXJyi9fv2w7dsOjXa2YYoEFcgVhZY4IHbMLNYh08-3o9dOdg0CWiWqB1rUXK5coVqRGmBQ2NEV0BHTzFgegdOuezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a71da5a.mp4?token=VmvFh1CDpae29aNNGWiFSM6Y4zKVKZ5LriRCZl3UnZSKsp1zhgIZi4eF1s1KrjlHe6OulkUFxdRe0OGUgzR_EahBn-i76FEUJBbkxoazg5cYa4QQ2kQdo5StMbu38DHAvNN4UiiKlMKOg0gu1G6Xe2fVcw9pgpGdQ-4sM2G_4BZzD5KbnbKmf8K-rn1mrUKgPB2tsyBiVEOmJXsiy-HMtrN_YhMgzLvhavK9IxarHQ20shIm5WpXsH3Bckf3BDXJyi9fv2w7dsOjXa2YYoEFcgVhZY4IHbMLNYh08-3o9dOdg0CWiWqB1rUXK5coVqRGmBQ2NEV0BHTzFgegdOuezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللل سوم انگلیس به مکزیک توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98504" target="_blank">📅 05:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلللگلگل سوم کینننن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98503" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کین پشت توپپپپ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98502" target="_blank">📅 05:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98501" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برای انگلیسسسسسسس</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98500" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پنالتییییییییییییی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98499" target="_blank">📅 05:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kntiWOwZc45AdsxpxeKWDpxeALCzAO_a7cXbaYlpBE6csXIbP832wetcDwxJNs8n9bd9qs1VofyXyTLhNZOrAyDdoMpUbySAQsGveptKZF-0Ovd_Fh-mtX3jZ9SpAc0EMi4CevM8dxfPPgQUBkuk04FqFcAbpUi4Kki-bBP29mYpu34-iPJT48BRHYh67UpwyQrtRppmbgxqP0eXOJPc7L2m9RMC4tgqXtTrDz_vpI5dCmzq_Z8I14zH-ZsA0nEPS0r_jk7I795-46vu0y1qSP9GstRdaQmdSDibTdk3riMlgRFLvTltIQMHoVQKJU-YDHW8WP6j3_j-9JR2S7weIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98498" target="_blank">📅 05:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کوانسا از انگلیس اخراج شد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98497" target="_blank">📅 05:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6VTdeDUB1MwrIczB_1AmfKe_JMtUz0DZ7sVL2TkdC-eufX1_kU87VE9bImWQJVectuck8haxMHytPyY2zAzw2XdYqfSoROVw6Dh1-SbTeWMYQklusOWloxyf0IakbB3ILA1rPgpRqh1e7QdI1fBn4qsgwpEUPbQgxs4nCfklw-TCTYkLNawJb27fAFeKk5hHcsPLVmhOLrCepAk846M-9IK4u_4gmmyx1wLtycMN4U-otEjwE09cYEGID14xNJCt0BMGc3sb79C78TA0Yd0qGad3v5nkuh8e8o-benvPcSJKWKNmIFv2MOtTGpoBELS7Trw1QibE2d0zSGFGQXLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با گلایی که مکزیک خورد حالا تیم ملی اسپانیا تنها تیمیه که تو جام‌جهانی 2026 گلی دریافت نکرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98496" target="_blank">📅 05:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بریم برا شروع نیمه دوم
🔥
🔥</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98495" target="_blank">📅 05:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKlV2pnFarGZXIn40UE-kZB3xXC7mpjBL940Hw2N1mGUdjC0JaAzOgF9bcU1Yg8QHHQMx9pJmO1phdLqhoIdmBhoaV-SLlCeN7XWx8KN-kqGD4Bk-2vlQB8SJH8SrS-F7OB2OhMiZA_QojOWGwdv-2lGVEQ1-ebdzF4Te2y3sHVwh_giSBqAKn6uNin396PKcnU-inU2s-_RGEEogZTZz0rlKBMP5YIwKC7-aIyil6bBEyb2aTJZqoXTG1tIWiTWBwH_P5_TNMH5wgVP1qy2bgavc6orHlBLoA46rFSecBldIp5rB_GS1m-o65Q66zLgvuHBkcyLCcFKJCDGdAOwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">19 نوامبر 2026:
توماس توخل، مورگان راجرز را در پست شماره 10 به جود بلینگهام ترجیح می‌دهد. [دیوید اورنشتین]
6 ژولای 2026:
جود بِلینگهام با 4 گل گلزن‌ترین هافبک جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98494" target="_blank">📅 05:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY7N1PKbbNYPYvw99NroHTbrSjrBAOw0SIJ1g0ay38Kvh3NMWWoKcTs8xL4Jd3YGyoIboek3m-EmcQEHOFS2NlU9tCCS1Bh6rFC0i2F1x-n8hkf0DshGT1BEGq_68U9dkSSRny9GyBQYfcxAdT0a6Y4NiGskV7ntvGPTBqLvaORiToOoRq3Wkf0I9gNUhHqkW-DY0p9IsZ919e1B_pfQpGuXOP-kSoUgKB--fidg_R3JwfvX4-oMl6UcUZqmlnlIClBCoXQLoBECBNPSOljw04MUkTz05E6tDUcL76U3Gc7-gCfjAgoqxkwiE0ssnpsLM8QiQyKYs1YIYgDEEBizSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کیلیان امباپه: 7 گل‌زده
🔹
وینیسیوس جونیور: 4 گل زده
🔹
جود بلینگهام: 4 گل زده
🔺
🔻
کل بازیکنان بارسلونا: 4 گل زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98493" target="_blank">📅 05:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmWcb8_VT-HwXm4J2FzCA4EhaalKaFTj3ujomJoGxAo86zSWz3f7IsOLZIhli5ndK2hBxmtUQeuSJvaKloOhAVk53P8R8cZXE0ogXgq3VL4SPGMu-1JBVFP6agb9Ym6kmMU0XMZ0LY_0ov4ZoI68nV5gZvPlDbK5xVReNzJ_6I5fQp3Woxubj0ZBa4tJro6EqWFdDdnbpgA3BspPfi4pf41ZKZemrDMMpcb0aX6Rt5W6z7ro9OK3Pn4waS5wqYnKTRwyk7xhXjU_e3eaZptVivj-gtWQk25UuqMZ5F4G3epWAUpRK7fJ_NcGsIQmuZkEDwjKVlMZfQRzheKUCZGknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس رو هر کاری میکنید نشون لاپورتا ندید که افسرده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98492" target="_blank">📅 05:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4IvrVn9ucFUaxP3u0X3xR9Ujff7KruyiAKnrWqKFKG-hC6uVJ1qvZalTBY3AJBfAkJgj_aEdeB8I7feQi71vYq-dysgXo6hlEr3kjY1ppdKl6hXW_L0PNrz3m0SSBUlno8PwzSUf_CyZ1oTIA_CZP4_aHeXlZy3C82JniQ7U0aGKxhUp7BJspwkeeQNJT9k2xWUOztLI9y31b-g1BiJocj1_CD2Bp8jVm5gKTDmEqeJ3XlGaIDpfRYpHVPBrTpALtCo9efsAqPQR0yy9TAnB3SqrpheLUatoh7i8-uBJZ3cKbWPdhPWFRB4-AlHRIbPWiLAgi7Xwrb9r717Y17XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUUUURRRRRAAAA
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98491" target="_blank">📅 05:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgy4dk7dZGIvPNCDYQfnWkusT9vwxbAB2lAyZcra4jcf9v3cBdEerF0TKhSrD2h82rQH7nNfaQYRJLNXlyRr9pQb-NO3KP1p16DK1JO_TD_Hpfub45o-lxeDcF8AFifiFWYXQ5m0qxdgsI5dlpd8b9Do2owzqq_CtuPdrmybo6zaZgE6PmRwyGlK-DZt7wSqPjjKRlEgkPmRFL_fULbJ7PjPNnaKnU4qTayFywtxeVCOxNdYaE9DZCG8_-ZWextFmngM0ylBZIky3aaq1cDb3D0bpNB0Iup8XICNUaFIxDOMnFPCrABpLLNHERJm3CRt3Xqcfk188g-Zv2J73qZ-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
تو جام جهانی 2026 مکزیک هیچ گلی نخورده بود.
🔺
و اما زمانی که بلینگهام از راه رسید: 2 گل خورده در 100 ثانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98490" target="_blank">📅 05:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیمه اول تموممممم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98489" target="_blank">📅 05:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مکزیک واقعا داره عالی بازی میکنه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98488" target="_blank">📅 05:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=OqfvK10fzUp8-gBSCI_QaDpOI1_JMxrEZop7B5pKv-wvhq6zquy8dnR5KJwKvJ64d3PQ7LdZxZkJJWPXO7Te4HTAhufyZ-GV61LVO7PAYTy8-fRzTG1gQyP_4Psa8suECxWmU51FJ4gfX1gjYdu98uQzO5I8F4jGb5Av-yZOIC6RhDn-qLqkdjWUGJgZVnwre0XLOImnAkbka2aT-1HLp48JtVVICUk6Ym0ROaAS_tRp7-bAlDVUEo0d8gBA8YpP-8Yy-28bso84vBqN39rg1Yj9G3m4JYIJIiP9SmlGHtptEdCDlg-1XxTJ5ciUx0txYpu0fbfo_WCp4DTKE7X7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a5a4ff0.mp4?token=OqfvK10fzUp8-gBSCI_QaDpOI1_JMxrEZop7B5pKv-wvhq6zquy8dnR5KJwKvJ64d3PQ7LdZxZkJJWPXO7Te4HTAhufyZ-GV61LVO7PAYTy8-fRzTG1gQyP_4Psa8suECxWmU51FJ4gfX1gjYdu98uQzO5I8F4jGb5Av-yZOIC6RhDn-qLqkdjWUGJgZVnwre0XLOImnAkbka2aT-1HLp48JtVVICUk6Ym0ROaAS_tRp7-bAlDVUEo0d8gBA8YpP-8Yy-28bso84vBqN39rg1Yj9G3m4JYIJIiP9SmlGHtptEdCDlg-1XxTJ5ciUx0txYpu0fbfo_WCp4DTKE7X7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول مکزیک به انگلیس توسط کوئینونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98487" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کوئینونس با این عملکرد شاهکار داره عربستان بازی میکنه
😐</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98486" target="_blank">📅 05:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو 6 دقیقه 3 تا گل رد و بدل شد
🔥
🔥</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98485" target="_blank">📅 05:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=qQSCToeS8Z4SCVfyrI0glbJiamoQYST3vo8EkwstF6_uS4USOGKoJaMHd9P-h3XRVF1Y8zcjz-G9v-Lqu7tlwa2HVJCU042Kss-gBNAo-oBD3fhIBwrsRZCkW8WLI_8t9-_jKb714vZ7Gw-r-DtnOv_BpnCJsm5GXu3uQYJiW2FNMer04jMtr7L0SYmJ_J2uGlg5FH3SR967189-vt8mQX4rZbYGK7q8Yc3hDstiHY8S6zyZTxA_tV1x_koDFiCX-MmPmhp8zl3XXUfZ7xGK9rYjCJKXe41-lXTY_iDH2QGj41EqxqPaLDXKBTESAXHjQQ31U60WVal-8eEAqmu8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f7a5b566.mp4?token=qQSCToeS8Z4SCVfyrI0glbJiamoQYST3vo8EkwstF6_uS4USOGKoJaMHd9P-h3XRVF1Y8zcjz-G9v-Lqu7tlwa2HVJCU042Kss-gBNAo-oBD3fhIBwrsRZCkW8WLI_8t9-_jKb714vZ7Gw-r-DtnOv_BpnCJsm5GXu3uQYJiW2FNMer04jMtr7L0SYmJ_J2uGlg5FH3SR967189-vt8mQX4rZbYGK7q8Yc3hDstiHY8S6zyZTxA_tV1x_koDFiCX-MmPmhp8zl3XXUfZ7xGK9rYjCJKXe41-lXTY_iDH2QGj41EqxqPaLDXKBTESAXHjQQ31U60WVal-8eEAqmu8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم انگلیسسس توسط بلینگهام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98484" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مکزیک اولییییی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98483" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پشماممممممممم عجب بازی ای</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98482" target="_blank">📅 05:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98481">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=ZXgadtAie6At15hBCi1-oNqjoEf6CXUwVQ8gBkeXO9oBwSLiAObyql_YbqwmFVUK38cWy09t-9D53Rwz3HObqJya_F32PmkCETgAYgiufiu4YpmMxZOTQyzbkOgZNZavph8-PQaBFNDY3HeuMRYTprNXfdsHWfJxuQX0UeFzZdqy2UfS9Bg0vJPS_rWSc3XbltFHpuclA8-rmKHBfYbO9sCvyeO-dSCxEUHeIKTGbgXxJSdic3GRhQuM-ALlEb7GYtkrAwumX8LnbKQqD4S6FFmkqU7cCOeeJFXEWk-HibUYvLsvhIbBoV4Ma9lXqrG9LuZi0qwsWueADJCzQhk2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c97e8c3c.mp4?token=ZXgadtAie6At15hBCi1-oNqjoEf6CXUwVQ8gBkeXO9oBwSLiAObyql_YbqwmFVUK38cWy09t-9D53Rwz3HObqJya_F32PmkCETgAYgiufiu4YpmMxZOTQyzbkOgZNZavph8-PQaBFNDY3HeuMRYTprNXfdsHWfJxuQX0UeFzZdqy2UfS9Bg0vJPS_rWSc3XbltFHpuclA8-rmKHBfYbO9sCvyeO-dSCxEUHeIKTGbgXxJSdic3GRhQuM-ALlEb7GYtkrAwumX8LnbKQqD4S6FFmkqU7cCOeeJFXEWk-HibUYvLsvhIbBoV4Ma9lXqrG9LuZi0qwsWueADJCzQhk2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول انگلیسسس توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98481" target="_blank">📅 05:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98480">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">2 دقیقه 2 گل برای بلینگهام</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98480" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بازم جود</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98479" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98478">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انگلیس گاییید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/98478" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98477">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دومییییییییی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98477" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگلگلگلگللللل
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98476" target="_blank">📅 05:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98475">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بلینگهامممممممممم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98475" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انگلیس
🔥
🔥</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98474" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گللللللللللللللللل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98473" target="_blank">📅 05:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=jcJwDK4-1cHA7RA1Qv8_ZO0Kan6AZWtT4m0lAkO07l0Vh8MD6ayhz-I_NKOOAeIlp45ohEgVtMcYKP5isoNo-ogcNvCLpbHDS1YAa9jwNVdeF97ACroDPUt6xUGD6RFYqoQKp9W11kSOjspfy3f-CWOM1hk1FX3b_XfQxkL5N2INH_XDi09n98K7HjhXrDc4pEij0oxTgpcO9o7TtkdIhdQPW3xge0_vaVxC7LkinBgOFMj4MXF3gfFlzOdd4IRFlJeQU-kl0QbDFPy4R9pOAOBn_VMMrsPwkMXcABspMVIppxElr8GBbf6WDVYUyt6WIuR0-H47kotKkmrFwsMF1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193c4326e8.mp4?token=jcJwDK4-1cHA7RA1Qv8_ZO0Kan6AZWtT4m0lAkO07l0Vh8MD6ayhz-I_NKOOAeIlp45ohEgVtMcYKP5isoNo-ogcNvCLpbHDS1YAa9jwNVdeF97ACroDPUt6xUGD6RFYqoQKp9W11kSOjspfy3f-CWOM1hk1FX3b_XfQxkL5N2INH_XDi09n98K7HjhXrDc4pEij0oxTgpcO9o7TtkdIhdQPW3xge0_vaVxC7LkinBgOFMj4MXF3gfFlzOdd4IRFlJeQU-kl0QbDFPy4R9pOAOBn_VMMrsPwkMXcABspMVIppxElr8GBbf6WDVYUyt6WIuR0-H47kotKkmrFwsMF1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقای هالند خجالت بکش جلوی ملکه آینده کشور به چیزی تنت کن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98472" target="_blank">📅 05:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فغانی برخلاف تانتاشف خیلی سفت و سخت داره تذکر میده به مکزیکیا.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98471" target="_blank">📅 05:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داور بازی هم اقای فغانی عزیز هستن واس هر قدمی که توی زمین میزاره افتخار میکنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98470" target="_blank">📅 04:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بازی خوبی بوده تا الان انگلیس مکزیک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98469" target="_blank">📅 04:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWGFLYMXc034T8NaIo_6XGCti8bB5FdJZmaABFmRWh_z5_QDIC2AsNN_2qv4OU8mUJ2aioS1pWH-jIX4v3kQMFDmP9y6e7ppJ5YnvCSKKElWwEmvScH6wlRg56XuRlRij0xK8KN44mumvtAe53u-DVzexhmTgbN2-Kvpd6yOwDcZn0-Xufs8bidKKrsgfySlGYTLA0XDKFBjdnI5cySOMvIyyAAewl9dIvewDvsBiyJ6UONS0MglPDiLs97MxsGH5KfWeYuxAfeVIAjd55TlY50GXgtnFPjZHcvOpKyGm0_QeyF_zThojIg34nP4EloST2Dup_WCrsLmLOqN-yhSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمار در تیم ملی برزیل:
130 بازی
80 گل
58 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98468" target="_blank">📅 03:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoECHQpAi5P9uIPcQn48h128T2QCdo2m8SKIV5Qd4wQigXrSaR0Fwzb1HhCE1i7WislpJtuElDAZfYcEZpYpuAHT3mK136frMUwbPz5Gr8r8_O-k7d2e9LShVWseYaOyW-OAClVRhK1IFxA1uCAESbVSxGSmzGwmq2FCsfVsLr4CJqB6HU2UH0a-rt8QiDeuCKJU96s16qGvVKYg7pjo3NlafHLmxxRpO5QpFhzY32yZlIshZresHq-wWnXEyY8IDli3eXS0nkK8oGKWgoqk-TWvyu-V_2e8dsKTgJTB3y78CdrRb87mMiFvhT2FI_QXTpAaR3ew4spALYhU9vuC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ap7Y-fU5Ar_rpDJ4P70fTZsmWD1tNiXrHB9EDYtxqmWiz9BDDh6ZjQobZbUNxBzOrkOgNEsTwh2SasLov29t5D-3h6RC5huj9CGzXkp22vAK7doRAb_CvMuyvx_D-dbomVvXZE_FoHEZeKKxE1_r48jp_YRQju_YSrAQLoj4m4LNEUz29lLGhmTkI538jiH0g5OiblbTp-XaT_kS6gmFTIVfI_4y48vk-q6Na2jTjxtXdXZhW8cnwlNQpq9isXrcIfabi0BmDxOCOhXmKn5zwYCucIe5nuXs07-sSHrm1qDTBtKxWKYm9A4WQhphnDyOGrwRiT-1qkQwFSSX5cNq6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98466" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=QAiyvFyOFT3Ku82-kBLmKRbO7FtvpeXq_UCNYBOCmI9bYqOXCI2bz0qCEaK3JRQ5Afz_NyefHJ6h4d7oIX_cq-xqdT96DJPombDDLEeX2vI_c_b9oJHj_jtWmm8vxggtei47c9IYSoT0v01Co8rRZ6d1Owj6Xy4wXJWfWVK7n29k9B23aRaaQhcvXRfvwrrmedM2dgyFYdwllpPIzjnsG5DAoM_27RTwG05ufiEypEgT4zahkaiTNBrBbn6mL1p1_IUwKhs3DgWR-OA49O7sY8Ct7rEEW5pFg-BX2GjSr7yHyeWUtJI1BwVoqB92gurAL-m31hZhu5wjfUQBNlNySRXXSA50DMHzjZ0tYt0JXZVTxg97EaE_MiitSGIK2Hb5-14WlfpUekDp2P9nj0QDQqAdSzf6vaNnptY5gRUqVES8RGOcwOAePjkEeOpyItrhgHCTRQ0RqFeroFpkfd7pSDqWuCrBh-8eh0t2WZCf8WzY1gqmey5q06S0vOn-r18TtWWahf5kpMMS2nVPfBf4Y3CWcijyjbATHTJl-umAA7b_3Wk_l9HVL_iT92eVvN3uGoOLp3kTxZ_e8VgCnB_j6xO1lbhKxgZCQ2b4bgh3SdV1v0Fr6mauIm3-utK9x1vp91qy4nqWC_RbF00ysy59kt8JuAVeURS7vdKOcU3NjKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=QAiyvFyOFT3Ku82-kBLmKRbO7FtvpeXq_UCNYBOCmI9bYqOXCI2bz0qCEaK3JRQ5Afz_NyefHJ6h4d7oIX_cq-xqdT96DJPombDDLEeX2vI_c_b9oJHj_jtWmm8vxggtei47c9IYSoT0v01Co8rRZ6d1Owj6Xy4wXJWfWVK7n29k9B23aRaaQhcvXRfvwrrmedM2dgyFYdwllpPIzjnsG5DAoM_27RTwG05ufiEypEgT4zahkaiTNBrBbn6mL1p1_IUwKhs3DgWR-OA49O7sY8Ct7rEEW5pFg-BX2GjSr7yHyeWUtJI1BwVoqB92gurAL-m31hZhu5wjfUQBNlNySRXXSA50DMHzjZ0tYt0JXZVTxg97EaE_MiitSGIK2Hb5-14WlfpUekDp2P9nj0QDQqAdSzf6vaNnptY5gRUqVES8RGOcwOAePjkEeOpyItrhgHCTRQ0RqFeroFpkfd7pSDqWuCrBh-8eh0t2WZCf8WzY1gqmey5q06S0vOn-r18TtWWahf5kpMMS2nVPfBf4Y3CWcijyjbATHTJl-umAA7b_3Wk_l9HVL_iT92eVvN3uGoOLp3kTxZ_e8VgCnB_j6xO1lbhKxgZCQ2b4bgh3SdV1v0Fr6mauIm3-utK9x1vp91qy4nqWC_RbF00ysy59kt8JuAVeURS7vdKOcU3NjKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت چمدون بازیکنای ژاپن با بازیکنای قلعه نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98465" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
