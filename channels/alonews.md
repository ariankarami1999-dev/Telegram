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
<img src="https://cdn4.telesco.pe/file/jBi5S9davFQ3OZbsy6ezOQHvkkB_7_q58CsS9y4LcnZYjfJr66v6ioNHBi1fXKPEyIaN0TVoKTxgtYqzaNpzGCjuaSnrEQhGFHMDOkK9p-WD9GR6eWXvIfHXVymADfFQRKiz80Va4QscDO7D5jdtezieTOm-VqE3_QSpe4yiL_w4-Zsys2n3Tt5h5H3qGTCbT6Al_cMAKVa36xk64h4XuoZluQ16ptBktPJy5ZRFaefDsRoNH5h25g8Pt_tpqKSE7X6Elr9UfurzN133uv6zbGeeMwiCJJnr2j1m-msDpW_EPCe1YDYLv8A-Pn0tj36hYwQZMJmMI3aWOhoo9x6WZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-149401">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqnnb6SBxpby5et0Qc5nIYlotkZrpMCrtZ3Z3PPlJo5U_6DUMiL5uRzBML23BhWptXWMlNzUjZytkzKs6H22rz1VPROCi0rJu99_2qoAl-YCAgq7LFxMyCkFeFH7ZhyylIzGR4jKjSl5Rff_i8ruZusOwjKntx2vQQ3rCqF0t1uRs-T8-C3Cvxg9Q2z-vJ4QEri65v5JdMVjO1RcprrRbv4wEYIWWbpFZZBK_sASfMDcsiIkGgvtwxq7PnxRx2V2cUGF90cpfVvjjGaQCp0vOE8rMXvAKHQoLnPpT3nwplJ02RKIdI_dt-BFIcklSVb_a-6SnZt5_aWUrAT2NADz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه، گفت که از رابطه شی جین‌پینگ، رئیس‌جمهور چین، با ترامپ حسادت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/alonews/149401" target="_blank">📅 20:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149400">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سنتکام: تا کنون مسیر ۱۲۲ کشتی تجاری به سمت ایران را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/149400" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز: حتی در صورت پذیرش پیشنهاد تهران درباره هرمز، امتیاز هسته‌ای نمی‌دهیم
🔴
یک مقام ارشد ایرانی به رویترز گفت: «حتی اگر آمریکا پیشنهاد تهران برای بازگشایی تنگه هرمز را بپذیرد، ایران هیچ امتیازی در موضوع هسته‌ای نخواهد داد.»
🔴
این مقام افزود: «تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149399" target="_blank">📅 20:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره:
پس از نخستین دیدار میان استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، کارشناسان فنی نیز به مذاکرات در نیویورک پیوسته‌اند.
🔴
اگرچه دولت آمریکا در ابتدا برای هیئت ایرانی روادید صادر نکرده بود، اما این روادیدها به‌سرعت صادر شد و به هیئت ایرانی اجازه داد به مذاکرات ملحق شود
🔴
طرح پیشنهادی ایران برای بازگشایی تنگه هرمز طی هفت روز، در صورت کنار گذاشتن محاصره از سوی آمریکا، در حال بررسی است.
🔴
این طرح نسخه‌ای تسریع‌شده از روند ۶۰ روزه‌ای خواهد بود که پیش‌تر درباره آن گفت‌وگو شده بود و شامل اقدامات فوری برای بازگرداندن دو کشور به مذاکرات مستقیم درباره برنامه هسته‌ای ایران خواهد شد.
🔴
مهم‌ترین مطالبات ایران که در حال حاضر در مذاکرات مطرح است، شامل رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده ایران است.
🔴
دو طرف همچنین همچنان درباره ترتیبات مربوط به تنگه هرمز گفت‌وگو می‌کنند؛ از جمله این موضوع که آیا ایران و عمان می‌توانند تحت چارچوبی مورد توافق که کشورهای منطقه و آمریکا نیز در آن مشارکت داشته باشند، به نوعی از مدیریت مشترک تنگه بازگردند یا خیر. همچنین ترتیبات مربوط به عبور و مرور کشتی‌های آمریکایی از تنگه نیز در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/149398" target="_blank">📅 20:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی عجیب قائم پناه معاون پزشکیان از برش دادن کیک ۹۶امین سالگرد تاسیس سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149397" target="_blank">📅 20:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149395">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZ37ABgVsisp1BniNGZebDaon9ABNqGdE5vqitWx3i3Om2JSC_D7gzDAZPQXmQ3g38wmrYZ8FfWWvLBneszEN0-GPo4LdmxpdodV0fX46Y23aHVAb6311rsZ5RKzRU3zDtuTNnScoUoX1v0Jv119xZHMQGyDdgT2y4FJQK-GFTUVToNmv2qrHd6HdbTD4atmOiDeAZCEaeIRBVGPtR4iNRvSF772axkE2L6J7u_H14oWpF35_BLiOGDimrWo9z5BQdlrCG50HFCyetGNjOiEmshAhi24tsnf8VMDj9L0LdrKNoYZW0K7fekkkUuhVBoEg5FsJMATRolKEIvtzKB2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOfD56UIpbo2-wpz80WEPHKrF4nJEFx9mr77NmY2HSKZwaUhzFGpcLHRU2rX5wPzkn-AtAtZlLYhLrLIaHBiC1MdCkkAFHW7O1LEJrIeAKG91jvcBJ3Hz331KlLRf_1IgIGk2-42FyZdUaTp9KggXlXSrHgTxEUv49xJmzWSs1yhMm0BkzWyxTB10nSKsGCltQU7WldV-arQDLv3nKvDrAb01QFllnwvUpzsdIqWuA3CkcooQ8ucxIj0xUaF3Vrkzqdv8T3AlAqf4ldo8xy45L3aZD_fq5C05iZOwjMpR7WHFJ_JxF2d8vniSGxelRgqP_l0xfy3tiuzt1g12CxPMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرماندهان ستاد‌های ارتش عربستان، پاکستان و ترکیه در ریاض جهت مقابله با حوثی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149395" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149394">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=gCAN634ZQFci-88X9AroRqIz-fqws0hr2gC2YDRnRYoApBMur-Xo7c6JPL0_L_NB8jxT6b0sL_fmyN2repANGYyt31yyRlXGMlv_Dt3Bji50JdQN5324GFj3JDHAV2DM86khGVim3m01K-ipp2w6y0k7-6CcdG-gqQORmiLxAmAIO3aKD0kQr8X7hWvi7wre-iDmGNNqG824VAuaSPG73AjHR87DKBfsADQjZbMFU0vqhfUxANpz1wd0rZdKzlDjPC4lZ7LeFZDIP2TgbM8k4U5rMTDLLg1le9Y125G_GEbss8myMhZbCvHJ4Y7JWYTgdUqKlLayeu9FyZWgoLj0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=gCAN634ZQFci-88X9AroRqIz-fqws0hr2gC2YDRnRYoApBMur-Xo7c6JPL0_L_NB8jxT6b0sL_fmyN2repANGYyt31yyRlXGMlv_Dt3Bji50JdQN5324GFj3JDHAV2DM86khGVim3m01K-ipp2w6y0k7-6CcdG-gqQORmiLxAmAIO3aKD0kQr8X7hWvi7wre-iDmGNNqG824VAuaSPG73AjHR87DKBfsADQjZbMFU0vqhfUxANpz1wd0rZdKzlDjPC4lZ7LeFZDIP2TgbM8k4U5rMTDLLg1le9Y125G_GEbss8myMhZbCvHJ4Y7JWYTgdUqKlLayeu9FyZWgoLj0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ: آیا درباره جنگ با ایران با رئیس‌جمهور شی گفت‌وگو کردید؟
🔴
ترامپ: بله، صحبت کردیم. فکر می‌کنم قرار است اوضاع خیلی خوب پیش برود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/149394" target="_blank">📅 19:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149393">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازم عجیب اما واقعی
‼️
🔴
عده‌ای بیکار و علاف هم جلوی منزل حسن روحانی تجمع کردن و خواستار محاکمه وی شدن
🔴
این جماعت معلوم نیست از کجا کسب درآمد دارن که هر روز ول میچرخن به یکی گیر میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149393" target="_blank">📅 19:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149392">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=QHLYIsu4As3Rh_TZ5r_NvcPgJqn698RB_IdVH4vSoricJ91_MY4atRcESpsFESV6qJQEwxWeienoAI9-X7YV5iYe2q202zinUPwAG1c4RXCZYYnY_PhB6cgR2gyOuyJuoWPw0uKs7HyfNBrmf1W7z0LNJMAeSMQwAGhz3ka_e3QROkpPKc56YxC7jD2xymDYWIXU8WlOw9XCIAgfDJl7ig-MsMzJqjBGQHAtFVVyg2DNJsOp5Ta1hIKEcHFSv_nLgxuHSQQdW7uY5Z2DSxYHzQ9UNeRfX2oKxgGPWDhs2uMJ2WEbn77ISCNC1zChytUb0BERihtB4gKUST4ij0KHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=QHLYIsu4As3Rh_TZ5r_NvcPgJqn698RB_IdVH4vSoricJ91_MY4atRcESpsFESV6qJQEwxWeienoAI9-X7YV5iYe2q202zinUPwAG1c4RXCZYYnY_PhB6cgR2gyOuyJuoWPw0uKs7HyfNBrmf1W7z0LNJMAeSMQwAGhz3ka_e3QROkpPKc56YxC7jD2xymDYWIXU8WlOw9XCIAgfDJl7ig-MsMzJqjBGQHAtFVVyg2DNJsOp5Ta1hIKEcHFSv_nLgxuHSQQdW7uY5Z2DSxYHzQ9UNeRfX2oKxgGPWDhs2uMJ2WEbn77ISCNC1zChytUb0BERihtB4gKUST4ij0KHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
امروز بسیجی‌ها به یک جوان که پرچم آمریکا رو پیراهنش بود وحشیانه حمله کردن
#بی_شناسنامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149392" target="_blank">📅 19:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149391">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گسیل ترابری های نظامی ایالات متحده به خاورمیانه جهت امضای توافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/149391" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149390">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
جررررررررر
🤣
سفیر اسرائیل رفته استارلینک رو تحویل نماینده ج.ا بده نماینده ج.ا هم عین دخترا قهر کرده و اونور رو نگاه میکنه
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149390" target="_blank">📅 19:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149389">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
👈
رهبر مذهبی عربستان سعودی در بیانیه ای بی سابقه از تمام مردم عربستان خواست برای جنگ با حوثی های یمن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149389" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149388">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHYZvoRQxMmBMu4OzgjP9lpCtwyUAAqTKNSm5FTS7bwQWy6d2flK6IbmfmUruvAkhcROxNNKTIF8BBNabuhnXAtYhLfTfrs-B44tfjKpU6i3gSuZWPL5zpcRJRZbrwCgLwukNTFr07xcoTxtZ1_WuY6XBhx4_ZxlFci_gn1XdHsF88HfdJY4UtbM3gue95s6IuP66sax4ylvinbOOx_-5_Ij0d0WbkD2c_X5J53NJIFDh2nGKcn8M_zPlHM-rgGH1DLrejvBbA9Ma5_5p2MpI3AgGnSNgo-9aNudUi6h8fZ2HuCzlfHmLmqHi_kqeizCwba_E6cmoHOB6SePSEu97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
دیروز تو تهران 96امین سالگرد تاسیس پادساهی سعودی جشن گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149388" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149387">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فایننشال تایمز: حوثی‌ها به اروپا تعهد دادند کشتی‌های اروپایی را هدف قرار ندهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149387" target="_blank">📅 19:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149386">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=DOwXIg4wLo3ZPBmUVVXBwYZL27_6P42iFyveXhJobJtwH71hfsN3ZDJnQhWnwqnVhO0q9b9-cfHTTbOBIJ2xKvRKLeeHdmp0UCFNogoOJj8v2716ru1ESXroE7fYPgFfOhqoFEugcz-tly-wYCmpx_COhrra3L_vyCELmsg94z2KgkwW-pnK5PaULlv6GaFkcOBmxzgXTwpNJxW0ewEv9Gwx17SKHbPyFy0aZrpCv0dYUWuMgPR879PnJLMOqYpvOJpZ6Cms-WEcqHI1LcHn7Ul_1-f3aLKDLgQg4yGWSwGnbnMnGOh_Z6ezXFTfYlDno1WcHzRaDUXkOZCewePlOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=DOwXIg4wLo3ZPBmUVVXBwYZL27_6P42iFyveXhJobJtwH71hfsN3ZDJnQhWnwqnVhO0q9b9-cfHTTbOBIJ2xKvRKLeeHdmp0UCFNogoOJj8v2716ru1ESXroE7fYPgFfOhqoFEugcz-tly-wYCmpx_COhrra3L_vyCELmsg94z2KgkwW-pnK5PaULlv6GaFkcOBmxzgXTwpNJxW0ewEv9Gwx17SKHbPyFy0aZrpCv0dYUWuMgPR879PnJLMOqYpvOJpZ6Cms-WEcqHI1LcHn7Ul_1-f3aLKDLgQg4yGWSwGnbnMnGOh_Z6ezXFTfYlDno1WcHzRaDUXkOZCewePlOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در دیدار با شی جین‌پینگ: این سفر برای آمریکا و چین بسیار ثمربخش بوده است
🔴
دونالد ترامپ در جریان استقبال از شی جین‌پینگ، رئیس‌جمهور چین، در کاخ سفید گفت: «آمریکا از این سفر بسیار خرسند است و مطمئنم چین نیز بسیار خوشحال است.»
🔴
او افزود: «اتفاقات بزرگی برای هر دو کشور در پیش است؛ این دیدار بسیار ثمربخش بوده است.»
🔴
ترامپ هنگام استقبال از شی جین‌پینگ به پرسش‌های خبرنگاران پاسخ نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149386" target="_blank">📅 19:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/149385" target="_blank">📅 18:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نفت خام برنت ۱۰۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149384" target="_blank">📅 18:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=l7e_2uWPACQQOv57W_p9aNz9oiC_dzMJNZeJs0Vv-LWgvme99O6-uzAg6ST7nOHb-EWPQrPnGY1ujAcVdolRGrXwkjmX0J9pWFvmTIuxlc7RT-slNo8uBONrjEddojKAE3SZKeySsLCHW2nDxPtEYb2W59A9WwCZ1FTuw4OrSxD34a-FUPhle8tFXTd_EW_PtkHP6XY9LjKjNptsBKCy8v5RKOT5602_9vGBkBBKWMmrqa4JOPiCHYZXqf9gtZcHdrs5cNy91QxBIOjgJnsrM3Exxy2Gmz1P0ediHKDK9JUrIYZtTO4pYCvxSXC5v5Cm5IF9Grl_G3ki5JUJrzsS5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=l7e_2uWPACQQOv57W_p9aNz9oiC_dzMJNZeJs0Vv-LWgvme99O6-uzAg6ST7nOHb-EWPQrPnGY1ujAcVdolRGrXwkjmX0J9pWFvmTIuxlc7RT-slNo8uBONrjEddojKAE3SZKeySsLCHW2nDxPtEYb2W59A9WwCZ1FTuw4OrSxD34a-FUPhle8tFXTd_EW_PtkHP6XY9LjKjNptsBKCy8v5RKOT5602_9vGBkBBKWMmrqa4JOPiCHYZXqf9gtZcHdrs5cNy91QxBIOjgJnsrM3Exxy2Gmz1P0ediHKDK9JUrIYZtTO4pYCvxSXC5v5Cm5IF9Grl_G3ki5JUJrzsS5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و شی در حال چای خوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149383" target="_blank">📅 18:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کارشناس نظامی صداوسیما: در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149382" target="_blank">📅 18:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc1yUKHrfPcH3-DzCC_t3Oe73FXLROmMdWt4w8e_WB8KAT0wBGhsGj_AKOsCW6w9_pXS-tAiVZcsb-qkWEna_-2ASV1slsunEczkTUvuyL6BILQIkSsTm4j70DAtKDWoJ6PW4EQvGCVnVaq43_tx0qo6btd6kpvu0BHe0kwgbxCIv7H8zHTsRltxMvTwt0k0d3tulAFQfn_U4QzdxLN38hhitDK_a04NsyzK4f7_gsS9r4kPFjlqSNQBhNX1INkOhpH9_zE77J5NdaabGRxLingndl_2lsdj2y63PXFhhm2nT76EfXOROOeWRsmstEDTa_-_8G8uXEE7oWlLmz7uEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
عراقچی و پزشکیان باید استیضاح بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149381" target="_blank">📅 18:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVqRLL59Ww2vxsqVp4bfiCEJdKpQVSdi2EieJs7gwwubgCubYo5qvOedFUAHrL5q_wg65a9DMb8m_2HoB9BMz3ugJ5zC1l7mbtKi9hULIW0hRR3OksqFAHw69zdNYSlz73p5P6WADMTK_XCmZzeK0vOCfB_Ye-VP19AvMf091Mvu6FKvkpZdYYHQKSpLHm-SAqHAjkNoOazoluGzs0T8vZodI7UqpeByoH4qIzMtlAIk2YHqN6YNNrkhHm53s9nciclJi7WjXr2Ey_L7Q8ipntgiFFcaSPZumPbEPXT7Z48EpSRfEPejqYrBPMlUzPrKnE4AKqxC5PNJutF5vnap0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
«محاصره هوایی ایران» (لغو شدن پروازهای ایران به کشورهای همسایه، منطقه و دیگر نقاط دنیا)، پیوستِ «محاصره دریایی» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149380" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ و همسرش، ملانیا، از رئیس جمهور چین، شی جینپینگ، و همسرش، پنگ لی‌یوان، در کاخ سفید استقبال کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149379" target="_blank">📅 18:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: ترامپ آمار اشتباه می‌دهد؛ تعداد افرادی که جانشان را از دست دادند ۳۰۱۵ نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149378" target="_blank">📅 18:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم: نمایندگان آمریکا در مذاکرات با ایران در سازمان ملل به ترامپ اطلاع دادند که تهران حاضر به مذاکره درباره برنامه هسته‌ای خود نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149377" target="_blank">📅 18:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مجری فاکس: شما میخواهید بمب بسازید؟
🔴
مسعود: نخیر نخیر
🔴
مجری فاکس: پس چرا اورانیوم بردید تو دل کوه؟
🔴
مسعود: اون داستان داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149376" target="_blank">📅 18:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💢
پیش بینی پشم ریزون قیمت دلار توسط نوستراداموس ایرانی</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149375" target="_blank">📅 18:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر خارجه اوکراین: دیدار با عراقچی مفید بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149374" target="_blank">📅 17:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وال‌استریت ژورنال : پس از تلاش قطر برای برقراری دور جدیدی از مذاکره بین ایران و آمریکا ، دولت آمریکا به قطر اعلام کرده است که ترامپ قصدی برای لغو تحریم یا محاصره دریایی ایران ندارد.
🔴
یک مقام کاخ سفید نیز گفته است تحریم‌ها و محاصره دریایی، آمریکا را در موقعیت قدرتمندی در برابر ایران قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149373" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی‌بی‌اس: ارتش آمریکا در حال زمینه‌سازی برای اقدام احتمالی در کوباست
🔴
ارتش آمریکا در حال بررسی این است که کدام واحدها می‌توانند از عملیات بالقوه علیه کوبا در چند ماه آینده پشتیبانی کنند
🔴
واحدهای درخواستی شامل یک گردان پشتیبانی رزمی، تیپ پزشکی، دسته جراحی پیشرو و یک تیپ پلیس نظامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149372" target="_blank">📅 17:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
توقف فروش بلیت پروازهای عراق تا اطلاع ثانوی
🔴
سازمان هواپیمایی کشوری: در پی توقف پروازهای اشرف از صبح امروز، این سازمان به شرکت‌های هواپیمایی ابلاغ کرده است نمایش و فروش بلیت این مسیر برای امروز و روزهای آینده تا اطلاع ثانوی متوقف شود.
🔴
شرکت‌های هواپیمایی موظف‌اند وجوه بلیت پروازهای تعلیق‌شده را در اسرع وقت و به‌طور کامل، بدون کسر جریمه، به مسافران بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149371" target="_blank">📅 17:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4Pn2pkxRgoofj-NH48l1odG5e6XmpqhDD7uIJtu6YjGySqdFtIFvmLiZQ0Le48dRyD9BoicB3oCr8S1ntV3jU1Hojd-Wq2t3LFFmV0wmgZ5iRovMITomm4MCJh-zS7T5E_xSn-rJvW8AynxUhNRLl2DmVWLUT0qmKQbK0-vtkQ_1migTGFDG98scOr0AQ0m-o6cI11-C6kPmvuunxP4wyhmQLESuuM1mKpTUOZuEkQT8rZNV4z2d24K25jcBuR6imBJGskv8T2dKJXIsc9IqkuC7lHlXXj6hqDvBldtmkza3usrjtGBpsyrTGtBAKIWnrggsHkkzeFd-6nRqP5eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلبری جانفدایان خانم با موتور و کلاشنیکف
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149370" target="_blank">📅 17:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBkQ7fKjR-0cEWAYSHMlFbTfGaTFJbTVhjnk4leDzYkN2AmHZUj70Mg8WmJ5JsNCSpTTro0xs-ed8q-KsKf2udqbYizUeM9EvgnKyztlJHerT7d1iYO6NLY5-VtBW1nzOuXVQ1NvC5LRFvWTvUVLEr3HtAC8dZ6ivBWpqTUAiueFW0yu0UUR7KEVZAB9DKhKyjj_IS2Bk6UnIZ4MuH23PqnAzbD6X0iRIVbYMWBPEOmR0LI1oF_JTvyWQX-ilEfCskYFogHizkUqGVvvpbLg2u6TbspIx_zumbkhNad-WyKpYnBXmSblm2Gvf4_WRsf1IG9dI2JJcE5Ik84x3XucLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا پزشکیان به دلیل تحریم هوایی تو آمریکا گیر افتاده و حالا حالاها نمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/149369" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149368">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پزشکیات در گفتگو با فاکس‌نیوز:
ما اصلاً کاری به انتخابات آمریکا نداریم.
🔴
اگر آمریکا برای گفت‌وگو بیاید و حق و حقوق ما را در چارچوب قوانین بین‌المللی به رسمیت بشناسد، آماده گفت‌وگو هستیم.
🔴
اگر نخواهد این حقوق را ببیند، چه قبل از انتخابات باشد و چه بعد از آن، برای ما چه فرقی می‌کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149368" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سفیر آمریکا در چین: طرف چینی در مذاکرات روز پنجشنبه تأیید کرد که از ایران حمایت نمی‌کند/پکن با ما موافق است که ایران نمی‌تواند سلاح هسته‌ای داشته باشد و تنگه هرمز باید باز بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149367" target="_blank">📅 17:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
در گفتگو با فاکس‌نیوز؛ پزشکیان درباره جزییات جلسه هیئت ایرانی با کوشنر و ویتکاف:
🔴
آنچه درباره‌اش بحث می‌کنیم، چارچوب قوانین بین‌المللی و حق و حقوقی است که باید داشته باشیم.
🔴
ما چیزی غیر از حق و حقوق خود در چارچوب قوانین بین‌المللی نخواسته‌ایم و نخواهیم خواست.
🔴
در نتیجه، بر همین اساس در حال تفاهم هستیم، اگر طرف مقابل بپذیرد.
🔴
پزشکیان درمورد منشأ اصلی نقض تفاهم‌نامه: مشکل این است که وقتی کسانی که یک عمر مسئول آن تنگه [هرمز] بوده‌اند، نتوانند کشتی خودشان را از آن منطقه عبور بدهند، طبیعتاً برای کشتی‌های دیگر هم حق عبوری نخواهد بود.
🔴
الان آمریکا نمی‌گذارد کشتی خودمان را از آنجا عبور بدهیم. به چه دلیل آمریکا آمده آنجا و اجازه نمی‌دهد؟ مگر کشتیرانی آزاد نیست؟ چرا راه ما را بسته است؟
🔴
پزشکیان در گفت‌وگو با فاکس‌نیوز:
مشکلی که در منطقه وجود دارد، نوعی عدم هماهنگی میان آمریکا و کسانی است که در منطقه و در ایران باید در چارچوب آن تفاهم‌نامه با هم کار کنند.
🔴
در اجرای آنچه در تفاهم‌نامه نوشته شده، سوءتفاهم‌هایی به وجود آمد. این سوءتفاهم‌ها، به جای اینکه پای میز مذاکره حل شود، به درگیری کشیده شد و همین، کل تفاهم‌نامه را زیر سؤال برد. اگر بخواهیم بر اساس تفاهم‌نامه عمل کنیم، طبعاً ممکن است در طول مسیر مشکلاتی هم وجود داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/149366" target="_blank">📅 17:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=n8J3SSbR6ERwh4il-Bsyud-rdRxhyiTOPnSMjRJjIn7h9YuROUutkxMERMRyPXCE5e9ApqyyRW83WWUKi0NeJ8Ay4mRbpKs9bqVMfl8zvEyBmeT-x-YewGeQX4B5-JY4ehf2J8QkNgcvBDWUeuHTTvfrYKZpM220MtGohW-rDpoENFY_0ANF0kuQNr7u73nvNsLpYljyR5hHg4y93_PIQc15X0tP4rDa1pL9WjFlpNrzmuhWE_OMnLg0KrPNB2aKKcfhp09Wf5LcLDsK5_w0Qg6IWARnF2b0DGAwWgxOK4G9XNNMq6WMn_DiDzalLj9uUbGLJlAzzTeZRkLq_IBO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=n8J3SSbR6ERwh4il-Bsyud-rdRxhyiTOPnSMjRJjIn7h9YuROUutkxMERMRyPXCE5e9ApqyyRW83WWUKi0NeJ8Ay4mRbpKs9bqVMfl8zvEyBmeT-x-YewGeQX4B5-JY4ehf2J8QkNgcvBDWUeuHTTvfrYKZpM220MtGohW-rDpoENFY_0ANF0kuQNr7u73nvNsLpYljyR5hHg4y93_PIQc15X0tP4rDa1pL9WjFlpNrzmuhWE_OMnLg0KrPNB2aKKcfhp09Wf5LcLDsK5_w0Qg6IWARnF2b0DGAwWgxOK4G9XNNMq6WMn_DiDzalLj9uUbGLJlAzzTeZRkLq_IBO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشتی باری-مسافری Blue Car Carrier II با پرچم یونان در شمال جزیره میکونوس دچار آتش‌سوزی شد
🔴
این کشتی ۲۹ سرنشین و نزدیک به ۲۰۰ کامیون و خودرو داشت
🔴
بر اساس گزارش‌ها، مصدومی گزارش نشده و مسافران در حال انتقال به جزیره تینوس هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149365" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فایننشال تایمز: حوثی‌های یمن به اتحادیه اروپا اعلام کرده‌اند که کشتی‌های اروپایی در دریای سرخ را هدف قرار نخواهند داد و گفته‌اند عملیات آنها علیه عربستان سعودی است، نه برای مختل کردن کشتیرانی بین‌المللی
🔴
حوثی‌ها همچنین پس از مذاکرات با واشنگتن با میانجی‌گری عمان، به آمریکا اطمینان داده‌اند که کشتی‌های آمریکایی را نیز هدف قرار نخواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149364" target="_blank">📅 16:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e6ed712f.mp4?token=rezjJmdGSPUyOu2sFG905Yle_oKRZ2uBZMbbjNajQmKViU5ZrmYSoikFefk8NfJqoXlXBh-Dluj-r115i0rHNeBVYYgD2w4RSu03siyXgjbyHlk8p2zkRjyyjd5Qxctt-PmhiZeyfwOMqSZMgVAsEwmLy5WYMFVxeOf0DTdHdIoJnpwSSs1jyYfL2HtkrrL-66XVpv3sznIgMnNLMIWu2D4hYYlYgysW_SUKYdCvo-_TWQ4g5ETXofz8QB7282WVh7p7bOg0bLlKG0V_EYar5EoBw3cWmkZKIPk0Q0sH7dOiUwBM0aHVqwKFs7eAIpyjgvi-j0FJpHTvlHhV1UswtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e6ed712f.mp4?token=rezjJmdGSPUyOu2sFG905Yle_oKRZ2uBZMbbjNajQmKViU5ZrmYSoikFefk8NfJqoXlXBh-Dluj-r115i0rHNeBVYYgD2w4RSu03siyXgjbyHlk8p2zkRjyyjd5Qxctt-PmhiZeyfwOMqSZMgVAsEwmLy5WYMFVxeOf0DTdHdIoJnpwSSs1jyYfL2HtkrrL-66XVpv3sznIgMnNLMIWu2D4hYYlYgysW_SUKYdCvo-_TWQ4g5ETXofz8QB7282WVh7p7bOg0bLlKG0V_EYar5EoBw3cWmkZKIPk0Q0sH7dOiUwBM0aHVqwKFs7eAIpyjgvi-j0FJpHTvlHhV1UswtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی طائب: «حضرت موسی ساخت بی‌سیم را به یهودیان یاد داد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149363" target="_blank">📅 16:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utl5GrxIQCfr4wGje5fvnxgt4ylVbaU-eM8ja6Geu79oTgi_iYbO4gfsvdSYjTCbf_01bXrqhcimoDeFVIjrsUw9LLrfw9UZWrq2oVCOUfBEszFuzMAuKbA7V4PdIzKJOjk8URzP34lgJ8OT3t4zw4x9OydtrX5yJYxU5Fqf8nANom-PyDVhv3Li__EcXt-EosdnvFFXAImgGCPJiMPr0zkNyJRagSmcAvJaMdkSSgegDxOepnb3SBMmf5WPuwkwDyeiZNtcNV2sOQViqEFKD-jJWNptljuPB5XI9g-h8TzPY-Yd63j5IWs31MFYvS2MmTwnpfmz0tNLF8tmWcpPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی:
یه خبر خوب.حکومت شرور جمهوری اسلامی سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/149362" target="_blank">📅 16:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رئیس جمهور ترکیه، اردوغان:درست نیست که به پیمان دفاع مشترک که در مکه منعقد شد، به عنوان یک ائتلاف تأسیس‌شده علیه ایران، اسرائیل یا هر کشور ثالث دیگری نگاه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149361" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⛔️
پیش بینی دقیق طلا و دلار توسط نابغه دانشگاه شریف
😳
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149360" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
الجزیره: عاصم منیر به‌زودی برای نشست با همتایان سعودی و ترکیه‌ای خود وارد عربستان می‌شود
🔴
انتظار می‌رود فیلد مارشال عاصم منیر، رئیس ستاد نیروهای دفاعی پاکستان، به‌زودی وارد ریاض شود تا در نشست پیش‌تر اعلام‌شده با همتایان سعودی و ترکیه‌ای خود شرکت کند.
🔴
این نشست در چارچوب توافق دفاعی مشترک مکه برگزار می‌شود
🔴
الجزیره از روابط عمومی نیروهای مسلح پاکستان، نهاد رسانه‌ای ارتش این کشور، درباره اینکه آیا منیر سفر خود به ریاض را آغاز کرده است یا خیر، سؤال کرد اما پاسخی دریافت نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149359" target="_blank">📅 16:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الجزیره: ایران اعلام کرده طرحی به آمریکا پیشنهاد داده که بر اساس اون، تنگه هرمز ظرف ۷ روز دوباره باز بشه. این پیام‌ها در حاشیه مجمع عمومی سازمان ملل در نیویورک و با میانجیگری قطر بین تهران و واشنگتن ردوبدل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149358" target="_blank">📅 16:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3W93jMgzE54oTHQ_jniI5DxBaI99YHKueKRcV77grOy2Wlw6FX3_142DYhkXVe7mWneEyis6-b_c1J-G6t66HANNtBM10qgSRAYyMsmg_QUficxlteipqHwATTqoqdB9ljMfm8Broz9xtELovHtOcw3J1RtEJ_s5n0WA0EKCL_LmQQ6RXMgZkhDbGv4UcdBu5SNyaGwlKChrS_wFA_pI5qq_bah_ha0MmFdAJWO1WKsdh91dbVVXC_n5ykCQjXIxBYuM9cnqBlMVTfstaOIHk75l4mPdbcUYF_Apem8vuq-JnmzIqhJzvXaQp6FuFk2BTLuCNimL-BKF4ZNb9JA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : جلسه بسیار سازنده‌ای با رئیس‌جمهور شی جین‌پینگ، هم برای ایالات متحده و هم برای چین داشتیم. اتفاقات فوق‌العاده‌ای در راه است.
🔴
او، مانند تقریباً همه، به نظر می‌رسید که نام "هوش مصنوعی" را که نامی نامناسب و نادرست است، به نامی دقیق‌تر و مهم‌تر، یعنی "هوش فوق‌العاده" تغییر می‌دهد. همه دیشب نیز با این موضوع موافق بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149357" target="_blank">📅 16:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / ترامپ خطاب به رئیس‌جمهور چین: هرگونه حمایت از تهران کاملا غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149356" target="_blank">📅 16:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1707c895.mp4?token=mqya2njgaLz28Gv5V0b09Ij2ZEC_qe7CHYpEGSHnI2lgi9f6Tu9QOJi6k0V1hA1Xr3kzlUh4dCjR0GFP0AdGheOwNlZ5yWvWwBEuKSRtpTmBkKnlOSNiIdAmt8o33m1qlHz-4M1qGT8DdQ65wENG6QnAJnO-JeiOTHJamWMZWGJqtLPxT7U2zYSVf_5M948kon22nuWOz5yhEdKu9nlUz4J66qL3K5q9jahCOm6pEQRSFpMhzG2UxzaPZGizw3dP3Qn8f3ljeC-1tG5ugkgboej3OY50JtEIfYMpBuZGL-GmmqTHiZG5oo0HePj2zTaEI5fZjdvcVo7ynQEhUj6big" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1707c895.mp4?token=mqya2njgaLz28Gv5V0b09Ij2ZEC_qe7CHYpEGSHnI2lgi9f6Tu9QOJi6k0V1hA1Xr3kzlUh4dCjR0GFP0AdGheOwNlZ5yWvWwBEuKSRtpTmBkKnlOSNiIdAmt8o33m1qlHz-4M1qGT8DdQ65wENG6QnAJnO-JeiOTHJamWMZWGJqtLPxT7U2zYSVf_5M948kon22nuWOz5yhEdKu9nlUz4J66qL3K5q9jahCOm6pEQRSFpMhzG2UxzaPZGizw3dP3Qn8f3ljeC-1tG5ugkgboej3OY50JtEIfYMpBuZGL-GmmqTHiZG5oo0HePj2zTaEI5fZjdvcVo7ynQEhUj6big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاظم جلالی، سفیر ایران در روسیه:
به نظر می‌رسد که دولت ترامپ، با وجود مواضع و اظهارات رسانه‌ای که مدعی پیروزی و موفقیت است، به طور کامل درک می‌کند که ملت ایران استوار ایستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/149355" target="_blank">📅 16:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IchkzoKS9bpaqFn3n28MRhfnexiZsYTJtvHRyA1aGN0FH7nSJhj3xezeim9b4J3IOQjeNFKOw74jJRzzRhsoBYJiH_of8MaOVL0KgKrP-wvg3KRpL2Dizzq8VHBClIfXeaFqRn6StSgQROimaczWtnyKqv9eO3P7Bxc5r7TsIgVyh--ZQyuHZx5oWXchIEw1I-sSjS43PZSwA0jX5zLxUxFBIb-34dno3q544y0gJMFb-hT9H29Jk6nmaxb7lSPZFC9e1N7750BNKgJM9jo1gVZ5pJtC69hwXm8SJshJ_Cl8qYDx-mLWI4jibBLA5cdYbgagvzzF8bWQTSTtZPjkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب خبرگزاری فارس که میگه شکاف در داخل باعث میشه ما شکست خورده به نظر برسیم و دلیل این شکاف، اصلاح‌طلبا بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149354" target="_blank">📅 16:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اکونومیست: چین در حال بهره‌گیری از تجربه جنگی روسیه است
🔴
اکونومیست در گزارشی نوشته است که چین برای جبران کمبود تجربه رزمی خود، به‌دنبال استفاده از درس‌ها، داده‌ها و فناوری‌هایی است که روسیه در جنگ اوکراین به دست آورده است.
🔴
به نوشته این نشریه، چنین همکاری‌هایی می‌تواند در سناریوی درگیری احتمالی بر سر تایوان برای ارتش چین اهمیت پیدا کند؛ از آموزش نبرد پهپادی و شهری گرفته تا همکاری در حوزه پدافند، موشکی و فناوری‌های زیردریایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149353" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: آمریکا و ایران در حال بررسی توافق مرحله‌ای برای پایان وضعیت جنگی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149352" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmbaY8aL4YHaWYJyJ17waASuVQCloNK4hQtKzhKY4EoTi5uRwnFJVRbHgkVyKy-WYWFUYvO2XSnwloYcTq_ZmV9P9Ve_tuDlYcznK3cORwJKrC3hg7QNSQ14shCUd95k-RtN9JbqsW74kYIDRrqgMHhsVv8x5r2QNX5qk4zj89yt2Yc-cXAae4NgLlxXxYnhMKFqAoy94yUV_DhQPAG9IHburpE1JPNpZsGHZrtwBty_qIgcTWXqejh8xr3j55dx7GotJzaqLpxfUOxVWbV-COeL5dU_RliiCcLWbfEvQxNN0RSgoQ-_ej3lsC0ZzygOEgiTIqNH_5bvGf2MgOqpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند لحظه پیش، دو حمله هوایی اسرائیل به حومه شهر زوتار الشرقیه در جنوب لبنان انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/149351" target="_blank">📅 15:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149348">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6QqDkqGyb_Z6Mj7geRBNY6PmrPpy9wLSSusLUZ00mYhDFQEI5UGD4ykLYMmTGf4ckxyQKBMykyI4W4hFrqHh310kpCUUz7yX2SUnW-2JYP_mZws2ECmohoNoDlKlTyRcNryDny83hy4HYzY5juAiiWr3Awi1JGwHlgCUvpNhj62atfHIQuTsugQOHljnL3l53pRI6nKVgvvjXChqd54QHdnr7DCz77GngOnxwTdP40suz6STzxLi2RpCQlsJfE19fWGt_PIRinpMeUsClJSnRTCx4ONhKVJ9sop3bSkl30prrBN6fC6kckI3nHJt5LCsw-j8WxBvJaQlgsgM7tF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7DHfxnxAXdZ-rSDgn0JAy0moSS7lKIJw7-w0R25Y7HqonepjopucgdOe4MPHyD1aHRiSKDRTIVT0lXkRLjl-7BNRPrJrWpY_BCIwgiCR3gz_3pKqGl-lKFhnI_Q-SJedHHYBiVXCLU7kz0u8vw-IVejfqEeFkrFnD7byzn-mb1WXfdiANYwEIeGHQnyAXAgv6SdKafNLO4E80dS9H5q8oF7esS_EXkUANiLPZNjM8rEhsqJ91fGu0k-E3Xi3ABARv-U4mTWjzYxYaOlDIVkE2xvBrr-PrTckEBW42qLzkLlzVbiBOZ02hazLMJu1lNb0P_h34fhL-FfB2qn4WkLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pG7yNsx7VsrU80AWwn3-h5hFrs-sdtzuNXXF0ZtN-iBKTmtUmRA_CIcq8UaQ_aqyErkNeiYWXnK7_f2tDh-g9Yfv4JLi6pYAAZj65nllkTUYub4BDq5ErpThDHq71cmjV_QWKh8T93_H9abwzDyUqIGnstl7sjN0_0FnabzJHTiNcdWQAZK-a7xR8YD5qaRonSmWAz305yBIjnR2Kp7aqquVBfiyZmj8Iw4qmW2F8dFp8FDksiHNrnfZDJB79EHsMfAsxNkX1tsC0zEjvvq2BltIpka0SJmQAyp5H2DBwEhyw7kjEcI6SdUaqIhA-DXTYIy1rbXAEpF6N7gk3AmYnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هنوز پروازهای متعددی از تهران به ترکیه، چین، پاکستان، تایلند و روسیه انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149348" target="_blank">📅 15:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149347">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
داده‌های پایش شبکه، امروز از اختلال و افت کیفیت در چند مسیر ارتباطی اینترنت ایران خبر می‌دهد
🔴
هم‌زمان، اختلال اینترنت در استان‌های مازندران و مرکزی نیز در سامانه پایش مستقل آی‌اودی‌ای ثبت و تأیید شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149347" target="_blank">📅 15:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149346">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmjdxHGj6V1hNGWJ5pi51agCeRQg9oglkoDypT5-sVsosuUw6zn-aBcZ-ncbNsHt9idZ-Bfn_x2JGdl1beV5xmCfj-UI6mVnJngK1yavxeeCoPt6SLUJyE8yn7e3AhcOYDkB_eZ3MW5jJKOWmxhDVXURZ2TdA5ysjinwxPIoZwxOWtul-rAOJkpKYZip2CxK9FnvLC6NHmnlboG1vsW_n75-MGyRPTEGm3fMbK2XjdLJgsZsjTehq4tq7q8j74pkgUIcKyzNACED98253UY1rR9p_YflQb6PQIoHDPVbuW_oQp2L6JCCPe5ZwL7WyCSRW8Tmm2eJSqcWkqEm-kbW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باریکلا قندلی
ترکوندی قندلی
@AloSport</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149346" target="_blank">📅 15:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149345">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📌
دلار امریکا در تایم فریم روزانه و هفتگی کاملا ساختار صعودی دارد
🕯
🔔
بعد از شکست سقف کانال صعودی در صورت تثبیت میتواند تا ۲۹۰ هزار تومن صعود کند !</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149345" target="_blank">📅 15:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149344">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzKOrof3yyJb9c7QvfBz-8X-XeCStyDzncRQsRDNePiou8NGB6T6_3-oFyKGZGEeFakREN4TQT5P5Okq40j5ul_wr41FTXz4dXu3aQUqo7d36wj0w_SvxucRuea1Pi4qYTXaGKNZiaPu4pMbA1CoR9wmVwAb28s94G9K8uhR49k2RlbVqUBr-jQ9Jkz_VkRaWUXzFUB_J-wEz8F3gft_jwpjpcYX16tFvicpqCtEncxL7Ej6qf20bSc1gwobBcGiFg28fcgOqzxnDDf9qhoC54y52750E2h3jqv5IX11raSeRjMUB1Q81fpqQHCQGR8sjydJO5AXjWOxzoCN4A6nxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد که یک موشک رهگیری را به سمت یک "هدف هوایی مشکوک" شلیک کرده است که در آسمان جنوب لبنان شناسایی شده بود، منطقه‌ای که نیروهای اسرائیلی در آن حضور دارند.
🔴
نیروی نظامی در حال بررسی این حادثه است. هیچ آژیر خطر در شمال اسرائیل به صدا در نیامد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149344" target="_blank">📅 15:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149343">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان: براساس ارزیابی‌های اطلاعاتی آمریکا ارائه تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به ایران کمک کرده تا کشتی‌ها را در تنگه هرمز تهدید کند و حملات دقیق‌تری را علیه پایگاه‌های آمریکا در خاورمیانه انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149343" target="_blank">📅 15:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149342">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac39b5acea.mp4?token=htn1gXSfVu5eTcCdShGCnAzyXExIxBU4a-iPF8OD7bt0ORHAZnDU4vL60tTW-j0qex0nKFjyfs_qkBvnwQvBpW6_IfJ9pGj3O-Y54LB4EUK9xZIqaHhOmyMElFHoTPWqJdHoyu5a-K2S_vbmriyLguKroSN8rIahLhkrCAR6xmxc0o21p6FN2_FrPKByYbw95Te0Jcp0Pw2q7huS1gwvo3dCqaeRDF-hO6k6izAyF9v35Bbfyyh9wd-lkNNISOeX_v9SPdd3NoXLjUv5TD95JNjlpEPr0GSMCXkYi5kVrWwjeVONz-KcBcuxRu7lXGfHUYmQt7cicOMCNPhc-BmHVWyFLuVTlQzO7kdtGvUnEEKEJ6ThT7PF_jrse9urDzTfveQeZLO8LpRLSodoOHUs87vKcvIQpd9n06q6HIZQEQbhQDdMSbhLtPj6VCTcQGtnLaHvAlybW1Jkyqjv66NcD72m30Swy3VguQAEWDocAcGGnRAiulZikKrAuQCXbYzoqOKt0KGaFLJjeyGx3d2ziXPU-oWhQMw1kIqFvEdyAzs2WfJ_5Qn6-e2BM-ZbmU2lSadV10G1_ei4DPPA88KUZVehAXCG1OUPSf0KNfVn_aXFPm1cyr9CQCNoZUggYOecSwwVa8VnJCcIIisooPhCJlW59eYCPUtsgjK_npHi5Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac39b5acea.mp4?token=htn1gXSfVu5eTcCdShGCnAzyXExIxBU4a-iPF8OD7bt0ORHAZnDU4vL60tTW-j0qex0nKFjyfs_qkBvnwQvBpW6_IfJ9pGj3O-Y54LB4EUK9xZIqaHhOmyMElFHoTPWqJdHoyu5a-K2S_vbmriyLguKroSN8rIahLhkrCAR6xmxc0o21p6FN2_FrPKByYbw95Te0Jcp0Pw2q7huS1gwvo3dCqaeRDF-hO6k6izAyF9v35Bbfyyh9wd-lkNNISOeX_v9SPdd3NoXLjUv5TD95JNjlpEPr0GSMCXkYi5kVrWwjeVONz-KcBcuxRu7lXGfHUYmQt7cicOMCNPhc-BmHVWyFLuVTlQzO7kdtGvUnEEKEJ6ThT7PF_jrse9urDzTfveQeZLO8LpRLSodoOHUs87vKcvIQpd9n06q6HIZQEQbhQDdMSbhLtPj6VCTcQGtnLaHvAlybW1Jkyqjv66NcD72m30Swy3VguQAEWDocAcGGnRAiulZikKrAuQCXbYzoqOKt0KGaFLJjeyGx3d2ziXPU-oWhQMw1kIqFvEdyAzs2WfJ_5Qn6-e2BM-ZbmU2lSadV10G1_ei4DPPA88KUZVehAXCG1OUPSf0KNfVn_aXFPm1cyr9CQCNoZUggYOecSwwVa8VnJCcIIisooPhCJlW59eYCPUtsgjK_npHi5Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرهنگ زشت آمریکا بجای خمس دادن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149342" target="_blank">📅 15:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149341">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
چقدر گفتیم از عراقیای جاکش برادر در نمیاد؟ عراق حریم هواییش رو ایران رو بسته
🔴
حالا باز بمالاش بیان بمالن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149341" target="_blank">📅 15:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149340">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس شرکت آرامکو: شرایط فعلی انرژی وخیم است و در بدترین وضعیت قرار دارد.
🔴
وضعیت انرژی وخیم‌تر هم خواهد شد زیرا اختلال بسیار گسترده است و تنها به یک منطقه محدود نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149340" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149339">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/capt3FgS4o5_jNKT302uTSFsErDXnYbsLSHsxeLEVv-9u4sHKZNwFIoWOUupt8eOTHPuzUkWPMfxSRhYu_D8g7_QFK2BCsQ7NJkQ82L15wwYcDmjgQZWjPjYVCiA-NNpvuk8Z1Q3l_1vQaXHksW0oXes_3_1ua8Xu90vvUHmyepU2dU9_cWWG5l6xR8QYUX8UXRaeWp6usfS_QZJOym24gPDdklfcvXh6jymmV0Y-WU0XTi4U4BXdbteF-1Ah94_nJa_GIMs_bhd3tNKRNDk985wmkdbXf-6ECeVn39N_8EG4eBguLRlTuXScdCD8-webtqIRaAGYqgXJfAa2qI4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مخبر: پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149339" target="_blank">📅 14:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149338">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
امام جمعه قم : برخورد قاطع قانونی و امنیتی با بی حجاب ها ضرورت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149338" target="_blank">📅 14:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149337">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAbjwWkmBGZVRd-Fpfhpk7ef87PJjgmkPCH_JL4TqUOsFPfAEY26vIaeMqme1LEe8A0AhXpbqo2QUniB0iZvzYwHlZXDfDpnzjyTTswxm_6jmwU_2Q-tXZRIXblKypWi2JeM8pt2hCdeq8KUIr-mLYNWY1ofroFHu9trydboZQt70lOLYwwJo6KGoQ4qq0yAcDGOb_U0DY4_aWoWoRrM57OOW3bUf8zz-RbDbNYl6AYkzX162jHQmf18zYG88yar47VK_xDnhMKQO_vLVLNVtxMkYsu_F0HV2mgqCb364lsd5n2S2m4A78K6gKsBpW9RwKkc0cqHFi6hXLFkWOeBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال شدن سامان پدافند هوایی در منطقه انگشت جلیل در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149337" target="_blank">📅 14:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149336">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88ddfa546.mp4?token=lJx9NcZO7ULWoQE-B6h9fryJNXG2cFs9JiG2V9ds2hrgBdtMi7uWWh49bhPVVmHl5d5t-hsM5WFKhT3k5R_OeW1U_zh5VxsIVBSgRr_Je3-BWz5FRIbp5dnQN2uTGe8Xyip8IT1cT14Nlvq8WnrPb0WPBDFQTf-cBuBMeF0mpRXNblyLBE4TgVSBI11Obw-KL2OzVpSDTZl5e1w6klRpCFCIKbrIpG6O1eSZ9T08cn5Uwp9tWGE_XgR1HwrEWp6PWpQNi7IxHpJzymKqd0y8vEHSJ5dKgWxKZ9By4olMyqJWxnmUo-oKnAaPClMCgHuy4rR9FDOo5j3DgolHXIumrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88ddfa546.mp4?token=lJx9NcZO7ULWoQE-B6h9fryJNXG2cFs9JiG2V9ds2hrgBdtMi7uWWh49bhPVVmHl5d5t-hsM5WFKhT3k5R_OeW1U_zh5VxsIVBSgRr_Je3-BWz5FRIbp5dnQN2uTGe8Xyip8IT1cT14Nlvq8WnrPb0WPBDFQTf-cBuBMeF0mpRXNblyLBE4TgVSBI11Obw-KL2OzVpSDTZl5e1w6klRpCFCIKbrIpG6O1eSZ9T08cn5Uwp9tWGE_XgR1HwrEWp6PWpQNi7IxHpJzymKqd0y8vEHSJ5dKgWxKZ9By4olMyqJWxnmUo-oKnAaPClMCgHuy4rR9FDOo5j3DgolHXIumrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما : وقت حمله به فرودگاه‌ها‌ی منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149336" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149335">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX6RJaCEY9NlvoWxeLGtlPbvhbflBppyHMA5VRU9McwhAeQxYzInIBqQ-P0VJHs_P38tPjS4MYR-ncQWYdW4CNI6fywB-isZrnGiF7EPiw9Om7TD2O0lViTmlwXlqLXsWuQgLCFnNNgWPaFB0dP6VOe27C1qpBNzjD8imv9KsRXuvHg5XhUmQ9NPeJzjjuT2DeNDapG-u6zXkUtnGm9w9lLnT9gKRlG9XlK2i-5bUS2bTam26uF3-dHo5mfrMcTMkUJgjDCU4IbpoYMzO9NUVucBmeLKP90xkNTXv72iMKZeALtKVopYFpcBMvi6qyHN_k3TyTIpX8Et_v6YDZzycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا استاد گودرزی رو مجدد سوار ماشین کردن و بردن جلوی خونش پیاده کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149335" target="_blank">📅 14:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149334">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149334" target="_blank">📅 14:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70490f2ce8.mp4?token=Wnd13wlLEfBFgOHrlUs7_8rrilHvFJqudrbkNapyP5ZlcJcIZ66vcFgyoL4_DrzZWY52XcF0OL8e6oZKPgMCvkZbfm2d-5A1R60WzBTAnxxpDvPYfgSLOXIHsyJ_pxcH81hS8sUANgU9L8MBCLaLUvbCGwzkablKJKpkSh90_V9Onrn0rJnado7G9eVgAJHJLtw6eRW-t9JdIt8XC7e-d_Nntqcvqvm2hwbfYF975z7bnNqSDIL0grX_Ewf6wmolVdGbNsTOwjMm7KmZCnC0Y9-u3aGntTDPXoppBeKMyQCIeFK10avK4gF89wKtA_rBJxMVTSK5d23PHl93iuxghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70490f2ce8.mp4?token=Wnd13wlLEfBFgOHrlUs7_8rrilHvFJqudrbkNapyP5ZlcJcIZ66vcFgyoL4_DrzZWY52XcF0OL8e6oZKPgMCvkZbfm2d-5A1R60WzBTAnxxpDvPYfgSLOXIHsyJ_pxcH81hS8sUANgU9L8MBCLaLUvbCGwzkablKJKpkSh90_V9Onrn0rJnado7G9eVgAJHJLtw6eRW-t9JdIt8XC7e-d_Nntqcvqvm2hwbfYF975z7bnNqSDIL0grX_Ewf6wmolVdGbNsTOwjMm7KmZCnC0Y9-u3aGntTDPXoppBeKMyQCIeFK10avK4gF89wKtA_rBJxMVTSK5d23PHl93iuxghjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل خواستار بررسی اخراج اسرائیل از سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149333" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیروهای امنیتی پاکستان، تلاش گروه طالبان افغانستان برای نفوذ به منطقه مرزی گلستان را روز جمعه دفع کردند و چندین تن از نیروهای طالبان را به هلاکت رساندند. این خبر را خبرگزاری رویترز گزارش داد.
🔴
منابع امنیتی پاکستان اعلام کردند که درگیری‌های پراکنده همچنان ادامه دارد و نیروها در حالت آماده‌باش کامل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149332" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVJ5YTcGcULrjCnp_YtadW3ZVgO4eJpWDUZNrWInFgrIWt9mtPzT1HJSlB1woRwsMaUn-eUrqMoC_2hSA201jCOTOQyd-zyXV8CZWpIJX4X4kvpEb_NJBV4ItIC7d5IyEYUOnijRV-SY6WlLF7BC_QS7RNL70ZBIL3KpMWRXcUmh6BdaBDENBOQRuZV04veM2scO3Ae5-uBHadXPlAcNGJNxnyxjephLXe4C1CikCwYuB9PSPFYwn01Ca2ukSHd8IAne-XGXj8rsr_aw5s0B4yc3B7sumj4uLpuQ4PTxZsiX4BMIzl95gptdN1x2xNtbCPszodXuXQJDflDltVoYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای دولتی ترکیه و پاکستان در ریاض فرود می‌آیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149331" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149330">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdkJQDAE5s4Jt8ucih0ZBLU0MOee7Fiv5kniItsDzfLYk0cQyIiWNy6IXao3rS30_4bkTbhIoLD29ud60_C_hUpPJNjUSjfP3ZTLTu6o_gZn2RnyN3qhS5tVqt_8EmwrcK3ua4MbV9g5RAn2wh67jtycdmjGoQRE1m36azV3dvvbxu5itusLpxUjpHjZOrGoLGi1tk8ovUQ-4apWJ7SuO6ZgVPDrPPD1dZFiwvJA76Z6SaUNyR1cyGr3irCb3osX068nNfvCGCZSNaIK_7ycNOxDkcJfWAxa6TftIqODJpk-2egpzo9UH27RFDLJLWG1CUkqXBExzJvc8iiijZ6jjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس اسبق فدراسیون بوکس ناطق نوری درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149330" target="_blank">📅 14:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149329">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=gCvAjWwYgG4fMznr_4bI7NCD50GNs0ciEo_KqNorWyFDxzpfjW_uf3ubPPUCs8lIt8ORTpobSwVAMR8MFZ8JuEMf-jZVcV_-5cTtZqWIttD_VyJAPRvVKg3CsZvXGKz0eq_nWCbDOfbPCNTiMsKpnZDMdjmaYj0hLmJ1k3oGvcWf0aMdXIJuuLFuCRM0rIb-wrfUI0fA1rxKY21XQhQZxVcAgiY4gbtq9TLU8TPCAdvvaO0IJ0sxzDN6dihfIiu35Etxoco4WR3G3da5sAnKvTOH6PDVBVbgjC7t8zpkMlByFA9JwpacgE2TO0XgaQBvJpu_zQfqQTdhJyewbDzyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=gCvAjWwYgG4fMznr_4bI7NCD50GNs0ciEo_KqNorWyFDxzpfjW_uf3ubPPUCs8lIt8ORTpobSwVAMR8MFZ8JuEMf-jZVcV_-5cTtZqWIttD_VyJAPRvVKg3CsZvXGKz0eq_nWCbDOfbPCNTiMsKpnZDMdjmaYj0hLmJ1k3oGvcWf0aMdXIJuuLFuCRM0rIb-wrfUI0fA1rxKY21XQhQZxVcAgiY4gbtq9TLU8TPCAdvvaO0IJ0sxzDN6dihfIiu35Etxoco4WR3G3da5sAnKvTOH6PDVBVbgjC7t8zpkMlByFA9JwpacgE2TO0XgaQBvJpu_zQfqQTdhJyewbDzyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج جدید افغانی‌هایی که از راه‌های سخت در حال ورود به خاک ایران هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149329" target="_blank">📅 13:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: میانجی‌هایی از جمله قطر در حال فشار آوردن برای برگزاری دور جدیدی از مذاکرات بین ایران و آمریکا در اوایل هفته آینده در عمان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149328" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: فرودگاه‌های اربیل و سلیمانیه در عراق، پروازها به ایران و از ایران را از امروز به حالت تعلیق درآوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149327" target="_blank">📅 13:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149326">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5891d8cd.mp4?token=LrFw9Hf8o9l4MYl8IZZ7HEuFt2m80wOIuA5ZB2Pj29_BoPfls-xoQc2pg24eTjYETSftuNkt-TsYL2VoyEP830YA6QscSkczP2FYduGJha9wi9bseHMsirr4K8aTlHnsP1tgImxq-iBmOamQAVrd_6anJz7B71ZPwEcJttUUdN2DqdP-y4QDaNiLMsNH1d8AB3EWw_ZlfbiUsIaO08ZxuMlrFf2mlVuqV2rvZJ7zDb2Ew8a-8xoKJ6pn05JzTu9ywPEWRFxqoxFdxWMT7ulZ6VqO7n5hcn4YQeeSKAaNhBPOfQ5g05TuGANO4zsDC1kjv4WhbR7k5isNwnCGDU87zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5891d8cd.mp4?token=LrFw9Hf8o9l4MYl8IZZ7HEuFt2m80wOIuA5ZB2Pj29_BoPfls-xoQc2pg24eTjYETSftuNkt-TsYL2VoyEP830YA6QscSkczP2FYduGJha9wi9bseHMsirr4K8aTlHnsP1tgImxq-iBmOamQAVrd_6anJz7B71ZPwEcJttUUdN2DqdP-y4QDaNiLMsNH1d8AB3EWw_ZlfbiUsIaO08ZxuMlrFf2mlVuqV2rvZJ7zDb2Ew8a-8xoKJ6pn05JzTu9ywPEWRFxqoxFdxWMT7ulZ6VqO7n5hcn4YQeeSKAaNhBPOfQ5g05TuGANO4zsDC1kjv4WhbR7k5isNwnCGDU87zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرین ارتش آلمان  توی خیابان های هامبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149326" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149325">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حذف ۵۰۰ میلیون دلار از ارز ترجیحی دارو؛ احتمال افزایش هزینه درمان
🔴
رئیس سازمان غذا و دارو از حذف ۵۰۰ میلیون دلار از منابع ارز ترجیحی دارو خبر داد.
🔴
به گفته او، کاهش این منابع می‌تواند هزینه تأمین و تولید دارو را افزایش داده و فشار بیشتری بر بیمه‌ها وارد کند؛ موضوعی که در صورت جبران نشدن، ممکن است سهم پرداختی بیماران و هزینه درمان خانوارها را افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149325" target="_blank">📅 13:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149324">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کرملین: پوتین و ترامپ درباره احتمال دیدار روسیه، آمریکا و اوکراین گفتگو کردند، اما هنوز جزئیات خاصی ارائه نشده است.
🔴
نشست سه جانبه آمریکا، روسیه و اوکراین به زودی برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149324" target="_blank">📅 13:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149323">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صادرات نفت ایران به چین از حدود ۱ تا ۱.۵ میلیون بشکه در روز پیش از جنگ، با کاهش ۹۲ تا ۹۵ درصدی، به حدود ۸۰ هزار بشکه در روز رسیده است.
🔴
بر اساس این گزارش، پکن بخشی از نیاز نفتی خود را با واردات از عراق، امارات، برزیل و کانادا جبران می‌کند؛ موضوعی که یکی از منابع مهم درآمد ارزی تهران را تحت فشار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149323" target="_blank">📅 13:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149322">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💥
💥
💥
اماده ادامه حرکت و رشد وحشتناک طلا باشید!!
💥
💥
💥
‼️
طلای گرمی 27 میلیون به زودی دیده خواهد شد !
‼️
⚠️
تحلیل ها نشان از این دارن که ساختار انس در یک فشردگی قرار گرفته و به زودی این رنج به بالا شکسته خواهد شد و طلای گرمی ۲۷ میلیون دور از انتظار نیست.  #طلا #تحلیل‌طلا</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149322" target="_blank">📅 13:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149321">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
به گزارش بلومبرگ، تایوان یک طرح اولیه برای راه‌اندازی مجدد یکی از نیروگاه‌های هسته‌ای متوقف‌شده خود را تأیید کرده است.
🔴
این تصمیم در چارچوب بازنگری سیاست‌های انرژی تایوان و تلاش برای تقویت امنیت تأمین برق و کاهش فشار بر شبکه انرژی این جزیره مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149321" target="_blank">📅 13:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149320">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حمله با چاقو به دو کارشناس اورژانس ۱۱۵ شیراز حین مأموریت
🔴
دو کارشناس اورژانس ۱۱۵ شیراز بامداد امروز، سوم مهرماه، حین انجام مأموریت از سوی همراهان یک بیمار با سلاح سرد مورد حمله قرار گرفتند
🔴
در جریان این حادثه، یکی از کارشناسان از ناحیه پهلو و سر و کارشناس دیگر از ناحیه قفسه سینه و دست دچار جراحت شدید شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149320" target="_blank">📅 13:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149319">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzmRcJ-yETmTe-EAsZonDLMLvux-p0TiuRMbw9RrNcf6xX74kzRMa7AkjsHSIJ45vOUi6NOgH27uBul2K2sZPExI79YDzF4Sr8XRNOQqbN9s3eT8kMo4xeEib5PXLJh5isazbSOGeWb6Y7vHONS8d4KF9z5BO9HCDVkTfRjjcJL276quTVH9CIELhQhU4r53Hi1fBQm9RNarHZuoXM5ZTGNLAjBiaKQwVzrXcUusrpmBsy8KwI-6O9F0wwD38sBmjkU-m2_n1UvGL2SDYVll4X1aKkIij_NGaPKbtOu9fJBnr93r97nNxj7uYNZ1l0KVF_McoaqHhNkEYke_GAT10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فهرست کشورهایی که نمایندگان آنها، هنگام سخنرانی نتانیاهو در سازمان ملل متحد، سالن را ترک کردند
✅
@AloNewd</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149319" target="_blank">📅 13:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149318">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی سپاه : در صورت خطای محاسباتی دشمن از تسلیحات جدیدی استفاده خواهیم کرد که تا کنون استفاده نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149318" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149317">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29702822d.mp4?token=fgD7JGq2r0Btq4Mb9TOtsSzl9dY94dfPKoHmTOBgB6o_S1l3B1a91RuRi0BSxOL73-OvnB_UumjHhLm-Ao2Ct9o-k4R30AYnGAERJJfFMzk6tTmDkz2gdZnDBs2s-ZnRgLBERfrKB6PPCGJGd9Zp2_GpoXxM9HscEeeDRsTXeAyiYklvlwM7HwMRt7o3a8yD1O-tQ-lWGocQAkNslCyASwpJoTvds0S_m9dYj1DqnlQECeUt-os4xZS2-IjoLIjzK_LyXv9ABNwoZd0sdwf2Yh6kB4aouW_kjuHfiYYlGRz5xgxU_cuFfXOuXet8Ee1H-2GE-hiC71bCdujai0ToTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29702822d.mp4?token=fgD7JGq2r0Btq4Mb9TOtsSzl9dY94dfPKoHmTOBgB6o_S1l3B1a91RuRi0BSxOL73-OvnB_UumjHhLm-Ao2Ct9o-k4R30AYnGAERJJfFMzk6tTmDkz2gdZnDBs2s-ZnRgLBERfrKB6PPCGJGd9Zp2_GpoXxM9HscEeeDRsTXeAyiYklvlwM7HwMRt7o3a8yD1O-tQ-lWGocQAkNslCyASwpJoTvds0S_m9dYj1DqnlQECeUt-os4xZS2-IjoLIjzK_LyXv9ABNwoZd0sdwf2Yh6kB4aouW_kjuHfiYYlGRz5xgxU_cuFfXOuXet8Ee1H-2GE-hiC71bCdujai0ToTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا: دستاوردهای رضا شاه رو نمیشه نادیده گرفت و مرد بزرگی بود
🔴
شما تو این نیم قرن چه کردید؟ فقط بنگاه دین باز کردید و ضد دین عمل کردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149317" target="_blank">📅 12:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149316">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین: «ترامپ در آخرین دیدارمان گفت: اوکراین مجوز تولید موشک‌های پاتریوت را دریافت خواهد کرد.»
✅
@AloNewd</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149316" target="_blank">📅 12:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149315">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOYTx_JShe__RtKm_wrdynJ-_o_yWAGNHxZtv59uG8yrqOl7Uw4EwrpZ3MUV3hcf_HCV0VbYJlfwIyikXGyCbsUsxbxl5QIavaEPU3oo3m_UEpII5OxIlg4Rcel4rOJ4PQjhV2e7YvV4BaR3D1uj5y7Jnn800lZRCMEpOA5rcNxmwrTmL6X0Lq1kkv-ZLZJ5JxGVDMtzfuUluViqAW1724Yv4GzVOwQH5ZYcmJILnKcgnp4CoNgfz33zJtowbzbHtutc6kWGZUFzH4D2G9Q7LUz_sGUTe5-fR0nYg3InCeaDjpmM8ErvDY6zfIIsvx7npupvs55Q3j3MlQZ-lwUkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی بعد باخت به ازبکستان: به امت مبعوث در خیابان قبطه میخورم کاش منم الان اونجا بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149315" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149314">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGFDjcdaMu-nip3LkJMwueSFDc5mU80M1viY-SPa_U3zqk96XknFWs9VCOUwmzwezzwu_MxtZPUm9tVL8sWxDUiu3z7wqGu2Iji3jCWtvQO8mfxp5H7qz9PSlxOTPbUDW3IOSXYrBQLNdsrYHD7wulQJHtBQU66xAmMpcCO2Uw_l0JFywdYG2_y-k3qqQr9UF-GRVzAmVum3kFswpzKwr-1RTmCxOXNGU_T7s_fpzJg5kBA7kuL9hZG4jwZfScXOzxcz0LK2e8f2JjdOxginntO1MSp1p0bOr4rOAz6kSmE0NLZ8ztc8ymJCAWCk4imYKb9Bk2-PrsYstc430p_Xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: چین پولمون رو نمیده
🔴
پ.ن: اونوقت امت معکوس میگن باید تا سانتی متر آخر تو باسن چین فرو بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149314" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149313">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اورشلیم پست به نقل از یک مسئول اسرائیلی: اطلاعات اسرائیل، تلاش ایران برای احیا و فعال‌سازی مجدد برنامه هسته‌ای خود در تاسیسات "کوه کلنگ" را رصد کرده است
🔴
اگر تهران از هر یک از "خطوط قرمز" عبور کند، ما مجدداً به هدف قرار دادن تاسیسات هسته‌ای و هر مکان مرتبط با آن خواهیم پرداخت، چه با مشارکت ایالات متحده و چه بدون آن."
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149313" target="_blank">📅 12:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
درگیری‌های شدیدی بین نیروهای مسلح حوثی و نیروهای وفادار به عربستان سعودی در مناطق کوهستانی کهبوب و جبهه الأغبره، بین استان‌های تعز و لحج، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149312" target="_blank">📅 12:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149311" target="_blank">📅 12:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149310">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMSpyFBW42e5jHmm-yJx5teBr0lw55-cgFF0EQR80crsUTxVTUmeqyGqVde-6SnNPe0FRcKKFaH36Lx7cU6C9Lr6vOqd3rt4ACILf91f-V8QVVwy-4pHvQzseApdxxmzRfj6KMGFCB7Tuj4FDlFNo7ecpjRK5z5f64OKO8mB-E_HKq9rFicBDo8wXrl5pvRLDqgRbyHTRVOpdEJBr9QlQuhh8S2kxEO4S1St4TH6Sao-vVZIvGvaOdebreWtcj9Cl7U7tP4D_1C-TSBLmotQBHNp31IWTT-shk_qTlxkgttHyxLPno4UYNjp5OY7_tVuVjAQZVdYR4-eTm0m6_iG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو اندونزی این مرد ۴۵ ساله بخاطر اینکه هر روز زن همسایشون بهش میگفت چرا ازدواج نمیکنی اونو با شلیک گلوله به قتل رسوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149310" target="_blank">📅 12:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149309">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=Qfy--nBMvkLeYiFyxxKiHbeTVeNZ1CSMgBWf4QVF8PuENB0wLB1l9E5pKUcUGRTDQDNyLsFNrGxKmyI3sroHzwntsKjV8xqOvp3giOXHBin4T4Q23BwSuQPnt2gj_o9xAthGOYTVp4wrdEoHuKIczgTecQOj0T82wqYQTp35GBOaOrUGIaw3osjjFjNy3S3BOT2ug1SHSwDSx8ogxJ5LChaNgOvO4vE9lk2ZHmT2HG6eJjU3m4XyuaatgNLFsXOkQfuzX2Gn5m0CEBfN9dphF2JXzi-26C3irxSANr1o4an8RCLWVVE9pCHjbnLM4hwX0hsSr5VgvgTXW7wXQKcC3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=Qfy--nBMvkLeYiFyxxKiHbeTVeNZ1CSMgBWf4QVF8PuENB0wLB1l9E5pKUcUGRTDQDNyLsFNrGxKmyI3sroHzwntsKjV8xqOvp3giOXHBin4T4Q23BwSuQPnt2gj_o9xAthGOYTVp4wrdEoHuKIczgTecQOj0T82wqYQTp35GBOaOrUGIaw3osjjFjNy3S3BOT2ug1SHSwDSx8ogxJ5LChaNgOvO4vE9lk2ZHmT2HG6eJjU3m4XyuaatgNLFsXOkQfuzX2Gn5m0CEBfN9dphF2JXzi-26C3irxSANr1o4an8RCLWVVE9pCHjbnLM4hwX0hsSr5VgvgTXW7wXQKcC3YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از دو برادر قهرمان کاراته پس از ورود به ایران
🔴
‏ مرتضی نعمتی: برای گرفتن معافیت، تظاهر به داشتن اختلالات روانی کردم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149309" target="_blank">📅 12:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149308">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
لبنان اعلام کرد که واشنگتن وعده داده است برای ایجاد یک منطقه آزمایشی جدید در کفر تِبنیت و علی‌الطاهر فشار دیپلماتیک وارد کند و از این طرح حمایت کند.
🔴
بر اساس این طرح، نیروهای اسرائیلی از این مناطق عقب‌نشینی خواهند کرد و پس از آن، ارتش لبنان وارد منطقه شده و در آن مستقر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149308" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149307">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2853b5ece7.mp4?token=vVaBHfIoMVkBco_Shwf3M9HXzBwHb21Kdmw6lq_xP3HaVQ1xK0aZw88MLtgFoxY8cVIZeYCUFEllvXlLHb6B-MDIDacF0Jl7b0dvh7slrOkB3iKLK33IO8x0hysoHdrv4A2oTkwH7LVheaX0lY9piuXrY75dlLEbksLqTEqdnq6YEIGJze0yPlzXZ-NselJ9BjZ_RWdTC6KyByD85kg06R46tbesreXMpbbxo3TnOVt-OWKoP-H0tWlmRAK6YiiZ65rlE5WK_CTXb-Q1QerTc3mot8l-ltB7Fl9qeEFx_VZgnO0tlOuqpZKzJrQXTau69AUAWArx0Lj36UrXFKHwXFZSTHSiA5GYOQTZCSjnsXBG9nxPHD0rpgbML7vpsCcQ3ZiDwz1dCtGH4JMa4X6VS9m4_oj0evuW83pU5MPR9h5KTRYm-rZhRdW7rYt1PL904InsYopclD_Yism_8U_PrVPX1Tn8OFlVodN2Vi6Rz3EOCVo0M60oYXd21Slc3X4KWuTVeBVw4C41pDxNJJ1FPK6cfDyTftG_aeluQm2Tl-Sco3q0KvAsJ-SeHVDE7nxfIMzj8PGqHxAL8rfU_6tBwE34LiNmztbbON-5b2DxLoG8Efkk1aDdv5MtQUKH7VKwtaR9OvNVdZZbnOzW3aMLVPCH80V-JMptuJNLQNOc3CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2853b5ece7.mp4?token=vVaBHfIoMVkBco_Shwf3M9HXzBwHb21Kdmw6lq_xP3HaVQ1xK0aZw88MLtgFoxY8cVIZeYCUFEllvXlLHb6B-MDIDacF0Jl7b0dvh7slrOkB3iKLK33IO8x0hysoHdrv4A2oTkwH7LVheaX0lY9piuXrY75dlLEbksLqTEqdnq6YEIGJze0yPlzXZ-NselJ9BjZ_RWdTC6KyByD85kg06R46tbesreXMpbbxo3TnOVt-OWKoP-H0tWlmRAK6YiiZ65rlE5WK_CTXb-Q1QerTc3mot8l-ltB7Fl9qeEFx_VZgnO0tlOuqpZKzJrQXTau69AUAWArx0Lj36UrXFKHwXFZSTHSiA5GYOQTZCSjnsXBG9nxPHD0rpgbML7vpsCcQ3ZiDwz1dCtGH4JMa4X6VS9m4_oj0evuW83pU5MPR9h5KTRYm-rZhRdW7rYt1PL904InsYopclD_Yism_8U_PrVPX1Tn8OFlVodN2Vi6Rz3EOCVo0M60oYXd21Slc3X4KWuTVeBVw4C41pDxNJJ1FPK6cfDyTftG_aeluQm2Tl-Sco3q0KvAsJ-SeHVDE7nxfIMzj8PGqHxAL8rfU_6tBwE34LiNmztbbON-5b2DxLoG8Efkk1aDdv5MtQUKH7VKwtaR9OvNVdZZbnOzW3aMLVPCH80V-JMptuJNLQNOc3CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
دیروز تو تهران 96امین سالگرد تاسیس پادساهی سعودی جشن گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149307" target="_blank">📅 12:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149306">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یحیی Fast سخنگوی نظامی حوثی‌ها: نیروهای یمنی هدف قرار دادن سایت‌های حساس متعلق به عربستان سعودی را آغاز کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149306" target="_blank">📅 11:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149305">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmk9ipSC_qKPWgz0XcQW6-xZYgL6tSEkKs4Om3sm136ghsNKwJFmAAXPrn2HDr5lqfuCxpbTYYFuexWxboEJGQIl-U0be6-TyqHuuhECQsPP-6IytQH-rQAPuv_2aTepaNcCAlVJ8eNnl2Lk8RnJWFKlxA-M46pVcFy7nTiB8QmHDqiMXKC_QCk80RSS6VOfwKZtcH5149pfkbqcsIJz6KQL5WAN2TBxu45D2ocp3YeBpxto5KPalEkiy04EW-ObnWCx3d-DsdTm9CuU98BtUk9vOeAgetrDrP6iENqSNBFTNmRvBjzzJs8TeoGeIiOQUnAufup56b_JO1THjwvNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بخشایش اردستانی، نماینده مجلس: «یه خبر خوب دارم؛ موفق شدیم از کره شمالی بمب اتم بخریم و الان بمب اتم داریم! اینو یه منبع عربی بهم گفته.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149305" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149304">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
صدا و سیما: روزای خوبی تو راهه، تحمل کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149304" target="_blank">📅 11:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وال‌استریت ژورنال: محمد بن سلمان خواستار تداوم محاصره دریایی ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149303" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149302">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe717fd2fe.mp4?token=bwxVZrh_rUcxagSZkcTSAzcWRADNuggc2LEb87wUPeGQjMv15L9r1ixNmtMgiGHCfh9okwra6LIA68y37F96OEDFztDiGjTdHBya_lGUcrX28up4wFvDZcviumvt0liilUhNfl3mjWaf8kieWOBtIQy7fOo4WfQT9FlsiGbHbaWq1xIXD9obhtj2RQVK9YvidgKe6MbNxCzMtwszzFcppstiepitFil4o_96kH704SzhelLPwJmMnZeim-JE-ztaw1awN8S05N3ptPpSNFTrK5-UrK72XRbx85M0ZLutANJKxbxVayzAO_n03OIi1LUYpN4HcBWDp6qYIzkjDXGfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe717fd2fe.mp4?token=bwxVZrh_rUcxagSZkcTSAzcWRADNuggc2LEb87wUPeGQjMv15L9r1ixNmtMgiGHCfh9okwra6LIA68y37F96OEDFztDiGjTdHBya_lGUcrX28up4wFvDZcviumvt0liilUhNfl3mjWaf8kieWOBtIQy7fOo4WfQT9FlsiGbHbaWq1xIXD9obhtj2RQVK9YvidgKe6MbNxCzMtwszzFcppstiepitFil4o_96kH704SzhelLPwJmMnZeim-JE-ztaw1awN8S05N3ptPpSNFTrK5-UrK72XRbx85M0ZLutANJKxbxVayzAO_n03OIi1LUYpN4HcBWDp6qYIzkjDXGfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 25 September، روزِ فرزند دختره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149302" target="_blank">📅 11:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هادی چوپان: من حکومتی نیستم و وطن پرستم، اونایی که به من حمله میکنن خائن وطنفروش هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149301" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف هم اعلام کرد که از ساعت ۲ بامداد ۳ اکتبر، تمامی پروازها به مقصد ایران و از ایران به حالت تعلیق درمی‌آیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149300" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anwA8OKZp-Vy0y-9gtQE0I2Ub1NDXOKFbAAoH1-XQi_mPk1RSnCFDF9koa2V0waihHiZWIFKovYkgbZT9dWYkaVdVp0mImPGist7oo_CBgzgXXJkdXC0KRvPArQfexa-qY8ScQbk33PpUFIoQ6J_67WnWFw7IbRIpInC1Qy95uhUxtfBMrYtFYutuOVke1-oqxXt3MpI0-EoJkXSgwiBfbgXqyLXB_Uu54Sp6LgS32fvusWM51oKeqord4DwmvMLovVLT0VTXzbBPzBTnuloRc0Icm4J88AgRgomR54wd97CSXb-1teRmSZQifk3wFSh7GqN8SU_ncvKbUaggZZK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آقای پزشکیان مگه گفته نشد که اون حرامزاده‌‌هایی که با گلوله تو ۱۸ و ۱۹ دی مردم رو کشتن عوامل موساد بودن؟ چرا از جوانان کشته شده، تو سازمان ملل نگفتید؟ اما از غزه‌ای ها که هیچ ربطی به ایران ندارند و به یه ور ملت هم‌نیستن گفتید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149299" target="_blank">📅 11:36 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
