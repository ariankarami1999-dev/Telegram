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
<img src="https://cdn4.telesco.pe/file/fDfV5QzbLDVO6CUP65gMTf9FmjY3SHKzVjbVZi6VKdcgbbFjoP4s6PnccnXxlivciELUBev1uzwduiNYJcQ2sh53lMvHQPCNa9dMfRfAFuMgbvcgOtSFH7H49eT9erAH7jifKi90IdlAZA6Mpd5NXvnc0BFBkcyPihddjYphBZ8CLWuLl3oXQCNEl5biIClaRTpeP0ccDkJxXTIq1enytuOEZWoLDxfl-tuIuPYEtYElKiCYjUT0GIrefyWRP8BLo8SagD5eBJ6tYgKXRZfOQivlfSI07goXTORJveLHMmjYpgmqlEQ0iyQbmZQ6O_q8jKCLdj2P_HHMPVyNgDjaWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.1K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-9144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه جمله امروز خوندم که خیلی تکان‌دهنده بود. ما رو بیدار می‌کنه و به زندگی‌مون و رفتارهامون آگاه می‌کنه:
«مرگ تو در یک روز معمولی، وسط برنامه‌های ناتمام فرا می‌رسد و جهان بدون تو ادامه خواهد داد.»
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/IranProxyV2/9144" target="_blank">📅 18:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y33fpe8zLYXo7vFlpcRNeFUhqZAxp5hN7jBHayOrFEq2caJs-HuP1TyA2sTX_Cs4Ne8c3IxHAvup5GqFJgFLwuMHUbuXFjhX48PRG5uogvfV2WBhWfQUiHLv91POeokSnemOMO14ziTNSVjp7MaH-m5ksTLG5EWwcUQB81xhICFq35Ej1H6gmbS1SDVmW1WyDq28vCH0y1MsvSdOuELHiRGjuKsYNVFsuk1Vin-tYCs_TH9seQAs-Ch5VKF4L1zeeODO7cvO9WKoibK7nhAsEkalshBow4TbvDswHCziPjyd1IENJVIoL8lWm8SPst-xo0XXg5h34RgVwDLQhxpgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور بازی جی‌تی‌ای 6 رسما منتشر شد و پیش فروشش از هفته بعد آغاز میشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/IranProxyV2/9142" target="_blank">📅 18:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9141">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=eIAAS656aM_xV-mn6Vf_aJLozqDNddSa7MEexdFZ8oBrW2HEm1prLhQNvIC157_fPTrRQr4papc--3GbfQfo9nNc_49QkggSPKyWmz1dAtNRTXZLPuLjF6kGYeKXkNEdV2NR5n0djTBTv0n0p7KaP-TMs4enBlRx8ooWfTmPi5dYE9pRPyyPUMjYqpmTtThi_hpCvD1KkCFSTsgpyAETpgSmJwNfi2MP-_hlgHz5dr6Ic9NvwCcDj_sL0pIPV_x5LxBbB7_qGJHRgn7KDJxSf4hobL3R_jMmfvauPFb4sn2s1YPv1agrKVIx_UctzMWRYdpE_GUFp-5BmVzDxdCVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=eIAAS656aM_xV-mn6Vf_aJLozqDNddSa7MEexdFZ8oBrW2HEm1prLhQNvIC157_fPTrRQr4papc--3GbfQfo9nNc_49QkggSPKyWmz1dAtNRTXZLPuLjF6kGYeKXkNEdV2NR5n0djTBTv0n0p7KaP-TMs4enBlRx8ooWfTmPi5dYE9pRPyyPUMjYqpmTtThi_hpCvD1KkCFSTsgpyAETpgSmJwNfi2MP-_hlgHz5dr6Ic9NvwCcDj_sL0pIPV_x5LxBbB7_qGJHRgn7KDJxSf4hobL3R_jMmfvauPFb4sn2s1YPv1agrKVIx_UctzMWRYdpE_GUFp-5BmVzDxdCVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بنده در حال انتخاب اسکوپ‌های بستنی:
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/IranProxyV2/9141" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9140">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طلا باید برای استفاده، زیبایی و لذت می‌بود، ماشین باید برای سوار شدن می‌بود، خونه باید سر پناه می‌بود، زمین باید برای خونه ساختن می‌بود، هیچکدوم نباید سرمایه و کاسبی می‌شدن. هیچکدوم نباید مایه‌ی این حجم از اظطراب و استرس و بخریم یا بفروشیم می‌شدن.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/IranProxyV2/9140" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9139">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scdeP6GbDsKsQYADTpHTb69rlpsGXitA0RNuyO97jOR3vO2Yf9oYcIbWbK8tYNgF5iy9iJeifq_cxgjs8S-2CmRPCdewY4ABDKJOSaRmV0RNG0lAG7elT90AjSwWf7YZWx3wPxDRWnpn5nhV6F3BxGT7GqmktlbqFE4lo8bEcB0AQ1yGzQa2EN6v_NHdJ8v2cdkq6c7Bdwd374SBE8SHOD1orhpjCu_CMpaZVrQ-bEbwUqLjL49BbH-PqC6Ta2rgwrNkybaF-hQduIgan-WgpMGqIA4ByyWATO7SrKvO4tFbXHANw7h3UIof28iOFwfN0KiHYF4tmXl_jsqF84V-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- لغو 11
+ نوزاد شما با موفقیت لغو شد
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/IranProxyV2/9139" target="_blank">📅 16:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9138">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏وقتی پول دارین چهارتا یتیم رو خوشحال کنید که بهتون بگن ناجی، نه که برین مکه که چهارتا عرب بهتون بگن حاجی
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/IranProxyV2/9138" target="_blank">📅 14:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آدما خیلی دیر میرسن، خیلی دیر محبت کنن، خیلی دیر میفهمنت، خیلی دیر پشیمون میشن و دقیقا همین فاصله هاست که از چشمت میوفتن و دیگه هیچوقت بهشون حسی پیدا نمیکنی.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/9137" target="_blank">📅 12:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9136">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به فرزندان خود راهنما زدن، دنگ دادن، حرمت نون و نمک نگه داشتن، با دهن بسته غذا خوردن و متعهد بودن رو بیاموزید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/9136" target="_blank">📅 11:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9135">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیالوگ یه فیلمی بود که می‌گفت وقتی واسه زدن یه حرف دو دل شدی اون حرف رو نزن چون اگه درست بود شک نمی‌کردی.
‌
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/9135" target="_blank">📅 11:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9134">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWaeb8xyCGkVcLaYhoq9pRriql6n0FPbfqNfZUX1EWayGStdM4sJq_rMQgjvJtsonxCKYs7_-sF71YyOGbr4JtQKxrZe0Ds20Fq5v1_w50HdN_fREU9GWc-Xqq6pIsDJ0rS8jIqYTuE5d7U1TLtICvvyusXCLNPaLWBijUGlxpx909dvXhID0hyo3A0OrYBXF665mY5zZj6L7aNvygoBtZiKmwpvu6bhjQC2RQFUvTJaHmDfOvxpKaDJYLnb_SlSZMStnZ8qxpvTBi997VJm42fX71SnA9-yTsZLEw_R8p-PNaZyV_hcRfoCOa9X3pb9HH5_EuCfay6er89QvlA1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میا خلیفه برای طارمی مظلوم
واقعیِ واقعی
پروکسی متصل
پروکسی متصل
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/9134" target="_blank">📅 10:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9133">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرصت‌ها معمولاً وقتی میان که دنبالشون نیستی.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/9133" target="_blank">📅 23:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9132">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfQ0JkNep8NdPO4JaVtK0Eh1FupUEyHUwyF17JdJ5TzEi1yE3i29jlvtW2k4FctwO7vaaVkx5SLibsOXTtXyPsVslsjRLARa99lCyzGafevsy1ct97pRokfxS5MwdzBRn4VIMUiJLWCIh6cbwZhtZw3z4Gu5d8AtkVD9s73e5mhOw_Xc3c4GS9-35U1OcYyp16Fw1pJorbJ5gBkJstH9NvZI_D_Tol2tMHaHi4niYFgeNe3ROQ2WnhszG3EIY5QxdalP2wRmVhkAmaGHCtUyZFJPXrCyeCEzLUDiY4qvG1dSlUDZFKH3IiCQ0JHnJC3Hm6WNu9ggNNITw8nkqwJfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماهی زلال‌پرست وقتی داره میره به شب‌نشینی خرچنگ‌های مردابی:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/9132" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9131">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏اولین تجربه روی زمین تجربه ی ناجالبی بود، دیگه تکرار نشه لطفاً.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/9131" target="_blank">📅 22:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9130">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مطمعن باشم شماهم مث من بازی پرتغالو بخاطر رونالدو میبینید دیگه؟
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/9130" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9129">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏دلار هزار تومن گرون می شد
ثانیه ای جنس گرون می کردید!
الان که از اوجش ۳۵ تومن ریخته دست به قیمتاتون نمی زنید؟
خیلی پفیوزید (ایرانخودرو هم این وسط گرونتر کرده)
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/9129" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9128">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بچه بودم یادمه 3 ماه گریه کردم واسم یه
شمشیر پلاستیکی خریدن آخرشم با همون خودمو میزدن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/9128" target="_blank">📅 17:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9126">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnkTdY0iT5h7_3QGNu4VjuDTDyhtZJJioGfIUcPXIvMY7OpnBKAEWfGC20ILu8I5OACwRLDm53TY2XKHfG4nZ4NMhuN34_ljC6hs6guEAzaEKcl7tDZYISi1dCFt5iX4fO6mMnVhjJKNLqdTMbCEfbqMyknoSOaiW-_3AkNnvwXVg7YSiZc9Kb3yFJorvACSseEOr-oubSmpVFjMjmsZm2FKIxJCH4n9-qGn4qpRG5PqW1YWwNUrOGlXYLfFklAhnmvLxuH-QnOuy8ls8oF_zXC301MlPtDMXba1w_JuQZoM-dVedXElkVqW7w6NyzN4epKApPMw8epcOfIaxfqJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClDu82K0gRnD7WZxLllSsfAGu68yE00hSryyCqo30ZCtXXPWS_nLvUohZYq2pGOl7lKDXe0IDt-V3CyFLvRQe1mHK2pSG5vyy_80oVYYtRh9A62094zjIEaP-XNml0_pCgmH6rHyHXrXGl4Gsn-O6zEGzEJ13gLD-QcWoOmMPmStUjYFU6_IZJP685y9gfN27ZTspX9OQD_-inhfJMlsPzIPVRySVMrnvqGQnCVb-ukOb6iJ3vUSVDYgXYMnlWDWwz-62MqUXy52brz0vxnurG5Iea4v8dsJtw1Gh5WNEmRTpsNYWL3wVIPuB_m1n_-uvAdPXrwHz356na_jHtAGPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چین یه توالت رباتیک ساخته که با یه دکمه میاد کنار تختت، کارت که تموم شد می‌شورتت و خشکت می‌کنه، بعدشم میره خودش رو تخلیه و تمیز می‌کنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/9126" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9125">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شما دو ماه بطور جدی روزی نیم ساعت تا ۴۵ دقیقه زبان تمرین کن، هر زبانی. اگه اعتماد به نفست عجیب نرفت بالا حتی اگه لولت اونقد تغییر نکنه،که میکنه . روتین برای یادگیری زبان معجزه میکنه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/9125" target="_blank">📅 13:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9124">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از آدمایی که دلخوری و ناراحتیشونو واضح بهم میگن و انتظار ندارن که بهم الهام بشه خوشم میاد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/9124" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9122">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZ-m8cTjYJprccXhe42e4aOyzbp-BUQ1LcVf8uGARFn7vmYTxjFonk3LAgjzB-Lz2WHkYixNWcSwHPYwux1sctM2HaW94trjX-Vn4zC5oXIHqwJeitklpvlmW5kP3pUjSZdx5vB5DX1TrTJwaPiXEIevOxpiL43cOExrQXyp76uwJX9L0JG2Iw6sdHsiWYdN24gwGzja5G9S3paSy6qzhD_oBQIywK6DjW5IuwcSHN8ACHHhABoQH3WKvNUt7Fan9_RZbbAq7agBvux9sBUZP2PrxVtLPIr0NNY3lrSLygdIj7bjgaPop7N2CZpnVGRm-8bJp0FczDjgCSuJAKsXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtLkQ6v1vOCLK2HubmMDRlcit-4JC4kj9p1mvEqa0RQkK0pQsQAjijWWO2h5DZb6nPdmTmhaQ_XgalmZQ6Jm_AYjv__86qqAscHAA6xwuDoqFQHFS8Uy2XhA1igZM9G7LiuxQ4cLHYJ47uNKcj0H1GXSJphoH94vhb_W1sU6ft9jIPIhgvJcsOTdwusOBRJBzt_VQnk_6UZcHiUBTKh7jElAbJRY1GbqRdPgLjtxIfpSvhbU3RykZF1Hd2Y6E2vpoJJv5bv8xTk2dZRLbOamm2M6PTE9aBtzn8_SWVd1B3BOyrkmViu5oq1jGpNMcrO6A8uVpwZzZfEaPUWmbJRbdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیوت بودن اگه عکس بود
🥹
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/9122" target="_blank">📅 12:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9121">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">راز رابطه ی موفق یک‌کلمه است :
احترام.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9121" target="_blank">📅 12:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکی از خوبی‌های پول نداشتن اینه که همه دارن از مشکلات بانکی که پیش اومده میگن، و تو اصلا خبر نداری
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/9119" target="_blank">📅 10:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از آدم‌هایی که در رو نمیبندن متنفرم، در اتاق، کابینت، کمد، دستشویی، مخصوصا دهن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/9118" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">100 گیگ کانفیگ رایگان
✅
https://188.121.124.130:8000/sub/djMsNDAsMTc4MTYzNTMzNw2e14b71496
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/9117" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏امروز روز جهانی برآورده شدن آرزوهاست و هیچ ربطی به ما ایرانی‌ها نداره.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/9116" target="_blank">📅 22:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میشه به همه احترام گذاشت به جز رفیقم، اگ به اون احترام بزارم فکر میکنه باهاش غریبه شدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/9115" target="_blank">📅 22:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏دوستان رک بخوام بهتون بگم برای هیچکس مهم نیست که شما تو نوت اینستاگرام چه آهنگی رو دارید گوش میدید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9114" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOf_BW2q1CwqwYd5cEe7D3IPuJ7DzA-trs7B9W2q0ByQEYGamRYf8C1FBqjkZ5txoLxKEOtSWyBR-qymb49YIPHKIsw315V4tI4VHhqLxl7XzYJKWVgrfRmQlHv_WskuR552MM363UwDl8J5qiwL-IMW9s7c2V2G1kydbGTpFYnu_Yjv0f5c8kjLKAP8VRCwwtS2aAuEUWpnv5t9cq6aJKjkAs_Srbck4m9lG5GhiQMGuUHC-sdbsLY9SxVpTcvXxfnUvz7sMMCLo_ZS5Q4gyVp-v4I-7BRQOhrokfyxFoR1jXv6GzYoJestzpj-IkpxEU6FpzZJ03guKf-9Yz0jqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">﻿زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان را به عنوان مهریه ازدواج خود ثبت کردند.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/9113" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9PF93AM5POq3YuzcOPdDcE05PIuAMioqXJ1zib3DtKjBO5WoXFQsHiXOOAD9DPPI0dpXuOE0OtcbOe9F7DhfOjq3SvZiSXh0UPZAqF4YtEcCenUSF9tJwhfRqJbCHrzRsRjHZrZP0YuK0qopowOsL7c8lpr55JV1FG_-W4CBvRq-oMfs5LfrVlSOZ_dvmjSbkrZNWNRpTjPopnKBLP9yg9vrgtIQC19NwOCEedDY-x_4kyF7CMWmKitLko75tgDKt0lB2kEUVdmnQyeH0AEhutvKFYGssAAifhd3BDkhz9cORJxEGonO0ds0r-Sg8BoAwoc7RYx8lbTaiAlgz89Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/9112" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مسئولیت‌های زندگی دارن مزاحم افسردگیم می‌شن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/9111" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آخه آمریکای لامصب؛ تو که ساعتت انقدر با بقیه دنیا فرق می‌کنه، برای چی میزبان جام جهانی میشی؟
آخه کی 5 صبح فوتبال می‌بینه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/9110" target="_blank">📅 13:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سلام بر کسانی که،
وجودشان از غم این دنیا می‌کاهد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/9109" target="_blank">📅 11:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJST1-YOoQvZapR-HeqEuReXx7CfH-o0VJLflLCuxUhiBL9PbXNaklHjVslCgI-7ijQbjmSn5LMhoUVbo7hvEHJ_1jNaHEbEq2eplD1OrF0MGsshdd5-i-Rew_pbQoYgQpVQi0NRa3h-JtSIW4seiY14aykJ8T5WDPY8VK5j5B3ISUAi21_D1BzopejT8WbAfz4LCB3a8vkabfg7txfVo4A-ryGZmpXQE8rXKtJeXtanP5kRGfcFLkY3DJwFCPENTOadBSVeazrdYV62ueCl1xa7QDeUagflfKJY8WQzSSRWLKYYLlmfxzzry6Pi2z4VE03QraQOaKxgXIVlCQQuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی ساعت اینو ازش بگیره :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/9108" target="_blank">📅 03:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوست باید جوری باشه که هم بشه باهاش بی حد و مرز چرند و پرت گفت، هم حرفای عمیق درست درمون زد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/9107" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=gTaNaiCOnjP557P-nRI9r1T4_A0f9dzRKYdjBnZIFM_AeyZBVOeJZGUpv9oh8RobZP5oKfADrG97CzWQD7dEgm1iL405T1PR4M9bHKnmkifWGbJsVliqkB4MHwDpLE7D0tLaKMWmIlm0toIzMPa1wNukpXH3aWMqL_L_vfHuAvDJzOlJnfpxMEH3IetMnrLu_ugpfd_LrnNSw17X8Q0yhqnIaBTqpZV_SECLAW2kPoU0pCcdwjxWW3i4jXnsaNFmByi8MDj-MorIYwpAFk6t3vzO5BEnSwmK3OVBbj99xnHuxCNI96ce_Wq9bzSAUVv88IBH0ni1K9dYa4gt4jiYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=gTaNaiCOnjP557P-nRI9r1T4_A0f9dzRKYdjBnZIFM_AeyZBVOeJZGUpv9oh8RobZP5oKfADrG97CzWQD7dEgm1iL405T1PR4M9bHKnmkifWGbJsVliqkB4MHwDpLE7D0tLaKMWmIlm0toIzMPa1wNukpXH3aWMqL_L_vfHuAvDJzOlJnfpxMEH3IetMnrLu_ugpfd_LrnNSw17X8Q0yhqnIaBTqpZV_SECLAW2kPoU0pCcdwjxWW3i4jXnsaNFmByi8MDj-MorIYwpAFk6t3vzO5BEnSwmK3OVBbj99xnHuxCNI96ce_Wq9bzSAUVv88IBH0ni1K9dYa4gt4jiYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر خوشگله core
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/9106" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKI1HzxzGmQfHtn8-oYE-M07SpR5rFIe9dInFZjl89jPgensgm2VAX-w822mreX8g3kswh2fG1mwZj0d03FpVBBEULK4UZgO6DQEB-YwaxvzWMRYuTC4aEXi9liCi7RDF-y47OshcE8peKUnITlSTkMyDCjZTXmN5yyE09LRA7--FcsRQxpGshxPZArSs8v3WHGOPTvSY9muWLZFCMxkllElgTg8XYKT6tANgat8szyv5Fa3mTzUbf7C9-ElGHzMsbXExpVn82N5zan-ejWukjgebqcGSvR7TWcrFEUUYp1WkxiiLx0exTL-PEAMx2X7y6pWBw_mRRqWGNarim7t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/9105" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تیتانیوم 94.npvt</div>
  <div class="tg-doc-extra">52.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9103" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/9103" target="_blank">📅 14:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.183&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/IranProxyV2/9102" target="_blank">📅 14:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50Gb Cfox_Server A76.npvt</div>
  <div class="tg-doc-extra">7.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/9101" target="_blank">📅 14:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=194.120.230.97&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/9100" target="_blank">📅 14:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTgmS4pNgZQehc4vbhF-0oS8vbWDTe3nrX1GzYuul4_hDxoGFBIa6MaYWv5U8ycpcB1pegZucH7_cxfe4dMJxX7HFTjtBx3-h6TzyWgqAEEzPJtizVTn328-WOI6Xm8gSmGSwzxJJh5dD05L58qdm-Is_bIw6e6Iw1hJlXhVlD5-AUguZoNjLEY8O6MUI2weHkP1a4wRGenlWLQTXlcRyTO1ez5ymX0fE5IdiC22aMonLq_XBd8AUR8f0tksbFguSA_S_W3gXF31Wk2Udo95gcdv_2cO92F0bm_rQn1n2_3DfLdGjZ_Qb_FyWY1Hl3vmwxosmr1GAB8ZD638rBvyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/IranProxyV2/9099" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=play.proxyvpn.site&port=443&secret=ee4d0c82ca73f261e6933ec36e5d902ff6706c61792e70726f787976706e2e73697465
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/IranProxyV2/9098" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فوق پر سرعت🔥.npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9097" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/IranProxyV2/9097" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">TIMSAR 263.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/IranProxyV2/9096" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-poll">
<h4>📊 بت زن داریم؟</h4>
<ul>
<li>✓ اره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/IranProxyV2/9095" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐝.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/IranProxyV2/9094" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇨🇦.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/9093" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">◀️
دوستان این تخفیف فقط تا آخر امشبه</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/IranProxyV2/9092" target="_blank">📅 21:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d3d046fa-d372-430a-8ed9-083d62c44efb@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=ssd.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/IranProxyV2/9090" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=51.250.65.108&port=443&secret=ee3a9f22462890489c0bde045048ff9a17617669746f2e7275
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/IranProxyV2/9089" target="_blank">📅 11:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9088">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول متصل⚡️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
🆓
npv tunnel
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/IranProxyV2/9088" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=zone.nolags.pw&port=443&secret=dd04d2a884220d45de24af8bade64322ac
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/IranProxyV2/9087" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ʙᴇꜱᴛ🇳🇱🇩🇪⚡🚀.npvt</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لوکیشن هلند و آلمان
🇳🇱
🇩🇪
Npv tunnel npsternet
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/IranProxyV2/9086" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نامحدود🛰️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
👀
Npv tunnel npsternet
🛡
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/IranProxyV2/9085" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes⛱️.npvt</div>
  <div class="tg-doc-extra">3.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
