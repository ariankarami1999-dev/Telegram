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
<img src="https://cdn4.telesco.pe/file/e6jl1dYsBZ9azK4PTMlG0qUNCGQ0njZ7HlM0oKxDhUrMXUwMpt50G8-4V5QwQ2UFpHcd2Gvpgw9E1-gMcman9ooMshQQumGURn1educ4WY4HuCGOOXd8YDpDBs1mNcznSCAQUw7WyUrc8B-RM7zHtBZEaLYFKnAVOLymFU26MD-fSQXV22aFwzCsWRz1xeFK1DmSV-9uT3owYeHUfQwM5iIwKSyghDSFM56Iwxnu6AmgV5kfLR0jm95-WyOKR9OVW3QqRQlzCrEIC_Dqaej5HOCpgvwk-PneUKFDXPFl00_dFWq2lzaHYSPxBM7rdS7IyQ9ih48DqJApWvYy3XO_eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-126962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c5dfe9eb.mp4?token=rBtBszQGDyZnFcXMJO_I_rCNzcdiyeQZSYsqSzBjMx7FToBGBZbUI51T1Cbc2LYEzBG7qgZVZhqi7naEA85VP7GYq0yYRWLRyHZ9RNU-Z1dJF2J3uV49uN2jGEGIFr6i6ozPZbsdf0mc6WrUHKtH1XI4rnNtvpCwpqeJtCBoPSGrVoMyTq9lKUFoiPBPTXVWWj9h03n5hq2T9WuEM0-TD5TXRWYWufHciAZAls1GQ9mRL_cX0skYmTA7tfTXjewLaEUoO506QXRFYEoza322GSWYihW7tUg88D4O80-1Cr_nKn7YWVEhVDxKyZZidTJw5GJK5wVWKXQ1RdODdb0Pkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c5dfe9eb.mp4?token=rBtBszQGDyZnFcXMJO_I_rCNzcdiyeQZSYsqSzBjMx7FToBGBZbUI51T1Cbc2LYEzBG7qgZVZhqi7naEA85VP7GYq0yYRWLRyHZ9RNU-Z1dJF2J3uV49uN2jGEGIFr6i6ozPZbsdf0mc6WrUHKtH1XI4rnNtvpCwpqeJtCBoPSGrVoMyTq9lKUFoiPBPTXVWWj9h03n5hq2T9WuEM0-TD5TXRWYWufHciAZAls1GQ9mRL_cX0skYmTA7tfTXjewLaEUoO506QXRFYEoza322GSWYihW7tUg88D4O80-1Cr_nKn7YWVEhVDxKyZZidTJw5GJK5wVWKXQ1RdODdb0Pkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ پیت هگست:
همانطور که رئیس‌جمهور ترامپ امروز گفت، آنها معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار را بسیار خوب انجام می‌دهد، بهتر از هر کس دیگری در جهان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/126962" target="_blank">📅 23:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/126961" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رئیس جمهور صربستان: من رئیس‌جمهور کشوری هستم که یکی از معدود کشورهای اروپا است که در همکاری و همکاری با اسرائیل تردید ندارد و به طور علنی و آشکار به این موضوع افتخار می‌کند و آن را پنهان نمی‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/126960" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گوترش: وضعیت کنونی در خاورمیانه می‌تواند به از سرگیری کامل درگیری‌ها منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/126959" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / استرالیا و کانادا از همه شهروندان خود در ایران خواسته‌اند فوراً کشور را ترک کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/126958" target="_blank">📅 23:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر ارتباطات از پیامرسان سروش پلاس تمجید و تقدیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/126957" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
🔴
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
🔴
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
🔴
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/126955" target="_blank">📅 23:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab968080c.mp4?token=g0Kl52zWfxevHShb7J8vBdxVHvk6mRn5w5Ws9XZlTfZxBuz2Wdo_z_qgQakuMuWxgDUSu3sMYNBeX7wVP2leHIbUQEU4g8A6LMMfNYrhyfFOaPmoo1XZnODErDI03hLFara4WuGnfcBnlhKHdlOfwt6-r0YFmiXiISitWndstJPlEb07cvX8kedtcZDdnTYDeFpcQCigpufWRrqvj5GthXMH0sQrIgo8HPrB93sy2rK32uMs-zHs4IlPOOEEvdTxBl-jen0U99Ny6A4qFHfa6TQa-rAlvBjRognlrDYqtW6P8k-SO78t35s61DifqFscDkilDeJkb5-4mvP8Is68Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab968080c.mp4?token=g0Kl52zWfxevHShb7J8vBdxVHvk6mRn5w5Ws9XZlTfZxBuz2Wdo_z_qgQakuMuWxgDUSu3sMYNBeX7wVP2leHIbUQEU4g8A6LMMfNYrhyfFOaPmoo1XZnODErDI03hLFara4WuGnfcBnlhKHdlOfwt6-r0YFmiXiISitWndstJPlEb07cvX8kedtcZDdnTYDeFpcQCigpufWRrqvj5GthXMH0sQrIgo8HPrB93sy2rK32uMs-zHs4IlPOOEEvdTxBl-jen0U99Ny6A4qFHfa6TQa-rAlvBjRognlrDYqtW6P8k-SO78t35s61DifqFscDkilDeJkb5-4mvP8Is68Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همسر یکی از شهدای ناو دنا: ما منتظر انتقام از آمریکاهستیم
/
پزشکیان: انتقام که‌فقط جنگیدن نیست انتقام ساختن ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/126954" target="_blank">📅 23:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E791F_mC-k-CuZAqYaVyzEr9vCSSmXTBp_X0idQaIiOdZJaaaVcw-DhRyRSgEIV1quBoJPkeVkNVY0M5d9LfvuG6CJwFD6zkI2jsgdFLaYHjyeDA-jWo2cWPMEZ7GqrmB4KT2HvPiw_bNlI7xpvOa9vVIcSoDcp1LySrEbQVd_WGddJFDQgSmau0l56imAViR4loIyyrtFx40ACVGpzC0Wk36xch2tgVGorTDZiRpdaoBPVBq0Sy4O0SeEZDmSE-VcBNpcJ4TPHoC_t48APOwQTvwwqQT2-GosH9USdRF3NmkrmTW64ffpF8EUluoDL9DhQYyASPcm6TIN3KIBo1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/126953" target="_blank">📅 23:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4eb4813c.mp4?token=XMg3WzqvsCx1OKCV3dq1i0riByhT6MZnnxte8DN2zwpPWibNZzEaROfYSn6WRkB2Jwe6n8szM1acq9nRastZuG-OwbU-86UhnCq-VyuAUGdIxwDooabS4YBsFoUFhpIrrdRSRwu6Pdk3SAUyKxYGJSrKj2cmrkLfZkks9VKqoLlrXcOzaplWdBNYgmLfcjtIXxjAPyzqZTeUjqk7Ba57KUe-0nFGdfnN8-USiIOclkBA-FjbYzi8qkOlX8oI8XXu1agoEMvmfPCMqkFJThwRQ1g0NezF8cNXQIGjyE47h8CT2V2MWZEl64JUqkyPJpNRFGM40hT0K2pM0Pg3fJNOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4eb4813c.mp4?token=XMg3WzqvsCx1OKCV3dq1i0riByhT6MZnnxte8DN2zwpPWibNZzEaROfYSn6WRkB2Jwe6n8szM1acq9nRastZuG-OwbU-86UhnCq-VyuAUGdIxwDooabS4YBsFoUFhpIrrdRSRwu6Pdk3SAUyKxYGJSrKj2cmrkLfZkks9VKqoLlrXcOzaplWdBNYgmLfcjtIXxjAPyzqZTeUjqk7Ba57KUe-0nFGdfnN8-USiIOclkBA-FjbYzi8qkOlX8oI8XXu1agoEMvmfPCMqkFJThwRQ1g0NezF8cNXQIGjyE47h8CT2V2MWZEl64JUqkyPJpNRFGM40hT0K2pM0Pg3fJNOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گدایی کنید تا فروشنده خوبی بشید :||||
دارن آموزش گدایی کردن میدن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126952" target="_blank">📅 23:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126950" target="_blank">📅 23:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/126949" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسایی: این عنو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126948" target="_blank">📅 23:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126947">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
باراک راوید: ممکنه مذاکرات ظرف ۲ تا ۳ ساعت آینده به فروپاشی کامل برسه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126947" target="_blank">📅 22:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
جنگ قطعی هست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/126946" target="_blank">📅 22:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
جنگ قطعی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126945" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urm_HTUT1-wRDIOeNIEdCtTFVwjhCEnGwBnDbyMk4aOynY2QnacAQbYfcmeobeoa4OvRG8EZb8Eq24XHB-fKy1PODHdcq4dGOMo9ZyyQziDF7HcckJzXwISrKyUaxNRq-vP6Wnh_d1jBuE--QN4GfkVT71FIF0Hdsbq8EffW-EsZqlSp9t-W43v3cyZD9PKtyluaDlNGOGmARO5iCC1awc-FEcJbT5MuRsoNBuiJ_WZA2-IZDtg1KH9FBfC2r2ck-NA0kindYTfYn_k4rNC8X3MzPCb2w_hSIAsjphPynR9jjyNX3bcVL3YOwC7oUWAJRFIXGs8lrkMtM6D-udBLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی: در جنگ چهل‌روزه وسعت آب‌های سرزمینی ایران افزایش یافت؛ در جنگ بعدی شاید وسعت خاک ایران افزایش یابد!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/126944" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcuVmA-zOayZUy1kD12EApkiIsbJbFDf2AcVdyb4Xvf-l5oJuMMVHwnTAbFGnEBIhFRAn7H0wmrK2GNgnF6RtFAKcRuJ6eQR2D3ZrVno5WSRY_G8EPVBVMNqyb4oB_RtaDJOpQR-BrvEWIYv2aQ0hxYu0La8SiUEnUD1wMJg_Ye1sUDQ3j97Cuot0LcnoY9js7npMi1Qr5i92NbMD4wIU6h2IGkpI7GNR25CPdcIxpdxZk25ajuL9wIXJ1IyiByv-gJ6JZ5Eo6nDul0tvEO_FdiuDqBxXS2XBacnZXhx85zvjfNgea66IM95lQ4dY_-OJujdiOb6NBRdCRk7fUbZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربى: اشتباه در برنامه فلايت رادار، این هواپيما يک فروند هوایپمای P_8 آمریکایی است و در حال پرواز به سمت قطر می باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/126943" target="_blank">📅 22:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ادعای یک دیپلمات لبنانی: نتانیاهو جنگ لبنان را تا انتخابات اسرائیل ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/126942" target="_blank">📅 22:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTe4lLo_sGbhLR6CZ2oclFDAU6m_FVCRRUPzauzuEPTshhtOtccT6f9ymbshjynz64O87iOIjm9-xSBWEhdGd79AEsKG5_4r0_l86TIYPJVD4wLgqCjgadRPkuiu9ypOJs1yOKBacEd3UpWZ70Ann8-ePOoWkiXI1-iX6N8TIM7UB-UF5k0WU9DvbQ07PA8kqrabNs7jWyBDKhylmKAxILqTQ1apkB6ZEr6QQiyVKGno27NfCLz8AMGxzczoHDkFkXoIE2sfV3XRCm5ZmSbLWS436aDaxQeI6ZwR5lsW1sE2Ga0gzUg93I0pWwAx83m3irbdQf9RDnPN64YwhVY6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35fd33820f.mp4?token=DRSaBIncLwi4Kq-9r2CCxsz9mg8bq1I6xZ1Ut8Ev3_rEnydvySfjlojKcAlz6eT8Fqr2FJtp-pc7In31sxT5wz4THMsFYokBrBnVxuHzAM4N1ZSdM2gOWC23uvSOZjOfmC-izsZNwkR_AzFJrMP62C9LqfiY9AQWAUW18D6cqfAzbHJ06hbwBrn7b22SAoMYFzwFn6idxBav3hROALYftynl_X1abL8r0nQwdpUgP1YTCEPpGCvsEpmt0vZy3LFBBrsxayvi7Lp4T-i3QUQqnUQnveTomFCq5ZbeZoRCOaMxGDbstLMxAZC1KL2GlqkFG3I2OhA7PI_WXsIPLftMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35fd33820f.mp4?token=DRSaBIncLwi4Kq-9r2CCxsz9mg8bq1I6xZ1Ut8Ev3_rEnydvySfjlojKcAlz6eT8Fqr2FJtp-pc7In31sxT5wz4THMsFYokBrBnVxuHzAM4N1ZSdM2gOWC23uvSOZjOfmC-izsZNwkR_AzFJrMP62C9LqfiY9AQWAUW18D6cqfAzbHJ06hbwBrn7b22SAoMYFzwFn6idxBav3hROALYftynl_X1abL8r0nQwdpUgP1YTCEPpGCvsEpmt0vZy3LFBBrsxayvi7Lp4T-i3QUQqnUQnveTomFCq5ZbeZoRCOaMxGDbstLMxAZC1KL2GlqkFG3I2OhA7PI_WXsIPLftMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لُبنان، منطقه صور؛ امشب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/126939" target="_blank">📅 22:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126935">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی: آتش‌سوزی انبار فرش در خیابان ری تهران مهار شد
🔴
نیروهای آتش‌نشانی پایتخت در حال لکه‌گیری در محل حریق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126935" target="_blank">📅 22:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126934">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/126934" target="_blank">📅 22:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس ایران: این بار، جنگ محدود به منطقه نخواهد بود، خواهیم دید چه اتفاقی می‌افتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126933" target="_blank">📅 22:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126932">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آکسیوس: ایرانی‌ها جلسه سه‌جانبه با آمریکا و قطر رو رد کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126932" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126931">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmHq_oKyqwkiEADcCRLQA-fzGEjgC5EkFdAP8XnaghQDesIUQ-rvEj1sCOEWpP1FxzoF0rpdJfnKlaNUkxS2hlQMM8do6IDrY1kmFmPjmx8UqL08mePNhXCnUzfM57K46wz3lyaoUNDhIBHqMVBLbsqwE-QscT0fNciQ4gJh9-eCKrRrbgbgBQGR_XiZ2dFloxqotM_PvXBbhzLGMT0dRko5DNucMrlIl_dtD2c5GN2AZYk2_bCVcldI0sYno36QRjIVkKbBc9Ob3BcePEwy0Iku4rtu7Qdj6jkpM2c9ntfzKgH-gY8sjggc7N0jJ38kiyvxCwaIXp8paTiohwcuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد خیابانی پس از ۳۶ سال از صداسیما خدافظی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/126931" target="_blank">📅 21:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126930">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ادعای عبدالخالق عبدالله مشاور سابق بن زاید: امارات در حال هموار کردن راه برای کاهش تنش با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126930" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هم اکنون ، فعالیت جنگنده، شرق عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126929" target="_blank">📅 21:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تصاویری از شعله‌های وحشتناک حریق قیام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126928" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126927">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فروند هواپیمای سوخت‌رسان هوایی KC-135R و KC-46A نیروی هوایی آمریکا در حال حاضر بر فراز منطقه خلیج فارس و اسرائیل در پرواز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126927" target="_blank">📅 21:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / صدای شدید جنگنده در آسمان خرم آباد(لرستان)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126926" target="_blank">📅 21:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع خود:
محرک حملات دیشب ترامپ به ایران، سرنگونی یک بالگرد آمریکایی بود، اما در پشت پرده، ترامپ در طول تقریباً دو هفته انتظار برای پاسخ ایران به آخرین پیشنهادش که هنوز هم نرسیده بود، به‌شدت کلافه و عصبانی شده بود.
🔴
یک مقام ارشد آمریکایی به اکسیوس گفت که حملات شامگاه سه‌شنبه با هدف بازگرداندن بخشی از اهرم فشار طراحی شد، اما چنان حساب‌شده بود که کسی کشته نشود و احتمال توافق از بین نرود
🔴
حدود ساعت ۵ بعدازظهر به وقت شرق آمریکا روز سه‌شنبه، وقتی جنگنده‌های آمریکایی در مسیر بودند، کاخ سفید پیام‌هایی به ایرانی‌ها فرستاد که فقط تأسیسات نظامی را هدف قرار خواهند داد.
🔴
یک مقام آمریکایی گفت: «ما به ایرانی‌ها گفتیم اگر خلبانان کشته می‌شدند، امروز در شرایط کاملاً متفاوتی بودیم
🔴
ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت.
🔴
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها ارسال کند.
🔴
درخواست‌های ترامپ این بود که ایران ظرف ۶۰ روز با کاهش غنای اورانیوم غنی‌شده خود موافقت کند و متعهد شود از هیچ کشتی‌ای که از تنگه عبور می‌کند عوارض نگیرد
🔴
در مقابل، ترامپ آماده بود موافقت کند که کاهش غنا در خاک ایران، تحت نظارت آژانس بین‌المللی انرژی اتمی انجام شود که امتیاز قابل توجهی محسوب می‌شود، با توجه به اینکه قبلاً اصرار داشت اورانیوم به خارج از کشور منتقل شود
🔴
به گفته یک منبع منطقه‌ای درگیر در میانجی‌گری و یک مقام آمریکایی، عباس عراقچی، وزیر خارجه ایران، به میانجی‌ها و آمریکا گفت برای گرفتن پاسخ به چهار یا پنج روز زمان نیاز دارد.
🔴
این زمان به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد، که در طی آن ترامپ به دلیل پوشش منفی و حتی تمسخرآمیز رسانه‌ها درباره وعده‌های برآورده‌نشده‌اش برای توافق، و همچنین انتقادهای جنگ‌طلبانی که می‌گفتند در قبال ایران نرم شده، به‌شدت کلافه می‌شد
🔴
به گفته یک منبع منطقه‌ای، مقامات ایرانی و آمریکایی طی دو روز گذشته به طور موازی با میانجی‌های قطری در دوحه گفت‌وگو کرده‌اند.
🔴
قطری‌ها سعی کردند یک دیدار سه‌جانبه ترتیب دهند تا مستقیماً درباره شکاف‌های باقی‌مانده مذاکره کنند، اما ایرانی‌ها نپذیرفتند.
🔴
میانجی‌های قطری روز چهارشنبه به تهران سفر کردند تا با عراقچی و سایر مقامات ایرانی دیدار کرده و تلاش کنند مذاکرات را دوباره به جریان بیندازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126925" target="_blank">📅 21:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هم اکنون وزیر جنگ آمریکا در حال حرکت فوری به سمت ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام در فلوریدا می‌باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126924" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/وزیر جنگ اسرائیل: کارزار علیه ایران تمام نشده است و ما آماده از سرگیری درگیری ها هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126923" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ به سازمان رادیو و تلویزیون اسرائیل: جنگ با ایران به طور ممتاز پیش می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126922" target="_blank">📅 21:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGZjCBja0aiqOwKWDRHWxjHF6A_J8-LCZLXBioG6AsP0H_irYShURw_ig3hkKa9LeeEhg6OJ4oAK_qVTBv8yTXrPKDzgYI4ubtY5-R96_EmfxP4hOQvkooyO9MSgBGUWSUkOKc4fjOQvX7R8xq1pW_euGpFIf5HPwhfV4UXqGVyiF8xnYsmgfYztb-7MMEUP-neF7LF7qiiXY5wrPrvRUt6WOFbaWA_Fr9gPtSsGyfrpQujq35Q2g8O445H09bkV7yDF0q6WBOhV80Sfw3YboB0ckoinfYJ3L4CDhhnE2CEwBTyYwXQQ3WZ8ELGBgBBef8NK9iIzRbeDt5ZlPKwD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ماه گذشته به ارتش بزرگ ایالات متحده دستور دادم یه مأموریت محرمانه برای حمایت از نفتکش‌ها و کشتی‌های تجاری از تنگه هرمز اجرا کنه
🔴
امروز خوشحالم اعلام کنم که این اقدام باعث شده بیش از ۱۰۰ میلیون بشکه نفت از این تنگه عبور کنه
🔴
و وارد بازار آزاد شه بیش از ۲۰۰ کشتی تجاری هم با امنیت کامل از این مسیر عبور کرده‌اند.
🔴
این موفقیت بزرگ به این خاطر است که ایالات متحده آمریکا کنترل تنگه هرمز رو تو دست داره
🔴
نه ایران. ارتش اونا شکست خورده و اقتصادشان از بین رفته است. کار ایران تمامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126921" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126920">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcqiinN_MStmKeUnoepd1gs1aFvcjpqQanz5WpC4VV8tbQJm5I-DWCZd7PFzq-c22b_jcxyJ2vfIFinANTIWLYym5Mgm6d6AYvCsCncNS-n9JmO4j1fS83pfrsmwxmv-ZXYCGhazULaRCyWiQG5r2G9R46_Du9TTS75ycuCQBz4wVQ3-9SLH0SeRlVPqDg37pk7du2JjryX5a1URjXI_Rp78yS04OwMSIlpBd5B4MGLsSY9Dan4uZuVnDJfHHIv_OVRBHLXM4KMCn_m6ErbVUUlLCFJe3nOtn6tOS21JIKEFyvfqVkbKmh3r3Rc-K-L3h4b7v9M9OBVLDI4mK4C65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یدونه هواپیما ترابری C-5M Super Galaxy هم از اروپا حرکت کرده بود الان تو آسمان عربستانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126920" target="_blank">📅 21:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYDgPwC8-URECFw4zXhFjuV-AwEwhSU1KfYnHUeWi13PkX8v7-Q1EW7IVFYTLeaxH9th4HjUNloXB051iiicM3iZUbquAbD349Nc1ZvRR4dITcRrR2ic1d6xXSh5I30Uz_r2Ogc3F8Q3if2Zcf1eGIO02cCy7dfNIpUq7Cp3Sc5aRhGJZuU2lHlALNBpDgsoo87o5tFdqdLLJA0fbwJp3YiIxzCCt6pKcoZkwFQ9Vm2rlYbKD8tGWcYLDNFfuT9pf64ob_8MH7v7rbisWNdlLEF6LLQmCOcyBL7BOW3bxMamnNJ-Mgn1wioaV3AzCa2WaCK6RtJbXXeksctCkUYsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون یک فروند بمب‌افکن B-52 در حال پرواز بر فراز عربستان و حرکت به سمت خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126919" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126918">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuEPI0SnjE37mnLmmozkXxPvNjtq56cgfo-ImlJzf6Y4q0ChvzD13x0I2Tg612pEHekiMNvwL5-rQmLJRkwgcg9xcG8MdZ55tSyANHr_YRnGWHrt0aYcYxbWcIFon7Smuw-8i9UQSGI2Ks45jRDlgGgEv-UfwHm-OqCmefkLeoce5-IZICTTsEINwifHpO4hvT1VxIzqh5XD5-s6OioExJdGKg_FTKuA1BK051mn3evHskUWrEZdJil7xhlA38kvn-u9IRdG4BLE9y5GGlYJGlsw0Gv8DiQIzsoTm3VpsJb5G1KJrZACWYRRbSyYPjQM4xmCPVYxVoywcUI6Njva4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تبریک به نیکول پاشینیان برای پیروزی قاطع او در انتخابات ملی ارمنستان. من بسیار افتخار می‌کنم که از او برای انتخاب مجدد حمایت کرده‌ام و شک ندارم که با او به عنوان رهبر کشور زیبای ارمنستان، به سطوحی از بزرگی و موفقیت فراتر از هر انتظاری دست خواهد یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126918" target="_blank">📅 21:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر انرژی آمریکا رایت، در پاسخ به سوال درباره اظهارات ترامپ، می‌گوید از خارج کردن نفت از ایران توسط آمریکا مطلع نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126917" target="_blank">📅 21:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آکسیوس: ترامپ پس از سرنگونی یک هلیکوپتر آمریکایی، حمله به ایران را دستور داد، اما مقامات می‌گویند خشم او به دلیل عدم پاسخ تهران به آخرین پیشنهادش، تقریباً دو هفته بود که در حال افزایش بود.
🔴
این حملات طوری طراحی شده بودند که بدون ایجاد تلفات انسانی یا به هم ریختن دیپلماسی، اهرم فشار را بازگردانند.
🔴
حتی در حالی که نیروهای آمریکایی به سیستم‌های نظامی ایران حمله می‌کردند، میانجی‌گران قطری گفتگوهای خود را برای احیای مذاکرات ادامه دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126916" target="_blank">📅 21:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OXf5ykOiy_NGJnpMc8ccSA_G0wBpWGDJqij-qbU7MFP99qTbuD99tOhz0ZdeJjAf1Zq79jo58Zz13bs307JWb8zwAWCDdfxJSFZXa6A7Epzk7LTZHr07Ni100KC-dl3Z5RdNWryJxn2E7SKt1gOi8-IrlS71oHEzJLFDb252tWhNwM8JqSJlSNcLRxlevWemi4rBAIy6I5mn0H7swdxAjBB4YiJwO-axWG7YzKmSV7CnG4oJr4H_HvaWjGB8p2hM2aQoP705MWq0YYfXPSE7M6lGpDzG2JtUVzAkNFWjDgm8FRSkI_xMbSC1so2ML7JXSpZwniehjX7KswIYrkh49hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OXf5ykOiy_NGJnpMc8ccSA_G0wBpWGDJqij-qbU7MFP99qTbuD99tOhz0ZdeJjAf1Zq79jo58Zz13bs307JWb8zwAWCDdfxJSFZXa6A7Epzk7LTZHr07Ni100KC-dl3Z5RdNWryJxn2E7SKt1gOi8-IrlS71oHEzJLFDb252tWhNwM8JqSJlSNcLRxlevWemi4rBAIy6I5mn0H7swdxAjBB4YiJwO-axWG7YzKmSV7CnG4oJr4H_HvaWjGB8p2hM2aQoP705MWq0YYfXPSE7M6lGpDzG2JtUVzAkNFWjDgm8FRSkI_xMbSC1so2ML7JXSpZwniehjX7KswIYrkh49hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه i24News : انتظار می‌رود ایالات متحده در ساعات آینده حملاتی را علیه طیف گسترده‌ تری از اهداف ایرانی انجام دهد که دامنه آن از حملات شب گذشته فراتر خواهد رفت
🔴
هدف از این حملات ارسال پیامی به تهران برای ارائه پاسخ فوری در مورد توافق پیشنهادی روی میز است و به معنای بازگشت به یک جنگ تمام‌ عیار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126915" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKKGtmS0pYOtBh8GKhixKLX0ttjgDszBNVYR1IFrb2oVBgIBWLMLf1RpUAYk5w8KkJ_PbbDyn8xmDxgoYcQduAslridqshYKz3px9BSnpaJTsz-6PIVl7SRT8-aSjt59IqoUC9F3-sXT6lffzVpqvG-ZmDpkgYn8lt98kEGZ5iUhEtQ7XuER2T_Chyjn9yOBnIa0gjBDu2BubK8ONxt_Cq0rDyQGXAADUpKXEVZnE-LJrET_50dW_KrsuMfEe4Wpys8QZb4h7GzAMCpBTY_nmzibE575E7jJ7kBN2ZQsL_Mhl7H7EuLPMbxrcIn4exVhwteWPq2MEOjPw8DjQcY2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل هاکبی :
احتمالاً اوضاع تو منطقه به‌زودی یه کم داغ و ملتهب می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/126914" target="_blank">📅 20:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ خطاب به سازمان رادیو و تلویزیون اسرائیل: ما در حال پیشرفت عالی با ایران هستیم
🔴
بدون من، اسرائیل وجود نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/126913" target="_blank">📅 20:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126912" target="_blank">📅 20:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDwAs3Fsimj9vzEzEeeTAmQPfGHVIOH44qSfNGQb2syZdKXtjVj-4T1wdGNUEL48i89k_ZXlJvUefkEGWE0SmDALakk6pl9CO_-64LjbUmEui5wk_t6GUsHxrYmCjZ0ha19P_KI1ncchEmXvD66tReKEdsUBD81Khax40v-Vl4jsXOnTpMZA381CTNvk-Zn2WOFGap6TKisuFpUCnvsoLVgZDLAo8sn1XrBdlA0CLDc9qv1_g_kBBWEX4izXuowQ59hQQ8Cou0NKNzIRvMTe8DN1wCH9mi8ze0EfZvUyC7cNfo71w4dn7WaiiQvhF_VnIFnwm9Bq613OWZ3fe42wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون / آتش‌سوزی در انبار کالا در میدان قیام
🔴
انبار فرش ، جنب پمپ بنزین پل ری!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/126911" target="_blank">📅 20:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حنظله تهدید کرد !
🔴
گروه هکری حنظله: به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند
🔴
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست. ضربهٔ ساعت‌های آینده تلخ خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126910" target="_blank">📅 20:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126909">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/126909" target="_blank">📅 20:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126908">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GARPYx6-t_uTUX6h8QM4ntTfjDT7uKb_bO8TmRE6cAiB6Jq5z2FRgnQMz95kq8IVVXJbbIRNLKhA1bmPGTQJiZ-xg58wZo4pPwDNMB4pO647uOJj7vhLJS9UNEDrY6oEGyXcIaFu3VkYxDVbffec8YN6KeJd8QNuKAX5sVzbu7NlTDVVBOnPxDQkLYfP6DgVv8i79MNzqvucFzYWq16KMF-pK7LzrYagkL_QjkQ_b8t70SvLDBGBePZqfn_iI2lXY_wy5BStQFBrv5LTZQvXxIzfSAqmTKjkARA-n5YIo3NOl0uw0YFK5zo0MBBJPvw5vqllQhERbV9EuBAzxdGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126908" target="_blank">📅 20:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMIi1B3V0UdgUTKPzXv2tvCw7bWz7FwZyZZZmAM8bU-pdeFOx2Gu7UAIwUVUgIUviJdTUqZtbjNYBacBvyUngBKDSfRT1TyYvnZjXAUKxyxYi2YDG4LdxtZRfALEANJmMtGHy3mMbgJJpOFrA6QozSNt9VnpZufid0J2y5bjyspRrJCVnLuXLX4EKJnuuf9mIn8SAxHeN8QultDfW1gx6bNQeYU3yqpHiEkeRB96exn3BjjGCulKMPa11Qh3zYk8KWMgIc3GgfzRDxaIWKQ67QrskDfqqmJDXkEekzFjYDrugYjMUQ6qiOazLE_9Ult__ZLvDPFCBHMw1jgk9fzNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: زیرساخت‌های حیاتی شریان حیات مردم هستند. تهدید به هدف قرار دادن آن‌ها — از شبکه‌های حمل‌ونقل تا صنایع برق و آب — نشانه قدرت نیست، بلکه نشانه‌ای از ناامیدی در برابر اراده یک ملت است.
🔴
ایران، با تکیه بر دانش و توانایی متخصصان خود، وحدت ملی و همبستگی، در برابر هرگونه فشار یا تهدید استوار خواهد ایستاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126907" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پیت‌ هگستث در خلیج گوانتانامو:
ما به دنبال دشمنان نیستیم. ما به دنبال دشمنان نیستیم. ما یک دوست بزرگ هستیم.
🔴
و امیدواریم به زودی بتوانیم دوست رهبری دولت کوبا باشیم.
🔴
ایران باید بداند که به ما بیشتر چالش ایجاد کند، کار نادانی است
🔴
من همین الان وارد یک قایق مواد مخدر در کارائیب یا اقیانوس آرام شرقی می‌شوم.
چون ما شما را شکار می‌کنیم همان‌طور که القاعده و داعش را در خاورمیانه شکار کردیم
🔴
در حال حاضر، حملات دفاعی برای اطمینان از محافظت از مردم ما.
🔴
باز هم، برای ایران غیرعقلانی خواهد بود که ما را بیشتر به چالش بکشد.
🔴
رئیس‌جمهور ترامپ به دنبال یک توافق است، اما نه فقط یک توافق، بلکه یک توافق بزرگ به نمایندگی از مردم آمریکایی تا اینکه ایران هرگز به سلاح هسته‌ای دست نیابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126906" target="_blank">📅 20:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126905">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تسنیم: ترامپ باز هم از ضربات کوبنده ایران عبرت نگرفته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126905" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upWM9mbyFi4wHELWN-WqycOz4VgnSgvmQv2TmWDjxvEAhmudHvixXEeLmcM3p_RYB15HfXA-3R5RSQWsZGHK9QBfFkOHLH6LMKc0QNDeDQA3Is6upXFqJnspFItbtZCCO_9gpPSpcJdNsbV6xtMwQRkiBfPHv2QQW2OnOl13UgPercmu5_ZqBZwEe9bGCiT1m7EU-0BWzYGYyX9yPni1GL9FsYSVhZxqbom-m3RwwYd9PCrFQCyG0YkUk8F9cocoPEv9rKKME48tDx8oyE0j1jWDUsKBlfa_YyvTwvoOiRWWsamnYw2Gdl1en_3ERGz2r2-T83CWohCR691boBkW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19a799ca2.mp4?token=U9hXRLyK_pXh-6IB0YzwmFbj2nUymZK7cjljGo1wxMhs_XJvTPhX41vjJSCs3LWzA_AdkM8mkIEgwxhi9W5n7A_nvlT-zMLIB5FPlwWCd21k4LRXUggZQ6pf6qf9rVYXMgcuXX6zWXmUVlTyWFqm69FKEFUk1LlcREcjmfuABxAsapYAy_vJ7F6aLCXiKzKCwHKYBZLNBUtRkO7Selhyd4hu8bPw1VCXJ8deDL3jDBH6sDr73d2SHtk3rQq-x233b1AsRkvz193404kci7rBTFP373gtdxX2Jk-DhVpzOaE04q0OxD_9V_Qq6Tz96rpsxh-E561cVFbnR0xkgE-mYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19a799ca2.mp4?token=U9hXRLyK_pXh-6IB0YzwmFbj2nUymZK7cjljGo1wxMhs_XJvTPhX41vjJSCs3LWzA_AdkM8mkIEgwxhi9W5n7A_nvlT-zMLIB5FPlwWCd21k4LRXUggZQ6pf6qf9rVYXMgcuXX6zWXmUVlTyWFqm69FKEFUk1LlcREcjmfuABxAsapYAy_vJ7F6aLCXiKzKCwHKYBZLNBUtRkO7Selhyd4hu8bPw1VCXJ8deDL3jDBH6sDr73d2SHtk3rQq-x233b1AsRkvz193404kci7rBTFP373gtdxX2Jk-DhVpzOaE04q0OxD_9V_Qq6Tz96rpsxh-E561cVFbnR0xkgE-mYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/126902" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126901" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز: هند معاون رئیس هیئت دیپلماتیک آمریکا در دهلی نو را در پی حمله به یک نفتکش در نزدیکی سواحل عمان احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126900" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126899">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: از زمان آغاز محاصره تنگه هرمز، تاکنون مسیر ۸ کشتی را مختل و ۱۳۴ کشتی را تغییر مسیر داده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126899" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126898">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قطعی آب سیریک پس از حمله آمریکا در ‌‌۱۲ ساعت وصل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126898" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126897">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwW8OYzYFnWzmGZN_zYHlRCZsQrvvPeMuL7b4GCpw90RS1PAk1p88wbgMwTR09t-UzuNEOmc3leas-TY_j7McI9LhwVw9oQdp7zNDxKIwm8-p7YEbocywGatCWq7sdkd2U56gszR8IfaON00KT1CtfZkrwBpRPgYUFJla44rObugC7dnaDIxcFEPCBlt5tfWiE-CrFU3xrXQi24-uQ2dqPtltc3yxl5cEGG1HgA9PNTYlk4fht5HuuFi4dIlTKT2Bq7Y3Bxd_KTEwbGvVEds1YYdhoL9CSnHzngtsBPE88oOVRLvLMmzswvdsilcOLhCaL0VY2KRJQ27K_QRBdZZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/یدونه B52 داره میاد خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/126897" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126896">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf0c94043.mp4?token=klSi4dvTO9QsnO3S-z6tfgAvFBtIOEQ4P5SF5eGe-Wb3Hm224uCdx4NH24ZJD28atdqVd2EJyGPvcbZNVY9Gu83XiYIePsIuesWIoSNByD7zkLoAXTA6Yzavawp3UJM1CBKi_QVSujfiys-mTWJphPFPYMAXjIY124WnTZMokVhn9K-5kqYuejvVmAl3OSiDnA24giWStgF8bK91sn5oSeEOzTMu0WLnQLsoex24tmtRQA6XCzOdhWOfUHPuCkWIW7QCz0yZN3sVZLj0K705sPOGNVLojv0PkbwMwP6CtmGyomTlw9ayuN7PUlA9DfUuZ8137G0ymNl7GJLtbRMUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf0c94043.mp4?token=klSi4dvTO9QsnO3S-z6tfgAvFBtIOEQ4P5SF5eGe-Wb3Hm224uCdx4NH24ZJD28atdqVd2EJyGPvcbZNVY9Gu83XiYIePsIuesWIoSNByD7zkLoAXTA6Yzavawp3UJM1CBKi_QVSujfiys-mTWJphPFPYMAXjIY124WnTZMokVhn9K-5kqYuejvVmAl3OSiDnA24giWStgF8bK91sn5oSeEOzTMu0WLnQLsoex24tmtRQA6XCzOdhWOfUHPuCkWIW7QCz0yZN3sVZLj0K705sPOGNVLojv0PkbwMwP6CtmGyomTlw9ayuN7PUlA9DfUuZ8137G0ymNl7GJLtbRMUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: براساس اطلاعات دقیق و میدانی، تعداد کشته‌های ارتش آمریکا تا به امروز ۵۰۰ نفر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126896" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126895">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac1b45c2.mp4?token=RjBtPoPTn4QnimgLSEV4aEbAhHApR9VwTEeHMDwUiYawo9vhGgywM-Uwl6VTAafNVItUNkfOAGX_-M51XLnm-2LWdEDLEFBLuIMeI6UplTZEPHFDU4x4rq_tk8dHPcHoxbh6uINc8bUOdER13mDzl7c-ZVAG7Ykn2666YPQKQNqMeUgikzZiH4tSKeYxuDhwACBuIHxKyoarDeWHG48_wcEH8OF63prid3sLAauRus9Tt5oXclTuu5XwcGRj3-IVasXWkkaVmLh_veOXa7JU9dk9BCNP6LrHzpeJhuyPeDzSe48AXqETGj1Uks_gJkXbnSFgUDT8fpP9I3tLhiUaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac1b45c2.mp4?token=RjBtPoPTn4QnimgLSEV4aEbAhHApR9VwTEeHMDwUiYawo9vhGgywM-Uwl6VTAafNVItUNkfOAGX_-M51XLnm-2LWdEDLEFBLuIMeI6UplTZEPHFDU4x4rq_tk8dHPcHoxbh6uINc8bUOdER13mDzl7c-ZVAG7Ykn2666YPQKQNqMeUgikzZiH4tSKeYxuDhwACBuIHxKyoarDeWHG48_wcEH8OF63prid3sLAauRus9Tt5oXclTuu5XwcGRj3-IVasXWkkaVmLh_veOXa7JU9dk9BCNP6LrHzpeJhuyPeDzSe48AXqETGj1Uks_gJkXbnSFgUDT8fpP9I3tLhiUaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ساعت 11:14 شب در 9 ژوئن، پس از اینکه کشتی دیگری با تلاش برای انتقال نفت از ایران، محاصره جاری را نقض کرد، نیروهای آمریکایی برای دومین روز متوالی یک نفتکش را در خلیج عمان از کار انداختند.
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) M/T Settebello با پرچم پالائو را هنگام عبور از خلیج عمان غیرفعال کرد.
🔴
پس از اینکه خدمه بارها از دستورات نیروهای آمریکایی پیروی نکردند، یک هواپیمای آمریکایی مهمات دقیق را به سمت موتورخانه کشتی شلیک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126895" target="_blank">📅 20:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126894">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeafbbbb61.mp4?token=IgbJlcHxWncm8aWqc7rCkf2bKcVJ3-TdGoOfDMWWrqltJwCR_rcY9pFvdEmX3FWZxb4qnuU3Y8eC5YEJhNUuQBwjtjRSDar1W8Ydy3DVcZHYQKHNsJR3ty9ucM-ZBNKrMy7li0gc6T5RPn0mK4ozJfQThrtw7k576plVKISDH_whtmf60p9HbsJlfIM0XF5_zo_t3nvT56joeU6MdcClmmWyRZVQ0SqMdDpdwH35tsRaP5SuOPOuL61yeXSfEVDHn24Ex7T4kt3w8W_l7LdotMQWPQ_pQuPA2irc990yM8vCqHSLsO1AJhgQ3k2WcMgKg1JYI4NahEESK6R9cl9Mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeafbbbb61.mp4?token=IgbJlcHxWncm8aWqc7rCkf2bKcVJ3-TdGoOfDMWWrqltJwCR_rcY9pFvdEmX3FWZxb4qnuU3Y8eC5YEJhNUuQBwjtjRSDar1W8Ydy3DVcZHYQKHNsJR3ty9ucM-ZBNKrMy7li0gc6T5RPn0mK4ozJfQThrtw7k576plVKISDH_whtmf60p9HbsJlfIM0XF5_zo_t3nvT56joeU6MdcClmmWyRZVQ0SqMdDpdwH35tsRaP5SuOPOuL61yeXSfEVDHn24Ex7T4kt3w8W_l7LdotMQWPQ_pQuPA2irc990yM8vCqHSLsO1AJhgQ3k2WcMgKg1JYI4NahEESK6R9cl9Mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: برخی افراد نگرانند که دریافت ویزا برای جام جهانی روز به روز سخت‌تر خواهد شد.
🔴
پرزیدنت ترامپ: ما بسیار نزدیک با هم کار می‌کنیم تا مطمئن شویم افراد درست وارد کشور ما می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126894" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126893">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=VseYi9n7kmalkpN1EuiqN9BcWbnAiDohEz8aG2UJFa7-iH2_dU4PkwRmahMB8p2VcmZa5r4hL1DXGVHLuLXWww-VjP5SDCPVI6qXib7r7WUWN6NcstG0iKXvKc5cXkAuokJTE8lFOEfs5SJqhhGGNUEGSnttH2Ols2dFTWkXesuF9RJo6A8iZWU3yZQvLQ0t51G6602QiR8OtB-WdfYYVucqEa9Q5BmToDNdK1Y1U1Qq06QJQ9BO7ByvLYLZLwAiaVUtJCiuwUMQaHRwmG3QV3RBaILx_9ODy8dTsL1YIy7wMSZ9mbSSnuRE4T1D8czE2jx-8AQ0TPXZS_joAi8_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=VseYi9n7kmalkpN1EuiqN9BcWbnAiDohEz8aG2UJFa7-iH2_dU4PkwRmahMB8p2VcmZa5r4hL1DXGVHLuLXWww-VjP5SDCPVI6qXib7r7WUWN6NcstG0iKXvKc5cXkAuokJTE8lFOEfs5SJqhhGGNUEGSnttH2Ols2dFTWkXesuF9RJo6A8iZWU3yZQvLQ0t51G6602QiR8OtB-WdfYYVucqEa9Q5BmToDNdK1Y1U1Qq06QJQ9BO7ByvLYLZLwAiaVUtJCiuwUMQaHRwmG3QV3RBaILx_9ODy8dTsL1YIy7wMSZ9mbSSnuRE4T1D8czE2jx-8AQ0TPXZS_joAi8_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي ایران و پاکستان
:
من به درخواست پاکستان به آن‌ها (تهران) فرصتی دادم. مارشال میدان و نخست‌وزیر پاکستان افراد بزرگی هستند.
🔴
ما مانع از جنگ آن‌ها با هند شدیم
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126893" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126892">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: وقتی جنگ تمام شود، تورم مانند سنگ پایین خواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126892" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126891">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
🔴
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است. حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
🔴
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126891" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126890">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ : این یه مسیر برای رسیدن به سلاح هسته‌ای بود
🔴
اونا تو دوره اون در حال توسعه سلاح هسته‌ای بودن
🔴
اگه سلاح هسته‌ای داشتن دیگه اسرائیلی وجود نداشت خاورمیانه‌ای هم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126890" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126889">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcf6ef687.mp4?token=OJs8H6dlqLbmfDjdSKnIwxAnoMpRyijFNsSfDr5UY0ARsyKFojuExxF2NojzYOGN7WDrrsHy9ToccTXkaszYWnrTQtokzZj1pnZm7Ic6Wt9Byg796Rw16XkjOD39S2u7fibznWRw2nyWLqo-Oi_uthUl7foBXoDYJTfJbiC4aKcsel3wGYiRZ-rriTx-W6cqrh8Dl6WgWyrRj9HFJY94EKCuKtAMOS6JdHNMQrz2tV94Z-Amt4s-j4kxG0wgVTfyNNduBW7LIWHbuliszIhhGSoF0ddNqPGyj0QU8qHMfwuo4h04mcdmYsMe0yduNznckzc8YoR32WJspcZahPOZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcf6ef687.mp4?token=OJs8H6dlqLbmfDjdSKnIwxAnoMpRyijFNsSfDr5UY0ARsyKFojuExxF2NojzYOGN7WDrrsHy9ToccTXkaszYWnrTQtokzZj1pnZm7Ic6Wt9Byg796Rw16XkjOD39S2u7fibznWRw2nyWLqo-Oi_uthUl7foBXoDYJTfJbiC4aKcsel3wGYiRZ-rriTx-W6cqrh8Dl6WgWyrRj9HFJY94EKCuKtAMOS6JdHNMQrz2tV94Z-Amt4s-j4kxG0wgVTfyNNduBW7LIWHbuliszIhhGSoF0ddNqPGyj0QU8qHMfwuo4h04mcdmYsMe0yduNznckzc8YoR32WJspcZahPOZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : فکر میکنم اونها میخوان مذاکره کنند...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126889" target="_blank">📅 19:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126888">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: ونزوئلا به یک کشور شاد تبدیل شده است، باور بکنید یا نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126888" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126887">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: ما با بمب‌افکن‌های B-2 به ایران حمله می کنیم
🔴
میلیون‌ها بشکه نفت ایران را بر میداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126887" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126886">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecrl0SHddJF1DR7aUUJAJBic0mjuv4cCV_p0tOz2RiB5VWQ2_4_RlxjPKYE3Do7prL4XpFw-zVRXDJzciJGR9A31As8tVho8vxEq9dSiI98GjPjSGmPkDxO0PDF2GW3d9cL4VqrdFY-0ztiQxKrPziVjFWtvwcErW2GTDOgdrIUQuufYZ5jDtl5jHhxgNf_I_D-7d5wCuetSumG2mHKBwjiU0_raaGOzmeI89dR92HQDAryp4i3hhmp79Pn9OepYxRUKDJ1tFdKqiJrVjM1wzbnp_0RvB_jFPOAk_YAtim_G1UhH4V-UREMdU10YcVh-uDrkHZg_OUhqyoSES-zbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید تا دیر نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126886" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126885">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ایران وقت‌کشی می‌کند و من می‌گویم چند روز دیگر هم به آن‌ها فرصت بدهیم، اما آن‌ها همچنان به تعلل و وقت‌کشی ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126885" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126884">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: شب گذشته ۲۲ کشتی ایرانی را منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126884" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80f48c832.mp4?token=bLm22ARbJlvGhmEhcYgH01835zC6LSpagWlEp60idRW5pv-0PB0HiTWWQ1q4lOlCpbxsiRiaxVNvCehP2aD9I_W0IgY24P3MdKQ2K6ssO34ZjG_iBtmGS-3isDgXDl-0VnNf8fcabFOpLVg82hnLZl7ynpNwmsKDLzhSa7UDkA9NwyAlL2v8f3PutOHwxLa6GyrM0kAGwStSX-nPxDd67DN5AS_rJsgYQxkp6R0vP5wXOG6V-LS69OBX4XEMFc4G0QPp0e9zK2d4CCj6YGeapih_DckvXifGaR_fSkR54x38LeCRQgj9QRHRE7kOFOXoGmtsueyTXQva_DPz8iNtDCXI6rga6Q7ER-858OdvRPnjvCemiL3BFRVPck0M4neWzC9-6iPzP40QA-rVZvbZ1V6qkhcy5sL8llc-iTtqgkUIkL63JXUy1V7faUyaYqPoGZ5D2f2HEL4Wd5KM-xmMbKNiNvWlM20ruC_TQr_2XUeTlvyxSXrZ-4cvmnIzpyK8NoWt7bHsuxNtHCPmURjXVqp_meIzTdlOFw-VgK20cVNdAJKTdoD5PZyiy6NOLabk0g6Osz-Zvv3hO2BrRRficDT5TUCYP3Blcl6UA6n_lzfbqOXs8TaAth1BJdOqGqivC6hrQyGMrvW3UiqoqeSm_s4dWlujKKwRl2myjwZV_jU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80f48c832.mp4?token=bLm22ARbJlvGhmEhcYgH01835zC6LSpagWlEp60idRW5pv-0PB0HiTWWQ1q4lOlCpbxsiRiaxVNvCehP2aD9I_W0IgY24P3MdKQ2K6ssO34ZjG_iBtmGS-3isDgXDl-0VnNf8fcabFOpLVg82hnLZl7ynpNwmsKDLzhSa7UDkA9NwyAlL2v8f3PutOHwxLa6GyrM0kAGwStSX-nPxDd67DN5AS_rJsgYQxkp6R0vP5wXOG6V-LS69OBX4XEMFc4G0QPp0e9zK2d4CCj6YGeapih_DckvXifGaR_fSkR54x38LeCRQgj9QRHRE7kOFOXoGmtsueyTXQva_DPz8iNtDCXI6rga6Q7ER-858OdvRPnjvCemiL3BFRVPck0M4neWzC9-6iPzP40QA-rVZvbZ1V6qkhcy5sL8llc-iTtqgkUIkL63JXUy1V7faUyaYqPoGZ5D2f2HEL4Wd5KM-xmMbKNiNvWlM20ruC_TQr_2XUeTlvyxSXrZ-4cvmnIzpyK8NoWt7bHsuxNtHCPmURjXVqp_meIzTdlOFw-VgK20cVNdAJKTdoD5PZyiy6NOLabk0g6Osz-Zvv3hO2BrRRficDT5TUCYP3Blcl6UA6n_lzfbqOXs8TaAth1BJdOqGqivC6hrQyGMrvW3UiqoqeSm_s4dWlujKKwRl2myjwZV_jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به هیچ‌چیز که کانادا دارد نیاز نداریم. ما به هیچ‌چیز که مکزیک دارد نیاز نداریم. اما آن‌ها به همه چیزهایی که ما داریم نیاز دارند.
🔴
آن‌ها باید با ما بهتر رفتار کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126883" target="_blank">📅 19:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: ما دیشب و پیش از این هم برای هدف قرار دادن رادارهای ایران تلاش کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126882" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: خواهیم دید سر توافق چه پیش می‌آید. واقعاً به توافق نزدیک بودیم، اما آن‌ها مدام ما را به بازی می‌گیرند. مدام ما را گول می‌زنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126881" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRgWtFC0xFO3e20_4UD2kFxpKLiL7r-DSAeNUHToQRI7aVVWtdINcLtJLdlxX85gypomFVMKtCN2xiLda6arZLfxWfojmLx3hLINq-lUMNQMGoaIsYyQiWtohWdYnWqF8KQSy6vlq-16LxoMvbJXXKW1MUgHjwBv3rtMFlNAEbnaVTkTPMWYIMedicbzdbz61UXb4tjuxnmGpfvenKBIbAuZ5h7tsVuvjsKZU6TbXQ64fe6skqtqcL8kz7-jx4dhoVdZSgEF2ixhQpzJWPY7c0hee4VlVSZHg9_nfZXgTq62oDPrQdbzzXk6h0D0Gmg6jSf2GOe6-GOo2X6jguIxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت بعد از تهدید جدید ترامپ بر علیه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126880" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929ac5f5bd.mp4?token=SHTR7nEtIUJuoujIraV9B5pj8xL9k3A4cYdA6t6QrTMdQHj2SgHljw4IDMtV18oPYMQnItyxCt6er7lrIfctmXLrXDPP3_tCnt6tN-KKspChCWTIt6BMD1ETGJTaJMpCFZkiVFS4QfxH_6XO2dLk0W1VT3TqU2GjHP3IafjZH3SLAVk5Je5cUAJGBV--NorVNCs3aFxVlP2VqQMJRkkIOivu2rILnA-o9bQ04EHdM81Rby8upIuNAfg24w83Jk-rDiNKoFleiIro35_w2lTSnBbcv8YSp3PPeAM1NDklH21MUzpwUBoqVM67hbG6_oimhirn_9yMyahSFan6ctKJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929ac5f5bd.mp4?token=SHTR7nEtIUJuoujIraV9B5pj8xL9k3A4cYdA6t6QrTMdQHj2SgHljw4IDMtV18oPYMQnItyxCt6er7lrIfctmXLrXDPP3_tCnt6tN-KKspChCWTIt6BMD1ETGJTaJMpCFZkiVFS4QfxH_6XO2dLk0W1VT3TqU2GjHP3IafjZH3SLAVk5Je5cUAJGBV--NorVNCs3aFxVlP2VqQMJRkkIOivu2rILnA-o9bQ04EHdM81Rby8upIuNAfg24w83Jk-rDiNKoFleiIro35_w2lTSnBbcv8YSp3PPeAM1NDklH21MUzpwUBoqVM67hbG6_oimhirn_9yMyahSFan6ctKJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : رئیس‌جمهور ترکیه اردوغان مدام اسرائیل رو تهدید می‌کنه؛ فکر می‌کنید ممکنه بین اسرائیل و ترکیه درگیری بشه؟
🔴
ترامپ : اون دوست خیلی خوب منه من خیلی دوستش دارم آدم قوی‌ایه
🔴
رهبر خیلی خوبیه فکر نمی‌کنم این اتفاق بیفته تا وقتی من رئیس‌جمهورم چون اون به من احترام می‌ذاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126879" target="_blank">📅 19:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گزارشگر: برای تولدتان چه آرزویی دارید؟
🔴
ترامپ: صلح برای کل جهان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126878" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: به توافق نزدیک شده‌ایم، اما ایران همچنان طفره می‌رود
🔴
ما توافقی مانند توافق اوباما نمی‌خواهیم.
🔴
من برای خاورمیانه و کل جهان صلح می‌خواهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126877" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bb596104.mp4?token=dMw8ePJkrhSC7lVfCXbW3mvXSipmX3i_xr8AKGAulDZIr3PcBX5lOTXzpwTISqgvDxiQuVfneNcsZvZ9sjYOfO7DWs6f_edf3sMHvYdLoDmGuNciWZCBCcjBl1hs-WOXIvczAlHvfwGzLVZ89ajuZ2yAzdzSuijbss3wGF5knUi9p9bSZ2kcDoHeRK6-5uVTfXB7xg77WUfOUSGTE8cRMeLbo64rSin6cvkbQsL7TYw_3zYoza2JxKeQYr1O7sjlbZ20e3gdtj1FOFAwSe_JP8U6J8r8zzXy7_PmCHIS6nDeXuAMYc8CNNQTXYna5wEKaR-XQsQlW30P-gh8Ho1iGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bb596104.mp4?token=dMw8ePJkrhSC7lVfCXbW3mvXSipmX3i_xr8AKGAulDZIr3PcBX5lOTXzpwTISqgvDxiQuVfneNcsZvZ9sjYOfO7DWs6f_edf3sMHvYdLoDmGuNciWZCBCcjBl1hs-WOXIvczAlHvfwGzLVZ89ajuZ2yAzdzSuijbss3wGF5knUi9p9bSZ2kcDoHeRK6-5uVTfXB7xg77WUfOUSGTE8cRMeLbo64rSin6cvkbQsL7TYw_3zYoza2JxKeQYr1O7sjlbZ20e3gdtj1FOFAwSe_JP8U6J8r8zzXy7_PmCHIS6nDeXuAMYc8CNNQTXYna5wEKaR-XQsQlW30P-gh8Ho1iGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ایران داره ما رو مثل آدم‌های ساده‌لوح بازی می‌ده
🔴
چون قبلاً با یه سری رئیس‌جمهورهای خیلی احمق طرف بوده من خجالت می‌کشم اینو بگم ولی آدم‌های خیلی نادونی اینجا بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126876" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: فاش نمی‌کنم که آیا امروز پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126875" target="_blank">📅 19:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126874">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: ایران وقت کشی می کند و من نمی دانم رهبرانش چه کار می کنند. ما مصمم هستیم که از دستیابی آنها به سلاح هسته ای جلوگیری کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126874" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126873">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ:  ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت، و آن‌ها به این موضوع توافق کرده‌اند. تنها کاری که باید انجام دهند امضای کاغذ است. این موضوع کاملاً مذاکره شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126873" target="_blank">📅 19:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126872">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4265b3dd.mp4?token=JGeBy7bXBawxLV4OC-eejoE5fTmYGfQ1qNqtwAbTTqDvkgjQgWe0eAE-LcX7A3MsfTOp03_gUZ5uqC2ocHFgzrDyA--qDd0NjLNBvt9VsfIVjaT-H7DdI6OYyakLkZN2UlpIgAx2baW_31k8sCpbvDMPvBFQ0vUPV8KJmKXqA-bI1EM_K4TvEcWGMBFzRfXezMcap7WM5a-0RdMvffPjxdXfH_JcxrsYdy52G80diKW9Ug_0-s8n0k3UGWbrpg-ewL22k_ltlxIHLMwFTjsylkIBMJpucOFfOS-YJfrQFWQYbV6KrdVXOw2KjXIUy8ctEAaE7Qjf4tMWJe_noLFEFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4265b3dd.mp4?token=JGeBy7bXBawxLV4OC-eejoE5fTmYGfQ1qNqtwAbTTqDvkgjQgWe0eAE-LcX7A3MsfTOp03_gUZ5uqC2ocHFgzrDyA--qDd0NjLNBvt9VsfIVjaT-H7DdI6OYyakLkZN2UlpIgAx2baW_31k8sCpbvDMPvBFQ0vUPV8KJmKXqA-bI1EM_K4TvEcWGMBFzRfXezMcap7WM5a-0RdMvffPjxdXfH_JcxrsYdy52G80diKW9Ug_0-s8n0k3UGWbrpg-ewL22k_ltlxIHLMwFTjsylkIBMJpucOFfOS-YJfrQFWQYbV6KrdVXOw2KjXIUy8ctEAaE7Qjf4tMWJe_noLFEFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووووووری / ترامپ: امروز ایران را به شدت هدف قرار خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126872" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4521420dfe.mp4?token=NtsZkPpNeN2MfOCAHTL24kYC_TMQUN2TQa9jl-5A2ExwfZg6hPBCAFQL4cPVqW9_ItUhH37y8qxwrP9upah2RkKLsIBrao2xEBrBhRm23EN-TojBasjizoQeZGE-FJ-vPAKxA4InqZRX7Zwp-gXM9mFKx0sP06qGtYoDYo0T8G12_6TROzMEtGO5wc-5AO15lErfBkU-QbvGHK_tVMiX1jsjWFlRLvswd6EiHG37NiH7qOVkcU6JdcddPkDA0PrQocsIYmttTqoQ8bFJjaFTG_NMo_5B4LVq1gGh46jU-1NZZV4j-3vG3YsAjE7JyACjANEIWAXBS6nP16iJ938TCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4521420dfe.mp4?token=NtsZkPpNeN2MfOCAHTL24kYC_TMQUN2TQa9jl-5A2ExwfZg6hPBCAFQL4cPVqW9_ItUhH37y8qxwrP9upah2RkKLsIBrao2xEBrBhRm23EN-TojBasjizoQeZGE-FJ-vPAKxA4InqZRX7Zwp-gXM9mFKx0sP06qGtYoDYo0T8G12_6TROzMEtGO5wc-5AO15lErfBkU-QbvGHK_tVMiX1jsjWFlRLvswd6EiHG37NiH7qOVkcU6JdcddPkDA0PrQocsIYmttTqoQ8bFJjaFTG_NMo_5B4LVq1gGh46jU-1NZZV4j-3vG3YsAjE7JyACjANEIWAXBS6nP16iJ938TCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
پاکستان هنوز در حال تلاش برای رسیدن به توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126870" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126869">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587a5ae9fa.mp4?token=ncre3gFxuTOIB1tovsFmuKdeCRsVcL72KMUX7aFWBtSYWeRfUzOw1Vf-aBu2Qn9fpNOW0yIJ8qMbK6cj2fOpTgelbSBXiK51rhCi8C-RnUhzfag1J5_SQprnotNVNdkZ3FG5C556JGDMjw_40Gn6GVxmpuUlDrG97x0aQ5dRqNnsdSllejJiP8k8hpjgP6y1fsiZNkvHxD4tsr_fT9bI7MEIMehr2OxHivQf0UTM8pylNo1mQd-M0OFH8Jax2qkmQW4mDaVGBjfu7-DbGjXYaab7hoNi62nysTGyk2vavTWll-SYGC5nTz5cH3kGBvevrOdcp-XAqnKLydv2Z0w7Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587a5ae9fa.mp4?token=ncre3gFxuTOIB1tovsFmuKdeCRsVcL72KMUX7aFWBtSYWeRfUzOw1Vf-aBu2Qn9fpNOW0yIJ8qMbK6cj2fOpTgelbSBXiK51rhCi8C-RnUhzfag1J5_SQprnotNVNdkZ3FG5C556JGDMjw_40Gn6GVxmpuUlDrG97x0aQ5dRqNnsdSllejJiP8k8hpjgP6y1fsiZNkvHxD4tsr_fT9bI7MEIMehr2OxHivQf0UTM8pylNo1mQd-M0OFH8Jax2qkmQW4mDaVGBjfu7-DbGjXYaab7hoNi62nysTGyk2vavTWll-SYGC5nTz5cH3kGBvevrOdcp-XAqnKLydv2Z0w7Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي ایران:
من چند ماه است که با ایران کار می کنم و آنها باید قرارداد را امضا کنند. معامله خوبی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126869" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126868">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / ترامپ: به ایران که به یک هلیکوپتر آپاچی آمریکایی حمله کرد، حمله خواهیم کرد
🔴
ما با قدرت به ایران حمله خواهیم کرد، این کشور باید توافق را امضا می‌کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126868" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126867">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / ترامپ: به ایران که به یک هلیکوپتر آپاچی آمریکایی حمله کرد، حمله خواهیم کرد
🔴
ما با قدرت به ایران حمله خواهیم کرد، این کشور باید توافق را امضا می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126867" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126866">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e8a0de94.mp4?token=CQqIyIj1blL1fCsZTYfQqnZOBwr5oUklH-Vc9wq-xySG0tBVSKw2EJNhtOWuI7E6UzWPTNAdltA5sCQbX3ho7PWwLrATFb2Pkr1QeCNesiEGYrrpeAylMGAWTAqromPxo2mbsdZ1lPOp-xLyGIQ7_kUv0QEL8PgNtQ6CIpWITkgiWjhGIwJfdC3BAbyq2JZ5wA7AI5PCVOjpLWFDUx64rYPiuvItsEL-EXxzOAVDkxxtGKvMSqY096ghRiPM5M55v03NBobduuGLdYrWNFr1RgZgtw7QYOESpFVPaPp5mJ_qaQK1L3TCcuqNBP1UQVRrc4YNfm2gAbv_ioceT1gDMYWyrieLrnYSD4M5blp9jQYZwxQuF7xIgPqKmLahZqjHZGJ6rNz_Glk0LbekV2KkHvp728beXTH9oTbIPfPsGjxnzTprEcDZa5z38OlAM-BULNVfKZHbLAu-udKd8JDgJHvkAGi2eqDlIAuTTpA7L7djqMCDwjRC0kr1cB3v79L7oZ_p4mDqKLoE9Q608WQXMc5_qAhNqFlQlQoD0yTExiR0pxfqjKBqNIHYbuEzXWBVGp4EKXWq8-xlwN3PTFQT9C8QwIhtiu93YguzKVdUhVlt6Z9Yl-Ef_jAuxAJPqaf5Bo8r2I0L78HLjSyJyI2CkPaKxwwFSKGojLhhrSzXuzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e8a0de94.mp4?token=CQqIyIj1blL1fCsZTYfQqnZOBwr5oUklH-Vc9wq-xySG0tBVSKw2EJNhtOWuI7E6UzWPTNAdltA5sCQbX3ho7PWwLrATFb2Pkr1QeCNesiEGYrrpeAylMGAWTAqromPxo2mbsdZ1lPOp-xLyGIQ7_kUv0QEL8PgNtQ6CIpWITkgiWjhGIwJfdC3BAbyq2JZ5wA7AI5PCVOjpLWFDUx64rYPiuvItsEL-EXxzOAVDkxxtGKvMSqY096ghRiPM5M55v03NBobduuGLdYrWNFr1RgZgtw7QYOESpFVPaPp5mJ_qaQK1L3TCcuqNBP1UQVRrc4YNfm2gAbv_ioceT1gDMYWyrieLrnYSD4M5blp9jQYZwxQuF7xIgPqKmLahZqjHZGJ6rNz_Glk0LbekV2KkHvp728beXTH9oTbIPfPsGjxnzTprEcDZa5z38OlAM-BULNVfKZHbLAu-udKd8JDgJHvkAGi2eqDlIAuTTpA7L7djqMCDwjRC0kr1cB3v79L7oZ_p4mDqKLoE9Q608WQXMc5_qAhNqFlQlQoD0yTExiR0pxfqjKBqNIHYbuEzXWBVGp4EKXWq8-xlwN3PTFQT9C8QwIhtiu93YguzKVdUhVlt6Z9Yl-Ef_jAuxAJPqaf5Bo8r2I0L78HLjSyJyI2CkPaKxwwFSKGojLhhrSzXuzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دموکرات‌ها: منتظر روزی هستم که دیگر آن‌ها را «دموکرات‌های احمق» صدا نکنم. و این اتفاق نخواهد افتاد مگر اینکه آن‌ها وظیفه‌شان را انجام دهند.
🔴
اگر بخواهند جرم را متوقف کنند، اگر بخواهند مالیات‌ها را کاهش دهند، اگر بخواهند آموزش عمومی و کارهای خوب را انجام دهند. کارهای زیادی هست که می‌توانیم با هم انجام دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126866" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126865">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55f3e4309.mp4?token=OVQLEG22xGDzst9RLGhdqRZDNQ8T01lfZ94j7yDL2h3-r-A-Arz1EgykWAlcxC4vBKG2TcdRJmpGZH2c0kf60N2oNHjWoEuuhoy_F98Yk4IOvH678I0ea4JoXMb4XG6UB9LeUImS7aIJKKjWyJtWTj9n44ehLnCpSVVgr1ahv_1kb3COG47hoTx5LRGqoDddF3PNxJjgxnulvBn0CSJBcFXuCPp0qhdhLqfISlzUGSV3V7kUQomZgOkhWeeSo9rycS_frfGt8mb_ihK4j7es9SY4M9H5xpG0DNVYQrwXybPsLaWGJQuZsVvsaRFg2STXFKoT2yGmgMyE7pUdI5JOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55f3e4309.mp4?token=OVQLEG22xGDzst9RLGhdqRZDNQ8T01lfZ94j7yDL2h3-r-A-Arz1EgykWAlcxC4vBKG2TcdRJmpGZH2c0kf60N2oNHjWoEuuhoy_F98Yk4IOvH678I0ea4JoXMb4XG6UB9LeUImS7aIJKKjWyJtWTj9n44ehLnCpSVVgr1ahv_1kb3COG47hoTx5LRGqoDddF3PNxJjgxnulvBn0CSJBcFXuCPp0qhdhLqfISlzUGSV3V7kUQomZgOkhWeeSo9rycS_frfGt8mb_ihK4j7es9SY4M9H5xpG0DNVYQrwXybPsLaWGJQuZsVvsaRFg2STXFKoT2yGmgMyE7pUdI5JOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شومر به خاطر این و آن دیوانه می‌شود، یا اپستین، اپستین، اپستین!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126865" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126864">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfc8df3d6.mp4?token=vPnQHLOjOX06lZnHDV_Dqfc53E0TMRiyNWEp8QwGzXpWrIx2lwBvooDV4YIRXDBITnd61rqmUTUJorAcBD5cQ3LtSASTYikgZ0Vk8lXFFJzsjBPdB-YmQ_-8cze601sQ1KgEUgauHXRf61UsW9jvTw2JQYG1p8p3hP5KPBURrZKA4tc0HPhr0SPG6m232FYtGTjmdaDhWZOeY0L5rpK5EwkyIXFb7dPkXrgMi-Ii_f-JWu94rE-U6-5hU4JMgGclAl0PJ7XCpx-N6gymZ9gD7txfsy0AIybEgt2eix4ejlxXHNczFR8Bev7V870B3FENM_tJg7FHjCGuJLEhNXhD0UDtHqUqTJJuCvbpikbXJCjMvXqfRKccOIMMRdcKvXHIg1-qOtty8nVM347HgH6Tb3ndk-yXOeK1K7mQfqLrBzbnLclYfICkZ0JdK5KI6SlhkwsBwNyIhd3gm3H8XO_g_Qfk8aRfBWraHkrVBp_-0Fx9RElc9qiFKBmnIA1-eglAJ-CG-NVRXGDIdm123kSu3tvNyKTpeCHRLnlc7upN97mSqgwhvM8ABWjSB0F9zimIzH3sGEJsKUxiDWL40RS_44x7UAsp97AbFyPegx87We1qQENDTuIs3F8ui3K4M9fbqY7aN25toWjWTNXsL2wpzVxHka-TtA7pxHk8kay78bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfc8df3d6.mp4?token=vPnQHLOjOX06lZnHDV_Dqfc53E0TMRiyNWEp8QwGzXpWrIx2lwBvooDV4YIRXDBITnd61rqmUTUJorAcBD5cQ3LtSASTYikgZ0Vk8lXFFJzsjBPdB-YmQ_-8cze601sQ1KgEUgauHXRf61UsW9jvTw2JQYG1p8p3hP5KPBURrZKA4tc0HPhr0SPG6m232FYtGTjmdaDhWZOeY0L5rpK5EwkyIXFb7dPkXrgMi-Ii_f-JWu94rE-U6-5hU4JMgGclAl0PJ7XCpx-N6gymZ9gD7txfsy0AIybEgt2eix4ejlxXHNczFR8Bev7V870B3FENM_tJg7FHjCGuJLEhNXhD0UDtHqUqTJJuCvbpikbXJCjMvXqfRKccOIMMRdcKvXHIg1-qOtty8nVM347HgH6Tb3ndk-yXOeK1K7mQfqLrBzbnLclYfICkZ0JdK5KI6SlhkwsBwNyIhd3gm3H8XO_g_Qfk8aRfBWraHkrVBp_-0Fx9RElc9qiFKBmnIA1-eglAJ-CG-NVRXGDIdm123kSu3tvNyKTpeCHRLnlc7upN97mSqgwhvM8ABWjSB0F9zimIzH3sGEJsKUxiDWL40RS_44x7UAsp97AbFyPegx87We1qQENDTuIs3F8ui3K4M9fbqY7aN25toWjWTNXsL2wpzVxHka-TtA7pxHk8kay78bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره گراهام پلاتنر: او یک اوباش است. احتمالاً بدتر از هر انسانی است که تاکنون برای مقام انتخاب شده است.
🔴
من او را نمی‌شناسم. نمی‌خواهم بد بگویم، اما هیچ‌کس سابقه‌ای مانند او نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126864" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126863">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ونس: توافق با ایران باید از نظر اقتصادی به نفع آمریکا باشد
🔴
جی دی ونس، معاون رئیس جمهور آمریکا: احساس می‌کنم در موقعیتی هستیم که بتوانیم به توافقی دست یابیم که از نظر اقتصادی به نفع آمریکا باشد و واقعاً موضوع برنامه هسته‌ای ایران را نه فقط در حال حاضر، نه فقط تا وقتی که دونالد ترامپ رئیس‌جمهور است، بلکه در بلندمدت حل کند.
🔴
عدم برخورداری ایران از سلاح اتمی، سیاست ماست و فکر می‌کنم بسیار به رسیدن به آن هدف نزدیک شده‌ایم، اما هنوز مقداری کار دشوار باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126863" target="_blank">📅 19:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126862">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cef8fd5d.mp4?token=jLnu5gr2TVcnLlbVaOrAT94_c6WMhKk2wpgoW7aFj_8HuNjipXg9KqHCca_26zNHVnydzoBeIJ5sXWiqPstqdqNCBYULurdilQGrI7gl-75UcyWcF258c7sNlkZcFisdVdqsPG7TX_iP526an4no2O3LMb8wGjT3hqF_ir3ICBO1M1yhJF2aqJBx4F_Jkr842YQVbxEHSKG3l7CBkNGf8xUeSJGIDXrqzNmbfP67jMHoWdGHrL7_rjgTe-J_iMvJ3TPxK6s_6QZzZ3Nj_FkI3d3EReJYzJ5AFAKgnGQQRzbxr9aDXz8r0U_Jf09aaW6grPP_dAgsz4QrLQQbHHoZ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cef8fd5d.mp4?token=jLnu5gr2TVcnLlbVaOrAT94_c6WMhKk2wpgoW7aFj_8HuNjipXg9KqHCca_26zNHVnydzoBeIJ5sXWiqPstqdqNCBYULurdilQGrI7gl-75UcyWcF258c7sNlkZcFisdVdqsPG7TX_iP526an4no2O3LMb8wGjT3hqF_ir3ICBO1M1yhJF2aqJBx4F_Jkr842YQVbxEHSKG3l7CBkNGf8xUeSJGIDXrqzNmbfP67jMHoWdGHrL7_rjgTe-J_iMvJ3TPxK6s_6QZzZ3Nj_FkI3d3EReJYzJ5AFAKgnGQQRzbxr9aDXz8r0U_Jf09aaW6grPP_dAgsz4QrLQQbHHoZ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما جریان فنتانیل را از مرزهایمان تقریباً ۶۰ درصد کاهش دادیم.
🔴
از طریق دریا، ۹۷ درصد. ما به دنبال آن ۳ درصد باقی‌مانده هستیم، زیرا فکر می‌کنیم آن‌ها از شجاع‌ترین افراد هستند.
🔴
متاسفانه باید به مکزیک بگویم که اکنون تمرکز ما بر ورود از طریق خشکی است.
🔴
بخش زیادی از آن از طریق دریا وارد می‌شد، درصدی بسیار بزرگتر از آنچه کسی می‌دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126862" target="_blank">📅 19:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126861">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de8ebd6c8.mp4?token=Agrq4yfZCVlQN9quHsQiRkdBEWLle9maC_QOVfbBGJr4HsedhHMoRe7EBtbbpdfxv7LKReaw80dbxSp15vG6k_TkobuEx_EDYWCsV4CCwj_Pgk68Yjnurcb0Ufcds1N3vCQCECsrgKKp1Cc8JCyReUPGKE7SrFld0JykTJ1r7ayxl4XpC9C9fOeZROKYMw7bLLoNo-p8L9YGi9eVrFCPOOTwBZY3bDdDw-kR2QsAG6tSxLFvxj7olxuRaVJu-psuo3qeMQAtKR-WjlHK82I8RX242rZA4Qv2XqFdWZ9WOhUw2WVa8kMYmn70wC8ay092AWQm6jRuk-4uudA9QM4ScrFrRsg4CGGEFCX3UxGdhRVxY_6Hv88Alyw_5ztgATDLW_G9U765JZTQJU9YeCkP_k3v39V5ehjItrBe_hV4bkXNLoUzPiPIh5x5HkbQ9yaI00ANLuuxOjJLiUsOSATKF4OfdS6FJOxo9rpSr_fbN13ruwKmZxajruQsO_WWdaH82kFx_FOtNu5umUh5stdjXRyS4HEF6C7BGQSG-1FfmLn9G0JBIopv_jAszqfNf4eMF56FIukrxfAvFzD6SkiO1Ar2V7rq3xtxuXeqEU3EPJ6YP37GGkfVTyQroGq6EpbN6Ok6UUUP8z0BcpKuYZVc4zbhwnq4SQLp69YvqMh4djQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de8ebd6c8.mp4?token=Agrq4yfZCVlQN9quHsQiRkdBEWLle9maC_QOVfbBGJr4HsedhHMoRe7EBtbbpdfxv7LKReaw80dbxSp15vG6k_TkobuEx_EDYWCsV4CCwj_Pgk68Yjnurcb0Ufcds1N3vCQCECsrgKKp1Cc8JCyReUPGKE7SrFld0JykTJ1r7ayxl4XpC9C9fOeZROKYMw7bLLoNo-p8L9YGi9eVrFCPOOTwBZY3bDdDw-kR2QsAG6tSxLFvxj7olxuRaVJu-psuo3qeMQAtKR-WjlHK82I8RX242rZA4Qv2XqFdWZ9WOhUw2WVa8kMYmn70wC8ay092AWQm6jRuk-4uudA9QM4ScrFrRsg4CGGEFCX3UxGdhRVxY_6Hv88Alyw_5ztgATDLW_G9U765JZTQJU9YeCkP_k3v39V5ehjItrBe_hV4bkXNLoUzPiPIh5x5HkbQ9yaI00ANLuuxOjJLiUsOSATKF4OfdS6FJOxo9rpSr_fbN13ruwKmZxajruQsO_WWdaH82kFx_FOtNu5umUh5stdjXRyS4HEF6C7BGQSG-1FfmLn9G0JBIopv_jAszqfNf4eMF56FIukrxfAvFzD6SkiO1Ar2V7rq3xtxuXeqEU3EPJ6YP37GGkfVTyQroGq6EpbN6Ok6UUUP8z0BcpKuYZVc4zbhwnq4SQLp69YvqMh4djQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام:‌ می‌خواهم از شخص بزرگ، خدا تشکر کنم. بعدش از ترامپ. آقای رئیس‌جمهور، شما از خدا دور نیستید، اما ما با او شروع می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126861" target="_blank">📅 19:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ درباره استخر بازتاب یادبود لینکلن: این طولانی‌ترین استخر جهان است، سه یا چهار برابر بیشتر.
🔴
جایی است که مارتین لوتر کینگ سخنرانی بزرگ خود را انجام داد و می‌گویند یک میلیون نفر حضور داشتند.
🔴
و من چند سال پیش در چهارم ژوئیه آنجا سخنرانی کردم و جمعیت زیادی بود.
🔴
و گفتند من ۲۵۰۰۰ نفر داشتم. گفتند او یک میلیون نفر داشت. اما وقتی به عکس نگاه می‌کنید، من گفتم، «صبر کنید، مردم در سخنرانی من حتی فشرده‌تر بودند. من بیشتر از او جمعیت داشتم.»
🔴
اما گفتند من ۲۵۰۰۰ نفر داشتم و او یک میلیون. اما من نمی‌خواهم با مارتین لوتر کینگ بحث کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126860" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126859">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc565a1c0d.mp4?token=kX58ntKn9tQqqxiFFl0tYB-WYvydhfgndXHJyJJKu6n_3Ur-59RtXOWjzUYFHzaJ1gaI4FpV-nljMDvtCGxK3nsaI1SuZew0NYVeAYB-PiACvnjo54opgpY5NtjzX-JgifoKkjobdevQL7zXJY0bkZ4JaQAW9nXLgb0yuRTNSH7QJGazEDSkzdv07qweY8JdcY2bIUxdCNjo88C1vJbbAcr6UuUUbgZ8SDzJMIIuC8V74CSwsW0dQy7vcCNTxVmBK269qX_F-eDvtuRuiWjaKQwoxyz55HxiuB8n2K9gyLnnbACsSqWhA2D9KJIEHCzZHat_3FpPNZOnRG2afp1Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc565a1c0d.mp4?token=kX58ntKn9tQqqxiFFl0tYB-WYvydhfgndXHJyJJKu6n_3Ur-59RtXOWjzUYFHzaJ1gaI4FpV-nljMDvtCGxK3nsaI1SuZew0NYVeAYB-PiACvnjo54opgpY5NtjzX-JgifoKkjobdevQL7zXJY0bkZ4JaQAW9nXLgb0yuRTNSH7QJGazEDSkzdv07qweY8JdcY2bIUxdCNjo88C1vJbbAcr6UuUUbgZ8SDzJMIIuC8V74CSwsW0dQy7vcCNTxVmBK269qX_F-eDvtuRuiWjaKQwoxyz55HxiuB8n2K9gyLnnbACsSqWhA2D9KJIEHCzZHat_3FpPNZOnRG2afp1Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث به همراه نیروهای آمریکایی در پایگاه گوانتانامو به تمرین می‌پردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126859" target="_blank">📅 19:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126858">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTb4EXJ6iNeIWZmlA7714GxK6xbqbi6tlbYJjluNjjlJGXwLeCzZY4ls8Kzw4m_V-fnLUtnQsKMIPDhbcf8CmVALXAKRNdWT3X3jdJOfxVTyue1B6T3ujzTh9MxY_SMDJK58ylgtcqJdy82BHQD7ArcTP0ynYpBmqa7BK3326nn2imiP-Q5II-RLilMbJSM9WHzxPF-gaCMAUf0gs0kZaLesBdAg0JCT11TyhvsRwQs5xzq6pRFzYGnZCAK2A3IQiF3sJA94yFF_dqqVPx2hy_h4v8g6iVgXTf-mG27nBXTh_UyWkf6hCBx4-xnOnwMWlnntyCBdAw7sGLO2xe2V6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏سید حمزه صفوی، تحلیل‌گر: وقتی رهبر انقلاب شهید شدند، صداوسیما اعلام کرد که مردم به ما اعتماد کنید. رهبری زنده هستند! و بعد دیدیم که رسانه اسراییلی خبر داد ایشان شهید شده است. این وضع صداوسیما است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126858" target="_blank">📅 19:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126857">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5ZZeyagje-xDNEugajeKivl6WVqbyLvxp9pSLahQKvO2_zQ7Buu8QoYjlJRBqym4idcL1HToV40iM-K8phO8P9uWb43i639oIM-hechhU49RvhoTsPi1gd-Uz5hnigS4Z1cqgw-WRAHSO72lAUzbCE530QBrj6oI6BIrNKHe99bmbEMq_jEghlZHUekycJSFFKwZzq5x2I6CINgDrLXUXpDMrz58ypoIjWRkx9cdQLxH_y1StVDN7j0F1z0qEEiRlk4R9y9tHzKhP2YHcTDW7gt440aywjKbWTuzmOLxsYmo5Ta-ttGKpY-5UW2EeM_fGyLwBCQVq3rDX1qsPf3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هنوز نگران تموم شدن حجمت هستی
😱
یا استرس ضریب و تایمشو داری؟؟
🥸
کافیه اشتراک TVPN رو تهیه کنی
نامحدود واقعی با ساب
🔥
که دیگه نه نگران حجم باشی نه تایم
🎈
اشتراک نامحدود فقط 290t
🎁
😀
حجمی از گیگی 2t
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126857" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126856">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126856" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126855">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نمایندگی‌های ایران، روسیه و چین در بیانیه‌ای مشترک در جلسه شورای حکام:
قطعنامه پیشنهادی آمریکا علیه ایران در شورای حکام ماهیتی سیاسی و غیرسازنده دارد که اوضاع شکننده کنونی را بدتر می‌کند.
🔴
با هرگونه تلاش برای گمراه کردن کشورهای عضو آژانس نسبت به وضعیت واقعی برنامه هسته‌ای ایران، از جمله از طریق گزارش‌های مدیرکل مخالفند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126855" target="_blank">📅 18:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126854">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/هم اکنون هواپیماهای سوخت رسان آمریکایی از آلمان به سمت خاورمیانه در حال حرکت می‌باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126854" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbwUvjd16IDduWcKcThuNsYmEAEblKENZQwBWuO6gMuWiItiC2jZ-0QGZ9yzlcwd3V2-_3QYU2X_It6unD-uCRVfKPsPjo396JnUmF2gzBC5ILAO2O8eihdXGAQtEUBtc027CsdSaVDxGY75wihSjNhH-8UV5oqEDvQhNQkxko7mpMJ83I-zbsYY_jHH4rObjn0v_P4YglGBAsFsZfXmQtVOdObYY_n4IPtklaYPY5UGL90pdu9_R9hBYeGSun72Y8wGfM0s_j8r4o1bOYMallx_XPfNFaZWheV4GSvtKAnI9L1BnAk3l5UCO2oT4_aMRxzqg3tdDndfO9c3vNuJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQOSnwLiXXV0FLnTTp8qdiRUZQFPpjw1rcsDz3WWvODhblSfkQyv2ja4BOFOcrhwA9G3yBliIntRRhSLQIeMlnQrlbeRlWZbK1sxIfuRcEGeMcKap0d0m6rGsuLwbqp3LDrK1lynziMKHHjWCcX-IpsavW2vkliRyMXGtHtxY4wBUy9p8uy-F9PwQbFy-KpI1BCsT_VOEbJxBm00GgdXUvDE9AO7tQ0HSkkB7rZfpRnVVb8RqB16xyvotj-PqQ8P6J_lmyiPYdm9s3kFxgo65tVrJPVkP9ONlZzzP5iMV-1U8V949BX8qTwme9ykKz1YPn_JbX1udp9kzdWLrBXt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkGSr28nLyS7-27EXo-8GPIIZR0Tsn1p774ddeNb4I9LJc8KQOzNNkZyZRrWk1F6WO6xTMtwYzHYntoFx5k4btXZMqE3k9mTszlUXh1irnFX1PiqDPTTO49DXiTvgNfOxDogLNNnqFWVMYN9O43B73gu18qcHuVT6jd-fn_i_3YElqI4GflKizuivcG-XqkhVjMh0T4Zxa6XqHLrHp0Qjar9ELXk77DYu--qMiGlrZKMRdS1z33Ii0GE4fo4Ae0EpEn9pPRJzVRBSMBHFZ00caV3yNVjQzEXRVO3bIZY5p-1c2QpRtNoDPlm6Ag7UFmPO5MqRlZ8x7gsF_keS1PA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYMy8dc50y3BC93eOzn0OUN2xbBPSqDy-EYJsPul15mG4C33VCgBk2ZQbQcEnIreezZjSnXmmPrJJTCJaOOYNvmbnTyRdS7zx-uqVUJ4X-lw4JOHdBWm2jfZQj_rw8Ta6W8na7_feJ4uZx2fEQcTnmRzfsHJceC8BlKKzXi4M8v99_RGvSYxkpmD2ISMD2ZCBZM3CGHwuboT1pk5032nVP1-2ibhioQuqtk72bAtDzSRC2RI8cajUUW1CFVVzt3KatMFOdyYrub7r41iEG0VvGXV6tku2jb0RlEKVqN2Y7JwVq4Oig4tHK4I8Kj6_P4aDsRl5HIYQ5rH_QWmwC84OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در جنوب لبنان ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126850" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
