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
<img src="https://cdn4.telesco.pe/file/EYo3rECzmFgeu5bQegqTKwHGqgDi9AGV75QXn6tPePOdSGOdbdQotiOnA8__5OKiW-pyzolBVu__r6thCEn8kM-02XFockqheAI3MFI2iYw3IhZyD-WK_B-O_7ah3IwC0cxsLQrHylx_2kyvSIJKXthSW0CatPHUz1lBG_rquKP8Qai7Lmz3MwCzS3-C_Ri8PM-3TRjyc5tAYXKtYw6y3AhD5w_c74bEpu6iHx-J_F8SE16tL9hz0zYFpk8BXUAQDaNxDjNTFSYWi805ohKozsMGbwCUQVvu1TEqJsbIfntvk4eCzcw29J0zh9NXFfRPTByWGDKz868Yqb8c4-Bttw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 145K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 05:42:52</div>
<hr>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnCPifdarCnk_f9J0wwF8MyrOcD2U0Gsl5gfLeiZhC5Fs1Z13xGxtAgBQE4HdNjrAHhIRmUGDrx0oWWfBQvWG3-NpBUS6LiyNvnj4AXb-eUSpqRT-uP9OK4GET9gmVaFHMRpaRaE2jA4cFmrp5vS_rmKVFMqbvPm365mgnbyi_EklUjCqWINXtdqgB1e-fDlH-5vu8K1mGr4mbGHi9_ZEmVXG9DGNSuNWs94V802tYYUn4tF_HWz6E7DHX2sv9x7Ha3vxSnyFHnovW7HAwTXTksMPG4iwXx00JNy367e7Ez5jk_5eFeUUzubQamU8c3rDV--VBtYuvbUIzhKf-B6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GuiKW4OG83ZY5bTNCygiKe8jfEZf448TsSDF9oOMvCwxnkgRnyc1sEOzAYMv2bDFRdL8uluJomkuFc0YGMdr6uAEJzwKZzGq4ryDSDSyI1GehP0FkTXkK_f-ue3HOBO6KEIBIl20G_zAbPjS4x3VzrxU2B1PF72bFx7tbnNJoJ0wy81PVCYjPwNV_vUht2676oxEUREZ8Pwcal42lbR5TMVl-8csUfqAuLt9vpwT2W5O6BLT6JvUbcr7LCJo45UNgJ9O23EUgHGTmJUuV3tk6pg1r4dYm-7o3EoTPH8xWDjJ94pkz11irecugmwhx77oZ1FhcP9BYtSqbXjU30rFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=QGeWEophFHLJ4TvY4dPrfTvUQjxq8FXpFEMndPahLi9XGLEqpSsm5J-HC3Ry57lCaswrVZKX3CQR45iz5rsgI3Z2DT30pxLdA3JHDXGibVAKgybh9SwGn0D9Q1ldn-0QCglgsjtetkPqL12P_K9IJwlZPk0GWYHUSg0XoIpPh1jov-Q93rIXVOGYoMJv2xHilDqSPyyYgWrouo1IbtEUsMJpfCXL0UOFfMoohB3FzCxf7PAc4AD4DUbHaFjjFG6fwNG7-ffuVsuMwnXFwJJcEjc-Uh0DJoch6m9CARsSki5NTwk-MaBjVNd5ZjZz9ebLpOH4jzIOFU9uQf_A3xqEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=QGeWEophFHLJ4TvY4dPrfTvUQjxq8FXpFEMndPahLi9XGLEqpSsm5J-HC3Ry57lCaswrVZKX3CQR45iz5rsgI3Z2DT30pxLdA3JHDXGibVAKgybh9SwGn0D9Q1ldn-0QCglgsjtetkPqL12P_K9IJwlZPk0GWYHUSg0XoIpPh1jov-Q93rIXVOGYoMJv2xHilDqSPyyYgWrouo1IbtEUsMJpfCXL0UOFfMoohB3FzCxf7PAc4AD4DUbHaFjjFG6fwNG7-ffuVsuMwnXFwJJcEjc-Uh0DJoch6m9CARsSki5NTwk-MaBjVNd5ZjZz9ebLpOH4jzIOFU9uQf_A3xqEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spuhAek_num7ppPiLmmI2sWkR-BT4IKNnDdxOSinr-7r2VX-tNdC1W8XS-88KiBE9OdUSicjaB07I2AUMMn8r5SacHEshgZlG0ADUASgAOSAJJYjrDXosah6vFrRc0HNn_waZUf4K4rnVRdMgAfSBRpAS2dQvRW65_iObcQCycpqp6SIE609zwE6Lszy0KqVPQWvhnX5vjYLix-6lV3s7sQRaJP9dcSGuPY3rcw3f_1Gr0rLtO7mfmPCIp1Wcpfx4PxXAq5rdPrWRT-dH6Pi1HYcYAQdq0TVDB8USyHrND92d0Eq8AKRKDbLAMiW9UIISivpmDqUIUk1zgGBI7Vcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hzt37atdxyukgfCCM8gr6hfna9w3YR8z3VML81NbWYoZ9pJmJC8_i8wRzN97fPRP0bdzmamra3SywTtTO6nVaFdi2DagtisnFab0z0mXTEDA5NlIlp4S-2pZR8BeRIthyfbfIJAozWjrRVYuv7vSVffuxYt6FaPr_pOiHO1LB3vky7mMKX016yu68EtdvEE0YfAnKiX-lSvPTpS4Ppwu9Rj6Dkgrt9b2F44g06gc7p9vpOoW7lZQ4dygYnCo3WKa0t2ms95z-ANRsQHy1BbMhHwqQ2e9u1eeAN-3Wrb_9qpEb1HxGz7UgTEZVcwS_KX90NfaM7USMUlUFizEzFCDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3dE6mZLc3UD8ZK_qqflo-uNH3gzfqjRdmVjDynKsE3qgnsg8pj9AQcZ0TkxbrRFqY44FXzXtjwKlbLorXZRuRHnquoKntwTa4_wA6cmydeXEtRpXqqRHaMWSGc3mVoh_CIykdxitVMwebCXnX6JVXVXeemste-Be_7ejPPocLM4mWkHk0J_QYgCTt8NjbrMbxXTzRbiPxIMVVxy5e1jjYV-M411snM0LlLpNlsixhtuqfAUMsn8SlqBdAOujxHJhLWdI4D3Hh7gmioFuNLOiO1tmvy9Yl2jOgbsVnkfmNLtn5qRXjh6Fl1iHKeEeZWRWmrxzey4gYDms7a_ljrUNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQg-iLgq9qwzpHQjrM3uwkmeWx1dkvCMY13LE82S3VmtLACKNg50BwNufzgOltICN01qFNU0AM4JHdL-AxXkv9mKxz6W5zRgSoOhuI8Xr6-dx_bLgoPAkSe5NfWqbVbv5FL5w2LMIoQa0qEREypscIL63_ljbe2VmbweqrdeQnYUJDp7ZQNhPeOwWq_5nN3qwFQszhR30ABsfjBDRG_Y7iXFofGMhXIUTZgh21dIjtG5HShGAyF0jYOv3hfZ-11H3_HX7rJr0avAxb6j2XcDpcm_WVN2xMH766icpbvoJ1Z3GX-uYk6tPSYQ2GenAvWgBVQP2aE4utvoRCHF-AvYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=IQKcjBt_RdyJg9574amRqlcovkau0NC09p7P5KkGPzBhTB9G-tKUzjVHhSW2E34NeH_VIiNWPEOUiN1E_UT5e7P_cdw8lBfrkAAjnsGTftBimZAvJFpBPH9XbRVgK2g96vRUSAPmHOZ8WMWXn447ZCcmyfwydqM85lDGGu7siG-HN20aHTTNt3FGSq3PHDgKHeC1yde3gG5nHPIqw2YX267kkjwkEVeIffM2XWUEMSwuLp_3eW7kaV-cRfF_Jpaj1kI5bOE7mbDwy7oS_1fxKRdmn3sliCL0IJVw_DEDF7QdXQEtxO3kfPh6Unbvzgid4_fPj50XVvqKWPuy8e-qUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=IQKcjBt_RdyJg9574amRqlcovkau0NC09p7P5KkGPzBhTB9G-tKUzjVHhSW2E34NeH_VIiNWPEOUiN1E_UT5e7P_cdw8lBfrkAAjnsGTftBimZAvJFpBPH9XbRVgK2g96vRUSAPmHOZ8WMWXn447ZCcmyfwydqM85lDGGu7siG-HN20aHTTNt3FGSq3PHDgKHeC1yde3gG5nHPIqw2YX267kkjwkEVeIffM2XWUEMSwuLp_3eW7kaV-cRfF_Jpaj1kI5bOE7mbDwy7oS_1fxKRdmn3sliCL0IJVw_DEDF7QdXQEtxO3kfPh6Unbvzgid4_fPj50XVvqKWPuy8e-qUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxP1mlYTdwMFb-KQOC8B8PPPFEE0VPJZTJ5KEsI5T7YPq_Oc_3opUOIMEPu-b5TZcrAooB1D8JHDATO5b4PUZBPIkRjFJ4bSgRxTwjm_WSQt15RkTCBGhiXrNO6D_Na1Vxyv-r5Z7ZfEWdNBkSNhD3jioN3TjILSekf5ZjzvwJOXIEx54whJOhvN1w-K3cjPr65GsbCmnvY_FI9fN1DNeO_2FXRVQXRKgmCJYhsbZ0xd3_ZeK9M4wntumY_Yvbd594e76QQm1YYpdsJPGKJEbOBeCPi_a5mxH1HZVb74-KzwEH8FY28HEhW5J0vDx1yKZdTQxxOtVSN8dgA8I-RTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZJeEnUqln_nvATSy6JQutsx9cxWN3ieAaY5QPocb4_qeuBGSxzqkqLxejrFAf7zo6vuO43n2aHlSwkxqKoBE73a0BNLcfPCS6-Nr94981EI_Zd7XF3cfiJLFHB_vIUIS9md783J8TamRJCOZy0_ceeg-WJzSCC_ISTYGsAbmTmJ2oZ0AavHvmCjAENfa1wjmpn5wgaSs5_9mpxowcBbNQOgWbVbXdZrbv_Hp7rClJTG0RKsaxPGr5hGlpDW9QUcGIEjcYNezG4h4kfnNYJ2c3ZcQQtvpvCJjmwmpuhVd4ElhVZ8bFvVmYaHG55QW5NlbaTqEdwN0mXvXYd_lLCd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3zeRRMSaloSqUmvH81fY6SzEWQj5WbeKdHDmszy4dRkiLX2jA044pMZL4UC5VYUZ9qHAabpPziMcHnkhVhzZ62rEIagKDCKPkxQXCkHM1LfKos3DLMI9EVw1pEPP0rv5JK0COL1YULfvIAublLLPgsJneKcwosbA-0LzpCfBDC3qzEpXf0ZQ9eRfXZl53cWmkSMogA1qHLLv7Aax72LpMyMK8wpHx43DNe0mTbbHPfDk3VDiMKUhz-qpiMcZ77BJdhfTbVtgcK7_GiZIhTfUCMCm6zjiKCa1oYAKjJE2QBbwOBeLhF8zUHc2TfnqdF42FNUiFhUv2RXjL42ZSpzgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiSJyuzNG0mQ1B1ej6VNuk82ewAslTicRzmKSsbzqACJ2BPXszijNkPtLVGUd_QDZRdFYPzFnjXZLvRm6QPrCQNEAXTraGU6KtwMNo1naakQmaBkafRWLfTFDxmBYPp7m8PMkIsPUXtuZFqW5QrBAE2cv5oOgcdHOdt97lZmVPMP1tFUUIJsf9bvXuEMlx05R8HjpyWdLNB3ysprWayBSlNH8qnrvqmnk9tZHPB_45Sje6K0ZMZTtcdNOCpQEImz-nWg4Up1GuhKBoQoq_ELb6RJGOdVWjxkG9Cggu6h6s-tsfkxqCboOdQL9nWu5YLwGN_rY5MRThGYPk-Yyew4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQUmHaoYThFlAE3W-jUqaFNaywNkVFfbUMwwJ_Rkx9idYSwOvagap5ykfBQaSr2dWYHXT4OxZIuI_4n9TnX9FG9YblCRxpXxHy5rq6JDOypbxYqzW1sjvghZO0VYLMxtA-5O6Bp8JalnhHcZzvwn0IwjJetU1VCS1sBgdC3AsMQlnvWTLje3T-DNWV5bbe-RkCqDAOxc_Mk8IiRWJ2lFXPE3h8a5YTJSbDVO2uHxBIrA3Skr9J9ri_SEYyrYyJQimV_DGKw14pugizaJTBr8VJUctjVZsc_3ZdsC9DJHXYLDpkOZFdNCuSdrYR0NVddjVYtGE7Or1OKhyUuyQGjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=l8mXmpT_2GiqtRPLMtLhhpoGmXfAkXIvsWJ7qojOk5F7Qxsz_TOVsgrHLg4tMvaI4CR7uy4Iy08HYXvCug4ZjhL9iUwR1aW_AuYBIC6iSilDoKrQadlhFBwVf9lb78kmLZyk38XlkjGqJAFkhVaChdYJ3EMMOpfF5c69AQX4TvHn4QaLjZWZxO6PE78v8ZHvXpc3TPp3QlgajzHPTGPHvKi8kgpF5_7KfAY1YUhUm_J_UceB9vdswvf108Xx9E8GgAejgazveS0DS35UOOUMtoMs_DILftq965ofL6n3ZEQtgBENbV9RQ60NjCLwhmmDWgdDMwvYXAdEOdY_vI5auA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=l8mXmpT_2GiqtRPLMtLhhpoGmXfAkXIvsWJ7qojOk5F7Qxsz_TOVsgrHLg4tMvaI4CR7uy4Iy08HYXvCug4ZjhL9iUwR1aW_AuYBIC6iSilDoKrQadlhFBwVf9lb78kmLZyk38XlkjGqJAFkhVaChdYJ3EMMOpfF5c69AQX4TvHn4QaLjZWZxO6PE78v8ZHvXpc3TPp3QlgajzHPTGPHvKi8kgpF5_7KfAY1YUhUm_J_UceB9vdswvf108Xx9E8GgAejgazveS0DS35UOOUMtoMs_DILftq965ofL6n3ZEQtgBENbV9RQ60NjCLwhmmDWgdDMwvYXAdEOdY_vI5auA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T-oKJYDFlCPD7ZtWFv3IpZpZupIqJW-MfzPw2hdEV8F3GBcJ8bN3dpNjistP1e6W2npjsbYsS0sFpzMOdmw3ph4KCC6ms8XLdkIRV8DCJlJJdwSWkIAzLnGtpc_iBuiAkppvZg8D-8uWn3pDL2PTyfwXjguRGwde3tGPhkZEEeUAtqtXChPooN5b5ZgkyGUzkEqage2kdvSX4cK-TU2-hRrBG-6OuzIERCtAE2J_Fc9wWdqqicGugyZ4n-fm_Z5URhOYTNxb8FJ0YahDeIrdUkiy9BRI7Xz9LMQKx0wVqOMpVbnjiSEopu3izw2mw0kI33wT5FPpZ3zLxuIIFozRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsmRS9qTJPfX5mVtv9Jffm9FROrWFogl_QIQkGs2j3WbxHIJWA51o21-ZituUlYxuEF3NPOsB1S8aSI9VMpwktZDW7mQVsfIABWh71vFexx63EOKvdN-a235aafO-jYxLkJ9FRB5z81DM2eoHfr7LVV-UF8Ayyp8SXfcnrrLeEFUtBZEOXRHAZqhC-u4hvgfklZ3BDTDsRQtA9SBC1m-KiAox07Xl50CrOTSP2rVWN0ruFFzlRkIyVRgVxXhVqvfFkGMJdfwvW0VBfmezWg4SJagPypXnx_XxZ61W-DnMSjt93WjUMHJd0L1miU5kcuzzZTGKgv-vSMvpm0HlnqGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Gmzuva8p5-cVj4lqpwI6d7AJjivRn23pHfmRukEVVsVkEByc3LYL1nnnpesvPrTRuIihZ1eVrb1qafsgKvz_gxmf00Tml-99IpW1MaCKjpJK0RzZDvS4zJLPykcpMEGWt8xUtCSLaQS0IzHTcubSSBFm_XgiOc7szYBigKdx80J6C7BqdOIo2ReH8bHAdh_l3K22Jdrh16Ki6Nf7pujgTb9gZBC5EhsXA6SALkVENy90k1eqXFk83lC8NN57Tmn7y6yFcp7RVDfkOlSeurUyHES6HrQb2GRbrXL8RRl1h_gJlZGHALq__7a1Mpb3wne2tTbM_RUOAHmcSRvpXU-S7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Gmzuva8p5-cVj4lqpwI6d7AJjivRn23pHfmRukEVVsVkEByc3LYL1nnnpesvPrTRuIihZ1eVrb1qafsgKvz_gxmf00Tml-99IpW1MaCKjpJK0RzZDvS4zJLPykcpMEGWt8xUtCSLaQS0IzHTcubSSBFm_XgiOc7szYBigKdx80J6C7BqdOIo2ReH8bHAdh_l3K22Jdrh16Ki6Nf7pujgTb9gZBC5EhsXA6SALkVENy90k1eqXFk83lC8NN57Tmn7y6yFcp7RVDfkOlSeurUyHES6HrQb2GRbrXL8RRl1h_gJlZGHALq__7a1Mpb3wne2tTbM_RUOAHmcSRvpXU-S7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzqd3tNoHONrRf2mEfriSc6Up3rj9XX4lFSAC63DWKHpcM67wQXdUyb08xepdkDv3WGmX7CEcM_iBl4yrkkKWmVq2qVz82AIodzYdMl-PQI4-v_Rih7wfD8P2m8egc53-yRV6b1eVUF8I5N6uFrVvBx5QoUfAw04_V90C0_mYurNkoV-ZPzTOoLOEIxfLd2oNCBvZXUoxBu_xtAt_ltU-XR98XhYxp_zVoRogGs0br9FzVBjEcamKg96AeHujaNLI6ELAT4R7D2P1FsR5qiOQOOaJIBQOLe8kpdUtmow2imFmj5IgTHVnUI--gh9k8QnWIXEOsCSey8rqOjw9Hul1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIwkcBWYDsw5FWUFYiAn1-wZZNBMvXJKMHTqaI7JdrvvV7sgACF97kk9OgmOJgqKaQSKSIvLUaJyZKkfk4OrYx23v8cu35dq57nAVQxmvrzByVtcKjm2O34WnfVUk1bmM_tUk4_VIkwaQa-uJVqq2n-MjmQ_GdjckHuEwIGUYFlPvcg0uys-J5ofd9HMCCjnJFCZfdVu_YTniIov34UOkDgshpm3LXipsxNc_7YKbEOC-5DhnRT11MLr3LIGTGS1OnaeHLDpy1c6Gh8NnfFigdQc5O3A-0rV-R9gBi-de4h7WcVUriyg8rFrhzK0jggR6MCHWph9bzgW-ogPEwTQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVikw_UiJiOAo1ksgddrLQk2-d9S4RmhMUkX6-V3tKnPBpwTza7EmPhOKfultJgCu9Bevx_Mmuq_K3pRTJGSIh8m31d7LMZWJ1v3CQeEbIJFqbo9XnQgwvDn4hJjS2MUR5oCTgPMookuQrdSFY7mSmBBAE8ifTuPWDVHKErHAihKeFZQHuHEL9judjHlolqdK-ysKvT0pJjeh_7cWT_oqvanDXQCW2xDFvQNDdveFeRwuasf_qK6BqNtDX4fi57Oc44YYZLTPDXaVn5sBibA7gkX7Ed2Fe9prpTk8viqu4Bj73VOvnrAESKsLUDzxuPAHOxCpk3bAbxxfBB92q1YjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=u9T22B5IXXs-vo9EyHw91CTJGdcN6kQ02yCN1ZlVrN81yphCCWP2qMgdAHOCA63CjvvDW5Zm-coaqLsv73qe0efTm6Oiq-EbtLcGG6X54PNZBUa1ofld9Hnh0J3ilzTPkcfJDKRX6ljvp84OX9Ec4vZ-eG_1m7T9eCEZJe0UpWqzx5EkSoGs0XETzuiKFBvfoNAbKzw1slWj4spXhJ81J59cjR0dwAiGKvRUycTlFuXAPlNPLQKgmBUBwiYRUk5COSeYdeqsh26WcHeqHjNyyuTd_or0McIYlke2ZcFvRn9-zKA-NeFm6Av3_QvlvVQOrsp9B4g0qtbbDBsVy3Y2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=u9T22B5IXXs-vo9EyHw91CTJGdcN6kQ02yCN1ZlVrN81yphCCWP2qMgdAHOCA63CjvvDW5Zm-coaqLsv73qe0efTm6Oiq-EbtLcGG6X54PNZBUa1ofld9Hnh0J3ilzTPkcfJDKRX6ljvp84OX9Ec4vZ-eG_1m7T9eCEZJe0UpWqzx5EkSoGs0XETzuiKFBvfoNAbKzw1slWj4spXhJ81J59cjR0dwAiGKvRUycTlFuXAPlNPLQKgmBUBwiYRUk5COSeYdeqsh26WcHeqHjNyyuTd_or0McIYlke2ZcFvRn9-zKA-NeFm6Av3_QvlvVQOrsp9B4g0qtbbDBsVy3Y2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/utTE1Nai6ySt0fMbbA8fxxKlyxzg5qvtdNKyFoKxcMCByfwaMF4tOTEMQ83YXfXp4mtssZUlKJKvs1UtLzDFJvlRaNga-1N3FqwPrYyd7M84jcyI86LJpQUE5HRGzr6XXRvbuzkKCArCU19K6p97WMey-qmbU3SQl0XpaNblM7vJ8VKbvo-FquYLzdW7uXuUYsMekZcoJizOiMeXPUv0B22SsuT5XPHob9ay8K9ZMi9tB4OeINXwu3ttnnzels82XipYmWY5u4LBfZo688ZwGxSylWzQ5DDjlATGTjafAW-I-5lXQHTOvbrtfrGh7-jRZ5pjAdE6bS1OwsWi5mvw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Am_cn3CDgjfq_GOygQofj9lOtTG2CAg_E5uK-N0WCz8v89YiB27oPUSRwRfH-4JxuCgwcKVaWPa8CvBuACOqxtOlm-QQqdlT4rDwTnlG4hko4E4djog8Sptj-pz4GgOo9enxqBpJmzXybLt_McpbIRIXbRCdbLTxx5lT72AL__Ta1IEHwkVGiZer87fB9ctBdvQzAoAol7g2ZyGSz2AOeIMO7WXqs0YPnH1_xnLJPbd7x6CEZBVnQYEIdMahOtZpqGDthJEIN_gm6TzstaTLIZ2pCwiLbIg9GJPT4qWvuTqMGsA9bsLbZJyhbMvXIpvBr-LyJDlBsj3ITL_AFFOwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Og9DH7bnEoYxfc1oQAUIxGl_kE7PSDheiFHo3LUWwQDXecXsGsWqB5ISu_v2HL2T0U2MkVXZPn7rsxrqDU1T1RqGG_6v3URg6SDofXsBV0FQfAqtoiUpGB9WpuyDWS4A3p_7xob-zWcihyxrb6zZB77bbuWqJQIlz0W2ZI81Bqdbu1m1qkOEVgxD1MADryW1xSogDFkUaBeYqyORvtcUNKPaWF5SWLj8mmtXiNpgmwa5e7F_YP3ZDwgoMx4-9yn-GNV2CPYEAQuBykei31aKAkGGq_W3_txeEXZMlUuUVwen6TmNvP5UVoDTDUi6TVXOnWC6HFo-jathoN7ti27S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJnHU4InXn-uGSPcvsJOOaYKjIMgmiHPcvF2LE-fOaMUAC7Qc_k31L1oWif6ZkZxum5omzUbcpaoChEhO0O1JMyrtYjcYEum7TDcmPud_5wLcT1rM8mdQhh9segNHfSMWo7JhGu1GIY7sUqItGE8Dz91-P73wOWGTcPKzrwFRb8gm4n9uRFj1brh2TTTVzvaKKGgG0q9j7zYVzX5MrhzraBEcEUvt1a6GApLLs6TqrGZiUETZ9W1O6kpZDMMVsWUFk9DoGLXsxvkDDqi5CyeAQqBupFh1S93NW_HWYJuZqUtCrZ2J0a6VZi4sNhAs5i6T0DZL_brw_1Ax0-hnoHSEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRPs9RocKodPRSMgCs7LGs2WO77Ge4Yyu6X3n1rnNTG_RQDyjGFaYGIHBk1381DST36bUYPyx7Xs_ZCOB9LtPMAgeAH7e_PoY5H1IQMQG1OVb_3G18M9ipqFeIM13jqNcDK0EGKHCSfjOdRh7G_aVRLDHJSQuPquD637GLXGhjELz_95El01t5ORzr9yZIYeFdfpPlxBsM6lTD7PR1rL0fX1nkNxMHD1854nfsXFA5wNChrEg51_YDyg3RIDwS2zeDqCgkNBJVoehBBUfDEtf01T8K8wdwR0729F2LU3tBE5-SPY01xkC1JZScUojLuWxSGz1ywxrOdKgZtQF6Kzsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oxZOxNbgEod6BE9rD-DTBAb2WDO0fWIMBFne0hZ6mmlqypzEgKm_rDjJPZEjri3RgNFA_EhYOLteGW3JYqxY4WvMD_evNRnEMeXXSK_UR6-V8ppXfgtFumYX4ZGsnRgNBNXmxWPacJSpChMwMutldUXozNitfLoalbkV2Me9AW5vL2DjEFRISamsVaXrmPVLDph7am8vfII4SDCSJnlG_JNGcIu5AGlx-Zz0ZI35z9tKH1m4Fh6na6r0bq0xXY9gJYP-GLmZOK0d9R8pNaks-UB4EDLfSRHAqgMHvvJydp2C2MyBOnb1VNFD8F1S36P7H6BPwpNliOeaLP1nZ__VOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=hsGDOGQJETGESijVibMAAj9Mh7ZoucXuOP-Lj46t7WZ7ZpGzOt_SKGOMyn1q0orHDOA5Jq45IOD3qQGqqrgxXeceze0OOXI3OdQjBzhdMP61oSMB3qM2v6sZ5RWCq6tQozZnhP9dpWXNsxA050xLRCDnCCE-j97XpEIi69tBzyPV-JXQH3UDsEFANu0nfxGZS2JlYmGe2Oqs-TuixjDj_HsQhLXoVSDRnoSU3hvx92vm_nWdHX4H9Po_vOJQMU_oZkWzxXexA8da-uzIQib7bzHcnas5SErsT6td-6zeGV_hBYldiTnqgopehZOAleIBbMg_PasgHOyjGXEa4mszjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=hsGDOGQJETGESijVibMAAj9Mh7ZoucXuOP-Lj46t7WZ7ZpGzOt_SKGOMyn1q0orHDOA5Jq45IOD3qQGqqrgxXeceze0OOXI3OdQjBzhdMP61oSMB3qM2v6sZ5RWCq6tQozZnhP9dpWXNsxA050xLRCDnCCE-j97XpEIi69tBzyPV-JXQH3UDsEFANu0nfxGZS2JlYmGe2Oqs-TuixjDj_HsQhLXoVSDRnoSU3hvx92vm_nWdHX4H9Po_vOJQMU_oZkWzxXexA8da-uzIQib7bzHcnas5SErsT6td-6zeGV_hBYldiTnqgopehZOAleIBbMg_PasgHOyjGXEa4mszjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYqRJguMDwZVibbhrfJBdeP0rej7P7rOIWlwRBvLHySFikpBkCctVk6tUg9u3kC7ZlanoKR1Zi1PZ1aTfRaodwPTiFMcvWU0LZGwk82fPirVJIn39e3nmivOdlGtnQjXUHLNzhjXigXwvamtnhWUakAHrethH9ZrC3oqcp12u56nT9B5_ppoU0z1qedFv9t2n_sKVLQUKJj7TkWUPITAl9TWaVhUfLjr9Wj4OZZ-AZg0qZXaSMd3BW_oX2LeKwt5C8Hc3i3GzU1_tcMFS-j3TeuPwmksE2KMlRhqcEzC3KbzxIzvHCHS1X2fn0QIKA9UgzRy6JbOAYDgN2tcmeeBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olaBpOzk74FHAyIgW6u-6F0hcuVSOXUYAqnoSZlw9V7mocOp-EOIZyx7FrYQF9YXKvWJEj_wD8j8r7suwu_lzkpqw05qaTLtqLgM0TmGXrt078ocWbcDn55JvjBYwuCoEDts0NxgixdcmK3036kse8I4wCILfzp20KrBk5mkxI61xzK9QUQfNNgQzrHI2CdbJ6-fMG4dVRb2RsbZhNCayeC-SCoqcYRD5qYz8YSiHIkvlhLtMp_9YAZe1RkGmKTmV700yQrgv97IDMlpR97b5A8K9Nr2osiVaWRhxJCmRMm3Kc2dBcGGsByoMlWOkmIYnq5v9HixqBewqQ81dsORbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuhklMLXYtnzfUpYq_ViZxcMPIj5J-4eNvojtE5ZRo586JwAEhRSuwQE14qedZW-Dm91HbRBO6UT-GkYeiEU_pOnl4jOax5BivJnG-wym2jKukoC93QZ2E369QK-FUDqZx_oNVwRyOHsDJ5KIjDR8ZI4s472of9ONPcP_veYX81iXvvyKlyPv2GgM5ScnEvQD9redx5PF-M64d9ok0QvmABpBNsPHNtdhrNV1hSh-vXuOtv_OmaEFZRyQ4MxhyzvGfxIIv9tqyCTERWX3NTiqul0QnFebvAZ5sTODX4CijWZhQxT7inMYpEwwYYfJxxT33-2ZwuiUlLO6ak7kB1kxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=BOpoNbucR2JK8kKpl-lDm079c-pXeHbtIuTH-UQ-eDqcpGaDWWn5AS-G_E-gdGP6lJfAffQ9sKD7kvyWSHNXsnI7_GsHxK5hYaRbb8-wS2ocrOEHc2LOOtubWNkjuE7KSzaXU-m_9JZzCeaOiMRtkL8Jo0k7q-fwYZGu3qnXjCu30l_AlgFzWWpSMPum9yRGrJIHmePeGJjQZwwgXBT8wavFAStJ4l5_JeuOhKpuhTPctOqnasXMZHUT8MUVvM9iWd1YeGzlakHw_dBW0Maijz4fB9SFU4T9TwqOWOf-MVi8FzmbYVub5zGyBWXW8480jEPtlfir8XWOQLWYa9urmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=BOpoNbucR2JK8kKpl-lDm079c-pXeHbtIuTH-UQ-eDqcpGaDWWn5AS-G_E-gdGP6lJfAffQ9sKD7kvyWSHNXsnI7_GsHxK5hYaRbb8-wS2ocrOEHc2LOOtubWNkjuE7KSzaXU-m_9JZzCeaOiMRtkL8Jo0k7q-fwYZGu3qnXjCu30l_AlgFzWWpSMPum9yRGrJIHmePeGJjQZwwgXBT8wavFAStJ4l5_JeuOhKpuhTPctOqnasXMZHUT8MUVvM9iWd1YeGzlakHw_dBW0Maijz4fB9SFU4T9TwqOWOf-MVi8FzmbYVub5zGyBWXW8480jEPtlfir8XWOQLWYa9urmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LX9sQSBkwg0nlq2aKCBekNosiZwovKlDvjaI-9vtFf6QO8VuxSuTTchUwqz0WI8IYP6n7qgI_j-Svc4sJAeHIUMlu7Amq0fGVtISR_3IclFY3yg2qIR11K3EPgw7FaMIvjKN4Q-fwBn8q4g658_C_xyb9duyUQwWApuUM9HZTGLKX5zj3ty1xzFx3vjdAdY-KT_To8Eu8rRZQgUkSiv3pXzreuYXJczxXm1SYMkMgEMO_Yx7GcVWZAqDCVK-YiD8Mi_U-0AFpsy10spxcX4e19Zpzh-IbJ5c-blT9Nfs6LIC_S57Skl5xp_PpFa4iXzqALdW3VnQU1YIeoA3Xl0mSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LX9sQSBkwg0nlq2aKCBekNosiZwovKlDvjaI-9vtFf6QO8VuxSuTTchUwqz0WI8IYP6n7qgI_j-Svc4sJAeHIUMlu7Amq0fGVtISR_3IclFY3yg2qIR11K3EPgw7FaMIvjKN4Q-fwBn8q4g658_C_xyb9duyUQwWApuUM9HZTGLKX5zj3ty1xzFx3vjdAdY-KT_To8Eu8rRZQgUkSiv3pXzreuYXJczxXm1SYMkMgEMO_Yx7GcVWZAqDCVK-YiD8Mi_U-0AFpsy10spxcX4e19Zpzh-IbJ5c-blT9Nfs6LIC_S57Skl5xp_PpFa4iXzqALdW3VnQU1YIeoA3Xl0mSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN7lr5VI1fNFXjLP3x7fIU6COYUge4kj5vkskmKPdRHtgmib0Is48LrrWiz-kJvPDnuVqYufcqy6PwxYQwsa9P8OLL-BLC63TFSS7Uhd-EOmvJRAqjtXDx6vLH8kbDm8sW_Bub_TsEagM-RSanYV5gO80pM6D72yYLYMCht3Ml-Vcq4Hz5g-Zg0CthCto5nJgVTONVQZUkhBIACih02x-Evgyocaf6EynqsNGZuUQVko9g-13B76LdU03dxeXmrW6RBRsxSyIdQHwx9zZtLU4R2uyZ34bDonI0E6X56omgWVZub7wxQoO5CTFFmz5D3sOTF4SiaMCM-0FujAQ0Jn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lahuLaxBNBRoehRCshXGWAxF9UbQFFGt0eH_pjrNg2fTAyias9dmVhBDOruODcSRQmTqHtU1OuvBpxJ8HNezhVk40Td7wFJto-xzQ5WgOXCemz9Qj-e55kPPwUTcPprJOWPKJywwNyI7FgDmP8uMbIyx-vJLjgiPP7-gldcEb4w_nJ2mEGPGc99uR-Nn3Ca-Zl4cMIOGle7AzIIPPsjpVpOV0-iP07ivr1YHK_V2P8fJ3SqN3Mxa1fLedWcCNYmcNfKh6uJkehdT59NAShucMj-bFsk08EyC-wif_Q1LFWCZziIHJU2AZDAOXPM5JnCZq5ajjRZaShic3oxU6WeikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSLP6TfBls1KTHrI3W-ttC_r4J5XkG1s5sKsuG4r-HLisHdQ_DxOr4AcFXn8Iiq81_uU-2xPxdC00oOsoTg2jINFBWNWFTfypPtOoGF6L-gFkxf-iDOK21STCsAohL-tNgKnSnaRrnROyG-1lgymgh5gDOzB8osW6Yqyh73M2ptn94KXWxFR_kWltjKaFDLmrNDmuH3syonBMFitjF9GWH17rwhqY_-Ico86m84i7XCj5QYkehqEvOK0JhL_VpciVnsEkSijzlTLmUd20N5wQ5XBkvWcrPpFOSm7m4KUmRJOUgs7DiJDpltBUkKtkhdhrkxrvfFlq_cQ-tNItmPivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEoDjwSGt53iqqfdjSEGjKeweWTha6o8Z3EdWpGa46ZSDalpaDdvk_NUr5w_udG4fmwSPANhukw-ej07LF9FrHJt8UGqFF1N9u7cADZc3gf3uGYU2cl7PWH3R4Iwi5Fqluc-UOsBDwjz-24IEeI7QkxltmVVZMOD7QvdTtsByr-c3qh4q_3q8liCRADnMNZFVLsfmbKfcpnzI8C209wArPWiSRxsa6mHo8qK3LBo8PX0G6MgxfDIhkJXT9re1CV0ixsch5vTXyA-S5_Kh81JWUwFwpsiJwUSJl39S1f8VYt9J2nhD2L692mcrtNyXbA7FJ5a6MyI5shlXFnGdDEcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeL6-0Bva_Wl-Lhk3xEVpVm3dJPzagYcLVshO6_p_GUu9yBq4H_hm_CQ3oEIyI9KZ1Gmq1s75yYx12SCDcK5R-pe04JvMTHWa-QOSufE_94EJu4O8M8bVr2odpMdssJOQxqHvSCpyYxySfxQbCapaznczzER04MSs8x-QEEzgnJGI_yB5AUXEqtkHBmSo2vRBzGbpi6kWtnJICJCqneYjkpe-SrQNCLDllFZ33dv8kikk2-uCtghMMtswc5l7dgVP4C3q5i0QLn1vaCMpN4AXwDmXLYpi9Lkn-FddbR_n4JdX1IZnyJ06zCEGj871xwd0E2hdFTPOiEJjwsIxt3weQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YOPwJRlmW805TO6uHCLSK5x5cLDsz-wZ8uyKJfPgejS8_75CxK0vUKJh_UQfmfYRPoOYpVnQMg-fXNYBFLdorROcsxGYZM9b-kbJODA-4LQw1BeNri3MFZ4a2uzAjEgAoXefsAUTv1g6o36jLqE2mvizejZnt1DRI5rJEV1YzA0suoEHFE8qB8qNM66-hOFhitd0g_C5j1J5ErRUiapz2RbK5YXgVymrFhgLe9Ajy0TKmuc_Z41sifJnFPi0Bh2ob8kbSVcDzxvw65sM4-5KYYTxmxKer9cAUX1evev8OHfKmBDL-9f2_XhlN1_2xD27O92jcpkDPnrn0cuT7p1pqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YOPwJRlmW805TO6uHCLSK5x5cLDsz-wZ8uyKJfPgejS8_75CxK0vUKJh_UQfmfYRPoOYpVnQMg-fXNYBFLdorROcsxGYZM9b-kbJODA-4LQw1BeNri3MFZ4a2uzAjEgAoXefsAUTv1g6o36jLqE2mvizejZnt1DRI5rJEV1YzA0suoEHFE8qB8qNM66-hOFhitd0g_C5j1J5ErRUiapz2RbK5YXgVymrFhgLe9Ajy0TKmuc_Z41sifJnFPi0Bh2ob8kbSVcDzxvw65sM4-5KYYTxmxKer9cAUX1evev8OHfKmBDL-9f2_XhlN1_2xD27O92jcpkDPnrn0cuT7p1pqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=D_5WRT6zybzXXE55vEhU1Kz0e8ooD-OZeAuqHHWTDZAgZbrDjxNu40YGDRxedcExTQd8gYD3sIwnPpWC_mfZg6aDD_R1rTC4wrwffYBDzuTDYmGwPkw1Uo-pWqvyw9YOgw8cDyo4GibdG0EEEN0jkQxffUOGHktqnLxKdNwuVHoX58g-L1HdeDifBjy8THtYqDBL9rtfHDOBMo_6KjL-OAYZxqUGBdfOH_1Ho8SWu2qHcMQSAWt7cyI9iCDXNtGiikLkB79g7bMQmPzeu3Dmi1jnwX-jBve6ip928ze2rc0shx8kPKdjREs3gvlOCzNTtGSCylm3hnRvhw0BC4WoMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=D_5WRT6zybzXXE55vEhU1Kz0e8ooD-OZeAuqHHWTDZAgZbrDjxNu40YGDRxedcExTQd8gYD3sIwnPpWC_mfZg6aDD_R1rTC4wrwffYBDzuTDYmGwPkw1Uo-pWqvyw9YOgw8cDyo4GibdG0EEEN0jkQxffUOGHktqnLxKdNwuVHoX58g-L1HdeDifBjy8THtYqDBL9rtfHDOBMo_6KjL-OAYZxqUGBdfOH_1Ho8SWu2qHcMQSAWt7cyI9iCDXNtGiikLkB79g7bMQmPzeu3Dmi1jnwX-jBve6ip928ze2rc0shx8kPKdjREs3gvlOCzNTtGSCylm3hnRvhw0BC4WoMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHoUEBV_M9hkuxm-ZaX2CGRSmRTu5WDbaG4bVbyuiepltfSiW0e97DjOH143F0R4NWTjCOw0MggGtUPX06wdr55sOhj7GlVkOZf22IruY7srfVbVJRLRIfNcxbFggCtevsW209zY35ntXYxXmnP6mZoXxpHfWpNX_3GdzbDAE-l6uZ7CwMYkuTT3Rz9Pgy_uXvuD6T8lTZQnnKrG0C7z0KfyB93_tItny2ouhc2kEqqMQXx7W8u1i1oSvlKjFWdHOy-TgJSX4PsuNzlbG13QBdI3ZAMNIObOx6n5a9es43Q3IIpFWoCj-avUQFX7QGRp28ieyZZMQllCcufAQQJmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SG5JPAjR6zfC71JdAljIOPB2xHD2lF8WKRNTeX0T403-W-hfIorS8cF19UEW132Vv_AuxxABmVX5qBiqLypy05bcmXKcTbZn-jUWz4HVuE2RElHLzu47_PnUl1CNZ8Ev-GSi0qmaxpj-Gt4EbMQ4Vm_cWGurCUHsUoARxgVBH46hcqYdY1KVeArbmq7WMSmOVJH-zJP_Zvi335IrH_220ZG9a-IeU51LIgGxUl6_uO0hOjYY6hazTipuB-8Y92k06Eme3mYSM7nRIoqfQl4N2qeFH94ptjUdqqc8oUoHSlAtpK0G8lVEpX8-T_4o7JrWQYoH4Cf1x8NvCXYRtcQ1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYrTzXpmCfdIPGGMkfKRge9IB5VAKIm0TwKWcv3y4o9n9kObb-3wSs-Y3anPulbDOOhfeBg9JFsgN_RXKvSBxd9SQ_49dxEsjPqSD5PYNxuRcqnOlf-dkQYqwo_zaVOj6Tg8ROm4ZjfjMlIblIH_ynGif9hG6n3uSwYFkuBBI7j5lOBSIEPeN-U1LluZg6LC1S6sbR27xpSk_T6vEg2eVP5Vzvdcd7V0pPpuGvz63C_BsEOeelFiVXNlp7PVDAxfDDLFGd6VVFROtfYf9cAtkMLLIczpv1SBdws-9WOjqmViwmAFpd30HL2Li2CZglOeeYXFYDGApJ6ND-DyXLXcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXtU_rxGClOAsgQbzoAPZNKdNMNfOyZbB_Z4gCM5_oxV1msWjeIbJ54CozYIRQRE6G0NeYXF7me__tgYfF9YRkOetydU190_pxyX9URO9OCCKK1ajikg5Tx7XuQNkEC4wnnWjZLa1mmpBnUsQgqILUVH4a050BJMf2cjr2Mkq5scHtHjjZQ81pOxX-YD55UkHIQTGRkyslQJX3sfPmtIxaCKcKdbIuyegIqI1xAuQUkQ_15VtQa3MCO0bNCY34GNMUE1e7ggmP-zdeQCjOVSy9T8IXokeVWOc1dp_Eka6NOr5XVhPXjNfmicgxPZT93guik5AyZgjqybEjAbboXeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=cxyN8fGNXuWEM2YwaqJ7jNHMevHbL6nMN_53mGEKZpP_Pw3tDSWpX9VJv4hqkpklg3GiBSm-LJQtHqwqexGQSYUjH-dUoX_R1R78MZArdqvZGmAlTr2aBOEj9f8LD04LI0JH3EpcYk9RBwLt7sNz5yG5iLPywvKvzdNurh-wtMN086-La21KJExtgZTEKtd2X_WhmLs4pjsnuVJjpjdQ6S0nWdnGL_gAgNp3KLeahr5o0UvC8HY2iJkuuXMOJX7nQl_yPCTH4KRUZLnmAPvv0gK4xmkvu_ipjYBK5bJlJWDFdhJjGRp24JuVa27zn9AcN0juLtJbT7TYxfS6GziuVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=cxyN8fGNXuWEM2YwaqJ7jNHMevHbL6nMN_53mGEKZpP_Pw3tDSWpX9VJv4hqkpklg3GiBSm-LJQtHqwqexGQSYUjH-dUoX_R1R78MZArdqvZGmAlTr2aBOEj9f8LD04LI0JH3EpcYk9RBwLt7sNz5yG5iLPywvKvzdNurh-wtMN086-La21KJExtgZTEKtd2X_WhmLs4pjsnuVJjpjdQ6S0nWdnGL_gAgNp3KLeahr5o0UvC8HY2iJkuuXMOJX7nQl_yPCTH4KRUZLnmAPvv0gK4xmkvu_ipjYBK5bJlJWDFdhJjGRp24JuVa27zn9AcN0juLtJbT7TYxfS6GziuVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEYAXO99d7VJU9YzoFMrmmx1AEFN6oasmMcGdVYFe39o7s4tPDEK52y1IWIQvFJVXIDqkuPUgnhZ1zDuOIOwLCg85_4MmynCn_tJ7IgNh4_NlMQD_47GFgR2dQdaT_txm385bP-xHTffm7UKFmze3XZvszfOGVxCSYXQG-XWorfmDsQkphXYfU824zRWHxnQ1KoPizbLYvz57OZpkOQpjj0DsCeDmGarO7ahfbLk2bg3Ljm2PFq-Kvk633P6aZOYMQXRy7eud6f0_BzNaMeTbabTjnb3hBgV4xB246Ex1HUGICMjov8H4d2m9lKlFPtU29cTsaOoN8zOkpubZOjhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=cHWolUj0G3nsLYmGP3VCj_32Qfe0x9e3Noae2ox71pxnjlnPij9OCarz9FWn-nv6Jynj9Eh4UgCWnHT_b5e3PYxM_yQ8OR_AxWKph_mxK8UzqPLzUu8ozFqmVBhRXkmq6dMm0Bhx7QcB4-P7uCDrPYaTTTEFgBLufdzBvMTEdOReFqCyJyUPAWnuHavW2CYi8QixxAHA65vVVQLfDPMn7yD0CGyMdRhi_jQ705dt949ZRiQ0FwoK7-WvcD7cKrft_mbFmIzl546LLVfgZajEwcJkxU9DmpxplfSyggKkfS9mtCd8J3LjO0S0PMval6cLJF8zVQhQi2dF2_QEX6AC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=cHWolUj0G3nsLYmGP3VCj_32Qfe0x9e3Noae2ox71pxnjlnPij9OCarz9FWn-nv6Jynj9Eh4UgCWnHT_b5e3PYxM_yQ8OR_AxWKph_mxK8UzqPLzUu8ozFqmVBhRXkmq6dMm0Bhx7QcB4-P7uCDrPYaTTTEFgBLufdzBvMTEdOReFqCyJyUPAWnuHavW2CYi8QixxAHA65vVVQLfDPMn7yD0CGyMdRhi_jQ705dt949ZRiQ0FwoK7-WvcD7cKrft_mbFmIzl546LLVfgZajEwcJkxU9DmpxplfSyggKkfS9mtCd8J3LjO0S0PMval6cLJF8zVQhQi2dF2_QEX6AC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=Q8rrD_abtZbJ2gJHhcdEHBTltCQnbjFT7MSsgkNZfZuZEXG0eqisyFX5jkQSURxmgwTKDNSyZfe2ksEjRBm5RMxxsxuJ9vqq8kE0Couz6eHWnYelTUVJMD_7v-quCrvwLOMUZee9neZG1O44XwIaYm0mI__l5IXc_0jMmrHeGcHqrk0PJwJcPRQ0MD-ClIYaq57lckZMEIluAQ-_TL0HRMn-rVxGztgsyqmvuaTBCCI25Zzn5M-b3k4d7Rth-P32kP-ePv8AGsXHbCiM881QUpoLSsDaf8SlAENKLdWxIJU6sbAUmf2fxo43AZH_nfbPWu0W1geIX9S5IkV0EFgUGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=Q8rrD_abtZbJ2gJHhcdEHBTltCQnbjFT7MSsgkNZfZuZEXG0eqisyFX5jkQSURxmgwTKDNSyZfe2ksEjRBm5RMxxsxuJ9vqq8kE0Couz6eHWnYelTUVJMD_7v-quCrvwLOMUZee9neZG1O44XwIaYm0mI__l5IXc_0jMmrHeGcHqrk0PJwJcPRQ0MD-ClIYaq57lckZMEIluAQ-_TL0HRMn-rVxGztgsyqmvuaTBCCI25Zzn5M-b3k4d7Rth-P32kP-ePv8AGsXHbCiM881QUpoLSsDaf8SlAENKLdWxIJU6sbAUmf2fxo43AZH_nfbPWu0W1geIX9S5IkV0EFgUGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPyFe5pw9YL9JBj5ds15fbWtTKca6q2iY3m_oHPRs2gsdnRq8r_hDcskCXey2ey0Hhdpz4nIE87eor_GZMhgQAK3PM-o_1hzyBIv_RC6z9L8V5c9nUZu13cK_GBGazFZFiWbDnGGaYe5K3Ld7otfjEXiWZmpmG7VyLT018FTTptKVBl_dr0asi0RDGMyc138xfOqcTsxmAETLvR_Oc1EWsidHl5gJu4S6Z7drmdcLOig7rLWJqLeY6qEmH6RGb2BSvMSqt9zXkodUhQNsByyPh16FxnYu6AGddBksNJMct3aPZQcglWlg227AgO5z-QNDPtVrxfsSeYcAZr0MfH9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s31Xn-8WfxrBcqB8d87hTdPOFdagjKDppkYGx-ejta65UIidZpFqXcsPPMnPJmPZT8GXJCqkCJi6UKuKLM5PMvs2T9HQqjztke4-0OQHyKudWEkg71sA9byx_Z-fG3t_CmwSLO_-Q5gEOrEDr3FYI33jQuW1S2zEtBLIu2vpSjQDENDyI0elieBzNAQMjPbGJH5bkIbhDdsPUf0Osq7PrEFKjaWPdrgPr5nKTN41-sfgbt94Q2Q_0Icy7L2OyhmIhgXrv0GOa6NQpox3kubv-wMbjd3qb6rFABSLtlbPuQ6G-gXYKC3bTVYMGD3ACGL606Yc9-7CZ6CwxrbvpiWn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=F0mtOqqzFxvxjNxq6aRTfygigWzCDzESE7vZWHjjlClo4OpFa19DgVnxkFlhEnwApyiJ7c0nZBsBmWsmLQ_nmhWnFSQxa-9igASDK_yQmsMD8eJ0lq_fejAXvyjE906oMU13KcoufwHMJVjj2OlenNpeoh8jPsYPxIeMSyeM008lVaPp5t-nBL8mlY2iXHivLWo8BlMA9ODhQ7NWs5Dr1jWHkLTx4aegEJDwhv7KJuKFW4lczTAi5YIfFxZL1lbquA5yeiXklmVLUNIcXe6T5NJD57MbgRJ0nBahX4tCxZyxjbHe--gvBERrOCOLm4q7wZ0UEKOYH69uFfiE_o_Sug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=F0mtOqqzFxvxjNxq6aRTfygigWzCDzESE7vZWHjjlClo4OpFa19DgVnxkFlhEnwApyiJ7c0nZBsBmWsmLQ_nmhWnFSQxa-9igASDK_yQmsMD8eJ0lq_fejAXvyjE906oMU13KcoufwHMJVjj2OlenNpeoh8jPsYPxIeMSyeM008lVaPp5t-nBL8mlY2iXHivLWo8BlMA9ODhQ7NWs5Dr1jWHkLTx4aegEJDwhv7KJuKFW4lczTAi5YIfFxZL1lbquA5yeiXklmVLUNIcXe6T5NJD57MbgRJ0nBahX4tCxZyxjbHe--gvBERrOCOLm4q7wZ0UEKOYH69uFfiE_o_Sug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=vDCPHoWYQdure30bHX2mhj9_Bv3dRhuAa82lvyLPLBcC2au4g95Ml1WRjU11QfDzvrkEaqlxtAYMREpCeVGqk6nZt_hv9dV1ZXT4wFABmRQcRBHBnqV_HdLzpbjJ6TJfpsDZSAnN4x2lCtx97rDzMHoiojMjM1son5ahiNlNaXGrikb-CWbSLwFi5sWGxIBAPwz1nHoK8zJXhTPsIdysodD8OcR82yZRdmGkr5fRUZ9adb2Y66_hL13oRTaARqu41tHKlya5gRvzy3G026LmDaAz_mdT61u3oZReVUP_xTzVt6B0ZQnd2o1ad5NRfn0jJqwSYR7te1am0tTHFJU3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=vDCPHoWYQdure30bHX2mhj9_Bv3dRhuAa82lvyLPLBcC2au4g95Ml1WRjU11QfDzvrkEaqlxtAYMREpCeVGqk6nZt_hv9dV1ZXT4wFABmRQcRBHBnqV_HdLzpbjJ6TJfpsDZSAnN4x2lCtx97rDzMHoiojMjM1son5ahiNlNaXGrikb-CWbSLwFi5sWGxIBAPwz1nHoK8zJXhTPsIdysodD8OcR82yZRdmGkr5fRUZ9adb2Y66_hL13oRTaARqu41tHKlya5gRvzy3G026LmDaAz_mdT61u3oZReVUP_xTzVt6B0ZQnd2o1ad5NRfn0jJqwSYR7te1am0tTHFJU3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOab1hpx4Cqhn9GdWLsQDvznmNVaDIF84O9zXAdKLqv-vdpwEFgZDFE3Dqaq1W8UVFwFodo07MC-cnAVEzdqKcpYwX5ojoAaPBREH5tmFgud6l08AICsdkCGeXp0lsX05ZKRcB7Dc14nZgR0ibwNJIwyEMgmSEFR5tJrwPhlcxqsEdOekpSWwL-RGtMDnd8MekpHcBuyl-MyKjqmkFoLDSN_iouLPjYCicCyU36RvMsXHtL410LxO4n77Hz9cd31yGueAyeqtWRPPwU7uDuCRgP03MoxjSe1sI7NIcwct3XK95xuPhLe63JWxfMVtA_m4-adETCPTlVZe_DSJ2z1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmzyILP7gf-dNZBVwDIDslRAnb6yHGY8usHg5ELKACK0nYQGLq0gD1qP4AHfJF8pAlhQsrYKjWuQ-Dm3N_VYjnte0F4SmzgBCJsFc4y7R9eKyEsJGha9qLnWRklYi2iLhM04BcQcYktlXx5HKznrfZj7Q5FyRTEjHboDGlfEpIuAarD8g00XXEUSMRxEDXkuhJ3ofg6GNnYoFQQ3MpgyLvSRvUS5Wrf3An2SOX1bftdsm-Gm4OXW4qpUJUns_8WWReqJKp9jhLZSyovyCWE32kmbIREJ5qs6W_bmGy10onbN1spnN55trKpQuNLZXuhr6hoXTGMVUZdCdOuK-7KbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce-wIZWcPq5doQNjh6NYx5OpAAZnNhrClydC2_GOJNrosBl657pGTz2cCdWeDRHTUMLMeU4WOg4HqWoklm5ANqdoWviJM8Z7ipUMJxqAh5m0mYXIElI60uKQlwBYyVAMW9p3pyv-sIIPZdIiH81f952kpPzSMjMYng2pTyBKUBn7v9o6MCueKgLYjtcOTeFhu5nz3urzopotNn8UFaXmaDhcZmXuo1Y307OD6gMODnBDrwLlxz-DPIs-QoXNDbBuPcIMixWA7N2rsUQK3ElJfm6dJLgUWehXANyr4tidVBXtYKy2E_-JD5XpDt913Vr8uNwUkzjP07isBws9lA58Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQXmhNI9wu3uXd2OqIBqCXEukqVotXrcoovU45iGIyt3Md5i4PixLIWOcpWbHnlIJNwVKi91wV874HQ2DjSE778667_PTDIA8MxUD9upqzqu-l3bTxLV2xLBmXavVYq1qEO6vZGcINyxNSrNadGfqH-wi7BZGnTcRrvnbZw-K6ITLJG-tkBLIPXhyR3G7fbV8C2oMoiyDA7biMSSJqI1etUK_TKo8O90iK2va4osCt3Yzp1bKg8MNUamIXHcIodJWzmWKj-jy26eDSdS4eDkomDvYlgimiUrhu97g6rC0UfqTFZE7m2k7aYAzEVPkeSWMjuVoHx9cZrvPGNeIhyyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=qj2ej-QRh5knU9Al2BWzJNFhBZTb3T0vFv78xCraqIPsNpnFPtKBXv6iLHdpCOGXuVTVQAAaDdq2tJyKqj3RpmYjUnPnvdWVw22zn0Sy0QRB0qfVaZXG2UPD6auYPOVyq-0wK9nUyIaZOA_ThmoYXu9siuTzB95_qa9_r4gWTLMAJiEFnv-Fuc8xatJPkZ0HTgkgm-MhW4MJfbUJCi282SrlmiMRE3ZeeEqHlckeP_29i2gCTEvic16_B6XZ_VPdUJ2W7V00IYu8ozxaAfIamT0ELKP1hVtcPtnk6e86ee_7Rn3P1auUj-iVrGW168FzAFOLjXC_l-gTTHk9yQBbMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=qj2ej-QRh5knU9Al2BWzJNFhBZTb3T0vFv78xCraqIPsNpnFPtKBXv6iLHdpCOGXuVTVQAAaDdq2tJyKqj3RpmYjUnPnvdWVw22zn0Sy0QRB0qfVaZXG2UPD6auYPOVyq-0wK9nUyIaZOA_ThmoYXu9siuTzB95_qa9_r4gWTLMAJiEFnv-Fuc8xatJPkZ0HTgkgm-MhW4MJfbUJCi282SrlmiMRE3ZeeEqHlckeP_29i2gCTEvic16_B6XZ_VPdUJ2W7V00IYu8ozxaAfIamT0ELKP1hVtcPtnk6e86ee_7Rn3P1auUj-iVrGW168FzAFOLjXC_l-gTTHk9yQBbMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1V6qilK3O0MJeunGrMBSPeUd8q_U6nKF9pxgU-rH-Jy16r43wW7z7PwJ7a6qYW3kQCJ5EoUP8mWbKaNuHbKRfHiS7AfiamtEajU6Aeqgw6mUvHAIQ_NiUzeLCSMCSMK4e0ma0kld2ZRWvF0USyfKYo9n0DMIftDOOJLhzeMyVj98QKpG28MSoXxCIJN4FKdDwV7GerQdGoLvKaqdbDoye9raUup7XTMpXhw0ON0AeK3mjinHcZjZFY4SlaCSDFCk9_-BZqz5BHirJiOdDZJ5R-csD-KU00zdgroqWvjOAJMb5TzQPEiScxqe9oMtUgpk_FHfHMtDnJqqkSuT_yykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=pGiW9cipHvZaK3aSYzbXq25zO8T1-ENi63YmDZIK1W6qe0SDBRYqII8gmlcD4Dpza0yO2zl6CvuDj9Wsuu3ZjAaap2LeCuMJiXufk9ixfh8cnEfLtVouKRh_e4c2JiEGDN22iTQeycwKlf4RCvEIlpnD9IJsc8CG2iM5eOblqeIcoEVpJpaFMdDcprJAukdprGhh2auMgIaCxUe-2X6B2FXeNIeQHoGDOwwh2waUqk-L4T3sT8warPpWf2ut5nb_zQEV9nD6GqWiln-H0nBhw-x4EwXQ5jfjGF2OU5o4NK26fyJIh7OxgLQZT7WlBvOInByf6P_Wp0s-2j9VOt3eMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=pGiW9cipHvZaK3aSYzbXq25zO8T1-ENi63YmDZIK1W6qe0SDBRYqII8gmlcD4Dpza0yO2zl6CvuDj9Wsuu3ZjAaap2LeCuMJiXufk9ixfh8cnEfLtVouKRh_e4c2JiEGDN22iTQeycwKlf4RCvEIlpnD9IJsc8CG2iM5eOblqeIcoEVpJpaFMdDcprJAukdprGhh2auMgIaCxUe-2X6B2FXeNIeQHoGDOwwh2waUqk-L4T3sT8warPpWf2ut5nb_zQEV9nD6GqWiln-H0nBhw-x4EwXQ5jfjGF2OU5o4NK26fyJIh7OxgLQZT7WlBvOInByf6P_Wp0s-2j9VOt3eMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lH05sWsRtnwbG0WuAl_Ij1zb3Yw_FSpp__Z2568-q8XWJIxfxmMF3CXBau5LGSXTDJ2cvc70AH3_ooddURGBrdoFJS3R-W0wMQOOjWRxWVjSQBwGzEFDQsN9RNcos1GSAum6FGKa5W-BAQmyWU7LbkA4UQDnEIatl71cXrsq0iKIdXrtZdFxrgzfFWAVGhXQvcD7Vnzl4lcvQzidaTb7QsFkflTgtZpv3aLuy2GLS2sRWMChXGltuXwQMS8-ge4I0zE5g5TVbPJvPM54VV8wjdwRx4XdZ8DB0NOTVzsHfHG2owDcpfYyf-dQO4PnQPvCQ1LqKDAaIPz1j9tjh26OqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUUK95bDoOoxGF9oPYJO2GmCtCpqwsomHtMsstNgmSD20OJ6wfZZWtFedCUjNDKFP1G6EAtTwOGH-ZGWU2DJpHYbVkzdjMAzzGP--j66AGzHi9Tsb0dwk1ZvJElGWYNtKhBbN_AJoomja4_TFUSduU0xo7bmfFlJ5WTJXsPA1pFASKov1BWX-vLuU9edrQPp_MJcjUaNREkFCYS3ai-kmxdrsZBd5gEpM1r19yq64z3_k_zfuqqOUwKOQuQvqUL74YA5D9KUq16yeR17CvfWHBiNFFIOKNLTRTY3Iv2S3AFc357r6Sw7U4lIJrVfbaLW6hFbAkZuXY8yidomi-4OjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlpvv5aR68kflDurOgla94KR_OqcSdIaxzLo76fVe5GkzZxotBwL_z7j9jUVCLVtHAs48HtNmdo81zGj9_ru0jf3OC_BdOleNH1zMZr-FwbpuRrKrz-Qdes2lSx3mqN5LCElTuYLaf-n0i08J_MzNC9PtXBlmSz3_CsjdOmNSXXadQYkWAyaGwxqBEEgy_VKWJgCVV1IGz5DEpNUCfMHDfOAx3vlQPdZ2SWUQznVvdEWLTOXzuWEXdDkO1XZ0Of8UsD9xX2ga512FbGfiLdUwwzaiAelJyDOV5Msos2fDL5LHtN3BASUWuchsBiCL2rm_FHHgBgSa8lReKabfF8tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaKw34srOBXcWbp-mtygGn5yR5kmtGupsPHLD6XkZUpFUEjdKZjMeabbrSf9kB3w11-oh542ljoxK-2V7wrjM1v7FiRZ93PIgvpSaOsfUtOqYFcZkfcJ_2zjTj-Z2oegPACH6YAF90htSGtebU2Fsw12cALG9Z-MxfDgxSu8PStECZUChFbRY9GWRUEMaLfjgB1JBNEt9UK-IZXQQ5-3z4yTXFSqH465gzI7-Yvo8Uj29UtRhH5rfITPBpL2wxDuC8MQ1eaYxtqUlsDpfa1ioYFVHxfwzBqPKyCjQIF1rBt6GTjFySHqXxAgXQYiUqHxamPvPer2Df3fShe5gjJnwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
