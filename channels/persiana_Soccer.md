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
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJAEah9fswP1bysHox6BWzVIHf2F1rzTUQAO42IwJWNASNrngo2RsLAhWvHWyZHfMLB8o8E9aVOr6SAJ5w1fq2QaqzYv8RuUPXPwBh_RI6oyUI6xCipAVTbFvQVTT-N9UDFyqX7XgG237ERPtkE_PNs8iWiZGEQWvGd5QCKWeIraS-og0j4oKyo_ivbS52q69keCkecMeycI7zKogXDdeSfoE0IYq7FWv-6kxjnXEMMiAYpBsYBdwlMRESrxmA-QMHGqA6m5nFAwaAwpI_WxC5piK_embVRNcF2T0t7uNIt1_UwUG_EOd9LKqG5a3ETqDXJ8nrTqHYQyb8IsSs3fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvSbFG-j0j5oDPLb_7qfQApLHbkH2QWDMvOQlvH1oAW4Kvt0aRmfhxit2Z7637vzcY8bL92SYrBy3yx-z1ruC-SnYyLRcWX1D6DWn_lRJ5KIxIYu4n1HtUiMn2RDttjFNI7GytHZDE05p-kjoAFJATnnqGVHAtwbBx8gZvVJMuOczxsCcWutxqmH1IW8mjNV7QJYuWWFD1q3naLUPJ0cmY1xqgoHSUFnOua3akB0RB5--eWMfq88NgrMdeT50PiEZqOhepTJ7hBijbGBtlOkNeZASNENFjz9YGY2GlGLH44CePjvO7Wt8IpNZ1C12zO9ImyNUf3LDEBs-QlejF7TOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIQfkx1ahLY1C9x0AgRbgi9pHY2GG5_6ywVGf05lqt6Z5c5PE0IYT3Q4PZ508gfj8ClG90HqjBdP3cIkjIRF_F2UCZCfzNaBjnYGt0B7P2wG_pP0uQMNH7DkR9CPJO-xuMAppDflRh5gzQ16K1mj7UyueXknWHJWutndyBpAFyzHemZG7jagkhDQxOLbVlnYEU2XQngUcrgCLZBOk-zMz3SiDpDAfbuTciDlO7jRu5odLUtjLuoIC6cGbAeW7--sv0OsgF05OmgLLzA4kCLC_ryriHoJhJUCPGIqsGmLk57p7mcvtNzmJzg-JZXGKCD3rtkUvAuuk0r7xtgAcqhrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0wctuF_4BLobvE3nYgFyYui8RTSB3SHGbI-XzrvkGcDpXKy2rsj0OaYTkZyLSPMLhH-n22DX3LBGYRfcW6kh0dLT2Kil39CGd-LK-b0NLUJT6x4_YB_YD4B-WGLbsZYI9qNEbbiUkrbKKvh3TmEFFqEgN37gaXb4YhK2RLKOfI_UioeeIHhCwNYdXaW_kEKsgYf3T6htSlwBYdp-WfV31FknUNfbthF-cwM_ebons4sXBJyQ33zfc9Kty0paf_MNrsLBQLiHgfm8zXonfZtIzs52JE49GtkfEmZb0tf9YkmcPDx1gKu1JKFLQCI7blmJqwAe5khRWVcnaY77cQNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc_NnBwKd1xSUrbA2-e3r4IZDyu4mhZgIi755l_MyihcbUO8xFsEBSdWixnqmIJkhMsXlg6EBg3mqFMTxuD-L2KFrrQGq9YcLKKPxQbQ4N8hJZXs3-Qj1jhy7B_DvNAkAQfOcsSSeVqphHvWm1yG87Wnjcc7hNOYY67ROZsaag86WBWdVLK217_KzB6vcsRgVu_zLiM6PqnA0L_Mbq9H1bcCmzBCHoN36uw0VOVDCmBI-6OcWrUcj61-gjAhVnFZO_yNlRfgssiQZfQeE4g5_zmErUTZ8o5tM6Cz6iD8gcEx7NLxYFhDQ058SHQkGPqOubsxliH5F20HIACKlEYOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFGtQMBGSea0mPE520BNUsr0f1D-DJiKesQbH7oeSgsKiOlhUr4RcOpPqEfKqi1-Qcf-ra88PTBUDJK718J8H0OMt3EJcOn-2x_SkmEojFushOLJPKytdbTKaKK2TzlpL8Qs_uzGgt9Kg4z2YvVRLXgO3UqyfUF-GjbTjx-4vj3x68Q1VYyjG6EJAmyyhGtg3YFYD3N8etmcI4utFR3Ao6t2ExTsQEiVbIfhKSdsRB-NWFNal_zCwdPxL66YMrKhp2ZD8g_f-XXM90oaVfHcqewXT6ChOlMyKIw3HqQIUxppXrJRq1qht750Flt4BdrhvNv8D3yZtJgdoAWGQKQTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av1gX0trTTWfb9bknAJjU9DUYFalulcB6OtgxwKYqrebAy9qAwUFY4aGxRBxDWLjk4gRPiCjdQxNPkh51H089FgkNcl06tHBiXvc_wjGGRUBHveQAqlv3nOyZVGekEsXfpWIj6_KA4Mc4ebHhGM4E2BHmDrf6L5AQ4lPUGsyFsDdoujzDFDnGmoabKSkEiwNbUKRztNF41bcQ6xaa4rtL9F5xiRCclMFRZ3x6_sEpteH5yx32THvBbyX5_ZRQ4GsYWjZg_PyQYK0II9P4FqxpAxdP2yXsdlEBdE8VACi3eoaEb13vpnudT8PqbkZoHstC5LGCe68LMIyZz53XneNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piuOvl4xx9sgrVxhHxaXV3c0be0QzMmvEpa9QJsV8_q5RF4klPpwsv7Hz4te6JD_E514lLsR-9g4jQCTDR-FFavYN-BDWImenunefA5AJHfCEqDmy9oeHKvaH9n6m3wt0NGLSbn0CJ970ol1RteTvMtPc87Lt3KV6-ZJeghLdiJn8pzxI0XcBlCaSamHI43bizMa_Mz-BF-tluQhZbw3Y3uUBMLPU_c930GZ659RnQgSXpINSXOLbGbXSUaJ-h4KycUAnalrWvjV1SxUySf0ZolOeJEiZfeMBW7Lw5nf6XcjIEwKi3Tkz-gqHl_q9ce0Hnj4o5KAyHq_5K3UtKauxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLUau9Bc26nHpjVFXBf8Q9daHv0y9JbbUTRSZtACpsUK_7bN8igjpgkrJ4va0QtTOAhue6mOb4067RF8-ct7nOTATVFU4I1o3fc2ntcIlIrnoOrPfIRJkZd3NCrOftM_h1d9JFGjoDSufZ14Dowy4hHkGJAvklW8KA0Sps5N83_bIRoFTj-LeD8sIlTwrYrla2DMTiAoR3Hvf14K9yqeluQKy7hq8PC72SLnOjitukzcnc6Gd511wgU3R2Xo_1doRbBzC-eKmxuePQK2_h2bj7_onMR_L1rZPvxlMX6WUv_IDfla3GStJAbkw4tHUvO5ZLLqqv27fmFEI7uPbDEPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eta5UaH_KYObuA4g01Na9gUe0nX_Nbf097FIplVs6W3DG28fYPtBtfX5KnJZjDBXA6sUodISx4bmFyP97MwfSNU6wQJclo8_qawOnKRsCwCkMIjphtXqI0njlvJ4TZsNKclvVZ3XSQv34M9-UP7v0YPUkVzPfHSu4JOSaxIfN1n3LONmP1HxhjrBhjG0ffquoBkUOC6rCoE1_ex986BoNMNlTCKUvP5P1a2iIlCRW58LM5qpjcHCmsvyx4awlntJSkVoYyyMenl3w-_ZkdBhMg3YXN-xuEY-WQULrzcCLMTy6CXJAgeNTMK3lN3qulqBnrdBR4ZCJyGWqYO_Krdydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhOMsRxXe5ZaKtZPFNrRzSwPfINFupFzaU1N9WjC2L4RAnqlE-Nkqe4U0Ln4NMdpXmYaUX6JOyStnnP7gTUKkMxFeREBroPsUoLmIv8nuSQdg8vRHSF-fnIVrSdQxXNpZnQh5V9-pqxsLkKG7LO9HVrV2PcMOxn5oS9otxRvpOLsbIqrliuaDPjkXzEIo5VcUYMBo2EjkzqMzhdldv3rZPw8hm35EKjHUpCfnH3ls_8eks2Snw66TtEaQMMbnqU4nGhy8N77jBQxVHcNBIW2e2-ASIzdntG-XslVZfnCVZ6UtTSjwktiMtQBTR4EeyTB09uMQ8hpHVcTF23mtyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzkSpNH-kCUf8sKq4iaVt4ezxUraqJVqKTsgle-1q0DAebrwgroDDCMWLH6E30nQ01xmIrQyrc4tQt3p3BV-N1Upgda4NEJY-Jy2_0AlH04fqpHCJrOjKlkfI3P7CDNqJ8ce2WeKV4bA97A-ik2bpJfJBz0we9oe4hgQgT0knruFStDjZjN65mh_TuB7PQM4yDEeQpgnxcqEucv3opRNqVG8FoyYyVFcfdwFpwPLjVp55XsgFfWFG1E-EURDJeHxrgqAzMufNdRhGudsSUO6DJyB1Py5P1SVJCwYzGX1UnyxiwHV1qz040afUr78rejJfilPV1BR9vWlP0fSec-_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwsmSb62ahJ71ArlCV18O8g5xFXJPkuvjalfk9BFvOTQ5rqjWq1xSIAXgnTWi3N-s16QrHmCo1rw-TleiIMoSJs02L-A6A4yKZRNhpEEbNV9_EkVIzxJt_EzFGhK6pQN9_Ah95ipH3kMLnlVKkpE9-La8sUHDn3j9wQz7HNFxfE9P5_F8kG_TQHgUmFChziYkoosHTxeWgw-LlZUFd2ZjKJovntu0u3M1Yx3H7OXF6VpNXfSDWta5eAR3VflQDoWRKvmbPNqNZRrYMGkqUH7lb8C-2Ey2cOWi3DT6IaJmzi3JNEhkVW1QTPnAyQCgVy7as-RArto-QNhZzFE9di1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7q-tPoxo4zA0GCjT6ZQ9DqbnAyqZedTVaenFtbRbtyocvGNsCGTUFwYQQiKWB21Li8cmze5wfDOUS8wx6gI6OCKNwqbTDomD9AypS8bgBafuTedb0hDVq1KRjuMCZRdNxG8DAFUpadYvP37AtLByVoaR4gryK_qkpQvYiY26hWN3tG9PuXlYSYmK07T3LEYhe86dQuuqtBbWBAGH5H8Lvmr__KgA82D5vC2UTgzYcHeXEIW1fdD44wonsYgK4KZBuxNc-UjBCMnBOPFs5nKBBBVSgVTWiXWgEKLfUr-6BFVcgNxXCFH9VAOzG_rDWhVuwtvBACqMiNxafWWP_W_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEyBCiPTMbKLglXkrjPRAsifBQNAl5PUTJ0k84ry4HGmC-TGT5ECjlB71dzUWkur6m0yl5H12EgwGnS5dvyjf2kkoiPFZV1o9R0wxi2xka2_n07NbZ7jVt8ibH-d2Cc4L6hvc3PBKS31EnpKEWkrg3Qfs2TX1n0Adpgb_eiJbze7TY8vKyqi_0kiPTxY9gN9eZwwXKXm4LKgQJYmy_4geB5MO9OUX9Zm55V1QNt-bBYYsh2KY5qWNuV2FYyK7oL_JaaiVQVyGvLhLZcz-jbj34KJDkd2EVdIiFVSr5JqWVqA8cNdf9SNfyItbPZGT-UGTFJ5FalsjMidkxuGxQ5m1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAI1c8MHnTqAqKS6CNU7uRaVpXSmdmoK8r0rBRVhuqFPMfQIZJIMS0kvQKyst1zXNYzRi3e3L4qPU5zzedHC_mA02LZkVVuKSfuCn2KjekPGyUTIbbTpPY0DFimbsJuFe8BkWD36p_vxyH64vMMBEjz0KD72GI2jBH4a1Ig0XgT-qwDw5EX6cquAqd6j0topjis6d20rL1Zg-QpwOFzUnD5sj5YqwhcxagvYxcPbolT0DcK-pHg4M19RsyoEAMtk8DCA7fdnHeRxHhFipGPan0pG3RqM4-JDlID87uAm5iI1tYHVdP9MYnLH4c1zBCC3GZEbL3deGJMWd_K49MmT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMLQuTwr1HyG_z0pufQR1Z_0-L8dcgYvxbl3QzCXXXYV62QCzYLkkw723LvY017X4RjHydQJ7mazLsJ1dDr4o2vx8mK1FwA6Cd-41obqwDcGXJoXi19nv9j1LaibA3kMHQRqUObYmZtJOyIhEKMxI3znj4N9gJz8cjKa6iuS2NZpThsVivffEH0Yc6rHfZQfTkL6hYvWPOJdPhlKCUTfnSBFD6S_FSMU1klFWuIOmbLMFX-H1jewobDvl-pWQ1bdGKBrFERsm9oNBUH19L5H55lWPLuMhMKMTd7-hA_dGonAtuqS3Lu-bs21urmV3kLgvlZ9-DA-oVtsn0POJ9IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw0aN6coJA3iv28mKLQ-sYVyQHtMyyd8qyUcAKjjvy8dJ-VDtei6HquEc5oYbDanPEor2Hvyuw5R0NZHDHJT8wPeUWQkCI9fdDbwX3CoNvtZgczmDR2VjT5FO4FGl-niz5POQgNrB2BpAIPgguwG19tnuLXGO6ilNV8Hp-AY9f5PeCPg8UbDIoBzGGFeLLCzfMvwLqOovqjjH9OgkxchO-fMFZSlNFRqhZlAn34uID1C2EDxhUgPa835QQESibb3SvhbV5amsVerO2D_ltlSewhMbOha9Yz9Krv0IcxaMqR_lZvRx9L89yBELI3lPuVq5Bhzg6fTsRx2M5ZPmzmRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs6G0XY8lO1FyZytWRgliXL3jb0Yrl6Mx6hbfg1vLdiYFgibKzrXxpYZPX6ZVmyILKgcisMFylk9zDWQnthTmhs-ClrqtQChep5Q6pnuwO1wyd4fE591zVejBw3Ggy9CuGAnZdI4Ucz8kHTZkG74Anf2qr8IeWl8IPijG_A96XokFmvDe5LLk6ZPPMr0NA53S7z6Gwpe6U12weE2QD5eODqxYbtM3dR_8u4YyzV-RJtT22yM35KfiK6WEdNZupSJ0WSBmdFKgA2v0waVpOfQjPfsIxj4YPvwngKIcMIQJ9Q3cLtO-RzAxQ7lUXVlkuBu2XsQFwHSjzdfGNh8qRIv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g4sFG5AZpYhsSRUTpiKK19vmokkIoR59SEmv06h41Mhf1-ugv6AaYl784unz5f56YNEXMhQDSCwW49c8QSaIIoG7mF8eR4WnFFD35GfIv5xiiECI2UjWsGtLe2JcJWpoXAdws42_v3shUj5rvzzmbCepbx2-VVlyL-8ibG9spmH6Lqb8jl0PPDI3_2LKk7TLblGKIZph9WHNL0C1NZAO9W7Xuo_FbEpsTiFQzvPCs2JJ0iuAcTkbjMeTk_lsOg6krwNGSZ6IwTceAK1pLJoZRjG5B8etyMM1L1WKX6DTUw6MGyEZWFOeRrsKz7zcpmrwCjqFPHxd0sRvMdg7pUr_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eE1MjswtM7QXyzjblrK3-_xzzLqh3bA2GGQpJbt2crlUYzCLr1sMTtfgFI7WnLHJFPJCASEQ2G8cy7cU2KVTLZWDupAmKEDjuqEB2KDwbHFTsrZVQByqP5sh0boOZm3eNOvmt5KxUMaUvPFsS_wQlowNO6O5oGH4xveSNd6P_Pxxp0yQVXVXWgNqObgqxTFG70NVzNhLMD5tcchsyiPfj0wmEoBRT9h8aizBZXF4UybqVnb8yGP-tJ_YOpmkf39m4aWcUoDdl0yfVJdL1Mnu7vJ0DAen9Do3rXsyFQvDQO0qiB82WW2GzdR2vBPf-9z-TACkAlcJYqc9WegrV51lDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDmw7M3CT20B0ZfL-AIJ4YtvyLfBUM7Rfo0SfdpNuJeWq9_ISaUvR_zswXZoiQV98xleSGZw2hN-bEEQ-nfxRmGWAfQmjlrKPAFKWKy2nRDjE1zZciOEx1pP-_2wPfrhezJZtY0ITyEUDXzKLn4Ipt7J3hrelh5SVwV5hXklj22q5thrNm-oNOmW9Fl63xBDzanjiQkdKef3IUAj-KxyEssI2es_iJ-GrUj-_MoD2v7QxegUtg6V6L9VSBswycwPF4P9oOtWaTobJXguMyta_SV6O1fllQJGkk8jrwi67Vgw2c3cdw5diF2BKxwwKRK-BIBcDGRLzStqIKrp87BU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcMCu3uHB70y2L0tvn91bmvvy5-nODopTxgf-37Mz9lzngpPwlSW8zgFNpNASXFu1VsR0Yi8VxyJbNS7I82mKmDdbNfj0wtHDwKO0rJa9rp3bqgvwuVbY3bLpZz6Zq5O00S2weDL-WSTr1QfFHR1lsipcvkEEdjIsBuggSMjJkAKKPZLoOqISc1Hkh_WGtQPhNxLU8jqOHkSoizcpNFSbmjSaR8oF1_o8WB6BJ8We9Y4YNsspLmyto603Gfys75QW9vBdTJeNHz9_k3lZ5x7fDn_EXdtkZbO8w11XI6rcqfm8vp4OUQQMn79nwVPFN38j7M1OFxZhnphu1BkcyVm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6HM2GJvL_idLSfgPaVPTCGlUPZl6v3k_0kJGtzyf-WnMmgLfUPnC2vRRqW_ClxGRQZnzgKh6ofPYu0G1oSOIyyrFIS05kcWJaFDO97nbjz7WzJy9s8KyfdUdEmbuNZX4v798Ac8HGCRZmoW-QZaGAMmjZ0oEl1WWyjdnyi29u_fVcorucBIFQjrcfifZun7t0rPIimMg62Yx34WIoDLS2lXhDOpl5n0-x0x45yRYsHgkeom4wJ4g9j666ewmelLES8LItngb-6TsHMkwCscZn7Os-GrPcU32LQUZGhkZpeNeR_jjW8EAwUoDZ6u1DKhkooHFc6lPiq81MFw7Ag13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAc1_ANE3Sp0R2WuqI84rqlKUt_4LnOwYK4_iFbikEx_-YMRWsh8jzZLKrCVMGIxMARhI2VYQj5ESvWrwIc5NlYsBWAUXJxz42ovLwBUcWhXqS_UKmNaMwBfiwwE0U-7R8fEBKRWZNfYDJPDO7rJvHJQ2zjoXzKLPIZgLfdcm_wAYzVVOU8NO4bhu3KkbZs8Pwdgq2Fw5tLDEdrOzwrn8AC8PbJvSuElFfdHJcBouJMWGeAkH8LDw0Hzl6DU4LsEWzakurxSmU9l9foBiX7Lq3XTjIbvdEwRuw_QL2c4GT5ZnCY742IVG8lDyVPSw5ThLMgcRXxbWl9VSAt1IGzy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbo7ZkB_GeRPtInTKX59-ZVOpph67Y8e5zCi9zVUsCwi0RfgU0GuUYTG5SJjXHtkT_05NwHOxwG7nzFHQZizGt2X2ccy5CR4ucgZevsUaXVr5-31jheUg0pwiBBSIjJ8SVbCvGlliDV9n9qy9D6BMe5f1YbtvKndAWiKgRpU1_soYlH_14_puRlVFsU78hG_Zre7qjCG0T84oiMnRmFILJ0KXDBwXRKuFIH9ZKmj3E9y7d-dVTDr_9RwgJNN3qeUkLdRz1R7hWA8S71cftEh4StfLJyIriM0hOVO2REY3z_0UTyVScF_huXedBMdLjldB38hAWuN3cYe3Ssdn9Y0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmDNqF7Pgo4bUCjBcu6ZpnAkS-uGowgXeHcEVkC0O0PZU4YzTqEeotI-hpKm0Ix6ZwNj1f8SAv804GOL28gOz-XUxAnd6Fts8ZWgR-hG0dPg-bvaeEVLyY9D47j4IDR4nWE9Jd1Hfnh2gr0S4qIKAFkzyqawFhQer_Sf3-_uUzST0ZLMRPISRj15X7IJiyrDiJhmuCa_zWMkEIVyFtihwZRTeidXF3RQsep9NXeVfeZySzwbCJ1Aka7RoMU6vivF-O9b32OJaqQNKB3H-sa6_WGEAaYRPOotbCotJblMGX-bMWDyIk5Ev55iU-i2KpwkjZ7VX2RdQskvWlqnjYlnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv29e3rxOdxXbGUcGMDDyGnUq5-siogELaVwPichUeHlie8u9TzTgjcIpMQTCZFCip31ppeZXmVJQmFwhcKvuDKgM7cH-cBy020TUKU956hnq7fjVmzxneorysPp0hh7d2DNuLOI-XP1kItkso0zuK4zTmJsSiKt_-ymly_7M7qGqWLMfWym8d5TQmNq8iN_hBBwxU1CLr14t8hqUBhybBVLijTf6mVEMsLkkZCyctcUtCITVWyQ8ptvzFBQXuboKAGc4ClMj3-FnJWR6I0yhG4JDbvUEAQe1-fk8x2ecjz1nI3GnwCvtpT840zZpIPuYL0rs8mPUTwTliJl0aSd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOZTvN-WIY-fuxCMLtSvWptcMtv7SxQvp3M0XrLmpFnXgErYGWUk6w7Diwc97SepcALoc3pF0flCmcSqW2OB4DMgt7HipmZEhDWjS4UnB7DgGrFOrts8wUEEqmGAV26Egpz9Ttd00jQJWJXZNCm5VESoUiY_FPSVrhplpo2soSMYlScizzRqcYxOTTbKAv8Pc-BmPqxkSyhhlcnoKDxPgYYQcRWQjRlvGYPX7ABgdsqgkuG24bnsjvxSNsHRqiaxmc4JZFyGmMyZD6qvSLTvY2dFnB_2rY5iq5qOgAAmqGw87h270Q_zhvS1wgijauy-OrYreU3TLOj4fXd652JurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaktirB7Bzlc1t68GRMsirBvrEHQRg1OiORaZ2tXwlnGhN-ZEGfQL6q_1k4XPFjDHYSyP6A6yZDtLI5m1rxYPwv9TlckVEpEdkYO_-En-i8hEyB2RI3SDil6DZvBoew2Hnm4AFoc8yVKELdEJjCAdRroZqoduwLEgf5-_sJHdrrr8AEOvxDMhXqyjlvjIrVbXwe2MsagFbu6wqiqpDAGfSIARnWGaVumGFSnp84dGal45AEmtwubbe6nR1_IQIyJdT04Yl3gSpk0Tv9X5psOi4Hg6WWqVhu4Gwxgd_8LTyNCPKhmmHUOzMbSm6I-uOHMcql5IGDUBQDc4qomHE1EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQN3hOpv35G8anayZ6RV07Ur1FTVsyS9p-pcoTzfMYT2XUieBwpXU_ZkxyeQwSmxMdJDnRvGxOMOCaPMjv38jNVaSmlHtqPRea9eLVl5O_mpbk7lNVh7YEBZS4uz77FLDDtgwwD4Eqh70rglIdxks3b0UtoLgDp5_3TXRzgHwHDT9Om3WA2FUjVR4XNR6FJz41x57HCCERfiESC-1PPsZbFniZqE8Ag25bf2iW4s4ZuyDlfGf-ikxaQxm0N9NEjUO6L9zq1YW3NXZFUrCDrD7zyeIfhvfTYKMBIylg4uXq8p3i_6_pYFCR_AKxx82TQjrpdVx75hfnw3K8Zt2Vki0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=MUU2KZ3WRzpnlEKJ2d3cONm40oAFLp4JLvqLPgSb1KHLCM-YCig6b4wzGRM2E7_nTsR1EYDVcNcLxUTDyJEKlFIstmpKytgOn0KFYf1vIyleQgGduswdQK--86U5FVgEWcJi2Vc2SKuEvmX7hkldArZrr2I-DiWO8REbjNdBOL-FFnj9BcS4Q6jeMYZkTA3TUx_jiHsAAfzQx5XMtYUMhcaS4u1rZ4g8Gsj5kqMmvHzqb_fKbUTzOWMhHmDry1D4aKDOc9Y715-QKHTZny8lycq5yarh0hoUlLu_mIurw9ojcU2aqrGuHjVbSrThnNk6VmriYn4OLWtuT2hIiC-5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=MUU2KZ3WRzpnlEKJ2d3cONm40oAFLp4JLvqLPgSb1KHLCM-YCig6b4wzGRM2E7_nTsR1EYDVcNcLxUTDyJEKlFIstmpKytgOn0KFYf1vIyleQgGduswdQK--86U5FVgEWcJi2Vc2SKuEvmX7hkldArZrr2I-DiWO8REbjNdBOL-FFnj9BcS4Q6jeMYZkTA3TUx_jiHsAAfzQx5XMtYUMhcaS4u1rZ4g8Gsj5kqMmvHzqb_fKbUTzOWMhHmDry1D4aKDOc9Y715-QKHTZny8lycq5yarh0hoUlLu_mIurw9ojcU2aqrGuHjVbSrThnNk6VmriYn4OLWtuT2hIiC-5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOo_Wjk8tWS1Z-YqnUsyp9WiS8m6_W3wgfaS9Im5TTt2nRh_NxAZLWPMHSdl9NavUSpGGGPofut4gIceUCpx9N2qvCT8HmRrY3NpZ5NxhaLJVbf5BCNMWjrPvyjdU5zA0qu5WaxjgVlxt6D9m5ETbVt5vawM8ge5IutJKKu7hUbs0vJ6PcdaMCwS76U-9mpFPjeUKEX4cOHATmediUulW-bQigQSB9YgfTS_2hsj4DAoWrEJsN1_C6T7wu0kqTHjcy4wdDdXniUamtEDTMJm0iNoDG5L0LEARCgr2cPaoufGobzb0XlFTwjZ4UbAprE37DjlgelVZ8tA1Ri0-5tpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAdGLb7cwc4wiFEu2_t4NlHH41CfW_xbka-u8KStNDsW4SQmXL3w0y0trNAcPhMy8VhCTminBWE4BQf49ejstWmsT5a43pOvbo6NGdTvx2BegWvch_lPdykQY2mkvj4xaLFUjbZXicyU5G84BukPeCsW3z_DIwxphVqmBDlew48zmn28c9o5GcChlUBQiVFwJIh2c3h3CTPUbJf3GV_AijgFJBl4nwVTcjHwQVq9G5abm1M1jnFuC-y_uONs949I4Epo3h5gv_27vLJhAcAwLnYdZM3qp3K9W8dDsaz8QbMkud1qremJK_zrOPpc49JGY1R8zYQ9XjU1gSpOpYziKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLnAQYai_aacQ4ZGsCobIf3WbLsi_mZBhtEofuaCr-8DuON7Phg0YoCq-j30NnHVJY-UGNg3cJOwaFhAOYsfkbQV6AKdZIio6IoAl0nCJx9oA8wgHRbJT1sFz0TWP4Fnwm2ErYJ3wjfZOtFWD620kF0Zt8iFSFJdPUPyoNR3DHznAJKgjpRMxe3nKhq6Td2tUlA5-PikI0YufipU95mWyIImfSw_DoAP8-sqWfcFqoPtJfXdK-WRCe32zQdWDQqHaebOqEdN3lSEXOXAKDNPZwBxSMXfSyZ-8au58PQ3LCpQMJv_gDwtlioaZnEWCd1XXiJIYSLaqAqonlQdqLFOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5zN0HppqAI1BAuFABkhWpZIMQ1v073vvsEk22L9mN30SxsmcnLayRBvrmAhD-_G-HS7NFIOOhwLuk601OkA-m1Kt1AZ5UfE3oXGARSwnlCX4bBVqMNwRLSoejjLaAYGZwerIZs0rkibC37uq0bnv0W6x5Bm-I8T_SJjJcO8P6SUKJVG5caJ8xlv0-n2vHslLhnZugRBrIjTKoyOMe2_dA3oIOxR8YQ6dqTBkDHyFV43k1Z7MH5s2EQ5cxUzOKWuCVH2TQnh9_KapOlhyAGDR3IRhOV8nHs5W-GyN46jcYAu188N3PS31_Zee9_XV3abA2F5DLs2JQANMr6Vo1X05g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMBiElxM98df44ikGTfa754hJ8g0AxOGNpbvvRl8Ts-xa9kzIziUpIF72Juat2MKdvJSIA5yCsi_1JE9lEN_nlPVcmnMBP_rz-YzBXHA2vd10W8TxuTkQigP_k359VPlcyYulQdqHpqejjgHkJWlm-Z_Khqs4Kr9Y0qT5es-Vd4Xo0oUCuMkPX5FVPl3vTgV06MMIsEIX7IDc_dICcEvwcotTJU4-M7kkrSVH_L2VuB28zY2VfDURVUybSV9NNo0ZbbmiHvBV6CyH7hWgct_IAk3oLfH-xfC5xCi5h3IuTZA1WBune8NYrMqzivimFoIaxk8L8q9KBCUMwunpo6FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjlxDs2g6qhOdqFyKEEuqqpOnvV6WpW5f7uEb_AxbLt8nalTsDtVOgoq-vdmDI145gTvjYAUbkSB0rg3PpLMaMvcm8t0_Fe4I8WvCYWJChCifLRULqJ9LxbDvvpA7fbFlxjrtb7B12D3qfxdomNzfFLSzy6HNiPGgqSo9-X6bnDMgDn8ZPuxyqncnTovm-kPrKShg33_-USF2ba7mGM45NqajoNCYGDZw2PH4v31fZsEeynTq73H7VfAIA-KKOo2_p3KmuNm-mm7tHylpEHx7zhVUnLllCK2XdHmZsfwex_kWQcq9NL6ZMgDHY6eDrQiSDn-4OKJXEe56IiNK3kAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2h8vjG3KG-h0e_XukqQZNyabNY6EtqxF8uWTe6MOAO2gL-Yu_3YJzdRHE_Ypm7KAXYt-cpEmJK3BIluCvIFBIiYgXZF9bcQEoXt1olp6oVkz1cqe5WG76uRa13KeO_kLhOGrePPlmKXn1w47_PvzuWX7UOGpxLbJLGOLwZ8BAX8RY4xooHwgemy4eA4pecNA3pIcz0tvlQsdJsXBConB4NIQHel5_Y5MB9SRCdD4Vw8KJ_fM7vU1iumrztFipHECCIaVkzyAKEeHAWGRj4BapK_EBAv3n31FRIMc5jablJlnA2-x7HlrFe9lXcmA46vmBJdhUhgeng_OE473Jddyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZNuyigEbUXowq--jyMQ--dWK8S164TFhi4lSTiUFW4TPUu0JMrJVGwZMrvMzy2Nd5TY4_RUf9WjkzjErcOWPz7GASxjjXhXTQAR_mBtOWZc6JtyEyIUsEAKr0QGdQi1m7Zkz37iyHyBbPYjhaMplZxKiL9Edz26yMvJzxICazDzhPvPCuHTNhe3qjmixmIKcz9CDzU0s8Vt0OjpRYcWidbth5ctrnhgLbDqwpYfBay6mWsrNr-pxIHPlOsom5YV4TcXgRlSPQDIITljnuDcHHgh6WiJ-J6-Nrpu3FCe6IpMx9b4zzqiiEeeDE1Ic2iLMeb-BnJzKIPfK-X9HKu2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-0mRpN42TzKvk8iquNwdZyAX6arxzeJYYQg0-qDl9vKJyafunlD7KMsBlYVwkAzCti-ixGRfPq1u0XWQP__Uxk4obKXYD9JnTggnR_3-8hGVWIailClm1_XfhGo6jYjD5p_Aqa_UqQqhoIQUJNaKM3mH2j1IKdCc9TApTQtkoQMFf5kruOw2JHbgV55A29aHP816EC8zDx4VjzgZjwnOt29JhYl5WDRdGzZUI9lKxDkex1o4x0Cq-wTBbSPMOY0UI3wkwaywGd8OCTAUgqbT-Gf7Cgb5xR3S3FwoGmmA2ukBF8vzJJu9S-nNbMaKwFnvWZkiAFiYzdWyJN8y9ZnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPLBAVxsiArRV_4UuuxqEgrNNRfTUdevbj6lPyKo40dL1g9gvl4L409G-01qxA2Z8ZN8paKy58xjW03Lk2Nskel8XKjiW6F_UChBljhnt6I5AXQY5FkCuHyRFJ3kN927sCfnPRZxMlZeIXcB1mFMOJPM5OPQDI_WQ6oCVb2PvYLUoUS9dgQXuK7ibNz8fOJ4TuElGqhMlV7N-7o0vSOGEewA_Im2EB-Ww-HdfoA4XTaRayjaQrhcI1QnxpcMXyik-tL_3FdD3D1C-ULf_Xls9SjiP1rf--QPjAY1I5ZXZFVVb4z1CvMNQDem6RsKh4GCaC4WvFZPvDS7k5BgyYevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdDQd7-Ps9adYG63-DUbxcUkdl7inWYRz6Fs3sfl2P0qpeNT3NzF2Db7D9Jn81mC3Aksgz7JPqNAixr2ZxiSJN_kisYc5oGdn32qvmUXcA0bzHcXtVGbHUBAx4-pJVApyDM3594FO2lr8at9D___eaWSa3xzF-TFmw5hrbPFKV41sAU4Bb5_mOAGkw2wo5G1ZPAo7FYxXJCG69wPujetGS7W8AaCIQzqPO38PbWqE9iDm9V-5RRE4XsXvxVc-k9NEW_kCPRw_Rl-YHV4XTMP2H5fhpxORoCwZhBMsvKU0ocQdIoLjBjUKLt9a0nTCwkW9nOqq7Q0F_1hgfyAnFKcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=aey4nBKkheQNjAXDR4GOKvLJdtef9tVZ-yc-eYNsJzYzmmk6OmX6FXQzG0kRWGdfbDxdaWc8td4ZtDdQsRcY2zV4_1OF6JaPYXOOC3vycuaFEu-7f5si4wEwE8TnnzQtHVu6LQTV-fMm0c_0tpuhgfsQMrR3crXZOaYaymK0LaXXBvs9CK1Du612fISd_8j_olbUFuVSSTWVx0wrEf5aIqPjgnp6b1nmYQc-14AbQbngnOJbYFF4EGUD1Y9J6K8-tW8JZrtlAZSFSb1mNPfrFjqmO4uPKNxb31tigYIHnrdtY5k6Vr2km8oyP4FbV7gMPHgcn2ewVHRJ6lIH1M9yyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=aey4nBKkheQNjAXDR4GOKvLJdtef9tVZ-yc-eYNsJzYzmmk6OmX6FXQzG0kRWGdfbDxdaWc8td4ZtDdQsRcY2zV4_1OF6JaPYXOOC3vycuaFEu-7f5si4wEwE8TnnzQtHVu6LQTV-fMm0c_0tpuhgfsQMrR3crXZOaYaymK0LaXXBvs9CK1Du612fISd_8j_olbUFuVSSTWVx0wrEf5aIqPjgnp6b1nmYQc-14AbQbngnOJbYFF4EGUD1Y9J6K8-tW8JZrtlAZSFSb1mNPfrFjqmO4uPKNxb31tigYIHnrdtY5k6Vr2km8oyP4FbV7gMPHgcn2ewVHRJ6lIH1M9yyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_2WdMYyLYpPf-5caxVIDz7oZ3D7qDIvpxsbyi6ZHYiAIY-gRvC1gzkjzy5q9_kvEJWFnBtqQmZhOyNN6WSnnpBL60e0AwHSnUfQal6deal9U4v8Sb9_2BGHfnmwKhqb7M04F5Qy0II8MjAC7-fh-uOEOVs0evfLXAEZLdLLFh0cGnaAUSLuCuSf0DdLmt_UAbcrXd9oBKBYCwhXdWgJn93auaEay2GFhkmXrRam9HSyjvBQzOOln99C73E3OCofhHHKa9Efn-dUiB2qvy87qY4YHXtkn9J1KHuK8ri15nl6gvy5Hh9WD0mrv_EO9aiU9yOBcV9Lk-esu9TStrD5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeK2EGdHncPJLhnPJnpD9XOQKyji3lNtMOkc4VmJU6Me78DXJgmmMSevI4fouj4RrwdfM3X2zHhC_tFARr407Fesu3BxjXbiJKcjIghBIP-XbLixN8N33Dj0xzcBI0q_dDibwJMjpt7Wz9GRA7mAb6Qc6W4dQ5Z2del189VTNpjB4K0cMqTVkVymLu7UqPBi9AUOiIdfDuqCneSZJF0mUcYDpx-2C-TgsJOiX-2w46o7hr24XiQrYoIju0XLLYt30Napqruw8TcwLJ1nZyK3-snWjv6F_MsWTL539HgcUAoq_jF_9OQ_VV3IWQsyq7KdB5OvP5VcJcQ7bC5cl9r-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=qvPYj6kKA6ZpN6wNUJprQr9cLOrrUZb9McSGsyk2MX0hiOkAzAq39cF6RfDFA5U4uUdcZDyDWTwtu4dQR5C3X81qOTRfRqXdv85n1-m1J6bkBMdZCY4-LmXTl9LBLk4qi3l-xyDurTw5WxEopR5G_vRTmS8u-g2YOEv0MtD3AN3ZB-F_t0mfXciUFpQuVlFVwg3gzIZyS3rQzKWZJZsPV4G5h43DVt8y6iujK3hDYhPw9cwN8xaZR9_HKfR8DfEAC4RhfM0KpuOJLomkwMMa68vSc7YCWftHf9kpZ0fNTLK2lJ0mHoywF_xBErEJpAflBnUGDu7lhqM3FSYAY2obVy9fz0ohRCXlNK6dLvmUADiO-zVze_2KF__8pbglmslAIIqVUUhBvWileapj5CjzPDMlrqM63tv3QRFdgDw8atX_d0HPtqvvuI6OsWRL332nMMnfZAsVpsKxwWwuD7D_OZ2CEEWmXr_ZChySnMMxoDEKWsmwlEQ3VU_5f3XCZtNrgqYDrk7ToozQNISLvsv8ZKD4gyQGMaBUQVFKe5YZruEpNFCTpYF1wstlhWm93ccINcgsBNduUkUPn02qGvKDp-ST3A20i4_fUvAiGKgbYPTfRHJeNyElugGljQezcVmflPF0_f8XcHgpzfn4ZBe5Zm-romOjVt5TYHD1P405PPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=qvPYj6kKA6ZpN6wNUJprQr9cLOrrUZb9McSGsyk2MX0hiOkAzAq39cF6RfDFA5U4uUdcZDyDWTwtu4dQR5C3X81qOTRfRqXdv85n1-m1J6bkBMdZCY4-LmXTl9LBLk4qi3l-xyDurTw5WxEopR5G_vRTmS8u-g2YOEv0MtD3AN3ZB-F_t0mfXciUFpQuVlFVwg3gzIZyS3rQzKWZJZsPV4G5h43DVt8y6iujK3hDYhPw9cwN8xaZR9_HKfR8DfEAC4RhfM0KpuOJLomkwMMa68vSc7YCWftHf9kpZ0fNTLK2lJ0mHoywF_xBErEJpAflBnUGDu7lhqM3FSYAY2obVy9fz0ohRCXlNK6dLvmUADiO-zVze_2KF__8pbglmslAIIqVUUhBvWileapj5CjzPDMlrqM63tv3QRFdgDw8atX_d0HPtqvvuI6OsWRL332nMMnfZAsVpsKxwWwuD7D_OZ2CEEWmXr_ZChySnMMxoDEKWsmwlEQ3VU_5f3XCZtNrgqYDrk7ToozQNISLvsv8ZKD4gyQGMaBUQVFKe5YZruEpNFCTpYF1wstlhWm93ccINcgsBNduUkUPn02qGvKDp-ST3A20i4_fUvAiGKgbYPTfRHJeNyElugGljQezcVmflPF0_f8XcHgpzfn4ZBe5Zm-romOjVt5TYHD1P405PPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy5MYq0OSmjtwQqvDjr_JKJPl_CR1DHa5PZGbQw7HSsMp8S5KJUVy4wTJ9neysNOxtLPljZt4337WvLAe11_mZAtk5GtA3y5w2kaqPaWekK5_RYGJmywDQG5eP3eDPNWRyBI4XOqBjvEa2SSoJTS8Y_6flpmA8lUFZci5Xq1xkOXmcpym1qq3iWi1QhyUZ7CO75zflWXJa8oq2bEicj6f3eefjWslwQUcFjT0GyZjPYVOCQO_iBU9QGCI-zvjyvPUI5ReW_d0D1DcEmabmU1KsGPP8HgfuaMP69KEW-SHS48N01-t9iUCdrLMtxMxXCuZ8bk5zsMsJ6xGweEDr35qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICQ_f0G-_YvjdPMNYe0zuYX-v142Wwtg9ashmZTl_0UeyBKshDb8hGYLzQfpb-Xb2RICxGWiEDlOfkYPkNxVSYaDzybcmhHx3A_mB6jHy_9ieLeCr03XjR6PohYVrBqchPA8LFW2eHNLF2HBXLq62Fi7dDWkhMxZJhglDA04MrbwtAt5frblJ0j8TGPk18RQOOdXYU7ZTMhT6szQThtguyNUdeyKHw0bObGWwbNOsq1Dhv1oXBs0jZffRddc8ZGwpk9oRKdAczvq78bzLPNEpr4q536zDSSRyj7QQO7EbDQukf0OwFJfWKgNp0Cvgcw6acMgN3Pda9MSH0CxTILCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u544tv3mpAoyWggQKRmZLxP2vkAugiWaDhdCivgWcri1C9jicudrP2pq1Py-42ZZH7FhMp2J9E8mYGXdlR6yekMGWx50EnKTPCuqohC1gIlk3hDc6cAmOVYnN9iTShkdSGLap3wNrvuXrhVFO6tUJc691_hXIzeh8fAZiZ0zcDRsGAsqenTPlsCh0PhsIYqi-GyKoEo8QeKVF-9f2XeOXJaoVmV2bekfJ4vGGB6Ej43AdMpYpYzl3DXxJiCj-XNGomLDT0lq-noB0hiwUiUS_AwpkHk6nkh8f_VIjILlvCW1VFbUz5w__nigr2LPwx-YmhHtBWrxsQSEL-SxSaOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t--JsDPnD4OoBHlly-01LUEDEPd9e-Mra9Vrn8pQe7_jGevgElhHNRFYnY8SarIsgUK1G10J8SC-jshchtbpn9Bf9qua4VBbgYWlirWTN7ZdScIX-HxLDpfonRLqGwXrV-Z3zDl9Qo34ECj54ulQ1ziWTSnc2V9xp5sgq4pe98oEErFoyyx1YOjIiJPSeHjNhHDv2v6KfstbuMN1_PKBNDysWkh0J5V52Dqt_aLMpXxNMpJfStMnBSpV5bI8y71NAiwMQgYKaJ85dn6kaKL-kgYfMc9_zppr3QqWDnwb8IqGPtDr016GVyiis5YiIlnVOKRCpLjm46vKE9xgHxRNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBs7anTIw8F7doK6WuNQw170FlokWjuCQRz77ZnePUYObhDu-xsENU_zGZls04Mu7F2zJVcCcLHUmUfE5OoUA-Ety5XZYMTYO-vNfbkpfuduHgHlrdv77aDJjOPxNq5R5Dvu_r4uxdCG_w3ARFT-kDMETcrvnafvUY8dP7bnbKw782A4QWvR0sSjvYTtuTKT_7b58VOmLt1teXuQNNCKLF_p2KI1S7kzTgP4-H0cCjbz4eOoO1EQyr3-DvGv_iZeIV2cXvoung1pYCiZswyb2Er9zqd7u1BtUs2zf5mXEknhfDIBW8QTBS25F8XD3xOwxbS8RhnO6jpqs6SsPCgwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unFIdHoBIQmQMHBukiKQNcchjVISC1l3MSM-V4IvQxgp_h2maogQGlvMngVCuAINSbo_X0DWWaJNVVW8YnkjojXgaZa_LVVEtC3tdk24I7eCHX8QQcWpwFdpanRSS9QTkQNI1Kwh49KwxYPrqSPgivXvBRFJnVZqOZPunDscXbWrAuPtYNk38toX-lBKHMQPgTeSU7gxdwJt7pWIO8J-Dikhj2soE-qr4YPkgHQM6L8LuRfUcfF9RGY06x5cOe_qdzyaDIWCiNhkNaCOJpFkeup7h8foTtowk2DkL4Y7tB5xIQQrM-ehLGhBxPLODFnVqVqp-0s6H_zxTQJu-5hBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fiqj_nKczA6f3Q7rbQnFDc58ePCQFEQy2SYRE3D4hXHBvoBtObBm4ZeVtdqq6QPMxMFx_x4u7eJWavurAuXZN_iEQghmWUVobFg8bqLlt-wND2KbKaiJ36zPpVZWuVHrtl9NKmi8NIWViWGFhHYvoxa5vN3ee-WLJ-tQGp_FvNLNoEwBZoJUkcNksWyD2w9VlsBmWc8MD-R4FWOXcOV4QSn1ZjTs8Tvg8c28YSN3xNXAdqGlId4eGEeMFbLEv5coqdguyrYZM__w0dAYpgqMEaGkF5itNWjVZ-FoCnR9K5HbHgkA1zTk6JvyCorkVyC6PsomaPDhwebFgJVnZ9F9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQK4_sS8R9A3IEZrjUP-L2A3IHGqZytzYZ7b80w-y2LJSaGd5PqVzPdVlR5dH1pLf_wafqSNfa4VDu-TWSBYH8TU1CWo9n86pQIrsinyLNgW6YkASKu0tkpu-Ri0AFZ092zOFvZEyhgTJDOs91yYO-fXVqkgijXRHmZaR6G3E49Md_Dje_fU1952Pen7CeM38cTGV4YPUpvD4L2cLzNMUZJxZFuPCR1sEN02RBv1E8w2ABlpl1TTKI1i3ErQX90DnzwTSX5sIxUOvi10vnqydWyfAqiDhIgrENWxFS_tli32zTS7YTnmuDLc9N9Kgc717QyR9VFdAc1QmArdKDtsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSQk-SUvNPOv2LgXEzgsHNvXGq0WULGYJtPCIxtNUe_hnN2DvNIvAkUrpnDE3HhYmwBmuF82BtXYpnphz4vHycRVAutNQfq7zaTEWk3W07PxfrZyLAfiTfAvvvwezw4HeMtpnUlyoqTWLKeCiDZYDjVpUyOX_Cu-8tnQ1EuGsnF6g0cqLXxZd5WYEavkAgdJ-mC2ODnjgSClfRpyEKnDY65cDwfM-Jnlosy_2v5j9CerKcbx6dZsFYiourM-eSy0MtUjLrkblD7panN-aUoynxrRm9HpvTtSobLXzWUFA0HIE53PIsDk-nIZredGEM2PhPYfjnoOYC9kMGz6SlYaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-rg4vbc2pHZekGFTrGtLsLvI6z8yRSmQsdi8g6Nm_xx7mqn5qZMhZdc1TIQlO9jaIm0_kMxiicS5YcJiQk21W6ywFigZVOzsI8prSrZiorGpL43B72j0fAGuemz17v9I0cIGmDfu3XsosGX8TNWVxXUuVpEJjEES6CQezaUAQzWKlvKXH0hmdBuhXbBOajjdA3CAxQ4nHAFkHVVbJiZuE8d8Vfc91qgITcVz1HjclFH20lRYXZsXIbM-krMQ7U1KPAT93tZsV5iT34DDaBlLlplq4pbvQCkuAwCo1gktsIsyHBQf1BckgBdv1FlS94ijWH4aV-3cRLVgOMMm9oBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOBR4KRtfRzM3ISRNjlaoIqQUARPC424aZ1jquVafeJwNDAgRsyLBtr0N8hBG7bjBWrNhrq7Aka370BVdUZFYWi1bdtPAK7cHLj3nmsKsl2P1mOmrSpmSbNqIEP5HX71y6RJVxJgzdfKnv9qOF4yc0AYjsxnPKucZ8Zq8nm1rmo4IXsKZAzqPwU_QqTCsNFFlAP7GtRYY_4Fc-ckJwjsbu2vB1CeHE_pf7F5diP_EdHxbSzsbQLe0mP3ckKpmCVZE9QJrgAMhQ4ZAXOybTp53XKkj4DigMuZp2xPNhdMnjv5HsdlooxYfnMpBO0LRSv7jiFIYQpJpktqZJP9C-XE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=fDIY_eQ1C_rCXYTAuoEk6VOgHooGj-bgOw7D7_lJsrkjhebq0QVAtCQeVGpM2KupGAeNc_2mu8lm7jf1Qbe9q-KOTUUqNSruoRs2JPh6l5rQy5SfjCyGj6IoAn3UGgyNb80_RA3xPAQ57qHpUy095lGINe0jzTGqwUiTKgZwx1mrGcyi7mvdhZnlbNa0V09CF3J0RAeP77aUskozZn_y23UqtVws19-7x25ElaTHg2xOiIB_mH1y4ldE0K6rfdTrXteDY2-fL8ir-pMal4LHGCSqSHkmekmFGK5ZeeC-HKGCwcDU7GmnqArBZ3JAzRTViDN3FqbD4Z24s7GDuwmEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=fDIY_eQ1C_rCXYTAuoEk6VOgHooGj-bgOw7D7_lJsrkjhebq0QVAtCQeVGpM2KupGAeNc_2mu8lm7jf1Qbe9q-KOTUUqNSruoRs2JPh6l5rQy5SfjCyGj6IoAn3UGgyNb80_RA3xPAQ57qHpUy095lGINe0jzTGqwUiTKgZwx1mrGcyi7mvdhZnlbNa0V09CF3J0RAeP77aUskozZn_y23UqtVws19-7x25ElaTHg2xOiIB_mH1y4ldE0K6rfdTrXteDY2-fL8ir-pMal4LHGCSqSHkmekmFGK5ZeeC-HKGCwcDU7GmnqArBZ3JAzRTViDN3FqbD4Z24s7GDuwmEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7BtlWZDd9Zl1bU7UEC9uUY4aPye5sXZbLfnVUdaBWk46OyoGNMd_WW5XAjqkMye76qwx8zinegFouAwMrDTUwL2IqMDNJkD4oL87z0fsDKWw774cnif0JtcmAv43r3sK5i8B6242sasLJWGpQ_vzbMSc7sTx80g_vskXX_LmmEORMckojWK_AdPIUPz5jbgReinuXAl2NrzgxAaZYtwRzTG_tQFrbBfzXFip_A1b8iFzvPM6Ci6U31Auv6T1DIK8rrREMM0-hz-8M6oR8-QTGwIfkdfTkZiD3tD8E7E_pI8Fzc5GVCTE--1UAOkyGP4j7TPWjN9g5kXq91rqg2gVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMfMSgklDDzcVTVvVKVV1iuIE5zsdf3c3G1Amwb8Fz54cuE0mEKRRw_xEdWzRkPdP_la-Omli_pCa6CvUq697ci4fd4y8dHAGLgL0GKbCiUtEOhLX7bKOdjaF0lrngPKc9JTmAABZVANAraboTTBiQBC6WKBc0XrVr22TTKS19cv2ewpM_axEgnUSKVWkfDX2iE6AwAJlk7xyAxKUnbv8dh8Ni2KfRDDSZG5AVAUEGtUdhKgZyQnQvnyw9jlw8D_tFEYHyJSxRGLxe3U77BSzfvZRv6S7LszxYn8-TzC76OJEkLhNItDMbhq7Tc478xaJOA8xMqkxrtuvGcbdqHTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPxe9-pvXFixp2r6hKTGP6pP4w5IGzUgCm_4AWzBTV0DF8ERquvvAEt0FfnzhL1YlItwLATdgCWfEqZJk3k911mzJECg5AuqUa3S93WSbB4OM5e5bDdNY4JENNG_WwQqRBVzyiXO0axP__uhFNo4n_mLWbo53FKROAuhmbxRTHb3JEORI2zWcEbNariaV_NkqUv0X4CUWYRyP2fhGTNpMwWgPKtzDXTnr--iblwtNjq_7u0PxTcJVRFgLZ0mOy8vIStWTKMBEjrZUUvGlSgq4LfKUR2I7GeC_I68uxssxg59UpgIistw_HrS9T-34SXgGcZJLPfdwRHmRP3eWZIFjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmw9UkoEbRg2UDxFR33zVRMBDkXiS82x3dUJlbd4UQCQGLY42jlL44kLtYwLx5bdvaZJqPuvO3bFzjSShZm0rssTAvQ3mCPb-fJ-QF2csT6nFH4I8IvYGNMsdwJfsEvF2VeIu6x11RJi5DbzJAnazF97luSGEFkuIsQitGJKRsl9QiQxYnMhcU-TnEzj_awIaYOqPQT9lZU53ggA5tgirD8OkjAbH6j5_PJHe8TklRpzZlEl_ZyxteA4p3kcoEev7CCmi2pDbuHvpuUe_dmkvxpWsz7ErrQ-DU3tHr55civwAGV5mW9D5_sMvYho2qt4lYoCvz8lilZ1Uf6EVa5n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=I1UuOc3kna5-JlZkbybxI43PgFikmTKs8RrRRp0Wv5KuLi3fGCWcQOz36BXryMoPJtDRNqghG7tF-eTmPUJls3iuWwmM4qpM3nmkStiBiavItYqLSEXi0WPKr_jA3zpcXdSMasjxtief-VGMyzgud4KML_wBH7Si1FrJKGmiU7UB6bqAcYGFrU8_0CJoHdw7_yAG_rvyTJIryAkHbA-dTB5jtnm0lAc2facMV0nb8zaNW2Ndrd-Wz8vHz0qloCFGiNNkKB-o4BkT8aro7EJR9Kgr8GmjLSge1Cob1awNB9L4yqBmyY0Hr8Ubua-7gciwQH3dVDEA2_lLfSrYTNbs1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=I1UuOc3kna5-JlZkbybxI43PgFikmTKs8RrRRp0Wv5KuLi3fGCWcQOz36BXryMoPJtDRNqghG7tF-eTmPUJls3iuWwmM4qpM3nmkStiBiavItYqLSEXi0WPKr_jA3zpcXdSMasjxtief-VGMyzgud4KML_wBH7Si1FrJKGmiU7UB6bqAcYGFrU8_0CJoHdw7_yAG_rvyTJIryAkHbA-dTB5jtnm0lAc2facMV0nb8zaNW2Ndrd-Wz8vHz0qloCFGiNNkKB-o4BkT8aro7EJR9Kgr8GmjLSge1Cob1awNB9L4yqBmyY0Hr8Ubua-7gciwQH3dVDEA2_lLfSrYTNbs1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrEnWEvv7UAKgqjPljE9psaRO6J5I9B9hKnV_H21iMx2WhGeJXuirFeVUPH3MQYQVv6l1Utav_-mOu2RONv1nIJNRJdupdlZaOll3i-eHwVpj42nKvVf89glqkvhCFiNaGoCKtuVcmkRc7Hjhm7kOq2_HQIPMIaSgXk-gU5ua0TE7JDcWpRvIhIIxDRBtobVMx6gjSXhXiHpIU5T0NRpjafOzJ6AWICPzziTFVRTGIH-Qe5rRfGvUp6SKPgBnyvMVZljNrpJMXRlS9_Bcg4V_Qwpgg-VoU3TSCncDeqmNotUmmKtpDsupDLqpjlBe40lvbajI09671UfTifP5p8Bug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZOdoAt4XeyAZzYichhA29Ax9XAXp_IP0HFJBHJz12cM-S08yEztGXMNA1kuG7ex9hwlEowzV45cay3YqaSBbdDBBapx2OFa--N_Xt_7paNE9frjyKM-GL7MFvazEGTJy1QQCI5hndAXgEeSCBsxI9exxkdt3LVUDtiptJyAdyM3hl0NQHHD9D3xQgho8lNvJpaz_FiojzHR4paaoVq9KKUjawqOJ2AYt9QCY8kMpd2YLxpYqBQ8QQ1qqwSWHfImfnWvgJnD11Z-LEbhRAMrX-50Ds9WW8PzeB9k_clIMiFPkD3EfUQBDbE0NPnvOXdWt1OXHtUrtLENc_MZYhfTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=Hzt9PbtOyCwF7cBf2lNrU5VgrG_RVHBZgtPewhNiiO-iTZdvnX1_Ogc_UQ5i888Nx9D-z3wbNL709uNLinVlfHI46Qo0i5ikQalmk8xOZuybsIoR6Q7ImWA0BJLgx_wdzr_qe-q1A5IHS-8VYeQsJGcYj443oBTlbkGlp4Sc9Joxn-qt4lGEg4TyBfWM2_Ba94uzrY-oV-_Xu6O2u0CgTSG8mbihyGg1w6g-yOZtIb_ZlJpxL8rVstG1uDJKbKY858h8FncTSZRj5X0U6ElBG5fWCIbb5D4Gz4LTnxcUTS8CotjsMQzVXTEtMi9pTmYJ8haLc-oOx7EK1nriAxuWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=Hzt9PbtOyCwF7cBf2lNrU5VgrG_RVHBZgtPewhNiiO-iTZdvnX1_Ogc_UQ5i888Nx9D-z3wbNL709uNLinVlfHI46Qo0i5ikQalmk8xOZuybsIoR6Q7ImWA0BJLgx_wdzr_qe-q1A5IHS-8VYeQsJGcYj443oBTlbkGlp4Sc9Joxn-qt4lGEg4TyBfWM2_Ba94uzrY-oV-_Xu6O2u0CgTSG8mbihyGg1w6g-yOZtIb_ZlJpxL8rVstG1uDJKbKY858h8FncTSZRj5X0U6ElBG5fWCIbb5D4Gz4LTnxcUTS8CotjsMQzVXTEtMi9pTmYJ8haLc-oOx7EK1nriAxuWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPwVS0uO25FdoeO8z_Cal6YXVpW97ebv6vLlLB-uDUcL5ewTQAHHiI0iqCbAGBQHIsnpRvnXcuxk4I2r-kjlwYKZyt1vSrRbm_PDv2nae52j0hTDwSfwVbW6glotJHA5Dq664Dopaz9eRmfVpMFL8NJZyb8xkG-BrY2lvhKjP2Rl7Vq29zsTDFB4RCnSOXcKpuJt0cndv7gdckF8Hy5_o54mEgzTKFtNuFV71MpObgN2bhPyvLIqxEqjsep_us7EhGnks0ftnBdvkUNWtxl9EgDRXv9oT_2a1Mokn0SKZ73bEDMnNh_VwEJ8pH1adPSjeOPhzkaPtNKEKqgLcl9kHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxYPSP4TFK1hy02e_6yM_xIU3YeciMmGUpxso8JCkYo_yH6chokmyYKJbfYLu8BVDE-DVLzpHAF7m6TaCmZk_Ay1ta5pTgoijwje7xwRTgLnooVFYPjlSMLRJMjWLEOy4x9tcFyQm6-Q06kyTzRMJVdYvmUtcrtZgzt0pZlIirKwg0T_BIJWpS9oLltQYSVnLa7s-lOf4t82TMP0cof8cuMHfpg4WRBoLmOrfNhVZO022BofqylT2J40kQwd7GhXHWXCw6NdplU9dfcweWO5IQM5AmsqY3uRue1EO7LAdVUsbJyvpCVFHVm7cLGlWC4JTdVqybQ6qomoEwzzpkq0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elQBjKXT3Sd7F1sI6N-VmSUfCikr9Gk5qFyGZNGqr88dafYiu-_Er8GBeFMojH-5X5Su2ZZJBksgfvKgsqIlb0-ryKVp0N5GkjPXklzGJCy5vq_8bgOj9KbjYOa_bA3CQyPmdhun8-DrKCLnnXMFEw50kXav3asvl5d6XSSt5_JloyNhZXqBPQgrSoiYHpZXrCzeSYvyk8nW3pjqmXhenFRnHLBV9-ClPuFJBrfrUZsgszGJacCXihauWKnQeBKds9KfJKKPR-ml9M_4GwYcrXY7-tK5SU7ysWfU7xiXzsZD94pA5cgTa655q7YxmREAb7ultZBoEsAiVYrafqEvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQtxQx3Ng0zvXaQkDQZ_JCd6Ldx_BYewPzbcC-T2OG6fVM9n4rgEwE6Al837wJoqM9SoWnGb_mZ7Xk236-oVi5u8yAyPAlz2ejdu5aBvtPfOt6RBfrIwHtpX_0RIliI8FDkoW8xzLuYzz9LNANb3mD3_d4QJME7LCzxpS1Sibus4-JoqJ5ms5eeSL9J6HBa5vgXxJkcraPAv9VLwuOtSZq-wJ9n6RwLHDNtjRUhPULl0qITMgfNmjIAB0d_c0IBLLvMvKIIAFfRg6QSQzqqSTG0bA26yYPats8X5JaSJVGhwlsGmc0dKEWSlc_-rjk-xu2MXihMJnq1OG8Cb71NeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prGX9MKIXL19RubM8tcUEUmvZ92Att08hK2iRKLC9_Xyr9Ce7W_iidRZ_80JnNuoiYhDM42TFOt6UkHKQh0DMklPGeEYjG1laJUwzfHuFRxHY99zMX3Ibc3QFPfkCH4dfIroxswQyziCgl-eGFFFAHNCkTTThHYsULjwPjjEr_DsW8fZhpWdiCHvFzLyvXqUtVMoFbJSrg89XPlbnobytCiVJYupKU56YEOvLug85V8fPvrtu80XDUo-8FTKBzZnmDfSL58OfRnSjiN210ggTVQZ_9R0iCVHmRIccHQ7WVA3ZnZXW10jnJ8xArP3dV_YaSl7zrmLd09uwVJejLdZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evy5BPacqBrUNpKjTgycewVSEKocj67MG4ijAXaX6FEMLuyT9I93bDsWsXYxVmJVg4wN1KbwdTKSns3BvkzEEWFiNz5hkaudoPQBaxgAhDDmW11H5QGnvbBVB6ThXrdLis-EwB9v9gODiOWpXZJYQAf7Fi8OZ087EU6AEjo9wKR1kVyuhhdM-ZqjAgYdpd9lYhczyiXCFvXONw4e9CgzFHt64DhyyZ-XsNZPoZ-a4Ma11aT5KR36vUZi0RDUyAqQZo9ZpAo626ZfnE9DKD202va0GbWZX5u7R93Iwg8-5HQIZt3A7B5HFTTbrX_6Z2YcYGg8T-f3H94T9DRdTun4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uf-s6xph5iMB6q1GUnxrEb7SRtc3fSxoZKPCUB2ft7j_Es8EbASkujgSr9o4y_lUIvATTFTpSv94oYsqAf6WgcuLuOuBwO3n59J9Hi82otvgjc-tS3AHtUwfI33tcuhYDRTtYX-ttWbsQyzDIiPt2GvR_Bn5eR-h4X03yju-uGFy72-9nM9thcasDAsTO8k_tw1FDT-M1saW2sLe7KeiErp79OLyHdlLCCwdolBObFvYbuHEhwsEqtJxByQMm01vs9Y9t6u_XB7Cy14yPMNpOfDMAl8kEDtKvmNtxuiU_2lwVawi6NCSYvlkaalWOWeyBph1LglGDZ9usVq_ASoGGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyc1tsWGugtZ0-zenZUp2lzp8mWxsx7uQOijhEkhL5qcR7mWa5NfiqMPPfKwOomWvLK_KDFeHJwBNch9UzuBpuOEb7l9GGcrmrCn5wRfaCZwgBX0reL7V0FvhQwtE9StrjaU-_az5FoLv9SJsQQhozHHjFIrjSnzgI2Q_V4s40XerlEPJzV8Jm-sRbeUrXCiJQKUsbPfxN578-38NE11stoYblHlyDBI_nv7Z6OQklhdiC9GZckFLSuMDfZZN2sEXIbY_zbG4A7mSfz6L7fniv2iW-9ZyMW41yPBlgrQuwTV1WuSKNOYeQ7e0EZO8uI3zDKU0btDJwk4XIEmZspwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShvyV57acahVrGOVct9Q3AInuEZ9GJ0hactLdHoUbLHSI_VxTRSOw-uZl08znPJkDbSBtNtinY2fgeMXCcnrjnfHthoxrEcLdK8j74FTWIIy1frISSTblma1_AB-6sP5AjT7lJMzojqHP8A-61V32pEVrDGsL-Tes7NAvCmLJeT6nQAjC7UMvU5IPqw4x2s0QF_JvJb92eLhfUuBMXj72aS04XcXC1ZoDq1AFHaS5gh-2BQKAkfMhgzZwMlAIOZB1a4rjrqZAzGwch9LiuxMOrmkjKB3lLOw8U-8sikqMBW5Z79lFiIN5iwyeAj1tNqy9Xp4qMyjXcAYPaskudz8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhFiIrH_x7NCxPTmaL6agrl-m3U6lCVKRSbyx6oVxD1RhxPeZkWDQIUlirizyhoISYhYrxHsX4z1_O9YF7kvuy3BjNQBSsPef34TfR0Yq_QoWmd8pmu1TzUTM5YC-g2axbmumgc4YGJQmULWknaHksJX29tyocPHWh2z__xByNdz7PXzyDYCQQ8Vs48WCRWDDt69C4RV_Npm4Qeqiwy9MC4vg6tVz8x6UXR8mDiP9E12TJPprP5Tres9cd61Vj8jWrOVFjXhy7HvD17f-hebJ2dv4erKqy2DE9XS9TJfWQwbipkg6fGwxRoDoofpNFTHkC2q_V0j46suKWIB_nfBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSZRM1dO9G2qaJ-lZSenDetwuBOdFu-sJv2KkaJBZ2nWKask0NYNuftF46DttA0BBoJiWzQCzeMLxU9g-Og9qFmaZxwo8pNTb_sKHdG_QzY0Bt0Tq4gar2GMjBoDv4DD8as6we-UrYWpAWM2pCTNnaK6YaqkPXNbeSMKfjr-pl8IOiQ50LDUeXmrQLlMQ8TERHAt3DG0-Faa7VfabrYdhD51wPmzzAMP-Q_idHZJYL7S65JdaYENppxhHv-uP4DdpHOh7iLuMK_dSTRxXlYQQPmglfa-ioiTzdrjc4nPTpxBHR9wO3q-qiLHySEPRCVD7U-6i5klLFF3Xp4KdXRWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=vJmVPptpNaXNuPh6bz9Y7RHNKmNJKF0POH3OVdqzlHv0XymTk6AjcBlcLt54mFgukPASk00Sx8En6dsT6Rgt8XBhW2jBLgh5V28-U9TqSo1yS8lNkG59H65x-PVPx5ljYQglFK1dCnaRWz_2tATc-0n9_kTHy0AVDOVGO6sRxVnx7X-dJ77IeAw5ZmNl8NF7eOxwzFlmfLtcEe2aZeS7-5a-82yrcsZV-XA7ejjMOrGzpMiWzxvJ5qZ8xQYDgiHgtg0IdjaGhFBqCvf_IU7Q3zzSyLI6NY7rQudqg-nbuyV4z7F9tEVIz8Yg7JqeFj576n4oIcr23ZttiGwpsfkg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=vJmVPptpNaXNuPh6bz9Y7RHNKmNJKF0POH3OVdqzlHv0XymTk6AjcBlcLt54mFgukPASk00Sx8En6dsT6Rgt8XBhW2jBLgh5V28-U9TqSo1yS8lNkG59H65x-PVPx5ljYQglFK1dCnaRWz_2tATc-0n9_kTHy0AVDOVGO6sRxVnx7X-dJ77IeAw5ZmNl8NF7eOxwzFlmfLtcEe2aZeS7-5a-82yrcsZV-XA7ejjMOrGzpMiWzxvJ5qZ8xQYDgiHgtg0IdjaGhFBqCvf_IU7Q3zzSyLI6NY7rQudqg-nbuyV4z7F9tEVIz8Yg7JqeFj576n4oIcr23ZttiGwpsfkg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV9DWSRgm7MvT_IuDJWQxjZ3g365AJWJNqZZZAAClpmQ15ONqc56bYj5JeBBbz6NHVqupKrCbUnvy5jU8kcecpUo3rOuBU9OiMD9ogAU-gdewtccZmAFzJaStP8fusBr8r2473_9rJJMgNHxKevH_thonORG5sEyxaeVlcVK7vKIGgVvWctmCzE6FZ7mMxGbRhgXwqhj_vN2pZlSKjzRnkSSTTUX1v26y_SnMSe2faCHICtKctmA_4I35AQx9s9_GnN5dy-m8qkZB_Kp7AhD-0XcVzx8m60Ld-r4KapOXnlBsbQTiYzcd0gdUZMsFe7Jnlpq2--W28XZF6S4aAluqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzne9zBDAOGpVf_3gEgmsgMo25xv2r72dLFvb0hJ3cQ3QQYCOHaphqEcNoaou1j6KflFXUZLJKU9B3sqJ9KjVd-QAI_qLDMoRtrYnO57nTclDhk5-rvFE7kalOQxn87aZLpk7Su7LLG_LPUksYYhwMXPwlgYG50NcKP-k8_PlJC-qG6lYOrmYWGAYJAd41kMFkxQWLiMcVovznMepCh1bWjlwPeXQOjF1IdxxjPfpta0w-coPsLibKf7TDu7MRdrMgDfEMnfHhvwWA9cTKx3l4EpKQLclDHoVhr4wW7JsAENH-pLSFIz0cDHm_E6VtzgWdP45STe5nG1eg3RbQvZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLaOWpWcL8EvQLOUbTOIG84aom1XTNUzXPoL_TTqti_CDJ2BF52Lp3GgDqX4QeW7k6XO0mHE0VpjSxrQfI6DRxBQZUJ89q8A-T-_pN3LLPj4nioNoaWDyONSnjyWyrHLzMysfpDcsetzxaC2Ct6IALOcuePF9XGGHPSG6BvEMCTkC_qGeJRq_0AAZ_oEwqKSRQ3LqdLJxmlSOeChJRtT5-l4QSyY_7NRi5BzoMOHeenE6IBYAMwZ5CUMy_SLRhh8hzRAZBp5NexfviF8qio3je3llGkcryNYLcBeEZjClsHKA9HqWQ-11ZDGRPO3ygXBFCgAZ-UZt96DiQdiSf2ebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjyJDiG66eViWeGheB6i8A6LLOTjqsejtvkdTqaq6vvfxyG2m4yaRp3CT9YNXzpwK4eHnOMj0V66HHd4m1ouFwbbKNuZq0sXASneyTtSAMf-xWHP-jG-_4nmzL0zzZATBSteBcvTudrDFS1Oko1-BGcigEP0q4cDeJS0uyfQMCpljkF5lA8JgnNtdlGQbjQWxdHfcS7Iuhq-BNKNkXbtdA_rFTucW5tRL1w6DDKvMZN7BVOnLpokwnSkva9LSgCeQbsKrynY64sU_ajqW-dGBNUcS6NaEuBKGVTudzEt8o6LqURzaioqqKPmvXQE2QCMWTBGGSXiQXWBuGD1rJP76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWaDHigooY4GQtmU0xWEA6n7g2_92J6pQWoG8cLIhGEL_K0NSSRwutE5Gr0IPUtVIwS1kus1BAmgheciSq00wdN6hWnQFmLuRcBSSr91zyWDlbmqbRJYmINw7ddz2lMSDDpetjx8MN-NqzE3SNeKg26l6bR_6GFOGIvu1auM_veNfbAkF5Tzb6L1CjSEDficYItlIWzLA398MxOhDvpyNI3sNd1rigA8LSumv8Cejf9WOZseCl_62O2y7SSi05GtH2RPS7z6CZwnZ55xuW6O-qodphK5PPb2njucnjzDwBQI0V--sJCbiQ_9S10gIUzlL5H1IfJADujbDg7_auLidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC8jkXCKiSDKSa_QYOc_F8VduIpMGV505i0SnO1lr8betzxJU1-lx5PEB4EaM37ldbmTDaH-ZghpAZBajmrWsAA1XNyuGG8rh_-PmxI9fY1CLxPrjXCYzE-vWnmStVBVPCPyEfJrQQftsojkficlYaL5woLEBCIxUMX4tmZHgq_s41UUq3KDWYKgSuUCEi4tpBsf-G63d9GZgmlmPXIHBwRo4OhVP2b2IkuptvYWvtGHRJRxeI5uQgMV_XZ2eqT1YBZExVaBhlBjcBJ-AKtXY7b3xPmvyLmLIBYRJVVyAiOENQJaY71EUBpxIBAIn4WQaHo57BbDP0w9Yjtc8ov_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRCQ-wFM0Zg86TpbV-AgFoI-GtFBPMrgG_S_8E-VIWUaxGvK5qcyQU24r3Gtnd0FNfGtpL-Me4s6ECtg9K0Bpbx0AU3ISpo59c5u-UjUPJX7qddK3s5bIXvx2r3SGV3OkiLBuVTRoUqpLGxPhgBMyWsU9JFRCbsHJeAKbPbCVnLFu9GfJLLC6wpJJIzlUHggK8U28M9KU5BRMKTT6fdff5g800BEP_FbSeL5umHm4qICLKcbeUEC0AmaUDUkr4TvbXtUXQo72Q02t1P5SK0yCQM5XeXliX0w5SVo4yh0wo9GRu85GVkXM3bBve95DZ_eind3jb4hxFguGUh2-xLjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8ro8wz5FtS7HMXx1MOx6GTOeaDfb5oaGAwWDMxZoBw8dHL_YpdSxV1r1scZlXiyzg7yBfeH_US5e50eBtGK6WbZ0fJjIX99DKSHjqsqbosxuzkM-JN6NNtZMxXGrKpVWEgFV_oUSdh3134mSuOWZgvmRpq6rgGhB07X_gwvf6_bgJlnTDxrqcdcwp5MVh3g9PNjtkcSvtI1rrX6Q9rv65e7yK6NpWAC9_5mVR9-Y2NVyu-DUV4U_N__8iImIRir95ZI-Y_skAmV8aJRsWsExfAbg5iRawYLPRzRBSucsmHlPcW_k7f9lhzva-SghxRKbOx1fpkdW6JtkPUG_UZrRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6iECHmFU9iapfspbmeUzmh89DwXp3LEp_JDG-RYLuWXeUQOc_Qz4RCy6Om5RELIbdN4TlxTHcPgXBMNwA7YClKH8C3B81WxjUu_vSJ-BFJcYajwq8pmZKLCGNofW7R89l_YHTQ7ujeYgsV5RVLe-KisXonLEJRe-ftXHkaaNJwllI0LEWay47Rx0W4Y1mQaIXsCzv38BOLB56L1as_vVt7MsgxpKmxG044P6P94P6xtxn5uZqVmiufW7r0JZnUqXdIJmF-ClQgUWdh9rSqD5Uqb1b2Yoc2eM_oZ3P60sMBnpu4mcBbKFMvP_uLGXg3rtzCoO676FvNdMI8JEirNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4tRno3TDwGZxaor8UBR-wCJ_x1-sihGzJXx8q1Emhe6wgTVxVUQbuqA0N0dNhqDXQEvVE_OsE1cnorAh6madKoGZuykEvZaXHeNKK4eMKOvqWq9cLuSh-tmKEyXCEY8JftlSKuJTwTBWpr4vXOEpxBIsZ543LR7UJd_r2lW87EaedrhiTj7DomS5phVXCb9woheg7hVsk74yDBfKv3icsFYE33X2akPlBPC8_kogQSe9ui2UwHYM4VU-4eR9dHR1U9SQqV8QVVF0mUO45VtxT6JpIYzAZvHwVS6HFo-iMFckWBcXURwkmirjI9UP5TXlcfcmw6p0vnqIHLKs7qVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
