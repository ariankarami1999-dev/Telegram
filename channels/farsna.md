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
<img src="https://cdn4.telesco.pe/file/pvyes6oSLmGvL7kjfqwqMLgJN8gYNEWZYj60VWT53UzW-qTYwXOkXH4tYxo6VzauMe4kDlde2zfW55iCdwweFWQT8vUI7-gNInwkXGXmA2hTCwVJ_AFZFTzyTIAh-4PbhGo8qHTVg7Pqd0eo770Pa-UrjMnktVfwm9rngEJkNBkxDAzjDOICTLxoEx7_wHEd-_LrdNZozOUSo0t1Gm4cwwkSKun7vI6Uq9cwqRrMRT0r76sr7yU7MH6S2jnRULgKn_R_9vP5xqpvrFH467fldhKLj2usYvqItxAtI2GAdzAu-X7TgRz_i0SV-V77ick3lvUzzsrf1ncUzFH4WgQILQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-450134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7263ff6e2.mp4?token=tTRznTlZ_DjPH-EGOSO2C5furSppki8G22x2aL8fK-d9UE02gHm-seL8mFymi_GisyAF9tRHZAwyHE4xQttS0-HAqW4w_QBZTw2LdltKON-oBy0GuRgNfQ2n8FF6t--fvvj9Ymv9kIGH2HplXA9P8hGMmJk-w3h2DLbB_s8jfjD5rQxIF_m3Sa1mAz_6Cr1ZwFEiwapRqVvS8vopE-rEIAzRV9raM4L9P5-vY4nxT8yTP8R_b0hFv0-bvVdS-Ct0ZOJhzHND0Nesbi4wUt60H1ncww7Si4ck3syZyLtNo6d06uMCwHRh1_4-Pts_XCGKjdtKBvQ6iJh3SaOC3381zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7263ff6e2.mp4?token=tTRznTlZ_DjPH-EGOSO2C5furSppki8G22x2aL8fK-d9UE02gHm-seL8mFymi_GisyAF9tRHZAwyHE4xQttS0-HAqW4w_QBZTw2LdltKON-oBy0GuRgNfQ2n8FF6t--fvvj9Ymv9kIGH2HplXA9P8hGMmJk-w3h2DLbB_s8jfjD5rQxIF_m3Sa1mAz_6Cr1ZwFEiwapRqVvS8vopE-rEIAzRV9raM4L9P5-vY4nxT8yTP8R_b0hFv0-bvVdS-Ct0ZOJhzHND0Nesbi4wUt60H1ncww7Si4ck3syZyLtNo6d06uMCwHRh1_4-Pts_XCGKjdtKBvQ6iJh3SaOC3381zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابلاغیه‌های لینک‌دار کلاهبرداری است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/farsna/450134" target="_blank">📅 14:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d02ed93f.mp4?token=XXo_7RlUkYXl7CsnB9VaqSSyB7g3lwQy92RUHQ1am3kxZ4eNAnYnCkGVxqG9alc1rlnc2qUkFaTKEm3c3O1LUZCMOSxqmVynXoLjnspRp-dGzMeOZLx5Gg5i1qT-n08tllG09ZfQ6u34dvR2oB02MWP6qnSbDAL_OS-0ZuwLxpkO-xdnmznxF5PyuVZ9oJkn1Czui5y3MHdYBLEfr2CoBeOqdUxxeTJ1Ct1yXIxRWxwwOi4wVpQvW04bHfMZxgc8kSZGhKHMt_WN5rhQ1zwKfFAeJIg5UIuqAG3eT5GzdqMI3N9OK1rBaw9kMxoD8ULsR3qinvxc-m6zaWAa47uaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d02ed93f.mp4?token=XXo_7RlUkYXl7CsnB9VaqSSyB7g3lwQy92RUHQ1am3kxZ4eNAnYnCkGVxqG9alc1rlnc2qUkFaTKEm3c3O1LUZCMOSxqmVynXoLjnspRp-dGzMeOZLx5Gg5i1qT-n08tllG09ZfQ6u34dvR2oB02MWP6qnSbDAL_OS-0ZuwLxpkO-xdnmznxF5PyuVZ9oJkn1Czui5y3MHdYBLEfr2CoBeOqdUxxeTJ1Ct1yXIxRWxwwOi4wVpQvW04bHfMZxgc8kSZGhKHMt_WN5rhQ1zwKfFAeJIg5UIuqAG3eT5GzdqMI3N9OK1rBaw9kMxoD8ULsR3qinvxc-m6zaWAa47uaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا به آهوهای ایرانی هم رحم نکرد
🔹
درپی حملات آمریکا به جزیرهٔ خارگ، تاکنون تلف‌شدن ۲۵ آهو تأیید شده است.
🔹
معاون دفتر حفاظت حیات‌وحش سازمان حفاظت محیط‌زیست می‌گوید که آمار تلفات حیات وحش مربوط به مناطق خارج از محدوده‌های نظامی است و تلفات واقعی بیشتر…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/450133" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVixGJ1xVGrhTAtbazi9xSrY-1LPWHlckJCRfUEmrYNkVfoU0FSXZ-CIGMVv8X57QE_Uc3cJlSB50cmfVj-5zHSGwNTKp1u2nKpk0IRZ7kANOitG6JDgWTDyRsYijXRrR4YOr5abo_7RVBpoXx1MeNzYV85X0Jl0Bw3zehge0fEokF27vcGFWmJozTpkStVahLyEtmReRFRYcdr5g9bp1KAh3zxx2rQGj3DOAA1iDMivUO7hWk4h9EbKs07diPMzxhXJ-ZpaufqKtK30PNQfdQlErtXdUiswGox8Vk8uanOfdH7CPszha58YW0wh8W1PKXkqarEleOuaA2qV9UW2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFGmk6L5MGjdOWVtyFRdH9OtMUv0drIrZO8TaUiZHkWNXeexVg7UIyKfyxBTxdvw-rBsXgaEmN6CwuilQvP3E9DKewlTP0QT7CCH0LZKJbLnBNps17EYKQFwvhBEsLTCkEd3oTlNzbwTAbn75DbtRlVrKc22FwwUxdJu4jt3PoSX7KfprPyKD6aA4sVwtjQYMstyK5l9ObwjUsMMbe_AUtlihTnedQhhDfuuI1kh728B4qFVWUVniI7uLFIcor-1apR_iPo2YUyrEdPSkkIK9eAmappz9FyGz0v02mexOAuTiohwTT32HRHn9vTNaTvfuS0IGi2Nh-JyAK38uPUu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwrBpsOmgGwzWcmg2NhaCLCcHafgBhfkfsk9ZIhX9Qu-yZSMfoDVAHTG3bSPkcfrCQIa7gwI9Ux1_LpGDWUaxvgM-0GdZmuLeRARL0-W9Z9K3gUTjQ5EU2X-KyNoNcM347eSZSZ1d08bbr9NxZVdnnbocy4f5ewLIS3rcoMw9UQevyW48hVfuH2nAp_p9spW-fbJDSQF3Is8zuszP9u2VZApEGA8sbIi5BGm5n4JVtrLDPzxkucXpDNO1xnh7qP-sIfAuGLRxsH7dXdC5AxgDw2VGALdZHjgYP3zKaUd80sb0RL37pAaLxjWvZGh08-vBdbNbvHaU8XVOKLNaerI_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
آشیانۀ جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
مردم شریف اردن، سحرگاه امروز که شرارت های ارتش کودک‌کش آمریکا علیه ملت ما مجددا از سر گرفته شد، در پاسخ به جنایت های شیطان بزرگ که بخش عمده…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/450130" target="_blank">📅 14:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6e6af36b.mp4?token=KgAXWWc6Gmb0xFXYSwgGSPUfiBrnyWuJINDle3d0Gi8HlKGW064BgnNAKZEti9edM_HZWXtFs6d6rNRWVVpFtLts4zXGh23cccE9PBSQglDQ5aN7FrCp8KmUMPo0NHkcyesA3KZPxPT_dFOE2vWRmIzeGrwQYCroAgdCKr3w-K7f8Tu0rXv2N7CrLZmR0wHN4afxvAFDw1TcMuIixgqj8BSg7GihkKY9Onv_I3j5cUgYwURX4mVNRa8PLElNw1qKKQlTFSjYtkPHz4dlNmJ6yzzUONbBVmq0r80IDEwLGYTtNhJk6t-iLeKFKUMYw3fwnFkRi3frruTo0GVG2O2jgZUTQBH6X8EioYSTKNVzbI21dcAC7-A9h9xCBXPor5gaSFm1E61AXA25YQbJjlgYLYFgyxzYPPHzS7xHeBQD1Qmpvycl-1kP8cLEqskn_zyEeIM4RTGjrew5u3NElJZz2BMFD09AcFxei36v2QJhok6E_Slrc4w8n_tupV97PcKbgS7fLjfEZmFwWQeOk6dbD6S3lYcELfCRHUlG4bsu4ugt-dJogae-3Hsffdl0Dg2K6Oggku-qk1jssIjxI5cC5BYxxsPNmeuljOfw9Qnnivj_FoehPPNHjP1lxtNrHRtWQUHGh-QzVIVUH9FwXe5zVh_3cG_s1jm-A3lGk4eDXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6e6af36b.mp4?token=KgAXWWc6Gmb0xFXYSwgGSPUfiBrnyWuJINDle3d0Gi8HlKGW064BgnNAKZEti9edM_HZWXtFs6d6rNRWVVpFtLts4zXGh23cccE9PBSQglDQ5aN7FrCp8KmUMPo0NHkcyesA3KZPxPT_dFOE2vWRmIzeGrwQYCroAgdCKr3w-K7f8Tu0rXv2N7CrLZmR0wHN4afxvAFDw1TcMuIixgqj8BSg7GihkKY9Onv_I3j5cUgYwURX4mVNRa8PLElNw1qKKQlTFSjYtkPHz4dlNmJ6yzzUONbBVmq0r80IDEwLGYTtNhJk6t-iLeKFKUMYw3fwnFkRi3frruTo0GVG2O2jgZUTQBH6X8EioYSTKNVzbI21dcAC7-A9h9xCBXPor5gaSFm1E61AXA25YQbJjlgYLYFgyxzYPPHzS7xHeBQD1Qmpvycl-1kP8cLEqskn_zyEeIM4RTGjrew5u3NElJZz2BMFD09AcFxei36v2QJhok6E_Slrc4w8n_tupV97PcKbgS7fLjfEZmFwWQeOk6dbD6S3lYcELfCRHUlG4bsu4ugt-dJogae-3Hsffdl0Dg2K6Oggku-qk1jssIjxI5cC5BYxxsPNmeuljOfw9Qnnivj_FoehPPNHjP1lxtNrHRtWQUHGh-QzVIVUH9FwXe5zVh_3cG_s1jm-A3lGk4eDXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل آتش‌زدن فرمانداری و کلانتری دهاقان اعدام شد
🔹
محمد امینی دهاقانی فرزند حسین از عناصر همکار دشمن که در روز ۱۹ دی ماه سال ۱۴۰۴ اقدام به آتش‌زدن فرمانداری و تخریب اموال عمومی در میدان امام حسین (ع) و کلانتری شهرستان دهاقان کرده بود، بامداد امروز پس از تایید…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/450129" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار معدنی علت شنیده‌شدن صدا در شیراز بود
🔹
معاون امنیتی استاندار فارس: امروز هیچگونه حملهٔ نظامی یا امنیتی در استان و شیراز رخ نداده و صدای شنیده‌شده ناشی از انفجار کنترل‌شده در پروژه‌های معدنی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/450128" target="_blank">📅 14:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌ ارتش: پاسخ تجاوز آمریکا به ایرانشهر را خواهیم داد
🔹
نیروی زمینی ارتش: ارتش تروریستی آمریکا بامداد امروز، با شلیک ۱۳ فروند موشک،  آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد.
🔹
بنابر این گزارش، دشمن متجاوز در اوج خباثت،…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/450127" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تعویق یک امتحان نهایی پایۀ یازدهم و دوازدهم در ۴ استان
🔹
وزارت آموزش‌وپرورش اعلام کرد امتحان نهایی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و امتحان نهایی پایه یازدهم در روز شنبه ۲۷ تیر در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان برگزار نخواهد شد.
🔹
زمان جدید برگزاری این آزمون‌ها در این ۴ استان متعاقباً اطلاع‌رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450126" target="_blank">📅 14:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTtarQpuZBNjvxGRdh0dJe_AJKhc_ijjWU9pjh_y7ZalGT_LjhI2CfB3EgIntg5ff-3EhyWIEQ41dTDQUcdZgzgxQF_m5mxnC9qy0T57jOu0iXmuuO9YyRpasDhKQVoFS89dzrU-_4NbtUe29DaslbBYIJi-Qkr5x8ORA6kaTRLFbJY1KkGyjONv05YyWwB76CFqAJkKW6eqqbMpoSfuimBdksMjsjky-XLNPslGtCf5tD_qA2FUffguP_WrHtC--WtT09-CDwtvzFVXjZFLNM0_kmpToBpFSO8R8oR1s8lc0SZ9xeRHeQaQAi4pN2pMGJc3yKY1y-dChIVMg1iGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیلات هرمزگان: ناوگان صیادی در تمامی بنادر استان طبق روال درحال فعالیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/450125" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIoq0u7Sm7B-kXiKIfBbePJPPZYs6PNkfB4KibpR0g-TiG9pRRFu18hlv6yD--c0tskFr-Y3l-UhKV1MjPsbLGp4pj2GuHGznq1ujU1vxh1l-38uiQvpXX1VnhX0oL66kdN52kOWyESzzpvSRZTzR2S2hDRZ-kuJomUcpT8kDAg21T9VvWYVUJnTD8UIIbz0qN-KmXsDvsI3SjeKA92BHX-QoDgnHN0zAvW-BCkEU6Ud0d1-E47D6ELgm6B8DbUhppWpdsUWis7c5VmfB2k-k3iE02o7cg04GwCDkAkllalG3-6ZQVA87-Zrd_Hm5ShudaAcleE_GITLfOlpEQZ_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدردانی واشنگتن از همکاری امنیتی اردن در برابر ایران
🔹
وزارت امور خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، روز گذشته در واشنگتن با ایمن الصفدی، معاون نخست‌وزیر و وزیر خارجه اردن، درباره روابط دوجانبه و تحولات منطقه از جمله آنچه «حملات مداوم ایران به کشتیرانی و کشورهای منطقه» خوانده شد، تبادل نظر کردند.
🔹
براساس بیانیه وزارت خارجه آمریکا، روبیو با اشاره به این موضوع، از نقش اردن در پیشبرد امنیت منطقه قدردانی کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/450124" target="_blank">📅 13:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9PUtNI0PEv_cvDFZ3XCQYUEsKX_cwXxQ5vbkp1DGvY-4YTEG2J_Niz4oJ1pxzzPB1zc9SrFfQhaj5VKQz19EFeQiK2Z2LF3kEMr91WBDJN_W5InTx_IT894SCKPyaHcOLOow74zPXPn74Gy77tNjokEmWy9TsWX29RcOaAQ4Udh4JO4zbi5q4hkCAmmmYIcsiYscqaQH5uee_rNW8SKgotyVfI_a1MrGe-N4vjBroSdYfMpAPlmjaUrEsnzX0L3E5bjXAOo_cDHWBCpkyDQw1SgNeVBO7D86L6ojqLead8XrpfKjSIk7oNIApEGKAvndZl3LKbbumpv4ZoyODrRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بیرانوند از پرسپولیس به دادگاه CAS
🔹
دروازه‌بان محروم تراکتور، شکایت خود از پرسپولیس و فدراسیون فوتبال را به دادگاه عالی ورزش فرستاد.
🔹
او داوری سه‌نفره خواسته چون همزمان از پرسپولیس به‌عنوان شاکی و از فدراسیون به‌عنوان صادرکنندۀ رأی شکایت دارد. @Farsna…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/450123" target="_blank">📅 13:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLZMLqMF8B8PDAVS6gWZwRtJnWwkc8u10Z9HGjtwjEVnkuBuop0tJC7dGaSzBJRjozO3LwpKNbvHt9o7zPbU02l4Kus7SuWv7vBVno8fdLJmob17YLV6SCrvV7rMHQRb_oYUPpF_RNwqvoL8mqeDjGLDmw5BnZl1gR_rZHHcCoBML8NqksF2FA54ladqhOitaIGtL8EhYn5nKLNya1x3l16ZRqz-4VxmZA6vqxmFOqYxl25AWKIVwM8fLB4BKSpH5a3X4pLdaCkKceByqnK9RfT4bRDDacN2jgrV0z1WF2qPbzzZA00JnQeqfvpXmjS7zGFkBh57J-mMeldxccEIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلی‌آف لیگ برتر با VAR شد
🔹
در جلسهٔ رئیس و دبیر سازمان لیگ فوتبال ایران با رئیس دپارتمان داوری فدراسیون فوتبال مقرر شد که دیدار پلی‌آف لیگ یک برای صعود به لیگ برتر، با تجهیزات تکنولوژی VAR (کمک‌داور ویدئویی) برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/450122" target="_blank">📅 13:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136fc8d572.mp4?token=HYubTdadZ0hNQb4PqWcc65pGh3hmXyyHDINBraXWE-xMItxwuCQGo1pGzCxUzWbpF0_nGUgVaXFeo1-SFoYJbIca7Yk87wmlB1R3-YZh1i3gIksnxQgss_zp2ezj1lQJzMCoDV4Jc7XcX7Z5mKNlvql9zkscc-GhbLhKv1YdTsV_J9Eq23c3AMb_gfQ1ikO003FSlf3RWVjDL9aj5rSiFESnQZ_-v432qa6lLrxY2u7K_pCJfMw-eer_KNCSl_yLc9w7moKEywT5vnRWnuIYJI9RybXdCWSa_T7dXDp-ohNBnxaAl_TYp3JIG-mV45268Hoa3ML_362c8HRko6yYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136fc8d572.mp4?token=HYubTdadZ0hNQb4PqWcc65pGh3hmXyyHDINBraXWE-xMItxwuCQGo1pGzCxUzWbpF0_nGUgVaXFeo1-SFoYJbIca7Yk87wmlB1R3-YZh1i3gIksnxQgss_zp2ezj1lQJzMCoDV4Jc7XcX7Z5mKNlvql9zkscc-GhbLhKv1YdTsV_J9Eq23c3AMb_gfQ1ikO003FSlf3RWVjDL9aj5rSiFESnQZ_-v432qa6lLrxY2u7K_pCJfMw-eer_KNCSl_yLc9w7moKEywT5vnRWnuIYJI9RybXdCWSa_T7dXDp-ohNBnxaAl_TYp3JIG-mV45268Hoa3ML_362c8HRko6yYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر لحظهٔ شلیک موشک‌های خیبرشکن، ذوالفقار و فاتح ۱۱۰ در موج‌های سوم تا هفتم عملیات نصر۲
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450121" target="_blank">📅 13:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfT6bsj_VMlMwrUzmeoO47S22y51O8_bXTEWmHLk_ecCneBeh4_4VpC6SQiaNt6u0vYhCz7zDsDcTOuf6eSYipM-uY_8Y2n2yENyAbbcHIv8keAz8TVviqsyIYigeQGVDrpaASTe1OsKRwl-aCYQuwDxjyQTX_EBDNIw9KvQBdEUkY5kGStFdeDyrrZBBVJQdD0t0uCtpuRc4kMkAkpMBuumlppxxPoILPMfDSiySkJLS5WQ0UcOEJzSbXkstpuUkv7yWwzUOzLntBWrH3ay-UJEaa6Cw_p1AprIkRvabdoLSCtN4YDLIAkYDJCT59sOnuqQ1v75U1lGuf9O0GCcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت حضرت آیت الله شهیدسیدعلی خامنه ای
و داماد ایشان شهید مصباح الهدی باقری کنی
و دیگر شهدای خانواده امام مجاهد شهید
🔻
مکان:مسجد دانشگاه امام صادق(ع)
🔶
زمان: چهارشنبه ۲۴تیر ساعت ۱۷</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450120" target="_blank">📅 13:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3Q74izq7f8JMMteEsIUuYmFBFa_lMKkizNrcZ54WUS02F3hMalSoKMiXq246koFcrsc77yrTzU3l7R-bGwvzG6gHXfWhBoq7z4htk48qvn8i8h5kVVgiPiJsAyxu0L8TmqHa6zMkcEK00j3OW5iBtafdfMlwbbiPcDwny3GpCv6Jzc2h10DjLCtsQq1iwnFMaPaWq6aiFiSQtbB0GrX2Cg6NfYfQNNA1eSBqA71DOXiRCqcK6Up6k60ZgStsiUGlCMKksRiVFqKK7nd7ct6O0Z0PH6SK5NvwcecQqMlzMMLu-5Vw4nDnPylGppF-noxnIK79K5s5EvCyRt_4_G3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران به مناسبت هفته تامین اجتماعی
🔹️
در این پیام آمده است: تأمین اجتماعی، صرفاً یک نهاد ارائه‌دهنده خدمات بیمه‌ای و حمایتی نیست، بلکه یکی از ارکان اساسی تحقق عدالت اجتماعی، حفظ کرامت انسانی، ارتقای سرمایه اجتماعی و تقویت امنیت و آرامش جامعه به شمار می‌آید.
🔹️
بی‌تردید، حمایت مؤثر از جامعه کار و تولید، صیانت از معیشت و سلامت بیمه‌شدگان، مستمری‌بگیران و اقشار تحت پوشش و گسترش خدمات مبتنی بر عدالت، از مهم‌ترین مؤلفه‌های توسعه پایدار و پیشرفت کشور است.
🔹️
بانک رفاه کارگران به عنوان بازوی مالی و بانکی خانواده بزرگ تأمین اجتماعی، همواره افتخار داشته است با توسعه خدمات نوین مالی، حمایت از تولید، تسهیل دسترسی ذی‌نفعان به خدمات بانکی و پشتیبانی از برنامه‌های رفاهی و اقتصادی، در کنار سازمان، در مسیر خدمت به مردم و اعتلای نظام رفاه و تأمین اجتماعی کشور ایفای نقش کند و این همکاری ارزشمند را سرمایه‌ای گران‌بها برای تحقق اهداف مشترک بداند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/450119" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/450118" target="_blank">📅 12:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
اقدام ضد ایرانی انگلیس این بار علیه سپاه
🔹
در ادامه دشمنی‌های انگلیس علیه ایران، لندن نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی تروریستی قرار داد.
🔹
شبکه اسکای نیوز گزارش داد که «بریتانیا سپاه پاسداران انقلاب اسلامی ایران را در فهرست سازمان‌های…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450117" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aElTJtf6sC9emjjLtz2NQQLrmK35qWUGNSytHZOc-UNao-3GQfBYOeKZW71nvNrQ6SRtBZfGXYvfvZ_Vr01UceyfrjX8jKijL7bIvMLLXqENMgQWzdGqXpQgPSLMuD6bxZ2xUyGqF72U0BY8ykUJGHupEQi1T2hx-Mmdi6gRRYEBAfA0SK7mkZQyeIVaxYz37lfltJPRare622P-FoCZ7IoUAeNTCE0nH5aeFQaNjlS1JfvzigUbLzL2tTKNZiGYH2dTfZIs20fVYX009ehH1L09BoVj86oYmj3ImgZdBGQ_7i1CRROdIMWJGOUFAOHgz_o50VTjD0Eqi2RjBBj9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۴ میلیون و ۹۰۰ هزار هم پایین‌تر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۱ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/450116" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">راهکار خروج از بازی دوگانهٔ ترامپ؛ «پاسخ صریح» جایگزین «واکنش به پیام‌های پشت پرده»
🔹
برآورد اندیشکده‌های مرتبط با حوزهٔ انرژی نشان می‌دهد، ضربه به تأسیسات نفتی منطقه، می‌تواند توسعهٔ کشورهای غربی را تا چند دهه متوقف کند.
🔹
به‌گزارش فارس، در تازه‌ترین اظهارات شب‌گذشته، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تهدید کرد که «پل‌های ایران را می‌زنیم و هفته بعد زیرساخت‌های نفتی را هدف قرار می‌دهیم» و بلافاصله افزود: «مگر اینکه ایرانی‌ها پای میز مذاکره بیایند.» این الگوی تکراری در ماه‌های اخیر، نشان‌دهندهٔ استراتژی همزمان «تهدید علنی» و «ارسال پیام‌های فریبنده از پشت پرده» است که هدف آن، القای تصویر «تسلیم‌شدن ایران» به افکار عمومی جهان است.
🖼
اما پرسش کلیدی این است: راهکار هوشمندانه برای مقابله با این شانتاژ رسانه‌ای و سیاسی چیست؟
۱. الگوی تکراری؛ تهدید در ملأعام، وعده در خفا
🔹
بررسی تحرکات رسانه‌ای و دیپلماتیک آمریکا در ماه‌های گذشته نشان می‌دهد که کاخ سفید همزمان با مطرح‌کردن تهدیدهای نظامی، از طریق واسطه‌هایی نظیر عمان، قطر و پاکستان، پیام‌هایی مبنی‌بر «امتیازهای غیررسمی» به تهران ارسال می‌کند. این پیام‌ها که اغلب وعده‌های  فریبنده و غیرقابل اعتماد هستند، پس از مدتی در رسانه‌های غربی به‌عنوان «نشانه تمایل ایران به مذاکره» تفسیر می‌شوند و روایت رسانه‌ای آمریکا را تقویت می‌کنند.
۲. چرا پاسخ به پیام‌های پشت پرده اشتباه است؟
🔹
کارشناسان راهبردی معتقدند که هرگونه واکنش به این پیام‌های غیررسمی، بدون لغو تهدید نظامی و رفع تحریم‌های قابل راستی‌آزمایی، عملاً در دام بازی رسانه‌ای ترامپ افتادن است. آمریکا به‌دنبال آن است که با القای «فشار حداکثریِ مؤثر»، ایران را در موضع انفعال قرار دهد و سپس هزینه‌های جدیدی را تحمیل کند.
۳. برآورد اندیشکده‌ها؛ ضربه‌ای که توسعهٔ غرب را دهه‌ها متوقف می‌کند
🔹
پژوهشگران حوزهٔ دفاعی، انرژی و توسعه در اندیشکده‌های مرتبط، برآورد کرده‌اند که اگر ایران به تأسیسات نفتی منطقه‌ای که به‌صورت مستقیم و غیرمستقیم از آمریکا حمایت می‌کنند، ضربه‌ای حیاتی و کلیدی وارد کند به‌گونه‌ای که صدور نفت از منطقه برای چندین سال متوقف شود، پیامدهای آن فراتر از یک بحران موقت خواهد بود.
🔹
براساس این برآوردها، چنین اقدامی می‌تواند روند توسعه در کشورهای غربی و به‌ویژه اروپایی را بسته به‌شدت عملیات ایران تا چند دهه متوقف کرده و حتی به عقب بازگرداند.
🔹
وابستگی شدید این کشورها به نفت و فرآورده‌های منطقهٔ خلیج‌فارس، به‌گونه‌ای است که هرگونه اختلال بلندمدت در عرضه، زنجیرهٔ تولید، حمل‌ونقل، صنایع پتروشیمی و حتی بخش کشاورزی و خدمات آنها را با شوکی جبران‌ناپذیر مواجه خواهد ساخت؛ این هشدار، نشان‌دهندهٔ اهرم بی‌بدیلی است که در اختیار ایران قرار دارد.
۴. راهکار کارشناسان؛ «پاسخ صریح» جایگزین «واکنش پنهان»
🔹
تحلیلگران حوزهٔ دفاعی و سیاست خارجی بر این باورند که هوشمندانه‌ترین واکنش در شرایط کنونی، «خروج از ابهام و اعلام صریح پاسخ متقارن» است؛ به این معنا که ایران باید از طریق کانال‌های رسمی و معتبر (سخنگوی وزارت خارجه، فرماندهان نظامی و یا بیانیهٔ شورای‌عالی امنیت ملی)، به‌صورت شفاف اعلام کند که:
🔸
هرگونه ضربه به تأسیسات نفتی ایران، به منزلهٔ بازشدن پای تمامی زیرساخت‌های انرژی آمریکا و متحدانش در منطقه به‌عنوان هدف مشروع خواهد بود.
🔸
در صورت هرگونه تعرض، تأسیسات نفتی عربستان، امارات و قطر که نقش جایگزین برای تولید نفت آمریکا را دارند، هدف قرار خواهند گرفت.
🔸
باب‌المندب بسته خواهد شد و تنگهٔ هرمز به‌طور کامل به‌روی نفت‌کش‌های متحدان آمریکا بسته خواهد ماند.
🔸
همزمان ایران باید در فکر کشته‌گیری گسترده از نظامیان آمریکایی در منطقه باشد.
۵. هم‌زمان، قطع تعامل با پیام‌های فریبنده
🔹
کارشناسان تأکید دارند که ایران باید صریحاً اعلام کند: «تا زمانی که تهدید نظامی لغو نشود و تحریم‌ها به‌صورت قابل راستی‌آزمایی برداشته نشوند، هیچ پیام غیررسمی پاسخ داده نخواهد شد.» این اقدام، ارزش پیام‌های پشت پرده را برای آمریکا به صفر می‌رساند و مانع از سوءاستفاده رسانه‌ای از آنها می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/450115" target="_blank">📅 12:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwyYtJrHFT8NRkHhb56NjAb_k2RvNY5ribAJrocfYkrOBOU_j18AyI08dE3CbX_ZXTmTdEIUSo9vhtMo8-yW_Q4wO-kfKIDUtprxkWglu6l1NOvtH5K3i1fIeyTrMmJ3DYmtW53l1hkuGGWi39dlG6hA2RmxLNgAldqUOYIYNLTwoMOJMRAoopv18Ln2ozX6-M65WxgXcV-YbA6WifXB7DcCD7eDs-9XXZfmNJzFPNkT-kNi_pFKYxhgi0N9q4-rFcl4_ClybuqJJSBgqMXky-2U9DRa6qp0VfqCW5etH3OhIkkUSBxxuhCa0CfBwiAQs1eD7L0CyUHZC4HEaY9vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5v7cTJh_LJIbIMo_7jN0A_OUdC1tHVYrNQkDkmgNDjfeqbIix70679EVdxgdNMupNbqiks5hBeRgEMYOvWtvlX2O53cK888TCDyJLOO6CApGij1DH8vTt4Rl5OhR7MPSXNgsfY5akOy-VweMmfk37sDAJnbwsSe44rDqMylrZYGTV-qV8L4uGS1jYReaLs46-FZAyOGG_x_aij19wTeQ-aTYuGpU0PDfNu6WdagO-JmwXHCawA6b6gQbSXaupIRnbkAJmSEBtS5dhm_GdnbmMgStN60O7ZN_vRED6ClBkskZmbZ2Bazw0vlI8srf5W-E_0TB0eBaWmQjgI2FML8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ppr1L9umqBigkGi8aH5R5ECbUiOQI3IM1Oqv_TyspNY7Ia7_2ypIBnl6maV8J1dMu5wQRfnVFE51XqbU2BhymjxHOJNjq-AjgPsrU8WRWqRc2KvP7yCRGcErPUM4oA4XpJbhqyPYxNF-UrINvWw4oUWDGR7mefFbiCNhK5VDEbPyhQej3ogkGlosiEwv9y1iLfKg99E_Uh1MYuVFjbdHnRYzzYPmXHoVLW8UfIoAz8d2YvbfS-GlgaW1VsNYQ5h7V5lsMG_ptGkoLLjqgaPtdnkfJLDo8nWY5JRfswQD-IMzOxEGVVpHaaAlZUOaKVYHdjvxyppDOb8JRiH0WYMy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c04J9H3hEusB5bF3Ki0HlVR9xe7fsEQybAXY2-IjPSd8jR46Xo4r8alHTH_rMKw-wXTgwVPqxz-0RDG2_-VKBfab0ZH0ZGj2dwPoK2XWe8YFXNnAJ1MlCpF41F8NLNjLrGF_cizzoIIQrsAc1HE-ztVh8SPUx98Ea7HaHwTMc_NsJfQBgrM8gygcm-f-KimJvYa2Tiu784I_61pU6_Jz5qR8kHEuOVub6GIlCXlYd023NbnRb4LB6fT2YiBY3_aE0wbr32TcG2Sq1ZHR2rcVLvRtZ2kPqjoeXjWaSUQa2NTC-3H5yXvEZIrCUi20ryB0ujFbnjxSip_dGODQayysYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXUz0KV_43HI8yJoeuYbzqkDy5ecsAgeZ7PLfFaGrWRj5YMXCEoiC4U8N-c6iE1amvD6xQgKw3V6MLzU4cGC_mgFg2-pS8S6ACXFXVv3MxhrQ5brdsJ2z0KmhHvN5b96lV_Uk6eOm0fOp0dwdz_CPcHqqKCNU_6vHibJyIPXRBGct_PX9Fp5AGtZ2Ixno4YfZ-40PJsB_g5YzVL8UQH1LB3QGQQAOAvdSTypRgPuXvHwemz4H5hldK4SCLVTMCyx0UtxxxlyMnguFaIUTSkistMCv7jmu4WIMsDhBrbeCm8xoPyF7oxKQwnwHRuiUhZSjaQYYDajTS73VEyqZdIPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر شهید نیروی دریایی سپاه در حرم حضرت شاهچراغ(ع)
🔹
آیین تشییع پیکر مطهر سرهنگ پاسدار «شهید محمدناصر دلیرور» از شهدای نیروی دریایی سپاه که‌ ۲۱ تیر در جزیرهٔ فارور خلیج‌فارس توسط دشمن آمریکایی به فیض عظیم شهادت نائل آمده بود، در حرم مطهر حضرت شاهچراغ(ع) برگزار شد.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450110" target="_blank">📅 12:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPiwq6JJZNuqLfUEYUReUjMgJE62pTa0Xa0OrCEzcFCNVNuTwz1rxI9iIIE8LnookurMlEjYw3awW63bNNzz3tH64pnc8Sy5tYg8EfMz0YABMcMgIJGmvwsaoHkygykWSYXRA4gO9d28x3ut42lmToMkjlwHIWTs95Js9BgfEH5joxVzLqwocv3tOjPxiJOCUEYpQaH9QUU-culmWOkS1XFl4KUHJkRCGCOGwOKNHECRu-0s2rgmq0xLon7X-7-zBleCHaKa_gVSWQUKfqPAKa92kSKsPVlJ_Z_YhVn0HJFhEnNQ6abunAkLTWLM7Vv1Ld2nH4JC7DWZBft9m-c9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt9lesbRzvmrqRd-9DhVCaeEIJWnHjrGsP3LEg2F8AUKI3U-xoACQBYTMfmP6fXZ0XFoayDPKrACNYw7dJR8ZHg_12EUuKFvzUVxJcF7bKffJTSzKwCNpxTZA4rK958o_D3xatTjbmx0uyJEfHcEmpaKnEkfc0ht7v869HwLvMm5Qpt_3raz02Mi1nK0VplLxha4wbgDmlRg0MC_JzmuUnAmdH7C6Ox-szWAxh2UrY6PL1LXBsbG8SJPSPh8oUeXvrXAaXbAQlLg57dZ1m6F_armSEqHDCavWprX6GkrqDNV3Bgg7jbUvw8gdDKNlsXVHySTrOA8KOfv0Xk_pblrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsPIHq9flEWywuwZWnkJRqlH7tqCPDBfCaIpdGXUApoS5t5zKpqU8P4_SxX2xxYUtCe9r5meWg6A8V2bIW8wMtPMCspH-HAnrefKzUjFUxwq7ZgDMoXv775SjBGqp-K2BOobuVoybMskhnOxZ4wKw-gnw_67rOGOEdnSZVyViKMOsoBNp4Zj2hkfXYU8oM1m1mSEr-iGj6w4UjQptPV9Hexd2Cy5mC5q33WcSBjy6O2IeKaRwj8FCGbF0IrIEBTje4erMZ97vCMNuYkFVmiZwNU8J0KA4sFJU5BKezkdxW_XdWrd7GsQJbhiiv3jZ5L2weDm5IwM3jn1Nj-y09YqRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نقل قول جعلی منسوب به مدیر روابط عمومی صداوسیما
❌
به‌تازگی پس از حملات آمریکا به بنادر ایران، تصویری با ادعایی منتسب به «افخمی، مدیر روابط عمومی صداوسیما» منتشر شده که در آن گفته می‌شود: «شهرهای حاشیه‌ای ایران اهمیت کمتری دارند و باید تلاش کنیم جنگ به تهران نرسد.»
✅
این درحالی است مدیر روابط‌عمومی صداوسیما «حسین قرایی» است، نه افخمی. همچنین تصویر منتشرشده در این شایعه نیز مربوط به آیت‌الله مظاهری است و ارتباطی با فرد ادعاشده ندارد.
⚠️
به‌نظر می‌رسد هدف از انتشار این ادعا، تحریک احساسات عمومی، به‌ویژه در میان مردم جنوب ایران و ایجاد شکاف میان مناطق مختلف کشور باشد.
@Fals_News</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450107" target="_blank">📅 12:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctXS0cNtpl83PJJXAd7kfAgSTDNUitk2JuQpsG6B36G7CTWgqYC5uZxYE6lrzqLR5UkKmbH1veq3YmEMHvR9CjWGotLzcEQaUwXGdson-vZPTzMUx1DrSa817qXNxu9wx4gr7eBEBYQSSqqQnRnO4bP8_nJa4GMWUJwy04CMXgXzFD6Umf-wNuXi1cZiqaDaZKJLLlqL64mJDJGHXWgx1b80wlD3_H53cApU2UCG0wmhlAf6GF-BNF5oLOWL8VhcPkD-lWiTjMd-bO4ZtUihA7COhtALXdSEEODZ7-O9wOmlBLkmUgbQuEj7CjAhFOoB_PQcjnNgInMiaD66hdZvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ارزی ۲۰ ساله برای یک شرکت سیمانی
🔹
وام ارزی شرکت سیمان بیارجمند که در سال ۱۳۹۱ از محل حساب ذخیرهٔ ارزی دریافت‌شده بود، با پیشنهاد بانک مرکزی و تصویب هیئت امنای حساب ذخیرهٔ ارزی و هیئت وزیران، تا سال ۱۴۱۱ تمدید شد.
🔹
براساس این مصوبه، دورهٔ بازپرداخت وام ۴ سال و ۶ ماه افزایش یافته و مجموع مدت آن به ۲۰ سال و یک ماه رسیده است.
🔹
اگر شرکت در مهلت جدید اقساط خود را پرداخت نکند، جریمهٔ دیرکرد از پایان دورهٔ استفادهٔ قبلی محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/450106" target="_blank">📅 11:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450105">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi8WOmcRzuV8R9IooIL3rE-65DiE5OYSdY1U8ddriv_OwbovkxLNbQc3kQ0y1k8PBvh4fpU7UcmQ0Phn60tei5QjRQUahnPD-p1cojHNkwZLEDjPKxsohb4ShHG4hPiOKoMP5kDfdclc8pxNpYikbcGmUBLorDRgmbIPeNFrRAcVf66qbJ2pwt4ymY9RgvVz2wCLNajKTMMMzn0oWSQew3OFDnowRi-D58R6e1FUHO6fNW-wyCX3jE2s1VVVq_zdji3x9seo_J3VLfOKS3B63ux1LXQ-oW_KHT0G0yJ4LBYMxpNJDsfRv5Gb829F_8d5yGt3iB_2XVbcWzDNQbeSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت رهبر شهید انقلاب فردا از ساعت ۱۷ تا ۱۹ در حرم حضرت عبدالعظیم(ع) برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450105" target="_blank">📅 11:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450104">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa32169e4.mp4?token=dCze-0DlL4vz2I-QJJHnTe-64bQ-Dm-Fiduve97t5TVQWb4Sd1wHrMadQupsj6h-xyTihCvo2I5xvY54T8AZ_gAEvPox8D9F2pNU4bWPXUugt-n7nluD2u_DJ3LfsfdmGHwxDUJAomDiz6Tqx5HwoWgxQQ1Fbg4BwGWRf1n1rEnKCeKGaSOWt0aS8ZUZYA-1PRsP720b7DQFJbMUX0C4j4uXfVN_GgaULB71uOAlRObJixnGZ8d92YXFJziEQiPwJW5yNbSUtPptklMO7_GU5xJoeW6ZIh0EDYUKn_c7Bqppm29Tch9na88xRv8vt-e0DKrnGkYpVsouRhnLuLpgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa32169e4.mp4?token=dCze-0DlL4vz2I-QJJHnTe-64bQ-Dm-Fiduve97t5TVQWb4Sd1wHrMadQupsj6h-xyTihCvo2I5xvY54T8AZ_gAEvPox8D9F2pNU4bWPXUugt-n7nluD2u_DJ3LfsfdmGHwxDUJAomDiz6Tqx5HwoWgxQQ1Fbg4BwGWRf1n1rEnKCeKGaSOWt0aS8ZUZYA-1PRsP720b7DQFJbMUX0C4j4uXfVN_GgaULB71uOAlRObJixnGZ8d92YXFJziEQiPwJW5yNbSUtPptklMO7_GU5xJoeW6ZIh0EDYUKn_c7Bqppm29Tch9na88xRv8vt-e0DKrnGkYpVsouRhnLuLpgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا هم نتوانست شاهرگ نفتی امارات را نجات دهد
🔹
موسسه تحلیلی HFI: بندر فجیره، یکی از مهم‌ترین مراکز انتقال نفت امارات، عملا از فعالیت بازمانده و آمریکا نتوانسته از اختلال در این بندر جلوگیری کند.
🔹
توقف فعالیت فجیره می‌تواند تأثیر قابل‌توجهی بر بازار جهانی نفت داشته باشد؛ شرکت‌های کشتیرانی نسبت به گسترش تنش‌ها و تأثیر آن بر مسیرهای صادرات نفت در منطقه ابراز نگرانی کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450104" target="_blank">📅 11:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwQX1LHezGP8EAug7HH4oB5H5lLDCj2LLIoBZqXIAR9bRBLUfnYFMV-AmhL01QNPVy4cn0mbkjhwGCHufolt-SGxTL7FfTgeOZ-orp-iyI_9S4wGowikJRUTW_JEapUvCGQv1F7gMNUXPYei3EyqCZKb0_c2S3m5nuqMrygdSECac29RD_B4VrFqrGfRYT74EriwYTxNAl390cgoxZBoEw1zs4sdzeN4UcCDTASuovX2FjTbwbp6WNK5N3maNHn762pHgebVEIaBMcJmh9yN8ZWYbJL7WmUL2YzBnClM_sqCjCWFx7x0DS08x2u1ukWpAiWprySktFCTT65OH-J3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما ترامپ را می‌کشیم
🔹
طرح جدید دیوارنگارهٔ میدان انقلاب تهران با تصویری از ترامپ در داخل تابوت
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450103" target="_blank">📅 11:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a8f0d96e.mp4?token=ex4hTEu7PFt32CqXzERY9xshhHPZN3v6tFlLqCB9U1cXqUzXXg2hXp9rVdGLWnjbaNQqsWL1DUr05hC14mfybrc-Qm3XuuHSRHDNGaG8-KXP2kmkJby6HK8nBnBoiCSTpiiaYy1WgZBNJbQbFd4GoDOpxyuLzBaftulpMgg4xPWegxzzMQ509CnRLexnrv07euWyxjetYXr1TGtaB2E-TVG3OebY1pHBHk5xUZrMa42aA3LeS2gjem3l3iuVz_ZfscSLNS1EKDhzpyGVW0E4a9rvyEZSpb90DxeX2BrTcu4uP1jAl-cYFwF-I9QJwrbpUEoCUOvn7iwUrWTjc_BNRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a8f0d96e.mp4?token=ex4hTEu7PFt32CqXzERY9xshhHPZN3v6tFlLqCB9U1cXqUzXXg2hXp9rVdGLWnjbaNQqsWL1DUr05hC14mfybrc-Qm3XuuHSRHDNGaG8-KXP2kmkJby6HK8nBnBoiCSTpiiaYy1WgZBNJbQbFd4GoDOpxyuLzBaftulpMgg4xPWegxzzMQ509CnRLexnrv07euWyxjetYXr1TGtaB2E-TVG3OebY1pHBHk5xUZrMa42aA3LeS2gjem3l3iuVz_ZfscSLNS1EKDhzpyGVW0E4a9rvyEZSpb90DxeX2BrTcu4uP1jAl-cYFwF-I9QJwrbpUEoCUOvn7iwUrWTjc_BNRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا هوش‌مصنوعی جای تراپیست‌ها را می‌گیرد؟
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450102" target="_blank">📅 11:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450101">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4iGr43Nin2RjHaZQx7FX12ULmPho52swAuYJi5pB8MXatCoMMB0KLieKETx6gOPlqS7HhfTXy0nIvBzfZi6U7Z0SavwhvAkD6N8Fn5EIA-MvrzWoXYQjUSv1sGyZSYPu93YigeLj1FGylq2yc0p0wnOFR3-3G4vUrWRjAqDoj_s2_myivclcRBxY4j6KOAbCIoif--lwmDSsL9EcpIUOeVE1_eT3tOnE7d3c7MVl_aLUC0DGsIOCIvlY6AMCGjAg9JMNBFI11ePY19Oeb51r92vXq8Yb3NnqbhlJUC4kIdKvM9gMih44sF1DQJSza8DLqZ34d2_dpScPKa6grY5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهندس نظامی شرکت صهیونیستی رافائل بر اثر حملات ایران به هلاکت رسید
🔹
رسانه‌های صهیونیستی اذعان کردند که مایکل کاتز، مهندس نظامی شرکت تسلیحاتی صهیونیستی رافائل، بر اثر «جراحت‌های واردشده در حملات موشکی ایران به حیفا» در عملیات وعدهٔ صادق ۴ به هلاکت رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450101" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
استانداری اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در جنوب اصفهان، بهارستان و صفه تا بعدازظهر امروز، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450100" target="_blank">📅 10:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عامل آتش‌زدن فرمانداری و کلانتری دهاقان اعدام شد
🔹
محمد امینی دهاقانی فرزند حسین از عناصر همکار دشمن که در روز ۱۹ دی ماه سال ۱۴۰۴ اقدام به آتش‌زدن فرمانداری و تخریب اموال عمومی در میدان امام حسین (ع) و کلانتری شهرستان دهاقان کرده بود، بامداد امروز پس از تایید حکم از سوی دیوان عالی کشور و طی روال قانونی به دار مجازات آویخته شد.
🔹
براساس تحقیقات انجام‌شده و مستندات به دست آمده از پایش دوربین‌های مدار بسته و اعترافات متهم، محمد امینی دهاقانی در روز ۱۹ دی سال ۱۴۰۴، اقدام به روشن‌کردن و پرتاب کوکتل مولوتف سمت فرمانداری دهاقان کرده است.
🔹
متهم در اعترافات خود گفته کوکتل مولوتف را به سمت فرمانداری پرتاب کرده است.
🔹
وی در بخش دیگری از اعترافات خود گفته است همراه تعدادی از افرادی که در اغتشاشات حضور داشتند سلاح گرم از جمله یک سلاح جنگی کلاشینکف بود.
🔹
آن‌ها سلاح را از ماموران دزدیده بودند. از آنها خواستم سلاح را در اختیارم بگذارند که با آن شلیک کنم.
🔹
براساس مستندات به دست آمده از بازبینی فیلم دوربین‌های مدار بسته، متهم نقش زیادی در تحریک و دعوت افراد حاضر در محل به حمله به کلانتری و پرتاب کوکتل مولوتف به سمت ماموران مستقر در کلانتری را داشته است.
🔹
متهم ساعت ۲۰:۳۰ روز ۱۹ دی ماه ۱۴۰۴ جلوتر از جمعیت حاضر در محل به طرف فرمانداری رفته و یک عدد کوکتل مولوتفی که زیر کاپشن خود پنهان کرده بود را روشن و به سمت فرمانداری پرتاب می‌کند که منجر به آتش‌سوزی می‌شود.
🔹
محمد امینی دهاقانی در اعترافات خود گفته همراه خود دو عدد کوکتل مولوتف داشته که یکی را سمت فرمانداری و دیگری را سمت کلانتری پرتاب کرده است.
🔹
در نهایت پس از طی روال قانونی، حکم اعدام محمد امینی دهاقانی بامداد امروز اجرا شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450099" target="_blank">📅 10:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450098" target="_blank">📅 10:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTRq4y2ugFYqj3o47nVPF527AwG56-lDQzbFRB6BFXULy8-jy-F4kgoHYFS7XJZEP-3jNZ2ZDposZid0XpilhiU66YrNI8GoR6KtAh0ilRE7R8e2Vhw5MRkmoAyaTm00K-48JF2FTwhlxDUGduFCk0B0-mfa6Jzd3YJMs4fk0ScoCS7DRd-JnFnERNLh2zcrEIU5rNwZqYWIqDkqTtL1aGuqWNrzEOGHxZVb9tEVsk9aNOzxIFmkFyo6FyU6jgsmc3CPiVCq2b8XgeG8frRRjTF0xI5c32wNiUJV0Z7G152f75pi2b3CSwMi_S0kUMsoqG7ZjKI8hdYMDtkHT7twJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
واریز سود سپرده‌ها به حساب مشتریان بانک صادرات ایران
🔹
به دنبال رفع عمده محدودیت‌ها در استفاده از سامانه‌های بانک صادرات ایران، سود سپرده‌های بلندمدت به حساب مشتریان واریز شد.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، همزمان با تلاش شبانه‌روزی تیم‌های فنی برای عرضه سایر خدمات بانکی باقی‌مانده، سود سپرده‌های بلندمدت، مربوط به دوران اختلال سامانه‌ها به حساب مشتریان واریز شد.
🔹
این اقدام در راستای بازگشت سامانه‌ها به چرخه خدمت‌رسانی مطلوب و قدردانی  شایسته از شکیبایی و همراهی شهروندان انجام شده و نشاندهنده این باور همیشگی و راسخ در بانک صادرات ایران است که بیش از ۷ دهه اعتماد ارزشمند مشتریان، مهم‌ترین پشتوانه برای عبور از چالش‌ها و گرانبهاترین دارایی در مسیر تکرار موفقیت‌هاست.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450096" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ_OIAyBoP1drOZg-x5IbHne1CqtONTVku4HiRhiqRCwYSWWaalW5TP9FlPokYjD9i5n2K30erYeEfMmAAxxirQF3MVFYPpn5LYff11yxKnDbWZ2jH4TCPxKRn1Y9OkiiEy-uMFV86JhPIyeIJmd7Z0NrrjKmnxtEVD1p6Gr7PK_0rw7h56e8F5W8CIAVlbdm2y-soCnkzUCn94hgZw7Df1yKc1AeryvWWlR5qY9gb_oYuTejeE_DPtjLWoRMdKIMEd42y5MAZG63TSJ23M8wLtsUA4GUPlqGMh2HSwmUOh9qo8hLzE8GaA04yRNsWUK-bt-VqcTRVBfweutvXo1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450095" target="_blank">📅 10:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450094" target="_blank">📅 10:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdNL44sQv_-KnSwZMlIMrtc78_DuJgXssNI_YA7zKp3LoQCCU-SPfUSi-uii67n90WTj0cMmvCnEN3I8gKCs8fbzdOj_rQzEYM7zTXuIHwgJTM4m0Kamv1illb0NTt-BayOjj3U35j_B4dVKOfAh1fZC3ywDrxv-QskfCNZgQNkBfwX-iGWxS5gvl_nT_fmTw5hzBaDhzO9hfkU009T_f7j8qu1b89rc86lkymWM2a0UhQyLCu6xfAIWQcqezmzWK8q3XOZvtWIAMADxkvcJ102eD3iuNxFu3LprX10xBmmHYVCi4kWhBHmzYiBrQi4ykGYONCFXIx2HKQOCYxE4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی دولت: در حملات روزهای اخیر به جنوب کشور، بیش از ۳۰ شهروند غیرنظامی به‌شهادت رسیدند
🔹
ضمن ابراز همدردی و تسلیت به خانواده‌های داغدار، یاد جان‌باختگان را گرامی می‌داریم. دولت با تمام توان در کنار مردم خواهد بود. جنوب ایران، قلب تپنده این سرزمین است.جنوب ایران، جان ایران.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450092" target="_blank">📅 10:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
معاون امنیتی استاندار بوشهر: مناطقی در شهرستان‌های دشتی و تنگستان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450091" target="_blank">📅 10:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bcd8a1985.mp4?token=AXxcYf27swTxqz5QUkJVMVwAYfE_XLXyD450GiYHsc28VISs6fmp3NPwk4rX0FaGHPFhwyoj1rZK2Wj3_wGrLymEpN6C7jkfe1PQKj601_z_ita8qqRJlCYLU97_Fm7QJorle7zNzHWOhyjBhHBCI2m7piclc4hj0PPTgGDT6JfL1wwAhjMSuq-w8OxkdmkfV6lA32vvHT6HhvBoaFM--nkWnoHFjGn_rKJLzU1Ze3XYM7rj2hNbep46bCEaeiFV1MLUVj4H3-0zTZ4gY5hsnpFyVzuoz0dhRyZOaX8uZ6RQSQP0Qvwqjowr_hQdNIGeI3fR72Of-84PCoFRTBX_VJQzv3aShjAs14rbK1O-9eLSAjRTPlFB3i7KEaUMAPKAj7_hkGdP0H0Se1Qc6jB9wWQW8OA1pG_OCe_yAP-JtVE5sfPrAqtEWKUI-B3RIIs2p-NT47iChQibCDPXHy0C6Dd4kMvtbHVBC2-onsT1ok-pFj-UPVDqJQb16iblA9J5LnJ0Yo7XlRPCXCLOE8KFixsEIWJkCEOwIBDwH5Ijll2xw9mt10-gpHePvQcdPEb2obAIX0KRbCJT38KFHlmXg1x-B1cCib4Yg5nrueehUhsyKV0LTpNx5am-8U40tL2PWnbg1cqBEVOyhW0s4CtaVe6qig2GyyVgQW4lOwCCU54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bcd8a1985.mp4?token=AXxcYf27swTxqz5QUkJVMVwAYfE_XLXyD450GiYHsc28VISs6fmp3NPwk4rX0FaGHPFhwyoj1rZK2Wj3_wGrLymEpN6C7jkfe1PQKj601_z_ita8qqRJlCYLU97_Fm7QJorle7zNzHWOhyjBhHBCI2m7piclc4hj0PPTgGDT6JfL1wwAhjMSuq-w8OxkdmkfV6lA32vvHT6HhvBoaFM--nkWnoHFjGn_rKJLzU1Ze3XYM7rj2hNbep46bCEaeiFV1MLUVj4H3-0zTZ4gY5hsnpFyVzuoz0dhRyZOaX8uZ6RQSQP0Qvwqjowr_hQdNIGeI3fR72Of-84PCoFRTBX_VJQzv3aShjAs14rbK1O-9eLSAjRTPlFB3i7KEaUMAPKAj7_hkGdP0H0Se1Qc6jB9wWQW8OA1pG_OCe_yAP-JtVE5sfPrAqtEWKUI-B3RIIs2p-NT47iChQibCDPXHy0C6Dd4kMvtbHVBC2-onsT1ok-pFj-UPVDqJQb16iblA9J5LnJ0Yo7XlRPCXCLOE8KFixsEIWJkCEOwIBDwH5Ijll2xw9mt10-gpHePvQcdPEb2obAIX0KRbCJT38KFHlmXg1x-B1cCib4Yg5nrueehUhsyKV0LTpNx5am-8U40tL2PWnbg1cqBEVOyhW0s4CtaVe6qig2GyyVgQW4lOwCCU54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی رسانه‌های معاند اشرار مسلح را شهروندان عادی جا می‌زنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450090" target="_blank">📅 10:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از فردا اعتبار سرپرستان خانواری که رقم پایانی کد ملی آن‌ها ۷، ۸ و ۹ است، فعال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450089" target="_blank">📅 09:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450088" target="_blank">📅 09:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=n0nJ2HMYNpwPGH8Y0ONafrANFZsM0h4D_3r4hlK6GKJfy3wAOLHwVAPQLR6XRJuLR_zBIWe-SI1dgH-qdY-TkgJnTLUJueNDccDC8KvHdjuuYTYCH2Ys4yJ4RN6OtZB1VZgX5juYAcOZVuzBK9-Tm3ePREXgHBKqdbG0u643JNwoN6hAgZwXsHaOmb_fxt7THZG4qUTioyGXO1q-TRwZAqC9njX6ARpn-2Rgkxdx0xu5j7pLA5Mmd426YwYImAu2pJZymJ2Gta34T6ovWQ7HRWbdyM36NjMQ8S0vmZk1IOTCimuJIqIyWUQw__r7rBmLuhKVnaNd1UZsBCcPVeTKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=n0nJ2HMYNpwPGH8Y0ONafrANFZsM0h4D_3r4hlK6GKJfy3wAOLHwVAPQLR6XRJuLR_zBIWe-SI1dgH-qdY-TkgJnTLUJueNDccDC8KvHdjuuYTYCH2Ys4yJ4RN6OtZB1VZgX5juYAcOZVuzBK9-Tm3ePREXgHBKqdbG0u643JNwoN6hAgZwXsHaOmb_fxt7THZG4qUTioyGXO1q-TRwZAqC9njX6ARpn-2Rgkxdx0xu5j7pLA5Mmd426YwYImAu2pJZymJ2Gta34T6ovWQ7HRWbdyM36NjMQ8S0vmZk1IOTCimuJIqIyWUQw__r7rBmLuhKVnaNd1UZsBCcPVeTKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام دقیق مرکز تعمیر و نگهداری جنگنده‌های پایگاه العدید قطر
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450087" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4d8d5241.mp4?token=BdltIX5jRmQlDMHbl5m_sA1Ll-b12CcqEArx4MP_moFWj1i8SpWafCZ1SsYpHgMT_gc_zjxftAIYekBxkzYK-2E_na90S4IGTJWIbyYWYmr8XEIpkR2YSTy9WAVqy22UFZoOzmE-3wVslamqKnh_M4-22z1rZoiDrKejcMO-rAP2mJC7UgNQgFL-RXukn-iSC4qViSeOgo21cOds-hICj39RNTOfahyNqlhasdqtnXeIx4l3N7egUtl4sc5bUKlzwHsnU1e1RkzMou26Cz9Fgn7veC-xt20b_RQNOBfOLftnEstAVBTch0ZmnnrsTMysvnlW2h3bTOsNJDBy7tTECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4d8d5241.mp4?token=BdltIX5jRmQlDMHbl5m_sA1Ll-b12CcqEArx4MP_moFWj1i8SpWafCZ1SsYpHgMT_gc_zjxftAIYekBxkzYK-2E_na90S4IGTJWIbyYWYmr8XEIpkR2YSTy9WAVqy22UFZoOzmE-3wVslamqKnh_M4-22z1rZoiDrKejcMO-rAP2mJC7UgNQgFL-RXukn-iSC4qViSeOgo21cOds-hICj39RNTOfahyNqlhasdqtnXeIx4l3N7egUtl4sc5bUKlzwHsnU1e1RkzMou26Cz9Fgn7veC-xt20b_RQNOBfOLftnEstAVBTch0ZmnnrsTMysvnlW2h3bTOsNJDBy7tTECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام دقیق مرکز فرماندهی پهپادها در پایگاه ناوگان پنجم آمریکا در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450086" target="_blank">📅 09:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cao4UYrMbH7G8PwZQpMI7R5W-B0OQ1xyUycqM7r1z4EYIUI-ut4dy7GwwlPQKnpvt7zygsPLChUMvbSjOC-hU4Ldd9R2ncccLLYxqo48nKoLc0DxRnv-d3NyYoDlj7vnqgbQ1IvtssdLOpZaNG7DGOQ5kh5xbTJ6tTfCT6Bj-wkqEBAjy2SuG7bEDyLpP95jUVQqyiiOJ3_qPb1FdWgtCTlHMg2LG-9JA0Ai0UmQoR1XDPzY3JY--wj3fixtyWgr5Jt6NOafnfKKU5LDtSZtCfGhe5CalfPGD-QL5U8xGOWHAbxxwbIVmGgEbgdxXaeoSZtjCQ-WLOGEL_BtDt9btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایندیپندنت: ترامپ نمی‌تواند در جنگ با ایران پیروز شود
🔹
یک رسانه انگلیسی در گزارشی با اشاره به اینکه دونالد ترامپ در تله خودساخته جنگ با ایران گرفتار شده، نوشت که رئیس‌جمهور آمریکا تاکنون ۳۲ بار اعلام پیروزی کرده، اما نمی‌تواند در این جنگ پیروز شود.
🔹
روزنامه ایندیپندنت نوشت، هر بار که ترامپ اعلام می‌کند جنگ «پیروز شده»، ایرانی‌ها از اهرم‌های خود برای گرفتن امتیازات بیشتر استفاده می‌کنند. هر بار که او با آغاز حملات تازه واکنش نشان می‌دهد، بازارها سقوط می‌کنند و قیمت هر بشکه نفت و تورم جهانی را بالاتر می‌برد و در این میان، آمریکا نیز آسیب می‌بیند. او نمی‌تواند پیروز شود. به تعبیری که دولت ترامپ بسیار دوست دارد، «او برگ‌های برنده را در دست ندارد».
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/450085" target="_blank">📅 08:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGLucLCoNNoR_XefNlSOxGmDCXfigXExTQgOm6PwH6D0VpI9-7Gu-oiaMWnzdgjoyOE9HcWieH1g8BN9l1O66uA2qnTX91lvS2syL_zkD_cEqfb-pD3iReHIgdNfCOYa6V2CgAafeIdTXC2ojBvZbBWxW1OTysf0nbW_M9XhWxuP0LYaM_UP51HaSp5Rjbbck2vLMPUM6X7SYgCUvQhIJGUSo0mV-1iywXgQoxcd818d2fjK1ebTWJoZDXQGzMaDdi2AHakOWYM0VZ0fF57h3dwJizWIUYlImswyGETVUJjm5r9t593BA2sycdj6_nHuRxsOpyTcbIqNC8GNGaVy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس کاردار ایران را احضار کرد
🔹
وزارت خارجۀ انگلیس با تکرار اتهامات واهی دربارۀ نقش نیروی قدس در هدایت گروه‌های مقاومت منطقه برای انجام حملات در اروپا، کاردار سفارت ایران در لندن را احضار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/450083" target="_blank">📅 07:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حوزه‌های امتحانی نزدیک مراکز نظامی جابه‌جا شدند
🔹
آموزش‌وپرورش: تمام حوزه‌هایی که در مجاورت مراکز حساس یا نظامی قرار داشتند، شناسایی و به مکان‌های امن‌تر همچون حسینیه‌ها و مراکز عمومی منتقل شدند تا محیطی کاملاً ایمن فراهم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/450082" target="_blank">📅 07:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
صدای دوبارۀ انفجار در کویت و اردن
🔹
منابع عربی از شنیده شدن مجدد صدای انفجار در کویت و اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/450081" target="_blank">📅 06:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
یک سیلوی ذخیرۀ گندم در شهرستان هویزه هدف قرار گرفت
🔹
معاون استانداری خوزستان: شب گذشته یک سیلوی ذخیره گندم در شهرستان هویزه و یک نقطه در شهرستان دشت آزادگان مورد تهاجم و اصابت پرتابۀ دشمن آمریکایی قرار گرفت‌
🔹
این حملات تاکنون هیچ‌گونه آسیب جانی در پی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/450080" target="_blank">📅 06:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
آشیانۀ جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
مردم شریف اردن، سحرگاه امروز که شرارت های ارتش کودک‌کش آمریکا علیه ملت ما مجددا از سر گرفته شد، در پاسخ به جنایت های شیطان بزرگ که بخش عمده…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/450079" target="_blank">📅 06:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
سپاه: صادرات نفت و گاز منطقه یا برای همه یا برای هیچکس
🔹
دشمن بداند حال که راهزنان او مسیر صادرات نفت و گاز به دنیا از اقیانوس هند را که منافع رقبای اقتصادی آمریکا را به مخاطره می‌اندازد بسته اند، باید منتظر بسته‌شدن سایر مسیرهای صادراتی نفت و گاز که منافع…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/450077" target="_blank">📅 06:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
سپاه: مرکز مدیریت ان‌اس‌آی، مرکز کنترل فرماندهی، انبارهای بزرگ قطعات و تجهیزات نظامی و مخازن سوخت ناوگان پنجم دریایی آمریکا در بحرین درهم کوبیده شد
🔹
اطلاعیۀ شمارۀ ۱۲ سپاه: ارتش کودک‌کش و رژیم عهدشکن آمریکا که شب گذشته با انتشار راهزنان دریایی خود در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450076" target="_blank">📅 05:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
سپاه: KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در میناعبدالله کویت به آتش کشیده شد
🔹
اطلاعیۀ شمارۀ ۱۱ سپاه: دشمن آمریکایی که شب‌های گذشته به بهانۀ اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می کرد، دیشب هم که هیچ کشتی جرأت تخلف و همراهی با…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450075" target="_blank">📅 05:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: تا زمانی که شرارت های آمریکا در منطقه وجود دارد یک قطره نفت و گاز از منطقه صادر نخواهد شد
🔹
این تجاوزها جز تأخیر در بازگشایی تنگه هرمز نتیجه‌ای نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/450074" target="_blank">📅 05:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452813fbb6.mp4?token=h0lRWtI91CWAd3YQ2FCi-rOz0js0XDygfYeasnSIhH_Uc5AH7KfLqw4G_6PYilIC7rbSmeuTBZmsytmLTeFpzM7FtHHA3VKrd6TRIkGe16H6g_TXDB2gWzsRVknpbj5pN4hukhaDUPtKgKQDDGZ-6vZTsIOZ-0yasUM9wGAkHbyeO2HpISLAMDgP5EbRcS97pKgp8nj0z1RX7_ab_zRHkRMR5KeILoqNKVNMw8l_U_LwDtzpqXdku8q5iQNJ3jdku7tTwLowXdnzIQmSSEsxk7XaHibOhBqoLfvDKzooBQ6cyoDN8tRvupmpkrD0JuQyovHVyv4ScZESS4UDGLxnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452813fbb6.mp4?token=h0lRWtI91CWAd3YQ2FCi-rOz0js0XDygfYeasnSIhH_Uc5AH7KfLqw4G_6PYilIC7rbSmeuTBZmsytmLTeFpzM7FtHHA3VKrd6TRIkGe16H6g_TXDB2gWzsRVknpbj5pN4hukhaDUPtKgKQDDGZ-6vZTsIOZ-0yasUM9wGAkHbyeO2HpISLAMDgP5EbRcS97pKgp8nj0z1RX7_ab_zRHkRMR5KeILoqNKVNMw8l_U_LwDtzpqXdku8q5iQNJ3jdku7tTwLowXdnzIQmSSEsxk7XaHibOhBqoLfvDKzooBQ6cyoDN8tRvupmpkrD0JuQyovHVyv4ScZESS4UDGLxnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل استقرار جنگنده‌های اف۱۸ در پایگاه الازرق اردن هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در مرحلۀ هفتم عملیات صاعقه و در ادامۀ حملات کوبندۀ پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده‌های اف ۱۸، ساختمان…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450073" target="_blank">📅 05:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هشدار حزب‌الله عراق دربارۀ جنگ‌افروزی علیه ایران
🔹
مسئول امنیتی «کتائب حزب‌الله» به آمریکا و رژیم صهیونیستی هشدار داد که آغاز جنگ جدید علیه جمهوری اسلامی ایران، واکنش فوری مقاومت عراق را همراه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450072" target="_blank">📅 04:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=ANL0XuwN8nKXXGr22T4pu6ngGdWFZYvvT8-YJwG0p06FGAe2bT9YK2OWq-cRwgaiJcTMoyg4z0G88vG79lmSaY3saP5FDWe-bCfpqHqoutb3MPojTx9AGGLws9MeWcAEp_DepDZH-8pAlqZw8g4wWvqLRWfbQ3sTwOxKhuWryWocj5DTnUYd8EAcwF9UR36OXnlXsCifrgnUR8yqJQlLCKfWiINQH-tYYzbhEnSTmyay8pDYqHm8xqep2DPog49fueTzscLvbZq0NEIX44sqep1tpiJdxGzE0eSslvjMnwr72Zf_APZuh_tTKGC3rie41e-ZeVzjs-lLkAITWLBEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=ANL0XuwN8nKXXGr22T4pu6ngGdWFZYvvT8-YJwG0p06FGAe2bT9YK2OWq-cRwgaiJcTMoyg4z0G88vG79lmSaY3saP5FDWe-bCfpqHqoutb3MPojTx9AGGLws9MeWcAEp_DepDZH-8pAlqZw8g4wWvqLRWfbQ3sTwOxKhuWryWocj5DTnUYd8EAcwF9UR36OXnlXsCifrgnUR8yqJQlLCKfWiINQH-tYYzbhEnSTmyay8pDYqHm8xqep2DPog49fueTzscLvbZq0NEIX44sqep1tpiJdxGzE0eSslvjMnwr72Zf_APZuh_tTKGC3rie41e-ZeVzjs-lLkAITWLBEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت موشک‌های ایرانی به اهداف آمریکایی در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450071" target="_blank">📅 03:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb04d40e12.mp4?token=DkxXzl4phPkCRN-khw62EtEt1JtSUmrf0dfoW_g58II_kCy1U0nCC101SkQA31KTob2gyjbk_inOr4Z9uJ5M_DiW4NK4FlDNkgHqX22PdJ31E4NxFgsv3YdP794l2TBY2U-fc9W3D_pvzlWjxhNhx-ELJvAEdsgqRBQnHBzStSKnbsVqQb5afs7vYMsXInmqzkxNgbzyOBnNY0CxSkQgyXHpBTU5uQHe61GctNvABZryu_31PyC_ZwWJEaAECitcePmh4lMkIbS-ITZDzL0fUG-1cmTxqL-5bN9p_dbNpnIxShQrNW2zHzCxqihWskEzk-Iyd_xPINdz5zd6HxXlLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb04d40e12.mp4?token=DkxXzl4phPkCRN-khw62EtEt1JtSUmrf0dfoW_g58II_kCy1U0nCC101SkQA31KTob2gyjbk_inOr4Z9uJ5M_DiW4NK4FlDNkgHqX22PdJ31E4NxFgsv3YdP794l2TBY2U-fc9W3D_pvzlWjxhNhx-ELJvAEdsgqRBQnHBzStSKnbsVqQb5afs7vYMsXInmqzkxNgbzyOBnNY0CxSkQgyXHpBTU5uQHe61GctNvABZryu_31PyC_ZwWJEaAECitcePmh4lMkIbS-ITZDzL0fUG-1cmTxqL-5bN9p_dbNpnIxShQrNW2zHzCxqihWskEzk-Iyd_xPINdz5zd6HxXlLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهادت اعضای خانوادهٔ یک محیط‌بان هرمزگان در حملهٔ کور آمریکا
🔹
در جریان حملهٔ بامداد امروز ارتش تروریستی آمریکا به هرمزگان، یک پست محیط‌زیست و انبار علوفه هدف قرار گرفته شد که درپی آن خانوادهٔ یک محیط‌بان شامل ۲ پسر و عروس او به‌شهادت رسیدند؛ این محیط‌بان…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/450070" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
🔹
گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/450069" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16d5ca6b3.mp4?token=ctN6kYOe3Gt9M6b4RZdpFHBTYdtM_tHYKhDhsmutS2T31d8qQvKG0ofqusJOUlaLwgKVRYBJP5gN4uIYPb_-bCcgaarSnli_DgT5gTMJgUwvP8wkI1uqhc7JLnzuKk_6kBgvtvnZNC2-CHbJMwulaEKXd9uBOEsmAt3IbXhhAvLJJw-AkHcyWtvIugKCMHI4xJYedgZ-Zp3bdJfShl1lrNr6p0aWRY0zlhSlPHhqZ9tIu1Rdpiu_iDaGYXSww6A4AlX4WFKlnoeEF6QeH-yM--eCnlWqKhDy4m3elmjA2iEQeHVGJDiBl88dnIZv5SZBh4E7gsEGodGdIwX-QIi6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16d5ca6b3.mp4?token=ctN6kYOe3Gt9M6b4RZdpFHBTYdtM_tHYKhDhsmutS2T31d8qQvKG0ofqusJOUlaLwgKVRYBJP5gN4uIYPb_-bCcgaarSnli_DgT5gTMJgUwvP8wkI1uqhc7JLnzuKk_6kBgvtvnZNC2-CHbJMwulaEKXd9uBOEsmAt3IbXhhAvLJJw-AkHcyWtvIugKCMHI4xJYedgZ-Zp3bdJfShl1lrNr6p0aWRY0zlhSlPHhqZ9tIu1Rdpiu_iDaGYXSww6A4AlX4WFKlnoeEF6QeH-yM--eCnlWqKhDy4m3elmjA2iEQeHVGJDiBl88dnIZv5SZBh4E7gsEGodGdIwX-QIi6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کویت
🔹
رسانه‌های عربی از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450068" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت.
🔹
هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست.
📝
اطلاعات تکمیلی منتشر می شود.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450067" target="_blank">📅 03:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2J_rUv3wcvUyfA_8PafnbuhyNjMfObOilMWyphsrWhRkNRQkc7sdqXAHEv0fDBT5ItLipi964Tfjd8oqG087bdeCjSwxfRWZkcg3quiEZCowgPVPYLFUHmKZkgUd4XsAwZzrXRu9mI-KYcPOz8IOUIFveg-WSgfGbTYPn0e-JYGeRo43cs4b18aiVfHnUja3m1kwTrhSIr6RX5jMAlc40AJuus_cgfrM7gI4Ge2INS6PtnDCGH-i_xpcRtQupXswOxkk7GeZLCnRFn5i2z1oUl7YybWZwI1G601yj9ouKeaIz0x2U0WSHnPbj-JUi5t8WQXrR1Lp_TqbcKPLSvQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450066" target="_blank">📅 02:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت.
🔹
هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست.
📝
اطلاعات تکمیلی منتشر می شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450065" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/450064" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa94abe270.mp4?token=KDBNcK2C_En2u4K2bG7AzPgkiVjWp1utklmSx7FB1VUPvEw0iYTr541rYbLZCCFu5YUVw2ZvhHUnUxcMSKPoEa7ZwFM9uN9yyfpzo85hOAfplfG8SvcCO6A_nlD9WUgAIO_5aeMlgig42zFrQbXLeM3D2UbFg1Pmetj2sCLuz3M0NvXTDaqfP7W3jjyycOmxxgsoSRz6HiHqDTmXMsFM5ozAlQQ0pp8VPGBvs8t3jQVRNAyintyrSJ5QJ1ZX5w_xfKE_LmwjRrzENOcYrhOIoUZm5U-mCJJIeRa9aa_qe8uls2BUOUcJjzZ2999TVrNU-xW8L0zFsmoYwQa6B8cZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa94abe270.mp4?token=KDBNcK2C_En2u4K2bG7AzPgkiVjWp1utklmSx7FB1VUPvEw0iYTr541rYbLZCCFu5YUVw2ZvhHUnUxcMSKPoEa7ZwFM9uN9yyfpzo85hOAfplfG8SvcCO6A_nlD9WUgAIO_5aeMlgig42zFrQbXLeM3D2UbFg1Pmetj2sCLuz3M0NvXTDaqfP7W3jjyycOmxxgsoSRz6HiHqDTmXMsFM5ozAlQQ0pp8VPGBvs8t3jQVRNAyintyrSJ5QJ1ZX5w_xfKE_LmwjRrzENOcYrhOIoUZm5U-mCJJIeRa9aa_qe8uls2BUOUcJjzZ2999TVrNU-xW8L0zFsmoYwQa6B8cZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیلی/
ترامپ: کوه کلنگ را زیر نظر داریم
🔹
رئیس جمهور آمریکا به شبکه «فاکس نیوز» گفت: «ما پس از دریافت اطلاعات مربوط به فعالیت در کوه کلنگ، آن را زیر نظر داریم. اگر ایران اقدامی انجام دهد، فوراً پاسخ خواهیم داد. ما سلاح‌هایی داریم که می‌توانند به اعماق زیاد برسند».
🔹
ترامپ در پاسخ به این سوال که «آیا احتمال عملیات زمینی محدود را رد می‌کند؟»، مدعی شد:‌ «نه. بعضی وقت‌ها به یک عملیات زمینی نیاز هست».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450063" target="_blank">📅 02:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در کویت
🔹
رسانه‌های عربی از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450062" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای ترامپ: ایران باید توافق را بپذیرد
🔹
رئیس جمهور تروریست آمریکا بامداد چهارشنبه بار دیگر تهدیدها دربارۀ حمله به زیرساخت‌ها و تأسیسات غیرنظامی در ایران را تکرار کرد.
🔹
ترامپ ادعا کرد: ما به‌شدت به ایران ضربه می‌زنیم. حملات به ایران تا زمانی که من بگویم دیگر بس است، ادامه خواهد داشت‌.
🔹
ما امشب، فردا و پس‌فردا به‌شدت به ایران حمله خواهیم کرد. در مرحلۀ آخر، نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد.
🔹
ما تمام پل‌های آنها را هدف قرار خواهیم داد، مگر اینکه آنها موافقت کنند به میز مذاکره برگردند.
🔹
ترامپ با ادعای اینکه آمریکا روز سه‌شنبه با ایران مذاکره کرد، اظهار داشت:‌ ما به ایرانی‌ها گفتیم که باید به توافق برسند، در غیر این صورت چیزی برایشان باقی نخواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450061" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
استانداری هرمزگان: اصابتی در بندرعباس، سیریک و جاسک در دقایق اخیر صورت نگرفته و صداهایی که گاهی شنیده می‌شود، از سمت دریاست.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450060" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010cb43dec.mp4?token=iPuWhxU3TGLn4uY_kABYjzCH9KiKwLjPY0SfgJf9aeUJyOpP9fRdPeq5TG-w0uABDN6gYAGi1LU1_Ee_CLvbcbxva2JC_5kzAOvnyC4YQgbFzqBmpr78lAMbcPTtR6ONoJPP-GFfIDTz4qUanxeBJ9eTthfr9990WSgmWXT5C0Me3I8KvtfT_Sfwb1cyBO29IwQTEO4VtrC3QEVy_jRZUKoQfEdpG1yUG5QZTzBg8vEeb19EJYzNvCH742Kxd5Fuq45bXmQDrEnGYH4qKbl38SfVxXGuT_6P3npDb-rX2TaLnHkHZi2Z7tXGZWSOWZifSk0egyGFIqnBgonjKwxqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010cb43dec.mp4?token=iPuWhxU3TGLn4uY_kABYjzCH9KiKwLjPY0SfgJf9aeUJyOpP9fRdPeq5TG-w0uABDN6gYAGi1LU1_Ee_CLvbcbxva2JC_5kzAOvnyC4YQgbFzqBmpr78lAMbcPTtR6ONoJPP-GFfIDTz4qUanxeBJ9eTthfr9990WSgmWXT5C0Me3I8KvtfT_Sfwb1cyBO29IwQTEO4VtrC3QEVy_jRZUKoQfEdpG1yUG5QZTzBg8vEeb19EJYzNvCH742Kxd5Fuq45bXmQDrEnGYH4qKbl38SfVxXGuT_6P3npDb-rX2TaLnHkHZi2Z7tXGZWSOWZifSk0egyGFIqnBgonjKwxqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل استقرار جنگنده‌های اف۱۸ در پایگاه الازرق اردن هدف حملات پهپادی ارتش قرار گرفت
🔹
ارتش: در مرحلۀ هفتم عملیات صاعقه و در ادامۀ حملات کوبندۀ پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده‌های اف ۱۸، ساختمان اسکان و سولۀ بزرگ تجهیزات ارتش تروریستی آمریکا در پایگاه الازرق اردن،  هدف حملات پهپادهای انهدامی قرار گرفت.
🔹
سربازان ملت در ارتش جمهوری اسلامی ایران قطعا درس بزرگ و پیام راهبردی رهبر شهید انقلاب برای دشمن را تثبیت خواهند کرد که «دوران بزن در رو» تمام شده و هر اقدامی علیه خاک و آب و آسمان این کشور تاریخی، بدون پاسخ و هزینه متناسب نخواهد ماند.
🔹
ارتش جمهوری اسلامی ایران، از آغاز  نقض‌عهد و آتش‌بس توسط آمریکا و حملات وحشیانه علیه مناطقی از کشورمان، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه ها و مراکز ارتش تروریستی آمریکا در منطقه انجام داده و این عملیات تا رسیدن به پیروزی نهایی استمرار خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/450059" target="_blank">📅 01:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=BzmhLQlbzYwf_E9iOS4de4GBn5kQBOPDsJ5N-UxM2o8UeJDsKkzHc3YbTgzaFCbdWj2elNANrcdX87_GoVDPlf0rHmZgNqCuQXPSZD5VL4SOQGCTInY5C1p6UQbmgJOS5Kc-GOp2-dWoXwZBYxt2ajnh-AagYrvoPNtInpphGNwPh8DgH_zqOwUtsQP9sKG4tMcg6NnOH8GAlFMO3TkmEr_o62OhX5RhmkxKzgtHe3XXQW02u04-V1QNbY-0urul7bHhZILZm5Bhu1x-zRuO4SizrAn_iv0JNyLnHzQVQeMu1PqxopX2Lnc-hcF-E_4PKGxpapPWEXF7ZieCCLqdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=BzmhLQlbzYwf_E9iOS4de4GBn5kQBOPDsJ5N-UxM2o8UeJDsKkzHc3YbTgzaFCbdWj2elNANrcdX87_GoVDPlf0rHmZgNqCuQXPSZD5VL4SOQGCTInY5C1p6UQbmgJOS5Kc-GOp2-dWoXwZBYxt2ajnh-AagYrvoPNtInpphGNwPh8DgH_zqOwUtsQP9sKG4tMcg6NnOH8GAlFMO3TkmEr_o62OhX5RhmkxKzgtHe3XXQW02u04-V1QNbY-0urul7bHhZILZm5Bhu1x-zRuO4SizrAn_iv0JNyLnHzQVQeMu1PqxopX2Lnc-hcF-E_4PKGxpapPWEXF7ZieCCLqdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناوبان جانباز کنارک: موشک دشمن را دیدیم اما لحظه‌ای عقب نرفتیم
🔹
ناوبان جانباز تهاجم آمریکا به کنارک، در روایت خود از دقایق پیش از اصابت موشک تا آخرین لحظه مأموریت می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/450058" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOu4UrEyY9bvigNrW3yiZSpW871EEI5Z33tRUOHERXevAEDCPz0LMgEbtBF7FPmZY-Wj_GffE-vet4p3GkGmBzS6LIPwSi5CaQxmEwkU9T41CQkPTUp-yKUYRHGu5xZW2qoa0DCRU_lpyW3FMT5Dg5ZV3yCeSGUXOFAjhH2895IDsQnH36_dFVCdTti_1OPS5ALVmfVDWOAjMuVwxlE4Y_pq0KKsrUWoU7TTHd7PCPlJBXKOxskXABKxsxIOTb6XT8ZMMZV2KhtsdWkQ3tcJpz8uSdmf9dEpqXNqf3cpcJIVaqGiirVV4XzANpSkroptOFG3RFPoSN3C_QBMfTBlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNsJT0JWdlOtV4Q6Zam9cupkTw5uWJ3uWrH-x_YUO2DOeR2gHww0DRrTRw1mY5sj_w5kdWYLV8gO5P4UYliJdSukWiO1pVjW82LLi7exAk3MSa8FktBjVDebjxOi-odvCGIMSAf5HNo5cVZNyc6LR87YAsNv7d1dThcMSbsonr3E4W7rCeBdfhEzJZbBqnNXmF8AYRispBmjZbtgrDRSlzcQxZgJ-IzKRl5HDL0r2t3jnXfJmQPTCUIrkUEa0ivjruceR4VOFtPuQy6He7xKY5ElP0i_3zaUOOYSeRmDfcZRnprEkAjdN43DR21oQGwOxQe1rinJxd9uzYIpVgkxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGg3M27je3jyyQRj2kMcbFFD3Rey7NhZxuVhRw1qpthLXLVLW2fSU3yfAaDgscd7l2YEkh_wE0pUT6G3PgVM2dkMyZ41dccMwab1NV-HUzkFebnHHRj6ZFaKTso9s9NE-KRdv_knvazWBF666CzDIraQ3wur6u3Q-PcNV9sngBJnQzbKUdF4bVt-1yy8RsHDrWWd0e0vshEZ7RyPPNo1oEtyYq6U2tYZlGtFu23nhSDcYrvpnbytpxgLUFcV0BCRpfPLbbllaQY-Azw6UIfLfWnhMMPnoKRDcuHYykjRcN7p_OUxzUfe_5CW1zV8JSE1MvwdmOc54CLIUeDpF7_EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpY5ZfUHZVwOvrRjF79mOR-BCUt65NLTyTmC_igX_i8Wy2PJcV07SodU4tG7WM6sShmW_bc9i1XSKonm5I47pMoat_44SjbYiz9lav6lGAWXY0ji9taw4nnPm4P7OeApT__n5tIDTVcNeBDOKmzOrSnjpimn4uI2hrAsaGa58wVijYGVhT-1X3bXAxfNrPr_KYttC39nUcSBey41YGMVL2M4uqalFQmcqYNSNcVse1icJodW10iN-HsBRvBYYEUmnandwmnxzyza7HleOQi-Bupvvi1b3EuebXkuSIz7pQ3P635RGBbifvSLsVhu8cMHJc1r2GUrH9aVLgERQtNJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۴ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450054" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez12576lrcAnXJ5uw8pTe035LGbLOhDmW9FAwAs6ezwowCknK4Pi3VhZSKIZGyYfK7_SEMmt32exq7cn_dIFa83lycNqDDwA-vmZjlvmGaN8vbw_oDNZmloCsG6XFvtpkafyYXsS4x_L9wPiBj-UtHjGrG03eqT1fMNLZi_Ug--ovmVtr9c8gheSGoCKwuVSelbATm1hdUf6YVe19w_kIx5sVyGfkXWV-xda_d6YhPQpzqeUR3z8Wf2bPSyXw5yDTrWfyjCuEjouzUJd_trwaMTi6WxPfVfglX_8E6MA9tpjwCO9kY_vaHpNY94now4xilP93xOX_WuL3dQF-7H3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDj7L50z93qR_u3TvBNkynh6wu-vnKNUXabuQQzBXtM11cTAjnHJpQQxWLXpBzVraWmY6MF0Y1A_Vb4MvAS7UXEX2YtJ_i-k6Dgofq-At46c2bCZ2Kvx2yt9qatr2Zhbnsc2CsA_kuKYVzxS9I5lnYzygVl4TBulO9E2oXsgmM-VJ46Cl6hdBvXTxyZVCAaqBB-E9tqotA5F3OqjrCCEBgsYRdkvkNTwHd5injY7LY4afH_gZ7y4DleW6UZFnsZ4w3Zgyy3RCMph5UvSN3dWFeiW_q1xWg6DpCTHrFsVeWGt9BnU1e18S1QQxdmfgDo3F1dyTJBFOTa4urfdLDnlfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipnKODn1QbGNzJhEdyQMNgVJLyfrJQ2pkhKqZ1IuSSuSsnFCLeyFK9nKrFoMRZu0y_CBJurl_g31VyaojahnZPnCndv0VrQuw9TEPfwtqVk-AOyKdAOPXqbS5W_zZxOiTsXT0kxkpyRj9EgraZcg6y4jQdjJEb7v7cepnMCu1NJnvvEkVMsYEmpiRrtjs4o2OpwKQQyvsPuCx-zmnm38Vj3DZJB-HKeUDtDXoN6wgKWAvEgiaMFqJiH5ctOX8OO4IA8WghqVazJn96wuzbuWM79jSQqQivetJsayv8DMMg9Ca107K2TfkjwtgzyazuiHmJD42b3j5Fb75t0U34tdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su-W6xUc-1_OuTeBbuuCirSmNsNoSoniNzr2FW-vlGUQDS8zPKvzntb5jjTBkjt0tFINXej5QNE5_uzydfr08A8RozLGh6dcjESCsma5U_cUk0bWVEh1lSGaJPBOTgAv2-QVP6VodOpsaNbCMHmslWhn8Doccq3y0E5TQQ4OupJKr27vMm8p9_1vk-EYnZZef2YNsPrdQkBdnRp5XU8-Ju-lszqOedWu5iD9S0KpL4EFsc8JzwCUo3odHslLsU8uKVcH36iW7_BfqcdtOUUyEOCkLJSSh2P1fh9GzC39daFGf6zbAkVdlH42aguuRQae8POT1DYfVdqxFTG1nObWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMPR1MC-xxAZ8KQMZrvpEu5j5fp8RBk9mE4yL2WtW8kcayc0ziZF3QnOOhSooQgZrXmuGi4P1ZH3WB8k4LM7MXAslmXIaALcQu1a-kiM_KnP-RNZRX6QPFPNvLTIfGR2X2tgBYgMbJxySlgJ8DJaURS6NjI2_gb1zej7-3ZJBtGuHtWaIfYq8BWBojdET1rQWS009JUaHcpS_pAhWQwZ9R20LosCh59_lnzjyEAkqozigITKKeBAEH8Bp7s_zxYAN1itORFLji37KMdEZLZz0-aABZZgXGClmU1ggW5ah2bOgrS2WZbOlBDpHy6kAJBN6I8gKp2hf6smvc0PnrtB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AI9zKWNS77jc3dVp0aVoEwmqaB7sL7lb26wt5Nf-uSm7VZHbbJpT5nROjl_TbucSkD2MBrLfTQ5l7kTW6dJzLlL7nQFFKmWgT0UBs3qiN6ThOQKWf83fDT7HSnYD_G1Nr56pFemd9ClTEmzUR1K6iHf6g40Wc2tov23zuAI9-koMrWiW12npJ_Xg6LxpOKhg9TBQ_pCaPX4YJbrCEvTmEuaF3XPE72ODQR80X0YLp9fPRD4Ud05m0LiLq5TMrN73SXIukzt3xZIByISlNVZgrKgEzidTm1CtuQQlWfpkIfO0IjNcHh3y7RWfwMjqdCqD6Fn4SorLTlGKd8NdEKdH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5qF3fY2YiroVPPqjDGge8YqIGFQoYV72SPtWdqUV2R-XBZxIZund3XA8G7SIVnhi3KOzYtk2LE2GDKDolmPxZSM7_p99rGF6a_-VCEogsWi2zE3otctP0g82GG55jWK-vOj26r65M-TbJ3kvr2PQk576l1DhM8YMiiMsdt7cV6YpRlYiOxXY4Scrk7KDbQOf-vDWoBKEyeHcswGHBreAEInjP-54hiUI5BPrqe4mCAp9dokX9J2gFD-PKKeensml8aSqSyLTy7eCuxQyM41eEAF5NhUFjc3DKFThqtDYUE5oy4778ZOgzmX43LutEiclxdCLRZ1Q7EqHZuBHKyMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWpNp2kFCon30TBwDXFji8fzsRHC3St1xgrEFDzzYnSTS02u_SgqVCVpGPow_XKCKZ7M6x4xJa4z67JLIP_fooQQhxqzgcVsPWMOSY2uBFRY_lY9ICKbw4It078UqjFFw0sYuoIbxiYnpkIuZTIDs_3YaoUTBqrJ5yml58dEzhlfA0Fq9hthLjuphk32c4nn6MAx6BHvrXC2h3qQm33p9HxIlaBtlAJsWq-2uHiwcejs5zYWFj09nbD_HkjfiDd8mjNhTuPoMB78ZzwUGXIbrC1C_acfOpBIf5WYJxryZfP5FGjlVSRAAM8_q6suNid-uDeIC9FUt8LIvdMQ3sPgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPXYAQ11ZSxKtN0ATxJ9zc-uRzsu1T6ThD202q532unWN_lIB9qjZ2cpqQPxesipRCRG-jHF14bowov2lN01ZiplBHyGm3xHPUAYLt_OPUj2p-G1qYDxyc8BZ5U83cjn7pIB4brUxmn69pijz9BFt81G0WJfiBrtPXq_YggqIINhEy63El0mhxJnHdZ_72yjFcjD1ANyDdL0LlW0TwsIEY_IJUlEGnfsqd1SsF02ONJ0Tw_s8rGJ03X5XkSi3k2Kbu8PIJ8aGz8grfXRsHa16U_fulhYPMkm9f7UK4Ct1nz5EW0MzuAoDXKcQkuXWYyinzwNbfFeMyrSQCH7EQVO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqMuSOlIB56v7Ym0Ludic2ufpApvn4vLGMNUNg2Fx5mO2LtkrBUOwiaix3O76JdMz7yEsPKuxVwQ0AVztwQ14QE4UHnMgJY_jyNw0NhxYVttdrpfVU9fti_bEJz5lyb_opagMnKeSJf5NfdGWOM1Y30h5-KF8thrXVcfRZ4A9VR6Yv_VnC7_GO_e7Z1NMQFvVlO4RVkQtXKfb8IjOw8jVpjf-rOnDJCUZ533NBQaveF100jKaeHK1y28MNZC1ex2ecDLmTNCs7t1eOhHg3AFO0Sjx2uQrA5r839vennqO-e8hPKBtjKpm34tr_mKFj73TMjRaY4ox0QiFOaZyfk2Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/450044" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT13v3W_ALlnq2CTF2pks7iVn5K9HvN4fifw2zuzla8GF6s4D0oJUbNcy_x5bOc7rWK4_QE2szFzQyfLk4_yHRcX2TDsnoelWLl50yi9mF83vIw4ojM4BExDjXgkJQgBiL1Sbk38yjMP5-pdX5DO6AKwlos3adMntzd9Zu64s-mMRoPuIZekP0utSD2shwPRMS5qJ7ExyToa0Xha-wYRWjqK_WFRR2qsWCZ3qXh1pJ310Ie8m30WY6b8M_Y6N1X4sWVb0DjhTfr_YLKHwekU9IuxX1ybn8G1c4k-E1W8mIALEb41QnP95tqyh4vN2n8sul8IN-Zxe0dmSY1gyMBApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج نظامیان آمریکایی از عراق تا پایان ماه سپتامبر
🔹
وزیر جنگ آمریکا در دیدار با نخست‌وزیر عراق که به واشنگتن سفر کرده، گفت که نظامیان آمریکایی تا پایان ماه سپتامبر از این کشور خارج خواهند شد.
🔹
پیش از این نیز الزیدی، نخست‌وزیر عراق طی نشست خبری بعد از دیدار با رئیس جمهور آمریکا گفته بود که از تاریخ ۳۰ سپتامبر، هیچ نظامی این کشور در عراق نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450043" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=vfWgyJogCNfEBdVY0l8FFvPZSkJk0lu--3n7bC9bsmvHss-abwz7YFLKDyr_fisDJ43tszap2t0iigTNHEMev8OBIAMy3PuAc-SVUwicm-ad8w-4h_FgcV-Bo7i_E3L8eTg2dYSk6uu-rdwWPeKhrc9-ZtYQCIyLnAooZ11GFHu4gexop3SMuWU-eWwFDKs6jIstEKRjSzKS-JKv9fJ9jObYNZvYMAE4GZesAULBvPljlOI8d55630cF_RxoINpnX3RwdWZ8MqlYz17KqKpdfYvWgkegUUthuToZNLsoxDAAkH2q_Mhbz2KJoa-5JFCRi-257_IoayEs3I3YWdtwPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=vfWgyJogCNfEBdVY0l8FFvPZSkJk0lu--3n7bC9bsmvHss-abwz7YFLKDyr_fisDJ43tszap2t0iigTNHEMev8OBIAMy3PuAc-SVUwicm-ad8w-4h_FgcV-Bo7i_E3L8eTg2dYSk6uu-rdwWPeKhrc9-ZtYQCIyLnAooZ11GFHu4gexop3SMuWU-eWwFDKs6jIstEKRjSzKS-JKv9fJ9jObYNZvYMAE4GZesAULBvPljlOI8d55630cF_RxoINpnX3RwdWZ8MqlYz17KqKpdfYvWgkegUUthuToZNLsoxDAAkH2q_Mhbz2KJoa-5JFCRi-257_IoayEs3I3YWdtwPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: خون‌خواهی رهبر شهید به فراموشی سپرده نخواهد شد
🔹
انتقام از قاتلان و آمران تروریست امام خامنه‌ای شهید، در سطح ایران و جهان فراموش نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450042" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ستاد استهلال دفتر رهبر انقلاب: چهارشنبه آخرین روز محرم است و پنجشنبه اولین روز ماه صفر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450041" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450040">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450040" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e320839ea.mp4?token=aKRqcAzyL6MXZJcsn3lUBeROvN6MgVI8Rl6m0hrj9ftCdJ-Xg8Vhddn86N2UpEdLBFRULz771Yn27s2SEtDYCLDnfnqtpsRSLUHBwOZhDdE7QQrfMUwp6D8TLTto1EiksWZtKyvL7YJjSZkWdrbZ0yVldVxYg_6lk80pgRxTMevd3a9Km-jTMQPHmGoYzucb3J43HjcvNX1UhJUyq3MO3ItB-g91t8Io67tctP-_own841eVsVemydZ2HfFKMiRxlxKB-80FVKz_20mrU_H3B1yMf8s5mOo1BUcOlc8fiNsWF7yqlLLOhNZ5D6Z3EsQnjfd3AahlI6IRemiwkyZgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e320839ea.mp4?token=aKRqcAzyL6MXZJcsn3lUBeROvN6MgVI8Rl6m0hrj9ftCdJ-Xg8Vhddn86N2UpEdLBFRULz771Yn27s2SEtDYCLDnfnqtpsRSLUHBwOZhDdE7QQrfMUwp6D8TLTto1EiksWZtKyvL7YJjSZkWdrbZ0yVldVxYg_6lk80pgRxTMevd3a9Km-jTMQPHmGoYzucb3J43HjcvNX1UhJUyq3MO3ItB-g91t8Io67tctP-_own841eVsVemydZ2HfFKMiRxlxKB-80FVKz_20mrU_H3B1yMf8s5mOo1BUcOlc8fiNsWF7yqlLLOhNZ5D6Z3EsQnjfd3AahlI6IRemiwkyZgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان اسپانیا، فرانسوی‌ها را ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450038" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzqHFwC3eqDKbEIwntDj9vPx-xZMfTcVqbV8rP-xU-7TRmT_dgDyFSlY8NtR5ACqUtxjTuQqje9TbPBNpEmHmx_L9m-QEiTrMmm1jskK0X_2lJ4C8WE8FvTLy217dwq17AYk-YamiKlSo73Ey6EbbK1zUHN4q0jPUfAx7UUHICVB1Omk2cVFWdsQORr0gDSeR-d-oUmgZMr_auYnEMHDX-xFl4FzikuE0_jmux2WVU_k93TfFNHrTwoYiKEJJisBOHyfSyEpyOpzmTH3qEf7G1_LYJ1LZVAT0N1v0bKdsRs0ljq0SQSjY-EXoilddJi_4gyZuUxbvb_XdjRNIgHs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: حمله به پست سرمحیط‌بانی در استان هرمزگان، جدیدترین نمونه از جنایت جنگی آمريکا علیه کیان ایران
🔹
سخنگوی وزارت خارجه: فهرست جنایات آمریکا علیه ایرانیان هر روز طولانی‌تر می‌شود و هر روز که می‌گذرد، آمریکا پردۀ جدیدی از کینه‌توزی خود علیه ایران را نشان می‌دهد.
🔹
بامداد سه‌شنبه، ارتش تروریستی آمریکا به یک پست سرمحیط بانی در روستای سیدجوذر شهرستان حاجی‌آباد در شمال هرمزگان حمله کرد و ۳ عضو خانواده آقای جواد حسن‌زاده، محیط‌بان زحمتکش، را به شهادت رساند.
🔹
این تنها جدیدترین نمونه از جنایات جنگی شنیع آمریکا طی چهار ماه و نیم اخیر است که با ترور رهبران و کودکان و زنان و مردان ایرانی در تهران و میناب و لامرد  و... در ۹ اسفند ۱۴۰۴ شروع شد.
🔹
هر جنایت جدید، عزم ایرانیان را برای پیگیری اجرای عدالت و محاکمه و مجازات عاملان و آمران این جنایات مصمم‌تر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450037" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2edcc47a.mp4?token=QJtEtSiSsu7JqzfyPLNHVYB61vYkou9ClKADFK2h9rV7RS_3NqsRQm3hKtZppz_JUa3p87wTBP8Paz6vyyrJC72XsfSeAoxyKaaBfWUCzOT8ejkm-Qi8zb9Sd0rBaJ0FmCeIqFzZMWh_n6q0eWSkqSrrUwOrUblv8_wFH5hP1d5FowGVpT9KvVHMhXHDD2eF_k4fNXCq4tOZe7trItkbZ1Hf1Q_doiwjMohMucY_i0cO19E8SUTPcxpgQva01ADZeIGtcuPIA7hmGJD7kSH4HT6fnIbojZwLmguWP55_TT5Iro5v6vw4AU8UuUQ1jcVUSlENBbCzzQ1ToVb1FiPKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2edcc47a.mp4?token=QJtEtSiSsu7JqzfyPLNHVYB61vYkou9ClKADFK2h9rV7RS_3NqsRQm3hKtZppz_JUa3p87wTBP8Paz6vyyrJC72XsfSeAoxyKaaBfWUCzOT8ejkm-Qi8zb9Sd0rBaJ0FmCeIqFzZMWh_n6q0eWSkqSrrUwOrUblv8_wFH5hP1d5FowGVpT9KvVHMhXHDD2eF_k4fNXCq4tOZe7trItkbZ1Hf1Q_doiwjMohMucY_i0cO19E8SUTPcxpgQva01ADZeIGtcuPIA7hmGJD7kSH4HT6fnIbojZwLmguWP55_TT5Iro5v6vw4AU8UuUQ1jcVUSlENBbCzzQ1ToVb1FiPKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت امباپه از کنار دروازه اسپانیا بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450036" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da428073cf.mp4?token=QksE3KNb5QO6gPiwhmhPhm_v4oFmeRuEx8uhQfW2Aiv15-aGrfAipE_3XXD2QeiatPiy-J-T8IU1oks16DFII_qo5UgL6fRUhNYDyluZONS38lrdgc9m_BRWYqScUVIYVuduPxVIPB18FZbrwftVrBVseqZ6y3FMxqvIxWJusj2vgMok1kjKzx1DX_6vlliApM0KNeF401Y8i9FCLboJHH7QQ3jF6Z2k18PA5RbcvX4IGJ_Mlu97MbmsN2FPkTMxius8y07sIgeudDI3Ng2l86WxDekGQzpGl9yl2vlvfZ8wyHO8zfz60F8I0GfOCvu8jwdjKUlyoCTb5RgeJIx2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da428073cf.mp4?token=QksE3KNb5QO6gPiwhmhPhm_v4oFmeRuEx8uhQfW2Aiv15-aGrfAipE_3XXD2QeiatPiy-J-T8IU1oks16DFII_qo5UgL6fRUhNYDyluZONS38lrdgc9m_BRWYqScUVIYVuduPxVIPB18FZbrwftVrBVseqZ6y3FMxqvIxWJusj2vgMok1kjKzx1DX_6vlliApM0KNeF401Y8i9FCLboJHH7QQ3jF6Z2k18PA5RbcvX4IGJ_Mlu97MbmsN2FPkTMxius8y07sIgeudDI3Ng2l86WxDekGQzpGl9yl2vlvfZ8wyHO8zfz60F8I0GfOCvu8jwdjKUlyoCTb5RgeJIx2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوسی‌وششمین شب از اجتماعات شبانه در قلعه‌گنج کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450035" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دریای خزر تا جمعه مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌بادهای شدید و مواج شدن دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را تا ظهر جمعه ۲۶ تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450034" target="_blank">📅 00:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de9f1865e.mp4?token=CthWrEyKz0A6yqtt4hjZWWPa5fBmCEYhiHAtK2Ktuisa5qABycR_YZjVQfkJ2qtnLtAQJkb82oftt2aYHMdqA2_C84e6f5WrJjIiMqcSEbg-pfN7LIdPEq8g2c3ic8GAB6XyFwNQf1KX7Ow13scf2sZ1FTk33KB3X1ynVMX1u5PCrwoiXNRc3whZCNuVluhvd-qo_RO6uk-zx5AIQHN0XWDsgw2O5iissrmNhbbEnn3FysxYQ-vgHDFK3DHh1x07MKNL56NTon3QBQCi3bKw_LTTYaEgwV5yJ0MX4bJKWGI7nBbyzNNbqWCRidpsLmBKL_NwEZljZTHaKckR71XrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de9f1865e.mp4?token=CthWrEyKz0A6yqtt4hjZWWPa5fBmCEYhiHAtK2Ktuisa5qABycR_YZjVQfkJ2qtnLtAQJkb82oftt2aYHMdqA2_C84e6f5WrJjIiMqcSEbg-pfN7LIdPEq8g2c3ic8GAB6XyFwNQf1KX7Ow13scf2sZ1FTk33KB3X1ynVMX1u5PCrwoiXNRc3whZCNuVluhvd-qo_RO6uk-zx5AIQHN0XWDsgw2O5iissrmNhbbEnn3FysxYQ-vgHDFK3DHh1x07MKNL56NTon3QBQCi3bKw_LTTYaEgwV5yJ0MX4bJKWGI7nBbyzNNbqWCRidpsLmBKL_NwEZljZTHaKckR71XrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم اسپانیا آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450033" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dce3529d.mp4?token=pUNmnGwU4C8i3dI-kvVJHQs5UbPEuapXeWGawyeTtLzpBOvOeMNAYV-j7KR2C0PxY6Jp-gc3bP6KkCO8G3BYypm4nGXegGEkKu7vI2fhKNDcobeph67nmYWGJM6OTvhc7sM5s5Dn8_mT8h-1m645rq21em7UjldlAzJJUp5eq88mF--wXybYddFeCIiE2kLfSJbIXDm3AJQw9zVDOKPEmd2wnuCJmgdh231kTwr8Xja-qAic79r2dMBp8LgBZJQMuxbHKZnGrLinSuzJwFPfMFvk3I3D89XOJ50CNZficaKkGkQrkgAsQlKrs_mMcwIjI9qD_RLardqn97CfIqA3QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dce3529d.mp4?token=pUNmnGwU4C8i3dI-kvVJHQs5UbPEuapXeWGawyeTtLzpBOvOeMNAYV-j7KR2C0PxY6Jp-gc3bP6KkCO8G3BYypm4nGXegGEkKu7vI2fhKNDcobeph67nmYWGJM6OTvhc7sM5s5Dn8_mT8h-1m645rq21em7UjldlAzJJUp5eq88mF--wXybYddFeCIiE2kLfSJbIXDm3AJQw9zVDOKPEmd2wnuCJmgdh231kTwr8Xja-qAic79r2dMBp8LgBZJQMuxbHKZnGrLinSuzJwFPfMFvk3I3D89XOJ50CNZficaKkGkQrkgAsQlKrs_mMcwIjI9qD_RLardqn97CfIqA3QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا به فرانسه توسط پورو در دقیقه ۵۸
⚽️
اسپانیا ۲ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450031" target="_blank">📅 23:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e50082f6.mp4?token=cPYpV5gPNXeOFL97bGzfqJT_YNwBAorToGljswonBnoZ83ypL_rrkUddD3ZXZW0I50DNEg-wJY6qYxX0mi4FAXaNU5_qurZyuYRryyJlQR-um4Xte-rbEvqPaFGmwSLiuFD28Jl7n_v1X_S4CXSD5jm8j51FMk1_B6gl4xHwu2FTXPMheDH1qPRoFVgXKHEvN9byctAh1MND8Al1Dn83uJf2Ujpoy9W0hnpEEgayvt--pToaKt7zm6Nt_ZZT2_iYPSSrBjTkseJ3el7VM2TZHHTtIGxjbNc0ShMImOm_2LDUxEQJaiImK6tYbNkagst9ai6OHCmM5qdZa5_c4jmN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e50082f6.mp4?token=cPYpV5gPNXeOFL97bGzfqJT_YNwBAorToGljswonBnoZ83ypL_rrkUddD3ZXZW0I50DNEg-wJY6qYxX0mi4FAXaNU5_qurZyuYRryyJlQR-um4Xte-rbEvqPaFGmwSLiuFD28Jl7n_v1X_S4CXSD5jm8j51FMk1_B6gl4xHwu2FTXPMheDH1qPRoFVgXKHEvN9byctAh1MND8Al1Dn83uJf2Ujpoy9W0hnpEEgayvt--pToaKt7zm6Nt_ZZT2_iYPSSrBjTkseJ3el7VM2TZHHTtIGxjbNc0ShMImOm_2LDUxEQJaiImK6tYbNkagst9ai6OHCmM5qdZa5_c4jmN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450030" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450029" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c80bdd581.mp4?token=BSg33H6LhaH4JACDJrwNl1N9nt-IhB837s-0JdiCkBe15mGY0f_HcUFcxWrhMMtaJxJ6aam1KBoRHnEzrwEdDiIRGYE-ZN5Qz2JG7qWguNeoFDJpt5WfncVGq2Pbj6H5ZUp0-LARWU-FED-ksFCXWM5pYeIlGQl9Wzl6oXyNgKYYog_976-95XfYiu-j5u7b5t_vAJzA8GFrl2YF-X3QOoIbl_45qyCvZHqvrLJdg7VVh7ihTXO79GJGglJe9mPoWiSQFAGdS63mWfTyP1TlYT4xgkyNiTot54TEPGfiwZEBqcbQ7HyNLhKpSI8mWGa1ORqpxH9epdsPpqnlBEaV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c80bdd581.mp4?token=BSg33H6LhaH4JACDJrwNl1N9nt-IhB837s-0JdiCkBe15mGY0f_HcUFcxWrhMMtaJxJ6aam1KBoRHnEzrwEdDiIRGYE-ZN5Qz2JG7qWguNeoFDJpt5WfncVGq2Pbj6H5ZUp0-LARWU-FED-ksFCXWM5pYeIlGQl9Wzl6oXyNgKYYog_976-95XfYiu-j5u7b5t_vAJzA8GFrl2YF-X3QOoIbl_45qyCvZHqvrLJdg7VVh7ihTXO79GJGglJe9mPoWiSQFAGdS63mWfTyP1TlYT4xgkyNiTot54TEPGfiwZEBqcbQ7HyNLhKpSI8mWGa1ORqpxH9epdsPpqnlBEaV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار خون‌خواهی و ایستادگی مردم کاشمر به ایستگاه ۱۳۶ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450028" target="_blank">📅 23:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بیانیه سنتکام درباره آغاز محاصره دریایی در تنگه هرمز
🔹
سنتکام با انتشار پیامی در شبکه اجتماعی ایکس مسئولیت دور جدید حملات علیه ایران را برعهده گرفت.
🔹
در این بیانیه آمده است: ساعت ۳ بعدازظهر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف قابلیت‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شوند، ادامه دهند.
🔹
ارتش آمریکا افزود: این حملات در حالی انجام می‌شود که نیروهای آمریکایی برای از سرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌شوند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا (۱۱:۳۰ به وقت تهران) آغاز می‌شود.
🔸
آمریکا پس از شکست در بازگشایی تنگه هرمز بار دیگر تلاش‌های خود برای محاصره دریایی ایران را از سرگرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450027" target="_blank">📅 23:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17ecbe176.mp4?token=hJduuEWsNTTqO5rvFhV_W04xf7gKt5C4hN-Zed_uDAxVpACu6nHIsa7fuCcxaORZDBoDDto1uEfJTeXx9pBslJJiUX7TFtT6brB_GFJZfV7YIfvP5TL8OBq_hOebKCOZDvdLDxFExR6FBQVJay6ng-gem2Rhnhs9QRQ2itZXNnv8aigVczmY2_eur0ec7sb82ZGRq7Lv021wnBiF9VGBQPfgiLLqoZqubyn7cY6et1xyu-ISb65syBaTrlF6nY6Bsy8cIX0hmS43N4Hh0YoxpDiFdbdhMEAZvlXjDYSvBUqz4beismbUcGiYR6qAzt5gNYlhjOPuggtvkz7BWB7B9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17ecbe176.mp4?token=hJduuEWsNTTqO5rvFhV_W04xf7gKt5C4hN-Zed_uDAxVpACu6nHIsa7fuCcxaORZDBoDDto1uEfJTeXx9pBslJJiUX7TFtT6brB_GFJZfV7YIfvP5TL8OBq_hOebKCOZDvdLDxFExR6FBQVJay6ng-gem2Rhnhs9QRQ2itZXNnv8aigVczmY2_eur0ec7sb82ZGRq7Lv021wnBiF9VGBQPfgiLLqoZqubyn7cY6et1xyu-ISb65syBaTrlF6nY6Bsy8cIX0hmS43N4Hh0YoxpDiFdbdhMEAZvlXjDYSvBUqz4beismbUcGiYR6qAzt5gNYlhjOPuggtvkz7BWB7B9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی نیروی دریایی سپاه در موج سوم عملیات نصر ۲  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450026" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/450025" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a35ad7e2.mp4?token=N1k9jJdQg2eR8k_zpesgV7HHGcKwBtm-xi7X8mKG4Fi8mp104BaytQZKF-8W8bxUmI7IEEbMxJtPLZIWMZucBhYLcEdnk0eTil82Ggz8fvO2NwskUZqGvWYwZ6WX79_uREOCDuCh3HicPGnewt-elpGJ8tZWj9ZaXi4PnugcnjX50olzFKSchgJFdWqJPs-7YSDgQcTLbfe9iBzQKwrme9LOW97Vs1vyKAmexU1VdJDVPd0S-CfMXHP-9eS_ZQ4ej3fU4K3sWPuASCjMhyqdD70kxtBaPX_ZQ_Z0ZZPw4HqIPMKEA-ChW7PX1xYtZxJcbHu9TfQaj7nzX5boDyVnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a35ad7e2.mp4?token=N1k9jJdQg2eR8k_zpesgV7HHGcKwBtm-xi7X8mKG4Fi8mp104BaytQZKF-8W8bxUmI7IEEbMxJtPLZIWMZucBhYLcEdnk0eTil82Ggz8fvO2NwskUZqGvWYwZ6WX79_uREOCDuCh3HicPGnewt-elpGJ8tZWj9ZaXi4PnugcnjX50olzFKSchgJFdWqJPs-7YSDgQcTLbfe9iBzQKwrme9LOW97Vs1vyKAmexU1VdJDVPd0S-CfMXHP-9eS_ZQ4ej3fU4K3sWPuASCjMhyqdD70kxtBaPX_ZQ_Z0ZZPw4HqIPMKEA-ChW7PX1xYtZxJcbHu9TfQaj7nzX5boDyVnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی نیروی دریایی سپاه در موج سوم عملیات نصر ۲
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450024" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اصابت پرتابه دشمن آمریکایی در حوالی بندرعباس و سیریک
🔹
بین ساعت ۲۲ تا ۲۳ امشب چند انفجار در شرق بندرعباس و نیز در سیریک گزارش شد.
🔹
همچنین حوالی ساعت ۲۳:۰۸ نیز چند انفجار در بندرعباس شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450023" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c2501449.mp4?token=HYGZbgPHVxYMFo24lqyaTsX0coXeYi4V4P_mfMp4kMQgBoQXkvgxx2-3tI6HqH7JLYY174na9TEi0-fgaXkpaGoNrOURpe9R-tJUi9zq1IRtMZwH6gHpmDvb8CbGAMwGLb26iF5KdKKItPuYoMl2NLogZ_SJlUyyP6XCCre9oRwf6KexkwyhQSGIhUBRcmuoIXbOD22xHOu5j_SfRVgz8e3WhUiGpLo8tY8dO_gWyhthjZDx5CsCKTbd89SjDHxin9Aq7HjexhrkK2C2LeI2mA-8hWJ3WONu-8L4CttrlMmRYUxV_RmRCCmCMEADMesD-DMJEDhKJXl97ej58wowFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c2501449.mp4?token=HYGZbgPHVxYMFo24lqyaTsX0coXeYi4V4P_mfMp4kMQgBoQXkvgxx2-3tI6HqH7JLYY174na9TEi0-fgaXkpaGoNrOURpe9R-tJUi9zq1IRtMZwH6gHpmDvb8CbGAMwGLb26iF5KdKKItPuYoMl2NLogZ_SJlUyyP6XCCre9oRwf6KexkwyhQSGIhUBRcmuoIXbOD22xHOu5j_SfRVgz8e3WhUiGpLo8tY8dO_gWyhthjZDx5CsCKTbd89SjDHxin9Aq7HjexhrkK2C2LeI2mA-8hWJ3WONu-8L4CttrlMmRYUxV_RmRCCmCMEADMesD-DMJEDhKJXl97ej58wowFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های مجری پرچمدار با مردمی که این روزها در خط مقدم در جنگ قرار دارند
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450022" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff6bcc325.mp4?token=XA2dlpJQ_ZD5js466MKrvyCK6OPsS257H_IavtvCapJzFyAWnWDzsbJOimHsKg_PqiucGiVvrQXf3qybN-_R15wxd8VI51BB59RxUmnJKSWZsstejIM8ozckbmxSfsrIFxjeDrcRSA5Z-dJjNNJUOwxfR8nKAKSLq3ZZnlSgaRUtGyiOZ7GJ4etuEaarJUi6HGCaaL_zsFlmwbxWLrKaQmWKDNsMY87_bx0bIiB4rML02M6ljOdyMq8g-jDn1p1SDr501AM_CQiXp9tRnOW1OY7oXd-Iz01nFGQmX3ZAQ8qokc-d6y3HCMVX7DvdERFcZuTKu4A7VbVI3rng4ycs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff6bcc325.mp4?token=XA2dlpJQ_ZD5js466MKrvyCK6OPsS257H_IavtvCapJzFyAWnWDzsbJOimHsKg_PqiucGiVvrQXf3qybN-_R15wxd8VI51BB59RxUmnJKSWZsstejIM8ozckbmxSfsrIFxjeDrcRSA5Z-dJjNNJUOwxfR8nKAKSLq3ZZnlSgaRUtGyiOZ7GJ4etuEaarJUi6HGCaaL_zsFlmwbxWLrKaQmWKDNsMY87_bx0bIiB4rML02M6ljOdyMq8g-jDn1p1SDr501AM_CQiXp9tRnOW1OY7oXd-Iz01nFGQmX3ZAQ8qokc-d6y3HCMVX7DvdERFcZuTKu4A7VbVI3rng4ycs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها با پرچم یالثارات برای خونخواهی امام شهید به‌پاخاستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450021" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08WghAyLkEf5KjkbAzcw56b6Df6uW2HyXNHcofMoo64NUemnqG6Ie6RX1WZx-p4cx4k8RJBcmkSFABqrFknPbsN8i4GLo_6cSd86l0rw2Es7gn3uaWHWhAvEcoWzg1MYzopsvYKb-ys0VfO_3WyzqgcGJS6K_-OHVb0uZk628DE2m6OGGgGyGX_V0tMzz1ZuN5w7h6pLlr6fyD8Vt6NEqhvxYd7COxKotwciR0Dhuy5-WsJmN7MRPN5y8Vwc6Nc6wQC0sZe11W9PBSoLg3TUo0r0Wk8KjqLvRAB8IojdIxsp_FwoPU8atQF0bchunnlY-gW7REt5AjYxYwCrVLFKsA-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08WghAyLkEf5KjkbAzcw56b6Df6uW2HyXNHcofMoo64NUemnqG6Ie6RX1WZx-p4cx4k8RJBcmkSFABqrFknPbsN8i4GLo_6cSd86l0rw2Es7gn3uaWHWhAvEcoWzg1MYzopsvYKb-ys0VfO_3WyzqgcGJS6K_-OHVb0uZk628DE2m6OGGgGyGX_V0tMzz1ZuN5w7h6pLlr6fyD8Vt6NEqhvxYd7COxKotwciR0Dhuy5-WsJmN7MRPN5y8Vwc6Nc6wQC0sZe11W9PBSoLg3TUo0r0Wk8KjqLvRAB8IojdIxsp_FwoPU8atQF0bchunnlY-gW7REt5AjYxYwCrVLFKsA-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راننده‌ای که کامیونش را وقف برپایی موکب رهبر شهید کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450020" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc44b8bf30.mp4?token=c6aQK9ieoZh0FaFx6AEtyowoat3_eiDnehFZZ8WajcliUYQgwVc2Vn4gCz96sI1d3tArrbP_54b5X2YeCjGCkGSPlrMWPDk7TthzP6JEXaKgTg80ACOY5jHlcp0bAhWazKjpIaumTp39rFfre0TdIlwuODED2Do-XkFC77V15r2wwrECHxUC9JXrWr-j3J6L3nmyNSv0lFgmwiqN3RGvuS13w1MMSZkvchnUgIlwakftw3o1j9ITDo7cU8iA6ofeZDN1O8gPL9U83QG8BEIzD5PB2FgFEk12BqxHlHGTmGc_ZvjApPvqEfcT_c8oc_c6ZRl9e7Ev0WI4WHwRxN9STQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc44b8bf30.mp4?token=c6aQK9ieoZh0FaFx6AEtyowoat3_eiDnehFZZ8WajcliUYQgwVc2Vn4gCz96sI1d3tArrbP_54b5X2YeCjGCkGSPlrMWPDk7TthzP6JEXaKgTg80ACOY5jHlcp0bAhWazKjpIaumTp39rFfre0TdIlwuODED2Do-XkFC77V15r2wwrECHxUC9JXrWr-j3J6L3nmyNSv0lFgmwiqN3RGvuS13w1MMSZkvchnUgIlwakftw3o1j9ITDo7cU8iA6ofeZDN1O8gPL9U83QG8BEIzD5PB2FgFEk12BqxHlHGTmGc_ZvjApPvqEfcT_c8oc_c6ZRl9e7Ev0WI4WHwRxN9STQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450019" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a32f2aaf.mp4?token=QsTJWW3xU0Pk_6vqXbHNWxLmkrZfSQzC5BgKLv26mtnRXPht48K0z15UdG-bVfXS9t7EZhMIcjhaxRStloiCxXfqL4ciDjnPbomQSkPOiZNQik89O-hOwWMnAQa3T8yAfb0CsHCUPrEhZ-lpYjzXl17QP-wguW7PB0fiSrWQQK06mMNxCBvP4bEx3Yx9VhiEetbxaZ4uQkNS9tsdabwIuphxHeaZ7nOEaJg85CU8DUhR_ZlAl2588igMi_7vpucxsOr-vghv4qomNoOFDUXb-LDnwGvaZ-P_h1eV43VhC18h50AsNGuJg73Cf38YPW2YVN0e9miulW4TT_Ngt3xHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a32f2aaf.mp4?token=QsTJWW3xU0Pk_6vqXbHNWxLmkrZfSQzC5BgKLv26mtnRXPht48K0z15UdG-bVfXS9t7EZhMIcjhaxRStloiCxXfqL4ciDjnPbomQSkPOiZNQik89O-hOwWMnAQa3T8yAfb0CsHCUPrEhZ-lpYjzXl17QP-wguW7PB0fiSrWQQK06mMNxCBvP4bEx3Yx9VhiEetbxaZ4uQkNS9tsdabwIuphxHeaZ7nOEaJg85CU8DUhR_ZlAl2588igMi_7vpucxsOr-vghv4qomNoOFDUXb-LDnwGvaZ-P_h1eV43VhC18h50AsNGuJg73Cf38YPW2YVN0e9miulW4TT_Ngt3xHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۳۶ مردم اسفراین خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450018" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
دوباره صدای انفجارها در کویت بلند شد
🔹
منابع عربی اعلام کردند برای چندمین‌بار طی ساعات گذشته مواضع نظامیان آمریکایی در کویت آماج حملات موشکی و پهپادی قرار گرفته است و صدای انفجارها به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450017" target="_blank">📅 23:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فردا صدای انفجارهای کنترل‌شده در برخی نقاط استان همدان شنیده می‌شود
🔹
سپاه استان همدان: به منظور انهدام کنترل‌شده مهمات به‌جامانده از جنگ رمضان، فردا حوالی ساعت ۵ صبح در محدوده‌های صالح‌آباد، روستای زاغه و آبرومند بهار صدای انفجار شنیده خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450016" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a1a193cd.mp4?token=IWVEMwLLP0tjx36rLYyTsu1frlM_45Xd4cYSBEHdb625uZOMC1CFXLbYzjmqZhh1rv52h83Q6yQhOh9AwISuwMpO1UI8jVng7yrJAWjbp_HIoWDwezlotJF7jYPi7J0F-AtGJ0lPAcbO1kdWQGYXMMmhl6G0TQwEdIqFV1v9hsD5x0xDXcF12Hzmzf6q5niWZxMWijhTraY6VCxwYVzg9-wKYNKzqykW9Z4JQ5MtDzwvB4Yr3uqamQAhd84a_M7MAY3vHAyRcdW7lX94HRJe4mARZ5B3nPRM74mxUGeo26z9tn2-h3sE98ooZF_yY6RGmAqgO3OtgSlhoUZ4eIQFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a1a193cd.mp4?token=IWVEMwLLP0tjx36rLYyTsu1frlM_45Xd4cYSBEHdb625uZOMC1CFXLbYzjmqZhh1rv52h83Q6yQhOh9AwISuwMpO1UI8jVng7yrJAWjbp_HIoWDwezlotJF7jYPi7J0F-AtGJ0lPAcbO1kdWQGYXMMmhl6G0TQwEdIqFV1v9hsD5x0xDXcF12Hzmzf6q5niWZxMWijhTraY6VCxwYVzg9-wKYNKzqykW9Z4JQ5MtDzwvB4Yr3uqamQAhd84a_M7MAY3vHAyRcdW7lX94HRJe4mARZ5B3nPRM74mxUGeo26z9tn2-h3sE98ooZF_yY6RGmAqgO3OtgSlhoUZ4eIQFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: نمی‌شود که آمریکا هربار بیاید تجاوزاتی انجام دهد و دوباره ما را دعوت به مذاکره کند
🔹
آمریکایی‌ها در هر اقدام علیه ایران باید به این نکات فکر کنند؛ این مسیر شکستی مجدد برای آمریکا رقم خواهد زد. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450015" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a1c41c78.mp4?token=PB1sd9uAysJ6nMv3WLA4nnd5GDfzW10Fz-rUzpCXYk0NvGqLLPiYJyFvCBdYeasBOHru4vZzz0sI31sNj39TwZiH2DqtLBYDcgC4YQLz0xtxHPir_baGNsk3RtKSMukGdmxb0hmb42Dsiz4i_Ld8z2To22oz_vXacE_qmUE1hB_6y6hf7_dJ4uitP8LBrGxZYue1O4Glo77SxJ_6pUBiNKJsVfJWzluvsTzsSfsdQXVCTUYFNMpnFM8kWnMZWynpFSZ6p2oyJaNsLCXTOTWlnHK9xZ3QD7_wgQsTTaKrttA068aBmEio9P9Y8y5fkoVOdjg-Y2LEQp_HjIzmTKlbew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a1c41c78.mp4?token=PB1sd9uAysJ6nMv3WLA4nnd5GDfzW10Fz-rUzpCXYk0NvGqLLPiYJyFvCBdYeasBOHru4vZzz0sI31sNj39TwZiH2DqtLBYDcgC4YQLz0xtxHPir_baGNsk3RtKSMukGdmxb0hmb42Dsiz4i_Ld8z2To22oz_vXacE_qmUE1hB_6y6hf7_dJ4uitP8LBrGxZYue1O4Glo77SxJ_6pUBiNKJsVfJWzluvsTzsSfsdQXVCTUYFNMpnFM8kWnMZWynpFSZ6p2oyJaNsLCXTOTWlnHK9xZ3QD7_wgQsTTaKrttA068aBmEio9P9Y8y5fkoVOdjg-Y2LEQp_HjIzmTKlbew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیوند عاشورا و انقلاب در شب پایانی محرم گناباد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450014" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ac0fafe5.mp4?token=RZJvxl1e0IcLh-l2DaISXW6018Dv7ZnoWUDl27qkB4OdjkghmkVsHtzOZrTTym4OiLvk1Ker0rZS_6Pxgw7mBA3uYXtwpvENTLhAQHYHoMjc67Nd1mv2qwP6LaEIiR7Lb4-WHF40XX2ADaN9RiACAu7EBLjP4_FyvS9zWtWE5NBMqG-Atz1xVILgNjMyj87oB59UZexSFGDPFc8tYGDMT8YbbbybuIOq2rOv7j7opGjdTFTVFSb6mZ2T8bfwDHf8RZktnrliEW1iqlpAXy9hbvtvGs4bjZCzF8MLYb9yuUPrOTNRJG3LNfG3ZZsyJCma_jwfuJecDImOrCTDIKn0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ac0fafe5.mp4?token=RZJvxl1e0IcLh-l2DaISXW6018Dv7ZnoWUDl27qkB4OdjkghmkVsHtzOZrTTym4OiLvk1Ker0rZS_6Pxgw7mBA3uYXtwpvENTLhAQHYHoMjc67Nd1mv2qwP6LaEIiR7Lb4-WHF40XX2ADaN9RiACAu7EBLjP4_FyvS9zWtWE5NBMqG-Atz1xVILgNjMyj87oB59UZexSFGDPFc8tYGDMT8YbbbybuIOq2rOv7j7opGjdTFTVFSb6mZ2T8bfwDHf8RZktnrliEW1iqlpAXy9hbvtvGs4bjZCzF8MLYb9yuUPrOTNRJG3LNfG3ZZsyJCma_jwfuJecDImOrCTDIKn0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های یک کودک فرانسوی پس از گل اول اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450013" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8547bb3b0b.mp4?token=IxgQ8MFLbmir3dsPGOh9ZN-Pgm-SYyx0Pml3Xy2ZCzW5BkMEDqxgS5NDqaDrWbHtRNbXvCt0kX2E-iOunH4INCHgCn6hcUijC5sYwib5-Ajmd5l0uPk4qtqBEFQQXmWrESahrekT13DZ5pWMP9asx2EaOBurBDoNH0FRlOm6Ciur-dSR3dH-GvWYU_Tc3r8qHYnWT_m8B2Gup5O8EOVbINZElCWxdnAKxShrbVV5_7-sU6Ci0FtKJpS790bXzx4yhgCM8uvZNc85FaLpwishidQkGfL9sX9CLFSIyetGaZHdX794wRuHa8fB0Ufwm88omBfT3AqIAAMtzFxIjsrqLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8547bb3b0b.mp4?token=IxgQ8MFLbmir3dsPGOh9ZN-Pgm-SYyx0Pml3Xy2ZCzW5BkMEDqxgS5NDqaDrWbHtRNbXvCt0kX2E-iOunH4INCHgCn6hcUijC5sYwib5-Ajmd5l0uPk4qtqBEFQQXmWrESahrekT13DZ5pWMP9asx2EaOBurBDoNH0FRlOm6Ciur-dSR3dH-GvWYU_Tc3r8qHYnWT_m8B2Gup5O8EOVbINZElCWxdnAKxShrbVV5_7-sU6Ci0FtKJpS790bXzx4yhgCM8uvZNc85FaLpwishidQkGfL9sX9CLFSIyetGaZHdX794wRuHa8fB0Ufwm88omBfT3AqIAAMtzFxIjsrqLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به فرانسه توسط اویارزابال در دقیقه ۲۲
⚽️
اسپانیا ۱ - ۰ فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450012" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd391abf5.mp4?token=jxIklc71zTqZhFAWMemXscJSr1ThSdoukdozKsm0oCjnnXtWO0s0K0uMgTn7X6Op1GN8jYC8d2vzzQBaVlHKPfczl6tB8DiVjhFaJ4OMH_vmADtgmUyhIMB83BjsWLJc8QVPk7gfhHQ_qj9o7s58NBndHe2a8hdRTHAkl6kTjo5wt4iOO6-g1a0OW_RmkGgLWClGtpZaZlBAWTQLNDPw45Y650GNddDPqRXeXKhoP0crh6XJnVcWCp379UMyQjwcJKP88RzBdv72c5WT9M79k2YEU2bSmDJKSfhc2uKhq6g9GBL6qKMlFJBl2LBHckei4ymvVaq6Bh91dc8gsNYJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd391abf5.mp4?token=jxIklc71zTqZhFAWMemXscJSr1ThSdoukdozKsm0oCjnnXtWO0s0K0uMgTn7X6Op1GN8jYC8d2vzzQBaVlHKPfczl6tB8DiVjhFaJ4OMH_vmADtgmUyhIMB83BjsWLJc8QVPk7gfhHQ_qj9o7s58NBndHe2a8hdRTHAkl6kTjo5wt4iOO6-g1a0OW_RmkGgLWClGtpZaZlBAWTQLNDPw45Y650GNddDPqRXeXKhoP0crh6XJnVcWCp379UMyQjwcJKP88RzBdv72c5WT9M79k2YEU2bSmDJKSfhc2uKhq6g9GBL6qKMlFJBl2LBHckei4ymvVaq6Bh91dc8gsNYJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر آمریکایی‌ها فکر می‌کنند با انجام محاصره می‌توانند کاری کنند که ما درخواست مذاکره کنیم اشتباه می‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450011" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c11b6dc.mp4?token=lqe7SvjFVgHgJ8u5S6UHV9s588f7N9ULWaiOXbKBpSJRfDctg6sG_FXxRRtGmLCSzATVMVL9aqpJtxTYDi4QIGOTs5tihEsAnoW4Sfst54DYmMd73paHLrQpyqcBlHwmUhMfhFact3lLg5IFTNx_jedremj6RroZiU_cAhQiIMuzGpFklNJv8xuL5R_wk4ZQpMScX-i90Dfnr2CGGNr7lQwzXErPBbbX76iSnKfGJw97wMhv2hrEO9rGDkv14egoBWrGgAFxTylZMoWxuzeRjWB30A6IPmrSAXE7jSyAcjOyaIrjR_tzsflb6e0WGsMUHzhpdGktHXNyD-U5VUVGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c11b6dc.mp4?token=lqe7SvjFVgHgJ8u5S6UHV9s588f7N9ULWaiOXbKBpSJRfDctg6sG_FXxRRtGmLCSzATVMVL9aqpJtxTYDi4QIGOTs5tihEsAnoW4Sfst54DYmMd73paHLrQpyqcBlHwmUhMfhFact3lLg5IFTNx_jedremj6RroZiU_cAhQiIMuzGpFklNJv8xuL5R_wk4ZQpMScX-i90Dfnr2CGGNr7lQwzXErPBbbX76iSnKfGJw97wMhv2hrEO9rGDkv14egoBWrGgAFxTylZMoWxuzeRjWB30A6IPmrSAXE7jSyAcjOyaIrjR_tzsflb6e0WGsMUHzhpdGktHXNyD-U5VUVGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: پاسخ‌های ما به تجاوزارت آمریکا نباید متناسب باشد؛ باید چندین‌برابر و پشیمان‌کننده باشد  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450010" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14731ed869.mp4?token=KKQNa4WDSwX-ILXHj6xzhhB8-OieX3ouhEkzGgJPxLxURvDor1ANIGnZa4UgdcGaC5GEcH-qTKvpfkUvt3U6KhMGe0vhVfQKubaMKQfdeBaXmHRpwS7vZO021OJMVh2r-C5bQhhI_TYvErEzu1w51b-_c0bdfxWBCvir9Xoi62RIjWJoLG5nIvBLCR_1RXpVJKO5HOU0PMFwqu_JLESYYUgE1cr9v9ih2-xf6Y5CsD2y1S8Djhocuo5PMOPKkqQt4b4BxuQ6ewg33rjmDZw1tQ_UOX_ilIOwuYD-Ki3sg5d4_RrX5TCF4_XOjOnxQKHx_qtN1hIPojMhan-C7yVYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14731ed869.mp4?token=KKQNa4WDSwX-ILXHj6xzhhB8-OieX3ouhEkzGgJPxLxURvDor1ANIGnZa4UgdcGaC5GEcH-qTKvpfkUvt3U6KhMGe0vhVfQKubaMKQfdeBaXmHRpwS7vZO021OJMVh2r-C5bQhhI_TYvErEzu1w51b-_c0bdfxWBCvir9Xoi62RIjWJoLG5nIvBLCR_1RXpVJKO5HOU0PMFwqu_JLESYYUgE1cr9v9ih2-xf6Y5CsD2y1S8Djhocuo5PMOPKkqQt4b4BxuQ6ewg33rjmDZw1tQ_UOX_ilIOwuYD-Ki3sg5d4_RrX5TCF4_XOjOnxQKHx_qtN1hIPojMhan-C7yVYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: نیروی دریایی سپاه طبق تفاهم‌نامه در شمال تنگه هرمز مین‌روبی را انجام داد اما مسیر قدیمی تنگه هرمز دارای مین بود
🔹
بعد از این یک مسیر جنوبی جدید در نزدیکی خاک عمان باز شد که باعث شد حاکمیت ما در تنگه هرمز نقض شود. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/450009" target="_blank">📅 22:40 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
