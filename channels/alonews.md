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
<img src="https://cdn4.telesco.pe/file/jgbFB-Eiw6AhjbiKjitEwtcqtuInrvqg76cb5mGF7hxvuKYkXhcEkMplmptFXPCmkw63_I_DPxu6fLdrX8w3iIx63J9mrxTBu-ZS5TkzGeZqr1gDyEHNUMiBBAceV_9ITI5KZh_TfGV-jJQDkbazdm1MljtdykuzqzFNqpeWtTIzGuQni5GpVm7viA-XMboTMbqz_wNXTKwP1kyphCyV6cxzvq1u0zySVeImvi5eJSl-TKJNaRVIH62oWMJMoqsxvTZAMcFrIWjmXY90-tIvB9KigdXZF-QogN5s-WzFbHw623-EfNt-FU40x4mwAJSQCDNfOmfscyOXASRN1JVkrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-123072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کاخ سفید به الجزیره گفت: رئیس جمهور ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/123072" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فارس: آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/123071" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثبت لحظه‌ی حمله به لانچرهای موشکی (یا پدافندی) هوافضا در اتوبان بستان‌آباد-تبریز توسط یک راننده‌ی تریلی ترکیه‌ای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123070" target="_blank">📅 17:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آغاز تخلیه شهر صور پس از هشدار ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123069" target="_blank">📅 17:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fQDvIrfX_CVrXXrBcCp9QE7Ka0tCcdf-PjNNYvz8vQqqbEs01BF2s3aGED3j90h3N9onj731bEInl_g2l69ve1q3-Oc_OgjojO5zbQ0ZTStIuj5-lftTVpkfGlzAnk2xpGbwnq33bvRytqMAT4dbrGeqSTmG6ku3GI6tjmHgl49uqihqOWTIe2miIEXYLLiMer_QQwPdrJCVcRS_DZUrEQjF8Jzl9XJb8eJ2bxWh1rUmGaWsOm76rO2JZzLbjwH2mvBcBa9nd3LSDQODedHpZjdo4wQbJFKGVPSHowWUe2-P5RyMveuRUSWr9evgdiOxtPz06fEQTSRvEGvIwMe41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ایرانی رفته جلوی کلیسای پروتستان که اصلا پاپ کاتولیک رو قبول ندارند که به اون ها بگه پاپ طرف جمهوری اسلامی رو گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/123068" target="_blank">📅 17:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/123067" target="_blank">📅 17:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eloAes96SnE-cEugZgeJ-Od7LUApq50mYa5hHmUvLiQa7gXdXOqyleoFx-lcZ8g9O-P8PhEBnWCm7OyJHrDEfNZXWvwE_-1mOGpRRNB0Ks5FV2kP6fabPhorq_xYzhcFika_JH2086nqolYXvmN1-rus7lI2SHqaVfRhM1gwcYbNKZ_-Q8jzwNPvN-rB3zineTtcP9_03DPKlNoCykxBLzKnxpW0-cZ1OjMq9o4x1XLi1XMuWKnynxM7sb1g_x51ctZXl0xILKW6XmMO4NyUw-HHGNsvjhbaJ3_oMVhRuajSlbE2qJccS3eFOpaSMtcMwrfXii7F_pJZ_0tuDyCCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل در اقدامی بسیار غیر عادی و عجیب دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراف آن را صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123066" target="_blank">📅 16:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8asDcMHgetcBW6LL7vHubVoqPgL0WqxAXCPaz_S8-iYFBc-NMHtqMO9KGX5LJudGzctEytAEofV-jhajOJD5hKoeN3AIvZlFbMGVizGGMO06RIfU8XNw_V5vbi23G9UxngU64UPwyuolOoFaghJOmxPddHVUbEL4bCdI--P7RZ0pJ7I4jrOtCEH0jfDPMfW-ZF8AQe_-dddxqB8z4Slzyxv2PI47vUCVNApBmLeUItq0JhHKWHiLM7sopt5NO0g221ntEwxtLAP0ksAcl_RV1d6RdUwJDAFEWJ3ULBCrCkABqSrlDnspL6GbV8ny-j6hzXUfPz48Pzx-n6OhZUi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5CcgIboI4HTGpYLsB19Ok8GgRyB5tGD2QLmvvGIEwnPr-YtxBfXgPwBxaYm7-dKpTdLp7umgH48yL0szvxU8_asjVqd3vQkAh6OH-jNG7eUl-9kAasQsG357bzYIFPHlyi5U5N-v8JahlBJYZ1aJw-68PTPALn5303_iZHPtTYtmnLSQRrXesV1Us-9IXUewA0GBctfK7YRts1oVI4dW33MMOMqGo_QJPJTEOlV5EBJwkJhbB1yeZpNGP3txbTff7cL4Z7hIzJvQ_qjdwXlK1G8rz6FYL8Qn2fj7xict6Yh2UNqFN6CpGEMCJ5iH1b9hbjraq-CG4Co2sQe3EBRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xng0yy5BvWgeCNiVvp19cWyjw6RQ7-93C_QShsOXBRd-pjEXrPdQUqK4tK5I3wH9uoN4sJwmAxB9GotYYbM8-evwchHV2z7LKBTkjQRPKlF4v4--TJhvSHzMUfQDQSQm-dIW0yTh6D9u5giCsSipua-cBSdkX5agQwXX9xnnVdORJDjb31im_I82JTI_9HbHTKYetNQJGGcb5E2YrJ0C_SUDWNisSK3FErOs8GAuwHrD3nDu9jCJ1Ei59YOEAoEyuDiSUgfmeAHuPKRZ__LJtcsw8QHSbbzikoEKtXclp_nH70i3u1WXapwA-JwB66eVFRymS7sRYYUbe4ZSs9RzuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به بریتال، کفر حونه و ملیخ در لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123063" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اسرائیل شدید داره به حزب الله حمله میکنه از وزارت خارجه گفتن امکان توقف مذاکره اولیه و انسداد کامل هرمز هست
🔴
یعنی نتم ممکنه دوباره قطع کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123062" target="_blank">📅 16:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyF4gbzXbP9p9v0Y6FsYEYAHdr8jMwFQRMj05akxrswE3b7OLaFaHhNYzdmNdiKc0WsGl2CJ5rU9QQmS9JhxBLJZSjS06W3epgF3demQv9EtDpzT96945JPDLId_O6ZmHmMiwc514Sxfx4S9Hcz4NgQ7LANn0eW9EcloIriU9xWngXJtV3cjY7w0H_r_vZiryrJ2MZN7R7yfpklVwcKP8wajjIJVZRnjkxcLb8f_r_4A9mZscb8DfXsS6Ns9KT5AE921zr0pLLVpOfhdNguEetIowgTk1Pi7QNhNW7Ujx9H51SXRuKaBvNwzDAMjhkFJdJITTKw4F1025wXm8QLWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۵.۱۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123061" target="_blank">📅 16:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfImbSyMgWj1jmbcS9JPL6pGtMtBfhyZF6D3PcTRigFK5_aeJeBYyie3K_-SkwolwHKiO6Gs0oHXHHlpUFCoMiSS-KEEhHz1lrg3M9BEZupBguU0nqxIYZ4aU8ouzeLOmWydO2gQqg_IywvGsNPno8zRbo6N0iI33ufUzvJsfYkSaAPvdSBBEN_4_twmankZ_8toziC8YO9qPI5AKdagsCrsD8Rm3ze1kLQNGCDtu631cPSbgVS52niej6Uv3ZqKk4S2YsTZlIRzI-wVRZJ4Fku1se4JY8oIK6Ehy-hn9BXym5lhBB0ubIGWE-KgK-rJ2c0Qzxt_EeIm1bB8PWhAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وقتی میبینه همه جا نوشتن با دستور رییس‌جمهور اینترنت بین الملل متصل شد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123060" target="_blank">📅 16:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر جنگ اسرائیل در جلسه کابینه امنیتی: ما در حال حاضر با ایالات متحده در مورد حملات به منطقه الضاحیه در بیروت وضعیت پیچیده‌ای داریم. در عین حال، ما متعهد به دفاع از خود با تمام وسایل لازم هستیم. هیچ‌کس ما را متوقف نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123059" target="_blank">📅 16:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/123058" target="_blank">📅 16:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtgDbpi8m7FyZKBnmTrr4tVJOUMB3GmuJe8DQrlUJ3-8ZJsECk2XRNfNbt5Nd5u7daiekWIyYF5DipIs3gdiD10S5mCje0sbCSUxyO8F3MGW08tUWMcEuplaIad9n_p1NF8K01niCWZ0zR2o1Ux96Tw_G8h9OHA14OffPM_1GoWJw86JvmsunGmzONVbNOrIKsjsKFhAnwg1MgANOrIY6JjMvBpEGzjRS_aT2amoz49WlKAj0QQe009E330dFfl9AbqzTKl6lQOtyixsPIeKtex4ll1UvQN_MFULh7hHZE5KeCP4TKCdlRznomTmV53q5NscYlRxAvCkSX_9uvQNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123057" target="_blank">📅 16:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Mu6DalWwScB1diWiIDSPRtgHssufpuKR8hnLn924-uVut4Q3uEq_isXUKzK2rOd_IhN8f2L3lbSBeuxmWpmtRI5ZS-a3MLHvfxbNwbifOvleWDczn0FlbO99q6DDJC6vTf6F1uqLJXIyGf9HHEOFHxYF__hR1PaCyIqxUvCgUmxU1GwYLxs2sSXPQes5sGueMI0wh75ijQqKRfopDTJjWBsixRJzK7h1c4mAcehVnRBeOsS_w55FLlyIjh9HGyxU9dio_4OiZUZ_-sa7tnozDbrNcb3u8sLgAOmHcyrOB3vu2s6eRgf7kc5XLczu4K9nbY4pKHCYqFrXS418eEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جو بایدن، رئیس‌جمهور سابق [آمریکا]، با ثبت شکایتی علیه وزارت دادگستری، تلاش دارد مانع از آن شود که دولت ترامپ فایل‌های صوتی و متن مکتوب مصاحبه‌های خصوصی او را منتشر کند؛ مصاحبه‌هایی که با یک نویسنده در سایه (نویسنده همکار) انجام شده بود که در نگارش کتاب خاطراتش به او کمک می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123056" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سی‌ان‌ان: هزینه‌های جنگ ایران، بودجه نظامی آمریکا را به شدت کاهش داده است
🔴
پنتاگون فشار مالی را احساس می‌کند و در برخی موارد برای انجام آموزش‌های روتین و تعمیر و نگهداری در بحبوحه عملیات‌های جاری خود علیه ایران با مشکل مواجه است و رهبران نظامی یونیفرم‌پوش کنگره را برای حمایت از بودجه اضافی تحت فشار قرار می‌دهند.
🔴
بر اساس یک سند داخلی، سپاه سوم زرهی ارتش، ستادی مستقر در تگزاس که بر تقریباً ۷۰ هزار سرباز و صدها تانک نظارت دارد، در اواخر آوریل شاهد کاهش تقریباً ۲۹۲ میلیون دلاری بودجه آموزشی خود بود.
🔴
سرپرست حسابرسی پنتاگون، در ۱۲ مه به زیرگروه دفاعی کمیته تخصیص بودجه مجلس نمایندگان گفت که آخرین برآورد پنتاگون از هزینه این درگیری تقریباً ۲۹ میلیارد دلار بوده است.
🔴
هرست اذعان کرد که این تخمین بر اساس هزینه مهمات و هواپیماهای منهدم شده بوده و هزینه‌های ساخت و ساز برای بازسازی پایگاه‌ها را شامل نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123055" target="_blank">📅 16:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
لیندسی گراهام، سناتور جمهوری‌خواه کارولینای جنوبی : مدتی است که برای من آشکار شده پاکستان به عنوان یک میانجی، بیش از حد مشکل‌ساز است. دشمنی آنها با اسرائیل دیرینه است.
🔴
غیرقابل انکار است که هواپیماهای نظامی ایران در پایگاه‌های هوایی پاکستان مستقر هستند و لفاظی‌های گذشته مقامات ارشد پاکستان علیه اسرائیل نگران‌کننده است.
🔴
وزیر دفاع پاکستان گفته بود این کشور هرگز به توافق‌نامه‌های ابراهیم ملحق نخواهد شد زیرا به اسرائیل اعتماد ندارد. این کلیپ ممکن است یک سال قدمت داشته باشد، اما من می‌ترسم این احساسات تازه باشد.
🔴
در این راستا، ضروری است پاکستان اکنون به درخواست رئیس‌جمهور ترامپ برای پیوستن به توافق‌نامه‌های ابراهیم پاسخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123054" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltaN5PKMfIuFFTLcwgoSjtNkDIDn7It8hR-e7Asmhazm8y3Ds3oB9xxue9_Zf8_YwZ0TO5IeOCj8dQ016nlFj2r7nCXP0LRZgrzzMdjDPZqpm4qh-bZPsrwivXVRYhXRalrQeY_ot0lH4BuJ5ybo5z_d56HmLwISGL5h7ne5kJ1AR_UGMu_o5XsUcSuKviTCfp3nNQ8YpCasqGgXcsiu_ODEw_EG3YSLExgI2jGxyM229FIuAVrIEpzRJpd4Fx-lmIylSJiqXmifEUOP1bmadhd3WNeMshUxktXdQmrDGH7Un5GAgtGHfAh5SHYnR4Czo5KJOcxPew9lVpd5r-_ZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل به شهر کفر حونه در بقیعه غربی لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123053" target="_blank">📅 15:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: برخی از بندهای یادداشت تفاهم بین تهران و واشنگتن
🔴
واشنگتن محاصره دریایی ایران را لغو کرده و نیروهای خود را از پیرامون ایران خارج می‌کند.
🔴
ایران متعهد می‌شود ظرف مدت یک ماه، تعداد کشتی‌های تجاری عبوری را (به استثنای کشتی‌های نظامی) به سطح پیش از تنش‌ها بازگرداند.
🔴
هماهنگی در خصوص مدیریت مسیر کشتی‌ها با ایران و عمان انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123052" target="_blank">📅 15:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زنگنه، نماینده مجلس: احتمالا عید غدیر جشن پیروزی ایران بر آمریکارو میگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123051" target="_blank">📅 15:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXOOHefzVdKhcyIHhI0c3yan8eM2eViqafEVeIjIl8T_2uF37qf2JB5AyuCqvleQzw25UVsH99OHbqgeoFjNaH8GY5tE-p0ttj69JgvWX_t9m4-F9vtUa0Qh9-NNSbmTFnb4b-_MTdOdloDZo3KxiXn2CSNf1s0qmeqWAb1SM0XuQ87IE_sm0Kcl8qmZ1Ja3f_bepVm6vcAZkmVkZbvjogvliSIRUjzOpXgWzUTOliEP_YlNHQlZ5IQRrma5yzUkL7SgDKqYA0IuoRV6klZk7EAUUlIzNtK35p_hJ__Xyura25aEiwcTStBfiLR18pSt-53Jqblm-f51gpHFrX_INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر نشان می‌دهد که هواپیمای سوخت‌رسانی جدید نیروی هوایی اسرائیل، KC-46A Pegasus "Gideon" (301)، اندکی پیش در اسرائیل فرود آمد و ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در مراسم استقبال حضور داشت. این هواپیما اولین فروند از شش فروند سفارش داده شده است و امکان سفارش دو فروند دیگر نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123050" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123049">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dff2f7cb6.mp4?token=C19_QM85BP7uih-PPoBBcNyiOy54sf_o_fPafz6iqqIWB3CkweX_7hXEBDog245MrZVbxdcQporjE5ha6FC11puT3Fe-ysNI2tnDk7XH4aC9TCuFFJMzYK6Z55VzL1n8CXlkVJ-KIq0y8wog12xpcCI8RXvOrAARYJ_gDx9vNb08fujKpSXxvuW9iVDzqTSQ8jalPuW2z_Mlw6lI7T_fIycNGMrDSRMs1AQxPLsRBK1rUDjogFjDJhplzhC5H_Vdghaj_S8oYf7WvtF3JDSAa77ThPgAY5PiYul-iyqx8yu6y7-YJfz0mAKM5n7CXIk-HaW23wwNaA2y643MeM2TUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dff2f7cb6.mp4?token=C19_QM85BP7uih-PPoBBcNyiOy54sf_o_fPafz6iqqIWB3CkweX_7hXEBDog245MrZVbxdcQporjE5ha6FC11puT3Fe-ysNI2tnDk7XH4aC9TCuFFJMzYK6Z55VzL1n8CXlkVJ-KIq0y8wog12xpcCI8RXvOrAARYJ_gDx9vNb08fujKpSXxvuW9iVDzqTSQ8jalPuW2z_Mlw6lI7T_fIycNGMrDSRMs1AQxPLsRBK1rUDjogFjDJhplzhC5H_Vdghaj_S8oYf7WvtF3JDSAa77ThPgAY5PiYul-iyqx8yu6y7-YJfz0mAKM5n7CXIk-HaW23wwNaA2y643MeM2TUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم دوربین مداربسته لحظه‌ای را نشان می‌دهد که جنگنده‌های اسرائیلی حملات هوایی به نبطیه در جنوب لبنان را انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123049" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123048">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFKYahq9kMfI1HRjPusWXE8sNA0H-85qkXhlOxWmQR_5jib7ydN903IR8sEfvIbE_dKbK5t6G5iEQXk6B2lkjTWTrDs07CVKWtP-jjB0dm08-LtjrzRFxdINno9ORiy5kwhugYEt297TjqGpBygzU7YK3dpkLca053qr3a8EVfVkSJPGFWRZHbtMlGZT-BQTVRmgImhTwCnEyAB_Fo743eBU8IfUUuFWSGTi08FbMETeNZWJFbi1XRSMH4kaurzcrMb-IoGce7gjrcSELHXR6HobGzF7bdJ4RZvejB6Wi9eIbA0UZZ2wGBGZq7w3DTZaGLrudHR8TF6uLXfR97GtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده درباره محاصره
:
تا امروز، ۱۰۹ کشتی تجاری برای اطمینان از رعایت قوانین محاصره به سوی مسیر دیگر هدایت شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123048" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123047">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_uYRwlAPfCNOAF1gS8aBNVfyNwWelDspE6yvSeu21OtOVBaM3BmGRASvvpxuWTJAbKXnfEek6FpUKaT5IwFswDExVfccc7hMX239OpyIUs3KCJRAO_kLBDdWm4wOwm4WuF5IY7RZTt1jSjvxWEYqcURGHhwChg1wc4-AF8o6jds-0ANLwsiur8-bV-BKUL1KJJOC5hohg-1HkKgZH4a6TV6nawuKxMPGuf8-K1z3K7-k3eHpukq_7gSj7H1Dov6bUCI1KlFn8VwLy0_SXKFlaBbhN8yEEvJRY58J5em9sPZaaaETQXCv8x8W2P8TcR_hJEXfmi8iXjmZtAq8O-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت امروز اینترنت بین الملل ایران از نگاه نت بلاکس
🔴
اینترنت هنوز به وضعیت ۱۰۰ درصدی بازنگشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123047" target="_blank">📅 15:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
العربیه: به گفته منابع، احتمال دارد طی چند هفته یک توافق میان آمریکا و ایران حاصل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123046" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
باقری،معاون دبیر شورای عالی امنیت ملی: ایران و عمان در حال مذاکره درباره سازوکار مدیریت تنگه هرمز هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123045" target="_blank">📅 15:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123044">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نیروی دریایی سپاه: ۲۳ شناور تا این لحظه از تنگه هرمز عبور کرده‌اند و عبور شناورهای دیگر نیز تا ساعات آینده ادامه دارد.
🔴
عبور شناورهای کشورهای متخاصم از تنگه هرمز همچنان ممنوع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123044" target="_blank">📅 15:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfPHzwyaBzqhE6Ory73sWAigTjOh5DAiVsWiF5mTc25Vw5t7N5eSrtH_0hz7y_X0r-taFopxGQiawMT5ec963UdPcqhB5Y_1eDjpIqZqQ3962j8jnfySa5CTkdbkT0DDDoKtmg-L4Fw63T3A7hWdrOHUL-jyXvZYDcAXSahWxDipph7M8aWW4P4HFYqoIOZtaJ8hlINKXe0GUv62_hNY7s9JyPrgSKMozrL2gFpX6tKTjZQQJaDHMwHKF0Z2C-oCkJw5xazvjVId8o3zfUELnxQihivgU8lvT5IzbR4OnU3pVHoO5yK8MC2tNz_8bgQR4gy2Y9YjJdVRhuG8lh23nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل، ایال زامیر، امروز ارقام جدیدی را به کابینه امنیتی اسرائیل ارائه داد که نشان می‌دهد از اکتبر ۲۰۲۳، نیروهای اسرائیلی حدود ۸۰۰۰ مبارز مظنون حزب‌الله را کشته‌اند، طبق گزارش ینت.
🔴
تقریباً ۲۵۰۰ نفر در جریان «عملیات شیر غران» کشته شدند، در حالی که ۷۰۰ مبارز دیگر پس از اجرای آتش‌بس کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123043" target="_blank">📅 15:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyIsb22xPWIyQfJ-e2b6s0lh1rc8vH9-n48Pw85ZZudUyPYxjBgAueVzbkRL2JdtkZt8K1iS6s4buEA8p0bHhuMIEcAbLW3PdtxDZi5-bJ9a8KtRTvxIes-li0aMyDXwCbKjRG_QJ1G2tHcNrYgEQvgN4Q4K2WN6sN5fvyMurnOd7XicbWiGRRuv1HWp5Zp7_UyB5BZkgtvSoR3Kqu4j60g_CxBcsRMP_Zez8eSBY4hgFnDeRX8jPeb1UdiFjYLqKmEbrm6Hp9-Ek6fHzcn81M47Gk2iNiwysTvgerYB05ehu9iNZLY2s2fhejCGWbwNTQ2GhKtvMll13dENY7qx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: اگر به شهرک‌های ما شلیک کنند، طبق وضعیتی که در گذشته به آنها عادت داده‌ایم، باید ساکنان ضاحیه را تخلیه کنیم، حمله کنیم و آن را ویران کنیم.
🔴
اگر پهپاد باشد — دیگر کسی نخواهد بود.
🔴
در حال حاضر در این زمینه با آمریکا در وضعیت پیچیده‌ای هستیم. در عین حال، ما متعهد به دفاع از خود به هر طریق هستیم؛ هیچ‌کس ما را متوقف نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123042" target="_blank">📅 15:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عضو هیئت‌مدیره اتحادیه مشاوران املاک:پس از جنگ ۴۰ روزه، قیمت‌های پیشنهادی مسکن در مناطق مختلف تهران به طور میانگین ۷۰ تا ۸۰ درصد رشد داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123041" target="_blank">📅 14:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eziDnir3JK-8mHmAEGb5lzJxzV6j7ZaDjSI4-XM02FsHdLDAm8772ODikj-GrOP6WTo49yWCnSfdbfLdCNVdALpiTIkaesRwXek6I_4FZ4mB00jS0VboQFF7XIrfU139sgbyXDl-coff7SYQEaeEXHJYtKvpLf6kv1uv3us8bLKGCOai66doX7xN2LCcOy2fer3tluSEae8ZAGYBD1Hib5xUVxyAIJFkX3msVKfAaLyGR5-6F10wqHk0ZzI2G9sOxE3FUR-lMhZvoFtqHr3WFTbkGJjhbV-t9lFCvWp5QOnbti6KxaAZ52MeGS8tPRHZVKXwX2YSyLetPKgwKY1cTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzR9M87tLX8vY6hMFwV4-zCYgSOWtBOzWrD-oHr_tklAjEghlHzrjcca260UEzoeaDTibJjqFh7bIgMZiHaNxkFgmQQXZltTSNWYKDBosdxPF5jc39_a2ak4RmpLbO-IKt5PPE-XBGKINvzQmdeLFAL0XDcq-aeDV0AfKWbt3SPYurYpxspagJCVHqMC75B6dxU8863ZF_5aMELwnNaCuQt4zYP4NytGc_icVP7b61cFVVyY6Lia3rkryLl39C1DQo1_Mnrf_vu9UOu63AQFOQeH--tfc0lvXcoOrO_PElhKTnZ2PgXu_P2z27HR2Z7arj-2f23lbcbNPEX6OjizXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIj0ZB2MKm8l7JzFcWShtwxZGIuBTKTFDdCOv8gjP8aW7X9JM-QDEN5V_XltN7ZaGGyVlB1x-4b4UI2CG37GgdV0_EX1SnkxO_-cGxHvKAYgH9tOdTVpvzj-pY5DBLoBLQpgvbnV5R9_BddAWyt1NjUyxMzMrsKhrElyz5ZqwsvT_BLsNCXK_gVBdY_xdcbsI-GJF1iSfWVqloCLc45ahTlbJa5_l2fMw6brxWFNTbKh34UvQY_RccKAuagjJm_4LWjjdVO3wUaXoS7uyrmAkp3RQdWBvjPcZlZ9unVGReRWNlzcJTfguufHhiKxkunF_gNNuNPYLb1qbuqDLC9lBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی لحظاتی پیش حمله هوایی به حبوش و نبطیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123038" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
علی باقری، معاون دبیر شورای عالی امنیت ملی ایران، امروز در حاشیه چهاردهمین نشست بین‌المللی امنیت در مسکو با مشاور امنیت ملی سوئیس دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123037" target="_blank">📅 14:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
العربیه:  رئیس‌جمهور ایران و نخست‌وزیر پاکستان امروز به صورت تلفنی گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123036" target="_blank">📅 14:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123030">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCeV8pUJtPbod4JyF2x22rh2qpRZRO-ZbHu2NlS5fY7K-LCIiHqiTgchAZ9Xa1y7fp24HgZcnOurKx4QZLuowGwkcLis1gGe9MbFLqfBI4G7MZ7ovpcCGwRekCX1AbuhjZVgJzencDkhgGmsj5ITP2RtvwFTSlQDQPr4xCpXmns8os7YjRgLGGE4xNsQAwUn2RwErw5MTtxJa2CY0mNIi0a7d_BNLzA9VuMQf9FHVdWmavdvq_IHZfV2G5BAtRyoxZVRwK9n5eKZHYsH9UEXSGwYa8VFvefaTofkMczytnJwBB-srht-ghNgqonv1svogNxgxaDtg3JT8t2rTbmKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oa_OVQL7RuSbZ_E3yS-R4ql9sQIH-vv00Yz0yyr0BFPDdV-JxB5hL52XjTaddHxDw_bgdKwZLDnKfDl4Rg1xDSGgvTNwvBAB6TRX0CCXdgyojiu7oHI9ymVMfbg-XOdJEHcn0piBNNcNlLspgc4DTAtYL0XZf_V1AQdpvSWFgYvIdrsz7Q6H4aAhVEwNW-xYw_HxXJpGYezkObpgJF0zGbwtlILmKofjUjEa8dqHrW3YWW2_-qBgyWFeFiTxxK7YM0M20ij0mMnRAwDidiPQTITTil0Lpul_5WOjlYqeI3FrMQ4pok8-cBnbcqUM3mkSUHDFmM9KVyy2CWXPCb7k3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7xLgHK2R5Gyb720Wg-VC5oZmvx8w046HjbGBGckgZbQv2r2e9yQVGkcyoNETbVwlL9y9MAkOdwDeX6Ai-BDbpik1gko4u5tEwlY50r7MsbKG9jUVKg6WkKZIelaeKG0JkWqGLHr6fD0n59kCIhmtCT44Y3oGdKR6UtXNVnt6HAaMYEC7FiTISzbrVoztIzvCYrrDc1fNXA8_u2weyIxhUxpInx3G2m7Vr_5vCA-Mkzq1wnYhUanxaf6Bb9kgwBiYdF3PDdzD-vXnoHdCz4tmsJb9ar7gnSfbQmfkXlshhIs38NilL8Rmb6n3iJSQ5zSDv2S80A30-sYQ_mPZ9_kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTDuOHUwyi-UIM2vgxoNN6t4pF1R_XA81ItqEQb1xnVznxi_NwmzBMIWddfTSnEOiiZP0FQrbZ9P6JEPutJpSWXBskGaiABi82lyLOIc8sgblMeeQY7iXVrlS4pNDk1VPa0xLu6rko5JzkAqP0yi7-lEBMLtMpUPy4YFnPv1XzJc86FwRAujH4QeGPOx4LMueeh1SdXmFO4iEx7Yn8xJWlHDF7BdIa-ncO6JICEEVvtnjJ2LU59fghXQxfda4HPQy9T4ylCK29XBVo9UeZkytAotszftTaXQ95C5hZ9jtU7J1iR1P4J-p-1vqfM-3Y8XZrDJsno90pvWndT_82vekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH-8hrFxCyk1npcWs-I99Gpmv_MzGoPBAv88lHYT3ZWYIFl8U3vAgQjpHVFLIBkRV6NXEiCoCMSNmGV7Z3_mHPBiAkVXSfi5QHekVHe3PX2OMA-gmcW8wjr2xnOpQXT41hP2_h_pigf3qgHg_Wlz2watbFdaH3aFGPXdfUBhAFB7CswzLFEh_ozxA3v24nOueLGH6f9BqM-Smar4FGkM7K68m3pPZ5LsIGnwjG3eRyu_DgotGlZ-Y5RXs8LVMXp95sivOtkAkIy56Xg1awUqhl5QzZqPodJvMqAS1jyKhxY6MpNTCwvWLB_a8o22IHF55sLn15G2mlasledXxyy1ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24df64f5f1.mp4?token=rGljknLxaRdbXoo9zdivkbU7RwIcigA4GWV2V1dQQFvGxUbtc6nFPJ2pwhPSfukJ-axf6Un0FYAjDaV-a7oiIVp4vJ8HDlfybiND0tV4XBAGA9vTEKCbK1qR0iOdIKDEAW4B3_fYIJYGDyRu7Ty61fiN_kBtR-QTv6l5YhvupS-ONsiRUZRUfjEhaTI3AgGZ9sGU2pe1gXYm7SFuTO7zwCGkk30nuOHALJidI1eXSptpYTR7a81L0Ap2WsPbaTSx8q0Kk2_2rI73F8FLFX349HSuZ9OKiYfCzi4EAMc8xFr0DuysuHmthJyjlRHvv4DTQxKB0iu2BeIzd7k6TA8Pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24df64f5f1.mp4?token=rGljknLxaRdbXoo9zdivkbU7RwIcigA4GWV2V1dQQFvGxUbtc6nFPJ2pwhPSfukJ-axf6Un0FYAjDaV-a7oiIVp4vJ8HDlfybiND0tV4XBAGA9vTEKCbK1qR0iOdIKDEAW4B3_fYIJYGDyRu7Ty61fiN_kBtR-QTv6l5YhvupS-ONsiRUZRUfjEhaTI3AgGZ9sGU2pe1gXYm7SFuTO7zwCGkk30nuOHALJidI1eXSptpYTR7a81L0Ap2WsPbaTSx8q0Kk2_2rI73F8FLFX349HSuZ9OKiYfCzi4EAMc8xFr0DuysuHmthJyjlRHvv4DTQxKB0iu2BeIzd7k6TA8Pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین ارتش اسرائیل به مواضع حزب‌الله در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123030" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123029">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idKbi7Y7980inOs7kYsPHHG9lIFZmqyqTj4dVT3fNtQYCAThdeN2BgVjj4o45f14TsABDt-rVhVtfekKS4CJ_-bcSm3uilknGuNcmW11dgktwW6ol07PNwra3rMlIvSYQWz16tVjslNVZqRnGRsBiDA4Mw_gsHS1K6oC8EFBeCi8Vl-oB6gobEuBukIiB4sxVRgJRKGVnhsctD0GyFMI5eN0KJqQD-eQFtOW2ZfcpOFvGp4EL4eb5feaoCPm98QJjZbjhWMY3u6TFADSqCqZ_YcEpx4nStjy1c6rZKcWaV2mEX3mJKSbz3sVTd4gD-rGpEL7S5SlOnloHhD7u7Ea4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲ اسرائیل، زمانی که توافقی برای پایان جنگ ایران امضا شود، تمام هواپیماهای نظامی آمریکا ظرف ۷۲ ساعت از فرودگاه بن گوریون اسرائیل تخلیه شده و به پایگاه‌هایی در اروپا منتقل خواهند شد، در حالی که در حالت آماده‌باش باقی می‌مانند تا در صورت از سرگیری درگیری با ایران، وارد عمل شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123029" target="_blank">📅 14:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123028">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aded17f1da.mp4?token=T9BbtH0isWBCzV16EqSjUbLnlHdgOXeGmel7ed4EzumAnBmfVdmrkSOVHa8oH2Sp_8-mriluH9EeQWHxpavCUxoOQoaX_OAVl_S8Kw6oL-WutkQVvGuZOVYGdcChVR7jtR_ZV69Nqhjoq2_cxbE8DmEqaIBOdn2f0_RzkMcCejvsoJdTF9sQ0GDoDdTeOCP1a68GB1vgfTpQuj5Z4evmG0A56t1sgrVUfn6pyipc1WtDy4Ai84hSRCxPECcgjt6Bd99FL-zXeOKOeBCXjgFUM4vYqUaAfvhFxXQP-Fk2l63-Tm7XfGmv8T6hMTXb2u-kbtFTCNntol4let3wMzqu9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aded17f1da.mp4?token=T9BbtH0isWBCzV16EqSjUbLnlHdgOXeGmel7ed4EzumAnBmfVdmrkSOVHa8oH2Sp_8-mriluH9EeQWHxpavCUxoOQoaX_OAVl_S8Kw6oL-WutkQVvGuZOVYGdcChVR7jtR_ZV69Nqhjoq2_cxbE8DmEqaIBOdn2f0_RzkMcCejvsoJdTF9sQ0GDoDdTeOCP1a68GB1vgfTpQuj5Z4evmG0A56t1sgrVUfn6pyipc1WtDy4Ai84hSRCxPECcgjt6Bd99FL-zXeOKOeBCXjgFUM4vYqUaAfvhFxXQP-Fk2l63-Tm7XfGmv8T6hMTXb2u-kbtFTCNntol4let3wMzqu9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری فاکس نیوز: جزئیات نهایی یک توافق احتمالی بین ایالات متحده و ایران همچنان در حال مذاکره است، در حالی که تنش‌های منطقه‌ای با امید به اینکه یک توافق می‌تواند از بازگشت به جنگ جلوگیری کند، کاهش یافته است، برنامه هسته‌ای ایران و تنگه هرمز را مورد توجه قرار می‌دهد.
🔴
مسئولان منطقه‌ای می‌گویند اجرای توافق مهم‌تر از کلمات خود توافق خواهد بود، هرچند مذاکره‌کنندگان همچنان در حال بحث درباره زبان خاص و جزئیات کلیدی هستند.
🔴
مسئولان درگیر در مذاکرات می‌گویند همسویی گسترده‌ای در چارچوب پیش‌نویس مقدماتی وجود دارد، اما تأکید می‌کنند که هر توافق نهایی یا یک «توافق خوب» خواهد بود یا اصلاً توافقی وجود نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123028" target="_blank">📅 14:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123027">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63369dc297.mp4?token=CUdDtbuv-WKNiXcifkeYYMlkZLHUGHpOuo5FzGfxOhIrC8hlmAb5uLPW17qfvoGPwLSZfS0ia_0TnEuQI_yFUgALU8-2dbBA77aBuUjdevgSN-xmqoX9vvCzR1VoisAEKfiwhM4QKDLaEIwoPozleSb3_27haamQWbgM9F507Y6Ogwhl0PPEn-jJ5W-fgA9h9pX-WndD_iD1XvlM_dA9bxt6Xlfcm32ZW-oOVEYqsAcNPOAbRIjiDB9qVBtszO0h9PeMSryPqL_PQLrXk4OTgeFW2bCMW1bY9b-uLreh4g_ISdeLUHCUHl-6TTbs6o0B6GOK_Rpk4UOz9-9xlhfkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63369dc297.mp4?token=CUdDtbuv-WKNiXcifkeYYMlkZLHUGHpOuo5FzGfxOhIrC8hlmAb5uLPW17qfvoGPwLSZfS0ia_0TnEuQI_yFUgALU8-2dbBA77aBuUjdevgSN-xmqoX9vvCzR1VoisAEKfiwhM4QKDLaEIwoPozleSb3_27haamQWbgM9F507Y6Ogwhl0PPEn-jJ5W-fgA9h9pX-WndD_iD1XvlM_dA9bxt6Xlfcm32ZW-oOVEYqsAcNPOAbRIjiDB9qVBtszO0h9PeMSryPqL_PQLrXk4OTgeFW2bCMW1bY9b-uLreh4g_ISdeLUHCUHl-6TTbs6o0B6GOK_Rpk4UOz9-9xlhfkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مرد آفریقایی به همراه چند تن از دوستانش قصد داشت تا معجزه حضرت موسی را تکرار کند اما ظاهراً موفق نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123027" target="_blank">📅 14:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123026">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNylDxjtJUdBYcMTtsEDpE3jLkBZ1uXi2B32dp62ACgctYm9S-JvnW4j6NXYmVhU8JDJs70VaPrMhtc32DGCKIa-q6xfZHx1OSuS0d1ZjL2uSMsnR7kbsouSVggg-T0Ixv0KzPgJb_yif4-1FaM-IacMo8Kt5t6ekfG4Qv9T3qbyEQPCRi1Fg0sMqSEpfGP_mnoMNtoHvvxWW0pjnaWqJ6Cw6PoC9bM27Y2EITwkfv-9k70QMsWYqS9rhZV2Hu_vSfeDcHDK2tFZhdrfwtp4OmsUgs9HjxxyO7z_EM07HQOPYpAFbsaXNFGyzo4Js5IFGHRTsM4U966AlYu0nGE-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123026" target="_blank">📅 14:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123025">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a909976f6.mp4?token=TJDFMBsZsSQFpvOjxA2bcbS8zI_VuTIewJ1aJZfCT-s9vea8dhR6ZZp5ovZJXn2ONJUwVG7O2aKtxQAP8tBZLu5EeeMnOXsdcwItLX4b3nVdNfJQAHjFnAFap9CZmcXcTPn6Gv5UqkRHtIRP_8aAhfyHZo1q-vvWWfHkkSTmypgr4p31-bEBotCBYKyx_OSSqn6vo7VbFXY1fWRMD7gW6qIqYWoxb8J7LPttW-5YT5z25Q2XNh_EYTX7pcPChV6YmERnxKAklY0mngUhVXV51nfl3Eb_4E8JJLe2wdOhzdyhT6-2E7lxRDJw2WpFS8CbpxP5u6YF4m-VcB8JJnOUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a909976f6.mp4?token=TJDFMBsZsSQFpvOjxA2bcbS8zI_VuTIewJ1aJZfCT-s9vea8dhR6ZZp5ovZJXn2ONJUwVG7O2aKtxQAP8tBZLu5EeeMnOXsdcwItLX4b3nVdNfJQAHjFnAFap9CZmcXcTPn6Gv5UqkRHtIRP_8aAhfyHZo1q-vvWWfHkkSTmypgr4p31-bEBotCBYKyx_OSSqn6vo7VbFXY1fWRMD7gW6qIqYWoxb8J7LPttW-5YT5z25Q2XNh_EYTX7pcPChV6YmERnxKAklY0mngUhVXV51nfl3Eb_4E8JJLe2wdOhzdyhT6-2E7lxRDJw2WpFS8CbpxP5u6YF4m-VcB8JJnOUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی پشت بام مجتمع تجاری در شوش تهران
🔴
سخنگوی سازمان آتش نشانی و خدمات ایمنی شهرداری تهران از آتش سوزی بر روی پشت بام یک مجتمع تجاری در خیابان شوش خبر داد.
🔴
با تلاش به موقع آتش نشانان این حادثه بدون سرایت به انبارها مهار شد و افراد نیز در همان لحظات اولیه از ساختمان تخلیه شدند و این حادثه بدون مصدومیت به پایان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123025" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123024">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=XDIHFHM788nNVLZpq1XRMzkFv40vcxrM9TvrbovsxSxm6uuUGZxK7Ys3xE1RtMgj77fy3ETxzogo-2zkjSxs-_N5x9rfkC5bF-s16zM10ogDnznazbgmY5WY4acejKl1gfC36V23ejVmVFvo_44bujpThJpgsb8m2ufBiClMGanVAABCyfUTOO0KrGJqo_tKJiukGES0rPYys1lyVychmfSqG-40rQLDNu63rq-sQzjBp69N-S0JqgkXEo5CBCCy7Z4olUsgnPPHksB-yFAzx_hW89kJ5FFr0hkbbsGbAqpETvjMFmxNo69rRDsxotcycfvZuDD3TtsWJwT46t7ttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=XDIHFHM788nNVLZpq1XRMzkFv40vcxrM9TvrbovsxSxm6uuUGZxK7Ys3xE1RtMgj77fy3ETxzogo-2zkjSxs-_N5x9rfkC5bF-s16zM10ogDnznazbgmY5WY4acejKl1gfC36V23ejVmVFvo_44bujpThJpgsb8m2ufBiClMGanVAABCyfUTOO0KrGJqo_tKJiukGES0rPYys1lyVychmfSqG-40rQLDNu63rq-sQzjBp69N-S0JqgkXEo5CBCCy7Z4olUsgnPPHksB-yFAzx_hW89kJ5FFr0hkbbsGbAqpETvjMFmxNo69rRDsxotcycfvZuDD3TtsWJwT46t7ttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
70 میلیارد نخ سیگار در طول یک سال در کشور مصرف می‌شود
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123024" target="_blank">📅 14:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123023">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GZc8-Hyodji2MTykAzXnkH2wWQQGq7X1oyCmCufaQphs39O3HLssfTs5ItPkLFyllAxbAqkhVS9oY35tyNDfOu1jqMDlZmxH2U7tCyhARKfMX9vXEktVenqYF0TeBKT94e78q7JpnpcxV_IhhD-RMrnWXJRBZUSSdChJvYHy7PrPhnr4JSS-T9bemc7B68o47yNk4RvH5w_p_2os0qlbI93ZU8Qhqk9o_pZBPMlukdvgFlH4tN-VEXEt0HLw9obf6Baj3QCFyTT-SDA4k11gWM-eWK_9y-NxGG_MQ2X5nizG-GCHIOv5zZepQ_BM74HVneczdTUlCNoQooa6-8Lc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول امروز در پیامی به کاربران اینترنت پرو اعلام کرد در صورت تمایل می‌توانید اینترنت خود را به حالت قبل برگردانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123023" target="_blank">📅 13:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123022">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCZg8BT4o7j23sfXjPVgRoaQK_TTrqh6Vftx6pZCC5UZ-tTv9c2d0reOZmYNW358rRWyhYzayIqsTEDd8Xlc9gMN6QDvMfeyABMehx_dl3ZASuWwzX1-tbUOxJxOsWb8VVwtzewGX_hP3pTJAXzb4P2wYJzFetX4z0DIHebMle4QQHOPmDpsybFxS2pGpqoUBRB3xEAz9ozPdUZxOovu-yUNpoNss8v-oeTnpZMkddUuqYdn3EvBr9nsPLMcxTO4jUS6pHLzytNVlOAdOubmXJjthhaHpV9qo-10bu9OcGqzG8_5rxpmAFbJaSmoMpI0GWIy7IOUdzPUBXcSqXwe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال کاهش حجم نیروهایی است که برای اعزام به اروپا در مواقع بحران برنامه‌ریزی کرده بود؛ این اقدام، گام جدیدی از سوی دولت ترامپ در راستای کاهش حمایت‌های نظامی خود از متحدان ناتو محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123022" target="_blank">📅 13:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123021">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رسانه I24 NEWS: نیروهای دفاعی اسرائیل (IDF) و فرماندهی مرکزی ارتش آمریکا (سنتکام) در حالت آماده‌باش بالا باقی مانده‌اند، در شرایطی که احتمال شکست مذاکرات میان واشنگتن و تهران و صدور دستور اقدام نظامی از سوی رئیس‌جمهور دونالد ترامپ وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123021" target="_blank">📅 13:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maLklGh-qeJeMb1i1mT0W42eUUE-ZHDvQDenCTHPquT1zRFvqh1nxKpBr2xscXfaB8SG8VpQPLx8ZFgsaiDheEfBc4eWfTdX2XafWWh-mkCsTA5wwAFfMU_Dz2byruDBmX-1yMIkdlPxwFEZ0yjx7ZOrk3a0wx444_pvn-HqDjHsJ2EeL7fmamwubzu8WJFr4Y7Sj5ydjaNMJJZ-ZeCNTvZgh44LzFW1QbCN2PSog5wiRKN2tohXA_nhAubYoAZz4TlDsfLbrOWEHTSOPewabHHKisxXYi_VL1bZhtdTQzv-zjR0VoByYLEz118M9UDQ6aC6h7CMfqbAPuI0vj93sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با تصاویر ماهواره‌ای سنتینل-۲ ناو آبی‌خاکی تریپولی آمریکا رو تو دریای عرب دیده شده
🔴
الانم با اسکورت یه ناوشکن داره حرکت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123020" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پارلمان مجارستان امروز قانونی را تصویب کرد که عضویت این کشور در دادگاه کیفری بین‌المللی را حفظ می‌کند، و بدین ترتیب تصمیم دولت سابق اوربان در سال ۲۰۲۵ برای خروج از این دادگاه را معکوس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123019" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو دیشب در جلسه کابینه: محدودیتی برای حملات در بیروت نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123018" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123017">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
امتحانات پایه‌های هفتم تا دهم به صورت غیرحضوری و از طریق سامانه جدید شاد برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123017" target="_blank">📅 13:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=kKYtw8vvpQEeUVWpXlYxWXDSLWDUl7_hFkEQook-A3o7lNzHeu6G57gLVWUUADw1rzoO1sKSpU_oZubnEVLMJNUR2CF7BjY3Cj0z4_P6Av5We4Us1GcdKVX1aY9u10unhjRe4qq-QsdLy-x6eUCgQxshfmUzdkTDeHTzRCSaFB-pS69NepD0_kEGgUQpoJBH6FWQK_BQLMxR1M2PgaV5cUwV3_-kacdttTNuIA44szL4RGEbtApEu7QiEO2ztHxIQv_x4G5d_Hjea9xwEB8FFTFtls194WPi_kO47OETSnd-GDIq_B_MLtYCN0k5EQSofRr2ZgVIQ2PEz_8DVG0VDSS7LNUmos3p6pd8vJ47ftV6149P5KukOOi0aXYJt2MzswQIW4k8Y0TBXrBxw3QwlrvflkRjg2nMcn3bTA42zr-bKRbPkq698uuAZ2sONFrCRLpOl_HxwwK-RUrRHNFzRPwYPcHNed9OCPaaKOF42O0GqLDSI5XWrBfoqQRul6XrD4nlfXsoW3ethoadgeHcuq53bByIKGpO8AUDnJZOqj1xsO5ey0uQ8ExmSgW5uTHI8OCOTPNQs3QKOnZfd5CivofBR1wdEJ2os26mBQMbBKWcaSuN7SoZSsFeSbR5NK6hcoXGnRR37mFmd0ebZ5fth3_KGLL675e5fyxHB_IzXN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=kKYtw8vvpQEeUVWpXlYxWXDSLWDUl7_hFkEQook-A3o7lNzHeu6G57gLVWUUADw1rzoO1sKSpU_oZubnEVLMJNUR2CF7BjY3Cj0z4_P6Av5We4Us1GcdKVX1aY9u10unhjRe4qq-QsdLy-x6eUCgQxshfmUzdkTDeHTzRCSaFB-pS69NepD0_kEGgUQpoJBH6FWQK_BQLMxR1M2PgaV5cUwV3_-kacdttTNuIA44szL4RGEbtApEu7QiEO2ztHxIQv_x4G5d_Hjea9xwEB8FFTFtls194WPi_kO47OETSnd-GDIq_B_MLtYCN0k5EQSofRr2ZgVIQ2PEz_8DVG0VDSS7LNUmos3p6pd8vJ47ftV6149P5KukOOi0aXYJt2MzswQIW4k8Y0TBXrBxw3QwlrvflkRjg2nMcn3bTA42zr-bKRbPkq698uuAZ2sONFrCRLpOl_HxwwK-RUrRHNFzRPwYPcHNed9OCPaaKOF42O0GqLDSI5XWrBfoqQRul6XrD4nlfXsoW3ethoadgeHcuq53bByIKGpO8AUDnJZOqj1xsO5ey0uQ8ExmSgW5uTHI8OCOTPNQs3QKOnZfd5CivofBR1wdEJ2os26mBQMbBKWcaSuN7SoZSsFeSbR5NK6hcoXGnRR37mFmd0ebZ5fth3_KGLL675e5fyxHB_IzXN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان: ان‌شاءالله این دیکتاتور به نام نتانیاهو، درسی که شایسته‌اش است را از مسلمانان جهان خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123016" target="_blank">📅 13:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=J12B5weDUUfo9bVKTC3_m_YJk-UeCdjkHlhXuRztffODp8VqKopWb1LTR50e5MmvilthapDjLeqhyM7qUf58GmML3RHhTvMO3AipXl4S283sERZny0TbdWdwr2YGw7WV1cLfBU5klza-LruksoXjGEpD-o2CVCBvGSAHMyTbp4tAsptte8hFXf0suB-MG4lsl9RCOLiBFd3jQSU8ovCmxw1I3EenGVPi-4UwmC_aCsyTwYuySY1NIjS34f9lL28a1Fq1EIVZhwuUdf4PnzGASj_nHUhTJRpbm1-h4oNzNk40l0WH9e_jnYt76UUkcLutgVEtqJUfIdZFz1H3X44cfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=J12B5weDUUfo9bVKTC3_m_YJk-UeCdjkHlhXuRztffODp8VqKopWb1LTR50e5MmvilthapDjLeqhyM7qUf58GmML3RHhTvMO3AipXl4S283sERZny0TbdWdwr2YGw7WV1cLfBU5klza-LruksoXjGEpD-o2CVCBvGSAHMyTbp4tAsptte8hFXf0suB-MG4lsl9RCOLiBFd3jQSU8ovCmxw1I3EenGVPi-4UwmC_aCsyTwYuySY1NIjS34f9lL28a1Fq1EIVZhwuUdf4PnzGASj_nHUhTJRpbm1-h4oNzNk40l0WH9e_jnYt76UUkcLutgVEtqJUfIdZFz1H3X44cfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هدف قرار گرفتن انبار تسلیحاتی پایگاه شکاری دزفول در ایام جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123015" target="_blank">📅 13:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqbwHtRwKjMkKvfS9Z4CwAZhILGy3XjrV1hpEb6R0lqgeKTHc41jk1MrK6apus0yDoSdVfv0NvJ9uEpZw2PLvIEvguvXNOiwCPXhpQkglBIG467a-Cph93doCe3iVFOWl3JbiPSaAwtAW4uIa6ZP5eXi1L9HuRRSPd6Q9AxTDh-oWNsWz_a2ox0W1TQC2_lgrgs-ryKO6hwuJMNWcTGQzYWqJVtHDCXJrQY27siPSpzlPMcx3z_s2skMc8h_W2EVf1_Uw7VL0BDUr_pW8nRpktyns2xSg9cqU7MjK2Bgf2S8T_6wYe0y9az3Y7oYZq_2KTJFWHJHpSj1mOyZNoTsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالود کارباجال، نماینده کنگره با انتشار نظرسنجی مبنی بر اینکه ۷۷٪ آمریکایی‌ها معتقدند سیاست‌های ترامپ زندگی را گران‌تر کرده نوشت:
🔴
«مردم آمریکا به‌حق از این موضوع ناراضی‌اند که قیمت خواربار، بنزین و دیگر کالاهای ضروری به دلیل جنگ غیرقانونی ترامپ سر به فلک کشیده است. این دولت خانواده‌ها را زیر فشار گذاشته بدون اینکه پایانی برای آن در چشم باشد، و جمهوری‌خواهان هم دارند اجازه می‌دهند این اتفاق بیفتد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123014" target="_blank">📅 13:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
معاون وزیر امور خارجه روسیه: ما آمادگی خود را برای انتقال اورانیوم غنی‌شده از ایران به واشنگتن اطلاع داده‌ایم و این پیشنهاد همچنان روی میز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123013" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
منبع آگاه نزدیک به تیم مذاکره کننده:
منابع بلوکه شده ایران که باید در طول مذاکرات آزاد شود، ۲۴ میلیارد دلار برآورد شده
🔴
ایران تاکید دارد که نصف این مبلغ باید با شروع اعلام یادداشت تفاهم در دسترس قرار گیرد و بقیه در طول ۶۰ روز منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123012" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Phmf5INqbxdOQ2ryl0qYlb56vKySGomuoQSsN6DxETaKNkxAAcO3BkryXcW3_xI5BC7SlZ0Tn9Xqzeq0KYJegroMHnv64WdF6-RBZAJTqqokRmhbhw4OwgrUm4P_yEKOvwoSC0iNNZLYFazcWcBK_OajuJhEVC0hWe-GdcY_LxgsUn5n4A4bkY_-TXGJZkmzd9noc_p7KOP9vGsRV6ckredScbcaSjTdoJygmZ0so9SjLVNAoIq9l4wWPNYNN5lRai3J6vKJ9vmfP_3zMqrWsrkzrF1jFWMcLDhE28dfCrnuAnO25bKJ3ulUOBOntIJUZQzV3sBIFRsk_yWcmKbE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منتسب به تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/123011" target="_blank">📅 12:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۲ عبری تهدید پهپادهای بمب‌گذاری شده خطرناک‌تر از آن است که «اسرائیل» تصور می‌کند، و راه‌حل‌های فعلی مانع فاجعه بعدی نخواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123010" target="_blank">📅 12:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است
🔴
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/123009" target="_blank">📅 12:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت امور خارجه کره جنوبی: احتمالاً یک موشک ایران اوایل این ماه یک کشتی باری کره را در تنگه هرمز هدف قرار داد.
🔴
ما سفیر ایران را احضار خواهیم کرد و خواستار اتخاذ اقدامات مسئولانه برای جلوگیری از تکرار این حمله خواهیم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123008" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یدیعوت آحارونوت: وتوی آمریکا مانع حمله ارتش اسرائیل به بیروت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123007" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123006">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4512e82014.mp4?token=HTY0E2pOtzoqjUpBtS9YWF2TpLP81LTbSctOq8EgKCaDixlWfunMRd9ERNYD9pQHh708foI2wJnT3bf64uVKZ-LBPpZp2CJuZItNM-9jqggZoxKJ_fiKoMm0USXD03daWECPMCBdxEANzfqJtEvKDTnBG1UhFx9gPsRHnvEGqSm5UYGx_tzhCWGQtYNrbaQnUO7BuIWpEuhS27P58nj5ifuboFkwdk1moSh6Hh1O1sG1MPcJkVEtw-lhLveaQpZkpA9IRdK7jVKjMG6IpJPaw8gbmTDnstWu9ztHQ-EglsSEqr1_nmslKftxhRkVfZiUldttsCwk-N8Cfkoj24loAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4512e82014.mp4?token=HTY0E2pOtzoqjUpBtS9YWF2TpLP81LTbSctOq8EgKCaDixlWfunMRd9ERNYD9pQHh708foI2wJnT3bf64uVKZ-LBPpZp2CJuZItNM-9jqggZoxKJ_fiKoMm0USXD03daWECPMCBdxEANzfqJtEvKDTnBG1UhFx9gPsRHnvEGqSm5UYGx_tzhCWGQtYNrbaQnUO7BuIWpEuhS27P58nj5ifuboFkwdk1moSh6Hh1O1sG1MPcJkVEtw-lhLveaQpZkpA9IRdK7jVKjMG6IpJPaw8gbmTDnstWu9ztHQ-EglsSEqr1_nmslKftxhRkVfZiUldttsCwk-N8Cfkoj24loAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی، شهردار نیویورک، گفت مردم در سراسر آمریکا، از شرق تا غرب کشور، هر ماه با استرس پرداخت اجاره خانه زندگی می‌کنند و نمی‌دانند می‌توانند اجاره را بپردازند یا نه
🔴
او تأکید کرد: چشم‌انداز ما شهری است که مردم نه تنها توان پرداخت اجاره، بلکه رویای خانه‌دار شدن را هم داشته باشند.
🔴
ممدانی افزود: بیشتر صحبت‌های سیاست فدرال ربطی به نگرانی واقعی مردم ندارد؛ نگرانی واقعی مقرون‌به‌صرفه کردن شهر و ساختن مسکن قابل دسترس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123006" target="_blank">📅 12:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123005">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
شبکه NBC News به نقل از معاون رئیس‌جمهور آمریکا: «من خوش‌بین هستم که ایران در هر توافقی، با عدم توسعه سلاح‌های هسته‌ای موافقت خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123005" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جی‌دی‌ونس در گفتگو با ان‌بی‌سی:
فکر می‌کنم پرسش دشوار این است که آیا ایران با سازوکار نظارتی و اجرایی‌ای موافقت می‌کند که به ما اطمینان دهد در آینده توافق را نقض نخواهند کرد یا نه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123004" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123003" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hKDrNuf4HQW4azkEQ1oh8wF5QTCMv4ys3_v_Aq5ua5sJ7a_ZjH9-zq75NdciYwAK3RKB75_MQrI0TJuTwk0z1Cp9F79MVp0sAVufTAJAjQyiUa8GO_H065tvtuJkX1so7sHAlXhj0ndQkBAnNJ-Q73QopX-oU7SApMRIlD3K6H4XG5gMPumTnsm9mJyohUG1OEC8N65TjbIqXyVoKFeJAhYdxw3tgF25kQJ5cxxrQxE0FYfNmsi8zcKiZ1s57kkKPz5Dy_4W8HeYQoG8LbIj55wl3SpzPjOjPGZYv9-5kBHgyiR1Y_RBHt2ViLXPFubcQ9ozBiseX3Z5pV5rNTyDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123002" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ارزیابی‌های اطلاعاتی حاکی از آن است که برنامه حمله به ایران از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123001" target="_blank">📅 12:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef47a108.mp4?token=Bkj8_o-uHjDNlPOV6EaIKM0WastCCN8togulg3WF66kYsuwFrGsVJ96lELlpNXUhpc0m_pszfdjeNe7gl4SH_78JvOrNG6Xh-oP7FDxu5IZFadjWtMmuxweb4jyWCCGrrAhJl4OYxCXVMEYKE-LINWAkqgGlV_fTjqZsxGkHq1HIhZ3-tpNk1SBPfrHTVj7Z_gDMbgBU72GoH5iuzgkNdg8NlcoyoZ0JU-WlVrJvucKiZmgFJxOf7rrX4jeZldxsgEarffX3DDKWczyttpJZObuA8KkLOR57jhMWhJ_4LpFrKCP_yxrnHuAE3odldynmoUbFYCSP-mBX3dE4_oucgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef47a108.mp4?token=Bkj8_o-uHjDNlPOV6EaIKM0WastCCN8togulg3WF66kYsuwFrGsVJ96lELlpNXUhpc0m_pszfdjeNe7gl4SH_78JvOrNG6Xh-oP7FDxu5IZFadjWtMmuxweb4jyWCCGrrAhJl4OYxCXVMEYKE-LINWAkqgGlV_fTjqZsxGkHq1HIhZ3-tpNk1SBPfrHTVj7Z_gDMbgBU72GoH5iuzgkNdg8NlcoyoZ0JU-WlVrJvucKiZmgFJxOf7rrX4jeZldxsgEarffX3DDKWczyttpJZObuA8KkLOR57jhMWhJ_4LpFrKCP_yxrnHuAE3odldynmoUbFYCSP-mBX3dE4_oucgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور صربستان در سفر به چین، از یک کارخانه ساخت ربات‌های انسان‌نما بازدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123000" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کره جنوبی: اعتقاد بر این است که حمله به یک کشتی کره جنوبی در تنگه هرمز در این ماه با موشک ایرانی انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/122999" target="_blank">📅 12:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
جاده چالوس بازم شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122998" target="_blank">📅 11:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ریانووستی به نقل از معاون دبیر شورای عالی امنیت ملی ایران نوشت: ایران و ایالات متحده هنوز در مورد رفع انسداد تنگه هرمز به توافق نرسیده‌اند.
🔴
ایران و عمان در حال مذاکره درباره رویه جدید عبور کشتی‌ها از تنگه هرمز هستند.
🔴
تماس‌های غیرمستقیم میان ایران و آمریکا ادامه دارد.
🔴
ذخایر اورانیوم غنی‌شده ایران در دستور کار مذاکرات نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122997" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb4HBEQ7vgwh4B8dpJz-81UT5ZPZVvRONBVprMJGQ84MF17Dm892jKBIY_yzlo0WYAESv1c_aEpdK_ZdeWnqytm6y5c_mgc6kI3uqLukZBy57_RdgRKLsPaI5lDldBviGyHyFgyn6Xsu41zEuMK8kDxYkcE2rUAdoGlcFFuS8AEmzC-0JepUQdroPfyj-YFuixPmbMpNW_F1BmuWVh3G3oxEIy0YQOIW6ZJdi7LYXBKTUqVJSu8dwxBhc-08gJyB-m_Z7qzwrHvpKhDFr6TcojYhY9fdwWHo4XBThFL0oq66mfUe2eV_3uGT40j_yX0mJi_vmFVzyvTmRjyj5ud6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یزدی‌خواه، نایب رئیس کمیسیون مجلس:
مسئولای بالا به این نتیجه رسیدن که فعلاً اینترنتو کامل باز نکنن بهتره؛
مردمم خیلی با قطع اینترنت مشکل خاصی ندارن و فقط به یه سری قشرایی که لازم داشتن، اینترنت بین‌الملل دادن.
الانم کشور تو وضعیت حساسیه، نه جنگه نه صلح؛ واسه همینم بخاطر مسائل امنیتی فعلاً قرار نیست اینترنت آزاد واسه همه وصل بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122996" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
«مردم ایران از سلول انفرادی به بند عمومی منتقل شدند.»
🤔
اینترنت جهانی برنگشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/122995" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فارس: بیش از ۲۰۰ فروند کشتی در یک هفته گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122994" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI-rUjX7I46v1zr73YAzNgN3y9Z4az7VTFK4zLr13rRicQzS3D_xLxrQQgZlAEemFMSBAvU5KpwQvsB_u0EUxFXoNVrRldoRdz5lqAsF0RPd-mvdxBlr0VyA-GWsbRyFguu7QAxbuulAA8RspOHI7Ghnotm3A34dzex-j5VYLZ54WqdsouWXH7fAfzj9UaDMcEpJaRiuIYs3IkIlAucLJRRCIg5z9yt5A-wlUH8GKM92OQDN5VDK1bVM6U9S7yNdIfolMF3cNh2BwIBs2_k28i10PnX5ECSclIPp0oRhecW0LHWh1hhbePqHRhwH1QR3sE5S5aRdS7yI_iP598Ntag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید، : مامویت سادست؛ صلح از طریق
قدرت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/122993" target="_blank">📅 11:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3d5d9df2.mp4?token=F0Yvd5KwdoHt-s4wrv96jjkeMaBBHtqUDxCTPu4ZhE9WpMT4fUCJ0p0f5esEFF07sbt0AQ7tkFX7fkmbOOQ2o6ZlTyKyw-SnqEyRlPjP1X8eOrceayptu-SDO_QSTcm6o6hExnE75twVVkzI5Tnw6D4Hu_SvyzP5gNjTdnb12pQeVW8W22UWrahkuPJN9A4NFi_sTDVQNabVK-SuaI6Z_0Ll92YRenar91XUagb5jFor6ASag65_keSFit-7d1Xgx7wuKjGPScMtb2A1yBp6ecZ0vl_7EsS30Obr1XbPyVQxVNPbRDubMe9NWRszrMAA7WoPAEe-QrKq4nkR0wPVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3d5d9df2.mp4?token=F0Yvd5KwdoHt-s4wrv96jjkeMaBBHtqUDxCTPu4ZhE9WpMT4fUCJ0p0f5esEFF07sbt0AQ7tkFX7fkmbOOQ2o6ZlTyKyw-SnqEyRlPjP1X8eOrceayptu-SDO_QSTcm6o6hExnE75twVVkzI5Tnw6D4Hu_SvyzP5gNjTdnb12pQeVW8W22UWrahkuPJN9A4NFi_sTDVQNabVK-SuaI6Z_0Ll92YRenar91XUagb5jFor6ASag65_keSFit-7d1Xgx7wuKjGPScMtb2A1yBp6ecZ0vl_7EsS30Obr1XbPyVQxVNPbRDubMe9NWRszrMAA7WoPAEe-QrKq4nkR0wPVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام یک قایق توسط ارتش آمریکا در اقیانوس آرام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/122992" target="_blank">📅 11:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIf8UxMS33SYIKJgX0Ipb3ggzWltexO1SqlRU3cCMEm9-4A8JmsHo-idnbrGadynoiidoENaPwhe9iFNIm1Wou0NiU_kktwhJx88ybbm2A-K9neDyfpOw7b0ZVfj-aNXmz_QjRAw_V_e5t-2VOvy5Q7h3qeo0Zc2h4pk9Hu3ebyBS-D0UOU0-FThnPI3-E4V60OX3wdjVe5Hid0O9iDwQYkOKD2fsaq77WyEk_jB04SxF06CiCztxMFHR-9_c_FxIPGt24a-HM3OXuHYJ4n5aqiEdSEYUQiIK7SjS-HbsgvBhjowREsi7hgWfY-iKEOu3RM7XmYrudcrak8fSOhZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع امنیتی به وال استریت ژورنال گفته‌اند که روسیه ممکن است به زودی تلاش کند در زمینه بحران با ترامپ انسجام ناتو را آزمایش کند
🔴
روسیه بزودی به یکی از کشورهای بالتیک یا جزایر سوئد و دانمارک حمله خواهد کرد
🔴
پوتین می‌خواهد فرمان یک بسیج عمومی صادر کند که برآورد این است که بسیج فقط برای جنگ در اوکراین از نظر او به منزله اعتراف به شکست تلقی خواهد شد پس قطعا حمله ایی در نزدیکی قطب شمال انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/122991" target="_blank">📅 11:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز ادعا کرد: وزارت جنگ آمریکا (پنتاگون) و شرکت اسپیس‌اِکس بر سر هزینه اجرای طرحی برای فراهم‌سازی دسترسی مستقیم کاربران ایرانی به اینترنت ماهواره‌ای استارلینک، بدون نیاز به تجهیزات زمینی، دچار اختلاف شده‌اند ولذا این پروژه متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/122990" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e84f6895e.mp4?token=Af1UjIuD5SfEXyriCghU1MgHnMlh8aVE9LubEx-BPEzRx1O_WHzaRgT88FyDpNWO9VVFmzgqY9i670RClknb2Kjrd9b0gOzD2ro7dhTkPkZ2ICOSW-GRSZUIyLCzgXe8_nRa7OrbRBV_Zqa3AiCm0YtmCcZ7T7Qq-UtJnwuxybYj4E-XzSd2zvxiuFr9Rm7tiBQE_u3w7YSKrWojG56iVBzF-jm0Od6OCxrmngaJ6XeqQo76755-XyefNAWsIRZHfNMUmvRQ0pDuoK6e-uqFASvUEhaQWwyt8b3WcVtmCqTio9oqpcFx5psiBOgGr2ZdyA7jDm3RTV_T-btjjstTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e84f6895e.mp4?token=Af1UjIuD5SfEXyriCghU1MgHnMlh8aVE9LubEx-BPEzRx1O_WHzaRgT88FyDpNWO9VVFmzgqY9i670RClknb2Kjrd9b0gOzD2ro7dhTkPkZ2ICOSW-GRSZUIyLCzgXe8_nRa7OrbRBV_Zqa3AiCm0YtmCcZ7T7Qq-UtJnwuxybYj4E-XzSd2zvxiuFr9Rm7tiBQE_u3w7YSKrWojG56iVBzF-jm0Od6OCxrmngaJ6XeqQo76755-XyefNAWsIRZHfNMUmvRQ0pDuoK6e-uqFASvUEhaQWwyt8b3WcVtmCqTio9oqpcFx5psiBOgGr2ZdyA7jDm3RTV_T-btjjstTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که محمد عوده و فرماندهان شاخه نظامی حماس ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/122989" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
در حالی که به‌روزرسانی فوری نرم‌افزارها پس از بازگشت اینترنت بین‌الملل به‌عنوان یک ضرورت امنیتی اعلام شده، شماری از کاربران از عدم امکان اتصال به گوگل‌پلی و مشکل در دریافت آپدیت اپلیکیشن‌ها خبر داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/122988" target="_blank">📅 11:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یک مقام سپاه می‌گوید احتمال جنگ مجدد با ایالات متحده کم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122987" target="_blank">📅 11:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS2sVVjtS3JSqAyQFqyQN14pJ_B4_p7KOsTvmReCYIORAqmEOzoM4BZ4ZM5XjpU9lwlQbXh2GWDvtX-g_wFFU_LgN6fIHL5vI6a9Lv56Cw18pAuCM7O-fzaeC6mZP8XX5qJmn5fLXFe4tJWBAJWdIMoVSzg1GoGzu55nb6kOg8A6woppJmM_CAilb9jImAuU089ZZ2M6BeAgGtqAKbvFpZSb9ntJcmiRfAQrDE2ud-4mNhe3TCQKfZ_qM5JK5Tnn9No-MzwlDzlAB__wIzmFZB3yIWRYmRH1SW7ajXzRLLdc-fsmdNaycjjdFigxt4PkDGsc6oWhuwVZHXFkEt7MSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از موافقت سپاه ، نفتکش متعلق به شرکت کاسکو، هوا لین وان، اکنون از تنگه هرمز عبور می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122986" target="_blank">📅 11:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8RrgB0udzvdvzFmrTv65UJdxAkCrA0glVCx53xC5mViCleUIwNhPidOtJgWsfJ1lz_rwG9D_G_1uknrAyUWTMGdv63ttZvjWFRi5fEsp4rYJjtgVwY9cP6PhfYZrENaoYZFBps2PbHcWlKULcFKvTnF06sCcoaLRa6oVsGi1npbmOge2xYWaTfbQsFhTnoq0NCRS0kLmD5zQsMGrVeXjxWjyWqCrRRVQGPjVWETMFRegJ7eQRs6_CgQpr1gx0ChKedxJBo04ZvjrCgIxSPucRtDc-FvouKDjdaSH3A8nWgzytSEdfArm8HCfm3-3lWPz9obuVtd_1LqffiHkO0gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۷.۱۷ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/122985" target="_blank">📅 11:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رئیس اتحادیه صنف خواربارفروشان تهران: پاک کردن قیمت روی کالا تخلف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/122984" target="_blank">📅 11:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122982">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز: پاکستان از میانجیگری عقب‌نشینی می‌کند در حالی که قطر به مرکز اصلی بین تهران و واشنگتن تبدیل می‌شود و تمرکز بر دارایی‌های مسدود شده ایران در دوحه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122982" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Q_W_kVpJRbTYDBeKXG6aCltR3jZOfxQFFtEAvBV_TFfS5GtRsmVtjQr9fR5Uy6ADTshHKOaLo-TMMoXX6En05TfGOoWIHad-5-iCwlvSGIaXi30Y_zxre_EaXglOQwZ3o8yOTvG7PumtBqOj0L5t3baYmvxvXWC1YiQ52Bfz0iaNnEVMgml3FT03w4BFsLEbqPXs_hnVuRwvdnOh66ZGUgW6gkXwQ1qEzCd5KEEQSip3AhSH4tlD-kl42_5O0lnSm-X8Tp00iEqRfG4uvRvd0wnOPxizOKaC3shFTUjP4amHZLCskcD4QTYY1QBMMj3Yi3V5LdqpX6CdMtG5yJSlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا الفت‌نسب، رییس اتحادیه کسب‌وکارهای اینترنتی ایران: اینترنت فقط چند اپلیکیشن نیست؛ زیرساخت کار، زندگی و امید میلیون‌ها نفر است.
🔴
ایستادگی در برابر فشارها برای
باز نگه داشتن ‎اینترنت، دفاع از اقتصاد مردم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/122981" target="_blank">📅 10:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktbKvhT6pTZLltVRUMr2Ny0DoGyOnZqcChcNlM9JVtEULFC8r2AxUUQMwlookwiCcE5t9s0_kP8WXZXcEruqZY3WVSdIM9LfVMqQdJXsRuGh9cwP5zN6yUWl9VPyqYH0uHFEVmxP_IBUL3TgXA8H8jI-0CGCKSxsjhIwnm57LrM0FF0ySj4-0vuqAMnZuihv9Z-h6ppphD7zvC9bdCIwScnSwd-pW5EAyJ_5vNR2hsxoJCscJqicPxg0zUH4JJDwcW86wK4wXD5qK5jFCpoAFZPJ2bKaPxmuRvJ0fuZvv2nOOXmAJvA88fLSD6LWIFGcXsviK6DqtM-dcimECK69eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان بی سی نیوز:  بازارهای اروپایی با بازگشایی مختلط مواجه می‌شوند، در حالی که معامله‌گران آتش‌بسِ شکننده میان ایالات متحده و ایران را ارزیابی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122980" target="_blank">📅 10:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رسانه‌های لبنانی گزارش می‌دهند که صدای انفجارهایی که چندی پیش شنیده شد، بوم صوتی بود!
🔴
برخی گزارش‌های رسانه‌ها همچنین ادعا می‌کنند که در زمان انفجارها هیچ پروازی بر فراز پایتخت وجود نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122979" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شماری از کاربران پس از بازگشت اینترنت بین‌الملل، از عدم امکان اتصال به گوگل‌پلی و مشکل در به‌روزرسانی اپلیکیشن‌ها خبر داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/122978" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bb329e51.mp4?token=TN48BRTLpXpYJ-Zn9j3YGmRV7MMK88_h_VY6CMqiZxd9mJR-Ihv9RzUEJjSSmdW_teHrX7OXkB_OPA4MC6GDTX_eu74mXTzJaeAJ3C7SwqLZCLmEiZNk9bw3bekYipZJP45UtWH0Fu-OSzc400Onky2DgoMp5ZBU2AQfOUcYu1zrRCheaVrOIIJ6Kyq4SXQh0VArbUAL5JdBzGdjZzUFw3Py3T5ckCxc1reMkBkJ9SQTEQkF0J7wTsTITG-67jr6F7Lj4yIDMbV3f4rj89u_PenXQZ1wYYUYmfbuP57BZ5xPfBzt_6nbMlN4MvxJZWv9_gpg-VgOdTKvo7DRlw7DCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bb329e51.mp4?token=TN48BRTLpXpYJ-Zn9j3YGmRV7MMK88_h_VY6CMqiZxd9mJR-Ihv9RzUEJjSSmdW_teHrX7OXkB_OPA4MC6GDTX_eu74mXTzJaeAJ3C7SwqLZCLmEiZNk9bw3bekYipZJP45UtWH0Fu-OSzc400Onky2DgoMp5ZBU2AQfOUcYu1zrRCheaVrOIIJ6Kyq4SXQh0VArbUAL5JdBzGdjZzUFw3Py3T5ckCxc1reMkBkJ9SQTEQkF0J7wTsTITG-67jr6F7Lj4yIDMbV3f4rj89u_PenXQZ1wYYUYmfbuP57BZ5xPfBzt_6nbMlN4MvxJZWv9_gpg-VgOdTKvo7DRlw7DCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:جمهوری اسلامی درخواست ۲۴ میلیارد دلار برای هر توافقی با آمریکا کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/122977" target="_blank">📅 10:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مجلس سوئد ازدواج فامیلی رو ممنوع کرد؛
🔴
طبق این مصوبه، از اول ژوئیه 2026 دیگه ازدواج بین بچه‌های "عمو، دایی، عمه و خاله" تو سوئد ممنوعه.
🔴
دلیلشم جلوگیری از خشونت‌های ناموسی، فشار خانوادگی و ازدواج‌های اجباری اعلام شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122976" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
بلومبرگ: خانوارهای بریتانیایی شاهد بیشترین افزایش هزینه‌های انرژی از سال ۲۰۲۳ خواهند بود، زیرا جنگ در ایران هزینه‌های عمده‌فروشی گاز و برق را افزایش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122975" target="_blank">📅 10:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs3Mb1fLbgq16f7dwT0cuzJx8krHCrPhOsi5t8wBf2hnxPFgJEIU6B3TpuXIy7uIHoCXUr573w86z-LRY3482Kp_pANn-yasB09lc0m7QgNDsxO4Ihzo-93fgn3aeU6W5omLKHSrT8yCiIFLbd1zQEjw2FJoZmow3Su5EL9EKWWnvsifb43trBwGXfpclLyzubQFxqzXjnrEFHiBZZ29J0uc4wYtGQKs1c_ujeIcuUHUzBmfDmBYbV66_YZSjHPhaZOMRVBIzmH0ChxSBH1EoGCAlyodzzvb5ViwVDAu3J9wesu-y7PxVaYJ-e5Wc_VZ4mj70gp9og6LdxmpZGafWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: ایران ۱۰ ملوان هندی را پس از رایزنیهای دیپلماتیک آزاد کرد!
🔴
مقامات کشتیرانی هند اعلام کرده اند که ۱۰ ملوان هندی ساکن در یک نفتکش که از ژوئیه ۲۰۲۵ در ایران بازداشت شده بود، پس از «رایزنی دیپلماتیک مستمر» آزاد شده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122974" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تهدید بمب‌گذاران انتحاری خطرناک‌تر از آن است که اسرائیل تصور می‌کند و راه‌حل‌های فعلی مانع فاجعه بعدی نخواهند شد، طبق گزارش کانال ۱۲ عبری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/122973" target="_blank">📅 10:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c3bd49e7.mp4?token=mg-O2ZoIoNhjr3XKq3wA2iNzPx1bZ08k7JcE285e24k8ywGbqLO7lQDQW_qa9ZBVs4QRnXb-IjO_vmzi95po4c43Pxe3g4twr03mlD1_CNYGSBa-L-WYxVMwOVPLkv8eae4ZD77jZduzZygJsPFm0E5O9CY_MTGq4pGzRwpGUq1ix1Rx45EEaXOGCjUDoPZxptDDsQzweNBWtZrCKa_cxF0RqZl0Xv2hKDJPYc7IR6qJ4bjigZvbVBOKtXWL_OELXv9pdRz3okoSWeUUB1QVFJR4bsJZ4lnfxXMeSiPXeK0wq8jjKDsSXppXTFUUXbbfuhaZOVLLE1p86-oNHLhtW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c3bd49e7.mp4?token=mg-O2ZoIoNhjr3XKq3wA2iNzPx1bZ08k7JcE285e24k8ywGbqLO7lQDQW_qa9ZBVs4QRnXb-IjO_vmzi95po4c43Pxe3g4twr03mlD1_CNYGSBa-L-WYxVMwOVPLkv8eae4ZD77jZduzZygJsPFm0E5O9CY_MTGq4pGzRwpGUq1ix1Rx45EEaXOGCjUDoPZxptDDsQzweNBWtZrCKa_cxF0RqZl0Xv2hKDJPYc7IR6qJ4bjigZvbVBOKtXWL_OELXv9pdRz3okoSWeUUB1QVFJR4bsJZ4lnfxXMeSiPXeK0wq8jjKDsSXppXTFUUXbbfuhaZOVLLE1p86-oNHLhtW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه کوبا: روبیو دروغ می‌گوید؛ او طراح اصلی محاصره کوباست
🔴
وزیر خارجه کوبا در پاسخ به ادعای مارکو روبیو، وزیر امور خارجه آمریکا، مبنی بر اینکه علت رنج مردم کوبا، غارت منابع این کشور توسط «رژیم کوبا» است، گفت: روبیو یکی از طراحان اصلی تشدید محاصره علیه کوبا در همه زمینه‌هاست.
🔴
وزیر خارجه کوبا تأکید کرد: او مدام دروغ می‌گوید و قصد دارد افکار عمومی آمریکا و جهان را فریب دهد. من بارها از او شنیده‌ام که می‌گوید محاصره وجود ندارد، در حالی که خودش طراح اصلی آن است.
🔴
وی افزود: روبیو در کوبا به دنیا نیامده، کوبا را نمی‌شناسد و هیچ چیز از کوبا نمی‌داند. این اظهارات به عنوان اقدامی تأسف‌بار به درک مردم کوبا از وزیر خارجه آمریکا اضافه شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122972" target="_blank">📅 09:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فایننشیال تایمز
:
صندوق رسمی «هیئت صلح» ترامپ، علی‌رغم وعده‌های کلان برای بازسازی غزه، یک ریال هم پول ندارد و هیچ پروژه بازسازی‌ای آغاز نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/122971" target="_blank">📅 09:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نخست‌وزیر قطر در تماس‌های جداگانه با مقامات عربستان، اردن، مصر و امارات، راه‌های هماهنگی منطقه‌ای برای پشتیبانی از میانجی‌گری پاکستان میان تهران و واشنگتن را بررسی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/122970" target="_blank">📅 09:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122969" target="_blank">📅 09:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
هاآرتص: عربستان سعودی و قطر نسبت به درخواست ترامپ برای پیوستن به توافق‌های ابراهیم محتاط هستند؛ این موضوع نیازمند تعهد به تشکیل دولت فلسطین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122968" target="_blank">📅 09:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در مذاکرات با ایالات متحده، ایران می‌خواهد کنترل بخشی از حدود ۱۰۰ میلیارد دلار دارایی‌های مسدودشده توسط غرب را دوباره به دست بگیرد و همچنین به بازارهای جهانی نفت دسترسی پیدا کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/122967" target="_blank">📅 09:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
طی روز‌های اخیر حدود ۱۰۰ اداره و بانک به‌دلیل رعایت نکردن الگوی مصرف، مشمول محدودیت برق شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/122966" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc255b611f.mp4?token=DfEM3EdM4Wyb9rmgQwLQmSfnpI39HujLG0fehokjkKpekEnW2gL0c1xXGSq4X1v2X35bDzudtKojpBngtHDKPdXH9sLfI2rdvM3Rmz0nbUE75TsakxDwde8a-d7tF9qr5Nt-4h8I8JyP1yEmXQHd7qXc_AHrHRPpjTEJH21E3M9I9zShTWJDVvCUrWnZg6IYpnqtr_j9q9LKY0fVFmy9dcCqiEwohG7YCzoSCf0qV9pPnJ3SFiaNbE-uLwiBrQvck6HQ-fdZPZt3hn0whbpzErybFgFiiaRQyGrNCRF5Lrad6swbFiFtrhRHTfAvv4k24EO8V8OVtVDs9_DhoTM9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار مخزن مواد شیمیایی در ایالت واشنگتن
🔴
در پی وقوع حادثه‌ای صنعتی در ایالت واشنگتن آمریکا، دست‌کم 1 نفر جان باخت و 9 کارگر دیگر همچنان مفقود هستند.
🔴
این حادثه چهارشنبه در یک کارخانه تولید کاغذ و بسته‌بندی رخ داد و نگرانی‌هایی درباره نشت مواد خطرناک شیمیایی به وجود آورده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/122965" target="_blank">📅 08:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkJ3HDagOlD_1LQsCbztIFv8Ds3JrGyz44t2CzDZGXZN2jKz9Z2vXGGX5LyxneIylodfCE6_V_rx2egO28BisIyGA6YG9Afagne5jZQmUZiGHsvLcx-NhvWz3p499cJNFxkA2tCv77o0RUseQcm_FUGB07XAe0ndMpqUfG3BJqBkya5xBiFOnr0sAjznUY7bMweCBgKHL5F6E5GxMaWhHwWDiOfJXjFGgqw3eH-4zlrk8JOLsJC_zX9v4754SEM-Jgfhq1NNGzCLLds4d8jwF7f_mfxneeCpnV6JrgbWjmkNxmK0AWi1-sI5VIvFW7Desi514ho5JCwcpVKMOsHiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی پایگاه هوایی تگانرونگ در روسیه را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122964" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edOqvTxF68GIS2tdLa5nfZyxC8Hd3ZnnnyiXu6ke8eXnxycd2MtKzkMAB2qgAw8MutN8ah-i2q0eISmRd-4-Apgpr7j_geIvtpy91sQL3XyuyvXHGFxJBZuGMDuM5PbIFdAEZN9lKpZWCV232mXFL6ZFEOjiQIvf6etbhGWDD_i67qlY4chW68ZeqJZJBkz5qNskkR15Jl87BbKFOoyD2LaCn3bBxCAQ3QSM5BbUEMVOmgxYCw-kStPed7JAEcIBjKWB2tMJZgSY66IdFZdmjCptuoesSRO2I42Au6i-8zEu4QI5XJF1WpHUuKMMFCvBiMET5hRPLGycT0QYIL71Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر روز رویترز از کشتی های پهلو گرفته در نزدیکی تنگه هرمز، سمت ساحل عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/122963" target="_blank">📅 08:54 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
