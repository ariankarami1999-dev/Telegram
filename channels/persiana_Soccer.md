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
<p>@persiana_Soccer • 👥 614K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 08:19:33</div>
<hr>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhOMsRxXe5ZaKtZPFNrRzSwPfINFupFzaU1N9WjC2L4RAnqlE-Nkqe4U0Ln4NMdpXmYaUX6JOyStnnP7gTUKkMxFeREBroPsUoLmIv8nuSQdg8vRHSF-fnIVrSdQxXNpZnQh5V9-pqxsLkKG7LO9HVrV2PcMOxn5oS9otxRvpOLsbIqrliuaDPjkXzEIo5VcUYMBo2EjkzqMzhdldv3rZPw8hm35EKjHUpCfnH3ls_8eks2Snw66TtEaQMMbnqU4nGhy8N77jBQxVHcNBIW2e2-ASIzdntG-XslVZfnCVZ6UtTSjwktiMtQBTR4EeyTB09uMQ8hpHVcTF23mtyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzkSpNH-kCUf8sKq4iaVt4ezxUraqJVqKTsgle-1q0DAebrwgroDDCMWLH6E30nQ01xmIrQyrc4tQt3p3BV-N1Upgda4NEJY-Jy2_0AlH04fqpHCJrOjKlkfI3P7CDNqJ8ce2WeKV4bA97A-ik2bpJfJBz0we9oe4hgQgT0knruFStDjZjN65mh_TuB7PQM4yDEeQpgnxcqEucv3opRNqVG8FoyYyVFcfdwFpwPLjVp55XsgFfWFG1E-EURDJeHxrgqAzMufNdRhGudsSUO6DJyB1Py5P1SVJCwYzGX1UnyxiwHV1qz040afUr78rejJfilPV1BR9vWlP0fSec-_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=mMz9g3BhCzVR7dAd-Bdl40nLzncWOsCLlMsf9z0ODvtznksjmxgQKZ54_fndX-LIbCoA0Izk6LftXbK6JCfDOConQni7uZ9QWfKJhDAwooW_Mt4e1xU9Amn0s_j85b6Zqdl0VHjmI__Ce0_9pv0aYkzYmsQIJ59Ayu3RHJS7_xrTezUu-590WN8vc5m81b241RtSNbacwjEuMGjBOPalujIGvi3HTqLhD9nqlvFuRnH1nuNN0NpINWG607ktWNiqo2jeLiPICizQxKqemtX7hTxThzOia4tu3Jx17Ymoe1exeK16XQQ-TSjxNqyvoGqqi_37lrl3OsGxOlkpp3Nxzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=mMz9g3BhCzVR7dAd-Bdl40nLzncWOsCLlMsf9z0ODvtznksjmxgQKZ54_fndX-LIbCoA0Izk6LftXbK6JCfDOConQni7uZ9QWfKJhDAwooW_Mt4e1xU9Amn0s_j85b6Zqdl0VHjmI__Ce0_9pv0aYkzYmsQIJ59Ayu3RHJS7_xrTezUu-590WN8vc5m81b241RtSNbacwjEuMGjBOPalujIGvi3HTqLhD9nqlvFuRnH1nuNN0NpINWG607ktWNiqo2jeLiPICizQxKqemtX7hTxThzOia4tu3Jx17Ymoe1exeK16XQQ-TSjxNqyvoGqqi_37lrl3OsGxOlkpp3Nxzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwsmSb62ahJ71ArlCV18O8g5xFXJPkuvjalfk9BFvOTQ5rqjWq1xSIAXgnTWi3N-s16QrHmCo1rw-TleiIMoSJs02L-A6A4yKZRNhpEEbNV9_EkVIzxJt_EzFGhK6pQN9_Ah95ipH3kMLnlVKkpE9-La8sUHDn3j9wQz7HNFxfE9P5_F8kG_TQHgUmFChziYkoosHTxeWgw-LlZUFd2ZjKJovntu0u3M1Yx3H7OXF6VpNXfSDWta5eAR3VflQDoWRKvmbPNqNZRrYMGkqUH7lb8C-2Ey2cOWi3DT6IaJmzi3JNEhkVW1QTPnAyQCgVy7as-RArto-QNhZzFE9di1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7q-tPoxo4zA0GCjT6ZQ9DqbnAyqZedTVaenFtbRbtyocvGNsCGTUFwYQQiKWB21Li8cmze5wfDOUS8wx6gI6OCKNwqbTDomD9AypS8bgBafuTedb0hDVq1KRjuMCZRdNxG8DAFUpadYvP37AtLByVoaR4gryK_qkpQvYiY26hWN3tG9PuXlYSYmK07T3LEYhe86dQuuqtBbWBAGH5H8Lvmr__KgA82D5vC2UTgzYcHeXEIW1fdD44wonsYgK4KZBuxNc-UjBCMnBOPFs5nKBBBVSgVTWiXWgEKLfUr-6BFVcgNxXCFH9VAOzG_rDWhVuwtvBACqMiNxafWWP_W_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEyBCiPTMbKLglXkrjPRAsifBQNAl5PUTJ0k84ry4HGmC-TGT5ECjlB71dzUWkur6m0yl5H12EgwGnS5dvyjf2kkoiPFZV1o9R0wxi2xka2_n07NbZ7jVt8ibH-d2Cc4L6hvc3PBKS31EnpKEWkrg3Qfs2TX1n0Adpgb_eiJbze7TY8vKyqi_0kiPTxY9gN9eZwwXKXm4LKgQJYmy_4geB5MO9OUX9Zm55V1QNt-bBYYsh2KY5qWNuV2FYyK7oL_JaaiVQVyGvLhLZcz-jbj34KJDkd2EVdIiFVSr5JqWVqA8cNdf9SNfyItbPZGT-UGTFJ5FalsjMidkxuGxQ5m1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAI1c8MHnTqAqKS6CNU7uRaVpXSmdmoK8r0rBRVhuqFPMfQIZJIMS0kvQKyst1zXNYzRi3e3L4qPU5zzedHC_mA02LZkVVuKSfuCn2KjekPGyUTIbbTpPY0DFimbsJuFe8BkWD36p_vxyH64vMMBEjz0KD72GI2jBH4a1Ig0XgT-qwDw5EX6cquAqd6j0topjis6d20rL1Zg-QpwOFzUnD5sj5YqwhcxagvYxcPbolT0DcK-pHg4M19RsyoEAMtk8DCA7fdnHeRxHhFipGPan0pG3RqM4-JDlID87uAm5iI1tYHVdP9MYnLH4c1zBCC3GZEbL3deGJMWd_K49MmT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMLQuTwr1HyG_z0pufQR1Z_0-L8dcgYvxbl3QzCXXXYV62QCzYLkkw723LvY017X4RjHydQJ7mazLsJ1dDr4o2vx8mK1FwA6Cd-41obqwDcGXJoXi19nv9j1LaibA3kMHQRqUObYmZtJOyIhEKMxI3znj4N9gJz8cjKa6iuS2NZpThsVivffEH0Yc6rHfZQfTkL6hYvWPOJdPhlKCUTfnSBFD6S_FSMU1klFWuIOmbLMFX-H1jewobDvl-pWQ1bdGKBrFERsm9oNBUH19L5H55lWPLuMhMKMTd7-hA_dGonAtuqS3Lu-bs21urmV3kLgvlZ9-DA-oVtsn0POJ9IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw0aN6coJA3iv28mKLQ-sYVyQHtMyyd8qyUcAKjjvy8dJ-VDtei6HquEc5oYbDanPEor2Hvyuw5R0NZHDHJT8wPeUWQkCI9fdDbwX3CoNvtZgczmDR2VjT5FO4FGl-niz5POQgNrB2BpAIPgguwG19tnuLXGO6ilNV8Hp-AY9f5PeCPg8UbDIoBzGGFeLLCzfMvwLqOovqjjH9OgkxchO-fMFZSlNFRqhZlAn34uID1C2EDxhUgPa835QQESibb3SvhbV5amsVerO2D_ltlSewhMbOha9Yz9Krv0IcxaMqR_lZvRx9L89yBELI3lPuVq5Bhzg6fTsRx2M5ZPmzmRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs6G0XY8lO1FyZytWRgliXL3jb0Yrl6Mx6hbfg1vLdiYFgibKzrXxpYZPX6ZVmyILKgcisMFylk9zDWQnthTmhs-ClrqtQChep5Q6pnuwO1wyd4fE591zVejBw3Ggy9CuGAnZdI4Ucz8kHTZkG74Anf2qr8IeWl8IPijG_A96XokFmvDe5LLk6ZPPMr0NA53S7z6Gwpe6U12weE2QD5eODqxYbtM3dR_8u4YyzV-RJtT22yM35KfiK6WEdNZupSJ0WSBmdFKgA2v0waVpOfQjPfsIxj4YPvwngKIcMIQJ9Q3cLtO-RzAxQ7lUXVlkuBu2XsQFwHSjzdfGNh8qRIv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g4sFG5AZpYhsSRUTpiKK19vmokkIoR59SEmv06h41Mhf1-ugv6AaYl784unz5f56YNEXMhQDSCwW49c8QSaIIoG7mF8eR4WnFFD35GfIv5xiiECI2UjWsGtLe2JcJWpoXAdws42_v3shUj5rvzzmbCepbx2-VVlyL-8ibG9spmH6Lqb8jl0PPDI3_2LKk7TLblGKIZph9WHNL0C1NZAO9W7Xuo_FbEpsTiFQzvPCs2JJ0iuAcTkbjMeTk_lsOg6krwNGSZ6IwTceAK1pLJoZRjG5B8etyMM1L1WKX6DTUw6MGyEZWFOeRrsKz7zcpmrwCjqFPHxd0sRvMdg7pUr_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eE1MjswtM7QXyzjblrK3-_xzzLqh3bA2GGQpJbt2crlUYzCLr1sMTtfgFI7WnLHJFPJCASEQ2G8cy7cU2KVTLZWDupAmKEDjuqEB2KDwbHFTsrZVQByqP5sh0boOZm3eNOvmt5KxUMaUvPFsS_wQlowNO6O5oGH4xveSNd6P_Pxxp0yQVXVXWgNqObgqxTFG70NVzNhLMD5tcchsyiPfj0wmEoBRT9h8aizBZXF4UybqVnb8yGP-tJ_YOpmkf39m4aWcUoDdl0yfVJdL1Mnu7vJ0DAen9Do3rXsyFQvDQO0qiB82WW2GzdR2vBPf-9z-TACkAlcJYqc9WegrV51lDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDmw7M3CT20B0ZfL-AIJ4YtvyLfBUM7Rfo0SfdpNuJeWq9_ISaUvR_zswXZoiQV98xleSGZw2hN-bEEQ-nfxRmGWAfQmjlrKPAFKWKy2nRDjE1zZciOEx1pP-_2wPfrhezJZtY0ITyEUDXzKLn4Ipt7J3hrelh5SVwV5hXklj22q5thrNm-oNOmW9Fl63xBDzanjiQkdKef3IUAj-KxyEssI2es_iJ-GrUj-_MoD2v7QxegUtg6V6L9VSBswycwPF4P9oOtWaTobJXguMyta_SV6O1fllQJGkk8jrwi67Vgw2c3cdw5diF2BKxwwKRK-BIBcDGRLzStqIKrp87BU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcMCu3uHB70y2L0tvn91bmvvy5-nODopTxgf-37Mz9lzngpPwlSW8zgFNpNASXFu1VsR0Yi8VxyJbNS7I82mKmDdbNfj0wtHDwKO0rJa9rp3bqgvwuVbY3bLpZz6Zq5O00S2weDL-WSTr1QfFHR1lsipcvkEEdjIsBuggSMjJkAKKPZLoOqISc1Hkh_WGtQPhNxLU8jqOHkSoizcpNFSbmjSaR8oF1_o8WB6BJ8We9Y4YNsspLmyto603Gfys75QW9vBdTJeNHz9_k3lZ5x7fDn_EXdtkZbO8w11XI6rcqfm8vp4OUQQMn79nwVPFN38j7M1OFxZhnphu1BkcyVm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6HM2GJvL_idLSfgPaVPTCGlUPZl6v3k_0kJGtzyf-WnMmgLfUPnC2vRRqW_ClxGRQZnzgKh6ofPYu0G1oSOIyyrFIS05kcWJaFDO97nbjz7WzJy9s8KyfdUdEmbuNZX4v798Ac8HGCRZmoW-QZaGAMmjZ0oEl1WWyjdnyi29u_fVcorucBIFQjrcfifZun7t0rPIimMg62Yx34WIoDLS2lXhDOpl5n0-x0x45yRYsHgkeom4wJ4g9j666ewmelLES8LItngb-6TsHMkwCscZn7Os-GrPcU32LQUZGhkZpeNeR_jjW8EAwUoDZ6u1DKhkooHFc6lPiq81MFw7Ag13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKoKFOQn6Nj4PKUTIpJ3FyWNCqqhKSuW7-tLEcI1zwM5DXWw4wlVeAqVvVGTCBQa7gkaBnWYtlYgEtCk0gR_I7CRS8hiRmrod7BCW99L86MG_ZJm1JUnCzh-Q_liVGNLXXFM6XspqA9BvMW-6E66qEN0Y9-z5LoYOlfNjuTr4wWZb_ijkGIfP9BwI2YIt0Nt6KD1SyRmxYdpa5NBxaMAXLdOWuLT9KO5RCRBELtbNBdM5WK6IwkfYQ8iRPNU30M50oc8dIrU8S-mmUgi9sePwyFBp1cKZLxmnT-4AaaAcMdYktDEalO1NIP_66Z219SsR6LcerE4c_VEijxdskveDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز
جمعه ۱۳ شهریور
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۳۰۰٪ بونوس رایگان بر روی اولین واریز
✔️
۱۰٪ بونوس روزانه واریز رمز ارز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/28998" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAc1_ANE3Sp0R2WuqI84rqlKUt_4LnOwYK4_iFbikEx_-YMRWsh8jzZLKrCVMGIxMARhI2VYQj5ESvWrwIc5NlYsBWAUXJxz42ovLwBUcWhXqS_UKmNaMwBfiwwE0U-7R8fEBKRWZNfYDJPDO7rJvHJQ2zjoXzKLPIZgLfdcm_wAYzVVOU8NO4bhu3KkbZs8Pwdgq2Fw5tLDEdrOzwrn8AC8PbJvSuElFfdHJcBouJMWGeAkH8LDw0Hzl6DU4LsEWzakurxSmU9l9foBiX7Lq3XTjIbvdEwRuw_QL2c4GT5ZnCY742IVG8lDyVPSw5ThLMgcRXxbWl9VSAt1IGzy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbo7ZkB_GeRPtInTKX59-ZVOpph67Y8e5zCi9zVUsCwi0RfgU0GuUYTG5SJjXHtkT_05NwHOxwG7nzFHQZizGt2X2ccy5CR4ucgZevsUaXVr5-31jheUg0pwiBBSIjJ8SVbCvGlliDV9n9qy9D6BMe5f1YbtvKndAWiKgRpU1_soYlH_14_puRlVFsU78hG_Zre7qjCG0T84oiMnRmFILJ0KXDBwXRKuFIH9ZKmj3E9y7d-dVTDr_9RwgJNN3qeUkLdRz1R7hWA8S71cftEh4StfLJyIriM0hOVO2REY3z_0UTyVScF_huXedBMdLjldB38hAWuN3cYe3Ssdn9Y0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=ggWf92W0wJ0Xp1n7BNqOpZ6ME0JMJbyCCxhvtkaCiF9R2ZEYa04LRee6uXezyA5fQOyKjlW7V1EDDd0pJYxSmTGBisMXJBprNMaoGIQMsGIleEveRDMLOB5tgHa2zbOppE4NWqWtZwuiah-AFActzOe6k_hkAkvYLXNgIxLR_UGv8I3rFEMs4P6CV2Q2y0tHyiV0RnmFRbiPRAzMY8sEg87r4Zk6g1O1KBBtbHKfipYl8gS5Bzk8BDf9b7gaY44R_PcR3AwTCqZ_9YTOqOWD_BAaf61A6giuOy1UfmLDSicyvVMH3s1_sLfY-W86G1Beztq81MBQo5IFWPhJHg9IIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=ggWf92W0wJ0Xp1n7BNqOpZ6ME0JMJbyCCxhvtkaCiF9R2ZEYa04LRee6uXezyA5fQOyKjlW7V1EDDd0pJYxSmTGBisMXJBprNMaoGIQMsGIleEveRDMLOB5tgHa2zbOppE4NWqWtZwuiah-AFActzOe6k_hkAkvYLXNgIxLR_UGv8I3rFEMs4P6CV2Q2y0tHyiV0RnmFRbiPRAzMY8sEg87r4Zk6g1O1KBBtbHKfipYl8gS5Bzk8BDf9b7gaY44R_PcR3AwTCqZ_9YTOqOWD_BAaf61A6giuOy1UfmLDSicyvVMH3s1_sLfY-W86G1Beztq81MBQo5IFWPhJHg9IIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmDNqF7Pgo4bUCjBcu6ZpnAkS-uGowgXeHcEVkC0O0PZU4YzTqEeotI-hpKm0Ix6ZwNj1f8SAv804GOL28gOz-XUxAnd6Fts8ZWgR-hG0dPg-bvaeEVLyY9D47j4IDR4nWE9Jd1Hfnh2gr0S4qIKAFkzyqawFhQer_Sf3-_uUzST0ZLMRPISRj15X7IJiyrDiJhmuCa_zWMkEIVyFtihwZRTeidXF3RQsep9NXeVfeZySzwbCJ1Aka7RoMU6vivF-O9b32OJaqQNKB3H-sa6_WGEAaYRPOotbCotJblMGX-bMWDyIk5Ev55iU-i2KpwkjZ7VX2RdQskvWlqnjYlnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv29e3rxOdxXbGUcGMDDyGnUq5-siogELaVwPichUeHlie8u9TzTgjcIpMQTCZFCip31ppeZXmVJQmFwhcKvuDKgM7cH-cBy020TUKU956hnq7fjVmzxneorysPp0hh7d2DNuLOI-XP1kItkso0zuK4zTmJsSiKt_-ymly_7M7qGqWLMfWym8d5TQmNq8iN_hBBwxU1CLr14t8hqUBhybBVLijTf6mVEMsLkkZCyctcUtCITVWyQ8ptvzFBQXuboKAGc4ClMj3-FnJWR6I0yhG4JDbvUEAQe1-fk8x2ecjz1nI3GnwCvtpT840zZpIPuYL0rs8mPUTwTliJl0aSd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOZTvN-WIY-fuxCMLtSvWptcMtv7SxQvp3M0XrLmpFnXgErYGWUk6w7Diwc97SepcALoc3pF0flCmcSqW2OB4DMgt7HipmZEhDWjS4UnB7DgGrFOrts8wUEEqmGAV26Egpz9Ttd00jQJWJXZNCm5VESoUiY_FPSVrhplpo2soSMYlScizzRqcYxOTTbKAv8Pc-BmPqxkSyhhlcnoKDxPgYYQcRWQjRlvGYPX7ABgdsqgkuG24bnsjvxSNsHRqiaxmc4JZFyGmMyZD6qvSLTvY2dFnB_2rY5iq5qOgAAmqGw87h270Q_zhvS1wgijauy-OrYreU3TLOj4fXd652JurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaktirB7Bzlc1t68GRMsirBvrEHQRg1OiORaZ2tXwlnGhN-ZEGfQL6q_1k4XPFjDHYSyP6A6yZDtLI5m1rxYPwv9TlckVEpEdkYO_-En-i8hEyB2RI3SDil6DZvBoew2Hnm4AFoc8yVKELdEJjCAdRroZqoduwLEgf5-_sJHdrrr8AEOvxDMhXqyjlvjIrVbXwe2MsagFbu6wqiqpDAGfSIARnWGaVumGFSnp84dGal45AEmtwubbe6nR1_IQIyJdT04Yl3gSpk0Tv9X5psOi4Hg6WWqVhu4Gwxgd_8LTyNCPKhmmHUOzMbSm6I-uOHMcql5IGDUBQDc4qomHE1EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQN3hOpv35G8anayZ6RV07Ur1FTVsyS9p-pcoTzfMYT2XUieBwpXU_ZkxyeQwSmxMdJDnRvGxOMOCaPMjv38jNVaSmlHtqPRea9eLVl5O_mpbk7lNVh7YEBZS4uz77FLDDtgwwD4Eqh70rglIdxks3b0UtoLgDp5_3TXRzgHwHDT9Om3WA2FUjVR4XNR6FJz41x57HCCERfiESC-1PPsZbFniZqE8Ag25bf2iW4s4ZuyDlfGf-ikxaQxm0N9NEjUO6L9zq1YW3NXZFUrCDrD7zyeIfhvfTYKMBIylg4uXq8p3i_6_pYFCR_AKxx82TQjrpdVx75hfnw3K8Zt2Vki0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=VH9j6vMR9LlV5S6mAgwB2yEhfhOm1lW6GQytuSJd2ng5rohf_Om6YTXml3dYAr8GAUNNNdRJrGwCKfDHcWcscUjaLZFbICcToJG4KtxfEy4_KiGPL8PTAAMcUMgnwUNjAYiJQELKz-tN7wYv4AhtYCC_W9eIfhcWQRH4NN8HhtK4R7mVKUUN5MNp_S21R3d5arcaebpsEQTj1fRxn2VUnyRilqFwZYvnGGwiN0PX_N1arQi7O5g_2vhhOJ3EhfupRM0HaWn2EgLoKCyuQdzk30HsNVoM7zMHLdW21Zto9ZlHRw_Cl8V8po2gawogcWsDmbpZ2ElV9oU03rQ-5FUFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=VH9j6vMR9LlV5S6mAgwB2yEhfhOm1lW6GQytuSJd2ng5rohf_Om6YTXml3dYAr8GAUNNNdRJrGwCKfDHcWcscUjaLZFbICcToJG4KtxfEy4_KiGPL8PTAAMcUMgnwUNjAYiJQELKz-tN7wYv4AhtYCC_W9eIfhcWQRH4NN8HhtK4R7mVKUUN5MNp_S21R3d5arcaebpsEQTj1fRxn2VUnyRilqFwZYvnGGwiN0PX_N1arQi7O5g_2vhhOJ3EhfupRM0HaWn2EgLoKCyuQdzk30HsNVoM7zMHLdW21Zto9ZlHRw_Cl8V8po2gawogcWsDmbpZ2ElV9oU03rQ-5FUFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOo_Wjk8tWS1Z-YqnUsyp9WiS8m6_W3wgfaS9Im5TTt2nRh_NxAZLWPMHSdl9NavUSpGGGPofut4gIceUCpx9N2qvCT8HmRrY3NpZ5NxhaLJVbf5BCNMWjrPvyjdU5zA0qu5WaxjgVlxt6D9m5ETbVt5vawM8ge5IutJKKu7hUbs0vJ6PcdaMCwS76U-9mpFPjeUKEX4cOHATmediUulW-bQigQSB9YgfTS_2hsj4DAoWrEJsN1_C6T7wu0kqTHjcy4wdDdXniUamtEDTMJm0iNoDG5L0LEARCgr2cPaoufGobzb0XlFTwjZ4UbAprE37DjlgelVZ8tA1Ri0-5tpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAdGLb7cwc4wiFEu2_t4NlHH41CfW_xbka-u8KStNDsW4SQmXL3w0y0trNAcPhMy8VhCTminBWE4BQf49ejstWmsT5a43pOvbo6NGdTvx2BegWvch_lPdykQY2mkvj4xaLFUjbZXicyU5G84BukPeCsW3z_DIwxphVqmBDlew48zmn28c9o5GcChlUBQiVFwJIh2c3h3CTPUbJf3GV_AijgFJBl4nwVTcjHwQVq9G5abm1M1jnFuC-y_uONs949I4Epo3h5gv_27vLJhAcAwLnYdZM3qp3K9W8dDsaz8QbMkud1qremJK_zrOPpc49JGY1R8zYQ9XjU1gSpOpYziKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLnAQYai_aacQ4ZGsCobIf3WbLsi_mZBhtEofuaCr-8DuON7Phg0YoCq-j30NnHVJY-UGNg3cJOwaFhAOYsfkbQV6AKdZIio6IoAl0nCJx9oA8wgHRbJT1sFz0TWP4Fnwm2ErYJ3wjfZOtFWD620kF0Zt8iFSFJdPUPyoNR3DHznAJKgjpRMxe3nKhq6Td2tUlA5-PikI0YufipU95mWyIImfSw_DoAP8-sqWfcFqoPtJfXdK-WRCe32zQdWDQqHaebOqEdN3lSEXOXAKDNPZwBxSMXfSyZ-8au58PQ3LCpQMJv_gDwtlioaZnEWCd1XXiJIYSLaqAqonlQdqLFOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAEut5px-9FpOFHYsHgtYpyDbepY2NPtTAGnaLjEE0XmhjN-gP7t59mNHI1GyimGYylwEY_btBT8o7ShqAugOI0b9AqP_qcX_VJJUr8FOoCBC0Q4aSWN14ibipgOzkDp_nmJWCLeTUnu5u2bWt-kn8e2jzf1y2YDaqc-hQ1qdV8cvP0oSavQb7lxdQuTAbIMvac4zk6PQY7RZMH4MHhbnfPO7vpmOaSABMeb-ycy4RhtYtbgfed72tIfUxT3lDqtyQd5qBgaKS_Lb_DliYzUfma3EeivyLQed9weeUmAf_ycd3IjCU9IZjrYutJiIMHq_2fQ4INd-AIwbkubhdxTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSWCzbeb86jnhRI5wBos7nEXzsrZxnFNOI2565GuTVBeuBzmDEN0mGeb5G63YWInJ5ZQGv656RilFzXOgTlgM7gY67ODfh373EsdBW-kYRJnj__g57-m0kWOACxlUaq4dPLxcc_YOkGQSE3wirJDet0WBuUS3NqDfBpqgyP7SQpax5Gf6AD2r5DZ3hHeziBct32cnvLdASqjHV1gs3Z_ExsMadIqMswVohkCXrF8p1DJnX-6zWqyZC46dHZuxlgFmNZ4Ex51E_cNhJ-ZqEN92NkQGc77xp9PI-jxVDYhkfe7TUhUvy388RmH6gZ1kZbqwsSMcqQvpXOznt5JjW6tmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjlxDs2g6qhOdqFyKEEuqqpOnvV6WpW5f7uEb_AxbLt8nalTsDtVOgoq-vdmDI145gTvjYAUbkSB0rg3PpLMaMvcm8t0_Fe4I8WvCYWJChCifLRULqJ9LxbDvvpA7fbFlxjrtb7B12D3qfxdomNzfFLSzy6HNiPGgqSo9-X6bnDMgDn8ZPuxyqncnTovm-kPrKShg33_-USF2ba7mGM45NqajoNCYGDZw2PH4v31fZsEeynTq73H7VfAIA-KKOo2_p3KmuNm-mm7tHylpEHx7zhVUnLllCK2XdHmZsfwex_kWQcq9NL6ZMgDHY6eDrQiSDn-4OKJXEe56IiNK3kAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jySfvoeeX0uiWnsR3yStJ0lKt3suxf5XsNFogIaweqcMe54-oXmQxah7RuSrMYifWKxFLb5YTjFJ7BgcCS3z7EjWfEZqriMKzEml0af7epQ_A52QxQrLQc9ek-3XKnobw3MSPO9p2VFwQS1FIhk5XO4jc0rsu1NKEv-2Z6_h82CBZM2Jn2u2M51mkFbczB8ewN9nhvnZgRGpeRBEitxqoUb1C_d8LjPN7wAXBzq_c99UkP5eGVGFOs4r6W_3u5bS0_XdvW3LkdMHtj7f7lP81xH4Q9NrUhRmJlHFjFr_oFrpUxvUCkCZXGA4bSh1wpUbMbByEHKs0I3-Tw70jAQTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZNuyigEbUXowq--jyMQ--dWK8S164TFhi4lSTiUFW4TPUu0JMrJVGwZMrvMzy2Nd5TY4_RUf9WjkzjErcOWPz7GASxjjXhXTQAR_mBtOWZc6JtyEyIUsEAKr0QGdQi1m7Zkz37iyHyBbPYjhaMplZxKiL9Edz26yMvJzxICazDzhPvPCuHTNhe3qjmixmIKcz9CDzU0s8Vt0OjpRYcWidbth5ctrnhgLbDqwpYfBay6mWsrNr-pxIHPlOsom5YV4TcXgRlSPQDIITljnuDcHHgh6WiJ-J6-Nrpu3FCe6IpMx9b4zzqiiEeeDE1Ic2iLMeb-BnJzKIPfK-X9HKu2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-0mRpN42TzKvk8iquNwdZyAX6arxzeJYYQg0-qDl9vKJyafunlD7KMsBlYVwkAzCti-ixGRfPq1u0XWQP__Uxk4obKXYD9JnTggnR_3-8hGVWIailClm1_XfhGo6jYjD5p_Aqa_UqQqhoIQUJNaKM3mH2j1IKdCc9TApTQtkoQMFf5kruOw2JHbgV55A29aHP816EC8zDx4VjzgZjwnOt29JhYl5WDRdGzZUI9lKxDkex1o4x0Cq-wTBbSPMOY0UI3wkwaywGd8OCTAUgqbT-Gf7Cgb5xR3S3FwoGmmA2ukBF8vzJJu9S-nNbMaKwFnvWZkiAFiYzdWyJN8y9ZnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPLBAVxsiArRV_4UuuxqEgrNNRfTUdevbj6lPyKo40dL1g9gvl4L409G-01qxA2Z8ZN8paKy58xjW03Lk2Nskel8XKjiW6F_UChBljhnt6I5AXQY5FkCuHyRFJ3kN927sCfnPRZxMlZeIXcB1mFMOJPM5OPQDI_WQ6oCVb2PvYLUoUS9dgQXuK7ibNz8fOJ4TuElGqhMlV7N-7o0vSOGEewA_Im2EB-Ww-HdfoA4XTaRayjaQrhcI1QnxpcMXyik-tL_3FdD3D1C-ULf_Xls9SjiP1rf--QPjAY1I5ZXZFVVb4z1CvMNQDem6RsKh4GCaC4WvFZPvDS7k5BgyYevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdDQd7-Ps9adYG63-DUbxcUkdl7inWYRz6Fs3sfl2P0qpeNT3NzF2Db7D9Jn81mC3Aksgz7JPqNAixr2ZxiSJN_kisYc5oGdn32qvmUXcA0bzHcXtVGbHUBAx4-pJVApyDM3594FO2lr8at9D___eaWSa3xzF-TFmw5hrbPFKV41sAU4Bb5_mOAGkw2wo5G1ZPAo7FYxXJCG69wPujetGS7W8AaCIQzqPO38PbWqE9iDm9V-5RRE4XsXvxVc-k9NEW_kCPRw_Rl-YHV4XTMP2H5fhpxORoCwZhBMsvKU0ocQdIoLjBjUKLt9a0nTCwkW9nOqq7Q0F_1hgfyAnFKcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=DS5kaiNY0Ohp7JPfDTdjQ5yk4wuo8lkOLBLkZnvMrTzyJhiyh2z4TQk4M6qVaI14AHBX3ip7fUgcA7B_xAgh8cUwwoeWzUhb8LAhVnNuR8K4ytUMHcR1may554FUFlS-vt6gTAUO0piWRkzT2uKxuM9mbJBK415UGBsaPCX42HQuzFKeqGNhJ32yj4emNWzfe163V4kxllcOu_f4c2_wkDmk1bp7QuWWfskEsBBPIuBjB25oDZUN5x6zTRn0YGuviVnL-p1CznM6NyFhtR6sak2_F204lqByMTL9DO2wNqDREDXpk_BPLSFgoaoa8tOykq_Retx7G1gTqTve2L3O4AuZJtPH7ozZ8eyWcxsN23n_tlBZFVn2Psb3pVt0ZdELmsAB8I0eYKLUxyS5IDArQidMNJcJiwjKa1dKcFuvheJDscN7mUJs_zpd2W4ibQMAsBR71gof8JTm2PahD2h22bmByATTQFy_h555dIZaZI5w2NSfAQr1b4WTjjcNbQxG_mUCqTkIIXvOb4AKt0Ujjqgf6pY2hh3d7kGRfr1a_nr6cNrLp25wamWNaV5u-Cfp1cpDPuoyt5JuAdOB_CzQqboSBStH12h7fsL09xZJd5RDlFtrtRwGwm_eCxi9q3ja3Dd_LyZt5TG7Z1IZzRdoC1sfC7Z6oz5tjjEpCIzsxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=DS5kaiNY0Ohp7JPfDTdjQ5yk4wuo8lkOLBLkZnvMrTzyJhiyh2z4TQk4M6qVaI14AHBX3ip7fUgcA7B_xAgh8cUwwoeWzUhb8LAhVnNuR8K4ytUMHcR1may554FUFlS-vt6gTAUO0piWRkzT2uKxuM9mbJBK415UGBsaPCX42HQuzFKeqGNhJ32yj4emNWzfe163V4kxllcOu_f4c2_wkDmk1bp7QuWWfskEsBBPIuBjB25oDZUN5x6zTRn0YGuviVnL-p1CznM6NyFhtR6sak2_F204lqByMTL9DO2wNqDREDXpk_BPLSFgoaoa8tOykq_Retx7G1gTqTve2L3O4AuZJtPH7ozZ8eyWcxsN23n_tlBZFVn2Psb3pVt0ZdELmsAB8I0eYKLUxyS5IDArQidMNJcJiwjKa1dKcFuvheJDscN7mUJs_zpd2W4ibQMAsBR71gof8JTm2PahD2h22bmByATTQFy_h555dIZaZI5w2NSfAQr1b4WTjjcNbQxG_mUCqTkIIXvOb4AKt0Ujjqgf6pY2hh3d7kGRfr1a_nr6cNrLp25wamWNaV5u-Cfp1cpDPuoyt5JuAdOB_CzQqboSBStH12h7fsL09xZJd5RDlFtrtRwGwm_eCxi9q3ja3Dd_LyZt5TG7Z1IZzRdoC1sfC7Z6oz5tjjEpCIzsxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvMtjZPPkwTq8_VCJ7sRnmcx0ogGK6VhTJ5O7k7eHQD_dd3SaVRRKYB9BgieliuRgkhukxnIfRc3zdV7eLX1dnAxaMFm6fiZyoX2e9B1T5RaImMk12GLVGhHJcmWLrAk00bBHX56hRRng7bhwx_MWmKaE_m7sOgOvrQOxk5txAm9q5doWRrKpiEjZByu2ZLhrFmvfoNJ4qLtw6yLOfIpUI_legcXi55p8zbsM5QBwf7q1i4EgI9kVYseOX_bMJkiQfTLvaMEqd0adSfzy7BnwjiPuHdkBK-f_XiewoUfQRFxPKKDjsW38kWOUdgVIC4gQpYSxVIYH2fIOz834KGaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUnp6zNZsCOnob6ZUmqQ48vxUEULBKUWaB22FQdZhdZEZ8GYRhkyLINqTH3jk6LljMxEKkyT-lesEBltbg2CaeHKAd5MuNIn_sHh0IM_icuJk_sZYqMdk6Kd8w5xU8BLffd2qj3CofuFnSTITEwFEkdpJ5JTsTYPHAuD8vVnJsGPM53D-lhCQGbYtv_ukCQ_YHWAlKHZdUsXOH7Jwr46CXDuq11Wf6qV4We8wky36F9FQ98Z_aPALZNsWVE3GEIdUWbIBnABv3kIVKSgZcWuwDI0Vt2oOZXDVHq3LhtvuhZ79K9Dx6kgBS7-7Tf9BIWSGGGlvU8KRuXQCZ5QNrQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=XViztiuODJBsetxFHc2mjqltXfmvQIkraBRSRy-3ZzbyMPZSvZPTjiIYQYmvvQY8k16vW-QiwyDx5F_4wBmg_5LptXvIIwQh2aWs29T8KitbJeqkHegu4MHN829sP0HPN5guIFCNuQXaQWwBAwSpZIB6ji5f2aDysF1pxkQpuBCezvsURiEweyooQrtAbg7M4vBPPp-dIlRBOH8FAMiH_ZZoasZE7gPl3WFj77yIGEhPy7IjFqr6TsaInsQXZxVGgayB1fAcf18i4ll1HrSeOP32OTSXSbzMf16bQq3SbzkIhjliYPrdC6tyewMjDufkihJyphBTKhDBZXARUTawFy-wGnbggeLlAT2W_I5hR8ngrFh6D4YMVMbyzzxDDC_H57hE6ufFlkxuKnp7av2-ghsZivD97L_fpTXGA9pJNKh0ZW9ErQH0fSzgc7bWOlJ1wxOWKWxLdgJ7e4Q5sqPT6wxfjeHT1Fo33Lh_GfDU0vmlqCwPKQVblU82Txhvwqlx7JuNAOF5rNUR_GcwY2EGNCt-l17ZUEPMTVmV8dzb7Vj91ZM_cDzNYSX_WoSohlh5FzZrb3dsHNh_wOBXh_vvvOzJi-GcWcOjU6o7Ydwx9qBnKAPIrHNsQzL0ehqQyXGnR-e_khb_1CNKPwGj35UevhRo8h3SWmE50hcs4S0j2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=XViztiuODJBsetxFHc2mjqltXfmvQIkraBRSRy-3ZzbyMPZSvZPTjiIYQYmvvQY8k16vW-QiwyDx5F_4wBmg_5LptXvIIwQh2aWs29T8KitbJeqkHegu4MHN829sP0HPN5guIFCNuQXaQWwBAwSpZIB6ji5f2aDysF1pxkQpuBCezvsURiEweyooQrtAbg7M4vBPPp-dIlRBOH8FAMiH_ZZoasZE7gPl3WFj77yIGEhPy7IjFqr6TsaInsQXZxVGgayB1fAcf18i4ll1HrSeOP32OTSXSbzMf16bQq3SbzkIhjliYPrdC6tyewMjDufkihJyphBTKhDBZXARUTawFy-wGnbggeLlAT2W_I5hR8ngrFh6D4YMVMbyzzxDDC_H57hE6ufFlkxuKnp7av2-ghsZivD97L_fpTXGA9pJNKh0ZW9ErQH0fSzgc7bWOlJ1wxOWKWxLdgJ7e4Q5sqPT6wxfjeHT1Fo33Lh_GfDU0vmlqCwPKQVblU82Txhvwqlx7JuNAOF5rNUR_GcwY2EGNCt-l17ZUEPMTVmV8dzb7Vj91ZM_cDzNYSX_WoSohlh5FzZrb3dsHNh_wOBXh_vvvOzJi-GcWcOjU6o7Ydwx9qBnKAPIrHNsQzL0ehqQyXGnR-e_khb_1CNKPwGj35UevhRo8h3SWmE50hcs4S0j2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVDbQ4QckgfWRW_-VpDwJR8zsCdujS299DczKtj3pq0wU6yMotWvz390Lyh_55cBzj_gYJQsj17jeELQfcKwCCxkU6_6aAVqP9K4mcDg-A1U8etvCqDjDQSgjZijjeBtDRoSEQY2UybE1enbqA4nCt8OXX5hGX9hUI2RVZLs7AK6cZAB7LZZtGNTMLkexePz7DSMHidfbxn5DoszKu4EWYQpr2tP_O88-J2jQj517_cmh-Y1SUe_RFDhwoJdJ1KIBTiCTauAz6EauK5xJNquIn2TG0v4-X-ZzpDNWh8wq9R2exM2Q4U4YCRDVhEJ6SoTyvLqFpMJJp9t-rrFFUqglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMk4cSkVgiuoWm29jQCgUldoYtX49mxRI_Fvrj0A76TNbsTs9jWz6oPK2r_K1BR-iYsB8fj0LPUKAqCYgjzzCa5ZucQDsgXVRFfeE7Ze_tClAtXqqfTY9oJRYGJdVTPBifMYSpCqneM4cbK6VEYmMEYr81mdMq2E4M-nsVEctbw6JgUGZXN9Jhc14BFDSeUZ5_bQ55cG-yYcwJlB2ZuiCANN66jC3ziv0ESNzmMie_2GI6IQpmZHok6eRB2tB-mG1cKYOV4QC4z4twu2JpQWdO28WDPRNJ5ATm0wBzQjbkvTLqVfxdQuEeYfB_8U_Ux05tY-tiwxeM4MchEET25GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u544tv3mpAoyWggQKRmZLxP2vkAugiWaDhdCivgWcri1C9jicudrP2pq1Py-42ZZH7FhMp2J9E8mYGXdlR6yekMGWx50EnKTPCuqohC1gIlk3hDc6cAmOVYnN9iTShkdSGLap3wNrvuXrhVFO6tUJc691_hXIzeh8fAZiZ0zcDRsGAsqenTPlsCh0PhsIYqi-GyKoEo8QeKVF-9f2XeOXJaoVmV2bekfJ4vGGB6Ej43AdMpYpYzl3DXxJiCj-XNGomLDT0lq-noB0hiwUiUS_AwpkHk6nkh8f_VIjILlvCW1VFbUz5w__nigr2LPwx-YmhHtBWrxsQSEL-SxSaOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH0MzOdkTtzCBIUbgWeCUghsIaORnPO02r8yG1xFo_O8Gv8aXnL6c2QpbL3pSg6f_oj6s7XrYcz8Dp456On_vsSPzAbw_MItSoxWdI5IYZcNfRWCKKB7OFq7VpUcAQ73kK82YtAfq1X2MHc3Z5_iOb4Ludv4x2HFafjp7bd9K-H2DItVnEId3pGA9YrS5VDslU6FNfOR4fQkj1k7kbuWEJSdxxlXN1gaF-HwEuOD-Qs-E6fxUEOJe2FTFl3I6wP6Lc88qiT44rp9KTuqo4OA4zwOnduJ9DFKm4-Z-vVjXm2Db75Ncl3CkCYF7_Gaekvd8wxqnEycJrS6qFwkB1eXnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMXGO7sAIu-m_ZoRYgS8y0esSAegi4gpr4cET7k4-tdO5YKeo7sn7jciItSMmMzD9Ks7gTMJShAcVaYIwXKXQDA5aIvm3Zh_VvvaQWzn1GHHLc-hmxB0Y2ZLN26PvRfJSAdsuGPWEO_hMTWwwaqciOFi9H4ZKaXFY2nPT16D6n5PnPrt-GSkuc2Pj4cyz7y_yBxSlOSdh_2OR-dpls8R1i35bN54z6cZnxr_NPSuIYgc5GGEyBt2KIFjlROjB2B2OmUiRVeo3zEltW3gSg6eCsQTZ_jFU0d7OzCqBAapr-9BS4Gcsls-O8rNCE54EJeo9AQRMppUR7D0cuMyE3EtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBs7anTIw8F7doK6WuNQw170FlokWjuCQRz77ZnePUYObhDu-xsENU_zGZls04Mu7F2zJVcCcLHUmUfE5OoUA-Ety5XZYMTYO-vNfbkpfuduHgHlrdv77aDJjOPxNq5R5Dvu_r4uxdCG_w3ARFT-kDMETcrvnafvUY8dP7bnbKw782A4QWvR0sSjvYTtuTKT_7b58VOmLt1teXuQNNCKLF_p2KI1S7kzTgP4-H0cCjbz4eOoO1EQyr3-DvGv_iZeIV2cXvoung1pYCiZswyb2Er9zqd7u1BtUs2zf5mXEknhfDIBW8QTBS25F8XD3xOwxbS8RhnO6jpqs6SsPCgwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unFIdHoBIQmQMHBukiKQNcchjVISC1l3MSM-V4IvQxgp_h2maogQGlvMngVCuAINSbo_X0DWWaJNVVW8YnkjojXgaZa_LVVEtC3tdk24I7eCHX8QQcWpwFdpanRSS9QTkQNI1Kwh49KwxYPrqSPgivXvBRFJnVZqOZPunDscXbWrAuPtYNk38toX-lBKHMQPgTeSU7gxdwJt7pWIO8J-Dikhj2soE-qr4YPkgHQM6L8LuRfUcfF9RGY06x5cOe_qdzyaDIWCiNhkNaCOJpFkeup7h8foTtowk2DkL4Y7tB5xIQQrM-ehLGhBxPLODFnVqVqp-0s6H_zxTQJu-5hBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqPA-SDzj74nf8-Vrj8uIbGPYFf2yx_cyR-yvoFRnMz_w4MGFog0QxiCySJMZ7wZyE6LOrnCfEdWWuoTlt0djpiowfJhCOHzvBm4FMyPFQv_jLoY6mxTP-i4bGH1-CuBsF_hkcYJVSm5Ds64Wjv-SiGjnVtJRQ6NYfcKhmiPJ7LN5e2A5Obct6Du7lTszBDmC3mQK3UxeziF3Bb8U9YikGXCYyE_bTkbT0a7bTNhIG49SHjUldpS2fc6vg4dLjH3OqSVWfbwYu-JDyLsepTglTedEsNLWm8mYATfQOjwt2L1ytKOHVxXmFJW1-InvaZYmczC6yJ7eR2ta59Iipk3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQK4_sS8R9A3IEZrjUP-L2A3IHGqZytzYZ7b80w-y2LJSaGd5PqVzPdVlR5dH1pLf_wafqSNfa4VDu-TWSBYH8TU1CWo9n86pQIrsinyLNgW6YkASKu0tkpu-Ri0AFZ092zOFvZEyhgTJDOs91yYO-fXVqkgijXRHmZaR6G3E49Md_Dje_fU1952Pen7CeM38cTGV4YPUpvD4L2cLzNMUZJxZFuPCR1sEN02RBv1E8w2ABlpl1TTKI1i3ErQX90DnzwTSX5sIxUOvi10vnqydWyfAqiDhIgrENWxFS_tli32zTS7YTnmuDLc9N9Kgc717QyR9VFdAc1QmArdKDtsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7HzEFmq3EnnzyiRJYmne8ydb80gh3JJHwQTAxiUEb07DZBiurEFzQEOjHRYBAtb85dPCpAc5Zy0RTAZv7SD8Ue2YW-flLlrsMn4MFSjlz5EPpWlz1Ibxn_NB4RftUaSnNlT4gcfyzaGHYEB0_Af8fE6qaDxdOAAtyvTh2e3hrW8GF0y0IkilkG6ykNCs1qiOHCF9sUNtcCtNb-hF8oDkBCg6znT4Jc0gVWetNSgKc9Kll-Xk3v0eSbwkcQV73DYj63aAlziAY0UbCXX1kKdIKT_nNyveTthDlkNm6s9blq4PglokQV8qUa8_XQ06hFVqMblfoB5eyJImKFz3Driow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D10b3iieRwQ0DffS4_tVynw74HIlXvb9bM8wjLxSgVOA1EE1no_wpXD-rPN0SudTQLEglvvDTNLBISZEuVh0F5TQp1NADfRX_N8WOyfOqJMxIRiXSsza4-4bljZi7_4QnOC0x7wtTbDxw5IRWoi5qDfi3QW4AacP_7oEVEESHzkbF0y9DeK3jh-UNX4rKeBijN_yBLhKb9dyq0XU5ZyMF-ij0TtnbhbYrJKvnN8GRc25QNFjypDrMT2T2xPCWbfi3qVUCWwRwPCuJRNF5sOSJog16rEY_y58Z94jItTa45satJJIvC-rjmww5lAXWidJDEx5MehnKGVDjLIJUXUAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=Vsp9j9t4Wu9ztVG0r6OUCwFhjlP_lc3TGMx_nMNQBHtFv5GiK8dYWDptubZQKJ4N3P1VASrRr5T_-q2evfCn6l7fdvCBoVk6FZPXKMip_4D7tCT48RSs_ltSLx_TN-PKYZHOyfRRX_vFnbfhPDCw2IZA2ddQ3rU_lJK2HA6tqMiHhipvG069KE6jZVvWJWKHfvbTS6imR6WFl5FLlTqBsdI4Xv2xhrXK_59JbC9og0gmiQl0DB-YHQl0xwzaT3nqAvHAJ_t5u5OLAgG-b1sZ0f4z_JNVjz6pzsF5UNWoiBo_HGanUE8H8jg5Ficxk4K2NP_rVofREO3xw4xbXwQrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=Vsp9j9t4Wu9ztVG0r6OUCwFhjlP_lc3TGMx_nMNQBHtFv5GiK8dYWDptubZQKJ4N3P1VASrRr5T_-q2evfCn6l7fdvCBoVk6FZPXKMip_4D7tCT48RSs_ltSLx_TN-PKYZHOyfRRX_vFnbfhPDCw2IZA2ddQ3rU_lJK2HA6tqMiHhipvG069KE6jZVvWJWKHfvbTS6imR6WFl5FLlTqBsdI4Xv2xhrXK_59JbC9og0gmiQl0DB-YHQl0xwzaT3nqAvHAJ_t5u5OLAgG-b1sZ0f4z_JNVjz6pzsF5UNWoiBo_HGanUE8H8jg5Ficxk4K2NP_rVofREO3xw4xbXwQrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOBR4KRtfRzM3ISRNjlaoIqQUARPC424aZ1jquVafeJwNDAgRsyLBtr0N8hBG7bjBWrNhrq7Aka370BVdUZFYWi1bdtPAK7cHLj3nmsKsl2P1mOmrSpmSbNqIEP5HX71y6RJVxJgzdfKnv9qOF4yc0AYjsxnPKucZ8Zq8nm1rmo4IXsKZAzqPwU_QqTCsNFFlAP7GtRYY_4Fc-ckJwjsbu2vB1CeHE_pf7F5diP_EdHxbSzsbQLe0mP3ckKpmCVZE9QJrgAMhQ4ZAXOybTp53XKkj4DigMuZp2xPNhdMnjv5HsdlooxYfnMpBO0LRSv7jiFIYQpJpktqZJP9C-XE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=HfBUBTH4MrX_hl7M39-XfJ3oVfQRbx87TlWVIEnSvTHokC5mtDT4jBkXWgAMHqYl9-bK3BbViyswaQ2PcB2cLrfwV4RVRWPwgycGaLCjmDb9U9yJBrxp5kbQ4K2kHyAbhA08sAB_iErDH-igHu_ui-IiX4-Q6fWbzoLaueonwXoGpK6fntQM9iIVqhb8dJkPcncTTRQPfKf2e4dQGjElpJdOgeKE0Pdc6LWS0I7GzGbhytq1HqOZM4nSlmxacwc1VTLZf_s3Axph-ts2xhmJ56Pp6xoiZKpnRh6GiGHcVj4CS3NBMnopvgKOdT_21fyGYQzf0jddY053Vxl-__6uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=HfBUBTH4MrX_hl7M39-XfJ3oVfQRbx87TlWVIEnSvTHokC5mtDT4jBkXWgAMHqYl9-bK3BbViyswaQ2PcB2cLrfwV4RVRWPwgycGaLCjmDb9U9yJBrxp5kbQ4K2kHyAbhA08sAB_iErDH-igHu_ui-IiX4-Q6fWbzoLaueonwXoGpK6fntQM9iIVqhb8dJkPcncTTRQPfKf2e4dQGjElpJdOgeKE0Pdc6LWS0I7GzGbhytq1HqOZM4nSlmxacwc1VTLZf_s3Axph-ts2xhmJ56Pp6xoiZKpnRh6GiGHcVj4CS3NBMnopvgKOdT_21fyGYQzf0jddY053Vxl-__6uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcJwff1urnbpZoW6ZQYX-XbOjpXGeoRgbExcrO5mp8N8A1BVnscEm4dtLzkjJV2mjMoKnIPkLX0g2ENO-0rc5wap9YFyoqCM_DpeUaZejFvFDi4XptP-US_36I78P77a_D_UDWBDPhgQ-erM5ImgNCMVQEot6W8IjuaxQ9uuadhSiKQEDRd1PNFjO5_g3LSYWuZRtCDOThnQcVLb2XT48s2HMKUIO4LwUThuMVpwHP0pGIz9ZyrURp1N9YtoKdRqyrN22ssUVPC2MqMI2Qhgl3CQIHTfZG1tOW_ZTtMuqngnBO3tlG7UAp_RwXaDHEbFBRsj_BnzM7ONrM8kgrIZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YULPAd4kIdSx6hcKDUcBj8Wxyt8_l5g_11y3mnhsPAkyO-X16oxVmI8Pel8SVFegW5v2OMDJ3TO85eq69MSoqKGPkQIS6mA64Z5iOj7kqGj2WcaVDwWifp-b7C4l0JcmcpwJXOwULK0R4nJstXoFERWAm5lgIuJupH2s5WvUxnVkrHlqkAOtji0Tq1vJt0CZciY62EgxcGy3usRf5iKURYGqtdMzsBiHJAnZT89UeVLpZLjwrM7DpX-5TcrUzqZaIQbOd9WUH_ifwZKwR3Augr2diCe-EXBZefyFRSMtSg8BaKzfoEepsgrEW0eIVOX5y0VYPQtJeOMsGqp4QF2OWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2pz_yGhk153vaAvACQx3tAo44T39bvYq_kB7oQ0AxaFolPRRdUPJaJena3dGW8GGpXani9IAv20qi16NvuYOJYFMEfpDpAQTnQb-EMbCSsH1JG57Zo0Qk8rlIsEg8RUoqrLOlRPMhw2u6Lp6cp5FeMwg8sdyEVSOB2swvk2mYADEmFBiP7mumeDUAh4g0eG1BHmgaZ-swi5qFlpfiFSQcMJ-VyTOF4SaUXVy_H_A3DZ7WU_ff0GH29nujr9KQw_c5vSBwwIp0FQM8nFSTJRb45qV60aM5fsr21CHL2dowVpvUNnLAbaD9atJpyO9Bb-W3ZU9CYoVJP8esfB18iVDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmw9UkoEbRg2UDxFR33zVRMBDkXiS82x3dUJlbd4UQCQGLY42jlL44kLtYwLx5bdvaZJqPuvO3bFzjSShZm0rssTAvQ3mCPb-fJ-QF2csT6nFH4I8IvYGNMsdwJfsEvF2VeIu6x11RJi5DbzJAnazF97luSGEFkuIsQitGJKRsl9QiQxYnMhcU-TnEzj_awIaYOqPQT9lZU53ggA5tgirD8OkjAbH6j5_PJHe8TklRpzZlEl_ZyxteA4p3kcoEev7CCmi2pDbuHvpuUe_dmkvxpWsz7ErrQ-DU3tHr55civwAGV5mW9D5_sMvYho2qt4lYoCvz8lilZ1Uf6EVa5n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3j5uJCiRvYvcC1FmUoHB2h_ccls18hwocMkYcZeMV-ZX7pceZyaUITTfXHTHoQmBDre6PNpWwcQ6T3qJbtGce28Ud-VuXt0oKPJ6yutk2ObO_P_7qKJieDkFoh97HusFMxI55XxCfP5MfeVMtUkJKh_WC0v05unkuz65uTmFCLd9fBkDdAxe1spAZ7sajBTgwzNWCbvHS7l7n57Aa5IfwTb5uyOUZjEbMpOQ2egDAZhZQkTT1fQlGTRemH0-SiiCvmNR2U_D7vAau5m2b0PHWveosxFqi5XFw_pqnNZvql88syYcG7HkrCGJ20hItG6tFVUDo7JnD3HMGrHtxyHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=kw1mWEK3un1I3f8lPXgsITdGp-Ik1lPkV5ny4AdF5og65sveGZEhzfqw8qomFDEWZGDONjQMkAJcMfQD0zLc26UJtMTfiizGP_t7Gn3aANI-V-LFQdN7hv6ZddLjUJKU2UQiL3Zzb8mxJpSsmCx0Rj2wPK5MFBA8ZsaS47H9JJF5OR9TtdPF0F9zjrtco1S8n2yqCIgcRiC92DSYBv7yOxnLwULZHbMh6kvbToff-yI7fqDAgNVZVE7gCHkDEXAyfdhrXJAH5JSGkzH0MdNSjlPF9QCqmju18fySfckdPwQXltD82ZINnI8mJJuVOlG2aC720Ydd67cj7BPq7V9oPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=kw1mWEK3un1I3f8lPXgsITdGp-Ik1lPkV5ny4AdF5og65sveGZEhzfqw8qomFDEWZGDONjQMkAJcMfQD0zLc26UJtMTfiizGP_t7Gn3aANI-V-LFQdN7hv6ZddLjUJKU2UQiL3Zzb8mxJpSsmCx0Rj2wPK5MFBA8ZsaS47H9JJF5OR9TtdPF0F9zjrtco1S8n2yqCIgcRiC92DSYBv7yOxnLwULZHbMh6kvbToff-yI7fqDAgNVZVE7gCHkDEXAyfdhrXJAH5JSGkzH0MdNSjlPF9QCqmju18fySfckdPwQXltD82ZINnI8mJJuVOlG2aC720Ydd67cj7BPq7V9oPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_mLIARdxk5Cj9ZUzNnJ3e3TWREakOMm5Cc59lEKDIpN3ZCsItjU_SsSQ6a8sHV-eJVAzPG6XedCfA6DesPD38QQKNRei1PuOXLOfGBOVvaxCljtGk5nttw2XXkmS2jOHLqVMpqxe1ARwVLdCR0aWYYQLpuWIpnLi0DDjUH9mvV4thvirknt6sKiHoTuGMQFZSnB259V6x3JmKIg2l-kTK8w28F_Td_S28QeuUFA-b_EhRma5T0Mt88BHRVEng-wo2pfPPCity4WpxRi7rC4ukeyhe-clIemtRDIzNIWC5jCFmrgvsVorvB169JHfuIkLnaf_Vhrj-apbB6hO0Y6Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHATo2s99SF5wLxhGxcSM9Mhax2QdCFxc6tcXnDBWRPEpekR55dPnC7dE5JgWg-2ZktDDYFJs71RQjGQm4GIS8zGqAs_CaspaFJNi8PlJzttbGTQCB_-Lqthzp-BXqAI4nuCzLk9vifvRCuMhePs0u9d9zmHKbS5IgF6r58D6O80tq9dkkyWpkBYAVrr59tEEShaOl072g9rxvnb8DtQ16JDPYudUpxckNFB3z818M2dREdjFLpKXRnw1CvXWCjuqEHCoXTvyQLCy9HYLuT5Lw8gc6Pxk_tyrlCK496eiHJVzIWdwLxdCsm1Cq5nRJIQZny469OC2CXPdPTJjWbLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sWAJqTlGPYALuEduk_dCtzr4dBNP7dZYtjrgh7_q2XA7xu1cS4FGSQCJfXRdBI2HsE-lG_ltolzhFbflg2L1WtGRq5g65rTqxzxjQ6y7UcG7ysS5IgrQWbULQkxMt1qkx6BeHfZIsrgZ5wAA-M3MwKwr--DDJgrwYsigNCW3DWQdH_uosiE1XNk69UvEZ92_p7X0X55T_h3Cv31hsGsmxtVjsYjDcUgxU7OwoHKwQE-N6cUSaTE_T6fXuSTCHcqmxG8qQKY5T7cb7ONrPCocupQ80vdQi3Qt7znLw3At0n3uDGxqflfkf8FwIoXZ_y4_jH2CmzWVb2q9w3YwiWMDcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sWAJqTlGPYALuEduk_dCtzr4dBNP7dZYtjrgh7_q2XA7xu1cS4FGSQCJfXRdBI2HsE-lG_ltolzhFbflg2L1WtGRq5g65rTqxzxjQ6y7UcG7ysS5IgrQWbULQkxMt1qkx6BeHfZIsrgZ5wAA-M3MwKwr--DDJgrwYsigNCW3DWQdH_uosiE1XNk69UvEZ92_p7X0X55T_h3Cv31hsGsmxtVjsYjDcUgxU7OwoHKwQE-N6cUSaTE_T6fXuSTCHcqmxG8qQKY5T7cb7ONrPCocupQ80vdQi3Qt7znLw3At0n3uDGxqflfkf8FwIoXZ_y4_jH2CmzWVb2q9w3YwiWMDcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=t3KK8awuCZ13SBHMXfUWTe75CHwTOGDshaXfQGgNUXJKWNgLTzNJuIFKcxA_-1lZjzvELiS-u36Ka0WThJxnZK4HJMTLZNSgphgq6ZHMw5XQOOeXL7YrS637pmpCCKcIvt7dehUX223vHvGfwhHl6VStbN6U5mrHEzJ4b9wL_V6uLUy_btTDReGZvtHFBKZcnKiqAeVu7ZFoeQfl-Ll-PX5_f7gEGeRdpXQtgnwv2GEM3K_n0M8w2AlIjqs8AukdgyKciBMMXOhCa4xEKVNh3F5nhNqtazKv91wQS71MTiilGytn2dpNzqjGwfpLWlrM95XqDxLT2NOUOdUWg0qBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=t3KK8awuCZ13SBHMXfUWTe75CHwTOGDshaXfQGgNUXJKWNgLTzNJuIFKcxA_-1lZjzvELiS-u36Ka0WThJxnZK4HJMTLZNSgphgq6ZHMw5XQOOeXL7YrS637pmpCCKcIvt7dehUX223vHvGfwhHl6VStbN6U5mrHEzJ4b9wL_V6uLUy_btTDReGZvtHFBKZcnKiqAeVu7ZFoeQfl-Ll-PX5_f7gEGeRdpXQtgnwv2GEM3K_n0M8w2AlIjqs8AukdgyKciBMMXOhCa4xEKVNh3F5nhNqtazKv91wQS71MTiilGytn2dpNzqjGwfpLWlrM95XqDxLT2NOUOdUWg0qBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=uTesLBu2oPHpUZj1GDDTwK421WbX1Ny-XoyC3uvhYZFfQIEe2UvrU2Iy3plnLwhjcxZ9o7MGdyXXSRqLohyiEJv3NDgkRi6fCpV8-033fF3JfUd2_bpskxWBmxYnqfFjAorNUpz5umWnPlCD1awPqP3HfJu-aWz6S6d8S21ekF9iZZq32VOYfXURpF0iXtA8Cb2BXrZnEHp-7nx6_flbwGSHOyab_2G-1KdnZXvktYKHmDSu5NzLZ9rTJxJX9CB23UUY1M_ZVXt3dOq7YbkwTgvHDcoDczTRupZbasaV0TmScSmp6ua8q5CdEV23rwIi8RP1QstnulnM3VqcX38A3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=uTesLBu2oPHpUZj1GDDTwK421WbX1Ny-XoyC3uvhYZFfQIEe2UvrU2Iy3plnLwhjcxZ9o7MGdyXXSRqLohyiEJv3NDgkRi6fCpV8-033fF3JfUd2_bpskxWBmxYnqfFjAorNUpz5umWnPlCD1awPqP3HfJu-aWz6S6d8S21ekF9iZZq32VOYfXURpF0iXtA8Cb2BXrZnEHp-7nx6_flbwGSHOyab_2G-1KdnZXvktYKHmDSu5NzLZ9rTJxJX9CB23UUY1M_ZVXt3dOq7YbkwTgvHDcoDczTRupZbasaV0TmScSmp6ua8q5CdEV23rwIi8RP1QstnulnM3VqcX38A3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrEHH6YjefNtClioQMmupdY7gGVLg1sz74KXxtv2nstyKbUu9COW5JJWgBaszNKztzvMWo9-6LWyeilaoqc6AqpFERcIqTAzcE4yPtSg-pzD2SFYmlKuzbq1UW9orX4HnXgbOT-8JvmYHIKCiaUYUv77nqeatiUihpzs7hNT6yAkX0XT7XweHuin_0QOYfReWmwcTJjw6E_LN279RKyhx4okNpc90y3vBEAvP9VtzCBkzFOTYZvtGjnsJN4NnOt7sJi_bu1PAeiqcqz-mjXpk_3Z4i7RNJE41AgnQqIN2x-GQ0axQ4apNGLCX2GZitLHspEIOkG2Wpcz4LzRfl9_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVW5keG3ZZLkcNUwPaeLgQxlsaBNxrSoMcnVh5kWLstF5zdpRvJmBVyGAqC6DK7MU5bNsa6rB3ZMe6viTDjqHZ2BayKghLlpkBe7KRUTnc3jmCXTqFhP9GgA8KPNewN_yr01ZhKlpKAE3ZkSMZoP28Fx2Lw263Hhfk6A95coKHMpghN91AfVQltuqXhLBx_9Z6wV09KlWAVtoxK_hR1mxKKmsCEXWYFclxrzd62TGCCVCOa9NP1xlRGAboS_wE6h3Hbn42gK5Lvj3xlrrRCePq9kx_znlQgUB4PzLKUqKTENWtZhh6Q8BZTA028MPCVF0DfFva2Vc7FFvWAe-jkhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elQBjKXT3Sd7F1sI6N-VmSUfCikr9Gk5qFyGZNGqr88dafYiu-_Er8GBeFMojH-5X5Su2ZZJBksgfvKgsqIlb0-ryKVp0N5GkjPXklzGJCy5vq_8bgOj9KbjYOa_bA3CQyPmdhun8-DrKCLnnXMFEw50kXav3asvl5d6XSSt5_JloyNhZXqBPQgrSoiYHpZXrCzeSYvyk8nW3pjqmXhenFRnHLBV9-ClPuFJBrfrUZsgszGJacCXihauWKnQeBKds9KfJKKPR-ml9M_4GwYcrXY7-tK5SU7ysWfU7xiXzsZD94pA5cgTa655q7YxmREAb7ultZBoEsAiVYrafqEvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=AMkB0la0zXaFQ4dBQ-0PGFWpS6mQHbGFFQnlLooUofCQQXa9Mof0X2homembnUmUH5NgmZt9QJek4PpQm9wx3ohS2leCeFOceFQQxMBK7CZQJd6GZZU7G-0Ma82UCJp1NXcwymEubxi_vPncEB-IycLAbkhsA5yPCRaPwZVt9vZUoIBilwx8-5-UeY2iMLRAHR9LvP7Ai0QNgAjUQYJx2OAdTdFvpMhNVZ5EcToexvYAQvIE_mJmO_RNjMs6_mPnZpSQUbe01PnB8mR6X_DrYAOQAsn-C1Q5pa_W_xzZ6BItXcVKH8zQMbfjl0YsNRxPRIN_eEoitCx3_bFgOL_hnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=AMkB0la0zXaFQ4dBQ-0PGFWpS6mQHbGFFQnlLooUofCQQXa9Mof0X2homembnUmUH5NgmZt9QJek4PpQm9wx3ohS2leCeFOceFQQxMBK7CZQJd6GZZU7G-0Ma82UCJp1NXcwymEubxi_vPncEB-IycLAbkhsA5yPCRaPwZVt9vZUoIBilwx8-5-UeY2iMLRAHR9LvP7Ai0QNgAjUQYJx2OAdTdFvpMhNVZ5EcToexvYAQvIE_mJmO_RNjMs6_mPnZpSQUbe01PnB8mR6X_DrYAOQAsn-C1Q5pa_W_xzZ6BItXcVKH8zQMbfjl0YsNRxPRIN_eEoitCx3_bFgOL_hnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQtxQx3Ng0zvXaQkDQZ_JCd6Ldx_BYewPzbcC-T2OG6fVM9n4rgEwE6Al837wJoqM9SoWnGb_mZ7Xk236-oVi5u8yAyPAlz2ejdu5aBvtPfOt6RBfrIwHtpX_0RIliI8FDkoW8xzLuYzz9LNANb3mD3_d4QJME7LCzxpS1Sibus4-JoqJ5ms5eeSL9J6HBa5vgXxJkcraPAv9VLwuOtSZq-wJ9n6RwLHDNtjRUhPULl0qITMgfNmjIAB0d_c0IBLLvMvKIIAFfRg6QSQzqqSTG0bA26yYPats8X5JaSJVGhwlsGmc0dKEWSlc_-rjk-xu2MXihMJnq1OG8Cb71NeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeFNyc-vqQW1qCUv_BdaLobcEgZ8KSZt9wYQpAB6mJMzMcLa1s1HaRoM4kD75fF3FoUCSbUfrKuxc9l_nDk8cabOYiHYx_3ek_CyVk1z0Y68xLI4uYMrbRLc5xDYSCt4EpqPCHV5HO9V_4E0Bzx3fKlRlD-jOePIbY1eLsBIoHe2v2WHpbSgJLyQpryya3NM1lSsjulBcElHxipG5Pch4WFu6mHvdZ58A4lLIaBa-HKDswdAmShgGmwFAvf_fI6Xbb5r3w2OEeYlwiuD4A49g7xEBdnhbBu6wZyfH5WtyE3HeEKOGyGC5BNwvLzJzl2BQplCXzwGszTAM8KMsXkaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnaGJN6nt3EbwZnAtZDqdomyMMhF4ehPJdkF9Wy2zHtqC5AlQAydevlDo_RatGdgD6t1pmHE_8Go4I3IkQl4L9QYatoDFQViAYHBg1KHonkyjMBjhlGcele1sTTG_iG-UIKev_2O69IvFdTZ4i2DMOgWWI-EX245NNjlcx-3nD6RUWmkUrAOuJ38Ha8fG7X1XVwR_It9z4G1uQ79mhmbneqBSxH7GoDEh4f3i-7bR8obK3R51BQe5Tf9eAtNHHDnJJE3is3zJ2F8XmGzgJIkmilmcq77Yq9dH8AxMZmjsykj9E2r9AB7sttNaZ9FKndEH1FgG_cX5vVv9fUhxHW8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRD-QfXBnipkBnoPK3OGOkGXohM_LpMsk-aFpVm08ySLkUFKs91ut9cYTtYXFEiB5qdBK6qvSBpmrsanJnUb0KusxkxqKD9_jQRp2KjzBRYSP2CjIwG6y-kJSA9zGKjcTMANvpBcniFDy8wtSb_xzagKLK3D0M2cqyjHieSSTXYn0cfNVQKD3o8cEZZPulD9LGLDAghxS-B3bTLBsUSdSnZAscWo9ppEUQBXZ56rVRNI7sxcxcYl_PG3TzyIshXmmVvDWYFkRTU0eMizWXlT6Hv-Vt7H5ZhCH1JI91VG8LS9bOuR2XH8KXpH3azCzlBF2gK5pbLbPtSFV1hWX2uBnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seaHc_Fxtcizh1du6-DtllpN0BHTcpu01f4wWvDn7tjXopZ61OV4iMifc3bRmKyQoamgtV9CTeMLTZ2Q2XpgkSfwYqsWMLmwfyMYP6e6BRLnxBqJJv-Wq-AWsLqpbUAH4vh9JdD_Cvrv5Mwkd49MHRPRyv4PMkFY5PgaClZUTevrFhkGLByHKEzyCEEVHvMyc6BidfAUM2U-BuGBHQ4VTcqQNECF6747aGG1PcNje_2MLSkMVbi6xCxViYJyQTPup2bXFHkNzuDK9KTlsj3aRls13mx1s05Tgq7ldJLk9jLrNZJvgZ28ihk5gIQb0xfgEq6ws260rAebU_WekAX_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojp1kz0wFfwTzngpYeJn7djWLWcMluSWmZNaz_r7Fk7w7JanuyTBeVHxj5OUsX4qf-08eezfitui0tPIPjvrN2FsbXl7oDPjbOg9p9nzuAWyjE-lrpZVRLqcdRBm-jwt2cnKthy8fqD2Rpx68ttOndtzeZ6rTZ6E3_s8itKhogOgsbXHV-19omD2o-INIr62-ohwdodleq0yBzvAmbetKnQ-WtMeB9uVcsDs0--piVw7V238HNHUKcgkxzg1Q-geD0pHOoe6AZ6QuOeaYV_L1KG0gkPMUjCWRBey5d4ghg7PUKqiZKWcrC66I0aIN76EXrvbasrMRuw1tLbwXGL2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUKgizRudzA3rSDwiaStWRWn0NJ9ojBCvwCD-J6fEBpJENuUYdaq7EPEuX8RZwCIqAsAvNorTXa9_jYeaCw8pmWG741iRRwpDSgFXOt_WWLIg1uaZwVvapYDid5seBemPimOm1JndcT6B-zVSrYEnT4VLhObJUSyPuckeiWfb-rJ-29a-lNsYPXU7mrErRJLNbyEyYDMJckWTEExTdwDDW_SExKr_Dq6rsAVhpCusXRROquf_FAxmLJlGjUA44QyrGE_LkHEEm0OTY5DqLBk5GQG-vGK2FacHs5cGL_fpGa3juvQ4MOYiQIP_AhaCZVkjOxRp463EVS9X3ueCyN2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSZRM1dO9G2qaJ-lZSenDetwuBOdFu-sJv2KkaJBZ2nWKask0NYNuftF46DttA0BBoJiWzQCzeMLxU9g-Og9qFmaZxwo8pNTb_sKHdG_QzY0Bt0Tq4gar2GMjBoDv4DD8as6we-UrYWpAWM2pCTNnaK6YaqkPXNbeSMKfjr-pl8IOiQ50LDUeXmrQLlMQ8TERHAt3DG0-Faa7VfabrYdhD51wPmzzAMP-Q_idHZJYL7S65JdaYENppxhHv-uP4DdpHOh7iLuMK_dSTRxXlYQQPmglfa-ioiTzdrjc4nPTpxBHR9wO3q-qiLHySEPRCVD7U-6i5klLFF3Xp4KdXRWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=GKeG7LuS05apfeuzodJkfLYYJ-eipJ6FLIl-8zU_c01gntLVXFEO1QkcZjhzdgwwS5pPtJtht21rguFThI1MtbbnQw6vzOQRjkGOvimf_T5p74S-KurLUEatCahSr2HpeNu3CSSKEF8HoZ9zlSgI1TRUsBrDcGzL_xzIVEUHyOdc-dhZO7ZFf-OOTpJqx3RtfxjoZnl6RwDXlZTjOAoCT4dwmyekleDdD18Bj0JlaZszYA5sqlB0Tz-GsCerlpmljl5SS-YhmX2-KligsDrR6LLov_7tdg1xeNr1urLb-wk67p8_Qaa6w0QbX0qeYm1knq7AUdxZKq8LIKnkG52uiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=GKeG7LuS05apfeuzodJkfLYYJ-eipJ6FLIl-8zU_c01gntLVXFEO1QkcZjhzdgwwS5pPtJtht21rguFThI1MtbbnQw6vzOQRjkGOvimf_T5p74S-KurLUEatCahSr2HpeNu3CSSKEF8HoZ9zlSgI1TRUsBrDcGzL_xzIVEUHyOdc-dhZO7ZFf-OOTpJqx3RtfxjoZnl6RwDXlZTjOAoCT4dwmyekleDdD18Bj0JlaZszYA5sqlB0Tz-GsCerlpmljl5SS-YhmX2-KligsDrR6LLov_7tdg1xeNr1urLb-wk67p8_Qaa6w0QbX0qeYm1knq7AUdxZKq8LIKnkG52uiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqa0nBgYCtpW6xS7RVu5yjusYqQMWd8WCAptThUfntJpmBE4m0XRV-kW555yf33JTvtywZX4w2kKL7tsv9_yha4GGUDSSosHiVq99LKfNJw3BTwrUZp7fQ9u25ViU1a2kxnj9_LgS5ZGPdGL1pWV81A71vuphZ0RS_khgBdwCbeXeEa-Zz-3DjQsa1bdi9ULU1uMjS1aE6c1a92G3dUEY2wjCbImUT28SCUXfRzPk2Gvh4pMn7gNJsW0BYV4BS3FR_erJeYilwPF4PyoiS8EfTeVFukXubTN5C7XtpE4qpIP8OdXzNzDoJORKtLlPJAZCe23EIr3PEHQxx67CHaxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isDRubeeGg0yAqzu5cRDap6A5P3beHCTcdDIT2JILGbY1Q3AIiGwDbB-3IKFx0YdHT3xAB0QInW6sedgaa8yTjxlBSxEJ6znhLezd4nZDnLN6cWR4nB-hpdSWoLSSeWK7LVy4GFDseVuxRZxfBbMsuraqh3BsseL03cOJJ0Rfyp3NrUr9OyajQQ2cpeGo7k-nBVt-pQqfaEcohXjqxsCPE0mGBfb9hF9yaXlD0seTRYstNDuYeeVLiaj_dKQN9Cyj_PI4lJS82zHv7Jb2-lVbZgjlIELKdJL4wUy_m3cCG5DS4dIa3DFcEalGMa0DEr-c5y3dWhx-R0B2xfdImxa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly2M_4vi5hG5N775_5U0SgjSWd1iAbF1T8hs7VTBwyxL1MVCn7xelwU0wP0dvieDs7WJJCPPIOucoNkOr3MJEa6XN21qROp1BF2WbieDQSCO970GnAsvHeuqHgMTn0foqa-M_H_iCOYqKDwnZUFV6EgkKey8xD8q6AN4aMH3YTn_8Au3P2dC91ekeu80rGmJUOnY2r34JmcAqf9zdIYU6wgb55SWXzea4_PtC4kjEOY07BvhP8N6HkQIzXBbpVCRFse3Jd8KffDQIke8liQzRsUzA-DPoOW-6fDBEH61cyuQ3SjPZkAHjkitLAmIu-fwTY5No-OPwv-8QiHArcYwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHSo9941TQhusW1eaKVJBv4-muhPXsCFVP9UmyY_F7YOYzMp0vFKTWQzRI-OSNXIXrBMhogIgX3LbCgy6V3Y8K1kyOFgFqmRVdfjsUbs5ewjINvaWX0NCg2WrbDOtvNNHCBowhZ9NsFCrwSRQdFTsBQtFSbk0JMTIZqzH_sj1_4N0VyBB4blfxxGY0QecDd9ljYziNWmDO-9nBAfUCvaSDWHNEuzG2-322XKrOvnSVKkfkUueAdebXbHIMyOd20_zQFrRKwXKqEIFblzV4yuXdAuu4TPVPQtUTQCfMSV7DgRqVEa__LqoDZYrGW8J5QEMZkcjjJqzTFZ2mOC5EEVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjjTUugExd9l4_ZfW0w11KqMaV1MJBEZjJYbtwYbBLNV40LWz-VEU6DUKFxmh3LkN8CUBT9iYy8aXhWPczeIStt6xyrUmE-jCCx4EZxYCKoQtkteHvex01Kq82SEyxMRCoyMuXy2FAn_COBlpJdPs9nX3hYtEjqR7W-gdT8hi9iDEvKbrkNCCdZBA9RDR-H4svGnhXKfw8_LcAB6lagtw1tItXr-44a-xHvVWmpkqj1h8f7qv0KiSZWitloOAJYzTYKMeOiHTkB89wBtANZt9wtFM_a6UkjhXMixdE9MNLckOQNfF0kgq9HMk24du6Ki4Ghvg_GCRt2zOYInzDMfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/domTrCs4J3PPBfS0Pc6WGjhTQssvv8pf2AmteLKeJv0vlKt3T6UtDt9Jfd0HqjJkTPvPydJOHkjDABBeCbqSxt7M9CDbajHpS-MO769eygOUkDlHRoTNW3QO-hBPgSNSOGfrgp2gABsNvE7teC8WmyZQ6wl7LAhsRqVXQ6R3CY18Qmbge-l654CGqLuwtrnNAzzWKRL7WRiZ3sj3HbSSNfM7bTTJDX_Fr5cy9a6bMMapAoFMkKf8raRym4lErtm4a5X5CWLHclVL2tegqzkY4YaxMq0y4Pjs2-CQU3ANeutX4TkgqTgZJHhQY073NHsV5M9MM4I7BOunBoECT-8Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1b1TV5yC4uL_nWy9VFdvsyHNoOriPRjC_yTDpG9bTH06Op__IVtScHEFfsPgW2hAY9TGPrZHaE175OdV26wpS3myRmh4yOIELc-9wlSWnaLZ7tSbPk8kHlNlNuBGtB876EDOPiEyb1t5FBi_Yr3KUX6tbSzPbzgYRfYtre6vibUuiW623saLb6CmoZ3H1TlfuU_Gz32d4V0fLnveqia945pBXaBiEESd6gkLTHTtjQz7xYqZk7flymBoOwHvB2JiMqAL40-QaCvi0G2R6Qa-Ypp27Ddf9E0rhEOSV3vhc8no4gdCvU3exBbi2nQTG4ipyvgi0JtHy6bxLNo4mhsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkMMo6etS_Ri6iu9cEIFpPN0qKrpO_7i6hclk1X9O-_9gK8jbzhrkw9in1SX5KhdRtmMGT9LZ1BtmXRJrb5UkmhBqDAb9XAswE9pFYCUi9y2AVV7c1sAugAHJ4cLEZFKF48hx84kJ4yCVL7BL_PFi07LgPI05RMWj8aYr3fsCDyOR1W9o2gbOgHsb1uGz15tnv4NNhVrp4RC7cfVCiiD1xEs7KQdjncre1AnfnQo9LZ1ifhwcgC4GhBEWLaS2l9nvphyNKo02MJPmMt5kzlmbAEN-hy-BjBFoI0C9MjdEYz_phqfMf9_EQxKGnwdLEfJ1sZtNSb3mtS7H-VhJ9m0Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fymANvWQaOYcVjUqN0V1PAfN6Ehe5KaSoBLLJd4T9HhIDyPwVSjVdr2hh8Ej5peAn5i1D3itGl2H4xZ7w1AOCem6vNAPYkpxuIhCF9aWN4JBAvj1ij40Yx2kAAUN1F-mt26UkCBnSOusyO0uEhUqAz2bot22nNusa0Orz6Z8muHGrR2nNXbLIoAosyIeD8oCOs0xuKJQw2STU7ZqQdUetjnj8jx2EsRFwKgI9NeKAWjcyU7I1khuUrsr874xkMc97_sulWbrNqQYpoUnBcHSo4rOy11eWlXWpPis0rgUOsis09QpjrDRI39LjfTwRpp0w6ISdL8PWoFTxwWyIQ0ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePCAV6OWjgZHsgdGbbq55MW_Q6ZUTdp5vfWcZZQuPj8fxiiyBd3tWUwSwztL--pujcQI6YHrLFJ3VDhP9lvipqXi9Yd_rAfq_tnqRDN6dyn58VRz9CWc9C7-0tM15sN_x2ThOmUK_X5v6LTZJEjbqV4_iMyzHoDUV4R9dTKR-QuUtcsCKV2PG-C_oGQix7hP29WMDHFkRGORssk3nhk2IG3fplOl8k20rHlg8-5Lo9Yg6pwhHahIDyuVq0kklmcvZnJURPUvScFnESo3SOa9Cp1tyiQzFsz55Sj15ynxYhzBkIhyYcGYhC-PntNX4UWX4jGt1HJ6_2Wcmms7leZJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=FKVgsmv17MjRRmMRFhgV1inS69cBRxHXQ1mhLVcOmiTGviwBIq6MvHGjObS8f7nDKA_bXijV0ATai0xPdO_tRFtkQ1lH-A2dIjwqWx5waYkV2Xr72tyjbmTY_2FU3xFI1zjs5EJ6jKyNDs8s6fNUWg1QSVmircJEvU1qm3M5O9DxAtR_HGiPFT8LgOFzl3_oTn2f5o-3wAsj0CWV1zHbU8vywYmQL1TGCo5A-I0XIF0N3m8Tz4jE2lVv0U-bxY6dZcF01GxLUbO8v1lP9LNDDuWXrDhR084xsMr99juyFd4VzbeVyIFvAnAC-K0Ib6kSmXkVy4OpKThPPGUn9xpDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=FKVgsmv17MjRRmMRFhgV1inS69cBRxHXQ1mhLVcOmiTGviwBIq6MvHGjObS8f7nDKA_bXijV0ATai0xPdO_tRFtkQ1lH-A2dIjwqWx5waYkV2Xr72tyjbmTY_2FU3xFI1zjs5EJ6jKyNDs8s6fNUWg1QSVmircJEvU1qm3M5O9DxAtR_HGiPFT8LgOFzl3_oTn2f5o-3wAsj0CWV1zHbU8vywYmQL1TGCo5A-I0XIF0N3m8Tz4jE2lVv0U-bxY6dZcF01GxLUbO8v1lP9LNDDuWXrDhR084xsMr99juyFd4VzbeVyIFvAnAC-K0Ib6kSmXkVy4OpKThPPGUn9xpDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9DHOJa9zU0-cL1aRgKGfZJiuDFfOk1IOLFy-tCXeXSyh1_3-SbQLtxaVPlt5bBHoeN2uxD5VSkQ6odpixgvGwTB527MgEcOLEih0S4XMfeAkc7Bq0kc_CBsLozFus4l9T8qlUg2P0Htcq_VpP_kLze-BHNEqtE-57kWlfgRtQu25f6mrKMKe02FmAcktJJInjIw7rb5rOr5XrLyIYLfPKHNiEFFD1Rdf6zYfEO2EFRX7Ba8vpyF7iwfY_4RItoRLrqUfiP9lBlUZXqG8eZ5z1RlfGI-qCX4zrk6g9oqDrD8De7DXAfzFSLME64c8nf4fIJihs4DSC_w8l2ckhELpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnJdx2s7sIT9yDNum7fnCdJ6QHKhKX-P0tA0FrKcdSXnogVchDuSnvhv1AoiBrA-exsEkNJLhfrWgxU8VbwHib6No3f5so-L_87-waKgIhv8MvfhhN1hWUeaXYIdextp7wogQW1QIJXlHrqVCPpgrzz_c-qFArGxCrXRERXmrdlq72JM9A_W6b_caLpwtRv9E-5O2ycY1_gLIgkGGClkTtJ9qy7QGVMugM88i9avkqTk1tq3raBgHi6eid9CGTqUByBiU6wVkWat9Ohu5UKb6aD47xnGrYQBfuq-Dl6wHX4cp5JcoNUupoxIYe4WvGBRWZYtYSbacV1PBGEB5NWPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4ZUoLV6aBtybN6MVXCDJynk6mrPLXJNQD0ZHUVoNoUjr411J6woQUrOOavyG78QNMBcHAyrj8D8WrWOgLCFEbcET5ww_eVXvajLfmP-SsY3BxLIWDn0DLYoYrQWOc5hMTv3_gNAWL3RN9QuNs_j-Wi_m99I5khcanZ-zwIeO3EvYOjpLVd9MAnyrOvjC5WWARA5FI-iV4H1c-NXwmXrKElEZfxVVaPigJTIUBmM3eMUPudlg0qFC_XvG0DGxTZ4rTzEcgQsLomRmUFTLNv6bMUphWfv8VBx9Labuxdl90y0O_uJdGCSFyhcr5FIr5fOO_DC3aFRy5BJ6wFhmzhUBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFx7YETH1sqMjjILN91UMQP2n32pgTliZPd9yFaXjxa-IPsxEWY6y1pm4UI1gjBt03CYTpEoW1YVIrKrnY8fyu2U8ctNRYaewIImGbz3rTpGbfslZIKxzfLkxYgTxELMjdlMIvGj7ZOrVEzT_rI_K2es23-60xoYfXLpkq266G6b_wrLRfW-Obr3yuPRrnYh96XyTxGAxsbTGcF6Uadc9cb6CIT9d4_4_ruPx3pHoQLHAwMWkqCIxgPnSOWWUa56O5UJSnSBXPsjDXEDFTPkag_1ABjAz9NDy1xtKl7RFIVXDCzCAx0rt_itrMywgHP7S-kc_EHATa4Loc1TTvbcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj4No7oLZKaxlSzcmKcFz_MFcxOTE_3cuJ7LzTW-8UQzKmS_X46FI-jV4_jNfnG6Jl3y0hjdSCvJhsk6mW_-MlGnNWz0sxSInqogA_5RnUDhibKTUqjLnAJFQb_pFLPmapVHDjc2D2zCBOCfCDNxXnH-gfU9llHWTNGNlVrwOD2Yb8qw9Zy8xnXZIi0q8oHMtczDGMQjyDQuhtoB4gHla7vviNwIPXC6Z1XzB8k2sTuApCd3UPZK9usa87lX-iZGLq9cfUKJGwNJ3v12RyMz0yDOIQfYdSzYZpEMvzntZmqpl5uL7tj8tTaQfFrJURQmM8e8Qim5dvrrGej0smAhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=P5jVCkp1x_ju6InAcf_sDY4Elohp8kEHD3Ay_scXbhXLVImcp5oxP5PNjSFe1zGueBwbf96a5FgtRMZgPqmjJ8MSxt4C28EKf-p_rX_VGPhlRBOL1x8kXmKaSlouT2fQvDIUGbb2CLOEuB5jexB0M9QvsSvNULF8hG2lmXZUHs76T56l74IPuPIznWuQVSnaOdfTY705u7NQ0K3ugyMrgYaDwWfexLH3JWENND765WOMAek4TEolezFq8IW6dMU12Ck5sou07JS_wQE9R25cUBlmmBc0zxZfl-jzhQSYEc_07PpSalVvNC-v-9Z6ZYuKGRBIV758tNE4XxEl81b-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=P5jVCkp1x_ju6InAcf_sDY4Elohp8kEHD3Ay_scXbhXLVImcp5oxP5PNjSFe1zGueBwbf96a5FgtRMZgPqmjJ8MSxt4C28EKf-p_rX_VGPhlRBOL1x8kXmKaSlouT2fQvDIUGbb2CLOEuB5jexB0M9QvsSvNULF8hG2lmXZUHs76T56l74IPuPIznWuQVSnaOdfTY705u7NQ0K3ugyMrgYaDwWfexLH3JWENND765WOMAek4TEolezFq8IW6dMU12Ck5sou07JS_wQE9R25cUBlmmBc0zxZfl-jzhQSYEc_07PpSalVvNC-v-9Z6ZYuKGRBIV758tNE4XxEl81b-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsepHU-SNh7JUC2BKzruY5-hNB6Xg9EE1j3CKKXQ5wVUMEZITlp8Gv2XRn9qaY6XAdBu_fPQpBLI_YGbfefVPHRQT-Y1LcOZ-jCk1u_Q4RTHzsvMU_iEBrI1kHSQ830yaZ3QSuOnYLg7lG_D2tTjU9mHHyAyAs_uzU4zcOMaN05J7X-5ZkeLWJOZpbGEnd1_erC6zZhhlxW_S9oaHM48Rr5P5ATXCA-1NSW-nXE6EkS3Kd_-51UQ2Obx89GK_jM8YePO2xbileibubvQae4e_NUSHYDSKypQoLHs_cqTnLy3lVeXqN2PBGecXRMBB9-H4JMn1q5jRau_WCnVCWIkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53x0oFZ1nszx7aVzwR2Kx4RcoHK0u9TgfYK3X0d-ZxFvjlHDCrGvwL_ky-m30PirO2suvCC949LA_kOaA1mgScS1uZETXi2K2YSWbLTARWnYU_3B9DFl8lGFJlob1A3NPctFwfqvQV6vrj3gsD8pIvpjB2Bt-ESM2S278Aq6Hp01piBv4p2qmLlETpErMkx82Hjtau6-j825NwQDnij4TGzhNtV7ZnixNmdfmpRL-LP1viP3wZo3-PcrSlaV5b7YhZUq02LxVCPDTzovZFxWO5EHgtCdF6TPqCWAGh9To37lUT49P2IckUc21nqFiNsSvGb_g3NhCrkc1YKejGgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpAQ5Y9UKFZ1mfl6Kbu0UZiOUZxCoThJb5epDIQihIP67f-0jIyGXrGY9HS6ahuzj0Tt2WyOxQ97Jy_PBAb0fhKwat0KZlgmG0tJb3YtZrLeNQzuZxl7TwS9VEVQA8oTTiltqQegeaVop3SnmX9W1_c62tilK1FooBgaPHW7oiaueuMSVyH8KHLgcR-cphtvPzzrgG-wXXXz8bbORlsO-zp1a_5HNaaJyuqzq2lOS-0e0Ua97deX04YKVlqrM1ve1r0v46ELhV7vaR_fUhOYEIU3oOsLQ4v2IMO7dOTzSyzJD48EehlYzXTPagToaLAqlqas7a2p8j-R6Z0Uo2Wx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=txTNhXzqpcahesVZCwYzSk_8jdFUUWypdbXgck0bFAo0d1TjSPIxtTzerJWsnecegnWwc3r_0o1L3VHeT8EVIeJXkmQ0I1FjDeLImrVB3PjWgsprVEReca7bycScdIXza0WYQISZYSqCime_Amm79hhR8Ie2TiGyEVaDPaanXtjbirAEZSyMg3B_wV4KFO9wBEJnfIe7RQVCjwNU4Sv8kN4kPwYu5zpunH2e8IUHrT1qez31vCJ1ctgoDJqVc1NaIlRmAq4Qa90DgeySRTVfv5ToTHJrHr6yvOm4SeJlgUl6q-cMOmQ9eFIQ_STGGW3vljlMt5SuuUAtgmhPrKOA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=txTNhXzqpcahesVZCwYzSk_8jdFUUWypdbXgck0bFAo0d1TjSPIxtTzerJWsnecegnWwc3r_0o1L3VHeT8EVIeJXkmQ0I1FjDeLImrVB3PjWgsprVEReca7bycScdIXza0WYQISZYSqCime_Amm79hhR8Ie2TiGyEVaDPaanXtjbirAEZSyMg3B_wV4KFO9wBEJnfIe7RQVCjwNU4Sv8kN4kPwYu5zpunH2e8IUHrT1qez31vCJ1ctgoDJqVc1NaIlRmAq4Qa90DgeySRTVfv5ToTHJrHr6yvOm4SeJlgUl6q-cMOmQ9eFIQ_STGGW3vljlMt5SuuUAtgmhPrKOA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZQptj-zh94aWKzgyubudVoMp3X5-75n8jefDpTFo_n30gBqXAeO0FDzkDwh78SxHn2h3KrLmg16pKluQyViWIQy-ZewmbjiJ_o98i6JQoCGmdeb9kncG19CidxIZQreFskcGjzT4Zp9Hgfjz7UydOzRI3qONA5wH2Z3tXM_mFeInVDMeiS3zs3PhVCoovZuVOcqCkUg8p0VksH0Z0AQ2ZoGX-TXcxgXhi_ZjVc9D9DnhsR2iQkQl0-ZwGXlHELafL16-cH2U8D2_qNkZh2NZr51HQEOlyjntFpdcWTQm4TBBmc9vJVJk8q6SpwODC261zfZuoO_wOR1e11nkZ1AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