💯
Npv tunnel npsternet
🟢
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/IranProxyV2/9084" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🍔.npvt</div>
  <div class="tg-doc-extra">1.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9083" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پرسرعت وصله دان بزنید
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/IranProxyV2/9083" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇸سرور آمریکا.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/IranProxyV2/9082" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🚀🇩🇪.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/IranProxyV2/9081" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9080">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/IranProxyV2/9080" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9079">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇳🇱.npvt</div>
  <div class="tg-doc-extra">24.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
📊
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/IranProxyV2/9079" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9078">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/IranProxyV2/9078" target="_blank">📅 03:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9077">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پرسرعت💯.npvt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9077" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/IranProxyV2/9077" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9076">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
چنل دوممون مربوط ب اخبار رو دنبال کنید
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/IranProxyV2/9076" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7pP50plf3pHTkXpUH7muoafFVDihuvSlZ26kIHPfbZ42SnVYd_vcnBzM0DyPuMMJgNPZMkTs7-9Pimc6BgTOlzoaAsxICTShXBVAmBxl94K5Y37xZ13ME05taKRScBa2_qM0ZGEVrs1hvASEqIhgawsl0RkXK8vTJo51-AyJunihy0Nb0nE8kBzctw5fvvTCejiiOjN9WoSQ9qe-RubOHeQ83-tXNazh53mHJ8RQKHPAspjuZ9A1XVgJKONK-SyCEUmib9CVrNHjWVavLteP4O1_ChkBumEOJOxss8zQBvTp9JDB7HNQAMuM10ac1_hquixVe1Jb31SssO27bMMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اختلال و قطعی نت بصورت موقت مارو در روبیکا دنبال کنید، هرمتود رایگان متصلی که پیدا کنیم براتون قرار میدیم.
🔴
rubika:
@activityall</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/IranProxyV2/9075" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9074">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=157.90.171.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=178.105.50.21&port=8443&secret=dd104462821249bd7ac51913020c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/IranProxyV2/9074" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9073">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=north.nolags.pw&port=443&secret=dd9760e74174fb9717de21cc7e17027e34
https://t.me/proxy?server=87.248.129.226&port=443&secret=FgMBAgABAAH8AwOG4kw63QFgMBAgABAAH8AwOG4kw63Q
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/IranProxyV2/9073" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9072">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
احتمال اختلال و قطعی اینترنت بالاست
کار ضروری دارید انجام بدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/IranProxyV2/9072" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9071">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/IranProxyV2/9071" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9067">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sInY4MXeKuRYQeCxi49VbXSLPQFCz3MlQ-XExBDglnpONhgCdTqha8_6Pp7gzOeKSjTEdrZDMbrS_63UJU2lik3AKvdJEKAMSmqbHNXR1otDZGLDjRT98G6FNXJZgFkMpOpEZsrb-07P5ntNDRNKLZ4QSMt_-1OI4BcMLqqU4x8HZiTsYTA79lkjL8ShYNVbBYfITi-9nF2LgUCB0IUrODDZMGZc4tMGSK4Yq6OJErF5gwcrkjjqYU-VqDEqwekPD0XWCLdcwXwZkNx0p0mjHe9QrtSu6ZfpvkXPdazSOe1ENxRn51DdpSKC5xSSXXXzH7nMJOHg2DVCt00sjPWynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/IranProxyV2/9067" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9066">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تازه نفس♥️🤌🏻.npvt</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🎁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/IranProxyV2/9066" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9065">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت قوی🚀🔥.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9065" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/IranProxyV2/9065" target="_blank">📅 17:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9064">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیک ظهرونه.npvt</div>
  <div class="tg-doc-extra">17.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/IranProxyV2/9064" target="_blank">📅 17:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9063">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐕‍🦺.npvt</div>
  <div class="tg-doc-extra">6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/IranProxyV2/9063" target="_blank">📅 17:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9062">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری
