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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 316K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 00:37:27</div>
<hr>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=XuvG2XL3fZ_him_tD09rmmUr1OAKh12Zv8zhSPoupgwZDY9Brf_OccGd7J9hCM62H7eg13PMrKHIqNMOffZ2k2nNfCMf1x9EoRB1C94_GXVObHlYn4PU_1xH6SG29JkTWoG3fj7PJp84qXmuhMBJla1l9HCX36GWgr79xLYKqyVYikcb0NsjHDDIw0CZo7vQOL9BjCWsYEFiO_NsriWZYlBujBguCSEiVfr46aQB-_0XaCs27dUao852BocRM0yjnxXk4w1F_DOaHNv1CNF9Ru9Zc_zCJVUd5RJ65p2ifTRhFUNAVzMkIeyCbEpInM69hpLNbj0AZHQshd6KMl4aVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=XuvG2XL3fZ_him_tD09rmmUr1OAKh12Zv8zhSPoupgwZDY9Brf_OccGd7J9hCM62H7eg13PMrKHIqNMOffZ2k2nNfCMf1x9EoRB1C94_GXVObHlYn4PU_1xH6SG29JkTWoG3fj7PJp84qXmuhMBJla1l9HCX36GWgr79xLYKqyVYikcb0NsjHDDIw0CZo7vQOL9BjCWsYEFiO_NsriWZYlBujBguCSEiVfr46aQB-_0XaCs27dUao852BocRM0yjnxXk4w1F_DOaHNv1CNF9Ru9Zc_zCJVUd5RJ65p2ifTRhFUNAVzMkIeyCbEpInM69hpLNbj0AZHQshd6KMl4aVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0N8SYrs3Zx2uuiD3B_NKmRAP9pgAP4XoQDiXE0prUrSKKCS7tWWDXwByx0oE8IW1L2Pq7Ep4EUEmpKD1fISxI3w2nNOMjZ_OS1IgRTt77vJEis3MZDZE6bldkad4eALuH6xMe989D3CpDqtAJ8oCP7IBmAkWLQGbHS3UAKAYc0gWSOar_PRbYtdQa9QFcPB0-ieewEF3wxKSvBOI9NI9J8QUdjalGmeJK_kTceIaoqR3B0tyZtjnhOh81_zL3wWYFyZHAfkn9DiQQPCFAMBQ37dzf6s3NLN9UbQifVG389tMpmVwBnwSPzXiQ-8JNcZGhH5d8xRYkm8mTxPn4btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd0prh6vQu6XzsSfY2VgMzs1VuUxVqRsN4x37-UwKoAkZ_UdOkgMuIL4vvJDG3jz4Zj5PMWtvKuZZ2ZA6strUlGHZ1xiTxTmgC3RD1_zah_6CHBr6PF-yMCFg7oGdWdpFC2GgZRoNbp3SkM6fvBFeX5dQ6NYMp7H4X2ySaFJntMgxNcsh7ONw3oyr-q2zp-Dk_opeDxEpG8plB9E1el3rd1I7f1k7f2FBdkUWnTOz_ohHOuokJHt6dqjVlw2-DMycDbKgMXs_wSz6rnndi9kHKmEe54HD5xECcZBbLvFoxWA24Fbfkc73TDemhhvcjbMLTqdVQV0OZD0dNckqghmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8XVL2u1nYnGRmWjx71l9xFKRJ8G3jqNNsE1ZfOolhcwtORgA52-XJ2Ae4KkNrdhVcQsfV_nib8qMeCFQAWpbRHqfGa_cr2Mm8Uv0PUeT2a3rWe1S8gqLZsHRLQvEslnXy4ExW7uYc2_i1HUL6nqHbEfmEAgVD-SJ0XV5j7Xt94Ei5SRjxrIi3EFkSe--wB46c_FeXdpgLa6Jwrt-wsGj7Xn-MXC9G64GSTQMfL7Tbtp3ICSVZlnSBQ32WFnBRNBx5A7wc3gyfgUAEOlEUjr4BgblE3ZR-lkycU3h6LGr3XTJcY9DhcfZchGrimUDdQcHyCjTnLer302HfmqqdO2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzqaYIdBvR14VtCr6R1hpmTsrK80Z0s7YrIomRkXH4Y8xtWOzRRzorotLbDusgq6wVe6Do_dsd-EEo_-9Yx52HCqhmiraqo5hPKIY-ZaC-6tMRExbkywYBLPP4p8ifYv3G79UVY4Dzs15WRpMtg3OOyskg3qKDVvfLE1gB0iUbS2JKqIBR7oAXAUIhgj16ARL0yjH_3CbYlD4NVtGTY-wkVRsi2GVt4w9Z0lF3wV1FaLXsVTiEuxr1Nqio4f28IX-2bmJY8usdIeELw6YSzf5TlyUAiEvggjqMfaw9a8ytSKBfznDfaPI-0iUoqW88qr7pNpueyfMiPxlnJz25uiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4YJEOqf3qlPEN6HVoOA1QtY3sVSAVaKP2bZ0iFdI5FJGLjeJ5PCSR2iXQwrJ9q4r1LV02jh9Wd77LULdVkNacVvCnnV-uqDNJbS1jejE8L-Ba9CTzfGb6XMYQ6Uo1qtGQ3ZefTz68KltRE3XtBo772R6QkcJp2hFlvbQ5L7_Ze5fEV404__gVHPZcr9XNlfjN62TXM22gsBTN3C1utVQBvckRFBpA1ibJ14Pt8bKiEegyJ6UdWjWvROELMUkh4lCQs5hrc4gbIw10-_uYGG9RgPOjL-JWCFfNRgajpf06L2uAk0t3Kji2IxvwUbw2s5_vehaLQnCwzej6uiFaZkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiSdtn_dkT5E0ru7Sa9Gv1q_6hBxOZJIraJZnJcezMbD1VvMpIm7yFCwl2vAgZIHam5hzon2r5GvN6AwD7vWK--u4IoF3Sko4uMSaNY7EJTjF7sQCliG2CMdaEi4P-_GxF-i3q8gnF5o5F2UtTWxeFmy4hE4paSQ9S5XEk9lhMiSzyey0Ctt9OQwlWlC4oV487f_ys43X0ULIGknTW-kpNym3KWprKdZsRgVQYafPI08R86js3n-elctKTE3iH-PhR843R6gyzTvjWLhzV1nnnm9UknOeMb44CgTtDG_fQU-HntZhwwv1SDYLuiVOXfTsX2grv-38BnYeJu4ZRqvow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXPcsVlQMUqYJRBdlxDntJELEJTzPZkvF40w_HAiVft0AYN30UicK3JFODJByibLNC2WKNoCHeqNfc_50rjlDjYTLZjysENcOM0AHlu6mChvSSGJRaSXVuf8ZLBJI0xJkYcIUtcnd8mDwru5eHfNP7jlHE-KtK3kL9URxQ7QKSTHWqHvlkoMsvnZsq_AGpAM8MEwQQ1JkbDUi4-NBp1tsWosYS6-suFTtzkF7gRPbgvuLbbz6qij8fRQh1AndSbGB3RgmP5KrEluWUs2FG5DvU30vhjlE-htWCU-0IPg2kFV3OvaTAhkqXy4WH-s_N4hvqbafXaGsLNOMzAdJrDRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSQlAM9Eu17ycwtFMx0dFXWfnEOJJ79kuBzwiKmm3gzaAb8F0m9-rb35WeXZCSjJ2OE5P2quxfIUsJVRCFsLot2n5HraJ16KFizq5O9FixusfJ2GGL6NFlJDQZCBWFWVhsQ22vQZlf_fsNEDcSGsL9jVGNHC8qpIcChLTVa6HHIUSvEncWIsNP_twxQkWQUgiHj63Ge_tkmT19IisqiEbcUcMUnAjoNU0W7E9ym1fvf3mM3H2t8zZl-dQM7xXxScJFpRT7t1oKe9EcI6wkLmx-0wKu_wBHMaqasdD2X6VN9eV8Ge5M_td2mbCwzvUL0rOEwLzBif4Bs9U-jkU2deGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=rRbza2iQ5sQPIs8P-Xg87QOIFlCRkIojuJVN4GCzvZGjzBtVMTf443NwFFkaJMCZlUvmxILVnrN4AIIrzGlYOD1ITwkZ--aWiwqQFvrangygjIJRBF1Y6U96hZkWOM-UzVq08vVs-Czoxo80jHkkZqsAGwFzlgXYTxN5kH_f5Fo_n6oNVlwH6-1D-kkggAXK8cUH-LecLRZCCj7r8gGRr6KXY0JWg4es0mAb-O7sZ9KAmO4OBURMCUwKoLz8qo8IuS9QfZFxu-fhQvxMrmR4TurgnghzUMtmV8L8P4Zj-AJFtFjkAOOyHp7WTTmzBCOU-wJqPWUUGLAVLGrGaZJ7JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP8LbxfzNgwrOUSuxHgI-oj7ItIPDvuElQWdDMI7sU5YSaYTa9Wk1UbhA3kgQyVbYS9I0TlTFlFvDQNTZXrcRKNoWTZOHfG8qwpQ6ELCRSzGmhs-17Smpgp2ciykIbTF7ly6gCaj675f3Un52KwxwcgYojEPNCrpqVff2aDrCbXqKTNm_sgEP27yCv8otrwp5ICkqFjWqdvW4r7nLIDHOvT-4AtMFLY0fHeFAj8vl_dUc6vG_mNBta_mJxIRgGmmeYDHY4tCG9qycS4ynBFneFhC49WQDkKlD7wB3W45GSN82loTrJIol_yCC53sxSvtzfj7OED0uHbnOa6NSpprYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw3nROEmaPiYjvWZotSdH1pEUPy9qiBisDjVpwg4BtwMlMZfe0aNtALiOECjLJlMkc66evJ2UmC5hl1t0kPQNbX3HfF027io5VbHBPTJXxebQ3rz4Rzj80nDE7e9QVs54cndAxsJowHsi421eOZ9BD_8RzdW6p5uzesufXVzQOWiyA-EhirLPvv66asRaq-tzNFeBiNxtnGN9iVsIEOUQbn_ksNd8eCkfGhhJOH9YW7xDu0IHkONWyv_2tb9ldiMw31f35s9B7-JhdrjA8-8Zcpl9EAb29Qs-OokS8Wf0O3YyJIU18XBq1-GjTHjLgi6AaovEFq9oDW7p94EeAC5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLhKfDF-hLrpHkc0DsFPoGRmTw2-r2bt2Ku55cw3zmBqZlAdYNXuK7uuTALe8m4Zlv1kzbfRZWVn1GQxeYF57Q4YUpDkidb3ChAT1RzRkMvmHTE-_6gEytDLeYkRoXaakM-mXyTfb2R7tfIcBGXMV2da7LiZtWRqdcKSiGGT907JUxm5AyuYcjAmg7AculINwafP5QWD_Ot2EKaX9l_55Jv1J2TUr0EDljrbewQqO6ty1jfcqatEvEBGJz3vBN_7GY3bDK8Kf29d4WtkFOXIpR2GDbYzwIKfrj3u00AWTeRMdegxReTge5bwR857TyzXFDyG3nfe2tVvtVqv-euWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuEvkyq826BJjrbpUtG_FDdx6p0-mvU_3Tg_CVwGdee6bvUbJk_Gkn_Nh95k4EPSkByrq2hGON8ev2FXQA19SZwxfK8lYJY1v-o0qlRkB-qlBDSKhnTucC2ZLZ8sg3RcfoXLc0fzhPH2wFVI5-F8KrONVkjfXoMnM1uR0h0i2Yn9d1IjtZT4IxuvOQoaSd5orp4aEY8w1h-pHLxCX6QVkZyYRKTMOn9nTwa_71nY3inNU-lolJbUemTPUaH9klA_xsMywKH4KWJhglJ1S_UUX3GjDn9eGz2f4Vr50_KxTmraUfH0CNZS1Rsj4wmxE0Gzgpfe5o_nhwdegAONLHskoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roo-JRyO0F8lCahydBzk5JFeKXcOW6jex-I52oivVRZd3TtzUEJp3Tw23vRtKJYiAKRdPZ0dyiFqmANihFt3kBAWflOfVGA1d69uB_ewe_HUtu4zlfUCgg1kc9dn5V9WqTVodBBfVHiWhWVDmEFM5OP8Sqx_GVqS2YRtLqXELhfQEQmpUggQCWZWUatA8zdMhFQtRmjepYDek6IWICiQ5uWQlNpwQSPvjIbj5E0ayp1NwY1R8Mc8soJvzgvjsMCwZKjcCSvyeYHNOVyKugXK2EvwRvIyUOl8gIRnV5egYEmBN3Hg97bwiPHGNxMdUr-c7Vl_IISUrqQ5nNP_zTjweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV97mUvuBGNDuhqrHCVFx3Q9USCv78RywBJvJGTxqfEaOUaSwIQigj6euHDe_kf5h3NgnM5qXeg3MJw1QGcZjxRQGD3VTqU-cgUd5EC1CGHCl2IqKJHf56RZUa4VxylJuCV5XcVqjO9BrNTyXQ-VAQ6DntGE37Uc9l09B1VTeITsFAZHHmeU0sg_oefj70WH0rjhZU0dWV1JnC2Lb3x6prgjLj81Xb9piBNUaBZY5EzVtofgKZ8OMzuO9etof0ZVsB02MFDDZy-YGjY-muQQPXyCJc3N7OPN-lHd1BEpD-5qzILS8vtq0Snm0fqtXOoXpWfPHqFPyuSOQsi3QWMtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab_dq4oCteske_wVVqmcV64T9zMxK485luf7aptUznfunATrz8Ig92on5lkywbiZLogtgU7wuqGOgDqafNOL3ba32sE3ExT-3iIgYGiZq1mTNuAjOrFX_d_4-Elt0gM8uDLOOWTlY99bLnTg4Wfy6oJDulFdye-qr9sxxjUWMIfCpagPVwkZXfkhi1q97fbz10hvMWUTGgqU26hnrfy88tEHKZT01v-yXXNg7EnHnJPDjHvC3wpAdy5N3IIzhFWu9m2mBcnk7bnoEG84xlqq0sU2foadWVUm4pFvwEDUrA9Ol5aQ6U7756c_kV1KbQgjSGKWvC01K5Sso4mtm8CiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZW4EIAPGtMBAJdk60RAjxDsm5Knc57yhWEhh10EvH6BgVhKNpW7CZGk2KUFP4gRjafWdf3f2E0ODcKH10VM6Gk_EQ6y0hO5cdP49FCCt9ESzLOe8WW1t_opWSSRsPxIRekG-fNQjtHct84CjDsnkTWMyvtNutV9cnxXm7taLSRcpYscjzglRI026bRPdI0IhVdSJy6eTMUQ41uFmZ36bgPj9VOfnEAmcnwbxzO54QEzFdNojSNba3Pxwq_s6sOS0cqRYv8i40mgBzBLWOkXL4NQgE2wfoSh0bFmxVIZG94_6KTG7j2JNUh8XqOSu9F1LuDysURw7ilu3VEZOLdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDws9Ln96Sj8HbuXvbEQQDKx1rHLtYVcgR_DkyoajcSiqTD7ZG4TD9jQKaTCt1zvIiM9EluBYUP20PIjWtvGlVQnwV1AmQhAtrQpuYqIyjiQ8bsnxfzwIk1L7VpjnmpyjhuQebL4W_qqodsj1WcB0kJIkhJlW3YyMnnttvnwlwUDXd_KSmY5UVN5BYC5kP8uHcnCce_G4LNkCfkK2LyU42_LSfNlDlJlY97Sn7ZkL_R5N4rk1XCMLyw6rDuK4FVUWPzYUOKzVFU0kkXoCup4fQSbBOxNnHI8IVzGnkYn6t91RXjWOkr97OueI5cWy36Otk4YHa0KcsKYogphHyiCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yso_zKFB_RI_aUW2k2rtA1Z5Nd7dkQJ_bgk48DNbnW8IbvOemmiWNBSI-RGlr6AF6SfObEdUoiRCpims7BNhUUYT4j2V-S_O0mX5sWI-ejPDur-hNatUZI5K7thQuM6QRnPmN2eLfwt0oH4l3vmHAluOdA_RdDMkQMXQJOs1nHYQOhoGrjVJgEFtdM8gSOkZfZDMlROGfjpbxy1TKwmVEg3xDFA-Jq6NcDeGgONNSPKVNHUMrpDt-3uJDVHgjHcy_zWxEQJMTbao7XG4H7e4YIezZBheLVL77Foak5Dynd85_Ntj3FyZu5JBHDWgf7YcZ0ETrJvqsBzJ-toN0x-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tCVLWRMK8GStN0BGfi7hbOq7TudBOuTDxrFkxaNVVoomFkx-B3JHe1nvaCDzcT1OnSJVN1fV5jT8YPA3lKHuZFAuWReh2iyCMyz4r45pIWuRsarQ951xUCwQDdccAE_FOxz6QJUh1KIV-RKLRfr4O15nzw8hzBacNW8BAL-TCdXXXRecQcwJeswWP5t46rhZfmITRmkfkON_YbkAkDDQWOgnKSWy02kF8Fq0XEGsPyC3k2I-PKmJoK5ZSzowwDeAgWs39alpLcRB0mWIqjFQzmK4P5DkiNPeIpN9vCZfvy_5PENh-_vBXJZIXL5Ouo9ugp7rkRpkEdVyiG4iTAwdig.jpg" alt="photo" loading="lazy"/></div>
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
🎁
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز 3
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24225" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8GrtOrmmygCDvXfbFSknnmOjzHcmCo3piyQoo5D4l4gr1-ZZQ6owHGtKj5uSfywAnm18D3D_P-nF1t7rqESbOm6AToq_6tTD_vKbaZBbjEXzFD5Vmv7hpUziNJpGESI5-yykAGXtg2gGh5RTkPNNmyE3klVLiY7EL0lhAuJ0ga7Ih8zK_m6lOkJSKFvt99X7yssdtZMiYc9m48i0zi8nDM6tl8tuk68TU3TtHGW_N-llVuROJHiAM09F5L1J1s-yT1Vztw8kYi19KUgJWhk4rF20a5bCXxHsaKYr11_1cFQg-1KNhnb8D5bWaxaMeBol-wze3PjivZs1UAj9FGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpj57wUDhukG5myY9N-7mFR6CI9M7r0pqypDGFArMTQDZ_f3wNGOCNS8tfs1KYSI40WjLSsZvNk0rYRdyIqcBfBhxI8xkKgr4WNbqEE8mjIFzq3pqbfR9wuo_9mENU19oOWJTU69u86oCLZ_XxiJRGUknNMzDaM3L6p8CPGGnzRo4FX20fdMDXM06SWwCB1nquiTYNzHwckmy7eH5zSZerJCGeR9c9Hu_o0WbKOvgVKEXMYBOyL5P9-SEhXd3ORNlQYRhlUMb9ZH3i7JrdWpUc6eXLKVjxRjvZDzLMF15PeGFBaU9i4GDAtO74nst5vkmuTOCXKge_EmaOL4MFjEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9UcZYkQxCMo2QBoj3dDEbgj1K2ulXsE3_w5uD8x-iS_xNTR9KO9-pwusaUhl1MUWMxG18Cxs_KFNq5lHNNz9OJQEiQ2vuEoofsLFjLy0CowuOd9am9PQ-EZ8QEHIUn3BIF7cijDzL5Aj5mFEPYq-ab_wZfiERQezVcqEXbFzGyvNhxuoSH0hE2fZ39ojjlbFS7ynZNBzlhIBNF4RyKeVnQuP5lnbLRW9UliQs2zaQNu49e3w1BcgUFh1W_fygwrDQnavpdt0jjAFwGpx_csOnPAsdSLKdOu2rsvktBMjVRTUGa2Hl8hKx1crbGv5CDIKHKJKf24z-Em2V0KsBdNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZpHEBQ8Lj4YNuGvBLWQda8JoOwjnigYObl4VPA7vZ76G9viBF467gAwFsXKfezTDGA_lzDYPFG77dcjcFHWV7Y0mM29tMN2Nd2Y0Rx3wuArSV7eBmcWBMCnbkvw_LjL4qMPMLNljes8_2kLhxBv2lLVy4Hm_xMKg-h7Jw9Jx6kopRnePXOCkT-rcckiY9fITQWnoGS8i_MXpXBOnKy2swl2jNi1DwvguAL8a99IsMgy65wp8BY6OK3ZffUR5YNdGLxO6qi2g6h7juOKBGWTSyzdesn4ZHspwcvlPFZhhLX14PTLaQpaDiFuaOJFe56RnU63iCw8HPDEfBfK3JGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoAYBz5PuS-E27DFjhlfwXXsZwN7gyeTL2eQEbtSuIkjElaNu97kbjkV93yGNukx80vzT30pSBNRc8N183a8m3INFsKU3gHJvGB6GdO1G7VUVdUw4Ths-9ZobiFKyzcEbsAXSQ6pzuGulg6bQb5r5cvG776yXtuxqPre_Tks6MRpX48SqXQgipVaOmk_HehhCuACiIlZlYx7je9OZCzevJmRvdhZCA76xOQps1_kQt91udN40C4sCXZxSC0_DraS4cB1RU7dzGH1eid-6dW59GgM_yLJctWuQ7C1o5YwyjKZvWQmlhOI4kk1EQhc1pxhrg06dVHL4Evbk3-uKC8C1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui31TouETTXkQRCkVkM7bZA96h53Gky-jqvP87CApd2UopAZMyozefAmSiN8EbnHofIYL-regDhulgDIsFOCAB_tUdqseW7iVt7I_KOD_qNMWA6YLMqOgY4Pd3Z78_nvgsHAlBkdrbmQ3_18yy_xZc9TmmTwELGPHVQlAbEH24rtKefdw5lXP4xIdOvOzh0O-DYn20BGZ75xQcCc8uM_7Qv_ye-_YzBPgxUG705fR2lp995JTffT6Of_pBcHDCKwRb8hY1h5PgMz9toCTftGXwI51krsaJMLIoM4qlYeu9MI3-BPgEQLdVKwBfz_sq_GajtQBLVGpCxAssnipZHQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTu8xcI4sL1Wb3RjMkMg9Df9Ptr9O1BD95bktNkgKqaMdKXFfydSAveva0CiyHznpOmUQ-n3gzgsBneEl00tfw7xgi0wPE-eq5YSO3McXhJj8zvKdVKdzOSDKJQjszB0r6p8Bb4mITdTxMgoqrT3wRf6QzToaT-a5XWX3WfgsdqWT6qvo2OTxIgolrviMlbKO2cDmmWWUCBAG7wD0ipFW0xrIcqKU1juPyGE53gHf2qzKktPgowxdc7ufrxTwisSu17p99OZuC28BUG50tjl4vZQSa8pdGULpAa_pzKRqNavyjOa-osqRAz7I8aLIuHJOPpylcDj_PskmShOhxrbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5FyqXFPftIun-oiTQXR256wvOplQtRtQUMxdCXA_V3D42CZmjSWXQGsFsx3-kPQsnDRV3yDIX3bh-avDs8mdeBHoW54kiaTWfg1Ywp9Tju0jBTpolcd-WSL01uvdbxUQsdsry5XaameVsYU5wSgI89dvgGYv6dOD8yIwGF6C5LT-xX23Nd4lrw537t6pUh8XG7ATEGpOG-cUHS6-j041UFUZQoL4vHMFOVFJo5F0Q6WZnt4iN0Wimzy3gurIDAUefHGeK3ZUscy85ApU-YpZGnOkKCRt4yiB8l-R5KvlfyaDC_z12CQEpix_IZ5hmcdWN9pMcBl3YRZ7-Fa7KBHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDLN_Xdf-tZ9K5HwkUCdXJKlt7FT0mkI1nQoZn5eaMRI20E-hKE_AMR8xyFGlwQEIN8yic-8wzqbL-pjM-mJ19ckvnYDhp10kZibz9m1PLGiIC9iD1W5qZYCppwb40gtCG5b4CoDV6SYTRvo4SiKJqhSbKWsaLzm6XE4KC4sKQbB1cHLb16dERTJbfQZcEGtTXOVg4BnvVXmBQQdt37gF30X_hU4LUM1KF3UUSDAv9BjJptqGki3oRppnu17MeMe_SKnquvwLcSucW093SygLlRNkK5zfuBhlajesiKpT99EMxOf1spyk4yYB8Lpao0orZFbPzR0B69HrqbpetTVbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Len6SN4cOAF-aG6t7VspkhkHXg6hCwSZhr8wl-wGiPlCp_ftfViZbZV2cC65Df1pC2QSiymrOPwtUAWtbxuedaIpnLTBzUk1T15OEDZXtNCOomDuSTp29RnncK-H6ZYi4TMObVHcmcTyQKYWHAo8nc2eG2t3AsTsKqu4N74ehn6GK2DJxuUrv4fUoPcwp5AXtTQOGwXlUtQ8x6hjzKauQuWOT2RXSEE1QN0mUqCAcltFNIPxP5AwBhk8Ls60NVv9j24fSuKt4h4kICyKxaxmYvynzjQbrRYLcP_9o-q67RD46F-c1IBAnUjPUtPsyp54XMn7G0lbI28C1AmiNgF0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Len6SN4cOAF-aG6t7VspkhkHXg6hCwSZhr8wl-wGiPlCp_ftfViZbZV2cC65Df1pC2QSiymrOPwtUAWtbxuedaIpnLTBzUk1T15OEDZXtNCOomDuSTp29RnncK-H6ZYi4TMObVHcmcTyQKYWHAo8nc2eG2t3AsTsKqu4N74ehn6GK2DJxuUrv4fUoPcwp5AXtTQOGwXlUtQ8x6hjzKauQuWOT2RXSEE1QN0mUqCAcltFNIPxP5AwBhk8Ls60NVv9j24fSuKt4h4kICyKxaxmYvynzjQbrRYLcP_9o-q67RD46F-c1IBAnUjPUtPsyp54XMn7G0lbI28C1AmiNgF0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma59HwYhNApqJgd1k9xnD9HILpnQVZK_ENCDDnciJyT5QRfBPrlAFQ6vMaBVmM_TzZ5uNFBPYBGdQ0ByD5AxNQyHje63CVHYIENJeH089wOlfz9ex6a6WGOdus2Ymvgd37Y04J9oFz_Bwg50LDA8__9tERezPyCWLs7OHxI7D-0e74f-JRo7MfKC3uvImD55FnWW5e4nsg0llAagpfi_M0EN-4VRDrUVNpNpnRieAviZlVwqzfqkKIXPE0Koti85FuS-l6qP4UrpQx6_BTbMfBBmACAz7QCA42UiNHVaD3twpg8oiGADSQoPHYIqG-h3MBzTP2egjI1j2t4rcWJz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KccOMXVgvZqUCZvtzwKsbNQZ-txDi-WFCEpILUGydHEWSs5Ri89wLe5I9PH0a11s2onB0_MjLZap6JF2u_bkvbqpYZjTgU5nbytgeiE_K1Je3VUvGBQ2SD4sVvUVvWy8INdR3D5UIHqUyJGS-kxP7-HTVPDcmeb73sNGxc2kPxmcBL8tkonNWqz_uuvr2LQPz7cOd1zKt_6jg7B-rT4VtSsavhcktPMnIDwN--oeRui9BTJN_d1hTeM8BImQGYyjVeuyACrZS2FK1ghtvTGOskUI57gNLUhBw9mvb7e72HLxSbvON_37xzkzU1lpKtlJC3rOk08quja8siuFBl62PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIJORollKbTrcqGIpWuY6fJld-Q6xuGn8wGdV00emnJuADfFvOYRQCcOq1HvK84GYTlch9S-LHMwbhkLyKUlxV8-vmwEGIcKPnD6fSG3D8eAq6f2QP4PGz_2lIjzqjpj9ymO1bLbGKtI0pZMM0AW2JIpyurusmswmR5Qwt7QytRm0xOpcHGRaOIBRo9LmwrlyLB5Et8gtVRhdPnFG0jhGaKmLLMUwZmPpgqXKhFKa1Djnm7doeYcplKBACh3SbsAd9B2f-CVcxgYbTV6COXOjmzNzWJmjdOYSqkzwXeN8KTgz7JhSwZEQG02-7WpcXe3NTwJUjFHbam2K2SDK6JrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCnodsbmfPE4Yk9OF4bq1SYnO_pyjLiYlxbGejGYAXK2e4ByLfpig1LRXlAtz1oY5uR2gF55-z1vnpQdmua_9IVO4AnhOCJJmd4kKF6sxeZ3CIfrnUkd8aOvFlkFFzhv27L-kZLqh8w3uzFmfFxyaug7te4nnE_piJmI9HWCgGW7kuWndKjhiIF9WVzv3HdJ_JEucISZ46qjv9-KeCRywejuTYk_M_-AvMiZvM6UJYzdKzdSXSGz609d0XzYmvV7b2QiQAyc_Eb24x68irksQVeBQg00_4Ifq1GkLB72-JPkNmf_7rwBZVe3x635A_2iXvCr3lnfs28y26I_lK-ilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teUpKn6zgkzQS6EnNrhDRGhhc6bEPYNw0FeBPoJj2-IJs-q6IhPmrjLaU6S3UMVWmYvpc9O_dZv2X7QBuWghCqhaGaOXObbqzKCrUM7hzlqj1KgIpcDtSqsQBbtSeqM8r5k6nyN0B_CoDM3lugV-4z_GJ0yGP-jdkcCFPRe2muRMekPHaBUwopYmj_e57R7uScvF-neuEenpXg0h6Hqs4D0DIkVrwuGdGhxwE-tEfmuisZEZkGY_qcDsArD0zkGZwP1OjBlXC5bKkduoHuqqVzjP4W228lQuK_nO2alJgxcRz_ZZLGrEhGA0AzfitkFP9g77njuuI6258AfpiFJypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=M0JdXjqJ8qXgZR13h4xbtXsd9eq8Zcp_Q_XXc3VKAA0Mq8xydtFdrjKhmtaZRbUxMKCdxDx1LGn7jlTz5pCkKxmJCLl-eXYsqpkVl8jyK0VS43TMolcJg-PPcqrR6g_maX54zw_YEDLdKSVa_-eYb_KzcTP0bSLzJm3eknCSE2XefopYwu2G0GKCZZ8quZl2IyuuXtqnUS3MW2QP87rbJZY3eVv5cZnRO-6ZwgACv8UhB-rvg2EI97IN0yrNQf1D0aG3nxrHDQbWD8aXtp7Y_j5HTdOatBVyq7wCsb9Vj6eFV81TEj-Rba1a7xUEZFL_LgO3V-JcaIY5UVz2z_i3tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=M0JdXjqJ8qXgZR13h4xbtXsd9eq8Zcp_Q_XXc3VKAA0Mq8xydtFdrjKhmtaZRbUxMKCdxDx1LGn7jlTz5pCkKxmJCLl-eXYsqpkVl8jyK0VS43TMolcJg-PPcqrR6g_maX54zw_YEDLdKSVa_-eYb_KzcTP0bSLzJm3eknCSE2XefopYwu2G0GKCZZ8quZl2IyuuXtqnUS3MW2QP87rbJZY3eVv5cZnRO-6ZwgACv8UhB-rvg2EI97IN0yrNQf1D0aG3nxrHDQbWD8aXtp7Y_j5HTdOatBVyq7wCsb9Vj6eFV81TEj-Rba1a7xUEZFL_LgO3V-JcaIY5UVz2z_i3tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0r3XNMWjL0YB4mIPuzfkSiM82uNb1O8fIvzfT2s6HdvhzAgrR6ES-B-ADhnlcJ0lLrw8T5GHh_uF14J-9XV-oxCBKGx3YnGsISiyHlt27xC5Jhi0yLVMAvfXfndBO6JBUSrzhVk27gc01Ro2XVFuV4ynOA_pa6Ph2nHoEwtRJPv77-y4Ys-rHM9dAjpie4aeCfnxraRTyJF-wNScP__CkjlPBUwTVRC_eS_4lseWeWySmaI78Ssughaia01u3saKsL2n7lz7Fuupb0FNXK-uMhu1DV_umUwGkKEa6UlG2-5uImcEpjMJ8TC6jG6r9olfwFDrI37vjTLX0wSbnkHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh16nR51Z5RtgBS2Xm5noZORI1dHK3djEXyPHwaUkefD-suH_ZQx8LkifCrK2WuHGnr3ylF7fxXOXpsQWaawxTPs9kfBQjFG4FEQYvxiN7ti0zDax4WGYgPNPDnNgkw2c0Zh-DjU3Zqu6BrEgyvDMnUtmVqgU91jdz0OJwAa4QL1DJDd8MVY5H9pbGgjFnSLrO5atiUSCSpYHFq09wGsXol8sOw4tK0awPjJWc5vMyO-xKQCy0zZtg3Z0ugWVVE1_L_z9J_jbc6drL2sjFGvmQsP3fVo1csYe1FTW5R-9_fxvpycRAQIgfUMIJBdvOMB11fg3eUfH4lUJdX-TR7yIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z113hzlA0zSCAbw9D0RPwBQfZl0gqx_vJfG-b7xu4osZLV-ZSA4MMPCKzanaDK5ScOJlu4sr3GozcO8JMOHpvX4ER2ZQNmbqkmSrlvRn7koPbgLXA_qy5d5RfA79GdsV2thMyB8KVs1fVusnF1KbwkjcNFTzXEovAv0LWE6xdtyJx-WAjxwKKTBuH0pcAAjbrMcOoqz9pvbGnGlbTCCqbmD4TRpKOJNg3-ZMvKV4S7SIVMVpwt0I7gb9_yc_aNLeNxaPI_CG4KIXKvsKZKCWwwUWf6ztnd3WeCApa3cL7p-CAZ1ptm9uYX6s8o2gsmfFDgW3cPRTe0yBFlx5ZvLk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJFszHaHotwZ155m9VvzIuAf46boz-S1Xl-_clpctIZZ6DN8v1L7SM_JOSfE3QmJmlFFvvk-7wS0ObVuziiGu5QnYy_ktmsX4svSXC468xnbrbMHNOk_pepmDMzz0wIpsYSSWOL24SnaA1j5YpMJhWlKGjWIAorXpmPmd3s3c3t03atKFvI9KJ1Y92Qdeae2nT9YRgAB_jJpChl6OzF7eijhTLFo7SDihLv9wtcyQqt0f7rwy2fApzS2vTr-RVtU-VLa8Jlv8-Hx7lrTF3hg7YtEPpDr1jFzxRql9YGduRMuykCADosInO15WSmgulBT_Gbjq_imnpkhXZdRoF7Txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=C3TOSOaWYbXnWioywYuVUQJNHa6VCbUJ8R6Mree8nbxjmRCC8XS3rW3WZ_CnoJMd96gKPMrgR3NKZovGcyXCFC-DNp1p6MkJLzuAz5wdT0iwdj2wqEcRLQWUuVg_TjqKriIiqaD5urb-oC9DmFxj7mNA-V2cIObvvhNkQ6UB4USx7FsRGoYzKvCrgJybPotvuSPIlRHH6H5_H5w1Y3sRdIomJdJ4Vcu4-Ul1pLc90K5RLLv7nf1QpJG-BEhWM8E5RLTJBkphAxFZw7X3sNQo1A6aeiqJfVbdOhiB17r_G-KummmoQG0jXLbYgv9O2rIBca9xjY13JdXOkEo6Zlg1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=C3TOSOaWYbXnWioywYuVUQJNHa6VCbUJ8R6Mree8nbxjmRCC8XS3rW3WZ_CnoJMd96gKPMrgR3NKZovGcyXCFC-DNp1p6MkJLzuAz5wdT0iwdj2wqEcRLQWUuVg_TjqKriIiqaD5urb-oC9DmFxj7mNA-V2cIObvvhNkQ6UB4USx7FsRGoYzKvCrgJybPotvuSPIlRHH6H5_H5w1Y3sRdIomJdJ4Vcu4-Ul1pLc90K5RLLv7nf1QpJG-BEhWM8E5RLTJBkphAxFZw7X3sNQo1A6aeiqJfVbdOhiB17r_G-KummmoQG0jXLbYgv9O2rIBca9xjY13JdXOkEo6Zlg1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8c0Q4SIuM3Fqp1s0D3tBNs8pvd4tlDCYT5aX3rE-_dLF0PnuHq8swrzyeRrp1ynZkPrk1HtXxmT583JuLdkW62u0evmdNUovb2Z3MnNBrkvsCvt5Ir94JN0jg9c_npCaQxdC5AQX4B4MyZqVyhR1vXzXQRZGBO2OMjAtAU69-rnsRWw71F-Xj5P9-2O4xB3yFbN8-OrjTp0KB0U2-MLIuDMSmB4kfZXiWfRnI0rrukAhM__Hh06hHIwbUmAf38zYySfUYzMvWf5BrU1X1JENAK9w8Ew4iYFnj2Ytt-Xgr_5ADeXyz1tTOEsc7SP-WJncFNLpw8jFO5uySJa5PhA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=ihLhuQo7dqadBp6m8VCR9YDcGbsheK3QIlBsmgkdEWBugc9Xywu1M6LPrAB1Yx6QKNdAHCLWYPQkn_kVlBl6Zl3d6rcxaDDDNnb0d0ttFHNUoeaR0xicXoRfoj3Jysy-j6XtkoFNNHiqqpAkoby_Bi0dIHPWK7dK4IzFP5reqPNNhAvWg67rHtXkrJaJ-6MfvhLRTTDo6ULo16KxftHPy3UhW_nQI8WGRg8cRL9bJ8QjFK2U8kroTbZTrx2nmR2ab3irikgaZy7x2PJ5W-OsBAOxpVWGhCP1D5SFKJRc9xR2mvkVHEjMnmIEXmxbA0xwfs6uKa5d6kS98qbq55Urpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=ihLhuQo7dqadBp6m8VCR9YDcGbsheK3QIlBsmgkdEWBugc9Xywu1M6LPrAB1Yx6QKNdAHCLWYPQkn_kVlBl6Zl3d6rcxaDDDNnb0d0ttFHNUoeaR0xicXoRfoj3Jysy-j6XtkoFNNHiqqpAkoby_Bi0dIHPWK7dK4IzFP5reqPNNhAvWg67rHtXkrJaJ-6MfvhLRTTDo6ULo16KxftHPy3UhW_nQI8WGRg8cRL9bJ8QjFK2U8kroTbZTrx2nmR2ab3irikgaZy7x2PJ5W-OsBAOxpVWGhCP1D5SFKJRc9xR2mvkVHEjMnmIEXmxbA0xwfs6uKa5d6kS98qbq55Urpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzRA4ekamkrjOtDLKQ9Fb6iZNiIR6b5pJVfF7xcGQhtdsbjVdRhQIsFg-h2Ddsdx2a5A0JuKOeZrfCOZ_x6ZJ4F7geVJ5kvw7SJaoa9Rs2MpEmu21K3G_IK-gTipxCs3FFIlcYibAMyiKGxi0sbLk-patzQL6z-UgUTbHZWwOS8v1wTYWjDT9tVXG-1zhz50wOSjDjG0IW8LRwxd19zi20Hb28qX6Oo5xvy0HRPFzgfQKKxaKYA23z0MyfrcfzNbOJEXVutq9WN96UKSNmnJBZv-qyqz1YQKcZIY5Zk1HpjSf5feqLnhBLalY9I9pFtGJnCt87sXrtLHsCzwx9WvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=UWLqZzOEUc6IzneGYS4tUsBc_qckdTXoVa6dqtnGuxVdTVcMa2PR634rsWq3UhYaTnlF_3Pcv1L9HuqmPpCfUgU5pI5-aZa_ENndQX1x6GFaPoMsrs1-gwz4Eqi-VVBorjkqERpPZRFJaI5SB928GYZwLharjXBtsEAkcrIiF_KJDVd8RA83J9YqyrH-JttqJUoW2BnbWC8IFonrMuMMslc0wbqFuaSKk8z6OqUIT3KGWETkL3uxDoKX-WD3ndEx80KiBBV0ee0vsew6y-bS2tjHRPG4585f9E41fnop2tq7o31OYEHPpLAqosMU5tEZri5ZGQdE3Vqt_GS5Coqgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=UWLqZzOEUc6IzneGYS4tUsBc_qckdTXoVa6dqtnGuxVdTVcMa2PR634rsWq3UhYaTnlF_3Pcv1L9HuqmPpCfUgU5pI5-aZa_ENndQX1x6GFaPoMsrs1-gwz4Eqi-VVBorjkqERpPZRFJaI5SB928GYZwLharjXBtsEAkcrIiF_KJDVd8RA83J9YqyrH-JttqJUoW2BnbWC8IFonrMuMMslc0wbqFuaSKk8z6OqUIT3KGWETkL3uxDoKX-WD3ndEx80KiBBV0ee0vsew6y-bS2tjHRPG4585f9E41fnop2tq7o31OYEHPpLAqosMU5tEZri5ZGQdE3Vqt_GS5Coqgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYeKaGV_xgsGKyDSIe2l_JceflSVbgXESbOFxiqhxmC-8axDhK4PKTgYvf4Ddu-EFsxvVUydtZIwdC2FgOcSHvpivG4-toR7asTBP8R6O4woO4yzVhJ4GtBJUnyAQMGYkEJeCgdgse6T1nzF0SzfDncY9W_JGmJh3r54xzMIR-GkJVEccVi86yLWpkyBib6SXbYPZ7PjeBHAvLMLYjm6AsC05_9UwROn7Ug0HB1GH2x_L7BrxzFAtMVSwyf6mPThIKqbshI99JIcqY-lUNjOb2S58478VqYX4IXlvMnQRw2M-icqPNkx6c4cQsgZg0z2KgYLAp-t2NBIkeUpUBHNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=pdllJhyicMXtglcVRsVXsrMozsyNgal0yKq6QWCniSsIGNzjFbCaShuxEnQaE3WGzQ7FjFfTn7TPJQFfct4we945WyKtd3OBrkPKwO2L0fphLZbvosccwVHcHCy6T4iFgHwFWGUiKFWSbmm06TyZ0e9GfS6BC-ZZ1S08c_Q6YYzNYCvYrzYdbp1YOCse1B8EOBbFI4rCjT1b_FHSd3DgTAoNeLa7ZyD0uicObJS1HKM8AziYCnnvmPxOK6Hmpsn4XMr4d_OLbEIGoKnE7YR_11VkKuj6eZhnFkiDTYNzwqelrLl5YDKjaG5DlL6updWtRqhuw17lVEbHqo07nfSp6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=pdllJhyicMXtglcVRsVXsrMozsyNgal0yKq6QWCniSsIGNzjFbCaShuxEnQaE3WGzQ7FjFfTn7TPJQFfct4we945WyKtd3OBrkPKwO2L0fphLZbvosccwVHcHCy6T4iFgHwFWGUiKFWSbmm06TyZ0e9GfS6BC-ZZ1S08c_Q6YYzNYCvYrzYdbp1YOCse1B8EOBbFI4rCjT1b_FHSd3DgTAoNeLa7ZyD0uicObJS1HKM8AziYCnnvmPxOK6Hmpsn4XMr4d_OLbEIGoKnE7YR_11VkKuj6eZhnFkiDTYNzwqelrLl5YDKjaG5DlL6updWtRqhuw17lVEbHqo07nfSp6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=YO1MCto2DYv0_zw9OeF0mtqFYcrWQRpN7i4buy5-fw6IeTEvqBYRdqLsmKcqhKrGNdJqAAVa_VhGaVwBamNP1Zz8SKbY_WEdaZP6q-kgD1VsG4vQ-H9ZKGq2rTIZCz0u_gJnuvXAY7VeFcj4CDLOKm931fv4zgx5Em0HgePxaZsBqE51oAbG5JR3v1QFT8iXZtyOZUB-bauh-dJAoLqiqMBJSL8WbkEy84o-pP8vbHzrtHRtrP_F6aRFlBKVo_LkdosoZJRHlK5b2O2A7N6sEmb8ymawcINmrB0J_akfcw6RYPIiIRablXGIHndbV0AWsiNx7N4YUg_H-3H84hpbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=YO1MCto2DYv0_zw9OeF0mtqFYcrWQRpN7i4buy5-fw6IeTEvqBYRdqLsmKcqhKrGNdJqAAVa_VhGaVwBamNP1Zz8SKbY_WEdaZP6q-kgD1VsG4vQ-H9ZKGq2rTIZCz0u_gJnuvXAY7VeFcj4CDLOKm931fv4zgx5Em0HgePxaZsBqE51oAbG5JR3v1QFT8iXZtyOZUB-bauh-dJAoLqiqMBJSL8WbkEy84o-pP8vbHzrtHRtrP_F6aRFlBKVo_LkdosoZJRHlK5b2O2A7N6sEmb8ymawcINmrB0J_akfcw6RYPIiIRablXGIHndbV0AWsiNx7N4YUg_H-3H84hpbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwUdNlD-_Y62R_pO94AlqQuaOP8S-lX4Z1-H8Gheq1IHY8d7aJBHJa9W-JeV0rpUiFZ2etludJ-dHd2E9yLV6FtN1WwLvwFhnQVUDVz18yEUXZ3aHB-grRdXPUNB1uf3h7gG_j-jeHll3NUBDM_8aPI77J8K4ILB6ARtq8w8iOSi3vUNjQMHEIt3wz1ex5w0xacsSFP_ypVwyFmgjIZDCh6_iyAAjdkx16BElns5WB1bCRHTyT6SUi6r3Qwfs2-Do_-ZHjYNOO_oZICB6JgBfuKfqpKAzQscpLs92izVTkXq23-ravfd9mAlJcJUrqfVZIubDFEljIYHnTQWX5XW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpuWXrcCe9_aTW_AvWKnGCBfTSNKUsTKKwR_sxg9QhbxeRwDwyIzFEBPZyqMltl5z7eTRg3wwxKjdjYBWS6iw0mO6iLdCI6QTGKUxhnJQ9fmfC3H3e0GMA4ANaMcK7aJnN264Kq6NM8D15TDJ_5n7Puezi8t_ASPKjt04sWt3ktBfC46l2kHwpEB_kvI6FFxrj8URMsrGcq-BVT7TVdCBZCOcAXJmL5TfXRR6rPnbu5jnEljV0kGl-h2CBZmo0MtTRS2TJA68uoNiqljxoFDCvvPrKJyxHH28uB92CcD82cXeFcZihNIBefDrdnD6EpIqIGy1x4n1s_tndL9JSPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2vWVMONF69lfxL0cgKZncyitd5mzI9y1u2rhZFlYeg8jnv3vOvjxEwQe6mm82Zjtd1B7IiSMdwRsIQAdeThFV2sgkd08tlCZqvlwNrvb8XMAJ-rX6yk4n2L-QGq4OT8jS-8RdjeUQpL0XcvQF1nx8f4pzTNUPzXHTQfeziFvzaNqjL8FqFoKQpyoQQtaDAWu5RZGaJNyy4kiMOq3_wDpzbWLeaCLbB7MrchzLbm64WOHLbpFqRL2vpSrlNBP93gg4lIJBOYmadKTz_HWZmxt0s9SKNat-Dv_L-vL_jtxartS0Ou-2hC1cMTgXSU62_8SBSTCWFvwkXgC_1cYfpxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggaNW5xjgb_GlzFsHl8PXCeV9vOWKs0jBKdHkYEnCwqaLFDyd_LtPcuWJGR6PbGF5YTxojjx3z_4dAk5WG_BisaUpGpDPEPafPcDQ1bE7UK6JKyCq91CVeEwWXIa6_uxha8CYIg5OOaPIclitH3Pv4TfpeFafehthB4Kg6OBS4GJcEG-_lYZOJV93FBTk1a0mEfp3WvDlRsUyCbFczbTkUzo4ME2cauBRI8jrycizIYPAFbduvufYa78KVC9RJVaqTJ_PHYuC_blr4tGMUTzGAogB_Za9dytBPHC-H48lPG86FgtTZgU__gkWiAcD14GUUNjXyFV7KA6siq3mRHtqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=PteCXK50uDk5ctv-AGL2baVgl3oyloLlib4CKuwwlcwJu87cZzQotj05wjDx9sNXGuIPBvmsmqRBmAnpDyUUOy1TmeLCZRwYkzAmZmWdPY_y_eJqoBgvU-6MQBqaOGr64RzRryookxJ7t5v-ozRVC0vYt4rWUCUoR_cAI8qW1EiwjuOeIeIr4D_jLSS1TYhNOuJS7SP26jJarBFhxQ30ZIIIe8uU9nTse2Z19O40cTWO6_plhCoB8SoolJV_3wBwbO6pKxuNY-_Ec5t4kLokfclZQCwyS61ENG0gRwpiX8iG8NM_TJ4yObgAhEUOgGmK4NzDusAWgHOiOQmD6rIn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=PteCXK50uDk5ctv-AGL2baVgl3oyloLlib4CKuwwlcwJu87cZzQotj05wjDx9sNXGuIPBvmsmqRBmAnpDyUUOy1TmeLCZRwYkzAmZmWdPY_y_eJqoBgvU-6MQBqaOGr64RzRryookxJ7t5v-ozRVC0vYt4rWUCUoR_cAI8qW1EiwjuOeIeIr4D_jLSS1TYhNOuJS7SP26jJarBFhxQ30ZIIIe8uU9nTse2Z19O40cTWO6_plhCoB8SoolJV_3wBwbO6pKxuNY-_Ec5t4kLokfclZQCwyS61ENG0gRwpiX8iG8NM_TJ4yObgAhEUOgGmK4NzDusAWgHOiOQmD6rIn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNAVSn5GDoTa90qAhwPyrACJ2EILD3YihT3hwIp3y3pDSXG_shkZUzbhe5ZXtXPipiF4zNuFvTwP-3EckuSWpM13P3mJa7iYYI_xVjH0BDwHUlYAl05iQtCm6VQQwEScixwj-oFOqvsbp0aW28aBRGCHJhaRm-D6V9DZy-pX9IJuH4LAg8Pckv8SWEhVlAz5Hx3hpQQ37lxC4VkDURbw4N1PTPVkGC0BnD9VNpNupAFxJXzwp37AnaW3bbheTVu5DJznDG9iK_kYVleyWLKAdxOueslGJyeyKhzzxbHrTlu5_0cHMFTt3qfgFW17D1KFX4AVGXYXImr8Uv6wWPXUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQstpsUoXa1z7mWHcqfrza5z-NeNv1-WDwCJmUiA0smPNAmFoGpSMmlFX-djtxIKsVwaOMYFWOa6fSPhISaFHMYAaDRDVS0TvtZhAh_6Nzy4h193sITVJQD-ZFnfq6Ts3Lsd7WlDenBtzQE_ePnDnw9dVJCMdH09cF9yt9Vht_vkGYE-6AerEDDGc9XM8ekLhT6083iYt7lnl1EXKqQbgnaC9RE4B9aigwOr1UoRfbBSGys8aiRCtqkUzgPin7Am0SUKaD2AB5O7S-a5ARvAVh8N8BQ7SfPt5dLBQbtVFWEGk3COnoEgmOueNcedVYmH2H7LnT_tTPLDtFDHen_i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbe8bAkqmQdtTIcCFudDhuClIBZaU3GXsGreT7mCYHRR9X0lf3WX_gSyml5GfdSoGducZP-2AzazcwFSkm9hwDNEql8IllOA8IZ9AbNwFCf0KvYqfTqRuDHneE-U1EE8kXh4YN1lXXtvo-uq2CZWmU45Y9LzwDwHxDimmVmG6zQ4SqHbPxpWMDAQVtOSQNfR4KZ6nszwrAqdKe25Yj79DGFSTN3_Ci6_5Fo9gds_FFqEcV_3vOB1r05x7QM-rT9d820a8NajG4yRo6XCVrxtIInnbKoaWLUNNXVbXE1pR-tbwqcm9_-_VsdhHfSr5VptNXjt-yHkIn5J4Jxxp0-Qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHz_X3innwTJgmLWrAOMHxtBBUR7RU1KeoxdLMXW5X5jSLoyszwcIo1qBnssTkG6SZHMvY5_Bp-s70iE8xEze0RxT6Fj0DvfAjHdUyvNJBAp7116HDdZK66upcM93fSDUVSuMz-X0fd0HSU4XKlHgTqvSk7G2Qv83-KHDaxsbpx8N383pLOjaN9RKgCbDb7MMh11VGfiRZ4AkvgUMxGkytBgFlrKLEet_Pj6xyM0oXiRmR41OUheeySZk-pmZo6_oXug7DZGRqLzEDLN1-mHiIbZQcIkh5PR_Pid3vXHpEBr1Xvzs-rL9oWFrPNzd6q1q4RSwZ02axh_LVS_8dxkCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbj-RLFde5Nm71J7mPbvuL850KPV2yVqfVbFxvOsCEuRayTQxdriGvvuuxZY0EnarnQfGjTKjP-w1ftZQIDXxnBtaN62kZKGGdlFdUp1bkuF7h_eJhGiK4DXkFiZ_GI-IA1js6VAOPyxjPMY7Q0pYFxVjpqjQfIZhVjtv-En-t4GpQPoFEqIs7BlGEVu1nAcUQ1XN9sXZRDtEabThVfxBWZ46o_fWJ6FISgVzcILWxdqLGmtXjEaYF_IaGCKp15cjfZ3nbJ4OPNt7jBGbTteqe_2tGMW9aUISJvDZmJF9vIoAe3EEwR-2SD4hA0tg21PvqReRZLEPFmhcIAjdaHg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9d3Tl515pPIQ0HymTJdYjs1YwEajF5KVlgjbC4EaTSAbOXWv9gVIjCx_dNomy7GsGYDzfafiEGSkwxFT8lMO9fUwKVICPUoidP9IZHWYESnfajkmLOPzDrU1KSr2IXIfYJdWEOjOhIxuGYvsb3bgm6uCEr3ZS5E6r0cftsN7wz4w_TYI9jP56yPpp5qXE_tSWunXBKtOA8eGesg7QsNbq8veE8PcYuOLxku_APiPwvZ0qj2O-9eSXMfFhv7gK9dIY_6_WCEA54r01ZgRvSjB6hUUezNZRhgt42reQsSHI3BXD6U1QCJImFyWI7DLAVWBHF6LxHHhKZ4TO3c1k9Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrE_uD83Rgue_wnSMBpTkTCBSD3wLan8D9NF7h9vvD6w4cQS-vbH41oSleD20E4_q67GhZGdfW0Rv_OxrEmr_GXWM6Q_NrR6n9deLbNrb0W9e4wdOrcjhoBYpvrY4_yOx2AZbbKXWUcixvgVCpunq-Sl_CyltpTqif6Dazl9b8hZdlj1Nrkj-tz0pYnnOuiGd24GvqKSG_RsJ5ofazBMO_6Fg1-b1fYJurJxaOdotC3D_5q6ZG2ECAuiXu-w35YjkZqJMBXJPtJFyqS9fusBQZrcVgBNYY71u_mq8vzrs3PfiTV2BU5wls_UbvtcpzTiynliFlWwPXlqQtcoVoB0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Z6jpw58rxmMna7GVYlEvd5WRKphrUDCZ1nw35B4FJ0bEbNAthbBQ8mZ1biRAS4bF_MCDl9vhBb1Okx8R2ESJIcNo4YqzNccmp5daUSvd0rpOM6Ok4uvw0_A_VMHgaKnz2OXOY38ehnHcBh5Fpy4lm5CGH1OxYq3errpduABRGXzVwGE1BOVMhrj8K0p88IusXbpZso2wTPE-Rerp0v6_svlmy-4_4nNiomcnCjQ8gNGfhriD9QO4vMmZEQfP77p6pa5dLYVTjB-TOcLccxqk0r2Mv6ZRqpKedwQltx2z5DaAx6YBQJdo-mCW7R9gCJZeE1tH2-qxkzm1BkSM-V_11w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Z6jpw58rxmMna7GVYlEvd5WRKphrUDCZ1nw35B4FJ0bEbNAthbBQ8mZ1biRAS4bF_MCDl9vhBb1Okx8R2ESJIcNo4YqzNccmp5daUSvd0rpOM6Ok4uvw0_A_VMHgaKnz2OXOY38ehnHcBh5Fpy4lm5CGH1OxYq3errpduABRGXzVwGE1BOVMhrj8K0p88IusXbpZso2wTPE-Rerp0v6_svlmy-4_4nNiomcnCjQ8gNGfhriD9QO4vMmZEQfP77p6pa5dLYVTjB-TOcLccxqk0r2Mv6ZRqpKedwQltx2z5DaAx6YBQJdo-mCW7R9gCJZeE1tH2-qxkzm1BkSM-V_11w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfk4mMt_yHN1aJlMQuCVuxkT0sLqSGGmTWZsq-vr8WezyfopwIlICL7Fi9KiDB0jniFd5PZPD5RwErPn33irqpZz3G1GUFT42j8bBENa-2scjrNfUWsK2wKG3eoxID8L5ysnsA7IQwEOoJfMbfGV9J1VFj_c0-U1JqRJ3CIIWKMIGiG1q1X6uIY-opKPeKoe1gP77l4x0TJLTR3fcnezpuOfyHGMWaNAooieMYRCi7CUDud7lhITlvd1hq0-cAKYjuqS_ysRXZDgTiz2JPIwOD_y0RfHf8XurOvjA989uuNDS2-1Mb3AmM9KlCbitLie42E5lXKN3dIzNX7u5u6D9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKz0coilhDt9B-1u0gJAhgYmKuQq0axddJHh_iLI9Irw1bJZm5iBikVMPNxCOMfp4SzrmkIF3t7HFcOu9bGXNSgV-ys33pvDeW2M1p1tsWMseEzaNzW2Ws5XFwHBjYLXmE9vRZ2TCqICSHkxqViqFY72kPlosEGKBZw4VkjzHyYxs0hxLY-hRdIYWRrlzxpZaCNuTcLjJFw5rOS5rcengkPAHhnCZGLr_I4RXo0cOE2WkL0kk-FMVN9B1kwVbZ0wfiWUwTR-0UwHejk3vG6ZOXAB6NShNg6nzW3pGdXThwO-mqXSVXS7LzGu28Rk6j7R27cyWB2RqCzXOw2Eh98LqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=dqQJuXoODEMDKkL6E7IJ5cxCoonaW2guey3wVdoFiBQmiY5pcQv3fy7NkK9pOSMQnekkg8AkZOui3hlG-JBinE7bMYijQ4jGksx6aj-1Dj8DFBj8h76OznAm-OL4MQQaVAJV1OcbfNCQUnmAv5qtgJs5XHTIdM5PzmF8IRU40xKPRRkjCj0AvzOqowRCXsmFqex2PkEhn8IWH_t4NBvepHpX6FndB39FNustfza8PiZ8K_x5vxXmKUsdgp2E-LxXH_RXLiCowAGXeHPvEXVXOEHxOi_PRElVVWayNf_8DVXRBvbWEgkmDCFVOaVs1hOEe71uFstyKdX98jP5-BVTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=dqQJuXoODEMDKkL6E7IJ5cxCoonaW2guey3wVdoFiBQmiY5pcQv3fy7NkK9pOSMQnekkg8AkZOui3hlG-JBinE7bMYijQ4jGksx6aj-1Dj8DFBj8h76OznAm-OL4MQQaVAJV1OcbfNCQUnmAv5qtgJs5XHTIdM5PzmF8IRU40xKPRRkjCj0AvzOqowRCXsmFqex2PkEhn8IWH_t4NBvepHpX6FndB39FNustfza8PiZ8K_x5vxXmKUsdgp2E-LxXH_RXLiCowAGXeHPvEXVXOEHxOi_PRElVVWayNf_8DVXRBvbWEgkmDCFVOaVs1hOEe71uFstyKdX98jP5-BVTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNuoCql1MBrI8rmx3V9bILGKbKOT_QxIwu63iD8z7OI0c5sy2dGm9tHMx5YkDNso6ohrJzYOnvpUv6rHT11x-9vAXQv3ryIHOvOicyX-bJq0gA4NFP5MAsqBh-gMJsaVWaUWPydVd3-pGAMBtZJyF0byW7n2FC92o7Dx8w6eKYiiubLJTzhm5IBAsz2lzB1L_khKwaBCPcWzV2S1QjJxg6ohFaATDWhpRTq-NObW8d38ZVQAYQBUGd09Dch-acGeru4pSOCCcvVIsRQBxj4UlsK9UNa8LFujzLPtLGrZ3KEj5xjMJGjA2utKzvH89CBFBb_AWi85PiwnpM-GQgnFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=uZfO0UafJdI7u9rt5gFEGuB2ABZSwLIsmXnibp7Kkorp4CvzX7iB5HiqeN5jRM-RtH75qMPUqY1C5OLB9vi9dnPCdD06shw62mf9Fy9foVKQFwddwQowvNh3J0KVQVLizAkDkoDQZ3jgKN12LZmn-NLJIq79aVb051Zb4YJvmKR98mAy_osO0MquNIC5gWG8-TfcGk1w22E-Og34fMl2JvK44u-a5lk4ztUz8ZYHx9vbtBbhvVxHa1eCpZ7Vs9U3Uuz4UGLzLISIf5zViLXoPKUlaRP3Yvuk6jxttaC8nPY__F5Rn4Hdrs3rMbvucuoIEeTDX5LbeHCK6ITegP8_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=uZfO0UafJdI7u9rt5gFEGuB2ABZSwLIsmXnibp7Kkorp4CvzX7iB5HiqeN5jRM-RtH75qMPUqY1C5OLB9vi9dnPCdD06shw62mf9Fy9foVKQFwddwQowvNh3J0KVQVLizAkDkoDQZ3jgKN12LZmn-NLJIq79aVb051Zb4YJvmKR98mAy_osO0MquNIC5gWG8-TfcGk1w22E-Og34fMl2JvK44u-a5lk4ztUz8ZYHx9vbtBbhvVxHa1eCpZ7Vs9U3Uuz4UGLzLISIf5zViLXoPKUlaRP3Yvuk6jxttaC8nPY__F5Rn4Hdrs3rMbvucuoIEeTDX5LbeHCK6ITegP8_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyHcsiTJLlA4iZ3bh9ZLr3RfQSE2876YjKeSRytDZPqR7ZxCfzmqcgPaGQSiibPAF_sWFnI3U-ZAvhJEcPhmf6xOJsOfjacJZOkUAANFt0z1_1PGGNBqRWSg7Gp9ukEa1GOAfDMAIHl0DgcF1lRti_BqcKCq0ukwZeb9_4-Ii89nrSQweh03VBI28lth2MfVZfrgR7FfPBFdQRWnv2b2cT-NxH2_nmuvU_3UB5ykMKbA0zYq_tC-YUv9FXx89G8oa1eXc2AtRlx4B-OXlardpfoS9xBc-LcsNlULoYMZPisuBf70Bmz-rxtRkIFRWXB04h3tS0HkL9cP1TKPmFjaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=tkJi8IKxjSXTuV3aGSwPSTi6wHFswuODUHIS35OzkKsgpSD4DnInaBNlt8DbAVYoCQIM4zX_EocbznOfZIk1qGhIUxV6S3DbSZxQbObD477UkBKPyUwT2xLXIF9PFPcXQ-18EUS5L2hHFK5mhL7I4YmfA7cOXmhPht5yMJOFBGXw65BROD2VliMK8ZuJjhIFE9tsX-nPl5rBzbIVvCTzyj3UK2akavSOQ9Ibat_C8IM_qwH5nur6gsdcY83IIV0vsLL7HY4wZnd0u_Z7Q0N7NBnLtSQuXD_ydN0cQENyUj5PxycL0xG4B5B0u859F2FauX0ZS8vSe0oBGIZWN_QBroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=tkJi8IKxjSXTuV3aGSwPSTi6wHFswuODUHIS35OzkKsgpSD4DnInaBNlt8DbAVYoCQIM4zX_EocbznOfZIk1qGhIUxV6S3DbSZxQbObD477UkBKPyUwT2xLXIF9PFPcXQ-18EUS5L2hHFK5mhL7I4YmfA7cOXmhPht5yMJOFBGXw65BROD2VliMK8ZuJjhIFE9tsX-nPl5rBzbIVvCTzyj3UK2akavSOQ9Ibat_C8IM_qwH5nur6gsdcY83IIV0vsLL7HY4wZnd0u_Z7Q0N7NBnLtSQuXD_ydN0cQENyUj5PxycL0xG4B5B0u859F2FauX0ZS8vSe0oBGIZWN_QBroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZID5cBRG869rg_SZu86e5bgqwO1_ukG9ALQyENeCYYh49O-GPF3lhHaHutVb3OACFSH9DMfYp0PxsHVOmT6ht8V3mAfSLRTH-JZV36E8ShuD3rVVKMoWqzrF9_k7FDrpxyHpE0xCpuuhWwD6xF_Lc9-tFnYJi-L6PqbbTtOEC1j1MhvUTnB6gM_6pWeQNWa5n56gESz7jfOacD0iNGKvv7SDUb1ratiRDawUB-cWSKlrZYCkiPW9H6ISYOZK2u-OOEVdOqXui_x5_XN3lMPP2hupc-ch9eUC_CHCWMiPmYmX4X-xi8s3-2A4gNX9_F1BNdIA0wtNp8MPun2PsDZBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8brkFNkwONJADl2dWnwX0tfuRpmh5iaaQGA6qAJP7WjcRq4olVeRMie3G9wMdiJMXWnUiuYsdgvTu5EuPvoknxSnlptY5EaxP4AXJgGzcw13PYOovgBiNeXEMogtJKsw5jIgQxYVzWs8Kw2WBQa6k9cEXVjO1M1fr0qa7uB5rXnDPT900XB1dvoU--jb843v5pYACe0g6WYpwUQbflpvWZQ1NqtL7MWjtjgpnDHkTShl4V-DD1eXNPGGOq3N5VwxF0npRmnMHwAnBTP6i9OWbciZKMjT_cg5kYa5z9WhJFeW5UZaWYgZsPUfvipjv4NaQnFpW4Aqxv_RwO02Qte5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=JtUej72CaI0skVm54nMYtUAvHorjo077IE-v_SkYYnqWM9TmZyPq4dz9TYndTDQDrXvemm7VlC2HTLtKAFukJyfGxxnywx_mdIwajrU91biJwK5bW2tGR54GK3IF5n2hlUK-vOV7xDaxCKfF4K9HDAPn0PwFct_VylScJo3tEWeN_tMPjRCSt-0_gNwgJFtR02SPv37pIgn0PApyLSUUJyPXJMnqiuhbGbdYU7uHNuHjK25CBGIVble2zEMtGWDJMd6-zRfHnJwBTgiPtG-br79AS9E7puPw5lAKRWUBi4RJVcoeQFs21tq4b9HLi_h-JqWcP_r0ixcDn3cg1YZYpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=JtUej72CaI0skVm54nMYtUAvHorjo077IE-v_SkYYnqWM9TmZyPq4dz9TYndTDQDrXvemm7VlC2HTLtKAFukJyfGxxnywx_mdIwajrU91biJwK5bW2tGR54GK3IF5n2hlUK-vOV7xDaxCKfF4K9HDAPn0PwFct_VylScJo3tEWeN_tMPjRCSt-0_gNwgJFtR02SPv37pIgn0PApyLSUUJyPXJMnqiuhbGbdYU7uHNuHjK25CBGIVble2zEMtGWDJMd6-zRfHnJwBTgiPtG-br79AS9E7puPw5lAKRWUBi4RJVcoeQFs21tq4b9HLi_h-JqWcP_r0ixcDn3cg1YZYpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_gy6t8GYF2TxYmEEOY8rVCOOViLJy0bd1YkkBC04T-PAiXR1jZ03BhS4DuZwB6bN1li-wEZ2prglJkf5BSJkEmd4vpZGapMggw5ZtaMPDv_ZQl8MTrFE1yg8MgHg2zrtisDBd-MOqvHQ8NLw5KJY9l1wIkh4stcwxVFMTChDttStD0YbNK5ofPAr6tz124SczSUWAWHcZ5oXFNEldx9HoQApFc2aF22hQ1zTJUL0cW07sWqnuM0SpyKk8UCUn-6H7SB5LIfbfpdkqYwmmkH3LG7UfIaTsVCt7AVh4vEp53RU6Fd4kNaMRVrgEBfNtl9N0gGF8vzNFkGjXuhbkh8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=iRj8-k_G9Ng9dTUcBtgYqO5tQc8dkVvxPQonwHtqcnUSHlbKYQvRHiELJlFHc6x4Vx0rN5shR9rj3Lc8ilv8hAEIWYCxb0D0Cn_ahWnIfXbRG911nWv0gt8hFdKcpOBo-bBQNqha_xU38lyBvEMe3wBnkOblEx-iGQet1Kx6Vykn8JN_5ZMHmHszE0A3tBjjABOgzuGGeCjLrohJQJjmdo0TXJD-hRGuEkIS9i-SK-NvFwthMNGNCSvk8IQkWlQTkA-vm7HgzpoGupDoWdL5F3kb7ZGvSZBV-7ALkuR9K6On0NTDLi9ZVhFdEbcmYEfSnKbvhPtvFdo2WPDq0N8GPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=iRj8-k_G9Ng9dTUcBtgYqO5tQc8dkVvxPQonwHtqcnUSHlbKYQvRHiELJlFHc6x4Vx0rN5shR9rj3Lc8ilv8hAEIWYCxb0D0Cn_ahWnIfXbRG911nWv0gt8hFdKcpOBo-bBQNqha_xU38lyBvEMe3wBnkOblEx-iGQet1Kx6Vykn8JN_5ZMHmHszE0A3tBjjABOgzuGGeCjLrohJQJjmdo0TXJD-hRGuEkIS9i-SK-NvFwthMNGNCSvk8IQkWlQTkA-vm7HgzpoGupDoWdL5F3kb7ZGvSZBV-7ALkuR9K6On0NTDLi9ZVhFdEbcmYEfSnKbvhPtvFdo2WPDq0N8GPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRtCIp-S8SdIZZ6-9b18Gm1_bpG-xOEX8F_h042GLFPaY-k67ncXPqkRE2IdTKx3D1GFxvW6reIK9Y3Rz5gxqu7yGo6Yg6is-H4H6XH34GsVo35yO_-IXjnqg6EwFbIsFwwi446S0g-zFDWN5Ejhg7VPsCNwjQ3kEv_BZvCqWKlEaGM7bBwFD7ld_OvdDnOA28BH1BrzpBd3UhoIIkZ6j7ShvOdMfSLEmXx1YmzgKVf9-dP8GcoGeoXBMX1NzBG_-NLyxgJJjca0pToNQTcBIO9Apav9IdhHgkwQ65_6rT8C9PFbsb6aeB5DEZD7MFvCpQKcgksC4RrLiPIy8FHPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3lDQonxuayCGC4Gm1NTJw80O3y2TQ0f8cRTLzUYLbbeOEa_h29EyemqcBEnXEUOGGt82ZK95UUPcwPfObWvvLoJVh-7RHEEr7TxN3YOq8pgaWqywORivE6ia6nO4iNQYlZ_kreqGH_iCQJLUDrO0Ueduo_jHiqW-HTjW0T49jODB2rFgmQ5IRUAffQA9vhomnF6xVsuu-mCfk6j3pIQVKZoJdNHBYj6AdDEbDRiUkIW1Irr-qqly9Tp-3Z0DmOsIi4JJnF6yq2Fnr0AYHNUqUre0jS0LwqHM_JDHmqgI8_fHL0BBaITzH38WUFuf_ozmZEfbTfzgvUFcHj0DJTLfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqQE0-QRzehMAh4EI7GN7BaXbnfEF0v8rTy9KOlyqNzP3RKNgTnpHgHLfJ9OXqsRQPUMHgn0GNcspmyykxlVa3WukHdEeciXJcYJIZny4i8ZY2_lilY0FREldPjW5cmJiuxXadzthDvElF1iajt5u4IgVcMqrXtc-hK7bnliA0YxnMkpgOVi1Oierml2KUD6mdGJtc6RMnQUiL3g560EB1f95ad9Z5FCQi1cL9HStnQZrSwgaor8f2LCF_ikelqRLM2O4wE3SoEfaTydFQKpbFaaf7spVIAmuAu8GE44JJJxabbVuSEXB9EBMYMv9bDGlRqg3LwIsjk0zLBqXgbFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJHKpyJuqRvS_43ECL76T8swcL9AeSIlXYvhOS_Y5KMpgt496r_gggqLoF9qat2fF1xLGVdAoOnQ_yaaVlapqTKY8mDRogoRpYkCeHgdO8xm0eOUulDIZU88VipiHbA0gmXlCJ0Oi4rKaTAGo2j4ZNkyfyBYPbP5DX1e0Kx5OHKfgZ-UEzjKYahG71oY9XCok0FHQyW0_VKvPxRWJ1Rg9VsmuPNzsnKHrD5shqo_HqPnxIPIBs1HGpmX1yFWQyWze61XGEIV5RrWLvtDr2qXjDPNbgRq2toxw7ZuSlvr9_uGmkYCHrjPMf4R7OO14xiMfPwMM3NO75dP-EVjzmQFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6ITcW_mVnfgQW7e2AL4XL4Qnuk9uTdOxXymzdXZba3TzuELA7hq_caq14p6W7EkeSTVN4G0QQ26dB9-0cAK4ucQL3ukG27obgMWwKgJYezgAcF5vBQ-r2pLjkGK43n-VNhZR82oLjHUoHBAH22z488zgv_fFkFdGnt4BmTZ8ngB1g5cBk0NqpS9GuChOrpQHN6pJsdRhw3Ev1r_izZe2ylwNbl0ZbEmRX8BVOHq6v_0MlMPOIrCATUUbRCsLc_ytvC7g68o9I2-e7dguD1qOKpnu20dW-YV9rA2thnnOioXLxnEDSp1Ih58EqhQaxMT0P621ePoK1eTUBm_jVMkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D61BORPbHo-44OJVlBvyDj14GB04PZjN3mFYb2qXGJsiuu5N6zyzUC4oOWuD49NuNfo6MW15TBhuCoN3kN78uhPUM6uaf_P1X5PiWlaal6NSlXm5LnQel8fCeAfXsIovbcm0jLFKvbg1GD-XLMeH2zWMiJqDM0ASCaC3uUB53gC_1p3pnX4U1Tg2wc1L_-rijeq3NtPJc_yd2DVot6JTniTJ_8fxxp6K_X5cpI5rKBgYk714M4MxhdczYcBsLG5g0i-gYnV1hmnMcX1zvLvlg9vaxvJchlLqdf0ajISlSEhk3OzpM2eN2oMu2hl6mTqSbjHmoaf5TsSySjIIiHnGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnTHviTYnuWhzo6muziPnPRwlmZo87Vi561DXIvOCUvyxfB6osJPru-ysJHeYYaFOCNTHH24G0ijxH5z7RcQ897DZOMoEtNmjUlwdqk5Ada4vZGBb0mfhqNgwaZfzJyTnMg_hAYZ7mxxWnjEkLGCfKZs3GZDloWxkv5m75JPcZOwniHHlLgsVuRoQXq3GAMB8ZZ05xp0jBgpkTGBW9E54DVNF8Xcb64gQkMIp1vFSpvA25L_i5VLNXOVATRp5QJmM1KITVZKqRDhF3xm1W6HRnzr-HFA88sZYkW3_rS6l8KauhwqffhHtnas1mCqITbAwAWHQSxQqFwGRnECSFss9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq_qsbgrM9jyGfvZjcK7ikKc3Va4NJ5KDHLH6fUPyiw6ma3U4954yQCFPxRaosMQEb96AWXIzuMDTkEzOIBrz4SxDYkYL4pFLyVyr9jyhdLtOctCh_hRcRuzsKnL6i4LBrtN_XKVY_TCQVfFU0a4l4t0ZsQfBnGEIA6pVzBYmmOEJtPBy5GiWjUBPzU2fUMKd44fdzoLy4yU-bGY7WUErDWz8XW0NxnY0rsoXxZp2eFR-1iw-jM_jNLs4mkYK10uPsdGSFeTbOR4oX_IJDcVfnhQZGz1rOZcYk59yN6KZ_OYbR1uuaBN209PP6w-I8g6Yox3S8K8-g5BRMx8I2L80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=ADrr0ObUKaySvscE1_GclsVJ9y1YwHgPeCrrzHyj3nVIndCq-mVd0137sMeMXjV5wIoySIzksVlIzHDIJi53QPPG7GkuMiYQIh1QoGncOtxUQ2sgRJlASjS3ONdQst_5pOWB2Kmx-mdNGwnbyS3KL0YWmu7ai9ofR1MS3DcWF3f0yhq4VqXk46uUGafd_bwfXoHQ_3NUj4PYXljdg6vlyzCgDzDv62Fz9sGe84wjstwVqU4fq_yM3JWcwUzZ2oNo5zuz7lXyC-N4xjcx2Kr82mSkkOz_olusSPNz5XpYYN7nIl4NYSEgWeLd4IkygDjaB2XIiKV3fXHW2HZyZOmemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=ADrr0ObUKaySvscE1_GclsVJ9y1YwHgPeCrrzHyj3nVIndCq-mVd0137sMeMXjV5wIoySIzksVlIzHDIJi53QPPG7GkuMiYQIh1QoGncOtxUQ2sgRJlASjS3ONdQst_5pOWB2Kmx-mdNGwnbyS3KL0YWmu7ai9ofR1MS3DcWF3f0yhq4VqXk46uUGafd_bwfXoHQ_3NUj4PYXljdg6vlyzCgDzDv62Fz9sGe84wjstwVqU4fq_yM3JWcwUzZ2oNo5zuz7lXyC-N4xjcx2Kr82mSkkOz_olusSPNz5XpYYN7nIl4NYSEgWeLd4IkygDjaB2XIiKV3fXHW2HZyZOmemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqSyzdnx_yQL6TBAKTvGn1PoWRwGUrEfvrm3x2dxT51o93iDKnRJz3RUOHFAXXANsHDpVpM3LJ3RvzW4cYZGWyTlpNuNmS94GARywppGaOiNEAE3OoOGn6caDbsZV7F7C0bFs2sXnKVfToKXB8Ck4W5LV8dO0kdUfVBTi5AcWshC0tf9zWtB40QdsJY6qVg7Ewd-iuBvQDhGKqYy6J-1tEQhEMD8L6M7FoW4T7fRJlSHXTYkLmg3x2z9qdD0f8YSZqr3dfVn-BU2VApwMCKhCK6D3LUdGNqSjlRM2Vm0mJdv_bOBQm2x964uIW7x0dlaTHl7OrmiLRWvNOWrRYSlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=HlihYupPwt6-crvG90UpP8kapx-RyLzFxrSi09IxiZt8SgPlsDX8mV8kT27snhKpCIPtNKfbmlCuK4-OFIHGllmYcO1rK8nGilwmBp9tUALKpkOYDkZbHTuDZFdswwvSnqXwnQ2KAJbgfvdk_cJVqABYUmJsEIGNGhMVycPEQ0dqWefDj1wPrIFUkbYDwGMXn7e6KvXtLsKPe3WSavaHYeaozNTDglS9y67kL_b31z5-olCCKDWJ4FtHa-7tVSnIpFw0E4YZNcC7dDYnVpxM3hkszvw0rmdwRW3nv3TxWUAZD9vGZzbNsreEgv-8keEG0Qdeysrr35dPlaV6-CtQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=HlihYupPwt6-crvG90UpP8kapx-RyLzFxrSi09IxiZt8SgPlsDX8mV8kT27snhKpCIPtNKfbmlCuK4-OFIHGllmYcO1rK8nGilwmBp9tUALKpkOYDkZbHTuDZFdswwvSnqXwnQ2KAJbgfvdk_cJVqABYUmJsEIGNGhMVycPEQ0dqWefDj1wPrIFUkbYDwGMXn7e6KvXtLsKPe3WSavaHYeaozNTDglS9y67kL_b31z5-olCCKDWJ4FtHa-7tVSnIpFw0E4YZNcC7dDYnVpxM3hkszvw0rmdwRW3nv3TxWUAZD9vGZzbNsreEgv-8keEG0Qdeysrr35dPlaV6-CtQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=i_hfm47TONyVtYYa53j3WZns6ybdC2siiIdxE0wqEfI2moACVuPF3iO6nJhrILO4DYaK8aHq3f02EfDsUzKwQA-ctxF2mNd6DlUHQnkNrEm8M0O9Qo2eCmZyfBFwSutU4BSd10pucjzMIKoqoJDTI2S1h5nMBc7D0JGPUUMu6R1vywVu0ckErnAxQUtuGYhszKLk4Qxch8o-z6sUJ9bOA2zSCHVdzaCDOaR5IpPlPLGC-DxebrfRy-IeZhB5dDUCa4_9EUb3_a45bkf-Q6p-X9tT2J0QoS5GRi_u7E1_q5dFAMSgugdq19RZc5i3MIsQUL7ud_V6ei-svbPh-O0TVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=i_hfm47TONyVtYYa53j3WZns6ybdC2siiIdxE0wqEfI2moACVuPF3iO6nJhrILO4DYaK8aHq3f02EfDsUzKwQA-ctxF2mNd6DlUHQnkNrEm8M0O9Qo2eCmZyfBFwSutU4BSd10pucjzMIKoqoJDTI2S1h5nMBc7D0JGPUUMu6R1vywVu0ckErnAxQUtuGYhszKLk4Qxch8o-z6sUJ9bOA2zSCHVdzaCDOaR5IpPlPLGC-DxebrfRy-IeZhB5dDUCa4_9EUb3_a45bkf-Q6p-X9tT2J0QoS5GRi_u7E1_q5dFAMSgugdq19RZc5i3MIsQUL7ud_V6ei-svbPh-O0TVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=pqFZy-duttZlB1aaRO3PxDdotuZ-W8ZTZI8hJ1PdymSXU8QYVFmRN_sWrM0oaWuBhTWR1Zw6tt0eKfwpjHYQwE4F5ojJ5DeWWXvCf2RepUvDqaKztEtXvlvGsn5tbzU1yqu1u3sfhZDbvgpn59kYiKyIbBvfBjvaWNMqGkEvV7GR-4Ks00X5zXaAnNn8bdhNc_fxbeWb0YLgLAljGAXngXPMxl0D_s7Hw_-4E6EllmXjSlbDtqmcdc3ZZm7ujy6z5uoQb2Emus_6n9H60Q2l41btYJNH6XWruV9bbhuzPShpFaLbz4OFvConv2pvNJXURl2BN7xS0KSDsDeyrMqgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=pqFZy-duttZlB1aaRO3PxDdotuZ-W8ZTZI8hJ1PdymSXU8QYVFmRN_sWrM0oaWuBhTWR1Zw6tt0eKfwpjHYQwE4F5ojJ5DeWWXvCf2RepUvDqaKztEtXvlvGsn5tbzU1yqu1u3sfhZDbvgpn59kYiKyIbBvfBjvaWNMqGkEvV7GR-4Ks00X5zXaAnNn8bdhNc_fxbeWb0YLgLAljGAXngXPMxl0D_s7Hw_-4E6EllmXjSlbDtqmcdc3ZZm7ujy6z5uoQb2Emus_6n9H60Q2l41btYJNH6XWruV9bbhuzPShpFaLbz4OFvConv2pvNJXURl2BN7xS0KSDsDeyrMqgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AObLspjZYWnI8EQPxQ1-kAx4kY8Z-Jog-hIfzEQodz-44X3XX8UP-hVjGAdYt63FdmmUk_AdR7W31P3FuKobegLRJbKkEgnImSJxKvCntMjoURdYzsWFimnKr5Xe-GXZyYUMWSyhtPWZLb1Ds4si44U9W4rYBNu8foKi55fWSjpQBnT2PGttFHM8n2pY4yAyhm3Pdqp0shes11zG2ZO0XvISnMJ_7bWLENUI8EwxnMgQdjLMFjd0oF6J9fKXPZ0j_2Hv8NY4O60oYpEWmdtP6HYvzHLJyXvRdYazV79zYbPNi1jZWoAf61Pgmn1b3HrxPq7tFx3RJ8-nk1vSGkbM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjGLuSSwabo7uEc-PqxeHYuls1fAakFml5zfy4D6xmfJgoQw0C5zGDAMx9-HLnQh4-dwgcqeAI1RyO7jbqcHCyJwqSfjIsPXYx02SrcYK8sgXtCtmoMd5W1YcJp93STlFnlythxjGvm_mVg-0MO_aYutINeVzeg2hj9c7X8gNCKUfMeDXTw8jMcIQ1UnyrhcWGXcIbFWZ4ygN3v8xNwcsDz5t2pHZn-1H2NiSP16mGNSvIP7AQ8-TFiY8FChT1pczoHENu-gUrYMahhBiyPlUHA8KH2ZUK1ZbzCLBKqV69Qdl05tsCtsLHcwk6C04jw1QI154gdfT-cMxtxMnGfUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2LPZySDdbOfXHAzNCei31qa9a_zs_MszZeDgGswNGMEKkpEJRsr3gcJEFlZW-J2u3timboy4lLye9FChdZ4maaXzovyypsQfo0CpncYdRmEXs937PFcn5BxhqxIYdGhu0YiTHst127ESutpP3dfpt4LwuXunuLUUEeRtxQ9YmUt50rS9Dcxu2oShKlvchkE9tIDedcIm63Jfr9nQubLGcieuz3Hz-xyTYIrYdHLor_uNLiJWd30guZAFx8JJMnbpUkWO84D3N5izUhQeff7tN54096Os3UtZWqnQSof87SylXJcgCyUeZ8bINI9IvXHBLtw9CHdWw8zL2cM4DRTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4YIHUkH7iIlmhJhqZBayPQQyCm7j8qTC83Q12jiwRidP8oNbIHW1xgE5OFKb-pBwtkF2pmbm7PPZlUcgzkVZe7gK03L5tSN2yS8Ssq-1QQ2qnAZ7MAueYjzJSYqelUTlqp2QPzSlFsAutR3wdyupt0NwFX0IkHgu5a_0hABzSbtqVuHehnA6tJNQFeAbE0Sp82h2p0rdXQwWydO8-VDNyDFmdk2jBax65JOgCv4jDNoIcLA-7dmua-RStJDGN2_htdFGHRbn3lBmwIcH-RiDBJYTwP91SSwQ9ABkC0enXnwXavi9S628tmF62ea-1VwfeJ3dO7KQ7xJHrx5YqBRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWPkza4sx45VmMWDxR2ppdwCYjENjdtyIF0dNUUtNzWxPpuzZQ2_FDLKLHL1n94wAyPBEyWVNUGyrdxdPDwevxByvqp7mqGKCl9hiVn7Y5mgsqcGG4o3HgYSrlDptU7RX5_ujxeCr5hYZY1U5z8Z-tukZWVgAHPYLEJr5xl82cXST4DNSsJilG-mm_EkoGp2F2E3jqZkPxNrQigveBB0K91NGpjFmbAqSaSaowPziNBS7eg_mJ4b1nsYsrjFWZi_eCc1af8Y9hTVsH28Lhwj1SwvV9FvRHSHZcwaT0drjl_HVVxQz39H2ZAhU0ys06hW6u8lpEb0yE-ltXTGrFreew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr-C96c1ZXfeWY9GJDqtO56I6zhIP1ivqFQ2whmlfwkc5bdFnp9kRlWaHmtyLDjkp5dFq2X4gxHTlRzGwQz0747SZDD-OccBWQOdzqpoLNUnM30rpxHQN4fnJfi7x-DgtkcRDvJfUiQLdTOL2KlzUTdg00F_yCGL6WDagM6tHwG58GIRU7EXbE85siYsxwIUQMANyYHFan92uOHkvkrA3LtoOkezmKxokArcyY7QXEajxtAanedTrCBu2mR47bTBvsvF3NCNTkdLpAijWF9egoGEtfkOLkJwChrSgJ8FVkWhPOY0m4fkz7jROSAe7aJTrkFzpLgFb-dKQXVyLc18eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=PVsaqsgf9mpOBeky78ORIbFZmRXiKk9h0mJ1NLx0mAG731Ac7HhR0Kkd6QqkmD7iJ4ZnmNEjvNMWJjXwkfj3wg3dEtG-HDDoxM8LKjTcl9SfMeBUhIvGeXK-3I3OcJZySzKWbNvSf2fb9hO5vvW6sGPfY9-Tlu0JLDidsUN8jSSJ2ZRMVFdEm_JZ3Pgu5SB7v2hvjXiX27wMX175nT335NvTqscHEl4XLYSNltUaoK7Rxw1Z0nyuXSXaVjv3x6uG1s2xWwH-NPauHDBcK6ivMHYPQtaRxHvP2TPHXggflywY7aqVZlzbLllsytKw6EqpyomWkZitdQqZUDjjEqYvPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=PVsaqsgf9mpOBeky78ORIbFZmRXiKk9h0mJ1NLx0mAG731Ac7HhR0Kkd6QqkmD7iJ4ZnmNEjvNMWJjXwkfj3wg3dEtG-HDDoxM8LKjTcl9SfMeBUhIvGeXK-3I3OcJZySzKWbNvSf2fb9hO5vvW6sGPfY9-Tlu0JLDidsUN8jSSJ2ZRMVFdEm_JZ3Pgu5SB7v2hvjXiX27wMX175nT335NvTqscHEl4XLYSNltUaoK7Rxw1Z0nyuXSXaVjv3x6uG1s2xWwH-NPauHDBcK6ivMHYPQtaRxHvP2TPHXggflywY7aqVZlzbLllsytKw6EqpyomWkZitdQqZUDjjEqYvPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuMZuzOfWcSzb27pzD9MCi72tOWFRtyHj82mBXCBpLXCVxUyDNw9BmjqecKYxyl2KjilEOVAtT9OqIxMKVnLLddlkPZO26SvZ3xEiOqlQYAufIOJCF-6SVenkGUJKuO-9NSqzKhg6fp579aw-ZdFKAltzQ71cLO7nnSAsS6E46V-PtlCKXHD8P5dN-j5cf3XWulVg5cqrpSyr9gaHYPZyVoS9xbdxMqcXo-mcnaywRfSbffh2AH_fUMPBhKpgIZ3PAWI3onpdn50mp_O4V2WRpCjHfOC7JAf0xF6ATKlCq2SzlTUkQ6a2fBfkuyoMIvYijJSWcIYMTh9Rjjc6yReAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLJQMomvA_AP5YvKQx8ZeuaTjK_fWWI4_HhxPaMBkOCrTWdHxBYkZQZxK-1s8rCR26c97rBZTPNyor3RWPcGrDHN33To746rndMG_LQH-vN-uhvCiA-DiLx6QB9o-Lbb5CPeqHBJUyC0RWw-m1z5gZBqkJqeem3vbt-Y5DhJOEUYXGlsktlPVwO4ykG6V7hOlvDUZ448nZFy4_8riPFYPIwKMe4cjZPnIEDYPb7rp8zXG38tFZngAmIk-WVzGTWmFhNeeWfTZkqeNkuWxbHopH7vSOXH_0IDilx4Dh5wqswZtUeb2GBGYEIg1YpCyNS1BNCLg6MtUdD1B78rmr1Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoCApCT7tRAgg6JicAtUXKayFy8-PfeoInRAd0rjQZlZvQgdt3yA4_lLqzqar1NZpDpzCLAohp9sPafzoVEe4altdy72e6HSpmkCqMlG23U11QDlqMXLW3HNGsLQmS_UgB4i3vW46ACbD4WNJt-594lpRZ02qC0RTcbpuzD9LhtqGY991fbAFkKyDkukRI1ueKuxzyntK02w8VGWYk5NcSqRIozZ4r3iPEMgXU7ICWMJtSdxgAK9jMju9-NJaK5d2tASc871-5uJ1XchpEEIgSj3_PLtwq8E2fYV-Aqc670Jgbr6oHbFmJHbdtUCRK9QFEhgSJkPEcRoPe4yifc2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUjGY233BAUO8GZGf7eThhqRTfFx34NJMTov1wCGEgyrmXupnruZ8t1K1WS1ihriXzrAh3fGlV6IXYok4vEs1DiBZg0Z9hBD3Z51ALPyTXIaQeoA6SWhWjBi8kAZsvM3fHkngqCCRwu43LYIeoXjatwndAF2LfXiVEhTJzinLnFXaXLrJV-3LDTytKkOiyfcz2L71NWGYsgl8a-AxI4p53qoOADMocM5c6uKZYy7mBUl1po_PjIODb1IsflACKFfNT5rTCMyOYQNp3wtorvbPMjOlgPt1flWBeUGtfpi8svuHlY4Vej0Ow_p03D_mKOwTwj6KtRfu1MNx7gl5O8kbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmhPrJwFUigld177OSk0WG1l1bbp_HrqiA1r_aIIhzyK3qRmaheXmn6_a5aOscARuvUVHRK21qRRLgs69uyyzshcMw8GyaR5dS9fBJX7U8oIvnKSWMYl5VLRgkzYHuStmwY0msiqz_oxKtV_496wjZ7jye3y0Px0M5qM-nS_wGjOTk1jtWxoj9353Ze-P0geXRnd0TwEA3ExHu48xeNbFCRYtO5cJpI3YC32caJeBmJ9Hk_VMeMNDTpqDsiSfGVKmE4fjW1UILgMnM_riBNvbMw6sSjQ3J_kN67hpUKD2GDOTPra65kisazUy9AKHAbBPphwyXDDnl4eodDmFaUdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC3Oxt6ntRH75PVUjYWOT_XzouHwaSHLDdJyOkXOGZUmSD8PVnagunyT6R9dEBHIQ-50NENWb2Jn9g6iqMHRLkubDFkOeobHBln5RdNZBPiOuv5Ttk5FOSok794jiAMc1IhSfa18pokD9QKUKX_-XlM0BbCgdPVB0kWixdPQ1rjZGIO2I5lBwZa3UHr4FrT0OfONmq8QImlnsul1IlkD5LWLah6NfLhl_lHtXZIxpTCx6QgRUj62p3Vooz29SfD3S_VZdcJpb3KryymCRlYmWGtIFhxrpB49not3GaJhtgmNM_r3TOH4AsLKPax0KsigSJVem4kprOwx6i-Ds1khpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
