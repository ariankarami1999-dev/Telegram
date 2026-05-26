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
<img src="https://cdn4.telesco.pe/file/YH5RcJrLUcOruxWu3KpnGwAfc_LPVJIn7ZuEVpV5LtNQEXvzEgbpgKyiMQfdTgMb9S6St99sjfIOTEIZd1x8UKOl_3qmSrnNd1w6kdwxIgq18orT34UuDhNW7X6Yv-IBe6GQxRRrlCqNmB4h53FYzj0HKI5Q1HhZGP5dJKvJ1_MefUvByvLYXOkAWBoWZG9nWEFWW27cyv2UaE3zJFKMJE1jlk9Sp3WsiTcU9IcjUicskpSU3sgVL5b7A6JyLXMvMfKI3KZMltQeuDwthJQW9CvQ12zE-Wppc-rIj9UO17a6omPlSlCULJhR2ox2VPDwL_TQZyWnkW81EUu_7egeoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_CHL9RBiYyq9HxC_sWmthysfmbb5B-5OrCDN9OICEHUtJtH4UhkWEMPQp4DLV1F7X02ywjdNJGBqmVF4FmJgXGBRKr4_pnMxAlXPs8zswKgRc1anLHmKj8o-iLWWwNHIa_Yblv0w_kQMUZk3dJ4muwk8e9FgsaxlVUSYVlNFSgSPA2DsW53UsAh8-MdcY3_asLX_EHU-9N_bcV_KQu9pPC156VfyP-CyGiCDsTXR0h5W2hvO2BgPzvAP2JP1mt220VmABlMvter9ERG4m3rCyVcwOkqXzv-GSB3tVGVPauscq9_Pp855fvOm0ha4fBKIq-DYqePOEwssVF_IetiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ZbrHhWNkF6asaI_zZ0DZSVagMP0Sj1brzG9CMPzGcZvW3XpWVecnn9714yNRz7_Gj812RfCOZRs2A6u36z5kVK681YWdx1mpQXmDg7KxntxxYCwpdg2TEHLRm_iYWeaR4IgoY8igu48lrD7qmS3uORuT2an-J6XmmJxpeevTTaHKOIlbaE6G_Wwd5MAT5PRdX1T8dWSBXg4VcD38MTZmemcPd9yDI3r0hV0iKx37RRrxiGgikGQ7EcDAH9B0uH7tApvHaCncXJjbUY_rOs78UhjdP6PQXuBz1szf8zOA7691l2VYNkxrXc9XIFPi-NgDCm6On4gedIyXr-71KiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf7UsMUanr0Aa1Cp5FM1MLqh4WZJe8WqmC5JjLJctb8TzWdg72V7ELk-TNlaAvCYEilxd0GF33n9lyKC8mYLTM_65YUMxi5pWuGLSgo979GvU9_oCtSx9mWutlgxkiYIM-xA0PRXmBtemCgdx7Wur_Y8RBdKYbvGRJeZ7m_eg3Adl3fAV6gN8yrACDMw7llkqXbE0I7opj6DCL3I7eFA8E342pDltsEfZGC5Tg9JGHFfwkLY_ZvxcvaahE3oNdblKqxil5uj9LjJztBrV-bUlEjVSNNriU1z76VdrTL-d1mlcNWmpgBk_f-l-OKRdWTOl_Wl8xS4C0GZyPYUs4YagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXPqqXk2dKQDnL13zNIt75kjiWPcxCnQkbopGx8QMWWVn1MYPamt2AYBBfE3XRBxl_UkAFavsSv084txQX--vD5bRa5y53e_S5nm6KIggN2-R2Mylxf1TSoOzlH2Y_yNzCBw-ohhVHXsy58xwKdRas-2PGUwPhiKvJxcIkIAb6i3PwC_043IVknCdcrB4IJZ9K-1JChqKKuF98ZwXYllo3IBnliki3aYGO4-yTl9v77TPwDWforuu2M0UyQliqMym2xtQpSDX4i0YfRqJS7kDD5uKQuaXryZ2pUP2IAS5JTTcVHUV2Wi8fLrxsuH7o4tWSuNJLloO4mPxBpDrjgmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=hA0DP6WpmX9zWpfMU5FkzQosX87obxsJK5LmrXHShXscXVaZAEgJUSES8f-E6JNVYiKGPYNfqmCUKD8XID-Umkg6DbxWJrxIUMH7O8ynSPdDJ9rtIRgKSJPOEAi7wOuMYquzln75FwIlVtHM0QW4e2szcpJkuUgTsFgU2lOxjwp-Y5twwpBSCCygU3To8lsqOneHWWkh6NjsPgO8dbHWHTsF9Z9wlD4UeLIZyJP2uUrsE8W2rGSaOtM7EvhR7ucPGtvFsD9jt9xa9OJ7_YJMeR53xfvlKrPCXSM6YbN5clkNA7SE-fNHetutH9dXSVatqWYfrodRYEYvofZzluqFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=hA0DP6WpmX9zWpfMU5FkzQosX87obxsJK5LmrXHShXscXVaZAEgJUSES8f-E6JNVYiKGPYNfqmCUKD8XID-Umkg6DbxWJrxIUMH7O8ynSPdDJ9rtIRgKSJPOEAi7wOuMYquzln75FwIlVtHM0QW4e2szcpJkuUgTsFgU2lOxjwp-Y5twwpBSCCygU3To8lsqOneHWWkh6NjsPgO8dbHWHTsF9Z9wlD4UeLIZyJP2uUrsE8W2rGSaOtM7EvhR7ucPGtvFsD9jt9xa9OJ7_YJMeR53xfvlKrPCXSM6YbN5clkNA7SE-fNHetutH9dXSVatqWYfrodRYEYvofZzluqFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgjpUJ_0cwWCdVN3XkpTsBIEueAVGN7ogXtoZo9OzB08jFW7eU9Qx-0-C7Fri8G3JEaX4ptI3aVewv9IpItLgmgbdMXzLYuAJ2TAErLDL0sP1aMh7TN18QvcYqA1ESah-NSbCt1Sd-ErcuikNZKgzr54ej0v0S1jo8L7P2KiNF3x3L15h23hjOD9oxq_WD530siEoj4Siiz2SHqUp8VDRCynlZvwL5YIomUO7vwW7Ekh4O91RdacU9pEJZekYCVylN2Hs4ZBqaoADbEZlb11LOkkr0mbraA-qr3I6a1anf5VOXP4ii3wFRjWCjTxl7AHmXjueTtNT4hiJERsHuLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Szxi_uYPxSaSRsOG8-cTkVqp8QBZK9UWregbHgRmx_49ctAHQoDehOVrjwAgAzNDXGQ8071JaKqelXJofHfoo2lNbG48p-WgSqiWYslD3LDAXqNOjqwzpQVCaruNhmi3E0N1gKI5hBR4_OGyJobO-aVtAhAOxZhY2g0qkcEf70iRG_hclo6arQ3OenHfrXY03sv8xmVQnWDctbI3GqCui597Iv550bcFLYKFWEzqTnFt2MeegOglJ779Ff3VWSToKK0dWxanyi-pmpOrZIUa6w1Ij0Et-SI2tKyJT8-231I89fFCEwpXlUNx66Q4aHeOij3PI_FahnrBZUK742yqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=Szxi_uYPxSaSRsOG8-cTkVqp8QBZK9UWregbHgRmx_49ctAHQoDehOVrjwAgAzNDXGQ8071JaKqelXJofHfoo2lNbG48p-WgSqiWYslD3LDAXqNOjqwzpQVCaruNhmi3E0N1gKI5hBR4_OGyJobO-aVtAhAOxZhY2g0qkcEf70iRG_hclo6arQ3OenHfrXY03sv8xmVQnWDctbI3GqCui597Iv550bcFLYKFWEzqTnFt2MeegOglJ779Ff3VWSToKK0dWxanyi-pmpOrZIUa6w1Ij0Et-SI2tKyJT8-231I89fFCEwpXlUNx66Q4aHeOij3PI_FahnrBZUK742yqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=K7TxQlAiYAeHQ3cm9TEKUm6c7HLzIfQ2MXJHt7ZCSpntMLwEItYhUUwACaKqa-tPpsvMRzWKblJXijm83JxC1eIJ2WUc8hH6rDxMz6ieyKri4A8Sz3v5E4X55J3YrM3D4nUL60Us_Z0OfhUBJmF2cfc0-fM9jqoFZicdr0l1MI9XKCcHAklnGTV9Tv2y0e50iUgAC0WIuf_XN1GrvsXsjdb9aHab7IpC1rw3GN6k5yQFbOmN6ixw9Oh-T9h3-CHlSZtvBRx9EGkUNzKBiP41MI71M_HWHl0hfEJznKGYKWYgxUcpXYlq_FahSL0oDbIZNJ19sUKga0poHo9Mhdak4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=K7TxQlAiYAeHQ3cm9TEKUm6c7HLzIfQ2MXJHt7ZCSpntMLwEItYhUUwACaKqa-tPpsvMRzWKblJXijm83JxC1eIJ2WUc8hH6rDxMz6ieyKri4A8Sz3v5E4X55J3YrM3D4nUL60Us_Z0OfhUBJmF2cfc0-fM9jqoFZicdr0l1MI9XKCcHAklnGTV9Tv2y0e50iUgAC0WIuf_XN1GrvsXsjdb9aHab7IpC1rw3GN6k5yQFbOmN6ixw9Oh-T9h3-CHlSZtvBRx9EGkUNzKBiP41MI71M_HWHl0hfEJznKGYKWYgxUcpXYlq_FahSL0oDbIZNJ19sUKga0poHo9Mhdak4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO_tbO7eldI7KNAGwO9Fw4uLgVJGoRD54hsyqEu7mt7I7vjj-brDA9p87g0MAVX0hPcousI8VWb1ovjyd7ZiJ0PSY2JtJSvQXyhjCinxUEHi_NnpRHH7nuN-SEfH67YbjSjX4PDCLLlVtZlAOqyixkI93sPOUpXWCSNyTJ5ZDp9zeKXf9909oznQnqdDl3gWrgtj39pxAubVlAIJpS14ZdHz8YaTFBiVDwuVQTniYWx3c1_upu9iGbDDIpwVCabjK8zzUavCdHZ0nF3eGARrfmy1vZc3ke_iEoRRUqlw0Nr7svb5kws7VE74u_oDp4f-sFHMtvKSN_x06QfjQVmcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MehFjieTuEtvYcQyJjRPiDKYPcD7HNmCOEQ4mHp3vt8mI62p-XeOKwC8rSj5rEagPJJ2flNEIWDmGXAbnxQe-Sxkkrxbu3vI0GvZc_t8ZgoHVYFMSUFdzzeVZuQM-lVTaIUbp0GKBMMIkmN7mQVTeFk8X0DbgStwhAiTRw7Jf2CNrqOXinmPlvkTQdINRDXckhOUB2QJY6DiMSXF7WSuXFD68ptH9wsxisBkXTmVsXvvSerRlY-PyHTBq9kap5Cn_K51rrlahn9MylId1tErGhkSD9ri_IkxtYTX1ddy22hftsDDp9LapYyBo2AwXs1iuS-6H1GQuH-w41j2DvPx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=PIij9k8PXZWQPa5WBfZftPm-gHCEd8i7iwk0Aa4alnc0lRIjFr8eRmtisgn0fZR-Q_ud9X9TKMJFgNOaffpSc4qLcAyTGqP6gYJP6aZUreZl5MDwGkbnEHwRcZOxzYK_lXbziND7gqCwZwbrdKquAQ11EzhPoiSd4SvNPFVq5TyJKh6598zUaFwV_awm5uw6J8absVAsz9zofU3n9P_m6wjMmdCCXEsVFcnPkeAruK-nwSfuJGhrLRoEZJ2YVWuemC4IqBMID_rltY4MZKn1hzBEBeb3CL3z4qpvz6rTpPXU_-4vpAok9chcVZJ7q78OSlx6vhqg6om7JCevtswFfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=PIij9k8PXZWQPa5WBfZftPm-gHCEd8i7iwk0Aa4alnc0lRIjFr8eRmtisgn0fZR-Q_ud9X9TKMJFgNOaffpSc4qLcAyTGqP6gYJP6aZUreZl5MDwGkbnEHwRcZOxzYK_lXbziND7gqCwZwbrdKquAQ11EzhPoiSd4SvNPFVq5TyJKh6598zUaFwV_awm5uw6J8absVAsz9zofU3n9P_m6wjMmdCCXEsVFcnPkeAruK-nwSfuJGhrLRoEZJ2YVWuemC4IqBMID_rltY4MZKn1hzBEBeb3CL3z4qpvz6rTpPXU_-4vpAok9chcVZJ7q78OSlx6vhqg6om7JCevtswFfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6DGobxuLaBVUiK-nLBewXwbiXLI1lBMdq2JnQ0sTzOHl9GWCbQ5AyOYX3TmqUAvV5kP0kCKpcwXjkps8hP5BbbT7vqiuj2CUVgYa_Ly1jqk7nZvoIiMNC4TOKHPQ2cdfVVBL0SOyzUD4fDbxx3Yj3gwCxfaauqUFUONK5au-fFyfiGhRELA1gblWsu1bCk69plEx0vwPIVVhnoo1zSkiv5PWoSbV3Zk1XMJ8M1WHLmdX1ulog6BX1Xl8RbYVkV24lqCets0ikvNhyRvGtSOIKewsnwF3RVSahD1soNMzNssWY3vyXXr0FckXs3nXUqx55ugQtu4meXuzscr2HUR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at4_Sd7B2fn4HKvo2cxEicqN4brMIxC5P9hGzQzw5q89JBmI1oIGv1f4CmdsWpF1-l-_j0V504w5HD_M5IThsxSnTfuG1G4KRb8zal0Ke6jX0EvvAUaakaZBgix0F6NIzQs9jT63k3fphyMnXH6dGaDkf7Q61hLtljyIRoHscggn7vmULBLVnrt0BxoMqOSybYvTOHtA2mYG53X2I3Pqe0WlPtapeBpQNwCvZ-4PUeVoC_PUQCoQLBLDoTDvQibnj4-IxaWHmYKADBgnxkcyGNh0scs8zvmD57XD09XrKeqZ7EM2w7UiWisQ9CjHYOulGRntc1QMU7gmbMINEQGJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxpSWJbea0yZ6iVTzaVSBQfLZOKS6LqTEs9L5O_zsXbQdsUtUYFe0kWlI5ehonwnl77KLEKDra83LkkGD_Lhpgx8Z0x6msayrGVjJ1dl_FpKlycoKEf3FpOTTgRx9REmi0OXQ065okqymI3xjpUy7hDD1vTf0M02fDTQwZvYiG3SwltIAEx46PKF4oINs5QBq5q5W2Tf_wBL9ueTkZ9aTo_h1_DSdwsFgiSnBxwfuVHVRZIzvIySv33H8ZCOZgaAR0SxaKvVY44QXg-3_hEmdInY0IMM1NytqZXVnQ1jAT2s3VqEO4HvuOsIHcExvsqa2YYKNTtJmo9KKZPAQ62-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH3gi_LhA9j0coNEyTC5HV68pw_a-zuzpT5MNKG30LyyDtPGnOu91iNXE8B-egzkyeO_7Qn9DEu2b3fzuABK7Z_E6Whu1VwEVvdR0pjqPiHpZJp0rM4NFV8KE8Ge9rIBso2xi1wXakuRLuVKf9l83b1mJNhrKmGRd-HOogzncogrnAM7BrSRs2SPOlHHQi04By8I3bJcKRoKkNkfcE_0UGlotK_aSVKZwQaDHx7iJm2Z54UdIxSHEfj0sAFumcl6D7gbWZq90Lisr-W10ddXFn3m5jZeSku63-QTP8dFcC2Butl7oCX4E7wALSWkji7WvMNCMv-YFWU-O7DghFPpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0z98ZuUl6H1Js3-cWb7XeUV4Eck7JgeBQrMxuPJp7KBSXiNK0uIJEpdMD_iMHz1mTVAmGng1tgaFxXnDDtnxBjsu7JzYDHVetiuz9dB1CVMXCbKNmhr5dU46iL_kvnBQ6UTvwMvvfXctpst4qITm2EKeZHJhRiHUw8LXBurbh6GHP-vhrWmRqfftaLk8q4vAprHlg0cPFx7aV0AmaXtEx-eX63dQ8H9uxTlcm0tGeJ6bIbfK8x48DXYLJxQSTpkzIGB4WB-W8AcY0rkzgV8SXGTBQD4oCE7gwEUYqWaKyeresFmKFkPgY6HHz4ZMe3ewzupDiGQbKkqi7hAYwkHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arSgi89N-WeKjpXRsS2c1vKZCTv6PVAGnN3CKw5fOrRWKOplozlOdt6A_e4HOgYKtIvIi3GDAaHctwTTpTIdzBoPOZVBUSWtIDO546lq8Za2nmBv5uHB9HOG-eoCFKjm5_Re0iEFUJuVFJIxq9qQux_DTqsZDI8_PWMOop9hnkCY8fDmKcrwG0WPfcU0nCXi7vN-Rvum5l5goezGeCfE1QWNisHliOllgWH5mFpEXkwESOzUW7Ic2WuDqHA1ikbe-rggvdJDdEkwgHNFx7RYRq8fGLcd4DyDcWxpWmALtgDpc3hm8MAYn7bPLfLhweV1V2tNpaCd19D2JpdhxIXocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTNQh8fhS2pFzkh3J4ZyX9n2TdwM9jBGcgncSUwtMl09YSd-_YKUyZ30OeFC-OXTVySniqJrO90arx5svkNsjlLDdduDlFfp3jMmlRCY899zVRwGhlZsWZeG0718GNu4thpRrUhKw896PGV7I9LvE1rV2zXbWSxL6dKIRqNjKQBRfGPbrWEkxn98f0Lh6GZ9vrzqCHKZukKkxxcbhHGKZH5QKSm7K9v7a1zOWOlfV5sAt7DCgVe-zrANG-uc_oq5n_MW7QS7yJJC0a06AyYf7yWRJvK5Vnll0vqgEZ-aiN1YaQNEULuGibbeGfBjiLTZaoLG6IVhZq6xko2x8T5Elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPVzl64ig0pgmqQn1z23dqc87VNAvOcfVUpwcBQm2ZW609ODUV7u0R0f5BqyTOfPeuLiF1At2shlS_hI8rSiD9rx9ZSTfJAdsS_bzbVhnUNSTDbJBCNCIMWXnjwR8caZMf04r84XdwNuSQJZPAIOfUmaXd1EErTmMF9poDt4TvX0kcVaAlz0fkGfYWIRp5sC-5_HevO7ZxHFIoBfu2xOyydUcjpC_N9Eco1PxzA-0UHKRQupc97a_yCsxFZWZr1kDTrd1DTl2dhqhPayXdC1HLhyKTREe3nBN1nplzsvQZvHbftCn7nS2puyqjru5QWYrUZq7gUG5t2yld_jFwbJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6kJu5b9ggAvZUew_7rvUErBgr5oULvnpjcmd3RW8wwkDN94roCeGDTFc2gDJCNs8kOyxh2-xR2nQxG4hQfBrnd1GoACDD3ucifre2Jm6W-Z1YTczDxFECFif5jRKLNVqx67ZXJ3kgLV8SzjbxGDH4XxHdOzxKqYp6p-vyTYs68ky_JHJ0SFDs_Wu9plX0NdfT9OOBigtziR6k3hA0oC8LYRUvfFBWDG_iYhsVUm9dNku9PEPDyv3AGSC_0UdV1TzfK_Zgo4p-PrbkzqTCJ10gVvQ2BuKtUdwkqYX70lKSskgE25JJkSs2WlsFGKyMa5Q_DPAxYUWVAHb-Q0HnGOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckZd_a6ZiRMAe5TMt8MXv4OFNFnNOIGEqKDAiory6V40iRfUT7hiEeRzd5B-yXYuCf0S_F_LQ9qIowCdc9xUrlNQD6M6RGkL5FfBhilt9F4w1DjQcvyDBi1ez1eHcx8VwbXr_TCJEsL5byTn28HrZ5PFXRuEb-TXM0tIKnnKA8uc7WKrD3HbiB56H-ZVd7UkZ_WaKv_nJdgQMYb26plWfPXem04FsbN0aen9DyKuIz6D3wMuM8JQtlamcIyrsXC3Ntj6nEaMf6hlfonvR-93_kYE5PPqdCkjNAn2SnmITymUlWhEwW3Sc5xUPd3k6P0dBnsJda7a78D2fM1UD6lRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5mmSNU3zk6CAxrbIRVndltIF5x4DIdsD7XCIIkkHed9101gwYNy23Ef3KNuUYd5tbopHW-dEkZRZwg5pe_gmyX6q9Tai5xHS4lEmflzGqUV3jtHKN7PbMQ41qmAwmwaJm8uddezJ0_vfZi7aTrWwfPyDEh9vRNdlTLZhJyGOJ1qPRooRmWBolQaj0ZdnfyGgUltUpYHEN2ghCv0gdWCY7ZTf4MLvmH8mGE5Y0yYuAnbllyAgtgzteJGdN68iiSe4OfqTyFqzLlQdl0TKfR-AFbvTSZU8H3alKi0SV6MDsh47ZdLwQ_yh2dytan6RxaWUCh8ZzKRBS1pHgMfD46Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=OfeSHKwwB8hHxqU8fGDPItqxS88sdnbYFoeJnPeux3HXwJONtIHVwGKGjY3rSbHwy8H09jteQyp6ARGr8W8_2Z8YYz8A0HmXfzSGuD9ltkK0a0EaFLpFzlgdtSLWS5KPdJhBxBxEI6TdC77DuPCE2N8llNsCwTR9TqWR3sWpOdllbJFpWUkrzw97n_NCIgSEEtb7N1CkX5EVz747w7JKNzaAuamvwx0VyxR8tvO8kNmzHltHs-E3lwzBw3oY_2NWvyLEbGNIqxV-vNAsMfjCiQQGk9iM_On2m_ukl7y1bRyL4NievQjJnr5KnCbuOxDEdwdP_0Gjo9-hQxBjWOyQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=OfeSHKwwB8hHxqU8fGDPItqxS88sdnbYFoeJnPeux3HXwJONtIHVwGKGjY3rSbHwy8H09jteQyp6ARGr8W8_2Z8YYz8A0HmXfzSGuD9ltkK0a0EaFLpFzlgdtSLWS5KPdJhBxBxEI6TdC77DuPCE2N8llNsCwTR9TqWR3sWpOdllbJFpWUkrzw97n_NCIgSEEtb7N1CkX5EVz747w7JKNzaAuamvwx0VyxR8tvO8kNmzHltHs-E3lwzBw3oY_2NWvyLEbGNIqxV-vNAsMfjCiQQGk9iM_On2m_ukl7y1bRyL4NievQjJnr5KnCbuOxDEdwdP_0Gjo9-hQxBjWOyQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=jY53cojknDKBPCikodfxDiLeaNlxPXwC0f1zN4OyLVmrAOFGWoxQaZpKtQfDvSmTIyXPEb6zsT4OiNCY5fx120QKeFJjkBk_cQ0Jaa_Tih_66kewcZXAoA8gtrpNguXKe2_phj48HKcIf7x5pd5XVdDSfWdVMr3M_Y-CweBEg7WaLuvrU1bUOEb28MxkSbxATiyZ3D55lJV-wh4OeaeUsJ-VaA9t4sXc2oYfCaTluDf0vzwd8q0MoAvzVnfgOUCLs0fXXbL3HIlAVNqjrzxESZ3xQyvs-k1fXb0xWXpZPSqbBjuu9O-KjraTJVvOBLT3gutRaTP4GkVMWbxNndDi9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=jY53cojknDKBPCikodfxDiLeaNlxPXwC0f1zN4OyLVmrAOFGWoxQaZpKtQfDvSmTIyXPEb6zsT4OiNCY5fx120QKeFJjkBk_cQ0Jaa_Tih_66kewcZXAoA8gtrpNguXKe2_phj48HKcIf7x5pd5XVdDSfWdVMr3M_Y-CweBEg7WaLuvrU1bUOEb28MxkSbxATiyZ3D55lJV-wh4OeaeUsJ-VaA9t4sXc2oYfCaTluDf0vzwd8q0MoAvzVnfgOUCLs0fXXbL3HIlAVNqjrzxESZ3xQyvs-k1fXb0xWXpZPSqbBjuu9O-KjraTJVvOBLT3gutRaTP4GkVMWbxNndDi9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM8NjhhStGkP0Z2AYAF8dbdMtFWDxXRyayhSYUK2D4V8NiW2DEp5xYx_W8mj-KF1dh7lyfpHylshVcgnsSQfVfAOQRXjAH8ePmep-bpi5EqSfkc7Qm06iBmTcrDPICZ32JeFYOcf-KklJaId3ey5ih6H9rzJ_yr0Mk6NfaAk61cCu_UG1d5rnc29WbknDe-LCmDXIb_bRmP38ctodqkueR7WW8SiUv60LcWd3V2-4J0waPmdux9TwjyiPM27c_vRyavxius0vYkG9h24CscTRdp4WbgEhBEfKg8Vj23HWMVn8flXfQm3pnvmrfiqxHwGYpCoJYfWtEGTy5_m3awIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed-IKCDQM7uJKG-GkewGVJU61p4NcViLjAU2k9yJxZ_NmJNnq5wTwzPQoa_9hBf3iUAeKkCYs210l7OU7mnLkDLVF5REkR439p9aLeOztspsXEwIcKGCg0ImPX1vxfGoudaENJ469Ebyt2sPWuSqciyaWj-jwFLmwUw4YWfsD0ILz4llmfQv6ga-ZwfVoBxD7NbkH3mqffmbj9Q-bpFgD0RfnNwJn5I35EASup4gGslF_iKfuiBabr1tYQdOLy_W9Vtarq6tFN6rDGVT1AWLoN31QmxT6ooIIQ3NByivGkEFu3lpw-xREmo_1R0-Ixvrwdo_cn0apielxb6V4rtkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKdTBn8aaZa-0LGdmYVtPtgQfkM_35CJ4Wyx4uwBklWNG-Y0AKg6fp8UWDwHNSieFWnmchgiirECXIqvMblh7I3yud03weGV_UfpR3CWMVojQ9IdxvacohJUGhNKyhgq0fu7-xW8Fndo-61L06EgxNoWHNl-uGOVi11jryfOq59Ttj_l5cUXaxTGLEv92Acp7RcTzwxv4Owa5LWuybjzUaLBbNeOiHP6F7_oK75cEndXLZdjfeO_NxDeqGZyHY1m6RlrznHjBgujbCAUtdK3Lpa5q9mowradl5sRmbJry-8qdfdMLzArBvFzMKXS8gebnqtvK-2D2a_hpXxm6hQIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=Cl6-efM-jDWdJ0Ma8vPU0_A_5Gk_Yoa2h38FzlkXTl8UwREFgw8Ee0pRtXOce5pflPR0diLK1gOTFqWqyqx7ESlyd_qA1QPzVUUwJANmgugwzEwxiJwWHkeIUVcnRU3pNORJE80f5-dpPjYZgVTNkZxpsBmj8qHn-VXBfcTWXsHbI-MhUYJ68HldlVnvUOgpY9HHEFL09a3ys71KevgXZgCa9te0AuxRP-WF99PIEkOk0pf7LlJAzyudRb9Tewl2eK7fr-0DRvicqZsb1b0s6Jvqh0sNry6wbbHdVkE_BKP04tRcPc1sVrRkiSWJZ3RU8m7VhvgbEqDCX12w0kNczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=Cl6-efM-jDWdJ0Ma8vPU0_A_5Gk_Yoa2h38FzlkXTl8UwREFgw8Ee0pRtXOce5pflPR0diLK1gOTFqWqyqx7ESlyd_qA1QPzVUUwJANmgugwzEwxiJwWHkeIUVcnRU3pNORJE80f5-dpPjYZgVTNkZxpsBmj8qHn-VXBfcTWXsHbI-MhUYJ68HldlVnvUOgpY9HHEFL09a3ys71KevgXZgCa9te0AuxRP-WF99PIEkOk0pf7LlJAzyudRb9Tewl2eK7fr-0DRvicqZsb1b0s6Jvqh0sNry6wbbHdVkE_BKP04tRcPc1sVrRkiSWJZ3RU8m7VhvgbEqDCX12w0kNczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exL8S1lGosn7ZNlZGISZtk_dImJszFwpKlBaml7b_orWm_7-DHYcqt_L-P5qQ5ySFjVmA47QJyKX0M7pjk3N5h2aX9Rm_o5w955DPXAmDaojligBZ05j3QTaouZx4jI2YJwzdR6EZB0ucGA1QKif6_EUuPBsNnoZkyXV4zZwrRORixNf-K53BGn-I3wQ-mU1LjaUTH7F1QIpetQ8-DWfKgmoPbnIDcJN9VlkcaD8AkERtcf62sJT7ESeg363BnfL3-Lvre7qpkRMEskzkg_ZmHkdpr3dJbwvYxOuywPBupojBlfxoYjb_Z9cDjQbQ45o8rai32tnxrRrl_DjdFKZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKjQeIkGh2OkbHU7oerWS-SUujE3SNDKG1Dcu3kVXfmaIeYB8XjdmMfTo4AYqA7iNzI1qI26Tz1n4CYD49ernxYIMZzhUjsihu2MjzRTjGKb112nnCvDnZXy8dmz81W9tqujLSqdX4fEH2-KKbEqbXqL2TAof44bvm7yNArvTnzpZUxWQ1YNg4DbmhY8HKm8AE76Chz3qor-i6u2UKoI_cfwLVaNtclYVpHP2S3Tk1y6LFgEkJqVhcHgDjRiBhMHkdp4D8RYkcLI1IGHXJQOF4JN62PVy8RGdg0ktIpQlOaNXHO58MOVF12gRKJ7DdE2j-MOHEg9omWveUQtFaO-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlXWmSTTErQuxLV21JUTIHXLzXEbNvkzawC793KMKZAziY4A_FzDed2bEzR2sXJENptfzr-ZHAOUQlSEtpLHsb7pg1u7iheuxPT7D2lT1WkWcUZuwxrYC4y5cQRHrwiFxvelD7RlCYe8ApinxPy-lylGaNR5Zr2NrvRr7NjmVTyO_jZUg1WTLYVExXt7wIA_zgEgSb8bcKxgGwdwu5aJ8zomSUPYuRouSJMX9qFmE9Mmkbk526NHiYVzHdSg01a7Y7jB5-rqIz1BCZfAaiY6W22Ey1w18C90EHvJrwylxPcsoaFA2EBsNnFGJMoN_zGbVXBs78K2uhLU6YYTya0Ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3HGB1fuXkz3ZtumGB57D8L421m1UStuCI2cdaw-8-3mfQMU-qZtjfKXyVoN8hXfhF0-qjzKNWBOmNJuwQdD5hz2TO5NqtG2WuzvhNxnzY7tXfD5M_H1sVjy3GrMZeL6lB86wr9_L1hlmCd7kyNLPr1fnOwiRfhi_dPY0AhvJsxZUo8hkFDRkcgHgwSAqhOKDv7y55QlV_ysVafAhmajP6L5f7ZsWI6JDKTk5Ha7MX4AV1v0Z40VKOSg7iGLuIfyjh-T3OX4CQ4dkwh_3ch0KA2bsueuMggGGNRHEtJdEzX0ctQ1hceLdMEirHfJM7tAdXoJtYGVniIPysbrNGkoNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAZ65dKtuDGZ7PGW3uq1d_zKjQRBNw1j4fYrDkTq8PtyK1GubRt8LaZIX67KfqPxew-XWRwaZuIz8dTj7KvGk1fPW7B7GokLkbEnVpFW7lqcpJcVULWnAmll7xwQidzkODtww1ZvSOdUxSA858Rzm7wMFk624I84tN72mKbkINAdnHAlbcyTv5hhAMpHg5TTJZCdfmjb_a0oNJttrpcLY0ZNEtMXFl7hoZWKu9-8senSlugVzii9PSFGuMpoeTIatyPPYIfIjqNTbynlOSBuf0khObPv2E0go8DIBZHxr28HFyZJf7nwHIwTtm1x7vbyKhWfnQSk6q5Y1w_JV1uToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_RCibJva1G83XWhCtcFq1XzMrA0SALhYWWFzTa35LsPQEYSaplYbcSNmCUEjDiLVQeLcoHTYISElFK6s7QmOWVrBxP7-TF3Dtugaa5QFyvz2GaN1OCUDtTf-VJ6T_sWn-3nonpg-QYoxYZWGs_cfvBoGyQgzve5v2l6eofPz2wGdJNNc02oGcE_G5MvsOBTiG-xgbnSrFV9QpzjRcIoL5VywejJC3lFIcRz98Lueuy8fUyl-Aw-alOvY26pvo4BPO9zvPLvER3cuNQeI4nzUNNkijEm7Ho-DqeHbkw4Fce9tviTcLUCEvzK9jylBG_DIt_bfw2iqWuxffG5OanSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6K5OGdtyW67EbFwNk9kRelJrJYzMhhHJzR8oxNIGPhT8fnykoJ_7aJesUTF74bZ3onDRV5uVa5vqudRe50M8I_LzI34n3_BZW3YZhefCgRSZkiA9GYxihRkBsMAopWeHqKSw-GsnLdwD3283OCibjaGJW-6yGQ0EaIahGAA1pjCvr7c8UiRRlFbu0XdvhrxTO0qxGqUyDvRyhsVO9uOg3gWhtaLxRIaie8Yr0hZuDBqb6bCzblYFtYuZ_JX-eTp4_yBqtysbSEqm6X3VbGpn0h5bUDQ8h821oyv1oMPa37a0g-ah7jvMjheGocRvjQ6tJCiFxhKW7_KiF-nEjpTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOoTA-gESr-7XGJfj8LRCUj9EA2IenFFVb4CuLQPsU_v08NJrMkTM8AVBDiUpD0mHcYNgobxkzV3nQZ6DvPQpKihBQJzigXZgIS5Tq6M17M_CRtQoaGBKJkbZVaqbb-A4K51Dften5Im566yV4Q4ugcX_7nOTiFTzKUy11bdGb-7buh_183CsvbzjE_zTQCp569l2uEhaGsUmiQAT-epWjVr9UVnFfMCQ6wLTCgb_CokfJwuILIpjERTUKm5DXmmvGlwcZH7R9DJxnoNvq0RvvUVndmFz4fcuIZhCg3oFKi6AlB9YIBKV9f0ZvXfd6wMjUtQ7i6EYpBpaIiuLuyx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cL5CyqNRm-E4k0A1gnfklflZZFEZTt-mRoisLm0lwPp_AwEW7IpDzm16eEXFRnnrZrwQURYeIWnZPhgH_fz9AOSne4rbXgq2bwPZkAriqlqg4GjhAIOR-P8rFPLpYCpOLPnA2oHPLRMeoYwk5P3ujNXPLxRsZF0oktLBW7fCfVa7dZY8N5G6qQRettzUtwzt-wXSn4Xo1r1dFxgWVrBRy2Q8uTWGWbQHkHy5HQm79dErDvJvMAj6lrOLpndw76dLuAEokG_zLJQZeOEu9fY6E9MhyQISwf62Wc7yN828C88Q4Dy1ev-K8fR4l76J0RNsPMsWCEU8NYh0gj5DrpxHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSefBW1pPQsSkl0V57BxeOC8Lyuw1Fi5xP-Dhyj_0-CbkUNyUfEE1vA1ul_uQcTvxTJny7PzfhKrNUrt158XZkr4bEcYhLtFk4ucvvAjxMLK54ja-dDlpQv9b0hnj8oZGh6IPdo7IpfMej7ARKeqotL34Qpw8C8KLRTSJDTrmoVZsAIbr4m8KWx-uB49reeeSiUegweUISYEQeB6pAnFDyyVKjCMp8XtIZeiFLMwBrEhi-EbY12eGYhCDXlZPFalcA5DJ5zUh-pMCYzN8j1aGgZxNjhl5ML_i18WDKfOYTajkfq06fZEqNen78u7Dxztlz3R7cK5LMoCVwROqB0SOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXQzE7Z1t42EDSPIwgniRDoetaexh-yrUTQXvsto8S0qKlO1sFA4ZCSX1nfxn-sPg22PziBi8rtCQ8BAsW3u64rMTSUqgtXLIluzJv_jD4bcqF1-jEbaC8NMlDv3nPGRPrs3LHD2eM2pCjClLa8Rqk7mDog-i-8IxbmldPO8QUHOGjpsuEVgKt9qtpY302TwAwHrYUeJUS82c5jmImlgE1FX4kl6YVnrNYrLi89G2diSEYroVFLPFN1HtV5iVpkQ1vvF9ZUVolD8wXiG39gMn35_w-5dJbNAEfR5-vYb9xhNgEX1kXbE5c-uWrSZOjL3Bz_oquoa12rKN2x0bNOkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=pAo5JytfFfouNgvTZ157LOtHwDUeIYDo2-lPCZ0O1Rx55f14ipl_luMAe06c29sb5LvfMKHbaBesl5fkP0qCw3ERY1U32-5MjtdQm61cIv6fdvbADW0bPdpA3VAvcqE_zRVHVUvhuyknbIrDdRiXGEiuLqykokHR39BdFk4JP49ksWDqSUgTK4a691ahxzW6ySwpRsRwg7KFuQYD6Gr1F8k71krXhPvH2Z_yeECPY0aAdiUW5inzAkc1haeO_o6rS99AtuC8wzKY_Gtogy5k5x4nIX-4xGTe4aYc8enOxe58P51mSIOS5CaBD2nxqS7XVUkLN06SHmALUWMv4qFzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=pAo5JytfFfouNgvTZ157LOtHwDUeIYDo2-lPCZ0O1Rx55f14ipl_luMAe06c29sb5LvfMKHbaBesl5fkP0qCw3ERY1U32-5MjtdQm61cIv6fdvbADW0bPdpA3VAvcqE_zRVHVUvhuyknbIrDdRiXGEiuLqykokHR39BdFk4JP49ksWDqSUgTK4a691ahxzW6ySwpRsRwg7KFuQYD6Gr1F8k71krXhPvH2Z_yeECPY0aAdiUW5inzAkc1haeO_o6rS99AtuC8wzKY_Gtogy5k5x4nIX-4xGTe4aYc8enOxe58P51mSIOS5CaBD2nxqS7XVUkLN06SHmALUWMv4qFzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=Xu4izo1WB-5TAqdYJesCwwdS98CO-jo5sL-2A3SXRz1kkgPWMtYdx1x2Z_KUjvCll30KkzF8EBWEdNazP_ZwD8ni-Qvj6kegUjkJO9Ufste94PGiCcMIYadqDnIHvUReY5Ra22nyL8xO2LoORKcXOHi2d11n-AOC0aNoY72ZJuq_37h6hjwWLdss9yZ-q8QsqYvgi7S1E1ov6SXbUxEO-KPNVvYjXJVg2F-ShtsmtUAi-sHAhdCPqBK_mmduE0ennKwGp8Xk_yjyPK9xctfGqidCcIIZe2LQv-imSOYW-8GGeGetluHst_gdhftDdEEevx976zYsM4gzRyHglN3BQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=Xu4izo1WB-5TAqdYJesCwwdS98CO-jo5sL-2A3SXRz1kkgPWMtYdx1x2Z_KUjvCll30KkzF8EBWEdNazP_ZwD8ni-Qvj6kegUjkJO9Ufste94PGiCcMIYadqDnIHvUReY5Ra22nyL8xO2LoORKcXOHi2d11n-AOC0aNoY72ZJuq_37h6hjwWLdss9yZ-q8QsqYvgi7S1E1ov6SXbUxEO-KPNVvYjXJVg2F-ShtsmtUAi-sHAhdCPqBK_mmduE0ennKwGp8Xk_yjyPK9xctfGqidCcIIZe2LQv-imSOYW-8GGeGetluHst_gdhftDdEEevx976zYsM4gzRyHglN3BQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=WOhbSbxr7Elskl523cICl_luCwfRlDBHgiDsDA8vN5j1G1VK29rq0Scwis85DlOqmkZNfZOy7eqvMdSAgw5sne-Eil0cFkR2ECrdyOGHRQKLJlkHU0KlG_XFUYSt2_qgggui2saZ6bCMMMdR6zxSOnbNLmm4Fd_GlmXXIjFEVK42OWPeVtk7a2zD_gWDdvoYQPZRTJtT3iPY1l5zn575WysznLe6pAi4wRRgMGYBuYtCfyN7Ta1B2fZWscdKVy_P2M-VofFAtrubQujxuyCFM2zjfP4Gg7yclZKUA_hUEi3qoy8xVyAEp1g50N9q8T-ZEgMBWyyU8iudwguOHxVu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=WOhbSbxr7Elskl523cICl_luCwfRlDBHgiDsDA8vN5j1G1VK29rq0Scwis85DlOqmkZNfZOy7eqvMdSAgw5sne-Eil0cFkR2ECrdyOGHRQKLJlkHU0KlG_XFUYSt2_qgggui2saZ6bCMMMdR6zxSOnbNLmm4Fd_GlmXXIjFEVK42OWPeVtk7a2zD_gWDdvoYQPZRTJtT3iPY1l5zn575WysznLe6pAi4wRRgMGYBuYtCfyN7Ta1B2fZWscdKVy_P2M-VofFAtrubQujxuyCFM2zjfP4Gg7yclZKUA_hUEi3qoy8xVyAEp1g50N9q8T-ZEgMBWyyU8iudwguOHxVu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmCAoOre1w1c6bde65j-vLRc1dzdnRoQhqh5VVIXUnsYpRKLC109zBP_NCDcFjunD5eBdcqF4n3Yyo3om2jGON3Z0TE9nnuvhugZZoBubVwsKV82PBJozZNv-bNfKK_F8xBLebHPtv1xdwGXoCZeczXwCemYQ2sfGXEBlnvVIEP727tIpBIRc2zNv8m0a6o7o1HY0UDeRla8hvK6GmhqVdFYVSW80cN_YhY1B-Ium1tYWYnn5H9sPJ_eeL1t_bUY6QIxFr7vW-CpsfN-mX9XowQCSQSQLvciU94h5MNIZtvlVlO5UhkiA9KoCwhzjsINtFyW3WauUOgsAQySgRi9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nSvt_TnQWMCNk04pW1lpFbYp_YQsColdDjKQD_B5CZuiLXyli8-mnarmaHAra7Pe9F5PkL_NcTZyOp7Fc_zunUyCpS6o8JkNC3krs5cPOGA9QtFDMBEy_uruMMaOiLqBf8KBhOKbgXpI8IANnqz-YsWYamVZSjm-UC3FuSKKWREIpBA59tHEAm-IPPLe8C9hw4KrFnP0yHM61UdK77liSJgm5wdEValifZuh80_KLy0crOqsfeZuGRbMD80yu8yoF72_3Ir-KlmyjKI_qSrUPngguHFhtSv18vh3VyXUwpI3UppapnqtAoAsuu9s_BbBlpF2mvl7c4lGRd3wldiHEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nSvt_TnQWMCNk04pW1lpFbYp_YQsColdDjKQD_B5CZuiLXyli8-mnarmaHAra7Pe9F5PkL_NcTZyOp7Fc_zunUyCpS6o8JkNC3krs5cPOGA9QtFDMBEy_uruMMaOiLqBf8KBhOKbgXpI8IANnqz-YsWYamVZSjm-UC3FuSKKWREIpBA59tHEAm-IPPLe8C9hw4KrFnP0yHM61UdK77liSJgm5wdEValifZuh80_KLy0crOqsfeZuGRbMD80yu8yoF72_3Ir-KlmyjKI_qSrUPngguHFhtSv18vh3VyXUwpI3UppapnqtAoAsuu9s_BbBlpF2mvl7c4lGRd3wldiHEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=YVjEYLPUoUO_V2zMzeHAH2IIM8THr8XjUMfz792knU5IWcP7qF7lA_o7grt5-QycDpVMDpYTBKZHN9oBbhdkiyVj-p6HM7ct2H1Nxjk4AIrkyW07XqGp80vz5eRpWZGHiSY-QoSIvweXzma9tyvXxN0vlxiWXUis4OCvDsNBc6Ksvex_eecxTgHjabg8i6qhbTEJ9AqoY0VDkTpcF83adWU4fqCe2SRQv9AjmL0FpLRK-__qkc5X1rJVfTRJo16OcHwuvnruMqFZGVkCN9-6lt_1VxZMSUoAIikxS0miwc1TdhjMYaBpZ6_pvM2atIeMnhPP1FuvIkfZvoRyKWDZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=YVjEYLPUoUO_V2zMzeHAH2IIM8THr8XjUMfz792knU5IWcP7qF7lA_o7grt5-QycDpVMDpYTBKZHN9oBbhdkiyVj-p6HM7ct2H1Nxjk4AIrkyW07XqGp80vz5eRpWZGHiSY-QoSIvweXzma9tyvXxN0vlxiWXUis4OCvDsNBc6Ksvex_eecxTgHjabg8i6qhbTEJ9AqoY0VDkTpcF83adWU4fqCe2SRQv9AjmL0FpLRK-__qkc5X1rJVfTRJo16OcHwuvnruMqFZGVkCN9-6lt_1VxZMSUoAIikxS0miwc1TdhjMYaBpZ6_pvM2atIeMnhPP1FuvIkfZvoRyKWDZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvhtfoRshoUgwFHm5hllDcNGBgxCzmKwdleySAC77CqZnmQpzgMY0_yXhm6ocagTVPdDvkr7CReIvoA6kQlm3dZOX7gJ-7P-bThVI8DlLGpQC6jymOS9XAFf3i4tD_mptmPXtpFeUCq9KAICR7pp-zqzF9vlc2ZPyltFlsm6w1vYS_JQmw5zXxiY6ywqz42jMuxjVpaNw05GZEaMWCTP30TaNaFMfxmm_7JvnmNc4NKTQ_WXHHeDg5hZvsVbPJqB5u84Nte5__0XCJfPJ5fGvKxFhWLMBvPOzNQIQH71yIMaaahIBTKdfDBA59BuQlJdfJGcJwwg1TJG_ufEzG1wgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiVYFMGKQ7Yd_oPr0-mEr2gpBR1-e_NgB-wzhsDphB96VIW--tZqWBPkBxNZFhhyn4R_u3ZPgRYSFwNEl1tA5U8R9Hopi4snRbfnznn4EFFIY9WzVjNBnAA6-PIxbEyF68nz2vEaZBvYVB7si1GY-w5RrXCWVfF6GzOapaEOvKHXph1JQttpfukxs7tIA5taBxADW1Xml7-D7LQ8I1Df3oWdcg8t4CwLY_IUY3lxpIc_xBn-YMi3jHwATsrCnTDPgiu5WaSm-dOEUrsQCKoWW8S6f6Dij-nBWTQmDEgIqM7am9AUZ2vuA1ePOahmxNUOm4ljZvLgXYRIBWzgh5k4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEMgIXq55SdHjuIT5k_gpXmhwJ0HcUp_Sw7UxMnPjxoOyqX-IMZACUerlNfZeb72MqFIozi58rL5tiBLfX5YK8HiIJiRQI9D-NWQn6UhkqJL-TRqku6Hg-vlif5d_zt-ZbxYClXa4kxhB3R7h93FViCdss2vfsFYNZwgigAlNtJcBhGrhPYeZp4jcy7ycszJujuGqhyE9cJQz6yEmmvgPYGgub7Jl7vTG95e8_r2YVo-ZFDF7NFaXO0uqJ2KhOymaMIFXLU_ENUO9hoWyXa7JLPxEXxOGQhXb3tHkK4tExD6m-XrJiDntJhxGjuibQo7SoWoV5R4EDrDWhDmNl1i3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTXWpau_uMzEaUk1UAcQx7T2pDMvQF_BDzj7oNECk0h-v_exPhgQf7CDPXj1Fs780-AT5Vg1y-FQQSunhhSaYFWGiSsGAbXitVxno98SVw--r1xbKpaHAGIJf5gazcnkFuimaMatpdt1fpwkFR2h8cIvdGW346hud1gA3ynCKM-3NPs7q4dglWa6SK8d6TsBta7RhJshUBXc-icOdsxI5NtIGLV0W8Wq2Oy2oHpTLaLtkiA6jH8DnXJxJDGeXYCFLUdjVLCl_lHX15MN1J9gO3-O4jprZQifvfLtpaP4umi2N9Z-SO8guedezX5wsokbSYs9siK0_Zc-odOsFBDSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLHkM-0O7fQggjIuQG4EFlvhgS70mao16oC3k_wpUmJ1moXupsQfKkufCI55J8dgUYaAaE18gMYIUcwXI873mhr1XGbNHRZmzSe2LIqr7S7IQwDvcFTs5yWpDwee3oqSYSYE4N_HpiHM7IEaCo5Qa2X_Ha2w4chjdAxRaWh-1xdLWjp9S8_J_JK2jG5Xr5GuHqFhG70wBwdT8i0iK-Ht7BU-vAQ0_A32iceUDvhhK_2irQGHNffx8GHEuyp-bB0ROYFVJajrf6__noaifCFHenj1c2_MUCy2wXiari5s-knE8CeqgJYVwwRRblozzaJu6JfzpccXVBgsO15fA3BpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcxLcogCZGPOANTUvta60On2GAi8nzP5Fe303tP4RhVfBKKj2yXHDiZViAoeKwfWBpejhsogsg_YPn-RimGV-nvE6zd539AH2Fm73I9Zytn3Lt2pqW4CzUE3uhTbM5vK4iRzOMMSCNjYnZkpWdKK1YtoE4WrBbRL6quXE10inrN91LbRibXeDklPk8iBSdU4Wwp13wyRbW6CapXF7CdlEFSsQYSV_cLRfjn2bu_IklI_IdaqZ_OfiTqvFiUzdR-XX5m_1H0pjAb04cnM6P438Ld5mV63pU05XISWA_TfUK97WnwPUppmoQrs7T6xBwX4vaXDkarn-wB4BTFOwlevpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dt3lQK5WrpyEbwtRLYPUbE2hAry0--SEmTiQm-sD6m_J49CgA3djcc8SYltbyX6lpfmsrijVSaSFZB8Uo5F0UTW283n_HcUnIMKVM4fwOI1SzkEjOc3Na6TS_Icj3y_hmmsLlvSnpnAcxtchSB_LVUvlvZD2pvg9rMDvo-nBd94nJE_NHjoDkKlGkNmFkIve84JX7nZtY9XrSXFTffctarfVG0Qan71uePowSY5LSIr03qux15aFW_hpAZ0gBRjk8jji0BrmuzsG6Zvhoy6Yuc0qzpWTVu1Ue1DOIsL9Y2u2mAq_8ah7crbnkLZIjPeHLnT0MIGFzVbZIxm_vvlR1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=P3r_KBE4jyApMBvc3GHwqSanp-UqE-cn8taUI-0113sBkJqJBA6s-y4AYuq1BEJxMya0t3hZJzSnR43hSL9JeniBHCZe6beSmYDxY0IksPFFLSozDm5Vzf_mbN6afzQA15hwaC86WzmyXpOVC-Qtra6SQDCXyf2-tTwioznK3e_qicvqHf85v_qFz4btpOF0Kuae4I7uNDInfE85IDmNHh4RVwslMUJXzYyIFZSiEwp6BDTxM8cYaDSEMRMEZuRas-CZoAulZH89foNNW4eaokbIp6FEKSg1td36xIYgNfACzKM4JzDpKZCy17P_5002nNrueSvB3pIyHmmbQMRk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=P3r_KBE4jyApMBvc3GHwqSanp-UqE-cn8taUI-0113sBkJqJBA6s-y4AYuq1BEJxMya0t3hZJzSnR43hSL9JeniBHCZe6beSmYDxY0IksPFFLSozDm5Vzf_mbN6afzQA15hwaC86WzmyXpOVC-Qtra6SQDCXyf2-tTwioznK3e_qicvqHf85v_qFz4btpOF0Kuae4I7uNDInfE85IDmNHh4RVwslMUJXzYyIFZSiEwp6BDTxM8cYaDSEMRMEZuRas-CZoAulZH89foNNW4eaokbIp6FEKSg1td36xIYgNfACzKM4JzDpKZCy17P_5002nNrueSvB3pIyHmmbQMRk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1WgTwk7qb2VcS3QsSfT4X_62cljLQQ_gq0x1u8_tcIiikkd3iUipX8H91jTPHWlLDMMquUghr-kQsG9AVeWn8bqzhYtjdKtJKrYIxP3j6Lq4YaJhl1I-cm3GzamZ2LmFZcuiyeL3jEsiMGEe1QCfChnv7kPkDX-6sn6uQyhfpUqz2Zc7lnrMYpXgGEJx0-pGGOXGG4zThLDbbIP-9FoZ_wXCc7g9JOtVev3gt8jIZvbFVD52GLKqazTG2Pn1dNN3fYY_yBGbPehFvfuidjfwPrVPN7LjDz1sJDt_R-MkkB9TuB1YbwqAYSaKM95CtmdvzwPJIAMuHZeznL7XaNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjsVrj_x16Pr-mAJzUdBseDP2hWqcdCRUdyfFfhJFbZblnAdQGRXTD7Fe324IgiKueFfJnYJL8yQ0BLeFTCUO2w_AtQdmcgkhFg_kXlN50sumiM9xTKQMGUBTIRRVKfGMNSYMxYN8tml3b8iBKbF-3CZ93xhpKyQd3zuqH-N-0pmLrJDvqL0Kwk0zrrrowToa7sfGl321w80Ush2xskGxNBhiuTGUH1--7sQu8BQqgvI4j3JaC6Qrudg3tslt3VaT0qPTAZ15vxSWkss91ns0hC6P8xtP9wUcu6tiMzxj-uCg-Ec7_wSkBboRrlX3Ahd57ND0bUrMXCV7Qq2QsyoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI2B2rJF9qvJ4rRuy01z6b9sA4_79Y2ur_to0zlQ-egXb57RXOneg2rSN_2l8ZpVwAOYvyPLkrLWnk6XYrQ8trp3fWeT25MOjKs47KrJ7Famuy01p4mNTGumUDQnxrHMESlGEgykTLGleMFLhhv0hgyeZr1ql8gMPMdLlhaHm09BlkRCBotVoVff2qQrSBWWWjBAg98crSraMGfu2_ZhO9BwooEV_7-GGX4rmllSMBkGXoZp7eH2Zr9Z8mlmiGgJjFHeSVkEi7Zcn33obXDXJTyoKurQJVmaymYyVnIQY8V4lgzbbOglrsC7-N_JinOXryZ9r5QxBuCPgxoINVmBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZp9uoDipjpXf0vbdZQUYAx7Vrp51tMsMLCpVC541SO5kNHaDftMBrTWpg26LBG9o8HU3JIUC5zZ5QT03jjpiRX23ShfauoI5zvfGc8oYQA4h7qnikp_38U6d8LwmUflIh_Yw8FusOFRujr1n_I03gd_gdjpLzv9BcuYWJECX1zoq7_Q6-UVvruzMBj6dIKavuGfG2NvPnU6B0K4pct7ruose1t4txK6u2PHDRXCgIZtBCtczq7B4AgkNKEcTZ0szFT_m0UkNw01COdDguuaXT6Zc6WozVjH_IA7qMO86fT9E_RB1CM5-YBbhwok1tC_3398FMvdxqEH_47z0pv5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=Sx9Fo7zZCKoyFgLHjUbJb7Wya7NDnpLC5NpyVdZFvpfs89f3jbkt6b6S4nTalKSqJREIbUBvc530_fDEmnVq_4dHiVu8nmKvo1uRldFJSH9zgQNaYcHzb3q0hbhXczvvYsmrWSilmDXMxVKtArXbOav2nsttYzoosjuVVyalNnfVnAhqicZgSfK1UePXqbDLKsObH9bvQTNqVH-ZZk3w8S_eXYUvmgovnSqpMGGi0b8alRl2pmmJ_vbZO0RGRWOIqkzGdEhbxKaLVrr9dEP-ZLeDBYkQzq2Z4TPvbqeyC1_9tVtB9FVgr2y2_bFEl7WDpZYV9PjCikJ8EnRTwHKXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=Sx9Fo7zZCKoyFgLHjUbJb7Wya7NDnpLC5NpyVdZFvpfs89f3jbkt6b6S4nTalKSqJREIbUBvc530_fDEmnVq_4dHiVu8nmKvo1uRldFJSH9zgQNaYcHzb3q0hbhXczvvYsmrWSilmDXMxVKtArXbOav2nsttYzoosjuVVyalNnfVnAhqicZgSfK1UePXqbDLKsObH9bvQTNqVH-ZZk3w8S_eXYUvmgovnSqpMGGi0b8alRl2pmmJ_vbZO0RGRWOIqkzGdEhbxKaLVrr9dEP-ZLeDBYkQzq2Z4TPvbqeyC1_9tVtB9FVgr2y2_bFEl7WDpZYV9PjCikJ8EnRTwHKXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwg9mqeMvxQwZNr8TD321EOYEQfLmBtMu2AtabbFmXsFzZWRl-QvDOD7GyYt_FGICb64SyqrckKIyHxgymibCWLgZuO8HQEjWSOiD5zLf5Epe22v5k92qcDNC9rUN-fVb2I71bG-d49y4FHEcztcyjlVfUEWAR__kz3Jr6D9Dtznc2M1hVOzR-fEy2SBRdWlS_ZZOjfRdm0nJw-ff86gdaYSR84Lg6yqLcdpjmE6MP39P2u5NIRL4NEwPBBrujFJ1PW3U5s-21GwZWhpYHQYLNvpFKu4Ly0Bn5XtXh9Rs0tdaDbUThvSnBMujW8a-y6OKUzgbYpxhLrpQkobzEOYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z57TY7L4zuP1dPGKrragEnEy0P6J-4ydGhy3ssDpMRXuZgQA5xg7XVTD4MkCYWK04PIWJDuUBDed0mtaLZgQcN0Bzd6JP_Y_w1vff_uxvN-3oPJLyLkkoxn52oC1RS3H2xPwGtrOf1q_0W9GiSOGtKjpmHgM9v1ThkiYpNasrgXQ5qAb6WEhMFkDaEbkFmlZ5J-GpECxyOFkR9Nf0B0FoWD8HTFqjjeN0jzwzir7QFY6GPprZPKRW5HgwkQBATjD8JyadgepllFAANqSpPaDhr5F-0diMBkgeEvOQMp9-qL3MjWR2pFHAs877DzWU4hVJdbYu8sg2XJFQFYoPPPDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGXsdOn382SmCV2XaJ-dghADNKRpEXI4Y7XZ3nsN8BV4z6g3vomzkfCpwEVB3d-lCibxdn0_RL0YCqtkQoGgSFU-WYtuNifIY9PBKT0_Uk5gsAyZIZiTh8HolLSIRGeQm2ztip9IKHjC1RLJTD8HX1IbP9fMKUwSqLLSq4OR2LjLNnAUuB8Blv3Df4v28G3K40pFbaR4W4_qPyphxypIyb3QS8x9sln7AaQXDl8O7S1rVRfly_-rw0In7i8V-oCHnfcocf--Y0AowAj67rVxQtM3cb-XmHRNh_OaVnvVX5m7_aFaqWyiBN_xs9ZtBFj-4lkQbC10fnbOEt-yvkm3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKD7N84SQcJydTEw8-yUpduqdJ8TbRcysIkZDsxG6TD5_mLwJ0tzC19hZiXnkKyNGrDR1Esq_mR1MVXjZ5QB03swtCJ6ilh873mCWMgNfmQaLoExrU5y_sbiUjmdLEIALv7rIQ9byCgil6gmWd-_TbdbFK3XJ5MntlGrb73vStGeZgJCW_3b_l2RNl3QHsR86b0bcEcpO_FLDyzAKgavsgrAdUzTCl9zIRZeMcSHLCJAN_Oz4aoyFOXJlI_AqqyDDbaFk3dzwvQKYvjGscrTG2IAc_TkCXjCHNHW-7lc5ZsDHFR0hHho79YxJKXdsUUOzPr217nyYxK_Oq5ObQtNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc3gtye7c9xLrHCPpgC7SJJafFc9ytsC40oA9c-scmPYGvdXaw21hesQCtTs9l56FObfnYyz6tRmsu4of20hiYjMrQQe0FZTIn0AkK-7vxq01Y8R5DFcAwgHiIXkvqiIp-W-Ie75zb8APSV1xVoU8mazbYFeX08M-Iklj4hTGMhQb2oQT2lDue-0Ge6XkTaeNzuG5AaKK50EVm0X38YHJhbA6lF2Y3Mx9u2-CjPbHh9lJqjeOgCsL9e6l6Jb9_26Z-dGbeSwqBN_9MQ_6jlJH2fZQ3lMqqDNIe2zz2EamYezSAULCS_j33b56x00AhopeCx2jMXoaXwJkne1_mxwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=N80-twyuBx7NxcRtnGK0SRZ2Qh_79RGm2PVYW9xW08Snx3XXfqQpzZNXKxE4X-4i4Q3WpIsVpkkmWGk422FRUYe21u1S0bXqQYSxI6biNGZ18c0MNqWWumOsnumao6JmELihdvUBiywwSzi2RNAC-61Ar7bWjnSrPYgnSI0paWRsTKKXqCOzBK6bOacChuIe8MHHw-zHXq207aC7rd2DHnfqJ-n47FotX5a6QAUx4hI1yrIs_0zd-Lj7SvLHzkHEfb3iI_CJli8s-iKaBWRdYTCXQXvAKpasrXq0Ui9lklGqXSk3KdZllhu0rPiBv8lO7supUDS1aLNpUdVnuJAqxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=N80-twyuBx7NxcRtnGK0SRZ2Qh_79RGm2PVYW9xW08Snx3XXfqQpzZNXKxE4X-4i4Q3WpIsVpkkmWGk422FRUYe21u1S0bXqQYSxI6biNGZ18c0MNqWWumOsnumao6JmELihdvUBiywwSzi2RNAC-61Ar7bWjnSrPYgnSI0paWRsTKKXqCOzBK6bOacChuIe8MHHw-zHXq207aC7rd2DHnfqJ-n47FotX5a6QAUx4hI1yrIs_0zd-Lj7SvLHzkHEfb3iI_CJli8s-iKaBWRdYTCXQXvAKpasrXq0Ui9lklGqXSk3KdZllhu0rPiBv8lO7supUDS1aLNpUdVnuJAqxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
