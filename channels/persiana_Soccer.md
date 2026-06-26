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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 03:26:33</div>
<hr>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjtjrlQmDnNjls3-e6K0oc8ViJwjouX-s333Yl_ClDjrICLDIP_UT3SW1JNGSKjlLY-0jz4_YKmvwBeTTZ5UF-rvN7XrHZVtO0NsOmJPjiMvvnGMfPzmOngLuayQPM7MCL8QLUm4Vbhknuwdj9HoXb61siGlbhy4mLDHpApOqub57I5WRdqTYMfGp_mvxVDVbOCBfNbi9zd04FQ_pUsazuN3-p3HmCtefWdyIUXPYpkF3lEVR0V3V3HAq82i-oR9CVOfYHOpsur8G1xzMKgFfAQmHuR5Gzco1zSXnM_hl7m-AoZB3WjNYYC44GvI1P3k7PyjBR-AvtMyU1_MJILMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=W1ped5xMLaa5kyAh7nsGUL_Ihv6lFpJRFIiZZKAhSp_hLRSsHwFwexaiLNXtAanugpx3a373d8Tqezek4Y-Z1-E3ashKDGo8wp0nKYR_1jaE9iTxmfubaAnLt5LyVcgwxBkEfVkryagFUaOi_EQkQVPy-y8e2f4BDPlGVgUlAcGKuX8GQF8LiboZU2K88OQcvzclutCO6_KXeOLSw0saPWQ3kFGxUUKWLYXvTiS_Y6PHYPlGHZ3TOE9o8wkonA6_y0pfOakyRaKOMoQ64sDZX1b-vjU631fETJxG3j2RZKxstD56mtpV0vd0DLc-g74y_6tg2k0XOcPhXoY89GCrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=W1ped5xMLaa5kyAh7nsGUL_Ihv6lFpJRFIiZZKAhSp_hLRSsHwFwexaiLNXtAanugpx3a373d8Tqezek4Y-Z1-E3ashKDGo8wp0nKYR_1jaE9iTxmfubaAnLt5LyVcgwxBkEfVkryagFUaOi_EQkQVPy-y8e2f4BDPlGVgUlAcGKuX8GQF8LiboZU2K88OQcvzclutCO6_KXeOLSw0saPWQ3kFGxUUKWLYXvTiS_Y6PHYPlGHZ3TOE9o8wkonA6_y0pfOakyRaKOMoQ64sDZX1b-vjU631fETJxG3j2RZKxstD56mtpV0vd0DLc-g74y_6tg2k0XOcPhXoY89GCrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NncNFZuVim-nahPDTR-YkMwJ3iBThoMTA6eagEZl05lDFKGd2DrA6gdARgJWB0IoUyeUOVis6OSNUBA0fKS6VAkHWDVOUWul8m4fViakcxE8YIYGY0NCPd3LXO7O_g0qdCNjyDVrLFOcwLixr9b9K7YpLcZGdBmjhFbs1s7BrXLILEOjMEeQ8TFuczOQ4hYvErNQK3SmYLscDWGFJsQFMDkld8R1o-8_nWFJWkbhB4fMHPY4W-ylslMeSvw-HvVhZySxG5ccQ2Yw8IPDolm8wHN8Lh_SgNWzAsYzzrZQSjGBkki-RhzGUrmPMx0IBd1e5xasu_jWnVL_e-Nqlosw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1DnXo8_ROvbYaLUsrXO9HcFtFhyNJvFfYAip7TYj4ISG-_N6FdF1Mp3Mw-9yNr_7ThxX_9dPd2CvWEbP2eCiPGTAXCMdfOH8ORJCeEEEhwV2eZz2i9erkipxPoi-B_ia71zHJONZVEdJs_wZP6-s8b1VvLgCA4z9Ai0nab7SNtwRf7dkIC2YcAc0ZKNu6YSzTgjYowxNgOb8purfnvRjaKuYwbNPMivJQajBXaxX6LS4VT59mhhv_FV3pdZ-VXa9EakPIEG2iVzdGJZpt6nDVHPlqqRfICB7rx2HrgILjcku20lbRf-wF4RttTPTwaKYXpgB3V1Ava7qhiCfTd82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaimqWgzoEWszjoi3c83Wqk8Ai-8FculBEA60tzDEqS84tUS-xY6GV3u8TEcxF8UjURMeZ5su_1NoYRI2t8b7QxPSDoQnt7iXdAPr6RGvmP4QFLEkvOc3cE7o3WWuN2SHQTwj2o2LfRq6mWK8JLZEzTCaQq0IeWCJRf5kqzcixROadxJjGYcJC6wDZiHXSo49WE3b5HCGHV4sQua1qc2PzTkP0-xFmSi6lsnl3PqVyKcevrF-B5VKkj9fS_lZzpofM96SXNAT8yTNXLKR0WR581jnHMqeoGH_sz0Hee0v1BSQCyT0Tg3_WQz133P1ZIK71Hb3_J1Gpi_o1MMSi4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPldQeY7imV9BLF4qFclFd53CPbQFTmDWuJ3YLZpYi_CFoZji2U1G25w3_XO-qLh0N7WFL1-FAuQgpxy4DjCa9-scNNSdrZvwNJUftC4oq_ZNwNUc2TCi4CEMIBWUhPLPuYrLwdgfGTHFKmim76m_8jHHkGXWNs7TVFM-B2FT1l8t6Sn9R9CJU2kDvjptrXmDSqDcDzlPJAg7KYYkHz2ImYEWGDAayBTCws7vOmMYJcQgIHHOB-0TA6YBkOO82M08g1zmLmSHu-xRafsihiDWCvxPWjEdHDj-Ed-UrcQSLVT-XIdvh7U1FbkJ6mBOIcRtFC3pTg3OM2RScoiyX455g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3TtugJiI4DRn1b2w2vrTGqmHxAF3qA65CK9XGWKrWKqh-V28bcwsYKNmQ67uYBhSLi96aqcorUrX8VMfitkecUoRB0drR10_55HC9bmIkq79pGyXwDmNcl-N-J9pvjAXuc8q03YNwkLiIJ8z3QPZ4W9UfkMu-4VZKv_fyJJHV4P8K6FH2FeltBgPJ68eICg-0HkzgTtoG-O1QoVjPAomfdGqwDuxHBcbU2wwR9LU6E9jJ3ywLeFFtGou8R3ToaS8XMCtOTEaLXbWTCp-3C046RorLuZ3VNYEINkRNFnlWDYKmGlwdNJEO3_Z2ZL1tDIhRaC9LGI8CC2_iNhYMNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDd1Y7vs8bTLfoO6MiUg_0iB8ywqJyj6k-p-as7GWN9yI_h84MFYzmY75CcISRgclAhcRXRsiT4rh2fUuOEQMdHtQ_410lqebZqUBtOilbXZKASJqEbyDS7VhVJc-LW_t04e1kL_w3ohGJMIr5BJPtqR-3l1xcfrPNrvguRhs7vrtz4DTJsN7_gtnpGUpHOIbPlWnzJRTHKCdTzhpJ09pLmIDbX-R71ofa4TP6ycWQaTd5f8WsZ7IIxawCuBVtlpzUBMSvoA3CBmeQCV5ZDcV6YgQHX8swGkthKU1wpSdjzYjUPvn2p61Z6BsTE55tk2IOnlFD8bj-G7BOP8rG9SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24411">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzbdX1ndPgYnnEFiS6ZHjMExYiz_GMc-DjiHlRaggFF4kCzJzC4863ohyNduiyTcbO7zo744H_5bk4hmT1dAFclXrqOzWDyfKg22e96ydk4fP9-6M2P2kgv7LBF31YzXXw9C6OS7iM4WdHAwxvOLNqQ96UN6Pobph7vpc9w68R3Bq5vjwd-RfIep4ADrI50EOkf5RyQRC7f1uUv556_pyYrVYoYqSi7UDWJJKbrj9lYHRV3sd2Cz6eoWztUTXc94z2q6lY-EjNcfDEoFxb6sh84SkIDQFhnwrXxQtXI1I34Rmlre5aFEb8L5rTp6pfI3Hzd6acWFwMYV7FOvGhVb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری کافیه با کانال ورسوس بت همراه شی.
🌐
ادرس عضویت کانالشون4:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/24411" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khKSJC-hVW53aWxtw0_QsQEoxonrPXJA1Fyw_S4pVy_HEy8138r4wTYMfgHsujvNuw1_JTozYrVNAmNmXTTaBPgefTQA4IIebDm4xvsFi8IM-mZ71Xh0SSrJQC04tW6Di2k3BQPrhj1uZ_U3h0ew9Y7PTAmOJJcCBbIU_djPaFIxpHOkpHlfmaKLYcUVgCxzyB71N_tLluuX01VTUjBy1U1e8IkwoIlTa7Vm9S1Aw6bUbeFa7OBLG2k4qDWRmOvaeTS1p_kSIajLO7q5vVU8MKs0O0yjhWs92oPK5wEOrLWRZg5-HUJ2tOwCFaa0Xo9IdIRczK0PahgYOw_8ey8kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR19KrBS0voWMfhLFJMoHUtrDuwxSGQsRdyy4eCLUYjurSwLwKk60yd2gUnoICFXVEYGgEFOKGyzHZNVUj-lqttWk1CSI5JjAdDIIURPFrUDBAQ5uLvKWQwiAEivMo0MRqN6xF-74Nh-kYeLxIYMH4U9w4wgFMZout9GGC-uHWms4JVBW_f-JNcmNF0ArN3G8LrpB4NWycpjQhMRM3So2U3BUasKaENi8FeQCk75fkggCyc9HqsD-jQJPaS1BO55v3eB1AKKeWRHIQbKbgYQNSp5nmtBNBIlESdwyLbLtPovOOICM8vZDJVe4CYOMKjUSpMrVINGJoZBGwWaRNb0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_RZXn0mSUSfvmtCbGKLuuxjLsN7M32UO2Xu5RTWyAYzTm6pCO9z7073b4KcAlOM6H0lqHEXshoL-gzddFmM78MNxbCWGOgQ7l9hLW6TlaZTWBIBwlJHDh3fELQaSUDoro6QIaNwXQ44F4ymJcz-8QAKcOWbd6B2F0BTbNBtyzHJ_XDl9hZg09xMdB91K3UUR8te90Ha6RFG-xuWI5QnOrf98WJcvLz35FfH4JX1E-XAr3cGox2ASF9ZnmtKlYzEwmGUb_c4eeGY5y7y61tuNvhyFLD_4IVAZEcWRhbSvH55dpmJ6ciha_raYf8Pv39ur-_UIbZzSMzRy8i9HzMgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di0cX_GKYFHbfytoa1IU28KDNzdCoV4v7DJL7J5Gj4RVIDYj81UTKreO4MKnCj4FZCPX9UnewaPpQuqHH5xJyLLst_wwz6199V-ApEjQKaNj-u6JGr7aWXqQLtfJhQU9j8Vi5sJ6cd0ZCT3MqKBTbizxSTNP2HdX5YI5jVrYTFJ6uPuQlTtAGTr5w5r2PKCIumFBhBrkQjT3MJc-_QDxY3JimVDo1WXjWhS3s23UQM3CWnejlEEqbzItikyNatkRZwTOwuu4jEZuzbV4HU7MpCwHNyuqHnsFAOw6d6RaurMLIEhwqSgx3VOwHw_h0CbIXN3ALDKL9vgz4F3M3l05Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrghxVjyyvcvDzgUUJRGcoPegUObdojViEYJCuQmhY36QfWe9hf9uAQZidM4fFW-2qplk9Q0IgLWPs4kORwh1-Tm7vTPFt4mqrPwM5jsrAWh4toCeRTcjBzkuZntG56iUDMbv4ZTo4heufmDC25B4455w_8F16HiIqfad22jzx7MT7v8-j5kUZmhBdZ4AfiGFa1R-X-i0oKT92w0HRcve5NuLMS6kuKSskTGGxQ7YvCzHIMwTkI82WrnhgXYWsozzZuNuCAxc0cWEYjvUR3l2ERBRYHW9HAQWX9rwxf861CZD5-ciJdAYAORULAnZ5YJqXYfj21IizufgNgVKVjmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=IbjEG-lHZ_K19t0NzU3mIbKGda7LoZDxXz5nzY7Pe2BNWh0HGwSB4ylDW_aL8ldMUXT5XxP277JYFHC_GszD6Q0B0KjB1SeCaMkssV3lzhUHIZbEpbi5hLEuPF7Xr8UO4JRHwzo8PcEdqoy2TWlpjpseOrwYeIlJplDPhJCVjMA_ia9Rg1a60CUy39RSaqynr8OuupCwuIhWOYgFfAuQIxMi4uGHk9QmGuLMhTmGdUMs0DLNtWREYP1XpLVWI8QpxsONx-WZvwnH5izPAmEoMj6AKwfYT4xRsFs07kG5t3Fm_xb5oTIrwhIWqQtJCdYIl2FYSleAgoS0PMDkKQVZ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=IbjEG-lHZ_K19t0NzU3mIbKGda7LoZDxXz5nzY7Pe2BNWh0HGwSB4ylDW_aL8ldMUXT5XxP277JYFHC_GszD6Q0B0KjB1SeCaMkssV3lzhUHIZbEpbi5hLEuPF7Xr8UO4JRHwzo8PcEdqoy2TWlpjpseOrwYeIlJplDPhJCVjMA_ia9Rg1a60CUy39RSaqynr8OuupCwuIhWOYgFfAuQIxMi4uGHk9QmGuLMhTmGdUMs0DLNtWREYP1XpLVWI8QpxsONx-WZvwnH5izPAmEoMj6AKwfYT4xRsFs07kG5t3Fm_xb5oTIrwhIWqQtJCdYIl2FYSleAgoS0PMDkKQVZ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUhS1uiNfqUzW5QiYvZMpAOx_8ZQEVBNrF2ZTU-3jW-1wph4DAkeeLmJrpO95ArZodSVTRmuhHvh3FYDMYdSooecR0u-7PNv7Z4muatlTkkPmmng8s1zFEs_tF9jECEUudSYMmJ0FV9qneXzoqKo5PK2FkWXC5kB7QhPESPO3xeT-yx3bhITrbgp058vGtCPfq4n6yfe8DZ4lskSiwlgLIvPEiTwKuhIa-qEnmNn9uEvVKMyXhkzTsG2yTBW_EGWYdOJ8x0LSBwIYQXT0Th-Ne55MV5XdcviL75kJ9Lh2ch4-yaQmtA5oKlGxU_51giQK1PeHiLkyqp2bLI9yWmLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=blXg5vFqqZTX9vOeFhjqS1xW0bS3uV9HMVvRWBNHh7-HltDguWg-z6er5-h-ePOyuuE8SV_ZEtazuAeNPu4cyRb881gUXtqrLJkYvFQQvpb8TARzshPLugF0u-ULSijzqbe32Y3gUeR3-ziEw27rayMOVH8_-pvx441ucoB_2KnyRTIAIqptKga__I_SBv5QfIJphcW7eRR2CtRKj-rzauihvnrfh_YvggQDD3uIY0bLcVqjim6YrFv_cekHLbgyTE8rAptcGj5GaD_jIW2DDUsCEPAsfeY9jgT3VrPQVRX0Yq3FDV6DdXoEAcyLrpHl9IhOFA58PvxwQbo0CTzW5T1oy2_i0-JaEFj20x_NMljRLaDlk4Uu2rGRfvuXT1IY3PdJWa6V5gVjVq5UK8CNxS8-jB1DHKi-XM8j61AzEDaD9pFkTJDXxRSuleLBn05JVGAHgyOjBc9BEVai6mUxYETj_6bwnYPbwGLJh4IxpcKHNX_vpRJX62gZSrzpr_oWifAdxENDFC58SoPmiMSTRB0ySV4q9gM0aO-ATka1o5KhYs5jX4KRxH9Uzydd0ot3Eek_r9PMeXox3FQavxPfcdXMZ231DYggUaYgx4p13pfy05Rp8A3QaeDYM1eGLVDEIC6hgsK4MJIg1ZpOHRaZZjzXswjUfmP43RghRix1vDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=blXg5vFqqZTX9vOeFhjqS1xW0bS3uV9HMVvRWBNHh7-HltDguWg-z6er5-h-ePOyuuE8SV_ZEtazuAeNPu4cyRb881gUXtqrLJkYvFQQvpb8TARzshPLugF0u-ULSijzqbe32Y3gUeR3-ziEw27rayMOVH8_-pvx441ucoB_2KnyRTIAIqptKga__I_SBv5QfIJphcW7eRR2CtRKj-rzauihvnrfh_YvggQDD3uIY0bLcVqjim6YrFv_cekHLbgyTE8rAptcGj5GaD_jIW2DDUsCEPAsfeY9jgT3VrPQVRX0Yq3FDV6DdXoEAcyLrpHl9IhOFA58PvxwQbo0CTzW5T1oy2_i0-JaEFj20x_NMljRLaDlk4Uu2rGRfvuXT1IY3PdJWa6V5gVjVq5UK8CNxS8-jB1DHKi-XM8j61AzEDaD9pFkTJDXxRSuleLBn05JVGAHgyOjBc9BEVai6mUxYETj_6bwnYPbwGLJh4IxpcKHNX_vpRJX62gZSrzpr_oWifAdxENDFC58SoPmiMSTRB0ySV4q9gM0aO-ATka1o5KhYs5jX4KRxH9Uzydd0ot3Eek_r9PMeXox3FQavxPfcdXMZ231DYggUaYgx4p13pfy05Rp8A3QaeDYM1eGLVDEIC6hgsK4MJIg1ZpOHRaZZjzXswjUfmP43RghRix1vDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IN96IahReHze1qHEOSEeNMAXZjRsv4ooISoyeE9SBj8satJKSQ4w0CtDE-GsGYapL7Hjmlot3f8nSgvbXwzb7tp4T8VT-UZAtUE2_fWFUUiWHFQaDL2M3hZGI5Zf0dcwvXamT4p-LhN80io2DfEN0lu-P5LYOEM0-VXRyE9y7bAfIVbXwQcDCbkjwjsKPDLm5RWoJOKnmdYu4PljN9rv5knDzRU6jBNpgFMAYwJuZagG9ccZ2W8q0svmKNAqO-bW4UQHGDSzCsrJTS_SE3X5BbC2Ud7HxzaLecY8UfyytUTfWNKWWG5yKQdE8zl_965eV8_TwXrsgAddX0KA0-k1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IN96IahReHze1qHEOSEeNMAXZjRsv4ooISoyeE9SBj8satJKSQ4w0CtDE-GsGYapL7Hjmlot3f8nSgvbXwzb7tp4T8VT-UZAtUE2_fWFUUiWHFQaDL2M3hZGI5Zf0dcwvXamT4p-LhN80io2DfEN0lu-P5LYOEM0-VXRyE9y7bAfIVbXwQcDCbkjwjsKPDLm5RWoJOKnmdYu4PljN9rv5knDzRU6jBNpgFMAYwJuZagG9ccZ2W8q0svmKNAqO-bW4UQHGDSzCsrJTS_SE3X5BbC2Ud7HxzaLecY8UfyytUTfWNKWWG5yKQdE8zl_965eV8_TwXrsgAddX0KA0-k1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGiLeKPwkzWQ9uUOPlEg5MKUzlxGR5N7QI2jsUvsp4bvdAT6SB3Ryw0sSJ9AR3yvOiYl9wDXyM8Wsqs9KxLgDg3yyB1YEpNYdHJsFjWTQYinVeWMxn--tYW7rU8Z1tiFKsOsJic44pc67gUPYKiu4M_bX771IymwtisuYgYK8g07KAZfcl8W5dyCCM299cRSd9I-9UYJhZPyif12j5tVeZ9LvgwUwTomefpq8avVKZTlGJW9TGoUQCgRie2c5RMRmd3g5_reprLNqinSFWUgxxwaD6Lmj7MjzyPdcZHCuFGirTd4n75PVPR8vjvBHuMfX3bErJUWnKLNH5OSMlrfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uan5GjPljwxSWYxX0BY2zGElv1zsf5YEhCN5SGwSlNcwAOj8AQHCkv8wz20Gx5NiQsVsshdj48HQfpeSaiN1UuOfNZsUALo5QRNPAVAl_rNcao5vF5yekR0wS98PRtlsfOTH_dEi__4kKbemB3xomjLVH-e8z3Na8kWHgy_EFJBVzp0EBeVCS-iUOFsVRtV6liRgYG5oCKb0xHx6jmJy2nfMzrIQNyXolS_qlpkCJdIkIPbjylYYVAJVEN84iutWBVOHkh9_aXJ2wwit6SF40VVxTMs18FHkgguJYG5Gf3y6xvXGmlKIFRBQBafe5jTu0XIlzWmQbD2gTNRpbNvVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-RUDcoXnH8pzKil41zqn3N5qvdUdrK2TMZTc0RRlPe37bK_lvSoD8J9_AYj1aBvuR7Wrw6vI6vjcQO6kR2CirdrzaUh1O94xr6hFsDjc__KmmRv9riHWX6YB1uzBpAKg6k8P99Xy_VPuXJqdBH26JKhNq-QbRs5nWqewsv_BzFjZShaD9g6b0G5EPoS4q03jVmYaJiu31UjgyL_jl1yJxbCpUf5eiMQdKDUP4VSl3cBpAtLcY4gAAWynYX7Bre2lWH5hh1X__ZvizAhZZKEbHniFSbm2hllrNQu9857LkD4h9294gA-V5jBd0lWhP5TOWSrbF3EZp4jkXWZOtYfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOdKetYj2uDmGoh9sdtsRHIH9vupsCyipiLmmmpzKv1qESVUdnwnv5WLK-ji248mtb3WZoiHUI5rUNP3cnC8hVpIo8OJhRxa0gJneq7gBUlogRnPzoC2ypXKDiGGkcBmSqyPdwHYU0T4cHVodRocA2-cqI1q_Y2OadlC6Zy2nj5GyWd3Pv2odN3rA-NdRu7NDTWfnzNJJX_KuDzzNor7OWYCK615-8SJWPt7sARXCEEYy4TUaQ5mN6vGwiGiDXCcG3_KIdfeyp2tI1sKO6BWgecQmUEDj1svQ_FwFG0A1UgXYxtlTJGkCNiQdKtcaUwN5GAzpR9d1MEVWDGgJmFVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wV3ULVbhYfJ0bBYM-jK_DoxO5dc-NwBnEEky_YNzNacZMjGQkODF8I5ubkIp1wUd4g407I5ouZcYazemhXe9dqfQ9trwRulZzCBj4ePUWh-Q3IjAUBYXQf-bgYlFBD5fd4SslOTBrvHcbaVGo3Vsrqw4hdzZXJLoW3fFTnIwOOo5oXi2STAV4XoDUjqQLR5nV-pWJ8d6erFvyNkeg0fia2MNJPINl-J9mTnoRcmuKN9L2l6Ux8nsYwCe6QnYgD0EpYS5_v8oLYniAmByCQDiYdGCVw5hL8Caky9IsqhF-97XPzXDG0iu_KV3htRI1uCITbR3v09F6-m061zkPEnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co2FPdErwdQZ7v8eF7v13oyjGrxq_JWINsII2X3YoRMIucQOsiAlIm5VsnRQ-cL5kZqVFLXQb-5jKNCRbmpvM0uEGf0lZdsM-AFtL__XEeGj3MgH4-GesS65ubKGFzsOX0F9yojXohXYTYEP4U7uigRTBY8S5f0vaXZvnWJz3XIY8_qpflJAwOdlPuGWACwBYBOgOz7JaBvee0M9L_lEiMEbYdpihghm_wjIPj5x1nfh14RcmmSC71E9wkiDBeO2VZXJzfMv-0mE3Ol7t61edzbXvcDZbt0PIVmcdOTIG5-exNc0dsEQwGgay2iF1v161zDvnZXL7NPE4QidK-IWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI57yRFHscgzso6SFLAZRfPWox73FwUaETer9I3Zgco9XIBgpJgQMddy-ionHP90p5j6Cg3v-gHrUOUKKobLyDaCOUCml-9L0U_hoQb9NX63HpxoLHZel7_3L1DU0LGkxfN4ym07iqc8Rugb729KspgcubPxAUxfgSjzCGjucBFb_AfM8lJXjcZ8uKfjzGWYu6jkAgi485u4yb6FL9uure7Z5wF9GhjP73VnSBbF05ND7M_6d5UZ9fioq0gRfYe2u-VuafNIqQQtoiV-yrFUC5oePMHGfqJIDdpgMhzV-7eoCsjFLDehpIkAUOzGY32LeazilsPCHw47_ONDE11juQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsxD5Zz9oGlQISOztox5woh2J2dD9xzUF5wQIaTVUXsI2FCaXApDqZbCNf5NcddPm8L-5cLUOj81Kovy21VbIW6uXbbivTK5eDOByphAiMUl5QjbmYaOV0J_0vR9I-NZmcqrIw-pSGYpwtA9OKs1vmrlAtdc1wnagpQqPiwWk9D1RXDRsoJ0MzkxzUlHcqFmtcRx5FfcNvAcJmHG51Z3ha2WPVHuI_Rdxayle8b6p78j00pPB5YyUifVTEMbgq3blkHwo0Z3W9IJ03GpxCVGH59R1-GByMRoqjvgBXgscnyP1-OW8cZjJ6Dy0HkKaGDChvvRa4_5rucul55pZb5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKCBsuGnmP0dQ-UdLHm262vcLbN2TdN9H5sbzW0c_hlclFBi_ajmoHYkdgLuqcnxjrbEIcSprM_sMX3lmIHVJoNTcUzDQo8bb789UGoUW2VyW13RVS6Iiejk4p6JKE34hBG4r6BR6uxlr-U4COG9w3ur285ufbearhakI5w_7_M_CrqwArASrEdAcGcviOuvXmeiT7QrllNzVNyim1Qmm8_piYMdBs2HwrCCFBUVj1DV-7zut2kSuLqJE8066ABA_xBJZ8asR-pNZ9Wvlskh_LFobvYfCOgnKWsMRxRwthkMPxx-4hqtorhrpl7e69q9sFKxU6ARIVmjj8voBo0zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRdo64N20t61CF90DyZ1y4WXDZs888BCWKKydAoHnrZBx17Ov651Yp7qOtouHtspXX5UM7ag0dm4E7c6u5Yn5j8u2ydgXDZKzbcylKQvcwZ3nzKaK8uNRVwuBZhXOnWZjHpO3ELXV-EU5LgHRFGaI6O3ZtDNWEGxdzjOysY3DGHEUxIncMgI6Q60iC2CEIA4WiFb5YjYT809M2phD6-qqwpmurvhj3gtAqd8DsVNbriq6Afr1oCRD_7HQKUqds6Lm4kg4zX-G4HBUnQYcgruZKhsw_fIVrmvZV4j6AV8TKHgz3AtJ6ytftOu5W1zO03yMlEYFxzvIidMyH9fJZyB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIBOZhVW1dbedMYmLl33XmrGDCjNvYqnqyD7wrlhDbIAnRAN5_bkEyLSdpSiP_ss6bRxwc9H-7pp554Bwb6KhEWZoxJJCdHFZbCg1xcHnlxbacKJCuATyoZ92f-U363Z2OWJObm_YkTvNJ_BnIR4M6jaoeoWJlLe-YDVySLIyATJMG-ddbljmzeaCFgJiX965vIyZFAibuybcY8NweKOYjkQpYwiwshn3gdhJLJsvgzELsEY5tJoYGAaA-VOWJCRYGCM_V8xbU-VyJS1p9rofVOL354KwneH-pGqTvohPeAC03yrRtkK60cFv1Wu40NeFHjs-Aar7ZXxJ_hVeq0f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Iia6EI6fZV6cmQ2ptU1Wx3lfPYZaYOT3ZopJ-9AAF2IKVe4RPluS0OWcuQxhyZvX7rfILl5x1ISeSk-lebO8yO6iQZIKr3XEMlNagdR8jW74IKChOxY9VA9ypGpt2fpkX5qskIb9F0MWUCrD1EhCgT1xP7ml9ACX5KafBpoCulhyAYtjWYpu4GhlZzrCd0xvj4yxj-6mtHAPk23Eei-pWOK4yNF3UL1IBTweX2zAb0ugRGT_5pIlPI4XUiNZOR-qH8f-GicHjqmsn7xhoS0uj3EK7UF4WPFwEKK6jejAo4tb0PfDN1iKzROaubjjSNq7ZUqKopLS7eBQH_tigWFXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی‌امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز  5
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24385" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxqfAWEuU4eao3usK4uLriyDfvGdeNzeggeD-NqPb6CIM07uzJEHE0MgF-sFOPqCDG92mVPf9a9MY9pVABXZPjfILcwkMwY6I4rF2jCbN93ES1UxFUIcC3DalpYW2IpwPwbMipNKcyU2LEnKxzaQY5e4KZUVe_0rxIUYi0ig_8HA4ciK0MRwCpfrDBd_LyhDmjuJheBcTiqEBLUH9aKxj6A_WniYsC6_ngzrgbydG1l3bvHiiV4DIFL347tpptr66cqc62EZxbDxSC-rl5rPNcyXBU5ZyuZkhVdHrzo53wQAy4QOlXV1wAdQEPOlPy4zByUy9uP2_TdCi3_heKvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEQ7fWFlXnEv89sO_tE5uvGgSJqnJiGQKOXImPlI2e4J5eUJRAE6wOB9e0YcE8U-4kW4_0mbqgzRpZ0d63JkE0bkj5YTWmVennzm36O5jB6gZ-EsdZWJpyNUYi1A9IEPSh0sutyWz1__H1bFAYk5VHuQTKUMYjI5bmxpoRnEzG6eIn-v6C9aXLyb3HNKkIwoWXILrwbfDuJHZFZ0C8WebfXDkpUfFYZspui8fXVR-cIDI7P1z2_KiusNrRMzeQJwOWsbfhNxxTxfXPOqxQuUfA3sOztkSq1APJcIxDHeXapSBriUAji0TLQuiRIuBpFZ32WbsK_o40QO13qb_7pQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNN_UQXyCgS9dsGiBd3wXJcc9TasnrobI51xOw7y828jrmeTIIvVTbTFIn8p_C_ZPSarmJqbJi1ByT9WlQGFjtAImL0-ILDwRNGVpOO5kx43kShusoGgQGkoj5EFwgbPIZwhXjVfVSIs61iGLVIzDr2Bwx9pCFFLuTP3Tq0FzwqhFkdL7cAsTSKBs6W7iqtQk7TjqZn8oJdDms4_ajtLYwTH-iNMyEsJcTS6Iwex9eO-NzLCrImaZik461fkSxitvbqeTMX6UsY4-z4Bl2-VFazC8523bDKiwSoY0bW4D1HVl9TxixbgK3N9v_By46KNBAOmRSmiHVlsru-BezAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5c2TC56R9nHRzkvwjJCL6I84MZWWXQqNM4T732JkDj-8UCOK9g9k5SuakxHwCrEyDnJfpvurF-SaMm6k5fDFpQ9O1Y2RLRj_2dXyTTB7a2gWoSKKFNpeehHaxbIc37cOzx4ZS0IJHL4S4SZCIO33eZ5wZzVecq4dh7p8LMNtpzQtEmrb0aXGc57F4-bhL2EMM38fCOVFbDHNDXvLM7SPs4Qh78AmsTCnyFB0nAQP96HNnNXx8miQx6j_4tt2z4aUlcNK1nLlJlpRyJWtMhBB2pevRcF9BvxB3Vd77yIhkm8WWLiuMBznhbFEQMV_HAbXXioHGc8loz3Fqep_eQ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8vAvaoSQHfE57Hki56-2E9novrnNWR2xJ7kZKGIFmQbPQZ926peUHylqF7zG01XAuphQTdLVxee4kU_bdhZkt_T36dlkawwp9TM2Tl6pLcjb2JOoKpr-_5Lv213nwjk-Aj47hfN9BbiHKzAGGeOU35K5rVVZFK2jkw0Y3YUwmLHNHsZP6zeTDP1K7Fp_MH-chuyL6R5HMqg8e6jRfLZT0OKWb-sjC-UOFCUHzB3TuPt7XPQ8KS7CUQQFVbD4DHq8Jx7sAsNifRe_jgGs59t0oM0byv7gMslHdSRKSXlf8-m3oMyux1aTeh5RcfJFfB9jx6z8qXf8RWluIZ2u7-_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EagfVo9qqlk9DmlMoeeFyG4Cfe5iI7vWFKFtsLB6pFeRDDdUCBJCmaZRITbz6xKvumV6WfISsLlvGSER1Ob-k5ybN2-E3bHFgqJRB1Uvhj8JM5xB_qNTdofUATJhU1d4hEvWSYKRHo8Myjrvm4TPXOqJPwAxMn_OUPrj_Jjqzb3dFc6clYCAW-7ExpKchcOZOC-B4mdRJnpT2Z6v7djz8L-L_yho6JMkMx3CDxsLJnEwnz65d9m4nvD-JGID99UfKPJihl0jhXMyrTZTOv6yO6z75lT2ADxzCt8LBz1S02ety30q-VUwmKwJmeEhPRD_qKXCRB_omW6x6LTAvvg4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbbC_TGJdKwNRvN4Cv3fskrRNnsyFiPlHixoBk5Stv0bo51s1_TqziDVAYFTDvvIP99SXh-GRBzZu1FDda5YfTdjyd9opo8YKQGP4YIi3C9W9C59pqISSD11p5AevFT2t_1C8e8N0cUjx8n-6CNjwxWxrFnvwGvbs-X9NBNBu0bs-vvCdgZCJq1a0LqYnU4N1q1PTJNIaV3XQB9A7y1HJD-Sx_lT7l_X6ZEv_0MSGysm5gfv1MnUi7fAgVNwarduoM-SRb-PaOXrATT3UhNXr6VB-ll2oSTJ0vT3xnThFmcgVTHAPhfDtCwWWW93gD0rS4M_Z4AwoucoEWN8kDueug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzzLm9ZnvbB9AhhFMYuU33UhxPRIq552v_mmc6jVcEY45_BO36y1OOtVzip0tHX83M9YCdtDqFBCq7NqUN0QizIWEXLzcgH8ICgGNk4q9NIJzWf6OTIb6CZ399CiJeuBSgDaRaayMxfPX76xTzZr44bQHP7Akq8DBtp9DwQtynjetvWPq5Ql7JG_vaZy2qvq-L1rmIVakMEQhgbIbKH4klywwH4s_JDFHTgX6BRwbnjmeNfX2YyLX4WlxlcdVSTxgyOIt2AkjR495LNgZJpxpxio-BcOPDoRcOko-KniQ6pNbf9m9hBMx37J6eqh82mhYhlOBApBdCTtOz2R4C_laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFlPzzGiwuhJOaU3p0QZ8b0_SuC0pR-aH6wH-7oiv-EXik-5DIGAqunYkYVH3FKZNkVnvEhM9mS5CvM3R0EkabtzIny3RtjvldDyMpwxq4QSDajkhhDdaBfZspiupd4dIRCRM61Ljxet0CQHYTnK_DMVUMdsEzifSrhjFAJ_rDBFtuxzW57WMiI9VSS4blKF2jKeLRM4LIrK5_FwQXUAoD0X_DLTKfKq6tsR_ZpfoZL99Aj4Re_OtO79scgsdxUyMTnqSZK_Efnh3ZEFDSdyuu8ji5yOFddAf9vTH-MKTKRRIhyfZcnitN7WSXzxausocyxM3KgPjk5flioG1ZOKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXROxRUJHYMc_UdiPsrDIP1c6md62Ml9fH-dc2eNJLF1c4zJYOwKyjKP776DXOVxJw9aN7xVHYHXhbFkvM3nAQGWJs6jveL4uTopm4dUZXxaE48LYFhCNZfanUns7UUKQuwZ9r_VZuF3WVFPJR8O9HjZy3SwEFSPxwCbOkkeb9xJTlTa0TWR2XG9uDvSBgJnmDUIc8OLt_L18yDkFhB5_gNm2kxVkTijXT8Am7NUpv8mwOJBadveuE2xVZvietDcT09ezA-69K_WGN4OVWEbfx9s5YT5tIDtvy015kdsWd6fem0cB0cCBI4wcNeHYNfnlx41wE6rL_QPFUQtibDhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=pjoua9QHWSmUUzWmD-xyuovpV1_i7gPTO0Ktsv4XF1uWPSeOAr4XoLD8UV1u1ez_mc12UVMAR2ENi7NVX4zG0Pxbq4pHANtbZJiV9xP9ZpZgFOkjs8M9_u6Cj7YJokUaarsZYs0fwjENhXERmM-OCZzaKM0fW1BXz9_K3I1_2WZfRTr2cnGvx5kVI8HXZc2zHdlko_GUvVj4ietTMwLpQ5f67_3Ky3KzMh1MBEPI5_WMsbFs1r0n5yTsVZqVZQZ2Y35Lw0_U10IaR__fVg5zpufICUk8KdWLIrE8NDqKbcwY-S7anT7L8xkr0Dr7C49_0ckR08nqcWYCCXCv7hWWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=pjoua9QHWSmUUzWmD-xyuovpV1_i7gPTO0Ktsv4XF1uWPSeOAr4XoLD8UV1u1ez_mc12UVMAR2ENi7NVX4zG0Pxbq4pHANtbZJiV9xP9ZpZgFOkjs8M9_u6Cj7YJokUaarsZYs0fwjENhXERmM-OCZzaKM0fW1BXz9_K3I1_2WZfRTr2cnGvx5kVI8HXZc2zHdlko_GUvVj4ietTMwLpQ5f67_3Ky3KzMh1MBEPI5_WMsbFs1r0n5yTsVZqVZQZ2Y35Lw0_U10IaR__fVg5zpufICUk8KdWLIrE8NDqKbcwY-S7anT7L8xkr0Dr7C49_0ckR08nqcWYCCXCv7hWWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz6J_6vAlYCqvIcgiBy3mKrNZwWzHrCB6D-bZUd7sHcR18TjOzrMrNU7w3dSMvinbpXPjygj2xtKi91g_Jz7T5Z-z14M3vlrrjDGc3Y02WY7bjajApzBNGpZepXQUX-yiA7BW7eumfE0WxBCDJ3pfVO6FQsMwTuVmiUqoFHPyRq1lem2-G2AMUwa8AqjXM33Z0kD6UiZmaRmsQMf0kVlOQWXqhtguQn6SfEwahzVlqlIAW8l8Zc9XV7c5eei-WnxcnJ28ZiWe0S0NNlH2WxsLT3U3UOdki107wc5DhQkJFOjwQp1L6hDR13DEEDmNTs6LHX9WccVRgyO838WDflqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7YVy4wTeC2I6M1p10Zb63bZB9V-N-tfnoYsZujdPFSgPVtCw8x-oufgN4NiPsN838hdczRORmICQmDC0I2hjymkzRLnuKGclouxK0Jo5yhacEn8y87azWgeGrxPnTOIS8XaAs0r-_IHi5sSvN6EFh2czxWd5R__mPQUP4pZXfgdUj-9N3BvKTU2cCA83pBGErxAUEgWjsEYSHD_jNoZZqpr81GF_HV6SJ0oR34eu1ruzQT19nYKgFxuyAsfAwDjCWMRIVY3HuSZEK2QGWffbajCh5Z_mO0fJotDZ_19BXPc4ZZ_NYEStwQoidekJQCsG22y_N_P9zxIxYUa2_Npng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWIujCFNNI3qoCjo9nGWt8U1FQnRqCpXXzKGGx-ex9r2DOzg56uPQ-BW3h2ePD2dcz1oDSVvZlUrTqDuVH9bKxf2atmhw8cFqE45pinEjPB4fZzCTou_O4yb1vWWqY-ec-gDrs2wIMet_0vkuiWnfYJ1oyKw_S1A80WgBOcTbZhWR2OqzgpObnoM_e5lKqXs7t-mvDXe8B78yft3E2y9hMJkknsKFO_AFONNQ8P14JMtmeqAQEqwMS6jNlo9r6Nlka7ufJI5UDOLpJs42Ri0_3Bat-OcfUqtF7Wy4wJodu9o8arsP8Bv5pIGW_ctPaZ4_Cfw2n5I_Rq0Hw_yCs_faQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9sY7JxCe5orYuCGGRp3BsQQw9eEmZS_Qoij7gRIJYJK5HMe72-S-sWvpj2L_hg1db2mJo5D6H-OARh2SWhcXkWF_W4lBh_tJ3B40k-tibOE3fpQNlo62-c5AYXKZXevpl1T7A2KuCbkoYxZdcsqnra-XkL5A8WRs4tIbwd_mX6v3hrAiX6fj02WO0wq5z0EZQ56U_Umtu-JDjoKCmkjvduKmHYSZLdb2Pj6MQnJFcj6vpZvkznPkQiD3mI5GfzSdIVT5PsU1b83eohFcEu2ShZVETkiVNhbkwg6WK-0GGvi_Kz8xxLJChbfy5EN2MTyw13YYAu1VhMhrua3hzf4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy2hgCGFYSj7U0QTTntce-sv1iJLOE7ngzBlQxC5_ZX0oANebJUIc5fLEa37Gypfz4Pj67aYi1ZKoiF1yuhmdWf62wbwcLclemKMs63-BKgpwhW25Fc7pMEUOcC-E8SC2dJ1m7oHNXv9qsw5K3Z14NWXTqYEuSQu4tvyYtu3nvSoPj1-LzkrytXKB75Au2G_Dk3WOiObIAKDPeDj8B7wjAiVUEOrlYLUvLBtNq-mFNNw_6zr_E_Im65NbT64Dg58NwzTjgMhV2-B94OHUgBS3drz5sTF6z_Et6TJTar1sAPb1nDzuQSDpfBDGzuIQpC7um-jVGxYc9GR4xZ-MItIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHM2qTBQFI2PWoZvj6ny9cWMVZ9Y0J7hg4mROrwS9T1bLWl420vEyyAswtN5A3V4aa1B5Peql8ksi4Ki0X6e-aarsI41f_fBv5KtNmb-LuHqftADA8xcZB6Bm4asi1j3DVpDkXN3rEeBUGPVHM64NdQy-8Nef4Shs126yycMShtri70y1lf-yvQpz_njv3_2CLB2OMGfaqXNBc9F8MgAmoXCkw6lX8_qgMgp4KmQ0B1LTZbTVWAAwKN2qvAiJH9_RO28tfft8DA41oZKQmTge2tBW3uDWrEEgJZSEQuutq9WCRRwfYikQA6LNzQugZYQu9j34puN5OPLK8bANchxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIa_eAhaI4WVa33haRI9NEmHvs96ySdVTLy7cEx9VF26OQ6Vf26ijxMiW2yMlL6CJLIoCbDyJrJcUrseBCk2dfc8k9MXVt5MCssZDqtKOMZ29ENuMPLZODqdzxJ8q3SyU8uIGty0Xqr0Cp8odBSTuT6pb62rsFCRyFP5hMYkeMkJ_OPb6M9BycxXBJylryvHuNtL9fAHhoav_Wzv6f5yKRjKJFXpdyBtoQNAYp3YjmsmzqG9xp8iRdV0zsjXuwiPcjk55uFAjhrZfJpaC9RIS__W0AJi6F4Nh_sX09Yf3EFb-BFOxVL0BZP7zoL2u_MutEkx4ebxsz_-axYan6lbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou5m-3S6A6fssi4S-CjPXPmfAQQMHAmuUmk3hExrjx6-Ffw2krIM7v5es8duC5hK8w7g0VJVasVQ6J0uyj4WBMlBkatnT9TMtIQ1qmyuOKfpGuqED72BboQTmPXBJ2LxcykfCxvt4M3T9aeuCpQ4ADJASlJOJsyHZcz6ugqrrIwF3nedqUaoLkVsGpXLd24gTh9GxBXTB8iGhzVKmM2vwCrqfXwjOt4--QN_fQ-mWr4tpCXRbmwTIdnpuS6jcDWEvAuMaWssBbIyyycL3WO1s_k5PBxTFoslDcJK7uBFkrSOvtGtJFuZeXKnnTAiswLqlAttsMauWqzDURokWpz23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upiFSqODacQdRwNUbIJX0WGDqfz8V_tiiQiJ-e_5gIidr7rZeYZNoqKMUwiw3NB2e5xVHiLg3qVX3p0OpPQ6Qd4ZZqMP0LFuw1Bel2QFk1-mPdeauX6RR7AU4svf4lZnr6gb7TETTcbWA11LCwAB3RmKuAfjkT75yhTCuFgsAZ7P_bvxrwJ1BS91ZzReQro0FwpWlfX3iE3TwJasMrelIzszLcIBwQY0hSSyAdhg-uBVLIiPInNlRB-gBPtXbJ_vGqpigyYbAkR4xSg8AexW4JAnZUpOkyTfA7iGDNkY5ZBHwjFlmkGydYLqA6FTf4d8e37BWVblmEwY9lYAgWQYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=Y--r91oiZ-TwiLq9DJOBpwDWWL88BN-fXRO8qvFTjgfMfinHPkKPbxr0dgyCqnZMz1OBHbZiXuouV3WtNQi0iLzpncui0q97oUk-tShDj3zlACpLH51hiqsgaA1g5LIIz5SgK4zFk2W40BS8Pi3-t2zhCQxDobVaYBs1W4VtPTvtkdqepTof9QxDqOmMbpZqvSS9r7tej2zK9CPOdilo0KvBORXFjcVveNyybmLs8r7vefIl2wjyFy47HErCJ75t5Uhsy8VdkTnaqIuq5kbafnbDvhs6yBqCo87L57LH1XTNfGlqe4a8U_38hDeDp4NF0jrbjP-HxeygsG2aT2qEiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=Y--r91oiZ-TwiLq9DJOBpwDWWL88BN-fXRO8qvFTjgfMfinHPkKPbxr0dgyCqnZMz1OBHbZiXuouV3WtNQi0iLzpncui0q97oUk-tShDj3zlACpLH51hiqsgaA1g5LIIz5SgK4zFk2W40BS8Pi3-t2zhCQxDobVaYBs1W4VtPTvtkdqepTof9QxDqOmMbpZqvSS9r7tej2zK9CPOdilo0KvBORXFjcVveNyybmLs8r7vefIl2wjyFy47HErCJ75t5Uhsy8VdkTnaqIuq5kbafnbDvhs6yBqCo87L57LH1XTNfGlqe4a8U_38hDeDp4NF0jrbjP-HxeygsG2aT2qEiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htNyngyaF8-wTbbdmheKMNQbobMc1Td8FDfDJl0IGXYKtHGQSeXs6y7Ej0t9JAXf_PvwGQq221HCDmZ24or6ORzHlXAtdcFCI2Y5oI2_FAYHDp_TUEiiPKdbfkvyKwjighHCKfgdiHu6rXTpTHG1GXgRHRnnpi5McIUxgBgBEy3S9Pid9lzYyJqJwQ7XsNptTm8FhF97rL2Xo_5ROUvGiI-EBoZhPlxHPQP3y2HM8g41bBLdCO5ao0s8urI98CJ2NCYqd1AdB5ZFMbus7wao5z2N4G-YYGiJZzjBpcyk7-dwuHcV-J1ng5V5cqPs1hgCLuMpr8Cyia9uWBizvo1daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Zu7Nip-SHhu_PJ-MJ1rkCK56zB5_nwxneGcT8nA_OEib4DN198Vq4a9YOEzyEQIhNqD215uW-EJUY7a6Bck0pFFMB-oJkBdEue_8hm1FR9vAc0WJLsFI4XkKg8HoVA6E6lYbhOM--u7AXak_ikSCNa4YPE7dr0Z78lIU4xmiyKtfosUqgDFjGY7BJ-TezoSy18QRtRcy705-DqTEMLy_0w1S_nw8l8CVUwvrWsNj-AynOOnrRVVqhEfRrDn4Lm6E8jOHBNPFxK3TQZpTd8ljylUM4qtqSPjlWrvc4aCTX6Yxp3sidEzTzMdl7wPYe2RalP2Gtffo-Ey4vgBweNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brK4LOdykucK3P4nRU0A9UQbqb94y89f1Kz5YsaYr-xVwE_Ss900cZRhdmnfMUD8PUnJeoEi7FgLkUztvdXWb0CJTuhHAjNG8Flokdn26vYlEtMUl19l5y2ZMPZQJI02TDcSe9c_eKqFD3_BOk90ql8IMHge2V0i4NNiRkkShpdZb6TT1Bbbvahi3RJBEyAvQoJtAGmV7ASanrY8_RHHhdzd-JvC4EBKcOYqDae1bDASoe0LGc1jqrZmicRmO32KFSF-86EHuPtzNHiRKocdLJfD9bfeKTyFHyAQhcSUu80VgTWquEOwOOolCYGN_nUcKKP6NDgRiEMg3SJZsL2Mrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS7tOt0uyn3dLz3wzGp12_1vAk8__eQurUGzLd6PPW4tDbQ6BoGP2t6FXpRpHCL5n7qR7emL_VqrJUBWSxELo5hcpURFT2WtowmGfkXRWfGUqKWN9T3cFn_WOctPhg7mhzl2T0eYbdMGhY_gnUqs-4gK2SJPXrmhQFYyJDCF_l8MFUgkDWzRJfBF0WZhrh75JStEe2y_Yv6q8UVurWzpdx1doErAUqk6sxaGFrcLY0Oh-EF76ogbKndjnxBrFvUoiOQqWTKSygodJ1uj8BOxkTJer7CsTQVw255ITAvg5c_LEnTSKILTQgebFPqvEwGk9HfMj0x0gug9HNaCWKuykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6SBIoUI7q3iMt_krw5OiZb2G9ODx9r_4XE1WmsJ-eRh-eqKtSAH13sIro89cWEj5mUvi3nfxyA8EgcWa5EaQc-J6dLsfE1Om4fxCC92w-Lcw6q3sg_LEIb5M9tt9S6YpMJrq3dfaKA4bGj9I9TDXtNndWE27kTsSTAOsHPxGGAK-KOfpT_c9brqDy7ubD9CUb1p6ER08-3DXuq3bYb4uLVKRqVknVDaquoWrLI44irUL9C47oXS3WHE29ZcAy3OcLySrCm2A8YDn08SCa5BPX37smc-IQJZDu1xpKVGsNKVYvuX90Td1kZbomoJvXacOwcDu_34MrMk7XmnVNffvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=ZqxDyM5j-TgoRcb8PzLk9e9FK3GyL10sCX-LxUhOS1i7xa7Cv2Za7fzClNs976HjQ723bewcJAzLDVAeRYGysAEkzYiOiKqaIF9JVbdXny83IcJjsU2Lk2VEc-XDk8J0_GDU5F-u3TZxIGD9EsTeYDx6gCZAtquoimZdNohp8fuarg3czks2Of0u6TzqDGSbu7qWevjp1jCzSWjIALr-wxrWRMHcBXEjRAJN9wEP7OaNRYQXykk9hzEl4PXl2L4tX5uKeJa1EHExWsoJrqqfk1bvQctCin4s5lnGH_Bfzk4k9Zfela4rpBQ_WtEHFjn3tIrTRsKiuLNXW1qkd-CG5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=ZqxDyM5j-TgoRcb8PzLk9e9FK3GyL10sCX-LxUhOS1i7xa7Cv2Za7fzClNs976HjQ723bewcJAzLDVAeRYGysAEkzYiOiKqaIF9JVbdXny83IcJjsU2Lk2VEc-XDk8J0_GDU5F-u3TZxIGD9EsTeYDx6gCZAtquoimZdNohp8fuarg3czks2Of0u6TzqDGSbu7qWevjp1jCzSWjIALr-wxrWRMHcBXEjRAJN9wEP7OaNRYQXykk9hzEl4PXl2L4tX5uKeJa1EHExWsoJrqqfk1bvQctCin4s5lnGH_Bfzk4k9Zfela4rpBQ_WtEHFjn3tIrTRsKiuLNXW1qkd-CG5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNQbc_ojunUpTV7UWOMHMuLANwWauw1GuhUIwyh4csFJaKvk9V4zG1UQl0zi6mtRualKXr1qcy06vPqUPYzV-ABUs6Bbp-1xssZf4mz9cgS58MIhnn4dEIgLNgMKy6JBNTBKCMVmqqmtrTHnxFZ7M9ZAHbT2XKatHsg5UDixKocZxmBWVSwV7sL6eq2AOArczpbLxj8py-Fhgmds0iQyDgwZEIzoNns11D_movZLIlmNAmQWN93omZFAAe7QBnxkzzJOhpwSAORhukZaTfGZaSykk2yI5umoM-mvKFJw0GEcS-rCX5m0_UAw6z7w9f2AqoM7WQqdrYb30svr-9l8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvynHpO9ZlqcQ0znGqj1cw8DYH2v1YXUoGAnfJYtrACtd8nQFPmS6Qm_kJ-lz-tMgIhAJTmB5uoeuUOHTj_pWI5iLMEHAM0GE8rd2tMQf6do8FmDL9U-grrcyaTbrUeglCc4l8x2AmbiUOqzIlQBrduAi6Q6XhGSiq7blQaBFIsegfAJqpO2G9neXTGcFEIbYqpCSPJYrDh2U_R9U6cITESbfYOXEUkW-tnLlzbvpLiQZI0s3XCGdmphTuqfY-jAoZq3WhtIZCdgfhdCLMLr5EEklpY8fxVN0oPnjskYsQFDPPbz-dwj4N4lkUVTCxtbyXKr01N6ZL8lvo7AKv1cPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpEOkiMgH33F7jvLryNX5F0bd4FmarIrvsRUjW-bRMru6Vn8ruq3Jt6YWzdpSt-a_Y8GX9H65ydlgyX2Ukc5BNxaXsgoWyjaF8FZYy8atL_JzBfy51O_OmtcI7V-l1UrvUJm1kYjzwvkrd6p2W9VDjozEir46mceo14t5A36HtB1IjsziJwgRbl73Z4kIuZny2FbZM9GqOfwMbVUlbX2mr_0cq0xahCmr8gj_p0LTacWJMD0aPES0RtRqmzjUw2nFEd2BvcGoNBliPxvu3wqUbAuKrMOYYY43qTtqz2-hRMHI0VLbL9l2W-aH6QzfK-tb6c2lR4c0_WDfRBG-0js5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AZ2Op95a0WTzO4rb1THQ8mqOL9_WTI31Z3t5sjs2tdOEGUdGBWm8tDi2GelZy-jWzX5iyo7xQ9SS7Ui1uWgd_YOII6IdZrkdhh27WpvM_qtn7bHhmbECqESwK2wn_fzeZzGWFgZ4wSgnqCtEignGXhPxXQS8uwqMPAit9fPqmcYJyBiSW0uhcFJ2IcT6j-htuB3YdHpYEX_ww-O87ILnhlZsvUEy1s52hVEbtrI28FpRPap1Cl_IEgYH31ANV5kmlV_zxZswwf9XowlrXVnHxAoDJ4AKQmRuZXU95tLhs3Xx-Ah06yzuuTlOf1PvzOvlO8mZZTAYNI2HsyXkYVJxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AZ2Op95a0WTzO4rb1THQ8mqOL9_WTI31Z3t5sjs2tdOEGUdGBWm8tDi2GelZy-jWzX5iyo7xQ9SS7Ui1uWgd_YOII6IdZrkdhh27WpvM_qtn7bHhmbECqESwK2wn_fzeZzGWFgZ4wSgnqCtEignGXhPxXQS8uwqMPAit9fPqmcYJyBiSW0uhcFJ2IcT6j-htuB3YdHpYEX_ww-O87ILnhlZsvUEy1s52hVEbtrI28FpRPap1Cl_IEgYH31ANV5kmlV_zxZswwf9XowlrXVnHxAoDJ4AKQmRuZXU95tLhs3Xx-Ah06yzuuTlOf1PvzOvlO8mZZTAYNI2HsyXkYVJxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuHFxF-cJoE3YxEJNS3PJm-TnGdCn4FwRyvuTzwJcP1AWjJ3gWb1goB5FhrP4yKMTu4uS014I9wwWXXRQYb2aFvnsVHhPl_yn0b9x5JbfkCmB1tNhEIOhvqnJzVR_yTnntMay-xfmsbve53HKP1YQuuRZ_zpTPcm_AWuyf01Cqo7Oslm-pw4gtnauYAoe5LzdOWdAaDGFHBxMHrSy726u31fvcuuoO_Gv82nbH9yA04LUCd4z6xQ9MSNc_AuGmPAfx6EllJwtYMTaq-XD_pl_II4unDvmBF0G_c2xrP1pHBQ7D0XhZ842Eym3tm60QBuLwVfpnpTgGdZT3WwKB7qNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnSnqTsFqJoBwDEspOTNf1uQeszsFptWvJ0_Ij8h4iGmrpD-nHxSCkiq6PoSqjYcPNg5IUozKzg1Q6GAl_J1sQpeRW4cn9wzJYKvxEuQ1CuEfPxvLY3HboehEfWFGch-bqEnxmZu2Kc-8DXL4uq8ID9bPAbCYdUznIr0QU-hsKVvW7DiTYiWfSViS2xTnmAK7jphH0NXg9ImhvkZEowOQ4_qnBsxtzJCJi-T1REKk8_bnuu48fI_-FNiJSjz59fthIFncO4qi6hJZuFGFfygdc5Z5tvN9dJIgE49fa1lu1lD9QlkoaLcB-PuNl56bc4lr4MioUR-pBfByJZ_GpL0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD3FHYgpBv8YC1Rkd0PmQpjWaokKFLLKvVABWy2ItQMEVMGwcA4eW4dQIQrO5p85VfEOyuzOopnYlab6AfA-vMYcfQ357H2fLgsRUVx2JFq-zHY2r8quZAk_KWOxP7abdFqijATyIldgapXC4w7nMpnzXqVr9RItYWayUt40RhK6xdztGT48anyLxDzRyXRAQS5RaI_edBGlbbWwkP8XFWuomhAd1ZGjsc_scRHdka5kgD-vtRHLRJeHKEGC9nMEoEV5B9XPEyCulbWWO94gEAPlfrFV_Ut9pAqwFKWdMvy2vCA15H_7FtwrS4lqBVz-5ka1Y8RcfVw9uxLjR-Ewgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwgtbyVJJJhIO-bqHaBpX5pwRPYdAX-5j98NGx1NXBPl7rAMM6xhvwSMN41jysvEYtSa4-EdqAuKLjZbBn6zXo5zjdv6v0nJc3G-49x3YZyFXsJmbhnOzWincjr9xnG_1z1Wd0YX_lMloJRgmDkaYDze5REKs_2GN-0Chgl3KcNESrp9LEjjan0mu8_2zGW1rKTNyFGmTYoCv__V2CCTDZ9-9GHAdYejjFEXItNH2j7iIwXSITgjtHgfFRlBxcGHx5Z-kauosiKntM5LSNxuUvxRh30bIXt328ZLLN-Z1gQuPfgDu0_ip9P2Bu2Db1dZ8nLrxZrGTRQNP2ZNDIat1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7r58m1Czk9odDnp-oFrevlDunA6xE_sK0WFNuhQelB1camUHRxI9A99j4irq8ll8ZAb2DlpI0ne4uGBB6x1GgNCMtLnbm7er8pTLfry3zBP1R0yosIs5mOMn2HCN4ziqBv59Z2ZLJq4n8sODOKpVGYaUtVlQxwkKGQD6vbnzGUk-q25jgX8eg6erdoBSspD3Dosm2Cz4sg5NHlUdur7rhG6TMzDOjD1l33Djm_vPYmTcJ7Ots9vV0roMIR3wN-BaJPEQ-JzJ7wzGmqYzSEear3TetWmN3QBYn-IJVIKZ1LLZhnAuj73m9avhqQfwgc0betywESQaMmYR0aFeUNIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7xpSCJE2NnbWO0nB5MvWW4FIjNajOZvtxI9Be4on4n8hwkR6G2z8IxqCgp9lVajQ3kJNFQapFXPHzJWM-0slJASTJcEPG1oJOey7g9kQuSaRTlVvcS4mX9NjtFwG6awu9WgMwLNi0tqAypkojCxkWt0h-bnyCAxdevHKMZGhy5clT1awZdyckk5l9T6f1p-mCh2gZrdFP7IbL5EsY6JSH0TvR48UNpl6KGSVWQn7x8_5nABJ92BJa6Hq7Lo3yxbELWMU3MCh2KKri3m_ScMzw8xMQWsLBn_3KR60r3albfh-FMcKS1er7KuA_5gt7CWVBmaCXcezfzldJrUO3-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIVDkCbkGErS3k3a9sXiAqcbygyMTzQDFaHR3YGygEZDas6LjObY1geFlHEn9I-lzT0NURXVenUKx-u5bK49uUkzHf68kabRbKmdxhOhAE9GZRhkytY9G2BkjRb0ZgYK6k5P82bKp8PWVkXVCXWWB2hXB6tKTwlQ2T45n4NU9nUH-CWLCGM_faBc57e7GiPk02vRstFNWtIGIxDooMus-jGRlRWkKRsafaqZF6MF6IjbulnE1N2akbVpOtWKWryiwQ3tPV9f4dkShoOyAFRamy7Dt56IG1jyuPTJSqaVWJ3d2Gq18TYOWhl2u6jWPmtUevFulH8Pc8LK2Q86dfiSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umu8y_fIRXAfewTHI6x7No33NNNGgh7hhVQ7x_ZeUOoCrgL2r4d7uYUOR36ZNwGbnDvhTh2vCraTn76_pXafaeth-RNUCs61mStpMJqxrTrZaTYpal-R2_hslUzH5x8R11gtNUkQiYb2bNdeHgSvFddpiaL1jzSTbC23Rc_07Ipc5vvuYH_Lq0WFtbtPu0IxCRuWmLIDQFm13NzD3j8D1_w9tJANk7QNaLEIRJd3JQqLdvbyRyQ-0vojw-3BJ9NJurXFX2m5CcZWOT1WpcQ9depeFLRMUpZXwLkZIuW_fY0hVqQ6svtIvldtbjEgHA-ocGkW2IdhdfcDVgLGjBalIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=C4MM2rp6tJmws3GhG3LVQ0VHDUecYEp2nrpHQEUxukQZDHHF3WEWZd3JZ2Ma3dEflKXY9aHpSpMnB0PBFw4CEJ3vgu18txnirJdDnHvbVsrXDTK26PYNMQop-YTyimhYeKsNzV8ewyJtkicLho3aRN6skk4zUnCzkpee2IbSIGoWfWoT9uriw5JGzBEIGYbhmf0COMDHjCHMEDuCqA4vWsHVPe7KnWXq5hoM6aqGRxlAkTZBJw2TZFWthnK7hgovFL0VCvPECEmNjfv716Aca5QYoN9NvV1kB7DFQUqBVeuYzy0o9LMht7XN8E1OQScMkYRSq2v9yn2_GVkQjdbB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=C4MM2rp6tJmws3GhG3LVQ0VHDUecYEp2nrpHQEUxukQZDHHF3WEWZd3JZ2Ma3dEflKXY9aHpSpMnB0PBFw4CEJ3vgu18txnirJdDnHvbVsrXDTK26PYNMQop-YTyimhYeKsNzV8ewyJtkicLho3aRN6skk4zUnCzkpee2IbSIGoWfWoT9uriw5JGzBEIGYbhmf0COMDHjCHMEDuCqA4vWsHVPe7KnWXq5hoM6aqGRxlAkTZBJw2TZFWthnK7hgovFL0VCvPECEmNjfv716Aca5QYoN9NvV1kB7DFQUqBVeuYzy0o9LMht7XN8E1OQScMkYRSq2v9yn2_GVkQjdbB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGYHFAMvbVE_uqipZyOElq0amYgJ8L6oi6tFotXJWyEIvsmQ1ecUDcVjMjrg511Rx7hBm6LIPlRKB-uTX3pAghJyxuC3_dR_BIx14_WVpWxB8T_2wu0JWyVCTQk8vFCJSEC7woyrwBBEBjCmfDr9YA2RDZK9GsvEIsBhZew2rk34J5BxRk2Bi6R8kalyGeHKzXWmWVb9iX7cv_xqTosZWcWFSzjDHt18aFlUB_se5gblaJVG0g8rLiiABH0ZPJKX3fEktciflDO3uEPV038xMBL3OQmp3E4JZN4nAc3fIedFOIqDiWdVIZypmsL9g3-knA6a9u7hUmTNbDmA3zdyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4z0ugUGk48ePpgHHeShZm5t2qesVmEI4nAFdAh_MD0V1QBPdurLyIThnFw7-a7Nr00XGqs8Zq3LEj4Js3MvJHLQFzlyB4BRogiPZNg8ZIfKBQ86OWQWkyMvS1Zc2xZK1iPlX1liNqlLceJYga0ry73LYHKWtGMcKG1MPUVA2x3UIveALW2pVe_Wn1Jqo-AkWvJCUE381Ik7lBi1d3jIRy4g8aPHXjim41NblYfl8jpPNjzjbFV435nqn6loH8kjJmFSrA0fo0sqameWtMMlT5OgXnHNvZKIudm1WiPwCQmcXw-MK1NEijCl5iWv9Zr47iT0aHrmZM45-J2vBY3w3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2k-_17m6t5qM5FmUugXdXhbi2FTBcjAArLjMJbwmnIqLeYwvWdGH8qarooj3x5ZQtbuciZP9vKhOV7l3wvqz4xHPjBcP3WNiUA7J6rv5-T-Qba1MW3EuD1wz-7FirtwVISxOiTcld1IV1S6cerizpZANvH2LS8a6AAFcbhemWoebfw6yhYZ7FeP-LVk0C_4lUhJc4HPLSpFI_R1gLH8UTsOCc92whRVugbCKCjJjv7lmnMksEMgdj9dKvS74q2-GkKp2TKFGyGBo-J9nAQ6adhhQnEag86H_4uA-eukRuKgqHyo61HleN3vHe6p4gUbzFyGE8VziORfvCQhqmCOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3tVdcd0GLEHV5N9yEmgmsyr5fJi8IVYAopWS9hlsX1BBbM6F5om1d-8ov7MWL-HkOwmyd0CjUIrUXcreLUQ1hKuQ1cxfi2Wd4j-PGVGG2tkss5nyazEWeOIcX66Yn_foCp3OIced8LNyGdChjdBrfBVivoEkc8Gm0wnHzxNTfJbPTGziFQwsqUMXwIOyiriNXo9NyHT-mH-s2KA87r30OAgztjdtgbN7a6q0Pg0OfUAhr9veaoIHWlpUmVyph7UGSXxBg5Z4_UPmecJaZf5_lRwATX8co3ui5gMFKyoTq1N9ICyKTOdpYrG9PqS-TOlSsjSzWITHoxnKfSCu5Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=Z07tvXF24VwZQBSfUpFHogRJaBJyjpHG-pOmNGCK1ko_Zb46G_zJ4aaWBNYagQXljHiP3lzR5stfkSloXDn3CSnuFmCv1H9wDnPcgHsaSqyHhbV08VJSblfn5EoXXMrlrAsVSygrTNiFCEITsq1v-qdFzYlmj4IiEnYJgjtsYi7CisCzSY4z3mF7F3P2pNv9IiIYh8QJtmSTc0Ke7XYNkHyVBnNpZELLEg77LUAPi2UbQcwJijEZf0WUpMYB-ZjiB7-PaxCFDtzkWFFxgHZObqivMDbKcyuRRqivuQQK9Cly9eLReLzID-rMNpGMhPt4gsVF7p7TY6k21WMjJ7eTLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=Z07tvXF24VwZQBSfUpFHogRJaBJyjpHG-pOmNGCK1ko_Zb46G_zJ4aaWBNYagQXljHiP3lzR5stfkSloXDn3CSnuFmCv1H9wDnPcgHsaSqyHhbV08VJSblfn5EoXXMrlrAsVSygrTNiFCEITsq1v-qdFzYlmj4IiEnYJgjtsYi7CisCzSY4z3mF7F3P2pNv9IiIYh8QJtmSTc0Ke7XYNkHyVBnNpZELLEg77LUAPi2UbQcwJijEZf0WUpMYB-ZjiB7-PaxCFDtzkWFFxgHZObqivMDbKcyuRRqivuQQK9Cly9eLReLzID-rMNpGMhPt4gsVF7p7TY6k21WMjJ7eTLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdWYYev_NsbO0HnqCCD8-y9whiiBlndw9LLa-wub_V2HNbDEnFLwbJvu8JM-Q9vCZthDvqTROQZObF1I7e__td7NS8BzwJYCrcxrCluuQbjsSoPPkMwx-1UqsA1haBnvZL70vniGrdCxwoMNGUzs2guKr1uFktF-9qeWvOojP6qEAiwnaD8Dg8cXk7i-6eOBqSQwMGPcXyNJwuIcXt69kCItHHtOL35KGttl6IU-YKEvL92lQwXt9dcCDT2TbeapVBXJ1-Rtp2bIvBUPQt2zqzYln6mWQ5D-UE7FxMGb621QRyzdqKQJ9lymmHV4--c81Y_juj3c9jyIBHiNiaLAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX6M5Vlaj6uSd7Fm5gGOnl8_NzRowAKt-ilJ5ASNFNXATwGRdw8JQ5JIXhpLHmAUTMoo8gwaieSJ5-E-c_EWMyrT4RIGyXuhP5bjcbAMz_HqbNucHy0S2UVS5IWXeWkheWIhbkbcDqhub1_DpkOO0Q90uevHWFvR0sTcB5pyZdRvtmM4qsK6TB4OD-UE1kmQQDN9L6vmo4XzzoosTU3kfxacSnSl6-iv6Z9XksdL55puAn3nMC4VC4nSI4dX4uz4VK11UlMzWg1CMiwqDQchUu39UyZm3nEcr8505T6_mjyE0mRwScgZX1zOjMEnPyf0eG_wWr2GK59B34TncYiJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKq85cJcePBbPIszd3vzmHPgY4W4bsufRMmxmYWvZql5vO6vy8POxKzODHTnG4vWpwZVTzWwU97HH-kY2hQR6B1-027TvIFzbat9n2H_6MNUAeI6pl8MHLZhiX7TC4GH1_-ZVjYy1i2sBPAw9uNzror3ywZqkvmkOkTMHMRiy_D9ZKd9Yd4HE7AdtywpJC9X8ndxee1sG2jDmJX4idzfBbYsD2UjYK4cgvyRlKMOnE-3XiCkiIuFu2Gqz32DqNVMEDITJzm1S3X-yxuby22V3iyAHnbhArBMfKLqDdA3o7ZutURM8Ng9ai7w3zCrNlQuR3A5volgz2q9CES0frcbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC577alnWuSGz_43T24vKXDGqssdI8ygqZ5Wlhv-AZbbBpsUDSrWBmf-_VA5sTlO4MhFYEbyASp_KqVyH8XCcNqH3VNEPO_D1nMHUDMGUqqptneNvrXMiNdZuoPKeTL13CgxJygag5vbHjlIUcV4rxKY7KmwZ2Q5guidBtrBM5VAEMebAfPtQcyzIT7iV0tedMGZyMZYEAYsc2Swbqd9VhIKuXpvICFV3CiyuWbrlauxJC-sLsox-7CkcmkFKtpau34MtW2c4s7ZUq7MGnNdgXqg8PQKG6tqMavQOLeYne1M5qw2Vq5gmQkcnTFE3dCU_juNLTw-utsJ2TqaB_clNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=hzun0BvnWaKP-4VWe3FQ2sCdVGnmbPHhcjV92htu6v3pJ38S5mUk_UxtTadFel_6q7g2lG5bL6FoicI_kVuYIo-Sr1cri-VQsZ_FrDXZxmm2GMZPaAhQys0-PMgDybomYzWHkntSBO16LluUbVkd0f1_GKPPURSF6G4tFTS-Swl4Av6NQWLPdrkhlIzb-fpqI82xEjMQhy9AJeicRGrBQ3c5SUiNWJyKHo9JjVqDyb4NcFgOFKfTY85QdBCZd2vuy_udaSj59t0lI4UCD8vGe1DbQ-Q-LN2GSYpY0ANlYsxBcJlPKC5NqeB0DFKmIG-jnp1sRw5r95KJ4XI-dj8M957aka17vtPxxKKqs04zcJxbXQ00egUUjIvxO9QyId_dgazHv7Wi2B_3CS0H8Dpl501DqYkMIIQQWrghqRDTxhWR7sg8Ixw_T8t5WXGHb9izAuX6RS7rMBzQd_nM_0amJGUC--zSLioN83fw4RFe58PdF8p5jcwQT1Snk8nMpt-5fGzfduc3B0ZUOpNyFWRGeyRV0wMPZSBiiE1p-gEx9RcPKX7WNiGrvLd7h-F-E5uv2gNFA23yIscC_sez8I2YFuJyPHTZ79AvMaN0ETVrrK0aY5xthhRohZmlVm3uC2oGqJ-mQrZuObN4m9Wf0CWrH56cGYqrghhAQ4hzD7tlADU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=hzun0BvnWaKP-4VWe3FQ2sCdVGnmbPHhcjV92htu6v3pJ38S5mUk_UxtTadFel_6q7g2lG5bL6FoicI_kVuYIo-Sr1cri-VQsZ_FrDXZxmm2GMZPaAhQys0-PMgDybomYzWHkntSBO16LluUbVkd0f1_GKPPURSF6G4tFTS-Swl4Av6NQWLPdrkhlIzb-fpqI82xEjMQhy9AJeicRGrBQ3c5SUiNWJyKHo9JjVqDyb4NcFgOFKfTY85QdBCZd2vuy_udaSj59t0lI4UCD8vGe1DbQ-Q-LN2GSYpY0ANlYsxBcJlPKC5NqeB0DFKmIG-jnp1sRw5r95KJ4XI-dj8M957aka17vtPxxKKqs04zcJxbXQ00egUUjIvxO9QyId_dgazHv7Wi2B_3CS0H8Dpl501DqYkMIIQQWrghqRDTxhWR7sg8Ixw_T8t5WXGHb9izAuX6RS7rMBzQd_nM_0amJGUC--zSLioN83fw4RFe58PdF8p5jcwQT1Snk8nMpt-5fGzfduc3B0ZUOpNyFWRGeyRV0wMPZSBiiE1p-gEx9RcPKX7WNiGrvLd7h-F-E5uv2gNFA23yIscC_sez8I2YFuJyPHTZ79AvMaN0ETVrrK0aY5xthhRohZmlVm3uC2oGqJ-mQrZuObN4m9Wf0CWrH56cGYqrghhAQ4hzD7tlADU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=ReCmClaPI9xo1tAOMQ3FNz4oAxBvTcijV-r6ZZkCBPOzwGe2IjK1QAzzilWukwLmMg9ghbKNlYCd69mE36-dneCKdVbM-zLPw2mT5x5jn9BF7UYeTet4VkeHwSu_EjSbQlxnISp23YpYO2VEk9jcMcz8hl8FH5Taj1AnPeX9Zyt0qKdrGmHSTVqFabCvlrcXv7hY8G8TBcIcPfyWiWvJXRrUeGygpF3w89t1XX1WMM865f6HyrvD4raQhh50dcIQ3qR3PCQqfEswMQ_MhCkKBYX3cl-UxixwBQEaHkBIfXrOlymMYxH3eVtlWLewC9Ucuq-Wu0YfW3cYnqnFI0mY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=ReCmClaPI9xo1tAOMQ3FNz4oAxBvTcijV-r6ZZkCBPOzwGe2IjK1QAzzilWukwLmMg9ghbKNlYCd69mE36-dneCKdVbM-zLPw2mT5x5jn9BF7UYeTet4VkeHwSu_EjSbQlxnISp23YpYO2VEk9jcMcz8hl8FH5Taj1AnPeX9Zyt0qKdrGmHSTVqFabCvlrcXv7hY8G8TBcIcPfyWiWvJXRrUeGygpF3w89t1XX1WMM865f6HyrvD4raQhh50dcIQ3qR3PCQqfEswMQ_MhCkKBYX3cl-UxixwBQEaHkBIfXrOlymMYxH3eVtlWLewC9Ucuq-Wu0YfW3cYnqnFI0mY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry-_9gb7ULifdCSG7zOOHCuFgvdouiwH_dcVG49E8MoVJ8pWF4skF-CHIC0GK-KlQN9Eu6yJxEeSlPGf6EqeJv5-i898UTIalJ7fVCPYdpwFqTTsaxd934BLgKPKdh_y9OFfwpPewdqyQbscehKt-ulOnxC-u6J4hdxWub4j5jC10Of40JYHJ5mDDrC9OcEiGqy413Zj9GeM2KW1SMlQ8ht0xmJ0veDMC0mHugVmWYO4dHSl8waJHKMFsN-dsQowMikP_17ySW3POgr5zOTm4i46-tiudxLcjQ1hKn382gWzOc3GPEJrqlRdulQ2TvrqoSYNyEr2cwlmY007AVjpag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE4huh0H99cBGWqkowh0v2_EKFjTXMgV2XKK2xZ29NYb82Oqpm2NQeJO_H0XkwiHncF6foQwsLSTMOixPfsN0Kh49V6bEFn5mjsXwIUzEnmB9JGYiXOJyhH6Ueb06Ox_82YkRN2Febspxtpni7WUIrHbd7BeLz2_GsyPbaC3IcNJ9eq1yNsd408gbX6i20HfDyK4OCTmSAf8bjneCGn-VOpvpZZFcBDBHWS_QA-7_qjq2A4T7cSGBHdhgd3PSlKehtystUsgpJRvv_Q38FNTjb3a5SluXIpVwFb3JwQbZzrSE47maK4vXxtOZ0a4zKtHNDJ543-Gvi3zqOA_TV1ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_8nsyb2b9IeUiBN-FlhgPUSKqcZ67QOZ-L-jtCP-TP6E1BFncrYYwRI3MSexKl2jsUdSTFqBUG-5CdH5RtIDHb_lLn_wm-v1xThHwQntgk2dpQLnAF6BnjOniuZIe1nmrM4Kq_LQb0XK1898JwCI_hVRjvTY6Ss2fkbM_Q_qem_wYqCxGAakPiWgFvnz9LOyNYI0k-fuWC5QjgSLiiVJ9EHuaJ1UncbHuF3DA30v_Dr5sBo6yIKBi-f4i6ZdFoaoRIeNpbQx3KjcL_zpPBZSij8Ld3YfW3bljuwHYWgja6GKiAhXmoOHII_kaEyvc2QxcqxDtvsGqy8RoTe4Re9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=b1-cg9a3hwL3lZ7jCsZPzZ0R9p30o1HrHykVQ8sR0DjxJBx-dUVmIsVigdV2ivxHUzgil-HLwUMhpZiOounbJET3Stt69ICasAzMwa5dKslqZlQ2vEnzRvaxg6B3JJcIU-B0RxmbFC1akdVI_ioEa7GDHkqRmw7wp934BCGXXZvz7iGtMtmnWG-o2iB_7V2eAE6zCn8o3FmgYBu_xWfwfr4yw4aye2v6lJUDA243Kc_Z1K3RZefwHAhAw2MH3XYOEGZtSmqyiuwpP4NqZajjahZw1rrAaMg8-qqmwiiWf9Tjr6abyofwCiTE6N72ixwCVfY5rpXMcZXYgmqolgcDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=b1-cg9a3hwL3lZ7jCsZPzZ0R9p30o1HrHykVQ8sR0DjxJBx-dUVmIsVigdV2ivxHUzgil-HLwUMhpZiOounbJET3Stt69ICasAzMwa5dKslqZlQ2vEnzRvaxg6B3JJcIU-B0RxmbFC1akdVI_ioEa7GDHkqRmw7wp934BCGXXZvz7iGtMtmnWG-o2iB_7V2eAE6zCn8o3FmgYBu_xWfwfr4yw4aye2v6lJUDA243Kc_Z1K3RZefwHAhAw2MH3XYOEGZtSmqyiuwpP4NqZajjahZw1rrAaMg8-qqmwiiWf9Tjr6abyofwCiTE6N72ixwCVfY5rpXMcZXYgmqolgcDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0zwTuDj7GGkage492WgixiI9uhlLEGpVnQ14XYcTkJJJ5_0EsvC_D7V5-xHNttE-pBIFmD4HdKkn-T3h_c_Gv8KHpHA0I-wR3fX3u1GgZB7LcLoUGNMBNPIpZYtiTuX6wD99yrJqk5-Jy77uyWdJ1uzYcG8mVRun6-vB6rnumlliPyGwqyrHiukYpTTeXqI-ldgXvBCD4H-Uc2twkDzlptKnWYLi_apa3mPhI4X7MqgaGMzBrBoGJDiKIwMhK5vidPiPEItjWRu2RnKtO6cjIqhNDQH1DQBMU-1URs8to0BvPKQ9UVUWIdfvhD8kdyeMkSSZS5PH_2xLRpXolq9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-HHQQwKB0CM-cnRrCHQ2Vhnp0ClO_GC6LXdFK6AeumlCptnuzBF0oxDhk5tJnEbCbocAYJsZAV2a_wGtpmBQ8d-lUOEMCZSFVjkoTOj6Rfa-8pArtoE58AVtt92h4CSGElebiN1wVhd_VQir1FRU1zM2L1z94-H_zArzHzXgGnCwZw1mM9nvd3OCuaKQ6j6YyFlPj5kVc3mK-cHW0rdcnrCcy4SGwQ9H5eiCNCeab09VFK2Ozc1qkLpfiEkgnInF5_awbwoBDMrZPqxDNO0Q5YV0KZOh0BqBQAC4MwynSWPQWS7EogmBw7b3PRroIRneuHddOPwdVcEjq785FLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUF5Bhh0fd_6R98vlPUt0uA30yH-JAcknb3iFQPPpilQUZJITZtcWsry-cQf_IvMPFFKnhRPjhCt19cIFGF_X_qgyJcngurKLiJrjrk-ajmEgKMvRuJGI3xu__Cd7pC_9up0Rz8lRG1qhWOLahlzgalRk2XDR2tywxQ5cQQE6H8wMndGTXSQXJtGIPPKOIOIn_brbRXAQK6a7NK3LsVH9c5c7bEQP7wbGeDCY-Fv1ll9q65RXoJJppIi9y6EJqZNMBtMasUTz7IXaRScdxaMcbKQrbM_EFWyriQte6CzYDLc6CLfgCi0nu__e81eDv3Jl2IGrEokRDAR0tu5FS7dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOz9nCvWFU0P1xYorUciNcWzgBApLySB4e1KukXwozE02SGUMMZHvs6V2Coz48eqJQ_zbZr_nj__o5fAAW8BPo0soivYHyjfuvqpTO0IrT8QpQxgte872MTPhdQzHTRSZj2mAafkVVqABmhWqu6kMD8g8QTssjXkwHH4xFpYx50TxelaWRvyUH0v97ujqVJdYFb9He-r-Y35mm3-Y_n8nrY-LS1XDyW0E-xZHCTdHPmqUysa7PIYdKXRqhQiM7AjBtkVBbBh8LSqiZKL7yR51Dt2zj3J2DVfeAI7_w2TO7JZP8WMxFp3xg2bUUx9vKomaPBIRdSNdNdxY-GM16zrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROgR7dmoQLOwRV91PQmNCvzD2EbSuSVzYgb4cfr0zHjy-ue57R5loSyPdfBxmQlo5KwLFdl-SFti9GWZjvJrfJOMG7cUlRE9BXOqZzrZcKtsiPzT9CcEH8qm5rGIvyFTcuNBre6bVwrYqdDu8kvZXSF5bKIoSU1IpmRlQ47QxNK2rI6i49sBbJ-yxnvs1arI8NY_ifxXpm6zUn1JAvtaUTBh28cpR507hlUwfwRO-aBHqzLvK-S2jvUwzWGh7atQX8xeAW2xZL-aYkLf76aN9j-T7SLlgHmAYGUikz91dPWkjAVpVn0yQLxN-9xNaIJA_q2xMM5YkPmo0FsoAZZQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCEmB9Rmg0dV9RNGlLHSX-E8WPeTPfCXW4aw-1Ynis6D6n9jxIqtdpVgAwDhMDKWkvtnzWOWUHG0J9MDIPKB54bVWZGIOc3yCQaEfWWtOKPJpeLcSq3Q0-K1UM84QR506111LrPp3-nYeSHPbIxcbIFLNKX-uwdCQ42PZHMIbrvCnwxeyxOPbOvuYCeClY4BeuSkXaPRzPzIRyWAw6luXairkV7t4nEeLwHmVQD-YXqubQhvVPsDKUVU9O79N-uCI-zx3XAucIpNzz7i93KKQ16BbuoNj8X-SKnJSZI7WdtIrkmB_al1M3u38LnwSrVRyVGuKOfYX1YdNUQulCzUEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seXV2dOA75XoTauXvi27j0iuZi-9bZDnFjA73fYZEUJWWDmwIWrPio5RqjLQ0mHEZIhDg3hNtD56EJQFT6jtVk4h1Pe5YAZoMFdRnaY5eSVniL-S6a3z_wSODUUAVjW2tLm1lC0jRkknfMf4t_25KU_IzTAk4Xem0UTbu9yiSrudV44iAPMzs31fGQrzc4EM2KZgQHqt5CF0HwqkWivyZ1a-ZIBCv4sR6YHYxgTg_V-RKAhgfQ9q9y0nH9DsnDQ62-vhaj5Zhggb4e9d3TohMe0dqmFRSognZ7I7il5qNpxTMIF5q8T5BSTcuQW0XGZzTpKm5CVYwIn-p-31-2w0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POQtQ8cI9zVYMajpfjkc2MnFuUyXqoobVHD90Ygl8lq3Xai1vdd8_66SmXm_vQTJTWKQpGcscIJPpTaDkgNEFFsz7Z1esKoOn9vA-65LamSY4x-MszyX4W7BB6pUWYv3mWp4dylTXtpeTtIYB3vLw8S16AevPg3GipTA1pqz4swKOa0n7JjUMXmK7-6KZlEQ4JT_fBn07axWHA32NpHF7sMxS7wfK17AIM0-bZOEBmvUUgiBF7lzwm4SfjLGEjGAqX8-HybAZ6fDhbVZmTnCmeII2IssUkV0Xn0e-13MXw15tR7IdL4I7rQelDTMfhHtUPVBO-XTBQvQdjJup6EIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
