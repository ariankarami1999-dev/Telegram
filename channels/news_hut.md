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
<img src="https://cdn4.telesco.pe/file/rMEG76iajonlWiNtrKEY-iWZS2msMguS0BxNsEoi--vUNeeqQjaWTP3R1bHHXD17OVHycY6NUxXwL5B7aF1Jef_G1JLbC3sOJdhiHlvtizLgr5kySoXnXgjgMGhff19vkN-iMe5Lj5avvCQIdXPK_mqp0BGnVivVCKP4sHnsDuqSKSrihYA1R6Y51_U3rkuaUEHG5qDiMwzXuhrFaDXlp5pDWet15AfRUUQvMCEFEIVJ4pJCBzFfSgEN1x4EwvW5IZIyUy94rc4bRdx5ePy50qS4e5miM-dLqdPrQKgMkSTosiFtR2Dk0_EWsUIkLhp6obUy2kLQPL-VC9il3EimaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=pHHov_rkjbth0EWTAtbPbcMV0Ut0arFd3sMkFoPvr9t24KlCN6lKIaBUt_-AkiLnhEdaF9fVjx9H8ah0ScEZlUlRuStu2kgC_1wwrFQJdTbNaGalUMFsXjr-GH11l_nJ3sFBgBH6zjGHQAgEUSWy_zdzaZb_uQL1MPHpPXUJbnFP8zdvlKL9z4lT-mvVu294NYzVq_czLuTIZijnxhUdBbG7Vlpe1uEKWReBdDyM_mpy31oiurErTPriZ0L4NAJM661TgYOa6fc7i29r37f20CPXw2TZIiHe09vFNbNjQnNYK16iVQbRj19ZUn1-iR5lVa3RobNBAh1YThQS28ORqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=pHHov_rkjbth0EWTAtbPbcMV0Ut0arFd3sMkFoPvr9t24KlCN6lKIaBUt_-AkiLnhEdaF9fVjx9H8ah0ScEZlUlRuStu2kgC_1wwrFQJdTbNaGalUMFsXjr-GH11l_nJ3sFBgBH6zjGHQAgEUSWy_zdzaZb_uQL1MPHpPXUJbnFP8zdvlKL9z4lT-mvVu294NYzVq_czLuTIZijnxhUdBbG7Vlpe1uEKWReBdDyM_mpy31oiurErTPriZ0L4NAJM661TgYOa6fc7i29r37f20CPXw2TZIiHe09vFNbNjQnNYK16iVQbRj19ZUn1-iR5lVa3RobNBAh1YThQS28ORqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhhsewN77S3JCMK5--mbQQEXD0bIjeiBHmxqQBGX2bPufWw3d84DiOX_REqNta-042XdEHUlOulmelLCJ_9-fvXTGkWrIV6-tNXYSkfcsvNbDUJzy8qQYmV5GK0xks8bofxbQBGEifxahwMpgTk4qDgO1fRH9R4mCx-NznpM32lwBqQyYPUxqLftiPOQe__awdugfIy8YVownQSKN0x7_N_DEKRjc2Cs5k3GL2Z9VO6SktMeD-HdZcOgjdZrN2s3RWaWzVTXrylRiwEuI2cTawdYDgqMQcOoyU9TF1KuCVUV7T8Zut9NfUHVvbu8Vx_0q7rNiBxQjSqPm-yBMeqbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ8AmelYGZd4b0EUH0FNnNjWv0nh3sVQs0bUz2AyQ7Cc8tBmkTAzhA8A9svfiNkBfki_LeJiyLQCv7pH9vg5ax7dcwejlGVxa6etJdT6F1IZ552jbhpTv50IRAD725VxuMB2gopY3N4cYnOpQDGNowFA8kOuDyMuvLAibB-xUiVdN3FA4u_gK7DH8B3SVRy1dfzSGtWbhc9rXXEbAzUBF2GtATk9oirXYzZKzMmUbjnYqjkYQ6YWcrVFC6gcWEWeehwyYthL64H4cpLMOUIECq2V0mjqp7AX8V_s9hpI17SekKWE2-BXaB0V6JX0GhTWsfoOSRoUVk7wtk08Je2nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaFz4c_4si9iZVxGT7JafsY5om9ccGzjC_89NuMmXvDg9Dw6mY-sB5YE0j-IWjqIMcrtJWBFEA6F27AAliJtFDLvBg6poL8Cvu27NWmgywuF5XN4CWZbYgTtc_9Yk61XMAViknQZe9TICSE0MFHjG9CtIwBjK4pQe1FI7gfUrKeTT_XCWZcIIMLfvFSjAYluLLz0tkKauMM8rzrpLEkWtyOxfXTqh-mgeGWlq3lV7kMcn5ZYja6A9dSIZKyzvwIF9U5iMWZ71I-sVRQc3jUAWasASkoFM_6XeSlhedGc3NGES72uc-MA1I3ZH9H_u033KACgJzJERUUIXr2ivOSvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq6vohSwkKAL9z1OQKzdF7PsKMVcNHeqKZyH6JvUnjctqY56YZxlkruBOaPzhY_aZUJLq4NZp-SwA3BMOBGz8DwdzlDQ8va1ovZD-kplh-ztr6eK2IrI43_QAto7cHZxQNiiKjBfjwjnqpzSR-gzTUfDk19kKootoB5Z2IZ2_v7WDonk6DyqvSy_TWvsjz5_Vkt8f4zuCSmb0ywjSESODFu5sqVFg-EHb9jgxjlGJGOT6hCA2VCZkbkuFAbd5bjdAi6OWzx4Y0OtSApwWCPKCfEUtoaD1oZ2H911RPuz-nEca2Swtwa9A_jiPTfEGkJbzRjZLVAVg0MHj3FtEN2iIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCxXac_zNnl45svKhFPglqSnncLHoODkN5HDEMdkqLdZP0LYNCcTjP5sbHI0HXV5pb-WEClF3GoocJRMGGiy4XY30qNRjYK9G9AvRGab-O_0n5xGxdYW98PK4xOJvyHOJCTSOAh7S3Quo4n3xe--t7vKIRMs4XMncDlXhXj4HuTSS3gT6y-nbpCryB5RrsR4gNsZjKOg1icIh2GU9O2sotOCYoBO0neLogD6Fv3moE2LDhg9SHcelqhZT9gLJDSyYukZaHdfTqrFfL3I5HXu616T9fios0nUwfy-fSJOMsblpjL3cUIM1dCiwY3u2Ek2f5mNowxwQ7sAdclH0wxD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq6ULdlFhnEhziVgbmQ09BB3c4hgM1hNlMEtRdL2hNEi63picREQkWs23BpRZJBnZh5UqX-Jk10i_EjVHNb8pIJH-SkIXiWsW6BeI4FkvLCj44alEAcC4pv53OXUwefiqFR2vm7EyUScNtv87tq5qEf2w5SGf1yOOthG6jPoM-2kqsVQSFaDu9jYWh9gwAUQ6NKPtFLNofi_ES7FDZauqtJQoExDIxKG617eYID1eX6hM5D1URRpbpBHXYfh3mKeOUePZsIXGViHLTNyf8_uhGOFe3J3JN4Btt7sBXaUYwidv9IubK-0NxllHdcKxQ6C5tCmuGKEjgGHGySeNwhzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=DLRQxXNfjLxgYkeuLuYlTx5Jacd-tk1L0XKgnxYtfhbuRt_U8FxRWvhkDJ2MMa6N4B80_3AVv2iGXF1aTe_UkCDSpiwrYlNUoKh709eLalBG4s041Cwqc-bsNQGkl-Uf2x-DHfFOWTz-2LOkFJJS7klM3BBi_MvXWRdcD8uoY-Fyd7AzAdaHCVQrkE172-HOMUvhOifHTzVmKTFjih21WHTUzcz2gA5UeFeWA2j6qRZojc3-fwOtUi0L1LhDE4fKk9DxYZ2-Cr6lJVOKEoxjGuteQ0Cc7ISDxMTZCcdVBwHnjnDzGnhAgpYYob_NHbXHUB0Xwfn-hi8udigKJh1EXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=DLRQxXNfjLxgYkeuLuYlTx5Jacd-tk1L0XKgnxYtfhbuRt_U8FxRWvhkDJ2MMa6N4B80_3AVv2iGXF1aTe_UkCDSpiwrYlNUoKh709eLalBG4s041Cwqc-bsNQGkl-Uf2x-DHfFOWTz-2LOkFJJS7klM3BBi_MvXWRdcD8uoY-Fyd7AzAdaHCVQrkE172-HOMUvhOifHTzVmKTFjih21WHTUzcz2gA5UeFeWA2j6qRZojc3-fwOtUi0L1LhDE4fKk9DxYZ2-Cr6lJVOKEoxjGuteQ0Cc7ISDxMTZCcdVBwHnjnDzGnhAgpYYob_NHbXHUB0Xwfn-hi8udigKJh1EXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=cnSfroYuVfg6WH-oxSOsiELa6IlFemVRNaa1aLKYtKujInFXX6luV1R9uS7FT0L4ue9m3LgN1ySX8dwhIRhN0hzuveSFsm9YQk7lBrVuOjsY41WBozQ-7tIOJOONmCi79c_c9HdcqJWIUJ_HOUkJDwua8SUMsXd5r01Y5dEN4zah4-3tZJO_3Jmq_WwEPfiTnyHrYZxoe-ii5K3sd7bAPBXXQ_pn6ZO7deFNUeMmQeAlfr0ah29pCgOzQkHbXBWsJ8QwPlJWkGe34Lsznhjumy3oBwjWndbO7oiMtpw0HtaatlaR_V13-sV8ow8U-MEzVun6DbcgS6PXFuXZqYEgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=cnSfroYuVfg6WH-oxSOsiELa6IlFemVRNaa1aLKYtKujInFXX6luV1R9uS7FT0L4ue9m3LgN1ySX8dwhIRhN0hzuveSFsm9YQk7lBrVuOjsY41WBozQ-7tIOJOONmCi79c_c9HdcqJWIUJ_HOUkJDwua8SUMsXd5r01Y5dEN4zah4-3tZJO_3Jmq_WwEPfiTnyHrYZxoe-ii5K3sd7bAPBXXQ_pn6ZO7deFNUeMmQeAlfr0ah29pCgOzQkHbXBWsJ8QwPlJWkGe34Lsznhjumy3oBwjWndbO7oiMtpw0HtaatlaR_V13-sV8ow8U-MEzVun6DbcgS6PXFuXZqYEgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldiDkbc6eExTlC4Iz-nDxErEz8sSmos6uRPXqcmg41WLGcKlk7U5QitP2Wk4fhn2YnEpVsXsizh8WzdV5DyOCexEURGC_svGZFMnZZ7QmGOn6-36lRYV8u3r3eOLQJGfYVWv4I6KzszYttn4PFvZ0yJXWZDt2np-YWLuuscEjDYuI3uE7BAJ_Rxu8PKTaiLbsPVcXyygixIMcXD3MPvIhF1cZIDSfzNeAIGo46-IfnWestFK7EPR3tVE1vrUpkkMlrbnKVmyXLxAjYh4husvA9a3ugOeIjYhvQKfMmM8OY26NW8YNX0Z_mNPZjAaN-kcTVdMNthiQopi3LomL-3IOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=PqyihOlIEdyrjezSCJ1jOBtEmbXgbhROwNvOzrYrOH8bI-eHURr5-nNFrgfLrUrkQ0FxouDcUQtLcy9W8WwWFN68wYHoGnEz149_L8OE53nh1EfgEHrmibdkwhagKUKMULHQXc2UD09sKyLB91aWQDidcSj0JAwkZ-xC5YfrI4hQh0R_IH-h8xH0168kR-2k-ks2ilzjdBXYvbD5BrsEiZGmQxLSiVX6DPjtYKn1puWDRqnqTlSActWJnWlpUSMErza1vZYG55Pvrb7MbnFlXoTxCXBKyc2v6RwSBv9vYyMdk_rED7HyjHiI494MiHz2qMYcbVPdDUvBGByCQZRda0xBfLbOBRCQRJQBFfDEGml6VnikCgA4mN517ISMphUlwwuPzPanWYOrFT617BECqrgNR_4WyOjvzvxvFRTrApkf3mRLM6Pck6SCROzCta6HY1NvBBEFIfhS7lrVfh9ul7I00CzgsJgGpKyXhUGwZ0xKd0z3ShUYZba2m6QY1Mgao4Qs9TB9WIDVtIHSQO77UsnpDdUMboM9-xSHYvR85TtA0UEDuXeJD69eNVVQ_iykoYIwoyd4MAx8nq-2ZDYLKDlyepGdQ539QopVIEA3L0lDXxdSMKZSz16mnHDTLQhUXa60XoJBY8hB_XOHsbQsDVO_oYWDi6rZqLbtcAxapV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=PqyihOlIEdyrjezSCJ1jOBtEmbXgbhROwNvOzrYrOH8bI-eHURr5-nNFrgfLrUrkQ0FxouDcUQtLcy9W8WwWFN68wYHoGnEz149_L8OE53nh1EfgEHrmibdkwhagKUKMULHQXc2UD09sKyLB91aWQDidcSj0JAwkZ-xC5YfrI4hQh0R_IH-h8xH0168kR-2k-ks2ilzjdBXYvbD5BrsEiZGmQxLSiVX6DPjtYKn1puWDRqnqTlSActWJnWlpUSMErza1vZYG55Pvrb7MbnFlXoTxCXBKyc2v6RwSBv9vYyMdk_rED7HyjHiI494MiHz2qMYcbVPdDUvBGByCQZRda0xBfLbOBRCQRJQBFfDEGml6VnikCgA4mN517ISMphUlwwuPzPanWYOrFT617BECqrgNR_4WyOjvzvxvFRTrApkf3mRLM6Pck6SCROzCta6HY1NvBBEFIfhS7lrVfh9ul7I00CzgsJgGpKyXhUGwZ0xKd0z3ShUYZba2m6QY1Mgao4Qs9TB9WIDVtIHSQO77UsnpDdUMboM9-xSHYvR85TtA0UEDuXeJD69eNVVQ_iykoYIwoyd4MAx8nq-2ZDYLKDlyepGdQ539QopVIEA3L0lDXxdSMKZSz16mnHDTLQhUXa60XoJBY8hB_XOHsbQsDVO_oYWDi6rZqLbtcAxapV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeHe7aTZZWGKVDxsOQNpIdHZ6DMm8pAp1wj59PH8C7FeghNjRl1tPP2dG3KafdtDXvm6HOZcQmHZwgL4MXRfwdQivTfjgcP_AV3yHVfebD9591CAX63aj349oU0a8QfiXHB1QZBFq7Q0YYclVlswd8aMStG3QDPuUrR1gmdXNIJYjMTD0F7Er017FHIGJWqsnt24Eawm4gGsl7oB8XrZbD_BgVpcCjfOhUSCkBoY6n5Q9fF_-NAuSGfSFpIUdvuWbkFsyinBlgkRn_uNuXx2UTDvYQFre9N2K0hayciUOqveVJEPtML7XK_8uUA2pCtIafwYQRsSGH8-mhO8nsM8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65872">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65872" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65871">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65871" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
دفتر امیر قطر: تمامی کشورهای منطقه در خصوص تفاهم ایران و آمریکا رضایت دارند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65870" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65869">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65869" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65867">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی فارس:
‌ منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی در شبکه اجتماعی تروث سوشال ادعا کرده بود که ایران در عالی‌ترین سطح با متنی برای یادداشت تفاهم اولیه موافقت کرده است.
وی دقایقی بعد در اظهاراتی مشابه خطاب به روزنامه آمریکایی نیویورک‌پست هم گفت که متن مزبور جمع‌بندی شده است.
ادعای ترامپ در حالی مطرح می‌شود که ایران و آمریکا بامداد پنجشنبه یکی از شدیدترین درگیری‌های خود را پس از اعلام آتش‌بس پشت سر گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65867" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65866">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
آکسیوس:
به گفته سه منبع آگاه از مذاکرات، قطری‌ها و ایرانی‌ها روز چهارشنبه معتقد بودند که به متن مورد توافقی رسیده‌اند که آمریکا نیز آن را خواهد پذیرفت.
این منابع گفتند که اختلاف‌ها در سه موضوع کلیدی کاهش یافته است:
سازوکار آزادسازی دارایی‌های مسدود شده ایران - مهمترین مسئله برای ایرانی‌ها.
تمهیداتی برای بازگشایی تنگه هرمز در طول دوره آتش‌بس ۶۰ روزه.
چگونگی انجام مذاکرات بر سر برنامه هسته‌ای ایران در طول دوره آتش‌بس ۶۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65866" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65865">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65865" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65864">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ به نیویورک پست : توافق «بلند مدت» با ایران تقریبا نهایی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65864" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65863">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65863" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65862">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports
(بدون VPN)
Bein Sports
(بدون VPN)
لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65862" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65860">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gC20_C2FvuIPygLZOg80WYtCO0Uqd-vYhWkPpzlpbVu3rkVCbZB-Ro2hkTqahifmqCKkZnI_nWFVrjCXbH4eEORLcnhwwyCqF2dI0Z6SuNtZqcPmUT3uj3gEYfYI-fL1idnKl8yIfbkZO49unJgfxLrQJzuEP-lron-XMCyEn8icLVQrQt-r4uPFn_H2h6PvnwQBxGDkWJ7BINZl6yY7FtXp-3cb1F8TiXZJpFY4wM8wutVyvufT-eqPSUmiFJ1C8XUD9HLwa5W_WAbXs-qcsP8rqwLSgEWlPkCKKOWlv-KPD8Ja6lx1H48Axv5hmp9uj9Kl0P7k27oW9_8h7Eqgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkOnRTCLg_uhmMSJGWzBfYTYwmoIGCBP5XGIUx7YlwiM5UESC9M7_vaxjHTqLQ7JVOJaXRSPyY0yo-BvbIAYTS84s7SDjDoToOwHWw1cxiY02Ix0XZ43RFKfrQoE8Lw5I-aihtUkbFjpMt7G5nfI4bf4R5Lsm5uRcwxynd-gjgE_Wpi3z73Peb_iXkqQgi5g294EiRnvKqmD567F6-SjK6dkNcUJdO7v3I7jA7Njlh_dw9X2gfRu9pO63K6yKmrjtvcRmQzxE2fwF9e4GiWC5uOEbruN8CP3AX0T8tGTmcmmli-7XPhbEHVk_1B2QZk6l-zqiuh6oVt_S4Aw4aSeRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اجرای شکیرا در مراسم افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65860" target="_blank">📅 21:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65859">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGFR7pP8oLLfcuVmTczp6czif2kKhOhsDU66_XxC1OF3CpaB1u8S-AE-8vBE9Xov1mDxfj7zA-I25Zli_8F0jyUa00W_xZjKCtjsIa3k0f08DI7Gl91v5Qh7wArl7Cjs43VjlA-9DmO8-rWT8CZ7Pa0cyJFT8YVKPRQ06RwI1umdjVYsR5xP7e-izeRVkTEKss-dOcH0LBnLnHwwEVjuZKIdpAiNoIvAvIYuEyLCLOqwuOG4vZHZWqdQ826TbJFaOtI70nkrX-KGT9Vn5PC3i1kPDGSem5dd_ONdNN9YGroKMPWiNQzafebYSkunvRfoBMIO1pEJYrgPeGSgLvvj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت سپی هست داداشمون
که در تمام سه ماهِ جنگ vpn هات نیوز رو برای پوشش اخبار تامین کرد، هواشو داشته باشید و می‌تونید از داخل سایت بطور زنده افتتاحیه رو ببنید فقط کافیه یه ورد بزنید
🔴
لینک سایت
http://Chosefil.com
🔤
لینک کانال
@officialChosefil
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65859" target="_blank">📅 21:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65858">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ=حرومیِ کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65858" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65857">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ماشالااا تراااااامپ شیردل
😤
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65857" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65856">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUb214uQMInpXSImEH2Eog35FDozRQhn9J-znRw8Yrl_tqeDg56pZvUFbilFcURbmD-luh__xnQSuknYoGkxNoddqSY7976A0ez0KII0ZBKyWfz22MXxlKYj9VdgOos1NdWeUDRCFaJ6lajZ0xvnZaB3dE1NMyiTBda6vpGZQ5uKws3qpKn49kvCHu77N0KlrQVeKN3Ar5IP5l15CWM5eepi-wJKR3EQtIsj3X1bmPNK4QZNx1C5jYmJV0wBZqzGz8WYcgdwWuqHnI479ePeShvhIEZBMTkP3cU0AEhXlyz_Wau8Jx7AHR8qxL4nL0cTKaVur7QkZjui36CmzHVeRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند
زمان و مکان امضا به زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65856" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65855">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ترامپ:
حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65855" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65854">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
علی‌عبداللهی فرمانده قرارگاه مرکزی خاتم‌الانبیا: صادرات نفت و گاز یا برای همه خواهد بود یا هیچکس. ترامپ اگر خریت کند تمام منافع و منابع نفتی و انرژی منطقه را با دستور قاطع پودر می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65854" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65853">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=c6UR6fQZ6qVFWAC3k9lUWcpqOqOh-ZOy8cy9eKOBXfPZWRv0DIrryCJ-tdmRIPcWKDvuBK5N7Y_CapaoMnMOWTQBws-lZpdJ1uYazSketA9jNvzWHJLIMp2Qs2Tl4m9Z7lqBHMxpU8yqfum6NpnEO6X7DBicAhSIjR38Z3yh24x2TQilZwBKu4Wvj57OjRE2y7hO-YR2PMRCtaGV6l4AqYgWnG-16Fs8B4ufpB258m-OuQKCoR2ww5QAVxByZRsN7vNPAw2gZHcGP4E9XLUahqv5Chy6CNnV9bXYDgZZmfGgWdQ_PFGlfIQRzntav3rdd4bEk9Oo-wAdKI3O8z0o_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=c6UR6fQZ6qVFWAC3k9lUWcpqOqOh-ZOy8cy9eKOBXfPZWRv0DIrryCJ-tdmRIPcWKDvuBK5N7Y_CapaoMnMOWTQBws-lZpdJ1uYazSketA9jNvzWHJLIMp2Qs2Tl4m9Z7lqBHMxpU8yqfum6NpnEO6X7DBicAhSIjR38Z3yh24x2TQilZwBKu4Wvj57OjRE2y7hO-YR2PMRCtaGV6l4AqYgWnG-16Fs8B4ufpB258m-OuQKCoR2ww5QAVxByZRsN7vNPAw2gZHcGP4E9XLUahqv5Chy6CNnV9bXYDgZZmfGgWdQ_PFGlfIQRzntav3rdd4bEk9Oo-wAdKI3O8z0o_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
تهدید وزیر خارکمبه علوم: اون دانشجویانی که پرچم پهلوی گرفتن تو دست و پرچم جمهوری اسلامیو اتیش زدن تحت تعقیبن قراره مجازات و اخراج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65853" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65852">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4OHb_838sqMpNWkoI-k-_aG3kze_sL6rXcV4vsEUSC5yg_04mEIDNP99mI2CYV2C28QEedN4BDFCiLYOlWxtpS1Mu3QKYEmUCNA5ko_kXX13KgOD5oIrUmiSNgu0qtF1ELtJHy7qApAhr1wbCUGSHlcg5S3Imxee661Ia3XRbM8sY8ZAwqXLsPmi5ImcKmWjkfjtAkS4IN3eFX6A0y_cWMMbK9Y5bJlB6ZsoBHjT760WGKHutgL1_mYHRqeuTPxeiqvRY_1b8vX1VqpUwZs7edN-yTxh_NnbQnae6D58G28YuRjoC1xNqIEE-V9cexzhMql-5r8y4zX1IoNQgWPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قالیباف:
استراتژی‌های اشتباه و تصمیمات عجولانه، کل اوضاع را به سمت بدتر شدن تغییر می‌دهد، زیرساخت‌های انرژی و بازارها را منفجر می‌کند و باتلاقی بی‌پایان ایجاد می‌کند که سال‌ها در آن گیر خواهید کرد.
شما ایران متفاوتی را خواهید دید.
زارت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65852" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65851">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW84i3xwznsXnNlbytGAMCCSQ_nRCYVC3cgUFEpKSGbVBBEdQ3lwOG0GuQ6FHokmWIsO3-cZKi4fcPjXgPy-JgJcgtgoWI73x8y1mh8arbbR7ZNO_yPWuZ2ozoh1MMpyJCDFD-Kw2GmFzpP7ErvF9d69ypBu4BnaSv4-V4YQKIyxPzSFTFFuvqmBYYR0d03opSXurZ0Z_wALKWqaXsFDid48iru3SsLfVHkKnR8E-ZzKMwwZ4SddqsBp9onW6AVWJIbjtBgeqzQNcF4d57hLi8diiXFzgXMDjzG3ln7oqQaeTywPVVqm1n5xPrbjJA7wVgDvwAPNpqqvh6dd-c4iyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به‌روزرسانی عملیات در لبنان:
سربازان ارتش اسرائیل فعالیت‌های خود را برای دستیابی به کنترل عملیاتی و پاکسازی منطقه شمال رودخانه سلوکی در امتداد خط دفاعی مقدم به پایان رساندند.
منطقه رودخانه سلوکی توسط حزب‌الله به عنوان مکانی اصلی برای عملیات پهپادهای انفجاری و حملات غیرمستقیم علیه سربازان ارتش اسرائیل استفاده شده است.
این نیروها صدها سازه تروریستی را منهدم و بیش از ۵۰ تروریست را از بین بردند. علاوه بر این، چندین سلاح از جمله دستگاه‌های انفجاری، موشک‌های ضد تانک و موشک‌اندازهای ضد تانک کشف و ضبط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65851" target="_blank">📅 19:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65850">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL62qDOZhlSsrS2iw_7xaSOoUCfyj95WJgpa8l0ucaJ3bNBrizYThHjkpQL_iiSW6cClYRrksriJKZbKQfL07fR__A4i5_-Pz-tAXToy65pmvQh4dVHEo0xR_5eXs96ZEZR9OJPUVWsuc4aPNkDIEvTN9UtOIV1V0FsUaMb5uX1qHs9yp5kitnD-jI7y5uqo5t-KjNEFfqZDKBIgIQksYkzoaaAHj9-pD68ct5nAovsj3J9ndJDINLsPWBCxDVcQijPUSYZlDa6Q5gpSaZZzhBXEZNh9XRm9aqE49fxxl_rw_6O9PkvJAAtHm-IBP5oPfmYC_Z3hPXQT2DJxRElqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پست جدید سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65850" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65849">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65849" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65848">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
جمعیت هلال‌احمر اعلام کرد که در پی خطرات احتمالی حملات امشب، در آمادگی سطح بالا و کامل قرار دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65848" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65847">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JArhhaOrzo2WQoAYOUx1lg3dBL04P9qsVRl8jSc2JkHd6gyNi_oc3aVnIMqnJeNpif17yQxO_Zzfk2nlmmRbv_1ryDl9imGoyOy0asdpAwD49D2ZKZTl7cEGVLVd3X0fdXulm15t0bL0FHTmpd8n2yIXdhW9Pb96co97lFXFInxLbs3nFJwUUK27Kse2XJQyEOh80lhCSRpN9lMJjAayzs1gHKQ04DR_KSGKFQik8vSNd2uAO0cywtLetyAUz1ETgBbgEbT9f5JczGZSiCkVFjzQCLpUJGlVBkwLHPf4TNL3KVdeX3LW00qCBK0elitJzxSkMRYftCw-QYGt7QsnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشیال
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65847" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65846">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65846" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65845">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxSW24C-LE4GVtfgP6-6wKClHJVxoJpMkPsviCe87dBMtn5qFqe6ZsEDpfGlL3vie9iUy5TE9qGoTM6Eq0-4h8VXhPo_q_VKaER1cDOM6vu_AsSrcc0SfwBIETFntpVFacPStqo0dQnrSijY9doI0ftGkmCNRo9DMjj98VN_L7Gc_dcB_SZ4cJHI2rPKa2MWSn3-6MSZHoM1JuDZyvoXl5Lbb3na5Zspnzj0LcJEgNzyIQqX_JpzYoRr8-A660lt-BsRNjEOGelv1Tr6sOvJp1Nd8ppAQmHAieHCkWEqqwh_AZFtwD9N4ErJF8larKKzj6kPINtlqADMkZtTmD8E2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65845" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65844">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=D_3-9jVirmtU9fnglDpWxQ_UuneVeGFclzNve-JlvNYwpscwwM4_fIhPivvL4TbhWLKNlFHMb9h2FOGl4YFSpCQR1QGsJBMTnMYVchWIi6seK6HG1HH0xmfkRN_6hPWdP3rQrcW-a4dtILRTqn3VNWTbsxi_TIwuGH5DjEXvbQASWJXDPxN8K9s0jJQvIApmidNuULGeNDoNPwrLWEcxU3KxXTQ2NlYq81iYuyjLwmvU2t3MvtwpoW6jj0TM2jkVmgn7GS_mXXYtnYAyxIJ_X3OipMl31ZiZzEkWZ4ff0Xi2pdvhwLBjPTARfqdrgGyFNWy2CI4kNZtar9YQgBq0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=D_3-9jVirmtU9fnglDpWxQ_UuneVeGFclzNve-JlvNYwpscwwM4_fIhPivvL4TbhWLKNlFHMb9h2FOGl4YFSpCQR1QGsJBMTnMYVchWIi6seK6HG1HH0xmfkRN_6hPWdP3rQrcW-a4dtILRTqn3VNWTbsxi_TIwuGH5DjEXvbQASWJXDPxN8K9s0jJQvIApmidNuULGeNDoNPwrLWEcxU3KxXTQ2NlYq81iYuyjLwmvU2t3MvtwpoW6jj0TM2jkVmgn7GS_mXXYtnYAyxIJ_X3OipMl31ZiZzEkWZ4ff0Xi2pdvhwLBjPTARfqdrgGyFNWy2CI4kNZtar9YQgBq0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
'لحظه انفجار حمله حدود ۴ صبح به
پیشوا
در  تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65844" target="_blank">📅 18:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65843">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0zXTMV7kFndFrm24OfHGM6_jjIoqknN7PTwwopoxNkf-_g3cMuJ0El0U9-GX8-wkAc68KHAcmVKLNFVbxtuevpN3nIvhGui0ltpDdlJBQ_4bX8mhTnQXP6zUT37x8ivyp7iRrH3WT9LcVHRlCYRl1mrGmzufrtccY-6x_DCkcUuFpaK4ZPVGNQto8oYwLpadSX3P_YOaX1bWcY-scMwphmW1ki6j6wvItE0dnKhJM4Vcyxrz_hPaADFYyISbjObRqhc7yFi4lOV22jWc_V5OubcCrLRfeRfZIiJm8qoWHHTBOX09FdGht3zYaolFjzZWyxyCHxHny_wcp1VHaAIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب کاخ سفید:
«رئیس جمهور ترامپ همه کارت ها را در دست دارد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65843" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
اسکات بسنت، وزیر خزانه داری آمریکا:
رژیم ایران در بازی مجموع صفر که در حال انجام آن است شکست خواهد خورد.
هر آسیبی که به متحدان ما در خلیج(فارس)وارد کند با وجوه استخراج شده از حساب های ایرانی جبران خواهد شد.
هر عوارضی که به مقامات تنگه خلیج(فارس)پرداخت شود با وجوه استخراج شده از حساب های آنها جبران خواهد شد.
هر حمله ای که ایران راه اندازی کند، تنها پیامد های مالی و اقتصادی را که با آن روبرو است عمیق تر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65842" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPl6m7xu_QD4uMhB9mxoCgb3q2XQrj006BjQ2leMBd41qB-7Rnsnk4Mjpd73bGL-MoPN4fcv0H1EuXYwSpQugBy8kRSdDH66RNKHNWO1Zhtm4yyQ0XDloyTJpxe8t4PcWiJjp9Yv2LBjpWrnZWkJqTUoj7_dOK63LXO05f8vSeeGsv4RDUEDexa-bCbMbuTr2-_ZSVru_Syxa83ms0Q_i4yaBEOMweq2uva-q3MPvYZ96t-hPL3_a5sJWfABGnu2iL7MqOY0-63bGfVSeaeSh12i_gGbo9uuCGpd1l0W9MlBc0qEQwOvHOaMp95qU7Mb31U7ckH3r_4bBRMwKdS-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار سختی خواهد زد.
در مقطعی در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.
از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65841" target="_blank">📅 17:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ارسال سلاح از طریق کردها:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند. فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد، کردها. من این را به یاد خواهم سپرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65840" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
جی دی ونس درباره نتانیاهو:
نتانیاهو کشوری را اداره می‌کند که به‌وضوح یک شریک بسیار نزدیک ایالات متحده است.
اما حتی وقتی ما شرکای نزدیک بوده‌ایم، گاهی اوقات منافع ما کاملاً همسو است و گاهی اوقات منافع ما ناهمسو است.
نتانیاهو به‌شدت منافع کشور خود را تأکید می‌کند. گاهی این بدان معناست که ما در یک صفحه هستیم و گاهی بدان معناست که نیستیم.
آن‌ها به‌عنوان یک شریک بزرگ در بسیاری از راه‌ها بوده‌اند، اما ما همچنین باید بر آنچه در بهترین منافع آمریکاست تمرکز کنیم. و جایی که این منافع منحرف می‌شود، متأسفانه برای اسرائیلی‌ها باید سمت مردم آمریکایی را انتخاب کنیم، که همیشه این کار را می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65839" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromromo heidary</strong></div>
<div class="tg-text">اسپویل
فیلد مارشال عاصم منیر، پادشاهان عرب به ویژه محمد بن سلمان از من خواستند که به دیپلماسی فرصت بدم و ایرانیا هم از من خواستن تا فرصت نهایی رو بهشون بدم منم گفتم باشه و حملات امشب که قرار بود زیرساخت های ایران رو نابود کنه و جزایر ایران رو از روی نقشه محو کنه متوقف کردم
از توجه شما سپاس گذارم</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65838" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65837" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EanE-fVkLUVmpcLv522R4olx5dizUIlQ3taMrzFotMJLo42674NpYye7PVHaZb0luWfq4XELSjbgW_RVC6TpSnURnxx-OXAIlLC9vU-n0Csj3bCNokDSvMAgYFj8mFo7FZHwLFqhPNeE6SDEnwAlAcL32MWtGe2WGv60yGjiepMElrvPo_ms-EQWNAYl8BLuQWasF4ssKDm_JTFb4YSMQYe79UKUy9B_WDEDSwEOm8hSs5T5l44m431Wh-uJdc1Pn8Q2mTlPfA4bQyZoOt7Og4z9QSVenG8GjQ0-8KK4Z3TwdYexsnEl94dDYWAzcqi0L-v_LWiencWynJWHmLN51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65836" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9xtxOm9ZxZopfNXW4NUJOihUl51BkbXwLfjChzF-ZLTahHnQH5nep53nKAImz98LRqmmvY3zUTTpjlFem8RwFaWile25S2fU8mcR5ANQWEqQqfCDBnUttSZrKco-q4L3i-7OTi0Wu_Qx-6azUEpv_lNp_yGwswG3DqyvJ5cjxO-e_74Ni2GqtURtMN2v2UGAxF_VkiCxLqnh-KIAmiabyKR8Yi-r7DoyCY_GzgsuL6ZzxaHb9sKyzBtpDq2n6Kh6rhBiKNQY0XvCAXCjj54U1UBH0I40ZVtTUsILLo5nv4TO-rxZJgAPH_NhZFZ-E4y9DgdryWoqdxXF3grAYwyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران اینترنشنال:
‏
محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در شبکه ایکس نوشت: «رییس‌جمهوری از تعادل خارج‌شده آمریکا تصور می‌کند بمب‌ها می‌توانند او را از باتلاقی که خود ساخته نجات دهند، اما موشک‌های جمهوری اسلامی او را بیش از پیش در همان باتلاق فرو خواهند برد.»
او همچنین نوشت آمریکا در برابر انتخابی دشوار قرار دارد.
رضایی افزود: «واشینگتن باید میان پذیرش شروط جمهوری اسلامی و از دست دادن آخرین بقایای اعتبار خود در جهان، یکی را انتخاب کند.»
اظهارات رضایی در حالی مطرح شده است که مقام‌های جمهوری اسلامی بارها بر ادامه پاسخ به اقدامات نظامی آمریکا تاکید کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65835" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
«ما آنها را بمباران خواهیم کرد.»
هشدار صریح رئیس جمهور ترامپ به ایران در جریان تماس تلفنی با تری‌یینگست، معاون رئیس جمهور ونس و نمایندگان ویژه استیو ویتکاف و جورد کوشنر از اتاق وضعیت مطرح شد.
دولت معتقد است که ایران همچنان در میز مذاکره تعلل می‌کند، حتی در حالی که نیروهای آمریکایی اهرم نظامی گسترده‌ای را نشان می‌دهند.
پیام ترامپ: ایران حتی نمی‌تواند آسمان کشور خود را کنترل کند. ایالات متحده ۴۹ موشک تاماهاک شلیک کرد که طبق گزارش‌ها برخی از حملات به اهدافی در حدود ۴۰ مایلی خارج از تهران اصابت کردند، در حالی که جت‌های جنگنده مواضعی را در امتداد ساحل جنوب غربی ایران هدف قرار دادند.
در مرکز این بن‌بست، یک توافق پیشنهادی وجود دارد که تنگه هرمز را بازگشایی کرده و محدودیت‌هایی را بر برنامه هسته‌ای ایران اعمال می‌کند. اکنون سوال این است که آیا تهران قبل از تشدید بیشتر فشارها، به میز مذاکره می‌آید یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65834" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6mcaSr4Nu0Vvo95_yt0VHffVFY-8v6-Ak1___tkWHGKlAFBWf4RqesHob09yunfPPtjAocRV9jQpF0oZ9reOf41jD-2nCSeqmzjvGUmu164l1mTP0I-tX8lwig7yjFK1IIqkLMR3xap_0ltAsz5eqWxl8SKu5dg5h33n3t9JT0h_gcmymxdAWlOuTMQoGQwk8Cf4Nztv7L59UFyWcpdRqG7w4Z9NDL0emZi-MmPDnX60pPCNYhN8aF_UsJl2I_N4HTv6bMI-UD2WmOTeN1VgcqyHYKSpWlKa_uIU6c-8kB11xlraR8YS9cx-NiGoIBtI6Y2jx68FsXHsb1T_e1K4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۱۰ ژوئن سومین نفتکش ناقض محاصره ایران در خلیج عمان را از کار انداختند.
سنتکام پس از تکرار عدم رعایت مقررات، دو موشک هلفایر را به موتورخانه کشتی M/T Jalveer با پرچم گینه بیسائو شلیک کرد.
اوایل این هفته، هواپیماهای آمریکایی کشتی‌های M/T Marivex و M/T Settebello با پرچم پالائو را به دلیل تلاش برای انتقال نفت ایران یا حرکت به سمت بنادر ایران از کار انداختند.
از ۱۳ آوریل، ۹ کشتی متخلف از کار افتاده، ۱۳۵ کشتی تغییر مسیر داده شده‌اند و ۴۲ کشتی کمک‌های بشردوستانه اجازه عبور یافته‌اند.
این محاصره به طور بی‌طرفانه علیه کشتی‌های همه کشورها که به بنادر و مناطق ساحلی ایران وارد یا از آنها خارج می‌شوند، اعمال می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65833" target="_blank">📅 15:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
خبرنگار صداسیما: شنیده شدن صدای انفجار در محدوده سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65832" target="_blank">📅 14:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_etVZWW6sNhVLS3aYuUY3Gu461ChbhBeNB4lbREjnrIs_Ty0gh1hos-hV0vYz98fbyNIrCQmIoYmFARivV0WSLRglw9oV3jtqFgr4nb8kSR6h1ajq-nsVGzMXOrFVKk8ksJxZfo1WodgxC1mSLzoRziZY2vKN97xWknegH47FIHdAwURQdtXqbYgSnmVDzFwzQvpLR4kJMf96vApL7FXrito_sesOUiwx1YXgCvaeRBbKoJcV92wNA-jc17YZKDVHiC8Qd_9xnOiMx4pcSwGvXflW_tlICd0uAiESOGbJNFMSK693wawvBD7R1UTftqhC-F16ksp-6TDP3cMJQN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
🚬
شاهکار جدید رستوران های تهران:
⭕️
پنیر+ گوجه+ خیار+ گردو= یک میلیون تومان وجه رایج مملکت!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65831" target="_blank">📅 14:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
دلار: 180.700
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65830" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
وزارت خارجه کویت:
حملات مکرر ایران نشان دهنده رویکردی سیستماتیک و تهاجمی است که کویت نه آن را می‌پذیرد و نه تحمل می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65829" target="_blank">📅 14:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKRxloDdBtXu1bXvT0ciYLBqmRs0yjS5JgABtUxp3psuCneJKu7d0Vja0mInyLx3GsxaomstNrQrw1AMZkDZ6zaeySlyaZosut76eeywzfKHVl2qA31s7PTnIgHwpc6Ol_e8OlHjmJFEo-FKXcgoV0FYDot9NR5zsoFw9jTFajkQlFFbpsUSdvo9ZozwKRYSlpYmwjVUTZ96Bs8hUrSkAOSU47TDhAy6Yh6irfkCVLY8Ry_HANfQ1lWpy0hjVZP_VCfcE1sb0EmJfpGR5qgvcOvga9l1Ncd-8AtBs_vxu5IEgSzZ5ZNv-PUg80hjxC2eAK_aYdKq2kPTQvP5IjRfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل به فارسی:
دیروز عصر و دوباره امروز صبح، حزب‌الله، نیروی نیابتی رژیم تروریستی ایران، با نقض آشکار آتش‌بس، از لبنان به سمت اسرائیل پهپاد پرتاب کرد. حزب‌الله به لبنان خدمت نمی‌کند. در خدمت منافع رژیم تروریستی ایران است، در حالی که مردم لبنان و ایران هزینه آن را می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65828" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXXgwaHmj1X3xl0BCbm1Vt8H3IMfjm03QP39kpOObC5hcc104pRXeL20_wd9SyrlxPmlkls2mLfIA4zIL3W_UZSFCPnB0tpj_qmStmp9e0UtmX3IU3rP5gI0wzrNgz6qJ5iNvc63TgDmWkzY5l8Eb8tbj1wlsqLH5_9TzSzgSZ5006ss4UempD4Z9HBb44T0tRlnSAAI2P1UXur6LBBLsoUPTNWfyQpSVhX8lTQdEAYVGjF7_cA96pBgJTEwcHCj_Fuh9oIRgZCuYcey81mFDkLv4Fo4XllqhB6BN9G9ciyPVt7OwQau5js1cupPZzWmhRfU4WaOkg4n_-qUWyZxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سی ان ان:
هیئت قطری امروز صبح پس از برگزاری مذاکرات شبانه با مقامات ایرانی که با هماهنگی ایالات متحده انجام شد، تهران را ترک کرد، در حالی که حملات آمریکا به ایران در همان بازه زمانی مذاکرات شبانه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65827" target="_blank">📅 13:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=RAd9F1qlvbjCuDMXTH0fCEdvPQCrcGfDXAg05q1OEp-nHxtBCIlLP5ETFA8Y1NhvyT9VlnNZ48G5S5L5OaSpNXviy-kTFu6YaKAAQM0l70f1P6feOFbISndXdisI7JjH0EmJgMhZsDoIx680T6gDsznH2UE-30v_A8qjqntsYeJNfw_5WjSVEbOUHhyMJwkaaouncevwslCTNmmXYAqzcwQpBvv-5TUJduIqv5E_JU0maUDguDozdFdPnq9oQtvBWfLyXef_g0bK3mEYZNHG6IxQ6IH2ohl-6gjLHoM8rtdPwwSJB9KgXSqfgj2WUKP5yFziD822f2Bn_oJ9aF20Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a59b3948d.mp4?token=RAd9F1qlvbjCuDMXTH0fCEdvPQCrcGfDXAg05q1OEp-nHxtBCIlLP5ETFA8Y1NhvyT9VlnNZ48G5S5L5OaSpNXviy-kTFu6YaKAAQM0l70f1P6feOFbISndXdisI7JjH0EmJgMhZsDoIx680T6gDsznH2UE-30v_A8qjqntsYeJNfw_5WjSVEbOUHhyMJwkaaouncevwslCTNmmXYAqzcwQpBvv-5TUJduIqv5E_JU0maUDguDozdFdPnq9oQtvBWfLyXef_g0bK3mEYZNHG6IxQ6IH2ohl-6gjLHoM8rtdPwwSJB9KgXSqfgj2WUKP5yFziD822f2Bn_oJ9aF20Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات امروز اسرائیل به اهداف حزب‌الله در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65826" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65825">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
🚨
🚨
منابع ایرانی به رویترز:
ایران و ایالات متحده هنوز در حال مذاکره درباره یک توافق اولیه هستند
تهران هنوز در حال مذاکره با آمریکا درباره مکانیزم آزادسازی پول‌های مسدود شده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65825" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=N-AzAB8jBQskfSPUk-AUtJiHhJto3LbNQzCcVBpVVPuDKqh-6AmsyFmEHLAjnZKiYvNQl4zN6RmFc4_DEFSpFTnZcH6L-EVG1oA5-UoWVEqZbDs4oFtgVFw0LXPluaI8QNRlF-XHJ1YkyZx5D03uulGhoWEgdgeA-zH02iEPC5MAiqlUmxNJoR6lAcBX4iXOYzrL0ev46pR4C_2HpUztrUoeaBStJWgTnJI--4D4UcrdMO2-QjazMjqYG_rHZ4ka-C6nX-XgvLrRAKu9TwpesEX8V66RqbVKAU93vdo0FTy991LuV_h3WZwJwYD4nHJZr-Ss8qYEyG6IEvYYeSmVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dae3f50b.mp4?token=N-AzAB8jBQskfSPUk-AUtJiHhJto3LbNQzCcVBpVVPuDKqh-6AmsyFmEHLAjnZKiYvNQl4zN6RmFc4_DEFSpFTnZcH6L-EVG1oA5-UoWVEqZbDs4oFtgVFw0LXPluaI8QNRlF-XHJ1YkyZx5D03uulGhoWEgdgeA-zH02iEPC5MAiqlUmxNJoR6lAcBX4iXOYzrL0ev46pR4C_2HpUztrUoeaBStJWgTnJI--4D4UcrdMO2-QjazMjqYG_rHZ4ka-C6nX-XgvLrRAKu9TwpesEX8V66RqbVKAU93vdo0FTy991LuV_h3WZwJwYD4nHJZr-Ss8qYEyG6IEvYYeSmVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش پزشکیان به سخنان همسر سرباز ناو دنا که گفته بود حمله کنید: انتقام که فقط جنگیدن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65824" target="_blank">📅 12:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65823">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65823" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65822">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65822" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65822" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=m7mOYJjjH3N2IiCo0GBYrzBuD6R5HF7HgxwOQrp54M6w8wAO_Ldmnf4Vx_Jkr8nfInSA8rswYMA3OZ68BfwUUw63h1i4Xm67obzsNigxQmYpsnOElquvDR0KanJBh0JW1rCnnjcWvLslwe38o4WLA3wNFfzTzlL-tbggs1y5mB86xXZYRReF-epS7Kia6i9kQWbRWk-jqjy2NLWA4PU5IhTdX3a857Yc00lWATZee80kKF99mcaspvs5_AAhs4_m2gvE_dqivjzauF-WQDMvaStAsfe-dhANw5pqogLaAKpSX5tTfv2hmnsG1uDuAYARHZuTukyWgPSV5HaOL5vFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e4c73c3.mp4?token=m7mOYJjjH3N2IiCo0GBYrzBuD6R5HF7HgxwOQrp54M6w8wAO_Ldmnf4Vx_Jkr8nfInSA8rswYMA3OZ68BfwUUw63h1i4Xm67obzsNigxQmYpsnOElquvDR0KanJBh0JW1rCnnjcWvLslwe38o4WLA3wNFfzTzlL-tbggs1y5mB86xXZYRReF-epS7Kia6i9kQWbRWk-jqjy2NLWA4PU5IhTdX3a857Yc00lWATZee80kKF99mcaspvs5_AAhs4_m2gvE_dqivjzauF-WQDMvaStAsfe-dhANw5pqogLaAKpSX5tTfv2hmnsG1uDuAYARHZuTukyWgPSV5HaOL5vFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کشتی JALVEER که امروز در نزدیکی بندر شناس عمان مورد اصابت قرار گرفت.این کشتی را خدمه ای هندی اداره میکند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65820" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkDp_wXMTUv_NehJ12i90gTVzMldmSQHfMqZXGjWwBG9AZi65bUE0URBNHLk32OYvBYTdrJi86f-iuqfXrXA3eE4nJs2nyd9LmlE7b6mM4UE9wRVYrzGv_gjutPQGS_25INEl6Iu8atrYeh5SW3nIiRoR_fCCqMNIXkYSG1gOUOYQMU0ClDmHAJcAcOGiDSd4-LoVjZZ8-0L6OFGyDXXsOOYPRXupg0P6zkbrDRrht6fNSN2rSKuQEezAOvjfXykW074tpOioosS3iD2sVLKIfX6N8aodLbOCBaKoG3NqqKwxvwc-0pfMicAKsOVa2grTHbaIhkNBLh9gRwRFsQgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی در خصوص نقض آتش بس توسط آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65819" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=URQ1YDXmHs-OFuwRjFDHBC1ffBpI9KZZCTcfp6Es-zk3SOo50J5IZLyK1yTcKu5Hl3Aq0qrIkyHK-i5lWTSQt6YnlFNKzIfmSKryWxz9TP17Gqn0x4I3XOfe4E62xx9SHRsJAjVXbT2rsAHCqr0s4uTbK8oHmePTLiBkvsiJDCaW6-A2yiVMxL_1k2n9c8NEMfwdMKp4l9NenFmVQN5vNUOsFz9J2cjTaKsegLCElU31NBdohpu2KWUVytVMztmYGgBba5IkK4iB9Ncx6whX01cDeWyL8pcng8GmhNDVGTfQp5r8xqlHiboGASFXOi75EPB3eXiCf9ftenJfug7mnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bec45c0e2.mp4?token=URQ1YDXmHs-OFuwRjFDHBC1ffBpI9KZZCTcfp6Es-zk3SOo50J5IZLyK1yTcKu5Hl3Aq0qrIkyHK-i5lWTSQt6YnlFNKzIfmSKryWxz9TP17Gqn0x4I3XOfe4E62xx9SHRsJAjVXbT2rsAHCqr0s4uTbK8oHmePTLiBkvsiJDCaW6-A2yiVMxL_1k2n9c8NEMfwdMKp4l9NenFmVQN5vNUOsFz9J2cjTaKsegLCElU31NBdohpu2KWUVytVMztmYGgBba5IkK4iB9Ncx6whX01cDeWyL8pcng8GmhNDVGTfQp5r8xqlHiboGASFXOi75EPB3eXiCf9ftenJfug7mnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لیندسی گراهام،درباره ایران:
اگه همین الان توافق نکنن، باید دست اسرائیل رو کاملاً باز بذاریم و خودمون هم از نیروی نظامی استفاده کنیم.
امیدوارم اتفاقات امشب باعث تغییر رفتار بشه.
اگه این فشارها باعث نشه که بیان پای میز مذاکره، باید استراتژی رو عوض کرد. باید با تمام قدرت وارد شد. کار رو یکسره کرد.
بعد از اینکه تکلیف ایران مشخص شد، به مرور زمان مردم ایران می‌تونن کشورشون رو پس بگیرن و مسیر صلح بین عربستان و اسرائیل هموار بشه.
همون افرادی که میگن زدن زیرساخت‌های ایران اشتباهه، باید بدونن که این‌ها اهداف نظامی مشروع محسوب میشن
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65818" target="_blank">📅 11:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65816">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwdxUJSsD5fsI8XE0sOdgyPt_NEi_zrpjRR1fXjY9rC62DYnwOD9LZU5v06ufdU35Ajr-fK-CvrrbaNLtf6SJfX5vYeAeosYYQsfoAtek6I0RXeL6BQ7259dHOYFzWpV9LPStVcAPZu7c-sg5JO9srILX91pnbC-2mFl_cDrgRyay9KB7D9sZseq2fc0gND8fL7_XtCEfNNebjfn6ibftapRPrzu2x0UrSAx08S-eYW1BOtO3vtw_RpBT8giK0WTuDNTHN0gySTjHPGtR_P_RKa_fdOizmrHLp6xtRC1N8VowsuK7SV7Qrar4GIZxXy1DfOl08VcuYbMRAMYqDJ-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJljp0-n2g7wQsNtwxMI8n0rPljHYLYVRU760g6FR6CIPcesSzRaEuypGnbDVIrpSGiPIf2WWI_Sdn2udn1xHT1l8T3AcmDA016QTwUOh0_AMRVGL_XldEKRlzcQZWrvRwH5NchGuxKQN3386gRdBIkCAx66xpOz3bofPQ86qw9neqxYgs1EmsiFDhASnMk1JvvFNxqf_I5M1q2SYto_EKn9n6RaWAwMnOysJoL7UytwsbGVhlcNGrAvquK8yEt8c8BKEEp1Q5c43EYxJamAVvUpXz9dxaBXVaQNu4g5l8AygxbbmZvSBumGHayfkC7NQ5Ewn3pTbC5PMhlPfoLGLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وزارت کشور بحرین:
این خسارات مربوط به حملات دیشب جمهوری اسلامی هست و دختر بچه ۱۱ساله ای هم توی این حملات زخمی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65816" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65815">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw8Dy8fk4o3lNmjXiwis54gpMD920dDEAqRV_4jXWVJtfJFAJYxsFsKKVppFw-Doc14OjS8zl-KXIpvP-rjcarqxPCH-8FcXGCiorExE8MBavYHpuVe2fTOYJDQAFEm-iQqcmgkRWS6Nx6_NBg4lBWQ_fd5o5c2eBUUNU21YtQCk2q5GuZ68yCmt66RMiriwqRtA6_QOZkAM9nzvT87QJXg8Q0hKRX-7q9mQr-lDH92CawLwNHqeU_RpS3B-rgudx4UkPmfeSEb89Dp7n2mHpN6pEDv1Pbx9PFz5Q26mQD5BWiIt-p0GQTYj48qBm-ZXIQUxW-EOwpvTxRM3P-ssTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان از پهپاد رهگیر جدید «کبرا ۶۰۰» رونمایی کرد
شرکت دیل دیفنس در نمایشگاه ILA 2026 از پهپاد رهگیر جت‌محور Cobra 600 پرده برداشت؛ سامانه‌ای که برای حمل و شلیک موشک هوا‌به‌هوای IRIS-T طراحی شده است. این پهپاد با طول ۶ متر و چهار موتور توربوجت، می‌تواند موشک را صدها کیلومتر دورتر از محل پرتاب به منطقه درگیری منتقل کرده و برد پوشش پدافند هوایی را به‌طور قابل‌توجهی افزایش دهد.
کبرا ۶۰۰ در واقع نقش یک «سکوی پرتاب هوابرد» را ایفا می‌کند و برای مقابله با پهپادها، موشک‌های کروز و سایر اهداف هوایی طراحی شده است. استفاده از موشک IRIS-T نیز به این سامانه امکان درگیری با اهداف مانورپذیر را می‌دهد.
این طرح ادامه‌ای بر مفاهیم قبلی آلمان برای ایجاد رهگیرهای بدون سرنشین مجهز به موشک IRIS-T محسوب می‌شود و می‌تواند لایه‌ای جدید به شبکه پدافند هوایی این کشور اضافه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65815" target="_blank">📅 10:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65814">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
نیروی دریایی سپاه:
به دلیل نقض های مکرر آتش‌‌ بس توسط دشمن آمریکایی تنگه هرمز تا اطلاع ثانوی مسدود خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65814" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65813">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
ترامپ:
اگر ایران توافقی که ما میخواهیم را امضا نکند فردا(امشب)ایالات متحده دوباره آنها را بمباران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65813" target="_blank">📅 09:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65809">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsYu63Y36U46uvvKQT2xKDUEwsalZaN6VUokOyRB14zaIhnY7YhXExSD9rr7M0jVOty8kS_6AwONk3Rxg-4scW_zOJPEDKZWs2Ux3uRqpPQXOGqyQ3br-YYczOHUwImOmVzQRwysNRDzzqDlwWiRlVzb3J1mHT66-EzrC6I0QMSTjL71KHyH46ZzsRHtHr81HyIu7Pe6_IN2O2zKJoQos1NEP3umipXxuS7l5lxpse77vkvbA9OPmQjtmiyOcIv_0nBbojHLgNlL2QOqeKaRwDqF-D7lO3ijpVT3xzLRBNB_V0uXIoUBVZUPOaVjP1aQLQw_vuLd1zr6RxdqfJ9FOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2NfqfDEa8C0qcMQwjhOH3uE__HBytR-iR2EaK6XvmMpqsNZKYBxrJd_qvHbcWhcwa8BjkeWLv3qbttR615HmhY7PHsdSZlcm2lwfUXe6DlN0O42CMBMg1muCQbI0LQxScCMoUD7X3VWmDNPs3iyMilx0nr14tJDoTFPiBYF_PAjQTBWacRYZ9k5eRPEHfmar1iKSueCQXbeIkumi6O9L5bf_SjNM6IVSCKQK-Bgq4FZqUfoSs0mjHc0ZED2LuTQaf2ooo_raRcQAMX6M_oUBQmXMmcFXytXUJRccRF_seVPNWj4pZYgIZup5KE9dlFvWGV_w9khUOXxdpvlV7HRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzszaglPYpIrfgOynXDYsuoVn4KLAAnqIAidzmzk9QJNHXlLf8WUzVtppRjFXy3LE2_2N9odJPvgvwgIELGMmIIkTkwQlCkS80plPmNV1ue82_7L7k-5D2fOyDPt9JO8soW1g8aCCPtXy9EZV327-wQK6J9wU-OJHBgYSAoQb9Z64yzAP2sZa1QLYKuviiyTNSzXP5_inmqff1y8vHI2Q8xchYdQpgMnrKTk3Prim6feHJPJRbC3lEJUngKoBgGdZLNQtlLUKsNkZszSBDA3IeQFQDs5ysiatRmI7uDP8vmzQQwcATGCkBFZNB3wD_bBymyvEAQ225S1gL1xWRTZOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=T-W46BERfg29hRmsqbIkE_SxhxxRfxukrGHWtbuRbexwwm3Dn1JiN6eSq_i_QzcMZ9kTxZf3cE1LeHGdPtxvlpABZiJgt05D0cD6pcrEDAczl6tkDAUxIgYz-2fgP4gGBX0Hh_PxTWNwEWrO0d4XcbSPok2b1bgATSSCm5J7zoN-cwk0tcZ3ZkXC7FJRqW4Wngk6gmN_jkUfEbD2MVCKhzcE5RV2db_4XbqieXYnh9Z91ljKr3QCiKD1X0bpPirvN3zlOaZsJJqZWqPi7JdRDH1LXE4cJDytgZ9FVMekV7K4yoEinm2ofyOapc6X8azLbZ5ukf7becP8aFdOpNvnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9bf04a71.mp4?token=T-W46BERfg29hRmsqbIkE_SxhxxRfxukrGHWtbuRbexwwm3Dn1JiN6eSq_i_QzcMZ9kTxZf3cE1LeHGdPtxvlpABZiJgt05D0cD6pcrEDAczl6tkDAUxIgYz-2fgP4gGBX0Hh_PxTWNwEWrO0d4XcbSPok2b1bgATSSCm5J7zoN-cwk0tcZ3ZkXC7FJRqW4Wngk6gmN_jkUfEbD2MVCKhzcE5RV2db_4XbqieXYnh9Z91ljKr3QCiKD1X0bpPirvN3zlOaZsJJqZWqPi7JdRDH1LXE4cJDytgZ9FVMekV7K4yoEinm2ofyOapc6X8azLbZ5ukf7becP8aFdOpNvnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بررسی وضعیت راهبردی بحرانی جمهوری اسلامی پس از حملات چند شب گذشته و فروپاشی بازدارندگی و چالش عبور از بحران
متنی که ادامه می‌بینید یک تحلیل جامع نیست و صرفا یک بررسی وضعیت است از راهبرد جمهوری اسلامی پس از حملات چند شب گذشته‌ی آمریکا و اسرائیل؛ خب جمهوری اسلامی در ۴۸ سال گذشته تمام تلاش خود را برای ایجاد دو اصل
#بازدارندگی
و
#بقا
انجام داده ولی حالا در ماه‌های اخیر با فروپاشی شدید مفهوم بازدارندگی و حتی بقای خود روبرو شده است!
استراتژی‌ای که بر پایه شبکه نیابتی، موشک‌ها، پهپادها و تهدید تنگه هرمز بنا شده بود، در برابر حملات آمریکا و اسرائیل به بدترین شکل ممکن آسیب دیده؛ من همچنان معتقدم که جمهوری اسلامی قصد داشته در دوره‌ی چهارساله‌‌ی ریاست‌جمهوری ترامپ مقاومت کند، زمان بخرد و امیدوار باشد که در انتخابات بعدی یک دموکرات روی کار آید و فضایی برای تنفس و معامله ایجاد شود. اما واقعیت میدانیِ چند شب گذشته این محاسبه را به چالش جدی کشیده است!
‼️
درس تاریخی و تأثیر بر دموکرات‌ها
من قبلا هم گفته بودم که سیاست آمریکا یک سیاست واحد است؛ یعنی حتی با تغییر رئیس جمهور هم سیاست کلی عوض نخواهد شد اما تاثیر گذار خواهد بود؛ برای مثال حمله بوش پدر به عراق (۱۹۹۱) ابهت صدام را شکست و راه را برای حملات موشکی مکرر کلینتون به عراق هموار کرد؛
امروز هم شکست بازدارندگی ایران می‌تواند پیامدهای مشابهی برای سیاست دموکرات‌ها داشته باشد. اگر دموکراتی مانند بایدن روی کار باشد، ممکن است بخاطر این ضعف، سیاست‌های سخت‌گیرانه‌تری اتخاذ کند یا حداقل نتواند به راحتی به سیاست‌های «تعامل» بازگردد
شکست فعلی جمهوری اسلامی نشان داده که «ببر کاغذی» تهدیدهای منطقه‌ای‌اش تا حد زیادی توخالی بوده و هزینه حمله به آن بسیار پایین‌تر از تصور قبلی است!
❌
وضعیت فعلی اتاق تصمیم‌گیری
اتاق تصمیم‌گیری جمهوری اسلامی اکنون در موقعیت دشواری قرار دارد؛ سوال اینجاست چگونه بحران را با کمترین خطر پشت سر بگذارد و همزمان بازدارندگی را برای حفظ اصل بقا، ترمیم کند؟
تهدید زیرساخت‌های اعراب
بستن تنگه هرمز برای اختلال در تجارت جهانی انرژی
واکنش‌های نامتقارن و کنترل‌شده برای نشان دادن قدرت
ظاهری
حملات دیشب آمریکا صحنه میدانی را به طور اساسی تغییر نداده، اما به تدریج در حال نابودی قابلیت‌های دفاعی ایران هستند و این حملات بخشی از الگوی گسترده‌تر فشار حداکثری و ضربه به تأسیسات نظامی، فرماندهی و پدافند است!
⁉️
قمار واکنش افراطی سپاه پاسداران
سؤال کلیدی این است که آیا واکنش افراطی جمهوری اسلامی (مانند حملات موشکی گسترده‌تر یا بستن کامل تنگه) می‌تواند چرخه فعلی حملات را بشکند؟ یا دقیقاً برعکس، خود سازنده حملات شدیدتر خواهد شد؟
تجربه ماه‌های اخیر نشان می‌دهد که جمهوری اسلامی در حال حاضر در موقعیت ضعف نسبی با استراژی های بشدت هزینه‌زای زیر قرار دارد:
تحمل و دوام؛ یعنی جذب ضربه، پاسخ محدود
انتظار شکاف سیاسی در طرف مقابل
در نهایت، موفقیت یا شکست این قمار به عوامل متعددی بستگی دارد:
انسجام داخلی رژیم
توان بازسازی سریع نظامی
واکنش بازار جهانی انرژی به تهدید تنگه هرمز
اراده سیاسی در واشنگتن و تل‌آویو
‼️
چشم‌انداز
جمهوری اسلامی در حال حاضر بین دو گزینه سخت گیر افتاده:
ادامه مقاومت تاکتیکی با امید به تغییرات سیاسی در آمریکا
پذیرش نوعی عقب‌نشینی راهبردی برای بقا
هیچ‌کدام آسان نیست. سیاست عملی رژیم در دهه‌های گذشته بیشتر «عبور از بحران» بوده تا حل ریشه‌ای مشکلات؛ برجام هم نمونه‌ای تاکتیکی از همین رویکرد بود
🔴
ارزیابی واقع‌بینانه:
بهترین سناریو برای رژیم: تحمل ضربه‌ها، مذاکره تاکتیکی، بازسازی تدریجی و انتظار تغییر در واشنگتن (دموکرات‌ها) اما شکست بازدارندگی قبلی این محاسبه را سخت‌تر کرده — طرف مقابل حالا هزینه حمله را پایین می‌بیند
بدترین سناریو برای رژیم: اگر اسرائیل/آمریکا فرصت را غنیمت بشمارند و حملات را ادامه دهند، رژیم ممکن است به سمت «همه یا هیچ» برود (بستن تنگه + حملات گسترده) که می‌تواند به فروپاشی سریع‌تر و یا حتی نابودی زیرساخت ها منجر شود
در مجموع بنظر من رژیم اسلامی ایران نه تسلیم کامل را انتخاب خواهد کرد و نه جنگ تمام‌عیار را؛ آنها می‌خواهند زمان بخرند، ضربه‌ها را جذب کند و با حداقل هزینه از این مرحله عبور کند تا بازدارندگی جدیدی (بر پایه تنگه + هسته‌ای پنهان) بسازند!
اما شواهد میدانی نشان می‌دهد این راهبرد پرریسک است و موفقیتش تضمینی ندارد و تحولات سریع (مثل حملات دیشب) می‌توانند معادلات را یک‌شبه تغییر دهند؛ بنابراین حالا رژیم اسلامی ایران صرفا در حال مدیریت انقباض است تا زنده بماند و در یک آینده‌ی خیالی به امید شرایط بهتر، بخشی از مردم را کنار خود نگه دارد
!
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65809" target="_blank">📅 08:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65808">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود  حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65808" target="_blank">📅 08:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65807">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در ۶۰ روز اخیر این سنگین ترین حمله‌ی موشکی سپاه پاسداران به کشور های منطقه بود
حالا باید از ترامپ پرسید، کدام نیروی هوایی و کدام موشک ها از بین رفته؟!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65807" target="_blank">📅 05:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65806">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THipG62SKQIie0Ap5fPltRR4Vhp-u-qda7T4uhwK1ug6JFFH0P7_mJcOxs7F9WxUmcnRCPVSi_1AOsCM6IViF3c7kpt9jZXvqpd-PhNrpo90Av-eANs22ec1YLrnVtyDg4WNe6h4XX8ZF7SWLld4AJ8wfpjJJ7s5Z7J1cBsx3kIjCSPtwebDmIKvKhkBhh4LH61yLYQAs6zXqTd5ZyPX1J4yz7W4dItWJn_IoHMxlGuUuM-DlBHfESRzDce_LJ6m_-yhaYBK-MAcxhlnUbfp27rQJd-cjrufZ7-iZ1j5fV2fGxtZbKTvEKw1ve2cvjaBefPZVTrVd3XqaEV7WDZKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کردستان
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65806" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65805">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbbcnwwvhvrPsvlHqw6lq6V5nAjtF_N4Xcw9UYkIaWVGPMyJwQ79u6VK3n_2HmxuQfHm1Es2UhKmHDwqCxl704TZWJ9Yl0YB0_SZxaX85ImMzzwdevops9_uIDFfsTn-HpbHpiDOoR1gqSIcF23Z8FhV_1FbNXxdoaqTs5Kg1LWpbnRodC2Hq4RqdmO9QksazRRbjwBCc00WFMNyhxN7C68Kco9wxrHLJ7j_Us0-SwdyQzRwhAlDJ2peH6PzVoic8jK0-Xh8FwAHaLWj797NDKftSfPgV5JCWmCcoFQNN5RQIghOPg6hDThF4eJi61jpPkAjx7ECu5Zm9YvVppEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارومیه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65805" target="_blank">📅 05:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65804">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdFiQYUszNioBEQrCXCUB_tijZjmTzyvRDXs_BcLFR60fWTPbpfB0nAZmCNYz0_ZBO74HwMyiBXCsB-wzoKTy11mwuk75-mJoKbKu30JQIYhOALU21Y2tfkTNzT4iqa2eTi2r31irHY9GNEmenvosTnO9J4KN4Fw7FsDEYYVt5ZK8oxLyTpf8GkcF0OYUBu1FRRCSqODrmhBFLfJfFEA8puTgKCTSR9OlHovjmHi9x7rsO8r9EjIvhFM_V2RL_jTl-irtMNYihSq_TAnZTkp25D6Gx-WBQ-oFXdbbjFP8u2qhKkOzDBrwFY4wlmVAMlHXJXXIbTQgzDmzEalXCF31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65804" target="_blank">📅 05:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSpYQUPAacwS71c3-C0eJSgqkRJO7-LHNDzk2zPwIGxJ-u3_8Jd2VevOPN3SVmudMWH3JJbjNCgL5jhFWWih9xMovQWmMTQTlnK3W_7hVFknXh2RY5jK9FMeXWggYNDAeKpLWpGct_LNmiBwgKhICk-e2MRZmkr9HlLDxRMB8jK8IsTN2NUDCDZOqZaZCHn6zmmlY1mSSzjVpETitFoYaDSZR3zDjGOZvaoQInk2ieVVRIe4-le7_VvhB1tkclhEEL0KWMp3VKLKmVRnSHMWT9hNdizPNRQs0-OtLBcAu4JoXti6HtUP39-2xc4qAn4lu0g5KlLyMVHawWI4Y5HBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زنجان
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65803" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVc956pzV4gVVcBfA5iNHYadxEA_1Cm5wDxa1bwvztdtRvLQBeU10b0e2s4hA5kuSOn8viEqVrYsol8DfXyi-Hj5kzp0mHTK50iHke_L6lHpBwRpTzocNTxJw1KwU4nUR5xwAlensIkyxlhR-H6YPk9nCsHkUop5KiWPUSklI7gl7D4JtRNSACs_Ye-t6YeKwWAYze0iZmCe0I6h2zQJCDVAO05JA6EzqZck6vbz07OfgvfbClJhTBv71HnwR29FiEQo0_TUqKTWLsmLGzNsSawqYfAqsgioHdQ3OVoaYEpTeJ9LPBEe-8n7W3l92b_CksaegXOM9BO899Pr7CMWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون خرم آباد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65802" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین سپاه آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65801" target="_blank">📅 05:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
فیلترشکن پرسرعت و رایگان اسگارد
• نسخه 3.0
متصل با همه اپراتورها
✅
کاملا رایگان
✅
بدون قطعی
✅
بدون محدودیت حجمی
دانلود مستقیم از فروشگاه گوگل پلی
👇🏼
https://play.google.com/store/apps/details?id=com.vpn.esgard</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65800" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65799" target="_blank">📅 03:00 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
