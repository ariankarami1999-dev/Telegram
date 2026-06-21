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
<img src="https://cdn4.telesco.pe/file/Mqp4b6MVJutlKUoaHv3Sd5VFu9uSE30R2iJsqVub6gWTOZ42nClqmjnCKG-ohFdRxFLL75yY2PEIhHyVtGAugG9fBrP3id2j-i2libHd3TWahGb5uJKacBODhbAgcl0NM0PyT8_UEgmR_jva7nw8_-4HxcaO1R9U2mlJaFEDdXeeZ8H2Fc0BKE3pNEuPhZD7LlcFvtDz9_qDJX2T0_-8JYfHY6dBcrR9oGW-ia9t4oL1hzOfsTiLlZBF4__POWilEeGmvxXhCGIFMLgFM4JutPqX5NW5WwVRtiRX2z_PM49yxhY5ucBD0O8MGPPAnaU5GhoEU5RN1dQHySaR8FyHzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-129499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/129499" target="_blank">📅 10:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1EuP3nqA2bZEpZMgjoQfquMO1d-wxnFNqKFZWHM9eb6tGelJAuR2XKNrwIBW3-BEgZVl_amx2_GMhsej6_mZ4AYwzWfYrgIcMkJv7KTt75tdDnZhI0dGfm9KnyZ486Y7l2IfUooGx-APk-TEV_nogUHbOilcpElt6IzIOvUGs6itOOQbHLzGyZ2aTieTVCEuogAe3XvQBPSMHeMNnkLhXVAweRUWZg1RpymcQxafZ0YHDYMXiLO7_vOni_9sgU6vbxxb6sU-SMwefemVqjGVJLn7Hn88cvB9I5tbRAakjOZtGFElYeu9imL2PPcVlVMJt7tll7ww7EGz7u1rxQ4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHqbxv99Kgst0z_NDRO75nzMj8RScq3ACh8sK9Ja9EWmUo7aW-41Yn7_vA7LcfasaO3UagkwYCBt5rquUwJGAXEOUQKELLfc3hh8WQGe3Ucx7gEmSPyB2N73eLaPyKVLfl1jfA-USDPNdAfyRtZpxwPNcdRyxNXuhPopluNjH4yXstK9Lo8a0fCjyvJ37VIT7jOBw74uHkOVhgCzIpyYT9p7UCpbKMWC1UWJIpvR-Ss3t8mVcMEecUpDSNvJh-QhHsgYr8z1ZpvOX7JasIZ2hsw8roD7pHlsKGm-xkiBydx6yc3xK6fDoDqvj3TO1FqD5JW2jTqwcsx_btlzlQBI9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلاره در ایران ۴۳ میلیارد تومان ، حتی اگر دلار رو ۱۸۰ هزار تومان درنظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/alonews/129497" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6knQXqsG7tV8jVjMiyHDRs2PI_C0eO9lhE1MfCxrTflUbkKipH10DcQsdeB9G-PGdnXjAEYQLiiTSSZJ_sFJMORAuUWPE34j59qe6_WwWkye4yJtxihUw53hCHLd_QDgpNxjpvFmJr9rCJg7m_LqeJmIxW5VpzhY8BhCoUfG7cSJFMrFt3Oleg2Q9WaF0njDo6KKTHuTGCBAWSIHKwXh_F7kdJmVIIJ1Y0Weoexokj9N0Prt_dUIP4W-9lo2OhruXLypX0Dzy7bdGrgZrG9BoskeKTGRVYDpW5b02WpmOQVeUYKbc0W3AVgJJuqnitgh1GVBmeMk9A3LtxfIYjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrxjDcBIWg_oq54VEmT9qNVlWDw49NyH6kdL2mjH20_dO346COTywOWzPgTuZklSeUaB7TBJjyABPWRGluRexDsRo8bOVWZvSPbsgyr9bBxQwbaPdWHfCyqKxYvRbDGYdOe2wDczhiRUkN-v7sa-IssGB_ELqHenEQ1OEBHdbvGGsS0MBDAHaPcYK_AKiq28Og6Oy8XHdp_zQUJ85RSxBWPzQcN4XqMlfUXtxmZMgPc28ITo_XZm6gy5MRVk8lURu9p3GwdrKRf0d4WwGIm_2y2B4gPLxeWT_w73UT9BocPNtZktRkFd4769xCCJT3iDkCPxcGg-AgDEIMfef-fljg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ورود هیأت ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/129495" target="_blank">📅 10:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/129494" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: شاید اگر توافق با ایران حاصل نشود، برای عبور از تنگه هرمز تعرفه وضع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/129493" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw4e8aOt4y63Ol5cYdd2JM5wGsOou8hyn0mFEZd01yJF68zMWH6dBT6BoekIK5QTz2lH4bVWBkJLRGA6x0jMyuQ7W5ueteyIMK1B2jhGVMrf0iUabgP-WzTe_bkBXWoIvywlrIrmDSRFb3hMPAgkL6Y_kAplPzOWlUaZ2LjQKU8f9VE6PYKk34LWE5jpGATyDTX8ZL_mFxQTlsX2q0CdjLDySfxe-5y1SKtfg0QOYA96rik4N3i-SAIkOqAdp2iwP8NkuhzAD9e8stQjoTsLhVtOjb4wYYkT0omcy1BEasvVAGl4RN1e6CaDX_FhwiDxapSqK1WuU752qtL7cfh2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/129492" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الجزیره: شکاف در روابط ترامپ و نتانیاهو به اوج خود رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/129491" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس : ظهر امروز به وقت محلی قرار‌است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129490" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک دیپلمات شرکت کننده در مذاکرات سوئیس: ادغام پرونده آتش‌بس لبنان در مذاکره با ایران، یک تحول راهبردی برای دولت ترامپ به شمار می‌رود
🔴
دولت آمریکا از راهبرد جدا نگه داشتن منازعات مختلف در خاورمیانه، دست کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/129489" target="_blank">📅 10:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Y7_AD99Xqg5AWTwFwd2J5mo7MKvaMCtXNq1d9CQpJAZh0yIMBM7Wr7iwadhmVumadewmVwi1hdvlPoN2OiCygOj5k5NOf_jYg8oUQPqIXfTvJ0sjDAsE0gubCYfZEdfixAMv2aoz_C4ki-uU8pyi9F43x7IlP3YlrTmJXeAfc2IvIKvPQaxtcqq-_cb8plvjV054MG_z7S4BcDcQ0gF4AP2plLvLtTJjudRFTrO51vY0Y17JAh0h-4SDAdt04RJsuh0t8YlstQG0mcLAG088cxLkKPuyRK1lqMw5l7YJy4XnnTSiVfhRPAR926c_aT8apQXWPH3BJXHY3hhTaO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترمینال سوخت کرچ که توسط روسیه اشغال شده بود، صبح امروز با حملات پهپادی اوکراین منهدم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/129488" target="_blank">📅 10:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/129487" target="_blank">📅 09:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/129486" target="_blank">📅 09:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: پرونده لبنان نخستین موضوع در نشست اضطراری خواهد بود که به مذاکرات سوئیس افزوده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/129485" target="_blank">📅 09:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره:
🔴
خو فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/129484" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گزارش روزنامه بریتانیایی "آبزرور"، نخست‌وزیر بریتانیا، کی‌یر استارمر، انتظار می‌رود دوشنبه آینده از سمت خود استعفا دهد و قصد کناره‌گیری دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/129483" target="_blank">📅 09:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0PT_2kU5awM62vadW-x8m51hhu_tfCdLD5oi2ae6K6PHBMxSN9QRZ6kv5Pi9NgTvlOh2_cu85l8tJRU2_FiG5cta4RNbVCcq0THdYz7NCH-MNj0Rn0phU5svh8lEa2PVmyEm1SrKKK3HhkcsLzUpLgY8SM3gAtVky1oF_AYnmiaXmUBLze-RIPKqDQChSH_AgkXi1IGDw4i0-gkrgujVt25HM_LP1LxNbl31Tiwi34_91TQjED0uHadGHiX2F1GYT0G6jcX1hCrISo3w9G9uSFsBSbt0qOh8Vf9421HBdSgah6ddHMPouQ8eOuuHvtRQXTtDuqjx2v2aZCHwpN7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه‌نویی با انتشار این تصویر به شایعات درمورد ساعتش خاتمه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129482" target="_blank">📅 09:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: آمریکا پیشنهاد داد، ایران تنها برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/129481" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات:
یک نشست اضطراری درباره لبنان به مذاکرات ایران و آمریکا در سوئیس اضافه شده؛ این موضوع نخستین دستور کاری است که مورد بررسی قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/129480" target="_blank">📅 09:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJabPvb1pFkiWwqyp0KF0cfFVTbhBmwCSGoPirIxi5K70ymtml0DbffUw7yqtz7e8Mm1QkRXFLIpSZaYYOLoy0FjMuNVZUgSWyhqoVrS8-KGRyKF8lPBAQFKFborpLzBL1Vlv-yo2CUHCv51FycRlP9t56SJTNxr1L1-tOn0KfAJbckbRMWs36uu9xDnVhgawrnvrbgXqVXyeptVeRS46RXqb0cPG0BrqviXR5HdZ-UhfyqY1j6vydmWnxzRroVzF03QYbXsM95Uj-Wbvt2iaBic9bNpqxtUQXa9sB-zWrq1_AsCoOuixTMxLpabeG10TaKagO14SdTkbUTDgqjBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/129479" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رادیوی اسرائیل: کشته شدن ۶ سرباز از جمله یک افسر ارشد و مجروح شدن بیش از ۲۰ نفر در حملات حزب الله در لبنان از پنجشنبه گذشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/129478" target="_blank">📅 08:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار الحدث: ونس، معاون رئیس‌جمهور آمریکا برای شرکت در مذاکرات با ایران وارد سوئیس شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/129477" target="_blank">📅 08:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I93FA1-IW-RrWQWA2luuBnnM633xHp-H3EnoQaN5aazk0WFLg7i-8p9_1ICOUe9yGcpoTvZHZCmmz4c71H7dJukJO1fBDCXu5tOO1IRzhjsxtQhzHDAGRi1_6S94QYATDX3j3W4esiQSwy3ZdJt1oGiQdgU69_nm_Y0m-82D9fbECL-3WBBzAAeiehVBUkAfEQpZiDl52XMLvzMnSaAPgUw4RdF9SsJfrdRNS03LiDlysw3zeLQdEPDWkpH9bpQ7b5DLAeV-jEBZMpoZ9SLT5YZM7UEdOfkznCXZcJtbggNLg6Tix7f8xHHl8vbTxU-YUs775x6yMQe4umLvEbHDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه، با انتشار تصویری اعلام کرد که یک جنگنده پنهان‌کار F-35 نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک تانکر سوخت‌رسان «کی‌سی-۱۳۵ استراتوتانکر» (KC-135 Stratotanker) سوخت‌گیری کرده است. سنتکام تاکید کرد که نیروهای آمریکایی به گشت‌زنی‌های مداوم خود در آسمان منطقه ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/129476" target="_blank">📅 08:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند ساعت پیش عباس خوش قدم (سید عباس عراقچی) رسید زوریخِ سوئیس، الانم این شهر طوفان شدیدی شده و کلی درخت افتاده روی مردم و مصدوم زیاد داشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/129475" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129474">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=q6hB-jnR5aiJrF5ZPHl_2keYsWEASDXXBKb6aEBVAv-RUFvER0iXR2NRIxrvp_7fWxjUGbpvJDR8Gp2MVT629mSSUTJ9kpuphTFJ18nc4WLbIQuGyhkH3KMiR4KbF19kd0GRmjkk8HqU_7bve-zWoD19y2cwgIacDiJyyaVYZiWXaXSV5DuwTzIRnCI8lNFjAAfZo38YTcwee2ehG69TZXH1_NU5ywIKSbPXu9aZWq-jbqvu2N5YkChqMhcVhVC7WLxciGLoteoLGpgglmIDaHnvyDjYNKdjpRbm6kmFmqIHrb_acdJbPm5xQpOgLwVcObaLIrDIKkcNCC9jCyiZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=q6hB-jnR5aiJrF5ZPHl_2keYsWEASDXXBKb6aEBVAv-RUFvER0iXR2NRIxrvp_7fWxjUGbpvJDR8Gp2MVT629mSSUTJ9kpuphTFJ18nc4WLbIQuGyhkH3KMiR4KbF19kd0GRmjkk8HqU_7bve-zWoD19y2cwgIacDiJyyaVYZiWXaXSV5DuwTzIRnCI8lNFjAAfZo38YTcwee2ehG69TZXH1_NU5ywIKSbPXu9aZWq-jbqvu2N5YkChqMhcVhVC7WLxciGLoteoLGpgglmIDaHnvyDjYNKdjpRbm6kmFmqIHrb_acdJbPm5xQpOgLwVcObaLIrDIKkcNCC9jCyiZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تیلیوزیون: باید فرودگاه مهرآباد رو ببندیم تا هی نرن مذاکره کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/129474" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129473">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مراد ویسی: نباید به ترامپ دل میبستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/129473" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avEnkuKAXFLr278EaBtJbjbQylujxFeSnFsk_3i-a_CSQfeRdSoCitRgZuKYbXyK_wxulXsLemtiRnqyFEQPJZYospTxxmr8twVsYux1NChyJSaDMZe-Plvkrp24wsWBjb5cNsA7vdZKftDBBnBMsRnzxrTZMkPxSp44gW6cTWicSp5ol1MRdhIOlAVioqR0lTLler7pBhwviZseONRCq70-iMfCDhtq3jMEEpTX-Z-QtPAHTVglsX-nDXxKF8NSwQao6hXNdaGXIBQG0Vai_sMJ3k90lh3oxsQzvpBV73fVIbO7grAhJcdCOWw92x9NgfCpC_MSPkJ8sFwmJ_4JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPaig20EHcGRCI9oMh_qucYtwnKZTXl6dTPTNflQbo_2ZxpZZUaN0Y2aW0DBJfssg_ZVH1UaXxHDpLYw_n7RI0rcF9VcS5BMoJpFzRKqGq-fHMKVirvL9qXfDmP7_PUS_NIWjjgEWaMC913XUoj4gCckQfjzzWtwu-dZY936aB0qluI1MebHgDgQ7_7VrW38qzIWCH3wSdGTzoLB6YKukhZiMfg-5Em_65yYz7mlw3papD50rDOF7oTwbdWbCZrw-Tt2k_vJ9_k1gc-TExsEqIx6H2O1sjTt5nvv4WjpZ2Te25ZlKeXN6LczYsrioQzqSuSAJxoLpV8xqUmaB9f1ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی با پرچم استقلال تو استادیوم داره بازی آلمان - ساحل عاج رو نگاه میکنه!
@AloSport</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/129471" target="_blank">📅 01:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=q9fKgTxPh6gSlnD3NEUA6kNE4KyeF4ybOKKHo9U-8s0Pof940PDkHF7H-gVEJttx0hJ4_5iTm3MtlosDyKrb8PGWUJ7n_wkBU_c6Y03FklDYMJmyMHgz9qhYTNj0UB52vJMWFc6PZtZWYbXeIGob3DCRNMHD1K9TT9OFh-AlWU7HAB7tyZagpS7hVxigHpDjoYvUC7IKjHyhp01gwCXFJ25KImJ7HjJ9fCQTirFH2LAd23TQ7w5oxnbbwXH4W6HxFoo0y1F_N1fF2VbsyySv06yZElz09DUmA56wOBBrPZoVm6Qdqa1EQ8081_UANXmhH6vo0bRYky1qN_zyEKcWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=q9fKgTxPh6gSlnD3NEUA6kNE4KyeF4ybOKKHo9U-8s0Pof940PDkHF7H-gVEJttx0hJ4_5iTm3MtlosDyKrb8PGWUJ7n_wkBU_c6Y03FklDYMJmyMHgz9qhYTNj0UB52vJMWFc6PZtZWYbXeIGob3DCRNMHD1K9TT9OFh-AlWU7HAB7tyZagpS7hVxigHpDjoYvUC7IKjHyhp01gwCXFJ25KImJ7HjJ9fCQTirFH2LAd23TQ7w5oxnbbwXH4W6HxFoo0y1F_N1fF2VbsyySv06yZElz09DUmA56wOBBrPZoVm6Qdqa1EQ8081_UANXmhH6vo0bRYky1qN_zyEKcWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشخوری عجیب ایرانخودرو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/129470" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0SknVvH3uCDbhCVu-wYJOuu1JRGAtEXRBsExkyqAFgR-gdE2rHoTZZPXbZJgwJGu5GFqOCKtH1KB1pdo2oHgDbVKfivDBXClAsudS7Ddjk2VukAZmnZCdezs7tj9CPnB_lnBXngzEj7ySas2dQfwr3h4FazNw_k614RZ7R_cqhr8ZNbd8JXMfacoSOa6P0lTVHGG-OLm0cS_HBO5TF_xvkMzOD0VfejMgeJMo0Xm5oO7ergKPQwL6aD6-kTtc20OWO4EvWPLto7FZLTUxILw3cWjHDDsw-cDNNeAEjRpBYB6bOMb8bBLLPsbquBMVcp32pW_-C1vu97rZgWZQboOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : آقای نبویان اشتباهی نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/129469" target="_blank">📅 00:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
علی زینی‌وند ، سخنگوی وزارت کشور :
به همه کسایی که توی مراسم تشییع و تدفین علی خامنه‌ای شرکت کنن بیمه رایگان تعلق میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/129468" target="_blank">📅 00:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCtxSvUtXBMCU3Evgpq6cd0b3c1OXpV1vEc4ygeKvllTCHw8Jkdgfg_nCzIh5RXNKxIXEZmmj-O7z0zCr5DEgvfEbJ3J1g1cIqrTOUmXykHeUhU8PsMGSKuDNIRz463KZqmIqAu6Y9GTqaaKp8R4GFlT48GK3ruUchdRvx2Z9Jde9z0M2JzAB2RwK_ga31MP6XekPh0RP9e14Dj1TjM9UnOU5kUuB8bnprV5-jhYV3pAB_vtpOyuD3veswPMAVKGAZ88qpM8c8cG8Hi2dQ-L7DTj9JccBVOsbUhvZrRKY9ZvZfmXjwWkWbsPkNg3xVWJ1nZRIGyYb4v_uaL5RPc7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بعد ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/129467" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0vX5cNWGx9QmpvvmFH9d2pyfKhcoCqPi3yll_M5H3irnk60-DrFxqqPbmLmMJ_f_ccAxqkF2TCU0N8iHhtypcmLLm1a7xB6YHjYkklD7-XTsGloTDe1FyoNZoBnM995YEB5Y8D6l6xT627LecjtKaDnihN0GKJ1XjbQojSGe1TkK-qy8Lz_Y4AvZIUQRV_OWhoosOwhL4XJ3DmPeEijWtMU8azyx2Zs-IuP-9nc9WOowUkAF0DpjOaT9puuUktn9zIshu3YXqtEhy0HRydu53pDqzGR9MXGcrkj49Y3as93FK_CB70YByKOkAaA5Sjn9dOKiWfQ_gelhccp-4WcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط ساعت رولکس امیر نیوکاسل در مکزیک دزدیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/129466" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129465">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=OfZ2CuiRhjBGODNDb6nHFc66XtdJp-D5xUiiLiP9Jl-oCa1ia_sxpabLU01tjds9enHJCEf9FIxaVkeXj7tuxIdeMzqZ8yF-2RWRFkn9WU6N5geDN8SR1VjcrBR_GIUv7zTQBQ5ZEtBF8qWfxw8JzVBe0P2KchQyadCsrLTZ2sN_wMy683evHX1_kSMKrjor6gNppyBBD7r5dusdjtkvqKCmwtAaqKOWlNXBY0OjXF0xCc1lorHRswiEeT_z5XAiN1caoX1yLelyJq2wbDFtyiw3AqNROgEreLU86ZReHfeojEoV79cTx5BU_gJobHE87HGmqyADaPE8EL5UfGFwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=OfZ2CuiRhjBGODNDb6nHFc66XtdJp-D5xUiiLiP9Jl-oCa1ia_sxpabLU01tjds9enHJCEf9FIxaVkeXj7tuxIdeMzqZ8yF-2RWRFkn9WU6N5geDN8SR1VjcrBR_GIUv7zTQBQ5ZEtBF8qWfxw8JzVBe0P2KchQyadCsrLTZ2sN_wMy683evHX1_kSMKrjor6gNppyBBD7r5dusdjtkvqKCmwtAaqKOWlNXBY0OjXF0xCc1lorHRswiEeT_z5XAiN1caoX1yLelyJq2wbDFtyiw3AqNROgEreLU86ZReHfeojEoV79cTx5BU_gJobHE87HGmqyADaPE8EL5UfGFwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/129465" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=cbH4X3V4ymIRoMVlBGP4n-dOU5cRxBzxdwTaeSBVH4bSd368EPbI_55YR0uDw2b1zdSNXEtOTKoBpqR8ar7vV2lKw79TTIOanh47-QX0FK0A9ojeKid6NEhKgmFEmS7Sa4_OTGUxZsVqSPa9ez50mJQLFByqZOJ319xEF4whPHqCBSJhTKTSEqyHSFjuI5Xgfda4-BJmjChSNehYAgOTwnCTU7S6MegBcOp995KR_YDT6suGoGNSXDcjW_wMf7XQ0BCkacJXRlf3KDkQQ4ikZykDHHzn1wTzeEcD-o5XPElENHUtAfDRUcA7SmDBW4J4mbB0wZ50AWQHr70Xhp6qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=cbH4X3V4ymIRoMVlBGP4n-dOU5cRxBzxdwTaeSBVH4bSd368EPbI_55YR0uDw2b1zdSNXEtOTKoBpqR8ar7vV2lKw79TTIOanh47-QX0FK0A9ojeKid6NEhKgmFEmS7Sa4_OTGUxZsVqSPa9ez50mJQLFByqZOJ319xEF4whPHqCBSJhTKTSEqyHSFjuI5Xgfda4-BJmjChSNehYAgOTwnCTU7S6MegBcOp995KR_YDT6suGoGNSXDcjW_wMf7XQ0BCkacJXRlf3KDkQQ4ikZykDHHzn1wTzeEcD-o5XPElENHUtAfDRUcA7SmDBW4J4mbB0wZ50AWQHr70Xhp6qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از راهی شدن جی‌دی ونس به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/129464" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
همه رفتن سوئیس فقط آقامجتبی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/129463" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdKXpvCiMjm5EHHT78Oq359l7B3Xo9xphPciqscKyEec615uHq8REjVGrBFwMYwC4MJtoW_ubbfVz2P0s2CGICgPnf3GY6eE-vPnaZGUyqiR0vA5s-m1jy1rBo8dXKiyPVYMmaVi8v70lPsKJT1RxlaQ42llmvq-A76AMPkj9Uyo6jEXdITuZLYqXlt_2K65Rx87H9HZHznbl4W9pY0YGUwve7GG7edZORbsRxerEFmYkp_GP5Q3ivA8ow8jCPOM1qRNIsrY5OOD7kTlqB9o45GuGi48761IEoyX7eCGDFVkdhRqevUS0vS0YnFx32y5JO2zQ_j8poMk9qSd2C65GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا بعد از اظهارات ضد امنیت ملی توسط نبویان، تنگه وی هم اکنون درحال باز شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/129462" target="_blank">📅 00:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=voVbdE9FJJtD1_zJ7tn8ZFgU-bXwhbvLsvROiGlcS7Fze53ZBRENR35ZRXVPkkhtrGu-6BIacAXRhTaPy9vORTsMb5aZo8Q8N4Q2ZEUeCpr3-iuYkCjTvNtIlIG1_XgkKhWlr8gtiQg3xsdPNlpRQkXGwZgzHFH2KhgGtUfwp9xGNKsO2aqMZCKoUVUMuk2QgeWaK3pOgQCoPDVUDdbfQuRE6IHJs7P2rBF1G4BEW0wec9CsYywYyq8vsPbnKljPBg4SdvRtaSsNct-fcsIY4k4VLmHeztQk4EiKHwGHwdrt_qbAhyRmB-xMM5jVhvUp3xIB_EBGWjbE-XBBUbdrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=voVbdE9FJJtD1_zJ7tn8ZFgU-bXwhbvLsvROiGlcS7Fze53ZBRENR35ZRXVPkkhtrGu-6BIacAXRhTaPy9vORTsMb5aZo8Q8N4Q2ZEUeCpr3-iuYkCjTvNtIlIG1_XgkKhWlr8gtiQg3xsdPNlpRQkXGwZgzHFH2KhgGtUfwp9xGNKsO2aqMZCKoUVUMuk2QgeWaK3pOgQCoPDVUDdbfQuRE6IHJs7P2rBF1G4BEW0wec9CsYywYyq8vsPbnKljPBg4SdvRtaSsNct-fcsIY4k4VLmHeztQk4EiKHwGHwdrt_qbAhyRmB-xMM5jVhvUp3xIB_EBGWjbE-XBBUbdrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ورود تیم مذاکره کننده ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/129461" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان پیشرفت حاصل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/129460" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هیئت مذاکره کننده ایران وارد زوریخ سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129459" target="_blank">📅 00:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / جی‌دی ونس، معاون رئیس جمهور آمریکا برای پیوستن به مذاکرات بل ایران ، واشنگتن را به مقصد سوئیس ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/129458" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/ بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/129457" target="_blank">📅 23:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/129456" target="_blank">📅 23:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/129455" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
محمد مرندی: ایران آماده است تا برای لبنان از توافق چشم‌پوشی کند، زیرا از متحدان خود دست نمی‌کشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/129454" target="_blank">📅 23:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB-kHVE5_Eon0Mdlf3Cez3LuM22yY8Am5GYa-cjU8zJvU5YNdWIIJvjqWmFqVmL9t1LVxGVP8EYber2EFGdf8evXtYCQM_nJnVVpumwFM_tieL3RsJTfDhg7XB0GSdrb-tny15fFKk4OYGLULMYcDTP9L9yQKyY3C7jZNLRue9QcJsHNUDIq-82iht2Dz5ANvUedd1q0f1TfRdQb3TmLgwU0O_juiwMM3AmHBn9btybdpRym5P1gcWbSvfO66rfsiyH9j_EeeojY1OsUvYLYibcZ0dPsRENNnffVgEIJ8M2av7KOCfpjec5IFtHhKbnwFAtK79Tjn_0kPalTHNsZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره، خطاب به پست ترامپ : هزنیه‌ای وجود داره، این قطعیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129453" target="_blank">📅 23:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129452" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/129450" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تصمیم به آتش‌بس در لبنان بعد از فشار شدید آمریکا بر اسرائیل گرفته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129449" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129448" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رسانه اسرائیلی آی ۲۴: پشت در‌های بسته در اورشلیم، انتقادات تندی متوجه ترامپ و تیم مذاکره‌کنندهٔ او بر سر رویکردشان به ایران و حزب‌الله شده
🔴
نگرانی در اورشلیم این است که ایران قصد دارد از هر توافقی برای بازسازی اقتصاد و توانایی‌های نظامی خود استفاده کند، در حالی که امتیازی اساسی در برنامهٔ هسته‌ای‌اش ارائه نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/129447" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKF90eZzE8HiAwSnBp5u0lTjektcdsgrRTkuPkTcgJ4fY_zBml9mKDkJzSlNQo-LB-1Pbl8V5Fs_dynqHd3Xs_Qa8Vq-WZH_r3iZVIlBmUYi_jB8OJVM9VofqiAIpPF9tAwl7FFMPwMtzcojIhEgWSQX533IAgoJaDWVUs8PUZZ3cMHr6TMJifx-DlIniheo0DcczKTAZnpzVNuuejdu8CUaYwGEopay0aAUu-TBnVIuFSS5dQ5xcM-C4fJmC3IqnGoB1iExMaDmTwPs7vU5L3E24WzmlXReXeZKn3qQBrqU2GpNFIDsGC3ynyHFTX66CKmdRestUV2T-NCPOLm-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در تنگه هرمز در طول ۶۰ روز دوره آتش‌بس، عوارض گمرکی وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز عوارض گمرکی اعمال نخواهد شد، مگر اینکه توسط ایالات متحده آمریکا و برای آنها، در صورتی که معامله به پایان نرسد، به عنوان خدماتی به عنوان فرشته نگهبان برای کشورهای خاورمیانه به منظور جبران هزینه‌های گذشته، حال و آینده اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/129446" target="_blank">📅 22:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال ۱۲ عبری: آمریکا در مذاکرات فردا به دنبال دستیابی به توافقی برای بازگشت بازرسان آژانس به ایران است
🔴
در صورت موافقت تهران با بازرسی آژانس از سایت‌های هسته‌ای، آمریکا چند میلیارد دلار از اموال بلوکه‌شده ایران در قطر را آزاد می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129445" target="_blank">📅 22:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
الجزیره: شکاف فزاینده بین ایالات متحده و اسرائیل این هفته به اوج خود رسید.
🔴
مقالاتی در نشریات مهم اسرائیلی منتشر شد که ترامپ را متهم می‌کرد که پس از امضای تفاهم‌نامه با ایران، اسرائیل را به ایران واگذار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/129444" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ‌، درباره نتانیاهو : من کارت‌های ضعیفی درباره نتانیاهو دارم
🔴
من تصمیم می‌گیرم که اون تو انتخابات برنده شه یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/129443" target="_blank">📅 22:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QALGGI9ces_-GVPvby1ghVEmfVo3O7RgBzfZimwqFOWELW0YX1jxz38TOwNv-wyNcgebTgoND-dcgMHjmibI7MaQGorleOipcHQcAooUdRbM3swKh9-b6GdLOWftISid2iRWrUwfOT3ypOhrkoRaJ85hpuwf2_YYFZEWScjWK1IBg_ez8K3RV72uUW-EKg6ycLpxL2ylemjf5GQX7Q029xddozi710laTrCDVO6-Iy33k7bSZOtu9CD7-LzlFaJyEr5dabMafgVSP2NHapEod5ZFfJxfRcT5hHCb6OZ511kQHaxuLHulllkgzq9IJ0GLiDeIQEad7rGOa8MCQlcc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید نبویان بعد از مصاحبه ناقصش توی صداوسیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/129442" target="_blank">📅 22:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از یک منبع دیپلماتیک: پیام آمریکایی‌ها به ما می‌گوید که در لبنان دست به تشدید نزاع نزنیم تا زمینه برای گفت‌وگوهای سوئیس فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/129441" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بیش از ۱۰۰ نماینده خواستار استعفای کیر استارمر شدند
🔴
روزنامه تلگراف از افزایش فشارها بر استارمر، نخست‌وزیر بریتانیا، خبر داده و نوشته است که بیش از ۱۰۰ نماینده حزب کارگر خواستار کناره‌گیری او هستند.
🔴
ستارمر اما هنوز نشانه‌ای از عقب‌نشینی نشان نداده است. او روز جمعه و بلافاصله پس از اعلام نتایج انتخابات میان‌دوره‌ای، در واکنش به سوالات خبرنگاران درباره آینده رهبری خود، با لحنی قاطع اعلام کرد که در صورت بروز رقابت داخلی برای رهبری حزب، «وارد نبرد خواهد شد و از سمت خود کناره‌گیری نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/129440" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee12760742.mp4?token=dNaSW3K7eAVce5ARZPLOCXYLCGxIwsXRLEgObzRYP0l6_5MNrMX6gvxOE76PaznIGkKbCd7RV34-nuePa3aqSwymqniox9ILscKoEUdUMZPfcWD0Kk-qO31_fXa-eZF0-iPPj0UFNJ9QuzPTi240i_XoEbyCSZJbrysyV14nauWTV9kf54LuUvQ5bj2Y7U9mgR5sNCuf0Pz3S_SDXVPSTgAQRa9Rs1krIGX_a6eqTt30ZmUNdE4jG-Mxq2Ob_05uQ1T7tNHAiyIY6Qt55J7P94dcdpLwlfpcbLY2Wl4p8ckbLINAzUclJPkNaeKmjCReg-udVdm0ksxSihFnOfQ86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee12760742.mp4?token=dNaSW3K7eAVce5ARZPLOCXYLCGxIwsXRLEgObzRYP0l6_5MNrMX6gvxOE76PaznIGkKbCd7RV34-nuePa3aqSwymqniox9ILscKoEUdUMZPfcWD0Kk-qO31_fXa-eZF0-iPPj0UFNJ9QuzPTi240i_XoEbyCSZJbrysyV14nauWTV9kf54LuUvQ5bj2Y7U9mgR5sNCuf0Pz3S_SDXVPSTgAQRa9Rs1krIGX_a6eqTt30ZmUNdE4jG-Mxq2Ob_05uQ1T7tNHAiyIY6Qt55J7P94dcdpLwlfpcbLY2Wl4p8ckbLINAzUclJPkNaeKmjCReg-udVdm0ksxSihFnOfQ86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زمانی که تیم ملی، تیم‌ِ ملی بود
@AloSport</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/129439" target="_blank">📅 22:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
المیادین: هیئت آمریکایی پیش از اعلام رسمی ایران وارد سوئیس شده بود/ کوشنر دو روز است در زوریخ منتظر تصمیم تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/129438" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
علی الاصول، هواپیمای حامل هیئت ایرانی تا ۱ساعت دیگه به سوئیس میرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/129437" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL5lIlinbZPfS-igWgmGyMAo4DmGrW9puWQaEVNNOxtWm3MNKrsV4cLCXGkbJMc2XphJ8-zTSRrFFtKUp6UpyatDSC7PE8AimfmbNa7us3qcWtm-LgQ1V3XjuDuCeeIdEdzF6MwwLveRtUC9Fb3ww4YX3r6kWUurBHix7rtDjVEDxr9y5G2LNKE2bM96RnimBG-aDxAb4bIDy4wtzBSslicBR38xKT0XtVQoRbnBcbR6tYuJA14rXayEjdy9K35mVvhUxcpqsX5OYJuMXFyhuNmH8GOaMYfd5knbAu0hVVuwLLuHX-CO5k4g1HxnNP7kAhlza3M4SXo3cWsn01EzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین های تک سرنشین وارداتی جدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/129436" target="_blank">📅 21:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8MFYOsoxesbAcVwnupGMKCpqTD0bdgYTXUwc9hu1Vcs92-8NZzMsmXxUEk6qP4VdC604IvhSQWTPG-Mnr5T7OrBWCrYWv1gVgAoirBxZh4hOaukd6W1ZKRGaSjOXLQXhKsEaFTSjPColBq-NqUZkwmDSIICoJO7el2w5Yt6LJsh5vgwlYG1fzh8mF6_PgttdmYjxS55yFf0EWb53mdrkrva8eQI2oZTUQLqsUESEADwd6OuCyWAo2Tc7hkShz3kpKqBoyb_JinRW4T8MFrNkkO3JNQQ7tR7IFT4Qg1vTlgo5hzBjjMu0G0xQDNNaIYEfi9cdGwX63Wcg59IRtJtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی:
رهبری میگفت باید جنگ رو ادامه بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/129435" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/129434" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYJ8KajfEehaBbHBmxyG9kNHf6NEMzflyWkj_tk3GjmkLdUSUBiLIdIKRbSHlsAHY7RuIoYb2GQaoQBRDhDeLNLf_1zld-v8a4Ki0hl1e1tiSTXeTNZwa3-C4EEDgS83-m62w1G-evPLSEHXgWZooPJYwPyetFULveLNH_LVydUBckkKc836CWU7zcZlngY7sHbMZsosq2JKxCVUjf0PNzHLuZJxOW1DpIaT9zv-jhYTenbOL1zHJn1CN6HGbm7IoKSJzWzXk9Y_sz1XquRSgfvb0sUBNIzKZqudVQjoMVP-kItZ5QW8J-JP5XScMJKHo70sF_IlkTM21oGgKCUbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای سوخت‌رسان KC-135 نیروی هوایی آمریکا وارد منطقه شدن و یک هواپیمای هشدار زودهنگام E-3 هم در مسیر خلیج فارس قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/129433" target="_blank">📅 21:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O43QOn7CIjDyzMwVpI_TJv5AoAC0v0Y9WqwUfHPjVB1TdM0FVjhf-HITpGNU9g7fC5StH0Fcq5A1hTjBLb53vYnbxFH8uK3XqwdnQARBteJ9kYEQb0f2whC12C3gUqRmyKjafgpCi8XqPDSB9MPRQcuQBJ1OaPJybCirLKEbTrC61dx60Hj_cihoyPYxJ1r-LuXeJZvGxCnfXsaWvvH6U8kGUvYQ6bwW2ML4KXz2kChmyg07vvHggsomBCp4MASQsfkN6lYfq_2LJ6RwxqT6e5nf5Q6nB4ixG8yoiP3dXiZyYmFksye8jgiSAc3owL2eDxT0DX2pSZuZIGsehOhxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129432" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqw3Ps_hs6wQnUQDcROamzf2Q0Ifn8A4ynD78a2EtaUukKytMOZHQ_TN-2jJ2dE3OZ7EZXyUBxumCVo_TfbdOkxvKABj27PeF3Ymt7_fhUL6euroAy1Joj_V1M0qlNSEsf_rA_UbW3-Aq4MXy1bCIunMoiYddUNaqSoBi9HlBp6dSxjFkxP7QXTYYu4qDUcC3fw-VRgRj_05IDvRkvK1S7ea9w6FQQM7jPO9jim5NtZHMwlVB6erK7CC8E3FEL98o92yGnGvsSR897vcvXtDhavnAYb6sd-7ctb7lUJe71n-wfhi0WxqvExRf-IWQ_eKQc3QlFDDNoDZYMRD08gkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان و فرمانده ارتش پاکستان هم به سوئیس میرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/129431" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/129430" target="_blank">📅 21:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=IPNVlHe2MJsNW_pkWQr3PuuExy1RmcKyLXhBy-UU0_nUEsiYSvUrObHEoCGKsHpx3jjsMg-KhBfuN_HPX0ung92MjxzVzygko9HIMEEfelR_foHCQgiQbd2ymS5UQ6p2690Zo5MuzwQWlBddF2j18OVgFBhE3G2e5X16c0fxrRi6s9xTdz8G2XRM_wyHoQQiViM6qz2xm4iWnrey1ZbDP4nM65q-nKdd58BfOE6Xe1WJ1g9Ab71yn2xxvmZKkGRiojj-p8fapB5P6UEu-vKToaR1Q6TWFXD8jVOM7eg5haotlzZQ9VFnW7l6zkDppuC2QzpQS2Q6oTWqjcgFjIlEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=IPNVlHe2MJsNW_pkWQr3PuuExy1RmcKyLXhBy-UU0_nUEsiYSvUrObHEoCGKsHpx3jjsMg-KhBfuN_HPX0ung92MjxzVzygko9HIMEEfelR_foHCQgiQbd2ymS5UQ6p2690Zo5MuzwQWlBddF2j18OVgFBhE3G2e5X16c0fxrRi6s9xTdz8G2XRM_wyHoQQiViM6qz2xm4iWnrey1ZbDP4nM65q-nKdd58BfOE6Xe1WJ1g9Ab71yn2xxvmZKkGRiojj-p8fapB5P6UEu-vKToaR1Q6TWFXD8jVOM7eg5haotlzZQ9VFnW7l6zkDppuC2QzpQS2Q6oTWqjcgFjIlEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/129429" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=ZBDgS6y7hKGTVza8-N1VrzLLoXGcGroRt9UKBcF-Szh0AZmFFick_bgORPDFCEz7J3QZs_7DZ__eFZU4vf73o-UD1A_gxD6lGq0XBse7oqcWx2MZTCAO6O05vAoIFgjzXJtp_ewl-OvTKo11SEwnmZ3M7iID4gwKPhiLfANeAl7Xhh7mdVO5LX3MCoZqV46KehSVyg-PlAqvpWeARAT0l6Y0VLm_5uYLRgK_LWXvfT4w_WOpoUGHWfIGTqKU4esJfPRd65v4E7Zt3xCkxx-CIszt6i0le522NvadDE2qADAhywM6fTtKx8W8DNxIovitK8zE9Om3nYVr-Ztbp7cQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=ZBDgS6y7hKGTVza8-N1VrzLLoXGcGroRt9UKBcF-Szh0AZmFFick_bgORPDFCEz7J3QZs_7DZ__eFZU4vf73o-UD1A_gxD6lGq0XBse7oqcWx2MZTCAO6O05vAoIFgjzXJtp_ewl-OvTKo11SEwnmZ3M7iID4gwKPhiLfANeAl7Xhh7mdVO5LX3MCoZqV46KehSVyg-PlAqvpWeARAT0l6Y0VLm_5uYLRgK_LWXvfT4w_WOpoUGHWfIGTqKU4esJfPRd65v4E7Zt3xCkxx-CIszt6i0le522NvadDE2qADAhywM6fTtKx8W8DNxIovitK8zE9Om3nYVr-Ztbp7cQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌گویند من به اندازه کافی سخت‌گیر نبودم؛ من بزرگ‌ترین پلشان را ظرف ۳ دقیقه نابود کردم فقط به‌خاطر اینکه دیر در یک جلسه حاضر شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129428" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prU5Z3BoztWj7lxtIgDzUCWYUYq_C1rqU-PMwpXg1mRORi-ZyhDynoiWQh0tCMNy_ZrmysEE6tytcLe3_Ks0DLgUv05rnA9yTux_xN12NKxDq8QQVsCotqeR4n3TGnR0AYXO2oJjVYE5QCGTkGwiYq3m4Pl2GXKqPUD3y5I5HgE6gGzR5zQCLg4Fr7g2quXBXYIuJYtTXC6gMy6Ii40wQDHGdnzkSjTl9TQenJMMBp0BdRV1Y0mSw6d9ZZmgS5DRhXIA7er8qYaMnHFJ3O0DEiPk6Kpu3I2E3e6YuypF-Fj2xwVGCwZlYzvNpxYCH8m2Dkmae-G4HkxwoxOyI4UeUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: سازمان مهاجرت و گمرک (ICE) توسط رسانه‌های جعلی در حدی بی‌سابقه مورد حمله قرار گرفته است. مأموران آن میهن‌پرستان بزرگی هستند که سخت کار می‌کنند و در محیطی بسیار خصمانه وظیفه‌شان را انجام می‌دهند. بخش زیادی از این دشمنی را دموکرات‌ها و رسانه‌های جعلی ایجاد کرده‌اند.
🔴
مدتی است به این فکر می‌کنم که نام ICE را به NICE تغییر دهیم. این کار خبرنگاران و روزنامه‌نگاران فاسد و غیرمیهن‌پرست را کاملاً گیج خواهد کرد!
🔴
تصور کنید مجبور شوند بگویند: "امروز از یک مرکز NICE بازدید کردیم" یا "مأموران NICE یک قاچاقچی خشن مواد مخدر را اخراج کردند." آن‌ها نمی‌توانند تحملش کنند و کاملاً دیوانه می‌شوند!
🔴
فقط کافی است یک حرف N (مخفف National) به ICE (اداره مهاجرت و گمرک) اضافه شود. به نظر من اسم معتبرتری است.
🔴
همه این ایده را دوست دارند، اما تام هومن به من گفته که خود مأموران به اندازه بقیه مردم از آن خوششان نمی‌آید.
🔴
چه کسی موافق است که یک N اضافه کنیم و ICE را به NICE تبدیل کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129427" target="_blank">📅 20:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/129426" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hoc8izHmSLMDN_5Y9nQUNri1Yy1NFlJN8I4pTOpD9vdxPDJaXzuwWvyvyzhsNW0cmT5_h9utslCdyzq77fFCqpkuiDzzgoQrxwv8sF8wqMoiFrF_G5t391OxeGhe8jtei0SzAZFxA-80lu7nVFU0nNUZWnoomAQ93HBu-yrksh-1AcJN4rlUZDOQM-cZHNzmdKC6usdQj66NzsIy54r4TAeYs8UPdDfLSi5w3Ppe92xdjFzCWc7WHZZHpO17FGsg10hvTGpmXxDBKQp1mjsmVRQcbuNAo6ws1DTwid6R23xgTYJmNYvcjhZ2dsyoTmGArQkhlr1-Ebdhd-S26_sYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/129425" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع شده منسوب به آیت الله خامنه ای را در تلویزیون منعکس کرد.
🔴
اگرچه این برنامه‌ی سازماندهی شده در صدا و سیما یک‌باره از آنتن زنده خارج و «قطع» شد اما رسانه‌های پرتعداد منسوب به این جریان، با ضریب دادن به این اظهارات تقطیع‌شده، به تحریکات علیه تیم مذاکره‌کننده که هم‌اینک عازم ژنو شده‌اند، دامن زدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129424" target="_blank">📅 20:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کانال ۱۵ اسراییل: اسرائیل تلاش کرد مسیر لبنان را از مسیر ایران جدا کند اما شکست خورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129423" target="_blank">📅 20:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/129422" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع نظامی:
ارتش اسرائیل دستورالعمل آتش بس دریافت کرده است و نیروهایش از منطقه علی الطاهر عقب نشینی نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/129421" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترکیب هیئت اعزامی ایران به سوئیس به ریاست قالیباف
🔴
محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیئت مذاکره کننده ایران
🔴
سید عباس عراقچی، وزیر خارجه
🔴
علی باقری کنی، معاون بین‌الملل دبیرخانه شورای‌عالی امنیت ملی
🔴
عبدالناصر همتی، رئیس کل بانک مرکزی
🔴
حمید بورد، معاون وزیر نفت و رئیس شرکت ملی نفت ایران
🔴
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزیر خارجه
🔴
اسماعیل بقائی، سخنگوی وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/129420" target="_blank">📅 20:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWWLbcMvD8B_bojFSfniXWBIOt37p0BOiAUTYpHvzjiEApU-bx-FMLfw-Mw-4qXEaqPsw6hzuOVn37x3MgAZtdVxnw7prUZggrNCsuvexWQ3naha2Yxv0CRUHp6GU4AlNBVKCs3PtbxjEebJsCRy5IQKObbGu7lBMnadbINvgMGBnl6Q7XDJEqX2yh_h85gi5x7wjNUNIFUmJOSdh3joYC1LAi40TTZ7kIrzjhjpGTeNHrlUE8A6uHPiqJJsqWRodao_BFjfT7jNMpMrkGp9AZ5RMmRSseTNX5nzKv1Ip6ZKgGBZ1DdAcGZgWPmU4QXkUdZYJCfRtRce3tVq4u18Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MO3M4y0KYwwS-Ppq6WSFtRaHlEQewtH4yHJc2e5vBAK_KYBbmcePzzdq-7cMENiUclapDAc9pEXBdi9XOaBX_9TUY0st1afcYIZs_c19OKPsw8NFBw7pG2zX_c6IlB2WpJv_ytWGNb_ag4vPgWd8Y8U0rrRxjPaJDaQAJxdN2I3G_Jnhu5LICE4a9slQzsYc5NGSh90QpuMoVqZWB_DIFXSUlRviv4NTNRHkXZMVbMe1tSAJsEaKjJHQKMBW08Be3DC7t6YPiV5hNAVY7eaoBOHwgO4OJcHAn_7o8Ufm4sdiR7p-kxA5-SZH_jyWCurRmEBy6_5h8ESxQUbGP63YyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecsFQryzQl4u0QL2RBNYeHNvRd83zOqzSuPE0uyCzx-QSRfvn11ACHiLoCJ0LA0fBu9dU3JzQzUwNRqOi4ifJOzTQP3p1bEsTGpedvRTizvxDDaLj-qYKgt2pnx_2tMgoH1W1j-tE2lGhNZstNrxYhhNRK9eD74xf4bbija2ljB5Cnox2sJEbq0xZ_YWmRZWZIEuaut9PdA8O_cq3ztTOEVE2RzBM7DyJfcHD4ojUIKKVdlylFwYor7AD57dib9Hm5qnDuGJhlhBCjlqmPLAV2sLD3CbwDIx4yzQMQYG8dbT2ng0FvdLOt2tUAAiR8vPlxTSc7ibY9XwW-NOy8DT3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
فرود پراید در اراک روی پشت بام یک خانه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/129417" target="_blank">📅 20:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO8sqRNFB8ZtNwip7qcrV48iBGGR0-lDr20z2aTEv43WRnq6gOanmcYeqJaP3YGisrJ4V-aoYzHgBbqQVVlbXLRRgz2S4QYUfq_-ys5lbYdRZd_hS-eZlzCsTEdvyYyRCDHPYpK4p1OZAb9gfQvl2pNIXx48raNfANmPoQB2ppEb4pSY2x2eva-wrRA2RKAcUntXMvtJiieNAh3FJkEK-FdmSFt-_Q4eVLRuhfX7MESJGBnuatU0_xAW2zeEdM-2hVCjHNtI30uuj29Jgq1hFUX_FuFP17ygOtUW1uHOchmJYBKNgBit2kSQE4evXdcKFTVTGCX-JiWnVe2V4jdYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوشته پشت موتور یک خانم: لطفا نزدیک نشید میترسم، تازه یاد گرفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129416" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_Ge8rlzPrVAwd8jVUSAKa13KbwfMukokTfkwOmDoSf4CKq04O_pa2Js71zccHmXIbwiDP7alLyR-rZ1zKeVEW53ByzotFMgAUVZiIZamnb1S5TBJIS0qR4PZPlLGZYtJ_VpjidYitF7NQSY7xFIxAC3UWsraQsPK0fqw_7kWG4p5XHE9DEqwvkHKDJeNwU3_2pbCeMQauLq1daqoBeLvsMzR3SHoz11ZJTtBuPL4ajEe6fiAoTCllnTvCuTwPm1LPK_8LtCpa9Ye_cKrqP6a6fD315HdFlZVWo4aMWPCH3aUEbCyUnNrJxAMmu6QMja1nw4x9zpQdOG1Y69-usJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با مسعود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129415" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بلومبرگ: عراق به میادین نفتی بزرگ دستور داده است که تولید خود را به بیش از ۳ میلیون بشکه در روز افزایش دهند، زیرا صادرات از طریق تنگه هرمز به تدریج پس از توافق آمریکا و ایران بهبود می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129414" target="_blank">📅 20:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92808565ea.mp4?token=FRQfcHzgDlrky0dFdjPOcSl6AUgBsblV3nklEspSzm9rVNIHXcVF6cR5c6pvRA8B97-87AM5tLAeJmyVc7r5zblN6DOMRnzwLa6SQkZ8on3Ka2PbTWxXaB2oYw-mRmAIU83M71gyCQerMNnaQ8pLshrZpT6OeBCc9J5yIkyIrHrjy8rAUcFuXhOOEqBUhb3xL-o30-HV5JThRm6nx98lFjEYne2VK4AwTfb0AuF35KARb7aoaItr7_Gxj8cBc3sGmA-Nrg0-2KNgkJk7Q9EEgHhcT_aYgnG6AtL8JRYRfY-uaOkXm03F3_E7rsdIG4_VQs2LLpKRxue5MMSy8xk7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92808565ea.mp4?token=FRQfcHzgDlrky0dFdjPOcSl6AUgBsblV3nklEspSzm9rVNIHXcVF6cR5c6pvRA8B97-87AM5tLAeJmyVc7r5zblN6DOMRnzwLa6SQkZ8on3Ka2PbTWxXaB2oYw-mRmAIU83M71gyCQerMNnaQ8pLshrZpT6OeBCc9J5yIkyIrHrjy8rAUcFuXhOOEqBUhb3xL-o30-HV5JThRm6nx98lFjEYne2VK4AwTfb0AuF35KARb7aoaItr7_Gxj8cBc3sGmA-Nrg0-2KNgkJk7Q9EEgHhcT_aYgnG6AtL8JRYRfY-uaOkXm03F3_E7rsdIG4_VQs2LLpKRxue5MMSy8xk7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طالبان یه معلم زن رو به جرم آموزش  آنلاین به دختران در ملاعام شلاق زد!
🔴
طبق باور طالبان، دختران و زنان حق تحصیل ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/129413" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام اسرائیلی: ارتش اسرائیل طی دو روز گذشته به 300 هدف حزب‌الله حمله کرد و 100 نفر از نیروهای این گروه را کشت
🔴
نتانیاهو به ارتش اسرائیل دستور داده است تا به هرگونه حمله از سوی حزب‌الله با قدرت و قاطعیت پاسخ دهد.
🔴
ارتش تا هر زمانی که ضرورت داشته باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129412" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر کشور ایران: محسن نقوی، وزیر کشور پاکستان حامل پیامی به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129411" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCIUhfrdQHwahxglxvf8nuLhnEnGhb7bCfU0xmLmmUkTwbBdeSjO6okcWON1uzvqQSY4dYduniUBtDwklkpeUQtKTGy7nA_BUCQvijUEwmMwAmtFSiY0V4NLlzCmb2PjVtAMfrW9QWDcCfzWqOBGUB3JoYDV766pJVYPlVTD_sOBmn5-MWq1RMVmRYPDCtFwAkxmT0B9AHzchArptRWnlB3E94WpFS5s3kX907WG873LYk0_-pa9pEHv3MT9yj2sjf--ehflCsBeR6IAEBa7zhzFxO8-dzD5od8VeYsJqvUwHD0UyP5zymFIAKoLDodTU-EnU6ZVAd4OWEgJyeqWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129410" target="_blank">📅 19:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pByenN202L6CcjWfhus1B0a3nQtM-FrikkHOU82QkgcIHyPmgDdCH0JBnHgA8NYR1pmjmjAQ6BZWdrXmSJmxo8Kfyai9UAFzS1XbCFC1xWuA1_S6g9c5T9HEGK_5rGPZdLFftR5wbCzq5yRXRrtCGDiEASrwnVjPb7v3ykusuTnbgbrJmvv_DG6LAGLhHaPHyUc4FynIMDwUEwqD2wu5GB03rgGiw7d2pa5_BaacU_rWMNDoLBBlwsT2Sc300ID_Hd-_wamy5LJte9jXfzSE2_lXnSF2xEGEcLzdZSsa6O6jG4HZHgp_POZ8TeJnVamOhXMtQeylHB_psxawPGs55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، فعال نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129409" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129408">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف دل ملت ایران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129408" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
محمد جواد ظریف: از مذاکرات استقبال میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129407" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند: عملیات نظامی در سراسر جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/129406" target="_blank">📅 19:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گزارش ها از اختلال در اکثر همراه بانکها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/129405" target="_blank">📅 19:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سنتکام بسته شدن تنگه هرمز را تکذیب کرد و اعلام کرد این تنگه همچنان به روی تمام کشتی‌ها باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/129404" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
معاون ترامپ: احتمالا طی ۴۸ ساعت آینده به سوئیس خواهم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/129403" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: تصمیم نتانیاهو و کاتس برای آتش‌بس در لبنان با هماهنگی ایالات متحده اتخاذ شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/129402" target="_blank">📅 18:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
حمله اسرائیل به غرب خان یونس در غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/129401" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGwCQN5bomtoFq4cGU2pMsH2k3mz8PC1tZ2raV0Q0R2xEnwE3DOe2AqbaQzxQwT-oSJI8OLrQbvXaVo2kd2R2ta-A4gilYhBFB-UUMvcexKKr836X6gldbLyjKEj94KzFakHNJ3mCq4MlO93fMcnFsqbaOMXaz6ZpvwTiZL3MBQGCEIcWARCgfjjiEv4RxmTW0WHlaNt34Bt4P3MtGFPWT4JyeEg3SiQVYCWxHsvg3RHGgjapcSo3-5c94T0W5j1DR4wVwP2wafpP70Rd9qbPutTdWVcEWoPv27Apihpak7gNs0itsXR4OQ37iJ_AeZBwB8noJTEdTSRtwcCMjJ8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران‌خودرو: دوباره گران می‌کنیم!
‌
🔴
شرکت ایران‌خودرو اعلام کرد که اصلاحیهٔ قیمت محصولات شرکت که در ۲۸ خرداد منتشر شد تنها تا پایان عرضه دورهٔ سیزدهم اولویت بندی محصولات این شرکت معتبر است.
🔴
‌لذا پس از پایان این دورهٔ ثبت‌نام، قیمت‌های اعلام شده در ۲۷ خرداد ملاک قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/129400" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLuwHUNe_tbIV_hSUb-wjmwfbw_9voM_vyNAj7TcBYq-_rTNPxBB41J4kaHc68JFsvF96w0FDrlz-pk1slCW-vnUcvyybEAPP9CktVhHS2t11JZ6GOzwaTR5IDmW9aw2-h16h3srcgNjjUTEzQ0yy5dS4ECG6R3Lsc3UGYHPWfl2Dz8vovl1WyrSAx6a0CITraCrFzARFr7QFJw3TN7Ps0lK3dEYdZ4zNlzIDIUxZoYrqhtJGyhBTGnWQwr2oEhv7H6GRNCDKvUQyLCB51wqUDeD9iS67uIuteaRGIvPNFFKzZMUC3Q-QN_Yr9zWZtnALT9B8b98ipmhHkYVtTqAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت مذاکره کننده ایرانی در راه زوریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129399" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سی‌ان‌ان: ونس امروز به سوئیس می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129398" target="_blank">📅 18:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/129397" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری : نتانیاهو دستور توقف حملهِ‌ها به لُبنان رو صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/129396" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) انجام دهها حمله هوایی در جنوب لبنان را در طول شب و صبح امروز تایید کرد، اما هرگونه اظهارنظر درباره تهاجم به تپه «علی الطاهر» در نزدیکی «نبطیه» را به طور کامل رد کرده و به جای آن، حملات را به «نقض آتش‌بس» توسط حزب‌الله نسبت می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129395" target="_blank">📅 18:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnNlwOZtpT-QlwU6qr-1bhJdcNIpvv051_dXOr3KlbFqSLgy5BcgzuxXz9UumTMn6p1nYRQQTXeb03rRW9cJyqE58VU99yYYZk9YGKbZ2CbQsHMTiaRinYRx_OvGTJpgG4lEciZViMJ2WnAAj8OBBIfmgpI30fMTlmyrJ-d6LIXobbCxsCMacWm9zweUoF2CqX93nXhJ4H_hvv0qOgpChkdHeV8jUcQblAy8uJ3ITv_r_Z5OYHjkp55aw87g2-5qFzstHIFEovPWBxUqNu7eifcn_TJbh77uWSpk6YHb9ywJGk3YWVbjckhw-giW7rtnxxpTSLecHsG3n-C7s8TJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/129394" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
