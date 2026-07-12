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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 179K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 00:41:58</div>
<hr>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=W-0IAM52AnOhzI-UpTIbR3TsjmE-vJd-SvUyDXM0JmIzdOUXDRZvyj_JVGAYjF7rwRWUJ3LHEBjQY259quvoA5s_ej1Sf1lvdvOXgOdTvrVvt0T2td3-lPZZ34GriKlhSrVr4H8Lmm0wzXdlAAPzWzEou4YLvF3OweXpprKc2gVI2eoz9v3gm8DqmE05J3PayZlpKcBJhTwFeQjoRRKUbPjSUBORObEffldSLhWlgQVge2NORZpdAnYsABcV2hdgKGXc7csW1_csxYplGQ798-poGtoqOWhx8fvAnvnz_rhE1PRaUvub9-mxWA9AnwTDzUHdohk36eZSQo8m33u6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=W-0IAM52AnOhzI-UpTIbR3TsjmE-vJd-SvUyDXM0JmIzdOUXDRZvyj_JVGAYjF7rwRWUJ3LHEBjQY259quvoA5s_ej1Sf1lvdvOXgOdTvrVvt0T2td3-lPZZ34GriKlhSrVr4H8Lmm0wzXdlAAPzWzEou4YLvF3OweXpprKc2gVI2eoz9v3gm8DqmE05J3PayZlpKcBJhTwFeQjoRRKUbPjSUBORObEffldSLhWlgQVge2NORZpdAnYsABcV2hdgKGXc7csW1_csxYplGQ798-poGtoqOWhx8fvAnvnz_rhE1PRaUvub9-mxWA9AnwTDzUHdohk36eZSQo8m33u6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTbp7J_X24O3OJtuKsSw2ZHv7Fo7Co8VJZtmrV4JhdQGn-pPrRji9KeeP69VjSuXo7xfei0pP5eE66zjKqBdFBupQofgYgoc-Iv528jCGqhnBnhMlJbO056iGdspZK6nduHG8M_LgX-dZfddze0AvrGEzLMBpJq2rqxPrFhAvaFUaoCcYA5d0HTFpOK-bMqkzXn2JVIZwnoWHkylRsX_bwfX7uaRXmLyJWZzMhLihcOSxEZMsb77JIf7RZMLcZ7AAWVAR8TO6ZZOueN9txkEeB8f8DsZs-IOcyanc27jxr8JSe7ZmjhRC5MlX3JtrT7F5AkS-3Tf1eKqRCcmySpohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1TU8_d8sA0cMqBREG4hLKtGbe7VEKFV07xg65TSowvI9IBBLdVus042Me2KzQGwca5_RSI8Rs748-nFKj8Lb0nscddv6JI3vDswJCUb7rrk67qUNDAVx6ernVlaEd3C39EaUNtBLzQJh4DZmH5VQ-R-mQobVgX4DxZ030i28MbRXoOmg8sr-zlU1_HXLWzAUjey3WHAPoLUkOAShuMd_GR-xHVmTThUAbZADnliZ4H6xc3PZtspP9-g9rdrnSSyeF-a2QXJ2j6fSbzBw7ma_UejaPeHot1pE1RDljdwI8Wnx-zyilSUm7fuQIzBpNJqDWi7SmAkPtPeCtC6squ7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iR6GW_XJfD2Rt_PG2TjqEqm8WPebjxd3x5VeD_IKh0nNaprnb3xCPrNLJac1KDSefTnbhEgLQJgB1km_7m_HsnTWsK7AOsJGFZiKGfzPL8V-n5qyWlCPn7CkxtCP08rsA_OFbC_dag1qWrRkVRHM-1rNStJfRqgBkYF03B8fM6aaxWNU2FhR5wfHqoPJquaPkod0j0CGaI8_Qm_Q2c5HBzpMjrymHxViyGpn9ePHP0uHSjs8p5UgggezbIr5m0w05FbU04KjqYqsAQuqQKvz-IIy7K7TDU8wyvbUZ6ZCQaq6QkbdiZKfBPKxjhFu7KFkVY_MML8GEs-tOdm1AxocBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjPLheQG-KlbONzYDK2AUtH4s5JH-YLUyDCpCpnQLqBe7ZmpM-DnphmkZxiHHFME-PD12jAe80iSP7lTxAxuw76gdiyPlAucdaRWWto8nPdJpiYVTW6FLjI_T_1IvJo-wjXyFN5LUV-UuKzeN03iMwbBUZ4UC-RkDlH6Ufi_-dahec51NcW_j7_k6VYG8x641ev9Q5waAFrYIDa2lgmkv9TtOBWDUUPiD2BHGxTnOlqHYMY4HvKggu9LDMpYsFQejLZsjTO1hKPpzWWDPwq1hr52H-5lwqvh6JdZAE6DOJpLMaaLj3Te_hFNqmZW6qXE6BL5UiX0RWybeFKIbDATYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalxPY4otBZk6a4En7Dx3zaumiTvRtTk2BidDx6PhQZ093qvsbAtR7dAV0BOYrcbMgF5u3BI2jGMFjX4DIbECPIpYd9RZq5zLAocXmE126MJ8YMA4v2tuhjajG0ZtMM0HHH2YtxtYM1oB4ah00meLaFX7ETvD9_VQAdbCZgURR1sH2rJFtLn8dPetijZD4cTOGDUS5KpzBCSxvgp7xlxEsOEogO3ek9lMRpi4mMHNSyYLMMQUsa3qawX-1Zp2RH60cTIeb7qPBmUfCtjQD-g_rkOQDAYi6D4fWkTsRi2yRGFsl5u8jARTMnHj8GpIGMBYUVoVTmQc5kvtZSzEzeoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5YlkypWvWJbu48d1tWyXQLuVh91FBvrAwuYIgnYbCeZ4bFewj5V9IoTZ2IvGOL035K-ZJ3kLKgYlJqracI0mILHdEqtYsRrOBtycS4c0kLYQxYCs00WbKJi4r0TYxWWhn84zflSo_NKXoSp2OEa_-AKNKnq_AOWi62dvnwf4JU-oruvTO-_MPWOHIKUKeEPvm76RRKYHw8KMMnu0E0ykzCpjwC8xPL-GwKHxX7cMIdyd4hF4xvKBgSCLrkomFmcGvxrno9ogZcv8CSNZEY87IqqSG-uAlRwMcOSGkHxRK6nQJVe8kLqdcTt8KX6-mhGzgW2orCawR7745uvqKGJRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=Whyn_5mo4dAqkMnbf5-y7KULAUwdTTGWqx1EJJOhtZFXyFd9fUtZAAXzvOfIwnWsl8gPvto4j78E-sVR9pCjH-MauCa0gpeuySTK9T0cXJHNd74oMaugDOT7EOA5KGOTLrzogzzP3_COe572Vxi8naGbb9cV_mil7GbQ7bUp109Cyzu5XVbE1PKGALBr89DOWIf0f50CCqbTCyYIdePnGHAbKIOEQ2BGB2kQiUEIjaBsxMa4X-yq8hq6oba5azqPNW-FmYNqkpHnAwYO3arr3nB6vK-Iq723-vTZgmuNzewDTJ2p2Rigdu-qSu9SCh34fwXhEsXYmrTHCpwiPfVn0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=Whyn_5mo4dAqkMnbf5-y7KULAUwdTTGWqx1EJJOhtZFXyFd9fUtZAAXzvOfIwnWsl8gPvto4j78E-sVR9pCjH-MauCa0gpeuySTK9T0cXJHNd74oMaugDOT7EOA5KGOTLrzogzzP3_COe572Vxi8naGbb9cV_mil7GbQ7bUp109Cyzu5XVbE1PKGALBr89DOWIf0f50CCqbTCyYIdePnGHAbKIOEQ2BGB2kQiUEIjaBsxMa4X-yq8hq6oba5azqPNW-FmYNqkpHnAwYO3arr3nB6vK-Iq723-vTZgmuNzewDTJ2p2Rigdu-qSu9SCh34fwXhEsXYmrTHCpwiPfVn0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtoAyr_lay5ErF2lrfaS3lXQlakJWnEzv-tJZSnInRIJH9JND1RABSiUtr0lJa0eMkIERX18N6CesqXu-WAUQmxJCkJM3LC_hoUnX3jOty4oH2CxUShTrOuaYiTH4RTU-ECiHkO_tg4IPijBGUl9O7hfjRZLzESsw61wY9kvCy8w2199osN6PwTf6JlFSGigjZlloIIHodiQGbvA7EPHbR2qsboviFN3wHz2tM2jUni4Qd7bVYu24JgtueyBIgq6AuOvU0NFenduSSdBCmGWoN29nHtFoNiknZRv2K7gdka-2cmEzuD4Q9K11MNTjLfilGZZpN0k2VNZEj99mvV1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8D00ijlgyxyRcSDswn21JO7vkgy4QVHV3zTfVgd9b9pnvIO51c39NdaoYybiHxEErr4-_0HeTR1CeUYS5BdDLMTJWYMjiBsMcj8ax5fWw_9dRLU5_eHTVW6Hp1O4_bIEQW3Rtvh2oyCbj2sQ7LyOxwDCIFMDZzdOgHbEZAiVbandkyvcKIYGAVWGFdPJh4IpMnBnYu8nOaiSvtcxHE9hsptOjgKdzJ9Rpik7s3sA3Qu8fttBNLyzg4yXNCNV9znCYJQHV6O9vcKDH-I8Mx4Lg5CAh4_yhvEAE_b0sWuch3fu9UeRy-5f9tuEUA2Ub09l7tlpefbudeliiswTv9lqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra87xl8jfzrkjyWJgdJiUe9DuyCGw3MzyYR9BxenGQuy1tD6fkvQwgTff4ffAljeCTecyvVL6rM58ynjoXSelTol6d70GJ0dlf5W9T41-ieh59XRVbA43OsKGB2IR7j6NdmTIfNutoV0Jm2RPxlpLRmnXPYkClMXAde40_9xHJ8NtGV3SjS-icjaEEZE26E3chIdWa4QlqBcUpmWSsQSQn-pEIYF6lj44KaVFS0NxAOI3bPWjbijcm0K_3CJQs6lNPr3As7furNBTWM25ONWOVv4fR1hGgtVzKVHwI87hKZ_czlfPeY3WwSCqwH0KMZMssfg9iqlxqOo-FcrkLDlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8f7jEDwMbBc5Uc5CqnUEf2dLKS4neZAIynrdbP8qqrPDXqovQdre8xPiJPGkxCmcROyEwQ4UtVqypiTmCzf6brBUoy2dHFzYwaxshpuIc8SfFTJO_4TyJSLtFv3rzKIjYeuRVWORabOKk1ybxqBb5agFLBHDKGO5P9V0aXhKv5YwGsDvzUPUHt7Gyyy5tPDA4JwUewLH8VxYg2qDqbeh-K0_K1RF9KiUtX1oUucc7OIvx2ZLmNLrb1uKm7KG7f2qehyddaiG9KP73Ik9lGXJWTkhkrpKDepMESPCtOA1FDDRx5nPNwWvy50vGh-oj05Qdh4Y2-Qz5Du0AH-AftdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONzwFF1ViSZZ_22tcxLd_Hy_dmmXFP1AnU54XX4L2HLAgMFZgR9v77V4BOByttyfDVOlPHfVKU_iA5yIQ__v7jQ0iMIzf4q5fSFmg3vVh5b8GxTsCkv7ThqjFsMp7qus4RtHO3zjC1mylbmSwOFovbxMuQzQONn-_FljAFYMKbRZA0Kv8je_UfeWVTOTaFY3AcrqiBLGXI93mifQBWnUDv6YjWPJHuvoqE_YySugZCzqM_R5reUwkMP0IAdqVtBcuZ71tBaRWmimKnLJ_Kb7En8Jr5f8prYORBQeJvi2kf_OLJm8lNe_j3dTPqLRRYr2ycemh1arP9iLBBGeUjYc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=nDyVDHYaY2XeNg8eAlcvHXxok62NO7VCsZL75LAbzUSG1T5fs4TrCOaYYNMZ_7u6yXG2NmWscSGSzZNF_iPVzOr6aA6VZpxja2GcuHJGsWvRqA_hEaNVHASxJ5Ilufs_Yo48XjAvklKkdy_hfDrjHOmkPETMwO1UqHl86h_fzJLQwriX-6CRM_c-Z7W0LvC5Hwuy62AVxMZ2ynSg5WvYotCbu8ssm8Hs8IBzTgDuVA3QqBON1k-pNN2h7-xtrp-OENvAwwRU7l7zaEKvCywekpgFIVbBQIzp6csDiCBw0TtSqpAB0ZnBXz8FAQbDst0qtIx20z3nPWsGah0LFbF0Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=nDyVDHYaY2XeNg8eAlcvHXxok62NO7VCsZL75LAbzUSG1T5fs4TrCOaYYNMZ_7u6yXG2NmWscSGSzZNF_iPVzOr6aA6VZpxja2GcuHJGsWvRqA_hEaNVHASxJ5Ilufs_Yo48XjAvklKkdy_hfDrjHOmkPETMwO1UqHl86h_fzJLQwriX-6CRM_c-Z7W0LvC5Hwuy62AVxMZ2ynSg5WvYotCbu8ssm8Hs8IBzTgDuVA3QqBON1k-pNN2h7-xtrp-OENvAwwRU7l7zaEKvCywekpgFIVbBQIzp6csDiCBw0TtSqpAB0ZnBXz8FAQbDst0qtIx20z3nPWsGah0LFbF0Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIifafmDSEBBc-ViUPKz6RHQTT3wIkjG56uj3qMNJXkRz-PU2dtcEmCM5kq4UEOXMqJGKeUf0Ag2q8Bx5vT0Op8pq1XxQzQB4wzGs7WQ22TUlWoU4457WykFDVEq-qILMDRMPEsUH-iIMC2NPZeVwiV40NU1Z9b4jPV1mkU12K9nBHx8bo3H0S-F3-DWUSB2Z72ZQXGOALWSK2Dw24n9C3jkyqAWLkhy1eTgJC8aThlBNGcU2tMT6VNfAgzV0OnKLYu-yZ9Pvwv1iEFLhXINecu9WNGfOmgPCfv1KjW1dBvGLF_1a0csbwSyD3U-paifcsmGU7lVsAr307xxrhX2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=oBQxEyIvTwB13TLtRDP1zyWR5SQiHZA6a6Dc5kLpaAhBgvNIjaqG7UfQspU0CCAxmNoEbbJlTI2KFxon5V_pOg5Kx4HaT_8YAEFmIEu_RNivIIeowsNmusgchdflxrpfcYHzdeuaD3o-LJKIvewCTS5kyTCLdxvRxKsOqL-eK5ZiSCUMq5NgpHAXm7tr-dDBNcABjAW3mKctYrmKGG_EBqnzH4K2pmU8c-yIZ0eco7P_fs-QUbRGXN0Ebkl93vZjMPxuEf_h_E888xpE-HF7JdMO4haK_xt549Pyo4WCDmDyVluQrqpY7VnZXiWNAnBDUJSI3zIm_w1xgh4njryrSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=oBQxEyIvTwB13TLtRDP1zyWR5SQiHZA6a6Dc5kLpaAhBgvNIjaqG7UfQspU0CCAxmNoEbbJlTI2KFxon5V_pOg5Kx4HaT_8YAEFmIEu_RNivIIeowsNmusgchdflxrpfcYHzdeuaD3o-LJKIvewCTS5kyTCLdxvRxKsOqL-eK5ZiSCUMq5NgpHAXm7tr-dDBNcABjAW3mKctYrmKGG_EBqnzH4K2pmU8c-yIZ0eco7P_fs-QUbRGXN0Ebkl93vZjMPxuEf_h_E888xpE-HF7JdMO4haK_xt549Pyo4WCDmDyVluQrqpY7VnZXiWNAnBDUJSI3zIm_w1xgh4njryrSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=VbsOHVR_6tvGgvV-yEQEIhWKwH_ZmT_z-5HGED2FZ19iyWaBI7sN2sxAP8LXotonlB9qFPJ_qhPxSgUSgY8PWJwOfSCNBG6TmVVLoWMTSd1HFhP1Vmty1TXqDUviwRSYJAkHiHxAa5a6vAa59G-krAq-8Y1O92YwyXM3HhlyVsKchpo-vWPzchsRIHWaNXN6D_pgttdJLk1WRylGf9TfnpDczH431_4L6yU285zCfFAnwjFR59F9XySk6l2IwSkonWK8YpFYijGdJFJwWr8FOuhkvtsK-fmjYEP7jFWgoTMVJg3XCOnTgW7Q4tyQoxZnjidw57mN88fokWGr23CjY5MVp5wj8hG_W9hmVGrhdEFCIDz2dNxn9k-b1PGxdVtU1COnlVHIQ0oqv7q43JWifmNzH-ZNyeZullXcWIpqQeIyoPZdx9N0MBKG3EHYcISDFUQ9e_RT112f6GN-EfDxKNdcX4QqdA5blRPDh4FA2y3pUj8yiHDBxFzRFa65i1b09_t6KYZakPxPi4NSKC_Gw4Xu-4PgVe-1ql12Cx2wacEe_AYLOc2ibJMolSQtpsH-wuanmeWgsIaS8Bn3wXnfN0fWti7QsGjywb10kGsbVu3Maf33XPoMTw5OF_Ks03QH-f1vnjn6h1-G4zGTQYywSNq-5Chn6CJmfvOXNxyZKr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=VbsOHVR_6tvGgvV-yEQEIhWKwH_ZmT_z-5HGED2FZ19iyWaBI7sN2sxAP8LXotonlB9qFPJ_qhPxSgUSgY8PWJwOfSCNBG6TmVVLoWMTSd1HFhP1Vmty1TXqDUviwRSYJAkHiHxAa5a6vAa59G-krAq-8Y1O92YwyXM3HhlyVsKchpo-vWPzchsRIHWaNXN6D_pgttdJLk1WRylGf9TfnpDczH431_4L6yU285zCfFAnwjFR59F9XySk6l2IwSkonWK8YpFYijGdJFJwWr8FOuhkvtsK-fmjYEP7jFWgoTMVJg3XCOnTgW7Q4tyQoxZnjidw57mN88fokWGr23CjY5MVp5wj8hG_W9hmVGrhdEFCIDz2dNxn9k-b1PGxdVtU1COnlVHIQ0oqv7q43JWifmNzH-ZNyeZullXcWIpqQeIyoPZdx9N0MBKG3EHYcISDFUQ9e_RT112f6GN-EfDxKNdcX4QqdA5blRPDh4FA2y3pUj8yiHDBxFzRFa65i1b09_t6KYZakPxPi4NSKC_Gw4Xu-4PgVe-1ql12Cx2wacEe_AYLOc2ibJMolSQtpsH-wuanmeWgsIaS8Bn3wXnfN0fWti7QsGjywb10kGsbVu3Maf33XPoMTw5OF_Ks03QH-f1vnjn6h1-G4zGTQYywSNq-5Chn6CJmfvOXNxyZKr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=ZvmWF7VKONIiNrKhPgtgyjCu_Pa6Aq_AuSVaDHS4_GcRxZ0b883reEeoaAYLYcR29sMnVlZevZDpmB3yR9YQLADPOIL-BR3FeoX4pa3FVQheDY9dtO-Z_dDTpDFxmGtFO7Excl-8Ua3FOiZn9VnanaUd18mPYJiVilrnp6yPLf5Mu5andhN-5YuKi0V3B5alnSZ08bKGO8wiTodsHAh5mg6RFgnUfWHzw4v7NWbnJsQ_qitciiN07gzC12WbiFpCAr2FgJTWMsttPhg_vWocCspsXNd7_QVi9QLsrjirMkQtdV3YySJANxk1OJPyAJ7PYFSGzUft8RFDr9A2HePqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=ZvmWF7VKONIiNrKhPgtgyjCu_Pa6Aq_AuSVaDHS4_GcRxZ0b883reEeoaAYLYcR29sMnVlZevZDpmB3yR9YQLADPOIL-BR3FeoX4pa3FVQheDY9dtO-Z_dDTpDFxmGtFO7Excl-8Ua3FOiZn9VnanaUd18mPYJiVilrnp6yPLf5Mu5andhN-5YuKi0V3B5alnSZ08bKGO8wiTodsHAh5mg6RFgnUfWHzw4v7NWbnJsQ_qitciiN07gzC12WbiFpCAr2FgJTWMsttPhg_vWocCspsXNd7_QVi9QLsrjirMkQtdV3YySJANxk1OJPyAJ7PYFSGzUft8RFDr9A2HePqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzn_f8QP17OdvKF-QQsUfVq6zYcROJfs-SvO7LXojzMupmFpvpZTNB1WBwXhKRAdkIOwMAv54GD-BItuIWXc9SVpiV_TH-BvRt9G-lC96G5KaNRmR7oJcFC0diVyGSwE8NVobDbxZwpBLdC1HHUl0f_K2YALeOhdoL8yINT0gfIN_Zw3kzE2RL-crDMeZ9LXk8E-LkXgETBE4F6Ra17UPFDtl0gjle2MQssOVPJvQ3nR9mCViTPN1HRGoxZHkCEQ2kGywphn7BuGMFTyP61bOF7fuomR5UD3EFji2nsy3Ns6TRxMSsQUC7ORQiPTl7zNLCLL054Hr4zmejwUQkhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwrqi4Gq0JmwY5e9XOy1rrFahUwnsHeghMma-FU3g6Id4ip2_vthirD9fKhaI8ASQaUbqPhcx3yLFVIEXJSWVEf5ay6pRYTc6SLf0I5HPt70bk-wkajV7CXxejHHycSA2zLJRD7i4rrtHVH_GdUZIwzGarrr4bi5LtiPDifZGiPzzfvr9_rSuCyQnGAgl2R4Hcxi1K80CSJ46dxb_sNVo2emn9YI6WQ1yZWW7movivEQ95vkEzXBdHDNgko2k1neAx2-S64ts4NUTK1bSMc8T-185lTZAtOB5C_rCCVx1ZM94iI5X9Kg591g74daNJp1gzhzbHEBCP8w6op8BBfPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=F8VHoTUkgGx28dpmEvNPRrTOnk5qDA01cRMYFl3jszdnOAjG3BUGhENfAAA5Q6vcqXsW0BH1IyaYKzUPZhuNYiTTKjFx2HzIrt5U3tBZ6OGVExMvNjjfhqf3az8MUvw75rmsahHi5IuqrZgVptuoXfXXjntqUl3b_sojeNYp2rW7G4AGKtsFrx0lsJjlETIDrkJ_cffbr__8REo8UmhfUR4h9XAkHLKzvR-PL4fyxPMGS_tfUAnFGc-x8DkpMnbfLRxAqZswor5mvMrmJ97fItLYZCNf5bRhG4yZY39RjWhgd4OsGeHh-9aOYQ_bNoOSvpLoZJaoW74U0IGvIRBKsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=F8VHoTUkgGx28dpmEvNPRrTOnk5qDA01cRMYFl3jszdnOAjG3BUGhENfAAA5Q6vcqXsW0BH1IyaYKzUPZhuNYiTTKjFx2HzIrt5U3tBZ6OGVExMvNjjfhqf3az8MUvw75rmsahHi5IuqrZgVptuoXfXXjntqUl3b_sojeNYp2rW7G4AGKtsFrx0lsJjlETIDrkJ_cffbr__8REo8UmhfUR4h9XAkHLKzvR-PL4fyxPMGS_tfUAnFGc-x8DkpMnbfLRxAqZswor5mvMrmJ97fItLYZCNf5bRhG4yZY39RjWhgd4OsGeHh-9aOYQ_bNoOSvpLoZJaoW74U0IGvIRBKsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GfI5UdH4WV0Z2KCWv7rX1Kh5wcgVOZIb31et2klQR2yOUFcu2V_VjdWWMy-bq2WgovhH3NS3MwLmGNGL_8UkXTkSq4xmQAW_JHbmhqI7Lr8li3xrCTsYlzuy4Hwh6PLtfbSImUIy7YfatKJWAt7ThgQmdTOC8_gFo7SVDWfn8Nc3GxXAO08uJE5oC-4z_kYERLvj7whUWlYDhz-Flz7MCXA4Hq7szOo6OtxDZkUikq6ZWwJaVtLy6WqNfJYiyTwlUROiWbEpXQF6mH4z_Kc2B8ndGjpw0DFV3T2ipxasElcLdUPWc1-BiEyfChioqpkIZ55KfUicxSDK2cr6XA0whQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GfI5UdH4WV0Z2KCWv7rX1Kh5wcgVOZIb31et2klQR2yOUFcu2V_VjdWWMy-bq2WgovhH3NS3MwLmGNGL_8UkXTkSq4xmQAW_JHbmhqI7Lr8li3xrCTsYlzuy4Hwh6PLtfbSImUIy7YfatKJWAt7ThgQmdTOC8_gFo7SVDWfn8Nc3GxXAO08uJE5oC-4z_kYERLvj7whUWlYDhz-Flz7MCXA4Hq7szOo6OtxDZkUikq6ZWwJaVtLy6WqNfJYiyTwlUROiWbEpXQF6mH4z_Kc2B8ndGjpw0DFV3T2ipxasElcLdUPWc1-BiEyfChioqpkIZ55KfUicxSDK2cr6XA0whQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huhpdtM2_LJj8Ba4El8bptGfANsZXigqZrN5qYLKmYOky-A-Yu_H_HtYTy1O9SzyGrX84ApyeTs1EtzewsrIC3Zd57f0jCLaxPr0FaCpSKS_2_8SmiXYl46lk_iPYaDzQVCG_RR-SgM5N8Ia3i0xANfvFYKRI1NMCJhs55WwfVAWWQSu_RJMtpqDTuhneitYKOA3O6ryr6QMx2p7OeuZd22t0jtxCgp6iqOHG8bfaKdg5e784ivlioL0SoO3XBe-FmtOpRHNj406NPPNZoxt49ZgKt81k1wh55yhcj84qv-K5wHLHARmIuKba9JX2aRu8ByB7nitCKOAF-qFoI2GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tihg_Jze-wqO4nEgjQ2SciirsgR55Eb-D--UKNshI1woT1lqdG3UNb_XykzHS1s5H_us7hMYkmpCF3HW467abdXWfO_AsF9iUhYVuuRQ83MUGykGx_ZHuWbllVOCn1s9fhw3ZRDVlitIXirmv3WiXQL4N9THJsrCothuooZFTrE6eRG1rWc-ZFAVFL_gxfzL83YBmWDvG-5ExDg_J-KN0lY6acaaRtapMsGVRgJm48WAnqy7ofGEhy8JXYuqiYg_34CUNnkOjYT3JxGtKk006FR8_tDSHRISCKJB9R2uYblnvb1QTQR702Ci3tmi6riFOWy1zlzEbpiUMUBrDjFNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgAgWkiGJHxzKoLUXTiwTXNfZkdam9khx7jtKXcIcN6eRZvXHy8s8GA0CQ21hNw5JPQSi-m1UiNFb6rs_GzTKyHYJTcDf--3BDj_gzM2p3bvBk2BCM4zF9dfDNS29f1g15T9U9D_Cilsm6rOfZHsK8G2sx_weUalgauT8Bh-Rh1xECtKo8cRBuy9De7X-1srve4oXnXVkiWyeO-vieQLq8VoBqVgj4a7RSShhiVTg5tYE6t3Te4NsU6x6QFYLoW92r4mdTnT5g-JdUKUttYkoMJDJUXHRRbUxVu78aKQSGNzEsrTgDZCPgLm7h9rsiaFTsINhbmB-H31ztZ9lCNqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6Z4jPeYYDF8xZx2nD2HIJ326kw1AAT0_MXJ9eSvJ3Q_EZH--GHIMrMpAzZYhS6GbFIpjhv9BiBMxiS0n-YOB-Wd0QFvJE9i-RcEd5GZaP7qSh7xGutLS10QbzhNRdclajgWGmOxnxr8UnBabfiMOxyGQdYutLnCSR1LDt7eivI3OAZZKQNzrUmZOoZ_w9F385u0VqDc0cnQr5wle-EmX458O03UQ-k7fW-f-OfEfdekpSp2DXH-t_cKvqo6-5k_2K9ZhHSyBmr3tDFOFTt-003_4-Bk7H9fqE039PVLd4-emBYFF_g5-_EnCIz4NXKofhBG-Z3-kMkesp9lOHeD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic_mznTMpZZGshsofIPbbC33FC3Del_m5HFIXAG4iIO4lSSw7IjDtQ4C-Cf73vm1KvtgfVIWOWdn4ROLuRdVxkuLvkP26fI25tkBGSj8Bapqbd-aZZ4MXQJpzzA7OPN0WXvr9xpNCJkWEYxO-9g5QW6spTUfd3dPqWUePZjKloi0vbPaaDINVWRKv1nMHyJAZkTgN69E0QblbeaEiyMvl3RDdLVUVdWzmUVSnjtOFAvxSLqKIcZw9cgEmhbRk41CaZf6uR5CRIgOf3bnnWG64t61rHfASHxOtlhf6BVgQwFeWfSXG9DL1OqRBMqmeUSE0A4VD0LqvaTbGqjOfIrSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYP1-mKvRpsDHRh93JOMvbUPv841pvIwydJtjH7jsUldh1qSPQAByIVuvm7QEc42tGF3tGXKvSvnJ4AYoHwOK_HojEheyN0LkjQYa6qFfAHAA6athOnUV375NENGSMh0cQRlSTen5Lku5gQaOhENAFtjp8M4OeXPiOhLwp2o0vxoVlfwALkKZblu3uRGRjCvoXtd5mJ9yWvyBy_9q1w9SV18EE7LHG-Ib9HM2vlEPuZi5sCaZqSZtJAplx6UQpC6e8wWJdYzND3L--NC9NFBZDFe9TyLL_8WJ9V83iVDMR9PeRjBeG2biRd7r9D5umI8s6nMMNLUnzN4kOCDzGChgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQrkdJaKJSuizMJrvsWUcrtmjb_L-BQ_evpchdn932iMwKo4eVurKHADjktMIFeZt_2rB96Z87clEttxzTh3X84yxkaZGgNege2Rp-VCF0DBIZIebbVmOPLgJDV281xM5YJ-Rav0Bl46_p_3dV2eN1QPK7b0BqUEPqUxjJcjWMQTsSCoXzepMmMm_RS6iTl6RNF8Lb6ys4jJ32RDCryh8fLTt_SATQAUEUqV2aZr6sKT3uVGIZ5GEl8S0WBUVBwYQiebGdFVUU9lNo4u7fpV3RC74Qw0jrCk5ICoCKhmxrWsJ2o-Xd6UoQGDfgrbCsj8D3NgQPt-l6d1M0E_aN5LLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qoh_-CVBUmqt1ZHbX7G5iusclUhXcSDbiUn5IXB7cI4EXW3NWCTTpiHyPAPtLjg5Zydu88Rr6Uq2xr9L3gkjxcUKb39G2HfNM4Nn-htQi4O81ZFNXED21jk03QglSUivwKLJ117r86Tik5IbkgOJQYUh9msVhZp8NEWQhrpo9OHak5WC1OtZP24XWc0L7mxNg3r51YyatlHJb18lM5knXm26gn1iaIg-TTlulxhteLdBr9ljyGiue1d-dW5oc3q5NJQ-thtSF4mAZfcAjkLeu76AHS0xmwhC-l2qW6N8xcD5m5PQCpmyNE0N-r1ScmAJwXmKliWZyz25z91RgHSEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBPobfIhy0u0HKZqmJg_xgiNPG_AHvT55LDbCoWcKpHWe-xbo0F84dBYQZDNYUAxMXcgGkHFce4YtB4LmbVjoT1gBsflSxhhYynzNfmUl0YZSyirHJDLulCSN7KcOvGZRcfyrhHrsvXQJvq-E9Jx17YFEuzv27rQew62Ei0wcaQOEttt_N61TL14H3iPbWSIXy29iRZHBMNi2imrNzexsT_hQR5GJ_S5SKMJjA3BjegWvRTVt0rHU7qbNzFcFOZahCkJ1GkejJgzZ3T9YLGQL-IqchdPC0apHmlM47tJJxMand6OtDaNiN8QOIVGBXYm0Ogd-0L_V8Mt2ru2E2F8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkN9BB5RgbckX655L1PARK5F3rtPUjvQn-BaDaXJRDM2hJwmacwCIvwEUUFbPDD0Qv-RsyCYO_E7XyJNOKR40J_wshx-14qrlsKEMWzo_PHZjf4JCYNWQkb8LW9EWfvPMMYxBS3WxuP79cegjXuWFN8yHyC8dS8UsZXsBBjA1vq4U682qaxKXznjkyUZe1HNlWCpjvHWSmcBjQ31iD77lP6oeY8Tbw-h16k4NNMT0pWfdMxHLJ4hfgOO12_Yz2v8EssM5Qm2JEWws7aUTobr-_9y7mTrEx-bj93rS_KKZnB4sx6jPatAv7VSJyYzBEVxUAUcSoH_2JF4hM_3U1y17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AjX9qNDbl34ihdpKY70GxSshz9apYfRuXrHB_1xjz0zSJ7rvn7EbFUSzyJy8gmrVhbHeaJNiX3tPqQ8vZS72Htt0hy9gng-gQUiMOpOWdBXHrBw1KxliZANo_8knMk5mmfX812hS-nrmuXqwCz8xTpsvJqDZvSzAlM_0-5Utcb52c_gXYsMBGIF6nRT70uhprQhbhA2_aTwJ1XZRCVjlrpb0e3w5Iq7d-hbH_5yOIIQ6CcmDC_tMfUZESJmj3VuAXPNZrGbyHCT8jTKfpSErgKVf5Uazpu5ntFIMFRB8OalXvBXU92uL8iaZDUIoMqJCYkb6vX1VM-zuDRUbb5sIvoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AjX9qNDbl34ihdpKY70GxSshz9apYfRuXrHB_1xjz0zSJ7rvn7EbFUSzyJy8gmrVhbHeaJNiX3tPqQ8vZS72Htt0hy9gng-gQUiMOpOWdBXHrBw1KxliZANo_8knMk5mmfX812hS-nrmuXqwCz8xTpsvJqDZvSzAlM_0-5Utcb52c_gXYsMBGIF6nRT70uhprQhbhA2_aTwJ1XZRCVjlrpb0e3w5Iq7d-hbH_5yOIIQ6CcmDC_tMfUZESJmj3VuAXPNZrGbyHCT8jTKfpSErgKVf5Uazpu5ntFIMFRB8OalXvBXU92uL8iaZDUIoMqJCYkb6vX1VM-zuDRUbb5sIvoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUBYZRIoMQxKi-pgu7rXysSgeyyVWd5P7fzGC9kAp6TRQ_oZhaiDHSBAfX0nogEtOaIAdkDD8TpbPPpl1jXZ5L3ehSjx4hV12qq6CmrzhEEDOrykjsxET81qvE4g_GnNf_ZtAmRnBbA_5ZCDd_fepDhDV2cNrMxo30FOD-LUUptFzO9wqNmwmRmSjimFqcqT8PSITKzk1ZFbbPPAzZZhXzIeElBK48ti3rKvJOpKJ-0KhpDDUPR2iw7EJamIJoK5F4-TxCchgVeMlYRqohh9xPJyvANMZ6JfDRKQ-7uQUIQ8yvo6COFQHs5uPUwh6zsKOYnK11fUo5QlSMOJmMKf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=bQZfRlKtoNSf9oRgkxcCoQxXdDsQ0zwzd6PXGfUTrha16cQojRRsuDAsGwNoP0tl_qOhpDaaDER3VykMREyMvutJwPj6jZDiTEKbGcY6jJ0Y5325bcnUCmQ5ND5YRW3cWqN8_ykMAUQ02izEV96ibxdXwf1F_stWA5LDX9-rbR5Gv4k9-Nn3-7PiwQgicFRWjPUOifRgecvMVjS5QwLrOZf0F_y7MTnRaYuYx9Qe5mSyTX7dlXR82AKlyHIj_RzOY5Tecah4cLZziG3dU_RI5N_sANnhT7c1AYxr1eum1s9DfsCRbbxaVnB81S7rKAKng27Kem3WupqeF0pM_AZupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=bQZfRlKtoNSf9oRgkxcCoQxXdDsQ0zwzd6PXGfUTrha16cQojRRsuDAsGwNoP0tl_qOhpDaaDER3VykMREyMvutJwPj6jZDiTEKbGcY6jJ0Y5325bcnUCmQ5ND5YRW3cWqN8_ykMAUQ02izEV96ibxdXwf1F_stWA5LDX9-rbR5Gv4k9-Nn3-7PiwQgicFRWjPUOifRgecvMVjS5QwLrOZf0F_y7MTnRaYuYx9Qe5mSyTX7dlXR82AKlyHIj_RzOY5Tecah4cLZziG3dU_RI5N_sANnhT7c1AYxr1eum1s9DfsCRbbxaVnB81S7rKAKng27Kem3WupqeF0pM_AZupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=gF7yrBRqvDhApUi9ekbjRs50MzApUsu1WSSQumCJZ8YcaIx6xa4YiaXkow9OKeWHc1YhtmfWxturdRETppOxqVYwzioO-kPN_kUEotFrFKP2JHZFhdB4z53K5mAU1DCl8pdYXQ1tO1bdjMjuL92ItOtpuoKazyRXm2prsk6f3qvogjzkJ09A_VTySmSy94EnOkhH6GESHIMlMdjMY69dLH_5qlo-IsWIdKeM_8o6j8utZgFPfdhn95InuZwP3DkVUkRQA5I6rkjMmdrWSW7OR2MzPoQYqPvwvQKpnztVnBPh14g7uRarC5TPDycQND6KEldAm94EZL2Z6aTNlVQewg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=gF7yrBRqvDhApUi9ekbjRs50MzApUsu1WSSQumCJZ8YcaIx6xa4YiaXkow9OKeWHc1YhtmfWxturdRETppOxqVYwzioO-kPN_kUEotFrFKP2JHZFhdB4z53K5mAU1DCl8pdYXQ1tO1bdjMjuL92ItOtpuoKazyRXm2prsk6f3qvogjzkJ09A_VTySmSy94EnOkhH6GESHIMlMdjMY69dLH_5qlo-IsWIdKeM_8o6j8utZgFPfdhn95InuZwP3DkVUkRQA5I6rkjMmdrWSW7OR2MzPoQYqPvwvQKpnztVnBPh14g7uRarC5TPDycQND6KEldAm94EZL2Z6aTNlVQewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=pK1Kgs30iHEQN6ziiPoyHKdaT38E1eAyWZjqyyJ96AtsmW-5MYjhoFaHIxLEYIs_5GEK4I4MeaFuC3oOw1bvC-lCuo6Ogf6jXKN_lq5YPqx4rcg3OiuzeKVPkKyiO1yxp-17JmLnGurgUC8c_BVH1JJmfrjA6rzPgn3nN5mDpM6jg4woOMhlok6TvLanHywjeiTKCKwP0OcDNZ0muqefgsmXQIy0eiWKpN95iMZLrhoRvZccSXJEkuJptb0haKC6-Tum84kAnDfE9dRfT_4F_qNxKf8fDeDqvyH-Pv5gFlKBr1dxKuDD_z2cMjq1427Nth4_lOwPUMqpCoeukqIm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=pK1Kgs30iHEQN6ziiPoyHKdaT38E1eAyWZjqyyJ96AtsmW-5MYjhoFaHIxLEYIs_5GEK4I4MeaFuC3oOw1bvC-lCuo6Ogf6jXKN_lq5YPqx4rcg3OiuzeKVPkKyiO1yxp-17JmLnGurgUC8c_BVH1JJmfrjA6rzPgn3nN5mDpM6jg4woOMhlok6TvLanHywjeiTKCKwP0OcDNZ0muqefgsmXQIy0eiWKpN95iMZLrhoRvZccSXJEkuJptb0haKC6-Tum84kAnDfE9dRfT_4F_qNxKf8fDeDqvyH-Pv5gFlKBr1dxKuDD_z2cMjq1427Nth4_lOwPUMqpCoeukqIm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNBqBUpNbFK6KqDmDUnEvdLlEwSkDMnHL0u-hN1jU6oR0PQlqi-2zgDKE9CDQm_9_9plo5sX1ka3fRgOQeB8RjeK0JzX7r_T5HUuXYZSHZgv_UXQmt-vcpbCLKfwL3AFXJESRAT4rwYel1sT4kv5nFqY7gqpqSiKDyAJJNJ-Q_-Zd4UYH1F2giL-fcLGA9NwflcjbG1DYs6IQW3xhuDYINm65qzrknAhWNG2nTvGfIsF5qB4KBicXqcFvoHjwoGvRrS7Un8jaBdQi5c-Uf8nJy2HiSYepCAyWRIfgEdJfHEM6SOqAUz8rdFiTJB0OkNWqv8neDMP7g9eXRCbTqIwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Cw7jqX23ksbSpKfic6UeXP4JbCuX78mQajcsd5zU6hbzNf204Q93nasA6YtQWDpcS3iloFpW3EGtZr0WMFjFRownczxZZ8LMSKG5iFziOeUWNifskK56UdO0xYkIjH6UHMGp16HQd_1SyUr7ALpBN4tdcFq5vlwzuZ6hhRIZcGzGpS9Ym55yp4h6Tg_VGQ-E9O3f1dxsToeyxMH6p0x1hY7WPHoYAPRLyCsaRpowjUowS8TQZuQTRYfouQ_qkIqrgbiqII5qS4YGYl50JFMr2jXn9SmvNfzDkRFF_YUIK-KBtd3Sj4Z53BEiIRqc854Zg9PbYzBDlfpFt7A-ylsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=FLl1XytK2_t4KdwUv6ccnRaSuThDY8Bk5KoA0QlKYv5hwE76hqjcm-GvYYfNYmlOkO5xYPdVe81dG3zLQH5NgQAKUwwf2lo2xN9ixhQJiJGNWTQ0_Ye_v8w8Uu0zj-thF0cSfZieMqwcd_GMjEwNL1Ymgk4K9iBcSntzXUMnlWzKeuyoXj8RKOxMS9ri6Wv_sT4GHhABZtWGZcrbpbngNuLfiR466rqJurRnPg3AAKcjc2Jv_aYGTnzo6kPiBlU5n5rZ_6PkHv1y6m2lxufSvp_vrIp0As-eO-v0UFEMrtlhza5E6vKhVU_KNtRtU8CHNbltmleqmJ3x040VOnQa8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=FLl1XytK2_t4KdwUv6ccnRaSuThDY8Bk5KoA0QlKYv5hwE76hqjcm-GvYYfNYmlOkO5xYPdVe81dG3zLQH5NgQAKUwwf2lo2xN9ixhQJiJGNWTQ0_Ye_v8w8Uu0zj-thF0cSfZieMqwcd_GMjEwNL1Ymgk4K9iBcSntzXUMnlWzKeuyoXj8RKOxMS9ri6Wv_sT4GHhABZtWGZcrbpbngNuLfiR466rqJurRnPg3AAKcjc2Jv_aYGTnzo6kPiBlU5n5rZ_6PkHv1y6m2lxufSvp_vrIp0As-eO-v0UFEMrtlhza5E6vKhVU_KNtRtU8CHNbltmleqmJ3x040VOnQa8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GawnvbIZ2_E9De3dDFbmFXRojWUPYG69_qzTYiAoDf8fvylyr8lEXitsJxi7_b-r_MxintInDlNrA1UxEUjSczGBOoe6oF0iFFway3Qh6DnVXKbUrHKE5ASTEU89VeXQtqTfMii95-2bf3AxyIHnUZ1P_nYilRXM2eehhBYY82nsy_ndT1jihS3V_Of2_XIC8fnFU5hWKIgx3Is4aWfJbxnJfEOZ8bY04mwcMsInfEwl3-s6NGc0XIkGyzgflSKGLd9wE6jwq97lFsbhjdiVVQG56GdGTIxj86kKyXf7uzDXLGMTS4Rq7TYEQlmqBuQ-__m28-z5uFid4u5NBBoFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjfA3kMbWMlqMCujt-tAJBDQFlpSHiHce--IY1pRKxHEmJw6zwXtjaLr-jWJUbX1b_gOfAHDOprLJjKO_t9NcjcYjELXx2zrOYMzofm1bBpyZWsan-Z_PAXja1831WBjDzicQEc2_aDoj6w-zkUU0_50h5BAwUk9lS_vezwRtV4JjYiFUwpJ8w20yoJ5nKD_oPno0cGLaqc1MPI8WLJMOviTRggg1lQNzy48NQER-WIt-3qF91PJ-fkCLevJAs5Qh7abQ0mQ9szEwBN2nK1i9D1F2osmtoQrysdHCl2aMzMCnanHwKdUpgPdOjuxSWEx9LmDFnuVf1cVifKsl9TCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvzMnnpwSBgKjuMfLexufPSe3oXRHOEL4IRcA5CXZau985p4Nz4PcLrdwd2GTHOOaLIiKXQPAcM6O5YtWlaS1khNKS3fEbcFCza8xL9rMHmb7zdGtb9Q9ukRFYjMwwUCmD-kG0EDEeqxW_luklXijq_e8HQky8BYbWu0kZi3PedR3CH2RtOc-Fv5Dg0NZ-NMGDjYGDzv1pFVdKq7Bk4PCTiIHjknuusr-vyt_2V-7K4dTnCcpjgJOb39yquB_lZ_bUVviweF5PPnGW3zAhdZvoCrupeImyDsJDZIOEni2lv-VoDeCCtQsViK2p2ZL9lByrAo6G0Y8q1V_eR9Vw3j4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8JsTseThPAtURBKJDJKxi-XacfltlFRE_UlpWNCfOhrsYFazVxerzZWau7BBe031nZ2yE_0WdxyhPXltq0yjgSz_9s8qMppAoNNRtDmiXo3AxwZhRNniAhWbYQMtJrXjzqXNXgoGj454KVaYTy9j1Hvu48HJZ9CNVYFY2kOBNgDTt-lqFbYuws-2yWlGc2BtcJwvhF5-D2S7ZFXU8bLuzOdZZQE03l3BWlDeYMd8VrNvyxg5qt127DszwNz1cSA-aTbaZ0xGUud8Oj5kwy-Yz4YnOzGhQ4sEHzMpGP9N5jgQs83Ub1LpTqJTM6TBNRDMb0wJCSLdxrJu1Nz73VsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=Khe8sGFRi-SDNzHQSheMbu_xGjYahVte6plsNZIQo8Dq3PyIxhrkzslMJkDYHI5SBlpFKP5cgyb2FwLKOV635GgymH1sYqHB68oBtlJC5HtpXyOpXF1XIUsLc55Kx-ZjSY7xrGZR19rDsPx6Vfi81HJZkSaZqwepI6QY_T_zdMe0FKBJInRYYyjzKXpPYbZJdZViSnwfhNLNUB8BkK1fwfdMlO969A0tjZymaT2Rnnhfr-FwoB5fIt1xM9IdDhrd1RHj1A4tKtRvfpKiPrf7pPSxMKH9VYkijf0uR9dWv9TlBikEKSTK-XIAfz2DZz-ykQU3Dk271mjnlsj-4MtRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=Khe8sGFRi-SDNzHQSheMbu_xGjYahVte6plsNZIQo8Dq3PyIxhrkzslMJkDYHI5SBlpFKP5cgyb2FwLKOV635GgymH1sYqHB68oBtlJC5HtpXyOpXF1XIUsLc55Kx-ZjSY7xrGZR19rDsPx6Vfi81HJZkSaZqwepI6QY_T_zdMe0FKBJInRYYyjzKXpPYbZJdZViSnwfhNLNUB8BkK1fwfdMlO969A0tjZymaT2Rnnhfr-FwoB5fIt1xM9IdDhrd1RHj1A4tKtRvfpKiPrf7pPSxMKH9VYkijf0uR9dWv9TlBikEKSTK-XIAfz2DZz-ykQU3Dk271mjnlsj-4MtRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWPV8CcOoOTn0uFuOoHPq5moYiEGy0ffhrfDnYekR336BBgIXgIb7dQlhI6TTjMnJbb2A7dkQnoT0iLOKecn49zlQEM7_Q-ve2S2P5xJkb2V9K_PbMvFMKmDakfq8k4UEUTHba4d_EkZz9LeFG5QtSMN_SEZC9FRke2vT277mPouzlpKJV8tNYgD7fXktyLyBc_OYuUXhm-HnIfaTVAuXGT3ZSwDO2LuljuQ5Z_XstT42uvsZO8DNdULTRSnTBL2sesm6zjI8vH-G7gMCMQ6chmL0WBopDk7UU2hL4dcGAwCyJ3KLwEcr4h9OWgcgQOdDfykZGRvoU9NHM9H56-sqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=mbH3SHDmpxafepI0pyF6y6kNKQMElf5_gjB1ErNw8WCoNI0Rl474mqyZA9gb8vfiCGBeC55dgJswov2xg7H6SY5rgRNsMluGVGeI4Hlj5pGigGiwIp3AWnY3X7zvedyPMXjibiKOuLgurLLtj4BghPeiYXdIWFT0iqEN74zgvVlbmy2Of7xMXKHdQwssh8WU0_I0suZsih7owbTgGtulR8VY7_wvU0oFPpItSlc_cicb4BqCu57uzQeyw1svlwSo0AZ7rKU6EunacGUH6advRFOTVNANthHBgEd1r3MmSvE8GOccGYnAFaL6iUbNf5IAim-R-xXNM5xpQ_2HSS85CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=mbH3SHDmpxafepI0pyF6y6kNKQMElf5_gjB1ErNw8WCoNI0Rl474mqyZA9gb8vfiCGBeC55dgJswov2xg7H6SY5rgRNsMluGVGeI4Hlj5pGigGiwIp3AWnY3X7zvedyPMXjibiKOuLgurLLtj4BghPeiYXdIWFT0iqEN74zgvVlbmy2Of7xMXKHdQwssh8WU0_I0suZsih7owbTgGtulR8VY7_wvU0oFPpItSlc_cicb4BqCu57uzQeyw1svlwSo0AZ7rKU6EunacGUH6advRFOTVNANthHBgEd1r3MmSvE8GOccGYnAFaL6iUbNf5IAim-R-xXNM5xpQ_2HSS85CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=QVnujGTGAfQWGKXxLDI0NuXqrz2jdea3Ipx0NeIqz0eCZbJWWPZ50L6bCflbInwYXolNfa22n_agErDCmcy9ffI_GgIuX7pHXx2r6ve4GjtnC_6NudYA8ZZrRIT7FALC6ej_keM2Fb6AdosxjGbdPeXo8mqUd1TjbdAWYdU8vRWMIq_WQO_R8vGutdEDPt3oICssWxpQ7d4UmWSEWgEomJgOk0kF6IIrjLN1gr6DBnHatA1ZOPI9MmPRMeoAYSqKnHA6rBkQ_nfTjk2nljrsvzrAiDqZmRwKmEvZ2RDXUXah17zPucZ_3OUpTY8kux9CIoaMn50LX4-nGWSlVpk7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=QVnujGTGAfQWGKXxLDI0NuXqrz2jdea3Ipx0NeIqz0eCZbJWWPZ50L6bCflbInwYXolNfa22n_agErDCmcy9ffI_GgIuX7pHXx2r6ve4GjtnC_6NudYA8ZZrRIT7FALC6ej_keM2Fb6AdosxjGbdPeXo8mqUd1TjbdAWYdU8vRWMIq_WQO_R8vGutdEDPt3oICssWxpQ7d4UmWSEWgEomJgOk0kF6IIrjLN1gr6DBnHatA1ZOPI9MmPRMeoAYSqKnHA6rBkQ_nfTjk2nljrsvzrAiDqZmRwKmEvZ2RDXUXah17zPucZ_3OUpTY8kux9CIoaMn50LX4-nGWSlVpk7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=GWfsnDy1eJAnXe0jRdpI5fBUuQDbUe5cuo0fsRAUJg9tu-079RjtBeAkmd2OlMSDyShhf9diTJ-iWmzBM9mSJl41JcRwKraFUlkXyzS2yWxqbXvFaQxPt3ui9ErH8yKctp9MHqYYLjYZ_98gPHv_hRHy0O6kqlUNrCqUU7FZFB9pStiPDEFUhPuIZZWLzt2ABeo94CirufxcZMiLbTd2yNhYN2dd9Fh8jdBvR_2d9PF8iVYX6uD57t8m_TTdOJzNeHzw8Pm5vzJFQG1ED4pQ-9huIyRtsuid0f8pteXGXgdEsTd2a-FVPP9DHLyMiZqRA40lM_pRg4rgFzwpR2hoMGxD23Z9debB9Ah95KeC6GALx3yHWy7YsEsdSU_iyh2SqXwAs3_gCaTcbuJj-b6OGZL6fERC-TB4Vl9U3NmmVLvSwvUnXNTU_mh-iKnwGH4s3C96L33F7UFhg4IH1nocUPvSYEKkteMHtx5hyCUVSp5YzvEOQghGNa3syqBjRhvuRJT9u5_D4zuqFZyPgrDYf5gNiKcdKOLrzu1itpWKLvh_N1V610sTzHYKXNBvskkLSaDouvqhJoDcirJkc9VFR-L5g-V1yD0tpeKKm9JO9DZdV3i190Mk7B3KQvCBR99GAxdQnF6r3QAyAztcEV521B6-fCy-t0DvEQyUdDPxiHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=GWfsnDy1eJAnXe0jRdpI5fBUuQDbUe5cuo0fsRAUJg9tu-079RjtBeAkmd2OlMSDyShhf9diTJ-iWmzBM9mSJl41JcRwKraFUlkXyzS2yWxqbXvFaQxPt3ui9ErH8yKctp9MHqYYLjYZ_98gPHv_hRHy0O6kqlUNrCqUU7FZFB9pStiPDEFUhPuIZZWLzt2ABeo94CirufxcZMiLbTd2yNhYN2dd9Fh8jdBvR_2d9PF8iVYX6uD57t8m_TTdOJzNeHzw8Pm5vzJFQG1ED4pQ-9huIyRtsuid0f8pteXGXgdEsTd2a-FVPP9DHLyMiZqRA40lM_pRg4rgFzwpR2hoMGxD23Z9debB9Ah95KeC6GALx3yHWy7YsEsdSU_iyh2SqXwAs3_gCaTcbuJj-b6OGZL6fERC-TB4Vl9U3NmmVLvSwvUnXNTU_mh-iKnwGH4s3C96L33F7UFhg4IH1nocUPvSYEKkteMHtx5hyCUVSp5YzvEOQghGNa3syqBjRhvuRJT9u5_D4zuqFZyPgrDYf5gNiKcdKOLrzu1itpWKLvh_N1V610sTzHYKXNBvskkLSaDouvqhJoDcirJkc9VFR-L5g-V1yD0tpeKKm9JO9DZdV3i190Mk7B3KQvCBR99GAxdQnF6r3QAyAztcEV521B6-fCy-t0DvEQyUdDPxiHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWR4lDW1oX8fwPuG34jA7a0SVHAoH8EjPjuMECnETkR-N_qWjImU3OiN6v3fe4poA3uLyMRHUO98nVKu0-6fjVUodbkyHXv8g1_AnAqcNlMr3TTD2sCAGU5SjNfd13WBGX1n96ypnMlBTbH7ru0YbwD2kVutacoY39bcqreyx7qiOU6kYv8XYtJ2cmptlfy-G-qLUvJ1Vemn7ck6QUccOovxiyRSOrBfMzzh2LmpYGtrfF_0W_GKn0pT7ItTOaxkFZ2fDKelHuSw8YRipiRatPRhaPo23sLfipi-85sn-eXdmAu92B0SYbal8tF5H9pfWPSGEYJe5ieGsv4nUZFNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=OcDZVgkVpWEWhuzwWLk4XmRjO_-zHmt4yMz5x1AvBTpoqdMEPYr6VkUyIE2ixcoauVVsHb4Np2JME2GRnKQpKgOYpqK8D3fQu0rC8oNCxWFLobIh4YG8iB9dl_JFGONnsDBAyaCKroKLy1l1-Ak21BlZifGgJxtuv0qTGQQk0RgO9MleKrhlRd2tf4bJ62yspOxISeK-9BQ_f2XIkMqLj0t9xNLfbIeLJ9WBcZ1iDtoxbAzRGIr4WPQ04AFn5hanYzc0q5LnoKg1lHwdQetB1dezK0BKyGAV52VlsHCmxnXUZNrQswx_J7RNrgLIaKC9m_xnxldHf6qQv-EAyL7z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=OcDZVgkVpWEWhuzwWLk4XmRjO_-zHmt4yMz5x1AvBTpoqdMEPYr6VkUyIE2ixcoauVVsHb4Np2JME2GRnKQpKgOYpqK8D3fQu0rC8oNCxWFLobIh4YG8iB9dl_JFGONnsDBAyaCKroKLy1l1-Ak21BlZifGgJxtuv0qTGQQk0RgO9MleKrhlRd2tf4bJ62yspOxISeK-9BQ_f2XIkMqLj0t9xNLfbIeLJ9WBcZ1iDtoxbAzRGIr4WPQ04AFn5hanYzc0q5LnoKg1lHwdQetB1dezK0BKyGAV52VlsHCmxnXUZNrQswx_J7RNrgLIaKC9m_xnxldHf6qQv-EAyL7z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
