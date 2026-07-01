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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 667K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-97363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQPt9x8iwmRfnVHK6lK4tz-mjMkYoEEJNY4v6s98J5VDksDmcI_DzgY1X8vPdx-5wPETzgNUH1LOznWQsc-SRE1lHhipo0UDnLQAXqWDOPo17QiZlBYX_CucCmtcvKWYTBqOll8UgZ2iCgfyrQxqM4k8-N7mXm3PlgxqlPPUML3dCr69Ok1dXj7zXHXdnLYKtx3dbpZaVuie-Xb9-Q3Kkg1uE0414m_B8w3xDNfmhfZ3AJTLxKKHXWJMt4grWP8E7XZz99-s6zUpkxKVN-HCHTOrJHQ0eCxzT3u_7AmMFaw_OX4H1cFdly0znMeufsqpoxs_73jhihkA1szykUt7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
دیشب بعد از پیروزی مکزیک مقابل اکوادور و صعود این تیم، 1 میلیون نفر میریزن کف خیابون و جشن میگیرن که در اثر ازدحام جمعیت 3 نفر بر اثر خفگی میمیرن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/97363" target="_blank">📅 17:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgFjfLO7WChKbVA4znt6teBUmAJddqTbpxEt-8DWcHhuQTpYY4fR3eaoF_Y_g1tTLxflNfICJ6yRiM9xjq2m8k40xzWFykx3H7pN_chy87NENl4emjw13lwoFqyvW-PzcfF9m-VInQ-EnE1K-3u8OBNlA26Syw47wFp8OVoeCjuwZyGBbEtHwW2hhsMZECPrT36ag712dDiXJKQFsiwohLtWIXqGBpRsLH8TitqTnY8gPUQ1kkwzZh-qqDoAWIQ5emBbdfBrYrO2HWWG9KYoYgoxPXpcvFPCM9XQq0wNTyju0QMjMPnMUKKLvIZj4ydMtOg9mZfXyVdpOlsrU9e3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/97362" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97361">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=V2guZ1g6TCCaSxxcF8WvnJsUSypCRPG-by46gTkBQFhgeyal8TipE8EnZCCUrOqhKkg3WXW-p5DgUt3m2bMEEPZnohqErjaMF3Tje-17v9jg7rhSp0o7mlSJ1Dv4AtU4hwJOMI31giqRKEBfnn1POc_JGmzrTcN7FEctohjPdYcg8dn9HrstbDCC2m31Bd8tx7eQesBjCgXpgvLhT8kVD6K0Fcera6L89OpPnUBNCdbrWDNMg3tPk6sZXqBKwLZqqWYGPpUsoiRva_rSudaUVKrUEb04sG9o3WhBOaiEcj6YbvF0qaQrd0cV_wUih2qDiq_qGeX-yirBIN6VURF_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=V2guZ1g6TCCaSxxcF8WvnJsUSypCRPG-by46gTkBQFhgeyal8TipE8EnZCCUrOqhKkg3WXW-p5DgUt3m2bMEEPZnohqErjaMF3Tje-17v9jg7rhSp0o7mlSJ1Dv4AtU4hwJOMI31giqRKEBfnn1POc_JGmzrTcN7FEctohjPdYcg8dn9HrstbDCC2m31Bd8tx7eQesBjCgXpgvLhT8kVD6K0Fcera6L89OpPnUBNCdbrWDNMg3tPk6sZXqBKwLZqqWYGPpUsoiRva_rSudaUVKrUEb04sG9o3WhBOaiEcj6YbvF0qaQrd0cV_wUih2qDiq_qGeX-yirBIN6VURF_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
دخترای کم‌سن‌وسال با دسته‌گل رفتن استقبال رامین‌رضاییان تو فرودگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/97361" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97360">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aToDUyyj38bs7KB5WgODfXJEUL7C2mQT8Ev8TbHQOnzGNXEc-IwupyMwviYM-1RCvC1hA-f6StlOVUChEyRQNp5py6zthtgEbagJ4sM8zP4HqTyz1UGat7ZjlQxjlr1845V6KP2VAJ4pa2X-XhHCCBjAzrJx3GLebJCf0coyp2QQB16wksSw4MOGQuiLaTVAkSWZLDvsIaFE1qQIFaVjW3t95iepl8iC7rNjvqoVtkqLCJGUM0A-IMFVv3sl0FThl-5lRz7dJ5ZrsLqAx6CL9_9R-pbm43QiTBYhuzC_WGc9zu4ttSJeV8Fne_Lwh73XH9jJKfT805d6RQAJfiTb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#فوری #اختصاصی_فوتبال‌180   باشگاه پرسپولیس به ریاست مدیریت بانک شهر پس از شکست مقابل چادرملو حکم اخراج اوسمار را صادر کرد و بزودی این خبر توسط رسانه رسمی این باشگاه اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/97360" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97359">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axxa-gDK1dtwGNtsFYGxnjyYA3ookymESIVNtmCzi-ZWVdSunX4kTu-tl9gOSr0443TG2WC_36sbtT7HsxCL2vaU8MFOUjb5qO8Rwd6-KWtO_sAOpENyfnCs0SDh4yQyNW6-48HIKAwAxKIRYGTLyMkT185vvHQkG5LFSnuvEQ6emLNl9AD20XDoIfYUqomYc6lkOW4Tz7owfBvZS5QXo4yDs45kqFYpjY3pw21h8YAqFr2xrkUaMELh8GY-uOKHIsz-lTLRwFJojc1ECAMg4R3BYEQax-1BY6s7AQOvY25L9jLElHn3eoOOK56u2P6yNnaodavLlFKRZOrr9szUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇨🇩
سایت Score 90: ترکیب منتخب بین انگلستان و کنگو قبل از دیدار
امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/97359" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97358">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwqAgSGQjGG2ww4YzYH-zRaHd8yMkR04kRUzPNK-GeNmUVybfIklEcLhSli-8Sq2--iv2XRcIlVb-FPw07e1V4iGWe77FJu45-OKXcOnukU0lQAB4G7OhNFIixkvo0wpnj5uLCXSmFrN7sEXAqfz_JpVR9OP6zy3uHWwQycK_8-4Wh-qU0El0V0zOGEYEnZp5lrHS9CGndWzo0ikFIbQYrgyT8-vdb8O7GrvIQTQmIxMCwtGQ-LyjHNjl8AuR3_xiKLjSuO-rlO4FN2MWQLGd7CDUtBaJJdGFYjIIR1w_bcJhF3m88PgjUHRNlwFbnuY60Q2dAwGBBTSMGl0ujQScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/97358" target="_blank">📅 17:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97357">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUnlTfHgfuZ3ReHy1cEqZGr25wVcrfGpJm6Jif5yXd84SX5vHWQad7KwQT4bZ5r0ImH8Pw08NyX8vNd4XXiLW5vvaFEp2H9rBVNchGELwQIZ32rHoxBZKtipxij1zYdFD_pF4JyCgCk3msORpV8V5aRa634L_xFCMTbNjn_GQLzzo7IjFrjYO8ricaCxv5uwfgInfT9QbbezOTpL35QdAbMLMdJ-v-XGIOWhPBYTA-9MZfzqKHJl7mHkIYWfFGGajl7HT0vFkv2Fi9uv9KVlBjYhDOqAJfsynKi1BtKU0Nd4a1X8CGOX1qnO3apgjdFpudBPdAqVLca6GcE6ITaQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فووووری
؛ لاپورتا: ما برای آلوارز پیشنهاد جدیدی فرستادیم و امیدوارم در مورد تصمیمشون بازنگری کنن و این پیشنهاد قبول شه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/97357" target="_blank">📅 17:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97356">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=vGfUQu8VeOwzl-Z52v0-9Mss-24NsWYLZF_zX9b1gwCBFzfbZo_ZPDr5ql2vKVEDAknwwwkRX3kaXkbEI78nVTArX_GdiWoYzFxEiaEiWTll0rlgzhgCWJIk0r_Z7VlIDetB2fLBv5FCV3_WhA3CYyOaY5HZbOuVG3EaCSlSlakd1XXDF-LxDS13QDhirUc-T7AjerxZVtGUwv9MY0tko9-kDdCH7Hv9k9fgOWPkJq_PlByKm-_2pppZeM2Cwht7PFv5CuceameeX5hed7k7bpR4xIqv8NMmlrJUNbMz13gdmmwAhAq0TtXPULwMR46bRlxVGACo0xXUdPrGwoev_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbd905f72.mp4?token=vGfUQu8VeOwzl-Z52v0-9Mss-24NsWYLZF_zX9b1gwCBFzfbZo_ZPDr5ql2vKVEDAknwwwkRX3kaXkbEI78nVTArX_GdiWoYzFxEiaEiWTll0rlgzhgCWJIk0r_Z7VlIDetB2fLBv5FCV3_WhA3CYyOaY5HZbOuVG3EaCSlSlakd1XXDF-LxDS13QDhirUc-T7AjerxZVtGUwv9MY0tko9-kDdCH7Hv9k9fgOWPkJq_PlByKm-_2pppZeM2Cwht7PFv5CuceameeX5hed7k7bpR4xIqv8NMmlrJUNbMz13gdmmwAhAq0TtXPULwMR46bRlxVGACo0xXUdPrGwoev_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ارضا شدن دسته‌های ارزشی از دیدن هواپیمای تیم منتخب ایران در آسمان تهران
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/97356" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97355">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAixx9vEGUYdjEMR0bBYQxKzpoMo2sLt2XCN2c5EpsDdM0SsU-u9x96t_NSmGf0LoHXt_pGKRiFLM6FilVbmsqkvzw7VKqyvQ6SS8kgwLNovpy3BA-BiKCEyJuKNYaKU1DPJaCghl-yAyTo3h7FuOzbKkGtiU1V9ge2shbiJsI51qo2LjScAzQdbZZgEF1ebjwcTsrSeuzmEiDLTZzzhgYWfmj1rj1SE3o_uKTkizqULc6m1lglhyElaurMJSc3TPhxdAC6_mHPBnsbkDsWaSwNcszEiF2rQuZSx5ZUR4HX5fgRc2SU4r4qEn5IjRCC_0tVYCYMQ-QSuCGyWF8cvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونمایی فدراسیون فوتبال پرتغال از لوگو جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/97355" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97354">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/97354" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97353">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plupn60FEKHo_PNLYoSPd31BHg7nzIBBZ9YMjUwUaHNY_DGrIQ3vMFj5RvwOGeyfpHlUqMLk298_NjA_NOP-FdTHTtH--NBaeTay41274QAAthVSNGcUe7HKpt5n9ORz_FSAFobWQofZhoSwXO19OviiOczaNfxCJTXFwKa15xptrqZQYPIFptElEYNyik4to4fWq6GUQ3zZqzPIFHBz40sRatAb3_jl3TgBQpsSfmta5Kj0uImCc_W7s0F2BIINtsxz5KGmHKKtVnKZ4UXkwRIfEHG374gUuJETo2lK4E14k1Us5a667mqeCs47h77VgDuZheCX931xQ1cEyGGjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/97353" target="_blank">📅 17:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97352">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=Ls2Hl-MPfDzvSa70zWWQMLhXGgEWn2jkGzSzk17zXPj7d_-EIwzhMIbtE0k_ByCwtiTYI-I0XChPr7kik_8hKEjxrLQAT24P6lJCk73OXh7d15UA_t_4Fu49tGCDWQ0GWhP5twd4gyqtNeMc-kl5AxrTktuRGvuPNeTAfAH1DpEcjxbF-d8wo6X1kyCm7-x68A1cMJ6KAAtglaMYbLMC638epj7XrWD7fnhNLTdodR-i879-rxH1LyR9cn231ejB7k8DyiNT6W4_CiKAl-K3Sn2zqS4pRRSG-cEhRRe7K7eo9Qw-gv1OTmpPKCyzWmfEhZDWn6hKK26o0ZwREjDH74zHmcn72TS8C4OBm-TE5ug17WBB-VBXOuJiKQs0NUEYAiiew9kKMaFGTCNuYXmomhlK0UFw3U7qlkD38280usDYkXdt4zGsVRP_-q0dsPIDwCnpmA8a9oPFMt49gyt06HGsRvSaKpfsSfdTz3YzfnH65tb397MWCVuKupQd0ZGm5ngHgn9f2Qx-yoi0yrk8dusSVhVUTBnFbD6FHLEBWQBGfTdndHerOlk3MlS95dryVLAr2gzlK6NtVS5IyvJGuIJ2sMsJY2Z7ymTswrwO738j6_3VSlIm8uAmntHyx3IRkTwvbrJ2kw_-bsgSWbFojhbpGxAyR14FOofRdy9xXu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd1a0c4bd.mp4?token=Ls2Hl-MPfDzvSa70zWWQMLhXGgEWn2jkGzSzk17zXPj7d_-EIwzhMIbtE0k_ByCwtiTYI-I0XChPr7kik_8hKEjxrLQAT24P6lJCk73OXh7d15UA_t_4Fu49tGCDWQ0GWhP5twd4gyqtNeMc-kl5AxrTktuRGvuPNeTAfAH1DpEcjxbF-d8wo6X1kyCm7-x68A1cMJ6KAAtglaMYbLMC638epj7XrWD7fnhNLTdodR-i879-rxH1LyR9cn231ejB7k8DyiNT6W4_CiKAl-K3Sn2zqS4pRRSG-cEhRRe7K7eo9Qw-gv1OTmpPKCyzWmfEhZDWn6hKK26o0ZwREjDH74zHmcn72TS8C4OBm-TE5ug17WBB-VBXOuJiKQs0NUEYAiiew9kKMaFGTCNuYXmomhlK0UFw3U7qlkD38280usDYkXdt4zGsVRP_-q0dsPIDwCnpmA8a9oPFMt49gyt06HGsRvSaKpfsSfdTz3YzfnH65tb397MWCVuKupQd0ZGm5ngHgn9f2Qx-yoi0yrk8dusSVhVUTBnFbD6FHLEBWQBGfTdndHerOlk3MlS95dryVLAr2gzlK6NtVS5IyvJGuIJ2sMsJY2Z7ymTswrwO738j6_3VSlIm8uAmntHyx3IRkTwvbrJ2kw_-bsgSWbFojhbpGxAyR14FOofRdy9xXu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرزشیا تو فرودگاه اومدن به سبک نروژی ها تشویق کنن ریدن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97352" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97351">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTH2XRPqRoPEkgbGY9fidogUKMtEW1xlRTm01JaYaaMNLzli8cuRWpP2sPfp2BGifUt4erNaRn8K46qtJiriB9LjT54YItbElj0moQ-zDCbQo1uRC8Yv9mFXEjfHujm5LfYjMhP9U0VPRBECWFDhy14Ucz5UGzqe0hz35Nl_qepKY-tLyapBm_9uEQ3aMJMYPDX9K_FZ4Zzd38FpQZEBHyuG1hLkRyLHkfcdCo-N6QHCIZMcNURdFT17gRIkDvBpweNdnOILlHDFQS7NKU0rC308u15vO2u5KnoVrBGKpyJbYMuRR9jFnRceRrloGvVWiHVGbvvlKc4_OK9Cmkl3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونی کروس:
ما در حال حاضر هیچ بازیکنی در سطح جهانی در تیم ملی آلمان نداریم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97351" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97350">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=M9uTiO-mYGdCfivUapi-OngipmIzavUkUSPU78LoVAloVUHPgepOvsj7rh6SCrwfBft_yssltH6qqbfK45tKT5fzcTQHHD70EaD4_CgHx21Cq8noiS6Vl-b2URJITVwCkWynaHsjvKyMhVWAzcywxwqwzK66s3Jj9DjDzmVGCOLZL_O_lqjVtoiuRaHydKhfH_cJUf-yMu3tZAG9YYPHGxtDrbigb45SKvZEVgH1zHlI-pr24dlzwMmHTlN6oRJhWHdh-R7g2_b9_UcIYsHrdcYpWVuOyPOw2lNm43trEagt0XnlJINUPEH-G5k7uEKXWSavdwXXIXeavslVhWZopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a746294c0.mp4?token=M9uTiO-mYGdCfivUapi-OngipmIzavUkUSPU78LoVAloVUHPgepOvsj7rh6SCrwfBft_yssltH6qqbfK45tKT5fzcTQHHD70EaD4_CgHx21Cq8noiS6Vl-b2URJITVwCkWynaHsjvKyMhVWAzcywxwqwzK66s3Jj9DjDzmVGCOLZL_O_lqjVtoiuRaHydKhfH_cJUf-yMu3tZAG9YYPHGxtDrbigb45SKvZEVgH1zHlI-pr24dlzwMmHTlN6oRJhWHdh-R7g2_b9_UcIYsHrdcYpWVuOyPOw2lNm43trEagt0XnlJINUPEH-G5k7uEKXWSavdwXXIXeavslVhWZopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تبلیغات داره به جاهای بدی میرسه دیگه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97350" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97349">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PApNHDINxuCLJMcUnJ-2IXMrs_kOvrCM-BwHEFIhYaj78iTQVgDuIdWFPCs5Cp5mnCCDCiqqA1fhnNglPQGSqUOj7LT9DcMjgSFYrcfXjfhZp2URwhx0nQwLayR6vy80JmijSJ0isWcXsufQ3hDKNivrqK7s4NNmk8T2buPkYzQjCIJ0reuOGjn9VbD9oBogAk95iMjkKbSZzcUvb8FtYDopw0u5rP6IvWolynRz5JfAwfDP6XhhUrl99Ts9u3H1K0BSMvj0EXsrdFKVcvn-_mZ6c6FEaC_bwwJxhHNA1kZdshPMXsDL8gMXy-7VgLvUc3qKWDyO8NzC4A--2i_54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس اتلتیکو مادرید :
آلوارز بازیکن ماست، حتی اگه پیشنهادم واسش بیاد قرار نیست بفروشیمش، من از اظهارات آلوارز تعجب کردم اما موضع ما واضح و روشنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97349" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97348">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97348" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97347">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97347" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97346">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=KmxOEREcPOu6NN4R_5dQXCLofepgub-JjgErHrfTdTRS_rBiBEWzipJfF3yGS-2zyqU7owQsPZjkdDX8XjolO-DYa7ssnNRAiokbmWT2ndLeS_0865UuvRr18NTrYcazO_JCI4nyr45VDB7I-uCXKoTiL-EV-xbbYqsu2b-NnSxxmckroYaTSe4jWykwTml_UPEy-OqPsH0IEJ8wITqxqNI2cG0wEu3P3YUoz9FsnB0Z6qrYtiDm8oJWBkypN8FSN-Cwg_7lYsB-E_k0yOwPvEXp0JyrBxddU_w15ABD7xc3IB_gmiv9ZoEmVJGgepXMDlCBT6oOZ516H6p1n8IORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91afe7d0a4.mp4?token=KmxOEREcPOu6NN4R_5dQXCLofepgub-JjgErHrfTdTRS_rBiBEWzipJfF3yGS-2zyqU7owQsPZjkdDX8XjolO-DYa7ssnNRAiokbmWT2ndLeS_0865UuvRr18NTrYcazO_JCI4nyr45VDB7I-uCXKoTiL-EV-xbbYqsu2b-NnSxxmckroYaTSe4jWykwTml_UPEy-OqPsH0IEJ8wITqxqNI2cG0wEu3P3YUoz9FsnB0Z6qrYtiDm8oJWBkypN8FSN-Cwg_7lYsB-E_k0yOwPvEXp0JyrBxddU_w15ABD7xc3IB_gmiv9ZoEmVJGgepXMDlCBT6oOZ516H6p1n8IORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
شادی مردم نروژ در استادیوم پایتخت این کشور پس از برتری مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97346" target="_blank">📅 15:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97345">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👶
🇧🇷
بچه‌رو چرا موقع فوتبال دیدن اذیت میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97345" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97344">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
‼️
در سال ۱۹۸۳، ریک چارلز و چهار شیرجه‌زن نخبه از برجی به ارتفاع ۱۷۲ فوت (حدود ۵۲ متر) در سی‌ورلد پریدند و رکورد جهانی شیرجه از ارتفاع را ثبت کردند؛ رکوردی که گفته می‌شود تاکنون شکسته نشده است. چارلز با سرعتی بیش از ۱۱۶ کیلومتر بر ساعت به سمت آب سقوط کرد و پیش از برخورد، یک پشتک سه‌گانه اجرا کرد. بدن او هنگام برخورد با آب نیرویی در حدود ۱۰ جی را تحمل کرد. در حالی که بسیاری از تلاش‌های بعدی برای ثبت رکوردهای مشابه با آسیب‌های شدید همراه بوده‌اند، چارلز به لطف ورودی کاملاً عمودی و بی‌نقص به آب، بدون آسیب جدی از آب بیرون آمد. بیش از ۴۰ سال بعد، هنوز هیچ‌کس به این رکورد نزدیک نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97344" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97343">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌رحمتی: بیشترین ضربه رو از کی‌روش من دیدم ولی واقعیت اینه فوتبال ایران باهاش خیلی پیشرفت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97343" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97342">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgW0yS-qBwLxV2oR83CJiBZOIV-yxTWLm7uqfzdjw723AhnSxOkJo8GlwdImfwm6ydPWYklWuiAmx69sY9mTdUiZP1lbZKJ1PdOIKuGKKDfGmi8uy8Bhb8QNxCmERg4hrPVlwJpHO4ArshAJ5n-G3bwoz5fL-bMuNaOHeWKsZlLrOLX6v74WQcIsE7pZHC4slIdFNxh9Ye4OORUHVXKAek5M-4WMSV5bs_IraqwOWMYdC84mwAFmLfmg6Ptp8WN3oMRKlNC7qcifUUJwIP-Bcw_KV2ov13yWSxhsgv8siHEQ9JLiIAkb-6FcMRmnH3oWykYMWDzL3u2gG4DtEc9-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هوادار نروژ در بازی دیشب مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97342" target="_blank">📅 14:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97341">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ادعای مهم و قابل توجه سید مهدی رحمتی درباره وضعیت تیم‌ملی و تصمیمات فدراسیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97341" target="_blank">📅 14:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97340">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiCqJI3zRSFHnpZioiTe4sI1FMB-2-7H_9cbxWqBHToo14ZzdHp2IiZV9tlLd60tNXox3X2U-LCI_NDn9kFcvPE_nZ2u53FWkfWDzQTpymC9Ak8eAEzr1w6C0Fg_pwPUuTv_5RCmI97v1F86MYh90AK5yqBUxoS95gj4Rbb-QdRpTft_yXNGY44O3l1NxvpABU9BL8fkOTVeyaLpCY_tdKWaeVhmZB8Bk3dpuIOO6K89AHdSzSgfeIQfd0ZJv8ohByPeM00df0Eix9lJW-oGD0ozApMfcDMuDUWEzHd2FNsiHepg1pA_6Ko-i9PpR3X1ToaBXzTmGR4XSrrmQ5Wn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🤡
کوکوریا بازیکن رئال‌مادرید:
🗣️
امباپه یا یامال؟ تا اطلاع‌ثانوی یامال اما بعد جام‌جهانی نظرم امباپه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97340" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97339">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLLioSWl-j03ajAZjpCpNZRL4Zj_T9gT5t2VXF01cXgYZM02934vI5-xT6NM4SX8EwmNMq6wmp9jve3Fyuv3ulPVCS6iG04zLTATzsOmtFRzP3Xf-W-WELgdNBjZjL6H3NkrLxuHyh8TlAaZBtr0Blf9rCMB_kO-xO9nIW90sgpLyvQUXbh4GuKYpmJxuUGl_1iyJ-g7eYGaAQfj_JYYjYLiT1pwJSKT_jq-6CWhuMqydX92jPfj3Ol8YylxJ74NQ478ScFTbjwZeRna6STLpsJ4A9y9aUBqOa6Kr902tr1oIiJqoylDdSGYL9-yITBGI7QTTHojKOcBSn_FWmkQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اخراج‌ یا استعفاهای انجام شده پس از حذف برخی تیم‌ها از جام جهانی تاکنون :
❌
🇹🇳
اخراج سرمربی تیم ملی تونس
❌
🇰🇷
استعفای سرمربی کره جنوبی
❌
🏴󠁧󠁢󠁳󠁣󠁴󠁿
استعفای سرمربی اسکاتلند
❌
🇨🇿
استعفای سرمربی چک
❌
🇳🇱
استعفای سرمربی هلند
❌
🇺🇾
استعفای سرمربی اروگوئه
❌
🇸🇦
استعفای رئیس فدراسیون عربستان
‼️
✔️
🇮🇷
در ایران اما امیر قلعه‌نویی و مهدی‌تاج با اقتدار به مسیر ریدنشان ادامه می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97339" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97338">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhdKLwLmAosBShYCL7SLK6qRreyo4YSMwu5tmFRw-Y6gAyauvHYUg8fro5CTbdk26wn_N-4s2KickbOvhpM3lWbUDuAQRmpUOzshlRUNa2ZyHlXRrvlHVkv9K2kOs23SsvNZ_dqeATqy_xyA5xg_ONKmsyzphIKZ47s1alkHalBqv5pJgaNIvaoTKT098QgUOFUpmQCRIVG-ux_qiQAn6e-12dueKg754XfVbb7XxlFqo8eN6nix5FfUi6dUG7r2R6XrSqlgwFLQmAONWFTf8QmkxaK23t9eNHXSK_hjAP_aLIABZ71XndZxn-Eqs5MjubvXWS11WJMcE7-IY1jUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
🇪🇸
#فوووووری
از الچرینگیتو: امباپه در اردوی فرانسه شدیدا با اولیسه درحال صحبت هست تا فشار بر بایرن‌مونیخ رو بیشتر کنه و به رئال بیاد. کاپیتان دیکتاتور فرانسه به اولیسه گفته حداقل میتونیم یک‌دهه تو رئال‌مادرید جام های اروپایی و داخلی زیادی کسب کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97338" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چرا فوتبال بدترین کسب‌وکار دنیاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97337" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇲🇦
مجری خانم ویژه‌برنامه جام‌جهانی بازم تو معرفی بازیکنای مراکشی سوتی ریز داد
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97336" target="_blank">📅 13:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97335">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdWNPxa8loRTm-_FW-XOB83MJByGe5Nmut4qbdMxtWMB25oRFDwk14IjwVpNJDL3RxiZtgrEGhfZo3zGCDcbgIf87UuKg4vWLstjvR9WPh1EXlvjoEdKzOChc1cKku516gG6DobznE9SZd3BvubLEhlhMVfuSVHejS3lAzYMCVvgJgFKZNHeYzW5FlwGqMbXFwx4ImJdVh0sVhBCW1ucQznvGpqmkLqSZT2AflNDgJnKCA73ZfaJwjOIoh2curA9s1XRS_cpJMlLD1Oqlb8LT7s5DE8ZZMsNog6vQx6avg7b4vsrtp4Jb0i99fsS4xiOJ1sAb4ZhmEjsS17lJOf-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛
در چنین روزی از سال ۲۰۱۶: منچستر یونایتد اعلام کرد که با زلاتان ابراهیموویچ به صورت انتقال آزاد قرارداد بسته است.
📊
ارقام و دستاوردها با منچستر یونایتد:
◉ [53] بازی.
◉ [29] گل.
⚽️
◉ [10] پاس گل.
🪄
🏆
لیگ اروپا [1x].
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام خیریه انگلیس [1x].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97335" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIP3CzyhT2QBBR9xNHkfZzcmZreHMe5w7DFHzTaAm3FPgWq7V7Vhn1nOYVftp3hvC9gBVTfBt2cv7pQ3_KU1qlJby9xt9YwgU52jd0CLBX-lHNHvIX5OMnFe3K9mWsQ0o2xRsgD8CCrLfbyKWXtOTgh9HydcyDJn3wP18qU6GsvbBV958JyrNWmjj7yeYzZMbPndti0UN6e_CBEwwn52vVOwM8D9NJ-7JAn7tGk9e9pWPxmJWBr3TFR8gVvOf2xg3mdcTGleH66J1csAinvs0BL3RPkCpS12ccPanr2F5tW6qxARzHe9vEkcvaGI_x7Y55cDdeMw4KloYVm1fqLZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ جرمی ژاکه مدافع رن با قراردادی به ارزش 72 میلیون یورو به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97334" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TZSatZ_wxRvxHIHwIWeI-AjUYMQqMS9sNUFsHoI27zrIeSiUfvIGORpqVgWt1zIm6q9xVG6W928rygBGqmyfr9-cR6XPZ8iYhfDuTkO3rFIJI60xFwtcqAVJIAFY1XBK86IfTdcVErvWMZDHChoCHGrLt3gjvIBxxKXJLc5fQg96_1m7dxyaNUC65lcrRVGavE1X3Qz6U_rh-oHGyeOXNs7hGuDlvhCzlgVYK6ppORAmGEh7tGK1hBNzOxEHe6Ca12uvohy9Db7_-buMuSFgYI4cW52iY-Q74BYKAdOWzBT4lJbWefiQnPgP-Omnsq1_p92nS9ZF9DFGOu-piNhjXOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TZSatZ_wxRvxHIHwIWeI-AjUYMQqMS9sNUFsHoI27zrIeSiUfvIGORpqVgWt1zIm6q9xVG6W928rygBGqmyfr9-cR6XPZ8iYhfDuTkO3rFIJI60xFwtcqAVJIAFY1XBK86IfTdcVErvWMZDHChoCHGrLt3gjvIBxxKXJLc5fQg96_1m7dxyaNUC65lcrRVGavE1X3Qz6U_rh-oHGyeOXNs7hGuDlvhCzlgVYK6ppORAmGEh7tGK1hBNzOxEHe6Ca12uvohy9Db7_-buMuSFgYI4cW52iY-Q74BYKAdOWzBT4lJbWefiQnPgP-Omnsq1_p92nS9ZF9DFGOu-piNhjXOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
عادل فردوسی‌پور: از عملکرد تیم‌ملی و قلعه‌نویی اسطوره نسازید. خیلی معمولی بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97333" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97332">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=Ffl3453htvF8UEeuBXnXOTMVx-_IVi6yLzyLdxEeBh2kat0codBS6Clq9OkRAcpymtPVzu76ZSim-iyuH8bXEr610d4t9n0hyNnH-ilWg5j2pVYJA3DqSH4BQ3PcudsW5x8d6KcovRzHuEF8gzZJj7SDGnUMoX5IHQLp8dXdNDordAz1rNz5oHDAeXc6j0e8zeuRPqOobjgHkYlHUnN3baQnfv4uP0Dqsgf9_luWYP90EEeDEVBgOmMoFrlcnekYAWmwBV0gl6i1bPMa3MB-dm-vt60umBA7O-djaYoRlWyRUmLlDnXzVuGTfp-GxadB__cJhV-xGCaBP2nTLKumkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=Ffl3453htvF8UEeuBXnXOTMVx-_IVi6yLzyLdxEeBh2kat0codBS6Clq9OkRAcpymtPVzu76ZSim-iyuH8bXEr610d4t9n0hyNnH-ilWg5j2pVYJA3DqSH4BQ3PcudsW5x8d6KcovRzHuEF8gzZJj7SDGnUMoX5IHQLp8dXdNDordAz1rNz5oHDAeXc6j0e8zeuRPqOobjgHkYlHUnN3baQnfv4uP0Dqsgf9_luWYP90EEeDEVBgOmMoFrlcnekYAWmwBV0gl6i1bPMa3MB-dm-vt60umBA7O-djaYoRlWyRUmLlDnXzVuGTfp-GxadB__cJhV-xGCaBP2nTLKumkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
چرت‌زدن پاره‌کننده هوادار مراکشی تو دقایق حساس بازی با هلند که سوژه رسانه‌ها شده
😂
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97332" target="_blank">📅 12:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
تفاوت سطح‌فکر سرمربی ژاپن و قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97331" target="_blank">📅 12:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCo68cet0EktP0WCYE_hqC1Vw5eXGnFSegrqJGhQ30Mbka5RJYpcM4Itam5sklFRytIggr_Fw6gCaigzyhPb0KZCFVGFF2NTNW5IIg2yIuWWG5QsDdD3Alr2cXMMANBsW8HQGHx_e23TVoX8aEnZw5YZuNksQTbRlL9UAsN8Bnx83IxwuDh4wECKaceDURE6PRZf4wAdQSP5npdjWUNwb-9wiLPRkqjmI70VXpu0PnB9jwRxG3SKWqPYU8xQz_fPDX9TytnlLIql68CW7K0snwEERBach_xM7m9lwJzqqyFWpFSrYLYljooEw5q43gAH2EmP3CvAaMNMJF_y9acjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🇩🇪
تصویری که آلمانی‌ها از جام‌جهانی میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97330" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD6SQ3q71i0ThZViEW1S_JvIQzr9hYX04KHpSHoMDMbXF-dKKDaCzXAwvHzWXSI-ratwsIV6GGTKKezH1537TuJaEqoNO_H2CabfUq3Up4YSKnPG_uMt9QMW2GWDgVRvxsRQ6v5M4n8dLkNNrRj76hFoILB-AYLvlQTT--OSKE_8kUixD8SSqZzndhx2Jrpis_ogs_Y6WowiynTvq3aXqqhRkfrac-RTLJegL0HfpBr8fvJ-RAqnx1UYO6qEhuWIfU5FCz43Crrxt9A5weXRAeOW0QDZQY9Q3efRs-z36n1_mePR9CGMy0nXSMma0M6u3rOrpg3WmfAPfteSkm3geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قرارداد کریستنسن با بارسلونا تا سال 2028 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97329" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇦
وضعیت مراکشی‌ها بعد بازی با هلند؛ خیابونای کازابلانکا رو ساعت ۵ صبح تسخیر کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97328" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_4VJEmkyhB9E7WZH7GE5NAj7JaOjXtujq5ywBOiGgXFUdcMwVBtUOXXtcLa_RqP0GHD4WBUPzVy8rg_G9NTZ011B887J3lznX38EfUAhMu6oN_tG-5wA8A2tbPQeOJ9MyK8Ao2v8LOSO11EyjLlm-IvcZSAbDVVcsvxJkkSdxHmcrOoSE4Qb9gW28XwpuZdopLEydEE3zH9y3ah_flr35iduYpwRiTKs388Alco3B1OBGqai_q87dr0FTj1mLBVao-fkEI-Xj1PsgWRRuhuZXqaol4TWxyMBCWjcyqWMX8IeXJikJQ1CHgHEo9kelMUTebBLAkmNiXApZLbl47wMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی اکوادور پس از حذف از جام جهانی توسط مکزیک از سمت خود استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97327" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار مراکشی وسط جمعیت هلندی نشسته بود و سر صحنه‌گل اینجوری کون هلندیا رو جر داد
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97326" target="_blank">📅 11:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97325">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
خانواده پاراگوئه‌ای‌ حین‌تماشای بازی آلمان و شادی فوق‌العاده بابت صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97325" target="_blank">📅 10:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97324">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
هواداران مشتی پاراگوئه بعد شکست آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97324" target="_blank">📅 10:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97323">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
این‌قاب برای آرژانتین حکم دین داره که حاضرن برای پرستش هرکاری بکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97323" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97322">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37351875f0.mp4?token=s3YZzvYOdRVrQ27B90eWDRpRtnlF8E4LcoY7Ukz_3tiYw-KN0MUSw0YYg5qGOZ7ujZs9OhYJf_o-MZ-3NHuwC7a_Yl5mmtPgxiXV1G18dh_3USG7CtPHBGquhBA98GF54O657ew81WEWnLrWsYyUvR0fZxAIJrQAzJJdRwNIedaMSSWgAVBxdZP52X4TJt6PYhdx9X3yd5xE0JK_1_D3Ccilp2ZNtHvWeY5NOdu_lknziPJrTwx15tOTZMu1CT6Pfkqnet-q3f7F_ncD3-cAgtwYzzLCnqynM-kntoSraaWnoLsHgVzrmyUwFG42idFA477N346gQce_OPM-xUcEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37351875f0.mp4?token=s3YZzvYOdRVrQ27B90eWDRpRtnlF8E4LcoY7Ukz_3tiYw-KN0MUSw0YYg5qGOZ7ujZs9OhYJf_o-MZ-3NHuwC7a_Yl5mmtPgxiXV1G18dh_3USG7CtPHBGquhBA98GF54O657ew81WEWnLrWsYyUvR0fZxAIJrQAzJJdRwNIedaMSSWgAVBxdZP52X4TJt6PYhdx9X3yd5xE0JK_1_D3Ccilp2ZNtHvWeY5NOdu_lknziPJrTwx15tOTZMu1CT6Pfkqnet-q3f7F_ncD3-cAgtwYzzLCnqynM-kntoSraaWnoLsHgVzrmyUwFG42idFA477N346gQce_OPM-xUcEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
آزمایش فیفا برای شناخت تکنیک های ناشناخته ژنرال و مقایسه با بهترین مربی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97322" target="_blank">📅 09:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0Pw9MBxl5CL1NzFIcN_SvBV2edwJzgFSIELLohSl-CrPEpbE6AFw_F7sYlf-BF3mxrTuJnLdUuKCyOObo8t3M_nQITNWbR6Q8UlYWvLIdBkEMZQxYCjyrUD-Ejx426_aj80GLK1T1hYBSgL9BIwxVTe9lfX3THLtlmWPWjrYFqkwO5jhqSynzvON5S6YEcZaNfDaG6YgncAMdyw7B6TKOq5jbT7UUZMmpi7h-FgtnAF7DsTYs3BxtfLyvUG8DJdS_wZzJMghN6xWhsZeMCWRs4GicJzSswXeD-vyheGITTID6Urzh2QiJTxQyzCKD_wHTgSg_9GrrwVYR03zqfBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇳🇱
آمار ۱۶ بازی اخیر هلند در جام‌جهانی که شکست‌ناپذیر در وقت‌های عادی بودند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97321" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN0KZgnnnZNnXZda4X8chlYDVHWSrTHkX7G-gtPPXKGq1FWfgrL3nVV48E6Hj_jVQRWuIHyWJ5epPnNVnU9HrU38YbyDFGu3NmVz-OX5z_KERSYVID1CTiRsCTd8RqyKQecz8dg0xfciigQ0C7sRnacce15qTVmdWVP4oRX4cxCSiugPvZj4Lpy7sT97X3TDKuoUCGBu8mX8aCc4HbDsKS2B8LyR5-8qGMczDuIe3otq7NDb_-rRbTs0BQdqrEUCkc31L07L5MbNpLKIC2svIPkr4t3DN-cBx2hXoCysEUz5OHtdWtBGAIKDuTa33EttATVDlk7ZSUz2BdZXBjRvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxzpB6rp9soKAgxLBywPl-c-r08IAnpzZ7MD83A5x19HCSCEXAOk8q4Oi7ukYYfSObl-mQltnkfUHFp5A380mK9Napnd-ra7wfF5fZV_4vqNTQXidfnoPae0fVn9HDoKtVegE0trYCpb-P64QC2L4CfPNHYaFrb0uFYPJyzSuv2vAuc97XaD7YiU4FnFbplhvjPtdM_8FBtUeNt7fmDKV6nUGZCoLcgjTkz3isF8QfftcDXuFTFDsyEwwia0pko43ozGsbUqRG1RqLOUOh5P7qHO8_ytqRPdykr0uNVa00yiI9aXAIAuAETbiGwOn22IE1XI8z50aJIhafKenkR-KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❗️
🇲🇦
وقتی اسماعیل سایباری به دنیا آمد، پزشکان به خانواده‌اش گفتند که به دلیل مشکلی مادرزادی در پاها، در راه رفتن مشکل خواهد داشت.
👍
اما مادرش هرگز دست از مبارزه برای داشتن یک زندگی عادی برنداشت.
⚽️
سال‌ها بعد، سایباری نه تنها راه رفت، بلکه به جام جهانی رسید و پریشب پنالتی تعیین‌کننده را گل زد تا مراکش هلند را حذف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97319" target="_blank">📅 08:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNKCR0v-GkPOlPiFqvm2sHxIOLv-eOmpPia74T3SuGWEi-r9IFbdPu2EARSZ37gJZ7CkqiL3K_EzHkVPnom5q4ivImbv_2W6ak-1Egm5sm3c6BDE4sD7OaMjV4Vda-S8TfchdsrdFmTat32xlVAij7IjugNXABrRzax1DOB--ipjYIlLIY_s8XtLZObUTzQBNf5Cb_0FFKK6k5pgxB_h_vYlllB_7t8nSTxHRp0uh48plCcpoarIzrrmfbt9u7jqWWyF4_ruCJQxisNUDJ66wCaTXT5a9zeq0L6Z0hsw0f44yommZ9rRH3ZkJGAc1QHB5bl2zEEjOkeKdFz3bbRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
آپدیت نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97318" target="_blank">📅 07:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgUjBcF3QRcs2E6vQo-9f_y69uAwX4Ewx6o7BPIrGd_hhPXNyDv7xxy_4BusEyG1UhNm2vhWciTg4GvTw7X1s4R_x1eCP-4OMThouLFPufZqzg-uLa6LRUtRlezBtoNBQCnbZOxxPEHDBYDNymwDAy4UJF--h2jNPQt5jBWq00chM5Tv-lW-NZiQd4uI8_whMlJaldgzl7YEUQtXWgXr4mQXRYFL-y5LjtHafR8CoRmMD2N9xQpEMgykq2y5TsZyI0RhxCW2zaa1G3ErBKa4OMVmn1E_JJs26CKxJbCRumoF6CBUlVFrmCKHS7oqUdiUmIhDP8vgO4DOTlaqo-A3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:  ۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97317" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZjrUE1bp4-SQfgkckgjMR8GTCekLMUSfUubEQYCnPccTZoS1cHCUZIYWHEuPn2VvFQogzok83UwTctLZU4YSK_Z3qlN2ZEGL9E8kPqZl4pKyE8umnTE1POkTy4lLq9s4gEDH-ovZijmR1FXqc9MO3qzycBelBSPz3jojP0MqSS8IBZVKcie28nJLwBAAq7nFzFm6-BUJFwi8Y9ZF9Z7S1F9wWaBbkJe_elD2k-Yu-sTJLPsha384bKaNz9nc1o5M1Khaxtt7v8RyL0S5EcW5p0Do7eqMBvixUl8pmmmnqnx1xVscr9XIiFiZA4A99YOS2ulz_K7x1Fu4SSBsLpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:
۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97316" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB3jPCKixOL3FgcEmvc3ffs1rdvrJEQ9A_Tn3qeP_atH4ni5iiMe4fcHs4KqdxkZ5ynUNaprWVGe6Y7zFRFDNlAu2bVN81H4Rd5O9o-2xIH3xJ003eJDD-i9UpugHuuqGu_i6729IVdrkinpJCXqKM6E4DaFIAYED0doFVopNOB6RlL9rTYIYxvblDcQkmk_0ztaYipsE6rYg9qc7v4LJzM2adpvw1GvPGEP3WsdXHenB-nt4dEfeScXZTDV60tPyWzU0FtFOvRpzLrDSBQYH-rWSgN8Lu-MCNCbOPNdP-p1KE7Ymb10kQ-3NmR-aN6Bmj_Xd40MSwbtCuceOL1nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
قانونی وینی(پرستیانی) بازهم قربانی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97315" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97314" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkusJuiLzPTcLvQm_bv8sZxvGgD3jbsMNgGugLpEm9tCMkj9lGtYvtMot8ZLcFquGan1ClauHq4kpsb9hG5OuCCegiYGQrhbOxlgHdT5qmeJDkB3p99BtWP2Wb1s49DcAA-LOlqLW8415Lm_HQPP2I_w1wrYZlCHT2Tcf1G6VFo9cLgFXNvxa3nzu7sWYt3XX-1HJhUCOtsWkS-SNHCmMv9HMV_5Oc4aTkZQtbo6JNzhRsiNDBIlW1F2GuL_CMkRqBpdVNLFjk5XL-2vbyrFY9W9b25XYM-dV0dNVsqXKiKEgyrCAoGDzOZL8ulCbemkia0DUO_wcPXxZkYyfsIz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97313" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دقیقه 95</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97312" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هینکاپیه اخراج شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97311" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=VhjRNbpg_uH5OcZ3OB1FYUQug_3jBQC1px4ixBu_SsGg_gBsDPlOTDwHOf9vsxkE5fmyMcFM-L9v1TyEm7Yjzo-_Yyw-ANyzS4KGE3zSbswARNG1Fdax-d4gIkT5RMLViTF-qLE_UzZW-If9-ynhG192ks6B-2qpIPhG74NdeRPBiOqBxBwA7FV9A3YdDz9m7UjY8iMIfEUNpJAsExJFNq8Enu4V0tJQC2K0e1utOKjUoYyUgQ6W6Ndr2X01JMTHSzU0UvsCVM1GDbLLGW_66PPa7yNy2HGNuc7wOvTHlFVmUDiTzuP6aXg2r5UOyLrmjH_omEIK_GrZX1WuoqdEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=VhjRNbpg_uH5OcZ3OB1FYUQug_3jBQC1px4ixBu_SsGg_gBsDPlOTDwHOf9vsxkE5fmyMcFM-L9v1TyEm7Yjzo-_Yyw-ANyzS4KGE3zSbswARNG1Fdax-d4gIkT5RMLViTF-qLE_UzZW-If9-ynhG192ks6B-2qpIPhG74NdeRPBiOqBxBwA7FV9A3YdDz9m7UjY8iMIfEUNpJAsExJFNq8Enu4V0tJQC2K0e1utOKjUoYyUgQ6W6Ndr2X01JMTHSzU0UvsCVM1GDbLLGW_66PPa7yNy2HGNuc7wOvTHlFVmUDiTzuP6aXg2r5UOyLrmjH_omEIK_GrZX1WuoqdEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
مانوئل نویر در ۴۰ سالگی، پس از حذف آلمان از جام جهانی ۲۰۲۶، برای همیشه با پیراهن تیم ملی خداحافظی کرد. او که پیش‌تر بعد از یورو ۲۰۲۴ بازنشسته شده بود، برای آخرین بار به درخواست کادر فنی بازگشت و آخرین فصل از یکی از پرافتخارترین دوران‌های تاریخ دروازه‌بانی را رقم زد.
◀️
۱۲۸ بازی ملی، قهرمانی جهان در سال ۲۰۱۴ و سال‌ها الهام‌بخش میلیون‌ها هوادار؛ بعضی اسطوره‌ها از فوتبال می‌روند، اما هرگز از قلب هواداران پاک نمی‌شوند...
Farewell Legend
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97310" target="_blank">📅 06:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شروع نیمه دوم بازی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97309" target="_blank">📅 06:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏆
پایان نیمه اول | مکزیک 2-0 اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97308" target="_blank">📅 06:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مکزیک هم هوادارای خوبی داره هم تیمش زیبا فوتبال بازی میکنه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97307" target="_blank">📅 06:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آلمان چقدر لوزر بود که به این اکوادور باخت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97306" target="_blank">📅 06:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=p1oSv1SqDFJL2tyTPA7DVdjyyO7aeHZ4E4TalA1Hp5Wupj_MadKuItyCGtOrrBdT5662Xw3oz2joUM-nxWB7LBD_pwpq46SqPbRKEDBXAEwUUiSodnbRmepBb1mkg4ktPk0IiPOWhy6aRUJY4gzBBKygLJ8Mnh5dQHED0Twtx2Vwu_tlnqklKs8wKLGgse99wdX9_65FSut_6e3C8KseUj7SOCb5-H6LyZcEI0T8uMTxOOK_eJjTg49NzJjouqoglwi_5Gd-fdTD5Ejky3_J9cNnFS53tkVoLTUwW78jF2IRVqR-apsOL6AFfp53gvvt-s8XBSui2hEF-HigFG4C0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=p1oSv1SqDFJL2tyTPA7DVdjyyO7aeHZ4E4TalA1Hp5Wupj_MadKuItyCGtOrrBdT5662Xw3oz2joUM-nxWB7LBD_pwpq46SqPbRKEDBXAEwUUiSodnbRmepBb1mkg4ktPk0IiPOWhy6aRUJY4gzBBKygLJ8Mnh5dQHED0Twtx2Vwu_tlnqklKs8wKLGgse99wdX9_65FSut_6e3C8KseUj7SOCb5-H6LyZcEI0T8uMTxOOK_eJjTg49NzJjouqoglwi_5Gd-fdTD5Ejky3_J9cNnFS53tkVoLTUwW78jF2IRVqR-apsOL6AFfp53gvvt-s8XBSui2hEF-HigFG4C0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مکزیک توسط رائول خیمنز
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97305" target="_blank">📅 06:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رائول خیمنز
🔥</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97304" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مکزیک دومیییی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97303" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97301">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMHALJ0-JWtsTc__D-sqsbgwR2c5xZ5tbh7a1m2KFDptBIV_xKBfEfzggn1vA32BJDMgZGuuOM4ayW-7qXBlUzrVHmBcqbwR-g8bd-xlWyQmylBT7CHWVNKvFBTSWECEvEc5EsJz0V5aOTE8ZPyfFNA8K5bJbTJ82jguJq7kAfd_EtZhjwA1tIBo_tlfl6UZUmsKRADjdRxlRQesDuyxcrY2L1hsSTS6ewiv9fPkj8WDzhVPQ4WEVP2vwqBYXxTJ2RMfp6wmzgaQsaDE8XHj_X1_nbJeslpPb8C-QDInIRjbzX4gGEecgKC2T99fg2iPRJ9ge1tMKDVbv7jnSayOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq3mSmhshCPWYeQQICqZ203RmklwNd90kKgnhpDSocMYN4EUo_nP62aPH0vlT1ZccY6lqNmoNTKtBRwuScugMlGAmI0amS8AerY6vRtdZ23RiGNW4DrlDuqRLIfT9fKo9el_UPe5tU4aEUtJmrZnNfHv2xyIi4REeog1W2j_uzYq-8o9gA1Y8SqgFxqfqfhrQ_xj87MH50GxZfaJF4ARHhrz5pYJDiDEpScW0aQKJzYevyGe9EuEo0AnroG876Ud-DHxzRwWCVYKSh8awzKRBLOCVmkbEweD3Klb7BIdF0p8_HxP0JuhSfjBaOK3sxHFCfySaBjAbnWZHRAglO0f6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97301" target="_blank">📅 06:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97300">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=L05xzDPW8IrWMwq58uQm10B1xwFAFOyyNmzmrkHaaZy3-LsOCmmedCDnIm0iS6gXLnrC3cl3y597Uir3Fm9h8pbNl7Cps2fRIVUObznI38ay41FG3B18ook3WV9p6TIdyLn3ZWMVA_4JBdX-Bqpzv0qXpU2-BezdaVeE0zo9DZAYQmHp8vhLCzFo44TgQCCCgS_pjOAcTLlb861zJUUiIze0Eu5BEftR0JhorfG8XGAU3lUkA8XG_07l0yf_Ev8QlK3rghMFrJFBT-LbfTepPYUF4eav-jzWsVsDoH7rzhYQmvoqfHKPbv2KS9KYBNuBX_SWXXR2h4E3TV0mHyQRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=L05xzDPW8IrWMwq58uQm10B1xwFAFOyyNmzmrkHaaZy3-LsOCmmedCDnIm0iS6gXLnrC3cl3y597Uir3Fm9h8pbNl7Cps2fRIVUObznI38ay41FG3B18ook3WV9p6TIdyLn3ZWMVA_4JBdX-Bqpzv0qXpU2-BezdaVeE0zo9DZAYQmHp8vhLCzFo44TgQCCCgS_pjOAcTLlb861zJUUiIze0Eu5BEftR0JhorfG8XGAU3lUkA8XG_07l0yf_Ev8QlK3rghMFrJFBT-LbfTepPYUF4eav-jzWsVsDoH7rzhYQmvoqfHKPbv2KS9KYBNuBX_SWXXR2h4E3TV0mHyQRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97300" target="_blank">📅 05:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97299">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX5wDwM8u_TbvlmsVJbm_ykYK4tzzntqx7zGj7Cg-Th3JZ_etDOL85l00a23uA0zVCkjoEFX0FNIQuzSd7NXC0kskXdSmMN1rxEdkNBwaBb8vpgJ-deD6Br1Mxve8uR8XaENct3DPKjdghL67DbLYb3ZsKpzz3-gxQpdBsWvsA_sziTgcmCQiO5LcJkPF9ydTitdyWbWbTKetcaXd2tXtovlGRk2SiOQB2MODGtacM4oo0jwZMF7pe08ZPgJE-_rxZIIDsJ7YQKWtZ_KPowQFMLY3c7c1cACzkIB673fXkzz-ZABOwfWNdfiGuR-ozY_JP46_aNnYGXpk7Wm_mzeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خب خب یه شخص کاملا جدید اومده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97299" target="_blank">📅 05:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بریم برا شروع بازی اکوادور - مکزیک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97298" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv1ioFm2z32CYV5f6xnHZ03cqBzs8AILTa9zynOJ0IougAp1oI2yy7m0VcDf66-AfzwjEXMbtHoecIoaryOWLjERKOn-kjqoevmAJAjxDwmxnCIGj-EcKQ5IZU3UIze2UDfej5VZYEp1Z5fQHMsytRl2Oj20uo4bdTQsmDg0R20fB-vjpAPko_GyW0b4R2cziKNMepXr95REDWuxmzzcryUyuJzFBamHFZ5G08L2gxSgNEat_8tvk1xDF43LxsvlqXiDfc_qAwSYyB025tPXUwjrs-b12R5RPbPPELDI3zCCj9sh6Ww3-Dp01GhxUI1wgmWBRagHIxJKRlEwewCknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
امروز قرارداد محمد صلاح با لیورپول به پایان رسید و او رسماً بازیکن آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97297" target="_blank">📅 05:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01873d097.mp4?token=VHP6cizFq2B4VryO4NSPdUDbocMLSgLSAStYTZ11VQlB0ktELxA_avYYPr2rWIM7lFOVHplJaA65mNoQLu0lT-5ZnTo7ZccJDw9-0KtM4q-ezb-rWenGeVtntQBx2erC6Rlxsu8qfeg8OwcybOvzBtFJyxk83jkfZ0Bi3yMvqp7bIxwOAxMsNc5-o5YnUmAwQgSvM_LkkWQMfS1XYRFOB_jfqd7xPB_tVS71qlLgZCpOMsFIi0SLEOZ9d1wIbQwO_yU6gPtHqGjq3kiSO3h36PNiyRIgeEtuUozYV01z4-4_0FLphLmrJzw8MJ1NvTAFDFq_h3vZH-174bQ3s8zwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01873d097.mp4?token=VHP6cizFq2B4VryO4NSPdUDbocMLSgLSAStYTZ11VQlB0ktELxA_avYYPr2rWIM7lFOVHplJaA65mNoQLu0lT-5ZnTo7ZccJDw9-0KtM4q-ezb-rWenGeVtntQBx2erC6Rlxsu8qfeg8OwcybOvzBtFJyxk83jkfZ0Bi3yMvqp7bIxwOAxMsNc5-o5YnUmAwQgSvM_LkkWQMfS1XYRFOB_jfqd7xPB_tVS71qlLgZCpOMsFIi0SLEOZ9d1wIbQwO_yU6gPtHqGjq3kiSO3h36PNiyRIgeEtuUozYV01z4-4_0FLphLmrJzw8MJ1NvTAFDFq_h3vZH-174bQ3s8zwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97296" target="_blank">📅 05:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97295">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA8tOyQoE21la2EzI-fE39KZLWSUhMt9deaB1ed4XgbwaEjObqwt6ErnhljFdYH0JwZ2AvTgHEmeCElKPGQ1yspem-OA_8Fiv-nsUyBgDMubLfs2G00kOuzW7-2k_suKh8y7NnpQwON1ILRPaDalL6rqvsJEwBCBWNW0Fp5MWmif5QvGHG78WxlrC_xDBjwhhVjdXY5g6_qNLmPQTMBggdex8YtFofY8Hf_3rK9QIC8AF0iaYZJpYjomnMA8752xL9_FcTIg67hc--o8RAwcXDBTrFnHpGu6RKanRWhKfth3s6WOxnpfndIT_r-untLr8jh9U3WdD6poo43YbbeCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه حاجی رعد و برقو
⚡️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97295" target="_blank">📅 04:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97294">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx4j9213fk8Xomev3ox0JNQy3kP0ektcT87qE87MUl_aEMIOiZEwUHGdPsv1doVgLBn2ixT7CVzMvmjP8sQS-qy1-CbGcR4y3yk99xZ6k2ifYqqXVjqJVjqt0f2-c3Xaljq5WAOSqJ1uIbtl6j3uYWdSQWEK4W1sy7WIY_ZFtpo3nvc5PC6isCmLx8P91wPtY9prYk9Qx0gGUDi7Jkv88OJiuOmcZz4KtvDHdvrfa2QKQbThyNPgLRi24EdmmX1JuzVvD2pMRT-Znu7Y9NLdw15nSGX86hqnFO9xKbIs08Jt6_NRh6G7p-is7DNHcW4QBpkT0XF0_phFNXoV3zH0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
| از زمان اولین حضور امباپه در جام جهانی، تعداد گل های امباپه در مراحل حذفی جام‌جهانی برابر یا بیشتر از مجموع گل‌های تیم‌های ملی انگلستان، پرتغال، اسپانیا، آلمان، هلند، بلژیک، اروگوئه، سوئیس و برزیل در جام‌جهانی است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97294" target="_blank">📅 04:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=EKSXT8v-3f91elU68ALgBnrP-ZvO8m19Uc9C0-cPH1-oBzhi6cLTAZLYqn2xdO-xyqajCXounHMm98UdB2MgModgXWxf_Lsrx7a74DWdWtOeXGtw5ptHunIVoM2pb20L56f207TrvJH5lgGW1OuNfZjpmo2OAyysm84x4HW9pNnfLk8wNi5owNu1P0LfxNuVXze_qkibIyYTSsOnyoEYZeRjqctx18Ay627ePymjVnMkCgvZxS2Eh5ph1XZs4sPvRhq4Kk1t8nZ_xU8moMNMVmrSRFF1Vng5tPiJ3lgqcmNx5ED9QAlmFvQCDRupTtpYuowktqTs7bP-auRaNukEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=EKSXT8v-3f91elU68ALgBnrP-ZvO8m19Uc9C0-cPH1-oBzhi6cLTAZLYqn2xdO-xyqajCXounHMm98UdB2MgModgXWxf_Lsrx7a74DWdWtOeXGtw5ptHunIVoM2pb20L56f207TrvJH5lgGW1OuNfZjpmo2OAyysm84x4HW9pNnfLk8wNi5owNu1P0LfxNuVXze_qkibIyYTSsOnyoEYZeRjqctx18Ay627ePymjVnMkCgvZxS2Eh5ph1XZs4sPvRhq4Kk1t8nZ_xU8moMNMVmrSRFF1Vng5tPiJ3lgqcmNx5ED9QAlmFvQCDRupTtpYuowktqTs7bP-auRaNukEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی دنبال دلیل درخشش امباپه تو بازی با سوئد میگشت؟
🙈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97293" target="_blank">📅 04:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwiJDhS_EukIjiDhedmNdtvAJt6WI80h_7bD0Ep4mmaCeRpVApHtip5oK7Rg34aOGBIf0AAlgHtfV4-w0ulbI18ioOBzy-XuxobwawLfVCQluZEel_h2GK5o6uRrcJ21cxXorM5z3tTZg5Uc8Ogk4U5J_55mlLE2Ucs_dNe0BSABMLqxQGh_ZOKH_w95sukw568pqyteod9FNp4psh14OTotoByO_yenacyHccT2z6iXsWq4liyLyksDXq_-DVqpDiYGDGNIN4wMrAgqRsUO6fVHl5uKAHE3k62Zz6sr4tLH-p_qPJdGhvXDR86hjpzo0GzrJLXDOdHZZ30Lh1dq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به دلیل شرایط جوی، بازی اکوادور و مکزیک نیم ساعت به تعویق افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97292" target="_blank">📅 04:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwGkRywWU3nRZpTFR20U97FamitQRuoBUoNHaqlotGnHX7NOFLFMwX-juPAKJcqwE_iCcMwUb9C67azMXmBh8PZUtSU0jbeWvm7xvcSmklmI2UY7u5sL9D4eY7kC71GMdgk6GSk1lQ-dXskBTtl7RAPDBPW5k_LGXmfx3Tgr0UyFerYaghRVgeZckPLo8SzRA9_Ua4Wn9UkNI8nk6rtgRx5fWMYThFopkBiCCleM0GX2S77qSMIMBwoI2fAUpQAMPhtXiQOccnMMtwntjJTMMh52YPZdjWXZcLMULe8_6atx5hs1QHeWIlRT0YOGWuRtuBoUHhr4HbG9nurzuAByig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egYKT5VvnuG1sI5QQsTj7YkboyjjKO4dUNXf9Zzm4SGLvdpRz9l2UCVT-5UmSlu242cEQHfHtk96CyA5ubhom9jbP2OAu0XmhTSYCMSskZivBELOzebNGnKVSlH7SRK8xQBq7HtNumg2Wda7H2HwHYSKbBVrhFf1_j_bBcWOYsNVeM6x2YR9baIp6kyW_JXlf5Ej_WW_df9-RDNs83_aYjfudvhndiAsB8ekvCF9dRkJtIsrh3ytO0A6yqsYy-4ty8NLDbh7OKlYdt8uEfVkOirxdCuI2v81NUMpZNf9QXwRXHSQlc6P8KvuIgIckBn7WsmIN7NfT7vUjSer_VYc2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇨
🇲🇽
ترکیب مکزیک و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97290" target="_blank">📅 03:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4L_WL-qpHUC78ZL6GJAhtP9_Q4BszZGBDpLzSAjCB3U_agcY5a_WNiOhB-WMF0hARgm67Vli-z8sX9zh-ijo5cQXjfNEv5MuVwi7_TDC5ij2kXF5jpN5jsbFvmG37vmSchK9CKgpBSy1mlvRAY0-Q60JiGYiOUaYBZ0I9n7bnxlWrrmH3WZXzaE0xm98bivv_SetrAYBWuHv7h48QCfxW8LFjAXBQ0DM82Uqk2vdhwC_kLQ8qjJxkcTorFhkJUk2EHXerDJ73eqXmFJ8i-sKFqlGu_hZDwIRnawSFqcXQptiFz3ZkbYlBsbYC4fKorJWR2X5SDU46E0b9hUnAx4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mi2Qsx7nttMHSLxl6xSCdqfQiim3IF3Gpj3ZSR97qtA9fktqlvTUulb8kw2UdtVMPzrixh6arKIElRoGJ2Wh0L_Z9SIgqfcJcCj6zAaVhHo7XdZG3JF9KneOaD1y9Tp3bUUA0XQ7qbBhmLB-VXW4xCcj2O9Xe6gos1F2cdT6R-Uy0mFrZosbbtbBhZD7ciTvGssWGdTLJY8Kj46ZsyjjzMnQonGIXawEBV7vU-Dns0mI1Tz-GETFSKtZXN5bh5F_-oWY5vQUNEHAB4s8sMCS_h4seeRkAQig9rHHmoasznkIPdO_wEB71YjaTk99W_KzI70GnU4tFgiaohNgon6yJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رایان شرکی که حسابی کلش از نیمکت نشینی کیری شده اینجوری دشان رو بعد بازی به تخمش گرفت و باهاش دست نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97288" target="_blank">📅 03:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhyHlqrzhBJsj0a44VfdvkHKHe14AgemVgfe3jbO283BSqEYmhyDzABbP__9YPvRqTLfbOp8AcQhvWEpMgAUpbrO2LRvaKoFQjQPm9O_9BniMg6v5HB3ZCz9X-Z9q4ZDpPUTp_9A07-QO5ybt21oJezYfV1yhT1Ey5Q4mVaH1WKtQYJvlL-7wqxFc3RPvLFawJBKjyrxlDmYsRFKRJxleaRGem2naz-6XTXRPWkw3-M2J_RK9CBXkVZ3ASm6k2fHCOTRJnGRi93C6IPFxkhonRy12jyTewshSHUxqcOeANw8dpRQ2nKt8nledgAC41AjHbVtgQfp_ZkAG73lx04ATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97287" target="_blank">📅 02:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv-B_MBdLGDBJ3XCpFh8IzFtsp-jvws7QvGGwmvX-zgW_8EdzIWLgqfE5jfkTiMR2Xzarq64UwxArPLF9LHCp48an8frl-aGxCgn-ChwZJGI3hCtZ9MZrBFxelFBflbaDoNskEXh-FXIkCImT0k8AWvmsBolkdkqJUaRXalJqmJDLZSbSl2nYbexU3NCxpcayud52cYr7fFy_vy3wPspaoGb4HCDhl2Tv_kXHGa66H2GkQ70nG21sjzg9stkcV6Rr004j1oRGqVzwNNJ5QMPiBEfdY-UHFRwdC9TKWyrpAul36bY7kq4Iyqp-b7nTPXsmX0dI63sTqhJy_hKStgIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه:
🔺
پاراگوئه؟ من در واقع دارم به رختکن و کولر فکر می‌کنم چون هوا گرم است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97286" target="_blank">📅 02:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj-y0gVju9F270qYkooBYt3nefGjGZzazaLXwbvXR9Ch9WmBwrSVXh7nM1zbviyre26B0oJ_EXEOETZXRd15PZIdqb6H6Um3hTX59EZ5cupJVuNcLQ6_bsRtnJ6SjnGpTO0tkkNZYu1H6UeYukhF-yCqKRmJ1l8YhGoR7OzDjQgQfyl4iWbcdk8sGUSapru22Q0cUjKL5pjjgcXTW4EdFFwwapCGCICntCXGf64dlnzmfTKhoUh2QadZuwr2i3vKUDvrCJAPzet98LiThvboXXxYeSfndbrtQ8FPZonQ4wtZDUXxjThfEdwvlN38EPlrd-pV0E31YkiPNMXWbgjU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امباپه با ادامه این روند موقع خداحافظی تموم رکوردهای فوتبال جهان رو در اختیار خواهد داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97285" target="_blank">📅 02:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOk4f6-xJyDATw2MWXFET8ou7Gu7l8rh1yenlalsFJdxd7IVSga0Cgs4iR4w0LZNIyRPu3H3mR9cKvv93vo2vq_N-bUlbIGa9Vv3QVlsUhw4K2tITw5DwekrTXyn0XfJrwCUR9wa4GLojLzZPV2He6CdZBQcrX5WupAF6MyCR8iHvdTTkYJZutVzBFpvtyyXfKu4yg1XvyCSJJgC0oKgkdRMrh2eNVXCfYM2RRRcAuK2LBh_Dsa8TUzeUyZdvn-50zbDPsrD9D0WuuAye1qgpS7mCj825sxcgtmn4MbCPJ-FL65mi0zxp481cvWVyKJNGYaeso96yVmimxzb--QRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های اسپانیایی با بیشترین گل در یک دوره جام جهانی :
🥇
بارسلونا در ۱۹۹۴: ۱۶ گل
🥈
رئال مادرید در ۲۰۲۶: ۱۳ گل
🥉
رئال مادرید در ۱۹۹۸: ۱۲ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97284" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97283">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97283" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LM8gcAQnLIk5KX9RWRshRKWuNv_J4MG-2RO_S_VG_0oIhrq1BLLdwK8F3twLJZR6lKTSSA-ynLn18nUu7K1bu47AG7juRVuf_jr4uOTZ1s0NkEYkOMkI4q5y12lRKVwDmYQgrmap0SxfQjFdtfkxZtvByfkhcbwTamovbLtEgPxyD23uVrS9m_Gpgx3poxbKg7JFHFBUHW4EBCyGpY7yBcog3TscTg27WaHkWCspW-Rm_yK2ZCFFULFTrHvkVYUfZgxNFHiugEZIBWmgEDXFfOKATpFsa-BfxZA-8lLkXuoSvgdHbwqcEuU_WuXGFUqVffcz3g70RCtQr2yETZ3S6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97282" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZAF1M8f1qRoCj9U8XIC1Hz6tXEJ43-9paJsaXgMq9AknOkfMWaGuoEUbq_tHbc5ynBPgm2iNEWVYZZCiD56KNOiRwL9fNGeSP1ZLuzxxWWPZioLNtJqGaR07jeLraaXo68R2i9WjGyFZ3jDELk7t598H-3apT0d6KrwMUy4jrhy24ayzSZknTfHi1j3Vdy4llSy-fmZXV7LVWOTfdYPa-3EiGdHW-etFLhtFtRS07Sf7dm-lINwCJmPL55-Cakhl0ATlbbfh3LXM2ttFaAre44akOhE3Yhk-yVa95ISB9VmrSM1YlY94HiXRrvfQpXSa0CRaIEaILhDN_K6YyUG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97281" target="_blank">📅 02:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi58ZKCcwntOY980JRb3bB-JhnQgP5vEPszrCfgx1bfhZKmX5QFQhsG_rg5aG-EHMoXiaW4lwppegCzQ-ManL5KkyQZzoXT1QKsdea1y5OSY14Pp3Ix_3f1hjaE9AnSflQmUi6T_1lVXcGZgwSkOaRugRRO3JFj9-bZ2oGLnEFjCyieXL_qwu_qdcYFssk525jLdQ1vNvUrkClBcGrwVYNUdmGjEHEN5a8e8W7mqTwewMq38mA4-eW3mATN-fwjtJ1ZRbSh__fIBPefOUHq2OK_IN1dckHIHOFbCeMEAafzb9emXM8FtWeD_x6WLvbfmrBqrOztcqDPGJMMmLOHIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازبان سوئد با وجود 3 گلی که خورد نمره 8.6 رو گرفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97280" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1fzlevpFp3B8s06PwIwVlOLP1HCa7ilB0aRfhXi6g6DcVKdYU5-OkMXlwvmVsMk2Z0WID4P-7HYZz9qWlN7FuLhe1QEeEImPMH03GQnsjFQV20uY67pYsfrt6evfrDmFchv2LGJoFOS-AQ5u_jzU65thbhdc3PHMmkM-ka1B9tFU44E3qGIYaSrIgw9MORjwaKYCViQea4CUVc8BQQtOfylghci7EcE1aGhaAwzlm8Z5DQZJSSCWMS-1UeShby8uYqWi4EJsbCT0TYbTdUxex6P9gUDd51d-L1OoAohKNRHZVYWeg-1ML12E_54WvizH79lVcerGCe3upPNDd0mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97279" target="_blank">📅 02:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3NXIk3FS5MxXnib3rY_ejiVw6tvbe8_7jzQrwCqr5KxgAFVQ7txQjuR4FGwkF8C9tTkDtvTdZD8a5PqlGnf21jzE6GMC4jctJhlPmxz4_RxhF6UuLsxD4EzuIbDwVsCJ86UtdP3N731lRscPyQF9d522Tl9y_39S_oMIX4SSgYm8caQ-F5UxTmKYMnLkyQ2-sckOcn_7bJZ00-Hqk_PiS1seOj3qgJRF899OJ36pBrtdyy8VWa2U5fLaaCO9OkVYYPGwJdks_ogmJ8U6rmMWTJjYH6sZJPBqwKd-YwI56G9wo-TAg0Sx3dLcQKGrwvNESUISgKC2KvrvVAgfuFF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
برای اولین بار پس از جام جهانی 1958، تیم ملی فرانسه موفق شد در 4 بازی اول خود در جام جهانی 13 گل به ثمر برساند!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97278" target="_blank">📅 02:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/telQSP1F6JQXZfmIatal_9lNbwlov6dvvfwqh-zhX9dVFuS7qh2dU2Kn_4tcvfXM8IiQxac2YEUesR4EQFrO9o8x_d6fkVL_Or9xDZERkahZkZc0U_3Xw-WTP_FBF1lRmBHpyRjqbOJl9Irbj5YXlLvLzR40lJ9uUjwF6lLmL8f5rkfIxYtGLOYMudsx-toPDjKtD4OmIr6qH0exwjhJjN0mnqwj48tTpF331-lzxJmsjXr1fBKugLnccbzO36qsPlXK0y8Xp-Ms_gGn1HGh_DDTOg0gtvEcpFS_8_n5QUSpJdARlZdfqUPiqAhu5G-ySm7AAImkOieh64yjoA3S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97277" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzyHc0sEj5UCHHv0AYBgfBGhpitpIRmdM_SFumcFljCJ-yfQcDiXxsNkk9s6rXCe0JokRGv_VNQBosYxYd_2eXiD5Obc-0-gk7-O51i0B6-0q6009D51EAkUDiZZkie7IGqVgNKLwBs_HrDhnZI5AVipGkjBg2R1tnwPhESYhWmnYrXRYK5t6vfg6KjWjOr0G6ME1DjGxIUfBCLOiPy75eTJ6mIgjuKGIWEDwV7D_zP5l2YYxp87koZxn59GNGRrhMEehSpYsgbbN17B4KheiKi9-T70I11J9zaqJbhT3_G-VoLOU6Blsvv3M5RuhhdUdR-iGk1aMlM3OtQS27qv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fv78rxAX8SZFt3LQUtBphIk3NCJ-IwfwDXT-gix1DiOxcKR0u3iC2WxbGkKbPadPTwL9IEGgZmtEYvu4gDwEwuqcU6ya45qir0ZiQkTuEngaPOW5y1Kfzji8aiQO1LyL6q3YFze-NSXxAjwdJvr-QpGsIiU2qQX5ofWojrsoxh8NQaVFXREtUM27KIBCnImkx9PE0yp1iJzMsD_DKcbOv-Gy0OKG7cWxahweY8XBmehFqlxvFR1TL9SnzPtXNAIz1F70FheRL780sAfX-gveEuYfmt_8b-gbXc3N3V_5fFG5_uY9sjWTH8w7OI7kAZ1Pzk7xOBUJibcHuNSAPJ06NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🔻
لامین یامال :
🔹
راستش اگه مسی نبود بازی های آرژانتین رو نمی دیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97275" target="_blank">📅 02:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5mHryKu9pxUSObTkcjVVHjAbVLEj7CGF6STitGxJCqM0mj3LUb4EuNZtyhELfUVbjwFDtxXbOItydxiTHy2kAOUHwzEagbHuNjnHHMKD0sDbr6O79QS5tBe_9vZOm0Iz44rDNPjTBoLnp3TkpmieJd33VHt82eKbB9sEg6HuXL5cx88slH8X4JOABxBGo0W46tqjIqAPwcLWnsUztpMwCHaAg_n0JvpsQRsU5Ehu_4qGIpaovBSHHQExyFBeoXvyYVI9bFvoOWpCTNr0hYKoYjCDKxKLBnAcZHaZmNjHjxCeJl-3qXs7m0fCAt6CeaQCAPwgmJOjZ0j3EFbyBxM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم دشان به امباپه وقتی تعویض شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97274" target="_blank">📅 02:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqK83Hzuqj1BviSI4BVBWV_f9mEckCKHvb0bX02v3y6k-xaZskWQ1RtvLkOx2dv9ztRxt55B9i7EAOKdIo8DdR3AyiB_p3JC9Bo8ruggrd7r9L-gOeJDSkbcSUUhcwDRfA-UcHUw2J_aSPy1UALOsvXIcR3QzcVox0GhcHYGcD-jss80dhJfPLpTVcHvhFd1VPBSyNFv4KQBlPA5Epx5GBvfn9cnHgxH0wo8xbQlmSI8c2CxkTT5yvPDRr4dKmjZVP7dYihKp8fdKgkxvN-mYJykVKCcgPoAwsm3VV4vMIF35-iDPX6lQPX5e9xGnaM3o38kg7bnM7BzUCh7qkyjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 تا اینجا 5 میلیون تماشاگر داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97273" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ91L5WpbqyUIN6rgjWxsRZHoXeG-I1kcYTYse3IQHqruAzR9CWaPy1M4nbSiTit1Ba5IYjw1CCV78WzYRxQPAE2QB4tb0yhL_I7OK9-YSvQmWMmuoeuRuYOmEn7CEh07P5kHC3i9USakdK_y8UgDPpKa-4hFvVhfFo_jKWzW4plaojzR37TxNpZboHFKL4OIHEg8tIS_eQ_C6oud8faqKLWr7-8JCmA-7DEt12oFycFXqU2WszeYU6OscVbdW0AppHCv5KIURjYxWDoenyomnyabu71fbholhmbu_nS_V_60yghMudT8IZu-F9yleeExRRiveoqS4BcuTwfmKERcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97272" target="_blank">📅 02:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW5pGPoh9XJXq_NoWLAGG6GoXkXtLXLet4ePMpZACCx1B2hNyNnKIZcJbpboCRoqdPYFNa4I_7hsBeJhEn4vKD811PQFaFPCkN5ppr2OGhsSozNeQZHaKPH9Vr7CI6EquyFgwI3jS8En9bPSpWH1AoLWh5rKnCfNSNFlt_NzSdbZjI4McTN1CHgLLuMZvZwed30pvqF5ntJ_DvdstJhIyzmk7XpJvOyToY0NJzr7iBbXMj8Bp9krCePIDFnkmveuzE3GTX12E3LbAnUxQS0soBkoS49QkrqzUC1eNQeGFzWnRrz1tPLHT_pQhXGg4hUqQVN4Tph59zaqB1VixYdQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_fHBiymCOsDdIL-cVXfxBnB1JJEwQNTNSFRZ8cC0bb55t4tDpb2WzslDQFZb28j9N4pYdVMuBZLa70k5wYaNY1tm6WC0FwSqow0hdYSs1hjZXbvwzyJa0pMnM84R99SOAJ2dTLOfn-8JdST1k_FtgHUh1Iw_8DChiTXh5ayApRBbOEl8AkGVNon_Kfb30HNmbtFsIJG4Q2ICWhaC9gm1VgL9F_fYKfplN4IltJixwBUN1Gho-9vrbFdqprkpdR_II4mp6MqM-4YntzX2BLxmuCldUYB9-GJO-ro-8yEvhXViDAeMwjWoq8OUcO9Omcm66LdBM8VYn4aGIEWktIqlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🌎
برترین گلزنان جام جهانی 2026
:
🔻
لیونل مسی : 6
🔻
کیلیان امباپه : 6
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97270" target="_blank">📅 02:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfIRpGf6dRDNg7b37j5m56Bs4iBiGBifNrFiDqCIx8LTbyOWpfVYiL9pYLvmofJ4lQAsiq6XycjhLsGQzd-Fxh3Xnfma2Gk8-MzicIBNQdn9qA9HDuxPPj0i78eXPpWQXdOyw6thRWMV-oYIN0FuNxm9yUb55YTvQ0FtM7nO85nme-ZPPxUso_bzXB_kZZjoydk2924IJHv7CbulS2rL_3i-wiUTbDsl9DP-a0mNlxroJ9v6eceGoU-UsDy7dUTw07Uc9r-ljgsfCG5EcSIeHPsFJ05ViK2QemOnn3HdgP2l1Jozf2UpFQIqpVHaP1oWoKOlpBiNwDOiKDxugcdU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانسه به اولین تیم تاریخ جام جهانی تبدیل شد که در 5 بازی متوالی 3 گل یا بیشتر به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97269" target="_blank">📅 02:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=ju7boiYOfL3BIo41FTaBhflqeznZbrh6YsYn5AVGqUWSu7eeoB5LPHgOpyh6suiPR3d8UOFgtDx7Wsrcu5R4wVng6aFs1ebSglKApxY3zb6alGUYA3i_8qnrylFUz486EjpLLllEJ873o4SbWfJun8BRfD7HFCMFGPjP3dWi-ZuhPX5C8KPGAbYmKsz_zVsxQyZl4xZohE0dYEiTYOpKhz86M_jVZGKwdT35QxOB8h2nRLJY9PIkomPi8PMJ87qxCzteIAWBU6zcX-7hqb6L4tBDpsj7B2zjV-T5encX6hV-uiJA4RyS9kHESpJmgu0jg9StoIJGEUx3JvtryK3xcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=ju7boiYOfL3BIo41FTaBhflqeznZbrh6YsYn5AVGqUWSu7eeoB5LPHgOpyh6suiPR3d8UOFgtDx7Wsrcu5R4wVng6aFs1ebSglKApxY3zb6alGUYA3i_8qnrylFUz486EjpLLllEJ873o4SbWfJun8BRfD7HFCMFGPjP3dWi-ZuhPX5C8KPGAbYmKsz_zVsxQyZl4xZohE0dYEiTYOpKhz86M_jVZGKwdT35QxOB8h2nRLJY9PIkomPi8PMJ87qxCzteIAWBU6zcX-7hqb6L4tBDpsj7B2zjV-T5encX6hV-uiJA4RyS9kHESpJmgu0jg9StoIJGEUx3JvtryK3xcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم فرانسه به سوئد روی دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97268" target="_blank">📅 02:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97267">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دبل لاکییییی با پاس اولیسه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97267" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلللللللللللل سوم فرانسه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97265" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امشب اولیسه تو گلزنی طلسم شده</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97264" target="_blank">📅 02:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeLkTO8o8Ssjbta9kFIB2zN7Iz63BrGg3CpAKgk54t8ZCFLEJGwkPMIe-bemUg_kXppk7RRcvORcRJGzT03TWsErDMIuNGvulYYF7SqYZNfohLifDeVifLEUhMtxEl2EV92aeAQYJ8wAY2szLj03gk8-cfNij8pk9v0hRRwFwuoJh_nNnvI8JZMCsyT3f6OHTi7YcmiGhVzJzEsftgDREXZ83b1IHUedzuJG2rTsiLbVf1kseetwqfbS6RDbcFB7qyopY-r0h0wbWN_dDRP0WpP7K6Z_4Kb16vrfP5E0LDWiFDSUtrVneTua2UpXDEtZKC1AVghsx4x-ogLa97mT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TP6hw2U2r0PYkEnWWgxWuKg_3fHBxrcHzV_HwyXlkbYq_DtcIGiB0hof18uqaRAMZ-nIqsG2dASO0kDnC4QSFm3m4PAf6zhUqpp8j2jc4NCx7YFPrvIJ4sionQVPfbL2k3Hs1QOFl6Z6_gEUsbcZjFt3DrjgxmlzraEnm8VaIJiD4CFfqqPLF8FvDUJdZbKVqjyGqmz60iA0EuXy6L8UY4WAxItztFDVWcJ-YN86PeN24qZzLDMtiIrYVJ0O3tddFO-JDw9lo6gfMa7Yaal82UQ8U9WcitztbBxz9eUZAKFjSGp8HAganisN-xSaJRr0yP1u17OzEWoVBbVPWGJ5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htmarO3nt98G8vjQibozQ2iJ1GF5AXOQ0FjqMmrH0WHKAizmmiddAc4Sjtyw7eE6rSYMBe9fYYZ-Uc3uRYx_ncp2nvinKn0UERJaXpl8lkoNaw5_6n9tuR2IFfzCK4B4z6mr6v_T2PTIrzSMQ6-6uqx9lL-J3VOhQWg6A2mllAigyNvOgMDWrmqKek0pZuOxLyMrsOf64UlUCXmj0tZ3QTa4GsQEcenOij0Dh6jeG_U5YWA3SDE06Ok9EqXNwcR4DvPy6UfsYvpyrbHmiZc1oATuyjnwI5HQx39w71Gklr8Kle76fdgogqDEVllZeoFu3ShVhXJnN5jr49aBqCXLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGd5Ud-WK2leKGqb_E028zD_SBmfkQsnQ9LniJ-EX95ZdLnDJA9UZXnYqd4SWtjvsBmtjrFLQwLa6kTVeRczjZbqyLAgsO4HlBlucK34wwkziMaszoxbpLwT4FZ7k8fSc8UlBHBKDI3OHA_WxFXJPbp0gNuKrzomXK-dp29U30O0_5znlrkcaDmXPzQVp2Sk2aYeBaOjSc6P72HE6TkLpjeiE-C2-_zxlBmUXKvEhzpFM1sAW1mCocTrggQDz_MfWaHvEpYsTF_e1f_Ij_XajYEt_KycYwnv6emJwfZK9bSNr0dUCaK61INpWI9N1C5JBfqENu3SVhJtHEIQFx4LYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edLE6PtrbXT-OFwTC72wk4IvpzaonmuTg_dn3d8eY8PBEGjaZFs13s-y33Kb3NwelClkotO5IGDeXjM0GSBNZXOuJNZOFimHYqc1ndEEplX3qr1c4XLuJiFGWNdr1bQUbH86n6rJ6O-NzQwBhukYKk_X-u3dndfEmBM9-2XiAhNnuUvgR5ZzJSdMn0-4txysCCJSre03pAWPtITod3SoXxC-I3HC9MYAwSMuev8kx4eu6RaqKJqUueE63PFM45R6iqcamWfOWL_TrWsei7RFIeYTuyKdR7hwYpm8oN1ldwp-ygnYVLkVQfiDglqrHkEOMGWTlXw6jad1_KdPeN49Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای سوئد و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97259" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC2xpj2CIChpdGnKn1nNGIWlThV_BGVOs61I1UU71QjXV9XHkLk5FeTaJj2dP9MVTE4gKrZmsHbAbKMQFQdo3YJ3rZwdFoIZffrcjXfhFgHDz8DWWIgnOB2krNKK6tWqR_buIXwOGppJCMULizoNhypxFRvTOxYHx1D_nhWr2Z8Nm00Sx_1-ChfY-kUJaCWga5UNfDr4Ub8YwJsyVI4lrEIjFOMrKA9aBd3L5n6aJE4eRTiZ1XDScSrGzJoVqkNogyYW2IkvIyn9UY_g9yRHVnCS20CMw-ZYkOXPL1A2lUyRQq_Q1jXtZ4_dyZp3HO-aCkmlb1rlBykCpYE9U0uRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97258" target="_blank">📅 01:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گل دوم فرانسه به سوئد توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97257" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97256" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9YduXyvCvdR5kQEGts0SC4oHf8yIQAZEIAyTJBySlrP1lbKb7RZbdhhIYauGEZtwMTzcMr0UyZz6yaLM4VzxpelNUMGfoUEhCdJmZsFdZbStqnHgyl8C6ejIi2-rRgmdyhKAFNU_ATauYq_jEaR3wHQmra_4EcjvPYW4DCR3GQdBRrWd8uIBVv-MXWHUJW6_-W4pApOICwb6Y49i_oRP3cQrjL5eyHYotdbKtN23d72ZrLhdAoGLqzyGKKmLj6QOck82H8KNloAuhfVZoT1mwDqS6ZgzLiUSytlmRDmPj4qnbEot7Gn2og8UPh04LtVzzJEeTUzVAY4nFi9Pkxysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97255" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97254">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بارکولااااا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97254" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97253">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلللللللللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97253" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
