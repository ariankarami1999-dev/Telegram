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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 620K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-98788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4ebc2564.mp4?token=sBFgJ6WzAO_nUM9-e99ViZJ6h_eWgAmQo92Oci2G1T6rnsPvKe6RCgpkrUReo_wkfspmouHMRvcZiSLg3fo8eCiHt6n0rg5e64XMFjK2HRl3Xcw11DYroDu3dpGAd_Psa9VQjoQocSN5c3kF_OXNJT8FS5LVG_MAvFOovdThQ6V-wA1YDsW8YfbtQdBzfqoeRCvupxSb3SinlayPAUFX8_qzT-oZmBcE4v2d1sI-6GBtMHzTIzL5J35c-auSqn-e0k7v864cd_jNtv_uttJmL_WE25PqxV2sktz1bXP9ck8yA5_QOWU8zxsCNN-FAJAt4H9pAlLFczwzwmI8a0yA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4ebc2564.mp4?token=sBFgJ6WzAO_nUM9-e99ViZJ6h_eWgAmQo92Oci2G1T6rnsPvKe6RCgpkrUReo_wkfspmouHMRvcZiSLg3fo8eCiHt6n0rg5e64XMFjK2HRl3Xcw11DYroDu3dpGAd_Psa9VQjoQocSN5c3kF_OXNJT8FS5LVG_MAvFOovdThQ6V-wA1YDsW8YfbtQdBzfqoeRCvupxSb3SinlayPAUFX8_qzT-oZmBcE4v2d1sI-6GBtMHzTIzL5J35c-auSqn-e0k7v864cd_jNtv_uttJmL_WE25PqxV2sktz1bXP9ck8yA5_QOWU8zxsCNN-FAJAt4H9pAlLFczwzwmI8a0yA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تفریحات داداش لامین‌یامال در آمریکا؛ بیچاره بلد نیست گلف بازی کنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/98788" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1325b4b8.mp4?token=NlbFC3xyUoE18CzWewqTYFPorxbvNhw7b_-NwVtlJ6FyXs5p4HdYC9aovYgOIine6oeK_QGOyn5vnGHBkTmFMOn_EA62NBtpYIz9YhJa4U53sVgqEHMMm6Hz42vv0EjCyUzzuPXe4xx6fzuQeUYeWOGgrzXtVAGutmmdYBMq8yP3lVma1ZaDemDrgN40lvTx1Ge64honuPUKy03QvlkbIn8dHqLsWk1HL3KASIUm7hc4y_r1yMl5vcYJkZO-ZHyHSQmk2mAjAkMIfJgoLWmwn-qDDIXe-PnNjCm-diBGxpNGM7dMzwOqCJmz-qbXQGvEdF6eEAR7-EKMwIyv7fdDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1325b4b8.mp4?token=NlbFC3xyUoE18CzWewqTYFPorxbvNhw7b_-NwVtlJ6FyXs5p4HdYC9aovYgOIine6oeK_QGOyn5vnGHBkTmFMOn_EA62NBtpYIz9YhJa4U53sVgqEHMMm6Hz42vv0EjCyUzzuPXe4xx6fzuQeUYeWOGgrzXtVAGutmmdYBMq8yP3lVma1ZaDemDrgN40lvTx1Ge64honuPUKy03QvlkbIn8dHqLsWk1HL3KASIUm7hc4y_r1yMl5vcYJkZO-ZHyHSQmk2mAjAkMIfJgoLWmwn-qDDIXe-PnNjCm-diBGxpNGM7dMzwOqCJmz-qbXQGvEdF6eEAR7-EKMwIyv7fdDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/98787" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTblcPuw-wEpm9y5gL2SebBpAojkBVna8APnct3MT_ynFvNOm4qYEWkuw97gWg_lsA-af6G3C7lEe7Wwo8hUGxfamSeXIBGFnzJb_5REgHn5KRH9r48ZomfP6ucPRI-PuVab23wD_pzceMH_TUxxzyZ2fM6zIiXnJi9Qte36MpgPNhUcmQrv06-0hxEUhYUO4VbgOIFZfXYzTgqTJLTKKjSAIQpnMJ0pTwIXtfyd_F0hP8IB-nzhK4rQr5aCnkH5YYLEh56L0xwE6rlX3DAVzMKIAHCPrX7Kb18XRxWrS7RXHNKAwrNZZ6fseEZk15O5NBDeaHhgTTdojYdU6Dq0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اگر لیونل مسی به مصر گلزنی کند، دومین بازیکن آرژانتینی تاریخ خواهد شد که در یک جام جهانی 8 گل به ثمر رسانده و با رکورد 8 گل گیرمو استابیله در جام جهانی 1930 برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/98786" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6074b72f72.mp4?token=CIhT09xAJlhZ4u_F47bXZM9dpe7o8gQ7ptXXlNS2xtZ6UI5OMRmwc7UTYvzhuMStkM2wNOo81j8TxidYMFJmcCXlzgJKhBhUT73aOqw9XsDX_8Ztc38x7JHfu60Es91tRYJRUbswgJaREvDfBAqKgXvvNMV-Np6eW3vmNYXmZilYv4xzSYOVPJR7O8Dc-c-xM_5M-MpeB39vryOecjmGgOd5MFUzc148INj5K1qXqJ1nkSqSGCb6AgAhF6wDss9r7rFqDwOdy76NW-PjZBP3ZDxQrjFbYIoVhFBhqZeXGn6hNSzb8qW2Tp1OFeKuFBklRvK84GCzzYiqAgYzyHqTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6074b72f72.mp4?token=CIhT09xAJlhZ4u_F47bXZM9dpe7o8gQ7ptXXlNS2xtZ6UI5OMRmwc7UTYvzhuMStkM2wNOo81j8TxidYMFJmcCXlzgJKhBhUT73aOqw9XsDX_8Ztc38x7JHfu60Es91tRYJRUbswgJaREvDfBAqKgXvvNMV-Np6eW3vmNYXmZilYv4xzSYOVPJR7O8Dc-c-xM_5M-MpeB39vryOecjmGgOd5MFUzc148INj5K1qXqJ1nkSqSGCb6AgAhF6wDss9r7rFqDwOdy76NW-PjZBP3ZDxQrjFbYIoVhFBhqZeXGn6hNSzb8qW2Tp1OFeKuFBklRvK84GCzzYiqAgYzyHqTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو شادی بعد بازی انگلیس، جان‌استونز خودشو به مصدومیت میزنه که توماس توخل نزدیک بود سکته کنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/98785" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcyAFGNh2v19pSoLFQzdrba4o-tpQCUeTteV1e8_y1k7zRhNU2_sUkvndItjjF3JG8WA5_QPW0lZYX-zdI0yKOtMWDfrhcYqKnyDWHwxX4j_XcViPZMfuzahzFUIvxh_lWAxOCF1dLVlxJJpLrtPSpowk6DtFLL7DTeIXeR9__lcrp1xSEa4od7bIKAL7SZmdc6ikmBmTMPwgG_sLt5xmzPcrDVAtv2IEj4EQvUDAbdC9mUGhjElsGArA12qQPK_qNHvQKU1TjnA64nN8O5jZjGhrkbv3lnl7DSqdTQCoBZdcb51X8zQayYBPYHO4-CjW_-1y9e0zVG4VrAJP1a6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کورتوا :
آمریکایی هارو به خاطر بی احترامی های چند روز گذشته مجازات کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98784" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98783" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98783" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98782">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98782" target="_blank">📅 15:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9aaabfe4.mp4?token=jfNAvmYMbAYIO5YBIsMW407rWIAhoFPA0vTi7HEOorGQBMKEmdo-mIt2Xo-H20XMO7tWWr2Gsn2ag7u95l4-rWLA48xXFL-Ws3ZSskjHo_YLhkBy0OkSX0tyVC-epVCPrYdTjL01KX2QhjMy2pbJsJ-9JeRqiwRDp5N3pVhyyu7vSLwOAgtUgPh8zwq-iylX5UWGtoSrF-34RCnDm1K34PLaDSw8S56eIqduD4znLW5acBaldMqRF0r-17lZbm3djOSyrUgVxGSo2cExpncO3CmoxIn74PSklbYExxc6kglJ2dK3IloUNI2oZNRp5BDHEkMQxMxSAl2kkA8vdUBMmzp_CH0L4wmYkPQ9D_Pd7e4rjcf-JTpRu2eKz8i6jSe9u4yd4zzIK23imkEkCrVNxYY4_o15SckoSyGOj8Pwo9HmNUUrlayK-WevxIQhCVZN3Wjld1Q7pG-jK4gm6fwho2hcecS9LZ8ITcfoN8liaVZKguWzw3Bopz0D7v4qdr4Wrg5pOeNfBW7ShFPebjLgr6mVwK5D9aQd1D3pvKEgXTruVWe8K2ZTpGeMzLl9GZJpgRdMVo22gMEysPYKZ8eMgEtAT4mTemPF9nk2ou-g2OyljJ84RYnDjg1C-XTPbUNBIVI07gFDLy97_y3i934RMKf0GpyrkgC8lHAIYvmXX-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9aaabfe4.mp4?token=jfNAvmYMbAYIO5YBIsMW407rWIAhoFPA0vTi7HEOorGQBMKEmdo-mIt2Xo-H20XMO7tWWr2Gsn2ag7u95l4-rWLA48xXFL-Ws3ZSskjHo_YLhkBy0OkSX0tyVC-epVCPrYdTjL01KX2QhjMy2pbJsJ-9JeRqiwRDp5N3pVhyyu7vSLwOAgtUgPh8zwq-iylX5UWGtoSrF-34RCnDm1K34PLaDSw8S56eIqduD4znLW5acBaldMqRF0r-17lZbm3djOSyrUgVxGSo2cExpncO3CmoxIn74PSklbYExxc6kglJ2dK3IloUNI2oZNRp5BDHEkMQxMxSAl2kkA8vdUBMmzp_CH0L4wmYkPQ9D_Pd7e4rjcf-JTpRu2eKz8i6jSe9u4yd4zzIK23imkEkCrVNxYY4_o15SckoSyGOj8Pwo9HmNUUrlayK-WevxIQhCVZN3Wjld1Q7pG-jK4gm6fwho2hcecS9LZ8ITcfoN8liaVZKguWzw3Bopz0D7v4qdr4Wrg5pOeNfBW7ShFPebjLgr6mVwK5D9aQd1D3pvKEgXTruVWe8K2ZTpGeMzLl9GZJpgRdMVo22gMEysPYKZ8eMgEtAT4mTemPF9nk2ou-g2OyljJ84RYnDjg1C-XTPbUNBIVI07gFDLy97_y3i934RMKf0GpyrkgC8lHAIYvmXX-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی کوتاه از عملکرد درخشان و قاطع علیرضا فغانی در بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98781" target="_blank">📅 15:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHzrnY3hVnwWax28BJiSECSoA8ieN7qGdVGStNwTh3RdkrqsW4XI_Mzf5gOtYHjNCZCRXYB1wU71BuuG8WEN9T42CxMwnzVp_gv-KlysyOJGO2jdvg0oa3EQLxpPyXJH0tgYrIvk7jJfNKQ-9mlLCxVLCt6cKDhrzGSFwh1yoYAJxI683EqomycNN4cRzRSEwg-fkfxlNlawoeFAjsBHmUnKMmNFRo8ndiUj6Tyew4_JMc-lB0evdNgCMBNDyN9OalkkTawEtp8nqWpnguZwStELvF4-VT47QOtEddmd6lO2JBPVBK88FsPGxCqM2-7LhT7nbZ1WjcblcCjYyBL_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/98780" target="_blank">📅 15:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20451491aa.mp4?token=Ut7AwcBbAEWr9qFqiTZWbk3Xu4q-XTbnBXCnK3xS8mfv_Atzc6fJZFv3w2xo7NWWVJhGkpBiwe4qjTD94BGseOn4-7nm2Fl3e_sA0O5LF8BVwhNmZtXkQuRG2gQQVoIjtQYWE4a7uVyK7HXr1TJyJJ2BGN4E80TrU2nztuzpC-0NnLEj27wInLkFwu4n8rH14jWiS9f3yJWpfTP3vh8xmLhxBEU32pbnd1ACjVjnjH9CwjifK4PoNb1FuklkVZiYw6kgvOPwh7V-Ki9lcV_f7pxdbvmF0vPcxdGLm7DbkBgI0SxjvnOxR-1m8GqCxgsN_tjyMmpntAQEF1EN60h-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20451491aa.mp4?token=Ut7AwcBbAEWr9qFqiTZWbk3Xu4q-XTbnBXCnK3xS8mfv_Atzc6fJZFv3w2xo7NWWVJhGkpBiwe4qjTD94BGseOn4-7nm2Fl3e_sA0O5LF8BVwhNmZtXkQuRG2gQQVoIjtQYWE4a7uVyK7HXr1TJyJJ2BGN4E80TrU2nztuzpC-0NnLEj27wInLkFwu4n8rH14jWiS9f3yJWpfTP3vh8xmLhxBEU32pbnd1ACjVjnjH9CwjifK4PoNb1FuklkVZiYw6kgvOPwh7V-Ki9lcV_f7pxdbvmF0vPcxdGLm7DbkBgI0SxjvnOxR-1m8GqCxgsN_tjyMmpntAQEF1EN60h-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های چندی‌پیش علیرضا فغانی درباره ظلم برخی از افراد فدراسیون نسبت به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98779" target="_blank">📅 15:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd25c97626.mp4?token=Oy6j1fZo0VfkX4mmiIlMOf4AXHyjimNBD4-UqqiNN3fP90hxOAqNI31uAqdasTbM48LggW32kkjVmCHJy_02WMa-fl74DaGQkoXJoeEGWF9RNg_xX7wZ9PCSw7LGyF48Z6bfdgp6aNeIavJhagDDSLmtNKvboZBeu1LrtfPocJQ1Fm0MDlwKEkIT4FM7acm0oJ-YuoY4FoavHiK9kNhMSKiHFYhZT_QT8M8ATaDRfKWmdwWLoN2kcUWQw3wuEKJ14itJX-k9gcS_7q1l-GDwgfKcZ4-26SgUjCyXDujpFlBHkTmPmugHDBd0L-fQhX5YlLhyT0wSLGV7CHtc6nsHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd25c97626.mp4?token=Oy6j1fZo0VfkX4mmiIlMOf4AXHyjimNBD4-UqqiNN3fP90hxOAqNI31uAqdasTbM48LggW32kkjVmCHJy_02WMa-fl74DaGQkoXJoeEGWF9RNg_xX7wZ9PCSw7LGyF48Z6bfdgp6aNeIavJhagDDSLmtNKvboZBeu1LrtfPocJQ1Fm0MDlwKEkIT4FM7acm0oJ-YuoY4FoavHiK9kNhMSKiHFYhZT_QT8M8ATaDRfKWmdwWLoN2kcUWQw3wuEKJ14itJX-k9gcS_7q1l-GDwgfKcZ4-26SgUjCyXDujpFlBHkTmPmugHDBd0L-fQhX5YlLhyT0wSLGV7CHtc6nsHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
لب‌خوانی نیمار در صحنه پنالتی بازی نروژ؛ حتی تو لحظه‌بگایی دست از کری‌خونی برنمیداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98778" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
رویای‌علیرضا فغانی: قضاوت فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98777" target="_blank">📅 14:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇬
آماده‌سازی ورزشگاه بازی مصر و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98776" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98773">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_kYQq4Ho84F-SnVIIL73uwwpdRTXu3bmqOciu9sveLft2cKrE-jHmZMQZRK9NRfdrNtHUDwOmuxygyZnZvKGv3py86MKz4nyCcBXWidTRrPxyLctp3iM-BRfZf71u_AE5iju18mTMpTnbRAoAVy7a0QxSqIepShDEroSD4jfCNjn_iCm4FcIKB1yplaHCmOnl0_M4uQ2pHTM1qd_98ifefax92jk41RsQSxPfAqeC8H51nenorSurg1QFROKwDyQYf-NEelrbtPI71nypgtigtevVkYt9IQihxce8J0lENwxR0BO2M9jLxBkeocC_iUjZTaSosqdSuMmUjthCi8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXwdO4ynZI2Qpn-JZcmD2wPSYopTKxQKFAtrHgv9h_w3Po15dM_F66n4jrhjjzng4Iv2hrBgEgGTmU9XySEJpcgJB-0iqKpzHcmISjjjbphfJMM4pxsr_pQXeA8Jbw_uRYstfg3euLSpLCGSx9Hlrve8l8uP7nO1Q4IRuejpYVahY9C6X6Lef8ziSfVdh-2qsuzFetiKBUBc41AONuk1-c4dLHif_ikgbKruaJ2Csw8n8tvO0oGX0VTHK6b7ff2coypq_YPrU10UwJmllTetYPLql3hNbw3xaZuBXYhq_-Pr4ExlrXx3d477DkKAus_OV_2hK4GM-bzSHMPmUeDuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utl_IU7n7F5r79p1VcouvflAzfDkelz62RbDzlq-O-IwX7vntweCt-JsRAAgVSopi_LO7FVCGv66Fn3Vs_1ucxN2rXsgApk8tPyaxDnwTPXoQElFPXyjrTrpP6Ak51eB8g4QSAe3U4qm6qjiTimB49Xcru72QMDxy2Rcv8gEQZpua439EE3Vv9S3rzuBGy8nTG7geKt1yatOIG9lBy_scplX-vHue7ge3oMPW67Ui-D2LXKyDtHO1MGyP-jumQ81L8LUb4-p4PCFsSGSBxAIyj8bDDDgEGeNlxVjy7QndXwcCEXrCaJFkw3PGpURrDQ2fg6fHCByhi5pXrKxISh-mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
دوس‌دختر ژائو نوس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98773" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98772">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jtc78GXfYb_IAGwc7N8JDa9UZOa-5mEcpQOipixSr37CRNzeG3Zj1MybtKBCsw5YXpjTxUAHLptyA1q1nWR3PpgExW30u0pBlavnNLFS2nDNmBxacMAHoFIg9uRn7fw0uWVJGeXCnjMPtUoyNFpCwRIYpZB1034O-gwgf1RGOfUnVf869Dq56EdA3rGVgHHd-zV5vRmovL-biUC18uglmoKQHsb7GlLJZeohQygFO0jPV5lQmXrD4H04BHH5UZfLoTX4nyb-W1jpSbvCWViCFiOtiO9lGQuEWv1vD_Vc6TIOFGq-_Cu-S-OomHjsNFoi1uNtCdYiUjnNKpQdmubWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق
🫠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98772" target="_blank">📅 14:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98771">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
🤣
💸
💸
وضعیت دیشب اهل دلا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98771" target="_blank">📅 14:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98770">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lkJParYxFRaDzCk3yXTlm_l9GHPFv-9HWUtgIQBqdeDAiKkeAp2ynA5gM360El43mKdd_Iumaj75p1dVuNPdk5KxQgBf2EYmgGUUUszCz2QFCzwPpS5jNpAdHm3ZLFme0g2WmniPJN_vpHgAyxehrAPJHorYSKpUa4MxxJwIkiAhS5tv7zCMx3ef9bQvILLMbKwB0ZH6Qq7Z65AeAlKR_xJtCUBOxfdTt04qCcEUhlw_0v7kTbw3al-hnrnUTfeON1Qllfr-fLfx_WoC4_kBdqFzCGxXctuwkrQ3jTCzGBGRHpp7PhiaYNXGbDw7otL7mDxwu2oio1oN5TNIhs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
آمار لیونل‌مسی، در بازی‌های مرحله حذفی رقابت‌های جام جهانی:
• 13 مسابقه.
• 6 گل.
⚽️
• 6 پاس گل.
🔴
• 12 مشارکت.
🔥
• بیشترین مشارکت در گلزنی در تاریخ بازی‌های حذفی جام جهانی.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98770" target="_blank">📅 13:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98769">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_8IqI8HA-dJIqmhLqpN3wv5WD4FmwVQBGi73aVqbSEoBL7GWsmjE37IR0nfcB_Pe_XhZrvuAm0-5pDCUSdbBxdZdbVfljNO9o5Gzhf4V9HN5y6DxkMvrspcRPrvCpUZeH2PwagLQKNs8EfO1b1JSWHOfvoqcE6IVokzxL7gM4JsvqjxdzShyO5weFrbkmz8sDQXuecLxuuWNlvxIubALV6uXHDXHrVMHkSchLGxmZANbOMvrMXy_88XLFM5jwi2J_GmydWJkJ3wq2jZBCspQFKYAtRr62uZIb3ygbaXcDfL-2pSxjJtWY4BvrZOfgtQoejAtVVJph-QyCBVe1rtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا در آستانه تکمیل قرارداد ژائو کانسلو با پرداخت ۱۰ میلیون یورو به تیم فوتبال الهلال عربستان قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98769" target="_blank">📅 13:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98768">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
وقتی با رفیق بی‌اعصاب فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98768" target="_blank">📅 13:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98767">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇵🇹
مشکلات‌رونالدو و بازیکنان پرتغال در همین ویدیو کوتاه کاملا واضح و مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98767" target="_blank">📅 13:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98766">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
#فوری
؛ پائولو دیبالا ستاره آرژانتینی قرارداد خود را با آاس‌رم تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98766" target="_blank">📅 12:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98765">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه‌های شدید نوجوان ایرانی طرفدار CR7
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98765" target="_blank">📅 12:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98764">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
😆
😆
پرزیدنت دونالد ترامپ در بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98764" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98763">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ویدیو لو رفته از رونالدو در رختکن پرتغال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98763" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98762">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpOgTlZrHhBrbHfF8wS_s8izBhKrIdYqB7P95fEaXWpR-XM8rFHpxSR4pugTRygLeYHo70DbqQo_zl61y0i-5tpRGjkVkZasjkRafkhoryPvAcwMtaKRMAjmtu-wn4a_ZIS7cb3ZFBIgTfvFII0PHCfrzKy8DkuTbu99zfB2CkkoDLStWsrXOyyjj-1--Q9pxP73zzQnfQy0QvXQCvbZpb4v_OCAxAO2YOylJ7FeTKE4sneJs9p-HWY4vCXkx4wPeIV2nh8ACqTApJzovfBjJFJrJ2WFxS7Di8iIn9K1ZqfE1J1cKxD3dsDjTZcm68p4OqYaRF5LgBNAxYuZxbJnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇧🇪
اونانا هافبک تیم‌ملی بلژیک در بازی دیشب دچار پارگی رباط صلیبی شده و ماه‌ها قادر به حضور در میادین فوتبال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98762" target="_blank">📅 11:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔥
🏆
فقط چند روز تا نبرد حساس مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98761" target="_blank">📅 11:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4HSIayb7GyKDWWTAaEYmiYN_7j4W9qIeAHi_xpMaLp-l9Zfzb1-Mz5iK4mrgxUZttaTmp4uao6E43JMTFFeum0gH1ePcNw3Xe7VTL2ZqQ8nCnikajpr6icAUyAEUenhE3nzh6jJoVtEWpKrqDhvYsRUw4Gb80tfzaq9n3UFc9KXWMvFEUm6GpODTyu-_Aux8BJNYomajX52tGwdbX1ZGONpsXXOcKJOuw4bcggEGokX5pybfdaews1tKOzpIQ0z0cagHScicJy12kfrejxTpy_iKRFeViHReQrOknCQIGWIFDzDSiacuAPlvW6xsGfm0fRs-LwZicQE4YUktd9MPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اینیگو مارتینز با النصر عربستان برای تمدید قرارداد یک ساله به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98760" target="_blank">📅 11:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Pxc_emWVzkWgBneIfrs9DjSz7PRMk4MfENlqZ_16Zzd4REOdT1YaTOG91mzN4MdxWDnCnJMVj3IIHQhXcJedqsplPJqyrKDwF3WUJa75plxKXWJhC73zTiQ987wh8ke4bzUcN_kt86MyIwH8r-oEJ3Qje1GvpITUMM4WeQ3uXbmQSUdGlfqdfb1q3a2mquTq52ZemAFj3t9nz_eV-d-XhbDi0eI2XH3F6Nrw15ucHYVUQOf9IcYH3XvxQ-3RY5K1LpejVyCWm9fROHx6snu1dCoCssrldxszFXjzmUZooI_XmDlz-azODfagQ0Apmiys6HB1YlM9iSDqoJIt_Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنان رئال مادرید تا به امروز، از بین تمام تیم‌ها، بیشترین تعداد گل را در جام جهانی به ثمر رسانده‌اند.
⚽️
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98759" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
🇧🇪
خلاصه تقابل آمریکا و بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98758" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ-1rofA9pYvpp6gt4kP3N8KW2A4Xn2Gymqhn2bMpA6uo3kSUCy2DXG2UwHRTJjNZpMjZqtrxF6f6TW-sPZNA4EK_BpxUmAvf7rYwQqWTgFQK4Pmsp0zUA1ZCaZjbcMV4LL7fV1nCgXL28DQmP2JYA4BTB7cna_sqIMWj5iFfR_BBHNQhW0LPnGt9bblfdvMg-w6kMwISDAmjQB_oeBIIkiJcn0o7mdYpu4EV8RvqOftXawnM6upWI_Z8pOoEJYeKCIFenOo9OwR5kZ3wd0XGT4bMVYLcZ9t-6tSeezLw5CvOF517ifzhwCU7Rm9XnMbpFedpL9DILB0feNBze-Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استوری پیج تیم ملی و کنایه به حذف آمریکا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98757" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
مشکلات واضح کریستیانو با برونو فرناندز و سایر بازیکنان پرتغال در بازی دیشب...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98756" target="_blank">📅 10:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
خوشحالی شدید میثاقی و دیگر مجری شبکه سه سیما از باخت و حذف تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98755" target="_blank">📅 10:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💔
💔
The End
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98754" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب فوتبال گریست.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98753" target="_blank">📅 09:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظی رونالدو و پرتغال با جام جهانی 2026! اسپانیا به یک چهارم نهایی رسید.
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98752" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
▶️
امیر مهدی‌ژوله یکی‌دوسال پیش این حرف طلایی رو به عادل فردوسی‌پور گفت. بفرستید برا هوادارای فوتبال خصوصا رونالدو فن‌ها که بدونن ناراحتی هیچ فایده‌ای نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98751" target="_blank">📅 08:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وضعیت آسمون بلژیک بعد از بازی امروز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/98750" target="_blank">📅 06:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3BFj3-MOKZLZmal3j8mBHdAZh301MVEoNo53oAhYeciT7MmG7-BcKQSntxSwI1uiD4xvIOxBWmYRTigK7LSs4gC0tS-_pAhl_UC_vDdZdling3JjYWH89qRZqjSxFYUy3HAdwjM9lfjsujcsYiGVIhqlpiM5YPbdwT8a6vFyPcFJrwHoES3PzX2iaIs_MPelTsApI4tuJt3IYaGpUFoG3CcN4YKMUIlkW60f3FfBg1OUXxWIAFKG04yNpbaV3sm0N0-D7O01j724lUjaX-PuP049Li9ESVgKYBTev9TcGXMXMiajWlf3IziXk-f-dhpGdz_AT653hcfN5voGNMqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/98749" target="_blank">📅 06:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGtaNIDXH6KGUryDa63rOy1EcFoPD-hMZBW2nWp7Q_LYw1jctLbIEzU8kTPyR4Menm3oKAPh3HFnx_L9ayA-OR_IVY2dagQgl2VC2IUTEjeQOWxYFDOmOZT6CkZjsTkbF6BoX2QYZZOxsr0gn20vC5nz5ZvzMREU0Ntt_BqZwTHCCfLu2nv1SUrS9vTgkuGNASn-N0xNwuZ_-Tsc2dAVzXma2TEzBnr2VA6gadYRGflk_IWM6fyiseF7IK3OnCRA8hx4ouNV2L-4o9TmN9q3o7oeHAHRZYmhK9IWzZ47IXDc7nYgDEtK6B7ZIBuAPJI5Gp7UUDkCAB4zLDvN_2T_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98748" target="_blank">📅 06:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkanwpFZVwpe3Yp685742g4NKbpIHxK8QvK-6WmC0tFl-hAw4EzePFL09gUGz8ptcVz-HwoucDGgiE-aRaPwb7rxjxKbs0Coj-Dv9yqDjgx5hgPqS9jmqJoEo8aA0rO-bWGjnsftc8jhtHtk6iAdVRSm01ETJawm6yPeTsrOtfrwJblNRNlK6Thb1lPioQ-igDIy10F3qxmqAApooqP1UC4Gc4q9pIsoxOv_FGWeYbZAMrWE43A2V4aAS6UczlQY_7NWVe0DR4jqTBog1joOBRZufqpS9mET1Hrw5hENtZYhfvtdfUEZOhqy_VSMwDDvllo39FeXiuGv4T4OBHJ0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج توییتر تیم ملی بلژیک به آمریکا: به این میگن
ساکر
فوتبال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/98747" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYpY1AJ3i8d-SboAIocxbFPGeBk6XmYPPrjzpy2MPB5yIyLaZePUcRUHh-mNkYGagAG2AeqnDUftK5nwc3uIa0E6s3Lt4xaFvpDWfiYrjbhlHJvld0RitupJaI7cX9fOKQOVKHjq8Wu6_dOYtPjf1p3XSKREjlBHHxJBZ08kFxQkkg6yafU4g7QCja4S8iVYCymokW20RAwEVfOk9cX8o8Rht36x2SshhC_sL6GbDFLF0fBFycLgwRp7mHcxYI_Bh_MYpTNUJkF5fXI8aqlDWPoqVDvQj2J_niI2BmQ4Y40Ej7LFHlOa6xxl1rbtQ6jddoNV404ivbkOR0MoKR3eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابل جذاب دو ستاره این‌بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98746" target="_blank">📅 05:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BobE2QSoKQ80LuQIdmNFVWb5_InAdBn0pTLontmVSqDEBxrGcrH2hGAlAd7akXdjKpxvlouOUv3s2n0VUaj0tkJwkaQJ5cMcKt2LaCHDwwdNHliIgN2QadJG0J4mOEXg-7PXTd0zSWCa1bnfZAk-TOlgLQaGxNfsr_8P5EObpwrCq21DL3m3nc7puNIQkfNxCvOgOI6IlSVlwEcExvmS3YvLCgFP1odqoTMLZ3qO93uZ43ebEeS4oDEOFDARptc1NaKoZu4XsY0umVM1pOGkKXM85h5ycXQAhRUB3Cz0wXxHrvw1npb9ul0x8o73QVEtopJbke6D5art5bIK_sjOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇪🇸
اسپانیا - بلژیک
🇧🇪
📆
جمعه، 19
تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98745" target="_blank">📅 05:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7macHP-2wy2mN5StMVRQy6FUOwGyTk65FnOgrxnE76Pmrpl5Kv_pCnH8I9lDXJaRbwcpQZFK2S1ygy17pJyq4TtP8gLYdqYjGAi1DwidRNgxOsIDyWgsAhv_7I7vP_6zCQMu0tCJBn-qnomryAHFc53LUUapUBsfRWcceeq2zjD2fZgssxlFOMF9gwpY9q7NwcdqUg2OWBzBPpNNgxMg31WNV6e66psMlbt9FAIEM3a-YcM0CZ-3if7UnDfTuVZhQ-Y6DTdewoeFW86kSDVou0UKIN1manqys-RktAY8snnsUh0adKILVO8OCm8gOoEW2wZG9IaE8vC5uBvQ-A6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98744" target="_blank">📅 05:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAMua9AER_YSgBShkJe3qT4OI5AZwtGxHRZ0OGBp4sDv278MKI6FBf-IBWTI0EGRMTEyr2Eip3bWdW1oghXf5jYWx-E9TQXA-rwlPzMJT6gUMbG4V6DbU1gslV-PmlRTFcewd6mBzeZJLe1MjxKeueLoNTqXvi-KHHBPKnu-Yv8RvIwipiazGqlUa3fCV6q4doNBOMbo0F_pxZ0esQL8ReJuA0VXX9Eq9jXxI_TsNP_8duip09Orp2NP8wHBHIsObz9BtsYycZVEak9joeqKo0SUn8B626_0CokUyWsklqexw72xJHkHKhk6AGwim6hsmtZrDh3XtiGHhTelmhBLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد قاطعانه بلژیک مقابل آمریکا در سیاتل؛
کارمای بالوگان!
🇧🇪
بلژیک
4️⃣
-
1️⃣
آمریکا
🇺🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98743" target="_blank">📅 05:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🔥
تقه چهارم بلژیک به آمریکا توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98742" target="_blank">📅 05:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بالوگان فردا املاکی کونت میذاره.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98741" target="_blank">📅 05:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98740">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جوری که بلژیک داره میرسه به یکچهارم نهایی ماتحت خیلی از تیمایی که حقشون بود تو اون مرحله باشن رو به آتش میکشه...</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98740" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل سوم بلژیک به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98739" target="_blank">📅 04:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/palChTQ3vk7u2ycn8I6HuBnF2PVmkfQ0KZYcnC-5QdOil6fj0rPcrZCubRmkIsHZJ95Tf8G0W4ISpIbY9OB84pqzjELTykTrw2JgOit9k-SvQ9KmLflRDWnPu1JRbxJp23OSRkmn6Tf0EtPYUFibr80FEhcvo0H2jC1swEZdsWltKnSiuDyCEEiRotPJeNpFE_ck148NQrKAPNtwNSt8bQdBS7LcDJP9G2SeIuWG82X19hQPiJgLoWxPOdLoDFS1A-DuvL-zNtVj36XxvJf9sEICPpydBPmuLYvo3U1LbamN7fkWpWbZ2OzeiciMpvgVyk4T0Kc7Ug5L3mbpztZDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی ترامپ قرار نیست برای گل‌زدن بلژیک به آمریکا با سنگر‌شکن B2 حمله کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98738" target="_blank">📅 04:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98737">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل دوم بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98737" target="_blank">📅 04:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کاشته خوشگل و گل تیلمن به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98736" target="_blank">📅 04:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98735" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9kkJhglmMjlEXD763G7ssT-_F4VAz7laEG_RMapExJTaWcX2z_K2c4WYBpbS_-yqdhlxrHEFsTfJZv0Xr-wY3v6Cby4r7y090WskTI5jHqxoL5DTS_YWXSs7-yub836BHubXOq4-RC7dAjpuFPKXBY96Z-wu4B9XgjDtsLlCEpzY6vIgAMTnFkx6-Wq_kAB3cFlFl9E6rTvSSmuPQ0IEE0RkBwQ3udUXwB0GkUfH63-rS19zPL6pcndU_zagWOULRMmLERF_K863RGBQswxbo_v1cGWF2D5OceEWTvLzHSjsUMaGgCFX-4bJYhE5UQiEG9vSA_x2bR9pJfUcRYkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اینفانتینو بعد گل خوردن آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98734" target="_blank">📅 03:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98733">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXAoXhSIoggCSFYxsG-T7yI9ckb7poBDEXuNyPXyHzXFmbnBo5lP_KIoD5eOSZW6BqhCsZCCefbmV0klbKG3GeZIqvpWJue3_JU1_58PUSF1CPAilgYTHWE0vmZxPVOVb3BQZURgKoTDRU-TfFLDmol6lIM-Y8SgCE2YbCC9HuD9Td_yBOMXI-hhGKHJJjIpEJ7kQRBlYczBBEkK5mjOWy2pJG4wnADUG8BmebmaCByK35je203kiYOjVE7VmcZ6RwbYyXFuRy-6znPFPVsK_cSISzhje2bH0zEAImgtsXj0hrZyk0sPYitE6ylZfITXiFNcGOJr_rq0YpYmS3wRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای رونالدو کامنتای مرینو رو بعد بازی حسابی گاییدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98733" target="_blank">📅 03:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98732">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گللللللللللللل بلژیک
🔥
🔥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98732" target="_blank">📅 03:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98731">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بریم برا بازی آمریکا - بلژیک</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98731" target="_blank">📅 03:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98730">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDiMAboBWIrXZpTn76zTQltUvXmSDM5z4-TXat077flw_BZTQVyiYSYpEDKbFr2xZAz-_SCJTGzO6rwbJ5kAr12idKs43UkbCvA8eFCosmFTKdR2AzCASV3mrd2OqsUZm0Hu2zuZ-bXAvDXNrMszwGTg-oA4SLxf7sSbQarepnZo1HeAcUK7Vc1IUnXccfPTdI_kCT0kzML4zm-xjUloxZsiVg-bZYrBQOR0Enyjqmz6hfohZTI_vedkh4UHwF5nKNN9vE3yXWC_Ry9ygDuPMLqheULQEM_ogalXUlyN5xClYbWwhbxnSltrWvd45LdMylmmg0Rlj2nw6m7ZFMxqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه عملکرد هالند و امباپه در تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98730" target="_blank">📅 03:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98729">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98729" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mANrtYm_nNXXz-LPpqonBs5-GfpcGKX57nFsXnoHbwIiKF2snsLlP1ypYykKOiuKiFn381mEL0jJ7J22vBD01fLCyGypKqlSTD8sw50T5AZwzz4erXKGRIAJCtl2eFqmynqkV4d-IQM0Mc0j_IvXpGSUh4icyd5w0nRH2EHd8YgghaFkzkW3pcK1W2ttcshaB02Tw9j9QehEpK8Ncqpq5jl5GcrUQ5i2BJbRiEqfRnc5eN6Pvy-S3cyRy41TztCgrTohg8bn8Caz97ndcEteWtNNNSJATdRkHuehkzx_8JxYzi2lDX2aZ9KPslfDORb5rZm2JvfGDp0eTgbkmprIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98727" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98726">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های اسپید بعد حذف پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98726" target="_blank">📅 02:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuIOTmTgbIW65pfgADkF-jLohcpVo55bmc4bBtCIeQkj630krXd6H9C4RHtMcq4OSNW0YXLttuAuo_HEZs290KzVL73IfqiSV3ggzEO6OKK9haxlBydhVqYn9GlKH0Xpx36eCO0ZAzRiMkVyQY9IWsv10YVZB2wCgScH03gqk-Rfvb5IT5p3vDc098MULSa853PfYnp_AQUtUW_Mlshk7K69V430Ydl-nCT-6tARyumuaMGauK6KY1jTRcxNbtS9Fu7m7JSkqZlIopC0_8f2kyl97M_6ZsVZlYB8QCGOZBj84kBfW4OpqV3PdG1dxmCNocVXkn78JZbnPxd52qXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn5bXCM2HLxteAfILY9fIRqe7nl37FoZYlY_uNBhKS6T_wzPh-HPaNu2Zo_rJOHn8ka5H7yoPL6YE1w0xmFukIlalDlnTZdatmlfAk9EgviWeNoTjBfeh9Mn9K8I6G5dlaZevJ-MQ1e8Zd1rJvkSi84WB9nJeCsyfSxCIlB_mU4SP5qWbjrtTVnPZKK5DMlz0_FoCz9MRU__KAAN4zO7gHCjt0JJ7kZbe9D_R6jQE7HJ5GYjDN44bMgcAgiS36YUA6UjJkEJSvIeaGIHaioU5LB6pf5J_VL64D9ZFQv126tVEIEykUaNcQJqK5sA71cbuZwlAmuMUUPzfiDGBrn7bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">-
First dance.
🫣
- Last dance.
🤕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98724" target="_blank">📅 02:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
رونالدو: از فردا در آغوش جورجینا خواهم بود و با فرزندانمان تعطیلات را با لذت و آرامش پیگیری خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98723" target="_blank">📅 02:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔥
👀
#فوووووری از جورجینا بعد از بازی:   برای امشب و تعطیلات تابستانی برنامه ویژه‌ای برای ریکاوری ذهنی و جسمی همسرم کریستیانو دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98722" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98721" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB1oobk1nEIc7YJjK4EB1Zb0FnrZ2sRWc8WQDXX4d4TEdph6cGg4NbCYtmunNsAyw8F3MAWDlMt2cN-JfFspooQblKWL3sgYGI9nFFKRq5C-KdRVt13c6YyVCH1pDfOdPs5Qx3A_8Uoc_Y2pU1YNbTFEl0tIm5vwmnNEve-kaNxnThv8kRMKpSG5lR3VlrEnudInf-tBd4cYwfT9zk4T8rTI9b-uHtjcpi86_Tf841uvYkkvkgnjeMiq5xKLpROEsmjuGJIMpouNEIrElwbaaKv1KotZmxA0WTzz3u7uQttD-qJClTCas6e5Q42UHL1XUCyzMW9d2KWKFC0OywjBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇧🇪
ترکیب تیم‌های بلژیک و آمریکا با حضور ثابت بالوگون بازیکن جنجالی آمریکایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98718" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98717" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98716" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHA4qw-8Ty0MeWDR8Otb7wiKhF6K4pWj595lNenI5_8QBOuLjM2Bv2AKbykKSl7NPrbBi5_YSBA-S8mHm72lGm1X1mnVlFU2l83MvyiVzpyfkH1qWFx0TWWcwemhTJkyTmwCypcpvBZV5uQETI3FoeqRl-mXo2phav5kc1uJFPe1LzakbFeyJ0I-rBhxRhy8bB2LoWmsUzALBFJGvRV07fgnThotIkBGAre-Q9fTgXW-iq63GJRcaD4-FdtGNLyvFShgv2lrDORLp-u7fjs2VCx7eG8IEpelHiOQ2EZPby3Pl9YdzGmJyIycLqZ7ry0cIgvc6JGgcPep-AQ-GIfEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:
‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."
"زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی من با تیم ملی در سال 2016، با قهرمانی در یورو بود. برای من، این مساوی جام جهانی بود."
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98715" target="_blank">📅 01:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAMmZYfmzqXrV1Ug8oGNMRj4cObA5wM0ZdxlZnioFk9OEXq0akZrFd_dzmRZbjG5FpQ4_mJvrG09iwPxo47vsRsSTP_hhEacpBhuNfeiz6teuLBN12hH3MOTpz9liPWIAJ8XG1GexlWIY8rzxoD04i8oKCnpNl5cPR9FQjoy3ZkazwCiPEzjMKHcJkNmf72mfujUO2zkQG06J6RxepJw3Z9tTq5psjgcoatyO5KvxWgPdfE9O9_SnAVwOAgxrmYdp84gRjm_OK7acKvKfQ980AI012SUt8Q0a_6MGtb9661IYhdNUo0wJoz3qgOgU6CwSWNwyptYx6VHRqLXHXQTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خورخه ژسوس گزینه اصلی جانشینی روبرتو مارتینز در تیم ملی پرتغال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98714" target="_blank">📅 01:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbAd9Ndlu4MQAtUjpXEOEUZgkNebDlY2INAafpBPYlPMahpT2KwJXZ65G1-KudeKlOefmd1nshMjhPPapDcsKTgH7WarYhGKU-tuLpo65E4eDgzlaRCSb_QrHRyAcoZQMGITeRQxVkO4zoS0qyVY_wm1muOtMrPWGvjrCRRxAfqF1B911cTdFzS_crmT4w7FX1H3VPUk6JGz4DzdvmSjQIKrbRp3-e7vUch2_Jhns2AC9PbjhjxCepH2vNKC7NmarLBCBvf6a7SdWzCUUGpoHOTU2il2HaPOgkWvdXcE6TeK8b74Zi-hzQUf4IO6E1fizfwcuUvxKN4dxeQgiVtarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
کسشر و خیانت‌کار اگه قاب بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98713" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjAlOLWBVHQ7iHIuU2iE1y8Dbp0MqmVq_vgp9XlSYSa_rOPFxC8ETsdxR4xxnXmr-MXkBDKVY1QVf-UJhFVCVZ2-YKIrE_qwEGKJdabCTfaoTIdgXLJezWVzNx1RJrVaqA7rimr7VhMUv2pkRL3UbCoYErCtTbFqygbi3JV-4rXjZNNI7gHjZ7s-UMhuW8GU-mkyYxk-DBPJcqaV69Ps2T7zjyqDc2LpIajUp90XKonpM1AaSv9srgpqKFibAwsAnpY8sCIZWYgMZhEymZC6gJunWYz2dKYBhNEnk5ibxuQojnUqdH8K0xO2kI5d1B2C3BhcX041PnssHtVw_VVJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🙂
ژست لامین‌یامال در رختکن اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98712" target="_blank">📅 01:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfZERwG6TD2saPO9G14qE0UdSKj6i3Q7zPfPn4PUtzwrUr-Gi1GPTbjiwb4FzoA3GoCvDk_8ay6y7aHM77qLEFgInKuFlYSGOWE3BVzooTruuaQiDFonZuw0FfvBY615Dz0w7v4R9kB-95Lz8cjvsGLIsRbKtOTLUglMchH5lbkprLbzTo8dAtAhH9YRm9xUzBcAaNQxtTynqe1qXZHvDNFAe81IPnP-7tyJhAmT6onYLSVVLQrGdHDArUn-fg9pkWwNF02nQpc0syL7G4N_RgLtV_F7o2fdlB9lvVfrmM5XBCABusm2GR-SG0nLakj-qxPmx6liOnfZao_O0AwiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی؛ حریف اسپانیا تا ساعاتی دیگر مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98711" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVyTQ9gzT4oEEzJ1gHNBBT6xCjPgJbP4kFiIfu2_6r5CxrtD6vin258NW5bfzELIggF8IOqrZPtiTEKlqbc5Mx2grsjxmMkgwjn4aLQfqibsxePvrzzeH1FcO0m8IPiqRbvW0Hc8qPi9hChgkq9bctjyQfx3cptsGL5zv6SMxOSGEdsOtt-RQ2imTV1Vf5Wd-Zfn8x0J4horhO5rflONLnL6T7uYZx-Ru8C6E5Eew8nfvFQ4DJsDryCnnXxUKokO8gRQN_0mwyeCtsu8yT3Fetf4q6eEu81lILCnCFWnJ0UM0oQyKbAMNsrmLx_PN4gL-DZCiEgvKGeuUhn1BZzmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پرتغال قبل کریستیانو
🇵🇹
:
❌
در 3 دوره از 17 جام جهانی شرکت کرده است.
❌
در 3 دوره از 11 مسابقات یورو شرکت کرده است.
❌
0 قهرمانی.
📊
• پرتغال با کریستیانو
🇵🇹
:
✅
در 6 دوره از 6 جام جهانی شرکت کرده است.
✅
در 6 دوره از 6 مسابقات یورو شرکت کرده است.
✅
قهرمان یورو
🏆
.
✅
قهرمان لیگ ملت‌های اروپا
🏆
✅
قهرمان لیگ ملت‌های اروپا
🏆
— پرتغال بدون کریستیانو، هیچ چیز نیست
🐐
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98710" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98709" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX5Nld2T1Xz9ghH6pfqHjSoAZ-n2R2qKcFn4Dg1IEqIy3344HaI04RoVYkQ9Rom31EyVyZezErHPRiZj4D0Vwed7zqFtz_RlOTZSBCtpFtten4e9A_qZKdDIwcEA9jvcAOtmOd9Gv2AOx36funyDB7F9vilSswRQ8JNBHjt2_Wlgw37fsWrcmXv6BXc0v_FHt9K9sieAwnvITGriNiXGdCQDWScP8oObAJbBWY_Ihra-umgZVai2N74f9EOdcS8Z73wEXjUU3PwSS4X_vdpgeEiXskrGnOkRMUzlmKdnOPdFDklffIrKlqyneDzooSQfBSNeEVJmvjWunue4V9XHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/98708" target="_blank">📅 01:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98707">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpFaRWFdgx4HCx4fRgdxFc7_NMPB_b0_yr07z-ew235OmuMDjbLxjqwRbSMgp2Hbw6kdq5NxtYJiHeK_HGhAi4GQ1JWpH_QtXjUy-UtKMABOvPG_j8sYZqRYS62zPPicugMzNqjTKpJQ7yaFJcyJtgrsPldCNXXmAUUra764RFh-TbZFx6p9cSUQvEyS1T4VYy_boNKV6NFFCGBSJG9saLjemy5WxCITBEm2OmQ7RkP-IMLDkCgZ2MO3O_tVGiVItL67PrGtuRYb0vDl3E6UJ6vCI3Nq56xPs6KBroQ5w13LNUN_CqdyunV9BeLlhmvbtaZpobj2d7IXej14_jM1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیانیه فرانس‌فوتبال برای رونالدو: - از شما برای خاطرات بی‌نهایتی که به ما دادید، سپاسگزاریم. میراث شما و پنج جایزه توپ طلایی‌تان، ابدی هستند.
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98707" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98706">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIgR1XC8kVKS0FcABlMnTuVEKI2tJhS3y4LC02B5TQpPvkgV8cOxbS6rp2QrFcV2mOv3a-W02x4eAz0xh02QZua0JMtKBcvPZejoQx3vrEppAwyYII6GdMU6xJh-nRePMAg8pbFCrM9JGBmprt0j9rJnox_Bn2tQEqCEAwbOH94BUEkaw7E8mYUyg-5nEre0YJ8RxaFwHqe4eA4RlwKEVl31TCgSOshn8772ncDFmZc4XmIZG41J186bdEbuhYgl1ExNOTjP7-vtCFKhRoHsjw-xRCbR2h8UhR12xPidCDn6U2Z7d3jq4G_n3bsYGM8_7_39P4YbbQQKOE9eNJ1m7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز از تیم ملی پرتغال جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98706" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98705">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153aac5990.mp4?token=FX_nRSYkKQWIJYNB94EjG_9cyrCjib3rJ4zTbFQnfApy7N31grj-t27y7UDn0OsGxAP5E3vMhEdHFPU9xr4djG3_zXmvM4DebyWRJ5NaBhtD8wcdXBfCb6e-idyYExF1dA7VmGIdIcQQbjPqT9UYO28YpZAYzYCFkGwcoJFncb1vYPL4CWy5BvRet6C-gHtNvQTsFRkpB4QLL8Zg85YB28rKqjyOTVHUSFR3dzOTLcc4TGffT0Iygyp1RCd0jHbNTOrwv0ZUNq6OXQvIBBi2AhbuQ3LjS26zG-JjjX6r5ep6f12gZ2VAAkmlr0qd7pmTwdEwZa6eAJlKFTWiC6twag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153aac5990.mp4?token=FX_nRSYkKQWIJYNB94EjG_9cyrCjib3rJ4zTbFQnfApy7N31grj-t27y7UDn0OsGxAP5E3vMhEdHFPU9xr4djG3_zXmvM4DebyWRJ5NaBhtD8wcdXBfCb6e-idyYExF1dA7VmGIdIcQQbjPqT9UYO28YpZAYzYCFkGwcoJFncb1vYPL4CWy5BvRet6C-gHtNvQTsFRkpB4QLL8Zg85YB28rKqjyOTVHUSFR3dzOTLcc4TGffT0Iygyp1RCd0jHbNTOrwv0ZUNq6OXQvIBBi2AhbuQ3LjS26zG-JjjX6r5ep6f12gZ2VAAkmlr0qd7pmTwdEwZa6eAJlKFTWiC6twag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
💔
💔
▶️
عادل فردوسی‌پور کاری کرد که امشب هر فوتبال دوستی بابت رونالدو اشک بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/98705" target="_blank">📅 01:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98704">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=GIuhf17ZMmQqslMfvAKBp1TkNA_3Romq0msPLipqJQoh9VrblYFikHfaBMZYS-uHAovy-0MtXb16KMX9nkg_zDQy0kOvs8M3wERNZp36s6GfQLK2qfD8bBr_D4-Ropf5w-7I0E5dZGvGMnXtBsVqY-0YhWcbiXm7ya5B8Nd-hprqEmVwviKSzT9oR3ut7ImIO9Hf_R8gHcI3f1Jz4hg6ozw4v4oSYZYw7A82S-P1GCh8GqYs2TKKovLCityrt5tsTLtC_N1zApE7spal9GPDzQGRY6PKVwhW5XdWLhcxJRxDr-4PsCbG0GZY9qiFe_sCXdP_IKHmirjfCe-OJ9HsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=GIuhf17ZMmQqslMfvAKBp1TkNA_3Romq0msPLipqJQoh9VrblYFikHfaBMZYS-uHAovy-0MtXb16KMX9nkg_zDQy0kOvs8M3wERNZp36s6GfQLK2qfD8bBr_D4-Ropf5w-7I0E5dZGvGMnXtBsVqY-0YhWcbiXm7ya5B8Nd-hprqEmVwviKSzT9oR3ut7ImIO9Hf_R8gHcI3f1Jz4hg6ozw4v4oSYZYw7A82S-P1GCh8GqYs2TKKovLCityrt5tsTLtC_N1zApE7spal9GPDzQGRY6PKVwhW5XdWLhcxJRxDr-4PsCbG0GZY9qiFe_sCXdP_IKHmirjfCe-OJ9HsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حرف‌های رونالدو قبل بازی: شاید این آخرین جام جهانی‌ام باشد، اما امیدوارم این‌طور نشود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98704" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98703">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8yapTY_I87E8RC4cdUZ3zOiKbkpHrWS5r2ATS73piPHB8U7gHVv1-68ZJQVuyjcDMoypxQFt5LZNvYpOpcgFyNmsGT1NFarPjPAlQWLaIidTqijq1veBY7Cl5BAhOK8YSowJV231H9QMOGoF11rHc6pLRLMk7-T6O0-wy_MoSZvjeh_mlVx5NADxAFDlut3VB5HE-dOsG49RY8oQz6Qyz40B5v_IUImWDPMXh9M3mFUcC8mm2BKHVx8WhydA9Eh7HHdfn0g2UvwRi-Hh5cfMIzbJTQtBGN4J4mg5EmIGdFwvSg7zr_g8BcSJ947Yx-1rkbN0Nj4NxR1Eo2Jt7ZDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل میکل مرینو به پرتغال ، اولین گل اسپانیا در مرحله یک هشتم نهایی جام جهانی پس از گل داوید ویا به پرتغال در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98703" target="_blank">📅 01:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98702">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjm01ODky-ZoeyEF4XDspv7IZF6tWf_KR1jO7EKxJxeNgmV-ybfB3s3MtSLmo9tI-ojGPJsCvhN2JNcZwc26hhKbHfl243KR856KUoO-J75zaBZ04JnN1-Ka2eonKINlCtdXFPQFkSxMFIF-lNs0fjwoVNdd8marXYe39JeNQtEEU2VubKOiB3QiLBmYSPUf5xck7i4z44nFDA8PL3EvbfFTDs_Rxrxt-Mr_BxzP3qL2gr6mQvxOySqZTlvQ8kFqGQdre0KfIR_Mv6hR8Ue0S4JoUJ12e-CBOY0DojqhMSi1yJqmqW2xxHmSujArxgUQbU_tcpsRhAlhu1HohPamlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
♥️
کاتیا آویرو (خواهر کریستیانو):
سر بلند بدار، برادرم.
تاج تو هرگز نخواهد افتاد.
تو یک غول هستی، تو سرنوشت‌مند و انتخاب شده‌ای.
تو فوق‌العاده هستی.
از تو برای همه چیز سپاسگزارم.
از تو برای خیلی چیزها سپاسگزارم.
از تو برای رویاها سپاسگزارم.
از تو برای شادی‌ها سپاسگزارم.
از تو میلیون‌ها بار سپاسگزارم.
تا ابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98702" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98701">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XyI6b1M3pnnG9iqrw7uSadRZ5TmwoN6UQyYFy8zF7q0KS9DXFjp2IVi7vVQw1foEXd0-FNsLXV8qXyDsCfN1ifZHsUqWhaZBnYEiqkMmkeW628KdlJH2cMJ-LVYKb71xiGAyJySBcLTeX0N1SteqQHO69VZm-07-Jd7jVUz5XLD56P9Po-muQmK5xsoFBEOP-d2Ox0mZDkHir_Iqt9LxcQ2GGWVSpXeFQssQQyQkPzfb_x2vA-aMM-WFZeQ2PzpONHGFIpe34mvUPpGQNEigPIaFcb9Y7onoqIKI6bnPdYxLwK0CbH2Ygh_S0aBBbRNAH_X-76KaZTRm_u4upxRGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج بازی پنج کلین‌شیت
✅
خانم ها و آقایان معرفی میکنم بهترین مدافع فعلی جهان پا پا پائو کوبارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98701" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98700">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AheKQtwAJ_f5RktldDfYRjMCskI7ljAycNlkd-ujLOMgd389UQNO5dT1i8UUdOc55YAAyRC6qTBB2Ti1XYHupitHnbRd2UAyUo2IsT9njPUl5XjowcUYSP2uuz0viTPerAhb7wEG66F7LuLV8RM8S2J7W1L760WbjH4zrfTWXPVF-RFi_pTNGUgBQe9s5C8aYJhCnJRnsUN5eGvCQVleFJFcRGP2TBgc_WmT8l9vhSIGuL1SSZ-QMVVxZjPMV_sfcYzEO4hDjcAU3XFRJKSpI2JLkK6GWQUc7Jg0qmQFxq-tqFcDE86CLecWoKlNxChAUQ7OiNubLA5LvmRgY3KuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙️
رودری [
🇪🇸
] :
"از برناردو سیلوا بابت تمسخر کردنش به خاطر از دست دادن فرصت در آخر بازی، عذرخواهی می‌کنم. اشتباه من بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98700" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98699">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZCJESf0W2jJCeNUHMokhIvWQKZzhIAyCgtcxuHc3-swqVGk-eisdD1j42krwfxCsIDRW_OeeicqqSRz-qrbr0WX4OKHVzHrrbtC4YLSBu3YnZbMY_R-qTvvykkx8a3-PrPZ32zH94jPXzObBVB-gEURPsLa8qxOorxaRVZJMQUfPm2ZoAe1qxZ5g9Kxr61Hpflr3ifMuBN0wdJcexj3vjoI02lzFhlJ_eEEPQS1a6SKSBb7bzCMTsL4oY-BW89ykPLiE0plATOpKUlZIyVg2AfhlLNe8hi_Nfa1CBjUJ5Sg3wK4GdLvOYnu7DlPzjMgGygdWRiSDUbOmEMzZjJCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
و تنها یک‌اسطوره همچنان باقی‌مانده؛ آیا تاریخ را رقم خواهد زد؟ برای گرفتن پاسخ کمتر از ۲۴ ساعت صبوری میکنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98699" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این جام هم مثل جام جهانی ۲۰۲۲ به کام بارسایی هاست
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98698" target="_blank">📅 01:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98697" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUwhY21Vcls9fMV9tceF-hYZCAva-9UKRowM2YTCWyzHU2P_4h2BUihoeUmvPBmG9SKnclNUYBFsCWo9YKdToFOG2rcQcP4GzjrAOokUWxirGuDEOYw8pcfFcCYkRTvsI1nJckQM1mtrnISKOsGwClObgaD9spHdwrjo6wAgZ5cMscNzwz5-p5p2gYC2UaMOi9DBJ9I8BFMW_KN07qKQq8EPJWwG0BC6ugwQNW25Y_PF_PwCG83Wxga5NaX3LDE5Vg6dTdfHc7I8Y6j1oex-zzemLac0okruSqdMuYtWjagRJSgqkTSuyd-6Hqk0qKuRWSofaRSgTXpm7XTYS1fx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
سجده شکر مدافع پرتغالی‌ها پس از حذف شدن از مسابقات جام‌جهانی
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/98696" target="_blank">📅 01:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7-Z6gFImBuO6YAubSyRNE99aB-onV2uUK2IX5_VRPOTyZD_qi34afvkhNNdJXrgHUImhli0971hSdeof5_2r7O-SikTdEn2cYqMNUbHqOicpVkwBFkuEOmRO5tNrPUum4CZTmzBT5vqzyMSSTStEPdw9-2bVvpJuMAexg69gcT_WT3oU_oTyFcP79zjd7tUv_cJ6g-1gd4z4WBeGHjre3DUsHBZ_K68bsRBYFfzoag6XWmzhgeMA_T6GRMIlLDnB3ZSmcXah2Gz1jQGcmaYl7FbUKZAB30CoLeS4JStu6HX9_QUOnCnT8cereRZZHvBT0i-gpABWEFNqm9lNm_7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
تمسخر پرتغالی‌ها توسط مرینو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98695" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWg7ljiuTfnNeKKgepf7Z9HUXelkvGfKTh-pwbND0O-bywZDWkcU-KjPHgtSGm-wVq9789Nj_iFt4nVgI-cBX2RXzgkOx0gnEzUhl4gqAzOnZJO4p2Qm34pEDlmklHjrYHnOwwbbts3GwpoXwJH1E-mq6Yu93LMu8XHSAeM2XDZMlLuMXHHZfzcJBKj_PbMDniXnsmf5Hs-DIrDPBfYvRjfNdbSHdE4_5zQrxRkPy739Vl8XI5pcMFbpMyxS1pHQ9lK1T0VjDAaFiEWMJW7jAIROSiKdE4TPRgJNmslyYH9867uKjAsp5HTCvr33yOdP6N6ef3mOqP_tI-aAHDF_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
تیم ملی اسپانیا، اولین تیمی در تاریخ جام جهانی است که ۶ بازی متوالی را بدون گل خورده به پایان رسانده است:
🇲🇦
مقابل مراکش.
🇨🇻
مقابل کیپ ورد.
🇸🇦
مقابل عربستان سعودی.
🇵🇾
مقابل اروگوئه.
🇦🇹
مقابل اتریش.
🇵🇹
مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/98694" target="_blank">📅 00:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=QyGCT248egWf7zn96uGQTm1RbZLnNxV5lBbcGm66pTfRQZPRKF-ud1RlSFkX_WJVjXgAL9rQp6zMP_oPVlD9TWM8fST677be8COqnScRsafVthyMC-_qmClNLX10z3IcraFQHq3pL_sT52yeQKKa-kV8SPZsUiyFC1-YMILsbvcedRTBvqiTJECEHYsTKgW7x3lQRzhJKWlnLKTv4kDjzAgIJw7wFc05aDJIOZyYnE9oZkghMN0l8SncnYjDm_6Tffyj5fzxH51kVS_euYDE9YvQa4f6AlLj_VY31b-B5KDtNPIds-AzrLHxWKhPi0Mze65vfkrfD16a-YHgFk0pOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=QyGCT248egWf7zn96uGQTm1RbZLnNxV5lBbcGm66pTfRQZPRKF-ud1RlSFkX_WJVjXgAL9rQp6zMP_oPVlD9TWM8fST677be8COqnScRsafVthyMC-_qmClNLX10z3IcraFQHq3pL_sT52yeQKKa-kV8SPZsUiyFC1-YMILsbvcedRTBvqiTJECEHYsTKgW7x3lQRzhJKWlnLKTv4kDjzAgIJw7wFc05aDJIOZyYnE9oZkghMN0l8SncnYjDm_6Tffyj5fzxH51kVS_euYDE9YvQa4f6AlLj_VY31b-B5KDtNPIds-AzrLHxWKhPi0Mze65vfkrfD16a-YHgFk0pOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال
؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/98693" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4ohLNhcYaEbHkm0_eI0bisT7KzVeBTeCoK-D-vj7vLe2OvaxQZ_6hCUPDZDdobey4MhiB4-_x3Z4FSIW1TNA1IOSNgq38vRY_cDmdywj0bnuIBYj7RVQhF1jzyZ6RUlbWp_3An_ly7gzqwqc2zBsvdjqLCaPPx6dusxR-_jxOIbU4HItaSmepmG_txjxf5EEm8SKntU-DLo9NmBhP6tPNkVH6jPSOM1rpCXCBpvo1Jy_eq0TzGNQT0WJZMw4nTGAeDqqdzPSE7OOP6e-1_tj8m_C9K7wmOOfmaiYx6OdSrKizdniaGEgJ-4FC0iumjXUVAJy29DlVp0ogQ2-Wn0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید هم یه گوشه کز کرده و فقط گریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/98692" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klWj8uE8zDKTl-gZWBLXwkFIVVl8ZsAxjTurHdNGTDnwWB09NINHr9aYEZqjMDjHlVFS4P4U0Dhan4qgO-ahLBylJicD6tr776V88HvQjFC-4LPUfCaWIW_gK191DVA6UlUUNt0rq0VADl9Pvf1A_1pGengq4D8OxHkS18UAibcfqt-iDeqvKWKvE_u6bXe2H_sCUtLmu-Vhls0Dtg5i0JipkDIn_SJM1h3c1YHJUW8VKeGpySwDZDMccLIAiH9LOut7BqoygpsJj-NwS6XxTT3mPBWceJV8FWK6I4CaYOLQlC5rr0WmEbdNbjantcN3wvrwi92k_kHjdtXBdHT7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
📊
🇵🇹
مسیر اسطوره، کریستیانو رونالدو در تاریخ جام‌های جهانی:
‏•
2006: حذف از نیمه‌نهایی.
❌
‏• 2010: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2014: حذف از مرحله گروهی.
❌
‏• 2018: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2022: حذف از مرحله یک‌چهارم نهایی.
❌
‏• 2026: حذف از مرحله یک‌هشتم نهایی.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/98691" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
🇵🇹
روبرتو مارتینز سرمربی کسخل پرتغال: این بهترین بازی تیمم در جام‌جهانی بود و اگر بدشانس نبودیم به راحتی برنده می‌شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98690" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98689" target="_blank">📅 00:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=OYk1WlXmFlQlZhVw43ejKYe04m1jrWGBVkRmQ0BLNeeXc7j3_vr7lWlIFLIZPQ1OVxxw2LA1pqsR6rRBv0y-QurNogB6VdBaLov_hhjJ0bsNO_8l8Eog9rGeVKrV27S5ce3HaLIJstKgWBbbStPgmudoS9w3tFW5HOg8S4bx9iwsO41ei8neoSRrAoneWxU_DkUAC3tp1ZZcl2jMijClTuRalVXmnndS_RKui4cW1PsD4C0ok2besdiHpKZdBc8yx1bmivN6fVrwX8Q6U5wVGPydA43BwqqGMItClyW8W3LkC5diwRcvD2Jb9zQOST9OC8t5c8ncirfsrIY-cWmE44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=OYk1WlXmFlQlZhVw43ejKYe04m1jrWGBVkRmQ0BLNeeXc7j3_vr7lWlIFLIZPQ1OVxxw2LA1pqsR6rRBv0y-QurNogB6VdBaLov_hhjJ0bsNO_8l8Eog9rGeVKrV27S5ce3HaLIJstKgWBbbStPgmudoS9w3tFW5HOg8S4bx9iwsO41ei8neoSRrAoneWxU_DkUAC3tp1ZZcl2jMijClTuRalVXmnndS_RKui4cW1PsD4C0ok2besdiHpKZdBc8yx1bmivN6fVrwX8Q6U5wVGPydA43BwqqGMItClyW8W3LkC5diwRcvD2Jb9zQOST9OC8t5c8ncirfsrIY-cWmE44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/98688" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_5zYi5gZNdmU5rCEJTyPcVWkeeQ6dkhTIMWWTd83ISrhf3_ixded08zLsvWGRuEjfkuKKemv4ORXSj9-_BaMXYf9Q73Pmzitai_Sk39KfIMNhKoRKf8Y8YL7qTMkruXmOdGoScRJIr50vMLUZNHtuO9O1dBvBu-aRcNybJPpGejZ_icCCSyHYYM_H_cjEDZumepchzZhEf-SUr6TWRVjIj6DlzI67XKTGhdkV0AXK9nAMkTzRs0xhG3yHpxhrlnAJA-ScPs1zFRWATPvHYWgZb1v7fAXq87QJZYtlwNp2c_SW0eXHK7NGjRKMFWHOu7NY6u2hHZHdOVFyXzaDRB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
خلاصه جام‌جهانی ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98687" target="_blank">📅 00:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOJEl-nG1fiojR91LcY55wKebEVDucvuKk9MMIck90nohK8pj_hr9vnXxsBFe8KVdjcanp0GsH7oubpLIASunxg76CIsl2OgrxhzkYg6CROmaDI20-9bWGZ0-MKRDclF4_kPnPp3jWG3M2cidGyw52m2CWX-Mh577qDydXHSrM8G3BR4oWjG3nsHYo0J7R-WMMiwfHvHrba24jWVUIE6bpSn8l1Dzg-dm-03s9y0CAGF0o8CjvkcGQ2sEpspFM6lpugYbKRQXVNHFDj4luW0IU7m3GawCkIhg1YW9y4-msmeEWz7PiGQO_GBKl0IM4V6TVb6d28Kjwp8XIPDOu8fAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
👑
👑
🔥
🔥
🔥
۱۸ سالگی و اولین حضور در ¼نهایی جام‌جهانی در اولین تجربه جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98686" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98685" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB0j2dZiSK4RDLmyR03wMjuKroIN_My_mIngN0ELDFXqLl-DEDs0GE2j_SodEIb0OUxu6gu579HP0C2t23u95u_sAIfhx2ym2oifTgjPOnPKJB-ttRL7Is1gDIY9CxNw1czcRTaGy_cwflo4x7qxIUER4jisVwqmL6lxy6sAotBs9gtE4gpCmWWlFeuNI9Iig5HDsat3tm7vs8OizO9O80ls7fFQmLfhrTmmM5J8Gzxzvbv90nXA3e7TX2_M2L8Gg0KoHvKCh86mD5jU29daoj8XxiJ8JbDagdHi_62KENHK1VGKRf84mlWYNLU11CACbgEOlKN3PUyE0guOmUWaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/98684" target="_blank">📅 00:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsMaI0zk0-tzZbkctEAB1sEyMrjBmLx63C7XlYtrBkNRZiFqGYAckpoe--5AeZIAIUikhvJh6oxExx9wUI0McbZXVWx3VQ1kf_bwHFT9WSrrDOj_EhPiy1h4q1hQ8jXpgGQhxqOc0pxjkoTUVyyNWqGXb3ufUJOVkDR3uzJBkouYSSDKSUrjei5mtsuCyiSynzxH5tjZniwDQcDOuD2EvkOp0rutQkcyvkwHwYpZLIPYMrfSNsDlM9tUS0827GDbwtDOD3sJN7Q5gzF08av7vpTAupavfUv-BStojDtTJ5GV3hdDh7mvKL0C3oXK7_PgyyeSJIeyzCSK9j5RgdWW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
💔
💔
💔
بدرود کریس؛ تاریخ فوتبال پرتغال بعدها حسرت داشتن چنین بازیکنی رو خواهد خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98683" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