-
ترامپ به فاکس نیوز :
به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/IranProxyV2/9062" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNir6v3UmjJLDPBrPRAqODY51e1gtPHpDWJfOO8NDMdTJhrcAkQFBTnJjr0Fp6OcK9dOpomyFkKFRHUUa7WIXOpczwvWbYSvihw5r8P_0tBYyjMAl-esaRGnJocb8BrDqLKJeK2NoA-IX1e2_RbHFpo7V5iUil2ww61Q8Oml9Bc1k_QqDTOPeJbX3-yZRTaFBTboNvTW_7eozbxsxAQWM3tQvmJGxsBKxPlNB9hfL6wbAtDE94q_wQpWXTzunJxL6r30XweyEJpIowPyA1JRsaEM8FxFP6Wew-FudTchuLcDDO-OCbPHtyiU5xC_uK9st5sLG3ak3-SqeGH3X7tuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-
ترامپ:
«ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد!!! آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!!!»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/IranProxyV2/9061" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اکثر نتا وصله
🍸
✅
vless://9dbaa630-c895-4883-aa8a-20e8a48ff4b2@fff.oakcup.ir:2052?encryption=none&type=httpupgrade&path=%2Fapi&host=Ip.oakcup.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.193:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&mode=auto&sni=ssj.new-persian-song.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://0c09799a-47ca-494e-a50e-828632ef9d81@199.232.78.159:443?encryption=none&type=ws&security=tls&path=%2F&host=bazaryabab.global.ssl.fastly.net&sni=default.ssl.fastly.net&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.162:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&host=vi.mojaz-persian-music.ir&mode=auto&sni=vi.mojaz-persian-music.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://07dce2d7-9849-4e22-adb9-36d2763c3b89@snapp.ir:2095?encryption=none&type=ws&path=%2F&host=api.aramonlineshop.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@141.193.213.11:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://cabbfe13-038b-4dbb-9c45-5079c829abfa@167.82.0.1:80?encryption=none&type=ws&path=%2F&host=max-gb1.global.ssl.fastly.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://8dc7722c-2767-4eea-a28b-2f8daacc07e3@sca11.myfymain.com:8880?encryption=none&type=grpc&mode=gun#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@89.116.46.68:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://44b3ee72-cffb-4d66-ab7c-3138b9bdeeef@54.36.162.217:443?encryption=none&type=tcp&security=reality&headerType=none&sni=speedtest.net&fp=chrome&allowInsecure=1&pbk=upTVUrc_t7xF1ULni8pHRDhRES1sT4BDm1r8rugTzyQ&sid=ff815f58c7e77aa9&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e4e7866d-920b-4a53-a8e2-6ae9b2a42fc2@47.77.214.201:10035?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://ae852d97-85f5-45cf-82a4-254eba345480@144.31.131.33:443?encryption=none&type=tcp&security=reality&headerType=none&sni=cdn.cdnjst.org&fp=chrome&allowInsecure=1&pbk=djH9iD2QV748ocK-wPH7HvDd03lu88zHhS4G-61w6Dc&sid=a120&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://d3d59da0-31a4-45da-bf9e-373c6ab140db@62.60.251.131:45656?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e0de62c9-f317-4275-b7e5-8da7b7fa9bc6@77.110.127.191:9443?encryption=none&type=ws&path=%2Fpourya#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.192:8080#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/IranProxyV2/9060" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=45.32.233.182&port=8443&secret=dd1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=mercedes.nine-gear.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/9059" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
♨️
مهر:
شنیده شدن مجدد صدای انفجار در جاسک
✅
موج دوم حمله درحال انجامه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/IranProxyV2/9058" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
لیست جدید پروکسی متصل پخش کنید مخصوص نت ملی و شرایط عادی
🇮🇷
https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d#proxydotnet
https://t.me/proxy?server=protocol.fast-mt.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=free.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=172.65.104.042&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/IranProxyV2/9057" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
✅
tg://proxy?server=5.78.53.137&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=5.78.57.102&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/IranProxyV2/9056" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=rec.nolags.pw&port=443&secret=dd0603553657b3f54b6bff0d3759e8db1d
https://t.me/proxy?server=5.78.59.193&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=office.proxytg.live&port=443&secret=eed604acbe90be65ddf34629f1e2234f7d6f66666963652e70726f787974672e6c697665
https://t.me/proxy?server=feed.proxytg.live&port=443&secret=ee7c1dc73472aff6b273c603d9713900d1666565642e70726f787974672e6c697665
https://t.me/proxy?server=87.248.129.222&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/IranProxyV2/9055" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9053">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پروکسی نت ملی میفرستم حتما ذخیره کنید داشته باشید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/9053" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9052">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مث اینک این دفعه اوضاع واقعا خرابه، از اونطرف صدا و سیما میگ ما نزدیم، از اونطرف آمریکا میگ شما زدید پس باید ما بزنیم، فک کنم آمریکا میخواد شروع دوباره جنگو این دفعه بنداز گردن ایران
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/9052" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9051">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پروکسی فول متصل،ذخیره کنید
✅
tg://proxy?server=5.78.48.55&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.42.228&port=4455&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/IranProxyV2/9051" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9050">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
تیتر شبکه خبر :
حملات موشکی سپاه ایران بزودی...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/IranProxyV2/9050" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9049">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
بیانیه جدید سپاه : حمله شرورانه آمریکا را بی جواب نخواهیم گذاشت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/IranProxyV2/9049" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9048">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به لبنان که حمله نشده جمهوری اسلامی بهش بر بخوره؛ خاک ایرانه دیگه، مگه مهمه براشون؟
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/IranProxyV2/9048" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9047">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حالا پاسخ ایران چه خواهد بود؟
🦦
بزن پایگاه هاشو تو منطق بگا بده مشتی
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/IranProxyV2/9047" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9046">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/IranProxyV2/9046" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
صدای انفجار در بندرعباس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/9045" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9044">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u26nOrA-jfEF1xLH3DvrNE2OrFl7ff_FS966CA5dyebWfcrJkV3RkGwFPUwNwSg4mfonmbEWPBI2drgj5kexl9nLquEDIVxehrxxcSaH9t5jmG-DrwdcQEP_ysIsgK3iOfiKo-3f24OgsLFSdmVSlIc4qyf80ldYYZHgoqUGHZW6meh0nh_rld2bMA2PGfUDV5F-oKdplQGHBLYW5-hSbdZGu1Fk_ZoX7YgHtOrWQwAMNe66mtsJuC6Yj9NQ54aLJCp8xuSwm0bmmA3nj14vhCrR9oxUnUiBOTR_iXiQOxBdSEk-4QyhWEk3a-9LfeF2fb6xJ2mkwa-dfKS5u2sNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/IranProxyV2/9044" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9043">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqY-hLhSDjvHY3JQqCm6N7QUDE1axh3j6WUge0rLdqityzwWdvVN8zafgTGl8UTPR1YbXeSQmh01-WWkNFClFsinlL6GP8lEC8brtT8nJ2OB-jdSb_xmGt4mQZDwdM4dzRulNWGtODweyjBlFXFy3xDeQEAMv_wXxoq26DPZKerJdvsUz3maLiI7KlVD5khB5qiUH0ikiwhD5xBt0IhRupyvkWzkBx0r8lRC44KLGy8CxUqqJeknTYIQ9HrpdLl55TxlYF6QPXic2KCpFiD2u3A_ADSHqjfTNyiONieBJH4GcYvY3SR02CAjkyw7pkb7yZVc60M607tyGZU85BOdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونل کردن ترافیک ایران به سمت کشورهایی نظیر اذربایجان برای باز کردن سایتهای تحریم شده مثل ChatGPT و Claude بدون نیاز به VPN، باعث شده که ظرف مدت چند ماهه بعد از عملی شدن قرارداد انتقال ترافیک، رتبه کشور اذربایجان در نرخ سرانه تعداد پیامهای ارسال شده به ChatGPT از رتبه 44 در اوایل سال 2025، به رتبه 6 در اوایل سال 2026 صعود کنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/IranProxyV2/9043" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9042">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=5.161.143.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/IranProxyV2/9042" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9041">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا :
دیدار ایران و مصر دیدار افتخار همجنسگرایان رنگین کمونی خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد. کاپیتان هر دو تیم الزامی هست که بازوبند رنگین کمونی  ببندن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/IranProxyV2/9041" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9040">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PILkza0gwGRqe3hUK_NLqSUHt3lq92Gh5ZRPa7wvYQ8Cfm1IPU-jsmMegOSbDK4LS3RXI2sG2j0xQ_fKJ7escGWUUN8m1cYaonWc5jbF2BOFheo9k8VCvC6CZIvqZo0cJIjGxVr_e2Y08ODQmoLa3m23dw5th0EiwgXo4gmlEcaQftJL-71P5dSmydk65xV0RHBzEZEPrOSXnBdEKLzIY5w240wyFBycOPGGGD1Xz5P1JSP0tsdkpvL6d9KjT4HenCuYilec9PpnbtbcSpJZUw62Ezxq-7LEUrngEMeHq9KhzIUgRcXZGShYU36ykU6M_AiG7NO3_QH8tyvMzgx1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/IranProxyV2/9040" target="_blank">📅 17:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9039">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d4eb1900-6515-494e-85c5-306bb9594f56@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=vo.new-persian-song.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/9039" target="_blank">📅 17:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9038">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://10a6b923-e349-4594-92bb-d81a6245aaec@172.67.74.10:443?path=%2Fdownload.php&security=tls&encryption=none&insecure=0&host=sertraline.adaspoloandco.com&fp=chrome&type=ws&allowInsecure=0&sni=sertraline.adaspoloandco.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/9038" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
