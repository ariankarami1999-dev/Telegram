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
<img src="https://cdn4.telesco.pe/file/hUcQJAotKD7h7GL5cEA6p4d3o0U11RDs7ngz5-q1r-Y028dCMBD_mJVLia48NmHP1aij7zwMGqP3l9kMkTDMNcxKMiXLe2GSQB20N_VLfcSxtBlBhg_TqzpE2CP7yf2eWHT2rlYhnjWzy4okItHyCh4NvU5YWBUKzJ_luJ9xFHClgKG9CO96dB1Kso0wgmCVSpSqOSh2kfvIWeKz5FNaij-OMJANyfBbabscv-WzLHZoTwc97x3LA2RS-FyvUoIzR6SR3u3JlNd125uLl09r5Ma6paSXNj8eoS9O0Ite82BldqFe4CtUYJ-SMxFj-fFS7IGm76jEF5WJhnmpJBGRUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 617K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLnAQYai_aacQ4ZGsCobIf3WbLsi_mZBhtEofuaCr-8DuON7Phg0YoCq-j30NnHVJY-UGNg3cJOwaFhAOYsfkbQV6AKdZIio6IoAl0nCJx9oA8wgHRbJT1sFz0TWP4Fnwm2ErYJ3wjfZOtFWD620kF0Zt8iFSFJdPUPyoNR3DHznAJKgjpRMxe3nKhq6Td2tUlA5-PikI0YufipU95mWyIImfSw_DoAP8-sqWfcFqoPtJfXdK-WRCe32zQdWDQqHaebOqEdN3lSEXOXAKDNPZwBxSMXfSyZ-8au58PQ3LCpQMJv_gDwtlioaZnEWCd1XXiJIYSLaqAqonlQdqLFOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4nLYQQbOaLMzZLAA1xGTxt7iSyiXU8iW_hJ71wrV1MQUoiriqE0HWK7x248kaTjulkIyx8SgwcxVPjiE99d68Kc25YNGOaTG42PGwY6HjHzk5eBzPqDJLWipxNEN1xzG-l8ChysXzE2G8Qv41nagK7PjR9cWDMuBTeyG_IG_oWKBhTp0aOJYAy4JWHrFQPI54oRhFdArBF4ddD1dJ_qb888OTYIB_OpJ_1-am5GzHw48YwS4BubfTtbGed5-45epQapjHM7GbAUAsNp5oA9dBZe5FtVCCGPWRAEAOFemDFFpUw6BsRAl0-v0w_2J4JvOt3nNT5vKoWFE6E9w8biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp06kt4Kww5KJsFiHfHV0C1rPQkwfw5H2Af-MZUAapr1-CK-Bxqmm-_RfAxlnHPKIFDTpQn3R53fQGUNcHd-P6vfc418l_MbK5F_6ShAW96rEXWkfGZ8E1p7HhylWjYKhhOvJRy2gn9XlvizZpJEMG3hW9mo_IcIYxFz3Upqhp5Bugvrmja305IYNMotohif7CyhFq9Y0otPOazBZkgrMOSwjL58jJPFoZ0KxQ5G0geU7o7tWVGNSh2Gipfsnj5TJrhLGjmcsHZJc3pB8FZZ46WZuja4UBCxerk6nnL0EGzLdw9iT5vLE-JmWwZ81HOT_NxfXFJM9Uj-0dP-xL4BHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjlxDs2g6qhOdqFyKEEuqqpOnvV6WpW5f7uEb_AxbLt8nalTsDtVOgoq-vdmDI145gTvjYAUbkSB0rg3PpLMaMvcm8t0_Fe4I8WvCYWJChCifLRULqJ9LxbDvvpA7fbFlxjrtb7B12D3qfxdomNzfFLSzy6HNiPGgqSo9-X6bnDMgDn8ZPuxyqncnTovm-kPrKShg33_-USF2ba7mGM45NqajoNCYGDZw2PH4v31fZsEeynTq73H7VfAIA-KKOo2_p3KmuNm-mm7tHylpEHx7zhVUnLllCK2XdHmZsfwex_kWQcq9NL6ZMgDHY6eDrQiSDn-4OKJXEe56IiNK3kAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i67uQAx2EQJW8QAWZ2mAbrQ8CdIBD02EbDcVS_jb7dvyIfESmpxhaXIdcbbQVAi1bR92tSaWEziFUKvhd1p17ICaX9024rE1SwK_EsAlnXXr-i1ivLeScmsTvTkojcv09yYH36ud4yisXvfoVKzQsOcYcteeGmei6ldrwM87CknyfGHqjOb0Ag_EqDp1iRG_Uskn3t0LCYzyXxtcBoPM96ygEkGSOQAIdgBZTed4FCNDBbrFm6rXa-IM9m7mlfdJdotge89bo0ltwmPjXAIaOGULTudz8zSMVMaRqP9wrHTz9ge8HSjOrLpNHXdST5pbU8ffzotTzG6Htq3X2d_yuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
تولوز
🆚
لیل
🇫🇷
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/28978" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=XFQ-4thvZVcp9hJRggSGQuiaTMnrR2hcB-Z9vUJKNoNjYlzBSATTkHIpKpYrAdHsOfGPQ91O6JqErw03rwuS9_eRn7EWZhrUvYj0EWNueBZTY3WMWWgJ6ZLWcpckWuW6YpHJWful4OqQSuQ4iWaRWpR8P_BbFfajS_rFr8RNsszveHA3lqMZKgdw0kGtjpejiREVeSt8nQLQbYwmMZyXZMVIiercuVhOy41xNI1W5rQylBNGBnxsdWVpz5QDnW_cbax7cSPxPdyfM-EiObDL8qhn1rb-3hckH4XEu3PWfb6wT_R8Mr-8YwOy8RRoVIViumG7OotHoeeq7X65IS3lzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=XFQ-4thvZVcp9hJRggSGQuiaTMnrR2hcB-Z9vUJKNoNjYlzBSATTkHIpKpYrAdHsOfGPQ91O6JqErw03rwuS9_eRn7EWZhrUvYj0EWNueBZTY3WMWWgJ6ZLWcpckWuW6YpHJWful4OqQSuQ4iWaRWpR8P_BbFfajS_rFr8RNsszveHA3lqMZKgdw0kGtjpejiREVeSt8nQLQbYwmMZyXZMVIiercuVhOy41xNI1W5rQylBNGBnxsdWVpz5QDnW_cbax7cSPxPdyfM-EiObDL8qhn1rb-3hckH4XEu3PWfb6wT_R8Mr-8YwOy8RRoVIViumG7OotHoeeq7X65IS3lzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=tA8LFPgbPkjop7aBsSVhv3BgF2kyyjdQm8S_BFRZAgAnAt7uI2mFf3_YPa_sSleLnWPD2lPVmkb0Piyykq6bA8Js0590awTXkjFbxQCv6db5t9KlCDU7W-AoLPlldmPRfCjBx9skIbqIBmJ_F57dan3LbiSnRgcvRcr9Xs898brr4RbJYUdlvBf79Jxa2myLRKIWtwDY2P0BZWZUwVjj25POGun-JJ3rbtffolkbOjXEnuWLRvncllzofdEkQISR4Jgt0Jf4c-VOgOJGGKFEqNEWd5Z8Gw09bb9-8WeeoxPDWYO81OvrTDix7YY6vFp9JmRECkMzfqICL1h5WpAaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=tA8LFPgbPkjop7aBsSVhv3BgF2kyyjdQm8S_BFRZAgAnAt7uI2mFf3_YPa_sSleLnWPD2lPVmkb0Piyykq6bA8Js0590awTXkjFbxQCv6db5t9KlCDU7W-AoLPlldmPRfCjBx9skIbqIBmJ_F57dan3LbiSnRgcvRcr9Xs898brr4RbJYUdlvBf79Jxa2myLRKIWtwDY2P0BZWZUwVjj25POGun-JJ3rbtffolkbOjXEnuWLRvncllzofdEkQISR4Jgt0Jf4c-VOgOJGGKFEqNEWd5Z8Gw09bb9-8WeeoxPDWYO81OvrTDix7YY6vFp9JmRECkMzfqICL1h5WpAaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhGIohENDXW3hHgYn_H16y1VFU0BfoL0XXs9EjxCtIzjfcJf9k-WvZF_3lgyDp9FLzmTGDgBjQbcK05HeHlCvbuRxwPHgBpMHfgGDddk2k_DH6lJo6AJDfKMeEbYilE8JBPbqpbYThSIsD3mdkOu8SrjHFl49ZO2clX4hP6OUECPSE_O5si-Yfwr18r9NEAPiJ77n4oBaT47xiqYU43qIZhNVm6rxPAigEt7u3HczV49isp03rWR3J4AWnuSzqS2SvhPmgzjkUbTB-o8f4w241nHKu9ZcNnCHvUw0o8vx907WXyNo2ErockTZZzvIK3xNTTLAVhWcfRl9yWX9OJtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=RuVolY_7znyuA3DUP_rlPF6tYYpt8JLOr_etJBQFl8gim8HkzjO-PJJuVDPXP88miYqPgm7pU4w9qsXgnKkEhKgqsv9ZNWq20HwKDDQ6AJhIPgnXM7lzNbTewYxfShi50WdOOwtVTpyXxG_dj1LuxRYoFuyrIgcwVo5gZ36bYCRR9d_E0DlGyI2P_jHlwg1aOHDe7tC3zx0JJa32sH0t0-wJcv7BoNLF0ZAKB3femoOn9PTrFUKPAoeQKUTfc78CB0RM7sr0KprI8hzOJYqt48hjHTaYNvUbajoYy5yd6hIj0FjBQqFu8xjX0is-MpvNMTnPW8XFcGdnUEM-CaMgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=RuVolY_7znyuA3DUP_rlPF6tYYpt8JLOr_etJBQFl8gim8HkzjO-PJJuVDPXP88miYqPgm7pU4w9qsXgnKkEhKgqsv9ZNWq20HwKDDQ6AJhIPgnXM7lzNbTewYxfShi50WdOOwtVTpyXxG_dj1LuxRYoFuyrIgcwVo5gZ36bYCRR9d_E0DlGyI2P_jHlwg1aOHDe7tC3zx0JJa32sH0t0-wJcv7BoNLF0ZAKB3femoOn9PTrFUKPAoeQKUTfc78CB0RM7sr0KprI8hzOJYqt48hjHTaYNvUbajoYy5yd6hIj0FjBQqFu8xjX0is-MpvNMTnPW8XFcGdnUEM-CaMgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZNuyigEbUXowq--jyMQ--dWK8S164TFhi4lSTiUFW4TPUu0JMrJVGwZMrvMzy2Nd5TY4_RUf9WjkzjErcOWPz7GASxjjXhXTQAR_mBtOWZc6JtyEyIUsEAKr0QGdQi1m7Zkz37iyHyBbPYjhaMplZxKiL9Edz26yMvJzxICazDzhPvPCuHTNhe3qjmixmIKcz9CDzU0s8Vt0OjpRYcWidbth5ctrnhgLbDqwpYfBay6mWsrNr-pxIHPlOsom5YV4TcXgRlSPQDIITljnuDcHHgh6WiJ-J6-Nrpu3FCe6IpMx9b4zzqiiEeeDE1Ic2iLMeb-BnJzKIPfK-X9HKu2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-5KM_xqFz2IiEkIZT6WKblpLeNYaTLMgLPDgK0q0NybLncJQnP4IYFwFqIH29e57XSEOlMsr8hMHPhf5bN877BJSt8RYmXfEHP0Ra_CmGreaAWkNJQcpMvfp4WumXnYTuHKW5VmbHDqaDyNWVYuQTmNjJTH7UCHcVctlNomouHCx_19YU8KkjpQjLdLcQJBQMuMTApvNLJmQeDfQ3pBoTib_9ivtQ0z8y7mz-9DcxOH5MPeHHSpUzl_s_ZhO4l4Gq0LY4ad3a1IGl1zCPKrFaMcCTrcHATE-z0kZ6BJVbqffV9pw1ZD567xgRIB15wKDPyLThBYjOAjNHKSm9iK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPLBAVxsiArRV_4UuuxqEgrNNRfTUdevbj6lPyKo40dL1g9gvl4L409G-01qxA2Z8ZN8paKy58xjW03Lk2Nskel8XKjiW6F_UChBljhnt6I5AXQY5FkCuHyRFJ3kN927sCfnPRZxMlZeIXcB1mFMOJPM5OPQDI_WQ6oCVb2PvYLUoUS9dgQXuK7ibNz8fOJ4TuElGqhMlV7N-7o0vSOGEewA_Im2EB-Ww-HdfoA4XTaRayjaQrhcI1QnxpcMXyik-tL_3FdD3D1C-ULf_Xls9SjiP1rf--QPjAY1I5ZXZFVVb4z1CvMNQDem6RsKh4GCaC4WvFZPvDS7k5BgyYevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKYv7-JG2CD6Q_qo7Z6Pb7oTXUkGNf3WSCtwx5ZtewzaTxjOAHNiLr0POFTvL8-SgHi7-NBiMpKgy4AWLpBOODDSIghVC-kfdFNhdtqt2VID66ntBDQ7f9mbzdpQJCa2mhf0EoY63xzTsjlMYZzQtyinEU01JdC9pY-TR-5RXs4tYzIfrXmRf_JITFXGnzmFN0YZlmlqJLwf5K2J8rxsSkpoBOmNgmmferh8inNxH54iqnLzH9cr9EHTPHWbRqMeSEIYMaI59yDr8RTlq2QxcxwqHgrIMC5a2-a0h86o4GMKw-3JSzEMf7Q8gV38ZvCm0JEndOjQiQmB7RCFNJSTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Z5pV66KoEtbEvvl6tU5Y9Ye4zeXzFE1IL8jGAWpvlCSq-GWXhToTewYiz5XrMiRz-_yMTeEoF7vrJeCpRE-MZZkWYKzK_iNtoghenyuUenrx27v2VrxV4zoPtM0y5c29e9moD9kOQ09xaU4LMIpYfnM0XXzs3KkovlcAVuZih7HmjZeX4a9yMcs7PFig14_o4zRpKjwjczRn4Ftz_hZKDg4itwKasJfaS0OO0Mik9gerU-O6kN5OEOnq70_9fyP79QAUMYzWZVHyK_0l2e7OrGBdzJK9wocGM0P40PiE2rGHIFBa-cf1oGloomeld485aP7IpSsc5sN2MpkFmShBI7UYh7MRsg-MkwHrEwZY2lw7NHbl7GK8zT-PaN6GAo2vQ7ts88OeA3SApV5x8vnCznZdogor01A8y6OV-q7J-xflTIzZOhrC1ctM4XgebxER8RGbDBeF0j8zB8Y7AUWuxwOfEdMPb2QgEF7vCg4FlzJuoB6I9YMLBWf2dDCttnaevJft9WZPiQ61L1ckeMU1sVt3pFpBiTT3KD8T7Ecp82e25YJihI3FOlb8cO6A-bkEZkm-lykQV7qsQ4saf34bdvE3T-pnV1e0VcebkWeOP4o0Vsby4n4PZxsGdgogO9Qvc-ssZYqEbum28X10yZmxy9j-bddUNQlWrXoTaRzGcxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Z5pV66KoEtbEvvl6tU5Y9Ye4zeXzFE1IL8jGAWpvlCSq-GWXhToTewYiz5XrMiRz-_yMTeEoF7vrJeCpRE-MZZkWYKzK_iNtoghenyuUenrx27v2VrxV4zoPtM0y5c29e9moD9kOQ09xaU4LMIpYfnM0XXzs3KkovlcAVuZih7HmjZeX4a9yMcs7PFig14_o4zRpKjwjczRn4Ftz_hZKDg4itwKasJfaS0OO0Mik9gerU-O6kN5OEOnq70_9fyP79QAUMYzWZVHyK_0l2e7OrGBdzJK9wocGM0P40PiE2rGHIFBa-cf1oGloomeld485aP7IpSsc5sN2MpkFmShBI7UYh7MRsg-MkwHrEwZY2lw7NHbl7GK8zT-PaN6GAo2vQ7ts88OeA3SApV5x8vnCznZdogor01A8y6OV-q7J-xflTIzZOhrC1ctM4XgebxER8RGbDBeF0j8zB8Y7AUWuxwOfEdMPb2QgEF7vCg4FlzJuoB6I9YMLBWf2dDCttnaevJft9WZPiQ61L1ckeMU1sVt3pFpBiTT3KD8T7Ecp82e25YJihI3FOlb8cO6A-bkEZkm-lykQV7qsQ4saf34bdvE3T-pnV1e0VcebkWeOP4o0Vsby4n4PZxsGdgogO9Qvc-ssZYqEbum28X10yZmxy9j-bddUNQlWrXoTaRzGcxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvMtjZPPkwTq8_VCJ7sRnmcx0ogGK6VhTJ5O7k7eHQD_dd3SaVRRKYB9BgieliuRgkhukxnIfRc3zdV7eLX1dnAxaMFm6fiZyoX2e9B1T5RaImMk12GLVGhHJcmWLrAk00bBHX56hRRng7bhwx_MWmKaE_m7sOgOvrQOxk5txAm9q5doWRrKpiEjZByu2ZLhrFmvfoNJ4qLtw6yLOfIpUI_legcXi55p8zbsM5QBwf7q1i4EgI9kVYseOX_bMJkiQfTLvaMEqd0adSfzy7BnwjiPuHdkBK-f_XiewoUfQRFxPKKDjsW38kWOUdgVIC4gQpYSxVIYH2fIOz834KGaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUnp6zNZsCOnob6ZUmqQ48vxUEULBKUWaB22FQdZhdZEZ8GYRhkyLINqTH3jk6LljMxEKkyT-lesEBltbg2CaeHKAd5MuNIn_sHh0IM_icuJk_sZYqMdk6Kd8w5xU8BLffd2qj3CofuFnSTITEwFEkdpJ5JTsTYPHAuD8vVnJsGPM53D-lhCQGbYtv_ukCQ_YHWAlKHZdUsXOH7Jwr46CXDuq11Wf6qV4We8wky36F9FQ98Z_aPALZNsWVE3GEIdUWbIBnABv3kIVKSgZcWuwDI0Vt2oOZXDVHq3LhtvuhZ79K9Dx6kgBS7-7Tf9BIWSGGGlvU8KRuXQCZ5QNrQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StBRRFlGmeQMGIUYCoL2w4wxOVOIkOJjBFZX-fJCiiBq1GV-jgym2Lf0XkpdHPwTknM6cB3iB7k_1DBh_brVzEhaK2px1nKKp5GynAT7MiSVHh5PjRFvAUI3a-Zsx9exz8gF0vgR8jjv3BpbE60mAACsp4XxSv4heFefzbVPPwczPkRE7GNEKVEWHsQ6L-xPGpYawsz62lp7JJIn1177euBffiJfxZMatRQETGRnh2opyBywY62ssLjH0x8RbiCpBKm80F-IL0rZQQUTkOsYYUT6r1IvqBRrSGw1cdDNlLdCZvO5iY3YQ4-WNlolr5F7CzFOQEGpZk1xYrdaZifZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/28964" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=s8jieAjWHjpZ2-tTXLl2L5YnhYJwLmPz-nan8fPIHYEiSbyvCnOn2LVKpy-Sk7YiW79wUiIn5ul01O2mSnG4ANHejg-EuFP1gJOSbOUppvV2jt-knBnTuv0df-QtjP1OihxT5kDMofUQHcSnoS3q4CbWSvZ659Lw2HDIlICJikKSOygjsVMeYiyj0cn3z2sn_s0bbe4p826MALYDC6E8GAuOfxKhif4F-m6iBM8aHgPfABapXKTJjx3_hvlriVr3DpFqd5q4fMpw51vrS1vaop30n2Z9WEcxltvtcV5O5IcnzPtg9XzHj-zdEmUZoylR84Wwf-aKxQ8US4zwapDzSxdaHZ8WFMWh_F_I6XkmtsHKwHHjjZZfvdQ6XPX9UQRWaXnBHJwpdCVLyJEok3soWUmz9gU27YqpWeMaXMyckBC8NOjA1xnrLDF5MUaysJZlsc5QIQQ3utBdbfptPsTpvntwjoLoQ1mFB7FrpxAih2oTWhvvXyvshUxmGegYCaYDbub-W7w1fHstIW8qHihKqUCx42UiakQxQ7QyCf5YstTa2XtUXmfxyjgcG4UzTzw4VGfej4iAV4RD-t7Es5pnf88IVxfkCaLbJrBETs1punO4RiNo-D_AJ7Aer_yWB9q1qnA2nsqVtUTpdH0YbwlXF2kco5SUM1tIBuzgEOmH_uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=s8jieAjWHjpZ2-tTXLl2L5YnhYJwLmPz-nan8fPIHYEiSbyvCnOn2LVKpy-Sk7YiW79wUiIn5ul01O2mSnG4ANHejg-EuFP1gJOSbOUppvV2jt-knBnTuv0df-QtjP1OihxT5kDMofUQHcSnoS3q4CbWSvZ659Lw2HDIlICJikKSOygjsVMeYiyj0cn3z2sn_s0bbe4p826MALYDC6E8GAuOfxKhif4F-m6iBM8aHgPfABapXKTJjx3_hvlriVr3DpFqd5q4fMpw51vrS1vaop30n2Z9WEcxltvtcV5O5IcnzPtg9XzHj-zdEmUZoylR84Wwf-aKxQ8US4zwapDzSxdaHZ8WFMWh_F_I6XkmtsHKwHHjjZZfvdQ6XPX9UQRWaXnBHJwpdCVLyJEok3soWUmz9gU27YqpWeMaXMyckBC8NOjA1xnrLDF5MUaysJZlsc5QIQQ3utBdbfptPsTpvntwjoLoQ1mFB7FrpxAih2oTWhvvXyvshUxmGegYCaYDbub-W7w1fHstIW8qHihKqUCx42UiakQxQ7QyCf5YstTa2XtUXmfxyjgcG4UzTzw4VGfej4iAV4RD-t7Es5pnf88IVxfkCaLbJrBETs1punO4RiNo-D_AJ7Aer_yWB9q1qnA2nsqVtUTpdH0YbwlXF2kco5SUM1tIBuzgEOmH_uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVDbQ4QckgfWRW_-VpDwJR8zsCdujS299DczKtj3pq0wU6yMotWvz390Lyh_55cBzj_gYJQsj17jeELQfcKwCCxkU6_6aAVqP9K4mcDg-A1U8etvCqDjDQSgjZijjeBtDRoSEQY2UybE1enbqA4nCt8OXX5hGX9hUI2RVZLs7AK6cZAB7LZZtGNTMLkexePz7DSMHidfbxn5DoszKu4EWYQpr2tP_O88-J2jQj517_cmh-Y1SUe_RFDhwoJdJ1KIBTiCTauAz6EauK5xJNquIn2TG0v4-X-ZzpDNWh8wq9R2exM2Q4U4YCRDVhEJ6SoTyvLqFpMJJp9t-rrFFUqglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnJwzC5Y_UyGSY7lpIbQuoHaQYAjqMBBdghr9aikHOwpSjXx0t84AsWUn1-pFvMEEOfQY2BameXjwoWmZqcdbobUlqVdR0ohMd5I-FFNqVHZ0DLf61QpsnpC-YnJrseQsfI1iTr3UIXqvwcUimhrGguhM0jZrRN4g0xmR1NyDNJqn9TRvwY60gDY1Uhq2R29-j8gD9d5nEYq6GkjtwQAUsdi_1nqKkw9tQWsIwo2GZQwBkFbUw2vMSY9TBMZmik0PaH1XIK8YPe0cxVcd7jrfv20mLVWjTuLzpOl4isHfRezzveT9DQwIKPXWCyUm3pUWAqi5LR5pEy1TO6qYJCxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOcGOP5tcNDx23JZo4j5p4hFGZWsXEr6Js76BlnejWI1U6xbaYxblHBBsGLyuLo5k7WHO93GiB4rnu10u19a5c2UpP0zP0isrChSIqb_BPbNgqX7JPNdP4e6UqHcrXqWVOkO3_dXW5ufERB_yECEMWSx1wVPkguC7xJyKVmRDJ6gnZFV92wVLpveOd5AgkaKXHxp2ZW85o8gGhlS9v8sVPnAqEOuWVpm5rCkjX5HHf4IapIsBhHOk3Qsl8BFr3xjIAtrEaDjN9xP1a91NOPVPTmsY8Rb48zeEjO0PDDkzLLX9AoW4jO9Hzhr1_y7gOalWsxQ9LXISMoyRB6HEb_Vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptk8mfMcJaQSH7SF5CuRY4w2PVmmlJDAfwMQhNLe3McgIbegOcRA_N052jRDqw22YJvKoTzxXk75COVwthmbgzUaHto74qf73oRKjCGVG0oZVevsgxzTRKYpe91-EW4f8Ug7-Im87aaHRpzX1OHuPDZ9GgDTfsrDb4pk2HX6ZVnLJZB1JexAJ9B9hfP3OxL5TlhaCRA4PgJ0mqYlY9_wxH_eCFlFMiH8RQjZSii5EKiYXhQ6xU3zwtlO6FUrQiNghesFO77qzeLIvfBP57mts5FTGXQA20ieTqEXyS3p-a35Nv64ILHit_HAVRKGv5IXSyX3d9tuUKVtFGbKN3MYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMXGO7sAIu-m_ZoRYgS8y0esSAegi4gpr4cET7k4-tdO5YKeo7sn7jciItSMmMzD9Ks7gTMJShAcVaYIwXKXQDA5aIvm3Zh_VvvaQWzn1GHHLc-hmxB0Y2ZLN26PvRfJSAdsuGPWEO_hMTWwwaqciOFi9H4ZKaXFY2nPT16D6n5PnPrt-GSkuc2Pj4cyz7y_yBxSlOSdh_2OR-dpls8R1i35bN54z6cZnxr_NPSuIYgc5GGEyBt2KIFjlROjB2B2OmUiRVeo3zEltW3gSg6eCsQTZ_jFU0d7OzCqBAapr-9BS4Gcsls-O8rNCE54EJeo9AQRMppUR7D0cuMyE3EtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYub4oOmsQ9Tu1uislo6IBt67rFVzqCVZ761QT5ZFb5XprbuMDd7oCM-tQS9uamIwomKMxr62gC4Z3PXhj0ifwNKkT2moOZo8CrFHP4K7dkjV-ikc3uvz258S9VykcNPl-SE8vJ2XYvn6DkgNPj9y6_zDh0q94OcdWmI_OIoIznFznNlKjBqO0G9mEh0YHN5Kbpw-yKRnmuB3zLE-VgAYjM1tINh3E4-wt8PJ22TlVreg7oj2XLofHhnoRrBA2A2vwNRlnsEc71bh6YZX6mbmr-1wmY94rH4cCZlB9sa_LdlVDtYLlWBdGKWTXGNigY3LlikdvBB18_mLm8E-YLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVggffYqmowiUhrXCGQC-DKdtOjFP16ons8gvNLDbDo6zadsJpRA_W0LnXOhk6oktKAO_1ZYB0s0jn1RuAf2lmW1TdxMELNep6bKDvUrkFfQjQ_vatec9tZkMXjeRCkqjWQEY-17W96IKJ94dG9ffQR5DUm9aDADFxq64YFq3rEJuQpsBK5m9nwA8RDW4wA_B0ff6QAttmanUcOc-D30XhkwtVM9ohv7grWr6UgP6650UFtuLMkYCRo827PDWkyrCV7It3BuLchwTq_b0sqaG85B9ELJT8D_71LUP5FzlMYTYaXOyIIqEZVGSUkGNEDNlxdHtGU1YueGoV1cbswEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4o4NgxKy8RLSc4tX8s4erVoJfZO-4xuo7bsbR3f52xafhiaSBzc4p6GOvzMI_wbPaaFl5Xk7khCayPgyQejckn_PDKiGNP_6nML6vj8i31NrNa5FiyAE1zhpoPbxE2t4g6LXE9KfQD98OTMI-dm7aMbX2qnH9GNNljMZT_mwhPSxCgHc_ZprJBdWrxQvk3DGdScwPTi4U90uxkdZI4FOZDEvzTPqEPObLeRyxe3JAPdfx75wmYPU3-8zxIZeIrcxsjqVyvijawLMzYEmUgOLkJXQgS2lGUQFjdMgTYdRtUSUBBww-D1E-XzUanb1TJnKj6qoxzcAb_A0S2htybPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwnWSdUl70tFw04STmRNvYgqLcSIs1jnpzSbXAf6oECz0rhxbOllL9Nwp3E91q6mhA3yqVlQMG5ztICYkLbFxhNGmXBGWk4mbx4NSQ6AL9kX17USzUIk8j2teehtu55iAWU94CLJtWZu3-htsodFRsI22Te3-OhJLLIJWLmSZExhi5z0YNahLz9xMFGs_hTWcTBMPyE8EFip7vFCl0CeBVwue7Jb76E3ZRrOZ8NrVGFwW4vpauzPdG4C8dsUJThzXsFfbMINXCJrwg58_x8U4gUAJVrHkp7SdQvO_4TvmXJqyLrJ3R1ujEuRGqNWmj0knxdRQk5Z3jbEFldKN2TzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28952">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6gIeHfutL3M2ThrTUN9OfTzpzuK0YQ-8ZVbp_A2_mNKUd71KHTF4pE1FcBqQGbE6ThcdyJ7HrIm40gK3-V1CQUpaqBFnwYB4-WuvmLjvo_3fcyXR6Jpp7tsbYdHVp9wZ-v2ROUUynmwX9qh98rYPRjIl2T3NKbOsE8PL2Lz0Uh8Hc6mGa-oZXBjJPLjMvxLQ-Y8_W1quAy2CR49VeFRlMWS4YpwO4jAXdBjNoRjQEOEd7-78BJkrDftnkRZ2M7gciwcI-0KXMTxw2nrJKTYrJVBqKslEiQSQDlZ0LO5Y7LWTFXDD9SQx-0MmpFL7XLMuk-KFHPNUuRf_ibfVZu1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین‌مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28952" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMeCeHxjUFOEBOrFTgB1J45cCdeSWo9cTa7KcKMJyL0CK0WP5APxPf9qykWTakWQateY8esMcxH4RbT3qKC_tM6EtftMp_3gq7g3nMddSI4N9N98T5zH0dQ73TEBhyk3n2PH0YjzRTgqPGXPaTP_wR8io9MGw358AFqE6-kbaKBH7H3cJDrZkS13Prn9aTbbq5N0ilm8rRvHPEO77uLknXA0ERk5W2H8NJ58fTetyi_6KZRB4pRspsD3s8lFx949uD3Agl-owFp-WRsWHX2a5ReKnspoR9o7MI6T88XQy-5n_dqP9VrE9FjrUqDwzVjVwa2o7lQQofot7M-0ZrdlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwWdvw3104k1bbTkIUYF_msaKW9c0GEd9xcy-cli9wQaWNiYuBZR_Zu07X0beWVDkAIX4ZwPBXcZimzBEqE1Tx7K5XWbqj_BqTSW4jY6THOslEmifu-q5r6053ePoP6v5pVJSMceshY_tKCdfHUHK_NNLzMuecIJxA4mwhJyXxXbNNnc9SkIwAf9tCCdxf0LM7nfc7M9hp_rxtIhtawN8cy-qje-d0Z4U4JGVNFdMQMJQTN7FvvOIOgmw05UmWbtFj81ZOhANFRo3guCHa398F78IKW0uGkii1VWFTjtDYGW9Da2Hk1axwhDV_bge6QT0sbQELRBoW2MREmvt9YuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpJ2FWG6u3jokEI9p7VzC8QPYiM4hOs-vRbGV03D1u2Dgk6Gr6s8B4GbDkY5PNx9FS4-bZ03H6xyMgAVFWfUZvCLFklw_elmI1X0SNLhj88g1tBYJ41y2Qt2uYtBj9TJasxh2BIV2duVavkxcEU08z9h9bnUEW8UakF_lAzNJLq7Uv0lWvSwL8mqT6MrAXFGzTv8D_mumA5u479Vz63j1I_U5TJ5hxu0q0cYib9h7Lz4_agOXuFzy4iHEW1yXCYf5Yfh6umZadic3H_Py-kXAgAWK5my11ujJItO3CeGX6tY9qyVxryGwRprdo42bKStJqc3oTkv_jDuxF_i9i9Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdGucIQDVN6utVJRSFBExqavBnZ7jFTCuiirwK_gxnVpW36Bz-qmtrM-T_UzjfxGbmzLCR4lCu3JdDONQI3MiXbLuleTCnMC3CroYm_eXxjRyqJYwwziziVqgBSAPwtb63t1Gy7HOYE9nv4U7eCRWi2bjK7JBAjpCYlHZ3I8m4PU04P7q-B4Ds366W2RN6pFMdSF-zhNdmrI-Fqm-HV_eExsvgRvXNKqvrDammCl5jHv5WY-YpHsTvNkp5yc08f1eMxvHm1zNsy231FsfHFRov9bhdB4bjxBsKqXLMDB_kKazsUAjTktHxMG4bhn6KYaaqvSxumeILjZaQ05mkGxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WY03DxhVsKaZIe7UUv3BERusBKYPKRJghGnwLs2ZiGnY-0rNt5KKKC3KWiokIbrW82DVCPABfcQ1n6p2No54OB5rn3Wfx4_GwmUdeGzZ-KX8XDFBJxlJ4P_hABHBzpgrGS51CHDzDvchk6O1bDdSBibhEbty1xNrEEcNeUOnlBWuMbqKu819oxl1Qm3TEzEgdkp92jLxF5mMjMjKz27WRlTBoXMaVs3f0aCMMUiHCmU1_YujOOoZdqqdW18BZ-NBztQfF9A58sSmlk-0Nbp58xPdOzoYHCPBxjyqUjqi3XfheFyvlMWJD58P0GkDmc0INoeymox6cSMmNcOxN3LN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKqtjncBQYablzamVCMz9vKAd6b9nvCMG5u7Zo-7PpSI-DwnMKVkxOx3L-gCPKHhnwH3fsyu4UYlSwFPpcru5emZMfwLBiTuAnFu_iGreQHHyxzd0mfXxjsY9-NiKtE7JG_bC72onrCikesuugz6TwgXUhoRgIJlJh5b_ZXIN72OtCxlDyAGtSEh8ztxF2XQJOFVWZYoPpJYrwUKPLp056SI7Ol5G5gowFTKAJsykUq9XPq9AAIHtfmYu5Dv0OUagaqLJP_8PUOTsW9gmXoSrtWQFkiEeqYG9zUntsD2tzQBfVMbSTIfiFzYL_FSRh48kWhYaXYMOdgtHg7_bHdJBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJTNGFwXal1NqqayPoJ7N9GAt_J28wa1KGHoQTdCDyO0mp8-BS_kxJ3NopbaK37im9S8Oc7xbKkK2gAwYz2EhKMpxcHQ_BQ1oYY07ySMgsvOqGQTjqUT_PvztJ41mxUTyMXwg9WyNEjMx4c5ogbepWV_TM0zM5vpg2hKIQE1FUGr3sKQ7_WOJKU5vNFGV1bw2NyovXHthVu-XLgoTgIi-gcb_Y4gVRfKyw1CaSbeS9hD_dDzFAATvz3vOYGPLxGfLtVv4vgOZePwvFsI8cAy7Ym3tGNtYvD5roEUsljB7A2i8nzjf5Rf_h2hYRT2MxQTJIRAGscEH_gDAC78E_rVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9SLSyv1g81TnkCR31mjEvtyVJagge75LHX_9z7BxnGBdUABYWZRnahdTjzK8sgxDnjKgNivOilKBW4TpoJxR92sw9bxhMWm_2G4wrqkU83vAVOBgaNOL2QYWldGzHjFcQLVArdFvlrKM-hl6IJeqvhbkmZ10mMCCqlF-BA5cq7xpzKyPTq3NNm9ENJEVb-0Xu0Dsw_cPzw1X71myPXEuzwdep0Eye_LvEibOi9Gp_c_dVbmznl9HoyEsrEbWN7UOKlMVh72p0luXZGt_XfySBqb00v4nKuMbOCMb6vUNU3Dojts4WPqkIaOLR7AQ7I5vZt0iGb6oQ4ZjKd_kSvBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaKgVYXMxW3PwSKTlnqh24qn-RxFjNOT8THlDGZ6_oNGVkM-ZYGjBUpah2uwVV0PPQnvxAfTxyMbTxZpLFl585yIDFS8gw7kQvQkgeE8VJVwv3JqBSm8WvWUr3I9LhFQtTHElFBg90IFjA22jEgOR9_YcAKyB4en2nnAwmNxASA60AvZs18CV68yK-uQ7W8LhxvS2APFj17KwslK-eR0LT_H3S04vtOKkkRTke0IXM2yyyXojHCAEpxnVqjk--d5owbxVAkx0YKklJruKPuA7ZfgfqYWVzg2jqD4uz_iWeVQvx91sybSw68GJ5CjiKjqCDnErg5MWftpyIEb-_A1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCFHZK6Nw2dcoq_9de2WjY1VxVXvEhEtNA1cSiTJF7OTeXxdnqnwpHmkLy2s268iZjg4KT5tDSuUrD2-swElQCK1G3Fj9qleNu8qQ7mhCiFr3biiIU7YR9_w3o-14UZeKHKTqjmIAJAdeGSll9jSVOpqQdxLvjdb3yKUeAhHJUiTXnS0Q-XLanKmrTkHjr8vXG8LWw6_aRc78bXBQ6EHCYNx2-LGfkpelK7gFRQAGfKnpI2qqy6FbIf21xBfcRbwKCJsz8WIa79s3XG8mZrDBlcMDEIn7qzjDZNh9v1AZWkpkARNuPIIYVGoQ2aDWV4_TiWgs8Xi3RRMSoX42N-OOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCgHu-puo_wJ0oZu5TuPA55grJ7aEHyf6UGj8JeOJlVVZtTK9iGV2DqVQ-k72EVWoAjw8bn_jwjXcy1NCG-68EpNX3-PkZ8_pef5KtW_1ACImUgiQGE4W0k5u_QdM9pD2gCNsfL41OjVbOH2Xv6lmPZKdrZxFanGAy1V61uqOEqGAK_aCPaiDMxh0TzuRbNCvNi5P2aavAyw6lcgU2DgKdxwrqbnMRDehvqAOq367-ffmRU6qRkAW0cYMs2sd6DcKkiW0J121Tu8sOuRGR4grnN4B7-jB8Lb8t3wFLBbtQX6K-mgCaZkFx6FyAvRFRFVm63GjmcvkPJe8yRzNiG0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld7sRZ8yl7CsOuKNSeYfbh6vD5H2qrR4wtXAgng8T4LWoM4KHghi9RTbvhgCGZgHxO0_CrO2VdYsNiZ2Jf6QDGWgnuXDXZo3m2o0baDa7fs9xT5Z2EkuZjbyre7FL63tSi8n4YqtzVmlUgPvdKquS1oKBUUTIq6Eaq411mDueM2-4_T5d1TuyMKi6Nu08q2z-8a981fW7IfAhSCAZahVwDqHP4JyPHDXwiHVLP9Ni7bTE36dj8ClhYjekMzHXgN_K8eeYU71Pc0RCMGCHLDlhxva2Eg0F3hA210ZU4A5GnEDkG4u4FYO6ve-i3c5pA-LwW4DP7C858crk6iDW5gm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJTRI8ltikY9Lx_i3iyWGzXye5fbRBzsfu8aBiWvxbYSSa4k5q4nV-1yJK2eNeDmfKxfhp_S9IyQxFfCVh4gKLbAnt7bEM1fkGNC4k5m_Z69B-xrxoQ4p13HaYLqF3YaBVAmfPleDJo3aKNkX1E7wFR9Pa4eb0EJMoHBpdUIyng0puKGoIM2w_h_KFWWG3k_pPJGfXBcPOyhYo1ugyqPd_2xyftwLKb1riLuZ0KfYo6AzZP2_M7FCwzVRSG9JaFZjhyB9umhY4VZO4AKV77e_bUkAJ5caCL8YUPqJF2Y34jKabdnv0GHVy_ijL6v0ULyoQtXfTger1CNkAcIY23EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIvYLexWLRsq3-DrVonIcYdnNrPShYokVnbTQWtvRGt2p81BEK-APS42-CclqxPqaxVclzRZLRtrvWFdynJODPcPG_xcMZ8MM9rhww0iwmM4QeNsr5oNUxMesoUEaP7UyyRnJUlkRhaCZYjSMEC_RkWE_cfuusFv3LYypQeayDw9GDYPb_vveBAru2UQE_USaMUMoPpFZZr9Dob9nJDhGjaJ2X3VUQm5c66Jgv05ls7kZov1WmF-e0kZhXAvYOS7X8Gu3SbBx8x8W2adMZaTHpD8fAHAyYawjmo2VODfDe8fGFC_8zFgUKgnUltE9eaMop0wMyxpJo7Gv4_rFeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg8RQWGvS7c7LgHfkOtijqBEnV0cDau-XxYqjUT0UVT-vUtT2fraGKATYiUOj_zlAo7nWwmri3UY6hLuvVo2_awBk5SI-dAqv7MdurHWGTd55EHsmWkw9LnTC8wC9qAJhZRZgAN2Pw6wiXmqlDRf5-3W79cjz6ymZqGRkqLxZb1EkomCcJpwhpdlQ8BL1QyIeI-8IiSWdXIrQApXdjCDa1L5k3HttrtKDkflBRskhNTzwXYhbJ9AzeoM_ts9VmrqJwKt0sUVzdIa0ueETS2QKOYNNs-gONVpAkn1NohoGqQYpllXFmeYmTBUyjyIYlGdjrTvEU0ftgdLzrBPCnrgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXCD05ycz2lT2mHJUVdA1yNrTjh54iiu66lk5Jz-rtqiDWRI-RsRRRQUVuqhlU19TADW1gZa8JcNdsFa7pm-Anyn0FQPOTi96kAwLQm7LEyWwSsEGaPzJ9A1tYbObAo3roiFI3JjLLo19QXKTu8IzjzGpi3E3loFwBlGxST7cOc6Tye7lMJeaP1SQ_FsxvYajhZLVmj5oKSAkeKQDDFqqoyXrxbriK42eLttntfwLU03FPdtOPP77oocor03vPx3pY9vjmZtaJsJLuFtQj-GC4X83J3feAYrxg-SaJtPglhTtquY_aLTt6kpnEkX6QIO6EYaSC5iNUvRyPA7Qv-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/carUBFQQ0x31e4Z8xHFNKvMsWlYzH5eE-gz_P0edhCLb4am9AEujVHxTicahqX8dUEvTP516MZFXcPoa_7Qzn_crEV7fuPKcpH88TGDa2plswpI0kRQkIqif7wLgs3MvI5iDGiao6FzIX-G-wkoElQnQlK1qhUtpxaTtUI8QnCwyHm82gqdn6f_zEA927_SGD1-8asmKa4zhTPVoxjWu3h0Kxv_YidQxE-wuBk6I4K-JT5pIDPF5EfHw05ZiPcPRVkf798bMSMjdZRXX8c5onQsU9IrQl4gw5MZzLbFhlcCGPMzbXUyb-E-IU2r7k63galiasHLr1mROBo57YRYz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqEVh8SselVcL5qAC170N9xFdE3Lxjq04byOt1QMdP89Dkt11RrWWdsmLgejeEX9708MWo07h9smCPNs22KCsLi4_f543rpvULf8_vvIhqgoBgipVhWDdFIWtI6wKJ2VL5ukkE5Erw7PsO_uujiOShsfdnhU_5fGt2BUF1I9AVC7W6o0CpRpNXTT9Rj-OhzSG2eGvGs8IBp4rU2Bm0nYlTACWKN5ZXEgiv5LTXSWF2bjAlT4hin9aarrf4j1yBIBEp-O7ObAK7_1LmbRt5YztH9Iaq1DfkckIwjBaeC06wSTdnW702Q3a9HGMGMT5SE5W0aHRgPA5utuPZlxs1x20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8Hm6w0MboqcZH540oG34XASLpRQOmcSQVoKSQiULI_iQOqyYntmnGdL8jxQEIZ-VBRR44DFUYghk33E6L5i-YkUvo7iCRykvqwcPWSaTHXwjLTpsIn5buoPJ6ihSqj6m_mVFu1_ViIUY2bnAu4-f8lykyCuIHc_4q4r_l1Iqtx_639mJ6IcbOpkeZvJb_BlXCZMhICmKb75W9148_FwoCmJSOgxMjzbZWiRwvH84bMZrgs6mTC9QGrkSiofw6yJ78U5pcnilOTbe8u00HsUsPJFGqYSnjbQ5Wevxe86aS5HxIuVgbfZuqQXJxE7zExkVBNgSI95pGIB_a44cGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwmmE_yi7rFGRhxW5XVDsSdAOOzg7TTLzuUcKJXgQo87W7XGdbDM99N8Gb1NBsogSvUkZdMFSCVvlKFIfKqa5xVPCFy_p3Ij5oBODVFFGT7P5iX1a0EwJyfcPDKIcIwblwDa4Q-ZO7w-vGgnaCn_YEHfs-m38A3l340R_WpMsdH3bCjO9i2EUjrre8lVB_g92RAZFImR5h_pkiP89gHjTA_XPkKfeowDOMravVyAY4iusGn6gX-yT4aoCEbRnBUmVWZ9WcEr9vqXUk1gQDY8fTW9Upd_yKVDDCWboH2ZeueuPrvNzeEjhfocnKoeG3pB-u0z1k41gWEbp0xTsDgAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAgf2k2NP1NHIEdZu6W24lG6kjdP44u9It2oXcu3pg0r3h_PB8BTLVT0mELQ1v-fpT8z7VkDL57oZg-ZT8s2j9jvYab7DV8YD23dboc9D0eOfLmdcUSGZprCA9eyuQpvLzSik-BHa_xWPKv7NqPJhKf3Kg2uBgreSaEm0YnVx2cKM2dDVxPQRUe0_VVXnFUeO9zL5MBwhT6lQYrQtdzqVJcK7seKdccww98Lp0eg8DNbHQra2W8jiZYnMkchrgWJQY4-AHp7t54cG9wrJkgJ8alK86-YyL6kdZXDjRM2xyYCrtamNnqhua-F9rweHT2XbPfBqil5-g0PIeYqac-YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea0yh9g32ObihxuJ3zl_OtyhRgiMgUrHBfMojue_0RKqOpNOr_vTr-zp--QCylfW1uG5JzLwCjPQ3HY7RrlhCepOQWJ8WXXVAB98lhVTCZbhHjbqS8I6pnjcbpamwi2X4Oh1Z02PMJqvYcHloezRS2K8szLKqy0YJViUp-KSwgk1Qmn45-lI--Mt-aNVhCw2ApzT14qq3v7zQk6s1ByRtOY8W20AHCBR8acEoQPmCln7Hd5oyJv0vvGgrFItrzkSvLTACQD-X053Rjdb2lTvic7R_811pOrC_97KBIpC1Ly8PVKBF3MZw9HlsT4VgJoArK1kTRThDsBuUF6yqoPbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plK595_FolqhqolxWAa81B3ayipEIqqUTA38oB_b3_1xxX2G0phj3Ma6H4Z4cB1zdDwEKQWL68AausKizWSfCx2v20CLDoCTAXzLMrl404dUvxNLqkqFi1OJ0PePyvYGirBm_kcMCDTJuadxwJFb7Mskx76_NDt1Xwm23YZsQHnbjxV3qyY683OzufgcR9KWvcaNwfTQqeMNl7sl36FMlwXoLt8BtsCL_r52p51DQYLKUZ3OWO2EXwaTNey5JhrUxCR8M0ySP57jtvKGarNlbxOkn-Ioxea7BDCLtIsYH9WiV94HE8dddnUEtuhXQNESQJTmz2pkNS1PTuxUGwznfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l88k_Bssx-Fz51Lw16wSjZdZB1GHsFVfXhAH_PnOmtCfbrkkciojUy_TrXVbvgfRaskOxAJasHKUHBvAvO8BiTYqFsiA-X0bJpsj3P0s5oxFrcXb_6ZfAnv186rUMvKnSadYujrCmfyjYCFR6LI3URszNqhskgXXfwnDoETdJ3_w7C3QG5ae7ZVMIQNP0BxnPfWa0BecES6Rnh3uJwNsF3loShhQK9XVk8ereDVs_f070afmEw9b4AMzl_DkGxuXrhk0ok4dQWSjkup66y5Fq2ofsn6HuguPm6v7PaNJWhXXtaxGDSQ7locZpCq30hf64QoQgRqCQBP2Q4BShaC0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR9nFjudbSF89j8tcp09kPtjDPvpEaWUzjcfvM3noBycHP1dr3pqsCyxERjOhlord7wNw01EpGJyVj1HaglV5qvBZZ5m7gMZ5X8M0uxXJBobLT94BQREuq18sV7Y8p1i08mUc308KvQ188KaqENYxH0PeQCWhuLofuKv1F-8lfrldu8IUGzi22ddxh4_SdHEr7KZjDh4zbj9sBa1qL5Lrwkp7kqi6OVluitBcJhZ63x7xpEJT4flhD2oTnvKb5XXhQv1NFb5tLerRTGxmcCInONMcqWSla9YMTmoZyBImSxyjErG4exHAkL1k2q2vPcdiiq33Jm0FvHAm0WJ7YiBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb66mFNbuBo-W0kaQVPLhsOwAu6_gnc8ji9p7--S0yUNXCA-YhkbqnwoTeHDYF7cDuYD5K9b0gjvgXuiOCIyTqBSNgVoZf9Wf4dQziISpbWHgI8I8BPhcb-x-lqfFSraJ3xWQrNaMzyyNm4KxjEPt-oLI4tayEDHj68XCqrQnjhXy6uk8ARdwOSi1ppflgNm7zQ6Kaut28z9I9YNry2fIKLMX2h1oRs1VU2eU6t08Var4E9R_vHnNcyrK3zsm2PptOBLwycq7OD02mOjbG3uUiWar_2x-ECry-6fQCzpLTdbA6a15Nm35F0YvsHGDC1lwFY7FJPnDyJWLQJ8j1CTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxJ_ohiewCFXLF4Knc9r8uzN72GrBWfr7jhxj84Ptp5WEOSy5oRMD0FkFk7vSfCYjhmMWDOY-oBkkPif7fIQy4vLVDc-Xs7ovZojzurKfp2zPppJkRk5vuyrlhk1Rz_zXddlw-tmjCfA_ysDo7mW3GPyR5CFnomkZit_y9xIzeRcsqnfBFJSSXfEYmmiEj2m1ykZnZzjorcSTBDZamexKeVxbkgnXlyO75i6tOpnF5K8YRsqId2HLOi31IZDmLe-iNZAuY6ysl9HbRm7EQ93Iq9CDf-_rYLrI7hZDk4baxpk3aFsJnvzC1LQShXdRNKyeMPxXpliQJW_1y-CB-N5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWtOpns0v-FvxrpbpXWfcOh_Bv-BmaWXzA5d_Wc23LghdlDSreXLowur3AbFY2dAwIhslHVKw9f8CuGKEmB5HRCBIlrper3cJkWXSrOl4qhQ0VcOJgoXIWXljMv_6Cs7UGllc4HAlrDy0fK3Rs0ZFKlBDWlf876a47KwIJOURtwPqqu3flPRD_u5MadXq3nnZRyHolWikjXzE8tzrvQ1onL6YMOqJB0jRtnnlMLIbbSr5lKv5F-r7D2jNeYXdN0PlocF1L4JJVvz_L2Od9oVBRj4jNrx-4JbCU6lCemmYIFds6B0qQRo0w1nYvr1Fn3DDOESn8ZfoJNvasbriRWFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNCQU2ApvdV7M93lDJ2Hs-oBcbanrIjHTQyVeZXLcNvbCtrUcAA1xu5VtnXNhP3E__Mtxy7Hk_J6MH_yzKnp2ZGLuy7_oB6kzzjjMxUvE-Uv7hcZ5_OCK58coBjx70YbLMjh_Bqduyw9bL_7i5B6bXwr6FOKygpfmFD4DaBo2TL1C3eGf3nHNG28rHgdUOqh8paYOZPhcOUuaZngFeCYUsHOtuLQDY9sf_WLtNehRg8fMuxPY7UUxC-rcxo6Bn1K9kL0hV-v_GChAz-Z3reT-RYJtXcuPCWMsOey9Z4Acshu21NPIyh7JPi-UMQe5NEPdrXOjGd2RboE0KE3TG7byg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql8WIjdho0V1qS-H3zV0I0xWZpupQ-lYamTZJf4S0rtXtcyAIXRfmvW0aqryP-lWrYTLhC66pbayQg_2ICsXIrkTdFQEbKxU3A6OB9SEBMN6zQVc-gKwDZBe3rFDju6xLg8U6p6b80wtDg-WbhToroLyXFVYPcBeKl_BGhi9EbM49r5TspC_62Y2sS35E0lU3sZwDzKyjZLnlDpL0krNas77WuUDHWUcvdYDcZGC32xtcLXmcgvXTf0WNtnmGa1tlEBxHB1z1UdfL7fAUydCdm8J1I3WPxmO7-A0wAzbOk_FPn3WUQTd0PJ4wz99Ofq5FSrmgD6GHd-akui12TDLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhuq-dnwJLFF_78SyUFQ42Xf6pExUO_hmN8-BnWlRABNZ17gBgWA3S699YRKo3sfyXrZtdESb95pvzMautxEEcfwrCNIUfMnAk3iKD0n6Cuau-XL-hqaQoQEJOw28ErspIPegx_l_4KgG8Q9jk9oYrruk4gvfKIYRZo8O7wu3Cm_IaC0hsmrfZ-K6ukqUPpC8XbkKP1cKAdOJTBXbMhw2bK6MKfL4BwtR_BEgHfDkgdpko4-ojUkWZRAvGLU5zj1b54WKJWvWqoDUWhWql2eRKYGa91wY1fTP1XNzotn1dJ8Eoqbax_WZ3tbaO8jFxAwh2dT2EUSsFI-sZepvmeFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=MXgmAStUD880zDQJyF3RqkxCJzCiJOkylVLxyq6hfml7zudXyJ9Ap1DLVVK57i_Bip8XkahJRCX9GSmx-4EuAmU2GYd4zsAVzvd9_-jkcvEyHUGGLGYO5EzAdXL_VpDl7eR3T387fvTPvE_2boEEtzMfZJUqPe2DwJffVuIKhyeqit_mAjGI0DbvwD9FXiq818AXlm_XtQ3nmjFCBDnMqaVe0xMsxr-GpykAzI2QSt5QAqCTHJ1rQXHVeUfOFngKN87GYKLH9g6cE2GEnA3_cbsViimjwK1OwgRSnW1vav9CtQfX5dOIkckvL-ExpGuWpQyfGMLBXyscM028fqd9YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=MXgmAStUD880zDQJyF3RqkxCJzCiJOkylVLxyq6hfml7zudXyJ9Ap1DLVVK57i_Bip8XkahJRCX9GSmx-4EuAmU2GYd4zsAVzvd9_-jkcvEyHUGGLGYO5EzAdXL_VpDl7eR3T387fvTPvE_2boEEtzMfZJUqPe2DwJffVuIKhyeqit_mAjGI0DbvwD9FXiq818AXlm_XtQ3nmjFCBDnMqaVe0xMsxr-GpykAzI2QSt5QAqCTHJ1rQXHVeUfOFngKN87GYKLH9g6cE2GEnA3_cbsViimjwK1OwgRSnW1vav9CtQfX5dOIkckvL-ExpGuWpQyfGMLBXyscM028fqd9YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjdSdCsfGvXINsUdbZbfr9Ke9WkO75ubg8Y1gUeGavOebbEvnY-jfrqH4LYrOory6wjc-bQrWee75juyC4YyLk4qLDI3J15rLbQmnlFnHWCfOZxVczcy0QtbC72oIVVlUEoYl0amcY8ZNTd4MfMKxUQ40p9z5Wk1o6X1HBKJNHX1NGjdcAdeIl2cIKc5npw466DGPqI1UZEcRIYGrxDXNU8T8a5DqRWCSEcAuA4Oo8ufTFVW9fqUbizKvfVE-bAbIXaiI3Hsgsj8I1DvzuBB0kBBXD7Hb2Q9MASyPYl_eWsNAqfRArNCdx5iCdYFgne24qFtDZEWmSQzwuwQirvUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwj9UsA7r9gdy1rfknD9Jj-qhOCvlCfkZ0f3PUoIsZH8pp6zSf5z7cDeKvUaNMIbFk7JMvkMl9mIBN6N3yAqH2JbdvcgQrt38x21G3plFlCavGFD6Dwsk7SXmmIp4yKgvSGChyTXQis8t5gIC9vgk3lcCaHJ9sihdwC_-yn2bKjWfjRzubonlPeGPHQ2U86Rze5Ju4IYTkCUv2TPnRGymiwNhp17hPfzxbNBxH1PXw3ZLc9kIheKNj4HJhUMVfekHFueUyaUhWtglJIrQP_lyhIjhJDAIthoPvrNKtudosT2VFw5Pxvoc_gbs5BY0HgpY_Sniv9lTAxmzU8avDONpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkRPh4ZG8Rr3bYZHtzegrllTfq8gYmYLvegpJKKhNm6d-pgcZkhRuruU_BhBMm2pPsYADvosSDhkxMbtwJ2vGutRMDrf93kwrwd1hJZpX3HHoIk5m3StnZmr27E1t9fDF_XgwWPw4kcF86hh5_4lMrRHtPC3Y5hDNnw1Q33pkItKuKelQ-27zlqyu8ZJn_Bjmm3WUMLfQnktaHlCUc_hihFGjq1UJV84ruVC0rFp30iuYDyH8MT8-df5HxeLNEVw2kz1WO8mlKnEeQLAkQfHeg7w5Zaqe6hJW-cZ13WXNIsRdJP7Zn4fQ-p-5NhvQYXfDcfxNW8zCSvVCLAMOXca6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttmXOahmb0WhJOko9SBpPMVskC9exqoJ6CVlB_OA_dqoNrL9-7PUQK0APgg4M2Oae6o2SQ7ElYDDhYGnVKKaR0aVuzl840yflgLuADk83JlIl4bCU3HpmTfb6-il2khTKLNDIjEB0jsUAVgJWYgdMSUBPWwOlsB2ClmLdZZ5mSMqcYNg7u3r-C5OsGLOqUczIZdwgdi-0gTlcVN-6tt0Lv11-gb0uGkXy6847P9oIRVPxK0kfFyEcEPJEYuEX-IOy1xPUItHxXOZiNk-V-aoEs2Vu8fY8lTuCVwaPkLIAYlH4au5UCo37ugjo8uPQUn3OubHPS7eHyWcd50fHBYy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_0zI06ZiKrn0nRi0Ys6CPZD6JcvfgbIticLJeAKdQTTIQQmGOX6aigd94OaGlEPHoCG578EDNeEN4NJfUKJU3acal0uf8wY2TL1pTJ4L2TQs07wsBdy-afOk83gMJU17zh2vmnJxvN_ueFA0Uq49CsOL27kAzyNk0DqO9YYyJJCeXP2IDz5_PLjmdyrsqLqzPFHGLjcB0F5pdEvEeHjyutGTnkya6vedgJbGF7KSf-bhee7hNj-3rM3Si_qmSe2SPzIAFTrRgHPTX9ovHIAQ427HU76K_Ip_7rDNUbOt7xdHpqgYYXJc1lkK7vtSSYdWrhFZy65DsAkhRCG7izO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=V0BWnOjJJnwYkAqMjRbKujANzv1JfK_mnW3Rz0v1UWDjWZTXljeHRYjk7KuJuzD22AUlaKWTwyXRp3xCKhBjeszlwKgaUc2FTDUQcHxnNYfkBaCl-iM128JuvW27zOfyQkSfeT33QO17SddBzjokH4wj7T-QI-ty4EBB8EbAq0zwZ_pGno3nYrKcLe0jj2XZ0jysuei9dscReMe7BljnWBcnevBucMWw-Xvz4e7CeEP83-mfYrHMmmGpuc-ejjoA9aw3SFxzQIh0Jnx9n3fqXImt7FRM_M6ENqZsj9K4BGxF400qxaLxlWx-RXwJXONfhfcg0LCJuXLKslLzuBV8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=V0BWnOjJJnwYkAqMjRbKujANzv1JfK_mnW3Rz0v1UWDjWZTXljeHRYjk7KuJuzD22AUlaKWTwyXRp3xCKhBjeszlwKgaUc2FTDUQcHxnNYfkBaCl-iM128JuvW27zOfyQkSfeT33QO17SddBzjokH4wj7T-QI-ty4EBB8EbAq0zwZ_pGno3nYrKcLe0jj2XZ0jysuei9dscReMe7BljnWBcnevBucMWw-Xvz4e7CeEP83-mfYrHMmmGpuc-ejjoA9aw3SFxzQIh0Jnx9n3fqXImt7FRM_M6ENqZsj9K4BGxF400qxaLxlWx-RXwJXONfhfcg0LCJuXLKslLzuBV8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snBRZyN5QqNZ7B4qKbOwcsXPh7jQkKBZffBjZTIDVpY4fQrZzWzCx7uSW3E0tl6LquLnVqJgS-4K5MzCUdZItReYoRT3QXvk6VtDPjDm_b0ygXLayykt_3ZJqz5kyokV6zdKyO9QvR-z8QrSPoAaKjSH0B6M6jQG393n6KQnPsrhXfrhdN3BC26C9BUKYomQIDzBF5i2Xp5rJaHlLxreL3r2sMX6EdfSBFosd-eVh5uv0muuJ-qkT_RFA_P3flnNYoCY5knPXTYsgPCiCfW2z6Nw5YWz3p6_8CHBRX8flSIt3ZYruMY7PEIBWU5gj3WEDvViOAh4KnAZMHkxIp7qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOLsvWQ8iDmoKfEBGgRimJOEjIVfCT8Mj7_iSTtzD7d-lpQzACyZt7XtUax3HPlWS9J0mcxdTTrTYVetmdPVIS3TrmSzMpuJ5udgEBsswYuZy5J-nhTqrK7-8bjKAZebdxOBBiX6cME8Wrev0Zldw6DILrruiOiicYhGI2f_l54QjVTCVWTTDX8RVOAT_ACN7GB56wxjUtzFEwDTZAB7PGLwPixzbnlvFaeWluxYGaDt5Hk3khv2wGgMoeYxLe1PwvFoZB0B814aWFNiE7Csn1QGcp7BCad85QaVY0QablDgyI1_FQ9f60Ix2-BP6fssfkceCCN82meOYDRv6_tyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRPtH-8zkJYY6VBK0G0FhbLFIU_WUFPluk23eX-Ggo-H6PLX3cKg4yeXAcAFQFMsv6i5HsibyTM8zWOdTUSp_EW_6Qi0-O0IaxvsBdmz6T4SzGCtUnBXhppvSOpm816vuinzeNDlN5aOsf3BtefI2BcW6vewJnFIIlAEha6p69dOeFs9mpAMnYu-JnoBiAqiSpLqjinDbzlk1ILYoNaEkiL-S3XCyPfAlBkB9ur0qZ4FHxBkKL8WCYo7JEo1XcdJbnqKVB--anmEahX-qx3bWXor_tk1o-K5Ho1gDxJHoAQ18_-tTKBiDqU21zdfjhovBKy03RCVd25NcwTMgURQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=X4cjqn86M-cmTNhNIixWjNPAeRxuw9GjMl5JUrHqa_-GEofMmXIBdnwk4ZMz5YiR271alUjkfnGxT83nV5SkuBvbdMlJpc8_lhU0HqJggpWgYWkg8rf5Aw9HshVO2iGiYmgS_4l2i_1k53tI6Ph0XPR79v3NV9SI-sgUrGvLk-Gd57ZbY4G226r3lWi5PHDanDd_AvLOwIXBib564g-SZlx0m6I7JphJGhQU8E1Fv5QRQEQlfPg8VejaNfZmQz2yPesLytPUPOw6je5HCYl6Rl7CLCbYdoEbtwxvqmxy5dBECSandUOanuLub9hDsOxTk1geLRD35jmX86-gUqf2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=X4cjqn86M-cmTNhNIixWjNPAeRxuw9GjMl5JUrHqa_-GEofMmXIBdnwk4ZMz5YiR271alUjkfnGxT83nV5SkuBvbdMlJpc8_lhU0HqJggpWgYWkg8rf5Aw9HshVO2iGiYmgS_4l2i_1k53tI6Ph0XPR79v3NV9SI-sgUrGvLk-Gd57ZbY4G226r3lWi5PHDanDd_AvLOwIXBib564g-SZlx0m6I7JphJGhQU8E1Fv5QRQEQlfPg8VejaNfZmQz2yPesLytPUPOw6je5HCYl6Rl7CLCbYdoEbtwxvqmxy5dBECSandUOanuLub9hDsOxTk1geLRD35jmX86-gUqf2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZQptj-zh94aWKzgyubudVoMp3X5-75n8jefDpTFo_n30gBqXAeO0FDzkDwh78SxHn2h3KrLmg16pKluQyViWIQy-ZewmbjiJ_o98i6JQoCGmdeb9kncG19CidxIZQreFskcGjzT4Zp9Hgfjz7UydOzRI3qONA5wH2Z3tXM_mFeInVDMeiS3zs3PhVCoovZuVOcqCkUg8p0VksH0Z0AQ2ZoGX-TXcxgXhi_ZjVc9D9DnhsR2iQkQl0-ZwGXlHELafL16-cH2U8D2_qNkZh2NZr51HQEOlyjntFpdcWTQm4TBBmc9vJVJk8q6SpwODC261zfZuoO_wOR1e11nkZ1AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpx3NleecOeRw2HCe7D_UcwLEobMflwGyfBnWLuDIVNyFfXXx2VNxJ2RPE0nK72EC4FP0bTZORI83jXiHtij0_3cObYTF_8YjwTh9phx4SFjWiYxeiStuxnfdh4mVmfoF2Lpnas-OFGSKSlura7AO7BeWguim7j7p6Ob-BYCvoC0fXrXfAA0uulJRR6qye10kWw6T5aC4v65kjIuQGHbJ4xPj1oZwIn3PzNjh64SDx9y_9AkrJ6XjZkESiw780TFm741Z6navB792aefIx8xV3WgFZ5vMuI9e4mWQh23nUfSNDDkibzcia1GvEhnqNrWPqEiAWwjfVvsJExJ89cp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHifjUXArj4k4qIrQQ0-1_LytM3n_J_IOZVdoAzoCefV8dm_etHXBrluAsfYusVw3FI_COby_0TwB6Fkkeo4_atY7ugKrEU1a2O3q01InU2LI8l7iBEDeAoIfT0AtH5U6aL8lL6zwfATwlNVshK4R4WmLy1fVMnFAjWeEJBZvv9MYIfTnAU7wvHEQZpFyy3JVJcs1oZYy4SSnf63k-9lz8pH81F2b6ubLNgDXRgK_q5HSplGYhfwvX6YoRFFhMHWxMzlIkXmVNGFv84XIlgw0eHjBW1nS7SImE9VzsUVVUnlTU_NlPZmJ3od8QhbkT-CfbbPkdoOimxQF6EbDc96KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tczG9LdTtafgtrl_S8-EmLbTZcIjehkrSvMTAMAd_hLQu6VADrbTzNtiD4p4vQpqcj1Yon2H9bf324fCMQMBC6N7ALhF4GoYG6-Isg7Hp_8YH84qHo2n9Qza-TeSY9mU-HCtjrRLkGVL4i2pJgCP-8t6k_NGImnj9_-FtHJCWTNlQajXnLVuPiPeIr1lsF6yyKQEOqsU7WT36wUI6YJuMMvoEuNcdFhR-yH7tCbQTo6HyCYsdFmsa8bsKNYhHNJIxvCdm40m_jV4yJKvIavCX4pym3FKlG_TsbqAbx0K-OgbqMouRVNS3mlOD8rairb3dHQvOHYrelKA3ZnweXuR6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTEnpF-tLNvDA1QyyipZ0shXxDamwcEXG-jlDOHFJp8nYGsKD-hjcd4Y9QslZVhCOcFnMQ-rEAKL2vzwK64nalrDddukegKb37pnWSZ0tvRIhOR_r_dpg5z8UVz92lQg7oROloh2Hukst3FIZV6PYk9FQw4gcBdODOWBycVRTK6v3VuQSomsxMKBn3-UT6iRsw48_0dO4hH6B7FiJJB93o--cPOf2d-ZOq67WlJNo_EEQ53H6jtGBoPcvLd388K6L4Rka1C9mydJ83iAy7VoOr8gsjgfwmNSR43drE3zsIdwpj8EZSeKuIqCQpKZQfRpHGWBT8xzEK7N579653rL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=XfjgkHvzkfTPY6gZFiGkYeHJozg4uvtw1OQhiAfaZxX5ej7kIcKerHWhEWOIiClPBVx3RKEG5yuUNEmZFk2n9M09NYuNjDVZkwu3jED57w1LoSJbnT4isiu3xgIqqnrgyYFsus_eHpWPfu6ojyU8DqeXsZo2jED7BrRRerykBFQDwTIM6GkzsWP0kEFr4PF3Rz1HSvACrSONYoJ-NPwp4lEEGilw7VKfls0TLmzUW5mJzD0xEWh2rmRkQXyD8sKMW-Zvqunpi6YdgHiVjEMfgO6C2hV7oa7NhGCIprwlggcadnJ7yxhF0dqdIW9k2s6t6DKMND9B9bpmTPOMkdk49A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=XfjgkHvzkfTPY6gZFiGkYeHJozg4uvtw1OQhiAfaZxX5ej7kIcKerHWhEWOIiClPBVx3RKEG5yuUNEmZFk2n9M09NYuNjDVZkwu3jED57w1LoSJbnT4isiu3xgIqqnrgyYFsus_eHpWPfu6ojyU8DqeXsZo2jED7BrRRerykBFQDwTIM6GkzsWP0kEFr4PF3Rz1HSvACrSONYoJ-NPwp4lEEGilw7VKfls0TLmzUW5mJzD0xEWh2rmRkQXyD8sKMW-Zvqunpi6YdgHiVjEMfgO6C2hV7oa7NhGCIprwlggcadnJ7yxhF0dqdIW9k2s6t6DKMND9B9bpmTPOMkdk49A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhuY_ldXnf3rEgih_vghU_DKT4yvE-0_pLOBz_i8huGv9liW6SSZm9NWgoTBzqLq0VVs8XvXZVksHArO56ucIpANGYKFaoP4j6VJ9WLlw3em12rxTGvO2kzweGVco_myCK24ncyfHc8WfwvaS5Pw-t8gpLjihPUsppLILN3ECdx41ZonmJ3Z5QIMj-sKPHbvxQxRIRKlQfX6gRt8DjvqPWc0oKn2Xz0ZELmGKcZDh6VFwfu-i08pxVlYugijA-GOVg_MR0sl4MIAj_BPQhaA3TEHZ3aIDaCi-GMiCEdbH369Oca2W1R5wvOLpaeZVwp8uwH95Q3vQs6NteE6hetldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s28Tg4EHFmSWNPbFpPwlX_8NAjg-iUxjpEbyS9wLNiFd3orcvgaSV8SNUq8K-G9gUnhpwpVJE9vgf2b_J9-E9HmJ1Hc7QefZNVn7SsyZLpQzSKBwGQxjQ_PSFGQcJeCwnH_ghVanbVSVjOHUAT9O9sTausk04A2MxGpcO4QgBK1TZM1dP_QjrtHJn0GXibFNv_zpopndOR2THjjN4fDN-vyb2kJKANebUfdr7GUhQWcANjR4zQt70cvsKwFgZIlrojdSiapchMFdPGyOPcj-5xoUn8HGsVKGBlO-k_afayRwyBc0G1o8ZGMvuSZBYiWO7Q0qq_DX_GsIGewRWbPqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMcMSYUFgBu2nDVhlVLV-eECtWHWBdexizwoHvV1KXA92PYNwwRv5d_jA9x5P0ZvnugyjiPXsgdVO8b7gI2Robb-6tGiM2rHWUzHTIOA0RGRd4JJsOci-MXmwjOJBK4wMua8WyhB_DrObN-HDoMMaE0XkAOovhGDbvnr6HFoqw1o1yYNyR5zY6e2FhnclKOl9TikEjH2ii9-a59Nkx3bVy0ym5qbSNij_3CKW1jDhZFOAzFDXSak_UFM5Bd31iA1Jt-K4mYcMoSEB_6Pqq1DYuK3-62G3H2o7LwA1XqpJnMHq5uxPWKmRq98-7gqZAGZ8M0td6R22YCNYihOdcZaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfmxNhzTi0P65RG2w-uiohGob9hWcRKlioVDBhLJq43SBrF5b_8JsWc81epBYgzjsL9Hc4nfokKd5pPXJwegKrYCTEctso2-9Cx_epgxWxhWZc2aHxzcrZu9eEcIVzELpEo0WX5csBEbO4TqXZsEf62smb43JKSk6xbZm8ao0wTwOZDP3FAPe_w2Cdi6JkZJbuIFDSPK1YeSyk0ok6jbPVWzQuNW4FqUuA367HUXrFXLACRGmQVz9d1DEBtSHbhQISssarrEqxwGzNF_kcBfNy2afX-N4hQKhIrhU8s601t1BDjktaIZydclX7AMPIewV5VvBVV3gHubcgekx3lREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFCbnlqZY6eSF0GHujSsOz51oW58AUXutdh3yT0zz5wqtW2iczn5MaYMtoUCXKmhF6BgvAenaVSuIG5-y5e20j_viMruezxAtLFSIzyAkA6LA3X9KXkR3svn6dKT_VTFrvXNxTl7iHtzv_JjCZX8nXBcLUD_6AV3C5a6rMnu2PCjSFFyVXitGnoIuiRul4gMkfmNBVWJo2EfuH-iouxloM4rmFHb2q2kOY1QYBFx4w9YL7h-Q8WwIa06T-KnwkLvSrSvYLS5hv9FBsUAA_FRhPA0bX8o7THoN5KL0IjD78x2xAiixBgaJlYYdK01HeCycrJmYmZreqZczetI0mzjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2P0XArla5zxu1fh3SwI0nDrYCYpsC1qO0dib0U8tCHbUitJDZoG0QCLpelZcMSXN4khicQW5c_esAlIiyAuf4kdTF2Yu-28CT0Z3hqKVsFSHdIveCxH-tOIYBPEQNn4zJjyfr4k8HZNyzQAdqsMViZglcSCni9mpL4ZhADtZ6bHXi92xveZhd3Z4EXm0GteN579ZJmP0caSnN6XWHKzOBpfZk9nDuvc9j2mUu0S2_XOQvdZLB7S7e1Fg2ZLqZX_uCU1CTGkqR2fWp-mR1gNahBd2g2oCgwdLKsC2qwP8fOTa5hpSY5VJJYNE6u07S7qhko-vdr84vmTG0HtLi2SzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUjZEsXwOvAJryX6xFD2I4u3DHcBGhuJak8cQk26LpuCwAgdATBTk6FtjtCxzklakaiJsqh9siWPsptsoKdwk6iJk5htpnqliIjFqMP28LaJyoUxmnmEIaPYX6IbfX_WliK2-nycecyLOEx6os00iPdGmBsSPncQRxMs1YdKo0ElKKTtgJ017qMn6NjtfukPXpGCEyASG4C58XmuGRd4vUMUxqHeq8j6-BwxxDtHZG2ea__lb5-9e4UkOlZIgZDXLsJDN9HWV0zXAUehZ9WoASoCzDyw-2hK3STr5Sz2anwns1Px9Ud8H6U5s-xoR2dDonaAHB_HgAKpd9E3CmMc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXMKcFblS5JVQXor0NnZL-EiH22MLX6FuuRwToCsMqQAe-oOl9H-vyHXWLpplwyENh0HVN2gfUxH7rRZrjdqixq7zkOcTJDuF0V5dqrkrJOHP4rXH3tHH0H2IWEIzGFhcZKqo01N_10gncEd3dVOphUC5syHjlirYl0Q0dSy4wvphh6AL1q5uJGSrj3HWPTtk1aupin9DXgIs4J6YSS4mq3W58cxKQHdMtGTXrf3e8u1rWQvbK-WpuUlNkwcStV3bAX8LlTLoPVnewoXb1IxyOT_2zGLbENOCQYdF5vEh_Qu6nQV53AqRp8ijlRlIbYQJ5fkAIcrU0mKl7nbnNXA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baV5mlspjL_yL_IIelc-VVsIvaYn0DZlIk2Wv9ozFNze45BoNoPmGkAFjwHwVnBIDNJDCW4ymMU5jzCiMgDiNupygxIyDvH7-sELIM14YovlPynDMdPeQa5qeUtCkUt5rD4chg_DnplFSEdJ7GARlaBc2mY_E4_RBFcvELTgUTL0VObce_4MBM6d50vS222Puc-BEBZisXYhvS11NqEWn51xUlfCc0f4P_VBlnQTqFzxGI15B30Yv5xtTbF6d37ySW9KKFtdwq0PChtnsKTE9FxWZmrajvbWMBGLjdNRVe01NN1jMDqXMKtdSXRV5wWQAlUJf-XcM49WBdIOza6vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA-isjHQ5RTW8AcivmoI5Hl-hYNjH0VKASGu05YwX8-c2GXTvkcT1tRlzMFZzjD5hinEW7zT_gmje5DLKT7zjVYt9zmdl2RqGgQelixQvzxdNfMJFSaD9WsHg_hEMcDyr8muAi9w_El3Hkn2bWhlfRZeA7Jyx3rEwak512Q5f8tMvoAtjtln3wHDBGfue9Ph2Tn-DI7_A5Wu6qfT_RtHzP6WSWA5QZvhgZ-YJBk5ebkZhnnzGEAGDCGD-tnEktl15-UQF0eNfvEguGGb_FyuyOAT0qWykmgG2lI1FTDqP603vgEkqfjYuS8uX_5XhdNHMzWoFLxEn55ZAjraY05xWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=Xz_jKD3LbMU2NDAJlZ6mfhUot4z6lLi7NLxBC7wygdR-Cg2OYaHIwB7XcR7HrcgW_79IibBsEXBsWgG2rqB-2vX8kyBD0b8wX3HtaiBfpGZEo6L2QFY-U1_zszH0Xd7JLyM7iThF_RuaLHiomWw51TQrvAafLI8-oxYWfzL_ODhKwYsKwnnBf3gBaHjX7k4jZW6V6MC6vt198iN8jZurYWOroZoS683ON-8p9yM565XkTtymMw427iht0KP7BN4LzPXOXg07-PQvWAPfFRFstmJ8274WaQ9oty0gmdLGSthROaRDvCaD8ZWIj_uH-zql5iiNVzjHMofrd7PWHQVwTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=Xz_jKD3LbMU2NDAJlZ6mfhUot4z6lLi7NLxBC7wygdR-Cg2OYaHIwB7XcR7HrcgW_79IibBsEXBsWgG2rqB-2vX8kyBD0b8wX3HtaiBfpGZEo6L2QFY-U1_zszH0Xd7JLyM7iThF_RuaLHiomWw51TQrvAafLI8-oxYWfzL_ODhKwYsKwnnBf3gBaHjX7k4jZW6V6MC6vt198iN8jZurYWOroZoS683ON-8p9yM565XkTtymMw427iht0KP7BN4LzPXOXg07-PQvWAPfFRFstmJ8274WaQ9oty0gmdLGSthROaRDvCaD8ZWIj_uH-zql5iiNVzjHMofrd7PWHQVwTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqfZvQWS-EbmWQ3pufTmvHIfwfecRxJabjxPp3_YfsGb9tTFrNXf9XK1ssdbeNXQioXjESzO6r_dHrZuRzF33h6_XBLl28WXhSrucQMxlwwIpLYZwQenLWMuO2yLZUEOhfRsjDlDpdy5Vlx-6ntY9V8xPXX6-dZVoRncxa66QKdOIHOFFaaDO6KUAKrjwfWtrRnQLAZGdZcl6W7_MYEcQTS9uwFzcnb8h5lX0StBGJNd1jZ4O1oE9F0cLYCjiqP6lvTw1PdCqD_z_EtjQ5m8t9PuyXptnTptWzmpQIX3dc1qbvZatSdumJKIiqe83Yd45EPOYr56cm7JSQEif4dBXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX-qCFIIaCmapP_La1hiDJvnGdAccP1jRms2miy6nWCHvMr5v6MBcIr_TeAx03zRpq2UMogEo-fFBgWSNbS2GEyF8Ji7JPxfcYyox1Uv2eGI2bGcbX7AC8U53skCTXeaau37fMlx-xvyHPiWKvxIAA0wKAxGi_PUgGHaK7s3MGBsNhodbh5z0ViMcVL0lbDuezm2Vv2kudZF4LIUPkSLm4hWxWDEjPEb6qKPMHjQ7dvszlVHq3QTom__2D4C1LrCmqF8YJxTP1zVJ1FfJ-dHEiFeWsrYqk0QqIuXl8xEKP7sqb3Sbq85Z6Ou7ZTR57X8aeIqB7RsCS6LKUzWv1GbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=jPcQXAn4OZWtxh1Zm798vnG9wfWzlOdn8n_5f2L349jS3QDvvjLhXy172rWh3kP_a5PWkJkww3luR6R2Gcl3ifu8VgSNeaeTGaLF8mPocn-BhqZ841Abd_sdcJIZHJXlMQRU_cfn0gA9W-L3T7w0Ln-WCJXIY9mxYC-G9eRvp-d7fyiq2AyX5hmIJhJsIb5D6Uc4masHynmiWvzNbr-vysp_3Kp7DQJCwkr-3jiipeMqba-bjq9WDZ3uJJ0VkmilWf7JsW27eYaZOAfwErCYttDWA-A95s8efxVwqCYYINtIX2b26bi_ps0iiQF9lCv65aHoVA3kYz2eDaXk3W3WHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=jPcQXAn4OZWtxh1Zm798vnG9wfWzlOdn8n_5f2L349jS3QDvvjLhXy172rWh3kP_a5PWkJkww3luR6R2Gcl3ifu8VgSNeaeTGaLF8mPocn-BhqZ841Abd_sdcJIZHJXlMQRU_cfn0gA9W-L3T7w0Ln-WCJXIY9mxYC-G9eRvp-d7fyiq2AyX5hmIJhJsIb5D6Uc4masHynmiWvzNbr-vysp_3Kp7DQJCwkr-3jiipeMqba-bjq9WDZ3uJJ0VkmilWf7JsW27eYaZOAfwErCYttDWA-A95s8efxVwqCYYINtIX2b26bi_ps0iiQF9lCv65aHoVA3kYz2eDaXk3W3WHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAGfIRopVXuRr4pC0032WeEzwuI4qzyf5b4pxOTZme8MqIrePmSb-tLx-sD35YzXL9SqpamWZo7_8xfC07tt2-OWFx4Nu0PsWySrRHIpeM_AMscFy1yC2Ec71Kpv16X4ZtYEJQYmx6o5mBKl7RUtkDM3iVRYtgsPnHDKBLfTBWp73nZ-l625sfUA4EC5EpxbAQtk8czId9bQHoq2MDVXjZLOX8CxboudLEie5n0M6mfAXgeQmd9Evi_MMwmUj7NhsESgIdNMYzd0Exuf5FE6qhcHZh3Z12t_rIEgxuxAVkYRWdY9evN9KnuwhLpI50R1kKW3RzHpTxwsD8bMNvsS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJkaXD574ygFXUh8dG-8trmPoGSX8XEPVVNO7L_j66HeKXIviaDie6AHDdwx9Wpj8uUeK1khI8-mgmfxYFmRtUbU1h_fD35WKxNGdLldP_RJ829CV6iRAbCCGgno5NLHtFLBA59ScJxxgpERfZvLDHiWff8pyrJEWhA91ILtopmAm8gqrNiFRgwWC9AOvYQw2vUFANyHxL9fGZoxc0SC8z8nnVvWZtf8QYfF3rHzYmJcF3177R1CLuUk0sZ6dmn2xabaLUa6lDqxnM141XPCiOI46SJOC5bzVg8aLrMn2ab0JKVkeXoEhBVFEmj7IdQbr-XgWwER1mWHeDKtTa8H7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBPJiskGh0D4BxL9ImKNTaYGO4RpN0jA36I3A4WJ1DYb8-hKaajGCfnWWCeaXtIdCqILWDJ2Ar-ERn6NUeUDkYzofLujXFlPJu8zHEzvJxiNX3sJ9KvMrO0hl1Kl9BEb2nONIuW2GS37sB44CB9ZZznCG_rqhYDkY6aOS9YMe3KnmEV7sJC4HGvNYxFW8cDYBicc6KUOAmwSl65386eX3fgUTS6ZeH3F5Z4HQ3Bd2UGacweurai6lWVPMuU3oGQ6qi8zmB_NSyQpXqht1rxnW-dt8d695LxZidLXqGlQVglh5VfbT7wgXk3Sk4kjmdIhX2PnJKKIk4qSnH4LNr2aUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cli9O18WAzUCGqf-rZyoCf3UoXUaIU3Ixo6OU70ECL7WT_-pk2DpzTI_Sq6275huMVBKD4qD0YPgxvMXv35cdsDRohMz6ERtXlCc4UvUVKRHcHn8DIeC6SWl4wMN38L0gCDjwKvqJeGEsB9wdEYOHUUtkG8BuPJVqPZtWnkCoc701-1yZhs3b0bYqnkGbNxlzYh7LKkDmCxdnUxgOgOjbaWOeyqpfnTTyuiKoL6sQPe7x23gS8lf7H7ifwP2om5YUk5kifw1oCpoBCgLaLcjskkMQ9mIytIcBiOZ6h0XlC5VWbthTuP-mBSPFfK41IsBeDi0wk_i6hbRByMaO28Y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsGIVokmQ-D2hh9S-Lj-19M0oF-nsfNwW0mc9Z2eXX3jDo8kJIpC0SLI8IwJlY-KWMyWWiylqM6y_15ARqVO4NAXXqDeKGcPgYxCpLjPb6zyebFrRq6TTLscwR5Qu9f5WIeWJlgGKDwaUeaQje7VKxar8McqCCLO7wt6R-3UpNA7S4UyLW0DiSFEe-28AQlyWwnQF0yApmdX9NZBB3ru4KE5hYbjWcw8j0XwaEgThChEYnuA5xWuPyNhkQNol05dnLZdq5LLV9Js6phZYGPIhsGhe31TZXhuKz75LFRYf4J_1ABfoJYwj5q8KFNBpnbEof3-AV3ZBu1EN4XA-a6tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEAaOAwx8FpwSe0-c9DOJKrDM1BCpQhga_-iEONJHYaJCknhO-dYVql60Bsn0KECw4GxaY5PY9R3M_JEJ98wp0Y_crqBFwD1G5SKcu3cpPxIU5tI70iwLAcm-qY-yumudiZUhjpvd2vJFPe9lEw1PLPTYRDN_uwEnmHmdliy9RiiBwanAdIP2cSfiY9sHqY3PAI03Z2p_jIKrSpXNzN8itwQPsXToScmrDoo-Y_BahiRd8pGkP3zcE5KD9VrLYLHz8D5ATt2a165Og5J0DHsXPsWhv0RfqsnZkCKOoF4i7h-1CYIjU0cAYXsnNPTjAomDABZA7AYNMuJ2Re91TuRog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
